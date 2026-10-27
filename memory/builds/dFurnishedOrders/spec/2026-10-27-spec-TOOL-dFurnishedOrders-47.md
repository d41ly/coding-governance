# TOOL-dFurnishedOrders-47 — unit 44's parity arm grades the receipt `apply` finishes: an adopter or render problem outside home parity is named and tolerated, and a refusal before the final receipt still fails the arm

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base e8b9b07c · streams tooling · order 9 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-47-round5-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-47-round5-fix-return.md) | research | TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-47-round5-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-47-round5-fix-brief.md) | research | TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 |
| [2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-4 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md`)
confirmed finding **id 10 at HIGH**, report item **H1**. No other id shares that item.

`TOOL-dFurnishedOrders-44` S1 says "A refused `apply` fails the arm", and its §4 sketch writes
`p.returncode != 0 -> FAIL` (spec-44 line 74). At `e8b9b07c` that `apply` exits 1 for reasons unrelated
to home parity, so the arm would be red on the day it lands. This unit's own probe re-ran it on
2026-10-27 (§4 "What the probe measured"): exit 1 in 20 s, with 19 problems, all from adopters, renders
and one gate-leg argv, and the final receipt was still written. A builder who accepts exit 1 by hand,
or narrows the selection with `--kits`, changes the oracle unit 44 was specced to read.

This unit states which outcome the arm accepts: the receipt `apply` finishes writing, graded alone,
with every problem outside home parity printed and never failing the arm. It repairs
`TOOL-dFurnishedOrders-44` and builds one step after it (order 9).

## 2. Scope (IN)

- **S1** — The outcome the arm accepts. `check_receipt_home_parity` in `tools/govkit/selftest.py`
  (unit 44 S1) proceeds when `apply`'s exit is 0, or is 1 and its stdout carries the final receipt
  step line `govkit apply — [11/RECEIPT]`. `step(STEP_RECEIPT, ...)` prints that line
  (`tools/govkit/govkit.py:8406`) after the final receipt write (`:8402`) and before `r.emit()` returns
  1 on any accumulated problem (`:1641-1649`). Any other exit fails the arm, naming the exit and the
  last three stderr lines. That covers 2, a `Refusal` (`:14133-14135`), and any other value. So does an
  exit 1 with no RECEIPT line, or a receipt file absent after it. Unit 44 S1's sentence "A refused
  `apply` fails the arm" holds for this narrower meaning of refused. Observed by AC1 and AC2.
- **S2** — The tolerated problems are printed, never silent. On exit 1 the arm counts the `govkit: `
  problem lines `Report.emit` prints, without the `<n> problem(s)` total. It prints
  `home parity: apply exit 1, <n> problem(s) outside home parity` and names each distinct entry id
  those lines quote. A problem of any class is tolerated, because unit 44 S2's compare in both
  directions is what grades the rows apply wrote: a problem that lost a kit's rows shows as a
  `derived-only` home. Observed by AC1.
- **S3** — Re-timed. The arm's counts line also prints the apply's wall seconds. The `govkit selftest`
  row of `tools/run-gates/selftest-budgets.txt` (`:66`, 1600, "worst of 7 readings 1065s, x1.5") is
  re-priced to `ceil(1.5 * (1065 + t))`. `t` is the apply wall time the pass measures once, and the
  row's note names both inputs. At this unit's probe `t` = 20, so the row is 1628 (PINNED,
  2026-10-27). Observed by AC3.

## 3. Non-goals (OUT)

- The isolation of unit 44 S3's DEAD PROBE clauses, its list literal, the rule image unit 44's arm
  compares, and the `govkit selftest` guard's coverage: the minors batch `TOOL-dFurnishedOrders-48`,
  for ids 4, 15, 34, 5, 17, 9, 35, 21, 11 and 28.
- Making every adopter succeed in the fixture: §4 "Alternatives rejected".
- Grading `apply`'s own health. The acceptance matrix and the suite's other `apply` arms own it, and
  this arm reads the receipt alone.
- The report's left-shift spec-lint rule (cite one observed run of a real command an AC fails on): no
  clause of this build names it. This spec's AC1 cites its run.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-44` — the arm's `p.returncode != 0 -> FAIL` line and S1's refusal sentence, which S1 and S2 replace with the receipt-alone outcome rule (id 10)
- **hands-off** `TOOL-dFurnishedOrders-48` — the outcome rule under which unit 48's DEAD PROBE cases and its rule-image compare run their `apply --all` (ids 4, 15, 17, 34)
- **hands-off** `TOOL-dFurnishedOrders-52` — S1's receipt needle, S2's problem count and S3's budget input, which unit 52 S1, S3, S8 to S11, S22 and S23 settle (ids 1, 28, 6, 13, 27, 19, 14, 30 of the sixth audit)

## 4. Design

### The arm's outcome rule, after this unit

```
p := run("apply", "--target", t, "--all")
p.returncode == 0                                        -> read the receipt
p.returncode == 1 and "govkit apply — [11/RECEIPT]" in p.stdout
                                                         -> print "home parity: apply exit 1, <n> problem(s)
                                                            outside home parity: <entry ids>"; read the receipt
anything else, or no install.json under t/.governance    -> FAIL "home parity: apply exit <rc>" + stderr tail
... unit 44 S2's compare and S3's DEAD PROBE, unchanged here
print "home parity: <k> kit(s), <r> row(s) compared, apply <t>s"
```

### What the probe measured

A scratch target under `%TEMP%`, with `git init`, `core.autocrlf false` and one commit, carried a
`deploy.toml` setting `prefix = "scripts"`, `DEPLOY_FULL`'s five answers and no `kits` line, plus
`[kit.memory-recall]` `kit = "scripts/recall"`. The probe ran `python tools/govkit/govkit.py apply
--target <t> --all` at `e8b9b07c` (PINNED, 2026-10-27):

| reading | value |
|---|---|
| exit, wall time | 1, 20 s |
| final receipt line | `[11/RECEIPT] 383 row(s), 27 kit(s), schema 3` |
| adopter exits | 4: agent-instructions (2), process-monitor, playbook-render, unattended |
| `rendered` absent after its adopter | 14: review-harness 5, unattended 9 |
| gate-leg argv naming an absent file | 1: check-agent-cap-restatement |
| total | `19 problem(s)` |

The same target with `[answers]` `kit = "x"` exited 2 on `target_context`'s seeded-token refusal and
left no `install.json`. That is the refusal S1 still fails.

### What it does not check

- `apply`'s problems themselves. An adopter that starts failing for a new reason shows as a changed
  count on the printed line, and nothing reds on it here.
- An edit to an adopter script changes this arm's verdict only when it makes `apply` refuse or skip
  its final receipt write. Unit 48 S17 gives the guard those directories anyway.

### Inventory

Minted: the printed token `home parity: apply exit`. No function, flag or file.

### Migration

None: unit 44's arm has never run.

### Rollout

Live at landing, at order 9, after unit 44.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `tools/run-gates/selftest-budgets.txt`

### Alternatives rejected

- **Give the fixture what every adopter needs (the report's option b).** It needs a `kits` list,
  `PROCMON_ROOTS`, a project layer, a governing doc, the unattended renders and a waivers file. That is
  six coupling points to adopters the arm does not grade, each a future false red. It also widens
  what the arm's guard must cover (unit 48 S17) for no added parity evidence.
- **Tolerate only the three measured problem classes.** A fourth class reds the arm for a reason
  unrelated to home parity, which is this finding again. Unit 44 S2's compare in both directions already
  catches lost rows.
- **Narrow to `--kits`.** It grades the instances chosen, and unit 44 §4 chose `--all` to grade every
  kit added later.

## 5. Production-readiness checklist

- security — the arm writes only its scratch target under the suite's temp root.
- perf / scale — unchanged from unit 44: one `apply --all`, measured at 20 s; S3 prices it.
- error / empty / loading states — a refusal, a missing final receipt and an empty compare each fail
  by name.
- observability — S2 prints the tolerated count and the entry ids; S3 prints the apply's seconds.
- risks — a problem that drops rows without dropping a whole home passes this rule and is caught by
  unit 44 S2's `receipt-only` or `derived-only` line only when it moves a home.
- testing — AC1 to AC3 by probes; the arm of §7 at the close.
- migration — none.
- user docs — none: a selftest arm.

## 6. Acceptance criteria

- **AC1** — When the pass's probe runs `python tools/govkit/govkit.py apply --target <t> --all` into
  S1's scratch target and feeds its exit and stdout to the arm's outcome rule, the rule proceeds to the
  compare. It prints a `home parity: apply exit 1` line whose count equals the `govkit: <n>
  problem(s)` total `apply` printed, and names every entry id those problem lines quote
  (`agent-instructions`, `process-monitor` and `unattended` among them on 2026-10-27).
  Red when: the arm fails on an exit 1 whose problems are all outside home parity.
  figure: exit 1 and 19 problems are PINNED from the 2026-10-27 probe; the count compared is DERIVED
  from the run observed.
  fixture: a scratch target repository under `%TEMP%`, built by the pass.
  cost: one `apply --all`, about 20 s.
- **AC2** — When the same probe runs over a target whose `deploy.toml` adds `[answers]` `kit = "x"`,
  the rule fails naming `apply exit 2` and the seeded-token refusal. When the captured stdout of AC1's
  run has its `[11/RECEIPT]` line removed and is fed to the rule with exit 1, the rule fails naming
  the missing receipt line.
  Red when: the arm tolerates a refusal or an `apply` that never reached its final receipt.
  fixture: a second scratch target under `%TEMP%`.
- **AC3** — When `grep -n "^govkit selftest" tools/run-gates/selftest-budgets.txt` runs, the row's
  budget is at least `ceil(1.5 * (1065 + t))`, `t` the apply seconds the pass measured, and its note
  names `1065` and `t`.
  Red when: the arm's apply lands inside the leg with its cost unpriced.
  figure: 1065 is PINNED from the row's note; `t` is DERIVED at the pass and was 20 on 2026-10-27.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · unit 44's parity arm, moved to the receipt-alone outcome rule, staged by restoring `p.returncode != 0 -> FAIL` after deleting `tools/govkit/__pycache__` and running Python with `-B` · none

## 8. Open questions

- **F1 — Which `apply` outcome does the arm accept?** Options: (a) exit 0, or exit 1 with the final
  RECEIPT line, any problem tolerated and named; (b) a fixture giving every adopter what it needs,
  exit 0 required; (c) (a) restricted to the three measured problem classes. (b) couples the arm to six
  adopter inputs it does not grade, and (c) reds on a fourth class for the reason this finding names.
  RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the skeptic-judged option (a) of id 10, whose
  receipt-written premise this unit's probe re-measured. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The unit this one repairs is unbuilt.** `TOOL-dFurnishedOrders-44` is specced and unbuilt at
  `e8b9b07c`. RESOLVED (agent, 2026-10-27, delegated): the build run re-grounds on it at the pass and
  stops this unit if `check_receipt_home_parity` is still absent then, rung 1, the brief's rule for
  unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, id 10
  (HIGH, item H1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-52, promoted from the spec audit of the round-5 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-47-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: unit 44's `check_receipt_home_parity` and the suite's `run`
(`tools/govkit/selftest.py:220`); `step` and its reserved `STEPS` tuple (`tools/govkit/govkit.py:93-102`),
whose `[11/RECEIPT]` line is the one print `apply` makes after its final receipt write; and
`Report.emit` (`:1641-1649`), whose `govkit: ` lines the arm counts. `python
tools/codebase-map/reuse_lookup.py "accept an apply that exits non-zero for adopter problems while
reading its receipt"` ranked `read`, `read_text`, `adopt` and `read_descriptors`, name-token neighbours
none of which grades an apply outcome. A grep of `tools/govkit/selftest.py` for `[11/RECEIPT]` and
`its adopter exited` found no arm that tolerates an adopter exit, so no existing seam fits beyond
those named. The recall probe returned units 43 and 44, TOOL-dGroundRules-29 and DEPL-cMendedVintage-5
and -16, which grade `apply` through `classify_outcome` or a scratch target, none disagreeing with
source.

Recall terms used: `python tools/memory-recall/query.py "how does a selftest arm grade an apply whose
adopters fail in a scratch target" --terms "apply receipt adopter exit accepted stop classify outcome
scratch target selftest arm RECEIPT step"`
