# Chapter 5. NP Completeness

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 5. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter explains NP completeness. It sketches the proof of the Cook Levin theorem (SAT and 3SAT are NP complete, by encoding the tableau of a nondeterministic computation as a Boolean formula), works through Karp style reductions to Clique, Subset Sum, Hamiltonian cycle and the travelling salesman problem, and describes the shape of the Gent, Jefferson and Nightingale reduction proving that the N queens completion problem is NP complete and that counting completions is #P complete. It then asks what completeness buys: a licence to look for approximation, heuristics, restricted cases or randomized methods instead of a polynomial algorithm, and, for this book, a precise meaning of rapid mixing of a level set chain for the queens as a statement about all of NP. All results are classical and the chapter only reports the construction of the queens reduction.

## From the literature

The Cook Levin theorem (Cook 1971, Levin 1973); Karp's 21 problems (1972); the Gent, Jefferson and Nightingale proof that queens completion is NP complete (2017); Valiant's #P completeness results (1979).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

NP completeness, Cook Levin theorem, SAT, 3SAT, Karp reductions, Clique, Subset Sum, Hamiltonian cycle, travelling salesman, queens completion problem, NP complete, #P complete counting, gadgets, parsimonious reduction, completeness, NP hard problems, hardness of a chessboard puzzle
