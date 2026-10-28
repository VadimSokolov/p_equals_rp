# Chapter 52. Other Laboratories

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 52. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter applies the vertical view to five other hard counting problems: the permanent, the ferromagnetic Ising model, the volume of a convex body, satisfying assignments and linear extensions of a partial order. For each it describes the staircase, the level set sampler and the status of mixing. The permanent is #P complete (Valiant 1979), with an FPRAS by Jerrum and Sinclair 1989 for dense matrices and Jerrum, Sinclair and Vigoda 2004 for all nonnegative matrices. The Ising model has an FPRAS by Jerrum and Sinclair, and the chapter discusses Glauber and Swendsen Wang dynamics, and hardness thresholds by Sly. Convex body volume is handled by Dyer, Frieze and Kannan 1991 with improvements to the running time. For SAT the clustering transition of random constraint satisfaction is the mixing conjecture made concrete. Linear extensions are counted by a coupling argument. The pattern the authors report is that the walk is polynomial exactly for the problems with decision versions in P, while for NP complete problems the bottom rungs shatter into pieces that no efficient chain connects; this is a heuristic reading and not a theorem.

## From the literature

- The permanent is #P complete (Valiant 1979); perfect matching in P (Edmonds 1965).
- FPRAS for the permanent of dense matrices (Jerrum and Sinclair 1989) and for nonnegative matrices (Jerrum, Sinclair and Vigoda 2004); faster cooling schedule (Bezakova, Stefankovic, Vazirani and Vigoda 2008).
- Ising partition function FPRAS (Jerrum and Sinclair 1993).
- Torpid mixing of Swendsen Wang at criticality on the complete graph (Gore and Jerrum 1999).
- Computational hardness beyond the uniqueness threshold (Sly 2010; Sly and Sun 2012); Weitz 2006.
- Randomized volume algorithm (Dyer, Frieze and Kannan 1991); n^4 algorithm (Lovasz and Vempala 2006); Gaussian cooling (Cousins and Vempala 2018); Barany and Furedi 1987 on deterministic hardness; isoperimetry (Kannan, Lovasz and Simonovits 1997).
- Log concave sampling (Applegate and Kannan 1991; Frieze, Kannan and Polson 1994).
- Clustering in random satisfiability (Achlioptas and Coja Oghlan 2008).
- Linear extensions are #P complete (Brightwell and Winkler 1991); coupling mixing (Bubley and Dyer 1997).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

other laboratories, permanent, Ising model, volume of convex body, #SAT, linear extensions, partial order, FPRAS, Jerrum Sinclair, Glauber dynamics, Swendsen Wang, hard core model, uniqueness threshold, Gaussian cooling, clustering transition, random k SAT, coupling, canonical paths, annealing ladder, staircase.
