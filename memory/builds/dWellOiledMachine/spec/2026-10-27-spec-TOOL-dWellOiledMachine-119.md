# TOOL-dWellOiledMachine-119 — spec 115's AC6 runs 90 AC20's walk over the two files at their repository paths

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 73 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-119-deviation-1191.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-119-deviation-1191.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-6 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md`),
finding 21, item H1, at HIGH. Item H1 merges findings 1, 9, 18 and 21, and each takes its own unit:
finding 1 is TOOL-dWellOiledMachine-116, finding 9 is TOOL-dWellOiledMachine-117 and finding 18 is
TOOL-dWellOiledMachine-118. Finding 21 names AC4 and AC6; those three units close its AC4 half, and
this unit closes its AC6 half, which the report also carries at medium as finding 10 (item M2) and
at low as finding 4 (item L1), both in TOOL-dWellOiledMachine-121.

115 AC6 runs the walk "over `supervise.py` and `door_fixture.py`", and 115's §6 preamble runs every
command from the repository root. Neither file sits there, so the walk's `open()` raises
`FileNotFoundError`, no `subprocess calls` line is printed, and AC6 is red on a correct build: the
liveness line it exists to observe is never seen over the two real files. This unit spells the two
repository paths in AC6.

## 2. Scope (IN)

- **S1** — 115 AC6's first clause rewritten. Spec 115 takes a rev bump, its §9 line naming this unit
  and finding 21, whose AC6 opens "When 90 AC20's walk runs, as 90 AC20 spells it, over
  `'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'`, it prints one line matching
  `^subprocess calls [1-9]`", in place of the clause over the bare names. The paths are quoted for the
  reason TOOL-dWellOiledMachine-117 S1 gives. Observed by AC1, AC2.
- **S2** — 115 AC6's red case gains ", or it runs over a bare name, which raises `FileNotFoundError`
  from the root and prints no count line" before its full stop. Observed by AC1.
- **S3** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 115 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. It lands before the amendments spec 115 makes are applied. At this
  unit's own pass, at order 73, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- AC4: findings 1, 9 and 18, TOOL-dWellOiledMachine-116 to -118.
- AC7's scratch copy and §4's AC10 text, which name the files the same way: findings 10 and 4,
  TOOL-dWellOiledMachine-121.
- AC6's other clauses, which TOOL-dWellOiledMachine-121 extends for findings 2, 8, 13 and 22.
- The walk itself: findings 13 and 25, TOOL-dWellOiledMachine-121.
- No spec-lint leg that runs each criterion from the repository root. That is the report's left-shift
  line, a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-115` — AC6's first clause and red case, which this unit rewrites before spec 115's amendments land
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

- Re-run 2026-10-27 at HEAD 63dbec5e8: the walk, run from the repository root over `supervise.py`,
  raised `FileNotFoundError: [Errno 2] No such file or directory: 'supervise.py'` and printed no
  count line. Over a scratch file holding one `subprocess.run([resolve_bash(s), s])` it printed
  `subprocess calls 1`.
- 90 S20 names the two fixtures, and 90's Files touched and §7 arm lines place them at
  `tools/runtime/supervise.py` and `tools/memory-tree/door_fixture.py`.

### How AC2 runs the walk

The walk is spelled in 90 AC20 alone (108 S10). AC2 takes it from there: the one code span of
`<AC20 of spec 90>` that opens `python -c "`, up to its closing quote, then appends the two quoted
paths. A walk that reaches 90 AC20 with its arguments already spelled still runs, because AC2 cuts
at the code's closing quote.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-115.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 115's rev cell moves)

### Alternatives rejected

- **"Runs the walk exactly as 90 AC20 spells it", with no paths.** It leaves the files to whatever 90
  AC20 names, and the report's reading of AC6 shows a builder can take the bare names from 115.
- **Run the walk from each file's directory.** 115's §6 preamble fixes the repository root.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — one `python -c` over two files.
- error / empty / loading states — a bare or missing file raises `FileNotFoundError` and prints no
  count line, which reads red.
- observability — the walk prints each bare argv's file and line, then the count.
- risks — none beyond 115's own.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`. Each command runs from the repository root; the
predicate is loaded as TOOL-dWellOiledMachine-98 §6 states.

- **AC1** — When `<AC6 of spec 115>` is piped to
  `grep -c "'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'"` and to
  `grep -c "FileNotFoundError"`, each prints 1, and piped to `grep -c "over .supervise.py. and"` it
  prints 0.
  Red when: AC6 still runs the walk over bare names.
- **AC2** — When `w=$(<AC20 of spec 90> | grep -o 'python -c "[^"]*"')` runs at this unit's pass, after
  unit 90 has built, then `eval "$w 'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'" | tail -1`
  prints a line matching `^subprocess calls [1-9]`, and `eval "$w supervise.py"` exits non-zero.
  Red when: the walk cannot read the two files at their repository paths, or a bare name resolves.
- **AC3** — When `check_amended_before_built 115 119 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 115 lands after unit 90's build commit, the earliest build
  that spec 115's corrections reach, as 115 AC17's pair for spec 98 names.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep, a walk run or a history probe at this unit's
pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-6 promotions, finding
  21 (H1).

## 10. Reuse audit

The seams reused are the walk 90 AC20 carries, run as written rather than retyped, 115's own
`<X of spec N>` slice, and TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`). No new probe is minted.

Probe: `python tools/codebase-map/reuse_lookup.py "flag a subprocess argv that opens with a bare bash literal"`
ranked `resolve_bash` and `resolve_shell_argv` among name-stem hits and no argv guard; the walk 90
AC20 will carry is the one seam, and this unit reuses it. The recall query below ranked this
finding's own report among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how does a guard that flags a bare bash argv
treat the resolve_shell_argv fallback" --terms "bare bash argv walk resolve_bash resolve_shell_argv
fallback exemption subprocess liveness count staged case"`
