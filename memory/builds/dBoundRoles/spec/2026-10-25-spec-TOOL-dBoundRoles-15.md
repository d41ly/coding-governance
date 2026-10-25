# TOOL-dBoundRoles-15 — the role static block carried once per spawn, and its budget over the whole rendered block

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 7 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0180@145f826e whole
**Carries:** node:policy-key.instructions.task-charter

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-a.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-6 TOOL-dBoundRoles-14 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-26 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |

<!-- /gen:spec-records -->

## 1. Goal

A role agent's charter blocks reach it once per spawn: from its static block where the backend loads
one, from its task where none does, the choice read from `instructions.task-charter` and the harness
kind, and `always` refused where it would carry the charter twice (gap-roles-19). The static block's
budget is measured over the whole rendered block, its `## Charter` included, so a charter block that
pushes a role over its ceiling is seen (gap-roles-20).

## 2. Scope (IN)

- **S1** — One composition of the static block: `render_static_block(kit_dir, slot, role,
  memory_root, charter, notes)` in `tools/roles/roles_lib.py` returns the bytes
  `render_agent_file` (`tools/roles/render_agents.py:144-155`) writes after its front matter, the
  rendered role, then `## Charter` and `render_charter_blocks`' output when the charter yields any.
  `render_agent_file` becomes its front matter plus this call, so every agent file renders
  byte-identical. Observed by AC5.
- **S2** — The ceiling as a role field, I1's `budget`: one integer byte count per role in each
  `tools/roles/agents/<slot>.agent.md`, the key added once to `FRONT_MATTER_KEYS`
  (`tools/roles/roles_lib.py:31-32`) and described by a `budget` row of TOOL-dBoundRoles-2's
  `tools/roles/role-schema.toml`. Each role's value is priced by §4 "Pricing". Observed by AC3 and AC4.
- **S3** — R5 grades the whole block: `check_roles.py`'s R5 measures `render_static_block`'s bytes,
  CR stripped, against the role's `budget`, for every role whether `agent` is true or false, and a
  role with no `budget` is an R5 defect naming the slot. The base-body checks R5 keeps (empty body,
  a `# `/`## ` line, a stray token, a protocol file name) are unchanged. `BODY_CEILINGS`
  (`tools/roles/check_roles.py:85-89`) is deleted in the same pass. Observed by AC3 and AC4.
  **Readers:** by name: `tools/roles/check_roles.py`, the table's definition and its one reader in R5
  (lines 218-223) · by value: `tools/roles/check_roles.py`, whose R5 compares each base body's bytes
  with it, re-pointed to the role's `budget` over the whole block.
- **S4** — The census row re-pointed: where TOOL-dGroundRules-9 S1's census `tools/policy/caps.toml`
  holds the `role-body` row with home `constant:roles/check_roles.py:BODY_CEILINGS`, its home becomes
  `file:roles/role-schema.toml:budget`, the form that census admits for a value an enforcer reads
  and hands in; and every enforcer PLAY-dOrderedCharter-11 S3/S4 built to hand that cap's value in
  reads the role's `budget` through `roles_lib.read_role_budget(role)`, the one reader S3 uses too.
  Observed by AC6.
- **S5** — The single-carry check. `check_single_carry(value, kind)` in `roles_lib.py` takes the
  `instructions.task-charter` value and the harness kind of §4 "The harness kind", returns whether the
  task carries the charter blocks, and raises `RolesError` on `always` with kind `static`, naming the
  key, its value, the role and the static block that already carries the charter. Observed by AC1
  and AC2.
- **S6** — `render_handoff` (`tools/roles/handoff.py:312-427`) appends the charter blocks to the task
  (today's lines 401-407) only where S5 says so: never for an agent-true role on the direct route under
  `when-not-static`, always for an `agent: false` role or a `--stand-in` render. The value is read
  once per render through TOOL-dGroundRules-2 S7's `policy.py get instructions.task-charter`, the
  policy kit located by `roles_lib.resolve_kit_dir("policy", "policy.py", KIT_DIR)`; the catalogue row
  is the one TOOL-dGroundRules-1 S3 seeds from v2:1360, and this unit is the key's one reader.
  Observed by AC1, AC2 and AC7.
- **S7** — The kit's own text: `handoff.py`'s docstring (lines 13-16), `render_agents.py`'s docstring
  (lines 7-11) and `tools/roles/README.md`'s render and catalogue sections say where the charter
  travels and what R5 measures. Observed by AC8.

## 3. Non-goals (OUT)

- The harness route's prompts. A `Workflow` stage spawns a typed agent whose static block loads, and
  its prompt is the harness's own text, which appends no charter block today; the harness-prompt
  templates are dWellOiledMachine's (`systems.md:421`).
- The harness adapters. Which adapter a role runs on is `runtime.act-harness` and
  `roles.harness.<role>` (v2:1191, v2:1399), dWellOiledMachine's keys. This unit derives the kind
  from the spawn route and hands the adapter's property over (§4 "The harness kind").
- The `instructions.task-charter` catalogue row: TOOL-dGroundRules-1 S3 seeds every v2 `[policies]`
  row, and the default when the policy file sets no value is TOOL-dGroundRules-3 S2's.
- The budget switch `budgets.enforce` and the cap reader `budgets.py`: dGroundRules'. A role over its
  `budget` is an R5 defect, as an over-ceiling body is today.
- A repository's own role's `budget` and its widening as a ceiling rises: TOOL-dBoundRoles-20's,
  which reads the field this unit adds.
- The role section's hash and its comparison at spawn: TOOL-dBoundRoles-6's. S1 changes no byte of
  the `## Role` section `render_handoff` hashes.

### Edges

- **consumes-from** `TOOL-dBoundRoles-2` — `role-schema.toml`, the kind file this unit adds the `budget` row to; without it the field has no declaration
- **hands-off** `TOOL-dBoundRoles-20` — `budget`, the role field a repository's role declares its ceiling in, so `BODY_CEILINGS` is a role field and never a table closed in code
- **hands-off** external — dWellOiledMachine: the harness adapter's own statement of whether it loads the static block, which replaces `derive_harness_kind`'s route reading once `runtime.act-harness` names more than one adapter

## 4. Design

### The harness kind

`derive_harness_kind(keys, stand_in)` in `roles_lib.py` reads what loads the role's text at spawn:

| Route | `agent` | Kind | Why |
|---|---|---|---|
| `Agent` call with `subagent_type` the role | `true` | `static` | Claude Code loads `.claude/agents/<slot>.md`, whose body is S1's block |
| `handoff.py render --stand-in` | either | `inline` | the main loop does the work and loads no agent file |
| any render of an `agent: false` role | `false` | `inline` | no agent file is rendered for it (`render_agents.py:270-274`) |

Today only Claude Code exists as an adapter, so the route decides the kind. The hand-over is the
adapter's own flag: once dWellOiledMachine registers a second adapter, its row says whether it loads a
static block, and this function reads that row instead of the route.

### The single carry

| `instructions.task-charter` | `static` | `inline` |
|---|---|---|
| `when-not-static` (default, v2:1360) | no charter block in the task | charter blocks in the task |
| `always` | refused, `RolesError`, exit 1 | charter blocks in the task |

The refusal line: `instructions.task-charter is always, and <role> loads its static block
(.claude/agents/<role>.md carries ## Charter): the charter would reach the agent twice; set
when-not-static or render with --stand-in`. Over gov at base, 48 of 60 handoffs carried the
duplicate, median 2,880 B (PINNED, scout A's reading of `research-instruction-writing-b.md:210`).

With no policy kit found, `resolve_kit_dir` raises `LookupError` and the render prints one note,
`handoff: note — instructions.task-charter unread: no policy kit; the single carry takes
when-not-static`, and proceeds under that value (§8 F2). A `policy.py get` exit 2 refuses the render
with the reader's line.

### Pricing

Each role's `budget` is its `BODY_CEILINGS` row plus its measured charter block, the `## Charter`
heading included, with no rounding: the headroom left over the rendered role is exactly the base
body's headroom today, so the re-pricing grants no byte of growth (§8 F3). Measured over gov at `4283cb44` on 2026-10-25
(PINNED; the pass re-derives every row with `render_static_block` and prices every role present then,
including those TOOL-dBoundRoles-1 and TOOL-dWitnessedBar-23 add):

| Slot | Base ceiling | Charter block | Whole block | `budget` |
|---|---|---|---|---|
| `gov-builder` | 4096 | 3928 | 6185 | 8024 |
| `gov-diff-reviewer` | 4096 | 3710 | 5081 | 7806 |
| `gov-orienter` | 3072 | 3025 | 4857 | 6097 |
| `gov-researcher` | 3072 | 2892 | 4510 | 5964 |
| `gov-reuse-scout` | 1536 | 2488 | 3134 | 4024 |
| `gov-session` | 2048 | 2609 | 3234 | 4657 |
| `gov-skeptic` | 3072 | 2808 | 4097 | 5880 |
| `gov-spec-reviewer` | 4096 | 3411 | 5138 | 7507 |
| `gov-spec-writer` | 4096 | 4221 | 6596 | 8317 |
| `gov-synthesizer` | 3072 | 2824 | 4030 | 5896 |

`gov-session` is measured though no agent file renders for it: its block is what a stand-in render's
role section and task carry together.

### Data model

```yaml
# tools/roles/agents/gov-reuse-scout.agent.md, front matter
budget: 4024
```

```toml
# tools/roles/role-schema.toml, the row this unit adds
[[field]]
key = "budget"
type = "integer"
meaning = "the byte ceiling of the role's rendered static block, ## Charter included (R5)"
```

The row's other keys take whatever grammar TOOL-dBoundRoles-2 S-items give `role-schema.toml`.

### Inventory

Minted: `render_static_block`, `read_role_budget`, `derive_harness_kind`, `check_single_carry`; the
`budget` front-matter key; the kinds `static` and `inline`; the note and refusal lines above. Naming
cells: each function is asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
at the pass.

### Migration

Additive for the agent files, whose bytes S1 leaves unchanged. The handoffs change: a direct-route
handoff of an agent-true role carries no `### Charter rules` and no carried section in its task, so
its task-sha moves; existing handoff files are records and are not re-rendered. An adopter's role
files gain `budget` through the roles kit's render; a role file without it reds R5 by name, and the
adopter's upgrade step is TOOL-dBoundRoles-20's composition of a repository role's fields.

### Rollout

Live at landing. The `roles catalogue` leg runs R5; the policy read is armed once dGroundRules' policy
kit is installed, and the note of §4 "The single carry" names its absence on every render.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/render_agents.py`
- `tools/roles/handoff.py`
- `tools/roles/check_roles.py`
- `tools/roles/role-schema.toml`
- `tools/roles/agents/*.agent.md` (the `budget` key)
- `tools/roles/README.md`
- `tools/roles/adopt-roles.test.sh`
- `tools/policy/caps.toml` (the `role-body` row's home)
- `.claude/agents/*.md` and `.claude/roles.json`, the renders, by `render_agents.py --write`

### Alternatives rejected

- **Keep `BODY_CEILINGS` and re-price it over the whole block.** It fixes gap-roles-20 and leaves the
  ceiling a table closed in code, which TOOL-dBoundRoles-20's clause rules out and I1 already moved
  to the role field.
- **Drop the charter from the agent file and keep it in the task.** It carries once, but a harness
  stage spawns the typed agent with the harness's own prompt and would then carry no charter at all.

## 5. Production-readiness checklist

- security — no new write path; the policy value is read through the one reader and only selects
  which existing text the task carries.
- perf / scale — one `policy.py get` subprocess per render; R5 renders each role once more, ten
  roles today.
- error / empty / loading states — an absent policy kit is a note and the default; a reader exit 2
  refuses the render; a role with no `budget` is an R5 defect.
- observability — the refusal and the note each name the key and the role.
- risks — a charter grown past a role's `budget` reds R5 on every role that cites the grown rule,
  which is the intent; the pricing keeps today's headroom so no role reds at landing.
- testing — AC1 to AC8 by a pass over scratch fixtures; the suite arm in §7 is observed RED then GREEN
  by the main loop at the close.
- migration — as §4 says; landed handoff records are frozen.
- user docs — none owed: no page under `help/` describes the role static block; `tools/roles/README.md`
  is updated by S7.

## 6. Acceptance criteria

- **AC1** — When `python handoff.py render --role gov-researcher --build tFix --unit TOOL-tFix-1
  --input question=q --stdout` runs in a scratch adopter whose policy file sets
  `instructions.task-charter = "always"`, it exits 1 and its stderr names `instructions.task-charter`,
  `always` and `gov-researcher`, writing no file.
  Red when: the render writes a handoff whose task carries `### Charter rules` beside an agent file
  that carries `## Charter`.
  fixture: a scratch clone with the roles and policy kits installed and a fixture build `tFix`.
- **AC2** — When the AC1 render runs with the key unset, so `when-not-static` resolves, the task part
  holds no line `### Charter rules`, and `grep -c '^### Charter rules$'` over `gov-researcher.md`
  under `.claude/agents/` prints 1; the same render of `gov-session`, and of `gov-researcher` with
  `--stand-in` under a waiver row, holds the line once in its task.
  Red when: the check reads the value alone and drops the charter from an `inline` render too, so a
  stand-in carries no charter.
- **AC3** — When `python check_roles.py` runs in a scratch adopter whose charter gains a section 1
  rule of 1100 bytes cited by `gov-reuse-scout`'s `rules`, its base body unchanged and under 1536
  bytes, it exits 1 with an R5 line naming `gov-reuse-scout`, the block's bytes and its 4024-byte
  `budget`; with the rule removed it exits 0.
  Red when: R5 measures the base body only, so the planted charter block reads green (gap-roles-20).
  figure: the 1100 is PINNED to clear the 4024 budget over the 3134-byte block measured 2026-10-25.
- **AC4** — When `grep -c 'BODY_CEILINGS' check_roles.py` runs in `tools/roles/` it prints 0, and
  when a scratch role file loses its `budget` line, `python check_roles.py` exits 1 with an R5 line
  naming the slot and `budget`.
  Red when: a role with no field is graded against a fallback number, so a missing ceiling passes.
- **AC5** — When `python render_agents.py --check` runs over gov after the pass, it exits 0 with no
  `drift` line for any file under `.claude/agents/`, and `python -c` comparing
  `render_static_block` for `gov-builder` with the bytes after that agent file's front matter
  prints `equal`.
  Red when: the composition moves a byte, so the rendered agent files drift.
- **AC6** — When `grep -n 'role-body' caps.toml` runs in the policy kit's directory, the row's home
  is the `file:` form naming `role-schema.toml` and its `budget` key, and `git grep -n 'check_roles.py:BODY_CEILINGS'` over
  `tools/` prints nothing.
  Red when: the census row still names the deleted constant, so the census join reads a home that is
  not there.
- **AC7** — When the AC2 render runs with the policy kit removed from the scratch clone, it exits 0,
  its stderr holds the note naming `instructions.task-charter` and `when-not-static`, and its task
  carries no `### Charter rules`.
  Red when: an absent kit is read as `always`, or the render refuses where the kit is merely absent.
- **AC8** — When `grep -n 'instructions.task-charter' README.md handoff.py` runs in `tools/roles/`,
  each file names the key and the `static` and `inline` kinds.
  Red when: the docstring still says the charter blocks are the task's last block on every render.

## 7. Gates

The pass adds no leg: the `roles catalogue` leg runs R5, and the roles adopter suite runs the renders.

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 AC3 AC7 · a fixture policy file setting `always` under an agent-true render, and a planted 1100-byte cited rule under `gov-reuse-scout` · none

## 8. Open questions

- **F1 — Where does the ceiling live once it covers the whole block?** Options: (a) I1's role field
  `budget`, priced per §4; (b) `BODY_CEILINGS` kept and re-priced; (c) a `budgets.*` key per role in
  the policy file. (b) leaves a closed table, which cl-dClosedLoop-0185 forbids; (c) puts a kit's
  structural ceiling in the owner's policy file, where dGroundRules-9 states a family cap's value may
  not be set. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, v2's clause cl-dClosedLoop-0185
  ("`BODY_CEILINGS` a role field") and the brief's I1. widens: none · relaxes: none
- **F2 — What does the single carry do when no policy kit is installed?** Options: (a) a note and
  `when-not-static`, the catalogue's default at v2:1360; (b) refuse every render; (c) carry the charter
  in every task. (b) breaks every adopter without dGroundRules' kit; (c) is the double carry the clause
  closes. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich survivor, and the
  precedent PLAY-dOrderedCharter-11 S4 sets for an absent sibling kit (`unarmed` named, the render
  proceeding). widens: none · relaxes: none
- **F3 — Is the re-pricing a raise, which `layer-roles.md:384-386` gives the owner alone ("the
  block's growth raises a ceiling only by an owner-approved change to it")?** Options: (a) each
  `budget` the base ceiling plus the measured charter block, exact, so the slack over the rendered role
  is today's to the byte; (b) the same rounded up to 1024, adding up to 1023 bytes of slack per role;
  (c) owner-set values, parking the unit. (b) grants growth nobody approved; (c) parks a unit whose
  values a rule derives. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the only option that
  moves the measure and not the allowance, so no block may grow by a byte it could not grow by
  before. widens: none · relaxes: none
- **F4 — The parents this unit calls are specced and not built at base `4ed9e567`.** TOOL-dBoundRoles-2's
  `role-schema.toml`, TOOL-dGroundRules-2 S7's `policy.py get`, TOOL-dGroundRules-9 S1's census and
  PLAY-dOrderedCharter-11 S3/S4's role-block enforcer do not exist in the tree. RESOLVED (agent,
  2026-10-25, delegated): the build run re-grounds on each at the pass, re-derives S3's reader list
  with `git grep -n BODY_CEILINGS` over the tree, and stops the unit if a called section is still
  absent then, rung 1 (the brief's rule for DEFERRED parents). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 15, the brief's I1, I7 and I8, scout
  A's row for cl-0180, and the source at `4283cb44`.

## 10. Reuse audit

The seams extended: `render_agent_file` (`tools/roles/render_agents.py:144-155`), whose body becomes
the one composition; `render_handoff`'s charter append (`tools/roles/handoff.py:396-407`), the single
carry's switch point; R5 (`tools/roles/check_roles.py:218-223`), the one grader I7 names;
`render_charter_blocks` (`tools/roles/roles_lib.py:284-303`), unchanged and still the one charter
composition; `resolve_kit_dir` (`tools/roles/roles_lib.py:97`) for the policy kit. `python
tools/codebase-map/reuse_lookup.py "carry the charter once per agent spawn and budget the rendered
static block"` ranked `parse_charter`, `resolve_charter_path` and `render_charter_blocks` in the
roles kit first, each matching source; it did not surface `render_agent_file` or `render_handoff`,
read here from source, and it named no policy reader, which is right, since `tools/policy/` is absent
at base. The recall probe returned scout A's row, the brief's row and `layer-roles.md:348`, whose
rule that a ceiling rises only by an owner-approved change is what §8 F3 answers. Scout A's line numbers (read at `748b309f`) match source at `4283cb44`, no file under
`tools/` having changed between them.

Recall terms used: `python tools/memory-recall/query.py "how does a role agent receive the charter
blocks and what does the role body ceiling measure" --terms "render_charter_blocks render_agent_file
BODY_CEILINGS R5 static block charter carry handoff task-charter budget"`
