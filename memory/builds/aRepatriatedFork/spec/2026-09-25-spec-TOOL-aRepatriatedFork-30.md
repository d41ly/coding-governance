# TOOL-aRepatriatedFork-30 — the suites run at a foreign prefix, and the install-prefix gate is a pure ban

**Status:** CLOSED · rev-6 · 2026-09-30 · node a · Tier-2 · base 2143b6d6 · streams tooling · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md) | research | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 |
| [2026-09-30-build-TOOL-aRepatriatedFork-30-1-acceptance-ledger.md](../build/2026-09-30-build-TOOL-aRepatriatedFork-30-1-acceptance-ledger.md) | journal | — |
| [2026-09-29-prompt-TOOL-aRepatriatedFork-30-build-brief.md](../prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-30-build-brief.md) | journal | — |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-44 TOOL-aRepatriatedFork-45 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-47 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aRepatriatedFork-18` shipped the arm-bearing suites to adopters and held one leg: install them
at a `scripts/` prefix and run each there. It was held because fixture-internal kit paths would
need repathing first, which only running them could verify. Units 23 to 29 drain every hard-coded
kit prefix, so this unit builds that leg and runs it. It then deletes what the drain made
unnecessary: the carried ban list, the waiver registry and both exemption markers. The
install-prefix gate becomes a pure ban with no grandfathering, which is the owner's 2026-09-25 end
state.

## 2. Scope (IN)

- **S1** — A held leg, with a row in `tools/run-gates/selftest-budgets.txt` as the owner ruled for
  `TOOL-aRepatriatedFork-18` §8 F3, clones gov into a scratch directory. Its population is §8 F3's:
  every row that budget file declares, withheld suites included, less the leg's own row. It
  calibrates that population at gov's prefix with `run-selftests.sh --pooled --calibrate`, then
  moves the whole tool root with `git mv` to each prefix §8 F1 names and grades each move with
  `run-selftests.sh --pooled`. That mode's parity compares every row's exit status, `FAIL` count and
  executed count against the calibration, so a suite that fails, skips an arm or runs a different
  count at a foreign prefix reds the leg, named with its prefix. A `--kit <substring>` argument
  passes through, so one suite can be run as a slice. Observed by AC1, AC2.
- **S2** — The carried ban list `tools/install-prefix-carried.txt` is deleted once every row has
  reached zero, together with the `--write-ratchet` and `--rebaseline` modes and the
  `PREDICATE_EPOCH` guard, as §8 F2 resolves. Observed by AC3.
  **Readers:** by name: `tools/check-install-prefix.sh`, `tools/check-install-prefix.test.sh` and
  `tools/govkit/entries/check-install-prefix.kit.toml`, which lists the file and the mode.
  by value: `tools/check-install-prefix.sh`'s ban arm is the only reader of the counts.
- **S3** — The waiver registry `tools/install-prefix-waivers.txt` is deleted once no row is left.
  Observed by AC3.
  **Readers:** by name: `tools/check-install-prefix.sh`, `tools/check-install-prefix.test.sh`,
  `tools/govkit/entries/check-install-prefix.kit.toml`, `tools/govkit/selftest.py`,
  `tools/check-dead-paths.sh` and `tools/check-testsuite-counts.sh`. The lexicon kit's waiver files
  and README cite it as prior art in prose. by value: `tools/check-install-prefix.sh`'s arm 1 is the
  only reader of its rows.
- **S4** — The markers `gov:root-fixture` and `gov:prefix-literal` are deleted. The gate stops
  reading them, and no tracked line under the gate's globs carries one. Observed by AC4.
  **Readers:** by name: `tools/check-install-prefix.sh` and its suite are the only programs that
  read either marker; every other file only carries one. Units 24 to 29 struck most of them, and
  this unit strikes the six they left in shipped code and in the hooks README.
  by value: NO VALUE READERS, because a marker carries no value beyond its reason text.
- **S5** — The gate grades one predicate, epoch 6's, over `TOOL-aRepatriatedFork-23` S2's
  population, with zero tolerance: any hit reds, naming `<path>:<line>`. Arms 1 and 3 are folded
  into it. The population leaves out a tracked file that re-renders byte-identically from a
  `rendered` template `govkit shipped` names, which is `TOOL-aRepatriatedFork-29` §8 F3 (a). The
  test is structural: the file must match its template whole, each `{{TOKEN}}` read as one line of
  any text and a repeated token read as the same text. The template stays in the population, and the
  gate prints how many renders it left out. Observed by AC5, AC6, AC9.
- **S6** — The gate's header states what it does not check, rewritten for the pure ban: a path
  assembled from two variables, a literal inside run-time `eval` text, and a file outside its globs.
  Observed by AC7.
- **S7** — The check-install-prefix entry and every other kit this unit moves take their version
  bump in every carrier. Observed by AC8.
- **S8** — The classes `TOOL-aRepatriatedFork-28` §4 "Returned" and `TOOL-aRepatriatedFork-46`
  handed this unit are drained, so the ledger reaches zero. A fixture laid out at a foreign literal
  prefix names each kit through a variable that holds that kit's directory name, derived from gov's
  tree or from the suite's existing kit-name map. The frozen adopter receipt writes its adopter-side
  paths through the `{prefix}` token too, and its reader resolves that token by field: gov's tool
  root for a `source`, and the adopter's recorded root for a `path`. Its generator emits the same
  shape. The install-prefix self-test's fixtures use a kit that exists only in the fixture, and they
  build gov's prefix from a variable. The fixture playbook, the fixture records and the four
  workflow renders drain through S5's render rule. Observed by AC3, AC9.
- **S9 (rev-6)** — The closing review's L1. S2 and S3 deleted the ledger and the waiver registry,
  and prose still described both as live: `check_entry_producer`'s docstring, the govkit and
  four other map dossiers, two line-length comments and a merge-rows suite comment. Each is
  rewritten to the pure ban or put in the past tense. The class gate: `tools/check-dead-paths.sh`
  grades the map dossiers under `memory/map/features/` too, since a dossier is the live inventory a
  session reads and not an append-only record; the rest of `memory/` stays out of scope. Observed
  by AC10.

## 3. Non-goals (OUT)

- Draining a literal of any class but S8's. A row outside those classes that is not zero when this
  unit starts is returned to the unit that owns it, and this unit does not delete the ledger over
  it.
- Putting the S1 leg on the ordinary bar. The owner ruled it a held leg, run once per build.
- Adopter repos. The gate still skips at a repo that is not a kit source.
- Amending `TOOL-aRepatriatedFork-18`. The held leg S1 builds is the one that CLOSED spec specified
  and parked (§4 Evidence). A landed record is frozen, so the dependency is stated here and not as a
  §3 edge, which the edge join would require that spec to reciprocate.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-23` — the ban's population, which becomes the pure ban's.
  Its predicate reaches this unit as epoch 6, through `TOOL-aRepatriatedFork-46`.
- **consumes-from** `TOOL-aRepatriatedFork-24` — a waiver registry four rows shorter, and hooks that
  run at the prefixes S1 installs at.
- **consumes-from** `TOOL-aRepatriatedFork-25` — ledger rows at zero for received code.
- **consumes-from** `TOOL-aRepatriatedFork-26` — ledger rows at zero for docs.
- **consumes-from** `TOOL-aRepatriatedFork-27` — ledger rows at zero for markers and comments.
- **consumes-from** `TOOL-aRepatriatedFork-28` — suites whose fixtures derive their prefix. Without
  them S1's leg is red by construction.
- **consumes-from** `TOOL-aRepatriatedFork-29` — gov-side files that derive their root, and the
  population rule for gov's own renders.
- **consumes-from** `TOOL-aRepatriatedFork-46` — the epoch-6 predicate, with its homonym and brace
  rules, and a ledger left holding only the literal-prefix classes this unit's population rule owns.
- **consumes-from** `TOOL-aRepatriatedFork-47` — one answer for the `{prefix}` token in every reader,
  which S1's installs at three prefixes depend on.

## 4. Design

### Evidence

- `TOOL-aRepatriatedFork-18` §7's third `New arm:` and its run-state decision entry of
  2026-09-24 record the leg and why it was parked. Its §8 F3 records the owner's ruling that it is
  a held leg with a budget row.
- From the 2026-09-25 prefix census at `2143b6d6` (session scratchpad, not committed): the ledger
  holds 139 rows and 904 occurrences, the waiver registry 11 rows, and the two markers 32 and 24
  lines (census §0 and §1). The registry's own 10 literals are this unit's under
  the census record's section 7's ownership rule.
- `govkit apply` already takes a prefix; `TOOL-aRepatriatedFork-18` AC2 installed the suites at
  `scripts/` through it.
- The unattended suites alone cost about 2.5 h pooled on node a, per this repo's recorded
  experience of running them once, early.

### Inventory

The S1 leg's driver is one new shell script in the run-gates kit, `foreign-prefix.gov.test.sh`,
withheld from adopters beside its gov-only sibling `run-gates.gov.test.sh` and declared the same
way: a `project-owned` rule in that kit's descriptor and an `[[exempt_leg]]` row in govkit's
registry. The lexicon's `--suggest` grades no file-name cell, so it named the driver's functions and
the sibling named the file. It adds one new leg in `tools/gate-legs.json` whose `chunk` holds it.

### Migration

Deleting two tracked files moves the check-install-prefix entry's shipped set. Its version bumps,
and an adopter's `govkit update` reports both files as withdrawn.

### Files touched (estimate)

`tools/check-install-prefix.sh` · `tools/check-install-prefix.test.sh` ·
`tools/install-prefix-carried.txt` · `tools/install-prefix-waivers.txt` ·
`tools/govkit/entries/check-install-prefix.kit.toml` · `tools/gate-legs.json` ·
`tools/run-gates/selftest-budgets.txt` · the run-gates descriptor and govkit's registry · the
foreign-prefix fixtures of S8 in `tools/govkit/selftest.py`, `.githooks/pre_push_bar_selftest.py`,
`tools/check-wiring.test.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`,
`tools/run-gates/adopt-run-gates.test.sh`, `tools/unattended/adopt-unattended.test.sh`,
`tools/unattended/check-unattended.test.sh`, `tools/workflows/check-review-join.test.sh`,
`tools/workflows/check-verifier-fanout.test.sh` and `tools/workflows/unattended-build.test.sh` · the
frozen receipt, its generator and `tools/dead-path-waivers.txt` · the six marker lines · the prose
that names either deleted file, which the dead-path gate reads

### Alternatives rejected

- Keeping the ledger at zero rows as a guard. A zero-row ban list and a pure ban grade the same
  thing, and the list is a place a future row can be written by hand.

## 5. Production-readiness checklist

- security — none; a gate over tracked text and a scratch-clone leg.
- perf / scale — S1 costs hours, which is why it is held and budgeted. The pure ban is one grep over
  the population and is faster than the three arms it replaces; AC6 records both.
- error / empty / loading states — an empty population still refuses as a dead probe.
- observability — S1 prints `run-selftests.sh`'s pooled verdict for every suite at every prefix,
  each block headed by the prefix it graded.
- risks — a suite that passes at `scripts/` by skipping. S1 compares executed counts, not exit codes.
- testing — AC2's staged break.
- migration — the version bump in S7.
- user docs — `WIRE-INTO-PROJECT.md`'s install-prefix paragraph, if it names the ledger.

## 6. Acceptance criteria

- **AC1** — When the S1 leg, budgeted in `tools/run-gates/selftest-budgets.txt`, runs, every suite in its population reports, at every prefix, an executed
  assertion count equal to its count at gov's prefix. The acceptance ledger records the table.
  Red when: any suite fails, or its count differs at any prefix.
  permission: the leg is held; the main loop runs it once, after units 23 to 29 are terminal.
  cost: hours; see §5.
- **AC2** — Red-first control: one suite's fixture is given back a literal `tools/` in a scratch
  clone, and the S1 leg reds naming that suite at `scripts/`. Staged, recorded and discarded.
  Red when: the leg stays green, so it cannot see the class it exists for.
- **AC3** — When `git ls-files -- tools/install-prefix-carried.txt tools/install-prefix-waivers.txt`
  runs, it prints nothing, and `check-install-prefix.sh --write-ratchet` exits with the usage
  refusal.
  Red when: either file is tracked, or the mode still runs.
- **AC4** — When `git grep -nE 'gov:(root-fixture|prefix-literal)' -- tools skills .githooks` runs,
  it finds nothing.
  Red when: a marker survives anywhere the gate grades.
- **AC5** — When a scratch clone adds one literal of each epoch-6 spelling to one file,
  `bash tools/check-install-prefix.sh` exits 1 naming each `<path>:<line>`, and with the literals
  gone it exits 0.
  Red when: any spelling passes, or the clean tree reds.
- **AC6** — When `bash tools/check-install-prefix.sh` runs on the real tree, it exits 0 and prints
  the population size.
  Red when: it reds, or reports an empty population.
  figure: DERIVED at observation time.
- **AC7** — When the header of `tools/check-install-prefix.sh` is read, its "does not check"
  paragraph names the three blind spots of S6.
  Red when: the paragraph still describes the ledger or the markers.
- **AC8** — `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch
  --base 2143b6d6` names no kit this unit moved.
  Red when: a moved kit's carrier was missed.
- **AC9** — When `bash tools/check-install-prefix.sh --list` runs on the real tree, it names the
  seven renders it left out, and a scratch clone that appends one line to one of them makes the
  gate grade that file again.
  Red when: a render is graded while it matches its template, or stays left out once it does not.
- **AC10** — rev-6. `bash tools/check-dead-paths.sh` exits 0 on the real tree with the map dossiers
  in its haystack, and a `tools/check-dead-paths.test.sh` arm planting a dossier under
  `memory/map/features/` that names a deleted file reds by its `<path>:<line>`.
  Red when: the arm passes, which the `7de665e5` gate does, or six dossier lines still name a
  deleted install-prefix file.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `testsuite counts (every bar self-test prints one)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `govkit selftest` · `run-gates canary` · `run-gates gov canary` · `dead-path carriers (deleted files still named)` · `lexicon naming predicates` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix` · `review-join self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `check-wiring self-test` · `memory-hygiene self-test` · `pre-push bar self-test` · `run-gates adopter e2e` · `playbook validity gate` · `review-protocol parity (kit vs dogfood)`

New arm: the S1 held leg beside `tools/run-gates/run-selftests.sh` · one suite given back a
literal prefix in a scratch clone · a new budget row

New arm: `tools/check-install-prefix.test.sh` · one fixture literal per epoch-6 spelling against
the pure ban, and a clean fixture · the suite's floor moves to its new arm count

New arm: `tools/check-install-prefix.test.sh` · a fixture render left out while it matches its
template, and graded once a line is appended to it · none

New arm: `tools/check-dead-paths.test.sh` · rev-6: a map dossier naming a deleted file is a carrier · the suite's floor rises by one

## 8. Open questions

- **F1 — at which prefixes does the S1 leg install?** Option (a): `scripts/` and `vendor/gov/`, as
  the owner suggested. The second prefix has two segments, which is the case the gate's own
  `_seg_kit` arithmetic once got wrong. Option (b): those two plus the repo root. The root is a
  legal install with its own failure shape, an empty prefix joined as `/<kit>`, and arm 1 existed
  for it. Option (c): `scripts/` only. Recommendation: (b). It costs half as much wall time again
  as (a), once per build, and it is the only run that exercises the empty prefix.
  RESOLVED (owner, 2026-09-25): (b), the recommendation.
- **F2 — what is left of the ban's machinery once the ledger is deleted?** Option (a): nothing. The
  modes `--write-ratchet` and `--rebaseline` and the epoch guard are deleted; a future widening
  reds its new hits, and they are drained before the widening lands. Option (b): keep the epoch and
  `--rebaseline`, so a future widening can re-create a ledger. Recommendation: (a). The owner's end
  state is no grandfathering, and (b) keeps the one mechanism that grandfathers.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.
- **F3 — which suites does the S1 leg run?** Option (a): the shipped suites, as
  `TOOL-aRepatriatedFork-18` specified. Option (b): every suite, withheld ones included. A
  `cp -r` installer receives withheld files unless it follows WIRE's removal step (census §0), and
  `TOOL-aRepatriatedFork-28` derived them all. Recommendation: (b). Without execution, the
  derivation in a withheld suite is unproven, and proving it is what this leg is for. It costs more
  wall time, once per build.
  RESOLVED (owner, 2026-09-25): (b), the recommendation.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft. Owner rulings of 2026-09-25: the hard-coded prefixes are
  drained first and `TOOL-aRepatriatedFork-18`'s held leg comes after; the carried list, the waiver
  file and both markers end empty and are deleted, and the gate is a pure ban with no
  grandfathering.
- rev-2 · 2026-09-25 · §8 resolved by the owner: every fork takes its recommendation.
- rev-3 · 2026-09-30 · header order 15 -> 18 · §3 Edges · S5 · AC5 · §7 New arm: this unit now
  follows `TOOL-aRepatriatedFork-46` and `TOOL-aRepatriatedFork-47`, adopted after the drain. The
  predicate it makes pure is epoch 6's, which 46 moves. The kit-id argv class
  `TOOL-aRepatriatedFork-28` returned here is closed by 46's homonym rule instead; the other classes
  28 returned stay this unit's.
- rev-4 · 2026-09-30 · S1 · S4 · S5 · S8 added · §3 Non-goals · §4 Inventory and Files touched ·
  §5 · AC9 added · §7 New arm, the unit pass before code. S1 installs by moving gov's whole tool
  root with `git mv` in the scratch clone rather than through `govkit apply`. An apply target has
  neither gov's records nor its registry, and it receives no withheld suite, which §8 F3 (b) runs,
  so its counts would differ from gov's for reasons other than the prefix. The parity it grades is
  `run-selftests.sh --pooled` against a calibration taken at gov's prefix in the same clone, which
  is the seam that already compares exit status, `FAIL` count and executed count. S5 gains the
  render rule `TOOL-aRepatriatedFork-29` §8 F3 (a) handed this unit, since the ledger's workflow and
  unattended-fixture rows are renders. S8 states how the classes `TOOL-aRepatriatedFork-28` and
  `TOOL-aRepatriatedFork-46` returned here drain, and §3 stops calling that out of scope. S4 names the
  six markers the drain units left. AC9 observes the render rule.
- rev-5 · 2026-09-30 · AC5 reflowed, no change of meaning: its command was wrapped across two lines,
  so hygiene check 23 read no token in it and could not join the acceptance ledger's answer.
- rev-6 · 2026-09-30 · closing review round 1 fold: L1 — prose that still described the deleted
  install-prefix ledger and registry as live is rewritten, and the dead-path gate grades the map
  dossiers so a dossier cannot carry a deleted file again (S9, AC10).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "count hardcoded kit prefix literals in shipped files"`
found no seam that grades a spelling outside `tools/check-install-prefix.sh`, which this unit
narrows in place. The S1 leg reuses the held-leg budget mechanism in
`tools/run-gates/selftest-budgets.txt` as its population, and `run-selftests.sh --pooled` with its
calibration as its parity check, rather than writing a comparison of its own. rev-4 dropped
`govkit apply --prefix` as the installer, for the reason its §9 line gives. The render rule reads
`govkit.py shipped`, the verb the gate already reads, for the `rendered` templates.

Recall terms used: `held leg budget scripts prefix install shipped suites execution proof carried
ban waiver marker pure ban`.
