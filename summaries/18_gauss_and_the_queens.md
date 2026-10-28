# Chapter 18. Gauss and the Queens

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 18. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter introduces the N queens problem, the counting laboratory of the book. It recounts Bezzel's 1848 question, Nauck's 1850 count of 92 solutions for the eight queens board and Gauss's correspondence with Schumacher, fixes notation (a placement is a permutation of {1,...,N} with no two queens on a common diagonal), tabulates Q(N), the number of solutions, and notes the exhaustive count to N = 27 (the Q27 project). It describes the dihedral symmetry of the board, which splits the 92 solutions of the eight queens into 12 orbits, and states Simkin's asymptotics Q(N) = ((1 + o(1)) N e^{-alpha})^N with alpha about 1.942, so that a solution is an exponentially rare event among row placements and permutations. It gives three reasons for choosing the queens: a natural energy (the number of attacking pairs) with a density of states, NP completeness and sharp P completeness of the completion problem (Gent, Jefferson and Nightingale), and enough concreteness to test Monte Carlo counting on exact data. The chapter is background and states no new theorem.

## From the literature

- Counting solutions of the eight queens problem, 92 (Nauck 1850; correspondence of Gauss 1850)
- Exponential growth of Q(N) conjectured (Rivin, Vardi and Zimmermann 1994); upper bound (Luria 2017), lower bound (Luria and Simkin), asymptotics with the constant alpha (Simkin 2021, published 2023)
- Exhaustive count to N = 27 (Preusser and Engelhardt 2017)
- NP completeness of queens completion and sharp P completeness of counting completions (Gent, Jefferson and Nightingale 2017)
- Toda's theorem: the polynomial hierarchy is contained in P with a sharp P oracle (Toda 1991)

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

N queens problem, eight queens, Q(N), Gauss, Nauck, Bezzel, Schumacher, backtracking, dihedral symmetry, Simkin asymptotics, rare event, density of states, completion problem, sharp P completeness, Toda's theorem, Q27 project
