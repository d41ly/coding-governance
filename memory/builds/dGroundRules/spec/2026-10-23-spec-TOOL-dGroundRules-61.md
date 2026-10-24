# TOOL-dGroundRules-61 — rule 7 bounds every settings layer it can read, so a declared settings file never hides the project's

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 17 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-61-deviation-49.md](../build/2026-10-23-build-TOOL-dGroundRules-61-deviation-49.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-61-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-61-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-61-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-61-build-brief.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-61-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-61-task.md) | research | TOOL-dGroundRules-62 TOOL-dGroundRules-63 |
| [2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-55-staleness-probe-brief.md) | research | TOOL-dGroundRules-55 TOOL-dGroundRules-62 TOOL-dGroundRules-64 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
confirmed **id 1 at HIGH**, item **H3**. `TOOL-dGroundRules-21` S34 has agent-cap's rule 7 resolve
"the settings file" the way `tools/check-wiring.sh:94-117` does, and that resolver is either/or:
with `GOV_SETTINGS_JSON` set, the declared file is the only file read. `TOOL-dGroundRules-10` S5 has
rule 7 read the project and the local settings files and take the value the harness applies, and
S34 silently replaces that reading whenever the variable is set. A project or local `env` value
above `runtime.agents-in-flight` is then never compared with the limit, rule 7 stays green, and
unit 10 has retired every other check of the limit. This unit is id 1's promotion: rule 7 reads
every settings layer it can read and bounds each one, and the item's left-shift is recorded as a
bug class. It repairs `TOOL-dGroundRules-21`, which sits at order 7, so it builds at order 17, after
every unit of the spec run.

## 2. Scope (IN)

- **S1** — The layers. Rule 7 (`checkSettingsInForce` in `tools/hooks/agent-cap.js`, unit 10 S5)
  reads its settings through one function, `readSettingsLayers(root)`, which returns the layers in
  the harness's precedence, highest first: the local file `.claude/settings.local.json` and the
  project file `.claude/settings.json` under the checkout root of the payload `cwd`, then, when
  `GOV_SETTINGS_JSON` is set in the hook's environment, the file it names, a relative path read
  against that checkout root. A declared path that resolves to the project or the local file is read
  once. This replaces the rule-7 half of `TOOL-dGroundRules-21` S34; its render half, and
  `TOOL-dGroundRules-25` S32's argv for the landing render, are untouched. Observed by AC1, AC2.
- **S2** — The bound. For each of `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` and
  `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`, every layer whose `env` sets the variable must hold a
  positive integer at or below the landed limit (§8 F1). Rule 7 refuses, exit 2, naming the first
  violating layer in S1's order, the variable, both numbers and
  `python tools/policy/policy.py settings --write <that file>`; it refuses when no layer sets the
  variable, as unit 10 S5 does. Observed by AC1, AC3.
- **S3** — The declared path that is not a file. With `GOV_SETTINGS_JSON` set to a path that is not
  a file, rule 7 refuses, exit 2, naming the path and `not a file`, as
  `tools/check-wiring.sh:106-108` refuses it; it never reads the declaration as an absent layer.
  Observed by AC4.
- **S4** — The cases, entries in `CASES` of `tools/policy/check_policy.py`, each under a landed limit
  of two, driving a `Workflow` payload through `tools/hooks/agent-cap.js` with the declared file
  outside the fixture's checkout: `limit-settings-elsewhere-project-over`,
  `limit-settings-elsewhere-only`, `limit-settings-elsewhere-declared-over` and
  `limit-settings-declared-absent`. Observed by AC1, AC2, AC3, AC4.
- **S5** — The help page. `help/agent-limit.md` (unit 10 S7) names the three layers rule 7 reads,
  and the three it cannot see: the `--settings` flag layer, the managed-policy layer and an exported
  environment variable (§8 F2; unit 10 §3 already leaves the last one out). Observed by AC5.
- **S6** — The left-shift. A new bug-class record,
  `memory/gotchas/check-grades-one-layer-of-a-layered-config.md`: a check that reads configuration
  reads every layer its consumer applies, a resolver built to locate a write target is never the
  reader of an enforcement check, and each such check carries a case in which a higher-precedence
  layer violates while the layer it grades is clean. Its body backticks `tools/hooks/agent-cap.js`
  and `tools/check-wiring.sh`, so `gotchas.py` selects it for a diff touching either, and
  `memory/gotchas/INDEX.md` is regenerated. Observed by AC6.

## 3. Non-goals (OUT)

- The settings render and its file argument: `TOOL-dGroundRules-21` S34's render half and
  `TOOL-dGroundRules-25` S32 stand as written.
- Reading the user layer `~/.claude/settings.json` when `GOV_SETTINGS_JSON` is unset. The project
  file outranks it, so a value there changes nothing the harness applies while the project file sets
  the variable, and when the project file does not, rule 7 already refuses.
- The managed-policy layer, the `--settings` flag layer and an exported environment variable (§8 F2).
- A change to `tools/check-wiring.sh`'s resolver, which locates the file the wiring arms grade and is
  right for that job.

### Edges

- **consumes-from** `TOOL-dGroundRules-21` — S34's resolution of the settings file, whose rule-7 half S1 replaces, and AC34's `limit-settings-elsewhere` case, beside which S4's cases sit

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23, in the tree this unit is written in; a cited line
number is the file's as this unit leaves it.

- `tools/check-wiring.sh:99-125` defines `settings_json`: with `GOV_SETTINGS_JSON` set it takes that
  file and no other (`:102-110`), refusing a declared path that is not a file (`:106-108`). Its
  comment (`:79-93`) says the variable exists for an adopter whose live settings sit outside the
  worktree, and names no layer of the harness for it.
- `tools/unattended/adopt-unattended.sh:867` and `tools/govkit/govkit.py:6132` resolve the same way,
  so the variable is a supported layout.
- `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:79-88` (S5) reads the
  project and the local file, the local file's value winning; `:301-305` (AC11) refuses a local
  file over the limit.
- `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-21.md:210-213` (S34) and
  `:548-550` (AC34) put rule 7 on the either/or resolver.
- `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-25.md:193-198` (S32) has the
  landing's render pass `.claude/settings.json` in its argv, so a declared variable steers only a
  render run with no file argument.
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
  const layers = [path.join(root, '.claude', 'settings.local.json'),
                  path.join(root, '.claude', 'settings.json')]
  const declared = process.env.GOV_SETTINGS_JSON
  if (declared) {
    const p = path.resolve(root, declared)
    if (!isFile(p)) throw deny(`GOV_SETTINGS_JSON names ${declared}, which is not a file`)
    if (!layers.some(l => samePath(l, p))) layers.push(p)
  }
  return layers.filter(isFile).map(p => ({ path: p, env: parseSettings(p).env || {} }))
}
```

`checkSettingsInForce` then walks the two variables. For each one it takes every layer whose `env`
holds the key and refuses on the first value, in layer order, that is not a positive integer or is
above the limit. It refuses when no layer holds the key. A file that does not parse refuses, naming
it, as `TOOL-dGroundRules-21` S38 states. The deny message keeps unit 10's shape and names the
violating file in the remedy.

This keeps the property the harness enforces whatever the declared file's place in its precedence:
the value the harness applies is one of the values the layers set, so when every read layer is at or
below the limit, the applied value is too, unless an unread layer sets it (§3, §8 F2).

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `readSettingsLayers` | js.function, lexicon `--suggest` OK on 2026-10-23 | `tools/hooks/agent-cap.js` |
| `limit-settings-elsewhere-project-over`, `limit-settings-elsewhere-only`, `limit-settings-elsewhere-declared-over`, `limit-settings-declared-absent` | `CASES` entries | `tools/policy/check_policy.py` |
| `check-grades-one-layer-of-a-layered-config` | bug-class record | `memory/gotchas/` |

### Rollout

Live at landing with the rest of the build. `KIT_AGENT_CAP_VERSION` moves once, in unit 10, and the
`kit epoch (shipped bytes move, the version moves)` leg grades from the merge-base, so this unit's
change to the hook's bytes lands under that one move.

### Files touched (estimate)

- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/policy/check_policy.py`
- `help/agent-limit.md`
- `memory/gotchas/check-grades-one-layer-of-a-layered-config.md`
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- **Rule 7 on `check-wiring.sh`'s resolver, as S34 wrote it.** It answers "which file do I grade",
  a write target's question; rule 7 asks what the harness applies, which no single file answers.
- **A precedence-ordered pick of one value per variable, the declared file lowest.** §8 F1.

## 5. Production-readiness checklist

- security — closes a fail-open path: a project or local value above the limit with the variable
  set. A shadowed lower layer above the limit now refuses, which is stricter than the harness needs
  and names its remedy.
- perf / scale — at most one more small JSON read per `Agent` or `Workflow` call.
- error / empty / loading states — a declared path that is not a file refuses; an absent project or
  local file is a layer that sets nothing; no layer setting a variable refuses, as before.
- observability — every refusal names the file, the variable, both numbers and the render command.
- risks — a developer whose user-level file carries an old raised value and is declared through
  `GOV_SETTINGS_JSON` is refused until that file is re-rendered or the value removed; the refusal
  says so.
- testing — AC1 to AC6, the cases of S4 and the `New arm:` lines under §7.
- migration — none: no file format changes.
- user docs — `help/agent-limit.md` (S5).

## 6. Acceptance criteria

Every command runs from the repository root. A case passes when its run prints no `WRONG`. The
literals the criteria run are spelled whole here, once; `tools/policy/check_policy.py` is created by
`TOOL-dGroundRules-1` and `help/agent-limit.md` by `TOOL-dGroundRules-10`, so neither can be run
before the build:

```text
CASE       = python tools/policy/check_policy.py --fixture <case>
DOC_LAYERS = grep -nE "GOV_SETTINGS_JSON|--settings|managed" help/agent-limit.md
```

- **AC1** — When `CASE limit-settings-elsewhere-project-over` runs, with `GOV_SETTINGS_JSON` naming a
  file outside the fixture's checkout that sets both variables to `2` and `.claude/settings.json`
  setting `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` to `3`, the payload through
  `node tools/hooks/agent-cap.js` exits 2 naming `.claude/settings.json` and that variable.
  Red when: rule 7 grades only the declared file, as `TOOL-dGroundRules-21` S34 wrote it, and exits 0.
- **AC2** — When `CASE limit-settings-elsewhere-only` runs, with the declared file at `2` and neither
  the project nor the local file setting an `env` key, the payload exits 0 through
  `node tools/hooks/agent-cap.js`.
  Red when: rule 7 drops the declared layer and refuses because no layer sets the variable.
- **AC3** — When `CASE limit-settings-elsewhere-declared-over` runs, with the declared file setting
  `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` to `3` and the project file at `2`, the payload exits 2
  through `node tools/hooks/agent-cap.js` naming the declared file.
  Red when: rule 7 grades one value per variable by precedence, ranks the declared file lowest, and
  passes a value the harness applies if that file is a higher layer.
- **AC4** — When `CASE limit-settings-declared-absent` runs, with `GOV_SETTINGS_JSON` naming a path
  that is not a file and the project file at `2`, the payload exits 2 through
  `node tools/hooks/agent-cap.js` printing that path and `not a file`.
  Red when: a declaration that resolves to nothing reads as a layer setting nothing, and exits 0.
- **AC5** — When `DOC_LAYERS` runs, it prints a line naming `GOV_SETTINGS_JSON` among the layers rule
  7 reads, and lines naming the `--settings` and managed-policy layers as unread.
  Red when: the page teaches rule 7 as covering every layer the harness applies.
- **AC6** — When
  `python tools/memory-tree/gotchas.py --for-paths tools/hooks/agent-cap.js tools/check-wiring.sh`
  runs, it lists `check-grades-one-layer-of-a-layered-config`, and
  `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: the record is unanchored, or the generated index is stale.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The policy legs `TOOL-dGroundRules-1` declares run the cases; they are named on the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py --fixture · covers AC1 AC2 AC3 AC4 · the four cases of S4, each planting its layers in the temporary repository and asserting its exit and the file it names · none
New arm: tools/hooks/agent-cap.test.sh · covers AC1 AC3 · a scratch checkout whose declared settings file holds the limit while its project file sets a harness variable above it, then the reverse, each refused, staged against a copy of the hook whose rule 7 reads the declared file alone · none

## 8. Open questions

- **F1 — How does rule 7 combine the layers it reads?** (a) The review's corrected fix as worded:
  for each variable take the highest-precedence file that sets it, the declared file ranked lowest
  as the user layer, and grade that one value. (b) Grade every read layer that sets the variable:
  each must be a positive integer at or below the limit. Both refuse the review's
  `limit-settings-elsewhere-project-over` and admit its `limit-settings-elsewhere-only`. The declared
  file's place in the harness's precedence is declared nowhere (`tools/check-wiring.sh:79-93` says
  only that it sits outside the worktree), and the harness carries a flag layer above the local file
  (§4 Evidence). If the declared file is that layer, (a) grades a shadowed project value and passes a
  declared value above the limit, the same fail-open in the other order, which widens a security
  surface the unit priced as closed (veto 3). (b) needs no precedence, and its cost is a refusal of a
  shadowed lower layer above the limit, which names its remedy. Recommendation (b). Rung 3.
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

## 10. Reuse audit

The seam extended is rule 7 itself, `checkSettingsInForce` in `tools/hooks/agent-cap.js` as
`TOOL-dGroundRules-10` S5 specs it: one reader function added beside it, and the declared-path
refusal copied in meaning from `tools/check-wiring.sh:106-108`, the house rule for that variable.
`python tools/codebase-map/reuse_lookup.py "read every settings layer the harness applies and
compare an env value with a limit"` ranked name-stem matches only (`read`, `read_text`, `read_conf`,
`readConfKey`), none of which reads a settings layer, so no existing seam fits the layer reader. The
recall probe returned the closing review's H3 and its skeptic fix, unit 21's S34 and the round-1
audit's id 21 that wrote it, and the open ask `TOOL-aDeferredBar-7` on two resolvers owning the
settings path; each agrees with source as read, and the ask concerns the wiring arms' resolver, which
this unit leaves alone.

Recall terms used: `python tools/memory-recall/query.py "which settings files does the harness apply
and in what precedence" --terms "settings.local.json settings.json GOV_SETTINGS_JSON precedence layer
harness env override rule 7 agent-cap check-wiring"`
