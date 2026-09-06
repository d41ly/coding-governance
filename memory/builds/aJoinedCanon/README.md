---
slug: aJoinedCanon
node: a
opened: 2026-09-04
streams: tooling
roster: TOOL
parents: aWeighedCanon
ids: TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11
---

# aJoinedCanon — the spec format starts joining what it already numbers

## The problem this build exists to solve

`aWeighedCanon` measured the spec format against the 479-spec corpus it produced and returned 29
confirmed findings at precision 0.85. They converge on one shape: **the format numbers things for
citation and then joins nothing to anything.** Scope items are never joined to the criteria that
observe them (13.3% of S ids are ever cited in their own §6). Criteria are joined to their ledger
answers by label alone, with no content compared — provably wrong on a CLOSED, green unit. Units
never declare sibling edges though 94% sit in multi-spec builds. No criterion names the break that
would turn it red. And the revision loop that 88% of specs enter has a one-clause instruction and a
log that names a section in 29.5% of its lines.

## Expected improvements

- Every seam the corpus breaks at becomes a declared join, and each join that has a mechanical form
  gets an arm rather than a convention nobody follows.
- The fold — measured by five builds as the source of 60–89% of the next round's defects — stops
  being one clause.

## Detriments if this is not built

- The seams stay implicit, and spec audits keep re-finding them at a full agent fan per build.
- The 29 findings decay into a research record nobody actions, which is the outcome the owner's
  "converge and spec it" instruction exists to prevent.

## Build-level rules

- **Every unit cites its finding**, at its post-skeptic numbers.
- **UNITS ARE SEQUENCED, NOT PARALLEL.** Six write `memory/TEMPLATE-SPEC.md` and its byte-compared
  twin; four more write `check-memory-hygiene.sh`. `order` is a chain, and both halves of a template
  edit move together.
- **Every template change is a DATED CUTOFF, never a retrofit**, declared in `.memory-tree.conf` AND
  `tools/memory-tree/.memory-tree.conf.example`, or an adopter gets a dead arm reading as armed.
- **A new arm owes its failing case OBSERVED before it lands**, and the spec names the fixture.
- **A finding is closed over its CLASS, never its address** — re-run its own predicate over all
  eleven specs. Round 2 measured 65% of its defects as the prior fold's work, fourteen of fifteen
  this shape; round 3 measured the rule working.
- **ONE OWNER PER SHARED ENGINE NAME.** Round 3's blocker: units 1 and 4 both bind `mcut` on the one
  check-12 awk invocation, to different cutoff keys, and last `-v` wins. A unit introducing an awk
  binding, a function or a fixture number claims it in `TOOL-aJoinedCanon-3`'s namespace registry
  first. Three rounds produced one class — an arm whose population is narrower than its spec
  believes — through three mechanisms; this is the third.
- **A unit editing a `watch:` path of `memory/guides/SESSION-KICKOFF.md` owes the `last-audit`
  re-stamp**, with a scope item, a criterion and the `kickoff-manifest ratchet` leg. Eight units
  edit one; none carried it.
- **`tFixture` blocks by `order`:** unit N takes `80 + 10N` upward.
- **No unit pins a literal a lower-`order` unit moves first**, and inside a shared write set cite by
  literal TEXT, not line number.

## Parked decisions

- **Three findings are deliberately NOT specced, so "all findings" is honestly accounted for.**
  C5 (the ledger population is located by its `Evidences` block, not its filename) — the skeptic
  rejected the fix as the paraphrase-beside-its-source class the charter refuses. Finding 34 (the
  ceremony is nearly free) — a negative result, nothing to build. Finding 20's proposal, same reason
  as C5. Each is recorded in the findings record and none needs a unit.
- **C2 (§10's predicate fails on 58.7% of the specs it nominally governs) gets no unit either.** The
  skeptic narrowed the live exposure to 12 SPECCED/INPROGRESS specs, and all 64 specs the evidence
  arm actually grades PASS. The number describes a grandfathered tail the cutoff deliberately
  parked. Reopening it is a corpus migration, not a format fix, and it is the owner's call whether
  that is ever worth doing.
- **Tier assignment is provisional until the owner approves scope.** Every unit here is SPECCED, not
  approved; §1's design-pass rule puts the menu in front of the owner before any code.

<!-- roster:units -->

| # | Unit | Tier | Mechanism | From |
|---|---|---|---|---|
| 1 | `TOOL-aJoinedCanon-1` | 2 | §9 becomes a structured entry: a rev line names the sections it moved | B2, 13 |
| 2 | `TOOL-aJoinedCanon-2` | 1 | the fold procedure gains a re-read set, in the template and in BUILD-METHOD M4 | B1 |
| 3 | `TOOL-aJoinedCanon-3` | 2 | a §2 scope item names the criterion that observes it, or says why none does | A1, 10, 21 |
| 4 | `TOOL-aJoinedCanon-4` | 2 | a §6 criterion names the break that would turn it red | A3, 23 |
| 5 | `TOOL-aJoinedCanon-5` | 1 | §6 declares a criterion's preconditions: cost, permission, fixture, derived figures | 22, 24, 25 |
| 6 | `TOOL-aJoinedCanon-6` | 2 | check 23 joins a ledger answer to its own criterion's tokens | A2, 19 |
| 7 | `TOOL-aJoinedCanon-7` | 2 | §7's contract: a leg name resolves, and the arm's home is declared | C1, 3, 11, 26 |
| 8 | `TOOL-aJoinedCanon-8` | 2 | a unit declares its sibling edges and its external preconditions | A4, 14, 27 |
| 9 | `TOOL-aJoinedCanon-9` | 2 | the §5 row set becomes a `.memory-tree.conf` declaration | C3, 6, 12, 32 |
| 10 | `TOOL-aJoinedCanon-10` | 1 | `TEMPLATE-SPEC.md:16` stops claiming a declaration that is not there | C6 |
| 11 | `TOOL-aJoinedCanon-11` | 1 | `base` resolves to a real object on a live spec | C4 |

Eleven units, one mechanism each per BUILD-METHOD M2. The `From` column cites the confirmed
findings in `memory/builds/aWeighedCanon/build/2026-09-04-build-TOOL-aWeighedCanon-2-what-the-spec-format-is-missing.md`.

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 11 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aJoinedCanon-1 — the revision log becomes a structured entry](spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md) | 1 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-2 — the fold procedure gains a re-read set](spec/2026-09-04-spec-TOOL-aJoinedCanon-2.md) | 2 | 1 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-3 — a scope item names the criterion that observes it](spec/2026-09-04-spec-TOOL-aJoinedCanon-3.md) | 3 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-4 — a criterion names the break that would turn it red](spec/2026-09-04-spec-TOOL-aJoinedCanon-4.md) | 4 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-5 — a criterion declares what it needs before it can be observed](spec/2026-09-04-spec-TOOL-aJoinedCanon-5.md) | 5 | 1 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-6 — a ledger answer is joined to its own criterion](spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md) | 6 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-7 — section 7 states the shape its join reads, and names where a new arm lives](spec/2026-09-04-spec-TOOL-aJoinedCanon-7.md) | 7 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-8 — a unit declares its sibling edges and its external preconditions](spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md) | 8 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-9 — the production-readiness row set becomes a declaration](spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md) | 9 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-10 — the template stops claiming a declaration that is not there](spec/2026-09-04-spec-TOOL-aJoinedCanon-10.md) | 10 | 1 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aJoinedCanon-11 — the base sha resolves to a real object](spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md) | 11 | 1 | SPECCED | rev-5 | 2026-09-05 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aJoinedCanon-1` | no |
| 2 | `TOOL-aJoinedCanon-2` | no |
| 3 | `TOOL-aJoinedCanon-3` | no |
| 4 | `TOOL-aJoinedCanon-4` | no |
| 5 | `TOOL-aJoinedCanon-5` | no |
| 6 | `TOOL-aJoinedCanon-6` | no |
| 7 | `TOOL-aJoinedCanon-7` | no |
| 8 | `TOOL-aJoinedCanon-8` | no |
| 9 | `TOOL-aJoinedCanon-9` | no |
| 10 | `TOOL-aJoinedCanon-10` | no |
| 11 | `TOOL-aJoinedCanon-11` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aWeighedCanon](../aWeighedCanon/README.md)
<!-- /gen:build-edges -->
