# TOOL-dPlacedRequest-60 — unit 57's read of 34 AC59 stops at the end of that bullet

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 30 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-60-deviation-601.md](../build/2026-10-25-build-TOOL-dPlacedRequest-60-deviation-601.md) | deviation | — |
| [2026-10-25-review-TOOL-dPlacedRequest-60-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-60-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-61 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-6 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-57-spec-audit.md`)
confirmed **finding 16 at HIGH**, its item **H1**. Finding 6, item **L3**, reports the same defect
at LOW, and `TOOL-dPlacedRequest-61` carries it. `TOOL-dPlacedRequest-57` AC2 extracts 34's AC59
bullet "the same way" as 44's AC1, a range that closes only at the next criterion bullet. AC59 is
34's last criterion, so the range runs to the end of the file and takes in §7 to §10. AC2's clause
that the bullet names `TOOL-dPlacedRequest-44` then passes on a §9 line, which this build's own
passes write into 34, while AC59 carries no pointer. This unit repairs `TOOL-dPlacedRequest-57`, at
order 29, so it sits at order 30: 57 AC2 reads the AC59 bullet and nothing after it.

## 2. Scope (IN)

- **S1** — The range closes. 57 AC2 spells its read of 34's AC59 bullet out, with no "the same
  way": `awk '/^- \*\*AC59\*\*/{f=1;print;next} f&&/^(- |#|$)/{exit} f'`. The range ends at the next
  bullet, the next heading or the next blank line, the three closers `TOOL-dPlacedRequest-59` §4's
  join uses. Both of AC2's clauses on AC59, the name and the no-sha test, read that output. Observed
  by AC1.
- **S2** — The red case is stated. 57 AC2 gains a `Red when:` clause naming a scratch copy of 34
  whose AC59 lacks `TOOL-dPlacedRequest-44` and whose §9 carries a line naming it. S1's read of that
  copy fails the name clause. Observed by AC2.
- **S3** — The record. 57 takes a rev bump with a §9 line naming this unit and AC2. Observed by AC3.

## 3. Non-goals (OUT)

- No change to 57 AC2's read of 44 AC1: 44 has an AC2, so that range closes.
- No edit to `TOOL-dPlacedRequest-34`: the red case is a scratch copy, and 34 sits 82 bytes under
  its 48128 ceiling.
- No lint over criterion extraction ranges: the closing review's left-shift decides one
  (BUILD-METHOD M8).
- No second direction of the defect: a §9 line quoting a sha is finding 6's item in unit 61.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-57` — AC2 as that unit's pass leaves it, whose read of 34 AC59 this unit bounds
- **hands-off** `TOOL-dPlacedRequest-61` — S1's bounded read, which that unit's item for finding 6 runs over a §9 line quoting a sha
- **hands-off** `TOOL-dPlacedRequest-63` — S1's bounded form and AC3, which that unit's items for findings 10 and 15 amend

## 4. Design

### The read

```bash
f=memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md
awk '/^- \*\*AC59\*\*/{f=1;print;next} f&&/^(- |#|$)/{exit} f' "$f"   # AC59 and its continuation lines
```

A continuation line of a bullet is indented, so it matches no closer. AC59 is followed by a blank
line and `## 7. Gates`, so the blank line closes the range.

### Evidence

- Measured 2026-10-25 on node a: `grep -n '^- \*\*AC' 2026-10-25-spec-TOOL-dPlacedRequest-34.md`
  ends at AC59. The unbounded range printed 60 lines and S1's read printed 3. A scratch copy of 34
  with a §9 line naming `TOOL-dPlacedRequest-44` appended gave 1 hit for the name through the
  unbounded range and 0 through S1's read. PINNED at that date.
- Unit 34 measured 48046 bytes on 2026-10-25, 82 under 48128. PINNED at that date.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md`: AC2 and its §9 line

### Alternatives rejected

- **Close at the next criterion or the next `## ` heading (the review's form).** It closes AC59
  correctly but keeps a trailing blank line, and it is a second closer set beside the one 59 §4
  already uses.
- **Add an AC60 to 34.** It moves a spec at its ceiling to suit a reader of it.

## 5. Production-readiness checklist

- security — none: a read of a spec file.
- perf / scale — one `awk` over one file.
- error / empty / loading states — a missing AC59 label prints nothing, which fails the name clause.
- observability — the read prints the bullet it graded.
- risks — an AC59 rewritten as two bullets would be read as its first only. 54 S3 cuts it to one
  line.
- testing — the probes of §6.
- migration — none: criterion text.
- user docs — none: criterion text.

## 6. Acceptance criteria

- **AC1** — When 57's AC2 bullet is read, it holds `f&&/^(- |#|$)/{exit}` and no `the same way`.
  When that read runs over unit 34's spec, its output ends before `## 7.` and holds the `AC59`
  label.
  Red when: the read of a section's last bullet runs on into the next section.
- **AC2** — When S1's read runs over a scratch copy of unit 34 whose AC59 lacks
  `TOOL-dPlacedRequest-44` and whose §9 names it, `grep -c TOOL-dPlacedRequest-44` over the output
  prints 0. The same copy read by `awk '/^- \*\*AC59\*\*/{f=1} f'` prints 1, and 57 AC2's `Red when:`
  names the copy.
  Red when: a §9 line satisfies a clause about a criterion.
  fixture: the scratch copy is made under the run's scratch directory, not held in the tree.
- **AC3** — When `grep -c 'TOOL-dPlacedRequest-60'` runs over 57's §9, it prints at least 1.
  Red when: a criterion changes with no revision naming the unit that changed it.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: the read is a criterion's command, observed by this unit's probes.

## 8. Open questions

- **F1 — Which closers end the read of 34 AC59 (S1)?** (a) The next bullet, heading or blank line;
  (b) the next criterion bullet or `## ` heading, the review's form; (c) an AC60 added to 34. (c)
  moves a spec at its ceiling, and (b) is a second closer set. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the closer set 59 §4 already uses, which also covers finding 6's form.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-6 promotions,
  finding 16 (HIGH, item H1, whose defect finding 6 of item L3 also reports).
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edge to `TOOL-dPlacedRequest-63`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is the bullet join of `TOOL-dPlacedRequest-59` §4, whose closers S1 copies. The
same three closers end a bullet span in `memory/builds/dPinnedHandoff/spec/2026-09-22-spec-TOOL-dPinnedHandoff-1.md`.
`python tools/codebase-map/reuse_lookup.py "extract one criterion bullet of a spec up to the next
bullet or heading"` ranked `extract`, `extract_row`, `read_spec_revisions` and `extract_run_facts`.
None of these is a bullet reader a criterion can call, so no existing seam fits beyond the join's
closers. `python tools/memory-recall/query.py "how is a criterion bullet extracted from a spec so the
range closes at the last bullet of a section"` returned TOOL-aDrainedSluice-4, a §9 range closed at
the next heading, this audit's H1 and the dPinnedHandoff span closers. None disagrees with source.

Recall terms used: awk extraction criterion bullet range terminator next heading last bullet spec section AC59
