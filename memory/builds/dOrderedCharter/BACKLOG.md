# dOrderedCharter — asks

## Asks

- PLAY-dOrderedCharter-38 · filed 2026-10-21 · build every roster unit of this build from its spec, filed by the opening so the spec run closes by carry-forward with each unit's spec header advancing this ask (README rule 1) · accept every unit of the README's `roster:units` pair is built from its spec and CLOSED, the last one's header carrying `closes` for this ask
- PLAY-dOrderedCharter-56 · filed 2026-10-26 · THE SLOTS NAME dBoundRoles AS THEIR RENDERER. PLAY-dOrderedCharter-17's non-goals say dBoundRoles renders the work order's slots, and clauses cl-dClosedLoop-0195 and cl-dClosedLoop-0203 give slot rendering to dFurnishedOrders, whose TOOL-dFurnishedOrders-4 specs `render_slot` · accept PLAY-dOrderedCharter-17's non-goals name TOOL-dFurnishedOrders-4 as the slots' renderer, amended by a rev bump with its §9 line
- PLAY-dOrderedCharter-57 · filed 2026-10-26 · THE LOAD SET TAKES NO FEATURE SELECTION. TOOL-dFurnishedOrders-18 selects a work order's instruction units by `feature.*`, adding a `features` argument to PLAY-dOrderedCharter-11 S1's `derive_load_set` · accept PLAY-dOrderedCharter-11 S1 carries the `features` argument and reports the selector `unarmed` while no `feature` namespace is registered, seen on a fixture with none registered
- PLAY-dOrderedCharter-58 · filed 2026-10-26 · THE FEATURE SELECTOR NAMES THE WRONG ARMING BUILD. PLAY-dOrderedCharter-25 §3 says dTotalRecall arms the `feature` selector, and clause cl-dClosedLoop-0209 says dLinkedLibrary does · accept PLAY-dOrderedCharter-25 §3 names dLinkedLibrary, amended by a rev bump with its §9 line
- PLAY-dOrderedCharter-59 · filed 2026-10-26 · THE TYPED-KIND FILE-NAME JOIN READS A LOOSE STEM. The typed-kind join PLAY-dOrderedCharter-42 generalises from `deviation_named` reads any record ending `-<kind>-<n>.md` as that kind, so once `plan` joins `TYPED_RECORD_KINDS` the six research records `2026-10-20-build-PLAY-dClosedLoop-1-execution-return-plan-2.md` to `-7.md` read as malformed plan records (TOOL-dRankedPlan-16 §8 F5) · accept the typed-kind file-name join reads `-<kind>-<n>.md` only on the stem `-build-<unit id>-<kind>-<n>.md`, seen on a research record named `…-return-plan-2.md` staying bound once `plan` joins `TYPED_RECORD_KINDS`

## Dispositions

- SEV · PLAY-dOrderedCharter-38 · MED · the build's units stay unbuilt and its owned gaps open
- DEFERRED · PLAY-dOrderedCharter-38 · until PLAY-dOrderedCharter-55 · the spec run carries every unit forward DEFERRED against this ask, each spec header advancing it; the build run builds them, and its last unit in build order, PLAY-dOrderedCharter-55 at order 41 today, closes it (README rule 1)
- SEV · PLAY-dOrderedCharter-56 · LOW · a reader looks for the slot renderer in a build that does not spec it
- SEV · PLAY-dOrderedCharter-57 · MED · the feature selection has no seam in its parent
- SEV · PLAY-dOrderedCharter-58 · LOW · a reader waits on the wrong build to arm the selector
- SEV · PLAY-dOrderedCharter-59 · LOW · six research records read as malformed plan records until TOOL-dRankedPlan-16 S2 narrows the stem itself
