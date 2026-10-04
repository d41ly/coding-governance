# TOOL-aMendedFleet-23 — check 19 reports the gotcha anchors that select no tracked path

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · order 23

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A gotcha record's anchors are DERIVED from the backticked path tokens in its body, and an anchor that
selects no tracked path can never put its record on a checklist. Check 19 reds a record with NO anchor
and a record whose anchors reach only the append-only tree, but says nothing about an anchor that
reaches nothing at all, so a record can carry dead anchors beside one live one and nobody hears of it.
The report counted 39 of 314 such anchors at `ac65de998`; the same count reproduces at base. This unit
makes check 19 REPORT them, non-gating, through a channel the hygiene leg actually prints.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/gotchas.py` gains `scan_dead_anchors`, which returns every anchor of a
  non-universal `kind: class` record that `selectable` maps to no tracked path. It calls `selectable`,
  the module's one copy of the selection predicate, and never a second matcher. Observed by AC1, AC2.
- **S2** — `cmd_check` prints ONE advisory line when that scan is non-empty, opening
  `HYGIENE advisory check 19:` and naming the dead-anchor count, the anchor population it was drawn
  from, and the record count, all derived. The line never changes the exit status. Observed by AC1.
- **S3** — `cmd_report` lists every dead anchor under its record path, after its existing rows.
  Observed by AC2.
- **S4** — `--selftest` gains one arm: a fixture class record carrying one anchor that selects a
  fixture file and one that selects nothing, asserting `--check` exits 0, prints the advisory line with
  the count 1 of 2, and `--report` lists the dead anchor. Observed by AC3.
- **S5** — `tools/memory-tree/check-memory-hygiene.sh` prints what `gotchas.py --check` said at every
  exit status, in the form the corpus_ids block beside it already uses, instead of only when red; and
  `add_offender_keys` skips any line opening `HYGIENE advisory `, so an advisory never becomes an
  `--offenders` key. The header sentence claiming that any output is a regression is corrected to
  name the non-gating lines. Observed by AC4, AC5.
- **S6** — check 19's catalogue entry in `tools/memory-tree/HYGIENE.template.md` gains one sentence
  naming the advisory, and `memory/HYGIENE.md` is re-rendered from it. Observed by AC6.

## 3. Non-goals (OUT)

- Gating the count. A shrink-only pin would need a new conf key, which is new kit surface, and the
  standing population holds illustrative tokens an author meant as examples; see §4 Alternatives.
- Editing the twenty records that carry a dead anchor today. The advisory names them; rewriting a
  record's prose is that record's own fold.
- Teaching `selectable` glob semantics. Eleven of the dead anchors are glob tokens such as `*.sh`,
  which the substring predicate cannot match; changing the predicate changes every checklist and is
  a separate mechanism. The advisory makes that population visible.
- The ranking and tiered cut of `--for-diff`, which is unit 16's.
- Moving the memory-tree kit version: the build moves each kit version it owes once, after the last
  pass that touches the kit, and the `kit epoch` leg grades that move at the close.

### Edges

- **hands-off** `TOOL-aMendedFleet-24` — the check 15 advisory rides the `add_offender_keys` skip
  this unit adds, so its line opens with the same `HYGIENE advisory ` prefix.

## 4. Design

### Evidence

Read at base `7af5f564`, whose bytes for every file below equal HEAD's at `6a88fbf7`.

- A scratch probe importing `gotchas.py` and calling `records` and `selectable` over `git ls-files`
  counted 94 records, all `kind: class`, 314 anchors, 39 selecting nothing, in 21 records, and no
  record whose every anchor is dead, so neither existing check 19 arm fires on any of them. Over the
  non-universal records, which is the population S1 grades, it counted 38 of 291 in 20 records: 11
  glob tokens, 2 home-directory tokens, 2 citations of a sibling record under `memory/gotchas/`, which
  the catalogue's self-exclusion never selects, and 23 others.
- `check-memory-hygiene.sh` line 2461 runs `gotchas.py --check` inside `if ! got=$(...)` and prints
  `$got` only on that branch, so any line printed at exit 0 is discarded. The corpus_ids block ten
  lines above prints first and decides status from the exit code, and its comment records why.
- `add_offender_keys` keys every non-empty line of the body it is handed, so a non-gating line in a red
  run would enter the offender set the bar compares between two trees.

### Mechanism

S1 loops the class records, skips universal ones because selection never reads their anchors, and
collects `(record path, anchor)` for each anchor with an empty `selectable` result over the tracked
paths `cmd_check` already lists. S2 reuses that `paths` list, so the scan adds no `git` call. The line:

```
HYGIENE advisory check 19: <n> of <m> anchor(s) in <k> class record(s) select no tracked path — gotchas.py --report lists them
```

S5 copies the corpus_ids block's four-line shape: capture with the exit code, print when non-empty,
set `status` from the code, key offenders only when red. The skip in `add_offender_keys` is one more
negated pattern in its existing `awk` filter, so every caller gets it.

### Inventory

- `scan_dead_anchors` — cell `py.function`; `python tools/lexicon/lexicon.py --suggest` answered OK.

### Rollout

Unit 16 also writes `tools/memory-tree/gotchas.py` and unit 24 writes both HYGIENE documents, so this
unit sequences after 16 and before 24. The re-render in S6 is the parity script's `--render` mode.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`

### Alternatives rejected

- **A shrink-only pin on the count.** It is the more feature-rich option, and M3's veto 2 removes it:
  the pin is a new `.memory-tree.conf` key every adopter inherits. The report asked for a report.
- **Print one advisory line per dead anchor in `--check`.** Thirty-eight lines on every hygiene run is
  the noise the catalogue's own docstring says teaches reviewers to skip; one line plus `--report`
  carries the same facts.
- **Report through `--report` alone.** No leg runs `--report`, so the finding would be invisible on
  the bar, which is a skip that looks like a pass.

## 5. Production-readiness checklist

- security — N/A: reads tracked paths and records already read; no new input or write path.
- perf / scale — one extra pass over anchors against the path list `cmd_check` already holds.
- error / empty / loading states — an empty scan prints nothing; a tree with no records never reaches
  the scan, as today.
- observability — the advisory line and the `--report` listing are the observability.
- risks — the hygiene leg prints one more line at exit 0; S5's skip keeps it out of the offender set
  the bar compares, so a red run's attribution does not move.
- testing — S4's selftest arm, plus AC1, AC2 and AC4 run directly.
- migration — N/A: no conf key, no record format change.
- user docs — S6's sentence in the hygiene catalogue.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --check` runs on the tree, it exits 0 and prints
  exactly one line opening `HYGIENE advisory check 19:`, whose three counts equal those
  `python tools/memory-tree/gotchas.py --report` lists.
  Red when: S2 is absent, which at base printed nothing at exit 0, or the line moves the exit status.
  figure: DERIVED at observation time; at base the probe measured 38 of 291 in 20 records.
- **AC2** — When `python tools/memory-tree/gotchas.py --report` runs, its listing names
  `memory/gotchas/concurrency-is-not-a-budget.md` with its glob anchor beneath it.
  Red when: S3 lists nothing, or lists a record whose anchors all select a tracked path.
  fixture: the tree holds that record and its dead glob anchor at base.
- **AC3** — When `python tools/memory-tree/gotchas.py --selftest` runs, S4's arm passes; with S2's
  print line removed as a staged break, that arm reds naming the missing advisory.
  Red when: the arm asserts on a fixture whose anchors all resolve, so it cannot fail.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs on the tree, its output carries
  the `HYGIENE advisory check 19:` line and its exit status equals what it was at base.
  Red when: the shell still prints the gotchas output only on a red run.
  cost: about three minutes, the `memory hygiene` leg's own command.
- **AC5** — With an anchorless class record placed in `memory/gotchas/` as a staged break,
  `bash tools/memory-tree/check-memory-hygiene.sh --offenders` exits 1 and its keys name that record
  under check 17-19 while no key carries `advisory`.
  Red when: `add_offender_keys` keys the advisory line.
  cost: about three minutes; remove the staged record afterwards.
- **AC6** — When `grep -n 'advisory' memory/HYGIENE.md` runs, it prints a line inside check 19's
  entry, and the same sentence is in `tools/memory-tree/HYGIENE.template.md`.
  Red when: the rendered copy and the template disagree, which the parity leg reds at the close.

## 7. Gates

`memory hygiene` · `gotchas selftest` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py --selftest · S4's dead-anchor arm, staged red by removing S2's print line · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#25] and a probe of the catalogue at
  base reproducing its count.

## 10. Reuse audit

The seam is `selectable` in `tools/memory-tree/gotchas.py`, the module's declared one copy of the
selection predicate, which S1 calls unchanged; `inert_only` beside it is the existing check 19 arm
built the same way, resolving first and classifying second. The shell half reuses the corpus_ids
block's print-then-decide form in `tools/memory-tree/check-memory-hygiene.sh`. The map probe
`python tools/codebase-map/reuse_lookup.py "report gotcha anchors that select no tracked path"`
ranked `selectable` and `cmd_report` of `tools/memory-tree/gotchas.py` among its candidates, at
fan-in 0, below name-token seams in unrelated kits; it prints `unscanned layers: .sh`, so it could
not see the shell half, which was read in source instead. Recall returned `TOOL-aScouredKit-2`'s wave-3 lens record naming exactly this
gap in `cmd_check` beside its two existing arms, and `TOOL-aProbedToolkit-1`'s measurement of the
substring-plus-basename predicate.

Where the report and the tree disagree: none on the count, which reproduces at 39 of 314. The report
does not separate universal records, whose anchors selection never reads; S1 grades the 291 that
selection does read.

Recall terms used: `python tools/memory-recall/query.py "should a gotcha record's anchor that selects no tracked path be reported by check 19" --terms "gotchas anchors derived selectable inert check 19 unanchored universal catalogue harvest basename zero-select"`
