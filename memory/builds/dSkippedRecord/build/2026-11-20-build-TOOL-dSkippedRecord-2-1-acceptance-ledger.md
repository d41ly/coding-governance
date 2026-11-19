# TOOL-dSkippedRecord-2 — acceptance ledger

**Serves:** journal TOOL-dSkippedRecord-2

No merge bar, no self-test suite, no `--selftest` and no leg argv ran in this pass. The pass started
at 6b3edfe12, and this ledger rides in the product commit `<p2>` that closes the spec. The probe is
the one unit 1's acceptance ledger records under "The probe, as run", saved under the session
scratchpad with the two edits the spec's section 6 names: after its own `hit` and `miss` it sets
`n=0` and evals the suite's three assertion definitions, and its `same)` arm evals the suite's own
block. It ran in a fixture repository under `%TEMP%`, with the suite and the driver copied from the
tree this commit carries.

**Evidences:** TOOL-dSkippedRecord-2
- AC1 — `STATUS 0` — over the built driver, mode `same` printed the skip line ending
  `last committed at c783a09`, the suite's block read `lu_hash` as that same hash, and the probe
  printed no `FAIL` line. Over `blank.sh`, whose `last committed at "` count printed 1, it printed
  `FAIL the skip line`, the actual line ending in a blank `at `, and `STATUS 1`. With the suite at
  `922413ff1` the same `blank.sh` probe printed `STATUS 0`, the gap the review's item 1 names.
- AC2 — `FAIL the skip line` — over `readme.sh` the probe printed the expected line ending at the
  `fixture` commit's hash and the actual line ending at the base commit's, a different hash, and
  `STATUS 1`.
- AC3 — `at unread` — with a suite copy whose `lu_hash` read names `absent.md` in the record's
  directory, the probe over `blank.sh` read an empty `lu_hash`, printed `FAIL the skip line` with
  the expected line ending `at unread`, and `STATUS 1`. The same copy with the fallback written
  `$lu_hash` printed `STATUS 0`.
- AC4 — `HELPER-SAME` — the `run_render_helper` range diff against `922413ff1` printed nothing,
  the function-definition count printed the same figure over both revisions (291 PINNED at
  `922413ff1` on 2026-11-20), and the probe passed the `moved`, `addfail`, `difffail` and no-mode
  lines.
- AC5 — `overrid[e]` — the case-blind grep over the unit's spec printed 0, `lu-shim` was found in
  it, and its section 9 names 26f99cdb0.
- AC6 — `git diff --quiet` — unit 1's spec is unchanged between `922413ff1` and this commit; the
  command exited 0.

**Also probed:** the expected text in the suite's `same` call was compared with the driver's skip
line up to its `GIT log` substitution, and the two matched byte for byte, em dash included.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `tools/unattended/unattended.test.sh` region 8, the `same` call's whole-line assertion,
  covering AC1, AC2 and AC3: the main loop's RED observation on its staged breaks, the driver's
  `GIT log` substitution deleted and pointed at `README`, and GREEN once restored, recorded here
  under a `Pass: none` commit.
- The gates the spec's section 7 names, and the `spec tokens` check the brief asks for, which a role
  pass may not run.

**Observed at the close (main loop, 2026-11-20):** through the probe unit 1's acceptance ledger records,
with the two edits this unit's section 6 names, against driver copies made from
`tools/unattended/unattended.sh` at 288af33d7 in the session scratchpad. The suite is held by the
owner's standing instruction, so the probe stands in for region 8. Every hash below is a fixture
repository's, DERIVED at observation.
- GREEN — the built driver with the suite at 288af33d7: no `FAIL` line, `STATUS 0`, the read hash present.
- RED — the hash substitution deleted from the skip line (one line, the break confirmed by `grep -c`):
  `FAIL the skip line`, the actual line ending `at ` against an expected line ending in the read hash, `STATUS 1`.
- RED — the substitution pointed at `README`: `FAIL the skip line`, the two lines ending in
  different hashes, `STATUS 1`.
- The gap, at the suite as of 922413ff1 over the blanked driver: `STATUS 0`, so the prefix-only arm
  passed the break this unit's arm fails.
