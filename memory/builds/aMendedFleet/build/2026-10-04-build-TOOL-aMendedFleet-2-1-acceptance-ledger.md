# TOOL-aMendedFleet-2 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-2

**Evidences:** TOOL-aMendedFleet-2
- AC1 — `git rev-list --merges --since=2026-09-01 HEAD` — piped to `wc -l` it printed 196 at `b93c1133d`, and the probe's first line at the same commit read `merges read: 196`; the census journal states 196
- AC2 — `write_ask_views` — the probe printed `FLAG 01c22e155 parent ef1dcdb61 tools/unattended/unattended.sh write_ask_views`, read from the merge commit, so `TOOL-aMendedFleet-1`'s restore at `fa55c1465` did not hide it; this is the census's liveness row
- AC3 — `parse_push_class` — the journal's table carries five rows, each with exactly one S3 disposition, and the `e2e840d08` row for `tools/push-main.sh` is among them, disposed superseded
- AC4 — `none restored here` — the journal says so; the one confirmed loss, `write_ask_views`, is owned by `TOOL-aMendedFleet-1`, and no loss was routed to `--rescope --act add`, because the other four rows are supersessions
- AC5 — `git grep -c -w` — at HEAD `b93c1133d` it printed 5 for `derive_push_failure` over `tools/push-main.sh`, and 2 for `scan_line`, 3 for `seen_keys` and 11 for `graded` over `tools/check-install-prefix.sh`; `derive_push_failure` is absent at both parents of `e2e840d08` and present at the merge, so the spec's candidate disposition is confirmed
- AC6 — `parse_shell_defs` — the journal's fenced probe imports `parse_shell_defs`, `_python_defs` and `parse_ts_defs` from `tools/lexicon/lexicon.py` and carries no definition regex; a python check compared the fenced block to the script that ran and found them equal; the journal's gap section names sub-definition and prose losses as unseen
