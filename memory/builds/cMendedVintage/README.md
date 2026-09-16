---
slug: cMendedVintage
node: c
opened: 2026-09-16
streams: deployer+tooling
roster: DEPL+TOOL
status: OPEN
authorized-by: prompt
ids: DEPL-cMendedVintage-1
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

- **Owner answers, 2026-09-16, one turn.** All six phases of the delivered fix plan are in scope,
  and the leg-emission stage is built in this run rather than deferred — it reuses unit 10's write
  stage, which is why it is sequenced after it.
- **`GOVKIT_RERENDER` may not flip until unit 6 lands.** `TOOL-dPolishedVitrine-11` records that the
  regenerate DELETES fixture records govkit ships as engine rows. Flipping the default first turns a
  recorded data-loss defect on for every adopter, which is M3's veto 3.
- **Two gates may not precede their remedy.** Unit 8 reds this repo until unit 1b lands
  `--render`; unit 11 reds every adopter whose pins moved until unit 10 ships in the same release.
- **Mixed roster, by construction.** The govkit engine units are `DEPL`; the units in `tools/<kit>/`
  are `TOOL`. The build is one build because every `TOOL` unit exists only to satisfy the deployer's
  update contract.
- **gov does not dogfood govkit** — no `.governance/install.json` in this tree — so almost every
  acceptance here is a selftest arm over a fixture, never an observation of a live install. Units
  whose criterion cannot be observed in this repo say so in their own §6 rather than implying more.
- **Classification at open**: all 22 MISSING; specced by the harness's SPEC stage.
- **The memory gate is RED at this commit, by construction, and clears at the SPEC pass.** Check 21
  reds because the mandate record's `Serves:` names a unit id no spec H1 defines yet, and check 14
  reds on all 22 cited-but-undefined ids. `RECORD_UNBOUND_PIN` sits at its floor, so the `none` form
  is unavailable and the record cannot be written unbound. Observed before the push, not after it.

## Parked decisions

(none yet)

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `DEPL-cMendedVintage-1` | OPEN | no rollback over a step this run declined; the declines print unconditionally |
| 2 | `DEPL-cMendedVintage-2` | OPEN | a failed restore keeps its receipt row forward and is named in the order |
| 3 | `DEPL-cMendedVintage-3` | OPEN | the coverage tail joins each open gap to its own refusal reason |
| 4 | `DEPL-cMendedVintage-4` | OPEN | the unattributed remedy names `--re-adopt --pin`; `--allow-ungraded` retired |
| 5 | `DEPL-cMendedVintage-5` | OPEN | `[[regenerate]]` for lexicon, drift-audit and memory-recall, with lexicon's `[[outcome]]` |
| 6 | `DEPL-cMendedVintage-6` | OPEN | the regenerate stops deleting the fixture records govkit ships as engine rows |
| 7 | `DEPL-cMendedVintage-7` | OPEN | `GOVKIT_RERENDER` defaults ON; the two off-path selftest arms pin it `0` |
| 8 | `DEPL-cMendedVintage-8` | OPEN | a descriptor shipping `rendered` rows and declaring no `[[regenerate]]` reds `selfcheck` |
| 9 | `DEPL-cMendedVintage-9` | OPEN | no descriptor destination may resolve under `{memory_root}/project/` |
| 10 | `DEPL-cMendedVintage-10` | OPEN | `update --write` writes the `.gitattributes` block and takes the renormalize with it |
| 11 | `DEPL-cMendedVintage-11` | OPEN | `cmd_check` grades the attributes row's block |
| 12 | `DEPL-cMendedVintage-12` | OPEN | `apply`'s CONFIGURE honours `deploy["inert"]` |
| 13 | `DEPL-cMendedVintage-13` | OPEN | `update --write` emits gate legs, on unit 10's write stage |
| 14 | `DEPL-cMendedVintage-14` | OPEN | stale conflict orders are reaped; an order filename keys on the full path |
| 15 | `TOOL-cMendedVintage-1` | OPEN | `adopt-memory-tree.sh --render`, the one adopter with no render path |
| 16 | `TOOL-cMendedVintage-2` | OPEN | `sh_hygiene.py` takes an optional registry; gate-lint stops seeding into the memory tree |
| 17 | `TOOL-cMendedVintage-3` | OPEN | `check-wiring.sh`'s boundary walk can produce the empty prefix its comment declares legal |
| 18 | `TOOL-cMendedVintage-4` | OPEN | the three settings-merge remedies resolve at the install prefix |
| 19 | `TOOL-cMendedVintage-5` | OPEN | the carried predicate sees a `${VAR:-tools/…}` default-value literal |
| 20 | `TOOL-cMendedVintage-6` | OPEN | `check-receipt.sh`, the receipt-sync leg, and its row on gov's own bar |
| 21 | `TOOL-cMendedVintage-7` | OPEN | that leg reports rows carrying `evidence: "unattributed"` |
| 22 | `TOOL-cMendedVintage-8` | OPEN | process-monitor's empty-live-scope arm gets a code distinct from a conf refusal |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node c · opened 2026-09-16 · streams deployer+tooling
ids DEPL-cMendedVintage-1

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
