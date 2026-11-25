# External comparison: redlydi/Erdos708-Research

Inspected version: https://github.com/redlydi/Erdos708-Research/tree/fe7ce85c8b0b4c27dd942248ba04a42e9b1182d1
Mathematical source: https://github.com/redlydi/Erdos708-Research/blob/fe7ce85c8b0b4c27dd942248ba04a42e9b1182d1/reports/REPORT.md
Code: https://github.com/redlydi/Erdos708-Research/blob/fe7ce85c8b0b4c27dd942248ba04a42e9b1182d1/code/check.py

This is independently authored work; only a comparison and attribution are included, not a copy of its report/code. Its README explicitly marks general asymptotic closure as open. Its primary report gives the following results under stated hypotheses; we reviewed the written arguments and source code, but did not execute the external verification programs.

* For representations \(a=dpr\) with \(p\le r\), a fixed number \(k\) of nontrivial core values \(d\) yields \(2n+C(k)\). Long core groups use a semiprime Hall reserve uniform over all subsets and shifts, short groups are treated first, and rank-two sources are repaired individually.
* For pairwise coprime cores, an oriented conflict graph (an outside prime of one source dividing another core) yields \(2n-1+f\) if deleting \(f\) module-labelled arcs makes the graph acyclic. With a smallest-prime outside factor the cycles are excluded.
* A local width bound \(\tau\le\sum_a w(a)\) uses the antichain width of prime-power supports containing \(a\). Order supports by cardinality; select enough distinct multiples of each support gcd, then charge new positions to as-yet uncharged comparable supports. Laminar supports give \(n\). General support width need not be two.
* Words of length at most three over pairwise coprime composite letters can be treated by median-letter pivots. The proof tracks \(\operatorname{ord}_u\) rather than assuming additivity of composite-letter exponents.

Useful quantitative deduction from the semiprime Hall proof: for \(L\to\infty\), the ratio of the number of semiprime sources to the number of available smaller-prime representatives is \(O(\log\log L/\log L)\), uniformly over subsets and shifts. For reciprocal mass \(x\le1\), the sum of prime quotas is \(O(D/\log L)\), where \(D=\sum\lfloor L/p\rfloor\). For \(x\ge1\), the neighborhood has \(\gg L\) positions and the number of semiprimes is \(O(L\log\log L/\log L)\). This follows from the second-moment proof and standard prime counting.

The genuine connection to our work is the LCM-loss bound and growing shared Hall reserve in COMPONENT_LEMMAS.md. This removes any need to require global injection among all local core groups if the residual LCM loss can be controlled. The general statement \(\sum_b E_b=o(n)\) is still open; large intersecting components and repeated prime units must be handled jointly.

The external stored outputs report 160 support-layer examples, 75 coprime-core examples, 75 overlapping-core examples, and a local two-cycle obstruction at 210. Its separate G3 script reports 58,253 subsets / 752 blocks and 99,125 subsets / 7,380 block checks. These are source-reported counts, not our new replay. The example at 210 is a counterexample only to a particular local payment, not to the original problem.
