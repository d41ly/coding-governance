# Build brief — TOOL-aBriskPreflight-1: check-wiring's per-item loops become one batched call per arm

**Serves:** research TOOL-aBriskPreflight-1

Build the unit its spec, `spec/2026-10-11-spec-TOOL-aBriskPreflight-1.md`, describes, in
`tools/check-wiring.sh`, and nothing else. The spec is the design; the baseline record
(`build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md`) carries the measured cost of each site.
This run sequences its unit passes one at a time, inline, because two passes committing at once in
one worktree race one git index; no sibling pass runs while you build.

## How to work in this tree — each line is a lesson a previous pass paid for

- **The spec is committed already.** Write the code in a later commit; never spec and code in one.
- **Declare before you write**, with `--dispatch` per the harness prompt. Declare EVERY path your
  commit will carry: the product file, `memory/builds/aBriskPreflight/README.md`, `memory/LIVE.md`,
  `memory/ledger/2026-10.md`, `memory/map/generated/symbols.json`, and any test or record file you
  add. The pre-commit hook re-renders the generated views; an undeclared one counts against a
  shrink-only ceiling with no repair.
- **Stage your declared paths AND `memory/builds/aBriskPreflight/RUN.md`** in the pass commit: the
  `--dispatch` and `--brief` rows live there and the `brief-recorded` leg reads them AT the build commit.
- **Name a new function** with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`
  first. After adding or renaming any function, run `python tools/codebase-map/gen_map.py --write`
  and commit the regenerated `symbols.json` with the code.
- **No suite, no bar.** Verify through a SLICED arm: the suite's prologue plus the one block you need,
  in a temporary script placed INSIDE `tools/` (the prologue resolves the checker from its own
  directory), run alone, then DELETED before `gen_map.py --write` (that generator reads untracked
  files, and a slice left behind lands its symbols in the map). Never run `check-wiring.test.sh` whole.
- **Equivalence on one tree**: run `bash tools/check-wiring.sh --check` from the committed BASE copy
  (`git show <base>:tools/check-wiring.sh > <scratch>/cw-base.sh`, run from the repo root) and from
  your edited copy, and compare the two outputs byte for byte; `--fix` and `--session` too, in a
  throwaway clone under `%TEMP%/<short>` so nothing in this tree is rewritten.
- **Spawn count**: trace with the build's instrument, `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh`,
  analyze with `…-trace-spawns.py`, before and after, and put the four numbers in the commit message.
  This host's spawn cost is 0.7 to 1.1 s, so a traced run of the old checker takes about ten minutes:
  run it in the background and do other work.
- **Do not bump `KIT_CHECK_WIRING_VERSION`**: the main loop bumps each kit once, after its last move.
- **Never kill a process you did not start.** The host is shared.
- Out of scope, per the spec: `$(first_of …)` and `$(resolve_receipt_path …)` (aSparedSpawn-8), and
  everything unit 2 owns (`json_str`, `matchers_of`, `settings_json`, the python resolution).
