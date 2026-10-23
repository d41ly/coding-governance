# TOOL-dSafePassage-57 — TOOL-52 AC1 reads the arm: its guard taken from the suite by content, evaluated after the scan and alone under `set -u`

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-57-deviation-103.md](../build/2026-10-23-build-TOOL-dSafePassage-57-deviation-103.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 51 and 52
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-51-52-spec-audit-round1.md`)
confirmed finding **id 3** at HIGH, its item **H2**. The same defect was found at MEDIUM as ids 9,
14 and 27, item M2, which are batched by their own ids in `TOOL-dSafePassage-58`.

TOOL-dSafePassage-52 AC1 evaluates the scan line and a guard it typed itself, and its second half is
a two-line `set -u` script. Neither reads the arm, so AC1 passes on today's tree, where
`grep -n check-arms.py tools/push-main.test.sh` prints nothing. It stays green when the arm is
missing, misplaced, or guarded by `${_mt_rc:-}`, the form TOOL-dSafePassage-52 §4 rejects.

This unit is id 3's promotion. The criterion takes the arm's own guard line out of the suite by
content and evaluates that text. It builds at order 14, one above TOOL-dSafePassage-52 (order 13),
whose AC1 it repairs. TOOL-dSafePassage-52's §3 hands-off bullet to this unit names the probe, so
that pass may observe its S1 with it.

## 2. Scope (IN)

- **S1** — The ok half. §4 "The arm probe" takes the first line of `tools/push-main.test.sh` that
  opens with `if ` and spells `check-arms.py`, the arm's guard. It refuses a guard spelling
  `${_mt_rc:-`. It strips the leading `if ` and the trailing `; then`, evaluates the suite's one
  `^_mt_rc=` scan line and then that condition, with `HERE=tools` from the repository root and
  `_mt_rc` unset in the environment, and prints `ok-branch` when the condition holds. Observed by AC1.
- **S2** — The abort half. The same extracted condition, evaluated alone under `set -u` with no scan
  before it and `_mt_rc` unset, prints `_mt_rc: unbound variable`, exits non-zero and runs nothing
  after it. Observed by AC2.
- **S3** — Red at the base. Over the suite at the build's pinned base, which holds no guard line
  spelling `check-arms.py`, the probe prints `no arm` and exits 1. Observed by AC3.
- **S4** — The reading. TOOL-dSafePassage-52 AC1 is read as this unit's AC1 and AC2, and its S1's
  "which AC1 observes" names this unit's AC1. TOOL-dSafePassage-52 AC2's first half, the `grep -c`
  count of scan lines, stays a count of scan lines and is not read as observing the arm. Observed by
  AC1.

## 3. Non-goals (OUT)

- The arm's place, which TOOL-dSafePassage-52 AC2 reads, and its anchor on the 28-32 block's `fi`:
  findings 15 and 28, batched in `TOOL-dSafePassage-58`.
- The suite run in gov's own tree and the staged suite copy with the arm above the scan, which the
  main loop observes at the close under the `New arm:` line of §7.
- Moving or rewriting the arm. TOOL-dSafePassage-50 places it and TOOL-dSafePassage-46 writes it.
- The report's left-shift gates and checklist entries.

### Edges

- **consumes-from** `TOOL-dSafePassage-52` — AC1, S1's ok-branch claim and AC2's scan count, which S4 reads in place; without them there is no criterion to repair
- **hands-off** `TOOL-dSafePassage-58` — §4's probe staged over a suite copy whose guard tests another file, run with `_mt_rc` exported by the caller, and the arm's own skip line told from the 28-32 skip, findings 9, 27 and 14 of the spec audit of units 51 and 52

## 4. Design

### The arm probe

```bash
f=tools/push-main.test.sh
g=$(grep -m1 '^if .*check-arms\.py' "$f") || { echo "no arm"; exit 1; }
case "$g" in *'${_mt_rc:-'*) echo "defaulted guard: $g"; exit 1 ;; esac
c=${g#if }; c=${c%; then}
env -u _mt_rc bash -c 'set -u; HERE=tools; eval "$(grep "^_mt_rc=" "$1")"; eval "$2" && echo ok-branch' _ "$f" "$c"
env -u _mt_rc bash -c 'set -u; HERE=tools; eval "$1"; echo after' _ "$c"; echo "alone rc=$?"
```

It runs from the repository root, written to the run's scratchpad. To read another copy of the
suite, `f` is set to that copy's path. This unit ran it on node d, bash under Git for Windows,
2026-10-23, over three suites:

| Suite | Guard line | Output | Exit |
|---|---|---|---|
| `tools/push-main.test.sh` at this spec's commit | none | `no arm` | 1 |
| a scratch copy, TOOL-dSafePassage-46's skeleton guard after the 28-32 `fi` | `[ -n "$_mt_rc" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ]` | `ok-branch`, then `_mt_rc: unbound variable` and `alone rc=127` | 0 |
| the same copy, its guard reading `${_mt_rc:-}` | the defaulted form | `defaulted guard: ...` | 1 |

The 127 is the `bash -c` form's code. The suite itself runs as a file, where the same abort exits 1,
which `TOOL-dSafePassage-58` states for TOOL-dSafePassage-52 S1.

### Inventory

Minted: none in the tree. The probe is a scratch file the pass writes from §4. No function,
constant, conf key, gate leg or policy key.

### Migration

None.

### Rollout

Live at landing. It builds at order 14, one above TOOL-dSafePassage-52 (order 13). Its pass writes
no file unless AC1 finds the guard defaulted, and then only the guard line of
`tools/push-main.test.sh`. That set does not meet TOOL-dSafePassage-51's, also at order 14, which is
the step module, its self-test and its help page. It shares the suite with `TOOL-dSafePassage-58`,
also at order 14, so the build run sequences the two by M6's first clause, this unit first by the
driver's id tie-break.

### Files touched (estimate)

- `tools/push-main.test.sh`, the guard line only, where AC1 finds it reading anything but a bare
  `"$_mt_rc"`.

### Alternatives rejected

- **Running the suite as the criterion.** A suite is not an acceptance observation (the spec
  format's direct-check rule); the suite run is the `New arm:` line's, at the close.
- **Grepping the guard line for `$_mt_rc` and stopping there.** It reads the text but never shows the
  condition takes its ok branch in gov's own tree.

## 5. Production-readiness checklist

- security: N/A — a read-only probe over a test suite's text.
- perf / scale: two `bash -c` runs.
- error / empty / loading states: no guard line prints `no arm` and exits 1, never a pass.
- observability: each half prints its outcome on its own line.
- risks: a guard spread over two lines is not found and reads `no arm`, the loud direction.
- testing: the three suites of §4 and the criteria of §6.
- migration: none.
- user docs: N/A — no `help/` page covers the lander's suite.

## 6. Acceptance criteria

- **AC1** — When §4's probe runs over the lander suite tools/push-main.test.sh as TOOL-dSafePassage-52's pass leaves
  it, it prints `ok-branch`, and the guard line it found holds `"$_mt_rc"` and no `${_mt_rc:-`.
  Red when: the arm's guard is missing, defaulted, or tests a file absent in gov's own tree, so it
  would take its `skip —` branch.
- **AC2** — When the same probe runs, its last two lines are `_mt_rc: unbound variable` and an
  `alone rc=` line whose code is not 0, and no line reads `after`.
  Red when: the arm's own condition, read before any scan, does not abort under `set -u`.
- **AC3** — When the probe runs with `f` set to a copy of the suite taken by
  `git show 3708a705:tools/push-main.test.sh`, it prints `no arm` and exits 1.
  Red when: the probe passes on a suite holding no arm.

## 7. Gates

`push-main self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `harness arms (fail branches armed or pinned)` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC1 AC2 · the suite run in gov's own tree prints the derived-count arm's `ok` line; its failing case is staged by a suite copy whose arm block sits above the `^_mt_rc=` scan, run under `env -u _mt_rc`, which prints `_mt_rc: unbound variable` and no `push-main.test: all cases ok` line · none

What the check does not cover: an arm whose guard spans two lines, and whether the arm's body counts
what TOOL-dSafePassage-46 says it counts.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 51 and 52's id 3
  (HIGH, item H2).

## 10. Reuse audit

The seams extended are the suite's own top-level scan line and TOOL-dSafePassage-46's guard line in
`tools/push-main.test.sh`, the probe reading both by content. `python tools/codebase-map/reuse_lookup.py "probe that a shell suite arm guard reads its variable after the scan"`
ranked `read`, `read_text`, `probe` and `arm`, name-token matches; `arm` in `tools/lib/lib-selftest.sh:108`
runs one self-test case against a wanted exit code and substring, and does not read another suite's
text, so no existing seam fits beyond
the suite itself.

Recall terms used: `python tools/memory-recall/query.py "how a lander suite arm is placed after the scan it reads and a template repaired through its render" --terms "lander suite arm placement scan set-u unbound render template dogfood parity minors"`
