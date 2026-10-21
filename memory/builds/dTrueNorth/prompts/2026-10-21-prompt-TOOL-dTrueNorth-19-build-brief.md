**Serves:** journal TOOL-dTrueNorth-19

# Build brief — TOOL-dTrueNorth-19

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- The build order is 1, 2, 3, 11, 15, 5, 13, 14, 4, 6, 9, 10, 12, 8, 17, 18, 19, 16, 20, 7. Every unit before yours in that order is built and committed on this branch; read
  their code where your spec names it, never re-implement it. Your spec's §3 Edges name what you consume.
- The spec audit is closed (two rounds, the owner capped it at two). Build what the spec says. A spec you cannot
  build as written is a DIVERGENCE hand-back, never an edit of the spec.
- The pinned base is `271aa59defcb695133a50a49dc07650f9058a930`.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dTrueNorth-19`, its trailer block carrying `Pass: TOOL-dTrueNorth-19`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- The `--brief` and `--dispatch` verbs stage rows in `memory/builds/dTrueNorth/RUN.md`: commit that file in your
  pass commit, or `brief-recorded` reds with no remedy but a history rewrite.
- Flip your spec's status header from `OPEN` to `CLOSED` in the pass commit, with a §9 line only where your spec's
  own text changed. If `gen_build_index.py --write` rewrites other files (README regions, `memory/LIVE.md`, other
  specs' records regions), commit every file it rewrote.
- A Tier-2 unit that closes owes its acceptance ledger in a `journal` record (`memory/HYGIENE.md`, "Acceptance
  ledger"): `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-19-ledger.md`, one line per AC with the
  probe you ran and what it printed. Commit it with the pass.
- If yours is the first unit of this build to change a kit's shipped bytes, bump that kit's version in its
  `kit.toml` and its version marker lines, as `python tools/govkit/govkit.py epoch --base 271aa59defcb695133a50a49dc07650f9058a930`
  would demand. A later unit touching the same kit does not bump again.
- Run no gate leg, no `*.test.sh` suite, no merge bar. Verify each AC by the probe or fixture the spec names. A new
  suite arm goes in the suite file and on a `New arm:` line; the main loop observes it red and green at the close.

## Traps this repository has already paid for

- `git commit` here runs a pre-commit hook that can take minutes: give the Bash call a 600000 ms timeout.
- Python written through a bash heredoc loses a level of backslashes; write scripts to a file under your scratch.
- A subprocess `bash` from Python is WSL's, blind to this worktree's git; call `git` directly.
- Read and write text with `encoding="utf-8"` and `newline=""` where a CR could matter; redirected stdout on this
  host is CRLF.
- A shipped kit file may not name an adopter, and a hook file may not spell `tools/<kit>/` as a literal.
- A new gotcha class needs a claim in a codebase-map dossier's gotcha-classes in the same commit.

