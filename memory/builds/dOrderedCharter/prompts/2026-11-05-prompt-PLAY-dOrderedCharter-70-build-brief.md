**Serves:** journal PLAY-dOrderedCharter-70

# Build brief — PLAY-dOrderedCharter-70

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's build run; the spec run landed every spec and deferred every unit to it (README rule 1).
- The owner ordered the build paused after unit 45 and the branch landed, so 29 units stay deferred and carried forward. The closing
  diff review (`memory/builds/dOrderedCharter/reviews/2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md`) promoted its
  findings to units 67, 68, 69 and 70, which build in that order, one at a time, because 68, 69 and 70 share files. Every earlier unit in
  this run is built and committed on this branch; read its code where your spec names it, never re-implement it. Your spec's section 3
  Edges name what you consume.
- The spec audit is closed: the owner capped spec review at two rounds
  (`memory/builds/dOrderedCharter/prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-owner-review-cap.md`), both ran in
  the spec run, and your spec carries every fold and the 2026-10-25 owner fork picks. Build what the spec says. A spec
  you cannot build as written is a DIVERGENCE hand-back, never an edit of the spec.
- The pinned base is `8bec4cefd957d194660a8d7c2916f420b7299074`. Your spec's `base ce13efbe` is the spec run's; where
  the tree moved since, the code at this branch's HEAD is the truth, and a difference that changes what you must build
  is a DIVERGENCE.
- Writes stay in your `--dispatch --writes` paths and this build's folder (README, "Build-level rules").

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-70`, its trailer block carrying `Pass: PLAY-dOrderedCharter-70` beside the attribution
  trailer. Stage explicit paths only, never `git add -A`.
- The `--brief` and `--dispatch` verbs stage rows in `memory/builds/dOrderedCharter/RUN.md`: commit that file in your
  pass commit, or `brief-recorded` reds with no remedy but a history rewrite.
- Flip your spec's status header from `DEFERRED` to `CLOSED` in the pass commit, with a history line only where your
  spec's own text changed. If `gen_build_index.py --write` rewrites other files (README regions, `memory/LIVE.md`, other
  specs' records regions), commit every file it rewrote.
- A Tier-2 unit that closes owes its acceptance ledger in a `journal` record (`memory/HYGIENE.md`, "Acceptance
  ledger"): `memory/builds/dOrderedCharter/build/2026-11-05-build-PLAY-dOrderedCharter-70-ledger.md`, one line per AC with the probe you
  ran and what it printed. Commit it with the pass.
- A departure from your spec once code has started is a `deviation` record (`memory/HYGIENE.md`, "Deviation records"),
  committed with the pass; never a silent difference.
- Bump no kit version: the lander mints versions at landing, and a branch owes none.
- A commit staging a file on the kickoff manifest's `watch:` list (`memory/guides/SESSION-KICKOFF.md`, its
  `manifest-audit` block) is refused by the pre-commit hook until that manifest's `last-audit` stamp is re-stamped in
  the same commit, with the delta line its stamp rule asks for. Put the manifest in your write set when you touch one.
- When the pre-commit hook refuses on a stale codebase map (`memory/map/generated/`), run the map generator it names
  and commit its output with your pass, declaring those paths in `--dispatch`. Regenerate nothing else.
- Your spec is held `DEFERRED`, which may refuse your product writes at the write gate: move its status to
  `INPROGRESS` before your first product write, then commit it only as `CLOSED`.
- Run no gate leg, no `*.test.sh` suite, no merge bar. Verify each AC by the probe or fixture the spec names. A new
  suite arm goes in the suite file and on a `New arm:` line; the main loop observes it red and green at the close.

## Traps this repository has already paid for

- `--dispatch` costs about 15 minutes a call. Declare everything in the first call: your spec, this brief's ledger, any deviation record,
  `memory/builds/dOrderedCharter/RUN.md`, `memory/builds/dOrderedCharter/README.md`, `memory/LIVE.md`,
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` and `memory/map/generated/`. A commit refused for an
  undeclared path costs another call.
- `--dispatch` takes ONE `--writes <path>` per path (`--writes a --writes b`); a space-joined list is refused by
  the dispatch spec-token check, and the verb then re-runs the 3-5 min spec-token check.
- `git commit` here runs a pre-commit hook that can take minutes: give the Bash call a 600000 ms timeout.
- Python written through a bash heredoc loses a level of backslashes; write scripts to a file under your scratch.
- A subprocess `bash` from Python is WSL's, blind to this worktree's git; call `git` directly.
- Read and write text with `encoding="utf-8"` and `newline=""` where a CR could matter; redirected stdout on this host
  is CRLF.
- A shipped kit file may not name an adopter, and a hook file may not spell `tools/<kit>/` as a literal.
- A new shell or Python function stales `memory/map/generated/symbols.json`; regenerate it in your pass.
- A new gotcha class needs a claim in a codebase-map dossier's gotcha-classes in the same commit.
- Unit 26's positional check reds new tracked text that cites a section by its sign, a hygiene check by its number,
  a method rule by its code, or a `path:line`: name them in words and cite code as `path#symbol`. Your pass must
  leave `python tools/playbook/gov_tag.py check` green.

## dOrderedCharter's own rules

- A deviation record's value is `report` or `author-recorded` (README, "Build-level rules"); write one per departure,
  in this build's `build/` folder, committed with the pass.
- Never move a blob `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --check
  dOrderedCharter` pins as an instrument; a pass that would is a DIVERGENCE hand-back.
- Your spec header's `advances PLAY-dOrderedCharter-38` stays `advances` when you flip it to `CLOSED`; you are not the last unit.
- The unattended kit's own self-test suites are WAIVED for this build's landing (README, "Build-level rules"); a
  criterion they would observe is named as owed with PLAY-dClosedLoop-12, never run.
