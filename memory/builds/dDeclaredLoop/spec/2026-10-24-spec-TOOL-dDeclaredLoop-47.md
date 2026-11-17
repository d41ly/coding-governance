# TOOL-dDeclaredLoop-47 — the stage factory writes a whole conforming stage: its witness, exit item, state and table rows

**Status:** WONTDO · rev-3 · 2026-11-15 · node d · Tier-2 · base ed497191 · streams tooling · order 21 · advances TOOL-dDeclaredLoop-35 · superseded by TOOL-dDeclaredLoop-25, whose splice.py new is the stage factory (§8 F3)

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-47-deviation-471.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-47-deviation-471.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-47-deviation-472.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-47-deviation-472.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-47-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-47-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-47-reground-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-47-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`)
confirmed finding **id 3 at HIGH**, its item **H3**, alone in that item: `TOOL-dDeclaredLoop-6`'s
stage factory wrote a gov `[[step]]` row alone, which the `loop definition` leg's checks refuse. The
audit gave two fixes: a factory writing the whole stage, or the kind narrowed to what a factory can
make conform. Rev-2 of this unit took the first, a gov step factory over `tools/loop/loop.toml`.

That factory cannot be built over the branch tip. `tools/loop/loop_lib.py#check_loop` refuses a
`[[step]]` row whose tag is not in `tools/loop/loop_lib.py#STEP_TAGS`, gov's five, and clause 0110
keeps those five whole and in order. `TOOL-dDeclaredLoop-6`'s committed rev-5 therefore writes no
stage factory (its §8 F4 (b), deviation 64), and `TOOL-dDeclaredLoop-25`'s committed rev-5 lands the
stage kind's factory as the repository stage, `splice.py new` run through `core.py new stage`, which
writes the stage row and its exit item to the overlay and grades both before any write. That is the
audit's second fix. Under §8 F3 (a), the recommendation this body is written on, no mechanism is left
for this unit, and it carries none to a builder.

## 2. Scope (IN)

Each item of rev-2 is settled here against the tip of branch/unattended-declared-loop-d56bf0 at
`b8215d6ef`. None is carried to a builder (§8 F3).

- **S1** — The gov stage that `new stage <name> --order <n> --state <state> --after <step tag> --exit
  <item tag>` was to write into `tools/loop/loop.toml`, a `[[step]]` row with its witness, its exit
  `[[item]]` row and its `[states]` entry, is not built: `check_loop` refuses any step tag outside
  `STEP_TAGS`, so the `loop definition` leg reds every such stage (§4 "Evidence"). The stage a factory
  writes is `TOOL-dDeclaredLoop-25` S8's repository stage, its `[[stage]]` row and its exit item
  `item.adopter.<name>.exit` with a `history` witness, written to the overlay.
  NOT OBSERVED: this unit builds nothing; the `factory` case of `TOOL-dDeclaredLoop-25`'s fixture
  observes that factory's instance.
- **S2** — The two transition rows inserted after `--after` by `derive_inserted_rows` in
  `tools/loop/factories.py` are not built. A repository stage's rows are derived at composition by
  `TOOL-dDeclaredLoop-25` S2's `derive_splice_rows`, R1 into the stage's state and R2 out of it, the
  state derived as `adopter-<name>` and never typed, and gov's `loop.toml` is never edited.
  NOT OBSERVED: this unit builds nothing; `TOOL-dDeclaredLoop-25`'s `between-test-deploy` case
  observes the derived rows.
- **S3** — A factory gate running `python tools/loop/loop_lib.py --check` and `python
  tools/loop/loop_table.py check` is not built. Both read gov's `loop.toml` only, through
  `tools/loop/loop_lib.py#read_definition`, which the stage factory never writes, so neither can red
  on its instance. The checks that hold a repository stage run before its factory writes:
  `check_splices`, `check_program`, `check_witness_classes` and `check_item_declarations`, as
  `TOOL-dDeclaredLoop-25` S8 states.
  NOT OBSERVED: this unit builds nothing; the `factory` case of `TOOL-dDeclaredLoop-25`'s fixture runs
  `splice.py check` and `loop_items.py check` over the factory's committed rows.
- **S4** — The `stage-new` and `stage-hand` plants restating `TOOL-dDeclaredLoop-6`'s stage criterion
  are not built: that unit's committed rev-5 writes no stage factory and keeps the stage kind pending
  (its S10). A hand-made repository stage that does not conform is planted by
  `TOOL-dDeclaredLoop-25`'s `exit-elsewhere`, `exit-unwitnessed` and `orphan-item` cases.
  NOT OBSERVED: this unit builds nothing; those cases observe it.

## 3. Non-goals (OUT)

- Every mechanism this unit's rev-2 named: the gov step factory, `derive_inserted_rows`, its two
  plants and its arm in `tools/loop/factories.py` (§8 F3).
- The repository stage, its factory, its frame check and its plants: `TOOL-dDeclaredLoop-25`'s.
  This unit adds no flag, check or case to them.
- A factory gate re-running the composition after `splice.py new` writes: §8 F3's option (b).
- A gov `[[step]]` row from any factory: `check_loop` closes gov's steps, and clause 0110 keeps them
  whole (`TOOL-dDeclaredLoop-6` §8 F4).
- Restoring created files and SIGINT handling in the factory contract: the round-1 audit's id 59,
  batched into `TOOL-dDeclaredLoop-56`.
- A factory selftest arm running every check of every gated leg over each kind's fresh instance, H3's
  left-shift: not a clause of this build.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-6` — its §8 F4 (b): the stage kind's register row left pending and no factory writing a gov `[[step]]` row, the ground of this unit's §8 F3
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 6, 44 and 54, which read the gov step factory this rev does not carry; that unit's own re-ground settles them

## 4. Design

### Evidence

Every claim below was read at the tip of branch/unattended-declared-loop-d56bf0, `b8215d6ef`, by
`git show`, since this writer's worktree is cut from main and lacks the loop kit.

- `tools/loop/loop_lib.py#STEP_TAGS` is the closed tuple of gov's five steps.
  `tools/loop/loop_lib.py#check_loop` refuses a step row naming any other tag, a repeated tag, a
  missing one and a row out of order.
- `tools/loop/loop_lib.py#check_program` refuses an item whose tag opens no `item.<step>.` of a gov
  step, so the exit item of a non-gov step is refused even beside a step row.
- Clause `cl-dClosedLoop-0110` keeps gov's five stages whole and in order and makes a repository's
  own stage an overlay row
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md@7751111bb776:118`).
- The register's `kind.stage` row carries `factory = ""` and its pending row names dDeclaredLoop
  (`tools/playbook/kinds.toml@3d09af84a8cc:135`, `tools/playbook/core-pending.txt@ec2abc1ac349:236`).
- `tools/loop/factories.py` and `tools/loop/splice.py` are absent at the tip; both are specced and
  unbuilt.
- `tools/loop/loop_lib.py#read_definition` reads `loop.toml` beside the kit, and
  `tools/loop/loop_table.py#main`'s `check` reads the same definition; neither reads the overlay.
- `TOOL-dDeclaredLoop-6`'s committed rev-5: S10 keeps the stage kind's row and pending row, §3 writes
  no gov `[[step]]` row from any factory, and §8 F4 resolved (b), deviation 64 recording the stage
  factory's move to `TOOL-dDeclaredLoop-25`.
- `TOOL-dDeclaredLoop-25`'s committed rev-5: S1 fills `kind.stage` with a `[[stage]]` overlay row and
  takes its pending row; S8 is the factory; its §5 names this unit's `kind.splice` and `[[splice]]`
  as names its own re-ground reads.

### Where each part of the rev-2 stage lands

| Rev-2 part | At the tip | Where it lands |
|---|---|---|
| the `[[step]]` row with a `history` witness | refused by `check_loop` | not built; `TOOL-dDeclaredLoop-25`'s `[[stage]]` overlay row |
| the exit `[[item]]` row | refused by `check_program` for a non-gov step | `item.adopter.<name>.exit`, built by `derive_new_item_row` |
| `--state` in `[states]` | a sixth step's state has no step | `adopter-<name>`, derived by `derive_stage_state` |
| the two rows of `derive_inserted_rows` | would edit gov's table | R1 and R2 of `derive_splice_rows`, at composition |
| the gate of both definition legs | those legs never read the overlay | the in-memory grading of `TOOL-dDeclaredLoop-25` S8 before any write |
| the `stage-hand` plant | no gov step to plant | the `exit-elsewhere`, `exit-unwitnessed` and `orphan-item` cases |

### Files touched (estimate)

None. This unit builds nothing under §8 F3 (a).

### Alternatives rejected

- **A gov step factory opening `STEP_TAGS`.** §8 F3 (c): it fails clause 0110.
- **A post-write gate on the repository stage's factory.** §8 F3 (b): the same predicates run twice,
  and an order this pass may not move.

## 5. Production-readiness checklist

- security — N/A: no write path, surface or grant is added.
- perf / scale — N/A: no code runs.
- error / empty / loading states — N/A: no code runs.
- observability — N/A: no code runs.
- risks — the run keeps this unit at DEFERRED and dispatches a builder with nothing to build, where
  §8 F3 is not resolved before this unit's turn. Unit 67's S9 and S32 read the gov step factory and
  stay unbuildable until that unit's own re-ground.
- testing — N/A: no arm is added or moved.
- migration — N/A: nothing is written.
- user docs — N/A: no `help/` page changes; `help/loop.md`'s stage section is `TOOL-dDeclaredLoop-25`'s.
- the write set, checked against what the change touches: no registry row in
  `tools/govkit/registry.toml`, no usage row in `tools/govkit/usage.toml`, no subject pin in
  `tools/govkit/subject-pins.tsv`, no entry of the verdict epoch's delegate list, no file on the kickoff
  manifest's watch list, no generated map file and no line the install-prefix ban reads. No existing
  fixture or selftest arm reads anything this unit writes, since it writes nothing.
- dependencies — §8 F3 rests on the committed rev-5 specs of `TOOL-dDeclaredLoop-6` and
  `TOOL-dDeclaredLoop-25`, which are being built or next. Where unit 25's S8 or its fixture's `factory`
  case changes at its build, F3 (a) reads the landed spec. No edge to `TOOL-dDeclaredLoop-25` is
  declared: this unit takes nothing from it and leaves it nothing. `TOOL-dDeclaredLoop-14`'s committed
  spec takes the `principle.p24` row of `tools/playbook/core-pending.txt`, above the `kind.stage` row,
  so that row's line moves; §4 cites it at its blob, and the row's content holds. `TOOL-dDeclaredLoop-4`
  reads `check_loop` and `STEP_TAGS` and changes neither. Units 45, 69, 78, 46, 81, 83 and 85 change
  no code this spec reads.

## 6. Acceptance criteria

N/A — under §8 F3 (a) this unit builds nothing, so no observation of its own code exists; the
repository stage's criteria are `TOOL-dDeclaredLoop-25`'s.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

No arm is added or moved: the unit builds nothing under §8 F3 (a).

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — A whole stage, or a narrower kind?** Options: (a) the factory writes the whole stage; (b) the
  kind narrowed to what a factory alone can make conform. (b) has no member: a step row cannot conform
  without its item, state and rows. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none
  · relaxes: none
- **F3 — With no gov stage a factory can add, what does this unit carry?** F2's pick read a gov step,
  and the narrowed kind it found memberless is now `TOOL-dDeclaredLoop-25`'s repository stage.
  (a) Nothing: H3 is answered by `TOOL-dDeclaredLoop-25` S8, whose factory writes the stage row and its
  exit item, derives the state and the rows, and grades them under every check that holds them before
  any write; the run resolves this fork, moves the spec to WONTDO with `TOOL-dDeclaredLoop-25` as its
  successor pointer, and writes the record that move owes, as deviation 64 records unit 6's.
  (b) This unit re-targeted as a post-write gate on `splice.py new`: after the factory appends its
  tables, run `splice.py check` and `loop_items.py check` and restore the overlay through the guarded
  write on a red. The factory already writes nothing on a refusal, so the gate re-runs predicates the
  factory ran, two answers to one question; it consumes code `TOOL-dDeclaredLoop-25` builds at the same
  order 21, so it needs an order after that unit's, which this pass may not move; and its edge to that
  unit stays one-way until that unit writes the mirror.
  (c) Rev-2's gov step factory, `STEP_TAGS` and `check_loop`'s five-step rule opened for it. It fails
  clause 0110, gov's five kept whole and in order, and `TOOL-dDeclaredLoop-6`'s resolved F4: the build
  method's first veto.
  Recommendation (a), the body's: (c) is vetoed, (b) is a second answer and an order move, and (a)
  leaves H3 closed by the unit that owns the stage kind.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: (c) breaks clause 0110 and (b) re-runs checks unit 25's factory already runs, so the unit carries nothing and TOOL-dDeclaredLoop-25 supersedes it
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 3 (HIGH, item H3).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-15 · §1 · S1 S2 S3 S4 · §3 · §4 · §5 · §6 · §7 · §8 F3 · §10 · re-grounded at
  `b8215d6ef`, the tip of branch/unattended-declared-loop-d56bf0, by the brief
  2026-11-15-prompt-TOOL-dDeclaredLoop-47-1-spec-writer; carries, order and status kept. The gov step
  factory cannot be built: `check_loop` closes gov's steps and clause 0110 keeps them whole, unit 6's
  rev-5 writes no stage factory, and unit 25's rev-5 lands the stage kind's factory as the repository
  stage. Every scope item is settled against unit 25's S1, S2 and S8 and built by none here; the
  criteria and the arm leave with them; F3 records the fork, recommending (a). The audit's file is
  cited by its tracked name.

## 10. Reuse audit

The seam is `TOOL-dDeclaredLoop-25`'s stage factory, `splice.py new` under `core.py new stage`, which
answers this unit's finding; no code is added here to extend it. `python
tools/codebase-map/reuse_lookup.py "a factory that writes a stage and its exit item so they conform
under the loop checks"`, run on 2026-11-15 over the tip of branch/unattended-declared-loop-d56bf0
extracted to a scratch directory, ranked generic `write` and `check` stems, `LoopError` and
`tools/loop/loop_lib.py#read_item_rows`, none a stage writer; the item kind's factory,
`tools/loop/loop_items.py#run_new`, is the row builder unit 25 extracts. The recall query's first
hits were unit 25's scout row, unit 6's §8 F4 and unit 25's non-goal on a gov `[[step]]` row.

Recall terms used: `python tools/memory-recall/query.py "can a factory add a stage to the loop that
conforms" --terms "stage factory gov step STEP_TAGS check_loop repository stage splice kind.stage exit
item conform H3"`
