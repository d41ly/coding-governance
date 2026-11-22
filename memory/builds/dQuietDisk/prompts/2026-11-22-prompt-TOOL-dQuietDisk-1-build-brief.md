**Serves:** journal TOOL-dQuietDisk-1

# Build brief — TOOL-dQuietDisk-1

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run.
  - Its base is the merge `e4699ee75`, which brought in dWitnessedBar's land tip `ed833f684`. The owner ruled on
    2026-11-22 to build on it and to land only after dWitnessedBar lands:
    `memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-owner-build-on-land-branch.md`.
  - This unit is build order 1. Nothing is built yet. Unit 14 builds after you, in this same tree, so commit directly
    here.
  - Your spec was re-grounded at `e4699ee75` (rev-2).
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- **The other tasks.** A measurement task is running in a detached scratch clone. It touches nothing in this worktree.
  Leave it alone, and run no suite beside it.

## Traps on this node

- **Do not touch dWitnessedBar's branch.** Never write into `branch/unattended-dwitnessedbar-2ed3b3` or its worktree.
  Its files are now in this tree through the merge, so edit them here only where your spec says to.
- **Never run the unattended kit's suites.** That means `check-unattended.test.sh`, `unattended.test.sh`,
  `check-pass-order.test.sh`, `check-brief-recorded.test.sh`, or anything `run-unattended-gates.sh --selftests` drives.
  That is the owner's rule of 2026-08-23. Run your own new store's fixture or selftest directly, which is how a
  refusal is staged RED.
- **`tools/gate-legs.json` is GENERATED.** It is rendered by `python tools/run-gates/leg_factory.py --write` from the
  kit descriptors and `tools/govkit/registry.toml`.
  - Declare a new leg in its kit's descriptor, then re-render.
  - A hand edit of the manifest makes the bar refuse before any leg.
- **Refresh the codebase map with every function change.** Before the pass commit, run
  `python tools/codebase-map/gen_map.py --write`, and commit what it rewrites whenever you add, rename or remove a
  function.
- **Name every new function from the lexicon.** Use a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
  Check a name with `python tools/lexicon/lexicon.py --suggest <name> --as function`.
- **No kit path literals in shipped code.** Never spell `tools/<kit>/...` literally. Name the kit once in a variable,
  as the install-prefix ban requires.
- **Cite code by symbol or blob.** In every record you write, fixture text included, cite code lines as
  `path#symbol` or blob-pinned, never as a bare `path:line`.
- **No here-string or heredoc fed from `$(...)`.** Never feed a `while` loop from a here-string or heredoc whose value
  came from `$(...)` (`done <<<"$var"`): the shell-hygiene leg bans it. Write the value to a scratch file and read
  the file instead.
- **Find bash and python explicitly.**
  - Python's bare `bash` is WSL's. A Python subprocess must resolve bash through `tools/lib/resolve_bash.py`.
  - Shell code finds python through `tools/lib/resolve-python.sh`.
- **A shared file grows only by appending.** Where you add to a file dWitnessedBar also changed (`catalogue.toml`,
  `selftest-budgets.txt`, `SESSION-KICKOFF.md`), add your rows and change none of theirs, so the merge with its
  landing stays additive.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-1`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-1` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` stages rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-1-1-acceptance-ledger.md`
  in the pass commit. Give it one line per §6 criterion, each leading with a backticked token that criterion itself
  spells. Mark a criterion whose observation is a gate leg or a suite as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, plus the kit descriptors,
  the map's generated files and the build records, in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` before you stage it.
- **Re-stamp the kickoff manifest when you touch a watched file.** The manifest's `watch:` list names
  `tools/gate-legs.json`, so re-stamp it in the same commit: `bash skills/session-kickoff/manifest-check.sh --stamp`,
  or the stamp rule its header gives.
- **Run no gate leg, no suite and no bar.** Verify with a fixture or a probe of the code you changed.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`.
  Its values are `report` and `author-recorded`.

## Third dispatch (after rev-4) — what changed

- **Start from the saved code.** Pass 2 (`wf_e88edf82-25c`) completed the code for the twelve declared files and saved it as
  `C:/Users/d41ly/AppData/Local/Temp/claude/b3f6db677b077b04/0840beea-0651-4dc3-9fe7-f227915b6b42/scratchpad/unit1-work/TOOL-dQuietDisk-1.patch`.
  Apply it with `git apply`, then bring it to rev-4: `read_info`'s oid from `git rev-parse --verify --quiet`, and
  `git_env_leaks_py` inline with `derive_git_env`. Re-run your probes.
- **Do not run `--dispatch`.** Check 49 refuses every dQuietDisk dispatch until the `history-store selftest` leg exists
  in `tools/gate-legs.json`, which only your commit creates. Stay inside the declared set (row `244f9949`). It
  already holds the spec, `tools/govkit/registry.toml`, `tools/gate-legs.json` and the map's generated files.
- **S12 and AC13 (the shell-role widen) are owed to the main loop.** Do not write `memory/project/shell-role.txt` or
  a widen record. Right after your commit, the main loop runs the pass legs. The portability leg reds on the three
  rows, and the main loop widens them as an inline red fix. Mark AC13 owed in the ledger.
- **What your commit carries.** Spec rev-4 is in the working tree, uncommitted, and your pass commit carries it with
  the status flip. `memory/builds/dQuietDisk/spec/2026-11-20-spec-TOOL-dQuietDisk-7.md` is also modified in the
  working tree. Do NOT stage it: the main loop commits it after yours.
