---
slug: aBriskPreflight
node: a
opened: 2026-10-11
streams: tooling
status: INPROGRESS
roster: TOOL
ids: TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7
authorized-by: prompt
---

# aBriskPreflight — the unattended preflight finishes in seconds, and its cost is a verdict

## The problem this build exists to solve

On node `a`, 2026-10-11, one `unattended.sh --preflight` took 18.7 minutes and another 26, and a
preflight that had passed every content check was then refused at its last step because the claim
push outlived its 60 s bound. About a third of that is `check-wiring.sh --check`, which spawns a
process per item where one call per arm would do. The rest is preflight's own steps. The owner's
prose is the mandate, recorded under [prompts/](prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md).

## Expected improvements

- A whole preflight on node `a` takes at most 60 s.
- `check-wiring.sh --check` spawns one process per arm, not one per item.
- The claim push no longer outlives its bound, so a passed preflight is not lost at its last step.
- A slow preflight or wiring check says so by name instead of waiting silently on 3600 s.

## Detriments if this is not built

- Every unattended run keeps paying 18 to 26 minutes before its first unit.
- A preflight refused at check 109 keeps costing another full run to retry.
- Each new arm or record keeps adding minutes that nobody sees until a run stalls.

## Build-level rules

- **Classification (M2)**: seven units, MISSING at open, one mechanism each. Authored by this run,
  so unreviewed. The spec audit is the owner's opt-in and this build is not opted in.
- **No check is weakened.** Every refusal and every `UNWIRED` line a touched arm prints today it
  still prints, observed RED on a staged break and GREEN once restored, through a sliced arm.
- **Spawns are cut; no timeout or ceiling is raised** to make a slow step pass.
- **Measured with one instrument**, before and after, A/B interleaved on one host state. The
  instruments and their result rows are committed under `build/`.
- No pass runs the merge bar or a self-test suite. The bar runs once, at the close.
- aOrientedCast owns `tools/roles/`, `tools/hooks/scratch-guard.js`, `tools/hooks/agent-cap.js`,
  the unattended and review harness scripts, `skills/session-kickoff/`, the charter template and
  `tools/govkit/registry.toml`; this build edits none of them. Its one late arm in
  `tools/check-wiring.sh` is reconciled additively by whoever lands second.
- aSparedSpawn-8 plans the driver's fork-free readers and a fork-count arm; this build converts
  none of those readers and adds no fork-count arm.
- One kit-version bump per touched kit, after that kit's last move.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aBriskPreflight-1` | check-wiring: each arm's per-item loop becomes one batched call, the merge-rows family harvest and the eol attribute read |
| 2 | `TOOL-aBriskPreflight-2` | check-wiring: the settings file and each fragment are read once per run, and python is resolved once |
| 3 | `TOOL-aBriskPreflight-3` | preflight's wiring scope: the arms preflight needs, decided by measurement, every candidate recorded |
| 4 | `TOOL-aBriskPreflight-4` | preflight starts its bounded probes together and collects each at its own check |
| 5 | `TOOL-aBriskPreflight-5` | preflight derives the phase only of the run records its checks read |
| 6 | `TOOL-aBriskPreflight-6` | the pre-push hook leaves before its per-ref prelude when a push carries no branch |
| 7 | `TOOL-aBriskPreflight-7` | preflight and the wiring check each declare a wall-clock ceiling and name a breach |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 0 unit(s) · node a · opened 2026-10-11 · streams tooling
ids TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 9 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
