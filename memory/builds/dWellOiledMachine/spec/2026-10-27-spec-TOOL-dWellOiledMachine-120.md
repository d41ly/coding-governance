# TOOL-dWellOiledMachine-120 — every path to the two unbuilt fixtures that the cross-read writes into a criterion is quoted, so the spec-token join skips it

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 73 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-120-deviation-1201.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-120-deviation-1201.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-6 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md`),
finding 17, item H2, at HIGH. Item H2 carries finding 17 alone.

115 S6 writes `tools/runtime/supervise.py` and `tools/memory-tree/door_fixture.py` unquoted into 108
AC8, a criterion of an OPEN spec. `tools/check-spec-tokens.py` grades every path-shaped word of an
acceptance code span against `git ls-files`, and neither file is tracked until units 90 and 94 build
it. `.unattended.conf` declares that checker as `SPEC_TOKENS_CLI`, and `--dispatch` refuses every
unit while it reds, so from the M2 cross-read on no unit could be dispatched, unit 90 included, which
is the unit that would track the file.

The class is wider than S6. 108 S8 and S9 write the same unquoted pathspec into 97 AC1, 94 AC8 and
90 AC20 as their liveness half, and 108 S10 has 90 AC20 run the walk over the two files without
saying how they are spelled. This unit rewrites 115 S6 so every such write is quoted, and states the
class in 115's §5 risks and §7.

## 2. Scope (IN)

- **S1** — 115 S6 rewritten. Spec 115 takes a rev bump, its §9 line naming this unit and finding 17,
  whose S6 reads: "Finding 3 (M3), with finding 17 of the round-6 promotions audit (H2), on
  TOOL-dWellOiledMachine-108 AC8, S8, S9 and S10. Spec 108's AC8 runs
  `git ls-files --error-unmatch 'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'` in
  place of the bare names, and 108 S8 spells the same quoted pathspec, so 97 AC1 and, through 108 S9,
  94 AC8 and 90 AC20 receive it quoted as their liveness half; 108 S10 has 90 AC20 run its walk over
  `'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'`. Each path sits inside single
  quotes, so the `spec tokens` paths join skips it before units 90 and 94 build the files. Observed by
  AC4." Every code span of that text stays on one line. Observed by AC1, AC2.
- **S2** — 115 §5's risks line gains "An untracked path written unquoted into a criterion's code span
  of an OPEN spec reds the `spec tokens` paths join, and `--dispatch` refuses every unit while it
  does, until the unit that builds the file has built it; S6 quotes every path of this kind that the
  cross-read writes." Observed by AC1.
- **S3** — 115 §7 gains, below its leg line, the sentence "`spec tokens` grades every word of an
  acceptance code span of an OPEN spec, and S6's quoted paths are words it skips (`NOT_A_TOKEN`), so
  the leg stays green before units 90 and 94 build the files." Observed by AC1.
- **S4** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 115 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. It lands before the amendments spec 115 makes are applied, so 108
  receives the quoted text before its own amendments of specs 97, 94 and 90 are applied. At this
  unit's own pass, at order 73, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- AC4's clauses that read the result: findings 1, 9 and 18, TOOL-dWellOiledMachine-116 to -118.
- AC6, AC7 and §4's AC10 text, which name the files in 115's own and 108's walk criteria: finding 21,
  TOOL-dWellOiledMachine-119, and findings 4 and 10, TOOL-dWellOiledMachine-121.
- No change to `tools/check-spec-tokens.py` or to the waiver registry: a waiver is shrink-only, and the
  quoted spelling needs none.
- No leg that runs the checker over scratch-applied amendments before the cross-read commit. That is
  the report's left-shift line, a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-115` — S6, §5's risks line and §7, which this unit rewrites before spec 115's amendments land
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

- `tools/check-spec-tokens.py:1565-1576` sends every whitespace word of an acceptance code span
  through `check_path_shaped` (`:1104`), which grades a word carrying `/` and a dotted last segment
  and reports it when `git ls-files` does not hold it. A word matching `NOT_A_TOKEN`
  (`tools/memory-tree/design_lib.py:525`), which includes one opening with `'`, is skipped. A probe
  run 2026-10-27 printed `False` for `'tools/runtime/supervise.py'` and `True` for the unquoted path.
- `.unattended.conf:201` sets `SPEC_TOKENS_CLI="tools/check-spec-tokens.py"`, and `--dispatch`
  (`tools/unattended/unattended.sh:13670-13682`) runs it and refuses the unit when it exits non-zero.
- At HEAD 63dbec5e8, neither path is tracked: `git ls-files --error-unmatch` exits 1 on both.
- At HEAD 63dbec5e8, the pattern AC1 names counts 2 unquoted paths in 115 S6 and 2 in 108 S8, and 0
  in the §6 of each of specs 90, 94, 97, 108 and 115, so every hit would arrive with the cross-read.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-115.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 115's rev cell moves)

### Alternatives rejected

- **Write the bare names, which this repo's paths join does not grade.** That is finding 3's defect:
  a bare pathspec matches only a file at the repository root.
- **Quote 108 AC8 alone, as the report's fix does.** 108 S8 and S9 carry the same pathspec into three
  more criteria, and one unquoted copy keeps `--dispatch` refusing.
- **Amend 108 S8 to S10 from this unit directly.** 115 already amends spec 108 at the same cross-read,
  so one more clause in 115 S6 reaches 108 without a second editor of it.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — greps over five sections.
- error / empty / loading states — an unquoted copy anywhere in the five sections counts 1 or more and
  reads red.
- observability — AC2 prints the count per spec.
- risks — the probe matches the two paths only; another untracked path is the checker's to report.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`,
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`, `<§K of spec N>` is
`awk '/^## K\./{p=1;next} /^## [0-9]+\./{p=0} p' <spec N> | tr -s '\n ' ' '` for section number K,
and `<unquoted>` is
`grep -oE "(^|[^'\"])tools/(runtime/supervise|memory-tree/door_fixture)[.]py" | grep -c .`. Each
command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6 states.

- **AC1** — When `<S6 of spec 115>` is piped to
  `grep -c "'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'"` it prints 1 and piped
  to `<unquoted>` it prints 0, while `git show 63dbec5e8:<spec 115>` sliced to S6 the same way and
  piped to `<unquoted>` prints 2; and `<§5 of spec 115>` piped to
  `grep -c "refuses every unit while it does"` and `<§7 of spec 115>` piped to
  `grep -c "are words it skips"` each print 1, and `<S8 of spec 108>` piped to `<unquoted>` prints 0.
  Red when: S6 writes an untracked path unquoted, or §5 and §7 leave the class unstated.
- **AC2** — When `awk '/^## 6\./{p=1;next} /^## 7\./{p=0} p'` runs over each of `<spec 90>`,
  `<spec 94>`, `<spec 97>`, `<spec 108>` and `<spec 115>` at this unit's pass, after the cross-read has
  applied every amendment, each piped to `<unquoted>` prints 0; and `<AC8 of spec 108>` and
  `<AC1 of spec 97>` piped to `grep -c "'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'"`
  each print 1.
  Red when: a chained amendment carried an unquoted copy into a criterion, so `--dispatch` would have
  refused every unit after the cross-read.
- **AC3** — When `check_amended_before_built 115 120 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 115 lands after unit 90's build commit, the earliest build
  that spec 115's corrections reach, as 115 AC17's pair for spec 98 names.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass. This
spec's own criteria name the two paths only inside quotes, so its own `spec tokens` reading is
unaffected by them.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-6 promotions, finding
  17 (H2).

## 10. Reuse audit

The seam reused is the spec-token checker's own skip rule, `NOT_A_TOKEN`
(`tools/memory-tree/design_lib.py:525`), which `check_path_shaped` in `tools/check-spec-tokens.py`
applies to every word; quoting a path uses that rule rather than adding a waiver row or a new
exemption. The ordering is TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`).

Probe: `python tools/codebase-map/reuse_lookup.py "skip a quoted word when grading a path token in a spec criterion"`
ranked name-stem neighbours only (`skip`, `resolve_prefix_token`, `read_spec_revisions`); the skip rule
was found by reading `check_path_shaped`. The recall query below ranked two earlier briefs that
already tell a writer to quote an untracked path inside a command, and this finding's report.

Recall terms used: `python tools/memory-recall/query.py "how does a spec criterion name an untracked
path without the spec token join reading it red" --terms "quoted pathspec untracked path spec tokens
criterion code span full path bare name error-unmatch"`
