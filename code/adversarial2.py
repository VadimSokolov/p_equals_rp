"""For the worst boards found by adversarial.py: is the level set {S <= 2}
of the conditioned board connected under swaps of the free rows, and what is
the ratio N(0) / N(<= 2)? Also the swap chain run on {S <= 1} from one
solution: fraction of solutions it visits."""
import json, random, time
from collections import deque
rng = random.Random(3)
r = json.load(open("adversarial.json"))

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

# reconstruct the worst random boards by re-searching is expensive; use the two searched boards and
# a fresh scan for worst random k = 2 board at N = 12
def random_board(n, k):
    while True:
        rows = rng.sample(range(n), k); cols = rng.sample(range(n), k); fixed = dict(zip(rows, cols)); fr = sorted(fixed)
        if all(abs(fixed[fr[a]] - fixed[fr[b]]) != fr[b] - fr[a] for a in range(k) for b in range(a + 1, k)): return fixed
boards = {"search_12_3": {int(a): b for a, b in r["search_12_3"]["fixed"].items()},
          "search_12_4": {int(a): b for a, b in r["search_12_4"]["fixed"].items()}}
worst = None
for inst in range(300):
    f = random_board(12, 2); st, fr = enum_le(12, f, 1); c = comps(st, fr); n0 = sum(s for _, s in c)
    if n0 == 0: continue
    g = max(s for _, s in c) / n0
    if worst is None or g < worst[0]: worst = (g, f)
boards["random_12_2"] = worst[1]
out = {}
for name, f in boards.items():
    n = 12; st1, fr = enum_le(n, f, 1); c1 = comps(st1, fr); st2, _ = enum_le(n, f, 2); c2 = comps(st2, fr)
    n0 = sum(s for _, s in c1)
    out[name] = dict(fixed={str(a): b for a, b in f.items()}, N0=n0, N1=len(st1) - n0, N2=len(st2) - len(st1),
                     comps1=len([1 for _, s in c1 if s > 0]), giant1=max(s for _, s in c1) / n0,
                     comps2_total=len(c2), comps2_withsol=len([1 for _, s in c2 if s > 0]), giant2=max(s for _, s in c2) / n0,
                     ratio02=n0 / len(st2))
    print(name, out[name], flush=True)
json.dump(out, open("adversarial2.json", "w"))
