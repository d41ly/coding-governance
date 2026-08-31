# TOOL-aClosedDocket-1 — M4 gains a disposition for a NON-CONVERGENT exit over a spec

**Status:** OPEN · rev-2 · 2026-08-31 · node a · Tier-2 · base 733552e1 · streams tooling · order 1 · ratified 2026-08-31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aClosedDocket-1.md](../prompts/2026-08-31-prompt-TOOL-aClosedDocket-1.md) | research | TOOL-aClosedDocket-2 TOOL-aClosedDocket-3 |
| [2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round1.md) | spec-audit | TOOL-aClosedDocket-2 TOOL-aClosedDocket-3 |

<!-- /gen:spec-records -->

## 1. Goal

Give `memory/guides/BUILD-METHOD.md` M4 a stated disposition for the case it currently has none for:
a NON-CONVERGENT exit whose review SUBJECT is a spec set, where the standing blockers are defects in
those specs rather than undone work. Today the rule says promote each to a unit, and M2 forbids a
unit that is not a mechanism, so a conforming run cannot follow both.

## 2. Scope (IN)

- **S1** — M4's disposition sentence in `tools/memory-tree/BUILD-METHOD.template.md` is REPLACED, not
  extended, so that it states both dispositions: FOLD as a `rev-N` bump when closing the blocker
  edits a document the review was already reading, PROMOTE to a unit when closing it needs a
  MECHANISM this build does not have. Both terminate, and the sentence says why each does.
- **S1a** — **the edit must be byte-neutral or negative, and this is a hard constraint rather than a
  preference.** Measured at authoring time: `memory/guides/BUILD-METHOD.md` is 24 549 B and its
  template 24 560 B against M1's own 24 576 B cap — 27 and 16 bytes of headroom. M3's delegation
  clause excludes M1's budget, so this run cannot raise the cap and has no ratified exit if the edit
  overruns it. The replacement therefore pays for itself out of M4, and §4 names the sentences it
  trims and why each trim is meaning-preserving.
- **S2** — the split is a TEST a run applies, not a judgement it restates: mechanism-needed promotes,
  document-defect folds. Stated once, in M4, and pointed at from everywhere else.
- **S3** — either disposition owes the same record. The build README's BUILD-LEVEL RULES slot carries
  which one was taken and why, which is where M4 already sends a CEILING exit.
- **S4** — `tools/unattended/unattended.sh`'s NON-CONVERGENT message names both dispositions, because
  a run reads that line at the moment it decides and the guide at the start.
- **S5** — **`tools/unattended/check-unattended.sh` clause 3 accepts a FOLD, and without this the
  whole unit is a rule the bar refuses.** That clause (`:246-303`) requires, for every subject that
  exited NON-CONVERGENT or CEILING, at least one unit id present at HEAD and ABSENT at the run's
  pinned BASE — promotion, machine-enforced as the only disposition. It is `subject:repo` with no
  guard, so it runs on every bar. A fold promotes no id and would red it permanently.
- **S5a** — the fold's machine-readable trace is what clause 3 reads instead. It must be a fact the
  DRIVER writes, not prose a run authors, for the reason every other run-state fact is: an authored
  claim is not evidence. The shape is settled in §8 Q3.
- **S6** — `tools/unattended/SKILL.template.md` and its render restate the promotion rule in full at
  `:571-573`. They are registered method carriers, so they move with M4 or the two disagree.
- **S7** — the memory-tree and unattended kit versions move and the renders regenerate;
  `check-kit-versions.sh` and `check-verdict-epoch.sh` are the authorities on which carriers, not
  this list.

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
| `tools/memory-tree/BUILD-METHOD.template.md` | S1, S1a, S2, S3 — the disposition sentence and its trim. AUTHORED SOURCE |
| `memory/guides/BUILD-METHOD.md` | RENDERED from the row above, never hand-edited |
| `tools/unattended/unattended.sh` | S4 the message; S5a the fold fact |
| `tools/unattended/check-unattended.sh` | S5 — clause 3 |
| `tools/unattended/SKILL.template.md` and its render | S6 — the restated rule |
| `tools/unattended/PROTOCOL.template.md` and its render | S4/S5a — only where they restate the rule |
| `tools/memory-tree/README.md`, `tools/unattended/kit.toml`, template markers | S7 — the versions |

### Clause 3 is ALSO vacuously satisfiable today, and this unit does not fix that

Measured on `aProvenReuse`, the build that motivated this one: two subjects exited NON-CONVERGENT, so
clause 3 demanded two ids new since BASE — and found three, because that run's BASE was its own
opening commit and the generated units region was EMPTY there. Every one of its ORIGINAL units read
as newly promoted. The clause passed, and not one blocker had been promoted.

That is a second defect in the same clause and it is NOT in this unit's scope: closing it means
distinguishing an id that appeared because a unit was promoted from one that appeared because the
region was first rendered, which needs a signal neither the region nor the run-state file carries
today. It is filed rather than folded, and S5 is written so as not to depend on it — the fold trace
is a positive fact, so it satisfies clause 3 whether or not the id delta is trustworthy.

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
- **Testing** — S5's clause-3 arm, plus the guide's byte budget and the kit version gates. There is no
  arm that can assert a run applied the RIGHT disposition; §7 says so rather than implying coverage.
- **Migration/rollback** — revert; no state.

## 6. Acceptance criteria

- **AC1** — `memory/guides/BUILD-METHOD.md` M4 states both dispositions and the test that selects
  between them, and `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0, proving the render
  came from the template rather than a hand-edit.
- **AC2** — `wc -c memory/guides/BUILD-METHOD.md` is **no larger than 24549**, its value before this
  edit, and the template no larger than 24560. Byte-neutral-or-negative, not merely under the cap:
  with 27 bytes of headroom, "under the cap" and "did not grow" are the same requirement and the
  second is the one a reader can check without knowing the cap.
- **AC3** — `bash tools/unattended/unattended.sh --review` prints both dispositions on a
  NON-CONVERGENT verdict. Observed by driving a fixture to a non-shrinking second round.
- **AC4** — `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh`
  both exit 0 after the version moves.
- **AC5** — `bash tools/memory-tree/check-method-carriers.sh` exits 0, the leg that grades M4's
  carriers and the first to notice a pointer this edit broke.
- **AC6** — a fixture run-state file recording a NON-CONVERGENT exit and a FOLD trace, with NO new
  unit id since its BASE, passes `bash tools/unattended/check-unattended.sh`. This is S5's whole
  point and it must be observed, because the same fixture reds the leg today.
- **AC7** — the same fixture with the fold trace REMOVED still reds
  `bash tools/unattended/check-unattended.sh`, naming the subject. Without this, AC6 cannot
  distinguish a clause that accepts a fold from one that stopped checking.
- **AC8** — `grep -c` for the promotion-only wording in `tools/unattended/SKILL.template.md` and its
  render returns 0 after S6, and both carriers state the same pair of dispositions M4 does.

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
- **Q2 — should S4 also change `PROTOCOL.template.md`?** **FACT-QUESTION · RESOLVED (agent,
  2026-08-31, delegated):** the probe is `grep -n "PROMOTED\|promot" tools/unattended/PROTOCOL.template.md`
  and the observation that decides it is whether the file states the rule or points at it. It can
  return zero, which is the liveness half. Edit it only where it RESTATES; where it points, editing
  would create the second copy this repo's rule against restatement exists to prevent.
- **Q3 — what is the fold's machine-readable trace, given S5a says it must be driver-written?**
  **RESOLVED (agent, 2026-08-31, delegated):** `--review` itself writes it. It already computes the
  NON-CONVERGENT verdict, already writes the round row, and is the only actor that knows the exit
  occurred at the moment it occurs; adding a fold marker to the row it already writes costs no new
  verb, no new file and no new grammar. The alternatives were a new `--fold` verb (a second verb for
  a fact the first one already has) and an authored README sentence (which S5a rejects, because an
  authored claim is not evidence). Reuse of the seam that already writes the row beats both.

## 9. Revision log

- rev-2 · 2026-08-31 · round-1 spec-audit fold. Blocker B1: BUILD-METHOD has 27 bytes of headroom
  against its own cap and M3's delegation excludes M1's budget, so S1 became a REPLACEMENT that pays
  for itself and S1a states the constraint. Blocker B2: `check-unattended.sh` clause 3 already
  machine-enforces promotion as the ONLY disposition and is unguarded, so a fold would red the bar
  permanently — S5 and S5a bring the check with the rule, and Q3 settles the trace. H1 added S6, the
  SKILL carriers that restate the rule in full. L1 corrected a §5 reference to a scope item that does
  not exist. §4 also records that clause 3 is separately VACUOUS on the prompt path, measured on
  aProvenReuse, and why that is filed rather than folded here.
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
