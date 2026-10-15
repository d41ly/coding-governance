# Brief — dRedressedBar: the closing review's 13 findings, promoted into units 21, 22 and 23

**Serves:** research TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23

## The prompt

> All 13

The owner's answer, 2026-10-15, to which of the closing review's findings to fix in this build before the arm observations and the full bar.

## The brief

### Goal
The round-1 closing diff review over `ebce889c7..e114f1356`, `reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md`, returned CLEAN WITH FIXES: no blocker, 1 high, 7 mediums, 5 lows, each confirmed by a skeptic, each with a stated fix and a left-shift gate. Fix every one at its root in this build, so the bar runs once over the fixed code. Read each finding's Where, What is wrong, Consequence, Fix and Left-shift gate in the record; where the skeptic judged the finder's fix unsound (L1, L2), the record's corrected fix is the one to spec.

### Items
1. **TOOL-dRedressedBar-21 — H1 (id 1), the profiler's dead-run sweep.** `tools/run-gates/measure_legs.py`'s S38 sweep (`derive_abandoned_scratch`, `write_recovered_logs`, `write_atomic`, the call in `main`) trusts a sibling `gate-profile.*/owner.json` it finds under the shared temp dir: it writes into the `record` directory that file names, reads `raw/<n>.out` through symlinks, and opens its temp file without `O_EXCL`. Spec the three-part fix in the record, an arm that plants a `record` outside the out root and a symlinked raw file and is observed RED against the current code first, and the left-shift gate the record names (a checklist entry or a static arm over `write_atomic`'s temp open).
2. **TOOL-dRedressedBar-22 — the profiler batch: M1 (ids 2, 14), M2 (id 3), M5 (id 11), M7 (id 15), L1 (id 6), L2 (id 9), L3 (id 10) and L5 (id 16).** All in `tools/run-gates/measure_legs.py`, its fixtures and `tools/run-gates/README.md`: an interrupted run names every raw-kept capture; the interpreter probe spawns the base interpreter; arms drive every `ProfileRefused` site in `resolve_launcher_aliases` and `resolve_alias_interpreter`; the resolution red half reads each compared leg's verdict and evidence it ran; `check_admit`'s dead drained clause goes and AC5 grades the loop's real release; `legs.tsv` is rewritten whole from the final records; AC35's arm runs two legs; the README's signalling sentence matches the docstring. Unit 21 writes the same file first, so this unit orders after it.
3. **TOOL-dRedressedBar-23 — the govkit batch: M3 (id 4), M4 (id 5), M6 (id 12) and L4 (id 13).** A narrower `apply` carries a carried kit's orders as it carries its rows, and `write_gate_legs`' no-runner branch lists carried kits' legs; the gained loop's adopter spawn decodes with `errors="replace"` (or all three adopter spawn sites go through one helper); the `govkit selftest` guard gains `{prefix}/codebase-map/kit.toml` as an exact path, with its manifest re-stamp; the `[-21] AC2` routing arm asserts liveness per member.
4. **Specs already CLOSED that describe the behaviour these units change** (18 and 19 for the profiler, 12, 14, 16 and 17 for govkit): a correction to a closed spec is a spec-writer pass at that unit's turn, never a build-pass edit, as units 12 to 19 did it. Name each such pass in the unit's §4 and give it its own `<wN>` commit.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades units 21, 22 and 23 READY, ordered after unit 19 in the order 21, 22, 23. Every finding id 1 to 16 except the refuted 7 and 8 is named by exactly one unit's scope, with an AC whose red half reproduces the defect the record describes.

### Gates
`memory hygiene` · `lexicon naming predicates`

### Non-goals
- No finding outside the round-1 record. The refuted ids 7 and 8 stay refuted.
- No `tools/unattended/` self-test suite runs (standing owner instruction, 2026-08-23).
- No merge to local main and no push without the owner's ask.
