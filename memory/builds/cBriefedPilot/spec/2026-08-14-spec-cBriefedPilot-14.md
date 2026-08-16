# TOOL-cBriefedPilot-14 — leg check 18, the kickoff road asserted as an order and not as a mention

**Status:** OPEN · rev-1 · 2026-08-14 · node c · Tier-1 · base 37c05e1b · streams tooling

## 1. Goal

Pin the one property FORK D actually resolved: that the Skill names `/session-kickoff` AFTER the
preflight invocation. A check that the Skill merely mentions kickoff is satisfied by the ordering
that deadlocks.

## 2. Scope (IN)

- **S1** — check 18 in `tools/unattended/check-unattended.sh`: one awk over
  `tools/unattended/SKILL.template.md` recording the line number of the kickoff mention and of the
  `--preflight` invocation, refusing unless the first is GREATER than the second.
- **S2** — keyed on a non-blank `KICKOFF_ENGINE`. Blank is silent, matching check 12, because an
  adopter may not ship the kickoff skill at all.
- **S3** — under a non-blank `KICKOFF_ENGINE`, a template that names preflight and never names
  kickoff is a refusal. Absence is not the safe side here: the deadlock and the missing step read the
  same on a count.
- **S4** — arms in `tools/unattended/check-unattended.test.sh`: conforming green, the two lines
  transposed red, kickoff absent red, blank engine silent. `ARMS_FLOORS` raised in the same commit;
  the leg header's check count and the charter's gate-suite count move with it.

## 3. Non-goals (OUT)

- **That the sequence WORKS.** This asserts the order of two lines in a document. Nobody has executed
  kickoff-after-preflight yet, and the build README carries that as a residual rather than letting
  this check imply it away.
- **The rendered Skill.** `adopt-unattended.sh --check` already pairs the render to the template and
  is its own leg; reading both here would be a second answer.
- **The kickoff engine's own text.** Check 12 owns Step 5b, the READY prompt string and the exit
  floor.
- **Writing the step.** Unit 11.

## 4. Design

Two line numbers and a comparison — the shape `region()` already uses in both this leg and the
driver, and for the identical reason recorded there: a transposed pair satisfies a count-only check,
and the driver's copy of that function truncated a file on one. Awk records the first match of each
pattern and the END block compares them, so a template naming either line twice is judged on the
first occurrence, which is the one the agent reads first.

The patterns anchor on what is stable across edits: the `--preflight` token inside the fenced command
block, and the literal `/session-kickoff`. Both are spelled once in unit 11's step D and step C
respectively, and neither is a heading, which a reword survives while gutting the body.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`.memory-tree.conf` (`ARMS_FLOORS`) · `AGENTS.md` (the gate-suite bullet's check count).

## 5. Production-readiness checklist

- security · perf / scale · a11y · i18n — N/A. One awk over one file, read-only.
- error / empty / loading states — the missing-kickoff branch is S3; the blank-engine silence is S2.
- observability — each branch names itself and prints the two line numbers it compared.
- risks — the untravelled sequence, stated in §3 and carried as a build residual.
- testing + left-shift gates — four arms in `unattended gate selftest`, each observed before its
  branch is written.
- migration / rollback — additive, and inert until unit 11 puts the kickoff line in the template.
- user docs — N/A, a gate.

## 6. Acceptance criteria

- **AC1** — When the kickoff line and the preflight invocation are transposed in the fixture's
  template, the leg reds and prints both line numbers.
- **AC2** — When the template names preflight and not kickoff under a non-blank `KICKOFF_ENGINE`,
  the leg reds.
- **AC3** — When `KICKOFF_ENGINE` is blank, check 18 prints nothing whatever the template says.
- **AC4** — The fixture's green control still exits 0 and prints nothing with check 18 live.

## 7. Gates

`unattended gate selftest` · `unattended kit gate` · `harness arms` · the full bar.

**No leg is added** — check 18 rides `unattended kit gate`. Of the four gates a new leg would trip,
`tools/gate-legs.json`, the dossier claim and the map re-render are all untouched; only the charter's
gate-suite bullet moves, for its check count.

## 8. Open questions

none — FORK D and FG-10 were both resolved in the design pass, and unit 11 records the ordering
evidence from the kickoff engine's own text.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds FG-10.

## 10. Reuse audit

- **`region()`'s two-line-numbers-and-compare** — the seam, present in this leg and in the driver
  with the order clause written out and the data-loss it prevented recorded beside it. Check 18 is
  the third instance of that shape and copies its discipline rather than its code, because it
  compares two patterns rather than a marker pair.
- **Check 12's `KICKOFF_ENGINE` gating** — the same declared-off disposition, on the same key.
- **The fixture's `mkconf`** — already emits or omits `KICKOFF_ENGINE` per arm, so the blank-engine
  case needs no new machinery.
- **`tools/unattended/SKILL.template.md`** — the fixture gains a copy of it in unit 12; this unit
  reuses that copy rather than adding a second.

Recall terms used: unattended gate leg kickoff preflight order line number awk transposed pair skill
template declared off engine blank silent fixture arm.
