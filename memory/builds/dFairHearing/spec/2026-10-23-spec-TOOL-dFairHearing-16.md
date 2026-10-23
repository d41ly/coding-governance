# TOOL-dFairHearing-16 — agent-cap's review rules moved to the review kit, each seen red at its new home before the hook stops carrying it

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 11 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0083@bd47ee4e whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
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

- **S1** — The shared readers stay one copy. `tools/hooks/agent-cap.js` exports the helpers a moved
  rule and a remaining rule both reach, and runs `main()` only when it is the entry point
  (`require.main === module`), the idiom `tools/hooks/scratch-guard.js` already uses. A helper that
  reads `EFFECTIVE_CAP` takes the cap as a parameter defaulting to it. A helper only a moved rule
  reaches moves with that rule. Observed by AC1.
- **S2** — The verifier total and the loop markers. The review kit's `check-verifier-fanout.js`, beside
  `tools/workflows/check-verifier-fanout.sh`, holds rule 2: `fanoutFindings` with the receivers it
  admits, the `gov:fixed-verifiers` and `gov:sequential-agents` markers and the one-marked-loop sweep,
  evaluated over both of agent-cap's exported views, at the cap agent-cap's exported
  `loadDeclaredCap` and `MAX_VERIFIERS` resolve. The gate runs it on every harness beside the hook's
  `--only=scripts`, which keeps rules 1 and 3 for dGroundRules to take later. `MAX_LENSES`, the
  array-literal receiver's bound, which TOOL-dFairHearing-13 leaves in the hook because rule 2 reads
  it there, moves with rule 2; the exact slot count that unit's native arm holds stays its own. Seen
  red at its new home by AC2, and agent-cap stops carrying it by AC3.
- **S3** — The ref-keyed join ban. The review kit's `check-review-join.js`, beside
  `tools/workflows/check-review-join.sh`, holds `scanJoinFindings` and its ban table, and the gate
  runs it where it ran the hook's `--only=join`. The gate's self-exclusion drops `agent-cap.js`, which
  no longer holds the table. The hook's rule 5 and the `join` member of its `--only` set leave the set,
  so `scripts` is its one member. Seen red at its new home by AC4, and agent-cap stops carrying it by
  AC5.
  **Readers:** by name: `tools/workflows/check-review-join.sh`, `tools/hooks/README.md`,
  `tools/check-wiring.sh`, `tools/check-wiring.test.sh`, `tools/hooks/agent-cap.test.sh`,
  `memory/map/features/agent-cap.md`, `memory/map/features/review-harnesses.md`. by value:
  `tools/hooks/agent-cap.js`, whose `ONLY_RULES` refuses a member outside the set, and
  `tools/check-wiring.sh`, which reds a wired command carrying any `--only` value.
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
  `tools/workflows/check-review-join.test.sh` and a new `spec-audit-optin.test.sh`, and the hook's
  suite gains one arm per moved rule asserting it now admits that rule's planted case.
  `tools/gate-legs.json` gains the leg `spec-audit opt-in pack self-test`, and
  `tools/workflows/kit.toml` withholds the new suite as it withholds its siblings and pins the
  fragment's line endings. Observed by AC8.
- **S6** — The wiring check. `tools/check-wiring.sh` grades the pack's fragment as it grades the hooks
  kit's: the scratch arm's per-fragment grading becomes one function both arms call, and
  `tools/check-wiring.test.sh` gains the pack's unwired case. Observed by AC9.
- **S7** — The kits' records. `tools/hooks/README.md` and `tools/workflows/README.md` say where each
  moved rule lives and how to run it; the default-install table of `WIRE-INTO-PROJECT.md` gains the
  pack's row; the dossiers `memory/map/features/agent-cap.md` and
  `memory/map/features/review-harnesses.md` claim the three new files and the new leg. The agent-cap
  and review-harness versions each move once against base `3708a705` if no earlier unit of this build
  moved them. Observed by AC10 and AC11.

## 3. Non-goals (OUT)

- Rules 1, 3, 4 and 6, the slot ledger, `FANOUT_CAP`, `--print-cap` and the `AGENT_CAP` refusal.
  They are dGroundRules' and dBoundRoles' by NT-27's table, and stay in the hook.
- The `gov:bounded-fanout` marker, which is rule 3's concurrency width (section 8 F2).
- The lens count as an exact slot count, TOOL-dFairHearing-13's native arm in the same gate.
- Retiring `tools/hooks/agent-cap.js` and moving its exported helpers to their last home, dBoundRoles'.
- The review protocol's statement of where each rule lives, which TOOL-dFairHearing-10 brings in line.
- A check of inline Workflow scripts' verifier total at the tool call. NT-27 moves the rule to the
  merge bar's harness check, and the harness's own concurrency settings bound an inline script.

### Edges

- **consumes-from** `TOOL-dFairHearing-13` — the native slot arm in the `verifier fan-out` leg, beside which the moved rules land in the same gate; without it the gate's header and clean line this unit extends are today's
- **hands-off** `TOOL-dFairHearing-10` — the review protocol's enforcement and predicate sections, rewritten to name where each moved rule now lives
- **hands-off** external — dGroundRules retires rules 1 and 3 and the slot ledger; dBoundRoles retires agent-cap and moves the helpers this unit exports
- **hands-off** `TOOL-dFairHearing-22` — finding id 40 (item H3) of the round-1 spec audit: the hook denies a spec-audit call while `spec-audit-optin.js` is not beside it, so a partial `govkit update` cannot fail open as §4 Rollout prices it
- **hands-off** `TOOL-dFairHearing-23` — finding ids 6, 10, 20, 29, 30, 31 and 33 of the round-1 spec audit: the version half of S7 and AC11 superseded by the lander's mint (its S12, S13, AC6), AC8's grep half replaced by counting the moved arms (its S16, AC9), `MAX_LENSES`'s home taken by `LENS_SLOTS` (its S42, AC33), the new leg's registry, budget and foreign-prefix rows (its S26, AC17), the fixtures copying `check-verifier-fanout.js` (its S27, AC18) and the kickoff manifest re-stamp after the gate-legs.json edit (its S28, AC19)

## 4. Design

### Evidence

- Rule 2 is `fanoutFindings` (`tools/hooks/agent-cap.js:789-1264`) with its markers (:491, :522) and
  its lens allowance (:493-497); rule 5 is `scanJoinFindings` (:1754-1811); rule 0 is
  `checkSpecAuditDeclared` and its helpers (:1813-2030). `main()` runs them at :2310-2316, :2338-2353
  and :2409-2422, and calls itself unguarded at :2427.
- Measured over the file by call site at base: `parseBranches` and `boundedBranch` are reached by
  rule 2 alone; `boundedK`, `intConsts`, `joinCall` and `topLevelArgs` by rules 2 and 3;
  `renderStrippedView`, `renderBlankedLiterals` and `renderPerLineBlanked` by rule 5 and another
  rule; `extractWorkflowArgs` and `extractBuildSlug` by rules 0 and 6; `readSpecAuditDefault` by rule
  0 alone. `boundedK` reads the module's `EFFECTIVE_CAP` (:551-556).
- `tools/workflows/check-verifier-fanout.sh` delegates to the hook with `--only=scripts` (:204-212),
  and its self-exclusion already names a `check-verifier-fanout.js` (:166). `check-review-join.sh`
  delegates with `--only=join` (:245), and its self-exclusion names `check-review-join.js` and
  `agent-cap.js` (:37).
- The `--only` set is closed at `join` and `scripts` (:2222); `tools/check-wiring.sh:861-875` reds a
  wired agent-cap command carrying any `--only`.
- The hooks kit's fragment idiom: `tools/hooks/scratch-guard.fragment.json` names `event`, `matcher`,
  `marker` and `hook_path` with a `{kit}` token, and govkit wires every landed `*.fragment.json`
  through the target's `settings-merge.py` (`tools/govkit/govkit.py:6109-6125`).
- The scratch arm of `tools/check-wiring.sh` (:898-960) grades every fragment in the hooks kit's
  directory, so a fragment in the review kit's directory is graded by no arm today.

### The order inside the pass

For each of the three rules, in this order: the new home lands with its arms; the pass observes the
new home red on the planted case and green on the shipped harnesses; only then does it delete the rule
from the hook and observe the hook admitting the same case. The pass's acceptance ledger records both
observations per rule. A rule is never absent from both homes at a commit, and never in both at the
pass's commit.

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
- `tools/workflows/tier2-review.template.js` (the `version:` line only, if no earlier unit moved it)
- `tools/workflows/tier2-review.js` (its render)
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

- **Copying the lexer into the review kit.** Rules 1 and 3 stay in the hook until dGroundRules, so a
  copy is two scanners of one script, the drift TOOL-aBatchedTribunal-1d ruled out (section 8 F3).
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
  (`tools/workflows/kit.toml`, `requires`).
- testing — AC1 to AC11 as direct runs of each home and of the hook over planted fixtures; the moved
  and new arms under section 7.
- migration — an adopter's update wires the pack through govkit; a hand copy runs
  `settings-merge.py --fragment` on it, as the runbook row says.
- user docs — `tools/hooks/README.md`, `tools/workflows/README.md` and the runbook's default-install
  table; `help/roles.md` lists hook refusals and names none of these three.

## 6. Acceptance criteria

Fixtures live under the pass's scratch directory; a payload's `cwd` is that directory, outside any
checkout, so rule 6 of the hook is unarmed, and `CLAUDE_PROJECT_DIR` is unset for the run.

- **AC1** — When `node -e "const m=require( './tools/hooks/agent-cap.js' ); console.log(typeof m.runBothViews, typeof m.loadDeclaredCap, typeof m.extractBuildSlug)"`
  runs, it prints `function function function` and exits 0 without reading stdin, and the hook fed a
  `Workflow` payload on stdin still judges it.
  Red when: requiring the hook runs `main()`, or a shared helper is not exported.
- **AC2** — When `node 'tools/workflows/check-verifier-fanout.js' --hook tools/hooks/agent-cap.js "$SCRATCH/fan-chunk1.js" "$SCRATCH/fan-two-seq.js"`
  runs over a harness verifying through `chunk(all, 1) // gov:fixed-verifiers` and one carrying two
  `gov:sequential-agents(5)` loops, it names both and exits 1; over `tools/workflows/tier2-review.js`
  and `tools/workflows/unattended-build.js` it exits 0.
  Red when: either planted case passes at the new home.
- **AC3** — When `node tools/hooks/agent-cap.js --only=scripts < "$SCRATCH/fan-chunk1.payload.json"`
  runs after the pass deletes rule 2, it exits 0, where the hook at the pass's starting commit exits
  2 on the same payload.
  Red when: the hook still carries rule 2, or still denies the verify fan.
- **AC4** — When `node 'tools/workflows/check-review-join.js' --hook tools/hooks/agent-cap.js "$SCRATCH/join.js"`
  runs over a harness keying its verdicts on `verdictByRef`, it names the line and exits 1, and over
  `tools/workflows/tier2-review.js` it exits 0.
  Red when: the planted join passes at the new home.
- **AC5** — When `node tools/hooks/agent-cap.js --only=join < "$SCRATCH/join.payload.json"` runs, it
  exits 2 naming `scripts` as the closed set; with `--only=scripts` it exits 0 on the same payload; and
  `grep -n "only=join" tools/workflows/check-review-join.sh` prints nothing.
  Red when: the hook still runs rule 5, or the gate still delegates to it.
- **AC6** — When `node 'tools/workflows/spec-audit-optin.js' < "$SCRATCH/sa-undated.json"` runs over a
  `kind: "spec-audit"` call placed in a fixture build whose README front matter carries no
  `spec-audit:` key, it exits 2 with the opt-in deny; with `spec-audit: 2026-10-23` in that front
  matter it exits 0; a `kind: "diff-review"` call exits 0; and with the fixture's hooks directory
  absent, the spec-audit call exits 2 naming the reader it could not load.
  Red when: an undated spec audit is admitted, or a missing reader admits it.
- **AC7** — When `node tools/hooks/agent-cap.js < "$SCRATCH/sa-undated.json"` runs after the pass
  deletes rule 0, it exits 0; and `grep -n "spec-audit-optin.js" .claude/settings.json` prints the
  wired command under a `Workflow` matcher.
  Red when: the hook still denies the call, or the pack is not wired here.
- **AC8** — When `python -c "import json; print([l['name'] for l in json.load(open( 'tools/gate-legs.json' )) if 'spec-audit-optin' in ' '.join(l['argv'])])"`
  runs, it prints the one leg, and `grep -n "spec-audit-optin" tools/workflows/kit.toml` prints the
  suite's withholding rule and the fragment's line-ending pin; `grep -c "checkSpecAuditDeclared\|scanJoinFindings\|fanoutFindings" tools/hooks/agent-cap.test.sh`
  prints 0.
  Red when: a moved arm is left in the hook's suite, or the new suite has no leg.
- **AC9** — When `bash tools/check-wiring.sh --check` runs in a scratch copy of `.claude/settings.json`
  with the pack's group removed, through the `GOV_SETTINGS_JSON` override, it prints an UNWIRED line
  naming `spec-audit-optin.js`; over the tree's own settings it prints the pack `ok`.
  Red when: the unwired pack reads as wired, or as not adopted.
  fixture: the settings copy at `"$SCRATCH/settings.json"`.
- **AC10** — When `grep -n "only=join\|rule 5 alone\|RULE 0" tools/hooks/README.md` runs, it prints
  nothing, and `grep -n "check-review-join.js\|spec-audit-optin.js\|check-verifier-fanout.js" tools/workflows/README.md WIRE-INTO-PROJECT.md`
  prints each new home in the review kit's README and the pack's row in the runbook.
  Red when: either README still sends a reader to the hook for a moved rule.
- **AC11** — When `grep -m1 "KIT_AGENT_CAP_VERSION = " tools/hooks/agent-cap.js` and
  `grep -m1 "version: " tools/workflows/tier2-review.template.js` run, each prints a version other than
  the same grep over `git show 3708a705:<file>` does; and `grep -n "spec-audit-optin\|check-review-join.js" memory/map/features/review-harnesses.md`
  prints the claims.
  Red when: a kit's shipped bytes moved over the build with its version unmoved, or a new file is
  claimed by no dossier.
  figure: the base versions, agent-cap `1.40` and review-harness `1.53`, are pinned, read at base
  `3708a705` on 2026-10-23.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `workflow script syntax` · `check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `agent-cap restatement` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene`

New arm: tools/workflows/check-verifier-fanout.test.sh · covers AC2 · rule 2's arms moved from the hook's suite, each planting its receiver or marker case · none
New arm: tools/workflows/check-review-join.test.sh · covers AC4 · rule 5's arms moved from the hook's suite, each planting a ref-keyed join · none
New arm: tools/workflows/spec-audit-optin.test.sh · covers AC6 · rule 0's arms moved from the hook's suite, each planting an undated, unplaceable or unreadable build, plus the missing-reader case · none
New arm: tools/hooks/agent-cap.test.sh · covers AC1 AC3 AC5 AC7 · one admit arm per moved rule over its planted case, and the export arm · none
New arm: tools/check-wiring.test.sh · covers AC9 · a settings file with the pack's group removed · none

## 8. Open questions

- **F1 — One unit for three moved rules, or three?** BUILD-METHOD M2 asks one mechanism per spec. (a)
  One unit, as the roster has it: one act, a rule leaving the hook for its review-kit home, done three
  times under one order and one ledger discipline. (b) Three units carrying the clause in parts. (b)
  adds two roster units and two departures, and each part would edit the same hook and its suite in
  sequence. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none ·
  relaxes: none
- **F2 — Which markers are "the loop markers"?** (a) `gov:fixed-verifiers` and `gov:sequential-agents`,
  the two rule 2 reads. (b) Those and `gov:bounded-fanout`. NT-27's table sends "the concurrency half
  of the bound rule" with the raw-primitive ban to dGroundRules, and the `gov:bounded-fanout` width is
  rule 3's (:1458-1481), so (b) moves a dGroundRules rule into this build. Recommendation (a). Rung 1.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F3 — Where do the helpers a moved rule shares with a remaining rule live?** (a) In the hook,
  exported, until its retirement moves them. (b) Copied into the review kit. (c) A new shared module in
  the hooks kit. (b) is two scanners of one script, which TOOL-aBatchedTribunal-1d ruled out; (c) adds
  a shipped file and a descriptor rule for a home dBoundRoles moves again. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
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

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-22 and TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.

## 10. Reuse audit

The seams are the hook's own rules, lifted rather than rewritten: `fanoutFindings`
(`tools/hooks/agent-cap.js:789`), `scanJoinFindings` (:1767) and `checkSpecAuditDeclared` (:1894),
with the views and binders they share exported, the `require.main` idiom of
`tools/hooks/scratch-guard.js:1614-1615`, the two gates' existing self-exclusions that already name
each `.js` home, the hooks kit's fragment shape, govkit's derived fragment wiring, and the scratch
arm of `tools/check-wiring.sh`. `python tools/codebase-map/reuse_lookup.py "check a committed workflow
harness bounds its verifier count and loop markers without the hook"` ranked `boundedParallel` and
generic `check` symbols, and `python tools/codebase-map/reuse_lookup.py "deny a spec audit workflow
call whose build declares no opt-in date"` ranked none of the hook's functions: the lookup's symbol
tier did not surface the three rule functions the source read found, which is where the hits
disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "where do agent-cap's review rules move when
agent-cap retires" --terms "agent-cap retired NT-27 verifier total loop markers fixed-verifiers
sequential-agents check-review-join spec-audit opt-in pack"`
