# Revision — dRedressedBar: TOOL-dRedressedBar-15, unit 14's stale CONFIGURE comment folded in

**Serves:** research TOOL-dRedressedBar-15 TOOL-dRedressedBar-14

## The brief

### Goal
Unit 14's builder ran the bug-class checklist over its pass `109fbb4ab` and it selected `amendment-leaves-its-other-half-standing`. The comment above `_cfg_run` in `_cmd_apply` (`tools/govkit/govkit.py:7811-7815` at `ffe73d97d`, written by TOOL-dRedressedBar-13) still says CONFIGURE runs "before the receipt is written" and calls a decode error there the F4 no-receipt half-install. Since unit 14 writes the receipt ahead of CONFIGURE, that holds only for the final RECEIPT write: a decode error there now leaves the early receipt behind. Unit 14's builder could not fix it because scratch-guard closes a CLOSED unit's product writes. Unit 15 writes `tools/govkit/govkit.py` next, so fold the correction into spec 15.

### Items
1. **TOOL-dRedressedBar-15** — bump the rev and add one S-item: the comment above `_cfg_run` is restated so it says what is true after unit 14, namely that the early receipt is already written when CONFIGURE runs and RECEIPT rewrites it, and what a decode error there would leave behind. Add one AC that reads the comment at the tip (a joined text cut that carries no `before the receipt is written`) with its "Red when" naming `ffe73d97d`. Name the finding in the §9 line. The comment change is a comment only: no code line moves, so no new arm.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 15 READY. Spec 15's §4 Files touched still lists `tools/govkit/govkit.py` and names no other spec.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 15. No status change.
