# DEPL-dShippedRelease-23 deviation 231 — the item arm admits an expansion role on its own layer's program

**Serves:** deviation DEPL-dShippedRelease-23

- **Departs from:** `TOOL-dBoundRoles-1@rev-3` [S7]
- **Hand-off:** design-to-spec
- **Before:** an item whose actor `role:<slot>` names a role an expansion registers, or whose index `layer` is an expansion row, is a refusal naming the item and the role
- **After:** the same refusal, except where the item's tag names a program a layer row registering that role lists under `programs`: `kits` on `layer.distribution` and `release` on `layer.integrations`
- **Cause:** design defect
- **Reason:** cl-dClosedLoop-0433 defines the deployer with two jobs that are items of its expansions, flow-roles:106, :107 and :119 name it as their actor, and the shared interface gives it `acts-as` `item`; TOOL-dBoundRoles-1 S7 and AC6 refuse every such item, because that unit reads "the core roster never names them" as "no item names them". The core-item refusal is what P28 asks, and it stays. The change is to a gate no clause of this build names, so it trips veto 2 outside the grant; every other option fails veto 1, and the standing ruling ER:388 takes the most capable of them.
- **Evidence:** `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md` S7, §4 "The item arm" and AC6; `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md:106-119`; layer-roles:480-484; `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` rung 5; DEPL-dShippedRelease-23 §8 F3
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer stage of the harness's spec run for dShippedRelease, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** ask DEPL-dShippedRelease-32
- **Caused-by:** DEPL-dShippedRelease-23
- **Surface:** tools/loop/loop_items.py check_item_roles
