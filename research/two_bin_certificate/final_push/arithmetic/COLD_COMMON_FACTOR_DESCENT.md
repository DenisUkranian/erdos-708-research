# Exact descent through a common cold factor

24 November 2026. This is a general proved arithmetic reduction. It does
not provide the simultaneous allocation among overlapping clusters that
would close the Erdős 708 asymptotic.

## 1. Notation and finite statement

Let 0<=w_p<=1 have finite support, let X(a)=sum_p w_p v_p(a), let c>1,
and let I be any interval of M consecutive positive integers. For an
integer 1<=g<=M define

    t=X(g),   N=floor(M/g),
    J_g={v:gv belongs to I}.

The set J_g is an interval of either N or N+1 consecutive positive
integers. Fix any N-term subinterval J_0 of J_g. Define the entire
g-divisible cluster defect, without assigning sources to other clusters,

    D_g = sum_{a<=M,g|a}(X(a)-c)_+
           -sum_{b in I,g|b}(X(b)-1)_+.

If 0<=t<1, put s=1-t and

    w'_p=min(w_p,s)/s,    c'=(c-t)/(1-t).

Then

    D_g <= s*[sum_{u<=N}(X_{w'}(u)-c')_+
                 -sum_{v in J_0}(X_{w'}(v)-1)_+].       (1)

For c=2+delta,

    c'=2+(delta+t)/(1-t)>=2+delta.                      (2)

All prices w'_p lie in [0,1]. Prices at primes above N can additionally
be set to zero on the right of (1), since they affect only the target
penalty and their deletion weakly increases that right side.

If t>=1, the exact elementary bound is instead

    D_g <= -N*min(t-1,c-1)<=0.                         (3)

No selected-target row balance is being transported through the
reduction. Statements (1)--(3) hold without any optimality assumption.

## 2. The clipping identity

Write

    Y(u)=sum_p min(w_p,s)v_p(u),
    L(u)=X(u)-Y(u)=sum_p(w_p-s)_+v_p(u).

For every integer u,

    (X(u)-s)_+ = L(u)+(Y(u)-s)_+.                     (4)

Indeed if L(u)=0 the equality is immediate. If L(u)>0, at least one
prime occurrence has original price larger than s. Its clipped price
is s, so Y(u)>=s, and both sides equal X(u)-s. This argument includes
all repeated prime occurrences.

For every real threshold theta, the 1-Lipschitz property of the positive
part gives

    (X(u)-theta)_+ <= L(u)+(Y(u)-theta)_+.             (5)

Finally, any nonnegative raw additive function L obeys exact prefix
domination on an interval of the same integer length:

    sum_{u<=N}L(u) <= sum_{v in J_0}L(v).              (6)

To see this, expand every valuation into all its powers. For each p,j,
the prefix contains floor(N/p^j) multiples of p^j, whereas J_0 contains
at least that many. No asymptotic remainder and no independence claim
are used.

## 3. Proof of cold-factor descent

Raw valuations give X(gu)=t+X(u), even when g and u share prime factors.
Deleting any extra target quotient position can only increase D_g.
Thus for theta=c-t and s=1-t,

    D_g <= sum_{u<=N}(X(u)-theta)_+
              -sum_{v in J_0}(X(v)-s)_+.

Apply (5) to the source and (4) to the target. The total L contribution
is nonpositive by (6). The remaining expression is

    sum_{u<=N}(Y(u)-theta)_+
      -sum_{v in J_0}(Y(v)-s)_+,

which equals the right side of (1) because Y=s*X_{w'}.

## 4. Proof for a hot or boundary common factor

Suppose t>=1. At every target quotient,

    (X(v)+t-1)_+=X(v)+t-1.

At every source quotient,

    (X(u)+t-c)_+<=X(u)+(t-c)_+.

Use (6) with L=X and the N-term interval J_0. This gives

    D_g <= N*[(t-c)_+-(t-1)]
         =-N*min(t-1,c-1),

proving (3). Extra target quotient positions only strengthen the bound.

## 5. Minimal-length consequences

Fix c>1. If an actual positive value of J_c exists, choose the smallest
integer prefix length M for which it exists, and any weight vector with
positive J_c at that length. Its own full tail

    A={a<=M:X(a)>c}

has gcd(A)=1. In fact, for this shortest length,

    D_g<=0 for every 2<=g<=M.                         (7)

To prove (7), use (3) when X(g)>=1. Otherwise (1) reduces to a normalized
threshold c'>=c and length N<M. A positive right side would imply a
positive J_c at that smaller length, contrary to minimality. The prices
above N can first be dropped. This proves (7) without any assumption
that the entire tail lies in that particular cluster.

For the gcd consequence, if every member of A were divisible by g>1, the global source
hinge sum equals its g-divisible part and the total target penalty is
at least its g-divisible part. Hence J_c<=D_g. If X(g)>=1, (3) gives a
contradiction. If X(g)<1, (1) produces positive J_{c'} at length
N=floor(M/g)<M. Since c'>=c, the same prices have J_c>=J_{c'}>0 there,
again a contradiction. Remove prices above N if necessary as described
after (2). No claim about preservation of individual row balances is
needed: a positive feasible price vector at the smaller length already
suffices.

This excludes a common-factor explanation of a shortest positive
example. It does not exclude a union of overlapping factor clusters.

The same consequence has a bounded-error version aligned with the
asymptotic problem. Fix any B>=0 and choose the shortest prefix length
violating J_c<=B. Then for every proper factor g>=2,

    D_g<=(1-X(g))B if X(g)<1,
    D_g<=0        if X(g)>=1.                         (8)

Indeed every smaller normalized problem has J_c<=B, and its increased
threshold c' only lowers that objective. In particular the full tail of
this shortest violation again has gcd one. This statement does not
assume the stronger exact assertion J_c<=0 at small lengths.

## 6. The precise remaining obstruction

It is invalid to sum (1) or (3) over arbitrarily chosen gcd clusters.
A target position divisible by two cluster generators contributes its
entire hinge penalty twice to that sum, whereas the original objective
contains it only once. Full-tail source counts and global exact prime
rows do not, by themselves, supply a fractional partition of this shared
target payment.

Thus the cold-factor reduction does legitimately raise the normalized
threshold and shorten the numerical interval for an isolated cluster.
The missing arithmetic statement is a simultaneous cluster allocation
that retains the one-copy target budget, or an independent bound on its
multiway overlap loss. Neither statement is proved here.
