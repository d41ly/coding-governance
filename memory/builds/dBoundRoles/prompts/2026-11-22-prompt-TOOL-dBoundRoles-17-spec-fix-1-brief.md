**Serves:** journal TOOL-dBoundRoles-17

# Brief — dBoundRoles: TOOL-dBoundRoles-17 revised over its first builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 17's first builder (run `wf_1aee65de-95e`) stopped before its
code on rev-5. Its return and the main loop's decision are in
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-17-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md` to its next rev so the next builder can
build it as written.

### Items

1. S2 names `tools/roles/render_agents.py` among the readers of `MARKER_RE`, its selftest handoff arm moving to the
   named groups; add the file to §4 Files touched, and make AC2's red case cover a reader indexing by position there.
2. A new §8 fork, resolved by M3 as a delegated agent resolution with `widens: none` and `relaxes: none`: this unit
   admits `F:work-order-legacy.txt` in memory hygiene check 3 in the same pass that creates the file, with the
   comment and the rendered hygiene guide that check's admissions carry (probe
   `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` at
   HEAD for how an admission lands). Add those files to Files touched, the matching edge to TOOL-dBoundRoles-44 as
   the unit that now consumes the admission as built, and the hygiene leg to §7 if it is not there.
3. Correct S3's Readers count of the embedded `render_handoff` calls in `tools/roles/adopt-roles.test.sh`.
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

No other spec; TOOL-dBoundRoles-44 is revised by its own writer. No product code. No change beyond the items.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md` alone.

### Reuse

The admissions already in hygiene check 3, such as `F:role-stand-in-waiver.txt`, the shape item 2 copies.
