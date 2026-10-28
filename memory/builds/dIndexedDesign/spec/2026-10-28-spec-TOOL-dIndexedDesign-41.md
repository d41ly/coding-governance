# TOOL-dIndexedDesign-41 — the design-exit refusals add no net `fail` site, so `unattended.sh` stays within its refusal ceiling at every pass tip

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 18 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |
| [2026-10-28-build-TOOL-dIndexedDesign-41-promoted-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-41-promoted-fix-return.md) | research | TOOL-dIndexedDesign-46 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-41-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-41-1-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dIndexedDesign-41-promoted-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-41-promoted-fix-brief.md) | research | TOOL-dIndexedDesign-46 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 31 to 38
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`)
confirmed finding **id 3 at HIGH**, report item **H3**, the item's only id. The report's run of
`check-arms.py --emit-floors` printed `tools/unattended/unattended.sh:323:314`, and `.memory-tree.conf:653`
caps that census at 323. `TOOL-dIndexedDesign-16` S7 (order 3) adds `check_design_exit` with its own
`fail 49` refusal. `TOOL-dIndexedDesign-38` S5 keeps exactly one site inside that new function and
retires none, so the census reaches 324. Its S7 claim that the census "stays at or under 323" is false,
and its AC5 cannot pass. `TOOL-dIndexedDesign-1` (order 4) and `TOOL-dIndexedDesign-3` (order 16) add
refusals too, while S5 to S7 land only at order 17.

This unit makes the design-exit refusals net-zero in the passes that add them. `check_design_exit`
returns a composed message and fails at no site of its own. `--dispatch` refuses through its existing
THIN site, made a composed site. The one new site `--phase BUILDING` needs is paid for by folding two
existing `fail 31` sites into one. It repairs `TOOL-dIndexedDesign-38` and takes order 18, one above
unit 38's 17.

## 2. Scope (IN)

- **S1** — In unit 16's pass commit, an act ahead of this unit's order:
  - `check_design_exit` holds no `fail <n> "` site. On a refusal it sets `_dx_msg` to the composed
    message, naming the slug, the first finding and `design.coverage`, and returns 1.
  - At `--dispatch`, the THIN site (`unattended.sh:13655`) becomes the one composed site
    `fail 49 "--dispatch declares a build pass for a unit $_d_why: $unit ($_d_spec)"`. `_d_why` holds
    the THIN clause or `_dx_msg`, and its literal run is the prefix the THIN arm already asserts.
  - At `--phase BUILDING`, `verb_phase` refuses through one new site, the refusal unit 16 S7 gives it,
    whose message opens with the literal `the move into BUILDING is refused by the Design exit: ` and
    ends with `$_dx_msg`.
  - The two `fail 31` sites of `verb_phase` (`:6348`, `:6350`) become one site whose tail is composed.
    Its literal run is the text the arm at `unattended.test.sh:3671` asserts.

  Net: zero sites at unit 16's pass tip. Observed by AC1 and AC2.
- **S2** — In unit 1's pass commit, an act ahead of this unit's order: unit 1's `_hov` policy-read
  refusal and its per-unit hand-off refusal set `_dx_msg` inside `check_design_exit` and add no site.
  This is unit 38 S6, landed earlier. Observed by AC1.
- **S3** — In unit 3's pass commit, an act ahead of this unit's order: unit 3's unreadable
  `review.design` refusal joins the existing `check_authorization` site its fail 52, 54 and 55 family
  uses, and adds no site. This is unit 38 S7, landed earlier. Observed by AC1.
- **S4** — Unit 38 S5 to S7 are true before unit 38's pass, and S5 now reads "no net new site". Unit 38's
  ledger carries the note `TOOL-dIndexedDesign-41 S4` under AC5's answer, naming `check-arms.py`.
  Observed by AC3.

## 3. Non-goals (OUT)

- `REFUSAL_CEILINGS`: unchanged at 323. A raise wants a DECISIONS.md id (`check-arms.py:985`) and is an
  owner turn, which unit 38 §8 F2 refused.
- The refusal codes and their wording, beyond the one composed site and the folded pair: units 16, 1 and 3.
- The verbs guide's refusal list: unit 1 S6 and unit 16 S12, and report id 9's item in
  `TOOL-dIndexedDesign-46`.
- The report's left-shift checklist entry. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-16` — S7's `check_design_exit` and its two callers, whose refusal S1 composes into existing sites in that unit's own pass commit (id 3)
- **consumes-from** `TOOL-dIndexedDesign-1` — its `_hov` read and per-unit hand-off refusals, which S2 composes into `_dx_msg` in that unit's own pass commit (id 3)
- **consumes-from** `TOOL-dIndexedDesign-3` — its unreadable `review.design` refusal, which S3 joins to an existing `check_authorization` site in that unit's own pass commit (id 3)
- **consumes-from** `TOOL-dIndexedDesign-38` — S5 to S7, AC5 and §8 F2, which S4 finds true before that unit's pass (id 3)

## 4. Design

### Evidence

- `tools/memory-tree/check-arms.py:131`, `FAIL_RE = \bfail (\d+) "(.*)$`, finds a site. `:204-221`,
  `signature`, keeps the longest literal run of the message. `:261-264` refuse a site whose run is
  shorter than 12 characters, so a bare `fail 49 "$_msg"` is refused as unarmable. Each composed site
  here keeps a literal run its existing arm already asserts.
- `tools/unattended/unattended.sh:13655` is the THIN refusal of `verb_dispatch`.
  `tools/unattended/unattended.test.sh` asserts its text, which holds the prefix
  `--dispatch declares a build pass for a unit`.
- `unattended.sh:6348` and `:6350` share the text "a run reaches LANDED only from LANDING, … a second
  time: $cur" and differ only by a tail. `unattended.test.sh:3671`, `:3691` and `:3697` assert that text.
- `.memory-tree.conf:653` sets `REFUSAL_CEILINGS` for `unattended.sh` at 323. The census of 323 is the
  report's measurement of 2026-10-28; PINNED, and AC1 re-derives it at each pass tip.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `_dx_msg`, `_d_why` | shell locals in `unattended.sh` | none: locals are not graded |

### Migration

None.

### Rollout

S1 lands in unit 16's pass (order 3), S2 in unit 1's (order 4) and S3 in unit 3's (order 16), each ahead
of this unit's order. Each unit's Edges block names its item, and its builder reads it there. S4 and
AC1 to AC3 are this unit's own pass at order 18, beside `TOOL-dIndexedDesign-40`, which writes no shell
file. `harness arms (fail branches armed or pinned)` reads green at every tip from unit 16's on.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1 to S3, in the passes of units 16, 1 and 3
- `tools/unattended/unattended.test.sh`: the composed sites' arms, unchanged in text
- `memory/builds/dIndexedDesign/build/`: S4's ledger note and the recorded censuses

### Alternatives rejected

- **`fail 49 "$_msg"`, the corrected fix's literal form.** Lost to `check-arms.py:261-264`: a site with no
  literal run of 12 characters is refused, so the composed site keeps the THIN prefix instead.
- **Raise the ceiling.** Lost to M3: the conf gives no run the terms to move it.
- **Retire a site no arm reaches.** Lost on evidence: the two `fail 31` sites are one message with two
  tails, which is a fold, not a deletion of a refusal.

## 5. Production-readiness checklist

- security — no refusal is removed. The folded pair still refuses on both paths.
- perf / scale — none.
- error / empty / loading states — every refusal still names its cause; the composed sites print the
  same text as before for THIN and LANDED.
- observability — `check-arms.py --report` names each composed site's signature.
- risks — an arm keyed on the old THIN or LANDED wording must still match the kept literal run. AC2
  checks the census and the arms together.
- testing — AC1 to AC3 by `check-arms.py` at each pass tip, the driver's own arms and a ledger grep.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/check-arms.py --emit-floors` runs in a worktree at each of the
  pass commits of units 16, 1 and 3, it prints `tools/unattended/unattended.sh` at or under 323 every time.
  Red when: a pass adds a net site.
  figure: 323 is PINNED by `REFUSAL_CEILINGS` at `.memory-tree.conf:653`.
- **AC2** — When `python tools/memory-tree/check-arms.py --report` runs at unit 16's pass tip, the
  composed THIN site and the folded `fail 31` site each read armed. When a scratch copy of
  `unattended.sh` gets a second literal `fail 49 "` site inside `check_design_exit`, `--emit-floors` over
  it prints one more than before.
  Red when: a composed site reads unarmed, or the census does not move on the planted site.
- **AC3** — When `grep -n "TOOL-dIndexedDesign-41 S4"` runs over unit 38's acceptance ledger, it prints
  the note under AC5's answer naming `check-arms.py`.
  Red when: the note is missing or stands as its own `- AC` line.
  permission: at this unit's pass, after unit 38's.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `unattended kit gate` · `memory hygiene` · `recall floor` · `recall floor arms`

## 8. Open questions

- **F1 — How do three items land in passes long before this unit, when the harness places a repair
  after the unit it repairs?** Options: (a) each item is an act in the pass that adds its refusal, named
  in that unit's Edges and this Rollout, with AC1 reading each pass tip. (b) Every item at this unit's
  pass. (c) Raise the ceiling. (b) leaves the census at 324 or more from order 3 to 17. (c) is an owner
  turn (veto 2). RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the one survivor. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 31 to 38, id 3
  (HIGH, item H3), on the skeptic's corrected fix with its literal-run correction, repairing
  TOOL-dIndexedDesign-38 S5 to S7 and AC5.

## 10. Reuse audit

The seams are the driver's existing refusal sites, the THIN site of `verb_dispatch`
(`tools/unattended/unattended.sh:13655`) and the `fail 31` pair of `verb_phase` (`:6348`, `:6350`), and
`check-arms.py`'s census as the measure. No new refusal mechanism is written. The probe
`python tools/codebase-map/reuse_lookup.py "compose several refusal messages into one existing fail site"`
ranked `fail`, `refusal`, `Refusal`, `DesignRefusal` and `read_id_list_refusals`. None composes messages
into a shared site, so no seam fits beyond the sites named. Where the record and source disagree: the
report's corrected fix spells `fail 49 "$_msg"`, and source refuses that shape (`check-arms.py:261-264`).

Recall terms used: `python tools/memory-recall/query.py "how is a fail site census kept under REFUSAL_CEILINGS" --terms "REFUSAL_CEILINGS check-arms emit-floors census fail site unattended.sh composed message armed signature"`
