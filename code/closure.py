"""Forced squares (the closure) of random boards at N = 12, 13: squares
occupied by every completion but not fixed. The closure is the minimal
sufficient statistic of the board for the completion law; the posterior
mean matrix M identifies it as the entries equal to one."""
import random, json
rng = random.Random(21)
def completions(n, fixed):
    x = [-1] * n; used = [False] * n; out = []
    for r, c in fixed.items(): x[r] = c; used[c] = True
    free = [r for r in range(n) if r not in fixed]
    def ok(i, c):
        return all(not (x[j] >= 0 and j != i and abs(x[j] - c) == abs(i - j)) for j in range(n))
    def rec(k):
        if k == len(free): out.append(tuple(x)); return
        i = free[k]
        for c in range(n):
            if used[c] or not ok(i, c): continue
            x[i] = c; used[c] = True; rec(k + 1); x[i] = -1; used[c] = False
    rec(0); return out
def random_board(n, k):
    while True:
        rows = rng.sample(range(n), k); cols = rng.sample(range(n), k); f = dict(zip(rows, cols)); fr = sorted(f)
        if all(abs(f[fr[a]] - f[fr[b]]) != fr[b] - fr[a] for a in range(k) for b in range(a + 1, k)): return f
res = {}
for n in [12, 13]:
    for k in [2, 3, 4, 5, 6]:
        rows = []
        while len(rows) < 100:
            f = random_board(n, k); comp = completions(n, f)
            if not comp: continue
            # forced squares: row i has the same column in all completions
            forced = sum(1 for i in range(n) if i not in f and len(set(s[i] for s in comp)) == 1)
            # entropy of the marginal matrix as an information measure
            rows.append(dict(N0=len(comp), forced=forced))
        res[f"{n}_{k}"] = dict(N=n, k=k, boards=len(rows), mean_N0=sum(r['N0'] for r in rows) / len(rows),
                               frac_with_forced=sum(1 for r in rows if r['forced'] > 0) / len(rows),
                               mean_forced=sum(r['forced'] for r in rows) / len(rows),
                               frac_with_forced_among_multi=(sum(1 for r in rows if r['forced'] > 0 and r['N0'] > 1) / max(1, sum(1 for r in rows if r['N0'] > 1))))
        print(res[f"{n}_{k}"], flush=True)
json.dump(res, open("closure.json", "w"))
