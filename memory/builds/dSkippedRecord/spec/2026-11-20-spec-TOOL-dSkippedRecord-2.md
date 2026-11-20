# TOOL-dSkippedRecord-2 — the `same` arm reads the skip line's commit hash, and the failed-stage modes are recorded as built

**Status:** CLOSED · rev-1 · 2026-11-20 · node d · Tier-2 · base 81657e77 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dSkippedRecord-2-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dSkippedRecord-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-20-prompt-TOOL-dSkippedRecord-2-promotion-brief.md](../prompts/2026-11-20-prompt-TOOL-dSkippedRecord-2-promotion-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 closing review of this build
(`reviews/2026-11-20-review-TOOL-dSkippedRecord-1-closing-diff-round1.md`) confirmed two LOW
defects, and the build method's severity rule batches both into this unit, per the promotion brief
(`prompts/2026-11-20-prompt-TOOL-dSkippedRecord-2-promotion-brief.md`). After it, the suite's
`same` arm reds when the skip line's trailing commit hash is blank or wrong. And this spec records
the failed-stage modes as they were built, a `git` shim on PATH, because unit 1's spec is CLOSED and
stays frozen with a description that does not match the code.

## 2. Scope (IN)

- **S1** — The review's item 1, finding 2. In region 8 of `tools/unattended/unattended.test.sh`,
  the `same` call of `run_render_helper` is followed by one line that reads the short hash of the
  commit that last changed `memory/builds/tRun/build/lu-record.md`, from the fixture repository the
  helper left. The prefix `hit` on `unattended: run record unchanged` becomes one `same` assertion
  over the whole skip line, ending in that hash, with `unread` standing in for an empty read. The
  block's comment gains the lines §4 gives. Observed by AC1, AC2 and AC3.
- **S2** — The suite edit stays inside that block. `run_render_helper` keeps its bytes, and the
  suite defines no new shell function, so the lexicon's function and verb pins do not move. Observed
  by AC4.
- **S3** — The review's item 2, finding 3. This spec's §4 states the failed-stage mechanism as
  built by red fix 26f99cdb0, and its §9 rev-1 entry names the correction to unit 1's suite-arm
  design and that red fix. Unit 1's spec is not edited. Observed by AC5 and AC6.

## 3. Non-goals (OUT)

- No change to `tools/unattended/unattended.sh`. The skip line and its `GIT log` substitution stay
  as unit 1 built them.
- No edit to `TOOL-dSkippedRecord-1`'s CLOSED spec, its §4 table included. Item 2 is corrected
  here alone, as `TOOL-dSettledStage-4` corrected its frozen sibling.
- No new shell function in the suite, and no change to `run_render_helper`'s output. Red fix
  26f99cdb0 exists because two new definitions broke both lexicon pins.
- No change to the `moved`, `addfail` or `difffail` arms, nor to the two no-mode calls.
- No `memory/gotchas/` entry for the review's two left-shift classes. Item 1's left-shift is this
  arm, and item 2's is a record correction the review grades LOW. A class entry is a separate
  document, so a separate unit (M2), for the owner to ask for.
- No unattended `--selftests` run, per the brief. The arm is observed through the hermetic probe
  unit 1's acceptance ledger records.

### Edges

none

## 4. Design

### Evidence, read at `922413ff1` on 2026-11-20

`tools/` is unchanged between unit 1's closing commit `e56a3e698` and `922413ff1`, and
`tools/unattended/unattended.test.sh` is blob `3d57b113` at both. The driver is blob `acd06237`.

The skip line is `tools/unattended/unattended.sh@acd06237009f:16597`. It ends
`the record was last committed at $(GIT log -1 --format=%h -- "$rec" 2>/dev/null)`, and `$rec` is
`memory/builds/tRun/build/lu-record.md` in the helper, parsed from the runlog stub's stdout
(`tools/unattended/unattended.sh#write_run_record`). The `2>/dev/null` means a failed read, or a
`$rec` naming a path no commit touched, ends the line in a blank `at ` with no error.

The `same` arm is `tools/unattended/unattended.test.sh@3d57b113b5f1:17236` to `:17239`. It asserts
the prefix `unattended: run record unchanged`, then `HEAD: same`, then the absence of
`its commit failed`. Nothing reads the hash, which is the review's item 1.

In mode `same`, the helper writes `lu-record.md` before `fixture`, so `fixture` commits it, and the
render stub writes nothing. The helper runs inside the arm's `$( … )`, but `reset_tree` and
`fixture` act on the repository in the suite's working directory
(`tools/unattended/unattended.test.sh#reset_tree`, `tools/unattended/unattended.test.sh#fixture`).
So after the helper returns, that repository's HEAD is the `fixture` commit, which `HEAD: same`
asserts, and it is the commit that last changed the record.

### S1 — the arm as built

The block becomes this. The three AC1 comment lines above it stay, and the `moved`, `addfail` and
`difffail` calls below it do not change.

```bash
# ---- TOOL-dSkippedRecord-2: the skip line is read whole, its hash the one `fixture` committed the
# ---- record at, read after the helper returns from the repository it left. An empty read stands as
# ---- `unread`, so a blank hash in the line cannot meet a blank read. Staged red by deleting the
# ---- driver's `GIT log` substitution from the skip line, or by pointing it at another path.
out=$(run_render_helper "" write_run_record same)
lu_hash=$(git log -1 --format=%h -- memory/builds/tRun/build/lu-record.md)
same "the skip line" "$(printf '%s\n' "$out" | grep '^unattended: run record unchanged')" \
  "unattended: run record unchanged — re-rendering it staged no change, so no commit was made; the record was last committed at ${lu_hash:-unread}"
hit  "$out" "HEAD: same"
miss "$out" "its commit failed"
```

`same` is the suite's exact-equality assertion (`tools/unattended/unattended.test.sh#same`), so the
line's end is pinned: a hash with trailing text, or a blank, is a mismatch. The `same` call replaces
the prefix `hit` one for one, so the assertion count does not move. The expected text is the
driver's own line, copied byte for byte, em dash included.

**The fallback is the arm's liveness.** Without `${lu_hash:-unread}`, a read that came back empty
would build an expected line ending `at `, and a driver whose substitution came back blank would
match it. With it, an empty read builds a line no driver prints. That is the class
`memory/gotchas/fixture-passes-by-finding-nothing.md` names.

**Each break edits the driver's own substitution.** Deleting it blanks the hash. Pointing its path
at `README`, which the probe's base commit commits and `fixture` never touches, prints a real hash
of the wrong commit. Neither break stands in a synthetic value for the shipped one
(`memory/gotchas/staged-break-substitutes-a-synthetic-value.md`).

### S3 — the failed-stage modes as built

This table states what red fix 26f99cdb0 built, read at
`tools/unattended/unattended.test.sh@3d57b113b5f1:17206` to `:17213`. Unit 1's §4 mode table
describes these two modes through two shell function definitions named `GIT`, which were never
landed in that form.

| Mode | Fixture | Expected |
|---|---|---|
| `addfail` | as `moved`, and a `git` shim first on PATH that exits 1 for an argv beginning `-c <pin> -c <pin> add -A` | "git could not stage what the index render moved: memory/LIVE.md"; `HEAD: same` |
| `difffail` | as `moved`, and the same shim exiting 128 for exactly `-c <pin> -c <pin> diff --cached --quiet` | the refusal line naming `exited 128`; `HEAD: same` |

The mechanism, in the helper's subshell, under `case "$lu_mode" in addfail|difffail)`:

1. `printf` writes one script to `$lu_g/lu-shim/git`, where `$lu_g` is the fixture's absolute git
   dir. Its `case` word is the mode followed by the argv, so one shim text serves both modes and
   each mode matches only its own call. The two `<pin>` slots are `$GIT_PIN_REPLACE` and
   `$GIT_PIN_GRAFTADV`, the pins the driver's `GIT` wrapper passes
   (`tools/unattended/lib-unattended.sh#GIT`).
2. Every other call reaches `exec` of the real git, whose path `command -v git` read before PATH
   moved. So `scan_dirty_paths`'s `diff --cached --name-only`, the stages before the failed one and
   the `rev-parse` the helper runs after the call all reach git.
3. The directory goes first on PATH spelled `$(cd "$lu_g/lu-shim" && pwd)`, the shell's own form.
   `git rev-parse --absolute-git-dir` prints `C:/...` on Windows, and that colon splits PATH.

The shape follows the tw5 arm's shim (`tools/unattended/unattended.test.sh@3d57b113b5f1:8471`).
The function-definition form was refused by two legs, which the red-fix records under
`memory/builds/dSkippedRecord/build/` carry: `lexicon naming predicates` read the `sh.function.conv`
count over its pin, and `lexicon wiring` read the verb offenders over theirs. The suite's own comment
at `:17205` states that reason.

### Order

**Order 2**, after `TOOL-dSkippedRecord-1`'s order 1. That unit is CLOSED and its code is in the
tree this unit reads. No criterion here rests on work another live unit builds, so §3 declares no
edge, and order is not one.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `lu_hash` | suite variable in region 8's main body | none, a variable | nothing |
| `the skip line` | the `same` assertion's label | none | the suite's `same` failure line |

No function, verb, flag, conf key or refusal number is minted.

### Files touched (estimate)

`tools/unattended/unattended.test.sh` · `memory/builds/dSkippedRecord/build/`

The second is the unit's acceptance ledger, carrying `**Serves:** journal TOOL-dSkippedRecord-2`.
`memory/guides/SESSION-KICKOFF.md`'s `watch:` line names neither, so no manifest re-stamp is owed.
No Python function moves, and the code map records suite functions by name and file, so no
`gen_map.py --write` is owed.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| The helper prints the expected hash beside its `HEAD:` line, the review's second fix | It changes the helper's output for every mode and both no-mode calls, where S2 keeps the helper's bytes. The repository the helper leaves already answers the question after it returns. |
| A second `hit` on `last committed at $lu_hash`, beside the prefix `hit` | `hit` is a substring match, so a hash with trailing text passes, and an empty `$lu_hash` passes over a blank line. |
| `git rev-parse --short HEAD` as the expected hash | It names HEAD, not the commit that last changed the record. It agrees in this fixture only because `fixture` is HEAD, and it reads a different fact from the driver's. |
| A new suite function that reads the hash | The brief's non-goal: the lexicon pins the count of function definitions, and red fix 26f99cdb0 is that refusal. |
| A rev-2 of unit 1's spec rewriting its mode rows | Unit 1's spec is CLOSED, and a CLOSED spec stays frozen (M4). Its correction is this unit. |

## 5. Production-readiness checklist

- security: N/A — a suite assertion and a record. No write path, surface or input.
- perf / scale: one `git log -1` in the fixture repository per suite run.
- error / empty / loading states: an empty hash read is the `unread` fallback, which fails the arm
  with the suite's own `FAIL the skip line` message rather than passing.
- observability: the `same` failure line prints the expected and the actual skip line, hash
  included.
- risks: the expected line copies the driver's text, so a reworded skip line reds this arm. That is
  wanted: unit 1's S3 holds that line byte-identical, and the arm is where a change shows.
- testing: the probe readings of §6 and the arm §7 declares.
- migration: N/A — no stored data and no conf key.
- user docs: N/A — no page under `help/` documents the unattended suite or the skip line.

## 6. Acceptance criteria

`<p2>` is the product commit, named in the ledger. Commands run from the worktree root on node d.
`<t>` is a fresh directory under `%TEMP%`. `<probe>` is the script unit 1's acceptance ledger records
under "The probe, as run"
(`memory/builds/dSkippedRecord/build/2026-11-20-build-TOOL-dSkippedRecord-1-1-acceptance-ledger.md`),
saved under the session scratchpad, with two edits. After its own `hit` and `miss` it sets `n=0` and
evals the suite's three assertion definitions. And its `same)` case arm evals the suite's own block,
so mode `same` is graded by the suite's lines, as built at the revision `<suite>` names:

```bash
eval "$(grep -E '^(hit|miss|same)\(\)' "$TESTF")"
eval "$(sed -n '/^out=\$(run_render_helper "" write_run_record same)$/,/^miss "\$out" "its commit failed"$/p' "$TESTF")"
```

The three driver copies under `<t>` are made from `tools/unattended/unattended.sh` at `<p2>`:

```bash
d=tools/unattended/unattended.sh
cp "$d" <t>/built.sh
sed 's|$(GIT log -1 --format=%h -- "$rec" 2>/dev/null)||' "$d" > <t>/blank.sh
sed 's|$(GIT log -1 --format=%h -- "$rec" 2>/dev/null)|$(GIT log -1 --format=%h -- README 2>/dev/null)|' "$d" > <t>/readme.sh
```

`<helper-diff>` compares `run_render_helper`'s bytes at `922413ff1` with its bytes at `<p2>`:

```bash
s='/^run_render_helper()/,/^}/p'
diff <(git show 922413ff1:tools/unattended/unattended.test.sh | sed -n "$s") <(sed -n "$s" tools/unattended/unattended.test.sh)
```

- **AC1** — When `bash <probe> <t>/built.sh <suite> tools/unattended/lib-unattended.sh %TEMP%/<short-name>`
  runs with `<suite>` the suite at `<p2>`, it prints no `FAIL` line and `STATUS 0`. With
  `<t>/blank.sh` it prints `FAIL the skip line` and `STATUS 1`, and `grep -c 'last committed at "'`
  over `<t>/blank.sh` prints 1, so the break was made.
  Red when: `<suite>` is the suite at `922413ff1`, whose block asserts only the prefix, and the
  probe over `<t>/blank.sh` prints `STATUS 0`, the gap the review's item 1 names.
- **AC2** — When the same probe runs `<t>/readme.sh` with `<suite>` at `<p2>`, it prints
  `FAIL the skip line` and `STATUS 1`, and the actual line it prints ends in a hash that is not the
  expected one.
  Red when: the arm accepts any hash, such as a `grep -E 'at [0-9a-f]{7,}$'` over the line, and the
  probe over `<t>/readme.sh` prints `STATUS 0`.
- **AC3** — When `<suite>` is a copy of the suite at `<p2>` whose `lu_hash` read names
  `absent.md` in the record's directory, a path no commit touched, the probe over `<t>/blank.sh` prints `FAIL the skip line`,
  and the expected line it prints ends `at unread`.
  Red when: the fallback is written `$lu_hash` in that copy, so the empty read meets the blank line
  and the probe prints `STATUS 0`.
- **AC4** — When `<helper-diff>` runs at `<p2>`, it prints nothing. The count `grep -cE '^[[:space:]]*[A-Za-z_][A-Za-z0-9_]*\(\) *\{'`
  prints the same number over the suite at `922413ff1` and at `<p2>`, and AC1's probe passes the
  `moved`, `addfail`, `difffail` and no-mode lines.
  Red when: the hash is read through a new suite function, and the second count is one higher.
  figure: both counts DERIVED at observation; 291 PINNED at `922413ff1` on 2026-11-20.
- **AC5** — When `grep -ciE 'overrid[e]'` runs over this spec, it prints 0, and `grep -c 'lu-shim'`
  over it prints at least 1. `sed -n '/^## 9\./,/^## 10\./p'` over this spec, piped to
  `grep -c 26f99cdb0`, prints at least 1.
  Red when: the same `overrid[e]` grep over `TOOL-dSkippedRecord-1`'s spec prints 4, the stale
  description the review's item 2 names, PINNED at `922413ff1`.
- **AC6** — When `git diff --quiet 922413ff1 <p2> -- memory/builds/dSkippedRecord/spec/2026-11-20-spec-TOOL-dSkippedRecord-1.md`
  runs, it exits 0.
  Red when: unit 1's §4 rows are rewritten in place, and the diff exits 1. A change confined to its
  `gen:spec-records` region is the index generator's, not this unit's, and the ledger names it.

## 7. Gates

`lexicon naming predicates` · `lexicon wiring` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `writing practice (records and units)` · `positional (the citation check alone)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `harness arms (fail branches armed or pinned)` · `unattended kit gate` · `testsuite counts (every bar self-test prints one)` · `kit epoch (shipped bytes move, the version moves)`

The lexicon legs hold the suite's function and verb pins, which S2 keeps. The record, citation and
map legs cover the spec and the ledger, and the two recall-floor legs guard the build folder the
ledger lands in. The suite, arm, kit and count legs cover the edited suite.

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · region 8, the `same` call's whole-line assertion of the skip line; its failing case is staged by deleting the driver's `GIT log` substitution from the skip line, and by pointing it at `README` · none

The arm moves no floor: `tools/unattended/unattended.test.sh` pins no `SELFTEST_FLOOR`, and the
assertion count does not move. The main loop observes the arm red, then green, at the close, through
AC1's probe because the unattended suites are held, and runs the bar once after the last unit is
terminal.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, from the promotion brief and the owner's "land it". It
  disposes the round-1 closing review's two LOW items, findings 2 and 3. The review's item 2 is
  corrected here: `TOOL-dSkippedRecord-1` is CLOSED and frozen, and its §4 suite-arm design
  describes `addfail` and `difffail` through two shell function definitions named `GIT`. Red fix
  26f99cdb0 built them as one `git` shim on PATH instead, because those definitions broke the
  `lexicon naming predicates` and `lexicon wiring` pins. §4 states the shim as built.

## 10. Reuse audit

The seam extended is the `same` call of `run_render_helper` in region 8 of
`tools/unattended/unattended.test.sh`, with the suite's own `same` assertion
(`tools/unattended/unattended.test.sh#same`) and the repository the helper's `fixture` leaves. No
helper, function or fixture is added. Item 2 follows `TOOL-dSettledStage-4`, whose spec recorded a
correction to a frozen sibling in its own §7 and §9.

`python tools/codebase-map/reuse_lookup.py "assert a test output line ends with the commit hash a fixture computed"`
ranked name-stem neighbours: `fixture`, `run_fixture_git`, `write_commit`, `build_commit` and
`read_git_output`. None asserts an output line against a commit hash. `fixture` is the suite's own,
and this unit reads the commit it makes. So no existing seam fits beyond the arm itself, recorded as
a miss.

Recall returned the brief, the build README's roster row, the review's items and unit 1's spec and
ledger, which state the defects and the probe this unit reuses. It returned
`TOOL-aLevelledCopy-9`'s brief, which weighed a rev bump of a CLOSED spec against recording the
correction elsewhere for the pass-order history leg's reason; this unit records it here. The records
and the code agreed on every citation re-read, and no hit was stale.

The gotchas `tools/unattended/unattended.test.sh` selects, each answered: under
`fixture-passes-by-finding-nothing`, the `unread` fallback and AC3; under
`staged-break-substitutes-a-synthetic-value`, both breaks edit the driver's own substitution; under
`a-helper-extraction-blinds-a-per-function-rule`, no helper is extracted; under
`two-answers-to-one-question`, the expected line is the driver's copied text, and the arm is what
reds when the two drift.

Recall terms used: `python tools/memory-recall/query.py "how does a suite arm check the commit hash
a skip line names, and how is a frozen closed spec corrected" --terms "run_render_helper skip line
commit hash same arm write_run_record PATH git shim frozen sibling correction"`
