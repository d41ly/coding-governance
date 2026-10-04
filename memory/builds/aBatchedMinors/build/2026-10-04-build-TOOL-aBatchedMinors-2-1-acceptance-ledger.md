# Acceptance ledger — TOOL-aBatchedMinors-2

**Serves:** journal TOOL-aBatchedMinors-2

Built at `131537ae`, hardened by `TOOL-aBatchedMinors-6`. The arms are the `TOOL-aBatchedMinors-2`
block of the `--review` arms in the driver's suite, run as a slice of that block: 37 assertions at
the build commit, 17 of them RED against the base driver, all green on the build.

**Evidences:** TOOL-aBatchedMinors-2
- AC1 — `--highs x` — refused as not a plain integer, and `--minors -1` likewise; the closing-round row count stays 0
- AC2 — `--minors 2` — on spec subject `S9`, refused naming the closing review; the S9 row count is 0 (added by unit 6)
- AC3 — `--review` — a converged closing round with no counts, and one with either count alone (unit 6), each refused naming both flags; a count on a CONVERGING closing round refused as a claim about an exit that has not happened
- AC4 — `--highs 0 --minors 3` — refused naming `promote` with no disposition, refused as folding nothing with `fold`, written with `promote`
- AC5 — `--highs 0 --minors 0 --disposition promote` — refused as promoting nothing; with no disposition the row `CONVERGED · highs 0 · minors 0` is written
- AC6 — `--highs 1 --minors 4 --disposition promote` — the row ends `CONVERGED · highs 1 · minors 4 · disposition promote` and the echo says `owes at least 2 new unit(s)`
- AC7 — `--review` — the whole `--review` block, spec-subject arms unchanged, ran 79 assertions green at `131537ae`
- AC8 — `bash tools/unattended/check-unattended.sh` — check 26 named `--highs --minors` before the usage line moved, and exits 0 after
