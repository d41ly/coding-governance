**Serves:** journal TOOL-dWitnessedBar-20

# TOOL-dWitnessedBar-20 — builder return 2 (run `wf_3119acf3-9ce`), committed 8f93133461be769b41b506188e02ab559036c02b

## Why

Built TOOL-dWitnessedBar-20 from its rev-5 spec. Every claim the spec makes about the current code held when probed against the tree, so there was no divergence to report. The work is one pass commit, 8f9313346. Its spec status is CLOSED, it carries the `Pass: TOOL-dWitnessedBar-20` trailer, and every path it touches was declared in the dispatch's write set or is the acceptance ledger.

## Summary

TOOL-dWitnessedBar-20 is built and committed: the legacy-homes list is now one ledger population keyed by conf and key (commit 8f93133461be769b41b506188e02ab559036c02b, base abf06676dfb430ec05e00414258f70121fca93a2). Every criterion is either observed by a probe here or listed below as owed to the close.

**What changed:**
- **The list:** `tools/policy/legacy-homes.txt` moved by `git mv` to `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/project/legacy-homes.txt`. It was rewritten through the factory's `write_rows` into the ledger grammar: the 114 keys the list held at the run's base 9e21ac76, each row with count 1, that base sha and `seeded`. (DERIVED from the builder's probe)
- **The registration:** one `[[ledger]]` table in `tools/govkit/registry.toml`. The `policy fixtures` guard gains the list's home, `legacy_ledger.py` and `coverage_join.py`, and `tools/gate-legs.json` was re-rendered.
- **`tools/policy/policy.py`:**
  - New `load_ledger` and `read_legacy_registration` reach the memory-tree copy of the factory and read the registration.
  - `check_legacy_graded` now needs a `source` census, a registration and a file at its home, with the census asked first.
  - `check_legacy_homes` and `write_legacy_homes` grade and write through the factory.
  - `lists --derive` and `lists --marks` were added (`cmd_derive_list`).
  - `read_base_pairs` and `LEGACY_HEADER` were deleted, and `LEGACY_WITHHELD` no longer mentions an `ORDER [project-owned]` row.
- **Rules and wiring:** the `project-owned` rule in `tools/policy/kit.toml` and the three govkit ignore patterns are deleted. `PROJECT_REGISTRY_EXTRA` and `.gitattributes` (`merge=rows`) gain the list.
- **`tools/policy/check_policy.py`:**
  - Each `legacy-homes` scratch tree now holds gov's registry and the factory, and its list is written by the factory's `seed`.
  - New cases `widened` and `drain-merge`.
  - `legacy-homes-present`, `legacy-homes-withheld-install` and `census-source-receipt` are re-pointed as the spec says.
- **Records and generated files:** the README, `help/policy.md`, the kickoff manifest re-stamp, `symbols.json` from `gen_map.py --write`, the build index, and the acceptance ledger at `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-20-1-acceptance-ledger.md`.

**Choices the spec left open** (each recorded as a `Decided:` trailer):
- A typed row no home holds gets a `gained` line next to its unmeasured-row line, because the new-home remedy text would be false for it.
- `--write` also refuses while the list holds a malformed row, since the writer would silently drop it.
- `legacy-homes-present` reads gov's registry with `tomllib`. Reading it through `read_registrations` would open every tracked `kit.toml`, and `tools/loop/kit.toml` is under no `policy fixtures` guard, so the guard trace would go red.
- `drain-merge` drains two adjacent list rows that come from two different files, so the edits to those files cannot conflict and only the list can.

**Checks that ran** (none is a gate):
- The naming lexicon `--suggest` admitted `load_ledger`, `read_legacy_registration` and `cmd_derive_list`. It refuses `--as cli.flag`, so the two new flags were not graded.
- The generators `leg_factory.py --write`, `gen_map.py --write` and `gen_build_index.py --write`.
- `policy.py lists --check` on the tree is green with 114 rows; with no list at the base it prints one note instead. This stands in for the `policy check` leg. (DERIVED from the builder's probe)
- AC1, AC2 and AC3 by `grep`/`awk`/`diff` on the tree; `--derive other` and a bare `--marks` exit 2.
- AC8 by `tools/lib/legacy_ledger.py read legacy-homes`, exit 0.
- AC9's attribute by `git check-attr`. AC10's `git ls-files` and greps.
- `arm_legacy_homes` probed in-process over gov's tree: 114 rows and no finding. (DERIVED from the builder's probe)
- `python` probes of `build_legacy_repo` over scratch repos under `%TEMP%` for planted-row, growth, widened, shrink, retrofit, unmarked (with `--marks`), withheld, absent-homes and main-dropped. Each gave the exit code and reports the cases expect. These stand in for the `policy fixtures` leg's `legacy-homes` and `legacy-homes-main-dropped` cases.
- `drain-merge` was seen RED with the merge driver unset (exit 1, content conflict) and GREEN with it set (both rows gone, `lists --check` green).
- AC11's logic probed over a scratch tree: graded is True beside the source-mode receipt, False beside the adopter receipt, and False before the home is written.
- The `legacy-homes-present` logic probed: one registration, its home a file, no list left in the kit.
- `gotchas.py --for-diff HEAD~1..HEAD` ran. I acted on the move-inventory, message-edit and row-shape-docs classes by sweeping with `git grep`; no stale reader or wording remains, so nothing more needed changing.

**Owed to the close:**
- Every §7 leg.
- The `--fixture` runs AC4 to AC7 and AC9 to AC11 name: `legacy-homes`, `legacy-homes-present`, `legacy-homes-withheld-install` and `census-source-receipt`.
- The RED-first observation of the `New arm:` line on `tools/policy/check_policy.py` (cases growth, planted-row, shrink, unmarked and drain-merge, covering AC4, AC5, AC6, AC7 and AC9).
- The kickoff manifest check, which I did not run.

**Skipped or timed out:** one README edit hung because a stray `cat` in the command waited on input. I killed it, the edit then applied, and I checked that it added no control bytes; nothing was re-run. Nothing else hit its time bound, and the scratch repos under `%TEMP%/p20` have been removed.
