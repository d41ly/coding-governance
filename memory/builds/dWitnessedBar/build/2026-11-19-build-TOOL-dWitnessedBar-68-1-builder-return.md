**Serves:** journal TOOL-dWitnessedBar-68

# TOOL-dWitnessedBar-68 — builder return 1 (run `wf_7c8c96ec-c1d`), committed 52bcf7599

## Why

TOOL-dWitnessedBar-68 is built as rev-3 states. The spec's claims about current code held against the tree: run_local_plant, run_fixture's git-variable list, run_fixture_command, read_local_verdict and check_local_record reading no sha, and the arm at lines 817-841. S3's "once unit 69 lands" branch is the one that holds now. Nothing in the spec diverged.

## Summary

Pass commit 52bcf7599 on base f6bcc989c. Subject names TOOL-dWitnessedBar-68; trailers are `Pass: TOOL-dWitnessedBar-68` and Co-Authored-By. The spec status is now CLOSED · rev-3 · 2026-11-21, a one-line header edit; the index generator also refreshed the spec's spec-records block.

What changed:
- **S1** (tools/run-gates/run-gates.gov.test.sh, the AC12 arm): one `"$PYBIN" -c` call, with `$KITDIR` on `sys.path`. It clears run_fixture's git variables, runs `run_local_plant("clean", <mktemp -d>, lambda *a, **k: None)` and rewrites `<common-dir>/gate-verdict/<tree>` in binary. Every plant line except verdict, sha and reused_cache is kept byte for byte, followed by the 5 lines S1 lists. The call's last line prints `<sha> <record path>`. (DERIVED from the builder's probe)
- **S2**: read_green_file and read_tag_lines now read that path.
- **S3**: the same call runs `read --backend local-hook --sha <HEAD>` through run_fixture_command. The arm gives it its own `a=$((a+1))` and checks that the printed line starts with `verdict: local-hook · GREEN · <sha8> `. On failure it prints the CLI line, plus the call's whole output when the call exited non-zero. The comment and the WHAT THIS DOES NOT CHECK clause are updated.
- **S4**: unit 65's ledger AC12 line now names TOOL-dWitnessedBar-68 AC3.
- **Shell-role row** for the suite: widened by `ratchet.py widen` (record 2026-11-21-build-TOOL-dWitnessedBar-68-widen-10.md), then set to the measured 636 (was 611), as unit 51 S1 says.
- **Records**: acceptance ledger 2026-11-19-build-TOOL-dWitnessedBar-68-1-acceptance-ledger.md written. gen_build_index --write rewrote LIVE.md, backlog/TOOL.md, the build README and the spec's records block; all are committed, along with RUN.md.
- **Not changed**: no function was added, so the codebase map needed no regeneration, and the kickoff manifest watch list does not name the suite.

Checks that ran (each a probe of this arm, standing in for the run-gates gov canary arm):
- I ran the arm's own lines (817-869) through `eval` with KITDIR set to the real kit (scratch script probe68.sh):
  - 3 assertions, fail 0.
  - The CLI printed `verdict: local-hook · GREEN · <sha8> · witness witnessed`.
  - AC1: `od -c` showed `\r\n` after GREEN, after the forty b and after `reused_cache\t0`. `grep -c '^reused_cache'` printed 2 and `grep -c '^selection'` printed 2. The record's file name equalled `HEAD^{tree}`.
  - AC2: rec_sha was forty b, 40 bytes. (DERIVED from the builder's probe)
- AC3 red half: over a scratch tools/ at %TEMP%/r68 (copies of run-gates/ and policy/, with read_tag_lines changed to `out.setdefault`, one changed line by diff), the arm printed `· NONE ·` naming `reused 1 leg(s) from the cache`, and fail was 1.
- With a missing KITDIR, the arm printed the call's traceback.
- `bash -n` on the suite passed.
- The commit hook's staged memory-hygiene grading passed.
- I ran `gotchas.py --for-diff HEAD~1..HEAD` and went through what it selected; nothing needed a change. The git-variable list is copied from run_fixture's, as S1 asks: a second copy that could drift (two-answers-to-one-question).

Owed at the close (not run here):
- The legs of §7: run-gates gov canary (held unless GATE_SELFTESTS / SELFTESTS_OWED_PATHS is set), portability (shell lines only shrink), recall floor, recall floor arms, and memory hygiene.
- The `New arm:` RED-first observation on run-gates.gov.test.sh: AC1-AC3, staged red by a verdict_backends.py whose read_tag_lines keeps the first of a repeated key.
- AC4 is checked by a grep on the ledger at the close.

Found, not caused by this unit: the shell-role seed (`sh_hygiene.py --shell-role --measure . :!memory/`) measures .githooks/pre-push at 1731, but its row says 1720. That row is unit 69's, from commit 9ff80bb15, and pre-push is unchanged since. So the portability leg is likely red at base on pre-push. I did not touch that row, because a widen from this unit would name the wrong cause.

Skipped commands: none.
