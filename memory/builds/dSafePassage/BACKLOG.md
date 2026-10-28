# dSafePassage — asks

## Asks

- TOOL-dSafePassage-14 · filed 2026-10-21 · build every roster unit of this build from its spec, filed by the opening so the spec run closes by carry-forward with each unit's spec header advancing this ask (README rule 1) · accept every unit of the README's `roster:units` pair is built from its spec and CLOSED, the last one's header carrying `closes` for this ask
- TOOL-dSafePassage-60 · filed 2026-10-23 · THE SPEC AUDIT'S DISPOSAL STAGE HANDS BACK SPECS THE MEMORY HYGIENE HOOK REFUSES. In this spec run the disposal stage of `tools/workflows/unattended-build.js` wrote the promoted specs of seven rounds, and five rounds' output failed the pre-commit hook: check 12 (a column-0 label line, a scope item with no criterion) in round 1, check 25 (a retirement item with no **Readers:** clause, an unbuilt reader named) in rounds 1, 3, 5 and 7, and check 7 (a title rendering an index row over its cap) in round 6; each time the main loop dispatched a spec writer before it could commit, and one promoted spec arrived FORKED · accept the disposal stage runs `bash tools/memory-tree/check-memory-hygiene.sh --staged` over a copy of the index holding its specs, and folds every finding it names before it returns, seen red on a planted promoted spec carrying a retirement item with no Readers clause
- TOOL-dSafePassage-79 · filed 2026-10-28 · THE UPGRADE-WALK LEG'S SUMMARY SUBTRACTS RED LINES FROM A COUNT OF UNITS. TOOL-dSafePassage-69's measured `--case down` run printed `down -1 passed 2 red` (`tools/govkit/upgrade_walk.py:944`), handed off in its §3 as recommended as its own unit, and the closing diff review's M10 (id 20) found no row receiving it · accept the leg's summary prints passed and red per unit, seen red on a whole-tree case with two red lines

## Dispositions

- SEV · TOOL-dSafePassage-14 · MED · the build's units stay unbuilt and its owned gaps open
- SEV · TOOL-dSafePassage-60 · LOW · every spec-run round with promotions costs a main-loop spec-writer dispatch before its commit
- SEV · TOOL-dSafePassage-79 · LOW · a merge-bar leg's summary can print a negative or overstated pass count, its exit still correct
- DEFERRED · TOOL-dSafePassage-14 · until TOOL-dSafePassage-1 · filed 2026-10-21; the build run, which builds TOOL-dSafePassage-1 first; the spec run specced and deferred every roster unit, each header advancing this ask, and the build run builds them (README rule 1)
- DEFERRED · TOOL-dSafePassage-60 · until TOOL-dSafePassage-1 · filed 2026-10-23; the change is to tools/workflows/unattended-build.js, outside this build's goal and its grant, so the build run, which builds TOOL-dSafePassage-1 first, re-reads it and either adopts it as a unit or files it with the kit's owner
- DEFERRED · TOOL-dSafePassage-79 · until TOOL-dSafePassage-77 · filed 2026-10-28; TOOL-dSafePassage-77 S4 builds the per-unit count
