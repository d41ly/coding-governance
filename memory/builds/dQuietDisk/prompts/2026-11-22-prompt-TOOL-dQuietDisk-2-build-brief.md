**Serves:** journal TOOL-dQuietDisk-2

# Build brief — TOOL-dQuietDisk-2

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. dWitnessedBar has landed, and this branch carries its landing through
  the merge `40def53f7`. Your spec is rev-5, re-grounded there.
- **Order 1 is built.** TOOL-dQuietDisk-1, the history store you consume, and TOOL-dQuietDisk-14 are CLOSED. Read the
  store as built: `tools/lib/history_store.py` and `tools/lib/history-store.sh`. Your spec's section 8 names its gaps
  and the pick for each; follow those picks.
- **Order 2 builds one unit at a time,** in this tree: 2, then 3, 4, 5, 7 and 8. Nothing else writes here while you
  run, so commit directly.
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Traps on this node

- **Never run the unattended kit's suites.** That includes `check-pass-order.test.sh`, the suite you add an arm to,
  and anything `run-unattended-gates.sh --selftests` drives (owner rule, 2026-08-23). Observe each criterion with a
  probe in a scratch repository under the scratch root. The new arm's RED-first observation is owed to the close.
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
- **Shell lines only shrink.** `tools/unattended/check-pass-order.sh` and its test have rows in
  `memory/project/shell-role.txt`. If your pass grows either past its row, say so in your return with the measured
  count. The main loop widens the row; you do not edit the ledger.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-2`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-2` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-2-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-2-deviation-1.md`. Its values are `report` and `author-recorded`.
