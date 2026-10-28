# Chapter 21. Entropy, Types and the Rate Function of the Queens

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 21. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter gives the information theoretic view of the counting problem. It reviews the method of types and Sanov's theorem, extends types to permutations through block occupancy matrices (permutons as limits), and uses the entropy chain rule for a uniform random solution as a counting tool, which is the skeleton of Simkin's upper bound. It interprets the ladder of the product estimator as a decomposition of the entropy drop from permutations to solutions, about 0.94 N nats or 1.36 N bits, in the light of Shannon's source coding theorem. It defines the rate function I(e) of the number of attacking pairs of a random permutation, computes finite size versions from the exact density of states for N = 8 to 11, and states a conjecture, not proved, that I(e) exists, is convex with I(2/3) = 0 and is given by a variational problem over queenon like densities with I(0) = alpha - 1. It ends with the link between entropy and mixing (modified log Sobolev inequality, random transposition walk) and an accounting of what entropy says about the cost of the program.

## From the literature

- Method of types and Sanov's theorem
- Source coding theorem (Shannon 1948)
- Asymptotics of Q(N) and the constant alpha (Simkin 2021, published 2023), giving the rate I(0) = alpha - 1
- Cutoff of the random transposition walk at N log N / 2 and the log Sobolev analysis of chains on the symmetric group (Diaconis and Shahshahani 1981; Diaconis and Saloff Coste 1993 and 1996)

## New results

<!-- results:begin -->
- [Existence and form of the rate function of the attack count](../RESULTS.md#attack_rate_function_conjecture) (Conjecture 21.1, page 82; open): The large deviation rate function of the number of attacking pairs of a random permutation is conjectured to exist, be convex with its zero at 2/3, and be given near zero by a variational problem over queenon like densities. New in this book.
<!-- results:end -->

## Key terms

method of types, Sanov's theorem, relative entropy, Kullback Leibler divergence, permuton, rate function, large deviations, attack count, queenon, entropy chain rule, source coding, log Sobolev inequality, modified log Sobolev, random transposition
