# Revision brief — aSmoothedDispatch: the bar-reds unit is TOOL-aSmoothedDispatch-18, not -10

**Serves:** research TOOL-aSmoothedDispatch-18

## The brief

### Goal
The spec stage authored `memory/builds/aSmoothedDispatch/spec/2026-11-10-spec-TOOL-aSmoothedDispatch-10.md`, and its commit was refused by build-index verdict V9: `TOOL-aSmoothedDispatch-10` is already a filed ask in this build's `BACKLOG.md`, since asks and units share one id sequence and the main loop minted the unit id without checking. A filed id is never renumbered, so the unit takes the next free id, `TOOL-aSmoothedDispatch-18`. The README roster row and the brief now name `-18`, and the brief moved to `2026-11-10-prompt-TOOL-aSmoothedDispatch-18-bar-reds.md`. Move the spec file to `2026-11-10-spec-TOOL-aSmoothedDispatch-18.md` and change every spelling of the unit's own id in it to `-18`, including its H1, its status header and every `Observed by` or arm-marker mention of the unit itself. Repoint the brief path it names. Change nothing else: no design, scope, criterion or gate moves, and the asks `TOOL-aSmoothedDispatch-10` to `-17` it may cite keep their ids. The spec is untracked and unrevised, so it stays at rev-1 with no revision-log line, unless the template requires one for a rename.

### Items
1. Rename the file to the `-18` name and remove the `-10` file.
2. Every self-reference to the unit's id becomes `TOOL-aSmoothedDispatch-18`, and the brief path becomes the `-18-bar-reds` record.
3. Run `python tools/check-spec-tokens.py --spec` on the renamed spec, and fix any hit.

### Acceptance
A grep of the `-18` spec for `TOOL-aSmoothedDispatch-10` finds only citations of ask 10, if any. The `-10` spec file no longer exists. The one-spec token check exits 0.

### Gates
Spec tokens (`--spec`), run by the writer. The build index render and the commit are the main loop's.

### Non-goals
Any change to the spec's content beyond the id and the brief path. Any edit to `BACKLOG.md`, the README or the brief.
