# Chapter 38. Nested Sampling: The Theory

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 38. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

What does the theory of nested sampling say about its accuracy, and how is it a vertical walk? This chapter gives the algorithm precisely: keep n live points drawn from the prior restricted to the region above the current likelihood level, discard the worst, replace it by a draw from the constrained prior, and sum the discarded likelihoods against the geometric grid of prior mass. It proves the shrinkage lemma, that the prior mass above the worst of n live points shrinks by a factor with the Beta(n,1) law of the maximum of n uniforms, independently of the likelihood. From this it derives the error in the number of live points, discusses the choice of that number and the stopping rule, and states consistency and asymptotic normality of the log evidence estimate under the regularity conditions of Chopin and Robert, with an explicit asymptotic variance in terms of the quantile function. It covers variants, importance nested sampling and dynamic nested sampling, and the consistency of the plug in estimate on a staircase. The cost sits in the constrained draws: the number of steps is about n times the log of the reciprocal prior mass, polynomial for the queens, and the constrained draw is the hard part.

## From the literature

Nested sampling (Skilling 2006). Properties of nested sampling, including the central limit theorem for the log evidence (Chopin and Robert 2010). Importance nested sampling and the MultiNest algorithm (Feroz, Hobson, Cameron and Pettitt 2019). Dynamic nested sampling (Higson, Handley, Hobson and Lasenby 2019). Diffusive nested sampling (Brewer, Partay and Csanyi 2011). The Beta law of the maximum of uniforms as a classical fact.

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

nested sampling, live points, shrinkage lemma, Beta distribution, maximum of uniforms, evidence estimation, marginal likelihood, stopping rule, asymptotic normality, consistency, Chopin and Robert, importance nested sampling, dynamic nested sampling, MultiNest, constrained prior sampling
