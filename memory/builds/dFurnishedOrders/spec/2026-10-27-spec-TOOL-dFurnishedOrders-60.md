# TOOL-dFurnishedOrders-60 — the eighth spec audit's 24 minors: a guard arm that grades the population it claims and names every checker failure, a reach read on the checker's own separators, waiver rows that name what they waive, one pass predicate, an interrupt cleanup on the held child, every deploy key refused by shape, and criteria that read the line they claim

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base dee9e867 · streams tooling · order 32 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-59-round8-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-59-round8-fix-return.md) | research | TOOL-dFurnishedOrders-59 |
| [2026-10-27-build-TOOL-dFurnishedOrders-60-deviation-601.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-60-deviation-601.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-59-round8-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-59-round8-fix-brief.md) | research | TOOL-dFurnishedOrders-59 |
| [2026-10-27-review-TOOL-dFurnishedOrders-59-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-59-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-59 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-7 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-53-spec-audit-round1.md`)
confirmed 11 MEDIUM and 13 LOW findings by raw id, beside its one HIGH, which takes
`TOOL-dFurnishedOrders-59`. BUILD-METHOD M4 batches the minors into one unit (§8 F1). A finding the
report merged into an item still takes its own scope item, at the severity its item gives it
(`review-shape` line: medium 11, low 13).

| Report item | Report id | Severity | Lands on | Scope item |
|---|---|---|---|---|
| M4 | 7 | MEDIUM | unit 54 AC2 | S1 |
| M6 | 10 | MEDIUM | unit 54 S3, AC3 | S2 |
| M7 | 26 | MEDIUM | unit 54 S3, §5, AC3 | S3 |
| M5 | 8 | MEDIUM | unit 57 S4, §6 | S4 |
| L5 | 11 | LOW | unit 57 §4, S1 | S5 |
| L5 | 17 | LOW | unit 57 §4, S1 | S6 |
| L6 | 12 | LOW | unit 57 AC1 | S7 |
| L7 | 13 | LOW | unit 57 title, S1 | S8 |
| M8 | 23 | MEDIUM | unit 57 §5; unit 58 S17 | S9 |
| M1 | 1 | MEDIUM | unit 58 AC19, S25 | S10 |
| M3 | 4 | MEDIUM | unit 58 S3, §4; unit 51 S5 | S11 |
| M2 | 5 | MEDIUM | unit 58 S15, AC8; unit 52 S24, AC13 | S12 |
| M2 | 16 | MEDIUM | unit 58 S15, §10 | S13 |
| M9 | 24 | MEDIUM | unit 58 S18, §4 Migration | S14 |
| M10 | 27 | MEDIUM | unit 58 title, S18, §5, AC14 | S15 |
| L1 | 2 | LOW | unit 58 S20, AC15 | S16 |
| L2 | 3 | LOW | unit 58 S1, §4, §5; unit 52 S13 | S17 |
| L3 | 6 | LOW | unit 58 AC10, AC12, AC20 | S18 |
| L4 | 9 | LOW | unit 58 S23, AC17 | S19 |
| L8 | 14 | LOW | unit 58 AC12 | S20 |
| L9 | 15 | LOW | unit 58 S14, AC11 | S21 |
| L10 | 18 | LOW | unit 58 S8, §4, §10; unit 52 S13, AC4 | S22 |
| L11 | 21 | LOW | unit 58 S17, §5 | S23 |
| L12 | 28 | LOW | unit 58 AC13 | S24 |

The report's skeptics re-graded ids 2, 3, 11, 17 and 21 from medium to low. Each stays at the grade
its item carries, as the raw-id tally does.

## 2. Scope (IN)

Each item states the built tree's end state. The pass does what is missing, or records that a landed
unit already left it so. Where a landed criterion cannot hold as written, that unit's ledger answers
it AMENDED, naming the item. Every ledger read this unit names follows unit 58 S10's rule: each named
token sits on its bullet's first physical line, and the read runs over joined bullets.

### The guard arm's population and failures (M4, M6, M7)

- **S1** — id 7. The untracked path is graded, and the criterion sees it. Unit 54 AC2 reads the
  graded population, not only the absence of a refusal. With the `scratch-kit` entry added, the
  arm's line `guard coverage: <n> path(s) required, <m> uncovered` (unit 48 S16) shows `n` one higher
  than the same call without it. Unit 56 S1's returned dict maps the `scratch-kit` path to the copy's
  covering row. With that row removed from a second copy, the arm names the `scratch-kit` path
  uncovered. Observed by AC1.
- **S2** — id 10. The checker is the arm's first read. `check_selftest_guard_coverage` loads
  `{prefix}/check-spec-tokens.py` from `gov_root` before it derives the required set, so no registry
  read (`load_registry`, `tools/govkit/govkit.py:255`) precedes it. Unit 54 AC3 gains a second case
  that withholds exactly one input: a scratch copy of the tree lacking only the checker. Observed by
  AC2.
- **S3** — id 26. Any failure of the loaded checker is named. Unit 54 S3 widens from "absent or raises
  on load" to every exception the loaded module raises. A failed load, or a failed read of
  `GLOB_MAGIC`, prints `DEAD PROBE: spec-token checker did not load: <reason>`. An exception from
  `derive_tripped_legs` prints `DEAD PROBE: spec-token checker did not answer: <reason>`. Neither lets
  a `Traceback` out of the arm. A checker copied without its memory-tree kit loads with `KIT_DIR` None
  (`tools/check-spec-tokens.py:424-428`, `:874`) and raises `ImportError` only when called
  (`:842-844`), which is the second message. Observed by AC3.

### Unit 57's reach and records (M5, L5, L6, L7, M8)

- **S4** — id 8. The rise is observed. Where the count of `govkit selftest <- ` rows in
  `memory/project/spec-token-waivers.txt` at the tip exceeds the count deviation 501 records, the
  record `2026-10-27-build-TOOL-dFurnishedOrders-57-deviation-571.md` exists in this build's `build/`
  folder with `**Bound:**`, `**Tier:**`, `**Reason:**` and `**Surface:**`. Unit 57's ledger answers S4
  naming this item. Observed by AC4.
- **S5** — id 11. The reach takes the line as printed. The checker pads `HIT` to `HIT   ` and prints a
  space after it (`tools/check-spec-tokens.py:1734`), so a `HIT` line has four spaces before
  `[guards]` and a `WAIVED` line one. Unit 57 §4's pattern admits any run of spaces there. Observed by
  AC5.
- **S6** — id 17. The reach is split on the checker's own separators. Unit 57 S1's reader splits each
  `--list` line on ` [guards] `, ` :: ` and ` — `, the separators `:1734` prints, and keeps the status
  word with its padding stripped. No spacing typed in a spec is load-bearing. Observed by AC5.
- **S7** — id 12. AC1's `--list` clause can fail. It becomes: the set of `govkit selftest <- `
  tokens printed on `HIT` or `WAIVED` `[guards]` lines equals the set of waiver rows with that
  prefix. A mis-keyed row is observed on the plain run's `STALE WAIVER` line (`:1729`, `:1824`),
  which `--list` never reaches (`:1819`). Unit 57's ledger answers AC1 AMENDED, naming this item.
  Observed by AC6.
- **S8** — id 13. The reach is the joined guard. Unit 57's title and S1 read "the leg's joined guard:
  its resolved rows minus the broad set `derive_guarded_legs` excludes"
  (`tools/check-spec-tokens.py:589-608`). A path that meets only broad guards prints a `NEAR` line
  ending `excluded from the join` (`:1628-1635`) and never a `govkit selftest <- ` token. M2's
  cross-read makes the rewording. Observed by AC7.
- **S9** — id 23. A waiver row names what it waives. A row is keyed by token alone
  (`memory/project/spec-token-waivers.txt:3`), and the token is the leg and the spec's first tripping
  path (`tools/check-spec-tokens.py:1620`), so one row waives every live spec sharing that path. Each
  `govkit selftest <- ` row's reason names every spec it waives, and the specs `--list` prints
  `WAIVED` under its token equal the specs its reason names. Unit 57 §5's risk line reads: a new spec
  sharing a waived token is waived, not named, and this criterion is what names it. Observed by AC8.

### Guard rows and their reach (M1)

- **S10** — id 1. The landing rule is read from the rows. Unit 58 AC19 reads parsed rows in place of
  its `git log -S` search. For each commit in the build range, `tools/gate-legs.json` is parsed at
  the commit and at its first parent with `git show <c>:tools/gate-legs.json`. Every commit whose
  `govkit selftest` guard gains a row is a pass commit of unit 50 or unit 58 by S13's predicate. The
  same commit adds a `govkit selftest <- ` row to `memory/project/spec-token-waivers.txt`. A
  `{prefix}/roles/` row on another leg (unit 29 S19's `answered-calls self-test`) is never read. Unit
  58's ledger answers AC19 AMENDED, naming this item. Observed by AC9.

### The interrupt probe (M3, L2)

- **S11** — id 4. The cleanup ends the child it holds. Where a `created` time was recorded at the
  pre-interrupt `live` read, unit 58 S3's rule stands. Where none was, because that read answered
  `unknown` (`tools/run-gates/measure_legs.py:1474-1493`) or the `stub pid is not the child's pid`
  branch never read a state, the cleanup calls `proc.kill()` then `proc.wait()` on the `Popen` child
  the arm holds, while `proc.poll()` is None. The handle rules out pid reuse. Without a recorded time,
  no kill addressed by pid number, `taskkill /PID` or `os.kill`, names the file's pid. Unit 51 S5
  holds on every branch. Observed by AC10.
- **S17** — id 3. Both branches of the first wait. After the pid file is non-empty and unit 51 S1's
  equality holds, the patched first call waits up to 2 s on `self.poll()`. If the child exited, it
  reads `state(pid)` and prints unit 58 S2's DEAD PROBE line. Otherwise it reads `state(pid)` and on
  `live` raises the interrupt. Every interrupt-arm run with the live 60 s stub pays the full 2 s. Unit
  58 §5 says so, and the roles row's `S` in `tools/run-gates/selftest-budgets.txt` (unit 52 S13, AC4)
  counts it. Observed by AC11.

### One pass predicate (M2)

- **S12** — id 5. S15 names its reader. Unit 58 S15's commits are read with
  `routed_commits.read_routed_commits(repo, [range])` (`tools/memory-tree/routed_commits.py:228-239`),
  and the routed entries are read from `ROUTED_PATHS` as `deviation_join` reads them
  (`tools/memory-tree/deviation_join.py:525`). Unit 52 S24's `read_attribution_tokens` route
  (`tools/unattended/lib-unattended.sh:1149-1155`) has no path test, so it is not the reader for this
  rule. Unit 52's ledger answers AC13 AMENDED, naming this item. Observed by AC12.
- **S13** — id 16. One predicate, two callers. `derive_pass_units(commit, units, entries)` in
  `tools/memory-tree/deviation_join.py` holds the per-commit rule `read_first_passes` applies today
  (`:325-340`): a `Pass:` trailer names the units, `none` names none, and with no trailer the subject's
  whole tokens count only when some path passes `routed_commits.test_routed_path`
  (`tools/memory-tree/routed_commits.py:181-186`). `read_first_passes` calls it and keeps the oldest
  commit per unit. S12's reader calls it for every commit. Observed by AC12.

### The deploy descriptor (M9, M10)

- **S14** — id 24. An empty `prefix` stays the default. The top-level `prefix` is refused only when
  present and not a string. `prefix = ""` applies as `tools`, as `tools/govkit/govkit.py:1475`,
  `:7982` and `:13031` read it and `tools/govkit/selftest.py:5530-5531` pins it. A present
  `kit.<eid>.prefix` that is not a string is refused naming that key; today it reaches `.strip` at
  `:1475`. Unit 58's Migration line lists each refused shape beside today's behaviour, as this
  unit's §4 "Migration" does. Observed by AC13.
- **S15** — id 27. Every key the engine reads is refused by its shape, in one place.
  `check_deploy_shapes(deploy)` in `tools/govkit/govkit.py`, called by `load_deploy` (`:1540-1548`),
  raises `Refusal` naming the key for each shape below. Unit 58 S18's four shapes move into it, so
  `target_context` carries no second spelling. The population is every top-level key read through
  `deploy.get(` in `tools/govkit/govkit.py`. `kits` and `own` already refuse a wrong shape by name
  (`:1114`, `:1560-1562`), and so stay where they are. Observed by AC14.

  | key | shape |
  |---|---|
  | `prefix` | string (S14) |
  | `kit`, each `kit.<eid>` | table |
  | `kit.<eid>.prefix` | string (S14) |
  | `answers`, `gate_runner`, `policy`, `charter` | table |
  | `inert` | array |
  | `decline` | array of tables |

### Criteria that read what they claim (L1, L3, L4, L8, L9, L12)

- **S16** — id 2. The fixture never spells the needle. Unit 58 S20's arm builds its stdout fixture
  without the literal, as `'[12/' + 'RECEIPT]'`, and says so. Unit 58 AC15's count of 1 and unit 52
  S23's ban both hold. Observed by AC15.
- **S18** — id 6. Unit 58 AC10, AC12 and AC20 read their ledgers by S10's rule. Each states it.
  Observed by AC16.
- **S19** — id 9. AC17 bounds what else prints. Every line
  `grep -n "govkit selftest" memory/builds/dFurnishedOrders/BACKLOG.md` prints is an ask row, and no
  `SEV` or `KEEP` row names the leg. Unit 58's ledger answers AC17 AMENDED, naming this item. Observed
  by AC17.
- **S20** — id 14. AC12's absence half is seen red. Its grep runs once over a scratch copy of
  `tools/govkit/selftest.py` with a `read_legs_for(` call planted in `check_selftest_guard_coverage`,
  and prints it. A positive half shows the arm calls the loaded module's `derive_tripped_legs`.
  Observed by AC18.
- **S21** — id 15. The pathspec takes two ledger names. Unit 58 S14's pathspec becomes the pair
  `memory/builds/dFurnishedOrders/build/*-build-TOOL-dFurnishedOrders-46-ledger.md` and
  `memory/builds/dFurnishedOrders/build/*-build-TOOL-dFurnishedOrders-46-acceptance-ledger.md`. The
  tree also holds closing-fix, landing, opt-in and followups ledger kinds, which the old glob took.
  Observed by AC19.
- **S24** — id 28. AC13 matches the tripped line. Unit 58 AC13 requires a line that, after its
  two-space indent, starts `govkit selftest <- tools/check-spec-tokens.py [`, the tripped-leg line
  `print_legs_for` prints (`tools/check-spec-tokens.py:666`). Its `UNEVALUATED <leg> <- <glob>`
  lines never satisfy it. Observed by AC22.

### One parse of a `.leg` row, and the leg's price (L10, L11)

- **S22** — id 18. `read_leg_row(line)` in `tools/run-gates/derive-ceilings.py` returns
  `(name, status, seconds)` for a tab-separated line of at least four fields whose fourth parses as a
  float, and `None` otherwise. `read_runs` (`:199`, its parse at `:272-279`) calls it. Unit 58 S8's
  and unit 52 AC4's `R` loads the file by path and calls it over S12's lines, keeping `ok` rows. Unit
  58 S8 states what it leaves out on purpose: `read_runs`' admission of non-`ok` rows inside the
  ceiling window, its foreign-contention census and its memory-pause set-aside. Observed by AC20.
- **S23** — id 21. S17's selection cost is priced. Unit 58 §5 and unit 58's ledger S17 row name the
  `govkit selftest` leg's worst reading from `tools/run-gates/selftest-budgets.txt` (1065 s at
  `:66`) and the checker's commits over the last 30 days (27), and accept the cost under unit 58 §8
  F2. They note that `policy fixtures` already guards the checker. Observed by AC21.

## 3. Non-goals (OUT)

- The HIGH of the same report: `TOOL-dFurnishedOrders-59` (id 19).
- Rewording the spec text of units 51, 52, 54, 57 and 58 in this pass. M2's cross-read reconciles
  them with this unit before the build run's first code pass, and a landed criterion is answered
  AMENDED.
- The report's left-shift gates (the spec-lints, the checklist entries and the policy checks). No
  clause of this build names them.
- Merging the other pass readers, `read_attribution_tokens` and `pass_commit` among them. That is
  `TOOL-dDeclaredLoop-23`'s; S13 lifts one predicate and adds no reader.
- A non-string `kit.<eid>.kit`. It falls back to the default today (`tools/govkit/govkit.py:1479-1481`)
  rather than crashing, and no finding names it.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-51` — S5's cleanup, which S11 makes end the held child on every branch (id 4)
- **consumes-from** `TOOL-dFurnishedOrders-52` — S13's `R` and `S`, S24's route and AC4 and AC13, which S12, S17 and S22 settle (ids 5, 3, 18)
- **consumes-from** `TOOL-dFurnishedOrders-54` — S3 and AC2 and AC3, the checker load and its failure messages, which S1 to S3 settle (ids 7, 10, 26)
- **consumes-from** `TOOL-dFurnishedOrders-56` — S1's returned dict, which S1 reads for the `scratch-kit` path (id 7)
- **consumes-from** `TOOL-dFurnishedOrders-57` — S1, S4, AC1, §4 and §5, the reach, its record and its risk line, which S4 to S9 settle (ids 8, 11, 17, 12, 13, 23)
- **consumes-from** `TOOL-dFurnishedOrders-58` — S1, S3, S8, S14, S15, S17, S18, S20, §5 and AC10 to AC20, which S9 to S24 settle (ids 23, 1, 4, 5, 16, 24, 27, 2, 3, 6, 9, 14, 15, 18, 21, 28)
- **hands-off** `TOOL-dFurnishedOrders-61` — S2, S7, S10, S12 to S15, S19, §4, §5, F2, F3 and AC2, AC5, AC6, AC9, AC12 to AC15, AC17 and AC20, which unit 61 S1 to S6, S10 to S17 and S21 to S27 settle (ids 1, 9, 27, 2, 3, 10, 11, 22, 18, 29, 28, 4, 5, 14, 15, 16, 17, 20, 24, 25 and 30 of the ninth audit)

## 4. Design

### Why one unit

The minors land on units 51, 52, 54, 57 and 58. M4 admits two batch units only when the halves split
into two disjoint write sets by M6. A guard-arm and deploy half (`tools/govkit/`) and a records,
roles and run-gates half would split on clause 1, but clause 2 fails twice. S23 prices the
`govkit selftest` leg whose runs S15's new targets add. S10's criterion reads the pass predicate S13
writes. One unit at order 32, after every unit it lands on, sequences both.

### The guard arm's reads, after this unit

```
cst     := load gov_root/{prefix}/check-spec-tokens.py              S2: before any registry read
           failure (load, GLOB_MAGIC)  -> DEAD PROBE: ... did not load: <reason>     S3
required:= unit 48 S14, S17, S18; unit 50 S1                       S1: n counts untracked paths
hit(p)  := cst.derive_tripped_legs(p, rows)
           failure                     -> DEAD PROBE: ... did not answer: <reason>   S3
```

### The pass predicate, after this unit

```
derive_pass_units(c, units, entries):                                S13
    c.trailer   -> units named by it; "none" -> {}
    no trailer  -> units among c.subject's whole tokens, if some p in c.paths
                   has routed_commits.test_routed_path(p, entries)
read_first_passes := oldest commit per unit over derive_pass_units   (unchanged result)
S12's reader      := derive_pass_units over read_routed_commits(repo, [range]), every commit
```

### The interrupt cleanup, after this unit

```
first wait : pid file non-empty; pid == self.pid; wait <= 2 s on self.poll()           S17
             exited -> state(pid) -> DEAD PROBE line · else state(pid) == live -> interrupt
cleanup    : recorded created -> unit 58 S3's kill · none -> proc.kill(); proc.wait()   S11
             (only while proc.poll() is None; no pid-addressed kill names the file's pid)
```

### What it does not check

- That a waiver reason names a spec correctly beyond the set comparison of S9. A reason naming the
  right specs for the wrong cause passes.
- `read_runs`' admission rule. S22 shares its parse, not its window or census.
- A deploy key no `deploy.get(` reads. S15's population is derived by that grep, so a key read
  another way is outside it.

### Inventory

Minted: `derive_pass_units` in `tools/memory-tree/deviation_join.py`, `check_deploy_shapes` in
`tools/govkit/govkit.py` and `read_leg_row` in `tools/run-gates/derive-ceilings.py`, each answered OK
by the lexicon on `py.function`; the printed token `DEAD PROBE: spec-token checker did not answer`.

### Migration

None for data: no arm here has run. Each of the eleven refused targets AC13 and AC14 list crashes
today. S15 also refuses a string where an array or a table is read, such as `inert = "x"`, which today
is read as its characters rather than crashing. No well-formed descriptor is refused, and
`prefix = ""` keeps its default (S14).

### Rollout

Live at landing, at order 32, after every unit it lands on. Before the build run's first code pass,
M2's cross-read (`memory/guides/BUILD-METHOD.md:66-71`) holds units 51, 52, 54, 57 and 58 to this
unit's items. govkit's, the memory-tree kit's and the run-gates kit's versions move for the kit epoch
leg where their shipped bytes move.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `tools/govkit/govkit.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/memory-tree/deviation_join.py`
- `tools/run-gates/derive-ceilings.py`
- `tools/run-gates/selftest-budgets.txt`
- `memory/project/spec-token-waivers.txt`
- `memory/map/generated/symbols.json` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Two batch units (§8 F1).** Clause 2 breaks twice, as "Why one unit" states.
- **Refuse `prefix = ""` (S14).** It needs a migration note, refusals at two more readers and a moved
  selftest arm, to remove a default three readers and a pinned arm agree on.
- **Narrow unit 58's title and §5 to four keys (S15).** It is the smaller change, but it leaves six
  keys that crash with a traceback, and the security row would still promise a boundary.
- **Key AC9 on the first gaining commit only (S10).** A later row landing without its reach would
  pass.

## 5. Production-readiness checklist

- security — S15 refuses every wrong-typed deploy key at the one load, and S14 keeps an empty prefix
  safe. S11 never kills a pid it cannot tie to the child it started.
- perf / scale — S17 prices 2 s per interrupt-arm run. S14 and S15 add eight `apply` targets
  beyond unit 58 AC14's four to the `govkit selftest` leg, priced with S23's figure at the pass.
- error / empty / loading states — S3 names every checker failure. S2 fixes which input an empty
  `gov_root` fails on first.
- observability — each DEAD PROBE and refusal names its cause or key.
- risks — S13 moves a shipped predicate. Its result is pinned by AC12 against `read_first_passes`'
  current answers.
- testing — AC1 to AC22 by probes and fixtures; the arms of §7 at the close.
- migration — none.
- user docs — none: self-test arms, records, refusal messages and a budget row.

## 6. Acceptance criteria

- **AC1** — When `python -B -c` calls `check_selftest_guard_coverage` with a registry copy gaining the
  `scratch-kit` entry and a legs copy whose row covers its path, `n` in the printed
  `guard coverage:` line is one more than without the entry, and the returned dict maps the
  `scratch-kit` path to that row. With the row removed from a second copy, the arm names the path
  uncovered.
  Red when: an arm that drops untracked paths passes.
  fixture: the registry copy of unit 48 AC6's third case, under `%TEMP%`.
- **AC2** — When the probe runs with `gov_root` an empty scratch directory, it prints
  `DEAD PROBE: spec-token checker did not load` and no registry refusal. Over a `git archive HEAD`
  copy with only `tools/check-spec-tokens.py` deleted, it prints the same line.
  Red when: the required set is derived before the checker loads.
  fixture: the archive copy under `%TEMP%`.
- **AC3** — When the probe runs over a `git archive HEAD` copy with only
  `tools/memory-tree/design_lib.py` deleted, it prints `DEAD PROBE: spec-token checker did not answer`
  naming the `ImportError`, and its output holds no `Traceback`.
  Red when: an exception from the loaded checker escapes the arm.
  fixture: the archive copy under `%TEMP%`, holding no `.git` and no receipt.
- **AC4** — When the `govkit selftest <- ` rows of `memory/project/spec-token-waivers.txt` are
  counted at the tip, the count is at most the one deviation 501 records, or
  `2026-10-27-build-TOOL-dFurnishedOrders-57-deviation-571.md` carries `**Bound:**`, `**Tier:**`,
  `**Reason:**` and `**Surface:**`.
  Red when: the shrink-only count rises with no record.
  figure: both counts DERIVED at the pass.
- **AC5** — When unit 57 S1's reader runs over `python tools/check-spec-tokens.py --list` in a scratch
  clone with one `govkit selftest <- ` waiver row removed and committed, its reach holds that token
  from the `HIT` line beside every `WAIVED` one.
  Red when: the reach drops an unwaived hit.
  fixture: unit 57 AC2's scratch clone under `%TEMP%`.
- **AC6** — When `--list` runs on the tip, the `govkit selftest <- ` tokens on its `[guards]` lines
  equal the waiver rows with that prefix. In the AC5 clone with one row's path replaced, the plain run
  prints `STALE WAIVER` naming it.
  Red when: a mis-keyed or missing row reads green.
- **AC7** — When `--list` runs in a scratch clone holding a live spec whose Files touched names only
  `tools/memory-tree/README.md`, a path only broad guards match, it prints a `NEAR` line for that spec
  ending
  `excluded from the join` and no `govkit selftest <- ` token for it. `grep -c "whole resolved guard"`
  over unit 57's spec prints 0.
  Red when: the reach is described as a guard the join does not read.
  fixture: the AC5 clone.
- **AC8** — When `--list` runs on the tip, for each `govkit selftest <- ` row of
  `memory/project/spec-token-waivers.txt` the specs printed `WAIVED` under its token equal the specs
  its reason names.
  Red when: a row waives a spec its reason does not name.
- **AC9** — When a probe walks the build range with `git show <c>:tools/gate-legs.json` at each commit
  and its first parent, every commit whose `govkit selftest` guard gains a row is a unit 50 or unit 58
  pass by `derive_pass_units` and adds a `govkit selftest <- ` row to the waivers file.
  Red when: a guard row lands in a commit without its reach's rows.
- **AC10** — When `python -c` patches the pre-interrupt state read to answer `unknown`, and again when
  the arm runs with the reaped-child stub, the cleanup calls `proc.kill()` on the held child, the
  child reads `dead` afterwards, and no `taskkill /PID` or `os.kill` names the file's pid.
  Red when: a live stub outlives the run, or a pid with no recorded time is killed.
  fixture: stub `.py` files and a pid file under `%TEMP%`.
- **AC11** — When the interrupt arm runs with the live 60 s stub, its first call returns after the
  2 s wait and raises the interrupt on `live`. `grep -n "^roles adopter self-test"
  tools/run-gates/selftest-budgets.txt` prints a note whose `S` counts those 2 s.
  Red when: the live branch is undefined or its wait unpriced.
- **AC12** — When a probe applies `derive_pass_units` to `read_routed_commits` over a scratch
  repository, a trailerless commit naming two units and writing only under `memory/` names neither,
  the same commit writing a routed path names both, and a `Pass: <id>` commit names that id alone.
  `read_first_passes` returns the oldest of each. `git grep -c "test_routed_path" --
  tools/memory-tree/deviation_join.py` prints 1.
  Red when: a memory-only commit is attributed, or a second routed-path test remains.
  fixture: a scratch repository under `%TEMP%`.
- **AC13** — When `python tools/govkit/govkit.py apply --target <t>` runs over a scratch target whose
  `deploy.toml` holds `prefix = ""`, it is not refused and its kits land under `tools/`. With
  `[kit.memory-recall]` holding `prefix = 5`, it exits 1 or 2 naming `kit.memory-recall.prefix`, with
  no `Traceback`.
  Red when: an empty prefix is refused, or a non-string per-kit prefix reaches `.strip`.
  fixture: two scratch targets under `%TEMP%`.
- **AC14** — When the same command runs over scratch targets whose `deploy.toml` holds, one each,
  `prefix = 5`, `kit = 5`, `[kit] memory-recall = 5`, `answers = 5`, `gate_runner = 5`, `policy = 5`,
  `charter = 5`, `inert = 5`, `decline = 5` and `decline = [5]`, each exits 1 or 2 naming the key with
  no `Traceback`. `grep -oE 'deploy\.get\("[a-z_]+"' tools/govkit/govkit.py` names no key outside
  S15's table, `kits` and `own`.
  Red when: a wrong-typed key reaches a dereference, or a read key is outside the table.
  fixture: ten scratch targets under `%TEMP%`.
- **AC15** — When `git grep -c -F '/RECEIPT]' -- tools/govkit/selftest.py` runs, it prints 1, and
  `git grep -n -F "'RECEIPT]'" -- tools/govkit/selftest.py` prints the arm's split fixture.
  Red when: the fixture spells the needle whole.
- **AC16** — When unit 58 AC10's, AC12's and AC20's ledger reads run over a scratch ledger whose
  named token wraps onto a continuation line, each finds it. Over the real ledgers, `grep -n` finds
  each token on its bullet's first line.
  Red when: a wrapped token reads as an unanswered row.
- **AC17** — When `grep -n -E "^- (SEV|KEEP) · .*govkit selftest"
  memory/builds/dFurnishedOrders/BACKLOG.md` runs, it prints nothing, and every line
  `grep -n "govkit selftest"` prints over that file opens `<n>:- TOOL-dFurnishedOrders-`.
  Red when: a disposition row names the leg.
- **AC18** — When unit 58 AC12's grep runs over a scratch copy of the govkit self-test module whose
  `check_selftest_guard_coverage` holds a planted `read_legs_for(` call, it prints that line. On the
  tip it prints nothing, and `git grep -n "derive_tripped_legs" -- tools/govkit/selftest.py` prints
  the arm's call.
  Red when: the absence check is never seen red.
- **AC19** — When S21's two pathspecs run over a scratch copy holding a `-46-ledger.md`, a
  `-46-acceptance-ledger.md`, a `-46-agent-ledger.md` and a `-46-closing-fix-ledger.md`, they match the
  first two only.
  Red when: another ledger kind is read as the acceptance ledger.
  fixture: a scratch copy under `%TEMP%`.
- **AC20** — When `python -B -c` loads `tools/run-gates/derive-ceilings.py` by path and calls
  `read_leg_row` on an `ok` line, a `timeout` line, a three-field line and a non-numeric fourth field,
  it returns a tuple for the first two and `None` for the rest.
  `python tools/run-gates/derive-ceilings.py --report` prints the same table before and after the
  pass.
  Red when: the two readers parse a row differently.
- **AC21** — When unit 58's ledger S17 row is read by S10's rule, it names the `govkit selftest`
  budget row's worst reading, the checker's commit count over 30 days and unit 58 §8 F2.
  Red when: the leg's widening ships unpriced.
  figure: 1065 s and 27 commits PINNED on 2026-10-27; both DERIVED again at the pass.
- **AC22** — When `python tools/check-spec-tokens.py --legs-for tools/check-spec-tokens.py` runs, a
  line, after its two-space indent, starts `govkit selftest <- tools/check-spec-tokens.py [`. In a
  scratch clone whose `govkit selftest` row carries a glob row and no exact row for the checker, no
  line starts so.
  Red when: an `UNEVALUATED` line satisfies the criterion.
  fixture: a scratch clone under `%TEMP%`.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `roles adopter self-test` · `routed-commits selftest` · `measure-legs selftest` · `run-gates evidence` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC13 AC14 · the guard arm's untracked-path count, a missing checker and a checker with no kit, and the twelve deploy targets, staged one at a time by filtering untracked paths, deriving the required set before the load, removing the call's exception handler and removing `check_deploy_shapes`' call, after deleting `tools/govkit/__pycache__` and running Python with `-B` · none
New arm: tools/roles/adopt-roles.test.sh · covers AC10 AC11 · the cleanup on an `unknown` read and on the reaped-child stub, and the live stub's 2 s wait, staged by killing the file's pid when no time was recorded and by raising the interrupt before the wait, after deleting `tools/roles/__pycache__` and running Python with `-B` · none
New arm: tools/memory-tree/deviation_join.py · covers AC12 · `derive_pass_units` over a memory-only trailerless commit, a routed one and a trailered one, staged by dropping the routed-path test · none

## 8. Open questions

- **F1 — How many units do the minors take?** Options: (a) one; (b) two, a `tools/govkit/` half and a
  records, roles and run-gates half. (b) fails M6 clause 2 twice (§4 "Why one unit"). RESOLVED
  (agent, 2026-10-27, delegated): (a), rung 1, BUILD-METHOD M4's one-unit rule. widens: none ·
  relaxes: none
- **F2 — Where does the deploy shape check live (S15)?** Options: (a) one check called by
  `load_deploy`, holding unit 58 S18's shapes too; (b) the new shapes at `load_deploy` and S18's in
  `target_context`; (c) narrow unit 58's claim to four keys. (b) spells one descriptor's validation
  in two places. (c) leaves six crashing keys. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the skeptic-judged fix of id 27 ("each refused at `load_deploy` naming the key"). widens: none ·
  relaxes: none
- **F3 — An empty `prefix` (S14): keep the default or refuse it?** Options: (a) refuse only a
  non-string, keeping `""` as `tools`; (b) refuse `""` at every reader. (b) changes a default three
  readers and a pinned arm agree on. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the first
  option of the skeptic-judged fix of id 24. widens: none · relaxes: none
- **F4 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the spec audit of the round-7 promotions' minors batched: 11
  MEDIUM and 13 LOW.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-61, promoted from the spec audit of the round-8 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-59-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended:

- `read_first_passes`, `read_routed_commits` and `test_routed_path`
  (`tools/memory-tree/deviation_join.py:325-340`, `tools/memory-tree/routed_commits.py:228-239`,
  `:181-186`), for S12 and S13. `TOOL-dDeclaredLoop-23`'s reuse scout counts four pass readers and
  plans to merge them; S13 lifts one predicate and adds no fifth reader.
- `load_deploy` (`tools/govkit/govkit.py:1540-1548`), with `_check_kits_shape` (`:1114`) and the
  `own` refusal (`:1560-1562`) as the precedents for a named shape refusal, for S14 and S15.
- `read_runs`' row parse (`tools/run-gates/derive-ceilings.py:272-279`), for S22.
- The checker's `--list` and `STALE` lines (`tools/check-spec-tokens.py:1734`, `:1824`), its broad
  split (`:589-608`) and `print_legs_for` (`:633-672`), for S5 to S9 and S24.
- `read_process_created` (`tools/run-gates/measure_legs.py:1474-1493`), for S11.

`python tools/codebase-map/reuse_lookup.py "refuse a malformed deploy descriptor table by its shape
when it is loaded"` ranked `load`, `load_conf`, `shape` and `load_workflows`, name-token neighbours
none of which reads the deploy descriptor. A second lookup, "attribute a commit to a unit by its pass
trailer or subject token and a routed path", ranked `units`, `build_commit`, `resolve_prefix_token`
and `pass_commit`; the last two pass readers have no routed-path test, as S12 states. The recall
probe returned TOOL-dDeclaredLoop-23's reuse scout, this report's M2, the round-6 report's note on
unit 52 S24, unit 58 S15 and TOOL-aWindowedPass-2, none disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "how is a commit attributed to a unit pass by
trailer subject token and routed path, and how is a deploy table refused by shape" --terms "pass
trailer subject token ROUTED_PATHS read_first_passes test_routed_path load_deploy shape refusal waiver
row"`
