# Chapter 20. Simkin's Theorem and the Queenon

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 20. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter explains how Simkin's theorem on the number of N queens solutions is proved and what its constant means. The upper bound on Q(N) comes from an entropy argument: the chain rule for entropy, applied row by row, is refined by conditioning on block occupation numbers on a coarse grid, which leads to a functional on the limit objects called queenons (permutons whose mass in each diagonal strip is at most the width of the strip). The lower bound comes from a random greedy placement analysed by the differential equations method of Wormald, with an absorption step, and the chapter reads this construction as a ladder whose rungs are the rows. It reports the authors' own enumeration of the queenon density at N = 13, which is largest near the midpoints of the edges and smallest in the corners, discusses the constant alpha = 1.942 with Simkin's bounds 1.939 to 1.945, compares it with the independence estimate 1 + 2/3, and examines finite size corrections in Q(N)/N! against data up to N = 27. No new theorem is stated.

## From the literature

- Asymptotics Q(N) = ((1 + o(1)) N e^{-alpha})^N and the queenon (Simkin 2021, published 2023)
- Differential equations method for random greedy processes (Wormald)
- Sanov's theorem and the analogy of the queenon with the Wigner semicircle and the Vershik and Kerov shape
- Jerrum, Valiant and Vazirani self reducibility (1986) as the row by row ladder

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

Simkin's theorem, queenon, permuton, limit shape, entropy chain rule, random greedy algorithm, differential equations method, absorption, Q(N) asymptotics, alpha constant, large deviations, finite size correction, N queens
