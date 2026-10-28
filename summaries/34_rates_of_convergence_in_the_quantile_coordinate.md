# Chapter 34. Rates of Convergence in the Quantile Coordinate

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 34. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

How fast does integration in the quantile coordinate converge, and why is it faster than naive Monte Carlo? This chapter proves the rate claims made in the vertical likelihood chapter. The integrand is a nonincreasing function on the unit interval, the quantile function of the likelihood, and the estimator is a Riemann sum or trapezoid on n ordered uniform draws. The tool is the exact distribution of uniform spacings. For a smooth integrand the trapezoid on random ordered nodes has mean squared error of order n to the power minus 4, against n to the power minus 1 for the plain average. For a general monotone integrand the left and right Riemann sums bracket the integral and have mean squared error of order log squared n over n squared, because the error is controlled by the largest spacing. For a staircase the rate depends on the number and heights of the steps. The chapter also explains why the original coordinate, of dimension N or N squared for the queens, admits no such rate, and adds a remark on quasi Monte Carlo and low discrepancy sequences. The rates apply only when the quantile function can be evaluated at the nodes, which is the catch of the vertical walk. These bounds are sharpened in the chapters on Yakowitz bounds and exact staircase theory.

## From the literature

The trapezoidal rule on ordered uniform draws and its mean squared error rate for smooth integrands (Yakowitz, Krimmel and Szidarovszky 1978). Trapezoidal Monte Carlo integration with random nodes (Masry and Cambanis 1990). The distribution of uniform spacings and the maximal spacing, of order log n over n, as classical facts.

## New results

<!-- results:begin -->
- [Riemann sums on random grids for monotone integrands](../RESULTS.md#riemann_sums_monotone_log_rate) (Theorem 34.1, page 137; proved): For any monotone integrand the left and right Riemann sums on ordered uniform nodes have mean squared error of order log squared n over n squared, with no smoothness assumed. New in this book.
<!-- results:end -->

## Key terms

rates of convergence, quantile coordinate, uniform spacings, order statistics, Riemann sum, random grid, trapezoidal rule, mean squared error, monotone integrand, staircase, maximal spacing, quasi Monte Carlo, discrepancy, Yakowitz
