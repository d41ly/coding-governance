**Serves:** journal TOOL-dTotalRecall-48
**Caused-by:** TOOL-dTotalRecall-48

# TOOL-dTotalRecall-48 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `c4a7d234b` from [2026-11-22-prompt-TOOL-dTotalRecall-48-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-48-build-brief.md), recorded whole; the pass commits are `4d1d9899a` and `5284138ed`.

## Why

TOOL-dTotalRecall-48 is built as its rev-3 spec states, in two pass commits, both carrying `Pass: TOOL-dTotalRecall-48`. The first, 4d1d9899a, holds the build and flips the spec to CLOSED. The second, 5284138ed, is a fix. The first commit wired `check_cause_line` into the record check, which means a record refusal can now name the `cause` rule. Nothing in the spec covers `tools/runlog/record.py#RECORD_RULES`, the closed list that every refusal must name, or `tools/runlog/selftest.py#test_schema_ac2_refusals`, which asserts that the rules it stages equal that list. Without the second commit `runlog selftest` would fail at the close. The second commit adds `cause` to the list and a `cause unserved` test case. Deviation record memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-48-deviation-1005.md documents it (cause: builder discovery; approver: author-recorded).

## Summary

Unit TOOL-dTotalRecall-48 is built and closed in two commits: 4d1d9899a (the build, spec set to CLOSED · rev-3 · 2026-11-23) and the fix 5284138ed on top. No gate, suite or merge bar ran in this pass. `runlog selftest`, `runlog record schema`, both run-log line legs, `policy fixtures` and `memory hygiene` all still need to run at the close.

**What changed in `tools/runlog/record.py`**
- `render_markdown` now writes `render_cause_line(serves)` at line 4, directly under the Serves line (S3).
- `check_record_lines` treats line 4 as the cause line when it matches the new constant `CAUSE_LINE_RE`, and then expects the fixed tail one line lower. Otherwise it uses the old six-line head. Any other line 4, or a second cause line at line 5, gets the existing fixed-text finding. The body loop now starts at the head's real length (S1).
- `check_cause_line` returns nothing when the cause line is empty or missing. It tests the target against the Serves tokens, checking each `N..M` range through `UNIT_RANGE_RE` arithmetically. A range used as the target is refused (S2).
- The second commit adds `cause` to `RECORD_RULES`; this is the deviation described above.

**What changed in `tools/runlog/selftest.py`**
- Unit 36's cut-cause test in `test_record_cause_line` is rewritten to the new rule: an unserved cause gives one finding naming `X-xFixtureRun-9`; an empty or missing cause line passes; a cause opening a served range passes.
- New `test_record_cause_head` covers AC1 and AC3 over `build_landed_fixture`: the render has its cause line at line 4 and grades clean, the version with the cause cut grades clean, and a doubled cause line gives the fixed-text finding at line 5.
- `test_schema_ac2_refusals` gains a `cause unserved` case at line 4.

**Records committed:** `memory/map/generated/symbols.json`, written by `gen_map.py --write`. The files rewritten by `gen_build_index.py --write`: `memory/LIVE.md`, `memory/backlog/TOOL.md`, the dTotalRecall README, this unit's spec records region, and the dClosedLoop as-built view. Also the acceptance ledger memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-48-1-acceptance-ledger.md, deviation 1005, and the dispatch rows in RUN.md.

**Write declarations:** extra paths were declared with `--dispatch`. On the second commit's first attempt the commit hook refused (unattended check 49): the pass had moved to 4d1d9899, so its earlier declarations no longer covered `record.py`, `selftest.py` or the ledger. I re-declared all five paths with the command the hook named, and the commit then went through.

**Checks that ran** (each stands in for `runlog selftest` or `runlog record schema`). All are scratch scripts under the scratchpad that call the record functions directly; no test function was run.
- `probe48.py` on the landed fixture:
  - AC1: line 4 is `**Caused-by:** X-xFixtureRun-1` and `check_record_lines` returns `[]`.
  - Cut cause line: `[]`.
  - Doubled cause line: fixed-text findings at lines 5, 6 and 7.
  - Unserved cause in the head: one `cause` finding at line 4.
  - AC3 direct calls: `X-xFixtureRun-9` against `[X-xFixtureRun-1]` gives one finding; empty and missing lines give none; `X-xFixtureRun-1` against `X-xFixtureRun-1..2` gives none; a range target and an id past the range each give a finding.
- `probe48b.py`: the `cause unserved` case lands on line 4 and every finding it produces is in `RECORD_RULES`.
- `probe48c.py`: running `check_record_lines` with the six-line head tuple restored reds AC1 at line 4, so the staged break can fail.
- AC2 stand-in: all 37 tracked `*-runlog-*.md` records have a blank line 4, so they grade under the same head as before. The real `runlog.py check-records` run is owed at the close.
- `lexicon.py --suggest` accepted `test_record_cause_head`; `lexicon.py --measure` still reads `VERB_OFFENDER_PIN` 1435, unchanged.
- No command timed out.

**Still owed at the close**
- AC1 and AC3 through `runlog selftest`.
- AC2 through `runlog record schema`.
- The first-failure checks for the new arm: `test_record_cause_head` and `test_record_cause_line`, broken by restoring `(TITLE, "", None, "", INTRO, "")` in place of the `head = ... if cause else ...` line. That tuple now appears once, as the conditional's else-branch, so anchor on the whole `head =` line. Watch for stale bytecode between staged edits.
- The `cause unserved` case in `test_schema_ac2_refusals`.
- A risk the probes cannot rule out: the extra head line adds about 35 bytes per record (DERIVED, the cause line's length), so any selftest that pins a byte count near the 24576 cap may move.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` was run after both commits. Acting on retirement-inventory-misses-readers-by-value is what found the `RECORD_RULES` reader. guard-above-a-fold (the `line or ""` fallback was removed), a-new-local-collides (`cause` and `head` are bound nowhere else in the function), insert-after-a-key-that-occurs-twice (the record has one cause line), containment-tested-one-way (range targets are refused) and line-claim-matched-over-the-whole-output (checks are per finding) were all checked; none needs a further fix.

Left for unit 60: the runlog README's head description and its `RECORD_SCHEMA` cause key.
