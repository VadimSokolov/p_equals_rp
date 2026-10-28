# Chapter 40. Bayesian Evidence as Counting

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 40. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

Is Bayesian evidence computation the same problem as counting? Vertical likelihood Monte Carlo was invented for the marginal likelihood, the expectation of the likelihood under the prior, and this chapter closes the loop. The evidence is the integral of the quantile function of the likelihood under the prior, so with an indicator likelihood on a discrete space it is a count over the size of the space, and with a Boltzmann weight it is a partition function. The standard estimators of the evidence are shown to be choices within the vertical framework: the harmonic mean estimator, thermodynamic integration over power posteriors, annealed importance sampling, and nested sampling. Posterior sampling becomes level set sampling by the slice sampling construction, and the complexity of the evidence is that of the level set draw: polynomial for log concave likelihood and prior, and as hard as the counting problem in general. The chapter restates the thesis of the program in Bayesian terms, discusses the horseshoe prior for sparse regression as a heuristic case with no mixing result claimed, and treats model selection over combinatorial model spaces as counting. No new theorem is proved.

## From the literature

Slice sampling with auxiliary variables (Damien, Wakefield and Walker 1999). Nested sampling (Skilling 2006). Vertical likelihood Monte Carlo as a unifying view of evidence estimators (Polson and Scott 2015). Polynomial time sampling from log concave distributions by the ball walk (Frieze, Kannan and Polson 1994; Applegate, Kannan and Polson 1990). The harmonic mean estimator, thermodynamic integration and annealed importance sampling as standard methods.

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

Bayesian evidence, marginal likelihood, Bayes factor, partition function, harmonic mean estimator, thermodynamic integration, power posterior, annealed importance sampling, nested sampling, slice sampling, level set sampling, model selection, horseshoe prior, posterior sampling, counting
