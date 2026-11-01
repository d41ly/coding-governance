# TOOL-dFoldedAudit-2 — --review and check 2 record and grade a spec exit that folds

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base 74274869 · streams tooling · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-2-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-2-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`--review` records a spec audit's terminal exit with `folded` and `promoted` counts, a fold legal
there, and check 2 grades that row so a fold cannot hide a HIGH. A run preflighted before the dated
cutoff, a closing diff review and every landed record keep today's bytes.

## 2. Scope (IN)

- **S1** — The flags. `--review` takes `--folded <N>` and `--promoted <N>`, parsed beside `--minors`
  and held to the same decimal rule. Observed by AC1 and AC6.
- **S2** — The rule. `read_spec_exit_rule` answers `old`, `counted` or `folds` from the subject, the
  cutoff, the record's own date and the disposal switch. Observed by AC7, AC8 and AC9.
- **S3** — The exit check. `check_spec_exit` holds this unit's one new `fail 37` site and refuses the
  flags off their rule, an unreadable switch, absent counts, a short sum and a disposition its
  counts do not derive. Observed by AC3, AC5, AC6 and AC7.
- **S4** — The row. A spec exit under `counted` or `folds` writes the design's row, disposition last.
  Observed by AC1 and AC4.
- **S5** — The fold refusal. `check_exit_fold` holds the two identical refusals as one site and
  passes a fold under `folds`. Observed by AC4, AC7 and AC13.
- **S6** — The sentences. The exit notes, the BOUNDED line and the terminal-subject refusal name the
  rule that applied, and today's literals stand for `old`. Observed by AC4 and AC12.
- **S7** — Check 2's reading of `SPEC_FOLD_CUTOFF`: imported, a malformed value named inside check 2,
  a blank one announced. Observed by AC1, AC8 and AC11.
- **S8** — Check 2's row clause: the new row's counts, sum and disposition graded on any spec exit
  past the cutoff. Observed by AC2, AC3 and AC5.
- **S9** — Check 2's promotion floor for the new row, and no floor for a fold. Observed by AC10.
- **S10** — The comments at `tools/unattended/unattended.sh:12659-12666`, `:12687-12693`,
  `:12781-12786` and `:12806-12811` state the two rules. NOT OBSERVED: a comment changes no behaviour,
  and the closing review reads it.

## 3. Non-goals (OUT)

- A closing diff review. Its exit rows, `closing-review-recorded` and every literal it prints keep
  every byte of behaviour.
- The DISPOSAL stage and `writeRound`, which are `TOOL-dFoldedAudit-3`'s. That unit's undeclared path
  writes today's row, and past a dated cutoff this unit's `--review` refuses it.
- The chain verdict and any row naming a spec. Check 2 grades counts, and `TOOL-dFoldedAudit-5`
  derives the chain from its own record.
- A rewrite of a landed record, or a re-grade of one: rows before the cutoff keep their shape and their
  grading.
- `specs-audited`, `closing-review-recorded`, `tools/unattended/check-pass-order.sh` and
  `tools/unattended/run-unattended-gates.sh`, which carry no disposition rule.
- Prose carriers, a kit version bump, and any new check number.
- A new `fail` site in `tools/unattended/check-unattended.sh`, which stands at its ceiling.

### Edges

- **consumes-from** `TOOL-dFoldedAudit-7` — `read_spec_audit_switch disposal` and `SPEC_FOLD_CUTOFF` as initialised and shape-checked by the driver; without them no spec exit reaches a rule but `old`
- **hands-off** `TOOL-dFoldedAudit-3` — `writeRound` passes `--folded` and `--promoted` after the stage, keeps every adjudicated UNVERIFIED finding in `--minors`, and reads the first call's refusal, which keeps naming `exits <state>` and a missing flag
- **hands-off** `TOOL-dFoldedAudit-1` — the `--review` entry, the state list and the key-table row describe the row, the flags and `SPEC_FOLD_CUTOFF` as built

## 4. Design

Every change branches on the subject through `verb_review`'s `subj = slug` split
(`tools/unattended/unattended.sh:12694`). No shared branch is reworded: each literal an existing suite
arm pins stays, and a new sentence sits beside it.

### The rule

`read_spec_exit_rule` takes the run-state file, the slug and the subject. It sets `_se_rule` and
`_se_why`, the out-variable idiom of `runmd_of` and `fact` (`:12676`).

| Subject | `SPEC_FOLD_CUTOFF` and the record | Disposal switch | `_se_rule` | Row | `fold` |
|---|---|---|---|---|---|
| the slug | not read | not read | `old` | today's | refused |
| a spec subject | blank, or the record began before it | not read | `old` | today's | refused |
| a spec subject | the record began on or after it | `promote-all` | `counted` | the new row | refused |
| a spec subject | the record began on or after it | `by-nature` | `folds` | the new row | legal |

**The date is the preflight's.** The cutoff keys on the date the run was preflighted, and never on the
README's `opened:`, because the chain builds opened in October and not yet started must inherit the
new rule. `check_landed_facts_due <record> <cutoff>` (`tools/unattended/lib-unattended.sh:1755`) already
is that predicate: status 0 graded, 1 grandfathered, 2 off on a blank cutoff. It reads
`read_first_commit_date` (`:1731`), whose floor dates a live `RUN.md` in a rotated folder at its own
tenancy, and it treats a record with no committed history as graded, which is the new run. Both readers
call it, so the driver and check 2 cannot disagree about one record, the
`two-guards-one-question-two-answers` class. Its `git log -1` runs first, so a record last touched
before the cutoff costs one spawn. A comment at each new call says the function reads any record
cutoff.

The switch is read only when the cutoff admits the record, so a run under `old` spawns no Python. A
refused read sets `_se_why` and leaves `_se_rule` at `counted`.

### The exit check

`check_spec_exit` is called once, directly after `state=$(review_state ...)` at `:12774`. It calls
`read_spec_exit_rule` on a terminal state, and it leaves `_se_rule` at `old` on every other state.

| Order | Condition | `_se_why` |
|---|---|---|
| 1 | the switch read refused | the reader's line |
| 2 | `_se_rule` is `old` and `--folded` or `--promoted` was given | `--folded and --promoted are counted only at a spec audit's terminal exit past SPEC_FOLD_CUTOFF` |
| 3 | `--highs` or `--minors` is absent | none: the check returns, and the refusals at `:12790` and `:12816` answer as today |
| 4 | `--disposition fold` under `counted` | none: the check returns, and `check_exit_fold` answers with today's sentence |
| 5 | `--folded` or `--promoted` is absent | the exit requires both, because every confirmed finding is folded or promoted and a row that does not count them cannot be graded |
| 6 | `f + p < b + h + m` | names the counts and says the findings fall short, so a confirmed finding has no disposition |
| 7 | `_se_rule` is `counted` and `f > 0` | a spec exit under `promote-all` folds nothing |
| 8 | the disposition is not the one the counts derive | names the disposition the counts derive |

The one site reads:

```bash
fail 37 "--review cannot record this spec audit exit: $_se_why"
```

**Rows 3 and 4 keep today's first refusal.** `TOOL-dFoldedAudit-3` probes a round with a bare first
call, and it reads the state word after `exits` in the refusal, so that sentence must still arrive
under `folds` and `counted`.

**Why one site.** `check-arms` holds the driver's census at 323 against a ceiling of 323, and
`check-unattended.sh`'s at 264 against 264 (PINNED, `python tools/memory-tree/check-arms.py --report`
on 2026-11-01: 318 branches plus five refusal sites, and 264 branches). `check-arms` reds a census past
its ceiling (`tools/memory-tree/check-arms.py:989`), and the way up is the owner's retirement review
(`tools/memory-tree/README.md:550`). So this unit adds one site and takes one away:

- `:12796` and `:12820` print one sentence from two places. `check_exit_fold`, taking the state, the
  review kind and the disposition, holds that `fail 37` once and is called from both places, in
  today's order. It returns 0 under `folds`. The census moves by minus one.
- `check_spec_exit` adds one. The census ends at 323, and the armed floor of 309 holds.
- The decimal rule costs no site: `folded` and `promoted` join the loop at `:12709`, whose `case` gains
  a `*[!0-9]*` alternative that only those two can reach, the other three being refused above it.

A helper naming a literal check number stays visible to `check-arms`. The rule at `:12742-12744` bars
a helper taking the code as a parameter.

### The row

```
verdict <v> · blockers <b> · <EXIT> · highs <h> · minors <m> · folded <f> · promoted <p>[ · disposition fold|promote]
```

`counts` at `:12832` gains the two fields under `counted` and `folds`, and `disp` stays last because
check 2 reads the disposition as the last field (`:12849`). The disposition is `promote` when `p > 0`,
`fold` when `p = 0` and `f > 0`, and absent when nothing stood. `f + p` counts findings, not units,
and equals `b + h + m` plus any UNVERIFIED finding the disposal adjudicated. The check is therefore
`f + p >= b + h + m`. `refuted` is not on the row: it covers the UNVERIFIED population alone
(`tools/workflows/unattended-build.template.js:2145-2149`), so it can never stand for a confirmed
finding, and a disposal return with `standing` is refused before any row exists.

In `verb_review`:

| Site | Under `old` | Under `counted` | Under `folds` |
|---|---|---|---|
| `:12789` no disposition at a non-converged exit | today | today | skipped: row 3 or row 8 answers |
| `:12793` and `:12819` fold | today, through `check_exit_fold` | today, through `check_exit_fold` | passes |
| `:12823-12831` `owe` and its two refusals | today | skipped | skipped |
| `owe` for the note at `:12853` | today | `max(1, p - m)` when `p > 0`, else 0 | the same |

### The sentences

`review_exit_note` keeps its `promote|closing` arm and gains `spec-fold` and `spec-promote`, used only
under `folds`. Both keep the word `FOLDS`, and `spec-promote` keeps `PROMOTED`.

| Exit | Under `old` and `counted` | Under `folds` |
|---|---|---|
| a fold | unreachable | every finding confirmed at this exit FOLDS into the spec it names, rev bumped, and none needs a new mechanism |
| a promotion | today | a finding that needs a new mechanism is PROMOTED to a unit of this build, a BLOCKER or HIGH to its own, the MEDIUMs and LOWs batched into one unit or two across disjoint write sets, and every other finding FOLDS into the spec it names |
| the BOUNDED line at `:12862` | `DISPOSED BY SEVERITY` | `DISPOSED BY NATURE` |

**The terminal-subject refusal.** `:12767` keeps its site and its refusal, because a chain's later
round is a fresh subject `<slug>-spec-set-r<N>` and one subject still takes no further round. Its
closing clause becomes `$route`, set through `read_spec_exit_rule` on this refusal path alone:

- `old` and `counted`: today's `is DISPOSED under the build method's M4 by the severity rule, and never re-rounded`.
- `folds`: `is DISPOSED under the build method's M4 by its nature, through the chain's next subject, and never re-rounded`.

### Check 2

| Line in `tools/unattended/check-unattended.sh` | Change |
|---|---|
| `:242` and the allow-list at `:333-341` | `SPEC_FOLD_CUTOFF=""` joins the initialiser, and the key joins the allow-list; check 22 reads both (`:3317`) |
| after `:719` | blank announces on stdout: `unattended: SPEC_FOLD_CUTOFF is blank or undeclared, so every spec audit exit keeps the old rule and no fold is graded` |
| after `:743` | a malformed value joins `rv_bad` and `rv_foldcut` stays empty, as `SPEC_COUNTS_CUTOFF`'s does; no `fail` site |
| after `:820` | `rv_foldpast=1` when `rv_foldcut` is set and `check_landed_facts_due "$rvf" "$rv_foldcut"` answers 0, passed to the awk as `foldpast` |
| `:839-841` | parse ` · folded <n>` and ` · promoted <n>` into `fo` and `pr` |
| `:850-851` | `specbad`'s fold half reads `foldpast != 1`, so a fold row past the cutoff leaves that clause while `!cnt` stays |
| beside `:851` | the row clause below |
| `:853`, `:863`, `:870` | each needs-assignment also stores `pp[it] = pr` and `nw[it] = nr`; the third gains `&& !nr` |
| `:880-896` | `if (nw[it]) { if (disp[it] == "promote") { nsubj++; nneed += floor } }` precedes `graded != 1`, so a fold past the cutoff owes nothing with `DISPOSITION_CUTOFF` blank too, and never reaches `closefold` |
| after `:900` | `rowbad`'s one sentence |

```awk
nr = (foldpast == 1 && it != slug)
if (nr && rs ~ /CONVERGED|NON-CONVERGENT|CEILING|BOUNDED/ && cnt) {
  want = pr > 0 ? "promote" : (fo > 0 ? "fold" : "")
  got  = (nf > 0 && fld[nf] ~ /^disposition /) ? substr(fld[nf], 13) : ""
  if (fo < 0 || pr < 0 || fo + pr < b + hi + mi || want != got) rowbad[it] = 1
}
```

The sentence is `record an exit row past SPEC_FOLD_CUTOFF whose folded and promoted counts are absent,
fall short of the findings it counted, or disagree with its disposition, so a confirmed finding cannot
be traced to a fold or a unit`. It feeds `rv_bad` and the existing `fail 2` at `:932`, so the census of
`check-unattended.sh` does not move.

**It runs on the counts, never on the verdict word.** The clause reads `b`, `hi`, `mi`, `fo` and `pr`,
and a `verdict CLEAN` row with a short sum reds. That is design tag `[survive]`'s first property,
answering what `tools/workflows/unattended-build.template.js:2013-2018` records.

**The floor.** `m` counts every MEDIUM, LOW and adjudicated UNVERIFIED finding, so `p - m` is a lower
bound on the promoted BLOCKERs and HIGHs, each of which takes its own unit, and a positive `p` takes
at least one. The row names neither which findings were promoted nor their severities, so the floor is
`max(1, p - m)` and stops there. It is a floor, as `:914` says of today's.

**What the row cannot show.** Check 2 sees counts, not which finding went where. That a fold named its
spec and rev is `TOOL-dFoldedAudit-3`'s reconciliation, and design tag `[survive]`'s third property is
met here only as far as a row's own arithmetic reaches.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `read_spec_exit_rule` | `sh.function` | the `read` row of `.lexicon.conf` |
| `check_spec_exit` | `sh.function` | `lexicon.py --suggest` answered OK on 2026-11-01 |
| `check_exit_fold` | `sh.function` | the `check` row of `.lexicon.conf` |
| `--folded`, `--promoted` | `--review` flags | design tag `[row]` |
| `spec-fold`, `spec-promote` | `review_exit_note` arguments | none, a closed `case` |

### Rollout

Dark until the close: `SPEC_FOLD_CUTOFF` stays blank through this unit, so every `--review` reads
`old` and spawns nothing new. `check-unattended.test.sh`'s `mkconf` declares
`SPEC_FOLD_CUTOFF="2099-01-01"` beside its `DISPOSITION_CUTOFF` line (`:246`), for that line's reason:
it moves no arm's verdict and keeps the announcement off the shared fixture. The blank-cutoff arm
strips it.

### Files touched (estimate)

`tools/unattended/unattended.sh`
`tools/unattended/check-unattended.sh`
`tools/unattended/unattended.test.sh`
`tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **Six `fail 37` sites, one per refusal, as the scout's "keep fail-37 branches inline" suggests.** Six
  past a ceiling of 323, which only the owner's review moves. The scout did not read
  `REFUSAL_CEILINGS`.
- **A third rule for `counted` writing today's row.** `TOOL-dFoldedAudit-3` AC6 requires `--folded 0` on
  a `promote-all` row, and one row shape past the cutoff keeps check 2 from reading a switch.
- **Check 2 reading the disposal switch.** It would grade a landed row by today's policy file.
- **`rv_fc` for the new cutoff.** That date has no floor, so a re-preflighted slug would read as the
  previous run's date.
- **Renaming `check_landed_facts_due`.** The name is narrower than the function, but a rename writes
  `tools/unattended/lib-unattended.sh`, outside this unit's file set, for no behaviour.
- **`f + p` graded as an equality.** Design tag `[row]` admits adjudicated findings above `b + h + m`,
  and a row written by hand under that sentence would red.

## 5. Production-readiness checklist

- **security** — No new write path: one more field pair on the row `park` already writes, screened by
  the decimal rule. A hand-edited row reds or keeps today's grading, and neither loosens one.
- **perf / scale** — `--review` adds one `git log` at a terminal spec exit, and one Python start only
  past a dated cutoff. Check 2 adds one `git log -1` per record with a review row, and a
  `--follow` walk only for a record touched at or after the cutoff.
- **error / empty / loading states** — A record with no commit reads as past a dated cutoff, which is
  the new run. An exit with nothing standing writes no disposition.
- **observability** — The rule shows on the row: only a spec exit past the cutoff carries `folded`.
  A blank cutoff is announced on every kit-gate run.
- **risks** — `check-arms` stands at 323 of 323 after this unit, so `TOOL-dFoldedAudit-5`'s verbs owe
  their own site-for-site cover or the owner's review. A row dated on the landing day by a run still
  on the old driver reads as past the cutoff, the `FOLD_CUTOFF` scar at
  `tools/unattended/unattended.sh:1009-1012`; `TOOL-dFoldedAudit-7` gives the close that check.
- **testing** — Fixture repositories, hand-written rows for what the driver refuses to write, and
  committer dates pinned so no arm depends on the day it runs. `fixture-passes-by-finding-nothing` is
  answered by a green control beside each red row.
- **migration** — Additive and forward only. No row is rewritten, and `.unattended.conf` is untouched
  here.
- **user docs** — `help/` documents neither `--review` nor the spec audit
  (`grep -ln -e '--review' help/*.md` prints nothing), so no page moves.

## 6. Acceptance criteria

Fixture R is a scratch git repository at `%TEMP%/fa2r` on branch `main` with no remote, holding copies
of `tools/unattended/` whole and of `tools/policy/policy.py` and `tools/policy/catalogue.toml` at those
paths, a `.unattended.conf` carrying `MEMORY_ROOT=memory`, `DISPOSITION_CUTOFF="2000-01-01"`,
`REVIEW_ROUNDS="1"` and `SPEC_FOLD_CUTOFF="2026-11-01"`, and a build `memory/builds/tFix/` whose
`RUN.md` is built as the suites' `mkdisp` and `bcopen` build it, its first commit dated with
`GIT_COMMITTER_DATE`. `DATED` means that date is `2026-11-02T12:00:00 +0000`, and `EARLY` means
`2026-10-30T12:00:00 +0000`. Hand-written rows are committed in that `RUN.md`. `$D` and `$G` are
`bash "$F/tools/unattended/unattended.sh"` and `bash "$F/tools/unattended/check-unattended.sh"`, the
fixture's own copies by absolute path, run with the fixture as the working directory, and only their
`UNATTENDED check 2` and `check 37` lines are read.

- **AC1** — When a `DATED` fixture runs `$D --review tFix --subject S1 --verdict "CLEAN WITH FIXES" --blockers 0 --highs 1 --minors 2 --folded 3 --promoted 0 --disposition fold`,
  it exits 0, and `RUN.md`'s last row ends `blockers 0 · CONVERGED · highs 1 · minors 2 · folded 3 · promoted 0 · disposition fold`;
  `$G` then prints no `UNATTENDED check 2 FAILED` line.
  Red when: `--review` refuses a spec fold, or check 2 reads the row through `specbad` or `closefold`.
- **AC2** — When an `EARLY` fixture commits AC1's row by hand, `$G` prints
  `spec subject(s) S1 record a terminal row with no highs and minors counts or with disposition fold`.
  Red when: the rule is keyed on today's date or on the README's `opened:`, so the old row reads as new.
- **AC3** — When a `DATED` fixture runs `$D --review tFix --subject tFix --verdict "CLEAN WITH FIXES" --blockers 0 --highs 0 --minors 3 --folded 3 --promoted 0 --disposition fold`,
  it refuses naming `--folded`, and a hand-written row `item tFix · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 0 · minors 3 · folded 3 · promoted 0 · disposition fold`
  makes `$G` print `record disposition fold on a row carrying highs and minors`.
  Red when: the `it != slug` half of `nr` is lost, so a closing review folds.
- **AC4** — When a `DATED` fixture runs `$D --review tFix --subject S2 --verdict BLOCKED --blockers 2 --highs 0 --minors 0 --folded 2 --promoted 0 --disposition fold`,
  it exits 0 printing `BOUNDED`, `DISPOSED BY NATURE` and `FOLDS`, and `$G` prints no check 2 line.
  Red when: a LOCAL BLOCKER is refused, or the state gate at `tools/unattended/unattended.sh:12793` still
  answers it.
- **AC5** — When a `DATED` fixture runs the same call with `--blockers 0 --highs 2 --folded 1`, it
  refuses naming `fall short`, and a hand-written row with those counts under `verdict CLEAN` makes `$G`
  print `record an exit row past SPEC_FOLD_CUTOFF`.
  Red when: a HIGH can leave the count, or the clause reads the verdict word.
- **AC6** — When a `DATED` fixture passes `--folded 1 --promoted 2 --disposition fold`, the call refuses
  naming `promote` on AC1's counts; `--highs 0 --minors 0 --folded 0 --promoted 0 --disposition fold`
  refuses; `--folded 3 --promoted 0` with no disposition refuses; and `--folded 08` refuses naming
  `at most nine digits`. A hand-written row
  carrying `folded 1 · promoted 2 · disposition fold` makes `$G` print `record an exit row past SPEC_FOLD_CUTOFF`.
  Red when: the disposition is taken from the flag and not derived from the counts.
- **AC7** — When a `DATED` fixture commits `.governance/policy.toml` setting `disposal = "promote-all"`
  under `[review.spec-audit]`, `--highs 1 --minors 0 --folded 1 --promoted 0 --disposition fold` refuses
  with `which folds nothing`; `--folded 1 --promoted 1 --disposition promote` refuses naming `promote-all`;
  and `--folded 0 --promoted 1 --disposition promote` exits 0, writing `folded 0 · promoted 1 · disposition promote`.
  An out-of-set value refuses with `policy: refused`.
  Red when: the switch is ignored, so the old value does not restore today's refusal. This is the
  refusal half of the brief's acceptance line 7.
- **AC8** — When a `DATED` fixture blanks `SPEC_FOLD_CUTOFF`, `--highs 1 --minors 0 --disposition promote`
  writes a row ending `highs 1 · minors 0 · disposition promote`, `--folded 0` refuses, and `$G` prints
  `SPEC_FOLD_CUTOFF is blank or undeclared`. With `tools/policy/` deleted from the fixture the first call
  still exits 0.
  Red when: a blank cutoff reads as the new rule, or an `old` exit reads the switch.
- **AC9** — When an `EARLY` fixture commits a later change to `RUN.md` dated `DATED`, `--folded 0` refuses,
  because the record began before the cutoff; and when a `DATED` rotation adds an archived
  `RUN.LANDED.0bd0bd00.md` beside an `EARLY` `RUN.md`, `--folded 3` with AC1's counts exits 0.
  Red when: the date is the last commit's, or `read_first_commit_date`'s floor is bypassed.
- **AC10** — When a `DATED` fixture's row carries `blockers 0 · CONVERGED · highs 2 · minors 1 · folded 0 · promoted 3 · disposition promote`
  and its README gains one new unit id over its pinned base, `$G` prints `against a floor of 2`; with two
  ids it prints no check 2 line. AC1's row with no new id prints no check 2 line, and neither does it with
  `DISPOSITION_CUTOFF` stripped from the conf.
  Red when: a promoted row owes today's `owe`, or a fold owes a unit.
- **AC11** — When the fixture's conf sets `SPEC_FOLD_CUTOFF="soon"`, `$G` prints a check 2 line naming
  `SPEC_FOLD_CUTOFF` and `soon`.
  fixture: `$D` refuses this conf at load, so only `$G` runs here, and it reads the conf itself.
  Red when: a malformed cutoff grades every record or none in silence.
- **AC12** — When a `DATED` fixture's S1 is terminal, a further `--review tFix --subject S1` prints
  `by its nature, through the chain's next subject`; under a blank cutoff, and on `--subject tFix`, it
  prints `by the severity rule, and never re-rounded`.
  Red when: the route sentence is reworded on the shared path, or a second round is admitted.
- **AC13** — When `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh tools/unattended/check-unattended.sh`
  runs, it prints 318 and 264, and `grep -c 'which folds nothing' tools/unattended/unattended.sh` prints 1
  in a `fail` line.
  figure: both PINNED, measured 2026-11-01 at `dccdeaa8`, and valid until a later unit of this build
  adds a site.
  Red when: a refusal is written as a new site, which passes the ceiling.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers`

The kit gate's check 22 reds on `SPEC_FOLD_CUTOFF` until `TOOL-dFoldedAudit-1` writes its key-table
row. That is owed at the close, where the gate runs, and not at this unit's pass.

New arm: tools/unattended/unattended.test.sh · covers AC1 AC4 · a dated record past the cutoff, staged with `check_exit_fold` refusing under `folds` · none
New arm: tools/unattended/unattended.test.sh · covers AC3 AC5 AC6 · one call per row of the exit check's table, staged with `check_spec_exit` returning at its head · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · a committed `promote-all` policy file, staged with `read_spec_exit_rule` answering `folds` past the cutoff whatever the switch says · none
New arm: tools/unattended/unattended.test.sh · covers AC8 AC9 · a blank cutoff, an early record and a rotated folder, staged with the rule reading today's date · none
New arm: tools/unattended/unattended.test.sh · covers AC12 · a terminal subject under each rule, staged with `$route` fixed to the `folds` sentence · none
New arm: tools/unattended/check-unattended.test.sh · covers AC1 AC2 · the same fold row committed at `DISPDATE` either side of the cutoff, staged with `foldpast` fixed at 1 · none
New arm: tools/unattended/check-unattended.test.sh · covers AC3 · a counted fold on the slug subject, staged with `it != slug` dropped from `nr` · none
New arm: tools/unattended/check-unattended.test.sh · covers AC5 AC6 · a short sum under `verdict CLEAN` and a disagreeing disposition, each staged with the row clause deleted, beside a green control · none
New arm: tools/unattended/check-unattended.test.sh · covers AC10 · one id and two against a floor of 2, and a fold with none, staged with the `nw[it]` branch deleted · none
New arm: tools/unattended/check-unattended.test.sh · covers AC8 AC11 · a blank and a malformed `SPEC_FOLD_CUTOFF`, with the blank arm stripping `mkconf`'s line, staged with the two reads deleted · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.

## 10. Reuse audit

The seams are `verb_review` (`tools/unattended/unattended.sh:12673`) and its `subj = slug` split at
`:12694`, check 2's awk (`tools/unattended/check-unattended.sh:821`), and
`check_landed_facts_due` (`tools/unattended/lib-unattended.sh:1755`), which both readers already call.
`reuse_lookup.py` ranked only name-stem hits for this behaviour and no seam beyond those. Recall returned
TOOL-aEvidencedLens-7 and TOOL-aBatchedMinors-3, whose counted-row shape this row extends, and the bug
class `a-merged-in-check-can-refuse-a-pinned-record` is the reason for the cutoff.

Where the records and the source disagreed: the scout's return says to keep the `fail 37` branches
inline, and `REFUSAL_CEILINGS` at `.memory-tree.conf:653` leaves no room for them, so they share one
site. It reads `FOLD_CUTOFF` and `SPEC_COUNTS_CUTOFF` as the model for the third cutoff; those two are
driver constants read with `core_of`, and the design's conf key is read through the import allow-list
as `DISPOSITION_CUTOFF` is. It says `specs-audited` needs no change, and this unit leaves it alone.

Recall terms used: `python tools/memory-recall/query.py "spec audit exit fold disposition row counted check 2 cutoff" --terms "disposition fold promote spec exit highs minors check 2 FOLD_CUTOFF SPEC_COUNTS_CUTOFF review row"`.
Reuse probe used: `python tools/codebase-map/reuse_lookup.py "record a review round exit row with counts and grade its disposition"`.
