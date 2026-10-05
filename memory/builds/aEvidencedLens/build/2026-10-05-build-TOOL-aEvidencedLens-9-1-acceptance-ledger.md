# TOOL-aEvidencedLens-9 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-9

Check 19 refuses a run commit that changes the effective `REVIEW_ROUNDS` bound, and check 2 grades a
spec subject's terminal row from `SPEC_COUNTS_CUTOFF`. The pass commit `2577d81d9` records no direct
check figures beyond `c117d0007` settling as no write, and says neither suite was run. The function
criteria were re-run here as the spec's preamble says: `read_rounds_of` and `scan_round_writes`
extracted with its `sed` from `tools/unattended/check-unattended.sh` at `2577d81d9` and at HEAD
`3bf1726b5`, beside `GIT() { git "$@"; }`, over a `git init` fixture in the session scratch. That
file moved after the pass in `091f81b0f`, `029b0522a` and `efad4cee4`.

**Evidences:** TOOL-aEvidencedLens-9
- AC1 — `rounds=2` — at `2577d81d9` the three-line blob printed `rounds=2`, and at HEAD it prints `rounds=multi:1,2`, the fail-closed reading `029b0522a` (`TOOL-aEvidencedLens-21` S6) gave a blob with two assignment lines, so the first half no longer holds as written at HEAD. At both revisions a blob with no assignment printed `rounds=3` with `DRIVER` at a scratch driver declaring `REVIEW_ROUNDS_DEFAULT=3`, and `rounds=` with `DRIVER` empty.
- AC2 — `scan_round_writes` — fed the fixture's four commits at both revisions it printed only the raise, `<sha> 1 2`; fed alone, the commit adding `REVIEW_ROUNDS="1"` with no prior assignment printed nothing, and so did the `--no-ff` merge of `main` into `run` that keeps `"2"`. `DRIVER` was `tools/unattended/unattended.sh`, whose default is 1.
- AC3 — `1 -> 2` — the `R1` live arm, the `R2` owner-merge arm and the `R3` terminal arm of `check-unattended.test.sh` carry it; no full `check-unattended.sh` run over a fixture was made. The suite arm is written but not run — the owner deferred the self-tests to a manual run on the merged tree (2026-10-05).
- AC4 — `c117d0007` — `git show --name-only` confirms it touches `.unattended.conf`, and fed to `scan_round_writes` at both revisions it printed nothing. `grep -n "does NOT check"` prints line 2518 at HEAD, naming an edit committed outside any run and a preflight `--waive`; the same header names an uncommitted working-copy edit the driver sources.
- AC5 — `closing-review row carrying counts` — each of the three `grep -c` patterns printed 0 at HEAD and 1 over `git show 2577d81d9~1:tools/unattended/check-unattended.sh`. Check 2's awk comment reads that a row carrying both counts, on any subject, is a counted exit.
- AC6 — `SPEC_COUNTS_CUTOFF` — check 2's awk program extracted at HEAD, run with `fc=2026-10-05`, `graded=1` and `slug=tRun`: at `speccut=2026-10-01` the folded row and the countless row each named `spec subject(s) S1`, and the counted row was silent; at `speccut=2026-10-10` all three were silent.
