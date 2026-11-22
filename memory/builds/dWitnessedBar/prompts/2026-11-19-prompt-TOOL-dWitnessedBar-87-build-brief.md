**Serves:** journal TOOL-dWitnessedBar-87

# Build brief — TOOL-dWitnessedBar-87

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 42.
- Built so far through order 42's first unit: every unit up to and including 4, 25, 40, 23, 42, 3, 44, 5, 41, 55, 8, 1, 59, 30, 29,
  7, 21, 6, 2, 43, 51, 56, 57, 58, 60, 62, 63, 64, 65, 66, 69 (`9ff80bb15`: `read_green_file` reads with one `IFS= read -r` loop and strips one CR, `read_tag_lines` splits on LF and strips one CR), 68 (`52bcf7599`), 67 (`af84e1a7a`: section `2o` fixtures built with `-c init.defaultBranch=master init --ref-format=files` under exported `GIT_CONFIG_NOSYSTEM`/`GIT_CONFIG_GLOBAL`), 70 (`0890c99d1`: the AC12 canary), 71 (`2972b3755`), 72 (`fa536b7cd`), 74 (`6a12d559c`: `check_cr_reached` and its liveness variant, with `rgf_why`), 75 (`5b7349498`: the canary's failure line names `rgf_what`), 73 (`563d828df`), 76 (`3596751cf`: `CANARY_KEYS`, `check_canary_keys` and one liveness loop over the keys), 77 (`18907b769`), 79 (`b9326245e`: `check_key_variant`, called for a tail and a length variant), 80 (`c0310ecd8`: the tail call passes `${_rg_v%?}x`), 81 (`778c11528`: records only) and 78 (`0e5103294`: `read_inherited_green`, the gov canary guard widened to `.githooks/pre-push`). Unit 28 (order 30) is deferred
  against asks TOOL-dWitnessedBar-101 to -103 and is not built. This spec, rev-5, was re-grounded at `0f92d2842`; it writes records only: two other units' acceptance ledgers (76 and 81) and its own. It mints no function and touches no code file; a staged break runs in a scratch copy of the suite under the scratch directory, never in the tracked suite.
- This unit closes order 42 and builds alone; nothing else is in flight in this working tree: commit directly here.
- The full `memory hygiene` leg is red at base on checks 13 and 15 from other records, and whole-tree spec tokens on one
  aMendedLedger spec; the main loop owns those at the close. Any other red is this unit's to fix.
- Cite code lines in every record you write as `path#symbol` or blob-pinned, never a bare `path:line`, fixture text
  included. Write no numeric fact without an id, a path:line, PINNED or DERIVED on its line.
- On this node bash 5.3.9 turns a `$'\r'` written inside `$(...)` into an empty string: a CR test inside a subshell
  uses a variable set outside it, as unit 70's `rgf_crb` does. Widen a shell-role row with `ratchet.py widen`, never
  by hand, and keep its TAB-separated columns.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-87`, its trailer block carrying `Pass: TOOL-dWitnessedBar-87`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-87-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
