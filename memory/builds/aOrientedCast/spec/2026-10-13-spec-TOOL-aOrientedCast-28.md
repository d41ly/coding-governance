# TOOL-aOrientedCast-28 — spec folds run through the build harness, and a leased session spawns no spec writer directly

**Status:** OPEN · rev-1 · 2026-10-13 · node a · Tier-2 · base 646d4a73581393acbf42f33864a9808c96d00a0c · streams tooling · order 29 · ratified 2026-10-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aOrientedCast-1-8-owner-addendum.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-8-owner-addendum.md) | research | TOOL-aOrientedCast-1 TOOL-aOrientedCast-27 |
| [2026-10-13-prompt-TOOL-aOrientedCast-28-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-28-1-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

In this build every spec fold ran as a direct `gov-spec-writer` spawn, because the build harness's
spec stage authors only MISSING specs. A direct spawn cannot set its effort, counts against the
per-prompt-turn spawn budget an unattended run cannot reset, leaves no harness journal and returns
free text (the owner's sixth addendum, "The follow-up"). This unit gives the build harness a fold
route that rev-bumps a present spec through the spec stage's own typed, effort-set, labelled and
schema-checked writer and its own commit stage. The unattended kit's PreToolUse hook then refuses a
direct spec-writer spawn from a session holding a live run's lease, naming that route.

## 2. Scope (IN)

- **S1** — `tools/workflows/unattended-build.template.js` and its render take a fold call: every
  `units[]` entry carries `foldRev`, the rev its spec must reach, with `specPath` and
  `specBriefPath`. §4 "The fold call" lists the refusals, each made before any agent spawns.
  Observed by AC1.
- **S2** — On a fold call the spec stage's fan spawns fold writers, as `roles.specWriter` at
  `efforts.specWriter`, with the fold prompt of §4 "The fold writer", a label ending
  ` · spec-fold` and `FOLD_SCHEMA`. It authors, audits, disposes and hands out nothing. Observed by
  AC2 and AC5.
- **S3** — The spec stage's merge reads a fold writer's `folded` list and refuses a claimed rev that
  is not the unit's `foldRev`. The spec commit stage commits the folded specs with its existing git
  block, one message line apart, so it refuses a foreign tree change exactly as it does for authored
  specs. The call then returns the fold return of §4 "The fold return". Observed by AC2, AC3 and AC4.
- **S4** — `tools/unattended/gate-guard.js` gains a spawn arm, §4 "The spawn arm": an `Agent` call
  whose `subagent_type` the role index maps to the `spec-write` workflow is refused from a session
  holding a live lease, read by `resolveLiveLeases`, which the question arm now calls too. Outside a
  live lease it is admitted. Observed by AC6, AC7, AC8 and AC10.
- **S5** — `tools/unattended/gate-guard.fragment.json`'s matcher becomes
  `Bash|PowerShell|AskUserQuestion|Agent`, and gov's `.claude/settings.json` is re-merged from it.
  Observed by AC9.
- **S6** — The two suites gain the arms of §4 "The suites", each floor rising by them. NOT OBSERVED
  by a criterion of its own: a pass runs no suite, and the main loop observes each arm at the close
  under §7's `New arm:` lines. Every arm re-observes a criterion below.
- **S7** — The prose of §4 "Documentation": the verbs template and the `/build` Skill template name
  the fold route where they say how a spec is revised, and the hook's header, two kit READMEs and
  `help/roles.md` describe the route and the refusal. Observed by AC11.
- **S8** — The unattended, review-harness and roles kits each move one version step with every
  carrier, after `TOOL-aOrientedCast-27`'s steps. Observed by AC12.
- **S9** — The unattended and review-harnesses dossiers gain this unit, and the map is re-rendered.
  Observed by AC13.
- **S10** — The template's edit reaches its render line for line. Observed by AC14.

## 3. Non-goals (OUT)

- **Rule 6 of `tools/hooks/agent-cap.js`.** The brief names it as the refusal's home, and §8 F1
  moves the refusal to the unattended kit's hook instead. `agent-cap.js` and the hooks kit's version
  are left as they are.
- Refusing a leased session's direct spawn of any role other than the spec writer. The builder is
  already dispatched through the unit harness, and the reviewers through the review harness (§3
  Edges).
- A fold route in the unit harness or the review harness, or a new declared harness.
- Auditing a fold. A fold call never runs AUDIT or DISPOSAL; a caller folding an audit round
  re-invokes the audit afterwards, as M4 and the verbs guide already say.
- Verifying a fold writer's claimed rev against the file. A workflow script has no filesystem; the
  header-rev-in-§9 check of hygiene check 12 grades the committed file at the bar.
- A call mixing fold units and units to author. It is refused (§4 "Alternatives rejected").
- Any change to the spec-writer role body, `tools/roles/workflows.toml`, `handoff.py harness-args`
  or `handoff.py stage-efforts`, the driver `unattended.sh`, or the protocol's §12.
- The `unattended-build@` identity marker in the harness's `meta.version`, which this build's
  harness units have left as it was (§4 "Kit versions").

### Edges

- **consumes-from** external — Claude Code delivers an `Agent` tool call to a PreToolUse hook whose
  matcher names `Agent`, with `session_id` and `tool_input.subagent_type` in its payload, as the
  spawn guard already reads them (`tools/hooks/agent-cap.js:2092`, `:2220`).
- **hands-off** external — the same lease-keyed refusal for other roles, should the owner want every
  leased session's agent to run inside a harness.

## 4. Design

Line numbers were read at `c5d722493`, the run branch's HEAD on 2026-10-13, where
`TOOL-aOrientedCast-25`, `TOOL-aOrientedCast-26` and `TOOL-aOrientedCast-27` are OPEN and unbuilt.
`TOOL-aOrientedCast-27` writes the build harness, its suite and render, the roles kit files and
`help/roles.md` before this unit does, so the builder finds each site by its content.

### Evidence

- The spec stage authors only MISSING specs: its prompt counts a present spec `alreadyPresent`
  (`tools/workflows/unattended-build.template.js:973-978`). `units` is required non-empty (`:301-309`).
- Audit-shaped arguments beside no `specAudit` are already refused (`:360-370`).
- The spec stage's fan, `renderStageOpts` and `SPEC_SCHEMA` sit at `:948-1000`, `:533-535` and
  `:700-711`. The merge is at `:1049-1103` and `specFolder` at `:1015`.
- The commit stage takes `authoredIds` (`:1117-1284`). Its git block (`:1151-1171`) records the
  tree first and refuses when an input of the build-index generator carries a change the index does
  not hold (`:1156-1160`). Its message is `spec(<slug>): <ids>` (`:1169`).
- `resumeRemedy` closes every refusal that asks for a commit (`:561-572`).
- `phase('Audit')` opens at `:1295`, after the commit stage.
- `handoff.py harness-args unattended-build` printed
  `{"builder":"gov-builder","disposal":"gov-spec-writer","skeptic":"gov-skeptic","specFinder":"gov-spec-reviewer","specWriter":"gov-spec-writer","synthesis":"gov-synthesizer"}`
  on 2026-10-13, PINNED. It names no `committer`, so the commit stage spawns untyped.
- `gate-guard.js`'s question arm, `checkAsk` (`tools/unattended/gate-guard.js:709-732`), resolves the
  checkout through `run-lease.js`'s `resolveRepo`, `readMemoryRoot` and `resolveLease`
  (`tools/unattended/run-lease.js:59`, `:107`, `:173-176`). It drops a lease whose phase is empty,
  `absent` or terminal, and asks `stop-guard.js`'s `runLiveness` and `parseLiveness`
  (`tools/unattended/stop-guard.js:107`, `:118`) whether the run is finished. `renderAskDeny`
  (`:739-757`) prints the lease head at `:744-746`. `main` dispatches the question arm before the
  `TOOLS` test, failing open (`:766-778`).
- The hook is wired on `Bash|PowerShell|AskUserQuestion` (`tools/unattended/gate-guard.fragment.json:4`,
  `.claude/settings.json:23`).
- The role index maps each role to its catalogue `workflow`, and only `gov-spec-writer` maps to
  `spec-write` (`.claude/roles.json`, read 2026-10-13).
- The hooks kit `agent-cap` requires `settings-merge` and `kickoff-manifest` only
  (`tools/hooks/kit.toml:9`). The unattended kit requires `review-harness`, which requires
  `agent-cap` (`tools/unattended/kit.toml:12`, `tools/workflows/kit.toml:9`). A lease exists only
  where the unattended kit is installed.
- No hooks-kit file reaches another kit's file: a sibling kit is a render token, and an engine
  reaches one through `resolve_kit_dir` (`tools/hooks/README.md:524-534`). The install-prefix gate
  bans a kit name typed as a path segment (`tools/check-install-prefix.sh:46-55`).
- `agent-cap.js` already reads `RUN.md`'s `## Run facts` inline for rule 0
  (`tools/hooks/agent-cap.js:1972-1994`), keyed by a build folder, never by the session.

### The fold call

A unit carrying `foldRev` is a fold unit, and a call is a fold call when any unit carries it. These
refusals sit at the head of the spec stage, after `specFolder`, before any agent spawns. Each
throws naming the key and the unit.

| Refusal | When |
|---|---|
| Mixed call | some units carry `foldRev` and some do not; the message names the ones without |
| `foldRev` | not an integer, or below 2 |
| `specPath` | not a non-empty string, or its `deriveRepoPath` fold does not open with `specFolder`, or carries a `..` segment |
| `specBriefPath` | not a non-empty string |
| `closes` | present on a fold unit: a fold writes no header verb |
| `specAudit` | present on a fold call: a fold never audits |
| `roles.specWriter` | absent on a fold call: the fold prompt leans on the role for the spec format |

The other audit-shaped arguments are already refused beside no `specAudit` (`:360-370`), so they
need no row. `folding` is computed once, above `TOOL-aOrientedCast-27`'s `log(identity)`, because
the identity reads it.

### The fold writer

The fan of `:948-1000` runs unchanged in shape: the same slices, `chunk`, `boundedParallel` and
`SPEC_WRITERS`. On a fold call only the prompt and the options change.

- `renderRoster` ends a fold unit's line with ` | fold to rev-<foldRev>` in place of its brief part.
  A unit with no `foldRev` prints as today.
- The prompt is `GROUND`, the role stamp, then: `FOLD every unit below, IN THIS ORDER.`, the group
  roster, and `Read the fold brief for each unit, and no other brief:` with its `specBriefPath`
  lines. Then, as prose: each spec exists at its line's path; fold into it what its brief asks and
  nothing else; raise the status header's rev to exactly the rev its line names, set the header
  date to today, keep every other header field; add that rev's §9 line naming the sections and ids
  it moved. A unit whose header already carries that rev or a higher one, or whose brief cannot be
  folded without a fork, goes in `refused` with the reason in the summary. Then the spec stage's own
  `AUTHOR ONLY — DO NOT COMMIT` sentence, and: return `folded`, one entry per folded unit, its id as
  the roster spells it, `rev` the integer the header now carries, and `moved` the scope tokens of
  the new §9 line.
- The options are `renderStageOpts('specWriter', { label: renderAgentLabel(<the group's ids>, 'spec-fold'), phase: 'Spec', schema: FOLD_SCHEMA })`.

```js
const FOLD_SCHEMA = {
  type: 'object',
  required: ['folded', 'refused', 'summary'],
  additionalProperties: true,
  properties: {
    folded: { type: 'array', items: { type: 'object', required: ['id', 'rev', 'moved'],
      properties: { id: SPEC_ENTRY, rev: { type: 'integer', minimum: 2 }, moved: { type: 'string' } } } },
    refused: { type: 'array', items: SPEC_ENTRY },
    summary: { type: 'string' },
  },
}
```

### The merge and the commit

- The merge loop of `:1053-1082` reads `r.folded` on a fold call where it reads `r.authored`
  otherwise. An entry whose id is no roster unit joins `unplaced`. An entry whose `rev` is not that
  unit's `foldRev` joins a list that throws, before the commit stage, naming the unit, the claimed
  rev and `foldRev`. Every other entry's id joins `specced.authored`, and `{id, rev, moved}` is kept
  for the return. A dead writer's units are refused, and an all-dead fan throws, as today.
- `resumeRemedy` reads, on a fold call: restore each named spec with `git checkout -- <its path>`,
  then re-invoke fresh, without `resumeFromRunId`, since a resume replays the cached answer.
- The commit stage runs as written on `authoredIds`. Two strings move on a fold call: the prompt's
  "just authored" reads "just folded", and the `git commit` line's message is
  `spec(<slug>): <id> rev-<foldRev> ...`, one pair per folded unit. Every other line of
  `commitBlock` is the spec stage's, so its foreign-change and input-check refusals are the same
  bytes.

### The fold return

After the commit stage, a fold call logs
`fold route: <n> spec(s) folded, <m> refused — no audit, disposal or hand-out` and returns, before
`phase('Audit')`:

```js
{ identity, slug, mode, base,
  folded: [{ id, rev, moved, specPath }],       // the committed path, after the path fill
  refused: specRefused,
  specCommit,                                    // { sha, checklist } or null when nothing committed
  nextAction,                                    // ACT on the checklist when one came back, then resume the step that asked for the fold
  note }                                         // 'DEGRADED — <m> fold(s) refused · ' when any, then 'fold complete'
```

`identity` is `renderAgentLabel(<every fold unit's id, space-joined>, 'fold, commit')`. It carries no
`roster`, `dispatch`, `verdict` or `audit` key.

### The spawn arm

In `gate-guard.js`, beside the question arm:

1. **`resolveLiveLeases(data)`** is `checkAsk`'s lease half, moved: the walk, the memory root, each
   lease of `data.session_id`, the phase filter and the liveness ask. It returns the live leases,
   each with `verdict`, or an empty list on any input `checkAsk` answered null for. `checkAsk`
   becomes `resolveLiveLeases` plus the questions, and its verdicts do not change.
2. **`renderLeaseHead(r)`** returns the two head lines `renderAskDeny` prints today (`:744-746`).
   `renderAskDeny` calls it, so its output does not change.
3. **`checkSpawn(data)`** answers null to allow, else `{ live, type }`:
   - `tool_input.subagent_type` is not a non-empty string: null;
   - `resolveRepo(cwd)` finds no checkout: null;
   - `.claude/roles.json` under the root cannot be read or parsed, or its `roles[type].workflow` is
     not `SPEC_WRITE_WORKFLOW`: null;
   - `resolveLiveLeases(data)` is empty: null.
4. **`renderSpawnDeny(live, type)`** is `renderLeaseHead(live[0])` and then this text:

```
A session driving an unattended run spawns no <type> agent directly: that role writes specs, and
a run's specs are written and revised through the build harness, unattended-build.js, whose writer
is typed, effort-set, journalled and schema-checked. A new spec is its spec stage. A revision is its
fold route: commit the fold brief, then call the harness with units each carrying specPath,
specBriefPath (that brief) and foldRev (the rev to reach). A session holding no lease may still
spawn <type> directly.
```

5. **`main`** dispatches `tool_name === SPAWN_TOOL` before the `TOOLS` test, wrapped and failing open
   as the question arm is.

`SPAWN_TOOL` is `'Agent'` and `SPEC_WRITE_WORKFLOW` is `'spec-write'`. The second restates the roles
catalogue's workflow name, and a suite arm pins it against gov's own index (AC10). Every input that
fails open for the question arm fails open here, and an unreadable liveness leaves the recorded
phase standing, as there.

The arm checks neither what the prompt asks for nor whether the role index tells the truth. It sees
only tool calls, so a harness's `agent()` spawns pass it by construction, which is the route it
names.

### The suites

- **`tools/workflows/unattended-build.test.sh`.** Fold arms over the runner `TOOL-aOrientedCast-27`
  leaves: the refusals of AC1, the spawn and return of AC2, the rev mismatch and dead fan of AC3,
  the block identity of AC4, and the unchanged non-fold trace of AC5. `FLOOR_ASSERTIONS` (`:2820`)
  rises by them.
- **`tools/unattended/gate-guard.test.sh`.** Spawn arms over the stub-driver fixture the question
  arms use (`:551-558`), its checkout given a `.claude/roles.json`: the deny of AC6, the allows of
  AC7, and the `SPEC_WRITE_WORKFLOW` liveness arm of AC10 over gov's own index. `FLOOR_ASSERTIONS`
  (`:647`) rises by them.

### Documentation

- `tools/unattended/VERBS.template.md`, "Drive the build as ONE program" (`:722-745`), gains the
  fold route in one sentence group: a revision is a call of the same harness whose `units` each
  carry `specPath`, `specBriefPath` and `foldRev`, after the fold brief is committed, since the
  commit stage refuses an uncommitted change under the memory root; the call authors, audits and
  hands out nothing; a direct spec-writer spawn from the session holding the run's lease is refused.
  The diverged-unit sentence (`:758-760`) and the CONVERGING bullet (`:783-785`) point at that route
  instead of a rendered handoff.
- `tools/roles/SKILL.template.md`, stage 5 step 4 (`:66-70`): commit the revision record, then call
  the build harness with `mode: 'attended'`, `units` holding that one unit with `specPath`,
  `specBriefPath` the record and `foldRev` its header rev plus one, no `planState`, and stage 3's
  `roles` and `efforts`; then dispatch the unit again.
- `tools/workflows/README.md`: the builder's hand-back bullet (`:380-384`) names the fold route, and a
  bullet after it, `**The fold route.**`, gives §4 "The fold call", "The fold writer" and "The fold
  return" in prose.
- `tools/unattended/README.md`, "The act is refused at the tool call" (`:87-100`): the matcher gains
  `Agent`, and a paragraph gives the spawn arm, its key and what it does not check.
- `gate-guard.js`'s header gains THE SPAWN ARM beside THE QUESTION ARM, and WHAT IT NEVER DENIES
  gains a spawn from a session with no live lease and a spawn of any other role.
- `help/roles.md`, "What the hooks refuse" (`:82-96`): a session holding an unattended run's lease
  cannot spawn the spec writer directly, and writes and revises specs through the build harness.

### Kit versions

One step for each kit this unit moves, from its value at this unit's parent commit.

- **Unattended**: `KIT_UNATTENDED_VERSION` (`tools/unattended/unattended.sh:66`), the same-line
  markers of the four `.sh` carriers and every shipped document's marker that
  `tools/check-kit-versions.sh:282-324` pairs with it, the `.js` courtesy markers, and the rendered
  copies under `memory/guides/` and `.claude/skills/unattended/`. 1.106 to 1.107.
- **Review harness**: the `version:` line and both markers at the head of
  `tools/workflows/tier2-review.template.js` and its render, one step past `TOOL-aOrientedCast-27`'s
  1.50, because every file under that directory ships under this entry
  (`tools/workflows/kit.toml:3-9`).
- **Roles**: `KIT_ROLES_VERSION` (`tools/roles/roles_lib.py:25`) and the markers of
  `tools/roles/README.md:1`, `tools/roles/SKILL.template.md:5` and `.claude/skills/build/SKILL.md:5`,
  one step past `TOOL-aOrientedCast-27`'s.
- The hooks kit does not move. The `unattended-build@` identity marker stays, as
  `TOOL-aOrientedCast-27` §4 "Kit versions" left it.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `resolveLiveLeases`, `checkSpawn`, `renderSpawnDeny`, `renderLeaseHead` | functions in `gate-guard.js`, each added to `module.exports` | `js.function`; `lexicon.py --suggest <name> --as js.function` answered OK for each |
| `SPAWN_TOOL`, `SPEC_WRITE_WORKFLOW` | constants in `gate-guard.js`, exported | none: `js.constant` is undeclared |
| `FOLD_SCHEMA`, `folding` | constants in the build template and its render | none: `js.constant` is undeclared |
| `foldRev` | a `units[]` key of the build harness | none: no argument-key cell is declared |

### Files touched (estimate)

`tools/workflows/unattended-build.template.js`
`tools/workflows/unattended-build.js`
`tools/workflows/unattended-build.test.sh`
`tools/workflows/tier2-review.template.js`
`tools/workflows/tier2-review.js`
`tools/workflows/README.md`
`tools/unattended/`
`memory/guides/UNATTENDED-PROTOCOL.md`
`memory/guides/UNATTENDED-ASKS.md`
`memory/guides/UNATTENDED-STOPS.md`
`memory/guides/UNATTENDED-VERBS.md`
`memory/guides/PLAYBOOK-TEMPLATE.md`
`.claude/skills/unattended/SKILL.md`
`.claude/settings.json`
`tools/roles/roles_lib.py`
`tools/roles/README.md`
`tools/roles/SKILL.template.md`
`.claude/skills/build/SKILL.md`
`help/roles.md`
`memory/map/features/unattended.md`
`memory/map/features/review-harnesses.md`
`memory/map/generated/`

`tools/unattended/` declares the hook, its fragment, its suite, the verbs template, the kit README
and every carrier of the kit's version marker. `tier2-review.template.js` and its render move their
version line and nothing else.

### Rollout

- **Order 29, after `TOOL-aOrientedCast-27`.** It shares the build template, its render and suite,
  the review template's version line, `tools/workflows/README.md`, the roles kit's library, README
  and Skill template, the rendered `/build` Skill, `help/roles.md`, the review-harnesses dossier and
  the generated map. The write sets are not disjoint, so this unit builds once `-27` has landed.
  It also calls what `-27` builds: `renderAgentLabel`, the run's `identity` and the build suite's
  stage-keyed stub runner. Without them the fold writer's label and the fold return's `identity`
  have nothing to call, and AC2's label reads fail. This is written here and not as a §3 edge,
  because `-27` declares no reciprocal line and this unit's writer does not edit that spec.
  `TOOL-aOrientedCast-25` lands before `-27` and shares the roles files; `TOOL-aOrientedCast-26`
  shares none.
- **Renders.** The builder re-renders the harness renders with
  `bash tools/workflows/check-protocol-parity.test.sh --render`, the unattended kit with
  `bash tools/unattended/adopt-unattended.sh`, as `TOOL-aOrientedCast-22` did, and the map with
  `python tools/codebase-map/gen_map.py --write`. The main loop's second pass re-renders the `/build`
  Skill with `bash tools/roles/adopt-roles.sh --scaffold`, as `TOOL-aOrientedCast-27` does.
- **The matcher.** Edit the fragment, then re-merge gov's settings with
  `python tools/settings-merge.py --fragment tools/unattended/gate-guard.fragment.json`.
- **Binding.** A settings edit is live on the next tool call
  (`memory/gotchas/settings-edit-takes-effect-mid-session.md`), and the hook script is read afresh on
  every call. So once the hook and the re-merged settings are in the tree a session's hooks run from,
  that session's next direct spec-writer spawn under a live lease is refused. For this run, every
  spec revision after this unit lands, the close's included, goes through the fold route.
- Adopters receive the arm and the fold route at `govkit update`, and the matcher at their next
  settings merge. No `watch:` path of the kickoff manifest moves. Rollback is a revert of the unit's
  commits, a re-merge of the fragment and the three re-renders.

### Alternatives rejected

- **The refusal in `agent-cap.js` rule 6**: §8 F1.
- **A `mode: 'fold'`, or a sibling harness**: §8 F2.
- **Keying the role on the call's `description` or on the name `gov-spec-writer`**: §8 F3.
- **A call mixing fold units and units to author.** One call would then author, fold and hand out a
  roster over half of its units, and the brief asks the fold route to hand out nothing.
- **One writer per fold unit.** The spec stage's slice-and-cap grouping already bounds the agent
  total, and a second grouping rule would be a second answer to one question.
- **A fold route that refuses a unit by reading its header rev.** The runtime has no filesystem; the
  writer refuses on the rev it reads, and the program refuses the rev it claims.

## 5. Production-readiness checklist

- security — The arm only narrows: it refuses a spawn and writes nothing. It reads the role index
  and the run-state records the question arm already reads, and fails open on every unreadable input
  but the liveness, as that arm does. The fold route adds no write class: the spec writer writes the
  spec its role already may, and the commit stage's git block is unchanged.
- perf / scale — One small JSON read per `Agent` call. The lease scan and the driver's
  `--liveness`, 3.9 s on node a (PINNED 2026-10-13 in `TOOL-aOrientedCast-24` AC8), run only for a
  spec-writer spawn. A fold call spawns at most `SPEC_WRITERS` writers and one committer.
- error / empty / loading states — A malformed fold call refuses by name before any spawn. A dead
  writer's units are refused and named, an all-dead fan throws, a rev mismatch throws before the
  commit, and nothing committed returns `specCommit: null` with a DEGRADED note.
- observability — The fold writers carry `<slug> · <ids> · spec-fold` labels, the run's first log
  line and `identity` read `<slug> · <ids> · fold, commit`, and the journal feeds
  `handoff.py agents --run`. The deny names the run, its phase, liveness and record, and the route.
- risks — The main loop of this run loses its direct fold route the moment the settings land
  mid-session; the fold route is its replacement. The role body's done sentence speaks of
  authoring, while the fold prompt names a different return; the role says the harness's shape
  wins. `SPEC_WRITE_WORKFLOW` is a restated catalogue name, pinned by AC10.
- testing — The direct probes and fixtures of §6 in the pass; the `New arm:` lines of §7, observed
  RED then GREEN by the main loop at the close.
- migration — None: no stored shape changes, and a call without `foldRev` runs as before (AC5).
- user docs — `help/roles.md` (S7).

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. Each runs the unit's own code over a
scratch fixture or a stub, or reads a file. `<c>` is the unit's commit.

Stub T is `TOOL-aOrientedCast-27` §6's: the build suite's `run_wf` runner copied into a scratch
script, looking up its returns by the text after the label's last ` · ` and printing `label:` and
the whole label before each `agent:` line. It evaluates a render with `node`. FOLD is these args,
and OK is these returns, with `<sha>` forty hex digits:

```json
{"repo": "C:/r", "slug": "tB", "scratch": "C:/s", "roles": {"specWriter": "gov-spec-writer"},
 "efforts": {"specWriter": "xhigh"},
 "units": [{"id": "A-tB-1", "order": 1, "foldRev": 2,
            "specPath": "memory/builds/tB/spec/2026-10-13-spec-A-tB-1.md",
            "specBriefPath": "memory/builds/tB/prompts/2026-10-13-prompt-A-tB-1-2-fold-brief.md"},
           {"id": "A-tB-2", "order": 2, "foldRev": 2,
            "specPath": "memory/builds/tB/spec/2026-10-13-spec-A-tB-2.md",
            "specBriefPath": "memory/builds/tB/prompts/2026-10-13-prompt-A-tB-2-2-fold-brief.md"}]}

{"spec-fold": {"folded": [{"id": "A-tB-1", "rev": 2, "moved": "§4 AC2"},
                          {"id": "A-tB-2", "rev": 2, "moved": "§6"}], "refused": [], "summary": "ok"},
 "commit": {"committed": true, "sha": "<sha>", "why": "", "summary": "ok", "checklist": "",
            "specs": [{"id": "A-tB-1", "path": "memory/builds/tB/spec/2026-10-13-spec-A-tB-1.md"},
                      {"id": "A-tB-2", "path": "memory/builds/tB/spec/2026-10-13-spec-A-tB-2.md"}]}}
```

Fixture G is `TOOL-aOrientedCast-24` §6's gate-guard fixture: a scratch kit dir holding copies of
`tools/unattended/gate-guard.js`, `tools/unattended/stop-guard.js` and
`tools/unattended/run-lease.js` beside a stub driver printing a chosen liveness, in
`TOOL-aOrientedCast-22` §6's fixture checkout with build `fx` leased to `tSess-1`. Its checkout gains
`.claude/roles.json` holding `gov-spec-writer` with workflow `spec-write` and `gov-builder` with
workflow `build`, each `agent: true`. Payload S is
`{"tool_name": "Agent", "session_id": "tSess-1", "cwd": <the checkout>, "tool_input": {"subagent_type": "gov-spec-writer", "prompt": "x", "description": "fx · spec-write"}}`.
Each staged break is restored before the next.

- **AC1** — When stub T runs `tools/workflows/unattended-build.js` over FOLD with one change each —
  `foldRev` dropped from `A-tB-2`; `foldRev` `1`; `foldRev` `"2"`; a `specPath` under
  build `tC`'s spec folder; `specBriefPath` dropped; `closes` `["ASK-1"]` on `A-tB-1`;
  `specAudit` `2026-10-13` with `base` `abcdef1`; `roles` `{}` — each prints a `THROW` line naming
  the key of §4 "The fold call" it breaks, and no `agent:` line.
  Red when: a malformed fold call spawns a writer, or a mixed call authors one half.
- **AC2** — When stub T runs `tools/workflows/unattended-build.js` over FOLD with OK, its first `log:`
  line is `log:tB · A-tB-1 A-tB-2 · fold, commit`; its `label:` lines read
  `tB · A-tB-1 · spec-fold`, `tB · A-tB-2 · spec-fold` and `tB · specs · commit`, one each; each
  writer's `type:` line ends `gov-spec-writer` and its `effort:` line ends `xhigh`; each writer's
  `prompt:` line holds `FOLD every unit below`, `fold to rev-2`, its own `specBriefPath` and
  `DO NOT COMMIT`. No `workflow:` line and no label ending `dispose` appears. The RESULT line opens
  `RESULT {"identity":"tB · A-tB-1 A-tB-2 · fold, commit",`, its `folded` holds both units at rev 2
  with their `moved` and `specPath`, `refused` is `[]`, and it carries no `roster` or `dispatch` key.
  Red when: a fold writer spawns untyped, at no effort or under another stage word, or the call
  audits or hands out a roster.
- **AC3** — When OK's `A-tB-1` entry carries `rev` 3, stub T prints a `THROW` line naming `A-tB-1`,
  `3` and `foldRev 2`, and no `label:` line ending `commit`. When `spec-fold` returns `null`, it
  prints a `THROW` line saying every writer returned nothing. When OK's writer lists `A-tB-2` in
  `refused` and not in `folded`, the RESULT's `refused` is `["A-tB-2"]`, its `note` opens
  `DEGRADED`, and the commit message names `A-tB-1 rev-2` alone.
  Red when: a claimed rev other than `foldRev` is committed, or a refused fold goes unreported.
- **AC4** — When the commit stage's `promptjson:` line of the AC2 run is decoded, and so is the one of
  a run over FOLD with every `foldRev` removed and returns `{"spec-write": {"authored": ["A-tB-1", "A-tB-2"], "alreadyPresent": [], "refused": [], "summary": "ok"}, "commit": <OK's commit>}`,
  the two fenced `sh` blocks differ in exactly one line, the `git commit` line, whose fold message
  reads `spec(tB): A-tB-1 rev-2 A-tB-2 rev-2`.
  Red when: the fold route's commit block drops or rewrites a refusal of the spec stage's block.
- **AC5** — When stub T runs the render at `<c>` and the render from
  `git show <c>~1:tools/workflows/unattended-build.js` over FOLD with every `foldRev` removed and
  AC4's authoring returns, the two outputs are byte-identical; so are they with `mode` `attended`
  and each unit given `planState` `MISSING`.
  Red when: a call without `foldRev` sees a changed prompt, label, log line or return.
- **AC6** — When payload S is piped to fixture G's copied `gate-guard.js` with the record at
  `BUILDING` and the stub printing `verdict: LIVE`, it exits 2, and stderr names `fx`, `BUILDING`,
  `liveness LIVE`, `unattended-build.js`, `foldRev` and `gov-spec-writer`.
  Red when: a leased session's direct spec-writer spawn is admitted, or the refusal omits the
  harness route.
- **AC7** — With fixture G, payload S exits 0 with an empty stderr when its `session_id` is
  `tSess-2`, when its `subagent_type` is `gov-builder`, when `.claude/roles.json` is removed, when
  the record is at `LANDED`, and when the record is at `LANDING` and the stub prints
  `verdict: TERMINAL`. With the stub exiting 1 and the record at `BUILDING` it exits 2, and stderr
  says the liveness could not be read.
  Red when: an attended session, another role or a finished run is refused, or an unreadable
  liveness admits a spawn.
- **AC8** — When `TOOL-aOrientedCast-24` AC6's and AC7's `AskUserQuestion` payloads are piped to
  fixture G's copied `gate-guard.js`, and to a copy of `git show <c>~1:tools/unattended/gate-guard.js`
  placed beside the same stubs, each pair exits with the same status and byte-identical stderr.
  Red when: moving the lease reader or the head line changed a question-arm verdict or message.
- **AC9** — When
  `python -c "import json, sys; print(json.load(open(sys.argv[1]))['matcher'])" tools/unattended/gate-guard.fragment.json`
  runs it prints `Bash|PowerShell|AskUserQuestion|Agent`, and
  `grep -c '"matcher": "Bash|PowerShell|AskUserQuestion|Agent"' .claude/settings.json` prints 1.
  Red when: the hook is not wired on `Agent`, in the fragment or in gov's settings.
- **AC10** — When
  `node -e "const g = require('./tools/unattended/gate-guard.js'); const r = require('./.claude/roles.json').roles; console.log(Object.keys(r).filter((k) => r[k].workflow === g.SPEC_WRITE_WORKFLOW).join(','))"`
  runs in this checkout, it prints `gov-spec-writer`.
  Red when: the restated workflow name matches no role, so the arm can never fire.
- **AC11** — When
  `grep -c "foldRev" tools/unattended/VERBS.template.md tools/roles/SKILL.template.md tools/workflows/README.md help/roles.md tools/unattended/README.md tools/unattended/gate-guard.js`
  runs it prints at least 1 for each file;
  `grep -n "spawn .gov-spec-writer. on it" tools/roles/SKILL.template.md` prints nothing; and
  `grep -c "Bash|PowerShell|AskUserQuestion|Agent" tools/unattended/README.md` prints at least 1.
  Red when: a page that says how a spec is revised still names a direct spawn, or the route is
  undocumented.
- **AC12** — When `KIT_UNATTENDED_VERSION` is read from `git show <c>~1:tools/unattended/unattended.sh`
  and from `tools/unattended/unattended.sh`, the second is one minor step above the first, and
  `git grep -l "gov:kit unattended@<the first>" -- tools/unattended/ memory/guides/ .claude/skills/unattended/`
  prints nothing. The `version:` value of
  `tools/workflows/tier2-review.template.js` and `KIT_ROLES_VERSION` in `tools/roles/roles_lib.py`
  each read one step above their `<c>~1` values, and
  `grep -c "gov:kit roles@<the second>" tools/roles/README.md tools/roles/SKILL.template.md .claude/skills/build/SKILL.md`
  prints 1 for each file. `git diff --quiet <c>~1 <c> -- tools/hooks/` exits 0.
  Red when: a kit's shipped bytes move with no step, a carrier keeps the old value, or the hooks
  kit moves.
  permission: the rendered `/build` Skill reads the roles step only after the main loop's second
  pass.
  figure: DERIVED, each as its `<c>~1` value plus one step.
- **AC13** — When `grep -c "TOOL-aOrientedCast-28" memory/map/features/unattended.md` runs it prints
  at least 1, and `grep -c "foldRev" memory/map/features/review-harnesses.md` prints at least 1.
  Red when: a dossier misses the route or the arm.
- **AC14** — When, on `<c>`, the added and removed lines of
  `git diff -U0 <c>~1 <c> -- tools/workflows/unattended-build.template.js` are compared with those of
  the same command over `tools/workflows/unattended-build.js`, they are identical apart from the
  rendered tokens, and so are those of `tools/workflows/tier2-review.template.js` and
  `tools/workflows/tier2-review.js`.
  Red when: an edit reached a template and not its render, or the reverse.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `unattended skill size` · `hook destinations (every declared hook path ships)` · `check-wiring self-test` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `roles adopter self-test` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `govkit selfcheck` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the fold arms, against the fold refusals staged out, then the merge's rev compare staged to accept any rev, then the commit message staged to the authoring form · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/unattended/gate-guard.test.sh · covers AC6 AC7 · the spawn arms, against `checkSpawn` staged to return null, then its `roles[type].workflow` test staged out so every role is refused · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/unattended/gate-guard.test.sh · covers AC10 · the `SPEC_WRITE_WORKFLOW` liveness arm over gov's index, against the constant staged to `spec-writer` · `FLOOR_ASSERTIONS` raised by its assertion

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — Which hook carries the refusal of a leased session's direct spec-writer spawn?**
  (a) Rule 6 of `tools/hooks/agent-cap.js`, as the brief names it, requiring `run-lease.js` and
  `stop-guard.js` from the unattended kit by path; (b) rule 6 with its own lease scan; (c) the
  unattended kit's `gate-guard.js`, its matcher widened to `Agent`, sharing the question arm's lease
  reader. (a) spells a sibling kit's path in a hooks-kit file, which the install-prefix gate bans and
  this spec's §7 runs, so veto 1 discards it; the hooks kit has no JS route to a sibling kit, and the
  hooks kit does not require the unattended kit. (b) is the copy the brief rules out, and it could
  not ask the driver's liveness without the same cross-kit path, so its answer would differ from the
  question arm's for a finished run. (c) is one reader for both arms, in the kit that owns the
  lease, and repeats `TOOL-aOrientedCast-22` §8 F1, which put the question arm there over the same
  options. It costs a widened matcher, which that unit already took. No veto applies to it.
  Recommendation: (c).
  RESOLVED (agent, 2026-10-13, delegated): (c), as §4 "The spawn arm" states it.
- **F2 — Is the fold route a new mode, a new `units` field, or a sibling harness?**
  (a) A third `mode` value, `fold`; (b) a `foldRev` key on each `units[]` entry, the fold brief
  riding the existing `specBriefPath`; (c) a sibling harness script. `mode` already selects
  attended or unattended grounding, and a fold runs in both, so (a) would need a second axis
  anyway. (c) cannot import the spec stage's role, effort, label and commit handling, so it copies
  them, and it is a new declared harness for the role index and the catalogue, a new public surface
  under veto 2. (b) reuses the fan, `renderStageOpts`, the merge and the commit stage, and adds one
  argument key. Recommendation: (b).
  RESOLVED (agent, 2026-10-13, delegated): (b), as §4 "The fold call" states it.
- **F3 — How does the spawn arm know the call spawns the spec writer?**
  (a) The role index's `workflow` for the `subagent_type` equals `spec-write`; (b) the call's
  `description` ends ` · spec-write`, which `TOOL-aOrientedCast-27`'s rule 6 step holds true; (c) the
  `subagent_type` is `gov-spec-writer`. (c) names gov's role and misses an adopter's own name. (b)
  parses the spawn name in a third place and holds only where the hooks kit's rule 6 is armed. (a)
  reads the one field the catalogue owns, switches on exactly where `.claude/roles.json` exists, as
  `help/roles.md` says every refusal does, and its restated workflow name is pinned by AC10.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), with `SPEC_WRITE_WORKFLOW` pinned by AC10.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "revise an existing spec to a new rev through the build
harness as a typed spec writer agent and commit it"` ranked name-stem neighbours only (`write`,
`build_commit`, `parse_spec_h1`), none of which spawns or commits a spec. The seam this unit extends
is the build harness's own spec stage: its fan, `renderStageOpts`, the merge and the commit stage in
`tools/workflows/unattended-build.template.js`. `"refuse an Agent spawn from the session holding a
live unattended run lease"` ranked `resolveLease` in `tools/unattended/run-lease.js` among stem
neighbours. The seam for the refusal is `checkAsk` in `tools/unattended/gate-guard.js`, whose lease
half becomes `resolveLiveLeases`. The recall probe surfaced the sixth addendum, the brief, the
roster row, `TOOL-aOrientedCast-27`'s naming spec, and `TOOL-aDeferredBar-14`, an unrelated driver
fold step. `python tools/memory-tree/gotchas.py --for-paths` over the harness template, the hook,
its fragment and the two doc templates selected `fixture-passes-by-finding-nothing`,
`staged-break-substitutes-a-synthetic-value`, `two-answers-to-one-question` and
`guard-above-a-fold-makes-its-fallback-dead`. AC5's and AC8's byte-identity checks, §7's code-level
staged breaks and AC10's liveness pin answer them. Where the brief and the code disagreed: the brief
places the refusal in `agent-cap.js`, and the kit boundary moves it (§8 F1).

Recall terms used: `fold rev-N spec-writer harness unattended-build specWriter efforts lease gate-guard spawn direct`
