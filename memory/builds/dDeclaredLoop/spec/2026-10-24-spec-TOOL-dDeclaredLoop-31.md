# TOOL-dDeclaredLoop-31 — `flow.on-exhausted`: a build whose budget is spent ends by a transition row, and never laps again

**Status:** CLOSED · rev-4 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 30 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0116@d75a79f0 whole

**Carries:** node:policy-key.flow.on-exhausted

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-build-TOOL-dDeclaredLoop-1-crosscheck-returns.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-1-crosscheck-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 |
| [2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 |
| [2026-11-05-build-TOOL-dDeclaredLoop-1-reground-returns.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-1-reground-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 |
| [2026-11-05-build-TOOL-dDeclaredLoop-31-deviation-311.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-31-deviation-311.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-31-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-31-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-31-deviation-312.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-31-deviation-312.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-31-deviation-313.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-31-deviation-313.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-31-red-fix-48.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-31-red-fix-48.md) | red-fix | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-56 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-31-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-31-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-31-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-31-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-31-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-31-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

A build whose rework budget is spent ends, and never laps again. `flow.on-exhausted` names how:
`best-effort-ending`, the default, takes the ending the build's units support and records it for the
owner; `park-for-owner` hands the build to the owner until the owner's disposition record;
`close-incomplete` closes it `incomplete`, its branch and records kept. Each ending is a row of the
build's transition table, and a lap after the budget is spent is refused naming what follows. Today
`tools/loop/budget.py#record_draw` answers `exhausted` and the driver's two draw sites refuse the lap,
but no verb reads `flow.on-exhausted`, no row enters `incomplete` or `parked`, and no halt code says a
spent budget ended a run (`gap-flow-23`).

## 2. Scope (IN)

- **S1** — The ending rows. Five `[[transition]]` rows of the build table in `tools/loop/loop.toml`, E1
  to E5 of §4, each on the item `@any`: its outcome the ending it records, `close-incomplete`,
  `park-for-owner` or `descope`, or `disposed` on the two rows out of `parked`, which match the
  owner's `disposition` fact, `continue` or `none`. Each carries `draws = "none"`, an optional row field
  the file's schema comment gains. `tools/loop/loop_table.py#check_transition_tables` admits `@any` on a
  row entering `@reentry`, as today, or on a row whose outcome is one of `ENDING_OUTCOMES`, those four
  words (§8 F4). `tools/loop/loop_transition.py#write_transition` draws `route-back` on a backward move
  only where the matched row's `draws` is not `none`, so E5 records on a spent budget. Observed by AC6.
- **S2** — The rule and its reader, in `tools/loop/budget.py` (§8 F5): `derive_ending(value, units)`,
  pure, §4 "The rule"; and `read_ending(build, root)`, which answers §4's ending line from one
  `read_budget_rows` read, `budget_state` over it through a new optional `held`, the value at HEAD
  through the policy kit's `resolve` as `read_budget_value` reads its keys, each unit's status header
  through `read_build_specs`, a reader of `tools/loop/loop_transition.py` that `read_build_unit_ids`
  then maps, and the owner's record through `tools/loop/adapt.py#read_disposition_release`. A unit is
  witnessed green when its header reads `CLOSED` (§8 F3), and open when it reads neither `CLOSED` nor
  `WONTDO`. The verb `budget.py ending --build <slug>` prints the line. Observed by AC1.
- **S3** — The verb `--exhausted <slug>`, `run_exhausted` in `tools/unattended/unattended.sh`, §4 "The
  verb": a standing exhaustion row is printed and nothing written; otherwise it reads the ending line
  through `TOOL-dDeclaredLoop-32`'s `run_budget_verb`, refuses unless its state reads `spent` (one
  `fail 37` site, which also relays a module refusal), parks the exhaustion record, one `decision` row,
  and prints the act its ending owes (S4) and that only the owner raises `flow.rework-budget`.
  Observed by AC2, AC3.
- **S4** — Each ending's act, through verbs that exist (§8 F6). `close-incomplete` is `--abort <slug>
  --code budget-exhausted`: the code joins `HALT_CODES_CORE` and not `HALT_CODES_HANDOFF`, and
  `verb_abort` refuses it (one `fail 33` site, through `check_exhausted_close`) unless the record holds
  an exhaustion row whose ending is `close-incomplete`, or `park-for-owner` with the owner's disposition
  `none`, and every open unit has its `rescope · item defer` row in force, read by
  `check_unit_deferred`. `park-for-owner` is `--handoff <slug> --code owner-decision`, whose parked
  decision is the exhaustion row. `land-green` and `descope` go on to `--close`, whose `build-complete`
  term lands the `CLOSED` units once every other unit is `DEFERRED` with an open ask it filed and a
  defer row (TOOL-dUnstuckLanding-23). Observed by AC4, AC5.
- **S5** — The lap refusal names its remedy. Each draw site already refuses the lap on `budget.py
  draw`'s exit 3, a spec subject's round excepted, so this unit adds no second guard: on exit 3
  `run_budget_draw` appends to `_bd_why`, which both relays print, `end the build with --exhausted
  <slug>` while no exhaustion row stands, else the recorded ending and that only the owner raises
  `flow.rework-budget`. `--fix-pass` draws nothing (`TOOL-dDeclaredLoop-32` §3), so it is no draw site
  here. Observed by AC2.
- **S6** — The exhaustion park is left by the owner. `check_owner_disposition <slug>` answers whether
  the ending line's `disposed` field reads `continue`. `verb_resume`'s HELD row, after its
  release-condition test and before any write, refuses (one `fail 57` site) a record held under
  `owner-decision` whose exhaustion row reads `park-for-owner` until that answer holds; every other
  hold resumes as it does today (§8 F7). Observed by AC5.
- **S7** — The phase reading: an `ABORTED` run whose `halt-code` is `budget-exhausted` reads
  `incomplete`, and a `HELD` run under `owner-decision` whose exhaustion row reads `park-for-owner` reads
  `parked`. `TOOL-dDeclaredLoop-52` ships both as qualified rows of its phase map; no reader in the tree
  applies the I3 table today, so this unit writes none (§8 F8). NOT OBSERVED, because the reader is
  that unit's.
- **S8** — Raising the budget stays the owner's. No ending raises `flow.rework-budget`, and
  `--exhausted` prints that only the owner raises it. `tools/policy/guard.py --staged` refuses an
  agent's staged raise off a live run's branch and admits one on it (PLAY-dOrderedCharter-84); this
  unit observes the first and changes neither. Observed by AC7.
- **S9** — The carriers. `tools/unattended/VERBS.template.md` gains a `--exhausted` entry naming the
  values, the halt code and the release, and its "Abort" path names `budget-exhausted`;
  `tools/unattended/SKILL.template.md` gains `unattended.sh --exhausted <slug>` in its fenced verb list;
  the driver's header gains the verb's line and `VERBS_SLUG` the verb, which takes no flag and so no
  `VERB_REQUIRES` row. `help/loop.md` states the endings and the rows, anchoring
  `verb:unattended.sh:--exhausted` and `budget.py`'s `#ending` row, which `tools/govkit/usage.toml`
  gains; `tools/loop/README.md` states the rows and the `@any` rule. Renders are their templates'
  copies. Observed by AC8.
- **S10** — The suite arms the `New arm:` lines in §7 declare. Observed by AC1, AC2, AC3, AC4, AC5 and
  AC6 through those lines, RED first at the close.

## 3. Non-goals (OUT)

- The budget, its draws, homes, count and freeze: `TOOL-dDeclaredLoop-30`'s, refined by units 48, 49,
  60, 61 and 62. This unit adds no counter.
- When a loop ends and where its findings go: `TOOL-dDeclaredLoop-32`'s routing, and BUILD-METHOD M4's
  spec-audit rule for a spec audit. The routing's ` · to on-exhausted` target sends a build here.
- The other rows and the engine: `TOOL-dDeclaredLoop-13`'s.
- Reverting a descoped unit from Test's tree, `build.revert-pass`: dScopedBuild's. E5 records the move.
- Witness-derived unit state; `derive_ending` reads status headers.
- The disposition grammar: `TOOL-dDeclaredLoop-16`'s. A `Hold` field and `check_owner_disposition` for
  every owner gate: `TOOL-dDeclaredLoop-56` S13 and `TOOL-dDeclaredLoop-19`.
- A second exhaustion after the owner's `continue` and a raise: the first row stands and is printed.
- An owner-silence deadline on a parked build, and any raise of `flow.rework-budget`: the guard is a
  parent build's, observed and never extended.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-13` — `loop.toml` transition rows and `[states]`: the build table the ending rows
  join and the engine that answers them; without it the rows have no table
- **consumes-from** `TOOL-dDeclaredLoop-16` — `record-kind.disposition`: the owner's disposition record that
  alone leaves the park; without it the release has nothing to read
- **consumes-from** `TOOL-dDeclaredLoop-30` — `flow.rework-budget`: `budget_state` and `read_budget_rows`,
  which the ending line reads, and `record_draw`'s `exhausted` answer, at whose relay the remedy prints
- **consumes-from** `TOOL-dDeclaredLoop-32` — `flow.route-backs`: `run_budget_verb`, through which the driver
  reads the ending line, and the ` · to on-exhausted` target that sends a fix-pass loop here
- **hands-off** `TOOL-dDeclaredLoop-19` — `record-kind.disposition`: `check_owner_disposition`, which that
  unit widens from the exhaustion park to every owner gate
- **hands-off** `TOOL-dDeclaredLoop-33` — `flow.on-exhausted`: the ending rows and their `draws = "none"`,
  which the termination check reads as terminal paths and uncounted edges
- **hands-off** `TOOL-dDeclaredLoop-52` — the phase-to-state-and-step map, which that unit ships as rows with one reader, S7's two readings among them (the round-1 spec audit's id 4)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 10, 15, 34, each a scope item of that unit; id 15's spent-only refusal holds here already

## 4. Design

### The rows

| Row | `from` | outcome on `@any` | `disposition` | `when` | `to` | Witness |
|---|---|---|---|---|---|---|
| E1 | the five step states | `close-incomplete` | | before-push | `incomplete` | the exhaustion record, and every open unit's `defer` row |
| E2 | the five step states | `park-for-owner` | | | `parked` | the exhaustion record and the hand-off |
| E3 | `parked` | `disposed` | `continue` | | `@prior` | the owner's disposition record |
| E4 | `parked` | `disposed` | `none` | before-push | `incomplete` | the owner's disposition record, and every open unit's `defer` row |
| E5 | `testing` | `descope` | | | `building` | the exhaustion record naming the descoped unit, and the revert commit |

The five step states are `planning`, `designing`, `building`, `testing` and `deploying`, written out
because `@open` holds `paused` and `parked` too. Each row carries `draws = "none"`. These are the
flow-steps record's rows (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`),
E1 serving `best-effort-ending` where nothing can land. None collide under the one-row rule: E1, E2 and
E5 differ by outcome, E3 and E4 by `disposition`, which `check_transition_tables` already reads as
disjoint. `derive_move` is unchanged: it matches item and outcome exactly, and E3 takes `prior` as B20
does. A descope in Build moves no state and has no row; its units go to asks, named on the exhaustion
record.

E5 is a backward move, and `write_transition` draws `route-back` on every backward move, refused on a
spent budget. It reads the row `derive_move` returns and skips the draw where `draws` is `none`, so an
ending is never a lap; a row without the field draws as today.

### The rule

```
derive_ending(value, units)                            units: {id: status}
  value == "park-for-owner"                         -> park-for-owner
  value == "close-incomplete"                       -> close-incomplete
  value == "best-effort-ending":
    counted = units whose status is not WONTDO
    counted non-empty and every one CLOSED          -> land-green
    some unit CLOSED                                -> descope
    otherwise                                       -> close-incomplete
  any other value                                   -> ValueError naming flow.on-exhausted and the value
```

A build with no units has nothing to land, so the flow-steps join's planted build that spends its
budget in planning reaches `incomplete`. The function returns an ending, never a draw.

### The ending line

```
loop: budget · ending · <ending|none> · <open|unfrozen|spent> <spent>/<total> · open <ids|none> · disposed <word|unrecorded>
```

The ending is `derive_ending`'s where the state is `spent`, else `none`; the ids are the open units,
space-joined; `disposed` is the `Disposition` word of the newest disposition record of the build whose
`Item` is `item.flow.on-exhausted` (`EXHAUSTED_ITEM`), else `unrecorded`. Exit 0; a value outside the
catalogue's three or a row outside its grammar prints `loop: budget · refused · <why>` and a kit that
does not resolve `loop: unarmed · <why>`, each exit 2, through `main`'s existing handlers.

### The verb

```
--exhausted <slug>                                     run_exhausted
  check_slug, check_run_state, refuse_if_terminal
  read_exhausted_row: a standing row -> print its ending and act, write nothing, exit 0
  read_exhausted_ending (run_budget_verb ending)       state not spent, or no line -> fail 37
  park "$rel" decision flow.on-exhausted "ending <e> · spent <s>/<t> · open <ids>"; stage
  print the act:
    close-incomplete  file each open unit with --rescope --act defer, then --abort --code budget-exhausted
    park-for-owner    reap the keepalive, then --handoff --code owner-decision
    land-green        go on to --close
    descope           defer each open unit against an ask, record --rescope --act defer, then --close
  print: only the owner raises flow.rework-budget
```

`read_exhausted_row <rel>` sets `_ex_row` to the newest `decision · item flow.on-exhausted` row's
ending, empty where none stands. `read_exhausted_ending <slug>` runs the verb once and sets `_ex_end`,
`_ex_state`, `_ex_open`, `_ex_disp` and `_ex_why`, answering 1 where the module does not answer. The
`decision` kind is owed (`tools/unattended/unattended.sh#PARK_KINDS_OWED`), so the record is surfaced
at the wrap-up, and it is the parked decision `run_handoff` requires under `owner-decision`.

### The acts and the release

`check_exhausted_close <slug> <rel>` runs in `verb_abort` for `budget-exhausted` where
`check_inherited_override` runs for `gate-red-out-of-scope`, after one `read_exhausted_ending`:
`_ex_row` must read `close-incomplete`, or `park-for-owner` with `_ex_disp` reading `none`, and
`tools/unattended/lib-unattended.sh#check_unit_deferred`, given `DEFERRED`, must answer 0 for each id
`_ex_open` names; the first miss is the `fail 33` site's. Outside `HALT_CODES_HANDOFF`, the code draws
no `print_abort_notice`. `check_owner_disposition <slug>` answers 0 where `_ex_disp` is
`continue`, else 1 with `_od_why`; `verb_resume` calls it after `check_hold_condition_met`, whose `owner`
condition is met on any resume, only where `hold-code` is `owner-decision` and `_ex_row` reads
`park-for-owner`. The owner writes the record through `build_records.py new disposition`, its item
`item.flow.on-exhausted`.

### The lap refusal

`run_budget_draw` keeps its name, arguments and two relays, `verb_review`'s `fail 37` and
`verb_dispatch`'s `fail 49`. On exit 3 it runs `read_exhausted_row` and appends ` · end the build with
--exhausted <slug>` where no row stands, else ` · the build's ending is <ending>, and only the owner
raises flow.rework-budget`, after the module's line, which keeps naming `flow.on-exhausted`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `--exhausted` | driver verb | flag, none |
| `run_exhausted`, `read_exhausted_row`, `read_exhausted_ending`, `check_exhausted_close`, `check_owner_disposition` | bash functions | `sh.function`, verb-first |
| `derive_ending`, `read_ending`, `read_build_specs` | Python functions | `py.function`, verb-first |
| `ending` | `budget.py` verb | none |
| `ENDING_OUTCOMES`, `EXHAUSTED_ITEM` | Python constants | none |
| `land-green`, `descope`, `disposed`, `unrecorded` | ending words, outcome, field word | none |
| `budget-exhausted` | halt code | none |
| `draws` | `[[transition]]` row field | none |
| `item.flow.on-exhausted` | the disposition record's `Item` | `tag.item` |

Each function name passed `python tools/lexicon/lexicon.py --suggest <name> --as <cell>` on the
worktree at `179486e8f`, whose verb declarations equal the branch's; the tag passed `--as tag.item` on
the branch's tree, which alone registers the `item` namespace.

### Migration

None. `flow.on-exhausted` has its catalogue row, and a run before this unit that was refused a lap
reads the remedy at its next refused draw.

### Rollout

Live at landing. The abort guard and the resume guard fire only on `budget-exhausted` and on a record
holding an exhaustion row, which no run before the verb writes.

### Files touched (estimate)

- `tools/loop/loop.toml`
- `tools/loop/loop_table.py`
- `tools/loop/loop_transition.py`
- `tools/loop/budget.py`
- `tools/loop/README.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/govkit/usage.toml`
- `help/loop.md`
- `tools/template-size-limits.txt`
- `.memory-tree.conf`
- `memory/project/positional-refs.txt`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`, `memory/map/generated/CARDS.md`,
  `memory/map/generated/inventories.json`

Each render is its template's copy: `memory/guides/UNATTENDED-VERBS.md` and
`.claude/skills/unattended/SKILL.md`.

### Alternatives rejected

- **A new INCOMPLETE phase.** Every reader of `PHASES_CORE` and the hook that restates its tail would
  gain a member, for a state an `ABORTED` record and its halt code already say.
- **A new `exhausted` park kind.** Owed kinds are spelled in two sibling kits held to the driver's line
  both ways; the `decision` kind is owed and is what `--handoff --code owner-decision` requires.
- **Let the driver pick the ending by judgment.** "The ending its evidence supports" is a derivation
  over the units' headers, and a derivation cannot choose to lap.

## 5. Production-readiness checklist

- security — no new write surface: one `park()` row, inheriting its line-end refusal, and the existing
  abort and hand-off with every refusal they make.
- perf / scale — one python start per `--exhausted`, per `budget-exhausted` abort and per resume of an
  exhaustion park; a refused draw adds one `grep`.
- error / empty / loading states — a module that does not answer, an unspent budget and an unknown
  value each refuse naming why; no units reads `close-incomplete`.
- observability — the record names the ending, the spend and every open unit, owed at the wrap-up.
- risks — `CLOSED` is a typed header; the guard admits an agent's raise on a live run's branch, which
  nothing here refuses; anyone who can write a disposition record through the door releases the park.
- testing — the budget plants run the module and the driver in scratch repositories, the table's and
  the writer's plants in memory and in scratch; the arms in §7 observed RED then GREEN.
- migration — none.
- user docs — `help/loop.md` states the endings, the rows and both commands; the verbs carrier the verb.

### The sweep

Read at branch `unattended-declared-loop-d56bf0`, tip `a68d80da1`, through `git show` and an export of
that commit; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| the build table | `check_transition_tables`, `derive_move`, `check_recorded_move`, `tools/loop/position.py` (unit rows), `tools/loop/scenario.py` (entry rows), `tools/loop/loop_parents.py`'s parent row | the route join skips an undeclared item; the other readers read rows these are not |
| the `@any` rule | B11; `loop_table.py`'s `PLANTS` and selftest moves | B11 enters `@reentry`; the `any-unending` plant keeps the refusal's text |
| the backward draw | `loop_transition.py`'s plants; `budget.py`'s `before-freeze`, `re-entry` and `trailer-only` plants | a row without `draws` draws as today |
| `read_build_unit_ids` | `resolve_build_anchor`, `read_budget_rows`, `freeze_budget` | it maps `read_build_specs`: same ids, same order |
| `budget_state` | `promotion_target`; plants asserting `open 2/6`, `unfrozen 1/4`, `unfrozen 2/4`; unit 32's `target` verb | `held` defaults to a fresh read |
| `budget.py`'s `main`, `PLANTS` | `loop budget fixtures`; the `#draw` and `#value` usage rows; units 60, 61, 62 adding plants | an added branch and added keys; other verbs byte-identical |
| `run_budget_draw` | both relays; the `spent-spec-round` plant's and the driver suite's `flow.on-exhausted` match | only exit 3 appends, after the module's line |
| `verb_abort`, `HALT_CODES_CORE` | check 2's `HALT_FLOOR`, a lower bound at 8; check 2's halt-code join over `RUN*.md`; `print_abort_notice` | the core grows by one; the join admits a core member; no hand-off code |
| `verb_resume` | the driver suite's `owner-decision` hand-off arms | the guard needs an exhaustion row, which none plants |
| `VERBS_SLUG`, the header | check 26's verb arm (header, carrier entry `- \`--exhausted\` — `, Skill line) and flag arm; check 52; the `docs` leg's new verb row, which the shrink-only undocumented list cannot take | the carriers of S9; no flag; no `VERB_REQUIRES` row; the anchor |
| the Skill render | `unattended skill size`, at unit 32's 10815 PINNED row | it rises by 33 PINNED bytes to 10848 PINNED, re-measured at the build |
| `item.flow.on-exhausted` | the `tags` leg's resolves join over backticked unfenced spans outside `builds/` | carriers spell it inside a fenced block, as `help/loop.md` spells `item.life.close` |
| other builds | `TOOL-dWellOiledMachine-59` calls `endings.py derive --state`; `TOOL-dRankedPlan-10` and `TOOL-dFurnishedOrders-16` read `check_owner_disposition` as general | §8 F5 and F7; their re-grounds read the landed names |
| subject pins, epoch delegates, upgrade rows | `tools/govkit/subject-pins.tsv`, `check-verdict-epoch.sh`'s `DELEGATES`, `[[upgrade]]` | no memory-tree file, no subject, no migration |
| suite floors | each `FLOOR_ASSERTIONS`, a lower bound | may rise by the arms added |

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:.claude/skills/unattended/SKILL.md" | tr -d '\r' | wc -c       # 10755, before unit 32
python tools/loop/loop_table.py check | head -n 1                          # on an export of $B: 31 rows
printf '%s\n' 'unattended.sh --exhausted <slug>' | wc -c                    # 33
```

### Budgets and records

- The driver's census, read through `tools/memory-tree/check-arms.py#branches` and
  `tools/memory-tree/check-arms.py#scan_refusal_sites` over the export, is 329 PINNED (324 branches and
  5 sites at `a68d80da1`), at its ceiling of 329 PINNED; `TOOL-dDeclaredLoop-32` raises both to 332
  PINNED. This unit adds three sites, S3's, S4's and S6's, so the ceiling rises 332 -> 335 PINNED with
  the comment line below, and `memory/project/positional-refs.txt`'s row pairing `.memory-tree.conf`
  with the driver at 332 PINNED is re-pointed in place to 335.
- The families of `tools/unattended/unattended.families.txt` do not move: no new message spells
  `requires --`, `requires $`, a newline, a carriage return, a separator or the bypass flag, and none
  opens `no run-state file`.
- `tools/unattended/check-unattended.sh` stays at 266 of its 266 PINNED; it is not edited.
- `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED: every new name leads with a declared verb.
- The shared records: the pass writes neither `memory/DECISIONS.md` nor
  `memory/project/readme-contract.txt`. The run lands the decision row below ahead of the pass, and the
  pass writes the comment line above `REFUSAL_CEILINGS` in `.memory-tree.conf`:

```
- **TOOL-dDeclaredLoop-31** - **the driver's refusal ceiling rises by three, 332 -> 335, for `--exhausted`'s relay, the `budget-exhausted` abort's guard and the exhaustion park's resume guard, and the `--exhausted` invocation the unattended Skill gains raises its render's no-headroom size row 10815 -> 10848, under TOOL-aSparedSpawn-14's rule and TOOL-aOrientedCast-23's four raise terms, as TOOL-dDeclaredLoop-32 raised both**: agent, <date>, under ER:388 (PLAY-dClosedLoop-6), landed ahead of the pass that makes both raises. Detail `builds/dDeclaredLoop/`.
# TOOL-dDeclaredLoop-31 RAISED the driver 332 -> 335, the census, under decision TOOL-dDeclaredLoop-31 (ER:388): --exhausted's relay, the budget-exhausted abort's guard and the exhaustion park's resume guard.
```

- The kickoff manifest watches `.memory-tree.conf`, so `memory/guides/SESSION-KICKOFF.md`'s
  `last-audit` is re-stamped with a `manifest-audit:` delta line.
- Help anchors: `verb:unattended.sh:--exhausted` and `script:tools/loop/budget.py#ending`, each with the
  fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints.
- The map: `python tools/codebase-map/gen_map.py --write` regenerates `symbols.json` and its siblings.
- Shipped comments name siblings by file name or `<prefix>`, never a kit path; the loop and unattended
  kit versions are owed at the lander.
- This revision turns the spec's line citations into symbol citations, so the commit landing it runs
  `python tools/playbook/positional.py shrink`, which takes their rows out of the positional list.

### Dependency

Order 30, beside units 60, 61 and 62, read on their committed specs: each edits `tools/loop/budget.py`
(the run-state population, a draw id, an append-only plant) and none renames `read_budget_rows`,
`budget_state` or a verb. `TOOL-dDeclaredLoop-32` (order 29, building) is read on its committed rev-5:
`run_budget_verb`, the ceiling of 332 and the Skill row of 10815, both PINNED there. Units 13, 16, 21,
30, 48 and 49 are CLOSED, read on landed code; `TOOL-dDeclaredLoop-34` is deferred against ask
TOOL-dDeclaredLoop-113 and shares no file. The suggests, the reuse probe and the recall query ran on
the worktree at `179486e8f`; every other claim was read on the branch.

## 6. Acceptance criteria

- **AC1** — When a scratch probe calls `budget.py`'s `derive_ending` under `best-effort-ending`, it
  answers `land-green` over one `CLOSED` and one `WONTDO` unit, `descope` over one `CLOSED` and one
  `INPROGRESS`, and `close-incomplete` over none `CLOSED` and over none at all; each other value answers
  itself over all `CLOSED`; `lap` raises naming `flow.on-exhausted`. And `python tools/loop/budget.py
  --fixture --plant ending` prints `held`: one `CLOSED` and one `INPROGRESS` spec under `rework-budget =
  0` and a committed `continue` record of `item.flow.on-exhausted` print `loop: budget · ending ·
  descope · spent 0/0 · open <the INPROGRESS id> · disposed continue`, and the default value prints
  `ending · none · unfrozen`.
  Red when: best effort over a mixed roster answers `land-green` or a lap.
  figure: `0/0` PINNED by the plant's policy file.
- **AC2** — When `python tools/loop/budget.py --fixture --plant driver-exhausted` runs the driver over a
  build under `rework-budget = 0`, it prints `held`: the build slug's second `--review` round exits 1
  naming `--exhausted`; `--exhausted <slug>` exits 0 and the run-state file gains one `decision · item
  flow.on-exhausted · reason ending ` row holding `spent 0/0`; a second `--exhausted` adds no row; and a
  further round on the slug and a second `--dispatch` of one unit each exit 1 naming the recorded
  ending and that only the owner raises `flow.rework-budget`.
  Red when: a round after the exhaustion row is admitted, a best-effort lap.
  cost: the driver in a scratch repository, about a minute.
- **AC3** — When the same plant runs `--exhausted <slug>` on its build under the default
  `flow.rework-budget`, it exits 1 naming `unfrozen`, and the run-state file's bytes are unchanged.
  Red when: the verb ends a build that still has budget.
- **AC4** — When the same plant sets `on-exhausted = "close-incomplete"` under `[flow]` with one unit
  open, runs `--exhausted` and attests `keepalive-reaped` and `parked-decisions-surfaced`, then
  `--abort <slug> --code budget-exhausted --reason r` exits 1 naming that unit; after `--rescope <slug>
  --act defer --item <id> --reason r` it exits 0, the record reads `phase: ABORTED` and `halt-code:
  budget-exhausted`, and `git rev-parse --verify main` still resolves; and on a record with no
  exhaustion row the same abort exits 1.
  Red when: the abort runs with an open unit unfiled, or with no exhaustion row.
- **AC5** — When a scratch repository whose policy file sets `on-exhausted = "park-for-owner"` and whose
  conf declares a `LANDER` runs `--exhausted`, then `--handoff <slug> --code owner-decision --reason r
  --reaped k1`, the run is HELD under `owner-decision`; `--resume <slug> --keepalive-id k2` exits 1
  naming `item.flow.on-exhausted`; once `build_records.py new disposition` has written and committed a
  record of that item reading `continue`, the same `--resume` takes the run over; and an `owner-decision`
  hand-off with no exhaustion row resumes as before.
  Red when: `--resume` leaves the park with no disposition record.
  cost: the driver in a scratch repository, about a minute.
- **AC6** — When `python tools/loop/loop_table.py check` runs it prints `loop: table build · 36 row(s)`, PINNED;
  `move --level build --from building --item @any --outcome close-incomplete --fact pushed=no` prints
  `move — build · building → incomplete`, the same from `landed` is refused, and `--from parked --item
  @any --outcome disposed --fact disposition=continue --fact prior=testing` prints `parked → testing`;
  `--fixture --plant any-unending` exits 1 naming `only a row entering @reentry`; a scratch probe reading
  `read_transition_rows` finds E1 to E5, each with `draws = "none"`; and `python
  tools/loop/loop_transition.py --fixture --plant descope-spent` prints `held`, its spent build
  recording `testing -> building` on `@any`'s `descope` with no draw row, where the backward move on
  `item.test.attribute`'s `code-miss` is refused naming the spent budget.
  Red when: E5 lacks `draws = "none"`, so the descope draws `route-back` and is refused.
  figure: 36 PINNED, the 31 rows PINNED at `a68d80da1` and the five this unit adds.
- **AC7** — When `python tools/policy/guard.py --staged` runs at the top of a scratch copy holding no
  run-state file, with an agent's raise of `flow.rework-budget` from `"4+2"` to `"6+2"` staged in
  `.governance/policy.toml`, it exits 1; and AC2's `--exhausted` output holds `only the owner raises
  flow.rework-budget`.
  Red when: the guard admits the raise off a live run's branch.
- **AC8** — When `grep -c -- '--exhausted'` runs over `tools/unattended/VERBS.template.md` and
  `memory/guides/UNATTENDED-VERBS.md` each prints at least 1; `grep -c 'unattended.sh --exhausted '`
  prints 1 over `tools/unattended/SKILL.template.md` and over `.claude/skills/unattended/SKILL.md`;
  `tr -d '\r' < .claude/skills/unattended/SKILL.md | wc -c` equals that render's row in
  `tools/template-size-limits.txt`; and `python tools/govkit/docs_leg.py --list` names
  `verb:unattended.sh:--exhausted` and `budget.py`'s `#ending` row as anchored on `help/loop.md`.
  Red when: a template is edited and its render is not, or the verb ships with no anchor.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `scratch-guard self-test` · `tier2-review self-test` · `govkit acceptance matrix` · `unattended skill size` · `unattended skill wiring` · `check-wiring self-test` · `loop definition` · `loop transition tables` · `loop transition record` · `loop budget fixtures` · `loop position fixtures` · `loop parent routes` · `loop command conformance` · `policy fixtures` · `docs` · `help page commands` · `govkit selftest` · `govkit refusal join` · `tags (the resolver's checks)` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `positional (the citation check alone)` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/budget.py · covers AC1 AC2 AC3 AC4 · the `ending` and `driver-exhausted` plants, staged against the base module, which has no `ending` verb, and the base driver, which has no `--exhausted` · none

New arm: tools/loop/loop_table.py · covers AC6 · the `any-unending` plant and the ending moves, staged against the base table, which holds no ending row · none

New arm: tools/loop/loop_transition.py · covers AC6 · the `descope-spent` plant, staged against the base writer, which draws on every backward move · none

New arm: tools/unattended/unattended.test.sh · covers AC5 · the exhaustion park's refused and admitted resume, and a positive assertion of each new refusal's text, staged against the base driver · waived for this build's landing by README rule 8, its text still read by check 26 and the harness arms leg

## 8. Open questions

- **F1 — What fires an ending row, when no item exits there?** Options: (a) the `@any` item with the outcome
  `exhausted` and a fact `ending`, the form `TOOL-dDeclaredLoop-13`'s B11 row already takes, its fact graded
  by `check_transition_tables` as `reenters` is; (b) the policy tag `policy.flow.on-exhausted`, which
  `check_transition_tables` refuses as a row `item` that resolves to no declared item; (c) a new item
  `item.build.exhausted`, which mints an item no clause or owned node names, for an ending that fires from
  any open state rather than from one step's program. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
  The rows out of `parked` take the owner's disposition, `continue` back to the prior state and `none` to
  `incomplete`, the two words `TOOL-dDeclaredLoop-28` grades a held change by. The row form is F4's.
- **F2 — Where does `incomplete` live in the driver?** Options: (a) ABORTED with the halt code
  `budget-exhausted`, read as `incomplete` by the engine's phase reading; (b) a new INCOMPLETE phase. (b) moves every
  reader of the phase set for a state the map can read. RESOLVED (agent, 2026-10-24, delegated): (a),
  rung 3.
- **F3 — Is "witnessed green" the spec's `CLOSED` header or a computed witness?** Options: (a) the header,
  today's only per-unit fact; (b) the position engine's derived state, which this unit's edges do not
  reach. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, with the risk named in §5.
  grants: PLAY-dClosedLoop-3 the --exhausted verb, the budget-exhausted halt code and their statement in the unattended verbs carrier
- **F4 — How does an ending row fire under the landed engine?** `check_transition_tables` admits `@any`
  only on a row entering `@reentry`, `derive_move` matches no `ending` fact, and its one-row rule tells
  rows apart by `disposition` alone. Options: (a) F1's form, the outcome `exhausted` and a fact
  `ending`, which teaches all three the fact; (b) the ending word as the outcome on `@any`, `disposed`
  with a `disposition` on the rows out of `parked`, which widens the `@any` rule alone; (c) a stand-in
  item, which books an item no build owns. Recommendation: (b). RESOLVED (agent, 2026-11-16,
  delegated): (b), by rung 3.
  widens: none · relaxes: none
- **F5 — Where does the ending rule live, and how does the driver reach it?** Options: (a) `budget.py`,
  which names the key and reads the budget, through a verb `ending` reached by `run_budget_verb`; (b)
  a new `tools/loop/endings.py` whose `derive` verb the driver feeds statuses and a state. (b) puts the
  roster read in the driver, adds a module with its own rows, selftest and help, and its state has no
  source the driver holds; (a) costs `TOOL-dWellOiledMachine-59` a home change at its re-ground. Recommendation: (a). RESOLVED (agent,
  2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F6 — Does `--exhausted` act, or record and name the act?** Options: (a) it records and prints the
  act, the existing `--abort` and `--handoff` acting, the abort guarded for `budget-exhausted`; (b) it
  calls `verb_abort` and `run_handoff` itself. (b) meets the abort's two attestations and the hand-off's
  reaped keepalive inside one call, which an agent completes only between calls. Recommendation: (a).
  RESOLVED (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F7 — Which hold does the disposition release?** A disposition record's `Item` must be an `item.`
  tag (`tools/memory-tree/build_records.py#check_disposition_fields`), so it cannot name a `decision`
  row. Options: (a) the exhaustion park only, by the tag `item.flow.on-exhausted`, units 19 and 56
  widening `check_owner_disposition` once `Hold` lands; (b) every `owner-decision` hold, which has no
  tag to read and would wedge each existing hand-off's resume; (c) no release check. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F8 — Where does the phase reading live?** No reader in the tree applies the I3 table:
  `tools/loop/loop_parents.py#WITHDRAWN_PHASE` reads every `ABORTED` parent as withdrawn, and
  `TOOL-dDeclaredLoop-52` ships the map as rows with one reader, its S1 naming this unit's two readings.
  Options: (a) that unit ships them; (b) this unit adds a reader of its own. (b) is a second copy of a
  map another unit owns. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by rung 1.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 31, the brief's I3, I19 and I20,
  flow-steps.md:758-770, and the driver's abort, hold, resume and rescope verbs read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-52, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-11-05 · §3 · S5 · §4 The lap refusal · AC2 · the non-goal gives a follow-up's and a fix pass's end and findings
  to TOOL-dDeclaredLoop-32 and a spec audit's to BUILD-METHOD M4's spec-audit rule; the lap refusal and
  AC2 read the closing review's round, a spec subject's round being unrefused under TOOL-dDeclaredLoop-30
  rev-4 S4, by the brief prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md
- rev-4 · 2026-11-16 · §1 to §10 · S1 to S10 · AC1 to AC8 · §8 F1 F4 to F8 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `a68d80da1`, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-31-1-spec-writer`: symbol citations; the ending as the row's
  outcome and `draws` read by the writer (F4); the rule and its line in `budget.py`, no state argument
  (F5); the verb records and names the act, `--abort` guarded and the park a hand-off (F6); the release
  by `item.flow.on-exhausted` for the exhaustion park (F7); the phase reading unit 52's (F8); the
  guard's live-branch admission; the remedy on `run_budget_draw`'s relay; the census 332 -> 335 PINNED
  and the Skill row 10815 -> 10848 PINNED under a decision row landed ahead; help, usage, sweep.

## 10. Reuse audit

No ending seam exists: `tools/loop/budget.py#record_draw` answers `exhausted` and leaves the ending
here, and the driver's one derived terminal is `write_landed_record`. The unit extends what exists:
the build table and `check_transition_tables` for the rows, the transition writer's backward draw for
`draws`, `budget.py`'s reads and `main` for the rule and its line, `adapt.py#read_disposition_release`
for the owner's record, `run_budget_verb` for the call, `park()` and the owed `decision` kind for the
record, `verb_abort`'s code-specific guard seam for `budget-exhausted`, `run_handoff` for the park and
`check_unit_deferred` for "every open item filed"; `read_build_specs` is extracted at the walk's second
reader.

`python tools/codebase-map/reuse_lookup.py "end a build whose rework budget is spent by a recorded ending and refuse another lap"`,
on the worktree at `179486e8f`, which holds no loop kit, ranked name-stem neighbours (`build_commit`,
`PolicyRefused`, the fixture builders); none ends a build, so no existing seam fits the rule itself,
and the seams above are where it attaches, found by reading the branch. `python
tools/memory-recall/query.py "what happens when a build runs out of rework budget" --terms "<the terms
below>"` returned unit 30's scout row, this spec's rev-3, `TOOL-dWellOiledMachine-59`'s call of
`endings.py derive` and the skeptic's B3-F9, which is unit 30's contention rule.

Recall terms used: rework budget flow.on-exhausted incomplete parked best-effort-ending descope owner-decision handoff halt-code disposition
