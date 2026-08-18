# TOOL-aDeclaredBound-3 — the ratchet lookback becomes a project-layer declaration

**Status:** OPEN · rev-3 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

`_RATCHET_LOOKBACK = 14` decides how many lines above a pin drift-audit will look for the
justification that excuses a weakening move. It is a module constant in the kit engine. Move it to
drift-audit's PROJECT LAYER, which is the seam this kit already declares for per-adopter values.

## 2. Scope (IN)

- **S1** — `drift_signals.py` may declare `RATCHET_LOOKBACK`. The engine reads it with a defaulting
  accessor, so an adopter's layer that predates the key keeps 14 and does not fail to import.
- **S1c** — the hook's attribution window in unit 4 is a SEPARATE number from this one, and both
  specs say so. An adopter who narrows `RATCHET_LOOKBACK` and leaves the hook's window wide gets
  attribution lines the hook accepts and the ratchet reds on. They are independent by design here;
  coupling them would make this unit a dependency of unit 4, which the build's order does not have.
- **S1b** — the call path is named, because the value is consumed two frames below where it is
  read. `_justified` uses it for the window and `ratchet_findings` interpolates it into the
  message, and the latter receives a LIST of ratchets rather than the layer module. Both gain a
  lookback parameter defaulted to the shipped 14, resolved once at the layer-load site and threaded
  down. Without this the declaration has nowhere to arrive.
- **S2** — NOT a conf key. `drift_report.py`'s own docstring says `NO SECOND CONF` and reads the
  corpus root from `.memory-tree.conf` precisely so it never grows one. The project layer is where
  this kit already puts `PRODUCT_GLOBS`, `SHRINK_ONLY`, `HANDKEPT`, `PINS` and the ratchet
  declarations themselves — a lookback that governs those ratchets belongs beside them.
- **S3** — `drift_signals.template.py` declares it, commented, so a new adopter sees the knob.
- **S4** — a value that is not a positive integer is a NAMED refusal, on the same channel as the
  layer's other validation. `load_project_layer` already refuses a layer missing a required
  attribute; a present-but-nonsense one gets the same treatment rather than an arithmetic surprise
  deep inside a slice.
- **S5** — arms in both directions over one fixture: a justification placed just inside a declared
  lookback is accepted, the same justification just outside it is not, and the shipped 14 applies
  when the layer declares nothing.

## 3. Non-goals (OUT)

- The DEFAULT does not move. 14 is what an adopter who declares nothing keeps.
- The justification GRAMMAR is untouched. `<old> -> <new>` in its three spellings stays exactly as
  it is; this unit changes only how far the search window reaches.
- No change to which keys are ratcheted, or to the `weakens` direction of any of them.
- The lookback is not made per-RATCHET. One number for the layer, matching what exists today. A
  per-key window is a plausible follow-up and is not this unit.

## 4. Design

### Data model

| declaration | shipped default | home |
|---|---|---|
| `RATCHET_LOOKBACK` | 14 | `drift_signals.py`, beside the ratchets it governs |

### Why the project layer rather than a conf key

Three reasons, in order of weight. The kit's module docstring commits to no second conf, and a key
in `.memory-tree.conf` would make an unrelated kit's conf the home of this kit's constant — which is
the objection `TOOL-aDeclaredCeiling-1` ratified when it put the template ceilings in a sibling file
rather than in a conf. The ratchet declarations this number governs are already IN the project
layer, so the value and its subject stay in one file. And the layer is Python, so the declaration
can carry its justification as a comment in the same register as everything around it.

### Why it is worth declaring at all

The window is not a style preference, but the first draft's evidence for that was wrong and is
replaced here rather than quietly dropped. It claimed `TOOL-aLoosenedCeiling-3` came within two
lines of pushing its `<old> -> <new>` literal out of the window. Measured at every commit carrying
that literal: the justification sits at `.memory-tree.conf:107` and the key at line 113 — a
distance of 6 against a window of 14, so the margin was 8 lines and never close.

What survives is the argument that does not depend on a near miss. The window's width is a
statement about a repo's COMMENT DENSITY, and this one's is unusual: that same conf carries a
six-paragraph running history above a single key. A repo that writes one-line justifications wants
a narrower window, so a justification for a DIFFERENT pin further up cannot be read as this one's;
a repo denser than this one wants a wider one. Fourteen is a measurement of gov's habits that every
adopter currently inherits.

### Migration

An adopter layer with no `RATCHET_LOOKBACK` behaves exactly as today. `load_project_layer`'s
required-attribute list does not grow, so no existing layer becomes invalid.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py` — the constant becomes a default, plus the accessor and S4.
- `tools/drift-audit/drift_signals.template.py` — the declaration and its comment.
- `tools/drift-audit/drift_signals.py` — this repo's own layer, declaring the shipped value
  explicitly so the example an adopter copies is a live one.
- `tools/drift-audit/selftest.py` — S5's arms.
- `tools/drift-audit/README.md` — the layer's key list.

### Alternatives rejected

- **A conf key.** Rejected under S2 and the reasoning above.
- **Per-ratchet windows.** Rejected on SCOPE, and the premise the first draft rejected them on was
  false. It said nothing in this corpus has two pins whose justifications compete for one window;
  measured, `ORPHAN_ID_PIN` and `DEAD_PATH_PIN` sit three lines apart at the same value, both
  declared `weakens: "up"`, so either one's justification is inside the other's fourteen-line
  window. Unit 4 then makes the competing-window case the DEFAULT shape, with three keys at one
  value in one small file. The rejection still stands on scope — a per-key window is a bigger
  mechanism than this unit — but it can no longer stand on the claim that the case does not arise.
- **Search the whole comment block above the pin, unbounded.** Rejected: the window's purpose is
  that a justification for a DIFFERENT number, further up the same block, must not be mistaken for
  this one's. Unbounded is not a wider window, it is no window.

## 5. Production-readiness checklist

- security — N/A. An integer from a Python module the adopter already owns and the engine already
  imports.
- perf / scale — N/A. A slice bound.
- a11y · i18n — N/A.
- error / empty / loading states — S4 covers a declared-but-invalid value; an absent one is the
  default by design.
- observability — the message ALREADY names the window and interpolates the constant, so this unit
  inherits that for free rather than adding it. The first draft described the property as missing.
- risks — a narrowed window silently stops excusing justifications that used to pass, which reds
  rather than passes, so the failure direction is safe.
- testing + left-shift gates — S5's both-directions arms.
- migration / rollback — delete the declaration.
- user docs — S3 and the kit README.

## 6. Acceptance criteria

- **AC1** — When a fixture layer declares `RATCHET_LOOKBACK` small enough to exclude a
  justification, `python tools/drift-audit/selftest.py` observes the weakening reported; when it
  declares one large enough to include the same justification, the signal is silent.
- **AC2** — When a fixture layer declares nothing, `python tools/drift-audit/selftest.py` observes
  the shipped 14 applying: a justification 14 lines above the pin passes and one at 15 fails, over
  the same fixture.
- **AC3** — When a fixture layer declares a non-integer, `python tools/drift-audit/selftest.py`
  observes a named refusal naming the attribute, with no traceback. The observer is the selftest
  and not `--check`, because `load_project_layer` resolves `drift_signals.py` from the KIT DIR: a
  `--check` run in this tree can only ever load gov's own layer, so it cannot see a fixture.
- **AC4** — When `python tools/drift-audit/drift_report.py --check` runs on this repo with the layer
  declaring 14 explicitly, the signal set is byte-identical to its output before this unit.
- **AC5** — When a fixture layer declares a window OTHER than 14 and the ratchet fires, `python
  tools/drift-audit/selftest.py` observes the message naming THAT number. Stated differentially on
  purpose: the message already names 14 today, so an absolute form would be green before a line of
  this unit is written.

## 7. Gates

`python tools/drift-audit/selftest.py` · `python tools/drift-audit/drift_report.py --check` · `bash
tools/drift-audit/adopt-drift-audit.sh --check` · `python tools/codebase-map/test_codebase_map.py` ·
and `GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded spec-audit round 1.
- rev-3 · 2026-08-18 · folded spec-audit round 2. The per-ratchet-window rejection rested on a
  premise the corpus contradicts — two pins three lines apart already compete for one window — so
  it now rests on scope, which is the reason that survives. S1c states that unit 4's hook window is
  a separate number, which neither spec said and which an adopter narrowing one would discover the
  hard way. The motivating measurement was wrong — the margin
  was 8 lines, not 2 — and section 4 now carries the measured figure and the argument that does not
  rest on a near miss. Section 5 claimed the message lacks a property it already has, and AC5 was
  green before the unit started; both restated differentially. S1b names the call path, since the
  value is consumed two frames below where it is read. AC3's observer changed, because the layer
  loads from the kit dir and `--check` cannot see a fixture.

## 10. Reuse audit

Satisfied for the set by `TOOL-aDeclaredBound-4` §10. The seam this unit extends is
`load_project_layer` in `tools/drift-audit/drift_report.py`, which already imports the adopter's
`drift_signals.py` and validates four required attributes. This unit adds an OPTIONAL fifth read
through a defaulting accessor rather than a fifth required attribute, which is what keeps every
existing adopter layer valid. No new mechanism, no new file, no new conf.
