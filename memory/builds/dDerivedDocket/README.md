---
slug: dDerivedDocket
node: d
opened: 2026-09-14
streams: tooling+playbook+deployer
roster: TOOL+PLAY+DEPL
authorized-by: prompt
status: OPEN
ids: DEPL-dDerivedDocket-1 PLAY-dDerivedDocket-1 TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36
---

# dDerivedDocket — backlog asks filed per build, status derived, and unattended runs pointed at them

## The problem this build exists to solve
Backlog status is the one work-state fact this repo still authors by hand in shared files. The TOOL
shard is several times its byte cap and waived from three checks, rows outlive the specs that closed
them, and a rotation reconcile has already lost CLOSED flips. Nothing lets an unattended run be
pointed at a set of asks and carry them to LANDED. This build files each ask once in its own build
folder, derives every status from records, generates the family views, audits pre-flip branches
merged later on any node, and makes ask-driven unattended runs finish, including the kit's own
recorded stop causes.

## Expected improvements
- Backlog status cannot drift from the records that decide it; rotation and the TOOL waiver retire.
- No two sessions write one authored backlog file, and a late pre-flip merge is audited, not trusted.
- An unattended run pointed at a slug lands with no owner turn on every recorded kit-side stop class.

## Detriments if this is not built
- The TOOL shard keeps growing unchecked and closures keep getting lost in reconciles.
- Status drift stays counted rather than prevented, with no triage pressure on finished builds.
- Unattended runs keep stopping on landing state, other builds' reds and host limits.

## Build-level rules
- **The design record is the spec source**: `build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`,
  rulings in its sections 17, 20 and 22. A spec that diverges takes a rev and a section-9 line.
- **Re-ground on the pinned BASE.** Three builds landed in this territory after the design was
  measured; every claim a spec makes about current code is re-verified there.
- **Self-protection first** (D12-i11): units 1 to 5 land before the rest so this run lands through them.
- **Dark until the flip.** Every unit before 34 keeps the shards mode byte-identical; 34 is the one
  switch-over commit.
- **Delegated signing** (owner, 2026-09-14): unit 33 signs the D2 and D6 tables under the mechanical
  rules its spec states, and the D10 drain is replaced by unit 9's permanent audit.
- **Auto-resume ships on** in the kit and here, overriding charter section 9's default-off gate for
  this feature by owner ruling; unit 5 records it as a DECISIONS row.
- **Unit passes run no gates.** Unattended self-tests run only in units 1, 3, 4, 5, 16, 17, 18, 22,
  24, 27, 28 and 30 (D12-h, D12-i8), each suite once at the unit's end.

## Parked decisions

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dDerivedDocket-1` | PLANNED | held-suite failure baseline: NEW, INHERITED and FIXED failure sets |
| 2 | `TOOL-dDerivedDocket-2` | PLANNED | in-place landing merge onto the observed remote tip, with a carry-set refusal |
| 3 | `TOOL-dDerivedDocket-3` | PLANNED | the run's landing path: lander mode, prepared-merge bar, records committed at close |
| 4 | `TOOL-dDerivedDocket-4` | PLANNED | the HELD phase: hold codes, a per-slug lease, one derived phase reader |
| 5 | `TOOL-dDerivedDocket-5` | PLANNED | auto-resume from HELD, on by default |
| 6 | `TOOL-dDerivedDocket-6` | PLANNED | ask and disposition parser, and the order-free status fold with REOPEN and SEV |
| 7 | `TOOL-dDerivedDocket-7` | PLANNED | generated family view with its data-loss and mode guards and print modes |
| 8 | `TOOL-dDerivedDocket-8` | PLANNED | hygiene engine, id corpus and row grammar in builds mode |
| 9 | `TOOL-dDerivedDocket-9` | PLANNED | transition-merge audit over history and at commit time, with liveness |
| 10 | `TOOL-dDerivedDocket-10` | PLANNED | the row merge driver refuses an authored shard merged into a generated view |
| 11 | `TOOL-dDerivedDocket-11` | PLANNED | migration planner: census, same-id table, mined closures, per-id status proof |
| 12 | `TOOL-dDerivedDocket-12` | PLANNED | relocation tools for pre-flip branches, with provenance rows |
| 13 | `TOOL-dDerivedDocket-13` | PLANNED | straggler instructions in the hook bodies, and the fleet inventory signal |
| 14 | `TOOL-dDerivedDocket-14` | PLANNED | rotation-note check for shards-mode backlog archives |
| 15 | `TOOL-dDerivedDocket-15` | PLANNED | ask envelope clauses, the READY predicate and the new-build scaffold |
| 16 | `TOOL-dDerivedDocket-16` | PLANNED | driver ask-awareness: the asks key, its preflight properties, roster and plan |
| 17 | `TOOL-dDerivedDocket-17` | PLANNED | the asks-disposed Definition-of-Done item and the asks-at-landing freeze |
| 18 | `TOOL-dDerivedDocket-18` | PLANNED | leg second opinions over the ask mandate |
| 19 | `TOOL-dDerivedDocket-19` | PLANNED | authority grants only from an owner-committed README |
| 20 | `TOOL-dDerivedDocket-20` | PLANNED | unattended carriers, and the shared-record against generated-index refusal |
| 21 | `TOOL-dDerivedDocket-21` | PLANNED | remote-relative bases and complete leg guards |
| 22 | `TOOL-dDerivedDocket-22` | PLANNED | LANDED derived from the advertised tip |
| 23 | `TOOL-dDerivedDocket-23` | PLANNED | red attribution, report-only |
| 24 | `TOOL-dDerivedDocket-24` | PLANNED | inherited-red policy with its own stamp kind |
| 25 | `TOOL-dDerivedDocket-25` | PLANNED | runner scratch hygiene and a tree-moved exit |
| 26 | `TOOL-dDerivedDocket-26` | PLANNED | honest verdicts under contention |
| 27 | `TOOL-dDerivedDocket-27` | PLANNED | one declared gate wall and the driver's bound stack |
| 28 | `TOOL-dDerivedDocket-28` | PLANNED | run-owned process ledger and reaping |
| 29 | `TOOL-dDerivedDocket-29` | PLANNED | review durability across a dead workflow fan |
| 30 | `TOOL-dDerivedDocket-30` | PLANNED | the open checker defects the stop census found |
| 31 | `TOOL-dDerivedDocket-31` | PLANNED | build-method carriers for forks and delegated passes |
| 32 | `TOOL-dDerivedDocket-32` | PLANNED | remote CI: the history audit and check 9 on every push |
| 33 | `TOOL-dDerivedDocket-33` | PLANNED | delegated signing of the same-id table and the triage sweep |
| 34 | `TOOL-dDerivedDocket-34` | PLANNED | the switch-over: migration applied and the views rendered |
| 35 | `TOOL-dDerivedDocket-35` | PLANNED | arming: the conf switched and the real-tree staged reds |
| 36 | `TOOL-dDerivedDocket-36` | PLANNED | memory-tree guides, carriers and the backlog dossier |
| 37 | `PLAY-dDerivedDocket-1` | PLANNED | charter template: the backlog wording and the unattended landing exception |
| 38 | `DEPL-dDerivedDocket-1` | PLANNED | adopter runbook: the migrate step and the merge attribute |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-09-14 · streams tooling+playbook+deployer
ids DEPL-dDerivedDocket-1 PLAY-dDerivedDocket-1 TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11
ids TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23
ids TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35
ids TOOL-dDerivedDocket-36

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 3 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
