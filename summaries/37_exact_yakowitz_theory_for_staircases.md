# Chapter 37. Exact Yakowitz Theory for Staircases

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 37. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

How accurate is the trapezoidal or stratified rule on a staircase, with constants that do not depend on the number of steps? This chapter gives an exact theory for the quadrature of a nonincreasing quantile function with random ordered nodes. The key is an exact representation of the trapezoid error as an integral of the signed distance to the midpoint of the containing spacing against the jump measure of the integrand. This reduces everything to the moments of that distance, which have closed forms. The consequences are the exact bias and mean squared error for a single step, a bound of order V squared over n squared for any integrand of bounded variation V with no logarithm and no dependence on the number of steps, an asymptotic constant equal to the sum of squared jump heights over 2 n squared for separated steps, and a variance bound over 4 n squared for the stratified rule. For the Boltzmann staircase of the queens, with geometric step heights, the root mean square error of a rung is at most 0.71 over n for the trapezoid and 0.5 over n for the stratified rule, whatever N. Computations at N = 8 and 10 on the exact density of states check the bounds. The chapter says the relative error still carries the unbounded factor of the rung integral, so the cost of the walk is not changed.

## From the literature

The trapezoidal rule on random ordered nodes and its error for smooth integrands (Yakowitz, Krimmel and Szidarovszky 1978). Uniform spacings and their moments as classical facts. Stratified sampling as the standard variance reduction.

## New results

<!-- results:begin -->
- [Trapezoid error as an integral against the jump measure](../RESULTS.md#staircase_error_representation) (Theorem 37.1, page 149; proved): The error of the trapezoidal rule on random ordered nodes equals the integral of the signed distance to the midpoint of the containing spacing against the jump measure of the integrand. New in this book.
- [Moments of the spacing containing a fixed point](../RESULTS.md#spacing_containing_a_point) (Lemma 37.2, page 150; proved): The signed distance from a fixed point to the midpoint of its spacing among uniform nodes has an explicit mean and second moment, bounded by one over twice n plus one and one over twice (n+1)(n+2). New in this book.
- [Exact bias and mean squared error of the trapezoid on one step](../RESULTS.md#trapezoid_single_step_exact) (Theorem 37.3, page 151; proved): For an integrand with a single jump, the bias and mean squared error of the trapezoidal rule on random ordered nodes are given in closed form, with leading mean squared error h squared over 2 n squared. New in this book.
- [Trapezoid on random nodes for bounded variation, no logarithm](../RESULTS.md#trapezoid_bounded_variation_no_log) (Theorem 37.4, page 151; proved): For any integrand of bounded variation V the trapezoid on random ordered nodes has bias at most V over 2(n+1) and mean squared error at most V squared over 2(n+1)(n+2), with no logarithm and no dependence on the number of steps. New in this book.
- [Asymptotic constant of the trapezoid for separated steps](../RESULTS.md#trapezoid_staircase_asymptotic_constant) (Proposition 37.5, page 152; proved): For a staircase with fixed separated jumps the mean squared error of the trapezoid is the sum of squared jump heights over 2 n squared, up to a relative error of order one over n. New in this book.
- [Stratified midpoint rule variance bound free of the number of steps](../RESULTS.md#stratified_rule_free_of_jump_count) (Theorem 37.6, page 153; proved): The stratified rule on n strata has variance at most V squared over 4 n squared for bounded variation V, and sum of squared jump heights over 4 n squared for a staircase with at most one jump per stratum. New in this book.
<!-- results:end -->

## Key terms

exact Yakowitz theory, staircase, trapezoidal rule, random nodes, jump measure, error representation, uniform spacings, midpoint, bounded variation, asymptotic constant, stratified rule, Boltzmann staircase, quadrature error of a rung, density of states
