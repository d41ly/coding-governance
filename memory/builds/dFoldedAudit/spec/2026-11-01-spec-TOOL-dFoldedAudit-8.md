# TOOL-dFoldedAudit-8 — dClosedLoop's unbuilt specs and its frozen design take the same rules

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base 74274869 · streams tooling · order 80

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 |
| [2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 |
| [2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 |
| [2026-11-01-build-TOOL-dFoldedAudit-8-1-claim-fold-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-8-1-claim-fold-return.md) | journal | TOOL-dFoldedAudit-1 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-8-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-8-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-8-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-8-build-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-8-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-8-fix-brief.md) | research | TOOL-dFoldedAudit-1 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-8-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-8-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

dClosedLoop's chain does not ship the promote-everything rule into `tools/loop/`: three unbuilt specs
take the new spec-audit rule by rev bump, and the one frozen design clause that states the old rule
takes a deviation record quoting the owner. Everything else in the chain is left as it stands.

## 2. Scope (IN)

- **S1** — `TOOL-dDeclaredLoop-32` takes spec subjects out of its strict-fall exit, and closing-review
  follow-ups and fix passes keep it, as the design record's tag [closedloop] says
  (`memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`). Its `**Carries:**`
  pin moves with the amended clause. Observed by AC1, AC2, AC3.
- **S2** — `TOOL-dDeclaredLoop-20` limits its dispose row to built work or a new mechanism, and rebases
  S9 on M4's rewritten sentences. Observed by AC1, AC4.
- **S3** — `TOOL-dFairHearing-17` re-points its chain rule to the new stop. Observed by AC1, AC5.
- **S4** — One deviation record under `memory/builds/dClosedLoop/build/` amends `cl-dClosedLoop-0117`,
  quotes the owner, and carries v2's two neighbouring catalogue rows in its text. Observed by AC2, AC6.
- **S5** — The pass touches nothing else: no live-claimed build, no landed record, not v2 and not
  `PLAY-dClosedLoop-1`. Observed by AC7.

## 3. Non-goals (OUT)

- `PLAY-dClosedLoop-1`, which restates no design fact.
- The bytes of v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`.
  It is frozen (`:1809-1811`), and a clause moves only by a record.
- Historic text that records why a unit exists: "M4 promotes every minor" in TOOL-dBoundRoles-66,
  TOOL-dDeclaredLoop-56, TOOL-dIndexedDesign-38 and TOOL-dFurnishedOrders-29, the resolved records in
  TOOL-dFairHearing-23 and TOOL-dTrueNorth-10, and DL-20's resolved F1, which keeps its `:144`.
- Retiring or refolding any unit already promoted. The brief rules that this change is not retroactive.
- dDeclaredLoop's README contract row, `memory/builds/dDeclaredLoop/README.md:95`, keeps its baseline
  pin: `memory/builds/dFairHearing/README.md:76` kept `5c5896a3` through the same move, so that table
  records the packet and not the head.
- Hand `spec-revised` records for the three specs. HYGIENE's deviation paragraph owes one for a spec
  "once its code has started", and none of the three has; `tools/memory-tree/deviation_join.py:589-606`
  will list each as an `audit` member, a listing under the host's `report` value that never moves an
  exit (`:144`), and each of the three is already past its audited rev for an earlier edge fold.
- A spec audit of these revisions, which the brief's non-goals exclude. Each revision reads as moved
  past its audited rev until a later run audits it.
- `tools/loop/`, which dDeclaredLoop builds.
- Writing `memory/DECISIONS.md`: TOOL-dFoldedAudit-1's row carries the clause.

### Edges

- **consumes-from** `TOOL-dFoldedAudit-1` — M4's rewritten sentences, which DL-20's S9 and FH-17's
  chain rule point at, and the decision row naming `cl-dClosedLoop-0117`, without which the record's
  owner approver has no row to cite

## 4. Design

### The pass

This pass is a gov-spec-writer pass, not a gov-builder one. Each write sits under a spec folder, which
`tools/hooks/scratch-guard.js:1057-1085` admits only from a `writes = spec` role, or under a `build/`
folder, which it does not class. `tools/workflows/unattended-unit.js:53-59` is not the route, because
its typed prompt tells the agent to hand a spec change back. The main loop dispatches the unit with
every path of the files list below declared under `--dispatch --writes`, spawns one `gov-spec-writer`
with this spec as its brief, and commits once.

The role regenerates no index, so that commit is the main loop's: it runs
`python tools/memory-tree/gen_build_index.py --write` and stages the as-built view with the record,
because a commit adding a matching record re-renders the view in that same commit
(`tools/memory-tree/README.md:28`).

**Re-read first.** Before any write the pass reads `bash tools/unattended/unattended.sh --claims` and
each of the three specs whole. A build reading `live` is not touched: `dDeclaredLoop` and
`dFairHearing` read `landed` and `dSafePassage` read `live` on 2026-11-01, and a change in the first two
parks that spec's edit with the reason. Edits below match on their old text, never on a line number. If
an old text is gone, the pass parks that edit and does not adapt it. Each new rev is the file's current
rev plus one, and the header's date moves to the pass's date.

### The revision of `TOOL-dDeclaredLoop-32`

`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md`, rev-2 to rev-3.

| # | Where | Edit |
|---|---|---|
| E1 | H1 | "every until and while loop ends on a non-decrease" becomes "every closing-review and fix-pass loop ends on a non-decrease"; the rest stays |
| E2 | header | `**Carries:** cl-dClosedLoop-0117@166df103 whole` moves to the record's hash, below |
| E3 | §1 | the first sentence becomes the text below |
| E4 | S2 | "`verb_review` passes it for every subject" becomes "`verb_review` passes it for the build slug and for no spec subject" |
| E5 | S3 | "The non-decrease test keeps reading the blocker and high count under every value." becomes the text below, and "Observed by AC10." becomes "Observed by AC10, AC11." |
| E6 | S4 | appends the text below, and its "Observed by AC4." becomes "Observed by AC4, AC11." |
| E7 | §3 | the `deriveRoundState` bullet's "where the fourth argument is unset" becomes "where the fourth and sixth arguments are unset"; Edges gains the bullet below |
| E8 | §4 predicate | the fence takes the sixth argument below |
| E9 | §4 under the value table | "Under `until-clean` and `while-finding` a round" becomes "Under `while-finding` a round", and the paragraph gains the sentence below |
| E10 | §4 Rollout | "A spec audit or closing review whose rounds fall" becomes "A closing review whose rounds fall" |
| E11 | §6 | AC11 below |
| E12 | §7 | the first `New arm:` line's `covers` list gains AC11 |
| E13 | §9 | the rev line below |

E3:

```
Every closing-review follow-up under `review.follow-up`'s `while-*` value and every fix pass against one
acceptance red ends at the first round whose blocker and high count does not strictly fall, or at
whichever of `review.max-rounds` and `flow.route-backs` it reaches first. A spec audit under
`review.design.rounds`' `until-*` values ends at its target or its bound, and BUILD-METHOD M4's
spec-audit rule disposes its findings and stops its chain.
```

The rest of §1 is kept, and the sentence that follows opens "A follow-up's or a fix pass's open
findings" in place of "Its open findings".

E5:

```
The non-decrease test keeps reading the blocker and high count on the build slug and on a fix pass. A
spec subject takes no non-decrease test: `verb_review` passes `review_state` a sixth argument,
`no-fall`, so an `until-*`, `one` or `fixed-count` subject ends at its target or its bound, and whether
another generation runs is the chain's verdict, not this loop's.
```

E6:

```
A spec subject's target is always ` · to units`: `promotion_target` is not called for it, because a
budget does not outrank a spec audit's chain stop (dFoldedAudit's README, owner, 2026-11-01).
```

E7's Edges bullet:

```
- **consumes-from** external — BUILD-METHOD M4's spec-audit rule, which owns a spec subject's disposal
  and its chain stop; TOOL-dFoldedAudit-1 states it
```

E8, the fence's head line and first NON-CONVERGENT line, the rest unchanged:

```
review_state <prior counts> <count> <bound> [<route-backs>] [<target>] [<no-fall>]   round = prior counts + 1
  no-fall unset, prior non-empty and count >= last prior -> NON-CONVERGENT
```

E9, the sentence appended: "A spec subject under `until-clean` takes no such exit: it runs to its
target or its bound."

E11:

```
- **AC11** — When the sliced `review_state` runs `review_state "3" 3 3 "" 3 no-fall` it prints
  `CONVERGING`, `review_state "3 3" 3 3 "" 3 no-fall` prints `BOUNDED`, and the same flat call with no
  sixth argument prints `NON-CONVERGENT`; and on the fixture with the budget spent, a spec subject's
  terminal row carrying `disposition promote` carries ` · to units`, where the build slug's carries
  ` · to asks`.
  Red when: `verb_review` passes `no-fall` to no subject, so a flat spec audit ends NON-CONVERGENT and
  a spent budget sends its new mechanism to an ask no chain audits.
```

E13:

```
- rev-3 · <date> · §1 §3 §4 §6 §7 · S2 S3 S4 AC11 · spec subjects leave the strict-fall exit, for the
  owner's 2026-11-01 ruling (TOOL-dFoldedAudit-8), and the `**Carries:**` pin follows the amends row of
  `<the record's stem>`; follow-ups and fix passes keep the rule.
```

### The revision of `TOOL-dDeclaredLoop-20`

`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-20.md`, rev-2 to rev-3.

E1, the `item.review.dispose` row's Routes cell, kept on the row's one line. "unbuilt to `item.review.fold`; built to new units or
asks by `review.findings`; NON-CONVERGENT or CEILING promoted to units while budget remains and to asks
after" becomes:

```
a local finding on an unbuilt spec to `item.review.fold`; built work and a new mechanism to new units or
asks by `review.findings`; NON-CONVERGENT or CEILING on built work or for a new mechanism promoted to
units while budget remains and to asks after
```

The `item.review.fold` row keeps its text, because it promotes "as `item.review.dispose` promotes".

E2, S9 becomes:

```
- **S9** — BUILD-METHOD M4's disposal paragraphs (`tools/memory-tree/BUILD-METHOD.template.md`, rendered
  at `memory/guides/BUILD-METHOD.md`, as TOOL-dFoldedAudit-1 rewrote them) point at `review.findings` and
  `review.unverified` for the count and the unverified route, their default reading unchanged: a spec
  exit still disposes by nature, and `review.findings` counts what that rule promotes. Observed by AC9.
```

E3, §9:

```
- rev-3 · <date> · §4 · S9 · the dispose row is limited to built work or a new mechanism and S9 rebases
  on M4 as rewritten, for the owner's 2026-11-01 ruling (TOOL-dFoldedAudit-8).
```

AC9 stands. Its `wc -c` still bounds the guide, and TOOL-dFoldedAudit-1 leaves room for S9's pointer.

### The revision of `TOOL-dFairHearing-17`

`memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md`, rev-3 to rev-4. The §3 bullet
at `:64-65` becomes the text below, and the §9 line follows it.

```
- No reading of a chain stop, which `gap-review-21` also names as a precision floor. The clause states
  the round state only, and a chain's stop is BUILD-METHOD M4's derived verdict.
```

```
- rev-4 · <date> · §3 · the chain rule points at M4's derived verdict, the precision floor having left
  M4, for the owner's 2026-11-01 ruling (TOOL-dFoldedAudit-8).
```

### The deviation record

`memory/builds/dClosedLoop/build/<date>-build-TOOL-dFoldedAudit-8-deviation-81.md`, its date the pass's.
The name's id is this unit's, which a record may carry across builds, and `81` is unused there. Its
title is `# TOOL-dFoldedAudit-8 deviation 81 — cl-dClosedLoop-0117 takes spec audits out of the
strict-fall exit`, its binding `**Serves:** deviation TOOL-dFoldedAudit-8`, and its fields, each one line
(`tools/memory-tree/deviation_join.py:212-266`):

| Field | Value |
|---|---|
| Departs from | `` `cl-dClosedLoop-0117@166df103` `` |
| Hand-off | `design-revised` |
| Before | the clause's text, copied from the as-built view's row |
| After | the fenced text below, unbroken |
| Cause | `owner ruling` |
| Reason | the owner's sentences, quoted verbatim from the prompt record: "promote only findings that need new mechanisms", the fold sentence and "Stop the chain at the first round whose highs all sit in the previous round's own promotions"; then that v2:1260 and v2:1261 are catalogue rows carrying no clause id, so they take no row in the view, and that this After is what reads over them for a spec audit |
| Evidence | `memory/builds/dFoldedAudit/prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md`; final-questions `:193-194`; `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-2-orient-dclosedloop.md`, `v2:1260`, `v2:1261` and `v2:1769` |
| Risk | `loosening`: a clause's scope narrows, which final-questions' table prices at the owner |
| Approver | `` owner, `TOOL-dFoldedAudit-1`, the decision row naming the clause, the ruling quoted in the prompt record above `` |
| Follow-through | `amends cl-dClosedLoop-0117@166df103` |
| Caused-by | `TOOL-dFoldedAudit-1` |

The After text, whose `|`-free line carries the two neighbours by name:

```
the convergence routing: every `while-*` value of a closing-review follow-up and every fix pass against one acceptance red ending at a NON-CONVERGENT round, whose findings are promoted, to units while budget remains and to asks after, never folded into another round, a CEILING round's open findings promoted the same way, and every review loop, the closing review's included, held to `review.max-rounds` rounds and, a spec audit apart, ended at whichever of it and `flow.route-backs` it reaches first, both promoting its open findings the same way, a blocking item's open work past `flow.route-backs` promoted to a new unit while budget remains and then ending as `flow.on-exhausted` says, and a non-blocking item's going to asks, every `until-*` value of a spec audit ending instead at its target or its round bound, the build method's spec-audit rule disposing its findings, a local finding folded into its spec and only a finding needing a new mechanism promoted, and its chain stopping on that rule's derived verdict or holding for the owner at its ceiling, which neither `flow.route-backs` nor `flow.rework-budget` outranks, seen red on a planted flat follow-up sequence that runs another round and on a planted sequence whose blocker and high count falls every round past `review.max-rounds`, the round after the limit refused and the report reading CEILING, and on a planted acceptance red that never greens, which must reach a terminal (P39, the owner's SL-3, keeping FR-9, the parked debt's review, the owner's FK-4-5, the owner's ruling of 2026-11-01)
```

Its hash is `afb50a20`, PINNED at 2026-11-01. `design_lib.derive_clause_hash` re-derives it from the
After line, and it reproduced both `166df103` from the view's row and `b793fdd5` from deviation 171's
After, so it is the hash the carries join compares. If the clause moved before the pass, the pass stops
and parks: the `Departs from` hash would no longer be the head.

### Data model

None. Every write is an authored record or a spec's text. The view's row is generated.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `no-fall` | a `review_state` argument value, specified for dDeclaredLoop's build | none |
| `deviation-81` | a record number within dClosedLoop's `build/` | none |

### Migration

None. Each spec stays DEFERRED, and its build run reads the new rev.

### Rollout

The three edits reach code only when dDeclaredLoop and dFairHearing build. Nothing ships here.

### Files touched (estimate)

- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md`
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-20.md`
- `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md`
- `memory/builds/dClosedLoop/build/2026-11-01-build-TOOL-dFoldedAudit-8-deviation-81.md`

The commit also carries the generated `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`
and the generated regions of two READMEs, none of which this pass writes.

### Alternatives rejected

- **One record per neighbouring row.** v2:1260 and v2:1261 hold no clause id, so a record could amend
  nothing the view renders. The clause states the carve-out and names both keys, which is the one place
  a reader of the chain looks.
- **An approver of `spec writer`.** It passes the host's `author-recorded` value today, but
  final-questions `:194` prices an owner's ruling at "the owner, quoted", and `deviation.approval`'s
  catalogue default is `by-risk`, under which it would be refused.
- **A new row in `memory/DECISIONS.md` for this unit.** TOOL-dFoldedAudit-1's row already records the
  ruling, and a second row would be one fact twice.
- **A `no-fall` test by subject name inside `review_state`.** `review_state` knows no subject, and the
  brief's [scope] tag branches at `verb_review`'s `subj = slug` split.
- **Leaving `flow.route-backs` on a spec subject.** A spec subject's generations are fresh subjects, so
  the bound reads a loop that never accumulates rounds, and the README rules a budget does not outrank R1.

## 5. Production-readiness checklist

- security — no new surface; the record's owner approver is graded by the join.
- perf / scale — N/A: four records.
- error / empty / loading states — a moved old text or a `live` claim parks that edit by name.
- observability — each revision's revision-log line and the record's `Since` citation in the view.
- risks — the record's approver is listed as refused until the decision row reaches the mainline,
  because `tools/memory-tree/deviation_join.py:715-733` reads rows there so a run cannot approve itself
  with a branch-only row. Under the host's `report` value that listing moves no exit, and the landing
  clears it. A later chain build reading DL-32's rev-3 before this build lands would see rev-2, which
  the claim check at the pass does not prevent.
- testing — the pass runs §6's reads; the main loop stages each arm of §7 on a scratch copy.
- migration — none.
- user docs — N/A: no page under `help/` covers a held spec.

## 6. Acceptance criteria

- **AC1** — When `grep -m1 '^\*\*Status:'` runs over each of the three specs, the headers read rev-3,
  rev-3 and rev-4, and `grep -c 'TOOL-dFoldedAudit-8'` over each prints at least 1 with the new rev's
  line present in that spec's §9.
  Red when: a spec's text moved with no rev bump, so the revision high-water lies.
  figure: the three revs are PINNED at 2026-11-01; each is the file's rev at the pass plus one.
- **AC2** — When a `python -c` probe imports `tools/memory-tree/design_lib.py` and prints
  `derive_clause_hash` over the record's After line, the result equals the hash on DL-32's
  `**Carries:**` line, and `grep -c 'cl-dClosedLoop-0117@166df103' <DL-32>` prints 0.
  Red when: the record lands and DL-32 keeps the old pin, so the carries join reads a stale pin.
- **AC3** — When `grep -c 'no-fall'` runs over DL-32 it prints at least 4, and
  `grep -c 'passes it for every subject'` prints 0.
  Red when: the predicate fence and S2 disagree, so a builder reads two rules for a spec subject.
- **AC4** — When `grep -c 'built work or for a new mechanism'` runs over DL-20 it prints 1, and
  `grep -c 'BUILD-METHOD.md:144'` prints 1, the resolved F1 and no scope item.
  Red when: S9 keeps the line citation, which moved when M4 was rewritten.
- **AC5** — When `grep -c "floor's chain rule"` runs over FH-17 it prints 0, and
  `grep -c 'derived verdict'` prints at least 1.
  Red when: the bullet still points at a sentence M4 no longer holds.
- **AC6** — When a `python -c` probe runs `deviation_join.read_record` over the record, `malformed` is
  empty; `grep -c 'promote only findings that need new mechanisms'` over it prints 1; and
  `git log --format=%H -1` over the view and over the record name one commit, and `grep -c` finds the
  record's stem in the view.
  Red when: the commit stages the record and not the view, so the head design and the view disagree.
- **AC7** — When `git diff --name-only 74274869 HEAD -- memory/builds/dSafePassage` runs it prints
  nothing, and the same diff over v2 and `memory/builds/dClosedLoop/spec/` prints nothing; and
  `bash tools/unattended/unattended.sh --claims`, read at the pass, shows no touched build `live`.
  Red when: a live run's spec is edited, which the brief refuses.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `policy fixtures`

New arm: tools/memory-tree/check-memory-hygiene.sh · covers AC1 · no new code, check 12's rev-logged branch over this pass's specs, staged by deleting one revised spec's new revision-log line on a scratch copy · none

New arm: tools/check-spec-tokens.py · covers AC2 · no new code, the carries join's stale-pin branch, staged by restoring `166df103` on DL-32's `**Carries:**` line on a scratch copy · none

New arm: tools/memory-tree/gen_build_index.py · covers AC6 · no new code, the view's drift branch, staged by restoring the view's row while the record stands · none

The pass is a records pass and may write no suite, so each line above re-observes an existing branch on
this unit's own population, and the main loop records RED and GREEN for each at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the design record's [closedloop] tag and the brief's item 8.
- rev-2 · 2026-11-01 · §4 · the unit 8 fix brief's item 1. Three §4 headings opened with another build's
  id, which the anchor grammar reads as this folder's claim, so check 13 named each id claimed by two
  build folders. Each heading now opens "The revision of"; no text cited them, and no edit moves.

## 10. Reuse audit

The seams are the records' own: a rev bump with a `**Carries:**` pin moved after an `amends` row is
`memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md:375` beside its deviation 171,
and the record grammar is `memory/HYGIENE.md:658-680`. No code changes, so no new mechanism is added.

`python tools/codebase-map/reuse_lookup.py "revise an unbuilt spec with a rev bump and record a design
deviation citing the owner"` ranked `read_spec_revisions` and `read_records`, the join this record
feeds, and `design_lib.derive_clause_hash`'s module; none is a thing to extend here, and the reuse_lookup
hits confirm the grammar. The orientation's line cites were each read against the file. One stale
reading: it counted `v2:1260` and `v2:1261` as clauses, and both are catalogue rows outside `[chain]`, so
the record amends one clause and carries them in its text.

Recall terms used: deviation record frozen design v2 follow-through amends cl-0117 dClosedLoop spec-revised rev-bump
