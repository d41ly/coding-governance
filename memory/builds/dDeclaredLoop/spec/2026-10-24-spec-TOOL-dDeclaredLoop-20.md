# TOOL-dDeclaredLoop-20 — the breakpoint program's own items: trigger, dispose, fold and cost, and the four keys `review.dispose` reads

**Status:** INPROGRESS · rev-5 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 31 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0105@cab8e16c whole

**Carries:** node:item.review.trigger

**Carries:** node:item.review.dispose

**Carries:** node:item.review.fold

**Carries:** node:item.review.cost

**Carries:** node:policy-key.review.blocks

**Carries:** node:policy-key.review.unverified

**Carries:** node:policy-key.review.left-shift

**Carries:** node:policy-key.review.findings

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 |
| [2026-11-05-build-TOOL-dDeclaredLoop-1-reground-returns.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-1-reground-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 |
| [2026-11-05-build-TOOL-dDeclaredLoop-20-deviation-201.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-20-deviation-201.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-20-deviation-202.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-20-deviation-202.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-20-red-fix-49.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-20-red-fix-49.md) | red-fix | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-20-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-20-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-20-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-20-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-20-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-20-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

A reviewer breakpoint runs one program: dFairHearing builds `review.pin` to `review.report`, and this unit
builds the four items around them, `review.trigger`, `review.dispose`, `review.fold` and `review.cost`,
with the four keys `review.dispose` reads, `review.blocks`, `review.unverified`, `review.left-shift` and
`review.findings` (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@d73cb002:569-576`).
Today disposal is fixed in code and prose. The driver's `tools/unattended/unattended.sh#verb_review` owes
one unit per blocker and high plus one for the minors, and check 2 of
`tools/unattended/check-unattended.sh` grades the same floor
(`tools/unattended/check-unattended.sh@dd64dc59:1180-1188`). The build harness's DISPOSAL stage promotes
every unverified finding it does not refute and bounds its units by the same rule
(`tools/workflows/unattended-build.template.js@a017fd13:2691-2705`). The stand-in
`tools/workflows/review_pin.py#main` takes `review.opt-in`, `review.unclassed`, `review.twin` and the two
`review.design-audit.*` values as flags a caller types.

## 2. Scope (IN)

- **S1** — The item rows' content. §4 "The item rows" is the table `TOOL-dDeclaredLoop-50` writes into
  `tools/loop/loop.toml`, in the landing that admits the review program's step and declares
  `item.review.pin` and `item.review.report` (§8 F4). Until that landing,
  `tools/loop/loop_lib.py#check_program` refuses an `item.review.*` tag, and every reader of the item
  table runs that check through `tools/loop/loop_lib.py#read_items`. This unit writes no `[[item]]` row.
  NOT OBSERVED, because the rows land with that unit.
- **S2** — `review.trigger`, the verb `--trigger <slug> --subject <s> --cause <c> [--pin <path>]...`,
  `run_trigger` in `tools/unattended/unattended.sh`. `<c>` is one of `owed`, `opt-in`,
  `recommendation`, `placement`. It refuses a subject whose loop already ended, by the predicate
  `verb_review` uses, lifted into `check_review_ended` so both call it. It reads the four keys of S11
  through `load_review_bounds` and the five pin flags through `review_bounds.py pin`. With a `--pin`, it
  runs `tools/workflows/review_pin.py` with one `--subject` per pinned path and those flags, and prints
  each line it prints with `trigger` and `reviewPolicy` added. With none, a diff review's call, it prints
  one line of `unclassed`, `twin`, `trigger` and `reviewPolicy`. No caller types a pin value. Observed by
  AC2, AC3.
- **S3** — `review.cost`. `renderShapeLine` in `tools/workflows/tier2-review.template.js` appends
  `trigger=`, `shape=`, `efforts=` and `role-sha=` after `out-tokens=`. The harness takes `trigger` as an
  argument checked in S2's closed set beside `unclassed`, absent printing `-`; the other three print `-`
  until dBoundRoles lands its shape registry. The build harness forwards a caller's `trigger` to its
  audit call as it forwards `unclassed`. Observed by AC4.
- **S4** — `review.findings` decides the promotion count, with its three values: `blocker-high-own`, the
  default and today's rule, one unit per blocker and per high and the minors batched; `all-own`, one unit
  per finding; `blocker-own`, one unit per blocker and every other finding batched. `derive_owed_units`
  computes both owed counts `verb_review` takes, and a terminal exit's row records ` · findings <value>`
  before its target where the value is not the default. Check 2 computes its floor from that field, an
  absent one reading the default. The DISPOSAL stage's unit floor and ceiling compute from
  `reviewPolicy.findings` through `deriveUnitBounds`. Observed by AC5, AC6.
- **S5** — `review.unverified`, with its three values: `ask`, the default, each unverified finding the
  DISPOSAL stage does not refute filed as an ask with its evidence and never promoted; `block`, each one
  adjudicated by the stage and promoted at the severity it reads or refuted, today's route (§8 F6);
  `record`, each one listed in the stage's summary and nothing filed. The stage returns the count its
  `ask` or `record` route took as `routed`, which joins the reconciling sum, and the count of promoted
  unverified findings, `adjudicated`, reads 0 under both. Observed by AC6.
  **Readers:**
  by name: `tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js`, `tools/workflows/unattended-build.test.sh`
  by value: `tools/unattended/check-unattended.sh`, whose check 2 counts the `--minors` the stage's record line carries, which adds only promoted unverified findings
- **S6** — `review.left-shift`, with its three values: `second-occurrence`, the default, a `class:<slug>`
  disposition whose slug a prior review record already disposed earns a gate; `every-class`, every
  `class:` and `new:` disposition earns one; `owner-selects`, each candidate an owner item.
  `measure_class_occurrences` in a new `tools/workflows/review_dispose.py` counts by the appendix's
  disposition column, read through `tools/workflows/replay_scorer.py#parse_appendix_rows`, and its
  `classes` verb prints the earned gates. The DISPOSAL stage runs it and files each earned gate as an
  ask. Observed by AC7.
- **S7** — `review.blocks`, with its three values: `every-review`, the default and today's, the roster
  held until the review's verdict is terminal; `owed-only`, held only when the trigger cause is `owed`;
  `none`, never held. The trigger folds the value and the cause into `reviewPolicy.blocks`, `yes` or
  `no`. The build harness takes `reviewPolicy` as one argument and refuses an object missing a key or
  carrying a value outside its set. Under `no`, its CONVERGING return carries the roster where it now
  carries `[]`, and its log names the review as running alongside. Observed by AC8.
- **S8** — `review.fold`, the in-loop fold of an unbuilt spec, keeps its mechanism: the build harness's
  CONVERGING `nextAction` gains the item's tag `item.review.fold` and the spec subject's terminal states,
  BOUNDED or CEILING. A spec subject takes `no-fall` (`TOOL-dDeclaredLoop-32` S3) and ends at its target
  or its bound, never NON-CONVERGENT. Observed by AC1.
- **S9** — BUILD-METHOD M4's DIFF-exit disposal sentence, in `tools/memory-tree/BUILD-METHOD.template.md`
  and its render `memory/guides/BUILD-METHOD.md`, points at `review.findings` for the count and at
  `review.unverified` for an unverified finding's route, its default reading unchanged. Its SPEC-exit
  promotion sentence points at the DIFF exit's, so one count governs both. The render stays at or under
  its `build-method size` row (§4 "The method's text"). Observed by AC9.
- **S10** — The suite arms the `New arm:` lines in §7 declare. Observed by AC1, AC2, AC4, AC5, AC6, AC7,
  AC8 and AC10 through those lines, RED first at the close.
- **S11** — The keys' one reader. `tools/loop/review_bounds.py` reads the four `review.dispose` keys
  beside its five, each through the policy kit's `resolve`; `show` prints `findings=`, `unverified=`,
  `left-shift=` and `blocks=` after `route-backs=`. Its `pin` verb prints the five flags `review_pin.py`
  takes for `review.opt-in`, `review.unclassed`, `review.twin`, `review.design-audit.runs` and
  `review.design-audit.seed`, and refuses a non-empty `review.opt-in` (§8 F5). The driver's
  `load_review_bounds` reads the four new fields, with kit defaults where the module does not resolve.
  Observed by AC10.
- **S12** — The carriers. `tools/unattended/VERBS.template.md` gains a `--trigger` entry,
  `tools/unattended/SKILL.template.md` the invocation in its fenced verb list, and the driver's header the
  verb's line with `--cause` and `--pin`; `VERBS_SLUG` gains the verb and `VERB_REQUIRES` the row
  `--trigger --subject --cause`. `help/loop.md` gains a section on the review program's disposal that
  anchors `verb:unattended.sh:--trigger` and states the four fields `show` prints. `tools/workflows/README.md`
  states `trigger`, `reviewPolicy`, the record line's fields and `review_dispose.py`. Renders are their
  templates' copies. Observed by AC11.

## 3. Non-goals (OUT)

- `review.pin`, `review.lens`, `review.refute` and `review.report`, and the report's disposition grammar:
  dFairHearing's, called here and never re-specced.
- The `[[item]]` rows themselves, the step admission and the two upstream rows: `TOOL-dDeclaredLoop-50`'s
  (§8 F4).
- The round bound and the route-back exit: `TOOL-dDeclaredLoop-21`'s `review.max-rounds` and
  `TOOL-dDeclaredLoop-32`'s routing. `review.trigger` refuses on the terminal state those leave, and adds no
  bound of its own.
- Where a breakpoint sits and who disposes it: `TOOL-dDeclaredLoop-19`'s `review.breakpoints`,
  `review.<stage>` and `autonomy`, which set the trigger cause this unit records.
- The disposition set of a placement or an owner (`TOOL-dDeclaredLoop-16`): the round's `fold|promote` and the
  report's `class:`, `new:`, `gate:`, `none` are different vocabularies, and this unit reads the second.
- A patch-build intake for an earned gate. The intake is a later build's; until it lands, an earned gate is
  filed as an ask, which is the item's stand-in.
- Disposal of a plan revision or a landing record: no plan record or landing-review record exists in this
  tree. Their routes are declared on the `review.dispose` row and are a later build's to arm.
- A verification round that re-runs the skeptic under `block`: the driver takes no round on an ended
  subject (§8 F6).
- Keying the class count by distinct review: `TOOL-dDeclaredLoop-56`'s, its id 64.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-21` — `review.max-rounds`: the terminal state `review.trigger`
  refuses on, and `review_bounds.py`, the module S11 extends
- **consumes-from** `TOOL-dDeclaredLoop-32` — `flow.route-backs`: the route-back exit `review.trigger`
  refuses past on the build slug, and the target `review.dispose` promotes by, ` · to units` or
  ` · to asks` on built work and always ` · to units` on a spec subject
- **hands-off** `TOOL-dDeclaredLoop-19` — `review.dispose`: the breakpoint's disposal, which a review
  breakpoint runs and whose trigger cause `TOOL-dDeclaredLoop-19` sets
- **hands-off** `TOOL-dDeclaredLoop-50` — the review program's item rows made to pass the program and declaration checks (the round-1 spec audit's id 2), written from §4's table
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 32, 64, each a scope item of that unit; id 32's reader holds here already

## 4. Design

### The item rows

The content `TOOL-dDeclaredLoop-50` writes, each row with step `none`. The actors take
`TOOL-dDeclaredLoop-9`'s grammar in the tag-derived form the program's command rows use, as
`item.plan.recommend` reads `command:plan.recommend`; that unit adds the inputs, allowance and returns a
non-role actor carries, and sets the outcome words and route targets `check_program` and the build
table's route join admit.

| Tag | Actor | Needs | Witness | Routes | Reads |
|---|---|---|---|---|---|
| `item.review.trigger` | `command:review.trigger` | none | the trigger line `--trigger` prints, joined to the review record's `trigger=` field | fired to `item.review.pin`; a round past `review.max-rounds`, or on the build slug past `flow.route-backs`, refused, its open findings to `item.review.dispose`; not fired, the flow continues | `review.blocks`, `review.opt-in`, `review.unclassed`, `review.twin`, `review.design-audit.runs`, `review.design-audit.seed`, `review.max-rounds`, `flow.route-backs` |
| `item.review.dispose` | `command:review.dispose` | `item.review.report` | each confirmed finding joined to its fold, unit or ask | a local finding on an unbuilt spec to `item.review.fold`; built work and a new mechanism to new units or asks by `review.findings`, the outcome `unit` the build table's B10 row fires on; NON-CONVERGENT or CEILING on built work promoted to units while budget remains and to asks after; a spec subject's new mechanism promoted by `TOOL-dDeclaredLoop-32`'s target, always units; a plan revision to `plan.record` and a landing record to its patch-build intakes, both declared and unarmed (§3); an unverified finding by `review.unverified` | `review.findings`, `review.unverified`, `review.left-shift`, `flow.rework-budget` |
| `item.review.fold` | `role:gov-spec-writer` | `item.review.dispose` | each confirmed finding joined to its fold at the spec's new blob, which the re-invoke's `prevSubjects` pins | the next round as `review.design.rounds` says, or released; BOUNDED or CEILING, the spec subject's terminal states, its new mechanism promoted as `item.review.dispose` promotes a spec subject's | `review.design.rounds` |
| `item.review.cost` | `command:review.cost` | `item.review.report` | the `review-shape` line's cost fields | done | none |

The dispose row keeps the owner `dDeclaredLoop`, which its `[[stand-in]]` row names
(`tools/loop/loop.toml@aea2a65c:900-902`), and the outcome `unit` that B10 fires on
(`tools/loop/loop.toml@aea2a65c:493-499`); `check_transition_tables` refuses a stand-in whose owner
differs from its item row's.

### The trigger

```
--trigger <slug> --subject <s> --cause owed|opt-in|recommendation|placement [--pin <path>]...
  check_slug, check_run_state, refuse_if_terminal, check_verb_flag for --subject and --cause
  a cause outside TRIGGER_CAUSES                                 -> fail 37
  check_review_ended "$rel" "$s"                                 -> fail 37, naming the subject
  load_review_bounds; review_bounds.py pin; with a --pin, review_pin.py --subject <p>... <flags>
    any of the three refusing                                    -> fail 37, relaying its first line
  blocks: yes under every-review, yes under owed-only when the cause is owed, else no
  print each pin line with "trigger": "<c>" and "reviewPolicy" added; with no --pin, one line
    {"unclassed": .., "twin": .., "trigger": .., "reviewPolicy": {"findings": .., "unverified": ..,
     "leftShift": .., "blocks": "yes"|"no"}}
```

`check_review_ended <run-state file> <subject>` is the pipeline `verb_review` runs today, lifted
unchanged into a function at its second caller. It answers a status and refuses nothing: each caller
spells its own `fail 37`, because check-arms finds a branch by its literal number, and `verb_review`'s
keeps its text and its route. The three refusals of a read share one site through one `_tr_why`. The
verb writes no row: a non-round row in the `review` kind would become the subject's last reason and hide
its terminal token from `review_last_reason`. A pin line is `json.dumps` output, so the two fields are
appended before its closing brace, each value a closed-set word. Under `whole-design` the pin prints one
line per run, and each takes both fields.

### The record line

```
review-shape kind=… round=… … agents=<n> out-tokens=<n|unknown> trigger=<cause|-> shape=- efforts=- role-sha=-
```

The four fields follow the existing ones, so a reader of today's line reads every field it read before.
`tools/workflows/replay_scorer.py#extract_stated_count` reads `confirmed=` alone. The harness checks
`trigger` beside `unclassed`, refusing a value outside `TRIGGERS` by name.

### The count

| `review.findings` | Owed under the `old` rule | Owed under `counted` or `folds`, `promoted` above 0 |
|---|---|---|
| `blocker-high-own` | `b + h + (m > 0)`, today's | `b + h > f ? b + h - f + (m > 0) : 1`, today's |
| `all-own` | `b + h + m` | `p`, every promoted finding its own unit |
| `blocker-own` | `b + (h + m > 0)` | `b > f ? b - f + (h + m > 0) : 1` |

`b`, `h`, `m`, `f` and `p` are the exit's blockers, highs, minors, folded and promoted. The owner's FL-B3
answer is the default: "As it is today, by default - BLOCKER and HIGH findings become their own units,
MEDIUM and LOW are batched" (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md@fd9c95cb:384`).
`derive_owed_units <value> <rule> <b> <h> <m> <f> <p>` prints the integer, and `verb_review` calls it at
both sites it computes `owe` today. The exit note names the value's rule: today's clause under the
default, "one per confirmed finding" under `all-own`, and "one per blocker plus one for the highs and
minors when any stood" under `blocker-own`. Under the default the integer and the note are today's.

A terminal row under a non-default value carries ` · findings <value>` after its counts and before
` · to <target>`, so check 2's ` · to asks · disposition ` match and its last-field disposition read keep
their positions. Check 2's two owe sites read that field and take the table's formula, an absent field
reading `blocker-high-own`, and its two floor sentences name the value's clause. Check 2 never reads the
policy file: the row records the value the driver applied.

`deriveUnitBounds(findings, counts)` in the build harness returns `{floor, ceiling}` over the stage's
`blockers`, `highs`, `minors`, `confirmedMinors`, `adjudicated` and `byNature`: under the default,
today's two expressions; under `all-own`, `blockers + highs + minors` for both; under `blocker-own`,
`blockers + (highs + minors > 0 ? 1 : 0)` and a ceiling of `blockers` plus two for the batch, plus
`adjudicated` by severity. The DISPOSAL prompt's batching sentences follow the value.

### The unverified route

Under `ask`, the DISPOSAL stage files each unverified finding it does not refute as an ask in the build's
`BACKLOG.md`, in the grammar `tools/unattended/lib-unattended.sh#asks_filed_in` reads, naming the report
id and the finding's evidence. Under `record`, it lists each in its summary and files nothing. Both
return their count as `routed`, an optional integer of `DISPOSAL_SCHEMA` read as 0 when absent. The
reconciling sum becomes `promoted + folded + refuted + routed + standing`, and the bound on `refuted`
becomes one on `refuted + routed`, at most `unverified`. Under `ask` and `record` a positive
`adjudicated`, a promotion above `confirmed`, is refused by name. Under `block`, the stage adjudicates as
today and `routed` must be 0.

### The left-shift count

```
python <prefix>/workflows/review_dispose.py classes --builds <memory root>/builds --record <report> --left-shift <value>
  review-dispose: gate <slug> · prior <n> · <value>[ · owner]      one line per earned gate
  review-dispose: skipped <path> · <why>                           a record the parser refuses, counted nothing
```

`measure_class_occurrences` reads every `*/reviews/*.md` under `--builds` through `parse_appendix_rows`
and counts each `class:<slug>` of the disposition column across records other than `--record`. It
answers one line per slug of `--record` that earns a gate under the value: under `second-occurrence`, a
slug with a prior count of 1 or more; under `every-class`, every `class:` and `new:` slug; under
`owner-selects`, every slug, marked `owner`. A `--record` the parser refuses exits 2 naming it. The
DISPOSAL prompt names the command, spelled under `{{TOOL_ROOT}}` as `DRIVER` is, and files each earned
gate as an ask naming the slug, the records and `item.review.dispose`.

### The hand-out gate

The build harness takes `reviewPolicy`, `{findings, unverified, leftShift, blocks}`, the object the
trigger prints, and refuses one missing a key or carrying a value outside its set, naming the key. An
absent `reviewPolicy` reads the four defaults, `blocks` reading `yes`, and logs that it did. Under
`blocks: 'no'` the CONVERGING return carries the roster the terminal hand-out renders, over the units the
spec stage committed, and logs `the review runs alongside`; its `nextAction` still orders the fold.

### The method's text

The render measures 30714 bytes (PINNED, at `02524cadf`) against its row of 30720
(`tools/template-size-limits.txt@1ff70a75:136`), which the owner ruled is theirs to raise. So the pointer
is paid for in the same section. The DIFF-exit sentence's tail `never one per minor.` becomes `never one
per minor (`review.findings` can change that count; `review.unverified` routes an unverified finding).`
The SPEC-exit sentence `A NEW MECHANISM finding is PROMOTED: a BLOCKER or HIGH to its own unit, a MEDIUM
or LOW batched into one unit, two across disjoint write sets.` becomes `A NEW MECHANISM finding is
PROMOTED as at a DIFF exit.` The render then measures 30718 bytes (DERIVED, by the commands in §5).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `--trigger` | driver verb | flag, none |
| `--cause`, `--pin` | driver flags | flag, none |
| `run_trigger`, `check_review_ended`, `derive_owed_units` | bash functions | `sh.function`, verb-first |
| `TRIGGER_CAUSES`, `REVIEW_FINDINGS_DEFAULT`, `REVIEW_UNVERIFIED_DEFAULT`, `REVIEW_LEFT_SHIFT_DEFAULT`, `REVIEW_BLOCKS_DEFAULT` | driver constants | none |
| `read_review_pin`, `render_pin_flags` | Python functions, `tools/loop/review_bounds.py` | `py.function`, verb-first |
| `pin` | `review_bounds.py` verb | none |
| `measure_class_occurrences` | Python function, `tools/workflows/review_dispose.py` | `py.function`, verb-first |
| `classes` | `review_dispose.py` verb | none |
| `deriveUnitBounds` | JavaScript function, the build harness | `js.function`, verb-first |
| `reviewPolicy`, `trigger`, `routed`, `TRIGGERS` | harness arguments, a return field and a constant | none |
| `trigger=`, `shape=`, `efforts=`, `role-sha=` | `review-shape` fields | none |
| `findings=`, `unverified=`, `left-shift=`, `blocks=` | `show` fields | none |

Each function name passed `python tools/lexicon/lexicon.py --suggest <name> --as <cell>` on the worktree
at `179486e8f`, whose verb declarations equal the branch's.

### Migration

None for data. Every key defaults to today's behaviour except `review.unverified`, whose default `ask`
files an unverified finding as an ask where the DISPOSAL stage promoted it before; that is v2's default
and the §8 F2 decision.

### Rollout

One landing. A harness call that passes no `reviewPolicy` reads the four defaults and logs that it did.
A row written before this unit carries no `findings` field and reads the default.

### Files touched (estimate)

- `tools/loop/review_bounds.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/review_dispose.py`
- `tools/workflows/README.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`
- `help/loop.md`
- `tools/template-size-limits.txt`
- `.memory-tree.conf`
- `memory/project/positional-refs.txt`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`, `memory/map/generated/CARDS.md`,
  `memory/map/generated/inventories.json`

Each render is its template's copy: `memory/guides/UNATTENDED-VERBS.md`, `.claude/skills/unattended/SKILL.md`,
`memory/guides/BUILD-METHOD.md`, `tools/workflows/tier2-review.js` and `tools/workflows/unattended-build.js`.
The kickoff manifest watches `.memory-tree.conf` and `memory/guides/BUILD-METHOD.md`, so
`memory/guides/SESSION-KICKOFF.md`'s `last-audit` is re-stamped with a `manifest-audit:` delta line.

### Alternatives rejected

- **Record the trigger as a `review` row.** It would become the subject's last reason and hide the terminal
  token `tools/unattended/unattended.sh#review_last_reason` reads.
- **A Python reader of the run-state for the trigger's refusal.** `tools/runlog/model.py` holds one, in
  another kit; the driver's own predicate, lifted once, is the refusal `verb_review` already gives.
- **Keep the DISPOSAL stage's promotion of unverified findings as the default.** It is `block`'s route
  now, and v2's default is `ask`.
- **A preflight line printing the review policy.** It would be a second print of the values the trigger
  line carries to the same caller.
- **Check 2 re-reading the policy file.** The driver reads the landed revision at the round's time;
  check 2 reads a record later, and the row is the one fact both share.

## 5. Production-readiness checklist

- security — no new write surface but one: the DISPOSAL agent appends ask rows under `ask`, as it
  appends roster rows today. `review_pin.py` still checks shapes only, and the harness's membership
  check stays the one check.
- perf / scale — `--trigger` starts python three times at most, the bounds, the pin flags and the pin;
  the class count reads each review record's appendix once per disposal.
- error / empty / loading states — an absent key reads its catalogue default; an absent `reviewPolicy`
  reads the four defaults and is logged; a review record the parser refuses counts nothing and is named.
- observability — the trigger cause and the cost fields ride the record line; a non-default count rides
  the exit row.
- risks — the owed formula lives in three languages, the driver, check 2's awk and the harness, each
  with its arm and none generated from another; the DISPOSAL stage files asks by agent, and check 2's
  `asks_filed_in` floor reads only ` · to asks` exits, so an unverified ask is graded by the stage's sum
  alone.
- testing — the pass probes the verb and the count on fixture repositories, the record line, the bounds
  and the hand-out by node slices and stub runs, and the class count on fixture records; the arms in §7
  are observed RED then GREEN by the main loop.
- migration — the one default change in §4 Migration.
- user docs — `help/loop.md`, the verbs carrier and `tools/workflows/README.md`.

### The sweep

Read at branch `unattended-declared-loop-d56bf0`, tip `02524cadf`, through `git show` and an export of
that commit; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `verb_review`'s terminal pipeline | its `fail 37` naming the route; the driver suite's arms on `already carries a terminal review round` | the `fail` line and its text stay in `verb_review`; the function answers a status |
| `verb_review`'s two `owe` sites | its exit notes, which the driver suite asserts; check 2's owe sites | `derive_owed_units` prints today's integer and the note keeps today's clause under the default |
| the review row | `review_counts`, `review_last_reason`, `check_review_ended`; check 2's awk; `tools/loop/budget.py` plants counting `review · item` rows | the field is written only under a non-default value and before ` · to <target>`; no matcher reads `findings` but check 2 |
| `review_bounds.py show` | `load_review_bounds`; check 2's `read_review_bounds_line` and check 19's walk, which match `spec-bound=` and `closing-bound=` by their trailing space; `loop_lib.py --check`'s `loop: review bounds ·` line; the `defaults` plant's needle; `help/loop.md`'s `#show` row | fields are appended after `route-backs=`; the needle is a prefix; the usage row's flags do not move, so its fingerprint holds |
| `load_review_bounds` | `verb_review`, `run_fix_pass`; the driver suite's parity arm holding `REVIEW_*_DEFAULT` to `show` | the parse reads eleven fields; the four new defaults join the parity arm |
| `renderShapeLine` | `tools/workflows/tier2-review.test.sh`'s `SHAPE_RE`, anchored at `out-tokens=unknown$` (`tools/workflows/tier2-review.test.sh@b6711b49:2053`); `replay_scorer.py`'s `confirmed=` match | the anchored arm is re-pinned to the longer line in this unit's arm; the scorer reads one field |
| the build harness's args | its `args` header, which the args-header arm joins to each `a.<field>` read; the forwarded set of the audit call | `trigger` and `reviewPolicy` gain header rows |
| `DISPOSAL_SCHEMA`, the sum and bounds | the suite's DISPOSAL arms; `deriveDispositionFault` | `routed` is optional and reads 0; each existing arm whose stub leaves an unverified finding to the stage passes `unverified: 'block'`, today's route, as derived below |
| the CONVERGING return | the suite's arms asserting `roster: []` held at audit | the roster rides only under `blocks: 'no'`, which no existing arm passes |
| `VERBS_SLUG`, `VERB_REQUIRES`, the header, the parser | check 26's verb arm (header, `- \`--trigger\` — ` in the carrier, the Skill line) and flag arm (`--cause`, `--pin` on a header line and a non-comment line of the driver suite); check 52's join of each `VERB_REQUIRES` pair to a `check_verb_flag` call; the `docs` leg's new verb row, which the shrink-only undocumented list cannot take | S12's carriers; the driver suite arm passes both flags; two `check_verb_flag` calls; the anchor |
| the Skill render | `unattended skill size`, at `TOOL-dDeclaredLoop-31`'s 10848 PINNED row | it rises by 74 PINNED bytes to 10922 PINNED, re-measured at the build |
| `memory/guides/BUILD-METHOD.md` | `build-method size` at 30720 PINNED; `kit/dogfood doc parity`; the kickoff manifest's watch list; the positional row `BUILD-METHOD M4` this spec already holds | §4 "The method's text"; the template is the edit; the stamp; no new `BUILD-METHOD M<n>` citation |
| a new module under the workflows kit | the kit's `**` include; the map's symbol inventory; `review-join self-test`, `verifier fan-out self-test` and both harness suites, whose guard is the kit folder | no registry row; `gen_map.py --write`; the arms named in §7 |
| reader coverage | `arm_reader_coverage`, which grades `dDeclaredLoop`'s keys once every spec of the build is terminal | each of the nine keys reaches `resolve` as a literal in `review_bounds.py`, the shape `scan_reader_keys` reads |
| `tools/loop/loop.toml` | `loop_lib.py --check`, the `loop definition` leg; every `read_items` caller; the build table's B10 row and the dispose `[[stand-in]]` row | untouched: the rows land with unit 50 (§8 F4), so the check reads at this landing what it reads at `02524cadf` |
| subject pins, epoch delegates, upgrade rows | `tools/govkit/subject-pins.tsv`, `check-verdict-epoch.sh`'s `DELEGATES`, `[[upgrade]]` | no memory-tree module, no subject, no migration |
| suite floors | each `FLOOR_ASSERTIONS`, a lower bound | may rise by the arms added |

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:.claude/skills/unattended/SKILL.md" | tr -d '\r' | wc -c                   # 10815, before unit 31
printf '%s\n' 'unattended.sh --trigger <slug> --subject <s> --cause <cause> --pin <path>' | wc -c   # 74
git show "$B:memory/guides/BUILD-METHOD.md" | wc -c                                     # 30714
git show "$B:tools/workflows/unattended-build.test.sh" | grep -n '"unverified":[1-9]'    # DERIVED, the stubs to re-point
git show "$B:tools/unattended/unattended.sh" | grep -c "grep -qE '(CONVERGED|NON-CONVERGENT|CEILING|BOUNDED)'"   # 1
```

### Budgets and records

- The driver's census, read through `tools/memory-tree/check-arms.py#branches` and
  `tools/memory-tree/check-arms.py#scan_refusal_sites` over the export, is 332 PINNED (327 branches and
  5 sites at `02524cadf`), at its ceiling of 332 PINNED; `TOOL-dDeclaredLoop-31` raises both to 335
  PINNED. This unit adds three sites, S2's cause refusal, its ended-subject refusal and its read relay,
  so the ceiling rises 335 -> 338 PINNED with the comment line below, and
  `memory/project/positional-refs.txt`'s row pairing `.memory-tree.conf` with the driver is re-pointed in
  place to 338.
- The families of `tools/unattended/unattended.families.txt` do not move: `required-flag` stands at its
  11 PINNED of 11 and `field-shape` at 36 PINNED of 37, so no new message spells `requires --`,
  `requires $`, a newline, a carriage return, a separator or the bypass flag, and none opens `no
  run-state file`. The required flags reach `check_verb_flag`'s one message.
- `tools/unattended/check-unattended.sh` stays at 266 PINNED of its 266: check 2's change edits awk
  and adds no `fail`.
- `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED: every new name leads with a declared verb.
- The shared records: the pass writes neither `memory/DECISIONS.md` nor
  `memory/project/readme-contract.txt`. The run lands the decision row below ahead of the pass, and the
  pass writes the comment line above `REFUSAL_CEILINGS` in `.memory-tree.conf` and a `RAISED` comment
  above the Skill's row in `tools/template-size-limits.txt`:

```
- **TOOL-dDeclaredLoop-20** - **the driver's refusal ceiling rises by three, 335 -> 338, for `--trigger`'s cause refusal, its ended-subject refusal and its policy-read relay, and the `--trigger` invocation the unattended Skill gains raises its render's no-headroom size row 10848 -> 10922, under TOOL-aSparedSpawn-14's rule and TOOL-aOrientedCast-23's four raise terms, as TOOL-dDeclaredLoop-31 raised both**: agent, <date>, under ER:388 (PLAY-dClosedLoop-6), landed ahead of the pass that makes both raises. Detail `builds/dDeclaredLoop/`.
# TOOL-dDeclaredLoop-20 RAISED the driver 335 -> 338, the census, under decision TOOL-dDeclaredLoop-20 (ER:388): --trigger's cause refusal, ended-subject refusal and policy-read relay.
```

- Help anchors: `verb:unattended.sh:--trigger`, with the fingerprint
  `python tools/govkit/docs_leg.py --fingerprints` prints; `review_bounds.py pin` and `review_dispose.py
  classes` are shown on no page, so neither takes a usage row.
- The map: `python tools/codebase-map/gen_map.py --write` regenerates `symbols.json` and its siblings.
- Shipped comments name siblings by file name or `<prefix>`, never a kit path; the unattended, loop,
  workflows and memory-tree kit versions are owed at the lander.
- This revision turns the spec's line citations into symbol and blob-pinned citations, so the commit
  landing it runs `python tools/playbook/positional.py shrink`, which takes their rows out of the
  positional list.

### Dependency

Order 31, alone. `TOOL-dDeclaredLoop-31` (order 30, building) is read on its committed rev-4: the
ceiling of 335 and the Skill row of 10848, both PINNED there, and its edits to the same driver header,
`VERBS_SLUG` and parser, which this unit extends by a line each. Units 21 and 32 are CLOSED, read on
landed code. Units 22 and 50, order 32, read this spec: 50 writes §4's rows, and 22's binding score
prints the trigger line S2's verb takes. `TOOL-dDeclaredLoop-34` is deferred against ask
TOOL-dDeclaredLoop-113 and shares no file. The suggests, the reuse probes and the recall query ran on
the worktree at `179486e8f`; every other claim was read on the branch.

## 6. Acceptance criteria

- **AC1** — When a scratch AsyncFunction run of `tools/workflows/unattended-build.js` with a stub audit
  returning `CONVERGING` on a spec subject reaches its held return, that return's `nextAction` names
  `item.review.fold`, `BOUNDED` and `CEILING`, and no `NON-CONVERGENT`.
  Red when: the instruction names NON-CONVERGENT, a state a `no-fall` spec subject never reaches.
- **AC2** — When a fixture repository under `%TEMP%` whose committed policy file sets `review.unclassed`
  to `reason` and `review.blocks` to `owed-only` runs `unattended.sh --trigger <slug> --subject <unit>
  --cause owed --pin <its spec path>`, it prints one JSON line carrying `"preset": "unit-spec"`,
  `"unclassed": "reason"`, `"trigger": "owed"` and a `reviewPolicy` whose `blocks` is `yes`; with
  `--cause placement` and no `--pin` it prints one line whose `blocks` is `no` and which carries no
  `preset`; `--cause later` exits 1 printing `UNATTENDED check 37`; and after a terminal `--review` row
  for the subject, the first call exits 1 naming the subject.
  Red when: the trigger fires on a subject whose loop ended, or prints a catalogue default the fixture's
  policy file overrides.
  fixture: a committed repository holding the driver, the loop kit's `review_bounds.py`, the policy kit
  and `review_pin.py` with its harness, and a run-state file, built by the probe.
- **AC3** — When `grep -c 'check_review_ended'` runs over `tools/unattended/unattended.sh`, it prints at
  least 3, the definition and the two callers, and the literal pipeline
  `grep -qE '(CONVERGED|NON-CONVERGENT|CEILING|BOUNDED)'` appears once.
  Red when: the predicate is copied into the new verb, so it appears twice.
- **AC4** — When a scratch node probe slices `renderShapeLine` from `tools/workflows/tier2-review.js` and
  renders a field set with `trigger: 'owed'`, the line ends
  `out-tokens=unknown trigger=owed shape=- efforts=- role-sha=-`, every earlier field at its position; and
  the harness's argument check with `trigger: 'later'` throws naming `trigger`.
  Red when: a cost field is printed as `0`, a result where none was produced.
- **AC5** — When the fixture repository, its policy file setting `review.follow-up` to `never` so the
  closing review's first round exits, records `--review <slug> --subject <slug> --verdict BLOCKED
  --blockers 1 --highs 1 --minors 3 --disposition promote` under each value of `review.findings`, the
  driver's printed note owes at least 3 unit(s) under `blocker-high-own`, 5 under `all-own` and 2 under
  `blocker-own`, and the row carries ` · findings all-own` under the second and no `findings` field under
  the first.
  Red when: the driver ignores the value, so `all-own` reads 3.
  figure: 3, 5 and 2 DERIVED by §4 "The count" from the fixture's counts.
- **AC6** — When a scratch node probe slices `deriveUnitBounds` from `tools/workflows/unattended-build.js`
  and evaluates it at 1 blocker, 1 high, 3 confirmed minors and 0 adjudicated, it answers `{floor: 3,
  ceiling: 4}` under `blocker-high-own`, `{5, 5}` under `all-own` and `{2, 3}` under `blocker-own`; and a
  stub run under `unverified: 'ask'` whose disposal promotes an unverified finding returns an empty
  roster naming `review.unverified`, while one returning it as `routed` hands the roster out.
  Red when: `adjudicated` stays positive under `ask`, so an unverified finding is promoted.
  figure: each bound DERIVED by §4 "The count".
- **AC7** — When the new class-count module's `classes` verb (S6) runs over a fixture builds root where
  one prior record disposes `class:stale-pin` and the current record disposes `class:stale-pin` and
  `class:fresh-slug`, it prints `stale-pin` alone under `second-occurrence`, both under `every-class`,
  and both marked `owner` under `owner-selects`; a prior record with no appendix prints a `skipped` line.
  Red when: the current record counts itself, so `fresh-slug` earns a gate on its first occurrence.
- **AC8** — When a scratch AsyncFunction run of `tools/workflows/unattended-build.js` passes
  `reviewPolicy` with `blocks: 'no'` and a stub audit returning `CONVERGING`, the return carries a
  non-empty `roster` and the log names the review as running alongside; with `blocks: 'yes'` the roster
  is `[]`; and `reviewPolicy` missing `findings` throws naming `findings`.
  Red when: the hand-out stays held under `no`.
  cost: a stub harness modelled on the build harness suite's stub agents.
- **AC9** — When `grep -c 'review.findings'` runs over `tools/memory-tree/BUILD-METHOD.template.md` and
  `memory/guides/BUILD-METHOD.md`, each prints at least 1, `grep -c 'PROMOTED as at a DIFF exit'` prints
  1 over each, and `wc -c` on the guide stays at or under 30720.
  Red when: the template names the key and the guide is not re-rendered, or the pointer is not paid for.
  figure: 30720 is PINNED, the `build-method size` row at `02524cadf`.
- **AC10** — When `python tools/loop/review_bounds.py --fixture --plant disposal-keys` runs, it prints
  `held`: a policy file setting the four keys prints them after `route-backs=`; `--plant pin` prints the
  five flags with the file's `review.unclassed`; `--plant opt-in-set` exits 2 naming `review.opt-in`;
  and the `defaults` plant's line ends `findings=blocker-high-own unverified=ask
  left-shift=second-occurrence blocks=every-review`.
  Red when: `show` prints the catalogue default where the policy file sets a key.
- **AC11** — When `grep -c 'verb:unattended.sh:--trigger'` runs over `help/loop.md`, it prints 1;
  `grep -c -- '--trigger'` over `.claude/skills/unattended/SKILL.md` and over
  `memory/guides/UNATTENDED-VERBS.md` each prints at least 1; and `wc -c` on the Skill render, CR-stripped,
  equals its row in `tools/template-size-limits.txt`.
  Red when: the verb is declared and no page anchors it.

## 7. Gates

`unattended kit gate` · `unattended skill size` · `unattended skill wiring` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `loop review bounds fixtures` · `build-method size` · `kit/dogfood doc parity` · `docs` · `check-wiring self-test` · `scratch-guard self-test` · `policy fixtures` · `straggler-guard arms` · `transition-audit arms` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC4 · the four record fields and the trigger refusal, staged against the base harness, whose line ends at out-tokens; the shape arm's anchored pattern re-pinned to the longer line · FLOOR_ASSERTIONS in that suite, raised by the arms added

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC6 AC7 AC8 · the fold instruction, the unit bounds under each findings value, the unverified routes, the class count over fixture records and the hand-out under each blocks value, staged against the base harness, which has no reviewPolicy · FLOOR_ASSERTIONS in that suite, raised by the arms added

New arm: tools/loop/review_bounds.py · covers AC10 · the disposal-keys, pin and opt-in-set plants, staged against the base module, whose line ends at route-backs · none

New arm: tools/unattended/unattended.test.sh · covers AC2 AC5 · the trigger on an ended subject with both flags, the owed count under each findings value, and the four defaults in the parity arm, staged against the base driver · none

New arm: tools/unattended/check-unattended.test.sh · covers none · check 2's floor read from a row's findings field under each value, staged against the base leg · none

The unattended kit's own suites are waived for this build's landing (README rule 8): the last two arms
are declared here and read by the owner's run PLAY-dClosedLoop-13 names.

## 8. Open questions

- **F1 — Does M4's batch-every-minor disposal change, as the scout reported it closer to `all-own` than to
  the default?** Probe read: FL-B3's answer, quoted in §4, defines `blocker-high-own` as today's rule, one
  unit per blocker and high and the minors batched, which is M4's text.
  The scout's reading was wrong; the default changes nothing. The change is the sentence's pointer to the
  key, a governance-carrier change the clause names. RESOLVED (agent, 2026-10-24, delegated): M4 points at
  `review.findings` and `review.unverified`, its default reading unchanged, rung 1.
  grants: PLAY-dClosedLoop-3 BUILD-METHOD M4's disposal sentence pointing at review.findings and review.unverified
- **F2 — What does `review.unverified` default to, when today's DISPOSAL stage promotes unverified findings
  and no value of the key describes that?** Options: (a) v2's default `ask`; (b) keep today's promotion as an
  undeclared fourth value. (b) adds a value v2's row (v2:1258) does not admit. RESOLVED (agent, 2026-10-24,
  delegated): (a), rung 1, v2 answers it.
- **F3 — Where is "why the breakpoint fired" recorded?** Options: (a) a `trigger=` field on the review
  record's `review-shape` line, beside `review.cost`'s fields; (b) a run-state row. (b) hides the subject's
  terminal token from `review_last_reason`. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
  grants: PLAY-dClosedLoop-3 the --trigger verb, the trigger and reviewPolicy harness arguments and the four review-shape fields
- **F4 — Who writes the four item rows, when `check_program` refuses an `item.review.*` tag and the
  admission lands with `TOOL-dDeclaredLoop-50` at order 32?** Measured by that unit's re-ground at
  `02524cadf`: the rev-4 rows make `loop_lib.py --check` exit 1 with `item row 62 tag
  'item.review.trigger' opens no item.<step>. of a gov step`, before any actor is read. Options: (a) unit
  50 writes them from §4's table, with step `none`, the actors `command:review.<name>` and the inputs,
  allowance and returns a non-role actor carries, beside its admission and the pin and report rows, in
  one landing; (b) this unit lands that step and actor shape and the check's admission, and unit 50
  drops what this unit lands; (c) this unit lands the rows alone, and every reader of the item table
  refuses until order 32. (b) puts the program check's admission, a second mechanism, in this unit; (c)
  reds the `loop definition` leg for one order. Recommendation: (a), so this unit writes no row and the
  check stays green at its landing. RESOLVED (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F5 — Which pin values does the trigger read, and how does the catalogue's `review.opt-in` set reach
  `review_pin.py`'s object?** The catalogue declares `review.opt-in` a set of lens names, default empty,
  and `review_pin.py` takes `none` or an object keyed by preset; `tools/workflows/lenses.toml` ships no
  `optin = true` row. `review.twin` and the two `review.design-audit.*` rows name `dDeclaredLoop` their
  owner as the build their reader lands in, and their specs point at `review.trigger`. Options: (a) all
  five, the empty set passed as `none` and any member refused by name until a lens map exists; (b) the
  two the clause names, the other three left with no reader, which reader coverage reds at this build's
  landing; (c) a member grammar naming each lens's slot and preset, which no lens needs today.
  Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F6 — What does `block` do at a terminal exit, where `verb_review` takes no further round on the
  subject?** Options: (a) the DISPOSAL stage's own adjudication, today's route, which reads the code and
  promotes or refutes each unverified finding, so it blocks the hand-out until each is settled; (b) a
  verification round on a fresh subject, a subject grammar no unit builds; (c) refuse `block` as unarmed,
  a catalogued value the owner could set and the tool would refuse. Recommendation: (a). RESOLVED (agent,
  2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F7 — How does M4 take the pointer, with 6 bytes left under its row?** Options: (a) the SPEC-exit
  promotion sentence restated by reference to the DIFF exit's, which pays for the pointer and puts both
  exits under one count; (b) raise the `build-method size` row, which the owner's ruling keeps theirs;
  (c) no pointer, so M4 states a rule a key can change. Recommendation: (a). RESOLVED (agent, 2026-11-16,
  delegated): (a), by rung 3.
  widens: none · relaxes: none
  grants: PLAY-dClosedLoop-3 BUILD-METHOD M4's spec-exit promotion sentence restated by reference to the diff exit's
- **F8 — Where are the four keys read?** Options: (a) `review_bounds.py`, the loop kit's one reader of
  the review loop's keys, its `show` read once per verb by `load_review_bounds`; (b) a new module with
  its own resolver, plants and scaffold, a copy of the first; (c) one `policy.py get` per key in the
  driver, a Python start each and a refusal site per caller. Recommendation: (a). RESOLVED (agent,
  2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F9 — Where does the class count live?** The appendix reader is
  `tools/workflows/replay_scorer.py#parse_appendix_rows`, which `tools/workflows/review_replay.py`
  already imports as a sibling. Options: (a) a workflows-kit module beside it, importing it; (b) the loop
  kit, reaching it through `resolve_kit_dir`; (c) a parser of its own. Recommendation: (a). RESOLVED
  (agent, 2026-11-16, delegated): (a), by rung 2.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 20, flow-steps.md:563-603, FL-B3, FL-R1 and
  FL-R2, the stand-ins of dFairHearing-3 and -8, and the driver and harness read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-50, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-11-02 · §4 · S9 · the dispose row is limited to built work or a new mechanism and S9 rebases
  on M4 as rewritten, for the owner's 2026-11-01 ruling (TOOL-dFoldedAudit-8).
- rev-4 · 2026-11-05 · §2 §3 §4 §6 · S8 AC1 · the rev-3 fold's leftovers: the dispose row promotes a spec
  subject's new mechanism by TOOL-dDeclaredLoop-32's target, always units, and declares the plan-revision
  and landing-record routes §3 names, unarmed; S8, the fold row and AC1 take the spec subject's BOUNDED or
  CEILING in place of NON-CONVERGENT; the trigger row and the TOOL-dDeclaredLoop-32 edge refuse past
  `flow.route-backs` on the build slug only, by the brief
  prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md
- rev-5 · 2026-11-16 · §1 to §10 · S1 to S12 · AC1 to AC11 · §8 F4 to F9 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `02524cadf`, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-20-1-spec-writer`: symbol and blob-pinned citations; the rows'
  content handed to unit 50, whose admission they need (F4), and AC1 moved onto S8's fold instruction;
  the trigger's `--pin`, the five pin values and the opt-in set (F5); `block` as today's adjudication
  (F6); M4's pointer paid for in its own section (F7); the keys read by `review_bounds.py` (F8); the
  class count beside `parse_appendix_rows` (F9); the count's row field for check 2, `deriveUnitBounds`
  and `routed`; the hand-out under `blocks: 'no'` on the CONVERGING return; help and carriers; the
  census 335 -> 338 PINNED and the Skill row 10848 -> 10922 PINNED under a decision row landed ahead;
  the sweep.

## 10. Reuse audit

Every item attaches to what exists. `review.trigger` lifts the terminal predicate of
`tools/unattended/unattended.sh#verb_review` into one function at its second caller and calls
`tools/workflows/review_pin.py` rather than re-deriving a preset. The four keys join the reader of the
review loop's keys, `tools/loop/review_bounds.py#read_review_bounds`, whose line the driver already
reads through `tools/unattended/unattended.sh#load_review_bounds`. `review.cost` extends
`tools/workflows/tier2-review.template.js#renderShapeLine`, the one record-line renderer.
`review.dispose` re-points the three owed-count sites that exist, `verb_review`, check 2 and the DISPOSAL
stage, at the key, and files asks in the grammar `tools/unattended/lib-unattended.sh#asks_filed_in`
reads. The class count reads the appendix through
`tools/workflows/replay_scorer.py#parse_appendix_rows`, the import `tools/workflows/review_replay.py`
already makes; the count itself is new, because no reader of the disposition column exists.

`python tools/codebase-map/reuse_lookup.py "read the review program's disposal policy keys and pass them
to the review harness"` ranked generic readers (`read_text`, `read`, `key`) and
`tools/playbook/policy_value.py#read_policy_value`, another kit's policy reader;
`review_bounds.py`, which the map does not yet index on this worktree, is the seam the driver already
calls. `python tools/codebase-map/reuse_lookup.py "count review findings disposed class across review
record appendix"` ranked record readers of other kits (`tools/memory-tree/gotchas.py`,
`tools/memory-tree/build_records.py`), none of them an appendix reader.
`python tools/memory-recall/query.py "how are review findings disposed, unverified findings routed and
class occurrences counted"` returned the scout record's row for this unit, its own rev-4 Goal and the
spec brief's Items 20; none disagrees with source. The runlog model's `REVIEW_EXITS`
(`tools/runlog/model.py#derive_review_exit`) lacks `BOUNDED`, a stale set this unit does not read and
records here.

Recall terms used: review.dispose review.findings review.unverified review.left-shift adjudicated unitFloor DISPOSAL stage disposition appendix class:slug review_pin trigger
