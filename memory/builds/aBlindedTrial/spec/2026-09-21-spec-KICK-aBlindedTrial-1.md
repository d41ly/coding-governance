# KICK-aBlindedTrial-1 — the kickoff engine puts the spec-audit question to the owner at READY

**Status:** INPROGRESS · rev-3 · 2026-09-21 · node a · Tier-2 · base 0e61932d · streams kickoff · order 1 · ratified 2026-09-21

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-review-TOOL-aBlindedTrial-7-8-kick1-closing-diff-round1.md](../reviews/2026-09-21-review-TOOL-aBlindedTrial-7-8-kick1-closing-diff-round1.md) | diff-review | TOOL-aBlindedTrial-7 TOOL-aBlindedTrial-8 |
| [2026-09-21-review-TOOL-aBlindedTrial-7-8-kick1-closing-diff-round2.md](../reviews/2026-09-21-review-TOOL-aBlindedTrial-7-8-kick1-closing-diff-round2.md) | diff-review | TOOL-aBlindedTrial-7 TOOL-aBlindedTrial-8 |

<!-- /gen:spec-records -->

## 1. Goal

Build READMEs are authored by the agent, so "the owner declares `spec-audit:`" needs a place where the
owner is actually asked. `/session-kickoff` already derives the tier and knows the roster at Step 3;
when the project's method makes the audit opt-in, it asks one question at READY, recommends by the
shape the trial could not measure, and writes the line on a yes.

## 2. Scope (IN)

- S1 — `skills/session-kickoff/SKILL.md` Step 3, after the risk-tier paragraph: when the DoR is a
  design pass AND the project's build method names `spec-audit:` as opt-in (`grep -q 'spec-audit:'` on
  the method carrier the manifest names, else skip), ask ONE `AskUserQuestion` — "Declare `spec-audit:`
  for this build?" — recommending yes when the roster has two or more units or a spec carries an open
  §8 fork, and no otherwise; on yes, write `spec-audit: <today>` into the build README front matter
  before the spec pass (create the README first when the DoR authors it); on no, nothing is written.
  Do NOT ask when the build README already carries `spec-audit:` (the README answered), else when
  `<repo>/.unattended.conf` declares a dated `SPEC_AUDIT_DEFAULT` (the project answered; a "no"
  could change nothing — round 1 R7, round 2 R10). Observed by AC1, AC2.
- S2 — Step 5's READY card `## open` section carries the answer, or what answered for it, as one
  line: `spec audit: declared <date>`, `spec audit: not declared (owner)` or `spec audit: project
  default <date>`, so the choice is on the card the session re-reads. Observed by AC3.
- S3 — Step 5b (the unattended hand-back) never asks: under a mandate the README at BASE decides and
  the driver's preflight line already says so. One sentence there. Observed by AC4.
- S4 — the engine stays under its 18432-byte cap (17349 today) and the installed junction still matches
  the tracked engine; `memory/map/features/session-kickoff.md` prose names the question. Observed by AC5.

## 3. Non-goals (OUT)

- No new sealed §A field: the answer lives in `## open`, and check 10 byte-compares the sealed set.
- No kit version bump: the engine carries no marker of its own, `KIT_MANIFEST_VERSION` is the manifest
  FORMAT version and bumping it makes every adopter's manifest WARN on format; recorded as
  `TOOL-aReplayedCard-17`'s shape.
- No change to `manifest-check.sh` or `MANIFEST-TEMPLATE.md`.
- No change to the project manifest `memory/guides/SESSION-KICKOFF.md`: its tier rule already says the
  audit is opt-in.

### Edges

- **consumes-from** external — the `spec-audit: <date>` key grammar (`TOOL-aBlindedTrial-2`) and M4's
  opt-in sentence (`TOOL-aBlindedTrial-5`), both landed at `0e61932d`.

## 4. Design

### Files touched (estimate)

`skills/session-kickoff/SKILL.md` · `memory/map/features/session-kickoff.md`.

### Alternatives rejected

- Asking on every kickoff: a project whose method does not make the audit opt-in has nothing to declare,
  and a Tier-1 unit has no spec pass to audit.
- Deriving the answer instead of asking: the whole point of `TOOL-aBlindedTrial-6` is that the owner
  decides; the engine may recommend, never decide.

## 5. Production-readiness checklist

- security — N/A
- perf / scale — one grep and at most one question per kickoff
- error / empty / loading states — a project without the method carrier skips silently; the engine says
  so in the step
- observability — the `## open` line on the card
- risks — the byte cap; prose has no arm, so the acceptance is greps plus the two gates
- testing — `check-template-size.sh` and `check-wiring.sh --check`
- migration — none; the engine is prose
- user docs — the engine is its own doc

## 6. Acceptance criteria

- **AC1** — When `grep -n 'spec-audit:' skills/session-kickoff/SKILL.md` runs, it names a Step 3
  paragraph carrying `AskUserQuestion`, the two-units-or-a-fork recommendation and the write-on-yes
  instruction.
  Red when: the step asks without recommending, or writes without asking.
- **AC2** — When the same grep runs, the Step 3 paragraph names the condition that gates the question
  (the project's method names `spec-audit:` as opt-in) and the skip when it does not.
  Red when: a project without the opt-in is asked.
- **AC3** — When `grep -n 'spec audit:' skills/session-kickoff/SKILL.md` runs, it names the `## open`
  line in Step 5 in all three spellings: `declared <date>`, `not declared (owner)` and
  `project default <date>` — the third written when `.unattended.conf` declares a dated
  `SPEC_AUDIT_DEFAULT` and Step 3 therefore does not ask (rev-2).
  Red when: the card carries no record of the answer, or asks under a project default.
- **AC4** — When `grep -n 'never ask' skills/session-kickoff/SKILL.md` runs, it lands inside Step 5b.
  Red when: an unattended run could put a question to nobody.
- **AC5** — When `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` prints
  `template-size OK` and `bash tools/check-wiring.sh --check` reports the installed engine matching
  tracked, both exit 0.
  Red when: the engine passes its cap or the junction drifts.

## 7. Gates

`kickoff engine size <=18KiB` · `kickoff-manifest ratchet` · `memory hygiene` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

## 8. Open questions

- **F1 — ask on every design pass, or only when the shape recommends yes.** RESOLVED (agent,
  2026-09-21, delegated): ask on every design pass where the audit is opt-in, with the recommendation
  varying. An owner who wants the audit on a one-unit build should not have to know the key exists.

## 9. Revision log

- rev-1 · 2026-09-21 · initial draft from the engine at 0e61932d.
- rev-2 · 2026-09-21 · §6 · §7 · closing diff review round 1 folded. R7: Step 3 does not ask when the
  conf declares a dated `SPEC_AUDIT_DEFAULT` — a "no" there could change nothing and the card misrecorded
  it — and Step 5 gains the third `## open` spelling, which AC3 now names. R6: the leg line names every
  leg the §4 files-touched trips under the guards join at the fold — the three `skills/session-kickoff/`
  legs and the two `memory/` recall legs.
- rev-3 · 2026-09-21 · S1 · S2 · closing diff review round 2 folded. R11: the scope items now
  describe what rev-2 built — S1 carries the no-ask clause and S2 the third `## open` spelling AC3
  names; the rev-2 line listed §6 and §7 only. R10: the no-ask clause takes README precedence, the
  driver's own order — a README `spec-audit:` is carded `declared <date>`, and the conf default is
  consulted and carded `project default <date>` only when the README carries no key.

## 10. Reuse audit

Probe: `tools/codebase-map/reuse_lookup.py "ask the owner one question at kickoff and write the answer
into the build README"` returned no candidate — the engine is prose and the probe scans no `.md`. The
seam is Step 3's existing `AskUserQuestion` convention ("ONLY for a field you genuinely cannot derive")
and Step 5's `## open` section; the unit adds one question and one line to each. Recall terms used:
kickoff engine READY card AskUserQuestion design pass tier spec-audit opt-in open section unattended
hand-back byte cap.
