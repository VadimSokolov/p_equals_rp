# Chapter 59. Lean Statements of the Main Results

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 59. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

Can the main results be stated in a proof assistant? This chapter is an untested sketch, not a machine checked formalization. It writes, in Lean 4 in the style of Mathlib, statements of the Lorenz identity (the layer cake formula in quantile form), the variance bound for the product estimator, the stratified quadrature bound, the main equivalence NP = RP and its sampler forms, and the vertical form of prRP = prP. The text says the code is pseudo Lean, has not been typechecked, leaves several identifiers undefined, and leaves most proofs as sorry. The chapter explains why formalizing is worth doing (it forces the definitions of a polynomial level set sampler, of total variation for a sampler that may fail, and of the promise into the open), comments on how the statements match Mathlib's probability and measure theory, and ends with the state of the project. It proves no mathematical result and verifies none by machine.

## From the literature

Mathlib, the Lean mathematical library (The Mathlib Community 2020); the cited theorems of the main equivalence (Bellare, Goldreich and Petrank 2000; Jerrum, Valiant and Vazirani 1986; Gent, Jefferson and Nightingale 2017) which a formalization would take as axioms.

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

Lean 4, Mathlib, formalization, proof assistant, formal verification, sorry, Lorenz identity, layer cake formula, product estimator, stratified quadrature, main equivalence, prRP, pseudo Lean, untested, not machine checked
