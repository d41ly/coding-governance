# DEPL-aTetheredConvoy-7 — the acceptance matrix, the refusal join, and the runbook parity gate

**Status:** OPEN · rev-2 · 2026-08-16 · node a · Tier-2 · base 0f0a121d · streams deployer+tooling

## 1. Goal

Close the deployer's test layer against the refusal population the six units before it produce: an
acceptance matrix over the repo SHAPES the contract names, a cross-check asserting every refusal
branch in the engine is exercised by an arm that provably reaches it, and a parity gate that keeps the
prose runbook honest against the descriptors. It lands LAST so its arms are written once against a
settled population rather than re-keyed after every unit.

## 2. Scope (IN)

- **S1 — the acceptance matrix**, over the four repo shapes the contract names: a fresh empty
  repository, a repository with no Python, one whose pre-commit hook refuses, and one carrying a gate
  leg of its own that is already red. Each arm asserts a specific MESSAGE or on-disk effect, never an
  exit code alone, and each arm's expected outcome is STATED in this spec rather than read off the
  implementation — an arm with no stated expectation is a test written after the fact against itself.
- **S2 — idempotency measured over DESTINATION BYTES**, in addition to the receipt. Unit 1 owns the
  receipt half; this unit adds the other, because the two observe different failures. A receipt row
  vanishing while the destination bytes stay identical is exactly the measured seed-row loss, and a
  destination-byte arm cannot see it; a destination rewritten with identical content the receipt still
  records is the reverse. Both, and each cites the other.
- **S3 — the refusal cross-check.** Enumerate the engine's refusal branches from source, and join them
  against the branch-anchor and fixture triples the arms ACTUALLY registered while running — so the
  join observes execution rather than source text and has no stale-file surface. A branch no arm
  reached reds naming it.
- **S4 — the enumerator's population is DISCOVERED, never named.** It is the tracked Python files under
  the deployer's own directory minus the harness files, and BOTH the branch count and the FILE count
  are shrink-only pins. A hardcoded filename sees a broken matcher and not a shrinking file set — and
  this build adds a region writer, a pin phase, a leg emitter and a baseline reader to a file already
  past a thousand lines, so the natural refactor moves refusals into new modules that a one-file scan
  would silently stop grading.
- **S5 — every refusal also carries a NEGATIVE arm, and the negative arm must PROVE it reached the
  branch.** A negative arm that merely runs the same verb on an unrelated fixture asserts an absence
  that is true for the wrong reason: the guard's precondition is never evaluated, so an always-firing
  guard passes. Each negative registration declares WHICH precondition it satisfies and asserts it on
  disk before running the verb; a registration without that assertion is a registration ERROR, the same
  way a registration without an expected message already is.
- **S6 — the runbook parity gate**, keyed on the registry entry id carried as an anchor in the runbook,
  in both directions, with a body-non-empty liveness half: an anchor whose section is empty satisfies a
  presence check and teaches nobody anything.
- **S7 — the runbook is DEMOTED to narrative** in the same diff, so the parity gate has something true
  to grade rather than becoming a second maintenance burden on a document the descriptors already
  supersede.

## 3. Non-goals (OUT)

- **Re-asserting what unit 3's deployability leg already asserts.** That leg is per-registry-entry and
  data-driven; this matrix is per-repo-shape and must be Python for its source join. They assert
  different things — every ENTRY deploys, versus the deployer behaves correctly across repo shapes —
  and the two assertions they would share, plan-equals-apply and apply-twice, stay with unit 3. This
  spec CITES them and adds neither. Recorded identically in unit 3's own §8 so it cannot be re-decided
  by whichever lands second.
- **Extending the shell arms-checker to a Python population.** An open backlog row, reserved for the
  owner as a governance-carrier change. S3 is where the guarantee lives instead, which is the
  resolution the deployer contract's own fork already chose.
- **Waiving a red arm.** Several arms will red on their first run in places that are not their own
  bugs. Each is either fixed by the unit that owns it or declared RED with its reason and a named
  owner. A waiver registry for acceptance arms is not in scope and would defeat the unit.
- **A second fixture builder.** The existing throwaway-target builder is extended in place with
  keyword variants.

**Assumes:** units 1 through 6, in full. This unit's population IS their refusal set; landing it
earlier means re-keying every anchor once per subsequent unit.

## 4. Design

### Why last, and what "last" buys

The refusal join's cost is a function of the refusal population. Units 4, 5 and 6 each add named
refusals — measured on the designs, roughly a dozen between them — and each addition re-keys the join.
Written alongside them, the anchors are rewritten three more times and every rewrite is a chance for an
arm to go stale silently, which is the exact failure the join exists to catch.

### The join observes execution, not source

The naive cross-check greps the engine for message literals and greps the harness for the same
literals. That has a stale-file surface: a message moved between files, a message assembled from
fragments, or a harness file nobody runs all read as covered. Instead, each arm REGISTERS its
branch anchor, its expected message fragment and its fixture as it runs; the join then compares the
enumerated branch set against the set of anchors that were actually registered during that run. An arm
that exists but did not execute is indistinguishable from one that does not exist, which is the correct
reading.

### Discovering the population

Two shrink-only pins, not one. The branch count catches a matcher that stopped matching; the FILE count
catches a module that stopped being scanned. Only the second survives the refactor this build makes
likely, and the adversarial pass found the single-pin version passing comfortably while grading a
shrinking fraction of the engine. The discovery rule follows the shell arms-checker's own doctrine —
discover the population, never name it.

### Negative arms that provably reach their branch

The measured hole: a refusal whose precondition is "the destination exists and carries no marker pair"
has a negative arm running the same verb on a fixture with no such destination at all. The anchor is
trivially absent, the arm passes, and an always-firing guard is not caught. The contract already
records shipping exactly that defect for four revisions in another criterion.

So a negative registration carries a precondition assertion evaluated on disk before the verb runs.
Refusing a registration that lacks one is the same shape as refusing one that lacks an expected
message, and it is what makes the negative half mean anything.

### The four shapes, and what each is expected to do

Stated here rather than read off the implementation:

| shape | expected outcome |
|---|---|
| fresh empty repository | the install COMPLETES; the default selection lands, including the playbook's bytes, which unit 1's criterion already asserts and this arm cites rather than re-derives |
| no Python present | the deployer runs on the DEPLOYER's interpreter; a kit whose adopter needs one in the target refuses NAMING the interpreter rather than failing obscurely |
| pre-commit hook refuses | the install COMPLETES and the receipt exists, because nothing commits during an install; an order carries the hook's own output. Unit 4 owns the probe; this arm owns the end-to-end expectation |
| a target leg already red | the install COMPLETES and reports it; a leg green before and red after FAILS the install naming the leg. Unit 4 owns the state machine; this arm owns the shape |

The two arms that need an adopter's exit code INTERPRETED rather than printed depend on unit 5's
outcome evaluator. That dependency is named here because without it those arms could only assert an
integer, which S1 forbids by name — a required dependency claimed by a criterion and owned by no unit
is how a spec ships an unbuildable arm.

### The parity key

Keying a parity gate on prose headings is fragile: a heading is edited for readability and the gate
reds for nothing. The key is the registry entry id, carried as a comment anchor in the runbook, which
is stable, machine-comparable, and already the identifier both sides use. The liveness half is that the
anchored section's BODY is non-empty — an anchor with nothing under it satisfies presence and is worse
than an absent one, because it reads as covered.

### Rollout

1. **The fixture variants and the four shapes** — S1, S2, and the citations to units 1 and 3.
2. **The join** — S3, S4, S5, over whatever the population is at that commit.
3. **The parity gate and the demotion** — S6, S7.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Harness | one new matrix process, one new parity gate | both under the deployer's own directory |
| Tests | `tools/govkit/selftest.py` | the fixture builder gains keyword variants and an import guard |
| Runbook | `WIRE-INTO-PROJECT.md` | demoted, and anchored |
| Gates | `tools/gate-legs.json`, `AGENTS.md` | two new legs, cited in the charter |
| Map | `memory/map/features/govkit.md` | two gate-leg claims |

### Alternatives rejected

**Put the join in `selfcheck`.** Rejected: `selfcheck` is a source-and-declaration checker with no
fixtures, and a join that observes EXECUTION needs the arms to have run. It belongs in the process that
runs them.

**One harness for everything.** Rejected: unit 3's leg is bash and per-entry; this is Python and
per-shape. Merging them means one process doing two jobs and paying the four-gate leg tax to delete a
leg later.

**Key the parity gate on descriptor step names.** Rejected: descriptors declare files, adopters and
legs, not steps. The entry id is the only identifier both sides genuinely share.

## 5. Production-readiness checklist

- security — fixtures only; every one is a throwaway repository the harness creates and owns.
- perf / scale — the matrix runs the deployer once per shape; the join is a source parse plus a set
  comparison. Both legs are guarded on the deployer's own paths.
- a11y — N/A: gate legs with stdout only.
- i18n — N/A: developer tooling.
- error / empty / loading states — the registration errors ARE this line: an arm with no expected
  message, and a negative arm with no precondition, are both refused rather than silently accepted.
- observability — each leg prints its derived counts: shapes exercised, branches enumerated, branches
  reached, anchors compared.
- risks — the first run reds in places that are not this unit's bugs; §3 forbids waiving them and
  requires a named owner instead. Second: the fixture builder does not set the platform's line-ending
  conversion, so a foreign-platform behaviour the matrix should grade is invisible to it — stated here
  rather than discovered, and the variant is part of S1.
- testing + left-shift gates — this unit IS the left-shift; its own liveness is the two shrink-only
  pins and the registration refusals.
- migration / rollback — additive.
- user docs — the runbook's demotion is the user-facing change, and the parity gate is what keeps it
  honest.

## 6. Acceptance criteria

- **AC1** When `python tools/govkit/matrix.py` runs, each of the four shapes reaches its stated
  outcome, asserted on a MESSAGE or an on-disk effect and never on an exit code alone. Liveness: the
  process prints a derived count of shapes exercised and reds when it is zero.
- **AC2** When each shape's fixture is applied twice by `python tools/govkit/matrix.py`, the DESTINATION
  bytes of every landed path are identical between runs. This arm cites unit 1's receipt-side criterion rather than replacing it: the
  measured seed-row loss is invisible to a destination-byte arm, because the file exists both times and
  only the receipt row vanishes.
- **AC3** When the matrix runs, the refusal join enumerates every refusal branch in the tracked
  `tools/govkit/*.py` population and reds naming any branch no arm registered during that run.
- **AC4** When a refusal branch is moved into a NEW module matching `tools/govkit/*.py`, the
  enumerator still finds it — asserted by the FILE-count pin, which reds when the scanned file set
  shrinks. Liveness: the branch-count pin alone passes in that state, which is why there are two.
- **AC5** When an arm registers a `negative=` half without a precondition assertion,
  `python tools/govkit/matrix.py` refuses the registration naming it — the same shape as a registration with no expected message. Liveness: a
  negative arm whose precondition IS asserted and whose branch does not fire passes, and one whose
  precondition is asserted and whose branch DOES fire reds.
- **AC6** When `python tools/govkit/check-runbook-parity.py` runs, it reds naming a registry entry with
  no anchored runbook section, and separately a runbook anchor naming no registry entry. Liveness: an
  anchor whose section body is empty REDS rather than counting as present.
- **AC7** When the demotion of `WIRE-INTO-PROJECT.md` lands, every anchored section is non-empty and the
  parity gate exits 0 — the demotion and the gate in one diff, so the gate never grades a document it was written
  against.
- **AC8** When `python tools/govkit/matrix.py` runs on both a POSIX shell and the platform shell this repo
  runs under, every arm produces the same verdict. A shape whose behaviour genuinely differs is asserted per-platform
  with both expectations stated.
- **AC9** When an arm depends on an adopter's exit code being INTERPRETED, it asserts the declared
  MEANING from unit 5's `[[outcome]]` evaluator and never the integer. Liveness: with the evaluator absent the arm
  must red rather than degrade to an integer comparison.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary; `GATE_FULL=1` for the DoD. Two new legs.

Adding a leg trips four gates at once and this unit adds two, so the tax is paid once here: the
codebase-map coverage assert, the codebase-map freshness byte-compare, the kickoff-manifest ratchet,
and drift-audit's handkept charter signal, which is pinned with zero slack — both new leg script paths
must be named in the charter's gate-suite section in the same commit, and the govkit dossier must claim
both.

Unit 3's leg correspondence reds until both new legs are claimed by a descriptor or carried by an
exemption. They are gov-internal harnesses, so an exemption with its reason is the expected answer, and
writing it is part of this unit.

Before review: `python tools/memory-tree/gotchas.py --for-diff 0f0a121d..HEAD`. The
`absence-assertion-over-whole-file-text` class is live: the join is a new absence predicate run for the
first time against the real engine, and this repo's rule is that such a predicate is run over the real
tree before it is trusted, not after.

## 8. Open questions

none — the forks below are RESOLVED. Authority: the owner's instruction to execute this build
delegates resolver authority for THIS build only, and every fork here is one the spec already stated,
which is exactly M3's condition. Each was taken through M3's veto order; none was discarded by a veto,
and the two that touch a write or security surface are called out in the wrap-up as owner-review items
rather than treated as settled by silence.

- **F1 — do the two new legs get exemptions, or descriptors?** RESOLVED (agent, 2026-08-16,
  delegated): exemptions with reasons. They are gov-internal harnesses over gov's own deployer, and an
  adopter receives neither. The asymmetry with the two self-tests the runbook DOES prescribe for copy
  is what the exemption reason must carry.
- **F2 — shrink-only pins, or exact?** RESOLVED (agent, 2026-08-16, delegated): shrink-only, matching
  every other pin in this repo and carrying the weakening-move convention it already enforces. An exact
  pin turns every legitimate refusal addition into a red bar and would be waived within a week.

## 9. Revision log

- rev-2 · 2026-08-16 · M3 fork sweep: F1 and F2 resolved in place under the owner's
  execute-the-build delegation. No veto fired.
- rev-1 · 2026-08-16 · initial draft. Grounded on a twelve-agent audit and adversarial pass. Three of
  this spec's decisions came from the adversary: the enumerator's population is discovered with TWO
  shrink-only pins rather than one hardcoded filename, because this build makes a refactor into new
  modules likely and a one-file scan would keep reporting full coverage of a shrinking fraction;
  negative arms must prove they REACH their branch, because the natural form asserts an absence that is
  true for an unrelated reason; and the destination-byte idempotency arm is IN ADDITION TO the receipt
  arm rather than instead of it, because each is blind to exactly the failure the other catches.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py` for the matrix, the join and the parity gate.

The existing throwaway-target builder in the deployer's selftest is already the fixture shape every
shape-arm needs; it is extended in place with keyword variants rather than copied, and making it
importable costs one guard. The codebase-map adopter's end-to-end fixture builder is the precedent for
a prefix-parameterized scratch repo and is the one unit 3's leg extends, which is why this unit does
not.

The selftest's arm registrar is the harness this matrix reuses; the join is its last arm rather than a
second process.

The shell arms-checker is NOT reused and is deliberately not extended — its population is repo-wide
shell and the contract's own fork keeps it that way. What IS reused is its doctrine: discover the
population, never name it, and pin in both directions.

The weakening-move convention on pins is reused unchanged, so a pin move in the weakening direction
must name both values beside it.

The four shipped render-parity checks are the nearest gates to S6 and none of them fits: every one
compares a RENDER to its template plus a conf, and none reads a prose document against a declaration
set. The closest in spirit is the method-carrier registry — structural only, per-repo, with a caveat
this gate copies word for word — but its registry is a hand-kept path list rather than a derived
population, so the parity gate is new.

No seam exists for parsing Python to find control-flow branches: the one place this repo parses Python
walks modules for exports and has no notion of a message string. The enumerator is new and small.
