"""Yakowitz type quadrature on the exact queens staircase. The quantile
function of e^{-S} under the uniform distribution on permutations is a
staircase with steps at the cumulative level fractions. We measure the mean
squared error of (i) the trapezoid rule on sorted independent uniforms and
(ii) the stratified midpoint rule, as functions of n, and compare with the
new K free bounds V^2/(2(n+1)(n+2)) and V^2/(4n^2), the asymptotic formula
sum h_k^2/(2 n^2), and the old bounds with K. Also checks the exact single
step formula."""
import json, math, numpy as np
rng = np.random.default_rng(3)
dos = json.load(open("dos.json"))

def staircase(N):
    d = {int(k): v for k, v in dos[str(N)].items()}; tot = math.factorial(N)
    ms = sorted(d); a = []; lam = []; cum = 0.0
    for m in ms:
        cum += d[m] / tot; a.append(cum); lam.append(math.exp(-m))
    # Lambda(s) = lam[j] on (a[j-1], a[j]); jumps at a[0..K-2] with heights lam[j]-lam[j+1]
    return np.array(a), np.array(lam)

def Lam(s, a, lam):
    j = np.searchsorted(a, s, side="right"); j = np.minimum(j, len(lam) - 1); return lam[j]

def Z_exact(a, lam):
    w = np.diff(np.concatenate([[0.0], a])); return float((w * lam).sum())

def trap(n, a, lam):
    U = np.sort(rng.random(n)); U = np.concatenate([[0.0], U, [1.0]]); f = Lam(U, a, lam)
    return float(((U[1:] - U[:-1]) * (f[1:] + f[:-1]) / 2).sum())

def strat(n, a, lam):
    U = (np.arange(n) + rng.random(n)) / n; return float(Lam(U, a, lam).mean())

res = {}
for N in [8, 10]:
    a, lam = staircase(N); Z = Z_exact(a, lam); K = len(lam) - 1
    h = lam[:-1] - lam[1:]; V = lam[0] - lam[-1]; sumh2 = float((h ** 2).sum())
    rows = []
    for n in [10, 20, 50, 100, 200, 500, 1000]:
        T = 4000
        et = np.array([trap(n, a, lam) - Z for _ in range(T)]); es = np.array([strat(n, a, lam) - Z for _ in range(T)])
        rows.append(dict(n=n, trap_mse=float((et ** 2).mean()), trap_bias=float(et.mean()), strat_mse=float((es ** 2).mean()),
                         bound_trap=V ** 2 / (2 * (n + 1) * (n + 2)), asym_trap=sumh2 / (2 * (n + 1) * (n + 2)),
                         old_trap=3 * lam[0] ** 2 * K ** 2 / ((n + 1) * (n + 2)),
                         bound_strat=V ** 2 / (4 * n * n), asym_strat=sumh2 / (4 * n * n), old_strat=K * lam[0] ** 2 / (4 * n * n)))
        print(N, rows[-1], flush=True)
    res[N] = dict(K=K, Z=Z, V=float(V), sumh2=sumh2, rows=rows)

# exact single step check
def single(p, n, T=200000):
    U = np.sort(rng.random((T, n)), axis=1)
    lo = np.where(U <= p, U, 0.0).max(axis=1); hi = np.where(U > p, U, 1.0).min(axis=1)
    D = (lo + hi) / 2 - p; return float((D ** 2).mean()), float(D.mean())
chk = []
for p, n in [(0.3, 5), (0.5, 20), (0.9, 20), (0.05, 50)]:
    mse, bias = single(p, n)
    f = (1 - (n + 2) * p * (1 - p) * (p ** n + (1 - p) ** n)) / (2 * (n + 1) * (n + 2))
    b = ((1 - p) ** (n + 1) - p ** (n + 1)) / (2 * (n + 1))
    chk.append(dict(p=p, n=n, mse_sim=mse, mse_formula=f, bias_sim=bias, bias_formula=b)); print(chk[-1])
res['single'] = chk

# rung experiment: a rung containing k geometric substeps, error against k
rows = []
for k in [1, 2, 5, 10, 20, 50]:
    # staircase on [0,1] with k equal width steps of heights e^{-j}, j=0..k, renormalised to Lambda(0)=1
    a = np.arange(1, k + 1) / (k + 1); a = np.concatenate([a, [1.0]]); lam = np.exp(-np.arange(k + 1))
    Z = Z_exact(a, lam); n = 100; T = 4000
    et = np.array([trap(n, a, lam) - Z for _ in range(T)]); es = np.array([strat(n, a, lam) - Z for _ in range(T)])
    h = lam[:-1] - lam[1:]
    rows.append(dict(k=k, trap_rmse=float(np.sqrt((et ** 2).mean())), strat_rmse=float(np.sqrt((es ** 2).mean())),
                     asym_trap=float(np.sqrt((h ** 2).sum() / (2 * (n + 1) * (n + 2)))), V=float(lam[0] - lam[-1])))
    print(rows[-1], flush=True)
res['rung'] = rows
json.dump(res, open("yak2.json", "w"))
print("done")
