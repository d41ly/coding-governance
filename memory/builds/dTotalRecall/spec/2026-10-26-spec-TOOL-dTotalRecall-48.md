# TOOL-dTotalRecall-48 — the run record's fixed head admits a cause line, and runlog grades its shape while the causes leg grades its absence

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 18 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 30 at HIGH**, its item **H4**, alone in that item. `TOOL-dTotalRecall-36` S4
writes `**Caused-by:**` on the run record's line after its Serves line and adds `check_cause_line`,
which reds a head with none. `check_record_lines` in `tools/runlog/record.py:1564-1574` grades the
fixed head `(TITLE, "", None, "", INTRO, "")`, so line 4 must be blank, and `render_markdown`
(`:1137`) writes exactly that head. The leg `runlog record schema` (`tools/gate-legs.json:1006`, no
guard) grades all 21 tracked run records, none with a cause line. Built as written, either every new
run record fails the fixed head, or a widened head leaves `check_cause_line` red on all 21. This unit
gives the head one optional cause line and leaves absence to the legacy-aware causes check. It repairs
`TOOL-dTotalRecall-36`.

## 2. Scope (IN)

- **S1** — The head admits the cause line. `check_record_lines` reads line 4: a line matching
  `**Caused-by:** <target>` is the cause line and the fixed tail `("", INTRO, "")` follows it; a blank
  line 4 is the head without one, its tail as today. Any other line 4 is the existing finding, `the
  record's head is fixed text`. Observed by AC1 and AC2.
- **S2** — Shape, not absence. `check_cause_line` reds a cause line whose target is not one of the
  served ids, or a second cause line, and never reds a head that has none. Whether a record needs a
  cause is `check_causes`' question, which reads the legacy population; runlog does not require
  memory-tree (`TOOL-dTotalRecall-5` §4 "The readers"), so it cannot read that population. Observed by
  AC2 and AC3.
- **S3** — `render_markdown` writes the cause line `TOOL-dTotalRecall-36` S4 gives it, under the head
  S1 admits. Observed by AC1.

## 3. Non-goals (OUT)

- The causes check and the legacy population: `TOOL-dTotalRecall-19`'s.
- The cause line's text and target: `TOOL-dTotalRecall-36` S4's.
- Rewriting the 21 tracked run records. They are in the legacy population and keep their bytes.

### Edges

- **consumes-from** `TOOL-dTotalRecall-36` — `render_markdown`'s cause line and `check_cause_line` in
  `tools/runlog/record.py`, which this unit admits into the fixed head and narrows to shape
- **hands-off** `TOOL-dTotalRecall-53` — the run record's head with its cause line, which that unit re-observes for unit 36's AC4 (id 16)
- **hands-off** `TOOL-dTotalRecall-60` — `check_cause_line` and the run record's head, whose range expansion, schema key, kit README and unit 36's arm that unit settles (the round-1 audit of units 44 to 53, ids 22, 30, 36 and 40)

## 4. Design

### The head

```text
1 TITLE
2 (blank)
3 **Serves:** journal <ids>      check_serves_line
4 **Caused-by:** <id>  | (blank)  check_cause_line on the first; nothing on the second
5 (blank)              | INTRO
6 INTRO                | (blank)
7 (blank)
```

The INTRO shifts one line when the cause line is present. Every later line number the checker reports
is counted from the head's real length, so a finding below the head names its real line.

### Inventory

Minted: none; `check_cause_line` is `TOOL-dTotalRecall-36`'s, narrowed here.

### Files touched (estimate)

- `tools/runlog/record.py`
- `tools/runlog/selftest.py`

### Alternatives rejected

- **Red an absent cause only for records dated after the seed.** It types the seed's date into the
  runlog kit beside the ledger that owns it, two homes for one fact.
- **Keep the six-line head and put the cause after the INTRO.** It falls outside the first
  `BIND_HEAD_LINES` lines only when the INTRO wraps, which is a cause line the reader finds by luck.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one extra line compare per record.
- error / empty / loading states — a head with a malformed line 4 reports the existing fixed-text
  finding at line 4.
- observability — `check_cause_line` names the line and the id it does not serve.
- risks — a run record with no cause passes runlog's leg; the causes leg reds it unless it is legacy.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none: every tracked record keeps its six-line head.
- user docs — none under `help/`: no page covers the run record's head.

## 6. Acceptance criteria

- **AC1** — When `render_markdown` from `record.py` renders a fixture record serving `TOOL-x-1` and
  `check_record_lines` grades the result, it returns no finding, and line 4 is `**Caused-by:** TOOL-x-1`.
  Red when: the fixed-text finding fires on line 4 of a record the renderer wrote.
- **AC2** — When `python runlog.py check-records` runs at the pass tip, it exits 0 over the 21 tracked
  run records, which carry no cause line.
  Red when: a head without a cause line is red.
  figure: 21 PINNED at base `462d20f3` by `git ls-files 'memory/builds/*/build/*-runlog-*.md'`.
- **AC3** — When `check_cause_line` grades a fixture head whose cause names `TOOL-x-9`, an id it does
  not serve, it returns one finding naming `TOOL-x-9`.
  Red when: a cause outside the served ids passes.

## 7. Gates

`runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `memory hygiene`

New arm: tools/runlog/selftest.py · covers AC1 AC3 · a rendered head with a cause line and one whose cause serves nothing, staged by restoring the six-line head tuple · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 30
  (HIGH, item H4).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `check_record_lines` in `tools/runlog/record.py:1564`, the run record's one head
grader, and its sibling `check_serves_line` (`:1461`), whose pattern the cause check follows; no
second head reader is written. `python tools/codebase-map/reuse_lookup.py "insert a cause line into a
record head after its binding line"` ranked `check_line` and `render_record` in the runlog kit, both
readers of other lines, and no head grader beside this one.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
