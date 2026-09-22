---
slug: dDerivedDocket
node: d
opened: 2026-09-14
streams: tooling+playbook+deployer
roster: TOOL+PLAY+DEPL
authorized-by: prompt
ids: DEPL-dDerivedDocket-1 PLAY-dDerivedDocket-1 TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 TOOL-dDerivedDocket-38 TOOL-dDerivedDocket-39 TOOL-dDerivedDocket-40 TOOL-dDerivedDocket-41 TOOL-dDerivedDocket-42 TOOL-dDerivedDocket-43 TOOL-dDerivedDocket-44 TOOL-dDerivedDocket-45 TOOL-dDerivedDocket-46 TOOL-dDerivedDocket-47 TOOL-dDerivedDocket-48 TOOL-dDerivedDocket-49 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-52 TOOL-dDerivedDocket-53 TOOL-dDerivedDocket-54 TOOL-dDerivedDocket-55 TOOL-dDerivedDocket-56 TOOL-dDerivedDocket-57 TOOL-dDerivedDocket-58 TOOL-dDerivedDocket-59 TOOL-dDerivedDocket-60 TOOL-dDerivedDocket-61 TOOL-dDerivedDocket-62 TOOL-dDerivedDocket-63 TOOL-dDerivedDocket-64
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
- **Re-ground on each spec's base.** origin/main passed `abac6d59` by 210 commits before any unit
  was built, so every spec re-verified its claims at `fb07ca25`; a pass re-verifies them on the tree.
- **Self-protection first** (D12-i11): units 1 to 5 land before the rest so this run lands through them.
- **Dark until the flip.** Every unit before 34 keeps the shards mode byte-identical; 34 is the one
  switch-over commit.
- **Delegated signing** (owner, 2026-09-14): unit 33 signs the D2 and D6 tables under the mechanical
  rules its spec states, and the D10 drain is replaced by unit 9's permanent audit.
- **Auto-resume ships on** in the kit and here, overriding charter section 9's default-off gate for
  this feature by owner ruling; unit 5 records it as a DECISIONS row.
- **A pass runs no gate, suite or bar**, which `tools/unattended/gate-guard.js` enforces. Attributed
  suite runs moved to the one VERIFYING run; a fixture run stays in the pass. D12-h and D12-i8 say
  otherwise and are parked for the owner.
- **Spec audits run per topic group**, five sequential spec-audit reviews each recording its own
  round subject: 827 KB of specs is past what one lens reads whole, and the harness audits one set.
- **A declined discovery filed as a shard row says so.** Its text carries `Declined under the
  unattended protocol's section 11`, which unit 35 S9 keys its KEEP on; any other row filed under
  this slug names its disposing unit in the filing commit.
- **Concurrent waves from unit 23** (owner, 2026-09-21): a wave shares one `order`, set from the
  section 3 edges and M6's three conditions; its group is dispatched at one commit and each
  pass runs in its own worktree. Rows 55 to 60 are the tooling this needed.

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
| 39 | `TOOL-dDerivedDocket-37` | PLANNED | spec-token join: a hands-off's payload tokens are named by the sibling it names |
| 40 | `TOOL-dDerivedDocket-48` | PLANNED | the ask witness reads a stream the capture does not merge |
| 41 | `TOOL-dDerivedDocket-49` | PLANNED | the plan's UNDECIDED next: shape and the fixture that grades it agree |
| 42 | `TOOL-dDerivedDocket-50` | PLANNED | the anchor reader reaches its corpus through a declared route |
| 43 | `TOOL-dDerivedDocket-51` | PLANNED | an example-family id the row grammar admits, so the anchor arm can red |
| 44 | `TOOL-dDerivedDocket-52` | PLANNED | a rotated record's ancestry fallback fires on the rename it actually makes |
| 45 | `TOOL-dDerivedDocket-53` | PLANNED | --at pins the conf it evaluates, not only the records it reads |
| 46 | `TOOL-dDerivedDocket-54` | PLANNED | the cross-run exclusion probe reads history unsimplified |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 50 unit(s) · node d · opened 2026-09-14 · streams tooling+playbook+deployer
ids DEPL-dDerivedDocket-1 PLAY-dDerivedDocket-1 TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11
ids TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23
ids TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35
ids TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 TOOL-dDerivedDocket-38 TOOL-dDerivedDocket-39 TOOL-dDerivedDocket-40 TOOL-dDerivedDocket-41 TOOL-dDerivedDocket-42 TOOL-dDerivedDocket-43 TOOL-dDerivedDocket-44 TOOL-dDerivedDocket-45 TOOL-dDerivedDocket-46 TOOL-dDerivedDocket-47
ids TOOL-dDerivedDocket-48 TOOL-dDerivedDocket-49 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-52 TOOL-dDerivedDocket-53 TOOL-dDerivedDocket-54 TOOL-dDerivedDocket-55 TOOL-dDerivedDocket-56 TOOL-dDerivedDocket-57 TOOL-dDerivedDocket-58 TOOL-dDerivedDocket-59
ids TOOL-dDerivedDocket-60 TOOL-dDerivedDocket-61 TOOL-dDerivedDocket-62 TOOL-dDerivedDocket-63 TOOL-dDerivedDocket-64

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dDerivedDocket-1 — held-suite failure baseline](spec/2026-09-14-spec-TOOL-dDerivedDocket-1.md) | 1 | 2 | CLOSED | rev-7 | 2026-09-22 |
| [TOOL-dDerivedDocket-2 — in-place landing merge](spec/2026-09-14-spec-TOOL-dDerivedDocket-2.md) | 2 | 2 | CLOSED | rev-5 | 2026-09-20 |
| [TOOL-dDerivedDocket-4 — HELD phase, lease and derived phase](spec/2026-09-14-spec-TOOL-dDerivedDocket-4.md) | 3 | 2 | CLOSED | rev-9 | 2026-09-22 |
| [TOOL-dDerivedDocket-3 — the run's landing path](spec/2026-09-14-spec-TOOL-dDerivedDocket-3.md) | 4 | 2 | CLOSED | rev-7 | 2026-09-22 |
| [TOOL-dDerivedDocket-5 — auto-resume from HELD](spec/2026-09-14-spec-TOOL-dDerivedDocket-5.md) | 5 | 2 | CLOSED | rev-8 | 2026-09-22 |
| [TOOL-dDerivedDocket-37 — a hands-off's payload tokens are named by the sibling it names](spec/2026-09-14-spec-TOOL-dDerivedDocket-37.md) | 6 | 2 | CLOSED | rev-5 | 2026-09-21 |
| [TOOL-dDerivedDocket-6 — ask parser and status fold](spec/2026-09-14-spec-TOOL-dDerivedDocket-6.md) | 6 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-7 — generated family view](spec/2026-09-14-spec-TOOL-dDerivedDocket-7.md) | 7 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-8 — hygiene engine in builds mode](spec/2026-09-14-spec-TOOL-dDerivedDocket-8.md) | 8 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-9 — transition-merge audit over history and at commit time](spec/2026-09-14-spec-TOOL-dDerivedDocket-9.md) | 9 | 2 | CLOSED | rev-7 | 2026-09-21 |
| [TOOL-dDerivedDocket-10 — driver refuses shard-into-view](spec/2026-09-14-spec-TOOL-dDerivedDocket-10.md) | 10 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-11 — migration planner](spec/2026-09-14-spec-TOOL-dDerivedDocket-11.md) | 11 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-12 — relocation tools for pre-flip branches](spec/2026-09-14-spec-TOOL-dDerivedDocket-12.md) | 12 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-13 — straggler hook bodies and the fleet inventory](spec/2026-09-14-spec-TOOL-dDerivedDocket-13.md) | 13 | 2 | CLOSED | rev-7 | 2026-09-21 |
| [TOOL-dDerivedDocket-50 — the kit's own route to the anchor grammar](spec/2026-09-20-spec-TOOL-dDerivedDocket-50.md) | 13 | 2 | CLOSED | rev-2 | 2026-09-21 |
| [TOOL-dDerivedDocket-14 — rotation-note check for shards-mode archives](spec/2026-09-14-spec-TOOL-dDerivedDocket-14.md) | 14 | 1 | WONTDO | rev-1 | 2026-09-14 |
| [TOOL-dDerivedDocket-51 — an admitted example family for the kit's scratch fixtures](spec/2026-09-20-spec-TOOL-dDerivedDocket-51.md) | 14 | 2 | CLOSED | rev-2 | 2026-09-21 |
| [TOOL-dDerivedDocket-53 — a pinned read pins its conf too](spec/2026-09-20-spec-TOOL-dDerivedDocket-53.md) | 14 | 2 | CLOSED | rev-1 | 2026-09-20 |
| [TOOL-dDerivedDocket-15 — ask envelope, READY predicate and new-build scaffold](spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md) | 15 | 2 | CLOSED | rev-8 | 2026-09-21 |
| [TOOL-dDerivedDocket-48 — the ask witness reads a stream the capture does not merge](spec/2026-09-20-spec-TOOL-dDerivedDocket-48.md) | 15 | 2 | CLOSED | rev-2 | 2026-09-21 |
| [TOOL-dDerivedDocket-49 — one declared ladder decides which next: shape the plan prints](spec/2026-09-20-spec-TOOL-dDerivedDocket-49.md) | 15 | 2 | CLOSED | rev-2 | 2026-09-21 |
| [TOOL-dDerivedDocket-16 — driver ask-awareness: the asks key, preflight and plan](spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md) | 16 | 2 | CLOSED | rev-7 | 2026-09-21 |
| [TOOL-dDerivedDocket-17 — asks-disposed DoD item and freeze](spec/2026-09-14-spec-TOOL-dDerivedDocket-17.md) | 17 | 2 | CLOSED | rev-7 | 2026-09-21 |
| [TOOL-dDerivedDocket-52 — the introducing commit of a pinned record line, across the rotation rename](spec/2026-09-20-spec-TOOL-dDerivedDocket-52.md) | 17 | 2 | CLOSED | rev-2 | 2026-09-21 |
| [TOOL-dDerivedDocket-18 — leg second opinions over the ask mandate](spec/2026-09-14-spec-TOOL-dDerivedDocket-18.md) | 18 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-54 — the cross-run exclusion probe reads history unsimplified](spec/2026-09-20-spec-TOOL-dDerivedDocket-54.md) | 18 | 2 | CLOSED | rev-2 | 2026-09-21 |
| [TOOL-dDerivedDocket-19 — authority only from an owner-committed README](spec/2026-09-14-spec-TOOL-dDerivedDocket-19.md) | 19 | 2 | CLOSED | rev-7 | 2026-09-21 |
| [TOOL-dDerivedDocket-20 — unattended carriers and the two-key refusal](spec/2026-09-14-spec-TOOL-dDerivedDocket-20.md) | 20 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-21 — remote-relative bases and complete leg guards](spec/2026-09-14-spec-TOOL-dDerivedDocket-21.md) | 21 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-22 — LANDED derived from the tip](spec/2026-09-14-spec-TOOL-dDerivedDocket-22.md) | 22 | 2 | CLOSED | rev-8 | 2026-09-22 |
| [TOOL-dDerivedDocket-23 — red attribution, report-only](spec/2026-09-14-spec-TOOL-dDerivedDocket-23.md) | 23 | 2 | CLOSED | rev-6 | 2026-09-21 |
| [TOOL-dDerivedDocket-29 — review durability across a dead fan](spec/2026-09-14-spec-TOOL-dDerivedDocket-29.md) | 23 | 2 | CLOSED | rev-7 | 2026-09-21 |
| [TOOL-dDerivedDocket-25 — runner scratch hygiene and a tree-moved exit](spec/2026-09-14-spec-TOOL-dDerivedDocket-25.md) | 24 | 2 | CLOSED | rev-6 | 2026-09-22 |
| [TOOL-dDerivedDocket-30 — checker defects from the stop census](spec/2026-09-14-spec-TOOL-dDerivedDocket-30.md) | 24 | 2 | CLOSED | rev-7 | 2026-09-22 |
| [TOOL-dDerivedDocket-33 — delegated signing of the same-id and triage tables](spec/2026-09-14-spec-TOOL-dDerivedDocket-33.md) | 25 | 2 | CLOSED | rev-6 | 2026-09-22 |
| [TOOL-dDerivedDocket-24 — inherited-red policy](spec/2026-09-14-spec-TOOL-dDerivedDocket-24.md) | 26 | 2 | CLOSED | rev-7 | 2026-09-22 |
| [TOOL-dDerivedDocket-26 — honest verdicts under contention](spec/2026-09-14-spec-TOOL-dDerivedDocket-26.md) | 27 | 2 | CLOSED | rev-8 | 2026-09-22 |
| [TOOL-dDerivedDocket-28 — run-owned process ledger](spec/2026-09-14-spec-TOOL-dDerivedDocket-28.md) | 27 | 2 | CLOSED | rev-9 | 2026-09-22 |
| [TOOL-dDerivedDocket-27 — declared gate wall](spec/2026-09-14-spec-TOOL-dDerivedDocket-27.md) | 28 | 2 | SPECCED | rev-9 | 2026-09-22 |
| [TOOL-dDerivedDocket-31 — fork items and delegated-pass carriers](spec/2026-09-14-spec-TOOL-dDerivedDocket-31.md) | 29 | 2 | SPECCED | rev-5 | 2026-09-21 |
| [TOOL-dDerivedDocket-32 — remote CI on every push](spec/2026-09-14-spec-TOOL-dDerivedDocket-32.md) | 30 | 2 | SPECCED | rev-5 | 2026-09-21 |
| [TOOL-dDerivedDocket-61 — one lease record, and HELD known to every out-of-session actor](spec/2026-09-22-spec-TOOL-dDerivedDocket-61.md) | 31 | 2 | SPECCED | rev-6 | 2026-09-22 |
| [TOOL-dDerivedDocket-62 — one worktree answers for a slug, and every other copy reads ELSEWHERE](spec/2026-09-22-spec-TOOL-dDerivedDocket-62.md) | 32 | 2 | SPECCED | rev-3 | 2026-09-22 |
| [TOOL-dDerivedDocket-63 — the holder keeps its own `--replaces`: row precedence in the re-keyed resume matrix](spec/2026-09-22-spec-TOOL-dDerivedDocket-63.md) | 33 | 2 | SPECCED | rev-3 | 2026-09-22 |
| [TOOL-dDerivedDocket-64 — the turnstile queue's heartbeat, a move the liveness clock sees](spec/2026-09-22-spec-TOOL-dDerivedDocket-64.md) | 34 | 2 | SPECCED | rev-2 | 2026-09-22 |
| [TOOL-dDerivedDocket-34 — the switch-over: migration applied and the views rendered](spec/2026-09-14-spec-TOOL-dDerivedDocket-34.md) | 35 | 2 | SPECCED | rev-8 | 2026-09-22 |
| [TOOL-dDerivedDocket-35 — arming and the real-tree staged reds](spec/2026-09-14-spec-TOOL-dDerivedDocket-35.md) | 36 | 2 | SPECCED | rev-7 | 2026-09-22 |
| [PLAY-dDerivedDocket-1 — charter backlog wording and unattended landing exception](spec/2026-09-14-spec-PLAY-dDerivedDocket-1.md) | 37 | 2 | SPECCED | rev-7 | 2026-09-22 |
| [TOOL-dDerivedDocket-36 — memory-tree docs, carriers and dossier](spec/2026-09-14-spec-TOOL-dDerivedDocket-36.md) | 38 | 2 | SPECCED | rev-5 | 2026-09-22 |
| [DEPL-dDerivedDocket-1 — adopter runbook: backlog switch and merge attribute](spec/2026-09-14-spec-DEPL-dDerivedDocket-1.md) | 39 | 1 | SPECCED | rev-7 | 2026-09-22 |
<!-- /gen:build-units -->

Records: 67 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dDerivedDocket-1` | no |
| 2 | `TOOL-dDerivedDocket-2` | no |
| 3 | `TOOL-dDerivedDocket-4` | no |
| 4 | `TOOL-dDerivedDocket-3` | no |
| 5 | `TOOL-dDerivedDocket-5` | no |
| 6 | `TOOL-dDerivedDocket-37`, `TOOL-dDerivedDocket-6` | yes |
| 7 | `TOOL-dDerivedDocket-7` | no |
| 8 | `TOOL-dDerivedDocket-8` | no |
| 9 | `TOOL-dDerivedDocket-9` | no |
| 10 | `TOOL-dDerivedDocket-10` | no |
| 11 | `TOOL-dDerivedDocket-11` | no |
| 12 | `TOOL-dDerivedDocket-12` | no |
| 13 | `TOOL-dDerivedDocket-13`, `TOOL-dDerivedDocket-50` | yes |
| 14 | `TOOL-dDerivedDocket-14`, `TOOL-dDerivedDocket-51`, `TOOL-dDerivedDocket-53` | yes |
| 15 | `TOOL-dDerivedDocket-15`, `TOOL-dDerivedDocket-48`, `TOOL-dDerivedDocket-49` | yes |
| 16 | `TOOL-dDerivedDocket-16` | no |
| 17 | `TOOL-dDerivedDocket-17`, `TOOL-dDerivedDocket-52` | yes |
| 18 | `TOOL-dDerivedDocket-18`, `TOOL-dDerivedDocket-54` | yes |
| 19 | `TOOL-dDerivedDocket-19` | no |
| 20 | `TOOL-dDerivedDocket-20` | no |
| 21 | `TOOL-dDerivedDocket-21` | no |
| 22 | `TOOL-dDerivedDocket-22` | no |
| 23 | `TOOL-dDerivedDocket-23`, `TOOL-dDerivedDocket-29` | yes |
| 24 | `TOOL-dDerivedDocket-25`, `TOOL-dDerivedDocket-30` | yes |
| 25 | `TOOL-dDerivedDocket-33` | no |
| 26 | `TOOL-dDerivedDocket-24` | no |
| 27 | `TOOL-dDerivedDocket-26`, `TOOL-dDerivedDocket-28` | yes |
| 28 | `TOOL-dDerivedDocket-27` | no |
| 29 | `TOOL-dDerivedDocket-31` | no |
| 30 | `TOOL-dDerivedDocket-32` | no |
| 31 | `TOOL-dDerivedDocket-61` | no |
| 32 | `TOOL-dDerivedDocket-62` | no |
| 33 | `TOOL-dDerivedDocket-63` | no |
| 34 | `TOOL-dDerivedDocket-64` | no |
| 35 | `TOOL-dDerivedDocket-34` | no |
| 36 | `TOOL-dDerivedDocket-35` | no |
| 37 | `PLAY-dDerivedDocket-1` | no |
| 38 | `TOOL-dDerivedDocket-36` | no |
| 39 | `DEPL-dDerivedDocket-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
