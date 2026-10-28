# TOOL-dIndexedDesign-51 — unit 38's one-site rule is restated at S22 and S35 before unit 38's pass, and the refusal census is read at every pass commit that changes `unattended.sh`

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 19 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 39 to 46
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md`)
confirmed finding **id 20 at HIGH**, report item **H3**, the item's only id. Report item M1, id 2, is the
same defect's AC5 half at MEDIUM and is batched into `TOOL-dIndexedDesign-53`. `TOOL-dIndexedDesign-41`
S1 leaves `check_design_exit` with no `fail` site, and its S4 restates only unit 38 S5. Unit 38 S22 still
refuses a `--design-exit` exit 2 "through S5's site", and S35 still reads "the variable S5's function
names". A builder of S22 who looks for that site finds none and adds a `fail 49`, taking the census to
324 at order 17. `check-arms.py --emit-floors` prints `tools/unattended/unattended.sh:323:314`, and
`.memory-tree.conf:653` caps it at 323. Unit 41 AC1 reads the census only at the passes of units 16, 1
and 3, while twelve units write `unattended.sh`.

This unit takes the report's sound fix. S22 and S35 are restated before unit 38's pass, so its builder
adds no site. The census is read at every pass commit that changes `unattended.sh`, listed by `git log`,
and unit 41 AC2's plant is reworded. It repairs `TOOL-dIndexedDesign-41` and takes order 19, one above
unit 41's 18.

## 2. Scope (IN)

- **S1** — An act ahead of this unit's order, at unit 38's pass. Unit 38 S22's refusal of a
  `--design-exit` exit other than 0 or 1 sets `_dx_msg` naming the exit and returns 1 from
  `check_design_exit`. `--dispatch` then refuses through the composed THIN site and `--phase BUILDING`
  through its one site, both unit 41 S1's. S22 adds no `fail` site, and "through S5's site" is
  superseded. Unit 38's arm for AC16 asserts the clause naming the exit, never the composed THIN site's
  literal run, which stays the THIN arm's alone (`TOOL-dIndexedDesign-48` AC2). Unit 38's Edges block
  names this, and its builder reads it there. Observed by AC1 and AC2.
- **S2** — Unit 38 S35's "the variable S5's function names" reads "the variable `check_design_exit`
  holds", the function unit 16 S7 adds. Its call is unchanged. Unit 38's acceptance ledger carries the
  note `TOOL-dIndexedDesign-51 S2` under AC16's answer, naming S22's and S35's restatements. Observed by
  AC3.
- **S3** — The census at every pass. Unit 41 AC1's three named passes are superseded by the commit list
  `git log --format=%H <base>..HEAD -- tools/unattended/unattended.sh`, read at this unit's pass. Units 52
  and 53, ordered after it, write `unattended.sh` at no pass of their own: unit 53's `fail 55` item lands
  in unit 3's pass. Unit 41's acceptance ledger carries the note `TOOL-dIndexedDesign-51 S3` under AC1's
  answer. Observed by AC1 and AC3.
- **S4** — Unit 41 AC2's plant reads "one literal `fail 49 "` site inside `check_design_exit`", where it
  read "a second", since unit 41 S1 leaves that function none. Unit 41's acceptance ledger carries the
  note `TOOL-dIndexedDesign-51 S4` under AC2's answer. Observed by AC3.

## 3. Non-goals (OUT)

- Unit 38 AC5's third clause and S5's "exactly one" sentence, and unit 38's hands-off line on them:
  report id 2, MEDIUM, in `TOOL-dIndexedDesign-53`.
- `REFUSAL_CEILINGS`: unchanged at 323. A raise wants a DECISIONS.md id and is an owner turn.
- AC2's fixture, how `check-arms.py` finds the planted copy: report id 13, LOW, in
  `TOOL-dIndexedDesign-53`.
- The report's left-shift checklist entry. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-38` — S22 and S35, which S1 and S2 restate before that unit's pass, and AC16, whose ledger answer S2 annotates (id 20)
- **consumes-from** `TOOL-dIndexedDesign-41` — S1's composed sites, through which S1 refuses, and AC1 and AC2, which S3 and S4 supersede (id 20)
- **consumes-from** `TOOL-dIndexedDesign-48` — the composed THIN site's own literal run, which AC2 reads in the refusal (id 20)

## 4. Design

### Evidence

- `python tools/memory-tree/check-arms.py --emit-floors` printed `tools/unattended/unattended.sh:323:314`
  in the report's run of 2026-10-28; PINNED, and AC1 re-derives it at each commit.
  `.memory-tree.conf:653` sets `REFUSAL_CEILINGS` for `unattended.sh` at 323.
- Unit 38 S22 (`2026-10-28-spec-TOOL-dIndexedDesign-38.md:165-167`) refuses "through S5's site", and S35
  (`:204-206`) names "the variable S5's function names". Read 2026-10-28.
- The Files touched estimates of units 1, 2, 3, 6, 9, 10, 11, 16 and 38 name `tools/unattended/unattended.sh`,
  and units 39, 41 and 46 name sites in it, read 2026-10-28. The list AC1 reads is derived instead.

### Inventory

Minted: no identifier. Three ledger notes and one recorded census per commit.

### Migration

None.

### Rollout

S1 lands in unit 38's pass, order 17. Unit 38's Edges block names it. S2 to S4 and AC1 to AC3 are this
unit's own pass at order 19, after `TOOL-dIndexedDesign-48`, from which it consumes. This unit's own pass
writes only ledgers.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1, in unit 38's pass
- `memory/builds/dIndexedDesign/build/`: the ledger notes and the recorded censuses

### Alternatives rejected

- **Read the census only at the passes that add refusals.** Lost to the finding: which passes add a net
  site is what the census measures, and a list typed by hand misses unit 10's `fail 46` change.
- **Let S22 keep a site of its own.** Lost to the ceiling: the census reaches 324.

## 5. Production-readiness checklist

- security — no refusal is removed; S22's exit-2 refusal still refuses at both verbs.
- perf / scale — one worktree and one `check-arms.py --emit-floors` per listed commit, a dozen or so.
- error / empty / loading states — an empty commit list is red, never a pass.
- observability — the recorded censuses name each commit and its count.
- risks — unit 38's builder must read S1 from its Edges block. AC2 reads the function body at that
  unit's pass commit, so a missed restatement is visible.
- testing — AC1 by `git log` and `check-arms.py`, AC2 by `sed` and a fixture, AC3 by a ledger grep.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `git log --format=%H <base>..HEAD -- tools/unattended/unattended.sh` runs at this unit's
  pass and `python <repo>/tools/memory-tree/check-arms.py --emit-floors` runs in a worktree at each listed
  commit, every run prints `tools/unattended/unattended.sh` at or under 323, and the list holds the pass
  commits of units 16, 1, 3 and 38.
  Red when: a commit's census exceeds 323, or the list is empty or misses one of those four.
  figure: 323 is PINNED by `REFUSAL_CEILINGS` at `.memory-tree.conf:653`; the list is DERIVED.
- **AC2** — When `sed -n '/^check_design_exit()/,/^}/p' tools/unattended/unattended.sh | grep -c 'fail [0-9]* "'`
  runs at unit 38's pass commit, it prints 0. When `--dispatch` runs over unit 38 AC16's fixture, whose
  committed policy file is invalid, it refuses printing `--dispatch refuses a build pass for a unit not ready to build`.
  Red when: `check_design_exit` holds a site, or the refusal prints another site's text.
- **AC3** — When `grep -n "TOOL-dIndexedDesign-51 S"` runs over the acceptance ledgers of units 38 and 41,
  it prints S2's note under unit 38 AC16 and S3's and S4's under unit 41 AC1 and AC2.
  Red when: a note is missing or stands as its own `- AC` line.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `unattended kit gate` · `memory hygiene` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 39 to 46, id 20
  (HIGH, item H3), on its sound fix, repairing TOOL-dIndexedDesign-41 S4, AC1 and AC2.

## 10. Reuse audit

The seams are `check-arms.py --emit-floors` as the census and `git log` over the driver as the commit
list, the derivation `TOOL-dIndexedDesign-39` AC1 already uses for the harness. No new census is written.
The probe
`python tools/codebase-map/reuse_lookup.py "compose several refusal messages into one existing fail site"`
is `TOOL-dIndexedDesign-41`'s, re-run on 2026-10-28, and it ranked `fail`, `refusal`, `Refusal`,
`DesignRefusal` and `read_id_list_refusals` as before: none reads a census per commit. No existing seam fits beyond the two named.

Recall terms used: `python tools/memory-recall/query.py "how is a fail site census kept under REFUSAL_CEILINGS" --terms "REFUSAL_CEILINGS check-arms emit-floors census fail site unattended.sh composed message armed signature"`
