# Chapter 39. Sequential Monte Carlo and Feynman Kac Models

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 39. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

How does the theory of sequential Monte Carlo describe the vertical walk with a population of particles? This chapter places the ladder of level sets in the Feynman Kac framework of Del Moral, where the walk is a sequence of potentials and Markov kernels, the particles are resampled at each rung, and the estimate of the normalising constant is unbiased. It states the unbiasedness and central limit theorems for the particle estimate with multinomial resampling and an explicit asymptotic variance, a sum over rungs. It shows how the variance decomposes rung by rung and isolates the contribution of the sampler at each rung, which separates the Bernoulli part of the product estimator from the error of the kernels. It treats adaptive levels chosen by a quantile rule, for which the unbiasedness theorem does not apply directly but consistency and asymptotic normality hold, and genealogies and coalescence of ancestral lines, with the bottom rung of the queens as the place where failure of mixing would show. It explains what this adds to the Yakowitz and nested sampling analyses: a law of large numbers in the number of particles for the whole walk.

## From the literature

The unbiasedness of the particle estimate of the normalising constant and its central limit theorem for Feynman Kac models (Del Moral 2004). Sequential Monte Carlo for rare event estimation with adaptive levels (Cerou, Del Moral, Furon and Guyader 2012). The Chopin and Robert (2010) result for nested sampling is cited for comparison.

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

sequential Monte Carlo, Feynman Kac model, particle filter, particle approximation, multinomial resampling, unbiased normalising constant, central limit theorem, variance decomposition, adaptive levels, multilevel splitting, genealogy, coalescence, Del Moral, rare event estimation
