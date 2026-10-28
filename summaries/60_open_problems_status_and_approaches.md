# Chapter 60. Open Problems: Status and Approaches

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 60. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

What is open in the program, and what has moved? This chapter is the working document of the book. For each problem it gives the statement, what is known, what the authors computed while writing, promising approaches and the bearing on the thesis. Problems on the structure of the queens landscape: the limit of N(0)/N(1), connectivity of solutions under swaps, the repair neighbourhood, the finite size correction to Simkin's asymptotics, the queenon and the Lorenz curve, mixing of the bottom rung, a random queens completion model and its threshold, the absence of a thermal phase transition. Problems on the vertical method: optimal vertical weight, rates in the quantile coordinate, two sided promises, hashing versus walking. Derandomization: vertical hitting sets, deterministic level set hitting. Broader program: the Jerrum, Valiant and Vazirani gap, Lean and the queens. Later rounds add the shattering depth of a board (with a rung skipping theorem), the spectral gap, depth growth and Markov window families. A final section records which problems changed status, with the exact computations to N = 13 and N = 17 that support the giant component.

## From the literature

Simkin's asymptotics for the number of queens configurations (Simkin 2023) and the queenon; random generation and approximate counting (Jerrum, Valiant and Vazirani 1986); the permanent (Jerrum, Sinclair and Vigoda 2004); the queens completion reduction (Gent, Jefferson and Nightingale 2017); Wang and Landau (2001) and nested sampling (Skilling 2006) as context for the vertical method.

## New results

<!-- results:begin -->
- [Rung skipping, the walk that starts at a connected level set](../RESULTS.md#rung_skipping) (Theorem 60.20, page 264; conditional on the swap chain on every sublevel set of energy at most j, for j at least m, is irreducible and mixes in polynomial time T; the rung ratios are at least 1/q(N) for a polynomial q; the ratio of the number of ground states to the size of the sublevel set at m is at least 1/p(N) for a polynomial p): If a connected, well mixed sublevel set is reached at some depth m with polynomial rung ratios and a polynomial ground state fraction, the vertical walk need not use the bottom rung and gives an FPRAS for the completion count. New in this book.
- [Shattering depth on hard boards](../RESULTS.md#shattering_depth_conjecture) (Conjecture 60.21, page 266; open): On boards built from hard formulas by the Gent, Jefferson and Nightingale reduction the shattering depth is conjectured to grow linearly in N, so that the ground state ratio at that depth is exponentially small. New in this book.
- [Depth growth on random boards](../RESULTS.md#depth_growth_conjecture) (Conjecture 60.25, page 269; open): On random boards with a fixed number of fixed queens the shattering depth is conjectured to stay bounded, so that the price of rung skipping is inverse polynomial, against the alternatives of logarithmic or linear growth. New in this book.
<!-- results:end -->

## Key terms

open problems, conjectures, status, shattering depth, giant component, near solutions, repair neighbourhood, spectral gap, queenon, finite size correction, random completion model, thermal transition, rung skipping, window families, derandomization problems, Lean formalization
