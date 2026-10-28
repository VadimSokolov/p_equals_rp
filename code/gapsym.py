"""The slowest mode of the swap chain on G_N and the board symmetries.
For N = 8..11: correlation of the second eigenvector with its images under
the eight dihedral symmetries, and the spectral gap of the quotient chain
on symmetry orbits, which governs every symmetric observable, in particular
the ground state indicator used by the vertical walk."""
import json, time, sys, math
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
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
def syms(p):
    n = len(p); q = list(p)
    inv = [0] * n
    for i, c in enumerate(p): inv[c] = i
    r = lambda t: tuple(t)
    out = {"id": r(q), "flipcols": r([n - 1 - c for c in q]), "fliprows": r(q[::-1]), "rot180": r([n - 1 - c for c in q[::-1]]),
           "transpose": r(inv), "anti": r([n - 1 - inv[n - 1 - c] for c in range(n)]),
           "rot90": r([n - 1 - inv[c] for c in range(n)][::-1] if False else [n - 1 - inv[n - 1 - c] for c in range(n)][::-1])}
    # rot90 and rot270 explicitly: (i, c) -> (c, n-1-i): row c gets column n-1-i
    rot90 = [0] * n
    for i, c in enumerate(p): rot90[c] = n - 1 - i
    rot270 = [0] * n
    for i, c in enumerate(p): rot270[n - 1 - c] = i
    out["rot90"] = tuple(rot90); out["rot270"] = tuple(rot270)
    return out
res = {}
for n in range(8, 12):
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
    best = max(range(ncomp), key=lambda c: int(((lab == c) & (E == 0)).sum()))
    keep = np.where(lab == best)[0]; kset = {int(k): t for t, k in enumerate(keep)}
    G = A[keep][:, keep]; m = len(keep); npairs = n * (n - 1) // 2
    deg = np.asarray(G.sum(axis=1)).ravel()
    P = G / npairs + sp.diags(1 - deg / npairs); Plazy = 0.5 * (P + sp.identity(m))
    vals, vecs = spl.eigsh(Plazy, k=4, which='LA', tol=1e-9)
    order = np.argsort(-vals); vals = vals[order]; vecs = vecs[:, order]; f = vecs[:, 1]
    # symmetry images
    corr = {}
    for name in ["flipcols", "fliprows", "rot180", "transpose", "anti", "rot90", "rot270"]:
        img = np.array([kset.get(idx.get(syms(states[keep[t]])[name], -1), -1) for t in range(m)])
        ok = img >= 0
        corr[name] = float(np.dot(f[ok], f[img[ok]]) / np.dot(f[ok], f[ok])) if ok.all() else None
    # quotient chain on orbits under the full group (those symmetries that preserve G_N)
    orbit = -np.ones(m, int); norb = 0
    for t in range(m):
        if orbit[t] >= 0: continue
        imgs = syms(states[keep[t]])
        members = set()
        for name, q in imgs.items():
            v = idx.get(q)
            if v is not None and int(v) in kset: members.add(kset[int(v)])
        for u in members: orbit[u] = norb
        norb += 1
    # lumped chain: Q[a,b] = sum over y in b of P[x,y] for x in a (same for all x in a by symmetry)
    rep = np.zeros(norb, int)
    for t in range(m): rep[orbit[t]] = t
    Pc = P.tocsr()
    Qr = []; Qc = []; Qv = []
    for a in range(norb):
        x = rep[a]; row = Pc.getrow(x)
        acc = {}
        for y, w in zip(row.indices, row.data): acc[orbit[y]] = acc.get(orbit[y], 0.0) + w
        for b, w in acc.items(): Qr.append(a); Qc.append(b); Qv.append(w)
    Q = sp.csr_matrix((Qv, (Qr, Qc)), shape=(norb, norb))
    # symmetrise with respect to orbit sizes for eigsh: D^{1/2} Q D^{-1/2} with D = orbit sizes
    sizes = np.bincount(orbit, minlength=norb).astype(float)
    Dh = sp.diags(np.sqrt(sizes)); Dmh = sp.diags(1 / np.sqrt(sizes))
    Qs = 0.5 * (Dh @ Q @ Dmh + sp.identity(norb))
    Qs = 0.5 * (Qs + Qs.T)
    qv = spl.eigsh(Qs, k=3, which='LA', tol=1e-9, return_eigenvectors=False); qv = np.sort(qv)[::-1]
    res[n] = dict(states=int(m), orbits=int(norb), gap_full_nonlazy=float(2 * (1 - vals[1])), gap_sym_nonlazy=float(2 * (1 - qv[1])),
                  relax_full=float(1 / (2 * (1 - vals[1]))), relax_sym=float(1 / (2 * (1 - qv[1]))), corr=corr,
                  eig_top4=[float(1 - v) for v in vals], secs=time.time() - t0)
    print(n, res[n], flush=True)
    json.dump(res, open("gapsym.json", "w"))
print("done")
