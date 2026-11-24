**Serves:** journal TOOL-dBoundRoles-92

# Brief — dBoundRoles: TOOL-dBoundRoles-92, promoted by the closing diff review, round 1

## The prompt

> Resume the held unattended build run dBoundRoles on node a and carry its close: the closing review, the owed list, prepare, close, land, wrap-up.

— the session that held the run, 2026-11-24, handing the close over. The closing diff review's round 1 is BLOCKED; its
items are promoted into the units TOOL-dBoundRoles-86 to TOOL-dBoundRoles-92, one mechanism each.

## The brief

### Goal

Write a new Tier-2 spec, `memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-92.md`, by `memory/TEMPLATE-SPEC.md`: status `OPEN`, `rev-1`, dated 2026-11-24, node a,
base `f3ec096a8`, `streams tooling`, and the tail `order 46`. It binds by `**Derived:** PLAY-dClosedLoop-2`, the line
this build's promoted units carry (TOOL-dBoundRoles-52 §8 F1). It is one mechanism: the round-1 closing review's minors, with the atomic step key unit 43 owed.

### The gap

Item M1 to M14 and L1 to L4 of `memory/builds/dBoundRoles/reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md` (findings 5, 7 to 10, 12, 14 to 26 and 30, less the parts H3 and H5 carry). Read that item whole, its **Where**, **What is wrong**,
**Consequence** and **Fix**, and the appendix rows of its findings. The code: each item's own **Where** line. Files it reaches: the files each item's **Fix** names, their suites and floors, `tools/run-gates/selftest-budgets.txt`, `tools/gate-legs.json` through its own renderer or row owner, `tools/roles/kit.toml`.

### Items

1. Probe at HEAD that each stated defect still holds, by the report's own probe or your own, and say how in the spec.
2. One scope item per report item, in the report's order, each taking the report's stated fix (the skeptic's corrected one where it names one), and one last item: the `roles/reviewers-to-gov-reviewer` row of `tools/roles/kit.toml` declares `resume = "atomic"`, as TOOL-dBoundRoles-43 S37 and its §8 F11 resolved and its ledger's AC37 answer owes; the row freezes at the landing, so this is its last pass, and the criterion names the frozen-row check that must read it as unlanded. Where an item's fix is an arm over code that reads correctly today, its criterion is the arm red on the staged break the report names. M4 chooses `max = 4` on the catalogue row over a clamp, with the join check; `tools/policy/catalogue.toml` may be a guarded path, so say which commit route the pass takes. L4 builds on the JSON reading TOOL-dBoundRoles-89 gives `read_scout_return`. Group the criteria by suite, and keep each suite's floor move in one place.
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
8. `python tools/check-spec-tokens.py --spec memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-92.md` and
   `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-92.md` exit 0 before you return.

### Acceptance

The spec exists, OPEN at rev-1, and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec, no product code, no record but this spec. No fix of another item of the report.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-11-24-spec-TOOL-dBoundRoles-92.md` alone. Work at HEAD of this worktree; do not merge or read another branch.

### Reuse

The seams the gap names, and the arms already in the owning suite.
