# TOOL-dWellOiledMachine-121 — the round-6 promotions audit's 17 medium and low findings, batched: the walk's consumers and exemption, path spellings, flattened slices, bounded fixture ranges and criteria green at base

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 74 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-121-deviation-1211.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-121-deviation-1211.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-6 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-109-spec-audit.md`)
exited CONVERGED with 17 confirmed findings below HIGH. BUILD-METHOD M4 promotes every one of them,
batched into ONE unit, and this is that unit. It closes, by report id:

- MEDIUM (9): 2, 3, 10, 13, 22, 24, 25, 27, 28.
- LOW (8): 4, 5, 6, 7, 8, 11, 15, 20.

Several findings share a report item (M1: 2, 22; M2 with L1: 10, 4; M7 with L2: 27, 5), and each
keeps its own scope item here. Findings 2, 3 and 22 are taken at their skeptics' medium grade,
finding 28 at its skeptic's medium grade, and findings 4, 5 and 6 at their skeptics' low grade; those
grades bind. Each finding takes the fix its skeptic judged SOUND. Findings 10 and 4 describe the AC6
defect TOOL-dWellOiledMachine-119 closes for finding 21 at HIGH, so here they take the part of
their fix that unit does not: AC7's copy and §4's AC10 text.

The findings land on specs 110, 113, 114 and 115, so this unit repairs none in particular and sits
after every unit of the build. One unit, not two: findings 27 and 5 amend 115 and 110 as one item,
and every amendment moves this build's README rev cells, a generated render two halves would both
write (M6 clause 3).

## 2. Scope (IN)

Each item names its finding, its report item and the spec it amends. "Spec N takes a rev bump" means
spec N is amended by S18's route, its §9 line naming this unit and the finding. §4 spells each final
text once; an item points at it rather than restating it.

- **S1** — Finding 2 (M1), on 115 S11, for 94 AC8. 115's S11 becomes §4's S11 text, whose clause on
  94 AC8 has 108 S10 set 97 S1's "expecting no output" to "expecting exactly the line
  `subprocess calls <k>`". 115 AC6 gains the consumer counts §4 spells. Observed by AC1.
- **S2** — Finding 22 (M1), on 115 S11, for 97 AC1. The same S11 text has 108 S10 set 97 AC1's "it
  prints nothing" to "it prints exactly the line `subprocess calls <k>`", with `k` of 1 or more.
  Observed by AC1.
- **S3** — Finding 3 (M3), on 115 S19, AC12 and §4 Evidence. 115's S19 becomes §4's S19 text, which
  spells the sentence 108 S17 adds to 95 S1's text for 90's S1 and keys 108 AC15's first clause on
  its phrase `tree-wide re-render`; 115 AC12 becomes §4's AC12; 115 §4 Evidence gains §4's line on
  the scratch copy of spec 90 with 95 S1 applied. Observed by AC2.
- **S4** — Finding 10 (M2), on 115 AC7. Its scratch copy names its source,
  `'tools/runtime/supervise.py'`, as §4's AC7 text spells. Observed by AC3.
- **S5** — Finding 13 (M4), on 115 S11, §4 and AC6. The walk exempts nothing: §4's walk is the
  one 115 §4 carries, without the `ok` set; §4's S11 text says why, citing
  `tools/govkit/govkit.py:1200`; 115 §4's "What the walk does not check" holds §4's three bullets in
  place of four; 115 S10 says "three bullets"; and 115 S12's spelling note and AC6's spelling clause
  count `isinstance(n,(ast.List,ast.Tuple))` and require `not in ok` absent. Observed by AC4.
- **S6** — Finding 24 (M5), on 115 AC7. AC7 reads `<S10 of spec 108>` and `<AC8 of spec 94>` for
  the three staged cases 115 S12 adds, as §4's AC7 text spells. Observed by AC5.
- **S7** — Finding 25 (M6), on 115 §4 and AC7. The resolver form held in a variable is staged in AC7
  with its verdict, one `<file> <line>` line: a true red under 90 S20, because the walk exempts
  nothing (S5). Observed by AC4.
- **S8** — Finding 27 (M7), on 115's §6 preamble. `<§4 of spec N>` is flattened with
  `tr -s '\n ' ' '`, as `<X of spec N>` is, so AC2, AC4 and AC5 read a wrapped phrase as one line.
  Observed by AC6.
- **S9** — Finding 28 (M8), on 113 S1 and AC1 and on 114 S1 and AC1. Each S1 names the clause it
  rewrites by its place, the whole-file count that ends AC1 and wraps over two lines, in place of a
  one-line quotation; each AC1 gains "and piped to `grep -c "p'\" <spec 96>"` it prints 0" (spec 97
  in 114), so an appended scoped count beside the old one reads red. Observed by AC7.
- **S10** — Finding 4 (L1), on 115 §4's AC10 text, which S12 sets as 108 AC10. Its walk runs over
  `'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'`, as §4's AC10 text spells.
  Observed by AC3.
- **S11** — Finding 5 (L2), on 110 S2. AC22's §4 clause pipes 97's §4 through `tr -s '\n ' ' '`
  before its count, as §4's AC22 text spells. Observed by AC6.
- **S12** — Finding 6 (L3), on 115's §6 preamble, AC3, AC9 and AC14. The preamble defines
  `<Fixture of spec N>` as `awk '/^### Fixture/{p=1;next} /^### |^## [0-9]+\./{p=0} p' <spec N>`,
  a range that ends at the next sub-head or numbered section; AC3, AC9 and AC14 read it in place of
  their open `sed -n` range. Observed by AC8.
- **S13** — Finding 7 (L4), on 115 AC16. Its count over `<AC11 of spec 108>` keys on
  `Files touched/{p=1;next}`, which only 115 S24 adds, in place of the README path. Observed by AC9.
- **S14** — Finding 8 (L5), on 115 AC6, AC8 and AC9. AC9 counts each fixture directory and §5 line
  115 S14 writes in specs 101, 104 and 107; AC8 counts `lib-unattended.sh:1149` in spec 98; AC6
  counts `test_no_bare_bash_argv` in 108's §10. §4 spells each clause. Observed by AC10.
- **S15** — Finding 11 (L6), on 115 §4 Evidence. Its first bullet becomes §4's Evidence bullet,
  which records every line the walk prints over `tools/run-gates/held_halves.py` and says which are
  never spawned. Observed by AC11.
- **S16** — Finding 15 (L7), on 115 §10 and S11. Both say the walk is modelled on
  `test_no_bare_bash_argv` and leaves it unchanged, and name the two liveness bars, as §4 spells.
  Observed by AC12.
- **S17** — Finding 20 (L8), on 110 S2 and §4 Evidence. AC22's first count reads
  `grep -cF "tr '\n' ' '"`, a token only 108 S12 writes into 97 AC1, in place of `grep -c "AC20"`,
  and 110's third Evidence bullet says 108 S10 also names `AC20` in 97 AC1. Observed by AC13.
- **S18** — The route. Every rev bump above is made by the build run's main loop at BUILD-METHOD M2's
  cross-read, before its first code pass, in a spec pass whose commit touches specs 110, 113, 114 and
  115 and whose subject names this unit and none of TOOL-dWellOiledMachine-90 to -94. It lands before
  the amendments those four specs make are applied. At this unit's own pass, at order 74, nothing is
  written: the pass runs AC1 to AC14 and records them. Observed by AC14.

## 3. Non-goals (OUT)

- The high items: H1, TOOL-dWellOiledMachine-116 to -119; H2, TOOL-dWellOiledMachine-120. AC4,
  AC6's first clause, AC6's bare-name red clause, S6, §5's risks line and §7 are theirs.
- The report's left-shift gates and checklist entries: each finding here is closed by its own
  criterion, and a lint over specs or a checklist row is a separate mechanism (M2).
- No code written at this unit's pass: the code the amended specs describe is built by their units.
- No change to `test_no_bare_bash_argv` (`tools/run-gates/measure_legs.py:2682`): S16 corrects the
  claim that the walk widens it.
- 115 AC14's stale loop check and AC9's `eval` range are kept as written; S12 changes only the range
  each reads its fixture from.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-115` — S10, S11, S12, S19, §4, §6's preamble, AC3, AC6, AC7, AC8, AC9, AC12, AC14, AC16 and §10, amended before 115's own amendments land (S1 to S8, S10, S12 to S16)
- **consumes-from** `TOOL-dWellOiledMachine-110` — S2's AC22 text and §4 Evidence, amended before 110's amendment of spec 108 lands (S11, S17)
- **consumes-from** `TOOL-dWellOiledMachine-113` — S1 and AC1, amended before 113's amendment of spec 103 lands (S9)
- **consumes-from** `TOOL-dWellOiledMachine-114` — S1 and AC1, amended before 114's amendment of spec 106 lands (S9)
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC14 loads from spec 95 and calls

## 4. Design

### The walk, and 115's texts around it (S1, S2, S5, S7, S10, S15, S16)

115 §4's walk, which 108 S10 has 90 AC20 run, becomes this one, its code span on one line:

`python -c "import ast,sys;T=[(f,ast.parse(open(f,encoding='utf-8').read())) for f in sys.argv[1:]];[print(f,n.lineno) for f,t in T for n in ast.walk(t) if isinstance(n,(ast.List,ast.Tuple)) and n.elts and isinstance(n.elts[0],ast.Constant) and n.elts[0].value=='bash'];print('subprocess calls',sum(isinstance(c,ast.Call) and isinstance(c.func,ast.Attribute) and isinstance(c.func.value,ast.Name) and c.func.value.id=='subprocess' for f,t in T for c in ast.walk(t)))"`

115 §4 then says: "The walk exempts nothing. A `bash`-led literal passed to `resolve_shell_argv`,
inline or held in a variable, is flagged, because that function (`tools/govkit/govkit.py:1200`)
returns its argv unchanged, still led by a bare `bash`, when no bash resolves. 90 S20 prescribes
`resolve_bash()` (`tools/lib/resolve_bash.py:15`), whose call leads the argv and is not a literal."

**115 S11** reads: "Finding 16 (M5), with findings 2, 13, 15 and 22 of the round-6 promotions audit,
on 108 S10 and §10. The walk exempts nothing, a `resolve_shell_argv` argument included, for the
reason §4 gives. It prints one last line, `subprocess calls <k>`, a liveness count modelled on
`test_no_bare_bash_argv` (`tools/run-gates/measure_legs.py:2682`). 108 S10 has every consumer of the
walk expect exactly that one line with `k` of 1 or more: 90 AC20; 94 AC8, whose 'expecting no
output' in 97 S1 reads 'expecting exactly the line `subprocess calls <k>`'; and 97 AC1, whose 'it
prints nothing' reads 'it prints exactly the line `subprocess calls <k>`'. S10 and 108 §10 cite
`test_no_bare_bash_argv` as the guard the walk is modelled on and leaves unchanged: that guard scans
only its own `__file__`, reads only calls with `n.args` and asserts `calls >= 3`, while the walk
reads every `bash`-led literal in the two files and expects `k` of 1 or more. Observed by AC6."

**115 §4's AC10 text** (108 AC10) reads: "When 90 AC20's walk runs over
`'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'`, it prints exactly one line,
`subprocess calls <k>` with `k` of 1 or more; over a scratch copy of `'tools/runtime/supervise.py'`
holding S10's six staged cases it prints six `<file> <line>` lines before that one; over a scratch
file whose only spawn is `subprocess.run([resolve_bash(s), s])` it prints only `subprocess calls 1`,
and over one whose only spawn is `subprocess.run(resolve_shell_argv(["bash", "x"]))` it prints one
`<file> <line>` line before it; `grep -c "isinstance(n,(ast.List,ast.Tuple))"` prints 1 over
`<spec 90>` and 0 over `<spec 94>`, `grep -c "not in ok"` prints 0 over `<spec 90>`, and the first
count prints 0 over `<AC1 of spec 97>`. Red when: a variable-held, keyword or concatenated argv
passes, a `resolve_shell_argv` form passes, the `resolve_bash` form reads as bare, or the walk is
spelled in two specs."

**115 S12's last sentence** reads: "108 AC10 becomes §4's AC10 text, whose spelling counts
`isinstance(n,(ast.List,ast.Tuple))` and requires `not in ok` absent, which only this walk
satisfies. Observed by AC7." **115 S10** says "with the three bullets below".

**115 §4's "What the walk does not check"** holds three bullets: an argv whose first element is not
the literal `'bash'` (a name such as `BASH`, `'bash.exe'`, or a path to bash); a command string run
with `shell=True`, `os.system` or `os.exec*`; and a `bash`-led literal that is never spawned, such as
a list of candidate names or a self-test's fixture rows, which it flags as a false red that surfaces
as a deviation and passes nothing wrong. The bullet on the `resolve_shell_argv` exemption has no
successor, because the exemption is gone.

**115 §4 Evidence's first bullet** reads: "The walk above, re-run 2026-10-27 over scratch files,
printed the direct list, the list held in a variable, the `args=` keyword, the walrus target, the `+`
operand, the tuple and the list split across lines, then `subprocess calls 7`. Over
`["bash.exe", "x"]` and `[BASH, "x"]` it printed only the count line. Over
`subprocess.run(resolve_shell_argv(["bash", "x"]))`, and over the same call with the list held in a
variable, it printed one line each, and over `subprocess.run([resolve_bash(s), s])` only the count
line. Over `tools/run-gates/held_halves.py` it printed lines 129, 516, 518, 519, 520 and 543, then
`subprocess calls 1`: line 129 is a row argv, `["bash", SHIM, "--leg"] + list(...)`, that reaches a
spawn later, and lines 516 to 543 are self-test fixture rows and a comparison literal that are never
spawned, the last 'does not check' bullet's class."

**115 §10's** clause on the walk reads: "the walk modelled on `test_no_bare_bash_argv`
(`tools/run-gates/measure_legs.py:2682`), which it leaves unchanged: that guard reads its own file
and asserts at least three calls, and the walk reads the two fixture files and asserts one (S10 to
S12)".

### 115's criteria (S1 to S8, S10, S12 to S14)

The §6 preamble's `<§4 of spec N>` reads
`awk '/^## 4\./{p=1;next} /^## 5\./{p=0} p' <spec N> | tr -s '\n ' ' '`, and the preamble gains
"`<Fixture of spec N>` is `awk '/^### Fixture/{p=1;next} /^### |^## [0-9]+\./{p=0} p' <spec N>`".

| AC | its text after this unit |
|---|---|
| AC3 | "When `<Fixture of spec 96>` and `<Fixture of spec 97>` are each piped to `grep -c "<loader>"`, each prints 1." Its red case stays. |
| AC6 | Its clause `grep -c "id(n) not in ok"` prints 1 over `<spec 90>` reads "`grep -c "isinstance(n,(ast.List,ast.Tuple))"` prints 1 and `grep -c "not in ok"` prints 0 over `<spec 90>`". Before "Red when:" it gains "; `awk '/^## 10\./{p=1} p' <spec 108>` piped to `grep -c "test_no_bare_bash_argv"` prints 1 or more; and `<AC20 of spec 90>`, `<AC8 of spec 94>`, `<S1 of spec 97>` and `<AC1 of spec 97>` each piped to `grep -c "subprocess calls"` print 1 and to `grep -cE "prints nothing\|expecting no output"` print 0". Its red case gains ", or a consumer of the walk still expects no output" before its full stop. Its first clause and the rest of its red case are TOOL-dWellOiledMachine-119's. |
| AC7 | "When 90 AC20's walk runs over a scratch copy of `'tools/runtime/supervise.py'` holding S12's six staged cases, it prints six `<file> <line>` lines and the count line; over a scratch file whose only spawn is `subprocess.run([resolve_bash(s), s])` it prints only `subprocess calls 1`; over a scratch file whose only spawn is `subprocess.run(resolve_shell_argv(["bash", "x"]))`, and over one holding `argv = ["bash", "x.sh"]; subprocess.run(resolve_shell_argv(argv))`, it prints one `<file> <line>` line before `subprocess calls 1`; `<AC10 of spec 108>` piped to `grep -c "isinstance(n,(ast.List,ast.Tuple))"` prints 1 and to `grep -c "isinstance(n.args"` prints 0; and `<S10 of spec 108>` and `<AC8 of spec 94>` are each piped to `grep -cF "cmd = ['bash'"`, `grep -cF "args=['bash'"` and `grep -cF "] + y"`, each printing 1." Fixture: four scratch Python files in the run's scratch directory. Red when: a variable-held, keyword or concatenated argv passes, a `resolve_shell_argv` form passes though it can spawn a bare `bash`, the `resolve_bash` form reads as bare, or 108 S10 and 94 AC8 keep three staged cases. |
| AC8 | Gains "; and `grep -c "lib-unattended.sh:1149"` over `<spec 98>` prints 1" before "Red when:". |
| AC9 | Its first `sed -n` range reads `<Fixture of spec 95>`. Before "Red when:" it gains "; and `grep -c 'abb95.XXXXXX'` over `<spec 101>`, `grep -c 'abb96.XXXXXX'` over `<spec 104>` and `grep -c 'abb97.XXXXXX'` over `<spec 107>` each print 2 or more, and `grep -c "never share a repository"` over each of the three prints 1". |
| AC12 | "When `<AC15 of spec 108>` is piped to `grep -c 'grep -c "tree-wide re-render"'`, it prints 1, and to `grep -c 'grep -c "TOOL-dWellOiledMachine-93"'` and `grep -c 'grep -c "re-render"'` it prints 0; and `<S17 of spec 108>` piped to `grep -c "refreshed by TOOL-dWellOiledMachine-93's tree-wide re-render"` prints 1. Red when: AC15's first clause reads 1 whether or not 108 S17 was applied." |
| AC14 | Its `sed -n` range reads `<Fixture of spec 97>`. |
| AC16 | Its count `grep -c "tools/memory-tree/README.md"` over `<AC11 of spec 108>` reads `grep -cF "Files touched/{p=1;next}"`. |

The `\|` in AC6's row is the table's escape for a literal `|`; the criterion spells `|`.

**115 S19** reads: "Finding 13 (L3), with finding 3 of the round-6 promotions audit (M3), on 108
AC15 and S17. 108 S17's pointer is spelled: spec 95's S1 text for 90's S1 ends with the sentence
'Its build-order rows are refreshed by TOOL-dWellOiledMachine-93's tree-wide re-render.' 108 AC15's
first clause reads 'When `<S1 of spec 90>` is piped to `grep -c "tree-wide re-render"`, it prints 1',
a phrase only 108 S17 adds: 95 S1's text for 90's S1 carries none. Observed by AC12." **115 §4
Evidence** gains: "A scratch copy of spec 90 whose S1 is 95 S1's text, built 2026-10-27, counts
`tree-wide re-render` 0 times and `TOOL-dWellOiledMachine-93` once in `<S1 of spec 90>`, so a key
on the unit id reads 1 whether or not 108 S17 was applied (finding 3)."

### 110, 113 and 114 (S9, S11, S17)

**110 S2's AC22 text** reads: "**AC22** — When `<AC1 of spec 97>` is piped to
`grep -cF "tr '\n' ' '"` and to `grep -c "grep -c 'tools/memory-tree/door_fixture.py'"`, each prints
1, and `awk '/^## 4\./{p=1;next} /^## 5\./{p=0} p' <spec 97> | tr -s '\n ' ' ' | grep -c "printed 0 on spec 90 as committed at 05ab0d1f8"`
prints 1. Red when: S12's slice or S13's base line is missing from spec 97." **110 §4 Evidence's
third bullet** ends: "108 S10 also names `AC20` in 97 AC1, since 97 AC1 runs 90 AC20's walk, so an
`AC20` count cannot tell S12 apart; `tr '\n' ' '` and the quoted
`grep -c 'tools/memory-tree/door_fixture.py'` occur in 97 AC1 only through S12."

**113 S1** names the clause it rewrites as "AC1's last clause, the whole-file count of the loader
string over `<spec 96>`, which opens with 'and' at the end of one line of spec 103 and carries its
code span on the next". **113 AC1** reads "When `<AC1 of 103>` is piped to `grep -c "awk '/^## 6"`,
it prints 1, and piped to `grep -c "p'\" <spec 96>"` it prints 0. Red when: AC1 still counts the
loader over the whole of spec 96, alone or beside the scoped count." 114 S1 and AC1 read the same
with spec 106 for 103 and spec 97 for 96.

### Evidence

Each finding's evidence is its row of the report's appendix, which its skeptic re-read and confirmed.
Probes re-run for this spec on 2026-10-27, at HEAD 63dbec5e8:

- The walk above printed what §4's Evidence bullet says over eight scratch files and over
  `tools/run-gates/held_halves.py`, whose last commit dc732dba3 predates this base (S5, S7, S15).
- `resolve_shell_argv` is defined at `tools/govkit/govkit.py:1200`; on `Refusal` it returns
  `list(argv)`. `tools/govkit/matrix.py:911` is a caller (S5).
- `test_no_bare_bash_argv` (`tools/run-gates/measure_legs.py:2682`) reads `__file__`, needs
  `n.args`, and asserts `calls >= 3` (S16).
- 97 S1 says "expecting no output" and 97 AC1 "it prints nothing" (S1, S2).
- 95 S1's text for 90's S1 counts `tree-wide re-render` 0 times and `TOOL-dWellOiledMachine-93` once;
  108 S17 counts `refreshed by TOOL-dWellOiledMachine-93's tree-wide re-render` 0 times (S3).
- `<AC1 of 103>` and `<AC1 of 106>` each count `p'" <spec 9N>` once today (S9).
- A scratch markdown file with `### Fixture` after `### Alternatives rejected` and a loader line in
  both §4 and §6 counted the loader 2 times through the open `sed -n` range and once through
  `<Fixture of spec N>` (S12).
- `<AC11 of spec 108>` counts `Files touched/{p=1;next}` 0 times (S13); `abb9N.XXXXXX` and `never
  share a repository` count 0 in specs 101, 104 and 107, `lib-unattended.sh:1149` 0 in spec 98, and
  `test_no_bare_bash_argv` 0 in 108's §10 (S14).
- 97 AC1 at 05ab0d1f8 and at HEAD counts `tr '\n' ' '` 0 times, and spec 110 carries it nowhere (S17).

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-110.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-113.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-114.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-115.md`
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since four rev cells move)

### Alternatives rejected

- **Keep the `resolve_shell_argv` exemption, cite the definition and state the fallback (S5).** It
  passes a spawn 90 S20 forbids, and finding 25's variable idiom then needs a second exemption that
  tracks names to their assignments.
- **Two batches, {113, 114} and {110, 115}.** The write sets are disjoint by spec, but both halves
  move rev cells of the one README render (M6 clause 3).
- **Require each wrapped sentence to sit on one line (S8, S11).** It binds every builder's wrapping;
  flattening the slice binds the criterion only, as `<X of spec N>` already does.
- **Place `### Fixture` first in §4 through 104 S1 and 107 S1 (S12).** It amends two more specs and
  leaves the range open for any later sub-head.

## 5. Production-readiness checklist

- security — N/A — spec text and criteria change.
- perf / scale — N/A — greps and one walk over scratch files.
- error / empty / loading states — a walk consumer still expecting no output reads red (S1, S2); a
  fixture range that reaches §6 can no longer pass on the §6 copy (S12).
- observability — the walk prints each bash-led literal's file and line, resolver forms included.
- risks — S5 makes the walk red on any `resolve_shell_argv` spawn in the two fixtures, which is the
  rule 90 S20 states; a build run that skips M2's cross-read builds units 90 to 97 on uncorrected text
  and AC14 is red at this unit's pass.
- testing — AC1 to AC14.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`,
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`, and `<§K of spec N>` is
`awk '/^## K\./{p=1;next} /^## [0-9]+\./{p=0} p' <spec N> | tr -s '\n ' ' '` for section number K.
`<walk>` is the code span of `<AC20 of spec 90>` that opens `python -c "`, cut at its closing quote
with `grep -o 'python -c "[^"]*"'`. Each command runs from the repository root, and the predicate is
loaded as TOOL-dWellOiledMachine-98 §6 states. Each criterion runs at this unit's pass, after units 90
to 120 have built.

- **AC1** — When `<AC8 of spec 94>`, `<S1 of spec 97>` and `<AC1 of spec 97>` are each piped to
  `grep -cE "prints nothing|expecting no output"`, each prints 0, and to `grep -c "subprocess calls"`
  each prints 1; and `<S11 of spec 115>` piped to `grep -c "expecting exactly the line"` and to
  `grep -c "it prints exactly the line"` each prints 1.
  Red when: a consumer of the walk still expects no output, so it reads red on a clean tree.
- **AC2** — When `<AC15 of spec 108>` is piped to `grep -c 'grep -c "tree-wide re-render"'`, it
  prints 1; `<S1 of spec 90>` piped to `grep -c "tree-wide re-render"` prints 1; and `<§4 of spec 115>`
  piped to `grep -c "a key on the unit id reads 1"` prints 1.
  Red when: AC15 keys on a token 95 S1 already supplies.
- **AC3** — When `<AC7 of spec 115>` is piped to `grep -c "copy of .'tools/runtime/"`, and
  `<AC10 of spec 108>` to `grep -c "'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'"`
  and to `grep -c "copy of .'tools/runtime/"`, each prints 1.
  Red when: a walk criterion still names a file by a bare name the root does not hold.
- **AC4** — When `eval "<walk>" <f>` runs over a scratch file whose only spawn is
  `subprocess.run(resolve_shell_argv(["bash", "x"]))`, and over one holding
  `argv = ["bash", "x.sh"]; subprocess.run(resolve_shell_argv(argv))`, each prints one `<file> <line>`
  line before `subprocess calls 1`, and over one whose only spawn is
  `subprocess.run([resolve_bash(s), s])` it prints only `subprocess calls 1`; and `grep -c "not in ok"`
  prints 0 over `<spec 90>` and over `<spec 115>`, and `grep -c "govkit.py:1200"` over `<spec 115>`
  prints 1 or more.
  fixture: three scratch Python files in the run's scratch directory.
  Red when: a `resolve_shell_argv` spawn, which falls back to a bare `bash`, passes the walk.
- **AC5** — When `<S10 of spec 108>` and `<AC8 of spec 94>` are each piped to
  `grep -cF "cmd = ['bash'"`, `grep -cF "args=['bash'"` and `grep -cF "] + y"`, each prints 1, and
  `<AC7 of spec 115>` piped to `grep -cF "args=['bash'"` prints 1.
  Red when: 94's red arm keeps three staged cases and 115 AC7 still passes.
- **AC6** — When `fold -s -w 60 <spec 108> | awk '/^## 4\./{p=1;next} /^## 5\./{p=0} p' | tr -s '\n ' ' ' | grep -c "0 for each full path and 1 for each bare name"`
  runs, it prints 1; `awk '/^## 6\./{p=1;next} /^- \*\*AC1\*\*/{p=0} p' <spec 115> | tr -s '\n ' ' ' | grep -c "/^## 5.\./{p=0} p' <spec N> | tr -s"`
  prints 1; and `<S2 of spec 110>` piped to `grep -c "<spec 97> | tr -s"` prints 1.
  Red when: a §4 slice is counted line by line, so a wrapped phrase reads 0.
- **AC7** — When `<AC1 of spec 103>` is piped to `grep -c "p'\" <spec 96>"` and `<AC1 of spec 106>`
  to `grep -c "p'\" <spec 97>"`, each prints 0; and `<AC1 of spec 113>` and `<AC1 of spec 114>` are
  each piped to `grep -c "it prints 0"`, each printing 1.
  Red when: the scoped count was appended beside the whole-file count instead of in its place.
- **AC8** — When `<AC3 of spec 115>`, `<AC9 of spec 115>` and `<AC14 of spec 115>` are each piped to
  `grep -c "Fixture of spec"`, each prints 1, and to `grep -c "sed -n '/^### Fixture/,/^### /p'"`,
  each prints 0; and over a scratch markdown file holding `### Fixture` after
  `### Alternatives rejected` and the loader string once in §4 and once in §6,
  `awk '/^### Fixture/{p=1;next} /^### |^## [0-9]+\./{p=0} p'` piped to `grep -c "<loader>"` prints 1.
  fixture: one scratch markdown file in the run's scratch directory.
  Red when: a fixture range runs to the end of the file and counts the §6 copy.
- **AC9** — When `<AC16 of spec 115>` is piped to `grep -cF "Files touched/{p=1;next}"`, it prints 1,
  and to `grep -c 'grep -c "tools/memory-tree/README.md"'` it prints 0; and `<AC11 of spec 108>`
  piped to `grep -cF "Files touched/{p=1;next}"` prints 1.
  Red when: AC16 keeps a clause already green before 115 S24 lands.
- **AC10** — When `grep -c 'abb95.XXXXXX'` runs over `<spec 101>`, `grep -c 'abb96.XXXXXX'` over
  `<spec 104>` and `grep -c 'abb97.XXXXXX'` over `<spec 107>`, each prints 2 or more;
  `grep -c "never share a repository"` over each of the three prints 1; `grep -c "lib-unattended.sh:1149"`
  over `<spec 98>` prints 1; and `awk '/^## 10\./{p=1} p' <spec 108> | grep -c test_no_bare_bash_argv`
  prints 1 or more.
  Red when: 115 S14 or S20 is skipped and every criterion of spec 115 still passes.
- **AC11** — When `<§4 of spec 115>` and `<§4 of spec 108>` are each piped to
  `grep -c "129, 516, 518, 519, 520 and 543"`, each prints 1, and `eval "<walk>" tools/run-gates/held_halves.py`
  prints those six line numbers and `subprocess calls 1`.
  Red when: the Evidence line understates what the walk prints.
- **AC12** — When `<§10 of spec 115>` is piped to `grep -c "leaves unchanged"`, it prints 1, and to
  `grep -c "widened from"` it prints 0; and `<S11 of spec 115>` piped to `grep -c "modelled on"`
  prints 1 and to `grep -c "this walk widens"` prints 0.
  Red when: a reader is told the guard was widened when it was copied with a different bar.
- **AC13** — When `<S2 of spec 110>` is piped to `grep -cF "tr '\n' ' '"`, it prints 1, and to
  `grep -c 'grep -c "AC20"'` it prints 0; `<§4 of spec 110>` piped to `grep -c "108 S10 also names"`
  prints 1; and `<AC22 of spec 108>` piped to `grep -cF "tr '\n' ' '"` prints 1.
  Red when: AC22's first count reads 1 whether or not 108 S12 was applied.
- **AC14** — When
  `for p in "115 90" "110 92" "113 93" "114 92"; do set -- $p; check_amended_before_built $1 121 $2 || echo $1; done`
  runs, it prints nothing.
  Red when: this batch's rev bump of a spec lands after the build commit of the earliest unit that
  spec's corrections reach, and the loop prints that spec.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved at this unit's pass: each criterion is a probe or a grep, and the arms the
amended units declare stay on their own §7 lines.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the round-6 promotions audit's 17 medium and low findings
  batched.

## 10. Reuse audit

Each item extends the seam its finding names: the walk 115 §4 already carries, shortened by its
exemption rather than widened; `resolve_bash` (`tools/lib/resolve_bash.py:15`) as the form 90 S20
prescribes; 115's own `<X of spec N>` flattening, applied to its `<§4 of spec N>` slice and to 110's;
and TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`) for the ordering. No item mints a module or a probe.

Probe: `python tools/codebase-map/reuse_lookup.py "flag a subprocess argv that opens with a bare bash literal"`
ranked `resolve_bash` and `resolve_shell_argv` among name-stem hits and no argv guard; reading
`resolve_shell_argv` at `tools/govkit/govkit.py:1200` found the fallback S5 acts on. The probe
`python tools/codebase-map/reuse_lookup.py "slice one section of a spec and count a token in it"`
returned lexical neighbours only, so no existing seam fits the slices beyond the idiom named above.

Recall terms used: `python tools/memory-recall/query.py "how does a guard that flags a bare bash argv
treat the resolve_shell_argv fallback" --terms "bare bash argv walk resolve_bash resolve_shell_argv
fallback exemption subprocess liveness count staged case"`
