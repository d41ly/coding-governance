**Serves:** journal TOOL-dBoundRoles-17

# TOOL-dBoundRoles-17 — the first builder's return, a divergence

Run `wf_1aee65de-95e`, started at `c14611161` on rev-5. It wrote nothing and committed nothing; `diverged: true`.

## The divergence, as returned

1. S2, §4 Files touched and the write set leave out a positional reader of `MARKER_RE`:
   `tools/roles/render_agents.py`, whose selftest handoff arm rewrites a planted marker through the role-sha and
   task-sha groups by number. The new named group `item` sits between `unit` and `path`, so every later group number
   moves by one, and that arm would hash the path and the role-sha instead while still passing on the envelope
   defect alone. S2's "every reader reads by name" holds only if that reader moves to the named groups.
2. The order against TOOL-dBoundRoles-44 is wrong. S6 commits `memory/project/work-order-legacy.txt`, and
   `memory/project/` admits only the names memory hygiene check 3 lists (`tools/memory-tree/check-memory-hygiene.sh`).
   The admission is TOOL-dBoundRoles-44's S6, at a later build order, so every pass leg between the two would red
   memory hygiene.
3. S3's Readers line undercounts the embedded `render_handoff` calls in `tools/roles/adopt-roles.test.sh`: there are
   three at `c14611161`, the third inside the planted gov-session script. None needs a change, since `item` is a
   keyword argument defaulting to none.

Every other claim it probed held at `c14611161`.

## The decision

Item 2 resolves by M3 as a delegated agent resolution: this unit admits `F:work-order-legacy.txt` in hygiene check 3
itself, in the pass that creates the file, and TOOL-dBoundRoles-44's S6 drops the admission it carried and consumes
it as built. Building unit 44's S6 first would pull a later unit's slice ahead of its order. widens: none · relaxes:
none.
