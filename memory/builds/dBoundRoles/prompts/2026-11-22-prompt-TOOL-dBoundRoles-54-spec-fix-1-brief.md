**Serves:** journal TOOL-dBoundRoles-54

# Brief — dBoundRoles: TOOL-dBoundRoles-54 revised over its first builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 54's first builder (run `wf_6da83969-b78`) stopped before its
code on rev-5: S3 rev-bumps TOOL-dBoundRoles-49's spec, which is now CLOSED and frozen. Its return is
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-54-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md` to its next rev so the next builder can
build it as written, without editing any CLOSED spec.

### Items

1. S3 and AC3 take route (a) of the return: no edit to unit 49's spec. This spec's own §6 carries unit 49's restated
   criterion for the roster set. The pass instead writes one deviation record in `build/`, its values `report` and
   `author-recorded`, saying unit 49's AC2 and its "Why two checks" claim are superseded by this unit's restated
   criterion, with the reason the frozen spec cannot carry it. Name that record's path in §4 Files touched in place of
   the spec of TOOL-dBoundRoles-49, and restate AC3 so it observes that record, passable on a correct build and red on
   the break it names. Record the choice as a §8 fork resolved by M3, a delegated agent resolution, `widens: none` and
   `relaxes: none`.
2. Probe every other claim of S1, S2, AC1 and AC2 against HEAD; the builder found them holding at `46e317547`.
3. Change nothing else. Keep every criterion's number. Cite code as `path#symbol` or `path@<blob8>:<line>`; pin any
   count. Keep the status `INPROGRESS`. One revision-log line names this brief and the return by their file stems.
4. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec carries its next rev with the item folded and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec, and above all not unit 49's. No product code. No change beyond the item.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md` alone.

### Reuse

The deviation records already in this build's `build/`, such as TOOL-dBoundRoles-16's, are the shape to follow.
