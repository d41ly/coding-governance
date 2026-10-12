# Build brief — TOOL-aBriskPreflight-2: check-wiring reads the settings file and each fragment once, and resolves python once

**Serves:** research TOOL-aBriskPreflight-2

Build the unit its spec, `spec/2026-10-11-spec-TOOL-aBriskPreflight-2.md`, describes, in
`tools/check-wiring.sh`, `tools/check-wiring.test.sh` and the regenerated `symbols.json`, and nothing
else. This run sequences its unit passes one at a time, inline, because two passes committing at once
in one worktree race one git index; no sibling pass runs while you build.

## The tree you start from

- TOOL-aBriskPreflight-1 is CLOSED at `4421bf650` in the same file: the eol population through one
  `git check-attr --stdin`, the smoke's per-id counts in one `awk`, the audit-line reads in one tagged
  `sed`, and the family harvest in one `sed` per chunk. Every line number in your spec is at BASE
  `b726385f`: re-locate each site in the current tree. Its result record,
  `build/2026-10-11-build-TOOL-aBriskPreflight-1-spawns-ab.md`, carries the after-unit-1 spawn count
  (333 forks, 246 execs), which is THIS unit's "before"; trace the "after" once with the same
  instrument (`build/…-1-run-traced.sh` and `…-1-trace-spawns.py`), with the host's spawn cost beside it.
- The run branch merged `origin/main` at `976a85a25`; under `tools/` that merge differs from main by
  unit 1 alone. `KIT_CHECK_WIRING_VERSION` reads 1.31 now, main's bump; do not touch it.
- Unit 1's pass found that `tools/gate-lint/sh_hygiene.py` refuses a loop fed by a here-document or
  here-string over a variable a command substitution filled, and that its registry row for this file
  (`tools/check-wiring.sh EOF 3`) can only shrink. Feed every new loop some other way, and run the
  leg's predicate over your file before committing (`sh_hygiene.scan_file`, as unit 5's pass did).

## How to work in this tree — each line is a lesson a previous pass paid for

- **The spec is committed already.** If you must diverge, rev the spec first in its own commit
  (`Pass: none`), then the code in a later one.
- **Declare before you write**, with `--dispatch` per the harness prompt: the product files, the
  test, `memory/builds/aBriskPreflight/README.md`, `memory/LIVE.md`, `memory/ledger/2026-10.md`,
  `memory/map/generated/symbols.json`, and any record you add.
- **Stage your declared paths AND `memory/builds/aBriskPreflight/RUN.md`** in the pass commit.
- **Name every new function** with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`
  first. After adding or renaming one, run `python tools/codebase-map/gen_map.py --write`.
- **The two inline copies between the `resolve_python` and `resolve_kit_dir` markers are gated
  byte-identical**: memoize around them, never inside.
- **No suite, no bar.** Verify through SLICED arms of `check-wiring.test.sh` in temporary scripts
  inside `tools/`, run alone, then DELETED before `gen_map.py --write`. Equivalence and `--fix` /
  `--session` runs go in a throwaway clone under `%TEMP%/<short>`; unit 1's pass used `%TEMP%/bp1r`.
- **The `skill` arm reds in a clone** because this machine's installed kickoff engine follows the
  primary checkout; that is not this unit's, and both arms of any comparison see it alike.
- **Never kill a process you did not start.** The host is shared.
- Out of scope, per the spec: `$(first_of …)` and `$(resolve_receipt_path …)` (aSparedSpawn-8).
