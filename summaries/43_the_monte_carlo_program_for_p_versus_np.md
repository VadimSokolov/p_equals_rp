# Chapter 43. The Monte Carlo Program for P versus NP

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 43. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter lays out the Monte Carlo program for P versus NP as a chain of five links, each a theorem, a conjecture or an experiment, running from the Lorenz identity for the partition function to the question whether P = NP. The objects are the queens completion problem, the energy given by the number of attacking pairs, the quantile function of the Boltzmann likelihood (a staircase with at most binomial(N,2)+1 steps), the vertical walk, ladder of nested level sets, level set sampler, and the product estimator. The central statement is a conditional FPRAS theorem: if a level set sampler is available, the ladder has at most 2K rungs and consecutive size ratios are at least one half, then the vertical walk with stratified quadrature estimates the ground state count N(0) within relative error epsilon with probability at least 3/4, in time O(K^2 epsilon^-2 C(N, epsilon/K)). The chapter separates what is proved (links one to three), what is conjectured (rapid mixing of the level set chain, and P = RP in vertical form), and what is a sketch (a conditional FPRAS for the unconditioned count Q(N)). It states plainly that it does not claim to resolve P versus NP, and lists the next steps: the shattering depth of reduction boards, a cluster chain with provable properties, and explicit hitting sets.

## From the literature

- NP completeness of queens completion and #P completeness of counting completions (Gent, Jefferson and Nightingale 2017).
- Equivalence of approximate counting and almost uniform sampling for self reducible problems (Jerrum, Valiant and Vazirani 1986).
- Approximate counting is in BPP with an NP oracle (Stockmeyer 1985).
- The derandomization hypothesis P = RP and the circuit lower bound hypothesis (Impagliazzo and Wigderson 1997).
- Quadrature bounds for weighted Monte Carlo integration (Yakowitz, Krimmel and Szidarovszky 1978).
- Nested sampling and its shrinkage error (Skilling 2006; Chopin and Robert 2010).

## New results

<!-- results:begin -->
- [Conditional FPRAS for the vertical walk with stratified quadrature](../RESULTS.md#conditional_fpras_vertical_walk) (Theorem 43.1, page 185; conditional on a level set sampler producing, in time C(N, delta), a sample within total variation delta of uniform on every sublevel set; the ladder hypothesis, that the ladder has at most 2K rungs and consecutive rung size ratios at least one half; for the optimality remark only, for the optimality remark only, that relative error epsilon in the product requires relative error of order epsilon over the square root of K in each rung ratio, which the book assumes and does not prove): Given a level set sampler and a ladder of at most 2K rungs with ratios at least one half, the vertical walk with stratified quadrature approximates the ground state count in time K squared over epsilon squared times the sampler cost, so counting reduces to level set sampling. New in this book.
- [FPRAS for the unconditioned queens count under mixing hypotheses (sketch)](../RESULTS.md#fpras_unconditioned_queens_count_sketch) (Proposition 43.2, page 187; conditional on the sublevel set of energy at most 2 is connected under swaps; polynomial mixing time of the swap chain on every sublevel set of energy at most m for every m at least 2; consecutive ratios of the sublevel sets on the integer ladder are at least inverse polynomial in N; polynomial mixing of the swap chain on the giant component of the sublevel set of energy at most 1, with a membership test and with the giant component holding all but an N to the minus c fraction of the solutions; closing the two gaps the book names in its proof sketch (ratios only inverse polynomial instead of at least one half, and no bound on the size of the giant component relative to the sublevel set)): Under connectivity and polynomial mixing hypotheses for the swap chain on the unconditioned queens, an FPRAS for the number of solutions would follow; the book gives only a sketch with two acknowledged gaps. New in this book.
<!-- results:end -->

## Key terms

Monte Carlo program, P versus NP, NP = RP, P = RP, queens completion, #P complete, FPRAS, almost uniform sampler, self reducibility, Jerrum Valiant Vazirani, vertical walk, level set sampler, ladder, rung ratio, product estimator, stratified quadrature, density of states, Lorenz identity, staircase, shattering depth, mixing conjecture, torpid mixing, hitting set, derandomization.
