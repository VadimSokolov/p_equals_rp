"""Rubinstein's cross entropy method for counting N queens solutions with a
product family: row i places its queen in column c with probability v[i,c],
independently. Performance S(x) = number of attacking pairs, where two queens
attack if they share a column or a diagonal. Solutions are the permutations
with S = 0. The CE iteration uses elite quantiles and the KL (maximum
likelihood) update; the count is estimated by importance sampling with the
final v as N^N E_v[1{S=0} f/g] with f uniform on [N]^N.
Reports estimate / exact, the effective sample size, and the KL gap bound."""
import numpy as np, json, time, math
rng = np.random.default_rng(1)
exact = {4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 9: 352, 10: 724, 11: 2680, 12: 14200}
def energy_batch(X):
    n = X.shape[1]; S = np.zeros(len(X), int)
    for i in range(n):
        for j in range(i + 1, n):
            d = np.abs(X[:, i] - X[:, j]); S += (d == 0) | (d == j - i)
    return S
def logg(X, v):
    n = X.shape[1]; return np.log(v[np.arange(n)[None, :], X]).sum(axis=1)
def all_solutions(n):
    out = []; x = [0] * n; cols = [False] * n; d1 = [False] * (2 * n); d2 = [False] * (2 * n)
    def rec(i):
        if i == n: out.append(tuple(x)); return
        for c in range(n):
            if cols[c] or d1[i + c] or d2[i - c + n]: continue
            x[i] = c; cols[c] = d1[i + c] = d2[i - c + n] = True; rec(i + 1); cols[c] = d1[i + c] = d2[i - c + n] = False
    rec(0); return out
res = {}
for n in range(6, 13):
    t0 = time.time(); M = 20000; rho = 0.1; alpha = 0.5
    v = np.full((n, n), 1.0 / n); gamma = None; its = 0
    hist = []
    while True:
        X = np.array([[rng.choice(n, p=v[i]) for i in range(n)] for _ in range(M)]) if False else \
            np.stack([(rng.random((M, 1)) > np.cumsum(v[i])[None, :]).sum(axis=1).clip(0, n - 1) for i in range(n)], axis=1)
        S = energy_batch(X); gamma = max(0, int(np.quantile(S, rho)))
        elite = X[S <= gamma]
        vnew = np.zeros((n, n))
        for i in range(n): vnew[i] = np.bincount(elite[:, i], minlength=n) / len(elite)
        v = alpha * vnew + (1 - alpha) * v; v = np.maximum(v, 1e-12); v /= v.sum(axis=1, keepdims=True)
        its += 1; hist.append((gamma, int((S == 0).sum())))
        if gamma == 0 or its > 60: break
    # final importance sampling estimate with K independent samples
    K = 200000
    X = np.stack([(rng.random((K, 1)) > np.cumsum(v[i])[None, :]).sum(axis=1).clip(0, n - 1) for i in range(n)], axis=1)
    S = energy_batch(X); hit = S == 0
    w = np.where(hit, np.exp(-n * np.log(n) - logg(X, v)), 0.0)   # f/g with f uniform on [N]^N
    est = (n ** n) * w.mean()
    ess = w.sum() ** 2 / (w ** 2).sum() if w.sum() > 0 else 0.0
    relvar = (w ** 2).mean() / w.mean() ** 2 - 1 if w.mean() > 0 else float('inf')
    # entropy deficit of the final marginals and the KL gap bound
    sols = np.array(all_solutions(n)); marg = np.stack([np.bincount(sols[:, i], minlength=n) / len(sols) for i in range(n)])
    Hm = -(np.where(marg > 0, marg * np.log(np.where(marg > 0, marg, 1)), 0)).sum(axis=1); deficit = (np.log(n) - Hm).sum()
    gap = n * math.log(n) - deficit - math.log(exact[n])
    Hv = -(v * np.log(v)).sum(axis=1); vdeficit = (np.log(n) - Hv).sum()
    # how many distinct solutions the final sampler finds
    distinct = len(set(map(tuple, X[hit])))
    res[n] = dict(iterations=its, hit_rate=float(hit.mean()), estimate=float(est), exact=exact[n], ratio=float(est / exact[n]),
                  ess=float(ess), relvar=float(relvar), distinct_solutions=distinct, deficit=float(deficit), kl_gap_bound=float(gap), final_v_deficit=float(vdeficit), best_product_relvar_bound=float(math.exp(gap) - 1),
                  crude_relvar=float(n ** n / exact[n] - 1), secs=time.time() - t0, level_history=hist)
    print(n, res[n], flush=True)
    json.dump(res, open("ce.json", "w"))
print("done")
