# TOOL-dDeclaredLoop-9 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-9

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon's `--suggest`
ran, as a builder's role allows, and answered OK for `check_item_declarations`,
`resolve_item_declaration` and `read_role_defaults`. The `loop definition` leg's own command,
`loop_lib.py --check`, is refused to a builder, so the unplanted verdict in gov is the close's to
observe; each plant below runs the same read with its break, and `actor-list-foreign` breaks only the
builds folder after the read, so its item lines are the definition's as shipped. Every criterion was
observed on node `d` (win32) over the built tree, in the pass from `9f835b2b`.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of its one
`New arm:` line, the `actor-two` plant of `tools/loop/loop_lib.py#main`, staged against the reader
as `TOOL-dDeclaredLoop-12` landed it, which reads an item's actor and never grades it.

**Evidences:** TOOL-dDeclaredLoop-9
- AC1 — `loop: items · 61 read · 9 pending · 0 unarmed` (PINNED 2026-11-14) — `--fixture --plant
  actor-list-foreign` exited 0, printed one `loop: item` line per item, 61 of them (PINNED 2026-11-14),
  the `item.build.unit-pass` line `role:gov-builder · inputs from role:gov-builder · allowance product
  from role:gov-builder · returns from role:gov-builder`, and that count line; the planner, architect
  and tester rows printed `pending`.
- AC2 — `role-copy` — `--plant actor-two` exited 1 naming `item.build.unit-pass` and both actors;
  `actor-bad-kind` exited 1 naming the kind `agent`; `witness-missing` exited 1 naming the item and
  `witness`; `allowance-missing` exited 1 naming `item.plan.place` and `allowance`; `role-copy` exited
  1 on a refusal saying the allowance copies the role's `writes`; `role-widen` exited 1 naming
  `item.design.seams`; `role-pending` exited 0 printing `role:gov-no-such-role · pending`; and
  `roles-no-kit` exited 0 printing every role item `unarmed`. Each plant that predates this unit kept its exit.
- AC3 — `read_role_defaults` — a `python -c` importing `loop_lib` from `tools/loop` printed
  `product role:gov-builder` for `resolve_item_declaration` of the `item.build.unit-pass` row, and
  `spec role:gov-builder` over `roles_lib.load_roles` of a scratch directory holding a copy of the
  builder's role file whose `writes` reads `spec`.
- AC4 — `actor = "role:gov-` — `git grep -c` printed 18 (PINNED 2026-11-14) for `tools/loop/loop.toml`,
  and the short-spelling `git grep -nE` printed nothing, exit 1.
- AC5 — `roles-no-kit` — `grep -c` printed 1 for `help/loop.md` and for `tools/loop/README.md`, and
  `grep -c 'role:planner' help/loop.md` printed 0.
