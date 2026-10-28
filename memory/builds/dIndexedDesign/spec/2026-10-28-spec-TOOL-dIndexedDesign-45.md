# TOOL-dIndexedDesign-45 — the unattended protocol stops saying `--dispatch` refuses only MISSING and THIN, with no byte added under its size row

**Status:** DEFERRED · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 6 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-46 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 31 to 38
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`)
confirmed finding **id 27 at HIGH**, report item **H7**, the item's only id.
`TOOL-dIndexedDesign-36` fixes the stale refusal claim in BUILD-METHOD M6 only.
`tools/unattended/PROTOCOL.template.md:707` and its render `memory/guides/UNATTENDED-PROTOCOL.md:707`
still say `--dispatch` refuses "on a MISSING or a THIN unit, and on no other state of a unit". Lines
708-709 add "Those two states are the whole of what the verb inspects". No spec of the build names
either carrier. The render measures 66859 bytes against its row of 66860
(`tools/template-size-limits.txt:146`), a row only owner rulings have raised (`:143-145`).

This unit rewrites those two clauses in the template and its render together, so the protocol points at
the verbs guide for the refusal set, and the render shrinks. It repairs `TOOL-dIndexedDesign-36` and
takes order 6, one above unit 36's 5.

## 2. Scope (IN)

- **S1** — The sentences. In `tools/unattended/PROTOCOL.template.md`, the clause "on a MISSING or a THIN
  unit, and on no other state of a unit" becomes "on a MISSING or a THIN unit, and on the further states
  the verbs guide lists". The sentence "Those two states are the whole of what the verb inspects, and it
  accepts a second declaration" becomes "It accepts a second declaration". The rest of the paragraph is
  unchanged. Observed by AC1.
- **S2** — The render. `memory/guides/UNATTENDED-PROTOCOL.md` re-renders from the template in the same
  commit, so the two carry the same text. Observed by AC2.
- **S3** — The budget. The two edits net about 45 bytes fewer, so the render stays at or under its row
  of 66860 and below its base size at this unit's pass tip. Observed by AC3.

## 3. Non-goals (OUT)

- The refusal set itself: units 1 and 16 own it, and the verbs guide lists it (unit 1 S6, unit 16 S12).
  The protocol points there and restates no list.
- BUILD-METHOD M6: `TOOL-dIndexedDesign-36`.
- The size row: unchanged. A raise is an owner ruling (`tools/template-size-limits.txt:143-145`).
- The verbs guide's two missing refusals: report id 9, LOW, in `TOOL-dIndexedDesign-46`.
- The report's left-shift checklist entry. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-36` — its M6 sentence and its pointer to the verbs guide, which S1 mirrors in the protocol so the two carriers state one refusal rule (id 27)
- **hands-off** `TOOL-dIndexedDesign-53` — §10's "which source confirms" and §8 F1's ground, which that unit's S16 corrects by ledger note (id 12)

## 4. Design

### Evidence

- `tools/unattended/PROTOCOL.template.md:705-710` and `memory/guides/UNATTENDED-PROTOCOL.md:705-710`,
  read 2026-10-28, carry both stale clauses at the same lines.
- `tr -d '\r' | wc -c` printed 66859 for the render and 66859 for the template on 2026-10-28; PINNED, and
  AC3 re-derives it at the pass tip. `tools/template-size-limits.txt:146` holds the row 66860.
- `tools/gate-legs.json:129-138`, `unattended protocol size`, runs `check-template-size.sh` over the render.
  `tools/unattended/check-unattended.sh:3150-3151` pairs the template with its render for the
  `unattended kit gate` leg.

### Inventory

Minted: no identifier. Two clauses in one template and its render.

### Migration

None.

### Rollout

Live at its pass, order 6, one above unit 36's 5, beside `TOOL-dIndexedDesign-2`, whose write set holds
no protocol carrier.

### Files touched (estimate)

- `tools/unattended/PROTOCOL.template.md`: S1
- `memory/guides/UNATTENDED-PROTOCOL.md`: its render, S2

### Alternatives rejected

- **List the refusals in the protocol.** Lost to the byte row and to one fact in one place: the verbs
  guide owns the list.
- **Delete the clause and keep "Those two states".** Lost to the reader the finding names: the second
  sentence states the same false set.

## 5. Production-readiness checklist

- security — N/A: prose in a guide.
- perf / scale — N/A.
- error / empty / loading states — N/A.
- observability — every unattended run reads the protocol, which now points at the full refusal set.
- risks — the row has 1 byte of headroom. S1 shrinks the render, and AC3 measures it.
- testing — AC1 to AC3 by `grep` and `wc` over the two files.
- migration — none.
- user docs — the guide is the doc; nothing under `help/` names the sentence.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'on no other state of a unit'` and `grep -c 'Those two states are the whole'` run
  over `tools/unattended/PROTOCOL.template.md`, each prints 0. When `tr '\n' ' '` joins the file and
  `grep -c 'the further states the verbs guide lists'` runs over it, it prints 1.
  Red when: a stale clause stands, or the pointer is missing.
- **AC2** — When the same three greps run over `memory/guides/UNATTENDED-PROTOCOL.md`, they print 0, 0
  and 1.
  Red when: the render lags the template.
- **AC3** — When `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c` runs at this unit's pass
  tip, it prints at most 66860 and less than the same count at the pass's base.
  Red when: the edit grows the render or breaches its row.
  figure: the base count is DERIVED from the pass's base commit; it read 66859 on 2026-10-28.

## 7. Gates

`unattended protocol size` · `unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene`

## 8. Open questions

- **F1 — May this run change a sentence of the unattended protocol, a governance carrier (M3 veto 2)?**
  Options: (a) edit it under the README's `may: PLAY-dClosedLoop-3` grant, as `TOOL-dIndexedDesign-36`
  §8 F1 edits M6 for the same refusals; (b) leave it and file an ask. (b) leaves the finding open, which
  the severity rule forbids. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the one survivor; the
  sentence states the refusals the build's own units add. grants: PLAY-dClosedLoop-3 the unattended
  protocol's `--dispatch` refusal sentence. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 31 to 38, id 27
  (HIGH, item H7), on the skeptic's corrected fix, repairing TOOL-dIndexedDesign-36's Files touched.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-53, promoted by the round-1 spec audit of units 39 to 46; nothing else
  moved.

## 10. Reuse audit

The seam is the pointer style `TOOL-dIndexedDesign-36` S1 gives M6, "the verbs guide lists which", here
applied to the protocol. No new carrier is written. The probe
`python tools/codebase-map/reuse_lookup.py "rewrite a stale sentence in a guide without growing its byte budget"`
ranked `derive_budget_cut`, `build_live_builds_without_activity`, `build_stale_dossiers`,
`check_budgets` and `check_claim_push_lock_stale`. None is a prose carrier, so no existing seam fits
beyond the paragraph and its pointer. The recall query returned scout A's note that `--dispatch` refuses
MISSING and THIN at base (`unattended.sh:13648-13656`), which source confirms.

Recall terms used: `python tools/memory-recall/query.py "where does the unattended protocol say what dispatch refuses" --terms "UNATTENDED-PROTOCOL dispatch refuses MISSING THIN no other state verbs guide template size row byte cap"`
