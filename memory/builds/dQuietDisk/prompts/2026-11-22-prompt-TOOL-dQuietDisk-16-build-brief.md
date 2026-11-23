**Serves:** journal TOOL-dQuietDisk-16

# Build brief — TOOL-dQuietDisk-16

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. dWitnessedBar has landed, and this branch carries its landing through
  the merge `40def53f7`. Your spec is rev-4, re-grounded at `7b8c737b0`.
- **Orders 1 to 3 are built.** You change `govkit update`'s receipt-row reads. Units 14 and 18 already changed
  `tools/govkit/govkit.py`; build on its committed code. Unit 17, at order 5, also writes `govkit.py`, and unit 9, at
  order 6, writes `upgrade_steps.py`; both build after you.
- **Order 4 builds one unit at a time** in this tree: you first, then 26 and 11. Unit 15 is deferred.
- **Check every git command, env var and shell idiom your spec names against the real tool** before you build on it.
  Sibling passes stopped on spec facts that did not hold: `git rev-parse --short` takes a single revision; a local
  `git clone --shared` spawns two processes; an MSYS shell rewrites a `!/path` argument into a Windows path.
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Traps on this node

- **Run no suite and no runner.** The govkit self-test, `run-gates.sh` in any form and every unattended-kit suite are
  the close's (owner rule, 2026-08-23; scratch-guard row G2). Observe each criterion with a probe over a scratch copy
  of a `tools/govkit/fixtures/` target under the scratch root. Your AC8, the runner's trace count under `run` and
  `reuse`, and AC7's read-only `govkit check` against the adopters are owed to the main loop.
- **Never touch an adopter.** Never run `apply`, `update --write` or `adopt --write` against incms, nicocares or
  swydee, and never enter a `gov-upgrade` worktree.
- **Run no gate leg, no suite and no bar.** Verify with a fixture or a probe of the code you changed.
- **The old leg for AC1 is the copy at `40def53f7`.** Extract it with `git show 40def53f7:<path>` into the scratch
  root, never by checking anything out in this tree.
- **Name every new function from the lexicon.** Use a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
  Check a name with `python tools/lexicon/lexicon.py --suggest <name> --as function`.
- **No kit path literals in shipped code.** Never spell `tools/<kit>/...` literally; name the kit once in a variable.
- **Cite code by symbol or blob.** In every record you write, cite code lines as `path#symbol` or blob-pinned, never
  as a bare `path:line`.
- **No here-string or heredoc fed from `$(...)`.** Write the value to a scratch file and read the file instead.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`; shell code
  finds python through `tools/lib/resolve-python.sh`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-16`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-16` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-16-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-16-deviation-1.md`. Its values are `report` and `author-recorded`.

