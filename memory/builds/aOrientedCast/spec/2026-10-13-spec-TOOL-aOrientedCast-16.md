# TOOL-aOrientedCast-16 — a role cites section 1 rule tags, and its agent carries those rules with the Protocols and Facts sections

**Status:** INPROGRESS · rev-1 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams tooling · order 16 · ratified 2026-10-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md) | journal | TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 PLAY-aOrientedCast-2 |
| [2026-10-13-prompt-TOOL-aOrientedCast-16-2-build-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-2-build-brief.md) | journal | TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 PLAY-aOrientedCast-2 |

<!-- /gen:spec-records -->

## 1. Goal

Main's charter is template v4.3, which has no `## §<n> — ` heading, so every role's `charter` id
resolves to nothing, the catalogue checker reds once per id, and the agent render and the handoff
render refuse. This unit replaces the `charter` key with `rules`, naming section 1 rule tags, and
makes `roles_lib` the one reader of the charter, so each agent type and handoff carries its cited
rule lines verbatim and the Protocols and Facts sections whole, and a rule edit stales exactly the
agent types that cite it.

## 2. Scope (IN)

- **S1** — `tools/roles/roles_lib.py` gains `parse_charter`, `check_rule_tags` and
  `render_charter_blocks` with the constants of §4 "The reader", and `FRONT_MATTER_KEYS` carries
  `rules` in the position `charter` held. `extract_charter_sections` retires: every caller moves to
  `parse_charter`, and `SECTION_RE` stays only as the pre-tag detector §8 F2 resolved.
  **Readers:** by name: `tools/roles/check_roles.py`, `tools/roles/render_agents.py`,
  `tools/roles/handoff.py`, `memory/map/generated/symbols.json`; by value:
  `tools/roles/check_roles.py`, `tools/roles/render_agents.py`, `tools/roles/handoff.py`.
  Observed by AC1 and AC2.
- **S2** — `tools/roles/check_roles.py` grades the `rules` key as §4 "The checker" states: R0 gains
  the three charter-shape refusals, R1 gains the tagged charter cited by no tag, R4 grades rule tags,
  R5 and R10 refuse a base body or an overlay naming a protocol file, a pre-tag charter prints one
  note, and the summary line counts rule tags and protocol file names. The catalogue region's
  `charter` column is replaced by `rules`. **Readers:** by name: `tools/roles/README.md`; by value:
  NO VALUE READERS — R11 compares the region only with a fresh render of itself. Observed by AC3 and
  AC4.
- **S3** — `tools/roles/render_agents.py` writes each agent type's body as `render_role`'s output,
  then `## Charter`, then `render_charter_blocks` for its role, and prints the library's notes. Its
  self-test fixture becomes a tagged charter inside a playbook region, arm 4 is re-keyed, and arms 14
  and 15 are added, as §4 "Self-test arms" states. Observed by AC4 and AC5.
- **S4** — `tools/roles/handoff.py` appends `render_charter_blocks` for the role as the last block of
  `## Task`, prints the library's notes on stderr as `handoff: note — <text>`, and its docstring at
  lines 11, 26 and 38 names rule tags and the charter's `[security]` rule. Observed by AC6.
- **S5** — In every role file under `tools/roles/agents/`, the `charter` key is replaced by `rules`
  holding the tags of §4 "The role files", and each body names a protocol by its name, never by its
  file. **Readers:** by name: `tools/roles/roles_lib.py`, `tools/roles/check_roles.py`,
  `tools/roles/render_agents.py`, `tools/roles/handoff.py`, `tools/roles/README.md`,
  `tools/roles/adopt-roles.sh`, `WIRE-INTO-PROJECT.md`, `help/roles.md`; by value:
  `tools/roles/check_roles.py`, `tools/roles/render_agents.py`, `tools/roles/handoff.py`.
  Observed by AC3 and AC7.
- **S6** — Gov's renders are refreshed in the build commit: `.claude/agents/` by
  `render_agents.py --write`, the roles README's catalogue region by `check_roles.py --write`, and
  the `/build` Skill by `adopt-roles.sh --scaffold` after `tools/roles/SKILL.template.md:95` cites
  the charter's `[land]` rule where it cites a template section by number. `.claude/roles.json`
  stays byte-identical. Observed by AC5 and AC7.
- **S7** — The documents that describe the old key say the new one: the roles README's handoff,
  agent-type, adopting and checker sections, the comment at `tools/roles/adopt-roles.sh:15-16`,
  `help/roles.md:16-17`, the paragraph at `WIRE-INTO-PROJECT.md:720-721`, and the roles dossier's
  prose at `memory/map/features/roles.md:38-39` and `:113-114`, whose `decisions` list gains this
  unit's id. NOT OBSERVED by a criterion: prose, read by the review against §4; AC7's grep covers
  the kit's own citations by number.
- **S8** — `python tools/codebase-map/gen_map.py --write` regenerates the map artifacts in the build
  commit, because the minted and retired functions move the symbol tier. NOT OBSERVED by a
  criterion: the `codebase-map coverage + freshness` leg observes it at the close.

## 3. Non-goals (OUT)

- The `[roles]` rule, the Agent roles section, the `mandatory` and `output` fields, the `roster`
  verb, the `ROLE_ROSTER` placeholder and the inline stand-in's waiver registry. Those are
  TOOL-aOrientedCast-17, TOOL-aOrientedCast-18, TOOL-aOrientedCast-19 and PLAY-aOrientedCast-2.
- Any edit of `coding-governance-agents.template.md` or of `AGENTS.md`. This unit reads the charter
  and changes nothing in it.
- A new checker rule number. The protocol-file ban rides R5 and R10, and the shape refusals ride R0
  and R1, so a sibling adding rules numbers on from R13 with nothing to reconcile.
- A gate that each bare tag exists in every v4.x seed. No tree here holds the older seeds; the
  README states the rule a kit author follows (§4 "The role files").
- Stripping the `<!-- one-line -->` markers or any other line from a carried section. Whole means
  whole.
- Any change to the hooks, the harnesses, `.claude/roles.json`, the workflow table or the policy
  file.
- A roles kit version bump. `KIT_ROLES_VERSION` at `tools/roles/roles_lib.py:18` and the
  `gov:kit roles@` markers at `tools/roles/README.md:1` and `tools/roles/SKILL.template.md:5`, with
  its render at `.claude/skills/build/SKILL.md:5`, move once, in the last unit of this build that
  moves the roles kit. `tools/check-kit-versions.sh:387-393` grades the constant against the README
  marker, and govkit reads the version through `tools/roles/kit.toml:22`.

**What it is built on.** The catalogue grammar, the library and the checker of
TOOL-aOrientedCast-1; the handoff renderer of TOOL-aOrientedCast-2; the agent render of
TOOL-aOrientedCast-3, whose §8 F1 put charter blocks into the agent type and which this unit
re-keys; the default install and its adopter test of TOOL-aOrientedCast-8 and
TOOL-aOrientedCast-15; and the trailing `?` for an optional name that TOOL-aOrientedCast-13 gave
the policy's `[gates]`. Each is CLOSED and declares no edge to this unit, so the dependency is
stated here rather than as an edge.

### Edges

- **hands-off** `TOOL-aOrientedCast-17` — a catalogue checker and an agent render that read the
  v4.3 charter's tagged section 1 rules without a defect, on which its two front-matter keys, their
  checker rules and its re-render are built. This unit mints no checker rule number, so its rules
  take the next free numbers after R12.
- **hands-off** `TOOL-aOrientedCast-19` — a `handoff.py render` and a `check_roles.py` that read the
  v4.3 charter without refusing, which its stand-in render and its registry grader extend.
- **hands-off** `PLAY-aOrientedCast-2` — an agent-type render that reads the v4.3 charter's tagged
  rules and carries its Protocols and Facts sections whole, and the help page's step 2 re-keyed to
  rule tags, on which that unit's help-page edits and its unmoved agent types rest.

## 4. Design

### Evidence

Read at `d518b483` on 2026-10-13, node a.

- `parse_front_matter` keeps a list value as one comma-separated line, the form `tools:` takes
  (`tools/roles/roles_lib.py:8-11`), and `FRONT_MATTER_KEYS` holds `charter`
  (`tools/roles/roles_lib.py:23-24`).
- `extract_charter_sections` reads only `## §<n> — ` headings (`tools/roles/roles_lib.py:49`,
  `tools/roles/roles_lib.py:134-145`). A `python -c` probe of it over `AGENTS.md` returned an empty
  map, so every `charter` id misses. Its callers are `tools/roles/check_roles.py:117`,
  `tools/roles/handoff.py:323` and `tools/roles/render_agents.py:115`.
- `AGENTS.md` is the playbook region whole (`AGENTS.md:1`, `AGENTS.md:158`). Section 1 opens at
  `AGENTS.md:12`; its tagged rules sit in two one-line regions, the second under the
  `### Micro-formats` sub-head (`AGENTS.md:14-50`, `AGENTS.md:68-78`). Section 3's
  `## Protocols — read the one whose trigger holds` is `AGENTS.md:134-142` and `## Facts` is
  `AGENTS.md:144-157`.
- The template fences `[cross-os]` in `<!-- when:cross-os -->` (`coding-governance-agents.template.md:42-44`),
  so a target that did not answer cross-os renders no such rule.
- A probe of every template commit marked v4.x found `[spec]` absent from every v4.0 commit and
  from the first v4.1 commit, `37c39f9c1` (for example
  `git show 9ae1d023e:coding-governance-agents.template.md`), and `[cross-os]` fenced in every one.
  Every other tag §4 "The role files" cites is unconditional in all of them, and every one carries a
  `## 1. ` line, `## Protocols` and `## Facts`. A v3.6 charter carries `## §<n> — ` headings, no
  tagged rule and neither section (`git show 646d4a73:AGENTS.md`), inside a playbook region with
  authored sections before and after it.
- An adopter's template is a seed `govkit update` never rewrites, and the playbook engine renders a
  v3 seed with a reseed note rather than a refusal (`tools/govkit/entries/playbook.kit.toml:134-138`,
  `tools/playbook/render_playbook.py:990-993`).
- The commit trailer and the kinds map, which the types rendered from the v3 charter's numbered
  sections gave the builder and the spec writer (`git show d518b483:.claude/agents/gov-builder.md`
  carries the trailer under its `### charter §3` block, and the spec writer's type the kinds map
  under `### charter §12`), are lines of v4.3's `## Facts` (`AGENTS.md:155`, `AGENTS.md:157`), and
  no section 1 tag carries either.
- The charter cites itself by handle since v4.0, and `playbook parity` fails any live file of a kit
  that cites a charter or template section by number (`tools/check-playbook-parity.sh:313-347`).
  Its predicate, run over the roles kit, hits every role file's `charter:` line,
  `tools/roles/SKILL.template.md:95`, `tools/roles/handoff.py:38` and the self-test fixture at
  `tools/roles/render_agents.py:304-307` and `:332-336`.
- The spawn guard hashes a prompt's `## Task` section from that line to the end of the text
  (`tools/hooks/agent-cap.js:2055-2062`), so blocks appended to the task section stay inside the
  hashed span.
- The role gate refuses a role agent a command whose argv equals a leg's word for word
  (`tools/hooks/scratch-guard.js:1374-1379`): `python tools/roles/check_roles.py` bare is the
  `roles catalogue` leg, while `render_agents.py --write`, `render_agents.py --check` and a
  `python -c` probe are not legs, which is why §6 observes the checker through its function.
- The govkit install arm and the adopter test copy gov's own charter into their targets
  (`tools/govkit/selftest.py:2791`, `tools/roles/adopt-roles.test.sh:60`), so both read v4.3 tags
  once this unit lands. The adopter test's arm 6 feeds a rendered task part to the spawn guard
  (`tools/roles/adopt-roles.test.sh:102-137`).

### The reader

Constants in `roles_lib.py`:

```python
#: The playbook render's region markers. A charter rendered into a larger file sits between them,
#: and only that span is read, so an adopter's own sections around it never reach an agent.
PLAYBOOK_OPEN, PLAYBOOK_CLOSE = "<!-- gov:playbook -->", "<!-- /gov:playbook -->"
SECTION_ONE_RE = re.compile(r"^## 1\. ")
#: A section 1 rule line, `- [<tag>] <text>`; the whole line is the rule.
RULE_LINE_RE = re.compile(r"^- \[([a-z0-9][a-z0-9-]*)\] ")
#: One entry of a role's `rules` value: a tag, a trailing `?` marking it optional.
RULE_KEY_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\??$")
#: The section 3 headings every agent type and handoff carries whole, in this order (§8 F3).
CARRIED_SECTIONS = ("Protocols", "Facts")
#: A v3.x charter's numbered heading, kept only to tell a pre-tag charter from an unknown doc.
SECTION_RE = re.compile(r"^## (§\d+) — ")
LEGACY_NOTE = ("%s is a pre-tag charter: it carries `## §<n> — ` headings and no section 1 rule tag, "
               "so no role's rules resolve and no agent type or handoff carries the charter; reseed "
               "the charter template from gov, then re-render")
```

`parse_charter(text, where)` turns the governing doc's text into one structure and raises
`RolesError` on a doc that is not a charter this kit reads. `where` is the display path every
message names.

1. CRLF folds to LF. When the text holds `PLAYBOOK_OPEN` once and `PLAYBOOK_CLOSE` once after it,
   only the lines between them are read; otherwise every line is.
2. A section is a `## ` line and the lines after it, up to the next `## ` line or the end of what is
   read. `###` lines stay inside their section.
3. Section 1 is the first section whose line matches `SECTION_ONE_RE`. Its rules are its lines
   matching `RULE_LINE_RE`, each kept whole, in charter order. A tag found twice raises
   `<where>: R0 — the governing doc repeats the rule tag [<tag>] in section 1`.
4. For each name of `CARRIED_SECTIONS`, the carried section is the first section whose line is
   `## <name>` or opens `## <name> `. Its heading is the line without `## `, and its body is its
   lines with blank edges trimmed.
5. With at least one rule, the shape is `tagged`, and each carried name must be found, else
   `<where>: R0 — the governing doc carries section 1 rule tags and no '## <name>' section, which every role agent carries`.
   With no rule and at least one line matching `SECTION_RE`, the shape is `legacy`, with no rules
   and nothing carried. Otherwise it raises
   `<where>: R0 — the governing doc carries neither a section 1 rule tag nor a '## §<n> — ' heading, so it is no charter this kit reads`.

```python
{"shape": "tagged",                                  # or "legacy"
 "rules": {"yagni": "- [yagni] YAGNI: ...", ...},    # section 1, charter order
 "carried": [("Protocols — read the one whose trigger holds", "<!-- one-line -->\n- ...\n<!-- /one-line -->"),
             ("Facts", "- **Product:** ...\n- **Commit trailer:** ...")]}
```

`check_rule_tags(charter, value)` returns `(defects, notes)`, two lists of strings naming no path,
for one role's raw `rules` value. It is the one predicate the checker and both renderers apply.

| An entry of the comma-separated value | Tagged charter | Legacy charter |
|---|---|---|
| not `RULE_KEY_RE` | defect: `rules entry '<e>' is not a lowercase tag, optionally ending in ?` | the same defect |
| its tag already named in this value | defect: `rules tag '<tag>' is named twice` | the same defect |
| bare, and section 1 holds the tag | admitted | admitted, unresolved |
| bare, and section 1 lacks it | defect: `rules tag '<tag>' names no section 1 rule of the governing doc` | admitted, unresolved |
| ending in `?`, and section 1 lacks it | note: `rules tag '<e>' names no section 1 rule of the governing doc, so this role carries no such rule here` | admitted, unresolved |

An empty value is legal, as an empty `charter` value was, and yields nothing.

`render_charter_blocks(charter, where, value, notes=None)` turns that structure into the text a
role agent carries. It raises `RolesError` with one `<where>: R4 — <defect>` line per defect, and
appends `<where>: <note>` to `notes` when one is given. On a legacy charter it returns `""`.
Otherwise it returns the blocks below joined by one blank line, ending in one newline: a
`### Charter rules` block holding the section 1 lines whose tag the value cites, in charter order,
present only when at least one is cited; then one block per carried section, its heading line
demoted to `### ` with its text verbatim, then its body verbatim.

### The agent type and the handoff

An agent type's front matter is unchanged. Its body:

```markdown
<render_role(kit_dir, slot, MEMORY_ROOT), ending in one newline>

## Charter

### Charter rules

- [yagni] YAGNI: build what this unit needs now, never scaffolding for later, and delete rather than disable.
- [reuse] Reuse before building: ...

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
...
<!-- /one-line -->

### Facts

- **Product:** ...
- **Commit trailer:** every agent commit ends with `...`.
```

In code: `text += "\n## Charter\n\n" + blocks` when `blocks` is not empty, so a legacy charter's
types carry no `## Charter` at all. On a tagged charter every type carries it, because the carried
sections reach every role whatever it cites. `load_catalogue` returns `parse_charter`'s structure
under `charter` where it returned `sections`, and `render_agent_file` takes that structure and a
`notes` list in place of `sections` and `charter_path`; `run_mode` prints each note as it prints the
policy's, `render_agents: note — <text>`.

A handoff's `## Task` keeps its opening and its `reads` blocks in declared order, then takes
`blocks.rstrip("\n")` as its last block when `blocks` is not empty. The role section is unchanged,
so `role-sha` moves only where `render_role` moves. A typed spawn handed a handoff carries the blocks
twice, the cost TOOL-aOrientedCast-3 §8 F1 accepted.

Because the blocks are the charter's own bytes, the render order is charter first and agents second:
an edit to a cited rule line stales exactly the types whose role cites that tag, and an edit to a
carried section stales every type, which `render_agents.py --check` reports and the
`roles render wiring` leg reads.

### The checker

| Rule | After this unit |
|---|---|
| R0 | adds: a governing doc of neither shape, a tagged doc lacking a carried section, a tag repeated in section 1 — each `parse_charter`'s refusal, exit 2 |
| R1 | adds: a tagged charter that no role's `rules` cites a tag of, as DEAD PROBE |
| R2 | `rules` is required and may be empty; `charter` is an unknown key, refused by `parse_front_matter` |
| R4 | each defect `check_rule_tags` returns; each of its notes prints as `roles: note: <path>: <note>` |
| R5 | adds: a base body spelling the file name of a protocol the charter's Protocols section names |
| R10 | adds: an overlay spelling such a file name |

The protocol file names are derived from the carried Protocols body: each backticked token ending in
`.md`, cut to the text after its last `/`. In gov they are the file names of every guide and
template the section lists; a body that writes "the build method's M6" spells none of them. On a
legacy charter no tag resolves and no file name is derived; one line, `roles: note: ` and
`LEGACY_NOTE` naming the doc, says so, and the shape-only R4 grading still runs. The summary line
replaces its charter-id count with
`<n> rule tags and <m> protocol file names against <doc>, a <tagged|pre-tag> charter`, both counts
derived.

The header's R lines and its WHAT THIS DOES NOT CHECK paragraph say the same, adding: whether a
cited rule suits its role, and whether a bare tag exists in every v4.x seed an adopter may hold.

### The role files

Tags are chosen from the rules' text for what each role produces. A tag every v4.x template carries
outside any `when:` or `kit:` block is cited bare. A tag a target's charter may lack is cited with
`?`: `cross-os`, fenced by `when:cross-os`, and `spec`, which v4.0 and the first v4.1 commit lack.
Each row is written in charter order. The roles README states this rule for whoever edits a role.

| Role | `rules` | Why these |
|---|---|---|
| `gov-builder` | `yagni, reuse, core, derive, verify, gate, security, bytes, cross-os?, tools` | builds the least on the named seam, verifies directly, lands gates seen red, and meets byte, OS and hook refusals |
| `gov-spec-writer` | `yagni, reuse, core, contract, derive, one-fact, spec?, verify, gate, class, small, docs, security` | designs the unit: its seam, its contracts, its acceptance and gates, its size, its help page and its security checklist |
| `gov-spec-reviewer` | `spec?, verify, gate, class, security, risk` | holds a spec to what a spec, a criterion and a gate must be, adversarially |
| `gov-diff-reviewer` | `verify, gate, class, left-shift, security, risk, bytes, cross-os?` | hunts defects by class in code and proposes the gate each finding owes |
| `gov-skeptic` | `verify, class, risk` | confirms only what it observes itself |
| `gov-synthesizer` | `left-shift, risk, signal` | writes one report whose every finding owes a gate |
| `gov-orienter` | `small, ids, memory, tokens, tools` | derives a small scope, cites ids without minting them, and reads tools rather than re-deriving |
| `gov-researcher` | `reuse, verify, class, memory` | tests candidates against the real tree, seam first, records as background |
| `gov-reuse-scout` | `reuse` | finds the seam |
| `gov-session` | `ids, memory` | owns its own ids and re-verifies the sender's records |

Each body names a protocol by its name: `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md` becomes "the build
method", `{{MEMORY_ROOT}}/guides/REVIEW-PROTOCOL.md` "the review protocol", and
`{{MEMORY_ROOT}}/TEMPLATE-SPEC.md` "the spec format", each keeping the M-section it cites. The
builder's "the trailers the build method and the charter sections you were given require" becomes
"the trailers the build method and the charter facts you were given require". A body that carries
no `{{MEMORY_ROOT}}` afterwards is legal.

### A pre-tag charter

§8 F2. `parse_charter` classifies the doc, and each consumer prints `LEGACY_NOTE` once per run:
the checker as a `roles: note:` line, the agent render as `render_agents: note — <text>`, and the
handoff on stderr. The agent types and handoffs render with no charter block, every mode exits 0,
and the adopter's `--scaffold` and `--check` succeed, so a v3 seed takes the roles kit at update and
is told to reseed. A doc of neither shape refuses as R0, because a doc this kit cannot read is not a
pre-tag charter.

### Self-test arms

`build_fixture` writes `DOC.md` as a tagged charter inside a playbook region, with a section after
the region's close:

```markdown
<!-- gov:playbook -->
# Doc

## 1. Practices

<!-- one-line -->
- [one] Rule one.
- [two] Rule two.
<!-- /one-line -->

## Protocols — read the one whose trigger holds

- A pass: `mem/P.md`.

## Facts

- **Fact:** one.
<!-- /gov:playbook -->

## Authored

after the region
```

The fixture roles carry `rules: two, one` for `r-one`, an empty `rules:` for `r-two` and
`rules: one` for `r-off`.

- **Arm 4, re-keyed.** `r-one`'s type ends with `## Charter`, then `### Charter rules` holding
  `- [one] Rule one.` before `- [two] Rule two.`, then the Protocols block, then
  `### Facts\n\n- **Fact:** one.\n`. `r-two`'s type carries `## Charter` with the two carried
  blocks and no `### Charter rules`. No type carries `after the region`.
- **Arm 14.** With `DOC.md` rewritten to `## §1 — One` and `## §2 — Two`, `--write` exits 0, one
  stdout line opens `render_agents: note` and carries `reseed`, and no type carries `## Charter`.
- **Arm 15.** With `three?` appended to `r-one`'s `rules`, `--write` exits 0 and one note line
  names `three?`. With `three` appended instead, `--write` exits 2, its stderr names `three` and R4,
  and every file under the fixture's `.claude/` keeps its bytes.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `parse_charter` | function, the governing doc's text into its structure | `py.function`; `lexicon.py --suggest parse_charter --as py.function` answered OK |
| `check_rule_tags` | function, one role's `rules` against the structure | `py.function`; answered OK |
| `render_charter_blocks` | function, the structure into a role agent's charter text | `py.function`; answered OK |
| `PLAYBOOK_OPEN`, `PLAYBOOK_CLOSE`, `SECTION_ONE_RE`, `RULE_LINE_RE`, `RULE_KEY_RE`, `CARRIED_SECTIONS`, `LEGACY_NOTE` | constants | none: `.lexicon.conf` declares no constant cell |
| `rules` | role front-matter key | none: front matter is graded by the catalogue checker |

Every new function leads with a verb the table carries, and the retired `extract_charter_sections`
did too, so the verb-offender count does not move.

### Migration

None for an adopter: the roles kit has not been pushed since it was built (the merge onto local
main, `6081d92e4`, left the run unpushed), so no adopter holds a role file or an overlay. Gov
re-renders its own types, README region and Skill in the build commit. A v3 seed that later takes
the kit gets the pre-tag note; a v4.x seed resolves every bare tag, and one that lacks `[spec]`
notes `spec?`.

### Rollout

One commit carries the library, the checker, the renderers, the role files, gov's three renders,
the documents and the regenerated map artifacts. Order inside the pass: the library and role files,
then `render_agents.py --write`, `check_roles.py --write` and `adopt-roles.sh --scaffold`, then
`gen_map.py --write`.

This session's agent registry was read before the render, so later passes of this run spawn the
types as registered at session start. A session started after the landing spawns the new ones.

### Files touched (estimate)

`tools/roles/roles_lib.py`
`tools/roles/check_roles.py`
`tools/roles/render_agents.py`
`tools/roles/handoff.py`
`tools/roles/agents/`
`tools/roles/README.md`
`tools/roles/SKILL.template.md`
`tools/roles/adopt-roles.sh`
`.claude/skills/build/SKILL.md`
`.claude/agents/`
`help/roles.md`
`WIRE-INTO-PROJECT.md`
`memory/map/features/roles.md`
`memory/map/generated/`

### Alternatives rejected

- **Rules in the order the key names them**, as `charter` ids were. The block would then depend on
  how an author ordered a list; in charter order it is a filter of section 1, checkable against the
  charter alone.
- **One block per rule, `### charter [<tag>]`.** It adds a heading per line and says nothing a
  line does not.
- **Carried headings kept at `## ` inside the handoff.** Legal for the spawn guard's hash, but every
  other block of `## Task` is `###`, and a reader would take `## Protocols` for a sibling of
  `## Task`.
- **Reading every tagged line of the doc.** Section 2 holds the adopter's own untagged rules, and a
  tag elsewhere would be a different contract.
- **Reading the whole file.** The v3.6 `AGENTS.md` at `646d4a73` holds authored sections before and
  after its playbook region, which would bleed into a carried body or shadow a heading.
- **Matching protocol paths in full after substituting `MEMORY_ROOT`.** It makes the checker read
  `MEMORY_ROOT`, and the file name alone is what a body spells.
- **A kit-owned map from tags to v3 sections.** §8 F2 (c).

## 5. Production-readiness checklist

- security — No new write path. Rule lines and carried sections are copied from the tracked
  governing doc into generated files; a hostile charter edit reaches every role agent, as a hostile
  role edit already does, and `--check` turns a hand edit of a type into a red leg. Reading only the
  playbook region keeps an adopter's authored text outside it away from every agent.
- perf / scale — One doc read per run. Each type carries one-line rules and two short sections where
  it carried whole numbered sections, so types shrink; `wc -c` over `.claude/agents/` before and
  after the render derives the figure at build time.
- error / empty / loading states — A doc of neither shape, a missing carried section and a repeated
  tag each refuse as R0, naming the doc. A bare tag the charter lacks refuses as R4 in the checker
  and both renderers, naming the role. An optional one is a note. A pre-tag charter is one note.
- observability — The summary line prints both derived counts and the charter's shape on every run,
  so a zero is visible; every note names the role or the doc.
- risks — A kit author adding a bare tag that an older v4.x seed lacks reds that adopter's render
  at update, and only the README rule guards it. The carried Facts name the bar command, which a
  role agent may not run; the role gate still refuses it. A charter edit to a carried section reds
  `roles render wiring` until a re-render, which is the intended signal.
- testing — Render self-test arms 4, 14 and 15, the checker's staged breaks and the wiring leg's
  staged rule edit, observed RED-first at the close; the direct probes of §6 in the pass; the adopter
  test's arm 6 for the spawn guard's admission of the longer task part.
- migration — None for an adopter, as §4 "Migration" states; gov re-renders in the build commit.
- user docs — `help/roles.md` step 2, the roles README and the runbook paragraph of S7.

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a self-test flag; each calls the unit's own code or reads
its output. The suite arms are under `New arm:` in §7.

- **AC1** — When a `python -c` probe calls `roles_lib.parse_charter` on the text of `AGENTS.md`, it
  returns shape `tagged`; its rules map holds exactly the tags that `^- \[([a-z0-9][a-z0-9-]*)\] `
  matches between the `## 1. ` line and the next `## ` line, each mapped to its whole line; and its
  carried list holds `Protocols — read the one whose trigger holds` and then `Facts`, each body a
  substring of the file whose last line is the line before the next `## ` heading or before
  `<!-- /gov:playbook -->`.
  Red when: a tag is missed or a rule line cut short, a carried body runs into the next heading or
  the region's closing marker, or Facts is not carried.
  figure: DERIVED — the tag set is the probe's own match at observation time.
- **AC2** — When the probe calls `parse_charter` on four texts, a v3 text whose only headings are
  `## §1 — One` and `## §2 — Two` returns shape `legacy` with no rules and nothing carried, and a
  text with neither shape, a tagged text with no `## Facts` line and a tagged text repeating `[one]`
  each raise `RolesError` naming R0, the one without Facts naming `Facts` and the one repeating the
  tag naming `one`. When it calls `render_charter_blocks` on AC1's structure with the value
  `yagni, nope`, it raises naming R4 and `nope`; with `yagni, nope?` it returns the yagni line and
  the carried blocks and appends one note naming `nope?`; on the legacy structure it returns an
  empty string.
  Red when: an unreadable doc passes as a pre-tag charter, a broken tagged doc parses, a bare
  missing tag renders, or an optional one refuses.
- **AC3** — When a `python -c` probe calls `check_roles.check_roles` with gov's root and the kit
  directory, it returns no defect and its summary names a rule-tag count above zero against
  `AGENTS.md`. Over a scratch copy of the kit with `nope` appended to `gov-builder`'s `rules`, its
  R4 lines are exactly one, naming `nope` and `gov-builder.agent.md` (the copy's README region also
  reads R11, since its `rules` column moved); with `BUILD-METHOD.md` written into the copy's
  `gov-spec-writer` body, its R5 lines are exactly one, naming that file; with the same name written
  into the copy's overlay for `gov-skeptic`, its R10 lines are exactly one. Over a scratch root whose
  `.memory-tree.conf` names a copy of `AGENTS.md` without its `[cross-os]` line, with gov's kit, it
  returns no defect and one `roles: note:` line per role citing `cross-os?`.
  Red when: an unresolvable bare tag, a protocol file in a body or in an overlay passes, or an
  optional absent tag reds.
  fixture: the kit copy and the scratch root sit under a short `%TEMP%` path, built in the pass.
  figure: DERIVED — the roles citing `cross-os?` are read from the role files.
- **AC4** — When a scratch repository holds a copy of the kit, a `.memory-tree.conf` naming
  `MEMORY_ROOT` and a `CHARTER` that holds `git show 646d4a73:AGENTS.md`, and the copy's
  `render_agents.py --write` runs there, it exits 0, exactly one of its `render_agents: note` lines
  carries `reseed` and names that doc, and no agent type it writes carries `## Charter`; and
  `check_roles.check_roles` over that root and that kit returns no R4 line and one `roles: note:`
  line carrying the same text.
  Red when: a pre-tag charter refuses the install, renders with no note, or carries part of a charter.
  fixture: a `git init` repository under a short `%TEMP%` path, built in the pass.
- **AC5** — When `python tools/roles/render_agents.py --write` runs in gov and
  `python tools/roles/render_agents.py --check` follows, the check exits 0. A `python -c` probe then
  finds each agent type's text after its front matter equal, byte for byte, to `render_role` plus
  `## Charter` plus `render_charter_blocks` for its role; `gov-builder.md` carries the
  `- [cross-os]` line of `AGENTS.md`; and no type carries `### charter §`. When the probe renders
  every type with `render_agents.render_agent_file` against `AGENTS.md` and again against its text
  with the `[verify]` line one word longer, the slots whose bytes differ are exactly the roles whose
  `rules` cite `verify`.
  Red when: the agent type and the library compose the charter two ways, a carried section is
  missing, or a rule edit leaves a citing type fresh or moves one that does not cite it.
  figure: DERIVED — the citing set is read from the role files at observation time.
- **AC6** — When `handoff.py render --role gov-researcher --build aOrientedCast --unit TOOL-aOrientedCast-16 --input question=probe --stdout --part task`
  runs from gov's root, it exits 0, its output ends with `render_charter_blocks`'s text for
  `gov-researcher` with its trailing newline as the task section's last bytes, and it carries no
  `### charter §` block.
  Red when: the handoff refuses on the v4.3 charter, or carries charter text its agent type does not.
  permission: whether the spawn guard admits the longer task part is the adopter test's arm 6, which
  the main loop runs at the close with the `roles adopter self-test` leg.
- **AC7** — When `git grep -n -E '^charter:' -- tools/roles/agents` runs it prints nothing, and each
  role file's `rules:` line equals its row in §4 "The role files"; when
  `git grep -n -I -i -E "(charter|template)('s)?[ ,:(-]{0,3}§ ?[0-9]" -- tools/roles .claude/skills/build .claude/agents`
  runs it prints nothing; and when
  `git grep -n -E 'BUILD-METHOD\.md|TEMPLATE-SPEC\.md|HYGIENE\.md|REVIEW-PROTOCOL\.md|UNATTENDED-PROTOCOL\.md' -- tools/roles/agents tools/roles/house`
  runs it prints nothing.
  Red when: a role keeps its `charter` key, the kit or its renders cite the charter by number, or a
  role file or an overlay names a protocol file.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `playbook parity` · `govkit selftest` · `govkit runbook parity` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/check_roles.py · covers AC3 · a role's `rules` staged to name a tag section 1 lacks, then a role body staged to name a protocol file · none
New arm: tools/roles/render_agents.py --selftest · covers AC2 AC4 AC5 · arm 4 against `render_charter_blocks` staged to key order, arm 14 against the pre-tag branch staged to raise, arm 15 against the optional branch staged to refuse · none
New arm: tools/roles/adopt-roles.sh --check · covers AC5 · the text of one cited rule line in `AGENTS.md` edited with no re-render, which must name exactly the citing types · none

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above. `playbook parity` and `govkit selftest` are listed because this unit is
what lets them pass, not as new arms: the parity predicate, run as a probe, hits the role files'
`charter:` lines (§4 "Evidence"), and the govkit install arm renders the roles kit over a copy of
gov's v4.3 charter, which today's agent render refuses. The second is read from the code and is
UNVERIFIED by a run, since no suite runs in a spec pass.

## 8. Open questions

- **F1 — How does a role file spell its list of tags?** The addendum writes the example as
  `rules: [spec, verify, gate]`. Options: (a) a comma-separated value, the grammar's one list form,
  as `tools:`, `reads:` and `charter:` already are (`tools/roles/roles_lib.py:8-11`); (b) a
  bracketed flow list; (c) both. (b) and (c) grow a second list form in the one grammar, and the
  brackets in the addendum read as the tags' own spelling in the charter, `[spec]`. No option
  satisfies a criterion the others fail; the tie-break is fewer open questions and reuse of the
  grammar's seam.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The role files" writes each row.
- **F2 — What does the kit do with a pre-tag (v3.x) charter?** An adopter's template is a seed
  update never rewrites, so a v3 adopter renders `## §<n> — ` headings with no tagged rule under the
  newest roles kit. Options: (a) refuse, R0 in the checker and exit 2 in the render, so the adopter
  exits 1 at install and update; (b) recognise the shape, print one note naming the doc and the
  reseed remedy, resolve no tag and carry no charter block, exiting 0; (c) as (b), carrying the v3
  doc's sections through a kit-owned map from tags to section numbers. (a) refuses the default kit
  to every v3 seed, against the playbook engine's own rule that a v3 seed renders with a reseed note
  (`tools/govkit/entries/playbook.kit.toml:134-138`). (c) is a second hand-kept copy of the charter's
  structure, and the v3 numbering moved between v3 releases, so it leaves more open than it closes.
  A doc of neither shape still refuses under every option, so a mis-set `CHARTER` is never read as a
  pre-tag charter.
  Recommendation: (b).
  RESOLVED (agent, 2026-10-13, delegated): (b), as §4 "A pre-tag charter" states.
- **F3 — Which section 3 sections does every role agent carry?** The owner's answer names the
  Protocols section. Under the v3 charter the builder and the spec writer took the commit trailer
  and the kinds map from numbered sections; in v4.3 both are `## Facts` lines (`AGENTS.md:155`,
  `AGENTS.md:157`) that no section 1 tag reaches, and an agent started with the charter omitted
  holds neither. Options: (a) Protocols only; (b) Protocols and Facts; (c) the whole of section 3,
  adding the node registry and the tools list. (b) closes the trailer and kinds gap that (a) leaves
  open, and it re-opens no owner answer: every agent still carries Protocols whole, and no role file
  names a protocol path. (c) adds sections no role agent acts on, and no criterion it satisfies
  beyond (b). No option trips a veto.
  Recommendation: (b), the most feature-rich survivor.
  RESOLVED (agent, 2026-10-13, delegated): (b), `CARRIED_SECTIONS` in §4 "The reader". The build
  README's roster line for this unit names Protocols alone and is the main loop's to widen.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read tagged one-line rules and a named section out of a
rendered markdown governing doc"` ranked only name-token neighbours of `read`, such as `read_text`,
`read_conf` and `read_conf_key`, none of which reads a charter. No existing seam outside the kit
fits. The seam extended is the kit's own charter reader, `extract_charter_sections` at
`tools/roles/roles_lib.py:134-145`, replaced in place by `parse_charter` for its three callers, with
the one composition, `render_charter_blocks`, shared by the agent render and the handoff where each
built its own blocks before. The optional `?` is the kit's existing spelling for an optional name,
in a role's `reads` (`tools/roles/handoff.py:318`) and in the policy's `[gates]`
(`tools/roles/roles_lib.py:306`). The pre-tag note follows the playbook engine's reseed note
(`tools/playbook/render_playbook.py:990-993`).

`python tools/memory-recall/query.py "how does an agent role cite the charter and what happens when
the charter has no numbered sections"` surfaced the TOOL-aOrientedCast-1 brief's charter-per-role
interface, TOOL-aOrientedCast-3 §8 F1, the owner's second addendum, the roles dossier and this
unit's brief. Each was read against source; the dossier's sentence that `## §<n> — ` headings are
the kit's only outside contract is what S7 corrects.

Recall terms used: `role charter section tag one-line rule Protocols governing doc agent type omitClaudeMd v4 legacy reseed`
