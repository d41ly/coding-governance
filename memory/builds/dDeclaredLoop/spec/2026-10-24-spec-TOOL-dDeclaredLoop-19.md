# TOOL-dDeclaredLoop-19 — breakpoints at any item boundary: reviews and owner gates one mechanism under `review.breakpoints`, `review.<stage>` and `autonomy`

**Status:** CLOSED · rev-3 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 33 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0104@2c27f8f3 whole

**Carries:** node:policy-key.review.breakpoints

**Carries:** node:policy-key.review.<stage>

**Carries:** node:policy-key.autonomy

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-16-build-TOOL-dDeclaredLoop-19-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-19-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-19-deviation-192.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-19-deviation-192.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-19-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-19-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-19-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-19-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-19-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-19-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-33 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

A breakpoint is one thing wherever it sits: a position at an item boundary, a disposer, which is a
reviewer or the owner, and a cause (the flow-steps record,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`). `review.<stage>` and
`autonomy` are its default declarations, and `review.breakpoints` places more at any item boundary. A
review breakpoint fires dFairHearing's harness through `--trigger`; an owner gate holds the run's close
until the owner's disposition record names its item, which `run.on-owner-question` will resolve only once
dBoundRoles lands it and never for a ratification. Under `decisions.major: author-owner-ratifies` the
owner item `item.build.ratify`, which the loop definition declares with the owner as its actor, holds a
build whose specs carry a fork the agent resolved under delegation. Today the policy kit catalogues
`autonomy`, `review.<stage>` and `review.breakpoints` and no code reads them; a design review is owed by
the README's `spec-audit:` key or the project's `SPEC_AUDIT_DEFAULT` alone
(`tools/unattended/unattended.sh#check_authorization`), and an owner decision is a parked `decision` row
(`tools/unattended/unattended.sh#verb_park`) handed over under `owner-decision` at no declared boundary
(`gap-flow-11`, AF-1, DA-H1, FK-9-1).

## 2. Scope (IN)

- **S1** — The list. `tools/loop/breakpoints.py`, new, holds `derive_breakpoints(values, steps, tags,
  facts)`, pure, the one rule that lists a build's breakpoints as §4 "The list" states, and
  `read_breakpoints(build, root, spec_audit, delegated)`, which reads its inputs: `autonomy`,
  `decisions.major` and the five `review.<stage>` keys at the landed revision through the policy kit's
  `resolve`, found by `tools/loop/loop_parents.py#read_policy_kit`; `review.breakpoints` through
  `tools/loop/composition.py#read_tag_policy` at the build's pin; the steps through
  `tools/loop/loop_lib.py#read_steps`; the composed item tags at that pin through
  `tools/loop/loop_items.py#read_composed_items`; each unit's tier through `read_build_headers` (S10); and
  each owner gate's release through `tools/loop/adapt.py#read_disposition_release`. An unset
  `review.<stage>` reads the catalogue's derived default, `owed` for `build` and `opt-in` for the other
  four, where `tools/policy/policy.py#read_default_value` raises `DerivedDefault`. The verb `list --build
  <slug> [--spec-audit] [--delegated-fork]` prints one §4 line per breakpoint, exit 0, and the verb `stage`
  prints one stage's reading through `read_stage_review(build, root, stage, rev)`. Observed by AC1, AC6,
  AC7.
- **S2** — The review declarations. Under `review.<stage>`, `off` places nothing, `opt-in` places the
  stage's review only where the build opts in, `owed` always, and `owed-above-tier` where a unit of the
  build reads Tier-2. The five positions are §4's table. Only Design has a per-build opt-in, the
  `--spec-audit` flag the driver passes where the run-state file's `spec-audit` fact holds a date; at
  the other four `opt-in` places nothing until `review.breakpoints` names the boundary. Observed by AC1,
  AC5, AC6.
- **S3** — The owner declarations. Under `autonomy`, `plan-only` places an owner gate at `item.plan.exit`;
  `three-gates` adds one at `item.design.exit` and one before `item.deploy.mandate`; `every-stage` adds one
  at each `[[step]]` row's `exit` item, read from the definition and never typed. Observed by AC1.
- **S4** — The placed declarations. Each member of `review.breakpoints`, redirected across a rename by
  `read_tag_policy`, places a `breakpoint` before that item with cause `placement`; a member the composed
  items at the pin do not declare is refused, naming `review.breakpoints` and the tag. Observed by AC2.
- **S5** — The owner item (§8 F4). Under `decisions.major = "author-owner-ratifies"`, given
  `--delegated-fork`, the list places an `owner item` at `item.build.ratify` with cause `ratification`.
  The driver passes the flag where `check_delegated_fork` finds a tracked spec of the build whose §8
  carries `RESOLVED (agent, <date>, delegated)`, every such fork read as major because no fork record
  carries a class. Under `author-rubric` or `owner-only`, or with no such fork, it places none.
  Observed by AC3, AC4.
- **S6** — The hold at `--close` (§8 F5, F6, F7). `check_owner_gates <slug>`, which `verb_close` calls
  after its HELD refusal, runs the list with `--delegated-fork` as S5 derives it and refuses through one
  `fail 82` site while an owner line reads `held`, naming each held item and the act: `--park <slug>
  --item <tag> --reason <question>`, then `--handoff <slug> --code owner-decision`, and the owner's
  disposition record whose `Item` is that tag releases it at the next `--close`. The plan gate's release
  is the authorization `check_authorization` verifies at the pinned BASE, so it is never held. A list that
  refuses is relayed through the same site; where the loop kit's `breakpoints.py` does not resolve,
  nothing is read and the close goes on (§8 F10). Observed by AC3.
- **S7** — `run.on-owner-question` is not read. Each owner line names its release as `authorization`,
  `held` or `released <record> <word>`, and the owner item carries cause `ratification`, the mark a later
  reader of that key refuses on. Observed by AC7.
- **S8** — The spec-audit opt-in reads `review.design` first (§8 F2, F8, F9). `read_design_review <slug>
  <rev>`, called by `check_authorization` after the project default's read and before
  `AUTH_SPEC_AUDIT_DERIVED` is set, runs `breakpoints.py stage --stage design --build <slug> --rev <rev>`
  at the default-branch side of BASE, `_cb`, and applies §4 "The opt-in": `owed` pins the BASE commit's
  date with the source `policy`; `not-owed` leaves the audit unowed with the source `policy`, any README
  key or project default unread; `opt-in` keeps today's derivation. A refused read is one `fail 55` site,
  which leaves `AUTH_SPEC_AUDIT_DERIVED` blank; an unresolved module or an empty `_cb` reads `opt-in`.
  `AUTH_DESIGN_REVIEW` holds the value read. `print_spec_audit_line` and the `specs-audited` term's
  not-owed line name the `policy` source and the value. Observed by AC5, AC6.
- **S9** — `--plan <slug>` prints `breakpoints.py list`'s lines after its `next:` and `frontier:` lines,
  through `print_breakpoint_lines`, called by the single-slug branch of the verb's dispatch, never under
  `--paths`, `--framed` or the position engine's hand-over call, and printing nothing where the module
  does not resolve. Observed by AC8.
- **S10** — The seams extended (M5). `run_loop_verb <script> <verb> <flag=value>...` is extracted from
  `run_budget_verb`, which keeps its name, its printed output, `_bd_why` and `_bd_rc`, so the driver's
  three new reads and the budget's are one runner. `read_build_headers(build, root)` is extracted from
  `tools/loop/loop_transition.py#read_build_specs`, answering each unit's tier beside its status, and
  `read_build_specs` maps it to the same pairs in the same order. `plan_state` takes a third argument,
  `delegated`, a mode of its one awk program printing `DELEGATED` or `NONE`, which `check_delegated_fork`
  reads. Observed by AC4, AC6, AC11.
- **S11** — The carriers. `tools/unattended/VERBS.template.md` and its render state the breakpoint lines of
  `--plan`, the `--close` hold and the `policy` source; `tools/unattended/PROTOCOL.template.md` and its
  render state the `specs-audited` row's and the `SPEC_AUDIT_DEFAULT` row's policy reading; BUILD-METHOD
  M4's "When" (`tools/memory-tree/BUILD-METHOD.template.md` and its render) is reworded to §4's exact text;
  `help/spec-audit.md`'s "When a chain runs" names `review.design`; `help/loop.md` gains a section on
  breakpoints anchoring the three usage rows `tools/govkit/usage.toml` gains, `breakpoints.py`, `#list` and
  `#stage`; `tools/loop/kit.toml` gains the comment naming the module and its leg. Observed by AC9.
- **S12** — The leg `loop breakpoint fixtures` in `tools/gate-legs.json`, running `breakpoints.py
  --selftest`, with chunk `selftests`, subject `kit`, `stage = ["step.test"]` and `enforces =
  ["principle.p7"]`, the principle whose first clause, `cl-dClosedLoop-0104`, this unit carries; its
  `[[exempt_leg]]` row in `tools/govkit/registry.toml`, its row in `tools/govkit/subject-pins.tsv`, its
  priced row in `tools/run-gates/selftest-budgets.txt` and its name in `memory/map/features/loop.md`.
  `tools/playbook/core-pending.txt` deletes its `principle.p7` row, armed by dDeclaredLoop, because the
  meta-check reds a pending row whose item a leg now enforces. Observed by AC10.
  **Readers:** by name: `tools/playbook/core-pending.txt`, the pending list that spells `principle.p7`, and `tools/playbook/core.py`, whose `meta-check` verb reads that list and reds a row whose item a leg now enforces
  by value: NO VALUE READERS — a pending row's value is its arming build, which the meta-check prints only in its pending count.
- **S13** — The suite arms the `New arm:` lines in §7 declare. Observed by AC1, AC2, AC3, AC4, AC5, AC6,
  AC7 and AC8 through those lines, RED first at the close.

## 3. Non-goals (OUT)

- `run.on-owner-question` and its values: dBoundRoles' key. The hand-over: once that build lands it, it may
  resolve an owner gate that is not a ratification, and the `ratification` cause is what it reads to
  refuse the rest.
- `build.ratify`'s own actor and the fork's class: dScopedBuild's item and a later build's fork record. The
  hand-over: the owner item sits at the item that build arms, and from then a fork's class decides which
  forks reach it. `decisions.major = "owner-only"`'s refusal of an agent's major fork is dLinkedLibrary's.
- The review program's items and keys: `TOOL-dDeclaredLoop-20`'s, which a review breakpoint fires and
  never re-specs.
- The recommendation: `TOOL-dDeclaredLoop-22`'s record. A binding `review` score fires a breakpoint
  through the same `--trigger` line.
- The `--phase` hold past a gated step exit: `TOOL-dDeclaredLoop-52`'s, on its phase map (§8 F5).
- A `Hold` field on the disposition record and `check_owner_disposition` widened to every owner gate:
  `TOOL-dDeclaredLoop-56` S13. `check_owner_disposition` stays the exhaustion park's.
- The opt-in pack `tools/workflows/spec-audit-optin.js` reading `review.design` in an attended session:
  dFairHearing's pack (§8 F9).
- `attendance` and its confirm gates, `run.owner-deadline` and `run.on-owner-silence`: later builds' keys.
- Firing a review breakpoint inside a running step: the main loop reads the `--plan` lines and fires
  `--trigger`; this unit lists and holds.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-16` — `record-kind.disposition`: the owner's disposition record,
  whose `Item` names the gate it releases; without it no owner gate has a release
- **consumes-from** `TOOL-dDeclaredLoop-26` — `read_tag_policy`: the read of `review.breakpoints` that
  re-points a renamed boundary, so a placed breakpoint follows its item across a rename
- **consumes-from** `TOOL-dDeclaredLoop-20` — `review.dispose`: the breakpoint program a review breakpoint
  runs, fired by its `--trigger` verb with the cause the line prints
- **consumes-from** `TOOL-dDeclaredLoop-22` — `record-kind.recommendation`: the `build.recommend` score
  whose `ratify` route reaches the owner item this unit places
- **consumes-from** `TOOL-dDeclaredLoop-31` — `record-kind.disposition`: the `owner-decision` hand-off the
  exhaustion park established, which an owner gate's remedy names, and `read_build_specs`, from which
  `read_build_headers` is extracted; `check_owner_disposition` stays that park's (§8 F7)
- **hands-off** `TOOL-dDeclaredLoop-52` — the phase-to-state-and-step map, which that unit ships as rows
  with one reader, and the `--phase` hold past a gated step exit built on it (§8 F5; the round-1 spec
  audit's id 4)
- **hands-off** `TOOL-dDeclaredLoop-53` — the owner gate's in-flight rule, which that unit scopes to builds
  opened after the placement (the round-1 spec audit's id 54)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids
  10 and 37, each a scope item of that unit

## 4. Design

### The list

```
derive_breakpoints(values, steps, tags, facts) -> [{name, relation, position, disposer, cause, release}]
  for each step, in [[step]] order: v = review.<its last segment>
    off               -> nothing
    opt-in            -> the stage's review, cause opt-in, only where facts.spec_audit and the stage is design
    owed              -> the stage's review, cause owed
    owed-above-tier   -> the stage's review, cause owed, where some unit's tier reads 2
  autonomy  plan-only   -> owner gate at item.plan.exit, release authorization
            three-gates -> + at item.design.exit, + before item.deploy.mandate
            every-stage -> + at each [[step]] row's exit item
  review.breakpoints: each member -> breakpoint before it, reviewer, cause placement;
                      a member outside tags -> ValueError naming review.breakpoints and the member
  decisions.major == author-owner-ratifies and facts.delegated
                    -> owner item at item.build.ratify, owner, cause ratification
  any value outside its catalogued set -> ValueError naming the key and the value
  sorted by the position item's place among the composed rows; on one item, before, then at, then after
```

| Stage | Review name | Position |
|---|---|---|
| plan | `breakpoint` | before `item.plan.exit` |
| design | `spec audit` | after `item.design.reason` |
| build | `closing review` | after `item.build.recommend` |
| test | `gate review` | before `item.test.exit` |
| deploy | `landing review` | before `item.deploy.notify` |

The table is `STAGE_REVIEWS`, the one typed fact: which review each stage owns and where, from the
flow-steps record. Each position tag is a declared `[[item]]` row of `tools/loop/loop.toml` at
`250b236fe`, and a position the composed tags lack is refused as S4's member is. A duplicate position
from two declarations, an owner gate under both `three-gates` and `every-stage` say, is listed once.
`read_breakpoints` answers each owner line's release: `authorization` for `item.plan.exit`, else
`released <stem> <word>` where `read_disposition_release(root, build, tag, ())` answers, else `held`.

### The lines

```
breakpoint: <name> · <before|at|after> <item tag> · <reviewer|owner> · <cause>[ · <release>]
breakpoints: stage <stage> · <value> · <owed|opt-in|not-owed>
breakpoints: refused · <why>                                    exit 2
breakpoints: unarmed · <why>                                    exit 2
```

A review line carries four fields and an owner line five. The names are I23's: `breakpoint`, `spec audit`,
`closing review`, `gate review` and `landing review` for a reviewer, `owner gate` for an `autonomy` cause
and `owner item` for `ratification`. The first four fields are the shape `TOOL-dCalibratedLens-1`'s main
loop reads to fire `--trigger --cause <cause>`. `stage --stage <s> --build <slug> [--rev <rev>]` reads one
`review.<stage>` at `<rev>`, else the landed revision: `owed` under `owed`, or under `owed-above-tier`
where a unit reads Tier-2; `not-owed` under `off`, or under `owed-above-tier` with none; `opt-in` under
`opt-in`. `unarmed` is a kit that does not resolve; `refused` a policy refusal, a slug outside
`[A-Za-z0-9_-]+`, a value outside its key's set, or S4's member. Every key is spelled as a string literal
at its read, since the policy kit's reader coverage counts a key only so
(`tools/policy/check_policy.py#READER_SHAPES`).

### The owner item

The FK-9-1 ruling held `build.recommend`'s route for the owner until dScopedBuild lands `build.ratify`.
At `250b236fe` the definition declares that item: `item.build.ratify`, actor `owner:build.ratify`,
outcomes `ratified` and `rejected`, its allowance "the owner's disposition record for each major fork",
and `item.build.recommend` routes `ratify` to it. So the owner item sits at that declared item rather than
standing in beside it (§8 F4), and the disposition record whose `Item` is `item.build.ratify` releases it.
A fork "its author classed major" has no class in this tree, so every §8 fork resolved `RESOLVED (agent,
<date>, delegated)` reads as major: holding one fork too many asks the owner once more, and holding one
too few lands a decision the owner ruled theirs. The forks are read by `plan_state`'s own grammar
functions, `check_mark`'s shape narrowed to `agent` and `delegated`, through the `delegated` mode of the
same awk program, never a second §8 parser: over each F-item span, or the whole section before
`FORK_ITEM_CUTOFF`, code and quoted spans removed as `check_span_mark` removes them.

### The hold

```
check_owner_gates <slug>                                   in verb_close, after the HELD refusal
  load_fork_cutoff; check_delegated_fork <slug>
  run_loop_verb breakpoints.py list --build=<slug> [--delegated-fork]
  module unresolved                    -> return 0, nothing read
  exit not 0                           -> _og_why = its first line
  owner lines whose release is held    -> _og_why = their tags and the act
  _og_why set                          -> fail 82 "...: $_og_why"
```

The act the refusal names is today's door: `--park <slug> --item <tag> --reason <question>` writes the
`decision` row (`tools/unattended/unattended.sh#PARK_KINDS_OWED` holds `decision`), `--handoff <slug>
--code owner-decision` holds the run (`HOLD_CODES_CORE` holds `owner-decision`), and the owner writes the
record through `build_records.py new disposition` with `Item` the gate's tag. A record's `Item` must be an
`item.` tag (`tools/memory-tree/build_records.py#check_disposition_fields`), so it names the gate's
position and never the `decision` row (§8 F7). The run resumes as any `owner-decision` hold does, and its
next `--close` reads the record. Under the defaults, `plan-only` and `author-rubric`, the one owner line
is the plan gate, released by `authorization`, so no close is held that is not held today (§8 F6).

### The opt-in

| `stage design` reads | `AUTH_SPEC_AUDIT` | `AUTH_SPEC_AUDIT_FROM` |
|---|---|---|
| `opt-in`, `unarmed`, an unresolved module or an empty `_cb` | today's README key, else `SPEC_AUDIT_DEFAULT` | `readme` or `project`, as today |
| `owed` | the BASE commit's date, `GIT show -s --format=%cs "$base"` | `policy` |
| `not-owed` | empty; a README key or project default is unread | `policy` |
| `refused` | not derived: `fail 55`, `AUTH_SPEC_AUDIT_DERIVED` blank | unchanged |

The value is read at `_cb`, the default-branch side of BASE that `SPEC_AUDIT_DEFAULT` is read at, so a run
can no more write `owed` than a README opt-in; the policy file is the owner's guarded file besides. The
README key's own refusals, fail 52 and fail 89, run as today under every reading, since a key present is
an attempt whether or not it decides. The owed date has the shape the run-state's `spec-audit` fact
carries, so `--preflight` pins it, the `specs-audited` term's presence comparison (fail 53) reads it
unchanged, and the opt-in pack, which in a live run reads only that pinned fact, admits the harness's
audit. `print_spec_audit_line` prints `opted in by policy review.design: <value>` with the date, or
`not owed by policy review.design: <value>` where the source is `policy` and nothing is pinned.

BUILD-METHOD M4's "When" paragraph reads, in the template and its render alike:

```
**When**, and `specs-reviewed` is owed only then: `review.design` is `owed`, `owed-above-tier` over a Tier-2 spec, or
`opt-in` (its default) and a `slug` README the owner landed carries `spec-audit: <date>`, or `.unattended.conf` on the
default branch a dated `SPEC_AUDIT_DEFAULT` and the README no key (TOOL-aBlindedTrial-7). Else none is owed.
```

It replaces the paragraph's opening through "instead of running one.", one byte shorter, which the
`build-method size` row's no-raise rule requires (§5 "Budgets and records").

### The plan lines

`print_breakpoint_lines <slug>` runs the list with `--spec-audit` where the run-state file's
`spec-audit` fact holds a date and `--delegated-fork` as S5 derives it, and prints the module's output
verbatim, its refusal line included; an unresolved module prints nothing. The dispatch's single-slug
branch calls it after `verb_plan` answers 0, with `PLAN_PATHS` empty and `GOV_POSITION_STATES` unset, so
the lines follow the `frontier:` line that `tools/loop/position.py`'s `plan-frontier` plant reads directly
after `next:`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_breakpoints`, `read_breakpoints`, `read_stage_review`, `read_build_headers` | Python functions | `py.function`, verb-first |
| `check_owner_gates`, `check_delegated_fork`, `read_design_review`, `print_breakpoint_lines`, `run_loop_verb` | bash functions | `sh.function`, verb-first |
| `list`, `stage` | `breakpoints.py` verbs | none |
| `--spec-audit`, `--delegated-fork`, `--stage`, `--rev` | `breakpoints.py` flags | none |
| `STAGE_REVIEWS`, `PLANTS` | Python constants | none |
| `AUTH_DESIGN_REVIEW` | driver global | none |
| `policy` | `AUTH_SPEC_AUDIT_FROM` value | none |
| `delegated`, `DELEGATED`, `NONE` | `plan_state` mode and answers | none |
| `breakpoint:`, `breakpoints:` | output line heads | none |
| `loop breakpoint fixtures` | gate leg | none |

Each function name passed `python tools/lexicon/lexicon.py --suggest <name> --as <cell>` on the worktree at
`179486e8f`, whose `.lexicon.conf` verb declarations equal the branch's.

### Migration

None. Every default reproduces today: `review.design` reads `opt-in`, so the README key and the project
default decide; `autonomy` reads `plan-only`, whose one gate the authorization releases; `decisions.major`
reads `author-rubric`, which places no owner item; `review.breakpoints` is empty.

### Rollout

One landing. A project whose policy file sets none of the keys sees two `breakpoint:` lines at `--plan`,
the plan gate and the owed closing review, and every close and preflight as today.

### Files touched (estimate)

- `tools/loop/breakpoints.py`
- `tools/loop/loop_transition.py`
- `tools/loop/kit.toml`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`
- `help/spec-audit.md`
- `help/loop.md`
- `tools/govkit/usage.toml`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/selftest-budgets.txt`
- `tools/playbook/core-pending.txt`
- `memory/map/features/loop.md`
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`, `memory/map/generated/CARDS.md`,
  `memory/map/generated/inventories.json`
- `.memory-tree.conf`
- `memory/project/positional-refs.txt`
- `memory/guides/SESSION-KICKOFF.md`

Each `memory/guides/*.md` is its template's render; the template is the edit.

### Alternatives rejected

- **Keep reviews and owner gates as two lists.** The clause makes them one mechanism; two lists are the
  `gap-flow-11` defect.
- **Read the major class from a field this tree does not have.** No fork record carries one; inventing it
  here would be a later build's mechanism.
- **Let the README opt-in go for `review.design: owed`.** The README key is the per-build channel `opt-in`
  needs, and the owner's per-build opt-in rulings (TOOL-aBlindedTrial-6, TOOL-aWardedAudit-4) stand.
- **A second runner beside `run_budget_verb`.** The kind's second instance extracts its factory.

## 5. Production-readiness checklist

- security — every key is read from the guarded policy file, `review.design` at the default-branch side of
  BASE, so a run cannot place or lift a gate; the slug is refused outside its grammar before it reaches a
  path; the hold adds no write surface, the remedy being `--park` and `--handoff` with their refusals.
- perf / scale — one python start per `--plan`, per `--close` and per `check_authorization`; the list
  composes the items once at the pin, and the fork scan is one awk pass per tracked spec.
- error / empty / loading states — an undeclared tag or a value outside its set refuses naming the key; an
  unset key reads its default; a missing loop kit reads as today.
- observability — every placed breakpoint is a `breakpoint:` line with its release; a held close names
  each item and the act; the preflight line names the `policy` source.
- risks — the owner item reads every delegated fork as major, the safe direction, ending with a fork
  class. A TOML file cannot set `review.design` beside the `[review.design]` table that
  `review.design.rounds` lives in (§8 F8). In an attended session the opt-in pack still reads the README
  and the conf alone (§8 F9). A run may resume past an owner gate; only its close is held until
  `TOOL-dDeclaredLoop-52`'s `--phase` hold lands.
- testing — the plants run the module and the driver in scratch repositories; the arms in §7 are observed
  RED then GREEN by the main loop.
- migration — none.
- user docs — `help/loop.md` gains the breakpoints section and `help/spec-audit.md` the policy source; the
  verbs and protocol carriers state the lines, the hold and the source.

### The sweep

Read at branch `unattended-declared-loop-d56bf0`, tip `250b236fe`, through `git show` and an export of
that commit; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `run_budget_verb`'s body, moved into `run_loop_verb` | `run_budget_draw`, `read_exhausted_ending`, `verb_review`'s and `run_fix_pass`'s `target` calls; `budget.py`'s `driver-draws`, `spent-spec-round` and `driver-exhausted` plants | name, printed output, `_bd_why` and `_bd_rc` byte-identical; the unresolved and empty-output texts spell the script and verb, which for `budget.py` are today's bytes |
| `read_build_specs`, mapped from `read_build_headers` | `tools/loop/budget.py#read_ending`'s `dict(...)`, `read_build_unit_ids`'s pairs | same pairs, same order |
| `plan_state`'s third argument | `verb_plan`, `print_spec_audit_line`, the `build-complete` term, check 30 through `--plan --framed` | an absent third argument runs today's program |
| `check_authorization` | `verb_preflight`, `run_takeover`, `dod_met`'s `authorization-reachable` term | `opt-in` is today's derivation; the driver suite runs a copied driver with no loop kit beside it, which reads `opt-in` and prints nothing new |
| `print_spec_audit_line`, the `specs-audited` term | the suite's `opted in by README spec-audit:` and not-owed arms | a new branch on `policy`; the other texts unchanged |
| `--plan`'s single-slug branch | `position.py`'s `plan-frontier`, `plan-line` and `built-unarmed` plants; the suite's `--plan` arms; `--paths` callers in the build harness; check 30's `--framed` read; the engine's hand-over call | lines follow `frontier:`; none under `--paths`, `--framed` or the hand-over; none where the module does not resolve |
| `verb_close` | the suite's `--close` arms; `budget.py`'s driver plants | defaults hold nothing; no loop kit, nothing read |
| two new refusal sites | the census and families, §5 "Budgets and records"; the harness arms leg | the decision row landed ahead; the suite arm hits both literals |
| `tools/playbook/core-pending.txt`'s `principle.p7` row | `core.py`'s `meta-check`, the `core meta-check` leg; its `arm_registry` fixture, which plants its own copy | the leg's `enforces` names it as the row goes |
| the new leg | `run-gates canary`, `every held leg is budgeted, every budget row resolves`, `measure-legs selftest`, `codebase-map gate coverage`, `govkit selfcheck`, `kickoff-manifest ratchet` | the registry, subject-pin, budget and map rows of S12; the manifest re-stamp |
| `tools/govkit/usage.toml` | the `docs` leg's anchor join | three anchors on `help/loop.md`, each with `docs_leg.py --fingerprints`' fingerprint |
| the carriers | `kit/dogfood doc parity`, `build-method size`, `unattended protocol size`, `tags (the resolver's checks)` | renders re-copied; sizes below; every backticked tag a declared item |
| shipped bytes | `install-prefix (shipped surface)` | `breakpoints.py` and the templates name siblings by file name or `<prefix>`, never a kit path |
| the policy keys | `policy check`'s reader coverage, graded once dDeclaredLoop lands | each key a string literal at its read |
| other builds | `TOOL-dCalibratedLens-1` parses the lines' first four fields; `TOOL-dBoundRoles-11` reads the `ratification` mark; `TOOL-dFurnishedOrders-16` reads S6's hold | the four fields and their order kept; the cause word kept; the hold is the `--close` refusal |
| subject pins, epoch delegates, upgrade rows | `tools/govkit/subject-pins.tsv`, `check-verdict-epoch.sh`'s `DELEGATES`, `[[upgrade]]` | one new pin row; no delegate touched; no migration |
| suite floors | each `FLOOR_ASSERTIONS`, a lower bound | may rise by the arms added |

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:memory/guides/BUILD-METHOD.md" | tr -d '\r' | wc -c                 # 30718
git show "$B:memory/guides/UNATTENDED-PROTOCOL.md" | tr -d '\r' | wc -c          # 67731
git show "$B:tools/playbook/core-pending.txt" | grep -c 'principle.p7'           # 1
git show "$B:tools/unattended/unattended.sh" | grep -c 'run.on-owner-question'   # 0
```

### Budgets and records

- The driver's census, read through `tools/memory-tree/check-arms.py#branches` and
  `tools/memory-tree/check-arms.py#scan_refusal_sites` over the export, is 338 PINNED at `250b236fe`, at its
  ceiling of 338 PINNED; `TOOL-dDeclaredLoop-22` raises both to 340 PINNED under its landed decision row.
  This unit adds two sites, `check_owner_gates`' `fail 82` and `read_design_review`'s `fail 55`, so the
  ceiling rises 340 -> 342 PINNED with the comment line below, and `memory/project/positional-refs.txt`'s
  row pairing `.memory-tree.conf` with the driver's count is re-pointed in place to 342.
- The families of `tools/unattended/unattended.families.txt` do not move: missing-run-state 1 of 1,
  required-flag 11 of 11 and field-shape 36 of 37, PINNED. Neither message spells `requires --`, `requires
  $`, a newline, a carriage return, a separator or the bypass flag, and neither opens `no run-state file`.
- `tools/unattended/check-unattended.sh` stays at 266 of its 266 PINNED; it is not edited.
- `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED: every new name leads with a declared verb.
- `memory/guides/BUILD-METHOD.md` measures 30718 bytes PINNED against its row of 30720, and the row's
  comment reserves its next movement to the owner ("Spent, it is the owner's again"), so §4's rewording
  lands it at 30717 bytes PINNED and any other wording is a divergence.
- `memory/guides/UNATTENDED-PROTOCOL.md` measures 67731 bytes PINNED against its row of 68130, so this
  unit's text keeps within 399 bytes PINNED; `TOOL-dDeclaredLoop-56` S25 trims after it.
- The shared records: the pass writes neither `memory/DECISIONS.md` nor
  `memory/project/readme-contract.txt`. The run lands the decision row below ahead of the pass, and the
  pass writes the comment line above `REFUSAL_CEILINGS` in `.memory-tree.conf`:

```
- **TOOL-dDeclaredLoop-19** - **the driver's refusal ceiling rises by two, 340 -> 342 (re-based over TOOL-dDeclaredLoop-22, which raised it 338 -> 340 first), for the `--close` owner-gate hold and the relay of the `review.design` read in `check_authorization`, under TOOL-aSparedSpawn-14's rule, as TOOL-dDeclaredLoop-31 raised it**: agent, <date>, under ER:388 (PLAY-dClosedLoop-6), landed ahead of the pass that makes the raise. Detail `builds/dDeclaredLoop/`.
# TOOL-dDeclaredLoop-19 RAISED the driver 340 -> 342, the census, under decision TOOL-dDeclaredLoop-19 (ER:388): the --close owner-gate hold and the review.design read's relay.
```

- The kickoff manifest watches `.memory-tree.conf`, `tools/gate-legs.json` and
  `memory/guides/BUILD-METHOD.md`, so `memory/guides/SESSION-KICKOFF.md`'s `last-audit` is re-stamped with a
  `manifest-audit:` delta line.
- The leg's budget row is priced from a timed run of the plants, PINNED with date and node by that file's
  rule; its manifest ceiling is 300 seconds, PINNED.
- Help anchors: `script:tools/loop/breakpoints.py`, `#list` and `#stage`, each with the fingerprint
  `python tools/govkit/docs_leg.py --fingerprints` prints. No driver verb or flag is added.
- The map: `python tools/codebase-map/gen_map.py --write` regenerates `symbols.json` and its siblings.
- The loop, unattended, memory-tree, govkit and playbook kits' versions are owed at the lander.
- This revision turns the spec's line citations into symbol citations, so the commit landing it runs
  `python tools/playbook/positional.py shrink`, which takes their rows out of the positional list.

### Dependency

Order 33, beside `TOOL-dDeclaredLoop-51`, read on its committed rev-2: it amends eight `[[item]]` rows of
`tools/loop/loop.toml`, which this unit reads by tag and never edits. `TOOL-dDeclaredLoop-22` (order 32,
after `TOOL-dDeclaredLoop-50`) is read on its committed rev-4: the census 338 -> 340 PINNED, and its edits
to `tools/unattended/VERBS.template.md` and `help/loop.md`, which this unit's land after.
`TOOL-dDeclaredLoop-50` (order 32, building) is read on its committed rev-3: its six review `[[item]]` rows
widen the composed tags a placement may name. `TOOL-dDeclaredLoop-52` and `TOOL-dDeclaredLoop-53` (order
34) are read on their committed specs: unit 52's S4 points the `--phase` refusal at its map, which it
builds there (§8 F5), and unit 53 scopes the `--close` hold. Units 13, 16, 20, 21, 26, 28, 30, 31 and 32
are CLOSED, read on landed code; `TOOL-dDeclaredLoop-34` is deferred against ask TOOL-dDeclaredLoop-113 and
shares no file. The suggests, the reuse probe and the recall query ran on the worktree at `179486e8f`,
which holds no loop kit; every other claim was read on the branch.

## 6. Acceptance criteria

Each `python breakpoints.py` command below runs in the loop kit's folder; every other command runs at the
top of the repository unless its criterion names a folder.

- **AC1** — When `python breakpoints.py --fixture --plant values` runs, it prints `held`: with no
  policy file, `list --build tFix` prints `breakpoint: owner gate · at item.plan.exit · owner · autonomy ·
  authorization` and `breakpoint: closing review · after item.build.recommend · reviewer · owed` and nothing
  else; with `autonomy = "three-gates"` it adds owner gates at `item.design.exit` and before
  `item.deploy.mandate`; with `every-stage` it adds one at each of `item.build.exit`, `item.test.exit` and
  `item.deploy.close` besides; and with `test = "owed"` under `[review]` it adds `gate review · before
  item.test.exit`.
  Red when: `review.<stage>` and `autonomy` are listed by two functions, so `every-stage` misses a review.
- **AC2** — When `python breakpoints.py --fixture --plant placed` runs, it prints `held`: under
  `breakpoints = ["item.build.unit-pass"]` in `[review]`, `list` adds `breakpoint: breakpoint · before
  item.build.unit-pass · reviewer · placement`; under `["item.build.nothing"]` it exits 2 printing
  `breakpoints: refused` naming `review.breakpoints` and the tag.
  Red when: an undeclared tag is placed silently.
- **AC3** — When `python breakpoints.py --fixture --plant ratification` runs, it prints `held`:
  under `major = "author-owner-ratifies"` in `[decisions]`, `list --delegated-fork` prints `breakpoint:
  owner item · at item.build.ratify · owner · ratification · held`, and after a committed disposition
  record of `item.build.ratify` reading `ratified`, `released <its stem> ratified`. And when the
  `driver-close` plant runs the driver over a repository holding that policy and a spec whose §8 fork reads
  `RESOLVED (agent, 2026-01-01, delegated)`, `unattended.sh --close tPos` exits 1 naming
  `item.build.ratify`, and once the record is committed the sourced driver's `check_owner_gates tPos`
  answers 0.
  Red when: the planted delegated fork reaches no gate and `--close` proceeds.
  cost: the driver in a scratch repository, about a minute.
- **AC4** — When the `ratification` plant lists the same repository under `major = "author-rubric"`, or
  without `--delegated-fork`, no `owner item` line prints; and the sourced driver's `plan_state <spec> ""
  delegated` prints `DELEGATED` over the planted spec and `NONE` over a spec whose fork reads `RESOLVED
  (owner, 2026-01-01)`.
  Red when: the owner item is placed under the default, or an owner's own ruling reads as delegated.
- **AC5** — When `python breakpoints.py --fixture --plant driver-optin` sources the driver in a
  repository whose README carries no `spec-audit:` key and calls `check_authorization tPos <HEAD>`, under
  `design = "owed"` in `[review]` it leaves `AUTH_SPEC_AUDIT` the HEAD commit's date and
  `AUTH_SPEC_AUDIT_FROM` `policy`; under `off`, with a README `spec-audit: 2026-01-01`, it leaves
  `AUTH_SPEC_AUDIT` empty and the source `policy`; with no policy file and that README key, `2026-01-01`
  and `readme`.
  Red when: `owed` leaves the audit not owed because the README is silent.
  cost: the driver in a scratch repository, about a minute.
- **AC6** — When `python breakpoints.py --fixture --plant stage` runs, it prints `held`: under
  `design = "owed-above-tier"` in `[review]`, `stage --stage design --build tFix` prints `owed` where one
  spec's header reads `Tier-2` and `not-owed` where every one reads `Tier-1`; with no policy file it prints
  `opt-in` for `design` and `owed` for `build`; and `read_build_headers` answers the tier beside the status
  `read_build_specs` answers unchanged.
  Red when: a Tier-1-only build is owed an audit, or the derived default refuses.
- **AC7** — When `grep -c 'run.on-owner-question'` runs over the loop kit's `breakpoints.py` and
  `tools/unattended/unattended.sh`, each prints 0; and every owner line the `values` and `ratification`
  plants print ends in `authorization`, `held` or `released <stem> <word>`, the owner item's cause
  `ratification`.
  Red when: a gate lists `run.on-owner-question` as its resolver before the build that owns it lands.
- **AC8** — When `python breakpoints.py --fixture --plant driver-plan` runs `unattended.sh --plan
  tPos` over a repository under `autonomy = "three-gates"`, the lines after its `frontier:` line equal what
  `list --build tPos` prints, in the same order; `--plan tPos --paths` prints no `breakpoint:` line.
  Red when: `--plan` derives its own list or prints between `next:` and `frontier:`.
  cost: the driver in a scratch repository, about a minute.
- **AC9** — When `grep -c 'owed-above-tier'` runs over `tools/memory-tree/BUILD-METHOD.template.md`,
  `memory/guides/BUILD-METHOD.md`, `tools/unattended/PROTOCOL.template.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md` and `help/spec-audit.md`, and `grep -c 'breakpoint: '` over
  `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, each prints at least 1;
  `tr -d '\r' < memory/guides/BUILD-METHOD.md | wc -c` prints 30717 and the protocol render stays at or
  under 68130; and `python tools/govkit/docs_leg.py --list` names the three `breakpoints.py` rows as
  anchored on `help/loop.md`.
  Red when: a template is edited and its render is not, or a usage row ships with no anchor.
  figure: 30717 and 68130 PINNED, §5 "Budgets and records".
- **AC10** — When `python -m json.tool gate-legs.json` runs in the tools folder, the row named `loop
  breakpoint fixtures` carries `enforces` holding `principle.p7` and `stage` holding `step.test`; `grep -c
  "principle.p7" tools/playbook/core-pending.txt` prints 0; `grep -c "loop breakpoint fixtures"` prints 1
  over each of `tools/run-gates/selftest-budgets.txt`, `tools/govkit/registry.toml`,
  `tools/govkit/subject-pins.tsv` and `memory/map/features/loop.md`; and `python tools/playbook/core.py
  meta-check` exits 0, naming neither that leg nor a stale pending row.
  Red when: the leg carries no `enforces`, or the pending row stays, which the meta-check reds stale.
- **AC11** — When `python tools/loop/budget.py --fixture --plant driver-exhausted` and `--plant ending` run
  after the extractions, each prints `held`.
  Red when: `run_budget_verb` or `read_build_specs` changes a byte its readers compare.
  cost: the driver in a scratch repository, about a minute.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `playbook render selftest` · `scratch-guard self-test` · `tier2-review self-test` · `loop definition` · `loop transition record` · `loop budget fixtures` · `loop position fixtures` · `loop composition fixtures` · `loop adapt fixtures` · `policy check` · `policy fixtures` · `core meta-check` · `docs` · `help page commands` · `help reference pages` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `every held leg is budgeted, every budget row resolves` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `build-method size` · `unattended protocol size` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `tags (the resolver's checks)` · `lexicon naming predicates` · `positional (the citation check alone)` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/breakpoints.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the `values`, `placed`, `ratification`, `stage`, `driver-close`, `driver-optin` and `driver-plan` plants, staged against the base tree, which has no breakpoints module and whose driver reads only the README and the conf · none

New arm: tools/unattended/unattended.test.sh · covers AC3 · a positive assertion of each new refusal's text, `check_owner_gates`' `fail 82` and `read_design_review`'s `fail 55`, staged against the base driver, which spells neither · waived for this build's landing by the build README's suite waiver, its text still read by the harness arms leg

## 8. Open questions

- **F1 — Which forks does the owner item hold, when no fork carries a class?** Options: (a) every
  fork the agent resolved under delegation; (b) none until a class exists; (c) every fork. (b) fails the
  clause's seen-red case, a planted major fork that must reach a gate. (c) holds forks the owner resolved
  already. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
- **F2 — Does `review.design: owed` take the README opt-in's place or sit beside it?** Options: (a) beside
  it, the README key deciding under `opt-in`; (b) fold the key and `SPEC_AUDIT_DEFAULT` into the policy
  value. (b) moves the owner's per-build channel and every reader of both keys, which the clause does not
  name. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
  grants: PLAY-dClosedLoop-3 the policy source of the spec-audit opt-in, the --close and --phase owner-gate refusals and the breakpoint lines of --plan, and BUILD-METHOD M4's "When" naming review.design
- **F3 — Where is an owner gate held in today's driver?** Options: (a) at `--close` and at the `--phase` move
  past the gated step, the places a run crosses a step exit; (b) only at `--close`. (b) lets a `three-gates`
  design gate pass the whole build before it holds. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
  Its `--phase` half moves to `TOOL-dDeclaredLoop-52` under F5, the table it read having no reader here.
- **F4 — Where does the owner item sit, now that the definition declares `item.build.ratify`?** The rev-2
  stand-in was placed "while the loop definition declares no `item.build.ratify` row", and at `250b236fe`
  it declares one, owned by dScopedBuild with the owner as its actor. Options: (a) at the declared
  `item.build.ratify`, under `author-owner-ratifies` with a delegated fork, released by a disposition
  record of that item; (b) keep rev-2's condition, which the landed definition makes never true, so the
  planted major fork reaches no gate; (c) read dScopedBuild's landing from its specs' statuses, a second
  "landed" reader beside the policy kit's. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated):
  (a), by rung 3.
  widens: none · relaxes: none
- **F5 — Where is an owner gate held at this tip?** I3's phase-to-step table has no reader in the tree,
  and `TOOL-dDeclaredLoop-52` ships it as rows with one reader at order 34, its S4 pointing this unit's
  `--phase` refusal at it. Options: (a) at `--close` alone, the `--phase` hold built by unit 52 on its map;
  (b) a phase-to-step copy here, a second copy of a map another unit owns; (c) the transition writer,
  which no unattended carrier runs. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by
  rung 1.
  widens: none · relaxes: none
- **F6 — What releases the plan gate?** `autonomy`'s default places it on every build. Options: (a) the
  authorization `check_authorization` verifies at the pinned BASE, the owner's landed README, so a default
  build closes as today; (b) a disposition record of `item.plan.exit`, which holds every run's close under
  the default. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F7 — What does an owner gate's disposition record name?** A record's `Item` must be an `item.` tag
  (`tools/memory-tree/build_records.py#check_disposition_fields`), and `TOOL-dDeclaredLoop-56` S13 adds
  `Hold` for the `decision` row later. Options: (a) `Item` the gate's position tag, read by
  `tools/loop/adapt.py#read_disposition_release`, `check_owner_disposition` left the exhaustion park's;
  (b) the `decision` row, which the record cannot spell until `Hold` lands; (c) widen
  `check_owner_disposition` to resume guards now, which has no tag to read on a hold the agent parked.
  Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F8 — `review.design` collides with the `[review.design]` table.** TOML cannot hold `design = "owed"`
  under `[review]` beside `[review.design]`'s `rounds`, the table `review.design.rounds` and
  `review.design.round-count` live in, and `review.build` meets `review.build.when` alike. Options: (a)
  read the catalogue's key as named, the collision stated as a risk for the owner's catalogue; (b) read
  another spelling, a key no catalogue row names. Recommendation: (a). RESOLVED (agent, 2026-11-16,
  delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F9 — Does the opt-in pack read `review.design`?** In a live run it reads only the `spec-audit` fact the
  preflight pins, which S8 pins under `owed`; in an attended session it reads the README and the conf.
  Options: (a) leave the pack, the attended gap stated; (b) widen it to the policy mirror through
  `tools/policy/policy-mirror.js`, a second kit's hook and suite. Recommendation: (a). RESOLVED (agent,
  2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F10 — What do `--close` and `check_authorization` read where the loop kit does not resolve?** The
  unattended kit copy-installs without it. Options: (a) nothing, the close going on and the opt-in read as
  today, since no item boundary exists to place a gate at without the loop kit's definition, as
  `load_review_bounds` takes the kit defaults (`TOOL-dDeclaredLoop-21` §8 F9); (b) refuse every close in
  such an install. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 19, flow-steps.md:516-562 and :302-317,
  layer-flow.md:299-303, and the driver's opt-in derivation, `print_spec_audit_line`, hold codes and
  `plan_state` read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-52, a hands-off TOOL-dDeclaredLoop-53, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-11-16 · §1 to §10 · S1 to S13 · AC1 to AC11 · §8 F3 to F10 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `250b236fe`, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-19-1-spec-writer`: symbol citations; the owner item at the declared
  `item.build.ratify` (F4); the hold at `--close` alone, `--phase` unit 52's (F5); the plan gate released
  by the authorization (F6); the release by `Item` through `read_disposition_release` (F7); the derived
  default computed, the table collision and the opt-in pack stated (F8, F9); the missing loop kit read as
  today (F10); `run_loop_verb`, `read_build_headers` and `plan_state`'s `delegated` mode extracted; the
  module's own leg enforcing `principle.p7`, the pending row deleted; the M4 rewording within its row;
  help, usage, sweep; the census 340 -> 342 PINNED under a decision row landed ahead.

## 10. Reuse audit

The owner gate reuses what holds a run for the owner today: the `decision` park `verb_park` writes, the
`owner-decision` hold the hand-off takes, and the owner's disposition record read by
`tools/loop/adapt.py#read_disposition_release`, which `TOOL-dDeclaredLoop-28` built for a held flow change.
The review breakpoint reuses `TOOL-dDeclaredLoop-20`'s `--trigger`, and the placement read reuses
`tools/loop/composition.py#read_tag_policy`. The spec-audit derivation is extended in place in
`check_authorization`, its two sources kept, and the forks are read by `plan_state`'s grammar. The runner
is extracted from `run_budget_verb` and the header read from `read_build_specs`, each at its second
instance. The list itself is new: no breakpoint list exists, and no code reads `autonomy`,
`review.<stage>` or `review.breakpoints` at `250b236fe` but the loop kit's own plants.

`python tools/codebase-map/reuse_lookup.py "list the review and owner breakpoints a build's policy places at item boundaries"`,
on the worktree at `179486e8f`, which holds no loop kit, ranked name-stem neighbours (`build`,
`read_policy_value`, `PolicyRefused`, `build_records`, `build_commit`); none lists or holds a breakpoint, so
no existing seam fits the list itself, and the seams above are where it attaches, found by reading the
branch. `python tools/memory-recall/query.py "where does a build hold for the owner at a review or owner
gate breakpoint" --terms "<the terms below>"` returned the scout record's row for this unit, this spec's
rev-2, the packet's clause, and `TOOL-dPlacedRequest-5`'s note that `--trigger`'s `placement` cause is
already in its closed set.

Recall terms used: breakpoint owner gate autonomy review.design spec-audit opt-in ratify disposition decisions.major placement
