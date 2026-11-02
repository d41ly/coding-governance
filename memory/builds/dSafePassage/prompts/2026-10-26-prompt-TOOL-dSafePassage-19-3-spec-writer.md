**Serves:** research TOOL-dSafePassage-19

# Brief: TOOL-dSafePassage-19's S2 drops the predicate call the stamp has no use for

## The prompt

No owner prompt: the build run's second builder of TOOL-dSafePassage-19 (`wf_b6e80581-a59`) handed it back as a DIVERGENCE between S2 and §7, and the run revises the spec under M2.

## The brief

### Goal

S2 states what the rollback stamp does without a `test_steps_recordable` call, so §7's staged break can still turn the arm red, and the unit builds as its fixture plants and arm over behaviour that already holds at HEAD.

**The defect.** S2 has the rollback stamp write no `steps` key "asking test_steps_recordable and adding nothing the predicate rejects", and TOOL-dSafePassage-16's spec (line 64) hands that call to this unit. §7's New arm stages its red by "a re-read that keeps a key the disk dropped". At HEAD the stamp (`tools/govkit/govkit.py:12688-12689`, `:12731`) adds no key at all. Any predicate call breaks one section: (a) dropping `steps` where the predicate rejects makes §7's break unobservable, since the stamp would remove the stale list the broken re-read kept (charter [gate]); (b) refusing there is a refusal no section names; (c) not calling departs from S2's wording. The builder measured both plants (`schema-step`, `schema-step-kill-before-stamp`) passing AC1 and AC2 over HEAD's product code: S1 already holds in `run_step_reread` (`tools/govkit/upgrade_steps.py:985-989`) and S3 comes from TOOL-dSafePassage-18's verdict list.

**The direction.** S2 drops the predicate call: the stamp adds no key, S1's re-read is what keeps the dropped `steps` out, and §7's break stays as written. State in one line that S1, S2's outcome and S3 already hold at HEAD (by TOOL-dSafePassage-4 and -18), so this unit's build is the two fixture plants, their `schema.block-after` trigger, the `[dSP-19]` selftest rows (tagged dSP-19, since `check_step_rollback`'s `startswith("schema-step")` test would label them dSP-18) and its ledger. Correct the outcome-neutral citation too: the rollback branch reads `receipt.get("schema", schema)` (TOOL-dSafePassage-4 S5), not TOOL-dSafePassage-3 S5's `max(schema, 3)`.

### Items

1. **Revise TOOL-dSafePassage-19** as a rev bump dated 2026-10-26, still `DEFERRED`: S2 as above; §4 Files touched and Inventory to match the reduced build; the citation fix; one §9 line names this brief.
2. **TOOL-dSafePassage-16 is CLOSED**: do not edit it; report its line 64 hand-off as superseded in your return.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- S2 names no `test_steps_recordable` call, and §7's staged break is unchanged.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.
- `bash tools/unattended/unattended.sh --plan dSafePassage --paths` lists TOOL-dSafePassage-19 READY.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code; no edit of a CLOSED spec.
- No commit, no stage into the real index, no deviation record.
