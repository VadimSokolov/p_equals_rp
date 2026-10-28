# Chapter 30. Rubinstein's Cross Entropy Method for Counting

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 30. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter sets Rubinstein's methods for counting beside the vertical walk: the cross entropy method for counting, the Gibbs cloner, stochastic enumeration and Knuth's tree size estimator. Its mathematical content is a theorem on product proposals for the queens: for any importance sampling proposal of product form on the N^N row placements, the relative variance of the estimator of Q(N) is at least exp(N log N - d - log Q(N)) - 1, where d is the total entropy deficit of the one point marginals of the uniform distribution on solutions, so a product family improves on crude Monte Carlo by a factor of at most e^d in the relative second moment. Exact marginals computed for N up to 12 show that d is at most 0.68 nats, and a run of the cross entropy method collapses onto a few placements. The chapter then discusses richer sequential families and the learned sampler question, cloning and generalised splitting as a Feynman Kac estimator, Knuth's estimator as a vertical walk with no chain, and why none of these escapes the NP = RP equivalence.

## From the literature

- Cross entropy method (Rubinstein and Kroese); counting with it (Rubinstein 2006); Gibbs cloner (Rubinstein 2009); stochastic enumeration (Rubinstein 2013)
- Tree size estimator (Knuth 1975); variance reduction for stochastic enumeration (Vaisman and Kroese)
- Generalised splitting (Botev and Kroese)
- Unbiasedness of Feynman Kac particle estimators (Del Moral)

## New results

<!-- results:begin -->
- [Product proposals for the queens](../RESULTS.md#product_proposals_for_the_queens) (Theorem 30.1, page 116; proved): No importance sampling proposal with independent coordinates can beat crude Monte Carlo for counting N queens by more than a factor given by the entropy deficit of the solution marginals, which is small for N up to 12. New in this book.
<!-- results:end -->

## Key terms

cross entropy method, Rubinstein, importance sampling, product proposal, relative variance lower bound, entropy deficit, Kullback Leibler divergence, Gibbs cloner, generalised splitting, stochastic enumeration, Knuth estimator, counting solutions, Monte Carlo counting
