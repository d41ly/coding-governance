**Serves:** research PLAY-dOrderedCharter-20

# Brief: unit 20's second divergence — the work-order template's home

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. Unit 20's builder (run wf_a0f4d30c-12c) returned `DIVERGENCE:` before writing code, against rev-7 at
`37babef65`. The tree is clean.

## The brief

### Goal

Revise spec 20 so its work-order template is reachable on every install that holds `tools/roles/handoff.py`, and fold the
builder's three smaller items.

### Items

1. **The template's home.** S7 puts the template at `tools/playbook/templates/work-order.template.md`, filled by
   `render_handoff` in `tools/roles/handoff.py`. The `tools/playbook/` files ship only with `playbook-render`, and the
   `requires` closure of the default selection holds `roles` and `playbook`, not `playbook-render`.
   - So on a default install `handoff.py render` refuses, and the `roles adopter self-test` fixture reds.
   - F10 does not reach this.
   - Decide by the fork rule, with the loser in the fork record. Options:
     - (a) Home the template in the roles kit, at `tools/roles/templates/work-order.template.md`; only `handoff.py` reads
       it.
     - (b) Keep the path and add a `[[files]]` rule to `tools/roles/kit.toml`.
     - (c) A fallback in `handoff.py`, saying why F10's objection to a fallback does not apply.
   - S7, S12, section 3 Edges, section 4 and AC7 follow the pick.
2. **A plant no leg runs.** No leg runs the `instruction_units.py` fixture, so the `New arm:` plants for that module
   never run on the bar.
   - Wire them into a leg, and say which one.
   - Spec 6's fork F6 adds an optional third argument to `run_plant_rows` for a script's plant entry, and that unit
     builds later. Take the wiring into this unit if it must land here, and say how the two relate. Return any edge
     that needs a mirror.
   - The `work-order` plant needs the roles kit, which a `playbook-render` target may not hold; say how it runs.
3. **AC7's selector.** A real row scoped `role.builder` reds S1's scope arm, since no `role` namespace is registered.
   AC7's plant only expands a slot, so it passes, but it must not read as a schema-valid row. Use a registered selector
   or say so.
4. **The mirror commit's trailer, and the write set.**
   - Section 4 Rollout's second commit, `.governance/policy.json` alone, carries `Pass: none`; say so.
   - Add `tools/playbook/adopt-playbook.sh` and `tools/playbook/instruction_units.py` to Files touched.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`.
- Add one history line naming this brief, with the S and AC ids it touched.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`.
- New text names a section in words. It never uses the section-sign form, the method-rule form or the hygiene
  check-number form, and it adds no `path:line`.
- An item that retires a name carries a `**Readers:**` clause. Its by-name half names readers by plain tracked path.
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

`tools/roles/kit.toml`; `tools/roles/adopt-roles.test.sh`; `tools/playbook/adopt-playbook.sh`'s `run_plant_rows`.
