# Brief — aShelvedLeg: the closing review's minors, batched

**Serves:** research TOOL-aShelvedLeg-2

## The brief

### Goal
Every MEDIUM and LOW the closing review confirmed on TOOL-aShelvedLeg-1 is fixed in one batch unit, as M4 promotes them, and each confirmed finding is left-shifted. The findings are in `memory/builds/aShelvedLeg/reviews/2026-11-10-review-TOOL-aShelvedLeg-1-closing-diff-round1.md` items 2 to 6, and `2026-11-10-review-TOOL-aShelvedLeg-1-closing-diff-round2.md` id 1.

### Items
1. **Stale merge-bar claims (round 1 items 2 and 3).** Every sentence in `tools/unattended/` that calls `check-unattended.sh` or the kit gate a merge-bar leg, or says it runs on the merge bar, is reworded to say the leg is held off every automatic bar by the 2026-11-10 ruling and runs through the kit's on-demand `--checks` route or the self-test variable. The review names `run-unattended-gates.sh:46-47` and `:434`, `check-unattended.sh:2`, `:73`, `:435` and `:3809`, and `check-unattended.test.sh:2485` and `:3330`; the spec re-derives the set by grep rather than trusting those line numbers. `check-unattended.sh` carries raw CR bytes, so it is edited in binary mode.
2. **The typed count (round 1 item 4).** The `--checks` comment at `run-unattended-gates.sh:561` names the population instead of typing "those four" about five rows.
3. **The changed-mode skip (round 1 item 5).** The HELD comment in `tools/unattended/kit.toml` and the kit README paragraph each gain one sentence: `GATE_SELFTESTS=changed` selects this leg by kit source only, so a records-only change leaves it held, and the self-test variable at `1` or the `--checks` route is how to run it after one.
4. **The unparseable reading (round 1 item 6).** The leg's row in `tools/run-gates/selftest-budgets.txt` is respelled so the `--rank` reader's `worst of (\d+) readings (\d+)s` form matches it, with the facts unchanged.
5. **The rc-only pooled reading (round 2 id 1).** The `no-trailer:` clause in `tools/run-gates/selftest-pooled-evidence.txt` states that this row's reading is rc only, because `check-unattended.sh` prints its failures as `UNATTENDED check <n> FAILED` and never a `^FAIL` line, and drops "likewise".
6. **Left-shift.** The three classes the review named new get one `memory/gotchas/` entry each: a hand-typed count of an enumerated population (round 1 id 4), changed-mode selection ignoring a kit-subject leg's `doc_reads` (round 1 id 5), and a fail count reading a pattern the row never prints (round 2 id 1). The amendment class for items 1 and 2 exists (`amendment-leaves-its-other-half-standing`), as does the spelling class for item 4 (`a-spelling-change-strands-its-readers`).

### Acceptance
1. A grep over `tools/unattended/` for merge-bar wording on the same line as `check-unattended` or the kit gate prints nothing. At BASE it prints the review's lines.
2. `run-unattended-gates.sh` types no count of the `--checks` rows.
3. `kit.toml` and the kit README each name `GATE_SELFTESTS=changed` beside the leg.
4. The leg's budget row matches `worst of (\d+) readings (\d+)s`, and `run-selftests.sh --rank` (main loop) no longer lists it among the unrecognised rows.
5. The evidence header says the row's reading is rc only, and `run-selftests.sh --check` (main loop) stays clean.
6. Each new gotchas entry passes memory hygiene.

### Gates
every held leg is budgeted, every budget row resolves · memory hygiene · spec tokens · docs · kit version markers · kit epoch · lexicon naming predicates · routed commits name a specced unit · brief-recorded; then the full bar at the lander.

### Non-goals
Counting `UNATTENDED check <n> FAILED` lines in `run-selftests.sh`'s fail column: `check-unattended.test.sh` fixtures print that same line, so a new pattern would move the fail counts of calibrated rows and break their pooled parity. A `--check` arm requiring every budget row to match a `--rank` form, which needs the 21 rows that already fail it respelled first. Adding the leg's `doc_reads` to changed-mode selection in `run-gates.sh`. Behaviour of any script.

### Limitations
Comments, docs, one data row and records only. A role agent runs no runner; the `--rank` and `--check` observations are the main loop's. Kit versions move through the lander's `mint`.

### Reuse
The wording TOOL-aShelvedLeg-1 already wrote at `run-unattended-gates.sh:8`, `:419` and `:559` and in the kit.toml HELD comment is the shape for item 1. The existing rows of `selftest-budgets.txt` that `--rank` parses are the shape for item 4.

## Owner confirmation

Asked: TOOL-aShelvedLeg-1 is built and the closing review has converged with 0 blockers. The build method requires the 6 leftover minors to be promoted into one batch unit, TOOL-aShelvedLeg-2: stale 'merge-bar leg' comments in two kit scripts, a typed miscount, a --rank-unparseable reading, a doc gap about GATE_SELFTESTS=changed, and the leg's rc-only pooled reading. That means another spec, build and review, roughly 1 h on this host. When should it run?
Answer: "Build 2 first"
