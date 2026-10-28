# Chapter 33. The Algorithms of Vertical Likelihood Monte Carlo

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 33. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

What is the algorithm behind vertical likelihood Monte Carlo, and can it run in polynomial time? This chapter returns to the paper of Polson and Scott and sets out its algorithms one at a time. The weighted slice sampler adds a weight on the slice variable to the slice sampling joint, so that the choice of a proposal on the sample space is replaced by a choice of a weight on the likelihood axis. Special cases include the harmonic mean estimator and power posteriors, and the construction covers energy level samplers. The score heuristic gives a default weight, the truncated reciprocal of the survival function of the likelihood, and the algorithm is shown to be equivalent to nested sampling. The chapter studies mixing of the chain of likelihood ordinates, which under exact draws moves as a random walk on the log survival scale, and states a conjecture, with a heuristic argument and no complete proof, that this chain mixes in time quadratic in the log of the reciprocal rare event probability, which is order N squared for the queens. A second conjecture says the whole algorithm is polynomial exactly when the level set draws are, so for log concave problems it is polynomial and for the queens completion count it is polynomial if and only if NP = RP. Nothing here proves that equivalence unconditionally.

## From the literature

Slice sampling with auxiliary variables (Damien, Wakefield and Walker 1999). The weighted slice sampler, special cases, default weight, equivalence with nested sampling and the mixing lemma of the paper (Polson and Scott 2015). Nested sampling (Skilling 2006). Sampling from log concave distributions in polynomial time by the ball walk (Frieze, Kannan and Polson 1994).

## New results

<!-- results:begin -->
- [Mixing of the reflected Laplace walk of log ordinates](../RESULTS.md#reflected_walk_mixing_conjecture) (Conjecture 33.1, page 133; open): Under exactness hypotheses, the chain of log ordinates of the weighted slice sampler is modelled by a reflected Laplace walk that mixes in time quadratic in the log of the rare event probability, quadratic in N for the queens. New in this book.
- [Vertical likelihood Monte Carlo is polynomial given polynomial level set draws](../RESULTS.md#vertical_likelihood_polynomial_time_conjecture) (Conjecture 33.2, page 134; open): Granted a polynomially convergent adaptive estimate of the curve Z, vertical likelihood Monte Carlo runs in polynomial time exactly when the restricted prior draws on likelihood level sets do, and for the queens exactly when NP equals RP. New in this book.
<!-- results:end -->

## Key terms

weighted slice sampler, vertical likelihood Monte Carlo, Polson and Scott, slice sampling, auxiliary variable, harmonic mean estimator, power posterior, default weight, score heuristic, nested sampling equivalence, ordinate chain, mixing time, reflected random walk, level set sampler, rare event, polynomial time, log concave
