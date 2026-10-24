# TOOL-dDeclaredLoop-19 — breakpoints at any item boundary: reviews and owner gates one mechanism under `review.breakpoints`, `review.<stage>` and `autonomy`

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 33 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0104@2c27f8f3 whole

**Carries:** node:policy-key.review.breakpoints

**Carries:** node:policy-key.review.<stage>

**Carries:** node:policy-key.autonomy

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

A breakpoint is one thing, wherever it sits: a position at an item boundary, a disposer, which is a reviewer
or the owner, and a trigger (flow-steps.md:518-527). `review.<stage>` and `autonomy` are its default
declarations and `review.breakpoints` adds more at any item boundary. A review breakpoint runs dFairHearing's
harness; an owner gate holds until the owner's disposition record, which `run.on-owner-question` will resolve
only once dBoundRoles lands it and never for a ratification. Until dScopedBuild lands `build.ratify`, the
owner gate stands in for it under `decisions.major: author-owner-ratifies`, holding `build.recommend`'s route
for the owner as RC-9's fallback holds `plan.exit`. Today reviews and owner decisions are two mechanisms at
fixed points: a design review is a dated README opt-in (`tools/unattended/unattended.sh:3963-3984`) and an
owner decision a park row (`verb_park`, `:12868`), and nothing places either at another boundary
(`gap-flow-11`, AF-1, DA-H1, FK-9-1).

## 2. Scope (IN)

- **S1** — `derive_breakpoints(policy, definition, build)` in `tools/loop/breakpoints.py`, the one rule that
  lists a build's breakpoints, each `{name, position, disposer, cause, ratification}`, `name` one of I23's
  `breakpoint`, `owner gate`, `owner item`, `spec audit`, `gate review`, `closing review`, `landing review`.
  It reads `review.<stage>` for each of the five stages, `autonomy`, `review.breakpoints` and
  `decisions.major` through the policy reader, with v2's catalogue defaults until dGroundRules' reader lands:
  `opt-in` for every stage but Build, `owed` for Build, `plan-only` and `none`. Observed by AC1, AC2.
- **S2** — The review declarations. Under `review.<stage>`, `off` places nothing, `opt-in` places the stage's
  review breakpoint only where the build opts in, `owed` always, and `owed-above-tier` when a spec of the
  build is Tier-2. The positions are the Plan breakpoint before `item.plan.exit`, the `spec audit` after
  `item.design.reason`, the `closing review` after `item.build.recommend`, the `gate review` before
  `item.test.exit` and the `landing review` before `item.deploy.notify`. Observed by AC1, AC5, AC6.
- **S3** — The owner declarations. Under `autonomy`, `plan-only` places the owner gate at `item.plan.exit`,
  `three-gates` adds one at `item.design.exit` and one before `item.deploy.mandate`, and `every-stage` adds one
  at every step's exit. Observed by AC1.
- **S4** — The placed declarations. `review.breakpoints` names item boundaries by item tag, read through
  `TOOL-dDeclaredLoop-26`'s `read_tag_policy`, so a boundary renamed under the build keeps its breakpoint;
  each is a review breakpoint whose cause is `placement`, and a tag the loop definition does not declare is
  refused naming `review.breakpoints` and the tag. Observed by AC2.
- **S5** — The ratification stand-in. Under `decisions.major: author-owner-ratifies`, while the loop definition
  declares no `item.build.ratify` row, `derive_breakpoints` places an owner gate on `build.recommend`'s route,
  after the closing review and before `item.build.distill`, marked `ratification`. It is placed when a spec of
  the build carries a fork resolved by the agent under delegation, every such fork read as major because no
  fork record carries a class until a later build lands one. Once a row for `item.build.ratify` is declared,
  the stand-in is not placed. Observed by AC3, AC4.
- **S6** — One holding mechanism. A review breakpoint fires through `TOOL-dDeclaredLoop-20`'s
  `--trigger <slug> --subject <s> --cause <c>`, the cause `owed`, `opt-in` or `placement` taken from S1's list.
  An owner gate holds as an `owner-decision` hold on a `decision` row naming the gate, released only by the
  owner's disposition record through `check_owner_disposition`. The driver's `--close` refuses while a placed
  owner gate has no disposition record naming it, and `--phase` refuses a move past a gated step exit, read
  through I3's phase-to-step table (`TOOL-dDeclaredLoop-1` §4) as `TOOL-dDeclaredLoop-13`'s engine applies
  it. Observed by AC3, AC7.
- **S7** — `run.on-owner-question` is not read. Every owner gate lists its resolver as the owner's disposition
  record, and a ratification gate is marked as one `run.on-owner-question` never resolves. Observed by AC7.
- **S8** — The spec-audit opt-in re-pointed to `review.<stage>`. The driver's derivation in
  `check_authorization` (`tools/unattended/unattended.sh:3963-4040`) reads `review.design` first: under
  `opt-in`, today's README `spec-audit:` key and `SPEC_AUDIT_DEFAULT` decide, unchanged; under `owed`, and under
  `owed-above-tier` with a Tier-2 spec at BASE, the audit is owed with the source `policy`; under `off`, it is
  not owed and a README key present is named as unread. `print_spec_audit_line` prints the `policy` source.
  BUILD-METHOD M4's "When" (`tools/memory-tree/BUILD-METHOD.template.md`, rendered at
  `memory/guides/BUILD-METHOD.md:117-119`) names `review.design` beside the two it names. Observed by AC5, AC6,
  AC9.
- **S9** — `--plan` prints one `breakpoint:` line per placed breakpoint, `name · position · disposer · cause`.
  Observed by AC8.
- **S10** — `tools/unattended/VERBS.template.md`, its render `memory/guides/UNATTENDED-VERBS.md`, and
  `tools/unattended/PROTOCOL.template.md` with its render `memory/guides/UNATTENDED-PROTOCOL.md` state the
  breakpoint lines, the gate refusals and the `policy` source of the opt-in. Observed by AC9.
- **S11** — The suite arms the `New arm:` lines in §7 declare. Observed by AC1, AC2, AC3, AC5 through those
  lines, RED first at the close.

## 3. Non-goals (OUT)

- `run.on-owner-question` and its values: dBoundRoles' key. The hand-over: once that build lands it, it may
  resolve an owner gate that is not a ratification, and `derive_breakpoints`' `ratification` mark is what it
  reads to refuse the rest.
- `build.ratify` and the fork's class: dScopedBuild's item and a later build's fork record. The hand-over: a
  declared `item.build.ratify` row stops the stand-in, and from then a fork's class decides.
- The review program's items and keys: `TOOL-dDeclaredLoop-20`'s, which this unit fires and never re-specs.
- The recommendation: `TOOL-dDeclaredLoop-22`'s record. A binding `review` score fires a breakpoint through the
  same `--trigger` line; this unit reads the record only to hold `build.recommend`'s route.
- `attendance` and its confirm gates, `run.owner-deadline` and `run.on-owner-silence`: later builds' keys.
- Executing a review breakpoint at an arbitrary item inside a running step: the position engine's next item is
  another unit's, and this unit lists and holds; a placed review breakpoint fires through `--trigger`.
- No help page: `help/` documents neither the driver nor the review loop.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-16` — `record-kind.disposition`: the owner's disposition record, the
  only release of an owner gate
- **consumes-from** `TOOL-dDeclaredLoop-26` — `read_tag_policy`: the read of `review.breakpoints` that
  re-points a renamed boundary, so a placed breakpoint follows its item across a rename
- **consumes-from** `TOOL-dDeclaredLoop-20` — `review.dispose`: the breakpoint program a review breakpoint runs,
  fired by its `--trigger` verb
- **consumes-from** `TOOL-dDeclaredLoop-22` — `record-kind.recommendation`: the `build.recommend` score record
  whose route the ratification stand-in holds
- **consumes-from** `TOOL-dDeclaredLoop-31` — `record-kind.disposition`: `check_owner_disposition`, the release
  check every owner gate's hold reuses
- **hands-off** `TOOL-dDeclaredLoop-52` — the phase-to-state-and-step map, which that unit ships as rows with one reader (the round-1 spec audit's id 4)
- **hands-off** `TOOL-dDeclaredLoop-53` — the owner gate's in-flight rule, which that unit scopes to builds opened after the placement (the round-1 spec audit's id 54)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 10, 37, each a scope item of that unit

## 4. Design

### The list

```
derive_breakpoints(policy, definition, build) -> [{name, position, disposer, cause, ratification}]
  for stage in plan design build test deploy:
    v = review.<stage>
    off                -> nothing
    opt-in             -> the stage's review, cause opt-in, only where the build opts in
    owed               -> the stage's review, cause owed
    owed-above-tier    -> the stage's review, cause owed, when a spec of the build is Tier-2
  autonomy: plan-only   -> owner gate at item.plan.exit
            three-gates -> + item.design.exit, + before item.deploy.mandate
            every-stage -> + every step's exit item
  review.breakpoints: each item tag -> breakpoint, reviewer, cause placement; unknown tag refused
  decisions.major == author-owner-ratifies and no item.build.ratify row and a delegated fork
                       -> owner gate on build.recommend's route, ratification
```

| Stage | Review name | Position |
|---|---|---|
| plan | `breakpoint` | before `item.plan.exit` |
| design | `spec audit` | after `item.design.reason`, before `item.design.ready` |
| build | `closing review` | after `item.build.recommend` |
| test | `gate review` | before `item.test.exit` |
| deploy | `landing review` | before `item.deploy.notify` |

Opting in is a fact per build: for Design it is S8's derivation; for the other stages no per-build opt-in
exists in this tree, so `opt-in` there places nothing until a placement disposition or `review.breakpoints`
names the boundary. The function is pure, and `python breakpoints.py list --build <slug>` prints its answer,
which the driver calls through `resolve_kit_dir` (`tools/unattended/lib-unattended.sh:191`).

### The ratification stand-in

The FK-9-1 ruling: until dScopedBuild lands `build.ratify`, `build.recommend`'s route under
`decisions.major: author-owner-ratifies` reaches this build's owner gate, held for the owner's disposition
(flow-steps.md:313-317). A fork "its author classed major" has no class in this tree, so the stand-in reads
every §8 fork resolved `RESOLVED (agent, <date>, delegated)` as major: holding one fork too many asks the owner
once more, and holding one too few lands a decision the owner ruled theirs. The forks are read by
`plan_state`'s own grammar functions (`check_mark`, `check_fitem_open`, `tools/unattended/unattended.sh:4466-4467`),
through a mode of the same awk program, never a second §8 parser.

### The hold

An owner gate is held where the run would pass it. `--close` refuses while any placed owner gate lacks a
disposition record naming its `decision` row; `--phase` refuses a move whose phase lies past a gated step
exit, the step a phase lies in read through I3's phase-to-step table as `TOOL-dDeclaredLoop-13`'s engine
applies it, never a second copy of that table. Holding writes the `decision` row and the
`owner-decision` hold (`HOLD_CODES_CORE`, `tools/unattended/unattended.sh:1029`), and releasing reads the
disposition record through `check_owner_disposition`. One mechanism, so the plan ratification, a
`three-gates` gate and the ratification stand-in are held and released alike.

### The opt-in

| `review.design` | README `spec-audit:` | Owed | `AUTH_SPEC_AUDIT_FROM` |
|---|---|---|---|
| `opt-in` (default) | as today | as today | `readme` or `project`, as today |
| `owed` | any | yes | `policy` |
| `owed-above-tier` | any | yes when a spec at BASE is Tier-2 | `policy` |
| `off` | present | no, the key named as unread | none |

`review.design` is read from the policy file at the landed revision, which is the owner's guarded file
(dGroundRules' guard), so a run can no more write `owed` than it can write a README opt-in. The owed value is
pinned as the BASE commit's date, the shape the run-state's `spec-audit` fact already carries, so the
`specs-audited` grader and fail 53's comparison read it unchanged.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_breakpoints` | Python function, `tools/loop/breakpoints.py` | `py.function`, verb-first |
| `check_owner_gates` | bash function, the `--close` and `--phase` refusal | `sh.function`, verb-first |
| `breakpoint:` | `--plan` output line head | none |
| `policy` | `AUTH_SPEC_AUDIT_FROM` value | none |

### Migration

None. Every default reproduces today: `review.design` `opt-in` keeps the README opt-in, `autonomy`
`plan-only` places the plan gate, which the plan's ratification already is, and `decisions.major`'s default
`author-rubric` places no stand-in.

### Rollout

One landing. A project whose policy file sets no key sees one `breakpoint:` line for the plan gate and one
for the owed closing review.

### Files touched (estimate)

- `tools/loop/breakpoints.py`
- `tools/loop/selftest.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`

Each `memory/guides/*.md` is the render of its template; the template is the edit.

### Alternatives rejected

- **Keep reviews and owner gates as two lists.** The clause makes them one mechanism; two lists are the
  `gap-flow-11` defect.
- **Read the major class from a field this tree does not have.** No fork record carries one; inventing it
  here would be a later build's mechanism.
- **Retire the README opt-in for `review.design: owed`.** The README key is the per-build channel `opt-in`
  needs, and the owner's per-build opt-in rulings (TOOL-aBlindedTrial-6, TOOL-aWardedAudit-4) stand.

## 5. Production-readiness checklist

- security — `review.design` and `autonomy` are read only from the guarded policy file at the landed
  revision, so a run cannot place or remove a gate; the hold adds no write surface beyond the existing
  `decision` row.
- perf / scale — one policy read per key and one §8 pass per spec per run.
- error / empty / loading states — an unknown `review.breakpoints` tag refuses; an absent key reads its
  catalogue default and `--plan` says so.
- observability — every placed breakpoint is a `breakpoint:` line; every hold is a `decision` row.
- risks — the stand-in reads every delegated fork as major, so a build under `author-owner-ratifies` asks the
  owner about forks a class would have passed; that is the safe direction and ends with the later build.
- testing — the pass probes `derive_breakpoints` directly and the driver on fixture repositories; the arms in
  §7 are observed RED then GREEN by the main loop.
- migration — none.
- user docs — the verbs and protocol carriers; no help page covers the driver.

## 6. Acceptance criteria

- **AC1** — When `python breakpoints.py list` runs over a fixture with no policy file, it prints an owner gate
  at `item.plan.exit` and a `closing review` after `item.build.recommend` and nothing else; with
  `autonomy = "three-gates"` it adds owner gates at `item.design.exit` and before `item.deploy.mandate`; with
  `every-stage` it prints an owner gate at each of the five step exits; with `review.test = "owed"` it adds a
  `gate review` before `item.test.exit`.
  Red when: `review.<stage>` and `autonomy` are listed by two functions, so `every-stage` misses a review.
- **AC2** — When the fixture sets `review.breakpoints = ["item.build.unit-pass"]`, `python breakpoints.py list`
  adds a `breakpoint` before `item.build.unit-pass` with cause `placement`; with `["item.build.nothing"]` it
  exits non-zero naming `review.breakpoints` and the tag.
  Red when: an undeclared tag is placed silently.
- **AC3** — When a fixture repository under `%TEMP%` sets `decisions.major = "author-owner-ratifies"`, declares
  no `item.build.ratify` row, and carries a spec whose §8 fork is resolved by the agent under delegation,
  `python breakpoints.py list` prints an owner gate on `build.recommend`'s route marked `ratification`, and
  `unattended.sh --close <slug>` is refused naming the gate until a disposition record naming its `decision`
  row is committed.
  Red when: the planted major fork reaches no gate and `--close` proceeds.
  fixture: a committed repository with a run-state file, a policy file and one spec, built by the probe.
- **AC4** — When the same fixture's loop definition declares an `item.build.ratify` row, the ratification gate
  is not listed; and under `decisions.major = "author-rubric"` it is not listed either.
  Red when: the stand-in is placed after the build that owns `build.ratify` has landed.
- **AC5** — When the fixture sets `review.design = "owed"` and the build README carries no `spec-audit:` key,
  `unattended.sh --preflight` prints the spec-audit line naming the policy source; with `review.design = "off"`
  and a README `spec-audit:` key, it prints not owed and names the key as unread; with the default and the
  README key, it prints today's README line.
  Red when: `owed` leaves the audit not owed because the README is silent.
- **AC6** — When the fixture sets `review.design = "owed-above-tier"`, the audit is owed with a Tier-2 spec at
  BASE and not owed with only Tier-1 specs, as `unattended.sh --preflight` prints.
  Red when: a Tier-1-only build is owed an audit.
- **AC7** — When `grep -c 'run.on-owner-question'` runs over the loop kit's breakpoint module
  and over `tools/unattended/unattended.sh`, each prints 0 outside comments; and every owner gate `python breakpoints.py
  list` prints names its resolver as the owner's disposition record, the ratification gate marked as one no
  key resolves.
  Red when: a gate lists `run.on-owner-question` as its resolver before the build that owns it lands.
- **AC8** — When `unattended.sh --plan <slug>` runs on the AC1 fixture, it prints one `breakpoint:` line per
  breakpoint `python breakpoints.py list` prints, in the same order.
  Red when: `--plan` derives its own list.
- **AC9** — When `grep -c 'review.design'` runs over `tools/memory-tree/BUILD-METHOD.template.md`,
  `memory/guides/BUILD-METHOD.md`, `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`,
  each prints at least 1, and `wc -c` on `memory/guides/BUILD-METHOD.md` stays at or under 30720 bytes.
  Red when: a template is edited and its guide is not re-rendered.
  figure: 30720 is PINNED, M1's budget at base `ed497191`.

## 7. Gates

`unattended kit gate` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC1 AC2 · each autonomy value, each review.<stage> value and a placed and an undeclared boundary, staged against the base tree, which has no breakpoint list · none

New arm: tools/unattended/unattended.test.sh · covers AC3 AC5 · the planted major fork held at --close, and the owed, off and default opt-in readings, staged against the base driver, which reads only the README · none

The unattended kit's own suites are waived for this build's landing (README rule 8): the second arm is
declared here and read by the owner's run PLAY-dClosedLoop-13 names.

## 8. Open questions

- **F1 — Which forks does the ratification stand-in hold, when no fork carries a class?** Options: (a) every
  fork the agent resolved under delegation; (b) none until a class exists; (c) every fork. (b) fails the
  clause's seen-red case, a planted major fork that must reach a gate. (c) holds forks the owner resolved
  already. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
- **F2 — Does `review.design: owed` retire the README opt-in or sit beside it?** Options: (a) beside it, the
  README key deciding under `opt-in`; (b) retire the key and `SPEC_AUDIT_DEFAULT` into the policy value. (b)
  moves the owner's per-build channel and every reader of both keys, which the clause does not name.
  RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
  grants: PLAY-dClosedLoop-3 the policy source of the spec-audit opt-in, the --close and --phase owner-gate refusals and the breakpoint lines of --plan, and BUILD-METHOD M4's "When" naming review.design
- **F3 — Where is an owner gate held in today's driver?** Options: (a) at `--close` and at the `--phase` move
  past the gated step, the places a run crosses a step exit; (b) only at `--close`. (b) lets a `three-gates`
  design gate pass the whole build before it holds. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 19, flow-steps.md:516-562 and :302-317,
  layer-flow.md:299-303, and the driver's opt-in derivation, `print_spec_audit_line`, hold codes and
  `plan_state` read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-52, a hands-off TOOL-dDeclaredLoop-53, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.

## 10. Reuse audit

The owner gate reuses what holds a run for the owner today: the `owner-decision` hold
(`tools/unattended/unattended.sh:1029`) on a `decision` park (`:893`), released through
`check_owner_disposition`, which `TOOL-dDeclaredLoop-31` adds for the exhaustion record. The review breakpoint
reuses `TOOL-dDeclaredLoop-20`'s `--trigger` and so dFairHearing's harness. The spec-audit derivation is
extended in place (`check_authorization`, `:3927`), its two sources kept, and the forks are read by
`plan_state`'s grammar (`:4458-4467`). The list itself is new: no breakpoint list exists, as the scout's
probe found (`git grep -i "autonomy\|owner gate\|breakpoint" -- tools` names no reader).

`python tools/codebase-map/reuse_lookup.py "hold an owner gate until the owner disposition record"` ranked
`records` (`tools/memory-tree/gotchas.py`), `holder` (`tools/hooks/agent-cap.js`), `read_records` and
`check_gate_wall`; none holds a gate for an owner, and the driver's hold codes above are the seam.
`python tools/memory-recall/query.py "how does an owner gate hold a build until the owner decides"` returned
the scout record's row for this unit, the packet's clause, and `TOOL-dUnstuckLanding-3`'s ask on
`owner-decision` holds, which agrees with source: `--code owner-decision` with no `decision` park is refused.
The scout's README read at `:3963-3980` agrees with source; the derivation runs on to `:4040`.

Recall terms used: owner gate breakpoint park decision autonomy spec-audit opt-in ratify disposition record PARK_KINDS_OWED
