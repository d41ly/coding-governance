**Serves:** journal TOOL-dQuietDisk-28

# Build brief — TOOL-dQuietDisk-28

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. dWitnessedBar has landed, and this branch carries its landing through
  the merge `40def53f7`. Your spec is rev-1, written at that base; the store it changes has not moved since.
- **Orders 1 and 2 are built.** You change TOOL-dQuietDisk-1's history store, which units 2, 3 and 4 consume
  (`b24fe84dc`, `efe7745ba`, `9a391e184`). Their stated bounds are upper limits, so none of their specs moves. Read
  the store as built, `tools/lib/history_store.py` and `tools/lib/history-store.sh`, and the consumers' calls of it.
- **Order 3 builds one unit at a time** in this tree, you first. Nothing else writes here while you run.
- **Check every git command, env var and shell idiom your spec names against the real tool** before you build on it.
  Sibling passes stopped on spec facts that did not hold: `git rev-parse --short` takes a single revision; a local
  `git clone --shared` spawns two processes; an MSYS shell rewrites a `!/path` argument into a Windows path.
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Traps on this node

- **Run no self-test.** `python tools/lib/history_store.py --selftest` and the unattended kit's suites are the close's
  (owner rule, 2026-08-23). Observe each criterion with a probe in a scratch repository under the scratch root,
  importing the module or sourcing the bash face. Your AC3 (the self-test unchanged) and the new arm's RED-first
  observation are owed to the close.
- **Run no gate leg, no suite and no bar.** Verify with a fixture or a probe of the code you changed.
- **The old leg for AC1 is the copy at `40def53f7`.** Extract it with `git show 40def53f7:<path>` into the scratch
  root, never by checking anything out in this tree.
- **Name every new function from the lexicon.** Use a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
  Check a name with `python tools/lexicon/lexicon.py --suggest <name> --as function`.
- **No kit path literals in shipped code.** Never spell `tools/<kit>/...` literally; name the kit once in a variable.
- **Cite code by symbol or blob.** In every record you write, cite code lines as `path#symbol` or blob-pinned, never
  as a bare `path:line`.
- **No here-string or heredoc fed from `$(...)`.** Write the value to a scratch file and read the file instead.
- **The three store copies stay byte-identical.** Edit `tools/lib/history_store.py` and copy it to
  `tools/unattended/history_store.py` and `tools/memory-tree/history_store.py` before the commit.
- **Shell lines only shrink.** `tools/lib/history-store.sh` and `tools/unattended/lib-unattended.sh` sit at their rows
  in `memory/project/shell-role.txt`. Widen each through
  `python tools/memory-tree/ratchet.py widen shell-role --key <path> ... --reason <text> --unit TOOL-dQuietDisk-28`,
  then set each row to the measured code lines. Your spec names widen record 4, but the build folder already holds
  widen records 1 to 7: the record is the one `ratchet.py` writes.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`; shell code
  finds python through `tools/lib/resolve-python.sh`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-28`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-28` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-28-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-28-deviation-1.md`. Its values are `report` and `author-recorded`.

