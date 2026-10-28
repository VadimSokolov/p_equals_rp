# Chapter 55. A Worked Example: The Eight Queens by Every Method

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 55. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

What do the theorems of the book give as numbers on the eight queens, where everything can be checked by hand? This chapter takes N = 8, with 40320 permutations and 92 solutions, and computes the density of states, the level set probabilities Z_m and ratios, and the staircase quantile function of the Boltzmann likelihood, whose integral is Z = 0.03378. It then runs, on paper, the product estimator (relative variance 0.0406 with 400 samples per rung, compared with the 0.13 coefficient of variation observed), nested sampling with n live points, the Polson and Scott chain on log ordinates, quadrature on the staircase (trapezoid versus stratified midpoint rule), and Wang and Landau flat histogram sampling. It checks the connectivity fact that the 92 solutions and 888 near solutions form one swap component of 980 states, and that the bottom ratio 92/980 equals the measured time fraction at energy zero. It also reports honestly that at N = 8 the Monte Carlo method costs more than enumeration. No new theorem.

## From the literature

Simkin's asymptotic constant for the number of queens configurations (Simkin 2023); nested sampling (Skilling 2006) and its properties (Chopin and Robert 2010); Wang and Landau density of states sampling (Wang and Landau 2001); vertical likelihood Monte Carlo (Polson and Scott 2015); product estimators for counting (Jerrum, Valiant and Vazirani 1986).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

eight queens, 8 queens, density of states, 92 solutions, staircase, quantile function, level set probability, product estimator, annealing ladder, nested sampling, Polson Scott chain, stratified quadrature, trapezoid rule, Wang Landau, flat histogram, near solutions, worked example
