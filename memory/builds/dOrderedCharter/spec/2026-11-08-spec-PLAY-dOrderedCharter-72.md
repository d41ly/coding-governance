# PLAY-dOrderedCharter-72 — the positional lists leave the kit, and the kit's code derives every path it spells

**Status:** DEFERRED · rev-2 · 2026-11-08 · node d · Tier-2 · base 93c4e987e · streams tooling · order 17 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-73 |
| [2026-11-08-prompt-PLAY-dOrderedCharter-72-1-spec-writer.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-72-1-spec-writer.md) | journal | — |
| [2026-11-08-prompt-PLAY-dOrderedCharter-72-build-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-72-build-brief.md) | journal | — |
| [2026-11-08-prompt-PLAY-dOrderedCharter-72-repair-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-72-repair-brief.md) | research | PLAY-dOrderedCharter-73 |

<!-- /gen:spec-records -->

## 1. Goal

Three close-bar legs that are green on `origin/main` go green over this tree again: the shipped-surface ban on
kit paths, the deleted-file carriers, and the drift report's product citations. A fourth, the method-carrier
census, stops naming the positional list. Nearly every offender is one cause: two gov-only lists sit under a
shipped kit. They move to `memory/project/`, the playbook kit finds them through `MEMORY_ROOT`, and the kit's
remaining literal kit paths are derived from each file's own location, as the ban's own remedy says.

## 2. Scope (IN)

Every line below was read at base `93c4e987e`. The Design section holds what a one-line item cannot.

- **S1** — `positional-refs.txt` and `positional-producers.txt` move from `tools/playbook/` to `memory/project/`,
  byte for byte, by `git mv`. The kit copy of `positional-refs.txt` retires, and so does the kit copy of
  `positional-producers.txt`. Observed by AC1 and AC2.
  **Readers:** by name: `tools/playbook/positional.py`, `tools/playbook/gov_tag.py`,
  `tools/playbook/render_playbook.py`, `tools/playbook/kit.toml`, `tools/playbook/README.md`,
  `tools/playbook/aliases.toml` and `help/tags.md` spell `positional-refs.txt`; `tools/playbook/positional.py`,
  `tools/playbook/kit.toml`, `tools/playbook/README.md` and `tools/govkit/selftest.py` spell
  `positional-producers.txt`. Each is re-pointed by S2, S3 or S5. by value:
  `tools/playbook/positional.py#check_positional` reads the rows of the first list,
  `tools/playbook/positional.py#check_producers` reads the second, and `tools/playbook/positional.py#read_git_grep`
  leaves the first out of its own scan.
- **S2** — `tools/playbook/positional.py` finds both lists under `<MEMORY_ROOT>/project/`, through one path
  function that takes the memory root, and its grep leaves the list out of the scan at that path. The
  memory-root read in `tools/playbook/positional.py#run_check` is hoisted into one reader the verbs share. The
  producer pathspecs and the selftest rows spell the tool root as `{prefix}/`, resolved through the kit's
  `resolve_prefix_token`. Observed by AC2, AC3 and AC9.
- **S3** — The readers outside the module follow. The tag fixture in `tools/playbook/gov_tag.py` writes its list
  under its own memory root, and lays its kit out at this install's layout: `FIXTURE_KIT` keeps its name and every
  reader, and takes a derived value. The write mode,
  `tools/playbook/render_playbook.py#write_empty_lists`, writes the empty positional list under the target's
  memory project folder and the empty pending list under the kit, each where its folder exists. Unit 71's arm in
  `tools/govkit/selftest.py` plants into `instructions-legacy.txt`. Observed by AC6, AC9 and AC10.
- **S4** — The hygiene engine's whitelist of `<MEMORY_ROOT>/project/` names, in
  `tools/memory-tree/check-memory-hygiene.sh`, admits `positional-refs.txt` by name, beside `pass-order-waiver.txt`,
  because the playbook kit's write mode writes it at every target. `tools/memory-tree/HYGIENE.template.md` and its
  dogfood `memory/HYGIENE.md` gain its bullet. Gov's `.memory-tree.conf` declares `positional-producers.txt` in
  `PROJECT_REGISTRY_EXTRA` as its twelfth member. Observed by AC7.
- **S5** — The `project-owned` include of `tools/playbook/kit.toml` holds `core-pending.txt` and
  `instructions-legacy.txt` alone, and its comment says where the positional lists live. The prose that places the
  lists beside the module is corrected in `tools/playbook/positional.py`'s docstring, `tools/playbook/README.md`,
  `tools/playbook/aliases.toml` and `help/tags.md`. Observed by AC1 and AC11.
- **S6** — The playbook modules spell no kit path. `tools/playbook/core.py` (26 spellings),
  `tools/playbook/gov_tag.py` (10), `tools/playbook/instruction_units.py` (9), `tools/playbook/positional.py` (5)
  and `tools/playbook/adopt-playbook.sh` (2) derive each from the module's own location, through the kit's
  existing layout readers. Observed by AC3 and AC9.
- **S7** — `tools/playbook/namespaces.toml` spells its twelve kit paths through `{prefix}/`, and
  `tools/playbook/tag_index.py#check_namespace_purpose` resolves that token against the registry's own tool root
  before it reads a `purpose-source` path. The resolver is an inline copy of the canonical `resolve_prefix_token`
  block. Observed by AC4 and AC9.
- **S8** — The `kind` row's `purpose-source` names `{prefix}/playbook/kinds.toml`, path-only, where it named a
  record under `memory/builds/dClosedLoop/`. The header comment of `tools/playbook/principles.toml` points at the
  conf key that names the design record, and spells no record id. Observed by AC5.
- **S9** — Three kits outside the playbook kit derive their fixture paths. `tools/lexicon/selftest.py` (3)
  reads the playbook home from a constant `tools/lexicon/lexicon.py` declares and its own resolver call reads.
  `tools/run-gates/py_reads.py` (1) and `tools/memory-tree/gotchas.py` (1) name their tool root from their own
  location. Observed by AC3 and AC9.
- **S10** — `memory/LIVE.md` is re-rendered by `python tools/memory-tree/gen_build_index.py --write`, because its
  product-citation column moves with the list. Observed by AC7.

## 3. Non-goals (OUT)

- **The lists' content.** No row is added, dropped or reworded. The move is a rename.
- **The encoding posture of `tools/playbook/core.py`, `tools/playbook/instruction_units.py` and
  `tools/playbook/positional.py`.** Their unencoded `subprocess.run` calls are unit 73's, which builds after this
  unit and reads its result.
- **The record fixes.** The method-carrier rows for `help/tags.md`, `tools/playbook/adopt-playbook.sh`,
  `tools/playbook/edge_grammar.py`, `tools/playbook/instructions-legacy.txt` and `tools/playbook/renderers.toml`
  are the main loop's, as are the kickoff manifest stamp and memory hygiene's own record reds.
- **A version line.** The kit-epoch leg reads every kit this build moved as owed at the lander, so no kit's version
  constant moves here.
- **Softening the absent-list red of `tools/playbook/positional.py#check_positional`.** Unit 70's skeptic kept it,
  and this unit keeps it by writing the empty list where the check now looks.
- **The tag fixture's non-kit directories.** `tools/corekit/`, `tools/expkit/` and the rest name no kit, so the ban
  does not count them and they stay as written.

### Edges

- **hands-off** `PLAY-dOrderedCharter-73` — the unencoded `subprocess.run` calls in `tools/playbook/core.py`,
  `tools/playbook/instruction_units.py` and `tools/playbook/positional.py`, the shell-idiom fix in
  `tools/playbook/adopt-playbook.sh`, and the `requires` row of `tools/playbook/kit.toml`, each on top of this
  unit's edits to the same files
- **hands-off** external — the method-carrier rows, the kickoff manifest stamp and memory hygiene's record reds,
  which the main loop writes

## 4. Design

### The cause, measured

At base the shipped-surface ban counts 18,847 kit-path spellings on 18,814 lines, from the close bar's log of
`install-prefix (shipped surface)` at `93c4e987e` (PINNED). 18,745 of them sit in `tools/playbook/positional-refs.txt`
and `tools/playbook/positional-producers.txt`, because the ban's population is every tracked file under the tool
root and each list row names a kit path. The same list carries all 5 dead-path rows, which cite files history
deleted, and 18 of the 19 offenders the drift report calls `new`, because its product globs are the tool root and
the list's rows name non-terminal specs. `memory/` is outside all three populations by declaration
(`tools/check-install-prefix.sh`, `tools/check-dead-paths.sh`, `tools/drift-audit/drift_signals.py#PRODUCT_GLOBS`),
and outside the method-carrier census, whose walk skips the memory root.

### The new home passes memory hygiene

The brief asked whether a 38,778-line, 4.4 MB list passes memory hygiene's budgets and pinned checks under
`memory/project/`. It does, measured in a scratch clone of `93c4e987e` with both lists moved and the producer list
named in `PROJECT_REGISTRY_EXTRA`:

| Check | Result | Why |
|---|---|---|
| Size and entry budgets | unaffected | the index set holds no file under `project/` |
| Id collisions, orphan ids, dead repo paths, read-path accounting | green at `ORPHAN_ID_PIN` 0 and `DEAD_PATH_PIN` 0 | `tools/memory-tree/corpus_ids.py#walk` reads `project/` as present-tense, but harvests paths only from backticked tokens and Markdown links, and the list holds neither; every id its rows spell is defined |
| The build-index render | red until `memory/LIVE.md` is re-rendered | the LIVE table's product-citation column counts the same citations the drift report does, and 11 rows of it fall |
| Every other check | the same verdicts as the bar's log at base | — |

So the home is `memory/project/` and no fork is owed. The recall floor's guard covers `memory/`, but the recall
corpus is Markdown alone (`tools/memory-tree/id_grammar.py#corpus_files`), so a `.txt` list moves no recall result.

### Which list goes where in the whitelist

`positional-refs.txt` is written at every target by the playbook kit's write mode, because the positional arm reds
an absent list. That is the kit-shipped class, and TOOL-bQuiltedLantern-3 rules it: a kit-shipped registry belongs
in the hygiene engine's whitelist, never in each adopter's `PROJECT_REGISTRY_EXTRA`. The named cases
`pass-order-waiver.txt` and `role-stand-in-waiver.txt` are that rule applied. So the whitelist gains a named case
for it, with a comment naming this unit, and gov's conf does not declare it.

`positional-producers.txt` is never written at a target. The arm reads it when present and reads an absent list as
nothing kept. That is the class `chain.toml` already sits in, gov's eleventh `PROJECT_REGISTRY_EXTRA` member, read
by the same kit at its default path. So it joins gov's conf as the twelfth member, with a comment in the shape of
the eleventh.

### The positional module

| Function | Change |
|---|---|
| `tools/playbook/positional.py#derive_list_path` | takes `memory_root` and a name defaulting to `LIST_NAME`, and returns `<root>/<memory_root>/project/<name>` |
| `tools/playbook/positional.py#run_check` | its memory-root expression moves into a new `read_memory_root(root)`, which `main` also calls for every verb |
| `tools/playbook/positional.py#read_git_grep` | its third parameter is the memory root, and its exclusion pathspec is the list's path under it |
| `tools/playbook/positional.py#read_producers`, `#check_producers`, `#run_producers` | read and seed the producer list through the path function; the pathspecs resolve `{prefix}/` against the tool root `kit_rel`'s parent names |
| `tools/playbook/positional.py#run_seed`, `#run_shrink`, `#run_pin` | take the memory root where they took `kit_rel` for the list |
| `tools/playbook/positional.py#check_positional` | passes its `memory_root` down; its messages name the list's tree path |
| `tools/playbook/positional.py#read_grandfathered` | unchanged: `kit_rel` still names the module whose adding commit is `L` |

`PRODUCER_PATHSPECS` becomes `{prefix}/roles/agents/`, `{prefix}/workflows/`, `skills/`, the charter template,
`{prefix}/playbook/practices.toml`, `{prefix}/*/SKILL.template.md` and `{prefix}/*/*.template.md`. The playbook kit
is always homed at `{prefix}/playbook/` (`tools/playbook/kit.toml`'s `to` row), so `{prefix}/playbook/` names it
correctly at every install. In `tools/playbook/positional.py#SELFTEST_ROWS` the three rows naming `tools/notes.md` and
the role file spell them `{prefix}/notes.md` and `{prefix}/roles/agents/gov-x.agent.md`, and
`tools/playbook/positional.py#run_selftest` resolves `{prefix}` beside its `{code}` and `{x}` tokens, against the
tool root the fixture lays out at.

The resolver is `resolve_prefix_token`, already inline in `tools/playbook/check_layers.py` and ten other files.
This unit adds the block inline to `tools/playbook/tag_index.py`, which `positional.py` imports as `ti`; the
module-level import of `check_layers` resolves the memory-tree kit, which unit 73 weighs. The parity row
`resolve_prefix_token` in `tools/lib/resolve-python.test.sh` finds every copy by its marker, so the new copy is
graded with no table edit.

### The writers and the moved arm

`tools/playbook/render_playbook.py#write_empty_lists` keeps its two names and its note. `positional-refs.txt` is
written under `<target>/<memory_root>/project/`, the memory root from
`tools/playbook/render_playbook.py#derive_memory_root`, where that folder exists and the list does not.
`core-pending.txt` stays under the kit directory, as today. A target with no memory project folder has no
memory-tree kit, and the tag arm already refuses there, because `tools/playbook/tag_index.py#load_memory_tree`
resolves that kit.

In `tools/playbook/gov_tag.py`, `tools/playbook/gov_tag.py#build_tags_fixture` writes the empty list at
`memory/project/positional-refs.txt`, beside the fixture's `chain.toml`, and
`tools/playbook/gov_tag.py#run_positional_plant` passes the fixture's memory root, `memory`, to every
`positional` call.

`FIXTURE_KIT` stays, and so does every reader of it: 14 uses in `tools/playbook/gov_tag.py`, among them
`write_chain_fixture`, `read_dump`, `run_plant`'s `run_verb` and five of its plant branches, and
`run_positional_plant`, plus two each in `tools/playbook/edge_grammar.py#build_resolve_fixture` and
`tools/playbook/instruction_units.py#arm_arms`, counted at `6eaaecd80`. Only its value moves, from the literal to
`instruction_units.derive_tool_rel(KIT_DIR.name)`, the seam `tools/playbook/instructions_edit.py` already uses for
the same fixtures. At gov it yields the same `tools/playbook`, so no reader's output moves. `gov_tag` imports
`instruction_units` at module level for it. That module imports nothing of `gov_tag`'s at module level, so no cycle
forms, and `derive_kit_prefix` spends one cached git call. The fixture's remaining literal kit paths in
`tools/playbook/gov_tag.py` spell the kit through `FIXTURE_KIT` too, and `tools/playbook/edge_grammar.py` is not
touched.

Unit 71's arm in `tools/govkit/selftest.py#main` planted into `positional-producers.txt`, which leaves the kit. It
plants into `instructions-legacy.txt`, the other `project-owned` list that `tools/playbook/instruction_units.py`
reads with `#` lines skipped. That list holds no tab row, so the record-row arm cannot trip, and no adopter name at
base. The flip deletes `, "instructions-legacy.txt"` from the include. The three `[dOC-71 S3]` labels stay, and the
named path in `_named` follows the file.

### Every remaining kit-path spelling

The ban's remedy is to derive the path from the file's own location. The playbook kit already has that seam:
`tools/playbook/instruction_units.py#derive_tool_rel` and `tools/playbook/instruction_units.py#derive_kit_rel`,
which drop the tool-root segment at a root install. A fixture lays its tree out at the install's own layout, as
`tools/playbook/instructions_edit.py` and the lexicon and govkit selftests already do.

| File | Sites | Derivation |
|---|---|---|
| `tools/playbook/core.py` | `derive_layout`'s fixture branch, `write_fixture`, `Case.write_legs`, `run_practice_read`, `arm_registry`, `arm_unenforced`, `arm_pending`, `arm_kinds`, `arm_practice`, `arm_instruction_unit`, `arm_bypass_never` | `tools/playbook/core.py#derive_layout` with a root returns that root beside the kit path and tool root the live branch derives. `Case` carries both, and every plant spells a kit file as the kit path joined to its name and the legs file under the tool root |
| `tools/playbook/gov_tag.py` | `FIXTURE_KIT`'s value, `SHAPE_PLANTS`, `build_tags_fixture`, `run_plant`, `run_positional_plant` | `FIXTURE_KIT` takes `instruction_units.derive_tool_rel(KIT_DIR.name)`, and every other kit spelling in the fixture reads `FIXTURE_KIT`. The notes file and the role file go through `derive_tool_rel` too. The `pending-source` plant spells its purpose-source `{prefix}/playbook/readers.toml#why` |
| `tools/playbook/instruction_units.py` | `LADDER_SOURCES`, `arm_tags`, `arm_priority`, `STATEMENT_ROWS`, `arm_extractor` | `LADDER_SOURCES` spells the tool root `{prefix}/`, resolved in `run_ladder_terms` against `derive_kit_prefix()`. The plants use `derive_kit_rel` and `derive_tool_rel`. The pointer row's command reads `bash {prefix}/push-main.sh`, still a command by its whitespace |
| `tools/playbook/positional.py` | `PRODUCER_PATHSPECS`, `SELFTEST_ROWS` | the positional-module section above |
| `tools/playbook/adopt-playbook.sh` | two rows of the tag resolver's `PLANTS` | the `pending-source` rows expect `pending reader · {prefix}/playbook/readers.toml#why` and `/readers.toml) lacks why`. The second keeps the field and the file, and drops the kit directory the fixture derives |
| `tools/playbook/namespaces.toml` | the six `source` and six `purpose-source` spellings | `{prefix}/playbook/<file>`, and `{prefix}/govkit/registry.toml` for the `kit` row |
| `tools/lexicon/selftest.py` | the `--tags` fixture | `tools/lexicon/lexicon.py` gains `PLAYBOOK_HOME = "playbook"`, which `read_tag_words` passes to its resolver. The selftest joins the copy's tool root to `lex.PLAYBOOK_HOME`, and so does its expected line |
| `tools/run-gates/py_reads.py` | `run_selftest`'s scratch tool root | the scratch root is named `HERE.parent.name`, and the two expected gap paths open with that name |
| `tools/memory-tree/gotchas.py` | `cmd_selftest`'s kit copy | the copy sits at the last two segments of its own location under the scratch tree |

The `purpose-source` reader resolves `{prefix}/` once, at the head of each row's read in
`tools/playbook/tag_index.py#check_namespace_purpose`. The tool root is the parent of `ctx["kit"]`, the registry's
own directory. A row whose resolved path matches what the old literal named grades exactly as before. Without the
resolution every row spelled through the token would print `pending` and its members would go ungraded. The
`pending-source` plant reads that case: its second half lands `readers.toml` and expects a red.

### The 19th drift offender

The `kind` row's `purpose-source` named
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md`. Its sibling rows name the file
their members are declared in. The kinds register is `tools/playbook/kinds.toml`, and its rows carry no purpose
field, so the row names that file path-only, as the `kit` row names its registry. The comment in
`tools/playbook/principles.toml` names the design record by path. It says instead that the rows were written from
the design record `.memory-tree.conf`'s `DESIGN_RECORD` names, sections `[principles]` and `[enforcement]`. That
keeps one fact in one place, and the id leaves product source.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_memory_root` | Python function | `py.function`, graded OK by `lexicon.py --suggest` at base |
| `PLAYBOOK_HOME` | Python module constant | none: no `py.constant` cell is declared |
| an inline `resolve_prefix_token` block in `tools/playbook/tag_index.py` | canonical copy | the existing `py.function` name |

### Migration

N/A — the lists and the write mode exist on this branch only. `origin/main` holds no `tools/playbook/positional.py`
and no `write_empty_lists`, so no adopter holds a list at the old path.

### Rollout

Live at landing, in one pass. The move, the readers and the whitelist land together, or the positional arm reads the
list absent, or the project-registry whitelist refuses it.

### Files touched (estimate)

- `memory/project/positional-refs.txt`, `memory/project/positional-producers.txt`: S1, moved
- `tools/playbook/positional-refs.txt`, `tools/playbook/positional-producers.txt`: S1, the old paths
- `tools/playbook/positional.py`: S2, S5, S6
- `tools/playbook/gov_tag.py`, `tools/playbook/render_playbook.py`, `tools/govkit/selftest.py`: S3, S6
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/HYGIENE.template.md`, `memory/HYGIENE.md`,
  `.memory-tree.conf`: S4
- `tools/playbook/kit.toml`, `tools/playbook/README.md`, `tools/playbook/aliases.toml`, `help/tags.md`: S5
- `tools/playbook/core.py`, `tools/playbook/instruction_units.py`, `tools/playbook/adopt-playbook.sh`: S6
- `tools/playbook/namespaces.toml`, `tools/playbook/tag_index.py`: S7
- `tools/playbook/principles.toml`: S8
- `tools/lexicon/lexicon.py`, `tools/lexicon/selftest.py`, `tools/run-gates/py_reads.py`,
  `tools/memory-tree/gotchas.py`: S9
- `memory/LIVE.md`: S10, re-rendered and never hand-edited

### Alternatives rejected

- **Both lists in `PROJECT_REGISTRY_EXTRA`, as the brief proposed.** The write mode writes `positional-refs.txt`
  into every target's memory project folder, so each adopter carrying memory-tree would red the project-registry
  whitelist on the first render until it declared the file itself. TOOL-bQuiltedLantern-3 refuses that shape by
  name.
- **A home outside the memory tree, such as a repo-root dotfile.** The measurement above shows the memory home
  passes, and `memory/project/` is where this repo's own registries already live.
- **Moving the list and keeping the kit path in `tools/playbook/positional.py#read_git_grep`'s exclusion.** The
  scan would then read the list's own 38,778 rows as citations, and the arm would red on every one.
- **A fixture tree at a fixed non-kit layout.** It clears the ban too. The in-kit precedent,
  `tools/playbook/instruction_units.py#derive_tool_rel`, and the lexicon and govkit selftests lay fixtures out at
  the install's layout, and one convention per kit is the cheaper one to read.
- **Resolving `{kit}/` as well as `{prefix}/` in `purpose-source`.** The playbook kit is always homed at
  `{prefix}/playbook/`, and the `kit` row names a sibling kit, so one token covers every row.

## 5. Production-readiness checklist

- security: N/A — no write boundary moves. The ban this unit drains stops gov's record citations reaching any
  target.
- perf / scale: the ban, the dead-path walk and the drift harvest each stop reading 4.4 MB. The positional arm reads
  the same list from a new path.
- error / empty / loading states: an absent positional list still reds, and the write mode still writes it empty
  where the check looks. An absent producer list still reads as nothing kept.
- observability: the positional arm's messages name the list's tree path, so a red points at the right file.
- risks: a reader left on the old path reads the list absent and reds by name, never silently. The `{prefix}/`
  resolution is the one silent risk, and the `pending-source` plant reds on it.
- testing: AC1 to AC11, and the two arms the gates section declares.
- migration: N/A — branch-only files, as the Design section says.
- user docs: `help/tags.md` names the list's new home.

## 6. Acceptance criteria

- **AC1** — When `git ls-files -- tools/playbook` runs, no line names a file opening `positional-`, and
  `git grep -n positional -- tools/playbook/kit.toml` prints no `include` row.
  Red when: a list or its include stays in the kit, so the ban and the dead-path walk still read it.
- **AC2** — When `python tools/playbook/positional.py check` runs over the tree, it exits 0 and its summary line
  reports `0 unlisted` and `0 stale`, with the same file:line and section row counts as the same command at base.
  Red when: the grep exclusion still names the kit path, so the list's rows read as unlisted citations, or the path
  function still looks beside the module, so the arm reads the list absent.
  figure: the base counts are DERIVED by running the command in a scratch worktree of `93c4e987e`.
- **AC3** — When `bash tools/check-install-prefix.sh` runs, it prints `install-prefix: clean`.
  Red when: one kit path stays spelled as a literal anywhere under the tool root.
  figure: 18,847 spellings on 18,814 lines at base, PINNED from the bar's log at `93c4e987e`.
  permission: the command is a leg's argv, so the main loop observes it.
- **AC4** — When `python tools/playbook/gov_tag.py check` runs, it exits 0, and its `purpose` line names no
  `pending` namespace that was graded at base. `git grep -nE 'tools/|memory/builds' -- tools/playbook/namespaces.toml`
  prints nothing.
  Red when: `tools/playbook/tag_index.py` does not resolve `{prefix}/`, so a row reads `pending` and its members go
  ungraded.
- **AC5** — When `git grep -n PLAY-dClosedLoop-1 -- tools/playbook/namespaces.toml tools/playbook/principles.toml`
  runs, it prints nothing, and `python tools/drift-audit/drift_report.py --check` prints no `new` row.
  Red when: a record path or id stays in product source, or the list still sits under the drift report's globs.
  figure: 19 `new` rows at base, PINNED from the bar's log.
  permission: the drift command is a leg's argv, so the main loop observes it.
- **AC6** — When `python tools/playbook/gov_tag.py check --base HEAD` runs in a scratch install of the
  playbook-render and memory-tree kits, after `bash tools/playbook/adopt-playbook.sh --target .` there, it prints
  `tags: positional · unarmed` and no `stale` row, and the installed kit directory holds no positional list.
  Red when: the write mode still writes the list under the kit, where the arm no longer looks, so the arm reads it
  absent and reds.
  cost: one scratch install. permission: a role agent's scratch guard refuses this run, so the main loop observes it.
- **AC7** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 3,9,13,14,15,16` runs, it exits 0, and
  `grep '^PROJECT_REGISTRY_EXTRA=' .memory-tree.conf` names `positional-producers.txt` and not `positional-refs.txt`.
  Red when: the project-registry whitelist admits neither name, `memory/LIVE.md` is not re-rendered, or a list row
  counts as a dead path.
- **AC8** — When `bash tools/check-dead-paths.sh` runs, it exits 0, and
  `bash tools/memory-tree/check-method-carriers.sh` names no file opening `positional-`.
  Red when: the list still sits outside the memory tree.
  figure: 5 dead-path rows at base, all in the list, PINNED from the bar's log.
  permission: both commands are legs' argv, so the main loop observes them.
- **AC9** — When `python tools/playbook/positional.py --selftest`, `python tools/playbook/core.py fixture`,
  `python tools/playbook/instruction_units.py fixture`, `python tools/memory-tree/gotchas.py --selftest`,
  `python tools/run-gates/py_reads.py --selftest` and `bash tools/playbook/adopt-playbook.sh --selftest` each run,
  each exits 0, and `printf 'layer.memory\n' | python tools/lexicon/lexicon.py --tags` exits 0.
  Red when: a derived fixture path disagrees with the line a plant expects, or the lexicon's resolver and its
  fixture name different homes.
  cost: a few minutes for the six runs.
- **AC10** — When `grep -c positional-producers tools/govkit/selftest.py` runs, it prints `0`, and the moved arm is
  observed RED with unit 71's role filter reverted and GREEN with it, as the gates section declares.
  Red when: the arm still plants into a list that left the kit, or passes with the ban reading `project-owned` rows.
- **AC11** — When `git grep -nE 'playbook/positional-|refs.txt beside' -- help tools/playbook` runs, it prints
  nothing, and `grep -c 'project/positional-' help/tags.md` prints at least `1`.
  Red when: a page or comment still places a list beside the module, or the help page names no new home.

## 7. Gates

`install-prefix (shipped surface)` · `dead-path carriers (deleted files still named)` · `drift-audit records` · `method carriers (every pointer declared)` · `memory hygiene` · `memory-hygiene self-test` · `tags (the resolver's checks)` · `tags positional selftest` · `tags bundle selftest` · `core selftest` · `instruction units selftest` · `instruction ladder (level is the one term)` · `instruction edits selftest` · `playbook render wiring` · `playbook render selftest` · `govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `govkit selfcheck` · `policy fixtures` · `lexicon selftest` · `lexicon naming predicates` · `codebase-map kit selftest` · `drift-audit selftest` · `gotchas selftest` · `python reads (a name never bound, an import outside its guard)` · `python resolver (behaviour + inline parity + idiom ban)` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `recall floor` · `recall floor arms`

The first five are the legs this unit turns or moves. The guards join owes the rest of the Files-touched paths:
`{prefix}/playbook/` for the matrix and the render selftest, `{prefix}/govkit/` and the two exact-path guards of
`policy fixtures`, `{prefix}/lexicon/lexicon.py` for three selftests, `memory/HYGIENE.md` for the parity leg,
`.memory-tree.conf` for two arm legs, and `memory/` for the recall legs. `{prefix}/`, `{prefix}/memory-tree/`,
`{prefix}/run-gates/` and `{prefix}/lib/` are broad under `BROAD_LEG_FLOOR` 5 and excluded. The others run the code
this unit moves, the parity leg grading the new inline block among them.

New arm: tools/govkit/selftest.py · covers AC10 · unit 71's plant moved from the producer list to `instructions-legacy.txt`, red with that unit's role filter reverted · none
New arm: tools/playbook/adopt-playbook.sh · covers AC4 · the `pending-source` plant's purpose-source spelled through `{prefix}/`, red with the token read in `check_namespace_purpose` reverted · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-08 · initial draft, by `2026-11-08-prompt-PLAY-dOrderedCharter-72-repair-brief`, every line read
  at `93c4e987e`. The memory home was measured in a scratch clone. TOOL-bQuiltedLantern-3 placed
  `positional-refs.txt` in the hygiene engine's project-registry whitelist rather than gov's
  `PROJECT_REGISTRY_EXTRA`, as the Alternatives record.
- rev-2 · 2026-11-08 · S3 · section 4 · the unit 72 builder handed the spec back before writing, at `6eaaecd80`:
  `FIXTURE_KIT` has 18 readers, two in `tools/playbook/edge_grammar.py`, which neither unit touches. It keeps its
  name and readers and takes a derived value; S3's retirement and its Readers clause are gone. Every other symbol
  the scope changes was re-grepped at `6eaaecd80`, and each caller sits in a file this unit touches.

## 10. Reuse audit

The seams are named in the Design section and none is new. The list path reuses the memory-root read the module
already makes in `tools/playbook/positional.py#run_check`. The tool-root token is the canonical
`resolve_prefix_token`, which `reuse_lookup.py` ranked a seam at fan-in 11 and 13 installs, inlined under its gated
marker. The fixture layout reuses `tools/playbook/instruction_units.py#derive_tool_rel`, which
`tools/playbook/instructions_edit.py` already uses for fixtures. The whitelist case reuses the project-registry
whitelist's named-case arm, whose rule the recall query returned as TOOL-bQuiltedLantern-3. No new mechanism is
minted.

Recall terms used: `python tools/memory-recall/query.py "a gov-only registry list moved out of a shipped kit into the memory project folder" --terms "positional-refs memory/project PROJECT_REGISTRY_EXTRA project-owned withheld kit registry whitelist check 3 named case install-prefix"`, and `python tools/codebase-map/reuse_lookup.py "resolve the prefix token against the tool root, a fixture laid out at the install's own layout"`
