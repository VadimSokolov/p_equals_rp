# Chapter 49. A Cluster Chain for the Queens

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 49. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter designs a Swendsen Wang style cluster chain for the N queens level sets and asks what would make it mix rapidly. The queens energy is a sum of pairwise interactions between row variables, a Potts like model on the complete graph with the extra constraint that columns are distinct. An Edwards Sokal bond augmentation is written for the pairwise weights, and the conditional update of the permutation given the bonds is shown to be a hard sampling problem, unlike the Potts model. The tractable alternative is a block Gibbs chain that resamples a random block of rows uniformly among block permutations keeping the energy at most m. A proposition shows that the block chain is reversible with respect to the uniform distribution on the level set and irreducible when the level set is connected under block moves. The chapter argues, without proof, that for the completion problem the conductance may be exponentially small, since cluster moves of the queens are not correlated with any domain structure. It states a conjecture that the block chain mixes in polynomial time on unconditioned boards and superpolynomially on boards from the Gent, Jefferson and Nightingale reduction.

## From the literature

- Swendsen Wang cluster algorithm (Swendsen and Wang 1987).
- The Fortuin Kasteleyn representation and the Edwards Sokal coupling (Edwards and Sokal 1988).
- NP completeness of queens completion and the reduction from satisfiability (Gent, Jefferson and Nightingale 2017).
- Conductance and mixing time of reversible Markov chains.

## New results

<!-- results:begin -->
- [The block chain is reversible and irreducible when the level set is connected](../RESULTS.md#block_chain_reversible_irreducible) (Proposition 49.1, page 209; proved): The block swap chain with exact conditional resampling of each block is reversible with respect to the uniform law on the level set and irreducible whenever the level set is connected under the allowed block moves. New in this book.
- [Mixing of the block chain on unconditioned and reduction boards](../RESULTS.md#block_chain_mixing_conjecture) (Conjecture 49.2, page 210; open): The block chain on the bottom level set is conjectured to mix in polynomial time on the unconditioned queens and superpolynomially on boards from the reduction applied to hard satisfiability instances. New in this book.
<!-- results:end -->

## Key terms

cluster chain, Swendsen Wang, Edwards Sokal augmentation, Potts model, block Gibbs sampler, level set sampler, queens, permutation, conductance, mixing time, reversibility, irreducibility, torpid mixing, cluster moves, hard core exclusion, reduction boards, conjecture.
