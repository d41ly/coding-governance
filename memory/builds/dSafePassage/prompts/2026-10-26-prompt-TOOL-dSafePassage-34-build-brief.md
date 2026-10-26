**Serves:** journal TOOL-dSafePassage-34

# Build brief — TOOL-dSafePassage-34

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dSafePassage's build run; the spec run landed every spec and deferred every unit to it (README rule 1).
- The build order is 1, 3, 16, 20, 43, 7, 2, 4, 15, 11, 18, 19, 22, 24, 8, 12, 10, 17, 23, 25, 29, 30, 32, 6, 9, 13, 21, 27, 28, 33, 36, 37, 5, 26, 39, 40, 31, 34, 35, 41, 38, 42, 44, 45, 46, 47, 48, 50, 49, 52, 51, 57, 58, 53, 54, 55, 56, 59 (each `order` group sorted by its specs' `consumes-from` edges). Every unit before yours in that order is built and committed on this
  branch; read their code where your spec names it, never re-implement it. Your spec's §3 Edges name what you consume.
- The spec audit is closed: the owner stopped it after round 7 (`memory/builds/dSafePassage/prompts/2026-10-23-prompt-TOOL-dSafePassage-1-owner-audit-cap.md`), and your spec carries every fold and the 2026-10-24/25 owner fixes. Build what the spec says. A spec you cannot build as written is a DIVERGENCE hand-back, never an edit of the spec.
- The pinned base is `60d90cb71db51e651aa1c5efe3f6d48ba21a997d`, with dGroundRules landed on it. Your spec's `base 3708a705` is the spec run's; where the tree moved since, the code at
  this branch's HEAD is the truth, and a difference that changes what you must build is a DIVERGENCE.
- Writes stay in your `--dispatch --writes` paths and this build's folder (README, "Build-level rules").

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dSafePassage-34`, its trailer block carrying `Pass: TOOL-dSafePassage-34`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- The `--brief` and `--dispatch` verbs stage rows in `memory/builds/dSafePassage/RUN.md`: commit that file in your
  pass commit, or `brief-recorded` reds with no remedy but a history rewrite.
- Flip your spec's status header from `DEFERRED` to `CLOSED` in the pass commit, with a §9 line only where your spec's
  own text changed. If `gen_build_index.py --write` rewrites other files (README regions, `memory/LIVE.md`, other
  specs' records regions), commit every file it rewrote.
- A Tier-2 unit that closes owes its acceptance ledger in a `journal` record (`memory/HYGIENE.md`, "Acceptance
  ledger"): `memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-34-ledger.md`, one line per AC with the
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

- `--dispatch` takes ONE `--writes <path>` per path (`--writes a --writes b`); a space-joined list is refused by check 49, and the verb then re-runs the 3-5 min spec-token check. Your Tier-2 spec is `DEFERRED`: move it to `INPROGRESS` before your first product write, as the units before you did, and commit it only as `CLOSED`.
- `git commit` here runs a pre-commit hook that can take minutes: give the Bash call a 600000 ms timeout.
- Python written through a bash heredoc loses a level of backslashes; write scripts to a file under your scratch.
- A subprocess `bash` from Python is WSL's, blind to this worktree's git; call `git` directly.
- Read and write text with `encoding="utf-8"` and `newline=""` where a CR could matter; redirected stdout on this
  host is CRLF.
- A shipped kit file may not name an adopter, and a hook file may not spell `tools/<kit>/` as a literal.
- A new shell or Python function stales `memory/map/generated/symbols.json`; regenerate it in your pass.
- A new gotcha class needs a claim in a codebase-map dossier's gotcha-classes in the same commit.

## dSafePassage's own rules

- A deviation record's value is `report` or `author-recorded` (README, "Build-level rules"); write one per departure, in this build's `build/` folder, committed with the pass.
- Never move a blob `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --check dSafePassage` pins as an instrument; a pass that would is a DIVERGENCE hand-back.
- Your spec header's `advances TOOL-dSafePassage-14` stays `advances` when you flip it to `CLOSED`, unless this brief says you are the last unit.
