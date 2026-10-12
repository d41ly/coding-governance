# TOOL-aScoutedSeam-3 — the scout's diff mode: a landed diff checked against the tree and the `## reuse` seams

**Status:** SPECCED · rev-2 · 2026-10-11 · node a · Tier-2 · base d19938f3 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md) | research | TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 KICK-aScoutedSeam-1 DEPL-aScoutedSeam-1 |
| [2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md) | research | TOOL-aScoutedSeam-1 |
| [2026-10-13-prompt-TOOL-aScoutedSeam-1-brief.md](../prompts/2026-10-13-prompt-TOOL-aScoutedSeam-1-brief.md) | research | TOOL-aScoutedSeam-1 KICK-aScoutedSeam-1 DEPL-aScoutedSeam-1 |

<!-- /gen:spec-records -->

## 1. Goal

Catch the duplicate a pre-spec scout cannot see, because it is written inside a helper during the
build. Half of gov's twelve measured reinventions were of that kind. Reviewing the landed diff solved
three gov cases that every pre-spec arm answering them missed, and it emitted the fewest MUSTs of any
arm (`2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md`, arm D1).

## 2. Scope (IN)

- **S1** — `reuse-scout.js` accepts `mode: "diff"` with `base` and `head`, two commits the
  caller resolved, and the optional `reuse` lines the card's `## reuse` section carries. It refuses a
  base or head that is not 7 to 40 hex characters, and a missing `roles.scout`, each naming the field
  before any spawn.
  - AC1 observes it.
- **S2** — One spawn of the `gov-reuse-scout` role with a DIFF lens instruction, which has the agent
  check two things:
  - every unit of behaviour or style the diff ADDS, judged against the tree at `base`, reporting only
    a real duplicate with its existing seam, a binding and how the diff should use it instead;
  - for each MUST line in `reuse`, whether the diff wires through it: `used`, `bypassed`, or
    `not-applicable` with a reason.

  Edits to existing code, legitimately new capability, tests and records are not reported.
  - AC2 observes it.
- **S3** — The return shape below, and the same deterministic caps as the orient mode: at most 10
  duplicates, MUST first.
  - AC2 observes it.
- **S4** — The role body gains its DIFF section under the same constant block, beside the orient
  checklist of `TOOL-aScoutedSeam-1`.
  - AC3 observes it.
- **S5** — Where it runs. `memory/guides/BUILD-METHOD.md` is rendered from the memory-tree kit's
  `BUILD-METHOD.template.md`. In a build whose card carries `## reuse`, the template gains one
  sentence in the pass loop: after a unit's build pass and before its closing review, the caller runs
  diff mode over the unit's range. Each `bypassed` MUST and each MUST duplicate becomes a fold item
  exactly as a review finding does.
  - AC4 observes it.
- **S6** — Diff mode runs at effort `high` unless `args.effort` names another. The orient mode's
  `medium` is not reused here: at `medium` the measured diff reviewer solved 4 of 23 cases where
  `extra` solved 7, and it bound a quarter as many MUSTs.
  - AC3 observes it.

## 3. Non-goals (OUT)

- A reuse lens inside `tools/workflows/tier2-review.template.js`. Its finder lenses are prompt
  literals aOrientedCast's review-harness unit leaves in place, so wiring one in is that build's later
  change (Edges).
- A gate leg that refuses a merge on a `bypassed` MUST. A diff-time verdict is agent judgement, and
  the fold is where judgement is answered. The deterministic refusal is `TOOL-aScoutedSeam-2`'s spec
  join.
- Running diff mode on a build that never ran the orient mode. It still finds duplicates, but its
  wiring half has nothing to check, so the method text names it only where `## reuse` exists.

### Edges

- **consumes-from** `TOOL-aScoutedSeam-1` — the harness, the role slot and the merge it extends;
  without it there is no script to add a mode to.
- **consumes-from** `KICK-aScoutedSeam-1` — the card's `## reuse` section the wiring half reads.
- **hands-off** external — wiring a reuse lens into the Tier-2 review harness, after aOrientedCast's
  review-harness unit lands; aOrientedCast confirmed on 2026-10-11 that its lenses stay literals.

## 4. Design

### Data model

The diff-mode args add three keys to `TOOL-aScoutedSeam-1`'s table:

| key | type | rule |
|---|---|---|
| `base` | string | 7-40 hex, resolved by the caller, never a ref name |
| `head` | string | 7-40 hex, resolved by the caller |
| `reuse` | string | the `## reuse` section verbatim, or empty |
| `effort` | string | absent means `high` in diff mode, not the orient mode's `medium` (S6) |

The return:

```json
{ "duplicates": [{"binding": "MUST", "path": "", "symbol": "", "new_code": "", "how": "", "evidence": ""}],
  "wiring": [{"seam": "<path> :: <symbol>", "verdict": "used", "why": ""}],
  "verdict": "clean", "lensesLive": 1 }
```

`verdict` is `clean`, `duplicates-found` or `bypassed`, and the strongest finding wins.

### Flow

1. The caller resolves `base` and `head` with `git rev-parse` and passes the card's `## reuse` text.
2. The script spawns one DIFF-lens agent. It reads `git diff --stat` first, then the added hunks.
3. The caller turns each MUST duplicate and each `bypassed` MUST into a fold item; a SHOULD is
   reported, not folded.

### Inventory

| identifier | cell |
|---|---|
| `renderDiffTask`, `checkDiffArgs` | js.function |
| `DIFF_SCHEMA` | js.constant |

### Files touched (estimate)

- `tools/workflows/reuse-scout.template.js`
- `tools/workflows/reuse-scout.js`
- `tools/workflows/reuse-scout.test.sh`
- `tools/workflows/README.md`
- `tools/roles/agents/gov-reuse-scout.agent.md` (body only)
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`

### Rollout

Inert until a caller passes `mode: "diff"`. The method sentence binds only a build whose card carries
`## reuse`, which exists only after an owner opt-in.

### Alternatives rejected

- **Grading the diff with the lookup.** The lookup matches names, and a duplicate's name is new by
  definition.
- **A deterministic duplicate detector over symbols.** It finds same-named copies; the measured
  duplicates were renamed re-implementations (`_marker_index` against `unfenced_lines`).

## 5. Production-readiness checklist

- security: read-only; the agent runs `git diff` and reads files, and writes nothing.
- perf / scale: measured per diff reviewer, medians, 2026-10-11: 28 tool calls and 31 minutes at
  `extra`, against 8 and 4 minutes at `medium`. Recall fell with that cost, which is why S6 sets
  this mode's default above the scout's.
- error / empty / loading states: a dead agent returns `lensesLive` 0 and no verdict, never `clean`.
- observability: the verdict and the wiring rows are the caller's fold input, and they are recorded
  with it.
- risks: a false `bypassed` sends a fold after a seam that does not fit. The fold answers it, the way
  it answers any review finding.
- testing: the stub suite of `TOOL-aScoutedSeam-1` gains the diff-mode arms.
- migration: N/A — a new mode on a new harness.
- user docs: `tools/workflows/README.md` documents the mode beside the orient mode.

## 6. Acceptance criteria

- **AC1** — When `reuse-scout.js` is given `mode: "diff"` with `base: "main"`, the stub suite
  records a refusal naming `base` and no spawn.
  Red when: a ref name reaches the agent and the review grades a moving range.
- **AC2** — When the stub diff agent returns one MUST duplicate and one `bypassed` wiring row, the
  return's `verdict` is `bypassed` and both rows survive the cap.
  Red when: the verdict takes the first finding instead of the strongest.
- **AC3** — When the shipped harness runs diff mode at its default effort on the three below-spec gov cases of
  `2026-10-11-build-TOOL-aScoutedSeam-1-3-cases.json`, `bench.py grade` reads at least two of them
  solved, with each run's duplicates collected as its seams. The cases are the quoted-headings brief
  reader, the pooled-sweep wall watchdog and the keyed-decisions id regex.
  Red when: the role's diff section loses the instruction to judge only ADDED code against the tree
  at `base`.
  cost: three agents at effort `high`, between the measured 4 and 31 minutes each.
  fixture: `bench.py d1` rebuilds the parent worktrees and the diffs.
  figure: DERIVED by `bench.py grade`.
- **AC4** — When the memory-tree kit re-renders the method, the rendered `BUILD-METHOD.md` carries
  the diff-mode sentence written in `BUILD-METHOD.template.md`, and the two compare byte-identical.
  Red when: the live copy is edited by hand, so the render and the template disagree.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `build-method size` · `memory hygiene` · `recall floor` · `recall floor arms` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test`

New arm: tools/workflows/reuse-scout.test.sh · covers AC1 AC2 · stub diff returns staged per arm · none

## 8. Open questions

- **F1 — Should diff mode run per unit or once over the build's range before the closing review?** Per
  unit catches a duplicate before the next unit copies it. Once per build halves the cost on a large
  build. Recommendation: per unit, because two measured duplicates were copied forward by a sibling
  unit.
- **F2 — Is `high` enough for diff mode, or should it default to `extra`?** `medium` was measured
  and lost 3 of 7 solved cases, and `extra` cost 31 minutes per diff; `high` was not measured.
  Recommendation: `high`, with AC3 as the measurement. If AC3 falls short, the default moves to
  `extra`.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S6 · §4 · §5 · §8 · AC3 · the effort comparison measured the diff reviewer at
  `medium` solving 4 of 23 where `extra` solved 7. This mode therefore defaults to `high`, and F2
  asks whether `high` is enough.

## 10. Reuse audit

The seam this unit extends is `TOOL-aScoutedSeam-1`'s harness and role. Its review-shaped return copies
the finding shape of `tools/workflows/tier2-review.template.js`, so a fold reads it the way it reads a
review. `tools/codebase-map/reuse_lookup.py "check that a diff wires through the seams the orientation
named and does not re-implement existing code"` ranked `check`, `note` and `wired` by name stem, and
none of them reviews a diff, so no existing seam fits beyond the two named.

Recall terms used: diff review duplicate re-implementation seam fold closing review pass loop wiring reuse
