# TOOL-dAlignedCarrier-4 — `--status` reports the holder-worktree and pinned-asks verdicts, read-only

**Status:** SPECCED · rev-1 · 2026-09-30 · node d · Tier-2 · base 87c245b3 · streams tooling · order 1 · advances TOOL-dDerivedDocket-72 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-5 TOOL-dAlignedCarrier-6 |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-3 TOOL-dAlignedCarrier-5 TOOL-dAlignedCarrier-6 |

<!-- /gen:spec-records -->

## 1. Goal

A no-id `--resume` runs two checks before it refuses: whether this worktree holds the run's branch
(check 58) and whether the build README's `asks:` line at HEAD is still the one the run pinned
(check 73). `--status` runs neither. The owner ruled that the build method's regrounding step moves
from a no-id `--resume`, which logs check 59 at every pass boundary, to `--status`, extended to report
those two verdicts read-only. This unit is that extension, and the stop contract's sentence about
regrounding follows it. Pointing the build method at `--status` is unit 5's.

## 2. Scope (IN)

- **S1** — `check_asks_moved` is minted in `tools/unattended/unattended.sh` and holds the one
  comparison `check_asks_pinned` makes today: the run-state file's pinned `asks` fact against the
  `asks:` line of the build README at HEAD. It returns 0 when the two differ and sets `AM_PIN` and
  `AM_NOW` to the two values, returns 1 when they agree or nothing is pinned, prints nothing and calls
  no `fail`. `check_asks_pinned` becomes that call followed by its existing `fail 73`, text unchanged.
  Observed by AC2, AC5.
- **S2** — `derive_holder_where` is minted and holds the derivation `check_holder_worktree` makes
  before its first `fail 58`: the path of the worktree `git worktree list --porcelain` shows with
  `HW_REF` checked out, else the remedy for a branch no worktree has checked out, else the remedy for
  a branch that does not exist here. `check_holder_worktree` calls it, and its refusal text is
  unchanged. Observed by AC3, AC5.
- **S3** — `verb_status` adds two fields to its one status line, both placed before the `keepalive`
  field, which stays the last suffix. Each prints on exactly the records whose `--resume` would run
  its check, and prints its verdict there whether it passes or not. The asks field prints whenever
  the record pins `asks`, as `--resume` runs check 73 on every row. The worktree field prints when the
  record carries `lease-utc`, its phase is not terminal, and it is not a LANDING the landed log
  observed, which are the rows on which `--resume` reaches check 58. A record on which neither check
  runs prints the bytes it printed at BASE. The spellings are §4's "Fields". Observed by AC1, AC2,
  AC3.
- **S4** — The report is READ-ONLY: the new code writes no fact, stages nothing and calls no `fail`, so
  `--status` exits as it does today whatever either verdict reads. Observed by AC4.
- **S5** — The stop contract's §8 paragraph opening "The no-id rows print the `--status` block FIRST"
  (`tools/unattended/STOPS.template.md:188` at BASE) is rewritten: the no-id rows still print the
  status block first, for any caller that spells `--resume` without an id, and `--status` carries the
  holder-worktree and pinned-asks verdicts that those rows reach first, as fields on its one line, so
  a session regrounding with `--status` loses neither. It names neither the build method's step nor
  its spelling, so it holds whichever order unit 5 lands in. The render follows. Observed by AC6.
- **S6** — The driver comment above `verb_resume` (`tools/unattended/unattended.sh:6267-6271` at BASE)
  is reworded the same way. Observed by AC6.
- **S7** — Arms for each field are written in `tools/unattended/unattended.test.sh`, not run: a moved
  asks line, a wrong worktree naming the holder's path, a record naming no run branch, a record with
  no `lease-utc`, and a passing record whose line is unchanged. Observed by AC7.

## 3. Non-goals (OUT)

- BUILD-METHOD M7 step 1. Naming `--status` there is unit 5's work.
- The `--status` entry of `tools/unattended/VERBS.template.md`, which enumerates the verb's optional
  fields. No accept clause of this build names that carrier, so M3 veto 2 leaves it to the owner. The
  entry stays right about the line's shape, a field joining it or not printing, and it does not list
  the two new fields.
- The Skill, whose Resume section already runs `--status` first.
- Any other check a no-id `--resume` reaches, such as 57 or 59. Those are refusals for want of an id
  or a clock, and a regrounding session has neither question.
- The resume matrix. Every row keeps its behaviour and its text.
- The kit version. The orchestrator moves it once, at VERIFYING.

### Edges

Files shared with a sibling, which are not edges. `tools/unattended/unattended.sh` is also written by
units 1, 3 and 6; this unit touches `check_asks_pinned`, `verb_status`, `check_holder_worktree` and
the comment above `verb_resume`, and nothing in the regions they own. `tools/unattended/unattended.test.sh`
is also written by units 3 and 6; this unit appends a new arm region. The stop contract's template
and render are this unit's alone.

- **hands-off** `TOOL-dAlignedCarrier-5` — BUILD-METHOD M7 step 1 names `--status` for regrounding
  under a mandate; this unit makes that verb carry the two verdicts a no-id resume reached first.
- **hands-off** external — the VERBS carrier's `--status` entry, for the owner, under veto 2.

## 4. Design

### Evidence

Read at `87c245b3` on 2026-09-30. `verb_resume` calls `check_asks_pinned` above every row
(`tools/unattended/unattended.sh:6290`) and `check_holder_worktree` for a record carrying `lease-utc`,
after the terminal and observed-landing rows (`:6394`). `resolve_holder_worktree` writes and prints
nothing. `check_holder_worktree` calls `verb_status` before its refusal when no id was passed, so the
new field and the refusal agree on one invocation. `verb_status` prints ONE line, and the suite arms
that at several sites, among them `check_status_one_line` in `tools/unattended/unattended.test.sh`:
every existing field joins the line only when it has something to say. `fail` records its check number
on the run journal's END line, which is why S1 and S4 keep it out of the report path.

### Fields

Appended before the `keepalive` field, the asks field first. Each field is one of these spellings:

```
 · asks as pinned
 · asks moved at HEAD, check 73 refuses a resume: pinned [<pinned value>] at HEAD [<value at HEAD>]
 · worktree holds the run
 · worktree not the run's, check 58 refuses a resume here: <derive_holder_where's text>
 · worktree unanswerable, the record names no run branch
```

`asks as pinned` prints when `check_asks_moved` returns 1 over a record that pins `asks`, and the
moved spelling when it returns 0. The three worktree spellings print when `resolve_holder_worktree`
returns 0, 1 and 2. The unanswerable one is a pass on `--resume`, which announces it on a line of its
own; here it prints so that a verdict the verb cannot give never reads as one it gave. None of the
five carries the ` · ` separator inside itself.

The pass spellings print because the owner's ruling has the verb REPORT the two verdicts, and a
report that is silent on a pass cannot be told from a verb that never asked. The regrounding step
unit 5 points at `--status` reads them in this run's own worktree, where both pass.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `check_asks_moved` | shell function, verb `check` | `sh.function` |
| `derive_holder_where` | shell function, verb `derive` | `sh.function` |
| `AM_PIN`, `AM_NOW` | globals set by `check_asks_moved` | none; `.lexicon.conf` declares no cell for a shell global |

Both names were asked of `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` and read
OK on 2026-09-30.

### Rollout

The render is `bash tools/unattended/adopt-unattended.sh`, run in the same pass after the template
edit; it re-renders the Skill and re-copies the protocol and the stop contract. `bash tools/unattended/adopt-unattended.sh --check`
is the parity observation.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/STOPS.template.md` ·
`memory/guides/UNATTENDED-STOPS.md` · `tools/unattended/unattended.test.sh`

### Alternatives rejected

- Calling `check_asks_pinned` and `check_holder_worktree` from `verb_status` and discarding their
  status. Each calls `fail`, which records a check number in the journal and prints a `FAILED` line,
  so the report would not be read-only; and `check_holder_worktree` calls `verb_status`.
- A second output line for the verdicts. The one-line promise is armed across the suite and read by
  every whole-output reader.
- Printing a verdict only when it fails, the verb's older field rule. A regrounding session could not
  tell a pass from a check the verb never ran, and unit 5's acceptance reads both verdicts on this
  run's own passing record.

## 5. Production-readiness checklist

- security — N/A: a read verb gains two comparisons over files it already reads; no write surface.
- perf / scale — one `git show` of the README at HEAD and one `git worktree list`, only on records
  that pin asks or carry a lease; milliseconds against the verb's existing reads.
- error / empty / loading states — a record naming no run branch prints the unanswerable field;
  nothing pinned prints nothing; a README absent at HEAD reads as an empty line and so as moved,
  exactly as check 73 reads it.
- observability — the two fields are the observability this unit adds.
- risks — every status line of a record carrying `lease-utc` or pinning `asks` gains bytes. A suite
  arm comparing such a line with a literal would red; arms comparing two readings of one fixture
  keep agreeing. The build pass greps the suite's `--status` arms for literal comparisons, amends
  each, and names them in its ledger.
- testing — the fixture observations below; the arms, written and not run.
- migration — none: no fact is added or read that a record lacks.
- user docs — the stop contract's §8 paragraph.

## 6. Acceptance criteria

- **AC1** — When the BASE driver, extracted by `git archive 87c245b3 tools/unattended` into a scratch
  directory, and the built driver each run `--status` over a passing fixture record, the built line
  is one line and carries `asks as pinned` and `worktree holds the run`, and with those two fields cut
  out it is byte-identical to the BASE line. With the `asks` and `lease-utc` facts deleted from the
  record, the two drivers print byte-identical lines.
  Red when: a passing verdict is silent, a field lands after the `keepalive` field, or a record on
  which neither check runs gains a byte.
  fixture: none in the tree. The pass builds a scratch repository under `%TEMP%` with a
  `.unattended.conf`, a build README pinning `asks:`, and a run-state file carrying a working phase, a
  witness, the `asks` fact, `lease-utc` and a `run-branch` naming the checked-out branch.
- **AC2** — When the fixture commits a README whose `asks:` line differs from the pinned fact,
  `--status` prints its one line carrying `asks moved at HEAD` with both values, and a no-id
  `--resume` over the same fixture prints `UNATTENDED check 73 FAILED`.
  Red when: the field is absent, or it prints while the resume does not refuse.
- **AC3** — When the fixture's main worktree is on another branch and a linked worktree added with
  `git worktree add` holds the run branch, `--status` from the main worktree carries
  `worktree not the run's` naming the linked worktree's path, and a no-id `--resume` there prints
  `UNATTENDED check 58 FAILED`; from the linked worktree the field is absent. With the `run-branch`
  and `branch-ref` lines deleted from the record it carries `worktree unanswerable`, and with
  `lease-utc` deleted it carries no worktree field.
  Red when: any of the four readings differs from what `--resume` would do on the same record.
- **AC4** — When `--status` runs over each fixture state of AC2 and AC3, `git status --porcelain` and
  `git hash-object` of the run-state file read the same before and after, the exit status is 0, and
  the output carries no `FAILED`.
  Red when: the report writes, stages, refuses or changes the verb's exit status.
- **AC5** — When `grep -c 'fail 73 ' tools/unattended/unattended.sh` and `grep -c 'fail 58 ' tools/unattended/unattended.sh`
  run, they print 1 and 5, their BASE counts, and `python tools/memory-tree/check-arms.py --report`
  still reads check 73 branch 1 and check 58 branch 1 ARMED.
  Red when: the extraction changed a refusal's text and disarmed its arm.
- **AC6** — When `grep -c -E "regrounding by the build method's|no-id spelling" memory/guides/UNATTENDED-STOPS.md`
  runs, it prints 0, where BASE prints 2; `grep -c "method's no-id spelling" tools/unattended/unattended.sh`
  prints 0, where BASE prints 1; the rewritten §8 paragraph names `--status` and both check numbers;
  `cmp tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md` exits 0; and
  `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: either carrier still ties regrounding to the no-id spelling, or the render differs.
- **AC7** — When `grep -c -E 'asks as pinned|asks moved at HEAD|worktree holds the run|worktree not the run|worktree unanswerable' tools/unattended/unattended.test.sh`
  runs, it prints at least 5, where BASE prints 0.
  Red when: a field has no arm.
  permission: running the suite is waived for this landing by the build README's rule; the arms are
  written and their run is not observed here.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: `tools/unattended/unattended.test.sh` · fixtures with a moved asks line, a wrong worktree, no run branch and no lease, each read by `--status` · none

## 8. Open questions

- **F1 — What does regrounding use, and what must it still see?** The owner ruled on this ask's parked
  decision: the build method's step regrounds with `--status`, extended to report the holder-worktree
  and pinned-asks checks read-only, in place of a no-id `--resume`. RESOLVED (owner, 2026-09-30): this
  unit extends `--status`, and unit 5 points the step at it.
- **F2 — Does a passing verdict print?** (a) Only a failing or unanswerable verdict prints, the
  verb's older field rule, so every passing line keeps its BASE bytes. (b) Each verdict prints on the
  records whose resume would run its check, pass included, and nothing prints where no check runs.
  (a) cannot be told from a verb that never asked, and it fails unit 5's AC5, which reads both
  verdicts on this run's own passing record; (b) costs the bytes of lease-carrying status lines and
  any suite arm comparing one with a literal. Recommendation (b). RESOLVED (agent, 2026-09-30,
  delegated): (b), the option satisfying more of the set's stated criteria, M3's rule, with the
  literal arms amended in the pass.

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, from the ask's accept clause, the owner's ruling and the
  build's spec brief.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "report a read-only verdict on the status line without
refusing"` ranked `read_text`, `report` and `read_conf`, all name-stem neighbours outside this kit, and
reported `.sh` as an unscanned layer. The seams were found by reading the driver and are reused rather
than copied: `resolve_holder_worktree`, which already writes and prints nothing; the comparison inside
`check_asks_pinned`, moved into `check_asks_moved` so check 73 and the report read one predicate; the
where-text inside `check_holder_worktree`, moved into `derive_holder_where` for the same reason; and
`verb_status`'s own field rule, which the stop-guard and orphan fields already follow.

Recall terms used: `status holder-worktree check-58 check-73 check_asks_pinned check_holder_worktree
resume matrix regrounding M7 read-only lease`.
