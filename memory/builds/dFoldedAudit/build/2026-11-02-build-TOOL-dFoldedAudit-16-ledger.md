# TOOL-dFoldedAudit-16 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-16

Most criteria were observed by this unit's builder at pass commit 365cdeb8c, through direct probes recorded in `2026-11-02-build-TOOL-dFoldedAudit-16-4-builder-return.md`. AC1 and AC8 run a gate leg's own command, so the main loop observed them after the main merge, at 1a804910b.

**Evidences:** TOOL-dFoldedAudit-16

- AC1 — `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'` — it exited 0 and printed `OK — no BANNED spawn idiom, and 2165 registered site(s) in 303 row(s) match the scan`. Every row for the three files reads as registered, and none is over its count.
- AC2 — `bash notes.sh` — over the parent and over the new driver, probe N printed five byte-identical lines. The new driver wrote 0 bytes to stderr, and the parent printed MISMATCH on all five rows.
- AC3 — `grep -c 'exitnote="*$(review_exit_note spec-' tools/unattended/unattended.sh` — printed 0, and the `$_exitnote` grep printed 2.
- AC4 — `grep -c '$(cat "$_sw_tmp/err")\|$(cat "$_fc_r/$_fc_f")' tools/unattended/unattended.test.sh` — printed 0, 10, 0 and 0 after the pass, and 7, 3, 1 and 1 at the parent, as rev-2 pins.
- AC5 — `grep -c 'strict run_wf "$1" "$(printf' tools/workflows/unattended-build.test.sh` — printed 0 and 0.
- AC6 — `bash throw.sh` — printed `FAIL second line`, `FAIL first line` and `ok   mid-line`.
- AC7 — `git diff --stat 74274869 -- memory/project/spawn-idiom-sites.txt` — printed nothing.
- AC8 — `python tools/drift-audit/drift_report.py --check` — at 1a804910b its stderr held 0 lines naming `cutoff_keys_armed`, and the stdout row reads `38 39 ok (pin 39, drain it)`. The pin is 39 there because TOOL-dFoldedAudit-17's merge re-based this unit's raise of two onto main's 37.
- AC9 — `python -` — at 365cdeb8c probe D printed `38 True True`, and the `-B3` grep showed `SPEC_SUPERSEDE_CUTOFF`, `SPEC_FOLD_CUTOFF` and `TOOL-dFoldedAudit-16`.

No `New arm:` line is declared, so no RED-first observation is owed. The section 7 legs are the close's bar.
