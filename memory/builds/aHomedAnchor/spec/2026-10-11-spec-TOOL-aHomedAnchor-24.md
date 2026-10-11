# TOOL-aHomedAnchor-24 — the `--overlaps` verb is named on both surfaces an agent reads

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 6 · closes TOOL-aHomedAnchor-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md](../prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md) | journal | TOOL-aHomedAnchor-22 TOOL-aHomedAnchor-23 TOOL-aHomedAnchor-25 |

<!-- /gen:spec-records -->

## 1. Goal

Gate shard 1/8 is red: `--overlaps`, which `KICK-aMendedFleet-2` added for the orientation card, is dispatched but absent from the Skill and from `VERBS_INLINE`, the declaration the refusal text renders.

## 2. Scope (IN)

- S1. `VERBS_INLINE` in `tools/unattended/unattended.sh` carries `--overlaps`. Observed by AC1.
- S2. `tools/unattended/SKILL.template.md` names `unattended.sh --overlaps  # local`, an argument after
  the verb because the leg's check 26 reads `unattended.sh <verb> ` with its trailing space; the
  rendered Skill is re-rendered, and two sentences outside the gated blocks are shortened to keep it
  at or under 10240 bytes. Observed by AC1 and AC2.
- S3. The verbs carrier, `tools/unattended/VERBS.template.md` and its byte-identical copy
  `memory/guides/UNATTENDED-VERBS.md`, gains a `--overlaps` entry beside `--claims`, the third surface
  check 26 joins. Observed by AC1.

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
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

## 6. Acceptance criteria

- **AC1** — When the suite arm's three surface greps and the leg's check 26 joins run for `--overlaps`,
  each finds it. Red when: a surface lacks it.
- **AC2** — When `check-template-size.sh` measures the rendered Skill and `adopt-unattended.sh --check` runs, both exit 0. Red when: the Skill outgrows its budget or drifts from its template.

## 7. Gates

`unattended kit gate` · `unattended skill size` · `unattended skill wiring` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S2 S3 AC1 · check 26 of the leg also reads the verbs carrier and wants a
  trailing argument in the Skill; found by the cross-component slice.

## 10. Reuse audit

No existing seam fits beyond the site named in §2. Recall terms used: `--terms "held job red suite daily remote-ci PYTHONUTF8 cp1252 reconfigure fixture stale launcher overlaps"`.
