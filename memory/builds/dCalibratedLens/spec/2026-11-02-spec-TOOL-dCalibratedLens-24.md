# TOOL-dCalibratedLens-24 — the stage receiver judged by the hook over a real payload, green on the shipped harness and red on a looped copy

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 17 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-24-deviation-241.md](../build/2026-11-02-build-TOOL-dCalibratedLens-24-deviation-241.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 16, HIGH, item H6 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`). Unit 1's AC3 runs
`node tools/hooks/agent-cap.js --only=scripts` with no stdin payload. The hook parses a PreToolUse
JSON payload from stdin and exits 0 on a parse failure or a tool other than Workflow or Agent
(`tools/hooks/agent-cap.js:1853-1858`), so the criterion passes before the unit is built and cannot red
on the seven-literal receiver S1 adds; unit 1's §4 evidence bullet cites the same bare command for
TOOL-dFairHearing-2's measurement. This unit makes the observation feed the harness to the hook, and
adds the red twin that shows the observation can fail. It repairs `TOOL-dCalibratedLens-1`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 1's text (rev-2, its §4
  "Amendments (round-1 spec audit)", id 16): AC3 builds the payload `{"tool_name": "Workflow",
  "tool_input": {"script": <the rendered tools/workflows/tier2-review.js>}}` with `node -e`, as
  `tools/workflows/check-verifier-fanout.sh:321-326` builds it, pipes it to `node
  tools/hooks/agent-cap.js --only=scripts` and expects exit 0; and the §4 evidence bullet states that a
  bare invocation reads no harness and measures nothing. Observed by AC1.
- **S2** — The observation over the built harness, at this unit's order: the AC3 payload over the
  shipped render exits 0. Observed by AC2.
- **S3** — The red twin, an arm of `tools/workflows/tier2-review.test.sh`: a scratch copy of the
  rendered harness whose stage receiver is rewritten to `boundedParallel(PLAN_LENSES.map((f) => () =>
  agent(f)), 5)`, fed the same payload, exits 2 and prints the hook's `spawns one agent per item` line;
  the shipped render, fed the same way, exits 0. The arm raises the suite's `FLOOR_ASSERTIONS` by the
  two assertions it adds. Observed by AC3.

## 3. Non-goals (OUT)

- Changing the receiver. Unit 1 S1 is built as written; this unit observes whether the hook admits it,
  and a red here is unit 1's defect, fixed in unit 1's code by the main loop.
- The `scriptPath` payload form the review also names. The inline-script form is the one the bar's
  own fan-out leg already uses, so the observation and the leg judge the same bytes.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-1` — the rendered `tools/workflows/tier2-review.js` carrying the four stage literals and their receiver; without it there is no receiver to judge

## 4. Design

### Evidence

- `tools/hooks/agent-cap.js:1853-1858` at base: `JSON.parse(readStdin())` in a `try`, `process.exit(0)`
  on a throw, and `process.exit(0)` when `tool_name` is neither `Workflow` nor `Agent`.
- `tools/workflows/check-verifier-fanout.sh:321-326` at base builds `{tool_name: "Workflow",
  tool_input: {script: <file text>}}` with `node -e` and pipes it to the hook under `--only=scripts`.
- `tools/hooks/agent-cap.test.sh:2325` at base denies `boundedParallel(all.map((f) => () => agent(f)),
  5)` under `--only=scripts` with `spawns one agent per item`: the deny the red twin stages.

### The observation

```bash
node -e 'process.stdout.write(JSON.stringify({tool_name:"Workflow",tool_input:{script:require("fs").readFileSync(process.argv[1],"utf8")}}))' tools/workflows/tier2-review.js \
  | node tools/hooks/agent-cap.js --only=scripts
```

### Inventory

None minted: the arm is a case of an existing suite.

### Files touched (estimate)

- `tools/workflows/tier2-review.test.sh` — S3, the arm and its floor

### Alternatives rejected

- **`echo '{}' |` as the payload.** The skeptic measured it: exit 0, because `{}` names no tool.
- **Relying on unit 1's AC2 alone.** `check-verifier-fanout.sh` does feed the script, but it exits 1 for
  any denial across every workflow script; the twin names this receiver's denial.

## 5. Production-readiness checklist

- security — the hook is unchanged; the arm runs it read-only over a scratch copy.
- perf / scale — two hook runs, under a second each.
- error / empty / loading states — a payload the hook cannot parse would exit 0; the twin's exit 2 is
  what proves the payload reached rule 2.
- observability — the hook's denial line names the rule.
- risks — none beyond the receiver's own: a denied receiver stops every review, which AC2 catches
  before the close.
- testing — the arm of S3, observed RED and GREEN by the main loop.
- migration — N/A.
- user docs — N/A: no help page names the hook's payload.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'tool_input' memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-1.md`
  runs, it prints amended AC3's payload.
  Red when: AC3 still runs the hook with no stdin.
- **AC2** — When the command of §4 "The observation" runs after unit 1's pass, feeding
  `tools/workflows/tier2-review.js` to `node tools/hooks/agent-cap.js --only=scripts`, it exits 0.
  Red when: the hook denies the shipped receiver.
- **AC3** — When the same command runs over the scratch copy of S3, it exits 2 and its stderr carries
  `spawns one agent per item`.
  Red when: the looped receiver passes, so the observation could never red.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out` · `agent-cap self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC2 AC3 · the shipped render and a looped-receiver copy fed to the hook under `--only=scripts`, staged red by the copy · FLOOR_ASSERTIONS raised by the two assertions added

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 16 (HIGH, item H6) of the round-1 spec audit;
  unit 1 amended at the disposal (its rev-2).

## 10. Reuse audit

The seam extended is the payload `tools/workflows/check-verifier-fanout.sh:321-326` already builds, and
the deny case `tools/hooks/agent-cap.test.sh:2325` already asserts, both read at base. `python
tools/codebase-map/reuse_lookup.py "isolate each reader so one failure becomes an unread line, never
the walk's exit"`, run once for the set, ranked name stems only; the two files above were read by hand
and are the seam. The recall probe returned TOOL-cMendedVintage-19, the placement ruling this unit's
order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
