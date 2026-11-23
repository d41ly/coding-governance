# KICK-dKeptSession-7 — dependency coordination: `deps.coordination` switching the dependency gate by the parent's lease, `deps.early-build` admitting Build, and the `confirmed`, `changed` and `landed` notices

**Status:** DEFERRED · rev-9 · 2026-11-23 · node a · Tier-2 · base 2b88519b · streams kickoff · order 24 · advances KICK-dKeptSession-29

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
| [2026-11-21-prompt-KICK-dKeptSession-7-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-7-precheck-brief.md) | research | KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-55 |
| [2026-11-22-prompt-KICK-dKeptSession-7-1-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-7-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-7-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-7-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-7-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-7-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

A dependent build coordinates with the builds its `parents:` names before it waits on them: a parent
is reachable while its build lease is live; at Design's exit a build posts its frozen interfaces to
each dependent as `confirmed`; a dependent's units enter Build once those are confirmed, as
`deps.early-build` admits; a later change posts `changed` and the landing posts `landed`; and a
dependent whose parent is unreachable enters Build only after the parent lands, as
`deps.coordination` says (coordination item 8, FI-2, FI-5). Each key is seen on strict's value,
`wait-for-landing` and `design-only` (C2-F11). At base the engine answers `blocked` on any `parents:`
build not landed, whatever its step and reach (`tools/loop/position.py#derive_answer`), so every
preset behaves alike and no build reaches another (gap-flow-06).

## 2. Scope (IN)

- **S1** — Reachability, `derive_parent_reach(root, parent)` in `tools/loop/position.py`: `landed`
  where the engine's landed test holds (`tools/loop/position.py#derive_position_into`); else
  `reachable` where `--lease status build <parent>` (`tools/unattended/unattended.sh#print_lease_status`)
  prints the `<parent>/build` row of six TAB fields whose fifth, the verdict, is `live` or `held`;
  else `unreachable`: any other verdict, `lease — none`, `lease — off`, a non-zero exit, a
  `LookupError` and a read past the bound. The read runs through §4 "The driver launch", as
  `tools/loop/placement.py#read_build_lease` runs it; no lease ref is parsed here and no other
  timeout applies (coordination `[interpretations]` 1). Observed by AC1, AC2, AC3 and AC6.
- **S2** — The gate. `deps.coordination` (`message-then-progress`, `wait-for-landing`, `order-only`;
  default `message-then-progress`) switches the gate per parent not `landed` by
  `derive_dependency_hold(coordination, early_build, reach, confirmed)`, `(cause, holds)` by §4's
  table. `derive_position_into` passes `derive_interrupts` (`tools/loop/position.py#derive_interrupts`)
  one row per open parent, `parent`, `reach`, `cause`, `value` and `holds`, for today's slug list;
  each `dependency` subject is `<parent> · <reach> · <cause> (deps.coordination: <value>)`, printed by
  `tools/loop/position.py#render_position_lines`. `holds` is true where the table holds Build and the
  build's step's `[[step]]` `order` (`tools/loop/loop.toml`) is at least `step.build`'s.
  `derive_answer` answers `blocked`, at its landed rung, on a dependency interrupt that holds, the
  reason the holding subjects joined by `; `. A Design item runs under every value (§8 F1). The landed
  `parent-unlanded` plant still holds, its `tPar` read `unreachable` or `policy unread` with no
  `.unattended.conf`. Observed by AC1, AC2 and AC3.
- **S3** — `deps.early-build` (`confirmed-interfaces`, `design-only`, `anything-coordinated`; default
  `confirmed-interfaces`), read for a `reachable` parent under `message-then-progress`.
  `confirmed-interfaces` reads `check_parent_interfaces(root, slug, parent)` in
  `tools/loop/loop_transition.py`, `(rc, line)`: the lease `witness` `w` by `--lease show build
  <parent>` (S7); where `git cat-file -e <w>^{commit}` fails, one bounded `git fetch <remote>`
  (`tools/loop/claims.py#resolve_remote`); `derive_interface_listing(root, parent, w)` (S4) in a
  scratch file; then `KICK-dKeptSession-27` S5's `check_interface_notice <slug> "interfaces <parent>"
  <file>`. The cause is `confirmed` on its exit 0, never chosen by arrival order; `awaiting confirmed`
  on its exit 1 or a witness of `-`; `confirmation unread` on its exit 2, a read past the bound, a
  commit still absent or a listing that does not derive, with one `position: NOTE · interfaces
  <parent> unread: <line>` (§8 F8). `design-only` is `not landed`; `anything-coordinated` is
  `coordinated`. Every unit of the dependent consumes the parent's interfaces (§8 F2). Observed by
  AC4, AC5 and AC6.
- **S4** — The `confirmed` notice. `derive_interface_listing(root, build, commit)` in
  `tools/loop/loop_transition.py` is the bytes `git ls-tree -r <commit> -- <memory
  root>/builds/<build>/spec/` prints under `read_clean_env()`, never through `read_git`, which decodes
  and strips; it is written by `Path.write_bytes`, so a key posted on one node recomputes on another,
  and a non-zero exit raises `ValueError`. `write_transition`
  (`tools/loop/loop_transition.py#write_transition`), on a move from `designing` to `building`, calls
  `write_dependency_notices(root, build, commit)` after `write_card_follow`, its lines joining `said`;
  it never raises. Per dependent of `read_dependents(root, build)` (S9) it posts `--mail post <build>
  --to build:<dependent> --kind <kind> --subject "interfaces <build>" --interface <listing file> <body
  file>` (`KICK-dKeptSession-27` S3), the listing at `commit`, the body its full sha. `<kind>` is
  `changed` where `tools/loop/loop_transition.py#read_mail_rows` over the dependent holds a
  `confirmed` row whose `from-build` is `build` with that subject, else `confirmed`. A read
  answering `unarmed` or raising, or a raising `read_dependents`, posts nothing to whom it covers
  and adds one `loop: notice · unread · <whom> · <why>`. `commit` is the
  transition commit, which the driver next passes as the lease's `witness`
  (`tools/unattended/unattended.sh#read_transition_witness`, §8 F3); where `transitions.record` selects
  `micro-format` alone no commit is made, the listing is taken at `HEAD` and the dependent holds as
  `awaiting confirmed`. A failed post adds its lines and fails nothing. Observed by AC7.
- **S5** — The `landed` notice. `write_landed_notices <slug> <sha>` in the driver runs at both of
  `verb_landed`'s success exits (`tools/unattended/unattended.sh#verb_landed`) before `return 0`,
  `<sha>` `DP_LANDING` in place and `head` on the recorded exit. With `RUN_CLAIMS` off it posts
  nothing; on, per line
  `run_loop_verb loop_transition.py dependents --build=<slug>` leaves in `_bd_out` at `_bd_rc` 0
  (`tools/unattended/unattended.sh#run_loop_verb`, S9) it runs `( main --mail post … )`, kind
  `landed`, `--to build:<dependent>`, subject `landing <slug>`, a `mktemp` body holding `<sha>`, and
  prints the post's line; a verb that does not answer prints `unattended: NOTE — no landed notice:
  <_bd_why>`. It returns 0, so the verb's exit never moves. Observed by AC8.
- **S6** — The keys, each read by `read_policy_kit()` (`tools/loop/loop_parents.py#read_policy_kit`)
  and `resolve(<key>, <root>, build=<slug>)` at the landed revision (`tools/policy/policy.py#resolve`),
  spelled whole, so a scenario-placed dependent reads its slot (`KICK-dKeptSession-20` S5). A
  `Refusal`, or the `LookupError` of no policy kit, reads no default: each open parent's cause is
  `policy unread`, holding Build, with one `position: NOTE · <key> unread: <why>` (§8 F8). A policy
  file naming `preset = "strict"` reads `wait-for-landing` and `design-only`, `[preset.strict]` of
  `tools/policy/presets.toml`, source `preset`. The NOTEs are a new `notes` field of the position,
  printed after the `interrupt —` lines and carried by `--json`. Observed by AC9.
- **S7** — The witness read (§8 F5, F7): `--lease show build <slug>`, dispatched beside `--lease
  status`, runs `print_lease_witness <slug>`: one `read_claims quiet` and the build row's `witness`,
  field 15 of `CLAIM_ROWS` (`tools/unattended/unattended.sh#read_claims`), alone, or `-` where it holds
  none or no lease exists; `lease — off · <slug>/build` with `RUN_CLAIMS` off, exit 0; `lease not
  written — <why>`, exit 2, for a read that does not answer; `lease not written — --lease show takes
  build <slug> and nothing else`, `_rl_rc=2`, for any other shape. It writes nothing. Observed by
  AC11.
- **S8** — The texts. `help/loop.md` gains `## Coordinating with a parent build` after `## Where a
  build is, and what runs next`: the gate's values, the reach words, the causes, the notices, and
  that an unacknowledged notice is open mail holding the dependent's moves under unit 5's guard. §4
  "The shipped texts" lists the other page, guide, docstring, README and driver-comment edits.
  Observed by AC10 and AC13.
- **S9** — The dependents. `read_dependents(root, build)` in `tools/loop/loop_transition.py`: every
  build whose README front matter's `parents:` names `build`, read by the memory-tree kit's
  `parse_front_matter` as `tools/loop/loop_parents.py#read_withdrawn_parents` reads it, sorted.
  `python loop_transition.py dependents --build <slug>` prints one per line, exit 0, `loop: unanswered
  · <why>` for an unreadable README and `loop: unarmed · <why>` for no memory-tree kit, exit 2.
  Observed by AC7 and AC8.
- **S10** — The budget rows: the seven `deps-*` plants move the `plants=<n>` token of the `loop
  position fixtures` row and `deps-notices` that of `loop transition record` in
  `tools/run-gates/selftest-budgets.txt`, re-priced as §4 states. Observed by AC12.

## 3. Non-goals (OUT)

- No re-entry on `changed`: dIndexedDesign's `design.reentry`
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md@4a13cbc82a99:143`).
- No `landing.order` or `deps.landing` (dShippedRelease's), and no `deps.on-parent-withdrawn`
  (dDeclaredLoop's).
- No lease write and no verdict: `--lease show` (S7) is read-only.
- No mailbox, kind or post path (`KICK-dKeptSession-5`), content key (`KICK-dKeptSession-27`) or
  acknowledgement of a consumed notice (`KICK-dKeptSession-42`).
- No automatic answer to a `confirm-request` (§8 F6), and no per-unit interface declaration (§8 F2).
- No catalogue edit and no help anchor for the two landed keys, so `.governance/policy.json`,
  `help/reference/policy.md` and `memory/project/docs-undocumented.txt` do not move.

### Edges

- **consumes-from** `KICK-dKeptSession-1` — `presets.toml`, whose strict cells `wait-for-landing` and `design-only` each key is seen on, read through the reader's preset step
- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox` and the `--mail post` writer, through which the notices are posted and the confirmations read
- **consumes-from** `KICK-dKeptSession-27` — `content-key`, its `--interface` option and `check_interface_notice`, the recomputed key that decides which confirmation is current, never arrival order
- **consumes-from** external — dDeclaredLoop, landed: the position engine's dependency gate and answer precedence, and `write_transition`; dPlacedRequest, landed: the build lease, `--lease status`, `CLAIM_ROWS`' `witness` and `run_sourced`; dGroundRules' `resolve`
- **hands-off** external — dIndexedDesign's `design.reentry` re-enters a dependent's consuming units on a `changed` message
- **hands-off** `KICK-dKeptSession-35` — `write_dependency_notices` and `verb_landed`'s notice, which that unit gives a pass and a visible refusal line (id 4)
- **hands-off** `KICK-dKeptSession-42` — the notices and S3's `check_parent_interfaces`, which that unit's transition writer reads to acknowledge what the dependent consumed (id 55)
- **hands-off** `KICK-dKeptSession-44` — `derive_parent_reach`, the listing's bytes and `read_dependents`, the batch's S17 and S20 (ids 24, 35)

## 4. Design

### Evidence

Read at `2b88519b` (2026-11-23), units 51, 27, 24, 10, 25, 21 and 6 read as landed.

- Coordination item 8 and its interpretations 1 and 2
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md@4a13cbc82a99:130`,
  `:187`): reachable while the lease is live, no timeout, Design's exit posts the frozen interfaces.
  FI-2 and FI-5's settled text
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md@6f6b55dd620d:78`,
  `:127`): a dependent designs at any time, building once its interfaces are confirmed. v2's values,
  strict's cells and the clause
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1165`,
  `:1490`, `:1771`).
- A sourced `main` refuses outside a subshell (`tools/unattended/unattended.sh#main`), so
  `read_build_lease` wraps it in `( … )`; `run_lease_verb` refuses an unknown act, so `show` is
  dispatched before it, as `status` is.

### The gate, per parent not landed

| `deps.coordination` | reach | `deps.early-build` | cause | Build items |
|---|---|---|---|---|
| `wait-for-landing` | any | not read | `not landed` | held |
| `message-then-progress` | `unreachable` | not read | `unreachable` | held |
| `message-then-progress` | `reachable` | `confirmed-interfaces` | `confirmed`; `awaiting confirmed` or `confirmation unread` | run; held |
| `message-then-progress` | `reachable` | `design-only` | `not landed` | held |
| `message-then-progress` | `reachable` | `anything-coordinated` | `coordinated` | run |
| `order-only` | any | not read | `order only` | run |
| either key unread | any | either key unread | `policy unread` | held |

Design items run in every row; the precedence is otherwise untouched. Every open parent's reach is
read, since its interrupt prints it.

### The driver launch

`tools/loop/breakpoints.py#run_sourced` gains two keyword-only arguments, its callers unchanged:
`args=()`, values passed as `$2` onward, never interpolated, and `timeout=900`, its landed bound.
Each call here, and S3's fetch, passes `MAIL_GUARD_SECONDS`, 30 seconds (PINNED at
`tools/loop/loop_transition.py@356ea5522ebe:134`), `TimeoutExpired` a read past the bound. Callers
import it inside the function, since `breakpoints.py` imports both modules at its top.

```
run_sourced(root, '( load_driver_conf && main --lease status build "$2" )', args=(parent,), timeout=B)
run_sourced(root, '( load_driver_conf && main --lease show build "$2" )', args=(parent,), timeout=B)
run_sourced(root, 'load_driver_conf && check_interface_notice "$2" "$3" "$4"', args=(slug, subject, file), timeout=B)
run_sourced(root, '( load_driver_conf && main --mail post "$2" --to "$3" --kind "$4" --subject "$5" --interface "$6" "$7" )', args=…, timeout=B)
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
| `derive_interface_listing`, `write_dependency_notices`, `read_dependents`, `check_parent_interfaces` | Python functions, `tools/loop/loop_transition.py` | `py.function`, OK by `lexicon.py --suggest` |
| `print_lease_witness`, `write_landed_notices` | driver shell functions | `sh.function`, OK by `lexicon.py --suggest` |
| `dependents`; `--lease show`; `notes` | a verb; a driver act; a position field | none |
| `args`, `timeout`; `fields`, `remote`; `content_key` | keywords of `run_sourced`, `write_foreign_lease`, `render_fixture_mail` | none |
| `reachable`, `unreachable`; the causes of §4's table | words on the engine's lines | none |
| `deps-wait`, `deps-unreachable`, `deps-order`, `deps-confirmed`, `deps-design-only`, `deps-anything`, `deps-strict`; `deps-notices` | `PLANTS` of `position.py`, each in `FX_DRIVER`; of `loop_transition.py` | none |

`tools/loop/placement.py#write_foreign_lease` gains `fields=()`, extra pairs such as `witness`, and
`remote=FIXTURE_REMOTE` for unit 10's keyword, since the position plants push to `origin`, not
`upstream`; `tools/loop/loop_transition.py#render_fixture_mail` gains `content_key=None`, a
`content-key: <k>` line, `k` the driver's `derive_gov_id --file` over the listing.

### The shipped texts

| Text | Edit |
|---|---|
| `help/loop.md`, "Where a build is" | the `blocked` sentence points to the new section; the plant list and driver sentence name the seven |
| `help/loop.md`, the `--lease` paragraph | names `--lease show`; its `verb:unattended.sh:--lease` anchor re-stamped by `python tools/govkit/docs_leg.py --fingerprints` at build time |
| `help/loop.md`, "Recording a build's move" | its plant list names `deps-notices` |
| `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md` | a sentence after `--lease status`'s on `--lease show`, one closing `--landed` on its notice; both the same bytes, as check 10 compares |
| `tools/loop/position.py` docstring | "`blocked` on a `parents:` build neither recorded nor derived `LANDED`" gains "whose cause holds the build's step"; a THE DEPENDENCY GATE paragraph; the driver sentence names the seven; WHAT THIS DOES NOT CHECK names interfaces beyond the `spec/` listing |
| `tools/loop/loop_transition.py` docstring | a `dependents` usage line, a notices sentence, the verb's exit |
| the docstrings of `derive_interrupts`, `derive_answer`, `write_transition`, `run_sourced` | the rows and `holds`, the notice lines, the keywords |
| `tools/loop/README.md`, "The transition record" | a sentence on the notices and `dependents` |
| `tools/unattended/unattended.sh` | the usage row; comments above the two new functions |

Left true: the `--lease` paragraph's `RUN_CLAIMS` off sentence, which `show` obeys; "writes nothing
to the tree" of `--landed` there and in `tools/unattended/STOPS.template.md` with its copy, a mail ref
being no tree write; the loop README's position section, whose `FX_DRIVER` phrase (unit 10) covers
the seven; "When a parent build is withdrawn", untouched; `tools/govkit/usage.toml`, no flag added
and no page showing `dependents`.

### Migration

None: no confirmation exists before this unit; a dependent with a reachable parent and no
confirmation holds its Build items under the default, exactly the clause's rule.

### Rollout

Live with the engine and the mailbox. The notices post only where a README's `parents:` names the
moving build. The kit version is the lander's to mint at the push (`tools/push-main.sh@78f40c3c2475:27`).

### The refusal ceiling

The driver's refusal sites stand at `347/347` (DERIVED: `python tools/memory-tree/check-arms.py
--report`'s `ceiling` row at `2b88519b`). This unit adds no `fail`, `exit 1` or `status=1` site:
`print_lease_witness` returns 2, the `show` dispatch sets `_rl_rc=2`, and `write_landed_notices`
echoes and returns 0. No `fail` branch is added, so the driver's `ARMS_FLOORS` pair stands.

### The budget rows

`tools/run-gates/run-selftests.sh#check_plant_tokens` holds each row's `plants=<n>` to `len(PLANTS)`:
32 and 18 at `2b88519b` (DERIVED: `len(PLANTS)`, each token equal). Unit 10's five and unit 24's one
land first, so S10 moves 37 to 44 and 19 to 20 (DERIVED: those counts). The builder re-reads both at
its base, sets each in place, and appends `Then re-read by KICK-dKeptSession-7 as PINNED proxy r <s>`.

| Figure | `loop position fixtures` | `loop transition record` |
|---|---|---|
| proxy `r`, the row's note (PINNED) | 68.5 s, 32 plants, 2026-11-22 | 44.3 s, 18 plants, 2026-11-23 |
| earlier units' plants, estimates (PINNED 2026-11-23) | 5 times 5 s | 6 s |
| this unit's, estimates (PINNED 2026-11-23) | 18 positions at 6 s | 6 driver calls at 5.5 s, rounded up |
| `r` after (PINNED 2026-11-23, the sum) | 201.5 s | 83.3 s |
| budget, row value or 1.5 `r`, the higher | 432 stands | 125, over 67 |
| leg ceiling, `tools/gate-legs.json` (PINNED 2026-11-23) | 300 | 120 |

The analogs, PINNED in the notes: `plan-frontier`'s 4.7 s driver run plus a second of lease and
policy push, per position AC1 to AC6 and AC9 derive; `mail-disposed`'s 5.4 s per driver call, three a
move. Where a reading takes `r` to its leg's ceiling the unit stops and names the raise, the owner's
(`memory/guides/BUILD-METHOD.md`, M3), never editing `tools/gate-legs.json`. The `unattended driver
selftest shard 8/8` row is an ESTIMATE by region share with no `plants=` token, so no row is
re-priced for the driver arm, as `KICK-dKeptSession-6` left it.

### Files touched (estimate)

- `tools/loop/position.py`: the reach, the gate, the key reads, `notes`, seven plants, the docstrings
- `tools/loop/loop_transition.py`: the listing, the notices, `read_dependents`, `dependents`,
  `check_parent_interfaces`, `render_fixture_mail`'s keyword, one plant, the docstrings
- `tools/loop/breakpoints.py`: `run_sourced`'s keywords and docstring
- `tools/loop/placement.py`: `write_foreign_lease`'s keywords, its callers unchanged
- `memory/map/generated/symbols.json`: the eight functions, by `python tools/codebase-map/gen_map.py
  --write`
- `tools/run-gates/selftest-budgets.txt`: S10
- `tools/unattended/unattended.sh`: S5, S7, the usage row and comments
- `tools/unattended/unattended.test.sh`: the arm in region eight, and the two floors §7 names
- `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`: the two sentences
- `help/loop.md`, `tools/loop/README.md`: §4 "The shipped texts"

### Alternatives rejected

- **A reply timeout as the reach test.** Coordination `[interpretations]` 1 makes the lease the bound.
- **The gate holding Design too under `wait-for-landing`.** FI-2 offered it and the owner did not pick
  it; the value set has no such member.
- **The engine parsing lease refs itself.** A second reader of the lease record beside `read_claims`.
- **The kind from the parent's Design exits.** A later dependent would first get a `changed`.

## 5. Production-readiness checklist

- security — the notices pass through unit 5's post path and body check; the engine's reads are
  sourced drivers with fixed scripts, each value a positional argument.
- perf / scale — per open parent and engine call one `--lease status`, and under
  `confirmed-interfaces` one `--lease show`, a fetch and a check, each bounded; one post per
  dependent per Design exit and landing.
- error / empty / loading states — an unread lease reads `unreachable`, a refused key `policy
  unread` and a refused check `confirmation unread`, each holding Build and naming why; a failed or
  unread notice prints its line and fails no transition or landing.
- observability — each open parent's interrupt names reach, cause and value; each notice is mail.
- risks — a parent that never confirms holds its dependents to the landing, the clause's fallback;
  a spec revised during Build, a question's mail commit as `witness` or a commit only an unpushed
  branch holds holds them to the next Design exit or renewal. Until `KICK-dKeptSession-42` lands a
  notice is open mail holding its dependent's moves until `--mail ack`. The boundary verb's position
  read has `CARD_POSITION_BOUND`, 10 seconds (PINNED at
  `skills/session-kickoff/manifest-check.sh@eb3e33878e89:305`); parent reads past it keep the card's
  pointer. Each fails closed. No plant stages `stale`, `terminal` or `released`, read as no lease.
- testing — the plants and arms of §6 and §7.
- migration — none.
- user docs — `help/loop.md` and the verbs guide pair.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/position.py --fixture --plant deps-wait` runs with
  `deps.coordination = "wait-for-landing"`, a parent unlanded and its lease `live`, a next item of the
  Design step answers `act` with the dependency interrupt naming `not landed`, and a next item of the
  Build step answers `blocked` naming the parent, `not landed` and the value.
  Red when: Design is held, or Build runs before the landing.
  fixture: the bare `origin`, the tree's `.unattended.conf` (`RUN_CLAIMS="on"`) as `FX_DRIVER`
  plants copy it, the lease by `write_foreign_lease`, the policy pushed; every `deps-*` plant so.
- **AC2** — When `--plant deps-unreachable` runs under `message-then-progress` with no parent lease
  on the remote, the Build item answers `blocked` naming `unreachable`; with the lease `live`, its
  `witness` a commit holding a parent spec, and a confirmation whose key recomputes, it answers `act`.
  Red when: an unreachable parent admits Build, or a reachable confirmed one holds it.
- **AC3** — When `--plant deps-order` runs with `deps.coordination = "order-only"` and the parent
  unlanded and unreachable, the Build item answers `act` and prints the dependency interrupt naming
  `order only`.
  Red when: `order-only` holds anything.
- **AC4** — When `--plant deps-confirmed` runs under the defaults with the parent reachable, the Build
  item answers `blocked` naming `awaiting confirmed` with no confirmation, `act` once a `confirmed`
  whose `content-key` recomputes is planted, still `act` once a newer `changed` whose key does not is,
  and `blocked` naming `awaiting confirmed` once the `witness` moves to a commit whose listing no
  row's key recomputes; with `breakpoints.run_sourced` planted to answer the check exit 2, it answers
  `blocked` naming `confirmation unread` and prints one `interfaces <parent> unread` NOTE.
  Red when: Build runs on no confirmation or a stale key, the newest row decides, or a refused check
  reads as unconfirmed.
  fixture: each confirmation planted on `origin` from `render_fixture_mail` with `content_key`.
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
  fixture: a scratch repository with two builds, a bare origin under `%TEMP%` and `RUN_CLAIMS=on`,
  `USERNAME` from `read_fleet_user` of `tools/loop/placement.py` and a session id in the environment.
- **AC8** — When `bash tools/unattended/unattended.sh --landed <parent>` succeeds in a region-eight
  fixture of two builds, the dependent's README naming the parent, one `landed` message to
  `build:<dependent>` carrying the landed sha is in the mailbox; with the post planted to fail, the
  verb still exits 0 and prints the post's line.
  Red when: a landing posts no notice, or a failed notice fails the landing.
- **AC9** — When `--plant deps-strict` runs with a policy file naming `preset = "strict"` and no
  override of either key, it gives AC1's answers and AC5's, the keys reading `wait-for-landing` and
  `design-only` with the source `preset`. In a second scratch whose only policy revision holds
  `deps.coordination = "bogus"`, since a valid earlier revision is read as `last-valid`, the Design
  item answers `act`, the Build item `blocked` naming `policy unread`, and a `deps.coordination
  unread` NOTE prints.
  Red when: a strict-named file behaves as standard, C2-F11's consequence, or a refused key reads a
  default.
- **AC10** — When `grep -n 'deps.coordination\|deps.early-build\|unreachable\|landed\|lease show'`
  runs over `help/loop.md`, each is found in its `## Coordinating with a parent build` section, and
  `lease show` and `deps-notices` elsewhere too; `grep -c 'lease show build'` over
  `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md` prints one non-zero
  count for both.
  Red when: the gate, the witness read or a plant is undocumented, or the guide's copies differ.
- **AC11** — When `bash tools/unattended/unattended.sh --lease show build <parent>` runs in AC8's
  fixture after a renew with `--witness <sha>`, `<sha>` a commit recording a transition of the build,
  it prints that sha alone, exit 0; with no lease it prints `-`; with `RUN_CLAIMS` off it prints
  `lease — off · <parent>/build`, exit 0; `--lease show unit <parent> <id>` exits 2.
  Red when: the verb prints any field but the witness, or writes a ref.
- **AC12** — When, at the unit's commit,
  `python -I -c "import sys; sys.path.insert(0, 'tools/loop'); import position as m; print(len(m.PLANTS))"`
  runs, it prints what `grep -oP '^loop position fixtures\t.*\Kplants=\d+' tools/run-gates/selftest-budgets.txt`
  prints after `plants=`, the same holding for `loop_transition` and `loop transition record`, and
  the eight plants are keys of the two `PLANTS`.
  Red when: either row still carries the count from before this unit's plants.
  figure: PINNED 2026-11-23 at `2b88519b`, the probes print `32` and `18`, the greps `plants=32`
  and `plants=18`, before units 10 and 24 land.
- **AC13** — When `grep -n 'dependents --build' tools/loop/loop_transition.py tools/loop/README.md`,
  `grep -n 'deps.coordination' tools/loop/position.py` and `grep -n 'lease show build'
  tools/unattended/unattended.sh` run, each file prints a line.
  Red when: a shipped text still states only the landed gate, or the verb or act is undocumented.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `scratch-guard self-test` · `tier2-review self-test` · `policy fixtures` · `loop position fixtures` · `loop transition record` · `loop placement fixtures` · `docs` · `every held leg is budgeted, every budget row resolves`

New arm: tools/loop/position.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC9 · the seven `deps-*` plants, `deps-wait` staged red by the gate read without its value · the `loop position fixtures` row's `plants=<n>` token rises by seven
New arm: tools/loop/loop_transition.py · covers AC7 · the `deps-notices` plant over a two-build fixture, red with the notice call left out · the `loop transition record` row's `plants=<n>` token rises by one
New arm: tools/unattended/unattended.test.sh · covers AC8 AC11 · the landed notice, staged by a post planted to fail, and the witness read over a renewed lease, in region eight · the effective `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by the arm's counted assertions, each with its `RAISED` line

The two floors read 4100 and 1317 at `2b88519b` (DERIVED: their last assignments,
`tools/unattended/unattended.test.sh@3d75bb5502e5:24312` and `:24601`), raised first by units 27,
24, 25, 21 and 6.

## 8. Open questions

- **F1 — Which items does the dependency gate hold?** Options: (a) the Build step's items and every
  later step's, Design items running, as FI-2's answer and FI-5's settled text say; (b) every item,
  the landed engine's rule, "Design waits too", which FI-2 offered and the owner did not take.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, FI-2 and FI-5. widens: none · relaxes: none
- **F2 — Which of a dependent's units consume a parent's interfaces?** Options: (a) every unit, since
  no record declares per-unit consumption and holding one that consumes nothing costs only waiting;
  (b) a new per-unit declaration, a surface no clause names. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — What interface text does a `confirmed` carry the key of?** Options: (a) the `git ls-tree -r`
  listing of the build's `spec/` folder at the transition commit leaving Design, which the dependent
  recomputes at the lease's `witness`; (b) a declared interfaces section, a kind no build has landed.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, re-resolved at rev-5 on the lease `witness`,
  a transition commit (`tools/unattended/unattended.sh#check_lease_transition`), not the
  `--witness` ancestor, and at `HEAD` where `micro-format` alone makes none; first resolved on rung 3,
  coordination `[interpretations]` 2. widens: none · relaxes: none
- **F4 — How is a later change told additive from breaking?** Options: (a) not here: every later
  Design exit posts `changed`, and dIndexedDesign's `design.reentry` judges it; (b) a classifier no
  record defines. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F5 — How does S3 read the parent lease's `witness`, when `--claims` prints fields 1 to 5 and
  `witness` is field 15?** Options: (a) a verb printing one lease's `witness`; (b) a sixth `--claims`
  field, moving a row shape others parse; (c) a second lease parser here. RESOLVED (owner,
  2026-11-05): (a) the `--lease show` read verb, "`unattended.sh --lease show build <slug>` prints the
  lease's `witness` field from `CLAIM_ROWS`, or `-` where it holds none"; who builds it is F7.
- **F6 — Does this unit answer a dependent's `confirm-request`?** Options: (a) no: the clause names
  no automatic answer, and the parent's session answers by hand with `--mail post --kind confirmed
  --answers <id> --interface <file>`; (b) `write_transition` answering each open request, confirming
  interfaces before Design freezes them. RESOLVED (agent, 2026-11-21, delegated): (a), rung 1; v2's
  clause and coordination item 8. widens: none · relaxes: none
- **F7 — Who lands `--lease show`, now that dPlacedRequest has landed without it?** Options: (a) this
  unit, beside `print_lease_status`; (b) a late ask of dPlacedRequest, every reachable parent's
  dependents held till it lands; (c) a second parser of `CLAIM_ROWS`. RESOLVED (agent, 2026-11-21,
  delegated): (a), rung 3; the owner's ruled verb, in this unit's file. widens: none · relaxes: none
- **F8 — What does the gate read where a key or the confirmation check is refused?** Options: (a)
  hold Build with a cause naming the unread read and one NOTE; (b) the catalogue default and
  `awaiting confirmed`, which reads standard's gate where a strict scenario places the build; (c)
  raise, holding Design too. RESOLVED (agent, 2026-11-21, delegated): (a), rung 1;
  `KICK-dKeptSession-20` §8 F4 never reads a posture unscoped, `KICK-dKeptSession-27` S5 keeps a
  refused check apart from `unconfirmed`, and (c) holds what F1 runs. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 7, scout C row 1, Shared interfaces I1,
  I8, I19, I20 and I22, coordination item 8, FI-2, FI-5, and v2's `deps` rows and strict cells.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-35`, `KICK-dKeptSession-42`,
  `KICK-dKeptSession-44` mirrored; no other section moved.
- rev-3 · 2026-10-26 · §2 S3, S4, S6 · §3 · §5 · AC7 · §8 F3, F5 · re-grounded by
  `build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`, rows 23, 24 and 26: the
  `witness` read through F5's verb, the listing at the transition commit, the keys by `policy.py get`.
- rev-4 · 2026-11-05 · S3 · §3 · §8 F5 · F5 resolved by the owner under
  `2026-11-05-prompt-KICK-dKeptSession-1-owner-forks`; no other section moved.
- rev-5 · 2026-11-21 · §7 · `scratch-guard self-test`, `tier2-review self-test` and `policy fixtures`
  named, the guards §4's paths trip, under `2026-11-21-prompt-KICK-dKeptSession-1-build-brief`.
- rev-6 · 2026-11-21 · §1 to §8 · §10 · re-grounded at c2a407b0 under
  `2026-11-21-prompt-KICK-dKeptSession-6-orders-23-24-reground-brief`: symbol or blob citations; the
  reach on `--lease status`; keys by `read_policy_kit`; `read_dependents`, `dependents` and the listing
  minted; AC7 a plant; widened by S7 (F7); narrowed by F6; the loop legs and `docs` joined §7.
- rev-7 · 2026-11-22 · S10 · §4 · AC12 · §7 · by
  `2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief`: the plants' two `plants=<n>` tokens
  observed, both rows re-priced, the stop at a leg's ceiling, the budget leg named.
- rev-8 · 2026-11-22 · S2 to S7 · §4 · §5 · AC4 · AC9 · AC10 · §8 F8 · §10 · by
  `2026-11-22-prompt-KICK-dKeptSession-7-1-spec-writer`: driver calls through the landed
  `run_sourced`, extended; S3's chain `check_parent_interfaces`; S6 reads `build=`; a refused key or
  check holds Build (F8); the listing is bytes; the verbs guide pair and `symbols.json` joined.
- rev-9 · 2026-11-23 · §1 · S1 to S10 · §3 · §4 · §5 · AC2 · AC4 · AC7 · AC8 · AC10 to AC13 · §7 · §8 ·
  §10 · re-grounded at `2b88519b` under `2026-11-23-prompt-KICK-dKeptSession-7-1-spec-writer`: the
  launches wrap `main` in `( … )`, as its sourced-call guard asks; S2 states the rows, `holds` and
  the reason; NOTEs are a `notes` field; S4 names a failed mailbox read; S5 mints
  `write_landed_notices`; the plants push to `origin` and plant keys; AC4 lets no newest row decide;
  the texts made false joined §4 and S8 (AC13); ceiling, floors and budgets re-stated; §8's options
  and §9's earlier lines cut for the size cap, no pick moved.

## 10. Reuse audit

The seam extended is the landed gate in `tools/loop/position.py`, `derive_interrupts` and
`derive_answer`, its landed test the `landed` reach; the reach reads `--lease status` through
`tools/loop/breakpoints.py#run_sourced`, extended; the notices post through unit 5's writer. The
keys reuse `read_policy_kit`; the plants `write_foreign_lease` and `render_fixture_mail`, extended.
No verb printed a `witness`, so S7 adds the owner's beside `print_lease_status`. `python
tools/codebase-map/reuse_lookup.py "a dependency gate switched by policy and parent reachability"`,
re-run at `2b88519b`, ranked `read_policy_value`, `read_policy_kit`, `PolicyRefused` and
`load_policy`, name stems on `policy`, none a dependency gate; `"print one build lease's witness
field"` ranked `build`, `field` and `build_records`, none a lease reader. `python
tools/memory-recall/query.py "how does a dependent build coordinate with its parent"` with the terms
below returned this spec, the spec brief's row and scout C's row 1; none disagrees with source.

Recall terms used: deps.coordination deps.early-build confirmed changed landed parent lease reachable wait-for-landing dependency gate
