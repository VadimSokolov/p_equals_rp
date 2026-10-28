# Chapter 56. Towards a Mixing Proof on Unconditioned Boards

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 56. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

Does the swap chain on the bottom level set of the unconditioned N queens mix in polynomial time, and what would a proof need? The chain moves by swapping the columns of two rows and stays inside the set of permutations with at most one attacking pair, restricted to the giant swap component G_N. The chapter states the mixing conjecture, proves elementary facts (reversibility, irreducibility, aperiodicity for N at least 8, and that swapping two rows of a solution creates at most four attacks), reports exact measurements that replace two earlier conjectures (repairable swaps per solution, distance from near solutions to solutions, spectral gap and relaxation times for N = 8 to 12), and proves a reduction by Cheeger's inequality: the mixing conjecture is equivalent to a polynomial lower bound on the conductance of G_N, the expansion conjecture. It discusses canonical paths and comparison with a block chain as possible routes and compares the problem with the KLS conjecture. The mixing and expansion conjectures remain open.

## From the literature

Cheeger's inequality and conductance bounds for reversible chains (Jerrum and Sinclair 1989; Sinclair and Jerrum 1989); the canonical path and comparison methods; the KLS isoperimetric conjecture (Kannan, Lovasz and Simonovits 1997) and its progress by Eldan's stochastic localisation, Chen (2021), Klartag and Lehec (2022) and Klartag (2023).

## New results

<!-- results:begin -->
- [Polynomial mixing of the swap chain on the bottom level set of the queens](../RESULTS.md#swap_chain_mixing_conjecture) (Conjecture 56.1, page 235; open): The swap chain restricted to the giant component of the permutations with at most one attacking pair is conjectured to mix in polynomial time, with the giant component holding almost all solutions. New in this book.
- [Reversibility, irreducibility and aperiodicity of the swap chain on the giant component](../RESULTS.md#swap_chain_basic_facts) (Lemma 56.2, page 235; proved): The swap chain on the giant component is reversible with respect to the uniform law, irreducible and aperiodic from N equal to 8, with off diagonal transition probabilities zero or one over the number of pairs. New in this book.
- [A swap of a solution creates at most four attacks](../RESULTS.md#swap_from_solution_at_most_four) (Lemma 56.3, page 236; proved): Swapping two rows of a solution of the N queens problem leaves at most four attacking pairs. New in this book.
- [Expansion of the bottom level set](../RESULTS.md#expansion_of_the_bottom_level_set) (Conjecture 56.4, page 237; open): The swap graph on the giant component of the near solutions has conductance bounded below by an inverse polynomial in N, which is equivalent to polynomial mixing of the swap chain. New in this book.
- [Expansion of the bottom level set is equivalent to polynomial mixing](../RESULTS.md#expansion_equivalent_to_mixing) (Theorem 56.5, page 237; proved): By Cheeger's inequality, a polynomial lower bound on the conductance of the giant component gives polynomial mixing of the lazy swap chain, and polynomial mixing conversely gives the conductance bound. New in this book.
<!-- results:end -->

## Key terms

swap chain, bottom level set, giant component, mixing time, relaxation time, spectral gap, conductance, Cheeger inequality, expansion conjecture, canonical paths, comparison method, near solutions, transposition walk, N queens, torpid mixing, KLS conjecture
