# Chapter 58. Rigorous Theorems on P, NP and RP

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 58. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

Which rigorous statements about P, NP and RP does the vertical approach yield? This chapter collects them and says clearly that none resolves P versus NP. The main equivalence says that NP = RP is equivalent to a fully polynomial almost uniform sampler for completions of a partial queens placement, to a sampler for the level sets of the queens energy on partial boards, and to an FPRAS for the number of completions; the proof assembles Bellare, Goldreich and Petrank, Jerrum, Valiant and Vazirani and the Gent, Jefferson and Nightingale reduction. The derandomization half restates the known hitting set formulation: prRP = prP is equivalent to deterministic computation of a point in, or the median of, a dense set, and under the Impagliazzo and Wigderson hypothesis P = RP; this is a coordinate change and not a proof of P = RP. The chapter also proves that no Monte Carlo method decides, approximates or samples the queens completion problem unless NP = RP, a conditional FPRAS with explicit rates in terms of the relaxation time, and a trivial vertical hitting set lemma.

## From the literature

Uniform generation of NP witnesses with an NP oracle (Bellare, Goldreich and Petrank 2000); random generation and approximate counting (Jerrum, Valiant and Vazirani 1986); NP complete queens completion (Gent, Jefferson and Nightingale 2017); P = BPP from exponential circuit lower bounds (Impagliazzo and Wigderson 1997); NP in BPP implies NP = RP (Ko 1982); one sided versus two sided error (Buhrman and Fortnow 1999).

## New results

<!-- results:begin -->
- [The main equivalence, NP = RP if and only if queens completions can be sampled or counted in polynomial time](../RESULTS.md#main_equivalence_np_rp_queens_sampling) (Theorem 58.1, page 242; proved): NP equals RP exactly when the completions of a partial queens placement can be sampled almost uniformly, the level sets of the queens energy can be sampled, or the number of completions can be approximated, in randomized polynomial time. New in this book.
- [Median form of the hitting set characterisation of prRP = prP](../RESULTS.md#derandomization_equivalence_prrp_prp) (Theorem 58.2, page 244; conditional on the extension to promise problems of the Buhrman and Fortnow theorem, that prRP = prP implies prBPP = prP (used only for (1) implies (2))): A restatement on the quantile axis of the known hitting set formulation, saying that promise RP equals promise P exactly when a point with value one, or the median, of a polynomial time Boolean function can be found deterministically under the promise. It rests on the Buhrman and Fortnow theorem, assumed here to extend to promise problems. New in this book.
- [Limits of Monte Carlo for the queens completion problem](../RESULTS.md#limits_of_monte_carlo_for_queens) (Theorem 58.5, page 245; proved): No one sided error decision algorithm, polynomial factor approximation of the completion count, or sampler within constant total variation distance runs in polynomial time unless NP equals RP. New in this book.
- [Conditional FPRAS with explicit rates for the stratified vertical walk](../RESULTS.md#conditional_fpras_explicit_rates) (Theorem 58.6, page 245; proved): For an energy with K plus one levels and reversible lazy level set chains with relaxation time at most t star, the stratified vertical walk estimates the ground state count with a number of chain steps given by an explicit bound, assuming the ratios of the product estimator are bounded below. New in this book.
<!-- results:end -->

## Key terms

main equivalence, NP = RP, FPRAS, almost uniform sampler, level set sampler, prRP = prP, hitting set, derandomization, promise problems, median form, conditional FPRAS, relaxation time, Impagliazzo Wigderson, Bellare Goldreich Petrank, limits of Monte Carlo
