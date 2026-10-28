# Chapter 22. Latin Squares and Other Permutation Counts

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 22. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter surveys counting problems on permutations in which a constraint removes an exponentially large fraction of the N! permutations, and compares their asymptotic constants with that of the queens. It treats derangements and board avoiding permutations, exact by inclusion exclusion through the rook polynomial; Latin squares, whose leading asymptotics log L(n) = n^2 log n - 2 n^2 + o(n^2) follow from the van der Waerden and Bregman permanent inequalities, with the lower order terms open; toroidal queens, which have no solutions unless gcd(N, 6) = 1 and whose count is ((1 + o(1)) N e^{-3})^N, matching upper and lower bounds; and the permanent of a zero one matrix. It explains why the Jerrum, Sinclair and Vigoda approximation scheme for the permanent covers every single permanent of the family but not the queens, whose inclusion exclusion over attacking pairs has alternating signs. It argues that the question about alpha is whether it is the value of a recognisable functional at the queenon, and states no new theorem.

## From the literature

- Number of derangements by inclusion exclusion; rook polynomial (Kaplansky and Riordan)
- Leading asymptotics of Latin squares via van der Waerden's conjecture (Egorychev 1981 and Falikman 1981) and the Bregman bound (Bregman 1973), presented by van Lint and Wilson
- Existence and counting of designs (Keevash); substructures of Latin squares (Kwan, Sah, Sawhney and Simkin)
- Toroidal queens: no solutions unless gcd(N, 6) = 1 (Polya 1918); upper bound (Luria 2017) and matching lower bound (Bowtell and Keevash)
- FPRAS for the permanent of a nonnegative matrix (Jerrum, Sinclair and Vigoda 2004)

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

Latin squares, derangements, rook polynomial, permanent, van der Waerden conjecture, Bregman inequality, toroidal queens, modular queens, permutation counting, inclusion exclusion, Egorychev Falikman, Keevash designs, asymptotic constants
