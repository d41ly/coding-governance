# KICK-aMendedFleet-2 — the orientation card shows which unmerged remote refs share paths with this tree's branch

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams kickoff+tooling · ratified 2026-10-04 · order 77

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Unit 60 of this build gives an unattended run a cross-run overlap probe at `--preflight`: it joins
the paths this branch changes and declares with those of every unmerged remote-tracking ref, and
announces each ref that shares one. An attended session never runs a preflight, so it starts as
blind to the other runs as before. This unit puts the same probe on the orientation card: a
read-only driver verb, `--overlaps`, runs unit 60's probe against the LOCAL remote-tracking default
branch with no network, and the card prints its answer as one `overlaps —` cell. The report's
second card item, a note when the PATH CLI is older than the running session, is a different
mechanism and moves to a unit the run adds (§8 F1).

## 2. Scope (IN)

- **S1** — THE VERB. `tools/unattended/unattended.sh` accepts `--overlaps`, parsed inside the
  argument loop and exiting there as `--version` does, so no slug, keepalive or run-state file is
  read. It calls `print_overlaps`, which takes the clone's single remote, resolves
  `refs/remotes/<remote>/HEAD` with `git symbolic-ref` and `git rev-parse`, both local, sets the
  anchor `ASHA` to that tip, and calls unit 60's `check_cross_run_overlap` with an empty slug. It
  never calls `observe_anchor`, never runs `ls-remote` and never fetches. When the clone has other
  than one remote, or the symref is unset, it prints one line,
  `unattended: overlap probe UNAVAILABLE — <why>`, instead. It exits 0 on every path. The verb gets
  its header invocation line, which the leg's check 26 joins. Observed by AC1 and AC3.
- **S2** — THE EMPTY SLUG. `check_cross_run_overlap` given an empty slug reads its own declared
  paths from the non-terminal specs the `<anchor>...HEAD` diff changed, the rule unit 60's S3
  applies to a ref; given a slug it behaves exactly as unit 60 specifies. Observed by AC2.
- **S3** — THE CELL. `derive_overlaps_line` in `skills/session-kickoff/manifest-check.sh` prints
  the cell, and `render_card` prints it after `worktrees —` and any `drift —` cell and before
  `live —`, inside the startup part `CARD_PARTS_AWK` reads. With no `.unattended.conf` at the root
  it prints `overlaps — skipped: no .unattended.conf in this tree` and reads nothing. The driver is
  found by `resolve_kit_file unattended unattended.sh`, the body of `resolve_id_reader` generalised
  to a kit name and an anchor file, which `resolve_id_reader` then calls; the engine spells no path
  of the unattended kit. Nothing resolving prints
  `overlaps — skipped: no unattended driver resolves in this tree`. Observed by AC4.
- **S4** — THE BOUND. The read is `timeout -k 2 "$CARD_OVERLAP_BOUND" bash <driver> --overlaps`,
  default 10 s, with stdin from `/dev/null`, `GOV_RUNLOG=0` so no journal line is written, and
  stdout sent to a scratch file under `CARD_DIR` that is read and then unlinked, never captured by
  a command substitution. A fired bound prints
  `overlaps — skipped: --overlaps did not answer within <n>s, so overlaps are unknown, not none`.
  A node whose `timeout` lacks `-k` prints a `skipped:` line naming that and starts no read. Any
  other non-zero exit prints `overlaps — skipped: ` and the read's first line, cut at 160 bytes.
  `CARD_OVERLAP_BOUND` is an environment override for the self-test, like `CARD_CAP_BYTES`, and not
  an adopter knob. Observed by AC5.
- **S5** — THE FORM. The read's first line prints as `overlaps — <line>`, verbatim. Each later
  line prints indented by two spaces and cut at 200 bytes, at most `CARD_OVERLAP_ROWS`, 5, of them,
  then `  … <m> more` when more remain. The card parses nothing inside the probe's lines, so its
  wording is unit 60's alone. Observed by AC1.
- **S6** — `tools/unattended/README.md`, in the overlap probe's section, names `--overlaps`, that it
  reads the local default-branch tracking ref and never the network, and that the card calls it;
  the comment block above `render_card` names the cell; and the map dossier
  `memory/map/features/session-kickoff.md` gains one sentence on it. Observed by AC6.
- **S7** — Arms: in `skills/session-kickoff/manifest-check.test.sh`, the cell over a stub driver
  that answers, one that sleeps past a one-second bound, and a tree with no `.unattended.conf`; in
  `tools/unattended/unattended.test.sh`, `--overlaps` over a fixture remote, which check 26 also
  requires of a new flag. NOT OBSERVED by a criterion here: the suites run once at the close, and
  the arms are declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- The note when the PATH CLI is older than the running session. §8 F1 splits it into a unit the run
  adds; it reads no driver and no remote ref.
- Fetching, or reading the remote's own HEAD advertisement. The card's no-fetch contract stands;
  the cell reads the refs as of this clone's last fetch, which unit 60's line already says.
- A second implementation of the join in the kickoff kit. The card prints the driver's lines.
- Folding this read and the live `aGraftedHelix` build's `--claims` read into one driver start.
  Both cells start the driver once each; one combined verb is a follow-up once both have landed.
- Re-reading on `--card --replay`, which prints the session-start card as stored.
- Any edit to `skills/session-kickoff/SKILL.md`, which is at its byte cap and needs none.
- Bumping the kickoff and unattended kit versions, owed once at the build's close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-60` — `check_cross_run_overlap` and its announcement; without
  it the verb has nothing to call.

## 4. Design

### Evidence

Read at the worktree HEAD `efc4b0c9`, whose bytes under `skills/session-kickoff/` and
`tools/unattended/` equal base `7af5f564`'s.

- Unit 60's spec defines `check_cross_run_overlap` in `tools/unattended/unattended.sh`, called once
  at preflight, reading `ASHA` from `observe_anchor`, storing nothing, and printing a summary line
  that always appears plus one line per ref sharing a path. Its Edges hand the card line to this
  unit, "which owes the readable entry point the card calls".
- `observe_anchor` runs `git ls-remote --get-url` and reads the remote's HEAD advertisement, a
  network read; `--version` and `--check-commit` are parsed and exit inside the argument loop,
  before any slug is read, the shape S1 copies.
- An unknown-argument call of the driver took 2.3 s wall on node a, which is its startup: the
  script is about 10,600 lines and resolves its generated indexes through Python before the loop.
  `git for-each-ref --no-merged=origin/main --no-merged=HEAD` over `refs/remotes/origin/` took
  0.05 s and listed two refs; one `git diff --name-only` per ref took about 0.06 s. PINNED,
  measured 2026-10-04.
- The card was budgeted at about 1.6 s quiet by `KICK-aReplayedCard-1`'s design record, and
  `TOOL-aReplayedCard-7` records about ten git spawns per write. No gate grades the wall.
- `git symbolic-ref -q refs/remotes/origin/HEAD` answers `refs/remotes/origin/main` on node a; a
  clone made by `git clone` sets it, a remote added by hand does not.
- The live `aGraftedHelix` build's unit 2, unbuilt on its branch at the date, specifies the same
  generalisation under the same name and signature, `resolve_kit_file <home> <anchor>`, the same
  `timeout -k 2` read with stdin from `/dev/null` and `GOV_RUNLOG=0`, and a `claims —` cell
  directly below `live —`. S3 and S4 copy those names so the later reconcile is one helper, and
  this cell sits above `live —` so that build's adjacency criterion survives.
- `resolve_id_reader` resolves the memory-tree id reader through `resolve_kit_dir` from the
  script's directory, then the repo root, then the one tracked copy `git ls-files` names.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `print_overlaps` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest print_overlaps --as sh.function` answered OK |
| `derive_overlaps_line` | shell function | `sh.function`; the lexicon answered OK |
| `resolve_kit_file` | shell function | `sh.function`; the lexicon answered OK |
| `--overlaps` | driver flag | none |
| `CARD_OVERLAP_BOUND`, `CARD_OVERLAP_ROWS` | card constants | not graded |
| `overlaps —` | card cell | none |

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/README.md`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/map/features/session-kickoff.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The card joins the refs itself.** It would be a second spelling of unit 60's join, its shared
  record and generated index exclusions and its marker filter, in another kit.
- **Preflight writes its announcement to a file the card reads.** Only an unattended run preflights,
  so the file would describe one run's branch from whenever it last started, not this tree's.
- **The card sources the driver's library.** The probe lives in the driver and needs the shared
  records and generated indexes the driver resolves at startup; sourcing that is reading another
  kit's internals.
- **Render the cell in the kickoff body.** The body is authored, and the engine is at its byte cap.

## 5. Production-readiness checklist

- security — reads local refs and objects only, through a tracked driver the resolver finds in this
  repository; the read's output is printed, never evaluated; the scratch file lives under the git
  dir and is unlinked after the read.
- perf / scale — one driver start, about 2.3 s on node a, plus unit 60's per-ref spawns, bounded at
  10 s; §8 F2 records why the card's budget grows by that.
- error / empty / loading states — the four `skipped:` forms and the UNAVAILABLE line; none changes
  the card's exit status.
- observability — unit 60's summary line always prints, so a clean answer reads differently from a
  read that did not run.
- risks — a session opened on the default branch shares no path with anything and reads the
  one-line zero; refs are as of the last fetch, which the line says.
- testing — AC1 to AC6 here; the arms in S7.
- migration — N/A: a new verb and a new cell; nothing stored changes shape.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When, under a short `%TEMP%` path, a bare repository is cloned from the unit's tip, a
  second clone pushes a branch whose one commit edits `tools/runlog/runlog.py`, and a third clone
  fetches, commits an edit of the same file on its own branch, and runs
  `bash skills/session-kickoff/manifest-check.sh --card --write --session t77a`, stdout carries one
  line opening `overlaps — unattended: overlap probe` and, indented beneath it, a line naming the
  pushed branch with `tools/runlog/runlog.py` tagged `diff`, both above the `live —` line.
  Red when: the `derive_overlaps_line` call is staged out of `render_card` and no `overlaps —` line
  prints, or the cell lands after `recent —`.
  cost: about a minute on node a; the clones are the only things written.
- **AC2** — When, in that third clone, the edit is reverted and a commit instead adds one `SPECCED`
  spec under a fixture build whose Files touched names `tools/runlog/runlog.py`, and
  `bash tools/unattended/unattended.sh --overlaps` runs, stdout names the pushed branch with that
  path; when the spec's status is flipped to `WONTDO`, the summary line reports no shared path.
  Red when: an empty slug reads no own declared paths, or a terminal spec still declares.
- **AC3** — When `git remote set-head origin -d` runs in the third clone and
  `bash tools/unattended/unattended.sh --overlaps` runs there, stdout is one line carrying
  `overlap probe UNAVAILABLE` and the exit status is 0; and while the clone's remote URL names a
  path that does not exist, the verb still answers from the local refs with exit 0.
  Red when: the verb reaches the network, or a missing anchor reads as no overlap.
- **AC4** — When the third clone's `.unattended.conf` is deleted in its working tree and the card is
  written under a new session id, the cell reads
  `overlaps — skipped: no .unattended.conf in this tree`; and when
  `grep -n "tools/unattended" skills/session-kickoff/manifest-check.sh` runs in this tree, it prints
  nothing.
  Red when: the card reads a driver in a tree that never adopted the kit, or spells its path.
- **AC5** — When `CARD_OVERLAP_BOUND=1` is exported and a stub driver that sleeps five seconds is
  the one the resolver finds, the card write exits 0 within about four seconds and the cell reads
  `overlaps — skipped: --overlaps did not answer within 1s`.
  Red when: a hung driver holds the session start, or a fired bound reads as no overlap.
  fixture: the stub replaces the third clone's tracked driver in its working tree only.
- **AC6** — When `grep -n -- "--overlaps" tools/unattended/README.md` and
  `grep -n "overlaps —" memory/map/features/session-kickoff.md` run, each hits the new text.
  Red when: a verb or a cell ships that its README or dossier never names.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `unattended kit gate` · `unattended skill wiring` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `line length` · `kit epoch (shipped bytes move, the version moves)`

New arm: `skills/session-kickoff/manifest-check.test.sh` · covers AC1 AC4 AC5 · a stub driver that answers, one that outlives a one-second bound, and a tree with no `.unattended.conf`, staged red by deleting the `derive_overlaps_line` call · none

New arm: `tools/unattended/unattended.test.sh` · covers AC2 AC3 · `--overlaps` over a fixture remote with an overlapping branch, a spec-only branch and an unset remote HEAD, staged red by making `print_overlaps` call `observe_anchor` · none

## 8. Open questions

- **F1** — Is the roster's unit one mechanism or two?
  The roster names the overlap cell and a note when the PATH CLI is older than the running session.
  The cell needs a driver verb in the unattended kit, a bounded read and unit 60's probe; the note
  needs one version comparison inside the card and no other kit. They share no source, no write in
  the unattended kit and no criterion, and unit 60's Edges hand THIS unit the readable entry point,
  so the overlap cell stays here.
  RESOLVED (agent, 2026-10-04, delegated): split — the stale-CLI note, the card comparing the PATH
  `claude --version` against the running session's version as unit 61 reads it from `AI_AGENT`,
  moves to a new unit the run adds. Unit 61's Non-goals name unit 77 for that note and owe a
  pointer update when the run adds it.
- **F2** — May the card's session-start cost grow by a driver start?
  Options: grow it, bounded at 10 s; keep the 1.6 s budget and drop the cell; compute the join in
  the card. The third is a second spelling of unit 60's join; the second leaves attended sessions
  blind, which is the report's finding. No veto applies: the verb is a read-only flag of an
  existing CLI and opens no network, write or security surface, and the budget is a design-record
  figure no gate grades.
  RESOLVED (agent, 2026-10-04, delegated): grow it, bounded at 10 s, per S4; the measured start is
  2.3 s on node a.
- **F3** — Which anchor does the card's probe use?
  Options: the remote's HEAD advertisement, as preflight observes it; the local remote-tracking
  default branch. The first is a network read the card's contract refuses; the refs the probe reads
  are local and as of the last fetch either way, so a local anchor is consistent with them.
  RESOLVED (agent, 2026-10-04, delegated): the local `refs/remotes/<remote>/HEAD` target, per S1.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 77, report items [B#10] and
  [B#40], unit 60's spec and Edges, the live `aGraftedHelix` build's unit 2 spec read from its
  branch, and timings of the driver's startup and the ref reads on node a.

## 10. Reuse audit

The seams extended are unit 60's `check_cross_run_overlap`, called rather than copied, the driver's
in-loop verb shape that `--version` uses, and in `skills/session-kickoff/manifest-check.sh` the
`render_card` cell list and `resolve_id_reader`, whose body becomes `resolve_kit_file`, spelled as
the live `aGraftedHelix` build's unit 2 spells it. `python tools/codebase-map/reuse_lookup.py "list
unmerged remote branches that change the same paths as this tree's branch"` returned name-stem
neighbours, among them `attribute_paths` in `tools/codebase-map/map_lib.py`, `branches` in
`tools/memory-tree/check-arms.py` and `check_paths_never_lost` in the govkit, none of which reads a
remote ref; it prints `unscanned layers: .sh`, so `git grep -n "no-merged"` over `tools/` and
`skills/` was the shell probe, and it found nothing at base. Recall returned unit 60's spec, whose
probe this calls, `KICK-aReplayedCard-1`, the card's no-fetch contract that S1 keeps, and
`TOOL-aReplayedCard-7`, the card's spawn cost that §8 F2 weighs. Where the report and the tree
disagree: the report placed one probe at preflight and on the card; unit 60's spec covers the
preflight half only and leaves the card half's entry point to this unit. The engine today names the
unattended kit only in a comment citing `<prefix>/unattended/check-unattended.sh`, which AC4's grep
does not match.

Recall terms used: `python tools/memory-recall/query.py "how does the session card learn which
other runs or remote branches touch the same files" --terms "orientation card overlap unmerged
remote refs claims cross-run concurrent runs files touched session start driver verb bounded"`
