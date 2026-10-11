---
slug: aTrimmedHook
node: a
opened: 2026-10-11
streams: tooling+kickoff
roster: TOOL+KICK
ids: KICK-aTrimmedHook-1 TOOL-aTrimmedHook-1 TOOL-aTrimmedHook-2 TOOL-aTrimmedHook-3
authorized-by: prompt
---

# aTrimmedHook — a one-file commit's hooks cost seconds, not minutes

## The problem this build exists to solve

A commit staging one `RUN.md` spends minutes in hooks on node a: the staged hygiene leg re-renders
the whole build index and walks the whole memory listing, the kickoff-manifest leg runs on every
commit whatever it stages, and `commit-msg` boots the 14k-line unattended driver to answer a
question that is almost always "no run here". Every check stays whole at the push boundary. The
owner's prose, with the orientation that refuted two of its premises, is the mandate, recorded under
[prompts/](prompts/2026-10-11-prompt-TOOL-aTrimmedHook-1-brief.md).

## Expected improvements

- A staged edit that cannot move the build index skips check 9's render, announced.
- The staged hygiene leg spends no process on a check whose staged selection is empty.
- manifest-check's staged leg returns at once when nothing it reads is staged.
- `commit-msg` starts the unattended driver only when a run names the branch.

## Detriments if this is not built

- Every commit on a busy node keeps paying minutes for checks that cannot change their answer.
- Sessions keep reaching for `--no-verify`, which skips the checks that do matter.
- Timing work keeps being contaminated by hook runs that dwarf what they measure.

## Build-level rules

- **Classification (M2)**: four units, MISSING at open, authored this run, one mechanism each.
- TOOL-1 and TOOL-2 both write `check-memory-hygiene.sh`: sequenced, 1 then 2. KICK-1 and TOOL-3
  are disjoint from them and from each other.
- Tiers per the manifest's tier rule: TOOL-1, TOOL-2 and KICK-1 are Tier-2 (gate semantics of a
  shipped checker); TOOL-3 is Tier-1 (a gov-only hook).
- Every skip announces itself, and no full run (STAGED=0) changes behavior.
- One kit-version bump per touched kit, after the last unit: memory-tree, kickoff-manifest.
- Owner rulings: the exact classifier for check 9; narrow and skip empties; no spec audit.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aTrimmedHook-1` | `gen_build_index.py --check --staged` classifies the staged set; hygiene check 9 renders only when it can move |
| 2 | `TOOL-aTrimmedHook-2` | hygiene `--staged` narrows FILES, skips PRE_* and empty selections, holds the legacy/debt guard unless a list is staged |
| 3 | `KICK-aTrimmedHook-1` | `manifest-check.sh --staged` skips, announced, when nothing staged touches the manifest, watch or verify-paths; C6 in one spawn |
| 4 | `TOOL-aTrimmedHook-3` | `.githooks/commit-msg` runs the unattended driver only when a tracked RUN.md names the current branch |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 1 unit(s) · node a · opened 2026-10-11 · streams tooling+kickoff
ids KICK-aTrimmedHook-1 TOOL-aTrimmedHook-1 TOOL-aTrimmedHook-2 TOOL-aTrimmedHook-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTrimmedHook-1 — check 9 under `--staged` renders the build index only when the staged set can move it](spec/2026-10-11-spec-TOOL-aTrimmedHook-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-10-11 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aTrimmedHook-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aTrimmedHook-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
