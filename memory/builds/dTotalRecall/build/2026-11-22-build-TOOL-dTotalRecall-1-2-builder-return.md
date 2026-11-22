**Serves:** research TOOL-dTotalRecall-1

# TOOL-dTotalRecall-1 build pass 2 — the builder's return

The gov-builder return of `unattended-unit.js` run `wf_2c520d14-677`, at base `d6de992c6`, pass commit `360b653fd`, saved verbatim.

## why

TOOL-dTotalRecall-1 is built at rev-7 and committed as one pass commit, 360b653fd. It carries the trailers `Pass: TOOL-dTotalRecall-1` and `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. The second line is the charter's spelling, which outranks the session's attribution reminder. In the same commit the spec's status is CLOSED, dated 2026-11-22. The F8 fix holds: each typed row grades only the paths `build_records.py#derive_record_name` matches. Every claim the spec makes about current code still held at d6de992c6, so nothing is returned as a divergence. One tension inside the spec is resolved and recorded under `Decided:`: AC10 needs `--check` to exit 0 after `new` alone, but §5 says `new` writes one tracked file. I made `new` re-render the HYGIENE view along with the row, so it writes two files, and that departure's deviation record is still owed.

## summary

TOOL-dTotalRecall-1 is built and committed (360b653fd on branch/unattended-dtotalrecall-ae256e, base d6de992c6). No gate, suite or bar ran. Several criteria and both new arms' RED-first observations are owed to the close, listed below.

**What landed.**
- `tools/memory-tree/record-kinds.toml`: 25 rows (generated from pass 1's script).
- `tools/memory-tree/record_kinds.py`: pass 1's draft plus four changes:
  - the F8 population rule, where a typed row grades only its own grammar's paths and the untyped rows take the rest;
  - the fixture's `…-deviation-notes.md` record;
  - `new` re-rendering the view;
  - the helper renamed to `remove_read_only`.
- The `gen:record-kinds` region and its section in `tools/memory-tree/HYGIENE.template.md`, rendered into `memory/HYGIENE.md` by `adopt-memory-tree.sh --render`.
- `[[ledger]] record-kinds-legacy` and the `record-kinds` `[[exempt_leg]]` row in `tools/govkit/registry.toml`. The exempt row was written by `leg_factory.py new --exempt` with ceiling 120, which also re-rendered `tools/gate-legs.json`.
- `memory/project/record-kinds-legacy.txt`: 11135 rows, seeded by `tools/lib/legacy_ledger.py seed` before this pass's own ledger was written.
- The `kind.record-kind` row of `tools/playbook/kinds.toml` now names its population, factory and gate, with owner dTotalRecall. Its pending row in `core-pending.txt` is deleted.
- The `gap-key` native row, the `record-kind-schema` class row, and a section in `tools/memory-tree/README.md`.
- Re-rendered by their own writers: `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt` (node d, 1.6s, `--observed`), `help/reference/kinds.md`, and the map files under `memory/map/generated/`.
- `memory/map/features/memory-tree-hygiene.md` now claims the leg.
- `.memory-tree.conf`'s `PROJECT_REGISTRY_EXTRA` gains the ledger's home, and the `SESSION-KICKOFF.md` manifest is re-stamped at d6de992c6.
- `gen_build_index.py --write` re-rendered `LIVE.md`, `backlog/TOOL.md` and the build README.
- The acceptance ledger is `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-1-2-acceptance-ledger.md`.

**Checks that ran.** These were fixtures and probes of this unit's own code. Each stands in for the `record-kinds` leg and its `--selftest` unless noted.
- **Fixture plants:** `record_kinds.py --fixture` with no plant, and with each of the eight plants. The six expected to fail exited 1 naming their subject; no plant and `field-missing-legacy` exited 0 (AC2, AC5 first half, AC7, AC8 first half, AC9, AC11).
- **Real tree:** `record_kinds.py --check` exited 0 in about 1.0 to 1.6s. It showed `deviation 0 graded 2340 legacy` and printed the `probe` and `acceptance` "unarmed — no record yet" lines (AC1 and AC8 before the commit). This is the new leg's own command, run as a probe of new code.
- **Other CLI verbs:** `--template deviation` (AC6) and `--print-gap-keys` (AC9).
- **`python -c` probes:**
  - the `enforces`/`binds` match and `core.py#check_kind_row` returning no red (AC1);
  - `new` in a `%TEMP%` fixture, which exited 2 without `--writer` and wrote nothing, then exited 0 with a green check (AC10);
  - the two HYGIENE regions equal byte for byte (AC5);
  - `read_kind_schema_members` over an empty directory returning `set()`.
- **Step gate:** `step_gate.py --list` printed `record-kind-schema · 88 members`, matching the `tomllib` count (AC4).
- **Naming:** every helper name passed the naming lexicon's `--suggest --as py.function`.

**Owed to the close.**
- AC1 at the pass tip.
- AC3: `step_gate.py --fixture --plant record-kind-schema`, with and without `--with-row`.
- AC5's `kit/dogfood doc parity` leg.
- Both `New arm:` RED-first observations:
  - the `record-kinds` leg and its `--selftest`, staged by deleting one row's `writer`;
  - the step gate's plant.
- All of section 7's legs.
- Possible meta-gate reds from the new leg, and the `kit epoch` leg for the memory-tree and playbook kits, whose shipped bytes moved without a version bump.

**Skipped or not done.**
- **Timed-out dispatch:** the second `--dispatch` (the three generated map files plus a deviation record path) timed out at 100s and was not re-run. The map files went in as generated renders. The deviation record for `new` writing two files (§5 says one) was not written. It is named in the commit's `Decided:` lines and is owed.
- **Pipe-escape edit refused:** after the gotchas checklist, the scratch-guard hook refused a one-line edit to `record_kinds.py` because the unit is now CLOSED. The edit would escape a `|` in view cells (class pipe-in-a-code-span-splits-a-table-cell). No current row holds a pipe, so the view is correct today. It is a follow-up.
- **Dossier over budget:** the pre-commit hook printed a warning only: `memory-tree-hygiene.md` is 21286 bytes against its 20480 budget.
- **Gotchas run:** `gotchas.py --for-diff HEAD~1..HEAD` selected 45 classes. Apart from the pipe escape, the relevant ones (fixture-finds-nothing, new-leg meta-gates, idempotent append, empty field, record without Serves) checked clean.
- **Untracked files:** the two TOOL-dTotalRecall-8 prompt files in `prompts/` are not mine and are left untracked.
