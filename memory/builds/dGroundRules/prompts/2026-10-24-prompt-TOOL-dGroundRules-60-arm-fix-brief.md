**Serves:** research TOOL-dGroundRules-60

# Arm fix brief — TOOL-dGroundRules-60's AC2 runs the overlap arm itself

## The prompt

> The builder of TOOL-dGroundRules-60 handed back a DIVERGENCE: TOOL-dGroundRules-52 rev-7 closes S21 through TOOL-dGroundRules-40's arm (`check_overlap_pair` and its one assertion in `tools/check-spec-tokens.test.sh`), not through TOOL-dGroundRules-45's `PAIRS_TABLE`, and its AC5 runs `PAIRS_PY`/`PAIRS_SH`; so AC2's `PAIRS_TABLE` reading no longer observes the check S21 names.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-60.md` so AC2 observes the overlap arm itself failing on the Python rule alone. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. §1, §2 S2 and §4 Evidence state that TOOL-dGroundRules-52 S21 is closed by TOOL-dGroundRules-40's arm, whose row function `check_overlap_pair` and one assertion TOOL-dGroundRules-56 (9bea9c85e) made the suite's last arm before `total=`, so they run alone.
2. AC2 runs that arm alone (the shape of TOOL-dGroundRules-56's `ROW_CHECK_RUN`, spelled whole in the fenced literal block) under `PY_RAW` in a scratch copy, and expects one `arm FAIL` line naming the trap row and `check_writes_intersect` and not `overlaps`; on the built tree, unstaged, the arm prints no FAIL. Its Red when names the case it catches: a Python rule broken alone that the arm does not report.
3. Drop the claim that AC2 observes `PAIRS_TABLE`'s Python column, and the consumes-from edge on TOOL-dGroundRules-45 if nothing then consumes from it, adjusting TOOL-dGroundRules-45's matching hands-off line only if hygiene check 12 requires it (45 is CLOSED: prefer keeping an edge that still names something this spec uses).
4. The status header's rev rises by one, with a revision-log line naming the divergence and the ruling. Every acceptance-section code span stays on one line; every acceptance bullet keeps a `Red when:` clause; no acceptance line starts at column 0 with `AC<n>`; no code span holds a path glued to a quote or a `rev:path` token; an untracked or fixture-relative path sits inside a fenced block or carries its target placeholder; every command runs from the repository root.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec or TOOL-dGroundRules-45.

### Gates
Memory hygiene only.

### Non-goals
Any other spec beyond item 3's edge; product code; the status cell, which stays `DEFERRED`.

### Limitations
TOOL-dGroundRules-62 builds while this runs and touches neither spec.

### Reuse
TOOL-dGroundRules-56's `ROW_CHECK_RUN` probe shape.
