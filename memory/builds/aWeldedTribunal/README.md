---
slug: aWeldedTribunal
node: a
opened: 2026-09-04
streams: tooling
roster: TOOL
ids: TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8
authorized-by: prompt
---

# aWeldedTribunal — work the eleven backlog rows the owner named, and say which were already fixed

## The problem this build exists to solve

The owner named eleven OPEN `TOOL` rows and asked for them to be built. Reading each row against
the source it names, **four of the eleven describe a defect the tree no longer has** — one was
already marked CLOSED in the backlog itself, two were fixed by `dSealedTally`, and one by
`DEPL-dRetiredFork-4`. Building those four is not possible: there is nothing left to change.
Leaving them OPEN is the harm the row-closing pass exists to remove, and this branch's own recent
history is four merges doing exactly that for a different cluster.

The remaining seven are live and were each re-measured rather than read. Three are holes in the
fan-out cap hook, which is the only mechanical control this repo has against an agent burst, and
two of those three were reproduced at exit 0 against the shipped hook. One is a review harness that
computes its own liveness counters and hands none of them to the agent writing the durable report.
One is a conf parser divergence that removes coverage rather than failing closed. One is a deploy
verb that cannot land a file gov started shipping. One is a push boundary that can be gated by a
hook from another checkout entirely.

## Expected improvements

- **The fan-out cap stops admitting three shapes it was written to deny.** Two are measured
  evasions today: `for await (…)` and `do { … } while (…)` both carry an unmarked thunk-array fan
  past the hook at exit 0. The third blanks every line below an unterminated template literal, so
  rule 3 sees nothing under it.
- **A degraded review can no longer write a confident report.** `tier2-review.js` gains the
  run-integrity block its two drift-audit siblings already carry, plus a criterion that reds while
  the prompt lacks it — so the class cannot silently return.
- **One conf parser, five readers.** A legal `.memory-tree.conf` spelling the kit's own example
  neither shows nor forbids currently takes `gotchas.py --check` from rc=1 to rc=0 over an identical
  planted violation. Coverage is removed, and the gate stays green.
- **`govkit update` can land a file gov started shipping.** Twelve of one adopter's fourteen claimed
  kits have descriptor sources with no receipt row; one of them killed every entry point of that
  adopter's kit for six days under a green bar.
- **The push boundary is gated by the hook that ships with the pushed tree**, or at minimum says so
  when it is not.
- **Four rows stop being open**, each with the evidence that closed it recorded beside it.

## Detriments if this is not built

- Three of the four rules in `agent-cap.js` stay bypassable by spellings that are ordinary
  JavaScript, not adversarial cleverness. `for await` is what anyone writes over an async iterable.
- The next Tier-2 review whose lenses half die writes a durable record that cannot say so, and the
  finding count it reports is read as coverage.
- The conf divergence is latent HERE and live for any adopter, which is the population this repo
  ships to. It fails open on a gate, which is this repo's own stated worst shape.
- The four stale rows keep being re-read, re-triaged and re-worked by later runs. That is what this
  build's own first hour was spent on.

## Build-level rules

- **The classification, written before acting on it (M2).** Eight units, all MISSING at the start —
  no conforming spec carried any of these ids — so every one is authored this run and every one is
  unreviewed by definition. `TOOL-aWeldedTribunal-7` is additionally FORKED and its fork is
  resolved in its own §8 before code, never during.
- **FOUR ROWS ARE CLOSED ON EVIDENCE, NOT BUILT, and each cite is a file and a line rather than a
  recollection.** This is `TOOL-aWeldedTribunal-8`, and the evidence is:
  - `TOOL-dScrubbedConduit-2` — already reads `CLOSED` in `memory/backlog/TOOL.md` itself. The
    owner's list included a row that was never open.
  - `TOOL-dScaffoldedMirror-22` and `TOOL-aGroundedOrientation-4` — one defect, two rows. Both say
    `--landed` writes `phase: LANDED` before the check that refuses it. `dSealedTally` moved both
    `set_fact` calls: `tools/unattended/unattended.sh:2444-2446` now writes `landed-anchor` then
    `phase` immediately before `stage_or_fail`, with the reason at `:2425`.
  - `TOOL-aFlaggedScaffold-4` — the `govkit apply` argv blowout. `DEPL-dRetiredFork-4` built
    `git_pathspec` at `tools/govkit/govkit.py:3724`, using the exact `--pathspec-from-file=-` plus
    `--pathspec-file-nul` candidate the row proposed, and added an allowlist and an empty-list
    refusal the row did not ask for.
- **`TOOL-aScouredKit-25` closes with `TOOL-aWeldedTribunal-6`, not beside it.** That row exists
  only to record an independent re-confirmation of `TOOL-aFlaggedScaffold-3` and says in its own
  text to close it against that one rather than work it twice.
- **`TOOL-aCandidStub-1`'s reachability was MEASURED and it runs through
  `TOOL-dFoldedVerdict-8`.** Four growth spellings for an empty array literal were piped to the
  shipped hook: `for (…)`, `.forEach`, a `map` reassignment, and `for await`. The first three exit
  2. Only the fourth exits 0, and it exits 0 because of the loop-walk hole, not the literal
  blessing. So unit 2 is sequenced AFTER unit 1 and its acceptance is measured against a tree where
  unit 1 already landed — otherwise its staged-RED arm passes for the wrong reason.
- **Three units write `tools/hooks/agent-cap.js`, so M6 clause 1 forbids running them together.**
  Units 1, 2 and 3 are a three-step chain. The other four code units have disjoint write sets.
- **`TOOL-aWeldedTribunal-8` writes `memory/backlog/TOOL.md`, a shared mutable record**, so M6
  clause 3 forbids pairing it with anything. It runs last, alone.
- **PARALLEL DISPATCH IS DECLARED AND NOT TAKEN, and this is a stated deviation from M6 rather
  than an oversight.** Units 4, 5, 6 and 7 have proven-disjoint write sets and M6 requires
  concurrency where disjointness is proven. This run is a single agent with no sanctioned
  build-pass fan-out primitive: the review protocol's caps govern review agents, and dispatching
  build passes as subagents is a capability this run was not granted. The passes are therefore
  sequenced, the write-set declarations are recorded anyway via `--dispatch` so the disjointness
  claim is on disk and falsifiable, and the cost is wall clock only.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aWeldedTribunal-1` | 2 | the loop walk recognises `for await` and `do`-blocks |
| 2 | `TOOL-aWeldedTribunal-2` | 2 | an identifier blessed from an empty literal is re-examined when grown |
| 3 | `TOOL-aWeldedTribunal-3` | 2 | rule 3's blanked view reports an unterminated scan and falls back |
| 4 | `TOOL-aWeldedTribunal-4` | 2 | the tier-2 synthesis prompt carries its run-integrity counters |
| 5 | `TOOL-aWeldedTribunal-5` | 2 | five memory-tree readers route through one conf parser |
| 6 | `TOOL-aWeldedTribunal-6` | 2 | `govkit update` lands a descriptor source with no receipt row |
| 7 | `TOOL-aWeldedTribunal-7` | 2 | the wiring check grades the resolved pre-push against the tracked blob |
| 8 | `TOOL-aWeldedTribunal-8` | 1 | four rows close on cited evidence rather than on a rebuild |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 8 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aWeldedTribunal-1 — one loop-header predicate, and it recognises `for await` and `do`-blocks](spec/2026-09-04-spec-TOOL-aWeldedTribunal-1.md) | 1 | 2 | OPEN | rev-1 | 2026-09-04 |
| [TOOL-aWeldedTribunal-2 — a bounded array loses its bound when a later statement grows it](spec/2026-09-04-spec-TOOL-aWeldedTribunal-2.md) | 2 | 2 | OPEN | rev-1 | 2026-09-04 |
| [TOOL-aWeldedTribunal-3 — the blanked view reports an unterminated scan, and its readers fall back](spec/2026-09-04-spec-TOOL-aWeldedTribunal-3.md) | 3 | 2 | OPEN | rev-1 | 2026-09-04 |
| [TOOL-aWeldedTribunal-4 — the tier-2 synthesis prompt carries the liveness counters the run computed](spec/2026-09-04-spec-TOOL-aWeldedTribunal-4.md) | 4 | 2 | OPEN | rev-1 | 2026-09-04 |
| [TOOL-aWeldedTribunal-5 — one `.memory-tree.conf` parser, read by all five python readers](spec/2026-09-04-spec-TOOL-aWeldedTribunal-5.md) | 5 | 2 | OPEN | rev-1 | 2026-09-04 |
| [TOOL-aWeldedTribunal-6 — `govkit update` reports a source gov started shipping instead of missing it](spec/2026-09-04-spec-TOOL-aWeldedTribunal-6.md) | 6 | 2 | OPEN | rev-1 | 2026-09-04 |
| [TOOL-aWeldedTribunal-7 — the wiring check names the pre-push that will actually run](spec/2026-09-04-spec-TOOL-aWeldedTribunal-7.md) | 7 | 2 | OPEN | rev-1 | 2026-09-04 |
| [TOOL-aWeldedTribunal-8 — close the four rows whose defect the tree no longer has](spec/2026-09-04-spec-TOOL-aWeldedTribunal-8.md) | 8 | 1 | OPEN | rev-1 | 2026-09-04 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 3 record folder(s).

Ids no record names: TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8.

Ids no `spec-audit` record has ever named: TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aWeldedTribunal-1` | no |
| 2 | `TOOL-aWeldedTribunal-2` | no |
| 3 | `TOOL-aWeldedTribunal-3` | no |
| 4 | `TOOL-aWeldedTribunal-4` | no |
| 5 | `TOOL-aWeldedTribunal-5` | no |
| 6 | `TOOL-aWeldedTribunal-6` | no |
| 7 | `TOOL-aWeldedTribunal-7` | no |
| 8 | `TOOL-aWeldedTribunal-8` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
