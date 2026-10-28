# Chapter 14. Proof Complexity and SAT Solvers

<!-- cite:begin -->
From *P = RP: A Monte Carlo Program for P versus NP* by Nick Polson and Vadim Sokolov (2026), chapter 14. Cite as Polson and Sokolov (2026), *P = RP: A Monte Carlo Program for P versus NP*, edition 1, https://doi.org/10.5281/zenodo.23738431. Book page: https://vsokolov.org/books/p_equals_rp/. Source: https://github.com/VadimSokolov/p_equals_rp.
<!-- cite:end -->

This chapter explains why SAT solvers and Monte Carlo methods fail on the same instances. It describes resolution, the DPLL procedure and conflict driven clause learning, lower bounds for resolution (Haken on the pigeonhole principle, and results on random 3SAT near the satisfiability threshold), stronger proof systems (cutting planes, extended resolution, Frege systems), the encoding of N queens as a CNF formula, why exact model counters based on component caching and knowledge compilation do not help for queens, and the difference between searching for one solution and sampling among many. It points out that proof complexity supplies lower bounds for a specific algorithmic method, which has no analogue for the swap chain except torpid mixing results such as Gore and Jerrum's, and it describes hybrid methods, including survey propagation derived from the cavity method of statistical physics. It contains no new theorem.

## From the literature

Davis, Putnam, Logemann and Loveland (1962); conflict driven clause learning (Marques Silva and Sakallah 1996; Moskewicz and coauthors); Haken's resolution lower bound for the pigeonhole principle (1985); width based resolution lower bounds; cutting planes, extended resolution and Frege systems; Gore and Jerrum on torpid mixing; survey propagation (Mézard, Parisi and Zecchina 2002).

## New results

<!-- results:begin -->
No new results of this chapter are catalogued.
<!-- results:end -->

## Key terms

proof complexity, resolution, DPLL, CDCL, SAT solver, pigeonhole principle, random 3SAT, satisfiability threshold, cutting planes, extended Frege, model counting, #SAT, component caching, survey propagation, cavity method, search versus sampling, torpid mixing, N queens as SAT
