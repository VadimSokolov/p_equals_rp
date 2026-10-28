# Chapter 53. Average Case Hardness and the Overlap Gap Property

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 53. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

Does the worst case hardness of the queens completion problem say anything about the random boards on which the Monte Carlo program is tested? This chapter sets the queens against average case complexity: Levin's distributional NP completeness and Heuristica versus Pessiland, the clustering (shattering) transition in random k SAT, and the overlap gap property (OGP) as a geometric obstruction that defeats stable algorithms, including local algorithms, low degree polynomials, approximate message passing and bounded time Langevin dynamics. It defines the overlap of two queens solutions as the fraction of rows on which they agree and argues, from the exact computations of the open problems chapter, that the unconditioned queens have a giant component under swaps through near solutions and therefore no overlap gap at the sizes computed. It conjectures that this holds for every N, and expects, without proof, that boards from the Gent, Jefferson and Nightingale reduction of hard random formulas inherit an overlap gap. It poses a random queens completion model (fix a fraction of queens, find the shattering threshold) as an open problem. The chapter proves nothing new: it is a literature survey with a conjecture and a problem.

## From the literature

Levin's average case complete problems (Levin 1986) and their extension to samplable distributions (Impagliazzo and Levin 1990); the five worlds, Heuristica and Pessiland (Impagliazzo 1995); the random 3 SAT threshold near 4.27 and its proof for large k (Ding, Sly and Sun 2015); the physics prediction of clustering, condensation and freezing (Mezard, Parisi and Zecchina 2002); the rigorous clustering transition and algorithmic barrier (Achlioptas and Coja Oghlan 2008); the overlap gap property and failure of stable algorithms (Gamarnik and Sudan 2014; survey by Gamarnik 2021), with applications to independent sets, spin glasses and random k SAT.

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

average case complexity, distributional problems, Levin completeness, Heuristica, Pessiland, random k SAT, satisfiability threshold, clustering transition, shattering, overlap gap property, OGP, stable algorithms, local algorithms, spin glass, queens completion, random queens model, giant component, swap chain
