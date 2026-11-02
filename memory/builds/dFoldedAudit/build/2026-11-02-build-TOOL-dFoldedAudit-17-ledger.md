# TOOL-dFoldedAudit-17 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-17

The builder observed every criterion on M `ccfa23ffe` and F `1a804910b`, as its return records, except AC12's manifest check. The main loop ran that check after F, and the other criteria are the builder's.

**Evidences:** TOOL-dFoldedAudit-17

- AC1 — `git diff --name-only --diff-filter=U` — named exactly the eight paths, with both merge drivers set.
- AC2 — `git diff --check` — 46 marker lines before resolving, then 0. It found nothing against either parent.
- AC3 — `SPEC_AC_ORDER_CUTOFF` — conf line 992 comes before `SPEC_SUPERSEDE_CUTOFF` at 1025. The docstring orders supersede before ac-order, and the dossier puts the criterion-order paragraph first.
- AC4 — `py_compile` — exited 0.
- AC5 — `FLOOR_ASSERTIONS=215` — the lines `200 -> 203` and `203 -> 215` print in order, ending with the floor.
- AC6 — probe P — printed exactly the spec's 13 lines.
- AC7 — probe D — printed `37 39 True`.
- AC8 — `python tools/check-spec-tokens.py` — the join count was 2 and the refusal count 0.
- AC9 — `drift_report.py --check` — stderr held 0 lines naming `cutoff_keys_armed`, and the row reads `38 39 ok (pin 39, drain it)`.
- AC10 — `gen_map.py --check` — both it and `gen_build_index.py --check` exited 0.
- AC11 — `mirror --check` — exited 1 on M and 0 on F.
- AC12 — `bash skills/session-kickoff/manifest-check.sh` — the main loop ran it after F and it exited 0. M's stamp names `HEAD^1`, F's names M, and `last-body-change` reads `201eb127`.
- AC13 — `git merge-tree` — exited 0, and `HEAD^1^2` equals `origin/main`, both `84acebdc`.
