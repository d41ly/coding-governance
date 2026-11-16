# TOOL-dDeclaredLoop-79 — the round-4 spec audit's 28 minors, batched

**Status:** DEFERRED · rev-6 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 40 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 |
| [2026-10-24-build-TOOL-dDeclaredLoop-79-deviation-791.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-79-deviation-791.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-79-deviation-792.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-79-deviation-792.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-79-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-79-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-79-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-79-reground-brief.md) | research | — |
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

Rev-6 re-grounds the batch on branch `unattended-declared-loop-d56bf0` at `8b06bb0a4`, built through
order 35, and on the committed specs of orders 36 to 39. Many minors were closed by a built unit or by a
committed sibling spec; those leave this unit's scope, each in §3 with what closed it, and one is
refused there because the spec it amends is CLOSED. The items left open stay here under their rev-5
labels, which sibling specs cite.

| Report item | Severity | Report ids | Rev-5 scope items | At rev-6 |
|---|---|---|---|---|
| M1 | MEDIUM | 2, 16, 32 | S1, S2, S3 | S1, S2, S3 |
| M2 | MEDIUM | 4, 23 | S4, S5 | S4; S5 in §3 |
| M3 | MEDIUM | 11, 30 | S6, S7 | S7; S6 in §3 |
| M4 | MEDIUM | 17, 34 | S8, S9 | §3 |
| M5 | MEDIUM | 3 | S10 | S10 |
| M6 | MEDIUM | 9 | S11 | §3 |
| M7 | MEDIUM | 10 | S12 | §3 |
| M8 | MEDIUM | 5 | S13 | S13 |
| M9 | MEDIUM | 13 | S14 | §3 |
| M10 | MEDIUM | 14 | S15 | §3 |
| M11 | MEDIUM | 20 | S16 | §3 |
| M12 | MEDIUM | 21 | S17 | §3 |
| M13 | MEDIUM | 22 | S18 | §3 |
| M14 | MEDIUM | 24 | S19 | S19 |
| M15 | MEDIUM | 35 | S20 | S20, by §8 F6 |
| M16 | MEDIUM | 36 | S21 | S21 |
| L1 | LOW | 7, 12 | S22, S23 | S22, S23 |
| L2 | LOW | 6 | S24 | §3, refused |
| L3 | LOW | 15 | S25 | S25 |
| L4 | LOW | 18 | S26 | §3 |
| L5 | LOW | 26 | S27 | §3 |
| L6 | LOW | 28 | S28 | §3 |

The report's 21 MEDIUM and 7 LOW findings by raw id are its own counts, PINNED from its appendix. Its
five refuted findings, ids 19, 25, 27, 29 and 31, are not in the disposal population.

## 2. Scope (IN)

The labels keep their rev-5 numbers, which sibling specs cite; every other rev-5 item is in §3.

- **S1** — id 2. `read_driver_conf` (`TOOL-dDeclaredLoop-70` S1, in `tools/loop/loop_lib.py`) unsets each
  requested name in its subshell before it sources the conf, so a value the caller's environment
  exports never reads as the conf's. A name the conf leaves unset answers unset, and the caller's driver
  default applies: 72's `memory` and 70 S3's empty population. Observed by AC1, AC3.
- **S2** — id 16. The same subshell sets `ROOT` to the work tree's top, in forward-slash form from
  `Path.as_posix()`, and `CONF` to `$ROOT/.unattended.conf`, before it sources the conf, as
  `tools/unattended/unattended.sh#load_driver_conf` sets both before its own source. A conf composing a
  value from `$ROOT` or `$CONF` reads as the driver reads it. Observed by AC2.
- **S3** — id 32. The selftest of `tools/loop/loop_table.py` gains the scratch tree `leak` among 70 §4
  "The arms" trees: its `.unattended.conf` holds one comment line and sets neither name, and its case runs
  with `MEMORY_ROOT=elsewhere` and `PHASES_EXTRA=BOGUS` set in the process environment, restored after
  (§4 "The leak tree", §8 F7). Observed by AC3.
- **S4** — id 23. `tools/loop/kit.toml`'s `requires` gains `run-gates` beside `memory-tree`, since
  `TOOL-dDeclaredLoop-68` S1 resolves that kit's `lib-attribute.sh` on every witness re-run. The comment
  above it says why, and the "Who owns it" section of `help/loop.md` says the loop kit requires the
  run-gates kit and why. run-gates declares `requires = []`, so no cycle forms. The receipt that
  `TOOL-dDeclaredLoop-57`'s arms in `tools/govkit/selftest.py#check_roles_default` write claims
  `run-gates` too, so those arms still grade the pair they name (§4 "The edge"). Observed by AC4.
- **S7** — id 30. The plant `sed-fails` joins `PLANTS` of `tools/loop/loop_witness.py` and its
  `--selftest` run, observing the `sed:` branch of 68 S3's refusal: the re-run's apply step exits
  non-zero, and the re-run refuses with no hash (§4 "The sed-fails plant", §8 F5). `help/loop.md` and
  `tools/loop/README.md` name it where they name 68's two plants. Observed by AC7.
- **S10** — id 3. The pass-commit probe of `TOOL-dDeclaredLoop-75` §4 "The pass-commit probe" runs, at
  the pass commit of each of units 68, 69, 70, 72, 74, 76, 77 and 78, every leg §4 "The probe's legs"
  derives for that commit, and each exit is recorded in this unit's acceptance ledger. Observed by AC10.
- **S13** — id 5. `tools/run-gates/README.md` carries one line opening `Leg-row keys:` that names, each
  in backticks, every key a row of `tools/gate-legs.json` carries, `stage` among them, under its section
  "The leg manifest is the kit dir's SIBLING". Observed by AC13.
- **S19** — id 24. In `tools/govkit/govkit.py#_cmd_update` the gained-prune loop grades the same
  `requires` at `to_commit` that 73's refusal grades: one call of `read_requires_at` over the claimed
  and the gained kits, made before the loop, feeds both the loop and `demand_claimed_requires`. A gained
  kit whose `requires` that vintage cannot answer is left out with a line naming it and why, never
  pulled in; a claimed kit's unknown `requires` refuses as `TOOL-dDeclaredLoop-73` S4 refuses it. The
  arm `check_gained_prune_vintage(tmp)` in `tools/govkit/selftest.py` observes it (§4 "The gained
  prune"). Observed by AC19.
- **S20** — id 35. 72's refusal is observed on an agreeing pair spelled apart: the plant
  `trailing-slash-agree` joins `PLANTS` of `tools/loop/budget.py`, `.unattended.conf` naming `memory/`
  and `.memory-tree.conf` naming `memory`, and a draw there reads no refusal (§8 F6). Observed by AC20.
- **S21** — id 36. Two https rows join `TOOL-dDeclaredLoop-77`'s `url-forms` table in
  `tools/loop/position.py`, `https://user:tok@host.example/r.git` and `https://user@host.example/r/`,
  each owed equal to the written `https://host.example/r` through `derive_fetch_url`. Observed by AC21.
- **S22** — id 7. The docstring of `tools/loop/guard.py#check_push_range` states the merge grade's cost:
  one `git merge-tree --write-tree` per two-parent merge whose policy blob differs from some parent's,
  with the per-merge time the pass measures, PINNED with its date and node. Observed by AC22.
- **S23** — id 12. `check_push_range` skips a merge before any re-merge only where its policy blob equals
  every parent's blob, an absent file counting as a value as `TOOL-dDeclaredLoop-78` S1 counts it, since
  git's clean re-merge then equals it too; every other merge reads `read_remerge_policy` as at the tip.
  The plant `push-merge-equal-to-every-parent` joins `PLANTS` of `tools/loop/guard.py`. Observed by
  AC23.
- **S25** — id 15. The absent-file half of 72's read is observed: the plant `no-confs` joins `PLANTS` of
  `tools/loop/budget.py`, a scratch holding neither conf, where `resolve_memory_root` answers `memory`
  with no traceback. Observed by AC25.

## 3. Non-goals (OUT)

- The three highs' mechanisms: units 76, 77 and 78, each its own unit.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- The refuted findings 19, 25, 27, 29 and 31.
- A preset of each driver default inside the subshell, and an import restricted to the names the conf
  declares: §8 F2 keeps the unset.
- A `./` prefix or a backslash in a `MEMORY_ROOT` value: 72's normalisation is the one rule (§8 F6).

### The rev-5 items the built code or a committed spec settles

Read on branch `unattended-declared-loop-d56bf0` at `8b06bb0a4`.

| Item | What settles it |
|---|---|
| S5 | `TOOL-dDeclaredLoop-68` rev-3 §3 retracts the §5 claim id 4 found false, so no claim is left to make true. Its universal form is false by design: the roles and unattended kits require the loop kit, so an edge back would cycle, and `tools/loop/kit.toml`'s comment records each reach that takes no edge and degrades to `unarmed` by name. |
| S6 | 68 rev-3 S1 and its §8 F3 (b) apply the program inside the bash `resolve_bash` answers, and its AC2 observes that no Python argv under `tools/loop/` names `sed`. |
| S8, S9 | The leg is `loop breakpoint fixtures`, built by `TOOL-dDeclaredLoop-19` with no `guard` key, so every bar runs it and an edit to the memory-tree kit selects it (71 rev-4 §8 F3). Every loop leg of `tools/gate-legs.json` carries no `guard`, and `TOOL-dDeclaredLoop-55` S1 and 67 rev-4 S31 hold that shape for `loop termination`. |
| S11 | `loop breakpoint fixtures` has its row in `tools/run-gates/selftest-budgets.txt`, and the held-leg predicate of `tools/run-gates/run-selftests.sh`, extracted and run over the tip, prints no leg. `TOOL-dDeclaredLoop-67` rev-4 S30 writes the row of the one loop leg it adds, `loop definition fixtures`; no `loop selftest` leg is added (75 rev-10 §3, its S21). |
| S12 | 68 rev-3 S1 hands every root to `write_normaliser` from `Path.as_posix()`, and its AC1 re-runs one command in two worktrees whose roots it builds from `Path` objects. |
| S14 | `TOOL-dDeclaredLoop-3` §8 F8 (a) reads the trailer reader through the memory-tree kit's copy, so `tools/loop/` holds no `commit_trailers.py`; the parity row's members are the canonical and two copies, and 67 rev-4 S39 re-copies both in its pass. |
| S15 | `tools/govkit/selftest.py#check_requires_vintage`, built by `TOOL-dDeclaredLoop-73`, runs `update --to A` from B's checkout over the target its AC1 left at A and asserts exit 0, a run past both vintage checks and the requires check, since any `Refusal` exits 2. |
| S16, S28 | `TOOL-dDeclaredLoop-75` rev-10 S24 writes the ask row naming `TOOL-aSurfacedLexicon-17` and `TOOL-dDeclaredLoop-66` on one line, and its AC24 reads that row, which the base's one filing line cannot satisfy. |
| S17 | 75 rev-10 S25 and §8 F6 fund its sentence by raising the render's row in its own commit, the commit whose change crosses it, and AC25 reads the render against the raised row (§8 F3). |
| S18 | No leg of `tools/gate-legs.json` carries a loop path in its `guard`, so the spec-token checker's guard join names no loop leg against any spec (§8 F4). |
| S26 | 75 rev-10 §4 "The pass-commit probe" builds the probe on `tools/run-gates/lib-attribute.sh#add_scratch_worktree` and `tools/run-gates/measure_legs.py#derive_leg_argv`; S10 runs that probe. |
| S27 | 67 rev-4 S30's `loop definition fixtures` is gov's own `[[exempt_leg]]` with no `guard` and no descriptor row, and no `loop selftest` leg is added. |

S24, id 6, is refused: it rewords a hands-off bullet in §3 of `TOOL-dDeclaredLoop-73`, which is CLOSED, and
a landed record is frozen. 75 rev-10 S26 states the wider population itself, which is what the reworded
bullet would have said.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-68` — `run_witness_commands`' normaliser route and its named refusal in `tools/loop/loop_witness.py`, whose `sed:` branch S7 plants, and the run-gates reach S4 declares (ids 4, 10, 11, 23, 30)
- **consumes-from** `TOOL-dDeclaredLoop-69` — the merge key grade in `tools/loop/guard.py`, which S22 prices and S23 pre-filters (ids 7, 12), and the `loop guard fixtures` leg S10 runs at its pass commit (id 3)
- **consumes-from** `TOOL-dDeclaredLoop-70` — `read_driver_conf` in `tools/loop/loop_lib.py`, whose subshell this unit isolates from the caller's environment, and the scratch-tree cases of the table selftest S3 extends (ids 2, 16, 32)
- **consumes-from** `TOOL-dDeclaredLoop-71` — the `loop breakpoint fixtures` leg as unit 19 built it, unguarded, which settles ids 9, 17, 22 and 34 (§3)
- **consumes-from** `TOOL-dDeclaredLoop-72` — `resolve_memory_root`'s refusal, its normalisation and its `.memory-tree.conf` read through `read_design_conf`, which S20 and S25 plant (ids 15, 35)
- **consumes-from** `TOOL-dDeclaredLoop-73` — `read_requires_at`, which S19 passes to the gained-prune loop, and the reverse-vintage arm that settles id 14; the bullet id 6 rewords stays frozen (ids 6, 14, 24)
- **consumes-from** `TOOL-dDeclaredLoop-75` — the pass-commit probe S10 runs, and the items of its rev-10 that settle ids 5, 9, 13, 18, 20, 21, 26 and 28 here; S13 writes the key list its S29 left to this unit (ids 3, 5, 9, 13, 18, 20, 21, 26, 28)
- **consumes-from** `TOOL-dDeclaredLoop-77` — `derive_fetch_url` and its `url-forms` plant, whose table S21 extends (id 36)
- **consumes-from** `TOOL-dDeclaredLoop-78` — the `absent` state, which S23's pre-filter counts as a value (ids 7, 12)
- **consumes-from** `TOOL-dDeclaredLoop-80` — the fixture boundary, inside which the `trailing-slash-agree` and `no-confs` plants write their confs (the round-5 spec audit's id 20)
- **hands-off** `TOOL-dDeclaredLoop-82` — S10's probe and the `sed-fails` plant, which that unit re-observes with an absent-leg line and hardens; S17, S18 and AC11 left this unit's scope at rev-6 (§3), so its ids 5, 19, 22 and 24 re-ground on what settled them (the round-5 spec audit's ids 5, 6, 13, 19, 22, 24)
- **hands-off** `TOOL-dDeclaredLoop-86` — S10's probe and AC10, which that unit re-observes at 80's pass commit for the `no-own-conf-read` plant (the round-6 spec audit's id 17)
- **hands-off** `TOOL-dDeclaredLoop-88` — AC10, whose re-observation at 80's pass commit that unit reads, amending it where it is absent (the round-7 spec audit's id 9)
- **hands-off** `TOOL-dDeclaredLoop-95` — S25 and AC25, the `no-confs` plant and its absent-file rule, which that unit's `read_tree_conf` keeps and re-runs (the round-11 spec audit's id 1)

## 4. Design

### Evidence

Every code claim was read on branch `unattended-declared-loop-d56bf0` at `8b06bb0a4`, through `git show`,
`git log` and a `git archive` copy in a scratch directory, because this worktree's main at `179486e8f`
lacks the loop kit. Units 68, 70, 72, 74, 75, 76, 77 and 80 are not built at that tip and are read on
their committed specs, rev-3, rev-3, rev-6, rev-3, rev-10, rev-6, rev-3 and rev-6. No line number is cited
but one blob-pinned range.

- `tools/unattended/unattended.sh#load_driver_conf` takes `ROOT` from `git rev-parse --show-toplevel`,
  moves there, sets `CONF` to `$ROOT/.unattended.conf`, assigns `MEMORY_ROOT=memory` and
  `PHASES_EXTRA=""` among its init lines, and then sources `"$CONF"`, so an inherited value never reaches
  it.
- 70 rev-3 §4 "The reader" holds the names in an array, sources the conf from the work tree's top as the
  working directory and reads each name back; nothing in it unsets a name or sets `ROOT` or `CONF`.
  `tools/loop/loop_witness.py#resolve_bash` tests the path it is given, `str(script)`, under each
  candidate bash.
- The unattended kit gate imports only the names the conf declares
  (`tools/unattended/check-unattended.sh@2a0e6616ca6f:484-491`), the shape §8 F2's option (c) names.
- `tools/loop/kit.toml` declares `requires = ["memory-tree"]`. The loop modules resolve the codebase-map,
  hooks, memory-tree, playbook, policy, roles, runlog and unattended kits through `resolve_kit_dir`, and
  none resolves run-gates at the tip; 68 S1 adds that reach. `tools/run-gates/kit.toml` declares
  `requires = []`; `tools/roles/kit.toml` and `tools/unattended/kit.toml` each require `loop`.
  `tools/govkit/registry.toml` holds `run-gates` in its default set.
- `tools/govkit/govkit.py#derive_unsatisfied_requires` grades each selected kit's `requires` against the
  selection and the receipt's claim; `tools/govkit/selftest.py#check_roles_default` calls it through
  `demand_claimed_requires` with the real descriptors and a hand-written claim of `kickoff-manifest`,
  `memory-tree` and `roles`, and its `[dDL-57] AC2 LIVENESS` and `AC4 LIVENESS` arms owe a gained `loop`
  with no refusal.
- `tools/govkit/govkit.py#_cmd_update` builds `descs` with `read_descriptors` from the working tree, runs
  the gained-prune `while` loop over `derive_unsatisfied_requires(gained, descs, receipt)`, then calls
  `read_requires_at(root, to_commit, list(claimed) + list(gained))`, raises on any unknown kit, and calls
  `demand_claimed_requires` with that answer. The docstring of
  `tools/govkit/selftest.py#check_requires_vintage` names the gained-prune loop's vintage as what it does
  not check.
- `tools/loop/guard.py#check_push_range` calls `read_remerge_policy` on every merge whose first parent
  holds the policy file, before any comparison of blobs, so a merge equal to every parent still runs
  `git merge-tree`; its docstring states no cost. The `push-merge-both-sides-clean` plant's
  `run_grade_in_process` stand-in counts the re-merges and prints `merge-tree runs: <n>`.
- `tools/loop/loop_table.py` carries `--fixture --plant`, whose `PLANTS` are breaks made in memory on the
  rows as read, never a scratch tree; 70 S5 adds the selftest's scratch-tree cases.
- `tools/run-gates/README.md` holds no line opening `Leg-row keys:`. The rows of `tools/gate-legs.json`
  carry the keys `argv`, `ceiling`, `chunk`, `doc_reads`, `enforces`, `guard`, `name`, `pack`,
  `pass_leg`, `reads`, `scope_of`, `signature`, `stage` and `subject`, 14 keys PINNED at `8b06bb0a4`,
  re-derived by AC13's probe.
- The loop legs of `tools/gate-legs.json` each run one module: `loop definition` runs `loop_lib.py`,
  `loop transition tables` runs `loop_table.py`, `loop parent routes` runs `loop_parents.py`,
  `loop computed witness` runs `loop_witness.py`, `loop guard fixtures` runs `guard.py`, `loop budget
  fixtures` runs `budget.py`, `loop breakpoint fixtures` runs `breakpoints.py`, `loop position fixtures`
  runs `position.py`, `loop transition record` runs `loop_transition.py` and `loop adapt fixtures` runs
  `adapt.py`.
- The pass commits of units 69 and 78 are `59982f60c` and `47c98c1a2`, each found by its `Pass:`
  trailer, and each changes `tools/loop/guard.py` alone under `tools/`.

### The driver-conf subshell (S1, S2)

70 rev-3's reader, its two lines before the source added and its `ROOT` passed:

```
run [bash, "-c", '__rdc_conf=$1; ROOT=$2; shift 2; __rdc_names=("$@")
                  for __rdc_n in "${__rdc_names[@]}"; do unset "$__rdc_n"; done
                  CONF="$ROOT/.unattended.conf"
                  . "$__rdc_conf" >/dev/null 2>&1 || exit 9
                  for n in "${__rdc_names[@]}"; do eval "v=\${$n-__UNSET__}"; printf "%s\0%s\0" "$n" "$v"; done
                  printf "__CONF_IMPORT_OK__\0\0"', "_", conf, Path(top).as_posix(), *names],
    cwd=top, the rest as 70 rev-3 runs it
```

The names are unset before `ROOT` and `CONF` are set, so a request for either reads the conf's value
over the driver's. The source keeps 70's `conf` argument, the path `resolve_bash` tested.

### The leak tree (S3)

70 §4 "The arms" builds its trees before the selftest's cases. The tree `leak` joins them, its
`.unattended.conf` the one line `# a conf that sets neither MEMORY_ROOT nor PHASES_EXTRA`. A tree may
declare an environment, and `run_table_case`'s `tree <name>` arm sets it in `os.environ` for that case
and puts the prior values back after; only `leak` declares one.

| Tree | Environment | Case | Owed |
|---|---|---|---|
| `leak` | `MEMORY_ROOT=elsewhere`, `PHASES_EXTRA=BOGUS` | `phase --from BOGUS` | exit 1, `refused — phase BOGUS: no row` |

### The edge (S4)

`requires = ["memory-tree", "run-gates"]`. The comment sentence beside the re-run stand-in's says that
`loop_witness.py` normalises each command's output with the run-gates kit's `write_normaliser`, found by
`resolve_kit_dir`, so this kit requires run-gates. `help/loop.md`'s "Who owns it" section gains the
sentence:

```
The loop kit requires the run-gates kit too, because loop_witness.py normalises each re-run's output
with that kit's normaliser before it hashes it.
```

`_dl_claim` in `check_roles_default` gains `run-gates`. Each of 57's arms still names the pair it names:
`roles` requires `loop`, and `loop`'s new edge is met by the claim.

### The sed-fails plant (S7)

68 rev-3 S4's `normaliser-missing` rebinds the module's `KIT` to an empty scratch directory and runs the
re-run in process. `sed-fails` takes the same route through the same check function,
`check_normaliser_missing_plant`, whose scratch directory holds one file for this plant alone:
`run-gates/lib-attribute.sh` inside it, the first place `resolve_kit_dir` probes from a folder outside
any repository, whose `write_normaliser` writes the program `s/(/x/`. `sed -E` refuses that program,
so the apply step exits non-zero inside whatever bash `resolve_bash` answers, with no stub on any PATH.

### The probe's legs (S10)

For each unit, its pass commit is the one 75's probe finds by the `Pass:` trailer. Its legs are every row
of `tools/gate-legs.json` at this unit's base whose argv names a file under `{prefix}/loop/` that the pass
commit changes, as `git show --name-only <pass>` lists them. Each leg runs at the pass commit as 75's
probe runs it, and a row the pass commit's manifest lacks is recorded `no leg`, as 75 records it.
Unit 71 writes nothing (71 rev-4 §8 F3) and unit 73 writes no loop file, so neither is in the population.

### The gained prune (S19)

```
_req_at, _unknown_at = read_requires_at(root, to_commit, list(claimed) + list(gained))
claimed unknown  -> Refusal, 73 S4's text over the claimed kits alone
gained unknown   -> each taken out of `gained`, printing
                    "govkit update — default-gained <kit> NOT installed: its requires are unknown at <commit8>: <why>"
while derive_unsatisfied_requires(gained, _req_at, receipt) is non-empty: the loop as at the tip
demand_claimed_requires(claimed, gained, _req_at, receipt, _gained_why)
```

`check_gained_prune_vintage(tmp)` is called beside `check_requires_vintage(tmp3)`. It builds a scratch gov
with `build_steps_gov` whose registry declares `demo` in the default and `other` and `extra` outside it,
none requiring anything, and a target that installs `demo` at that commit, A. Then B adds `extra` to the
default and makes it require `other`; D keeps `extra` in the default and drops that edge again; E takes
`extra`'s descriptor out while the registry still names it. Read-only `update` runs:

| Checkout | `--to` | Owed |
|---|---|---|
| A | B | exit 0, `default-gained extra NOT installed`, no `update would leave` |
| B | D | exit 0, `would gain extra` |
| D | E | exit 0, `default-gained extra NOT installed: its requires are unknown at` |

### The pre-filter and its cost (S22, S23)

For a merge whose first parent holds the policy file, `check_push_range` reads each later parent's blob
through `read_policy_blob` and skips the merge where M's blob equals every parent's, an absent blob
equal only to an absent one. The `push-merge-equal-to-every-parent` plant stages the three tables as
`push-merge-both-sides-clean` does, then a side branch and main each commit a non-policy file and main
merges side `--no-ff`; `run_grade_in_process(base, {}, rows)` grades it, owing exit 0, `0 finding(s)` and
`merge-tree runs: 0`.

### The budget plants (S20, S25)

Each is a case of `tools/loop/budget.py#run_budget_plant`, inside 80 S1's boundary.

| Plant | Staged | Owed |
|---|---|---|
| `trailing-slash-agree` | `write_transition_plant(top, "default")` with `memory/builds/tFix/RUN.md` as `PLANT_RUN`; `.unattended.conf` written as `MEMORY_ROOT=memory/` beside `.memory-tree.conf`'s `MEMORY_ROOT=memory`; committed; one `draw` on `tFix` | exit 0, and the run-state file under `memory` gains the draw row |
| `no-confs` | the same staging, then `.memory-tree.conf` taken out with `git rm` and committed, no `.unattended.conf` written | `resolve_memory_root(top)` answers `memory` with no traceback |

### The url-forms rows (S21)

| configured | written | owed | a break it reads |
|---|---|---|---|
| `https://user:tok@host.example/r.git` | `https://host.example/r` | equal | a scheme URL's user and token kept |
| `https://user@host.example/r/` | `https://host.example/r` | equal | a scheme URL's user kept |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_gained_prune_vintage` | function in `tools/govkit/selftest.py` | `py.function` |
| `sed-fails` | `PLANTS` key of `loop_witness.py` | not graded |
| `trailing-slash-agree`, `no-confs` | `PLANTS` keys of `budget.py` | not graded |
| `push-merge-equal-to-every-parent` | `PLANTS` key of `guard.py` | not graded |
| `leak` | a scratch tree of the table selftest | not graded |
| `Leg-row keys:` | a line of the run-gates README | not graded |

`python tools/lexicon/lexicon.py --suggest check_gained_prune_vintage --as py.function` answered OK on this
worktree at `179486e8f`; the tip export holds no `.git`, so the verb refused there, and the two
`.lexicon.conf` files differ in `VERB_OFFENDER_PIN` alone of what this verb reads, as 70 §4 records.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/loop_table.py`
- `tools/loop/loop_witness.py`
- `tools/loop/budget.py`
- `tools/loop/guard.py`
- `tools/loop/position.py`
- `tools/loop/kit.toml`
- `tools/loop/README.md`
- `help/loop.md`
- `tools/run-gates/README.md`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/run-gates/selftest-budgets.txt`, only where a timed reading at the close moves a row
- `memory/map/generated/symbols.json`, with any generated sibling `gen_map.py --write` rewrites

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, govkit and loop.** The halves are not disjoint by M6 clause 2: S4 writes
  `tools/govkit/selftest.py`, which S19 writes too, and its edge is graded by the govkit predicate S19's
  arm runs.
- **A sed stub first on the bash's PATH, rev-5's staging.** Git for Windows' `bin/bash.exe` sets its own
  PATH and runs `/usr/bin/sed` past the stub, as `TOOL-dDeclaredLoop-82` §4 Evidence records, so the
  plant would read differently by which bash `resolve_bash` answers (§8 F5).
- **The env-leak case as a `loop_table.py --fixture` plant, rev-5's home.** Those plants break rows in
  memory and build no tree, so no conf is sourced (§8 F7).

## 5. Production-readiness checklist

- security — S1 and S2 keep a stray export from choosing the records root or the phase set; S7 observes
  the refusal that keeps a partial normalisation from being hashed; S21's rows carry a token only in a
  fixture literal.
- perf / scale — S10 costs one scratch worktree and its legs per unit, minutes in total, once at this
  pass; S23 runs `git merge-tree` for fewer merges than the tip does.
- error / empty / loading states — S7, S19 and S25 each name the failed, unknown or empty case.
- observability — S7's refusal names the step; S19's line names the kit left out and why.
- risks — S4's edge refuses an `update` over a receipt claiming `loop` without `run-gates` until
  `apply --kits` adds it, the population 75 S26 accepts; run-gates is in the default set, so a default
  install already holds it.
- testing — AC1 to AC25 as plants, probes and greps; the arms under §7, observed RED then GREEN at the
  close.
- migration — none: no receipt, conf or adopter file changes shape, so no `[[upgrade]]` row is owed.
- user docs — `help/loop.md` gains S4's sentence and names S7's plant.

### Dependency

Order 40, alone, after every unit it reads. Order 36's `TOOL-dDeclaredLoop-70` (rev-3) lands
`read_driver_conf` and its scratch-tree cases, and `TOOL-dDeclaredLoop-72` (rev-6) lands
`resolve_memory_root`, its refusal and its normalisation; 56 (rev-6) and 71 (rev-4) touch none of them.
Order 37's `TOOL-dDeclaredLoop-68` (rev-3) lands the normaliser route, its refusal and the
`normaliser-missing` plant S7 shares, and `TOOL-dDeclaredLoop-76` (rev-6) wraps 72's body in
`resolve_memory_root_source`, keeping its answer. Order 38's `TOOL-dDeclaredLoop-80` (rev-6) lands the
fixture boundary, `TOOL-dDeclaredLoop-67` (rev-4) the `loop definition fixtures` leg, and
`TOOL-dDeclaredLoop-74` (rev-3) `derive_fetch_url`. Order 39's `TOOL-dDeclaredLoop-75` (rev-10) lands the
probe, its S26 route in `demand_claimed_requires` and its S27 re-merge reading in `guard.py`, and
`TOOL-dDeclaredLoop-77` (rev-3) the `url-forms` plant and table. Each is read on its committed spec. Units
69, 73 and 78 are CLOSED and read on landed code. `TOOL-dDeclaredLoop-82` builds at order 41 and reads
S10's probe and S7's plant. `TOOL-dDeclaredLoop-34` is deferred against ask TOOL-dDeclaredLoop-113, and
`TOOL-dDeclaredLoop-33`'s numeric direction against ask TOOL-dDeclaredLoop-114; neither shares a file with
this unit.

### The sweep

Read at `8b06bb0a4`. Each figure is PINNED 2026-11-16 and re-derived by the commands below the table.

| What moves | Its readers, pins and populations | What keeps each green |
|---|---|---|
| `read_driver_conf`'s subshell | 70's callers: `derive_phase_position`'s default, 72's `resolve_memory_root`, 67 S23's `check` verb; the `loop transition tables` leg | every caller reads the conf's own values; no caller relies on an inherited one, and the leg's existing trees export nothing |
| the table selftest's trees | the `loop transition tables` leg, ceiling of 120 seconds PINNED | one more `git init` and one case beside 70's three trees |
| `tools/loop/kit.toml`'s `requires` | `tools/govkit/govkit.py#derive_unsatisfied_requires` in `apply`, `plan` and `update`; `check_roles_default`'s 57 arms; `govkit selfcheck`; `tools/govkit/matrix.py`, which closes its install set over `requires`; `tools/policy/check_policy.py#derive_requires_closure` | `_dl_claim` gains `run-gates`; the default set holds it, so `OC8 AC2`'s default selection stays satisfied; the matrix and the policy closure add it themselves; no `--kits` selection under `tools/` names `roles`, `loop` or `unattended` but 57's two |
| the descriptor comment and the help sentence | `install-prefix (shipped surface)`; `docs` and `help page commands` | each names a file and a kit, never a path joined to the prefix; no usage row or command block moves, so no anchor is re-stamped |
| the `sed-fails` plant | the `loop computed witness` leg, its budget row of 75 seconds PINNED; 68's `normaliser-missing`, whose check function it shares; 82 S7 | one re-run more, seconds; the stub file is written only for `sed-fails`, so `normaliser-missing` still finds an empty directory; 82 re-grounds on this staging |
| `check_push_range` | the `loop guard fixtures` leg, ceiling of 300 seconds PINNED and row of 90 seconds PINNED; every `push-merge-*` plant | the pre-filter skips only a merge equal to every parent, which no existing plant stages as a policy change; the new plant runs in one scratch |
| `budget.py` plants | `loop budget fixtures`; 80's `no-own-conf-read` case and its AC4 greps for `trailing-slash-agree` and `no-confs`; 88 S9; 95's re-run | both write their confs inside `run_budget_plant`, which 80 S1 bounds; the two names 80 AC4 greps are the names minted here |
| the `url-forms` table | `loop position fixtures`; 77 AC3, which owes each row as tabled; 82 S19 and S23 | two rows more, computed in memory |
| `_cmd_update`'s prune | `govkit refusal join`, whose anchors are a function and an ordinal; 73's arms; 57's `would gain` and `NOT installed` lines | no `raise` is added or taken out, and none sits between the read's old and new places, so each anchor keeps its ordinal; 73's AC3 still reaches the claimed kit's unknown refusal |
| `check_requires_vintage`'s docstring | `govkit selftest`, budget row of 1600 seconds PINNED | the clause naming the prune's vintage as unchecked goes, since the new arm checks it; one scratch gov and three read-only updates more |
| the run-gates README | `run-gates canary`'s width-source arm and the evidence suite's section arms read other sections; `measure-legs selftest` reads the profiler section | one line under the manifest section, which no arm reads |
| new names | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED | `check_gained_prune_vintage` leads with a declared verb |
| the codebase map | `codebase-map coverage + freshness`; `recall floor` and `recall floor arms` guard `memory/` | `python tools/codebase-map/gen_map.py --write` records the new function; both recall legs run at the close |
| the census and the families | `tools/memory-tree/check-arms.py`'s readers over the driver; `tools/unattended/unattended.families.txt` | no shell file is edited |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither, and no decision row is owed ahead of it |
| kit epochs | the loop, run-gates and govkit kits' shipped bytes move | the lander mints each version, `KIT_LOOP_VERSION` and the README marker paired |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md` | no watched path is edited, so no re-stamp |
| subject pins, epoch delegates, upgrade rows, size rows | `tools/govkit/subject-pins.tsv`, `tools/memory-tree/check-verdict-epoch.sh`'s `DELEGATES`, `[[upgrade]]` rows, `tools/template-size-limits.txt` | no leg is added, no memory-tree file is edited, no migration is owed, and no size row names a touched file |
| this spec's citations | `positional (the citation check alone)`; the 16 rows PINNED of this spec in `memory/project/positional-refs.txt` | this revision cites by symbol and one blob-pinned range; the commit landing it runs `python tools/playbook/positional.py shrink` |
| this spec's labels | 68, 76, 80, 82, 86, 88 and 95 cite S4, S6, S8, S10, S17, S18, S25, S26, AC10, AC11, AC20 and AC25 | the kept labels keep their numbers; S6, S8, S17, S18, S26 and AC11 are in §3, and 68 and 82 re-ground at their own orders |

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:tools/loop/kit.toml" | grep -n '^requires'
git grep -n -E 'resolve_kit_dir\("[a-z-]+"' "$B" -- tools/loop | grep -o 'resolve_kit_dir("[a-z-]*"' | sort | uniq -c
git grep -n -e '--kits' "$B" -- tools | grep -E 'roles|loop|unattended'
git show "$B:tools/run-gates/selftest-budgets.txt" | grep -E '^(loop computed witness|loop guard fixtures|govkit selftest)'
git show "$B:tools/gate-legs.json" | grep -A12 -E '"(loop transition tables|loop guard fixtures)"' | grep ceiling
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN='
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-79.md'
git log --format=%h --grep='^Pass: TOOL-dDeclaredLoop-69$' --grep='^Pass: TOOL-dDeclaredLoop-78$' "$B"
python -c "import importlib.util as u; s = u.spec_from_file_location('ca', 'tools/memory-tree/check-arms.py'); m = u.module_from_spec(s); s.loader.exec_module(m); print(len(m.branches('.', 'tools/unattended/unattended.sh')))"   # in a copy of the tip
```

### Budgets and records

- The driver's census is 343 PINNED, 338 branches PINNED counted by
  `tools/memory-tree/check-arms.py#branches` over the tip export and 5 sites PINNED by
  `tools/memory-tree/check-arms.py#scan_refusal_sites`; this unit edits no shell file, so the census, its
  ceiling and the families of `tools/unattended/unattended.families.txt` do not move.
- `VERB_OFFENDER_PIN` stays 1215 PINNED: the one new function name leads with `check`.
- The shared records: the pass writes neither `memory/DECISIONS.md` nor
  `memory/project/readme-contract.txt`, and no decision row is owed ahead of it.
- Help anchors: none added or re-stamped; no verb or flag is added, and each `--plant=` takes any name.
- The loop, run-gates and govkit kit versions are owed at the lander.

## 6. Acceptance criteria

Each `python <module>.py` command below runs that file of gov's loop kit in `tools/loop/`; every other
command runs at the top of the repository.

- **AC1** — When a `python -c` probe, run with `MEMORY_ROOT=elsewhere` exported, calls
  `read_driver_conf(tree, ["MEMORY_ROOT"])` over a scratch work tree whose `.unattended.conf` does not set
  it, the mapping has no `MEMORY_ROOT` key.
  Red when: the subshell inherits the export and answers `elsewhere`.
- **AC2** — When the same probe reads a conf holding `MEMORY_ROOT="${ROOT##*/}-records"` and
  `PHASES_EXTRA="${CONF##*/}"`, it answers the scratch tree's directory name followed by `-records`, and
  `.unattended.conf`.
  Red when: `ROOT` or `CONF` is unset in the subshell, so the answers are `-records` and empty.
- **AC3** — When `python loop_table.py check --selftest` runs, it exits 0 with its `leak` case passing:
  `phase --from BOGUS` exits 1 printing `refused — phase BOGUS: no row`. And a `python -c` probe run with
  `MEMORY_ROOT=elsewhere` and `PHASES_EXTRA=BOGUS` exported, calling `resolve_memory_root` over a scratch
  work tree whose `.unattended.conf` sets neither and which holds no `.memory-tree.conf`, prints `memory`.
  Red when: the exported `PHASES_EXTRA` admits `BOGUS` as an adopter phase, or the exported root wins.
- **AC4** — When `grep -n '^requires' kit.toml` runs in `tools/loop/`, it prints a line naming
  `run-gates`; a probe calling `derive_unsatisfied_requires(["loop"], descs, {"kits": []})` over the
  working tree's descriptors lists `('loop', 'run-gates')`; and `grep -c "requires the run-gates kit"
  help/loop.md` prints at least 1.
  Red when: the edge is absent and a selection with `loop` alone installs with no run-gates kit.
- **AC7** — When `python loop_witness.py --fixture --plant sed-fails` runs, it exits 0:
  `run_witness_commands` raises a `LookupError` whose text opens `witness: normaliser unavailable — sed:`,
  the fixture repository lists one worktree, and the `rerun` verb run in process prints a
  `rerun · inconclusive · ` line and a stderr line carrying `witness: normaliser unavailable — sed:`. And
  `grep -c sed-fails` prints at least 1 over `help/loop.md` and over `tools/loop/README.md`.
  Red when: the failed apply step's empty output is hashed, or the refusal names another step.
- **AC10** — When the pass-commit probe of 75 §4 runs, at the pass commit of each of units 68, 69, 70, 72,
  74, 76, 77 and 78, every leg §4 "The probe's legs" derives, each exit is recorded in this unit's
  acceptance ledger with its unit, its leg and its commit, and every exit is 0 or `no leg`.
  Red when: a pass broke the leg running its own file and only a hands-off bullet was read.
  cost: one scratch worktree per unit, minutes in total.
- **AC13** — When `grep -c "^Leg-row keys:" tools/run-gates/README.md` runs it prints 1, and a probe
  taking every key of every row of `tools/gate-legs.json`, less the backticked words on that line,
  prints nothing.
  Red when: no single key-list line exists, or it omits `stage` or another key the manifest carries.
- **AC19** — When a `python -c` probe imports the govkit kit's self-test module and calls
  `check_gained_prune_vintage` over a temporary folder, its three updates read as §4 "The gained prune"
  tables them: the first exits 0 printing `default-gained extra NOT installed` and no
  `update would leave`, the second prints `would gain extra`, and the third prints
  `default-gained extra NOT installed: its requires are unknown at`.
  Red when: the prune grades the working tree, so the first run refuses the whole update and the second
  leaves `extra` out.
- **AC20** — When `python budget.py --fixture --plant trailing-slash-agree` runs, it prints
  `loop: fixture · trailing-slash-agree · held`: the draw exits 0 and its row lands under `memory`.
  Red when: a raw compare refuses `memory/` against `memory`.
- **AC21** — When `python position.py --fixture --plant url-forms` runs, it prints both https rows as
  `· equal` against `https://host.example/r` and holds every other row as tabled.
  Red when: a scheme URL keeps its user part, so a row reads `· unequal`.
- **AC22** — When `python -c` prints `check_push_range.__doc__` from the loop kit's `guard.py`, it names
  `merge-tree` and `per two-parent merge`, and a measured time in ms with its date.
  Red when: the docstring states no cost, or keeps 69 §5's "unchanged".
- **AC23** — When `python guard.py --fixture --plant push-merge-equal-to-every-parent` runs, it prints
  `merge-tree runs: 0` and every scenario held, exiting 0; and
  `python guard.py --fixture --plant push-merge-revert-to-unchanged-side` still exits 1 with every
  scenario held.
  Red when: a merge equal to every parent still runs the re-merge, or the pre-filter skips the revert
  case.
- **AC25** — When `python budget.py --fixture --plant no-confs` runs, it prints
  `loop: fixture · no-confs · held` and no `Traceback`.
  Red when: an absent `.memory-tree.conf` raises, or the root reads as anything but `memory`.

## 7. Gates

`loop transition tables` · `loop computed witness` · `loop budget fixtures` · `loop guard fixtures` · `loop position fixtures` · `loop definition` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `docs` · `help page commands` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `positional (the citation check alone)` · `kit epoch (shipped bytes move, the version moves)` · `every held leg is budgeted, every budget row resolves` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_table.py · covers AC3 · the leak tree's case, staged against 70's subshell, which inherits the export and admits BOGUS · none
New arm: tools/loop/loop_witness.py · covers AC7 · the sed-fails plant, staged against an apply step whose non-zero exit is ignored and its empty output hashed · none
New arm: tools/loop/budget.py · covers AC20 AC25 · the trailing-slash-agree and no-confs plants, staged against a raw compare of the two roots and a conf read that raises on an absent file · none
New arm: tools/loop/guard.py · covers AC23 · the equal-to-every-parent plant, staged against the tip's grade, which runs the re-merge first · none
New arm: tools/loop/position.py · covers AC21 · the two https rows of the url-forms table, staged against a user-part cut for the scp and ssh forms alone · none
New arm: tools/govkit/selftest.py · covers AC19 · the gained-prune vintage arm, staged against the prune grading the working tree's descriptors · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Isolate the driver-conf subshell by unsetting the names, presetting the driver's defaults, or
  reading only names the conf declares (ids 2, 16)?** (a) unset each requested name, the callers holding
  the defaults; (b) preset each from the driver's init lines, which needs the unattended kit resolved and
  its init block parsed; (c) import only declared names, as the unattended kit gate does. (b) adds a
  reach the loop kit takes no edge for; (c) still inherits for a name the conf appends to. (a) satisfies
  AC1 to AC3 with no new dependency. RESOLVED (agent, 2026-10-24, delegated): (a), S1.
  widens: none · relaxes: none
- **F3 — Fund 75 S25's protocol bytes by a trim or a raise of the row (id 21)?** (a) trim
  `tools/unattended/PROTOCOL.template.md` in this unit; (b) raise the row in 75's own commit, the commit
  whose change crosses it, which the row file's first condition allows. Rev-5 took (a) while 75 had no
  route of its own; 75 rev-10 §8 F6 takes (b) and its AC25 reads the raised row, so a trim here would
  fund bytes already funded. RESOLVED (agent, 2026-11-16, delegated): (b), by 75; S17 is in §3.
  widens: none · relaxes: none
- **F4 — Clear S18's join hits by amending sibling leg lines or by waiver rows (id 22)?** (a) the leg on
  each tripped spec's line; (b) dated rows in `memory/project/spec-token-waivers.txt`, shrink-only by its
  header, so a new row reds. At rev-6 no loop leg carries a `guard`, so the join names no hit and (a)
  amends nothing. RESOLVED (agent, 2026-11-16, delegated): (a), with nothing to amend; S18 is in §3.
  widens: none · relaxes: none
- **F5 — How does the `sed-fails` plant make the apply step fail (id 30)?** (a) a `sed` stub first on the
  bash's PATH, rev-5's staging; (b) 68's `normaliser-missing` route with a stub run-gates library whose
  `write_normaliser` writes a program `sed -E` refuses; (c) a `BASH_ENV` file prepending the stub
  directory, as `TOOL-dDeclaredLoop-82` S7 proposes. (a) reads differently by which bash answers, since
  Git for Windows' launcher sets its own PATH; (c) needs a `cygpath` spelling and a pre-check per bash.
  (b) fails the real `sed` the same way under every bash, through a route 68 already builds.
  Recommendation: (b). RESOLVED (agent, 2026-11-16, delegated): (b), S7.
  widens: none · relaxes: none
- **F6 — Which spellings of one records root agree (id 35)?** (a) 72's normalisation, surrounding
  whitespace and slashes stripped, observed on `memory/` against `memory`; (b) that, and a leading `./`
  stripped and `\` folded to `/`, as rev-5 wrote. Under (a) a `./memory` beside `memory` refuses by name
  with both values printed, and the fix is to spell them alike; (b) widens a function 72 lands for
  spellings no conf in the tree uses. Recommendation: (a).
  RESOLVED (agent, 2026-11-16, delegated): (a), S20.
  widens: none · relaxes: none
- **F7 — Where does the env-leak observation run (id 32)?** (a) a scratch tree of the table selftest, 70's
  form, its case run under the exported names, with a `python -c` probe of `resolve_memory_root`; (b) a
  `budget.py` plant reading the root alone; (c) rev-5's `loop_table.py --fixture` plant. (c) builds no
  tree, so nothing is sourced, and (b) observes one of the two names. Recommendation: (a).
  RESOLVED (agent, 2026-11-16, delegated): (a), S3.
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
- rev-6 · 2026-11-16 · §1 to §10 · S1 to S28 · AC1 to AC28 · §8 F3 to F7 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `8b06bb0a4` and on the committed specs of TOOL-dDeclaredLoop-68
  rev-3, -70 rev-3, -72 rev-6, -74 rev-3, -75 rev-10, -76 rev-6, -77 rev-3 and -80 rev-6, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-79-1-spec-writer`: S5, S6, S8, S9, S11, S12, S14 to S18 and S26
  to S28 and their criteria in §3 with what settles each, S24 refused on CLOSED 73; S1 and S2 on 70's
  rev-3 reader; S3 a scratch tree of the table selftest (F7); S4 brings the help sentence and 57's claim;
  S7 staged through 68's route (F5); S10's legs derived on 75's probe; S19's arm and its fixture; S20 on
  72's normalisation (F6); S21 on `derive_fetch_url`; S23 on the built grade; S25 the `no-confs` plant
  alone; F3 and F4 re-resolved; line citations made symbol citations; the sweep.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy: 70's `read_driver_conf` and its
scratch-tree cases (S1 to S3), the driver's own `tools/unattended/unattended.sh#load_driver_conf` order
for `ROOT` and `CONF` (S2), the descriptor's `requires` and govkit's one predicate
`tools/govkit/govkit.py#derive_unsatisfied_requires` (S4), 68's `normaliser-missing` route and check
function (S7), 75's pass-commit probe on the run-gates kit's `add_scratch_worktree` and `derive_leg_argv`
(S10), 73's `tools/govkit/govkit.py#read_requires_at` passed to a second caller and the scratch-gov factory
`tools/govkit/selftest.py#build_steps_gov` (S19), 72's normalisation and `run_budget_plant` (S20, S25),
77's `url-forms` table over 74's `derive_fetch_url` (S21), and `tools/loop/guard.py#read_policy_blob`
with the `run_grade_in_process` counter (S22, S23).
`python tools/codebase-map/reuse_lookup.py "strip the user part from a remote url before comparing"` and
`"find calls that read a config file by walking a module's syntax tree"` ranked `resolve_remote`,
`read`, `read_text`, `walk` and `read_conf`, read above and not fit; the memory-recall query on the
driver-conf reader returned this build's own records and spec 70, so no new reader is minted where one
of these exists. At rev-6 the seams above were each read on the branch tip, and the counter the guard
plant needs was found already built in the `push-merge-both-sides-clean` plant's stand-in.

Recall terms used: read_driver_conf MEMORY_ROOT unattended.conf sourced subshell inherited environment driver default requires run-gates gained prune merge-tree pre-filter derive_fetch_url
