# TOOL-aWokenSentinel-14 — `seed()` commits once, so every fixture that borrows it has a born HEAD

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 12b3701d · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H6 (round 1, raw id 32): both real-driver integration arms —
`TOOL-aWokenSentinel-3` AC11 and `TOOL-aWokenSentinel-4` AC10 — run `--liveness fx` in a `git init`
fixture "seeded the way `adopt-unattended.test.sh`'s `seed()` builds one". That seed
(`tools/unattended/adopt-unattended.test.sh:38` to `:80`) `git add`s one stub and never commits;
`print_audit`'s clock block, which unit 2 moves verbatim into `read_tree_clocks`, marks
`git log -1 --format=%ct` DEAD on the empty answer an unborn HEAD gives, and unit 2 makes a dead
probe a `fail 52` refusal with no verdict line. The hook then reads `liveness-unreadable` and
allows, so spec 3 AC11 ("the invocation blocks") can never go green and spec 4 AC10's `last-stall:`
line never prints — both arms red for a reason unrelated to the hooks they test. This unit gives
`seed()` its one commit, so every present and future borrower inherits a born HEAD, and
left-shifts the class — a fixture built from another suite's seed inherits that seed's HEAD state —
into `memory/gotchas/`.

## 2. Scope (IN)

- **S1** — `seed()` in `tools/unattended/adopt-unattended.test.sh` ends with one commit over
  everything it staged: `git add -A && git commit -q -m seed --no-verify` inside the fixture, with
  the fixture's own `user.email` and `user.name` already set by the function. Every arm of the
  adopter suite then runs over a repo whose HEAD names a commit. Observed by AC1 and AC2.
- **S2** — The adopter suite's own arms keep their assertions: none reads HEAD, none asserts an
  empty log, and the fixture-gone arms move files the commit does not track differently. Observed
  by AC2.
- **S3** — Specs 3 and 4 are folded at their rev-2 so each real-driver fixture paragraph and each
  `fixture:` line says "seeded by `seed()`, which commits once, so HEAD is born and the driver's
  `git log` probe is live" and cites this unit; the arms themselves are those units' to build.
  Observed by AC3.
- **S4** — A new class in `memory/gotchas/`, `borrowed-seed-inherits-its-head-state.md`: a fixture
  built from another suite's seed inherits that seed's HEAD state, and a probe that reads HEAD is
  dead on an unborn one; anchored by the paths it cites. Observed by AC4.

## 3. Non-goals (OUT)

- **No change to `unattended.sh`.** The dead-probe refusal is correct: a probe that answered
  nothing must say so. The fixture is wrong, not the refusal.
- **No change to the driver suite's own seed.** `unattended.test.sh` builds its fixture with
  commits already; it is the adopter suite's seed the hooks borrow.
- **No content in the commit beyond what `seed()` stages.** The stub checklist, the kit copy, the
  settings file and the conf; the commit is the act, not a fixture of its own.

### Edges

- **consumes-from** external — `tools/unattended/adopt-unattended.test.sh`'s `seed()` at base,
  the function two later units borrow.
- **hands-off** `TOOL-aWokenSentinel-3` — AC11's real-driver fixture, seeded by the committed
  `seed()`; spec 3's fixture paragraph and `fixture:` line cite this unit at rev-2.
- **hands-off** `TOOL-aWokenSentinel-4` — AC10's real-driver fixture, on the same terms.
- **hands-off** `TOOL-aWokenSentinel-2` — nothing; its `fail 52` on a dead `git log` probe is the
  behaviour this unit's fixture stops triggering.

## 4. Design

### The commit

The last statement of `seed()`:

```
( cd "$1" && git add -A && git commit -q -m seed --no-verify )
```

`--no-verify` because the fixture has no hooks and the real tree's `core.hooksPath` is repo-global
and could otherwise reach a fixture created inside a checkout; `-q` because the suite's output is
its assertions. The function already sets `user.email` and `user.name` at `:40`, so the commit
needs no identity of its own. `git add -A` takes what the function wrote beside what it staged;
the arms that later move a fragment aside or delete a hook act on the working tree and the
adopter's `--check` reads the working tree, so a tracked-versus-untracked difference changes no
arm's observation.

### The class, in `memory/gotchas/`

Front matter `name: borrowed-seed-inherits-its-head-state`, a one-line `description`,
`kind: class`; the body names the class, the instance — specs 3 and 4 borrowing
`tools/unattended/adopt-unattended.test.sh`'s `seed()` for a fixture the driver's
`git log -1 --format=%ct` probe at `tools/unattended/unattended.sh:3013` reads — and the remedy:
a fixture that borrows a seed states the HEAD state it inherits, and a seed that a driver's clock
will read commits once. Anchors are DERIVED from the backticked paths in the body, so a diff
touching the adopter suite or the driver's clock block selects it.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `memory/gotchas/borrowed-seed-inherits-its-head-state.md` | gotcha class | no cell; the folder's grammar |

No function, key, verb or kit file is minted.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/adopt-unattended.test.sh` | one line at the end of `seed()` |
| `memory/gotchas/borrowed-seed-inherits-its-head-state.md` | new |

### Alternatives rejected

- **Have each borrowing arm commit after seeding.** Two copies of one line in two suites, and the
  next borrower forgets; the seed is the one place.
- **Have the arms assert the check-52 refusal instead.** That makes the arm observe the fixture's
  defect rather than the hook, which is an arm about nothing.

## 5. Production-readiness checklist

- security — N/A; a commit inside a scratch fixture.
- perf / scale — one `git commit` per seeded fixture, milliseconds; the adopter suite seeds a
  handful.
- error / empty / loading states — a commit that fails fails the seed loudly, which is the suite's
  own refusal shape.
- observability — `git log -1` inside any borrowed fixture answers.
- risks — an arm in the adopter suite that silently depended on an unborn HEAD would change
  behaviour; AC2 runs the suite's arms as commands over a seeded fixture and reads no change.
- testing — §6.
- migration — N/A.
- user docs — none; the gotcha class.

## 6. Acceptance criteria

- **AC1** — When `seed()` is extracted from the adopter suite (the file §4 names) and run by hand
  as one function over a scratch directory under a short `%TEMP%` path, `git -C <dir> log -1 --format=%ct`
  prints one integer and exits 0; at this unit's base the same run prints nothing and exits
  non-zero.
  Red when: HEAD is still unborn, which is the commit line absent or failing quietly.
  fixture: the function run by hand, as spec 3 AC15 already does; never the suite.
- **AC2** — When the adopter's `--check` runs inside a fixture seeded by the committed `seed()`,
  its exit and its output lines are what they are at this unit's base for the same fixture, read
  by running `bash adopt-unattended.sh --check` once from each; and `grep -c 'git commit'` over
  the adopter suite file §4 names prints 1 and 0 at base.
  Red when: the commit changed what `--check` reports, which is an arm depending on tracked state;
  or the count is 0, which is the line lost.
- **AC3** — When `grep -c 'HEAD is born'` runs over
  `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-3.md` and over
  `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-4.md`, each prints at
  least 1.
  Red when: a borrowing spec still describes the fixture without its HEAD state, which is the
  class re-entering by prose.
- **AC4** — When `python tools/memory-tree/gotchas.py --for-diff <base>..<tip>` runs over a range
  touching the adopter suite file, its stdout names
  `borrowed-seed-inherits-its-head-state`, and the tool's report does not list the record as
  unanchored.
  Red when: the class reaches no path, which is a gotcha nobody is shown.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)` · `unattended kit gate`

These run once at `--close`. The pass runs none of them: it verifies with the extracted `seed()`
of AC1, the adopter's `--check` of AC2, and the greps of AC3 and AC4.

New arm: none — the seed is a fixture, not an assertion; the arms it un-reds are units 3 and 4's.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 1 as the
  promotion of H6 (raw id 32).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "seed a fixture repository with one commit so HEAD is
born"` ranked `seed_affordances` in the map kit and the run-gates `KITDIR`/`ROOTN` fixture seam,
neither a git fixture seed, and reported `unscanned layers: .sh`; no existing seam fits. The seam,
read at source: `seed()` at `tools/unattended/adopt-unattended.test.sh:38` to `:80`, which stages
and never commits; the driver suite's own fixture, which commits and is why units 1, 2, 5, 7 and 9
never met this; and the clock probe at `tools/unattended/unattended.sh:3013` that reads HEAD. The
recall probe returned `TOOL-aBoundedCeiling-12` (a killed bar's turnstile beacon, a different dead
state), this build's audit at the H6 paragraph, and `DEPL-dRatifiedSeam-5`; no prior record names
a borrowed seed's HEAD state, which is why the class is new.

Recall terms used: `seed fixture git init unborn HEAD commit git log dead probe fail 52 liveness adopter suite borrow`
