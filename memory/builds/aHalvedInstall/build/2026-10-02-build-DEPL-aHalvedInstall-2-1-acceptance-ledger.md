# Acceptance ledger — DEPL-aHalvedInstall-2

**Serves:** journal DEPL-aHalvedInstall-2

Built at `6d7dcc05`; the version bump it owed rides `1bfa4d01` with the build's other moves. The arm
is selfcheck check 6b in `tools/govkit/govkit.py`. It was observed RED before either probe was
fixed, naming exactly the two refutation-shaped holes, and green after. The narrowed probe was
exercised over seven conf shapes by hand, and its text is identical whether read with `tomllib` or
with the awk reader `unattended.test.sh` uses for its AC15 arm.

**Evidences:** DEPL-aHalvedInstall-2
- AC1 — `python tools/govkit/govkit.py selfcheck` — `20 ran, 2 exited 0`, naming `playbook-placeholders` and `keepalive-tool-names`, with both probes at base text
- AC2 — `python tools/govkit/govkit.py selfcheck` — `20 ran, 0 exited 0, 0 could not launch`, exit 0, after S2 and S3
- AC3 — `RESUME_SCHEDULE_CREATE` — absent 1, placeholder 1, empty 1, both real 0, unquoted real 0, `RESUME_SCHEDULE="off"` with neither 0, no conf at all 1
- AC4 — `test -f` — the playbook probe exits 1 with no charter file present
- AC5 — `python tools/govkit/govkit.py epoch` — `--base cd90f7fa` prints no `FAILED` line at `1bfa4d01`
