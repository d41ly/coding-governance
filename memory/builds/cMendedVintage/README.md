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

- **Owner answers, 2026-09-16, one turn.** All six phases in scope; leg emission is built here
  rather than deferred, and `-13` reuses `-10`'s write stage.
- **Four ordering constraints, spelled as ids because `#` is a position and not a rank (§2).**
  `GOVKIT_RERENDER` may not flip until `DEPL-cMendedVintage-6` lands: the regenerate DELETES fixture
  records govkit ships as engine rows (M3 veto 3). `DEPL-cMendedVintage-8` reds this repo until
  `TOOL-cMendedVintage-1` ships `--render`. `DEPL-cMendedVintage-11` reds every adopter whose pins
  moved unless `DEPL-cMendedVintage-10` ships beside it. `DEPL-cMendedVintage-16` must follow
  `DEPL-cMendedVintage-5` at once, because `classify_outcome` reads the kit-level outcome list
  unscoped, so `apply`'s CONFIGURE consults it and a failed lexicon first scaffold reports as adopted
  from the moment `-5` lands.
- **`order` moves without a rev bump.** Enforcing the constraint above moved `-16` from 25 to 7 and
  shifted 7-24 up one. `order` is sequencing metadata, not design; this sentence records all nineteen.
- **Mixed roster.** govkit engine units are `DEPL`, units under `tools/<kit>/` are `TOOL`. One build:
  every `TOOL` unit exists only to satisfy the deployer's update contract.
- **gov does not dogfood govkit** — no `.governance/install.json` here — so nearly every acceptance is
  a fixture arm, never a live install. A unit whose criterion cannot be observed here says so in §6.
- **Spec-audit round 1, BOUNDED.** 14 confirmed findings collapsed to 13 rows; 1 blocker and 6 highs
  PROMOTED to units of their own, 6 mediums FOLDED as rev-2 bumps. Nothing parked, waived or
  re-reviewed. The promotions are unreviewed by definition and are the next audit's subject.

## Parked decisions

(none yet)

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-cMendedVintage-9` | CLOSED | `--card --write` resolves its session id without blocking on an open stdin |
| 2 | `DEPL-cMendedVintage-1` | CLOSED | no rollback over a step this run declined; the declines print unconditionally |
| 3 | `DEPL-cMendedVintage-2` | CLOSED | a failed restore keeps its receipt row forward and is named in the order |
| 4 | `DEPL-cMendedVintage-3` | CLOSED | the coverage tail joins each open gap to its own refusal reason |
| 5 | `DEPL-cMendedVintage-4` | CLOSED | the unattributed remedy names `--re-adopt --pin`; `--allow-ungraded` retired |
| 6 | `DEPL-cMendedVintage-5` | OPEN | `[[regenerate]]` for lexicon, drift-audit and memory-recall, with lexicon's `[[outcome]]` |
| 7 | `DEPL-cMendedVintage-16` | OPEN | the lexicon `[[outcome]]` cannot accept a failed first scaffold |
| 8 | `TOOL-cMendedVintage-1` | OPEN | `adopt-memory-tree.sh --render`, the one adopter with no render path |
| 9 | `DEPL-cMendedVintage-6` | OPEN | the regenerate stops deleting the fixture records govkit ships as engine rows |
| 10 | `DEPL-cMendedVintage-7` | OPEN | `GOVKIT_RERENDER` defaults ON; the two off-path selftest arms pin it `0` |
| 11 | `DEPL-cMendedVintage-8` | OPEN | a descriptor shipping `rendered` rows and declaring no `[[regenerate]]` reds `selfcheck` |
| 12 | `TOOL-cMendedVintage-2` | OPEN | `sh_hygiene.py` takes an optional registry; gate-lint stops seeding into the memory tree |
| 13 | `DEPL-cMendedVintage-9` | OPEN | no descriptor destination may resolve under `{memory_root}/project/` |
| 14 | `TOOL-cMendedVintage-3` | OPEN | `check-wiring.sh`'s boundary walk can produce the empty prefix its comment declares legal |
| 15 | `TOOL-cMendedVintage-4` | OPEN | the three settings-merge remedies resolve at the install prefix |
| 16 | `TOOL-cMendedVintage-5` | OPEN | the carried predicate sees a `${VAR:-tools/…}` default-value literal |
| 17 | `DEPL-cMendedVintage-10` | OPEN | `update --write` writes the `.gitattributes` block and takes the renormalize with it |
| 18 | `DEPL-cMendedVintage-11` | OPEN | `cmd_check` grades the attributes row's block |
| 19 | `DEPL-cMendedVintage-12` | OPEN | `apply`'s CONFIGURE honours `deploy["inert"]` |
| 20 | `DEPL-cMendedVintage-13` | OPEN | `update --write` emits gate legs, on unit 10's write stage |
| 21 | `DEPL-cMendedVintage-14` | OPEN | stale conflict orders are reaped; an order filename keys on the full path |
| 22 | `TOOL-cMendedVintage-6` | OPEN | `check-receipt.sh`, the receipt-sync leg, and its row on gov's own bar |
| 23 | `TOOL-cMendedVintage-7` | OPEN | that leg reports rows carrying `evidence: "unattributed"` |
| 24 | `TOOL-cMendedVintage-8` | OPEN | process-monitor's empty-live-scope arm gets a code distinct from a conf refusal |
| 25 | `DEPL-cMendedVintage-15` | OPEN | the synthesized `attributes` snapshot entry is restorable and leaves the orphan sweep |
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
| [TOOL-cMendedVintage-9 — the card verbs resolve a session id without blocking on an open stdin](spec/2026-09-16-spec-TOOL-cMendedVintage-9.md) | 1 | 2 | CLOSED | rev-4 | 2026-09-16 |
| [DEPL-cMendedVintage-1 — no rollback over a render step this run declined](spec/2026-09-16-spec-DEPL-cMendedVintage-1.md) | 2 | 2 | CLOSED | rev-3 | 2026-09-16 |
| [DEPL-cMendedVintage-2 — a failed restore keeps its receipt row forward, and the order names the path](spec/2026-09-16-spec-DEPL-cMendedVintage-2.md) | 3 | 2 | CLOSED | rev-3 | 2026-09-16 |
| [DEPL-cMendedVintage-3 — the coverage tail joins each open gap to its own refusal reason](spec/2026-09-16-spec-DEPL-cMendedVintage-3.md) | 4 | 2 | CLOSED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-4 — the unattributed remedy names a command that works, and the override retires](spec/2026-09-16-spec-DEPL-cMendedVintage-4.md) | 5 | 2 | CLOSED | rev-3 | 2026-09-16 |
| [DEPL-cMendedVintage-5 — `[[regenerate]]` for the three kits whose adopter already renders](spec/2026-09-16-spec-DEPL-cMendedVintage-5.md) | 6 | 2 | CLOSED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-16 — the lexicon outcome block cannot accept a failed first scaffold](spec/2026-09-16-spec-DEPL-cMendedVintage-16.md) | 7 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-1 — `adopt-memory-tree.sh --render`, the one adopter with no render path](spec/2026-09-16-spec-TOOL-cMendedVintage-1.md) | 8 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-6 — the fixture records are rendered per prefix, so nothing deletes them](spec/2026-09-16-spec-DEPL-cMendedVintage-6.md) | 9 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-7 — `GOVKIT_RERENDER` defaults ON, and `=0` becomes the revert](spec/2026-09-16-spec-DEPL-cMendedVintage-7.md) | 10 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-8 — a descriptor shipping `rendered` rows must declare a regenerate](spec/2026-09-16-spec-DEPL-cMendedVintage-8.md) | 11 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-2 — gate-lint stops seeding into the memory tree](spec/2026-09-16-spec-TOOL-cMendedVintage-2.md) | 12 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-9 — no descriptor destination under `{memory_root}/project/`](spec/2026-09-16-spec-DEPL-cMendedVintage-9.md) | 13 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-3 — `check-wiring.sh`'s boundary walk can produce the empty prefix it declares legal](spec/2026-09-16-spec-TOOL-cMendedVintage-3.md) | 14 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-4 — the three settings-merge remedies resolve at the install prefix](spec/2026-09-16-spec-TOOL-cMendedVintage-4.md) | 15 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [TOOL-cMendedVintage-5 — the carried predicate sees a `${VAR:-tools/…}` default](spec/2026-09-16-spec-TOOL-cMendedVintage-5.md) | 16 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-10 — `update --write` writes the `.gitattributes` block, with the renormalize](spec/2026-09-16-spec-DEPL-cMendedVintage-10.md) | 17 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-11 — `cmd_check` grades the attributes row's block](spec/2026-09-16-spec-DEPL-cMendedVintage-11.md) | 18 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-12 — `apply`'s CONFIGURE honours `deploy["inert"]`](spec/2026-09-16-spec-DEPL-cMendedVintage-12.md) | 19 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-13 — `update --write` emits gate legs](spec/2026-09-16-spec-DEPL-cMendedVintage-13.md) | 20 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-14 — stale conflict orders are reaped, and keyed on the full path](spec/2026-09-16-spec-DEPL-cMendedVintage-14.md) | 21 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [TOOL-cMendedVintage-6 — the receipt-sync leg, and its row on gov's own bar](spec/2026-09-16-spec-TOOL-cMendedVintage-6.md) | 22 | 2 | SPECCED | rev-3 | 2026-09-16 |
| [TOOL-cMendedVintage-7 — the receipt leg reports rows carrying `evidence: "unattributed"`](spec/2026-09-16-spec-TOOL-cMendedVintage-7.md) | 23 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [TOOL-cMendedVintage-8 — the empty-live-scope case gets a code distinct from a conf refusal](spec/2026-09-16-spec-TOOL-cMendedVintage-8.md) | 24 | 2 | SPECCED | rev-2 | 2026-09-16 |
| [DEPL-cMendedVintage-15 — the synthesized attributes entry is restorable, and no orphan line names it](spec/2026-09-16-spec-DEPL-cMendedVintage-15.md) | 25 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-17 — a target whose pins were withdrawn never reaches the empty-marker write](spec/2026-09-16-spec-DEPL-cMendedVintage-17.md) | 26 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-18 — a withdrawn row whose path did not restore stays in the receipt](spec/2026-09-16-spec-DEPL-cMendedVintage-18.md) | 27 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-19 — a row's role is re-resolved at every schema, so a role move is reported](spec/2026-09-16-spec-DEPL-cMendedVintage-19.md) | 28 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-20 — a retired flag's absence is graded under every spelling it has](spec/2026-09-16-spec-DEPL-cMendedVintage-20.md) | 29 | 2 | SPECCED | rev-1 | 2026-09-16 |
| [DEPL-cMendedVintage-21 — the atomic write is one helper, and something fails when it is absent](spec/2026-09-16-spec-DEPL-cMendedVintage-21.md) | 30 | 2 | SPECCED | rev-1 | 2026-09-16 |
<!-- /gen:build-units -->

Records: 10 bound to this build, across 4 record folder(s).

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
| 7 | `DEPL-cMendedVintage-16` | no |
| 8 | `TOOL-cMendedVintage-1` | no |
| 9 | `DEPL-cMendedVintage-6` | no |
| 10 | `DEPL-cMendedVintage-7` | no |
| 11 | `DEPL-cMendedVintage-8` | no |
| 12 | `TOOL-cMendedVintage-2` | no |
| 13 | `DEPL-cMendedVintage-9` | no |
| 14 | `TOOL-cMendedVintage-3` | no |
| 15 | `TOOL-cMendedVintage-4` | no |
| 16 | `TOOL-cMendedVintage-5` | no |
| 17 | `DEPL-cMendedVintage-10` | no |
| 18 | `DEPL-cMendedVintage-11` | no |
| 19 | `DEPL-cMendedVintage-12` | no |
| 20 | `DEPL-cMendedVintage-13` | no |
| 21 | `DEPL-cMendedVintage-14` | no |
| 22 | `TOOL-cMendedVintage-6` | no |
| 23 | `TOOL-cMendedVintage-7` | no |
| 24 | `TOOL-cMendedVintage-8` | no |
| 25 | `DEPL-cMendedVintage-15` | no |
| 26 | `DEPL-cMendedVintage-17` | no |
| 27 | `DEPL-cMendedVintage-18` | no |
| 28 | `DEPL-cMendedVintage-19` | no |
| 29 | `DEPL-cMendedVintage-20` | no |
| 30 | `DEPL-cMendedVintage-21` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
