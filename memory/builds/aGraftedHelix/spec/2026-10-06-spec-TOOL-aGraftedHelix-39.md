# TOOL-aGraftedHelix-39 — one derivation of the paths a dispatched pass may write

**Status:** SPECCED · rev-1 · 2026-10-06 · node a · Tier-2 · base 290d0d2d · streams tooling · order 23 · ratified 2026-10-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-prompt-TOOL-aGraftedHelix-39-1-spec-brief.md](../prompts/2026-10-06-prompt-TOOL-aGraftedHelix-39-1-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Unit 38's builder reported that a second `--dispatch` naming only new paths left the pass's earlier
paths outside the set its next commit was graded against. It reproduces (§4). The kit answers "which
paths may this pass write" in four places and in three different ways, and `--check-commit`
disagrees with check 23 in both directions. This unit derives the answer once, in the kit library,
as the rule the verbs contract and check 23 already state: every row a unit parks at one anchor
stands, and the pass may write their union. Every reader asks that one function, and `--dispatch`
prints the set it leaves in force.

## 2. Scope (IN)

- **S1** — `read_pass_declarations`, a new function in `tools/unattended/lib-unattended.sh`. It
  reads a run-state file's dispatch rows and prints one row-shaped line per key, where a key is an
  anchor and a unit: `<utc of the key's first row> dispatch · item <anchor> <unit> · reason <paths>`.
  `<paths>` is every path of every row under that key, in first-appearance order, each once. Keys
  print in the order they first appear. With a second argument `current`, it keeps, for each unit,
  only the key holding that unit's LAST row. It is one awk process, and a file holding no dispatch
  row prints nothing. Observed by AC5 and AC6.
- **S2** — `check_pass_open` in `tools/unattended/unattended.sh` loses its same-anchor supersession
  test, the block under the `THE LAST ROW CARRYING THIS SET` comment that `TOOL-cMendedVintage-10`
  added. A pass is its key and its declared set is the key's union, so no row of a key closes
  another. The commit test below it is unchanged, and the function header states the rule. Observed
  by AC1 and AC3.
- **S3** — `verb_dispatch` builds its sibling set and its condition-1 loop from
  `read_pass_declarations` over every key, asking `check_pass_open` about each key's union. A pass's
  earlier same-anchor paths therefore stay reserved against a sibling until the pass commits inside
  its union, and are released then. The comment above the sibling loop that says the driver and
  `--audit` ask over "two populations" is rewritten to the one population. After the row is parked,
  the verb prints one more line, `unattended: dispatch effective — <anchor> <unit> · <paths>`, read
  from the `current` key of that unit. Observed by AC3 and AC4.
- **S4** — `check_commit_message`, the `--check-commit` verb, reads `read_pass_declarations` with
  `current`. A commit made now belongs to the key holding its unit's last row, which is the window
  check 23 grades it in, so a row at a later anchor is graded alone and an earlier pass's paths do
  not carry into it. A key whose pass commit is HEAD keeps today's amend reading. Both path
  refusals name the pass they graded against, `graded against the pass at <anchor>, which declares:
  <paths>`, right after the paths they list and before the repair, so the printed `--dispatch`
  stays the last thing on the line and still runs as printed. Observed by AC1 and AC2.
- **S5** — `print_audit` reads `read_pass_declarations` with `current` in place of its own awk, and
  `derive_refreshed_at` takes its path list from the library's lines. Neither changes behaviour.
  Observed by AC5 and AC7.
- **S6** — Check 23 in `tools/unattended/check-unattended.sh` takes `dsrows` from
  `read_pass_declarations "$f"` in place of its private awk. Its verdict is unchanged; the paths of
  a key now come in first-appearance order. Observed by AC5 and AC8.
- **S7** — The driver suite gains one block in region two, beside the `--check-commit` arms, built
  on the suite's own `build_specced_tree`. (a) Same anchor: dispatch a.sh and b.sh, dispatch again
  naming only c.sh at the same HEAD, stage all three under `Pass: ARCH-tRun-1`, and `--check-commit`
  exits 0. (b) The second dispatch prints the `dispatch effective` line naming all three. (c) While
  that pass is open, `ARCH-tRun-2` declaring a.sh is refused as a sibling's path; after the pass
  commits a write to c.sh alone, the same declaration is accepted. (d) The brief's four steps at a
  later anchor: dispatch a.sh and b.sh, commit under `Pass: ARCH-tRun-1` touching a.sh, dispatch c.sh,
  stage b.sh, and `--check-commit` exits 1 naming b.sh and the anchor it graded against. (e) The
  one-derivation arm, in the shape of the `baseline_units` arm. `FLOOR_ASSERTIONS` and
  `FLOOR_SHARD_2` rise by exactly the assertions the block adds. Observed by AC1, AC2, AC3, AC4, AC5
  and AC9.
- **S8** — The gate suite's check 23 block of widening-repair arms gains arm F, built as arm A is
  with its sibling row: two same-anchor rows for one unit with DISJOINT paths, a commit writing
  inside both, and check 23 reports no write outside the declared set. The floors of the shard
  holding the block and `FLOOR_ASSERTIONS` rise by exactly its assertions. Observed by AC8 and AC9.
- **S9** — `tools/unattended/SKILL.template.md` corrects its re-declaration sentence, which says
  narrowing is refused. It says instead that a second declaration may name only the paths it adds,
  that every row at one anchor stands and the pass may write their union, which `--dispatch` prints,
  that a narrower row is accepted and frees nothing, and that a row at a later anchor is a new pass.
  The installed Skill is re-rendered. Observed by AC10.
- **S10** — The class record `two-guards-one-question-two-answers` gains this instance under
  "Where it bit" and names this unit's arm under "Its gate", beside the `baseline_units` one.
  Observed by AC10.
- **S11** — The `unattended` kit's version moves once, after the unit's last edit to a shipped file,
  in every carrier `tools/check-kit-versions.sh` pairs, and the installed guides are re-adopted.
  Observed by AC11.

## 3. Non-goals (OUT)

- **No change to the contract text.** `memory/guides/UNATTENDED-VERBS.md` already says a
  declaration is append-only and both rows stand, and the shared brief's invariant 10 keeps the
  verbs, protocol and stops templates out of this unit's reach. The new output line is not a
  contract the entry states, so nothing there turns false.
- **No change to the commit test.** `pass_commit` and the commit test in `check_pass_open` keep
  their bytes; S2 changes only which rows make up a pass. `check_pass_open` still opens its commit
  window up to HEAD, where check 23 bounds it at the unit's next anchor; that is a question about
  openness, not about which paths, and it is named in §4's gaps.
- **No change to what check 23 grades.** It already unions same-anchor rows; S6 moves the
  derivation, not the rule. The `declared before COMMIT, not before WRITE` limit recorded against
  `TOOL-dUnstalledConvoy-23` stands.
- **No new verb, flag, check number, leg or conf key.**
- **No rewrite of any run-state file.** Rows already on record are read under the union.
- **The owed suites are not run here.** The main loop runs them once at VERIFYING.

### Edges

- **consumes-from** external — the readers as they stand at `eee0dbb9`: check 23's union and
  `--audit`'s union from `TOOL-dUnstalledConvoy-23` and the aProbedUnit closing review, the
  supersession test from `TOOL-cMendedVintage-10`, and `--check-commit` with its amend reading from
  `TOOL-aWindowedPass-3` and `TOOL-aWindowedPass-6`. This unit builds none of them.
- **hands-off** external — the re-run of the owed unattended suites, which the main loop makes once
  at VERIFYING.

## 4. Design

### What was reproduced

The probe was a slice of the driver suite: its prologue, lines 1 to 629 of the suite with `HERE`
pinned to the kit dir of this worktree at `eee0dbb9`, and a block of four variants built on its own
`build_specced_tree`, `fixture` and `run`. It ran from the session scratchpad with `TMPDIR` under a
short directory in %TEMP%, in 108 s on node `a`, 2026-10-06. Fixture paths are spelled through the
suite's prefix, so a.sh reads `tools/a.sh` below. Every figure in this table is PINNED to that run.

| Variant | Steps | `--check-commit` | What check 23 grades |
|---|---|---|---|
| V1, same anchor | dispatch a b; dispatch c at the same HEAD; stage a, then a b, then a b c | exit 1 each time, naming whichever of a and b is staged as "outside the set it declared before dispatch" | the key's union, a b c |
| V1, sibling | while that pass is open, `ARCH-tRun-2` declares a | accepted, `dispatch declared` | — |
| V2, same anchor, rows committed by a `Pass: none` records commit (unit 38's shape) | stage a | exit 1, naming a | the union |
| V3, later anchor, the brief's four steps | dispatch a b; records commit; commit a under `Pass:`; dispatch c; stage b | exit 0 | the c row alone: the next commit writes b, and b is outside {c} |
| V4, as V3 with a records commit after the second dispatch | stage b | exit 1, naming b | the c row alone |

The probe can answer either way, which is its liveness: in the same run the verb exited 0 on a
declared path, V3's second step staging a.sh, and 1 on an undeclared one, V4.

Unit 38's own rows have V2's shape. `memory/builds/aGraftedHelix/RUN.md` holds two rows at
`7db5d7a8` for that unit, the full set and then one gotcha file alone, and its rev-2 spec commit,
`333160ad`, carried `Pass: none`. Under V2 its code commit is graded against the gotcha file alone,
which is what the builder reported. The builder then parked a third row at `333160ad` restating the
full set, and `bc3f3ab0` went through against it.

### Why the readers disagree

| Reader | Where | Today | After |
|---|---|---|---|
| check 23 | `tools/unattended/check-unattended.sh`, its `dsrows` awk | union per key, every key | S1, every key |
| `--audit` | `print_audit` | its own awk: union at the unit's newest anchor | S1 with `current` |
| `--dispatch` sibling set and condition 1 | `verb_dispatch` | per ROW, an earlier same-anchor row with a different set closed by `check_pass_open` | S1, every key, the union tested open |
| `--check-commit` | `check_commit_message` | per ROW through `check_pass_open`, plus every row whose pass commit is HEAD, across anchors | S1 with `current` |
| refresh | `derive_refreshed_at` | every row's paths | S1's lines' paths, the same set |
| order gate | `verb_dispatch` | whether ANY row names a unit | unchanged; it asks no set |

The contract is one answer and it is written down three times. The `--dispatch` entry of the verbs
guide says "A DECLARATION IS APPEND-ONLY", that a re-declaration is accepted "wider, NARROWER, or
disjoint", and that "both rows stand"; `TOOL-cMendedVintage-15`, ruled 2026-09-20 and recorded in
`memory/DECISIONS.md`, wrote that text. `TOOL-dUnstalledConvoy-23` S2 and AC2 made check 23 grade the union of same-anchor rows,
and the aProbedUnit closing review made `--audit` do the same.

`TOOL-cMendedVintage-10` landed three days before that ruling. It found that a per-ROW openness test
wedged: a narrowed row's abandoned paths stayed reserved forever, because no commit would ever write
inside them. It fixed that by closing an earlier same-anchor row when a later one carried a
different set. That made a disjoint re-declaration, which ADDS paths, read as one that replaces
them, which is V1. And `--check-commit`, which arrived later in `TOOL-aWindowedPass-3`, inherited
the per-row reading through the same function.

The union keeps `TOOL-cMendedVintage-10`'s fix without its cost. A key's pass closes when its commit
writes inside the union, so a pass that narrowed and then committed releases every path its rows
named. That is its AC1's shape, and S7 (c) asserts it. What changes is the window before the
commit: an open pass that narrowed keeps the abandoned paths reserved until it commits. That is the
conservative direction a disjointness proof wants, and it is what "both rows stand" says.

V3 is a second defect of the same class. `--check-commit` reopens a row whose pass commit is HEAD,
for `git commit --amend`, and unions it with the open row's paths. When the second dispatch is
anchored on that pass commit and the run commits without a records commit in between, a new commit
also sees HEAD as the earlier pass's commit, and the earlier pass's paths leak into the new pass.
Check 23 grades the new commit in the window of the key holding the unit's last row. S4 grades it
there too.

### Data model

One library line per key, the shape of a raw row, so every reader parses it with the expansions it
already uses (`${r#* dispatch · item }`, `${r#* · reason }`):

```
2026-10-06T11:52:28Z dispatch · item 0674d99e ARCH-tRun-1 · reason tools/a.sh tools/b.sh tools/c.sh
```

The utc is the key's FIRST row's, which is what `--audit` prints as `dispatched`. Check 23's private
awk iterated `for (a in add)`, whose order awk leaves unspecified, and kept the first row's
timestamp; nothing it grades reads the order.

### Inventory

| identifier | where | cell |
|---|---|---|
| `read_pass_declarations` | `tools/unattended/lib-unattended.sh` | `sh.function` |
| `unattended: dispatch effective — ` | the stdout of `--dispatch` | an output prefix, no naming cell grades it |

`python tools/lexicon/lexicon.py --suggest read_pass_declarations --as sh.function` answered OK on
2026-10-06; `read` is the verb `read_brief_paths` already uses for the same file. No check number,
leg, conf key or gotcha record is minted, and no map key moves: the map does not scan `.sh`.

The call sites S3 to S6 add, PINNED by the table above: five non-comment calls in
`tools/unattended/unattended.sh` (two in `verb_dispatch`, one each in `check_commit_message`,
`print_audit` and `derive_refreshed_at`) and one in `tools/unattended/check-unattended.sh`. A builder
who routes two readers through one call re-pins the count with a §9 line.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `memory/gotchas/two-guards-one-question-two-answers.md`
- `memory/gotchas/INDEX.md`, only if the generator moves it
- every other version carrier `tools/check-kit-versions.sh` pairs for the `unattended` kit, with
  the guides `tools/unattended/adopt-unattended.sh` re-adopts from them

### Rollout

One pass, in this order, each step verified by its own criteria before the next:

1. S1, then AC6 over its fixture.
2. S2 to S6, the readers.
3. S7 and S8, the arms, each observed red on its staged break.
4. S9 and S10, the Skill and the class record.
5. S11, the version, last.

### Gaps it leaves, stated

- **Declared before commit, never before write.** A pass that wrote outside its lane and then
  re-declared at the same anchor is covered by the union. That is `TOOL-dUnstalledConvoy-23`'s
  recorded limit, and this unit does not move it.
- **An amend of a pass commit that a later row is anchored on** is graded as a new commit of the
  later pass, because the `commit-msg` hook cannot tell an amend from a new commit when HEAD is the
  earlier pass's commit. The reading is the conservative one: it refuses, and its printed
  `--dispatch` widens the later key, which check 23 then skips as an anchor the amend orphaned.
- **The openness window.** `check_pass_open` asks `pass_commit` up to HEAD, while check 23 bounds a
  key's window at the unit's next anchor. An earlier-anchor pass whose own window held no commit
  stays open until a later commit naming the unit writes inside its set. Out of scope (§3).
- **A new private reader under another spelling.** S7 (e) counts calls and definitions; it cannot
  see a reader that parses the rows without the function name, which is the class record's own
  position on a pair-specific arm.

### Alternatives rejected

- **Last-row supersession everywhere** (§8 F2, option b), by the contract and by the aProbedUnit
  finding that a last-row `--audit` graded a finished unit open for hours.
- **Supersession only for a strict subset** (§8 F2, option c), because it contradicts "nothing
  rewrites, supersedes or retracts an earlier one", and a partly overlapping row has no reading.
- **Keep unioning the reopened and the open rows in `--check-commit`** (§8 F3, option b), by V3.
- **Refuse whenever a reopened and an open row coexist** (§8 F3, option c), which refuses the
  ordinary commit after a re-dispatch with no records commit between.
- **Extend the `dispatch declared` line instead of adding one.** That line names the row just
  parked, which is a fact worth keeping; a second line keeps the row and the pass's set apart.

## 5. Production-readiness checklist

- security — No write path and no new surface. The sibling refusal reserves more, never less, while a
  pass is open. `--check-commit` admits exactly the set check 23 grades, which is wider than today
  at one anchor and narrower across anchors.
- perf / scale — One awk over the run-state file per reader call in place of a grep per reader.
  `--check-commit` runs on every commit and now asks `check_pass_open` once per unit rather than
  once per row.
- error / empty / loading states — A run-state file with no dispatch row gives the library empty
  output, and each reader keeps the message it prints today for that case: check 23's announced
  skip, `--audit`'s `no unit is dispatched and open`, and `--check-commit`'s refusal naming no open
  pass.
- observability — The `dispatch effective` line states the set after each `--dispatch`, and both
  path refusals of `--check-commit` name the anchor and the set they graded against.
- risks — `tools/unattended/check-unattended.sh` and `tools/unattended/unattended.sh` lose lines
  above literals the install-prefix waivers key by line, so the builder reads that leg and re-keys
  any moved row. A run in flight with an OPEN pass that narrowed at one anchor now sees its abandoned
  paths reserved against siblings until it commits. This build has no such pass: over its
  `RUN.md` at `eee0dbb9`, every one of its 11 keys has a pass commit writing inside the key's union,
  measured 2026-10-06 with the library's `pass_commit`, so the union reading closes all of them.
  Arm F must add no finding to the arms-groups linter's reading of the gate suite.
- testing — Every new arm is observed red on a staged break, and AC1 to AC4 are observed failing on
  the parent. The owed suites run once at VERIFYING, at the main loop.
- migration — None. No run-state file is rewritten.
- user docs — The Skill sentence (S9). The verbs guide already states the rule.

## 6. Acceptance criteria

A slice is a suite's prologue plus the block a criterion names, run from the session scratchpad under
a name that is not a suite name, with `HERE` pinned to the kit dir under test and `TMPDIR` under a
short directory in %TEMP%. "The parent" is the pass's parent commit, checked out as a worktree under
a short directory in %TEMP%: its slice pins `HERE` to that worktree's kit dir and runs the block
from the pass's commit. Each staged break is made in a scratch copy and undone, which
`git diff --quiet` against the pass's commit confirms. The driver suite and the gate suite are the
two files §7's `New arm:` lines name.

- **AC1** — When a slice of the driver suite runs S7's arm (a) at the pass's commit, `--check-commit`
  exits 0 with a.sh, b.sh and c.sh staged under `Pass: ARCH-tRun-1`. The same slice over the parent
  exits 1 naming a.sh with the text `stages paths outside the set it declared before dispatch`.
  Red when: the graded set is the last same-anchor row's alone, c.sh, which the parent shows and a
  scratch copy of the library printing each key's last row reproduces.
  figure: the parent's exit and text are PINNED from §4's V1 run at `eee0dbb9`.
- **AC2** — When the same slice runs S7's arm (d), `--check-commit` exits 1, names b.sh, and its
  text carries `graded against the pass at` followed by the anchor of the c.sh row. The parent
  exits 0.
  Red when: `check_commit_message` collects every reopened row with the open one, which a scratch
  copy that reads every key rather than `current` shows.
- **AC3** — When the same slice runs S7's arm (c), `--dispatch tRun --pass ARCH-tRun-2` declaring
  a.sh is refused with `a path a sibling pass in the same group already declared` while the first
  pass is open, and accepted with `dispatch declared` after that pass commits a write to c.sh alone.
  Over the parent, the first declaration is accepted.
  Red when: the pass never closes after its commit, the `TOOL-cMendedVintage-10` wedge, which a
  scratch copy whose `verb_dispatch` asks `check_pass_open` per row shows.
- **AC4** — When the same slice runs S7's arm (b), the second `--dispatch` prints
  `unattended: dispatch effective — ` followed by the anchor, `ARCH-tRun-1` and all three paths.
  Over the parent no line carries `dispatch effective`.
  Red when: the line prints the new row's paths alone, which a scratch copy reading the parked row
  instead of the library shows.
- **AC5** — When `grep -c '^read_pass_declarations()' tools/unattended/lib-unattended.sh` runs it
  prints 1, the non-comment calls of `read_pass_declarations` number 5 in
  `tools/unattended/unattended.sh` and 1 in `tools/unattended/check-unattended.sh`, neither file
  defines it, and `grep -c "THE LAST ROW CARRYING THIS SET" tools/unattended/unattended.sh` prints 0.
  S7's arm (e) asserts the same four counts and passes in the slice.
  Red when: a reader keeps a private parse, which a scratch copy of the gate leg holding its old
  `dsrows` awk shows as 0 calls there and arm (e) failing.
  figure: the counts are PINNED by §4's Inventory.
- **AC6** — When `bash -c '. tools/unattended/lib-unattended.sh && read_pass_declarations "$0"'` runs
  over a scratch run-state file holding four dispatch rows, unit u at anchor g1 with paths a and b,
  u at g1 with c and a, unit v at g1 with d, and u at g2 with e, it prints three lines in that order:
  u at g1 with `a b c`, v at g1 with `d`, u at g2 with `e`. With `current` it prints two, v at g1 and
  u at g2. Over a file holding no dispatch row it prints nothing.
  Red when: a repeated path prints twice, or `current` keeps a unit's earlier key.
- **AC7** — When a slice of the driver suite runs its `--audit` block, the one opening
  `SAME-ANCHOR ROWS ARE ONE PASS`, no line opens `FAIL`.
  Red when: `print_audit` reads the last row alone, which a scratch copy of the library printing
  each key's last row shows as a failing `closes the pass` assertion.
- **AC8** — When a slice of the gate suite runs its check 23 widening-repair block, arms A to F, no
  line opens `FAIL`. Arm F fails over a scratch copy of the library whose function prints each key's
  last row only.
  Red when: check 23 grades a disjoint same-anchor re-declaration against its last row.
  cost: each arm runs the whole leg over its fixture, minutes on node `a`.
- **AC9** — When `git diff` from the parent over each suite is filtered for the assertion lines it
  adds, the counts equal the rise of that suite's floors: `hit`, `miss`, `same` and `n=$((n+1))`
  lines in the driver suite, and `hit`, `miss`, `same` and `mutate` lines in the gate suite. The
  pass's `bash tools/unattended/check-arms-groups.sh` reports the same rule A, B and C counts over
  the parent's gate suite, written to the scratchpad by `git show`, as over the pass's own.
  Red when: a floor rises by a number its block does not carry, or arm F adds a linter finding.
- **AC10** — When `grep -c "narrowing is refused" tools/unattended/SKILL.template.md` runs it prints
  0, `bash tools/unattended/adopt-unattended.sh --check` exits 0,
  `python tools/memory-tree/gotchas.py --check` exits 0, and
  `grep -c "TOOL-aGraftedHelix-39" memory/gotchas/two-guards-one-question-two-answers.md` prints at
  least 1.
  Red when: the installed Skill differs from its template, or the class record does not name the
  instance.
- **AC11** — When `python tools/govkit/govkit.py epoch --base <the parent>` runs at the pass's
  commit, its `unattended` line reads `clean` at the bumped version, and
  `bash tools/check-kit-versions.sh` exits 0.
  Red when: the kit's shipped bytes moved and its version did not.
  figure: the version is DERIVED from the parent at observation.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `check-wiring self-test` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `gotchas selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `line length` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · S7 arms (a) to (e), staged as AC1 to AC5 name · FLOOR_ASSERTIONS and FLOOR_SHARD_2, by the assertions added
New arm: tools/unattended/check-unattended.test.sh · check 23 arm F, staged as AC8 names · the floor of the shard holding the block and FLOOR_ASSERTIONS, by the assertions added

Neither suite is on the bar. A pass runs every criterion above directly, through slices, the
library and the checkers, and the main loop runs the owed suites once at VERIFYING.

## 8. Open questions

- **FACT-QUESTION · F1 — Does the report reproduce?** Probe: the slice and four variants of §4.
  Observation: V1 and V2 refuse a path the earlier same-anchor row declared, and V3 admits a path
  check 23 will count. Liveness: the same verb exits 0 on a declared path and 1 on an undeclared one
  in that run, so the probe can answer no.
  RESOLVED (agent, 2026-10-06, delegated): it reproduces, at the same anchor and at a later one, so
  the brief's first branch governs and no refusal message was misread.
- **F2 — What does a second row at the same anchor mean?** (a) Both rows stand and the pass may write
  their union, which is what the verbs contract, check 23 and `--audit` say. (b) The last row
  replaces the rows before it, which is what `check_pass_open` does; every other reader and the
  contract would move to it. (c) A strict subset narrows and anything else adds. Option (b) edits the
  verbs template, which the shared brief's invariant 10 reserves to unit 1, and re-opens the
  aProbedUnit finding that a last-row `--audit` graded a finished unit open. Option (c) contradicts
  "nothing rewrites, supersedes or retracts an earlier one" and has no reading for a row that partly
  overlaps. Option (a) trips no veto and keeps `TOOL-cMendedVintage-10`'s AC1 through the union's
  commit test (§4).
  RESOLVED (agent, 2026-10-06, delegated): (a), the union per anchor and unit, derived once in the
  kit library.
- **F3 — Which declaration does `--check-commit` grade a commit against?** (a) The key holding the
  unit's last row, the window check 23 grades the commit in. (b) Every open row and every row whose
  pass commit is HEAD, today's reading. (c) Refuse whenever a reopened and an open row coexist. V3
  rejects (b): it admits a write check 23 counts. Option (c) refuses the ordinary commit after a
  re-dispatch with no records commit between, with no repair but an extra commit. Option (a) grades
  as check 23 does, and its one wrong case, an amend under a later anchor, refuses (§4 gaps).
  RESOLVED (agent, 2026-10-06, delegated): (a), with `read_pass_declarations` in `current` mode.

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, from the unit 39 spec brief, grounded on the run branch at
  `eee0dbb9`, with the four-variant reproduction run on node `a` and the readers read whole.

## 10. Reuse audit

The map probe was `python tools/codebase-map/reuse_lookup.py "union of a pass's declared write paths
across repeated dispatch rows"`. It ranked name-stem neighbours only, `write` and `write_text` first,
and printed `unscanned layers: .sh`, so its miss says nothing about the shell files this unit edits,
which were read by hand. The seam this unit extends is check 23's `dsrows` awk, which already
computes the union; S1 moves it into `tools/unattended/lib-unattended.sh` beside `read_brief_paths`,
the library's existing reader of the same file shared by the driver and the leg. The class gate
copies the `baseline_units` arm in the driver suite, which the class record names as its precedent.

Recall surfaced the unit 39 brief, `TOOL-dUnstalledConvoy-23`'s spec and its review finding H1 on
"declared before COMMIT, never before WRITE", `TOOL-cMendedVintage-10`'s spec, the aProbedUnit
closing review's finding that a last-row `--audit` graded a finished unit open, and the
aWindowedPass round-2 finding on the amend reading that `TOOL-aWindowedPass-6` built. None of them
records a ruling for last-row supersession after `TOOL-cMendedVintage-15`.

Recall terms used: `python tools/memory-recall/query.py "when a pass re-declares its write set with dispatch, which paths may the pass commit write and do earlier rows stand" --terms "dispatch re-declaration append-only superseded row check_pass_open union same-anchor check 23 check-commit write set narrowing widening"`
