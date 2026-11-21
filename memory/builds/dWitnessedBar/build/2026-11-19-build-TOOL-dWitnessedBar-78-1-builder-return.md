**Serves:** journal TOOL-dWitnessedBar-78

# TOOL-dWitnessedBar-78 — builder return 1 (run `wf_01c7ef60-ba2`), committed 253e21771

## Why

Every claim the spec makes about current code still held at the base (read_bar_file's IFS split, the inherited green's ten awk reads, the guard in registry.toml, the four DEFERRED specs, the landed verdict_backends open, section 2o's two assertions, the 35 GIT_CONFIG_COUNT lines). So TOOL-dWitnessedBar-78 was built as written and committed with its spec set to CLOSED. The orientation card said the unit was Tier-2 DEFERRED, but the spec already read INPROGRESS at base 1ab2e0605. No divergence.

## Summary

Built TOOL-dWitnessedBar-78 in commit 253e21771, on top of 1ab2e0605. It has the `Pass: TOOL-dWitnessedBar-78` trailer and sets the spec header to CLOSED. No gate, suite or bar ran.

**What changed:**
- **`.githooks/pre-push` (S7, S8):** `read_bar_file` now reads with `read_green_file`'s rules: the whole line is read, an unterminated last line included; the key is split at the first TAB; one CR is stripped; the last repeated key wins. It uses `_rb_` locals and one `<key>) bg_<name>=` per case line, and gains `bg_age` and `bg_blocks`. A new `read_inherited_green` replaces the inherited green's ten awk reads, with every `bg_*` declared local. `check_bar_base`'s local list names the two new variables.
- **Gov canary guard (S6):** `tools/govkit/registry.toml` gains `{prefix}/` in the gov canary guard, and `tools/gate-legs.json` was re-rendered with `leg_factory.py --write`.
- **Gov suite (S7, S13):** `tools/run-gates/run-gates.gov.test.sh` gains two assertions: `read_bar_file`'s every-key record, which also checks that `base`, `max_age` and `blocks` are derived, and the line-rule record read by both readers.
- **Ask rows (S9):** PLAY-dConvergedCharter-42, TOOL-dPlacedRequest-74 and TOOL-dWellOiledMachine-130, each with a SEV row. Re-running the derivation found the same four specs as the spec.
- **Ledgers:** lines added for S1, S2, S5, S9, S12 and S14 to S18 in the ledgers of units 69 to 73, appended to the AC lines the close's greps read, plus this unit's own ledger at `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-78-1-acceptance-ledger.md`.
- **Shell-role rows:** widened under widen-21 and widen-22 to the measured counts, 1743 for the hook and 820 for the gov suite. The hook's base blob already measured 1731 against its row's 1720, a gap this pass did not make; the widen record names it.
- **Other files in the commit:** the regenerated index files (LIVE.md, `backlog/PLAY.md` and `TOOL.md`, four build READMEs, the spec's records table), RUN.md, and a kickoff manifest re-stamp in `memory/guides/SESSION-KICKOFF.md`, which the pre-commit hook required because `tools/gate-legs.json` is on its watch list. The re-stamp and the generated paths were declared with an extra `--dispatch`. `gen_map --write` rewrote nothing.

**Checks run (each stands in for a gate the close runs):**
- **AC8 and AC14** (stand in for the gov canary): the new suite lines, cut out and run over the built hook, passed. Over three scratch breaks they failed as specified: the base `read_bar_file` reported `missing: base max_age blocks` and named `bg_fp bg_reused bg_sha bg_st`; an `IFS=$'\t'` split in `read_green_file` named `rec_man`; a loop without `|| [ -n ]` named `rec_st`.
- **AC1** (stands in for the canary): with the hook's CR strip deleted, the canary lines printed the `for count 0` line plus the compare lines naming `rec_sha` and `rec_fp`.
- **S2:** each liveness variant's canary mutant differed from its variant by one line.
- **AC9:** `read_inherited_green` gave `ig_sha` 40 bytes and `ig_age` `7`, and left a caller's `bg_sha` unchanged. The awk range counted 0 and 1. (DERIVED from the builder's probe)
- **AC4, AC5, AC7** (stand in for `measure-legs selftest` and the guard probes), in a fixture repo under `%TEMP%/p78fx`: the hook-only commit exited 1; the two scratch manifests, one without the hook entry and one spelling it `{prefix}/.githooks/pre-push`, exited 0; a commit touching only `tools/hooks/kit.toml` exited 1; no glob in the guard.
- **AC11 and AC12** (stand in for the encoding posture leg): a `0xff` byte read GREEN and a directory read NONE, with no Traceback; the posture scan printed `[]`.
- **AC10, AC18, AC19, AC20:** greps observed. `bash -n` passed on the hook, and `read_inherited_green` passed the naming lexicon.

**Owed to the main loop at the close:**
- Every §7 leg.
- The `New arm:` RED-first observations in `tools/run-gates/run-gates.gov.test.sh` (covers AC8 and AC14): a `read_bar_file` keeping `IFS=$'\t' read -r k v` (names a `bg_*` variable), an `IFS=$'\t'` split in `read_green_file` (names `rec_man`), and a loop without `|| [ -n "$_rg_l" ]` (names `rec_st`).
- The suite runs of AC1 and AC2, plus the close's ledger greps for AC2, AC3, AC6, AC13, AC15, AC16, AC17 and AC19.
- The `PASS (<n> assertions)` count with the two new assertions; the floor stays 72.

**The bug-class checklist was run over HEAD~1..HEAD and acted on:**
- `a-spelling-change-strands-its-readers`: `check_tree_selection` hashes LF-written rows, so the CR strip matches the runner's `read_tag_lines`.
- `fixture-passes-by-finding-nothing`: an empty derivation or an empty cut reds the new assertions.
- `insert-after-a-key-that-occurs-twice`: every ledger and backlog insert required exactly one match.
- `an-attested-count-must-count-what-the-grader-counts`: the row counts come from the grader's own `measure_code_lines`.

No probe was skipped or ran out of time. The scratch fixtures under `%TEMP%` were removed.
