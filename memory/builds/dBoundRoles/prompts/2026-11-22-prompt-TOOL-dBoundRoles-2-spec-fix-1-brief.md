**Serves:** journal TOOL-dBoundRoles-2

# Brief — dBoundRoles: TOOL-dBoundRoles-2 revised over its first builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 2's first builder (run `wf_07a97cf8-bbd`) stopped before its code on
rev-4 and returned two blockers and a re-ground list. Its return is
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-2-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-2.md` to rev-5 so every claim it makes about
current code holds at HEAD, and the next builder can build it as written.

### Items

1. Blocker (1), decided by the main loop as a §8 fork, RESOLVED (agent, 2026-11-22, delegated) with
   `widens: none · relaxes: none`: the three sections render at the end of the role, after `## Charter`, through the
   one composition S6 states. AC5 says that order. Moving them inside `render_agent_file` loses: it is a second route.
2. Blocker (2): add `tools/loop/factories.py` and `tools/playbook/kinds.toml` to Files touched and to S5's readers. The
   factory's `--returns` flag gives way to flags writing `never` and `return` in the grammar §4 sets; name the flags,
   the `role-new` fixture's values so it stays green, and the `role-hand` plant so it reds R2 for the missing `writes`
   it names and not for an unknown key. Keep the spelling the lexicon admits.
3. Item (3): re-point every drifted citation the return lists, and add `gov-tester` to S5's readers.
4. Then re-verify every other claim the spec makes about current code against HEAD, reading that code. Re-ground any
   sentence whose code changed in behaviour since the spec's base. TOOL-dBoundRoles-14 is built and CLOSED at
   `7a58950fb`; claims about what it built hold against HEAD.
5. Cite code as `path#symbol` or `path@<blob8>:<line>`, never a bare `path:line`, and put a pin on any line quoting a
   count. Keep every criterion passable on a correct build at HEAD and red on the break it names. Keep the status
   `INPROGRESS`. One revision-log line names this brief by its file stem and the return by its file stem.
6. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec is rev-5 with both blockers folded as items 1 and 2 state; both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change to the unit's mechanism beyond what a blocker or a stale claim forces.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-2.md` alone.

### Reuse

The spec's own §10; `tools/loop/factories.py#write_role` is the seam blocker (2) extends.
