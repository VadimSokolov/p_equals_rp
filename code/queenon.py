"""Queenon tilted proposals. The empirical queen density of all solutions at
N = 13 is interpolated to an N by N board and used to tilt the swap proposal
of the bottom rung chain on {S <= 1}, with a Metropolis Hastings correction so
that the target stays uniform. Compared with uniform swap proposals by the
integrated autocorrelation time of the first row column and the acceptance rate."""
import random, json, time, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
rng = random.Random(5); np.random.seed(5)

def all_solutions(n):
    out = []; x = [0] * n; cols = [False] * n; d1 = [False] * (2 * n); d2 = [False] * (2 * n)
    def rec(i):
        if i == n: out.append(tuple(x)); return
        for c in range(n):
            if cols[c] or d1[i + c] or d2[i - c + n]: continue
            x[i] = c; cols[c] = d1[i + c] = d2[i - c + n] = True
            rec(i + 1)
            cols[c] = d1[i + c] = d2[i - c + n] = False
    rec(0); return out

t0 = time.time()
sols13 = all_solutions(13)
dens = np.zeros((13, 13))
for s in sols13:
    for i, c in enumerate(s): dens[i, c] += 1
dens /= len(sols13)   # row i: probability distribution over columns
print("solutions at 13:", len(sols13), "secs", round(time.time() - t0, 1), flush=True)
# profile of the density along the middle row and the corner for the text
prof = dict(middle_row=[round(v * 13, 3) for v in dens[6]], corner_row=[round(v * 13, 3) for v in dens[0]])
print(prof)

def interp_density(n):
    # bilinear interpolation of the 13 x 13 density onto n x n in [0,1]^2 coordinates
    src = (np.arange(13) + 0.5) / 13
    tgt = (np.arange(n) + 0.5) / n
    def interp1(vals, t):
        return np.interp(t, src, vals)
    tmp = np.array([interp1(dens[i], tgt) for i in range(13)])       # 13 x n
    q = np.array([interp1(tmp[:, j], tgt) for j in range(n)]).T       # n x n
    q = np.maximum(q, 1e-6)
    q /= q.sum(axis=1, keepdims=True)
    return q

def energy(p):
    n = len(p); c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(p[i] - p[j]) == j - i: c += 1
    return c
def delta_energy(p, i, j):
    n = len(p); old = 0; new = 0
    q = list(p); q[i], q[j] = q[j], q[i]
    for k in range(n):
        if k != i and k != j:
            if abs(p[i] - p[k]) == abs(i - k): old += 1
            if abs(p[j] - p[k]) == abs(j - k): old += 1
            if abs(q[i] - q[k]) == abs(i - k): new += 1
            if abs(q[j] - q[k]) == abs(j - k): new += 1
    if abs(p[i] - p[j]) == abs(i - j): old += 1
    if abs(q[i] - q[j]) == abs(i - j): new += 1
    return new - old
def find_solution(n):
    p = list(range(n)); rng.shuffle(p); e = energy(p)
    while e > 0:
        i, j = rng.sample(range(n), 2); d = delta_energy(p, i, j)
        if d <= 0 or rng.random() < 0.05:
            p[i], p[j] = p[j], p[i]; e += d
    return p
def iat(x):
    x = np.array(x, float); x -= x.mean(); v = x.var()
    if v == 0: return float('inf')
    n = len(x); tau = 1.0
    for k in range(1, n // 4):
        c = np.dot(x[:-k], x[k:]) / ((n - k) * v)
        if c < 0.02: break
        tau += 2 * c
    return tau

def run_uniform(p, m, steps):
    n = len(p); e = energy(p); out = []; acc = 0
    for _ in range(steps):
        i, j = rng.sample(range(n), 2); d = delta_energy(p, i, j)
        if e + d <= m:
            p[i], p[j] = p[j], p[i]; e += d; acc += 1
        out.append(p[0])
    return out, acc / steps

def run_tilted(p, m, steps, q):
    n = len(p); e = energy(p); out = []; acc = 0
    iu = np.triu_indices(n, 1)
    c = np.array(p)
    A = q[:, c]                       # A[i,j] = q[i, c_j]
    W = (A * A.T)[iu]; Z = W.sum()
    for _ in range(steps):
        r = rng.random() * Z
        k = int(np.searchsorted(np.cumsum(W), r)); k = min(k, len(W) - 1)
        i, j = int(iu[0][k]), int(iu[1][k])
        d = delta_energy(p, i, j)
        if e + d <= m:
            wf = W[k] / Z
            # reverse weight: q[i,c_i] q[j,c_j] over the new normaliser
            c2 = c.copy(); c2[i], c2[j] = c2[j], c2[i]
            A2 = q[:, c2]; W2 = (A2 * A2.T)[iu]; Z2 = W2.sum()
            wr = q[i, c[i]] * q[j, c[j]] / Z2
            if rng.random() < min(1.0, wr / wf):
                p[i], p[j] = p[j], p[i]; e += d; c = c2; W = W2; Z = Z2; acc += 1
        out.append(p[0])
    return out, acc / steps

res = {}
for n in [12, 16, 20, 24]:
    t0 = time.time(); q = interp_density(n)
    tu = []; tt = []; au = []; at = []
    for rep in range(5):
        p = find_solution(n); xs, a = run_uniform(list(p), 1, 3000 * n); tu.append(iat(xs)); au.append(a)
        xs, a = run_tilted(list(p), 1, 3000 * n, q); tt.append(iat(xs)); at.append(a)
    res[n] = dict(iat_uniform=float(np.mean(tu)), sd_uniform=float(np.std(tu)), acc_uniform=float(np.mean(au)),
                  iat_tilted=float(np.mean(tt)), sd_tilted=float(np.std(tt)), acc_tilted=float(np.mean(at)), secs=time.time() - t0)
    print(n, res[n], flush=True)
    json.dump(dict(profile=prof, results=res), open("queenon.json", "w"))

fig, ax = plt.subplots(1, 2, figsize=(8, 3.3))
im = ax[0].imshow(dens * 13, cmap="Blues", origin="upper")
ax[0].set_title("Empirical queen density, $N=13$ (times $N$)"); plt.colorbar(im, ax=ax[0], fraction=0.046)
ns = sorted(res)
ax[1].errorbar(ns, [res[n]['iat_uniform'] for n in ns], yerr=[res[n]['sd_uniform'] for n in ns], fmt='o-', color='#1f4e79', capsize=3, label='uniform swaps')
ax[1].errorbar(ns, [res[n]['iat_tilted'] for n in ns], yerr=[res[n]['sd_tilted'] for n in ns], fmt='s-', color='#c0392b', capsize=3, label='queenon tilted swaps')
ax[1].set_yscale('log'); ax[1].set_xlabel('$N$'); ax[1].set_ylabel('autocorrelation time (proposals)'); ax[1].legend(fontsize=8)
ax[1].set_title('Bottom rung chain on $\\{S \\leq 1\\}$')
plt.tight_layout(); plt.savefig('fig_queenon.pdf')
print("done")
