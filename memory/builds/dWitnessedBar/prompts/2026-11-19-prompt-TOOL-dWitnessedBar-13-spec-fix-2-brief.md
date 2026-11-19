**Serves:** journal TOOL-dWitnessedBar-13

# Brief — dWitnessedBar: TOOL-dWitnessedBar-13 re-grounded on the tree as built, before dispatch

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
   - Built: unit 26 (`7526c98fa`, the `resolve_bash_py` block `scan_bash` / `scanBash`, `scan_bare_bash` in
     `tools/run-gates/measure_legs.py`, section `2j`); unit 27 (`cc35bb62c`, `tools/lib/refuse-wrong-shell.sh` and the
     refusal in every `resolve_python` member, section `2n`); unit 48 (`75a15d9ce`, row_grammar's resolver an adapter,
     `scan_bare_bash` shape 2 widened). Unit 49 (`ef33493d7`, shape 4 of `scan_bare_bash`: a PATH lookup of `bash`). Unit 13 (rev-3) is building now.
   - Queued from re-grounded specs, each the contract for what will exist: unit 13 (rev-3, building now: `tools/lib/legacy_ledger.py`,
     parity row `legacy_ledger_py`, section `2o`), unit 50 (rev-4), unit 15 (rev-8: `test.seed` at every check's
     registration, `retrofit.unseeded` read through `policy.py get`), unit 12 (rev-6: the `leg`, `check` and `pack` tag
     namespaces, a `tag` on every leg, `LEG_KEYS` gaining `tag`, check rows as `[[numbered_check]]` tables, the policy
     kit's owner segment `policy-kit`), unit 61 (rev-3). Sections `2j` to `2o` of `tools/lib/resolve-python.test.sh` are
     taken; a spec citing unit 13's section as `2l` cites `2o`.
   - Also queued from re-grounded specs: unit 22 (rev-4: `tests` edge field on legs, `read_leg_edges` wired into
     `edge_grammar.py#read_tree_edges`), unit 47 (rev-6), unit 19 (rev-4: the leg's `purpose` field).
2. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.
3. Unit 13's first builder (run `wf_62b9efd5-0fc`) stopped at a divergence before writing any code; its return is
   `build/2026-11-19-build-TOOL-dWitnessedBar-13-1-builder-return.md`. Read it whole and settle all six points in one
   revision: (1) `compare <population>` has no stated source for its measured counts — name it, sharing or deferring to
   the seed-run contract units 15 and 51 own rather than designing their part here; (2) AC1's invocation contradicts S10
   and AC9; (3) how `read_registrations` finds the tool root at a fixture or an adopter with no govkit registry;
   (4) `compare_to_base` must re-key base rows through the `<base>..HEAD` renames before judging the direction, or AC4
   fails; (5) whether `carry` / `write_rows` runs unit 15's home-admission test here, so sections 4 and 5 agree; (6) the
   merge class's other postconditions run with the ledger row predicate and key, or `no_row_loss` refuses every ledger
   merge. A choice among these the spec cannot derive is a fork for item 2.
Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-13` and
`python tools/check-spec-tokens.py --spec <path>` over each spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for every spec; each spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-13. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

Each status header keeps its status. The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-13.md` alone.

### Reuse

Each spec's §10 seam, re-verified at HEAD.
