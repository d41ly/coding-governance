# TOOL-dScopedBuild-39 — the round-1 audit of units 25 to 35, its 29 minors batched: 16 MEDIUM and 13 LOW findings, each its own scope item

**Status:** DEFERRED · rev-3 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 17 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-39-deviation-391.md](../build/2026-11-01-build-TOOL-dScopedBuild-39-deviation-391.md) | deviation | — |
| [2026-11-01-build-TOOL-dScopedBuild-39-deviation-392.md](../build/2026-11-01-build-TOOL-dScopedBuild-39-deviation-392.md) | deviation | — |
| [2026-11-01-prompt-TOOL-dScopedBuild-39-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-39-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dScopedBuild-39-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-39-promoted-fix-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dScopedBuild-40-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-40-promoted-fix-brief.md) | research | TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 |
| [2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-36 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 25 to 35
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md`)
exited CONVERGED with 32 confirmed findings: three at HIGH, which `TOOL-dScopedBuild-36` to
`TOOL-dScopedBuild-38` take, and 29 minors. BUILD-METHOD M4 batches every MEDIUM and LOW into one
unit, two only where they split into disjoint write sets by M6; §4 "Why one unit" says why these stay
one. Each finding is named by report id and is its own scope item, including the ids the report
merged into one item (M2, M10, M11, L1, L3), each of which takes that item's severity. The minors
land on twelve units, so this unit repairs no one unit and builds after every unit of the build
(order 17).

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M1 | MEDIUM | 1 | unit 29 S2, §4 | S1 |
| M2 | MEDIUM | 2 | unit 35 AC18 | S2 |
| M2 | MEDIUM | 13 | unit 35 AC18 | S3 |
| M3 | MEDIUM | 3 | unit 25 AC1 | S5 |
| M4 | MEDIUM | 4 | unit 26 AC1 | S6 |
| M5 | MEDIUM | 5 | units 7 S5, 1 S1, 14 S1 | S8 |
| M6 | MEDIUM | 6 | unit 35 S10; unit 4 S3 | S9 |
| M7 | MEDIUM | 7 | unit 32 AC2 | S10 |
| M8 | MEDIUM | 12 | unit 26 AC1; unit 30 AC3 | S7 |
| M9 | MEDIUM | 14 | unit 35 S26, AC26 | S12 |
| M10 | MEDIUM | 15 | unit 32 S2, §4 | S14 |
| M10 | MEDIUM | 31 | unit 32 S2, §4 | S15 |
| M11 | MEDIUM | 23 | unit 28 S1, Files, §5 | S16 |
| M11 | MEDIUM | 30 | unit 28 S1, Files | S17 |
| M12 | MEDIUM | 27 | unit 26 S1, S2, §5 | S18 |
| M13 | MEDIUM | 28 | unit 35 S21, AC21 | S19 |
| L1 | LOW | 8 | unit 26 S2, §4 | S20 |
| L1 | LOW | 19 | unit 26 S2, §4 | S21 |
| L2 | LOW | 9 | unit 27 S2, AC3 | S22 |
| L3 | LOW | 10 | unit 28 §4 | S23 |
| L3 | LOW | 24 | unit 28 §4, S2 | S24 |
| L3 | LOW | 32 | unit 28 §4 | S25 |
| L3 | LOW | 17 | unit 28 §4, §5 | S26 |
| L4 | LOW | 16 | unit 32 AC2 | S11 |
| L5 | LOW | 18 | unit 30 §4 | S27 |
| L6 | LOW | 20 | unit 35 S26, §10 | S13 |
| L7 | LOW | 21 | unit 29 §3, §10 | S28 |
| L8 | LOW | 25 | unit 26 §7, Files | S29 |
| L9 | LOW | 29 | unit 35 AC18 | S4 |

That is 16 MEDIUM and 13 LOW findings by raw id. Every item supersedes or completes a clause of the
unit it lands on by name; that unit's §3 names this unit, and its acceptance ledger answers the
clause with a note naming this unit's scope item.

## 2. Scope (IN)

- **S1** — id 1. The failed-exit line names the script. Unit 29 S2's and §4's
  `<argv[0] basename>` reads `<script basename>`: argv[1]'s basename when unit 29 S1 rewrote argv[0]
  to the interpreter, else argv[0]'s. So a non-zero exit prints `not-installed: map_diff.py exited
  <rc>` and an `OSError` prints `not-installed: map_diff.py could not start: <why>`, as unit 29 AC2
  expects. Observed by AC1.
- **S2** — id 2. Unit 35 AC18's `grep -n "scope"` is superseded by AC2, which reads the closed
  `<kind>` bullet whole, its continuation lines included, or the `gen:record-kinds` region
  TOOL-dTotalRecall-1 S6 renders where that region exists. Observed by AC2.
- **S3** — id 13. The same probe closes id 13: it never confines the read to the one line opening
  the bullet, because the list spans `memory/HYGIENE.md:628-631` and a correct build may add `scope`
  on a continuation line. Observed by AC2.
- **S4** — id 29. The same probe closes id 29: it prints 0 for both files at base, so it is red
  until unit 35 S18 is built. Observed by AC2.
- **S5** — id 3. Unit 25 AC1's `decisions.major` half, and its `review.build.when` half with it, is
  observed over `tools/unattended/unattended.sh` alone: `READER_SHAPES`' `.sh` row
  (`tools/policy/check_policy.py:433-434`) run over that file's non-comment lines, never the
  tree-wide `scan_reader_keys('.')` an ancestor's reader fills. This supersedes unit 25 AC1's
  command. Observed by AC3.
- **S6** — id 4. Unit 26 AC1's `flow.route-backs` half is observed in `reuse_check.py` alone, by
  S7's named-reader grep over that file. Observed by AC4.
- **S7** — id 12. A named reader beside the coverage scan. The first `.py` row of `READER_SHAPES`
  (`check_policy.py:426-427`) counts any `identifier("literal"`, so a `Refusal("<key>", …)` fills it.
  Unit 26 AC1 adds a grep for `read_policy_value("<key>"` in `reuse_check.py`, each key at least one
  line, and no `"get"` argv there; unit 30 AC3 adds the same for `deviation.gate` over
  `routed_commits.py` and `deviation_join.py`. No grep demands one line per key, because unit 26 S1
  reads the second-pass key in both `question` and `join`. `scan_reader_keys` stays the coverage
  half. Observed by AC4 and AC5.
- **S8** — id 5. One owner per superseded clause, and it is the earlier unit's builder, building the
  repair's form. Unit 7 (order 9) adds `core-result`'s per-kind row in `build_records.py` and its
  `TYPED_RECORD_KINDS` member in `tools/memory-tree/tree_lib.py` together, in unit 31 S2's
  spelling, so the import check of PLAY-dOrderedCharter-42 S2 holds at every step; unit 31 S2
  observes them and adds no second row. Unit 1 (order 1) does not move `read_first_passes`,
  `read_commit_times` or `derive_pass_units`, and builds unit 33 S1 and S2's form. Unit 14 (order 2)
  does not mint `read_gate_value`, and reads `deviation.gate` through `read_policy_value` and unit
  30 S2's `check_gate_value`, which unit 14's builder mints in unit 30's spelling. Each of units 1,
  7 and 14 carries this in its §3 hands-off line to this unit. Observed by AC6.
- **S9** — id 6. `routed_commits.py --unit-commits <unit> <range>` is built by unit 4's builder
  (order 14) as part of its S3, in unit 35 S10's spelling; unit 35 S10 observes it, and its
  Inventory's row for the mode is superseded by unit 4 as its minter. Observed by AC7.
- **S10** — id 7. Unit 32 AC2 also asserts that the `gates-green` arm's body calls
  `derive_bar_scrub "unattended: gates-green"` and that `unattended.sh` holds no `_gscrub` loop
  outside it. At base `grep -c _gscrub` prints 5, so the clause is red until unit 32 S1 is
  built. Observed by AC8.
- **S11** — id 16. Unit 32 AC2 also asserts that `derive_bar_scrub()` is defined once and the one
  `_gknobs="` line sits inside its body. At base the definition count is 0. Observed by AC9.
- **S12** — id 14. A failing `GOV_BASH`, traced. Unit 35 S26 catches `corpus_ids.Problem` and
  re-raises it as `Refusal`, the leg's exit 2 with its line. Unit 35 AC26 is split into two plants:
  a stub that passes `-c :` and exits 1 on the dispatch-row script, and a stub that fails `-c :`.
  Observed by AC10.
- **S13** — id 20. `corpus_ids.resolve_bash()` stays the spawn's resolver, same kit. Its
  system32 and windowsapps path filter (`tools/memory-tree/corpus_ids.py:390-433`) and S12's
  `Refusal` on a non-zero spawn answer TOOL-dSettledRoster-6 for this consumer: a bash that starts
  but cannot run the script is the leg's exit 2, never an `attended` reading. §8 F2. Observed by AC10.
- **S14** — id 15. The reap's slug. Unit 32 S2's signature reads
  `run_gate_bar <label> <slug> <R> [<legs file>] [-- <env word>...]` and it calls
  `run_orphan_reap "$slug"` (`tools/unattended/unattended.sh:1847`), so unit 32 S3's callers read
  `run_gate_bar "build-exit" "$slug" "$ASHA"` and `run_gate_bar "build-core" "$slug" "$R" "<core legs
  file>" -- GATE_FULL=1`. Observed by AC11.
- **S15** — id 31. The bound. `run_gate_bar` sets `RB_BOUND` for its one `run_bounded` call the
  way `gates-green` does: `GB_SUM` where `derive_gate_backstop` (`unattended.sh:9670`) derives,
  `GATE_BOUND` otherwise (`:11156`), cleared after the call (`:11274`, `:11278`). Observed by AC12.
- **S16** — id 23. The adopter snippets. The memory-trigger snippets in `tools/memory-tree/README.md`
  (`:128`) and `WIRE-INTO-PROJECT.md` (`:268`) read `--diff-filter=ACMRD`, each with one line saying
  a deletion runs the leg so check 32 sees it. Unit 28 §5's user-docs line names both. Observed by
  AC13.
- **S17** — id 30. The third copy, `WIRE-INTO-PROJECT.md:268`, is in S16, and AC13's grep reads all
  three files. Observed by AC13.
- **S18** — id 27. A failed adapter load is not a verdict. In `reuse_check.py`, a `LookupError` from
  `resolve_kit_dir` or an `ImportError` loading `policy_value.py` is the CLI's exit 2 with one line
  naming `memory-tree/policy_value.py`, as unit 26 S2's other refusals are. Observed by AC14.
- **S19** — id 28. The bar's whole verdict set. Unit 35 S21 reads the `verdict` file's word against
  every word `run-gates.sh` writes (`:5390`, `:5527-5543`): `GREEN` is rc 0 and `RED` rc 1, as now;
  `HOST`, `REFUSED`, `TREE MOVED` and any word outside that list each refuse, naming the word.
  Observed by AC15.
- **S20** — id 8. One value check. Unit 26 S2's second-pass read is spelled
  `routed_commits.check_gate_value("build.reuse-check.second-pass",
  read_policy_value("build.reuse-check.second-pass", root), ("off", "on"))`, its `Refusal` the CLI's
  exit 2. The `flow.route-backs` read keeps its inline non-negative-integer check, because an
  integer has no closed set for `check_gate_value` to hold. Unit 26 §4 Inventory's "S2's check is
  inline at the two reads" is superseded. Observed by AC16.
- **S21** — id 19. The same spelling closes id 19, the reuse lens's statement of the duplicate.
  Observed by AC16.
- **S22** — id 9. One fixture for unit 27's exit arm. Unit 27 S2 and AC3 run the sliced
  `check_build_exit` over the two trees the routed-commits selftest builds, unit 3 AC2's and unit 9
  AC3's, each built through `routed_commits.build_fixture` by `python -c` from the driver suite with
  `ASKS_CMD` declared in its `.unattended.conf`. Unit 27 AC3's fixture line is superseded. §8 F3.
  Observed by AC17.
- **S23** — id 10. Unit 28 §4's second Evidence bullet is superseded: with unit 28 S1, a
  deletion-only commit runs the gate over an empty staged set and an empty `FILES` listing, because
  `STAGED_SET` and `_SBUILD` fill only from the ACMR read
  (`tools/memory-tree/check-memory-hygiene.sh:654-670`). Only check 32's `deviation_join.py --staged`
  verb, through its own `-M` name-status read, sees the deletion. Observed by AC18.
- **S24** — id 24. Check 32 runs unconditionally under `--staged`, under no `FILES` or `STAGED_MD`
  guard, so the deletion S23 describes reaches it. Observed by AC18.
- **S25** — id 32. The same correction closes id 32. Observed by AC18.
- **S26** — id 17. The cost. Unit 28 §4's fourth bullet and §5's "about 20 s" are superseded by the
  wall time of one deletion-only `check-memory-hygiene.sh --staged` run on this tree, measured at
  the pass and pinned in unit 28's ledger. Observed by AC19.
- **S27** — id 18. Unit 30 §4's last Evidence command reads
  `git grep -l read_policy_value c891f007 -- 'memory/builds/*/spec/*' | wc -l`, which prints 50.
  Observed by AC20.
- **S28** — id 21. Unit 29 §3's first bullet's reason is superseded. The run-gates copies are not
  shared because a canonical block in `tools/lib/` would hold one of three differing rules:
  `measure_legs.derive_leg_argv` (`tools/run-gates/measure_legs.py:503`) also resolves `{prefix}`
  and aliases, and `tools/run-gates/regen.py:273` does neither. No tree rule forbids the block.
  `derive_leg_argv` is the closest existing seam, named in unit 29's §10 by this item. §8 F4. The
  rationale has no behaviour; unit 29's acceptance ledger names this item. Observed by AC22.
- **S29** — id 25. Unit 26 §7's first `New arm:` line names the existing reader-coverage check with
  no edit to `tools/policy/check_policy.py`, so no `policy fixtures` leg is owed. Observed by AC21.

## 3. Non-goals (OUT)

- The report's left-shift gates: spec-lint, spec-audit checklist, parity and lint rules, one per
  item. No clause of this build names them.
- The three HIGH findings, which units 36 to 38 take.
- Rewording units 1 to 35. Each item supersedes a clause by name, answered in that unit's ledger.
- Moving any unit's order. The disposal adds this unit at order 17 and renumbers nothing.

### Edges

- **consumes-from** `TOOL-dScopedBuild-1` — S1's move of the first-pass readers, which S8 rules unit 1 does not build, building unit 33's form (id 5)
- **consumes-from** `TOOL-dScopedBuild-4` — S3's per-unit commit read, whose `--unit-commits` mode S9 makes unit 4's to mint (id 6)
- **consumes-from** `TOOL-dScopedBuild-7` — S5's `core-result` registration, which S8 rules unit 7 builds in unit 31 S2's spelling, row and member together (id 5)
- **consumes-from** `TOOL-dScopedBuild-14` — S1's `read_gate_value`, which S8 rules unit 14 does not mint, minting unit 30's `check_gate_value` instead (id 5)
- **consumes-from** `TOOL-dScopedBuild-25` — AC1's tree-wide reader scan, which S5 restricts to `unattended.sh` (id 3)
- **consumes-from** `TOOL-dScopedBuild-26` — S1 and S2's reads, AC1, §4 Inventory and §7's arm line, which S6, S7, S18, S20, S21 and S29 complete (ids 4, 12, 27, 8, 19, 25)
- **consumes-from** `TOOL-dScopedBuild-27` — S2's and AC3's fixture, which S22 makes one (id 9)
- **consumes-from** `TOOL-dScopedBuild-28` — S1's trigger, §4 Evidence and §5's cost and docs lines, which S16, S17 and S23 to S26 complete (ids 23, 30, 10, 24, 32, 17)
- **consumes-from** `TOOL-dScopedBuild-29` — S2's exit line and §3's rationale, which S1 and S28 correct (ids 1, 21)
- **consumes-from** `TOOL-dScopedBuild-30` — S2's `check_gate_value`, which S20 calls, AC3, which S7 completes, and §4's command, which S27 respells (ids 8, 12, 18)
- **consumes-from** `TOOL-dScopedBuild-32` — S1's scrub, S2's `run_gate_bar` and AC2, which S10, S11, S14 and S15 complete (ids 7, 16, 15, 31)
- **consumes-from** `TOOL-dScopedBuild-35` — AC18, S10, S21 and S26, which S2 to S4, S9, S12, S13 and S19 complete (ids 2, 13, 29, 6, 14, 20, 28)
- **hands-off** `TOOL-dScopedBuild-41` — S22's two trees, which this unit's builder builds with `build_fixture(..., checkout=True)` and reads by `git diff --cached --name-only`; AC10's first plant, a `.cmd` stub on Windows asserting no `GOV_BASH is set to` line; S18's load failure as the class, any exception or a module lacking `read_policy_value`; and S8, S9, S15, S16, S27 to S29, §4 and AC4, AC5, AC13, AC20 and AC21, which that unit's S1 to S9, S12, S16 and S18 to S20 complete (ids 1, 21, 2, 14, 23, 3, 10, 17, 18, 26, 7, 9, 11, 13)
- **hands-off** `TOOL-dScopedBuild-42` — S22's two trees and AC17's driver-suite arm, which that unit's pass extends with a count of the staged ask rows after each run (id 14)

## 4. Design

### Why one unit

M6's clauses decide a split. S10, S11, S14, S15, S19 and S22 write `tools/unattended/unattended.sh`
or its suite; S1 and S12 write `tools/memory-tree/routed_commits.py`; S18 and S20 write
`tools/codebase-map/reuse_check.py`; S16 the two adopter docs; S24 the hygiene gate. A shell and a
Python half fail clause 2: S22's driver-suite arm builds its trees through
`routed_commits.build_fixture`, an acceptance input of the shell half in the file the other half's
S1 and S12 write. No other partition separates them, so the minors are one unit.

### Evidence

- `check_policy.py:426-427` is the literal-first-argument `.py` row and `:433-434` the `policy.py
  get` row; the `.sh` scan over `unattended.sh` prints `False False` at base (S5, S7).
- `awk` over the closed `<kind>` bullet of `tools/memory-tree/HYGIENE.template.md` and
  `memory/HYGIENE.md` piped to `grep -cw scope` prints 0 for each at base, and the bullet is four
  lines (S2 to S4).
- `corpus_ids.py:405-418` runs `[GOV_BASH, "-c", ":"]` and raises `Problem` when it fails;
  `routed_commits.py` catches `Refusal` alone (S12).
- `unattended.sh:1847` takes a slug and returns at once without one; `:267` falls back to
  `${GATE_BOUND:-0}` when `RB_BOUND` is empty (S14, S15).
- `git grep -n "diff-filter=ACMR "` prints `.githooks/pre-commit:227`, `WIRE-INTO-PROJECT.md:268` and
  `tools/memory-tree/README.md:128` at base (S16, S17).
- `run-gates.sh:5527-5543` sets `GREEN`, `RED`, `HOST`, `REFUSED` or `TREE MOVED`, and `:5390` writes
  `verdict\tREFUSED` (S19).
- `git grep -l read_policy_value c891f007 -- 'memory/builds/*/spec/*' | wc -l` printed 50 on
  2026-11-01, PINNED (S27).

### Inventory

Minted: nothing new. `check_gate_value` is unit 30's, `--unit-commits` unit 35's spelling, built by
unit 4 (S9), and `run_gate_bar` unit 32's, its signature widened by `<slug>` (S14). No lexicon cell
applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 17, after every unit, as the disposal rule places a batch landing on several units.
Where an item corrects an interface or a clause an earlier unit builds, S8, S9 and S14, that unit's
builder builds the item's form, which its §3 hands-off line to this unit names, and this unit's pass
observes it and builds what remains.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/README.md`
- `WIRE-INTO-PROJECT.md`
- `tools/codebase-map/reuse_check.py`

### Alternatives rejected

- **Two units, shell and Python.** Rejected by §4 "Why one unit": S22's driver-suite arm reads the
  Python fixtures as an acceptance input.
- **One unit per minor.** M4 forbids it.
- **Renumbering units 31, 33 and 30 before the units they repair (S8).** A disposal places only the
  units it adds; S8 moves the build of each superseded clause instead.

## 5. Production-readiness checklist

- security — S12, S18 and S19 each turn an unread or unloaded value into a refusal; nothing widens a
  write path.
- perf / scale — S15 restores the backstop bound to the two new bars; S26 states the hook's cost.
- error / empty / loading states — S18's load failure and S19's non-GREEN words each get a named
  refusal line.
- observability — S1's line names the script; S19's refusal names the word.
- risks — S8, S9 and S14 rest on earlier builders reading their §3 hands-off lines; AC6, AC7 and
  AC11 observe the built form at the close.
- testing — each AC a probe, a fixture or a slice; AC6, AC7, AC11 and AC15 at the close.
- migration — none.
- user docs — `tools/memory-tree/README.md` and `WIRE-INTO-PROJECT.md`, S16.

## 6. Acceptance criteria

- **AC1** — When unit 29 AC2's fixture runs the claim arm with a map stub that exits 3, it prints
  `claim · not-installed: map_diff.py exited 3`; with an argv whose first word cannot start, it
  prints `not-installed: map_diff.py could not start:` and the reason.
  Red when: the line names the interpreter's basename.
  fixture: unit 29 AC2's.
- **AC2** — When `awk '/<kind>. is closed/{f=1;print;next} f&&/^- /{exit} f' FILE | grep -cw scope`
  runs with FILE each of `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` on the
  built tree, each prints at least 1; where the file holds a `gen:record-kinds` region, `sed -n
  '/gen:record-kinds/,/\/gen:record-kinds/p' FILE | grep -cw scope` prints at least 1 instead.
  Red when: the kind list omits `scope`, the case that prints 0 at base.
  figure: DERIVED at observation; each prints 0 at `c891f007`.
- **AC3** — When `python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as
  c; rx = c.READER_SHAPES[2][1]; ks = {m.group(2) for l in open(sys.argv[1], encoding='utf-8') if
  not l.lstrip().startswith('#') for m in rx.finditer(l)}; print('review.build.when' in ks,
  'decisions.major' in ks)" tools/unattended/unattended.sh` runs on the built tree, it prints
  `True True`.
  Red when: either read in that file is not the counted `policy.py get` shape.
  figure: DERIVED at observation; it prints `False False` at `c891f007`.
- **AC4** — When `git grep -nE 'read_policy_value\("(build\.reuse-check\.second-pass|flow\.route-backs)"'
  -- '*reuse_check.py'` runs on the built tree it prints at least one line per key, and `git grep -n
  '"get"' -- '*reuse_check.py'` prints nothing.
  Red when: a key is read as an argv list, or spelled only in a refusal.
  permission: observed at the close, after unit 26 is built.
- **AC5** — When `git grep -n 'read_policy_value("deviation.gate"' -- '*routed_commits.py'
  '*deviation_join.py'` runs on the built tree it prints at least one line, and the same grep for
  `'"get"'` prints nothing.
  Red when: `deviation.gate` has no named adapter read.
- **AC6** — When `git grep -n "def read_gate_value" -- tools/memory-tree` runs after units 1, 7 and
  14 are built it prints nothing, `grep -c "^def read_first_passes" tools/memory-tree/deviation_join.py`
  prints 1, and `python -c` imports `build_records` with `core-result` in its per-kind table and in
  `tree_lib.TYPED_RECORD_KINDS`.
  Red when: an earlier unit builds the clause its repair supersedes, or the factory refuses at import.
  permission: observed at the close.
- **AC7** — When `grep -c -- "--unit-commits" routed_commits.py` runs after unit 4 is built it prints
  at least 1, and unit 4's `per-unit` reading runs over it in unit 35 AC10's fixture.
  Red when: unit 4 calls a mode nothing has minted.
  permission: observed at the close.
- **AC8** — When `grep -c _gscrub tools/unattended/unattended.sh` runs on the built tree it
  prints 0, and the `gates-green` arm's body holds `derive_bar_scrub "unattended: gates-green"`.
  Red when: the arm keeps its inline loop beside the function.
  figure: DERIVED at observation; it prints 5 at `c891f007`.
- **AC9** — When `grep -c '^derive_bar_scrub()' tools/unattended/unattended.sh` runs it prints 1, and
  `awk '/^derive_bar_scrub\(\)/{f=1} f&&/^}/{exit} f' tools/unattended/unattended.sh | grep -c
  '_gknobs="'` prints 1.
  Red when: the list stays inline in `gates-green`.
- **AC10** — When `check_routed_commits` runs with `GOV_BASH` a stub that exits 0 on `-c :` and 1 on
  the dispatch-row script, it exits 2 and does not read the unit `attended`; with a stub that exits
  1 on `-c :`, it exits 2 printing the `corpus_ids` line.
  Red when: a failed spawn falls back to the spec's Files touched, or `Problem` escapes as a
  traceback.
- **AC11** — When `run_gate_bar "build-exit" tExit <R>` runs in the driver suite's fixture whose proc
  ledger holds an orphan for `tExit`, the `PROCMON_CMD` stub records that orphan's reap before the
  bar runs.
  Red when: the reap reads no ledger.
  fixture: unit 1 AC5's slug fixture with a planted proc ledger.
  permission: observed at the close, after units 1 and 32 are built.
- **AC12** — When the same call runs with `run_bounded` replaced by a function recording
  `$RB_BOUND`, it records the declared backstop's `GB_SUM`; with `derive_gate_backstop` failing it
  records `GATE_BOUND`; after the call `RB_BOUND` is empty.
  Red when: the bar runs under bare `GATE_BOUND` while a backstop derives.
- **AC13** — When `git grep -n "diff-filter=ACMR " -- .githooks tools/memory-tree/README.md
  WIRE-INTO-PROJECT.md` runs on the built tree, it prints nothing.
  Red when: any adopter snippet keeps the ACMR trigger.
  figure: DERIVED at observation; it prints three lines at `c891f007`.
- **AC14** — When `reuse_check.py bound` runs with `resolve_kit_dir` pointed at a directory holding no
  `policy_value.py`, it exits 2 naming `policy_value.py`, and no `BACKLOG.md` row is
  staged.
  Red when: the load failure exits 1, read as a bound hit.
  fixture: unit 12's `reuse_check.py --fixture` tree.
- **AC15** — When `--close tRun --override gates-green` runs over a `gates-run` fact whose record
  reads `REFUSED`, `build-complete` is UNMET naming `REFUSED`; over one reading `TREE MOVED`, it is
  UNMET naming `TREE MOVED`; over `RED` with an `x OWN` row it stays unit 35 AC21's.
  Red when: a non-GREEN word other than RED reads as rc 0.
  permission: observed at the close, after unit 35 is built.
- **AC16** — When `git grep -n 'check_gate_value("build.reuse-check.second-pass"' --
  '*reuse_check.py'` runs it prints at least one line, and unit 26 AC2's `["maybe"]` stub exits 2
  naming `maybe` through `Refusal`.
  Red when: a second inline off/on check guards the read.
- **AC17** — When the driver suite builds unit 3 AC2's and unit 9 AC3's trees through
  `routed_commits.build_fixture` with `ASKS_CMD` declared and runs the sliced `check_build_exit` over
  each under `warn-and-ask`, it returns 0 and stages one ask per finding, naming `tools/beta/b` and
  `feat`; a rerun at the same tip stages none.
  Red when: the exit arm runs over a tree whose findings differ from the push arm's.
- **AC18** — When the hygiene suite's scratch tree stages a deletion-only commit of a spec and runs
  `check-memory-hygiene.sh --staged`, the output holds check 32's line, and no other check names the
  deleted path.
  Red when: check 32 is skipped on an empty `FILES` listing.
  permission: observed at the close, after units 2 and 14 are built.
- **AC19** — When one deletion-only `check-memory-hygiene.sh --staged` run is timed on this tree at
  the pass, its wall time is written to unit 28's ledger in place of the 20 s figure.
  Red when: the ledger keeps a figure measured on another input shape.
  figure: PINNED at the pass.
- **AC20** — When `git grep -l read_policy_value c891f007 -- 'memory/builds/*/spec/*' | wc -l` runs,
  it prints 50.
  Red when: the command prints a number other than the one pinned beside it.
  figure: PINNED; 50 at `c891f007`.
- **AC21** — When `git log --format=%s BASE..HEAD -- tools/policy/check_policy.py` runs at the close,
  no subject names `TOOL-dScopedBuild-26`.
  Red when: unit 26's build edits the arm its §7 calls existing without naming its leg.
- **AC22** — When `awk '/^\*\*Evidences:\*\* TOOL-dScopedBuild-29$/{f=1;next} /^\*\*Evidences:\*\*|^#/{f=0}
  f' memory/builds/dScopedBuild/build/*.md | grep -c 'TOOL-dScopedBuild-39 S28'` runs after unit 29
  is built, it prints at least 1.
  Red when: unit 29's ledger answers its §3 rationale without naming this item, or the note sits in
  another unit's `**Evidences:**` block; a planted journal holding the note under
  `**Evidences:** TOOL-dScopedBuild-30` prints 0.
  figure: DERIVED at observation; it prints 0 at `c891f007`.
  permission: observed at the close, after unit 29 is built.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC11 AC12 AC15 AC17 · the reap, the bound, the overridden close's verdict words and the one-fixture exit, staged by an empty slug, a cleared bound, a REFUSED word read as 0 and the slug fixture · none

New arm: tools/memory-tree/routed_commits.py · covers AC10 · the two `GOV_BASH` stubs, staged by catching `Refusal` alone · none

New arm: tools/codebase-map/reuse_check.py · covers AC14 AC16 · the unloadable adapter and the out-of-set value through `check_gate_value`, staged by letting `ImportError` escape · none

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC18 · the deletion-only staged commit, staged by guarding check 32 on `FILES` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause.
  It lands on twelve units. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the precedent
  `TOOL-dWitnessedBar-91` §8 F1 set. widens: none · relaxes: none
- **F2 — Keep `corpus_ids.resolve_bash()` for S26's spawn, or carry `tools/lib/resolve_bash.py`
  inline (id 20)?** Options: (a) keep it and record that the path filter and S12's refusal answer
  TOOL-dSettledRoster-6 here; (b) carry the canonical probe inline with a parity row, so a bash that
  cannot see the script is skipped for the next candidate. Under (b) S12's first plant, a stub that
  starts and fails the script, is skipped rather than exiting 2, so (b) fails AC10. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 3, M3 veto 1, the one survivor. widens: none · relaxes: none
- **F3 — Which fixture does unit 27's exit arm run over (id 9)?** Options: (a) the driver suite's slug
  fixture, given both findings by hand; (b) the two trees the routed-commits selftest builds, built
  through `routed_commits.build_fixture` with `ASKS_CMD` declared. (b) observes the exit on the
  findings the push arm's fixtures produce and reuses one fixture builder. RESOLVED (agent,
  2026-11-01, delegated): (b), rung 3, the tie-break on reuse of a seam M5 found. widens: none ·
  relaxes: none
- **F4 — Promote the argv rewrite to `tools/lib/`, or keep it kit-local (id 21)?** Options: (a) a
  canonical `tools/lib/` block carried inline in `routed_commits.py` with a parity row; (b) the
  kit-local function with §3's reason corrected and `derive_leg_argv` named as the closest seam. (a)
  holds one of three differing rules and leaves the two run-gates copies outside its parity row, so
  it closes no more follow-ups than (b) and adds a file. RESOLVED (agent, 2026-11-01, delegated):
  (b), rung 3, the tie-break on fewer open questions. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 25 to 35, its 29
  minors: MEDIUM ids 1 2 3 4 5 6 7 12 13 14 15 23 27 28 30 31 and LOW ids 8 9 10 16 17 18 19 20 21
  24 25 29 32.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullet mirroring the edges of TOOL-dScopedBuild-41,
  the promotions of the round-1 spec audit of units 36 to 39 (ids 1, 21, 2, 14, 23, 3, 10, 17, 18, 26, 7, 9, 11, 13).
- rev-3 · 2026-11-01 · §3 · the Edges block gains the bullet mirroring the edges of TOOL-dScopedBuild-42, the promotion of the round-1 spec audit of units 40 and 41 (id 14).

## 10. Reuse audit

Each item extends the seam of the unit it lands on and mints nothing: `check_gate_value` (unit 30
S2) for S20, `routed_commits.build_fixture` (`tools/memory-tree/routed_commits.py:387`) for S22,
`READER_SHAPES` (`tools/policy/check_policy.py:422`) for S5 and S7, `corpus_ids.resolve_bash()` for
S13, and `gates-green`'s bound (`tools/unattended/unattended.sh:11156`, `:11274`) for S15.
`python tools/codebase-map/reuse_lookup.py "compare a fixture repository's index and working tree
before and after a call"`, run for this audit's set, ranked `build_fixture` among its candidates,
the fixture builder S22 reuses; no item needs a seam beyond those named.

Recall terms used: `python tools/memory-recall/query.py "how were the minor findings of a promoted spec audit disposed" --terms "minors batch spec-audit promoted supersedes clause acceptance ledger hands-off order earlier builder"`
