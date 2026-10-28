# Chapter 6. Circuits and Lower Bounds

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 6. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter surveys Boolean circuit lower bounds, because both P versus NP and P versus BPP would most likely be settled by them. It presents Shannon's counting argument (most functions need circuits of size about 2^n/n) and the contrast with the best explicit bounds, then restricted classes: constant depth circuits (parity not in AC0, switching lemma), monotone circuits (clique, Razborov, Alon and Boppana), and modular gates (Razborov and Smolensky; Williams's separation of NEXP from ACC0). For general circuits the record is 3.1n minus lower order terms. It explains why such techniques stop (the natural proofs barrier), how hardness versus randomness needs exponential circuit lower bounds for a function in E, the partial converses of Impagliazzo, Kabanets and Wigderson and of Kabanets and Impagliazzo, and what this means for the hitting set formulation of P = RP: a derandomization would give a circuit lower bound. No new result is claimed.

## From the literature

Shannon's counting argument (1949) and Lupanov's refinement; Furst, Saxe and Sipser (1984) and Ajtai (1983) on parity and AC0; Håstad's switching lemma (1986); Razborov's monotone lower bound for clique (1985) with Alon and Boppana; Razborov (1987) and Smolensky (1987) on modular gates; Williams (2011) on NEXP and ACC0; Blum (1984), Find, Golovnev, Hirsch and Kulikov (2016) and Li and Yang (2022) on general circuits; Razborov and Rudich on natural proofs; Impagliazzo, Kabanets and Wigderson (2002); Kabanets and Impagliazzo (2004).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

circuit lower bounds, Boolean circuit complexity, Shannon counting argument, AC0, parity, switching lemma, monotone circuits, clique, ACC0, NEXP, explicit hard function, natural proofs, hardness versus randomness, derandomization implies lower bounds, hitting set
