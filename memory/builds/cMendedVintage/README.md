---
slug: cMendedVintage
node: c
opened: 2026-09-16
streams: deployer+tooling
roster: DEPL+TOOL
authorized-by: prompt
ids: DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9
---

# cMendedVintage — `update` gains an install-effect stage, and stops rolling kits back for work it declined to do

## The problem this build exists to solve

`govkit update --write` moves bytes and performs none of the install effects a new vintage needs: no
render, no `.gitattributes` block, no gate leg, no renormalize. It then runs each kit's own
`[check]` — the program that asks whether those effects happened — and rolls the kit back on the red
it just caused. Five rollbacks across two adopter repos, and a rolled-back run withholds the
`gov_commit` re-stamp, so the next run decides identically: three kits cannot advance at any number
of retries. Around that sit four more: a seed no adopter's hygiene gate admits, remedy strings that
resolve to nothing at a `scripts/` prefix, a partial rollback that reverts a receipt row whose file
did not revert, and an outbox nothing drains.

## Expected improvements

- A kit whose check reds on a step this run declined is reported, never rolled back.
- Renders, `.gitattributes` pins and gate legs all land on `update --write` alone.
- A failed restore keeps its receipt row forward and names the path it could not restore.
- gate-lint stops writing into a memory tree whose gate refuses the file.
- Every shipped settings-merge remedy resolves at the prefix the adopter installed at.

## Detriments if this is not built

- lexicon, unattended and process-monitor stay un-updatable at both adopters, permanently.
- Every adopter's Skills, protocols and byte-comparing CI stay one vintage behind on each pull.
- A failed restore keeps leaving the receipt disagreeing with the tree, silently.
- Adopters keep landing gov's seed with `--no-verify`, or not at all.
- Each new gate leg keeps needing a hand-run `apply` that overwrites their local forks.

## Build-level rules

- **Owner answers, 2026-09-16, one turn.** All six phases of the fix plan are in scope, and the
  leg-emission stage is built here rather than deferred: `-13` reuses `-10`'s write stage.
- **Three ordering constraints, spelled as ids because the `#` column is a position and not a rank
  (§2).** `GOVKIT_RERENDER` may not flip until `DEPL-cMendedVintage-6` lands — the eleventh
  dPolishedVitrine row records that the regenerate DELETES fixture records govkit ships as engine
  rows, so flipping first arms a known data-loss defect at every adopter (M3 veto 3).
  `DEPL-cMendedVintage-8` reds this repo until `TOOL-cMendedVintage-1` lands `--render`.
  `DEPL-cMendedVintage-11` reds every adopter whose pins moved until `DEPL-cMendedVintage-10` ships
  beside it. A first cut spelled all three positionally and every one was wrong once the roster was
  sorted into the order they demand.
- **Mixed roster.** govkit engine units are `DEPL`, units under `tools/<kit>/` are `TOOL`. One build,
  because every `TOOL` unit exists only to satisfy the deployer's update contract.
- **gov does not dogfood govkit** — no `.governance/install.json` here — so nearly every acceptance
  is a selftest arm over a fixture, never a live install. A unit whose criterion cannot be observed
  in this repo says so in its own §6.
- **Classification at open**: all 23 MISSING; specced by the harness's SPEC stage.
- **Spec-audit round 1 disposal, 2026-09-16, BUILD-METHOD M4 by severity.** The round exited BOUNDED
  with 14 confirmed findings collapsing to 13 report rows, 1 blocker and 6 highs. Every blocker and
  high was PROMOTED to a unit of its own — orders 24 through 30, each sequenced after the unit whose
  finding it closes — and the six mediums were FOLDED as rev-2 bumps into `TOOL-cMendedVintage-1`,
  `DEPL-cMendedVintage-4`, `TOOL-cMendedVintage-6`, `DEPL-cMendedVintage-2` and
  `TOOL-cMendedVintage-9`. Nothing was parked, waived, retired or re-reviewed, and the seven
  promotions are unreviewed by definition, so the next audit takes them as its subject.
  `TOOL-cMendedVintage-5` also took a rev-2 for a hygiene check 12 red found while disposing; it is
  not a review finding and is recorded in that spec's own §9.
- **The memory gate is RED at BASE by construction and clears at the SPEC pass**: check 21 on the
  mandate record's `Serves:` line, check 14 on the cited-but-undefined ids. `RECORD_UNBOUND_PIN` is
  at its floor, so the record could not be written unbound. Observed before the push, not after.

## Parked decisions

(none yet)

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-cMendedVintage-9` | OPEN | `--card --write` resolves its session id without blocking on an open stdin |
| 2 | `DEPL-cMendedVintage-1` | OPEN | no rollback over a step this run declined; the declines print unconditionally |
| 3 | `DEPL-cMendedVintage-2` | OPEN | a failed restore keeps its receipt row forward and is named in the order |
| 4 | `DEPL-cMendedVintage-3` | OPEN | the coverage tail joins each open gap to its own refusal reason |
| 5 | `DEPL-cMendedVintage-4` | OPEN | the unattributed remedy names `--re-adopt --pin`; `--allow-ungraded` retired |
| 6 | `DEPL-cMendedVintage-5` | OPEN | `[[regenerate]]` for lexicon, drift-audit and memory-recall, with lexicon's `[[outcome]]` |
| 7 | `TOOL-cMendedVintage-1` | OPEN | `adopt-memory-tree.sh --render`, the one adopter with no render path |
| 8 | `DEPL-cMendedVintage-6` | OPEN | the regenerate stops deleting the fixture records govkit ships as engine rows |
| 9 | `DEPL-cMendedVintage-7` | OPEN | `GOVKIT_RERENDER` defaults ON; the two off-path selftest arms pin it `0` |
| 10 | `DEPL-cMendedVintage-8` | OPEN | a descriptor shipping `rendered` rows and declaring no `[[regenerate]]` reds `selfcheck` |
| 11 | `TOOL-cMendedVintage-2` | OPEN | `sh_hygiene.py` takes an optional registry; gate-lint stops seeding into the memory tree |
| 12 | `DEPL-cMendedVintage-9` | OPEN | no descriptor destination may resolve under `{memory_root}/project/` |
| 13 | `TOOL-cMendedVintage-3` | OPEN | `check-wiring.sh`'s boundary walk can produce the empty prefix its comment declares legal |
| 14 | `TOOL-cMendedVintage-4` | OPEN | the three settings-merge remedies resolve at the install prefix |
| 15 | `TOOL-cMendedVintage-5` | OPEN | the carried predicate sees a `${VAR:-tools/…}` default-value literal |
| 16 | `DEPL-cMendedVintage-10` | OPEN | `update --write` writes the `.gitattributes` block and takes the renormalize with it |
| 17 | `DEPL-cMendedVintage-11` | OPEN | `cmd_check` grades the attributes row's block |
| 18 | `DEPL-cMendedVintage-12` | OPEN | `apply`'s CONFIGURE honours `deploy["inert"]` |
| 19 | `DEPL-cMendedVintage-13` | OPEN | `update --write` emits gate legs, on unit 10's write stage |
| 20 | `DEPL-cMendedVintage-14` | OPEN | stale conflict orders are reaped; an order filename keys on the full path |
| 21 | `TOOL-cMendedVintage-6` | OPEN | `check-receipt.sh`, the receipt-sync leg, and its row on gov's own bar |
| 22 | `TOOL-cMendedVintage-7` | OPEN | that leg reports rows carrying `evidence: "unattributed"` |
| 23 | `TOOL-cMendedVintage-8` | OPEN | process-monitor's empty-live-scope arm gets a code distinct from a conf refusal |
| 24 | `DEPL-cMendedVintage-15` | OPEN | the synthesized `attributes` snapshot entry is restorable and leaves the orphan sweep |
| 25 | `DEPL-cMendedVintage-16` | OPEN | the lexicon `[[outcome]]` cannot accept a failed first scaffold |
| 26 | `DEPL-cMendedVintage-17` | OPEN | a withdrawn pin set takes its own verdict, never the empty-marker write |
| 27 | `DEPL-cMendedVintage-18` | OPEN | a withdrawn row whose path did not restore stays in the receipt |
| 28 | `DEPL-cMendedVintage-19` | OPEN | a row's role is re-resolved at every schema, so a role move is reported |
| 29 | `DEPL-cMendedVintage-20` | OPEN | a retired flag's absence is graded under every spelling it has |
| 30 | `DEPL-cMendedVintage-21` | OPEN | one atomic-write helper, with an observer that fails when it is absent |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 30 unit(s) · node c · opened 2026-09-16 · streams deployer+tooling
ids DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13
ids DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5
ids TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-cMendedVintage-9 — the card verbs resolve a session id without blocking on an open stdin](spec/2026-09-16-spec-TOOL-cMendedVintage-9.md) | 1 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-1 — no rollback over a render step this run declined](spec/2026-09-16-spec-DEPL-cMendedVintage-1.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-2 — a failed restore keeps its receipt row forward, and the order names the path](spec/2026-09-16-spec-DEPL-cMendedVintage-2.md) | 3 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-3 — the coverage tail joins each open gap to its own refusal reason](spec/2026-09-16-spec-DEPL-cMendedVintage-3.md) | 4 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-4 — the unattributed remedy names a command that works, and the override retires](spec/2026-09-16-spec-DEPL-cMendedVintage-4.md) | 5 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-5 — `[[regenerate]]` for the three kits whose adopter already renders](spec/2026-09-16-spec-DEPL-cMendedVintage-5.md) | 6 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-1 — `adopt-memory-tree.sh --render`, the one adopter with no render path](spec/2026-09-16-spec-TOOL-cMendedVintage-1.md) | 7 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-6 — the fixture records are rendered per prefix, so nothing deletes them](spec/2026-09-16-spec-DEPL-cMendedVintage-6.md) | 8 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-7 — `GOVKIT_RERENDER` defaults ON, and `=0` becomes the revert](spec/2026-09-16-spec-DEPL-cMendedVintage-7.md) | 9 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-8 — a descriptor shipping `rendered` rows must declare a regenerate](spec/2026-09-16-spec-DEPL-cMendedVintage-8.md) | 10 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-2 — gate-lint stops seeding into the memory tree](spec/2026-09-16-spec-TOOL-cMendedVintage-2.md) | 11 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-9 — no descriptor destination under `{memory_root}/project/`](spec/2026-09-16-spec-DEPL-cMendedVintage-9.md) | 12 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-3 — `check-wiring.sh`'s boundary walk can produce the empty prefix it declares legal](spec/2026-09-16-spec-TOOL-cMendedVintage-3.md) | 13 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-4 — the three settings-merge remedies resolve at the install prefix](spec/2026-09-16-spec-TOOL-cMendedVintage-4.md) | 14 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [TOOL-cMendedVintage-5 — the carried predicate sees a `${VAR:-tools/…}` default](spec/2026-09-16-spec-TOOL-cMendedVintage-5.md) | 15 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-10 — `update --write` writes the `.gitattributes` block, with the renormalize](spec/2026-09-16-spec-DEPL-cMendedVintage-10.md) | 16 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-11 — `cmd_check` grades the attributes row's block](spec/2026-09-16-spec-DEPL-cMendedVintage-11.md) | 17 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-12 — `apply`'s CONFIGURE honours `deploy["inert"]`](spec/2026-09-16-spec-DEPL-cMendedVintage-12.md) | 18 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-13 — `update --write` emits gate legs](spec/2026-09-16-spec-DEPL-cMendedVintage-13.md) | 19 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-14 — stale conflict orders are reaped, and keyed on the full path](spec/2026-09-16-spec-DEPL-cMendedVintage-14.md) | 20 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [TOOL-cMendedVintage-6 — the receipt-sync leg, and its row on gov's own bar](spec/2026-09-16-spec-TOOL-cMendedVintage-6.md) | 21 | 2 | SPECCED | rev-3 | 2026-09-16 |
| [TOOL-cMendedVintage-7 — the receipt leg reports rows carrying `evidence: "unattributed"`](spec/2026-09-16-spec-TOOL-cMendedVintage-7.md) | 22 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-8 — the empty-live-scope case gets a code distinct from a conf refusal](spec/2026-09-16-spec-TOOL-cMendedVintage-8.md) | 23 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-15 — the synthesized attributes entry is restorable, and no orphan line names it](spec/2026-09-16-spec-DEPL-cMendedVintage-15.md) | 24 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-16 — the lexicon outcome block cannot accept a failed first scaffold](spec/2026-09-16-spec-DEPL-cMendedVintage-16.md) | 25 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-17 — a target whose pins were withdrawn never reaches the empty-marker write](spec/2026-09-16-spec-DEPL-cMendedVintage-17.md) | 26 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-18 — a withdrawn row whose path did not restore stays in the receipt](spec/2026-09-16-spec-DEPL-cMendedVintage-18.md) | 27 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-19 — a row's role is re-resolved at every schema, so a role move is reported](spec/2026-09-16-spec-DEPL-cMendedVintage-19.md) | 28 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-20 — a retired flag's absence is graded under every spelling it has](spec/2026-09-16-spec-DEPL-cMendedVintage-20.md) | 29 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-21 — the atomic write is one helper, and something fails when it is absent](spec/2026-09-16-spec-DEPL-cMendedVintage-21.md) | 30 | 2 | SPECCED | rev-1 | 2026-09-16 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21.

Ids no `spec-audit` record has ever named: DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-cMendedVintage-9` | no |
| 2 | `DEPL-cMendedVintage-1` | no |
| 3 | `DEPL-cMendedVintage-2` | no |
| 4 | `DEPL-cMendedVintage-3` | no |
| 5 | `DEPL-cMendedVintage-4` | no |
| 6 | `DEPL-cMendedVintage-5` | no |
| 7 | `TOOL-cMendedVintage-1` | no |
| 8 | `DEPL-cMendedVintage-6` | no |
| 9 | `DEPL-cMendedVintage-7` | no |
| 10 | `DEPL-cMendedVintage-8` | no |
| 11 | `TOOL-cMendedVintage-2` | no |
| 12 | `DEPL-cMendedVintage-9` | no |
| 13 | `TOOL-cMendedVintage-3` | no |
| 14 | `TOOL-cMendedVintage-4` | no |
| 15 | `TOOL-cMendedVintage-5` | no |
| 16 | `DEPL-cMendedVintage-10` | no |
| 17 | `DEPL-cMendedVintage-11` | no |
| 18 | `DEPL-cMendedVintage-12` | no |
| 19 | `DEPL-cMendedVintage-13` | no |
| 20 | `DEPL-cMendedVintage-14` | no |
| 21 | `TOOL-cMendedVintage-6` | no |
| 22 | `TOOL-cMendedVintage-7` | no |
| 23 | `TOOL-cMendedVintage-8` | no |
| 24 | `DEPL-cMendedVintage-15` | no |
| 25 | `DEPL-cMendedVintage-16` | no |
| 26 | `DEPL-cMendedVintage-17` | no |
| 27 | `DEPL-cMendedVintage-18` | no |
| 28 | `DEPL-cMendedVintage-19` | no |
| 29 | `DEPL-cMendedVintage-20` | no |
| 30 | `DEPL-cMendedVintage-21` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
