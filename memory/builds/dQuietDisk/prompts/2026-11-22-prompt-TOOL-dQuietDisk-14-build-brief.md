**Serves:** journal TOOL-dQuietDisk-14

# Build brief — TOOL-dQuietDisk-14

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run.
  - Its base is the merge `e4699ee75`, which brought in dWitnessedBar's land tip `ed833f684`. The owner ruled on
    2026-11-22 to build on it and to land only after dWitnessedBar lands:
    `memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-owner-build-on-land-branch.md`.
  - This unit is build order 1, beside TOOL-dQuietDisk-1, which is CLOSED. Nothing else is built. Commit directly in
    this tree.
  - Your spec is at rev-3. Its rev-3 pass only gave its symbol citations full paths.
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- **AC6's before reading is taken.** The main loop ran `govkit.py check` read-only against `C:/projects/incms/main`
  and `C:/projects/nicocares/main` at `1abd1c969`. Both exited 0. Their outputs are in the session scratchpad as
  `u14-check-before-incms.txt` and `u14-check-before-nicocares.txt`. The main loop takes the after reading and
  compares the two.

## Traps on this node

- **Do not touch dWitnessedBar's branch.** Never write into `branch/unattended-dwitnessedbar-2ed3b3` or its worktree.
- **Never touch an adopter.** AC6's check is read-only and the main loop's. Never run `apply`, `update --write` or
  `adopt --write` against incms, nicocares or swydee, and never enter a `gov-upgrade` worktree. Every probe writes
  only into a scratch gov and a scratch target under the session's temp root.
- **Never run the unattended kit's suites,** and run no gate leg, no suite and no bar. That includes `govkit
  selftest`, which §7 lists for the close's bar, not for you. Verify with the probes §6 describes.
- **Name every new function from the lexicon.** Use a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
  Check a name with `python tools/lexicon/lexicon.py --suggest <name> --as function`.
- **Refresh the codebase map with every function change.** Before the pass commit, run
  `python tools/codebase-map/gen_map.py --write`, and commit what it rewrites.
- **No kit path literals in shipped code.** Never spell `tools/<kit>/...` literally in `govkit.py`. It ships to
  adopters at their prefix. Reach `held_halves.py` through the path govkit already resolves for gov's tree.
- **Cite code by symbol or blob.** In every record you write, cite code lines as `path#symbol` or blob-pinned, never
  as a bare `path:line`.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`, since
  bare `bash` is WSL's.
- **`govkit.py` is copied to its byte-identical twins by the kit's parity rows.** If `govkit selfcheck --write`
  re-derives a sum or a twin, commit what it rewrites. Run it once before the pass commit:
  `python tools/govkit/govkit.py selfcheck --write`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-14`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-14` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` stages rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-14-1-acceptance-ledger.md`
  in the pass commit. Give it one line per §6 criterion, each leading with a backticked token that criterion itself
  spells. Mark AC6's adopter-check half as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the map's generated
  files, govkit's selfcheck outputs and the build records, in `--dispatch` before your spawn. A path beyond that list
  needs its own `--dispatch` with `--writes` before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-14-deviation-1.md`. Its values are `report` and `author-recorded`.
