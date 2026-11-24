"""Exact arithmetic check of a row-level obstruction, not a g(n) calculation."""

from math import isqrt


def main() -> None:
    n = 2_000_000
    m = 2 * n
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p :: p] = b"\x00" * ((n - p * p) // p + 1)
    pi_n = sum(sieve)
    small_primes = [p for p in range(2, isqrt(n) + 1) if sieve[p]]
    source = 2 * n - n.bit_count() - pi_n - 2

    x0 = 1 << 100
    rough = bytearray(b"\x01") * n
    for p in small_primes:
        first = (-x0 - 1) % p
        rough[first::p] = b"\x00" * ((n - 1 - first) // p + 1)
    rough_count = sum(rough)
    valuation_sum = n - (x0 + n).bit_count() + x0.bit_count()
    target = n - rough_count + valuation_sum

    assert pi_n == 148_933
    assert rough_count == 154_615
    assert valuation_sum == 1_999_993
    assert source == 3_851_058
    assert target == 3_845_378
    assert source - target == 5_680
    assert (source - target) ** 2 > m

    print({"M": m, "quotient_start": "2^100+1",
           "source": source, "target": target,
           "deficit": source - target, "sqrt_M": isqrt(m)})
    print("PASS: actual-source eligibility and full-tail row count checked.")


if __name__ == "__main__":
    main()
