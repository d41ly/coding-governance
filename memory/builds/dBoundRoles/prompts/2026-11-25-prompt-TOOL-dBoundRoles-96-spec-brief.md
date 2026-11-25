**Serves:** journal TOOL-dBoundRoles-96

# Brief — dBoundRoles: TOOL-dBoundRoles-96, promoted by the security review of TOOL-dBoundRoles-95

## The prompt

> Unit 23 F6: "Close it before landing".

— the owner's words on 2026-11-25, as the session that started this run quoted them; no answer was typed in this session.
TOOL-dBoundRoles-95 is that fix, and its security review, CLEAN WITH FIXES, holds a high that leaves the property false on a narrow
path, with a medium and two lows. Its items are promoted, batched into this one unit.

## The brief

### Goal

Write a new Tier-2 spec, `memory/builds/dBoundRoles/spec/2026-11-25-spec-TOOL-dBoundRoles-96.md`, by `memory/TEMPLATE-SPEC.md`: status `OPEN`, `rev-1`, dated 2026-11-25, node a,
base `a911378eb`, `streams tooling`, and the tail `order 49`. It binds by `**Derived:** PLAY-dClosedLoop-2`, the line
this build's promoted units carry (TOOL-dBoundRoles-52 §8 F1). It is a security surface.

### The gap

Items H1, M1, L1 and L2 of `memory/builds/dBoundRoles/reviews/2026-11-25-review-TOOL-dBoundRoles-95-security-diff-review-round1.md` (findings 2 to 7; finding 1 is a duplicate). Read each item whole, with its **Fix** and its
**Left-shift**, and the appendix rows of its findings. The review established H1 by reading and executed nothing.

### Items

1. Probe at HEAD that each stated defect or missing arm still holds, H1 by execution: a scratch repository under `%TEMP%` whose
   landed history opened the key and then closed it, a live run's branch, a cap census row taken out, then a catalogue row,
   and `guard.py --staged` admitting the run's change of the policy file. If H1 does not reproduce, say what you ran and return.
2. One scope item per report item, in the report's order, each taking the report's stated fix, the skeptic's class-level one
   where it names one. H1's is `source == "file"` alone. State what a run sees while the landed file reads invalid, and
   that no caller relies on a `last-valid` opening (name each on a **Readers:** line).
3. TOOL-dBoundRoles-95 is CLOSED and frozen: what its value table, its limits and its deviation record 951 state is restated in
   ONE deviation record of this unit, numbered `961`, never in its text. The guard's header, `help/policy.md` and the READMEs lose the
   limit this unit closes and keep the rest.
4. §3 Edges: no **hands-off** or **consumes-from** bullet naming another unit of this build, since each is CLOSED and
   frozen; `external` bullets stay allowed.
5. §6 criteria each name the command that observes them, pass on a correct build and red on the break they name; H1's two
   scenarios red on the present line, M1's plant red on step four put back to the resolver, L1's rows red on the branch or the
   check each covers deleted. Floors and budget rows move in one place each. §7 lists every leg Files touched trips
   (`python tools/check-spec-tokens.py --list` prints them) and one `New arm:` line per new arm.
6. Resolve every fork by M3 as a delegated agent resolution, with `options`, `pick`, `admitted-by`, `widens:` and
   `relaxes:`. A fork M3's vetoes refuse, or one that widens what any agent may write, is left open and returned as such.
7. §10 reuse audit, with `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and a recall query, each named.
8. Cite code as `path#symbol` or `path@<blob8>:<line>`, never a bare `path:line`; pin any count on its own line; never set
   a number before a counted noun in prose, and never write a section number beside one.
9. Files touched names every file, each `help/` page a changed fixture or behaviour documents included.
10. `python tools/check-spec-tokens.py --spec memory/builds/dBoundRoles/spec/2026-11-25-spec-TOOL-dBoundRoles-96.md` and
    `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec memory/builds/dBoundRoles/spec/2026-11-25-spec-TOOL-dBoundRoles-96.md` exit 0 before you return.

### Acceptance

The spec exists, OPEN at rev-1, and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec, no product code, no record but this spec. No change to what the two open values admit, to
`tools/memory-tree/routed_commits.py`, to `tools/loop/position.py` or to anything on `origin/main`.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-11-25-spec-TOOL-dBoundRoles-96.md` alone. Work at HEAD of this worktree; do not merge or read another branch.

### Reuse

`read_guard_value`, `build_guard_repo`, `write_guard_plant` and `write_live_run`, and the cases and plants TOOL-dBoundRoles-95 added.
