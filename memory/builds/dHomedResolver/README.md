---
slug: dHomedResolver
node: d
opened: 2026-10-09
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dHomedResolver-1 TOOL-dHomedResolver-2 TOOL-dHomedResolver-3
---

# dHomedResolver — a rotation is graded against its declared home, and a half-staged one is refused

## The problem this build exists to solve

Rotating inCMS core's decision index exposed two gov defects. Hygiene check 10 finds a stem's live
index by BASENAME anywhere under the memory root. Two build-folder files named `DECISIONS.md` made
the stem resolve to three indexes, and core had to rename them to land its rotation. The finding
blamed the rotation for a name collision it did not cause. Separately, `gen_build_index.py --write`
derives `ids:` from `git ls-files`. Run while the new archive was untracked, it silently rewrote 17
unrelated build READMEs and `LIVE.md`. The prompt is in `prompts/`.

## Expected improvements

- Check 10 resolves a stem at its declared home, so a namesake file elsewhere cannot red a rotation.
- Check 24's Python reader resolves the same home, joined to the shell by the cross-reader arm.
- `--write` and `--check` refuse while an archive is untracked, and name the remedy.

## Detriments if this is not built

- Every adopter with a build file named `DECISIONS.md` or `<FAMILY>.md` reds its next rotation.
- A half-staged rotation keeps rewriting unrelated build READMEs with no line saying why.

## Build-level rules

- The solution is the owner's: declared-home resolution, and a refusal over an announcement.
- Keep every property check 10's header names: TOOL-cSpliceWarden-2's same-day disambiguator and
  preamble window, and TOOL-cTracedPromise-6's shards under `backlog/`. A missing home is a named
  finding, never a `continue`.
- Every new arm is observed RED against BASE before its fix lands, and every new predicate is run
  over gov, inCMS core and nc first. Core and nc are read, never written.
- No self-test suite and no bar inside a pass. The flagged bar runs once, at the close.
- Classified at kickoff (M2): all three MISSING; authored and built inline, in roster order.
  Units 1 and 2 share the hygiene suite's fixture conventions, so they are sequenced.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dHomedResolver-1` | 2 | check 10 and check 24 resolve a rotated archive's live index at the stem's declared home |
| 2 | `TOOL-dHomedResolver-2` | 2 | the build-index generator refuses while a file under the archive folder is untracked |
| 3 | `TOOL-dHomedResolver-3` | 1 | two gotcha records for the classes units 1 and 2 close |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node d · opened 2026-10-09 · streams tooling
ids TOOL-dHomedResolver-1 TOOL-dHomedResolver-2 TOOL-dHomedResolver-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dHomedResolver-1 — check 10 and check 24 resolve a rotated archive's live index at the stem's declared home](spec/2026-10-09-spec-TOOL-dHomedResolver-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-dHomedResolver-2 — the build-index generator refuses while a file under the archive folder is untracked](spec/2026-10-09-spec-TOOL-dHomedResolver-2.md) | 2 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-dHomedResolver-3 — two gotcha records for the classes units 1 and 2 close](spec/2026-10-09-spec-TOOL-dHomedResolver-3.md) | 3 | 1 | CLOSED | rev-1 | 2026-10-09 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dHomedResolver-1 TOOL-dHomedResolver-2 TOOL-dHomedResolver-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dHomedResolver-1` | no |
| 2 | `TOOL-dHomedResolver-2` | no |
| 3 | `TOOL-dHomedResolver-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
