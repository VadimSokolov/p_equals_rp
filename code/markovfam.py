"""Divergence from the uniform law on solutions to its projection on the
order k Markov sequential family, D_k = sum_i H(X_i | X_{i-k..i-1}) - log Q(N),
computed exactly from all solutions for N = 8..13. Also the entropy of each
conditional, to see where the information sits."""
import json, math, numpy as np
from collections import Counter
def all_solutions(n):
    out = []; x = [0] * n; cols = [False] * n; d1 = [False] * (2 * n); d2 = [False] * (2 * n)
    def rec(i):
        if i == n: out.append(tuple(x)); return
        for c in range(n):
            if cols[c] or d1[i + c] or d2[i - c + n]: continue
            x[i] = c; cols[c] = d1[i + c] = d2[i - c + n] = True; rec(i + 1); cols[c] = d1[i + c] = d2[i - c + n] = False
    rec(0); return out
def H(counter):
    tot = sum(counter.values()); return -sum(c / tot * math.log(c / tot) for c in counter.values())
def cond_entropy(sols, i, k):
    # H(X_i | X_{i-k..i-1}) = H(X_{i-k..i}) - H(X_{i-k..i-1})
    lo = max(0, i - k)
    joint = Counter(s[lo:i + 1] for s in sols); marg = Counter(s[lo:i] for s in sols)
    return H(joint) - H(marg)
res = {}
for n in range(8, 14):
    sols = all_solutions(n); Q = len(sols); logQ = math.log(Q)
    row = {}
    for k in range(0, n):
        D = sum(cond_entropy(sols, i, k) for i in range(n)) - logQ
        row[k] = float(D)
        if D < 1e-9: break
    # also: divergence for the family that conditions on ALL previous rows but only through a window? no. Report.
    res[n] = dict(Q=Q, logQ=logQ, D=row, nlogn_minus_logQ=float(n * math.log(n) - logQ))
    print(n, Q, {k: round(v, 3) for k, v in row.items()}, flush=True)
json.dump(res, open("markovfam.json", "w"))
print("done")
