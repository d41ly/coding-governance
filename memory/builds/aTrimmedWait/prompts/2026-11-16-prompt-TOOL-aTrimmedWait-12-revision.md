# Revision — TOOL-aTrimmedWait-12: AC13 names a suite

**Serves:** research TOOL-aTrimmedWait-12

## The prompt

The main loop's pass-legs run over `7c3e4d4e5..c50583f10` read one leg red,
`spec tokens (the pass's own spec)`, quoted:

> [bar] `python tools/memory-tree/gen_build_index.py --selftest` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete

AC13 states the selftest as an acceptance observation. Every other leg read green. The pass is
built and the spec is CLOSED; this revision moves prose only.

## The brief

### Goal
Revise TOOL-aTrimmedWait-12 so `check-spec-tokens.py --pass-spec` reads no hit over it.

### Items
1. AC13 leaves §6. What it observed, the selftest exiting 0 on a frozen clone of the merge, is
   stated in §7 as a run the close owes, beside the three conflicted suites, in the form §7 already
   uses for them.
2. Any §5 or Rollout sentence that cites AC13 by id points at §7 instead.

Change nothing else. Bump the revision, keep the header CLOSED, and leave the spec uncommitted: the
main loop commits it.

### Acceptance
- `python tools/check-spec-tokens.py --pass-spec 7c3e4d4e5fd723848b4eed249e9859b652623947 --spec memory/builds/aTrimmedWait/spec/2026-11-16-spec-TOOL-aTrimmedWait-12.md` reads no unwaived hit, or, where that flag pair is refused, `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-16-spec-TOOL-aTrimmedWait-12.md` exits 0 and no line of the spec spells `--selftest` inside §6.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 25 --spec memory/builds/aTrimmedWait/spec/2026-11-16-spec-TOOL-aTrimmedWait-12.md` exits 0.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
No change to any other criterion, to the resolutions, or to any figure.
