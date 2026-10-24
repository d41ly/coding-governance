# TOOL-dGroundRules-61 — rule 7 bounds every settings layer it can read, so a declared settings file never hides the project's

**Status:** CLOSED · rev-3 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 17 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-61-deviation-49.md](../build/2026-10-23-build-TOOL-dGroundRules-61-deviation-49.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-61-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-61-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-61-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-61-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-61-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-61-build-brief.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-61-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-61-task.md) | research | TOOL-dGroundRules-62 TOOL-dGroundRules-63 |
| [2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md) | research | TOOL-dGroundRules-55 TOOL-dGroundRules-62 TOOL-dGroundRules-64 |
| [2026-10-24-prompt-TOOL-dGroundRules-61-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-61-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-61-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-61-probe-fix-brief.md) | research | — |
| [2026-10-25-prompt-TOOL-dGroundRules-32-close-arms-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-32-close-arms-brief.md) | research | TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-41 TOOL-dGroundRules-43 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-62 TOOL-dGroundRules-65 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
confirmed **id 1 at HIGH**, item **H3**. At HEAD 8eab342e0, with `TOOL-dGroundRules-21` built
(f6674a6a2), rule 7 (`checkSettingsInForce` in `tools/hooks/agent-cap.js`) reads two files: the one
`GOV_SETTINGS_JSON` names, in the project file's place, and the local file
`.claude/settings.local.json`, whose value wins where it sets one. With the variable set, the project
file `.claude/settings.json` is never read. `TOOL-dGroundRules-10` S5 has rule 7 read the project and
the local file and take the value the harness applies, and S34 of `TOOL-dGroundRules-21` swapped the
project file out whenever the variable is set. A project `env` value above `runtime.agents-in-flight`
is then never compared with the limit, rule 7 admits, and unit 10 left no other check of the limit.
This unit is id 1's promotion: rule 7 reads every settings layer it can read and bounds each one, and
the item's left-shift is recorded as a bug class. It builds at order 17.

## 2. Scope (IN)

- **S1** — The layers. Rule 7 reads its settings through one function, `readSettingsLayers(root)`,
  which returns the layers highest precedence first: the local file `.claude/settings.local.json`
  and the project file `.claude/settings.json` under the checkout root of the payload `cwd`, then,
  when `GOV_SETTINGS_JSON` is set in the hook's environment, the file it names, a relative path read
  against that checkout root. A declared path that resolves to the project or the local file is read
  once. Each layer's `env` is read as `checkSettingsInForce` reads a file at HEAD: an absent file
  sets nothing, a file that does not parse throws naming it (`TOOL-dGroundRules-21` S38). This takes
  the place of the rule-7 half of `TOOL-dGroundRules-21` S34; its render half, and
  `TOOL-dGroundRules-25` S32's argv for the landing render, are untouched. Observed by AC1, AC2.
- **S2** — The bound. For each of `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` and
  `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`, every layer whose `env` sets the variable must hold a
  positive integer at or below the landed limit (§8 F1). Rule 7 refuses, exit 2, one line per
  variable naming the first violating layer in S1's order, the variable and both numbers, with the
  render remedy HEAD's refusal carries. When no layer sets the variable it refuses naming
  `.claude/settings.json` and `is absent`, as HEAD does and `limit-settings-elsewhere` asserts.
  Observed by AC1, AC3.
- **S3** — The declared path that is not a file. With `GOV_SETTINGS_JSON` set to a path that is not
  a file, rule 7 refuses, exit 2, naming the path and `not a file`, as `settings_json` in
  `tools/check-wiring.sh` and `cmd_settings` in `tools/policy/policy.py` refuse it; it never reads
  the declaration as a layer that sets nothing. Observed by AC4.
- **S4** — The cases, in `LIMIT_CASES` of `tools/policy/check_policy.py`, run by `run_limit_case`
  and named in the module docstring, each under a landed limit of two, driving a `Workflow` payload
  through `tools/hooks/agent-cap.js` with the declared file outside the fixture's checkout: new
  `limit-settings-elsewhere-project-over` and `limit-settings-declared-absent`; and in the existing
  `limit-settings-elsewhere`, the project file planted at `2` after its `GOV_SETTINGS_JSON unset`
  check and before its `GOV_SETTINGS_JSON at 3` check. Observed by AC1, AC3, AC4.
- **S5** — The help page. `help/agent-limit.md`, in its rule-7 section and in its install line naming
  the order `check-wiring.sh` reads in, names the three layers rule 7 reads, and the three it cannot see: the `--settings` flag layer, the managed-policy layer
  and an exported environment variable (§8 F2; unit 10 §3 already leaves the last one out).
  Observed by AC5.
- **S6** — The left-shift. A new bug-class record under `memory/gotchas/`, slug
  `check-grades-one-layer-of-a-layered-config`: a check that reads configuration reads every layer
  its consumer applies, a resolver built to locate a write target is never the reader of an
  enforcement check, and each such check carries a case in which a higher-precedence layer violates
  while the layer it grades is clean. Its body backticks `tools/hooks/agent-cap.js` and
  `tools/check-wiring.sh`, so `gotchas.py` selects it for a diff touching either, and
  `memory/gotchas/INDEX.md` is regenerated. Observed by AC6.

## 3. Non-goals (OUT)

- The settings render and its file argument: `TOOL-dGroundRules-21` S34's render half and
  `TOOL-dGroundRules-25` S32 stand as written.
- Reading the user layer `~/.claude/settings.json` when `GOV_SETTINGS_JSON` is unset. The project
  file outranks it, so a value there changes nothing the harness applies while the project file sets
  the variable, and when the project file does not, rule 7 already refuses.
- The managed-policy layer, the `--settings` flag layer and an exported environment variable (§8 F2).
- A change to `settings_json` in `tools/check-wiring.sh`, which locates the file the wiring arms
  grade and is right for that job.

### Edges

- **consumes-from** `TOOL-dGroundRules-21` — S34's resolution of the settings file, whose rule-7 half S1 takes over, and AC34's `limit-settings-elsewhere` case, which S4 extends and AC2 and AC3 observe

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 at HEAD 8eab342e0, except the harness probe, run on
2026-10-23.

- `checkSettingsInForce` in `tools/hooks/agent-cap.js` builds its file list as the declared
  variable, else the project file, then the local file; an `ENOENT` read returns an empty `env`, so
  a declared path that is not a file reads as a layer that sets nothing, and the value graded per
  variable is the local file's where it sets one, else the first file's. The rule-7 header comment
  above it says `In force: GOV_SETTINGS_JSON, else .claude/settings.json (TOOL-dGroundRules-21 S34)`.
- `limit-settings-elsewhere` in `tools/policy/check_policy.py`, `TOOL-dGroundRules-21` AC34, asserts
  that a declared file at `2` with no project file admits, that the variable unset refuses naming
  `.claude/settings.json` and `is absent`, and that the declared file at `3` refuses naming it. No
  case plants a project file beside a declared one.
- `settings_json` in `tools/check-wiring.sh` takes the declared file and no other, refusing a
  declared path that is not a file; its comment says the variable exists for an adopter whose live
  settings sit outside the worktree, and names no layer of the harness for it.
- The gate-guard wiring check of `tools/unattended/adopt-unattended.sh`, `run_fragment_merges` in
  `tools/govkit/govkit.py` and `cmd_settings` in `tools/policy/policy.py` resolve the same way, so the
  variable is a supported layout.
- `help/agent-limit.md` names `GOV_SETTINGS_JSON` in its install section and its rule-7 section, and
  names neither the `--settings` nor the managed layer.
- `TOOL-dGroundRules-10` S5 reads the project and the local file, the local file's value winning;
  its AC11 refuses a local file over the limit. `TOOL-dGroundRules-25` S32 has the landing's render
  pass `.claude/settings.json` in its argv, so a declared variable steers only a render run with no
  file argument.
- The installed harness, `~/.local/bin/claude.exe` on node d, carries the settings source list
  `["userSettings","projectSettings","localSettings","flagSettings","policySettings"]`, found by
  `grep -a -o` over the binary (PINNED, 2026-10-23). The documented precedence reads it lowest
  first, so the local file outranks the project file and both outrank the user layer; that a later
  entry wins is UNVERIFIED by a probe here. The same binary names the managed layer's sources as a
  file under `C:/Program Files/ClaudeCode`, `/Library/Application Support/ClaudeCode` or
  `/etc/claude-code`, and the `HKLM SOFTWARE/Policies/ClaudeCode` registry key.

### Rule 7 after this unit

```js
function readSettingsLayers(root) {                 // highest precedence first
  const names = ['.claude/settings.local.json', '.claude/settings.json']
  const declared = process.env.GOV_SETTINGS_JSON
  if (declared) {
    const p = path.resolve(root, declared)
    if (!isFile(p)) throw new Error(`GOV_SETTINGS_JSON names ${declared}, which is not a file`)
    if (!names.some((n) => samePath(path.resolve(root, n), p))) names.push(declared)
  }
  return names.map((name) => ({ name, env: readEnv(root, name) }))  // HEAD's per-file read, lifted
}
```

`isFile` is a `fs.statSync` test and `samePath` compares `fs.realpathSync` of two existing files, as
`checkHarnessCall` already resolves paths. `checkSettingsInForce` then walks the two variables. For
each one it takes every layer whose `env` holds the key and refuses on the first value, in layer
order, that is not a positive integer or is above the limit; it refuses when no layer holds the key.
A throw from the reader reaches the rule-7 catch in `main`, which already denies naming the step and
the message. The deny message keeps unit 10's shape and names the violating layer by the name it
was read under.

This keeps the property the harness enforces whatever the declared file's place in its precedence:
the value the harness applies is one of the values the layers set, so when every read layer is at or
below the limit, the applied value is too, unless an unread layer sets it (§3, §8 F2).

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `readSettingsLayers` | js.function, lexicon `--suggest` OK on 2026-10-23 | `tools/hooks/agent-cap.js` |
| `limit-settings-elsewhere-project-over`, `limit-settings-declared-absent` | `LIMIT_CASES` entries | `tools/policy/check_policy.py` |
| `check-grades-one-layer-of-a-layered-config` | bug-class record | `memory/gotchas/` |

### Rollout

Live at landing with the rest of the build. No version marker moves on the branch:
`KIT_AGENT_CAP_VERSION` and the `gov:kit agent-cap@` markers stay as the branch carries them, and
the landing mints the next minor (`TOOL-dGroundRules-10` rev-5 §4), so `kit version markers` and
`kit epoch (shipped bytes move, the version moves)` are graded at the close, after that mint.

### Files touched (estimate)

- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/policy/check_policy.py`
- `help/agent-limit.md`
- `memory/gotchas/` — the new record of S6
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- **Rule 7 on `check-wiring.sh`'s resolver, as S34 wrote it.** It answers "which file do I grade",
  a write target's question; rule 7 asks what the harness applies, which no single file answers.
- **A precedence-ordered pick of one value per variable, the declared file lowest.** §8 F1.
- **Two more new cases for AC2 and AC3.** `limit-settings-elsewhere` already asserts both; one
  planted project file there makes its at-3 check refuse the F1 (a) pick as well.

## 5. Production-readiness checklist

- security — closes a fail-open path: a project value above the limit with the variable set. A
  shadowed lower layer above the limit now refuses, which is stricter than the harness needs and
  names its remedy.
- perf / scale — at most one more small JSON read per `Agent` or `Workflow` call.
- error / empty / loading states — a declared path that is not a file refuses; an absent project or
  local file is a layer that sets nothing; no layer setting a variable refuses, as before.
- observability — every refusal names the file, the variable, both numbers and the render command.
- risks — a developer whose user-level file carries an old raised value and is declared through
  `GOV_SETTINGS_JSON` is refused until that file is re-rendered or the value cleared; the refusal
  says so.
- testing — AC1 to AC6, the cases of S4 and the `New arm:` lines under §7.
- migration — none: no file format changes.
- user docs — `help/agent-limit.md` (S5).

## 6. Acceptance criteria

Every command runs from the repository root. A case passes when its run prints no `WRONG`. The
literals the criteria run are spelled whole here, once:

```text
CASE       = python tools/policy/check_policy.py --fixture <case>
DOC_LAYERS = grep -nE "GOV_SETTINGS_JSON|--settings|managed" help/agent-limit.md
```

At HEAD 8eab342e0 the criteria that red are AC1, AC4, AC6 and the `--settings` and managed-policy
lines of AC5. The criteria green before this unit are AC2, AC3 and the first line of AC5; each names
the staged break or the HEAD observation that reds it.

- **AC1** — When `CASE limit-settings-elsewhere-project-over` runs, with `GOV_SETTINGS_JSON` naming a
  file outside the fixture's checkout that sets both variables to `2` and `<repo>/.claude/settings.json`
  setting `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` to `3`, the payload through
  `tools/hooks/agent-cap.js` exits 2 naming `.claude/settings.json` and that variable.
  Red when: rule 7 reads as HEAD does, the declared file in the project file's place beside
  `<repo>/.claude/settings.local.json`, so the project value is never read and the payload exits 0.
- **AC2** — When `CASE limit-settings-elsewhere` runs, its `GOV_SETTINGS_JSON at 2` check, a declared
  file at `2` and no project or local file in the checkout, admits the payload, exit 0. Green before
  this unit: the `TOOL-dGroundRules-21` case asserts it at HEAD.
  Red when: rule 7 omits the declared layer and refuses because no layer sets the variable, staged
  as a copy of `tools/hooks/agent-cap.js` whose reader omits it, run on the check's payload.
- **AC3** — When `CASE limit-settings-elsewhere` runs, its `GOV_SETTINGS_JSON at 3` check, the
  declared file setting both variables to `3` and `<repo>/.claude/settings.json` planted at `2` (S4),
  refuses the payload, exit 2, naming the declared file and `above runtime.agents-in-flight 2`. Green
  before this unit: the case asserts the refusal at HEAD, which reads no project file while the
  variable is set.
  Red when: rule 7 grades one value per variable by precedence, the declared file ranked lowest (§8
  F1 (a)), takes the project's `2` and exits 0, staged as a copy of `tools/hooks/agent-cap.js`
  making that pick, run on the check's payload.
- **AC4** — When `CASE limit-settings-declared-absent` runs, with `GOV_SETTINGS_JSON` naming a path
  that is not a file and `<repo>/.claude/settings.json` at `2`, the payload through
  `tools/hooks/agent-cap.js` exits 2 printing that path and `not a file`.
  Red when: a declaration that resolves to nothing reads as a layer setting nothing: at HEAD the
  payload exits 2 printing `is absent` and never `not a file`, and a reader that kept the project
  layer would admit on its `2`, exit 0.
- **AC5** — When `DOC_LAYERS` runs, it prints a line naming `GOV_SETTINGS_JSON` among the layers
  rule 7 reads, and lines naming the `--settings` flag layer and the managed-policy layer as layers
  rule 7 does not read. The first line is green before this unit: the page names the variable in
  its rule-7 section at HEAD.
  Red when: the page teaches rule 7 as covering every layer the harness applies, as at HEAD, where
  no line matches `--settings` or `managed`.
- **AC6** — When `python tools/memory-tree/gotchas.py --for-paths tools/hooks/agent-cap.js tools/check-wiring.sh`
  runs, it lists `check-grades-one-layer-of-a-layered-config`, and
  `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: the record is absent, as at HEAD, or unanchored, or the generated index is stale.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

`policy fixtures` runs the cases of S4; `agent-cap self-test` runs the hook arm below.

New arm: tools/policy/check_policy.py --fixture · covers AC1 AC4 · the two new cases of S4, each planting its layers in the temporary repository and asserting its exit and the file it names, red against HEAD's rule 7 · none
New arm: tools/hooks/agent-cap.test.sh · covers AC1 AC2 AC3 · beside the rule-7 block's scratch checkout, a declared settings file outside it: project over with the declared file at the limit, declared-only at the limit, declared over with the project at the limit; each staged against a copy of the hook, HEAD's either/or read for the first, a reader omitting the declared layer for the second, the F1 (a) precedence pick for the third · none

## 8. Open questions

- **F1 — How does rule 7 combine the layers it reads?** (a) The review's corrected fix as worded:
  for each variable take the highest-precedence file that sets it, the declared file ranked lowest
  as the user layer, and grade that one value. (b) Grade every read layer that sets the variable:
  each must be a positive integer at or below the limit. Both refuse the review's
  `limit-settings-elsewhere-project-over` and admit its `limit-settings-elsewhere-only`. The declared
  file's place in the harness's precedence is declared nowhere (the comment on `settings_json` in
  `tools/check-wiring.sh` says only that it sits outside the worktree), and the harness carries a
  flag layer above the local file (§4 Evidence). If the declared file is that layer, (a) grades a
  shadowed project value and passes a declared value above the limit, the same fail-open in the
  other order, which widens a security surface the unit priced as closed (veto 3). (b) needs no
  precedence, and its cost is a refusal of a shadowed lower layer above the limit, which names its
  remedy. Recommendation (b). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b). widens: none · relaxes: none
- **F2 — Does rule 7 read the managed-policy layer?** (a) No: the help page names it, the
  `--settings` flag layer and an exported variable as layers rule 7 cannot see. (b) Read it. The
  installed harness names four sources for it (§4 Evidence), one of them a Windows registry key, and no
  record of this build verifies any of them on its harness version, so (b) carries an open question
  per source. The layer is written with administrator rights a session does not hold, so the hand
  raise rule 7 exists to catch does not come through it. Both options meet AC1 to AC6; tie-break,
  fewer open questions: (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 1 (HIGH, item H3) of the spec run's
  closing diff review, from the skeptic's corrected fix widened by §8 F1 to every read layer, with
  the cited lines read and the harness binary probed on 2026-10-23.
- rev-2 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.
- rev-3 · 2026-10-24 · §1 §2 §4 §5 §6 §7 §8 §10 · disagreements, from the read-only probe of steps 15 to 20 at e1c7051cb, restated at 8eab342e0 with units 1 to 41 built: §1 and AC1's Red when said rule 7 grades only the declared file, where `checkSettingsInForce` reads `GOV_SETTINGS_JSON` in the project file's place and still reads the local file; AC2 and AC3 were written to red, where the `limit-settings-elsewhere` case of `TOOL-dGroundRules-21` (f6674a6a2) asserts both; §4 Rollout had `KIT_AGENT_CAP_VERSION` move in unit 10, where no version marker moves on the branch; the `GOV_SETTINGS_JSON` half of AC5 is green at HEAD; §6 and §7 said `tools/policy/check_policy.py` and the policy legs could not run before the build, where `policy fixtures` is a leg; the evidence cited moved lines by number; S4 put the cases in `CASES`, where the limit cases sit in `LIMIT_CASES`. Ruled: §1 and AC1 restate HEAD's read; AC2 and AC3 observe the existing case, green before this unit, each with the staged break that reds it, and S4 plants the project file at `2` in that case before its at-3 check so the F1 (a) pick is refused there too; the rev-2 cases `limit-settings-elsewhere-only` and `limit-settings-elsewhere-declared-over` are not added, the existing case asserting both; AC1 and AC4 red at HEAD, and AC5 reds only on its `--settings` and managed-policy lines; the landing mints the next minor (`TOOL-dGroundRules-10` rev-5 §4); every citation by symbol or AC id; no criterion consumes a literal of `TOOL-dGroundRules-51`, -53, -54, -57, -58 or -59, closed WONTDO.

## 10. Reuse audit

The seam extended is rule 7 itself, `checkSettingsInForce` in `tools/hooks/agent-cap.js` as
`TOOL-dGroundRules-10` S5 specs it and `TOOL-dGroundRules-21` built it: its per-file read is lifted
into one reader function beside it, and the declared-path refusal is copied in meaning from
`settings_json` in `tools/check-wiring.sh`, the house rule for that variable, which `cmd_settings`
in `tools/policy/policy.py` follows too. The cases extend `LIMIT_CASES` and the existing
`limit-settings-elsewhere` case, and the hook arm extends the rule-7 block of
`tools/hooks/agent-cap.test.sh`. `python tools/codebase-map/reuse_lookup.py "read every settings
layer the harness applies and compare an env value with a limit"` ranked name-stem matches only
(`read`, `read_text`, `read_conf`, `readConfKey`), none of which reads a settings layer, so no
existing seam fits the layer reader. The recall probe returned the closing review's H3 and its
skeptic fix, unit 21's S34 and the round-1 audit's id 21 that wrote it, and the open ask
`TOOL-aDeferredBar-7` on two resolvers owning the settings path; each agrees with source as read,
and the ask concerns the wiring arms' resolver, which this unit leaves alone.

Recall terms used: `python tools/memory-recall/query.py "which settings files does the harness apply
and in what precedence" --terms "settings.local.json settings.json GOV_SETTINGS_JSON precedence layer
harness env override rule 7 agent-cap check-wiring"`
