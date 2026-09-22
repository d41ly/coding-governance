**Serves:** journal DEPL-dGaugedVintage-4

# Acceptance ledger — DEPL-dGaugedVintage-4, check 5c

**Evidences:** DEPL-dGaugedVintage-4

- AC1 — `python tools/govkit/govkit.py selfcheck` — exits 0, and all eight drift-audit marker sites
  now read `1.8`: the five repaired plus the README and the two workflow harnesses.
- AC2 — `python tools/govkit/govkit.py selfcheck` — with `selftest.py`'s marker staged to `@9.9` the
  run exits 1 naming that file; restored, it exits 0.
- AC3 — `python tools/govkit/govkit.py selfcheck` — with `# gov:kit lexicon@9.9` appended to a file
  inside drift-audit's claim, the reverse arm reds: `entry 'lexicon' neither claims that path nor
  declares it in marker_carriers`.
- AC4 — `python tools/govkit/govkit.py selfcheck` — RED OBSERVED before the repair: the forward arm
  named all five stale files (`adopt-drift-audit.sh` at `@1.2`, and `drift_report.py`,
  `drift_signals.py`, `drift_signals.template.py`, `selftest.py` at `@1.4`) against constant `1.8`.
- AC5 — `python tools/govkit/govkit.py selfcheck` — an entry with a constant and an empty derived
  marker set is ANNOUNCED, not skipped. It named six: `check-wiring`, `codebase-map`,
  `kickoff-manifest`, `playbook`, `playbook-render`, `review-harness`.
- AC6 — amended rev-3 — rendered destinations are not in check 5c's population, measured False for
  four probes, so the criterion would have passed by absence. Recorded as a known gap in §6.
- AC7 — `python tools/govkit/govkit.py selfcheck` — with `drift-audit-code.js`'s marker staged to
  `@7.7` the run reds naming it, which proves the declared `marker_carriers` allowance really pulled
  that cross-entry file into drift-audit's basis. It is claimed by `review-harness`, so without the
  allowance no arm reaches it.

## What this ledger does not claim

Check 5c's population is each entry's claimed SOURCES plus its declared `marker_carriers`, minus
`*.test.sh`. It is NOT the tracked tree: a bare grep returns spec and review prose under
`memory/builds/**`, including this build's own records, and that set is self-referential. Rendered
destinations are outside it — see AC6.
