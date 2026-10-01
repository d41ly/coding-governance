# TOOL-aRepatriatedFork-55 — check 23 does not count a generated render as an undeclared write

**Status:** SPECCED · rev-1 · 2026-10-02 · node a · Tier-1 · base 65bb64c2 · streams tooling · order 26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-02-prompt-TOOL-aRepatriatedFork-55-build-brief.md](../prompts/2026-10-02-prompt-TOOL-aRepatriatedFork-55-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Check 23 compares what a dispatched pass declared it would write with what its commit wrote, and
counts every pass that wrote outside its declaration against the shrink-only pin
`UNDECLARED_WRITE_CEILING`. The final bar of this run counted 58 against 53. Three of this build's six
were spec-revision commits whose only out-of-set write was the build README's generated region,
which `gen_build_index.py --write` re-renders whenever a spec's status header moves. A generated
render is written by the generator, not by the pass, and the charter's rule for one is to re-render
it, never to reconcile it. This unit makes check 23 skip such a write and lowers the pin to the new
measured count.

## 2. Scope (IN)

- **S1** — A path the pass committed is not counted as outside its declaration when a
  `GENERATED_INDEXES` index covers it, through the same `covers` the declaration test uses. Each such
  skip prints one `check 23 excluded` report line naming the path and the index. Observed by AC1.
- **S2** — A path is not counted when the commit changed it only inside its generated regions: with
  every line from a `<!-- gen:<name> -->` marker to its `<!-- /gen:<name> -->` marker removed, the
  file at the commit equals the file at its parent. A file new at the commit, or one absent at
  either side, is counted as before. Each skip prints one `check 23 excluded` report line. Observed
  by AC2 and AC3.
- **S3** — `UNDECLARED_WRITE_CEILING` in `.unattended.conf` is lowered to the count the leg measures
  on this tree after S1 and S2, and the conf comment says what closed. Observed by AC4.
- **S4** — The check's comment states what the skip does not see. Observed by AC5.

## 3. Non-goals (OUT)

- The run-state file and a brief's own path, which check 23 already excludes by their own rules.
- Any other check's notion of a generated file. `--dispatch`'s condition 3 keeps its own reading of
  `GENERATED_INDEXES`.
- Raising the pin. It may fall and never rise.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-56` — the other gate this run's final bar redded; it writes
  disjoint files.

## 4. Design

### Evidence

- The final bar at `01c22e15`, `GATE_FULL=1`, 2026-10-01: `unattended kit gate` red, check 23 at 58
  against 53. Its report lines name `TOOL-aRepatriatedFork-53` twice and `TOOL-aRepatriatedFork-54`
  once writing `memory/builds/aRepatriatedFork/README.md`, and `TOOL-aRepatriatedFork-30` writing
  `memory/LIVE.md` and a ledger shard.
- `GENERATED_INDEXES` in `.unattended.conf` already names the generated whole-file indexes and their
  generators for `--dispatch`; check 23 reads the key and does not consult it.
- The build README's unit table, a spec's record table and the ledger rows are fenced by
  `<!-- gen:… -->` markers that `gen_build_index.py` rewrites.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`
- `.unattended.conf`
- the unattended kit's version carriers

### Alternatives rejected

- Excluding the build README whole. Its front matter and prose are authored, so a pass editing them
  outside its declaration would go uncounted.
- Raising the pin to 58 for this landing. It is shrink-only, and the class recurs on every spec
  revision made during a dispatch window.

## 5. Production-readiness checklist

- security — none; a read-only gate over tracked history.
- perf / scale — two blob reads per out-of-set path, and only for those paths.
- error / empty / loading states — a blob that cannot be read counts the path, which fails closed.
- observability — every skip prints its own report line.
- risks — a pass that hand-edits inside a gen region is not counted; S4 states it.
- testing — AC1 to AC3.
- migration — none.
- user docs — none; a gov-internal leg.

## 6. Acceptance criteria

- **AC1** — When a fixture pass declares one path and also commits a change to a path a
  `GENERATED_INDEXES` index covers, check 23 does not count it and prints `check 23 excluded`.
  Red when: the base checker is staged into the arm and it counts the pass, which is the red-first
  control.
- **AC2** — When a fixture pass commits a change confined to a `<!-- gen:units -->` region of a
  README it did not declare, check 23 does not count it.
  Red when: the base checker is staged into the arm and counts it.
- **AC3** — When the same pass instead changes a line of that README outside the gen region, check
  23 counts it and reports `wrote memory/README.md`.
  Red when: the authored edit goes uncounted.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs on this tree, check 23 is green and
  its count equals the pin.
  Red when: the count sits above the pin, or below it.
  figure: DERIVED at observation time.
- **AC5** — When the check's comment is read, it states that a hand edit inside a gen region is not
  counted, in a line reading `a hand edit inside a gen region`.
  Red when: it does not.

## 7. Gates

`unattended kit gate` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates`

New arm: `tools/unattended/check-unattended.test.sh` · a generated-index write, a gen-region-only README write, and an authored README write beside a declared path · the suite's floor rises by the new arms

## 8. Open questions

- **F1 — which files count as generated?** Option (a): the `GENERATED_INDEXES` indexes plus any
  change confined to gen regions. Option (b): the indexes only. Recommendation: (a), because the
  build README, the file that actually tripped the pin, is not an index.
  RESOLVED (owner, 2026-10-02): (a), "Exclude generated renders".

## 9. Revision log

- rev-1 · 2026-10-02 · initial draft from the owner's 2026-10-02 ruling on the final bar's check 23 red.

## 10. Reuse audit

The seams are check 23's own subset test in `tools/unattended/check-unattended.sh`, its existing
brief-path exclusion beside it, and the `covers` helper it already calls. The generated set is
`GENERATED_INDEXES`, which check 23 already loads from the conf. No new conf key.

Recall terms used: `check 23 undeclared write ceiling generated index render dispatch declaration gen region`.
