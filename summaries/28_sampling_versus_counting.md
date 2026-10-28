# Chapter 28. Sampling versus Counting

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 28. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter states and explains the equivalence between approximate counting and approximately uniform sampling for self reducible problems, and what it means for the queens. The queens completion problem is self reducible by fixing the column of the first queen. The theorem of Jerrum, Valiant and Vazirani says that for a self reducible NP relation a fully polynomial randomized approximation scheme (FPRAS) exists exactly when a fully polynomial almost uniform sampler exists, and the chapter explains why an FPRAS for an NP complete decision problem gives NP = RP. It lists successes of the method (the permanent of dense matrices and of arbitrary nonnegative matrices, the ferromagnetic Ising model, convex body volume), notes that all have decision versions in P, and discusses torpid mixing for antiferromagnetic models. It then presents the Swendsen and Wang cluster algorithm through the Edwards and Sokal joint distribution, the random cluster model, and slice sampling, proposes a slice sampling form for the repulsive queens interaction, and states that its mixing is unknown. No new theorem is stated.

## From the literature

- Equivalence of approximate counting and almost uniform sampling for self reducible relations (Jerrum, Valiant and Vazirani 1986)
- FPRAS for the permanent of dense matrices (Jerrum and Sinclair 1989), the ferromagnetic Ising model (Jerrum and Sinclair 1993), and arbitrary nonnegative matrices (Jerrum, Sinclair and Vigoda 2004)
- Volume of a convex body (Dyer, Frieze and Kannan 1991)
- Swendsen and Wang cluster algorithm (1987); Edwards and Sokal (1988); random cluster model (Fortuin and Kasteleyn)
- Slice sampling interpretation (Higdon 1998; Damien, Wakefield and Walker 1999)
- Torpid mixing of Swendsen and Wang for the Potts model on the complete graph (Gore and Jerrum 1999)

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

approximate counting versus sampling, self reducibility, FPRAS, almost uniform sampler, Jerrum Valiant Vazirani, permanent, Ising model, Swendsen Wang algorithm, Edwards Sokal, random cluster model, Potts model, slice sampling, torpid mixing, NP = RP
