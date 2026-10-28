# Chapter 23. Product Estimators and Annealing

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 23. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter develops the product estimator, the first of the Monte Carlo counting methods. A rare event probability rho = Z_0 is written as a telescoping product of conditional probabilities along a ladder of nested level sets of the energy, each ratio being estimated by ordinary Monte Carlo from samples conditioned on the larger level set. The variance of the product of independent unbiased estimates is computed exactly, and the chapter derives a total sample size of order T^2/epsilon^2 for a ladder of length T whose ratios are bounded below, a ladder of length O(N) for the queens being granted rather than shown. It uses the exact values for N = 8 with the density of states, and shows that the bottom ratio Z_0/Z_1 falls with N (0.094, 0.094, 0.048, 0.038 for N = 8 to 11), so the integer ladder fails the bounded ratio condition. It compares well balanced schedules, the cooling schedules of Stefankovic, Vempala and Vigoda, simulated annealing on the Boltzmann ladder, phase transitions and the cross entropy method. No new theorem is stated.

## From the literature

- Product estimator for counting (Jerrum, Valiant and Vazirani 1986); splitting for rare events (Kahn and Harris 1951)
- Well balanced schedules (Dyer and Frieze); adaptive cooling schedules of length O* of the square root of log Z (Stefankovic, Vempala and Vigoda 2009); paired product estimator (Huber)
- Simulated annealing (Kirkpatrick, Gelatt and Vecchi 1983)
- Cross entropy method (Rubinstein)

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

product estimator, telescoping product, splitting, level sets ladder, relative variance, cooling schedule, simulated annealing, Boltzmann ladder, annealed importance, phase transition, rare event, counting by sampling, partition function ratio
