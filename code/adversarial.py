"""Adversarial conditioning. Random partial boards (k queens, not necessarily
from a solution) at N = 12 and 13: distribution of the number of solution
components of the conditioned level set {S <= 1} under swaps of the free rows,
and a greedy adversarial search that moves one fixed queen at a time to
maximise the number of solution components."""
import random, json, time, sys
from collections import deque
rng = random.Random(2026)

def energy(p):
    n = len(p); c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(p[i] - p[j]) == j - i: c += 1
    return c

def enum_le1(n, fixed):
    x = [-1] * n; used = [False] * n
    for r, c in fixed.items(): x[r] = c; used[c] = True
    fr = sorted(fixed); base = 0
    for a in range(len(fr)):
        for b in range(a + 1, len(fr)):
            if abs(fixed[fr[a]] - fixed[fr[b]]) == fr[b] - fr[a]: base += 1
    if base > 1: return []
    out = []; free = [r for r in range(n) if r not in fixed]
    def rec(k, conf):
        if k == len(free): out.append(tuple(x)); return
        i = free[k]
        for c in range(n):
            if used[c]: continue
            add = 0
            for j in range(n):
                if x[j] >= 0 and j != i and abs(x[j] - c) == abs(i - j):
                    add += 1
                    if conf + add > 1: break
            if conf + add > 1: continue
            x[i] = c; used[c] = True; rec(k + 1, conf + add); x[i] = -1; used[c] = False
    rec(0, base); return out

def components(n, states, free):
    idx = {s: i for i, s in enumerate(states)}
    seen = [False] * len(states); comps = []
    for s0 in range(len(states)):
        if seen[s0]: continue
        q = deque([s0]); seen[s0] = True; sols = 0; size = 0
        while q:
            u = q.popleft(); size += 1; p = states[u]
            if energy(p) == 0: sols += 1
            for a in range(len(free)):
                for b in range(a + 1, len(free)):
                    i, j = free[a], free[b]
                    r = list(p); r[i], r[j] = r[j], r[i]; v = idx.get(tuple(r))
                    if v is not None and not seen[v]: seen[v] = True; q.append(v)
        comps.append((size, sols))
    return comps

def analyse(n, fixed):
    free = [r for r in range(n) if r not in fixed]
    states = enum_le1(n, fixed)
    comps = components(n, states, free)
    n0 = sum(s for _, s in comps); n1 = len(states) - n0
    withsol = sorted([s for _, s in comps if s > 0], reverse=True)
    return dict(N0=n0, N1=n1, comps=len(withsol), giant=(withsol[0] / n0 if n0 else 0.0), sizes=withsol[:6])

def random_board(n, k):
    while True:
        rows = rng.sample(range(n), k); cols = rng.sample(range(n), k)
        fixed = dict(zip(rows, cols))
        # reject boards whose fixed queens attack each other
        ok = True
        fr = sorted(fixed)
        for a in range(k):
            for b in range(a + 1, k):
                if abs(fixed[fr[a]] - fixed[fr[b]]) == fr[b] - fr[a]: ok = False
        if ok: return fixed

res = {}
# Part 1: distribution over random boards
for n, ks, inst in [(12, [2, 3, 4, 5], 300), (13, [3, 4, 5], 150)]:
    for k in ks:
        t0 = time.time(); rows = []
        while len(rows) < inst:
            fixed = random_board(n, k)
            a = analyse(n, fixed)
            if a['N0'] == 0: continue
            rows.append(a)
        multi = sum(1 for r in rows if r['comps'] > 1)
        res[f"{n}_{k}"] = dict(N=n, k=k, instances=len(rows),
            mean_N0=sum(r['N0'] for r in rows) / len(rows),
            frac_multi=multi / len(rows),
            mean_comps=sum(r['comps'] for r in rows) / len(rows),
            max_comps=max(r['comps'] for r in rows),
            mean_giant=sum(r['giant'] for r in rows) / len(rows),
            min_giant=min(r['giant'] for r in rows),
            worst=min(rows, key=lambda r: r['giant']),
            small_multi=sum(1 for r in rows if r['comps'] > 1 and r['N0'] <= 10) / max(1, multi),
            secs=time.time() - t0)
        print(n, k, {kk: vv for kk, vv in res[f"{n}_{k}"].items() if kk != 'worst'}, flush=True)
        json.dump(res, open("adversarial.json", "w"))

# Part 2: greedy adversarial search at N = 12, k = 4: maximise comps, tie break by small giant fraction
def score(a):
    return (a['comps'], -a['giant'])
n = 12
for k in [3, 4]:
    t0 = time.time(); best_overall = None
    for start in range(8):
        fixed = random_board(n, k); a = analyse(n, fixed)
        while a['N0'] == 0:
            fixed = random_board(n, k); a = analyse(n, fixed)
        cur = score(a)
        for step in range(60):
            r = rng.choice(list(fixed)); new = dict(fixed); del new[r]
            r2 = rng.choice([x for x in range(n) if x not in new])
            c2 = rng.choice([c for c in range(n) if c not in new.values()])
            new[r2] = c2
            if any(abs(new[u] - new[v]) == abs(u - v) for u in new for v in new if u < v): continue
            b = analyse(n, new)
            if b['N0'] == 0: continue
            if score(b) >= cur: fixed, a, cur = new, b, score(b)
        if best_overall is None or cur > score(best_overall[1]): best_overall = (dict(fixed), a)
        print("search", k, start, a, flush=True)
    res[f"search_{n}_{k}"] = dict(fixed={str(r): c for r, c in best_overall[0].items()}, result=best_overall[1], secs=time.time() - t0)
    json.dump(res, open("adversarial.json", "w"))
print("done")
