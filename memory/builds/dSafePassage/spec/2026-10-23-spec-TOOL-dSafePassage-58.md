# TOOL-dSafePassage-58 — the spec audit of units 51 and 52, its ten minors on TOOL-52: the arm probe staged, the placement anchored on the block's `fi`, the abort's real exit, and the render's four outputs

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-58-deviation-104.md](../build/2026-10-23-build-TOOL-dSafePassage-58-deviation-104.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 51 and 52
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md`)
exited BOUNDED with 22 minors. BUILD-METHOD M4 batches them, and they split into two disjoint write
sets by M6's clauses. `TOOL-dSafePassage-59` batches the 12 that land on TOOL-dSafePassage-51, whose
writes are the step module. This unit batches the other ten, 5 MEDIUM and 5 LOW, all on
TOOL-dSafePassage-52, whose writes are the lander's suite and the spec template. Each is named by its
report id and is its own scope item, including where the report merged ids into one item.

All ten land on TOOL-dSafePassage-52, so this unit repairs that unit and builds one above it, at
order 14. Where a minor would bite TOOL-dSafePassage-52's pass, that unit's own §3 hands-off bullet
to this unit names it, so that pass may build it.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M2 | MEDIUM | 9, 14, 27 | S1, S2, S3 |
| M4 | MEDIUM | 15, 28 | S4, S5 |
| L3 | LOW | 10 | S6 |
| L4 | LOW | 11, 20, 26 | S7, S8, S9 |
| L8 | LOW | 21 | S10 |

That is 5 MEDIUM and 5 LOW findings by raw id. Item M2 shares its defect with id 3 at HIGH, item
H2, whose promotion `TOOL-dSafePassage-57` writes the probe that reads the arm. S1 to S3 add what
each of ids 9, 14 and 27 asks beyond it. The skeptic re-graded id 10 from medium to low, id 14 from
high to medium and id 26 from medium to low. It REJECTED the finders' fixes of ids 9 and 27, so S1
and S3 are built from the skeptics' corrected fixes.

## 2. Scope (IN)

### The arm probe, staged (M2)

- **S1** — id 9, the skeptic's corrected fix. The condition TOOL-dSafePassage-52 AC1 evaluates is
  the suite's own `if` line spelling `check-arms.py`, with `if ` and `; then` stripped, never a guard
  the criterion types. `TOOL-dSafePassage-57`'s probe is that form. Over a suite copy whose guard
  tests `check-arm.py`, a file absent in gov's tree, the probe prints no `ok-branch`. So the real arm
  testing the wrong file turns the criterion red. Observed by AC1.
- **S2** — id 14. The arm's skip line names the arm, as TOOL-dSafePassage-46 §4 "The arm's locator"
  writes it: `skip — <arm> no memory-tree kit beside this lander, so the derived-count arm did not run`.
  So the close's run of the suite in gov's own tree can assert that no `skip —` line spells
  `derived-count arm`, which tells the arm's skip from the 28-32 block's. TOOL-dSafePassage-50's
  `New arm:` line is read with that assertion. Observed by AC2.
- **S3** — id 27, the skeptic's corrected fix. `_mt_rc` reaching the suite from the environment
  cannot green the abort half. Both halves of `TOOL-dSafePassage-57`'s probe run under
  `env -u _mt_rc`, and the close's staged break runs the suite copy with the arm block above the
  `^_mt_rc=` line under `env -u _mt_rc`. That run prints `_mt_rc: unbound variable`, exits non-zero
  and prints no `push-main.test: all cases ok`. Observed by AC3.

### The arm's place, anchored on its target (M4)

- **S4** — id 15. TOOL-dSafePassage-52 AC2 is read with §4 "The placement probe". The bound is the
  first `^fi$` after the `skip — 28-32` line, found by
  `awk '/skip — 28-32/{s=1} s&&/^fi$/{print NR; exit}'`, not the skip line itself. The first
  `check-arms.py` line must be greater than the scan line and that `fi`, and smaller than the final
  `[ "$fail" = 0 ]` line. Observed by AC4.
- **S5** — id 28. The probe fails loudly when an anchor is absent. A suite with no scan line, no
  `skip — 28-32` line, no `fi` after it or no final line prints `no anchor` with the four values and
  exits 1, so an edit to the skip message cannot make the criterion vacuous. Observed by AC5.

### The abort's real exit (L3)

- **S6** — id 10. TOOL-dSafePassage-52 S1 is read with the exit the suite really has. Run as
  `bash <file>`, which `tools/gate-legs.json:664` does, an unbound read under `set -u` prints
  `<file>: line N: _mt_rc: unbound variable`, exits 1 and prints no `push-main.test:` final line. The
  127 TOOL-dSafePassage-52 S1 quotes is the `bash -c` form's code alone. So the staged break's red is
  the missing final line and the `unbound variable` text, never an exit code, since FAILURES also
  exits 1. Observed by AC6.

### The render's four outputs (L4)

- **S7** — id 11. TOOL-dSafePassage-52 S4, its Files touched and its Rollout are read with the four
  live copies `tools/memory-tree/kit-dogfood-parity.test.sh --render` writes, the `PAIRS` of its line
  61: `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md` and
  `memory/guides/ANNOTATION-STYLE.md`. Its M6 disjointness claim is read over all four. Observed by
  AC7.
- **S8** — id 20. After the render, `git diff --name-only` must list `memory/TEMPLATE-SPEC.md` alone
  among the four. Any other of the three it lists is restored from HEAD with `git checkout --` before
  the commit, and the pass records that it was restored. Observed by AC7.
- **S9** — id 26. A non-zero `--render` exit is a stop. The live copy is restored from HEAD, never
  committed, and TOOL-dSafePassage-52's §5 error line is read with that sentence. NOT OBSERVED: a
  failure path no staged break of this build reaches; the `kit/dogfood doc parity` leg at the close
  grades a truncated live copy.

### The suite in Files touched (L8)

- **S10** — id 21. TOOL-dSafePassage-52 §7's "This unit adds no arm and moves none" is read as
  conditional. Where its AC2 finds the arm misplaced and its pass moves it, that pass carries
  `New arm: tools/push-main.test.sh · covers AC2 · ...`, and its leg line names
  `harness arms (fail branches armed or pinned)`. This unit's own §7 carries both. NOT OBSERVED: a
  reading of a gates section, which the close's arm observation carries.

## 3. Non-goals (OUT)

- Every step-module minor: `TOOL-dSafePassage-59`.
- The arm probe itself: `TOOL-dSafePassage-57`, id 3's promotion.
- Rewriting a built spec. An item that corrects a spec's text states the reading here.
- The report's left-shift gates and checklist entries.

### Edges

- **consumes-from** `TOOL-dSafePassage-52` — S1's failure mode, AC1, AC2's place, S4's render route, §5 and §7, which S1 to S10 read; without them there is nothing to stage or anchor
- **consumes-from** `TOOL-dSafePassage-57` — §4's arm probe, which S1 stages over a wrong-file guard and S3 runs with `_mt_rc` exported

## 4. Design

### The placement probe

```bash
f=tools/push-main.test.sh
s=$(grep -n -m1 '^_mt_rc=' "$f" | cut -d: -f1)
k=$(grep -n -m1 'skip — 28-32' "$f" | cut -d: -f1)
e=$(awk '/skip — 28-32/{s=1} s&&/^fi$/{print NR; exit}' "$f")
l=$(grep -n '^\[ "\$fail" = 0 \]' "$f" | tail -1 | cut -d: -f1)
a=$(grep -n -m1 'check-arms\.py' "$f" | cut -d: -f1)
[ -n "$s" ] && [ -n "$k" ] && [ -n "$e" ] && [ -n "$l" ] || { echo "no anchor: scan=$s skip=$k fi=$e final=$l"; exit 1; }
[ -n "$a" ] || { echo "no arm"; exit 1; }
[ "$a" -gt "$s" ] && [ "$a" -gt "$e" ] && [ "$a" -lt "$l" ] && { echo "placed: scan=$s fi=$e arm=$a final=$l"; exit 0; }
echo "misplaced: scan=$s fi=$e arm=$a final=$l"; exit 1
```

This unit ran it on node d, 2026-10-23, written to the run's scratchpad, over four suites:

| Suite | Output | Exit |
|---|---|---|
| `tools/push-main.test.sh` at this spec's commit | `no arm` | 1 |
| a copy with TOOL-dSafePassage-46's skeleton after the 28-32 `fi` | `placed: scan=873 fi=1047 arm=1048 final=1054` | 0 |
| a copy with the arm's guard between the skip echo and the `fi` | `misplaced: scan=873 fi=1048 arm=1047 final=1050` | 1 |
| the second copy with its skip message edited | `no anchor: scan=873 skip= fi= final=1054` | 1 |

Line numbers are PINNED to those copies; the probe derives each one by content.

### The abort, as the bar runs it

On the same node, a scratch file holding `set -u` and `if [ -n "$_mt_rc" ]; then echo ok; fi`, run
as `env -u _mt_rc bash <file>`, printed `<file>: line 2: _mt_rc: unbound variable`, printed no later
line and exited 1. `TOOL-dSafePassage-57` §4 measured 127 for the `bash -c` form.

### Inventory

Minted: none in the tree. Both probes are scratch files. No function, constant, conf key, gate leg,
plant or policy key.

### Migration

None.

### Rollout

Live at landing. It builds at order 14, one above TOOL-dSafePassage-52 (order 13), and after
`TOOL-dSafePassage-57` by the driver's id tie-break. Its write set is `tools/push-main.test.sh`, and
only where AC2 or AC4 finds the arm's skip line or place wrong. That set does not meet
TOOL-dSafePassage-51's, also at order 14. It shares the suite with `TOOL-dSafePassage-57`, so the
build run sequences the two by M6's first clause.

### Files touched (estimate)

- `tools/push-main.test.sh`

### Alternatives rejected

- **Requiring that no line between the skip echo and the `fi` spells `check-arms.py` (S4).** The
  report's second option. It bounds one gap and leaves the arm free to sit above the scan, which the
  first option's single comparison chain already catches.
- **Asserting exit 127 on the staged break (S6).** The suite runs as a file and exits 1 on the abort,
  the same code as FAILURES, so an exit code cannot tell the two apart.
- **Dropping `tools/push-main.test.sh` from TOOL-dSafePassage-52's Files touched (S10).** The report's
  first option. A misplacement AC2 finds would then belong to nobody until the close.

## 5. Production-readiness checklist

- security: N/A — probes over a test suite's text and a render's write set.
- perf / scale: one `grep` and one `awk` pass over the suite.
- error / empty / loading states: an absent anchor prints `no anchor` and exits 1, never a pass.
- observability: the placement probe prints every line number it compared.
- risks: none beyond TOOL-dSafePassage-52's.
- testing: the four suites of §4 and the criteria of §6.
- migration: none.
- user docs: N/A — no `help/` page covers the lander's suite, and `memory/TEMPLATE-SPEC.md` is the
  documentation S7 to S9 route.

## 6. Acceptance criteria

- **AC1** — When `TOOL-dSafePassage-57`'s probe runs with `f` set to a scratch copy of
  the lander suite tools/push-main.test.sh whose guard line spells `check-arm.py`, it prints no `ok-branch`.
  Red when: the probe evaluates a guard it typed, so the wrong file still reads `ok-branch`.
- **AC2** — When `grep -n 'skip — .*derived-count arm' tools/push-main.test.sh` runs, it prints one
  line, below the arm's guard line.
  Red when: the arm's skip line cannot be told from the 28-32 block's.
- **AC3** — When `TOOL-dSafePassage-57`'s probe runs from a shell that has exported `_mt_rc=memory-tree`,
  its abort half still prints `_mt_rc: unbound variable` and a non-zero `alone rc=` line.
  Red when: an exported `_mt_rc` reaches the probe and greens the abort half.
- **AC4** — When §4's placement probe runs over the lander suite tools/push-main.test.sh, it prints a `placed:` line
  and exits 0. Over a scratch copy with the arm's guard between the `skip — 28-32` echo and the `fi`,
  it prints `misplaced:` and exits 1.
  Red when: the bound is the skip line, so an arm inside the else-branch passes.
- **AC5** — When the same probe runs over a scratch copy whose `skip — 28-32` message is edited, it
  prints `no anchor` and exits 1.
  Red when: a missing anchor leaves the probe comparing against nothing.
- **AC6** — When `env -u _mt_rc bash <scratch file>` runs a file holding `set -u` and an
  `if [ -n "$_mt_rc" ]` line, it prints `unbound variable` and exits 1, not 127.
  Red when: the suite's abort is given the `bash -c` form's exit code.
- **AC7** — When `git log --format=%H <BASE>..HEAD` lists the commits whose `Pass` trailer is
  `TOOL-dSafePassage-52`, `git show --name-only` of each lists none of `memory/HYGIENE.md`,
  `memory/guides/BUILD-METHOD.md` and `memory/guides/ANNOTATION-STYLE.md`, `<BASE>` being the build
  run's pinned base.
  Red when: the render's other outputs ride into TOOL-dSafePassage-52's commit.
  figure: the commit count is DERIVED; zero commits touching the template prints `no edit`, never
  coverage.

## 7. Gates

`push-main self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `harness arms (fail branches armed or pinned)` · `kit/dogfood doc parity` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC2 AC4 · the suite run in gov's own tree prints the derived-count arm's `ok` line and no `skip —` line spelling `derived-count arm`; its failing cases are staged by a suite copy with the arm's guard between the `skip — 28-32` echo and its `fi`, and by a copy with the arm block above the `^_mt_rc=` scan run under `env -u _mt_rc`, which prints `_mt_rc: unbound variable` and no `push-main.test: all cases ok` line · none

What the check does not cover: a render that fails after writing part of a live copy and is then
committed by hand, which the `kit/dogfood doc parity` leg grades, and a skip line that names the arm
in other words.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 51 and 52's 5 MEDIUM and 5
  LOW findings on TOOL-dSafePassage-52, one scope item per raw id.

## 10. Reuse audit

The seams extended are `TOOL-dSafePassage-57`'s arm probe, the suite's scan line and 28-32 block in
`tools/push-main.test.sh`, and the `PAIRS` of `tools/memory-tree/kit-dogfood-parity.test.sh:61`, all
read at source on 2026-10-23. `python tools/codebase-map/reuse_lookup.py "probe that a shell suite arm guard reads its variable after the scan"`
ranked `read`, `read_text`, `probe` and `arm`, name-token matches, none bounding a line by a block's
closing `fi`. So no existing seam fits beyond the suite and that probe.

Recall terms used: `python tools/memory-recall/query.py "how a lander suite arm is placed after the scan it reads and a template repaired through its render" --terms "lander suite arm placement scan set-u unbound render template dogfood parity minors"`
