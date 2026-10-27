---
slug: dFurnishedOrders
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-21 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-43 TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-47 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-57 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61
spec-audit: 2026-10-21
parents: dBoundRoles
may: PLAY-dClosedLoop-3
---

# dFurnishedOrders — the Orders build of the dClosedLoop chain

## The problem this build exists to solve

dFurnishedOrders owns 13 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-roles-09,
gap-roles-10, gap-roles-12, gap-roles-13, gap-roles-15, gap-roles-16, gap-roles-17, gap-orient-15, gap-roles-21,
gap-roles-22, gap-roles-29, gap-conc-10, gap-mem-44. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 20 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 13 owned gaps above close.

## Detriments if this is not built

- Its 13 owned gaps stay open.
- Its 4 child builds wait on it: dMindYourWords, dScopedBuild, dShippedRelease, dTendedCadence.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dFurnishedOrders` green before the first pass; a moved instrument
  blob is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dFurnishedOrders`, a record per member "recorded by nobody", the same with `--write` (commit
  it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-18.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dFurnishedOrders-1` | `cl-dClosedLoop-0192@e52307f5` | the orientation scout composing the card in a sidechain at session start |
| 2 | `TOOL-dFurnishedOrders-2` | `cl-dClosedLoop-0193@a564937b` | prompt-writer calls batched by `prompts.batch` |
| 3 | `TOOL-dFurnishedOrders-3` | `cl-dClosedLoop-0194@48cbc488` | a return's harness notices persisted with it |
| 4 | `TOOL-dFurnishedOrders-4` | `cl-dClosedLoop-0195@d3ad9dda` | work-order fields an optional component or an expansion fills (the map's dossiers) declared as optional slots in their three states |
| 5 | `TOOL-dFurnishedOrders-5` | `cl-dClosedLoop-0196@f158a89c` | each role's trust profile and context temperature declared and rendered (`roles.trust` |
| 6 | `TOOL-dFurnishedOrders-6` | `cl-dClosedLoop-0197@ced122c4` | the answered-call hook (`roles.answered-calls`) |
| 7 | `TOOL-dFurnishedOrders-7` | `cl-dClosedLoop-0198@9197dfef` | repairs recorded in returns and filed as asks against the producer's record (`roles.on-contradiction`) |
| 8 | `TOOL-dFurnishedOrders-8` | `cl-dClosedLoop-0199@871337bc` | the role files' re-verification orders and protocol pointers replaced by rendered slices |
| 9 | `TOOL-dFurnishedOrders-9` | `cl-dClosedLoop-0200@89a5045e` | the role-by-step matrix derived from the item declarations and joined both ways |
| 10 | `TOOL-dFurnishedOrders-10` | `cl-dClosedLoop-0201@53144abb` | role metrics per role and item into the value ledger |
| 11 | `TOOL-dFurnishedOrders-11` | `cl-dClosedLoop-0202@504bb58f` | the work order's memory slices |
| 12 | `TOOL-dFurnishedOrders-12` | `cl-dClosedLoop-0203@325cbb22` | the work order's `map` slot for the roles `memory.project-map` names |
| 13 | `TOOL-dFurnishedOrders-13` | `cl-dClosedLoop-0204@34f664ed` | the orientation scout composing the card's map cell |
| 14 | `TOOL-dFurnishedOrders-14` | `cl-dClosedLoop-0205@5bbb1b2c` | the answered-call hook's range matching |
| 15 | `TOOL-dFurnishedOrders-15` | `cl-dClosedLoop-0206@e18404dd` | the tester agent |
| 16 | `TOOL-dFurnishedOrders-16` | `cl-dClosedLoop-0207@770af750` | owner questions asked live while the build is attended |
| 17 | `TOOL-dFurnishedOrders-17` | `cl-dClosedLoop-0208@b6c1dedb` | the `code` slot rendered per item from its declared seed: the seed's definitions with their ranges |
| 18 | `TOOL-dFurnishedOrders-18` | `cl-dClosedLoop-0209@97727c41` | the work order selecting instruction units by `feature.*` once dLinkedLibrary arms that selector |
| 19 | `TOOL-dFurnishedOrders-19` | `cl-dClosedLoop-0210@c44de500` | every role return declaring the rows it establishes (seams |
| 20 | `TOOL-dFurnishedOrders-20` | `cl-dClosedLoop-0211@6b17e1fe` | the problems whose subject intersects an item's seed handed in its work order as rows |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** DEFERRED · 60 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12
ids TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-21 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23
ids TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34
ids TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-43 TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-45
ids TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-47 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56
ids TOOL-dFurnishedOrders-57 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dFurnishedOrders-8 — the role files' protocol pointers and re-verification orders replaced by rendered slices](spec/2026-10-26-spec-TOOL-dFurnishedOrders-8.md) | 1 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-5 — each role's trust profile and context temperature declared and rendered](spec/2026-10-26-spec-TOOL-dFurnishedOrders-5.md) | 2 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-15 — the tester re-founded with its allowance, and the `probe` outcome on every role's return template](spec/2026-10-26-spec-TOOL-dFurnishedOrders-15.md) | 3 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-4 — the work order's optional slots in three states, and bug classes as a core field the spec names](spec/2026-10-26-spec-TOOL-dFurnishedOrders-4.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-1 — the orientation scout composing the card in a sidechain at session start, its recall re-verified once at entry and a moved-source record handed as stale](spec/2026-10-26-spec-TOOL-dFurnishedOrders-1.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-25 — the retired-argument upgrade steps scan an adopter's executable call sites only, never its records or its markdown, so `up` and `witness` pass on a tree whose history quotes the retired command](spec/2026-10-26-spec-TOOL-dFurnishedOrders-25.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-13 — the orientation scout composing the card's project-map cell, placed and shape-checked at the append, not installed until the map renderer lands](spec/2026-10-26-spec-TOOL-dFurnishedOrders-13.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-35 — the call-site scan's kit files defined on every target kind: gov's own kit source, a receipt, or the directories a `kit.toml` homes, so gov's own update walk passes](spec/2026-10-26-spec-TOOL-dFurnishedOrders-35.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-36 — the kits' own suites out of the call-site scan on every target: a `project-owned` file or a `*.test.sh` under a kit home spells the retired keys on purpose and is never an adopter's call site](spec/2026-10-26-spec-TOOL-dFurnishedOrders-36.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-3 — a return's harness notices persisted with it, as runlog `notice` events and on the agent ledger's returned line, by `notices.record`](spec/2026-10-26-spec-TOOL-dFurnishedOrders-3.md) | 7 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-40 — a receipt target's kit home is the kit's declared home under the target's prefix, never the directory of a receipt row, so a merged or seed row at the repo root widens nothing](spec/2026-10-27-spec-TOOL-dFurnishedOrders-40.md) | 7 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-19 — every role return declaring the rows it establishes, and each work order's return schema rendered from its own rows, so a dropped, invented or doubled row fails the return and is retried](spec/2026-10-26-spec-TOOL-dFurnishedOrders-19.md) | 8 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-43 — a receipt target's kit homes are the directories `apply` lands each kit's home at, derived through the entry's own destination rules, never a formula beside them](spec/2026-10-27-spec-TOOL-dFurnishedOrders-43.md) | 8 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-44 — the step's receipt homes held to the receipt `apply` writes: one govkit selftest arm applies every shipped kit to a scratch target with a per-kit override and compares both ways](spec/2026-10-27-spec-TOOL-dFurnishedOrders-44.md) | 8 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-24 — each work order's return schema rendered as one branch per outcome, the template's and each arm's, so a valid refused or probe return passes and a malformed one fails on its own fields](spec/2026-10-26-spec-TOOL-dFurnishedOrders-24.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-47 — unit 44's parity arm grades the receipt `apply` finishes: an adopter or render problem outside home parity is named and tolerated, and a refusal before the final receipt still fails the arm](spec/2026-10-27-spec-TOOL-dFurnishedOrders-47.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-7 — a false handed fact repaired in the return and filed as an ask against its producer's record, routed by `roles.on-contradiction` through the refusal outcome table](spec/2026-10-26-spec-TOOL-dFurnishedOrders-7.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-14 — the answered-call hook's range matching, the excerpt keys it matches and a repair's carry, designed as RC-7 asks](spec/2026-10-26-spec-TOOL-dFurnishedOrders-14.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-31 — a field table is no outcome arm: `derive_return_arms` yields only tables carrying `outcome`, so every branch of the per-order schema names an outcome from the step unit 24 builds at](spec/2026-10-26-spec-TOOL-dFurnishedOrders-31.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-6 — the answered-call hook: a role agent's call its work order already answers refused, warned or recorded by `roles.answered-calls`, a verifier's read of its subject exempt, and each hook failure recorded](spec/2026-10-26-spec-TOOL-dFurnishedOrders-6.md) | 11 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-22 — a verifier's subject declared as the input slots it reads, `subject-reads`, checked against `reads` and `verifies` and written into the role index](spec/2026-10-26-spec-TOOL-dFurnishedOrders-22.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-23 — the answered-call hook's verifier exemption keyed on `subject-reads`, and certified on every verifier the shipped role index holds, never on a planted block name](spec/2026-10-26-spec-TOOL-dFurnishedOrders-23.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-9 — the role-by-step matrix derived from the item declarations, joined both ways, and rendered to each role as its own row](spec/2026-10-26-spec-TOOL-dFurnishedOrders-9.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-10 — role metrics per role and item, classed by runlog's extractor and kept in this build's metrics file](spec/2026-10-26-spec-TOOL-dFurnishedOrders-10.md) | 13 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-32 — a reviewer's subject read from the roster present at the pass: the merged reviewer's subject is the first slot of a `subject-reads` group its work order hands, so its criterion stays non-exempt](spec/2026-10-26-spec-TOOL-dFurnishedOrders-32.md) | 13 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-11 — the work order's memory, code-notes, legacy and house-index slots, each under its own budget and its own answer](spec/2026-10-26-spec-TOOL-dFurnishedOrders-11.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-12 — the work order's `map` slot for the roles `memory.project-map` names, with each item's unfolds](spec/2026-10-26-spec-TOOL-dFurnishedOrders-12.md) | 15 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-17 — the `code` slot rendered per item from its declared seed, as ranges under `memory.code-budget`](spec/2026-10-26-spec-TOOL-dFurnishedOrders-17.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-20 — the problems whose subject meets an item's seed, read from the register when the order is cut and handed as rows](spec/2026-10-26-spec-TOOL-dFurnishedOrders-20.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-18 — the work order selecting instruction units by `feature.*`, and its code-notes slot filled from the tag's bundle as `annotations.delivery` says](spec/2026-10-26-spec-TOOL-dFurnishedOrders-18.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-2 — prompt-writer calls batched by `prompts.batch`: one call frames a step's tasks of one role, split per task at render](spec/2026-10-26-spec-TOOL-dFurnishedOrders-2.md) | 19 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-16 — owner questions asked live while the build is attended, never decided at raise, and a late answer placed as an amendment that re-enters its item](spec/2026-10-26-spec-TOOL-dFurnishedOrders-16.md) | 20 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-26 — presence read inside a run's window: `derive_attended` counts only owner turns after the run started, so the prompt that launched an unattended run never reads as the owner attending](spec/2026-10-26-spec-TOOL-dFurnishedOrders-26.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-27 — every owner question the driver raises carries the run's window: `--dispatch` and `--phase` ask the door through one helper that hands it the run's session and lease start](spec/2026-10-26-spec-TOOL-dFurnishedOrders-27.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-28 — an unreadable presence inside a run's window reads away, so no owner question of an unattended run is held for an owner nobody can show is there](spec/2026-10-26-spec-TOOL-dFurnishedOrders-28.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dFurnishedOrders-29 — the round-1 audit's 35 roles, hooks and runlog minors: one reader per value, bounded slot readers, the verifier hooks' failure paths and registries, and fixtures that read only what they plant](spec/2026-10-26-spec-TOOL-dFurnishedOrders-29.md) | 22 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-30 — the round-1 audit's 16 workflows, unattended, kickoff and memory-tree minors: retired keys refused and observed, every cold carrier named, the card's map cell given a failure state, and the harness's rows checked in-script](spec/2026-10-26-spec-TOOL-dFurnishedOrders-30.md) | 22 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-33 — an unreadable posture inside a run's window reads away unless an owner turn after the run's start shows the owner there, so the stall an unread posture holds is closed](spec/2026-10-26-spec-TOOL-dFurnishedOrders-33.md) | 22 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-34 — the posture read's failures named and bounded: a `breakpoints.py list` that fails, hangs or prints no `attendance —` line, and a policy read that fails, each an unreadable posture with its cause](spec/2026-10-26-spec-TOOL-dFurnishedOrders-34.md) | 22 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-37 — the second spec audit's 37 minors: readers that tell a missing input from an empty one, one bounded runner, the retired-key scan's shapes and conf, the card's map cell bounded and never re-derived, and criteria that read what they claim](spec/2026-10-26-spec-TOOL-dFurnishedOrders-37.md) | 23 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-38 — the per-pass line's absence arms graded on their content: a named `miss` helper, and a probe whose red pattern reads each arm's text, never git grep's prefixed line](spec/2026-10-27-spec-TOOL-dFurnishedOrders-38.md) | 24 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-39 — the roles kit's one bounded runner writes its child's output to files, never a pipe, so a descendant holding stdout cannot outlive the bound, from one canonical block the run-gates kit already proves](spec/2026-10-27-spec-TOOL-dFurnishedOrders-39.md) | 24 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-41 — the third spec audit's 12 upgrade-step minors: the walk run on the repository root, kit source narrowed to kit homes, kit homes matched to gov's descriptors, `project-owned` suites derived and mapped, and a scan that skips links and caps a read](spec/2026-10-27-spec-TOOL-dFurnishedOrders-41.md) | 25 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-42 — the third spec audit's 19 roles, runlog, hooks, unattended and kickoff minors: criteria that read what they claim, one output for an empty transcript, imports gated as a class, the posture read decoded and bounded, and a runner bound a suite can lower](spec/2026-10-27-spec-TOOL-dFurnishedOrders-42.md) | 25 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-45 — the fourth spec audit's 8 upgrade-step minors: a copied kit.toml matched on its own `home`, a top level compared as a file, every git child stripped of the leaking variables, live fixtures, one tool-root search and a deploy descriptor refused by name](spec/2026-10-27-spec-TOOL-dFurnishedOrders-45.md) | 26 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-46 — the fourth spec audit's 18 roles, run-gates, process-monitor, unattended and kickoff minors: one re-stamp last, one bounded runner that carries its imports and kills on any exception, criteria that read the real gate, and the guards and pins the new arms move](spec/2026-10-27-spec-TOOL-dFurnishedOrders-46.md) | 26 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-48 — the fifth spec audit's 26 govkit, parity-arm, guard and ratchet minors: the ratchet's own predicate and a landing re-stamp, two tool-root answers, one environment strip, isolated DEAD PROBE clauses, a guard derived from the registry, homes from the receipt, and a deploy descriptor refused at its boundary](spec/2026-10-27-spec-TOOL-dFurnishedOrders-48.md) | 27 | 2 | DEFERRED | rev-4 | 2026-10-27 |
| [TOOL-dFurnishedOrders-49 — the fifth spec audit's 6 roles-suite, budget and write-set minors: a disjointness read from what units 45 and 46 wrote, a budget re-pinned from every worktree's readings by an expression, and an interrupt probe that waits for its child](spec/2026-10-27-spec-TOOL-dFurnishedOrders-49.md) | 27 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-50 — unit 48's `govkit selftest` home rows priced in the guards join: a home only where `apply` runs or renders from it, no guard pushed into the broad set, and every live spec the rows reach carrying the leg or a waived, asked row](spec/2026-10-27-spec-TOOL-dFurnishedOrders-50.md) | 28 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-51 — unit 49's interrupt probe reads the pid its kill path targets: a Python stub writing `os.getpid()`, that pid read live before the interrupt in the kill's own namespace, and a no-op tree kill that reds the arm](spec/2026-10-27-spec-TOOL-dFurnishedOrders-51.md) | 28 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-52 — the sixth spec audit's 26 minors: a `govkit selftest` row priced for unit 48's runs, the ratchet observed through C5, apply's problems read by their total, one receipt needle, gov's one trip rule, live fixtures, every path token refused, a roles reading any directory reproduces, an interrupt that grades the whole kill, and ledger reads that survive a wrap](spec/2026-10-27-spec-TOOL-dFurnishedOrders-52.md) | 29 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-57 — unit 50's reach read from the spec-token checker itself: the `govkit selftest <- ` tokens its `[guards]` rows print over the whole resolved guard, and every waiver row keyed to one of them](spec/2026-10-27-spec-TOOL-dFurnishedOrders-57.md) | 29 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-53 — the guard arm's covered rule is one-way for a required directory: each required path meets the trip rule without its trailing slash, so a home's own `kit.toml` row never covers the home](spec/2026-10-27-spec-TOOL-dFurnishedOrders-53.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-54 — the guard arm's trip answer is computed over the `legs` it is handed: the spec-token checker's own per-path join, loaded by path and run in process, so a scratch manifest is the manifest graded](spec/2026-10-27-spec-TOOL-dFurnishedOrders-54.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-55 — the guard arm's glob rows read from the `legs` it is handed: each `govkit selftest` row carrying the checker's `GLOB_MAGIC` printed as unevaluated, never as covering, missing or dropped](spec/2026-10-27-spec-TOOL-dFurnishedOrders-55.md) | 30 | 2 | DEFERRED | rev-1 | 2026-10-27 |
| [TOOL-dFurnishedOrders-56 — the guard arm returns the row that covered each required path, so a criterion over a scratch manifest proves the copy's own spelling was graded and reds when another manifest was read](spec/2026-10-27-spec-TOOL-dFurnishedOrders-56.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-58 — the seventh spec audit's 27 minors: an interrupt probe whose every branch has a fixture and whose kill spares a reused pid, budget and roles readings that count only what ran, criteria that read the ledgers they claim, guard rows that land with their reach, every deploy table refused by shape, and one receipt needle](spec/2026-10-27-spec-TOOL-dFurnishedOrders-58.md) | 31 | 2 | DEFERRED | rev-3 | 2026-10-27 |
| [TOOL-dFurnishedOrders-59 — unit 53's one-way case planted: the guard fixture holds a `kit.toml` row below the home it drops, asserts the old rule would read that home covered, and shows the arm graded the planted row](spec/2026-10-27-spec-TOOL-dFurnishedOrders-59.md) | 31 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-60 — the eighth spec audit's 24 minors: a guard arm that grades the population it claims and names every checker failure, a reach read on the checker's own separators, waiver rows that name what they waive, one pass predicate, an interrupt cleanup on the held child, every deploy key refused by shape, and criteria that read the line they claim](spec/2026-10-27-spec-TOOL-dFurnishedOrders-60.md) | 32 | 2 | DEFERRED | rev-2 | 2026-10-27 |
| [TOOL-dFurnishedOrders-61 — the ninth spec audit's 27 minors: a reach and a landing rule read over the population and range they claim, one frozen parse compared, a guard fixture graded through the trip rule's own object, a registry-less root named, an empty prefix documented as `tools`, and every deploy key and row field refused at one check](spec/2026-10-27-spec-TOOL-dFurnishedOrders-61.md) | 33 | 2 | DEFERRED | rev-1 | 2026-10-27 |
<!-- /gen:build-units -->

Records: 94 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dFurnishedOrders-61.

Ids whose spec moved past its audited revision: TOOL-dFurnishedOrders-1@rev-1 TOOL-dFurnishedOrders-10@rev-1 TOOL-dFurnishedOrders-11@rev-1 TOOL-dFurnishedOrders-12@rev-1 TOOL-dFurnishedOrders-13@rev-1 TOOL-dFurnishedOrders-14@rev-1 TOOL-dFurnishedOrders-15@rev-1 TOOL-dFurnishedOrders-16@rev-1
TOOL-dFurnishedOrders-17@rev-1 TOOL-dFurnishedOrders-18@rev-1 TOOL-dFurnishedOrders-19@rev-1 TOOL-dFurnishedOrders-2@rev-1 TOOL-dFurnishedOrders-20@rev-1 TOOL-dFurnishedOrders-22@rev-1 TOOL-dFurnishedOrders-23@rev-1 TOOL-dFurnishedOrders-24@rev-1 TOOL-dFurnishedOrders-25@rev-1
TOOL-dFurnishedOrders-26@rev-1 TOOL-dFurnishedOrders-27@rev-1 TOOL-dFurnishedOrders-28@rev-1 TOOL-dFurnishedOrders-29@rev-1 TOOL-dFurnishedOrders-3@rev-1 TOOL-dFurnishedOrders-30@rev-1 TOOL-dFurnishedOrders-31@rev-1 TOOL-dFurnishedOrders-32@rev-1 TOOL-dFurnishedOrders-34@rev-1
TOOL-dFurnishedOrders-35@rev-1 TOOL-dFurnishedOrders-36@rev-1 TOOL-dFurnishedOrders-37@rev-1 TOOL-dFurnishedOrders-4@rev-1 TOOL-dFurnishedOrders-5@rev-1 TOOL-dFurnishedOrders-6@rev-1 TOOL-dFurnishedOrders-7@rev-1 TOOL-dFurnishedOrders-8@rev-1 TOOL-dFurnishedOrders-9@rev-1
TOOL-dFurnishedOrders-38@rev-1 TOOL-dFurnishedOrders-39@rev-1 TOOL-dFurnishedOrders-40@rev-1 TOOL-dFurnishedOrders-41@rev-1 TOOL-dFurnishedOrders-42@rev-1 TOOL-dFurnishedOrders-43@rev-1 TOOL-dFurnishedOrders-44@rev-1 TOOL-dFurnishedOrders-45@rev-1 TOOL-dFurnishedOrders-46@rev-1
TOOL-dFurnishedOrders-47@rev-1 TOOL-dFurnishedOrders-48@rev-1 TOOL-dFurnishedOrders-49@rev-1 TOOL-dFurnishedOrders-50@rev-1 TOOL-dFurnishedOrders-51@rev-1 TOOL-dFurnishedOrders-52@rev-1 TOOL-dFurnishedOrders-53@rev-1 TOOL-dFurnishedOrders-54@rev-1 TOOL-dFurnishedOrders-56@rev-1
TOOL-dFurnishedOrders-57@rev-1 TOOL-dFurnishedOrders-58@rev-1 TOOL-dFurnishedOrders-59@rev-1 TOOL-dFurnishedOrders-60@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dFurnishedOrders's 20 clause(s) and 14 owned node(s), over 60 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 20
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-26-spec-TOOL-dFurnishedOrders-22.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-23.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-24.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dFurnishedOrders-25.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-26.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-27.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-28.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dFurnishedOrders-29.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-30.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-31.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-32.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dFurnishedOrders-33.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-34.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-35.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dFurnishedOrders-36.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dFurnishedOrders-37.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-39.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-40.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dFurnishedOrders-41.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-43.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-44.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dFurnishedOrders-45.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-47.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-48.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dFurnishedOrders-49.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-51.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-52.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dFurnishedOrders-53.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-55.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-56.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dFurnishedOrders-57.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-58.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-59.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dFurnishedOrders-60.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-27-spec-TOOL-dFurnishedOrders-61.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0192, cl-dClosedLoop-0195, cl-dClosedLoop-0200, cl-dClosedLoop-0204, cl-dClosedLoop-0205, cl-dClosedLoop-0211
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dFurnishedOrders-8` | no |
| 2 | `TOOL-dFurnishedOrders-5` | no |
| 3 | `TOOL-dFurnishedOrders-15` | no |
| 4 | `TOOL-dFurnishedOrders-4` | no |
| 5 | `TOOL-dFurnishedOrders-1`, `TOOL-dFurnishedOrders-25` | yes |
| 6 | `TOOL-dFurnishedOrders-13`, `TOOL-dFurnishedOrders-35`, `TOOL-dFurnishedOrders-36` | no |
| 7 | `TOOL-dFurnishedOrders-3`, `TOOL-dFurnishedOrders-40` | yes |
| 8 | `TOOL-dFurnishedOrders-19`, `TOOL-dFurnishedOrders-43`, `TOOL-dFurnishedOrders-44` | no |
| 9 | `TOOL-dFurnishedOrders-24`, `TOOL-dFurnishedOrders-47`, `TOOL-dFurnishedOrders-7` | no |
| 10 | `TOOL-dFurnishedOrders-14`, `TOOL-dFurnishedOrders-31` | no |
| 11 | `TOOL-dFurnishedOrders-6` | no |
| 12 | `TOOL-dFurnishedOrders-22`, `TOOL-dFurnishedOrders-23`, `TOOL-dFurnishedOrders-9` | no |
| 13 | `TOOL-dFurnishedOrders-10`, `TOOL-dFurnishedOrders-32` | no |
| 14 | `TOOL-dFurnishedOrders-11` | no |
| 15 | `TOOL-dFurnishedOrders-12` | no |
| 16 | `TOOL-dFurnishedOrders-17` | no |
| 17 | `TOOL-dFurnishedOrders-20` | no |
| 18 | `TOOL-dFurnishedOrders-18` | no |
| 19 | `TOOL-dFurnishedOrders-2` | no |
| 20 | `TOOL-dFurnishedOrders-16` | no |
| 21 | `TOOL-dFurnishedOrders-26`, `TOOL-dFurnishedOrders-27`, `TOOL-dFurnishedOrders-28` | no |
| 22 | `TOOL-dFurnishedOrders-29`, `TOOL-dFurnishedOrders-30`, `TOOL-dFurnishedOrders-33`, `TOOL-dFurnishedOrders-34` | no |
| 23 | `TOOL-dFurnishedOrders-37` | no |
| 24 | `TOOL-dFurnishedOrders-38`, `TOOL-dFurnishedOrders-39` | yes |
| 25 | `TOOL-dFurnishedOrders-41`, `TOOL-dFurnishedOrders-42` | yes |
| 26 | `TOOL-dFurnishedOrders-45`, `TOOL-dFurnishedOrders-46` | yes |
| 27 | `TOOL-dFurnishedOrders-48`, `TOOL-dFurnishedOrders-49` | yes |
| 28 | `TOOL-dFurnishedOrders-50`, `TOOL-dFurnishedOrders-51` | yes |
| 29 | `TOOL-dFurnishedOrders-52`, `TOOL-dFurnishedOrders-57` | yes |
| 30 | `TOOL-dFurnishedOrders-53`, `TOOL-dFurnishedOrders-54`, `TOOL-dFurnishedOrders-55`, `TOOL-dFurnishedOrders-56` | no |
| 31 | `TOOL-dFurnishedOrders-58`, `TOOL-dFurnishedOrders-59` | no |
| 32 | `TOOL-dFurnishedOrders-60` | no |
| 33 | `TOOL-dFurnishedOrders-61` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md)
- **Child builds:** [dMindYourWords](../dMindYourWords/README.md), [dScopedBuild](../dScopedBuild/README.md), [dShippedRelease](../dShippedRelease/README.md), [dTendedCadence](../dTendedCadence/README.md)
<!-- /gen:build-edges -->
