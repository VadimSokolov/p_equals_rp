# Chapter 36. Beyond Yakowitz: Higher Order and Stratified Vertical Rules

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 36. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

What can be gained beyond the Yakowitz trapezoid in the quantile coordinate? This chapter gives three improvements, all proved with the same spacing calculus. First, interpolatory rules of degree k on the random grid have expected error of order n to the power minus (k+1) and mean squared error of order n to the power minus 2(k+1) for integrands with k+1 bounded derivatives, a gain of a factor n to the power minus 2 in mean squared error per extra derivative. Second, stratified uniforms, one node in each of n equal strata, give an unbiased estimator whose variance is bounded by the sum of squared oscillations over four n squared, which for a staircase with K jumps is smaller by a factor K than the earlier bracketing bound (a comparison of upper bounds). Third, the nested sampling estimator, with the discarded likelihoods held fixed and the latent positions given the product Beta law, has exact mean and variance, giving an exact error bar for the spacing error rather than removing it. The chapter then asks whether the spacing error of nested sampling can be beaten, and ends with a table of rates. It states what these improvements do and do not buy for counting: they improve the quadrature of a rung and leave untouched the cost of the conditioned draws.

## From the literature

Nested sampling (Skilling 2006). The trapezoidal rule on random nodes (Yakowitz, Krimmel and Szidarovszky 1978). Stratified sampling and the Beta law of the maximum of uniforms as classical facts.

## New results

<!-- results:begin -->
- [Degree k interpolatory rules on random grids](../RESULTS.md#interpolatory_rules_high_order) (Theorem 36.1, page 144; proved): For an integrand with k plus one bounded derivatives, the degree k interpolatory rule on a random grid has mean squared error of order n to the minus 2(k+1). New in this book.
- [Stratified quadrature in the quantile coordinate](../RESULTS.md#stratified_vertical_rule) (Theorem 36.2, page 145; proved): The stratified estimator, with one uniform node in each of n equal strata, is unbiased with variance bounded by the oscillations on the strata, giving root mean square error of order the square root of K over n for a staircase with K jumps. New in this book.
- [Exact mean and variance of the nested sampling estimate under the product Beta law](../RESULTS.md#nested_sampling_exact_mean_variance) (Theorem 36.3, page 146; proved): With the discarded likelihoods held fixed and the latent positions following the product Beta law, the nested sampling estimate has an exact mean and an exact variance formula given by second moments of the positions. New in this book.
<!-- results:end -->

## Key terms

higher order quadrature, interpolatory rule, random grid, stratified sampling, stratified midpoint estimator, variance bound, oscillation, nested sampling estimator, exact mean and variance, Beta law, latent positions, spacing error, table of rates, vertical rules
