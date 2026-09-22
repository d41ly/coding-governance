# TOOL-aTetheredRecord-3 — the retrofit: all 76 records gain a binding line

**Status:** CLOSED · rev-4 · 2026-08-20 · node a · Tier-1 · base 96141aed · streams tooling · ratified 2026-08-17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-17-review-TOOL-aTetheredRecord-1-1.md](../reviews/2026-08-17-review-TOOL-aTetheredRecord-1-1.md) | spec-audit | TOOL-aTetheredRecord-1 TOOL-aTetheredRecord-2 TOOL-aTetheredRecord-4 TOOL-aTetheredRecord-5 TOOL-aTetheredRecord-6 TOOL-aTetheredRecord-7 |

<!-- /gen:spec-records -->

## 1. Goal

Bring the whole existing corpus into conformance before anything grades it. The owner ruled out a
date cutoff, so the 76 records are scope rather than history. Because the parser from
`TOOL-aTetheredRecord-2` is inert, these edits land against a green bar and the gate arrives last,
onto a corpus already proven conformant by the gate's own predicate.

## 2. Scope (IN)

- **S1** — Re-run the binding census with the shipped predicate and commit it as a record under this
  build's `build/` folder. It is the provenance for every inferred value, and it is a record, so it
  carries its own binding line.
- **S2** — Author the binding line for every record whose spec is stated in its own body. This is the
  largest class and the one requiring no judgement.
- **S3** — Author the binding line for records whose build has exactly one spec-defined id, where the
  body does not state it.
- **S4** — Author the binding line for set-scoped and whole-build records, enumerating the ids.
- **S5** — Author the unbound form, with its reason, for records that precede or outlive every spec
  in their build.
- **S6** — Author the binding line for the one non-markdown record, as a comment.
- **S7** — Add conformant binding lines to the non-spec fixtures inside
  `tools/memory-tree/check-memory-hygiene.test.sh`, so that the harness's existing global assertions
  survive the arrival of check 21.

## 3. Non-goals (OUT)

- **No content edit beyond the binding line.** A record is an account of a moment. Correcting its
  prose, its verdict line or its findings is not this unit, and would make the retrofit unreviewable
  by mixing a mechanical insertion with judgement.
- **No filename changes.** Fork A resolved to rename every record, and that is
  `TOOL-aTetheredRecord-7`, which runs after this unit because it DERIVES each target name from the
  binding line this unit authors. Keeping them separate also keeps two judgements apart: which spec a
  record is about, and what the file should therefore be called.
- **No verdict-line backfill.** Measured 12 of 53 review records carry the line M4 requires. That is
  a real gap in the same head region of the same files, and folding it in here would smuggle a second
  rule into a mechanical pass. It is a recommendation with its own unit.
- **No repair of the dead pointer** in the sole `prompts/` record. Recorded, not fixed here.

## 4. Design

### The adjudication precedence

Every binding value comes from exactly one of these, tried in order, and the rule that produced it is
recorded inline on the line itself when it is not rule 1:

1. **The record's own body.** It names a spec id, a spec path, or a unit label the build README maps
   to an id. Authoritative.
2. **The build README's authored unit table**, where the record names a wave, a group or a phase that
   the table resolves to ids.
3. **Single-spec inference**, and only where the build has exactly ONE spec-defined id. Then the
   record can serve nothing else.
4. **The unbound form**, with the reason stated.

The filename ordinal is NEVER evidence. It is a round counter on its own sequence and treating it as
a binding is the precise defect this build exists to remove.

A value from rule 2 or 3 carries an inline note saying so, so a reviewer grades the inference in the
file rather than in a commit body no gate reads.

Each authored BOUND line also carries the KIND token from `TOOL-aTetheredRecord-2` §4; the unbound
form takes none, because there is no relation for a kind to describe and the parser classifies a
kind-bearing `none` line as malformed. The kind is read from the same evidence and by the same
precedence: a record calling itself a pre-code pass over a spec is a `spec-audit`, one naming a
commit range is a `diff-review`, and the filename is not evidence for the kind either. A
COMMISSIONING brief takes `research` whatever its H1 says — it precedes the specs, so it cannot be a
pass over one, and letting its phrasing make it a `spec-audit` would manufacture review coverage.

*(AC2 was deleted at rev-3 and the numbering deliberately keeps its gap: the template numbers
acceptance items so reviews can cite them stably, and renumbering would silently repoint every
citation already written against this set.)*

### Inventory — the classes and their handling

| Class | Handling |
|---|---|
| the record states its spec | rule 1, no note |
| the record is set-scoped over several specs | rule 1 or 2; ids enumerated, never wildcarded |
| the record covers the whole build | ids enumerated from the build's spec-defined set at authoring time |
| the record covers a second build's units too | those ids are named; a fully qualified id crosses builds by construction |
| the record precedes every spec in its build | the unbound form plus the inverse line naming what it commissioned |
| the record's build has no spec at all | the unbound form, reason citing the build README |
| the record's work was rejected and no spec was minted | the unbound form, reason citing the disposition |

MEASURED after the pass: **six** records take the unbound form — a build that shipped before the
spec-format ratchet reached it and holds no spec at all; two design passes whose scope the build
README records as rejected or as preceding the set; two commissioning censuses that produced specs
rather than serving them; and this build's own design-pass record. That six is the number
`TOOL-aTetheredRecord-4` pins. An earlier draft predicted three, which is why the spec says the count
is measured here rather than asserted in advance.

### Migration

Batched by class, one kind of judgement per commit, so a reviewer reads one decision rule at a time.
After each batch: re-render the index, re-run the checklist for the committed range, stage. The bar
is green after every commit in the sequence, because nothing yet enforces the line.

The retrofit's checklist is the gate's own predicate — `--print-bindings` from
`TOOL-aTetheredRecord-2`. A separate seed list could disagree with the gate; the same predicate
structurally cannot.

### Files touched (estimate)

76 records, one to two lines each; one new census record; the hygiene test file's fixtures.

### Alternatives rejected

**Seed a waiver instead.** That is a cutoff wearing a registry's clothes, and the owner ruled it out
for this repo. It remains the right answer for an ADOPTER, whose corpus nobody here can read, and
that asymmetry is `TOOL-aTetheredRecord-6`'s subject.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — 76 files, hand-authored in batches.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A; a record either carries the line or is reported.
- observability — `--print-bindings` reports the remaining unbound set after every batch.
- risks — the real risk is a FABRICATED binding: a plausible id that was never the record's subject.
  Mitigated by the precedence rule, the inline inference note, and the committed census. The
  filename-ordinal temptation is named and banned because it is the most available wrong answer.
- testing + left-shift gates — S7 keeps the existing harness assertions valid; check 21 arrives next
  and is what prevents regression.
- migration / rollback — per-batch commits, each revertible.
- user docs — none; the rule's prose home lands in `TOOL-aTetheredRecord-2`.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --print-bindings` runs after the final
  batch, it prints zero `A` rows (absent plus malformed) and zero `B` rows, and its `N` count equals
  the number `TOOL-aTetheredRecord-4` pins.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --check` runs after each retrofit
  commit, it is clean.
- **AC4** — When `python tools/memory-tree/corpus_ids.py --check` runs, it is green — no authored
  binding introduced an orphan id, which is the free resolution check doing its work.
- **AC5** — When `bash tools/run-gates.sh` runs at every commit in the sequence, it is green.
- **AC6** — When the census committed by S1 under `memory/builds/aTetheredRecord/build/` is read,
  every binding produced by precedence rule 2 or 3 carries its inline note, and no binding cites the
  filename ordinal as evidence.

## 7. Gates

`memory hygiene (20 checks)` · `build-index selftest` · `bash tools/run-gates.sh` at the push
boundary. The checklist `python tools/memory-tree/gotchas.py --for-diff` runs after each batch.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the adversarial design pass recorded under this build's
  `build/` folder.
- rev-2 · 2026-08-17 · folded the owner's fork resolutions. Fork E ratified ADD-NOW, so every
  authored line now carries a kind token derived by the same precedence as the ids; Fork A ratified
  RENAME-ALL, so §3 hands the filenames to `TOOL-aTetheredRecord-7` and says why they stay separate.
- rev-3 · 2026-08-17 · folded the M4 audit. §4 had instructed authors to put a kind on EVERY line,
  which the landed parser classifies malformed on the unbound form. AC1 reworded onto the four-class
  vocabulary, and AC2 DELETED: its witness emits per-file rows rather than a total, counts two
  non-records, and cannot skip a fenced example — AC1 already asserts the same thing through the
  gate's own predicate. §4 also now fixes the commissioning-brief case, which would otherwise have
  manufactured spec-audit coverage from an H1's phrasing.

- rev-4 · 2026-08-17 · BUILT, and one defect found afterwards by unit 5's render: rule 1 scanned
  forty lines, so two aSiftedPlaybook M4 records bound nine and ten ids by sweeping up ids they CITE
  as prior decisions. Corrected in place. The rule stands as written — the head is the evidence — and
  the executing pass read too far, which is the kind of error a rendered table makes visible and a
  per-file read does not.

## 10. Reuse audit

The retrofit consumes `TOOL-aTetheredRecord-2`'s `--print-bindings` rather than carrying a seed list
of its own — the single seam that matters here, because a seed list and a gate predicate that
disagree is the classic retrofit failure. Resolution reuses check 14 as described in
`TOOL-aTetheredRecord-2` §10, which is what makes AC4 a real assertion rather than a restatement.
No new seam is created. Recall terms: `build slug spec artifact filename header adversarial review
closeout journal bookkeeping convergence naming hygiene`.
