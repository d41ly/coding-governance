**Serves:** journal TOOL-dQuietDisk-12

# Build brief — TOOL-dQuietDisk-12

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. dWitnessedBar has landed, and this branch carries its landing through
  the merge `40def53f7`. Your spec is rev-3, re-grounded at `7b8c737b0`.
- **Orders 1 and 2 are built, and so are units 28, 18 and 10.** You consume TOOL-dQuietDisk-7's template cache as
  built (`360d706f6`, `3ffbc03fe`): read `tools/lib/template_cache.py`, `tools/lib/template-cache.sh` and the
  `--template` path of `tools/lib/lib-selftest.sh` whole. Every clone it hands out has no remote, and a cached clone
  costs three git processes. Unit 13 (`5ea60aaa9`) added `read_template_mode` to `template_cache_sh`; where your suite
  reads the switch, it calls that, never a copy of the read.
- **Order 3 builds one unit at a time,** in this tree: 28, 18, 10 and 13 are built, and you close it. Nothing
  else writes here while you run, so commit directly.
- **Check every git command and shell idiom your spec names against the real tool before you build on it.** Units 2
  and 3's first passes each stopped on a spec fact that did not hold (`git rev-parse --short` takes a single
  revision).
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Traps on this node

- **Never run a suite.** `.githooks/pre-push.test.sh`, `tools/lib/lib-selftest.test.sh`, the runner,
  the govkit self-test and every unattended-kit suite are the close's (owner rule, 2026-08-23;
  scratch-guard row G2).
  Observe each criterion with a probe in a scratch repository under the scratch root, sourcing or importing the code
  you change. The new arm's RED-first observation is owed to the close.
- **Run no gate leg, no suite and no bar.** Verify with a fixture or a probe of the code you changed.
- **The old code for comparison is the copy at `40def53f7`.** Extract it with `git show 40def53f7:<path>` into the
  scratch root, never by checking anything out in this tree.
- **Name every new function from the lexicon.** Use a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
  Check a name with `python tools/lexicon/lexicon.py --suggest <name> --as function`.
- **No kit path literals in shipped code.** Never spell `tools/<kit>/...` literally; name the kit once in a variable.
- **Cite code by symbol or blob.** In every record you write, cite code lines as `path#symbol` or blob-pinned, never
  as a bare `path:line`.
- **No here-string or heredoc fed from `$(...)`.** Write the value to a scratch file and read the file instead.
- **Shell lines only shrink, and your spec owns the widen.** Your spec grows `.githooks/pre-push.test.sh` past its
  row in `memory/project/shell-role.txt`. Widen it through
  `python tools/memory-tree/ratchet.py widen shell-role --key <path> ... --reason <text> --unit TOOL-dQuietDisk-12`,
  which writes the widen record; then set each row's count to the measured code lines.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`; shell code
  finds python through `tools/lib/resolve-python.sh`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-12`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-12` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-12-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-12-deviation-1.md`. Its values are `report` and `author-recorded`.


