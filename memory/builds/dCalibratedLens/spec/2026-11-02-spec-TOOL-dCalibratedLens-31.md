# TOOL-dCalibratedLens-31 — a shape's optional `[ · …]` group rendered as its content or dropped, and every fenced shape's rendered line admitted by the format guard

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 13 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-31-deviation-311.md](../build/2026-11-02-build-TOOL-dCalibratedLens-31-deviation-311.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-31-1-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-31-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 30, BLOCKER, item B1 of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`). Unit 25 S1 gives the
`returned` shape an optional `[ · units <units>]` group and names one consumer of it, the format
guard's `buildShapeRegex`. The other consumer is `render_shape_line` in `tools/roles/handoff.py`,
which `print_agent_lines` calls for every `agent` and `returned` line it prints. It replaces only
`<name>` placeholders and has no bracket handling, so every `returned` line the roles kit prints
would carry literal `[` and `]`, which the charter's `[grammar]` rule says never appear in an
emission and which the live format guard refuses. This unit teaches the renderer the group and
holds the renderer and the guard to one another over every shape the fence defines. It repairs
`TOOL-dCalibratedLens-25`.

## 2. Scope (IN)

- **S1** — The renderer. `render_shape_line(definition, fields)` in `tools/roles/handoff.py` splits
  the definition on its `[ · …]` groups the way `buildShapeRegex` does
  (`tools/hooks/format-guard.js:164-179`): a group opens at the literal `[ · ` and closes at the next
  `]`, so a markdown link such as `[<name>](<path>)` is never a group. A group whose every `<name>` is
  a key of `fields` renders as its content without its brackets; a group naming any other placeholder
  renders as nothing, so its text never reaches the line. A placeholder outside every group still
  raises `RolesError` when `fields` lacks it, as today, and each value's ` · ` and line breaks are
  still folded as today. Observed by AC1 and AC2.
- **S2** — The arm, in `tools/roles/adopt-roles.test.sh`: it reads the charter fence of the
  repository's `AGENTS.md` with `roles_lib.extract_microformat_shapes`, renders each definition
  twice through `render_shape_line` (once with every placeholder filled by the sample value `x`, once
  with only the placeholders outside every group filled), and pipes both lines to one `node`
  process that loads the hooks kit's `format-guard.js`, found by `roles_lib.resolve_kit_dir` as the
  suite's arm 6 finds it, and asserts that `buildShapeRegex` of that definition admits each line. One
  assertion per definition and form; the suite's `FLOOR_ASSERTIONS` rises by the count. A definition
  ending in the repeat marker `…` (the `gates` shape) is a variable-length shape no renderer prints
  from a dict; the arm lists its head as `not rendered` and asserts nothing for it. A missing
  hooks kit or `node` SKIPs the arm by name and lowers the floor by its count, as arm 6 does.
  Observed by AC3.

## 3. Non-goals (OUT)

- Changing `buildShapeRegex` or `checkCarries`. The guard's grammar is the contract; the renderer
  follows it.
- The `units` field's position and the guard's fixtures R1u to R3u: `TOOL-dCalibratedLens-25` S1 and
  S2, unchanged.
- The leg's guard: `TOOL-dCalibratedLens-37`, id 24.
- A skip read as coverage. The arm SKIPs only where the hooks kit is absent; in this repository it is
  present, and this repository's run is the coverage.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-25` — the `returned` fence carrying the `[ · units <units>]` group, the first group `print_agent_lines` renders; without it the arm still renders the `SPEC` shape's group, but no printed line exercises S1

## 4. Design

### Evidence

- `tools/roles/handoff.py:708-719` at base: `render_shape_line` substitutes `SHAPE_FIELD_RE`
  (`<([^<>]+)>`, `:124`) matches and nothing else; `print_agent_lines` renders every head through it
  (`:917` and `:926`).
- The review's probe ran `render_shape_line` on unit 25's amended definition and printed
  `- returned — r · c · 3m · 12k out[ · units -] · run direct/a1`.
- `AGENTS.md:55-69` at base: the `SPEC` shape already carries an optional group, `[ · open
  <ids|none>]`, and the `agent` shape a markdown link, `prompt [<name>](<path>)`, which is not a
  group. The `merged` shape carries a group with no placeholder, rendered whole by S1. The `gates`
  shape ends in ` …`, which `buildShapeRegex` turns into a repeat. The `[grammar]` rule
  (`AGENTS.md:76`) says the bracket never appears in an emission.
- `tools/hooks/format-guard.js:554` exports `buildShapeRegex`, so a `node -e` caller reads the
  guard's own regex rather than a copy.
- `tools/roles/adopt-roles.test.sh:160-173`: arm 6 resolves the hooks kit through
  `roles_lib.resolve_kit_dir("hooks", "agent-cap.js", …)` and SKIPs naming what is absent.

### The rendering, by example

```
definition: returned — <role> · <outcome> · <wall> · <tokens> out[ · units <units>] · run <run-id|direct>/<agent-id>
units held: - returned — r · c · 3m · 12k out · units - · run direct/a1
units not held: - returned — r · c · 3m · 12k out · run direct/a1
```

### Inventory

No identifier is minted. The arm adds assertions to an existing suite.

### Files touched (estimate)

- `tools/roles/handoff.py` — S1
- `tools/roles/adopt-roles.test.sh` — S2

### Alternatives rejected

- **Render the group always, brackets stripped.** A definition whose group names a field the deriver
  lacks would raise or print `unknown`, where the shape says the field is optional.
- **An arm in the format guard's own suite.** That suite's leg is guarded on the hooks kit only
  (`tools/gate-legs.json`), so a renderer edit would not select it; the roles adopter self-test
  carries no guard and runs on every bar.

## 5. Production-readiness checklist

- security — no new surface; a value is still folded so it cannot add a field.
- perf / scale — one split per definition, and one `node` process per arm run.
- error / empty / loading states — a group whose field is absent is dropped, never printed empty.
- observability — a refused line is printed by the arm with its definition's head.
- risks — a future definition nesting a group inside a group: the split takes the first `]`, as the
  guard does, so both read it the same way.
- testing — AC1 and AC2 by the pass; the arm of S2 at the close.
- migration — N/A: no stored line changes.
- user docs — N/A: the fence is the definition and its rule already says the bracket never appears.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe from the roles kit directory calls
  `handoff.render_shape_line` with the `returned` definition carrying `[ · units <units>]` and a
  dict holding `units`, it prints a line with ` · units ` before ` · run ` and no `[` or `]`.
  Red when: the line carries the bracket or loses the field.
- **AC2** — When the same probe passes a dict without `units`, the line holds no `units` and no
  bracket, and when the dict lacks `role` the call raises `RolesError` naming `role`.
  Red when: an absent optional field raises, or an absent required field renders.
- **AC3** — When `node -e` loads `format-guard.js` and tests the lines the S2 arm renders for every
  fenced definition of `AGENTS.md`, `buildShapeRegex` admits each, and under the staged break (S1
  reverted) it refuses the `SPEC` and `returned` lines.
  Red when: any rendered line is refused, or the reverted renderer passes.

## 7. Gates

`roles adopter self-test` · `policy fixtures` · `micro-format definitions` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/roles/adopt-roles.test.sh · covers AC3 · every fenced definition rendered through `render_shape_line` and fed to `buildShapeRegex`, staged red by the renderer with its group handling removed · FLOOR_ASSERTIONS raised by the assertions added

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 30 (BLOCKER, item B1) of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; unit 25 amended at the disposal (its rev-2).

## 10. Reuse audit

The seam extended is the shape grammar both consumers already share: `render_shape_line` in
`tools/roles/handoff.py` gains the `[ · …]` rule `buildShapeRegex` in `tools/hooks/format-guard.js`
already applies, and the arm calls the exported guard function rather than a copy. `python
tools/codebase-map/reuse_lookup.py "render an optional bracket group of a shape definition into an
emitted line"` ranked name stems only (`shape` in `tools/govkit/matrix.py`, `render`, `render_line`
in `tools/runlog/runlog_lib.py`); none renders a bracket group, so the rule is added to the one
renderer rather than minted beside it. The recall probe returned TOOL-cMendedVintage-19, the
placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
