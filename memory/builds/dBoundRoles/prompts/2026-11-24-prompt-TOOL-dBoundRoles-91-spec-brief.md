**Serves:** journal TOOL-dBoundRoles-91

# Brief — dBoundRoles: TOOL-dBoundRoles-91, promoted by the closing diff review, round 1

## The prompt

> Resume the held unattended build run dBoundRoles on node a and carry its close: the closing review, the owed list, prepare, close, land, wrap-up.

— the session that held the run, 2026-11-24, handing the close over. The closing diff review's round 1 is BLOCKED; its
items are promoted into the units TOOL-dBoundRoles-86 to TOOL-dBoundRoles-92, one mechanism each.

## The brief

### Goal

Write a new Tier-2 spec, `memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-91.md`, by `memory/TEMPLATE-SPEC.md`: status `OPEN`, `rev-1`, dated 2026-11-24, node a,
base `f3ec096a8`, `streams tooling`, and the tail `order 45`. It binds by `**Derived:** PLAY-dClosedLoop-2`, the line
this build's promoted units carry (TOOL-dBoundRoles-52 §8 F1). It is one mechanism: the declaration verb cuts a work order from the composed item kind.

### The gap

Item H5 of `memory/builds/dBoundRoles/reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md` (findings 9 and 13). Read that item whole, its **Where**, **What is wrong**,
**Consequence** and **Fix**, and the appendix rows of its findings. The code: `tools/loop/loop_lib.py#run_declaration_command`, `tools/loop/loop_items.py#read_composed_items` and the caller of `derive_outcome_set`, `tools/roles/handoff.py#read_item_declaration` and its actor compare. Files it reaches: `tools/loop/loop_lib.py`, `tools/loop/loop_items.py`, `tools/roles/handoff.py`, `tools/roles/adopt-roles.test.sh` or the plants of `tools/loop/loop_items.py`, `tools/run-gates/selftest-budgets.txt`, the `help/` page that documents the verb.

### Items

1. Probe at HEAD that each stated defect still holds, by the report's own probe or your own, and say how in the spec.
2. Resolve the row from the composed item kind for the caller's repository through the composition reader with a lazy import, `--root` passed from `handoff.py`; outcomes from the composed row; fall back to gov's rows only where the composition is unarmed and refuse when it refuses; roles through the composed roles, an actor `role:adopter.<name>` normalised to its slot by the existing helper on both sides. Plants: a repository item, an inputs amendment, an actor patch; a join that renders a declaration for every item the composed kind admits in a fixture overlay. The `loop item kind` leg is red at this run's BASE on `record-kind.flake`, which no record-version row pins: do not fix it here, and write each criterion so it passes beside that red.
3. §3 Edges: write no **hands-off** or **consumes-from** bullet naming another unit, since every sibling of this set is
   written in parallel and every earlier unit of the build is CLOSED and frozen; `external` bullets stay allowed. Name
   the units it relates to in prose outside the Edges list.
4. §6 criteria each name the command that observes them, pass on a correct build and red on the break they name.
   §7 lists every leg your Files touched trips (`python tools/check-spec-tokens.py --list` prints them) and one
   `New arm:` line per new arm in the owning suite, with the floor move it owes. The spawn guard's leg is named
   `spawn-guard self-test`.
5. Resolve every fork by M3 as a delegated agent resolution, with `options`, `pick`, `admitted-by`, `widens:` and
   `relaxes:`.
6. §10 reuse audit, with `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and a recall query, each named.
   The seam to extend first is the code the gap names.
7. Cite code as `path#symbol` or `path@<blob8>:<line>`, never a bare `path:line`; pin any count; never set a number
   before a counted noun in prose, and never write a section number beside one.
8. `python tools/check-spec-tokens.py --spec memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-91.md` and
   `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-91.md` exit 0 before you return.

### Acceptance

The spec exists, OPEN at rev-1, and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec, no product code, no record but this spec. No fix of another item of the report.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-91.md` alone. Work at HEAD of this worktree; do not merge or read another branch.

### Reuse

The seams the gap names, and the arms already in the owning suite.
