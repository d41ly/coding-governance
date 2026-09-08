# TOOL-aReapedSpinner-3 — the classifier: age DECIDES, the CPU rate LABELS

**Status:** OPEN · rev-4 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md](../build/2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md) | research | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 |
| [2026-09-08-build-TOOL-aReapedSpinner-2-union-graph-measured.md](../build/2026-09-08-build-TOOL-aReapedSpinner-2-union-graph-measured.md) | research | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round3.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round3.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |

<!-- /gen:spec-records -->

## 1. Goal

Turn a scoped census row into one verdict from a closed vocabulary, using a declared age ceiling as
the decision and the CPU rate as the label, so a report says not just WHICH processes are dead
weight but WHY each one is judged so.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/classify.py`, exposing `derive_verdict(row, conf, live_pids)`
  returning one of the closed set `OK · SPIN · IDLE · ORPHAN · UNKNOWN`. Observed by AC1.
- **S2** — the DECISION: a row is flagged when `age_s > PROCMON_AGE_CEILING`. Under the ceiling the
  verdict is `OK` whatever the rate or the parent. Observed by AC2.
- **S3** — the LABELS, applied only to a flagged row, first match wins: `UNKNOWN` when `cpu_s`
  is `None`, which is the whole of PARENT-UNKNOWN by §4; else `ORPHAN` when it is PARENTLESS by §4;
  else `SPIN` when `cpu_s / age_s >= PROCMON_SPIN_RATE`; else `IDLE`. Observed by AC3-AC6.
- **S4** — `classify.py --report` renders one line per flagged row plus a summary naming the rows
  HANDED TO IT and the flagged count, both derived. Observed by AC7.
- **S5** — the report distinguishes "0 flagged of N graded" from "the input could not be read",
  which exits non-zero. Observed by AC8.

## 3. Non-goals (OUT)

- **No second sample, no sleep, no mtime probing.** The research record rejects the two-sample
  probe on cost and on the observation that age alone decides every case in the prompt.
- **No killing and no scoping.** Units 2 and 4 own those; this is a pure function over a row.
- **No `OVERAGE` member.** rev-1 declared one produced "when the rate cannot be computed" while S4
  and AC6 gave that same input `UNKNOWN` — one input, two verdicts, and nothing could emit
  `OVERAGE` at all. AC1's closed-set arm then passed on a dead member: a criterion satisfied by the
  spelling of an enum rather than by behaviour (D4). Deleted rather than given a condition, because
  no condition was left for it.
- **No census read and no scope derivation.** This unit is handed rows. rev-1's `--report` claimed
  to print "the scoped size", a figure only unit 2 can produce, which made unit 3 consume unit 2's
  output as an acceptance input while both sat in one parallel group (D5). The whole
  census→fence→classify→kill chain now has ONE owner, unit 4's `--sweep`.
- **No per-command ceilings.** One ceiling, declared once. A per-pattern table is named as a
  follow-up rather than built.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-1` — `age_s`, `cpu_s` and `win_ppid`. The PARENTLESS
  predicate uses the WINDOWS parent graph because it is the only one defined for every row;
  `msys_ppid` being absent is a statement about backend visibility, never about a dead parent.
- **consumes-from** `TOOL-aReapedSpinner-2` — grades only members of the in-scope SET, and does
  not re-derive scope. This unit therefore sits at `order 4`, after unit 2, not beside it.
- **consumes-from** `TOOL-aReapedSpinner-6` — `PROCMON_AGE_CEILING` and `PROCMON_SPIN_RATE`.
- **hands-off** `TOOL-aReapedSpinner-4` — the reaper acts on the vocabulary S1 closes, owns the
  full chain, and `PROCMON_REAP_MODE=reap-orphans` names the `ORPHAN` member specifically.

## 4. Design

### Why age decides and the rate only labels

A single CPU sample cannot separate "spinning uselessly" from "working hard", and this repo runs
legitimately CPU-bound gate legs for many minutes. What it CAN separate is "past a declared
deadline" from "not past it", and every failure the prompt reports was hours past any defensible
one — the spin loops at 11.4 h, the Monitor greps at 52 to 61 h.

The prompt's own figures make the labelling arithmetic concrete: 46221 CPU-seconds over 41040 s of
age is a rate of 1.13 across the pair, unambiguous at one sample.

**The measurement that proves the ordering matters.** Run unscoped over this node's real table with
no ceiling, the orphan predicate flagged 297 of 315 rows — including Windows Defender at rate 0.79,
`lsass.exe`, `csrss.exe`, `svchost.exe` and Docker. Run with the ceiling and the fence, it flagged
two: both 53-hour `tail -f` processes with dead parents. **The label is meaningless outside the
fenced, over-ceiling population**, and a `reap-orphans` mode reading the label alone would have
reaped `lsass.exe`.

### The PARENTLESS and PARENT-UNKNOWN predicates, stated ONCE each

**PARENTLESS: the row's `win_ppid` names no row in this census.** Its parent process is gone.

**PARENTLESS IS A LABEL AND NEVER A LICENCE.** Measured on this node: 24 of 337 rows are
parentless and 18 are older than an hour — `csrss.exe`, `wininit.exe`, `winlogon.exe`,
`explorer.exe`, `Spotify.exe`, `msedge.exe`. On Windows a parent exiting neither reparents its
children nor clears the field, so parentless is the ORDINARY state of a long-lived desktop
process and no age ceiling separates it from an abandoned one. The only thing between
`reap-orphans` and `explorer.exe` is unit 2's fence, which is why this unit grades only members of
the in-scope set and why that ordering is a safety requirement rather than tidiness.

**PARENT-UNKNOWN: `cpu_s` is `None`, and nothing else.** The backend could not describe the row
fully. This grades `UNKNOWN` and is NEVER `ORPHAN`.

**`msys_ppid` is NOT part of either predicate.** rev-3 put it in PARENT-UNKNOWN, which grades every
NATIVE row unknown — 300-plus of 313 here — and so makes `reap-orphans` inert over the entire
population the kit exists to reap (D32). The parent question moved onto `win_ppid` at rev-3
precisely because it has no sentinel; the MSYS graph carries no parent signal in this unit at all,
and this unit's §3 Edges never claimed it did.

The split is the whole of D18 and it is worth the two names. rev-2 folded `ppid 0` into "parentless"
citing the measurement that says the opposite: `ps -W` reports EVERY non-MSYS Windows process with
`ppid 0`, which is *parent not visible in this backend*, not *parent dead* — the live-predicate
record names it as exactly what "the naive orphan predicate reads as parent is dead", 297 of 315
rows. Combined with unit 2's program-path admission, that made every in-scope `python.exe` or
`node.exe` grade ORPHAN the moment it passed the ceiling, with a live parent — and unit 6 §8 F1
resolves the default mode to `reap-orphans` on the ground that an ORPHAN "has no live claimant by
construction". **The kit's default would have killed healthy, live-parented, in-scope processes.**

The fix is unit 1's, applied here: `win_ppid` is defined for every row and carries no sentinel, so
the predicate needs none. The MSYS graph is used for the descendant walk (unit 4) and for nothing
else.

**The consequence that keeps S2 first:** this repo's own freshly-spawned shells are parentless the
instant their launcher exits, and they are alive and wanted. Only the age ceiling separates them
from the 53-hour orphans, which is what "age DECIDES" means operationally.

**Liveness is answered from the census snapshot**, not with a per-row probe: the census is one
consistent snapshot and probing per row spends a syscall on a question the snapshot answers.

### Alternatives rejected

Output-file mtime as a progress signal: it needs to know which file a process writes, which the
census does not give and cannot derive on Windows without opening handles. Rejected on
unavailability, not on merit.

### Files touched (estimate)

`tools/process-monitor/classify.py` new; arms added to `tools/process-monitor/selftest.py`.

## 5. Production-readiness checklist

- security — read-only. Its output is what a reaper acts on, so a false `ORPHAN` is the failure
  that matters; AC4 and AC6 stage both directions of it.
- perf / scale — arithmetic per row over a few hundred rows.
- error / empty / loading states — S5: an empty flagged set and an unreadable input are different
  exits and say so differently.
- observability — the summary names the graded and flagged counts, derived at report time.
- risks — a ceiling set too low kills healthy work, and §4's measurement shows how much sits just
  the wrong side of a bad one. Mitigated by declaring the ceiling with this repo's bar figures
  beside it, and by `reap-orphans` rather than `reap-all` being the default.
- testing — a fixture per verdict member, plus an arm asserting EVERY member has a producing
  fixture, so a member cannot exist without behaviour.
- migration — none.
- user docs — the kit README's verdict table, unit 6.

## 6. Acceptance criteria

- **AC1** — When the fixture table is graded, every verdict is a member of the closed set, the set
  has exactly the five members S1 names, AND every member is PRODUCED by at least one fixture.
  Observed by `selftest.py`, arm `test_every_verdict_member_has_a_producing_fixture`.
  Red when: a member exists that no input can produce — rev-1's `OVERAGE`, where the arm passed on
  the spelling of the enum (D4). Counting members is not coverage; producing them is.
- **AC2** — When a row's `age_s` is one second UNDER the ceiling, the verdict is `OK` even with a
  rate of 1.0 and a `ppid` of 0; one second OVER, it is not `OK`. Observed by `selftest.py`, arm
  `test_ceiling_decides_before_any_label`.
  Red when: a high rate or a parentless ppid flags a young row — which would red every healthy gate
  leg and every fresh Bash-tool shell on the box.
- **AC3** — When a flagged row's `ppid` names no census row, the verdict is `ORPHAN` even though
  its rate would have said `SPIN`. Observed by `selftest.py`, arm `test_orphan_outranks_rate`.
  Red when: the rate labels are tested first and a dead-parent row reports `SPIN`, which
  `reap-orphans` would then decline to kill.
- **AC4** — When a flagged NATIVE row (`msys_ppid` absent) has a `win_ppid` naming no census row,
  the verdict is `ORPHAN`, and under `reap-orphans` it IS killed. When a flagged row has
  `cpu_s is None`, the verdict is `UNKNOWN` and it is NOT killed. Observed by `selftest.py`, arms
  `test_native_parentless_row_is_orphan_and_reaped` and `test_no_cpu_row_is_unknown`.
  Red when: `msys_ppid` participates in either predicate. rev-3 keyed PARENT-UNKNOWN on it, which
  grades every native row unknown and makes `reap-orphans` inert over the whole target
  population (D32) — the mirror image of D18, and introduced by D18's own repair.
- **AC5** — When a flagged row's `win_ppid` names a LIVE census row, the verdict is not `ORPHAN`.
  Observed by `selftest.py`, arm `test_live_windows_parent_is_not_an_orphan`.
  Red when: liveness is inferred from a sentinel VALUE rather than from the snapshot.
- **AC6** — When a flagged row's rate is at the declared threshold exactly the verdict is `SPIN`;
  just below it, `IDLE`. When `cpu_s` is `None` it is `UNKNOWN` and never `IDLE`. Observed by
  `selftest.py`, arm `test_rate_boundary_and_unknown`.
  Red when: `None` is coerced to 0.0, which turns a failed CIM join into a manufactured kill
  candidate, or the comparison is strict and the documented threshold is off by one case.
- **AC7** — When `classify.py --report` runs over a fixture, its summary names the graded count and
  the flagged count, both computed from the run. Observed by `selftest.py`, arm
  `test_summary_counts_are_derived`.
  Red when: any count is a literal, or the report names a "scoped" count this unit cannot know —
  rev-1's AC7 did, which is the acceptance-input half of D5.
  `figure:` DERIVED — the arm compares the printed counts against the fixture's own length.
- **AC8** — When the input cannot be read, `--report` exits non-zero and prints no "0 flagged"
  line. Observed by `selftest.py`, arm `test_unreadable_input_is_not_a_clean_report`.
  Red when: a read failure renders as a clean report.

## 7. Gates

`line length` · `lexicon naming predicates` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/process-monitor/selftest.py` · stages a row per verdict member, boundary pairs at
the ceiling and at the rate, `ppid` 0 and 1 and a live parent, a `None` cpu row, and an unreadable
input · floor moves with unit 1's arms, one suite.

## 8. Open questions

- **F1 — should `PROCMON_AGE_CEILING` be one value or a per-pattern table?**
  RESOLVED (agent, 2026-09-08, delegated): ONE value. A pattern table needs a declared pattern set
  the adopter maintains, and every failure in the prompt is hours past any single defensible
  ceiling. Recorded as a follow-up in §3 rather than built. Vetoes clean; the tie-break is fewer
  open questions.
- **F2 — should `OVERAGE` be given a condition instead of deleted?**
  RESOLVED (agent, 2026-09-08, delegated): DELETED. The only candidate condition — a flagged row
  that is neither parentless nor above the spin rate — is exactly `IDLE`, and a second name for one
  state is two answers to one question. The vocabulary shrinks to five and AC1 now requires a
  producing fixture per member, so this cannot recur silently.

## 9. Revision log

- rev-4 · 2026-09-08 · S3 · §4 · AC4 · folded round 3 at its NON-CONVERGENT exit. D32:
  PARENT-UNKNOWN drops its `msys_ppid` clause and is `cpu_s is None` alone — rev-3's version
  graded every native row UNKNOWN and made the default mode inert over the entire target
  population, which is D18's repair overshooting into D18's mirror image. §4 also gains the
  measured false-positive population for PARENTLESS, so no later reader can read the label as
  a licence.
- rev-1 · 2026-09-08 · initial draft.
- rev-2 · 2026-09-08 · header order · S1 · S3 · S4 · §3 · §4 · AC1 · AC4-AC7 · §8 F2 · folded
  round 1 and the live-predicate probe.
- rev-3 · 2026-09-08 · S3 · §3 Edges · §4 · AC4 · AC5 · folded round 2. D18: the predicate
  SPLITS into PARENTLESS (`win_ppid` names no census row) and PARENT-UNKNOWN (`msys_ppid`
  absent), which grades `UNKNOWN`. rev-2 folded the MSYS `ppid 0` sentinel into parentless
  against the measurement that produced it, so every in-scope native process would have graded
  ORPHAN with a live parent and `reap-orphans` would have killed it. D4: `OVERAGE` deleted — nothing
  could produce it — and AC1 now demands a producing fixture per member rather than a member count.
  D5: `order` moves 3 → 4 because this unit consumes unit 2, and the "scoped size" figure leaves
  `--report`; the whole chain becomes unit 4's `--sweep`. D15: the ORPHAN predicate is stated ONCE
  in §4, `ppid` 0 joins it on the probe's evidence, and AC4 stages both values.

## 10. Reuse audit

No existing seam fits for the predicate itself. What IS reused, and it is the substantive half:
`tools/run-gates/run-gates.sh`'s ceiling regime is the model for a DECLARED bound whose absence is
announced rather than defaulted, and `.unattended.conf`'s `GATE_BOUND` comment is the model for
writing this repo's measured bar figures beside a ceiling so a later reader can tell a tuned value
from a guessed one. Both verified against source at BASE.

`python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report it to
the session"` returned no classifier and no verdict vocabulary over processes; its `SEAM`-marked
hits were the `report` name stem. Recorded because that probe also missed the shell process-table
reader unit 1 §10 now cites — the map's own coverage line says `unscanned layers: .sh`, so a shell
seam is invisible to it and a `no seam fits` finding from this probe alone is weaker than it looks.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
