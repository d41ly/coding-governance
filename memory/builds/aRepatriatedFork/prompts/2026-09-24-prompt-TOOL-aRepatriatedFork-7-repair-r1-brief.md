# Gate repair brief R1 — the full bar at VERIFYING

**Serves:** journal TOOL-aRepatriatedFork-7

A repair pass under the aRepatriatedFork mandate, at VERIFYING.

Legs **unattended-build self-test** (`bash tools/workflows/unattended-build.test.sh`) and **kit
placeholders** (`python tools/check-kit-placeholders.py`).

- unattended-build self-test: the PV-* arms render the protocol pair and the harness at a `scripts/`
  layout and fail with "the harness did not return: Node.js v22.22.3" and missing `rendered ...`
  lines. The likeliest cause is the closing-review residual (b) fold, which made the parity renderer
  take FANOUT_CAP from `check-verifier-fanout.sh --print-cap` relaying `agent-cap.js --print-cap`;
  in a fixture that lacks the hooks kit, or where node prints a banner, that relay may fail. Also
  `PV-R2-3 ...naming the protocol it skipped` and `PV-AC12 nested`.
- kit placeholders: `tools/memory-tree/HYGIENE.template.md` spells `ARMS_FLOORS=<value>`, a key its
  own kit's conf declares, so gov's value ships to every adopter; render it through a placeholder.

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
