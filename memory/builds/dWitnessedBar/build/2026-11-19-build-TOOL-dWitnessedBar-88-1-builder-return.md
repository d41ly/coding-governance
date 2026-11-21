**Serves:** journal TOOL-dWitnessedBar-88

# TOOL-dWitnessedBar-88 — builder return 1 (run `wf_81a62cd1-8d0`), committed 7f1e87a6d557681ecf5a45b875e824852def7432

## Why

Every claim the spec makes about current code held when I checked it before the first edit: return codes, the `check_key_variant` arguments and match, the floor at 80 with the `TOOL-aShardedFloor-2` line above it, shell-role 850, the registry guard, `BROAD_LEG_FLOOR` 5, the two aScoutedSeam specs, the measure probe printing nothing, the caller count of 2, and the owner derivation printing 28 and unit 90. One wording point for the spec writer, not a divergence: read literally, AC3's "unedited cut" (the hook's cut with its CR strip still in place) prints both variables and returns 1, which is what S3 says it should do. I read it as the canary's mutant with no variant edit, which returns 0 and prints nothing. This is recorded in the ledger and in a Decided trailer.

## Summary

TOOL-dWitnessedBar-88 is built and committed as 7f1e87a6d557681ecf5a45b875e824852def7432, starting from base fd9628af8. The commit carries a `Pass: TOOL-dWitnessedBar-88` trailer and sets the spec header to CLOSED, dated 2026-11-21. No gate, suite or bar was run.

**What changed**
- `tools/run-gates/run-gates.gov.test.sh`, existing lines rewritten only:
  - S3: `check_canary_keys` now returns 0 when it printed nothing, 1 when it printed a variable, and 2 on an unreadable file or a failed visit count. `check_key_variant` accepts only a 1 with exactly `<var>`: a 2 keeps the `rc 2` reason and any other return prints the passed reason.
  - S10: the `<key>)` match now accepts bare, quoted, braced, braced-quoted and aligned arms.
  - S17: the length call's fifth argument is now `the length variant named`.
  - Shell-role stays at 850 and `FLOOR_ASSERTIONS=80` is untouched, with no line added above it.
- S11: the `run-gates gov canary` guard in `tools/govkit/registry.toml` gains `.githooks/` last, and `tools/gate-legs.json` was re-rendered with `leg_factory.py --write`.
- `memory/guides/SESSION-KICKOFF.md`: `last-audit` re-stamped at fd9628af8.
- `memory/builds/dWitnessedBar/BACKLOG.md`: new ask TOOL-dWitnessedBar-105 with a LOW `SEV` line, covering the two `manifest-check` files and naming DEPL-aScoutedSeam-1 and KICK-aScoutedSeam-1.
- New acceptance ledger at `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-88-1-acceptance-ledger.md`, one line per criterion.
- `gen_build_index.py --write` re-rendered the build README, `memory/LIVE.md`, `memory/backlog/TOOL.md` and the spec's records region, and `RUN.md` is committed with the pass. `gen_map.py --write` changed nothing, because no function was added or renamed.

**Checks that ran**
Each is a probe or fixture standing in for the `run-gates gov canary` arm, the `spec tokens` leg or the `testsuite counts` leg.
- A scratch cut of the edited suite's functions, sourced over the real AC12 record built by the suite's own python block under `%TEMP%/p88`:
  - **AC3:** the length variant's `sha` mutant returned 1 and printed exactly `rec_sha`. The canary mutant with no variant edit returned 0 with no output. A missing file returned 2.
  - **AC10:** the new match changed one line on each of the five spellings. The old match changed 0 lines on the braced, braced-quoted and aligned ones, so this probe would have caught the old code. (DERIVED from the builder's probe)
  - **Liveness loop:** all four variant calls returned 0.
  - **AC2 / AC17:** with `check_canary_keys` wrapped to over-report, the calls printed `it named rec_sha whose CR arrived`, `the length variant named rec_sha whose CR arrived` and `the length variant named rec_fp whose CR arrived`, each returning 1.
- **AC5:** in a fixture repository under `%TEMP%/p88f`, `build_commit` printed the second commit's sha while the `git log | grep` lookup named the `Pass: none` commit.
- **AC11:** `--legs-for .githooks/pre-push.test.sh` printed `run-gates gov canary <- .githooks/ [selftests/repo] broad`, and `--legs-for .githooks/pre-push` still printed the exact entry.
- **AC8, AC9, AC14, AC18:** the two floor greps each printed 1, the measure probe printed nothing, the caller count printed 2, and the AC18 pipeline printed nothing.
- **AC6 (partial):** the owner derivation printed 28 and unit 90's spec.
- `sh_hygiene.py --shell-role --measure` printed 850, and `bash -n` passed.

**Owed by the main loop at the close**
- The `New arm:` on `run-gates.gov.test.sh` (AC2, AC10, AC17) owes its RED-first observation: the over-reporting scratch suite should reach `the length variant named rec_fp whose CR arrived`, and a one-spelling match should reach `variant changed 0 lines` on a braced arm. (DERIVED from the builder's probe)
- The scratch-clone arm runs for AC2, AC7, AC10 and AC17.
- AC6's planted-spec clone and AC13's clone at the commit that added the spec.
- The scratch copies for AC9 and AC14.
- Every other-unit ledger line for AC1, AC2, AC4 to AC12, AC14 to AC16, AC18 and AC19.
- The legs of §7, held legs included under GATE_SELFTESTS.

**Bug-class checklist**
`gotchas.py --for-diff HEAD~1..HEAD` exited 0 with 35 classes. I acted on three:
- `a-spelling-change-strands-its-readers`: the only two callers of `check_canary_keys` are in the suite. One was updated and the other tests only for a 2.
- `fixture-passes-by-finding-nothing` and `staged-break-substitutes-a-synthetic-value`: the probes used the real record, and the old match failed them.
- `held-suite-guard-misses-a-sibling-kit` is the gap S11 fixes, with the rest carried by ask TOOL-dWitnessedBar-105.

**For the caller**
- The commit trailer uses the charter's `Claude Opus 5` attribution rather than the system reminder's 5.5; recent build commits use both.
- `help/reference/drive.md` and `help/reference/units.md` were already modified before this pass (line-ending noise only) and were not staged.
- Nothing timed out or was skipped.
