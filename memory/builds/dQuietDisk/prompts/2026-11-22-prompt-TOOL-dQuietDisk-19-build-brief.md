**Serves:** journal TOOL-dQuietDisk-19

# Build brief — TOOL-dQuietDisk-19

You build ONE unit from its spec. The spec is the contract. This brief adds only what the spec cannot know.

## Where the build stands

- **The build.** This is dQuietDisk's build run. Every product unit is terminal: orders 1 to 6 are built, 6 and 17
  are WONTDO and 15 is DEFERRED. Your spec is rev-5, re-grounded at `18948bf27`, with its F3 ruled (b).
- **The readings are committed.** B0 is in the record since `291aa99e4`. The main loop took A at `1d493fe43` and
  committed every A row and the `## Switches at A-off` section in `b57a5eeb7`. Take every number from the record's
  Readings table; never re-run the instrument, a suite or a leg.
- **What your pass writes**, all in `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-19-measurements.md`:
  the `### The instrument` heading line S1 names, the `## Comparison` table, the `## nicocares seed suite` section from
  the nicocares record the spec cites (read it read-only with `git -C C:/projects/nicocares/main show 7b9396cae:<path>`),
  the `## Owed by other units` line, and the Limits lines S6 and AC5 name, in the section order the spec's record
  table gives.
- **Read each owning unit's bound as built.** Quote it from that unit's spec at `HEAD`, CLOSED, not from an older rev.
  Where A-on misses a bound, write `no` and say so in a Limits line; never adjust a number.
- **Your commit.** Your pass commit ends with the charter's trailer,
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Traps on this node

- **Run no suite, no runner and no instrument.** Every reading is the main loop's and already committed.
- **Never write into nicocares** or any adopter, and never enter a `gov-upgrade` worktree. Reading a committed blob
  with `git -C <repo> show <sha>:<path>` is the whole of your access.
- **Derive every comparison cell by the spec's rules**, and show the arithmetic's inputs in the row as the spec says.
  Compute with Python, never by hand, and keep the script under the scratch root.
- **Cite code by symbol or blob.** In every record you write, cite code lines as `path#symbol` or blob-pinned, never
  as a bare `path:line`.
- **No here-string or heredoc fed from `$(...)`.** Write the value to a scratch file and read the file instead.
- **Find bash and python explicitly.** A Python subprocess resolves bash through `tools/lib/resolve_bash.py`; shell code
  finds python through `tools/lib/resolve-python.sh`.

## What the main loop needs from your commit

- **One pass commit.** Its subject names `TOOL-dQuietDisk-19`, and its trailer block carries
  `Pass: TOOL-dQuietDisk-19` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- **Commit `memory/builds/dQuietDisk/RUN.md` with the pass**, because `--dispatch` and `--brief` stage rows in it.
- **The status flip.** The spec's status is already `INPROGRESS`. Move it to `CLOSED` only in the pass commit, after
  every edit has landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging, and commit every
  file it rewrites.
- **The acceptance ledger.** Write `memory/builds/dQuietDisk/build/2026-11-22-build-TOOL-dQuietDisk-19-1-acceptance-ledger.md`
  in the pass commit. Give it one line per section 6 criterion, each leading with a backticked token that criterion
  itself spells. Mark a criterion whose observation is a suite run or an adopter check as owed to the main loop.
- **Write only inside the declared set.** The main loop declared the spec's Files touched, the build records and the
  index outputs in `--dispatch` before your spawn. A path beyond that list needs its own `--dispatch` with `--writes`
  before you stage it.
- **Record every deviation.** A change the spec did not state is a deviation record in `build/`, named
  `…-TOOL-dQuietDisk-19-deviation-1.md`. Its values are `report` and `author-recorded`.

