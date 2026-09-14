# Brief — KICK-aReplayedCard-3, the engine consumes and appends

**Serves:** journal KICK-aReplayedCard-3

What this pass is handed: the unit's spec at rev-3, the build README, `skills/session-kickoff/SKILL.md`
at 18225 bytes under an 18432-byte gate (`bash tools/check-template-size.sh skills/session-kickoff/SKILL.md`
reads the margin; 207 B at base), and the writer's verbs as units 2 and 4 shipped them:
`--card --write` at every session start, `--card --replay` after a compaction, and
`--card --append --session <sid>` reading a body on stdin whose six sections and READY line are
the shape KICK-aReplayedCard-2's spec §4 declares, refusing a READY line whose `base` is not
`git rev-parse HEAD`, and rewriting the `tree —` cell to the tree it runs in. The wiring is live
in this worktree since 39df2b1a; the acceptance ledgers of units 2 and 4 under `build/` name the
exact bytes.

What it builds: three clauses of engine prose and a manifest re-stamp. No code.

What is not obvious:

- **The budget is the whole job.** Three clauses must fit 207 B of headroom, or you TRIM the Step 1
  batch prose the card now makes redundant to make room; do not touch any other step's wording
  than the spec's S1, S2, S3 and S4 name, and do not cross 18432 B — the gate is a bar leg.
  Measure with `wc -c` after every edit and record the final size in the ledger.
- **Step 1 consumes**: a card opening `orientation —` in context satisfies the node tag, the tree
  kind, the worktree count and the recent subjects; the engine still runs `git branch --show-current`,
  `git rev-parse HEAD` as the BASE, `status --short`, and the fast-forward on the default branch
  with a clean tree; the card's branch and BASE are never consumed. No card → the batch as today.
- **Step 5 appends, then commits**: the six sections (`## task`, `## manifest`, `## read`,
  `## records` with the `Recall terms used:` line, `## classes`, `## open`) and the READY
  micro-format go to `bash <check-script> --card --append --session <sid>` with `<sid>` from the
  card header in context and `base <sha>` the BASE Step 1 pinned; Step 2b's repair commit, when
  the audit found drift, is made AFTER that append and BEFORE the halt — and in Step 5b after the
  append and before continuing. State it in Step 5 by text; AC5 reads the sentence.
- **Step 2b leaves the §3 list alone**: it changes only WHEN its repair commits; the audit still
  runs at kickoff and the ratchet spec `memory/builds/aRatchetForge/spec/manifest-ratchet-spec.md`
  §4 is the text this reorders — say so in the spec's §10 if it is not already there.
- **AC1 and AC2 are the ORCHESTRATOR's, and even it cannot observe them in this run**: the
  installed `/session-kickoff` on this node is a junction to the PRIMARY tree's engine on `main`,
  and a session that could re-point it does not exist inside an unattended run. Write both lines
  in the OBSERVED form naming the observation — one kickoff in a session started after landing,
  with a card in context, whose transcript shows the reduced Step 1 batch and whose card ends with
  the READY line — and say in your return that they are owed at the first post-landing kickoff;
  the orchestrator parks them for the owner with the command.
- **AC5 you observe by text**: Step 5 and 5b state the repair-commit ordering, and
  `grep -n 'git commit'` over the inline code spans of Steps 0 through 4 is empty. AC3 is the size
  gate; AC4 is the ratchet.
- **The manifest owes `last-audit`** — `SKILL.md` is in `watch:` — with the delta line in the
  commit message; the body does not change, so `last-body-change` stays. Stamp sha =
  `git merge-base origin/main HEAD`. Run `bash skills/session-kickoff/manifest-check.sh` plain and
  `--staged` before committing.
- **The dossier `memory/map/features/session-kickoff.md`** is refreshed on touch; this is the only
  unit that writes it — say in one sentence that Step 1 consumes the card and Step 5 appends.
- **`tools/check-wiring.sh --check` will report `UNWIRED skill` after your edit**: the junction
  targets the primary's unedited copy and the arm compares installed against tracked. Expected,
  clears at landing; record it in the ledger, do not chase it.
- **The acceptance ledger** is `2026-09-14-build-KICK-aReplayedCard-3-1-acceptance-ledger.md`
  under `build/`, `**Serves:** journal KICK-aReplayedCard-3`, AC1–AC5, every backticked token on
  the bullet's first physical line.
- **Author with the Write tool, LF; the engine file is prose and the deny is live** — your commit
  passes on the absent-card rule with a witness line. Finish with the records: spec status CLOSED
  with today's date, `gen_build_index.py --write`, `git add -A`, the hygiene gate (minutes, never
  through `tail`), `python tools/check-spec-tokens.py`, `bash tools/check-template-size.sh
  skills/session-kickoff/SKILL.md`, and commit with the unit id in the subject. No push, no merge.
