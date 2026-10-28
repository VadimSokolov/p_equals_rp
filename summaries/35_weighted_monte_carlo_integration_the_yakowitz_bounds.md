# Chapter 35. Weighted Monte Carlo Integration: The Yakowitz Bounds

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 35. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

What is the exact error of the trapezoidal rule on random nodes, and what does it give for the staircases that arise in counting? This chapter gives the full Yakowitz theory for weighted Monte Carlo integration in the quantile coordinate. It sets up the integral of a nonincreasing quantile function by ordered uniform nodes, derives the exact moments of uniform spacings, and proves the Yakowitz, Krimmel and Szidarovszky trapezoidal theorem for twice continuously differentiable integrands with explicit constants: expected absolute error of order n to the power minus 2 and mean squared error of order n to the power minus 4. It extends the analysis to Lipschitz integrands and to bounded variation, with a logarithmic factor from the maximal spacing, and to staircases with K jumps, where the left and right Riemann sums bracket the integral and the root mean square error is of order K times the top height over n. The last section applies the bounds to the vertical walk and says exactly which part of its error they control: the quadrature error on one rung, and not the error of the conditioned draws or of the product across rungs. The staircase bounds carry a factor K that a later chapter removes.

## From the literature

The trapezoidal theorem with mean squared error of order n to the power minus 4 for smooth integrands (Yakowitz, Krimmel and Szidarovszky 1978). Moments of uniform spacings as classical facts.

## New results

<!-- results:begin -->
- [Trapezoid rule on random nodes for Lipschitz and bounded variation integrands](../RESULTS.md#trapezoid_lipschitz_and_bv_bounds) (Theorem 35.2, page 141; proved): The trapezoid rule on ordered uniform nodes has mean squared error of order 1 over n squared for Lipschitz integrands and of order log squared n over n squared for bounded variation or monotone integrands. New in this book.
- [Bracketing Riemann sums and trapezoid for a staircase with K jumps](../RESULTS.md#staircase_bracketing_bound) (Theorem 35.3, page 142; proved): For a staircase with K jumps the left and right Riemann sums bracket the integral and have mean squared error at most a constant times lambda one squared K squared over n squared, which Chapter 37 later improves. New in this book.
<!-- results:end -->

## Key terms

Yakowitz bounds, weighted Monte Carlo integration, trapezoidal theorem, uniform spacings, Lipschitz integrand, bounded variation, monotone integrand, staircase, Riemann sums, random grid, mean squared error, quantile coordinate, quadrature error of a rung
