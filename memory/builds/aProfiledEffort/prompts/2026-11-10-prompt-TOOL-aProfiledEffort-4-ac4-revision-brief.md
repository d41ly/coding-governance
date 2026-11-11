# Brief — aProfiledEffort: unit 4's AC4 counts a line the tree already holds

**Serves:** research TOOL-aProfiledEffort-4

## The brief

### Goal
DIVERGENCE: spec section 6, AC4 (memory/builds/aProfiledEffort/spec/2026-11-10-spec-TOOL-aProfiledEffort-4.md). AC4 says `grep -c 'if not words:' $L` prints `1` after the build. With the guard built exactly as section 4 "The resolver" spells it, the command prints `2`: tools/roles/roles_lib.py already holds `elif not words:` at line 507, inside `load_policy`'s profile loop, and the unanchored pattern matches it as a substring. The count is `1` at HEAD 5b7edfe1c before any edit, so the criterion as written is green before the unit and red after it. The design and the criterion cannot both hold, and a builder may neither reword the guard nor touch line 507 to make the count fit. What the spec would have to say: AC4's grep anchored to the new line, for example `grep -c '^    if not words:' $L` prints `1` (it prints `0` at HEAD, since line 507 is an `elif` at eight spaces), with a `figure:` line pinning that 0. Nothing else diverged. Every path I changed is restored and nothing is committed.

### Items
1. AC4's grep is anchored to the new guard's line, so it reads 0 at `5b7edfe1c` and 1 after the build, with the figure pinned.
2. The spec says whether the builder's three unspelled edits are in scope: the `print_agent_lines` docstring no longer naming the agent types as a source, the `PATH_ID_RE` comment dropping its clause about a role naming an agent type, and the roles README's limits paragraph introducing the two stage names with "which today is".
3. The spec takes a rev bump to rev-2 and a §9 line naming this record.

### Acceptance
1. `grep -c '^    if not words:' tools/roles/roles_lib.py` prints `0` at `5b7edfe1c`, and AC4 pins that figure.
2. `python tools/check-spec-tokens.py` prints no hit for this spec.

### Gates
spec tokens · memory hygiene.

### Non-goals
Any other criterion, the design of section 4, any sibling spec, any code.

### Limitations
Records only. The main loop runs the token check and commits; the writer runs no hygiene pass over the whole tree.

### Reuse
The builder's patch of the whole unit is kept in the session scratchpad and re-applies once AC4 is revised.
