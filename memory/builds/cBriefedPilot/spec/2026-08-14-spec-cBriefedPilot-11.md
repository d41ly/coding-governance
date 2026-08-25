# TOOL-cBriefedPilot-11 — the kickoff step, taken after preflight, and the README read as a roster

**Status:** CLOSED · rev-2 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-15-review-TOOL-cBriefedPilot-1-1.md](../reviews/2026-08-15-review-TOOL-cBriefedPilot-1-1.md) | spec-audit | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |
| [2026-08-16-review-TOOL-cBriefedPilot-1-2.md](../reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md) | diff-review | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |

<!-- /gen:spec-records -->

## 1. Goal

Put `/session-kickoff` on the unattended road at the only position where it works — after preflight —
and tell the agent to READ the build README rather than merely treat it as the authorization. This is
finding F2 and the second half of F3.

## 2. Scope (IN)

- **S1** — a step D in `tools/unattended/SKILL.template.md`, after the `--preflight` command block:
  *"If this project ships `/session-kickoff`, invoke it now — after preflight, never before."*
- **S2** — one sentence giving the reason, because a rule with no reason is a rule the next editor
  reorders: Step 5b of the kickoff engine fires only on a live run-state file, and preflight is what
  creates one.
- **S3** — the Skill's step 1 gains the roster sentence: the build README's authored Units table is
  the ROSTER (M2), so the README is read for its content and not only asserted as authorization.
- **S4** — conditional PROSE, keyed on the project shipping the skill. No new render key, no adopter
  surface, no composer.
- **S5** — the Skill's `--plan` blurb drops the sentence that the verb cannot see a planned unit with
  no spec. Unit 6 is what falsifies it and unit 6's §5 assigns the two carriers by name; the
  protocol's matching §7 bullet is unit 18's S6. This unit takes the Skill half because it already
  owns the Skill's roster-reading sentence, and a second unit editing this template would be the
  write-set collision S4 is scoped to avoid.

## 3. Non-goals (OUT)

- **Asserting the order.** Leg check 18 does that, in unit 14. This unit writes the two lines; the
  next one pins which comes first.
- **The roster MARKER pair.** The owner resolved P3 to require it, and it lands with `build-complete`
  in unit 7. S3 is a reading instruction, not a marker.
- **Teaching `--plan` to parse the table.** Unit 6.
- **Any edit to the kickoff engine.** `skills/session-kickoff/SKILL.md` already carries Step 5b and
  the six enumerated exits, and leg check 12 already grades them. This unit invokes that road; it
  does not pave it again.

## 4. Design

### Why after, and not before

Step 5b's own text makes the ordering non-negotiable: it fires only when *"this session is already
inside a started unattended run — its run-state file exists for this build, in a non-terminal phase,
written by that kit's own preflight"*, and it says in the next paragraph that the committed build
folder is a PRECONDITION and not the trigger. Kickoff first therefore takes the default path, halts
at the READY card, and waits for an owner who left. Preflight is the only writer of the run-state
file, so preflight first is the only order in which Step 5b is reachable at all.

### Why prose and not a declaration

`adopt-unattended.sh` renders exactly six keys — `KIT_DIR`, `MEMORY_ROOT`, `LANDER`,
`KEEPALIVE_CREATE`, `KEEPALIVE_DELETE`, `KEEPALIVE_INTERVAL` — and none of them is a kickoff key.
Adding one would put a second declaration beside `KICKOFF_ENGINE`, which `.unattended.conf` already
declares and already permits to be blank. The conditional the agent reads and the conf key the leg
reads answer the same question, so only one of them may be new, and the leg's is the one that exists.

### The residual, checked rather than assumed

Preflight stages the run-state file, so kickoff Step 1 meets a tree dirtied by the run's own
reporting. Step 1's STOP conditions are a foreign `MERGE_HEAD` or `UU`, a failed fast-forward, and a
branch violating conventions — verified against source, none of them is a dirty tree — and the
fast-forward clause runs *"only when on the default branch with a clean tree"*, which an unattended
run never is, because preflight refuses the default branch. So the sequence should pass. It is
recorded as a residual in the build README rather than claimed here, because "should" is the word
that precedes every reproduced bypass in this kit's history, and nobody has executed this order yet.

### Files touched (estimate)

`tools/unattended/SKILL.template.md` · the rendered `.claude/skills/unattended/SKILL.md`.

## 5. Production-readiness checklist

- security · perf / scale · a11y · i18n — N/A, two sentences in a document.
- error / empty / loading states — a project with no kickoff skill declares a blank
  `KICKOFF_ENGINE` and the step's condition is simply false; nothing refuses.
- observability — N/A.
- risks — the untravelled order, stated above and carried as a build-level residual.
- testing + left-shift gates — the render parity arm now; check 18's order assertion in unit 14.
- migration / rollback — the template and its render move together or the wiring check reds.
- user docs — this IS the user doc.

## 6. Acceptance criteria

- **AC1** — In the rendered Skill, the line naming `/session-kickoff` has a GREATER line number than
  the line carrying the `--preflight` invocation.
- **AC2** — The kickoff step reads as a condition on the project shipping the skill, and the render
  gains no new substitution key.
- **AC3** — The Skill's step 1 names the build README's authored Units table as the roster.
- **AC4** — `bash tools/unattended/adopt-unattended.sh --check` is green and the render carries no
  surviving brace-shaped placeholder.
- **AC5** — The rendered Skill's `--plan` blurb no longer claims the verb is blind to a planned unit
  with no spec, grepped and found zero — the observation that the Skill and unit 6's behaviour agree.

## 7. Gates

`unattended skill wiring` · `unattended adopter e2e` · `method carriers`
(`tools/unattended/SKILL.template.md` and its render are already declared carriers) · the full bar.

## 8. Open questions

none — FORK D resolved in the design pass to kickoff-after-preflight, with `KICKOFF_ENGINE`,
`KICKOFF_EXITS` and leg check 12 all left in place, and the build README records the evidence.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds C10 and D7.
- rev-2 · 2026-08-14 · S5 and AC5 added on the cross-read. Unit 6 makes the Skill's `--plan` blurb
  false and unit 6's §5 pointed the repair at unit 18, which touches this template nowhere; measured,
  `tools/unattended/SKILL.template.md:65-67` still carries the sentence. The Skill half lands here,
  the protocol half in unit 18's S6, so neither template gets two editors.

## 10. Reuse audit

- **`skills/session-kickoff/SKILL.md` Step 5b** — the seam. It was written for exactly this
  hand-back and has been unreachable from the unattended path since it landed; this unit supplies the
  invocation it was waiting for, and edits nothing in it.
- **`tools/unattended/SKILL.template.md` and `adopt-unattended.sh`** — the render seam, unchanged.
  Static text, no new key.
- **`.unattended.conf`'s `KICKOFF_ENGINE`** — already the declaration for whether this project ships
  the skill. Unit 14's check 18 keys on it; this unit's prose defers to the same fact.

Recall terms used: unattended skill kickoff step preflight order run-state hand-back READY card
roster README units table M2 session start.
