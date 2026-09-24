# Gate repair brief R2 — the full bar at VERIFYING

**Serves:** journal DEPL-aRepatriatedFork-13

A repair pass under the aRepatriatedFork mandate, at VERIFYING.

Leg **govkit selftest** (`python tools/govkit/selftest.py`): 68 arms FAILED. The log shows several
clusters; find each one's cause:
- many CONTROL/LIVENESS arms print only `govkit: precedence: ...` and expect GREEN: a scratch gov
  fixture now fails selfcheck, possibly on a new selfcheck arm this build added (TOOL-aRepatriatedFork-14
  7j2/7j3, TOOL-15 epoch, TOOL-16 shipped) or on the fan-out cap relay;
- `[-5] D1 every function that runs a shell command is DECLARED in SHELL_EXEC_SITES — undeclared
  spawn in: remove_wired_fragments, run_fragment_merges` (TOOL-aRepatriatedFork-11);
- `plan's write set equals the receipt rows carrying gov bytes — ['tools/codebase-map/map_extractors.py']`;
- `...the playbook file previews as a seed WRITE, not as an order` (DEPL-aRepatriatedFork-17's KEEP);
- `[-14] AC8 check output is BYTE-IDENTICAL across the S1 extraction`;
- the `[-PV]` F2 and R2 arms, one naming "not answer the effective fan-out cap".

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
