# TOOL-aMendedFleet-92 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-92

**Evidences:** TOOL-aMendedFleet-92
- AC1 — `bash tools/unattended/check-unattended.sh --emit-ceiling` — exited 2 in 0.19 s naming the retirement of the old ceiling key, and `grep -n '^RETIRED_CONF_KEYS=' tools/unattended/check-unattended.sh` printed line 2836 naming `UNDECLARED_WRITE_CEILING`; nothing in this unit touched either
- AC2 — `unattended: check 23 fleet — 1 undeclared write(s)` — a scratch slice of the kit-gate suite inside the kit dir, its prologue plus the two per-run arms and the three new fleet arms, passed 11 assertions; the line read `over tRun=1` once; with the fleet `printf` staged out the same slice redded the new arms three times while the per-run arms stayed green
- AC3 — `over none` — the same slice's arm B read `0 undeclared write(s) over 1 graded pass(es) in 1 record(s) · budget 0 per run · over none`, and arm C, a derived-LANDED-only population, printed no fleet line; with the record counter staged above the derived-LANDED exclusion, arm C redded on the unexpected line
- AC4 — `sed -n 1,40p tools/unattended/check-unattended.sh` — grepped for `check 23 fleet`, it hit line 29, exception TWO
- AC5 — `python tools/drift-audit/drift_report.py --json` — in a `git clone --local` of the unit tree under a short `%TEMP%` root, run with `--base-ref refs/remotes/origin/main` because the clone's own branch has no tracking ref there: `fleet_over_budget` read `live` false; after `0.out` under the clone git dir's `gate-run/r92` carried main's line shape with no `range` field and `over aFixture=2`, it read value 1, `of` 3, `gateable` false and a detail naming `aFixture`; deleting the file returned it to `live` false
- AC6 — `git show` — the `_FLEET_HEAD` line through the end of `measure_fleet_over_budget`, cut from node d's `d99cd0328` blob and from this unit's file and compared with `diff`, differ only in the git-dir enumeration, where `read_git_dirs` replaces node d's single `--git-dir` read (§8 F4); the comment lines spelling the fields sit above that cut and were rewritten there; `grep -c "check 23 fleet — "` printed 1 over the kit gate and 2 over the drift engine
- AC7 — `grep -n fleet_over_budget tools/drift-audit/README.md` — printed one table row, line 142; `grep -c UNDECLARED_WRITE_BUDGET tools/drift-audit/README.md` printed 0
