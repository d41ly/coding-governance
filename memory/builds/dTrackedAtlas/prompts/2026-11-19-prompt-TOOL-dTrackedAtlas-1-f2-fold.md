# Revision — dTrackedAtlas: TOOL-dTrackedAtlas-1 spec rev-2, fork F2 resolved

**Serves:** research TOOL-dTrackedAtlas-1

## The prompt

> Resolve fork F2 of TOOL-dTrackedAtlas-1 under the mandate's delegated authority (`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`) and fold it into the spec as rev-2.

## The brief

### Goal
Fold the run's resolution of fork F2 into `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-1.md` as rev-2 and commit it. The main loop resolved F2 to option (a), edit the schedule as §4 states: it is the only option meeting the owner's acceptance ("the schedule script prints builds landed 6 at 9e21ac760"), it trips none of M3's vetoes (the schedule is an instrument, not a governance carrier, and nothing under `tools/` moves), and its cost, the schedule instrument's blob moving under every chain packet's pin and `tools/chain-packet.py#INSTRUMENT_BLOBS`, is an owner re-pin (`packet.py --repin`) plus the door constant's re-pin, which the main loop files as one ask in this build's BACKLOG.md and surfaces in the wrap-up.

### Items
1. Mark F2 in §7 with the closed fork mark, in the shape `memory/TEMPLATE-SPEC.md` §8 states: `RESOLVED (agent, 2026-11-19, delegated): (a), the only option meeting the owner's acceptance; the re-pins are filed as one ask at the close.`
2. Make §6 Gates and every sentence citing F2 agree with (a) as resolved, so no "recommendation" is left standing.
3. Bump the status header to rev-2 and add one revision-log line naming F2's resolution and this record.
4. Run `bash tools/unattended/unattended.sh --check-specs dTrackedAtlas TOOL-dTrackedAtlas-1` and fix every refusal it names for this unit.
5. Stage only that spec and what `python tools/memory-tree/gen_build_index.py --write` re-renders, then commit with subject `spec(dTrackedAtlas): TOOL-dTrackedAtlas-1 rev-2 — F2 resolved, the schedule edited in place`, a `Pass: none` trailer and `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, under a `600 s` bound, since the pre-commit hook takes minutes.

### Acceptance
`bash tools/unattended/unattended.sh --plan dTrackedAtlas --paths` grades TOOL-dTrackedAtlas-1 READY, not FORKED; `--check-specs` prints no refusal for it; the commit exists on the run branch with the subject above.

### Gates
The memory hygiene gate the pre-commit hook runs; no other gate.

### Non-goals
No other section's design changes; no other spec, no product code, no `--no-verify`, no `git add -A`.
