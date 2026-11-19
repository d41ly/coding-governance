**Serves:** journal TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49

# Brief — dWitnessedBar: TOOL-dWitnessedBar-48, TOOL-dWitnessedBar-49 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The run's first two builders each stopped at a divergence, because the
specs were written at `cdfbd1cf` and the tree has moved since; each spec is now re-grounded before its dispatch.

## The brief

### Goal

Revise each spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read each spec whole against the code at HEAD and settle every claim the landed code has moved: every path,
   symbol, line citation, section name, count, population and edge. Re-derive each PINNED count with the command the
   spec states and re-pin it with today's date. A population the spec enumerates is re-derived, every new member listed
   in Files touched with the legs its guard names on the gates section's leg line, and a prose-only mention named as
   outside the population. Cite moved lines as `path#symbol` or blob-pinned, never a bare `path:line`.
   What is built so far:
   - Unit 26 (`7526c98fa`): the `resolve_bash_py` block in `tools/lib/resolve_bash.py` is `scan_bash(script, host)`
     returning `(found, tried, refusal)` with `BASH_NAMES`; its twin `scanBash` is in `tools/lib/resolve_bash.js`; both
     are inlined behind name-keeping adapters in every site; govkit's `resolve_shell_argv` raises `Refusal`;
     `scan_bare_bash` in `tools/run-gates/measure_legs.py` widens `test_no_bare_bash_argv`; section `2j` of
     `tools/lib/resolve-python.test.sh` is the resolver truth table, with a `resolve_bash_js` parity row.
   - Nothing else of this build is built. Unit 27 (order 2) is re-ground first; units 48 and 49 build after it.
2. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49` and
`python tools/check-spec-tokens.py --spec <path>` over each spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for every spec; each spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-48, TOOL-dWitnessedBar-49. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

Each status header keeps its status. The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-48.md`, `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-49.md` alone.

### Reuse

Each spec's §10 seam, re-verified at HEAD.
