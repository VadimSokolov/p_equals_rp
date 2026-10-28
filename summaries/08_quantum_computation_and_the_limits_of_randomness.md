# Chapter 8. Quantum Computation and the Limits of Randomness

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 8. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter asks what quantum computation changes for the book's program. It defines BQP and the inclusions BPP in BQP in PP in PSPACE, describes Shor's and Grover's algorithms (with the evidence that NP is not in BQP relative to a random oracle), and amplitude estimation and quantum counting, which estimate a probability to precision epsilon with order 1/epsilon calls instead of 1/epsilon squared. It then reports the quantum Bayesian computation of Polson, Sokolov and Xu and applies the arithmetic to the N queens: a classical rejection cost of about e^{0.942 N} per solution against about e^{0.471 N} for a quantum rejection sampler, and a quadratic gain in each rung of the vertical walk under an overlap hypothesis, while the ladder itself is unchanged. It notes that BQP has no derandomization theorem of the BPP type and concludes that a quantum computer does not change the equivalence of NP = RP with polynomial samplability, which concerns classical randomization.

## From the literature

Shor's factoring algorithm (1994); Grover's search algorithm (1996); Bennett, Bernstein, Brassard and Vazirani on optimality of Grover search; Brassard, Høyer, Mosca and Tapp on amplitude estimation (2000); Adleman, DeMarrais and Huang on BQP in PP; quantum Bayesian computation (Polson, Sokolov and Xu 2023, the authors' own paper).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

BQP, quantum computation, Shor's algorithm, Grover's algorithm, quantum counting, amplitude estimation, quantum rejection sampling, quantum Bayesian computation, quantum speedup for Monte Carlo, quantum walk, derandomization of BQP, N queens
