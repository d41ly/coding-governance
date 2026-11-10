# Revision brief — aSmoothedDispatch: spec 5 owes the hand-off edge spec 7 consumes

**Serves:** research TOOL-aSmoothedDispatch-5

## The brief

### Goal
The bar at `e1781668e` reds memory hygiene check 12: spec 7 declares a §3 `consumes-from` edge to `TOOL-aSmoothedDispatch-5`, and spec 5 declares no matching `hands-off` edge to `TOOL-aSmoothedDispatch-7` back, "so one author read the handoff and the other never saw it". Spec 7 is right: it consumes unit 5's `--spec` mode. Revise spec 5 as a rev bump with its revision-log line naming this record, adding the matching `hands-off` edge in §3 in the form the template and check 12 read. The spec stays CLOSED: this records an edge its built code already honours, and changes no design, scope or criterion.

### Items
1. Spec 5 §3 gains a `hands-off` edge to `TOOL-aSmoothedDispatch-7`, naming what it hands off: the checker's one-spec `--spec` mode, which unit 7's overlay tells the spec writer to run.
2. A revision-log line for the new rev, scoped to §3, naming this record.

### Acceptance
`bash tools/memory-tree/check-memory-hygiene.sh --only 12` exits 0, run by the main loop. `python tools/check-spec-tokens.py --spec` on spec 5 is not run, because spec 5 is CLOSED and the scoped mode grades live specs only.

### Gates
memory hygiene check 12, run by the main loop.

### Non-goals
Any other change to spec 5, any change to spec 7, and the other four red legs of the same bar.
