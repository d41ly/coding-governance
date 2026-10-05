# TOOL-aEvidencedLens-20 — the minors batch of unit 18's audit: each of its criteria observed live, unit 15's prints and break reused by name, the revs it expects, its false prose corrected, and a closing write set derived rather than asserted

**Status:** CLOSED · rev-1 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-aEvidencedLens-20-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-aEvidencedLens-20-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-aEvidencedLens-20-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-20-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md) | diff-review | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14 TOOL-aEvidencedLens-15 TOOL-aEvidencedLens-18 TOOL-aEvidencedLens-19 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of `TOOL-aEvidencedLens-18`
(`reviews/2026-10-05-review-TOOL-aEvidencedLens-18-spec-audit-round1.md`) exited CONVERGED with
fifteen confirmed findings. Id 14 (HIGH) is promoted on its own to `TOOL-aEvidencedLens-19`. The
method promotes the other fourteen, batched into ONE unit, and this is that unit. It repairs
`TOOL-aEvidencedLens-18` and closes:

- **id 7 (MEDIUM)** — unit 18's S1 tie runs with filters on, so its record claims a byte tie it does
  not have. Closed by S1.
- **id 12 (MEDIUM)** — unit 18's S5 asserts it is the build's last open unit, which this audit's
  promotions make false. Closed by S2.
- **id 15 (MEDIUM)** — the same assertion as a class: a closing write set stated rather than derived.
  Closed by S3.
- **id 2 (LOW)** — unit 18's ledger is asked to observe the commit that contains it. Closed by S4.
- **id 1 (LOW)** — unit 18's AC1 tie has no staged break, so its red-when is unobserved. Closed by S5.
- **id 11 (LOW)** — unit 18's AC1 tie cannot red as specified and does not observe independence from
  the working copy. Closed by S6.
- **id 4 (LOW)** — unit 18's AC5 first clause reads fixed history and cannot red. Closed by S7.
- **id 3 (LOW)** — unit 18's AC4 rev clause is green before it builds. Closed by S8.
- **id 5 (LOW)** — unit 18's §1 premise of four missing pieces is stale against unit 15's ledger.
  Closed by S9.
- **id 9 (LOW)** — unit 18's AC3 "stops after one red" clause cannot fire against the driver it
  reuses. Closed by S10.
- **id 6 (LOW)** — unit 18 names unit 15's step-1 break `broken1.js`; unit 15 recorded `broken.js`.
  Closed by S11.
- **id 10 (LOW)** — unit 18's rebuild-when-absent rule covers the driver and not the step-1 break.
  Closed by S12.
- **id 16 (LOW)** — a lost scratch leaves unit 18's AC2 step-1 re-run undefined. Closed by S13.
- **id 8 (LOW)** — unit 18's §4 says `round` feeds `inputPrint`; it feeds only the key. Closed by S14.

Unit 18 builds first, as written. This unit then observes what its criteria could not, records it in
its own ledger, corrects the false prose of unit 18's spec, and derives its own closing write set.

## 2. Scope (IN)

- **S1** — THE FORM UNIT 18 RAN, ON RECORD (id 7). The hash-object form unit 18's ledger names for
  its S1 tie is copied into this ledger. Spec 18 takes ONE rev bump for S1, S2, S9, S11 and S14
  together, and its §9 line states that the S1, §4 and AC1 equality ran with filters on, so it ties
  no line-ending bytes, and that the filter-off tie is `TOOL-aEvidencedLens-19`'s. Observed by AC1.
- **S2** — UNIT 18'S "LAST OPEN UNIT", CORRECTED (id 12). The same §9 line states that S5 and §4's
  last files-touched bullet held only if no promotion followed unit 18, and that two did. This ledger
  records unit 18's `--dispatch` row from the build's `RUN.md` and `git show --name-only` of every
  commit of unit 18's pass. Observed by AC1 and AC2.
- **S3** — THIS UNIT'S CLOSING WRITE SET, DERIVED (id 15). This unit's `--dispatch` declares
  `memory/LIVE.md` and the month's ledger shard if and only if `gen_build_index.py`'s derived build
  status, with this unit flipped to CLOSED, differs from the status currently rendered; otherwise it
  declares neither. The ledger records both statuses and which branch held. Observed by AC2.
- **S4** — OBSERVED BEFORE EACH COMMIT (id 2). S3's outcome is read before every commit of this pass
  with `git diff --cached --name-only`, never by a `git show` of the commit that carries the ledger.
  No commit stages an index the dispatch row did not declare, and every declared index is staged by
  some commit of the pass. Observed by AC2.
- **S5** — UNIT 18'S TIE, BROKEN ONCE (id 1). `head-x.js` is `head.js` with one byte appended. Unit
  18's AC1 assertion, in the form its ledger names, run over `head-x.js` against `git rev-parse
  HEAD:tools/workflows/tier2-review.js`, reds and names the file. The red is recorded beside unit
  18's two equalities. Observed by AC3.
- **S6** — INDEPENDENCE FROM THE WORKING COPY (id 11). In a scratch clone at the pass's `HEAD`, under
  `%TEMP%/<short-name>`, the harness working copy gets one byte appended. A `git show
  HEAD:tools/workflows/tier2-review.js` save still hashes with `--no-filters` to the rev-parse blob,
  and the dirty working copy does not. The clone lives outside the worktree and is cleaned up after
  the reading. Id 11's AC5 half is S7's reading. Observed by AC3.
- **S7** — UNIT 15'S CLAUSE, A PRECONDITION (id 4). `git show --name-only d239695c6 ad25d88c3`, both
  commits of unit 15's pass, is read once into this ledger under the label `precondition`. It lists
  neither generated index. Observed by AC4.
- **S8** — THE REVS NAMED (id 3). After unit 18's pass, spec 1 reads `rev-4`, spec 12 `rev-5` and
  spec 15 `rev-3`. The new §9 lines of specs 1 and 12 name `TOOL-aEvidencedLens-15`, and spec 15's
  names `TOOL-aEvidencedLens-12` and `TOOL-aEvidencedLens-1`. Observed by AC5.
- **S9** — THE PREMISE RE-READ (id 5). Unit 18's four re-run prints equal unit 15's recorded
  `aada6477`, `6380ce0a`, `30f26c60` and `62ba7747` and are pairwise distinct. Spec 18's §1 is
  corrected in place: unit 15's ledger already carried those prints and the per-arg-set key-mask
  reds, and what it lacked was S1's tie and S2's step-3 break. Observed by AC1 and AC6.
- **S10** — THE STOP CLAUSE, BROKEN ONCE (id 9). `u15-check-exit1.js` is `u15-check.js` with a
  `process.exit(1)` after the first red inside its arg-set loop. Its `--mask-key` run over `base.js`
  and `head.js` reds on one arg set only, which is the defect unit 18's AC3 clause names, while the
  unmodified driver reds on both. Observed by AC6.
- **S11** — THE BREAK BY ITS RECORDED NAME (id 6). Spec 18's §9 line states that its `broken1.js` is
  unit 15's `broken.js`. This ledger names it `broken.js` throughout. Observed by AC1.
- **S12** — THE REBUILD RULE COVERS THE BREAK (id 10). When `broken.js` is absent from the scratch it
  is rebuilt by its recorded edit: `head.js` with step 1's `forward slashes (a relative answer`
  changed to `backward slashes (a relative answer`, one occurrence asserted. This spec's §6 preamble
  carries the rule, and the ledger records whether the file was reused or rebuilt. Observed by AC7.
- **S13** — THE STEP-1 RE-RUN, DEFINED (id 16). `node u15-check.js --mask-class base.js broken.js`
  runs over both arg sets on the break S12 defines. It reds in each, names `resume:probe`, and keeps
  each `<KEY>` count at 1. Observed by AC7.
- **S14** — THE PRINT'S INPUTS, CORRECTED (id 8). Spec 18's §4 Evidence second bullet is reworded in
  place: `inputPrint` is built at `tools/workflows/tier2-review.js:696-697` from checklist, specs,
  priorFindings and the other context fields, and the two arg sets differ in those. `round` enters
  only `deriveReviewKey` at `:702`. Observed by AC1.
- **S15** — Every outcome above is written to this unit's acceptance ledger,
  `memory/builds/aEvidencedLens/build/2026-10-05-build-TOOL-aEvidencedLens-20-1-acceptance-ledger.md`,
  carrying `**Serves:** journal TOOL-aEvidencedLens-20` and an `**Evidences:** TOOL-aEvidencedLens-20`
  block. Observed by AC8.

## 3. Non-goals (OUT)

- Any change under `tools/`. This unit observes and corrects records.
- Rewriting unit 18's criteria or its ledger. Unit 18 is built as written. Its §2 and §6 stand as
  what it was built against, and the one rev bump corrects only its §1 and §4 prose and adds the §9
  line naming what no longer holds.
- The filter-off tie of id 14 and its two staged breaks. They are `TOOL-aEvidencedLens-19`'s.
- The report's left-shift proposals: a spec-token check for "last open unit", `--dispatch` deriving
  the closing write set, a spec-token check resolving a sibling's scratch names, and the checklist
  entries. Each is a separate mechanism, and none is needed to close these fourteen findings.

### Edges

- **consumes-from** `TOOL-aEvidencedLens-18` — the completed observation and its ledger: the tie
  form, the four re-run prints, the step-1 and step-3 break outcomes, and the `u15-check.js` driver
  with unit 15's ledger it carries forward. This unit observes what those criteria could not and
  corrects that spec's prose.

## 4. Design

### Evidence

Read at `ad25d88c3` on 2026-10-05.

- Unit 15's ledger names its step-1 break `broken.js`, gives the one-occurrence edit S12 rebuilds,
  and records the prints `aada6477` and `6380ce0a` for round 1 and `30f26c60` and `62ba7747` for
  round 2.
- `tools/workflows/tier2-review.js:696-697` builds `inputPrint` with no `round` field; `:702`
  interpolates `round` into the key alone.
- `gen_build_index.py` returns the first precedence token any unit holds, so the build stays SPECCED
  while any unit is SPECCED. Unit 19 shares this unit's order, so which of the two closes the build
  depends on which finishes last. S3 therefore derives the write set rather than assuming it.

### Files touched (estimate)

None under `tools/`. The dispatch write set is:

- the acceptance ledger of S15;
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md`, for the one rev
  bump of S1, S2, S9, S11 and S14;
- this spec's own status header and `gen:spec-records` region;
- the regenerated `memory/builds/aEvidencedLens/README.md`;
- `memory/LIVE.md` and the month's ledger shard, if and only if S3's derivation says this pass
  changes the build status.

The scratch copies, the scratch clone and the driver live outside the tree.

### Alternatives rejected

- **Amending unit 18's criteria before it builds.** That is a fold, and the method promotes a
  spec-audit finding rather than folding it.
- **One unit per finding.** The method batches the minors into one unit, or two where the write sets
  split. These do not split: S1, S2, S9, S11 and S14 all write spec 18, and every item writes this
  unit's one ledger.
- **Rewriting unit 18's AC1 to the filter-off form.** Its criteria are what it was built against.
  Rewriting them after the build would make the record claim an observation that never ran.

## 5. Production-readiness checklist

- security — N/A: no code, and no write outside the build's records and the two generated indexes.
- perf / scale — a handful of hashes, three staged breaks, one scratch clone and six driver runs,
  seconds each apart from the clone.
- error / empty / loading states — a break that reads green, a print that differs from unit 15's,
  a rev other than the one named, and an index staged outside the dispatch row each red the
  observation with its reason.
- observability — the ledger names every outcome per item, including which branch S3 took.
- risks — the scratch may be empty after a lost session. The driver and `broken.js` are rebuilt as
  §6's preamble says, and the ledger says which happened.
- testing — S5, S6, S10 and S13 are staged breaks observed red; S3 and S4 observe every commit.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

Every scratch file named here lives outside the tree. `u15-check.js` is unit 15's driver, rebuilt
when absent as unit 18's §6 preamble states. `broken.js` is unit 15's step-1 break, rebuilt when
absent by the edit S12 records. The ledger records, for each, whether it was reused or rebuilt.

- **AC1** — When spec 18 is read after this pass, it carries exactly one rev above the rev its own
  pass closed at. Its §1 states that unit 15's ledger already held the four prints and the per-arg-set
  reds, its §4 Evidence second bullet names `round` as a key input only, and the new §9 line states
  the filtered form of S1, the conditional status of S5, and `broken1.js` as `broken.js`.
  Red when: the rev moved by other than one, or any of the five corrections is missing.
- **AC2** — When the dispatch row of this unit in the build's `RUN.md` is read, it declares
  `memory/LIVE.md` and the month's ledger shard if and only if the derived build status with this
  unit flipped to CLOSED differs from the rendered one. `git diff --cached --name-only` taken before
  each commit of this pass lists no index outside that row, and each declared index appears in at
  least one of them. The ledger also records unit 18's dispatch row and the files each of its pass
  commits wrote.
  Red when: an index is staged undeclared, a declared index is never staged, or the declaration
  disagrees with the derived status delta.
- **AC3** — When `head-x.js` is put through unit 18's AC1 assertion against HEAD's blob, it reds and
  names the file. In the scratch clone with the harness working copy dirtied, the `git show` save
  ties with `--no-filters` to the rev-parse blob and the working copy does not.
  Red when: `head-x.js` reads green, or the dirty working copy ties.
- **AC4** — When `git show --name-only d239695c6 ad25d88c3` is read, it lists neither
  `memory/LIVE.md` nor the month's ledger shard, and the ledger records it as a precondition.
  Red when: either commit lists an index.
- **AC5** — When the status headers and §9 logs of specs 1, 12 and 15 are read after unit 18's pass,
  they carry `rev-4`, `rev-5` and `rev-3`. The new §9 lines of specs 1 and 12 name
  `TOOL-aEvidencedLens-15`, and spec 15's names `TOOL-aEvidencedLens-12` and `TOOL-aEvidencedLens-1`.
  Red when: any rev differs or a new line names the wrong unit.
- **AC6** — When unit 18's ledger is read, its four prints equal `aada6477`, `6380ce0a`, `30f26c60`
  and `62ba7747` by render and arg set, and no two coincide. `node u15-check-exit1.js --mask-key
  base.js head.js` reds on one arg set only, and the unmodified driver reds on both.
  Red when: a print differs, two coincide, or the early-exit copy reds on both arg sets.
- **AC7** — When `node u15-check.js --mask-class base.js broken.js` runs over both arg sets, it reds
  in each, names `resume:probe`, and each `<KEY>` count is 1.
  Red when: either arg set reads green, or a count is not 1.
- **AC8** — When `2026-10-05-build-TOOL-aEvidencedLens-20-1-acceptance-ledger.md` under the build's
  `build/` folder is read, it carries `**Serves:** journal TOOL-aEvidencedLens-20` and an
  `**Evidences:** TOOL-aEvidencedLens-20` block naming the outcome of AC1 to AC7, one line each.
  Red when: the observation lives only in the transcript, in a file check 23 does not read, or an
  AC has no line.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

No `New arm:` line: a self-test cannot read this repository's BASE from an adopter's copy
(`TOOL-aEvidencedLens-13` §3).

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, the minors batch promoted from the spec audit of unit 18
  (`reviews/2026-10-05-review-TOOL-aEvidencedLens-18-spec-audit-round1.md`), ids 7, 12 and 15
  (MEDIUM) and ids 1, 2, 3, 4, 5, 6, 8, 9, 10, 11 and 16 (LOW), repairing `TOOL-aEvidencedLens-18`.

## 10. Reuse audit

The seam reused is unit 18's completed observation and, through it, unit 15's stub driver
`u15-check.js`, its ledger and its step-1 break. This unit adds three staged breaks, one scratch
clone, a pre-commit reading and a derived dispatch declaration; no tool is built. The derivation is
`gen_build_index.py`'s own status precedence, read rather than re-implemented.
`python tools/codebase-map/reuse_lookup.py "compare a saved file to its git blob byte for byte with
line-ending filters off"` returned name-stem neighbours only and printed `unscanned layers: .sh`, so
no seam fits beyond the git plumbing and unit 15's driver. The recall probe returned unit 18's spec,
this audit's findings, and unit 15's audit, whose id 3 is the instance S3 turns into a derivation.

Recall terms used: hash-object no-filters blob crlf autocrlf acceptance ledger byte identity staged break object database working copy
