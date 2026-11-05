# TOOL-dFinishedRecord-2 — check 24's HELD exclusion gets its arm, and the roster row names the placement built

**Status:** SPECCED · rev-1 · 2026-11-05 · node d · Tier-1 · base 51912ffc · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-05-prompt-TOOL-dFinishedRecord-2-round1-fix-brief.md](../prompts/2026-11-05-prompt-TOOL-dFinishedRecord-2-round1-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's round 1 confirmed two lows against `TOOL-dFinishedRecord-1`. L1 is check 24's
exclusion of a HELD record under a hand-off code, which no arm observes. L2 is the build README's
roster row, which places check 24's call where the spec rejected it. The record is
`memory/builds/dFinishedRecord/reviews/2026-11-05-review-TOOL-dFinishedRecord-1-closing-diff-round1.md`.
This unit adds the missing arm, corrects the row, and writes each finding into the bug class that
names its shape. It is the one batched unit `memory/guides/BUILD-METHOD.md` M4 owes for the two lows.
The brief is `memory/builds/dFinishedRecord/prompts/2026-11-05-prompt-TOOL-dFinishedRecord-2-round1-fix-brief.md`.

## 2. Scope (IN)

"The suite" is `tools/unattended/check-unattended.test.sh`, and "the block" is its check 24
derived-LANDED block, opening at `tools/unattended/check-unattended.test.sh:4229`. Every "Observed by"
below names this spec's own criteria.

- **S1** — L1. Arm D goes after arm C in the block. tRos's record reads `phase: HELD` under
  `hold-code: owner-landing`, its commit is pushed to the fixture origin, and `ARCH-tRos-7` is added
  after it with no rescope row. The arm makes one `hit` of the EXCLUDED line naming the record and its
  landing commit, and one `miss` of `check 24 FAILED`. It then restores the origin to `$ANCHOR0`.
  Observed by AC1 and AC2.
- **S2** — The block's opening comment names arm D's HELD record beside the LANDING record of arms A
  to C. Observed by AC2.
- **S3** — `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` each rise by 2, the count of arm D's assertions.
  A `RAISED` comment line naming this unit is added in the house shape, below unit 1's line. Observed
  by AC3.
- **S4** — L2. The Mechanism cell of the README's roster row for `TOOL-dFinishedRecord-1` says
  check 24 asks `check_derived_landed` after every skip, as check 23 does. Observed by AC4.
- **S5** — L1's left-shift. `memory/gotchas/observed-by-claim-no-arm-discharges.md` gains a final
  paragraph in its Where it bit section. Observed by AC5, AC6 and AC7.
- **S6** — L2's left-shift. `memory/gotchas/amendment-leaves-its-other-half-standing.md` gains a
  final paragraph in its Where it bit section, and the sentence in its anchors section that counts
  code surfaces now counts two. Observed by AC5, AC6 and AC7.
- **S7** — `memory/gotchas/INDEX.md` is re-rendered by `python tools/memory-tree/gotchas.py --write`,
  so the two rows' anchor counts match the edited records. Observed by AC7.
- **S8** — The pass changes no byte of the leg, its library or the driver. Arm D's red observation
  is the main loop's, on a staged break it restores. Observed by AC8.

## 3. Non-goals (OUT)

- **`tools/unattended/check-unattended.sh`**, which the review found correct. Check 24's call, its
  messages and header exception TWO do not move. The staged break in AC1 belongs to the main loop at
  the close, and it is restored before the bar.
- **`check_derived_landed` and `read_landing_commit`**, including the HELD admission at
  `tools/unattended/check-unattended.sh:698`.
- **`TOOL-dFinishedRecord-1`'s spec**, which is CLOSED and stays as written. Its design text already
  says a HELD record under a hand-off code is excluded, and the arm is what was missing.
- **A re-review of the closing review's subject.** Round 1 is terminal for it under M4.
- **A control arm for a HELD record under another hold code.** That refusal is the predicate's. Check
  7's HELD arm at `tools/unattended/check-unattended.test.sh:6612` observes it, and this unit does not
  edit the predicate. Any caller break that skips every HELD record already reds arm D's `hit`.
- **The README's other prose and its generated regions.** The Build-level rules line that classifies
  one unit belongs to the main loop's README re-read at the close (M8). The `gen:` regions are the
  committer's index render.
- **A new gotcha class, a codebase-map claim, or a machine gate.** Both findings extend existing
  classes, so the `codebase-map coverage + freshness` leg the brief names for a new class is not owed.
- **A hand bump of the kit version.** The suite ships as `engine` (`tools/unattended/kit.toml:42`), so
  the kit epoch moves, and kit versions move through the lander's `mint`.
- **A help page.** No verb, flag, conf key or output changes.

## 4. Design

### Evidence

Read at the build branch's tip `a18457df` on 2026-11-05, which carries `TOOL-dFinishedRecord-1` as
built at `9feeafc6b`. The `base` field is `51912ffc`, the build's pinned BASE and the local default
branch, as in unit 1's spec. Line numbers are PINNED to that reading, and the builder finds each site
by its quoted text.

| Site | Where | What it holds today |
|---|---|---|
| check 24's phase skip | `tools/unattended/check-unattended.sh:4191` | skips `LANDED` and `ABORTED` only, so HELD reaches the call |
| check 24's call | `tools/unattended/check-unattended.sh:4201` | `check_derived_landed "$f"; rs_dl=$?`, after the build-README skip at line 4195 |
| the HELD admission | `tools/unattended/check-unattended.sh:698` | a HELD record whose `hold-code` is in `HOLD_CODES_HANDOFF` |
| the hand-off codes | `tools/unattended/unattended.sh:1187` | `HOLD_CODES_HANDOFF="owner-landing owner-decision"` |
| the block's comment | `tools/unattended/check-unattended.test.sh:4229` | six lines, naming only a LANDING record |
| arm C's restore, the block's close | `tools/unattended/check-unattended.test.sh:4271` and `:4272` | `symbolic-ref HEAD refs/heads/main`, then `reset_tree` |
| check 7's HELD arm | `tools/unattended/check-unattended.test.sh:6615` | `hold-code: owner-landing`, the code this arm copies |
| the floors | `tools/unattended/check-unattended.test.sh:7328` and `:7340` | `FLOOR_ASSERTIONS=1140`, `FLOOR_SHARD_8=215` |
| the roster cell | `memory/builds/dFinishedRecord/README.md:47` | "after its recorded-phase skip" |

`fact_of` reads only the `## Run facts` section (`tools/unattended/check-unattended.sh:1267`), and
`build` writes one `phase:` line there, so a `sed` that rewrites that line puts `hold-code` in the
section both `fact_of` and `read_landing_commit` read. For a HELD copy under a code in the list,
`read_landing_commit` (`tools/unattended/lib-unattended.sh:1689`) answers the last commit that wrote
the record. That commit is the hand-off commit, because `add_u7` touches only the README. The suite
carries no CR byte (`grep -c $'\r'` printed 0), so it is edited as text.

### The suite's edits

The block's first six lines become these. Only the fourth and fifth lines change in substance; the
last two re-wrap.

```bash
# ---- DERIVED LANDED IS NOT GRADED BY CHECK 24 EITHER (TOOL-dFinishedRecord-1): an in-place landing
# ---- leaves its record at LANDING, and a roster that grows after the landing owes a rescope row the
# ---- driver's --rescope refuses on a finished record. Each arm is tRos live with ARCH-tRos-1, its
# ---- record moved to LANDING, or in arm D to HELD under a hand-off code, then ARCH-tRos-7 added
# ---- AFTER the landing commit with no row - the dConvergedCharter shape. Each asserts only check
# ---- 24's strings, because a LANDING record also moves checks 7, 15 and 19.
```

Arm D goes between arm C's `git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/main` and the
block's closing `reset_tree`, so the block still closes on `reset_tree`:

```bash
# D: HELD under a hand-off code, pushed, so derived LANDED too. Check 24's call admits every phase the
# predicate admits there, and this is the arm a call narrowed to LANDING turns red
# (TOOL-dFinishedRecord-2, the closing review's L1). The code is check 7's HELD arm's.
seed_ros
sed -i 's/^phase: .*/phase: HELD\nhold-code: owner-landing/' memory/builds/tRos/RUN.md
git add -A && git commit -q -m "tRos hands off" --no-verify
c24_hold=$(git rev-parse HEAD)
git push -q -f origin HEAD:main
add_u7
git add -A && git commit -q -m "a unit added after the hand-off" --no-verify
out=$(run)
hit  "$out" "check 24 EXCLUDED memory/builds/tRos/RUN.md — derived LANDED: its landing commit $c24_hold"
miss "$out" "check 24 FAILED"
git push -q -f origin "$ANCHOR0":main
```

The `hit` names the landing commit, so it cannot pass on an EXCLUDED line for some other commit, and
it is the liveness half: a fixture the predicate did not admit prints no EXCLUDED line. The `miss`
is the verdict half. Arm D adds no `reset_tree` cycle beyond the one `seed_ros` runs, and region 8
declares no `MUT_EXPECTED` count: the only non-zero one is at line 2555, in another block.

The floor block gains this line directly below unit 1's `RAISED 1133 -> 1140` paragraph, and the
two values move from 1140 to 1142 and from 215 to 217:

```bash
# ---- RAISED 1140 -> 1142 by exactly the arms, TOOL-dFinishedRecord-2: check 24's derived-LANDED arm D
# ---- after arm C in region 8, one `hit` and one `miss`, so FLOOR_SHARD_8 carries the same +2 and the
# ---- other seven are untouched. COUNTED off the block's own lines; this pass runs no suite, and its
# ---- RED-first observation is the close's.
```

### The staged break the main loop observes

Arm D is red only against a call that no longer admits HELD. The main loop stages that break in
check 24's loop and never in the shared predicate. It replaces the line at
`tools/unattended/check-unattended.sh:4201` with:

```bash
  case "$ph" in LANDING) check_derived_landed "$f"; rs_dl=$? ;; *) rs_dl=1 ;; esac
```

`ph` is set at line 4191 in the same loop. Under the break, arm D prints
`FAIL missing: check 24 EXCLUDED memory/builds/tRos/RUN.md` and
`FAIL unexpected: check 24 FAILED`, while arms A to C stay green. That is why arm D, and no arm
before it, discriminates. The leg carries bare CR bytes inside awk regexes, so the break is applied
by a byte-preserving edit, never a text-mode read
(`memory/gotchas/text-mode-read-eats-a-bare-cr.md`). It is restored with
`git checkout -- tools/unattended/check-unattended.sh` before the bar.

### The README's edit

Row 1 of the authored `roster:units` table becomes:

```markdown
| 1 | `TOOL-dFinishedRecord-1` | check 24's roster loop asks `check_derived_landed` after every skip, its recorded phase and its build README, as check 23 does, and excludes a derived-LANDED record |
```

The new cell carries no pipe character (`memory/gotchas/pipe-in-a-code-span-splits-a-table-cell.md`).
Row 2 and every other line of the README stay as they are.

### The classes' edits

Each finding extends the class whose shape it already is. Neither needs a new record.

- **L1 goes to `memory/gotchas/observed-by-claim-no-arm-discharges.md`.** Unit 1's S1 excluded
  every record the predicate answers 0 for, and named AC1, AC2, AC4 and AC5 as its observers. None
  of them reads a HELD record. That is one behaviour on two admitted inputs, with the cited arms
  reading one of them. The class's last paragraph already says a conditional needs a fixture per
  branch, seen red against the collapsed branch.
- **L2 goes to `memory/gotchas/amendment-leaves-its-other-half-standing.md`.** The spec moved the
  call off the brief's placement and listed the brief's placement under Alternatives rejected. The
  README row, written from the brief at the build's opening, kept the old placement. That is a
  correct amendment with an uncorrected neighbour, the class's own words.

This paragraph is the new last paragraph of the Where it bit section of
`memory/gotchas/observed-by-claim-no-arm-discharges.md`, directly above `## The fix`:

```markdown
It bit again in `TOOL-dFinishedRecord-1`, whose S1 excluded from check 24 every record
`check_derived_landed` answers 0 for, at its call in `tools/unattended/check-unattended.sh`. The
predicate admits two phases there, LANDING and HELD under a hand-off code, and S1's three arms in
`tools/unattended/check-unattended.test.sh` all set LANDING, so a call narrowed to that phase left
the suite green (dFinishedRecord's closing review, round 1, L1). `TOOL-dFinishedRecord-2` added
arm D, a HELD record under `owner-landing`. The check: a call to a shared admission predicate needs
one arm per phase the predicate admits at that call, each red against the call narrowed to the others.
```

This paragraph is the new last paragraph of the Where it bit section of
`memory/gotchas/amendment-leaves-its-other-half-standing.md`, directly above `## The fix`. Its last
sentence is L2's left-shift, which the review states as a check for the close.

```markdown
It bit again in dFinishedRecord's closing diff review, 2026-11-05
(memory/builds/dFinishedRecord/reviews/2026-11-05-review-TOOL-dFinishedRecord-1-closing-diff-round1.md, L2).
The build README's roster row for `TOOL-dFinishedRecord-1` was written from the brief, which placed check 24's
call to `check_derived_landed` directly after the recorded-phase skip. The spec moved the call after every skip,
as check 23 asks it, and listed the brief's placement under Alternatives rejected. The code in
`tools/unattended/check-unattended.sh` followed the spec and the row kept the brief's words, so the next editor
of the call had two placements to follow. `TOOL-dFinishedRecord-2` rewrote the row. The check, at the close: no
roster Mechanism cell describes a design its unit's spec lists under Alternatives rejected.
```

In the same file's anchors section (`memory/gotchas/amendment-leaves-its-other-half-standing.md:141`),
this text:

```text
the review harness template named above, the one code surface where this class has been observed.
```

becomes:

```text
the review harness template named above and the unattended kit gate whose call a roster row misplaced, the two code surfaces where this class has been observed.
```

### Anchors and the index

An anchor is a backticked token carrying `/` or a known source extension
(`tools/memory-tree/gotchas.py:65`). The first paragraph adds two:
`tools/unattended/check-unattended.sh` and `tools/unattended/check-unattended.test.sh`. That moves
the class from 5 anchors to 7. The second paragraph adds `tools/unattended/check-unattended.sh`,
moving that class from 12 to 13. The review record's path stays unbackticked, as in the class's
dTrueNorth paragraph, so it is evidence rather than an anchor. Both full-path anchors select the
classes at the `path` tier for `--for-paths tools/unattended/check-unattended.sh`, which selects
neither today. `memory/gotchas/INDEX.md` renders each record's anchor count, and check 17 compares it
byte for byte, so the pass re-renders it with `python tools/memory-tree/gotchas.py --write`.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `c24_hold` | suite block local, absent from the suite today | not graded; no shell-variable cell is declared |

### Rollout

1. Edit the suite: S2's comment, then arm D, then S3's floor line and values.
2. Edit the README row, then the two classes, then run `python tools/memory-tree/gotchas.py --write`.
3. Verify in the pass with AC2 to AC8. The pass runs no gate leg and no suite.
4. Commit once with the unit id in the subject, staging only the five files below.
5. The main loop observes AC1 at the close: red under the staged break, green once it is restored.
   It records both in this unit's acceptance ledger under a `Pass: none` commit (M8).

### Files touched (estimate)

`tools/unattended/check-unattended.test.sh` · `memory/builds/dFinishedRecord/README.md` ·
`memory/gotchas/observed-by-claim-no-arm-discharges.md` ·
`memory/gotchas/amendment-leaves-its-other-half-standing.md` · `memory/gotchas/INDEX.md`

### Alternatives rejected

- **A new class for each finding.** Each class above already names its finding's shape, so a new
  record would hold one fact twice and owe a map claim.
- **Anchor the classes on the README or the suite alone.** The brief's AC3 asks the checklist for
  `tools/unattended/check-unattended.sh`, the file a next editor of the call touches. That editor is
  the one the review says the row would mislead, and the one a narrowed call would slip past.
- **Read the hand-off code from the driver inside the arm.** Check 7's HELD arm spells
  `owner-landing` too, and the suite's `HOLD_CODES_HANDOFF` mutation arms from line 5293 already red
  when the driver's list stops parsing. A rename of the code reds arm D beside check 7's arm, which
  is loud rather than silent.

## 5. Acceptance criteria

Run from the worktree root in one Bash shell with these names set:

```bash
S=tools/unattended/check-unattended.test.sh
B='/DERIVED LANDED IS NOT GRADED BY CHECK 24 EITHER/,/^# ---- check 23 (TOOL-dUnstalledConvoy-10)/p'
O=memory/gotchas/observed-by-claim-no-arm-discharges.md
A=memory/gotchas/amendment-leaves-its-other-half-standing.md
```

- **AC1** — When the suite's region 8 runs at the close, arm D's `out` carries
  `check 24 EXCLUDED memory/builds/tRos/RUN.md — derived LANDED: its landing commit` followed by
  the fixture's hand-off commit, and carries no `check 24 FAILED`.
  Red when: the staged break `case "$ph" in LANDING) ...` replaces the call at
  `tools/unattended/check-unattended.sh:4201`, so the HELD record is graded and fails 24 for
  `ARCH-tRos-7`, while arms A to C stay green.
  permission: the suite runs at the main loop's close, never in a unit pass.
  fixture: the suite's own `seed_ros` fixture and bare origin, and the fixture kit's
  `HOLD_CODES_HANDOFF`, which holds `owner-landing`; nothing in the tree is required.
- **AC2** — When `sed -n "$B" "$S" | grep -E '^(# [A-D]( \(control\))?:|reset_tree$)' | cut -c1-4`
  runs, it prints `# A:`, `# B `, `# C:`, `# D:` and `rese` in that order. Over the same range,
  `grep -cE '^(hit|miss|same) '` prints `9`, `grep -cF 'phase: HELD\nhold-code: owner-landing'`
  prints `1`, and `grep -c 'or in arm D to HELD under a hand-off code'` prints `1`. Then
  `bash -n "$S"` exits 0.
  Red when: arm D sits outside the block or after its closing `reset_tree`, the comment still names
  LANDING alone, or the arm carries other than two assertions. Today the first command prints no
  `# D:` line and the count is `7`.
  figure: 7 is PINNED at `a18457df`, and 9 is that plus arm D's two assertions as designed.
- **AC3** — When `grep -nE '^FLOOR_(ASSERTIONS|SHARD_8)=' "$S"` runs, it prints `1142` and `217`,
  and `grep -c 'RAISED 1140 -> 1142 by exactly the arms, TOOL-dFinishedRecord-2' "$S"` prints `1`.
  Red when: arm D lands and either floor stays at 1140 or 215, or rises by a count other than the
  block's two new assertions.
  figure: 1140 and 215 are PINNED at `a18457df`; the raise is DERIVED from AC2's count less 7.
- **AC4** — When `grep -c "after its recorded-phase skip" memory/builds/dFinishedRecord/README.md`
  runs, it prints `0`, and
  `grep -c "^| 1 | .TOOL-dFinishedRecord-1. | check 24's roster loop asks .check_derived_landed. after every skip, its recorded phase and its build README, as check 23 does" memory/builds/dFinishedRecord/README.md`
  prints `1`.
  Red when: the row keeps the brief's placement, where the first command prints `1` today, or the
  rewording lands on another row.
- **AC5** — When
  `python tools/memory-tree/gotchas.py --for-paths tools/unattended/check-unattended.sh | grep -cE '^- \[ \] (observed-by-claim-no-arm-discharges|amendment-leaves-its-other-half-standing) \(path\)'`
  runs, it prints `2`.
  Red when: a paragraph lands without its backticked full path, so the class is not selected for
  the leg. It prints `0` today.
- **AC6** — When `sed -n '/^## Where it bit/,/^## The fix/p' "$O" | grep -c 'TOOL-dFinishedRecord-1'`
  runs, it prints at least `1`, and the same command over `"$A"` prints at least `1`.
  `grep -c 'the two code surfaces where this class has been observed' "$A"` prints `1`, and
  `grep -c 'the one code surface where' "$A"` prints `0`.
  Red when: a paragraph sits outside Where it bit, or the anchors section still counts one code
  surface while the record anchors two. Each `TOOL-dFinishedRecord-1` count prints `0` today.
- **AC7** — When
  `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import gotchas as g; print(len(set(g.ANCHOR_RE.findall(open(sys.argv[1], encoding='utf-8').read().split('---', 2)[2]))))" "$O"`
  runs, it prints `7`, and with `"$A"` it prints `13`. Then
  `grep -c '^| \[observed-by-claim-no-arm-discharges\][^|]* | class | 7 |' memory/gotchas/INDEX.md`
  and
  `grep -c '^| \[amendment-leaves-its-other-half-standing\][^|]* | class | 13 |' memory/gotchas/INDEX.md`
  each print `1`, and `git diff --numstat a18457df -- memory/gotchas/INDEX.md` prints 2 added and
  2 deleted.
  Red when: the index is not re-rendered, so its rows still read 5 and 12, or a paragraph adds a
  backticked path beyond the ones designed.
  figure: 5 and 12 are PINNED at `a18457df` on 2026-11-05; 7 and 13 are DERIVED from the designed
  text.
- **AC8** — When
  `git diff --stat a18457df -- tools/unattended/check-unattended.sh tools/unattended/lib-unattended.sh tools/unattended/unattended.sh`
  runs at the pass's commit, it prints nothing.
  Red when: the pass edits the leg, the predicate's library or the driver, or commits AC1's staged
  break.

## 6. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/check-unattended.test.sh · covers AC1 · arm D after arm C in check 24's derived-LANDED block in region 8, red on the staged break narrowing check 24's call to LANDING and green once it is restored · FLOOR_ASSERTIONS and FLOOR_SHARD_8, each +2

The suite is not a manifest leg: it ships as `engine` and its leg is withheld
(`tools/unattended/kit.toml:42`). It runs at the close, after the last unit is terminal, as its eight
shards, with region 8 in shard 8, and unsharded for the floor. The full bar runs at the landing.
`recall floor` and `recall floor arms` are owed because the `memory/` paths in Files touched trip the
guard those two legs carry. `memory hygiene` holds the gotcha index (check 17) and this spec.
`kit epoch` and `kit version markers` hold the moved shipped bytes, minted by the lander. The brief's
`codebase-map coverage + freshness` leg is owed only for a new class, and this unit adds none.

What no leg checks: that a roster Mechanism cell matches the code. AC4 observes this row once, and
the class's close-time check is the only standing guard.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-05 · initial draft, from the round-1 fix brief, the closing review's L1 and L2, the
  suite, leg and kit library read at the build tip `a18457df`, and the two classes' records.

## 9. Reuse audit

`python tools/codebase-map/reuse_lookup.py "regression arm for a held record under a hand-off code
excluded as derived landed by a gate check"` scanned every present layer and returned name-stem
neighbours only, such as `check`, `arm`, `records` and `check_landed_facts_due`. None of them builds
a check 24 fixture. The seam was read directly. This unit extends arms A to C of check 24's
derived-LANDED block in `tools/unattended/check-unattended.test.sh`, copying their `seed_ros`,
push and restore shape, and takes the hand-off code from check 7's HELD arm in the same suite. The
record shape is `TOOL-dEasedEffort-2`'s, as the brief names. The left-shifts extend
`memory/gotchas/observed-by-claim-no-arm-discharges.md` and
`memory/gotchas/amendment-leaves-its-other-half-standing.md`. `python tools/memory-tree/gotchas.py
--for-paths tools/unattended/check-unattended.sh` selects neither class today, which is what AC5
measures. The asks probe in M5 was not run, because this stage may not run the build-index
generator.

The recall probe returned the review record and the brief, `TOOL-dUnstuckLanding-14`'s spec and
acceptance ledger, which introduced the HELD admission, and `TOOL-dUnstuckLanding-4`'s backlog row.
The records and the source disagreed on one point. The review cites check 7's HELD arm at test
line ~6614, and the arm's `write_lg_record` line is at 6615 at `a18457df`, under its comment at 6612.
The code was taken over the record.

Recall terms used: check 24 derived LANDED HELD hold-code hand-off arm roster Mechanism Alternatives rejected gotcha

The question passed with them: "which arm proves check 24 excludes a HELD record under a hand-off
code, and which bug class names a roster cell describing a rejected placement".
