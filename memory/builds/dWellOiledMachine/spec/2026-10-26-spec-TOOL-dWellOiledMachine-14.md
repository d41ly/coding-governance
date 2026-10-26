# TOOL-dWellOiledMachine-14 — harness adapters with capability tables, measured and never claimed, and their install targets

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 7 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0292@7eaaf1a6 whole
**Carries:** node:point.harness-adapters
**Carries:** node:policy-key.runtime.harnesses

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-48 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

gov runs through harness adapters (v2 P36), and today nothing describes one: no table separates what a
harness can do from what an adapter claims, the Codex row went stale within days (gap-rt-31,
gap-register:296), and eight descriptor rows write Claude Code's `.claude/` paths with no adapter
declaring them (gap-rt-19, gap-register:284). This unit registers each harness adapter at
`point.harness-adapters` with a capability table of measured rows and its install targets, reads
`runtime.harnesses` through them, and moves the hard-coded Skill destinations onto the adapter.

## 2. Scope (IN)

- **S1** — The capability table (I7): `tools/runtime/harnesses/claude-code.toml`, which
  TOOL-dWellOiledMachine-1's spike creates with its measured rows, and `tools/runtime/harnesses/codex.toml`,
  each a list of `[[capability]]` rows `name`, `value`,
  `measured-on` (a UTC date), `binary-version` (two to four dotted integers). A row whose `value` is
  the string `unmeasured` carries neither date nor version and reads as absent. One name may carry one
  row per binary version. The names are a closed list, `CAPABILITY_NAMES` in
  `tools/runtime/harness.py`: `prompt-submit`, `subagent-stop`, `permission-request`,
  `preset-session-id`, `headless-fork`, `schema-return`, `live-inbox`, `hook-hold-seconds`, `browser`,
  `credential-read` (I7); the spike's `subagent-start`, `subagent-stop-owner-stopped`,
  `subagent-stop-stalled`, `subagent-stop-killed`, `return-byte-match`, `hook-hold-timeout` and
  `single-agent-backend` (TOOL-dWellOiledMachine-1 S5); and `on-failure`, which
  TOOL-dWellOiledMachine-10 reads. A unit that measures a new capability adds its name there in its
  own unit. The table is kept apart from `workflows.toml`'s
  `harness` field, which names a role-harness script (`tools/roles/workflows.toml:7`). Observed by AC1.
- **S2** — The seed: the claude-code table keeps every row the spike measured, unchanged, and every
  other name in either table is written `unmeasured` until TOOL-dWellOiledMachine-36's fixture
  measures it. Nothing is claimed from documentation or help text: Codex's twelve documented hook
  events and Claude Code's help-listed `--session-id` stay `unmeasured` (research-harness-cli section
  5 marks the latter "(help)", not tested). Observed by AC1.
- **S3** — The reader: `read_capability(adapter, name, version=None)` returns the row for that binary
  version, else the row of the newest measured version, else None for `unmeasured` or absent;
  `check_capability_rows(path)` refuses an unknown name, a measured row missing `measured-on` or
  `binary-version`, a malformed date or version, and two rows for one name and version. CLI: `python
  harness.py capability <adapter> <name> [--version <v>]` prints `<value> · <binary-version> ·
  <measured-on>`, or `unmeasured` with exit 1; `python harness.py --check` runs the row check over
  every table. Observed by AC1 and AC2.
- **S4** — The registration (I4, `point.harness-adapters`): the `[[point]]` row `point.harness-adapters`
  in `tools/runtime/points.toml`, `purpose` "how a harness loads instructions, spawns, hooks and
  compacts, with its capability table and its install targets" (layer-runtime `[extend]`), `contract`
  this spec's S1 and S5; and one `[[adapter]]` row per harness, `name` `claude-code` and `codex`, each
  with `table` naming its capability file, `grant = { service = "local", scopes = [], secret =
  "anonymous" }` graded by TOOL-dWellOiledMachine-17's `check_adapter_grant`, and `tenancy`,
  `retention` and `region` as I4 spells them. Observed by AC3.
- **S5** — The install targets: each adapter file carries `[install]` with `skill`, `agent` and
  `settings`, the three kinds a descriptor row lands today. claude-code declares `.claude/skills`,
  `.claude/agents` and `.claude/settings.json`; codex declares none, its targets being dShippedRelease's
  (research-harness-cli section 6). `resolve_install_target(kind, harnesses)` returns the one target the
  named harnesses declare for that kind, and refuses, naming the kind and the harnesses, when none or
  more than one declares it. Observed by AC4 and AC5.
- **S6** — `runtime.harnesses` (`policy-key.runtime.harnesses`, catalogue
  `tools/policy/catalogue.toml:505-509`, a non-empty set, default `["claude-code"]`) read through
  `policy.py get runtime.harnesses` run in the target (I31), and every name it holds resolved against
  the S4 rows: an unregistered name is refused, never skipped. Observed by AC5.
- **S7** — The Skill destinations read through the adapter. govkit's `target_context`
  (`tools/govkit/govkit.py:1436`) seeds the token `{skill_home}` from S5 over S6's value and adds it to
  `SEEDED_TOKENS` (`:1397`), so a target cannot supply it. The five `rendered` Skill rows spell their
  destination with it: `tools/branch-reconcile/kit.toml:32`, `tools/drift-audit/kit.toml:54`,
  `tools/lexicon/kit.toml:74`, `tools/memory-recall/kit.toml:63` and `tools/roles/kit.toml:57`, and so
  does every `probe` and `lf_pin` `pattern` in those five descriptors naming the same file, each already
  resolved through `resolve_tokens` (`:1233`, `classify_outcome` :6557, `lf_pins` :5886). Each kit's
  adopter reads its destination from `GOV_SKILL_HOME`, which govkit exports from `{skill_home}` when it
  runs `[adopt]`, and defaults to `.claude/skills` when run by hand: `adopt-branch-reconcile.sh:45`,
  `adopt-drift-audit.sh:66`, `adopt-lexicon.sh:126`, `adopt-memory-recall.sh:118`, `adopt-roles.sh:129`.
  Observed by AC4, AC6 and AC7.
- **S8** — The one-fact check, `python harness.py --check-targets`: no `to`, `probe` or `pattern` value
  in any kit descriptor begins with `.claude/skills`; every other `.claude/` destination a descriptor
  or an adopter still spells as a literal — the settings row `tools/govkit/entries/settings-merge.kit.toml:19`,
  the generated rows `tools/roles/kit.toml:126,131` and `tools/policy/kit.toml:62`, and the five
  adopters' hand-run defaults — equals or sits under a target claude-code's `[install]` declares. A
  literal outside every declared target is refused, naming its file and line. Observed by AC6.
- **S9** — `help/runtime.md` gains a section on harness adapters: the capability table, what
  `unmeasured` means, `runtime.harnesses` and the install targets. Observed by AC8.

## 3. Non-goals (OUT)

- Measuring a row: TOOL-dWellOiledMachine-36's conformance fixture measures and rewrites rows, and
  TOOL-dWellOiledMachine-1's spike records `hook-hold-seconds`. This unit measures nothing; it writes
  `unmeasured` for every name no measurement has filled.
- Codex's install targets (`.codex/hooks.json`, `.codex/config.toml`) and its hook-trust step:
  dShippedRelease's (research-harness-cli section 6). Codex registers here with a capability table
  and no install target.
- Re-pointing the settings merge and the agent render: `settings-merge.py` and `render_agents.py`
  merge Claude Code's own formats, so their destinations stay literals S8 holds equal to the declared
  targets; a second harness's settings target is the unit that wires that harness.
- The dispatcher's per-harness wiring: TOOL-dWellOiledMachine-10.
- `runtime.act-harness`, `runtime.binary` and `runtime.owner-harness`: TOOL-dWellOiledMachine-56 and
  TOOL-dWellOiledMachine-36 own them and read these rows.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-20` — `points.toml`, where S4 adds the `point.harness-adapters` row and the two adapter rows
- **consumes-from** `TOOL-dWellOiledMachine-17` — `check_adapter_grant`, which grades each harness adapter's `[[adapter]]` row
- **consumes-from** `TOOL-dWellOiledMachine-1` — `hook-hold-seconds` and the spike's other rows, already in `claude-code.toml`, which S2 keeps
- **hands-off** `TOOL-dWellOiledMachine-36` — `[[capability]]`, the rows the conformance fixture measures and writes
- **hands-off** `TOOL-dWellOiledMachine-10` — `[[capability]]`, whose `on-failure` row the dispatcher's session line reads
- **hands-off** `TOOL-dWellOiledMachine-5` — `[[capability]]`, whose `prompt-submit` row decides the fallback's drain per harness
- **hands-off** `TOOL-dWellOiledMachine-29` — `[[capability]]`, where the measured `browser` row lands
- **hands-off** `TOOL-dWellOiledMachine-23` — `[[capability]]`, where the measured hook-channel cap lands
- **hands-off** `TOOL-dWellOiledMachine-12` — `[[capability]]`, where the card's measured re-attachment cap lands
- **hands-off** `TOOL-dWellOiledMachine-32` — `[[capability]]`, whose `preset-session-id` row decides a preset or returned session id
- **hands-off** `TOOL-dWellOiledMachine-35` — `[[capability]]`, whose `live-inbox` row admits live delivery
- **hands-off** `TOOL-dWellOiledMachine-37` — `[[capability]]`, read through `read_capability`, where the trusted-hook store's row lands
- **hands-off** `TOOL-dWellOiledMachine-56` — `[[capability]]`, read through `read_capability`, holding each adapter's `credential-read` row

- **hands-off** `TOOL-dWellOiledMachine-25` — `[[capability]]`, read through `read_capability`, whose spike rows S4 decides the host from
- **hands-off** `TOOL-dWellOiledMachine-43` — `[[capability]]`, the four rows read through `read_capability`
## 4. Design

### Evidence

- No capability table exists: `git grep -i capabilit -- tools skills` finds only branch-reconcile's and
  the lexicon's unrelated senses (scout B row 6, rerun 2026-10-26).
- Six descriptor `to` rows name `.claude/`: the five Skill rows of S7 and the settings row; three
  `[[generated]]` rows name `.claude/agents`, `.claude/roles.json` and `.claude/settings.json`
  (`git grep -n '\.claude/' -- '*kit.toml'`, 2026-10-26). gap-rt-19 counted eight at the baseline.
- `resolve_dests` already lands a list-valued `to` and resolves every token through
  `resolve_tokens`, and an unresolved token is a refusal, not a path (`govkit.py:6617-6641`).
- The five adopters hard-code their Skill path at the lines S7 cites.

### The table

```toml
# tools/runtime/harnesses/claude-code.toml
[install]
skill = ".claude/skills"
agent = ".claude/agents"
settings = ".claude/settings.json"

[[capability]]
name = "permission-request"
value = "yes"
measured-on = "2026-10-14"
binary-version = "2.1.292"
```

### The seed

| Adapter | Rows at this unit's landing | Measured by |
|---|---|---|
| claude-code | the spike's S5 rows, as it wrote them | TOOL-dWellOiledMachine-1, `spike.py --live --write` |
| claude-code | every other name, `unmeasured` | — |
| codex | every name, `unmeasured` | — (gap-rt-31: documentation is a claim) |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_capability` | function, `tools/runtime/harness.py` | `py.function`, `read`, OK |
| `check_capability_rows` | function, `harness.py` | `py.function`, `check`, OK |
| `resolve_install_target` | function, `harness.py` | `py.function`, `resolve`, OK |
| `check_install_targets` | function, `harness.py`, the `--check-targets` flag | `py.function`, `check`, OK |
| `CAPABILITY_NAMES` | constant, `harness.py` | none |
| `skill_home` | govkit seeded token | none |
| `GOV_SKILL_HOME` | environment variable govkit exports to an adopter | none |

### Migration

None for an adopter: under the default `runtime.harnesses` the token resolves to `.claude/skills`,
the path every receipt already records, so `update` writes the same bytes to the same place.

### Files touched (estimate)

- `tools/runtime/harness.py` — S1, S3, S5, S8 (new)
- `tools/runtime/harnesses/claude-code.toml` — S2's `unmeasured` rows, S5's `[install]` (created by
  TOOL-dWellOiledMachine-1)
- `tools/runtime/harnesses/codex.toml` — S1, S2, S5 (new)
- `tools/runtime/points.toml` — S4
- `tools/runtime/selftest.py` — the arm in §7
- `tools/govkit/govkit.py` — S7, `target_context` and `SEEDED_TOKENS`
- `tools/govkit/selftest.py` — the arm in §7
- `tools/branch-reconcile/kit.toml`, `tools/branch-reconcile/adopt-branch-reconcile.sh` — S7
- `tools/drift-audit/kit.toml`, `tools/drift-audit/adopt-drift-audit.sh` — S7
- `tools/lexicon/kit.toml`, `tools/lexicon/adopt-lexicon.sh` — S7
- `tools/memory-recall/kit.toml`, `tools/memory-recall/adopt-memory-recall.sh` — S7
- `tools/roles/kit.toml`, `tools/roles/adopt-roles.sh` — S7
- `help/runtime.md` — S9

### Alternatives rejected

- **A capability field on the role or workflow rows.** `workflows.toml`'s `harness` names a script, and
  a capability belongs to a harness binary, so the two would be one word with two meanings.
- **Copying Codex's documented events in as rows.** That is a claim, the defect gap-rt-31 records.
- **Expanding a Skill row once per harness.** Only claude-code declares a Skill target in this build;
  S5 refuses an ambiguous kind rather than writing a second copy nobody reads.

## 5. Production-readiness checklist

- security — the tables hold no credential; the adapter rows declare `anonymous`; `GOV_SKILL_HOME` is
  a path govkit derives, and a target cannot supply `{skill_home}` (S7).
- perf / scale — two small TOML reads per govkit apply; one `policy.py get` per target.
- error / empty / loading states — `unmeasured` reads absent; an unknown name, an unregistered harness
  and an undeclared install kind each refuse by name.
- observability — `harness.py capability` prints value, version and date together.
- risks — a table this thin answers `unmeasured` for most names until unit 36's fixture runs, so a
  reader that needs a row refuses rather than guesses; that is the intent.
- testing — the arms in §7.
- migration — none, §4.
- user docs — `help/runtime.md`, S9.

## 6. Acceptance criteria

- **AC1** — When `python harness.py --check` runs over the two shipped tables it exits 0; over a
  fixture table holding a row named `teleport`, a measured row with no `binary-version`, and two
  `permission-request` rows for one version, it prints three refusals and exits 1.
  Red when: a measured row with no version passes.
- **AC2** — When `python harness.py capability claude-code permission-request` runs it prints the
  value the spike measured with its binary version and date; `python harness.py capability codex
  preset-session-id` prints `unmeasured` and exits 1.
  Red when: an `unmeasured` row prints `yes` or `no`.
- **AC3** — When `grep -c 'point = "point.harness-adapters"'` runs over the runtime kit's
  `points.toml` it prints `2`, the file holds the `[[point]]` row `name = "point.harness-adapters"`, and
  `python grants.py --check` over it exits 0.
  Red when: a harness adapter row carries no `grant`.
- **AC4** — When govkit's `plan` runs the lexicon entry into a fixture target whose
  `.governance/policy.toml` sets no `runtime.harnesses`, the Skill lands at
  `.claude/skills/lexicon/SKILL.md`; with `GOV_HARNESS_TABLES` pointing at a fixture claude-code table
  whose `skill` reads `.agents/skills`, it lands under that directory, its outcome probe and `lf_pin`
  following.
  Red when: the destination stays `.claude/skills` under the fixture table.
- **AC5** — When the fixture target's policy sets `runtime.harnesses = ["codex"]`, `plan` refuses the
  lexicon Skill row naming kind `skill` and harness `codex`; with `["claude-code", "gemini"]`, it
  refuses naming `gemini` as unregistered.
  Red when: either lands a file.
- **AC6** — When `python harness.py --check-targets` runs on the tree it exits 0; with
  a fixture descriptor's `to` planted as a literal under `.claude/skills` it refuses that row, and with
  `tools/policy/kit.toml`'s generated path planted outside every declared target it refuses that
  literal.
  Red when: either plant passes.
- **AC7** — When `bash tools/lexicon/adopt-lexicon.sh --scaffold` runs in a fixture repository with
  `GOV_SKILL_HOME=.agents/skills`, the Skill is rendered under that directory and nothing is written
  under `.claude/`.
  Red when: the adopter writes `.claude/skills/lexicon/SKILL.md`.
- **AC8** — When `grep -n "runtime.harnesses"` runs over the runtime kit's help page, `runtime.md`, it
  finds S9's section.
  Red when: the page does not name the key.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `lexicon selftest` · `codebase-map kit selftest` · `drift-audit selftest` · `branch-reconcile selftest` · `memory-recall kit selftest` · `roles adopter self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runtime/selftest.py · covers AC1 AC2 AC3 AC6 · the malformed table rows and the planted `.claude/` literals, staged against `check_capability_rows` and `check_install_targets` stubbed to return no refusal · none
New arm: tools/govkit/selftest.py · covers AC4 AC5 · a fixture target under the default, a fixture table, a codex-only and an unregistered harness set, staged against a `target_context` that seeds `.claude/skills` as a literal · none

## 8. Open questions

- **F1 — Which install kinds does an adapter declare in this build?** Layer-runtime `[extend]` names
  five: Skill, agent, rule, hook and settings fragment. Only three are landed by a descriptor today,
  and a declared kind no row reads is a claim nobody checks. Recommendation: the three a descriptor
  lands, each later kind added with its first reader. RESOLVED (agent, 2026-10-26, delegated): the
  three, rung 3; a kind with no reader fails the repository's YAGNI rule and widens nothing.
- **F2 — Do the settings and agent destinations move onto a token too?** Their writers,
  `settings-merge.py` and `render_agents.py`, emit Claude Code's own formats, so a token there would
  name a path for a format no other harness reads. Recommendation: keep them literals held equal to
  the declared targets by S8's check, the charter's one-fact rule's second form. RESOLVED (agent,
  2026-10-26, delegated): S8's check, rung 3; it closes the drift both ways without a writer change.

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended are govkit's token resolution, `target_context` and `resolve_tokens`
(`tools/govkit/govkit.py:1233,1436`), for the install targets, and the point registry I4 for the
adapter rows. `python tools/codebase-map/reuse_lookup.py "a harness capability table read before a
launch"` returned only name-stem matches (`read`, `read_text`, `read_conf`, `read_descriptors`); no
existing seam fits the capability table, the evidence being scout B row 6's empty `git grep -i
capabilit` and the probe's shortlist. Where scout B's row and source disagree: it lists four descriptor
rows; source holds six `to` rows and three `[[generated]]` rows, and §4 cites all nine.

Recall terms used: `python tools/memory-recall/query.py "which harness capabilities are measured and
where are install targets declared" --terms "harness adapter capability table measured claimed install
targets claude-code codex PermissionRequest onFailure runtime.harnesses"`
