# TOOL-dWellOiledMachine-92 — the lifted node lock handed to TOOL-dPlacedRequest-24 and -11 by an ask row, and unit 83's claim on their contract withdrawn

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 31 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-92-deviation-921.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-92-deviation-921.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-91-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-91-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-2 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md`),
finding 22, item H2, at HIGH. TOOL-dWellOiledMachine-83 S1 mints
`write_node_lock <dir> <owner> <until-epoch> <event-stem> [stale-fn]` in
`tools/unattended/lib-unattended.sh`, and its §8 F1 asserts that TOOL-dPlacedRequest-24 "re-points to
this library". That unit, DEFERRED in another build, still defines a two-argument
`write_node_lock <dir> <owner token>` in the `gov_feed_sh` block with fixed `node-lock-broken` events,
and TOOL-dPlacedRequest-11 S6 still deletes the three claim-push functions 83 moves. No ask row and no
edge tells either unit. `unattended.sh` sources the library and dPR-24 AC6 inlines `gov_feed_sh` into
it, so if dPR-24 builds as written both definitions land in one shell and the later one drops the
deadline, the stem and the stale test the supervisor's start claim needs: the double start 83 closes
returns. This unit files the hand-off where the other build reads it, and restates 83 so it claims
nothing about that build's contract.

## 2. Scope (IN)

- **S1** — The ask row. `memory/builds/dPlacedRequest/BACKLOG.md` gains one ask row under `## Asks`, in
  the grammar of its existing rows (`memory/builds/dPlacedRequest/BACKLOG.md:6`), its id the next free
  `TOOL-dPlacedRequest` id, the numeric maximum of that family's ids in the tree plus one, derived at
  this unit's pass (72 at this spec's writing). Its title reads `THE NODE LOCK IS ALREADY LIFTED.` Its
  text names TOOL-dWellOiledMachine-83 S1's library factory and its signature
  `write_node_lock <dir> <owner> <until-epoch> <event-stem> [stale-fn]`, with `remove_node_lock` and
  `check_node_lock_stale` and the events `<stem>-lock-broken` and `<stem>-guard-cleared`. It asks
  TOOL-dPlacedRequest-24 S1 and AC6 to take that factory and signature, either by sourcing the library
  or by moving it into `gov_feed_sh` unchanged and deleting the library's copy, and
  TOOL-dPlacedRequest-11 S6 to delete the claim-push call sites of the factory and the `claim-push`
  stem rather than the three functions 83 removed. Its `accept` clause reads: every carrier defining
  `write_node_lock` defines it with 83 S1's five parameters, and no shell sources two definitions.
  `## Dispositions` gains `- SEV · <that id> · HIGH · a second write_node_lock definition drops the
  supervisor start claim's deadline and stale test, and two supervisors start`. Observed by AC1, AC3.
  **Readers:** by name: `memory/builds/dPlacedRequest/BACKLOG.md`, the file the row lands in. by value: NO VALUE READERS — an ask row is read by the backlog fold and the index generator, which read every row alike.
- **S2** — 83's claim withdrawn. Spec 83 takes a rev bump at this unit's pass: §8 F1's sentence "so
  TOOL-dPlacedRequest-24 re-points to this library rather than minting" becomes "the re-point of
  TOOL-dPlacedRequest-24 and -11 is asked by the row TOOL-dWellOiledMachine-92 files, and their
  contract is theirs to change"; §3's last non-goal names that ask row; and §3 Edges gains
  `- **hands-off** external — TOOL-dPlacedRequest-24 S1 and AC6 and TOOL-dPlacedRequest-11 S6, asked by
  the dPlacedRequest ask row TOOL-dWellOiledMachine-92 files to take the lifted factory`. Its §9 line
  names this unit and finding 22. Observed by AC2.

## 3. Non-goals (OUT)

- No edit to TOOL-dPlacedRequest-24's or -11's spec: they belong to another build, and README rule
  "Writes stay in this build's folder" admits only an ask row outside it.
- No change to 83's factory, its signature or its call sites.
- No lint over specs asserting another build's re-point: a separate mechanism (M2), named by the
  report's left-shift line and not built here.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-83` — S1's lifted factory and its signature, which the ask row hands to TOOL-dPlacedRequest-24 and -11, and §8 F1, which this unit restates
- **hands-off** `TOOL-dWellOiledMachine-97` — S1's ask row, its content key and its caller list, AC1, Files touched and §4 Evidence, amended before this unit builds (round-3 promotions audit, findings 16, 17, 21 and 30)

## 4. Design

### Evidence

- dPR-24 (DEFERRED, rev-4) S1 defines `write_node_lock <dir> <owner token>` in the `gov_feed_sh` block,
  built from the claim-push bodies, with events `node-lock-broken` and `node-lock-guard-cleared`
  (`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:40-52`), and AC6
  requires the inline block in `unattended.sh` (`:194-196`).
- dPR-11 (DEFERRED, rev-3) S6 deletes the lander lock and spells the three functions
  (`memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-11.md:59-62`).
- `unattended.sh` sources `lib-unattended.sh` (`tools/unattended/unattended.sh:96-101`).
- 83 F1 asserts the re-point (`spec-83.md:152-159`) and 83's Edges name only TOOL-dWellOiledMachine-78
  and TOOL-aGraftedHelix-37 (`spec-83.md:71-72`).
- Every ask row in a build's `BACKLOG.md` carries that build's own slug: a scan of every
  `memory/builds/*/BACKLOG.md` on 2026-10-27 found no row filed under another slug, so the row takes a
  `TOOL-dPlacedRequest` id.
- The build README admits, outside this build's folder, "only an ask row in another build's
  `BACKLOG.md` and the shared renders" (`memory/builds/dWellOiledMachine/README.md:53-54`); the line
  numbers are PINNED at this spec's writing, and the README's generated regions move them.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| the next free `TOOL-dPlacedRequest` id | ask row in `memory/builds/dPlacedRequest/BACKLOG.md` | none |

### Files touched (estimate)

- `memory/builds/dPlacedRequest/BACKLOG.md`: S1
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-83.md`: S2's rev bump

### Alternatives rejected

- **Renaming 83's factory so the two never collide.** Two spellings of one factory is the drift the
  charter's reuse rule stops; the names are dPR-24's and the signature is the one the supervisor claim
  needs.
- **Withdrawing 83's claim alone, with no ask.** dPR-24 would still build its copy and the collision
  would land at that build; the ask is the one record the other build's run reads.

## 5. Production-readiness checklist

- security — keeps the supervisor start claim's exclusivity once dPR-24 builds; no surface added.
- perf / scale — N/A — a record and a spec text change.
- error / empty / loading states — N/A — no runtime path.
- observability — the ask row shows in `gen_build_index.py --asks` for dPlacedRequest.
- risks — dPR-24's run may answer the ask either way S1 offers; both keep one definition per shell.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

- **AC1** — When `grep -n "write_node_lock <dir> <owner> <until-epoch> <event-stem>" memory/builds/dPlacedRequest/BACKLOG.md`
  runs, it prints the new ask row, and `grep -n "SEV · TOOL-dPlacedRequest-" memory/builds/dPlacedRequest/BACKLOG.md`
  prints its disposition row naming the same id.
  Red when: no ask row hands the factory to the other build.
- **AC2** — When `grep -c "re-points to this library" 2026-10-27-spec-TOOL-dWellOiledMachine-83.md` runs
  over spec 83 it prints 0, and `grep -n "hands-off\*\* external" 2026-10-27-spec-TOOL-dWellOiledMachine-83.md`
  prints a line naming `TOOL-dPlacedRequest-24`.
  Red when: 83 still claims the other build's contract or carries no hand-off to it.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --asks --build dPlacedRequest` runs, it
  lists the new ask's id.
  Red when: the row's grammar is refused and the ask is invisible to the other build's run.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-2 promotions, finding
  22 (H2).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-3
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-97.

## 10. Reuse audit

The seam is the builds-mode ask row (`memory/HYGIENE.md`, `builds` layout, and the rows of
`memory/builds/dPlacedRequest/BACKLOG.md`), the one record a build's run reads for work another build
hands it; no new record kind is minted. The probe
`python tools/codebase-map/reuse_lookup.py "hand a contract change to another build's deferred unit"`
ranked `build`, `units`, `changed` and `build_commit` by name stem, none a hand-off, because an ask is
a record rather than a symbol; the recall query below ranked TOOL-dPlacedRequest-36, which writes
dPR-24's lock events, and TOOL-dPlacedRequest-24 itself among its first five hits, the units this row
reaches.

Recall terms used: `python tools/memory-recall/query.py "who owns the node lock factory write_node_lock"
--terms "write_node_lock node lock factory gov_feed_sh claim-push lib-unattended ask row hand-off
dPlacedRequest"`
