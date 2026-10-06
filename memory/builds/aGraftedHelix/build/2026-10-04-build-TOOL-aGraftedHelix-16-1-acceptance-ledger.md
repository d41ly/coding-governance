# Acceptance ledger — TOOL-aGraftedHelix-16

**Serves:** journal TOOL-aGraftedHelix-16

Node `a`, 2026-10-05. The build commit is `bc60ff9c`, over the spec's rev-3 commit `91b3f355`. That
rev was made before any code, after a scratch run of a drafted block found three things rev-2 could
not hold: the attribution trailer only the agent knows, the re-add that the whole-line loop makes
redundant, and the `-B` break that a host setting `PYTHONDONTWRITEBYTECODE` hides. No merge bar and no
self-test suite ran in this pass. AC1 and AC4 ran unit 15's scratch `node` probe from the session
scratchpad. AC2 ran a slice of the build-harness suite under a name that is not a `.test.sh`: the
prologue, the GH15 block, the layout scratch root and the new GH16 block, 105 arms, all `ok`, on the
render at the build commit. Each staged break was a scratch COPY of the render or of the slice,
deleted after its run.

**Evidences:** TOOL-aGraftedHelix-16
- AC1 — `commit:specs:tB` — the probe decoded that prompt off its `promptjson:` line and found one
  fenced shell block, two fence lines in all.
- AC1 — `set -e` — the block's first line. Its render line, block line 9, carries `-B`.
- AC1 — `git add -- <spec paths>` — at block line 10, right after the render line, and
  `git status --porcelain -- <spec paths>` is the block's last command.
- AC1 — `git commit` — none of the four command spellings occurs outside the block; the one
  near-miss printed was the prose's ban on `git add -A`.
- AC1 — `committed: false` — the prose returns it for a non-zero step with that step's output, and
  for a non-empty last line with the porcelain lines quoted in `why`.
- AC1 — `gen_build_index.py --write` — RED on three render copies: the re-add deleted, a prose re-add
  re-inserted outside the block, and the quoting sentence deleted.
- AC2 — `git status --porcelain -- <spec>` — printed nothing after the block exited `rc=0` in a
  repository under `%TEMP%`, and `git rev-parse HEAD:<spec>` equalled `git hash-object <spec>`.
- AC2 — `<!-- gen:spec-records -->` — present in `git show HEAD:<spec>`, and
  `git show --name-only --format= HEAD` named the spec and the build README and neither foreign path.
- AC2 — `__pycache__` — `git ls-tree -r --name-only HEAD` held none; the foreign paths still read
  ` M notes.txt` and `?? scratch.txt`; `gen_build_index.py --check` in a clean clone exited 0.
- AC2 — `git rev-parse HEAD` — with a sibling spec's header edited unstaged, the block refused naming
  that spec, with `HEAD` unmoved and nothing staged.
- AC2 — ` M <spec>` — step 5 removed whole printed it and the two hashes differed. The inverted
  filter committed both foreign paths, `-B` removed committed 2 caches, and the input check removed
  moved `HEAD` in the variant.
- AC2 — `git hash-object <spec>` — the re-add removed ALONE left every real-git row green, as spec
  rev-3 states; the suite's order arm read RED on that copy.
- AC3 — `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` — with `91b3f355` it
  printed `epoch: review-harness · clean · 1.33`, up from `1.32` at that parent.
- AC3 — `bash tools/check-kit-versions.sh` — printed
  `kit-versions: clean — 16 declared carrier(s) under tools/`.
- AC3 — `tools/workflows/unattended-build.js` — line 3 reads `1.5`, up from `1.4` at the parent.
- AC4 — ` M <path>` — a commit double returning `committed: false` with that `why` ended in `THROW`
  carrying it; RED on a render copy whose refusal dropped the `why`.

The channel canary and the real-git arm were also observed RED on a slice copy whose `promptjson:`
line flattened newlines: the canary read `false` and the arm reported every row it holds UNRUN.
`python tools/lexicon/lexicon.py` read OK, `bash tools/check-install-prefix.sh` read clean,
`python tools/check-spec-tokens.py` exited 0, `node tools/workflows/check-workflow-syntax.js` printed
`6 workflow script(s) parsed clean`, and `python tools/codebase-map/test_codebase_map.py` printed six
`ok` lines. Left to the main loop at VERIFYING, because only a suite observes them: the build-harness
self-test whole, at its new floor of 387, and the other legs the spec's section 7 names.
