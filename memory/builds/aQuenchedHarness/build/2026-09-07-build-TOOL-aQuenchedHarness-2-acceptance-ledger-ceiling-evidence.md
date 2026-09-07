# Acceptance ledger — TOOL-aQuenchedHarness-2

**Serves:** journal TOOL-aQuenchedHarness-2

**Evidences:** TOOL-aQuenchedHarness-2

Tier-2 · node a · 2026-09-07. One line per numbered criterion, each naming the observation that
answered it. A line saying MET without an observation is a checkbox, which is why the gate refuses
one; a line saying NOT MET is equally a result and is recorded the same way.

- AC1 — MET, OBSERVED — `python tools/run-gates/derive-ceilings.py --report` prints one row per leg with its absolute reading and the headroom applied, plus the declared `max(120s, 1.0 x max)` margin and the node and window the readings came from.
- AC2 — MET at build time in `230971b8`; NOT re-observed in this session. The staged break — a ceiling lowered under its evidenced maximum plus headroom — was run when the check landed and is recorded in that commit.
- AC3 — MET at build time in `230971b8`; a re-run in a scratch tree with no `<git-dir>/gate-run` this session did not reproduce the exact `DEAD PROBE` wording and is recorded here as UNCONFIRMED rather than as a pass, because a probe arm that cannot be re-observed is the class this unit exists to close.
- AC4 — MET, OBSERVED — `tools/run-gates/ceiling-evidence.txt` carries a row for each leg with a reading and the count is derived, not typed: 37 of 99 legs backed over 2 retained runs.
- AC5 — MET, OBSERVED — `python tools/run-gates/derive-ceilings.py --check` exits 0 today over a manifest that grew by three legs during this build, and its report names the 62 unbacked legs rather than passing over them silently.
- AC6 — MET at build time in `230971b8`; NOT re-observed. The MONOTONE write — a lower observed maximum does not lower a committed row without `--reset` — is the behaviour that commit records.
