**Serves:** journal TOOL-dSafePassage-3

# TOOL-dSafePassage-3 — acceptance ledger

The unit as built: `RECEIPT_SCHEMA = 4` and `derive_receipt_schema` in `tools/govkit/govkit.py`, which
`apply` and `adopt` ask for the `schema` and `steps` keys of every receipt they write; the `gov_oid`
back-fill pinned to `schema < 3` and the integrity message spelling schema 3; `update`'s re-stamp at
`max(schema, 3)`; `check` reading `steps` through `read_step_states`; the field's one reader and one
writer, `read_step_states` and `set_step_state`, in `tools/govkit/upgrade_steps.py`; the step
`govkit/receipt-schema-4`, the first row of `tools/govkit/steps.toml`, and its program
`tools/govkit/steps/receipt_schema_4.py`; matrix's `build_role_pair` taking `steps` out of a receipt
it forces below 4; the selftest's schema assertions re-read; the receipt section of
`help/upgrade-steps.md`; and the selftest arm `check_receipt_schema`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1, AC2, AC4 to AC9 and
AC14 were observed by the new arm's BODY, `check_receipt_schema`, executed outside the suite by a
scratch stand-in for the suite's `check`, `run`, `git`, `settle` and `make_target` helpers (the
first four taken from `selftest.py` by `ast`, `run` threading `--to HEAD`), over scratch targets each
installed by gov's own `apply` of `check-wiring`: 34 lines `ok`, 0 failures. That arm's RED-first
observation and the `govkit selftest` leg itself are the close's (the spec's `New arm:` line).
AC3, AC10, AC12 and AC13 were read off gov's tree, AC11 by a `python -c` call of matrix's builder.

**Evidences:** TOOL-dSafePassage-3
- AC1 — `govkit.py update --target <t>` — a receipt forced to schema 3 with one engine row's `gov_oid` taken out exited 2, stderr naming `` `commit` and no `gov_oid` `` and the row's path, the receipt's bytes unchanged, `RECEIPT_SCHEMA` read 4 (`ok`).
- AC2 — `govkit.py update --target <t> --write` — the same row at schema 2 exited 0 with no `REFUSING`, its `gov_oid` back equal to the value `apply` first wrote, and the receipt at schema 3 with no `steps` (`ok` twice).
- AC3 — `grep -n -E 'RECEIPT_SCHEMA = 4|below schema 3' tools/govkit/govkit.py` — printed `50:RECEIPT_SCHEMA = 4  # readers accept 1 to 4; 4 is reached by the step govkit/receipt-schema-4, or by a first install's apply or adopt` and `9471: "A receipt below schema 3 has ...`, beside the unchanged `check` comment at 5584.
- AC4 — `govkit.py apply --target <t>` and `govkit.py adopt --target <t> --write` — each first install's receipt read `"schema": 4` with `"steps": []` its last key; `apply` printed `schema 4` (`ok` twice).
- AC5 — `receipt_schema_4.py witness|up|down <t>` under `-I` — over an `apply` receipt forced back to 3 the witness exited 1, the up 0 leaving schema 4 and `"steps": []` last, the witness 0, and the down 0 leaving bytes equal to the schema-3 bytes (`ok` twice).
- AC6 — `receipt_schema_4.py up|down <t>` — the up over schema 2 exited 1 naming `schema 2`, bytes unchanged; the down with an `applied` row for `lib/python-floor-3.15` exited 1 naming it, bytes unchanged; the down over schema 4 without `steps` left schema 3 without the field; a non-number schema refused both verbs, bytes unchanged (`ok` five times).
- AC7 — `upgrade_steps.set_step_state` in process — a schema-3 receipt refused with no `steps` added; a schema-4 receipt gained `{"id", "introduced", "state"}`; `done`, a `failed` row with no `failure`, a `failure` on `applied`, an empty `failure`, a non-string id and a non-commit `introduced` each refused leaving one row; a second call moved the row to the end and `None` kept the known commit (`ok` nine times), and `read_step_states` refused a field below 4, a schema-4 receipt without it, a non-list and a non-object row (`ok` five times).
- AC8 — `govkit.py check --target <t>` — a `steps` row with state `done` exited 1 printing `the receipt's step record is malformed` with the row's id and `'done'`; a valid row printed no such line (`ok` twice).
- AC9 — `govkit.py update --target <t> --write` — a clean run over a schema-3 receipt left 3 with no `steps`, over a first install's schema-4 receipt left 4 (`ok` twice).
- AC10 — `python tools/govkit/upgrade_steps.py list` — printed `upgrade-steps: 1 · govkit/receipt-schema-4 · unlanded · tools/govkit/steps.toml`, then the agent-cap step second.
- AC11 — `python -c` calling `matrix.build_role_pair(..., schema=3, ...)` — the receipt it left read schema 3 with no `steps` key; at `schema=4` it kept `"steps": []`.
- AC12 — `grep -n -F '3 == GK9.RECEIPT_SCHEMA' tools/govkit/selftest.py` printed nothing (exit 1); `git diff --quiet 60d90cb7 -- tools/run-gates/check-receipt.py` exited 0.
- AC13 — `grep -n -E 'steps|rolled-back|first install' help/upgrade-steps.md` — printed the section `What the receipt records about steps`, naming `steps`, `applied`, `failed` and `rolled-back`, and "A first install, by `apply` or `adopt`, is born at schema 4", with an existing receipt reaching 4 "only by the step `govkit/receipt-schema-4`".
- AC14 — `govkit.py apply --target <t>` and `govkit.py adopt --target <t> --re-adopt --write` re-runs — a receipt planted at schema 4 with the one `govkit/receipt-schema-4` row read schema 4 with that row byte-equal after each, and one forced to schema 3 read schema 3 with no `steps` after each; each command printed the schema it wrote (`ok` four times).
