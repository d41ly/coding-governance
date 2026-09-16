# Brief — TOOL-aReplayedCard-3, the resume section kicks off

**Serves:** journal TOOL-aReplayedCard-3

What this pass is handed: the unit's spec at rev-3 (CLEAN WITH FIXES at round 1, two folds since),
the build README, `tools/unattended/SKILL.template.md` whose `## Resume` section starts at line 661
and whose first `/session-kickoff` mention is at line 185 below the first `--preflight` at 175, its
render `.claude/skills/unattended/SKILL.md`, and the engine's Step 5b as `KICK-aReplayedCard-3`
left it: on a live non-terminal run-state file it emits the READY card, appends the six sections and
the READY line through `--card --append`, and continues.

What it builds: one step of prose in the template's `## Resume` section, after the reap and
re-schedule paragraphs and before `## Close`, and its render. Nothing else.

What is not obvious:

- **The step is one numbered instruction**: invoke `/session-kickoff`; Step 5b fires because the
  run-state file exists in a non-terminal phase, the READY card lands on the orientation card, and
  the run continues at the phase the record names. Say why in one sentence: a resumed session
  starts with no card, or a replay-written one, and its first commit would otherwise be the first
  durable act nobody oriented.
- **Order inside the section is the point**: after the paragraph that schedules the replacement
  keepalive and before `## Close`. AC1 reads that.
- **Check 18 of `tools/unattended/check-unattended.sh` anchors on FIRST occurrences**: the first
  `/session-kickoff` in the whole template must stay below the first `unattended.sh --preflight`.
  Line 185 is already the first mention and it stays; your addition sits near line 690. Check 20
  reads five section-scoped literals in the prompt path; touch nothing there.
- **The render is byte-compared**: re-render `.claude/skills/unattended/SKILL.md` from the
  template the way the kit does — `bash tools/unattended/adopt-unattended.sh` has the render verb;
  read its header for the spelling — and the `unattended skill wiring` leg is the gate. Do not
  hand-edit the render.
- **AC2 is the ORCHESTRATOR's, and it cannot observe it in this run**: it needs a fresh session
  and a scratch clone with a throwaway run-state file and its own keepalive, and the installed
  engine on this node is the primary's until landing. Write the AC2 line in the OBSERVED form
  naming the observation and say in your return that it is owed at the first post-landing resume;
  the orchestrator parks it for the owner.
- **AC3 and AC4 are yours**: `bash tools/unattended/check-unattended.sh` is a long leg — the
  design record's skeptic measured it past 100 s and unit 7 saw 16040 s in the ledger — so budget
  it, run it to a file, never through `tail`, and read its checks 12, 18 and 20 lines. If the
  whole leg is not affordable, run the checks' own predicates by grep as unit 7 did and say so in
  the ledger as a documented check; the push boundary's total run is where the leg binds.
- **The manifest owes nothing**: neither file is in `watch:`.
- **The dossier `memory/map/features/unattended.md`** is refreshed on touch, one sentence.
- **The acceptance ledger** is `2026-09-14-build-TOOL-aReplayedCard-3-1-acceptance-ledger.md` under
  `build/`, `**Serves:** journal TOOL-aReplayedCard-3`, AC1–AC4, every backticked token on the
  bullet's first physical line.
- **Author with the Write tool, LF; the deny is live** — your commit passes on the absent-card rule
  with a witness line. Finish with the records: spec status CLOSED with today's date,
  `gen_build_index.py --write`, `git add -A`, the hygiene gate (minutes, never through `tail`),
  `python tools/check-spec-tokens.py`, the wiring leg's argv from `tools/gate-legs.json` for
  `unattended skill wiring`, and commit with the unit id in the subject. No push, no merge.
