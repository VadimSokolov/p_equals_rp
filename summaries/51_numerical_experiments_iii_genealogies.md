# Chapter 51. Numerical Experiments III: Genealogies

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 51. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter uses the genealogy of a particle system as a diagnostic for shattered level sets. In the split sampling sampler with M = 400 particles, each initial particle carries an ancestor label through selection and mutation, and the number of distinct ancestors among the elite at each rung is recorded. It is compared with a neutral model, A_{t+1} = A_t (1 - (1 - f)^{M/A_t}), in which selection alone causes coalescence. The runs cover unconditioned queens at N = 10, 14, 18 and 22 and randomly conditioned boards at N = 14 and 18. The observed counts track the neutral prediction with a one sided shortfall of 10 to 20 percent in the middle rungs; the bottom rung at N = 18 has 4 ancestors against 8 predicted, which a diagnostic of this resolution cannot distinguish from fluctuation. The chapter notes that the equal family size formula is an upper bound on the neutral expectation, so the comparison cannot separate structure from bias, and that M in the thousands is needed for N above 20. The experiment on hard reduction boards, where an overlap gap structure should show collapse of ancestry, is not done.

## From the literature

- Genealogies and ancestral lineages of interacting particle systems (Del Moral).
- Split sampling and sequential Monte Carlo as particle methods.
- The overlap gap property as a barrier for local algorithms (Gamarnik 2021).
- NP completeness of queens completion (Gent, Jefferson and Nightingale 2017).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

genealogy, ancestral lineage, particle system, sequential Monte Carlo, split sampling, coalescence, neutral model, selection, distinct ancestors, shattered level sets, witch's hat, mixing diagnostic, overlap gap property, queens, randomly conditioned boards, cyclic resampling.
