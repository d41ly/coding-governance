**Serves:** journal TOOL-dBoundRoles-20

# TOOL-dBoundRoles-20 — the main loop's decision on the builder's divergences of round one

The builder of round one (`wf_210dcba7-3d4`) read the spec at rev-7 against the tree at `fc7ae199a`, wrote nothing,
and handed back the places the spec leaves open or the tree contradicts. The main loop checked the second against
source: no item of `tools/loop/loop.toml` names `gov-reviewer`, `gov-skeptic` or `gov-synthesizer` as its actor,
and each of them declares `layer: layer.roles` and `acts-as: item` and is listed in the `roles` of the
`spec-write`, `spec-review` and `closing-review` entries of `tools/roles/workflows.toml`. Each answer below is the
option no worse than the others on any principle (P18), decided rather than parked, and binds over the spec as the
owner's ruling `2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling` does; the builder records each departure in its
deviation record.

1. **The write set.** AC1's plant lives in the plant tables of `tools/playbook/gov_tag.py#PLANTS` and
   `#SHAPE_PLANTS`, and its arm in the plant cases of `tools/playbook/adopt-playbook.sh`. Both paths join section 4's
   Files touched and the dispatch's write set.
2. **The matrix arm.** Its home is `check_role_acts(roles, items, workflows)` in `tools/roles/roles_lib.py`, run by
   `check_roles.py` over `compose_roles`, `compose_workflows` and the composed items `read_composition_at` returns. A
   role acts when a composed item names it as `actor` or a composed workflow entry lists it in `roles`. The
   population is every composed role whose `acts-as` is `item`, gov's and the repository's alike, so the clause's
   "every core item role acts in at least one core item" holds on gov's tree through the workflow entries, and AC7's
   `role.adopter.triager` is in it. An exclusion that leaves such a role acting nowhere is admitted only when the
   role is excluded with it, else the arm reds naming the role.
3. **A repository role's body.** An overlay `[[role]]` row carries front-matter fields only, and section 8 F9 lets no
   `body` field be declared. So a composed row whose `origin` is `repository` is listed in the role index and graded
   by every field check, while R5's body and static-block checks and the agent-file render skip it, each printing
   one note naming the row. A repository role with a body stays a role file under the kit's `agents/`, the
   migration section's path; moving it to the overlay is item 17's adoption, a non-goal of this unit.
4. **The actor patch's template.** A role-acted item carries no `returns` and no `allowance`: both derive from the
   role (`tools/loop/loop_lib.py#check_item_declarations`). So `check_actor_patch(item, role, original)` takes the
   gov row's original actor role as its third argument, and `check_item_composition` hands it from the operation's
   `gov` value. The template is the original role's `return`: every row of it must be a row of the patched role's
   `return`. The ceiling is the original role's `writes`: every class of it must be in the patched role's `writes`.
   The shape test stands as written. `check_roles.py --check-actor-patch <file>` reads the composed item row and the
   original role's slot from that file. AC6's "with the template added" means the original role's `return` rows
   added to the repository role's.

widens: the roles kit's checks, by `check_role_acts` and the third argument of `check_actor_patch` · relaxes: R5 and
the agent-file render for a repository row, by the note each prints.
