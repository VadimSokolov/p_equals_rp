# Chapter 46. Approximate Counting in the Polynomial Hierarchy

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 46. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter presents approximate counting within the polynomial hierarchy and places it against the vertical walk. It states Stockmeyer's theorem, that every #P function can be approximated within a factor of 1 plus or minus epsilon by a randomized polynomial time algorithm with an NP oracle (so approximate counting is in BPP with an NP oracle and in the third level of the hierarchy), and explains the proof by pairwise independent hashing, over affine maps on GF(2), and Chebyshev's inequality. The hashing ladder halves the fibre at each step, a vertical walk with ratio one half in which the NP oracle plays the role of the level set sampler. The chapter also discusses Sipser's hashing and the Valiant Vazirani isolation lemma, and the counting of satisfying assignments of a DNF formula by the Karp and Luby sampling scheme, which has an FPRAS because the embedding ratio is at least 1/k. It sketches Toda's theorem that the polynomial hierarchy lies in P with a #P oracle, and locates the queens completion count: exactly #P complete, approximately in BPP with an NP oracle, and with an FPRAS if and only if NP = RP. It states that the ladder length, rung variance and sampling cost are the three sources of difficulty in FPRAS design.

## From the literature

- Approximate counting in BPP with an NP oracle (Stockmeyer 1985).
- Hashing proof that BPP is in the polynomial hierarchy (Sipser 1983, with Lautemann's simplification 1983).
- The isolation lemma, NP is as easy as detecting unique solutions (Valiant and Vazirani 1986).
- FPRAS for DNF counting (Karp and Luby 1983; Karp, Luby and Madras 1989).
- Toda's theorem, the polynomial hierarchy is in P with a #P oracle (Toda 1991).
- Equivalence of approximate counting and almost uniform sampling (Jerrum, Valiant and Vazirani 1986).
- NP completeness of queens completion (Gent, Jefferson and Nightingale 2017).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

approximate counting, polynomial hierarchy, Stockmeyer's theorem, BPP with NP oracle, pairwise independent hashing, universal hashing, Sipser Lautemann theorem, Valiant Vazirani isolation lemma, Karp Luby DNF counting, FPRAS, Toda's theorem, parity class, #P, queens completion, level set sampler, embedding principle.
