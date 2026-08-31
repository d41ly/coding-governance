# TOOL-aClosedDocket-1 — M4 gains a disposition for a NON-CONVERGENT exit over a spec

**Status:** OPEN · rev-1 · 2026-08-31 · node a · Tier-2 · base 733552e1 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aClosedDocket-1.md](../prompts/2026-08-31-prompt-TOOL-aClosedDocket-1.md) | research | TOOL-aClosedDocket-2 TOOL-aClosedDocket-3 |

<!-- /gen:spec-records -->

## 1. Goal

Give `memory/guides/BUILD-METHOD.md` M4 a stated disposition for the case it currently has none for:
a NON-CONVERGENT exit whose review SUBJECT is a spec set, where the standing blockers are defects in
those specs rather than undone work. Today the rule says promote each to a unit, and M2 forbids a
unit that is not a mechanism, so a conforming run cannot follow both.

## 2. Scope (IN)

- **S1** — M4's disposition paragraph in `tools/memory-tree/BUILD-METHOD.template.md` gains the
  spec-subject case: standing blockers that are defects IN the reviewed documents are FOLDED as a
  `rev-N` bump with its §9 line and the loop stops; the promotion rule keeps its existing meaning for
  a DIFF subject and for any blocker that names undone work.
- **S2** — the split is stated as a TEST a run can apply, not as a judgement call: a blocker is
  promoted when closing it needs a MECHANISM this build does not have, and folded when closing it
  edits a document the review was already reading.
- **S3** — either disposition owes the same record. The build README's BUILD-LEVEL RULES slot carries
  which one was taken and why, which is where M4 already sends a CEILING exit.
- **S4** — `tools/unattended/unattended.sh`'s NON-CONVERGENT message names both dispositions, because
  a run reads that line at the moment it decides and the guide at the start.
- **S5** — the memory-tree kit version moves and the render is regenerated; `check-kit-versions.sh`
  and `check-verdict-epoch.sh` are the authorities on the carriers, not this list.

## 3. Non-goals (OUT)

- **N1** — changing the CONVERGENCE predicate. Strictly-smaller stays as it is; this unit is about
  what happens at the exit, never about when the exit fires.
- **N2** — changing what promotion means for a diff subject. `aScouredKit` promoted three units at
  such an exit and that outcome stays correct; this ADDS a case rather than replacing one.
- **N3** — `TOOL-dHonouredPark-8`, that `--review` keys convergence on `--subject` alone so a spec
  audit and a closing diff review collide when both name the slug. Adjacent, filed, and a different
  mechanism.
- **N4** — automating the choice. No verb decides which disposition applies; S2 gives the test and the
  run applies it, because "is this a mechanism" is exactly the judgement M2 already asks an author to
  make.

## 4. Design

### Inventory

| Path | Change |
|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | S1–S3 — the disposition paragraph. AUTHORED SOURCE |
| `memory/guides/BUILD-METHOD.md` | S1–S3 — RENDERED, never hand-edited |
| `tools/unattended/unattended.sh` | S4 — the NON-CONVERGENT message |
| `tools/unattended/PROTOCOL.template.md` and its render | S4 — only if the protocol restates the disposition |
| `tools/memory-tree/README.md`, template markers | S5 — the version |

### The authority this unit is built under

M3 veto 2 puts a change to a governance carrier outside what a standing mandate delegates, and
`BUILD-METHOD.template.md` is one. The owner's instruction names `TOOL-aProvenReuse-3` by id, which
IS that turn — for the row as written. The row states one thing: the promotion sentence has no legal
referent when the subject is a spec. So S1 adds the missing case and S2 states its test; anything
that would change what M4 demands of a DIFF-subject exit is outside the turn and is N2.

### Why a fold is the right disposition and not a weaker one

Promotion terminates because a promoted unit is audited as a SPEC — that is M4's own reasoning. When
the blocker IS a spec defect, promotion does not terminate: the new unit's spec enters the same audit
that produced the blocker, and its own fold can produce another. A fold terminates for the same
reason promotion does in the diff case — the document stops being wrong, and the loop has already
stopped by rule.

### Alternatives rejected

- **Leaving the rule and letting each run explain its departure.** Two builds have now done exactly
  that, and both wrote the same explanation. A rule every conforming run departs from is a rule with
  a missing case, not a rule with disobedient readers.
- **Making the fold the only disposition.** It would silently retire `aScouredKit`'s promotion, which
  was correct: three of its blockers named work nobody had done.
- **A verb that decides.** N4. The test is the same judgement M2 already asks for, and a verb that
  guessed it would be a second answer to a question the author must answer anyway.

### Rollout

One commit. The change is to a document and a message; nothing is generated from it and nothing
flips.

## 5. Production-readiness checklist

- **Security** — N/A. Prose in a guide and one message string.
- **Performance** — N/A.
- **Error states** — N/A; no new predicate.
- **Observability** — S4 puts both dispositions in the line a run reads at the moment it decides.
- **Testing** — S6 in §7's sense: the guide's own budget gate and the kit version gates. There is no
  arm that can assert a run applied the right disposition; §7 says so rather than implying coverage.
- **Migration/rollback** — revert; no state.

## 6. Acceptance criteria

- **AC1** — `memory/guides/BUILD-METHOD.md` M4 states both dispositions and the test that selects
  between them, and `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0, proving the render
  came from the template rather than a hand-edit.
- **AC2** — the file still fits its own stated budget: `≤24 KB` and `≤350 lines`, measured with
  `wc -c` and `wc -l` after the edit. M1 makes that budget a constraint of the document, and an edit
  that breaks it is refused by the same rule that admits this one.
- **AC3** — `bash tools/unattended/unattended.sh --review` prints both dispositions on a
  NON-CONVERGENT verdict. Observed by driving a fixture to a non-shrinking second round, not read
  off the source.
- **AC4** — `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh`
  both exit 0 after the version move.
- **AC5** — `bash tools/memory-tree/check-method-carriers.sh` exits 0, since it is the leg that
  grades M4's carriers and would be the first to notice a pointer this edit broke.

## 7. Gates

`bash tools/run-gates/run-gates.sh`. Four legs are named because this unit reaches each:
`memory hygiene`, `kit/dogfood doc parity`, `method carriers` and `unattended kit gate`.
`bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh` for AC4.
What no gate here checks, and it is the honest limit: whether a run facing a NON-CONVERGENT exit
applies the right disposition. That is a judgement, S2 gives it a test, and no predicate reads intent.

## 8. Open questions

- **Q1 — does the fold disposition need a distinct record kind, or does the BUILD-LEVEL RULES slot
  suffice?** **RESOLVED (agent, 2026-08-31, delegated):** the slot suffices. M4 already sends a
  CEILING exit there, the slot is byte-capped so it cannot absorb an essay, and a new record kind
  would need a filename grammar, a hygiene check and a place in the wrap-up derivation — three
  mechanisms for a fact that is one sentence. Reuse of the seam M4 already names beats a new one.
- **Q2 — should S4 also change `PROTOCOL.template.md`?** **RESOLVED (agent, 2026-08-31, delegated):**
  only if that file restates the disposition. It is checked at build time; where the protocol merely
  points at M4, editing it would create the second copy this repo's own rule against restatement
  exists to prevent.

## 9. Revision log

- rev-1 · 2026-08-31 · authored by the aClosedDocket run.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "recording a telemetry log line when a lookup tool runs so
a later check can observe it"` was the set's map probe and returned no seam for this unit — it is a
prose change to a guide, and the guide is the seam. No existing seam fits for the RULE itself; what
this unit reuses is M4's own CEILING-exit convention, which already sends an abnormal disposition to
the build README's BUILD-LEVEL RULES slot, so Q1 needs no new record kind.

Recall terms used: `non-convergent review loop blocker promotion spec subject mechanism unit
disposition wall-clock timing assertion flake elapsed bound contention`. That query returned the two
prior NON-CONVERGENT exits this unit must not contradict — `aScouredKit`, which promoted three units,
and `aBoundedVerdict`, whose standing set was empty after its fold — and `TOOL-dHonouredPark-8`, which
is N3.

Where a hit was STALE: none. M4's current sentence was read at
`tools/memory-tree/BUILD-METHOD.template.md:137` and the driver's message at
`tools/unattended/unattended.sh:3591` at writing time, rather than taken from the backlog row's
description of them.
