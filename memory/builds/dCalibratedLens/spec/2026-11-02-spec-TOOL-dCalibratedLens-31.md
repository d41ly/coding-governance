# TOOL-dCalibratedLens-31 — a shape's optional `[ · …]` group rendered as its content or dropped, and every fenced shape's rendered line admitted by the format guard

**Status:** DEFERRED · rev-2 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 13 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-31-deviation-311.md](../build/2026-11-02-build-TOOL-dCalibratedLens-31-deviation-311.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-31-1-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-31-1-spec-writer.md) | journal | — |
| [2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md](../reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 |

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
- **S2** — The arm, in `tools/hooks/format-guard.test.sh` beside its AC6 parity arm, the suite whose
  guard names the hook and, once `TOOL-dCalibratedLens-47` lands, the roles renderer and `AGENTS.md`
  (round-3 id 6). The suite resolves the roles kit with its own `resolve_kit_dir` as it resolves the
  runlog kit (`tools/hooks/format-guard.test.sh:234`). A python step reads the charter fence of the
  repository's `AGENTS.md` with `roles_lib.extract_microformat_shapes` and renders each definition
  through `render_shape_line` in two forms: every placeholder filled by the sample value `x`, and
  only the placeholders outside every group filled. It writes each line as UTF-8 bytes through
  `sys.stdout.buffer.write`, as `tools/roles/handoff.py:933` does, and one `node` process that loads
  the hook beside the suite reads its stdin as `utf8` and asserts that `buildShapeRegex` of that
  definition admits each line (round-3 id 14). One assertion per definition and form; the suite's
  `FLOOR_ASSERTIONS` rises by the count. A definition ending in the repeat marker `…` (the `gates`
  shape) is a variable-length shape no renderer prints from a dict; the arm lists its head as
  `not rendered` and asserts nothing for it. A missing roles kit or `node` SKIPs the arm by name and
  lowers the floor by its count. Beside the guard's verdict, each line is held free of a literal
  bracket by `TOOL-dCalibratedLens-44` (round-3 id 12); a render error and a shape with one form are
  `TOOL-dCalibratedLens-45`'s (round-3 id 27). Observed by AC3.

## 3. Non-goals (OUT)

- Changing `buildShapeRegex` or `checkCarries`. The guard's grammar is the contract; the renderer
  follows it.
- The `units` field's position and the guard's fixtures R1u to R3u: `TOOL-dCalibratedLens-25` S1 and
  S2, unchanged.
- The leg's guard: `TOOL-dCalibratedLens-47`, round-3 ids 23 and 6.
- A skip read as coverage. The arm SKIPs only where the roles kit is absent; in this repository it is
  present, and this repository's run is the coverage.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-25` — the `returned` fence carrying the `[ · units <units>]` group, the first group `print_agent_lines` renders; without it the arm still renders the `SPEC` shape's group, but no printed line exercises S1
- **hands-off** `TOOL-dCalibratedLens-44` — the shape arm in `tools/hooks/format-guard.test.sh` and the lines it renders, which that unit's bracket assertion holds (round-3 id 12)
- **hands-off** `TOOL-dCalibratedLens-45` — the arm's python step and its two forms, whose render errors that unit reports as FAIL lines (round-3 id 27)
- **hands-off** `TOOL-dCalibratedLens-47` — the shape arm in `tools/hooks/format-guard.test.sh`, which runs the renderer that unit adds to the `format-guard self-test` guard (round-3 id 6)

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
- `tools/runlog/prose.py:34-51`: `build_shape_regex`, a Python port of the guard's group split, which
  the suite's AC6 arm (`tools/hooks/format-guard.test.sh:578-610`) holds to the hook (round-3 id 17).
- `tools/run-gates/run-gates.sh:3249-3251` holds every `subject = kit` or `chunk = selftests` leg when
  `GATE_SELFTESTS` is empty, and under `changed` (`:3070-3082`) a leg selects by its kit's shipped
  sources, or by its guard where no entry ships its suite (round-3 id 6).

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
- `tools/hooks/format-guard.test.sh` — S2

### Alternatives rejected

- **Render the group always, brackets stripped.** A definition whose group names a field the deriver
  lacks would raise or print `unknown`, where the shape says the field is optional.
- **The arm in the roles adopter self-test.** That leg carries no guard and is held on a default bar
  like every self-test (`run-gates.sh:3249-3251`); under `changed` an edit to `format-guard.js`
  never selects it, so the guard side of the contract would go unobserved. The hooks suite is
  selected by the hook and, through `TOOL-dCalibratedLens-47`'s entries, by the renderer, so one leg
  sees both sides (round-3 id 6).
- **Reuse `prose.py`'s group split from `render_shape_line`.** The roles kit requires
  `kickoff-manifest` and `memory-tree` only (`tools/roles/kit.toml:12`); reaching the runlog kit at
  print time adds a kit dependency for a ten-line split. The renderer keeps its own split, and this
  arm is what holds it to the guard, as AC6 holds `prose.py`'s, so a grammar change reds rather than
  drifts (round-3 id 17).

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
  fenced definition of `AGENTS.md`, `buildShapeRegex` admits each. Under the staged break (S1
  reverted) the guard refuses the all-filled `returned` and `merged` lines; the `SPEC` line it still
  admits is caught by `TOOL-dCalibratedLens-44`'s bracket assertion, and `returned`'s second form
  raises `RolesError` naming `units`, which `TOOL-dCalibratedLens-45` prints as that form's FAIL line
  (round-3 ids 12, 27 and 9). A run with `PYTHONUTF8=0` set prints the same verdicts (round-3 id 14).
  Red when: any rendered line is refused, the reverted renderer's `returned` and `merged` lines pass
  the guard, or a non-ASCII field crashes the pipe.

## 7. Gates

`format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `roles adopter self-test` · `policy fixtures` · `micro-format definitions` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/hooks/format-guard.test.sh · covers AC3 · every fenced definition rendered through `render_shape_line` and fed to `buildShapeRegex`, staged red by the renderer with its group handling taken out · FLOOR_ASSERTIONS raised by the assertions added

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 30 (BLOCKER, item B1) of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; unit 25 amended at the disposal (its rev-2).
- rev-2 · 2026-11-03 · §3 §4 §7 §10 S2 AC3 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`: S2 names the bracket assertion of
  `TOOL-dCalibratedLens-44` (id 12) and the render-error envelope of `TOOL-dCalibratedLens-45` (id 27),
  and AC3's staged red reads the lines that go red (ids 12, 27, and 9 of `TOOL-dCalibratedLens-48`);
  from `TOOL-dCalibratedLens-48`, the arm moves to the hooks suite with the §4 rationale corrected
  (id 6), its pipe is UTF-8 bytes (id 14), and `prose.py`'s split is named with why the renderer keeps
  its own (id 17); §3 gains the hands-offs to units 44, 45 and 47.

## 10. Reuse audit

The seam extended is the shape grammar both consumers already share: `render_shape_line` in
`tools/roles/handoff.py` gains the `[ · …]` rule `buildShapeRegex` in `tools/hooks/format-guard.js`
already applies, and the arm calls the exported guard function rather than a copy. A third reader of
the same split exists, `build_shape_regex` in `tools/runlog/prose.py`, held to the hook by the suite's
AC6 arm; §4 records why the renderer does not import it. `python
tools/codebase-map/reuse_lookup.py "render an optional bracket group of a shape definition into an
emitted line"` ranked name stems only (`shape` in `tools/govkit/matrix.py`, `render`, `render_line`
in `tools/runlog/runlog_lib.py`); the map's name-stem ranking did not surface `prose.py`, which the
round-3 audit found by reading the suite. The recall probe returned TOOL-cMendedVintage-19, the
placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
