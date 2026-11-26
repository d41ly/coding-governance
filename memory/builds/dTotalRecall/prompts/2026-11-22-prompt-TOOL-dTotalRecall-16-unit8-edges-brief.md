**Serves:** journal TOOL-dTotalRecall-16

# Brief — dTotalRecall: the edges to the deferred unit 8 dropped, unit 5's slug-class item, unit 38's arm home

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. TOOL-dTotalRecall-8 is DEFERRED to owner ask TOOL-dTotalRecall-109
(`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-8-deviation-83.md`), and `--dispatch` (check 49)
refuses a pass for a unit whose spec consumes from a sibling that is neither CLOSED nor this pass, so unit 16's
dispatch was refused on its `consumes-from TOOL-dTotalRecall-8` edge, which takes nothing (unit 8 mints no
`policy_value.py`).

## The brief

### Goal

Revise each spec named below in place, each as a rev bump with one revision-log line naming this brief by its file
stem.

### Items

1. In each of specs 2, 3, 4, 5, 7, 9, 16, 19 and 43 (`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-<n>.md`),
   delete the `consumes-from TOOL-dTotalRecall-8` bullet. Where it carried a fact the spec still needs (the policy read
   goes through `tools/memory-tree/tree_lib.py#read_policy_value`), keep that fact as one Scope or §4 sentence. Spec
   16 is INPROGRESS: keep its status. Spec 43 consumes unit 8's `code_record.py`; state in its §3 that the items
   landing on the record (its S10, S29, S55, S56 and the Files-touched row) wait with unit 8 on ask
   TOOL-dTotalRecall-109, and leave those items for its own re-ground.
2. In `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md` (DEFERRED, rev-8), delete the matching
   `hands-off` bullets to units 2, 3, 4, 5, 7, 9, 16, 19 and 43, so every edge stays two-way; keep its hands-off to
   TOOL-dTotalRecall-37 and the external one.
3. In `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-5.md` (DEFERRED, rev-6): add a Scope item,
   with a criterion observing it, that binds `tools/memory-tree/tree_lib.py#build_id_token_re`'s slug class to the
   grammar the unit exports, replacing its hard-coded `[A-Za-z0-9]+`; TOOL-dTotalRecall-38 rev-4's AC4 and
   TOOL-dTotalRecall-54 rev-3 depend on it, and spec 5 promises it today only in its edges to units 46 and 54.
4. In `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-38.md` (DEFERRED, rev-4): its `New arm:` line
   names `tools/memory-tree/id_grammar.py`, which has no self-test mode and which no leg runs; move the arm to
   `tools/memory-recall/selftest.py`, as TOOL-dTotalRecall-54 rev-3's §8 F2 did for its own arm (read it), naming the
   leg that runs that suite on the gates section's leg line.
5. Change nothing else in any spec.

Before returning, run `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <path>` over every spec you
edit, `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-2 TOOL-dTotalRecall-3
TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-7 TOOL-dTotalRecall-9 TOOL-dTotalRecall-16
TOOL-dTotalRecall-19 TOOL-dTotalRecall-38 TOOL-dTotalRecall-43` and `python tools/check-spec-tokens.py --spec <path>`
over each, and fix every finding they name in these specs. The write grant is the eleven spec files named here; do
not commit.

### Acceptance

Every command exits 0 for every spec edited; each carries its next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but those named. No product code. No other criterion changed.
