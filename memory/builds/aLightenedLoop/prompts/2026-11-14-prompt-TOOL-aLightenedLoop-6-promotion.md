**Serves:** research TOOL-aLightenedLoop-6

# Promotion — TOOL-aLightenedLoop-6: the closing review's round-1 items, batched into one repair unit

## The prompt

> Done means: the build folder and the four specs committed through `/build`, with READY → go, the units built, the closing review and the bar run, then the owner asked to land.

## The brief

### Goal
Close every confirmed item of the closing review's round 1, `memory/builds/aLightenedLoop/reviews/2026-11-14-review-TOOL-aLightenedLoop-1-5-implementation-diff-round1.md`: seven MEDIUM and one LOW. The verdict is CLEAN WITH FIXES, CONVERGED, with no blocker or HIGH. the build method's spec-audit rule (`doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`) promotes every MEDIUM and LOW at a DIFF exit into ONE batched unit naming them all. These items share the generated indexes and one generator, so they are not disjoint and stay one unit. The build's parity rule binds this unit as it bound units 1 to 5.

### Items
1. M1 (id 1): `print_wake` in `tools/unattended/unattended.sh` reads the recorded phase, but it is not on check 39's allow-list (`PHASE_RECORDED_FNS` in `tools/unattended/check-unattended.sh`), so the unattended kit leg reds. Make the kit leg green without widening what check 39 admits beyond this one reader.
2. M2 (ids 2, 5, 10): the L5-AC4 checkout move in `tools/unattended/stop-guard.test.sh` also moves refs, so it cannot go red when `head` is dropped from `deriveLivenessKey`. Give the `head` key part a move that changes HEAD alone, so that arm goes red when `head` is dropped.
3. M3 (id 3): `run_spec_token_check` in `tools/unattended/unattended.sh` derives the cache key after its tree-stability bracket closes, so an edit made during the replay can be recorded under a verdict from the earlier tree. Bring the key derivation inside the bracket, or otherwise make a moved tree refuse to record, and arm it.
4. M4 (id 6): the liveness cache's near-expiry arm stores a deadline that has already passed, so the `wait+1` margin is never exercised. Place the arm on the margin's boundary, so a change to the margin turns it red.
5. M5 (id 7): spec 1's AC4 half "no stamp on a red write" has no arm. Add one to the build-index selftest.
6. M6 (id 8): three of `--wake`'s FULL reasons in spec 2's table have no arm: the clock probe, the task probe, and the LANDING/terminal/absent phase. Add one arm per reason.
7. M7 (id 11): check 29's staged INPROGRESS path calls `read_carries_texts` twice over every chain spec. Read once, with the verdict and its bytes unchanged.
8. L1 (id 9): the "input record cannot be replayed" not-recorded branch of the spec-token cache has no arm. Add one.
9. Left-shift (M8): the review names three new bug classes — `boundary-arm-sits-past-its-margin`, `refusal-branch-with-no-arm` and `hot-path-reads-its-input-twice`. Record each as a `memory/gotchas/` class, owing `gotchas.py --write` and a dossier claim, unless an existing class already covers it, which the spec states with evidence.

### Acceptance
Each item has an observation that proves it closed: the kit leg's check 39 green (M1); each new or moved arm named on a `New arm:` line, with its staged break stated (M2, M3, M4, M5, M6, L1); M7's verdict and output byte-identical before and after on the real tree, with `read_carries_texts` called once (a count probe); and the gotcha records present and indexed. Parity holds for every touched check.

### Gates
The build's merge bar at the close; the unattended pooled suites for the `tools/unattended/` items.

### Non-goals
No behaviour beyond the eight items. The owner's rulings recorded in the review's by-design block stand: unit 1's staged stamp under the `[class]` override, unit 3 unscoped, unit 5's fault path and its default-on cache with a kill switch.

### Limitations
The build brief's limitations hold: `memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md`.

### Reuse
The fixtures units 1, 2, 3 and 5 added to `tools/unattended/unattended.test.sh`, `tools/unattended/stop-guard.test.sh`, `tools/check-spec-tokens.test.sh` and the build-index selftest.
