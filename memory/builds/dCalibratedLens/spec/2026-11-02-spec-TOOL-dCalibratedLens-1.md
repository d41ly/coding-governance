# TOOL-dCalibratedLens-1 — each stage review's lenses and effort: four stage literals in the lens catalogue, chosen by the breakpoint's stage, run at `review.<stage>.effort`

**Status:** OPEN · rev-3 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 16 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0458@5429e502 whole
**Carries:** node:policy-key.review.<stage>.effort

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-1-reuse-scout.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-1-reuse-scout.md) | journal | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-2-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-2-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-3-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-3-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-edge-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-edge-fix-brief.md) | research | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-15 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md) | research | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

Review exists at two stages only, and Plan, Test, Deploy and Maintain have none (`gap-review-01`,
HIGH). dDeclaredLoop places a review breakpoint for each stage and dFairHearing gives the harness a
lens catalogue and presets, but no catalogue row is a lens of those four stages, and the effort a
stage review runs at is read for the Design review alone (TOOL-dIndexedDesign-3 §8 F7 hands the rest
here). This unit adds four five-slot literals to dFairHearing's catalogue, `plan`, `test`, `deploy`
and `maintain`, selects one by the stage of the breakpoint that fires, and runs every stage review at
`review.<stage>.effort`, the key this build owns.

## 2. Scope (IN)

- **S1** — Four literals in `tools/workflows/tier2-review.template.js`: `PLAN_LENSES`,
  `TEST_LENSES`, `DEPLOY_LENSES` and `MAINTAIN_LENSES`, each opening with the marker
  `// gov:lens-slots <stage>` and holding the single line `{{LENS_SLOTS}}`, the form
  TOOL-dFairHearing-13 S3 gives the other literals. `PRESETS` (TOOL-dFairHearing-2 S1) gains the four
  names, and the marked receiver `const LENSES = ... // gov:fixed-verifiers` gains one ternary arm per
  literal. `tools/workflows/tier2-review.js` is re-rendered. Observed by AC1, AC2 and AC3.
- **S2** — The rows, in `tools/workflows/lenses.toml`, as §4 "The rows" tabulates: fourteen new rows,
  each `kinds = ["spec-audit"]`, `optin = false`, and `presets` and `default_in` naming its one stage;
  and three of TOOL-dFairHearing-2 S3's design-audit rows, `grounding`, `coherence` and
  `failure-envelope`, gaining the stages §4 names in their `presets` and `default_in`. Every stage
  literal fills exactly five slots. Observed by AC1 and AC2.
- **S3** — (amended, id 43) The stage reaches the preset. `tools/workflows/review_pin.py` (TOOL-dFairHearing-3 S8)
  takes `--stage <stage>`: a stage that a `gov:lens-slots` marker of the rendered harness beside it
  declares prints that literal as `preset`; `design` and `build`, which no marker names, leave the
  subject mapping as it is; any other value exits 2 naming the stage and the marked literals. The
  marker set is read by `read_lens_literals` from the rendered `tier2-review.js`, the way
  `read_spec_subject_path` reads `SPEC_SUBJECT_PATH`. `PLAN_RECORD_PRESET` (TOOL-dRankedPlan-6 S1)
  takes the value `plan`, so a plan subject with no `--stage` runs the Plan literal. Observed by AC4
  and AC5.
- **S4** — The effort. In `resolve_stage_efforts` (`tools/roles/roles_lib.py:596-601`), TOOL-dIndexedDesign-3
  S4's step 1a reads `review.<stage>.effort` through `read_policy_setting(f"review.{stage}.effort", root)`
  for the review stage keys of the call, where `stage` is the new `review_stage` argument, and absent
  it is `design` for a workflow of `DESIGN_REVIEW_WORKFLOWS` and `build` for one of
  `BUILD_REVIEW_WORKFLOWS = ("closing-review",)`. The review stage keys are the `stages` map of
  `spec-review` for every stage but `build`, and of `closing-review` for `build`
  (`tools/roles/workflows.toml:47`, `:67`). `python tools/roles/handoff.py stage-efforts <workflow>
  --review-stage <stage>` passes it. A stage outside `REVIEW_STAGES`, a stage the workflow's kind
  cannot run, and a level outside `EFFORT_LEVELS` (`tools/roles/roles_lib.py:45`) each raise a
  `RolesError` naming the key. Observed by AC6, AC7 and AC8.
- **S5** — The breakpoint carries its stage. TOOL-dDeclaredLoop-20 S2's `--trigger` verb in
  `tools/unattended/unattended.sh` takes `--stage <stage>`, passes it to `review_pin.py`, and adds
  `efforts` to the JSON line it prints, the output of `handoff.py stage-efforts <workflow>
  --review-stage <stage>` with `<workflow>` `closing-review` for `build` and `spec-review` otherwise.
  TOOL-dDeclaredLoop-19 S6's firing site passes the step segment of the breakpoint's `position` tag
  (`item.<step>.<name>`) as `--stage`. Observed by AC9.
- **S6** — The catalogue row. The `review.<stage>.effort` row (`tools/policy/catalogue.toml:1241-1245`)
  gains `summary` and `usage`, its `allowed` and `default` unchanged, and `python tools/policy/policy.py
  lists --write` drains the name from `tools/policy/unsummarised-keys.txt` (`:179`). Observed by AC10.
- **S7** — The docs: `tools/workflows/README.md` names the four stage literals and `--stage`;
  `tools/roles/README.md`'s effort section (`:171-190`) states step 1a per stage and `--review-stage`;
  `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`, states
  `--trigger`'s `--stage`; `help/policy.md`'s key table (`:206-213`) gains the key's row. Observed by
  AC11.

**Build-run precondition.** TOOL-dFairHearing-13, -2 and -3, TOOL-dRankedPlan-6, TOOL-dIndexedDesign-3,
TOOL-dBoundRoles-21, TOOL-dDeclaredLoop-19 and -20 are DEFERRED at `8bec4cef`. The build run builds
this unit once each is CLOSED, and re-grounds every line this spec cites against its base.

## 3. Non-goals (OUT)

- Where a stage's breakpoint sits, when it fires and who disposes it: TOOL-dDeclaredLoop-19's
  `derive_breakpoints` and `review.<stage>`, read as built. A Maintain review runs where
  `review.breakpoints` places one at an `item.maintain.*` boundary (TOOL-dDeclaredLoop-19 S4);
  `review.maintain` itself is read by no row of `derive_breakpoints`, and §8 F4 files that as an ask
  on dDeclaredLoop.
- The Design review's lenses and the spec-audit presets: TOOL-dFairHearing-2 and its replay. The
  Build review keeps the diff literal; this unit reads its effort only.
- The opt-in swap, the lens notes after a swap and the six opt-in rows: TOOL-dFairHearing-3 and -9.
  `review.opt-in` keys a swap by literal name, so it already reaches a stage literal.
- A losing test for any new row. Every row ships as the default of a literal no breakpoint fires
  until its stage opts in or is owed (`review.<stage>` defaults `opt-in`), and the Loop Review's ledger
  is where a stage lens is priced (TOOL-dCalibratedLens-2). The six owed opt-in tests stay the ask
  TOOL-dFairHearing-3 S11 files.
- The `lens` kind, its namespace and its step-gate class: TOOL-dCalibratedLens-13.
- Lens removal and repository lenses: TOOL-dCalibratedLens-14.
- `REVIEW_SHAPE` and the kit `version:`, minted at landing.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-13` — the `kind.lens` row and `lens.<key>` tags, under which the fourteen new rows are tagged once that unit lands
- **consumes-from** external — TOOL-dFairHearing-13, -2 and -3: the catalogue, `render_lenses.py`, the `gov:lens-slots` marker, `PRESETS`, the design-audit rows and `review_pin.py`; without them there is no row to add and no preset to print
- **consumes-from** external — TOOL-dRankedPlan-6 S1, `PLAN_RECORD_PRESET`, whose value this unit sets
- **consumes-from** external — TOOL-dIndexedDesign-3 S4's step 1a and TOOL-dBoundRoles-21's `read_policy_setting`, the effort order this unit widens from one stage to six
- **consumes-from** external — TOOL-dDeclaredLoop-19 and -20: `derive_breakpoints`, the firing site and `--trigger`
- **hands-off** external — dDeclaredLoop reads `review.maintain` in `derive_breakpoints` (§8 F4's ask)
- **hands-off** `TOOL-dCalibratedLens-24` — the rendered `tools/workflows/tier2-review.js` and its stage receiver, which that unit feeds to the hook beside a looped copy (id 16)

## 4. Design

**Waits on:** TOOL-dFairHearing-13, TOOL-dFairHearing-2, TOOL-dFairHearing-3, TOOL-dRankedPlan-6,
TOOL-dIndexedDesign-3, TOOL-dBoundRoles-21, TOOL-dDeclaredLoop-19 and TOOL-dDeclaredLoop-20, each
DEFERRED at base. This unit specs none of their primitives and names each where it reads one.

### Evidence

- The harness's literals sit at `tools/workflows/tier2-review.template.js:781` (`DIFF_LENSES`) and
  `:817` (`SPEC_LENSES`), its receiver at `:849`, its `efforts` argument at `:260-277`. The live keys
  are `security`, `correctness`, `seams`, `verification`, `intent` and `coherence`, `grounding`,
  `reuse`, `blast-radius`, `failure-envelope`.
- `resolve_stage_efforts` (`tools/roles/roles_lib.py:596-601`) resolves a workflow's `stages` keys
  from `[effort.stages.<workflow>]`, else the slot's level; `print_stage_efforts`
  (`tools/roles/handoff.py:474-488`) prints it, keyed by workflow (`:954` parses the verb).
- `python tools/policy/policy.py get review.plan.effort` exits 2 at base, "the row
  review.<stage>.effort carries a derived default no reader computes yet": the `<stage>` placeholder
  matches `plan` (`tools/policy/policy.py:21-22`, `:222-238`), so one row answers every stage.
- v2's preset table sets `review.<stage>.effort` to the role's effort under every preset and lists
  `review.maintain` (v2:1656-1657). The review-system record says this build "draws its per-stage
  lenses from this catalogue, once Plan, Test, Deploy and Maintain have reviews to calibrate on.
  Today there are none" (review-system:174-175). The walkthrough names each stage's concerns:
  "Plan (order, dependencies, duplicates, readiness), Test (seen red, arms, cost, flakes), Deploy
  (what landed against the plan, release notes against the epoch, adopter updates), Maintain (fixes
  inside the declared set, detectors owned)" (walkthrough:712-714), and Plan Review "a lens over
  order, dependencies, duplicates, overlap with live work and readiness" (walkthrough:349-350).
- The receiver's nested ternary: TOOL-dFairHearing-2 §4 measured a three-literal ternary admitted by
  `node tools/hooks/agent-cap.js --only=scripts`. Seven literals are UNVERIFIED until the build pass;
  AC3 observes it.

### The rows

A row's `brief` is one line; the text below is the brief, its subject the record the stage's
`review.pin` pins. New rows carry `presets = default_in = ["<stage>"]`.

| Stage | Slot | Key | Row | Brief |
|---|---|---|---|---|
| plan | 1 | `order` | new | Order: does the plan's order follow from its priorities and dependencies? Cite each item placed ahead of what it needs, or behind what needs it, with both entries. |
| plan | 2 | `dependencies` | new | Dependencies: does every item name the parents and interfaces it expects, and does each parent exist and deliver that interface? Cite the item and the parent. |
| plan | 3 | `duplicates` | new | Duplicates: does an item restate another item, an open ask or a landed unit? Cite both. |
| plan | 4 | `overlap` | new | Overlap with live work: does an item touch a file or a node a live build already claims? Cite the item and the build. |
| plan | 5 | `readiness` | new | Readiness: can each item start as written, its acceptance an observation, its cut-line drawn and no fork left to its builder? Cite the item and what it lacks. |
| test | 1 | `seen-red` | new | Seen red: is every acceptance arm the stage claims recorded red on its planted break and green without it? Cite the arm whose red is asserted and not recorded. |
| test | 2 | `arms` | new | Arms: does each changed behaviour have an arm that fails when it breaks, exercising this change rather than an unrelated green? Cite the behaviour. |
| test | 3 | `cost` | new | Cost: what did the legs and suites cost against what they caught? Cite a leg whose time or tokens grew with no new catch. |
| test | 4 | `flakes` | new | Flakes: did a leg pass on retry or change verdict at one SHA? Cite the flake record and whether it was explained. |
| test | 5 | `grounding` | drawn | the design-audit row, `presets` and `default_in` gaining `test` |
| deploy | 1 | `landed-vs-plan` | new | Landed against the plan: does what landed match the plan's and the specs' scope, no unit missing and none extra? Cite the landing field and the record it disagrees with. |
| deploy | 2 | `release-notes` | new | Release notes: do the notes and kit versions name every user-facing change since the last epoch, and only those? Cite the change. |
| deploy | 3 | `adopter-updates` | new | Adopter updates: does every change an adopter must act on carry its upgrade step or help page? Cite the change and the missing step. |
| deploy | 4 | `grounding` | drawn | the design-audit row, gaining `deploy` |
| deploy | 5 | `coherence` | drawn | the design-audit row, gaining `deploy` |
| maintain | 1 | `fix-set` | new | Fixes inside the declared set: was every fix the period applied one `maintain.fixes` admits, and everything else filed rather than fixed? Cite the fix. |
| maintain | 2 | `detector-owners` | new | Detectors owned: does every reading and detector the period ran have an owner and a pin, and is a dead one filed? Cite the reading. |
| maintain | 3 | `grounding` | drawn | the design-audit row, gaining `maintain` |
| maintain | 4 | `coherence` | drawn | the design-audit row, gaining `maintain` |
| maintain | 5 | `failure-envelope` | drawn | the design-audit row, gaining `maintain` |

Slot order is file order (TOOL-dFairHearing-13 §4), so each stage's new rows sit in the table's order
and a drawn row fills its stage's slot after them, by the render's per-literal walk. The renderer's
rules hold unchanged: every kind is `spec-audit`, which rule 5 requires of a literal other than
`diff-review`; no key equals a literal name (rule 7); `cost` recurs only beside the opt-in `cost` row,
whose `presets` are disjoint from `test` (rule 6, TOOL-dFairHearing-13 §8 F2).

### The stage path

```
derive_breakpoints  -> {name, position = item.<step>.<x>, ...}           (TOOL-dDeclaredLoop-19)
firing site         -> --trigger <slug> --subject <s> --cause <c> --stage <step>
--trigger           -> review_pin.py --subject <s> ... --stage <step>    -> {"preset": "<step>" | mapped}
                    -> handoff.py stage-efforts <spec-review|closing-review> --review-stage <step>
                    -> prints {"preset", "optIn", "trigger", "blocks", "efforts"}
caller              -> tier2-review.js with those arguments
```

| `--stage` | Preset | Effort keys read |
|---|---|---|
| `plan`, `test`, `deploy`, `maintain` | the literal of that name | `review.<stage>.effort` for `specFinder`, `skeptic`, `synthesis` |
| `design` | TOOL-dFairHearing-3 S8's subject mapping | `review.design.effort`, as TOOL-dIndexedDesign-3 reads it |
| `build` | none printed; the diff kind takes no preset | `review.build.effort` for `diffFinder`, `skeptic`, `synthesis` |
| absent | the subject mapping, `PLAN_RECORD_PRESET` included | the workflow's default stage |
| anything else | exit 2 | `RolesError` |

### The effort order

| Step | Source | Applies to |
|---|---|---|
| 1 | `roles.effort.<w>.<s>` | every stage key (TOOL-dBoundRoles-21) |
| 1a | `review.<stage>.effort`, `<stage>` the call's review stage | the review stage keys of that stage's review workflow |
| 2 to 5 | `roles.effort.<r>` and the rest | TOOL-dBoundRoles-21 §4, unchanged |

The key is read once per call. `REVIEW_STAGES = ("plan", "design", "build", "test", "deploy",
"maintain")` is the closed set; `build` runs only under `closing-review`, every other stage only under
`spec-review` or `spec-write`, and a mismatch names both. An unset key leaves steps 2 to 5 to decide,
which is the catalogue's derived default, "the role's declared effort".

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `PLAN_LENSES`, `TEST_LENSES`, `DEPLOY_LENSES`, `MAINTAIN_LENSES` | JS constants, the template | none declared for a JS constant |
| `plan`, `test`, `deploy`, `maintain` | literal names, `PRESETS` members | none |
| the fourteen keys of §4 "The rows" | lens keys | the catalogue's key pattern |
| `read_lens_literals` | Python function, `review_pin.py` | `py.function`, `--suggest` OK |
| `REVIEW_STAGES`, `BUILD_REVIEW_WORKFLOWS` | Python constants, `roles_lib.py` | `py.constant` is undeclared in `.lexicon.conf` |
| `--stage` | flag of `review_pin.py` and of `--trigger` | none |
| `--review-stage` | flag of `handoff.py stage-efforts` | none |

### Migration

None. An unset `review.<stage>.effort` reads as today; a call with no `--stage` maps its subject as
today, but a plan subject now runs the Plan literal where it ran `unit-spec`.

### Rollout

One landing, after the parents. Every stage review stays opt-in under the default preset, so no run
spawns a stage lens until the owner opts a stage in or a preset owes it.

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 16 · AC3, §4 Evidence (H6, `TOOL-dCalibratedLens-24`)** — AC3 feeds the hook a payload:
  `node -e` builds
  `{"tool_name": "Workflow", "tool_input": {"script": <the text of tools/workflows/tier2-review.js>}}`,
  as `tools/workflows/check-verifier-fanout.sh:321-326` builds it, and pipes it to
  `node tools/hooks/agent-cap.js --only=scripts`, which exits 0. A bare invocation reads no harness:
  the hook exits 0 on an unparsable stdin (`tools/hooks/agent-cap.js:1853-1858`), so §4 Evidence's
  citation of TOOL-dFairHearing-2's measurement through that command measured nothing, and the
  seven-literal receiver stays UNVERIFIED until AC3 runs with the payload. The red twin over a
  looped receiver is `TOOL-dCalibratedLens-24`'s.
- **id 4 · §7 (H5, `TOOL-dCalibratedLens-23`)** — This unit edits
  `tools/workflows/tier2-review.template.js` and `tools/workflows/lenses.toml`, both in the guard of
  TOOL-dCalibratedLens-10's held leg `instruction-eval`, so the seed case is owed from this pass. It
  is the build's last unit to edit a guard path: after it builds, the main loop records one replay
  of every owed case through the procedure TOOL-dCalibratedLens-10 S8 writes into
  `tools/workflows/README.md`, before the close bar.
- **id 43 · S3, §7 New arm, AC11 (M23, `TOOL-dCalibratedLens-30`)** — Moving `PLAN_RECORD_PRESET`
  from `unit-spec` to `plan` flips three arms of TOOL-dRankedPlan-6 in
  `tools/workflows/tier2-review.test.sh`: its AC1 now expects `{"preset": "plan"}`, its AC3 five
  spawns at the Plan lens keys, and its AC4 a `gov:lens-slots` marker naming the Plan literal; the
  first `New arm:` line covers those flips. `help/loop.md`'s Plan Review paragraph, which says the
  preset stays `unit-spec` until this build's Plan lenses land, is rewritten in this pass, and AC11
  also runs `grep -c 'PLAN_LENSES' help/loop.md`, at least 1.

### Amendments (round-2 spec audit)

The round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Its ids restart at 1, so each bullet
spells `r2 id`; each supersedes the text it names, and the unit it names owns the finding and its
proof.

- **r2 id 15 · AC3 (M8, `TOOL-dCalibratedLens-41`)** — AC3's own text carries the `node -e` payload
  pipe, so a builder following the criterion runs the observation id 16 asks for.

### Files touched (estimate)

- `tools/workflows/lenses.toml`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (its render)
- `tools/workflows/review_pin.py`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`
- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md` (its render)
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `help/policy.md`
- `help/loop.md` — the Plan Review paragraph (id 43)

### Alternatives rejected

- **One literal per stage typed in the harness.** The catalogue is the source and the harness its
  render (TOOL-dFairHearing-13 S3); a typed literal is the defect that unit closes.
- **A map from stage to literal in the harness.** The hook denies a map or a registry of lens sets
  (review-system:161-162); the receiver's ternary is the admitted shape.
- **A record-kind mapping per stage.** It works for Plan, whose record is a file with a
  `**Serves:**` line, and not for Deploy, whose landing record lives under `refs/gov/landing/*`
  (DEPL-dShippedRelease-1 §4), so the stage must come from the breakpoint.

## 5. Production-readiness checklist

- security — no new write path. The briefs are tracked catalogue rows rendered by the escaping
  TOOL-dFairHearing-13 states; `--stage` is checked against the marker set before it is printed.
- perf / scale — no new agent: each stage review runs five finders, as every literal does. One more
  `handoff.py` start per `--trigger` call.
- error / empty / loading states — an unknown stage exits 2 in `review_pin.py` and raises a
  `RolesError` in `handoff.py`, each naming the closed set; a missing harness beside `review_pin.py`
  exits 2 naming it, as `read_spec_subject_path` does.
- observability — the harness logs each stage's effort line (`tier2-review.template.js:356-360`) and
  its preset (TOOL-dFairHearing-2 S5), so a stage run names both.
- risks — a stage lens with no calibration finds noise; it ships behind `review.<stage>`'s opt-in
  default, and the ledger prices it. A seven-arm ternary the hook denies would stop every review;
  AC3 observes it before landing.
- testing — AC1 to AC11 as probes and fixtures; the arms in §7.
- migration — none; an existing install re-renders the harness through the kit's regenerate row.
- user docs — `help/policy.md`'s key table; the kit READMEs and the verbs guide.

## 6. Acceptance criteria

- **AC1** — When `python render_lenses.py lenses.toml < tools/workflows/tier2-review.template.js`
  runs, the output holds four literals marked `gov:lens-slots plan`, `test`, `deploy` and `maintain`,
  each listing the `key:` lines of §4 "The rows" for its stage in slot order.
  Red when: a stage literal is missing a row, holds a key of another stage, or is not rendered.
  figure: the twenty keys are PINNED by §4's table.
- **AC2** — When `bash tools/workflows/check-verifier-fanout.sh tools/workflows/tier2-review.js` runs,
  its `slots` line names each of the four stage literals holding 5 and it exits 0.
  Red when: a stage's drawn row lacks the stage in `default_in`, so its literal renders four slots.
- **AC3** — (amended, id 16; r2 id 15) When `node -e` builds `{"tool_name": "Workflow", "tool_input": {"script": <text>}}`
  from the re-rendered `tools/workflows/tier2-review.js` and pipes it to
  `node tools/hooks/agent-cap.js --only=scripts`, the hook exits 0; a bare invocation with no stdin reads no harness and is not this
  observation.
  Red when: the receiver's ternary over seven literals is denied, so no review can spawn.
- **AC4** — When `python review_pin.py --subject <a design record> --stage deploy`
  runs, it prints `{"preset": "deploy"}`; with `--stage build` it prints the subject mapping's line,
  as without the flag; with `--stage nightly` it exits 2 naming `nightly` and the marked literals.
  Red when: the stage is ignored, or an unmarked stage prints a preset.
- **AC5** — When `review_pin.py --subject <a planted plan record>` runs with no `--stage`, it prints
  `{"preset": "plan"}`.
  Red when: `PLAN_RECORD_PRESET` still reads `unit-spec`.
  fixture: a plan record whose first `**Serves:**` word is `plan`, as TOOL-dRankedPlan-6 S3 plants.
- **AC6** — When `python tools/roles/handoff.py stage-efforts spec-review --review-stage test` runs in
  a fixture repository whose policy file sets `review.test.effort = "low"` and
  `review.design.effort = "high"`, it prints `low` for `specFinder`, `skeptic` and `synthesis`; with
  the test key unset it prints the house levels, never `high`.
  Red when: the test review reads the design key, or ignores its own.
- **AC7** — When `handoff.py stage-efforts closing-review` runs in that fixture with
  `review.build.effort = "max"`, it prints `max` for `diffFinder`, `skeptic` and `synthesis`.
  Red when: the Build review's key is unread.
- **AC8** — When `handoff.py stage-efforts spec-review --review-stage nightly`, `handoff.py
  stage-efforts closing-review --review-stage plan`, and a fixture setting `review.plan.effort =
  "huge"` each run, each exits 1 and its stderr names, in turn, `REVIEW_STAGES`, both the stage and
  `closing-review`, and `review.plan.effort` with the levels.
  Red when: any of the three prints levels.
- **AC9** — When `bash tools/unattended/unattended.sh --trigger <fixture slug> --subject <a planted
  landing subject> --cause opt-in --stage deploy` runs in a fixture repository whose policy file sets
  `review.deploy.effort = "medium"`, its JSON line carries `"preset": "deploy"` and an `efforts`
  object reading `medium` for the three review keys.
  Red when: `--stage` is not passed through, or `efforts` is absent.
  fixture: the `--trigger` fixture TOOL-dDeclaredLoop-20 lands in the unattended kit's suite, whose arm
  §7's `New arm:` line declares.
- **AC10** — When `python tools/policy/policy.py lists --check` runs, it exits 0, and
  `grep -c 'review.<stage>.effort' tools/policy/unsummarised-keys.txt` prints 0.
  Red when: the row has no `summary` or `usage`, or the name is still listed.
- **AC11** — (amended, id 43) When `grep -c 'review.<stage>.effort' help/policy.md`,
  `grep -c 'MAINTAIN_LENSES\|gov:lens-slots maintain' tools/workflows/README.md`,
  `grep -c '\-\-review-stage' tools/roles/README.md` and
  `grep -c '\-\-stage' memory/guides/UNATTENDED-VERBS.md` run, each counts at least one.
  Red when: a page still describes stage reviews without their lenses or their effort.

## 7. Gates

`verifier fan-out` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `kit placeholders (a declared token its adopter substitutes)` · `roles catalogue` · `roles adopter self-test` · `policy check` · `policy fixtures` · `unattended kit gate` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's legs are not on the line: `tools/loop/` holds no leg at base, and this unit writes no
file there.

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC4 AC5 · the render over the shipped catalogue, `review_pin.py` with each stage and an unknown one, and a planted plan record, each red against the parents' tree with no stage literal · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/roles/adopt-roles.test.sh · covers AC6 AC7 AC8 · fixture policy files setting a stage's key beside the design key, the build key, an unknown stage, a kind mismatch and an unknown level, red against step 1a reading the design key alone · none
New arm: tools/unattended/unattended.test.sh · covers AC9 · a `--trigger` call with `--stage deploy` in a fixture setting the deploy key, red against the verb as TOOL-dDeclaredLoop-20 lands it, which takes no stage · none

## 8. Open questions

- **F1 — Which rows fill the four stage literals?** (a) TOOL-dFairHearing-2's five design-audit rows
  for every stage, no new brief. (b) New rows for each concern the walkthrough names per stage, the
  remaining slots drawn from the record-aimed design-audit rows. (c) Twenty new rows. (a) gives four
  identical literals and none of the concerns the walkthrough lists; (c) writes briefs for slots no
  record names a concern for. (b) carries every named concern and draws the rest from the catalogue,
  as the clause says. Recommendation (b). RESOLVED (agent, 2026-11-02, delegated): (b), rung 3, the
  most feature-rich survivor. widens: none · relaxes: none
- **F2 — Which review kind does each stage literal run under?** (a) The spec-audit kind for all four,
  each subject a record the stage writes. (b) A diff-kind preset for Test and Deploy, which needs
  `preset` beside the diff kind that TOOL-dFairHearing-2 S1 refuses and a kind per marker that
  TOOL-dFairHearing-13 rule 5 does not admit. (b) re-specs two parent primitives, which the brief's
  parent rule forbids; v2:706 has the landing review run "dFairHearing's preset", a spec-audit preset,
  until this build lands. Recommendation (a). RESOLVED (agent, 2026-11-02, delegated): (a), rung 1,
  v2:706. widens: none · relaxes: none
- **F3 — How does a stage review learn its literal?** (a) `--stage` from the breakpoint, through
  `--trigger` to `review_pin.py`, with `PLAN_RECORD_PRESET` set for a plan subject. (b) A record-kind
  mapping per stage, TOOL-dRankedPlan-6's shape. (c) A per-stage table typed in the harness. (b) cannot
  read a landing record held in a ref; (c) is a second answer to the stage the breakpoint already
  knows. Recommendation (a). RESOLVED (agent, 2026-11-02, delegated): (a), rung 3. widens: none ·
  relaxes: none
- **F4 — Where does the Maintain review sit?** PRIMITIVE GAP: `derive_breakpoints` reads five stages
  and no row of it reads `review.maintain`, which v2:1656 lists. (a) Maintain's literal runs where
  `review.breakpoints` places a review at an `item.maintain.*` boundary, and the build files an ask on
  dDeclaredLoop. (b) This unit adds a sixth stage row to `derive_breakpoints`, choosing a position and
  a breakpoint name outside I23's closed list. (b) changes dDeclaredLoop's `--plan` lines and name set,
  a public surface no clause of this build names, so it fails veto 2 outside the grant; (a) runs the
  Maintain lenses through dDeclaredLoop's breakpoints as the clause says. Recommendation (a).
  RESOLVED (agent, 2026-11-02, delegated): (a), rung 3. The main loop files the ask in
  `memory/builds/dDeclaredLoop/BACKLOG.md`: "DERIVE_BREAKPOINTS READS NO REVIEW.MAINTAIN · v2:1656
  lists `review.maintain` under every preset and TOOL-dDeclaredLoop-19 S1 reads `review.<stage>` for
  plan, design, build, test and deploy only, so `review.maintain: owed` places nothing · accept
  `derive_breakpoints` reads `review.maintain` and places a Maintain review breakpoint at a position
  the Maintain step declares, each value seen on its planted case". widens: none · relaxes: none
- **F5 — Does the Build review's effort belong here?** (a) Yes: step 1a reads `review.build.effort`
  for `closing-review`. (b) No: the Build review keeps its house levels. TOOL-dIndexedDesign-3 §3 names
  "Effort for the Plan, Build, Test, Deploy and Maintain reviews" as this build's, and the clause says
  "each stage review's lenses and effort"; (b) leaves one stage review without its key. Recommendation
  (a). RESOLVED (agent, 2026-11-02, delegated): (a), rung 1, the clause. widens: none · relaxes: none
- **F6 — Does the build's grant lift veto 2 for these files?** `tools/workflows/`, `tools/roles/`,
  `tools/unattended/` and `tools/policy/` are governance carriers. `cl-dClosedLoop-0458` names lenses
  for four stages drawn from the catalogue, run at `review.<stage>.effort` through the breakpoints;
  the literals, the rows, the stage flag, the effort step and the key's catalogue fields are that
  change. RESOLVED (agent, 2026-11-02, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants:
  PLAY-dClosedLoop-3 the stage literals and rows in the review kit, the stage flag through the
  trigger and the pin, and the stage effort in the roles kit · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft. The header carries `OPEN`, not the brief's `DRAFT`, which check
  12's header grammar (`tools/memory-tree/check-memory-hygiene.sh:2145`) does not admit.
- rev-2 · 2026-11-02 · §3 §4 §7 S3 AC3 AC11 · amended at the disposal of the round-1 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4 "Amendments (round-1 spec
  audit)": ids 16 (`TOOL-dCalibratedLens-24`), 4 (`TOOL-dCalibratedLens-23`) and 43
  (`TOOL-dCalibratedLens-30`); §3 gains the hands-off to `TOOL-dCalibratedLens-24`.
- rev-3 · 2026-11-02 · §4 AC3 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`, §4 "Amendments (round-2 spec audit)": r2 id
  15 (`TOOL-dCalibratedLens-41`), AC3's text carrying the payload.

## 10. Reuse audit

The seams extended are three. The effort is `resolve_stage_efforts`
(`tools/roles/roles_lib.py:596-601`), which `python tools/codebase-map/reuse_lookup.py "choose a
review preset lens set for a stage"` ranked among its candidates, its step 1a TOOL-dIndexedDesign-3's
and widened here from one stage to six. The rows are TOOL-dFairHearing-13's catalogue, rendered by its
`render_lenses.py`, with three of TOOL-dFairHearing-2's rows drawn rather than copied. The preset is
TOOL-dFairHearing-3's `review_pin.py`, whose `PLAN_RECORD_PRESET` TOOL-dRankedPlan-6 S1 left for this
unit to set. `python tools/codebase-map/reuse_lookup.py "resolve the reasoning effort level for a
review stage from policy"` returned name-stem neighbours only (`resolve`, `resolve_caps`,
`load_policy`); none resolves a stage's level, so `resolve_stage_efforts` stands. Hits that disagreed
with source: TOOL-dIndexedDesign-3 S4 cites the row at `catalogue.toml:1212-1215`, which sits at
`:1241-1245` at base; the dIndexedDesign scout cites the harness's `efforts` at `:254-271`, now
`:260-277`; TOOL-dFairHearing-13 §4 cites the literals at `:774-836`, now `:781-849`.

Recall terms used: `python tools/memory-recall/query.py "which lenses and effort does each stage
review run at" --terms "lens catalogue preset review.<stage>.effort resolve_stage_efforts step 1a
breakpoint stage-efforts design-audit spec-audit diff-review"`
