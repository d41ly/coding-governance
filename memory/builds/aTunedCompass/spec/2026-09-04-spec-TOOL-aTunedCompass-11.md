# TOOL-aTunedCompass-11 — the map log gains the run-state reader a closed unit's acceptance claimed

**Status:** SPECCED · rev-1 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Land the half of `TOOL-aClosedDocket-2` that did not land, and correct the acceptance ledger line that
says it did. That unit is CLOSED and ratified, its title is that `reuse_lookup.py` logs and the
run-state item counts either probe, and the logging half shipped. The reading half did not. This unit
ships the reader and makes `TOOL-aTunedCompass-8`'s new field land against something that consumes it.

## 2. Scope (IN)

- **S1** — the `reuse-probed` item in `tools/unattended/unattended.sh` (`:3588`) counts rows from the
  MAP log as well as the recall log, which is what `TOOL-aClosedDocket-2`'s S5 specified.
- **S2** — a `MAP_CLI` declaration beside `RECALL_CLI`, optional and blank by default, which is that
  unit's S4. Blank must mean not-adopted and announce the skip, exactly as the `RECALL_CLI` arm does,
  because a skip that looks like a pass is indistinguishable from coverage.
- **S3** — the declaration is a DECLARATION, never a probe of guessed paths. That unit's own spec
  records getting this wrong three ways, and the reasons still bind: a literal kit path breaks the
  declarations-not-constants rule, it raises the carried-prefix ratchet because it arrives verbatim in
  an adopter installed at another prefix, and it is unreachable by a self-test that runs the driver
  from outside the tree under test.
- **S4** — the acceptance ledger at
  `memory/builds/aClosedDocket/build/2026-08-31-build-TOOL-aClosedDocket-1-acceptance-ledger.md` gains
  a correction line for its AC8. That line asserts a merge-bar run was "check 22's key-table join
  accepting `MAP_CLI`", and `MAP_CLI` appears nowhere in the product. The correction supersedes rather
  than rewrites, because the ledger is evidence and rewriting evidence is worse than annotating it.
- **S5** — the same correction is recorded against `TOOL-aClosedDocket-2` itself, whose scope items S4
  and S5 describe work that is not in the tree. The unit stays CLOSED; what changes is that a reader
  meeting its claims also meets the correction.

## 3. Non-goals (OUT)

- Not putting this item on the merge bar. `reuse-probed`'s own header explains why and the reasoning
  still holds: the evidence lives in the git common dir, is neither tracked nor pushed, and a leg
  could only ever report a dead probe in a fresh clone. This unit extends what the item reads, never
  where it runs.
- Not adding the returned paths to the log row. That is `TOOL-aTunedCompass-8`, which is BLOCKED on
  this unit and sequenced after it.
- Not widening what the item OBSERVES. Its header already declares its blind spots — that it cannot
  tell whether a probe ran for this build, whether its question was relevant, or whether its answer
  was read. This unit adds a second log to count, not a second claim to make.
- Not reopening `TOOL-aClosedDocket-2`. An id in the units region at a pinned BASE may not leave it,
  and its status stays CLOSED.

## 4. Design

The measurement that makes this a unit rather than a hunch: `grep -rn "MAP_CLI" tools/ .unattended.conf`
returns nothing, and `lookups.jsonl` appears exactly once in the product, at its writer in
`tools/codebase-map/reuse_lookup.py` (`:442`). So the map log is a write-only surface, and the
closed unit's AC8 asserts a gate accepted a declaration that does not exist.

That last part is the reason S4 and S5 are in scope at all. This build's unit 1 corrects two records
that assert facts their sources refute; this is a third, and it is the most serious of them, because
an acceptance ledger is the strongest claim shape this repo has. A ledger line that names a passing
gate as evidence for a thing that is absent is worse than an unfinished unit, since the next reader
has no reason to doubt it.

The row grammar the map logger writes is already compatible. `TOOL-aClosedDocket-2`'s S3 records that
`type` is the field the existing reader filters on first, and the map writer emits it, so the reader
change is a second path to count rather than a second parser.

## 5. Production-readiness checklist

Security: a second declared CLI path is a second thing an adopter's conf can point at, and it is read
for existence only, never executed by this item. Observability: the not-adopted skip announces itself
per S2. Testing: arms for adopted-and-present, adopted-and-empty, and not-declared, since the middle
one is the state that silently passed before. Migration: an adopter who declares nothing keeps
today's behaviour exactly. Rollback: the item is one arm and reverting restores the recall-only count.

## 6. Acceptance criteria

1. `grep -rn "MAP_CLI" tools/` returns the declaration, its reader, and its self-test arms — the
   command that returns nothing today is the acceptance for this unit.
2. With a map log present and a recall log absent, the `reuse-probed` item is MET, verified by
   running the driver's check against a fixture built that way. That is the arm the closed unit
   claimed and never had.
3. With neither log present and both CLIs declared, the item is NOT met and names which logs it
   looked for, so an unmet item is diagnosable rather than merely red.
4. With `MAP_CLI` blank, the item announces a skip naming the missing declaration rather than passing
   silently, exercised by its own arm.
5. `bash tools/unattended/run-unattended-gates.sh` passes, and the record states it was run on demand
   because that kit's suites are on no bar by owner ruling.
6. The correction lines from S4 and S5 are present, and `bash tools/memory-tree/check-memory-hygiene.sh`
   exits 0 with them staged.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `unattended kit gate`, `memory hygiene` and `kit version
markers` the legs that bind. The unattended kit's `*.test.sh` suites are on no bar by the owner ruling
of 2026-08-23, so S6's arms run through `bash tools/unattended/run-unattended-gates.sh` on demand and
the record must say so rather than reporting them green from an ordinary bar.

## 8. Open questions

- **F1 — does the correction belong on the closed unit, or only in this build's record?** S4 and S5
  annotate a CLOSED, ratified unit and its acceptance ledger. Options: annotate both, so a reader
  meeting the claim meets the correction; annotate only the ledger, since that is where the false
  assertion lives; or record the correction only here and leave the closed unit untouched, on the
  principle that a ratified record is not rewritten.
  Recommendation: annotate both, as a superseding note rather than an edit. The append-only rule
  protects against rewriting a ratified decision, and a note that says "this claim was measured false
  on this date, here is the unit that closed it" is exactly what that rule contemplates. Left open
  because touching a ratified unit is the owner's call and the third option is defensible.

## 9. Revision log

- rev-1 · 2026-09-05 · first draft. Added by the restructure recorded in the build README, after the
  owner chose to land the missing reader before shipping `TOOL-aTunedCompass-8`'s new field. Scope
  grew beyond the reader once the closed unit's acceptance claim was checked and found false.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a run reads its own probe log to prove an orientation
probe ran"` returned `read_text`, `run`, `read` and `owners_of` — four generic seams matched on the
stems `read`, `run` and `own`, none of which is the subject. **No existing seam fits from the probe.**
The seam was found by reading: it is the `reuse-probed` case in `tools/unattended/unattended.sh`
(`:3588`), whose `RECALL_CLI` arm is the exact shape the `MAP_CLI` arm copies, and the specification
of both arms already exists in `TOOL-aClosedDocket-2`'s S4 and S5. This unit implements a spec that
was written, reviewed and closed rather than designing a new one, which is the strongest form of reuse
available here.

Recall terms used: reuse-probed liveness map log MAP_CLI RECALL_CLI unattended definition-of-done
declaration adopter skip announce acceptance ledger
