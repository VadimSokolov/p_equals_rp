# Chapter 19. Counting as a Rare Event

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 19. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

The chapter turns counting into probability. For a finite set of configurations with an energy whose zero set is the set of solutions, the number of solutions equals the size of the set times the probability that a uniform configuration has zero energy, so counting N queens becomes estimating the rare event probability rho_N = Q(N)/N^N (or Q(N)/N! on permutations). It shows why naive Monte Carlo fails, since the relative variance (1 - rho)/(M rho) forces a sample size of order 1/(epsilon^2 rho), exponential in N, and presents the embedding principle of shrinking the ambient space to the symmetric group. It tabulates the exact density of states N(s), the number of permutations with s attacking pairs, for N = 4 to 9, and introduces the Boltzmann weight, the partition function Z(gamma), and the zero temperature limit that returns the count, so that annealing, Wang and Landau and related methods become counting methods. The chapter also states the central claim of the book, that the quantile function of Monte Carlo links the physicist's entropy of states with the complexity theorist's sharp P.

## From the literature

- Counting as a rare event probability, used for the queens by Diaconis and Holmes (1995) and Rubinstein (2006)
- Embedding the queens in the rooks problem (Rubinstein and Kroese)
- Partition function, microcanonical entropy and the Wang and Landau method of statistical physics

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

counting as rare event, rare event probability, naive Monte Carlo, relative variance, embedding principle, density of states, microcanonical entropy, Boltzmann distribution, partition function, zero temperature limit, simulated annealing, queens energy, attacking pairs
