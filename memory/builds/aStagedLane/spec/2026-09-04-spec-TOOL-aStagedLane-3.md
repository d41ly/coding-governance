# TOOL-aStagedLane-3 — the spec stage fans over slices, each writer holding only its brief

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base 15339de0 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The spec stage of `tools/workflows/unattended-build.js` gives every unit of a build to one agent
under a ten-line prompt. Fan it over disjoint slices, each writer holding a brief for its own slice
and nothing else, so a build's specs stop being written from one accumulating context.

## 2. Scope (IN)

- **S1** — an optional `specBriefPath` per entry in the `units` argument, symmetric with the
  `briefPath` the build stage already takes. A unit with no spec brief falls back to the current
  prompt, so the argument is additive and no caller breaks.
- **S2** — the spec stage groups units into slices and fans one writer per slice through the
  `boundedParallel` helper already inlined at the top of the file, at its existing cap. The helper is
  reused rather than re-spelled, because `check-verifier-fanout.sh` already grades that shape.
- **S3** — slices arrive from the caller in the `units` argument. The script has no filesystem and
  cannot derive a grouping; the caller holds the plan output and the build README and is the only
  side that can.
- **S4** — every writer's prompt forbids running the index generator. The generated build index is a
  shared mutable artifact, and the parallelism rule refuses concurrent passes that touch a generated
  index together with its generator. The caller regenerates once after the fan returns.
- **S5** — the stage's return keeps its existing shape, with per-slice results merged. The refused
  list stays a required field, so a slice that wrote nothing is reported rather than being absent.
- **S6** — arms in `tools/workflows/unattended-build.test.sh` covering a multi-slice fan, a
  single-slice fan, and a slice whose writer returns nothing.

## 3. Non-goals (OUT)

- Not a consistency-audit stage. The audit stage already pins every spec of the build at its blob
  and reviews them together, so cross-slice disagreement is inside its subject already.
- Not authoring the brief content. What a brief says is a per-build act; this unit builds the seam
  that carries one.
- Not copying gate rules into any prompt. `memory/TEMPLATE-SPEC.md` owns the spec format, the
  hygiene check owns the placeholder scan, and a prompt that restates either becomes a second copy
  that drifts. The scratchpad script that motivated this build proved the drift inside one day.
- Not parallel BUILD passes. The dispatch order is settled and stays sequential; this unit fans the
  spec stage alone.
- Not raising the concurrency cap. The existing helper's bound is reused as-is.

## 4. Design

### Why the fan is permitted

The parallelism rule requires concurrency where disjointness is proven, and proves it with three
clauses. Clause 1: the write sets are the spec file paths, one per unit, and they do not intersect.
Clause 2: no writer reads another writer's output, and no spec is a contract input to a sibling
spec. Clause 3: no writer touches a shared mutable record, which is what S4 enforces by keeping the
generator out of the writers' hands. All three hold, so the fan is owed rather than merely allowed.

### Why the brief is a file and not a string

The build stage already takes a brief as a path and the driver already hashes it, so what a building
agent was handed is answerable on disk after the run ends. The spec stage has no such answer today.
Making the spec brief a path rather than an inline string puts it in the same tracked position, and
the recording verb it needs already exists.

### What context isolation actually buys here

A sidechain agent receives its prompt and nothing else, so the isolation is a property of the fan
rather than a feature to build. The unit's work is the slicing and the brief seam; the isolation
follows from spawning at all.

### Files touched (estimate)

`tools/workflows/unattended-build.js` and `tools/workflows/unattended-build.test.sh`. Two files, the
same pair as the preceding unit, which is why the two are sequenced.

### Alternatives rejected

One writer per unit rather than per slice was rejected: a build of many small units would spawn more
agents than the cap admits and gain nothing, since adjacent units often share the reading a single
writer does once.

Deriving slices inside the script was rejected because the script cannot read the tree.

## 5. Production-readiness checklist

- security — N/A. No new write path outside the build's own spec folder.
- perf / scale — the point of the unit. Wall clock falls from the sum of the units to the slowest
  slice, bounded by the existing cap.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — a slice whose writer dies returns null and must be counted as
  refused, never dropped.
- observability — the merged return names which slice produced which spec.
- risks — the live one is a writer running the generator despite S4, which would race the index. The
  mitigation is that the caller regenerates once and any writer-written region is overwritten.
- testing + left-shift gates — S6, with the multi-slice arm observed red before it is made green.
- migration / rollback — a build passing no slices behaves exactly as today.
- user docs — none; the carriers are `TOOL-aStagedLane-4`.

## 6. Acceptance criteria

- **AC1** — When the spec stage runs over a `units` argument carrying three slices, three writer
  agents are spawned, and the concurrency never exceeds the cap enforced by
  `bash tools/workflows/check-verifier-fanout.sh`.
- **AC2** — When a unit entry carries a `specBriefPath`, that path appears in the writer's prompt
  and no other slice's brief does.
- **AC3** — When a unit entry carries no `specBriefPath`, the writer receives the current prompt and
  the stage completes, proving the argument is additive.
- **AC4** — When one slice's writer returns nothing, its units appear in the stage's `refused` list
  and the other slices' results are still returned. The arm observes the empty return before the
  merge logic is written.
- **AC5** — When `bash tools/workflows/check-verifier-fanout.sh` and
  `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js` run, both exit
  0.
- **AC6** — When `bash tools/workflows/check-review-join.sh` runs, it counts the new wave and does
  not report a ref-keyed join.

## 7. Gates

`bash tools/workflows/check-verifier-fanout.sh`, `bash tools/workflows/check-review-join.sh`,
`node tools/workflows/check-workflow-syntax.js`, and the `agent-cap` hook at the tool call. The full
bar is `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — who decides the slice boundaries?** The caller holds the plan output, so it can group by
  declared order, by shared subject area, or one slice per unit.
  Options: group by the order verb, so units that land together are written together; group by the
  files each unit touches, which the caller does not reliably know before the spec exists; leave it
  to the caller with no guidance.
  Recommendation: group by the order verb. It is derivable from data the caller already has, and
  units sharing an order value are the ones most likely to share reading.

- **F2 — should a missing `specBriefPath` warn?** Falling back silently keeps the argument additive,
  but a build that meant to supply briefs and mistyped the key gets the old behaviour and no signal.
  Options: log the fallback per unit; refuse when some units have the key and others do not; stay
  silent.
  Recommendation: log it. A silent fallback and a deliberate omission are indistinguishable
  otherwise, and this is the class the harness's own return schema already guards against elsewhere.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "fan spec writing over disjoint slices with a per-slice
brief file"` returned `write` in `tools/memory-tree/gotchas.py` at fan-in 19 and `write_text` in
`tools/memory-tree/gen_build_index.py` at fan-in 18 as its top seams, both matched on the name stem
`writ` and both unrelated to spawning agents. The corpus is Python symbols and this unit's subject is
a JavaScript workflow script, so no candidate could have fitted. The seam found by reading is the
`boundedParallel` helper already inlined at the top of `tools/workflows/unattended-build.js`,
together with the `briefPath` argument the build stage already accepts; this unit reuses both shapes
rather than inventing either.

Recall terms used: `parallelism disjoint write-set dispatch pass concurrency M6 spec authoring
fan-out agent-cap bounded`. The query was whether spec authoring passes may run in parallel over
disjoint write sets; it returned 40 hits, and the binding one is the parallelism rule's three
clauses, which this unit's design section answers one at a time.
