# Review 2 — adversarial pass over the U1 flatten sub-spec

**Scope:** `spec/units/2026-08-08-spec-aFoldedQuarry-3-u1-flatten.md` at rev-1, before any code.
**Method:** for each check the unit retargets, ask what happens if the retarget is WRONG rather than
absent — a path regex that stops matching prints nothing, and nothing is what a passing gate prints.

| # | Severity | Where | Finding |
|---|---|---|---|
| F1 | blocker | §2, §6 AC1 | a mis-retargeted path regex makes a check VACUOUS, and the bar goes green |
| F2 | high | §6 AC7 | `git log --follow` cannot fail, so it is not an acceptance criterion |
| F3 | high | §2 S8 | the generator's unit list still names the deleted discipline trees |
| F4 | medium | §2 S1 | relative links inside a moved build folder change depth |
| F5 | medium | §2 S5 | the cutoff arms the requirement for the NEXT session, which is unsaid |
| F6 | low | §4 | the optional FAMILY qualifier needs the closed alternation, not `[A-Z]+` |

## F1 — the whole unit's risk is vacuity, and rev-1 has no guard against it (blocker)

Six populations are selected by a path regex whose segment count is about to change:

| Selector | Today | After the flatten |
|---|---|---|
| check 4 | `^$M/$disc/builds/[^/]+/` | `^$M/builds/[^/]+/` |
| check 5 | `^$M/[^/]+/builds/[^/]+/(prompts\|spec\|build\|reviews)/[^/]+\.md$` | one segment shorter |
| check 8 `STATUS.md` | `^$M/[^/]+/builds/[^/]+/STATUS\.md$` | one segment shorter |
| check 12 spec glob | `^$M/[^/]+/builds/[^/]+/spec/…` | one segment shorter |
| `index_set` STATUS rows | `^$M/[^/]+/builds/[^/]+/STATUS\.md$` | one segment shorter |
| check 10 archive | `^$M/$d/archive/…` | `^$M/archive/…` |

Leave ANY of them with the old segment count and it matches zero paths. `grep … || true` then yields
an empty result, `[ -n "$bad" ]` is false, and the check prints nothing — which is exactly what a
passing check prints. The gate would go green over an unlinted tree, and the failure would be
invisible until the first real violation slipped through months later.

This is the same class as U6's empty-population arms, and it needs the same remedy, so a scope item
is added: **S11 — every retargeted population asserts it is NON-EMPTY.** A selector that matches
nothing on a tree that demonstrably has specs, build folders and STATUS files is a defect, and the
check must say so instead of passing. The assertion is cheap (a count) and it is the only thing
standing between a typo'd regex and a silently disarmed gate.

## F2 — `git log --follow` cannot distinguish `git mv` from delete-plus-add (high)

AC7 proposed proving the migration preserved history by running `git log --follow` on a moved file.
Git does not record renames; `--follow` reconstructs them heuristically at read time and returns the
same answer whether the move was staged as a rename or as a delete plus an add. The criterion is
therefore satisfiable by any migration method, including a wrong one, so it measures nothing.

Replaced with a criterion that can fail: the tracked file COUNT under the memory root is unchanged
except for the deliberate merges, and every pre-migration path resolves to exactly one
post-migration path. That is checkable from the diff and it goes red if a file is dropped.

## F3 — the generator would report the deleted discipline trees as stale (high)

`gen-memory-tree.sh` iterates `UNITS="root $DISCIPLINES"` and, in `--check`, treats an absent target
as drift. After the discipline directories are deleted, `--check` would report four missing
`TREE.md` files and check 9 would red on every run. S8 says the generator moves to the flat shape;
the specific consequence — `UNITS` narrows to `root`, and `_render_root` lists the flat children
rather than the disciplines — is now written down rather than left to be discovered from a red bar.

## F4 — a moved build folder is one directory level shallower (medium)

`<MEMORY_ROOT>/<disc>/builds/<folder>/README.md` sits three levels under the memory root; the same
file at `<MEMORY_ROOT>/builds/<slug>/README.md` sits two. Any relative link in a moved file that
climbs out of its own folder resolves somewhere new. Hygiene check 2 catches the broken ones, but
only for `.md` targets and only outside the exempt set, so the migration sweeps them deliberately
rather than waiting for the gate to find some of them.

## F5 — the cutoff arms the requirement for the next session, not this one (medium)

Setting `STREAMS_CUTOFF` strictly ahead of the corpus means every spec written from the following day
onward MUST carry `streams`. That is the intent, but rev-1 states only the grandfathering half, so a
future session would meet the requirement as a surprise from a red gate. Said plainly in S5, and
`SPEC-TEMPLATE.template.md` documents the field the way it already documents the other two cutoffs.

## F6 — the optional FAMILY qualifier must use the closed alternation (low)

`([A-Z]+-)?` would accept `XYZ-` and quietly admit a family that does not exist. The kit already
derives `FAM_ALT` from `FAMILIES`; the qualifier uses that, which is also what makes AC5's rejection
arm meaningful.

## Disposition

All six folded into rev-2 before any code. F1 adds scope item S11; F2 rewrites AC7; the rest sharpen
existing items.
