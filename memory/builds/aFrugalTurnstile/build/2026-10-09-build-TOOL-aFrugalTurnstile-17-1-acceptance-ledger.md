# TOOL-aFrugalTurnstile-17 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-17

No merge bar, no suite and no run-gates.sh over this repo ran for this ledger. The TOOL-aFrugalTurnstile-6
post-merge fixture harness was copied to a scratch root with `core.autocrlf false` and a scratch
`GATE_TURNSTILE_DIR`, and the three new arms were driven through it, with a control arm showing a clean
default-bar green still writes its record. Against `post-merge.sh` at the previous commit `3a0ec554`
AC1 was RED (the dirty tree's green was written); AC2 and AC3 guard behaviour that already existed, so
their RED was observed on a staged break with both guards disabled, where both arms failed with exit 0.
Against the edit all three were GREEN. AC4 was RED at `3a0ec554`, whose row did not name `gate-env.sh`.
The close still owes the new arm block in `tools/run-gates/run-gates.evidence.test.sh`, written and not
run, and every §7 leg.

**Evidences:** TOOL-aFrugalTurnstile-17
- AC1 — `gate-bar-green.shared` — at the edit a `bash dirty.sh` bar that appends to tracked `verdict.txt` exited 0, no `gate-bar-green.shared` was written and the output read "no gate-bar-green.shared written — the scratch worktree is not clean after the bar"; at `3a0ec554` the record was written.
- AC2 — `verdict RED` — a stub runner exiting 0 with `verdict RED` made `post-merge.sh` exit 1 with "treating it as RED", `refs/gov/bar-red` (staged at c1) still present and no green record; with the guard disabled it exited 0 and cleared the ref.
- AC3 — `REFUSED` — a `bash mover.sh` bar detaching to HEAD~1 made `post-merge.sh` exit 2 with "post-merge: REFUSING" and a `REFUSED` record; with the HEAD guard disabled it exited 0.
- AC4 — `gate-env.sh` — `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` exited 0, the `GATE_POLICY_FILE` row names `.githooks/gate-env.sh` for `GATE_POST_MERGE`, and `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` printed 66709 / 66712 and exited 0.
