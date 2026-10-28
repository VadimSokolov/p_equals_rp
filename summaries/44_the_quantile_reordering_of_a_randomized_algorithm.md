# Chapter 44. The Quantile Reordering of a Randomized Algorithm

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 44. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter turns the machinery of vertical likelihood on the complexity classes. A randomized polynomial time algorithm A(x, r) with random string r has an acceptance probability that is an expectation, and the expectation is the integral of a quantile function. Taking the likelihood to be the indicator of acceptance, the quantile reordering of the algorithm is a step function with a single step, whose location is the acceptance probability p(x). For a language in RP with acceptance probability above one half, deciding membership is evaluating the quantile function at the median, and P = RP is equivalent to a statement that the median of a Boolean function that is either identically zero or true on more than half of the random strings is computable in deterministic polynomial time. The chapter then examines in what sense the nested sampling walk is a hitting set, concluding that it is not: it is a randomized hitting set generator whose randomness sits in the level set sampler, so reordering changes where the randomness lives and does not remove it. It places derandomization of RP and approximate counting of #P on one axis, the density of states as the widths of a monotone step function. It does not resolve P versus RP.

## From the literature

- Counting accepting computations is complete for #P (Valiant 1979).
- The hitting set formulation of derandomization (Andreev, Clementi and Rolim 1998).
- Approximate counting is in BPP with an NP oracle (Stockmeyer 1985) and the Jerrum Valiant Vazirani correspondence between counting and sampling (Jerrum, Valiant and Vazirani 1986).
- The one sided error class RP and amplification of acceptance probability.

## New results

<!-- results:begin -->
- [An RP language is decided by the median of the quantile function of its algorithm](../RESULTS.md#rp_decided_by_quantile_median) (Proposition 44.1, page 190; proved): Deciding a language in RP is the same as evaluating at one half the quantile function of the acceptance probability of its algorithm, that is, taking a median. New in this book.
- [P = RP if and only if medians of RP type Boolean functions are computable in P](../RESULTS.md#p_equals_rp_iff_medians) (Theorem 44.2, page 190; proved): P equals RP exactly when the median can be computed deterministically in polynomial time for every polynomial time Boolean function that, on every input, is either identically zero or true on more than half of the random strings. New in this book.
<!-- results:end -->

## Key terms

quantile reordering, randomized algorithm, acceptance probability, Lorenz curve, quantile function, step function, RP, P = RP, median of a Boolean function, promise, derandomization, hitting set, pseudorandom generator, level set sampler, nested sampling, density of states, #P, approximate counting, queens.
