# TOOL-aReplayedCard-3 — the unattended Skill's resume section kicks off after `--resume`

**Status:** CLOSED · rev-6 · 2026-09-14 · node a · Tier-2 · base c4f02308 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md](../build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md) | research | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-build-KICK-aReplayedCard-1-2-closing-fold-round1.md](../build/2026-09-14-build-KICK-aReplayedCard-1-2-closing-fold-round1.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 |
| [2026-09-14-build-TOOL-aReplayedCard-3-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aReplayedCard-3-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md](../prompts/2026-09-13-prompt-KICK-aReplayedCard-1-0-run-mandate.md) | journal | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-prompt-TOOL-aReplayedCard-3-brief.md](../prompts/2026-09-14-prompt-TOOL-aReplayedCard-3-brief.md) | journal | — |
| [2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md](../reviews/2026-09-13-review-KICK-aReplayedCard-1-spec-audit-round1.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md) | diff-review | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round2.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |
| [2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md](../reviews/2026-09-14-review-KICK-aReplayedCard-1-spec-audit-round3.md) | spec-audit | KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5 |

<!-- /gen:spec-records -->

## 1. Goal

A run resumed in a new session after process death today reads its run-state file and continues,
and never re-reads the manifest, re-runs a probe, or writes a READY line — so its first commit is
now denied. Add one step to the Skill's resume section: invoke `/session-kickoff` after
`--resume`, where Step 5b fires on the live run-state file, emits the card, appends READY and
continues. The prompt path's step 1 stays where it is, and nothing above the template's first
`--preflight` mentions the kickoff.

## 2. Scope (IN)

- **S1** The `## Resume` section of `tools/unattended/SKILL.template.md` gains, after the reap and
  re-schedule paragraphs, one step: invoke `/session-kickoff`; Step 5b fires because the run-state
  file exists in a non-terminal phase, the READY card lands on the orientation card, and the run
  continues at the phase the record names. Observed by AC1 and AC2.
- **S2** The rendered `.claude/skills/unattended/SKILL.md` is re-rendered in the same commit so
  the byte-compare stays green. Observed by AC3.
- **S3** No `/session-kickoff` mention is added above the template's first `unattended.sh
  --preflight` line, which check 18 of `check-unattended.sh` anchors on by first occurrence; the
  resume section sits far below it. Observed by AC4.
- **S4** The prompt path's step 1 gains no new probe wording; check 20's five section-scoped
  literals are untouched. Observed by AC4.

## 3. Non-goals (OUT)

- No change to the driver: `--resume` writes nothing new and reads no card.
- No change to the kickoff engine's Step 5b; `KICK-aReplayedCard-3` owns the append there.
- No exemption for a resumed run's first commit; the kickoff is the remedy, and it is one kickoff.
- No change to the protocol document; the resume section is operating summary, and the protocol's
  section on resume already says the record survives where the context did not.

### Edges

- **consumes-from** `KICK-aReplayedCard-3` — Step 5b's append; without it the resumed run emits a
  READY card that never lands and stays denied.
- **consumes-from** `TOOL-aReplayedCard-1` — the deny that makes a resumed run's un-oriented
  commit visible at all.
- **consumes-from** `TOOL-aReplayedCard-2` — the wired writer; AC2 needs a fresh session's card to
  append to, which exists only once the SessionStart entries are wired.
- **hands-off** external — the kit self-test for `check-unattended.sh`, held by the 2026-08-23
  ruling; AC4 runs the check itself, not its suite.

## 4. Design

### Data model

None. One numbered step of prose.

### Inventory

No identifier minted.

### Migration

None; the rendered Skill is regenerated by the kit's render, as for every template edit.

### Rollout

Live at the commit; the next resumed run reads it.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/SKILL.template.md` | one step in `## Resume` |
| `.claude/skills/unattended/SKILL.md` | re-rendered |
| `memory/map/features/unattended.md` | refreshed on touch |

### Alternatives rejected

**A `--resume` that writes the READY line itself.** The driver would be authoring the orientation
outcome the kickoff exists to derive; and it cannot run the manifest audit.

**Exempting a resumed run in the deny.** A run that lost its context is exactly the run that
should re-orient; the design record's improvement 7.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one kickoff per resume-after-death, measured by the counterfactual harness's
  wall figure once `TOOL-aReplayedCard-5` lands; the design record lists it as a cut with a trigger.
- error / empty / loading states — a resumed run with no run-state file is already a driver
  refusal before this step is reached.
- observability — the READY line on the card names the build slug and run-state path.
- risks — check 18's first-occurrence anchor; S3 and AC4.
- testing — AC4 runs `check-unattended.sh` once, which the design record measured past 100 s.
- migration — none.
- user docs — the Skill is the document.

## 6. Acceptance criteria

- **AC1** — When `tools/unattended/SKILL.template.md` is read at the landing commit, the `## Resume`
  section names `/session-kickoff` after the paragraph on scheduling the replacement keepalive and
  before `## Close`.
  Red when: the step is added above the reap paragraph, so a resumed run orients before it reaps.
- **AC2** — When a fresh session executes the resume section in a scratch clone of this branch
  holding a throwaway run-state file in a non-terminal phase, written by `--preflight` against a
  keepalive id that session scheduled itself, the transcript shows the READY card and that clone's
  orientation card ends with a `READY —` line naming the throwaway build's slug.
  Red when: Step 5b halts at the READY stop because the run-state file was not read first.
  fixture: a scratch clone and a throwaway `RUN.md` — never this build's own, because the resume
  section's first act reaps the recorded keepalive, and reaping the live run's job from a second
  session is the failure the section exists to prevent; recorded in the ledger with the clone path.
  cost: one kickoff, one keepalive scheduled and reaped by the fixture session.
- **AC3** — When `bash tools/unattended/adopt-unattended.sh --check`, the `unattended skill
  wiring` leg, runs at the landing commit, the rendered-versus-template byte compare passes.
  Red when: the template moved and the render did not.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs at the landing commit, checks 18
  and 20 pass, and the first `/session-kickoff` occurrence in the template is still below the
  first `--preflight` occurrence.
  Red when: a kickoff mention lands above the preflight anchor.
  cost: the design record's skeptic measured the check past 100 s; budget it, do not pipe it
  through `tail`.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit/dogfood doc parity` · `codebase-map coverage + freshness` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · §3 · §6 · AC2 · folded the round-1 spec audit. AC2's fixture is a scratch
  clone with a throwaway run-state file and its own keepalive, never this build's live `RUN.md`,
  whose keepalive the resume section would reap from a second session (H9); a `consumes-from
  TOOL-aReplayedCard-2` edge and order 5, because AC2 needs a wired writer (M5).
- rev-3 · 2026-09-14 · header · order 6, because AC2 also consumes `KICK-aReplayedCard-3`'s Step 5b
  append and the two cannot share a parallel step (round-2 M2).
- rev-4 · 2026-09-14 · S1 · header · at the build pass: the step sits last in `## Resume`, after the
  paragraph on the record that cannot be corrected in place, and the schedule paragraph's ordering
  sentence gains the words `kick off` so the section states its sequence once rather than in a
  copy the new step would contradict. Status CLOSED; AC2 is owed at the first post-landing resume.
- rev-5 · 2026-09-14 · AC3 · the byte compare is `adopt-unattended.sh --check`, the `unattended skill
  wiring` leg, and not a check inside `check-unattended.sh`, which carries none; the criterion
  named the wrong observer, found at the build pass when the ledger line was written.
- rev-6 · 2026-09-14 · AC4 · "that same run" pointed at AC3's `check-unattended.sh` run, which rev-5
  moved out of AC3; AC4 now names the run itself. The bug-class checklist over the build commit
  selected `amendment-leaves-its-other-half-standing`, and this was the standing half.

## 10. Reuse audit

The seam is the Skill's own `## Resume` section at `tools/unattended/SKILL.template.md` line 661
and the engine's Step 5b hand-back, which already fires on a non-terminal run-state file and needs
no change. `python tools/codebase-map/reuse_lookup.py` run for this build returned the unattended affordance seam through
`.unattended.conf`; the section was found by reading the template. `TOOL-cBriefedPilot-11` is the
record that fixed the kickoff-after-preflight order this unit preserves.

Recall terms used: `manifest-check verb kickoff engine scratch-guard PreToolUse deny SessionStart matcher settings-merge fragment check-wiring arm session card compaction`
