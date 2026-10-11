# Acceptance ledger — DEPL-dRemeasuredRender-1

**Serves:** journal DEPL-dRemeasuredRender-1

Built on `7a474bab`. The new self-test arms ran through a scratch runner that loads the self-test
module, keeps `check_update_safety`'s fixture builders and runs only this unit's block, once with
`GOVKIT` pointed at this tree's `govkit.py` and once at base `17472e21`'s copy in a detached
worktree. Here all nine assertions held. At base the receipt, commit, count and KEPT assertions
failed: the row kept `written: false` with no `sha256` or `oid` at all, the run printed no
re-measure line, and the refused render printed no KEPT line. The AC2 `check` assertion holds at
both, as the spec says: before this unit the sums and the receipt agreed with each other and both
named the pre-render state.

The `oid` assertion stages the render in the fixture target and reads the index entry with
`git ls-files -s`, so the arm does not grade the code's own `hash-object` call against itself.

`lexicon naming predicates` reads 1068 offenders over a pin of 1063 both here and at base; the new
function `measure_rendered_rows` leads with a declared verb and adds none.

**Evidences:** DEPL-dRemeasuredRender-1
- AC1 — `install.sums` — after `update --write` the fixture row's `sha256` was the hash of `docs/out.md`, its `oid` the index blob `git ls-files -s` named once the render was staged, and the sums carried that hash beside `docs/out.md`; the run printed `rendered receipts: 1 re-measured · 0 kept`; red at 17472e21
- AC2 — `govkit check` — over the settled fixture it exited 0
- AC3 — `KEPT` — with the regenerate exiting 5 after writing, the row was byte-equal to its pre-update record and the run printed `receipt: KEPT [rendered] docs/out.md — its render was refused`; red at 17472e21
