**Serves:** journal TOOL-dQuietDisk-13

# Build brief — TOOL-dQuietDisk-13

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. dWitnessedBar has landed, and this branch carries its landing through
  the merge `40def53f7`. Your spec is rev-4, re-grounded at `7b8c737b0`.
- **Orders 1 and 2 are built, and so are units 28, 18 and 10.** You consume TOOL-dQuietDisk-7's template cache as
  built (`360d706f6`, `3ffbc03fe`): read `tools/lib/template_cache.py`, `tools/lib/template-cache.sh` and the
  `--template` path of `tools/lib/lib-selftest.sh` whole. Every clone it hands out has no remote, and a cached clone
  costs three git processes. Your F1 ruled that you add `read_template_mode` to `template_cache_sh` and keep the
  inline copy in `lib-selftest.sh` byte-identical; unit 12 builds after you.
- **Order 3 builds one unit at a time,** in this tree: 28, 18 and 10 are built, you are next, then 12. Nothing
  else writes here while you run, so commit directly.
- **Check every git command and shell idiom your spec names against the real tool before you build on it.** Units 2
  and 3's first passes each stopped on a spec fact that did not hold (`git rev-parse --short` takes a single
  revision).
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Traps on this node

- **Never run a suite.** `tools/run-gates/run-gates.turnstile.test.sh`, `tools/lib/lib-selftest.test.sh`, the
  runner, the govkit self-test and every unattended-kit suite are the close's (owner rule, 2026-08-23;
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
- **Shell lines only shrink, and your spec owns the widen.** Your S7 grows the turnstile suite and the two lib files
  past their rows in `memory/project/shell-role.txt`. Widen each through
  `python tools/memory-tree/ratchet.py widen shell-role --key <path> ... --reason <text> --unit TOOL-dQuietDisk-13`,
  which writes the widen record; then set each row's count to the measured code lines.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`; shell code
  finds python through `tools/lib/resolve-python.sh`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-13`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-13` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-13-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-13-deviation-1.md`. Its values are `report` and `author-recorded`.


