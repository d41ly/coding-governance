# TOOL-dBoundRoles-47 — one criterion across the fence, the strip and the graded text: with units 38, 45, 24 and 41 landed, an anchor planted in a typed `--input` value is refused

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 21 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-49 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-48 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the eight promoted specs 37 to 44
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`) confirmed
finding **id 9 at HIGH**, report item **H1**. Ids 1 and 17 share the item at HIGH and take
`TOOL-dBoundRoles-46` and `TOOL-dBoundRoles-45`.

Id 9 is the grounding face of the item. `TOOL-dBoundRoles-41` §4 keeps an authored block in the graded
text as "the block itself", and after `TOOL-dBoundRoles-38` that block carried a fence, which
`TOOL-dBoundRoles-24` S2 strips before it scans. 41 §3 says the unit does not lean on the fence, yet its
AC2 and 24's AC2 both rest on what the fence does. `TOOL-dBoundRoles-45` removes the fence from a typed
value. No criterion in the tree observes the four units together: each unit's own arm stages its own
break, so a later change that fences typed values again, or strips them from the graded text, passes
every arm while the anchor check stops grading the text the order authors.

This unit adds the cross-unit criterion the report's fix asks for: a render with 38, 45, 24 and 41
landed plants a backticked `record:` anchor in `--input question=`, sees it refused, and is seen red
against a render that fences the value. It repairs `TOOL-dBoundRoles-41` and builds one step after it
(order 21).

## 2. Scope (IN)

- **S1** — The case, in `tools/roles/adopt-roles.test.sh`, one render pair. A `--role gov-builder`
  render hands `--input spec=` a scratch spec whose prose quotes the backticked span
  `record:TOOL-tFix-9@000000000000`, and passes `--input question=` holding the same span. It exits
  non-zero, names the span once, and writes no file. The same render
  with the question holding plain words exits 0 and writes its prompt file, so the span inside the
  handed spec is not graded. Observed by AC1.
- **S2** — The staged break. A scratch copy of the roles kit whose `render_handoff` wraps the typed value
  in `render_handed_fence`, as `TOOL-dBoundRoles-38` S2 first specified, renders S1's first case with
  exit 0: the planted span is stripped and the arm reads red. The pass makes this observation once, by
  hand, and the `New arm:` line records it for the close. Observed by AC2.
- **S3** — The arm names its four producers. The case's comment names `TOOL-dBoundRoles-38`, `-45`, `-24`
  and `-41` and the one fact each contributes, so a change to any of them that turns the case red finds
  its reason beside it. Observed by AC3.

## 3. Non-goals (OUT)

- The fence scope and the render's line rule: `TOOL-dBoundRoles-45`'s, for id 17.
- The spawn guard's reading of a typed block: `TOOL-dBoundRoles-46`'s, for id 1.
- The graded text itself, `check_anchors` and the strip: `TOOL-dBoundRoles-41`'s and
  `TOOL-dBoundRoles-24`'s, unchanged.
- The report's left-shift text as a general checklist entry for every spec that changes how a block is
  wrapped. S1's case is the regression for this one.

### Edges

- **consumes-from** `TOOL-dBoundRoles-41` — the graded text inside `render_handoff`, which S1's second render shows leaves the handed spec's span out (id 9)
- **consumes-from** `TOOL-dBoundRoles-45` — the typed value written unfenced, which S1's first render shows `check_anchors` grades and S2's break shows the fence would hide (ids 9 and 17)
- **hands-off** `TOOL-dBoundRoles-52` — the render pair, which unit 52 re-roles onto `gov-orienter`, a role that reads its typed and its handed input; this unit's AC1 and AC2 are answered `amended rev-<n>` at the revision unit 52's pass writes (id 13 of the round-1 audit of units 45 to 51)
- **hands-off** `TOOL-dBoundRoles-58` — the cross-unit case, which unit 58 widens by a typed diff render on `gov-skeptic`, a read check on every render and renders derived from the typed set (ids 2, 39 and 50 of the round-1 audit of units 45 to 51)

## 4. Design

### Evidence

- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-41.md` §4 "The graded text" keeps an
  authored block whole, and §3 says the unit does not lean on the fence.
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md` S2 strips fenced blocks before
  the scan, and its AC2 plants a `record:` anchor in `--input question=`.
- `tools/roles/handoff.py:380-386` appends a typed value as one more `reads` block, so the render's
  treatment of it is the only thing that separates it from a handed one.

### What each producer contributes

| Unit | Fact the case reads |
|---|---|
| `TOOL-dBoundRoles-38` | handed content is fenced, so the spec's span sits in a fence |
| `TOOL-dBoundRoles-45` | a typed value is written raw |
| `TOOL-dBoundRoles-24` | `check_anchors` refuses an anchor the order does not hand, and skips fenced spans |
| `TOOL-dBoundRoles-41` | the graded text leaves a handed block's content out and keeps a typed value |

One span planted in both places separates the two halves: a refusal that names it once proves the typed
copy was graded, and a clean second render proves the handed copy was not.

### Inventory

Minted: the case and its scratch spec. No function, constant or plant.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 21. `TOOL-dBoundRoles-11` holds order 21 and writes no file this unit writes;
this unit's two producers are at orders 12 and 20.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- **A criterion in each producer.** Each producer's spec is converged, and a criterion inside one unit
  stages only that unit's break; the defect is the seam between them.
- **Two separate cases.** The single span in both places is what tells a graded typed value from a
  graded handed one; split across two renders, a check that grades everything passes the first and a
  check that grades nothing passes the second.

## 5. Production-readiness checklist

- security — guards the anchor check's coverage of authored text against a later wrapping change; no
  new write path.
- perf / scale — two renders in the existing fixture.
- error / empty / loading states — the refusal case writes no file, which the case asserts.
- observability — the case names its four producers.
- risks — a later unit that renames the typed input changes the case's argument; the case fails loudly
  rather than passing.
- testing — AC1 to AC3 by render, a staged copy and grep; the arm of §7 at the close.
- migration — none.
- user docs — none: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the roles adopter fixture runs S1's two renders of `handoff.py render --role gov-builder`,
  the first exits non-zero, its stderr names `record:TOOL-tFix-9@000000000000` once, and no prompt
  file is written; the second exits 0 and writes its prompt file.
  Red when: the typed value's span passes, or the handed spec's span refuses.
  fixture: a scratch repository with the roles kit installed, under `%TEMP%`, short-pathed.
- **AC2** — When the same first render runs against a scratch copy of `tools/roles/handoff.py` whose
  `render_handoff` wraps typed values in `render_handed_fence`, it exits 0.
  Red when: the case passes against the fence that hides the typed value, so it cannot see the defect.
  fixture: the scratch copy is built under the run's scratch path by the pass.
- **AC3** — When `grep -n 'TOOL-dBoundRoles-45' tools/roles/adopt-roles.test.sh` runs, it names the case's
  comment, which also names units 38, 24 and 41.
  Red when: the case carries no account of the producers whose seam it observes.

## 7. Gates

`roles adopter self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 · S1's render pair, staged by a `render_handoff` that wraps typed values in `render_handed_fence`, which stops the planted span from refusing · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 41 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 37 to 44, id 9
  (HIGH, item H1, shared with ids 1 and 17), the report's cross-unit criterion.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-52 and -58, promotions of the round-1 audit of units 45 to 51; nothing else moved.

## 10. Reuse audit

The seam is the roles adopter suite's render fixture (`tools/roles/adopt-roles.test.sh`), where
`TOOL-dBoundRoles-24` AC2 and `TOOL-dBoundRoles-41` AC1 already put their cases.
`python tools/codebase-map/reuse_lookup.py "a render case that plants one anchor in a typed argument and in a handed file"`
ranked `render`, `anchors`, `anchor_at` and `render_cards_md`, none a render case of the roles kit, so no
existing seam fits beyond the suite's fixture.

Recall terms used: `python tools/memory-recall/query.py "how are typed input values kept from forging executor lines in a work order" --terms "typed input question diff fence handed content fact line marker forged authored framing refusal"`
