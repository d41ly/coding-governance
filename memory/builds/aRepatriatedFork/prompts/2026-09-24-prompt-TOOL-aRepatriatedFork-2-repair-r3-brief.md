# Gate repair brief R3 — the full bar at VERIFYING

**Serves:** journal TOOL-aRepatriatedFork-2

A repair pass under the aRepatriatedFork mandate, at VERIFYING.

Legs **hook destinations** (`bash tools/check-hook-destinations.sh`) and its **self-test**
(`bash tools/check-hook-destinations.test.sh`), **drift-audit selftest**
(`python tools/drift-audit/selftest.py`), **codebase-map kit selftest**
(`python3 tools/codebase-map/selftest.py`), **spec-tokens self-test**
(`bash tools/check-spec-tokens.test.sh`) and **process-monitor adopter selftest**
(`bash tools/process-monitor/adopt-process-monitor.test.sh`).

- hook destinations: `tools/memory-recall/recall-opened.fragment.json` is now `{here}`-shaped
  (TOOL-aRepatriatedFork-2 S4) but `tools/memory-recall` is not the home of a kind=flat descriptor,
  so the gate says the hook arrives nowhere. Decide whether the gate's rule or the fragment is wrong,
  against what govkit actually lands at an adopter.
- drift-audit: 17 arms fail with ".lexicon.conf is present but its kit is not importable here":
  the lexicon lookup moved onto `resolve_kit_dir` and the fixture no longer resolves it.
- codebase-map: "the installed gate and its template have diverged; 14515 vs 14613 bytes".
- spec-tokens: "AC4 live keys :: refused or unmatched: ['pre_push_bar_selftest.py']" and a manifest
  suite invocation parity arm.
- process-monitor: `test_hung_census_does_not_block_the_hook (returned in 2s; the census never ran)`;
  the census argv was re-derived by TOOL-aRepatriatedFork-2 S2. Backlog row TOOL-dGatedProse-12 records
  OTHER process-monitor arms red on main for environmental reasons; check whether this one is new.

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
