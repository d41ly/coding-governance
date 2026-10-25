# TOOL-dPlacedRequest-63 — the round-7 promotions' minors: every inventory row names its base, the sweep places its own criteria, one run-fact clause, a CR the arm can see, and criteria that read what they amend

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 35 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-63-deviation-631.md](../build/2026-10-25-build-TOOL-dPlacedRequest-63-deviation-631.md) | deviation | — |
| [2026-10-25-review-TOOL-dPlacedRequest-62-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-62-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-7 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-60-spec-audit.md`)
exited CONVERGED with 22 confirmed findings. Its one high, finding 13, is unit 62. This unit is the
batch BUILD-METHOD M4 makes of the rest: 12 MEDIUM and 9 LOW findings by raw id, one scope item per
id, each naming its finding and, in brackets, the review item holding it (M1 to M8, L1 to L8). Four
review items hold more than one id (M2: 2, 9 and 23; M3: 6 and 16; M4: 8 and 22; L3: 5 and 12).
Findings 11 and 7 report one defect at two binding grades, items M5 and L4, and each keeps its own
item and its own observation.

Findings 10 and 15 land on unit 60 and the rest on unit 61 and on the specs and code its pass
leaves, so this unit repairs none in particular and sits above every unit of the build, at order
35, after unit 62 at 34. It is built after units 60, 61 and 62, and every edit is made in place on
what their passes left. Criterion ACn observes item Sn.

| Item | Finding | Severity | Lands on |
|---|---|---|---|
| S1 | 1 (M1) | MEDIUM | units 43, 52, 54, 57, 59, 61 |
| S2 to S4 | 2, 9, 23 (M2) | MEDIUM | units 54, 61 |
| S5, S6 | 6, 16 (M3) | MEDIUM | units 57, 61 |
| S7, S8 | 8, 22 (M4) | MEDIUM | unit 61, the S7 arm of unit 59 |
| S9 | 11 (M5) | MEDIUM | unit 61 |
| S10 | 14 (M6) | MEDIUM | unit 61 |
| S11 | 21 (M7) | MEDIUM | units 44, 61 |
| S12 | 24 (M8) | MEDIUM | units 59, 61, `CLAIM_KV_AWK` and its arm |
| S13 | 3 (L1) | LOW | unit 61 |
| S14 | 4 (L2) | LOW | units 59, 61 |
| S15, S16 | 5, 12 (L3) | LOW | units 57, 61 |
| S17 | 7 (L4) | LOW | unit 61 |
| S18 | 10 (L5) | LOW | unit 60 |
| S19 | 15 (L6) | LOW | units 57, 60, 61 |
| S20 | 17 (L7) | LOW | units 57, 61 |
| S21 | 18 (L8) | LOW | units 56, 61 |

## 2. Scope (IN)

Every edit to another unit's spec is in place, one rev bump per spec with its §9 line naming this
unit and the items it carries. "The run's base", "the fixture's base" and "extracted" are 61 §2's,
as unit 62 narrows the last and S19 joins its bullet half. "The sweep" is 61 §4's and "the reverse
direction" is 61 S4's.

- **S1** — finding 1 (M1). The reverse direction matches `RUN\.md|fixture's( later)? base`, so 59
  AC2's `fixture's later base` reads as named. This unit's pass runs it over every inventory row of
  54 §4 as units 59 and 61 leave it, and writes the base wording into each row's criterion that
  lacks it: `the fixture's base` on a fixture row, and the `base:` fact of `RUN.md` on a run row.
  The `49 S3` row is read through 44 AC1, the criterion it names. Measured today, the rows no unit
  rewords are 43 AC24, 52 AC11 to AC14 and AC17, 54 AC1, 57 AC1 and 59 AC21; S3 owns 61 AC20. 61
  S4 and S12, its Files touched and its Edges name 43 and 52. Observed by AC1.
- **S2** — finding 2 (M2). 54 §4's `Excluded, text only` sub-table, as unit 61 leaves it, names 61
  AC4 and AC13, each with the phrase that matched, and 61 S1's excluded list names them. 61 §4
  Evidence's hit set names 56 AC19. Observed by AC2.
- **S3** — finding 9 (M2). 61 AC20 is an inventory row of 54 §4, and its bullet says it runs on 54's
  no-merge fixture with the fixture's base. 61 S1's row list names it. Observed by AC3.
- **S4** — finding 23 (M2). The sweep's population is the whole spec folder, the specs of units 60
  to 63 included. At this unit's pass every hit is an inventory row or an excluded row, 62's and
  63's hits too, and 54 §4 Evidence records the hit set measured then. 61 §4 Evidence's pinned set
  points at that record. Observed by AC4.
- **S5** — finding 6 (M3). 61 S10 restates 57 AC2's clause "names `RUN.md` and `## Run facts`" in
  place, to "names `RUN.md` and `extract_run_facts`", and 57 AC2 as unit 61 leaves it reads so.
  Observed by AC5.
- **S6** — finding 16 (M3). 61 AC10 greps the plain spelling: 57's AC2 bullet, extracted, holds no
  `Run facts`, and 44's AC1 bullet, extracted, meets 57 AC2's name clause. Observed by AC6.
- **S7** — finding 8 (M4). The CRLF row's invocation is spelled. The arm lifts `CLAIM_KV_AWK` out
  of the shipped driver bytes, the way `slice_fn` lifts a function, and runs `awk -v BINMODE=3`
  over that text. An environment prefix is not the form. 61 S11, its §4 Evidence's GNU Awk bullet
  and its §7 `New arm:` line say so, and the Evidence bullet names the forms measured. Observed by
  AC7.
- **S8** — finding 22 (M4). 61 AC11 is restated to that invocation. The lifted function reads the
  CRLF row's `status` as `live`, and a copy without its CR strip reads `live` and a CR. Under the
  environment prefix both read `live`, which AC11 records as the form that cannot go red on node a.
  This unit's pass runs the staged copy. Observed by AC8.
- **S9** — finding 11 (M5). 61 AC4's first clause reads 59's AC3 bullet, extracted, and requires
  it to hold the widened pattern `oracle[^.]*(runs|run |prints|exits)`. Observed by AC9.
- **S10** — finding 14 (M6). 61 §8 F1, its §5 risks line and its last Alternatives bullet are
  restated from the driver. At a shared order the workflow reaches 56 before 57 by id
  (`tools/workflows/unattended-build.js:608-613`), and `--dispatch` then refuses 56 with fail 49
  while 57 is neither CLOSED nor WONTDO (`tools/unattended/unattended.sh:13746-13758`, asserted at
  `tools/unattended/unattended.test.sh:6399-6411`). That refusal is option (c)'s existing seam, so
  (c) is not a new leg. Option (a) and S7 stand, S7's reason being that the index reads true.
  Observed by AC10.
- **S11** — finding 21 (M7). 61 §4's head sketch opens with `base=$1` and the
  `git rev-parse -q --verify "$base^{commit}"` refusal printing `version oracle: base does not
  resolve`, ahead of `t=`, as 54 §4 has them. 44 §4, as unit 61 leaves it, holds them in that place.
  61 AC20 gains both observations of AC11. Observed by AC11.
- **S12** — finding 24 (M8). `CLAIM_KV_AWK`'s bare branch matches `/^[a-z-]+:[[:blank:]]*$/`, the
  class the trim uses, in `tools/unattended/unattended.sh` and in the sketches of 61 §4 and 59 §4.
  The S7 arm of 59 gains a `renews:` plus tab row beside the two-space row, and 61 AC16 names it.
  `read_claims` passes `bare` 0, so its reads are unchanged. Observed by AC12.
- **S13** — finding 3 (L1). 61 S14 says that 57 AC2's no-sha clause reads unit 60 S1's bounded
  output, an edit unit 60 makes and 61 does not repeat. 61 AC14 reads 57's AC2 bullet instead of
  re-running 60's command. Observed by AC13.
- **S14** — finding 4 (L2). 61 S20 writes the whole head into 44 §4 alone, and 59 S21 is a pointer
  to 44 §4, as 61 S13 has it. 61 AC13 gains a clause over 59's S21 bullet. Observed by AC14.
- **S15** — finding 5 (L3). 61 S19 and 57 §4 cite the read's semantics from its parts.
  `extract_run_facts` (`tools/unattended/lib-unattended.sh:2057`) keeps the `## Run facts` section
  and its CRs, the `sed` expression takes any run of blanks after `base:`, and `tr -d '\r'` takes
  the CR. Beside `fact` (`tools/unattended/unattended.sh:1359-1375`) the one difference is a tab
  after `base:`, which `fact` keeps. Observed by AC15.
- **S16** — finding 12 (L3). 61 AC19 and its §4 Evidence bullet name the scratch file's bytes: a
  `## Run facts` heading, then `base:<sha>`, each line ending CRLF. Observed by AC16.
- **S17** — finding 7 (L4). 61 AC4 runs the pattern 59's AC3 bullet states, as S9 extracts it,
  and requires 44 AC2 and 56 AC10 among its hits. Observed by AC17.
- **S18** — finding 10 (L5). 60 AC3 requires a §9 line of 57 naming this edit:
  `grep -cE 'TOOL-dPlacedRequest-60\b.*AC2'` over 57's §9 prints at least 1. Observed by AC18.
- **S19** — finding 15 (L6), the skeptic's corrected fix. Unit 60 S1's form is the one reader of a
  labelled bullet, and its output is joined by `| tr '\n' ' ' | tr -s ' '`. 60 S1 and 57 AC2's
  spelled read, as unit 60 leaves it, append the join. 61 §2's "Extracted", as unit 62 narrows it,
  names the joined form for S and AC bullets. It says why the sweep keeps its own join: the sweep
  reads every bullet of a file in one pass, which a label reader cannot. Observed by AC19.
- **S20** — finding 17 (L7). 61 S10's list gains 57 AC1's phrase naming S1's reader, reworded to
  "read by `extract_run_facts`". 61 AC10 becomes a sweep of the spec folder. Observed by AC20.
- **S21** — finding 18 (L8). 61 S7's update list gains 56 §3's "No renumbering of any order"
  bullet, restated to name S7's moves. 61 AC7 gains the order prose of 59 §1 and the edges of 56 and
  57. Observed by AC21.

## 3. Non-goals (OUT)

- No second mechanism for the high: unit 62 owns finding 13. S11, S14 and S19 extend the readers and
  criteria it restates.
- No change to which keys `read_claims` reads or to its completeness check: S12 widens the bare
  branch alone, which only the walk's keys reach.
- No edit to `TOOL-dPlacedRequest-34`: it sits 82 bytes under 48128, and S13 reads 57 AC2 instead.
- No sequencing in the run that builds this unit: that run plans its roster before this pass, so
  S10 corrects the record only.
- No driver knob for the arm: §8 F2.
- No new gate leg, no lint over spec criteria and no new bug-class record: the arm rows join an
  existing suite, and the closing review's left-shift decides any record (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-61` — §1, §2's preamble, S1, S4, S7, S10, S11, S12, S14, S19, S20, §4's sketches and Evidence, §5, §7, §8 F1 and AC4, AC7, AC10, AC11, AC13, AC14, AC16, AC19 and AC20, which every item but S18 amends
- **consumes-from** `TOOL-dPlacedRequest-62` — §2's narrowed "Extracted" and the restated AC13 and AC20, which S11, S14 and S19 extend
- **consumes-from** `TOOL-dPlacedRequest-60` — S1's bounded form and AC3, which S18 and S19 amend
- **consumes-from** `TOOL-dPlacedRequest-54` — §4's inventory, its excluded sub-table and its Evidence as unit 61 leaves them, and AC1, which S1 to S4 amend
- **consumes-from** `TOOL-dPlacedRequest-57` — AC1, AC2 and §4 as units 60 and 61 leave them, which S1, S5, S15, S19 and S20 amend
- **consumes-from** `TOOL-dPlacedRequest-59` — AC3, AC21, S21 and §4's key reader sketch as unit 61 leaves them, and the S7 arm, which S1, S9, S12, S14 and S17 amend
- **consumes-from** `TOOL-dPlacedRequest-44` — §4's oracle as unit 61 leaves it, which S11 gives the base refusal
- **consumes-from** `TOOL-dPlacedRequest-52` — AC11 to AC14 and AC17, which S1 gives the fixture's base
- **consumes-from** `TOOL-dPlacedRequest-43` — AC24, which S1 gives the `base:` fact of `RUN.md`
- **consumes-from** `TOOL-dPlacedRequest-56` — §3's renumbering bullet, which S21 restates
- **hands-off** `TOOL-dPlacedRequest-64` — S1, S7, S10, S11, S15, S19, §4's readers, sketches and Evidence, §5, §6's preamble, §8 F2, §10, Edges, AC1, AC7, AC8, AC10, AC11, AC15, AC18, AC19 and AC21 as this unit's pass leaves them, which that unit's items for every finding but 6, 10, 18 and 19 amend

## 4. Design

### The reverse direction, as this unit leaves it (S1, S4, S19)

```bash
d=memory/builds/dPlacedRequest/spec
bullet() { awk "/^- \*\*$2\*\*/{f=1;print;next} f&&/^(- |#|\$)/{exit} f" \
  "$d/2026-10-25-spec-TOOL-dPlacedRequest-$1.md" | tr '\n' ' ' | tr -s ' '; }
# for each inventory row "<unit> <label>" of 54 §4; the 49 S3 row reads 44 AC1
bullet "$u" "$l" | grep -qE "RUN\.md|fixture's( later)? base" || echo "red: $u $l"
```

`bullet` is unit 60 S1's form with the label as an argument and S19's join appended. `\*\*` after
the label keeps `AC1` from reading `AC10`.

### The CRLF row's invocation (S7, S8)

```bash
s=$(grep -n "^CLAIM_KV_AWK='" "$SCRIPT" | cut -d: -f1)
e=$(awk -v s="$s" "NR>s && /'\$/ {print NR; exit}" "$SCRIPT")
eval "$(sed -n "${s},${e}p" "$SCRIPT")"      # the shipped text, lifted as slice_fn lifts a function
printf 'status: live\r\n' | awk -v BINMODE=3 "$CLAIM_KV_AWK"'
  BEGIN { K["status"] = 1 } { kv($0, K, v, 0) } END { print (v["status"] == "live") }'
```

### The key reader's bare branch (S12)

```
bare and line ~ /^[a-z-]+:[[:blank:]]*$/ -> k = before ":";  value = ""
```

### The oracle's head, opening (S11)

```bash
base=$1
git rev-parse -q --verify "$base^{commit}" >/dev/null \
  || { echo "version oracle: base does not resolve"; exit 2; }
t=$(git rev-list --first-parent --min-parents=2 --max-count=1 HEAD --)
# the rest as 61 §4's sketch states it
```

### Evidence

- Measured 2026-10-25 on node a: the reverse direction over the rows of 59 S3 and 61 S1, read by
  `bullet`, was red on 43 AC24, 44 AC1 to AC3, 49 S3, 52 AC11 to AC14 and AC17, 54 AC1, 55 AC1 and
  AC2, 56 AC6 and AC10, 57 AC1, 59 AC21 and 61 AC20. 52 AC29 does not exist yet. Units 57 and 59
  reword 44's, 49's, 55's and 56's rows, so S1's list is the rest. PINNED at that date; S1
  re-measures at this pass.
- GNU Awk 5.4.0 on node a, over `status: live` and a CR: the default read printed length 12,
  `BINMODE=3 awk` as an environment prefix 12, `awk -v BINMODE=3` 13 and `BEGIN{BINMODE=3}` 13,
  from a file and through a pipe. Measured 2026-10-25. PINNED at that date.
- `extract_run_facts` piped to S10's `sed` and `tr` printed nothing over a CRLF file holding only
  `base:<sha>`, and the sha over the same file with a `## Run facts` CRLF line first. A tab after
  `base:` was taken by the `sed`. Measured 2026-10-25.
- `fact` strips a trailing CR at `tools/unattended/unattended.sh:1364` and leading spaces only at
  `:1371`. Read 2026-10-25.
- `tools/unattended/unattended.test.sh:708` defines `slice_fn`, which evals a function out of the
  shipped driver bytes by its line span. Read 2026-10-25.
- 57's §9 holds one line naming `TOOL-dPlacedRequest-60`, the round-7 hands-off fold, and
  `grep -cE 'TOOL-dPlacedRequest-60\b.*AC2'` over 57's §9 printed 0. Measured 2026-10-25.
- `grep -lE "/\^## Run facts/|S1'?s .awk."` over the spec folder printed 57's spec alone, and
  `grep -c 'shared order\|at this order'` printed 1 over 56 and 1 over 57. Measured 2026-10-25.
- `grep -c 'neither CLOSED nor WONTDO, so the consumer would build' tools/unattended/unattended.sh`
  printed 1, the fail-49 message at `:13758`. Read 2026-10-25.
- The sweep over 62's and 63's specs as written printed `63 AC11`, the one criterion of the two
  that runs the oracle, which names the fixture's base. Measured 2026-10-25.

### Files touched (estimate)

- `memory/builds/dPlacedRequest/spec/`: the specs of units 43, 44, 52, 54, 56, 57, 59, 60 and 61,
  each edit a rev bump with its §9 line
- `tools/unattended/unattended.sh`: S12 in `CLAIM_KV_AWK`
- `tools/unattended/unattended.test.sh`: the CRLF invocation and the tab row in 59's S7 arm

### Alternatives rejected

- **Two batches.** S18 and S19 write 60, and S19 also writes 61 §2 beside every item landing on 61,
  so no split gives M6 two disjoint write sets.
- **The reverse direction limited to the rows 59 S4 and S5 reword (finding 1's second fix).** It
  leaves inventory rows whose criteria state no base, the case the direction exists to catch.
- **A `CLAIM_BINMODE` knob on the driver's calls (finding 8's first form).** It adds an environment
  surface to a shipped kit for a test arm's sake.
- **Taking S14 and AC14 out of 61 (finding 3's first fix).** It leaves 61's item list with a gap
  and no criterion of 61's own for finding 6.

## 5. Production-readiness checklist

- security — S12 widens the bare branch alone, which `read_claims` never reaches with `bare` 0, so
  the strict reader admits nothing it refused before.
- perf / scale — one class change in one awk branch; one sweep and one reverse pass over the spec
  folder at this pass.
- error / empty / loading states — S11 names the empty base's refusal; S1 prints each red row.
- observability — S4 records the hit set measured at this pass, and S8 records which invocation
  cannot go red.
- risks — S1's derived list may differ from the pinned one; a red row outside it is amended the same
  way, Files touched and Edges first.
- testing — the probes of §6 and the arm rows of §7.
- migration — none: every surface is new in this build.
- user docs — none beyond the specs: no user-facing behaviour changes.

## 6. Acceptance criteria

`bullet <unit> <label>` and the reverse direction are §4's. `sec <file> <prefix>` is unit 62 §4's.
The oracle fixtures are units 52's and 54's under `%TEMP%` with a short name.

- **AC1** — When the reverse direction reads each inventory row of 54 §4, it prints no `red:` line.
  Over a scratch copy of 52 whose AC11 bullet names no base, it prints `red: 52 AC11`. 61's S4
  bullet names `fixture's( later)? base`.
  Red when: an inventory row's criterion states no base.
  fixture: the scratch copy is made under the run's scratch directory.
- **AC2** — When 54 §4's `Excluded, text only` sub-table is read, it names `61 AC4` and `61 AC13`,
  each with a phrase, and 61 §4 Evidence's hit set names `56 AC19`.
  Red when: a hit among the batch's own criteria has no placement.
- **AC3** — When 54 §4's inventory is read, it holds a `61 AC20` row, and `bullet 61 AC20` names
  `fixture's base`.
  Red when: a criterion of the batch that walks history is placed as text only.
- **AC4** — When the sweep reads the folder with units 60 to 63 present, every hit is an inventory
  row or an excluded row, `63 AC11` among the rows. 54 §4 Evidence holds that hit set under this
  pass's date.
  Red when: the pinned set predates the specs it sweeps.
  figure: the hit set DERIVED at this pass.
- **AC5** — When `bullet 57 AC2` is read, it names `RUN.md` and `extract_run_facts`, and
  `bullet 61 S10` names the restated clause.
  Red when: a replacement leaves the clause it replaces standing.
- **AC6** — When `bullet 57 AC2` is read, `grep -c 'Run facts'` over it prints 0, and `bullet 44 AC1`
  names `RUN.md` and `extract_run_facts`. `bullet 61 AC10` names `grep -c 'Run facts'`.
  Red when: a criterion greps for a retired heading in one spelling only.
- **AC7** — When `bullet 61 S11` and 61's §7 `New arm:` line are read, each names `-v BINMODE=3`,
  and 61 §4 Evidence's GNU Awk bullet names `BEGIN{BINMODE=3}` and the environment prefix.
  Red when: a platform knob is spelled in a form that leaves the CR dropped.
- **AC8** — When the CRLF row runs §4's lifted `CLAIM_KV_AWK` under `awk -v BINMODE=3`, `status`
  reads `live`. A copy without `sub(/\r$/, "", line)` reads `live` and a CR, and under the
  environment prefix both read `live`. `bullet 61 AC11` names `-v BINMODE=3`.
  Red when: the staged break cannot go red on the machine the evidence came from.
- **AC9** — When `bullet 59 AC3` is read, it holds `oracle[^.]*(runs|run |prints|exits)`, and
  `bullet 61 AC4` names `59 AC3`.
  Red when: a criterion reads its own copy of a pattern instead of the edited one.
- **AC10** — When 61's §8 F1 span is read, it names `--dispatch` and `fail 49`, and
  `grep -c 'It is a new leg\|That is harmless'` over 61's spec prints 0.
  `grep -c 'neither CLOSED nor WONTDO, so the consumer would build' tools/unattended/unattended.sh`
  prints 1.
  Red when: a fork is resolved on an account of the driver the code contradicts.
- **AC11** — When `sec` reads 44's `### The oracle` section, `base does not resolve` sits on a line
  before the first `rev-list`. On 54's no-merge fixture, with the fixture's base given as the empty
  string, the oracle prints `version oracle: base does not resolve` and exits 2. 61 §4's head sketch
  opens `base=$1`.
  Red when: an empty base reaches the ancestor test and is refused with the wrong line.
- **AC12** — When the arm's row feeds `renews:` and a tab to the walk's call, the value is empty, as
  for `renews:` and two spaces. A copy whose bare branch reads `[ ]*` leaves the key absent.
  `bullet 61 AC16` names the tab row.
  Red when: a key reader's match and its trim use two whitespace classes.
- **AC13** — When `bullet 61 AC14` is read, it names 57's AC2 bullet and its `Red when:` names an
  unbounded read. `bullet 57 AC2` holds `f&&/^(- |#|$)/{exit}`.
  Red when: a criterion re-runs a sibling's fixed command and never reads the text it certifies.
- **AC14** — When `bullet 59 S21` is read, `grep -c 'merge-base --is-ancestor'` over it prints 0 and
  it names `44 §4`. `bullet 61 S20` names 44 §4 and not 59 S21, and `bullet 61 AC13` names `59 S21`.
  Red when: a sketch stated once has two copies.
- **AC15** — When `bullet 61 S19` is read, it names `extract_run_facts`, `lib-unattended.sh:2057`
  and `tr -d`, and 57's `### The read, at the close` section, read by `sec`, names
  `extract_run_facts`.
  Red when: a contract cites a reader the pipeline does not run.
- **AC16** — When S10's read of 61 reads a scratch file holding `## Run facts` then `base:<sha>`,
  each line ending CRLF, it prints the bare sha. Without the heading it prints nothing.
  `bullet 61 AC19` names `## Run facts`.
  Red when: a fixture written from the criterion's text reads as no base.
  fixture: the scratch file is made under the run's scratch directory.
- **AC17** — When the pattern `bullet 59 AC3` holds is grepped over each joined bullet of the
  folder, 44 AC2 and 56 AC10 are among its hits, and under `oracle[^.]*(runs|run )` neither is.
  `bullet 61 AC4` names the pattern's source as `59 AC3`.
  Red when: a criterion passes whichever pattern 59 AC3 states.
- **AC18** — When `awk '/^## 9\./{f=1;next} /^## /{f=0} f'` reads 57's §9,
  `grep -cE 'TOOL-dPlacedRequest-60\b.*AC2'` over it prints at least 1, and `bullet 60 AC3` names
  that pattern. Over a scratch copy of 57 without unit 60's §9 line it prints 0.
  Red when: a record check is green before the unit it records is built.
- **AC19** — When `bullet 60 S1` and `bullet 57 AC2` are read, each names `tr -s ' '`, and 61's §2
  preamble names the joined form and the sweep's own join. Over a scratch copy of 59 whose AC4
  wraps between `fixture's` and `base`, `bullet` finds `fixture's base` and unit 60 S1's form
  without the join does not.
  Red when: one bullet has two readers that disagree on a wrapped phrase.
  fixture: the scratch copy is made under the run's scratch directory.
- **AC20** — When `grep -rlE "/\^## Run facts/|S1'?s .awk." memory/builds/dPlacedRequest/spec/`
  runs, every path it prints is 61's or 63's spec, and `bullet 57 AC1` names `extract_run_facts`.
  Red when: a copy of a superseded reader survives in a sibling.
- **AC21** — When 59's §1 is read, it names `order 32` and `order 31`, and 56's §3 holds no
  `No renumbering of any order`. `sec` over the `### Edges` sections of 56 and 57, piped to
  `grep -c 'shared order\|at this order'`, prints 0 for each.
  Red when: a renumbering leaves prose citing the old orders.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC8 AC12 · the CRLF row staged against the lifted function without its CR strip under `awk -v BINMODE=3`, and the tab row against a bare branch matching spaces only · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How is finding 1 closed (S1)?** (a) The base wording written into each red row's
  criterion, the rows derived by running the reverse direction at this pass; (b) the reverse
  direction limited to the rows 59 S4 and S5 reword. (b) leaves rows whose criteria state no base.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's first fix judged sound, with
  its criterion over the built folder. widens: none · relaxes: none
- **F2 — How does the CRLF row's `BINMODE` reach the shared function (S7)?** (a) The arm lifts
  `CLAIM_KV_AWK` out of the shipped driver bytes and runs it under `awk -v BINMODE=3`; (b) the
  driver's two calls take `-v BINMODE="${CLAIM_BINMODE:-0}"` and the arm sets the variable. (b) adds
  an environment surface to a shipped kit, which BUILD-METHOD M3's veto 2 discards. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, on the `slice_fn` seam. widens: none · relaxes: none
- **F3 — How is finding 3 closed (S13)?** (a) 61 AC14 reads 57's AC2 bullet; (b) 61 S14 and AC14
  taken out, citing 60 AC1 and AC2. (b) leaves a gap in 61's items and no criterion of 61's own for
  finding 6. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's second fix judged
  sound, the option keeping a criterion that can fail. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-7 promotions' 12
  MEDIUM and 9 LOW findings.
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.

## 10. Reuse audit

Each item extends the unit its finding names, and the new text reuses four seams: unit 60 S1's
bullet form for every labelled read, unit 62's section form for every `###` read, `slice_fn`
(`tools/unattended/unattended.test.sh:708`) for S7's lift of the shipped text, and the fail-49 edge
refusal of `--dispatch` (`tools/unattended/unattended.sh:13746-13758`) for S10's account.
`python tools/codebase-map/reuse_lookup.py "keep a carriage return visible to awk so a line reader's
strip is observable"` ranked `read`, `read_text` and `read_conf`, name stems only, none a CR-aware
reader: no existing seam fits beyond `slice_fn`. `python tools/memory-recall/query.py "how is a spec
audit's minor findings batch promoted into one unit that amends the batch spec its predecessor round
wrote"` returned TOOL-aDistilledCharter-7, TOOL-aGraftedHelix-32 and -36, `TOOL-dPlacedRequest-61`,
`TOOL-dPlacedRequest-52` and `TOOL-dPlacedRequest-59`, batches of the same kind. None disagrees with
source.

Recall terms used: minors batch promote medium low round finding inventory reverse direction BINMODE extract_run_facts renumber
