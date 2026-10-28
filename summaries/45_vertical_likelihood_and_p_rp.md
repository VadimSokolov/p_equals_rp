# Chapter 45. Vertical Likelihood and P = RP

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 45. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter states precisely what vertical likelihood sampling proves about P and RP, what it would prove under natural conjectures, and what the conjectures are. A level set sampler produces near uniform samples from the sublevel sets of an energy. Under the hypothesis that such a sampler exists and consecutive level set ratios are at least inverse polynomial, the vertical likelihood walk with the integer ladder gives an FPRAS for the ground state count, with O(K^2 q epsilon^-2) samples. Applied to the queens energy on partially filled boards this yields NP = RP, a conditional statement whose hypotheses nobody has proved and which the authors regard as unlikely. Unconditionally the chapter records two standard facts: the nested sampling walk locates the single step of an RP algorithm's quantile function with the shrinkage error of nested sampling, and the Boltzmann partition function is the integral of a step function with at most K + 1 steps, with the trapezoidal rule in the quantile coordinate having mean squared error at most V^2 over 2(n+1)(n+2). It then states three conjectures in vertical form (P = RP, prBPP = prP, and a queens conjecture on the absence of a polynomial level set sampler). The authors say explicitly that they do not claim to prove P = RP; the contribution is a viewpoint.

## From the literature

- Nested sampling and the shrinkage estimate (Skilling 2006; Chopin and Robert 2010).
- NP completeness of queens completion (Gent, Jefferson and Nightingale 2017).
- Collapse of NP inside BPP to RP (Ko 1982).
- The hitting set formulation of derandomization (Andreev, Clementi and Rolim 1998).
- The hypothesis that exponential circuit lower bounds imply P = BPP (Impagliazzo and Wigderson 1997).
- One sided versus two sided error (Buhrman and Fortnow 1999).
- The product estimator for counting via self reducibility (Jerrum, Valiant and Vazirani 1986).

## New results

<!-- results:begin -->
- [Conditional FPRAS with an integer ladder from a polynomial level set sampler](../RESULTS.md#conditional_fpras_integer_ladder) (Theorem 45.1, page 193; conditional on a polynomial level set sampler for the energy; every ratio of consecutive level sets is at least 1/q for a polynomial q): A polynomial level set sampler together with inverse polynomial ratios of consecutive level sets gives an FPRAS for the ground state count by running the vertical walk on the integer ladder. New in this book.
- [A polynomial level set sampler for the queens energy gives NP = RP](../RESULTS.md#queens_energy_sampler_implies_np_rp) (Corollary 45.2, page 193; conditional on a polynomial level set sampler for the queens energy on partially filled boards; the ratios of consecutive level sets of the queens energy are at least inverse polynomial): If the queens energy on partial boards admitted a polynomial level set sampler with inverse polynomial rung ratios, there would be an FPRAS for the completion count and hence NP would equal RP. New in this book.
- [Vertical form of the queens conjecture](../RESULTS.md#queens_conjecture_vertical_form) (Conjecture 45.7, page 195; open): The queens energy on partial boards is conjectured to admit no polynomial level set sampler, so that every polynomial time ergodic chain on its level sets mixes superpolynomially somewhere; this is NP differs from RP specialised to the queens. New in this book.
<!-- results:end -->

## Key terms

vertical likelihood, P = RP, conditional theorem, FPRAS, level set sampler, ladder, rung ratio, queens completion, NP = RP, nested sampling, shrinkage, trapezoidal rule, quantile coordinate, step function, hitting set, prBPP = prP, prRP = prP, derandomization conjecture, promise problems.
