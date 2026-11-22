**Serves:** journal TOOL-dBoundRoles-17

# TOOL-dBoundRoles-17 — the third builder's return, a divergence on rev-7

Run `wf_913518d6-7fc`, started at `644c7eac2` on rev-7. It built and probed most of the unit, restored every path and
committed nothing; `diverged: true`. Its partial build is kept in the session scratchpad as
`p17/TOOL-dBoundRoles-17-wip.patch`, with the seeded legacy home beside it.

## The divergence, as returned

1. The change needs `tools/playbook/instruction_units.py`, outside the write set: `#arm_work_order`, the `work-order`
   plant the `instruction units selftest` leg runs, renders a handoff and compares it byte for byte with its pinned
   `ORDER_HEAD`, whose marker carries no `item=`. S3 writes `item=` on every marker, so that arm reds unless
   `ORDER_HEAD` gains the field; the marker sits outside both hashed sections, so neither sha moves.
2. S3's Readers line says the marker has no value readers, which is false for that arm. The spec owes the reader in
   S3, the file in §4 Files touched and the leg in §7.

It also flagged a rollout order: the session's hook is the project directory's `tools/hooks/agent-cap.js`, so a hook
from before this unit refuses every marker this unit's renderer writes. Every other citation held at `644c7eac2`.

## The decision

Both items go to the spec writer. The rollout order needs no new mechanism: the hook and the renderer change in one
pass commit, so no tree carries one without the other; the spec states that.
