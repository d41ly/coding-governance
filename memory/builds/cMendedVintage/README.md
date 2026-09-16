---
slug: cMendedVintage
node: c
opened: 2026-09-16
streams: deployer+tooling
roster: DEPL+TOOL
status: OPEN
authorized-by: prompt
ids: DEPL-cMendedVintage-1 TOOL-cMendedVintage-9
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

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node c · opened 2026-09-16 · streams deployer+tooling
ids DEPL-cMendedVintage-1 TOOL-cMendedVintage-9

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
