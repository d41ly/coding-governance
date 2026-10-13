# TOOL-dSweptBranches-24 — the follow-up review's process-monitor items, batched

**Status:** OPEN · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 21

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The follow-up's closing diff review (round 1) confirmed four MEDIUM and LOW items against unit 21's
winpid backstop and its live-tree arm. None changes what the reaper kills; each is a field nobody
reads, an outcome no arm can fail on, or a log line that says the wrong thing. This unit closes them
together, per BUILD-METHOD M4's exit rule.

## 2. Scope (IN)

- **S1** — `render_kill`'s killed line carries `backstopped <n>`, and a signal error whose winpid
  backstop also failed carries the backstop's message after the MSYS one (M2, L2: ids 7 and 12).
  **Readers:**
  by name: `reap.py`'s `--kill` and sweep output, which print `render_kill`.
  by value: NO VALUE READERS — no tracked file parses the killed line.
  Observed by AC1.
- **S2** — One stubbed arm drives three members whose MSYS signal is refused, with a backstop that
  lands, one that finds the process gone and one that is denied, and asserts each outcome: none,
  `already_gone` and `errors`. It also asserts `backstopped`. It replaces the arm that only greps
  `reap.py` for `already_gone` (M4: id 13).
  Observed by AC2.
- **S3** — The live-tree arm's spawn poll prints whether the tree was whole or the bound expired,
  from a flag set at the completion exit (L1: ids 5, 9 and 14).
  Observed by AC3.
- **S4** — Spec 21's §7 line for AC1 names a shipped arm with a staged five-second delay, and no
  shipped arm stages one: AC1 was observed by hand on a scratch edit. Spec 21 records that as an
  erratum, and this spec states what is unguarded (M3: id 8).
  Observed by AC4.

## 3. Non-goals (OUT)

- No shipped staged-delay arm: a second live tree with a five-second delay adds about 15 s to a
  suite whose ceiling is 40 s, to guard a poll whose regression costs a flake, not a wrong kill.
- No health-event field for the backstop: the event records what died, and the census decides that.
- No change to which members are signalled, or how.

### Edges

- **consumes-from** `TOOL-dSweptBranches-21` — the backstop and the poll these items sit on.

## 4. Design

S1 extends the existing format strings. S2 reuses the stub shape of
`test_msys_signal_is_backstopped_by_winpid`, adding three members whose stubbed taskkill answers rc
0, rc 128 with taskkill's not-found wording, and rc 1 with `Access is denied`. S3 sets `whole =
True` before the completion `break` and prints from it.

What stays unguarded after this unit: reverting the poll to a fixed three-second wait stays green on
an unloaded node, because the tree usually spawns inside three seconds. The class is
`observed-by-claim-no-arm-discharges`, and its checklist entry gains this case.

### Files touched (estimate)

- `tools/process-monitor/reap.py`
- `tools/process-monitor/selftest.py`
- `memory/builds/dSweptBranches/spec/2026-10-13-spec-TOOL-dSweptBranches-21.md`, the erratum
- `memory/gotchas/observed-by-claim-no-arm-discharges.md`

### Alternatives rejected

- Keeping the source-grep arm beside the behavioural one: it stays green whatever the call sites do,
  so it reads as coverage it does not give.

## 5. Production-readiness checklist

- security — N/A: output and tests.
- perf / scale — the new arm is stubbed and spawns nothing.
- error / empty / loading states — a doubly failed signal now shows both messages.
- observability — S1 and S3.
- risks — none beyond the unguarded poll §4 names.
- testing — AC1 to AC3.
- migration — N/A.
- user docs — N/A: the killed line is self-describing.

## 6. Acceptance criteria

- **AC1** — When `test_backstop_outcomes_are_each_classified` renders its report, the killed line
  reads `backstopped 3` and the error line carries both messages.
  Red when: `render_kill` omits the count.
- **AC2** — When `test_backstop_outcomes_are_each_classified` runs, the landed member is in neither
  list, the gone member is in `already_gone` and the denied member is in `errors`.
  Red when: the backstop's gone disjunct is dropped from `run_kill`.
- **AC3** — When `test_live_tree_dies_completely` prints its spawn line, the line reads `whole`
  only when the completion exit was taken.
  Red when: the line is printed without the flag.
- **AC4** — When `grep -n "erratum" memory/builds/dSweptBranches/spec/2026-10-13-spec-TOOL-dSweptBranches-21.md`
  runs, it finds the line naming AC1 as observed by hand.
  Red when: spec 21 still claims a shipped staged-delay arm.

## 7. Gates

`process-monitor census selftest` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: `tools/process-monitor/selftest.py` · covers AC1 · three refused members, stubbed · none
New arm: `tools/process-monitor/selftest.py` · covers AC2 · three refused members, stubbed · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · promoted at the follow-up's closing diff review, round 1 (M2, M3, M4, L1, L2).

## 10. Reuse audit

`reuse_lookup.py "render a reaper kill report line with counts"` ranked only name-token neighbours
(`counts`, `report`, `render_cards_md`); none renders a kill report. The seam is unit 21's own stubbed arm and `render_kill` in `tools/process-monitor/reap.py`. No new
helper is added.

Recall terms used: "why is the process-monitor census selftest flaky on the daily held job" --terms
"process-monitor census selftest live tree winpid reaper fixed sleep held job windows runner flaky"
