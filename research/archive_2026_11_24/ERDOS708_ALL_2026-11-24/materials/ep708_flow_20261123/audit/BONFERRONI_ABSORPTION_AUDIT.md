# Audit of the enlarged substantial-prime cutoff

## Result

PASS. The Bonferroni error can be absorbed using the actual reciprocal mass of the selected prime subset. A single explicit constant, 1/8, works for every integer s>=2. This gives a finite cutoff M^{1/(s+1)}/8. A further uniform sparse-regime bootstrap, in Section 4, removes that constant factor, yielding cutoff M^{1/(s+1)} and the improved retained occurrence bound 2s.

This is a necessary reduction for the sparse obstruction regime, not a proof of J_weak. The finite absorption itself needs neither a prime-counting estimate nor the quadratic ambient gate.

## 1. Finite statement

Let 0<=w_p<=1 be finitely supported raw weights, let X(n)=sum_p w_p v_p(n), and let h count the targets of an actual length-M interval with X>1. Fix eta>0 and an integer s>=2 with s*eta>1. Set

    z=M^{1/(s+1)}/8,
    P_0={p<=z : w_p>=eta},
    mu_0=sum_{p in P_0}1/p.

Then

    min(mu_0,1/2)
      <=(2s+1)((h+1)/M)^{1/s}
        +(2^{s+2} s! h/M)^{1/s}.                          (1)

An empty P_0 is immediate. Otherwise put a=max_{p in P_0}1/p. Since p^s is hot,

    a<((h+1)/M)^{1/s}.                                   (2)

Choose Q subset P_0 with reciprocal mass mu'<=1/2 and

    mu'>=min(mu_0,1/2)-a.

Write k=|Q|. Because every prime in Q is at most z,

    k<=z*mu'.                                            (3)

The previously proved finite Bonferroni inequality gives

    h+E_s(k)>=M e_s/2,
    E_s(k)=binom(k,s)+(s+1)binom(k,s+1),
    s! e_s >= (mu'-(s-1)a)_+^s.                          (4)

These statements use the actual shift-uniform divisibility counts; no expected independent model is substituted.

## 2. Absorption with explicit constants

If mu'<2s*a, then min(mu_0,1/2)<=(2s+1)a, which is already covered by (1).

Otherwise mu'>=2s*a. Equation (4) gives

    h+E_s(k)>=M mu'^s/(2^{s+1}s!).                        (5)

Also

    E_s(k)<=(k^s+k^{s+1})/s!.

Using (3), mu'<=1/2, M>=1, and the specified z,

    E_s(k)/M
       <=mu'^s/s! * [8^{-s} M^{-1/(s+1)}
                       +8^{-(s+1)} mu']
       <=mu'^s/s! * [8^{-s}+8^{-(s+1)}/2]
       <=mu'^s/(2^{s+2}s!).                              (6)

The last inequality holds for all s>=2: it is equivalent to 17/4<=4^s. Subtracting (6) from (5),

    h/M>=mu'^s/(2^{s+2}s!),
    mu'<=(2^{s+2}s!h/M)^{1/s}.

Combine with min(mu_0,1/2)<=mu'+a and (2). The bound (1), which is slightly larger than the maximum of the two case bounds, follows.

## 3. Sparse-obstruction application

Suppose h=O_c(m), m/M=rho->0, and the previously proved raw weighted mean satisfies mu_w=sum_p w_p/(p-1)<=1+o(1). For each fixed eta, take s=floor(1/eta)+1. The right side of (1) tends to zero, so eventually min(mu_0,1/2)=mu_0 and

    mu_0=O_{c,s}(rho^{1/s}).                              (7)

The weighted monomial lemma with degree s+1 bounds the total weighted demand of sources having at least s+1 low substantial occurrences by

    M(s+1+mu_w)mu_0^{s+1}
      =O_{c,s}(m rho^{1/s})=o(m).                        (8)

After removing these sources, each remaining source has at most s low substantial occurrences.

For fixed s, if

    M>8^{(s+1)(s+2)},

then z^{s+2}>M. Thus any integer at most M has at most s+1 occurrences of primes greater than z. Every retained source therefore has at most

    s+(s+1)=2s+1                                         (9)

substantial occurrences. The threshold on M is allowed to depend on fixed eta. For a fixed finite selection of weight bands, use the maximum of these finitely many thresholds, so the same uniform selection argument remains valid.

The reduction bounds occurrences in each retained source. It still does not bound the number of substantial primes in the union of those sources, remove the dense regime, or justify reusing the target hinge across different source patterns.

## 4. A further bootstrap: cutoff M^{1/(s+1)} and 2s occurrences

Under the same sparse-obstruction hypotheses, put y=M^{1/(s+1)} and let mu(y) be the reciprocal mass of all substantial primes at most y.

The already proved finite estimate gives mu(y/8)=O_{c,s}(rho^{1/s}). The remaining constant-factor shell has mass at most

    sum_{y/8<p<=y}1/p <=8*pi(y)/y=O_s(1/log M),           (10)

by Chebyshev's upper bound. Consequently

    mu(y)=O_{c,s}(rho^{1/s}+1/log M)=o(1).                (11)

This preliminary o(1) bound is used only to justify absorption; the logarithmic term will not remain in the final estimate.

For sufficiently small rho and sufficiently large M, take Q to be the entire substantial-prime set up to y. Its mass mu'=mu(y) is less than 1/2, and its cardinality satisfies k<=y*mu'. Write a=max_{p in Q}1/p as before.

If mu'<2s*a, the desired O_{c,s}(rho^{1/s}) bound follows immediately from (2). Otherwise (5) holds, while now

    E_s(k)/M <= mu'^s/s! * [M^{-1/(s+1)}+mu'].             (12)

The bracket tends to zero by (11). Once it is at most 2^{-s-2}, subtracting (12) from (5) gives

    mu(y)<=(2^{s+2}s!h/M)^{1/s}=O_{c,s}(rho^{1/s}).       (13)

Combining the two cases establishes (13), with no additional logarithmic error. Uniformity is explicit: (11) ensures the required bracket bound whenever rho is below a fixed c,s-dependent threshold and M exceeds a fixed c,s-dependent threshold. No rate relationship between rho->0 and M->infinity is assumed.

Use the weighted monomial lemma at degree s+1 for this enlarged low set. Its exceptional weighted demand is still O_{c,s}(m rho^{1/s})=o(m), so every retained source has at most s low substantial occurrences. Every prime above y is strictly greater than M^{1/(s+1)}, so any s+1 such occurrences would have product greater than M. Thus there are at most s high occurrences, and every retained source has at most

    2s                                                    (14)

substantial occurrences in total.

The final 2s conclusion holds along every sparse actual-obstruction sequence. It remains a per-source bound, and it does not resolve the joint target-capacity problem.
