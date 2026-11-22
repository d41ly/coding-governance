**Serves:** journal TOOL-dBoundRoles-44

# Brief — dBoundRoles: TOOL-dBoundRoles-44 consumes the legacy-file admission TOOL-dBoundRoles-17 now makes

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. TOOL-dBoundRoles-17's first builder found that the file it seeds under
`memory/project/` stays unadmitted until this unit's S6, a later build order, so every pass leg between them would
red memory hygiene. The decision moves the admission into unit 17; it is recorded in
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-17-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-44.md` to its next rev so its S6 no longer
admits `F:work-order-legacy.txt` and instead consumes the admission TOOL-dBoundRoles-17 builds.

### Items

1. S6 drops the hygiene check 3 admission of `F:work-order-legacy.txt` and its comment, and states that
   TOOL-dBoundRoles-17 makes it; keep any other part of S6.
2. The consumes-from edge to TOOL-dBoundRoles-17 names the admission as built by unit 17. Any criterion that observed
   this unit's admission observes it as consumed, passable on a correct build and red on the break it names; keep
   the check that `.memory-tree.conf` names no such file. Drop any file from Files touched that only the admission
   needed.
3. Change nothing else. Keep every criterion's number. Cite code as `path#symbol` or `path@<blob8>:<line>`; pin any
   count. Keep the status `DEFERRED`. One revision-log line names this brief and the return by their file stems.
4. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec carries its next rev with every item folded and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change beyond the items.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-44.md` alone.

### Reuse

TOOL-dBoundRoles-17's spec, revised beside this one, for the admission's exact shape.
