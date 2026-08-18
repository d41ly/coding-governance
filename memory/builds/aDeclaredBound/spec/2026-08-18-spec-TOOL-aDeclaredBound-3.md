# TOOL-aDeclaredBound-3 — the ratchet lookback becomes a project-layer declaration

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

`_RATCHET_LOOKBACK = 14` decides how many lines above a pin drift-audit will look for the
justification that excuses a weakening move. It is a module constant in the kit engine. Move it to
drift-audit's PROJECT LAYER, which is the seam this kit already declares for per-adopter values.

## 2. Scope (IN)

- **S1** — `drift_signals.py` may declare `RATCHET_LOOKBACK`. The engine reads it with a defaulting
  accessor, so an adopter's layer that predates the key keeps 14 and does not fail to import.
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

The window is not a style preference. `TOOL-aLoosenedCeiling-3` wrote a six-paragraph justification
above a raised ceiling and came within two lines of pushing the required `<old> -> <new>` literal
out of the window — at which point the gate would have reported an unjustified weakening over a
justification that was right there. A repo whose comment convention is denser than this one needs a
wider window, and a repo with terse pins might want a narrower one so a justification for a
DIFFERENT pin cannot be read as this one's.

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
- **Per-ratchet windows.** Rejected as unrequested and speculative: nothing in this corpus has two
  pins whose justifications compete for one window, and the shape can be added later without
  changing the single-number form into a wrong one.
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
- observability — the ratchet's failure message already quotes the required `<old> -> <new>` form;
  it should also say how far it looked, or an operator whose justification sits just outside the
  window is told to write text they already wrote.
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
- **AC3** — When a fixture layer declares a non-integer, `python tools/drift-audit/drift_report.py
  --check` prints a named refusal naming the attribute and does not raise.
- **AC4** — When `python tools/drift-audit/drift_report.py --check` runs on this repo with the layer
  declaring 14 explicitly, the signal set is byte-identical to its output before this unit.
- **AC5** — When the ratchet fires, the text `python tools/drift-audit/drift_report.py --check`
  prints states the window it searched, so an operator whose justification sits just outside it is
  not told to write a sentence they already wrote.

## 7. Gates

`python tools/drift-audit/selftest.py` · `python tools/drift-audit/drift_report.py --check` · `bash
tools/drift-audit/adopt-drift-audit.sh --check` · `python tools/codebase-map/test_codebase_map.py` ·
and `GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.

## 10. Reuse audit

Satisfied for the set by `TOOL-aDeclaredBound-4` §10. The seam this unit extends is
`load_project_layer` in `tools/drift-audit/drift_report.py`, which already imports the adopter's
`drift_signals.py` and validates four required attributes. This unit adds an OPTIONAL fifth read
through a defaulting accessor rather than a fifth required attribute, which is what keeps every
existing adopter layer valid. No new mechanism, no new file, no new conf.
