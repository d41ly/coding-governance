**Serves:** journal TOOL-dBoundRoles-6

# Brief — dBoundRoles: TOOL-dBoundRoles-6 revised over its first builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 6's first builder (run `wf_c709768a-dd5`) stopped before its code
on rev-7. Its return and the main loop's decision are in
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-6-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-6.md` to its next rev so the next builder can
build it as written.

### Items

1. §5 names the user docs this unit owes and what each gains: `help/policy.md`, `help/roles.md` and
   `help/red-fix-lane.md`, plus `tools/policy/README.md`'s guard section and its count of guard cases. Add them, and
   the `kit.policy` change record the pass stages, to §4 Files touched; add the docs leg to §7 if it is not there.
2. Re-ground every `tools/hooks/agent-cap.js` citation against HEAD, which TOOL-dBoundRoles-17 changed, and drop the
   claim that the file is still the blob it was.
3. A new §8 fork, resolved by M3 as a delegated agent resolution with `widens:` and `relaxes:` each a value or `none`:
   where `render_role_section` gets the drive lines and the work order's role half without the library importing
   `tools/roles/handoff.py` (moving those helpers into the library, or the library writing the section itself), and
   whether `tools/policy/guard.py` carries its own inlined `resolve_kit_dir` or reads the path another way. Probe each
   option against HEAD, including the renderer's ranked selftest that points the kit at a fixture without templates,
   and put any moved symbol in the Inventory.
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

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-6.md` alone.

### Reuse

`tools/policy/policy.py`'s inlined `resolve_kit_dir`, the copy item 3 weighs.
