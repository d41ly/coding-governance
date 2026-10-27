# TOOL-dWellOiledMachine-109 — spec 108's AC12 greps the full paths over 90's AC20 slice, so it reads red until the rewrite is made

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 71 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-109-deviation-1091.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-109-deviation-1091.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-115 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-5 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md`),
finding 27, item B1, at BLOCKER. Item B1 carries finding 27 alone. The same AC12 is also reported as
finding 4 (item H1, closed by TOOL-dWellOiledMachine-110) and finding 10 (item M4, closed by
TOOL-dWellOiledMachine-115).

Finding 27 is 108 AC12. 108 S12 and S13 require 90's AC20 to spell `tools/runtime/supervise.py` and
`tools/memory-tree/door_fixture.py`, but AC12 greps only the bare names. Each full path contains its
bare name, so AC12 is green before the rewrite and stays green after it. A build that skips the
rewrite of 90 AC20 is certified as done. This unit rewrites AC12 to grep the full paths, so it reads
red on today's spec 90 and green only once the rewrite has landed.

## 2. Scope (IN)

- **S1** — 108 AC12 rewritten. Spec 108 takes a rev bump, its §9 line naming this unit and finding
  27, whose AC12 reads: "When `awk '/^- \*\*AC20\*\*/{p=1} /^- \*\*AC21/{p=0} p' <spec 90> | tr '\n' ' '`
  is piped to `grep -c 'tools/runtime/supervise.py'` and to `grep -c 'tools/memory-tree/door_fixture.py'`,
  each prints 1, and piped to `grep -c 'tools/\*\*'` it prints 0. Red when: 90's AC20 rewrite was
  skipped, so the slice names only the bare `supervise.py` and `door_fixture.py` and both full-path
  counts print 0." Observed by AC1, AC2.
- **S2** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 108 and whose subject names this unit and not
  TOOL-dWellOiledMachine-92. It lands before the amendments spec 108 makes are applied. At this
  unit's own pass, at order 71, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- A criterion that reads the S12 and S13 edits to spec 97: finding 4, TOOL-dWellOiledMachine-110.
- 108 §4 Evidence's base reading of the two full paths: finding 10, TOOL-dWellOiledMachine-115.
- The rewrite of 90 AC20 itself, which 97 S1 and 108 S8 to S12 specify. This unit changes only the
  criterion that observes it.
- No spec-lint leg that runs every grep-count criterion against the base tree. That is the report's
  left-shift line, a separate mechanism (M2), and the open ask TOOL-aHonedRuleset-12 already names
  it.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-108` — AC12, which this unit rewrites before unit 108's pass
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

- Re-run 2026-10-27 at HEAD 05ab0d1f8, the flattened AC20 slice of spec 90 reads "When
  `git grep -nE "\[\"bash\"|\['bash'" -- supervise.py door_fixture.py` runs, it prints nothing.
  Red when: a bare `bash` argv remains." Piped to `grep -c`, it prints 1 for `supervise.py`, 1 for
  `door_fixture.py`, 0 for `tools/runtime/supervise.py`, 0 for `tools/memory-tree/door_fixture.py` and
  0 for `tools/\*\*`. Finding 27's appendix row reads the same.
- After the rewrite, 90's AC20 spells both full paths: 108 S9 gives it the
  `git ls-files --error-unmatch` liveness half that S8 spells with the full paths, and S10's walk
  runs over the same two files. The slice is flattened to one line, so each count is 1 however often
  a path recurs.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-108.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 108's rev cell moves)

### Alternatives rejected

- **Keep the bare names and add a `tools/\*\*` count of 0.** That clause is green at base too.
- **Count occurrences with `grep -o | wc -l`.** How often each path recurs depends on the walk's
  final spelling, which finding 12's fix still moves (TOOL-dWellOiledMachine-115).

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — three greps over one slice.
- error / empty / loading states — an empty slice prints 0 for both full paths, so it reads red.
- observability — AC2 prints the three counts on spec 90 as committed today, beside the counts at
  this unit's pass.
- risks — none beyond 108's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`,
`<AC12 of 108>` is the output of `awk '/^- \*\*AC12\*\*/{p=1} /^- \*\*AC13\*\*/{p=0} p' <spec 108> | tr -s '\n ' ' '`,
and `<slice>` is `awk '/^- \*\*AC20\*\*/{p=1} /^- \*\*AC21/{p=0} p' | tr '\n' ' '`. Each command runs
from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6 states.

- **AC1** — When `<AC12 of 108>` is piped to `grep -c "grep -c 'tools/runtime/supervise.py'"` and to
  `grep -c "grep -c 'tools/memory-tree/door_fixture.py'"`, each prints 1, and piped to
  `grep -c "grep -c 'supervise.py'"` it prints 0.
  Red when: AC12 still greps a bare name that the full path contains.
- **AC2** — When `git show 05ab0d1f8:<spec 90>` is piped to `<slice>` and then to the three counts
  of the rewritten AC12, they print 0, 0 and 0; and when `<spec 90>` at this unit's pass, after unit
  90 has built, is piped the same way, they print 1, 1 and 0.
  Red when: the rewritten AC12 reads green on spec 90 before its AC20 was rewritten.
- **AC3** — When `check_amended_before_built 108 109 92` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 108 lands after unit 92's build commit, the earliest build
  that spec 108's corrections reach (through 97 S20).

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-5 promotions, finding
  27 (B1).

## 10. Reuse audit

The seams reused are spec 108's own `<X of spec N>` slice convention, kept as AC12 already spells
it, and TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`), loaded from spec 95 rather than copied. No new probe is
minted. The recall query below ranked this finding's own report second and TOOL-aHonedRuleset-12
first, the open ask for an anti-vacuity arm that runs criterion greps at base, which §3 leaves to
that ask.

Probe: `python tools/codebase-map/reuse_lookup.py "slice one section of a spec and count a token in it"` returned
lexical neighbours only (`counts` and `slice` in two suites, `read_spec_revisions` in `design_lib.py`);
none slices a spec section for a criterion, so no existing seam fits beyond the idiom named above.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec criterion that is
green before its build made red at base" --terms "criterion green at base bare name full path grep
count flattened slice red case rewrite"`
