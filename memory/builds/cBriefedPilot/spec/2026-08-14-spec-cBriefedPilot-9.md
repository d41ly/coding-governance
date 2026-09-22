# TOOL-cBriefedPilot-9 — the Skill's directive table, and a step 0 that is no longer a suggestion

**Status:** CLOSED · rev-4 · 2026-08-16 · node c · Tier-1 · base 37c05e1b · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-15-review-TOOL-cBriefedPilot-1-1.md](../reviews/2026-08-15-review-TOOL-cBriefedPilot-1-1.md) | spec-audit | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |
| [2026-08-16-review-TOOL-cBriefedPilot-1-2.md](../reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md) | diff-review | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-18 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |

<!-- /gen:spec-records -->

## 1. Goal

Put the eleven directives in front of the agent at the one moment it will read them, and make the
build-method read that the whole instruction layer hangs on into an unconditional step. This is
finding F1: today the only link between the Skill and any work instruction is one soft conditional.

## 2. Scope (IN)

- **S1** — step 0 of `tools/unattended/SKILL.template.md` becomes unconditional: read
  `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md` WHOLE, before anything else. The "if this project ships
  one" hedge is deleted.
- **S2** — a directive table in the rendered Skill with four columns: handle, what it names, the
  carrier section, and the owner directive it came from. Eleven rows.
- **S3** — the table's gloss column NAMES rather than STATES. A cell reads "the parallelism default
  under a mandate", never M6's three conditions.
- **S4** — `reuse-first` carries a "recommend against waiving" marker in its row, and a sentence
  REQUIRING that a waived run's spec §10 name the waiver, so a skipped reuse audit is legible in the
  record instead of silent. Both are settled: the owner resolved P4 on 2026-08-14.
- **S5** — the `land-once-done` row names the close-time consequence: waiving it still owes
  `--override build-complete --reason`.
- **S6** — the Skill's Close section states that `--override <item> --reason <text>` REPEATS, one
  pair per unmet item. `tools/unattended/SKILL.template.md:92` spells one pair and says nothing about
  a second; unit 1 §3 defers the sentence to this cluster by name, and units 7 and 8 add the two DoD
  items that make two pairs the ordinary case. Without it the unattended agent — which reads only the
  Skill — writes one pair and meets unit 1's missing-reason refusal with nobody present.

## 3. Non-goals (OUT)

- **The waiver turn itself.** Unit 10 builds the AskUserQuestion step; this unit builds the table it
  reads from.
- **The driver-side refusal on an absent carrier.** That is unit 4. The Skill instructing the read
  and the driver refusing without it are two mechanisms.
- **The join that proves the table matches the registry.** Leg check 16, unit 12.
- **Any restatement of a build-method rule.** S3 is the whole discipline. A gloss that grows into a
  rule is the M1 defect this build exists to avoid, and three cells in the pre-fold design already
  did it.

## 4. Design

### Why the table lives in the Skill and not in the driver

The Skill is read once, at the moment the run starts, by an agent that has not yet done anything.
That is exactly when a directive list is worth its bytes. The driver's alternative — printing the
list at preflight or at `--resume` — was cut in the design pass: at preflight the agent has just read
this table, and at `--resume` a compacted agent cannot decode `sub-specced:M2` any better than it
could decode nothing.

### Why the gloss column is authorial and not gated

Leg check 16 pins the `(handle, carrier)` PAIRS in both directions, and `check-method-carriers.sh`
already catches a copied section heading. Neither can see a gloss growing from a name into a
restatement. A byte cap was considered and refused, because a budget permits a compressed rule. The
only control is the review lens, and the build README records that as a residual risk rather than
implying it away.

### Files touched (estimate)

`tools/unattended/SKILL.template.md` · the rendered `.claude/skills/unattended/SKILL.md` via
`adopt-unattended.sh` · `tools/unattended/adopt-unattended.test.sh` if the render arm needs the new
rows.

### Alternatives rejected

Rendering the registry INTO the Skill at adopt time from the driver constant, rather than
hand-authoring the table. Rejected: it makes the gloss column unwritable, and it converts a
second-opinion join (a shell constant against a markdown table in a different file) into a
generator-and-its-output pair, which no longer checks anything.

## 5. Production-readiness checklist

- security — N/A, documentation.
- perf / scale — the Skill grows by roughly a screen; it is read once per run and is not on the
  charter read path.
- a11y · i18n — N/A.
- error / empty / loading states — a surviving `{{`-shaped placeholder in the render is already its
  own arm in `adopt-unattended.sh --check`.
- observability — N/A.
- risks — gloss drift, stated above and carried as a residual risk.
- testing + left-shift gates — the render parity arm; leg check 16 in unit 12.
- migration / rollback — the template and its render move together or the wiring check reds.
- user docs — this IS the user doc.

## 6. Acceptance criteria

- **AC1** — When the Skill is rendered, `bash tools/unattended/adopt-unattended.sh --check` is green
  and the render carries no surviving brace-shaped placeholder.
- **AC2** — The rendered Skill's step 0 contains no conditional clause about whether the project
  ships a build method.
- **AC3** — The table carries exactly eleven rows, and every handle in it appears in the registry
  unit 2 declares.
- **AC4** — No gloss cell contains a numbered condition, a threshold, or a procedure.
- **AC5** — The rendered Skill's Close section states that the `--override` pair repeats once per
  unmet item, and the two-item example it gives spells two `--reason` values.

## 7. Gates

`unattended skill wiring` (`bash tools/unattended/adopt-unattended.sh --check`) ·
`unattended adopter e2e` · `method carriers` (`tools/memory-tree/check-method-carriers.sh`) ·
the full bar.

## 8. Open questions

### P4 — RESOLVED (owner, 2026-08-14): yes, the naming is required

S4's second clause is unconditional. The reasoning is kept below because it is what changed the answer.

**P4 — does a waived `reuse-first` have to say so in §10?** The refusal option is off the table: it
rested on the claim that this waiver reds the bar, and that was measured false (hygiene check 12
exits at `if (hdr ~ /Tier-1/) next`, and an `N/A` body passes the Tier-2 test). The live question is
narrower. S4's second clause requires a waived run's §10 to name the waiver; without it the waiver is
invisible in a green tree. Recommendation: keep it — one sentence in this table, and it converts a
silent skip into a legible one. Resolver: owner.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds C10, C14, D5, D11 and D13.
- rev-2 · 2026-08-14 · S4 gains its second clause and §8's P4 fork is rewritten. The waiver of
  `reuse-first` was measured SILENT rather than loud — it leaves the bar green over a build that
  skipped the reuse probes — so the table's job changes from warning about a failure to making an
  invisible skip legible.
- rev-3 · 2026-08-14 · the owner resolved P4: the naming is REQUIRED, so S4's second clause is no
  longer conditional and §8 records the decision rather than the question.
- rev-4 · 2026-08-14 · S6 and AC5 added on the cross-read. Unit 1 §3 defers "telling the agent that
  the pair repeats" to units 9 through 11 and none of the three claimed it; measured, no spec in the
  set contains the word. Units 7 and 8 make two `--override` pairs the ordinary close, so the
  sentence had to land somewhere, and this is the unit that already owns the template's structure.

## 10. Reuse audit

- **`tools/unattended/SKILL.template.md` and `adopt-unattended.sh`** — the render seam. The table is
  static text in the template; no new substitution key is added, so the renderer needs no change.
- **`check-method-carriers.sh`'s registry** — the Skill template and its render are already declared
  carriers, so the copy test already covers the new section. `memory/project/method-carriers.txt`
  needs a row only for files this build newly makes carriers.
- **The `{{`-placeholder arm in `adopt-unattended.sh --check`** — already distinguishes template
  parity from placeholder completeness, which is the failure mode a new table section would hit.

Recall terms used: unattended skill render template placeholder directive table build method step
carrier gloss adopter parity wiring check.
