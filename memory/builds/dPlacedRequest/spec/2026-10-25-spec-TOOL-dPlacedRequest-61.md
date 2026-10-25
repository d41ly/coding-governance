# TOOL-dPlacedRequest-61 — the round-6 promotions' minors: a two-way oracle inventory, one run-fact reader, a claim reader that keeps its normalisation, honest orders, and criteria that can fail

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 33 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-61-deviation-611.md](../build/2026-10-25-build-TOOL-dPlacedRequest-61-deviation-611.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-61-deviation-612.md](../build/2026-10-25-build-TOOL-dPlacedRequest-61-deviation-612.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-review-TOOL-dPlacedRequest-60-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-60-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-60 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-6 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-57-spec-audit.md`)
exited CONVERGED with 21 confirmed findings. Its one high, finding 16, is unit 60. This unit is the
batch BUILD-METHOD M4 makes of the rest: 11 MEDIUM and 9 LOW findings by raw id, one scope item per
id, each naming its finding and, in brackets, the review item holding it (M1 to M7, L1 to L9). Two
review items hold more than one id (M1: 1, 9, 17 and 18; M2: 2 and 15). L3, finding 6, restates
H1's defect, which unit 60 closes at HIGH. Each id still gets its own item and its own observation.

The minors land on units 57 and 59 and on the specs and code those units' passes leave, so this unit
repairs none in particular and sits above every unit of the build. S7 moves unit 59 to order 32, so
this unit takes order 33 and never shares a step with the unit whose output it amends. It is built
after units 57, 59 and 60, and every edit is made in place on what their passes left. Criterion ACn
observes item Sn.

| Item | Finding | Severity | Lands on |
|---|---|---|---|
| S1 to S4 | 1, 9, 17, 18 (M1) | MEDIUM | units 54, 59 |
| S5, S6 | 2, 15 (M2) | MEDIUM | unit 59 |
| S7 | 3 (M3) | MEDIUM | units 56, 57, 58, 59 |
| S8 | 7 (M4) | MEDIUM | unit 57 |
| S9 | 10 (M5) | MEDIUM | units 48, 50, 56, 59 |
| S10 | 14 (M6) | MEDIUM | units 44, 57 |
| S11 | 20 (M7) | MEDIUM | unit 59 |
| S12 | 4 (L1) | LOW | unit 59 |
| S13 | 5 (L2) | LOW | units 44, 54, 59 |
| S14 | 6 (L3) | LOW | unit 57 |
| S15 | 8 (L4) | LOW | units 54, 59 |
| S16 | 11 (L5) | LOW | unit 59 |
| S17 | 12 (L6) | LOW | unit 59 |
| S18 | 13 (L7) | LOW | unit 57 |
| S19 | 21 (L8) | LOW | unit 57 |
| S20 | 22 (L9) | LOW | units 44, 59 |

## 2. Scope (IN)

Every edit to another unit's spec is in place, one rev bump per spec with its §9 line naming this
unit and the items it carries. "The run's base" is S10's read of the observing run's `base:` fact.
"The fixture's base" is the base commit of the fixture a criterion builds. "Extracted" means read
by unit 60 S1's form, from the label to the next bullet, heading or blank line.

- **S1** — finding 1 (M1). 54 §4's oracle inventory, as 59's pass leaves it, gains rows for 59 AC2,
  AC4, AC5 and AC21, each naming the fixture's base. Under an `Excluded, text only` sub-table it
  names every sweep hit that runs no oracle, 56 AC19 and 59 AC13 among them, each with the phrase
  that matched. 59 S3 is restated to the same list. Observed by AC1.
- **S2** — finding 9 (M1). Every inventory row is one label, `<unit> AC<n>` or `49 S3`, and no row
  holds a range. 59 AC3 matches each label anchored as `AC<n>\b`. Observed by AC2.
- **S3** — finding 17 (M1). 59 AC3 compares the sweep's hits with an explicit expected list, the
  inventory rows and the excluded rows together, and is red on a hit in neither. This unit's pass
  runs the sweep over the real spec tree and records its hit set in 54 §4 Evidence. Observed by AC3.
- **S4** — finding 18 (M1). The sweep matches `oracle[^.]*(runs|run |prints|exits)`, so a criterion
  worded "the oracle prints" is a hit. 59 AC3 gains the reverse direction: every inventory row's
  criterion, extracted, names the base its row names, `RUN.md` for the run's base or `fixture's
  base`. A row whose criterion names no base is red. Observed by AC4.
- **S5** — finding 2 (M2), the skeptic's corrected fix. 59 AC7's count is
  `grep -cE 'index\([^,)]*, *": "\)' tools/unattended/unattended.sh`, which must print 1 with its
  one hit on a line between `CLAIM_KV_AWK='` and its closing quote. The pattern matches a split
  under any variable name. Today it prints 1 at `:2170`, so the line-position clause is what makes
  it red before the build. Observed by AC5.
- **S6** — finding 15 (M2), the skeptic's corrected fix. 59 AC7 states its red case as a probe the
  pass runs: a scratch copy of the driver that adds `p = index(s, ": ")` to the age walk makes the
  count print 2. Observed by AC6.
- **S7** — finding 3 (M3), the skeptic's corrected fix. 57 keeps order 29, 56 moves to 30, 58 to 31
  and 59 to 32. The prose citing the old numbers moves with them: 56 §1's order sentence and its
  consumes-from edge to 57, 58 §1's "at order 29, so it sits at order 30", 59 §1's "at order 31,
  after unit 58 at 30" and 59 §3's no-renumbering bullet, and 57's hands-off edge to 56 and its
  Files touched sentence on 44. After `gen_build_index.py --write`, step 29 holds 57 alone and step
  30 holds 56 and 60, whose Files touched do not intersect. Observed by AC7.
- **S8** — finding 7 (M4). 57 §1 says that today's refusal comes from the subject test, because
  `c63aabbb` is dOrderedCharter's landing. 57 AC1 first asserts that `git log -1 --format=%s` of
  the merge it finds starts `merge: dPlacedRequest — land onto `, and otherwise prints `AC1
  unexercised` and does not pass. AC1 gains a contrast leg: the oracle run with the spec run's base,
  read by S10's form from `memory/builds/dPlacedRequest/RUN.LANDED.*.md`, walks the spec run's
  landing and exits 0, while the run's own base exits 2. Observed by AC8.
- **S9** — finding 10 (M5), the skeptic's corrected fix. 48's and 50's Files touched each carry the
  sentence word for word: "`TOOL-dPlacedRequest-<other>` writes `tools/unattended/unattended.test.sh`
  at order 25, so the two passes run in sequence." The joined read in 59 §4, and in 56 AC5 as 59 S19
  restates it, admits the backtick:
  ``grep -o 'TOOL-dPlacedRequest-[0-9]*`\? writes [^.]*unattended\.test\.sh[^.]*in sequence'``.
  Observed by AC9.
- **S10** — finding 14 (M6). 57 S1, 57 §4 and 44 AC1, the copy 57 S2 gives it, read the base by the
  library's filter, the spelling of `tools/unattended/check-pass-order.sh:356`:
  `b=$(bash -c '. tools/unattended/lib-unattended.sh; extract_run_facts' < memory/builds/dPlacedRequest/RUN.md | sed -n 's/^base:[[:space:]]*//p' | head -1 | tr -d '\r')`.
  57 §10 names `extract_run_facts` as the seam extended, and 57 AC2 requires 44 AC1 to name
  `extract_run_facts`. Observed by AC10.
- **S11** — finding 20 (M7). The function in `CLAIM_KV_AWK` strips a trailing CR from its line
  before the split, as `read_claims` does today at `:2170`, and declares `p`, `k` and `value` as
  function locals. 59 S7 and §4's sketch say so. The S7 arm gains a CRLF body row, run under
  `BINMODE=3` so the CR reaches the reader. Observed by AC11.
- **S12** — finding 4 (L1). 59 AC4 requires `fixture's base` in each bullet it extracts, and 59 AC5
  requires 43 AC24 to name `RUN.md`. Neither clause matches a bare `base` substring. Observed by AC12.
- **S13** — finding 5 (L2). The ancestor test's status case lives in 44 §4 only. 54 §4's `### The
  oracle's head` section becomes a pointer to 44 §4, as 59 S13 makes 52's. 59 S21 is restated to
  name 44 §4 alone, and 59 AC13 also requires `grep -c 'git rev-list'` over 54's head section to
  print 0. Observed by AC13.
- **S14** — finding 6 (L3). 57 AC2's no-sha clause reads 34's AC59 by unit 60 S1's bounded form. A
  scratch copy of 34 whose AC59 is correct and whose §9 line quotes `c63aabbb` passes the clause.
  Observed by AC14.
- **S15** — finding 8 (L4), the skeptic's corrected fix. 59 S1 and the 54 §4 Evidence bullet it
  writes say that the merge found on the real tree was a foreign landing, which the subject test
  refused before the ancestor test ran. 59 AC1 checks that bullet for `subject test`, and no longer
  for `the base itself`. Observed by AC15.
- **S16** — finding 11 (L5). For the age walk's keys only, the function trims the value's leading
  and trailing blanks, so `renews:` followed by two spaces parses to the empty value, as 52 S26
  says. `read_claims` passes `bare` 0 and gets no trim, so the strict reader admits nothing it
  refused before. 59 AC7 gains that two-space `renews:` row. Observed by AC16.
- **S17** — finding 12 (L6). 59 §1 reads "Four review items hold more than one id". Observed by
  AC17.
- **S18** — finding 13 (L7). 57 §5's perf line reads "one read of a run-state file of a few hundred
  lines at most". Observed by AC18.
- **S19** — finding 21 (L8). S10's read is the contract for 57's base, with the semantics of `fact`
  (`tools/unattended/unattended.sh:1350-1353`): a trailing CR stripped and any run of spaces after
  `base:`, none included. 57 §4 cites them. Observed by AC19.
- **S20** — finding 22 (L9). 59 S21 and the sketch in 44 §4 show the whole head. `[ -z "$t" ] ||
  [ "$own" = 0 ]` exits 2 with `no prepared merge on HEAD` first, and only then does the captured
  `merge-base --is-ancestor` case run. Observed by AC20.

## 3. Non-goals (OUT)

- No second mechanism for the high: unit 60 owns finding 16. S14 reads 34 AC59 by its form.
- No edit to `TOOL-dPlacedRequest-34`: S14's copy is scratch, and 34 sits 82 bytes under 48128.
- No change to which keys `read_claims` reads, or to its completeness check: S11 and S16 only keep
  the CR strip it already has, and the trim is for the walk's keys alone.
- No sequencing in the run that builds this unit: that run plans its roster from the headers before
  this pass, so S7 corrects the record and any later plan (§8 F1).
- No new gate leg, no lint over spec criteria and no new bug-class record: the arm rows join an
  existing suite, and the closing review's left-shift decides any record (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-57` — §1, S1, §4, §5, §10, AC1, AC2, the hands-off edge to 56 and the Files touched sentence on 44, which S7, S8, S10, S14, S18 and S19 amend
- **consumes-from** `TOOL-dPlacedRequest-59` — §1, §3, S1, S3, S7, S19, S21, §4's sketches, AC1, AC3, AC4, AC5, AC7 and AC13, which S1 to S7, S9, S11 to S13, S15 to S17 and S20 amend
- **consumes-from** `TOOL-dPlacedRequest-60` — the bounded read of 34 AC59, which S14 runs over a §9 line quoting a sha
- **consumes-from** `TOOL-dPlacedRequest-54` — §4's inventory, Evidence and head section as unit 59's pass leaves them, which S1 to S3, S13 and S15 amend
- **consumes-from** `TOOL-dPlacedRequest-44` — AC1 and §4's oracle as units 57 and 59 leave them, which S10, S13 and S20 amend
- **consumes-from** `TOOL-dPlacedRequest-56` — §1, the consumes-from edge to 57, the header order and AC5 as unit 59 restates it, which S7 and S9 amend
- **consumes-from** `TOOL-dPlacedRequest-58` — §1 and the header order, which S7 moves
- **consumes-from** `TOOL-dPlacedRequest-48` — the Files touched sequence sentence, which S9 fixes word for word
- **consumes-from** `TOOL-dPlacedRequest-50` — the Files touched sequence sentence, which S9 fixes word for word
- **hands-off** `TOOL-dPlacedRequest-62` — §2's "Extracted", AC13 and AC20, which that unit narrows and restates so a `###` section is read from its heading to the next heading
- **hands-off** `TOOL-dPlacedRequest-63` — §1, §2's preamble, S1, S4, S7, S10, S11, S12, S14, S19, S20, §4's sketches and Evidence, §5, §7, §8 F1 and their criteria, which that unit's items for every finding but 10 amend
- **hands-off** `TOOL-dPlacedRequest-64` — §4's reverse comment, Evidence and Alternatives, §5, §8 F1, S19, Files touched and Edges as unit 63's pass leaves them, which that unit's items for findings 1, 3, 7, 13 and 14 read and correct

## 4. Design

### The inventory sweep, both ways (S1 to S4)

```bash
join() { awk '/^- \*\*AC/{if(b)print b; b=$0; next} /^(- |#|$)/{if(b)print b; b=""; next} b{b=b" "$0} END{if(b)print b}' "$1" | tr -s ' '; }
for f in memory/builds/dPlacedRequest/spec/*.md; do
  u=${f##*-}; u=${u%.md}
  join "$f" | grep -E 'oracle[^.]*(runs|run |prints|exits)' | sed -nE "s/^- \*\*(AC[0-9]+)\*\*.*/$u \1/p"
done   # each hit must be an inventory row or an excluded row, matched as "<unit> AC<n>\b"
# reverse: each inventory row's criterion, extracted, names its row's base (RUN.md or fixture's base)
```

### The shared key reader, as this unit leaves it (S11, S16)

```
CLAIM_KV_AWK = function kv(line, keys, v, bare,   p, k, value)
  sub(/\r$/, "", line)
  p = index(line, ": ")
  p > 1             -> k = before p;  value = after p + 1
  bare and line ~ /^[a-z-]+:[ ]*$/ -> k = before ":";  value = ""
  bare              -> value trimmed of leading and trailing blanks
  (k in keys) and !(k in v) -> v[k] = value with tabs as spaces
```

### The oracle's head, stated once in 44 §4 (S13, S20)

```bash
t=$(git rev-list --first-parent --min-parents=2 --max-count=1 HEAD --)
case "$(git log -1 --format=%s "${t:-HEAD}" --)" in
  "merge: dPlacedRequest — land onto "*) own=1 ;; *) own=0 ;; esac
if [ -z "$t" ] || [ "$own" = 0 ]; then echo "version oracle: no prepared merge on HEAD"; exit 2; fi
git merge-base --is-ancestor "$t" "$base"; a=$?
case $a in
  0) echo "version oracle: no prepared merge on HEAD"; exit 2 ;;
  1) ;;
  *) echo "version oracle: the ancestor test failed"; exit 2 ;;
esac
```

### Evidence

- Measured 2026-10-25 on node a: S4's sweep over `memory/builds/dPlacedRequest/spec/*.md`, with
  `no oracle runs` dropped, printed 44 AC1 to AC3, 52 AC11 to AC14 and AC17, 54 AC1 and AC2, 55 AC1
  and AC2, 56 AC6 and AC10, 57 AC1, and 59 AC2, AC4, AC5, AC13 and AC21. 59 AC13 matched on text and
  runs no oracle. PINNED at that date; S3 re-measures at this pass.
- `grep -nE 'index\([^,)]*, *": "\)' tools/unattended/unattended.sh` printed one line, `:2170`, in
  `read_claims`, which runs `sub(/\r$/, "")` before the split. Read 2026-10-25.
- GNU Awk 5.4.0 on node a dropped the CR of a CRLF file read by default and through a pipe, and kept
  it under `BINMODE=3`. Measured 2026-10-25. PINNED at that date. The review read the dropped CR as
  making the CR case unobservable on node a; `BINMODE=3` makes it observable.
- S10's read printed `c63aabbb4a73d44315dd5dd1219ff1dac5055cf8` over this run's `RUN.md`, and the
  same sha over a scratch CRLF file holding `base:<sha>` with no space. Measured 2026-10-25.
- `tools/unattended/lib-unattended.sh:2057` defines `extract_run_facts`, which
  `tools/unattended/check-pass-order.sh:356` and `tools/unattended/check-brief-recorded.sh:381` read
  `base` through. Read 2026-10-25.
- The house sentence form, a backticked id before " writes", passed the joined read of S9 and failed
  59 §4's form, over a scratch Files touched section wrapped between `run in` and `sequence`.
  Measured 2026-10-25.
- `tools/workflows/unattended-build.js:608-613` sorts the roster by `order`, then by id, and its
  header says dispatch is strictly sequential within a shared order.
- `memory/builds/dPlacedRequest/RUN.md` holds 133 lines. Measured 2026-10-25.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/`: the specs of units 44, 48, 50, 54, 56, 57, 58 and 59, each
  edit a rev bump with its §9 line
- `tools/unattended/unattended.sh`: S11 and S16 in `CLAIM_KV_AWK`
- `tools/unattended/unattended.test.sh`: the CRLF and two-space rows in 59's S7 arm

### Alternatives rejected

- **Two batches.** S7 writes 59's header and S10 and S13 write 44, beside the items landing on 59
  and 44, so no split gives M6 two disjoint write sets.
- **The inventory derived from the sweep (finding 9's first fix).** The sweep misses 43 AC24, 52
  AC29 and 49 S3, so an inventory it derives drops them.
- **A trim in `read_claims` too (finding 11's first form).** It would let `status: live ` pass the
  strict reader's status test, which refuses it today.
- **A gate refusing a shared order over intersecting write sets (finding 3's left-shift).** It is
  a new leg, and the closing review's left-shift decides one.

## 5. Production-readiness checklist

- security — S11 keeps the CR strip `read_claims` has, and S16's trim is for the walk's keys only,
  so the strict reader admits nothing it refused before.
- perf / scale — one `sub` and one trim per claim body line; one sweep over the spec folder.
- error / empty / loading states — S8 reports an unexercised AC1 rather than passing it; a missing
  archive makes the contrast leg report the same.
- observability — S3 records the sweep's hit set, and S8 prints which test refused.
- risks — S7's renumbering lands after units 56 to 59 are built, so it corrects the record only
  (§8 F1).
- testing — the probes of §6 and the arm rows of §7.
- migration — none: every surface is new in this build.
- user docs — none beyond the specs: no user-facing behaviour changes.

## 6. Acceptance criteria

`join <file>` is §4's. The oracle fixtures are units 52's and 54's under `%TEMP%` with a short name.

- **AC1** — When §4's sweep runs over the spec folder, every hit is a row of 54's inventory or of
  its `Excluded, text only` sub-table, and 59 AC2, AC4, AC5 and AC21 are inventory rows naming
  `fixture's base`.
  Red when: a criterion of the batch that ran the oracle is not in the inventory.
- **AC2** — When 54's inventory rows are read, none holds ` to ` between two labels, and a label
  `52 AC1` does not match a hit `52 AC11` under 59 AC3's `AC<n>\b` test.
  Red when: a row stands for a range a label lookup cannot read.
- **AC3** — When §4's sweep runs over a scratch copy of the folder whose
  `2026-10-25-spec-TOOL-dPlacedRequest-54.md` lacks one inventory row, 59 AC3's comparison names
  that row's label. 54 §4 Evidence holds the hit set this pass measured.
  Red when: the sweep's result is compared with nothing.
  figure: the hit set DERIVED at this pass.
- **AC4** — When §4's sweep runs, 44 AC2 and 56 AC10 are hits for `oracle[^.]*(runs|run |prints|exits)`. When the reverse direction runs over
  a scratch copy of 54 whose 43 AC24 row names a criterion with no base, it is red on that row.
  Red when: an oracle criterion worded "prints" leaves the inventory unseen.
- **AC5** — When 59 AC7's `grep -cE 'index\([^,)]*, *": "\)'` runs over `tools/unattended/unattended.sh`
  it prints 1, and that line sits inside `CLAIM_KV_AWK`'s text.
  Red when: the count admits read_claims' own split beside the shared one.
- **AC6** — When the same count runs over a scratch copy of the driver whose age walk adds
  `p = index(s, ": ")`, it prints 2, and 59 AC7's `Red when:` names that copy.
  Red when: a second split under another variable name is invisible.
- **AC7** — When `grep -o 'order [0-9]*'` reads the status headers of 56, 57, 58, 59 and 61, it
  prints `order 30`, `order 29`, `order 31`, `order 32` and `order 33`. After
  `gen_build_index.py --write`, the README's build-order step 29 lists `TOOL-dPlacedRequest-57`
  alone. 56's §1 names `order 30`, and 58's §1 names `order 31`.
  Red when: two units sharing a step write one file.
- **AC8** — When 57's AC1 bullet is extracted, it names `AC1 unexercised`, `land onto` and
  `RUN.LANDED`. 57 §1 names `subject test`.
  Red when: a refusal criterion passes without showing which test refused.
- **AC9** — When the S9 joined read runs over 48's and 50's Files touched sections and over a
  scratch copy of 48 whose sentence wraps between `run in` and `sequence`, each prints one match
  naming the other unit.
  Red when: a house-style sentence makes the criterion print nothing.
- **AC10** — When 57's S1 and AC2 and 44's AC1 are extracted, each names `extract_run_facts`, and
  `grep -c "/\^## Run facts/"` over each extraction prints 0. 57 §10 names `extract_run_facts`.
  Red when: a criterion keeps its own reader of the Run facts grammar.
- **AC11** — When the S7 arm's CRLF row feeds `status: live` ending in CR to the shared function
  under `BINMODE=3`, the claim reads complete. A copy of the function without the strip reads it
  incomplete.
  Red when: the shared reader refuses a claim the old reader accepted.
- **AC12** — When 59's AC4 and AC5 bullets are extracted, AC4 names `fixture's base` and AC5 names
  `RUN.md`. 56 AC10 as it stands today fails AC4's clause.
  Red when: a substring of `merge-base` satisfies a base clause.
- **AC13** — When 54's `### The oracle's head` section is extracted, `grep -c 'git rev-list'` over
  it prints 0 and it names `TOOL-dPlacedRequest-44`. 59 S21 names 44 §4 and not 54 §4.
  Red when: the oracle's head is stated in two specs.
- **AC14** — When unit 60's bounded read runs over a scratch copy of 34 with a correct AC59 and a
  §9 line quoting `c63aabbb`, `grep -cE '[0-9a-f]{8}'` over the output prints 0.
  Red when: a sha in the revision log fails a criterion about AC59.
  fixture: the scratch copy is made under the run's scratch directory.
- **AC15** — When 54's §4 Evidence real-tree bullet is read, it names `subject test`, and 59's AC1
  bullet names `subject test` and not `the base itself`.
  Red when: the evidence names the wrong test as the one that refused.
- **AC16** — When the arm's row feeds `renews:` and two spaces to the walk's call, the value is
  empty. `status: live` with a trailing space through `read_claims`' call still reads incomplete.
  Red when: a trim widens what the strict reader admits.
- **AC17** — When `grep -c 'Four review items'` runs over 59's spec, it prints 1.
  Red when: a stated count disagrees with its list.
- **AC18** — When `grep -c 'under a hundred lines'` runs over 57's spec, it prints 0, and
  `wc -l < memory/builds/dPlacedRequest/RUN.md` prints under 300.
  Red when: a size claim is false.
- **AC19** — When S10's read runs over a scratch run-state file holding `base:<sha>` with CRLF
  endings, it prints the bare sha. 57 §4 names `unattended.sh:1350`.
  Red when: a hand-edited fact reads as no base.
- **AC20** — When 44's §4 oracle section is extracted, `[ "$own" = 0 ]` appears on a line before
  `merge-base --is-ancestor`, and on 54's no-merge fixture row the oracle prints `no prepared merge
  on HEAD`.
  Red when: the short-circuits are lost in a swap of the `if`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC11 AC16 · the CRLF row staged against the function without its CR strip, and the two-space row against it without its trim · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How is finding 3 closed when this unit is built after units 56 and 57 (S7)?** (a)
  Renumber 56 to 30, 58 to 31 and 59 to 32 at this pass, the skeptic's corrected fix; (b) keep the
  orders and restate 57's and 56's prose to the dispatcher's tie-break, which runs 56 before 57
  (`tools/workflows/unattended-build.js:608-613`); (c) a gate refusing a shared order over
  intersecting write sets. (b) leaves the index rendering a dependent pair as parallel. (c) is a new
  leg. The run that builds this unit plans its roster before this pass, so under every option unit
  56's pass there precedes 57's. That is harmless, because 56 S11's measurement of 34 counts no edit
  of 57's and 59 S8 re-measures 34 after both. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. The
  index and any later plan read true. widens: none · relaxes: none
- **F2 — Where does the value trim live (S16)?** (a) Inside the function, for the walk's keys only;
  (b) inside the function for every caller; (c) in each caller. (b) widens the strict reader. (c)
  is the second reader S7 of unit 59 removes. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-6 promotions' 11
  MEDIUM and 9 LOW findings.
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edges to `TOOL-dPlacedRequest-62` and `TOOL-dPlacedRequest-63`, mirroring their consumes-from.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.

## 10. Reuse audit

Each item extends the unit its finding names, and the new text reuses three seams. They are
`extract_run_facts` (`tools/unattended/lib-unattended.sh:2057`) for S10 and S19, unit 59's
`CLAIM_KV_AWK` for S11 and S16, and unit 60's bounded read for S14.
`python tools/codebase-map/reuse_lookup.py "read a run fact such as base from the run-state file
section"` ranked `read` and `read_text`, name stems only. The bullet probe of unit 60 ranked
`extract_run_facts` among its four. `python tools/memory-recall/query.py "how is a spec audit's minor
findings batch promoted into one unit that amends the specs and code its predecessors wrote"`
returned TOOL-aDistilledCharter-7, TOOL-aGraftedHelix-32 and -36, `TOOL-dPlacedRequest-52`,
`TOOL-dPlacedRequest-56` and `TOOL-dPlacedRequest-59`, batches of the same kind. None disagrees with
source, except this audit's L5 on node a's CR, which §4 Evidence corrects.

Recall terms used: minors batch promote medium low round finding renumber order extract_run_facts CLAIM_KV_AWK inventory
