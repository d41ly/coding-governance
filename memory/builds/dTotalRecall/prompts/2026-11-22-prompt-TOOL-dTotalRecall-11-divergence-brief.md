**Serves:** journal TOOL-dTotalRecall-11

# Brief — dTotalRecall: TOOL-dTotalRecall-11's first build pass diverged; fold the spec to rev-7

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The unit's first builder returned a DIVERGENCE at base `4993aec72`,
recorded whole in `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-11-1-builder-return.md`.

## The brief

### Goal

Revise the spec in place as a rev-7 bump, with one revision-log line naming this brief and the builder return by their
file stems, so the next builder can build it as written over HEAD.

### Items

1. Read the builder return whole. AC4 names a review record in `aBriskPreflight`, a build whose lease reads `held` by
   another session, so the door's landed authority read (`build_records.py#check_mint_authority` through
   `placement.read_lease_class`, TOOL-dTotalRecall-2's S6) refuses it on every node. Settle it as a §8 fork decided by the
   build method's M3: name a landed review record in a build whose lease reads free (the return measured
   `memory/builds/aBatchedPacket/reviews/2026-11-13-review-TOOL-aBatchedPacket-1-diff-review-round1.md`: no RUN.md,
   Serves `diff-review TOOL-aBatchedPacket-1`, expected `-build-TOOL-aBatchedPacket-1-shape-run-1.md`, `Blocker` 0,
   `Out-tokens` 90630, `Merged` 0; re-derive each value yourself), or have the fixture free the lease, and state what
   the fixture plants. AC5 and AC6 read "that review record" and "the AC4 clone": keep them consistent with the choice.
   Where §8 F5 cites the old file name as a measurement, leave the measurement and name its date.
2. Files touched gains the three paths the builder had to declare beyond the dispatched write set:
   `memory/HYGIENE.md` (the template's `--render`), `memory/map/features/memory-tree-hygiene.md` (the dossier row) and
   `tools/run-gates/ceiling-evidence.txt` (the new leg's evidence row); name on the gates section's leg line any leg
   their guards name.
3. A §8 resolution mark is exactly `RESOLVED (agent, 2026-11-22, delegated)`: nothing else inside the parentheses (check
   12 strips code spans and refuses the rest); cite the brief after the mark.
4. Keep every other rev-6 decision; a forced change is named in the revision-log line. Every number you write carries
   an id, a path:line, PINNED or DERIVED on its line.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-11`,
`python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/writing_practice.py check pinned-facts`, and
fix every finding they name in this spec. The status header keeps `INPROGRESS`; the write grant is the spec file alone;
do not commit.

### Acceptance

The three commands exit 0 or read green; the spec carries rev-7 and one revision-log line naming this brief and the
return.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-11. No product code.
