# Checked constant-weight star calculation and its limitation

## Scope

This is an internal calculation for a proposed route toward the general joint estimate. It is not a general weighted theorem and is not offered as a solution of the requested unrestricted problem. The calculation below has no diffuse positive-weight block and assumes that all high-prime occurrences have the same price b. Mixed prices do not automatically satisfy its key occurrence identity.

The important correction is that a contributing source forces its smallest high prime into a much shorter logarithmic range than the condition T>=p alone would imply. That restriction controls the otherwise excessive prefix-exclusion cost.

## 1. Setup

Fix b in (0,1], delta>0, and put

    s=floor(1/b)+1,   y=M^{1/(s+1)}.

Let P_L be a low-prime set contained in [2,y], with

    mu_L=sum_{q in P_L}1/q=o(1),
    k_L=|P_L|<=y*mu_L.

Let P_H contain primes strictly greater than y. Every high-prime occurrence has price b. Inactive prime factors are allowed without restriction. Let alpha(n) in [0,1] depend only on the complete P_L-part of n. The auxiliary load is

    W(n)=alpha(n)+b*Omega_{P_H}(n).

Only sources a<=M with W(a)>2+delta need be charged.

## 2. A contributing source has exactly s high occurrences

Every source has at most s high occurrences because a product of s+1 primes greater than y exceeds M. Conversely, if it had at most s-1 occurrences, then

    W(a)<=1+(s-1)b<=2.

Thus every contributing source has exactly s high occurrences.

Let l be its full low part and let p be its smallest high prime. Set

    d=l*p,  T=M/d,  h=alpha(l)+b-1.

Then

    h>delta,
    0<h<=b,
    b(s-1)<=1,
    p^s<=a<=M,
    T>=p.                                                (1)

The source excess can be written

    W(a)-2-delta=h+b(s-1)-1-delta
                 <=h*b(s-1).                            (2)

The final inequality follows from h<=1, b(s-1)<=1, and
(h+v-1)_+<=h*v for h,v in [0,1].

## 3. Counting source extensions, including inactive cofactors

For a fixed root (l,p), write its sources as a=l*p*t. The actual integer quotients t are distinct and at most T. Each has exactly s-1 remaining high occurrences, all on primes at least p. Therefore (2) gives

    sum_{a assigned to(l,p)}(W(a)-2-delta)
       <=h*b*sum_{t<=T}Omega_{P_H intersect[p,infinity)}(t)
       <=h*b*T*sum_{p<=q<=T, q prime}1/(q-1).             (3)

This is a weighted reciprocal-tail count, not a prime-fibre cardinality claim. Arbitrarily many different inactive cofactors are included correctly in the sum over t. Repeated high-prime powers are included through 1/(q-1).

## 4. A signed star with a unique positive root

For roots that actually occur among the contributing sources, define

    K_{l,p}(n)=h*1_{lp|n}*
       [1-sum_{q in P_L}1_{lpq|n}
          -sum_{q in P_H,q<p}1_{lpq|n}].                 (4)

A positive term in (4) forces l to be the complete low part of n and p to be its smallest high prime. Hence at most one root contributes positively at any target. Its positive value is h, and W(n)>=alpha(l)+b=1+h. All remaining terms are nonpositive. Consequently

    sum_{(l,p)}K_{l,p}(n)<=(W(n)-1)_+.                    (5)

For a fixed root, interval multiple counts give

    sum_{n in I}K_{l,p}(n)
      >=h*T[1-mu_L-mu_prefix
                   -(k_L+pi(p)+1)/T],                  (6)

where mu_prefix=sum_{q in P_H,q<p}1/q. Because T>=p>=y and k_L<=y*mu_L,

    (k_L+pi(p)+1)/T<=mu_L+O(1/log y).                    (7)

Thus the target loss is uniform over all roots. There is no multiplication of an absolute error by the total number of source patterns.

## 5. The logarithmic gap, with the correct root range

Write

    a_log=log(p)/log(y).

Equation (1) implies the crucial bound

    1<=a_log<=(s+1)/s.                                   (8)

Also T<=M/p. Standard prime harmonic-sum asymptotics, uniformly for endpoints at least y, give

    mu_prefix<=log(a_log)+o(1),
    b*sum_{p<=q<=T}1/(q-1)
      <=b*log((s+1-a_log)/a_log)+o(1).                   (9)

Therefore the combined cost is bounded by

    f_{b,s}(a_log)
       =log(a_log)+b*log((s+1-a_log)/a_log).              (10)

For all allowed b,s and the full range (8),

    f_{b,s}(a_log)<=log 2<1.                             (11)

For s>=3, b<=1/(s-1)<=1/2, and (10) is increasing throughout (8). At the upper endpoint it is

    log(1+1/s)+b*log(s-1)
      <=log(1+1/s)+log(s-1)/(s-1)
      <=log(4/3)+(log 2)/2<log 2.

For s=3 this is the displayed endpoint value. For s>=4, both terms decrease as s increases, apart from the already checked transition from s=3 to s=4.

For s=2, b belongs to (1/2,1]. For fixed a_log in [1,3/2], the coefficient log((3-a_log)/a_log) is nonnegative, so (10) is increasing in b. Its maximum is therefore at b=1, where it equals log(3-a_log)<=log 2. This also covers repeated high-prime occurrences.

Combining (3), (6), and (9)--(11), for sufficiently large M and sufficiently small mu_L, every root's signed target count pays its assigned source excess with a fixed positive logarithmic margin. Summing and using (5) validates this auxiliary constant-weight charging argument.

## 6. Why this does not yet give the requested theorem

The identity that every contributing source has exactly s high occurrences is special to one common high price b, in the absence of an additional diffuse load. With different high prices, a source can have a mixture of occurrence counts and need not have a single high prime whose removal leaves weighted high load at most one.

An added diffuse block can also make a source contribute with fewer than s high occurrences, so the short root range (8) is no longer automatic. The conditional diffuse comparison must be integrated with the star argument, with its target capacity charged only once.

The low-block aggregate-cap reduction and the filtered-bank counts remain valid, but they do not repair these two gaps by themselves. No general mixed-weight estimate, sparse source-tail theorem, or J_weak proof is claimed here.
