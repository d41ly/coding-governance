# TOOL-dDeclaredLoop-45 — a unit reads `built` from its pass commit while no acceptance writer is armed

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 18 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-45-deviation-451.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-45-deviation-451.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 6 at HIGH**, its item **H6**, alone in that item. `TOOL-dDeclaredLoop-7` S2
marks a unit `built` only when an attributed pass commit sits on the run branch and the unit's
acceptance record holds. The only writer of that record is `TOOL-dDeclaredLoop-17`'s stand-in
`loop_witness.py acceptance`, which writes only when a caller runs it, and `TOOL-dDeclaredLoop-17` §3
says there is no executor and that the stand-in parses no spec. So once `--plan` reads the engine, every
unit with its pass commit reads `designed`, and the `next:` line keeps naming built units as live, a
regression from today's ladder; the fixtures plant acceptance records, so `TOOL-dDeclaredLoop-7` AC1 and
AC10 stay green over the gap. This unit takes the report's second fix. It repairs
`TOOL-dDeclaredLoop-7`.

## 2. Scope (IN)

- **S1** — The acceptance half of `built` is armed by the `[[computed-witness]]` row `acceptance`
  (`TOOL-dDeclaredLoop-17` S7), read through `read_computed_witnesses`: while that row names the
  stand-in `loop_witness.py acceptance` as its writer today, the half is unarmed; once a build re-points
  it to the executor, it is armed. Observed by AC1, AC3.
- **S2** — Unarmed, `derive_unit_step` reads `built` from the attributed pass commit alone and prints the
  unit line as `unit — <id> · built · acceptance unarmed`; an acceptance record that exists is still
  read, and one whose runs do not hold keeps the unit `designed`, so a stand-in's refutation is never
  ignored. Armed, `TOOL-dDeclaredLoop-7` S2 stands unchanged. This supersedes S2's unconditional
  acceptance requirement while the writer is the stand-in. Observed by AC1, AC2.
- **S3** — `TOOL-dDeclaredLoop-7` AC10 gains a case: a unit with its pass commit and no acceptance record,
  whose `next:` line from `unattended.sh --plan` does not name that unit as live. Observed by AC3.

## 3. Non-goals (OUT)

- Wiring the stand-in into the pass path: `TOOL-dDeclaredLoop-17` §3 refuses any parse of a spec's
  acceptance commands, so no caller can name them for it; the executor's build arms the writer.
- The `tested` and `deployed` witnesses: `TOOL-dDeclaredLoop-7` S2's, unchanged.
- A spec-set join of record kinds with readers and no writer, the finding's left-shift: not named by any
  clause of this build; the class is recorded at the close.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-7` — `derive_unit_step` in `tools/loop/position.py` and the `--plan` `next:` line it renders, whose `built` witness this unit arms by state
- **consumes-from** `TOOL-dDeclaredLoop-17` — `read_computed_witnesses` and the `acceptance` row's writer, which say whether the acceptance half of `built` is armed
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 11, 44 and 48: this pass keeps the loop position fixtures leg green; the armed predicate's named constant and the amended line grammar are scope items of that unit

## 4. Design

### Evidence

- `TOOL-dDeclaredLoop-17` §4 "The computed witness kinds" lists `acceptance` with writer today
  `loop_witness.py acceptance` and armed by the executor's build, dWellOiledMachine; S7 names its reader
  `read_computed_witnesses`.
- `TOOL-dDeclaredLoop-7` S2 names the four witnesses and §4 "The `next:` line" maps an `act` answer on a
  Design or Build item to the live-unit shape, so a built unit read as `designed` is printed live.

### The rule

| Acceptance writer (computed-witness row) | Record | Pass commit | Step |
|---|---|---|---|
| stand-in | none | present | `built`, `acceptance unarmed` |
| stand-in | holds | present | `built` |
| stand-in | does not hold | present | `designed` |
| executor | none or not holding | present | `designed` |
| executor | holds | present | `built` |

### Files touched (estimate)

- `tools/loop/position.py`
- `tools/unattended/unattended.sh`

### Alternatives rejected

- **Wiring `loop_witness.py acceptance` into `--dispatch`'s close.** The caller would have to extract the
  criterion commands from a spec, which `TOOL-dDeclaredLoop-17` §3 rejects: a criterion carries several
  backticked tokens and prose, so any parse guesses.
- **Dropping the acceptance half until the executor lands.** A stand-in record that refutes a criterion
  would then be ignored.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one more read of the loop definition's computed-witness rows per engine call, cached.
- error / empty / loading states — unarmed is printed on the unit line, never silent.
- observability — the `acceptance unarmed` tag on each unit read that way.
- risks — until the executor lands, `built` rests on the pass commit, today's ladder's rule.
- testing — AC1 to AC3 as plants and a probe; the arm under §7, observed at the close.
- migration — none.
- user docs — none beyond `help/loop.md`, which `TOOL-dDeclaredLoop-1` owns.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant built-unarmed` runs, a unit with its
  pass commit and no acceptance record prints `unit — <id> · built · acceptance unarmed`.
  Red when: the missing record keeps the unit `designed`.
- **AC2** — When `--plant built-refuted` runs, a unit whose stand-in record carries a run that does not
  hold prints `designed`; and with the fixture's `acceptance` row re-pointed to an executor writer,
  `--plant built-unarmed`'s unit prints `designed`.
  Red when: the unarmed reading ignores a record that exists, or survives the writer being armed.
- **AC3** — When `bash tools/unattended/unattended.sh --plan <slug>` runs over the `built-unarmed`
  fixture, its `next:` line does not name the built unit.
  Red when: the line names the built unit as live, the regression the finding records.
  fixture: the `built-unarmed` fixture repository; the unattended kit's suites are waived for this
  landing (README rule 8), so this is a probe.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/position.py · covers AC1 AC2 · the `built-unarmed` and `built-refuted` plants, staged against `TOOL-dDeclaredLoop-7`'s rule, which reads the first `designed` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Wire the stand-in, or read `built` from the pass commit while unarmed?** Options: (a) the stand-in
  run by the pass path; (b) S2's state-armed rule. (a) violates `TOOL-dDeclaredLoop-17` §3's non-goal,
  veto 1. RESOLVED (agent, 2026-10-24, delegated): (b), rung 3. It relaxes nothing against base, whose
  ladder reads the pass commit alone. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 6 (HIGH, item H6).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dDeclaredLoop-17`'s `read_computed_witnesses`, the one declaration of which computed
witness has which writer, and `TOOL-dDeclaredLoop-7`'s `derive_unit_step`; the rule adds a table read,
never a second list of armed witnesses. `python tools/codebase-map/reuse_lookup.py "a witness whose
writer is not yet armed reads unarmed"` ranked generic name-stem hits (`read`, `read_text`, `write`,
`note`, `arm`), none of which grades a witness by its writer; both seams are minted in this build, so
the map has not indexed them yet.

Recall terms used: built acceptance record unarmed stand-in executor computed-witness position next plan pass commit
