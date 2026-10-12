# Build brief — aPairedSlots, units built inline by the main loop

**Serves:** journal TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 TOOL-aPairedSlots-11 TOOL-aPairedSlots-12 TOOL-aPairedSlots-13 TOOL-aPairedSlots-14 TOOL-aPairedSlots-15

Written 2026-10-11 for every unit of this build. The author is the main loop, building inline and
in sequence; M6 allows an inline author to sequence its own passes, and this brief says so. Units
1, 2, 3, 4, 5, 7 and 9 all write `tools/run-gates/run-gates.sh` and could not run concurrently in
any case; 6 and 8 are disjoint and are sequenced only because one author builds them.

## Ground

- Build from the unit's spec under `memory/builds/aPairedSlots/spec/`, read whole, on aFrugalTurnstile's
  landed host turnstile (origin/main `d19938f3`, merged at `fcc9a2b4`).
- The owner ruled on 2026-10-11 to build beside the A/B, which runs on frozen clones under
  `%TEMP%/pab` and is never touched by a pass.
- Fast direct checks only: a scratch fixture under the session scratchpad or `%TEMP%`, or a slice of
  one suite arm in an untracked `zz-slice-*.sh` beside the suite, deleted before `gen_map.py --write`.
  No merge bar, no `*.test.sh` run, no self-test suite inside a pass; the suites run sliced at
  VERIFYING. Never wrap a bar in `timeout`.
- Each criterion's failing case is staged and observed RED on a runner copy before GREEN.
- Every pass: `--brief`, then `--dispatch` naming its writes, the spec committed before its code,
  the code commit carrying `Pass: <unit-id>` and `memory/builds/aPairedSlots/RUN.md`, then
  `gotchas.py --for-diff HEAD~1..HEAD`.
- A new shell function: `gen_map.py --write` before the commit. Function names lead with a declared
  verb (`.lexicon.conf`).
- At `slots=1` every line a bar prints and every file it writes must equal the base runner's.
