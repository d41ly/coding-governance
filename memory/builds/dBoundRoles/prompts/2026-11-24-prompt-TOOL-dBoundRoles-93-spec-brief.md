**Serves:** journal TOOL-dBoundRoles-93

# Brief — dBoundRoles: TOOL-dBoundRoles-93, promoted by the closing diff review, round 2

## The prompt

> Resume the held unattended build run dBoundRoles on node a and carry its close: the closing review, the owed list, prepare, close, land, wrap-up.

— the session that held the run, 2026-11-24, handing the close over. The closing diff review's round 2 is CONVERGED,
CLEAN WITH FIXES, with no blocker and no high; its mediums are promoted, batched into this one unit.

## The brief

### Goal

Write a new Tier-2 spec, `memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-93.md`, by `memory/TEMPLATE-SPEC.md`: status `OPEN`, `rev-1`, dated 2026-11-24, node a,
base `3c9b6ad0e`, `streams tooling`, and the tail `order 47`. It binds by `**Derived:** PLAY-dClosedLoop-2`, the line
this build's promoted units carry (TOOL-dBoundRoles-52 §8 F1). It is the batch of round 2's mediums.

### The gap

Items M1 to M9 of `memory/builds/dBoundRoles/reviews/2026-11-24-review-TOOL-dBoundRoles-86-closing-diff-review-round2.md` (findings 6 and 10 to 17). Read each item whole, with its **Fix** and its **Left-shift**, and the
appendix rows of its findings.

### Items

1. Probe at HEAD that each stated defect or missing arm still holds, by the report's own probe or your own.
2. One scope item per report item, in the report's order, each taking the report's stated fix, the skeptic's
   class-level one where it names one. M1's PowerShell brace fix moves a view every reader of `scanCommandHeads` shares:
   name each on a **Readers:** line with what it sees after, and keep the Bash reading byte for byte. Where an item's fix
   is an arm over code that reads correctly today, its criterion is the arm red on the mutant the report names.
3. §3 Edges: no **hands-off** or **consumes-from** bullet naming another unit, since every earlier unit of the build is
   CLOSED and frozen; `external` bullets stay allowed. Name the units it relates to in prose outside the Edges list.
4. §6 criteria each name the command that observes them, pass on a correct build and red on the break they name, grouped
   by suite, each suite's floor move in one place. §7 lists every leg your Files touched trips
   (`python tools/check-spec-tokens.py --list` prints them) and one `New arm:` line per new arm in the owning suite.
5. Resolve every fork by M3 as a delegated agent resolution, with `options`, `pick`, `admitted-by`, `widens:` and
   `relaxes:`.
6. §10 reuse audit, with `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and a recall query, each named.
7. Cite code as `path#symbol` or `path@<blob8>:<line>`, never a bare `path:line`; pin any count on its own line; never set
   a number before a counted noun in prose, and never write a section number beside one.
8. Files touched names every file, the `help/` page a changed verb or fixture plant documents included.
9. `python tools/check-spec-tokens.py --spec memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-93.md` and
   `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-93.md` exit 0 before you return.

### Acceptance

The spec exists, OPEN at rev-1, and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec, no product code, no record but this spec. No fix of a finding the report refuted: the quote-before-comment
and here-string readings of `buildCommandView` stay as they are, and an ask carries them.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-93.md` alone. Work at HEAD of this worktree; do not merge or read another branch.

### Reuse

The seams the items name, and the arms already in the owning suites.
