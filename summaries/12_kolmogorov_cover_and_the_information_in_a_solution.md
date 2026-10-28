# Chapter 12. Kolmogorov, Cover and the Information in a Solution

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 12. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter uses algorithmic information theory to restate the Monte Carlo and derandomization halves of the program. It compares three descriptions of an N queens solution (a permutation code of about log N! bits, Cover's enumerative code of log Q(N) bits, and Kolmogorov complexity) and proves a coding theorem for the queens: NP = RP holds if and only if the completions of every board can be encoded and decoded in randomized polynomial time with a shared random string at their information content log of the completion count plus a logarithmic term. It reads the Markov window computation and Cover's gambling interpretation in this language, relates the level set ladder to Kolmogorov's structure function (Vereshchagin and Vitányi), states a Kolmogorov form of Sipser's observation that incompressible strings (distinguishing complexity) are witnesses for an RP algorithm with strong error bounds, and connects both halves to the Liu and Pass equivalence between one way functions and time bounded Kolmogorov complexity.

## From the literature

Kolmogorov complexity and the structure function (Kolmogorov 1974; Vereshchagin and Vitányi 2004); Cover's enumerative coding and universal gambling; Sipser's coding lemma and complexity theoretic approach to randomness (1983); Buhrman, Fortnow and Laplante on resource bounded Kolmogorov complexity (2002); Sinclair and Jerrum (1989) and Jerrum, Valiant and Vazirani (1986) on counting and sampling; Liu and Pass on one way functions and Kolmogorov complexity (2020).

## New results

<!-- results:begin -->
- [Coding theorem for the queens](../RESULTS.md#coding_theorem_for_the_queens) (Theorem 12.1, page 47; proved): NP equals RP exactly when the completions of every queens board can be encoded and decoded in randomized polynomial time at their information content, the logarithm of the completion count up to a logarithmic term. New in this book.
<!-- results:end -->

## Key terms

Kolmogorov complexity, algorithmic information, enumerative coding, Cover, coding theorem, arithmetic coding, NP = RP, FPRAS, structure function, minimal sufficient statistic, distinguishing complexity, time bounded Kolmogorov complexity, incompressible strings, derandomization, one way functions, universal gambling, N queens
