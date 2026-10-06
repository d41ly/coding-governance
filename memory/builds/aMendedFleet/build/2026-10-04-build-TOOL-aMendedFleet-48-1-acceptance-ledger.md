# TOOL-aMendedFleet-48 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-48

**Evidences:** TOOL-aMendedFleet-48
- AC1 — `python tools/drift-audit/drift_report.py --check` — run twice with `GOV_DEFAULT_BRANCH=main` in a `git clone --local` of the unit's staged tree under `%TEMP%/af48`, detached at that tree's commit object: `--json` printed 22 records, and `.git/drift-history.tsv` held 45 lines, one header spelling the nine S2 columns tab-separated in order and two groups of 22; every row had nine fields, its `state` one of 32 live, 6 dead, 4 declared-empty and 2 not-asked; each run printed one `22 history rows appended to` line on stdout
- AC2 — `render_drift_offenders` — `python -c` importing `drift_report` from `tools/drift-audit`: two live records whose detail lists differ in one member gave different `key_hash` values, two differing only in a `:<digits>` locator gave equal ones, and the same three-row over-pin record (a located dict, its duplicate, a located string) rendered the identical three keys, ordinal `#2` included, under this tree and under the pre-hoist engine read from `git show HEAD:`
- AC3 — `drift-history.tsv` — replaced by a directory in that clone: `--check` exited 1, the same status the writable runs returned (whose red is `non_terminal_specs_cited_by_product_source = 4 (pin 2)`, foreign specs), and stderr carried one `history NOT written to <path>: [Errno 13] Permission denied` line; the file was restored afterwards
- AC4 — `python tools/drift-audit/drift_report.py --offenders` — then `--json` in that clone left the file at 45 lines; `--check` in a linked worktree `%TEMP%/af48w` of the clone moved the common file 45 -> 67 lines and the worktree's private git dir `.git/worktrees/af48w` held no `drift-history.tsv`
- AC5 — `grep -c "drift-history.tsv" tools/drift-audit/README.md` — printed 3: the layout-table row and the new section's heading and body

## The arm

`test_drift_history` in `tools/drift-audit/selftest.py`, seven checks over a `make_repo` fixture:
two `--check` runs, `--offenders`, `--json` and `--json --check` writing nothing, a member swap and
a locator move through `build_history_rows`, and a directory on the file's name. Run ALONE through a
scratchpad slice calling it, fixture under `%TEMP%/a48`: seven `ok`. Staged red twice and restored:
with the write failure re-raised, the exit-status and stderr checks FAILED (`0 -> 1`, a traceback);
with the key built from the raw located rows, the locator check FAILED. `CHECK_FLOOR` 302 -> 309.
The suite did not run.

## Owed at the close

- `drift-audit selftest`, `drift-audit records`, `drift-audit wiring`, `codebase-map coverage +
  freshness`, `recall floor`, `recall floor arms`, `lexicon naming predicates` and `spec tokens`.
- The drift-audit kit version bump, per the brief; `kit epoch` is the close's.
