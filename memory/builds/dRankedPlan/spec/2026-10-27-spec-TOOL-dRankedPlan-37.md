# TOOL-dRankedPlan-37 — the spec audit of units 19 to 29: its 25 medium and low findings, closed in one batch

**Status:** DEFERRED · rev-4 · 2026-10-28 · node a · Tier-2 · base 0689e7fa · streams tooling · order 18 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-30-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-30-promoted-fix-return.md) | research | TOOL-dRankedPlan-30 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 |
| [2026-10-27-build-TOOL-dRankedPlan-37-deviation-371.md](../build/2026-10-27-build-TOOL-dRankedPlan-37-deviation-371.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-37-deviation-372.md](../build/2026-10-27-build-TOOL-dRankedPlan-37-deviation-372.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-28-build-TOOL-dRankedPlan-37-deviation-373.md](../build/2026-10-28-build-TOOL-dRankedPlan-37-deviation-373.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md) | research | TOOL-dRankedPlan-30 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 |
| [2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-38 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 TOOL-dRankedPlan-48 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-57 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-64 TOOL-dRankedPlan-67 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 TOOL-dRankedPlan-81 |
| [2026-10-28-prompt-TOOL-dRankedPlan-1-parents-reground.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-reground.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-9 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-24 TOOL-dRankedPlan-29 TOOL-dRankedPlan-31 TOOL-dRankedPlan-45 |
| [2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) | spec-audit | TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-36 TOOL-dRankedPlan-33 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 19 to 29
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`) confirmed 17
MEDIUM and 8 LOW findings. BUILD-METHOD M4 promotes them all into one unit, and this is that unit.
Each finding is named by its report id and given its own §2 item. Where the report merged ids into one
item, each id still takes its own item, and the item it shares is named beside it. Four mediums are the
medium face of a high that has its own unit. Each of those items adds the observation the medium's fix
names, over the high's mechanism, and never repeats the mechanism.

| Item | Ids | Grade | High face | §2 |
|---|---|---|---|---|
| M1 | 1, 32 | MEDIUM | `TOOL-dRankedPlan-33` (H3) | S1, S2 |
| M2 | 2, 12, 22, 33, 34 | MEDIUM | none | S3, S4, S5, S6, S7 |
| M3 | 3 | MEDIUM | none | S8 |
| M4 | 4 | MEDIUM | none | S9 |
| M5 | 5 | MEDIUM | `TOOL-dRankedPlan-36` (H6) | S10 |
| M6 | 7 | MEDIUM | none | S11 |
| M7 | 9 | MEDIUM | `TOOL-dRankedPlan-30` (H1) | S12 |
| M8 | 11 | MEDIUM | `TOOL-dRankedPlan-31` (H2) | S13 |
| M9 | 13 | MEDIUM | none | S14 |
| M10 | 23 | MEDIUM | none | S15 |
| M11 | 31 | MEDIUM | none | S16 |
| M12 | 35 | MEDIUM | none | S17 |
| L1 | 8, 18, 25 | LOW | none | S18, S19, S20 |
| L2 | 14 | LOW | none | S21 |
| L3 | 16 | LOW | none | S22 |
| L4 | 17 | LOW | none | S23 |
| L5 | 24 | LOW | none | S24 |
| L6 | 27 | LOW | none | S25 |

The minors land on more than ten units, so this unit repairs none in particular and is ordered after every
unit of the build. Several items observe another unit's criterion at a tip where what it rests on
exists. That is the honest place for them, and each such unit's §3 carries a hands-off edge naming the
item, so its builder reads the change before building.

## 2. Scope (IN)

- **S1** — Id 1, item M1 (with id 32; high face `TOOL-dRankedPlan-33`). The two other fixtures that
  record an admitted `plan.exit` move seed their scratch repository through `TOOL-dRankedPlan-33` S1's
  `ratify.py --fixture --seed <dir> --build <slug>`, for each build whose move they write through
  `write_transition`. They are `gen_build_index.py --ratified-order --plant drafts-cross-session`
  (`TOOL-dRankedPlan-21` S4), with builds `dA`, `dB` and `dC`, and every `plan_revision.py --selftest`
  plant that plants a `plan.exit` move (`TOOL-dRankedPlan-15` S6), with build `tFix`. The generator's
  plant reaches the loop kit as `TOOL-dRankedPlan-21` S3 does, running its CLIs as subprocesses found
  through `backlog.resolve_kit_dir`, `ratify.py --fixture --seed` and `loop_transition.py record` for
  each move, and imports no loop-kit module (PLAY-dOrderedCharter-7 §4); `plan_revision.py`, inside the
  loop kit, calls `write_transition` itself. Observed by AC1.
- **S2** — Id 32, item M1 (with id 1). `TOOL-dRankedPlan-10` AC6, a `pre-placement` move admitted with
  no disposition, holds over the seeded record of `TOOL-dRankedPlan-33` S2. `TOOL-dRankedPlan-19` AC2's
  `pre-placement` variant of `plan-record-absent`, which has no record, is refused. The two criteria
  read different plants, and both stand. Observed by AC2.
- **S3** — Id 2, item M2 (with ids 12, 22, 33, 34). Every `plan_revision.py --selftest` plant loses its
  stub `read_plan_ratification`: unit 15 S6's seven, unit 23 S3's and unit 29 S32's. Each plant that
  records a re-entry plants its `plan.exit` move with an explicit `ratification=` value. So
  `TOOL-dRankedPlan-23` AC4's count of the name in the module reads 0. Observed by AC3.
- **S4** — Id 12, item M2. `TOOL-dRankedPlan-29` S32's plant `reentry-later-session` is restated. Its
  re-entering move carries `ratification=witness`, and `show` runs in a second process whose session id
  is on no `.typed` line, with no stub. This supersedes unit 29 S32's "its stub `read_plan_ratification`
  answers no witness". Observed by AC4.
- **S5** — Id 22, item M2. After S3 and S4, `plan_revision.py` holds no definition, call or reference
  named `read_plan_ratification`, so `ratify.py --check-callers` (`TOOL-dRankedPlan-22` S2, read by
  `TOOL-dRankedPlan-32`) admits the file at this unit's tip. Observed by AC5.
- **S6** — Id 33, item M2. The plant `goal-fork` plants its re-entering move with
  `ratification=witness`. `TOOL-dRankedPlan-15` AC1's expected line, `revision — 1 · ratified · request
  · <witness> · design re-entered at <sha8>`, is superseded by `TOOL-dRankedPlan-23` S2's form,
  `revision — 1 · ratified · witness · harness <h> · design re-entered at <sha8>`. Observed by AC6.
- **S7** — Id 34, item M2. `TOOL-dRankedPlan-29` AC26's red case becomes a `show` that re-asks the real
  predicate. In S4's second process the predicate answers no witness, so a `show` that asks it prints
  unratified, and the plant reds. Observed by AC4.
- **S8** — Id 3, item M3. `TOOL-dRankedPlan-25` AC2's second move is spelled `--field harness=codex`,
  and `TOOL-dRankedPlan-10` AC2's move, which `TOOL-dRankedPlan-21` AC1 reads, is spelled `--field
  harness=claude-code`. Their harness halves are observed here, over `TOOL-dRankedPlan-29` S15's
  pass-through, which lands at order 17. Observed by AC7.
- **S9** — Id 4, item M4. This unit owns `TOOL-dRankedPlan-22` AC3. At its tip, after units 21, 23 and
  29 and S3 to S5 here, the tree run of `ratify.py --check-callers` exits 0. A scratch clone whose
  `gen_build_index.py` carries one `read_plan_ratification(` call exits 1 naming that file. Observed
  by AC5.
- **S10** — Id 5, item M5 (high face `TOOL-dRankedPlan-36`). The plant `plan-new-first` joins
  `scenario.py --fixture`. A `new` build with no plan record and no transition record writes the
  claim's first move into `planning`, carrying `scenario=scenario.feature`, through `loop_transition.py
  record`. It is admitted over `TOOL-dRankedPlan-36` S2's pin. Observed by AC8.
- **S11** — Id 7, item M6. `TOOL-dRankedPlan-29` S3's hold is spelled `bash
  tools/unattended/unattended.sh --park dRankedPlan --item TOOL-dRankedPlan-5 --reason <text>`, the
  per-decision verb (`tools/unattended/unattended.sh:17`). `--hold` takes no `--item` and requires
  `--code`, `--until` and a reap flag (:24). Unit 29 AC2's hold-row branch reads the `decision · item
  TOOL-dRankedPlan-5` row that verb writes. Observed by AC9.
- **S12** — Id 9, item M7 (high face `TOOL-dRankedPlan-30`). At this unit's tip, `bash
  tools/check-install-prefix.sh --offenders` prints no key whose path is the loop kit's `ratify.py`.
  Observed by AC10.
- **S13** — Id 11, item M8 (high face `TOOL-dRankedPlan-31`). Two guards widen in their kits'
  `[[gate_leg]]` declarations, each leg's one declaration, under a `[gate_leg.gov]` sub-table where
  gov's guard differs from an adopter's, and `python tools/run-gates/leg_factory.py --write` renders
  `tools/gate-legs.json` (TOOL-dWitnessedBar-11 S1, S2); until that unit lands, the manifest edit is
  the hand-written stand-in the pass's deviation record names. `build-index selftest` gains
  `{prefix}/loop/ratify.py`, which `TOOL-dRankedPlan-21` S4's plant runs. `loop selftest` gains
  `{prefix}/memory-tree/plan_record.py` and `{prefix}/memory-tree/plan_fields.py`, which
  `TOOL-dRankedPlan-19`'s plants run. Unit 22's tree run has left the guarded leg through
  `TOOL-dRankedPlan-31`. Observed by AC11.
- **S14** — Id 13, item M9. The `reader-bound` plant (`TOOL-dRankedPlan-24` S3) gains `merged-add`.
  A record added on a branch forked after the newest transition and merged is kept. A record added on
  a branch forked before it and merged after is not kept. Both are dated by `TOOL-dRankedPlan-34`'s
  `read_first_appearance`. The loop kit holds one adding-commit read, so a second reader cannot hold the
  opposite tie-break. §4 records why `tree_lib.read_adding_commits` is not that reader. Observed by AC12.
- **S15** — Id 23, item M10. The two recipe checks of `tools/unattended/unattended.test.sh`, at :12454
  and :12470, extend their needles past `--asks <value>` to the ` --priority <n>` that
  `TOOL-dRankedPlan-29` S28 adds, so the substring `hit` reds on a recipe that lacks the flag. Observed
  by AC13.
- **S16** — Id 31, item M11. Two cases join `ratify.py --fixture --plant <case>`, each laid out from
  `TOOL-dRankedPlan-30`'s anchors. In `caller-shell-bare`, a `.githooks/pre-commit` runs `"$py"
  "$d/ratify.py" "$slug"`, the bare `ratify.py "$slug"` form `TOOL-dRankedPlan-32` S2 reads, and it is
  refused. In `caller-shell-exit`, the same command continues with
  `\` onto a second line carrying `--exit`, and it is admitted. Observed by AC14.
- **S17** — Id 35, item M12. `read_ratifying_exit(repo, slug)` in `tools/loop/ratify.py` answers the
  newest of the build's `plan.exit` moves whose `ratification` is in `RATIFYING_EXITS`, or `None`.
  `check_ratified_order`'s ratified set (`TOOL-dRankedPlan-21` S3) is the set of rows whose build it
  answers for: the verdict of `ratify.py <slug> --exited` (that unit's S1, §8 F3) reads `ratifying`
  when `read_ratifying_exit` answers a move, so the generator still reads it by subprocess. So a later crossing that records no owner act, a forged `before-placement` trailer
  included, cannot downgrade a row an owner act ratified, which is unit 21 §3's rule that a revision
  keeps the row ratified. `read_exit_ratification` stays the newest-move reader `show` takes
  (`TOOL-dRankedPlan-23` S1). The `drafts-cross-session` plant gains a forged newer `plan.exit` move
  for `dA` carrying `ratification=before-placement`. Observed by AC15.
- **S18** — Id 8, item L1 (with ids 18, 25). `TOOL-dRankedPlan-29` AC12 is superseded by AC16 here,
  which reads unit 16's spec text and not a pinned sha, so the criterion can go red. Observed by AC16.
- **S19** — Id 18, item L1. `TOOL-dRankedPlan-29` S16's re-pin is carried out as a record correction of
  `TOOL-dRankedPlan-16` §4's population line (:149), 697 to 695, as a rev bump of that spec with a §9
  line naming this unit and finding 18. Observed by AC16.
- **S20** — Id 25, item L1. The same correction covers unit 16 §5's perf line (:248), "697 files", so no
  line of that spec states 697. Observed by AC16.
- **S21** — Id 14, item L2. §4 records why `Item` and ancestry stand beside `Hold`. `Hold` names the
  run-state `decision` row a driver hold writes (TOOL-dDeclaredLoop-56 S13). `check_plan_exit` runs
  inside `write_transition` in any session, attended ones included, where no run-state and no `decision`
  row exist. An ask row in `memory/builds/dDeclaredLoop/BACKLOG.md` asks that `loop_lib.py disposition`
  carry the one freshness bound `read_item_disposition` holds. Observed by AC17.
- **S22** — Id 16, item L3. `show` in `tools/loop/plan_revision.py` (`TOOL-dRankedPlan-23` S2) tests
  `how in RATIFYING_EXITS`, imported from `ratify.py` (`TOOL-dRankedPlan-21` S2). A re-entry whose
  `how` is `before-placement` prints `revision — <n> · admitted · before-placement · no owner act ·
  design re-entered at <sha8>` and exits 0. The plant `before-placement-reentry` joins
  `plan_revision.py --selftest`. Observed by AC18.
- **S23** — Id 17, item L4. `check_repo_relative_path(value)` (`TOOL-dRankedPlan-29` S19) lives in
  `tools/memory-tree/tree_lib.py`, which `routed_commits.py` already imports
  (`tools/memory-tree/routed_commits.py:73`). It raises `ValueError` naming the rule for an absolute
  path, a drive letter, a leading `~` or a `..` segment, and each caller wraps it in its own refusal.
  `routed_commits.py`'s inline copy (:159-162), `read_asks_args` (`gen_build_index.py`) and
  `TOOL-dRankedPlan-13` S2's `Scope` check call it, so all three refuse `~`. Unit 29 AC15 widens to three
  callers. Observed by AC19.
- **S24** — Id 24, item L5. The reason units 27 and 28 give for leaving the kit version alone is
  restated. The roles version is `KIT_ROLES_VERSION` at `tools/roles/roles_lib.py:27`, named by
  `tools/roles/kit.toml:22`'s `version_from`. The memory-tree version is `KIT_MEMORY_TREE_VERSION` in
  `tools/memory-tree/check-memory-hygiene.sh:69`, named by `tools/memory-tree/kit.toml:6`. `govkit.py
  mint` at the lander writes every owed bump (`tools/push-main.sh:26-30`), so no unit moves one by
  hand. This supersedes the descriptor reason of unit 27 S3 and unit 28 §3. A gotcha class,
  `memory/gotchas/a-version-claim-names-the-descriptor-not-its-carrier.md`, names the trap and its two
  carriers. Observed by AC20.
- **S25** — Id 27, item L6. `read_item_disposition` does not keep a record whose path git does not
  track, which is an untracked or a staged-only record, whether or not the build has a transition. It
  appends `disposition <path> not committed` to its `why` (`TOOL-dRankedPlan-35` S1). A tracked record
  with no adding commit appends `disposition <path> has no adding commit`. `reader-bound` gains
  `untracked`, a fresh record left uncommitted, run with and without a transition. Observed by AC21.

## 3. Non-goals (OUT)

- Any HIGH of the same audit: units 30 to 36.
- Rewriting a landed spec. Every correction here supersedes a sentence it names. Unit 16's spec is a
  record of this build, corrected by a rev bump before the build lands (S19).
- Real provenance for a `Gov-Transition` trailer, meaning a commit-time check that one arrives only
  through `write_transition`. It is a named follow-up of S17, and the hands-off below names it.
- Two batch units. A disjoint half exists, made of ids 11, 14, 23 and 24, which touch only manifest,
  record and test files. It is four small edits, and one unit is what M4 asks for by default.

### Edges

- **consumes-from** `TOOL-dRankedPlan-10` — AC2's and AC6's plants and moves, which S2 re-reads over the seeded base and S8 spells with `--field harness=claude-code`
- **consumes-from** `TOOL-dRankedPlan-13` — S2's `Scope` check, the third caller S23 points at `check_repo_relative_path`
- **consumes-from** `TOOL-dRankedPlan-15` — `plan_revision.py --selftest`'s plants and AC1's expected line, which S1, S3 and S6 seed, de-stub and supersede
- **consumes-from** `TOOL-dRankedPlan-16` — §4's population line and §5's perf line, the two 697s S19 and S20 correct
- **consumes-from** `TOOL-dRankedPlan-19` — AC2's `pre-placement` variant and the `plan-record-*` plants, which S2 re-reads and whose memory-tree reads S13 adds to the guard
- **consumes-from** `TOOL-dRankedPlan-21` — `read_exit_ratification`, `RATIFYING_EXITS`, `check_ratified_order` and the `drafts-cross-session` plant, which S1, S17 and S22 extend and S13 guards
- **consumes-from** `TOOL-dRankedPlan-22` — AC3 and the `caller-guard` plant, which S9 owns at this tip and S16 extends
- **consumes-from** `TOOL-dRankedPlan-23` — `show`, AC4 and S3's plants, which S3, S6 and S22 complete
- **consumes-from** `TOOL-dRankedPlan-24` — `read_item_disposition`, its `reader-bound` plant and §10, which S14, S21 and S25 extend
- **consumes-from** `TOOL-dRankedPlan-25` — AC2's `codex-reentry` move and the `fallback-reentry` plant, which S8 spells with `--field harness=codex` and S2 re-runs
- **consumes-from** `TOOL-dRankedPlan-27` — S3's reason for leaving the roles version alone, which S24 restates
- **consumes-from** `TOOL-dRankedPlan-28` — §3's reason for leaving the memory-tree version alone, which S24 restates
- **consumes-from** `TOOL-dRankedPlan-29` — S3, S15, S16, S19, S28 and S32 with AC2, AC12, AC15, AC22 and AC26, which S4, S7, S8, S11, S15, S18 and S23 respell, observe or supersede
- **consumes-from** `TOOL-dRankedPlan-30` — the derived allowlist, over which S12 reads `--offenders` and S16 lays out its cases
- **consumes-from** `TOOL-dRankedPlan-32` — the shell reading of the caller predicate, over which S16 plants the bare and the continued command
- **consumes-from** `TOOL-dRankedPlan-33` — `ratify.py --fixture --seed`, through which S1 seeds the two other fixtures
- **consumes-from** `TOOL-dRankedPlan-34` — `read_first_appearance`, over which S14 plants the merged adds and S25 names a record with no adding commit
- **consumes-from** `TOOL-dRankedPlan-35` — the reader's `why` list, which S25 writes its two lines into
- **consumes-from** `TOOL-dRankedPlan-36` — the pin on a build's first move, over which S10 plants a `new` build's move into `planning`
- **hands-off** external — the commit-time provenance check that a `Gov-Transition` trailer arrives only through `write_transition`, S17's named follow-up
- **hands-off** `TOOL-dRankedPlan-42` — AC19's CLI half, which that unit respells quoted and observes through a selftest case on the literal `~/x` (spec audit of units 30 to 37, id 10)
- **hands-off** `TOOL-dRankedPlan-45` — S13's guards, S19's correction of unit 16, S23's helper, S25's hold line and S24's gotcha render, which that unit's items for findings 15, 29, 28, 40, 18 and 31 correct; carry S11, S12, S18's AC11 reading, S27 and S30 of that unit into this unit's pass (spec audit of units 30 to 37)
- **hands-off** `TOOL-dRankedPlan-61` — S1's render rule, which this unit's function makes owed: carry `memory/map/generated/symbols.json` into this unit's Files touched and `codebase-map coverage + freshness`, `recall floor` and `recall floor arms` onto its leg line, in this unit's pass (spec audit of units 46 to 52, id 22)

## 4. Design

### Evidence

- M2: `TOOL-dRankedPlan-15` S6 gives every plant a stub. `TOOL-dRankedPlan-23` S3 removes it from
  `unratified-reentry` only, and its AC4 needs the name's count to be 0. `TOOL-dRankedPlan-29` S32 adds
  a stub back.
- M3: `TOOL-dRankedPlan-10` §4 "The record" writes `harness=unknown` when none is passed, and the
  pass-through is `TOOL-dRankedPlan-29` S15, at order 17.
- M6: `tools/unattended/unattended.sh:17` gives `--park <slug> --item <text> --reason <text>`, and
  `verb_park` (:12872) records the row `decision · item <item> · reason <text>` (:12905). Line :24
  gives `--hold` its required `--code`, `--until` and reap flags.
- M10: `hit()` (`tools/unattended/unattended.test.sh:144`) is `grep -qF`, a substring match.
- L1: `TOOL-dRankedPlan-16` states 697 at :149 and :248, and unit 29 S16 measured 695 at `0689e7fa1`.
- L4: `tools/memory-tree/routed_commits.py:159-162` refuses `^([A-Za-z]:|/|~)` and a `..` segment.
  `tools/memory-tree/gen_build_index.py:3340` refuses `/`, a drive letter and `..`, but not `~`.
- L5: `tools/roles/kit.toml:22` and `tools/memory-tree/kit.toml:6` each hold only a `version_from`
  pointer. `tools/push-main.sh:26-30` mints kit versions into the prepared merge.
- M1, M8: PLAY-dOrderedCharter-7 §4 (its spec :202-205) has a kit reach a sibling only by running its
  CLI, and `tools/memory-tree/kit.toml:8` declares no `requires_if` row for `loop`; TOOL-dWitnessedBar-11
  S1, S2 make a leg's declaration the one home of its guard, the manifest rendered from it.

### The shared adding-commit reader (S14)

`tree_lib.read_adding_commits` (`tools/memory-tree/tree_lib.py:302-325`) is the memory-tree kit's one
adding-commit reader, and it returns the oldest add, as `read_first_appearance` does. It reads with
`--no-renames`, so a renamed path is added again under its new name. That is the defect
`TOOL-dRankedPlan-34` closes, so the loop kit keeps its own one reader and states the reason here. The
two agree on the tie-break, oldest add first, for a record deleted and re-added.

### The strongest owner act (S17)

| The build's `plan.exit` moves, oldest first | `read_exit_ratification` (show) | `read_ratifying_exit` (order) |
|---|---|---|
| `witness` | `witness` | `witness` |
| `disposition`, then a forged `before-placement` | `before-placement` | `disposition` |
| `before-placement` only | `before-placement` | `None` |

The window is every crossing of the build, never "since the newest backward move". `TOOL-dRankedPlan-21`
§3 keeps a row ratified across a plan revision, and a window that opened at the revision's B6 move
would unratify it until the next crossing.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_ratifying_exit` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest read_ratifying_exit --as py.function` answered OK |
| `merged-add`, `untracked` | `reader-bound` cases | none |
| `caller-shell-bare`, `caller-shell-exit` | `ratify.py` fixture plants | none |
| `before-placement-reentry` | `plan_revision.py --selftest` plant | none |
| `plan-new-first` | `scenario.py` fixture plant | none |
| `a-version-claim-names-the-descriptor-not-its-carrier` | gotcha class | none |

### Rollout

This unit lands last, at order 18. S23 moves shipped bytes of the memory-tree kit, and the lander
mints that kit's version, which is S24's own rule.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`: S1, S17's plant, S23
- `tools/loop/plan_revision.py`: S1, S3, S4, S6, S7, S22
- `tools/loop/ratify.py`: S14, S16, S17, S25
- `tools/loop/scenario.py`: S10
- `tools/memory-tree/kit.toml`, `tools/loop/kit.toml`: S13's declarations
- `tools/gate-legs.json`: S13, rendered by `leg_factory.py --write`, hand-written as the stand-in
  until TOOL-dWitnessedBar-11 lands
- `tools/unattended/unattended.test.sh`: S15
- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/routed_commits.py`, `tools/memory-tree/plan_fields.py`: S23
- `memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md`: S19, S20
- `memory/builds/dDeclaredLoop/BACKLOG.md`: S21's ask row
- `memory/gotchas/a-version-claim-names-the-descriptor-not-its-carrier.md`: S24

### Alternatives rejected

- **Order this batch's order-sensitive items early.** BUILD-METHOD M4 orders a batch that repairs no
  one unit after every unit. Each early unit is told instead, through its own hands-off edge.
- **Refuse `~` nowhere.** A home-relative path is outside the repository in every shell, so deny by
  default refuses it in all three callers.

## 5. Production-readiness checklist

- security — S17 narrows the reorder a forged trailer could unlock, and its §4 states the model:
  a trailer and its log record are agent-writable, a forged pair goes undetected, and the order check
  reads the strongest owner act the history holds. S23 refuses `~` everywhere. S25 holds an
  uncommitted owner act.
- perf / scale — one more transition read per build for S17, and none elsewhere.
- error / empty / loading states — S25's two lines name why a record was not kept.
- observability — each plant prints its answer, and S11's row is on the run-state file.
- risks — S19 edits a spec of this build that has closed. It is a record correction with a §9 line,
  before the build lands.
- testing — the plants of S1, S4, S10, S14, S16, S17, S22 and S25, the probes of S5, S9, S12 and S13,
  and the greps of S3, S15, S18 to S21 and S24.
- migration — none.
- user docs — N/A — no user-facing surface moves. `help/plan.md` already names `--exited`, and S17's
  reader is internal to the order check.

## 6. Acceptance criteria

- **AC1** — When `python3 tools/memory-tree/gen_build_index.py --ratified-order --plant
  drafts-cross-session` runs at this unit's tip, the commit putting `dB` before `dA` exits 1 and the
  commit reordering `dC` exits 0. When `python plan_revision.py --selftest --plant goal-fork` runs, it
  reaches its re-entry and exits 0.
  Red when: a seeded fixture reads `item.plan.record unread` at its `plan.exit` move.
- **AC2** — When the plants `claude-adapter`, `pre-placement` and `fallback-reentry` of `python ratify.py
  --fixture` run at this unit's tip, each admitting move exits 0, and the `pre-placement` variant of
  `plan-record-absent` exits 1.
  Red when: unit 10 AC6 and unit 19 AC2 cannot both hold.
- **AC3** — When `grep -c "read_plan_ratification" plan_revision.py` runs over the loop kit's module at
  this unit's tip, it prints 0.
  Red when: a stub of the predicate is left in any plant.
- **AC4** — When `python plan_revision.py --selftest --plant reentry-later-session` runs, `show` in the
  second process prints `ratified · witness` and exits 0.
  Red when: `show` re-asks the real predicate, which answers no witness in that process.
- **AC5** — When `python ratify.py --check-callers` runs over this repository at this unit's tip, it
  exits 0. On a scratch clone whose copy of `tools/memory-tree/gen_build_index.py` carries one
  `read_plan_ratification(` call, it exits 1 naming that file.
  Red when: a caller is left in the tree, or a planted caller passes.
  fixture: the clone sits under a short `%TEMP%` path.
- **AC6** — When the plant `goal-fork` runs to its re-entry, `show` prints `revision — 1 · ratified ·
  witness · harness`.
  Red when: the line keeps unit 15 AC1's `ratified · request` form.
- **AC7** — When the plant `codex-reentry` runs its second move with `--field harness=codex`, the
  admitted trailer carries `harness=codex`. When `ratify.py tFix --exited` runs after `claude-adapter`'s
  move with `--field harness=claude-code`, it prints `harness claude-code`.
  Red when: a move's harness never reaches the trailer the reader reads.
- **AC8** — When `python scenario.py --fixture --plant plan-new-first` runs, the claim's first move
  into `planning` exits 0 and its trailer carries `scenario=scenario.feature`.
  Red when: a `new` build's first move is stopped by the no-record exit.
- **AC9** — When `bash tools/unattended/unattended.sh --status dRankedPlan` runs at this unit's tip,
  either every mapping record of `TOOL-dRankedPlan-5` ends its `Reason` with `ratified <value>
  <witness>`, or the run-state file holds a `decision · item TOOL-dRankedPlan-5` row.
  Red when: unit 5 closed with records and no witness, or was held by a refused `--hold`.
- **AC10** — When `bash tools/check-install-prefix.sh --offenders` runs at this unit's tip, no key it
  prints names the loop kit's `ratify.py`.
  Red when: the predicate's allowlist spells a literal kit path.
- **AC11** — When a probe reads `tools/gate-legs.json`, the `build-index selftest` guard holds the
  loop kit's `ratify.py`, and the `loop selftest` guard holds the memory-tree kit's `plan_record.py`
  and `plan_fields.py`, each under `{prefix}` as S13 spells it. Each kit's `[[gate_leg]]` entry carries
  the same guard, and `python tools/run-gates/leg_factory.py --check` exits 0.
  Red when: a suite reads a sibling kit file its leg's guard does not name, or a guard is widened in
  the manifest alone.
  fixture: `leg_factory.py` lands with TOOL-dWitnessedBar-11; before it, the two reads are compared.
- **AC12** — When the plant `reader-bound` runs its `merged-add` case, the record from the branch
  forked after the newest transition is kept and the one forked before it is not. `grep -c
  "diff-filter=A" ratify.py` over the loop kit's module prints 1.
  Red when: a merge-delivered record is dated by the merge, or a second adding-commit read appears.
- **AC13** — When `grep -c -- "--priority <n>" tools/unattended/unattended.test.sh` runs, it prints at
  least 2.
  Red when: a recipe check stays green with the flag dropped.
- **AC14** — When `python ratify.py --fixture --plant caller-shell-bare` runs, the check exits 1
  naming `.githooks/pre-commit`. When the plant `caller-shell-exit` runs, the check exits 0.
  Red when: a bare shell call of the predicate's CLI passes, or a continued `--exit` call is refused.
- **AC15** — When the `drafts-cross-session` plant runs with the forged newer `before-placement` move
  for `dA`, the commit putting `dB` before `dA` still exits 1.
  Red when: a later crossing with no owner act de-ratifies a row.
- **AC16** — When `grep -c "697"` and `grep -c "695"` run over
  `memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md` at this unit's tip, they
  print 0 and at least 2.
  Red when: the spec still states the figure measured at a later commit.
  figure: 695 is PINNED at `0689e7fa1`, measured by unit 29 S16 on 2026-10-27.
- **AC17** — When `grep -c "read_item_disposition" memory/builds/dDeclaredLoop/BACKLOG.md` runs at this
  unit's tip, it prints at least 1.
  Red when: the second reader of the record kind stands with no ask filed.
- **AC18** — When `python plan_revision.py --selftest --plant before-placement-reentry` runs, `show`
  prints `admitted · before-placement · no owner act` and exits 0.
  Red when: a crossing no owner act gated reads as ratified to `show`.
- **AC19** — When a probe calls `check_repo_relative_path` from `tree_lib.py` with `/abs`, `C:/x`, `~/x`
  and `a/../b`, each raises. When `gen_build_index.py --asks --path ~/x` runs, and when the routed
  commits reader takes a `ROUTED_PATHS` entry `~/x`, each refuses.
  Red when: the three callers disagree on any of the four shapes.
- **AC20** — When `python tools/memory-tree/gotchas.py --for-paths tools/roles/kit.toml` runs, it lists
  `a-version-claim-names-the-descriptor-not-its-carrier`.
  Red when: the trap is not handed to the next editor of a kit descriptor.
- **AC21** — When the plant `reader-bound` runs its `untracked` case, with a transition and without
  one, `read_item_disposition` returns `None` and its `why` reads `disposition <path> not committed`.
  Red when: an uncommitted record is kept, or held with no reason.

## 7. Gates

`build-index selftest` · `routed-commits selftest` · `gotchas selftest` · `unattended kit gate` · `tier2-review self-test` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/plan_revision.py · covers AC3 AC4 AC6 AC18 · the de-stubbed plants, `reentry-later-session` in a second process and `before-placement-reentry`, staged by a `show` that asks `read_plan_ratification` · none

New arm: tools/loop/ratify.py · covers AC12 AC14 AC21 · `merged-add`, `untracked`, `caller-shell-bare` and `caller-shell-exit`, staged by a reader that dates by `git log --diff-filter=A -1` and keeps an untracked record · none

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC15 · `drafts-cross-session` seeded and carrying the forged trailer, staged by an order check that reads the newest crossing only · none

New arm: tools/loop/scenario.py · covers AC8 · `plan-new-first`, staged by a check that exits 2 on a build with no prior record · none

New arm: tools/unattended/unattended.test.sh · covers AC13 · the two recipe checks, staged by a recipe printed without ` --priority <n>` · none

New arm: tools/memory-tree/routed_commits.py · covers AC19 · its self-test's `ROUTED_PATHS` refusal of `~/x` through the shared helper, staged by a helper that admits `~` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 19 to 29: its 17 MEDIUM and
  8 LOW findings, ids 1 2 3 4 5 7 8 9 11 12 13 14 16 17 18 22 23 24 25 27 31 32 33 34 35, batched
  under BUILD-METHOD M4.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-42`, the hands-off edge to `TOOL-dRankedPlan-45`, each the reciprocal of that promoted unit's own edge (spec audit of units 30 to 37, `reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-61`, each the reciprocal of that promoted unit's own edge (spec audit of units 46 to 52, `reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`); no other section moves.
- rev-4 · 2026-10-28 · §2 S1, S13, S17 · §4 Evidence, Files touched · §6 AC11 · re-grounded by the cross-check record `build/2026-10-28-build-TOOL-dRankedPlan-1-parents-crosscheck.md`, rows 60 and 61: guards widen in each leg's one `[[gate_leg]]` declaration and `tools/gate-legs.json` is rendered by `leg_factory.py --write` (TOOL-dWitnessedBar-11 S1, S2), hand-written as the stand-in until that unit lands; the generator and its plant run the loop kit's CLIs as subprocesses and import none of its modules (PLAY-dOrderedCharter-7 §4), S17's ratified set read through `--exited`'s verdict.

## 10. Reuse audit

Each item extends the seam its finding names rather than minting one. S1 reuses
`TOOL-dRankedPlan-33`'s seed. S17 extends `TOOL-dRankedPlan-21`'s reader beside
`read_exit_ratification`. S22 imports `RATIFYING_EXITS` from its one home. S23 moves
`check_repo_relative_path` into `tree_lib.py` (`tools/memory-tree/tree_lib.py`), the module
`routed_commits.py` already imports (:73). S24 points at the `version_from` carriers. `python
tools/codebase-map/reuse_lookup.py "refuse a path that is absolute, has a drive letter, a tilde or
climbs with dot dot"` ranked name stems only (`has`, `CensusRefused`, `build_spec_path_re`), none a
path refusal, so no seam fits beyond the three copies S23 joins. The recall query returned
`TOOL-dRankedPlan-29`'s reuse audit and the dKeptSession batch specs, and they agree on the batch form.

Recall terms used: `python tools/memory-recall/query.py "which minor findings of the second dRankedPlan spec audit land on which unit" --terms "spec audit minors batch plan_revision stub read_exit_ratification guard sibling kit recipe priority version carrier gotcha"`
