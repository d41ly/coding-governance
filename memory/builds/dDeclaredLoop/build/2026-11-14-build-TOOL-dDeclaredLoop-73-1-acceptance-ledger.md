# TOOL-dDeclaredLoop-73 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-73

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on
node `d` (win32) by a scratch probe of the unit's own code: a script in the session scratchpad that
builds a scratch gov under a short temp directory from the working copy's `govkit.py`,
`upgrade_steps.py` and `adopters.toml`, with commits A, B and C as section 6 states them, applies
`--kits demo` into a `fixture_target.build_target` target at A, and runs the verb each way from a
detached checkout; then imports the working copy's `govkit` for AC3's and AC4's calls and AC5's
`blob_at` stand-in. The same probe ran once at the pass base `62ee39d1` and once on the built tree.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of the one
`New arm:` line, the `[dDL-73]` checks in `tools/govkit/selftest.py#check_requires_vintage`, staged
by passing `descs` back to `demand_claimed_requires` in `tools/govkit/govkit.py#_cmd_update` for one
run and restoring the call. The arm's body was checked here only by compiling it and resolving every
name it loads; it did not run.

**Evidences:** TOOL-dDeclaredLoop-73
- AC1 — `'demo' requires 'other'` — at base the update to B from A's checkout exited 0; built, it
  exited 2 with stderr naming the pair and `apply --kits demo,other`.
- AC2 — `update would leave` — at base the update to A from B's checkout exited 2 with that line;
  built, it exited 0 and neither stream held it.
- AC3 — `does not resolve` — at base the update to C from B's checkout refused on the working tree's
  pair; built, it exited 2 with stderr `'demo' requires are unknown at` C naming the demo descriptor
  that does not resolve there, and the call over C returned `demo` in its second mapping alone.
- AC4 — `read_requires_at` — the call at A for `other` returned `other` with an empty `requires` in
  the first mapping and an empty second mapping.
- AC5 — `so the default set there is unknown` — with `blob_at` answering None the reason equalled the
  registry path built from the tool root followed by `does not resolve at aaaaaaaa, so the default
  set there is unknown`.
- AC6 — `memory/map/generated/symbols.json` — `grep -c 'read_requires_at'` over it printed 1 after
  `gen_map.py --write`, and `grep -c 'read_registry_at'` printed 2.

Regression probes of the read, by `python -c` over this checkout: at the release-0 pin the release-0
`deploy.toml` kits plus HEAD's default set read with no unknown kit and no unmet edge, and every id
HEAD's registry declares reads with no unknown kit; at each vintage of the DEPL-dCarriedReceipt-8 `V8`
tuple `check-wiring` reads with an empty `requires`; at HEAD `roles` requires `loop`, which the
`[dDL-57]` checks in `tools/govkit/selftest.py#check_roles_default` grade, and at `ed497191` it does
not.
