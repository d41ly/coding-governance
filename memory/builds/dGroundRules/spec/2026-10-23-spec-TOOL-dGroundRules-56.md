# TOOL-dGroundRules-56 — the row check observed refusing: the not-a-trap row run through the arm's own row function, never read off the table

**Status:** CLOSED · rev-2 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 18 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-56-deviation-44.md](../build/2026-10-23-build-TOOL-dGroundRules-56-deviation-44.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-56-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-56-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-53-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-task.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-57 |
| [2026-10-23-prompt-TOOL-dGroundRules-56-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-56-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-53-staleness-probe-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 |
| [2026-10-24-prompt-TOOL-dGroundRules-56-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-56-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-56-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-56-probe-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run, round 1
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`),
confirmed finding **id 14 at HIGH** under item **H1**, which it shares with ids 5, 9, 12 and 19.
Id 14 is H1 seen from verification. `TOOL-dGroundRules-44` S2 is the row check: before the arm
grades either rule, a `disjoint` row with no raw string prefix in either direction adds a
disagreement naming the row and the words `not a string-prefix trap` to the arm's one assertion,
which then fails. AC3 is the only criterion S2 names, and it runs `TRAP_PROBE`, which reads the
suite's table in Python. It never runs the check, so a build that skipped S2 entirely would still
pass it. This unit is id 14's promotion for the check itself: the row function
`check_overlap_pair` of `TOOL-dGroundRules-45` S1 is run alone on the staged non-trap row, with the
arm's one assertion after it, so the refusal is observed in the assertion the check feeds. It
observes `TOOL-dGroundRules-44` and `TOOL-dGroundRules-45`, both at order 14, so it builds after
them, at order 18.

## 2. Scope (IN)

- **S1** — The refusal is the function's own. Inside `check_overlap_pair`, the row function
  `TOOL-dGroundRules-45` S1 defines in the suite, the row check of `TOOL-dGroundRules-44` S2 adds
  its disagreement, naming both paths of the row and the words `not a string-prefix trap`, to the
  list the arm's one assertion names, and returns before either verdict check. It calls no `arm`
  and moves no counter. The call lines are followed by that one assertion and nothing else up to
  the suite's `total=` line. So the function and the assertion, run alone on a non-trap row, need
  nothing from the suite beyond `pass` and `fail`. Where the built suite places the row check
  outside the function, in a loop of its own or a line printed beside the assertion, this unit moves
  it into the function. Observed by AC1, AC2.
- **S2** — The refusal half of `TOOL-dGroundRules-44` AC3 restated. With `NOT_A_TRAP` of
  `TOOL-dGroundRules-44` §6 staged, `ROW_CHECK_RUN` (§4) prints the arm's one assertion failing,
  its line naming the staged row and the refusal words. Observed by AC1.
- **S3** — The check stays silent on a true trap. On the built tree, `ROW_CHECK_RUN` prints the
  arm's assertion line and no line carrying `not a string-prefix trap`. Observed by AC2.

## 3. Non-goals (OUT)

- The staging itself: `NOT_A_TRAP` is `TOOL-dGroundRules-44`'s. This unit runs the row function in
  the copy that staging leaves.
- Any change to the row check's predicate, to either verdict check, to either overlap rule or to
  the arm's one assertion and its FAIL line.
- Running the suite from a criterion. The suite runs at the close, through
  `TOOL-dGroundRules-44`'s `New arm:` line (§7).
- The class record for a criterion that reads its check's input: `TOOL-dGroundRules-55`.
- An edge to `TOOL-dGroundRules-45`, whose `check_overlap_pair` S1 reads. That spec carries no
  reciprocal line and this pass writes no other spec; its order, 14, puts it before this unit's.

### Edges

- **consumes-from** `TOOL-dGroundRules-44` — S2's row check and its refusal words, which S1 places in the row function, and `NOT_A_TRAP`, the staging S2 runs the row function in; without them there is no check to run and the function only ever sees a true trap

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 at 8eab342e0, from the repository root.

- `TOOL-dGroundRules-44` S2 (rev-5) says the row check adds a disagreement naming the row and the
  words `not a string-prefix trap` to the arm's one assertion, inside the arm's per-row read: the
  loop over `OVERLAP_PAIRS`, or `check_overlap_pair` should `TOOL-dGroundRules-45` build first. Its
  §4 says the check is plain string comparison that calls neither rule. Its §6 spells
  `NOT_A_TRAP`, the disjoint row respelled as two paths relative to `PFX` neither of which starts
  with the other, in whichever form the suite holds it.
- `TOOL-dGroundRules-45` S1 (rev-3) makes each row a `check_overlap_pair` call line; the function
  adds each disagreement to the list `TOOL-dGroundRules-40`'s one assertion names, calls no `arm`
  and moves no counter. Its §4 sketches the definition at column 0, closed by `}` at column 0, the
  row check at its head, and the call lines and the one assertion below it, and says the definition
  line is not matched by `^check_overlap_pair `.
- In `tools/check-spec-tokens.test.sh` the suite's helpers `scratch` and `arm` build a scratch
  repository and run the lint against it, `arm` counting into `pass` and `fail`; a row check that
  called `arm` would need the lint, a scratch repository and the suite's header.
- At 8eab342e0 the arm under the comment `TOOL-dGroundRules-32 S9, TOOL-dGroundRules-40` reads
  `OVERLAP_PAIRS` in a `while read` loop inside a subshell and holds no `check_overlap_pair`; its
  one assertion is the last block before the suite's `total=` line, its FAIL line naming every
  disagreement. `ROW_CHECK_RUN` printed nothing there.
- A copy of the suite, its arm replaced by a `check_overlap_pair` shaped as S1 states, the two call
  lines and that one assertion, was built in the session scratchpad. `ROW_CHECK_RUN` with `.`
  there printed one `arm FAIL` line naming `TOOL-dGroundRules-40` and the trap row's verdict-check
  disagreements, and no refusal. After `NOT_A_TRAP` it printed the one line below. With
  `NO_ROW_CHECK` also staged, no line carried the refusal words; with `FLIPPED` alone, the
  `arm FAIL` line named the trap row with them.

```text
arm FAIL  TOOL-dGroundRules-40 check_writes_intersect and overlaps give each OVERLAP_PAIRS row its expected answer — rows , [row policy/a.py policy/ab.py disjoint: not a string-prefix trap]
```

### The literal

It is spelled here, in §4, so no join over §6 reads it as a suite invocation or a path, and no sweep
can respell it. Run it from the repository root, with `ROOT` the tree under test: `.` for the built
tree, or the scratch copy's path. It evaluates the row function's definition, the suite's `disjoint`
call lines and the lines after the last call line up to the suite's `total=` line, which S1 makes
the arm's one assertion, and nothing else of the suite.

```text
ROW_CHECK_RUN = bash -c 'fail=0; pass=0; PY=python; PFX=tools/; s=$1/tools/check-spec-tokens.test.sh; eval "$(sed -n "/^check_overlap_pair() {/,/^}/p" $s)"; eval "$(grep "^check_overlap_pair .* disjoint\$" $s)"; eval "$(sed -n "/^check_overlap_pair /,/^total=/p" $s | grep -v "^check_overlap_pair ")"' _ ROOT
```

On the built tree the true trap row passes the row check and reaches the verdict checks. Outside
the suite's header `tools/memory-tree/design_lib.py` and `tools/unattended/lib-unattended.sh` are not resolved, so those checks
disagree and the assertion line fails naming them. AC2 reads only that the assertion line is
printed and that no line carries the refusal words, so those disagreements do not move it.

### Inventory

No identifier is minted. `check_overlap_pair` is `TOOL-dGroundRules-45`'s, and `ROW_CHECK_RUN` is
a literal label inside this spec.

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **The suite run in the copy, as the review's fix words it.** A criterion that runs a self-test
  suite is not an acceptance observation in this corpus (`memory/TEMPLATE-SPEC.md`, the direct
  check rule); the suite is named on a `New arm:` line and run at the close. The row function and
  the assertion, run alone, are the direct check.
- **The row check printing a line of its own and raising `fail`.** `TOOL-dGroundRules-44` S2 and
  `TOOL-dGroundRules-45` S1 keep the arm one assertion that names every disagreement; a second
  line and a second count would move the suite's assertion count for no new red case.
- **The row check moved into a function of its own.** `TOOL-dGroundRules-44` §4 keeps it inside the
  per-row read and mints no identifier, and the row function already isolates one row.
- **The table read again in Python, with the paths whole.** That is the side read id 14 finds: it
  certifies S2 without running it.

## 5. Production-readiness checklist

- security — N/A: a test suite's row function and a read-only probe of it.
- perf / scale — one shell start; the function runs once per `disjoint` row.
- error / empty / loading states — a suite with no row function makes the probe print nothing,
  which AC1 and AC2 red.
- observability — the assertion's FAIL line names the row and the reason.
- risks — moving the row check into the function changes no verdict and no assertion count.
- testing — AC1 and AC2.
- migration — none.
- user docs — N/A: a gov-only suite.

## 6. Acceptance criteria

Every command runs from the repository root. `ROW_CHECK_RUN` is spelled in §4 and takes the tree
under test as `ROOT`; `NOT_A_TRAP` is spelled in §6 of `TOOL-dGroundRules-44`. Both criteria need
`TOOL-dGroundRules-44` and `TOOL-dGroundRules-45` built: at HEAD 8eab342e0 the suite holds no
`check_overlap_pair` and `ROW_CHECK_RUN` prints nothing, so both are red there. Once those two are
built as their specs state, both are green before this unit, whose S1 is the move should they not
be; each names the staged break that reds it:

```text
SCRATCH      = a git clone of this repository under %TEMP%/gr56, checked out at the commit under test
NO_ROW_CHECK = in SCRATCH, the row check's lines deleted from check_overlap_pair
FLIPPED      = in SCRATCH, the row check's prefix test negated, so it refuses a row that is a trap
```

- **AC1** — When `NOT_A_TRAP` runs and `ROW_CHECK_RUN` runs with `ROOT` set to `SCRATCH`, it
  prints one line starting `arm FAIL` and naming `TOOL-dGroundRules-40` that carries both paths
  `NOT_A_TRAP` stages and `not a string-prefix trap`, and no other line carrying those words. The
  staged break is `NO_ROW_CHECK`, after which no line carries them.
  Red when: the row check is absent, prints its refusal on a line of its own, or sits outside the
  row function, so the function and the assertion run alone never fail naming the non-trap row.
- **AC2** — When `ROW_CHECK_RUN` runs with `ROOT` set to `.`, it prints one line starting `arm`
  and naming `TOOL-dGroundRules-40`, and no line carrying `not a string-prefix trap`. The staged
  break is `FLIPPED`, after which that line names the trap row with the refusal words.
  Red when: the row check refuses the true trap row, so the arm could never reach its verdict
  checks, or the probe prints no assertion line.

## 7. Gates

`spec-tokens self-test` · `memory hygiene`

The suite arm that stages the non-trap row and reds by name is `TOOL-dGroundRules-44`'s `New arm:`
line. This unit moves no arm and adds none.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 14 (HIGH, item H1) of the closing diff
  review round 1 for the row check it found unobserved, with `ROW_CHECK_RUN` run against a mock of
  the arm on 2026-10-23.
- rev-2 · 2026-10-24 · §1 S1 S2 S3 §3 §4 §5 §6 AC1 AC2 §9 §10 · disagreements, from a read-only
  probe of steps 15 to 20 at e1c7051cb, restated at 8eab342e0: S1 had the row check print its own
  line and raise `fail`, and AC1 read that line and a `fail=1` count, where `TOOL-dGroundRules-44`
  S2 and `TOOL-dGroundRules-45` S1 have it add a disagreement to the arm's one assertion and move
  no counter; S2 and AC1 ran in a staging of `TOOL-dGroundRules-57`, since retired WONTDO, with a
  consumes-from edge on it; AC2 printed `fail=0` and no refusal at HEAD, green with nothing built;
  §4 cited the suite's helpers and `run_arms` by line; the scratch copy's path sat in prose.
  Ruled: S1 and AC1 restated onto the one assertion, `ROW_CHECK_RUN` evaluating the function, the
  disjoint call lines and the assertion and AC1 reading its FAIL line; the staging is
  `TOOL-dGroundRules-44`'s `NOT_A_TRAP` and the edge to `TOOL-dGroundRules-57` is dropped; both
  criteria name `TOOL-dGroundRules-44` and `TOOL-dGroundRules-45` built as their precondition and
  their staged break; `scratch`, `arm` and `run_arms` cited by symbol; `ROW_CHECK_RUN` takes the
  tree as an argument so it runs from the repository root, and the scratch path moved into a fenced
  block; Evidence re-run at 8eab342e0 on a scratchpad copy of the suite.

## 10. Reuse audit

The seam extended is `check_overlap_pair`, the per-row function `TOOL-dGroundRules-45` S1 places in
`tools/check-spec-tokens.test.sh`, with `TOOL-dGroundRules-40`'s one assertion after it; the probe
runs both as built and adds nothing beside them. `python tools/codebase-map/reuse_lookup.py "run one
suite function alone on a staged row to observe the arm assertion it fails"` ranked `rows`, `row`,
`run`, `arm` and `fail`; `arm` is the suite's lint-running helper, and `run_arms` in
`tools/lib/lib-selftest.sh` runs every arm a suite declared, not one function on one row, so no
existing seam fits the probe itself. The recall probe returned `TOOL-dGroundRules-55` and
`TOOL-dGroundRules-44`, whose class record and row check this unit sits beside and observes; both
agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion that reads a fixture
instead of running the check repaired" --terms "acceptance criterion fixture side read never runs
check row function disjoint row disagreement one assertion overlap arm"`
