**Serves:** research PLAY-dOrderedCharter-20

# Brief: unit 20's divergence — three conflicts with units 65, 7 and 15, and the kit dependencies

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. Unit 20's builder (run wf_d03c1158-8ec) returned `DIVERGENCE:` before writing code, against rev-6
at `bb719e318`, each item with a probe. The tree is clean.

## The brief

### Goal

Revise spec 20 so each conflict below is resolved and its builder can build it as written.

### Items

1. **The kind's factory name.** S9, AC9 and section 4's Inventory say `core.py new unit`. `core.py new <kind>` looks up the
   row `kind.<kind>`, and the row is `kind.instruction-unit`, so that command refuses and exits 2. An alias would break
   unit 65's rule that a kind's name is never a namespace word. Say `core.py new instruction-unit`, in the row's factory
   too.
2. **The gate leg's principles.** S9 makes the schema leg the kind's gate and takes the kind off `core-pending.txt`.
   S10 fixes that leg's `enforces` at p11 and p13, but `kind.instruction-unit` binds p13 and p16, and
   `tools/playbook/core.py#check_kind_row` requires the gate leg to enforce every bound tag. Add `principle.p16` to the
   leg, or rule that the binds change. Decide by the fork rule.
3. **Reading change records before unit 15.** S3 reads them through the record factory as the kind unit 15 registers,
   but unit 15 builds after this unit: `tools/memory-tree/build_records.py` holds the kind as pending, and reading it
   raises. `derive_status` over passed-in records is buildable, but the tree reads behind S2's active, S3's render arm
   and S8 are not. Say what they read until unit 15 lands, or move the work. Options include: no records, every unit
   active with an unarmed line, unit 15 wiring the reader; or this unit registering the kind. Decide by the fork rule.
4. **Kit dependencies.** The adopters will depend on `render_playbook.py`, but `tools/agent-instructions/kit.toml` has
   `requires = []`, `tools/roles/kit.toml` does not require `playbook-render`, and the agent-instructions adopter's
   header claims no hard dependencies. The section 5 risk that an adopter renders with the old renderer cannot hold
   under AC5. Rule on `requires`, and rewrite that risk.
5. **Files touched and section 7.**
   - `tools/roles/adopt-roles.test.sh` copies only the roles kit into its fixture, so `render_playbook.py` is unreachable
     there.
   - Section 7 omits the `roles adopter self-test` leg.
   - `tools/roles/kit.toml` needs its `[[generated]]` generator changed.
   - `help/roles.md` and `tools/govkit/usage.toml` still name `render_agents.py --write`; that writer must go or it
     writes with no lock row.
6. **The selftest fold.** S6 does not say whether `roles render selftest` keeps its `render_agents.py --selftest` argv or
   moves to `render_playbook.py`. Say which.
7. **A stale pending row.** `python tools/playbook/core.py meta-check` is red at HEAD:
   - The row `principle.p11` in `tools/playbook/core-pending.txt` is stale, because units 12 and 13 now enforce it.
   - Add its deletion to this unit's scope, since S9 already edits that file.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`.
- Add one history line naming this brief, with the S and AC ids it touched.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`.
- New text names a section in words. It never uses the section-sign form, the method-rule form or the hygiene
  check-number form, and it adds no `path:line`.
- An item that retires a name carries a `**Readers:**` clause. Its by-name half names readers by plain tracked path.
- A consumes-from or hands-off edge you add or change has its mirror on the other spec. List any such edge in the
  return; do not edit another spec.
- Stay under the 47000-byte authored budget.

For the run:

- No unit is building, so edit the spec in the tree.
- Writes stay in spec 20. A fork no option survives is written open in the fork record and said in the return.
- Do not commit and run no gate.
- Return the new rev, each fork decision with its loser, and any edge needing a mirror.

### Acceptance

- Every item above is folded, or listed in the return with the reason it was not.

### Gates

The memory-hygiene hook, at the main loop's commit.

### Non-goals

- No code.
- No other spec.

### Limitations

The items above, "For the run".

### Reuse

`tools/playbook/core.py#check_kind_row`; `tools/playbook/kinds.toml`; `tools/memory-tree/build_records.py`.
