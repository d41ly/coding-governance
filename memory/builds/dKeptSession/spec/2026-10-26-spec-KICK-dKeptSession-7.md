# KICK-dKeptSession-7 — dependency coordination: `deps.coordination` switching the dependency gate by the parent's lease, `deps.early-build` admitting Build, and the `confirmed`, `changed` and `landed` notices

**Status:** DEFERRED · rev-7 · 2026-11-22 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 24 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0145@b38efe3e whole
**Carries:** node:policy-key.deps.coordination
**Carries:** node:policy-key.deps.early-build

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-26 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-7-deviation-71.md](../build/2026-10-26-build-KICK-dKeptSession-7-deviation-71.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-7-deviation-72.md](../build/2026-10-26-build-KICK-dKeptSession-7-deviation-72.md) | deviation | — |
| [2026-11-05-build-KICK-dKeptSession-7-deviation-73.md](../build/2026-11-05-build-KICK-dKeptSession-7-deviation-73.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-5 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-25 KICK-dKeptSession-36 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-7-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-7-1-spec-writer.md) | journal | — |
| [2026-11-05-prompt-KICK-dKeptSession-1-owner-forks.md](../prompts/2026-11-05-prompt-KICK-dKeptSession-1-owner-forks.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-9 KICK-dKeptSession-20 KICK-dKeptSession-25 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md) | research | KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-26 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-35 KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 |
| [2026-11-21-prompt-KICK-dKeptSession-6-orders-23-24-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-6-orders-23-24-reground-brief.md) | research | KICK-dKeptSession-6 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

A dependent build coordinates with the builds its `parents:` names before it waits on them: a parent
is reachable while its build lease is live; at Design's exit a build posts its frozen interfaces to
each dependent as `confirmed`; a dependent's units enter Build once those interfaces are confirmed, as
`deps.early-build` admits; a later change posts `changed` and the landing posts `landed`; and a
dependent whose parent is unreachable enters Build only after the parent lands, as
`deps.coordination` says (coordination item 8, FI-2, FI-5). Each key is seen on strict's value,
`wait-for-landing` and `design-only` (the whole-design audit's C2-F11). At base the landed position
engine answers `blocked` on any `parents:` build not landed, whatever its step and reach
(`tools/loop/position.py#derive_answer`), so strict and standard behave alike and no build reaches
another (gap-flow-06).

## 2. Scope (IN)

- **S1** — Reachability, `derive_parent_reach(root, parent)` in `tools/loop/position.py`: `landed`
  where the engine's landed test holds, the hand-over's `LANDED` or the parent's newest move entering
  `landed` (`tools/loop/position.py#derive_position_into`); else `reachable` where the driver's one-lease
  read `--lease status build <parent>` (`tools/unattended/unattended.sh#print_lease_status`) prints a row
  whose verdict, field 5, is `live` or `held`; else `unreachable`, for every other verdict,
  `lease — none`, `lease — off`, a non-zero exit, no bash and a read past the bound. The read runs
  through §4 "The driver launch", never by parsing a lease ref here. There is no other timeout
  (coordination `[interpretations]` 1). Observed by AC1, AC2, AC3 and AC6.
- **S2** — `deps.coordination` (`message-then-progress`, `wait-for-landing`, `order-only`; default
  `message-then-progress`) switches the engine's dependency gate per parent not `landed`, by
  `derive_dependency_hold(coordination, early_build, reach, confirmed)`, which answers the cause of
  §4's table. Each such parent's interrupt, built in `derive_interrupts`
  (`tools/loop/position.py#derive_interrupts`), prints
  `interrupt — dependency · <parent> · <reach> · <cause> (deps.coordination: <value>)`. `derive_answer`
  answers `blocked`, at the rung its landed `blocked` holds, only where a cause is `not landed`,
  `unreachable` or `awaiting confirmed` and the build's step is `step.build` or a later step by
  `[[step]]` `order` (`tools/loop/loop.toml`); its reason is the interrupt's text after
  `interrupt — `. A Design item runs under every value (§8 F1). Observed by AC1, AC2 and AC3.
- **S3** — `deps.early-build` (`confirmed-interfaces`, `design-only`, `anything-coordinated`; default
  `confirmed-interfaces`), read for a `reachable` parent under `message-then-progress`.
  `confirmed-interfaces`: the cause is `confirmed` once `KICK-dKeptSession-27` S5's
  `check_interface_notice <slug> "interfaces <parent>" <file>`, run through §4 "The driver launch",
  exits 0, a `confirmed` or `changed` row from the parent whose `content-key` equals the key recomputed
  over `<file>`, never chosen by arrival order; else `awaiting confirmed`. `<file>` is
  `derive_interface_listing(root, parent, w)` written to a scratch file (S4), `w` the parent lease's
  `witness`, read by `--lease show build <parent>` (S7) and fetched by one `git fetch <remote>`
  (`tools/loop/claims.py#resolve_remote`) where this clone lacks it. A witness of `-`, a commit still
  absent, or a listing that cannot be derived holds as `awaiting confirmed`. `design-only`: the cause
  is `not landed`. `anything-coordinated`: the cause is `coordinated`. Every unit of the dependent
  counts as consuming the parent's interfaces (§8 F2). Observed by AC4, AC5 and AC6.
- **S4** — The `confirmed` notice at Design's exit. `derive_interface_listing(root, build, commit)` in
  `tools/loop/loop_transition.py` is the bytes `git ls-tree -r <commit> -- <memory
  root>/builds/<build>/spec/` prints, the one listing S3 and this item key. `write_transition`
  (`tools/loop/loop_transition.py#write_transition`), on a move from `designing` to `building`, calls
  `write_dependency_notices(root, build, commit)` after its commit, its lines joining `said` beside
  `write_card_follow`'s (`tools/loop/loop_transition.py#write_card_follow`); it never raises, and the
  move stands whatever it prints. Per dependent of `read_dependents(root, build)` (S9) it posts
  `--mail post <build> --to build:<dependent> --kind <kind> --subject "interfaces <build>"
  --interface <listing file> <body file>` (`KICK-dKeptSession-5` S5, `KICK-dKeptSession-27` S3), the
  listing at `commit`, the body the commit's full sha, launched as `KICK-dKeptSession-5` S9's
  `read_mail_rows` launches the driver. `<kind>` is `changed` where `read_mail_rows(root, dependent)`
  holds a `confirmed` row from `build` with that subject, else `confirmed`. `commit` is the transition
  commit, the one the driver next passes as the lease's `witness`
  (`tools/unattended/unattended.sh#read_transition_witness`, §8 F3); where `transitions.record`
  selects `micro-format` alone the writer makes no commit and nothing records a transition
  (`tools/unattended/unattended.sh#check_lease_transition`), so the listing is taken at `HEAD` and the
  dependent holds as `awaiting confirmed`. A post that fails appends its own lines and fails nothing.
  Observed by AC7.
- **S5** — The `landed` notice. `verb_landed` (`tools/unattended/unattended.sh#verb_landed`), at each
  of its two success exits, posts one message per dependent: kind `landed`, to `build:<dependent>`,
  subject `landing <slug>`, its body the landed sha, `DP_LANDING` on the in-place exit and `head` on
  the recorded one. The dependents are `run_loop_verb loop_transition.py dependents --build=<slug>`'s
  lines (`tools/unattended/unattended.sh#run_loop_verb`, S9), and each post runs as
  `( main --mail post … )` in a subshell. A post that fails, or a loop kit that does not resolve,
  prints its line and never changes the verb's exit. Observed by AC8.
- **S6** — The keys, each read by `read_policy_kit()` (`tools/loop/loop_parents.py#read_policy_kit`)
  and its `resolve(<key>, <root>)` at the landed revision, as
  `tools/loop/placement.py#read_placement_policy` reads its keys, each spelled whole. A `Refusal`, or
  the `LookupError` of no policy kit, reads the catalogue default and prints one
  `position: NOTE · <key> reads <default>: <why>` line. A policy file naming `preset = "strict"` with
  no override reads `wait-for-landing` and `design-only`, strict's cells in I1
  (`tools/policy/presets.toml`, `KICK-dKeptSession-1`), through `KICK-dKeptSession-2`'s preset step,
  source `preset`. Observed by AC9.
- **S7** — The witness read (§8 F5, F7): `--lease show build <slug>`, dispatched beside `--lease status`
  in the driver's `--lease` branch, runs `print_lease_witness <slug>`: one `read_claims quiet` and the
  slug's build row's `witness`, field 15 of `CLAIM_ROWS` (`tools/unattended/unattended.sh#read_claims`),
  printed alone, or `-` where the row holds none or no lease exists; `lease — off · <slug>/build` with
  `RUN_CLAIMS` off, exit 0; `lease not written — <why>`, exit 2, where the read does not answer. It
  writes nothing. Its usage-header row joins the `#   unattended.sh --lease …` rows. Observed by AC11.
- **S8** — The documentation. `help/loop.md` gains `## Coordinating with a parent build` after
  `## Where a build is, and what runs next`: the gate's values, the reach words, the causes and the
  three notices, and that section's sentence on a `parents:` build answering `blocked` points to it.
  Its `--lease` paragraph under `## Claim keys` names `--lease show build <slug>`, its anchor
  re-stamped with the fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints. Observed by
  AC10.
- **S9** — The dependents. `read_dependents(root, build)` in `tools/loop/loop_transition.py`: every
  build whose README front matter's `parents:` names `build`, read by the memory-tree kit's
  `parse_front_matter` as `tools/loop/loop_parents.py#read_withdrawn_parents` reads it, sorted.
  `python loop_transition.py dependents --build <slug>` prints them one per line, exit 0, and
  `loop: unanswered · <why>`, exit 2, for an unreadable README. Observed by AC7 and AC8.
- **S10** — The budget rows. The seven `deps-*` plants move the `plants=<n>` token of the `loop
  position fixtures` row and `deps-notices` that of the `loop transition record` row in
  `tools/run-gates/selftest-budgets.txt`, each re-priced as §4's budget rows state. Observed by AC12.

## 3. Non-goals (OUT)

- No re-entry on `changed`: the cross-build interface-change re-entry is dIndexedDesign's
  `design.reentry`, which a `changed` message triggers
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md@4a13cbc82a99:143`).
- No landing order and no held landing: `landing.order` and `deps.landing` are dShippedRelease's.
- No `deps.on-parent-withdrawn`: dDeclaredLoop's.
- No lease write and no verdict: this unit reads `--lease status` and adds the read-only
  `--lease show` (S7).
- No mailbox, kind or post path: `KICK-dKeptSession-5`'s; no content key or supersession rule:
  `KICK-dKeptSession-27`'s.
- No automatic answer to a dependent's `confirm-request` (§8 F6).
- No per-unit interface declaration (§8 F2).
- No catalogue rows: both keys' rows are landed in `tools/policy/catalogue.toml`, owner dKeptSession.

### Edges

- **consumes-from** `KICK-dKeptSession-1` — `presets.toml`, whose strict cells `wait-for-landing` and `design-only` each key is seen on, read through the reader's preset step
- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox` and the `--mail post` writer, through which the notices are posted and the confirmations read
- **consumes-from** `KICK-dKeptSession-27` — `content-key`, its `--interface` option and `check_interface_notice`, the recomputed key that decides which confirmation is current, never arrival order
- **consumes-from** external — dDeclaredLoop, landed: the position engine's dependency gate and answer precedence, and `write_transition`; dPlacedRequest, landed: the build lease, `--lease status` and `CLAIM_ROWS`' `witness`; dGroundRules' `resolve`
- **hands-off** external — dIndexedDesign's `design.reentry` re-enters a dependent's consuming units on a `changed` message
- **hands-off** `KICK-dKeptSession-35` — `write_dependency_notices` and `verb_landed`'s notice, which that unit gives a pass and a visible refusal line (id 4)
- **hands-off** `KICK-dKeptSession-42` — the notices and S3's listing, which that unit's transition writer reads to acknowledge what the dependent consumed (id 55)
- **hands-off** `KICK-dKeptSession-44` — `derive_parent_reach`, the listing's bytes and `read_dependents`, the batch's S17 and S20 (ids 24, 35)

## 4. Design

### Evidence

- Coordination item 8
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md@4a13cbc82a99:130`)
  and its interpretations 1 and 2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md@4a13cbc82a99:187`): reachable while the build
  lease is live, no separate timeout; Design's exit posts the frozen interfaces, which is how a frozen
  design confirms them.
- FI-2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md@6f6b55dd620d:78`):
  "progress to the best of their ability, otherwise build waits for parent's landing (if they cannot
  communicate)". FI-5 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md@6f6b55dd620d:109`) and its settled text
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md@6f6b55dd620d:127`): a dependent designs at any time and enters Build once
  the interfaces it consumes are confirmed.
- v2 gives the values and defaults
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1165`,
  `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1166`); strict sets `wait-for-landing` and `design-only`
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1490`, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1491`). The clause
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1771`) names interfaces confirmed at Design's exit, and no
  answer to a `confirm-request`.
- The landed gate: `derive_position_into` lists each `parents:` build neither `LANDED` in the hand-over
  nor recorded as entering `landed`, `derive_interrupts` makes each a `dependency` interrupt, and
  `derive_answer` answers `blocked` on any, after an owner decision and before `act`.
- `--lease status` is the driver's one-lease read, kept for a reader that must not parse `--claims`
  (`tools/unattended/unattended.sh#print_lease_status`); `placement.py` reads it through the sourced
  driver (`tools/loop/placement.py#read_build_lease`). No verb prints a lease's `witness`: `--claims`
  cuts to fields 1 to 5 (`tools/unattended/unattended.sh#print_claims`), and `--lease status` prints six
  fields without it. `git grep -n 'lease show' -- tools memory/builds/dPlacedRequest` finds nothing at
  base c2a407b0: the ask F5 names was never filed.
- A lease's `witness` is a transition commit or, for a waiting question, a mail commit
  (`tools/unattended/unattended.sh#check_lease_witness`).
- `write_transition` commits the move, then runs the card follow, which never raises; with neither
  `trailer` nor `log` selected it writes no commit.
- The loop kit reads policy through `read_policy_kit`, and already imports it in `position.py`.

### The gate, per parent not landed

| `deps.coordination` | reach | `deps.early-build` | cause | Build items |
|---|---|---|---|---|
| `wait-for-landing` | any | not read | `not landed` | held |
| `message-then-progress` | `unreachable` | not read | `unreachable` | held |
| `message-then-progress` | `reachable` | `confirmed-interfaces` | `confirmed`, or `awaiting confirmed` | run, or held |
| `message-then-progress` | `reachable` | `design-only` | `not landed` | held |
| `message-then-progress` | `reachable` | `anything-coordinated` | `coordinated` | run |
| `order-only` | any | not read | `order only` | run |

Design items run in every row; the engine's precedence is otherwise untouched.

### The driver launch

Each read of the driver's state is one sourced driver, spelled as `KICK-dKeptSession-42` §4 "The
check's launch" spells it, minted once as `run_driver_sourced(root, call, *args)` in
`tools/loop/loop_transition.py`, the bash `resolve_bash(<driver>)`
(`tools/loop/loop_witness.py#resolve_bash`), the driver `resolve_kit_dir("unattended", "unattended.sh",
KIT) / "unattended.sh"` (`tools/loop/loop_lib.py#resolve_kit_dir`), stdin closed, `read_clean_env()`
and the bound `MAIL_GUARD_SECONDS` (`KICK-dKeptSession-5` S9):

```
[<bash>, "-c", '. "$1" && load_driver_conf && check_interface_notice "$2" "$3" "$4"',
 "check_interface_notice", <driver>, <slug>, "interfaces <parent>", <listing file>]
[<bash>, "-c", '. "$1" && load_driver_conf && main --lease status build "$2"', "main", <driver>, <parent>]
[<bash>, "-c", '. "$1" && load_driver_conf && main --lease show build "$2"', "main", <driver>, <parent>]
```

### The notices

```
confirmed · to build:<dependent> · subject interfaces <slug> · content-key <12 hex>   first Design exit
changed   · to build:<dependent> · subject interfaces <slug> · content-key <12 hex>   every later Design exit
landed    · to build:<dependent> · subject landing <slug>    · body <landed sha>       verb_landed's success
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_parent_reach`, `derive_dependency_hold` | Python functions, `tools/loop/position.py` | `py.function`, OK by `lexicon.py --suggest` |
| `derive_interface_listing`, `write_dependency_notices`, `read_dependents`, `run_driver_sourced` | Python functions, `tools/loop/loop_transition.py` | `py.function`, verb-first |
| `dependents` | `loop_transition.py` verb | none |
| `--lease show`, `print_lease_witness` | driver act; shell function | `sh.function`, OK by `lexicon.py --suggest` |
| `landed`, `reachable`, `unreachable`; the six causes | words on the engine's lines | none |
| `deps-wait`, `deps-unreachable`, `deps-order`, `deps-confirmed`, `deps-design-only`, `deps-anything`, `deps-strict`; `deps-notices` | `PLANTS` of `position.py`; of `loop_transition.py` | none |

### Migration

None: no confirmation exists before this unit; a dependent with a reachable parent and no
confirmation holds its Build items under the default, exactly the clause's rule.

### Rollout

Live with the engine and the mailbox. The notices post only where a README's `parents:` names the
moving build, so a build no other build depends on posts nothing. The kit version is the lander's to
mint at the push (`tools/push-main.sh@78f40c3c2475:27`).

### The budget rows

`check_plant_tokens` holds the `plants=<n>` token of each loop-kit row equal to `len(PLANTS)` of the
module its argv runs, once imported (`tools/run-gates/run-selftests.sh#check_plant_tokens`). Units
ordered before this one add six `position.py` plants, KICK-dKeptSession-13's one and -10's five, and
six `loop_transition.py` plants, KICK-dKeptSession-5's two, -36's three and -24's one. So S10 moves
the `loop position fixtures` token from 37 to 44 and the `loop transition record` token from 19 to
20 (DERIVED: `len(PLANTS)` read at 7df6a1dac, 31 and 13, plus those units' plants). The builder
re-reads both counts at the unit's base and sets the tokens seven and one above them.

| Figure | `loop position fixtures` | `loop transition record` |
|---|---|---|
| proxy `r` at this tree, the row's note (PINNED 2026-11-21) | 68.3 s over 31 plants | 33.4 s over 13 plants |
| the earlier units' plants, estimates (PINNED 2026-11-22) | 2 s, then 5 times 5 s | 6 times 9 s |
| this unit's plants, estimates (PINNED 2026-11-22) | 7 times 5 s | 9 s |
| `r` after this unit (PINNED 2026-11-22, the sum) | 130.3 s | 96.4 s |
| budget, max of the row's value and 1.5 `r` | 432 stands over 196 | 145, over the row's 60 today |
| the leg's ceiling in `tools/gate-legs.json` | 300, above 130.3 s | 120, above 96.4 s |

The `boundary` case's 2 s is KICK-dKeptSession-13's estimate (PINNED 2026-11-22). The other
`position.py` estimates are the `plan-frontier` plant's 4.7 s, a driver run, rounded up, since each
`deps-*` plant pushes to a bare origin and reads a lease. The `loop_transition.py` estimates are the
`backward-rows` plant's 8.2 s, the module's slowest, rounded up, since each plant builds a scratch
repository with a second build or a bare origin. Each analog was read alone by direct CLI on the
run's node at 7df6a1dac. The builder reads each new plant alone by direct CLI and appends
`Then re-read by KICK-dKeptSession-7 as PINNED proxy r <s>` to each row's note, with each budget the
row's value or 1.5 `r` rounded up, whichever is higher. Neither leg has a row in
`tools/run-gates/ceiling-evidence.txt`, so no evidenced maximum moves. A declared ceiling is the
owner's to move (`memory/guides/BUILD-METHOD.md`, M3): where the builder's reading takes either `r`
to its leg's ceiling, the unit stops before it lands and names the raise for the owner, and it never
edits `tools/gate-legs.json`.

### Files touched (estimate)

- `tools/loop/position.py`: the reach, the switched gate, the key reads, seven plants
- `tools/loop/loop_transition.py`: the listing, the notices, `read_dependents`, `dependents`, the launch, one plant
- `tools/loop/placement.py`: `write_foreign_lease` takes extra record fields, its callers unchanged
- `tools/run-gates/selftest-budgets.txt`: S10, the `loop position fixtures` row's `plants=` token 37
  to 44 and the `loop transition record` row's 19 to 20, each note's re-read (DERIVED: `len(PLANTS)`
  at the unit's base)
- `tools/unattended/unattended.sh`: `--lease show`, `print_lease_witness`, the `landed` notice in `verb_landed`
- `tools/unattended/unattended.test.sh`: the landed-notice and witness-read arm
- `help/loop.md`: the new section and the `--lease` paragraph

### Alternatives rejected

- **A reply timeout as the reach test.** Coordination `[interpretations]` 1 makes the lease the bound:
  no timeout applies.
- **The gate holding Design too under `wait-for-landing`.** FI-2 offered "Design waits too" and the
  owner did not pick it; the value set has no such member.
- **The engine parsing lease refs itself.** A second reader of the lease record beside `read_claims`.

## 5. Production-readiness checklist

- security — the notices pass through unit 5's post path and its body check; the engine's reads are
  sourced drivers with fixed argv, each value a positional argument.
- perf / scale — per parent not landed and per engine call: one `--lease status`, and under
  `confirmed-interfaces` one `--lease show` and one check; one post per dependent per Design exit and
  per landing.
- error / empty / loading states — an unread lease reads `unreachable`, which holds Build and never
  admits it; an absent or unfetchable `witness` holds Build as `awaiting confirmed`; a failed notice
  prints its lines and fails no transition or landing.
- observability — every unlanded parent prints its interrupt with reach, cause and value; every
  notice is a mail message the dependent's interrupt lists.
- risks — under the default, a dependent with a live parent that never confirms waits for the
  landing, the clause's fallback; a parent spec revised during Build moves the listing and holds its
  dependents until its next Design exit posts `changed` or it lands; a parent whose lease `witness` is
  a waiting question's mail commit lists no spec, so its dependents hold until its next transition
  renews the lease. Each fails closed. The plants stage no `stale`, `terminal` or `released` verdict,
  which read by S1's one `unreachable` branch as no lease does.
- testing — the plants and arms of §6 and §7.
- migration — none.
- user docs — `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/position.py --fixture --plant deps-wait` runs with
  `deps.coordination = "wait-for-landing"`, a parent unlanded and its lease `live`, a next item of the
  Design step answers `act` with the dependency interrupt naming `not landed`, and a next item of the
  Build step answers `blocked` naming the parent, `not landed` and the value.
  Red when: Design is held, or Build runs before the landing.
  fixture: the plant's scratch carries a bare origin, the tree's `.unattended.conf` with
  `RUN_CLAIMS="on"`, the planted lease written by `write_foreign_lease` and the policy file committed
  and pushed; every `deps-*` plant reads so.
- **AC2** — When `--plant deps-unreachable` runs under `message-then-progress` with no parent lease
  on the remote, the Build item answers `blocked` naming `unreachable`; with the lease `live`, its
  `witness` the parent's transition commit and a current confirmation, it answers `act`.
  Red when: an unreachable parent admits Build, or a reachable confirmed one holds it.
- **AC3** — When `--plant deps-order` runs with `deps.coordination = "order-only"` and the parent
  unlanded and unreachable, the Build item answers `act` and prints the dependency interrupt naming
  `order only`.
  Red when: `order-only` holds anything.
- **AC4** — When `--plant deps-confirmed` runs under the defaults with the parent reachable, the Build
  item answers `blocked` naming `awaiting confirmed` while no confirmation is in the mailbox, `act`
  once a `confirmed` whose `content-key` recomputes is, and `blocked` again when the newest
  confirmation's key does not recompute.
  Red when: Build runs on no confirmation, or on one whose key is stale.
- **AC5** — When `--plant deps-design-only` runs with `deps.early-build = "design-only"` and the parent
  reachable, the Design item answers `act` and the Build item `blocked` naming `not landed`.
  Red when: `design-only` admits Build before the landing.
- **AC6** — When `--plant deps-anything` runs with `deps.early-build = "anything-coordinated"`, the
  parent reachable and no confirmation, the Build item answers `act`; with no lease it is `blocked`
  naming `unreachable`.
  Red when: `anything-coordinated` holds a reachable parent's dependent, or admits an unreachable one.
- **AC7** — When `python tools/loop/loop_transition.py --fixture --plant deps-notices` moves a
  fixture parent from `designing` to `building` with one dependent README naming it in `parents:`,
  one `confirmed` message to `build:<dependent>` with subject `interfaces <parent>` and a 12-hex
  `content-key` is in the mailbox, the key recomputed over the parent's `spec/` listing at the move's
  transition commit, with `--witness` planted at an older ancestor whose listing differs; a second
  move out of Design posts `changed` with a different key and no second `confirmed`.
  Red when: Design's exit posts nothing, a later exit posts `confirmed` again, or the key is taken at
  `--witness`.
  fixture: a scratch repository with two builds, a bare origin under `%TEMP%` and `RUN_CLAIMS=on`.
- **AC8** — When `bash tools/unattended/unattended.sh --landed <parent>` succeeds in that fixture, one
  `landed` message to `build:<dependent>` carrying the landed sha is in the mailbox; with the post
  planted to fail, the verb still exits 0 and prints the post's line.
  Red when: a landing posts no notice, or a failed notice fails the landing.
- **AC9** — When `--plant deps-strict` runs with a policy file naming `preset = "strict"` and no
  override of either key, it gives AC1's answers and AC5's, the keys reading `wait-for-landing` and
  `design-only` with the source `preset`. This is each key seen on strict's value.
  Red when: a strict-named file behaves as standard, C2-F11's consequence.
- **AC10** — When `grep -n 'deps.coordination\|deps.early-build\|unreachable\|landed\|lease show'`
  runs over `help/loop.md`, each is found in its `## Coordinating with a parent build` section, and
  `lease show` also in its `--lease` paragraph.
  Red when: the gate's values or the witness read are undocumented.
- **AC11** — When `bash tools/unattended/unattended.sh --lease show build <parent>` runs in AC8's
  fixture after a renew with `--witness <sha>`, it prints that sha alone, exit 0; with no lease it
  prints `-`; with `RUN_CLAIMS` off it prints `lease — off · <parent>/build`, exit 0.
  Red when: the verb prints any field but the witness, or writes a ref.
- **AC12** — When, at the unit's commit,
  `python -I -c "import sys; sys.path.insert(0, 'tools/loop'); import position as m; print(len(m.PLANTS))"`
  runs, it prints the number that
  `grep -oP '^loop position fixtures\t.*\Kplants=\d+' tools/run-gates/selftest-budgets.txt`
  prints after `plants=`; the same probe importing `loop_transition` prints the number
  `grep -oP '^loop transition record\t.*\Kplants=\d+' tools/run-gates/selftest-budgets.txt`
  prints after `plants=`; and the seven `deps-*` plants and `deps-notices` are keys of the two `PLANTS`.
  Red when: either row still carries the count from before this unit's plants.
  figure: PINNED 2026-11-22 at `7df6a1dac`, the probes print `31` and `13`, the greps `plants=31`
  and `plants=13`, before the units ordered ahead of this one land.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `scratch-guard self-test` · `tier2-review self-test` · `policy fixtures` · `loop position fixtures` · `loop transition record` · `loop placement fixtures` · `docs` · `every held leg is budgeted, every budget row resolves`

New arm: tools/loop/position.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC9 · the seven `deps-*` plants, `deps-wait` staged red by the gate read without its value · the `loop position fixtures` row's `plants=<n>` token rises by seven
New arm: tools/loop/loop_transition.py · covers AC7 · the `deps-notices` plant over a two-build fixture, red with the notice call left out · the `loop transition record` row's `plants=<n>` token rises by one
New arm: tools/unattended/unattended.test.sh · covers AC8 AC11 · the landed notice, staged by a post planted to fail, and the witness read over a renewed lease · none

## 8. Open questions

- **F1 — Which items does the dependency gate hold?** Options: (a) the Build step's items and every
  later step's, Design items running, as FI-2's answer and FI-5's settled text say a dependent designs
  at any time; (b) every item, the landed engine's single rule, which is "Design waits too", an
  option FI-2 offered and the owner did not take. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1,
  FI-2 and FI-5. widens: none · relaxes: none
- **F2 — Which of a dependent's units consume a parent's interfaces?** Options: (a) every unit of the
  dependent, since no record declares per-unit consumption and holding a unit that consumes nothing
  costs only waiting; (b) a new per-unit declaration, a surface no clause names. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — What interface text does a `confirmed` carry the key of?** Options: (a) the listing
  `git ls-tree -r` of the build's `spec/` folder at the transition commit that leaves Design, the
  record of its frozen feature design, which the dependent recomputes at the parent lease's `witness`,
  so any spec change since the confirmation holds the dependent until a `changed` names it; (b) a
  declared interfaces section, a record kind no build has landed.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, re-resolved at rev-5 on the lease `witness`,
  a commit recording a transition of the build (`tools/unattended/unattended.sh#check_lease_transition`),
  not the `--witness` ancestor the writer resolves, so the key is taken at the transition commit, and
  at `HEAD` where `micro-format` alone makes none; first resolved on rung 3, coordination
  `[interpretations]` 2's "Design's exit posts each frozen feature's declared interfaces".
  widens: none · relaxes: none
- **F4 — How is a later change told additive from breaking?** Options: (a) not here: every later
  Design exit posts `changed` with the new key, and dIndexedDesign's `design.reentry` judges the
  change; (b) a classifier in this unit, which no record defines. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F5 — How does S3 read the parent lease's `witness`, when `--claims` prints fields 1 to 5 and
  `witness` is field 15?** Options: (a) a read verb printing one lease's `witness`, run as S1 runs its
  read; (b) `--claims` printing `witness` as a sixth field, which moves a row shape another reader
  parses; (c) parsing the lease ref's commit here, a second lease parser beside `read_claims`, which
  §4's rejected alternative refuses. RESOLVED (owner, 2026-11-05): (a) the `--lease show` read verb,
  "`unattended.sh --lease show build <slug>` prints the lease's `witness` field from `CLAIM_ROWS`, or
  `-` where it holds none", then asked of dPlacedRequest; who builds it is F7.
- **F6 — Does this unit answer a dependent's `confirm-request`?** Options: (a) no: the clause names
  interfaces confirmed at Design's exit and no automatic answer, and the parent's session answers a
  request by hand with `--mail post --kind confirmed --answers <id> --interface <file>` and
  `--mail ack`, the verbs units 5 and 27 land, which the dependent's check reads as any confirmation;
  (b) `write_transition` answering every open request at each move, which confirms interfaces before
  Design freezes them, and whose `confirmed` leaves the request `open` under `KICK-dKeptSession-5` S7,
  so the parent's own guard still refuses. RESOLVED (agent, 2026-11-21, delegated): (a), rung 1; v2's
  clause and coordination item 8, which gives the answer to the parent's session. widens: none ·
  relaxes: none
- **F7 — Who lands `--lease show`, now that dPlacedRequest has landed without it?** Options: (a) this
  unit, beside `print_lease_status`, in the owner's words, read-only; (b) the ask filed late in
  dPlacedRequest's `BACKLOG.md`, `confirmed-interfaces` holding every reachable parent's dependents as
  `awaiting confirmed` until it lands, a deferral this build run may not take; (c) field 15 read in a
  sourced snippet, a second positional parser of `CLAIM_ROWS`. RESOLVED (agent, 2026-11-21,
  delegated): (a), rung 3; the most capable option no veto removes, the owner's ruled verb in the
  clause's own lease read, and the driver is this unit's file. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 7, scout C row 1, Shared interfaces I1,
  I8, I19, I20 and I22, coordination item 8 and its interpretations, FI-2, FI-5, and v2's `deps`
  rows and strict cells.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-35`, `KICK-dKeptSession-42`,
  `KICK-dKeptSession-44` mirrored, the other ends of the edges the round-1 spec audit's promoted
  units declare; no other section moved.
- rev-3 · 2026-10-26 · §2 S3, S4, S6 · §3 Non-goals, Edges · §5 · §6 AC7 · §8 F3, F5 · re-grounded on
  dPlacedRequest at `2740f0a3d` and dDeclaredLoop at `783f1ad3a` by the cross-check record
  `build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`, rows 23, 24 and 26: the lease
  `witness` is read through the verb F5 asks for, the listing is taken at the transition commit, and
  the keys are read by `policy.py get` as a subprocess.
- rev-4 · 2026-11-05 · §2 S3 · §3 Non-goals · §8 F5 · F5 resolved by the owner to (a), the
  `--lease show build <slug>` read verb asked of dPlacedRequest in its `BACKLOG.md`, under the brief
  `2026-11-05-prompt-KICK-dKeptSession-1-owner-forks`; no other section moved.
- rev-5 · 2026-11-21 · §7 · the leg line names `scratch-guard self-test`, `tier2-review self-test`
  and `policy fixtures`, the legs whose manifest guards §4's `tools/unattended/unattended.sh` and
  `tools/govkit/govkit.py` trip, as the spec-tokens guards join named at the build run's spec stage
  under the brief `2026-11-21-prompt-KICK-dKeptSession-1-build-brief`; no other section moved.
- rev-6 · 2026-11-21 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §8 F1, F3, F5, F6, F7 · §10 · re-grounded on
  the run's base c2a407b0 under the brief `2026-11-21-prompt-KICK-dKeptSession-6-orders-23-24-reground-brief`:
  every line citation re-cited to a symbol or a blob pin; the gate re-cited to the landed
  `derive_interrupts` and `derive_answer`; the reach read moved from `--claims` to the one-lease
  `--lease status`, and every driver read to the sourced launch `KICK-dKeptSession-42` F2 rules; the
  keys read by `read_policy_kit` as the loop kit reads policy; S5 names `verb_landed`'s two success
  exits; `read_dependents` homed in `loop_transition.py` with a `dependents` verb the driver runs, and
  `derive_interface_listing` minted as the one listing; the AC7 arm moved from the absent
  `tools/loop/selftest.py` to a `loop_transition.py` plant; widened by S7, the `--lease show` verb the
  owner ruled and no build filed (F7), and by `write_foreign_lease`'s extra fields; narrowed by F6,
  the `confirm-request` answer dropped, by the kit version move the lander mints and the
  `subject-pins.tsv` regeneration no leg change owes; the leg line gains the loop legs, `loop
  placement fixtures` and `docs`; AC2 and AC6 stage unreachable by no lease.
- rev-7 · 2026-11-22 · S10 · §4 · §4 Files touched · AC12 · §7 · by
  `2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief`: the eight plants move two `plants=<n>`
  tokens `check_plant_tokens` grades, so S10 and AC12 observe them, `tools/run-gates/selftest-budgets.txt`
  joins Files touched, §4 states both rows' re-price over the earlier units' plants and the stop at a
  leg's ceiling, and §7 names the budget leg.

## 10. Reuse audit

The seam extended is the landed dependency gate in `tools/loop/position.py`, `derive_interrupts` and
`derive_answer`, its landed test kept as the `landed` reach word; the reach reads dPlacedRequest's one
lease read `--lease status` through the sourced driver `placement.py` already runs, and the notices
post through unit 5's writer, after the commit where `write_card_follow` runs. The keys reuse
`read_policy_kit`; the plants reuse `placement.py`'s `write_foreign_lease`, extended rather than
copied. No verb printed a lease's `witness`, so S7 adds the one the owner ruled.
`python tools/codebase-map/reuse_lookup.py "a dependency gate switched by policy and parent
reachability"`, re-run at c2a407b0, ranked `read_policy_value`, `read_policy_kit`, `PolicyRefused`
and `load_policy`, name stems on `policy`; `read_policy_kit` is the reader S6 reuses, and none is a
dependency gate. `python tools/memory-recall/query.py "how does a dependent
build coordinate with its parent"` with the terms below, re-run at c2a407b0, returned this spec, the
spec brief's unit row, the C2 skeptic brief and scout C's row 1, which names TOOL-dDeclaredLoop-7 S4's
interrupt, the seam above; none disagrees with source.

Recall terms used: deps.coordination deps.early-build confirmed changed landed parent lease reachable wait-for-landing dependency gate
