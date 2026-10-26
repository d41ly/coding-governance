**Serves:** journal TOOL-dGroundRules-16

# Build brief — TOOL-dGroundRules-16

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dGroundRules' build run; the spec run landed every spec and deferred every unit to it (README rule 1).
- The build order is 1, 11, 16, 2, 3, 4, 24, 5, 6, 14, 19, 26, 28, 65, 7, 8, 10, 9, 15, 17, 18, 20, 21, 22, 23, 25, 29, 27, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 57, 58, 61, 64, 54, 56, 59, 60, 62, 63. Every unit before yours in that order is built and committed on this
  branch; read their code where your spec names it, never re-implement it. Your spec's §3 Edges name what you consume.
- The spec audit is closed: the owner capped it at round 6, and your spec carries every fold. Build what the spec says. A spec you cannot build as written is a DIVERGENCE hand-back, never an edit of the spec.
- The pinned base is `3c2b69be4652ade1ec267f0ce0e3d99389531633`. Your spec's `base 3708a705` is the spec run's; where the tree moved since, the code at
  this branch's HEAD is the truth, and a difference that changes what you must build is a DIVERGENCE.
- Writes stay in your `--dispatch --writes` paths and this build's folder (README, "Build-level rules").

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dGroundRules-16`, its trailer block carrying `Pass: TOOL-dGroundRules-16`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- The `--brief` and `--dispatch` verbs stage rows in `memory/builds/dGroundRules/RUN.md`: commit that file in your
  pass commit, or `brief-recorded` reds with no remedy but a history rewrite.
- Flip your spec's status header from `DEFERRED` to `CLOSED` in the pass commit, with a §9 line only where your spec's
  own text changed. If `gen_build_index.py --write` rewrites other files (README regions, `memory/LIVE.md`, other
  specs' records regions), commit every file it rewrote.
- A Tier-2 unit that closes owes its acceptance ledger in a `journal` record (`memory/HYGIENE.md`, "Acceptance
  ledger"): `memory/builds/dGroundRules/build/2026-10-23-build-TOOL-dGroundRules-16-ledger.md`, one line per AC with the
  probe you ran and what it printed. Commit it with the pass.
- A departure from your spec once code has started is a `deviation` record (`memory/HYGIENE.md`, "Deviation records"),
  committed with the pass; never a silent difference.
- Bump no kit version: the lander mints versions at landing, and a branch owes none.
- A commit staging a file on the kickoff manifest's `watch:` list (`memory/guides/SESSION-KICKOFF.md`, its
  `manifest-audit` block) is refused by the pre-commit hook until that manifest's `last-audit` stamp is re-stamped in
  the same commit, with the delta line its stamp rule asks for. Put the manifest in your write set when you touch one.
- When the pre-commit hook refuses on a stale codebase map (`memory/map/generated/`), run the map generator it
  names and commit its output with your pass, declaring those paths in `--dispatch`. Regenerate nothing else.
- A spec held `DEFERRED` may refuse your product writes at the write gate: move its status to `INPROGRESS` first,
  then `CLOSED` in the pass commit.
- Run no gate leg, no `*.test.sh` suite, no merge bar. Verify each AC by the probe or fixture the spec names. A new
  suite arm goes in the suite file and on a `New arm:` line; the main loop observes it red and green at the close.

## Traps this repository has already paid for

- `git commit` here runs a pre-commit hook that can take minutes: give the Bash call a 600000 ms timeout.
- Python written through a bash heredoc loses a level of backslashes; write scripts to a file under your scratch.
- A subprocess `bash` from Python is WSL's, blind to this worktree's git; call `git` directly.
- Read and write text with `encoding="utf-8"` and `newline=""` where a CR could matter; redirected stdout on this
  host is CRLF.
- A shipped kit file may not name an adopter, and a hook file may not spell `tools/<kit>/` as a literal.
- A new shell or Python function stales `memory/map/generated/symbols.json`; regenerate it in your pass.
- A new gotcha class needs a claim in a codebase-map dossier's gotcha-classes in the same commit.
