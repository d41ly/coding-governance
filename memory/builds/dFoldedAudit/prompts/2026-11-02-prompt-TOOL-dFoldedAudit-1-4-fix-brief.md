# Fix brief — TOOL-dFoldedAudit-1: the bar join's one hit

**Serves:** research TOOL-dFoldedAudit-1

## The brief

### Goal
Clear the one spec-token hit left on TOOL-dFoldedAudit-1, so `--dispatch` admits it. Commit nothing; the main loop commits and runs the checker.

### Items
1. `tools/check-spec-tokens.py` reports `[bar] tools/memory-tree/kit-dogfood-parity.test.sh` on this spec: a bar or suite is not an acceptance observation. Reword the §6 clause it hits, AC15 most likely, so the observation is the extracted block run alone over a scratch fixture, as AC15 already says it runs, without spelling the suite file in that criterion. Read `scan_bar` in that checker to see which spellings it grades. The `New arm:` line may keep naming the suite.

### Acceptance
TOOL-dFoldedAudit-1 carries a rev bump and a §9 line, its status cell stays INPROGRESS, and the checker reports no hit naming this build.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No change to what is observed, no code, no write outside this one spec.
