**Serves:** research TOOL-dBoundRoles-20 TOOL-dBoundRoles-22

# Brief: unit 20's scope as TOOL-dBoundRoles-22 §8 F2 (a) widens it

## The prompt

> resolve all forks with recommendations - record it

— owner, 2026-11-05. TOOL-dBoundRoles-22 §8 F2 is resolved to (a) by the fold the brief
`2026-11-05-prompt-TOOL-dBoundRoles-3-owner-forks.md` drove: "TOOL-dBoundRoles-20 adds the two kinds to
the `activatable` list and composes a scenario's activated rows with gov's and a repository's". That
fold revised spec 22 only, so spec 20 does not carry the scope yet. The same fold resolved
TOOL-dDeclaredLoop-26 §8 F5 to (a), which spec 20's §8 F6 still calls open.

## The brief

### Goal

Make TOOL-dBoundRoles-20 carry the scope TOOL-dBoundRoles-22 §8 F2 (a) gives it, and read
TOOL-dDeclaredLoop-26 §8 F5 as resolved. No other design changes.

### Items

- Spec 20 gains a scope item:
  - The unit adds `kind.role` and `kind.workflow` to TOOL-dDeclaredLoop-27 S3's `activatable` list,
    through that set field's `widens = "add"`.
  - The unit composes a scenario's activated role and workflow rows with gov's and a repository's, by
    the same composition its S3 and S6 use for the declarations.
  - The item gets a files-touched entry and one acceptance criterion that observes a scenario
    activating a role row and a workflow row on a fixture.
- Spec 20 §8 F6: the mention of TOOL-dDeclaredLoop-26 §8 F5 reads it as RESOLVED (owner, 2026-11-05)
  to (a), the `compose` verb.
- Spec 22 changes only if its F2 mark or §3 line must name the scope item spec 20 now carries.

One writer revises `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-20.md`, and spec 22
only as above. Write probe copies only under
`C:/Users/d41ly/AppData/Local/Temp/claude/abaae6cd36b7dece/bc821d4c-b305-40e3-bf2f-7dc1519c57f1/scratchpad/forks/dBoundRoles-cascade/`,
and delete nothing else there. Return, per spec: the rev it reads; the sections moved; and its byte
count.

In every spec you revise:

- Both specs already carry a rev dated 2026-11-05 from this fold. They keep that rev, and their
  2026-11-05 §9 line gains this brief and the sections moved.
- Stay under the class cap of 49152 bytes.

### Acceptance

- `wc -c <spec>` is under 49152.
- Spec 20 names `kind.role`, `kind.workflow` and the scenario composition in a scope item, a
  files-touched entry and an acceptance criterion.
- `grep -n -i "open for the owner" <spec 20>` prints no line outside §9.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Findings that only a
  `gen_build_index.py --write` render cures belong to the main loop.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No file outside specs 20 and 22. No commit, no stage into the real index, no deviation record, no
  `BACKLOG.md` row.
- No fork, and no other build's spec.
