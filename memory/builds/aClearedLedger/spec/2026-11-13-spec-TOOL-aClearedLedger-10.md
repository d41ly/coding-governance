# TOOL-aClearedLedger-10 — four suite budget rows re-declared from readings taken alone on a quiet node, with the ceiling evidence and the pass legs re-derived

**Status:** DEFERRED · rev-1 · 2026-11-13 · node a · Tier-1 · base 8db6f4be · streams tooling · order 10 · closes TOOL-aNimbleMend-22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md) | research | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 |
| [2026-11-13-review-TOOL-aClearedLedger-1-2-3-4-5-6-7-9-10-diff-review-round1.md](../reviews/2026-11-13-review-TOOL-aClearedLedger-1-2-3-4-5-6-7-9-10-diff-review-round1.md) | diff-review | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 |

<!-- /gen:spec-records -->

## 1. Goal

Four suites ran past their declared cost budgets at aNimbleMend's close, on readings taken beside
other suite jobs. This unit re-declares the four rows of `tools/run-gates/selftest-budgets.txt`
from readings the main loop takes of each suite alone, after every other unit of this build is
CLOSED, and carries each reading into the ceiling evidence and the pass-leg declaration.

## 2. Scope (IN)

- **S1** — The four rows of `tools/run-gates/selftest-budgets.txt` named in §4 "The rows" each
  carry a new budget and a new reading text, in the shape §4 "A row" gives. The budget is the
  reading at the file's stated margin. No other row and no header line moves. Observed by AC1 and
  AC2.
- **S2** — For each of the four legs whose reading exceeds its recorded maximum in
  `tools/run-gates/ceiling-evidence.txt`, that row is raised through
  `tools/run-gates/derive-ceilings.py --write --observed`, as §4 "The evidence" gives. A leg whose
  reading does not exceed its maximum keeps its row. No other evidence row moves. Observed by AC3.
- **S3** — `python tools/run-gates/pass_legs.py --apply` runs after S2, so the `pass_leg` fields of
  `tools/gate-legs.json` are what the tracked evidence derives. Observed by AC4.
- **S4** — Where `tools/gate-legs.json` moved, the `last-audit` value of
  `memory/guides/SESSION-KICKOFF.md` is re-stamped in the same commit, under that file's stamp
  rule, with a delta line in the commit message. Observed by AC5.

## 3. Non-goals (OUT)

- Taking the readings. They are the main loop's, taken after units 1 to 9 are CLOSED, and they
  reach the builder in this unit's build brief.
- Any change to a suite, to `tools/run-gates/ceiling-margin.txt`, or to the margin the budgets file
  states in its header.
- Lowering an evidence row. The file is monotone and `--reset` is not used.
- Any other budget row, the estimate rows of the sharded suites included.
- A raised manifest ceiling, unless F1 is resolved to allow it.
- Any kit version, which the lander's `mint` moves.

## 4. Design

### The rows

The figures the four rows and their legs hold today. Each leg takes its argv from
`tools/gate-legs.json`, so the third field of its budget row is empty and stays empty.

| Row and leg name | Budget now | Manifest ceiling | Evidence maximum | Pinned at |
|---|---|---|---|---|
| `unattended-build self-test` | 500 | 700 | 332.0 | `8db6f4be` |
| `run-gates canary` | 3660 | 13200 | 2304.8 | `8db6f4be` |
| `run-gates evidence` | 2250 | 7040 | 1385.1 | `8db6f4be` |
| `memory-hygiene self-test` | 1220 | 4800 | 1970.5 | `8db6f4be` |

### The reading

The main loop takes one reading per leg and hands the builder, for each: the whole seconds `N`,
rounded up; the sha of the frozen clone it ran on; the date; the suite's verdict and its assertion
total as the suite printed them; and what showed the node quiet, as a count of foreign suite
processes before the run. A reading is one direct timed run of the leg's own argv, alone, on a
frozen clone of the build's tip. A run that was killed or did not print its total is not a reading.
The builder writes no figure the brief does not carry.

### A row

The file's header states the margin: the worst observed reading times 1.5, with a floor that is PINNED at `8db6f4be` as 60 seconds.
The newest rows round the product up to the next ten, so the budget is:

```
budget = max(60, ceil(1.5 * N / 10) * 10)
```

The row keeps its four tab-separated fields. The fourth opens with the phrase the `--rank` reader of
`tools/run-gates/run-selftests.sh` recognises as a direct reading, and closes with this unit's id:

```
<name>	<budget>		measured <N>s on node a <date> at <sha8>, one direct run of the leg's own argv alone on a frozen clone, <assertion total and verdict>, <the quiet evidence>, x1.5. TOOL-aClearedLedger-10
```

### The evidence

For a leg whose `N` exceeds its evidence maximum, the builder runs, once per leg:

```
GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --observed "<leg>=<N>" --how "<text>"
```

The `--how` text is one line. It holds no tab and no double quote, and it spells no kit path,
because the install-prefix leg reads this file (TOOL-dSafePassage-85). It says who took the
reading, that the leg ran alone, the sha and the quiet evidence.

The command also distils the worktree's own run record, so its summary line must read `0 raised`
and `1 raised by --observed`. Where it would raise another row, the builder runs it in a fresh
clone of the pass's tree, whose git directory holds no run record, and copies
`ceiling-evidence.txt` back. The verb takes one `--observed` per call.

For a leg whose `N` is at or under its maximum the verb refuses, exit 1, and writes nothing. The
builder makes no call for it and the acceptance ledger names the maximum that stands.

### The ceiling

`derive-ceilings.py#cmd_check` passes a leg whose ceiling is at least its evidenced maximum plus the
larger of the margin file's floor and its fraction of that maximum. With today's margin row a
ceiling must be at least twice a reading that is above the floor, PINNED at `8db6f4be` as 120 seconds.
A reading above half of a leg's manifest ceiling therefore leaves that ceiling short. F1 asks who
moves it. The readings at aNimbleMend's close, on a busy node, put two of the four legs past that
half.

### The pass legs and the stamp

`pass_legs.py --apply` rewrites the `pass_leg` fields from tracked files. The four legs are suites,
which its rule excludes, so the fields move only if another input moved. Where
`git diff --quiet -- tools/gate-legs.json` reports a change, from this verb or from F1, the builder
re-stamps `last-audit` in the same commit and names the delta in the commit message.

### Files touched (estimate)

- `tools/run-gates/selftest-budgets.txt`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

- **AC1** — When `grep -c 'alone on a frozen clone.*TOOL-aClearedLedger-10$' tools/run-gates/selftest-budgets.txt`
  runs it prints 4, and `git diff --numstat HEAD~1 HEAD -- tools/run-gates/selftest-budgets.txt`
  at the unit's commit prints 4 added and 4 deleted.
  Red when: a row keeps its old reading, or a row outside the four moved.
- **AC2** — When this probe runs, it prints the four row names, each followed by `at-margin`:
  `awk -F'\t' '/TOOL-aClearedLedger-10$/ { match($4, /measured [0-9]+s/); r = substr($4, RSTART+9, RLENGTH-10); b = int((r*1.5 + 9.999)/10)*10; if (b < 60) b = 60; print $1, ($2 == b ? "at-margin" : "OFF") }' tools/run-gates/selftest-budgets.txt`
  Red when: a budget was typed from anything but its own row's reading, or the reading does not
  open with the phrase the `--rank` reader recognises.
  figure: DERIVED by the probe from each row. The probe prints `at-margin` for the three rows TOOL-aNimbleMend-15 wrote, observed at `8db6f4be`.
- **AC3** — When `grep -E '^(unattended-build self-test|run-gates canary|run-gates evidence|memory-hygiene self-test)	' tools/run-gates/ceiling-evidence.txt`
  runs, it prints four rows, each maximum at or above that leg's reading in the budgets file, and a
  row whose maximum equals the reading names node `a` and the `--how` text in its last field.
  Red when: a reading above the stored maximum was not carried, or a row was typed by hand and
  carries the `runner` source for a reading the runner never saw.
- **AC4** — When `python tools/run-gates/pass_legs.py --check` runs at the unit's commit, it exits 0.
  Red when: the manifest's `pass_leg` fields are not what `--apply` writes from the tracked files.
- **AC5** — When `git log -1 --format=%H -- tools/gate-legs.json` and `git log -1 --format=%H -G'^last-audit:' -- memory/guides/SESSION-KICKOFF.md`
  run after the unit's commit, both print that commit's sha, or the first prints a sha from before
  this unit.
  Red when: the manifest moved in a commit that did not move the stamp.
- **AC6** — When the main loop runs `python tools/run-gates/derive-ceilings.py --check` at the
  unit's commit, it exits 0 and names none of the four legs in a `CEILING-EVIDENCE FAILED` line.
  Red when: a carried reading leaves a ceiling short of its margin and F1's answer was not applied.
  permission: the `leg ceilings clear their evidenced maximum` leg runs this argv, so the
  observation is the main loop's and no builder pass makes it.

## 6. Gates

`leg ceilings clear their evidenced maximum` · `every held leg is budgeted, every budget row resolves` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures`

The close's bar runs these once, after this unit, which is the last. No pass runs one. The last
four guard `tools/gate-legs.json`. The four
suites themselves are run by the main loop alone, to take the readings, and this unit adds no arm.

## 7. Open questions

- **F1 — If a reading leaves a manifest ceiling short of its margin, who raises that ceiling?**
  The build method says a declared ceiling is the owner's to move unless the declaring file names
  the rows a run may raise, and `tools/gate-legs.json` names none. The owner's prompt orders the
  evidence written and expects the manifest to move, and does not name a ceiling.
  - Option A: the builder raises that leg's `ceiling` to the smallest multiple of ten that clears
    `derive-ceilings.py --check`, in this unit's commit, and the acceptance ledger names the old
    and new value. TOOL-dRankedPlan-83 raised one ceiling this way, on the owner's order.
  - Option B: the builder stops before the evidence row is written for that leg, and the main loop
    asks the owner with the reading and the figure the margin needs. The other legs proceed.
  - Option C: the reading is left out of the evidence file, so no ceiling is short. The budget row
    then names a reading the evidence file does not hold.
  - Recommendation: A, ruled once before the readings are taken, so the unit does not stop
    mid-pass. Whether it applies at all is decided by the readings.
  RESOLVED (owner, 2026-11-13): A, the builder raises a short ceiling to the smallest multiple of ten that clears the check, in the unit's commit, and the ledger names both values.

## 8. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 9. Reuse audit

The seams are the two verbs the prompt names, used as they stand; this unit writes no code.
`python tools/codebase-map/reuse_lookup.py "re-measure a self-test suite's cost budget row and
record an out-of-band ceiling reading"` ranked row readers only, and for the out-of-band route no
existing seam fits by that probe, so it was found by reading: `tools/run-gates/derive-ceilings.py`
`cmd_write` admits one `--observed` reading per call, refuses one that does not raise its row, and
distils the run record beside it, and `tools/run-gates/pass_legs.py` `cmd_apply` reads tracked
files alone. Recall returned the precedents: TOOL-aHomedAnchor-28, which re-declared the
`unattended-build self-test` row from a quiet reading; TOOL-dRankedPlan-83, which sized a ceiling
through `--observed` and re-stamped the kickoff manifest; and TOOL-dSafePassage-85, where a
`--how` text that spelled a kit path redded the install-prefix leg.

Recall terms used: `python tools/memory-recall/query.py "how is a selftest budget row re-measured
alone on a quiet node and its ceiling evidence raised out of band" --terms "selftest-budgets budget
row reading quiet node x1.5 derive-ceilings observed ceiling-evidence monotone pass_legs apply
last-audit"`
