**Serves:** journal TOOL-dWitnessedBar-41

# TOOL-dWitnessedBar-41 — builder return 1 (run `wf_9b2631d7-a7c`), committed 5a4f86e0c17436a5d4ae35dd8cf59a91535acbe5

## Why

TOOL-dWitnessedBar-41 is built as its spec (rev-3) says. Every citation in the spec matched the tree at base: the blobs d9c0c2e8, cfb339de and 2ed9424c, both plants found by the git grep, and the symbols it names. The criteria were checked with fixture probes, not gates. Spec status is set to CLOSED in the pass commit.

## Summary

Unit TOOL-dWitnessedBar-41 is built and committed as 5a4f86e0c (base 386b3ebee), with a `Pass: TOOL-dWitnessedBar-41` trailer and the spec status moved to CLOSED in the same commit.

**What changed**
- `tools/run-gates/run-gates.sh`: while it reads the selection file, the runner now also builds the canonical text: every line whose first field is `held`, with a trailing CR cut. Each row is still parsed exactly as before. The per-tree verdict gains `selection` (the hash of that text, or `none` when there is no file) and one `selection.<n>` key per row, written next to `run_id`.
- `.githooks/pre-push`:
  - The old S7 block is now a function, `check_selection_at_r <--run|--selection> <path>`, and its messages are unchanged.
  - `read_bar_file` reads `bg_sel` and `bg_sel_rows`, and `check_bar_base` keeps both local.
  - A new `check_tree_selection` is called from `check_tree_verdict` and from the cover pass's `bar` branch, next to `check_tree_reuse`. It refuses a record with no `selection` key, passes `none`, refuses rows that do not match the stored hash, and otherwise runs `select --check --selection` at R, at most once per hash per push.
- `tools/run-gates/verdict_flow.py`: `select --check` now takes exactly one of `--run` or `--selection`; anything else exits 2.
- Test plants: the per-tree records the hook suites plant gain `selection none`. The run-log suite's plant also gains `reused 0` and `reused_cache 0`.
- New test arms: a second-worktree AC2 arm in `.githooks/pre-push.test.sh`, two more AC3 cases there (`seledit`, `selkeyless`), and an AC1 arm in `tools/run-gates/run-gates.evidence.test.sh`.
- `tools/run-gates/README.md` documents the new keys and the flag. The kickoff manifest is re-stamped with delta none. The acceptance ledger is at `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-41-1-acceptance-ledger.md`.

**How it was checked** (fixture probes, no gate or suite run)
- **AC1:** I ran the runner over a scratch clone with `GATE_SELECTION` naming a file outside it (CRLF row, header, one non-held row). It wrote `selection 392504f4` and `selection.1 guarded · quarantine · TOOL-x-7`, and the hash matched `git hash-object` of the canonical text. A second run with no selection wrote `selection none`. This stands in for the `run-gates evidence` arm.
- **AC2:** I ran the hook from a second, detached worktree with no run directory of the first:
  - A record whose selection R does not derive was not covered, the bar ran, and the message named the row.
  - A record holding exactly the row R derives was covered with no bar run, and so was a `selection none` record.
  - The CLI `select --check --selection` exited 1 and 0 on the same two files.
  - An extracted copy of `check_tree_selection` ran its check once across two calls on the same hash.
  This stands in for the `pre-push self-test` arm.
- **AC3:** in the same probe, an edited `selection.1` and a deleted `selection` key were each refused with their reason, and the bar ran.
- The naming lexicon answered OK for `check_tree_selection`, `check_selection_at_r` and `write_bg_selection`. `bash -n` passed on the hook and the runner.

**Still to run at the close (main loop)**
- The two `New arm:` lines, each observed RED on its staged break and then GREEN:
  - `.githooks/pre-push.test.sh` (AC2 and AC3), staged red by skipping `check_tree_selection`.
  - `tools/run-gates/run-gates.evidence.test.sh` (AC1), staged red by dropping the `selection` keys from the writer.
- The section 7 legs: `measure-legs selftest`, `pre-push self-test`, `pre-push bar self-test`, `pre-push run-log line`, `run-gates canary`, `run-gates evidence`, `kickoff-manifest ratchet`, `recall floor`, `recall floor arms`, `memory hygiene`.
- The spec asked the pass to see whether the run-log suite's `DEC covered` checks pass at HEAD before the change. I did not run that suite, so it goes to the close, the same as the `pre-push run-log line` leg.

**How the commit was made**
- The shared worktree held unit 55's uncommitted files, which would have made the generated-file checks in the pre-commit hook read stale. So I committed in a clean clone (base plus only this unit's paths), through a linked worktree there: the hook refuses commits on the clone's primary tree.
- I regenerated the index (`gen_build_index`) and the codebase map in that clone; the generated files that changed were `memory/backlog/TOOL.md`, `memory/builds/dWitnessedBar/README.md` and `memory/map/generated/symbols.json`. All hooks passed with no `--no-verify`.
- I then moved the shared branch forward with a compare-and-swap `update-ref` from 386b3ebee, and aligned only this unit's index and working-tree entries to the commit.
- **Unit 55:** its working files were left untouched. Its working copy of `memory/builds/dWitnessedBar/README.md` still shows unit 41 as INPROGRESS until it regenerates. Its RUN.md row also declares `memory/map/generated/symbols.json`, which is in this unit's write set too.
- The clones and fixture repositories are deleted.

**Bug-class checklist:** `gotchas --for-diff HEAD~1..HEAD` selected 49 classes. Reviewing them changed nothing: the arms assert real refusals and real covers, empty fields survive the ` · ` round trip, the records are read by key, and both per-tree readers call the new check.
