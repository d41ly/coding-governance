---
slug: aReplayedCard
node: a
opened: 2026-09-13
streams: kickoff+tooling
roster: KICK+TOOL
ids: KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5
authorized-by: prompt
---

# aReplayedCard — session orientation, stage 1: a cited card that survives compaction

## The problem this build exists to solve

Orientation is the least-measured stage in this repo. Nothing observes compaction, hook context is
summarized when it happens, and the only enforced step-0 today is `tools/check-wiring.sh --session`,
which orients nothing and re-runs on every compaction. A kickoff reads about 69 KB into the main
context and none of it is pinned. The manifest's environment-traps section is half the manifest and
global, so every session reads bullets keyed to files it will never touch. Build the artifact, the
replay, and the commit-time deny the design record specifies, without the subagent.

## Expected improvements

- A session's orientation lives on disk and is replayed verbatim after compaction and resume.
- A commit-shaped command without a READY line is refused with the remedy in the reason.
- The two existing SessionStart entries stop running on every compaction.
- Path-bearing traps move where `gotchas.py --for-paths` selects them by area.
- A runnable harness measures the stage-2 subagent matrix before anyone builds it.

## Detriments if this is not built

- Every compaction silently drops the orientation, and the next pass rebuilds it or skips it.
- Orientation stays a request, so a session that skips it is indistinguishable from one that ran it.
- The 35–81 s wiring check keeps running at every compaction for 753 B of rows.
- Stage 2 gets built on an occupancy argument nobody has measured.

## Build-level rules

- **Stage 1 only.** No `orient` subagent, no `.claude/agents/` definition wired for use. The
  counterfactual harness ships an agent definition as a TEMPLATE the harness installs for a run and
  removes after. Owner decision 1, 2026-09-13.
- **No `--waive` verb and no waiver line.** Doc-only sessions pay a kickoff. Owner decision 2.
- **The prompt-path build-folder commit is EXEMPTED by the deny** when the cwd holds a build folder
  declaring `authorized-by: prompt`; hook logic with its own RED arm. Owner decision 3.
- **The traps eviction is inside this unit**, as `TOOL-aReplayedCard-4`. Owner decision 4.
- **The design record is `build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md`**;
  its appendix carries every load-bearing claim with a skeptic verdict. A refuted claim is not a
  design input. Three UNVERIFIED claims are settled by criteria in the specs that rest on them.
- **Classification at M2, 2026-09-13:** every unit MISSING at the run's start; all eight authored
  in the opening commit, so each is unreviewed and M4 audits the set before any code. Round 1 came
  back BLOCKED on four units; the fold is rev-2 of seven specs, and two forks it settled are
  delegated marks in `TOOL-aReplayedCard-1` §8: the deny set is `git commit` alone, and the
  exemption keys on a NEW build README, staged or untracked.
- **Every gate arm is observed RED before it lands.** No exceptions for a print-only verb.
- **The kit self-tests are held**; the DoD for the kit units owes `GATE_SELFTESTS=1` on the full
  bar because this is kit work.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aReplayedCard-4` | 1 | 22 path-bearing manifest trap bullets become `memory/gotchas/` records |
| 2 | `KICK-aReplayedCard-1` | 2 | `manifest-check.sh --card` writes and replays the session card |
| 2 | `TOOL-aReplayedCard-5` | 1 | `orient-counterfactual.js` measures one stage-2 arm per call |
| 3 | `KICK-aReplayedCard-2` | 2 | `--card --append` and `--card --check` run the batched citation check |
| 3 | `TOOL-aReplayedCard-1` | 2 | `scratch-guard.js` denies a `git commit` with no READY line |
| 5 | `KICK-aReplayedCard-3` | 2 | the engine consumes the card at Step 1 and appends at Step 5 |
| 4 | `TOOL-aReplayedCard-2` | 2 | SessionStart matchers, two card fragments, a rematching merge, a wiring arm |
| 5 | `TOOL-aReplayedCard-3` | 2 | the unattended Skill's resume section kicks off after `--resume` |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 8 unit(s) · node a · opened 2026-09-13 · streams kickoff+tooling
ids KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aReplayedCard-4 — path-bearing manifest trap bullets become `memory/gotchas/` records](spec/2026-09-13-spec-TOOL-aReplayedCard-4.md) | 1 | 1 | SPECCED | rev-1 | 2026-09-13 |
| [KICK-aReplayedCard-1 — `manifest-check.sh --card` writes and replays the session's orientation card](spec/2026-09-13-spec-KICK-aReplayedCard-1.md) | 2 | 2 | SPECCED | rev-2 | 2026-09-13 |
| [TOOL-aReplayedCard-5 — `orient-counterfactual.js` measures one stage-2 arm per call](spec/2026-09-13-spec-TOOL-aReplayedCard-5.md) | 2 | 1 | SPECCED | rev-2 | 2026-09-13 |
| [KICK-aReplayedCard-2 — `--card --append` and `--card --check` run the batched citation check](spec/2026-09-13-spec-KICK-aReplayedCard-2.md) | 3 | 2 | SPECCED | rev-2 | 2026-09-13 |
| [TOOL-aReplayedCard-1 — `scratch-guard.js` denies a `git commit` with no READY line](spec/2026-09-13-spec-TOOL-aReplayedCard-1.md) | 3 | 2 | SPECCED | rev-2 | 2026-09-13 |
| [TOOL-aReplayedCard-2 — SessionStart matchers, two card fragments, a rematching merge, a wiring arm](spec/2026-09-13-spec-TOOL-aReplayedCard-2.md) | 4 | 2 | SPECCED | rev-2 | 2026-09-13 |
| [KICK-aReplayedCard-3 — the engine consumes the card at Step 1 and appends at Step 5](spec/2026-09-13-spec-KICK-aReplayedCard-3.md) | 5 | 2 | SPECCED | rev-2 | 2026-09-13 |
| [TOOL-aReplayedCard-3 — the unattended Skill's resume section kicks off after `--resume`](spec/2026-09-13-spec-TOOL-aReplayedCard-3.md) | 5 | 2 | SPECCED | rev-2 | 2026-09-13 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aReplayedCard-4` | no |
| 2 | `KICK-aReplayedCard-1`, `TOOL-aReplayedCard-5` | yes |
| 3 | `KICK-aReplayedCard-2`, `TOOL-aReplayedCard-1` | yes |
| 4 | `TOOL-aReplayedCard-2` | no |
| 5 | `KICK-aReplayedCard-3`, `TOOL-aReplayedCard-3` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
