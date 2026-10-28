# Chapter 47. Phase Transitions and the Density of States

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 47. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter examines the staircase of the Boltzmann likelihood for the N queens problem and asks where along the quantile axis the difficulty of counting concentrates. For permutations of size N the quantile function has heights e^-s and widths N(s)/N!, where N(s) is the density of states, the number of permutations with s attacking pairs. For N = 8 the chapter reads off the widths from the exact density of states, finds that the steps s = 3 to 6 hold 69 percent of permutations, and that the ratio Z_0/Z_1 = 0.094 is the hardest. A heuristic with independent diagonal pairs gives mean energy about 2N/3 and a Poisson ground step width e^{-2N/3}, larger than Simkin's e^{-0.942 N}, and the deficit is read as the queenon correction. Exact enumeration shows the ratios N(1)/N(0) and N(2)/N(1) growing with N for N = 8 to 11. The chapter discusses where level set sampling by swap moves would fail, namely level sets that are disconnected under local moves on partially filled boards, the mechanism by which NP hardness would appear in Monte Carlo, and states that a failure to mix appears in the quantile coordinate as a wrongly estimated width.

## From the literature

- The asymptotics Q(N) of the number of solutions, e^{-0.942 N} for the ground step width, and the queenon (Simkin 2021).
- Swendsen Wang cluster moves (Swendsen and Wang 1987).
- The Wang Landau flat histogram algorithm for the density of states (Wang and Landau 2001).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

density of states, phase transition, queens staircase, quantile function, Boltzmann likelihood, ground state count, attacking pairs, energy of a permutation, level set, shattering, swap moves, mixing failure, disconnected level sets, Simkin, queenon, Poisson heuristic, exact enumeration, N queens.
