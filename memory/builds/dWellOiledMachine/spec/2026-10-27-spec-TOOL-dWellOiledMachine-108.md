# TOOL-dWellOiledMachine-108 — the round-4 promotions audit's 22 medium and low findings, batched: the arm parse, liveness halves, scoped greps, stale figures and the ask's second row

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 70 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-108-deviation-1081.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-108-deviation-1081.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`)
exited CONVERGED with 22 confirmed findings below HIGH. BUILD-METHOD M4 promotes every one of them,
batched into ONE unit, and this is that unit. It closes, by report id:

- MEDIUM (11): 2, 3, 4, 5, 6, 14, 15, 23, 28, 32, 33.
- LOW (11): 7, 8, 9, 10, 16, 17, 18, 22, 25, 26, 27.

Several findings share a report item (M6: 14, 28; M7: 15, 32; L1: 7, 25; L3: 9, 17), and each keeps
its own scope item here. Finding 22 is taken at its skeptic's low grade, which binds. Each finding
takes the fix its skeptic judged SOUND, or the skeptic's corrected fix where the report marks the
finder's UNSOUND (finding 7). The findings land on specs 95, 96 and 97, so this unit repairs none in
particular and sits after every unit of the build. One unit, not two: findings 4, 10, 16 and 18 amend
spec 95, nine findings amend spec 96 and eleven spec 97, findings 10 and 18 amend both 95 and 97, and
every amendment moves this build's README rev cells, a generated render two halves would both write
(M6 clause 3).

## 2. Scope (IN)

Each item names its finding, its report item and the spec it amends. "Spec N takes a rev bump" means
spec N is amended by S23's route, its §9 line naming this unit and the finding; where the amended
text is itself a rev bump of a further spec, that further spec receives the corrected text when spec
N's own amendment lands at the same M2 cross-read.

- **S1** — Finding 2 (M1), on TOOL-dWellOiledMachine-96 S2 and S3. Spec 96 takes a rev bump whose S2
  returns the token "without a trailing `/`, only when `check_dir_shaped(token.rstrip("/") + "/")`
  holds", and whose S3 carries the same wording into 93 S3. Observed by AC1.
- **S2** — Finding 3 (M2), on 96 S3. Spec 96's S3 also rewrites 93 S3's join site to "`parse_spec_text`'s
  unit entry (`tools/memory-tree/gen_build_index.py:548`)" and 93 S3's Readers line to name
  `parse_spec_text` where it names `collect`. Observed by AC2.
- **S3** — Finding 4 (M3), on TOOL-dWellOiledMachine-95 S1 and S2. Spec 95 takes a rev bump whose S1
  also rewrites 90 AC2 to open "When `python tools/memory-tree/gen_build_index.py --write` re-renders
  the build README" in place of "When the same render runs", and adds to 90's §6 a first line defining
  `<BASE>` as the build run's pinned `base:` fact in `memory/builds/dWellOiledMachine/RUN.md`; and
  whose S2 also deletes 93 §4 Evidence's clause "the reading 90 AC1 moves to `no`". Observed by AC3.
  **Readers:** by name: `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-93.md`, the one spec spelling the deleted clause. by value: NO VALUE READERS — spec prose no program reads.
- **S4** — Finding 5 (M4), on TOOL-dWellOiledMachine-97 S2 and AC1. Spec 97 takes a rev bump whose
  AC1 counts the tree-wide glob only over spec 94's S14 and AC8 bullets,
  `awk '/^- \*\*(S14|AC8)\*\*/{p=1;print;next} /^- \*\*/{p=0} /^#/{p=0} p' <spec 94> | grep -c "tools/\*\*/\*.py"`,
  so S2's evidence line may record the probe with its literal glob. Observed by AC4.
- **S5** — Finding 6 (M5), on 96 S3. Spec 96's S3 has 93's AC7 fixture list
  `tools/memory-tree/gen_build_index.py` under Files touched in the arm-carrying spec as well, as 96
  AC2 already does, so one fixture is described one way. Observed by AC5.
- **S6** — Finding 14 (M6), on 96 S2 and AC1. Spec 96's S2 skips one leading interpreter token,
  `python`, `python3`, `bash`, `sh` or `node`, before taking the first token, and its AC1 gains the
  line `New arm: python3 tools/memory-tree/gen_build_index.py --selftest · s · none`, which prints
  `tools/memory-tree/gen_build_index.py`. Observed by AC6.
- **S7** — Finding 28 (M6), on 96 §3, §4 and AC3. Spec 96's §4 table replaces the row "a one-segment
  name such as `row_grammar.py --selftest` | 31 | `None`" with three rows: that row at 19, "an
  interpreter word, then a path | 7 | the path", and "a prose phrase naming a path later | 5 |
  `None`", MEASURED 2026-10-27; its §3 third non-goal names the 19 bare filenames and the 5 prose
  lines as a measured residual; and its AC3 also requires that no line whose first field, backticks
  removed, opens with an interpreter word and then a two-segment path yields `None`. Observed by AC7.
- **S8** — Finding 15 (M7), on 97 AC1. Spec 97's AC1 requires, before its bare-bash check,
  `git ls-files --error-unmatch tools/runtime/supervise.py tools/memory-tree/door_fixture.py` to
  exit 0, so the check cannot pass over files that do not exist. Observed by AC8.
- **S9** — Finding 32 (M7), on 97 S1. Spec 97's S1 gives the rewritten 94 AC8 and 90 AC20 the same
  liveness half. Observed by AC9.
- **S10** — Finding 33 (M9), on 97 S1 and AC1. The class is any spawn whose argv's first element is
  the literal `bash`. Spec 97's S1 has 90 AC20 check it with the walk
  `python -c "import ast,sys;[print(f,n.lineno) for f in sys.argv[1:] for n in ast.walk(ast.parse(open(f,encoding='utf-8').read())) if isinstance(n,ast.Call) and n.args and isinstance(n.args[0],(ast.List,ast.Tuple)) and n.args[0].elts and isinstance(n.args[0].elts[0],ast.Constant) and n.args[0].elts[0].value=='bash']"`
  over the two files, its code span on one line, expecting no output, in place of the line regex;
  94 AC8 runs 90 AC20's walk and
  stages its red arm with three cases in a scratch copy of `supervise.py`: `['bash', 'x']`, a list
  whose `"bash",` sits on the next line, and a tuple `("bash", "x")`; and 97 AC1 runs 90 AC20's walk.
  The walk is spelled in 90 AC20 alone. Observed by AC10.
- **S11** — Finding 23 (M8), on 96 S3. Spec 96's S3 has unit 93 state the first-field rule where the
  build order is derived: `derive_arm_suite_path`'s docstring and the `--new-spec` paragraph of
  `tools/memory-tree/README.md` say that the first path-shaped token of two or more segments in a
  `New arm:` line's first field, after one interpreter word, joins the build-order write set, and that
  a bare filename joins nothing; 93's Files touched gains `tools/memory-tree/README.md` and its §7 leg
  line gains `kit/dogfood doc parity`. The two spec templates are not edited (§8 F1). Observed by AC11.
- **S12** — Finding 7 (L1, the skeptic's corrected fix), on 97 AC1's third clause. Spec 97's AC1
  replaces `grep -c "door_fixture.py"` over spec 90 with a flattened slice of 90's AC20,
  `awk '/^- \*\*AC20\*\*/{p=1} /^- \*\*AC21/{p=0} p' <spec 90> | tr '\n' ' '`, piped to
  `grep -c 'tools/runtime/supervise.py'` and to `grep -c 'tools/memory-tree/door_fixture.py'`, each
  printing 1. Observed by AC12.
- **S13** — Finding 25 (L1), on 97 AC1 and §4. The same slice piped to `grep -c 'tools/\*\*'` prints
  0, and 97's §4 Evidence records that the slice's `tools/memory-tree/door_fixture.py` count printed 0
  at base, so the clause tells a skipped rewrite from a made one. Observed by AC12.
- **S14** — Finding 8 (L2), on 97 AC8. Spec 97's AC8 greps each of the seven leg names S16 lists over
  spec 94, each printing 1 or more. Observed by AC13.
- **S15** — Finding 9 (L3), on 96 §1. Spec 96's Goal states 244 annotated lines and cites §4's table
  for the figure. Observed by AC14.
- **S16** — Finding 17 (L3), on 96 §4 Alternatives rejected. Its first alternative states 244.
  Observed by AC14.
- **S17** — Finding 10 (L4), on 95 S1 and 97 §3 and S19. Spec 95's S1 text for 90's S1 also points at
  TOOL-dWellOiledMachine-93's tree-wide re-render; spec 97's S19 deletes 94 S26's S1 clause and keeps
  its Files touched pointer; 97's consumes-from line to TOOL-dWellOiledMachine-94 gains S26, and 94's
  hands-off line to TOOL-dWellOiledMachine-97 gains S26 in the same rev bump of spec 94, so the edge
  keeps both ends. Observed by AC15.
- **S18** — Finding 16 (L5), on 95 AC3. Spec 95's AC3 counts
  `grep -cE "design_lib.py|gen_build_index.py"`, printing 0. Observed by AC16.
- **S19** — Finding 18 (L6), on 95 §4 and 97 §4. Each citation of an OPEN spec the report names is
  rewritten by bullet label: in 97, 90's AC14 and AC23 bullets for "lines 85, 401, 402, 407 and 425",
  and 91's hands-off line to TOOL-dWellOiledMachine-94 for `spec-91.md:70`; in 95, 90's Files touched
  sub-head for `:316` and 90's AC1 bullet for `:367-369`. Observed by AC17.
- **S20** — Finding 22 (L7, the skeptic's grade), on 96 S3. Spec 96's S3 also rewrites 93 S4's
  dispatch sentence to name the parse: "the first whitespace-delimited token of each `New arm:` line's
  first field, after one interpreter word, one trailing comma stripped, when it is a path of two or
  more segments (`design_lib.derive_arm_suite_path`)", and extends 93 AC5 to require
  `grep -c "derive_arm_suite_path" tools/workflows/unattended-unit.js` to print 1 or more. Observed by
  AC18.
- **S21** — Finding 26 (L8), on 97 S20 and AC12. Spec 97's S20 has the pass grep `## Dispositions`
  for `SEV · TOOL-dPlacedRequest-<id> ·` before appending, and append only when it is absent; its AC12
  also counts that row as exactly 1. Observed by AC19.
- **S22** — Finding 27 (L9), on 97 S15. Spec 97's S15 rev bump of spec 93 drops S2's binding of
  `GATES_HEAD` into the checker, since `extract_gates`, its only reader, moves to `design_lib`; the
  comment at `tools/check-spec-tokens.py:363` is reworded to name `design_lib.read_spec_gates`.
  Observed by AC20.
  **Readers:** by name: `tools/check-spec-tokens.py`, which spells `GATES_HEAD` at its binding and its comment. by value: `tools/memory-tree/design_lib.py`, whose `read_spec_gates` reads the pattern once `extract_gates` moves there.
- **S23** — The route. Every rev bump above is made by the build run's main loop at BUILD-METHOD M2's
  cross-read, before its first code pass, in a spec pass whose commit touches specs 95, 96 and 97 and
  whose subject names this unit and none of TOOL-dWellOiledMachine-90 to -94, before the amendments
  those three specs make are applied, by the route TOOL-dWellOiledMachine-95 §8 F1 takes. At this
  unit's own pass, at order 70, nothing is written: the pass runs AC1 to AC21 and records them.
  Observed by AC21.

## 3. Non-goals (OUT)

- The HIGH item H1 and its ten findings: TOOL-dWellOiledMachine-98 to -107, one unit each.
- The report's left-shift gates and checklist entries: each finding here is closed by its own
  criterion, and a lint over specs or a checklist row is a separate mechanism (M2).
- No edit to `memory/TEMPLATE-SPEC.md` or `tools/memory-tree/SPEC-TEMPLATE.template.md` (§8 F1).
- No code written at this unit's pass: the code the amended specs describe is built by their units.
- The 5 prose arm lines S7 records stay outside the write set: their path is a fixture, a manifest or
  a directory as often as the suite.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-95` — S1's text for spec 90, S2, AC3 and §4 Evidence (S3, S17 to S19)
- **consumes-from** `TOOL-dWellOiledMachine-96` — §1, S2, S3, §3, §4, AC1 and AC3 (S1, S2, S5 to S7, S11, S15, S16, S20)
- **consumes-from** `TOOL-dWellOiledMachine-97` — S1, S2, S15, S19, S20, §3 Edges, §4 Evidence, AC1, AC8 and AC12 (S4, S8 to S10, S12 to S14, S17, S19, S21, S22)
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC21 calls
- **hands-off** `TOOL-dWellOiledMachine-109` — AC12, rewritten to grep the two full paths over 90's AC20 slice (round-5 promotions audit, finding 27)
- **hands-off** `TOOL-dWellOiledMachine-110` — S12, S13 and §6, which gain the joins, the exact §4 line and AC22 reading spec 97 (round-5 promotions audit, finding 4)
- **hands-off** `TOOL-dWellOiledMachine-111` — AC21, whose spec-97 clause becomes one predicate call per unit from 90 to 94 (round-5 promotions audit, finding 5)
- **hands-off** `TOOL-dWellOiledMachine-112` — S23, §4, §5's testing line and §6, which gain the fixture and AC23 that observe AC21's loop red (round-5 promotions audit, finding 29)
- **hands-off** `TOOL-dWellOiledMachine-115` — S10, S11, S21, §4, AC8, AC10, AC11, AC15 and AC19, amended before this unit's own amendments land (round-5 promotions audit, findings 3, 7, 10, 11, 12, 13, 15, 16, 23, 25, 30 and 32)

## 4. Design

### Evidence

Each finding's evidence is its row of the report's appendix, which its skeptic re-read and confirmed;
the items cite the clause they correct. Probes re-run for this spec at base `0689e7fa`, 2026-10-27:

- `derive_dir_segments` returns `[]` for a token without a trailing `/`
  (`tools/memory-tree/design_lib.py:567-585`), so a file path passes `check_dir_shaped` only with one
  appended (S1).
- `def parse_spec_text` is at `tools/memory-tree/gen_build_index.py:494`, `"writes"` is set at `:548`
  inside it, and `def collect(` is at `:1106` (S2).
- Spec 96's S2 parse, implemented over the 2496 lines of
  `git grep -h "^New arm:" -- 'memory/builds/*/spec/*.md'` with `check_dir_shaped`, returns `None`
  for 57 lines: 31 one-segment, 9 `none` and 17 with no separator, as 96's table says. Of the 31, 12
  carry a path-shaped token; with one interpreter word skipped, 7 of them yield the path and 5 stay
  `None`, each a prose phrase such as "a `namespace ban` leg over `tools/process-monitor/`" (S6, S7).
- `git grep -cE` of the bare-bash regex over `tools/**/*.py` hits 99 lines in 8 files, and neither
  `supervise.py` nor `door_fixture.py` is tracked at base (S8 to S10, S13).
- The walk in S10, run over a scratch file, prints the one-line list, the list split across lines and
  the tuple, and not `["bash.exe", "x"]`, a candidate tuple in a `for` header, or a list opening with
  a name (S10).
- `memory/TEMPLATE-SPEC.md:283-288` and its kit copy at the same lines say the `covers` field is the
  one part of an arm line a checker reads; the build README's `may: PLAY-dClosedLoop-3` grants only
  the carrier changes the build's own chain clauses name, and dWellOiledMachine's row names no spec
  template (S11).
- The flattened AC20 slice of spec 90, piped to `grep -c 'tools/memory-tree/door_fixture.py'`,
  prints 0 at base, and `grep -c door_fixture.py` over the whole spec prints 14 (S12, S13).
- 97 S16 lists seven legs and 97 AC8 greps three (S14).
- 96's table rows read 141, 75 and 28, which sum to 244, against 274 at 96's lines 20 and 124 (S15,
  S16).
- 94 S26 rev-bumps 90's S1 and Files touched, 95 S1 sets 90's S1, and 97's consumes-from line to 94
  omits S26 (S17).
- `GATES_HEAD` is defined at `tools/check-spec-tokens.py:343`, named in the comment at `:363`, and
  read only inside `extract_gates` at `:531` (S22).

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-96.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-97.md`
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since three rev cells move)

### Alternatives rejected

- **Two batches.** Spec 95 and spec 97 each take items from finding 10 and finding 18, so any split by
  spec shares an item, and every split shares the README render (§1).
- **The first path-shaped token of the first field, whatever precedes it (S6).** On the 5 prose lines
  it returns `tools/gate-legs.json`, a fixture's home or a directory rather than the suite.
- **The rev bumps at this unit's own pass.** It is order 70, after every unit it corrects has built.

## 5. Production-readiness checklist

- security — N/A — spec text and criteria change.
- perf / scale — N/A — no runtime path.
- error / empty / loading states — S8 and S9 make an absent file a red rather than an empty pass.
- observability — S7's table names what the parse leaves out.
- risks — a build run that skips M2's cross-read builds units 90 to 97 on the uncorrected text; AC21
  is red at this unit's pass in that case.
- testing — AC1 to AC21.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, and
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`. Each `python -c` call runs from
`tools/memory-tree/` and imports `design_lib`; every other command runs from the repository root, and
the predicate is loaded as TOOL-dWellOiledMachine-98 §6 states. Each criterion runs at this unit's
pass, after units 90 to 97 have built.

- **AC1** — When `grep -c 'check_dir_shaped(token.rstrip("/") + "/")'` runs over `<spec 96>`, it
  prints 2 or more, and `python -c` printing `derive_arm_suite_path` over
  `New arm: tools/memory-tree/design_lib.py · covers AC1 · s · none` prints the path with no slash.
  Red when: a file path is tested as-is and every arm returns `None`.
- **AC2** — When `<S3 of spec 93>` is piped to `grep -c "parse_spec_text"`, it prints 1 or more, and
  piped to `grep -c "collect"` it prints 0.
  Red when: the join site is named two ways.
- **AC3** — When `<AC2 of spec 90>` is piped to `grep -c "gen_build_index.py --write"` it prints 1 and
  to `grep -c "the same render"` it prints 0; `awk '/^## 6\./{p=1;next} /^- \*\*AC1\*\*/{p=0} p' <spec 90> | grep -c "<BASE>"`
  prints 1; and `grep -c "90 AC1 moves to"` over `<spec 93>` prints 0.
  Red when: 90 AC2 has no command, `<BASE>` is undefined, or 93's stale Evidence clause stays.
- **AC4** — When `awk '/^- \*\*(S14|AC8)\*\*/{p=1;print;next} /^- \*\*/{p=0} /^#/{p=0} p' <spec 94> | grep -c "tools/\*\*/\*.py"`
  runs, it prints 0, and `<AC1 of spec 97>` piped to `grep -c "S14|AC8"` prints 1.
  Red when: the glob count reads the whole spec, evidence included.
- **AC5** — When `<AC7 of spec 93>` is piped to `grep -c "gen_build_index.py"` and to
  `grep -c "(its selftest)"`, each prints 1 or more.
  Red when: the arm-carrying fixture spec names no Files touched and the render reads `unknown`.
- **AC6** — When `python -c` prints `derive_arm_suite_path` over
  `New arm: python3 tools/memory-tree/gen_build_index.py --selftest · s · none`, it prints
  `tools/memory-tree/gen_build_index.py`, and `grep -c "python3 tools/memory-tree/gen_build_index.py --selftest"`
  over `<spec 96>` prints 1 or more.
  Red when: an interpreter word is taken as the suite and the line yields `None`.
- **AC7** — When `python -c` runs `derive_arm_suite_path` over every line
  `git grep -h "^New arm:" -- 'memory/builds/*/spec/*.md'` prints, it prints 0 for the lines yielding
  `None` whose first field, backticks removed, opens with `python`, `python3`, `bash`, `sh` or `node`
  and then a token of two or more segments; and `grep -c "an interpreter word, then a path"` over
  `<spec 96>` prints 1.
  figure: 0 is the bound; the line set is DERIVED from the tree at observation time.
  Red when: an interpreter-led suite path is dropped, or the table still files it as a bare name.
- **AC8** — When `git ls-files --error-unmatch supervise.py door_fixture.py`
  runs, it exits 0, and `<AC1 of spec 97>` piped to `grep -c "error-unmatch"` prints 1.
  Red when: either file is absent and the bare-bash check passes over nothing.
- **AC9** — When `<AC8 of spec 94>` and `<AC20 of spec 90>` are each piped to `grep -c "error-unmatch"`,
  each prints 1.
  Red when: the rewritten criteria carry no liveness half.
- **AC10** — When 90 AC20's walk runs over the two files it prints nothing, and over a scratch copy
  of `supervise.py` holding the three staged cases of S10 it prints three lines; and
  `grep -c "isinstance(n.args\[0\],(ast.List,ast.Tuple))"` prints 1 over `<spec 90>` and 0 over
  `<spec 94>`, and the same pattern counts 0 in `<AC1 of spec 97>`.
  Red when: a multi-line or tuple argv passes, or the walk is spelled in two specs.
- **AC11** — When `grep -c "joins the build-order write set" tools/memory-tree/README.md` runs, it
  prints 1, and `python -c` printing `design_lib.derive_arm_suite_path.__doc__` prints text naming
  `bare filename`.
  Red when: the rule is stated nowhere an author or adopter of the kit reads.
- **AC12** — When `awk '/^- \*\*AC20\*\*/{p=1} /^- \*\*AC21/{p=0} p' <spec 90> | tr '\n' ' '` is piped
  to `grep -c 'supervise.py'` and to `grep -c 'door_fixture.py'`, each
  prints 1, and piped to `grep -c 'tools/\*\*'` it prints 0.
  Red when: 90's AC20 rewrite was skipped and the bare name still satisfies the clause.
- **AC13** — When `grep -c` runs over `<spec 94>` for each of `shell hygiene (a fork spent on builtin work)`,
  `shell hygiene (a loop fed by a command substitution)`, `shell hygiene (a location probe asked from a moved directory)`,
  `shell hygiene (a fixed-name temp renamed into place)`, `spawn budget (forks per hot entrypoint)`,
  `unattended skill size` and `template size <=48KiB`, each prints 1 or more, and `<AC8 of spec 97>`
  names all seven.
  Red when: a leg S16 adds is dropped from 94's leg line and AC8 still passes.
- **AC14** — When `grep -c "274"` runs over `<spec 96>`, it prints 0, and `grep -c "244"` prints 2 or
  more.
  Red when: the annotated-line figure is stated two ways.
- **AC15** — When `<S1 of spec 90>` is piped to `grep -c "re-render"`, it prints 1 or more;
  `<S26 of spec 94>` piped to `grep -c "S1 and Files touched"` prints 0; and the consumes-from line of
  `<spec 97>` naming TOOL-dWellOiledMachine-94 and the hands-off line of `<spec 94>` naming
  TOOL-dWellOiledMachine-97 each name `S26`.
  Red when: two units write 90's S1, or an edge omits S26.
- **AC16** — When `<AC3 of spec 95>` is piped to `grep -c "design_lib.py|gen_build_index.py"`, it
  prints 1, and `awk '/^### Files touched/{p=1;next} /^#/{p=0} p' <spec 90> | grep -cE "design_lib.py|gen_build_index.py"`
  prints 0.
  Red when: `gen_build_index.py` stays in 90's Files touched and AC3 passes.
- **AC17** — When `grep -c "spec-91.md:70"` and `grep -c "85, 401, 402, 407 and 425"` run over
  `<spec 97>`, and `grep -cE ":316|:367-369"` over `<spec 95>`, each prints 0.
  Red when: a line-number citation of an OPEN spec stays one line off.
- **AC18** — When `grep -c "derive_arm_suite_path" tools/workflows/unattended-unit.js` runs, it prints
  1 or more, and `<AC5 of spec 93>` piped to `grep -c "derive_arm_suite_path"` prints 1.
  Red when: the dispatch sentence and the render read one arm line by two rules.
- **AC19** — When `grep -c "· HIGH · a second write_node_lock" memory/builds/dPlacedRequest/BACKLOG.md`
  runs, it prints exactly 1, and `<S20 of spec 97>` piped to `grep -c "## Dispositions"` prints 1.
  Red when: a re-run of unit 92's pass appends a second disposition row.
- **AC20** — When `grep -c "GATES_HEAD" tools/check-spec-tokens.py` runs, it prints 0.
  Red when: the checker keeps a binding nothing reads.
- **AC21** — When `check_amended_before_built 95 108 90`, `check_amended_before_built 96 108 93` and
  `check_amended_before_built 97 108 94` run, each exits 0.
  Red when: a rev bump of this batch lands after the build commit of a unit whose spec it corrects.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved at this unit's pass: each criterion is a probe or a grep, and the arms the
amended units declare stay on their own §7 lines.

## 8. Open questions

- **F1 — Where is the first-field rule stated for authors (finding 23)?** (a) in
  `memory/TEMPLATE-SPEC.md` and its kit copy, the report's fix; (b) in `derive_arm_suite_path`'s
  docstring and the kit README's `--new-spec` paragraph, which are not carriers; (c) nowhere. (a)
  changes a governance carrier (BUILD-METHOD M11 lists the spec template), which M3 veto 2 reserves to
  the owner, and the `may:` grant `PLAY-dClosedLoop-3` covers only carriers this build's chain clauses
  name, and they name no spec template. (c) leaves the finding open. (b) survives and states the rule
  where the build order is derived and where an adopter of the kit reads about specs. RESOLVED (agent,
  2026-10-27, delegated): (b); (a) is recorded at the M2 cross-read that lands S11, as a surfaced
  park entry in the run-state file naming the two template paragraphs, so the wrap-up offers it to
  the owner. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the round-4 promotions audit's 22 medium and low findings
  batched.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-5
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-109, TOOL-dWellOiledMachine-110, TOOL-dWellOiledMachine-111, TOOL-dWellOiledMachine-112, TOOL-dWellOiledMachine-115.

## 10. Reuse audit

Each item extends the seam its finding names: `check_dir_shaped` and `derive_arm_suite_path` (S1, S6,
S7, S11, S20), `parse_spec_text` (S2), 90's own criteria and 94's leg line (S3, S8 to S10, S12 to
S14), the builds-mode ask row and its key (S21), `design_lib`'s spec readers (S22), and
TOOL-dWellOiledMachine-98's predicate (S23). The probe `python tools/codebase-map/reuse_lookup.py "take
the suite path from a New arm line after an interpreter word"` ranked `arm`, `armed` and `run_arms`
by name stem, none an arm-line parser, so the seams are the per-item ones above; the recall query
below ranked TOOL-dWellOiledMachine-90, -79, -94 and -97 first, the earlier batches whose shape this
unit follows. No item mints a module.

Recall terms used: `python tools/memory-recall/query.py "how are a spec audit's medium and low
findings batched into one promoted unit" --terms "minors batch spec audit medium low promoted findings
arm suite path interpreter liveness pathspec"`
