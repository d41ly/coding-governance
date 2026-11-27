**Serves:** journal TOOL-dTotalRecall-52
**Caused-by:** TOOL-dTotalRecall-52

# Brief — dTotalRecall: fold TOOL-dTotalRecall-52 rev-6 over its builder's divergence

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 52's builder, dispatched at `d1920cb20`, returned a divergence
(`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-52-1-builder-return.md`): AC3 and AC5 cannot both
hold. The merged home keeps old-home row 24452, whose derived section anchor spells `legacy-records` (an untagged heading
of the dClosedLoop systems-retrofit review), so AC3's grep over `memory/project` prints it, and dropping the row reds AC5.

## The brief

### Goal

Revise unit 52's spec in place as one rev bump, with one revision-log line naming this brief by its file stem, so AC3
and AC5 can both hold.

### Items

1. Decide the fork by M3 and record it in §8 as `RESOLVED (agent, 2026-11-23, delegated)`, the brief cited after the
   mark: (a) AC3's pathspec also spares `memory/project/record-kinds-legacy.txt`, a ledger home whose rows key derived
   anchors and name no population; (b) AC3 greps the old name only as a carrier spelling (`legacy-records.txt`, or the
   quoted `"legacy-records"`), which its Red-when line already describes. Re-derive at HEAD which survives: whichever
   holds the carrier lines §1 counts (18 in 6 files, DERIVED in spec 52 §1) red at the base and nothing at the tip, with the merged home's anchor
   row present. Make AC3, its Red-when line, §1's carrier count and §8 F2 agree.
2. Change nothing else; every other claim held at HEAD (the builder's return lists them).
3. A §8 resolution mark has nothing else inside the parentheses; every number carries an id, a path:line, PINNED or
   DERIVED on its line.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-52` and
`python tools/check-spec-tokens.py --spec <path>`, and fix every finding they name. The status header keeps `INPROGRESS`;
do not commit.

### Acceptance

Both commands exit 0; the spec carries the next rev and one revision-log line naming this brief; AC3 and AC5 no longer
conflict.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No spec but unit 52's.
