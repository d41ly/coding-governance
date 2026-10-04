# TOOL-aEvidencedLens-3 — the spec skeptic confirms by the rubric, re-runs the evidence, and refutes duplicates and by-design

**Status:** SPECCED · rev-2 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 3 · ratified 2026-10-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-3-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-3-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |

<!-- /gen:spec-records -->

## 1. Goal

The spec-audit skeptic confirms only what "makes the spec unbuildable or wrong", which contradicts
the rubric it is handed beside it: a LOW can never be confirmed, and it has no duplicate or by-design
refutation although the diff skeptic has both. This unit rewrites the spec kind's skeptic sentence so
a finding is confirmed when its claim is true at any rubric grade, refuted in named cases only, and
judged by RE-RUNNING the evidence unit 2 makes every spec finding carry.

## 2. Scope (IN)

- **S1** — The spec kind's skeptic sentence in `tools/workflows/tier2-review.template.js` is
  rewritten. CONFIRM when the finding's claim is true of the spec set, and of the tree where the claim
  is about the tree, at any rubric severity; the rubric grades it. The new sentence does not contain
  the words "unbuildable or wrong". Observed by AC1.
- **S2** — The same sentence names SIX refutation cases, each by its own clause: (1) a non-goal or a
  parked fork withholds what the finding asks; (2) the cited section already says it; (3) the premise
  is false on re-probe; (4) BY DESIGN, a case the BY DESIGN block covers; (5) a DUPLICATE, of a prior
  round's original or of another finding in this batch, with the reason opening `duplicate of id=<n>`
  for an in-batch survivor or `duplicate of prior <ref>` for a prior original; (6) a PREFERENCE that
  names no defect the rubric grades, not even a low. The sixth is §8 F1. Observed by AC1.
- **S3** — Every spec-kind skeptic line carries the finder's evidence after the fix, as
  ` | evidence: <text>`, folded to one line by the existing `renderCell`, so an absent evidence reads
  `-`. The skeptic is told to RE-RUN the command or RE-READ the `read: <path>:<line>` the evidence
  names, say in `reason` what it observed, and refute a finding whose evidence does not reproduce.
  "Does not reproduce" means the observation contradicts the claim. A probe the skeptic could not run
  inside its bound falls to the existing default by the finder's grade, never to a refutation by
  itself. Absent evidence means the skeptic probes for itself and never confirms on the finder's word.
  Observed by AC1 and AC2.
- **S4** — A claim about code or a record is checked against that code or record, not against the
  spec's description of it. Stated in the S1 sentence. Observed by AC1.
- **S5** — The spec-kind verify prompt carries the PROBE POLICY block unit 2 renders under each
  spec finder's LENS line, the same bytes, before `Findings to judge:`. One copy of the read-only
  rule, never a skeptic-worded second (§8 F3). Observed by AC3.
- **S6** — A refutation whose reason opens `duplicate of id=<n>` is checked by the harness, spec kind
  only, after the existing join. When `<n>` is the finding's own id, is not in the same batch, or is
  not CONFIRMED, the refutation is ORPHANED: the finding is demoted to UNVERIFIED exactly as a
  contradicted one is, its ledger reason reads `duplicate of an unconfirmed id`, a `WARNING:` line
  names the ids, and the spec-kind RUN INTEGRITY block counts them (§8 F2). The scan does not run on
  the diff kind, whose duplicate refutation names no surviving id. Observed by AC4 and AC5.
- **S7** — The diff kind is untouched: its finder, skeptic and synthesis prompts, and its probe
  prompt, are byte-identical before and after this unit (shared invariant 2). Observed by AC5.
- **S8** — The tier2-review self-test gains the arms of §7's `New arm:` line, written and not run
  in the pass, and its `FLOOR_ASSERTIONS` rises by the number of assertions they add. Observed by AC6.

## 3. Non-goals (OUT)

- `VERDICT_SCHEMA`. Its fields, its `required` list and its three verdicts stay as they are.
- The `uncertain` default by the finder's grade (`TOOL-aSightedSkeptic-6` §8 F3). A finding the
  skeptic cannot establish is still refuted at medium or low and answered `uncertain` at blocker or
  high; S3 only says that a probe which could not run is that case, not a non-reproduction.
- The diff kind's skeptic, and the diff kind's own duplicate refutation, which names no surviving id.
- Checking a `duplicate of prior <ref>` reason against `priorFindings`. A prior original is fixed
  text the round is not judging, so a wrong prior citation loses nothing this round found.
- A duplicate ACROSS batches. A skeptic sees only its own batch; the synthesis already merges
  confirmed findings of one defect into one item, so a cross-batch duplicate is confirmed twice and
  merged, never lost.
- `REVIEW_SHAPE`. `TOOL-aEvidencedLens-1` moves it once for the build (shared invariant 5), and this
  unit adds no input, so `inputPrint` is unchanged. A verify file written between that unit's landing
  and this one's, under the old sentence, would be reusable; no run happens between them.
- The finder's PROBE POLICY text and the `evidence` field's shape. Both are
  `TOOL-aEvidencedLens-2`'s.
- A governance carrier. `memory/guides/REVIEW-PROTOCOL.md` says "default-refute skeptics" for both
  kinds, which stays true, and states no spec-kind refutation list (shared invariant 11).
- The kit version. The main loop bumps it once at the close (shared invariant 7).

### Edges

- **consumes-from** `TOOL-aEvidencedLens-2` — the REQUIRED `evidence` string on every spec finding and the PROBE POLICY block, both of which this unit hands to the skeptic; without them S3 re-runs nothing and S5 has no block to copy.
- **hands-off** `TOOL-aEvidencedLens-12` — the fold that carries `evidence` onto the skeptic line. S3 folds it through `renderCell`, which also escapes every `|`, so a pipe-bearing command reaches the skeptic altered; that unit replaces the fold with a line-break-only one (round-1 spec audit, id 36, HIGH).

## 4. Design

### Evidence

Read at `b3950dc7` on 2026-10-05, whose `tools/` tree equals BASE `028b5cac`:
`git diff --stat 028b5cac b3950dc7 -- tools/` prints nothing. Line numbers are PINNED to that read
and move as units 1 and 2 land first; the identifiers do not.

- The spec skeptic sentence (`:889`) confirms "real, and it makes the spec unbuildable or wrong" and
  refutes three cases, none of them a duplicate or by-design. The diff sentence (`:890`) refutes
  "by-design / duplicate".
- The rubric (`:380-386`) defines `low` for the spec kind as "would differ only cosmetically or in a
  comment", and the synthesis is told to grade confirmed findings by it, so a LOW is a grade the
  skeptic sentence makes unreachable.
- The skeptic line (`:901-903`) is `id=<n> [<grade>] lens=<lens> <ref> — <claim> | impact: … | fix: …`.
  The stubs in `tools/workflows/tier2-review.test.sh` read only `id=(\d+) \[` and the
  `(<n> verdicts, ids <list>)` substring, so appending a field after the fix moves neither.
- `renderCell` (`:1061`) is a top-level function declaration, hoisted through the script body, and
  folds every line-break run to one space; it is the one existing one-line folder in the file.
- The join (`:941-954`) demotes a contradicted id by deleting it from `verdictById` and keeps it in
  `conflicts`; the ledger (`:1043`) writes `contradictory verdicts` as its reason. S6 is that shape
  with a second set.
- The skeptic is handed `renderBrief('skeptic')` (`:887`), so it already sees the PRIOR ROUND block
  and the BY DESIGN block the refutation cases name.

### The sentence

The spec kind's sentence, as the build writes it. Wording may tighten; each clause stays, and AC1's
markers are the bolded words, which the arm reads.

```
You are an adversarial skeptic. For EACH finding below, try hard to REFUTE it. Read the cited spec
at the cited section and the siblings it names; a claim about code or a record is checked against
that code or record, never against the spec's account of it. Then re-run the finding's evidence
under the PROBE POLICY above: run the command it names, or re-read the path and line it names, and
say in `reason` what you observed.
"confirmed" when the claim is TRUE of the spec set, and of the tree where it makes a claim about the
tree, AT ANY RUBRIC SEVERITY: the rubric grades it, confirmation does not.
"refuted" in these cases only: (1) a NON-GOAL or a PARKED FORK withholds what it asks; (2) the cited
section ALREADY SAYS it; (3) the premise is FALSE ON RE-PROBE, including evidence that does not
reproduce; (4) BY DESIGN, a case the BY DESIGN block covers; (5) a DUPLICATE, opening `reason` with
`duplicate of id=<n>` for another finding in this batch that you CONFIRM in this same answer, or
`duplicate of prior <ref>` for a prior round's original; (6) a PREFERENCE that names no defect the
rubric grades, not even a low.
Evidence that reads `-` was not recorded: probe the claim yourself and never confirm on the finder's
word. A probe you could not run inside its bound is a finding you cannot establish; apply the
default by the finder's grade, and never call it evidence that does not reproduce.
```

### Data flow

```
spec finder ── finding {file, where, severity, claim, impact, fix, evidence}   (unit 2)
      │
      ▼
skeptic line: id=<n> [<grade>] lens=<lens> <ref> — <claim> | impact | fix | evidence: renderCell(evidence)
      │
      ▼
verdict {id, verdict, reason, …}  ── join (unchanged) ── conflicts demoted (unchanged)
      │
      ▼  spec kind only
orphan scan: refuted ∧ reason ~ /^duplicate of id=(\d+)/ ∧ (n = own id ∨ n ∉ own batch ∨ n not confirmed)
      → orphanDuplicates; verdictById.delete(id); ledger reason 'duplicate of an unconfirmed id'
```

The scan runs after `for (const id of conflicts) verdictById.delete(id)`, so a survivor already
demoted by a conflict is not confirmed and its duplicates are orphaned with it. The batch test reads
the existing `batches` array. An orphan falls into `noVerdict`, so the existing `NO usable verdict`
line counts it; the dedicated `WARNING:` line says which of those were orphaned duplicates.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `orphanDuplicates` | const `Set` | not graded: the lexicon grades function names |

No function is minted. The scan is inline beside the conflict demotion it mirrors.

### Rollout

Edit the template, regenerate the render with `bash tools/workflows/check-protocol-parity.test.sh --render`,
and commit both together (shared invariant 1). Before editing, copy the pre-pass render with
the `git show` of `tools/workflows/tier2-review.js` at HEAD into the run's scratch directory; AC5 compares
against it. The pass's direct checks are §6's stub runs and greps; the arms of S8 run once at
VERIFYING, beside their reading against the pre-pass render.

### Files touched (estimate)

`tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` · `tools/workflows/tier2-review.test.sh`

### Alternatives rejected

- **F2 (a), warn on an orphaned duplicate and keep the refutation.** It reports the loss and keeps
  it: the defect leaves the confirmed set with a log line nobody under a mandate reads. The demotion
  already has a precedent in this file, the conflict demotion, and an UNVERIFIED finding reaches the
  build harness's disposal, which can still refute it with a reason.
- **F2 (c), trust the skeptic's duplicate.** A wrong in-batch duplicate is the one refutation whose
  error the harness can detect from the ids alone, so trusting it leaves a cheap check unmade.
- **F3 (b), a skeptic-worded copy of the probe policy.** Two copies of one read-only rule drift; the
  diff kind's history in this file is a run of such pairs, each later closed by a unit.

## 5. Production-readiness checklist

- security — the skeptic now RUNS commands the finder named. The PROBE POLICY bounds them: read-only
  under `repo`, scratch only, every command bounded, no bar or suite. A finder-supplied command is
  agent output; the skeptic runs it under the same policy it would apply to its own probe, and the
  gate guard refuses a suite before `VERIFYING` regardless.
- perf / scale — one re-probe per finding in each batch. A batch holds up to ⌈raw/5⌉ findings, so a
  40-finding run hands each skeptic eight probes, each bounded by the policy's timeout.
- error / empty / loading states — absent evidence renders `-` and is probed fresh; a probe that
  cannot run follows the grade default; an orphaned duplicate is demoted, counted and announced.
- observability — the orphan `WARNING:` line, the ledger reason, and the RUN INTEGRITY count.
- risks — confirming at any grade raises the LOW count, and under `TOOL-aEvidencedLens-7` and
  `TOOL-aEvidencedLens-8` every spec-audit LOW is promoted into the minors batch. Refutation case (6)
  is what keeps a pure preference out of that batch. Confirming at any severity also RAISES the
  precision a round reports, and BUILD-METHOD M4 ends a chain of promotions only when a promoting
  round's precision falls below the review protocol's floor, so this unit makes that bound slower to
  reach. `TOOL-aEvidencedLens-8` §5 states the interaction and where the generation bound was parked.
- testing — the arms of S8 over stub agents.
- migration — none: no schema or input changes, and REVIEW_SHAPE is already moved by unit 1.
- user docs — N/A: no `args` field is added and no carrier states the skeptic sentence.

## 6. Acceptance criteria

`u3-check.js` and `pre-u3.js` below live in the run's scratch directory, outside the tree.
`u3-check.js` is a driver copying the `runReview` AsyncFunction shape of
`tools/workflows/tier2-review.test.sh` with recording stubs; it is not the suite and runs in seconds.

- **AC1** — When `node u3-check.js tools/workflows/tier2-review.js` runs a spec-kind review
  over stub agents, every `verify:` prompt carries `AT ANY RUBRIC SEVERITY`, each of `NON-GOAL`,
  `ALREADY SAYS`, `FALSE ON RE-PROBE`, `BY DESIGN`, `duplicate of id=`, `duplicate of prior` and
  `PREFERENCE`, `could not run inside its bound` and `apply the default by the finder's grade`, and
  the sentence about a claim on code or a record; none carries `unbuildable or wrong` and none
  carries `not a refutation`.
  Red when: any marker is absent, or the old confirmation test survives in the spec prompt.
- **AC2** — When the same driver hands a spec finding whose `evidence` is `cmd: grep -c x a.md -> 0`,
  a second whose evidence spans two lines, and a third with none, each `verify:` line carries
  ` | evidence: ` after ` | fix: `, the two-line evidence on one line, the third as `evidence: -`, and
  the prompt says to re-run or re-read it and that absent evidence is never confirmed on the finder's
  word. `grep -c "evidence: " tools/workflows/tier2-review.js` prints more than the same grep over
  `pre-u3.js`.
  Red when: the line lacks the field, a line break in evidence starts a new prompt line, or the
  re-run instruction is absent.
- **AC3** — When the driver runs a spec-kind review, the text from `PROBE POLICY` to the next blank
  line in each `verify:` prompt equals, byte for byte, the same slice of each `find:` prompt.
  Red when: the verify prompt lacks the block or carries different bytes.
  fixture: needs `TOOL-aEvidencedLens-2`'s block in the render; the tree holds none at BASE, so this
  is observable only after that unit lands, which its order guarantees.
- **AC4** — When the driver's skeptic stubs answer, in one batch, id 1 `confirmed` and id 2 `refuted`
  with reason `duplicate of id=1`, id 2 stays refuted; when they answer id 1 `refuted` and id 2
  `refuted` with `duplicate of id=1`, the return's `unverified` counts id 2, its ledger row reads
  `verdict` `unverified` with reason `duplicate of an unconfirmed id`, a `WARNING:` log line names
  id 2, and the `synth` prompt's RUN INTEGRITY block names one orphaned duplicate. A reason naming
  the finding's own id, or an id in another batch, is orphaned the same way.
  Red when: an orphaned duplicate stays refuted, a confirmed survivor's duplicate is demoted, or the
  demotion is silent.
- **AC5** — When `node u3-check.js --compare pre-u3.js tools/workflows/tier2-review.js`
  runs the same diff-kind args over both renders, every `resume:probe`, `find:`, `verify:` and
  `synth` prompt is byte-identical between them; `node tools/workflows/check-workflow-syntax.js tools/workflows/tier2-review.js`,
  `bash tools/workflows/check-verifier-fanout.sh` and `bash tools/workflows/check-review-join.sh`
  each exit 0. A second diff-kind run over both renders, whose skeptic stubs answer id 1 `refuted`
  and id 2 `refuted` with reason `duplicate of id=1` in one batch, returns the same `refuted` and
  `unverified` counts and the same ledger rows from both renders, and logs no orphan `WARNING:` line.
  Red when: any diff-kind prompt differs, the orphan scan demotes a diff-kind duplicate, or the edit
  broke the parse, the fan-out grammar or the id join.
  fixture: `pre-u3.js` is the `git show` of `tools/workflows/tier2-review.js` at HEAD taken before the
  pass edits anything; the comparison is to this unit's predecessor and not to BASE, because
  `TOOL-aEvidencedLens-1` moved the review key that every DURABILITY line carries.
- **AC6** — When `grep -c "spec skeptic:" tools/workflows/tier2-review.test.sh` runs it prints at
  least 5, where the pre-pass file prints 0, and `FLOOR_ASSERTIONS` equals its pre-pass value plus
  the number of assertions those arms add, both figures written in the pass's commit message.
  Red when: an arm of S8 is missing or the floor did not move by the count added.
  figure: DERIVED at observation time from the pre-pass file and the pass's own diff.
  permission: a pass runs no suite; the arms are read at the main loop's VERIFYING run, which also
  reads them RED against `pre-u3.js`.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `review-protocol parity (kit vs dogfood)` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · stub spec findings with one-line, two-line and absent evidence, stub skeptics refuting as a duplicate of a confirmed, a refuted, its own and an out-of-batch id, and a diff-kind run whose verify prompt carries no evidence field and no probe policy · FLOOR_ASSERTIONS rises by the assertions added

The `kit epoch` leg reds from the first unit that moves shipped bytes until the main loop's single
version bump at the close; that is shared invariant 7, not a defect of this unit.

## 8. Open questions

- **F1 — Does "a style preference" survive as a refutation case beside the brief's five?** (a) Drop
  it, as the brief's list does. (b) Keep it, worded as a preference that names no defect the rubric
  grades. Under (a), confirming "at any rubric severity" lets a pure preference be confirmed as a
  LOW, and `TOOL-aEvidencedLens-8` promotes every spec-audit LOW into the minors batch, so taste
  becomes build work. Under (b), a real cosmetic defect, such as a wrong comment or a stale name,
  still grades LOW and is confirmed, because it names a defect. Recommendation (b).
  RESOLVED (agent, 2026-10-05, delegated): (b), the survivor that keeps the rubric's LOW reachable
  without promoting taste.
- **F2 — What happens to a refutation as a duplicate whose named survivor is not confirmed?** (a)
  Warn and keep it refuted. (b) Demote it to UNVERIFIED as a contradicted verdict is, and announce
  it. (c) Trust it. §4 Alternatives rejected records why (a) and (c) lose. Recommendation (b).
  RESOLVED (agent, 2026-10-05, delegated): (b), reusing the conflict demotion this file already has.
- **F3 — Where does the skeptic's read-only rule come from?** (a) The PROBE POLICY bytes unit 2
  renders for the finders, interpolated once more. (b) A skeptic-worded copy. Recommendation (a).
  RESOLVED (agent, 2026-10-05, delegated): (a), one copy of one rule.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the build's shared spec brief, unit 3, and the harness
  template read at `b3950dc7`.
- rev-2 · 2026-10-05 · §3 §4 §5 S3 S6 AC1 AC5 · round-1 spec audit fold. Id 9 (MEDIUM): S6 says the
  orphan scan stays off the diff kind and AC5 runs a diff-kind duplicate refutation over both
  renders. Ids 10 and 31 (MEDIUM): the sentence's last line now applies the grade default instead of
  saying "not a refutation", and AC1 carries its two markers. Id 34 (LOW): base 3640cf58 becomes
  028b5cac, with §4 Evidence restated against it. Id 45 (MEDIUM, its unit-3 half): §5 says
  confirming at any severity slows M4's precision bound. §3 gains the hands-off edge to
  `TOOL-aEvidencedLens-12`, the unit id 36 (HIGH) was promoted to.

## 10. Reuse audit

The probe, run on 2026-10-05:

```
python tools/codebase-map/reuse_lookup.py "skeptic refutes a finding as a duplicate or by design and re-checks the finder's evidence"
```

It ranked name-stem neighbours only (`check`, `checks`, `check_records`, `build_lang_mode_findings`)
and printed `unscanned layers: .sh`; none judges a review finding. No existing seam fits outside the
harness, so the seam this unit extends is the harness's own verify stage in
`tools/workflows/tier2-review.template.js`: the spec skeptic sentence, the skeptic line, `renderCell`
reused as the evidence folder, and the conflict demotion reused as the shape of S6. The recall probe
returned `TOOL-aSightedSkeptic-1` (the skeptic's brief), `TOOL-aSightedSkeptic-6` (the rubric and
the `uncertain` default, both kept), `TOOL-aSightedSkeptic-2` (the fix verdict, untouched) and the
owner's disposal ruling `TOOL-aProbedUnit-9`; none had decided the spec skeptic's confirmation test
or a duplicate refutation for the spec kind. A grep for the old sentence's words across `tools/`,
`memory/guides/` and `skills/` found it only in the template and its render, so no test or carrier
pins it.

Recall terms used: skeptic refute confirmed duplicate by-design spec-audit verdict uncertain rubric severity evidence prior-round

The question passed with them: "how does the spec-audit skeptic decide confirmed or refuted, and
when is a duplicate or by-design finding refuted".
