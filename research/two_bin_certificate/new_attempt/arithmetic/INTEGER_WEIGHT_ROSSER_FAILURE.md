# Integer prices do not repair the direct weighted Rosser recurrence

24 November 2026. No weighted transfer theorem is proved here. The desired
statement remains

    sum_(a<=M) (Y(a)-2r)_+ <= sum_(b in I) (Y(b)-r)_+,
    Y(t)=sum_p k_p v_p(t),  0<=k_p<=r, k_p,r integers.       (1)

The finite example below is a counterexample to a natural weighted
coefficient construction and its aggregate source reserve, **not** to (1).

## 1. The specific recurrence

Process primes in decreasing numerical order and store every integer
threshold t=0,...,r simultaneously. Start with q_1(t)=t. At prime p of
integer price k_p, for every old mixed/nonunit modulus d<=M let

    J=max{j>=0:d*p^j<=M}.

The cumulative coefficient at exponent j<J is q_d((t-j*k_p)_+). At the
last exponent use

    min_(e>=J) q_d((t-e*k_p)_+).

Successive differences of these cumulative values give the new divisor
coefficients. For d=1 retain the complete exact univariate sequence until
the cumulative value becomes zero. Thus pure-prime-power cancellation is
preserved even at moduli exceeding M. Old pure-power coefficients exceeding
M are carried forward; their downward-threshold minimum is unchanged.

Termwise lower replacement proves the global target minorant

    F(t)=Y(t)-r+Q_r(t) <= (Y(t)-r)_+.

The binary construction is recovered at r=1 and every positive k_p=1.
The question is whether the total prefix reserve of F pays its negative
floor terms at general integer prices.

## 2. An exact small failure

Take

    r=10,  (k_2,k_3,k_5,k_7)=(1,1,3,1),  M=105.

The recurrence gives exactly one nonzero mixed coefficient at threshold r:

    q_105(10)=-1.

After exact univariate cancellation, the global minorant has the closed
form

    F(t)=(v_2(t)-10)_+ +(v_3(t)-10)_+
           +(3v_5(t)-10)_+ +(v_7(t)-10)_+ -1_(105|t).      (2)

Its validity as a target minorant can also be checked directly: the sum
of the four univariate positive parts is at most (Y(t)-10)_+, and the last
term only decreases it.

On the full prefix 1<=a<=105, max Y(a)=8. All four overflow terms in (2)
vanish, so

    sum_prefix F=-1,    sum_prefix(Y-20)_+=0.

The aggregate source reserve is already negative before paying any floor
error. At M=105 the actual floor error of modulus105 is zero, because105
divides M. This does not rescue the negative source reserve.

There is also an exact actual-floor version. At M=106 the recurrence is
unchanged. For the interval I={105,...,210},

    sum_prefix F=-1,    sum_I F=-2.

There is one prefix multiple of105 and two interval multiples. Hence the
negative coefficient incurs its full one-unit floor loss. The actual
source and target hinges in (1) are both zero: (1) itself is not violated.

## 3. The local boundary mechanism

After processing7 and5, the pair coefficient is

    q_35(t)=1 for t=1,2,3, and zero at all other integer thresholds.

At prime3, the last allowed exponent at d=35 is J=1. The cumulative
minimum is zero, so

    q_105(t)=-q_35(t).

At prime2, the source modulus105 is already a boundary state with J=0.
Although2 does not divide the source105, the minimum over downward
threshold shifts imports the value -1 from threshold1,2,or3 to threshold10:

    q_105^new(10)=min_(e>=0) q_105((10-e)_+)=-1.

The source105 has Y(105)=5. Its desired source hinge is zero, and its
unmodified target-threshold hinge is also zero. There is no local source
reserve to pay this boundary loss. All integer thresholds were retained
throughout; their simultaneous availability is precisely what permits
this uncharged minimum.

## 4. Pruning unused prices does not solve the general recurrence

The finite example has an empty full tail, so deleting prices unused by
that tail would remove it. This limitation is explicit. A previously
proved counterfamily to the same corrected raw recurrence already avoids
that simplification:

    P=2^j, M=2P^3, r=10j,
    k_2=11, k_p=4j for P<p<=1.1P.

These are integer prices bounded by r for j>=2. They are exactly the
normalization of the family in
`ep708_terminal_20261124/variation/RAW_ROSSER_AGGREGATE_COUNTERFAMILY.md`.
Every positive price appears in the own full tail, and for fixed
0<delta<1/20 its size is

    n_delta=Theta(P^((17-10delta)/11)/log P),
    M=o(n_delta^2).

Nevertheless the normalized prefix certificate sum is
-Omega(P^3/(log P)^3), before any negative floor charge. That family fails
the genuine-optimizer mandatory-bank row equations; it is not a
counterexample to the target arithmetic theorem.

## Conclusion

Integer price quantization changes neither the local boundary mechanism
nor the known aggregate obstruction. No corrected signed recurrence with
a common payment of all boundary and negative-floor terms was obtained.
The remaining requirement is a new arithmetic estimate using the actual
full-tail optimum and its mandatory banks, not merely simultaneous storage
of integer thresholds.
