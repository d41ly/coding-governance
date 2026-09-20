# TOOL-aWokenSentinel-26 — the marker region's accepting arm asserts its entry state before it runs: a committed `LANDING` record, a clean tree and HEAD advertised on `origin main`

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 830c46e8 · streams tooling · order 26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-prompt-TOOL-aWokenSentinel-26-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-26-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H2 (round 4, raw ids 1 and 23): `TOOL-aWokenSentinel-22`'s pushed control
reads `phase: LANDED` as `1`, so it lands the fixture's record and its `git push -q -f origin
tscratch:main` moves `origin main`; the accepting arm at `tools/unattended/unattended.test.sh:4549`
to `:4554` has no setup of its own, so with the control placed above it that arm runs `--landed`
on a LANDED record, check 26 refuses, its three `miss` strings are none of that sentence and pass,
and its `same` on `phase: LANDED` reads the control's write — spec 16 AC3's arm green by absence,
and no criterion in spec 22 §6 watching it. The control's after-state restoration is folded at
spec 22's rev-2. The CLASS is an arm whose reading is inherited from a predecessor's write, and the
accepting arm is the one arm in the region that establishes nothing before it reads: every other
arm there runs `reset_tree`, `sed` to `LANDING`, `fixture` and its own push, and the MISSING-marker
arm at `:4556` says in its comment why it does. This unit gives the accepting arm three `same`
lines on entry — the record is at `LANDING` exactly once, the tree is clean, and HEAD is the commit
`origin` advertises for `main` — so the next arm inserted above it that leaves any of those false
reds here with the property that moved, rather than passing the accepting arm on the sentence of an
unrelated refusal.

## 2. Scope (IN)

- **S1** — Three `same` lines directly above the accepting arm's `printf` of the marker at
  `unattended.test.sh:4547`, in the suite's own helper idiom: `same "accepting arm enters at a
  committed LANDING record" "$(grep -c '^phase: LANDING' memory/builds/tRun/RUN.md)" "1"`;
  `same "accepting arm enters with a clean tree" "$(git status --porcelain | grep -c '')" "0"`;
  `same "accepting arm enters with HEAD advertised as origin main" "$(git rev-parse HEAD)"
  "$(git ls-remote -q origin refs/heads/main | cut -f1)"`. Observed by AC1 and AC2.
- **S2** — The three lines are observed RED first, one property at a time, by evaluating them in
  the fixture at the pass with the record `sed` to `LANDED`, then with one untracked file written,
  then with `origin main` moved to a scratch commit by `git push -q -f origin <scratch>:main`,
  each printing `FAIL accepting arm enters` naming its property; and GREEN with the region's own
  setup restored. Observed by AC2.
- **S3** — The accepting arm's comment names the three properties as the arm's precondition and
  names spec 22's control as the write that first violated it, by id `TOOL-aWokenSentinel-22`.
  Observed by AC3.
- **S4** — `FLOOR_ASSERTIONS` at `unattended.test.sh:5721` and the shard floor the accepting arm
  sits under rise by three, the executed count of S1, in the same commit. Observed by AC4.

## 3. Non-goals (OUT)

- **No change to what the accepting arm reads.** Its three `miss` lines and its `same` on
  `phase: LANDED` are spec 16 AC3's; this unit adds what must be true BEFORE they run.
- **No setup of its own for the accepting arm.** A `reset_tree; --preflight; mkconf; sed; fixture;
  push` block above it would re-establish the state silently and hide the next insertion the way
  the region hides this one; an assertion names the arm that broke the state, a rebuild does not.
- **No guard on the other arms in the region.** Each already establishes its own state before it
  reads; a guard there asserts what the line above just did.
- **No suite-wide rule.** "Every arm re-establishes its state" is not greppable and this unit does
  not pretend it is; the class is closed where its one instance lives.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-22` — the two arms and the pushed control above the
  accepting arm, and the after-state restoration its rev-2 adds; this unit's guard is what proves
  that restoration ran, and is ordered after it so the first green of the guard is a reading over
  the region as it will ship. The accepting arm itself is the one unit 16's rev-2 keeps in the
  region on the remote arm, which unit 22 already consumes; this unit reaches it through unit 22
  and declares no second edge to a spec round 3 closed.
- **consumes-from** external — the suite's `same`, `fixture`, `reset_tree` and `mkconf` helpers at
  `unattended.test.sh:71`, `:363`, `:357` and `:108`, and its fixture `origin` added at `:344`.
- **hands-off** external — nothing.

## 4. Design

### The guard

```
# THE ACCEPTING ARM ESTABLISHES NOTHING, so it asserts what it needs. Spec 22's pushed control
# (TOOL-aWokenSentinel-22) landed the record and moved origin main above this line; every miss
# below passes on ANY refusal, so an inherited LANDED record read as green here. Three properties,
# each named when it is the one that moved.
same "accepting arm enters at a committed LANDING record" "$(grep -c '^phase: LANDING' memory/builds/tRun/RUN.md)" "1"
same "accepting arm enters with a clean tree" "$(git status --porcelain | grep -c '')" "0"
same "accepting arm enters with HEAD advertised as origin main" "$(git rev-parse HEAD)" "$(git ls-remote -q origin refs/heads/main | cut -f1)"
printf 'landed main at %s by push-main\n' "$(git rev-parse HEAD)" > "$GCD/tmarker"
out=$(run --landed tRun)
```

The third `same` reads the advertisement the driver itself reads, `ls-remote` against the fixture
`origin`, rather than `refs/remotes/origin/main`, so the guard and check 34 agree on what "HEAD is
on the remote" means. The clean-tree count is `git status --porcelain | grep -c ''`, which reads an
empty listing as `0`; it is a pipe from a command, not from a captured variable, and is outside
unit 23's predicate by that fact.

### The RED-first readings

In the fixture clone at the accepting arm's position, before the guard is committed, the pass
evaluates the three lines under each of three staged states: `sed -i 's/^phase: .*/phase: LANDED/'
memory/builds/tRun/RUN.md` reds the first; `: > stray` reds the second; `git push -q -f origin
<scratch>:main` where `<scratch>` is one `--allow-empty` commit on a branch off HEAD reds the
third. Each prints the `FAIL accepting arm enters …` sentence of its own property and no other.
The region's own setup — `sed` to `LANDING`, `rm stray`, `fixture`, `git push -q -f origin
HEAD:main` — restores all three, and the lines print nothing.

### Inventory

| identifier | kind | cell |
|---|---|---|
| none | — | — |

No function, key, verb or file is minted; the three labels are `same` arguments.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/unattended.test.sh` | three `same` lines and the comment above the accepting arm's `printf`; `FLOOR_ASSERTIONS` and the accepting arm's shard floor raised by three |

### Alternatives rejected

- **Have spec 22's control restore the state and stop there.** The fold does that. It fixes the
  instance; the next arm inserted between the control and the accepting arm inherits the same
  hole, and the region's comment at `:4557` already asked for this once.
- **Give the accepting arm its own setup block.** See §3: a rebuild hides the insertion the guard
  names.
- **A `hit "$out" "phase LANDED"` on the accepting arm's output.** The driver prints the phase on
  success, so a positive read helps; but it is red only when the run refuses, and the
  inherited-state case here does not refuse — it accepts on the wrong record.

## 5. Production-readiness checklist

- security — N/A; three assertions in a suite.
- perf / scale — one `grep`, one `git status` and one `ls-remote` against a local fixture remote,
  milliseconds.
- error / empty / loading states — a missing record makes the first `same` read `0` and red; an
  unborn `origin main` makes the third read an empty string against a sha and red.
- observability — each `same` names its property and prints both values.
- risks — a future move of the accepting arm past another landing arm reds the guard on its first
  run, which is the reading this unit wants; the remedy is the region's own setup, named in the
  comment.
- testing — §6; the three staged states and the restored one, in the fixture at the pass.
- migration — N/A.
- user docs — none; the comment.

## 6. Acceptance criteria

The fixture is the suite's marker fixture at `tools/unattended/unattended.test.sh:4514`, in a
scratch clone under a short `%TEMP%` path, at the accepting arm's position after spec 22's arms and
control have run.

- **AC1** — When `grep -c 'accepting arm enters' tools/unattended/unattended.test.sh` runs at the
  tip it prints 3 and 0 at this unit's base, and the three lines sit above the accepting arm's
  `printf 'landed main at %s by push-main'` and below spec 22's pushed control, by line number.
  Red when: the guard is absent or sits below the read it guards, which asserts nothing about
  entry.
  figure: the line numbers are DERIVED by `grep -n` at observation.
- **AC2** — When the three `same` lines are evaluated in the fixture with the record at `LANDED`,
  the output carries `FAIL accepting arm enters at a committed LANDING record: expected [1], got
  [0]`; with one untracked file present, `FAIL accepting arm enters with a clean tree`; with
  `origin main` moved by `git push -q -f origin` to a scratch commit, `FAIL accepting arm enters
  with HEAD advertised as origin main`; and with the region's setup restored, no `FAIL` line.
  Red when: a staged state passes its guard, which is a guard that cannot fail; or the restored
  state reds, which is a guard that reds every honest run.
  fixture: the marker fixture plus one `--allow-empty` commit on a scratch branch for the third
  reading.
- **AC3** — When `grep -c 'TOOL-aWokenSentinel-22' tools/unattended/unattended.test.sh` runs at the
  tip it prints at least 1, on the comment above the guard.
  Red when: the comment names the hazard without the id of the write that first produced it.
- **AC4** — When `sed -n 's/^FLOOR_ASSERTIONS=//p' tools/unattended/unattended.test.sh` runs at the
  tip, its last value is the value at the tip of unit 22's pass plus 3, and the shard floor line
  the accepting arm sits under has moved by 3 as well.
  Red when: the floors did not move, which is three executed assertions of slack nobody declared.
  figure: both values are DERIVED by the `sed` and by `grep -n '^FLOOR_SHARD_'` at observation,
  over the tip and over the file at the tip of unit 22's pass — the commit whose subject carries
  `TOOL-aWokenSentinel-22`.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the greps of AC1, AC3 and
AC4 and the four evaluations of AC2 in the fixture. Under `harness arms`, no branch's verdict
moves — the guard arms nothing and reads the suite's own state.

New arm: `tools/unattended/unattended.test.sh` · three entry-state assertions on the accepting marker arm, staged RED by a LANDED record, an untracked file and a moved `origin main` · `FLOOR_ASSERTIONS` and the accepting arm's shard floor rise by three

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 4 as the
  promotion of H2 (raw ids 1, 23): the control's after-state restoration is spec 22's rev-2 fold,
  and the accepting arm's entry guard is this unit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "assert a test arm's entry state before it runs so a
predecessor arm's write cannot be inherited silently"` ranked the `run` seam across thirteen Python
tools, `write` in `tools/memory-tree/gotchas.py` and `armed` in `tools/memory-tree/corpus_ids.py`,
none a shell assertion, and reported `unscanned layers: .sh`; no Python seam fits. The seam, read
at source, is the suite's own `same` helper at `tools/unattended/unattended.test.sh:71` and the
marker region's setup idiom at `:4514` to `:4566`, whose MISSING-marker arm at `:4556` already
states the precondition this unit asserts. The recall probe returned `TOOL-dTieredTribunal-28`
(an arm asserting a refused `--landed` leaves the record byte-identical, a gate whose failing case
was observed against the pre-fix revision — the RED-first shape S2 copies), this build's round-4
audit at the H2 paragraph, and `TOOL-aGroundedOrientation-4` (the wedged terminal record check 26
refuses, which is the refusal the accepting arm's `miss` lines pass on); no prior record guards an
arm's entry state.

Recall terms used: `marker region accepting arm fixture state inherited predecessor write green-by-absence LANDED LANDING miss vacuous`
