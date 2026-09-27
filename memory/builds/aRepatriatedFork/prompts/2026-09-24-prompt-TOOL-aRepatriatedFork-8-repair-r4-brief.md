# Gate repair brief R4 — the full bar at VERIFYING

**Serves:** journal TOOL-aRepatriatedFork-8

A repair pass under the aRepatriatedFork mandate, at VERIFYING.

Legs **pre-push run-log line** (`bash .githooks/pre-push.runlog.test.sh`), **shell hygiene**
(`python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt`) and **dead-path
carriers** (`bash tools/check-dead-paths.sh`).

- run-log: AC7 "the writer adds no external exec" counts one more `git` exec than its baseline, in
  all four modes. It was already red at c6513db0, before the closing-review folds, so it came from an
  earlier unit of this build (the hook's refusal-token or remote-resolution work); find which and
  remove the extra exec from the writer's path, or show it is not the writer's.
- shell hygiene: `tools/unattended/check-unattended.sh` measures 3 `<<<` sites against 2 declared.
- dead-path carriers: `STATUS.md` build-root mentions in `tools/memory-tree/README.md`,
  `check-memory-hygiene.sh` and its test (TOOL-aRepatriatedFork-10's grandfathering). A mention of a
  pattern is not a dead path; declare it the way the leg allows, or reword.

## How to repair

The run is at VERIFYING: the full bar ran once over `6ee9be2e` (`GATE_FULL=1 GATE_SELFTESTS=1`) and
these legs went RED. Each leg's full output is under `C:/projects/coding-governance/.git/worktrees/arepatriated-fork-build-e42158/gate-logs/`, one file per leg named after it.

- For each leg named above: read its log, then RUN THAT LEG ALONE by its argv (from
  `tools/gate-legs.json`) to reproduce at HEAD. At VERIFYING a single leg or suite may run; the
  WHOLE bar may not, and neither may `GATE_FULL`/`GATE_SELFTESTS`. Bound every command.
- Decide per failure whether this build caused it: compare against BASE `f8fdd873` in a
  `git clone --local --shared` of this worktree under a short `%TEMP%` path. A failure already red
  at BASE is not this build's: say so in `summary` with the evidence, and fix it only if the fix is
  small and inside a file this build already changed. Everything this build caused is fixed.
- Fix the CAUSE, not the assertion. An arm that pins text this build legitimately changed is
  updated to the new text; an arm that caught a real regression keeps its expectation and the code
  is fixed. Say which, per arm.
- Re-run the leg alone after the fix: it exits 0, or `summary` says exactly what still fails and why.
- Each fix folds into the OWNING unit's spec as a rev-N bump whose §9 line names "gate repair at
  VERIFYING" and the leg; the status header stays CLOSED. The owner is the unit whose commit
  introduced the regressed line (`git log -S` finds it).
- Before committing, all exit 0: `python tools/lexicon/lexicon.py`, `bash tools/check-install-prefix.sh`,
  `python3 tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills`.
  After committing: `python tools/govkit/govkit.py epoch --base f8fdd873`, `bash tools/check-kit-versions.sh`,
  `python tools/govkit/govkit.py selfcheck`, `python3 tools/memory-tree/check-arms.py --check`; a kit
  whose shipped bytes moved owes its version bump in every carrier. A staged watched file owes a
  `last-audit` re-stamp and a `Manifest delta:` line.
- Commit subject: `<owning unit id>: gate repair — <leg>`; several owners mean several commits.

## What to return

Per leg: reproduced at HEAD or not, caused by this build or already red at BASE (with the evidence),
the fix, and the leg's exit code after it. Name any leg you could not bring to 0.
