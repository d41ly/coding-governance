# TOOL-dPlacedRequest-7 — the probe program: eight items, the `probe` and `probe-trigger` records, and the four `probe.*` keys

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 15 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0125@4e0727e5 whole
**Carries:** node:item.probe.trigger
**Carries:** node:item.probe.pin
**Carries:** node:item.probe.design
**Carries:** node:item.probe.experiment
**Carries:** node:item.probe.run
**Carries:** node:item.probe.judge
**Carries:** node:item.probe.judge-claimed
**Carries:** node:item.probe.return
**Carries:** node:record-kind.probe
**Carries:** node:record-kind.probe-trigger
**Carries:** node:policy-key.probe.points
**Carries:** node:policy-key.probe.raise
**Carries:** node:policy-key.probe.observations
**Carries:** node:policy-key.probe.experiment.authority

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

No testing happens outside Test: an owner's observation cannot be verified before placement, a
reported bug cannot be made red before its fix, no experiment can set a measured reference, and 61 of
81 items have no role that could ask for a test (gap-flow-18). The unattended driver's `TESTING`
position exists only as a phase word (`tools/unattended/unattended.sh:852`). P31 makes testing a
program with two ways in (v2:1024-1028): placed at an item boundary by `probe.points` or the owner, or
raised by a role's `probe` outcome under `probe.raise`. This unit lands flow-steps' `[probe]`
program (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:605-675`):
its eight items, the `probe` and `probe-trigger` record kinds, the commands behind `probe.trigger`,
`probe.pin`, `probe.run`, `probe.judge` and `probe.return`, the role steps `probe.design` and
`probe.experiment`, its record handed to the asking item, an
entry-time probe keyed by content as triage is, the four keys, and a stand-in for each later part.

## 2. Scope (IN)

- **S1** — The items: eight `[[item]]` rows of `tools/loop/loop.toml` in TOOL-dDeclaredLoop-12 S1's
  shape, tags `item.probe.trigger`, `.pin`, `.design`, `.experiment`, `.run`, `.judge`,
  `.judge-claimed` and `.return` (I17), each with the actor, needs, witness, outcomes and routes of
  flow-steps.md:632-639, as §4's table states, and `step = "none"`. `check_program`'s admission of
  `step = "none"`, which TOOL-dDeclaredLoop-50 S3 grants rows whose tag's middle segment is `review`,
  reads the tuple `PROGRAM_SEGMENTS = ("review", "probe")` in `tools/loop/loop_lib.py`. Observed by AC1.
- **S2** — The stand-ins, flow-steps.md:666-675, as `[[stand-in]]` rows (TOOL-dDeclaredLoop-13's
  table, read by `read_stand_ins`): `item.probe.design` and `item.probe.judge-claimed` owned by
  dWitnessedBar's tester, `item.probe.experiment` by dBoundRoles' `experiment` shape, each routing
  its work to an owner item until its owner lands; `item.probe.run` by dWellOiledMachine's executor,
  its stand-in TOOL-dDeclaredLoop-17 S4's re-run; `item.probe.return` by dTotalRecall's `record`
  command, its stand-in S5's write through the record factory; and a visual verification, which
  needs dWellOiledMachine's capture adapter, `unrunnable`. Observed by AC1 and AC6.
- **S3** — `probe.trigger`, the verb `python tools/loop/probe.py trigger --cause <c> --asker <item tag>
  --subject <text> (--build <slug> | --request <content key>) [--at <item tag>]`, in
  `review.trigger`'s flag shape (TOOL-dDeclaredLoop-20 S2). `<c>` is one of the closed set I17 names,
  `point`, `owner`, `observation`, `raised` and `reproduction`, held as data: `[[trigger-cause]]` rows
  of `tools/loop/loop.toml`, each `program = "probe"` and `cause`, read by `read_trigger_causes(program)`.
  It opens the probe and writes a `probe-trigger` record, or prints `probe — not opened · <key>: <why>`
  when a key below refuses the cause, writing nothing. Observed by AC2 and AC3.
- **S4** — `probe.pin`, `python tools/loop/probe.py pin --trigger <record> --sha <sha> --kind
  verification|reproduction|experiment --question <text> --losing <text>`, writes the `probe` record's
  head (`Sha`, `Kind`, `Question`, `Losing`, `Asker`, `Trigger`) and commits it alone, subject
  `probe pin(<asker>): <kind>`, before any command runs; a SHA that does not resolve exits 2. An
  experiment routes to `item.probe.experiment`, the others to `item.probe.design`. Observed by AC4.
- **S5** — `probe.run`, `probe.judge` and `probe.return`. `python tools/loop/probe.py run --probe
  <record>` reads the method `item.probe.design` declared (each command and its predicted
  `<exit>:<hash>`), calls TOOL-dDeclaredLoop-17's `loop_witness.py rerun --sha <pinned> --cmd <c>
  --expect <exit>:<hash>` once, never a second runner, and writes each `run · <exit> · <hash> ·
  <command>` line. `judge` reads the re-run's per-command answers: every one `confirmed` is
  `confirmed`, any `refuted` is `refuted`, otherwise `inconclusive`; a method marked `judge = claimed`
  routes to `item.probe.judge-claimed`. `return` writes `Verdict` and `Writer` (`stand-in` until the
  executor lands) and prints `probe — <verdict> · <record> · to <asker>`, the line the asking item's
  re-entry reads as its input (flow-steps.md:35-36); a `claimed` or `unrunnable` verdict routes to an
  owner item. Observed by AC5 and AC6.
- **S6** — The record kinds, rows of the record factory `tools/memory-tree/build_records.py`
  (PLAY-dOrderedCharter-7 S7), copying TOOL-dDeclaredLoop-17 S1's `acceptance` row:
  `record-kind.probe-trigger`, `<date>-build-<unit id>-probe-trigger-<n>.md`, fields `Cause`,
  `Asker`, `Subject`, `At` and `Key`; and `record-kind.probe`, `<date>-build-<unit id>-probe-<n>.md`,
  fields `Sha`, `Kind`, `Question`, `Losing`, `Asker`, `Trigger`, `Verdict`, `Writer` and the `run`
  lines. `Verdict` is closed per `Kind`: `confirmed`, `refuted`, `inconclusive`, `unrunnable` for a
  verification or a reproduction, `measured`, `within-noise`, `aborted`, `unrunnable` for an
  experiment (flow-steps.md:622-624). Observed by AC7.
- **S7** — The entry-time probe. Before `entry.claim` no build folder exists, so a trigger given
  `--request <content key>`, the key TOOL-dPlacedRequest-19's `request_content_key` derives (I11),
  writes its records beside that request's local text (I12):
  `<git-common-dir>/requests/<content key>.probe-trigger.md` and `<content key>.probe.md`, in the
  record kinds' field grammar, minting no id (flow-steps.md:632). A request holds one entry-time
  probe: a trigger for a key whose probe is open with a new subject joins it, adding its `Subject`
  line and printing `probe — joined · <record>`, so placement may trigger once per observation; the
  same subject again exits 1 as already opened. The design then declares a command per subject, and
  the judge's aggregate verdict covers them all. Observed by AC8.
- **S8** — The `probe` outcome on every role item: each `[[item]]` row whose actor is a role and whose
  `outcomes` is a list gains `probe`, routed to `item.probe.trigger` (flow-steps.md:35-36); a check
  `check_probe_outcomes(items)` in `tools/loop/loop_lib.py` refuses a role item lacking it. Until
  dBoundRoles puts the outcome on the role templates, no role returns it, so probes are placed, never
  raised (flow-steps.md:672). Observed by AC9.
- **S9** — The keys, each read through dGroundRules' `policy.py get` (I24), with v2's catalogue
  default until that reader lands, their rows added through TOOL-dDeclaredLoop-6 S4's
  `python tools/playbook/core.py new policy-key … --owner dPlacedRequest` (v2:1248-1251):
  `probe.points` (default `none`), a set of item tags in `review.breakpoints`' grammar, read through
  TOOL-dDeclaredLoop-26 S6's `read_tag_policy`, listed by `probe.py points --build <slug>`, a tag the
  loop definition does not declare refused naming the key; `probe.raise` (`roles-and-owner`,
  `owner-only`, `off`), refusing `raised` under `owner-only` and `off`, and `owner` under `off`;
  `probe.observations` (`verify-before-place`, `verify-at-plan`, `on-request`), admitting the cause
  `observation` at `--at item.entry.place` under `verify-before-place`, at `item.plan.input` under
  `verify-at-plan`, and only with the owner's request under `on-request`; and
  `probe.experiment.authority` (`within-cap`, `owner-opts-in`, `free`), named with its value on the
  owner item an experiment routes to, the cap under `within-cap` being the agent cap
  `tools/hooks/agent-cap.js` enforces (:61-71). Observed by AC3 and AC10.
- **S10** — The fixture, `python tools/loop/probe.py --fixture --plant <case>`, a throwaway repository
  in the system temp directory with a stub policy kit and a pinned commit, each case printing its
  observation; the leg `loop probe fixtures` runs every case, and the page `help/loop.md` gains the
  probe's section. Observed by AC1 to AC11.

## 3. Non-goals (OUT)

- Test's landing verdict: only `test.verdict`'s runner-written record gates a landing; no probe
  verdict feeds `deploy.current`, and seen-red stays Test's record kind (night-pass.md:180-182).
- The tester, the `experiment` shape, the scorer factory's experiment judging, the executor, the
  visual capture adapter and the `record` command: dWitnessedBar's, dBoundRoles', dFairHearing's,
  dWellOiledMachine's and dTotalRecall's; S2 names each stand-in.
- The `probe` outcome on the role templates: dFurnishedOrders' `cl-dClosedLoop-0206`.
- Where placement routes an observation: TOOL-dPlacedRequest-4's `entry.place`, which calls S3 with
  `--cause observation --at item.entry.place`.
- `review.trigger`'s own cause set: the `[[trigger-cause]]` table admits a `program = "review"` row,
  and moving the driver's literal set onto it re-points its readers, the driver's verb and the review
  harness, which is not this clause's.
- Firing a probe point at its boundary: the executor's; `probe.py points` lists them and S3 opens one.
- Publishing an entry-time record: it stays on the typing node with the request until
  dWellOiledMachine publishes the request redacted.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-19` — `request_content_key`, the key an entry-time trigger and its records are filed under beside the request's local text
- **hands-off** `TOOL-dPlacedRequest-4` — `item.probe.trigger`, which `entry.place` routes an owner's observation to under `probe.observations`, receiving the probe's record back
- **hands-off** `TOOL-dPlacedRequest-3` — `item.probe.trigger`, the route target of the entry items' `probe` outcome, which the entry rows declare
- **consumes-from** external — dDeclaredLoop, built before this build run: the item rows and `check_program` (TOOL-dDeclaredLoop-12, -50 S3), `read_stand_ins` (TOOL-dDeclaredLoop-13), `loop_witness.py rerun` (TOOL-dDeclaredLoop-17 S4), `review.trigger`'s flag shape (TOOL-dDeclaredLoop-20 S2), `read_tag_policy` (TOOL-dDeclaredLoop-26 S6), the policy-key factory (TOOL-dDeclaredLoop-6 S4)
- **consumes-from** external — the record factory (PLAY-dOrderedCharter-7 S7) and dGroundRules' `policy.py get`
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### The items

| Item | Actor | Needs | Witness | Routes |
|---|---|---|---|---|
| `item.probe.trigger` | `command:probe.py trigger` | none | the `probe-trigger` record | opened → `item.probe.pin`; not-opened → the asker's next item |
| `item.probe.pin` | `command:probe.py pin` | `item.probe.trigger` | the head's commit, before any run | verification, reproduction → `item.probe.design`; experiment → `item.probe.experiment` |
| `item.probe.design` | `role:tester` | `item.probe.pin` | the method's schema check | done → `item.probe.run` |
| `item.probe.experiment` | `role:researcher` | `item.probe.pin` | the method's schema check | done → `item.probe.run`; beyond-authority → owner item |
| `item.probe.run` | `executor` | `item.probe.design` or `item.probe.experiment` | the `run` lines by hash | done → `item.probe.judge`; unrunnable → `item.probe.return` |
| `item.probe.judge` | `command:probe.py judge` | `item.probe.run` | the computed verdict | judged → `item.probe.return`; claimed → `item.probe.judge-claimed` |
| `item.probe.judge-claimed` | `role:tester` | `item.probe.judge` | the judgment's schema check, held as claimed | done → `item.probe.return` |
| `item.probe.return` | `command:probe.py return` | `item.probe.judge` | the `probe` record | returned → the asker's re-entry; claimed, unrunnable → owner item |

"Owner item" is the route `stand-in:tools/unattended/unattended.sh`, its `--park` under a mandate and
the owner's own turn when attended, until the owner gate of dDeclaredLoop's breakpoints arms it.

### The trigger's refusals

| Cause | Refused when |
|---|---|
| `point` | `--at` is not in `probe.points` |
| `owner` | `probe.raise` is `off` |
| `observation` | `--at` is not the position `probe.observations` admits |
| `raised` | `probe.raise` is `owner-only` or `off` |
| `reproduction` | never; a patch build's red-first reproduction (`cl-dClosedLoop-0408`) |

### The records

```
**Serves:** journal TOOL-dExample-2

**Cause:** observation
**Asker:** item.entry.place
**Subject:** the owner reports the card drops its route after a compaction
**At:** item.entry.place
**Key:** 3f9c2a71d0e4
```

```
**Serves:** journal TOOL-dExample-2

**Sha:** 3f9c2a71
**Kind:** reproduction
**Question:** does a compaction drop the card's route?
**Losing:** the replayed card keeps its ## route
**Asker:** item.entry.place
**Trigger:** 2026-10-25-build-TOOL-dExample-2-probe-trigger-1
**Verdict:** confirmed
**Writer:** stand-in
- run · 1 · 9c0e5a1b2f33 · bash replay-case.sh
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/probe.py` | module | none declared for files |
| `trigger`, `pin`, `design`, `run`, `judge`, `return`, `points` | verbs of `probe.py` | none |
| `read_trigger_causes`, `check_probe_outcomes` | functions | `py.function`, OK |
| `PROGRAM_SEGMENTS` | constant | none declared |
| `[[trigger-cause]]` | table of `loop.toml` | none |
| the eight `item.probe.*` tags | item tags | graded by `gov_tag.py check` |
| `probe`, `probe-trigger` | record kinds | none |
| `loop probe fixtures` | leg | none |

### Migration

None: no probe exists before this unit, and the `probe` outcome on existing rows is additive.

### Rollout

Live at landing, placed only: probes open from the owner, `probe.points` and placement's
observations; no role raises one until dBoundRoles lands the outcome on the templates.

### Files touched (estimate)

- `tools/loop/probe.py`
- `tools/loop/loop.toml`: the eight rows, the `[[stand-in]]` and `[[trigger-cause]]` rows, `probe` on the role rows
- `tools/loop/loop_lib.py`: `PROGRAM_SEGMENTS`, `read_trigger_causes`, `check_probe_outcomes`
- `tools/loop/kit.toml`: the module and the leg
- `tools/memory-tree/build_records.py`: the two kind rows
- `tools/policy/catalogue.toml`: four rows, through the factory
- `.governance/policy.json`: the mirror, regenerated in its own commit
- `tools/gate-legs.json`: the leg `loop probe fixtures`, argv `python {prefix}/loop/probe.py --fixture`
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `tools/run-gates/ceiling-evidence.txt`: the new leg's row
- `memory/map/features/loop.md`: the module's claim and the leg
- `help/loop.md`: the probe's section

### Alternatives rejected

- **A second runner in `probe.py`.** TOOL-dDeclaredLoop-17 S4's `rerun` already answers the
  verification vocabulary at a pinned SHA; its §3 hands `probe.run` and `probe.judge` here by name.
- **A probe step.** Testing is not a step (flow-steps.md:607); the rows ride `step = "none"` as the
  breakpoint program's do.
- **A second record kind for an experiment's reference.** The experiment's probe record is the
  measured reference (night-pass.md:180-182).

## 5. Production-readiness checklist

- security — the re-run executes the method's commands in a detached worktree at the pinned SHA
  under a timeout (TOOL-dDeclaredLoop-17 S2); the method is declared by a role or the owner, never by
  the asker's reasoning; an entry-time record stays on its node with the request text.
- perf / scale — one re-run per probe; an experiment never runs before its shape lands.
- error / empty / loading states — a refused cause writes nothing and names the key; an unresolved
  SHA exits 2; a visual verification is `unrunnable`, routed to the owner.
- observability — each verb prints one `probe —` line naming the record and the route taken.
- risks — a claimed verdict is held as claimed and goes to the owner, never fed to a gate.
- testing — S10's plants, red and green.
- migration — none.
- user docs — `help/loop.md` gains the probe's section.

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --check` runs over the tree, it passes with the eight
  `item.probe.*` rows at `step = "none"` and the five `[[stand-in]]` rows of S2, and the plant
  `probe-step` with an `item.plan.x` row at `step = "none"` exits 1 naming it.
  Red when: a probe row is refused for its step, or the admission widens past the two segments.
- **AC2** — When `python probe.py --fixture --plant trigger-causes` runs `trigger --cause hunch`, it
  exits 2 naming the five causes `read_trigger_causes("probe")` returns, and `trigger --cause owner`
  writes one `probe-trigger` record.
  Red when: a cause outside the rows opens a probe, or the set is typed in `probe.py`.
- **AC3** — When the plants `raise-owner-only`, `raise-off`, `points-unlisted` and
  `observation-at-plan` run their refused cause, each prints `probe — not opened` naming its key and
  `git status --porcelain` prints nothing; each value's admitted case opens.
  Red when: a key's value does not move what opens.
- **AC4** — When the plant `pin` pins a verification, `git log -1 --format=%s` in the fixture reads
  `probe pin(item.entry.place): verification` and that commit holds the record's `Losing` field while
  no `run` line exists yet; an unresolvable `--sha` exits 2.
  Red when: a command runs before the losing outcome is committed.
- **AC5** — When the plant `run-judge` pins a reproduction whose method predicts the planted failing
  command's exit and hash, `run` then `judge` then `return` write `Verdict: confirmed`, and the plant
  `run-refuted`, whose prediction differs, writes `refuted`; `return` prints `probe — <verdict> ·
  <record> · to item.entry.place`.
  Red when: the verdict is typed rather than computed from the re-run, or the record does not name its asker.
- **AC6** — When the plant `visual` pins a verification of kind visual, `run` routes to `return`
  with `Verdict: unrunnable` and the owner-item route; the plant `experiment` routes `pin` to
  `item.probe.experiment`, whose stand-in prints the owner item naming dBoundRoles.
  Red when: an unbuilt part runs as if it were built.
- **AC7** — When `python build_records.py read` runs over the AC5 fixture's records, both grade
  clean, and a plant `verdict-cross` writing `measured` on a reproduction is refused naming `Verdict`.
  Red when: a verdict outside its kind's set is admitted.
- **AC8** — When the plant `entry-time` runs `trigger --cause observation --request 3f9c2a71d0e4 --at
  item.entry.place`, the record lands at `requests/3f9c2a71d0e4.probe-trigger.md` under the
  fixture's git common dir, no build folder gains a file, a second observation's trigger prints
  `probe — joined` and adds its `Subject` line to that record, and the first trigger again exits 1 as
  already opened.
  Red when: an entry-time probe mints an id or writes into a build folder.
- **AC9** — When the plant `role-no-probe` removes `probe` from one role item's outcomes,
  `loop_lib.py --check` exits 1 naming the item, and over the tree every role item with a listed
  outcome set routes `probe` to `item.probe.trigger`.
  Red when: a role item cannot ask for a test.
- **AC10** — When `python -c "import tomllib, sys; print(sorted(r['name'] for r in tomllib.load(open(sys.argv[1], 'rb'))['key'] if r['name'].startswith('probe.')))" catalogue.toml`
  runs in the policy kit's directory, it prints `probe.experiment.authority`, `probe.observations`,
  `probe.points` and `probe.raise`, and `git grep -n "probe.raise" -- probe.py`, run in the loop kit's
  directory, finds a literal-key read.
  Red when: a key has no row, or is read in a shape the reader-coverage arm does not count.
  fixture: the catalogue is dGroundRules', untracked until it builds.
- **AC11** — When `grep -n "probe.observations" loop.md` runs in `help/`, it finds the probe section
  naming the two ways in and the four keys.
  Red when: the program lands and the page does not say how a probe opens.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/probe.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the `loop probe fixtures` leg running every `--fixture` case, its failing case staged by `run-refuted` against a predicted `confirmed` · none

New arm: tools/loop/loop_lib.py · covers AC1 AC9 · the `probe-step` and `role-no-probe` cases under the `loop definition` leg, the failing case staged by `role-no-probe` · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that
  legal?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-25:
  the tuple does not hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it.
  RESOLVED (agent, 2026-10-25, delegated): `OPEN`.
- **F2 — Where does an entry-time probe's record live, when no build folder exists and the trigger
  "mints no id"?** Options: (a) beside the request's local text, keyed by its content key; (b) on the
  request ref's commit; (c) in a scratch build folder. (b) pushes a subject the request's text is
  withheld from the remote to protect (`cl-dClosedLoop-0137`); (c) mints a build before placement.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the survivor, the home I12 gives the request's
  own text.
- **F3 — The cause set "as data": does `review.trigger`'s literal set move onto the table here?**
  Options: (a) the table with a `program` column, probe's rows only; (b) both programs' rows, the
  driver's verb and the review harness re-pointed. (b) re-points a parent's two readers outside this
  clause. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3; the `program` column is what lets
  review's rows join without a second table.

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 7, flow-steps' `[probe]`, P31 and
  v2:1248-1251.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: AC10's grep names the module by its basename,
  run in the loop kit's directory.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-34,
  each the mirror of that promoted unit's own edge.

## 10. Reuse audit

The seams extended are the item rows and their program check (TOOL-dDeclaredLoop-12, -50 S3), the
stand-in table (TOOL-dDeclaredLoop-13), the re-run primitive `loop_witness.py rerun`
(TOOL-dDeclaredLoop-17 S4), whose §3 names `probe.run` and `probe.judge` as this build's, the
trigger verb's shape (TOOL-dDeclaredLoop-20 S2), `read_tag_policy` (TOOL-dDeclaredLoop-26 S6) for
`probe.points` in `review.breakpoints`' grammar, and the record factory (PLAY-dOrderedCharter-7 S7).
Scout C's row holds against source: `TESTING` is a phase word with no reader
(`tools/unattended/unattended.sh:852`), and `read_preflight_probes` reads background handles, not
probes. `python tools/codebase-map/reuse_lookup.py "pin a subject by sha, run commands and judge the
verdict against a losing outcome"` ranked name stems (`run`, `run_arms`, `run_git`,
`classify_outcome`), none a pinned re-run, so the parents' specs hold every seam.

Recall terms used: `python tools/memory-recall/query.py "how is a probe triggered pinned run and judged" --terms "probe.trigger probe.pin probe.run probe.judge loop_witness rerun confirmed refuted inconclusive probe.raise probe.points"`
