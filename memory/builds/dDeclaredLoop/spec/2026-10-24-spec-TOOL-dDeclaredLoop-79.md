# TOOL-dDeclaredLoop-79 — the round-4 spec audit's 28 minors, batched

**Status:** DEFERRED · rev-5 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 40 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 |
| [2026-10-24-build-TOOL-dDeclaredLoop-79-deviation-791.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-79-deviation-791.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 |
| [2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md`)
exited CONVERGED with 31 confirmed findings over units 68 to 75, the round-3 promotions. Its three highs
are units 76, 77 and 78, one per id. This unit is the batch BUILD-METHOD M4 makes of the rest, every
MEDIUM and every LOW, each by its report id and each its own scope item, where the report merged ids
into one item too. The minors land on eight units, so this unit repairs none in particular and builds
after every unit (order 40). Where a minor is the medium grade of a defect a high unit closes, the item
here is what that grade's fix asks beyond the high unit's mechanism.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2, 16, 32 | S1, S2, S3 |
| M2 | MEDIUM | 4, 23 | S4, S5 |
| M3 | MEDIUM | 11, 30 | S6, S7 |
| M4 | MEDIUM | 17, 34 | S8, S9 |
| M5 | MEDIUM | 3 | S10 |
| M6 | MEDIUM | 9 | S11 |
| M7 | MEDIUM | 10 | S12 |
| M8 | MEDIUM | 5 | S13 |
| M9 | MEDIUM | 13 | S14 |
| M10 | MEDIUM | 14 | S15 |
| M11 | MEDIUM | 20 | S16 |
| M12 | MEDIUM | 21 | S17 |
| M13 | MEDIUM | 22 | S18 |
| M14 | MEDIUM | 24 | S19 |
| M15 | MEDIUM | 35 | S20 |
| M16 | MEDIUM | 36 | S21 |
| L1 | LOW | 7, 12 | S22, S23 |
| L2 | LOW | 6 | S24 |
| L3 | LOW | 15 | S25 |
| L4 | LOW | 18 | S26 |
| L5 | LOW | 26 | S27 |
| L6 | LOW | 28 | S28 |

That is 21 MEDIUM and 7 LOW findings by raw id. The report's five refuted findings, ids 19, 25, 27, 29
and 31, are not in the disposal population.

## 2. Scope (IN)

- **S1** — id 2. `read_driver_conf` (`TOOL-dDeclaredLoop-70` S1) unsets every requested name in its
  subshell before `. "$1"`, so a value the caller's environment exports never reads as the conf's: a name
  the conf leaves unset answers unset, and the caller's driver default applies, 72's `memory` and 70 S3's
  empty population. Observed by AC1.
- **S2** — id 16. The same subshell sets `ROOT` to the tree's top level and `CONF` to the conf's path
  before sourcing, as the driver does (`tools/unattended/unattended.sh:546-548`), so a conf composing a
  value from `$ROOT` reads as the driver reads it. Observed by AC2.
- **S3** — id 32. The plant `env-leak` joins `loop_table.py --fixture`: `MEMORY_ROOT=elsewhere` and
  `PHASES_EXTRA=BOGUS` exported over a `.unattended.conf` that sets neither; `resolve_memory_root` answers
  `memory` and the adopter population is empty. Observed by AC3.
- **S4** — id 23. `tools/loop/kit.toml`'s `requires` gains `run-gates`, beside `TOOL-dDeclaredLoop-56`
  S17's `memory-tree`, so `derive_unsatisfied_requires` (`tools/govkit/govkit.py:950`) sees the loop kit's
  dependency on the normaliser `TOOL-dDeclaredLoop-68` S1 resolves. run-gates declares `requires = []`
  (`tools/run-gates/kit.toml:15`), so no cycle forms. Observed by AC4.
- **S5** — id 4. 68 §5's claim that the loop kit's descriptor requires the kits it resolves holds: every
  kit named by a `resolve_kit_dir("<kit>", ...)` call under `tools/loop/` sits in that descriptor's
  `requires` or `requires_if`, and a probe lists any that does not. Observed by AC5.
- **S6** — id 11. 68 S1's normaliser is applied inside the bash `resolve_bash` answers,
  `. "$1"; write_normaliser "$2" "$3" "$4" && sed -E -f "$2" < "$5"`, so that bash's PATH supplies `sed`;
  no Python argv under `tools/loop/` names a bare `sed`. Observed by AC6.
- **S7** — id 30. A failure to start that bash, or any non-zero exit of the apply step, refuses the re-run
  as `witness: normaliser unavailable — sed: <reason>` and records no hash, widening 68 S3's named
  refusal. Observed by AC7.
- **S8** — id 17. The `loop breakpoints fixtures` leg's guard becomes `{prefix}/loop/`,
  `{prefix}/memory-tree/` and `{prefix}/lib/`, the shape `build-index selftest` carries, in both
  `tools/gate-legs.json` and `tools/loop/kit.toml`, so an edit to the memory-tree kit's `parse_conf`
  selects the leg. Observed by AC8.
- **S9** — id 34. The widened guard is checked against the files the module reaches: a probe applies
  `check_guard_trips` (`tools/check-spec-tokens.py:581`) to `tools/memory-tree/tree_lib.py`,
  `tools/loop/loop_lib.py` and `tools/lib/resolve_kit_dir.py` over the row's guard, and each trips.
  Observed by AC9.
- **S10** — id 3. The pass-commit probe of `TOOL-dDeclaredLoop-75` S10 and S22, built per S26, also runs
  at the pass commit of each later unit that edits a loop file, the leg running that file: 68
  `loop computed witness`, 69 and 78 `loop guard fixtures`, 70 `loop transition tables`, 71
  `loop breakpoints fixtures`, 72 and 76 `loop budget fixtures` and `loop breakpoints fixtures`, 74 and 77
  `loop position fixtures`. Each exit is recorded in this unit's acceptance ledger. Observed by AC10.
- **S11** — id 9. Every held leg of `tools/gate-legs.json` whose name opens `loop ` carries a row in
  `tools/run-gates/selftest-budgets.txt`, `loop breakpoints fixtures` (71 S1), `loop definition fixtures`
  and `loop selftest` (`TOOL-dDeclaredLoop-67` S30) among them, in the file's row shape and its header's
  calibration, measured at this pass. None owes a `tools/run-gates/windows-only-legs.txt` row: no arm of
  the three exercises a subject only Windows has. Observed by AC11.
- **S12** — id 10. 68 S1's roots reach `write_normaliser` in forward-slash form, from `Path.as_posix()` or
  `git rev-parse --show-toplevel`, never `str()` of a Windows path. Observed by AC12.
- **S13** — id 5. The run-gates README's leg-row key list is one line opening `Leg-row keys:` that names
  every key a row of `tools/gate-legs.json` carries, `stage` among them; this pass writes it where 75
  S29's pass left another spelling, so the key list is a line a probe can pin. Observed by AC13.
- **S14** — id 13. `tools/loop/commit_trailers.py`, a member of the `commit_trailers_py` parity row
  `TOOL-dDeclaredLoop-3` adds it to, is refreshed with 75 S23's three copies after 67 S15 and S52 move the
  canonical. Observed by AC14.
- **S15** — id 14. `TOOL-dDeclaredLoop-73`'s reverse vintage case reaches the requires check: its fixture
  reuses the target AC1 left at A, checks out B and runs read-only `update --to A`, which asks for the
  vintage already installed, and asserts exit 0 with the plan printed and the receipt's `gov_commit` equal
  to A, so the run is past `demand_forward_vintage` and `demand_published_vintage`
  (`tools/govkit/govkit.py:9231-9232`). Observed by AC15.
- **S16** — id 20. 75 AC24's BACKLOG half is observed by a token only the new ask row carries: one line of
  `memory/builds/aSurfacedLexicon/BACKLOG.md` names both `TOOL-aSurfacedLexicon-17` and
  `TOOL-dDeclaredLoop-66`; where 75's pass wrote the row without both ids on one line, this pass completes
  that row. Observed by AC16.
- **S17** — id 21. After 75 S25's sentence, the render `memory/guides/UNATTENDED-PROTOCOL.md` stays at or
  under its 66860-byte row (`tools/template-size-limits.txt:143`, pinned with no headroom): this pass trims
  `tools/unattended/PROTOCOL.template.md` by at least the bytes that sentence added beyond what 56 S25's
  trim left free, and regenerates the render. §7 names `unattended protocol size`. Observed by AC17.
- **S18** — id 22. After 71's leg lands and S8 widens its guard, the spec-token join is run over a scratch
  copy of the tree, and every non-terminal spec whose Files touched trips `loop breakpoints fixtures`
  carries that leg on its §7 leg line, amended as a rev bump with its §9 line. The population is the
  join's own output at this pass, this unit included. Observed by AC18.
- **S19** — id 24. `cmd_update`'s gained-prune loop (`tools/govkit/govkit.py:9247-9259`) grades
  `derive_unsatisfied_requires` over the same `requires` at `to_commit` that 73 S2's refusal reads,
  computed once by 73 S1's `read_requires_at` and passed to both callers. A gained kit whose `requires` is
  unknown at `to_commit` is left out with a line naming it, never pulled in. 73 §3's "every other use
  unchanged" holds for every use but this caller. Observed by AC19.
- **S20** — id 35. `TOOL-dDeclaredLoop-72` S2's refusal is restated to its own pseudo-code:
  `resolve_memory_root` refuses where `.memory-tree.conf` declares a root that differs from the driver's
  effective root, whether `.unattended.conf` sets it or leaves the default. Both sides are compared after
  normalising: a leading `./` and every trailing `/` stripped, separators written `/`. So `memory` and
  `memory/` agree. Observed by AC20.
- **S21** — id 36. Two https rows join `TOOL-dDeclaredLoop-77`'s `url-forms` table:
  `https://user:tok@host.example/r.git` and `https://user@host.example/r/`, each equal to the written
  `https://host.example/r` through `normalise_fetch_url`. Observed by AC21.
- **S22** — id 7. The merge grade's cost is stated where the code is: `check_push_range`'s docstring in
  `tools/loop/guard.py` says one `merge-tree` per two-parent merge whose policy blob differs from some
  parent's, with the per-merge time measured at this pass. Observed by AC22.
- **S23** — id 12. The pre-filter keeps the revert case: a merge is skipped before C only when M's policy
  blob equals every parent's, an absent file counting as a value (`TOOL-dDeclaredLoop-78` S1), since C
  then equals it too; otherwise C is computed. 59 S1's `--cc --name-only` list is not consulted on the
  computable branch. Observed by AC23.
- **S24** — id 6. 73 §3's hands-off bullet to 75 is reworded to the fix's text: the vintage-correct
  refusal, whose wider population 75 S26 and F3 accept and state, whose route names every unmet pair, and
  which 75 observes on the write path (ids 11, 36, 40). The edit is a rev bump of 73 with its §9 line.
  Observed by AC24.
- **S25** — id 15. `resolve_memory_root` reads `.memory-tree.conf` as `parse_conf(text, {})`, the
  signature `tools/memory-tree/tree_lib.py:135` defines, an absent file read as empty text, and its
  docstring cites the driver's conf path at `tools/unattended/unattended.sh:548`. Observed by AC25.
- **S26** — id 18. The pass-commit probe is built on the run-gates kit's code, never a raw worktree and a
  typed argv: `add_scratch_worktree` (`tools/run-gates/lib-attribute.sh:59`) makes the detached worktree,
  and `derive_leg_argv` (`tools/run-gates/measure_legs.py:503`) resolves the leg's argv at that commit,
  `{prefix}` through `resolve_prefix_token` (:104). It serves 75 S10 and S22 and S10 here. Observed by AC26.
- **S27** — id 26. `tools/loop/kit.toml`'s `[[gate_leg]]` rows for `loop definition fixtures` and
  `loop selftest` carry the same `guard` lists 75 S21 writes into `tools/gate-legs.json`. Observed by AC27.
- **S28** — id 28. 75 AC24's BACKLOG half is re-observed as a count: the lines of
  `memory/builds/aSurfacedLexicon/BACKLOG.md` naming `TOOL-aSurfacedLexicon-17` number one more than at
  base `ed497191`, where they number 1. Observed by AC28.

## 3. Non-goals (OUT)

- The three highs' mechanisms: units 76, 77 and 78, each its own unit.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- The refuted findings 19, 25, 27, 29 and 31.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-68` — `run_witness_commands`' normaliser route and named refusal in `tools/loop/loop_witness.py`, and the loop kit's descriptor claim (ids 4, 10, 11, 23, 30)
- **consumes-from** `TOOL-dDeclaredLoop-69` — the merge key grade's pre-filter and stated cost in `tools/loop/guard.py` (ids 7, 12), and the `loop guard fixtures` leg its pass keeps green (id 3)
- **consumes-from** `TOOL-dDeclaredLoop-70` — `read_driver_conf` in `tools/loop/loop_lib.py`, whose subshell this unit isolates from the caller's environment (ids 2, 16, 32)
- **consumes-from** `TOOL-dDeclaredLoop-71` — the `loop breakpoints fixtures` leg, its guard and its meta rows (ids 9, 17, 22, 34)
- **consumes-from** `TOOL-dDeclaredLoop-72` — `resolve_memory_root`'s refusal and its `.memory-tree.conf` read (ids 15, 35)
- **consumes-from** `TOOL-dDeclaredLoop-73` — `read_requires_at`, the reverse-vintage fixture and its hands-off bullet's wording (ids 6, 14, 24)
- **consumes-from** `TOOL-dDeclaredLoop-75` — the pass-commit probe, S21's guards, S23's copies, S24's ask row, S25's protocol sentence and S29's key list (ids 3, 5, 9, 13, 18, 20, 21, 26, 28)
- **consumes-from** `TOOL-dDeclaredLoop-77` — `normalise_fetch_url` and its `url-forms` plant (id 36)
- **consumes-from** `TOOL-dDeclaredLoop-78` — the `absent` state, which the pre-filter counts as a value (ids 7, 12)
- **consumes-from** `TOOL-dDeclaredLoop-80` — the fixture boundary, inside which the `trailing-slash-agree`, `unset-driver-root` and `no-confs` plants write their confs (the round-5 spec audit's id 20)
- **hands-off** `TOOL-dDeclaredLoop-82` — S10's probe, S17's trim, S18's population, the `sed-fails` plant and AC11, which that unit re-observes with an absent-leg line, bounds by the parsed anchors, widens to `loop selftest`, sets inside the bash and observes through the checker (the round-5 spec audit's ids 5, 6, 13, 19, 22, 24)
- **hands-off** `TOOL-dDeclaredLoop-86` — S10's probe and AC10, which that unit re-observes at 80's pass commit for the `no-own-conf-read` plant (the round-6 spec audit's id 17)
- **hands-off** `TOOL-dDeclaredLoop-88` — AC10, whose re-observation at 80's pass commit that unit reads, amending it where it is absent (the round-7 spec audit's id 9)
- **hands-off** `TOOL-dDeclaredLoop-95` — S25 and AC25, the `parse_conf(text, {})` signature and the absent-file rule that unit's `read_tree_conf` keeps and re-runs (the round-11 spec audit's id 1)

## 4. Design

### Write set

This pass writes the tools below. Outside this build's folder it writes one ask row in
`memory/builds/aSurfacedLexicon/BACKLOG.md` where S16 completes 75's, and the protocol render S17
regenerates. Inside it, S18 and S24 amend sibling specs' §3 and §7 lines. S5, S9, S10 and S26 observe or
record and write no code.

### The driver-conf subshell (S1, S2)

```
read_driver_conf(tree, names):
    run [bash, "-c", 'for n in "${@:3}"; do unset "$n"; done
                      ROOT="$1"; CONF="$2"
                      . "$CONF" >/dev/null 2>&1 || exit 9
                      for n in "${@:3}"; do eval "v=\${$n-__UNSET__}"; printf "%s\0%s\0" "$n" "$v"; done
                      printf "__CONF_IMPORT_OK__\0\0"', "_", top_level(tree), conf, *names]
```

### The normaliser's apply step (S6, S7, S12)

```
run [bash, "-c", '. "$1"; write_normaliser "$2" "$3" "$4" && sed -E -f "$2" < "$5"',
     "_", kit/lib-attribute.sh, prog, Path(wt).as_posix(), Path(repo).as_posix(), raw]
    start failure or rc != 0 -> refuse "witness: normaliser unavailable — sed: <reason>", no hash
```

### Evidence

- The driver assigns `MEMORY_ROOT=memory` and `PHASES_EXTRA=""` on its init lines
  (`tools/unattended/unattended.sh:560-561`) after `ROOT` and `CONF` (:546, :548) and before `. "$CONF"`
  (:617): read at base `ed497191`.
- `run-selftests.sh --check` prints every leg with subject `kit` or chunk `selftests` that has no row in
  `tools/run-gates/selftest-budgets.txt` (`tools/run-gates/run-selftests.sh:826-835`), run as the leg
  `every held leg is budgeted, every budget row resolves` (`tools/gate-legs.json:1767`).
- `{prefix}/lib/` is carried by 36 legs and `{prefix}/memory-tree/` by 13, both over `BROAD_LEG_FLOOR = 5`
  (`tools/check-spec-tokens.py:331`), so S8's guard adds no join hit; `{prefix}/loop/` is carried by none
  at base, so S18's population is every non-terminal spec declaring a `tools/loop/` path: counted
  2026-10-24 by reading `tools/gate-legs.json`, DERIVED by that read.
- `memory/guides/UNATTENDED-PROTOCOL.md` measures 66859 bytes CR-stripped against the 66860 row
  (`tools/template-size-limits.txt:143`): PINNED 2026-10-24, re-derived by `tr -d '\r' < <file> | wc -c`.
- `cmd_update` calls `demand_forward_vintage` and `demand_published_vintage` on every run
  (`tools/govkit/govkit.py:9231-9232`) and grades the gained prune over the working-tree `descs` (:9164,
  :9247-9259).
- At base `memory/builds/aSurfacedLexicon/BACKLOG.md` holds one line naming `TOOL-aSurfacedLexicon-17`:
  PINNED, re-derived by `git show ed497191:<file> | grep -c TOOL-aSurfacedLexicon-17`.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/loop_table.py`
- `tools/loop/loop_witness.py`
- `tools/loop/budget.py`
- `tools/loop/guard.py`
- `tools/loop/position.py`
- `tools/loop/commit_trailers.py`
- `tools/loop/kit.toml`
- `tools/gate-legs.json`
- `tools/run-gates/selftest-budgets.txt`
- `tools/run-gates/README.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/builds/aSurfacedLexicon/BACKLOG.md`
- `memory/builds/dDeclaredLoop/spec/`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, govkit and loop.** The halves are not disjoint by M6 clause 2: S4's probe imports
  `tools/govkit/govkit.py`, which S19 writes, as an acceptance input, and S18's join reads every spec,
  73's included, which S24 writes.
- **Waiver rows for S18's hits.** `memory/project/spec-token-waivers.txt` is shrink-only by its header, so
  a new row reds; the leg on the spec's own line is the declaration the join asks for.

## 5. Production-readiness checklist

- security — S1 and S2 keep a stray export from choosing the records root or the phase set; S7 refuses
  rather than hashing a partial normalisation.
- perf / scale — S10 and S26 cost one scratch worktree and one leg run per named unit, minutes in total,
  once at this pass; S23 runs `merge-tree` for fewer merges than 69 does.
- error / empty / loading states — S7, S19 and S20 each name the failed, unknown or disagreeing case.
- observability — S7's refusal names the reason; S19's line names the kit left out and why.
- risks — S17 trims protocol prose, as 56 S25 does for units 14 and 19; S18 amends sibling specs' leg
  lines, each with its §9 line.
- testing — AC1 to AC28 as plants, probes and greps; the arms under §7, observed at the close.
- migration — none: every reader is unbuilt at base.
- user docs — S17 keeps 75 S25's protocol sentence and trims elsewhere in the same guide.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe calls `read_driver_conf(tree, ["MEMORY_ROOT"])` with `MEMORY_ROOT=elsewhere`
  exported over a `.unattended.conf` that does not set it, the mapping has no `MEMORY_ROOT` key.
  Red when: the subshell inherits the export and answers `elsewhere`.
- **AC2** — When the same probe reads a conf holding `MEMORY_ROOT="${ROOT##*/}-records"`, it answers the
  scratch tree's directory name followed by `-records`.
  Red when: `ROOT` is unset in the subshell and the answer is `-records`.
- **AC3** — When `python loop_table.py --fixture --plant env-leak` runs, `resolve_memory_root` answers
  `memory` and the adopter population is empty.
  Red when: an exported `PHASES_EXTRA` admits `BOGUS` or an exported root wins.
- **AC4** — When `grep -n "run-gates" kit.toml` runs in `tools/loop/`, it prints the `requires` line, and a
  probe calling `derive_unsatisfied_requires(["loop"], descs, {"kits": []})` lists `('loop', 'run-gates')`.
  Red when: the edge is absent and a selection with `loop` alone installs cleanly.
- **AC5** — When a probe lists the first argument of every `resolve_kit_dir(` call under `tools/loop/` and
  every kit in the `requires` and `requires_if` of the loop kit's `kit.toml`, the first set less the second
  is empty.
  Red when: the loop kit resolves a kit its descriptor does not name.
- **AC6** — When `git grep -n '\["sed"' -- tools/loop/` runs, it prints nothing, and
  `grep -c "sed -E -f" loop_witness.py` in `tools/loop/` prints at least 1.
  Red when: a bare `sed` is spawned from Python.
- **AC7** — When `python loop_witness.py --fixture --plant sed-fails` runs the apply step with a `sed` stub
  exiting 2 first on the bash's PATH, the re-run exits non-zero printing `witness: normaliser unavailable — sed:`
  and writes no hash.
  Red when: the stub's empty output is hashed.
- **AC8** — When a probe prints the `guard` of the `loop breakpoints fixtures` row in `tools/gate-legs.json`
  and in the loop kit's `kit.toml`, both are `{prefix}/loop/`, `{prefix}/memory-tree/` and `{prefix}/lib/`.
  Red when: either keeps the three loop files alone.
- **AC9** — When a probe loads `tools/check-spec-tokens.py` by `importlib` and calls `check_guard_trips` for
  `tools/memory-tree/tree_lib.py`, the loop kit's `loop_lib.py` and `tools/lib/resolve_kit_dir.py` against
  each entry of that guard with `{prefix}` read as `tools`, each path trips one entry.
  Red when: a file the module reaches selects no guard entry.
- **AC10** — When the pass-commit probe, `add_scratch_worktree` at that unit's pass commit and the leg's
  argv from `derive_leg_argv`, runs each S10 unit's leg, every exit is recorded in this unit's acceptance
  ledger and every one is 0.
  Red when: a pass broke the sibling-minted leg covering its own file and only a prose sentence was read.
  cost: one scratch worktree per unit, minutes in total.
- **AC11** — When a probe lists the legs of `tools/gate-legs.json` whose name opens `loop ` and whose subject
  is `kit` or chunk `selftests`, less the first fields of `tools/run-gates/selftest-budgets.txt`, it prints
  nothing, and `grep -c "loop breakpoints fixtures" tools/run-gates/selftest-budgets.txt` prints 1.
  Red when: a held loop leg has no budget row.
- **AC12** — When `python loop_witness.py --fixture --plant two-worktree-roots` hashes a command printing its
  worktree path in two worktrees whose roots arrive as `pathlib.Path` objects, the two hashes are equal.
  Red when: a backslash root reaches `write_normaliser` and the forward-slash spelling passes through.
- **AC13** — When `grep -c "^Leg-row keys:" tools/run-gates/README.md` runs it prints 1, and a probe taking
  every key of every row of `tools/gate-legs.json` less the backticked words on that line prints nothing.
  Red when: no single key-list line exists, or it omits `stage` or another key the manifest carries.
- **AC14** — When a probe lists the files `git grep -l "^# >>> commit_trailers_py" -- tools` names and
  compares each block, CR-stripped, with the canonical's, the loop kit's `commit_trailers.py` is among them and
  every block is equal.
  Red when: the loop copy is stale, or the population is a typed count.
- **AC15** — When the probe of `TOOL-dDeclaredLoop-73` AC1, over the target it left at A, checks out B and
  runs `python tools/govkit/govkit.py update --to A` read-only, with no `--write`, it exits 0, prints its
  plan, and the receipt's `gov_commit` equals A.
  Red when: a vintage refusal ends the run before the requires check and the probe still reads it as a pass.
- **AC16** — When `grep -cE "TOOL-aSurfacedLexicon-17.*TOOL-dDeclaredLoop-66|TOOL-dDeclaredLoop-66.*TOOL-aSurfacedLexicon-17"`
  runs over `memory/builds/aSurfacedLexicon/BACKLOG.md`, it prints 1.
  Red when: only the 2026-09-05 filing line names the ask.
- **AC17** — When `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` runs after the
  render, it exits 0, and `grep -c "adopter phase" memory/guides/UNATTENDED-PROTOCOL.md` prints at least 1.
  Red when: the render is over its row, or the trim took 75's sentence.
- **AC18** — When `python tools/check-spec-tokens.py` runs in a scratch copy of the tree after this pass,
  it prints no `loop breakpoints fixtures <-` hit.
  Red when: a non-terminal spec declaring a loop path lacks the leg on its leg line.
- **AC19** — When the same probe runs `python tools/govkit/govkit.py update --to B` read-only where a
  gained kit's edge is met in the working tree at A and unmet at B, it prints `default-gained <kit> NOT installed`
  and raises no `Refusal`; with the vintages swapped, the kit is listed `would gain`.
  Red when: the prune grades the working tree and the refusal then fails the whole update.
- **AC20** — When `python budget.py --fixture --plant trailing-slash-agree` reads confs naming `memory/` and
  `memory`, it reads without refusal, and `--plant unset-driver-root` exits non-zero printing `records root:`.
  Red when: a raw string compare refuses an agreeing pair, or the defaulted root escapes the refusal.
- **AC21** — When `python position.py --fixture --plant url-forms` runs, both https rows read equal to
  `https://host.example/r`.
  Red when: a scheme URL keeps its user part.
- **AC22** — When `python -c` prints `check_push_range.__doc__` from the loop kit's `guard.py`, it names
  `merge-tree per two-parent merge` and a measured time in ms.
  Red when: the docstring keeps 69 §5's "unchanged" cost.
- **AC23** — When `python guard.py --fixture --plant push-merge-equal-to-every-parent` runs, it prints
  `merge-tree runs: 0` and exits 0, and `--plant push-merge-revert-to-unchanged-side` still exits 1.
  Red when: the pre-filter skips the revert case, or computes C where every blob is equal.
- **AC24** — When `grep -c "to the edges an update introduces"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-73.md`, it prints 0, and
  `grep -c "wider population"` over the same file prints at least 1.
  Red when: the bullet still promises a scoping 75 rejected.
- **AC25** — When `grep -n "parse_conf(" loop_lib.py` runs in `tools/loop/`, every call passes text and a
  dict, and `python budget.py --fixture --plant no-confs` answers `memory` with no traceback.
  Red when: the call passes a path, or an absent file raises.
- **AC26** — When this unit's acceptance ledger is read, each pass-commit probe exit line names
  `add_scratch_worktree` and `derive_leg_argv` as its route.
  Red when: an exit was taken from a raw `git worktree add` and a typed argv with `{prefix}` unresolved.
- **AC27** — When a probe compares the `guard` of the `loop definition fixtures` and `loop selftest` rows of
  the loop kit's `kit.toml` with the same rows of `tools/gate-legs.json`, each pair is equal.
  Red when: the descriptor row carries no guard, so adopters run the legs unguarded.
- **AC28** — When `grep -c "TOOL-aSurfacedLexicon-17" memory/builds/aSurfacedLexicon/BACKLOG.md` runs, it
  prints 2.
  Red when: the new ask row is absent and the count stays at the base's 1.
  figure: the base count 1 is PINNED at `ed497191`, re-derived by `git show`.

## 7. Gates

`measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended protocol size` · `every held leg is budgeted, every budget row resolves` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures`, `loop breakpoints fixtures`, `loop position fixtures`, the leg
`loop guard fixtures`, the leg `loop transition tables` and the leg `loop computed witness`, none of them
a leg at HEAD.

New arm: tools/loop/loop_table.py · covers AC3 · the env-leak plant under exported MEMORY_ROOT and PHASES_EXTRA · none
New arm: tools/loop/loop_witness.py · covers AC7 AC12 · the sed-fails and two-worktree-roots plants, staged against a bare sed and a str() root · none
New arm: tools/loop/budget.py · covers AC20 AC25 · the trailing-slash-agree, unset-driver-root and no-confs plants · none
New arm: tools/loop/guard.py · covers AC23 · the equal-to-every-parent plant beside 69's revert plant · none
New arm: tools/loop/position.py · covers AC21 · the two https rows of the url-forms table · none
New arm: tools/govkit/selftest.py · covers AC15 AC19 · the reverse-vintage and gained-prune-vintage cases · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Isolate the driver-conf subshell by unsetting the names, presetting the driver's defaults, or
  reading only names the conf declares (ids 2, 16)?** (a) unset each requested name, the callers holding
  the defaults; (b) preset each from the driver's init lines, which needs the unattended kit resolved and
  its init block parsed; (c) import only declared names, as `check-unattended.sh:297` does. (b) adds a
  kit dependency the loop kit carries only as `requires_if`; (c) still inherits for a name the conf
  appends to. (a) satisfies AC1 to AC3 with no new dependency. RESOLVED (agent, 2026-10-24, delegated):
  (a), S1. widens: none · relaxes: none
- **F3 — Fund 75 S25's protocol bytes by a trim or a raise of the row (id 21)?** (a) trim
  `tools/unattended/PROTOCOL.template.md`; (b) raise the 66860 row. The row file lets a run raise only in
  the commit of the unit whose own change crosses it (`tools/template-size-limits.txt`, condition 1), and
  the crossing change is 75's, so (b) is the owner's from this unit. (a) is the route 56 S25 takes for
  units 14 and 19. RESOLVED (agent, 2026-10-24, delegated): (a), S17. widens: none · relaxes: none
- **F4 — Clear S18's join hits by amending sibling leg lines or by waiver rows (id 22)?** (a) the leg on
  each tripped spec's line; (b) dated rows in `memory/project/spec-token-waivers.txt`. The waiver file is
  shrink-only, so (b) reds on arrival. RESOLVED (agent, 2026-10-24, delegated): (a), S18.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-4 spec audit's 28 minors batched (21 MEDIUM, 7 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-80 and TOOL-dDeclaredLoop-82, written by the round-5 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-86, written by the round-6 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-95, written by the round-11 spec audit's disposal; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy: 70's `read_driver_conf` (S1 to S3),
68's run-gates normaliser run in place (S6, S7, S12), the manifest row and its descriptor twin (S8, S11,
S27), `check_guard_trips` (S9), 73's `read_requires_at` passed to a second caller (S19), 72's
`resolve_memory_root` (S20, S25), 77's `normalise_fetch_url` (S21), 78's states (S23) and the run-gates
kit's `add_scratch_worktree` and `derive_leg_argv` (S26).
`python tools/codebase-map/reuse_lookup.py "strip the user part from a remote url before comparing"` and
`"find calls that read a config file by walking a module's syntax tree"` ranked `resolve_remote`,
`read`, `read_text`, `walk` and `read_conf`, read above and not fit; the memory-recall query on the
driver-conf reader returned this build's own records and spec 70, so no new reader is minted where one
of these exists.

Recall terms used: read_driver_conf MEMORY_ROOT unattended.conf sourced subshell inherited environment driver default two-readers conf
