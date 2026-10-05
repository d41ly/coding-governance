# TOOL-aEvidencedLens-18 — unit 15's observation is completed: the HEAD bytes tied to their blob, a break on the masked line, all four prints, both edges, and the closing pass's write set

**Status:** SPECCED · rev-3 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-18-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-18-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-18-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-18-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of `TOOL-aEvidencedLens-15`
(`reviews/2026-10-05-review-TOOL-aEvidencedLens-15-spec-audit-round1.md`) exited CONVERGED with six
confirmed findings and none at BLOCKER or HIGH. The method promotes every one of them, batched into
ONE unit, and this is that unit. It repairs `TOOL-aEvidencedLens-15` and closes:

- **id 4 (MEDIUM)** — unit 15's only staged break sits on the probe's step 1, which the class mask
  never writes, so a mask broader than its S1 would pass every criterion. Closed by S2.
- **id 5 (MEDIUM)** — unit 15 reads its HEAD render from the working copy and records the HEAD blob
  from `git rev-parse`, and nothing ties the bytes observed to the blob recorded. Closed by S1.
- **id 1 (LOW)** — unit 15's §3 Edges omit `TOOL-aEvidencedLens-12` and `TOOL-aEvidencedLens-1`,
  although its S2, AC1 and AC2 rest on both. Closed by S4.
- **ids 2 and 6 (LOW, merged in the report)** — unit 15's S5, §5 and AC4 count "both prints" and its
  AC2 "the HEAD run's print", where two renders over two arg sets make four. Closed by S3.
- **id 3 (LOW)** — unit 15, as the build's last open unit, would rewrite `memory/LIVE.md` and
  `memory/ledger/2026-10.md` without declaring them. Closed by S5.

Unit 15 builds first, as written. This unit then re-runs its observation with the four missing
pieces of evidence, writes them to its own ledger, and repairs the two record defects.

## 2. Scope (IN)

- **S1** — HEAD BYTES TIED TO THEIR BLOB (id 5). Both renders come from the object database: the
  driver's inputs are `git show 028b5cac:tools/workflows/tier2-review.js` and `git show
  HEAD:tools/workflows/tier2-review.js`, saved to the run's scratch as `base.js` and `head.js`.
  Before the driver runs, `git hash-object` of each saved file equals `git rev-parse` of the same
  path at the same revision, and the observation reds when either pair differs. The class-masked
  comparison of unit 15's AC1 is then re-run over `base.js` and `head.js`. Observed by AC1.
- **S2** — A BREAK ON THE LINE THE MASK WRITES (id 4). A second staged break, `broken3.js`, is
  `head.js` with step 3's `<the first 12 hex of the head sha>` changed to `<the first 16 hex of the
  head sha>`. That is the one line where the mask writes `<KEY>`, so the break sits next to the masked
  value. The class-masked comparison against it reds per arg set and names `resume:probe`, while each
  run's `<KEY>` count stays 1. Unit 15's step-1 break, `broken1.js`, is re-run beside it so the
  ledger carries both outcomes. Observed by AC2.
- **S3** — EVERY PRINT, PER ARG SET (ids 2 and 6). The driver prints the `inputPrint` of all four
  runs, BASE and HEAD for each of the two diff-kind arg sets. Under `--mask-key` it reds once PER arg
  set, names `resume:probe` in each red, and prints that arg set's HEAD print as the value left
  standing. A driver that stops at its first red is the defect this closes. Observed by AC3.
- **S4** — THE TWO MISSING EDGES (id 1). Unit 15's `### Edges` gains a **consumes-from** bullet to
  `TOOL-aEvidencedLens-12`, for the harness as the build ships it, and one to
  `TOOL-aEvidencedLens-1`, for the `REVIEW_SHAPE` move its AC2 rests on. Unit 12's and unit 1's
  `### Edges` each gain the **hands-off** back to `TOOL-aEvidencedLens-15`. Each of the three specs
  takes a rev bump and a §9 line, all in this unit's pass, so check 12's reciprocity join sees both
  ends at once. Observed by AC4.
- **S5** — THE CLOSING PASS DECLARES WHAT IT WRITES (id 3). This unit now orders after unit 15, so
  unit 15's pass no longer flips the build status and writes neither generated index. This unit's
  own `--dispatch` declares `memory/LIVE.md` and `memory/ledger/2026-10.md`, and its pass commit
  writes each only if `gen_build_index.py --write` moves that row. Units 19 and 20 were promoted
  after this unit at order 11, so this unit is not the build's last open unit, the build stays
  SPECCED when it closes, and its pass writes neither. Observed by AC5.
- **S6** — The blob ids, the hash-object equalities, the four prints, the four token counts and the
  outcomes of AC2 to AC5 are written to this unit's acceptance ledger,
  `memory/builds/aEvidencedLens/build/2026-10-05-build-TOOL-aEvidencedLens-18-1-acceptance-ledger.md`,
  carrying `**Serves:** journal TOOL-aEvidencedLens-18` and an `**Evidences:** TOOL-aEvidencedLens-18`
  block. Observed by AC6.

## 3. Non-goals (OUT)

- Any change to `tools/workflows/tier2-review.template.js` or its render. This unit observes, as
  unit 15 does; a red here is a defect in the unit that moved the probe, fixed there.
- Rewriting unit 15's criteria or its ledger. Unit 15 is built as written; this unit's ledger
  carries the evidence unit 15's criteria under-asked for, and S4 is the one edit to unit 15's spec.
- A standing suite arm. A self-test cannot reach a sha of this repository's history from an
  adopter's copy (`TOOL-aEvidencedLens-13` §3).
- The report's left-shift proposals: a reliance probe in check 12, `--dispatch` deriving
  generated-index writes, and the three checklist entries. Each is a separate mechanism, and none is
  needed to close the six findings.

### Edges

- **consumes-from** `TOOL-aEvidencedLens-15` — the stub driver `u15-check.js`, its class mask and
  its `--mask-class` and `--mask-key` modes, and unit 15's step-1 staged break; without them there is
  no observation to complete.
- **consumes-from** `TOOL-aEvidencedLens-12` — the last unit of this build that edits the review
  harness, so the HEAD blob this unit reads is the harness the build ships.
- **consumes-from** `TOOL-aEvidencedLens-1` — the `REVIEW_SHAPE` move that makes each arg set's
  BASE and HEAD prints differ; AC3's per-arg-set red rests on it.
- **hands-off** `TOOL-aEvidencedLens-19` — this unit's AC1 observation, which that unit re-runs over
  bytes saved with `git cat-file blob` and tied with filters off, with a CRLF copy and a one-byte
  append each observed red.
- **hands-off** `TOOL-aEvidencedLens-20` — this unit's completed observation and its ledger, whose
  criteria that unit observes live and whose §1 and §4 prose it corrects.

## 4. Design

### Evidence

Read at `a1a77460f` on 2026-10-05.

- `const inputPrint = deriveFnv1a(renderCanonical({ shape: REVIEW_SHAPE, ... }))` sits at
  `tools/workflows/tier2-review.js:696`. `${inputPrint}` is interpolated at `:702`, the key, and at
  `:720`, step 3 of the diff-kind probe, which spells
  `<the first 12 hex of the base sha>-<the first 12 hex of the head sha>-${inputPrint}`. The S2 break
  edits that line and no other.
- The inputs to `inputPrint` include `priorFindings` and `round`, so the round-1 and round-2 arg sets
  carry distinct prints. Unit 13's ledger recorded four distinct values for the same arg sets.
- `gen_build_index.py` derives a build's status from the first precedence token any unit holds. With
  this unit at SPECCED, unit 15's flip to CLOSED leaves the build at SPECCED, so its `memory/LIVE.md`
  row and its `memory/ledger/2026-10.md` row do not change in unit 15's pass.

### The completed observation

```text
base.js = git show 028b5cac:<harness>   head.js = git show HEAD:<harness>
assert hash-object(base.js) == rev-parse 028b5cac:<harness>     # red on mismatch (S1)
assert hash-object(head.js) == rev-parse HEAD:<harness>
for args in (diff r1 + checklist + specs, diff r2 + priorFindings):
  --mask-class base.js head.js     -> one resume:probe each, byte-identical, <KEY> count 1 per run
  --mask-class base.js broken1.js  -> red, names resume:probe           (unit 15's step-1 break)
  --mask-class base.js broken3.js  -> red, names resume:probe, count 1  (S2, step 3's masked line)
  --mask-key   base.js head.js     -> red, names resume:probe, prints this arg set's HEAD print
record: 2 blobs, 2 equalities, 4 prints, 4 token counts, every outcome above, per arg set
```

### Files touched (estimate)

None under `tools/`. The dispatch write set is:

- the acceptance ledger of S6;
- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md`,
  `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md` and
  `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md`, for S4's edges;
- this spec's own status header and `gen:spec-records` region;
- the regenerated `memory/builds/aEvidencedLens/README.md`;
- `memory/LIVE.md` and `memory/ledger/2026-10.md`, declared by the main loop's dispatch. The pass
  writes either only if the generator moves its row; with units 19 and 20 open it moves neither.

The stub driver and every render live in the run's scratch directory.

### Alternatives rejected

- **Amending unit 15's criteria before it builds.** That is a fold, and the method promotes a
  spec-audit finding rather than folding it.
- **One unit per finding.** The method batches the minors into one unit, or two where the write sets
  split. These do not split: every item writes the build README, and S4 and S5 both write records
  of the closing pass.
- **Asserting a clean working copy by hand, as unit 13's ledger did.** It is the gap id 5 names.
  Reading both sides from the object database removes the working copy from the observation.

## 5. Production-readiness checklist

- security — N/A: no code, and no write outside the build's records and the two generated indexes.
- perf / scale — eight stub runs of a harness render plus four staged-break runs, seconds each.
- error / empty / loading states — a hash-object mismatch, a run with no `resume:probe` label, a
  token count other than 1, and a driver that stops at its first red each red the observation with
  its reason.
- observability — the ledger names both blobs, both equalities, the four prints, the four token
  counts and every outcome, per arg set.
- risks — `u15-check.js` lives in scratch, which a lost session empties. §6 rebuilds it from unit
  15's §6 and S1 when it is absent, and the ledger says which happened.
- testing — the observation is the test; S2's break and S3's per-arg-set red are its liveness.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

`u15-check.js` is unit 15's driver, in the run's scratch directory and outside the tree. When it is
absent it is rebuilt from unit 15's §6 and S1, and the ledger records that it was rebuilt. It is not
the suite and runs in seconds.

- **AC1** — When `base.js` and `head.js` are saved with `git show` from BASE `028b5cac` and from the
  pass's `HEAD`, `git hash-object` of each equals `git rev-parse` of
  `tools/workflows/tier2-review.js` at the same revision. Then `node u15-check.js --mask-class base.js
  head.js` over the two diff-kind arg sets yields exactly one `resume:probe` prompt per run, the BASE
  and HEAD prompts are byte-identical per arg set, and each of the four runs prints a `<KEY>` count
  of 1.
  Red when: either hash-object differs from its rev-parse, the probe moved, a run has no
  `resume:probe` label, or a count is not 1.
- **AC2** — When `node u15-check.js --mask-class base.js broken3.js` runs, where `broken3.js` is
  `head.js` with step 3's `<the first 12 hex of the head sha>` changed to `<the first 16 hex of the
  head sha>`, the comparison is red for each arg set and names `resume:probe`, and each run's `<KEY>`
  count is still 1. The same command over `broken1.js`, unit 15's step-1 break, is also red.
  Red when: the step-3 break reads green on either arg set, which means the mask is wider than unit
  15's S1, or a count other than 1 shows the break moved the mask.
- **AC3** — When the AC1 command runs with `--mask-key` in place of `--mask-class`, it is red on
  BOTH arg sets, each red names `resume:probe`, and each prints its own arg set's HEAD print as the
  value left standing. The four prints differ from one another.
  Red when: either arg set reads green, the driver stops after one red, or two of the four prints
  coincide.
- **AC4** — When `check-memory-hygiene.sh` runs without `--staged` after this pass, check 12 is
  green. Unit 15's `### Edges` carries **consumes-from** bullets to `TOOL-aEvidencedLens-12` and
  `TOOL-aEvidencedLens-1`, those two specs each carry the **hands-off** back to
  `TOOL-aEvidencedLens-15`, and each of the three carries a bumped rev with a §9 line naming §3.
  Red when: either end of either edge is missing, or check 12 reds on the reciprocity join.
  cost: the whole hygiene run, minutes rather than seconds; `--staged` holds the join and cannot
  observe it.
- **AC5** — When `git show --name-only` is read for unit 15's pass commit, it lists neither
  `memory/LIVE.md` nor `memory/ledger/2026-10.md`. This unit's `--dispatch` row in the build's
  `RUN.md` lists both. `git diff --cached --name-only` before this unit's pass commit lists each
  index only if `gen_build_index.py --write` moved its row, which with units 19 and 20 open it does
  not.
  Red when: unit 15's pass wrote either index, this pass writes an index its dispatch did not
  declare, or it stages an index row the generator did not move.
- **AC6** — When `2026-10-05-build-TOOL-aEvidencedLens-18-1-acceptance-ledger.md` under the build's
  `build/` folder is read, it carries `**Serves:** journal TOOL-aEvidencedLens-18` and an
  `**Evidences:** TOOL-aEvidencedLens-18` block. The block names the two blob ids with their
  hash-object equalities, the four prints by render and arg set, the four token counts, and the
  outcomes of AC2 to AC5.
  Red when: the observation lives only in the transcript, in a file check 23 does not read, or the
  ledger names fewer than four prints.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

No `New arm:` line: a self-test cannot read this repository's BASE from an adopter's copy (§3).

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, the minors batch promoted from the spec audit of unit 15
  (`reviews/2026-10-05-review-TOOL-aEvidencedLens-15-spec-audit-round1.md`), ids 4 and 5 (MEDIUM)
  and ids 1, 2, 3 and 6 (LOW), repairing `TOOL-aEvidencedLens-15`.
- rev-2 · 2026-10-05 · §3 · gains the hands-off to `TOOL-aEvidencedLens-19` and to
  `TOOL-aEvidencedLens-20`, the units the spec audit of this unit
  (`reviews/2026-10-05-review-TOOL-aEvidencedLens-18-spec-audit-round1.md`) promoted for id 14
  (HIGH) and for ids 7, 12 and 15 (MEDIUM) and 1, 2, 3, 4, 5, 6, 8, 9, 10, 11 and 16 (LOW). Nothing
  else moves; this unit builds as written.
- rev-3 · 2026-10-05 · §2 §4 §6 S5 AC5 · the build pass diverged before code: S5, §4's last
  files-touched bullet and AC5 assumed this unit is the build's last open unit, which held only
  until units 19 and 20 were promoted after it. With them open the build stays SPECCED, so the pass
  writes neither generated index; S5 and AC5 now make each write conditional on the generator moving
  its row. `TOOL-aEvidencedLens-20` S2 carries the fuller correction; nothing else moves.

## 10. Reuse audit

The seam reused is unit 15's stub driver `u15-check.js` and its class mask, which is unit 13's
driver shape over the `runReview` stubs of `tools/workflows/tier2-review.test.sh`. This unit adds an
object-database read, a hash-object assertion, one staged break and a per-arg-set loop. No tool is
built. `python tools/codebase-map/reuse_lookup.py "stage a break on the masked line and read the
HEAD render from the object database"` returned name-stem neighbours only (`read_text`, `read`,
`render_report`) and printed `unscanned layers: .sh`. None of them compares prompts, so no existing
seam fits beyond unit 15's driver. The recall probe returned unit 15's spec, the audit findings this
unit closes, and `TOOL-aDeferredBar-10`, an ask about a ledger line asserting a result for a tree
that moved afterwards. That ask is the class of id 5, and this unit answers it for one observation
by reading from the object database.

Recall terms used: staged break masked line inputPrint resume probe acceptance ledger hash-object blob object database class mask liveness
