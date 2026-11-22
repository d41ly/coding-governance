**Serves:** journal TOOL-dBoundRoles-21

# Brief — dBoundRoles: TOOL-dBoundRoles-21 revised over its first builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 21's first builder (run `wf_db323633-aff`) stopped before its code:
an unset key of its four rows answers a derived-default refusal, never source `default`. Its return is
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md` to its next rev so every one of the
return's four items is answered and the next builder can build it as written.

### Items

1. Item (1), a §8 fork you resolve by M3's rule as a delegated agent resolution, with `widens:` and `relaxes:` each a
   value or `none`. Option (b), a change to the policy kit's `get`, loses: it changes another build's mechanism and
   public surface (veto 2). Weigh (a), reading the derived-default refusal, against any option inside this unit's own
   write set, such as the unit's own catalogue edit giving the four rows a literal default the reader maps to unset;
   probe each against HEAD before you pick, and state what the pick does not check.
2. Item (2): state where the policy kit search starts and what reader the render selftest's fixtures see, so every
   selftest arm can pass on a correct build.
3. Item (3): either list `render_agents.py#run_mode` and the handoff render's grant read among S7's readers, or have
   `load_policy` return the merged grant (the role field, else the house row) so every reader takes it; pick by M3 and
   record it.
4. Item (4): add `.governance/policy.json` to Files touched, rewritten as its render by `policy.py mirror --write` in
   the pass commit, the route units 44 F5 and 51 F3 record, and keep `.claude/agents/` and `.claude/roles.json` there.
5. Keep every criterion passable on a correct build and red on the break it names; keep each criterion's number. Cite
   code as `path#symbol` or `path@<blob8>:<line>`; pin any count. Keep the status `INPROGRESS`. One revision-log line
   names this brief and the return by their file stems.
6. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec carries its next rev with items 1 to 4 folded; both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change to the unit's mechanism beyond what the four items force.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md` alone.

### Reuse

`tools/policy/policy.py#read_default_value` and the four catalogue rows the return cites.
