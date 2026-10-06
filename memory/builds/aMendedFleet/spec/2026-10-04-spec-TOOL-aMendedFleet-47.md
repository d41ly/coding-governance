# TOOL-aMendedFleet-47 — `run_records_nonterminal_but_merged` honours derived LANDED, and the unused-verb pin drops to 0

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 47

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

The drift signal `run_records_nonterminal_but_merged` still counts a `LANDING` run record whose own
landing commit is on the default branch, although owner ruling D12-i2 makes such a record LANDED by
derivation, and the unattended driver and its gate leg already read it that way through
`read_landing_commit` in `tools/unattended/lib-unattended.sh`. Re-measured on 2026-10-04 at `fee9f62b`
against `origin/main` at `35438ba0`, the signal reads 13 of 76; 12 of those are `LANDING` records
whose landing commit is on the base, so 2 are actionable, both `BUILDING`. This unit applies the
derived-LANDED rule in the signal, re-seeds its report-only pin at the drained value, and lowers the
gateable `lexicon_verbs_declared_but_unused` pin from 3 to 0, which the signal already reads as 0 of
23 today. What remains of the run-records signal is the population the open ask
`TOOL-aReapedTicket-5` wants a staleness bound for; that bound is not built here.

## 2. Scope (IN)

- **S1** — In `build_nonterminal_merged_runs`, a record whose phase at HEAD is `LANDING` is read
  LANDED when its landing commit is reachable from the base ref, and is then neither counted nor
  unjudgeable. The landing commit is the one `read_landing_commit` names: the newest commit, in
  HEAD's history, that changed the record's path. The test runs BEFORE the witness is placed, so a
  derived-LANDED record never reaches the "witness not re-written since preflight" reason.
  Observed by AC1 and AC2.
- **S2** — The landing commits come from ONE `git log` over every `LANDING` record's path, and the
  ancestry test reuses the parent graph the signal's existing `rev-list --parents` walk already
  built, so the signal costs four git calls where a `LANDING` record exists and three where none
  does, whatever the record count. No call is made at all for a repo with no `LANDING` record.
  Observed by AC2.
- **S3** — The record's `detail` closes with one summary line naming how many `LANDING` records read
  LANDED by derivation, before the existing refused-landing note, so a drained value is
  distinguishable from a probe that stopped reading them. The record gains a `derived_landed` count
  beside `unjudgeable`. Observed by AC1.
- **S4** — The comment block above the signal is corrected: it names derived LANDED as excluded, the
  call count becomes "four at most", and its "WHAT IT DOES NOT SEE" paragraph gains the one case the
  batched read can disagree with the per-record one (§4). Observed by AC5.
- **S5** — `PINS` in `tools/drift-audit/drift_signals.py`: `run_records_nonterminal_but_merged`
  moves 5 to 2, re-seeded at the measured value as its comment requires, and
  `lexicon_verbs_declared_but_unused` moves 3 to 0, its comment rewritten to say the aspirational
  verbs it described are all in use and that a new aspirational verb now reds `--check` until a
  definition uses it. Both are drains, so neither needs a `<old> -> <new>` justification. Observed
  by AC3 and AC4.
- **S6** — `RATCHETS` gains a row for `lexicon_verbs_declared_but_unused`, weakening upward, so
  raising the pin back above 0 needs a reason written in place. Observed by AC4.
- **S7** — The kit selftest's run-records arm moves: the three fixture records that are `LANDING`
  with their commit on `main` become derived-LANDED expectations, one new `LANDING` record whose
  commit is not on the fixture's base ref stays counted, and the call-count arm asserts three calls
  for `BUILDING`-only populations and four once a `LANDING` record exists. NOT OBSERVED by a
  criterion here: the suite runs once at the close, and the arm is declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- The staleness bound and age column for the residual, which `TOOL-aReapedTicket-5` asks for. It
  needs a declared bound that ask deliberately left unpicked, and the synthesis offered it as a
  follow-on rather than as part of this point.
- Observing the remote's advertised tip. The driver derives LANDED against the tip the remote
  advertises; this offline signal derives it against its own base ref, which `resolve_base_ref`
  already reads as the remote-tracking branch. A fetch-stale clone therefore under-derives, which
  over-counts, the direction the signal already errs in.
- Using `branch-sha:`. It is written at preflight, so every live run would derive LANDED on day one.
- Turning the run-records signal gateable, or re-arming the stable-key pins as identity baselines,
  which unit 56 of this build owns.
- Bumping the drift-audit kit version here. It is owed once, after the last unit that moves the kit.

### Edges

- **consumes-from** external — `read_landing_commit` in the unattended kit library, whose definition
  of a landing commit this signal re-spells offline. The drift kit is copy-installed without the
  unattended kit, so it cannot call it.
- **hands-off** external — the staleness bound of `TOOL-aReapedTicket-5`, and the kit version bump
  owed at the build's close.

## 4. Design

### The derived-LANDED read

After CALL 2 parses every record at HEAD, collect the paths whose `phase` is `LANDING`. When that
list is non-empty, CALL 4 is

```
git log --format=%x01%H --name-only --no-renames HEAD -- <each LANDING record path>
```

and the landing commit of a path is the first commit printed above it. CALL 3's `parents` map, the
history of the base ref, answers ancestry by membership: a landing commit that is a key of `parents`
is on the base ref. Derived records are skipped by the counting loop before `w_in` is read.

The batched read agrees with `git log -1 --format=%H HEAD -- <path>`, which is what
`read_landing_commit` runs, on all 12 live `LANDING` records measured on 2026-10-04. It can
disagree in one shape: when the record's newest change is a MERGE that resolved it, because a merge
prints no names without `-m`. Then the batched read names an older commit on one side of that merge;
the older commit is an ancestor of the merge, so on a base ref holding the merge it still derives
LANDED, and on one that does not the record stays counted. The disagreement can only over-count.

`read_landing_commit` also refuses a record whose working copy differs from HEAD beyond the lease
lines. The signal reads HEAD's bytes and never the working copy, so that clause has nothing to
read here.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `derived_landed` | record field, int | none; a JSON key |

No new function. `build_nonterminal_merged_runs` grows by the CALL 4 block; the existing
`_check_run_ancestor` is not used for this test, because membership in `parents` already answers it.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/selftest.py`

### Alternatives rejected

- One `git log -1` per `LANDING` record, exactly as `read_landing_commit` runs it. Exact by
  construction, but the population is every landed unattended build's live `RUN.md` and grows with
  each landing, so a per-record spawn turns a fixed-cost signal into one that grows without bound on
  a host where a spawn was measured at 751 ms.
- Comparing the record's blob at HEAD with its blob at the base ref. One call and content-based, but
  it reads a record as not landed whenever the base has since rewritten that path, which a later run
  in the same folder does, and it diverges from the ruling's definition rather than re-spelling it.

## 5. Production-readiness checklist

- security — N/A — reads the object store and history only; the paths passed to `git log` come from
  `git ls-tree` output, never from a working-tree read.
- perf / scale — one more `git log` over HEAD's history, measured at 0.2 s for 12 paths on node a.
- error / empty / loading states — a failed CALL 4 returns the existing DEAD shape naming the call,
  never a value computed with derivation silently skipped.
- observability — S3's summary line and `derived_landed` count.
- risks — the merge-resolution disagreement of §4, which can only over-count.
- testing — AC1 to AC4 observe the live tree; the selftest arm is S7's.
- migration — N/A — a report value changes; nothing stored changes.
- user docs — N/A — the README's signal row asks the same question and stays true.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs on node a, the
  `run_records_nonterminal_but_merged` record has `value` equal to the count of its `BUILDING` and
  other non-`LANDING` detail rows, `derived_landed` equal to the number of live `LANDING` records
  whose `git log -1 --format=%H HEAD -- <path>` commit satisfies
  `git merge-base --is-ancestor <commit> origin/main`, and its detail ends with the derived summary
  line and then the refused-landing note.
  Red when: a `LANDING` record whose landing commit is on `origin/main` still appears as counted or
  unjudgeable.
  figure: DERIVED at observation time; at writing, value 2 and 12 derived.
- **AC2** — When the signal runs in a `git clone --local` of the tree into a short directory under
  `%TEMP%`, with `--base-ref` naming a commit before the newest `LANDING` record's landing commit,
  that record is counted and not derived; with the default base ref it is derived; and a
  `python -c` that wraps `subprocess.run` and `subprocess.Popen` in a counter around one
  `build_nonterminal_merged_runs` call, as the kit selftest's call-count helper does, counts four
  git calls.
  Red when: the derivation reads a branch-local commit as landed, or the call count grows with the
  record count.
- **AC3** — When `python tools/drift-audit/drift_report.py` runs, its table row for
  `run_records_nonterminal_but_merged` reads `ok (pin 2, drain it)` and its row for
  `lexicon_verbs_declared_but_unused` reads `ok (pin 0)`.
  Red when: either pin still reads its old value.
- **AC4** — When a scratch clone appends one verb line that no definition leads with to the
  `VERBS:` block of `.lexicon.conf`, `python tools/drift-audit/drift_report.py --offenders` there
  prints a `lexicon_verbs_declared_but_unused` line and exits 1; reverting it exits 0. When the same
  clone raises that pin to 1 in `tools/drift-audit/drift_signals.py` with no `0 -> 1` comment and
  commits it, `--offenders` prints a `ratchet` line naming the key.
  Red when: an aspirational verb passes `--check`, or the pin rises without a ratchet finding.
- **AC5** — When `grep -n "derived LANDED" tools/drift-audit/drift_report.py` runs, it prints a
  line inside the signal's header comment, and `grep -c "THREE GIT CALLS" tools/drift-audit/drift_report.py`
  prints 0.
  Red when: the comment still promises three calls whatever the record count.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · the three `LANDING` fixtures re-read as derived, one `LANDING` record committed past the base ref, and the call count with and without a `LANDING` record · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — Batched or per-record landing-commit lookup?
  RESOLVED (agent, 2026-10-04, delegated): batched, one `git log` over every `LANDING` path, per §4.
  It keeps the call count fixed as landed runs accumulate; the measured agreement with the per-record
  read was 12 of 12, and the one disagreeing shape over-counts.
- **F2** — Does the lexicon pin get a `RATCHETS` row?
  RESOLVED (agent, 2026-10-04, delegated): yes. A gateable pin at 0 that can be raised silently is
  the raise-looks-like-drain class `TOOL-aNumeralWarden-3` filed; one row closes it for this key.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.

## 10. Reuse audit

The seam extended is `build_nonterminal_merged_runs` in `tools/drift-audit/drift_report.py`: its
CALL 3 parent graph answers the ancestry test, so no new walk is added. The rule re-spelled is
`read_landing_commit` in `tools/unattended/lib-unattended.sh`, which the driver's `read_derived_phase`
and the gate leg's check 7 share. `python tools/codebase-map/reuse_lookup.py "derive whether an
unattended run record landed from its landing commit"` returned `build_nonterminal_merged_runs` and
name-stem neighbours, no Python reader of a landing commit, and named `.sh` as unscanned; `git grep
read_landing_commit -- tools` covers that layer and finds the shell definition and its callers only.
Where the report and the tree disagree: the report measured 12 hits and 2 actionable at
`ac65de998`; the tree now reads 13 and 2, the extra one being `aBatchedMinors`, whose close landed
after the report. The lexicon pin's population already drained to 0, so that half is the pin alone.

Recall terms used: `python tools/memory-recall/query.py "why does the drift signal for run records
count a LANDING record whose work already landed" --terms "run_records_nonterminal_but_merged
D12-i2 derived LANDED read_landing_commit witness base ref drift-audit report-only pin"`
