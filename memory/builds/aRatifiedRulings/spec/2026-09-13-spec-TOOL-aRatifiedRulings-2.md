# TOOL-aRatifiedRulings-2 — check 23 stops reporting the brief `--brief` staged, by the path its row names

**Status:** SPECCED · rev-2 · 2026-09-13 · node a · Tier-2 · base 9fac2b53 · streams tooling · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md](../reviews/2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md) | spec-audit | TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-3 TOOL-aRatifiedRulings-4 |

<!-- /gen:spec-records -->

## 1. Goal

Build the ruling `TOOL-aLeakedHandle-7` in `memory/DECISIONS.md`: check 23 of
`tools/unattended/check-unattended.sh` excludes, from the undeclared-write population of a dispatched
pass, the path that a `brief · item <unit>` row names for that unit. The ruling is the authority and
is not restated here; the park that motivated it is the 2026-09-10T10:52:00Z decision row in
`memory/builds/aLeakedHandle/RUN.md`. The class keeps firing for every other undeclared write, and
that is proven by a control in the same fixture, not asserted.

## 2. Scope (IN)

- **S1** — The subset test in check 23 drops a committed path when the unit's own brief rows name
  it. The row set is read from the run-state file AS OF THE PASS COMMIT, through the same
  `GIT show "<rev>:<path>"` read the leg already makes of that file, so a row appended after the
  commit excludes nothing. Observed by AC1, AC2 and AC3.
- **S2** — The exclusion is keyed on the PATH the row names, compared as one normalised spelling
  through the library's `normpath`, never on the directory that path sits in. A hand-written row
  naming `prompts/` excludes nothing under it. Observed by AC4 and AC5.
- **S3** — The exclusion announces itself on the report channel, one `report` line per excluded
  path, so the default run stays byte-stable and a reader asking why a brief did not fire gets an
  answer under `GOV_UNATTENDED_REPORT=1`. Observed by AC1.
- **S4** — `tools/unattended/check-unattended.test.sh` gains one arm of five fixtures in region two,
  beside the existing check-23 arms, with its failing case observed RED against the unfixed checker
  before the fix lands. `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the assertions the arm
  executes. Observed by AC6.
- **S5** — The leg run over this repository names no brief path in any check-23 line whose pass
  commit's tree carries the unit's brief row, still names it in any line whose pass commit's tree
  does not, and every line that named another undeclared path beside the brief still prints,
  minus the brief. The corpus holds one line of the second kind, and it is S1's boundary on live
  data rather than an exception to it. Observed by AC7.

## 3. Non-goals (OUT)

- **Nothing else leaves the population.** The derivation AC7 records shows 24 of today's 29
  brief-naming lines also name other paths: shared records and generated indexes such as
  `memory/LIVE.md`, `memory/ledger/2026-09.md` and `memory/backlog/TOOL.md`, which `--dispatch`
  refuses to declare because they are `SHARED_RECORDS` or `GENERATED_INDEXES`, and acceptance
  ledgers, README rows and product files the pass simply never declared. Those lines keep firing
  after this unit, minus the brief. The shared-record class is the one `TOOL-aLeakedHandle-3`'s
  park describes and it needs its own ruling; this unit does not widen into it, and the build
  README's "thirty corpus lines clear" sentence is corrected at close from the leg's own count
  rather than from this paragraph.
- **The hash in the brief row is not read here.** Whether the committed blob matches the row's
  hash is the `brief-recorded` leg's join, made at the build commit. Reading it twice is two
  answers to one question.
- **No change to `--brief`, `--dispatch`, `pass_commit`, `covers` or the row grammar.** The
  writer stays as it is; only the reader's exclusion set changes.
- **No new shell function in either file.** The lexicon leg parses `.sh` and grades `*.test.sh`
  helpers too, and `VERB_OFFENDER_PIN` in `.lexicon.conf` is shrink-only, so a `brow()` beside
  `drow()` would red the bar. The fixture rows are written inline.
- **No kit version bump inside this unit.** `TOOL-aRatifiedRulings-1` also edits this kit —
  `tools/unattended/unattended.sh` at check 37's branch 10 and
  `tools/unattended/unattended.test.sh`, never `check-unattended.sh`, which holds no check 37 —
  and two units bumping
  `KIT_UNATTENDED_VERSION` independently is a conflict or a double bump on every carrier. Section 8
  carries it.
- **No sequencing with unit 1 is owed.** The two write sets are disjoint: this unit writes
  `tools/unattended/check-unattended.sh` and `tools/unattended/check-unattended.test.sh`; unit 1
  writes `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`, the BUILD-METHOD
  template and render, and `memory/guides/SESSION-KICKOFF.md`. The only line both could touch is
  the carrier `check-unattended.sh:40`, and only under an in-pass bump, which section 8 F1 forbids.
  `--dispatch` condition 1 at `unattended.sh:4853` refuses a pair on overlap alone, so it will NOT
  refuse this one, and the build README declares no order; the roster may run the two in either
  order or concurrently.

### Edges

- **consumes-from** external — `verb_brief` in `tools/unattended/unattended.sh` refuses an
  untracked path and stages only the run-state file, so the brief arrives in the index before the
  pass begins and lands in the pass commit. If that verb ever started staging the brief itself,
  nothing here changes; if it stopped requiring the file tracked, a brief could be named and never
  committed, and the exclusion would then name a path no commit carries, which is harmless.
- **hands-off** external — the `KIT_UNATTENDED_VERSION` bump across every carrier
  `tools/check-kit-versions.sh` pairs, once for the kit, as section 8 F1 recommends.

## 4. Design

### The join today

Check 23 sits at `check-unattended.sh:2222` to `:2361` at base `9fac2b53`. It skips a `LANDED` or
`ABORTED` run at `:2243`, unions dispatch rows per `(anchor, unit)` at `:2249`, resolves the pass
commit through `pass_commit` at `:2301` — the first commit after the anchor whose subject names the
unit and which touches something other than the run-state file — and runs the subset test at
`:2346` to `:2357`. That loop takes `git diff-tree --name-only` of the pass commit, drops the
run-state file by `grep -v -x -F "$f"` at `:2347`, and reports every remaining path no declared path
`covers`. The brief file is never declared, because the pass never wrote it: `verb_brief` at
`unattended.sh:4261` requires the path already tracked at `:4280`, hashes it, parks the row at
`:4306` and stages only the run-state file at `:4307`. The orchestrator therefore has the brief in
the index before dispatch, and the pass's one commit carries it. `c0964657` on the parent build is
the measured instance: its tree lists the brief beside the run-state file and the declared paths.

### The row

`park()` at `unattended.sh:3911` writes `<ISO-Z> brief · item <unit> · reason <hash12> <path>`,
reason line-final. Two readers already depend on that shape and this unit becomes the third. The
parse is the sibling leg's, verbatim: `check-brief-recorded.sh:263` to `:265` take
`${row#* · reason }`, then the hash as `${rest%% *}` and the path as `${rest#* }`. This unit needs
only the path and spells the same three expansions, so a grammar change breaks both readers the
same way and the sibling's DEAD PROBE guard at `check-brief-recorded.sh:144` is the canary for both.

The row is selected by the whole field ` brief · item <unit> · reason `, both separators included,
which is what makes the unit id a whole token: `TOOL-x-1` is a prefix of `TOOL-x-10`, and the
existing check-23 arm F in the suite exists because an unanchored match once refused a correct run.

### The exclusion

Inside the per-row loop, after `pass_commit` has answered and before the subset test:

1. Read the run-state file at the pass commit: `GIT show "$dshit:$f"`, into a variable. The leg
   already reads that file at a revision the same way at `check-unattended.sh:1467`, and the
   run-state path has no leading dot segment, so the `rev:dotpath` mangling the sibling avoids with
   `ls-tree` does not reach it. An adopter whose `MEMORY_ROOT` starts with a dot inherits the
   sibling's exposure, stated here rather than solved.
2. Walk that text with `while read` fed by a heredoc holding the VARIABLE, never a command
   substitution — the `shell hygiene (a loop fed by a command substitution)` leg refuses the other
   form and `memory/project/substitution-fed-loops.txt` is shrink-only. Keep every line carrying
   ` brief · item $dsunit · reason `, take the path with the three expansions above, and append
   `normpath` of it to a newline-delimited set.
3. In the subset loop at `:2347`, before the declared-path walk, drop a committed path that is a
   member of that set by exact string match. The `diff-tree` spelling is git's canonical one, so
   only the row's side is normalised; `covers` is deliberately not used, because it is a
   containment test and a row naming a directory would then hide everything under it.
4. Emit `report "check 23 excluded <path> for <unit> in <file> — the path its brief row names,
   staged by --brief rather than written by the pass"` for each dropped path. `report()` prints
   only under `GOV_UNATTENDED_REPORT=1`, so the default stdout changes by exactly the brief paths
   leaving the `wrote` lists and by nothing else.

The check's header comment gains one paragraph naming the ruling and the two boundaries: the
path, not its directory; the tree at the pass commit, not the working copy.

### Why the tree at the pass commit

Reading brief rows from the working-tree run-state file would pass the two mandated arms and open
the post-hoc dodge the parent build's park refused in its option (a): a run that committed a stray
file could then `--brief` that file afterwards, and the row would silence the report. Check 23
already closes that shape for dispatch rows by anchoring — arm C in the suite pins that a widened
row at a later anchor does not cover a commit already made. A brief row has no anchor, so the
ordering constraint is obtained the way `pass_commit` obtains its own: a row is in force for a pass
only if the pass commit's tree contains it. A row appended after the commit is outside that tree
by construction. The live corpus holds one such row: `TOOL-dRetiredFork-6`'s brief row was parked
before its pass commit `ffdaa82b` but reached the tree only in `295e58d8`, the run-state commit
made after it, so `git show` of that file at the pass commit holds no row for the unit and its
brief path stays reported. That is the cost of the boundary and it is paid rather than waived: a
rule that read the row's timestamp or the working tree to rescue it could not tell it from the
post-hoc row fixture C stages. AC7 names it as the residual. This is one extra git spawn per
`(anchor, unit)` row that reaches the subset test; `TOOL-aQuenchedHarness-7` measured the leg at
2321 spawns after its cut, and the rows that reach the subset test are a subset of the
` dispatch · item ` keys in the live run-state files, which is a `grep -c` away and is not typed
here.

What this does NOT buy, said in the header as well: a run that writes the brief row and the stray
file into the same pass commit still hides the stray file. Both artifacts are authored by the run,
which is the limit check 23's own header already states for dispatch rows, and a brief row naming a
stray path is a lie the `brief-recorded` leg later joins against a build commit. This unit does not
claim to reach it.

### The arm

Five fixtures in region two of `tools/unattended/check-unattended.test.sh`, placed after the
`covers` normalisation pair at `:2951` to `:2968` and before the exit-code arm at `:2970`, using the
existing `drow` helper for the dispatch row and an inline `printf` for each brief row. Every brief
row is written with a real twelve-hex `git hash-object` prefix so the fixture is also a conforming
`brief-recorded` row, even though check 23 never reads the hash.

| Fixture | The pass commit carries | Brief row | Assertion |
|---|---|---|---|
| A · silent | `work/one.txt` declared, the brief file, the run-state file with the brief row | in the pass commit | `miss` on `unattended: check 23 —`; `hit` on the report-channel `check 23 excluded` line under `GOV_UNATTENDED_REPORT=1` |
| B · control | A plus `work/stray.txt` | in the pass commit | `hit` on `wrote work/stray.txt in memory/builds/tRun/RUN.md`; `miss` on `build-brief.md` anywhere in the output |
| C · post hoc | `work/one.txt` and the brief file, NO row yet; a second commit appends the row | after the pass commit | `hit` on a `wrote` list naming the brief path |
| D · directory | A plus `memory/builds/tRun/prompts/other.md` | names `memory/builds/tRun/prompts` | `hit` on a `wrote` list naming `other.md` |
| E · spelling | as A | names `./memory/builds/tRun/prompts/…` | `miss` on `unattended: check 23 —` |

B is what keeps A from passing by finding nothing: the two fixtures differ by one file and the
report must name that file and not the brief. The `hit` in A is the positive artifact that the
exclusion branch ran on that path rather than check 23 skipping the row for an unrelated reason —
a `skipped` line and a silent pass look identical without it. C pins the ordering boundary, which
the two mandated arms cannot see. D pins path-not-directory. E pins the `normpath` call, for the
reason the `covers` arm above it was written: a bare string compare passed both suites at
byte-identical counts when that fix landed.

Red-first: the arm is committed against the checker at base first and the shard is run; A and E
print `FAIL unexpected: unattended: check 23 —`. Then the exclusion lands and the same invocation
prints neither line. The observation is that FAIL-line delta and never the exit status or a
`PASS (<n> assertions)` line, because the suite cannot print one on this tree: backlog row
`TOOL-aHoistedPass-38` records it RED in both shards for causes that predate this build, and two
of them are still in the source at base. `mkconf` at `check-unattended.test.sh:81` to `:106`
declares no `DISPOSITION_CUTOFF`, so `check-unattended.sh:418` prints its notice on every default
run and the `same ... ""` controls at `:283` and `:1880` fail; and the `pedit` of
`Ten kit-owned core items.` at `:1924` and `:1929` is a fixture no-op against
`PROTOCOL.template.md:324`, which reads `Twelve`, so `mutate` at `:245` sets `st=1`. `PASS` prints
only at `st=0` (`:3191`), and `n` otherwise prints only on a floor breach (`:3131`). Repairing
those causes is that row's work under its own owner, outside this ruling's mandate, so this unit
reads the suite as a set of FAIL lines: the lines present at base minus the lines present after are
the arm's, and both full outputs are quoted in the acceptance ledger so the residual is visible
rather than implied. The floors are read the one way the suite still prints `n`, which AC6
spells.

### Inventory

No identifier is minted. No leg name, no shell function, no conf key, no waiver row, no inventory
key of any kind the codebase map enumerates, so `memory/map/generated/` is untouched and no
`subject-pins.tsv` or `selftest-budgets.txt` row moves. `tools/unattended/check-unattended.sh`'s
`ARMS_FLOORS` entry in `.memory-tree.conf` counts `fail` branches, and check 23 reports through
`printf`, so it does not move either.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh` — the exclusion set, the membership test, the report line,
  one header paragraph. About thirty lines.
- `tools/unattended/check-unattended.test.sh` — five fixtures and the two floors. About sixty
  lines.
- `memory/builds/aRatifiedRulings/build/` — the acceptance ledger with the red-first output.

### Alternatives rejected

- **Exclude by directory** (`prompts/` under the build folder). Rejected by the ruling's own
  grammar and by the task: a pass could hide any write under `prompts/`. Fixture D is the arm.
- **Read the rows from the working-tree run-state file.** Rejected above; fixture C is the arm.
- **Extract a shared row-parse helper into `lib-unattended.sh`** for this leg and the sibling.
  Three parameter expansions do not earn a function, and a new shell function is graded by the
  lexicon leg against a shrink-only pin.
- **Declare the brief path in the dispatch row instead**, driver-side. The park refused this as the
  post-hoc-declaration dodge, and declaring it up front would make every orchestrator spell a
  path the driver already knows from the brief row. The reader is the right side.
- **Drop the brief path with `grep -v -x -F -e` beside `$f`.** Exact and cheap, but it cannot
  normalise the row's spelling, and a path holding a space breaks the argument list. The
  `case`-over-a-newline-set form costs the same and does both.

## 5. Production-readiness checklist

- security — the exclusion admits one path per brief row, named in a record the run authored,
  which is the trust level dispatch rows already carry. Ordering-bound to the pass commit's tree,
  so a row written after the fact hides nothing; the same-commit lie is named in section 4 and in
  the header, not closed.
- perf / scale — one `git show` per graded row that reaches the subset test and one `normpath`
  subshell per brief row, against a leg whose spawn count `TOOL-aQuenchedHarness-7` records. The
  five fixtures add five leg invocations to a suite that is no bar leg; the budget row is re-read
  after the measured run rather than re-declared.
- error / empty / loading states — a pass commit whose tree holds no run-state file, or no brief
  row for the unit, yields an empty set and today's behaviour; a row with nothing after the hash
  yields an empty path, which matches no committed path.
- observability — the default output loses exactly the brief paths; the report channel names each
  exclusion. No new skip line, because nothing is skipped.
- risks — two readers of one row grammar in two legs, both spelling the sibling's parse; the
  `-1`/`-10` prefix trap, closed by matching both separators; the one carrier line this unit and
  `TOOL-aRatifiedRulings-1` could both move, `check-unattended.sh:40`, which neither pass touches
  under section 8 F1.
- testing — five fixtures, one red-first observation, two floors moved; section 6.
- migration — N/A. No record shape changes and rows already in the corpus are read as they are.
- user docs — the check's header is the rule's prose home and gains one paragraph;
  `memory/map/features/unattended.md` is not touched, because a dossier sentence restating a
  checker rule is a second answer to one question.

## 6. Acceptance criteria

For AC1 to AC5 the observation is the shard's own FAIL lines: `hit` and `miss` at
`check-unattended.test.sh:57` and `:58` print `FAIL missing: <text>` and `FAIL unexpected: <text>`
and nothing on success, so a criterion holds when the arm's lines are absent from the output at
the landed tip and were present in the red-first run. The exit status is NOT the observation, and
neither is a `PASS` line: `TOOL-aHoistedPass-38` records the suite red in both shards at base for
causes this unit does not repair, so the shard exits 1 before and after, and the ledger quotes the
FAIL lines that remain so nobody reads them as the arm's.

- **AC1** — When `bash tools/unattended/check-unattended.test.sh --shard 2/2` runs fixture A, the
  default leg output carries no `unattended: check 23 —` line, and the same fixture run under
  `GOV_UNATTENDED_REPORT=1` prints a `check 23 excluded` line naming the brief path and the unit.
  Red when: the checker at base is used, which prints the brief path in a `wrote` list — the
  observed RED before the fix — or the exclusion branch never executes and the report line is
  absent while the default output is silent for another reason.
  cost: region two of the suite, minutes rather than seconds; the whole-file figure is the
  `unattended gate selftest` row of `tools/run-gates/selftest-budgets.txt`.
  permission: the suite is on the bar under no chunk at all — `tools/unattended/kit.toml` records
  the 2026-08-23 ruling that removed it — so no boundary runs it and the direct invocation above is
  the only observation. It exits 1 on this tree before and after the fix: `TOOL-aHoistedPass-38`
  records the suite RED in both shards for causes that predate this build, and the two still in
  the source at base are named in section 4. So the observation is the arm's own FAIL lines, as
  the section preamble states, and a FAIL exit is not the arm's failure until a line names it.
  `bash tools/unattended/run-unattended-gates.sh` runs it unsharded with the five sibling suites;
  `TOOL-aTracedSpawn-1` recorded the driver suite dying unsharded at its line 4107, and that line
  was fixed at `8b29f0b9` on 2026-09-08 while the backlog row still reads OPEN.
  fixture: the suite's own scratch repo, `drow` and the `tRun` build; no fixture in this tree.
  Check 23 arms no conf cutoff, so no key gates the fixture.
- **AC2** — When the same shard runs fixture B, the output carries a `wrote` list whose only
  member is the stray file — the line reads wrote work/stray.txt in memory/builds/tRun/RUN.md,
  spelled here without backticks because the spec-tokens leg joins backticked paths against
  `git ls-files` and these are fixture paths — and no occurrence of `build-brief.md`.
  Red when: the exclusion widened past the named path and the stray file went silent too, or the
  brief path stayed in the list beside the stray one.
- **AC3** — When the same shard runs fixture C, where the brief row lands in a commit AFTER the
  pass commit, the output carries a `wrote` list naming the brief path.
  Red when: the rows are read from the working-tree run-state file, so a row appended after the
  commit silences the report.
- **AC4** — When the same shard runs fixture D, whose row names the directory
  `memory/builds/tRun/prompts` and whose pass commits `other.md` under it, the output carries a
  `wrote` list naming `other.md`.
  Red when: the membership test is a containment test, so the directory row covers the file.
- **AC5** — When the same shard runs fixture E, whose row spells the brief path with a leading
  `./`, the default output carries no `unattended: check 23 —` line.
  Red when: the row's path is compared as a raw string and the dot-spelled row excludes nothing.
- **AC6** — When `bash tools/unattended/check-unattended.test.sh --shard 2/2` and the unsharded
  `bash tools/unattended/check-unattended.test.sh` run at the landed tip, neither prints a
  `FAIL executed` line, `FLOOR_SHARD_2` and `FLOOR_ASSERTIONS` each stand exactly the arm's
  executed assertions above their base values of 309 and 392 at `check-unattended.test.sh:3125`
  and `:3108`, and `FLOOR_SHARD_1` at `:3124` is unchanged. The suite prints `n` nowhere on this
  tree except its floor-breach line at `:3131`, because `PASS` needs `st=0`, so `n` is read from
  that line: one shard run with `FLOOR_SHARD_2` over-pinned in place to `99999` by `sed`, reverted
  with `git checkout` of the file afterwards, prints the breach line
  `FAIL executed <n> assertions in shard 2/2 against a floor of 99999`; the same read at base
  gives the base `n`, and the difference is the arm's executed count.
  Red when: a `FAIL executed` line appears in either run at the landed tip, which is a floor
  pinned above what the suite executes; or the tip's breach-line `n` minus the base's is below
  the arm's `hit` and `miss` call count, which is an assertion stranded past an exit or outside
  region two; or the floors did not move, so a stranded arm is invisible.
  cost: two shard runs beyond the red-first pair, one at base and one at the tip, each with the
  floor over-pinned; minutes each, on the same budget row AC1 names.
  figure: the arm's executed count is DERIVED from the two breach-line reads, never from this
  line; by design in section 4 it is seven, because `hit`, `miss` and `same` at
  `check-unattended.test.sh:57` to `:59` each add exactly one and `drow` at `:2777` adds none.
  Both floors are then PINNED in the suite by the build at base plus that count.
- **AC7** — When `bash tools/unattended/check-unattended.sh` runs over this repository at the
  landed tip, every `-build-brief.md` path whose unit's brief row is in the pass commit's tree has
  left its `unattended: check 23 —` line, every such path whose row is NOT in that tree is still
  in it, and every line that named another path beside the brief at base still prints without
  the brief. The expected set is DERIVED from the base run, never counted by hand: for each line
  of the `committed a path outside` class, take the unit, the pass sha and the run-state file
  from its `<unit> at <sha> wrote <paths> in <file>` tail, run `git show` of `<sha>:<file>`, and
  keep the row carrying the unit's whole ` brief · item <unit> · reason ` field; a brief path that
  row names is expected to leave, any other is expected to stay. The loop is recorded in the
  acceptance ledger beside its output, so the audit re-runs it rather than re-counting.
  Red when: an expected-to-leave brief path survives in a `wrote` list; an expected-to-stay one
  leaves it, which means the rows were read from somewhere other than the pass commit's tree; or
  a line that also named another path has gone silent — the widening this ruling does not
  license.
  cost: the leg, `unattended kit gate` in `tools/gate-legs.json`, chunk `declarations`, subject
  `repo`, no guard, so every boundary bar runs it; measured 220 s wall on 2026-09-13 in this
  worktree with three sibling agents editing beside it, and 5 m 35 s earlier the same day under a
  running bar, against the 435 s idle reading the runner records.
  figure: DERIVED at observation time by the loop above. Its result on 2026-09-13, node a, this
  worktree at `2928df63` with the unattended sources byte-identical to base, over the leg's 30
  check-23 lines: 29 of the `committed a path outside` class, each naming exactly one
  `-build-brief.md`, and 1 of the `moved inside its window` class. Of the 29, the pass commit's
  tree holds the unit's brief row for 28 and not for 1: `TOOL-dRetiredFork-6` at `ffdaa82b`,
  whose brief and dispatch rows first reach `memory/builds/dRetiredFork/RUN.md` in `295e58d8`,
  the run-state commit made after the pass commit. So 5 lines fall silent, the ones where the
  brief was the only path; 23 keep printing without the brief; and 1 keeps printing WITH it, by
  construction and not by grandfathering — that row is fixture C's shape on live data, and S1
  cannot tell it from a row appended to hide a stray write. The ruling's "30" is the count of
  brief rows across the live run-state files, 28 in `memory/builds/dRetiredFork/RUN.md` and 2 in
  `memory/builds/dRatifiedSeam/RUN.md` at `2928df63`, not the count of lines that clear.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)`

Chunks and guards, from `tools/gate-legs.json` at base: `unattended kit gate` is chunk
`declarations`, subject `repo`, no guard, and its stdout is AC7's observation. `memory hygiene` is
chunk `records`, no guard, and grades this file. `spec tokens` is chunk `declarations`, no guard,
and joins this section's list and section 6's backticked paths against the manifest and
`git ls-files`. `shell hygiene` is chunk `product`, no guard, and refuses a substitution-fed loop
in the edited checker. `lexicon naming predicates` is chunk `declarations`, guarded on `tools/`,
and grades any function the edit would add. `harness arms` is chunk `declarations`, no guard, and
would move only on a `fail` branch, which this unit adds none of. No leg here is chunk
`selftests`; the suite that observes AC1 to AC6 is on no leg and is named in AC1.

New arm: `tools/unattended/check-unattended.test.sh` · fixtures A and E run against the checker
at base, which prints the brief path in a `wrote` list and so fails their `miss` · `FLOOR_ASSERTIONS`
and `FLOOR_SHARD_2` rise by the arm's executed assertions.

## 8. Open questions

- **F1 — who bumps `KIT_UNATTENDED_VERSION`, and once or per unit?** `TOOL-dMuffledSentinel-3`
  records that a checker edit shipped without a bump made an adopter's `kit-versions` leg refuse
  the pull, and that no rule forces the bump. This unit and `TOOL-aRatifiedRulings-1` both edit
  the unattended kit in disjoint files, and the one surface they share is the carrier line
  `check-unattended.sh:40` together with its three pairs at `unattended.sh:42`,
  `check-brief-recorded.sh:49` and `check-pass-order.sh:38`, which `tools/check-kit-versions.sh`
  holds equal; the rendered copies under `memory/guides/` and `.claude/skills/unattended/` are
  re-made by `adopt-unattended.sh`. Options: each unit bumps in its own pass, which conflicts on
  every carrier; the closing pass bumps once for the kit after both units land; no bump, which
  repeats the refusal. Recommendation: once, at the closing pass, 1.19 to 1.20, by whichever pass
  lands last in the kit, recorded in that pass's declaration.

RESOLVED (agent, 2026-09-13, delegated) F1: the kit version is bumped ONCE, 1.19 to 1.20, by
the closing pass after both units that edit the unattended kit have landed, and that pass
declares every carrier `tools/check-kit-versions.sh` pairs plus the two renders
`adopt-unattended.sh` re-makes. Per-unit bumps collide on every carrier; no bump repeats the
refusal `TOOL-dMuffledSentinel-3` records. This repo's own note that a watched-kit change owes
more stamps than the checker names is the reason the carrier list is spelled in the declaration
rather than remembered. No M3 veto is tripped: the bump is the kit's own convention. The bump
commit lands AFTER the two commits that moved the kit's bytes, and no gate grades that order for
this kit: `tools/memory-tree/check-verdict-epoch.sh` reads `KIT_MEMORY_TREE_VERSION` from the one
engine its `ENGINE` line at `:68` names, and `check-kit-versions.sh` asserts the carriers equal,
not when they moved. The closing pass states this in its declaration rather than showing an
epoch-gate observation the kit has no gate to make.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · §3 · §4 · §5 · §6 · §8 · S5 · AC1 · AC6 · AC7 · folded the round-1
  spec audit, clusters D (id 3), E (id 42), C (ids 4, 14, 44) and F (ids 28, 49). D: AC7 and S5
  assert the set the mechanism derives from each pass commit's tree, naming
  `TOOL-dRetiredFork-6` at `ffdaa82b` as the one brief path that stays by construction. E: AC1
  to AC5 observe the arm's FAIL-line delta and AC6 reads `n` from the floor-breach line, since
  `TOOL-aHoistedPass-38` leaves the suite unable to print `PASS`. C: §3, §5 and F1's body name
  unit 1's real files, the carrier line as the only shared surface, and the write sets as
  disjoint; the F1 RESOLVED mark is unchanged and F1 now states that no epoch gate grades this
  kit's bump order. F: the header tail carries the `ratified` pointer the mark owes.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "check 23 excludes the brief path a dispatched pass
commits undeclared"`, run on 2026-09-13 at this worktree, reported
`scan coverage: 70 files scanned | 0 parse skips | unscanned layers: .sh`. Every file this unit
touches is `.sh`, so the map probe is BLIND to this subject and no claim in this spec rests on it —
its ranked candidates are Python `check_*` functions from other kits and the `.unattended.conf`
affordance seam, none of which is this seam. The seam was found by reading the source and it
exists: `covers` and `normpath` at `lib-unattended.sh:100` and `:79` are the path compare every
containment question in the kit already goes through; the `GIT show "<rev>:<path>"` read of the
run-state file at `check-unattended.sh:1467` is the revision-bound read this unit reuses; and the
brief row parse at `check-brief-recorded.sh:263` to `:265` is the grammar reader this unit spells a
second time rather than a new one. The recall query returned the ruling as its first hit, the
`dUnstalledConvoy-23` spec and red-first record as the origin of check 23's window and `covers`
rule, and the parent park; it also surfaced `TOOL-aSiftedFork-1` and `-2`, which name a different
check 23 — the memory-hygiene one — and were set aside.

Recall terms used: `python tools/memory-recall/query.py "why does check 23 report the brief file a
dispatched pass commits, and what did the owner rule about excluding it" --terms "check 23" "brief"
"verb_brief" "dispatch" "declared write set" "undeclared write" "run-state" "parked" "prompts"
"subset test" "covers" "TOOL-dUnstalledConvoy-10" "TOOL-dBriefedPass-2"`
