# TOOL-aHomedAnchor-4 — the pre-commit hook runs the Skill wiring check when its inputs are staged

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-1 · base 40a976d9 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aHomedAnchor-1-runlog-5ac5d61b.md](../build/2026-10-09-build-TOOL-aHomedAnchor-1-runlog-5ac5d61b.md) | journal | TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 |
| [2026-10-09-build-TOOL-aHomedAnchor-4-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aHomedAnchor-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aHomedAnchor-1-1-reconstructed-build-briefs.md](../prompts/2026-10-09-prompt-TOOL-aHomedAnchor-1-1-reconstructed-build-briefs.md) | journal | TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 |

<!-- /gen:spec-records -->

## 1. Goal

Close the closing review's HIGH id 17 by left-shifting H1: a hand-edited rendered Skill, or a conf
or template change with no re-render, reds at commit time rather than only at the bar.

## 2. Scope (IN)

- S1. `.githooks/pre-commit` gains a staged leg: when `.unattended.conf`, any staged path ending in
  `SKILL.template.md`, or `.claude/skills/unattended/SKILL.md` is staged, it resolves the
  unattended kit's `adopt-unattended.sh` through the hook's existing kit-root ladder and runs it with
  `--check`. A miss is the hook's announced skip. Observed by AC1 and AC2.
- S2. `.githooks/pre-commit.test.sh` gains the arms. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

The bar's own wiring leg is unchanged; this is an early signal, as the hook's other staged legs are.

### Edges

- **consumes-from** `TOOL-aHomedAnchor-3` — a Skill in sync, or this unit's own commit reds

## 4. Design

The template-size leg is the shape: a staged-path test, `resolve_kit_gate`, `print_kit_miss`.

### Files touched (estimate)

- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`

## 5. Production-readiness checklist

- perf / scale — the check renders one Skill; it runs only when its inputs are staged.
- testing — AC1, AC2.

## 6. Acceptance criteria

- **AC1** — When a fixture repo stages `.unattended.conf` with a stand-in `adopt-unattended.sh` at the
  kit root, the commit's output names the stand-in run with `--check`.
  Red when: the leg is absent or never resolves the kit.
- **AC2** — When the fixture stages only an unrelated file, the commit output carries no `--check`
  line from the stand-in.
  Red when: the leg runs on every commit.

## 7. Gates

`branch-guard self-test`

New arm: .githooks/pre-commit.test.sh · covers AC1 AC2 · a stand-in adopter staged-for and not · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from `memory/builds/aHomedAnchor/reviews/2026-10-09-review-TOOL-aHomedAnchor-1-implementation-diff-round1.md` HIGH id 17.

## 10. Reuse audit

The seam is the hook's template-size staged leg and its `resolve_kit_gate` ladder in
`.githooks/pre-commit`. Recall terms used: `--terms "pre-commit staged leg resolve_kit_gate
print_kit_miss template size kit root ladder adopt-unattended check"`.
