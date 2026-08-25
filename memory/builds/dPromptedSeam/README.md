---
slug: dPromptedSeam
node: d
opened: 2026-08-25
streams: tooling
roster: TOOL
ids: TOOL-dPromptedSeam-1 TOOL-dPromptedSeam-2 TOOL-dPromptedSeam-3
---

# dPromptedSeam — a refused name also answers "does this already exist"

## The problem this build exists to solve
The lexicon kit's stated failure mode is ABSENCE — someone who would have used your verb, or your
seam, had they known it existed. `--suggest fetch_conf` closes half of that: it answers which verb
the declaration wants. It says nothing about whether `load_conf` is already sitting there with a
fan-in of 16, which is the half that actually saves the work. The two facts are one keystroke apart
and live in two kits that do not speak. `read_object()` was written inside the lexicon precisely to
make `build_index` and `render_index` comparable as one concept, and today only `--brief` reads it.

## Expected improvements
- A refusal becomes the moment reuse is proposed — the author has not written the function yet.
- `read_object()` gains its second consumer, so its split is load-bearing rather than one verb's
  private helper.
- Measured on this corpus: object `conf` returns `load_conf` at fan-in 16, `index` returns
  `build_index`, `verbs` returns `leading_verb`. Three for three.

## Detriments if this is not built
- The kit keeps answering "call it `load`" while the thing called `load_conf` stays unfound, and the
  absence it was built to attack survives in the half nobody instrumented.
- `read_object()` stays a single-caller helper, which is the shape that gets deleted by a later
  reader who cannot see why it is separate.
- Every adopter re-discovers by hand that the naming answer and the reuse answer are the same
  question asked twice.

## Build-level rules
- THE LEXICON KIT STAYS SELF-CONTAINED. `subtokens.py` is a deliberate port rather than an import so
  the kit works for an adopter who never took `codebase-map`; a hard dependency here would undo the
  reason that port exists. Discovery is optional and absence is a normal outcome.
- THE HINT NEVER CHANGES A VERDICT. It cannot move an exit code, a pin, or a predicate. A reuse
  prompt that can fail a gate is a second naming authority, and this repo has a name for that.
- EVERY SKIP ANNOUNCES ITSELF. Map absent, object empty, lookup timed out, lookup refused — each
  says which, because a hint that silently is not there is indistinguishable from one that found
  nothing.

## Parked decisions
- The spec audit refuted rev-1's mechanism on three grounds and the goal was re-specced through the
  rendered Skill. What is NOT resolved is whether an instruction nobody is forced to read is enough:
  rev-2 trades an automatic trigger for a correct query and says so plainly rather than arguing the
  loss away. If the Skill step is measured to go unread, `-1` Q2 reopens.

<!-- gen:build-index -->
**Build status:** OPEN · 3 unit(s) · node d · opened 2026-08-25 · streams tooling
ids TOOL-dPromptedSeam-1 TOOL-dPromptedSeam-2 TOOL-dPromptedSeam-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dPromptedSeam-1 — a refused name carries a reuse prompt](spec/2026-08-25-spec-dPromptedSeam-1.md) | — | 1 | OPEN | rev-4 | 2026-08-25 |
| [TOOL-dPromptedSeam-2 — `read_object` cannot say WHY it returned nothing](spec/2026-08-25-spec-dPromptedSeam-2.md) | — | 1 | WONTDO | rev-4 | 2026-08-25 |
| [TOOL-dPromptedSeam-3 — `--brief` calls nine unrelated concepts one concept, out loud](spec/2026-08-25-spec-dPromptedSeam-3.md) | — | 1 | OPEN | rev-1 | 2026-08-25 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 2 record folder(s).

Ids no record names: TOOL-dPromptedSeam-3.

Ids no `spec-audit` record has ever named: TOOL-dPromptedSeam-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
