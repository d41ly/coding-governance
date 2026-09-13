# TOOL-aRatifiedRulings-2 — check 23 stops reporting the brief `--brief` staged, by the path its row names

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-2 · base 9fac2b53 · streams tooling

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
- **S5** — The leg run over this repository names no brief path in any check-23 line, and every
  line that named another undeclared path beside the brief still prints, minus the brief. Observed
  by AC7.

## 3. Non-goals (OUT)

- **Nothing else leaves the population.** The measurement in section 4 shows 24 of today's 29
  brief-naming lines also name shared records and generated indexes — `memory/LIVE.md`,
  `memory/ledger/2026-09.md`, `memory/backlog/TOOL.md`, the build README — which `--dispatch`
  refuses to declare because they are `SHARED_RECORDS` or `GENERATED_INDEXES`. Those lines keep
  firing after this unit. That class is the one `TOOL-aLeakedHandle-3`'s park describes and it needs
  its own ruling; this unit does not widen into it, and the build README's "thirty corpus lines
  clear" sentence is corrected at close from the leg's own count rather than from this paragraph.
- **The hash in the brief row is not read here.** Whether the committed blob matches the row's
  hash is the `brief-recorded` leg's join, made at the build commit. Reading it twice is two
  answers to one question.
- **No change to `--brief`, `--dispatch`, `pass_commit`, `covers` or the row grammar.** The
  writer stays as it is; only the reader's exclusion set changes.
- **No new shell function in either file.** The lexicon leg parses `.sh` and grades `*.test.sh`
  helpers too, and `VERB_OFFENDER_PIN` in `.lexicon.conf` is shrink-only, so a `brow()` beside
  `drow()` would red the bar. The fixture rows are written inline.
- **No kit version bump inside this unit.** `TOOL-aRatifiedRulings-1` edits the same file for
  check 37, and two units bumping `KIT_UNATTENDED_VERSION` independently is a conflict or a double
  bump. Section 8 carries it.
- **Sequencing with unit 1 is the build plan's.** Both units write
  `tools/unattended/check-unattended.sh`, so `--dispatch` refuses them as a concurrent pair by its
  own disjointness rule; nothing here needs to say which goes first.

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
by construction. This is one extra git spawn per `(anchor, unit)` row that reaches the subset
test; `TOOL-aQuenchedHarness-7` measured the leg at 2321 spawns after its cut, and the rows that
reach the subset test are a subset of the ` dispatch · item ` keys in the live run-state files,
which is a `grep -c` away and is not typed here.

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

Red-first: the arm is committed against the checker at base first and the suite is run; A and E
print `FAIL unexpected: unattended: check 23 —` and the run exits 1. Then the exclusion lands and
the same invocation prints `PASS (<n> assertions)` with `n` at or above the raised floor. Both
outputs are quoted in the acceptance ledger.

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
  `-1`/`-10` prefix trap, closed by matching both separators; the shared file with
  `TOOL-aRatifiedRulings-1`, sequenced by the build plan.
- testing — five fixtures, one red-first observation, two floors moved; section 6.
- migration — N/A. No record shape changes and rows already in the corpus are read as they are.
- user docs — the check's header is the rule's prose home and gains one paragraph;
  `memory/map/features/unattended.md` is not touched, because a dossier sentence restating a
  checker rule is a second answer to one question.

## 6. Acceptance criteria

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
  the only observation. `bash tools/unattended/run-unattended-gates.sh` runs it unsharded with the
  five sibling suites; `TOOL-aTracedSpawn-1` recorded the driver suite dying unsharded at its line
  4107, and that line was fixed at `8b29f0b9` on 2026-09-08 while the backlog row still reads OPEN.
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
- **AC6** — When the suite finishes, its closing `PASS (<n> assertions)` line reports `n` at or
  above the raised `FLOOR_SHARD_2` for the shard run and the raised `FLOOR_ASSERTIONS` for an
  unsharded one, and `FLOOR_SHARD_1` is unchanged.
  Red when: the arm sits outside region two, so the shard floor counts assertions the shard never
  executes; or the floors were not moved, so a stranded arm is invisible.
  figure: both floors are PINNED in `tools/unattended/check-unattended.test.sh` by the build, from
  the `n` the suite itself printed, and rise by the assertions the arm executes — seven as
  designed in section 4, counted from the run rather than from this line.
- **AC7** — When `bash tools/unattended/check-unattended.sh` runs over this repository after the
  fix, no `unattended: check 23 —` line names a path ending in `-build-brief.md`, and every line
  that named another undeclared path beside the brief at base still prints without it.
  Red when: a brief path survives in any `wrote` list, or a line that also named a shared record
  or generated index has gone silent — the widening this ruling does not license.
  cost: the leg, `unattended kit gate` in `tools/gate-legs.json`, chunk `declarations`, subject
  `repo`, no guard, so every boundary bar runs it; measured 5 m 35 s wall on 2026-09-13 while
  sibling builds ran beside it, against a 435 s idle reading the runner records.
  figure: DERIVED at observation time from the leg's stdout. PINNED for comparison, 2026-09-13,
  node a, this worktree at `16da4c6a` with the unattended sources byte-identical to base: 30
  check-23 lines, 29 of the `committed a path outside` class and every one of those naming a
  `-build-brief.md`, 5 naming the brief alone, 24 naming shared records or generated indexes as
  well, and 1 line of the `moved inside its window` class. The 30 brief rows in the three live
  run-state files are the figure the ruling's "30" matches; the lines that fall silent are 5.

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
  `tools/unattended/check-unattended.sh`; two independent bumps collide on every carrier
  `tools/check-kit-versions.sh` pairs, and the rendered copies under `memory/guides/` and
  `.claude/skills/unattended/` are re-made by `adopt-unattended.sh`. Options: each unit bumps
  in its own pass, which conflicts; the closing pass bumps once for the kit after both units land;
  no bump, which repeats the refusal. Recommendation: once, at the closing pass, 1.19 to 1.20, by
  whichever pass lands last in the kit, recorded in that pass's declaration.

RESOLVED (agent, 2026-09-13, delegated) F1: the kit version is bumped ONCE, 1.19 to 1.20, by
the closing pass after both units that edit `check-unattended.sh` have landed, and that pass
declares every carrier `tools/check-kit-versions.sh` pairs plus the two renders
`adopt-unattended.sh` re-makes. Per-unit bumps collide on every carrier; no bump repeats the
refusal `TOOL-dMuffledSentinel-3` records. This repo's own note that a watched-kit change owes
more stamps than the checker names is the reason the carrier list is spelled in the declaration
rather than remembered. No M3 veto is tripped: the bump is the kit's own convention.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

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
