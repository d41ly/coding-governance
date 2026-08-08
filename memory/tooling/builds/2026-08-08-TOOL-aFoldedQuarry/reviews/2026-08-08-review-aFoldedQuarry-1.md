# Review 1 — adversarial pass over the master spec and the U6 sub-spec

**Scope:** `spec/2026-08-08-spec-aFoldedQuarry-1.md` and
`spec/units/2026-08-08-spec-aFoldedQuarry-2-u6-indexed-join.md`, both at rev-1, before any code.
**Method:** read each claim as a hostile reader would, then RUN the ones that make a claim about a
tool's behaviour. Four of the six findings below could only be found by running something.

| # | Severity | Where | Finding |
|---|---|---|---|
| R1 | blocker | U6 §6 AC7 | `node --check` is a vacuous gate on this file |
| R2 | high | U6 §2 S5 | an identical repeat verdict is not a conflict |
| R3 | high | U6 §2 S8 | the ban gate matches its own source |
| R4 | medium | master §2 S1 vs U6 §2 S8 | the two specs scope the ban differently |
| R5 | medium | U6 §2 S7 | the `judged === 0` early return contradicts S7 |
| R6 | low | U6 §2 S9 | the version bump has a machine-checked format |

## R1 — `node --check` exits 0 on a genuine syntax error here (blocker)

AC7 proposed `node --check tools/workflows/tier2-review.js` as the syntax gate. Measured on
node v24.16.0:

```
$ printf 'export const x=1\nlet y=(\n' > probe.js && node --check probe.js ; echo $?
0
```

Node's automatic module detection retries the parse and the failure is swallowed, so the gate would
have been green on every input including a truncated file. That is the exact "green by absence"
shape this repo already bans elsewhere, and it would have shipped as an acceptance criterion.

The dialect is also neither CommonJS nor a module: the harness uses `export const meta`, top-level
`await` AND top-level `return`. No standard parser mode accepts all three. What does accept them is
the shape the Workflow runtime itself uses — an async function body. Verified:

```
AsyncFunction = Object.getPrototypeOf(async function(){}).constructor
new AsyncFunction('args','agent','parallel','phase','log',src.replace(/^export\s+(const|…)\b/gm,'$1'))
```

Green on the real harness and on a top-level-await-plus-return fixture, RED with
`SyntaxError: Unexpected token '}'` on the truncated fixture. AC7 is rewritten against this probe,
which becomes `tools/workflows/check-workflow-syntax.js`.

## R2 — a repeated verdict that AGREES is not a conflict (high)

S5 demoted any id receiving a second verdict to unverified. A skeptic that lists a finding twice
with the same verdict is not ambiguous, and demoting it discards a real adjudication and inflates
the unverified count — which then reads as harness degradation in the report. Only a repeat whose
`verdict` token DIFFERS is a genuine conflict. Split the two: an identical repeat is idempotent and
counted as a duplicate; a disagreeing repeat demotes to unverified and is logged with its id.

## R3 — the ban gate would fail on itself (high)

S8's gate must hold the banned pattern verbatim in order to search for it. Scanning `tools/` without
excluding the gate's own source and its test file means the gate reds on a clean tree from the first
run. This is the upstream "exclude the pin from its own scan" lesson arriving one unit early; the
population is `tools/**/*.js` MINUS the gate script and its fixture-bearing test.

## R4 — the two specs disagree on the ban's scope (medium)

Master §2 S1 says the ban covers `tools/`; U6 §2 S8 says `tools/workflows/`. A sub-spec that
contradicts its master is a defect regardless of which is right. The wider reading is also the
correct one — `tools/hooks/agent-cap.js` is JavaScript under `tools/` and nothing stops a future
join from being written there — so both move to `tools/**/*.js`.

## R5 — the `judged === 0` early return drops the report S7 promises (medium)

The harness returns early at `:224` when nothing was judged. S7 says synthesis runs when
`confirmed + unverified > 0` and carries unverified findings as outstanding. With the early return
in place, the single most degraded run — findings raised, no verdicts at all — is exactly the run
that produces NO report, which is when a written list of outstanding findings is worth most. Remove
that early return and let one `needsReport` test govern; its note text survives in the final return.

## R6 — the version bump is format-checked (low)

`tools/check-kit-versions.sh:24` asserts `version: '<X>.<Y>'` in the harness. The bump in S9 must
keep the two-part shape or that leg reds. Noted so the build does not discover it from a red bar.

## Disposition

All six folded into rev-2 of both specs before any code was written. R1 additionally adds a kit file
(`tools/workflows/check-workflow-syntax.js`) that the rev-1 inventory did not list.
