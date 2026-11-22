**Serves:** journal TOOL-dTotalRecall-54

# Brief — dTotalRecall: unit 54 lands the keyword-only `alt` unit 38 consumes

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 38's second re-ground
(`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-38-reground-2-return.md`) decided its F4: its
caller-bound readers call `parse_id_parts(ident, root, alt=...)` with a family alternation their own validator used.

## The brief

### Goal

Revise unit 54's spec in place, folding this into the rev-5 already in the working tree (one more revision-log line
naming this brief by its file stem), so unit 54 builds first in step 8 and lands what unit 38 rev-6 consumes.

### Items

1. Read `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-38.md` rev-6 for its F4 and its §4 stop
   condition. Add to unit 54's S1, its design sketch and a criterion a keyword-only `alt` on `parse_id_parts`: a
   caller passing it matches the family part against that alternation and skips the tree's families; omitted, the
   tree's families apply as rev-5 states. A criterion observes both answers on one id.
2. State in §3 that unit 54 builds before units 38 and 4 inside step 8, and add the `hands-off TOOL-dTotalRecall-38`
   bullet naming `parse_id_parts` with `root` and `alt`, if the edge is not already there.
3. Keep every other rev-5 claim.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-54
TOOL-dTotalRecall-38`, `python tools/check-spec-tokens.py --spec <path>` and
`python tools/playbook/writing_practice.py check pinned-facts`, and fix every finding they name in unit 54's spec.
The write grant is unit 54's spec alone; do not commit.

### Acceptance

The commands exit 0 or read green; unit 54's spec carries `alt` in S1, its sketch and one criterion.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but unit 54's. No product code.
