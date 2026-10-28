# TOOL-dIndexedDesign-36 — BUILD-METHOD M6 names the refusals `--dispatch` gained, and stops saying it refuses "on nothing else"

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 5 · advances TOOL-dIndexedDesign-17 · ratified 2026-10-28

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`)
confirmed finding **id 33 at HIGH**, report item **H3**, the item's only id.
`TOOL-dIndexedDesign-1` S2 makes `--dispatch` and the `BUILDING` move refuse FORKED and UNCARRIED
units under `derived-ready`, and a Tier-2 unit with no pinned audit under `ready-plus-audit`;
`TOOL-dIndexedDesign-16` S7 adds a `design.coverage` refusal at `--dispatch`. Yet
`memory/guides/BUILD-METHOD.md:227-228` still reads "What refuses is `--dispatch` at the moment of
the act, on a MISSING or THIN unit and on nothing else", and its source
`tools/memory-tree/BUILD-METHOD.template.md` carries the same sentence. No spec in the set edits it,
so the guide every agent reads before a build states the old refusal set, and the next run reasons
from "nothing else" into an unexpected fail 49.

This unit rewrites that one M6 sentence, in the template and its render together, to name the new
refusals and point at the verbs guide that lists them. It repairs `TOOL-dIndexedDesign-1` and builds
one step after it, at order 5.

## 2. Scope (IN)

- **S1** — The sentence. In `tools/memory-tree/BUILD-METHOD.template.md` M6's `passes-harnessed`
  paragraph, the clause "on a MISSING or THIN unit and on nothing else," becomes "on a MISSING or
  THIN unit, and on a FORKED, UNCARRIED or unaudited one where `design.handoff` or `design.coverage`
  says so (the verbs guide lists which),". The rest of the paragraph is unchanged. Observed by AC1.
- **S2** — The render. `memory/guides/BUILD-METHOD.md` re-renders from the template in the same
  commit, so the two carry the same sentence. Observed by AC2.
- **S3** — The budget. The edit adds at most 120 bytes, and the render stays within M1's declared
  ≤30720 bytes and ≤400 lines at this unit's pass tip. Observed by AC3.

## 3. Non-goals (OUT)

- The refusal set itself and its per-value detail: unit 1 S2 and S6 (the verbs guide entries of
  `--dispatch` and `--phase`) and unit 16 S7 and S12. M6 points there and restates no table, by M1's
  one rule.
- Any other M6 sentence, and M2's paragraph, where `TOOL-dIndexedDesign-8` S12 and
  `TOOL-dIndexedDesign-20` S12 add their sentences after this order.
- M1's budget figure: unchanged.
- The report's left-shift text, a checklist entry asking a spec that adds a refusal to grep the
  guides; no clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-1` — the `design.handoff` refusals of its S2 at `--dispatch`, FORKED, UNCARRIED and an unaudited Tier-2 unit, which S1's sentence names (id 33)
- **consumes-from** `TOOL-dIndexedDesign-16` — the `design.coverage` refusal its S7 adds at `--dispatch`, which S1's sentence names beside the hand-off (id 33)

## 4. Design

### Evidence

- `tools/memory-tree/BUILD-METHOD.template.md:227-228` and `memory/guides/BUILD-METHOD.md:227-228`,
  read 2026-10-28, both read "on a MISSING or THIN unit and on nothing else"; the two files differ
  only by the template's `{{TOOL_ROOT}}` prefixes elsewhere in the paragraph.
- `wc -c` printed 29354 for the render and 29368 for the template on 2026-10-28, against M1's
  ≤30720. PINNED on 2026-10-28; AC3 re-derives it at the pass tip.
- `tools/gate-legs.json` names two legs reading the render: `build-method size` and
  `kit/dogfood doc parity`.

### Inventory

Minted: no identifier. One sentence in one template and its render. Naming cells: none apply.

### Migration

None.

### Rollout

Live at its pass, order 5, one above unit 1's 4, beside `TOOL-dIndexedDesign-7`, whose write set holds
no method carrier. Units 8 and 20 then add their M2 sentences against the headroom this leaves.

### Files touched (estimate)

- `tools/memory-tree/BUILD-METHOD.template.md`: S1
- `memory/guides/BUILD-METHOD.md`: its render, S2

### Alternatives rejected

- **List each value's refusals in M6.** Lost to M1's one rule, that nothing in the method is stated
  anywhere else: the verbs guide owns the table (unit 1 S6), and a second copy here would drift.
- **Delete the clause and say only "what refuses is `--dispatch`".** Lost to the reader the finding
  names: the sentence exists to tell an agent what the script does not refuse, and dropping the set
  leaves that unanswered.

## 5. Production-readiness checklist

- security — N/A: prose in a guide.
- perf / scale — N/A.
- error / empty / loading states — N/A.
- observability — the guide now names the refusal an agent will meet.
- risks — the byte budget is shared with units 8 and 20; S3 caps this edit and AC3 measures it.
- testing — AC1 to AC3 by `grep` and `wc` over the two files.
- migration — none.
- user docs — the guide is the doc; nothing under `help/` names M6's sentence.

## 6. Acceptance criteria

- **AC1** — When `grep -c "THIN unit and on nothing else" BUILD-METHOD.template.md` runs in the
  memory-tree kit, it prints 0, and `grep -c "design.handoff. or .design.coverage" BUILD-METHOD.template.md`
  prints 1.
  Red when: "on nothing else" stands, or the new refusals go unnamed.
- **AC2** — When `grep -n "design.handoff. or .design.coverage"` runs over
  `memory/guides/BUILD-METHOD.md` and over the template, both print the same line text at the same
  line number.
  Red when: the render lags the template.
- **AC3** — When `wc -c memory/guides/BUILD-METHOD.md` and `wc -l memory/guides/BUILD-METHOD.md` run at
  this unit's pass tip, they print at most 30720 and at most 400, and the byte count exceeds the
  pass's base by at most 120.
  Red when: the edit breaches M1's budget or grows past its cap.
  figure: the base count is DERIVED from the pass's base commit; it read 29354 on 2026-10-28.

## 7. Gates

`kit/dogfood doc parity` · `build-method size` · `recall floor` · `recall floor arms` · `memory hygiene`

## 8. Open questions

- **F1 — May this run change a sentence of BUILD-METHOD, a governance carrier (M3 veto 2)?** Options:
  (a) edit M6 under the README's `may: PLAY-dClosedLoop-3` grant, which lifts veto 2 for the carrier
  changes the build's own clauses name, here cl-dClosedLoop-0383's hand-off; (b) leave the sentence
  and file an ask. (b) leaves the finding open, which the severity rule forbids. RESOLVED (agent,
  2026-10-28, delegated): (a), rung 3, the one survivor; the sentence states the refusals the
  clause's own unit adds. grants: PLAY-dClosedLoop-3 BUILD-METHOD M6's refusal sentence.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of this build, id 33
  (HIGH, item H3), repairing TOOL-dIndexedDesign-1 S6 and its Files touched.

## 10. Reuse audit

The seam is the method's own M6 paragraph and its pointer style: M6 already points at the unattended
kit's `--dispatch` for the record of what was dispatched, and S1 points at the verbs guide the same
way. The probe
`python tools/codebase-map/reuse_lookup.py "state which refusals a driver verb makes in the build method guide"`
ranked `build`, `refusal`, `Refusal` and `build_commit`, none a prose carrier, so no
existing seam fits beyond the paragraph itself.

Recall terms used: `python tools/memory-recall/query.py "where does the build method say what --dispatch refuses" --terms "BUILD-METHOD M6 passes-harnessed dispatch refuses MISSING THIN FORKED UNCARRIED design.handoff design.coverage verbs guide"`
