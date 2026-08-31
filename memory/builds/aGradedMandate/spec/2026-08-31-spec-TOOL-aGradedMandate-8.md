# TOOL-aGradedMandate-8 — the agent-facing carriers corrected, in one render

**Status:** CLOSED · rev-3 · 2026-08-31 · node a · Tier-1 · base 396cd9db · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-acceptance-ledger.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-acceptance-ledger.md) | journal | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 |
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-9 |
| [2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round1.md) | diff-review | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 |
| [2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round2.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round2.md) | diff-review | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-5 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-9 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-9 |

<!-- /gen:spec-records -->

## 1. Goal

Four statements an unattended agent reads are wrong or missing in a way that changes what the agent
DOES. They are collected into one edit of the Skill template and one adopter render, so the
divergence is repaired once rather than four times.

## 2. Scope (IN)

- **S1** — The Skill says "One item has NO override" and names `authorization-reachable`. The driver
  holds two: `DOD_NO_OVERRIDE="authorization-reachable pieces-complete"`. Name both, and add the
  `--abort` route to the paragraph that offers `--override`.
- **S2** — The Skill's forbidden dispositions for a promoted blocker read "Not parked, not waived,
  and not re-reviewed", which is exhaustive in tone and omits the cheapest exit. Add "not retired".
- **S3** — The Skill's "While it runs" walks nine verbs and never names the one per-pass quality act
  on CODE: `python tools/memory-tree/gotchas.py --for-diff <range>`, which M6 mandates per pass and
  M8 re-mandates over the full range on every closing round. Neither kit carrier mentions it. Name
  it, with the committed-range caveat that makes the pre-commit spelling read as a clean checklist.
- **S4** — All six documented `--record-piece` / `--record-set` invocations spell `--verdict PASS`,
  and `FAIL` appears in no example. Make one example spell `FAIL`, so the instruction layer stops
  priming the answer on the item that takes no override.
- **S6** — Name the retirement split `TOOL-aGradedMandate-5` adds in the Skill's `--rescope`
  paragraph, so a run learns from the file it actually reads that a retirement now reaches the
  owner's one turn. The self-test-escalation half of this item was deleted in the round-1 fold, with
  `TOOL-aGradedMandate-3`.

*S5 was DELETED in the round-1 fold. It claimed the protocol §2 fact-3 correction that
`TOOL-aGradedMandate-5` S5 also claimed; one edit now has one owner, and this unit touches
`PROTOCOL.template.md` not at all.*

## 3. Non-goals (OUT)

- **No edit to a carrier outside this kit.** The charter, the build method and `memory/HYGIENE.md`
  are M3 veto 2 and are out of the prompt's stated scope, which is "any layer of the kit".
- **No new rule.** Every sentence here either states what the code already does or points at a
  section that owns a rule. A gloss that grew into a condition would be the defect the pointer design
  exists to avoid.
- **No render of the DoD set into the Skill.** Enumerating the core Definition-of-Done set in an
  agent-facing carrier creates a fourth copy of a set that already has three; only the
  non-overridable pair is named, because that is the pair the agent has to act on at close.

## 4. Design

The edits land in `tools/unattended/SKILL.template.md` and `tools/unattended/PROTOCOL.template.md`,
and the renders `.claude/skills/unattended/SKILL.md` and `memory/guides/UNATTENDED-PROTOCOL.md` are
produced by `bash tools/unattended/adopt-unattended.sh` rather than hand-edited, because the wiring
leg byte-compares the pair and a hand edit is how the two stop agreeing.

### Files touched (estimate)

| File | Why |
|---|---|
| `tools/unattended/SKILL.template.md` | S1, S2, S3, S4, S6 |
| `.claude/skills/unattended/SKILL.md` | render |

### Alternatives rejected

Hand-editing the renders. Rejected by the wiring leg's own existence.

## 5. Production-readiness checklist

- security — N/A. Prose.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the render is verified by the existing wiring leg rather than by eye.
- risks — **the rendered Skill has NO size ceiling anywhere in this tree.**
  `tools/template-size-limits.txt` declares three subjects and this is not one of them, no leg caps a
  skill other than the kickoff engine, and `check-unattended.sh` performs no byte measurement at all.
  So the additions land with nothing measuring the result. Stated rather than mitigated: adding a
  measured row to another kit's declared limits table is a pin this unit did not price.
- testing + left-shift gates — the machine half is `TOOL-aGradedMandate-9`, which makes the S1 class
  of divergence red rather than ship. S2 to S6 have no machine half and that is stated here.
- migration / rollback — reverting the template and re-rendering.
- user docs — this unit IS the user docs.

## 6. Acceptance criteria

- **AC1** — `grep -c "pieces-complete" .claude/skills/unattended/SKILL.md` is at least 1, and the
  paragraph naming the non-overridable set names both members and the `--abort` route.
- **AC2** — `grep -c "not retired" .claude/skills/unattended/SKILL.md` is at least 1.
- **AC3** — `grep -c "gotchas.py" .claude/skills/unattended/SKILL.md` is at least 1.
- **AC4** — `grep -c -- "--verdict FAIL" .claude/skills/unattended/SKILL.md` is at least 1.
- **AC5** — `bash tools/check-wiring.sh --check` reports the installed Skill matching the tracked
  render.
- **AC6** — The rendered Skill still passes the SHAPE checks the kit's leg applies to it, verified by
  `bash tools/unattended/check-unattended.sh`. There is no size half, for the reason section 5 gives.
- **AC7** — The `--rescope` paragraph of `.claude/skills/unattended/SKILL.md` names the owner's
  turn: `grep -c "owner's one turn" .claude/skills/unattended/SKILL.md` is at least 1. **Measured
  before the edit: 0.** The obvious spelling was rejected because it is not falsifiable —
  `grep -c 'retire'` on the unedited render returns 2, and one of those hits
  (`--act retire|supersede|add`) sits INSIDE the `--rescope` bullet, so the paragraph qualifier does
  not rescue it. A grep-shaped criterion whose pre-edit count nobody measured is an assertion about
  nothing.

## 7. Gates

`unattended skill wiring` · `unattended kit gate` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored from findings F10, F6 and F7 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`.
- rev-3 · 2026-08-31 · round-2 fold of R5 and R11: AC7 is re-anchored on bytes S6 must INTRODUCE,
  with the pre-edit measurement written down, because `grep -c 'retire'` was already 2 inside the
  very paragraph the criterion scoped itself to; and this header, which read rev-1 over a rev-2 log
  that hygiene's rev arm cannot see because it fires only on a header AHEAD of its log.
- rev-2 · 2026-08-31 · round-1 fold. S5 deleted (F17: one edit, two owners), the escalation half of
  S6 deleted with `TOOL-aGradedMandate-3`, the section 5 size-ceiling claim corrected (F12: the
  mitigation did not exist), AC6 narrowed to the shape half it can actually observe, AC7 added for S6
  (F18), and the prose count in section 3 replaced (F19).

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is `tools/unattended/adopt-unattended.sh`, the kit's own renderer, and the existing
convention that the two `*.template.md` files are the sources and the two renders are outputs. No new
mechanism: the directive table in the Skill is already rendered and already joined to the driver in
both directions by the leg, and this unit adds prose to files that pipeline already carries.
