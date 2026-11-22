**Serves:** journal TOOL-dBoundRoles-1

# TOOL-dBoundRoles-1 — the first builder's return, a divergence

Run `wf_917db953-a98`, builder agent `a1e5efb3030ef7449`, started at `79a74d578` on rev-6. It wrote no product path and
committed nothing; `diverged: true`.

## The divergence, as returned

(1) S1 says R2 grades `layer` as a tag that must name a `[[layer]]` row of `tools/playbook/layers.toml`. §5 says that
when the roles kit cannot find that file, R2's layer check becomes a note and is never a pass. AC1's scratch holds
copies of `tools/roles/` and `tools/loop/` only, with no `tools/playbook/`. In that scratch the kit's sibling lookup
cannot find `layers.toml`: `resolve_kit_dir("playbook", "layers.toml", kit_dir)` has no git root or install receipt to
read, and it probes only `<kit>/playbook` and `<kit>/../playbook`; the same holds for
`tools/loop/loop_lib.py#read_layer_tags`. So `layer: layer.nowhere` would print a `roles: note:` line, not the R2 line
AC1 owes, and AC1 would show one R2 line, not two: AC1's own "Red when".

(2) The §7 arm `New arm: tools/roles/adopt-roles.test.sh` has the same gap: `tools/roles/adopt-roles.test.sh#build_fixture`
copies only `loop_lib.py` and `loop.toml` beside the roles kit, in a fresh `git init` with no install receipt. The
planted layer tag cannot turn red unless the suite also copies `layers.toml` to `<fixture>/playbook/`, an edit to a
path §4 Files touched does not list.

## What held

At HEAD `79a74d578`: R6, R7, R8, `BODY_CEILINGS`, `WORKFLOW_NAMES`, `WRITE_FOLDERS`, `read_workflow_order`,
`render_roles_index`, `print_roster`, `write_role` with its `role-new` and `role-hand` rows, `write_workflow`, the
`kind.role` usage row, the loop.toml `research` row at order 0, `step.design` as a declared step, the five layers.toml
rows, `build_layers_fixture`, the plant lists of `adopt-playbook.sh` and `loop_items.py`, `read_role_defaults`,
`read_layer_tags`, `check_item_declarations`, `read_drive_reference_rows`, the reviewer keys, and no gov item's actor
naming a cycle role or a reviewer slot. The next builder must also declare `.claude/roles.json` and
`help/reference/kinds.md`, which the dispatched write set left out.
