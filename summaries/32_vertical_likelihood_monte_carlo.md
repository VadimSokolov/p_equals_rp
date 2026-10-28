# Chapter 32. Vertical Likelihood Monte Carlo

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 32. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

Can an expectation over an astronomically large space, such as the count of N queens solutions, be turned into a one dimensional integral that Monte Carlo can attack, and what does that say about derandomizing RP? This chapter develops vertical likelihood Monte Carlo, the technical core of the book. The Lorenz identity writes the evidence Z, the expectation of a nonnegative likelihood under a prior, as the integral over the unit interval of the quantile function of the likelihood. Vertical importance sampling puts a density on the quantile axis, and the choice of that density is the choice of an annealing schedule. The chapter shows how nested sampling, split sampling, the Wang Landau algorithm, the multicanonical and 1/k ensembles, and energy domain samplers sit in one framework, and it explains why Yakowitz type trapezoidal rules on ordered uniforms converge faster than naive Monte Carlo when the quantile function can be evaluated. It states plainly that sampling from the prior restricted to a likelihood level set is an oracle, as hard for the queens as NP = RP. It then reorders a randomized algorithm: the acceptance probability of an RP algorithm is a single step quantile function, and P = RP is restated as a question about medians of promise Boolean functions. The reordering relocates the randomness and does not derandomize anything, and no proof of P = RP is claimed.

## From the literature

The Lorenz identity, that the mean of a nonnegative variable is the integral of its quantile function (Lorenz 1905, concentration curve). The trapezoidal rule on ordered uniform draws and its fast rate for smooth integrands (Yakowitz, Krimmel and Szidarovszky 1978; Masry and Cambanis 1990). Slice sampling with auxiliary variables (Damien, Wakefield and Walker 1999). Nested sampling (Skilling 2006). Split sampling (Birge, Chang and Polson 2013). The multicanonical sampler (Berg and Neuhaus 1991), the 1/k ensemble (Hesselbo and Stinchcombe 1995) and the Wang Landau algorithm (Wang and Landau 2001). Vertical likelihood Monte Carlo and its unification of energy level samplers (Polson and Scott 2015). Counting accepting computations is complete for sharp P (Valiant 1979). Hitting sets as the known formulation of P = RP.

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

vertical likelihood Monte Carlo, Lorenz identity, quantile function, survival function, vertical importance sampling, nested sampling, split sampling, Wang Landau, multicanonical, 1/k ensemble, density of states, energy domain sampler, concentration function, quantile reordering, RP, medians of Boolean functions, hitting set, derandomization
