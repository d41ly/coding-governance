# TOOL-dFoldedAudit-18 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-18

The builder observed AC1 to AC5 at pass commit `65b587e50` with probe A, which calls the docs leg's own functions. The main loop then ran the leg itself.

**Evidences:** TOOL-dFoldedAudit-18

- AC1 — `python "$P/probe.py"` — printed five lines of `1 help/spec-audit.md ok`, where it printed five lines of `0 - BAD` before the page.
- AC2 — `python "$P/probe.py"` — `command 57` and `command 84` both read `tested tools/unattended/unattended.sh`, and `links 2` came with no finding.
- AC3 — `python tools/govkit/docs_leg.py --list --undocumented` — counted 0 of the five ids, against 5 before.
- AC4 — `grep -c '(spec-audit[.]md)' help/README.md` — printed 1.
- AC5 — `git rev-list --parents -1 HEAD` — `65b587e50` has the single parent `612e15d1f`, which descends from `30396a42`. Only the two help files changed.

After the pass the main loop ran `python tools/govkit/docs_leg.py`. It exited 0 with `45 anchors on 13 pages · 0 stale`, no UNDOCUMENTED line, and the list at its low-water of 370.
