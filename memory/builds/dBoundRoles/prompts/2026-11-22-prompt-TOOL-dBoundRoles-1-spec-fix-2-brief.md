**Serves:** journal TOOL-dBoundRoles-1

# Brief — dBoundRoles: TOOL-dBoundRoles-1 revised over its second builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 1's second builder (run `wf_34a1cec1-85d`) stopped before its code
on rev-7: the roles library refuses the hyphenated schema key `acts-as` at import. Its return is
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-1-2-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md` to rev-8 so its `layer` and `acts-as`
schema rows can be added without breaking the roles library's import.

### Items

1. Record the fork as §8 F12, RESOLVED (agent, 2026-11-22, delegated), rung 3, `widens:` Files touched by
   `tools/roles/roles_lib.py` · `relaxes: none`: option (a). `load_role_schema`'s key grammar widens to a hyphenated
   word (letters and digits, single hyphens between them), stated in S1 with the regex; S1 names the `SCHEMA_SHAPES`
   value each new row takes, adding a shape only where no existing one grades the value, and AC1 or AC2 observes the
   widened grammar (a hyphenated key loads; a key with a leading, trailing or doubled hyphen is refused). Option (b)
   loses: it departs from the carried clause's spelling of the key.
2. Add `tools/roles/roles_lib.py` to §4 Files touched. Verify every claim the revision adds against HEAD.
3. Change nothing else. Cite code as `path#symbol` or `path@<blob8>:<line>`; pin any count. Keep the status
   `INPROGRESS`. One revision-log line names this brief and the return by their file stems.
4. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec is rev-8 with F12 folded as item 1 states and `roles_lib.py` in Files touched; both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change beyond the schema key grammar and what it forces.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md` alone.

### Reuse

`tools/roles/roles_lib.py#load_role_schema`, the one reader of the schema.
