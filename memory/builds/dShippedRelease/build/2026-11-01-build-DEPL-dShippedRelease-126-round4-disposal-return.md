**Serves:** research DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138

# Round-4 disposal return — dShippedRelease

The disposal's final return, read from the workflow journal by script, never retyped, and quoted whole.

Run wf_83e0b8e3-969/aec53e777743a1a55, promoted 63, folded 0, refuted 0, standing 0.

> All 63 confirmed findings are disposed: promoted 63, folded 0, refuted 0, standing none. The report held 0 unverified findings. Its 8 refuted ids (6, 18, 29, 30, 39, 43, 49, 51) need no disposal.
>
> Units, 13 new Tier-2 specs, status OPEN:
> - DEPL-dShippedRelease-126 closes id 1 (BLOCKER, B1): `mint` classifies in the regenerate context.
> - DEPL-dShippedRelease-127 closes id 21 (BLOCKER, B1): the proof runs on a clone of gov's tracked deploy.toml, with a liveness term.
> - DEPL-dShippedRelease-128 closes id 54 (BLOCKER, B1): the regenerate population and a token class check.
> - DEPL-dShippedRelease-129 closes id 2 (H1).
> - DEPL-dShippedRelease-130 closes id 4 (H2): `render_landing_record` and `dispose-with-reason` in deploy_items.py, with AC4 become a parser test.
> - DEPL-dShippedRelease-131 closes id 5 (H3).
> - DEPL-dShippedRelease-132 closes id 22 (H4).
> - DEPL-dShippedRelease-133 closes id 23 (H5).
> - DEPL-dShippedRelease-134 closes id 55 (H6).
> - DEPL-dShippedRelease-135 closes id 56 (H7).
> - DEPL-dShippedRelease-136 closes id 57 (H8).
> - DEPL-dShippedRelease-137 closes id 58 (H9).
> - DEPL-dShippedRelease-138 is the batch: 41 MEDIUM and 10 LOW, one §2 item per raw id, order 36. It stays one unit: §8 F1 records that the only clause-1 cut holds ids 14, 31, 66 and fails clause 2 on tools/integrations/kit.toml.
>
> Rescope: 13 `--rescope --act add` rows are in RUN.md, staged by the verb. Each reason names the report id and severity it closes, and -138's names all 51 ids.
>
> Staging: the 13 specs and 32 amended specs are staged. Each amended spec has a rev bump and a §9 line. Nothing is committed and no index was regenerated. The audit report stays untracked for the dispatcher's commit.
>
> Verification:
> - `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,23,25` ran over the staged set. Its one finding was check 25 on batch S40. I reworded S40, and `--only 25` then exited 0 with no line naming this build (that form also runs check 12). The full set was not rerun after the rewording, and the sole change was one sentence of S40.
> - A read-only join over 120 units and 852 bullets found no unpaired edge, no order violation and no consumes-from cycle.
> - That join also found 63 confirmed ids (3 blocker, 9 high, 41 medium, 10 low), every minor once in -138, and each promoted spec's criteria joined to its scope. Each repair order is one above its unit.
> - §7 leg lines come from a read-only join of gate-legs.json with the broad-guard floor of 5. -138 also hand-names `unattended kit gate`, `unattended skill size`, `review-replay selftest` and `remote literals (kit code names no remote)`.
> - Spec tokens and carries.py were not run. They stay the main loop's.
>
> Decisions, each stated in its spec:
> 1. Unit ids start at 126.
> 2. -126 F1 takes the regenerate context, because widening `ANSWER_VALUE_RE` trips veto 3.
> 3. -130 F1 keeps the writer in deploy_items.py, and that verb spelling is minted there, where unit 106 S49 named only an option.
> 4. -131 F1 binds the pin class in the row's `ref` cell, `pin:<class>`.
> 5. -132 F1 takes the priced refusal: 4 of 244 tracked records stay ambiguous, pinned at e8ced8ac.
> 6. -133 F1 adds a `--root` flag to dispose-landing.
> 7. -134 F1 reads an off-line record as dead and adds no fetch.
> 8. -138 F2: a `-` bound is forged only with a non-`-` field. -138 F3 adds `applies = "regenerate"` to the `[[outcome]]` row. -138 F4 takes the exact-file guard for `deploy items`.
> 9. -138 S48 leaves `--lease epoch` unminted, so `read_lease_epoch` reads TOOL-dPlacedRequest-34 S22's `--lease status`, which is specced and DEFERRED.
>
> For the main loop: an order-36 batch cannot reach lower orders, and M4 forbids a fold. So ids 12, 41 and 47 ride as notes on the §3 hands-off bullets of units 125 and 106: the three extra write paths on 125, and the Land sentence on 106.
>
> The edge list holds 128 bullets, 71 in the new specs and 57 mirrors.

## Placements

| unit | repairs | order |
|---|---|---|
| DEPL-dShippedRelease-126 | DEPL-dShippedRelease-122 | 31 |
| DEPL-dShippedRelease-127 | DEPL-dShippedRelease-122 | 31 |
| DEPL-dShippedRelease-128 | DEPL-dShippedRelease-122 | 31 |
| DEPL-dShippedRelease-129 | DEPL-dShippedRelease-123 | 14 |
| DEPL-dShippedRelease-130 | DEPL-dShippedRelease-116 | 15 |
| DEPL-dShippedRelease-131 | DEPL-dShippedRelease-125 | 35 |
| DEPL-dShippedRelease-132 | DEPL-dShippedRelease-109 | 15 |
| DEPL-dShippedRelease-133 | DEPL-dShippedRelease-114 | 15 |
| DEPL-dShippedRelease-134 | DEPL-dShippedRelease-124 | 16 |
| DEPL-dShippedRelease-135 | DEPL-dShippedRelease-113 | 15 |
| DEPL-dShippedRelease-136 | DEPL-dShippedRelease-115 | 15 |
| DEPL-dShippedRelease-137 | DEPL-dShippedRelease-116 | 15 |
| DEPL-dShippedRelease-138 | none | 36 |
