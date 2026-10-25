# TOOL-dPlacedRequest-64 — the round-8 promotions' minors: criteria that read joined text and every carrier, a measured BINMODE, one lift seam that prints what it read, one bullet reader, and citations by anchor

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 36 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-64-deviation-641.md](../build/2026-10-25-build-TOOL-dPlacedRequest-64-deviation-641.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-64-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-64-promoted-fix-return.md) | research | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-64-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-64-promoted-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-8 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-62-spec-audit.md`)
exited CONVERGED with 19 confirmed findings, none at BLOCKER or HIGH. This unit is the batch
BUILD-METHOD M4 makes of them: 9 MEDIUM and 10 LOW findings by raw id, one scope item per id, each
naming its finding and, in brackets, the review item holding it. Three review items hold two ids
each (M3: 3 and 13; M5: 9 and 21; L3: 6 and 18). Findings 20 and 4 report one `bullet` signature
defect at two binding grades, items M7 and L1, and each keeps its own item.

The findings land on units 62 and 63 and on the specs and test arm their passes leave, so this unit
repairs none in particular and sits above every unit of the build, at order 36, after unit 63 at 35.
It is built after units 62 and 63, and every edit is made in place on what their passes left.
Criterion ACn observes item Sn.

| Item | Finding | Severity | Review item | Lands on |
|---|---|---|---|---|
| S1 | 1 | MEDIUM | M1 | 63 AC10, 61 §5 and §4 Alternatives |
| S2 | 2 | MEDIUM | M2 | 63 AC21, 59 §1 |
| S3 | 3 | MEDIUM | M3 | 63 S1 and AC1, 59 AC3, 61 §4 |
| S4 | 13 | MEDIUM | M3 | 63 AC1, 61 Files touched and Edges |
| S5 | 7 | MEDIUM | M4 | 63 §4 Evidence, S7 and AC7, 61 §4 Evidence |
| S6 | 9 | MEDIUM | M5 | `slice_fn`, 63 §4, §8 F2 and §10 |
| S7 | 21 | MEDIUM | M5 | the CRLF row, 63 AC8 |
| S8 | 19 | MEDIUM | M6 | 62 S2, AC1 and AC2, 59 AC13 |
| S9 | 20 | MEDIUM | M7 | 63 §4 `bullet`, AC1 and AC19 |
| S10 | 4 | LOW | L1 | 63 §6 preamble, 62 §6 preamble |
| S11 | 5 | LOW | L2 | 63 S11 |
| S12 | 6 | LOW | L3 | 62 §4 Evidence |
| S13 | 18 | LOW | L3 | 62 §4 Evidence |
| S14 | 10 | LOW | L4 | 62 §10 |
| S15 | 11 | LOW | L5 | 62 AC4, 63 AC18 |
| S16 | 12 | LOW | L6 | 63 S19, AC19 and Edges, 60 §4 |
| S17 | 14 | LOW | L7 | 63 S10, S15, §4, §10 and AC15, 61 §8 and S19, 57 §4 |
| S18 | 15 | LOW | L8 | 62 AC4, 63 AC18, 63 §4 |
| S19 | 23 | LOW | L9 | 63 AC11 and §5 |

## 2. Scope (IN)

Every edit to another unit's spec is in place, one rev bump per spec with its §9 line naming this
unit and the items it carries. Where a defect sits in a text that 62's or 63's pass wrote into a
sibling, the sibling is corrected too. `bullet`, `sec`, `flat` and `entries` are §4's readers.

- **S1** — finding 1 (M1). 63 AC10's absence grep runs over `flat` of 61, which squeezes the file to
  one line, so the Alternatives bullet that wraps `It is` / `a new leg` is seen. AC10 gains a clause
  over 61's §5 `risks` line, which names `--dispatch` or `fail 49`. At this pass both hold over 61,
  and a place 63's pass left stale is restated as 63 S10 states it. Observed by AC1.
- **S2** — finding 2 (M2). 63 AC21's clause on 59 reads 59's §1 joined by `sec` and
  `tr -s '[:space:]' ' '`. It requires `at order 32, after unit 58 at 31`, the restatement 61 S7
  prescribes, and the absence of `at order 31, after unit 58 at 30`. At this pass 59 §1 reads so.
  Observed by AC2.
- **S3** — finding 3 (M3). 63 S1 names the two texts that carry the reverse pattern
  `RUN\.md|fixture's( later)? base`: 59 AC3's reverse clause as 61 S4 leaves it, and 61 §4's reverse
  comment line. 63 AC1 gains a clause that `bullet 59 AC3` names `fixture's( later)? base`. At this
  pass both carriers hold the pattern. Observed by AC3.
- **S4** — finding 13 (M3). 63 AC1 gains two clauses. 61's `### Files touched (estimate)`, read by
  `sec`, names units 43 and 52. 61's `### Edges` holds a consumes-from edge to each of
  `TOOL-dPlacedRequest-43` and `TOOL-dPlacedRequest-52`. At this pass both hold. Observed by AC4.
- **S5** — finding 7 (M4). 63 §4 Evidence's GNU Awk bullet states the measured values per input
  path: through a pipe the default read prints 12, the environment prefix 12, `-v BINMODE=3` 13 and
  `BEGIN{BINMODE=3}` 12; from a file `-v BINMODE=3` and `BEGIN{BINMODE=3}` each print 13. 63 S7 and
  AC7 require 61 §4 Evidence to say that a `BEGIN` assignment comes too late for stdin, so
  `-v BINMODE=3` is the one form for the piped row. 61's Evidence bullet, as 63's pass leaves it, is
  restated so. Observed by AC5.
- **S6** — finding 9 (M5). `slice_fn` in `tools/unattended/unattended.test.sh` gains a variable
  mode. `slice_fn <name> var` opens at `^<name>='` and closes at the first later line ending in `'`,
  with the same two FAIL guards and `st=1`. A call with one argument reads exactly as today. The
  CRLF row lifts `CLAIM_KV_AWK` by `slice_fn CLAIM_KV_AWK var` and holds no `grep -n`, `sed -n` or
  `eval` of its own. 63 §4's CRLF sketch, its §8 F2 and its §10 name that call. Observed by AC6.
- **S7** — finding 21 (M5). The CRLF row prints the value it read,
  `printf "%s|%d", v["status"], length(v["status"])`, and asserts `live|4`. A mismatch prints a FAIL
  line holding the `od -c` of the output and sets `st=1`. This unit's pass stages two scratch driver
  copies: one without `sub(/\r$/, "", line)`, which reads `live`, a CR and `|5`, and one with
  `CLAIM_KV_AWK` renamed, which prints the lift's FAIL line. 63 AC8 is restated to those readings.
  Observed by AC7.
- **S8** — finding 19 (M6). 62 S2 restates both clauses of 59 AC13 to the section form: 52's
  `### The oracle (S11 to S13, S17)` is read by `sec` with the prefix `### The oracle`, as 54's head
  section is. 62 AC2 requires 59's AC13 bullet to name `/^##+ /` for the 52 clause too, and 62 AC1
  gains `grep -c '^### The oracle'` over 52, which prints 1. At this pass 59 AC13 reads so.
  Observed by AC8.
- **S9** — finding 20 (M7). 63 §4's `bullet` takes a file path as its first argument, in place of a
  unit number under a fixed `$d`. The reverse loop resolves each row's unit to
  `$d/2026-10-25-spec-TOOL-dPlacedRequest-<unit>.md` before the call. AC1's and AC19's red cases
  pass the scratch copy's path to the same function. Observed by AC9.
- **S10** — finding 4 (L1), the skeptic's corrected fix. 63 §4 is the build's one definition of
  `bullet`, joined. 63 §6's preamble states that `bullet <unit> <label>` abbreviates
  `bullet "$d/2026-10-25-spec-TOOL-dPlacedRequest-<unit>.md" <label>`, so its calls stand. 62 §6's
  preamble points at 63 §4 for `bullet` and says its form gained the join through 63 S19.
  Observed by AC10.
- **S11** — finding 5 (L2). 63 S11 cites its own §4 sketch `### The oracle's head, opening` for
  `base=$1` and the refusal, in place of "as 54 §4 has them", text 61 S13 removes. Observed by AC11.
- **S12** — finding 6 (L3). 62 §4 Evidence's second bullet drops "44's heading sits at line 71".
  Observed by AC12.
- **S13** — finding 18 (L3). The same bullet keeps its two heading counts, each printing 1, as the
  pin that stands in place of the line number. Observed by AC13.
- **S14** — finding 10 (L4). 62 §10 names `extract_run_facts` in
  `tools/unattended/lib-unattended.sh` as the seam: its fixed-prefix `index() == 1` open, closed at a
  heading, widened to take the heading as an argument and to close at `##` or `###`. 62 §10 makes no
  claim that 57 AC2's `sed` range is the seam extended. Observed by AC14.
- **S15** — finding 11 (L5). 62 AC4 and 63 AC18 read §9 by `sec <file> '## 9.'`, in place of the
  hand-spelled §9 range. Observed by AC15.
- **S16** — finding 12 (L6). 63 S19 names 60 §4's `### The read` beside 60 S1. 63 AC19 gains a
  clause that `sec` over that section holds `tr -s ' '`, and 63's consumes-from edge to 60 names 60
  §4. At this pass 60 §4's read carries the join. Observed by AC16.
- **S17** — finding 14 (L7). The citations 63 wrote by base-tree line number are restated by anchor:
  `fact()`, `slice_fn()`, `extract_run_facts()` and the fail-49 message text. That covers 63 S10,
  S15, §4 Evidence, §10 and AC15, and the texts 63's pass wrote into 61 §8, 61 S19 and 57's
  `### The read, at the close`. Observed by AC17.
- **S18** — finding 15 (L8), the skeptic's corrected fix. 63 §4 defines `entries`, which joins each
  §9 entry with its own continuation lines only. 62 AC4 and 63 AC18 grep each joined entry, never §9
  joined whole, and 63 AC18's red case still prints 0. Observed by AC18.
- **S19** — finding 23 (L9). 63 AC11 gains a second row on 54's no-merge fixture, with a well-formed
  40-hex sha the fixture does not hold as the base. The oracle prints
  `version oracle: base does not resolve` and exits 2, as for the empty base. 63 §5's error line
  names both input classes. This unit's pass runs both rows. Observed by AC19.

## 3. Non-goals (OUT)

- No change to the driver `tools/unattended/unattended.sh`: S6 and S7 change the test arm that
  lifts `CLAIM_KV_AWK`, never the function.
- No `slice_var` beside `slice_fn`: §8 F1.
- No change to what the oracle, the sweep or the claim reader does: every item corrects a criterion,
  a sketch, a citation or a record.
- No edit to `TOOL-dPlacedRequest-34`: no finding reaches it.
- No new gate leg, no lint over spec criteria and no new bug-class record: each review item's
  left-shift is the closing review's to decide (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-63` — S1, S7, S10, S11, S15, S19, §4's readers, sketches and Evidence, §5, §6's preamble, §8 F2, §10, Edges, AC1, AC7, AC8, AC10, AC11, AC15, AC18, AC19 and AC21 as that unit's pass leaves them, which S1 to S7, S9 to S11 and S15 to S19 amend
- **consumes-from** `TOOL-dPlacedRequest-62` — S2, §4 Evidence, §6's preamble, §10, AC1, AC2 and AC4, which S8, S10, S12 to S15 and S18 amend
- **consumes-from** `TOOL-dPlacedRequest-61` — §4's reverse comment and Evidence, §4 Alternatives, §5, §8 F1, S19, Files touched and Edges as unit 63's pass leaves them, which S1, S3, S4, S5 and S17 read and correct
- **consumes-from** `TOOL-dPlacedRequest-59` — §1, AC3 and AC13 as units 61 and 63 leave them, which S2, S3 and S8 correct
- **consumes-from** `TOOL-dPlacedRequest-60` — §4's `### The read`, which S16 gives the join
- **consumes-from** `TOOL-dPlacedRequest-57` — §4's `### The read, at the close` as unit 63 leaves it, which S17 cites by anchor
- **consumes-from** `TOOL-dPlacedRequest-52` — the `### The oracle (S11 to S13, S17)` heading, which S8's section read of 59 AC13 names by its prefix
- **consumes-from** `TOOL-dPlacedRequest-54` — the no-merge fixture, which S19's absent-sha row runs on
- **consumes-from** `TOOL-dPlacedRequest-44` — §4's oracle as units 61 and 63 leave it, whose base refusal S19 exercises with a second input class

## 4. Design

### The readers, as this unit leaves 63 §4 (S1, S2, S9, S10, S18)

`bullet` keeps its awk body and its join. Its file operand becomes `"$1"`, and its label stays `$2`.
`sec` is 62 §4's and `flat` is 52 §6's, both unchanged. `entries` is 61 §4's `join` idiom with a
`- rev-` opener, written into 63 §4 beside `bullet`:

```bash
entries() { sec "$1" '## 9.' | awk '/^- rev-/{if(b)print b; b=$0; next} /^(- |#|$)/{if(b)print b; b=""; next} b{b=b" "$0} END{if(b)print b}' | tr -s ' '; }
# the reverse loop: for each inventory row "<unit> <label>" of 54 §4; the 49 S3 row reads 44 AC1
bullet "$d/2026-10-25-spec-TOOL-dPlacedRequest-$u.md" "$l" | grep -qE "RUN\.md|fixture's( later)? base" || echo "red: $u $l"
```

A joined section read is `sec <file> <prefix> | tr -s '[:space:]' ' '`, which S2 uses for 59 §1.

### The lift, as this unit leaves `slice_fn` (S6)

```bash
slice_fn() { # <name> [var] -> eval that function, or that quoted variable, out of the SHIPPED driver bytes
  local s e o='()' c='^}' n='closing brace'
  [ "${2:-}" = var ] && { o="='"; c="'\$"; n='closing quote'; }   # ponytail: multi-line values only, as TASK_OPEN_AWK is
  s=$(grep -n "^$1$o" "$SCRIPT" | cut -d: -f1)
  [ -n "$s" ] || { echo "FAIL cannot find $1$o in the driver, so every arm that grades it would grade nothing"; st=1; return 1; }
  e=$(awk -v s="$s" -v c="$c" 'NR>s && $0 ~ c {print NR; exit}' "$SCRIPT")
  [ -n "$e" ] || { echo "FAIL cannot find the $n of $1$o in the driver, so the slice below would be a fragment"; st=1; return 1; }
  eval "$(sed -n "${s},${e}p" "$SCRIPT")"
}
```

With one argument, both messages and both searches are byte-identical to today's. A value opened and
closed on one line is not liftable: the end search starts below it. `CLAIM_KV_AWK` takes the
multi-line shape `TASK_OPEN_AWK` has at its definition.

### The CRLF row, as this unit leaves it (S6, S7)

```bash
slice_fn CLAIM_KV_AWK var &&
out=$(printf 'status: live\r\n' | awk -v BINMODE=3 "$CLAIM_KV_AWK"'
  BEGIN { K["status"] = 1 } { kv($0, K, v, 0) } END { printf "%s|%d", v["status"], length(v["status"]) }')
[ "$out" = "live|4" ] || { echo "FAIL the CRLF row read $(printf '%s' "$out" | od -c | head -1), not live|4"; st=1; }
```

The staged copy without the strip prints `live`, a CR and `|5`. A failed lift prints its FAIL line
and skips the row, so no failure reads as a pass.

### Evidence

- Measured 2026-10-25 on node a, GNU Awk 5.4.0, over `status: live` and a CR: through a pipe the
  default read printed length 12, `BINMODE=3 awk` 12, `awk -v BINMODE=3` 13 and `BEGIN{BINMODE=3}`
  12. From a file, the default printed 12, `-v BINMODE=3` 13 and `BEGIN{BINMODE=3}` 13. PINNED at
  that date.
- The §4 lift, run on HEAD with `SCRIPT` at the driver, set `TASK_OPEN_AWK` to its 252-byte text,
  defined `plan_state` with one argument, and printed `FAIL cannot find CLAIM_KV_AWK='` with
  `st=1`, since the variable is absent today. Measured 2026-10-25. PINNED at that date.
- Measured 2026-10-25 on HEAD, before 62's and 63's passes: `flat` of 61 piped to
  `grep -o 'It is a new leg\|That is harmless'` printed both phrases, where the line grep finds one.
  59 §1, joined, held `at order 31, after unit 58 at 30` once and `at order 32, after unit 58 at 31`
  not at all. 61's §5 risks clause named neither `--dispatch` nor `fail 49`. PINNED at that date.
- Measured 2026-10-25 on HEAD: `grep -c '^### The oracle'` over 52 printed 1, and over 44 printed 1
  at line 72. `sec` over 60's `### The read` held no `tr -s ' '`. `bullet` over 59 AC3 held no
  `fixture's( later)? base`. `entries` over 62 found no `TOOL-dPlacedRequest-62` entry naming AC13.
  PINNED at that date.
- `slice_fn` has 23 calls in `tools/unattended/unattended.test.sh`, each with one argument.
  The messages `slice_fn` prints are read by no other file: `marker-contract.test.sh` spells its own.
  Read 2026-10-25.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/`: the specs of units 57, 59, 60, 61, 62 and 63, each edit a
  rev bump with its §9 line
- `tools/unattended/unattended.test.sh`: `slice_fn`'s variable mode and the CRLF row of 59's S7 arm

### Alternatives rejected

- **Two batches.** S1 to S7, S9 to S11 and S15 to S19 write 63, and S8, S10, S15 and S18 write 62.
  S10, S15 and S18 each write both, so no split gives M6 two disjoint write sets.
- **A second paragraph joiner for S1 and S2 (finding 1's `awk 'BEGIN{RS=""}'` form).** 52 §6's
  `flat` and a joined `sec` already squeeze a wrap, so a third joiner would be a copy.
- **§9 joined whole with `tr '\n' ' '` (finding 15's first fix).** `.*` then matches across entries,
  and AC18's red case prints 1.
- **Changing 62's line number to 72 (finding 6's first form).** The next fold of 44 moves it again.

## 5. Production-readiness checklist

- security — none: a read of spec files and a test helper, with no driver change.
- perf / scale — one `awk` per criterion read, and one extra argument test in `slice_fn`.
- error / empty / loading states — a failed lift prints its FAIL line and sets `st=1`. S19 names the
  empty base and the absent sha as the two refusal inputs.
- observability — S7's row prints the value and its length, and a mismatch prints its `od -c`.
- risks — 62 and 63 are built before this pass, so their criteria were observed in their stale form.
  This unit's criteria re-observe each carrier, and a carrier found stale is corrected the same way.
- testing — the probes of §6, and the arm of §7.
- migration — none: the one-argument `slice_fn` reads as today.
- user docs — none beyond the specs: no user-facing behaviour changes.

## 6. Acceptance criteria

`bullet <unit> <label>` is 63 §4's reader as S9 and S10 leave it, with the abbreviation S10 states.
`sec <file> <prefix>` is 62 §4's, `flat <file>` is 52 §6's, and `entries <file>` is §4's. A
`<unit>` operand of `sec`, `flat` or `entries` names that unit's spec. The oracle fixtures are units
52's and 54's under `%TEMP%` with a short name.

- **AC1** — When `flat 61` is piped to `grep -c 'It is a new leg\|That is harmless'`, it prints 0.
  `sec 61 '## 5.' | tr -s '[:space:]' ' '` holds a `risks — ` clause naming `--dispatch` or
  `fail 49`, and `bullet 63 AC10` names `flat` and `risks`.
  Red when: an absence grep runs over text that wraps the phrase it looks for.
- **AC2** — When `sec 59 '## 1.' | tr -s '[:space:]' ' '` is read, it holds
  `at order 32, after unit 58 at 31` and no `at order 31, after unit 58 at 30`, and `bullet 63 AC21`
  names both phrases.
  Red when: a restatement is graded by a token the stale text already holds.
- **AC3** — When `bullet 59 AC3` is piped to `grep -cF "fixture's( later)? base"`, it prints 1, and
  the same count over `sec 61 '### The inventory sweep'` prints 1. `bullet 63 S1` names `59 AC3`.
  Red when: an amended rule's carrier keeps the narrow form.
- **AC4** — When `sec 61 '### Files touched'` is piped to `grep -cE '\b43\b'`, and again to
  `grep -cE '\b52\b'`, each prints at least 1. `sec 61 '### Edges'` holds a `consumes-from` line
  for each of `TOOL-dPlacedRequest-43` and `TOOL-dPlacedRequest-52`, and `bullet 63 AC1` names
  `### Files touched` and `### Edges`.
  Red when: a scope claim no criterion reads goes unbuilt.
- **AC5** — When `sec 63 '### Evidence' | tr -s '[:space:]' ' '` is read, it holds no
  `from a file and through a pipe` and names `too late for stdin`. `sec 61 '### Evidence'` names
  `too late for stdin`, and `bullet 63 AC7` names it. At this pass,
  `printf 'status: live\r\n' | awk 'BEGIN{BINMODE=3}{print length($0)}'` prints 12 and the same
  under `awk -v BINMODE=3` prints 13.
  Red when: a platform claim measured on one input path is recorded for another.
- **AC6** — When the test file's `slice_fn` definition is copied to a scratch file and sourced with
  `SCRIPT` at the driver, `slice_fn TASK_OPEN_AWK var` sets the variable and `slice_fn plan_state`
  defines the function. Against a scratch driver copy with `CLAIM_KV_AWK` renamed,
  `slice_fn CLAIM_KV_AWK var` prints `FAIL cannot find CLAIM_KV_AWK='` and leaves `st=1`. The CRLF
  row holds no `grep -n` of its own, and `bullet 63 AC8` names `slice_fn CLAIM_KV_AWK var`.
  Red when: a lift copied beside its seam drops the seam's guards.
  fixture: the scratch copies are made under the run's scratch directory.
- **AC7** — When the CRLF row's commands run with `SCRIPT` at the shipped driver, they print
  `live|4`. With `SCRIPT` at a scratch copy without `sub(/\r$/, "", line)`, the output piped to
  `od -c` shows `l i v e \r | 5`, and the row prints its FAIL line. `bullet 63 AC8` names `live|4`.
  Red when: a staged break prints a boolean that a failed lift also prints.
  fixture: the scratch copy is made under the run's scratch directory.
- **AC8** — When `bullet 59 AC13` is read, its 52 clause names `### The oracle` and `/^##+ /`, and
  `sec 52 '### The oracle'` piped to `grep -c 'git rev-list'` prints 0. `grep -c '^### The oracle'`
  over 52 prints 1, `bullet 62 S2` names `52's`, and `bullet 62 AC1` names
  `grep -c '^### The oracle'`.
  Red when: one bullet's two clauses are read by two readers.
- **AC9** — When `bullet` is given a scratch copy of 52 whose AC11 names no base, piped to
  `grep -cE "RUN\.md|fixture's( later)? base"`, it prints 0, and over the in-tree 52 it prints 1.
  `sec 63 '### The reverse direction'` holds `"$1"` and no `-$1.md`.
  Red when: a red case needs the in-tree spec edited to run.
  fixture: the scratch copy is made under the run's scratch directory.
- **AC10** — When `grep -rlE '^bullet\(\) ' memory/builds/dPlacedRequest/spec/` runs, it prints
  63's spec alone. `sec 63 '## 6.'` names `abbreviates`, and `sec 62 '## 6.'` names `63 §4`.
  Red when: one helper name carries two signatures.
- **AC11** — When `bullet 63 S11` is read, it names `The oracle's head, opening` and holds no
  `as 54 §4 has them`.
  Red when: a citation points at text an earlier unit removes.
- **AC12** — When `sec 62 '### Evidence'` is piped to `grep -c 'line 7[0-9]'`, it prints 0.
  Red when: a pin names a line a sibling's fold can move.
- **AC13** — When `sec 62 '### Evidence'` is read, it names `grep -c '^### The oracle'` and
  `grep -c "^### The oracle's head"`, and `grep -c '^### The oracle'` over 44 prints 1.
  Red when: the uniqueness pin is dropped with the stale number.
- **AC14** — When `sec 62 '## 10.'` is read, it names `extract_run_facts` and `index`, and
  `grep -c "sed -n '/^## 2"` over it prints 0.
  Red when: the reuse record names a seam its own design rejects.
- **AC15** — When `bullet 62 AC4` and `bullet 63 AC18` are read, each names `sec` and `'## 9.'`, and
  `grep -rlE "awk '/\^## 9[\]" memory/builds/dPlacedRequest/spec/` prints nothing.
  Red when: a criterion hand-spells a reader the build defines once.
- **AC16** — When `sec 60 '### The read'` is piped to `grep -c "tr -s ' '"`, it prints 1.
  `bullet 63 S19` and `bullet 63 AC19` name `### The read`, and `sec 63 '### Edges'` names `60 §4`.
  Red when: an amendment to a reader leaves another spelling of it standing.
- **AC17** — When each of `bullet 63 S10`, `bullet 63 S15`, `bullet 63 AC15`,
  `sec 63 '### Evidence'`, `sec 63 '## 10.'`, `sec 61 '## 8.'`, `bullet 61 S19` and
  `sec 57 '### The read, at the close'` is piped to `grep -cE '\.sh:[0-9]|[[:punct:]]:[0-9]'`, it
  prints 0, and `bullet 63 AC15` names `fact()`.
  Red when: a citation measured on the base tree is restated after units that move it.
- **AC18** — When `entries 57` is piped to `grep -cE 'TOOL-dPlacedRequest-60\b.*AC2'`, it prints at
  least 1, and over a scratch copy of 57 without unit 60's §9 entry it prints 0. Over a scratch copy
  of 59 whose 62 entry wraps between the id and `AC13`, `entries` finds it.
  `bullet 62 AC4` and `bullet 63 AC18` name `entries` and neither names `tr '\n' ' '`.
  Red when: a join crosses a record boundary, or a correct wrapped entry reads absent.
  fixture: the scratch copies are made under the run's scratch directory.
- **AC19** — When the oracle runs as 63 AC11 runs it, on 54's no-merge fixture with base
  `deadbeefdeadbeefdeadbeefdeadbeefdeadbeef`, it prints `version oracle: base does not resolve` and
  exits 2. `bullet 63 AC11` names that sha, and `sec 63 '## 5.'` names the empty base and the absent
  sha.
  Red when: a guard covering two input classes is tried with one.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC6 AC7 · the CRLF row staged against a scratch driver copy without its CR strip, which reads live, a CR and length 5, and one with CLAIM_KV_AWK renamed, which prints the lift's FAIL line · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Where does the lift of a quoted variable live (S6)?** (a) A `var` mode of `slice_fn`; (b) a
  `slice_var` beside it with the same guards, the review's other form. (b) copies one kind's guards
  at its second instance, which the charter's `[reuse]` rule refuses. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How are 63's base-tree line citations kept true (S17)?** (a) Cite by anchor; (b) re-measure
  each span at this pass and record the date. (b) goes stale again at the next edit of either file.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's first fix judged sound.
  widens: none · relaxes: none
- **F3 — How is a wrapped §9 entry read (S18)?** (a) `entries`, each entry joined with its own
  continuation lines; (b) a rule that the id and the AC label sit on one physical line. (b) leaves a
  correct wrapped entry red. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the skeptic's
  corrected fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-8 promotions' 9
  MEDIUM and 10 LOW findings.
- rev-2 · 2026-10-25 · S14 reworded with no retirement verb: it corrects 62 §10's reuse claim and
  retires no named thing, so it owes no **Readers:** clause (HYGIENE check 25).

## 10. Reuse audit

Each item extends the unit its finding names, and the new text reuses five seams: 63 §4's `bullet`,
62 §4's `sec`, 52 §6's `flat` for every joined read, 61 §4's `join` idiom for `entries`, and
`slice_fn` (`tools/unattended/unattended.test.sh`, by name) for the variable lift, which S6 extends
rather than copies. `python tools/codebase-map/reuse_lookup.py "lift a quoted shell variable's value
out of the shipped driver bytes into a test"` ranked `drive`, `parse_shell_defs` and
`read_conf_value`, name stems only, none a lift from shipped bytes: no existing seam fits beyond
`slice_fn`. `python tools/memory-recall/query.py "how does a minors batch repair the criteria of the
batch its previous round wrote"` returned TOOL-aEvidencedLens-20, `TOOL-dPlacedRequest-63`, `-59` and
`-61`, and PLAY-dOrderedCharter-55, batches of the same kind. None disagrees with source.

Recall terms used: minors batch promote criteria joined paragraph absence grep slice_fn BINMODE section reader bullet signature
