**Serves:** journal TOOL-dBoundRoles-17

# Brief — dBoundRoles: TOOL-dBoundRoles-17 revised over its third builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 17's third builder (run `wf_913518d6-7fc`) stopped on rev-7. Its
return and the main loop's decision are in
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-17-3-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md` to its next rev so the next builder can
build it as written.

### Items

1. S3's Readers line names `tools/playbook/instruction_units.py#arm_work_order` as a value reader of the marker, by
   its pinned `ORDER_HEAD`, and states the re-pin: `item=-` between the unit and the path, neither sha moving. Add
   the file to §4 Files touched and `instruction units selftest` to §7.
2. State that the hook `tools/hooks/agent-cap.js` and the renderer change in the one pass commit, so no tree carries
   a renderer that writes `item=` beside a hook that refuses it.
3. Sweep the spec once for any other site that pins the marker's bytes; probe `git grep` for the marker's opening at
   HEAD and name each site that compares the whole line.
4. Change nothing else. Keep every criterion's number and keep each passable on a correct build and red on the break
   it names. Cite code as `path#symbol` or `path@<blob8>:<line>`; pin any count. Keep the status `INPROGRESS`. One
   revision-log line names this brief and the return by their file stems.
5. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec carries its next rev with every item folded and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change beyond the items.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md` alone.

### Reuse

The S2 readers table the previous revision added, the shape item 1's reader row joins.
