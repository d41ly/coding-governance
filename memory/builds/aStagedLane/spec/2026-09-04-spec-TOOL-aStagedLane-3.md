# TOOL-aStagedLane-3 — the spec stage fans over slices, each writer holding only its brief

**Status:** SPECCED · rev-3 · 2026-09-04 · node a · Tier-2 · base 15339de0 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md) | spec-audit | TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-4 |

<!-- /gen:spec-records -->

## 1. Goal

The spec stage of `tools/workflows/unattended-build.js` gives every unit of a build to one agent
under a ten-line prompt. Fan it over disjoint slices, each writer holding a brief for its own slice
and nothing else, so a build's specs stop being written from one accumulating context.

## 2. Scope (IN)

- **S1** — an optional `specBriefPath` per entry in the `units` argument, symmetric with the
  `briefPath` the build stage already takes. A unit with no spec brief falls back to the current
  prompt, so the argument is additive and no caller breaks.
- **S2** — the spec stage fans one writer per slice through a `boundedParallel` helper that this
  unit INLINES INTO `tools/workflows/unattended-build.js`. **The helper is not there today.** It
  lives at `tools/workflows/tier2-review.js:17` with its `// gov:bounded-fanout` marker at :20;
  `unattended-build.js` contains no `boundedParallel`, no `parallel(` and no fan at all — its four
  `agent(` calls are single awaited calls and its header says so at length. So this is a NEW marked
  copy taken from that sibling, not a reuse, and the work it implies is real: a second copy of a cap
  constant `tier2-review.js` owns, and a new shape for `check-verifier-fanout.sh` to grade over a
  file whose header records that `agent-cap` denied every earlier fan-shaped draft there.
  `tier2-review.js` remains the OWNER of the cap literal; this copy carries the same value and names
  that file beside it, so the two are one figure with a stated source rather than two declarations.
- **S3** — slices arrive from the caller in the `units` argument, grouped by the declared `order`
  verb: units sharing an order value form one slice. The script has no filesystem and cannot derive
  a grouping; the caller holds the plan output and the build README and is the only side that can.
  The order verb is chosen because it is already in the data the caller reads, and units that land
  together are the ones most likely to share the reading a single writer does once.
- **S3b** — **the fan's receiver must be one the hook can PROVE bounded, and a caller-supplied
  grouping is not.** `tools/hooks/agent-cap.js` denies any `agent(` fanned over a receiver it cannot
  delimit, and a slice list whose length comes from the caller is exactly that. The shape BUILT is
  the sanctioned one: the slice array is re-split with `chunk(x, Math.ceil(x.length / K))` for a `K`
  the hook resolves to an integer ≤5, on an assignment line carrying the `gov:fixed-verifiers`
  marker, spelled as `tier2-review.js:397` spells it. This bounds the TOTAL number of writers, which
  is a second rule and not the concurrency cap wearing a different hat: the caller's slice count
  bounds neither. The grammar is `tools/hooks/README.md`; this item names the marker so the shape is
  decided at spec time rather than discovered at the tool call.
- **S3c** — **spec writers AUTHOR and never COMMIT; the caller commits once after the fan returns**,
  alongside the single index regeneration S4 already gives it. Without this the disjointness proof is
  false: every writer is told to read `memory/guides/BUILD-METHOD.md` whole, M6 makes "a spec
  authored" a pass and orders a commit at the end of every pass, so N writers would contend on one
  git index — and the spec template mandates a backlog row per spec, so they would contend on
  `memory/backlog/<FAMILY>.md`, a record clause 3 of the parallelism rule enumerates BY NAME. That
  contention is the recorded experiment E4, which `TOOL-cBriefedPilot-21` ratified as
  `parallelism route: none` and `TOOL-cBriefedPilot-28` records as never actually run. Both ids sit
  in the header of the very file this unit edits. Authoring-only keeps this stage clear of that
  verdict instead of contradicting it unremarked.
- **S4** — every writer's prompt forbids running the index generator. The generated build index is a
  shared mutable artifact, and the parallelism rule refuses concurrent passes that touch a generated
  index together with its generator. The caller regenerates once after the fan returns.
- **S5** — the stage's return keeps its existing shape, with per-slice results merged. The refused
  list stays a required field, so a slice that wrote nothing is reported rather than being absent.
  **And the merge REFUSES when EVERY slice returns nothing.** The existing guard is `if (!specced)
  throw` on a falsy return; a merged object is always truthy, so after the fan a spec stage in which
  every writer died would present as a clean object with empty arrays and reach AUDIT and BUILD on
  whatever specs already existed. The refusal that file spends six lines justifying would become
  unreachable, which is a guard deleted without saying so.
- **S6** — arms in `tools/workflows/unattended-build.test.sh` covering a multi-slice fan, a
  single-slice fan, and a slice whose writer returns nothing.
- **S7** — a unit entry with no `specBriefPath` logs the fallback, naming the unit, before the
  writer is spawned. A silent fallback and a deliberate omission are otherwise indistinguishable,
  and a mistyped key would hand back the old behaviour with no signal.

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
- Not raising the concurrency cap. The copied helper carries `tier2-review.js`'s bound unchanged;
  S2 copies the helper because it is not in this file, and copying it is not licence to re-pick its
  number.

## 4. Design

### Why the fan is permitted

The parallelism rule requires concurrency where disjointness is proven, and proves it with three
clauses. Clause 1: the write sets are the spec file paths, one per unit, and they do not intersect.
Clause 2: no writer reads another writer's output, and no spec is a contract input to a sibling
spec. Clause 3: no writer touches a shared mutable record — which needs BOTH S4, keeping the index
generator out of the writers' hands, AND S3c, keeping the git index and the backlog out of them.
Rev-2's proof covered the spec file paths and the generated index and never covered the COMMIT, and
a proof missing a clause it enumerates by name is not a proof. With S3c the three hold, so the fan
is owed rather than merely allowed.

### How this stage relates to the ratified `parallelism route: none`

`TOOL-cBriefedPilot-21` ratified that verdict for the DISPATCH of build passes, and the header of
the file this unit edits records it. That verdict is not contradicted here, and the distinction is
the commit: it failed on E4, "each pass can commit at its own end without the two commits racing one
index", which S3c removes from this stage by having writers author and never commit. Build dispatch
stays strictly sequential — the fourth non-goal — and `TOOL-cBriefedPilot-28` stays open, because
E3 and E4 are still unrun and this unit does not run them.

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

`tools/workflows/unattended-build.js` and `tools/workflows/unattended-build.test.sh`. Two files
written, the same pair as the preceding unit, which is why the two are sequenced.
`tools/workflows/tier2-review.js` is READ as the copy source for the helper and its cap literal and
is not edited.

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

- **AC1** — When the spec stage runs over a `units` argument carrying three slices, writer agents
  are spawned for all three, and the TOTAL spawned never exceeds the resolvable `K` of S3b however
  many slices the caller supplies. A criterion tying the agent count to the caller's slice count
  would bound concurrency and leave the total unbounded, which is the second of the two rules the
  charter insists are not one rule.
- **AC2** — When a unit entry carries a `specBriefPath`, that path appears in the writer's prompt
  and no other slice's brief does.
- **AC3** — When a unit entry carries no `specBriefPath`, the writer receives the current prompt,
  a `log()` line names that unit as falling back, and the stage completes, proving the argument is
  additive and the fallback is not silent.
- **AC4** — When one slice's writer returns nothing, its units appear in the stage's `refused` list
  and the other slices' results are still returned. The arm observes the empty return before the
  merge logic is written. **And when EVERY slice's writer returns nothing, the stage THROWS** rather
  than returning a truthy object with empty arrays — observed as its own arm, because that is the
  path on which the existing refusal stops firing.
- **AC5** — When `bash tools/workflows/check-verifier-fanout.sh` and
  `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js` run, both exit
  0, AND `tools/hooks/agent-cap.js` admits the changed file when its own predicate is run over it.
  The two workflow checks exiting 0 do not answer the hook's question, and the hook is the gate that
  actually denies this shape at the tool call.
- **AC7** — When `bash tools/workflows/unattended-build.test.sh` runs its S3c arm over the composed
  writer prompt, the prompt instructs the writer to AUTHOR and forbids committing, and the
  caller-side commit is named in the stage's return or its log line. A fan of committing writers is
  the failure S3c exists to prevent, and no downstream gate reads a prompt.
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
  RESOLVED (owner, 2026-09-04): group by the order verb. Written into S3.

- **F2 — should a missing `specBriefPath` warn?** Falling back silently keeps the argument additive,
  but a build that meant to supply briefs and mistyped the key gets the old behaviour and no signal.
  Options: log the fallback per unit; refuse when some units have the key and others do not; stay
  silent.
  Recommendation: log it. A silent fallback and a deliberate omission are indistinguishable
  otherwise, and this is the class the harness's own return schema already guards against elsewhere.
  RESOLVED (owner, 2026-09-04): log the fallback. In scope as S7, observed by AC3.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-04 · both forks resolved at the owner's scope-approval turn, both as recommended.
  F1 wrote the order-verb grouping into S3; F2 added S7 and widened AC3 to observe the log line.
- rev-3 · 2026-09-04 · round-1 spec audit folded: B2, H6, H7, H8. B2 is a false premise in the one
  section whose job is to have been checked against source — `boundedParallel` is not in the file
  this unit edits, it is in `tier2-review.js` — so S2 now states the helper is INLINED afresh as a
  marked copy, §4 names the copy source, and §10 carries the correction rather than the claim. S3b
  adds the bounded receiver the `agent-cap` hook actually requires, with the marker spelling named
  at spec time, since a caller-supplied slice list is precisely the receiver it denies; AC1 was
  rewritten because it bounded concurrency and left the total free. S3c makes writers author and
  never commit, which is what clause 3 of the disjointness proof needs and what keeps this stage
  clear of `TOOL-cBriefedPilot-21`'s ratified verdict — rev-2's proof covered the file paths and the
  index and skipped the commit and the backlog row. S5 and AC4 close the all-slices-dead path, where
  the existing truthy-object guard would otherwise stop firing.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "fan spec writing over disjoint slices with a per-slice
brief file"` returned `write` in `tools/memory-tree/gotchas.py` at fan-in 19 and `write_text` in
`tools/memory-tree/gen_build_index.py` at fan-in 18 as its top seams, both matched on the name stem
`writ` and both unrelated to spawning agents. The corpus is Python symbols and this unit's subject is
a JavaScript workflow script, so no candidate could have fitted.

**CORRECTED at rev-3, and the correction is what this section is for.** Rev-2 named the seam as
"the `boundedParallel` helper already inlined at the top of `tools/workflows/unattended-build.js`".
It is not there: `grep -n boundedParallel tools/workflows/unattended-build.js` returns nothing, and
the helper is at `tools/workflows/tier2-review.js:17` with its marker at :20. So the seam is in a
SIBLING harness, this unit COPIES it rather than reusing it in place, and that is more work than
rev-2 priced — S2 now says so. What is genuinely reused in the edited file is the `briefPath`
argument the build stage already accepts, which `specBriefPath` is modelled on symmetrically.

Recall terms used: `parallelism disjoint write-set dispatch pass concurrency M6 spec authoring
fan-out agent-cap bounded`. The query was whether spec authoring passes may run in parallel over
disjoint write sets; it returned 40 hits, and the binding one is the parallelism rule's three
clauses, which this unit's design section answers one at a time. Rev-2 answered only two of the
three: the records that bind the commit half are `TOOL-cBriefedPilot-21` and `TOOL-cBriefedPilot-28`,
both cited in the header of the very file this unit edits and neither reached by that query.
