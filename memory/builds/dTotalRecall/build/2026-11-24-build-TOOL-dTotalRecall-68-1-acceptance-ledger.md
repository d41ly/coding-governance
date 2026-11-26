# TOOL-dTotalRecall-68 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-68
**Caused-by:** TOOL-dTotalRecall-68

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`c0a707782` and ran each probe below on node a, 2026-11-24; a fixture is built under the system temp directory
and removed. §7's legs are owed to the close.

**Evidences:** TOOL-dTotalRecall-68
- AC1 — `tools/govkit/registry.toml shrink-only` — printed, then the home, then `True True True`; the read-back exited 0 over nine rows, each ending in a TAB and `1`, and the canonical read exited 0 (DERIVED 2026-11-24, this probe).
- AC2 — `ratchet (never gains) · census-kept-paths · gained · <that key>` — printed after `[]` and the one `gained` tuple naming the third row's key, and `1` last (DERIVED 2026-11-24, this probe).
- AC3 — `ValueError` — raised naming `census-kept-paths.txt` and `line 2` over the three-field row; the source probe printed `True False` (DERIVED 2026-11-24, this probe).
- AC4 — `python record_causes.py --cause-writers` — its build-folder lines equal the base's byte for byte, `8 kept · 1 pinned · 0 red`; the alias probe lists `deviations.py line 380 · kept pinned instrument`, one kept (DERIVED 2026-11-24, this probe).
- AC5 — `a row with five is a pinned writer` — the probe printed 0, as it did for `by its five-field row` and `with two more fields`, and 5 for the `records` field phrase, over unit 66 rev-5, which this pass left as it stood (DERIVED 2026-11-24, this probe); the `git merge-base --is-ancestor` half is owed until unit 66 builds.
- AC6 — `kept-row-drained` — it and `kept-row-editable` each exited 1 with one `RED` line naming `census-kept-paths.txt` and the planted path; `reason-on-other-file` exited 1 with two, one naming the registry; the alias census's `marker-in-kept-script` and the `adopter-no-registry` plant each printed `PASS` (DERIVED 2026-11-24, this probe).
