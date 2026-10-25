# TOOL-dPlacedRequest-62 — unit 61's criteria read a `###` section from its heading to the next heading

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 34 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-62-deviation-621.md](../build/2026-10-25-build-TOOL-dPlacedRequest-62-deviation-621.md) | deviation | — |
| [2026-10-25-review-TOOL-dPlacedRequest-62-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-62-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-63 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-7 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-60-spec-audit.md`)
confirmed **finding 13 at HIGH**, its item **H1**, which holds no other finding.
`TOOL-dPlacedRequest-61` §2 makes unit 60 S1's bullet reader the meaning of "extracted" for every
criterion. That reader closes at the next bullet, heading or blank line, and the line after a
heading is blank, so on a `###` section it prints the heading line alone. 61 AC13's
`grep -c 'git rev-list'` over 54's head section then prints 0 whatever the section holds, and its
pointer clause passes only on the heading line. 61 AC20 can never find `[ "$own" = 0 ]` in 44's
oracle section. The builder gets one vacuous clause and two impossible ones. This unit repairs
`TOOL-dPlacedRequest-61`, at order 33, so it sits at order 34: a criterion reads a `###` section
from the line after its heading to the next `##` or `###` heading.

## 2. Scope (IN)

Every edit is in place on what 61's pass left, one rev bump per spec with its §9 line naming this
unit and the criteria it restates.

- **S1** — Two readers, one per shape. 61 §2's "Extracted" is narrowed to S and AC bullets, which
  unit 60 S1's bullet form reads. A `###` section is read by §4's section form, from the line after
  its heading to the next `##` or `###` heading, so a `# comment` line inside a fenced block does
  not close it. A criterion names a heading prefix that exactly one heading of its file carries.
  Observed by AC1.
- **S2** — 61 AC13 is restated to the section form: 54's head section, read by it, holds no
  `git rev-list` and names `TOOL-dPlacedRequest-44`. Its `Red when:` names a scratch copy of 54 at
  rev-3, whose head section the form reads with a `git rev-list` count of 1. The clause 61 S13 adds
  to 59 AC13, over the same section, names the same form. Observed by AC2.
- **S3** — 61 AC20 is restated to the section form: 44's oracle section, read by it, holds
  `[ "$own" = 0 ]` on a line before `merge-base --is-ancestor`. Its `Red when:` names a scratch copy
  of 44 with those two lines swapped. Observed by AC3.
- **S4** — The record. 61 and 59 each take a rev bump with a §9 line naming this unit and AC13, and
  61's line also names AC20. Observed by AC4.

## 3. Non-goals (OUT)

- No change to unit 60's bullet form: finding 15's item of `TOOL-dPlacedRequest-63` joins its
  output.
- No edit to what the two sections hold: 61 S13 and S20 own that, and finding 21's item of
  `TOOL-dPlacedRequest-63` owns the base refusal in 44 §4.
- No reader under `tools/` and no lint over extraction forms: the form is a criterion's command, and
  the closing review's left-shift decides any lint (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-61` — §2's "Extracted", AC13 and AC20, and 54's head section and 44's oracle section as that unit's pass leaves them, which this unit reads by the section form
- **consumes-from** `TOOL-dPlacedRequest-59` — AC13 as unit 61 extends it with a clause over 54's head section, which this unit spells with the section form
- **hands-off** `TOOL-dPlacedRequest-63` — §2's narrowed "Extracted" and the restated AC13 and AC20, which that unit's items for findings 4, 15 and 21 extend
- **hands-off** `TOOL-dPlacedRequest-64` — S2, §4 Evidence, §6's preamble, §10, AC1, AC2 and AC4, which that unit's items for findings 4, 6, 10, 11, 15, 18 and 19 amend

## 4. Design

### The section form

```bash
sec() { awk -v h="$2" 'index($0, h) == 1 {f=1; next} /^##+ /{f=0} f' "$1"; }
d=memory/builds/dPlacedRequest/spec
sec "$d/2026-10-25-spec-TOOL-dPlacedRequest-54.md" "### The oracle's head"   # body, heading excluded
sec "$d/2026-10-25-spec-TOOL-dPlacedRequest-44.md" '### The oracle'
```

The heading is matched as a fixed prefix, so an apostrophe or a regex character in it needs no
escape. `/^##+ /` needs two or more `#`, so a bash comment inside a fenced block stays in the
section.

### Evidence

- Measured 2026-10-25 on node a: unit 60 S1's form, given the label `### The oracle's head`, printed
  `### The oracle's head, as this unit leaves it` alone over 54. The section form printed that
  section's body, and `grep -c 'git rev-list'` over it printed 1. PINNED at that date.
- `grep -c "^### The oracle's head"` over 54 and `grep -c '^### The oracle'` over 44 each printed 1,
  so each prefix names one heading today. 44's heading sits at line 71. Read 2026-10-25.
- 54's head sketch holds the line `# the rest of the oracle as units 52 and 55 leave it`, inside its
  fenced block. Read 2026-10-25.
- `git show 6df7a970:memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md`
  prints 54 at rev-3, with the head sketch holding `git rev-list`. Read 2026-10-25.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md`: §2's preamble, AC13,
  AC20 and its §9 line
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md`: AC13 and its §9 line

### Alternatives rejected

- **Close at the next heading of any level, `/^#/`.** 54's head sketch holds a `# ` comment line, so
  the read would stop inside the fenced block.
- **A `sed` range to the next `### ` heading.** The last `###` of a section runs on past the next
  `## ` heading into the following section.
- **The bullet form with its blank-line closer taken out.** It still closes on the `# ` comment line,
  and it changes the reader unit 60 owns.

## 5. Production-readiness checklist

- security — none: a read of spec files.
- perf / scale — one `awk` over one file per criterion.
- error / empty / loading states — a prefix that names no heading prints nothing, which fails AC13's
  pointer clause and AC20's order clause rather than passing them.
- observability — the form prints the section it graded.
- risks — a heading renamed by a later pass leaves a prefix naming nothing, which reads red; AC1
  counts each prefix's headings.
- testing — the probes of §6.
- migration — none: criterion text.
- user docs — none: criterion text.

## 6. Acceptance criteria

`sec <file> <prefix>` is §4's. `bullet <file> <label>` is unit 60 S1's form.

- **AC1** — When 61's §2 preamble is read, it names the `/^##+ /` closer and limits unit 60 S1's form
  to S and AC bullets. `grep -c "^### The oracle's head"` over 54 and `grep -c '^### The oracle'` over
  44 each print 1.
  Red when: one reader is applied to a record shape it cannot read.
- **AC2** — The prefix is `### The oracle's head`. When `sec` reads that section of 54,
  `grep -c 'git rev-list'` over it prints 0 and `grep -c TOOL-dPlacedRequest-44` prints at least 1.
  Over a scratch copy of 54 taken by `git show 6df7a970:<path>`, the same count prints 1 and the
  `bullet` form's count prints 0. 61's AC13 bullet and 59's AC13 bullet each name `/^##+ /`.
  Red when: a criterion over a section reads its heading line alone.
  fixture: the scratch copy is made under the run's scratch directory.
- **AC3** — The prefix is `### The oracle`. When `sec` reads that section of 44, the first line
  holding `[ "$own" = 0 ]` comes before the first line holding `merge-base --is-ancestor`. Over a
  scratch copy of 44 with those two lines swapped, the order inverts. 61's AC20 bullet names
  `/^##+ /`.
  Red when: the short-circuit cannot be found because the read stopped at the heading.
  fixture: the scratch copy is made under the run's scratch directory.
- **AC4** — When `awk '/^## 9\./{f=1;next} /^## /{f=0} f'` reads the §9 of 61 and of 59,
  `grep -cE 'TOOL-dPlacedRequest-62\b.*AC13'` over each prints at least 1. It prints 0 over both on
  this spec's tree.
  Red when: a criterion changes with no revision naming the unit that changed it.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

No new arm: the form is a criterion's command, observed by this unit's probes.

## 8. Open questions

- **F1 — Where does the read of a `###` section close (S1)?** (a) At the next `##` or `###` heading,
  the skeptic's corrected fix; (b) at the next heading of any level; (c) a `sed` range to the next
  `### ` heading. (b) stops on the `# ` comment line in 54's sketch, and (c) runs past a `## `
  heading. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-7 promotions,
  finding 13 (HIGH, item H1).
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is the heading-scoped read 57 AC2 already spells,
`sed -n '/^## 2\./,/^## 3\./p'`, narrowed to a `###` label and closed at either heading level.
`python tools/codebase-map/reuse_lookup.py "extract a markdown section from its heading to the next
heading"` ranked `extract`, `extract_row`, `extract_run_facts` and `extract_records`, name stems
only. None is a section reader a criterion can call, so no existing seam fits beyond that range.
`python tools/memory-recall/query.py "how does a criterion read a spec's subsection from its heading
to the next heading rather than one bullet"` returned TOOL-aDrainedSluice-4, a §9 range closed at the
next `## ` heading, unit 60's §10 and this audit's H1. None disagrees with source.

Recall terms used: extract section heading awk range criterion vacuous bullet reader label oracle head
