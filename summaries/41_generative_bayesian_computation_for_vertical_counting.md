# Chapter 41. Generative Bayesian Computation for Vertical Counting

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 41. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

Can generative Bayesian computation implement vertical counting? Generative Bayesian computation, GBC, represents a posterior or target distribution by a generator, a map from base noise to the target learned from simulated pairs by quantile regression, and the quantile function is also the central object of the vertical walk. This chapter shows how a learned level set generator gives a practical implementation of the ladder of level sets with no Markov chain steps. It states three theorems for finite spaces: the representation theorem, that the quantile function of the likelihood and the generator of each level set exist and are unique up to null sets under a fixed order; the estimation theorem, a Dvoretzky Kiefer Wolfowitz type bound for the empirical quantile function, whose integral is exactly the sample mean; and the amortised ladder theorem, bounding the relative mean squared error of the product estimator when each rung generator has total variation error delta. It says what generators cannot do, since a generator trained on a trapped chain inherits the trap, and ends with a section on monads, Markov categories and functors that places the Monte Carlo and derandomization halves on one axis. The chapter does not prove that a generator can be learned in polynomial time.

## From the literature

Generative Bayesian computation for likelihood free inference (Polson and Sokolov 2023). The Dvoretzky Kiefer Wolfowitz inequality. Monads for computational effects (Moggi 1991) and the Giry monad of probability measures (Giry 1982).

## New results

<!-- results:begin -->
- [Amortised ladder with a fitted level set generator](../RESULTS.md#amortised_ladder_generator_error) (Theorem 41.3, page 170; proved): A ladder run with draws from a fitted level set generator, with equal ratios, has relative mean squared error T(1 - theta)/(theta M) plus a bias term of order T squared delta squared over theta squared, at first order only. New in this book.
<!-- results:end -->

## Key terms

generative Bayesian computation, GBC, generator, quantile regression, quantile function, vertical counting, level set generator, amortised ladder, product estimator, empirical quantile function, Dvoretzky Kiefer Wolfowitz, total variation error, Giry monad, Markov category, functor, likelihood free inference
