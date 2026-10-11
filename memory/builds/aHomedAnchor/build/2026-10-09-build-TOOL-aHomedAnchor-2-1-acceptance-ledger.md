# Acceptance ledger — TOOL-aHomedAnchor-2

**Serves:** journal TOOL-aHomedAnchor-2

Tier-2 · node a · 2026-10-09

Observed through a slice of `tools/unattended/check-unattended.test.sh`: its prologue plus only this
build's local-anchor block, at `d31d7bc9`, 16 assertions, 19 min 10 s. Its one FAIL was the suite's
helper-placement check refusing `add_local_scope` inside a shard region; hoisted at `51518b16`, and a
prologue-only slice then read `SLICE-PASS`. No arm in the block failed. The suite was not run, by the
owner's instruction. `read_origin_scope` was also probed by hand over seven conf shapes.

**Evidences:** TOOL-aHomedAnchor-2
- AC1 — `admitted by the local anchor` — origin's conf declares local and an unpublished base on HEAD's history is admitted on the report channel
- AC2 — `is not published on the remote` — local in the working tree only, check 9 still refuses
- AC3 — `local` — origin declares local and a base off HEAD's history still reads not published
- AC4 — `local` — the off-default slug record under origin's local prints no check 29 refusal
