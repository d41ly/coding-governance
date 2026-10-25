# TOOL-dDeclaredLoop-63 — an adopter's extra phase reads as ungated through the driver's own phase set, never refused for lacking a row

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 35 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-63-deviation-631.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-63-deviation-631.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 56 at HIGH**, its item **H8**, alone in that item; id 35 is the same defect at
medium grade, item M16, batched into `TOOL-dDeclaredLoop-67`. The driver's phase vocabulary is
`phases()`, `PHASES_CORE` plus the conf's `PHASES_EXTRA` (`tools/unattended/unattended.sh:1069`, :852,
:842), and `verb_phase` admits any member of it (:6140-6143). `TOOL-dDeclaredLoop-52` maps
`PHASES_CORE` alone, and its §5 says a phase with no row refuses by name, while S4 has the `--phase`
refusal ask `loop_table.py phase <PHASE>`. So once it lands, every `--phase` move into an adopter's own
phase is refused, wedging that adopter's unattended runs. This unit gives an extra phase a defined
reading taken from the driver's resolved set. It repairs `TOOL-dDeclaredLoop-52`.

## 2. Scope (IN)

- **S1** — `derive_phase_position(phase, halt_code=None, hold=None, extra=())` answers
  `("none", "none")` for a phase with no row that is a member of `extra`, and still refuses by name a
  phase in neither the map nor `extra`. The CLI gains `--extra "<space-separated phases>"` and prints
  `state none · step none · adopter phase` for such a phase. This amends `TOOL-dDeclaredLoop-52` §5's
  "a phase with no row refuses by name" to phases outside the driver's set. Observed by AC1.
- **S2** — The population is the driver's own answer: the `--phase` consumer in
  `tools/unattended/unattended.sh` passes `--extra "$PHASES_EXTRA"`, the half of `phases()` the conf
  supplies, so the loop kit never re-derives the vocabulary from conf text. Observed by AC2.
- **S3** — Step `none` is ungated: the `--phase` refusal `TOOL-dDeclaredLoop-19` S6 makes past a gated
  step exit has no step exit to pass for an adopter phase, so the move is admitted, and `--plan` prints
  the `adopter phase` reading. Observed by AC2.
- **S4** — The fixture case `phases-extra` joins `loop_table.py --fixture`: a scratch conf declaring
  `PHASES_EXTRA="STAGING"` and a `--phase STAGING` move. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The `[[phase]]` check's population, `check_transition_tables` joining over the driver's set: the
  audit's id 35, batched into `TOOL-dDeclaredLoop-67`.
- An overlay through which an adopter maps its own phases to states and steps: no clause names one, and
  an unmapped phase reading as ungated is the defined default the finding asks for.
- A checklist entry that a reader of a configurable vocabulary reads the owner's resolved answer, the
  finding's left-shift: the class is recorded at the close; S4 is this reader's adopter fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-52` — `derive_phase_position`, the `loop_table.py phase` CLI and its `--phase` consumer, whose reading of an unmapped phase this unit defines
- **hands-off** `TOOL-dDeclaredLoop-67` — the adopter-phase reading, whose population that unit's check of the phase rows matches (id 35)
- **hands-off** `TOOL-dDeclaredLoop-70` — the default of `extra`, which that unit makes the driver's population for every caller (the round-3 spec audit's id 19)
- **hands-off** `TOOL-dDeclaredLoop-75` — §5's protocol sentence in the template and its render (the round-3 spec audit's id 35); this pass keeps the `loop transition tables` leg green (id 31)

## 4. Design

### Evidence

- `phases() { printf '%s %s\n' "$PHASES_CORE" "$PHASES_EXTRA"; }` (`tools/unattended/unattended.sh:1069`);
  `PHASES_EXTRA` is an optional adopter key (`tools/unattended/kit.toml:174`) and gov's conf sets it
  blank (`.unattended.conf:289`).
- `verb_phase` refuses only a phase outside `phases()` (:6140-6143); no driver verb prints the set, so
  the consumer passing the variable it already holds is the one read that is the owner's.

### The reading

| Phase | Row | Answer |
|---|---|---|
| a `PHASES_CORE` member | its row | the row's state and step |
| a `PHASES_EXTRA` member | none | `state none · step none · adopter phase`, ungated |
| neither | none | refused by name, exit 2 |

### Files touched (estimate)

- `tools/loop/loop_table.py`
- `tools/unattended/unattended.sh`

### Alternatives rejected

- **Parsing `PHASES_EXTRA` out of `.unattended.conf` in Python.** It re-derives a value the driver
  composes by sourcing the conf, the two-readers class the finding names.
- **A new driver verb printing `phases()`.** A public surface no clause of this build names; the
  consumer already holds the value.

## 5. Production-readiness checklist

- security — an adopter phase is admitted ungated, as it is before `TOOL-dDeclaredLoop-52` lands; the
  owner gates of core phases are unchanged.
- perf / scale — one more argument on one call.
- error / empty / loading states — a blank `PHASES_EXTRA` passes `--extra ""` and changes nothing.
- observability — the `adopter phase` reading is printed on `--plan`.
- risks — an adopter phase spelled like a core phase is a core phase; the driver's own membership test
  has the same rule.
- testing — AC1 and AC2 as plants and a scratch-run probe; the arm under §7, observed at the close.
- migration — none.
- user docs — the unattended protocol's breakpoint text, `TOOL-dDeclaredLoop-19` S10's, gains one
  sentence on adopter phases.

## 6. Acceptance criteria

- **AC1** — When `python loop_table.py phase STAGING --extra "STAGING"` runs, it prints
  `state none · step none · adopter phase` and exits 0; `python loop_table.py phase STAGNG --extra
  "STAGING"` exits 2 naming `STAGNG`.
  Red when: the map is the whole population, so `STAGING` is refused for lacking a row.
- **AC2** — When a scratch repository whose `.unattended.conf` sets `PHASES_EXTRA="STAGING"` holds a run
  in `REVIEWING` and runs `unattended.sh --phase <slug> STAGING`, the move is admitted.
  Red when: the consumer omits `--extra`, so the loop kit refuses the adopter's phase.
  cost: one scratch repository and one run-state file, seconds.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_table.py · covers AC1 · the `phases-extra` plant, staged against `TOOL-dDeclaredLoop-52`'s reading, which refuses a phase with no row · none

The unattended kit's own suites are waived for this build's landing (README rule 8); AC2 is a probe.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 56 (HIGH, item H8).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-70 and TOOL-dDeclaredLoop-75, written by the round-3 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is the driver's `phases()` (`tools/unattended/unattended.sh:1069`) and the `PHASES_EXTRA` value
its `--phase` consumer already holds, passed to `TOOL-dDeclaredLoop-52`'s reader. `python
tools/codebase-map/reuse_lookup.py "adopter phase vocabulary extension PHASES_EXTRA"` ranked `adopt`,
`phases`, `require_adopted_root`, `derive_phase` (`tools/runlog/model.py`) and `read_recorded_phase`;
`phases` is the composer this unit reads, and the runlog `derive_phase` reads a record's phase, not the
vocabulary.

Recall terms used: PHASES_EXTRA PHASES_CORE phases adopter phase map derive_phase_position loop_table --phase gated step
