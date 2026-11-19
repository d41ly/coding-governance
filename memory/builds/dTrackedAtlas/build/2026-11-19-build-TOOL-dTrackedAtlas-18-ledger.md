# TOOL-dTrackedAtlas-18 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-18

No merge bar, gate or self-test suite ran in this pass. Every criterion was observed by the spec's own
command from the worktree root at the pass's base `b1b9c9b61` and after the edits, with `$PY` the
interpreter `tools/lib/resolve-python.sh` resolved and the agent markers `AI_AGENT` and `CLAUDECODE` set
as the agent's shell sets them. Each red was observed in `$F`, a clone of the worktree's branch at
`b1b9c9b61` under `%TEMP%/ta18fx`, so the reds read the tree before this unit on the real packets, the
real door and the real instrument, and no tracked file was edited to stage a red. The clone was removed
after the last red, and the real repository's refs were never written. Every capture sat in the run's
scratch directory.

The first `--repin` start ran under a bound too short for the measured pace and was stopped after it had
written one packet, dTrueNorth's; that packet was restored with `git checkout --` before the second start,
as section 4 provides for a partial loop, so the run AC1 grades is the second, from the restored base.

**Evidences:** TOOL-dTrackedAtlas-18
- AC1 — `"$PY" "$PACKET" --repin schedule.py` exited `0` after `2 h 33 min` (`10:47:20Z` to `13:19:59Z`) and printed `22` lines opening `packet: `.
  Each of the `22` read `packet: <slug> · $SCHED pinned 5aa5421e265b -> 6184e5717b59 · <packet path>`, one per chain build in the order `read_tree` lists them, so `$NEW` at this HEAD is the measured `6184e5717b5909ebff84695a6d317548b6ab2ff5` (DERIVED, `git rev-parse HEAD:$SCHED`).
  No line opened `packet: owner repin`, so the guard found no live chain run at this branch, as section 4 measured.
  Red: in `$F` with `phase: BUILDING` appended to `memory/builds/dWitnessedBar/RUN.md`, the same call in this agent's shell exited `1` and printed the one line `packet: refused: --repin is the owner's, and inside a chain run only an owner at a console runs it: an agent's call (AI_AGENT, CLAUDECODE set in its environment): memory/builds/dWitnessedBar/RUN.md (phase BUILDING)`.
  `git -C "$F" status --porcelain` then listed ` M memory/builds/dWitnessedBar/RUN.md` alone, no packet.
- AC2 — `grep -l` for the line `- instrument: $SCHED blob $NEW` over `$PACKETS` listed `22`, and `grep -l` for `$OLD` over them listed `0`.
  `git diff -U0` of the base against the tree over `$PACKETS`, filtered to removed lines opening `- instrument:`, showed the schedule's line `22` times and no other instrument's.
  Red: the same two greps over the packets at `b1b9c9b61` (each read by `git show`) counted `0` and `22`.
- AC3 — `"$PY" tools/chain-packet.py --check <slug>` for each of the `22` slugs exited `0` in `17 s` to `24 s` each, every run printing `byte compare green`, `completeness 0 findings` and `pin arm 7 instruments, 0 findings`, with an empty stderr, so no line opening `chain-packet:`.
  Red: in `$F`, the door's `--check dPlacedRequest` exited `1` after `540 s` with `byte compare red`, the six ask-arm findings for `PLAY-dClosedLoop-33` to `-38`, and `pin arm: instrument $SCHED moved: pinned 5aa5421e265b, HEAD holds 6184e5717b59`.
  The same red was observed beyond the criterion for `19` more slugs in `$F`, each exiting `1` with `byte compare red` and that pin-arm line; `--check dCalibratedLens` in `$F` met its `560 s` bound and was skipped, and dConvergedCharter's red was not run.
- AC4 — `"$PY" tools/chain-packet.py --check dPlacedRequest > "$X/door.out" 2> "$X/door.err"` exited `0` in `19 s`; `"$PY" "$PACKET" --check dPlacedRequest > "$X/inst.out"` exited `0` in `373 s`.
  `cmp "$X/door.out" "$X/inst.out"` found them identical, `261` bytes each (DERIVED, `wc -c`), and `"$X/door.err"` held no line opening `chain-packet:`.
  `"$PY" tools/chain-packet.py --parity dPlacedRequest` exited `0` in `393 s`, printing `chain-packet: parity dPlacedRequest · identical · 56017 bytes · <packet path>`.
  Red: in `$F`, the door's `--check dPlacedRequest` wrote the stderr line `chain-packet: shortcuts off, running the instrument as it stands — schedule: blob 6184e5717b59, read against 5aa5421e265b`, and `--parity dPlacedRequest` exited `2` printing that line alone.
- AC5 — the probe calling `d.scan_moved(d.resolve_instruments())` over `tools/chain-packet.py` printed `[]`.
  Red: the same probe in `$F` printed `['schedule: blob 6184e5717b59, read against 5aa5421e265b']`.
- AC6 — the probe wrapping the module's `git` and calling `tree_state('HEAD', {'dDeclaredLoop': []})` printed `0` with `$SCHED`, and `104` with `git show "$OLD"` written to `$X/schedule-old.py` (PINNED at `b1b9c9b61`).
  `grep -n -B3 "\"schedule\": \"$NEW\"" tools/chain-packet.py` showed lines `92` to `94` naming `set_reads`, `tree_state` and the chain build-state derivation.
  Red: at `b1b9c9b61` the comment above the `"schedule"` entry names `git("ls-tree", "-r", "--name-only", ref, <folder>)` and `git("show", f"{ref}:{p}")`, the two calls the probe at `$SCHED` counts as `0`.
- AC7 — `git diff --stat` of the base against the tip over `tools/` lists `tools/chain-packet.py` alone, `4` lines in and `4` out, and `git diff -U0` over it shows the one hunk `@@ -92,4 +92,4 @@ INSTRUMENT_BLOBS = {`: the `"schedule"` entry and its three comment lines.
  Red: in `$F`, this pass's file with one staged edit to the docstring of `set_reads` made `git diff -U0` show a second hunk, `@@ -190 +190 @@ def set_reads(packet, tree_lib):`, and `git diff --stat` count `5` lines in and `5` out; the clone's file was restored after.

Owed to the close: the plain bar, whose legs section 7 names; `chain-packet self-test` stays held under
ask `TOOL-dTrackedAtlas-19`, its arms CP3 to CP9 UNVERIFIED at this blob. No suite arm is added, so no
`New arm:` observation is owed.
