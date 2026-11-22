**Serves:** journal TOOL-dQuietDisk-36

# Build brief — TOOL-dQuietDisk-36

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. Every roster unit is terminal, and the closing diff review's round 1
  (`memory/builds/dQuietDisk/reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md`) confirmed two
  HIGHs. You are that round's fold, rev-1 of your spec at base `1af732885`. Round 2 reviews your commit alone, so
  change nothing your spec does not name.
- **Read H1 and H2 in the review whole** before you build; your spec's design answers them.
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Traps on this node

- **Run no suite and no runner.** `lib-selftest.test.sh`, `resolve-python.test.sh`, `run-gates.turnstile.test.sh`,
  `run-gates.sh` and every kit self-test are the close's (owner rule, 2026-08-23; scratch-guard rows G1 to G3). Your
  new arms are written, not run: the main loop observes each RED then GREEN. Verify with probes of the blocks you
  changed, under the scratch root.
- **Never point a probe's GIT_DIR at this repository.** Every H1 probe exports `GIT_DIR` at a scratch repository it
  made under the scratch root.
- **Keep the three copies of the template block byte-equal**: `tools/lib/template-cache.sh`, the inline copy in
  `tools/lib/lib-selftest.sh` and the one in `.githooks/pre-push.test.sh`.
- **Never touch an adopter**, and never enter a `gov-upgrade` worktree.
- **The shell-line rows widen after your pass.** Do not edit `memory/project/shell-role.txt` or any other shrink-only
  ledger under `memory/project/`: the main loop widens them once your pass legs report the counts.
- **Name every new function from the lexicon.** Use a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
  Check a name with `python tools/lexicon/lexicon.py --suggest <name> --as sh.function`.
- **No kit path literals in shipped code.** Never spell `tools/<kit>/...` literally; name the kit once in a variable.
- **Cite code by symbol or blob.** In every record you write, cite code lines as `path#symbol` or blob-pinned, never
  as a bare `path:line`.
- **No here-string or heredoc fed from `$(...)`.** Write the value to a scratch file and read the file instead.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`; shell code
  finds python through `tools/lib/resolve-python.sh`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-36`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-36` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-36-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-36-deviation-1.md`. Its values are `report` and `author-recorded`.

