# TOOL-aUnblockedFleet-3 — the protocol and the Skill state the rule the code now runs

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-1 · base 117de044 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Two carriers state the at-most-one-live-run rule as binding. Units 1 and 2 remove it from the code.
A contract that outlives its enforcement is worse than either — it tells the next agent to expect a
refusal that no longer exists, and `TOOL-dClosedLexicon-11`'s review already recorded one agent
building to exactly that kind of phantom.

## 2. Scope (IN)

- **S1** — `tools/unattended/PROTOCOL.template.md` §3: the paragraph beginning "**At most one
  run-state file in the tree may be in a non-terminal phase.**" is replaced by the rule that
  actually binds — concurrent runs are permitted and announced, a build folder holds one live
  record, and an archived record must be terminal (leg check 4, which is what still enforces it).
- **S2** — the replacement states WHY the old rule went, in one sentence naming the measurement, so
  the next reader does not re-derive it or re-add the refusal.
- **S3** — `tools/unattended/SKILL.template.md`: the `--preflight` refusal list drops "and when a
  second run is already live". Every other refusal in that sentence stays.
- **S4** — BOTH renders are regenerated in the same commit as their templates, and the rendered
  copies are `memory/guides/UNATTENDED-PROTOCOL.md` and `.claude/skills/unattended/SKILL.md`. Leg
  check 10 byte-compares the shipped protocol against the installed one, so a template edited without
  a re-render reds — which is the gate that makes this unit's failure mode loud rather than silent.
- **S5** — the kit version bumps in `tools/unattended/unattended.sh` and
  `tools/unattended/check-unattended.sh` (both, paired by `check-kit-versions.sh`) and the
  `gov:kit unattended@<v>` stamp in the rendered Skill follows from the re-render.

## 3. Non-goals (OUT)

- The repository's own `AGENTS.md` / charter template. Neither states this rule; both point at
  `memory/guides/UNATTENDED-PROTOCOL.md` rather than restating it, which is the design working.
  Verified by grep at writing time.
- Any other section of the protocol. §3's neighbouring paragraphs about terminal phases, `--phase`,
  and `LANDING` being close-only are correct and untouched.
- Rewriting the protocol's Definition-of-Done table, the phase vocabulary, or the anchor sections.

## 4. Design

The change is text in two templates plus their renders. The mechanism that makes it safe is already
built: leg check 10 fails when the shipped template and the installed render disagree, and leg check
16 asserts the installed protocol still spells the archive filename grammar. Both run on the bar.

The one judgement is what the replacement paragraph SAYS. It must not read as "the rule was
relaxed", because the rule was not relaxed — it was found to have no referent. The replacement
states three facts that are all still true and all still enforced somewhere: concurrent runs are
permitted, every verb is slug-addressed so no reader ever has to resolve "the run", and a build
folder holds at most one live record because there is one `RUN.md` and check 4 refuses a
non-terminal archived one.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/PROTOCOL.template.md` | §3's singularity paragraph replaced |
| `memory/guides/UNATTENDED-PROTOCOL.md` | the render of the above |
| `tools/unattended/SKILL.template.md` | one clause dropped from the `--preflight` refusal list |
| `.claude/skills/unattended/SKILL.md` | the render of the above |
| `tools/unattended/unattended.sh` | `KIT_UNATTENDED_VERSION` bump |
| `tools/unattended/check-unattended.sh` | the paired `KIT_UNATTENDED_VERSION` bump |

## 5. Production-readiness checklist

- security — N/A, documentation of a non-security control.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — N/A, static documents.
- observability — leg checks 10 and 16 are the observability; an unrendered template reds.
- risks — `two-answers-to-one-question`, which is the class this unit exists to avoid: the code
  saying one thing and the contract another. Mitigated by landing this unit in the same commit range
  as units 1 and 2 and by check 10.
- testing + left-shift gates — no new arm. Check 10's parity gate already covers the failure mode and
  a second arm asserting prose content would be a second answer to one question.
- migration / rollback — revert.
- user docs — this unit IS the user docs.

## 6. Acceptance criteria

- **AC1** — When `grep -n "At most one run-state file" tools/unattended/PROTOCOL.template.md
  memory/guides/UNATTENDED-PROTOCOL.md` runs, it returns nothing.
- **AC2** — When `grep -n "a second run is already live" tools/unattended/SKILL.template.md
  .claude/skills/unattended/SKILL.md` runs, it returns nothing.
- **AC3** — When `bash tools/unattended/check-unattended.sh` runs, check 10 is silent, proving the
  shipped template and the installed render agree after the edit.
- **AC4** — When `bash tools/check-kit-versions.sh` runs, the two `KIT_UNATTENDED_VERSION`
  declarations still pair, and `bash tools/check-wiring.sh --check` reports the installed Skill
  matches tracked.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `unattended kit gate`, `unattended skill wiring` and the
kit-version pairing leg binding.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-31 · authored under the aUnblockedFleet mandate.

## 10. Reuse audit

No seam to find — the unit edits two prose templates and re-runs an existing renderer
(`tools/unattended/adopt-unattended.sh`). The render path, the parity gate and the version pairing
are all existing machinery this unit uses rather than extends.

Recall terms are unit 1's; the record that binds this unit specifically is
`TOOL-dClosedLexicon-11`'s review finding, which recorded an agent building to a refusal that did not
exist. That is the failure mode S1 and S3 prevent in the opposite direction.

**Verified at writing time**: both carriers hold the sentences S1 and S3 name, and neither `AGENTS.md`
nor `coding-governance-agents.template.md` restates the rule — both point at the protocol instead.
