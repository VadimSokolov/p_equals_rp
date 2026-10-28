# Chapter 24. Markov Chains and Mixing Times

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 24. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter collects the theory of Markov chain mixing that the vertical walk relies on, since every conditioned draw of the walk is produced by a chain whose mixing time decides whether the walk is polynomial. It covers stationarity, reversibility and the Metropolis chain for the uniform distribution on a level set of the queens (swap two queens, accept if the energy stays below the level), total variation distance and mixing time, the spectral gap, conductance and Cheeger's inequality, canonical paths, coupling, and slow (torpid) mixing caused by bottlenecks. It presents the Frieze, Kannan and Polson isoperimetric analysis of the ball walk for log concave densities, as the template of a mixing proof, and a 1996 discussion paper of one author on geometric ergodicity of Gibbs and Metropolis chains. It closes by stating what mixing means for the thesis: if the mixing time is polynomial at every level the walk is an FPRAS, and for the queens completion count that would give NP = RP, while the authors believe the opposite. No new theorem is stated.

## From the literature

- Spectral gap, conductance and Cheeger's inequality; canonical paths (Sinclair and Jerrum 1989; Jerrum and Sinclair 1989)
- Coupling method for mixing times
- Mixing of the ball walk for log concave densities by isoperimetry (Applegate and Kannan 1991; Frieze, Kannan and Polson 1994)
- Localisation lemma (Lovasz and Simonovits)

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

Markov chain mixing time, spectral gap, conductance, Cheeger inequality, canonical paths, coupling, total variation, reversibility, detailed balance, Metropolis chain, torpid mixing, log concave sampling, ball walk, isoperimetric inequality, rapid mixing
