# Build brief — TOOL-dLoggedFlight-14, -16 and -20 to -27

**Serves:** journal TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27

This is what the building agent for any one of these ten units is handed, beyond its spec. Units 1 to
13 are CLOSED and their code is on this branch; these ten change that code. Read "Every unit", then
your own entry under "By unit", then "The pass". Your spec is the design and this file is the house
knowledge. Where the two disagree, the spec wins. A needed change goes into the spec first, as a rev
bump with its section 9 line.

## Every unit

- **Run no suite and no gate** (owner, 2026-09-13). The gate-guard hook denies any `selftest.py`,
  `*.test.sh` or `run-selftests.sh` invocation while this run's phase is before VERIFYING, and that
  includes `tools/runlog/selftest.py`. Do not work around it: no import of the suite module, no copy of
  it under another name. Write your arms and raise `ASSERTION_FLOOR` by your arm's assertion count. The
  main loop runs the suite once, at VERIFYING, and stages each arm RED there.
- **Observe your change directly.** Call the function your spec names, `build_run_model`,
  `render_record`, `verify` and the like, over a synthetic fixture, from a Python script you write to a
  file under the system temp directory and run with `python <file>`. Never run Python from a heredoc or
  stdin: on this node that loses an escape level, and a dash argument can run the wrong interpreter.
  Record in your acceptance ledger what you observed, and for each AC the break that stages its arm RED.
- **No journal or transcript time is committed** (owner, 2026-09-16). The committed record carries
  counts, commit shas and times read from git or the run-state file. Nothing in a fixture, an arm name
  or a tracked file comes from a real transcript, journal or store extract; fixtures are synthetic.
- **Never render this run's own record.** The local store holds a stale extract of this run's session,
  and a render before the build lands would write exactly the defect these units close.
- **Function names lead with a declared verb.** `.lexicon.conf` pins the offender count as an
  equality. The verbs are build, load, read, write, parse, render, resolve, check, scan, extract,
  measure, derive, seed, init, run, arm, add, remove, set and print. `append` is not a verb. Ask
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function` when unsure.
- **Python is stdlib only**, Python 3.12, no `unittest`. The suite's shape is `check(name, got, want)`,
  arms as functions, a printed assertion count and a floor.
- **A kit file names nothing outside itself by literal.** Derive the kit dir from `__file__`. A retired
  identifier is removed from every reader in the same unit: grep the kit, its README, the map dossier
  and the other open specs for the name before you delete it.
- **A carried-prefix count is raised by hand** in `tools/install-prefix-carried.txt`, with its reason
  extended, and only when the gate's own pattern matches the new literal.
- **A `project-owned` list takes file names, never globs.** A new runlog fixture is added by name to
  `tools/runlog/kit.toml`.
- **The rendered Skill is a render.** A change to `tools/runlog/SKILL.template.md` is re-rendered with
  `bash tools/runlog/adopt-runlog.sh --scaffold` and both files are committed together. Never edit
  `.claude/skills/runlog/SKILL.md` by hand.
- **A watched file needs the kickoff manifest re-stamped.** If pre-commit refuses over
  `memory/guides/SESSION-KICKOFF.md`, stamp its `last-audit` at `git merge-base origin/main HEAD` with
  your real local time and offset, and say in the commit message what changed.
- **Codebase map.** A new file or identifier a dossier claims is claimed in
  `memory/map/features/runlog.md`; regenerate with `python tools/codebase-map/gen_map.py --write` in the
  same commit. A retired identifier leaves the dossier in the same commit.
- **Kit versions do not move.** runlog is new in this build at 1.0. No unit here touches another kit;
  if yours finds it must, stop and say so in your return.
- **Line endings.** Read data files with `newline=""`; a new script or data path is pinned LF in
  `.gitattributes`.
- **The worktree is shared.** A spec-audit harness may be committing review records and spec folds in
  this worktree while you build. Stage explicit paths only, never `git add -A` or `git add .`. If a
  commit fails on `index.lock`, wait and retry. If the build README changed under you, re-read it and
  edit only your own roster row.

## By unit

Build in this order; each unit reads the landed code of the units before it.

- **16, freshness.** First. `extracted_at`, `check_extract_covers` and the `stale` state. Its AC4 pins
  an existing arm unedited; unit 22 later restates that pin, so do not pre-empt 22.
- **14, source order.** After 16. A live transcript is read before a store extract, on the named and
  the discovered path. AC7 counts `extract_session` calls: wrap the function inside the arm and restore
  it in a `finally`, never by editing `extract.py` for the test.
- **21, the commitment.** A digest and a line count, and `verify` recomputes from the time-ordered
  prefix. Land it before 22 and 20, which consume a commitment with no time.
- **24, the Summary window.** The git-only window the schema leg already derives, reused, not
  re-derived a third time. Before 25, 22 and 20.
- **25, the window's closer.** After 24. The closer names a terminal write its own commit carries, and
  its arms observe real models at each of the Skill's render placements. It removes the window loop
  from `test_record_ac4_classes` that 26 then works over.
- **26, derived fixture counts.** After 25. Every count and value the record arms assert over a shared
  fixture builder is derived from what the builder placed, on kinds the record keeps. Before 22.
- **22, the retirements.** The journal rows, the time columns and `scan_owner_times` retire, and every
  arm, vocabulary and floor reading them is rewritten by name. Grep the suite for each retired name
  before you call it done.
- **27, the withheld-rows fact.** After 22. Each retired kind is counted from a declared source, and a
  source the model did not read renders `-`, never `0`.
- **20, the source rule.** After 21, 24, 25, 26, 22 and 27. What it still owns after its audit is its spec's
  current rev; read its section 9 before its section 2.
- **23, the population arm.** Last. One arm over every time-bearing token a render writes, classes and
  slots read from `RECORD_SCHEMA`, and a fixture that reaches every conditional slot.

## The pass

1. Declare the write set with the driver's `--dispatch`. List every path the commit will carry,
   including this brief, the spec, the ledger, the regenerated map files, `memory/LIVE.md`,
   `memory/ledger/2026-09.md` and the build README.
2. Build.
3. Observe the change directly, per "Every unit". Run no suite and no gate.
4. Write the acceptance ledger at
   `memory/builds/dLoggedFlight/build/<date>-build-TOOL-dLoggedFlight-<n>-1-acceptance-ledger.md`,
   where `<date>` is the day you write it, with `**Serves:** journal TOOL-dLoggedFlight-<n>` and
   `**Evidences:** TOOL-dLoggedFlight-<n>`. One line per criterion,
   `- AC1 — \`<command or path>\` — <what was observed>`, with the backticked token on the `- ACn —`
   line itself. An AC whose observation is a suite arm or a gate leg is written as owed to the
   post-build run, naming the arm and its RED break, never as met.
5. Set the spec's status header to CLOSED and your row in the build README's authored roster table to
   CLOSED. Run `python tools/memory-tree/gen_build_index.py --write` and stage what it rewrote.
6. Commit with the subject `feat(dLoggedFlight): TOOL-dLoggedFlight-<n> — <the claim>`, with a 600000
   ms timeout, because the pre-commit hook runs longer than the default. Record a choice with no other
   home as a `Decided: <choice> — <why>` trailer beside `Co-Authored-By:`.
7. Run `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names.

## Never

- Run a suite, a gate leg or the merge bar, or any suite that was under `tools/unattended/` before
  this build.
- Push, merge, touch the primary tree, or use `--no-verify`.
- Use a bare `git stash`. The stash is shared with other sessions.
