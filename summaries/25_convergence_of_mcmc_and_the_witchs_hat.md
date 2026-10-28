# Chapter 25. Convergence of MCMC and the Witch's Hat

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 25. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter gives the statistical side of Markov chain Monte Carlo convergence, because every level set sampler of the book is an MCMC algorithm. It describes the Gibbs sampler and the Metropolis Hastings algorithm as used in Bayesian inference, Peskun's ordering of reversible chains, the convergence theory of Tierney and of Meyn and Tweedie (geometric ergodicity, drift and small sets), a 1996 discussion paper of one of the authors on these conditions, and the diagnostics of Gelman and Rubin and of Geyer. Its central example is the witch's hat, a density on the unit cube with a narrow spike over a flat plateau, for which Gibbs and Metropolis chains can look converged by every diagnostic while being exponentially far from stationarity, because the spike carries most of the mass and is exponentially hard to find. The chapter reads the witch's hat as the bottom rung problem of the queens in miniature. No new theorem is stated.

## From the literature

- Gibbs sampler (Geman and Geman 1984; Gelfand and Smith 1990); Metropolis Hastings algorithm (Metropolis and coauthors 1953; Hastings 1970)
- Peskun ordering (Peskun 1973)
- Convergence theory of Markov chains (Tierney 1994; Meyn and Tweedie)
- Diagnostics (Gelman and Rubin 1992; Geyer 1992)

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

MCMC convergence, Gibbs sampler, Metropolis Hastings, Peskun ordering, geometric ergodicity, drift and minorisation, small sets, Tierney, Meyn and Tweedie, convergence diagnostics, Gelman Rubin, witch's hat, multimodality, bottom rung
