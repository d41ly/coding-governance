# TOOL-dDeclaredLoop-20 — the breakpoint program's own items: trigger, dispose, fold and cost, and the four keys `review.dispose` reads

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 31 · advances TOOL-dDeclaredLoop-35

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
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

A reviewer breakpoint runs one program: dFairHearing builds `review.pin` to `review.report`, and this unit
builds the four items around them, `review.trigger`, `review.dispose`, `review.fold` and `review.cost`,
with the four keys `review.dispose` reads, `review.blocks`, `review.unverified`, `review.left-shift` and
`review.findings` (flow-steps.md:563-575). Today disposal is fixed in code and prose: the driver owes one
unit per blocker and high plus one for the minors (`tools/unattended/unattended.sh:12819`), the build
harness's DISPOSAL stage promotes every unverified finding it does not refute
(`tools/workflows/unattended-build.template.js:2205-2208`), and the stand-ins dFairHearing-3 and -8 left
take the opt-in and the unclassed values as arguments a caller types (AF-1, FM4).

## 2. Scope (IN)

- **S1** — Four item rows in the loop definition `tools/loop/loop.toml`, tagged `item.review.trigger`,
  `item.review.dispose`, `item.review.fold` and `item.review.cost`, each with its actor, needs, witness,
  routes and the policy keys it reads, as flow-steps.md:566-575 states them. Observed by AC1.
- **S2** — `review.trigger`, the verb `--trigger <slug> --subject <s> --cause <c>` in
  `tools/unattended/unattended.sh`. `<c>` is one of `owed`, `opt-in`, `recommendation`, `placement`. It
  refuses a subject whose loop already ended, by the predicate `verb_review` uses, extracted into
  `check_review_ended` so both call it. It reads `review.opt-in`, `review.unclassed` and `review.blocks`
  through dGroundRules-2's `policy.py get` (I10), passes the first two to `tools/workflows/review_pin.py` as `--opt-in` and
  `--unclassed`, and prints that JSON line with `trigger` and `blocks` added. dFairHearing-3 S9's and
  dFairHearing-8 S3's stand-ins are re-pointed to this verb: no caller types either value. Observed by AC2,
  AC3.
- **S3** — `review.cost`. `renderShapeLine` in `tools/workflows/tier2-review.template.js` (`:78-83`) appends
  `trigger=`, `shape=`, `efforts=` and `role-sha=`, the harness taking `trigger` as an argument validated in
  the closed set S2 names, and the other three printing `-` until dBoundRoles lands its shape registry.
  Observed by AC4.
- **S4** — `review.findings` decides the promotion count, with its three values: `blocker-high-own`, the
  default, one unit per blocker and per high and the medium and low batched, which is today's rule;
  `all-own`, one unit per finding; `blocker-own`, one unit per blocker and every other finding batched. The
  driver's owed count in `verb_review`, check 2's floor in `tools/unattended/check-unattended.sh` and the
  DISPOSAL stage's floor and ceiling in `tools/workflows/unattended-build.template.js` each compute from the
  value. Observed by AC5, AC6.
- **S5** — `review.unverified`, with its three values: `ask`, the default, each unverified finding filed as an
  ask with its evidence and never promoted; `block`, a verification round that re-runs the skeptic, drawing
  on the budget and counted against `flow.route-backs`, the finding filed as an ask past that bound;
  `record`, the finding listed in the report and nothing filed. The DISPOSAL stage's prompt and its
  `adjudicated` count follow the value. Observed by AC6.
- **S6** — `review.left-shift`, with its three values: `second-occurrence`, the default, a `class:<slug>`
  disposition whose slug a prior review record under `memory/builds/*/reviews/` already disposed earns a
  gate, filed as an ask; `every-class`, every `class:` and `new:` disposition earns one; `owner-selects`,
  each candidate an owner item. `measure_class_occurrences` in `tools/loop/review_dispose.py` counts by the
  dFairHearing-8 disposition column of the review records. Observed by AC7.
- **S7** — `review.blocks`, with its three values: `every-review`, the default and today's, the roster held
  until the review's verdict is terminal; `owed-only`, held only when the trigger cause is `owed`; `none`,
  never held. The build harness takes the value with the other three in one `reviewPolicy` argument the
  driver prints at preflight, and its hand-out gate reads it. Observed by AC8.
- **S8** — `review.fold`, the in-loop fold of an unbuilt spec, keeps its mechanism: the build harness's fold
  instruction (`tools/workflows/unattended-build.template.js:1990-1997`) gains the item's tag and its
  NON-CONVERGENT and CEILING route, findings promoted as `review.dispose` promotes them. Observed by AC1.
- **S9** — BUILD-METHOD M4's disposal sentence (`tools/memory-tree/BUILD-METHOD.template.md`, rendered at
  `memory/guides/BUILD-METHOD.md:144`) points at `review.findings` and `review.unverified` for the count and
  the unverified route, its default reading unchanged. Observed by AC9.
- **S10** — The suite arms the `New arm:` lines in §7 declare. Observed by AC2, AC4, AC5, AC7, AC8 through
  those lines, RED first at the close.

## 3. Non-goals (OUT)

- `review.pin`, `review.lens`, `review.refute` and `review.report`, and the report's disposition grammar:
  dFairHearing's, re-pointed here and never re-specced.
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
- No help page: `help/` does not document the review program.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-21` — `review.max-rounds`: the terminal state `review.trigger`
  refuses on, from the spec and closing bounds `review_bounds.py show` prints
- **consumes-from** `TOOL-dDeclaredLoop-32` — `flow.route-backs`: the route-back exit `review.trigger`
  refuses past, and the ` · to units` or ` · to asks` target `review.dispose` promotes by
- **hands-off** `TOOL-dDeclaredLoop-19` — `review.dispose`: the breakpoint's disposal, which a review
  breakpoint runs and whose trigger cause `TOOL-dDeclaredLoop-19` sets
- **hands-off** `TOOL-dDeclaredLoop-50` — the review program's item rows made to pass the program and declaration checks (the round-1 spec audit's id 2)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 32, 64, each a scope item of that unit

## 4. Design

### The item rows

| Tag | Actor | Needs | Witness | Routes | Reads |
|---|---|---|---|---|---|
| `item.review.trigger` | command | none | the trigger line `--trigger` prints, joined to the review record's `trigger=` field | fired to `item.review.pin`; a round past `review.max-rounds` or `flow.route-backs` refused, its open findings to `item.review.dispose`; not fired, the flow continues | `review.blocks`, `review.opt-in`, `review.unclassed`, `review.max-rounds`, `flow.route-backs` |
| `item.review.dispose` | command | `item.review.report` | each confirmed finding joined to its fold, unit or ask | unbuilt to `item.review.fold`; built to new units or asks by `review.findings`; NON-CONVERGENT or CEILING promoted to units while budget remains and to asks after; an unverified finding under `block` to a verification round | `review.findings`, `review.unverified`, `review.left-shift`, `flow.rework-budget` |
| `item.review.fold` | spec writer | `item.review.dispose` | each confirmed finding joined to its fold at the spec's new blob, which the re-invoke's `prevSubjects` pins | the next round as `review.design.rounds` says, or released; NON-CONVERGENT or CEILING promoted as `item.review.dispose` promotes | `review.design.rounds` |
| `item.review.cost` | command | `item.review.report` | the `review-shape` line's cost fields | done | none |

The rows take the field names `TOOL-dDeclaredLoop-9` and `TOOL-dDeclaredLoop-12` give every item row; the
table above is their content. A plan revision and a landing record are declared routes of
`item.review.dispose` with no armed consumer, as §3 says.

### The trigger

```
--trigger <slug> --subject <s> --cause owed|opt-in|recommendation|placement
  refuse a cause outside the set                               (fail 37)
  refuse when check_review_ended "$rel" "$s"                 (fail 37, the verb_review sentence)
  optin=review.opt-in  unclassed=review.unclassed  blocks=review.blocks
  python review_pin.py <subject paths> --opt-in "$optin" --unclassed "$unclassed"
  print that JSON line with "trigger": "<c>", "blocks": "<yes|no>"
```

`check_review_ended` is the grep pipeline at `tools/unattended/unattended.sh:12762`, lifted unchanged
into a function at its second caller. It returns a status and refuses nothing: each caller spells its own
`fail 37`, because check-arms finds a branch by its literal number (`:12738-12740`). `blocks` is `yes` under `every-review`, `yes` under
`owed-only` only when the cause is `owed`, and `no` under `none`. The verb writes no row: a non-round row
in the `review` kind would become the subject's last reason and hide its terminal token from
`review_last_reason`.

### The record line

```
review-shape kind=… round=… … agents=<n> out-tokens=<n> trigger=<cause|-> shape=- efforts=- role-sha=-
```

The four fields follow the existing ones, so a reader of today's line reads every field it read before. The
harness validates `trigger` beside `intensity`, refusing a value outside the closed set by name; absent, it
prints `-`.

### The count

| `review.findings` | Owed units at an exit |
|---|---|
| `blocker-high-own` | `blockers + highs + (minors > 0 ? 1 : 0)`, today's |
| `all-own` | `blockers + highs + minors` |
| `blocker-own` | `blockers + (highs + minors > 0 ? 1 : 0)` |

The owner's FL-B3 answer is the default: "As it is today, by default - BLOCKER and HIGH findings become
their own units, MEDIUM and LOW are batched … How it works should be owner-adjustable"
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md:382-387`). The driver's
`owe` (`tools/unattended/unattended.sh:12819`), check 2's floor and the DISPOSAL stage's `unitFloor` and
`unitCeiling` (`tools/workflows/unattended-build.template.js:2208-2209`) each take the formula of the value,
and the DISPOSAL prompt's batching sentence (`:2083-2090`) is rendered from it.

### The unverified route

Under `ask`, the DISPOSAL stage files each unverified finding it does not refute as an ask in the build's
`BACKLOG.md` with the finding's evidence, and `adjudicated` is 0. Under `record`, it lists them in its
summary and files nothing. Under `block`, it returns them as a verification round the caller runs by
re-invoking the harness on those ids alone; the round is recorded by `--review` and so draws on the budget
and counts against `flow.route-backs` through `TOOL-dDeclaredLoop-32`'s rule, and a finding still unverified
past that bound is filed as an ask.

### The left-shift count

`python review_dispose.py classes <reviews root> <record>` reads every review record's disposition column
(dFairHearing-8 S8), counts each `class:<slug>` across records other than `<record>`, and prints one line per
slug of `<record>` that earns a gate under the value: under `second-occurrence`, a slug with a prior count of
1 or more; under `every-class`, every `class:` and `new:` slug; under `owner-selects`, every slug, marked as an
owner item. The DISPOSAL stage files each earned gate as an ask naming the slug, the records and the item
`item.review.dispose`.

### The hand-out gate

The driver's preflight prints `unattended: review policy — findings <v> · unverified <v> · left-shift <v> ·
blocks <v>` beside the spec-audit line (`print_spec_audit_line`, `tools/unattended/unattended.sh:7887`), and
the caller passes the four as `reviewPolicy`. The harness refuses an object missing a key or carrying a value
outside its set. Under `none` and under `owed-only` with a cause other than `owed`, the hand-out follows the
audit's start rather than its terminal verdict, and the log says the review runs alongside.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `--trigger`, `--cause` | driver verb and flag | flag, none |
| `run_trigger`, `check_review_ended` | bash functions | `sh.function`, verb-first |
| `measure_class_occurrences` | Python function, `tools/loop/review_dispose.py` | `py.function`, verb-first |
| `reviewPolicy`, `trigger` | harness arguments | none |
| `trigger=`, `shape=`, `efforts=`, `role-sha=` | `review-shape` fields | none |

### Migration

None. Every key defaults to today's behaviour except `review.unverified`, whose default `ask` files an
unverified finding as an ask where the DISPOSAL stage promoted it before; that is v2's default and the
§8 F2 decision.

### Rollout

One landing. A harness call that passes no `reviewPolicy` reads the four defaults and logs that it did.

### Files touched (estimate)

- `tools/loop/loop.toml`
- `tools/loop/review_dispose.py`
- `tools/loop/selftest.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/README.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`

Each `memory/guides/*.md` and each `tools/workflows/*.js` above is the render of its template; the template
is the edit.

### Alternatives rejected

- **Record the trigger as a `review` row.** It would become the subject's last reason and hide the terminal
  token `review_last_reason` reads (`tools/unattended/unattended.sh:12626-12638`).
- **A Python reader of the run-state for the trigger's refusal.** `tools/runlog/model.py` holds one, in
  another kit; the driver's own predicate, lifted once, is the refusal `verb_review` already gives.
- **Keep the DISPOSAL stage's promotion of unverified findings.** No value of `review.unverified` describes
  it, and v2's default is `ask`.

## 5. Production-readiness checklist

- security — no new write surface; `review_pin.py` still checks the opt-in's shape only, and the
  harness's membership check stays the one check.
- perf / scale — the class count reads each review record's appendix once per disposal.
- error / empty / loading states — an absent key reads its catalogue default and the preflight line says
  so; an absent `reviewPolicy` reads the four defaults and is logged; a review record with no disposition
  column counts nothing and is named.
- observability — the trigger cause and the cost fields ride the record line; the policy values ride the
  preflight line.
- risks — the DISPOSAL stage files asks by agent; the driver's `asks_filed_in` floor reads them, and a
  missing ask reds check 2.
- testing — the pass probes the verb on fixture repositories, the record line and floor by node slices, and
  the class count on fixture records; the arms in §7 are observed RED then GREEN by the main loop.
- migration — the one default change in §4 Migration.
- user docs — the verbs carrier and `tools/workflows/README.md`; no help page covers the review program.

## 6. Acceptance criteria

- **AC1** — When a scratch probe loads the loop definition through the loop kit's reader, it finds rows
  tagged `item.review.trigger`, `item.review.dispose`, `item.review.fold` and `item.review.cost`, each with a
  non-empty actor, witness and route set, the dispose row reading `review.findings`, `review.unverified` and
  `review.left-shift`, and the fold row's routes naming the NON-CONVERGENT and CEILING promotion.
  Red when: a row lacks its witness, so the item has no computed proof.
- **AC2** — When a fixture repository under `%TEMP%` runs `unattended.sh --trigger <slug> --subject <spec>
  --cause owed`, it prints one JSON line carrying `preset`, `optIn`, `unclassed`, `"trigger": "owed"` and
  `"blocks": "yes"`, the `unclassed` value being the one the fixture's policy file sets; `--cause later`
  exits 37; and after a terminal `--review` row for the subject, the same call exits 37 naming the
  terminal round.
  Red when: the trigger fires on a subject whose loop ended.
  fixture: a committed repository whose policy file sets `review.unclassed`, built by the probe.
- **AC3** — When `grep -c 'check_review_ended'` runs over `tools/unattended/unattended.sh`, it prints at
  least 3, the definition and the two callers, and the literal pipeline
  `grep -qE '(CONVERGED|NON-CONVERGENT|CEILING|BOUNDED)'` appears once.
  Red when: the predicate is copied into the new verb, so it appears twice.
- **AC4** — When a scratch node probe slices `renderShapeLine` from `tools/workflows/tier2-review.js` and
  renders a field set with `trigger: 'owed'`, the line ends `trigger=owed shape=- efforts=- role-sha=-`, and
  every field the line carried before keeps its position; a harness argument check with `trigger: 'later'`
  throws naming `trigger`.
  Red when: a cost field is printed as `0`, a result where none was produced.
- **AC5** — When the fixture repository records an exit with `--blockers 1 --highs 1 --minors 3` under each
  value of `review.findings`, the driver's printed owed count reads 3 under `blocker-high-own`, 5 under
  `all-own` and 2 under `blocker-own`.
  Red when: the driver ignores the value, so `all-own` reads 3.
- **AC6** — When a scratch node probe slices the DISPOSAL floor from `tools/workflows/unattended-build.js`
  and evaluates it at 1 blocker, 1 high, 3 minors and 2 unverified, `unitFloor` under
  `blocker-high-own` and `ask` is 3 with `adjudicated` 0, under `all-own` is 5, and under `record` the
  prompt names no ask for the unverified findings.
  Red when: `adjudicated` stays positive under `ask`, so unverified findings are promoted.
- **AC7** — When `python review_dispose.py classes` runs over a fixture reviews root where one prior record
  disposes `class:stale-pin` and the current record disposes `class:stale-pin` and `class:fresh-slug`, it
  prints `stale-pin` alone under `second-occurrence`, both under `every-class`, and both marked owner under
  `owner-selects`.
  Red when: the current record counts itself, so `fresh-slug` earns a gate on its first occurrence.
- **AC8** — When a scratch AsyncFunction run of `tools/workflows/unattended-build.js` passes
  `reviewPolicy` with `blocks: 'none'` and a stub audit that never returns a terminal verdict, the roster is
  handed out and the log names the review as running alongside; with `blocks: 'every-review'` it is held;
  and `reviewPolicy` missing `findings` throws naming `findings`.
  Red when: the hand-out stays held under `none`.
  cost: a stub harness of about 60 lines, modelled on the build harness suite's stub agents.
- **AC9** — When `grep -c 'review.findings'` runs over `tools/memory-tree/BUILD-METHOD.template.md` and
  `memory/guides/BUILD-METHOD.md`, each prints at least 1, and `wc -c` on the guide stays at or under
  30720 bytes, M1's declared budget.
  Red when: the template names the key and the guide is not re-rendered.
  figure: 30720 is PINNED, M1's budget at base `ed497191`.

## 7. Gates

`unattended kit gate` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC4 · the four record fields and the trigger refusal, staged against the base harness, whose line ends at out-tokens · FLOOR_ASSERTIONS in that suite, raised by the arms added

New arm: tools/workflows/unattended-build.test.sh · covers AC8 · the hand-out under each blocks value and the missing-key refusal, staged against the base harness, which has no reviewPolicy · FLOOR_ASSERTIONS in that suite, raised by the arms added

New arm: tools/loop/selftest.py · covers AC7 · the second-occurrence count over fixture records, staged against the base tree, which has no class counter · none

New arm: tools/unattended/unattended.test.sh · covers AC2 AC5 · the trigger on an ended subject and the owed count under each findings value, staged against the base driver · none

The unattended kit's own suites are waived for this build's landing (README rule 8): the last arm is declared
here and read by the owner's run PLAY-dClosedLoop-13 names.

## 8. Open questions

- **F1 — Does M4's batch-every-minor disposal change, as the scout reported it closer to `all-own` than to
  the default?** Probe read: FL-B3's answer, quoted in §4, defines `blocker-high-own` as today's rule, one
  unit per blocker and high and the minors batched, which is M4's text (`memory/guides/BUILD-METHOD.md:144`).
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

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 20, flow-steps.md:563-603, FL-B3, FL-R1 and
  FL-R2, the stand-ins of dFairHearing-3 and -8, and the driver and harness read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-50, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.

## 10. Reuse audit

Every item attaches to what exists. `review.trigger` lifts the terminal predicate of `verb_review`
(`tools/unattended/unattended.sh:12762`) into one function at its second caller and calls dFairHearing-3's
`tools/workflows/review_pin.py` rather than re-deriving a preset. `review.cost` extends `renderShapeLine`
(`tools/workflows/tier2-review.template.js:78-83`), the one record-line renderer. `review.dispose` re-points the
three owed-count sites that exist (`tools/unattended/unattended.sh:12819`, check 2's floor, and the DISPOSAL
floor at `tools/workflows/unattended-build.template.js:2208-2209`) at the key, and files asks through the
build's `BACKLOG.md` grammar `asks_filed_in` reads. The class count is new: no reader of the report's
disposition column exists, because dFairHearing-8 adds the column.

`python tools/codebase-map/reuse_lookup.py "dispose confirmed review findings by severity into units or
asks"` ranked the ask helpers of `tools/unattended/lib-unattended.sh`, `derive_review_exit` and
`derive_review_verdict` (`tools/runlog/model.py`); the runlog pair reads a run-state reason in another kit,
rejected in §4. `python tools/memory-recall/query.py "how are review findings disposed and who folds them"`
returned the scout record's row for this unit, `TOOL-aEvidencedLens-8`'s reuse audit and the scout's row for
unit 16 on the closed-set constant. One hit disagrees with source: the scout reads M4's batch-every-minor as
closer to `all-own`, and FL-B3 defines it as `blocker-high-own` (§8 F1). The runlog model's `REVIEW_EXITS`
(`tools/runlog/model.py:110`) lacks `BOUNDED`, a stale set this unit does not read and records here.

Recall terms used: review.dispose fold promote REVIEW_DISPOSITIONS severity MEDIUM LOW batched unverified left-shift class gate
