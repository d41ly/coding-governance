---
name: drift-audit
description: Measure whether this repo's records still describe reality, and optionally hunt dead / unwired / duplicated code. Use when the build "feels" like it is drifting, when the project's state is unclear, before a big planning session, or when you want to know whether a green gate actually means anything. Three cost tiers — Tier 0 is seconds and no agents, so run that first and always. Do NOT use for reviewing a diff; that is a code-review skill.
---

# Drift audit

Answers one question: **do this repo's own records still describe reality?** — and, at higher tiers,
is there dead, unwired, or duplicated code.

Rendered from `tools/drift-audit/SKILL.template.md` by `adopt-drift-audit.sh`. Edit the template, re-render;
a hand-edited copy reds the `--check` arm.

---

## Run Tier 0 first. Always. It is seconds, and it needs no agents.

```bash
python tools/drift-audit/drift_report.py
```

```
python tools/drift-audit/drift_report.py --json     # full detail per signal
python tools/drift-audit/drift_report.py --check    # exit 1 if a gateable signal is over its pin
```

The signals, stdlib and git only, no cache:

| Signal | Asks |
|---|---|
| `ledger_rows_contradicting_git` | does an in-flight row claim "not merged" about a landed sha? |
| `non_terminal_specs_cited_by_product_source` | does a SPECCED/INPROGRESS spec describe shipped work? |
| `shrink_only_lists_not_shrinking` | are the lists that promise to shrink actually shrinking? |
| `handkept_inventories_disagreeing_with_source` | does a hand-kept list still match what generates it? |
| `dangling_pointers_in_own_ledger` | do this node's own rows point at worktrees that exist? |
| `closed_specs_with_no_product_commit` | does a CLOSED spec have a commit that names it and changed the product? |

**Read the `status` column, not just the value.** A signal that cannot move prints `DEAD PROBE` and
its number means nothing. That column exists because the upstream adopter's convergence tool shipped
a `collision_flags` signal structurally incapable of being non-zero, and every reader took the 0 as
"converged" for thirteen days.

Gateable signals carry a **shrink-only pin** in `tools/drift-audit/drift_signals.py`, seeded at measured
values. Over the pin is a regression. At the pin means "still owed, drain it". Lower a pin whenever
its population drops.

Signals are declared where they belong: the five implementations are the kit's; `PRODUCT_GLOBS`,
`SHRINK_ONLY`, `HANDKEPT` and `PINS` are this repo's, in `drift_signals.py`. The corpus root comes
from `.memory-tree.conf` — there is deliberately no second place to state it.

**In the audit that produced this kit, Tier 0 alone produced the blocker, the vacuous-metric lead and
the entire work-state answer.** The 22 agents of Tier 2 deepened those and added the code-level
findings. They did not originate the most consequential ones. That is the whole argument for tiering.

---

## Tier 1 — targeted, one wave, ≤5 agents

Use when Tier 0 moved a signal and you want to know *why*, or when you suspect a specific instrument
is blind. Not for open-ended discovery.

Run the `drift-audit-state` workflow with its lens list narrowed to the signal that moved, plus the
standing instrument-integrity lens — that one earns its keep on every run.

---

## Tier 2 — full adversarial, two waves, ~22 agents

Use when the question is "is there dead / unwired / duplicated code", or after a long unattended
build wave. This is a deliberate spend; say so before starting it.

```
tools/workflows/drift-audit-code.js     # dead · unwired · duplication · inefficiency · instruments
tools/workflows/drift-audit-state.js    # records · charter · work-state · record-gate integrity
```

Run them **sequentially**, not together — the concurrency cap is fleet-wide, not per-workflow.
Both scripts take an `args` object; set `repo`, `base`, and the by-design priming (see below).

---

## Harness invariants — do not re-derive these, each was paid for

1. **Verdicts join on an orchestrator-assigned INTEGER id.** A ref-string key silently matched
   nothing twice, reported `precision 0.00`, and hid 14 real findings including 2 blockers. `0.00`
   reads like a clean bill of health. It is not.
2. **A finding with no verdict is UNVERIFIED — never refuted.** Count verdicts back and report the
   gap explicitly, even when it is zero. The absence is the point.
3. **Cap verify agents by TOTAL, not just concurrency.** Batch size grows with finding count; agent
   count never does. Route all fan-out through a bounded helper — concurrency is not a budget.
4. **The orchestrator independently re-verifies every headline claim.** In the founding run a finder
   said a regex damaged 2 files, its skeptic said 13, and direct measurement said **24**. Both agent
   tiers understated it.
5. **Precision 1.00 with zero refutations is a smell.** It means nothing was fabricated, not that the
   severities were right. Report the correction direction beside it: that run's was 20 of 22
   downgrades and zero upgrades.
6. **Label every heuristic you hand an agent with its known failure mode.** A "99 suspect-stale
   specs" heuristic was passed as a lead to re-derive, explicitly not as a finding. It landed at 43.
7. **Long prose goes to a file; agents return `{path, summary}` with forward-slash paths.** A
   backslash in hand-serialized JSON is the top output-token waste in a workflow transcript.
8. **Read the run journal before believing a hard zero.** It holds each agent's actual return value.

---

## Priming — precision collapses without it

Every finder prompt must carry the by-design set, or agents re-report known debt as new findings:

- the OPEN backlog rows for the area under audit (derive them at run time; do not hand-keep a list);
- any already-recorded duplication or dead-code findings from prior audits;
- the known false-positive classes for whatever metric you are quoting.

---

## What this audit structurally cannot see

Say these out loud in the report rather than letting silence read as absence:

- **Other nodes' local state.** Their *landed* work is visible; working trees, unpushed branches and
  worktrees are not.
- **Anything in a separate repo or submodule**, which has its own ledger and its own drift.
- **Whether a human obligation was met.** "Was the security review done?" has no oracle in the tree.
