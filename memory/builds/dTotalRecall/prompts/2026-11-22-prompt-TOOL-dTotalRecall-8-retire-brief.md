**Serves:** journal TOOL-dTotalRecall-8

# Brief — dTotalRecall: TOOL-dTotalRecall-8 retired by its own losing test, and the units that only served it

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 8's first builder timed the cold code record at the pass base and
it lost AC1 (`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-8-1-builder-return.md`); the main
loop took §8 F1's RESOLVED loss route, recorded the amendment (`--rescope --act retire`) and
`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-8-deviation-83.md`.

## The brief

### Goal

Carry the retirement into the specs, each as a rev bump with one revision-log line naming this brief by its file
stem.

### Items

1. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md` (INPROGRESS, rev-6): set the status to
   `WONTDO` with the tail the spec format requires, a reason pointer to deviation 83; remove the `closes` list from
   the header, since the record that would have answered TOOL-dTotalRecall-102 and -103 is not built; keep §8 F1 as it
   is and add one line under it saying the loss route was taken, with the measurement and the deviation's file stem.
   Keep its hands-off bullets to units 2, 3, 4, 5, 7, 9, 16 and 19 (the policy-read note stays true), and say in each
   hands-off to TOOL-dTotalRecall-37 and -43 that the record is not built.
2. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-37.md` (DEFERRED, rev-3): unit 37 narrows the
   `.gitattributes` generated registration so the code record keeps the hand-written workflow scripts. Read it whole
   and decide by M3 whether any of its scope stands with no code record. Where none does, set it `WONTDO` with a
   reason pointer naming TOOL-dTotalRecall-8's retirement and deviation 83; where some does, cut its scope to that, as
   a rev bump. Name the decision in your return.
3. `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-43.md` is NOT yours to edit: list in your return
   each of its items that lands on `code_record.py`, its cache or the `code record` leg, for its own re-ground.
4. Keep every edge two-way: where a spec you edit drops or rewords an edge, its partner must still match, or hygiene
   check 12 refuses it; name any partner edge outside your grant in your return.

Before returning, run `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <path>` over each spec you
edit, `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-37` and
`python tools/check-spec-tokens.py --spec <path>` over each spec you edit, and fix every finding they name in your
specs. The write grant is specs 8 and 37; do not commit.

### Acceptance

Every command exits 0 for the specs you edit; each carries its next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but 8 and 37. No product code. No new design for a code record.
