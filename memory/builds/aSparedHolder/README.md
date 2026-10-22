---
slug: aSparedHolder
node: a
opened: 2026-10-11
streams: tooling
roster: TOOL
ids: TOOL-aSparedHolder-1
---

# aSparedHolder — the resume tick spares a live session, and a resumed one waits for its work

## The problem this build exists to solve

On 2026-10-10 the resume tick killed and relaunched run aFrugalTurnstile seven times in fourteen
hours. The first kill took the owner's live interactive session, which was waiting on a Workflow
whose agent had sat in one Bash call for two hours. Each relaunch was `claude -p`, which stops a
background Workflow ten minutes after its last turn, so the run went quiet and read STALE again.
Nine idle-wake jobs piled up across the resumes, and none of them ever delivered a prompt. The
owner's prose is the mandate, recorded under [prompts/](prompts/2026-10-11-prompt-TOOL-aSparedHolder-1-build-brief.md).

## Expected improvements

- The tick never kills a live session it did not launch; it reports it to the health log.
- A resumed session keeps its background Workflows and agents through a turn end.
- A resumed session deletes the idle-wakes it inherited before it schedules its own.
- The protocol states the idle-wake's silence as measured, not owner-reported.

## Detriments if this is not built

- A session waiting on long background work is killed by the actor meant to rescue it.
- Every resume loses its background work at the first turn end, so the kill loop repeats until the
  attempt cap.
- Each resume leaks one more recurring job into the session's scheduler.

## Build-level rules

- **Classification**: one Tier-1 unit, MISSING at open, three defects in one actor.
- Out of scope: the aFrugalTurnstile build, which is closing in its own session.
- The protocol template stays byte-identical to its render and inside its size row without moving
  the ceiling, which only the owner moves.
- One unattended kit-version bump, after the last code move.

## Parked decisions

- **The unattended self-tests are owed** (owner, 2026-10-11: not run this session). The pooled run refused: no pooled
  calibration reading on node a for the 8 driver selftest shards. Run `--selftests --pooled` after
  calibrating, or `--selftests --serial --attribute 69e0ff0f`, from the merged tree.
- **Landed with no bar** (owner, 2026-10-11): `git push --no-verify` from local main at 75a1a52e, after the
  attended lander was stopped mid-bar. Gates observed instead are in the spec and this session.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aSparedHolder-1` | the tick kills only what it launched, and the resumed `-p` waits for background work |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node a · opened 2026-10-11 · streams tooling
ids TOOL-aSparedHolder-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aSparedHolder-1 — the resume tick kills only what it launched, and a resumed session waits for its background work](spec/2026-10-11-spec-TOOL-aSparedHolder-1.md) | 1 | 1 | CLOSED | rev-1 | 2026-10-11 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aSparedHolder-1.

Ids whose spec moved past its audited revision: none — 0 of 1 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aSparedHolder-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
