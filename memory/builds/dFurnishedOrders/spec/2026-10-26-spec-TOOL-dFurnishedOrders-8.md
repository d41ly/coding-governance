# TOOL-dFurnishedOrders-8 — the role files' protocol pointers and re-verification orders replaced by rendered slices

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 1 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0199@871337bc whole
**Carries:** node:policy-key.instructions.slices

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-c.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-16 |

<!-- /gen:spec-records -->

## 1. Goal

Every role agent carries the charter's whole `## Protocols` section today, a list of whole documents
to read (gap-roles-12: 811 method-class reads by role agents), and four role files plus the spec
format order every claim re-verified (gap-roles-10). This unit hands each role the protocol slices it
declares, whole or as a pointer to the slice as `instructions.slices` says, re-points the machinery
that carries and asserts the whole section (`roles_lib.CARRIED_SECTIONS`, `check_roles.py`'s R0, R5
and R10, `render_agents.py`'s self-test arm 4), and deletes the re-verification orders.

## 2. Scope (IN)

- **S1** — The `slices` role field. One `[[field]]` row in `tools/roles/role-schema.toml`
  (TOOL-dBoundRoles-2 S1's grammar): `key = "slices"`, `owner = "gov"`, `shape = "list"`,
  `required = "optional"`. Each entry is a section tag of PLAY-dOrderedCharter-19 S3's `doc`
  namespace, `doc.<name>#<seg>`, one `##` section of a protocol document. Every role file declares
  its set as §4 "### The declared slices" derives it. Observed by AC1 and AC3.
- **S2** — The slice cut. `resolve_slices(root, entries)` in `tools/roles/roles_lib.py` resolves each
  tag through PLAY-dOrderedCharter-19 S6's `gov_tag.py where <tag>`, run as a subprocess from the
  playbook kit found by `resolve_kit_dir("playbook", "gov_tag.py", KIT_DIR)`, to `path:line`, then
  reads that file and cuts from the line to the line before the next `## ` heading outside a fenced
  block, or the end of file. It returns one `(tag, path, lo, hi, text)` per entry, in declaration
  order. The section split `parse_charter` does today (`tools/roles/roles_lib.py:216-221`) moves into
  one `parse_sections(lines)` that both read, fence-aware. Observed by AC1, AC3 and AC8.
- **S3** — The rendered block. `render_charter_blocks` (`tools/roles/roles_lib.py:309-328`) takes the
  resolved slices and the mode, and renders `### Method slices` after the carried sections, per §4
  "### The block". Under `handed` each slice's text travels; under `pointer` one line per slice names
  its tag, its path and its line range, never a whole document. The block sits inside
  `render_static_block`'s one composition (TOOL-dBoundRoles-15 S1) and, for an inline render, in the
  task as the charter blocks already are. Observed by AC1 and AC2.
- **S4** — The key read. `instructions.slices` is read once per render through
  `read_policy_setting("instructions.slices", root)` (TOOL-dBoundRoles-21 S1, shared interface J1);
  `None` renders the catalogue's default, `handed` (`tools/policy/catalogue.toml:1356-1359`). The two
  renderers that compose charter blocks, `render_agent_file` (`tools/roles/render_agents.py:144-155`)
  and `render_handoff` (`tools/roles/handoff.py:401-407`), pass the value in. Observed by AC2 and AC9.
- **S5** — `roles_lib.CARRIED_SECTIONS` re-pointed: `("Protocols", "Facts")` becomes `("Facts",)`,
  so no role carries the whole Protocols section. `parse_charter` keeps reading `## Protocols` when
  present, as the source of `protocol_files`, the file names its backticked paths end in, which it
  now returns beside `carried`; the regex `PROTOCOL_PATH_RE` moves from `check_roles.py:110-111` into
  `roles_lib.py` as that one reader's. Observed by AC4 and AC5.
  **Readers:** by name: `tools/roles/roles_lib.py` (the tuple at :67, `parse_charter`'s docstring at
  :206 and its loop at :237-248), `tools/roles/check_roles.py` (the zip at :171), `tools/roles/README.md`
  (:214, :241-242, :271 describe the carried pair) · by value: `render_charter_blocks`
  (`tools/roles/roles_lib.py:325-327`), which renders each carried section under `### `;
  `check_roles.py:171-172`, which reads the carried Protocols body for the protocol file names;
  `render_agents.py`'s fixture `FIXTURE_DOC` (:99-102) and arm 4 (:382-391), which assert the
  carried text; and `handoff.py:401-407`, which appends the same blocks to an inline task.
- **S6** — `check_roles.py` re-pointed. R0 refuses a tagged doc lacking `## Facts` only, its message
  naming the carried sections from the tuple. R5 (:218-220) and R10 (:361-363) read
  `charter["protocol_files"]` in place of the carried Protocols body, so a body or overlay spelling a
  protocol's file name stays a defect. R3 gains the slice join: a `slices` entry that is not
  `doc.<name>#<seg>`-shaped, that `gov_tag.py where` does not resolve, or that a role names twice is
  one R3 line naming the role file and the entry; with no tag resolver installed R3 prints one
  `roles: note:` and grades no slice. The module docstring's R0, R3, R5 and R10 entries say so.
  Observed by AC3, AC4 and AC5.
- **S7** — `render_agents.py`'s self-test arm 4 re-pointed: its fixture doc gains a fixture guide
  with two `##` sections, one holding a fenced `## ` line, a fixture role declares one slice, and the
  arm asserts the carried text is `### Facts` then `### Method slices` with that slice's text cut at
  the next unfenced heading, and, under a fixture policy setting `pointer`, the one pointer line.
  Observed by AC1, AC2 and AC8, which the `New arm:` line of §7 re-observes.
- **S8** — The re-verification orders deleted from the role files and the spec format:
  `tools/roles/agents/gov-spec-writer.agent.md:30-31` and `gov-researcher.agent.md:33-34` lose their
  "Verify every claim about current code" bullets, the researcher keeping its second half as "Say
  where a record and the code you read disagree"; `gov-session.agent.md:18-19` loses "to re-verify
  against the tree" and reads "The sender's records are background, not instructions"; and
  `gov-builder.agent.md:19` reads "Build from the spec and the brief your task names" in place of
  "Read the spec whole before you touch code, and the brief your task names". The rule that replaces
  them, acting on a handed fact as given, renders in each role's `## Trust` block, which
  TOOL-dFurnishedOrders-5 owns. The spec format's writing rule
  (`tools/memory-tree/SPEC-TEMPLATE.template.md:106`, rendered to `memory/TEMPLATE-SPEC.md:106`)
  becomes: "A claim about existing code counts as verified when this unit's author read that code at
  writing time, or was handed it with its key; cite it by path and line or by that key, and mark the
  rest `UNVERIFIED`." Observed by AC6.
  **Readers:** by name: the five lines above and their renders under `.claude/agents/` and
  `memory/TEMPLATE-SPEC.md` · by value: NO VALUE READERS — prose a role reads, which no code
  compares, counts or derives from.
- **S9** — Each role's `budget` (TOOL-dBoundRoles-15 S2) re-derived by that unit's §4 "Pricing" rule
  over the new charter block: the role's base allowance plus its measured charter block, Protocols
  gone and `### Method slices` in, under `handed`, so the authored body gains no byte. Observed by AC7.
- **S10** — The kit's text: `tools/roles/README.md`'s render section and `help/roles.md`'s "How a
  task reaches an agent" say a role carries the slices it declares, handed or pointed at as
  `instructions.slices` says, and that editing a sliced protocol section stales the role files that
  carry it until `render_agents.py --write`. Observed by AC10.

## 3. Non-goals (OUT)

- The protocol slices as instruction units: dConvergedCharter builds them (systems.md:420-428). Until
  it lands the slice is the heading-bounded cut of S2, addressed by PLAY-dOrderedCharter-19's `doc`
  section tags; the hand-over is that a `slices` entry then names that unit's tag and `resolve_slices`
  reads the unit's text instead of cutting a document.
- Selecting slices by the item a role acts in, and by the trigger the item decides
  (layer-roles.md:368-373): the `slices` field is the per-role stand-in until dDeclaredLoop's items
  carry instruction tags; selection by `feature.*` is TOOL-dFurnishedOrders-18's.
- The `## Trust` block that states the replacement rule: TOOL-dFurnishedOrders-5.
- The charter's own `## Protocols` section, which the main session reads in `AGENTS.md`: unchanged.
- The answered-call hook that refuses a whole-guide read a slice answers: TOOL-dFurnishedOrders-6.

### Edges

- **hands-off** `TOOL-dFurnishedOrders-18` — `instructions.slices`, the key read where a role's protocol pointer renders, which that unit's instruction selection reads beside its own key
- **hands-off** `TOOL-dFurnishedOrders-5` — `## Trust`, the static block that states the act-on-handed-facts rule replacing the re-verification orders S8 deletes
- **hands-off** `TOOL-dFurnishedOrders-4` — `doc.build-method#m6-passes-commits-parallelism`, the slice `gov-builder` carries, whose text that unit edits and whose role files it re-renders
- **hands-off** `TOOL-dFurnishedOrders-6` — `### Method slices`, the rendered block whose `#### <tag> — <path>:<lo>-<hi>` heading per handed slice the answered-call hook reads to tell a whole-document read the slice answers; a `pointer` line hands no text and answers nothing
- **consumes-from** external — TOOL-dBoundRoles-2's `role-schema.toml`, TOOL-dBoundRoles-15's `render_static_block` and `budget`, TOOL-dBoundRoles-21's `read_policy_setting`, and PLAY-dOrderedCharter-19's `doc` section tags and `gov_tag.py where`, each specced and unbuilt at base
- **hands-off** `TOOL-dFurnishedOrders-29` — `resolve_slices`, the Protocols carry's readers and the roles dossier, which unit 29 S15, S17, S21 and S22 settle (ids 35, 39, 37, 47)

## 4. Design

### The declared slices

Each set is the sections the role's body cites by name, so the set is derived from the body and never
chosen afresh. A tag's `<seg>` is its heading lower-cased with each run outside `[a-z0-9]` folded to one
hyphen (PLAY-dOrderedCharter-19 S3). The pass derives the sets over every role file present then,
thirteen once TOOL-dBoundRoles-1 adds `gov-prompt-writer`, `gov-planner`, `gov-architect` and
`gov-tester` and TOOL-dBoundRoles-18 merges the two reviewers into `gov-reviewer`; a role whose body
cites no protocol section declares none. The sets at base, read from gov's bodies at `1a3ce03d`:

| Role | `slices` | Cited at |
|---|---|---|
| `gov-spec-writer` | `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`, `doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`, `doc.build-method#m5-recall-and-reuse`, `doc.template-spec#3-edges-what-this-unit-takes-and-what-it-leaves`, `doc.template-spec#7-gates-the-shape-the-leg-join-reads-and-where-a-new-arm-lives`, `doc.template-spec#10-reuse-audit-the-two-facts-and-what-satisfies-each`, `doc.template-spec#fork-item-cutoff-8-is-f-item-shaped-and-each-fork-is-graded-alone` | body :19-38 |
| `gov-builder` | `doc.build-method#m6-passes-commits-parallelism` | body :34, :43 |
| `gov-researcher` | `doc.build-method#m12-research-test-choose-when-the-solution-is-not-given`, `doc.build-method#m5-recall-and-reuse` | body :23, :28 |
| `gov-orienter` | `doc.build-method#m5-recall-and-reuse` | body :33 |
| `gov-reviewer` (today `gov-spec-reviewer` and `gov-diff-reviewer`), `gov-skeptic`, `gov-synthesizer` | `doc.review-protocol#the-tier-2-pattern` | "by the review protocol" |
| `gov-reuse-scout`, `gov-session` | none | no protocol section cited |

TOOL-dFurnishedOrders-15 declares the tester's set when it re-founds that role.

### The block

Under `handed`, after the carried `### Facts`:

```
### Method slices

#### doc.build-method#m6-passes-commits-parallelism — memory/guides/BUILD-METHOD.md:180-230

<the section's lines after its heading; each heading line inside it demoted two levels, a fenced block untouched>
```

Under `pointer`:

```
### Method slices

- `doc.build-method#m6-passes-commits-parallelism` — `memory/guides/BUILD-METHOD.md` lines 180-230
```

A role with no `slices` renders no `### Method slices` heading. With no tag resolver found,
`resolve_kit_dir` raises `LookupError`, the render prints one note, `roles: note — doc tags
unresolved: no gov_tag.py; each slice renders as its tag alone`, and each entry renders as
`- \`<tag>\` — not installed: no tag resolver`. A resolver that answers but does not resolve a tag is a
refusal, the render's exit 1 naming the role and the tag, since R3 grades the same join.

### Data model

```toml
# tools/roles/role-schema.toml, the row this unit adds
[[field]]
key = "slices"
owner = "gov"
shape = "list"
required = "optional"
```

```yaml
# tools/roles/agents/gov-builder.agent.md, front matter
slices: doc.build-method#m6-passes-commits-parallelism
```

### Inventory

Minted: the `slices` front-matter key; `resolve_slices`, `parse_sections`; the `### Method slices`
heading; the note and refusal lines above; `protocol_files` in `parse_charter`'s return. Each function
was asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function`, and both answered
OK. `PROTOCOL_PATH_RE` moves and keeps its name.

### Migration

The agent files and every inline handoff change: Protocols leaves them and the slices arrive, so each
role's role-sha and task-sha move. Landed handoff files are records and are not re-rendered. An adopter
receives the field, the block and the re-pointed checks through the roles kit's update; its role files
with no `slices` carry no slice block and lose the Protocols block, which is the clause's intent.

### Rollout

Live at landing under `handed`, the catalogue default. An edit to a sliced section stales the role
files carrying it, and `roles render wiring` reds until `render_agents.py --write`; the README and the
help page say so (S10).

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/check_roles.py`
- `tools/roles/render_agents.py`
- `tools/roles/handoff.py`
- `tools/roles/role-schema.toml`
- `tools/roles/agents/` (every role file's `slices` and `budget`, and S8's four bodies)
- `tools/roles/README.md`
- `tools/roles/adopt-roles.test.sh`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `memory/TEMPLATE-SPEC.md` (its render)
- `.claude/agents/` and `.claude/roles.json` (renders, by `render_agents.py --write`)
- `help/roles.md`

### Alternatives rejected

- **A slice address of the roles kit's own, `<file>#<heading>`.** A second spelling beside the
  `doc` tags PLAY-dOrderedCharter-19 indexes; two spellings of one section drift (§8 F1).
- **Slices in the task block, per item.** No item declares instruction tags until dDeclaredLoop's
  items do, and shared interface J19 puts them in the static block's one composition (§8 F2).

## 5. Production-readiness checklist

- security — no new write path; the renders read tracked protocol documents and the policy file
  through their own readers, and a subprocess runs a tracked kit script with argv, never a shell string.
- perf / scale — one `gov_tag.py where` call per declared slice per render, fifteen over
  the sets at base.
- error / empty / loading states — no resolver is a note and tag-only lines; an unresolved tag is a
  refusal; a role with no slices renders no heading; no policy kit renders `handed`.
- observability — the note and the refusal name the key, the role and the tag.
- risks — a protocol edit stales role files, which the render wiring leg names; the spec writer's
  static block grows by its seven sections under `handed`, priced by S9 and halved under `pointer`.
- testing — AC1 to AC10 by a pass over scratch fixtures; the arms of §7 at the close.
- migration — as §4 says; landed handoffs are frozen records.
- user docs — `help/roles.md`, by S10.

## 6. Acceptance criteria

- **AC1** — When `python render_agents.py --write` runs in a scratch adopter with no policy file,
  `grep -c '^### Method slices$'` over the rendered `gov-builder.md` prints 1, the file holds the
  line `#### doc.build-method#m6-passes-commits-parallelism` followed by M6's first paragraph, and
  `grep -c '^### Protocols'` over every rendered agent file prints 0.
  Red when: the render still carries the whole Protocols section, or carries no slice text.
  fixture: a scratch clone with the roles, playbook and policy kits installed.
- **AC2** — When the AC1 render runs with the scratch policy file setting `instructions.slices =
  "pointer"`, `gov-builder.md`'s block holds exactly one `- ` line naming the tag and
  `memory/guides/BUILD-METHOD.md` with a `lines <lo>-<hi>` range, and no line of M6's text.
  Red when: the pointer names the document without a range, or the text travels anyway.
- **AC3** — When a scratch role file declares `slices: doc.build-method#m99-no-such-section` and
  `python check_roles.py` runs, it exits 1 with an R3 line naming that file and the tag; with the
  entry removed it exits 0.
  Red when: an unresolved slice renders silently as an empty block.
- **AC4** — When `python -c` calls `roles_lib.parse_charter` on a fixture charter carrying a
  section 1 rule and `## Facts` but no `## Protocols`, it returns with `carried` holding Facts alone;
  the same fixture without `## Facts` raises `RolesError` naming R0; and `roles_lib.CARRIED_SECTIONS`
  prints `('Facts',)`.
  Red when: R0 still demands a Protocols section no role carries.
- **AC5** — When a scratch role body gains the text `BUILD-METHOD.md` and `python check_roles.py`
  runs, it exits 1 with an R5 line naming the file; the same text in a scratch house overlay gives an
  R10 line.
  Red when: re-pointing the protocol file list off the carried body leaves it empty, so both bans go
  quiet.
- **AC6** — When `grep -rn "Verify every claim about current code" tools/roles/agents/` runs it
  prints nothing, `grep -c "re-verify" gov-session.agent.md` in that directory prints 0, and
  `grep -c "counts as verified when" memory/TEMPLATE-SPEC.md` prints 1.
  Red when: an order survives in one role file, or the template and its render disagree.
- **AC7** — When `python check_roles.py` runs over gov after the pass, it exits 0, and for each
  role `budget` minus the measured whole block equals the headroom it had before the pass, printed by
  a `python -c` over `render_static_block` for every role.
  Red when: a budget rounds up, granting the body bytes nobody approved.
  figure: the headroom is DERIVED at the pass from the role files before and after.
- **AC8** — When `python -c` calls `roles_lib.resolve_slices` on a fixture guide whose second
  `##` section holds a fenced block containing a `## ` line, the cut for the first tag ends at the
  line before the second section's heading, and the cut for the second runs past the fenced line to
  the end of file.
  Red when: a heading inside a fence ends a slice early.
- **AC9** — When the AC1 render runs with the policy kit removed from the scratch clone, it exits 0
  and renders `handed`; with the playbook kit removed it exits 0, prints the note naming
  `gov_tag.py`, and `gov-builder.md` holds `not installed: no tag resolver`.
  Red when: an absent optional kit refuses the render.
- **AC10** — When `grep -n "instructions.slices" README.md` runs in `tools/roles/` and the same over
  `help/roles.md`, each prints a line.
  Red when: the docs still say the role carries the whole Protocols section.

## 7. Gates

The pass adds no leg: `roles catalogue` runs R0, R3, R5 and R10, and the render legs run the renders.

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/render_agents.py · covers AC1 AC2 AC8 · arm 4's fixture guide with a fenced `## ` line and a role declaring one slice, staged by cutting at every heading line · none
New arm: tools/roles/adopt-roles.test.sh · covers AC3 AC5 · a scratch role declaring an unresolved slice and a body spelling a protocol file, staged by dropping the R3 slice join · none

## 8. Open questions

- **F1 — What addresses a slice, and what cuts it, until dConvergedCharter's slices land (D6)?**
  Options: (a) PLAY-dOrderedCharter-19's `doc.<name>#<seg>` section tags, resolved by `gov_tag.py
  where` to `path:line`, cut in the roles kit to the next unfenced `## `; (b) `extract_chunks`
  (`tools/memory-recall/extract.py:730`) reached by subprocess; (c) a roles-kit address
  `<file>#<heading>` cut in-kit. (b) loses two probes: its `heading_level` (`extract.py:604-606`)
  is not fence-aware, so TEMPLATE-SPEC's skeleton splits at its fenced `## 1. Goal`, and its
  `CHUNK_MAX = 2400` (`extract.py:259`) windows M2's 3,565 bytes into two chunks; it also has no CLI,
  so the subprocess would import a sibling kit's module. (c) mints a second spelling of a section
  beside the tag index. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich
  survivor, tie-broken by reuse: dOrderedCharter is an ancestor of this build (v2:1767-1773), so its
  tags exist at the build run, and the hand-over to dConvergedCharter is a tag change. widens: none ·
  relaxes: none
- **F2 — Do handed slices count against the role's static-block budget?** Options: (a) yes, each
  `budget` re-derived by TOOL-dBoundRoles-15 §4 "Pricing" (base allowance plus measured charter
  block), so the body gains nothing; (b) slices carried in the task, outside the budget; (c) each
  role's set trimmed to today's headroom. (b) contradicts J19 and leaves the static block's slices
  unpriced; (c) hands the spec writer one section of the seven its body cites. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the precedent TOOL-dBoundRoles-15 §8 F3 set: the measure moves
  and the allowance does not, so `layer-roles.md:384-386`'s owner approval for a raise is not
  engaged. widens: none · relaxes: none
- **F3 — The parents this unit calls are specced and unbuilt at base `2193e25d`.** TOOL-dBoundRoles-2's
  `role-schema.toml`, TOOL-dBoundRoles-15's `render_static_block` and `budget`, TOOL-dBoundRoles-21's
  `read_policy_setting` and PLAY-dOrderedCharter-19's `gov_tag.py` do not exist in the tree.
  RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on each at the pass, re-derives
  S5's reader list with `git grep -n CARRIED_SECTIONS`, and stops the unit if a called section is
  still absent then, rung 1 (the brief's rule for DEFERRED parents). widens: none · relaxes: none
- **F4 — Is editing `memory/TEMPLATE-SPEC.md`'s writing rule inside this build's grant?** The clause
  names the role files' re-verification orders, and gap-roles-10, which this build owns, cites the
  template's line 106 as one of them. RESOLVED (agent, 2026-10-26, delegated): yes, rung 3 with veto
  2 lifted by the grant. grants: PLAY-dClosedLoop-3 the spec format's verification rule rewritten.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 8, the brief's J1 and J19 and its D6,
  scout C's row 8, and the source at `1a3ce03d`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-29, promoted from the round-1 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `CARRIED_SECTIONS` and `parse_charter` (`tools/roles/roles_lib.py:67`,
`:201-249`), whose section split becomes the one `parse_sections`; `render_charter_blocks`
(`:309-328`), the one composition every agent file and inline task already passes through;
`render_agent_file` (`tools/roles/render_agents.py:144-155`) and `render_handoff`'s charter append
(`tools/roles/handoff.py:401-407`); `PROTOCOL_PATH_RE` and the R5/R10 bans
(`tools/roles/check_roles.py:110-111`, `:171-172`, `:218-220`, `:361-363`); `resolve_kit_dir`
(`roles_lib.py:97`) for the playbook kit. `python tools/codebase-map/reuse_lookup.py "hand a role
agent the protocol sections it needs instead of whole documents"` returned name-stem candidates
only (`RolesError`, `load_roles`, `render_role`, `REVIEW-PROTOCOL.md` as an inventory key),
none of them a section cut, as scout C found; the seams above were read from source. The recall probe returned scout C's row, the brief's
row, `layer-roles.md:348`'s `[tags]` paragraph naming the machinery to re-point, and
TOOL-aOrientedCast-16, the unit that made every agent carry the Protocols section whole (its §8 F3,
cited at `roles_lib.py:66`); this unit reverses that carry, which the clause orders. Scout C's line
numbers, read at `281c336e`, match source at `1a3ce03d`, no file under `tools/` having changed
between them, except that `PROTOCOL_PATH_RE`'s comment sits at `:110`, one line above scout C's
`:111`. No protocol slice exists to reuse: dConvergedCharter owns them (systems.md:422).

Recall terms used: `python tools/memory-recall/query.py "how does a role agent receive protocol
sections and what carries the charter's Protocols section" --terms "CARRIED_SECTIONS Protocols
parse_charter render_charter_blocks slices instructions.slices R0 R5 R10 doc tag gov_tag"`
