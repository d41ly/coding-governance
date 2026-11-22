**Serves:** journal TOOL-dQuietDisk-37

# Build brief — TOOL-dQuietDisk-37

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. Every roster unit is terminal, and the closing diff review converged
  at round 2. You are the unit its exit promoted: round 1's MEDIUM and LOW findings, batched, rev-1 of your spec at
  base `db9670ee7`. M3 is not yours (ask TOOL-dQuietDisk-39).
- **Read the review's MEDIUM and LOW sections whole** in
  `memory/builds/dQuietDisk/reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md`; cite the code
  as it stands at your base. TOOL-dQuietDisk-36 (`4840e65ed`) already changed the template block: build on it.
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Traps on this node

- **Run no suite and no runner.** The govkit self-test, `run-gates.test.sh`, `run-selftests.test.sh`,
  `lib-selftest.test.sh`, `resolve-python.test.sh`, `run-gates.sh`, a fixture bar and every kit self-test are the
  close's (owner rule, 2026-08-23; scratch-guard rows G1 to G3, gate-guard row D4). Your new arms are written, not run:
  the main loop observes each RED then GREEN. Verify with probes of the code you changed, under the scratch root.
- **Never point a probe's GIT_DIR at this repository, and never sweep the real temp dir.**
- **Keep the three copies of the template block byte-equal**: `tools/lib/template-cache.sh`, `tools/lib/lib-selftest.sh`
  and `.githooks/pre-push.test.sh`.
- **Never touch an adopter**, and never enter a `gov-upgrade` worktree.
- **The shell-line and spawn-idiom rows widen after your pass.** Do not edit any shrink-only ledger under
  `memory/project/`: the main loop widens them once your pass legs report the counts.
- **Name every new function from the lexicon.** Use a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
  Check a name with `python tools/lexicon/lexicon.py --suggest <name> --as py.function` (or `sh.function` for shell).
- **No kit path literals in shipped code.** Never spell `tools/<kit>/...` literally; name the kit once in a variable.
- **Cite code by symbol or blob.** In every record you write, cite code lines as `path#symbol` or blob-pinned, never
  as a bare `path:line`.
- **No here-string or heredoc fed from `$(...)`.** Write the value to a scratch file and read the file instead.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`; shell code
  finds python through `tools/lib/resolve-python.sh`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-37`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-37` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-37-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-37-deviation-1.md`. Its values are `report` and `author-recorded`.

