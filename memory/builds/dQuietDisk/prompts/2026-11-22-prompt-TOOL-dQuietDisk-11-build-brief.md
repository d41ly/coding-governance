**Serves:** journal TOOL-dQuietDisk-11

# Build brief — TOOL-dQuietDisk-11

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. dWitnessedBar has landed, and this branch carries its landing through
  the merge `40def53f7`. Your spec is rev-4, re-grounded at `c3c0811b8`.
- **Orders 1 to 3 are built, and units 16 and 26 of order 4** (`fe51f4d4d`, `b31f3bd11`). You pass TOOL-dQuietDisk-7's
  `TemplateCache` to the govkit suite's recurring `build_target` calls. Unit 18 already added arms to
  `tools/govkit/selftest.py` (`87bd02fec`, `e8f0e7d31`); build on its committed arms. Unit 16 changed `govkit.py` and
  `upgrade_steps.py` but not the suite. Unit 17, at order 5, also writes `govkit.py`, and builds after you.
- **Read the cache as built:** `tools/lib/template_cache.py`, `build_target(..., template=None)` in
  `tools/govkit/fixture_target.py`, and `read_template_mode` in `template_cache_sh`. Every clone the cache hands out
  has no remote, and a cached clone costs three git processes [PINNED, TOOL-dQuietDisk-7 rev-6 AC7].
- **Order 4 builds one unit at a time** in this tree: 16 and 26 are done, you are the last. Unit 15 is deferred.
- **Check every git command, env var and shell idiom your spec names against the real tool** before you build on it.
  Sibling passes stopped on spec facts that did not hold: `git rev-parse --short` takes a single revision; a local
  `git clone --shared` spawns two processes; an MSYS shell rewrites a `!/path` argument into a Windows path;
  `git hash-object --stdin-paths` and an alternates line both refuse an MSYS `/c/...` path.
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Traps on this node

- **Run no suite and no runner.** The govkit self-test (`python tools/govkit/selftest.py` in any form), `run-gates.sh`
  and every unattended-kit suite are the close's (owner rule, 2026-08-23; gate-guard row D4, scratch-guard row G3).
  Observe AC1 to AC5 and AC7 with probes that import the suite's helpers or `fixture_target` under the scratch root.
  AC6, the arm extraction over the suite before and after, is owed to the main loop. The new arm is written, not run:
  its RED-first observation is the main loop's at the close.
- **Never touch an adopter.** Never run `apply`, `update --write` or `adopt --write` against incms, nicocares or
  swydee, and never enter a `gov-upgrade` worktree.
- **Run no gate leg, no suite and no bar.** Verify with a fixture or a probe of the code you changed.
- **The old suite is the copy at `b31f3bd11`.** Extract any old file with `git show b31f3bd11:<path>` into the scratch
  root, never by checking anything out in this tree.
- **`tools/gate-legs.json` and `tools/govkit/registry.toml` are shared surfaces.** Change only the rows your spec names,
  and re-render whatever reads them where your spec says so. The kickoff manifest's `last-audit` re-stamp follows the
  manifest's own stamp rule.
- **Name every new function from the lexicon.** Use a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
  Check a name with `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- **No kit path literals in shipped code.** Never spell `tools/<kit>/...` literally; name the kit once in a variable.
- **Cite code by symbol or blob.** In every record you write, cite code lines as `path#symbol` or blob-pinned, never
  as a bare `path:line`.
- **No here-string or heredoc fed from `$(...)`.** Write the value to a scratch file and read the file instead.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`; shell code
  finds python through `tools/lib/resolve-python.sh`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-11`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-11` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-11-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-11-deviation-1.md`. Its values are `report` and `author-recorded`.

