"""Two depths for a board: m_s(B), least m with all completions in one swap
component of the conditioned {S <= m}; and m_c(B), least m with {S <= m}
itself connected. Computed for the three severely shattered boards and for
random boards at N = 12, up to m = 4."""
import json, random, time, sys
from collections import deque
rng = random.Random(9)
sys.setrecursionlimit(10000)
def energy(p):
    n = len(p); c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(p[i] - p[j]) == j - i: c += 1
    return c
def enum_le(n, fixed, m):
    x = [-1] * n; used = [False] * n
    for rr, c in fixed.items(): x[rr] = c; used[c] = True
    out = []; free = [q for q in range(n) if q not in fixed]
    def rec(k, conf):
        if k == len(free): out.append(tuple(x)); return
        i = free[k]
        for c in range(n):
            if used[c]: continue
            add = 0
            for j in range(n):
                if x[j] >= 0 and j != i and abs(x[j] - c) == abs(i - j):
                    add += 1
                    if conf + add > m: break
            if conf + add > m: continue
            x[i] = c; used[c] = True; rec(k + 1, conf + add); x[i] = -1; used[c] = False
    rec(0, 0); return out, free
def comps(states, free):
    idx = {s: i for i, s in enumerate(states)}; seen = [False] * len(states); out = []
    for s0 in range(len(states)):
        if seen[s0]: continue
        q = deque([s0]); seen[s0] = True; sols = 0; size = 0
        while q:
            u = q.popleft(); size += 1; p = states[u]
            if energy(p) == 0: sols += 1
            for a in range(len(free)):
                for b in range(a + 1, len(free)):
                    i, j = free[a], free[b]; t = list(p); t[i], t[j] = t[j], t[i]; v = idx.get(tuple(t))
                    if v is not None and not seen[v]: seen[v] = True; q.append(v)
        out.append((size, sols))
    return out
def depths(n, fixed, mmax=4):
    ms = None; mc = None; info = {}
    for m in range(0, mmax + 1):
        st, fr = enum_le(n, fixed, m); c = comps(st, fr)
        n0 = sum(s for _, s in c)
        if n0 == 0: return None
        withsol = [s for _, s in c if s > 0]
        info[m] = dict(size=len(st), comps=len(c), comps_withsol=len(withsol), giant=max(withsol) / n0)
        if ms is None and len(withsol) == 1: ms = m
        if mc is None and len(c) == 1: mc = m
        if mc is not None: break
    return dict(ms=ms, mc=mc, N0=n0, levels=info)
def random_board(n, k):
    while True:
        rows = rng.sample(range(n), k); cols = rng.sample(range(n), k); fixed = dict(zip(rows, cols)); fr = sorted(fixed)
        if all(abs(fixed[fr[a]] - fixed[fr[b]]) != fr[b] - fr[a] for a in range(k) for b in range(a + 1, k)): return fixed
out = {}
boards = {"worst_random_k2": {0: 2, 11: 0}, "search_k3": {11: 10, 10: 5, 7: 11}, "search_k4": {0: 7, 11: 8, 8: 10, 1: 11}}
for name, f in boards.items():
    t0 = time.time(); d = depths(12, f); d['secs'] = time.time() - t0; out[name] = d; print(name, d, flush=True)
    json.dump(out, open("depths.json", "w"))
for k in [2, 3]:
    rows = []; t0 = time.time()
    while len(rows) < 40:
        d = depths(12, random_board(12, k))
        if d is None: continue
        rows.append(d); print(k, len(rows), d['ms'], d['mc'], d['N0'], flush=True)
    out[f"random_k{k}"] = dict(rows=rows, secs=time.time() - t0,
        ms_hist={str(m): sum(1 for r in rows if r['ms'] == m) for m in range(5)},
        mc_hist={str(m): sum(1 for r in rows if r['mc'] == m) for m in range(5)},
        mc_none=sum(1 for r in rows if r['mc'] is None))
    print(k, out[f"random_k{k}"]['ms_hist'], out[f"random_k{k}"]['mc_hist'], out[f"random_k{k}"]['mc_none'], flush=True)
    json.dump(out, open("depths.json", "w"))
print("done")
