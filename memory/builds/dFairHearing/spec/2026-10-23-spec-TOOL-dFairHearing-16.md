# TOOL-dFairHearing-16 — agent-cap's review rules moved to the review kit, each seen red at its new home before the hook stops carrying it

**Status:** INPROGRESS · rev-6 · 2026-11-03 · node d · Tier-2 · base 3708a705 · streams tooling · order 11 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0083@bd47ee4e whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-16-deviation-169.md](../build/2026-10-23-build-TOOL-dFairHearing-16-deviation-169.md) | deviation | — |
| [2026-11-03-build-TOOL-dFairHearing-16-1-builder-return.md](../build/2026-11-03-build-TOOL-dFairHearing-16-1-builder-return.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-departures-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-3 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-30 TOOL-dFairHearing-32 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-mark-rewrap-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-mark-rewrap-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-23 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-11-02-prompt-TOOL-dFairHearing-16-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFairHearing-16-build-brief.md) | research | — |
| [2026-11-03-prompt-TOOL-dFairHearing-16-1-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-16-1-spec-writer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dFairHearing-16-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-16-fix-brief.md) | research | TOOL-dFairHearing-22 TOOL-dFairHearing-26 TOOL-dFairHearing-28 TOOL-dFairHearing-29 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js` retires (the night pass two's point 7, the owner's NT-27), and three of its
rules are the review kit's, not a fan-out guard's. This unit moves them there: the verifier total and
the loop markers to the merge bar's harness check, the ref-keyed join ban to `check-review-join.sh`
alone, and the spec-audit opt-in to a review-kit pack on Workflow calls. Each is seen red on its
planted case at its new home before agent-cap stops carrying it, so no rule is unguarded for a
commit.

## 2. Scope (IN)

- **S1** — The shared readers stay one copy. `tools/hooks/agent-cap.js` exports the helpers two homes
  reach, and runs `main()` only when it is the entry point (`require.main === module`), the idiom
  `tools/hooks/scratch-guard.js` already uses. Two homes reach a helper when a moved rule and a
  remaining rule both call it, as rules 0 and 6 call `extractWorkflowArgs` and `extractBuildSlug`.
  They reach it too when two moved rules with different homes call it, as rules 2 and 5 call
  `runBothViews` and `resolveHarnessName`; the three views a moved rule calls (`renderCodeView`,
  `renderStrippedView` and `renderBlankedLiterals`) stay with `runBothViews`, because each reads the
  view mode it switches. And they reach it when a reader outside the hook
  reads it there, as `tools/check-playbook-parity.sh` reads `MAX_VERIFIERS` and `MAX_LENSES` from the
  hook's source. `readWriterBound` stays and is exported because the policy-kit path it reads,
  `POLICY_HELPER`, is rule 7's too, so the policy kit is probed from one place. A helper only a moved
  rule reaches moves with that rule. §4 Evidence holds the measurement. Observed by AC1.
- **S2** — The verifier total and the loop markers. The review kit's `check-verifier-fanout.js`, beside
  `tools/workflows/check-verifier-fanout.sh`, holds rule 2 whole: `fanoutFindings` with the receivers it
  admits, its three markers (`gov:fixed-verifiers`, `gov:fixed-writers` and `gov:sequential-agents`),
  the one-marked-loop sweep and the deny message `main()` prints for it, evaluated through agent-cap's
  exported `runBothViews`. A verifier split is judged against the exported `MAX_VERIFIERS`, and a
  writer split against the bound the exported `readWriterBound` reads at the process's own working
  directory, where the hook's `--only=scripts` read it. The gate runs it on every harness in place of
  the hook's `--only=scripts`, passing the hook path it already resolves as `--hook`. That mode runs
  rules 2 and 5 alone, so once both have left it runs nothing (S3). Rule 5, which it also ran per
  harness, then runs from `check-review-join.sh` alone, as the clause says. `MAX_LENSES` stays in the
  hook by S1, until TOOL-dFairHearing-23's `LENS_SLOTS` takes its place; the exact slot count that
  TOOL-dFairHearing-13's native arm holds stays its own. Seen red at its new home by AC2, and agent-cap
  stops carrying it by AC3.
- **S3** — The ref-keyed join ban, and the selector it leaves empty. The review kit's
  `check-review-join.js`, beside `tools/workflows/check-review-join.sh`, holds `scanJoinFindings`, its
  ban table and its deny message, and the gate runs it where it ran the hook's `--only=join`, passing
  the hook path it already resolves as `--hook`. The gate's self-exclusion drops `agent-cap.js`, which
  no longer holds the table. Once rules 2 and 5 have left, the hook's `--only=` selector, its
  `ONLY_RULES` set and its script read feed no rule, and all three leave the hook (§8 F7). Every
  argument opening `--only=` is then refused, exit 2, before stdin is read, naming
  `check-verifier-fanout.js` and `check-review-join.js` as where the script rules run. Seen red at its
  new home by AC4, and the hook's rule 5 and selector gone by AC5.
  **Readers:** by name: `tools/workflows/check-verifier-fanout.sh`, `tools/workflows/check-review-join.sh`,
  `tools/policy/check_policy.py`, `tools/hooks/README.md`, `tools/check-wiring.sh`,
  `tools/check-wiring.test.sh`, `tools/hooks/agent-cap.test.sh`, `memory/map/features/agent-cap.md`,
  `memory/map/features/review-harnesses.md`. by value: `tools/check-wiring.sh`, which reds a wired
  agent-cap command carrying any `--only` and keeps doing so; its message, that the flag runs one rule
  and disables the rest, is rewritten to say the hook now refuses every call carrying it.
- **S4** — The spec-audit opt-in pack. The review kit's `spec-audit-optin.js` is a `PreToolUse` hook on
  `Workflow` calls holding rule 0 whole: `checkSpecAuditDeclared`, `readSpecAuditDefault` and
  `NO_AUDIT_PHASES`. It reads `extractWorkflowArgs` and `extractBuildSlug` from agent-cap's exports
  and `readFrontMatterKey` and `readConfKey` from `scratch-guard.js`, both probed in the hooks kit
  beside the review kit. A spec-audit call, or one carrying `specAudit`, that it cannot load those
  readers for is denied by name; every other call is admitted. Its fragment,
  `spec-audit-optin.fragment.json`, declares the event, the `Workflow` matcher, the marker and the hook
  path, and `.claude/settings.json` wires it through `tools/settings-merge.py --fragment`. Seen red at
  its new home by AC6, and agent-cap stops carrying it by AC7.
- **S5** — The suites follow their rules. The arms of `tools/hooks/agent-cap.test.sh` over rules 0, 2
  and 5 move to `tools/workflows/check-verifier-fanout.test.sh`,
  `tools/workflows/check-review-join.test.sh` and a new `spec-audit-optin.test.sh`. They include the
  arms that reach a moved rule's verdict under no rule label: the `msg` arms, the view arms and the
  base-versus-now property arm, whose current side becomes the two `.js` homes. The two rule-5 arms
  that pass a selector move under their labels and base verdicts, run against
  `check-review-join.js`. The hook's suite gains one arm per moved rule asserting it now admits that
  rule's planted case, one arm asserting every `--only=` argument refuses, and the export arm; the
  refusal arm replaces the four rule-6 arms run under a selector. No arm left in the hook's suite
  carries a `rule0`, `rule2` or `rule5` label. Two fixtures of `tools/policy/check_policy.py` follow:
  `limit-hook-writer-split` runs `check-verifier-fanout.js --hook` over its hook copy where it ran
  `--only=scripts`, and the rule-2 and rule-5 rows of `limit-hook-rules-kept` expect the hook to admit,
  as its rows for rules 1 and 3 already do. `tools/gate-legs.json` gains the leg
  `spec-audit opt-in pack self-test`, and `tools/workflows/kit.toml` withholds the new suite as it
  withholds its siblings and pins the fragment's line endings. Observed by AC8.
- **S6** — The wiring check. `tools/check-wiring.sh` grades the pack's fragment as it grades the hooks
  kit's: the scratch arm's per-fragment grading becomes one function both arms call, and
  `tools/check-wiring.test.sh` gains the pack's unwired case. Observed by AC9.
- **S7** — The kits' records. `tools/hooks/README.md` and `tools/workflows/README.md` say where each
  moved rule lives and how to run it, and the hooks README's section on running one rule says every
  `--only=` now refuses. The default-install table of `WIRE-INTO-PROJECT.md` gains the pack's row;
  the dossiers `memory/map/features/agent-cap.md` and `memory/map/features/review-harnesses.md` claim
  the three new files and the new leg. Observed by AC10 and AC11.

## 3. Non-goals (OUT)

- Rules 6 and 7, which judge the call rather than the script, and stay in the hook.
- The `gov:bounded-fanout` marker. Rule 3 read it and retired with TOOL-dGroundRules-10, and no rule of
  the hook reads it at `8b2b995f` (section 8 F2).
- A version bump. The lander's `govkit.py mint` dates every kit whose shipped bytes moved, so a branch
  owes none, and no earlier unit of this build moved a version on its branch. At the pass's starting
  commit `8b2b995f`, agent-cap reads 1.42 and review-harness 1.56, each minted by another build's
  landing (§4 Evidence).
- The lens count as an exact slot count, TOOL-dFairHearing-13's native arm in the same gate.
- Retiring `tools/hooks/agent-cap.js` and moving its exported helpers to their last home, dBoundRoles'.
- The review protocol's statement of where each rule lives, which TOOL-dFairHearing-10 brings in line.
- A check of inline Workflow scripts' verifier total at the tool call. NT-27 moves the rule to the
  merge bar's harness check, and the harness's own concurrency settings bound an inline script.

### Edges

- **consumes-from** `TOOL-dFairHearing-13` — the native slot arm in the `verifier fan-out` leg, beside which the moved rules land in the same gate; without it the gate's header and clean line this unit extends are today's
- **hands-off** `TOOL-dFairHearing-10` — the review protocol's enforcement and predicate sections, rewritten to name where each moved rule now lives
- **hands-off** external — dBoundRoles retires agent-cap and moves the helpers this unit exports; dGroundRules, which retired rules 1, 3 and 4 and the slot ledger, has landed
- **hands-off** `TOOL-dFairHearing-22` — finding id 40 (item H3) of the round-1 spec audit: the hook denies a spec-audit call while `spec-audit-optin.js` is not beside it, so a partial `govkit update` cannot fail open as §4 Rollout prices it
- **hands-off** `TOOL-dFairHearing-23` — finding ids 6, 10, 20, 29, 30, 31 and 33 of the round-1 spec audit: the version half of S7 and AC11, which rev-6 dropped once the lander's mint had landed (its S12, S13, AC6), AC8's grep half replaced by counting the moved arms (its S16, AC9), `MAX_LENSES`'s home taken by `LENS_SLOTS` (its S42, AC33), the new leg's registry, budget and foreign-prefix rows (its S26, AC17), the fixtures copying `check-verifier-fanout.js` (its S27, AC18) and the kickoff manifest re-stamp after the gate-legs.json edit (its S28, AC19)
- **hands-off** `TOOL-dFairHearing-26` — finding id 10 (item H2) of the spec audit of units 20 to 23: every rule 0 and rule 5 arm counted by label at its new suite and gone from the hook's, any arm left behind moved (its S1 to S3, AC1 to AC3)
- **hands-off** `TOOL-dFairHearing-32` — findings ids 12, 17 and 37 of the round-3 spec audit: the hook finds this unit's opt-in pack, `spec-audit-optin.js`, through one port of `resolve_kit_dir` held to the canonical by a truth table (its S25 to S27)
- **hands-off** `TOOL-dFairHearing-36` — finding id 24 of the round-4 spec audit: the leg this unit adds runs the pack's suite that receives units 28 and 29's moved arms, and that unit names it and reads its argv


## 4. Design

### Evidence

Measured at `8b2b995f` on 2026-11-03, PINNED; rev-5 measured base `3708a705`, and the hook has moved
since.

- dGroundRules landed between the two (TOOL-dGroundRules-10, -18, -21, -61, -73 and -78, merged at
  `e6dd731b5`). It retired rules 1, 3 and 4, the slot ledger, `FANOUT_CAP`, `--print-cap`, the
  `AGENT_CAP` refusal, `EFFECTIVE_CAP` and `loadDeclaredCap`:
  `grep -c "loadDeclaredCap\|EFFECTIVE_CAP\|FANOUT_CAP\|print-cap" tools/hooks/agent-cap.js` prints 0.
  The hook, 2008 lines, keeps rules 6, 7, 0, 2 and 5, in that order (`tools/hooks/agent-cap.js:11-12`),
  and exports nothing.
- Rule 2 is `fanoutFindings` (:748-1225) with its markers (:455, :464, :487), `MAX_VERIFIERS` (:456),
  the lens allowance `MAX_LENSES` (:461) and `readWriterBound` (:466-471). Rule 5 is
  `scanJoinFindings` with its ban table (:1346-1389). Rule 0 is `checkSpecAuditDeclared` and its
  helpers (:1448-1605). `main()` (:1832-1973) holds the selector (:1842-1850), rules 6 and 7
  (:1861-1902), rule 0 (:1907-1917), the script read (:1919-1937), rule 2 with its deny message
  (:1939-1955) and rule 5 with its own (:1957-1970), and calls itself unguarded at :1975.
- Measured by call site over the file, comments dropped, by a scratch script:

| Helper | Reached by | Here |
|---|---|---|
| `extractWorkflowArgs`, `extractBuildSlug` | rule 0, and rule 6's `checkHarnessCall` and `checkHandoffSpawn` | stay, exported |
| `runBothViews`, `resolveHarnessName` | rules 2 and 5 | stay, exported (F3) |
| `renderCodeView`, `renderStrippedView`, `renderBlankedLiterals` | rule 2, rules 2 and 5, and rule 5, each reading the view mode `runBothViews` switches | stay, exported (F3) |
| `MAX_VERIFIERS`, `MAX_LENSES` | rule 2, and `tools/check-playbook-parity.sh:392-394` by source line | stay, exported |
| `readWriterBound` | rule 2; its `POLICY_HELPER` (:465) is rule 7's too (:1782) | stays, exported |
| `boundedK`, `intConsts`, `parseBranches`, `boundedBranch`, `joinCall`, `topLevelArgs`, the markers | rule 2 alone | move with rule 2 |
| `renderPerLineBlanked`, the ban table | rule 5 alone | move with rule 5 |
| `readSpecAuditDefault`, `NO_AUDIT_PHASES` | rule 0 alone | move with rule 0 |

- Every view reads `VIEW_MODE` (:365), directly or through a callee, and `runBothViews` switches it
  (:410-418), so the views and `runBothViews` stay in one module.
- `tools/workflows/check-verifier-fanout.sh` resolves the hook (:263-273), delegates with
  `--only=scripts` (:325-333), and its self-exclusion already names a `check-verifier-fanout.js`
  (:280). `check-review-join.sh` resolves the hook (:296-306), delegates with `--only=join` (:365),
  and its self-exclusion names `check-review-join.js` and `agent-cap.js` (:38).
- `--only=scripts` runs rules 2 and 5 and `--only=join` rule 5 (:1939-1970); both skip rules 6, 7 and
  0, and the script read feeds rules 2 and 5 alone. The other callers of the selector are
  `tools/policy/check_policy.py`'s fixture `limit-hook-writer-split` (:3016-3033, described at :123)
  and the hook's suite: two rule-5 arms (`tools/hooks/agent-cap.test.sh:489`, :495), four rule-6 arms
  (:2319-2325) and the property arm's base side (:2040). `limit-hook-rules-kept` (:2946-2957) asserts
  the hook denies a verifier per finding and a ref-keyed join. `tools/check-wiring.sh:992-996` reds a
  wired agent-cap command carrying any `--only`, and `tools/check-wiring.test.sh:446-460` stages it.
- Rule 7 refuses a payload `cwd` in no checkout wherever `policy-mirror.js` sits beside the hooks
  kit (`tools/hooks/agent-cap.js:1782-1785`), so the hook's suite runs a copy beside `scratch-guard.js`
  and no policy kit (`tools/hooks/agent-cap.test.sh:34-39`).
- The hooks kit's fragment idiom: `tools/hooks/scratch-guard.fragment.json` names `event`, `matcher`,
  `marker` and `hook_path` with a `{kit}` token, and govkit wires every landed `*.fragment.json`
  through the target's `settings-merge.py` (`run_fragment_merges`, `tools/govkit/govkit.py:5894-5935`).
- The scratch arm of `tools/check-wiring.sh` (`check_scratch_guard`, :1028-1087) grades every fragment
  in the directory the hooks kit's fragment was found in (:1044), so a fragment in the review kit's
  directory is graded by no arm today.
- Versions: agent-cap 1.42 (`tools/hooks/agent-cap.js:85`) and review-harness 1.56
  (`tools/workflows/tier2-review.template.js:3`). Along the first-parent line from `3708a705`, each
  moved only at another build's landing merge, `3c0318d95`, `3ada42ab1` and `30396a422`. The epoch
  leg's own text puts the bump at the lander and owes a branch none
  (`tools/govkit/govkit.py:13845-13850`).
- `help/agent-limit.md` names the hook's `MAX_VERIFIERS` (:11) and rule 7 as what the hook refuses
  (:49-60); no page under `help/` names rule 0, 2 or 5.

### The order inside the pass

For each of the three rules, in this order: the new home lands with its arms; the pass observes the
new home red on the planted case and green on the shipped harnesses; only then does it delete the rule
from the hook and observe the hook admitting the same case. The pass's acceptance ledger records both
observations per rule. A rule is never absent from both homes at a commit, and never in both at the
pass's commit. The selector and the script read leave last, once rules 2 and 5 have both left and
both gates run their `.js` homes (§8 F7).

### The three homes

| Rule | New home | Runs from | Planted case |
|---|---|---|---|
| verifier total and loop markers | `check-verifier-fanout.js` | `check-verifier-fanout.sh`, per harness, with `--hook <path>` | a verify fan over `chunk(all, 1) // gov:fixed-verifiers`, and two `gov:sequential-agents(5)` loops |
| ref-keyed join ban | `check-review-join.js` | `check-review-join.sh`, per script | a verdict join keyed `verdictByRef` |
| spec-audit opt-in | `spec-audit-optin.js` | the `PreToolUse` wiring, on `Workflow` | a `kind: "spec-audit"` call whose build README carries no `spec-audit:` date |

Each `.js` home is a CLI as well as a module: given files, `check-verifier-fanout.js` and
`check-review-join.js` print each finding as the hook printed it and exit 1 on a finding, 0 clean,
and 2 when they cannot load agent-cap's exports or read a file. Each deny message keeps its bytes,
because the moved arms assert them.

### Files touched (estimate)

- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`
- `tools/workflows/check-verifier-fanout.js` (new)
- `tools/workflows/check-verifier-fanout.sh`
- `tools/workflows/check-verifier-fanout.test.sh`
- `tools/workflows/check-review-join.js` (new)
- `tools/workflows/check-review-join.sh`
- `tools/workflows/check-review-join.test.sh`
- `tools/workflows/spec-audit-optin.js` (new)
- `tools/workflows/spec-audit-optin.fragment.json` (new)
- `tools/workflows/spec-audit-optin.test.sh` (new)
- `tools/workflows/kit.toml`
- `tools/workflows/README.md`
- `tools/policy/check_policy.py`
- `tools/gate-legs.json`
- `tools/check-wiring.sh`
- `tools/check-wiring.test.sh`
- `.claude/settings.json`
- `WIRE-INTO-PROJECT.md`
- `memory/map/features/agent-cap.md`
- `memory/map/features/review-harnesses.md`

### Rollout

Live. In this repository the pack is wired in the same commit that removes rule 0 from the hook, so
the opt-in is never unenforced here. An adopter's `govkit update` lands the fragment and wires it
before its checks run; `check-wiring.sh` reports the pack UNWIRED in a tree that unwired it. A
session started before the wiring reads the new hook once the settings watcher catches the edit
(`memory/gotchas/settings-edit-takes-effect-mid-session.md`).

### Alternatives rejected

- **Copying the lexer into the review kit.** Rules 2 and 5 both read the views and land in two
  files, so a copy per home is two scanners of one script, the drift TOOL-aBatchedTribunal-1d ruled
  out; moving the views is their last move, dBoundRoles' (section 8 F3).
- **Keeping `--only=scripts` as the selector's one member.** It would read a script and run no rule,
  so the fan-out gate's call to it could never go red (section 8 F7).
- **The join ban as awk inside the shell gate.** The awk the hook replaced matched inside string
  contents and missed `${...}` interpolations; the hook's view narrowed both, measured by the suite's
  fixtures (section 8 F5).
- **A third hand-written wiring arm.** The scratch arm already grades fragments; a copy would grade one
  fragment two ways (section 8 F6).

## 5. Production-readiness checklist

- security — the spec-audit opt-in keeps fail-closed for its kind: an unreadable README, an unplaceable
  call and a missing reader all deny, as rule 0 did, and the pack is wired before the hook stops
  carrying the rule. The verifier total is no longer checked at the tool call for an inline script,
  the owner's NT-27 ruling, and stays checked on every committed harness at the merge bar.
- perf / scale — one more node process per `Workflow` call for the pack; the two gates start one node
  process per script as they did.
- error / empty / loading states — each home exits 2 naming the missing export or file rather than
  passing; each gate keeps its empty-population refusal.
- observability — each deny message keeps its bytes; the wiring check names the pack by its fragment.
- risks — a tree that lands the review kit without the hooks kit has no reader to load, and the pack
  then denies every spec audit; the review kit already requires the agent-cap kit
  (`tools/workflows/kit.toml`, `requires`). A review-kit gate older than its hook, after an update
  naming the hooks kit alone, still calls `--only=` and now reds naming the two homes, rather than
  passing every harness with rule 2 run nowhere (§8 F7).
- testing — AC1 to AC11 as direct runs of each home and of a copy of the hook over planted
  fixtures; the moved and new arms under section 7.
- migration — an adopter's update wires the pack through govkit; a hand copy runs
  `settings-merge.py --fragment` on it, as the runbook row says.
- user docs — `tools/hooks/README.md`, `tools/workflows/README.md` and the runbook's default-install
  table. No page under `help/` names rule 0, 2 or 5, and `help/agent-limit.md`'s mention of the
  hook's `MAX_VERIFIERS` stays true, since the constant stays in the hook.

## 6. Acceptance criteria

Fixtures live under the pass's scratch directory; a payload's `cwd` is that directory, outside any
checkout, and `CLAUDE_PROJECT_DIR` is unset for the run, so rule 6 of the hook is unarmed. A
criterion that judges a call runs `$SCRATCH/p/hooks/agent-cap.js`, copied with `scratch-guard.js` and
no policy kit beside them, as the hook's suite arms its own copy, so rule 7 adds no rule.
`$SCRATCH/base/hooks/` holds the same two files written by `git show` from the pass's starting
commit. The in-tree hook, with `tools/policy/policy-mirror.js` beside it, refuses every such payload
under rule 7 (§4 Evidence).

- **AC1** — When `node -e "const m=require( './tools/hooks/agent-cap.js' ); console.log(typeof m.runBothViews, typeof m.extractWorkflowArgs, typeof m.extractBuildSlug, typeof m.readWriterBound, m.MAX_VERIFIERS)" < /dev/null`
  runs, it prints `function function function function 5` and exits 0; and
  `node tools/hooks/agent-cap.js < "$SCRATCH/fan-chunk1.payload.json"` exits 2 with rule 7's
  `is in no git checkout` refusal, so the hook run as the entry point still judges a call.
  Red when: requiring the hook runs `main()`, which exits on the empty stdin before the line prints,
  or a shared helper is not exported.
- **AC2** — When `node 'tools/workflows/check-verifier-fanout.js' --hook tools/hooks/agent-cap.js "$SCRATCH/fan-chunk1.js" "$SCRATCH/fan-two-seq.js"`
  runs over a harness verifying through `chunk(all, 1) // gov:fixed-verifiers` and one carrying two
  `gov:sequential-agents(5)` loops, it names both and exits 1; over `tools/workflows/tier2-review.js`
  and `tools/workflows/unattended-build.js` it exits 0.
  Red when: either planted case passes at the new home.
- **AC3** — When `node "$SCRATCH/p/hooks/agent-cap.js" < "$SCRATCH/fan-chunk1.payload.json"` runs
  after the pass deletes rule 2, it exits 0, where `node "$SCRATCH/base/hooks/agent-cap.js"` exits 2
  on the same payload naming `MAX_VERIFIERS`; and `grep -c "function fanoutFindings" tools/hooks/agent-cap.js`
  prints 0.
  Red when: the hook still carries rule 2, or still denies the verify fan.
- **AC4** — When `node 'tools/workflows/check-review-join.js' --hook tools/hooks/agent-cap.js "$SCRATCH/join.js"`
  runs over a harness keying its verdicts on `verdictByRef`, it names the line and exits 1, and over
  `tools/workflows/tier2-review.js` it exits 0.
  Red when: the planted join passes at the new home.
- **AC5** — When `node "$SCRATCH/p/hooks/agent-cap.js" < "$SCRATCH/join.payload.json"` runs after the
  pass deletes rule 5, it exits 0, where the starting commit's copy exits 2 naming
  `ref-keyed verdict join`. `node "$SCRATCH/p/hooks/agent-cap.js" --only=scripts < /dev/null` and the
  same run with `--only=join` each exit 2 naming `check-verifier-fanout.js` and `check-review-join.js`,
  where the starting commit's copy exits 0 on both. And
  `grep -n -e "--only=" tools/workflows/check-verifier-fanout.sh tools/workflows/check-review-join.sh tools/policy/check_policy.py`
  prints nothing, where it prints five lines at the pass's starting commit.
  Red when: the hook still runs rule 5, a `--only=` argument is admitted or ignored, or a caller still
  delegates to the hook.
- **AC6** — When `node 'tools/workflows/spec-audit-optin.js' < "$SCRATCH/sa-undated.json"` runs over a
  `kind: "spec-audit"` call placed in a fixture build whose README front matter carries no
  `spec-audit:` key, it exits 2 with the opt-in deny; with `spec-audit: 2026-10-23` in that front
  matter it exits 0; a `kind: "diff-review"` call exits 0; and a copy of the pack at
  `$SCRATCH/q/workflows/`, with no `$SCRATCH/q/hooks/` beside it, exits 2 on the spec-audit call
  naming the reader it could not load.
  Red when: an undated spec audit is admitted, or a missing reader admits it.
- **AC7** — When `node "$SCRATCH/p/hooks/agent-cap.js" < "$SCRATCH/sa-undated.json"` runs after the
  pass deletes rule 0, it exits 0, where the starting commit's copy exits 2 with the opt-in deny; and
  `grep -n "spec-audit-optin.js" .claude/settings.json` prints the wired command under a `Workflow`
  matcher.
  Red when: the hook still denies the call, or the pack is not wired here.
- **AC8** — When `python -c "import json; print([l['name'] for l in json.load(open( 'tools/gate-legs.json' )) if 'spec-audit-optin' in ' '.join(l['argv'])])"`
  runs, it prints the one leg, and `grep -n "spec-audit-optin" tools/workflows/kit.toml` prints the
  suite's withholding rule and the fragment's line-ending pin; `grep -cE '"rule[025]\b' tools/hooks/agent-cap.test.sh`
  prints 0, where it prints 116 at the pass's starting commit.
  Red when: a labelled arm of a moved rule is left in the hook's suite, or the new suite has no leg.
  figure: 116 is PINNED, measured at `8b2b995f` on 2026-11-03. The grep counts labelled arms only. An
  unlabelled deny arm left behind reds the hook's suite, whose hook no longer denies; an unlabelled
  admit arm left behind is not seen.
- **AC9** — When `bash tools/check-wiring.sh --check` runs in a scratch copy of `.claude/settings.json`
  with the pack's group removed, through the `GOV_SETTINGS_JSON` override, it prints an UNWIRED line
  naming `spec-audit-optin.js`; over the tree's own settings it prints the pack `ok`.
  Red when: the unwired pack reads as wired, or as not adopted.
  fixture: the settings copy at `"$SCRATCH/settings.json"`.
- **AC10** — When `grep -n "only=join\|rule 5 alone\|RULE 0" tools/hooks/README.md` runs, it prints
  nothing, and `grep -n "check-review-join.js\|spec-audit-optin.js\|check-verifier-fanout.js" tools/workflows/README.md WIRE-INTO-PROJECT.md`
  prints each new home in the review kit's README and the pack's row in the runbook.
  Red when: either README still sends a reader to the hook for a moved rule.
- **AC11** — When `grep -n "spec-audit-optin\|check-review-join.js" memory/map/features/review-harnesses.md`
  runs, it prints the claims, where it prints nothing at the pass's starting commit.
  Red when: a new file is claimed by no dossier.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `workflow script syntax` · `check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `agent-cap restatement` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `policy fixtures` · `playbook parity`

New arm: tools/workflows/check-verifier-fanout.test.sh · covers AC2 · rule 2's arms moved from the hook's suite, each planting its receiver or marker case · none
New arm: tools/workflows/check-review-join.test.sh · covers AC4 · rule 5's arms moved from the hook's suite, each planting a ref-keyed join · none
New arm: tools/workflows/spec-audit-optin.test.sh · covers AC6 · rule 0's arms moved from the hook's suite, each planting an undated, unplaceable or unreadable build, plus the missing-reader case · none
New arm: tools/hooks/agent-cap.test.sh · covers AC1 AC3 AC5 AC7 · one admit arm per moved rule over its planted case, the arm that every --only= argument refuses, and the export arm · none
New arm: tools/check-wiring.test.sh · covers AC9 · a settings file with the pack's group removed · none
New arm: tools/policy/check_policy.py · covers none · the limit-hook-writer-split fixture run through check-verifier-fanout.js over a writer split above the fixture's landed limit · none

## 8. Open questions

- **F1 — One unit for three moved rules, or three?** BUILD-METHOD M2 asks one mechanism per spec. (a)
  One unit, as the roster has it: one act, a rule leaving the hook for its review-kit home, done three
  times under one order and one ledger discipline. (b) Three units carrying the clause in parts. (b)
  adds two roster units and two departures, and each part would edit the same hook and its suite in
  sequence. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none
- **F2 — Which markers are "the loop markers"?** (a) The markers rule 2 reads: at `8b2b995f`
  `gov:fixed-verifiers`, `gov:sequential-agents` and `gov:fixed-writers`, the last added by
  TOOL-dGroundRules-18. (b) Those and `gov:bounded-fanout`. NT-27's table sends "the concurrency half
  of the bound rule" with the raw-primitive ban to dGroundRules, and the `gov:bounded-fanout` width
  was rule 3's, which TOOL-dGroundRules-10 retired, so no rule reads it now and (b) moves a marker
  nothing judges. Recommendation (a). Rung 1. RESOLVED (agent, 2026-10-23, delegated): (a). Re-read
  at `8b2b995f` on 2026-11-03: rule 2 reads three markers and moves whole, and the pick stands.
  widens: none · relaxes: none
- **F3 — Where do the helpers that two homes reach live?** (a) In the hook, exported, until its
  retirement moves them. (b) Copied into the review kit. (c) A new shared module in the hooks kit.
  (d) Moved into the review kit, the hook keeping none. (b) is two scanners of one script, which
  TOOL-aBatchedTribunal-1d ruled out; (c) adds a shipped file and a descriptor rule for a home
  dBoundRoles moves again; (d) is the helpers' last move, which §3 leaves to dBoundRoles.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). Re-read at `8b2b995f`
  on 2026-11-03: rules 1 and 3, which shared the views at base, have retired, so the views' sharers
  are rules 2 and 5 in two homes, and (d) became an option; the pick stands.
  widens: none · relaxes: none
- **F4 — Does the grant cover the moved rules, the pack's wiring and its leg?** Every path this unit
  touches under `tools/`, `.claude/settings.json` and `WIRE-INTO-PROJECT.md` is a governance carrier
  by `PLAY-dClosedLoop-10`'s list, and the clause names the three rules' moves and "a review-kit pack
  on Workflow calls", which is a wired hook with its suite. RESOLVED (agent, 2026-10-23, delegated):
  lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the three agent-cap review rules
  moved to the review kit, the spec-audit opt-in pack's PreToolUse wiring, its runbook row and its
  self-test leg · widens: none · relaxes: none
- **F5 — The join ban's form at its new home.** (a) A node module the shell gate owns and runs. (b)
  Awk inside the shell gate, the clause's "`check-review-join.sh` alone" read as one file. (b) restores
  the scanner the hook replaced, which matched retired names inside strings and missed interpolations,
  so it fails the moved arms that pin both. Recommendation (a): the gate alone runs it and nothing else
  carries the ban. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F6 — How does the wiring check grade the pack?** (a) The scratch arm's per-fragment grading
  extracted into one function both arms call. (b) A new arm copying it. (b) is a second instance of one
  kind written as a copy, which the charter's `[reuse]` rule refuses. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F7 — What happens to the hook's `--only=` selector and its script read once rules 2 and 5
  leave?** At `8b2b995f`, `--only=scripts` runs rules 2 and 5, `--only=join` rule 5, and the script
  read feeds those two alone (§4 Evidence), so after S2 and S3 neither mode runs a rule. (a) Delete
  the selector, its set and the script read. Every `--only=` argument is refused before stdin is
  read, naming the two `.js` homes, and both gates and the policy fixture stop delegating to the hook.
  (b) Keep `--only=scripts` as the set's one member, rev-5's text. It reads a script and runs no rule,
  so the fan-out gate's per-harness call can never go red. That is the vacuous-selector class the
  selector's own comment and TOOL-dTieredTribunal-14 S4 refuse, and a gate the charter's `[gate]`
  rule refuses. (c) Keep a script rule in the hook so the mode has one: rule 2 or rule 5 then lives in
  two homes, against §4's order, or rule 5 is not `check-review-join.sh`'s alone, against the clause.
  (d) Delete the selector and ignore the argument. A stale caller then runs rules 6 and 7 over a script
  payload: a review gate older than its hook, after an update naming the hooks kit alone, passes
  every harness with rule 2 run nowhere, a fail-open. (b) fails AC3 and AC5 and the `[gate]` rule,
  and (c) fails §4's order or the clause, so veto 1 discards both. (d) leaves the stale caller silent
  where (a) reds it by name, so (a) satisfies the most criteria and leaves no follow-up. It stays
  inside F4's grant, because the selector exists only to run the moved rules. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-22 and TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.
- rev-3 · 2026-10-23 · §3 · the disposal of the spec audit of units 20 to 23: a hands-off edge to TOOL-dFairHearing-26, the census of the moved rule 0 and rule 5 arms.
- rev-4 · 2026-10-23 · §3 · the round-3 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-32,
  whose resolver port finds this unit's opt-in pack.
- rev-5 · 2026-10-23 · §3 · the round-4 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-36, which reads the
  leg this unit adds.
- rev-6 · 2026-11-03 · §4 · Evidence re-measured at `8b2b995f`, after dGroundRules retired rules 1, 3
  and 4, the slot ledger, `EFFECTIVE_CAP` and `loadDeclaredCap`: every line, the helper reach table,
  the selector's callers and rule 7's refusal of a cwd in no checkout (fix brief
  2026-11-03-prompt-TOOL-dFairHearing-16-fix-brief, item 1).
- rev-6 · 2026-11-03 · S1 · AC1 · the exports are those two homes reach at `8b2b995f`, among them
  `MAX_VERIFIERS` and `MAX_LENSES`, which the playbook parity gate reads from the hook, and
  `readWriterBound`; `loadDeclaredCap` and `EFFECTIVE_CAP` are gone (same brief, item 2).
- rev-6 · 2026-11-03 · S2 · S3 · AC3 · AC5 · §4 · §8 F7 · the `--only=` selector and the script read
  leave the hook last, every `--only=` refuses, both gates run their `.js` homes, §4's order and
  alternatives say so, and AC3 and AC5 run a copy of the hook so each can go red (same brief, item 3).
- rev-6 · 2026-11-03 · §3 · S7 · AC11 · the non-goals and the external edge list nothing already
  gone; the version half leaves S7 and AC11 for a non-goal reading agent-cap 1.42 and review-harness
  1.56 at `8b2b995f`, because the lander mints every bump, and the edge to TOOL-dFairHearing-23 says
  so (same brief, item 4).
- rev-6 · 2026-11-03 · §5 · §10 · the risks name a stale caller of `--only=`, the user-docs line reads
  `help/` at `8b2b995f`, and the reuse audit adds F7's seam and its recall query (same brief, item 3).
- rev-6 · 2026-11-03 · S5 · AC8 · the suites' move names the unlabelled arms, the selector arms and
  two `check_policy.py` fixtures, and AC8 counts the labelled arms left, 116 at `8b2b995f`, where
  rev-5's grep already printed 0 (same brief, item 5).
- rev-6 · 2026-11-03 · §6 · AC1 · AC3 · AC5 · AC7 · the criteria that judge a call run a copy of the
  hook with no policy kit beside it, because the in-tree hook refuses a cwd in no checkout under rule
  7 (same brief, item 5).
- rev-6 · 2026-11-03 · §4 · §7 · §8 F2 · F3 · the files touched add `tools/policy/check_policy.py`
  and drop the version lines, the leg line adds `policy fixtures` and `playbook parity`, and F2 and F3
  are re-read at `8b2b995f` with their picks unchanged (same brief, item 5).

## 10. Reuse audit

The seams are the hook's own rules, lifted rather than rewritten: `fanoutFindings`
(`tools/hooks/agent-cap.js:748`), `scanJoinFindings` (:1346) and `checkSpecAuditDeclared` (:1472),
with the views and readers two homes share exported, the `require.main` idiom of
`tools/hooks/scratch-guard.js:1614-1615`, the two gates' existing hook resolution and
self-exclusions that already name each `.js` home, the hooks kit's fragment shape, govkit's derived
fragment wiring, and the scratch arm of `tools/check-wiring.sh`. F7's refusal reuses the selector's
own refusal of a member outside its set (`tools/hooks/agent-cap.js:1845-1850`), with the set gone.
`python tools/codebase-map/reuse_lookup.py "check a committed workflow
harness bounds its verifier count and loop markers without the hook"` ranked `boundedParallel` and
generic `check` symbols, and `python tools/codebase-map/reuse_lookup.py "deny a spec audit workflow
call whose build declares no opt-in date"` ranked none of the hook's functions: the lookup's symbol
tier did not surface the three rule functions the source read found, which is where the hits
disagreed with source. For rev-6, the second recall query below returned `TOOL-dTieredTribunal-14`
S4, the selector's origin and its vacuous-selector refusal, which F7 cites.

Recall terms used: `python tools/memory-recall/query.py "where do agent-cap's review rules move when
agent-cap retires" --terms "agent-cap retired NT-27 verifier total loop markers fixed-verifiers
sequential-agents check-review-join spec-audit opt-in pack"`, and at `8b2b995f` on 2026-11-03
`python tools/memory-recall/query.py "a hook selector mode left running no rule after its rules move
out" --terms "only selector vacuous agent-cap scripts join refuse retired mode"`
