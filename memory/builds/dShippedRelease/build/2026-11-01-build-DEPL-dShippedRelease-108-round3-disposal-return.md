**Serves:** research DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125

# Round-3 disposal return — dShippedRelease

The disposal's final return, read from the workflow journal by script, never retyped, and quoted whole.

Run wf_ee2f27b5-1d0/a292979c9f9758b2c, promoted 69, folded 0, refuted 0, standing 0.

> All 69 confirmed findings are disposed: promoted 69, folded 0, refuted 0, standing none. The report held 0 unverified findings. Its 4 refuted ids (6, 23, 40, 42) need no disposal.
>
> Units, 18 new specs, all Tier-2:
> - DEPL-dShippedRelease-108 closes id 1 (BLOCKER, B1).
> - -109 to -112 close ids 2, 29, 38, 48 (H1).
> - -113, -114 close ids 3, 22 (H2).
> - -115, -116, -117 close ids 4, 30, 49 (H3).
> - -118 closes id 50 (H4).
> - -119 closes id 5 (H5).
> - -120 closes id 21 (H6).
> - -121 closes id 39 (H7).
> - -122 closes id 47 (H8).
> - -123 closes id 59 (H9).
> - -124 closes id 67 (H10).
> - -125 is the batch: 45 MEDIUM and 7 LOW, one §2 item per raw id, order 34. It stays one unit because no split passes M6: both halves write `tools/gate-legs.json`, and each re-cut fails clause 1 on `tools/loop/kit.toml` or clause 2 on a generator input.
>
> Rescope: 18 `--rescope --act add` rows are in `memory/builds/dShippedRelease/RUN.md`.
>
> Staging: the specs and 45 amended specs are staged, each amended spec with a rev bump and a §9 line. Nothing is committed, and no index was regenerated. The audit report stays untracked for the dispatcher's commit.
>
> Verification:
> - `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,23,25` exits 0, with no line naming a new spec.
> - A read-only join finds no raw id missing, extra or duplicated, and no unpaired edge anywhere in the set.
> - Each order is one above the repaired unit's.
> - §7 leg lines come from a read-only guard join. Batch §7 also hand-names `run-gates adopter e2e` (id 44), `unattended kit gate`, `push-main self-test` and `policy check`.
>
> Gate breach to report: I ran `python tools/check-spec-tokens.py --help` to read its usage, and that script ran as the spec-tokens gate, which my role does not allow. It timed out into the background; I killed it, used none of its output, and it wrote nothing. Spec tokens has therefore not graded these specs. It stays the main loop's, along with `carries.py`.
>
> Departures, each stated in its spec:
> 1. Unit ids start at 108, since 107 is a filed ask.
> 2. New spec filenames carry today's date, 2026-11-01, as `--new-spec` would write them.
> 3. -123 F1 reads "at or above" `record-epoch` where H9's corrected fix reads "above". A release keeps the holder's epoch (TOOL-dPlacedRequest-1 S3), so "above" would refuse the honest hand-over. An earlier landing's hand-over still sits strictly below. -123 also adds a `record-epoch` field and a `--lease released` act, so unit 1's field count becomes thirteen (-125 S15).
> 4. -120 F1 picks `{kit}/ci/ci_emit.py` over M1's `.governance/deploy.toml`, which cannot fail.
> 5. -125 F3 takes id 72's accepted stop (exit 4) over id 18's exit 2 when no table is declared. Exit 2 stands when a table is declared.
> 6. -116 adds a `--facts` door to `tools/workflows/review_replay.py`, a surface of the workflows kit, because `parse_appendix_rows` drops the rows H4 needs. -109, -112 and -117 add keys to that door.
> 7. -109 S3 states the `read_pin_range` door at order 14, because the landing term needs it there. Batch S21 (id 12) keeps only the absent-kit answer.
>
> For the main loop: an order-34 batch cannot reach order 11, and M4 forbids a fold. So ids 7, 16, 17 and 37 are carried as notes on the §3 hands-off bullets of units 59, 69, 68, 102, 99, 101 and 104, which those units' builders read. Those bullets are edge text only; no scope moved.
>
> The edge list holds 210 bullets, the two amended 90-to-106 bullets included.

## Placements

| unit | repairs | order |
|---|---|---|
| DEPL-dShippedRelease-108 | DEPL-dShippedRelease-80 | 14 |
| DEPL-dShippedRelease-109 | DEPL-dShippedRelease-90 | 14 |
| DEPL-dShippedRelease-110 | DEPL-dShippedRelease-90 | 14 |
| DEPL-dShippedRelease-111 | DEPL-dShippedRelease-90 | 14 |
| DEPL-dShippedRelease-112 | DEPL-dShippedRelease-90 | 14 |
| DEPL-dShippedRelease-113 | DEPL-dShippedRelease-85 | 14 |
| DEPL-dShippedRelease-114 | DEPL-dShippedRelease-85 | 14 |
| DEPL-dShippedRelease-115 | DEPL-dShippedRelease-85 | 14 |
| DEPL-dShippedRelease-116 | DEPL-dShippedRelease-85 | 14 |
| DEPL-dShippedRelease-117 | DEPL-dShippedRelease-85 | 14 |
| DEPL-dShippedRelease-118 | DEPL-dShippedRelease-85 | 14 |
| DEPL-dShippedRelease-119 | DEPL-dShippedRelease-102 | 21 |
| DEPL-dShippedRelease-120 | DEPL-dShippedRelease-88 | 30 |
| DEPL-dShippedRelease-121 | DEPL-dShippedRelease-101 | 21 |
| DEPL-dShippedRelease-122 | DEPL-dShippedRelease-87 | 30 |
| DEPL-dShippedRelease-123 | DEPL-dShippedRelease-95 | 13 |
| DEPL-dShippedRelease-124 | DEPL-dShippedRelease-86 | 15 |
| DEPL-dShippedRelease-125 | none | 34 |
