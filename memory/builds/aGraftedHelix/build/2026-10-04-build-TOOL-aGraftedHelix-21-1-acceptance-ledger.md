# Acceptance ledger — TOOL-aGraftedHelix-21

**Serves:** journal TOOL-aGraftedHelix-21

Node `a`, 2026-10-05. The build commit is `e80d7b27`, over the spec's rev-4 commit `0fbb05cb`. That
rev was made before any code, after reading the built unit 16 block: it named the record `before`
while S3 and AC2 spell `rec`, and section 4 now says the input check's refusal on an unstaged
run-state file is right for a live run. No merge bar and no self-test suite ran in this pass. AC1 ran
unit 16's scratch `node` probe from the session scratchpad. AC2 ran a slice of the build-harness suite
under a name that is not a `.test.sh`: the prologue, the GH15 definitions, a layout scratch root under
`%TEMP%` and the GH16 and GH21 blocks, 34 arms, all `ok`, on the render at the build commit. Each
staged break was a scratch COPY of the render, deleted after its run.

**Evidences:** TOOL-aGraftedHelix-21
- AC1 — `git status --porcelain --untracked-files=all` — the probe decoded the `commit:specs:tB` prompt off its `promptjson:` line and read that listing at step 1 and again at step 5, equal.
- AC1 — `${rec+x}` — one test at block line 3, between step 1 and step 2, and one at block line 13, after the render and before the loop; the prose carries `Run it as ONE Bash invocation`.
- AC1 — `git status --porcelain --untracked-files=all` — RED on a render copy with the flag deleted from step 5: the two listing lines differed.
- AC2 — `git ls-tree -r --name-only HEAD` — after the block exited `rc=0` with foreign/sub/brief.md planted, it named no `foreign/` path.
- AC2 — `git status --porcelain --untracked-files=all` — listed exactly the three foreign paths, unchanged.
- AC2 — `unset rec` — inserted after step 4, the block exited non-zero naming the record and the cleanup, `git rev-parse HEAD` was unchanged, and after that cleanup the block run again exited `rc=0`.
- AC2 — `git diff --cached --name-only` — empty after the block ran with step 1's assignment deleted, which exited non-zero naming the record, and the listing equalled its value before the run.
- AC2 — `git ls-tree -r --name-only HEAD` — with notes.txt deleted between step 4 and step 5, the block exited `rc=0` and HEAD still named it.
- AC2 — `git ls-tree -r --name-only HEAD` — RED on four render copies: without the flag it held `foreign/`, the whole-line membership test dropped notes.txt, the early guard deleted left the spec staged and the views rendered, and the late guard deleted moved HEAD.
- AC3 — `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` — with `0fbb05cb` it printed `epoch: review-harness · clean · 1.34`, up from `1.33` at that parent.
- AC3 — `bash tools/check-kit-versions.sh` — printed `kit-versions: clean — 16 declared carrier(s) under tools/`.
- AC3 — `tools/workflows/unattended-build.js` — line 3 reads `1.6`, up from `1.5` at the parent.

The re-add removed ALONE also read RED on a render copy, on the blob row and the order arm, which is
the change unit 16 predicted once the loop compares paths. `python tools/lexicon/lexicon.py` read OK,
`bash tools/check-install-prefix.sh` read clean, `python tools/check-spec-tokens.py` exited 0,
`node tools/workflows/check-workflow-syntax.js` printed `6 workflow script(s) parsed clean`, and
`python tools/codebase-map/test_codebase_map.py` printed six `ok` lines. Left to the main loop at
VERIFYING, because only a suite observes them: the build-harness self-test whole, at its new floor of
399, and the other legs the spec's section 7 names.
