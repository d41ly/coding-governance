# TOOL-dWellOiledMachine-126 — the round-7 promotions audit's 11 medium and low findings, batched: 97 S1's unquoted pathspec, criteria that observe 108 S8 and S10 and the edges, the token checker's own predicate, a positive count that can fail, a pinned held_halves read and observers that read 115

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 76 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-126-deviation-1261.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-126-deviation-1261.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-7 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md`)
exited CONVERGED with 11 confirmed findings below HIGH. BUILD-METHOD M4 promotes every one of them,
batched into ONE unit, and this is that unit. It closes, by report id:

- MEDIUM (7): 3, 4, 7, 10, 11, 14, 16.
- LOW (4): 5, 8, 12, 15.

Several findings share a report item (M1: 4, 7, 10; M3: 11, 16; L1: 5, 12), and each keeps its own
scope item here. Findings 8 and 15 are taken at their skeptics' low grade, which binds. Each finding
takes the fix its skeptic judged SOUND; finding 15 takes the skeptic's corrected fix, and finding 8
takes the reading of its fix that a pass can make (§4, "Finding 8").

The findings land on specs 120 and 121, so this unit repairs none in particular and sits after every
unit of the build. One unit, not two: the halves on 120 and on 121 are disjoint by spec, but each
moves a rev cell of the one README render (M6 clause 3), and TOOL-dWellOiledMachine-122 to -125 also
write spec 121.

## 2. Scope (IN)

Each item names its finding, its report item and the spec it amends. "Spec N takes a rev bump" means
spec N is amended by S12's route, its §9 line naming this unit and the finding. §4 spells each final
text once; an item points at it rather than restating it.

- **S1** — Finding 4 (M1), on 120 S1. Spec 120 takes a rev bump whose S1 text for 115 S6 has 108 S10
  also set 97 S1's clause for 94 AC8 to run 90 AC20's walk over the quoted pair, in place of its
  `git grep` line and that line's unquoted pathspec, as §4 spells. Observed by AC1.
- **S2** — Finding 7 (M1), on 120 §1 and §4 Evidence. 120's class paragraph names 97 S1 as a third
  carrier, and its fourth Evidence bullet counts 97 S1's 2 unquoted paths, as §4 spells. Observed by
  AC1.
- **S3** — Finding 10 (M1), on 120 AC1. AC1 gains a clause reading `<S1 of spec 97>` through
  `<unquoted>`, which prints 2 at 454dbf8d7 and must print 0 after the cross-read, as §4 spells.
  Observed by AC1.
- **S4** — Finding 14 (M4), on 120 S1 and AC1. 120 S1's text has 115 AC4 gain a clause reading
  `<S8 of spec 108>` and `<S10 of spec 108>`, and has 115 S6 end "Observed by AC4's clause on 108 S8
  and S10" in place of "Observed by AC4"; 120 AC1 reads that clause in 115 AC4, as §4 spells.
  Observed by AC2.
- **S5** — Finding 5 (L1), on 120 S1. 120's rev bump of spec 115 adds S8 and S9 to 115's
  consumes-from line to TOOL-dWellOiledMachine-108, and 120 S1's text for 115 S6 has the rev bump of
  spec 108 that applies it add S8 and S9 to 108's hands-off line to TOOL-dWellOiledMachine-115, as §4
  spells. Observed by AC3.
- **S6** — Finding 12 (L1), on 120 §4 Files touched and AC1. Files touched names the edge edit in
  spec 115 and says the edge edit in spec 108 is made by 115's own amendment of 108; 120 AC1 greps
  both edge lines for S8 and S9, as §4 spells. Observed by AC3.
- **S7** — Finding 8 (L2), on 120 §6 preamble, AC2, §5 and §10. The preamble gains `<graded>`, a
  probe that calls the spec-token checker's own `check_path_shaped`; AC2 runs it over the five specs
  and over a staged file the regex misses; AC2's red case names what `<graded>` observes; §5 says
  `<unquoted>` approximates the checker; §10 names the checker's functions as the seam, as §4 spells.
  Observed by AC4.
- **S8** — Finding 3 (M2), on 121 AC1 and the AC6 row of 121 §4. Each positive count
  `grep -c "subprocess calls"` reads `grep -c "exactly the line .subprocess calls"`, a phrase the
  walk's own code never spells. Observed by AC5.
- **S9** — Finding 11 (M3), on 121 AC11. AC11 runs the walk over `tools/run-gates/held_halves.py`
  as committed at 63dbec5e8, written to the run's scratch directory, in place of the live file, as §4
  spells. Observed by AC6.
- **S10** — Finding 16 (M3), on 121 S15, §4's text for 115 §4 Evidence's first bullet, and AC11. The
  Evidence text names the revision, "`tools/run-gates/held_halves.py` at 63dbec5e8", S15 says so,
  and AC11 counts the phrase in 115 §4. Observed by AC6.
- **S11** — Finding 15 (L3), on 121 AC1 and AC10. AC1 reads `<AC6 of spec 115>` and AC10 reads
  `<AC8 of spec 115>`, `<AC9 of spec 115>` and `<AC6 of spec 115>`, so 121 S1 and S14's "Observed
  by" pointers name criteria that read the clauses they add, as §4 spells. Observed by AC7.
- **S12** — The route. Every rev bump above is made by the build run's main loop at BUILD-METHOD M2's
  cross-read, before its first code pass, in a spec pass whose commit touches specs 120 and 121 and
  whose subject names this unit and none of TOOL-dWellOiledMachine-90 to -94. It lands before the
  amendments those two specs make are applied. At this unit's own pass, at order 76, nothing is
  written: the pass runs AC1 to AC8 and records them. Observed by AC8.

## 3. Non-goals (OUT)

- The high items: H1, TOOL-dWellOiledMachine-122 to -124, which own 121 AC4; H2,
  TOOL-dWellOiledMachine-125, which owns 97 AC1's files in 121's 115 S11 text, 121 S2 and the
  97 AC1 clauses of 121 AC1.
- The report's left-shift gates and checklist entries: each finding here is closed by its own
  criterion, and a lint over specs or a checklist row is a separate mechanism (M2).
- No run of `tools/check-spec-tokens.py` as a command at any pass: that is the `spec tokens` leg,
  and a pass runs no gate (M6). `<graded>` calls the checker's functions instead.
- No change to `tools/check-spec-tokens.py` or its waiver registry.
- No code written at this unit's pass: the code the amended specs describe is built by their units.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-120` — S1, §1, §4, §5, §6's preamble, AC1, AC2 and §10, amended before 120's amendment of spec 115 lands (S1 to S7)
- **consumes-from** `TOOL-dWellOiledMachine-121` — S15, §4's AC6 row and 115 Evidence text, AC1, AC10 and AC11, amended before 121's amendments of spec 115 land (S8 to S11)
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC8 loads from spec 95 and calls

## 4. Design

### 120 (S1 to S7)

**120 S1's text for 115 S6** reads: "Finding 3 (M3), with finding 17 of the round-6 promotions audit
(H2) and findings 4, 5 and 14 of the round-7 promotions audit, on TOOL-dWellOiledMachine-108 AC8, S8,
S9 and S10. Spec 108's AC8 runs
`git ls-files --error-unmatch 'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'` in
place of the bare names, and 108 S8 spells the same quoted pathspec, so 97 AC1 and, through 108 S9,
94 AC8 and 90 AC20 receive it quoted as their liveness half; 108 S10 has 90 AC20 run its walk over
`'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'`, and has 97 S1's clause for 94
AC8 run 90 AC20's walk over the same quoted pair, in place of its `git grep` line and that line's
unquoted pathspec. Each path sits inside single quotes, so the `spec tokens` paths join skips it
before units 90 and 94 build the files. The rev bump of spec 108 that applies this item adds S8 and
S9 to 108's hands-off line to TOOL-dWellOiledMachine-115. Observed by AC4's clause on 108 S8 and
S10."

**120 S1** also says: "115 AC4 gains, before 'Red when:', '; and `<S8 of spec 108>` and
`<S10 of spec 108>` are each piped to
`grep -c "'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'"`, each printing 1, and to
`grep -oE "(^|[^'\"])tools/(runtime/supervise|memory-tree/door_fixture)[.]py" | grep -c .`, each
printing 0', and its red case gains ', or 108 S8 or S10 leaves a fixture path unquoted' before its
full stop. This rev bump of spec 115 also writes S8 and S9 before S10 in 115's consumes-from line to
TOOL-dWellOiledMachine-108."

**120 §1's class paragraph** gains, after its first sentence: "97 S1 writes it unquoted as well, as
the population of the `git grep` line it sets as 94 AC8."

**120 §4 Evidence's fourth bullet** reads: "At HEAD 63dbec5e8, the pattern AC1 names counts 2
unquoted paths in 115 S6, 2 in 108 S8 and 2 in 97 S1, and 0 in the §6 of each of specs 90, 94, 97,
108 and 115, so every hit would arrive with the cross-read."

**120 §4 Files touched** gains, under spec 115's line: "(also its §3 consumes-from line to
TOOL-dWellOiledMachine-108, which gains S8 and S9; 108's hands-off line to TOOL-dWellOiledMachine-115
gains them through 115's own amendment of spec 108, outside this unit's write set)".

**120 §6 preamble** gains: "`<graded>` is
`python -c 'import importlib.util as u,re,subprocess,sys;s=u.spec_from_file_location("cst","tools/check-spec-tokens.py");m=u.module_from_spec(s);s.loader.exec_module(m);F=set(subprocess.run(["git","ls-tree","-r","--name-only","0689e7fa"],capture_output=True,text=True).stdout.split());[print(p,w) for p in sys.argv[1:] for b in re.findall(r"^- .*(?:\n\x20\x20.*)*",m.extract_acceptance(open(p,encoding="utf-8").read()) or "",re.M) for t in m.TICK.findall(b) for w in t.split() if m.check_path_shaped(w,F) and w not in F]'`,
which prints `<spec> <word>` for each word of an acceptance bullet's code span that the checker's own
`check_path_shaped` grades and the tree at base 0689e7fa does not track; that is the tree the cross-read
meets, before units 90 and 94 build the two files." The code span stays on one line.

**120 AC1** gains, before "Red when:": "; `<S1 of spec 97>` piped to `<unquoted>` prints 0, while
`git show 454dbf8d7:<spec 97>` sliced to S1 the same way prints 2; `<AC4 of spec 115>` piped to
`grep -cF "<S10 of spec 108>"` prints 1; and the consumes-from line of `<spec 115>` naming
TOOL-dWellOiledMachine-108 and the hands-off line of `<spec 108>` naming TOOL-dWellOiledMachine-115,
each piped to `grep -c "S8, S9, S10"`, print 1". Its red case gains ", or 97 S1, 115 AC4 or an edge
line was left as the round-7 promotions audit found it".

**120 AC2** gains, before "Red when:": "; `<graded>` run over the same five specs and piped to
`grep -c "supervise.py\|door_fixture.py"` prints 0; and over a scratch markdown file holding an
`## 6. Acceptance criteria` heading and one bullet whose only code span is the supervisor's quoted
path prefixed by `--path=`, `<graded>` prints one line while that file's §6 piped to `<unquoted>`
prints 0. Fixture: one scratch markdown file in the run's scratch directory." Its red case reads
"Red when: a chained amendment wrote a fixture path into a criterion's code span in a form the
spec-token checker's own predicate grades against the tree the cross-read meets, or `<graded>`
misses the form `<unquoted>` misses."

**120 §5's risks line** gains: "`<unquoted>` approximates `check_path_shaped` in both directions: it
reads 0 on a quoted path behind `--path=`, which the checker grades, and counts an unquoted path in §6
prose, which the checker never reads. It stays as the spelling half; the verdict on what the checker
grades is `<graded>`'s, which still repeats the checker's bullet pattern
(`tools/check-spec-tokens.py:1560`)."

**120 §10** gains: "`<graded>` calls `check_path_shaped` (`tools/check-spec-tokens.py:1104`),
`extract_acceptance` (`:539`) and `TICK` (`:315`) from the checker itself, so AC2's verdict is the
checker's rather than a regex copy of it (round-7 promotions audit, finding 8)."

### 121 (S8 to S11)

**121 AC1** reads, apart from the 97 AC1 clauses TOOL-dWellOiledMachine-125 adds: "When
`<AC8 of spec 94>`, `<S1 of spec 97>` and `<AC1 of spec 97>` are each piped to
`grep -cE "prints nothing|expecting no output"`, each prints 0, and to
`grep -c "exactly the line .subprocess calls"` each prints 1; `<S11 of spec 115>` piped to
`grep -c "expecting exactly the line"` and to `grep -c "it prints exactly the line"` each prints 1;
and `<AC6 of spec 115>` piped to `grep -c "expecting no output"` prints 1." This unit leaves its red
case as TOOL-dWellOiledMachine-125 sets it.

**The AC6 row of 121 §4**, the consumer clause: "`<AC20 of spec 90>`, `<AC8 of spec 94>`,
`<S1 of spec 97>` and `<AC1 of spec 97>` each piped to `grep -c "exactly the line .subprocess calls"`
print 1 and to `grep -cE "prints nothing|expecting no output"` print 0", in place of the
`grep -c "subprocess calls"` count. The rest of the row stays.

**121 AC10** gains, before "Red when:": "; and `<AC8 of spec 115>` piped to
`grep -c "lib-unattended.sh:1149"`, `<AC9 of spec 115>` piped to `grep -c "abb97.XXXXXX"` and
`<AC6 of spec 115>` piped to `grep -cF "awk '/^## 10"` each print 1".

**121 AC11** reads: "When `<§4 of spec 115>` and `<§4 of spec 108>` are each piped to
`grep -c "129, 516, 518, 519, 520 and 543"`, each prints 1, and `<§4 of spec 115>` piped to
`grep -c "held_halves.py. at 63dbec5e8"` prints 1; and when
`git show "63dbec5e8:tools/run-gates/held_halves.py" > "$SCRATCH/held_halves.py"` has run, with
`$SCRATCH` the run's scratch directory, `eval "<walk>" "$SCRATCH/held_halves.py"` prints those six
line numbers and `subprocess calls 1`. Red when: the Evidence line understates what the walk prints
over the file at the revision it names."

**121 S15** gains, after "`tools/run-gates/held_halves.py`", " at 63dbec5e8, the revision AC11
reads, since no unit of this build owns that file". **121 §4's text for 115 §4 Evidence's first
bullet** reads "Over `tools/run-gates/held_halves.py` at 63dbec5e8 it printed lines" in place of
"Over `tools/run-gates/held_halves.py` it printed lines".

### Finding 8

The report's fix asks AC2 to run `python tools/check-spec-tokens.py`. That command is the
`spec tokens` leg, and a pass runs no gate (M6), so the role hook would refuse the criterion. The
fix's own aim is that a criterion about the checker's verdict calls the checker, not a regex copy.
`<graded>` loads the checker as a module and calls its predicate, so it gets that aim inside a pass.
It reads the tree at base, not the live tree: at 120's pass units 90 and 94 have built, both paths
are tracked, and a live read would print nothing whatever the spelling. That is a selector that
cannot fail.

### Evidence

Each finding's evidence is its row of the report's appendix, which its skeptic re-read and confirmed.
Probes re-run for this spec on 2026-10-27, at HEAD 454dbf8d7:

- `<S1 of spec 97>` piped to 120's `<unquoted>` prints 2; `<S8 of spec 108>` counts the quoted pair 0
  times and `<unquoted>` 2; `<S10 of spec 108>` counts the quoted pair 0 times (S1 to S4).
- 115's consumes-from line to TOOL-dWellOiledMachine-108 (spec 115 line 178) and 108's hands-off
  line to TOOL-dWellOiledMachine-115 (spec 108 line 156) each list "S10, S11, S21, §4, AC8, AC10,
  AC11, AC15 and AC19" (S5, S6).
- `<graded>` over a scratch spec whose acceptance bullet holds the supervisor's quoted path behind
  `--path=` and, on a continuation line, the door fixture's bare path printed both words, while
  `<unquoted>` over its §6 counted 1, the bare one. Over specs 90, 94, 97, 108 and 115 it printed
  nothing (S7).
- `<S1 of spec 97>` counts `exactly the line .subprocess calls` 0 times; 121 §4 and 121 AC1 each
  carry `grep -c "subprocess calls"` once (S8).
- The walk 121 §4 spells, run over `tools/run-gates/held_halves.py` read by `git show` at
  63dbec5e8, printed lines 129, 516, 518, 519, 520 and 543, then `subprocess calls 1`; the file's
  last commit is dc732dba3, from dRedressedBar (S9, S10).

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-120.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-121.md`
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since two rev cells move)

### Alternatives rejected

- **Delete 97 S1's `git grep` clause for 94 AC8 instead of spelling its population (S1).** 94 AC8
  still runs the walk over the two files, so the population must be spelled somewhere; spelling it
  beside 90 AC20's in 108 S10 keeps one sentence for both.
- **Run `python tools/check-spec-tokens.py` in AC2 (S7).** It is the `spec tokens` leg, refused
  inside a pass (M6).
- **Keep `<unquoted>` alone and only soften AC2's red case (S7).** It leaves AC2 unable to see the
  `--path=` form the checker grades.
- **Two batches, {120} and {121}.** The write sets are disjoint by spec, but both halves move rev
  cells of the one README render (M6 clause 3).

## 5. Production-readiness checklist

- security — N/A — spec text and criteria change; `<graded>` loads a tracked repo tool and runs
  read-only git queries.
- perf / scale — N/A — greps, one walk over one file and one module load.
- error / empty / loading states — a failed module load makes `<graded>` exit non-zero with no lines,
  which the staged file's expected one line reads red; a missing commit makes `git show` fail and the
  walk print no count line.
- observability — `<graded>` prints each graded untracked word with its spec.
- risks — `<graded>` repeats the checker's bullet pattern, so a change to that loop is not followed;
  the staged file catches a probe that grades nothing.
- testing — AC1 to AC8.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`,
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`, and `<§K of spec N>` is
`awk '/^## K\./{p=1;next} /^## [0-9]+\./{p=0} p' <spec N> | tr -s '\n ' ' '` for section number K.
`<unquoted>` is
`grep -oE "(^|[^'\"])tools/(runtime/supervise|memory-tree/door_fixture)[.]py" | grep -c .`, as
spec 120 defines it, and `<walk>` is the code span of `<AC20 of spec 90>` that opens `python -c "`,
cut at its closing quote with `grep -o 'python -c "[^"]*"'`. `$SCRATCH` is the run's scratch
directory. Each command runs from the repository root, and the predicate is loaded as
TOOL-dWellOiledMachine-98 §6 states. Each criterion runs at this unit's pass, after units 90 to 125
have built.

- **AC1** — When `<S1 of spec 120>` is piped to `grep -c "97 S1's clause for 94 AC8"`,
  `<§1 of spec 120>` to `grep -c "population of the .git grep. line"`, `<§4 of spec 120>` to
  `grep -c "2 in 97 S1"` and `<AC1 of spec 120>` to `grep -cF "<S1 of spec 97>"`, each prints 1; and
  `<S1 of spec 97>` piped to `<unquoted>` prints 0.
  Red when: 97 S1's pathspec reaches 94 AC8 unquoted, or 120 still counts two carriers.
- **AC2** — When `<S1 of spec 120>` is piped to `grep -cF "<S10 of spec 108>"` and to
  `grep -c "Observed by AC4's clause on 108 S8 and S10"`, each prints 1; `<AC4 of spec 115>` piped to
  `grep -cF "<S10 of spec 108>"` prints 1; and `git show 454dbf8d7:<spec 108>` sliced to S8 the same
  way and piped to `grep -c "'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'"`
  prints 0.
  Red when: 115 S6 names an observer that never reads 108 S8 or S10.
- **AC3** — When `grep "consumes-from\*\* .TOOL-dWellOiledMachine-108." <spec 115>` and
  `grep "hands-off\*\* .TOOL-dWellOiledMachine-115." <spec 108>` are each piped to
  `grep -c "S8, S9, S10"`, each prints 1, and `<§4 of spec 120>` piped to
  `grep -c "108's hands-off line to TOOL-dWellOiledMachine-115"` prints 1 or more.
  Red when: an edge record understates 115's write set in spec 108.
- **AC4** — When `g=$(grep -o "python -c '[^']*'" <spec 120>)` has run, `eval "$g $SCRATCH/staged.md"`
  over a scratch markdown file holding an `## 6. Acceptance criteria` heading and one bullet whose
  only code span is the supervisor's quoted path prefixed by `--path=` prints one line, and that
  file's §6 piped to `<unquoted>` prints 0; `<AC2 of spec 120>` piped to `grep -cF "<graded>"` prints
  1; and `<§5 of spec 120>` piped to `grep -c "approximates .check_path_shaped."` prints 1.
  fixture: one scratch markdown file in the run's scratch directory.
  Red when: AC2's verdict on the checker still rests on a regex the checker disagrees with.
- **AC5** — When `<AC1 of spec 121>` and `<§4 of spec 121>` are each piped to
  `grep -c "exactly the line .subprocess calls"`, each prints 1, and to
  `grep -cF 'grep -c "subprocess calls"'`, each prints 0; and `<S1 of spec 97>` piped to
  `grep -c "exactly the line .subprocess calls"` prints 1, while `git show 454dbf8d7:<spec 97>` sliced
  to S1 the same way prints 0.
  Red when: a consumer count reads 1 from the walk's own `print` whatever the expectation says.
- **AC6** — When `<AC11 of spec 121>` is piped to `grep -cF '"63dbec5e8:tools/run-gates/held_halves.py"'`,
  `<S15 of spec 121>` to `grep -c "at 63dbec5e8"` and `<§4 of spec 115>` to
  `grep -c "held_halves.py. at 63dbec5e8"`, each prints 1; and after
  `git show "63dbec5e8:tools/run-gates/held_halves.py" > "$SCRATCH/held_halves.py"`,
  `eval "<walk>" "$SCRATCH/held_halves.py"` prints six lines ending 129, 516, 518, 519, 520 and 543,
  then `subprocess calls 1`.
  Red when: AC11 reads a live file that another build can shift before order 74.
- **AC7** — When `<AC1 of spec 121>` is piped to `grep -cF "<AC6 of spec 115>"` and
  `<AC10 of spec 121>` to `grep -cF "<AC8 of spec 115>"` and to `grep -cF "<AC9 of spec 115>"`, each
  prints 1; and `<AC6 of spec 115>` piped to `grep -cF "awk '/^## 10"`, `<AC8 of spec 115>` to
  `grep -c "lib-unattended.sh:1149"` and `<AC9 of spec 115>` to `grep -c "abb97.XXXXXX"` each print 1.
  Red when: the cross-read skipped 121 S1's or S14's clauses in spec 115 and every 121 criterion
  still passed.
- **AC8** — When `for p in 120 121; do check_amended_before_built $p 126 90 || echo $p; done` runs,
  it prints nothing.
  Red when: this batch's rev bump of spec 120 or 121 lands after unit 90's build commit, the earliest
  build their corrections reach through spec 115, and the loop prints that spec.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved at this unit's pass: each criterion is a probe, a grep or a history read,
and the arms the amended units declare stay on their own §7 lines. Each path to the two unbuilt
fixtures in this spec's criteria sits inside quotes or is described in prose.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the round-7 promotions audit's 11 medium and low findings
  batched.

## 10. Reuse audit

Each item extends the seam its finding names: 120's own quoted spelling and `<unquoted>` spelling
check, now beside the spec-token checker's own `check_path_shaped`
(`tools/check-spec-tokens.py:1104`), `extract_acceptance` and `TICK`, loaded as a module rather than
copied; 121's own `<X of spec N>` slices and `<walk>` cut; `git show` at a pinned commit, as 120
AC1 already reads spec 115; and TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`) for the ordering. No module or fixture file is minted.

Probe: `python tools/codebase-map/reuse_lookup.py "grade the path-shaped words of a spec acceptance code span"`
ranked name-stem neighbours only (`shape`, `read_spec_revisions`, `build_spec_path_re`); reading
`tools/check-spec-tokens.py` found `check_path_shaped` and its bullet loop, which `<graded>` calls.
The probe `python tools/codebase-map/reuse_lookup.py "count a token only inside one code span of a spec section"`
returned lexical neighbours only, so no existing seam fits the slices beyond the idioms named above.

Recall terms used: `python tools/memory-recall/query.py "how does a spec criterion name an untracked
path without the spec token join reading it red" --terms "quoted pathspec untracked path spec tokens
criterion code span full path bare name error-unmatch"`
