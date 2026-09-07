# TOOL-aReapedSpinner-3 — the classifier: age DECIDES, the CPU rate LABELS

**Status:** OPEN · rev-1 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Turn a scoped census row into one verdict from a closed vocabulary, using a declared age ceiling as
the decision and the CPU rate as the label, so that a report says not just WHICH processes are dead
weight but WHY each one is judged so.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/classify.py`, exposing `derive_verdict(row, conf, live_pids)`
  returning one of the closed set `OK · OVERAGE · SPIN · IDLE · ORPHAN · UNKNOWN`. Observed by AC1.
- **S2** — the DECISION: a row is flagged when `age_s > PROCMON_AGE_CEILING`. Under the ceiling the
  verdict is `OK` whatever the rate. Observed by AC2.
- **S3** — the LABELS, applied only to a flagged row: `ORPHAN` when its `ppid` names no live
  process in the census; else `SPIN` when `cpu_s / age_s >= PROCMON_SPIN_RATE`; else `IDLE`; and
  `OVERAGE` when the rate cannot be computed. `ORPHAN` outranks the rate labels because it is the
  only one carrying independent evidence. Observed by AC3, AC4, AC5.
- **S4** — `UNKNOWN` for a row whose `cpu_s` is `None`, which is what unit 1's join miss produces.
  It is never folded to zero and never labelled `IDLE`. Observed by AC6.
- **S5** — `classify.py --report` renders one line per flagged row and a summary naming the
  population size, the scoped size and the flagged count — all three DERIVED. Observed by AC7.
- **S6** — the report distinguishes "0 flagged of N scoped" from "the census could not be read",
  which exits non-zero. Observed by AC8.

## 3. Non-goals (OUT)

- **No second sample, no sleep, no mtime probing.** The build's research record rejects the
  two-sample progress probe on cost and on the observation that age alone decides every case in the
  prompt.
- **No killing and no scoping.** Units 2 and 4 own those; this unit is a pure function over a row.
- **No per-command ceilings in this unit.** One ceiling, declared once. A per-pattern ceiling table
  is a plausible follow-up and is named here as one rather than built speculatively.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-1` — `age_s`, `cpu_s` and `ppid`. `cpu_s` may be `None`,
  which S4 exists to handle.
- **consumes-from** `TOOL-aReapedSpinner-2` — the classifier grades only admitted rows; it does not
  re-derive scope and would grade an out-of-scope row if handed one.
- **consumes-from** `TOOL-aReapedSpinner-6` — `PROCMON_AGE_CEILING` and `PROCMON_SPIN_RATE`.
- **hands-off** `TOOL-aReapedSpinner-4` — the reaper acts on the verdict vocabulary S1 closes, and
  `PROCMON_REAP_MODE=reap-orphans` names the `ORPHAN` member specifically.
- **hands-off** `TOOL-aReapedSpinner-5` — the hook reports these verdicts and adds none.

## 4. Design

### Why age decides and the rate only labels

A single CPU sample cannot separate "spinning uselessly" from "working hard", and this repo runs
legitimately CPU-bound gate legs for many minutes. What it CAN separate is "past a declared
deadline" from "not past it", and every failure the prompt reports was hours past any defensible
one — the spin loops at 11.4 h, the Monitor greps at 52 to 61 h. So the rate is never a reason to
flag a row; it is how a flagged row is described to a human.

The prompt's own figures make the labelling arithmetic concrete: 46221 CPU-seconds over 41040 s of
age is a rate of 1.13 across the pair, unambiguous at one sample. No process doing real intermittent
work sustains that for eleven hours.

### Why ORPHAN outranks the rate

A dead parent is INDEPENDENT evidence: nothing is waiting for this process's exit status, so nobody
will notice it finishing. The rate labels are heuristics over one sample. Where both apply, the
stronger evidence names the row, and `reap-orphans` mode acts on exactly that member.

**`ppid` liveness is answered from the census itself**, not with a `kill -0` probe: the census is
one consistent snapshot, and probing per row would spend a syscall per process on a question the
snapshot already answers. A `ppid` of 1 is treated as dead by definition — measured: a test
descendant reparented to 1 in front of the probe during this build's research.

### Alternatives rejected

Output-file mtime as a progress signal. It requires knowing which file a process writes, which the
census does not give and cannot derive on Windows without opening handles. Rejected on
unavailability, not on merit.

### Files touched (estimate)

`tools/process-monitor/classify.py` new.

## 5. Production-readiness checklist

- security — read-only; decides nothing irreversible. Its output is what a reaper acts on, so a
  false `ORPHAN` is the failure that matters, which AC4 stages directly.
- perf / scale — arithmetic per row over a few hundred rows.
- error / empty / loading states — S6: an empty flagged set and an unreadable census are different
  exits and say so differently.
- observability — the summary names all three counts, each derived at report time (S5).
- risks — a ceiling set too low kills healthy work. Mitigated by making the ceiling a declared conf
  value with this repo's own bar figures written beside it, and by `reap-orphans` being the default
  mode rather than `reap-all`.
- testing — a table-driven arm per verdict member, plus one arm asserting the vocabulary is CLOSED
  so a new member cannot appear untested.
- migration — none.
- user docs — the kit README's verdict table, unit 6.

## 6. Acceptance criteria

- **AC1** — When `derive_verdict` is called across the fixture table, every returned verdict is a
  member of the closed set, and an arm asserts the set has exactly the six members S1 names.
  Observed by `selftest.py`, arm `test_verdict_vocabulary_is_closed`.
  Red when: a seventh verdict is added and no arm covers it, which is how a report grows a state
  nothing downstream handles.
- **AC2** — When a row's `age_s` is one second UNDER the ceiling and its rate is 1.0, the verdict is
  `OK`; one second OVER, it is not `OK`. Observed by `selftest.py`, arm `test_ceiling_decides`.
  Red when: a high rate flags a young row, which would red every healthy gate leg on the bar.
- **AC3** — When a flagged row's `ppid` names no row in the census, the verdict is `ORPHAN` even
  though its rate would have said `SPIN`. Observed by `selftest.py`, arm
  `test_orphan_outranks_rate`.
  Red when: the rate labels are tested first and a dead-parent row is reported as `SPIN`, which
  `reap-orphans` mode would then decline to kill.
- **AC4** — When a flagged row's `ppid` names a LIVE row in the census, the verdict is not `ORPHAN`.
  Observed by `selftest.py`, arm `test_live_parent_is_not_an_orphan`.
  Red when: liveness is inferred from `ppid != 1` alone, which mislabels every row whose parent is
  alive but not the init process.
- **AC5** — When a flagged row's rate is at the declared threshold exactly, the verdict is `SPIN`;
  just below it, `IDLE`. Observed by `selftest.py`, arm `test_rate_boundary_is_inclusive`.
  Red when: the comparison is strict and the documented threshold is off by one case from the code.
- **AC6** — When a row carries `cpu_s = None`, the verdict is `UNKNOWN` and never `IDLE`. Observed
  by `selftest.py`, arm `test_missing_cpu_is_unknown_not_idle`.
  Red when: `None` is coerced to 0.0, which turns a failed CIM join into a manufactured kill
  candidate — the exact reason unit 1's F1 resolved to carry `None`.
- **AC7** — When `classify.py --report` runs on this node, its summary line names the census size,
  the scoped size and the flagged count, and all three are computed from the run rather than
  written as literals. Observed by `selftest.py`, arm `test_summary_counts_are_derived`.
  Red when: any count is a literal, which the build rules forbid and which is wrong on the next run.
  `figure:` DERIVED — the arm compares the printed counts against the fixture's own length.
- **AC8** — When the census raises, `classify.py --report` exits non-zero and prints no "0 flagged"
  line. Observed by `selftest.py`, arm `test_unreadable_census_is_not_a_clean_report`.
  Red when: a read failure renders as a clean report, which is the class the build rules name.

## 7. Gates

`line length` · `lexicon naming predicates` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/process-monitor/selftest.py` · stages a row per verdict member, a boundary pair at
the ceiling and at the rate, a `None` cpu row, and a raising census · floor moves with unit 1's
arms, one suite.

## 8. Open questions

- **F1 — should `PROCMON_AGE_CEILING` be one value or a per-pattern table?**
  RESOLVED (agent, 2026-09-08, delegated): ONE value. A pattern table needs a declared pattern set
  the adopter maintains, and every failure in the prompt is hours past any single defensible
  ceiling, so the table would buy nothing measurable today. Recorded as a follow-up in §3 rather
  than built. The veto check is clean and the tie-break — fewer open questions — favours the single
  value.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.

## 10. Reuse audit

No existing seam fits for the predicate itself. What IS reused, and it is the substantive half:
`tools/run-gates/run-gates.sh`'s ceiling regime is the model for a DECLARED bound whose absence is
announced rather than defaulted, and `.unattended.conf`'s `GATE_BOUND` comment is the model for
writing this repo's measured bar figures beside a ceiling so the next author can tell whether a
value is tuned or guessed. Both verified against source at BASE. The probe
`python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report it to
the session"` returned no classifier and no verdict vocabulary over processes; the `SEAM`-marked
hits were the `report` name stem, which is a collision.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
