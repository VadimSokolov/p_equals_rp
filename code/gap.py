"""Exact spectral gap of the lazy swap chain on the giant component G_N of
{S <= 1}, N = 8..12, by sparse eigensolver; the sign cut of the second
eigenvector and its conductance (an upper bound on the conductance of G_N)."""
import json, time, sys, math
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
from collections import deque
sys.setrecursionlimit(10000)
def enum_le1(n):
    out = []; x = [0] * n; used = [False] * n
    def rec(i, conf):
        if i == n: out.append(tuple(x)); return
        for c in range(n):
            if used[c]: continue
            k = 0
            for j in range(i):
                if abs(x[j] - c) == i - j:
                    k += 1
                    if conf + k > 1: break
            if conf + k > 1: continue
            x[i] = c; used[c] = True; rec(i + 1, conf + k); used[c] = False
    rec(0, 0); return out
def energy(p):
    n = len(p); c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(p[i] - p[j]) == j - i: c += 1
    return c
res = {}
for n in range(8, 13):
    t0 = time.time(); states = enum_le1(n); idx = {s: i for i, s in enumerate(states)}; M = len(states)
    E = np.array([energy(s) for s in states])
    rows = []; cols = []
    for u, p in enumerate(states):
        for i in range(n):
            for j in range(i + 1, n):
                r = list(p); r[i], r[j] = r[j], r[i]; v = idx.get(tuple(r))
                if v is not None: rows.append(u); cols.append(v)
    A = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(M, M))
    ncomp, lab = sp.csgraph.connected_components(A, directed=False)
    # giant = component with most solutions
    best = max(range(ncomp), key=lambda c: int(((lab == c) & (E == 0)).sum()))
    keep = np.where(lab == best)[0]; G = A[keep][:, keep]; m = len(keep)
    npairs = n * (n - 1) // 2
    deg = np.asarray(G.sum(axis=1)).ravel()
    P = G / npairs + sp.diags(1 - deg / npairs)          # swap chain with rejection
    Plazy = 0.5 * (P + sp.identity(m))
    vals, vecs = spl.eigsh(Plazy, k=3, which='LA', tol=1e-8)
    order = np.argsort(-vals); vals = vals[order]; vecs = vecs[:, order]
    gap = 1 - vals[1]; f = vecs[:, 1]
    # sign cut of the Fiedler vector
    S = f > 0
    if S.sum() > m / 2: S = ~S
    cut = G[S][:, ~S].sum()
    phi = cut / (npairs * S.sum())
    # fraction of solutions on the small side
    Es = E[keep]
    sol_small = int(((Es == 0) & S).sum()); sol_tot = int((Es == 0).sum())
    res[n] = dict(states=int(m), gap_lazy=float(gap), gap_nonlazy=float(2 * gap), relax=float(1 / (2 * gap)),
                  third=float(1 - vals[2]), cut_size=int(S.sum()), cut_edges=int(cut), phi_cut=float(phi),
                  sol_small=sol_small, sol_tot=sol_tot, mean_deg=float(deg.mean()), secs=time.time() - t0)
    print(n, res[n], flush=True)
    json.dump(res, open("gap.json", "w"))
print("done")
