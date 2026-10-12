# Acceptance ledger — TOOL-aSparedSpawn-18

**Serves:** journal TOOL-aSparedSpawn-18

Node `a`, 2026-10-12, bash under MSYS. The pass ran no merge bar, no suite, no held leg and no slice
of a suite. AC1 was observed through the instrument committed beside this ledger,
`2026-10-12-build-TOOL-aSparedSpawn-18-direct-checks.sh`, which runs the width A/B instrument with
`AB_LOAD=0` over a `git clone --local` of the tree frozen at `d35fca5b`, against a two-leg
`GATE_LEGS` manifest of `bash -c` legs, so each arm's bar took 6 to 11 s. The manifest has two legs
where the criterion names one: the second is a kit-subject `selftests` leg, the held class, and the
first is the control (a `records` repo leg in `ok` and `red`, a `selftests` repo leg in `held`). The
instrument ran over the changed script, over the base script `d35fca5b` (byte-identical to
`f479ba42`'s), and over a copy of the changed script with `GATE_SELFTESTS=1` removed, the staged break
that isolates the new count from the new knob. `bash -n` passed on both scripts. An all-held bar exits
2, not the 1 the review states; the `rc` column records any non-zero exit, so the difference is moot.

**Evidences:** TOOL-aSparedSpawn-18
- AC1 — `2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh` run by `direct-checks.sh ok|red|held` — changed script: `ok` read `yes` on all six rows with `gate_lines` 2, `legs` 2, `rc` 0, and the arm printed `GATE ok    fx kit`; `red` read `no` on all six rows with `gate_lines` 2 and `rc` 1, the arm printing `GATE FAIL  fx kit  (exit 1)`, so the exit, not the count, is what refuses it, and the best-wall widths read `none`; `held` read `yes`, both self-test legs executing. Base script: `red` read `yes` on all six rows, the kit leg printing `GATE held  fx kit` and the bar going GREEN on the one leg left, and `held` read `yes` on all six rows over a bar that printed `executed NOTHING` — the red the criterion names. Staged break (knob removed): `held` read `no` on all six rows with `gate_lines` 0 and `rc` 2, so the count alone refuses `held` lines.
- AC2 — `grep -n 'one verdict per leg' memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh` — printed line 15 of the header's rule, an arm being a figure only when it executed one verdict per leg and its bar exited 0; the same grep over the base script counted 0.
