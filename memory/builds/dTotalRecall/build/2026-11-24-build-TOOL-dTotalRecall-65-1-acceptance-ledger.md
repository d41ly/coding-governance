# TOOL-dTotalRecall-65 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-65
**Caused-by:** TOOL-dTotalRecall-65

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-5 over base
`cb72756eb` and ran each probe below on node a, 2026-11-24; a fixture is built under the system temp directory
and removed. §7's legs and its `New arm:` RED-first observations are owed to the close.

**Evidences:** TOOL-dTotalRecall-65
- AC1 — `CENSUS_KEPT_PATHS` — both spelled greps printed nothing, exit 1, and the `PROJECT_REGISTRY_EXTRA` grep printed `1` (DERIVED 2026-11-24, this probe).
- AC2 — `python record_causes.py --cause-writers` — its build-folder lines equal the base's byte for byte, `8 kept · 1 pinned · 0 red`, exit 0; `python record_kinds.py --check` prints the base's lines byte for byte, `deviations.py:380` `kept pinned instrument` among them, its reds the host's stray common-dir entries alone; `grep -c '^check_' census-kept-paths.txt` printed 9, the table's count at the base (DERIVED 2026-11-24, this probe).
- AC3 — `adopter-no-registry` — its check exited 0, both censuses read 0 rows, one `PASS` line, exit 0; with one engine-held row returned beside the registry's in the probe process it exited 1 (DERIVED 2026-11-24, this probe).
- AC4 — `kept-row-drained` — it and `kept-row-editable` each exited 1 with one `RED` line naming `census-kept-paths.txt` and the planted path; with the registry unread, and with the domain widened to `*`, in the probe process, each exited 0 (DERIVED 2026-11-24, this probe).
- AC5 — `ValueError` — raised, naming `census-kept-paths.txt` and `line 2` (DERIVED 2026-11-24, this probe).
