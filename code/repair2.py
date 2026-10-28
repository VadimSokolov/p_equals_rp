"""Near solutions in the giant component: distance to the nearest solution
along swaps inside {S <= 1}, and the fraction with a solution as a direct
swap neighbour. Also the degree distribution of the solution graph H_N
(two step neighbours through one near solution)."""
import json, time, sys
from collections import deque, Counter
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
for n in range(8, 14):
    t0 = time.time(); states = enum_le1(n); idx = {s: i for i, s in enumerate(states)}; M = len(states)
    E = [energy(s) for s in states]
    def nbrs(u):
        p = states[u]
        for i in range(n):
            for j in range(i + 1, n):
                r = list(p); r[i], r[j] = r[j], r[i]; v = idx.get(tuple(r))
                if v is not None: yield v
    # giant component: component with the most solutions
    comp = [-1] * M; best = (-1, -1)
    for s0 in range(M):
        if comp[s0] >= 0: continue
        cid = s0; q = deque([s0]); comp[s0] = cid; sols = 0
        while q:
            u = q.popleft(); sols += (E[u] == 0)
            for v in nbrs(u):
                if comp[v] < 0: comp[v] = cid; q.append(v)
        if sols > best[0]: best = (sols, cid)
    giant = best[1]
    # multi source BFS from solutions in the giant component
    dist = [-1] * M; q = deque()
    for u in range(M):
        if E[u] == 0 and comp[u] == giant: dist[u] = 0; q.append(u)
    while q:
        u = q.popleft()
        for v in nbrs(u):
            if dist[v] < 0: dist[v] = dist[u] + 1; q.append(v)
    dd = Counter(dist[u] for u in range(M) if comp[u] == giant and E[u] == 1)
    near_in_giant = sum(dd.values())
    # degree of H_N: solutions reachable in two steps through a near solution
    degs = []
    for u in range(M):
        if E[u] != 0 or comp[u] != giant: continue
        seen = set()
        for v in nbrs(u):
            if E[v] == 1:
                for w in nbrs(v):
                    if E[w] == 0 and w != u: seen.add(w)
        degs.append(len(seen))
    degs.sort()
    res[n] = dict(near_in_giant=near_in_giant, dist=dict(sorted(dd.items())), frac_dist1=dd[1] / near_in_giant,
                  maxdist=max(dd), deg_mean=sum(degs) / len(degs), deg_min=degs[0], deg_median=degs[len(degs) // 2], deg_max=degs[-1],
                  sols_in_giant=len(degs), secs=time.time() - t0)
    print(n, res[n], flush=True)
    json.dump(res, open("repair2.json", "w"))
print("done")
