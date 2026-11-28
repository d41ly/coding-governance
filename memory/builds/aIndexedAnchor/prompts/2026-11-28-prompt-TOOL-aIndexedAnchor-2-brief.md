# Brief — aIndexedAnchor: a record of another build is not a build commit

**Serves:** research TOOL-aIndexedAnchor-2
**Caused-by:** TOOL-aIndexedAnchor-1

The push bar over aIndexedAnchor's landing redded `pass-order history`, OWN: `TOOL-aIndexedAnchor-1 — BUILT at
1b161ee30 with NO tracked spec at that commit's parent 229f1ddef`. 1b161ee30 is that unit's SPEC commit. The owner
was asked how to clear it, offered fixing the gate and re-landing, and chose it.

## The prompt

> Fix the gate, re-land

## The brief

### Goal
`build_commit` stops taking a commit for a unit's build commit when the only paths it touches outside the
unit's own build folder and the declared record surface are another build's `BACKLOG.md` or `README.md`.

### Items
1. `build_commit` in `tools/unattended/lib-unattended.sh` excludes, beside the graded build's own folder,
   every sibling build folder's `BACKLOG.md` and `README.md`, the builds root derived from the build folder it
   is handed. Both callers, `check-pass-order.sh` and `check-brief-recorded.sh`, take it through the one
   predicate. The exclusion line `check-pass-order.sh` prints names the new surface.
2. An arm in `tools/unattended/check-pass-order.test.sh`: a build whose spec commit also writes another
   build's `BACKLOG.md` row and `README.md`, then builds product code in a later commit, grades conforming; a
   commit naming the unit that touches another build's `BACKLOG.md` and a product file is still its build
   commit.

### Acceptance
The new arm, seen red with the sibling exclusion removed and green with it; its product-file half red in
neither.

### Gates
`pass-order history`, the unattended kit's test legs this file trips, and every leg the spec's files trip.

### Non-goals
Any `.unattended.conf` key, `SHARED_RECORDS` or `GENERATED_INDEXES` among them; `pass-order-waiver.txt`; the
ask door `gov_record.py new build-readme`; any file of TOOL-aIndexedAnchor-1; history.

### Limitations
History is never rewritten and the waiver ledger is shrink-only, so the gate's predicate is the fix. Every
`-e` pattern `build_commit` passes is a regex built from a conf value (the conf-value-interpolated-into-a-regex
class), and a value holding a backslash switches off the leg's lineage memo (`check-pass-order.sh` near
line 557), so the new pattern lives in the code, not in a conf value.

### Reuse
`build_commit`'s `_bc_ex` already carries `-e ^<path>` exclusions beside `-e "^$_bc_dir/"`; the sibling
pattern joins that list. Why the case arises: `gov_record.py new build-readme --asks` refuses an ask filed
in the new build's own `BACKLOG.md`, so a build opened for an ask writes its row into the build that raised
it, here `memory/builds/dTotalRecall/BACKLOG.md`, and the index render rewrites that build's `README.md`.
The pass-order log's exclusion line named every other path 1b161ee30 touched as excluded. Recall terms
used: build_commit exclusion build folder sibling BACKLOG README spec commit pass-order SHARED_RECORDS.

## Drawn from the session

> Should I spec and fix the pass-order gate, rename the two helpers, merge the peer's fix branch and re-land, or hold the landing where it is?
— agent, 2026-11-28, the question the owner answered

## Owner confirmation

Asked: Should I spec and fix the pass-order gate, rename the two helpers, merge the peer's fix branch and re-land, or hold the landing where it is?
Answer: Fix the gate, re-land

## route
- build: aIndexedAnchor
- unit: TOOL-aIndexedAnchor-2 · spec memory/builds/aIndexedAnchor/spec/2026-11-28-spec-TOOL-aIndexedAnchor-2.md
- brief: memory/builds/aIndexedAnchor/prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-2-brief.md
