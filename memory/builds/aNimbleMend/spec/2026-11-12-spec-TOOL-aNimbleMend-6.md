# TOOL-aNimbleMend-6 — the hooks: the pass-leg runner is refused to a role agent by the role-gate arm and stays admitted at the main loop by the gate guard, pinned on both

**Status:** INPROGRESS · rev-2 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-6-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-6-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-aNimbleMend-5 ships a gate runner under a new file name, which neither hook knows. Unnamed, a
role agent can start it inside its pass, where the build rules say no gate runs. This unit names it
to the role-gate arm and pins what the gate guard does with it, so the pass legs run at the main
loop and nowhere else.

## 2. Scope (IN)

- **S1** — `GATE_RUNNERS` in `tools/hooks/scratch-guard.js` gains `pass-legs.sh`. A Bash or
  PowerShell call carrying an `agent_type` that runs the adapter is then refused as row
  `G2 runner`, by basename and in any form, exactly as the bar runner is. Observed by AC1.
- **S2** — The main loop is admitted as before. A call with no `agent_type` that runs the adapter
  passes the role-gate arm at its first step, and no code of this unit changes that. Observed by
  AC2.
- **S3** — The gate guard, `tools/unattended/gate-guard.js`, gains no deny row and no allow row.
  The adapter's command matches none of rows D1 to D5, so it is admitted in every phase, and a
  non-empty full-bar or self-test flag in front of it is still row D1. This unit changes that file's
  header comment only, where the paragraph headed `WHAT IT NEVER DENIES` gains one sentence naming
  the adapter beside the plain bar. Observed by AC3, AC4 and AC5.
- **S4** — The prose that lists the G2 runners names the fourth: the header comment of
  `tools/hooks/scratch-guard.js` at its `THE FOURTH CHECK` paragraph, the comment on
  `GATE_RUNNERS`, and the `G2 runner` row of the table in `tools/hooks/README.md`. Observed by AC6.

## 3. Non-goals (OUT)

- Refusing the plain bar during a pass. F1 asks it; as written this unit leaves the plain bar
  admitted at the main loop.
- Reading the pass-leg key in either hook. With the key off the adapter itself runs nothing, so a
  hook that admitted it admitted a no-op.
- A role allowlist entry for the adapter. Row G2 has no allowlist, and no role is meant to run it.
- Row G1 for the declared legs. A manifest row is already refused to a role agent word for word,
  whichever field it carries, and the scoped legs of TOOL-aNimbleMend-4 are manifest rows.
- The textual ceiling both hooks state of themselves. An adapter reached through an alias or an
  assembled path still walks past, as the bar runner does.
- The pages under `help/`. That is TOOL-aNimbleMend-11.
- The kit version bumps, which the lander's `mint` moves once.

### Edges

- **consumes-from** `TOOL-aNimbleMend-5` — the adapter's file name, `pass-legs.sh`, and the fact
  that it empties the two flags itself. Without that unit the name this unit adds refuses nothing.

## 4. Design

### Evidence

Read at 97e0841d.

| Fact | Where |
|---|---|
| Row G2 is `GATE_RUNNERS.includes(buildBaseName(c.head))`, over three basenames. | `tools/hooks/scratch-guard.js#checkGateRunner`, `:1302` |
| The role-gate arm returns null when the payload carries no `agent_type`. | `tools/hooks/scratch-guard.js#checkRoleGate`, step 1 of its comment |
| A launched script is a candidate, so `bash <path>/pass-legs.sh` reaches row G2. | `tools/hooks/scratch-guard.js@209dc48a:1501` |
| Row G2 has no allowlist: only a manifest leg on the role's list is admitted ahead of it. | `tools/hooks/scratch-guard.js#checkRoleGate`, step 7 of its comment |
| The gate guard denies a flag token matching `FLAG_RE` with a non-empty value, and a head word `resolveFileRow` classifies. | `tools/unattended/gate-guard.js#scanDenyHits` |
| `resolveFileRow` classifies three shapes: the self-test runner, the unattended gates runner, and a suite file. `pass-legs.sh` is none. | `tools/unattended/gate-guard.js#resolveFileRow` |
| A hit denies only while a run record on the branch is in a phase outside `PHASES_ALLOW`. | `tools/unattended/gate-guard.js#checkCommand` |
| The README table's G2 row reads "the bar runner, the self-test runner or the unattended gates runner". | `tools/hooks/README.md:619` |

### The change

One array member in `tools/hooks/scratch-guard.js`, and comment or table text at four sites. The
gate guard's predicate is not edited: the property S3 states is true at 97e0841d and this unit pins
it with arms, so a later row that would catch the adapter reds a suite instead of stalling a run.

| Caller | Command | Role-gate arm | Gate guard before `VERIFYING` |
|---|---|---|---|
| main loop | the adapter | admitted | admitted |
| main loop | the adapter behind a non-empty flag | admitted | denied, row D1 |
| role agent | the adapter, any form | refused, row G2 | not reached |
| main loop | a self-test suite or the flagged bar | admitted | denied, as today |
| role agent | any manifest leg off its allowlist | refused, row G1 | not reached |

The first row is "the hooks admit the pass-leg runner during a pass". The other four are "and
nothing else": every refusal that stood at 97e0841d still stands, and the one new runner name is
refused where a pass must stay gate-free.

### Inventory

No identifier is minted. `pass-legs.sh` is minted by TOOL-aNimbleMend-5.

### Rollout

The array member lands after TOOL-aNimbleMend-5 and before TOOL-aNimbleMend-7 calls the adapter. A
project whose installed hook predates this unit refuses nothing new and admits the adapter to a role
agent until its next `govkit update`.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/README.md`
- `tools/unattended/gate-guard.js`
- `tools/unattended/gate-guard.test.sh`

### Alternatives rejected

- **An allow row in the gate guard for the adapter.** The guard is a deny list keyed on five shapes
  and the adapter matches none, so an allow row would be dead code that reads as coverage, the
  class `guard-above-a-fold-makes-its-fallback-dead`.
- **Deriving the G2 list from the kit descriptor.** One name is added to a list of three. A second
  reader of the descriptor inside a hook that fails closed for a role agent is a larger change than
  the fact it removes.
- **Admitting the adapter to the builder role.** The build's rule puts the pass legs at the main
  loop, after the builder's commit, and the role-gate refusal is what keeps a pass cheap.

## 5. Production-readiness checklist

- security — the change narrows what a role agent may run and widens nothing; the role-gate arm
  still fails closed for a role agent when it throws.
- perf / scale — one more string in a three-member array compare.
- error / empty / loading states — N/A: no new state; an absent role index or manifest behaves as
  the arm's comment already states.
- observability — the existing deny text names the row and the command.
- risks — a project that renames the adapter loses the refusal, the same ceiling the bar runner's
  basename carries.
- testing — AC1 to AC6 as direct payload probes, and the two arms of §7.
- migration — N/A: an adopter takes both hooks at its next `govkit update`.
- user docs — `tools/hooks/README.md`, S4; the `help/` page is TOOL-aNimbleMend-11.

## 6. Acceptance criteria

Each probe pipes one PreToolUse payload to a hook on stdin and reads its exit code and stderr. The
payload's `cwd` is this worktree, whose `.claude/roles.json` names `gov-builder` and whose run
record on this branch is in a phase before `VERIFYING` during the pass. No probe starts a gate: a PreToolUse
hook decides and runs nothing. `<prefix>` is `tools` in this repository.

- **AC1** — When `node tools/hooks/scratch-guard.js` reads a Bash payload with `agent_type`
  `gov-builder` and the command `bash <prefix>/run-gates/pass-legs.sh --base HEAD~1`, it exits 2
  and its stderr names `G2 runner`. The same holds for the command behind `env`, behind
  `timeout 600`, and as a PowerShell payload.
  Red when: `GATE_RUNNERS` does not hold the name, so a role agent starts the pass legs in its pass.
- **AC2** — When the same hook reads the same payload with the `agent_type` key deleted, it exits 0
  and prints no line opening `BLOCKED`.
  Red when: the new name is tested above the arm's first step and the main loop is refused.
- **AC3** — When `node tools/unattended/gate-guard.js` reads a Bash payload with the command
  `bash <prefix>/run-gates/pass-legs.sh --base HEAD~1`, it exits 0 and prints nothing.
  Red when: a deny row classifies the adapter and the main loop cannot run the pass legs before
  `VERIFYING`.
- **AC4** — When the same hook reads that command with a non-empty assignment of the full-bar flag
  in front of it, it exits 2 and its stderr names the flag token as row D1's `flag:` line.
  Red when: the adapter's name exempts a flagged run, or the fixture's run record is not keyed and
  AC3 passed by the hook failing open.
- **AC5** — When the probe below runs, it prints nothing, where `PRE` is the tip the pass started
  from, recorded in the ledger:
  ```
  git diff -U0 "$PRE" -- tools/unattended/gate-guard.js | grep -E '^[-+][^-+]' | grep -vE '^[-+] \*'
  ```
  Red when: a line outside the header comment moved, so the guard's predicate changed.
- **AC6** — When `grep -c 'pass-legs' tools/hooks/README.md` runs, it prints at least 1, and
  `grep -n 'pass-legs' tools/hooks/scratch-guard.js` prints at least three lines: the header
  comment, the comment on the array, and the array.
  Red when: the code refuses a runner the prose does not name.
  figure: three is DERIVED from the three sites S1 and S4 name.

## 7. Gates

`scratch-guard self-test` · `format-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `policy fixtures` · `docs` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates`

Every leg on that line from `format-guard self-test` to `policy fixtures` guards the hooks
directory or `scratch-guard.js`. All seven suites are in the held tier, and the close runs them only if it asks
for that tier. The gate guard's suite is no manifest leg; it is budgeted in
`tools/run-gates/selftest-budgets.txt` as `unattended gate-guard selftest`.

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 · the name taken back out of `GATE_RUNNERS` · none
New arm: tools/unattended/gate-guard.test.sh · covers AC3 AC4 · a `resolveFileRow` shape added for the adapter's basename · none

## 8. Open questions

- **F1 — Does "and nothing else" also refuse the plain bar during a pass?** The gate guard admits
  the bar runner with neither flag in every phase, and `doc.build-method#m6-passes-commits-parallelism` names that form as the main
  loop's scoped bar. The roster row reads that the hooks admit the pass-leg runner during a pass
  "and nothing else".
  - **Leave the plain bar admitted.** The guard gains no row. With the key off or on, every call
    is decided as at 97e0841d, which is the byte-for-byte clause of the build's acceptance. The
    main loop keeps the scoped bar M6 grants it.
  - **Deny the plain bar before `VERIFYING` while the pass-leg key is on.** The guard gains a row
    D6 for the bar runner's basename and a read of the policy key on a hit. A pass then has one
    gate command. It contradicts M6 as it stands, so TOOL-aNimbleMend-11 would have to change that
    sentence, and the guard gains its first policy read.
  Recommendation: leave the plain bar admitted. The second option changes a rule of the build
  method that the owner's prompt did not ask to change.
  RESOLVED (agent, 2026-11-12, delegated): leave the plain bar admitted. The other option changes a rule of the build method the prompt did not ask to change, and it gives the guard a policy read.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · every §8 fork resolved in place under the run's mandate (M3).

## 10. Reuse audit

The seam is row G2 of the role-gate arm, `GATE_RUNNERS` beside `checkGateRunner` in
`tools/hooks/scratch-guard.js`, extended by one member. For the gate guard no code seam is extended:
`resolveFileRow` and `FLAG_RE` in `tools/unattended/gate-guard.js` already decide the adapter the
way this build needs, and the unit adds arms to that hook's suite.
`python tools/codebase-map/reuse_lookup.py "hook refuses a gate runner to a role agent by
basename"` returned `loadRoleIndex` and `resolveRoleRoot` in `tools/hooks/scratch-guard.js` and the
two PreToolUse hook inventory rows, which is the file the seam was then read in. Recall returned
the TOOL-aSmoothedDispatch-5 and TOOL-aSmoothedDispatch-22 evidence that row G1 matches a leg's
argv word for word, which is why §3 leaves the declared legs to that row, and TOOL-aOrientedCast-11,
the unit that built the arm. `gotchas.py --for-paths` over the estimate selected
`guard-above-a-fold-makes-its-fallback-dead` and `fixture-passes-by-finding-nothing`; the first
rejected alternative and AC4 answer them.

Recall terms used: `python tools/memory-recall/query.py "how does a run execute a subset of gate
legs scoped to a diff and which hook admits or refuses a gate runner during a pass" --terms "pass
leg GATE_LEGS GATE_BASE manifest guard run record gate-guard scratch-guard role-gate GATE_RUNNERS
turnstile ceiling"`
