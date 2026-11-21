**Serves:** journal TOOL-dWitnessedBar-79

# TOOL-dWitnessedBar-79 — builder return 1 (run `wf_7ea119b0-4e3`), committed 08f226f3d

## Why

Unit 79 is built as rev-3 of its spec says, and the spec header is now CLOSED. I checked the spec against HEAD before writing and found no divergence. The loop body is still inline, as unit 77 left it. The one-edit grep printed 1 and the `_rg_v:1}` grep printed 0. The suite's shell-role row read 787 and measured 787, so a widen was needed. The suite is not on the kickoff manifest's watch list. The orientation card called the unit DEFERRED, but the spec header read INPROGRESS, so the unit was buildable.

## Summary

Commit 08f226f3d (Pass: TOOL-dWitnessedBar-79) changes C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh in three places.
- A new top-level function `check_key_variant <key>:<var> <replacement> <label> <passed reason> <other lead>`, whose variables are all local. It holds the old loop body: the one `<key>)` sed edit, the two diff counts and the `check_canary_keys` call. It returns 0 silently, or prints one reason and returns 1.
- The per-key loop calls it twice per pair. First the tail variant, `'${_rg_v%?}'` with an empty label, so its four reasons are byte-identical. Then the length variant, `'${_rg_v:1}'` with label `length ` and reason `the length variant passed a value one byte short`. Each failed call's reason prints unit 74 S3's line and sets fail=1. A key joins rgf_seen only when both variants were seen red.
- The arm's header comment names the length variant and says the `-ge 41` hole is not checked.

Other changes in the commit:
- The shell-role row was widened through `ratchet.py widen` (record memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-79-widen-20.md). Widen sets the count to 788, so I then set it to the measured 797, as the spec says.
- `gen_map.py --write` added check_key_variant to symbols.json.
- I wrote the acceptance ledger at memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-79-1-acceptance-ledger.md.
- `gen_build_index.py --write` rewrote README.md, LIVE.md, backlog/TOOL.md and the spec's records table. Its derived build status now reads DEFERRED, because no unit is INPROGRESS.
- RUN.md went in with the commit.
- The commit hook's staged memory-hygiene grading passed.
- The unrelated dirty help/reference/drive.md and units.md files were left unstaged.

Checks that ran (no gate, suite or bar):
- `bash -n` on the suite.
- The three AC3 greps, each of which printed 1. This stands in for AC3's grep, which is in no leg.
- An AC1 probe: the sha and fingerprint length edits each give one variant line and one mutant line. The sourced mutant over a hand-built AC12-shaped record read 40 bytes ending in `\r` for the edited key and 41 for the other. (DERIVED from the builder's probe)
- A scratch probe in C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/probe79.sh. It sources the suite's own function block and loop, and stands in for the `run-gates gov canary` leg.
  - Over the built suite: no line printed, rgf_seen held rec_sha and rec_fp.
  - At `-ge 0`: exactly the two AC2 lines for rec_sha and rec_fp, no tail-variant reason, fail=1, rgf_seen empty.
  - At `-ge 41`: no line, which is the hole the header names.
  - Over a hook whose sha case reads `rec_sha="$_rg_v"`: `variant changed 0 lines` then `length variant changed 0 lines`.
- `measure_code_lines` gave 797, standing in for the portability leg.

Owed to the main loop at the close:
- AC2 on a scratch clone over the real `run_local_plant` record, with the arm's non-zero exit.
- The New arm's RED-first observation: the suite with `-ge 0` in `check_cr_reached`, which should print the length-variant line for rec_sha and rec_fp.
- The legs `run-gates gov canary`, portability, codebase-map coverage + freshness, lexicon naming predicates, recall floor, recall floor arms and memory hygiene.

`gotchas.py --for-diff HEAD~1..HEAD` listed 32 classes. The ledger tokens are each on one line, the hand record stands in for the shipped one only until the close's clone run, and the function name uses the lexicon's `check` verb. Nothing needed a further edit. No check was skipped for running past its time bound.
