# Chapter 50. Numerical Experiments II: The Bottom Rung

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 50. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter measures the mixing of the swap chain on the bottom level set {S <= 1} of the N queens energy for unconditioned boards, for N in 8, 10, 12, 14, 16, 18, 20, 24, 28 and 32. From a solution found by a min conflicts heuristic, the chain is run for 4000N proposed swaps and the integrated autocorrelation time of the first row column is estimated from six independent runs at each N. The autocorrelation time grows from 59 swaps at N = 8 to about 900 at N = 32, with a power law fit of exponent 1.76. The fraction of time at energy zero, an estimate of the bottom ratio Z_0/Z_1, falls from 0.094 to about 0.015, with the product with N between 0.4 and 0.75, consistent with decay like 1/N and no positive limit. The chapter extrapolates a cost near N^5 for the whole vertical walk on unconditioned boards, explicitly as an extrapolated estimate and not a demonstrated polynomial algorithm. It says that nothing here concerns hard reduction boards, where the NP hardness would sit, and proposes running the chain on boards from the Gent, Jefferson and Nightingale reduction as the next experiment.

## From the literature

- NP completeness of queens completion (Gent, Jefferson and Nightingale 2017).
- Integrated autocorrelation time as a measure of Markov chain mixing.
- Min conflicts heuristic for constraint satisfaction.

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

numerical experiments, autocorrelation time, integrated autocorrelation, swap chain, bottom rung, level set, mixing time, polynomial mixing, power law fit, min conflicts, bottom ratio, queens, N queens, mixing conjecture, reduction boards, Monte Carlo cost.
