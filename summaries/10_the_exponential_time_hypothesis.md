# Chapter 10. The Exponential Time Hypothesis

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 10. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter places the book's program inside fine grained complexity. It defines the exponential time hypothesis (ETH, 3SAT has no 2^{delta n} algorithm) and the strong version (SETH), states the sparsification lemma and its consequences for lower bounds on independent set, clique, dominating set, orthogonal vectors, edit distance and the permanent (through counting ETH), and presents Schöning's random walk algorithm and the PPSZ algorithm as Monte Carlo methods in the exponential regime. The main new statement is a theorem that links ETH and the circuit hardness hypothesis of Impagliazzo and Wigderson to the two halves of the program: under them P = RP = BPP and not equal to NP, and under a randomized ETH every sampler and every FPRAS for completion counts on the Gent, Jefferson and Nightingale boards takes time exponential in the formula size for infinitely many sizes. The chapter also analyses a Schöning type walk for the queens and shows that its bound is worse than exhaustive search, and discusses average case, moderately exponential and approximation routes around ETH.

## From the literature

The exponential time hypothesis (Impagliazzo and Paturi 2001); the sparsification lemma (Impagliazzo, Paturi and Zane 2001); the survey of Lokshtanov, Marx and Saurabh (2011); counting ETH and the permanent (Dell, Husfeldt, Marx, Taslaman and Wahlén 2014); Williams on SETH lower bounds (2005); Schöning's algorithm (1999); the PPSZ algorithm (Paturi, Pudlák, Saks and Zane 2005) with Hertli's analysis (2014); Impagliazzo and Wigderson (1997); Sinclair and Jerrum on approximate counting (1989); Gent, Jefferson and Nightingale on queens completion.

## New results

<!-- results:begin -->
- [ETH and the program (exponential lower bounds for samplers on hard boards)](../RESULTS.md#eth_and_the_program) (Theorem 10.3, page 36; conditional on the hypothesis that the class E of problems decidable in time 2^{O(n)} contains a problem with no circuits of size 2^{epsilon n} for some epsilon > 0 (parts 1 and 2); the exponential time hypothesis (part 2); the randomized exponential time hypothesis, that 3 satisfiability has no randomized algorithm of time 2^{delta n} for some delta > 0 (part 3)): Under the circuit hardness hypothesis of Impagliazzo and Wigderson, P equals RP, and under the exponential time hypothesis as well, P = RP and both differ from NP; under a randomized exponential time hypothesis every sampler and every FPRAS for completion counts of queens boards built from hard formulas needs exponential time for infinitely many sizes. New in this book.
- [A Schoening walk for the queens](../RESULTS.md#schoening_walk_for_the_queens) (Proposition 10.4, page 38; proved): A Schoening type random walk repairing attacking pairs finds a queens completion in expected time at most (2f)^f times a polynomial in the number f of free rows, which is worse than exhaustive search. New in this book.
<!-- results:end -->

## Key terms

exponential time hypothesis, ETH, strong exponential time hypothesis, SETH, randomized ETH, sparsification lemma, fine grained complexity, counting ETH, permanent lower bound, Schöning algorithm, PPSZ, local search for SAT, FPRAS lower bound, sampler lower bound, N queens completion, circuit hypothesis
