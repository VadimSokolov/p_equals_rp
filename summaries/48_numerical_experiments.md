# Chapter 48. Numerical Experiments

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 48. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter reports three numerical experiments on the N queens counting problem. First, the split sampling ladder with population 400, quantile fraction 0.3 and 4N Metropolis swaps per rung, run ten times at each N from 8 to 16, estimating Q(N) within a factor 1.25 of the exact count at every N with coefficient of variation between 0.13 and 0.5 and between five and nine rungs. Second, the Wang Landau algorithm for the whole density of states at N = 10, compared with exhaustive enumeration of all 3,628,800 permutations, with relative error below 1 percent for energies 2 to 7 and 11 percent at the ground state (642 against 724). Third, a reading of the ladder itself, showing that the final ratio Z_0/Z_1 decreases with N and that the bottom rung is the hardest. The chapter states what the experiments do and do not show: the ladder works at sizes where counts can be checked, polynomial cost is by design over N up to 16, and the experiments cannot speak to the limit of large N. These are computations, with exact values known to N = 27, and not proofs of a polynomial algorithm.

## From the literature

- Split sampling and the product estimator of ratios of level sets (Polson and Scott 2015, the authors' earlier paper).
- Wang Landau algorithm for the density of states (Wang and Landau 2001).
- The Metropolis swap chain on permutations.
- Exact counts for the queens problem; the asymptotics of Q(N) (Simkin 2021).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

numerical experiments, split sampling, ladder, Wang Landau, density of states, N queens counting, Metropolis swap chain, product estimator, bottom rung, ground state estimate, multicanonical, flat histogram, exact enumeration, coefficient of variation, simulation study.
