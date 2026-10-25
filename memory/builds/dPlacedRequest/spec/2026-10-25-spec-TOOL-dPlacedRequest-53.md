# TOOL-dPlacedRequest-53 — unit 52's "named twice" criteria count occurrences, never lines of squeezed text

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 28 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-53-deviation-531.md](../build/2026-10-25-build-TOOL-dPlacedRequest-53-deviation-531.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-53-promoted-fix-return.md) | research | TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-53-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 |
| [2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-4 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md`)
confirmed **finding 1 at HIGH**, its item **H1**. The same defect is reported by findings 7 and 18,
item **M1**, which `TOOL-dPlacedRequest-56` carries at MEDIUM. `TOOL-dPlacedRequest-52` §6 defines
`flat <file>` as `sed '/^## 9\./,$d' <file> | tr -s '[:space:]' ' '`, whose output is one line. Its
AC1, AC6 and AC9 each require `flat … | grep -c <pat>` to print "at least 2", but `grep -c` counts
matching lines, so over one line it prints 0 or 1. The three criteria stay red however correctly S1,
S6 and S9 are built, and the "named in two places" property each exists to check is never decided.
This unit repairs `TOOL-dPlacedRequest-52`, at order 27, so it sits at order 28: the three criteria
count occurrences, and the build's spec set holds no other criterion of the same shape.

## 2. Scope (IN)

- **S1** — Occurrences, not lines. `TOOL-dPlacedRequest-52` AC1, AC6 and AC9 are rewritten in place,
  one rev bump of 52 with its §9 line naming this unit, so each "at least 2" count reads
  `flat <file> | grep -o '<pat>' | wc -l`. The patterns stay as 52 writes them: `S25` over 48,
  `43 S30` over 48, and `48128` over 43. Observed by AC1 and AC2.
- **S2** — No sibling of the shape stands. Across `memory/builds/dPlacedRequest/spec/`, no criterion
  pairs `flat` (or any `tr -s '[:space:]'` squeeze) with `grep -c` and a count above 1. A hit found at
  this unit's pass is rewritten the same way, in place, with its §9 line. Observed by AC3.

## 3. Non-goals (OUT)

- No change to what `flat` is or to the criteria that expect 0: a `grep -c` over one line answers
  present or absent correctly, which is all AC8, AC10, AC18, AC23 and AC28 ask. The note saying so
  under the `flat` definition is finding 18's item of `TOOL-dPlacedRequest-56`.
- No change to what S1, S6 and S9 of unit 52 build: only how their criteria count.
- No new bug-class record: the closing review's left-shift decides one (BUILD-METHOD M8), and S2
  sweeps the one population the class has today.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-52` — §6's `flat` definition and AC1, AC6 and AC9, which this unit rewrites in place to count occurrences; without them there is no criterion to correct
- **hands-off** `TOOL-dPlacedRequest-56` — the rewritten AC1, AC6 and AC9, beside which that unit's items for findings 7 and 18 observe each named place and state under `flat` what `grep -c` answers
- **hands-off** `TOOL-dPlacedRequest-59` — S1, AC1, AC3 and §4 Evidence, which that unit's items for findings 3, 4, 7, 11, 12 and 19 amend

## 4. Design

### The rewritten counts

```
AC1   flat 2026-10-25-spec-TOOL-dPlacedRequest-48.md | grep -o 'S25' | wc -l       -> at least 2
AC6   flat 2026-10-25-spec-TOOL-dPlacedRequest-48.md | grep -o '43 S30' | wc -l    -> at least 2
AC9   flat 2026-10-25-spec-TOOL-dPlacedRequest-43.md | grep -o '48128' | wc -l     -> at least 2
```

`grep -o` prints each match on its own line, so `wc -l` counts matches whatever the input's line
structure. The rest of each criterion, its `Red when:` included, is unchanged.

### Evidence

- Measured 2026-10-25 on node a over a hand-written sample whose two `S25` sit in two paragraphs
  before a `## 9.` heading: `flat | grep -c 'S25'` printed 1, and `flat | grep -o 'S25' | wc -l`
  printed 2. PINNED at that date.
- On the same date, before unit 52's pass, `flat` of 43 held `48128` once and `flat` of 48 held
  `43 S30` zero times: the counts the rewritten criteria start from.
- `grep -n "grep -c" memory/builds/dPlacedRequest/spec/*.md` filtered to "at least" found 52:287 and
  52:309 on the criterion's line, and 49:328, which counts lines of `tools/hooks/scratch-guard.js`
  unsqueezed and is correct; 52:300 carries its "at least 2" on the next line, which that filter
  misses and AC3's `-A1` reads.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md`: AC1, AC6, AC9 and
  its §9 line. `TOOL-dPlacedRequest-54` and `TOOL-dPlacedRequest-55` write this file at the same
  order, so the three passes run in sequence.

### Alternatives rejected

- **`grep -c` over the unsqueezed file.** It counts lines, so two mentions on one wrapped line read
  as 1, and a phrase the house wrap splits is not matched: the case `flat` exists for.
- **Grep the two named paragraphs separately.** It needs one extraction per paragraph per criterion,
  where one occurrence count answers the same question.

## 5. Production-readiness checklist

- security — none: criterion text.
- perf / scale — none.
- error / empty / loading states — N/A — no runtime path changes.
- observability — each count prints the number it compares.
- risks — none beyond unit 52's own.
- testing — the probes of §6.
- migration — none.
- user docs — none: criteria.

## 6. Acceptance criteria

- **AC1** — When `flat` is applied to a scratch file holding `S25` in two paragraphs before its
  `## 9.` heading, `grep -o 'S25' | wc -l` over it prints 2 and `grep -c 'S25'` prints 1.
  Red when: the rewritten form still counts lines and prints 1.
  fixture: built by the probe, not held in the tree.
- **AC2** — When `grep -n "grep -o" 2026-10-25-spec-TOOL-dPlacedRequest-52.md` runs, it names AC1,
  AC6 and AC9, and the same three bullets carry no `grep -c`.
  Red when: any of the three still asks `grep -c` for at least 2.
- **AC3** — When `grep -n -A1 "grep -c" memory/builds/dPlacedRequest/spec/*.md` is read for "at least"
  with a count above 1, no hit pairs it with `flat` or a `tr -s` squeeze.
  Red when: a criterion of the build still asks a line count of one line for 2 or more.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: the three counts are criteria commands, observed by unit 52's pass and at the close.

## 8. Open questions

- **F1 — How do the criteria count the second mention?** (a) `grep -o | wc -l` over `flat`; (b)
  `grep -c` over the unsqueezed file before §9; (c) one paragraph extraction per mention. (b) misses
  a wrapped phrase and counts two mentions on one line as one; (c) costs an extraction per mention.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's fix judged sound, measured on a
  two-mention sample. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  1 (HIGH, item H1, whose defect findings 7 and 18 of item M1 also report).
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edge to `TOOL-dPlacedRequest-59`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-52` §6's `flat` definition, kept as written; only the
counting stage changes. `python tools/codebase-map/reuse_lookup.py "count how many times a phrase
occurs in a squeezed spec"` ranked `counts` (`tools/unattended/check-playbook.test.sh`),
`read_spec_revisions` and `parse_spec_h1`, name stems only, none a criterion's counting stage: no
existing seam fits, since the unit edits criterion text. `memory/gotchas/` holds
`line-count-reads-empty-capture-as-one` and `msys-grep-counts-cr-on-every-line`, two line-count
classes that are not this one. `python tools/memory-recall/query.py "which criterion counts a phrase
twice over a whitespace-squeezed spec"` returned this spec, this audit's H1, TOOL-aBoundedVerdict-32
and TOOL-aHonedRuleset-12, asks on other counts; none disagrees with source.

Recall terms used: flat squeezed grep count occurrences lines criterion at least two spec phrase wrap
