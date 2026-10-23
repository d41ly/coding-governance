# TOOL-dGroundRules-10 — the agent limit as runtime.agents-in-flight, rendered into the harness's settings, agent-cap's counting retired

**Status:** DEFERRED · rev-3 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dGroundRules-12

**Carries:** cl-dClosedLoop-0016@df63b6eb whole

**Carries:** node:policy-key.runtime.agents-in-flight

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-11 |
| [2026-10-23-prompt-TOOL-dGroundRules-10-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-10-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-10-span-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-10-span-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-1 TOOL-dGroundRules-11 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The agent limit today is agent-cap's lower-only cap: five direct-spawn claims per prompt id, a claim
freed 45 minutes after it was made, Workflow agents never counted, and a kit conf as its carrier that
can only lower it (gap-rt-34; `research-agent-cap.md` §2, probes B, F, H and I). This unit makes
`runtime.agents-in-flight` the one carrier of the limit: the policy reader resolves it, `.agent-cap.conf`
read as a legacy home whose `FANOUT_CAP` only ever lowers it, and a render writes it into the harness's
own two concurrency settings in `.claude/settings.json`. In the same unit agent-cap's slot ledger, its
ban on raw `parallel` and `pipeline`, the concurrency half of its bound rule, its clamp of every bound
to 1 to 5, its refusal of a set `AGENT_CAP` and its print mode retire, their readers are re-pointed to
the policy reader, and the hook keeps one check of the limit: that the settings a session starts under
do not exceed it.

## 2. Scope (IN)

- **S1** — The legacy home. `read_legacy_fanout(repo, rev)` in `tools/policy/policy.py` reads
  `.agent-cap.conf` at the checkout root, at the same revision `resolve` reads the policy file, in
  the grammar `loadDeclaredCap` reads today (`tools/hooks/agent-cap.js:1628-1657`): a line
  `FANOUT_CAP=<n>` or `FANOUT_CAP="<n>"`, a BOM and a trailing CR tolerated, the last such line
  winning. `resolve("runtime.agents-in-flight")` returns the smaller of the value its resolution
  order gives and that line's integer. A lowering keeps the source and appends to the reason
  `lowered to <n> by FANOUT_CAP at .agent-cap.conf:<line>`; a value at or above the resolved one
  changes nothing and appends `FANOUT_CAP=<n> at .agent-cap.conf:<line> does not lower it`. A value
  that is not an integer of at least 1 refuses, exit 2, as
  `policy: refused · .agent-cap.conf:<line> · FANOUT_CAP must be an integer of at least 1`. There
  is no upper bound. Observed by AC1, AC2, AC3.
- **S2** — The render. `python tools/policy/policy.py settings [--write|--check] [<settings-file>]`,
  the file defaulting to `.claude/settings.json` under the repository root. It sets
  `env.CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` and `env.CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` to
  the limit `resolve` gives at `rev="HEAD"` (§8 F4), as decimal strings, keeps every other key and its
  order, creates `env` when absent, and writes `json.dumps(obj, indent=2, ensure_ascii=False)` plus a
  newline, the shape `tools/settings-merge.py:506-507` writes. `--check` exits 1 printing one line
  per env key that is absent or differs, `policy: settings · <file> · env.<KEY> is "<v>",
  runtime.agents-in-flight resolves <n>`, and 0 when both match; `--write` writes only when they
  differ. A refusal from `resolve` exits 2 unchanged. Observed by AC4, AC5.
- **S3** — The landing regeneration. A `[[generated]]` row in `tools/policy/kit.toml`, `stage = 1`,
  whose `write` and `check` argv are the two S2 modes, so `tools/run-gates/regen.py --write` renders
  it at the merge commit of every landing (`tools/push-main.sh:749-772`) and `--check` grades it
  before a bar's first leg. Gov's own `.claude/settings.json` is rendered in this unit. Observed by
  AC5.
- **S4** — agent-cap's retirements, in `tools/hooks/agent-cap.js`:
  - rule 4, the direct-spawn slot ledger: `guardAgentSpawn`, `sweepTurns`, `gitCommonDir`,
    `SLOT_TTL_MS` and every helper only they call;
  - rule 1, the ban on raw `parallel` and `pipeline`: `offendingLines` and its denial;
  - rule 3, the bound rule's concurrency half: `capFindings`, its denial, and every helper only it
    calls;
  - the clamp: `loadDeclaredCap`, `CAP_CONF`, `EFFECTIVE_CAP`, `CAP_SOURCE`, `renderCapSource` and the
    unused `CAP`, so no value outside 1 to 5 is refused and the hook reads no conf;
  - the refusal of a set `AGENT_CAP` (`:2241-2257`) and the `--print-cap` print mode (`:2191-2211`).
  Rules 0, 2, 5 and 6 and the `--only=` selector stay. Rule 2's bound is `MAX_VERIFIERS`, the
  review protocol's verify total (§8 F2). `KIT_AGENT_CAP_VERSION` moves to `'2.0'` and the header
  states only the kept rules. Observed by AC6, AC7, AC8, AC9.
  **Readers:**
  by name: `tools/workflows/check-verifier-fanout.sh`, `tools/workflows/check-protocol-parity.test.sh`,
  `tools/workflows/check-verifier-fanout.test.sh`, `tools/hooks/agent-cap.test.sh`,
  `tools/govkit/selftest.py`, `tools/workflows/unattended-build.test.sh`, `tools/workflows/kit.toml`,
  `tools/workflows/REVIEW-PROTOCOL.template.md`, `memory/guides/REVIEW-PROTOCOL.md`, `README.md`,
  `WIRE-INTO-PROJECT.md`, `tools/hooks/README.md`, `tools/check-wiring.sh` (a comment naming the
  `AGENT_CAP` class, kept as history).
  by value: `tools/workflows/check-protocol-parity.test.sh` renders `{{FANOUT_CAP}}` from the
  print mode's answer, and `tools/workflows/check-verifier-fanout.sh` prints it on its clean line.
- **S5** — Rule 7, the settings in force, in `tools/hooks/agent-cap.js`, run for every `Agent` and
  `Workflow` call outside `--only=`, after rule 6. It locates `policy-mirror.js` in the `policy` kit
  beside the hooks kit, as `resolveHarnessName` probes the workflows kit (`agent-cap.js:109-117`); with
  none there it adds no rule. It reads the landed limit with `readPolicy("runtime.agents-in-flight",
  { repo })` (TOOL-dGroundRules-5), then `.claude/settings.json` and `.claude/settings.local.json` at
  the payload `cwd`'s checkout root, and takes for each of the two harness variables the value the
  harness applies, the local file's when set and else the project file's. It refuses, exit 2, when
  either is absent, not a positive integer, or above the limit, naming the file, the variable, both
  numbers and `python tools/policy/policy.py settings --write`. A `PolicyRefusal` refuses with its
  line. After rule 7 an `Agent` call exits 0. Observed by AC10, AC11.
- **S6** — The readers re-pointed. `tools/workflows/check-protocol-parity.test.sh` takes the
  `{{FANOUT_CAP}}` token from `policy.py get runtime.agents-in-flight --rev HEAD`, the policy kit
  located by the inlined `resolve_kit_dir`, and refuses to render, naming why, when the kit is absent
  or the answer is not a positive integer; its `[1-9]` case widens to any positive integer.
  `tools/workflows/check-verifier-fanout.sh` gives up its `--print-cap` verb, and its clean line names
  no number. The three review and drift-audit templates write `const MAX_VERIFIERS = 5` in place of
  the token, so the token carries only concurrency widths and `SPEC_WRITERS` (§8 F3), and their prose
  names the verify total as the hook's `MAX_VERIFIERS`. The four renders are regenerated.
  `tools/workflows/kit.toml` adds the `policy` kit to `requires`. Observed by AC12, AC13.
  **Readers:**
  by name: `tools/workflows/check-protocol-parity.test.sh`, `tools/workflows/check-verifier-fanout.test.sh`.
  by value: NO VALUE READERS — the verb relayed the hook's number, and the token render above, which
  S6 re-points, was its one caller to use the value.
- **S7** — The carriers. The review protocol's hard-cap and concurrency sections in
  `tools/workflows/REVIEW-PROTOCOL.template.md`, and its render `memory/guides/REVIEW-PROTOCOL.md`,
  state the verify total as the hook's and the at-once bound as `runtime.agents-in-flight`'s; the
  sentences in `README.md`, `WIRE-INTO-PROJECT.md`, `tools/hooks/README.md` and
  `tools/workflows/README.md` that describe agent-cap as it was before this unit are rewritten;
  `help/agent-limit.md` is new and `help/README.md` lists it. Observed by AC14.
- **S8** — The fixture cases, entries in `CASES` of `tools/policy/check_policy.py` whose names open
  `limit-`, each planting its input in the `--fixture` mode's temporary repository and asserting the
  outcome its criterion states; and `arm_mirror_landed`'s case, which TOOL-dGroundRules-5 hands over,
  run against `tools/hooks/agent-cap.js` where that unit wrote a fixture hook. Observed by AC1 to AC4,
  AC6 to AC11.
- **S9** — The live observation. `python tools/policy/check_policy.py --live` builds a fixture
  repository, renders its settings, and drives headless `claude -p` sessions in it whose agents each
  run a stamp script appending a start and an end line with `time.time_ns()` around a 20-second
  sleep; it computes each run's peak overlap from those lines and reads refusals from the session's
  `stream-json` output. Observed by AC15, AC16, AC17.

## 3. Non-goals (OUT)

- The in-flight ledger, the admission queue, the session-wide total and the direct bound under
  ultracode (`gap-rt-35`): dWellOiledMachine's hook pack. Until it arms, the limit binds direct
  spawns and each Workflow run separately, as v2:1216 states.
- Moving `FANOUT_CAP` into the key and retiring `.agent-cap.conf`: dSafePassage's step.
- Rules 0, 2, 5 and 6 of agent-cap, and its `--only=` selector: their homes are dFairHearing's and
  dBoundRoles' (`research-agent-cap.md` §5). Rule 2 changes only its comparand.
- Refusing an environment override of the two harness variables, which no hook can see the harness
  apply, and a guard over `.claude/settings.json` (the brief's S7 lists the guarded paths).
- The catalogue row for `runtime.agents-in-flight`, the file, the reader's resolution order and the
  JSON mirror: TOOL-dGroundRules-1, -2, -3 and -5.

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — the `policy` kit, its `kit.toml`, the catalogue row for `runtime.agents-in-flight` and the value the policy file holds, and `check_policy.py` with `CASES` and its `--fixture` mode; without them nothing resolves and no case runs
- **consumes-from** `TOOL-dGroundRules-2` — `resolve`, `Resolution` and the `get` verb, which S1 extends and S2 and S6 call
- **consumes-from** `TOOL-dGroundRules-3` — the resolution order whose result S1 lowers
- **consumes-from** `TOOL-dGroundRules-5` — `readPolicy` in `tools/policy/policy-mirror.js` and its `PolicyRefusal`, which rule 7 calls, and `arm_mirror_landed`, whose fixture hook S8 replaces with `tools/hooks/agent-cap.js`
- **hands-off** external — dWellOiledMachine: the in-flight ledger, the admission queue, the session total and the ultracode exemption (`gap-rt-35`)
- **hands-off** external — dSafePassage: the step that moves `FANOUT_CAP` into the key and retires `.agent-cap.conf`
- **hands-off** `TOOL-dGroundRules-15` — the conf lowering moved from the `resolve` wrapper into `resolve_read` (finding 2)
- **hands-off** `TOOL-dGroundRules-18` — the writer marker `gov:fixed-writers`, whose split rule 2 judges against the limit while verifiers stay at `MAX_VERIFIERS` (finding 13)
- **hands-off** `TOOL-dGroundRules-20` — `tools/hooks/agent-cap.js`, which the `limit-hook-` cases run, named in the `policy fixtures` guard (finding 35)
- **hands-off** `TOOL-dGroundRules-21` — the map card, the D7 arm, the settings file's resolution, the playbook-parity rows, the stale markers, the adopter's first render, rule 7's catch-all, the suite's oracle, the atomic write and the regenerated codebase map (findings 9, 34, 21, 33, 38, 42, 45, 43, 54, 40)

## 4. Design

The limit has one resolution, in the reader, and two outward copies, each derived and checked: the
harness's two settings and the `{{FANOUT_CAP}}` token in four rendered harnesses. The harness counts
agents in flight and knows when each one ends, which a `PreToolUse` hook cannot
(`research-agent-cap.md` §3): `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` refuses a direct spawn over it and
`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` queues a Workflow agent over it, per session and per run
(the same record, §3; the harness here is 2.1.304 by `memory/builds/dGroundRules/RUN.md`, above the
2.1.269 that record names, UNVERIFIED beyond the record). The hook keeps the one thing a call-time
check can see: the settings files the harness started from. The harness reads them from the working
tree, so rule 7 is what stops a hand-raised `env`, or a render left behind a lowering, from running
past the landed limit.

### Data model

- `.agent-cap.conf`: unchanged grammar, read only by `read_legacy_fanout`.
- `.claude/settings.json`: gains `"env": {"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS": "<n>",
  "CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS": "<n>"}`. Today it has no `env` key.
- `Resolution` keeps the four sources the brief's S4 fixes; a lowering is named in `reason` (§8 F5).

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `read_legacy_fanout` | py.function, lexicon `--suggest` OK on 2026-10-23 | `tools/policy/policy.py` |
| `render_settings` | py.function, lexicon `--suggest` OK on 2026-10-23 | `tools/policy/policy.py` |
| `settings` | CLI verb of `policy.py`, modes `--write` and `--check` | `tools/policy/policy.py` |
| `limit-conf-lowers`, `limit-conf-no-raise`, `limit-conf-malformed`, `limit-settings-render` | `CASES` entries | `tools/policy/check_policy.py` |
| `limit-hook-admits-eight`, `limit-hook-six-spawns`, `limit-hook-rules-kept`, `limit-hook-env-cap`, `limit-hook-settings-over`, `limit-hook-local-over` | `CASES` entries | `tools/policy/check_policy.py` |
| `--live` | CLI mode of `check_policy.py` | `tools/policy/check_policy.py` |
| `checkSettingsInForce` | js.function, rule 7 | `tools/hooks/agent-cap.js` |

### The hook after this unit

`main()` keeps, in order: the `--only=` selector, the payload parse and tool filter, rule 6, rule 7,
an `Agent` exit 0, rule 0, the script read, rule 2 with its deny message naming `MAX_VERIFIERS` where
it named `EFFECTIVE_CAP` and `renderCapSource()`, and rule 5. `boundedK` compares against
`MAX_VERIFIERS`. Rule 2's remedy keeps `boundedParallel(..., MAX_VERIFIERS)` as an example only. The
suite drops the arms of the retired rules (`tools/hooks/agent-cap.test.sh:1214-1227`, `:1237-1322`,
`:1917-2001` and the rule 1 and rule 3 corpora) and gains the arms §7 declares. A slot-ledger
directory an earlier version left under the git common dir is read by nothing and left in place.

### Migration

- An adopter with `.agent-cap.conf` keeps its lowering: the reader applies it and the render writes
  the lowered value. A value above 5, which every call refused before, now reads as a limit, lowering
  only when below the key.
- An adopter at `FANOUT_CAP=4` had a verify total of 4; it is now the hook's `MAX_VERIFIERS`, while
  its at-once bound is 4 in the harness.
- An adopter whose hooks kit updates before its policy kit installs has no `policy-mirror.js`, so
  rule 7 adds no rule there, and its renders refuse until the `policy` kit is installed, which the
  workflows kit now requires.

### Rollout

Live at landing: the landing's regeneration renders gov's settings, every session started after it
runs under them, and rule 7 refuses spawns in a worktree whose settings are missing or above the
landed limit until `policy.py settings --write` is run there.

### Files touched (estimate)

`tools/policy/policy.py` · `tools/policy/check_policy.py` · `tools/policy/kit.toml` ·
`.claude/settings.json` · `tools/hooks/agent-cap.js` · `tools/hooks/agent-cap.test.sh` ·
`tools/hooks/README.md` · `tools/workflows/check-verifier-fanout.sh` ·
`tools/workflows/check-verifier-fanout.test.sh` · `tools/workflows/check-protocol-parity.test.sh` ·
`tools/workflows/unattended-build.test.sh` · `tools/workflows/tier2-review.template.js` ·
`tools/workflows/tier2-review.js` · `tools/workflows/drift-audit-code.template.js` ·
`tools/workflows/drift-audit-code.js` · `tools/workflows/drift-audit-state.template.js` ·
`tools/workflows/drift-audit-state.js` · `tools/workflows/unattended-build.js` ·
`tools/workflows/kit.toml` · `tools/workflows/README.md` · `tools/workflows/REVIEW-PROTOCOL.template.md` ·
`memory/guides/REVIEW-PROTOCOL.md` · `tools/govkit/selftest.py` · `README.md` ·
`WIRE-INTO-PROJECT.md` · `help/agent-limit.md` · `help/README.md`

### Alternatives rejected

- **Keep the slot ledger, re-keyed per session.** `research-agent-cap.md` probe F: five idle claims
  refuse a sixth agent, and probe H: five claims aged 46 minutes admit five more while the first
  five run. It counts claims, not agents in flight.
- **A hook pack counting agents in flight now.** Whether SubagentStop fires for every way an agent
  ends is unmeasured (the same record, §4 B test 2), and the pack is dWellOiledMachine's.
- **Rule 7 reading the hook's own environment.** Whether a hook process inherits the settings `env`
  the harness applies is unmeasured here, and a rule that reads nothing when it does not would grade
  an empty population; the files are what the harness starts from and what a hand edit changes.

## 5. Production-readiness checklist

- security — the limit moves from a hook that only ever lowered it to the harness's settings. A hand
  edit of `env` in either settings file that raises it is refused by rule 7 at the next spawn; an
  environment override of the two variables can still raise it for a session and nothing here sees
  it. The retired `AGENT_CAP` refusal guarded a variable no longer read; refusing the harness
  variables' override belongs with dWellOiledMachine's hook pack.
- perf / scale — rules 1, 3 and 4 and their file and git reads leave the hook; rule 7 adds two small
  JSON reads and one `readPolicy`, which spawns git and the shim (TOOL-dGroundRules-5 §5 prices it).
- error / empty / loading states — an absent policy file resolves the catalogue default; an absent
  conf lowers nothing; a malformed conf or a refused policy refuses the render, the token render and
  rule 7, naming the line; an absent `env` is created by the render and refused by rule 7.
- observability — `policy.py get runtime.agents-in-flight --explain` names the source and any
  lowering; the S2 check and rule 7 each name the file, the variable and both numbers.
- risks — rule 7 refuses every spawn in a worktree whose settings are stale, which after a lowering
  lands is the intent, and after a branch raises the key before landing is the price of reading the
  landed limit. A session started before a lowering keeps its harness settings until it restarts.
  Under ultracode the harness does not enforce the direct bound.
- testing — AC1 to AC14 by fixture and probe; AC15 to AC17 by the live driver at the close; the
  `New arm:` lines under §7.
- migration — §4 Migration.
- user docs — `help/agent-limit.md`, new: how to raise or lower the limit by a policy write, what the
  render does, what rule 7 refuses and how to clear it, and what a conf lowering does.

## 6. Acceptance criteria

- **AC1** — When the `--fixture` run of `python check_policy.py` reaches
  `limit-conf-lowers`, which plants `FANOUT_CAP=2` in `.agent-cap.conf` with no policy value,
  `policy.py get runtime.agents-in-flight` prints `2` and `--explain` names `.agent-cap.conf:1`.
  Red when: `read_legacy_fanout` is not called and the answer is the catalogue default.
  figure: the default is DERIVED from the catalogue row at observation time.
- **AC2** — When the run reaches `limit-conf-no-raise`, which plants `FANOUT_CAP=8` under the key's
  default, `policy.py get runtime.agents-in-flight` prints the catalogue default and its reason says
  the line does not lower it.
  Red when: the conf raises the limit and the answer is `8`.
- **AC3** — When the run reaches `limit-conf-malformed`, which plants `FANOUT_CAP=abc`,
  `policy.py get runtime.agents-in-flight` exits 2 printing
  `policy: refused · .agent-cap.conf:1 · FANOUT_CAP must be an integer of at least 1`.
  Red when: a malformed lowering is ignored and the default is printed with exit 0.
- **AC4** — When the run reaches `limit-settings-render`, which commits `agents-in-flight = 8` under
  `[runtime]` and runs `policy.py settings --write`, both `env` keys hold `"8"`; after it commits a
  policy write of `6`, `policy.py settings --check` exits 1 naming both keys, and after `--write`
  both hold `"6"` and `--check` exits 0.
  Red when: either key is absent or keeps the earlier value after the second render.
- **AC5** — When `python policy.py settings --check` runs over this repository at the
  unit's commit, it exits 0, and `python tools/run-gates/regen.py --list` lists the S3 row.
  Red when: a hand edit sets either `env` value in `.claude/settings.json` to `50`.
- **AC6** — When the run reaches `limit-hook-admits-eight`, a fixture whose `.claude/roles.json`
  declares one `agent`-true role and one harness, under a landed limit of eight with settings
  rendered at eight and `FANOUT_CAP=8` planted in `.agent-cap.conf`, a handoff-valid `Agent` payload
  and a `Workflow` payload whose `scriptPath` is the registered harness each exit 0 through
  `node tools/hooks/agent-cap.js`.
  Red when: the hook still reads the conf, and both exit 2 with `must be an integer from 1 to 5`.
- **AC7** — When the run reaches `limit-hook-six-spawns`, six `Agent` payloads with one `session_id`
  and `prompt_id` and six `tool_use_id`s each exit 0 through `node tools/hooks/agent-cap.js`, and no
  `agent-cap` directory appears under the fixture's git common dir.
  Red when: the slot ledger survives and the sixth exits 2 with `5 of 5 claimed`.
- **AC8** — When the run reaches `limit-hook-rules-kept`, `Workflow` payloads whose scripts call raw
  `parallel` over an `items.map`, and `boundedParallel(thunks, 50)`, each exit 0 through
  `node tools/hooks/agent-cap.js`; one spawning a verifier per finding exits 2 naming `MAX_VERIFIERS`,
  and a ref-keyed verdict join exits 2.
  Red when: rule 1 or rule 3 survives, or rule 2 or rule 5 left with them.
- **AC9** — When the run reaches `limit-hook-env-cap`, `node tools/hooks/agent-cap.js` run with
  `AGENT_CAP=50` set over a clean script exits 0, and `git grep -n -- --print-cap -- tools` over the
  repository prints nothing.
  Red when: the `AGENT_CAP` refusal survives, or a reader still asks the retired print mode.
- **AC10** — When the run reaches `limit-hook-settings-over` under a landed limit of two, a
  `Workflow` payload exits 2 through `node tools/hooks/agent-cap.js` with settings rendered at `3`,
  naming `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` and `policy.py settings --write`; with no `env`
  it exits 2 the same way; at `2` it exits 0; and with `tools/policy/` absent from the fixture it
  exits 0.
  Red when: rule 7 is unwired and the payload at `3` exits 0.
- **AC11** — When the run reaches `limit-hook-local-over`, settings at `2` and
  `settings.local.json` setting either variable to `5` under a landed limit of two, the payload
  exits 2 naming the local file; and when `arm_mirror_landed` runs its case with the working-tree
  `policy.json` hand-edited to `8`, the real hook refuses settings at `3`.
  Red when: rule 7 reads only the project file, or reads the working-tree mirror.
- **AC12** — When the four renders are regenerated in this repository,
  `grep -c "const MAX_VERIFIERS = 5" tools/workflows/tier2-review.js` prints at least 1 and
  `grep -n "boundedParallel(thunks, cap = " tools/workflows/tier2-review.js` shows the value
  `policy.py get runtime.agents-in-flight` prints.
  Red when: the token still renders the print mode's `5`, or `MAX_VERIFIERS` renders the limit.
  figure: the width is DERIVED from the reader at observation time.
- **AC13** — When each of the four renders is piped as a `Workflow` script through
  `node tools/hooks/agent-cap.js --only=scripts`, each exits 0.
  Red when: a template still writes `const MAX_VERIFIERS = {{FANOUT_CAP}}` and rule 2 refuses a
  render above `MAX_VERIFIERS`.
- **AC14** — When
  `git grep -n "AGENT_CAP\|print-cap\|FANOUT_CAP" -- README.md WIRE-INTO-PROJECT.md tools/workflows/REVIEW-PROTOCOL.template.md memory/guides/REVIEW-PROTOCOL.md tools/hooks/README.md`
  runs, no line it prints says a set `AGENT_CAP` is refused, names the print mode, or calls
  `FANOUT_CAP` a ceiling of five; and `agent-limit.md` names `runtime.agents-in-flight` and
  `policy.py settings --write`.
  Red when: a carrier still teaches a rule this unit removed as live.
- **AC15** — When `python check_policy.py --live` runs a Workflow of four agents under
  a limit of two, the run's peak overlap is at most 2; under the control with no `env` rendered, the
  same run's peak reaches at least 3.
  Red when: the render is absent and the peak is 4 under the limit of two.
  permission: drives headless `claude` sessions in a fixture repository; the main loop's, at the close.
  cost: about five minutes and four short agents per run.
- **AC16** — When `python check_policy.py --live` has one session start three background
  `Agent`s in one message under a limit of two, at most two stamp at once and the third's tool result
  is an error with no stamp of its own; under the control, all three stamp and overlap.
  Red when: the third runs beside the first two.
  permission: as AC15. cost: as AC15.
- **AC17** — When `python check_policy.py --live` has one session start two Workflow
  runs of four agents each in one message under a limit of two, each run's peak overlap is at most 2,
  and the session's total peak is printed and not asserted, being the in-flight ledger's.
  Red when: either run's peak exceeds 2.
  permission: as AC15. cost: as AC15.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `check-wiring self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `hook destinations self-test` · `govkit selftest` · `lexicon naming predicates` · `govkit refusal join` · `govkit acceptance matrix` · `verifier fan-out` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `agent-cap restatement` · `kit version markers` · `memory hygiene`

New arm: tools/policy/check_policy.py --fixture · covers AC1 AC2 AC3 AC4 AC6 AC7 AC8 AC9 AC10 AC11 · the `limit-` cases in `CASES`, each planting its input in the temporary repository and asserting its outcome, in the `policy fixtures` leg TOOL-dGroundRules-1 declares · none
New arm: tools/hooks/agent-cap.test.sh · covers AC6 AC7 AC8 AC9 AC10 · a conf at `FANOUT_CAP=8`, six spawns in one prompt, a raw `parallel` script, a width of 50 and a set `AGENT_CAP`, each admitted, and settings above a fixture limit refused, staged by running each arm against the base revision's hook, `git show 3708a705:tools/hooks/agent-cap.js` in the suite's scratch copy · none
New arm: tools/govkit/selftest.py · covers AC12 · its fixture renderer arm, re-pointed from the print mode to the policy reader, staged by an absent `policy` kit · none
New arm: tools/workflows/unattended-build.test.sh · covers AC12 · its renderer arm at line 1997, re-pointed to the policy reader, staged by a reader answering a non-integer · none

AC5, AC13 and AC14 are probes the close reads directly; AC13 is also the `verifier fan-out` leg's
verdict. AC15 to AC17 are the main loop's live observation at the close, and no suite runs them.

## 8. Open questions

- **FACT-QUESTION · F1 — Is `DRAFT`, the status the spec brief names, a legal spec status?** Probe:
  `grep -n "OPEN · SPECCED" memory/HYGIENE.md` prints the seven tokens a spec header reuses (line
  105). Liveness: the line would print `DRAFT` if the vocabulary declared it. Observed 2026-10-23:
  it does not. RESOLVED (agent, 2026-10-23, delegated): `OPEN`, which TEMPLATE-SPEC gives as
  drafting, as `TOOL-dTrueNorth-2` §8 F1 settled the same question.
- **F2 — What does rule 2 compare against once the clamp retires?** (a) The hook's own
  `MAX_VERIFIERS`, the review protocol's verify total. (b) The smaller of `MAX_VERIFIERS` and the
  limit: the rendered harnesses would then need `MAX_VERIFIERS` at that smaller value while their
  widths carry the limit, so the renderer needs the verify total, which only the hook holds and whose
  print mode the clause retires (veto 1), or a second spelling of it (`[one-fact]`). (c) The limit
  unclamped, which lifts the protocol's verify total to the limit's default, a governance-carrier
  change no clause names (veto 2 outside the grant). `memory/guides/REVIEW-PROTOCOL.md:20` already
  separates the two numbers: the verify total "is not the concurrency cap wearing a different hat".
  Recommendation (a); rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none
- **F3 — What does the `{{FANOUT_CAP}}` token carry once the print mode retires?** (a) The resolved
  limit, through the policy reader, with the three `MAX_VERIFIERS` lines written as the hook's
  literal. (b) Retire the token and write every width as a literal, the harness's settings holding
  the at-once bound alone. (c) Keep it at the smaller of five and the limit. (b) deletes the token's
  readers where the clause says they are re-pointed (veto 1), and leaves a raised limit unread by
  `SPEC_WRITERS`; (c) needs the verify total outside the hook, as F2 (b) does. Recommendation (a);
  rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — Which revision does the settings render read?** (a) `rev=None`, the landed revision: the
  landing's regeneration runs at the merge commit before the push (TOOL-dGroundRules-5 §4), where the
  landed revision is still the previous tip, so a policy write's render lands one landing late and
  every bar in between reds on `regen.py --check`. (b) `rev="HEAD"`: the regeneration renders the
  merge being landed, so a policy write and its render land together, and a branch's own render
  matches its own policy file. An unlanded raise rendered on a branch then reaches that worktree's
  harness, which rule 7 refuses at the next spawn because it reads the landed limit; the clause's
  "never from the working tree" holds, `HEAD` being a commit. Recommendation (b); rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b). widens: none · relaxes: none
- **F5 — What `source` does a limit lowered by `.agent-cap.conf` carry?** The brief's S4 fixes four
  sources. (a) Keep them: the source is that of the value the conf lowered, and the reason names the
  conf line. (b) Add a fifth source, `legacy`, which respells S4 for every writer. Recommendation (a),
  which changes no shared interface; rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none
- **F6 — Does any hook read the limit, and to do what?** The brief's S6 and TOOL-dGroundRules-5's
  hand-off both have `agent-cap.js` read it through `readPolicy`. (a) No hook reads it: the harness
  enforces its settings, and `readPolicy` has no consumer in this build. (b) Rule 7: the hook refuses a
  spawn when the settings files the harness started from are missing or above the landed limit. (c)
  The hook counts spawns against the limit itself, which needs the in-flight ledger this clause leaves
  to dWellOiledMachine (veto 1, the clause's non-goal). (a) leaves a hand-raised `env` running past
  the owner's limit until a bar, a wider surface than the retired `AGENT_CAP` refusal left (veto 3),
  and leaves the mirror helper with no consumer. Rule 7 is a bound this spec adds beyond the clause,
  the weakest tier, and it satisfies every criterion the clause states. Recommendation (b); rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-15, TOOL-dGroundRules-18, TOOL-dGroundRules-20, TOOL-dGroundRules-21 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit's findings that repair this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-24 · §6 · AC12, AC14: a criterion code span rejoined onto one line so hygiene check 23 reads the criterion's tokens; no meaning change.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "render a policy value into the harness settings env
of .claude/settings.json"` ranked name-stem matches only (`render`, `render_role`, `load_policy`),
none of which writes `.claude/settings.json`. Read against source: `tools/settings-merge.py` is the one
writer of that file and wires hook fragments only (`:428-547`); it has no `env` mode, and it is a
separately versioned copy-installed kit, so this unit writes the file in the policy kit and matches its
`_dump` shape (`:506-507`) rather than adding a second purpose to it. The landing seam is
`tools/run-gates/regen.py`'s `[[generated]]` row, which `tools/push-main.sh:749-772` runs at every
landing: extended, not rebuilt. The conf grammar is `loadDeclaredCap`'s (`agent-cap.js:1628-1657`),
moved into the reader, so the conf keeps one parser. The kit locators are the inlined
`resolve_kit_dir` the verifier fan-out gate already carries and `resolveHarnessName`'s sibling probe in
the hook. The mirror read is `readPolicy`, TOOL-dGroundRules-5's. Recall hit [6]
(`2026-10-19-review-PLAY-dClosedLoop-1-night-pass-two-b.md:119`) says the clause retires only the
ledger, the conf, the refusal and the print mode; the clause at `df63b6eb` also retires the raw
primitive ban and the bound rule's concurrency half, and the clause governs.

Recall terms used: `python tools/memory-recall/query.py "how is the agent fan-out cap declared,
lowered and read by the hook and the harness renderer" --terms "agent-cap FANOUT_CAP print-cap slot
ledger raw parallel bounded-fanout lower-only harness concurrency settings render"`
