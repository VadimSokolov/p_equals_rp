# Chapter 29. Rare Event Simulation

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 29. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter reviews the theory of rare event simulation from the vertical point of view, with the queens probability P(S = 0), about e^{-0.942 N} on permutations, as the running example. It covers the relative error criterion and logarithmic efficiency, importance sampling and exponential tilting (Siegmund), splitting (Kahn and Harris, with the analysis of Lagnoux), the zero variance estimator and its approximations, and the work of Diaconis and Holmes, the direct ancestor of the authors' approach to counting the queens. It connects Simkin's theorem to large deviations: the queenon is the large deviations tilt, but an importance density built only from the one point marginals of the queenon would not be the optimal density p(. | S = 0), and no bounded relative error is claimed. It ends with the general principle that importance sampling, tilting, splitting and cross entropy are all schemes for reweighting or rearranging the quantile function so that the rare region is reached. No new theorem is stated.

## From the literature

- Exponential tilting for sums of independent variables (Siegmund 1976)
- Splitting for neutron transport (Kahn and Harris 1951); fixed effort splitting analysis (Lagnoux 2006)
- Counting the queens through a Metropolis chain and a rare event probability (Diaconis and Holmes 1995)
- Sanov's theorem as the model for large deviations

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

rare event simulation, importance sampling, exponential tilting, splitting, relative error, logarithmic efficiency, zero variance estimator, bounded relative error, large deviations, Diaconis and Holmes, queenon, quantile coordinate, Kahn and Harris
