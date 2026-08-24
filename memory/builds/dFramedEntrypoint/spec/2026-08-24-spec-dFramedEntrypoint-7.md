# TOOL-dFramedEntrypoint-7 — the conformance pass that seeds the registry with a real population

**Status:** CLOSED · rev-4 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · order 8 · streams tooling · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-build-TOOL-dFramedEntrypoint-7-acceptance.md](../build/2026-08-25-build-TOOL-dFramedEntrypoint-7-acceptance.md) | journal | — |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md) | spec-audit | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-8 |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md) | spec-audit | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-8 |
| [2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round1.md](../reviews/2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round1.md) | diff-review | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-8 |
| [2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round2.md](../reviews/2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round2.md) | diff-review | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-8 |

<!-- /gen:spec-records -->

## 1. Goal

Units 1 through 3 ship a contract, a budget and a registry that together bind nothing: the registry
lands with every build README exempt, and a rule binding zero files is coverage of nothing. This unit
conforms a measured starting population to the canon, moves those rows from exempt to bound, and lowers
the exempt pin — so the contract's first run is a real measurement rather than a green report over an
empty set.

## 2. Scope (IN)

- **S1** — a DERIVED candidate population: the build READMEs whose authored half can be conformed
  without inventing content, measured by a script that reports, per file, which canonical slots it can
  already fill from its own text and which it cannot.
- **S2** — the conformance itself, one commit per build folder, each restructuring only that build's
  own README into the canon.
- **S3** — every evicted class is ROUTED, never deleted silently: each conformance commit records where
  each evicted block went — a spec section, a build journal record, or deleted with its reason.
- **S4** — the registry rows for the conformed files move from exempt to bound, and the exempt pin falls
  by the same number, in the same commit as the file they describe.
- **S5** — this unit performs the ONE seeding event for unit 2's ceilings, from this measured
  population, recorded with the command that produced them. Unit 2 declares the rule and provisional
  values and performs no seeding, so the fact has one owner rather than three.
- **S6** — builds at a terminal status are OUT of the population by declaration, with the reason
  recorded once in the registry header rather than per row.
- **S6b** — this build's OWN README is conformed by this unit and joins the bound set, which is what
  creates the parked-decisions slot that AC8 parks into. Without it AC8 depends on a slot no S-item
  makes, and the build that writes the contract is the one build not under it.
- **S7** — a per-file conservation check: the set of authored blocks before and after each conformance
  is compared, and every block is accounted for as kept, moved with its destination, or deleted with
  its reason. A block that is simply absent is a refusal.

## 3. Non-goals (OUT)

- No conformance of TERMINAL builds, ever. Their two judgement slots cannot be honestly authored after
  the fact — the same reason the review-verdict cutoff in this tree was set forward-only in truth
  rather than in intent.
- No editing of another node's PROSE MEANING. A block moves; it is not rewritten. Where a block must be
  summarised to fit a budget, it moves whole to its destination and the slot carries a pointer.
- No new gate. The conservation check of S7 is a build-time script and an acceptance observation, not a
  merge-bar leg: it grades a migration that happens once.
- No conformance of builds owned by another node without their content moving intact. 45 of 61 READMEs
  belong to node a, and this unit's discipline is that a move is mechanical and reviewable, not that
  one node curates another's judgement.

## 4. Design

### Data model

The candidate report is one row per build README: measured authored bytes, the canonical slots it can
fill from its own text, the classes it carries that have no slot, and the destination proposed for each.
It is generated, never hand-kept.

### Inventory

The corpus splits 12 live against 49 terminal. The live half carries roughly 52.6 KB of authored prose,
15% of the total, and 8 of the 12 are already under 5 KB. That is the population this unit can conform
honestly, and it is small enough that per-build commits are reviewable.

### Migration

One commit per build folder, each carrying: the restructured README, the routed blocks at their
destinations, the registry row moving from exempt to bound, and the pin falling by one. A commit that
cannot route a block stops and parks it rather than deleting it.

### Rollout

Incremental by construction. Every intermediate state is legal: the contract binds exactly the bound
rows, so a half-conformed corpus is a smaller bound set, not a red bar.

### Alternatives rejected

**One corpus-wide surgery commit.** Rejected on the population rather than on a retirement: 49 of the
61 READMEs belong to terminal builds and are out of scope by S6, and 45 of 61 belong to another node,
so a single commit would carry another node's judgement content in a diff nobody can review. The landed
slot-contract surgery is the shape reused instead — a derived population, its own position in the build
order, and a per-file record because the diff alone is not reviewable. The retired ROSTER-WRAPPING plan
is a different plan, and its readers-removed premise is one of the dossier claims unit 8 corrects, so
it is not leaned on here.

**Conforming terminal builds too, to make the population large.** Rejected by S6's reasoning. A large
population bought by authoring judgements nobody held at the time is worse than a small honest one.

### Files touched (estimate)

Every conformed `memory/builds/*/README.md` and the records its evicted blocks move into ·
`memory/project/readme-contract.txt` · `tools/memory-tree/build-readme-slot-limits.txt` for the seeded
ceilings · a candidate-report script under the memory-tree kit or, if it is single-use, under this
build's own folder with its output recorded.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A. A one-time migration over at most a dozen files.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a build whose README cannot fill a required slot from its own text
  stays exempt and is reported, rather than being conformed with invented content.
- observability — the candidate report is the observability, and it is regenerated rather than
  hand-kept so it cannot go stale between commits.
- risks — the dominant hazard is silent prose destruction. S7's conservation check is the mitigation,
  and it is per-file rather than corpus-wide because a corpus-wide count can balance while two files
  are individually wrong.
- testing + left-shift gates — the conservation check runs per commit; the bar runs at the push
  boundary as usual.
- migration / rollback — per-build commits, each independently revertible.
- user docs — none; this unit ships no mechanism.

## 6. Acceptance criteria

- **AC1** — When the candidate report script runs, its `--report` output prints one row per tracked build README naming
  the slots it can fill and the classes it carries with no slot.
- **AC2** — When a build README is conformed, `python tools/memory-tree/gen_build_index.py --check-format`
  exits 0 with that file's registry row moved to bound.
- **AC3** — When a build README is conformed, `git diff` plus the conservation check report every pre-existing authored
  block as kept, moved with a named destination, or deleted with a reason, and reports zero unaccounted.
- **AC4** — When the conformance pass completes, the exempt pin in `memory/project/readme-contract.txt`
  equals the measured exempt count, and both are lower than at unit 3's landing.
- **AC5** — When the unit-2 ceilings are seeded from this population — this unit owns the seeding event,
  unit 2 ships only the rule and provisional values — `--report` shows every bound file under every
  ceiling, recorded with the command that produced the seed.
- **AC6** — When a terminal build is offered to the pass, the pass declines it and names the DERIVED
  build status as the reason, together with its source: the front-matter `status:` key where the build
  declares one, else the terminal status of every unit's own spec header. A build README carries no
  status header of its own — that is the spec grammar — and its status is derived precisely because it
  must not be authored twice.
- **AC7** — When `bash tools/run-gates/run-gates.sh` runs after the pass, the bar is green and the bound
  count printed by the slot-contract leg is greater than zero.
- **AC8** — When a block cannot be routed, the pass parks it in this build's parked-decisions slot in `memory/builds/dFramedEntrypoint/README.md` with
  the question and the reason, and does not delete it.

## 7. Gates

`build README slot contract` · `memory hygiene` · `build-index selftest` · the full bar at the push
boundary.

## 8. Open questions

- **F1 — are all 12 live builds in the seed, or only those conformable without an owner judgement?**
  Some live READMEs carry improvements and detriments nobody ever wrote, and inventing them is the same
  fault as conforming a terminal build. RESOLVED (agent, 2026-08-24, delegated): seed with the conformable
  subset, and report the remainder as still-exempt with the missing slot NAMED, so the gap is visible
  rather than filled. Inventing a judgement nobody held is the same fault S6 already forbids for a
  terminal build.
- **F2 — where do the evicted owner-decision and fork-ruling blocks actually go?** A spec's open-questions
  section holds a fork that belongs to that spec, but a kickoff ruling that binds a whole SET belongs to
  no single spec — and one build measured four dangling citations the last time such a block was
  relocated under cap pressure. Options: a build journal record with a stable name, cited by every spec
  it binds; or the build-level rules slot, which is budgeted and short. RESOLVED (agent, 2026-08-24, delegated): a
  build journal record with a stable name, cited by every spec it binds, and the citation shape fixed
  BEFORE the first move. The rules slot is budgeted and short, so a ruling set routed there is evicted
  again at the next cap movement; and one build measured four dangling citations the last time such a
  block moved without a fixed shape.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the owner's fork-1 ruling. The live-versus-terminal split and
  the reviewability objection to a single surgery commit are both from this build's migration research.
- rev-2 · 2026-08-24 · folded spec-audit round 1. AC6 stopped asserting that a build README carries
  a spec status header; the build status is derived, and the criterion now names the derivation and
  its source. This build's own README joins the bound set here, which is what creates the park slot
  AC8 writes into. The alternatives paragraph is re-grounded on the terminal and node-ownership
  counts rather than on a retirement whose premise unit 8 corrects. The ceiling seeding is stated as
  this unit's, once.
- rev-3 · 2026-08-24 · every open fork in section 8 resolved under the standing mandate's delegated resolver authority, by M3's rule: the most feature-rich survivor after the three vetoes. No option was taken that needed a new dependency, install location or public surface. The one question this build refuses is not a spec fork and is parked on the run-state file instead.
- rev-4 · 2026-08-25 · BUILT and CLOSED. This build's own README is conformed to the canon it defines and is the first and only BOUND row; the pin fell 62 to 61 and the ceilings are seeded from it. Three breaks staged against the bound file: a non-canon heading, a slot over its ceiling, and a slot past its high-water. The seed is ONE file rather than the twelve F1 contemplated, which is F1's rule applied literally — conform what can be conformed without inventing a judgement, and report the rest. Ledger: `build/2026-08-25-build-TOOL-dFramedEntrypoint-7-acceptance.md`.

## 10. Reuse audit

No existing seam fits, and the evidence is that the nearest one was retired: the last corpus-wide build
README surgery in this tree was planned, specced, and then abandoned in favour of removing the readers
of the thing it was going to conform. What this unit reuses is the SHAPE recorded by the surgery unit
that did land — a derived population, its own position in the build order, a per-file conservation
check rather than a corpus-wide count, and a binding gate that arrives after the migration rather than
with it.
