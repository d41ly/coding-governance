# TOOL-dGroundRules-56 — the row check observed refusing: the not-a-trap row run through the arm's own row function, never read off the table

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-56-deviation-44.md](../build/2026-10-23-build-TOOL-dGroundRules-56-deviation-44.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-53-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-task.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-57 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run, round 1
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`),
confirmed finding **id 14 at HIGH** under item **H1**, which it shares with ids 5, 9, 12 and 19.
Id 14 is H1 seen from verification. `TOOL-dGroundRules-44` S2 is the row check: before the arm
grades either rule, a `disjoint` row with no raw string prefix in either direction fails the arm by
name. AC3 is the only criterion S2 names, and it only reads the suite's table in Python. It never
runs the check, so a build that skipped S2 entirely would still pass it. Its stripped staging is
`TOOL-dGroundRules-57`'s. This unit is id 14's promotion for the check itself: the row check's
refusal is printed by the arm's own row function, and that function is run alone on the staged
non-trap row, so the refusal is observed where the check runs. It repairs `TOOL-dGroundRules-44`,
which sits at order 14, and runs in the copy `TOOL-dGroundRules-57` stages at order 17, so it builds
at order 18.

## 2. Scope (IN)

- **S1** — The refusal is the function's own. Inside `check_overlap_pair`, the row function
  `TOOL-dGroundRules-45` S1 defines in the suite, the row check of `TOOL-dGroundRules-44` S2 prints
  its failure line itself, naming both paths of the row and the words `not a string-prefix trap`. It
  raises the suite's `fail` counter and returns before either verdict check. So the function, run
  alone on a non-trap row, needs nothing from the suite beyond `fail`. Where the built suite prints
  that line through a helper defined outside the function, this unit moves the line into the
  function. Observed by AC1, AC2.
- **S2** — The refusal half of `TOOL-dGroundRules-44` AC3 restated. In the copy
  `NOT_A_TRAP_WHOLE` of `TOOL-dGroundRules-57` stages, `ROW_CHECK_RUN` (§4) prints the refusal line
  naming the staged row and then `fail=1`. Observed by AC1.
- **S3** — The check stays silent on a true trap. On the built tree, `ROW_CHECK_RUN` prints no line
  carrying `not a string-prefix trap`. Observed by AC2.

## 3. Non-goals (OUT)

- The staging itself and `TRAP_PROBE`'s line: `TOOL-dGroundRules-57`. This unit reads the copy
  that unit leaves.
- Any change to the row check's predicate, to either verdict check or to either overlap rule.
- Running the suite from a criterion. The suite runs at the close, through
  `TOOL-dGroundRules-44`'s `New arm:` line (§7).
- The class record for a criterion that reads its check's input: `TOOL-dGroundRules-55`.
- An edge to `TOOL-dGroundRules-45`, whose `check_overlap_pair` S1 reads. That spec is under another
  writer's edit in this disposal, so its reciprocal line cannot be written here; its order, 14, puts
  it before this unit's.

### Edges

- **consumes-from** `TOOL-dGroundRules-44` — S2's row check and its refusal words, which S1 places in the row function and S2 observes; without them there is no check to run
- **consumes-from** `TOOL-dGroundRules-57` — `NOT_A_TRAP_WHOLE`, the staged copy S2 runs the row function in; without it the function only ever sees a true trap

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `7810198ad`.

- `TOOL-dGroundRules-44` S2 says the row check fails the arm "with a line naming the row and the
  words `not a string-prefix trap`", and its §4 says the check is plain string comparison that
  calls neither rule. It does not say which code prints the line.
- `TOOL-dGroundRules-45` §4 sketches `check_overlap_pair() {` at column 0, closed by `}` at column
  0, with the call lines below it, and says the definition line is not matched by
  `^check_overlap_pair `.
- `tools/check-spec-tokens.test.sh:199-243` holds the suite's `scratch` and `arm` helpers; `arm`
  runs the lint and counts into `pass` and `fail`, so a row check that called it would need the
  lint, a scratch repository and the suite's header.
- A mock suite holding a `check_overlap_pair` shaped as S1 states, with the two call lines of
  `TOOL-dGroundRules-45` §4, was built in the session scratchpad. `ROW_CHECK_RUN` printed `fail=0`
  and no refusal there. After `NOT_A_TRAP_WHOLE` it printed
  `arm FAIL  overlap row tools/policy/a.py tools/policy/ab.py — not a string-prefix trap` and
  `fail=1`.

### The literal

It is spelled here, in §4, so no join over §6 reads it as a suite invocation or a path, and no sweep
can respell it. Run it verbatim from the root of the tree or the copy under test. It evaluates the
row function's definition and the suite's `disjoint` call lines, and nothing else of the suite.

```text
ROW_CHECK_RUN = bash -c 'fail=0; pass=0; PY=python; eval "$(sed -n "/^check_overlap_pair() {/,/^}/p" tools/check-spec-tokens.test.sh)"; eval "$(grep "^check_overlap_pair .* disjoint\$" tools/check-spec-tokens.test.sh)"; echo "fail=$fail"'
```

On the built tree the true trap row passes the row check and reaches the verdict checks, which may
print lines of their own outside the suite's header. AC2 reads only the absence of the refusal
words, so those lines do not move it.

### Inventory

No identifier is minted. `check_overlap_pair` is `TOOL-dGroundRules-45`'s, and `ROW_CHECK_RUN` is
a literal label inside this spec.

### Files touched (estimate)

- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **The suite run in the copy, as the review's fix words it.** A criterion that runs a self-test
  suite is not an acceptance observation in this corpus (`memory/TEMPLATE-SPEC.md`, the direct
  check rule); the suite is named on a `New arm:` line and run at the close. The row function, run
  alone, is the direct check.
- **The row check moved into a function of its own.** `TOOL-dGroundRules-44` §4 keeps it inside the
  row loop and mints no identifier, and the row function already isolates one row.
- **The table read again in Python, with the paths whole.** That is the side read id 14 finds: it
  certifies S2 without running it.

## 5. Production-readiness checklist

- security — N/A: a test suite's row function and a read-only probe of it.
- perf / scale — one shell start; the function runs once per `disjoint` row.
- error / empty / loading states — a suite with no row function makes the probe print `fail=0` and
  no refusal, which AC1 reds.
- observability — the refusal line names the row and the reason.
- risks — moving the line into the function changes no verdict and no assertion count.
- testing — AC1 and AC2.
- migration — none.
- user docs — N/A: a gov-only suite.

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. A scratch copy is a git clone
of this repository under `%TEMP%/gr56`, checked out at the commit under test. `ROW_CHECK_RUN` is
spelled in §4; `NOT_A_TRAP_WHOLE` is spelled in §4 of `TOOL-dGroundRules-57`.

- **AC1** — When `NOT_A_TRAP_WHOLE` runs in the scratch copy and `ROW_CHECK_RUN` runs there, it
  prints one line carrying `not a string-prefix trap` and both staged paths, then `fail=1`.
  Red when: the row check is absent, silent, or prints its refusal through code outside the row
  function, so the function run alone never refuses the non-trap row.
- **AC2** — When `ROW_CHECK_RUN` runs on the built tree, it prints no line carrying
  `not a string-prefix trap`.
  Red when: the row check refuses the true trap row, so the arm could never reach its verdict
  checks.

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

## 10. Reuse audit

The seam extended is `check_overlap_pair`, the per-row function `TOOL-dGroundRules-45` S1 places in
`tools/check-spec-tokens.test.sh`; the probe runs it as built and adds nothing beside it.
`python tools/codebase-map/reuse_lookup.py "run one suite function alone on a staged row to observe
its refusal line"` ranked `rows`, `row`, `run` and `run_arms`; `run_arms` (`tools/lib/lib-selftest.sh:201`)
runs every arm a suite declared, not one function on one row, so no existing seam fits the probe itself.
The recall probe returned `TOOL-dGroundRules-45` and `TOOL-dGroundRules-44`, whose row function and
row check this unit observes, and `TOOL-dGroundRules-42` and `TOOL-dGroundRules-47`; all agree with
source.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion that reads a fixture
instead of running the check repaired" --terms "acceptance criterion fixture side read never runs
check stripped literal respelled trap row overlap arm suite function"`
