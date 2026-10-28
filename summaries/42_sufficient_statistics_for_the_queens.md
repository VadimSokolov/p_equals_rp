# Chapter 42. Sufficient Statistics for the Queens

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 42. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

Is there a sufficient statistic for the N queens problem, and what does it cost to compute? The chapter answers in three readings. For the Boltzmann family on placements, the energy, the number of attacks, is minimal sufficient for the temperature and the density of states determines the family. For the completion problem, with a partial board as data and the completions as the unknown, the minimal sufficient statistic is the closure, the set of squares occupied by every completion, and the posterior mean matrix, the summary statistic that Jiang and Wong proposed for approximate Bayesian computation, is sufficient too, for every self reducible problem. The cost is the finding: deciding membership in the closure is coNP hard, the exact matrix is sharp P hard, and approximating it to relative accuracy one over N squared in randomized polynomial time is equivalent to NP = RP. Theorems on learned generators show that a uniform generator conditioned on a summary forces sufficiency, that a product over rows pays the mean field gap, and that planted pair training weights boards by their number of completions and rarely shows the hard ones. Forced squares on random boards are tabulated. The chapter states that it does not establish NP = RP, and that no argument in the book does.

## From the literature

Sufficient statistics, the Fisher Neyman factorisation, and minimality (Lehmann and Scheffe 1950). Learning summary statistics for approximate Bayesian computation by a deep network, with the posterior mean as summary (Jiang, Wu, Zheng and Wong 2017). Semi automatic approximate Bayesian computation (Fearnhead and Prangle 2012). Approximate Bayesian computation with Kullback Leibler divergence as discrepancy (Jiang, Wu and Wong 2018). Uniform generation and self reducibility (Jerrum, Valiant and Vazirani 1986).

## New results

<!-- results:begin -->
- [Minimal sufficiency of the closure of a board](../RESULTS.md#closure_minimal_sufficient_completion) (Theorem 42.2, page 175; proved): For the queens completion problem the set of squares occupied by every completion is a minimal sufficient statistic, and the posterior mean matrix is sufficient and reveals it as its entries equal to one. New in this book.
- [Posterior mean sufficiency for completion problems](../RESULTS.md#posterior_mean_sufficient_self_reducible) (Theorem 42.3, page 176; proved): For any completion problem where fixing a forced value changes nothing, including every self reducible problem, the posterior mean is a sufficient statistic and its entries equal to one form a minimal one. New in this book.
- [Hardness of the closure and the posterior mean matrix](../RESULTS.md#hardness_of_sufficient_statistics_queens) (Theorem 42.4, page 176; proved): Deciding membership in the closure is coNP hard, the exact posterior mean matrix is sharp P hard, and approximating it to relative accuracy one over N squared is possible in randomized polynomial time if and only if NP equals RP. New in this book.
- [Learned generators conditioning on a summary statistic](../RESULTS.md#learned_generator_summary_dichotomy) (Theorem 42.5, page 178; proved): A generator that is exactly uniform on completions given a summary forces the summary to be sufficient, a polynomial time version would give NP equal to RP, and a generator that is a product over rows pays at least the mean field gap. New in this book.
- [Planted sampling gives the posterior mean but weights boards by completions](../RESULTS.md#planted_sampling_board_law) (Theorem 42.6, page 180; proved): Training on planted pairs of a uniform solution and a random subset of its queens makes the posterior mean the regression target, but the training boards appear in proportion to their number of completions, so hard boards are rarely seen. New in this book.
- [Learning the posterior mean matrix is equivalent to NP equals RP](../RESULTS.md#learning_problem_equivalent_to_np_rp) (Theorem 42.7, page 181; proved): NP equals RP is equivalent to a randomized polynomial time algorithm, or a uniform polynomial size circuit family, computing the queens posterior mean matrix of every board to relative accuracy one over N squared. New in this book.
<!-- results:end -->

## Key terms

sufficient statistic, minimal sufficient statistic, closure of a board, forced squares, posterior mean matrix, completion problem, self reducible, approximate Bayesian computation, summary statistic, Jiang and Wong, density of states, generative Bayesian computation, planted sampling, mean field gap, coNP hard, sharp P hard, Kolmogorov sufficiency
