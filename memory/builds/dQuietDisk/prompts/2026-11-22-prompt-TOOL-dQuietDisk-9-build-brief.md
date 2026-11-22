**Serves:** journal TOOL-dQuietDisk-9

# Build brief — TOOL-dQuietDisk-9

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. dWitnessedBar has landed, and this branch carries its landing through
  the merge `40def53f7`. Your spec is rev-5, re-grounded at `ebab8b90b`, with its fork F1 ruled (b).
- **Orders 1 to 5 are done.** Order 4's units 16, 26 and 11 are built (`fe51f4d4d`, `b31f3bd11`, `33a4e2325`).
  TOOL-dQuietDisk-17, order 5, is WONTDO, so `tools/govkit/selftest.py` stands as units 18 and 11 left it.
  TOOL-dQuietDisk-6 is WONTDO and TOOL-dQuietDisk-15 is DEFERRED. You are order 6, the last product unit; unit 19,
  the measurements, follows you.
- **You touch many files.** The spec's Files touched names the owned-scratch blocks, both runners, the cleanup lint,
  and the 46 files [PINNED, the spec's Files touched at ebab8b90b] the predicate and the hook grep name. Several are copies of one block across kits
  (`commit_trailers.py` and `history_store.py` each travel as kit copies). Keep each copy byte-equal to the canonical
  block the parity rows grade, and keep every copy-installed file self-contained.
- **Check every git command, env var and shell idiom your spec names against the real tool** before you build on it.
  Sibling passes stopped on spec facts that did not hold: `git rev-parse --short` takes a single revision; a local
  `git clone --shared` spawns two processes; an MSYS shell rewrites a `!/path` argument into a Windows path;
  `git hash-object --stdin-paths` and an alternates line both refuse an MSYS `/c/...` path; a plain `x=$(...)`
  assignment makes the shell-hygiene scanner follow a heredoc loop over `$x`, where `if ! x=$(...)` did not.
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## This is the second pass

- **The first pass diverged and committed nothing** (unit harness run `wf_13bf29df-96d`). Its rulings are in rev-6 of
  your spec, from `2026-11-22-prompt-TOOL-dQuietDisk-9-divergence-task`. Read the rev-6 revision-log line first.
- **Start from its patch.** Apply
  `C:/Users/d41ly/AppData/Local/Temp/claude/b3f6db677b077b04/0840beea-0651-4dc3-9fe7-f227915b6b42/scratchpad/u9/TOOL-dQuietDisk-9-build.patch`
  with `git apply`, then check every hunk against rev-6 rather than trusting it. Never apply
  `TOOL-dQuietDisk-9-frozen-steps.patch`: the three step programs a landed row names stay byte-identical, and their two
  cleanup sites become waived rows in `memory/project/cleanup-sites.txt`.
- **The declared write set still names the three frozen programs.** Leave them untouched; a declared path you do not
  write is no finding.

## Traps on this node

- **Run no suite and no runner.** `run-gates.sh` and `run-selftests.sh` in any form, a fixture bar included, every
  `--selftest`, every kit self-test and every unattended-kit suite are the close's (owner rule, 2026-08-23;
  scratch-guard rows G1 to G3, gate-guard row D4). The spec marks each criterion the main loop owes; observe the rest
  with probes of the blocks you wrote, under the scratch root. The new arms are written, not run.
- **Never sweep the real temp dir.** Every sweep probe plants its roots under a scratch dir and points the sweep
  there. Never delete anything under `%TEMP%` or the host temp root: the leftover roots the spec counts there are the
  owner's to remove, and the close's bar observes the two orphaned ones.
- **Never touch an adopter.** Never run `apply`, `update --write` or `adopt --write` against incms, nicocares or
  swydee, and never enter a `gov-upgrade` worktree.
- **The old files are the copies at `ebab8b90b`.** Extract any old file with `git show ebab8b90b:<path>` into the
  scratch root, never by checking anything out in this tree.
- **The shell-line rows widen after your pass.** Do not edit `memory/project/shell-role.txt`, or any other
  shrink-only ledger under `memory/project/` that your spec does not name: the main loop widens through
  `ratchet.py widen` once your pass legs report the counts. `memory/project/cleanup-sites.txt` is yours: it is the
  new lint's own registry, which your spec creates.
- **Kit versions.** Each kit whose shipped bytes move moves its version, as `kit epoch` requires. Find each kit's
  version where its descriptor or file keeps it, and name every bump in your return.
- **Name every new function from the lexicon.** Use a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
  Check a name with `python tools/lexicon/lexicon.py --suggest <name> --as py.function` (or `sh.function` for shell).
- **No kit path literals in shipped code.** Never spell `tools/<kit>/...` literally; name the kit once in a variable.
- **Cite code by symbol or blob.** In every record you write, cite code lines as `path#symbol` or blob-pinned, never
  as a bare `path:line`.
- **No here-string or heredoc fed from `$(...)`.** Write the value to a scratch file and read the file instead.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`; shell code
  finds python through `tools/lib/resolve-python.sh`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-9`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-9` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-9-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-9-deviation-1.md`. Its values are `report` and `author-recorded`.

