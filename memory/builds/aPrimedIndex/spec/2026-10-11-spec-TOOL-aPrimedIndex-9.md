# TOOL-aPrimedIndex-9 — the lexicon render proves freshness alone

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-1 · base 29653d90 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aPrimedIndex-9-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-9-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The lexicon kit's staged `[[regenerate]]` row proves its render fresh with the kit's `[check]`, which
is the whole naming gate. Main carries inherited naming violations, so after the reconcile the
preflight read that row STALE, and a regeneration cannot cure it: every bar would refuse. Give the
row a check that compares the render and nothing else.

## 2. Scope (IN)

- **S1** — `adopt-lexicon.sh --check-render` runs the existing Skill byte-compare alone: exit 0 when
  the rendered Skill matches a fresh render or no `.lexicon.conf` is present, 1 when it drifted.
  Observed by AC1.
- **S2** — The lexicon `[[regenerate]]` row carries `check` naming that mode, so `regen.py` stops
  falling back to the kit's `[check]`. Observed by AC2.

## 3. Non-goals (OUT)

- The naming violations main carries are not fixed here; the lexicon leg keeps grading them.
- `regen.py` is unchanged: a row-level `check` already overrides the kit's.
- No kit version is bumped by hand: the lander mints it, as the build README rules.

### Edges

- **consumes-from** `TOOL-aPrimedIndex-1` — the descriptor row being narrowed.

## 4. Design

One mode branch beside `--render` in `tools/lexicon/adopt-lexicon.sh`, calling `check_skill`, the
function `--check` already calls for the same compare. No new function.

### Files touched (estimate)

- `tools/lexicon/adopt-lexicon.sh`
- `tools/lexicon/kit.toml`
- `tools/lexicon/selftest.py`
- `tools/lexicon/README.md`

## 5. Production-readiness checklist

- security: read-only; the mode writes nothing.
- perf / scale: one render, against the whole gate's 73 s measured on the merged tree.
- error / empty / loading states: no conf exits 0 as `--check` does; an empty render refuses through
  `check_skill`.
- observability: `check_skill`'s own DRIFTED lines.
- risks: none beyond the compare `--check` already runs.
- testing: a selftest arm over a drifted and a fresh Skill.
- migration: none.
- user docs: the kit README names the mode.

## 6. Acceptance criteria

- **AC1** — When the rendered Skill has one byte changed, `--check-render` exits 1 and prints
  `lexicon: DRIFTED`; when it matches, it exits 0. Red when: the mode is absent or ignores the drift.
- **AC2** — When `regen.py --check` runs over the merged tree that carries main's naming
  violations, the lexicon row reads `fresh`. Red when: it reads STALE, as it does with the kit's
  `[check]`.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `codebase-map coverage + freshness`

New arm: tools/lexicon/selftest.py · covers AC1 · a drifted Skill and a fresh one · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, adopted from the reconcile's preflight observation.

## 10. Reuse audit

The compare is `check_skill` in `tools/lexicon/adopt-lexicon.sh`, reused as is; the row-level
`check` override is `build_items` in `tools/run-gates/regen.py`. No existing seam fits a render-only
lexicon check: `reuse_lookup.py` ranks only other kits' `render` functions, none comparing the lexicon
Skill, and `govkit.py` has no render-compare verb.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.
