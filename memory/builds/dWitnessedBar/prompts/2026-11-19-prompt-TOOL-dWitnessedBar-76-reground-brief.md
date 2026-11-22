**Serves:** journal TOOL-dWitnessedBar-76

# Brief — dWitnessedBar: TOOL-dWitnessedBar-76 re-grounded on the tree as built, before dispatch

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
   outside the population. Cite moved code-file lines as `path#symbol` or blob-pinned, never a bare `path:line`; leave a carried clause token byte-identical.
   What is built so far:
   - Built and landed through order 40's third unit: every unit up to and including 4, 25, 40, 23, 42, 3, 44, 5, 41,
     55, 8, 1, 59, 30, 29, 7, 21, 6, 2, 43, 51, 56, 57, 58, 60, 62, 63, 64, 65, 66, 69, 68, 67 (`af84e1a7a`), 70
     (`0890c99d1`), 71 (`2972b3755`: `run_planted_git` in the resolver suite), 72 (`fa536b7cd`: the canary's `rgf_mr`
     measures `rec_fp` beside `rec_sha`) and 74 (`6a12d559c`: `check_cr_reached <file> <record> <var>` is a top-level
     function in the gov suite, with a `${_rg_v%?}` liveness variant seen red on every run). Unit 75 (order 40) is
     being re-grounded alongside this spec and builds before order 41. Every unit this spec consumes from is CLOSED.
   - Unit 28 is NOT built: it waits on three dOrderedCharter changes (asks TOOL-dWitnessedBar-101 to -103) and the run
     defers it; any item of this spec that needs it leaves the scope, named in §3 as waiting with unit 28.
   - Order 41 is units 73, 76, 77, 79, 80 and 81; 77 consumes 75 and 76, and 79, 80 and 81 consume 76. Units 73 and
     76 are re-grounded side by side now; list Files touched exactly, so the run can tell which order-41 units share
     a file and must build one at a time.
   - A bash fact on this node: bash 5.3.9 (cygwin) turns a `$'\r'` written inside `$(...)` into an empty string, so a
     CR test inside a subshell uses a variable set outside it, or a function body defined at the top level.
   - Suite floors at HEAD: read each from its suite file, never from this spec. A suite that grows past its
     `memory/project/shell-role.txt` row is widened in the pass that grows it, by `ratchet.py widen`, never by hand.
   - Settle every claim about the landed shape of each unit this spec consumes from against the tree, reading each
     unit's committed builder return under `memory/builds/dWitnessedBar/build/` where the spec relies on what it built.
2. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.
3. A `[[ledger]]` home spelled under `tools/<kit>/` reds `install-prefix (shipped surface)`; keep every home under
   `memory/project/`. Blob-pin code-file line citations only at a commit HEAD holds. A spec over its ceiling of
   49152 B (PINNED 2026-11-20 by the spec size check) is tightened in prose you touch, never by dropping a criterion.
4. Name every new function the spec introduces with a verb from `.lexicon.conf`'s VERBS table, nested helpers
   included: the lexicon leg grades them.
Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-76` and
`python tools/check-spec-tokens.py --spec <path>` over each spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for every spec; each spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-76. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

Each status header keeps its status. The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-76.md` alone.

### Reuse

Each spec's §10 seam, re-verified at HEAD.
