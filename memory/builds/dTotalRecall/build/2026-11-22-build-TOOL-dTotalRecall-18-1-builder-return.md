**Serves:** research TOOL-dTotalRecall-18

# TOOL-dTotalRecall-18 build pass 1 — the builder's return

The gov-builder return of `unattended-unit.js` run `wf_22e6d4f6-8d5`, at base `c344bdc40`, pass commit `305b6e9d1`, saved in substance.

## why

TOOL-dTotalRecall-18 is built as spec rev-7 says and committed in one pass commit: subject names the unit, trailers `Pass: TOOL-dTotalRecall-18` and `Co-Authored-By: Claude Opus 5`, and the spec header is set to CLOSED in the same commit. I checked the spec against the tree before the first edit and every claim held at base: the 46c806b6a pins, the rename's sites, READ_KEYS, WRITE_FOLDERS, load_roles, derive_record_ref, read_definition, read_item_rows, DOOR_KINDS, check_one_door, load_memory_tree_path, the [[retired]] grammar and the common-dir listing. The F3 probe found no new `journal` reader. Nothing diverged, so I return no divergence.

## summary

Built and committed as 305b6e9d1 on base c344bdc40. No gate, suite or bar ran. The only lexicon commands were `--suggest` and `--measure`.

**What changed**
- **Registry** (`tools/memory-tree/record-kinds.toml`): now 46 rows. `home`, `lifecycle`, `readers`/`readers-none` and `layer` are filled on every row; the four empty homes are filled; the five kinds of S5 and the 16 pocket rows are added; `journal` is renamed `log`. (DERIVED, the builder's own run)
- **`tools/memory-tree/record_kinds.py`:**
  - the four columns are now required and graded, and readers are checked against the roles;
  - the view has seven columns, with Read by and Written by re-read from the roles and loop kits each time, and `unarmed` where a kit is missing;
  - `|` is escaped in cells;
  - `check_pockets` and `GIT_OWN` are added, using an inline `common_git_dir` copy;
  - `resolve_kit_dir` is carried inline;
  - `check_serves_aliases` holds runlog's `SERVES_ALIASES` to `KIND_ALIASES`;
  - `new` gains `--layer`, `--lifecycle`, `--reader` and `--readers-none`;
  - the legacy ledger is read through `resolve_kind`, and the nine new plants are added.
- **The rename:**
  - `tree_lib.py` gets `KIND_ALIASES` and `resolve_kind`, and `read_bindings` accepts the alias.
  - Writers now write `log`: `tools/runlog/record.py`, `tools/roles/handoff.py`, `tools/loop/upstream.py`, `tools/memory-tree/migrate_backlog.py` and `tools/unattended/unattended.sh`.
  - Readers resolve the alias: `tools/memory-tree/deviation_join.py`, `tools/memory-tree/seen_red.py`, check 23's awk and `derive_chain_verdict`.
  - Fixtures and prose are updated, and `memory/HYGIENE.md` and `help/reference/kinds.md` were re-rendered.
- **Doors:** `writing_practice.py` drops the four record door kinds and prints each registry row's writer as its door. A `doors.toml` row naming a record kind now reds. `doors.toml` loses those rows.
- **Other files:** the `roles` and `loop` `requires_if` rows in `tools/memory-tree/kit.toml`; the `[[retired]]` row for `record-kind-schema:journal.Serves` in `tools/govkit/registry.toml`; `VERB_OFFENDER_PIN` in `.lexicon.conf` re-measured 1444 to 1445 (one arrived: the inline `common_git_dir` copy); `last-audit` in `memory/guides/SESSION-KICKOFF.md` re-stamped; the acceptance ledger.
- **Generated files:** `memory/map/generated/symbols.json`, `memory/LIVE.md`, `memory/backlog/TOOL.md` and `memory/builds/dTotalRecall/README.md` were regenerated. Only my hunks of the README were staged: its rows for units 4, 38 and 54 come from another writer's uncommitted specs.

**Checks run (each stands in for a gate)**
- **`record_kinds.py --fixture`** green, plus each new plant, standing in for the `record-kinds` leg and its selftest arm. As expected, these exited 1: `lifecycle-missing`, `role-reads-moved`, `roles-unresolved`, `pocket-stray`, `alias-drift`. These exited 0: `item-inputs`, `pocket-registered`, `new-row`, `pipe-cell` (AC1, AC2, AC4, AC8–AC10, AC12).
- **`writing_practice.py --fixture`:** `--plant door-in-registry` exited 1 and `--plant none` exited 0. Stands in for `writing practice (records and units)` (AC3).
- **`python -c` probes** of `check_row`, `check_readers`, `check_pockets` and `check_serves_aliases` over the worktree: no row reds; the legacy `log` count is 3924, matching the `cut | grep -cx journal` count; the only unmatched pocket is `dHomedResolver` (AC1, AC4).
- **Scratch-tree probes:** `read_bindings` (AC6) and `check_serves_line` (AC12).
- **AC7:** the `git grep` hits are only in readers' fixtures.
- **AC8 and AC11:** `tomllib` probes of `kit.toml` and `registry.toml`, plus `read_retired` and `read_kind_schema_members`.
- **AC9:** `new` without `--layer` on the worktree exited 2 and wrote nothing.

**Owed to the close**
- `record_kinds.py --check` (AC1/AC4). It reds on the real tree until the stray `dHomedResolver/` in the common git dir is moved out, as F2 says.
- `check-memory-hygiene.sh --only 23` through `memory-hygiene self-test` (AC5).
- Legs: `step-gate` (AC11), `runlog selftest` and `runlog record schema` (AC12), `python resolver (behaviour + inline parity + idiom ban)` for the two inline blocks, `docs` and `kit/dogfood doc parity`, and the remaining section 7 gates.
- The `record-kinds` row in `tools/run-gates/ceiling-evidence.txt` was not re-timed, because that needs the leg to run. The leg now reads the roles, items and common dir. The `ceiling` in `tools/govkit/registry.toml` and `tools/gate-legs.json` (via `leg_factory.py --write`) only need to change if that evidence calls for a higher one.
- **RED-first observations for the three new arms:**
  - `record_kinds.py --selftest` plants, broken by clearing one row's `home`;
  - the `ARCH-tFixture-150`/`151` arms in `check-memory-hygiene.test.sh`, broken by making check 23's awk match `journal` only;
  - the `door-in-registry` plant in `writing_practice.py`, broken by restoring the `deviation` row with no red.

**Skipped:** `unattended.sh --dispatch ... --writes` for a deviation record (`...-18-deviation-183.md`) hit its 110 s timeout and was not re-run. So no deviation record was written; the choice to let `home` be a list of globs is recorded as a `Decided:` trailer instead. (DERIVED, the builder's own run)

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` ran over the commit. I checked the rename for stranded readers (none outside the spec's table), the test lines matching the edited check 23 messages (all updated), and the pipe escape. One gap I left: the refusal branches for the `home` and `readers` grammar have no plant of their own (refusal-branch-with-no-arm).
