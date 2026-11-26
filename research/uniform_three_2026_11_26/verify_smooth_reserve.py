"""Integer bounds for the two continuous sieve integrals at cutoff 1/7."""
from fractions import Fraction

N = 2000  # exponent mesh
S = 10**12  # reciprocal integral unit


def ceildiv(x, y):
    return -(-x // y)


# Each cell [i/N,(i+1)/N] has mass int dt/t between 1/(i+1) and 1/i.
lower = [0] * (8 * N + 1)
upper = lower.copy()
for i in range(1, 8 * N):
    lower[i + 1] = lower[i] + S // (i + 1)
    upper[i + 1] = upper[i] + ceildiv(S, i)

emin = Fraction(2718, 1000)  # e > 2.718 by its Taylor series
worst = None
for lo in range(N, int((7 - 2 * emin) * N) + 1):
    hi = lo + 1
    # u_0=(7-t)/2, v=7-e-t, with t in [lo/N,hi/N].
    ulo = (7 * N - hi) // 2
    uhi = ceildiv(7 * N - lo, 2)
    vhi = ceildiv((7 * N - lo) * emin.denominator - N * emin.numerator,
                  emin.denominator)
    # Lower bound for twice rho(u_0), in units 1/S^2.
    bound = 2 * S * (S - upper[uhi] + upper[N])
    for i in range(N, ulo - N):
        # Include only complete rectangles whose largest coordinates sum <= ulo/N.
        jend = ulo - i - 1
        if jend > N:
            bound += (lower[i+1] - lower[i]) * (lower[jend] - lower[N])
    # Upper bound for twice the compatible pair mass.
    for i in range(N, hi):
        # Include all cells with lower corners i+j <= vhi and j<hi.
        jend = min(hi, vhi - i + 1)
        if jend > N:
            bound -= (upper[i+1] - upper[i]) * (upper[jend] - upper[N])
    if worst is None or bound < worst:
        worst = bound
assert worst > 6 * S**2 // 1000
print(f'Minimum certified margin exceeds 0.003 across mesh 1/{N}.')
