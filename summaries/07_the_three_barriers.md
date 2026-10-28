# Chapter 7. The Three Barriers

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 7. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter explains why P versus NP has resisted every known technique through three barrier theorems: relativization (Baker, Gill and Solovay: there are oracles making P = NP and P not equal to NP), natural proofs (Razborov and Rudich: a natural property useful against circuits contradicts pseudorandom functions) and algebrization (Aaronson and Wigderson). It sketches why each holds and which known results (interactive proofs, PCP) escape relativization by arithmetization. It then asks where the Monte Carlo program stands. The sampling half would require a mixing time bound for a concrete Markov chain, which is neither relativizing nor natural, although it must go the wrong way relative to the truth. The derandomization half, a deterministic hitting set, is a circuit lower bound by Kabanets and Impagliazzo, so all barriers apply in full. The chapter states that neither half is a proof and that the book claims neither.

## From the literature

Baker, Gill and Solovay on oracles (1975); Razborov and Rudich on natural proofs (1997); Aaronson and Wigderson on algebrization (2009); Savitch's theorem; Håstad, Impagliazzo, Levin and Luby, and Goldreich, Goldwasser and Micali, on pseudorandom functions from one way functions; Shamir's IP = PSPACE (1992); Kabanets and Impagliazzo (2004).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

relativization, oracle separation, Baker Gill Solovay, natural proofs, Razborov Rudich, pseudorandom functions, algebrization, Aaronson Wigderson, barriers to proving P not equal to NP, non relativizing proofs, mixing time bound, hitting set
