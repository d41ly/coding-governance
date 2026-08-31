# TOOL-aClosedDocket-1 — M4 gains a disposition for a NON-CONVERGENT exit over a spec

**Status:** OPEN · rev-3 · 2026-08-31 · node a · Tier-2 · base 733552e1 · streams tooling · order 1 · ratified 2026-08-31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aClosedDocket-1.md](../prompts/2026-08-31-prompt-TOOL-aClosedDocket-1.md) | research | TOOL-aClosedDocket-2 TOOL-aClosedDocket-3 |
| [2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round1.md) | spec-audit | TOOL-aClosedDocket-2 TOOL-aClosedDocket-3 |
| [2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round2.md) | spec-audit | TOOL-aClosedDocket-2 TOOL-aClosedDocket-3 |

<!-- /gen:spec-records -->

## 1. Goal

Give `memory/guides/BUILD-METHOD.md` M4 a stated disposition for the case it currently has none for:
a NON-CONVERGENT exit whose review SUBJECT is a spec set, where the standing blockers are defects in
those specs rather than undone work. Today the rule says promote each to a unit, and M2 forbids a
unit that is not a mechanism, so a conforming run cannot follow both.

## 2. Scope (IN)

**This unit is the DOCUMENT change and nothing else.** The gate clause and the driver-written fact
that rev-2 carried here are `TOOL-aClosedDocket-4`, split out at round 2's NON-CONVERGENT exit
because M2 states verbatim that *"a separate document, gate, adopter or generated artifact is a
separate unit with its own id and spec"*.

- **S1** — M4's disposition sentence in `tools/memory-tree/BUILD-METHOD.template.md:137` is REPLACED,
  not extended, so it states both dispositions: FOLD a defect in a document the review read, PROMOTE
  one needing a mechanism this build lacks. Both terminate, and the sentence says why each does.
- **S1a** — **the replacement fits in the existing headroom, measured rather than promised.** The
  sentence it replaces is 217 B; the conforming replacement is **228 B**, `+11`. The template has
  **16 B** of headroom (24 560 of M1's 24 576 cap) and the render 27 B. Rev-2 said §4 would name a
  trim budget and §4 named none, which round 2 raised as B1 — there is no trim, because none is
  needed. If a later wording exceeds 16 B the unit is blocked on arithmetic and the remedy is a
  shorter sentence, never a raised cap: M3's delegation clause excludes M1's own budget.
- **S2** — the split is a TEST a run applies, not a judgement it restates: mechanism-needed promotes,
  document-defect folds. Stated once, in M4, and pointed at from everywhere else.
- **S3** — either disposition owes the same record: the build README's BUILD-LEVEL RULES slot, which
  is where M4 already sends a CEILING exit.
- **S4** — `tools/unattended/SKILL.template.md:571-573` and its render restate the promotion rule in
  full. They are registered method carriers, so they move with M4 or the two disagree.
- **S5** — the memory-tree kit version moves and the renders regenerate. `check-kit-versions.sh` and
  `check-verdict-epoch.sh` are the authorities on which carriers, not this list.

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
| `tools/memory-tree/BUILD-METHOD.template.md` | S1, S1a, S2, S3 — the sentence. AUTHORED SOURCE |
| `memory/guides/BUILD-METHOD.md` | RENDERED from the row above, never hand-edited |
| `tools/unattended/SKILL.template.md` and `.claude/skills/unattended/SKILL.md` | S4 |
| `tools/memory-tree/README.md`, template markers | S5 — the version |

### The authority this unit is built under

M3 veto 2 puts a change to a governance carrier outside what a standing mandate delegates, and
`BUILD-METHOD.template.md` is one. The owner's instruction names `TOOL-aProvenReuse-3` by id, which
IS that turn — for the row as written. The row states one thing: the promotion sentence has no legal
referent when the subject is a spec. So S1 adds the missing case and S2 states its test; anything
that would change what M4 demands of a DIFF-subject exit is outside the turn and is N2.

### Why a fold is the right disposition and not a weaker one

Promotion terminates because a promoted unit is audited as a SPEC — M4's own reasoning. When the
blocker IS a spec defect, promotion does not terminate: the new unit's spec enters the same audit
that produced the blocker. A fold terminates because the document stops being wrong, and the loop has
already stopped by rule.

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

One commit. Two of the four files it touches ARE generated — `memory/guides/BUILD-METHOD.md` and
`.claude/skills/unattended/SKILL.md` — so the commit includes their re-render, and rev-1's
"nothing is generated from it" was wrong from the moment S4 existed. Nothing flips and no state
moves.

## 5. Production-readiness checklist

- **Security** — N/A. Prose in a guide and two rendered carriers.
- **Performance** — N/A.
- **Error states** — N/A. This unit adds no predicate; `TOOL-aClosedDocket-4` is where the predicate
  went, and rev-1's "no new predicate" was true only after that split.
- **Observability** — the guide states both dispositions; the line a run reads at the moment it
  decides is `TOOL-aClosedDocket-4`'s.
- **Testing** — S5's clause-3 arm, plus the guide's byte budget and the kit version gates. There is no
  arm that can assert a run applied the RIGHT disposition; §7 says so rather than implying coverage.
- **Migration/rollback** — revert; no state.

## 6. Acceptance criteria

- **AC1** — `memory/guides/BUILD-METHOD.md` M4 states both dispositions and the test that selects
  between them, and `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0, proving the render
  came from the template rather than a hand-edit.
- **AC2** — `wc -c tools/memory-tree/BUILD-METHOD.template.md` is **at most 24576** and
  `wc -c memory/guides/BUILD-METHOD.md` at most 24576 after the edit. Measured before: 24 560 and
  24 549. **No gate enforces M1's cap** — round 2 established that — so this criterion is the only
  thing that measures it, which is why it names the number rather than pointing at a leg.
- **AC3** — `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh`
  both exit 0 after the version move.
- **AC4** — `bash tools/memory-tree/check-method-carriers.sh` exits 0, the leg that grades M4's
  carriers and the first to notice a pointer this edit broke.
- **AC5** — `grep -c` for the promotion-only wording in `tools/unattended/SKILL.template.md` and
  `.claude/skills/unattended/SKILL.md` returns 0 after S4, and both state the same pair M4 does.
- **AC6** — `bash tools/unattended/adopt-unattended.sh --check` exits 0, so the SKILL render is
  regenerated from its template rather than hand-edited.

## 7. Gates

`bash tools/run-gates/run-gates.sh`. Named because this unit reaches each: `memory hygiene`,
`kit/dogfood doc parity`, `method carriers`, `unattended skill wiring`.
`bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh` for AC3.
`bash tools/unattended/run-unattended-gates.sh`, which that script's own header mandates for
`tools/unattended/` work and which S4 makes this unit owe.
What no gate here checks, twice over: whether a run facing a NON-CONVERGENT exit applies the right
disposition, which is a judgement no predicate reads; and M1's own byte budget, which nothing
enforces and AC2 is therefore the only measurement of.

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

## 9. Revision log

- rev-3 · 2026-08-31 · round-2 spec-audit fold, at the loop's NON-CONVERGENT exit (3 blockers then
  4). B2 SPLIT this unit: M2 states verbatim that a document and a gate are separate units, and rev-2
  had a document, a gate clause and a driver fact under one id — the gate half is now
  `TOOL-aClosedDocket-4`, promoted at the exit, which is promotion in its literal sense. B1 settled
  the arithmetic by measuring rather than promising: the replacement is 228 B against 217 B, +11
  into 16 B of headroom, so there is no trim budget because none is needed. B3 swept §4 Rollout and
  §5, which still said "nothing is generated" and "no new predicate" after S4 added two rendered
  carriers. §7 gained the self-test DoD its own script header mandates.
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
