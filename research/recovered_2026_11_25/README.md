# Recovered original research archives — 25 November 2026

All eight original ZIP packages omitted from the previous public archive are stored here **byte-for-byte**, together with the new independent g(9) replay log. Because the connector could not send the combined binary in one request, it is stored as ten binary pieces. Each Git blob SHA-1 was independently compared to the corresponding local bytes before the pieces were committed. The manifest also records the SHA-256 of each piece and the complete ZIP.

## Restore

From the repository root, run:

~~~sh
python3 research/recovered_2026_11_25/restore_archives.py --output recovered_2026_11_25
~~~

The script reconstructs the exact 6,921,905-byte ZIP, checks every part and the combined SHA-256, checks the original packages' SHA-256 and ZIP integrity, and extracts the original ZIPs and replay log to the output directory. It refuses unsafe archive paths and different existing output files. To additionally extract the contents of each original ZIP, add --unpack. To rerun the original g(9) upper-13 verifier, use --verify-g9 (Python 3 and g++ C++17 required). This is separate from replaying its upstream finite-case dependencies.

## Inventory

- ERDOS708_g9_new_prime_group_lemmas.zip
- ERDOS708_g9_structural_tail_9450.zip
- ERDOS_708_g9_at_most_two_large_primes.zip
- ERDOS_708_g9_bounds_12_to_13_verified.zip
- ERDOS_708_g9_high_high_frontier.zip
- ERDOS_708_g9_new_partial_closures.zip
- ERDOS_708_g9_partial_new_reductions.zip
- erdos708_descent_attempt.zip

The external redlydi repository is not republished. The current asymptotic work and its corrections are indexed in [the November 25 checkpoint](../asymptotic_2026_11_25/README.md). The finite-case results are indexed in [g9_12_or_13](../g9_12_or_13/README.md) and [g9_followup](../g9_followup/README.md).

The original packages are historical research, not independently refereed or uniformly proved results. In particular, the exact g(9) and general asymptotic remain open. The upper-13 computation was actually replayed; the other recovered archives have their original provenance and validation limitations.

## Browseable files

[Source index](SOURCE_INDEX.md): 67 original proof, code, small data and log files, available directly on GitHub in addition to the complete byte-preserving archives.
