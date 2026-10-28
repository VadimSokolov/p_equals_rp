# Chapter 57. The Completion Problem

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 57. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

What changes when some queens are already placed? The queens completion problem asks for the number Q(N; X_0) of solutions extending a partial placement X_0, or whether one exists. This chapter shows that the Lorenz identity, the vertical walk, the ladder and the trapezoidal rule go through with the uniform law on the completions in place of the uniform law on permutations, so that only the sampler changes. The hardness changes: completion decision is NP complete and completion counting is sharp P complete (Gent, Jefferson and Nightingale 2017). The chapter describes that reduction from satisfiability (the partial placement encodes the clauses by blocked squares), the self reducibility of completion, which makes search polynomially equivalent to decision and brings in the Jerrum, Valiant and Vazirani sampling to counting equivalence, and the vertical walk on a partial board. It records the consequence that a polynomial level set sampler for completions would give NP = RP, and that failure of the chain on reduction boards is expected.

## From the literature

NP completeness and sharp P completeness of n queens completion (Gent, Jefferson and Nightingale 2017); self reducibility and equivalence of approximate counting and almost uniform sampling (Jerrum, Valiant and Vazirani 1986).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

queens completion, partial placement, conditional counting, NP complete, sharp P complete, #P complete, self reducibility, search to decision, Gent Jefferson Nightingale, reduction from satisfiability, conditioned vertical walk, completions
