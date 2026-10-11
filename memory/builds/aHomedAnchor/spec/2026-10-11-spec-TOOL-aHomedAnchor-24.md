# TOOL-aHomedAnchor-24 — the `--overlaps` verb is named on both surfaces an agent reads

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 6 · closes TOOL-aHomedAnchor-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md](../prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md) | journal | TOOL-aHomedAnchor-22 TOOL-aHomedAnchor-23 TOOL-aHomedAnchor-25 |

<!-- /gen:spec-records -->

## 1. Goal

Gate shard 1/8 is red: `--overlaps`, which `KICK-aMendedFleet-2` added for the orientation card, is dispatched but absent from the Skill and from `VERBS_INLINE`, the declaration the refusal text renders.

## 2. Scope (IN)

- S1. `VERBS_INLINE` in `tools/unattended/unattended.sh` carries `--overlaps`. Observed by AC1.
- S2. `tools/unattended/SKILL.template.md` names `unattended.sh --overlaps`, the rendered Skill is re-rendered, and two sentences outside the gated blocks are shortened to keep it at or under 10240 bytes. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

Any other suite's red; running the unattended shard suites (owner, 2026-10-11).

### Edges

none

## 4. Design

The brief is `memory/builds/aHomedAnchor/prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md`. The red was read from the daily held job's run 38045767386 at `d006cfc5`.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`

## 6. Acceptance criteria

- **AC1** — When the arm's three surface greps run for `--overlaps`, each finds it. Red when: a surface lacks it.
- **AC2** — When `check-template-size.sh` measures the rendered Skill and `adopt-unattended.sh --check` runs, both exit 0. Red when: the Skill outgrows its budget or drifts from its template.

## 7. Gates

`unattended kit gate` · `unattended skill size` · `unattended skill wiring` · `check-wiring self-test` · `lexicon naming predicates`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the site named in §2. Recall terms used: `--terms "held job red suite daily remote-ci PYTHONUTF8 cp1252 reconfigure fixture stale launcher overlaps"`.
