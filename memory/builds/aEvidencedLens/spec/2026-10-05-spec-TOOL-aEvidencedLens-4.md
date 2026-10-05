# TOOL-aEvidencedLens-4 — a spec fold round reads its diff, and a moved subject is graded, not fixed at BLOCKER

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 4 · ratified 2026-10-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-aEvidencedLens-1-runlog-696fbe29.md](../build/2026-10-05-build-TOOL-aEvidencedLens-1-runlog-696fbe29.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14 TOOL-aEvidencedLens-15 TOOL-aEvidencedLens-18 TOOL-aEvidencedLens-19 TOOL-aEvidencedLens-20 TOOL-aEvidencedLens-21 |
| [2026-10-05-build-TOOL-aEvidencedLens-4-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-aEvidencedLens-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-4-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-4-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md) | diff-review | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14 TOOL-aEvidencedLens-15 TOOL-aEvidencedLens-18 TOOL-aEvidencedLens-19 TOOL-aEvidencedLens-20 |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |

<!-- /gen:spec-records -->

## 1. Goal

A spec-audit fold round tells every lens to "aim at the text the previous round's fixes introduced"
and gives it no way to find that text, and in the same brief says "this is a first-round review" when
no prior findings were handed over. A spec that moved since it was pinned is a hard-coded BLOCKER
finding from every lens. This unit hands a fold round the diff from the blob the previous round
audited, says so plainly when it has none, and replaces the fixed BLOCKER with a probe-detected move
that the run-integrity block names and the lenses grade on its consequence.

## 2. Scope (IN)

- **S1** — A spec subject may carry `prevBlob`, the blob of that path the previous round audited, 7
  to 40 hex by the existing `PINNED_SHA`. It is validated in the prelude, after the subject ladder and
  before the first agent: present on a malformed value, or present at round 1, throws
  `tier2-review: …` naming `prevBlob`, the subject index, the legal shape and the value given
  (shared invariant 4, §8 F1). The diff kind reads no `subjects` and ignores it. The args header's
  `subjects` line names the field. Observed by AC1.
- **S2** — At round > 1, the spec brief carries a `FOLD DIFF` block naming the PRIMARY subject, the
  text the previous round's fixes introduced, one line per subject: the command
  `git -C <repo> diff <prevBlob> <blob>` when it carries one; `unchanged since the previous round`
  when `prevBlob` and `blob` name one object; `no prevBlob was supplied - review this file whole`
  otherwise. The block tells a lens whose diff command fails to review that file whole. Finders and
  skeptics read it, since both read the brief. Observed by AC2.
- **S3** — At round > 1 the spec brief never carries `this is a first-round review`. With no
  `prevBlob` on any subject AND no `priorFindings`, the REVIEW ROUND line reads as a DEGRADED fold
  review that names both absences, and a `WARNING:` line says the same before the first agent. With
  some subjects lacking `prevBlob`, a `WARNING:` line names those paths. The prior-findings line, at
  round > 1 with none, reads `none supplied for this round-<n> review`. Observed by AC2 and AC3.
- **S4** — The spec kind's resume probe gains one step: run `git -C <repo> hash-object <path>` for
  each subject and return `blobs`, one `{path, now}` per subject, `now` empty when the command fails.
  The probe reports and judges nothing; the HARNESS compares, and a subject is MOVED when `now` is 40
  hex and does not begin with the pinned `blob`. A subject with no usable `now` is UNCHECKED. The
  `blobs` field is optional in the probe schema, so a probe that omits it reads as every subject
  unchecked, never as none moved (§8 F2): a live probe returning a valid object with no `blobs` key
  is not read through `(probe.blobs || [])` as zero moves. Observed by AC4.
- **S5** — The acquire sentence stops hard-coding a BLOCKER. A lens still runs `git hash-object` on
  each subject; on a mismatch it reviews the file as it now stands, reads the moved text with
  `git -C <repo> diff <blob> -- <path>`, which anchors every path at `repo` and compares under git's
  own filters, as unreviewed fold text, and reports a defect
  IN that text as a finding graded by the SEVERITY RUBRIC. The move itself is not a finding. A moved
  subject's SUBJECT line in the brief carries `MOVED since pinned, now <now>`. Observed by AC4.
- **S6** — The spec kind's RUN INTEGRITY block names every moved subject with its pinned and current
  blob, every unchecked subject, or `move check: the resume probe died` when it did; and at round > 1
  states how many subjects carried `prevBlob`, and DEGRADED when S3's condition holds. A `WARNING:`
  line names each moved subject before the first lens. Observed by AC2, AC3 and AC4.
- **S7** — `prevBlob` joins `inputPrint` as `prevBlobs`, one value per subject in subject order,
  `null` where absent, and only when at least one spec subject carries one. A run carrying none, the
  diff kind included, keeps its print and so its key. `REVIEW_SHAPE` does not move (shared invariant
  5). Observed by AC5.
- **S8** — The diff kind is untouched: its probe, finder, skeptic and synthesis prompts are
  byte-identical before and after this unit (shared invariant 2). Observed by AC6.
- **S9** — The tier2-review self-test gains the arms of §7's `New arm:` line, written and not run in
  the pass, and its `FLOOR_ASSERTIONS` rises by the number of assertions they add. Observed by AC7.

## 3. Non-goals (OUT)

- Producing `prevBlob`. The caller pins it from the previous round; `TOOL-aEvidencedLens-5` makes the
  build harness do so on a fold re-invoke.
- The diff kind's identical contradiction. A diff review at round > 1 with no `priorFindings` also
  prints `first-round review of the whole diff`; shared invariant 2 forbids moving a diff-kind prompt
  in this build, so the line stays and is a follow-up for a later build.
- Resolving `prevBlob` against the object database. The harness has no filesystem; an unknown object
  is the lens's to meet, and S2 tells it to fall back to the whole file. The harness cannot see that
  fallback, which is a degraded review it does not announce.
- Re-keying reused lens files on a move. The review key pins `path@blob`, so a re-run with identical
  args after a subject moved can reuse a lens file that read the earlier text. The move is announced
  by S6 on that run; the reuse itself is the resume probe's existing contract and is not changed here.
- The skeptic sentence (`TOOL-aEvidencedLens-3`) and the probe policy (`TOOL-aEvidencedLens-2`), both
  in force before this unit by order. The fold diff and moved-text diff commands are read-only and
  write nothing, scratch included.
- The kit version (shared invariant 7) and any governance carrier (shared invariant 11).

### Edges

- **hands-off** `TOOL-aEvidencedLens-5` — the per-subject `prevBlob` field and its validation; that unit passes it from the previous round's pin on a fold re-invoke, and without it every fold round this unit improves is DEGRADED.
- **hands-off** `TOOL-aEvidencedLens-21` — the closing diff review's batched minors, which amend what this unit built.

## 4. Design

### Evidence

Read at `b3950dc7` on 2026-10-05, whose `tools/` tree equals BASE `028b5cac`:
`git diff --stat 028b5cac b3950dc7 -- tools/` prints nothing. Line numbers are PINNED to that read
and move as units 1, 2 and 3 land first; the identifiers do not.

- The REVIEW ROUND line (`:737`) prints `this is a FOLD review. Aim at the text the previous round's
  fixes introduced` at any spec round > 1, and the prior line (`:747`) prints `none - this is a
  first-round review of the whole spec set` whenever `priorFindings` is empty, so a round-2 run with
  no prior findings carries both.
- The acquire sentence (`:766-769`) tells every lens to report a moved spec "as a BLOCKER finding".
- `round` is inferred as 2 only from `priorFindings` (`:169`); a caller may pass any positive integer.
- The resume probe (`:622-657`) skips its step 2 on the spec kind, so its prompt numbers 1, 3, 4
  there; its schema requires `commonDir`, `finds` and `verifies` only.
- `inputPrint` (`:614`) hashes a canonical object; adding a key on the diff kind would move every
  diff-kind DURABILITY line, which carries the key.
- The build harness pins each subject at `HEAD:<path>` and refuses a subject whose tree differs from
  that blob (`TOOL-aWokenSentinel-15`, `tools/workflows/unattended-build.template.js`), so on the
  harnessed path a move is rare and a pinned blob is a committed object.
- Probed on this tree: `git diff <blob> <blob>` between two committed blobs of one path prints their
  diff and exits 0; two equal blobs print nothing; an unknown id prints `fatal: ambiguous argument`.

### The brief, spec kind, round > 1

```
REVIEW ROUND: <n> - this is a FOLD review.
FOLD DIFF - the PRIMARY subject is the text the previous round's fixes introduced. Read each diff
below FIRST, then each file whole for agreement. A diff command that fails means its file is
reviewed whole.
  - <path>: git -C <repo> diff <prevBlob> <blob>
  - <path>: unchanged since the previous round
  - <path>: no prevBlob was supplied - review this file whole
```

When no subject carries `prevBlob` and `priorFindings` is empty, the first line instead reads
`REVIEW ROUND: <n> - a DEGRADED fold review: no subject carries prevBlob and no priorFindings were
supplied, so nothing names the text the previous round's fixes introduced. Review every subject whole.`
and no FOLD DIFF block is printed. "Unchanged" compares the two strings by prefix, since either may
be abbreviated. At round 1 the REVIEW ROUND and prior-findings lines are byte-identical to the
pre-pass render's; the acquire sentence moves at every round, by S5.

### Data model

```
subjects[i]      { path, blob, prevBlob? }       prevBlob: PINNED_SHA, round > 1 only
probe return     { commonDir, finds, verifies, skipped?, blobs? }
  blobs[j]       { path: string, now: string }   spec kind only; now = '' on failure
inputPrint       + prevBlobs: [prevBlob | null, …]   only when some subject carries prevBlob
```

### Moved and unchecked

```
probeLive ∧ blobs[j].path = subjects[i].path ∧ now ~ /^[0-9a-f]{40}$/
    now begins with subjects[i].blob   → current
    otherwise                          → MOVED (path, blob, now)
no such row, or now unusable           → UNCHECKED
probe dead                             → every subject UNCHECKED, reported as "the resume probe died"
```

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `movedSubjects` | const array | not graded: the lexicon grades function names |
| `uncheckedSubjects` | const array | not graded |
| `prevBlobs` | `inputPrint` key | not graded |

No function is minted.

### Rollout

Edit the template, regenerate the render with `bash tools/workflows/check-protocol-parity.test.sh --render`,
and commit both together (shared invariant 1). Before editing, copy the pre-pass render with
the `git show` of `tools/workflows/tier2-review.js` at HEAD into the run's scratch directory; AC6 compares
against it. The arms of S9 run once at VERIFYING.

### Files touched (estimate)

`tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` · `tools/workflows/tier2-review.test.sh`

### Alternatives rejected

- **F2 (a), every lens reports the move as a finding graded by its consequence.** Five lenses each
  raise one finding for one move, so the skeptics judge five duplicates and the synthesis merges them,
  and the harness learns of the move only by parsing claim text. A move is a fact about the run, as a
  dead lens is, and the one agent that already reads the tree before the lenses can establish it
  once.
- **F2 (c), keep detection in the lenses and parse a claim prefix.** It names moved subjects in RUN
  INTEGRITY only through agent prose, which the harness cannot validate.
- **F1 (b), the subject ladder's warn-at-round-1 for a malformed `prevBlob`.** A `prevBlob` has no
  meaning at round 1, so a round-1 value is a caller error at any shape, and shared invariant 4 asks
  a malformed field to throw.

## 5. Production-readiness checklist

- security — the new commands are `git diff` and `git hash-object` without `-w`; none writes under
  `repo`. `prevBlob` reaches a prompt only after `PINNED_SHA`
  admits it, so it cannot carry a space or a control character.
- perf / scale — one `hash-object` per subject in the probe, and one diff per subject per lens.
- error / empty / loading states — a malformed or round-1 `prevBlob` throws before any agent; an
  absent one is announced per path; a dead probe reports every subject unchecked; a failed diff falls
  back to the whole file.
- observability — the DEGRADED and missing-`prevBlob` `WARNING:` lines, the moved `WARNING:` line,
  and the RUN INTEGRITY clauses.
- risks — a caller that keeps passing no `prevBlob` gets a DEGRADED round every time; S3 makes that
  loud, and `TOOL-aEvidencedLens-5` is the caller that supplies it.
- testing — the arms of S9 over stub agents.
- migration — none: `prevBlob` is optional and every round-1 prompt is unchanged.
- user docs — the `args` header comment's `subjects` line, in the same commit.

## 6. Acceptance criteria

`u4-check.js` and `pre-u4.js` below live in the run's scratch directory, outside the tree.
`u4-check.js` is a driver copying the `runReview` AsyncFunction shape of
`tools/workflows/tier2-review.test.sh` with recording stubs; it is not the suite and runs in seconds.

- **AC1** — When `node u4-check.js tools/workflows/tier2-review.js` runs a spec-kind review whose
  subject carries `prevBlob: 'zz'` at round 2, and another whose subject carries a well-formed
  `prevBlob` at round 1, each throws a message naming `prevBlob`, and the stub trace holds no agent.
  A well-formed `prevBlob` at round 2 proceeds, and a diff-kind run carrying `subjects` with a bad
  `prevBlob` proceeds.
  Red when: either bad case is accepted, the throw comes after the resume probe, or the diff kind
  refuses.
- **AC2** — When the driver runs a spec review at round 2 over three subjects, one carrying a
  `prevBlob` that differs from its blob, one carrying its own blob as `prevBlob`, and one carrying
  none, with one prior finding, every `find:` and `verify:` prompt carries `FOLD DIFF`, the line
  `git -C /tmp/r diff <prevBlob> <blob>` for the first, `unchanged since the previous round` for the
  second, and `no prevBlob was supplied` for the third; a `WARNING:` log line names the third path;
  and the `synth` prompt's RUN INTEGRITY block says `2 of 3` subjects carried `prevBlob`.
  Red when: a line is absent or attached to the wrong subject, or the count is absent or wrong.
- **AC3** — When the driver runs a spec review at round 2 with no `prevBlob` and no `priorFindings`,
  no prompt carries `first-round review`, every `find:` prompt carries `DEGRADED fold review` and
  `none supplied for this round-2 review`, a `WARNING:` line says so before the first `find:` agent,
  and the `synth` prompt's RUN INTEGRITY block says DEGRADED. The same run at round 1 carries `first-round review` and no `DEGRADED`, and in its
  `find:` prompts the text from `REVIEW ROUND:` through the `PRIOR ROUND'S FINDINGS` line is
  byte-identical to the same slice under `pre-u4.js` with the same args.
  Red when: the round-2 brief still says first-round, the degradation is silent, or round 1 moved.
- **AC4** — When the driver's probe stub returns `blobs` with a 40-hex `now` that does not begin with
  the pinned blob for one subject and an empty `now` for another, a `WARNING:` line names the moved
  path with both hashes, each `find:` prompt's SUBJECT line for it carries `MOVED since pinned`, and
  the `synth` RUN INTEGRITY block names the moved and the unchecked subject; when the probe stub
  returns null, RUN INTEGRITY says `the resume probe died`; when the probe stub returns a valid
  object carrying no `blobs` key, RUN INTEGRITY names every subject as unchecked and does not say
  `the resume probe died`. No prompt in any of these runs carries `as a BLOCKER finding` or
  `diff -u - `, and every spec `find:` prompt carries `diff <blob> -- <path>` and `SEVERITY RUBRIC`.
  The traced spec-kind `resume:probe` prompt carries `hash-object` and each subject path, and its
  schema lists `blobs` among its properties and not in `required`.
  Red when: a move is silent, a dead probe or an absent `blobs` key reads as no move, the probe is
  never asked for the hashes, or the fixed BLOCKER survives.
- **AC5** — When the driver runs two round-2 spec reviews identical except for one subject's
  `prevBlob`, their returned `key` values differ; the same diff-kind args, and the same round-1 spec
  args carrying no `prevBlob`, return the same `key` over `pre-u4.js` and the new render.
  Red when: `prevBlob` does not reach the print, or a run carrying none moved its key.
- **AC6** — When `node u4-check.js --compare pre-u4.js tools/workflows/tier2-review.js` runs the same
  diff-kind args over both renders, every `resume:probe`, `find:`, `verify:` and `synth` prompt is
  byte-identical; `node tools/workflows/check-workflow-syntax.js tools/workflows/tier2-review.js`,
  `bash tools/workflows/check-verifier-fanout.sh` and `bash tools/workflows/check-review-join.sh`
  each exit 0, and `grep -c prevBlob tools/workflows/tier2-review.template.js` and the same grep over
  `tools/workflows/tier2-review.js` print the same count of at least 3.
  Red when: any diff-kind prompt differs, the render was not regenerated, or the edit broke the
  parse, the fan-out grammar or the id join.
  fixture: `pre-u4.js` is the `git show` of `tools/workflows/tier2-review.js` at HEAD taken before the pass edits
  anything; the comparison is to this unit's predecessor, not to BASE, because
  `TOOL-aEvidencedLens-1` moved the review key every DURABILITY line carries.
- **AC7** — When `grep -c "fold:" tools/workflows/tier2-review.test.sh` runs it prints at least 6
  more than in the pre-pass file, and `FLOOR_ASSERTIONS` equals its pre-pass value plus the number of
  assertions those arms add, both figures written in the pass's commit message.
  Red when: an arm of S9 is missing or the floor did not move by the count added.
  figure: DERIVED at observation time from the pre-pass file and the pass's own diff.
  permission: a pass runs no suite; the arms are read at the main loop's VERIFYING run, which also
  reads them RED against `pre-u4.js`.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `review-protocol parity (kit vs dogfood)` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · a malformed and a round-1 `prevBlob` in the prelude, a round-2 spec run with three subject shapes, a round-2 run with neither input, probe stubs returning a moved, an unusable and a null `blobs`, and a key compare over `prevBlob` · FLOOR_ASSERTIONS rises by the assertions added

The `kit epoch` leg reds from the first unit that moves shipped bytes until the main loop's single
version bump at the close (shared invariant 7).

## 8. Open questions

- **F1 — How is a `prevBlob` validated at round 1?** (a) Refuse any `prevBlob` at round 1, and a
  malformed one at every round. (b) The subject ladder's own rule: warn on a malformed value at round
  1 and refuse it above. (c) Ignore it at round 1. §4 Alternatives rejected records why (b) loses;
  (c) silently drops a caller's input, the default shared invariant 4 forbids. Recommendation (a).
  RESOLVED (agent, 2026-10-05, delegated): (a), the one option that never silently drops the field.
- **F2 — Who detects a moved subject, and is the move a finding?** (a) Every lens reports the move as
  a finding graded by its consequence, as the brief words it. (b) The resume probe returns each
  subject's current hash, the harness compares and names moves in a WARNING and in RUN INTEGRITY, and
  lenses grade defects in the moved text as ordinary findings. (c) Lenses detect and the harness
  parses a claim prefix. §4 Alternatives rejected records why (a) and (c) lose. (b) meets both of the
  brief's halves, a graded consequence and a RUN INTEGRITY block naming every moved subject, without
  a fixed grade and without five copies of one fact. Recommendation (b).
  RESOLVED (agent, 2026-10-05, delegated): (b), the most feature-rich survivor after M3's vetoes; the
  probe is an existing agent, so no fan-out and no new surface is added.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the build's shared spec brief, unit 4, and the harness
  template read at `b3950dc7`.
- rev-2 · 2026-10-05 · §3 §4 §5 S3 S4 S5 S6 AC2 AC3 AC4 · round-1 spec audit fold. Id 2 (MEDIUM): AC4
  reads the spec `resume:probe` prompt for `hash-object` and the probe schema for an optional
  `blobs`. Id 3 (MEDIUM): S4 and AC4 cover a live probe object with no `blobs` key. Id 4 (LOW): AC3
  asserts the `none supplied for this round-2 review` line and AC2 the `2 of 3` count. Id 44 (LOW):
  S5's moved-text read is `git -C <repo> diff <blob> -- <path>`, not a cwd-dependent pipe. Id 34
  (LOW, its unit-4 half): base 3640cf58 becomes 028b5cac, with §4 Evidence restated against it.
- rev-3 · 2026-10-05 · §3 · the mirror of `TOOL-aEvidencedLens-21`'s consumes-from edge, written by
  the main loop when the closing review's minors were promoted.

## 10. Reuse audit

The probe, run on 2026-10-05:

```
python tools/codebase-map/reuse_lookup.py "fold review reads the diff between the previous audited blob and the current blob of a spec"
```

It ranked name-stem neighbours only (`read_text`, `read`, `blob_oid`, `parse_spec_h1`) and printed
`unscanned layers: .sh`; `blob_oid` in `tools/govkit/govkit.py` hashes a file for the receipt and is
not reachable from a workflow script, which has no imports. No existing seam fits outside the harness,
so this unit extends the harness's own seams in `tools/workflows/tier2-review.template.js`: the
subject ladder and `PINNED_SHA` for `prevBlob`, the resume probe for the move check, `renderBrief`
for the fold block, `inputPrint` for the key, and the RUN INTEGRITY block. The recall probe returned
the `fold-text-is-unreviewed-surface` gotcha, which measured that most round-N findings sit in fold
text and is why the diff is the PRIMARY subject; the `TOOL-aProbedUnit-1` round-2 closing review that
found the build harness priming a fresh spec as a FOLD review, closed by `subjectRound`; and the
`TOOL-dCarriedReceipt` backlog rows on spec rounds. None decided how a fold round locates its fold
text or how a move is graded.

Recall terms used: fold round prevBlob blob subjectRound priorFindings moved BLOCKER spec-audit hash-object CONVERGING re-invoke

The question passed with them: "how does a spec-audit fold round know which text the previous
round's fixes introduced, and what happens when a subject moved".
