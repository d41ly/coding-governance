# TOOL-aOrientedCast-2 — the handoff renderer: a role's constant block and a task block rendered from the card, the brief and the unit, into one prompt file

**Status:** OPEN · rev-1 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md) | journal | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 |

<!-- /gen:spec-records -->

## 1. Goal

A role file says who an agent is; nothing yet turns it, plus what one task needs, into the prompt
the agent is handed. This unit builds `python tools/roles/handoff.py`: `render` composes a role's
rendered block with a task block holding exactly the inputs that role declares, read from the
session's card, the build's brief, the governing doc and the caller's arguments, and writes one
hashed prompt file under the build's `prompts/` folder; `check` re-derives the two hashes; and
`harness-args` prints the `roles` object a harness takes. A required input that resolves to nothing
refuses by name, so an agent is never handed a prompt with a hole in it.

## 2. Scope (IN)

- **S1** — `render` composes the file of the build's interface 7 byte for byte, in the layout §4
  "The prompt file" pins: the binding line, the H1, the marker, `## Role` holding the role as the
  catalogue's library renders it, and `## Task` holding one block per declared input in declared
  order, then one block per charter id. Observed by AC1 and AC2.
- **S2** — Each `reads` key is gathered from its source as §4 "Sources" states: `task:` and `card:`
  keys from the card, `brief:` keys from the build's brief record, `input:` keys from `--input`, and
  charter ids from the governing doc. Observed by AC1, AC9, AC10 and AC11.
- **S3** — A required key that resolves to nothing, an empty value or a placeholder exits 1 naming the
  key and its source, and writes nothing. A missing optional key is named on one line of `## Task`.
  Observed by AC5 and AC6.
- **S4** — The card defaults to the session's own, found by calling the kickoff checker's
  `--card --path` verb with the session id `CLAUDE_CODE_SESSION_ID` carries; the renderer never
  re-derives the card's location (§8 F1). Observed by AC6.
- **S5** — `role-sha` and `task-sha` are the first 12 lowercase hex digits of the SHA-256 of each
  section's bytes, LF-normalized, as §4 "The two hashes" defines; `check <file>` re-derives both and
  compares the marker's `path` with the file's own. Observed by AC3 and AC4.
- **S6** — `--part task` prints the marker line, a blank line and the `## Task` section, which is
  what a native-typed spawn passes as its prompt; `--stdout` prints instead of writing. Observed by
  AC7.
- **S7** — `harness-args <harness>` prints, as one line of JSON with sorted keys, the union of the
  `stages` tables of every workflow whose harness is that script. Observed by AC8.
- **S8** — The file is named `<date>-prompt-<id>-<n>-<role without gov->.md`, `<n>` one above the
  highest already used for that date and id. Observed by AC2.
- **S9** — The kit README gains the renderer's section, the roles dossier's prose names the renderer,
  and `memory/map/generated/symbols.json` is regenerated. NOT OBSERVED by a criterion: the
  `roles catalogue` and `codebase-map coverage + freshness` legs grade these at the close.

## 3. Non-goals (OUT)

- Spawning anything. The renderer writes and prints files; harnesses and the main loop spawn.
- The hooks. The write gate and the spawn guard are `TOOL-aOrientedCast-6` and
  `TOOL-aOrientedCast-7`; this unit gives the second its marker and its `check` verb and enforces
  nothing itself.
- Rendering agent types under `.claude/agents/` (`TOOL-aOrientedCast-3`).
- Composing a harness's own per-agent prompts. A harness writes its stage protocol; a role reaches a
  harness agent as its agent type's system prompt, never through this file.
- Grading whether a card field says something true. The renderer applies `KICK-aOrientedCast-1`'s
  presence and placeholder grammar and copies the value verbatim.
- Deriving a unit's spec path from its id. `input:spec` comes from `--input spec=` alone.
- A staleness check of a rendered role against the current catalogue. `check` re-derives the hashes
  of the file's own bytes and nothing more.
- Adapters for tools other than Claude Code, beyond the file itself, which any tool can read.

### Edges

- **consumes-from** `TOOL-aOrientedCast-1` — the library's role loader, role composition, conf
  reader, charter locator and section reader, workflow loader and inline kit resolver, and the
  workflow table's `stages` tables. Without them there is no role to render and no stage map.
- **consumes-from** `KICK-aOrientedCast-1` — the eight task labels and the field grammar, placeholder
  rule included, by which every `task:` key is read.
- **hands-off** `TOOL-aOrientedCast-4` — the harness-arguments output for the two build harnesses,
  which that unit's caller passes as the harness's roles argument.
- **hands-off** `TOOL-aOrientedCast-5` — the harness-arguments output for the review harness.
- **hands-off** `TOOL-aOrientedCast-7` — the marker grammar, the two hash definitions and the check
  verb, against which the spawn guard verifies an agent call's prompt.
- **hands-off** `KICK-aOrientedCast-2` — the render and harness-arguments verbs the attended router
  composes every agent prompt and every harness call from.

## 4. Design

### Evidence

Read at `646d4a73` on 2026-10-11.

- `--card --path` resolves the card under the git common dir from a session id given by
  `--session` and prints its path, before any manifest resolves, exit 0
  (`skills/session-kickoff/manifest-check.sh:284-293`). It refuses a session id carrying a separator
  or `..` (`:268-282`).
- `CLAUDE_CODE_SESSION_ID` is set in every shell Claude Code starts. Measured on node `a` on
  2026-10-11, CLI 2.1.293, from inside an agent this run's Workflow spawned: its value equals the
  session id the orientation card is named by. The runlog kit already reads it
  (`tools/runlog/README.md:22`). PINNED at that CLI.
- The kickoff checker is homed under `skills/` in this repository and at the install prefix in an
  adopter, where the receipt records it (`tools/govkit/entries/kickoff-manifest.kit.toml:4-10`). The
  canonical kit resolver reads the receipt, then probes beside the caller
  (`tools/lib/resolve_kit_dir.py:14-44`); the shell resolver adds a last rung, the one tracked file
  carrying that name, because no probe walks to `skills/` and gov keeps no receipt
  (`skills/session-kickoff/manifest-check.sh:797-808`).
- The brief record's shape is the kickoff checker's `BRIEF_SKELETON`: `## The prompt`, then
  `## The brief` with `### Goal`, `### Items`, `### Acceptance`, `### Gates`, `### Non-goals`,
  `### Limitations` and `### Reuse` (`skills/session-kickoff/manifest-check.sh:94-142`). Measured on
  2026-10-11: 26 records under a build's `prompts/` carry `## The prompt`; one carries `## The brief`
  as well, this build's own; the other 25 are run mandates with no brief.
- A prompt record is named by check 5's grammar, `<date>-<kind>[-<FAMILY>]-<slug>-<seq>[-<unit-tail>].md`
  (`memory/HYGIENE.md:187-192`), and is bound by its `**Serves:**` line (`memory/HYGIENE.md:541-548`).
  `<id>-<n>-<role>` reads as the id's seq followed by a unit tail.
- The id-defining H1 is the first unfenced H1 whose first token is an id
  (`tools/memory-tree/tree_lib.py:203-225`), so an H1 opening with a role name defines nothing.

### The prompt file

```text
**Serves:** journal <id>

# <role> handoff — <id>

<!-- gov:handoff role=<role> build=<slug> unit=<id|-> path=<repo-relative path> role-sha=<12 hex> task-sha=<12 hex> -->

## Role

<the role, as the catalogue's library renders it with this tree's memory root>

## Task

This handoff is for build `<slug>`, unit `<id>`.
Not supplied, optional: `<key>`, `<key>`.

### <reads key, without its ?>

<value, verbatim>

### charter §<n>

<that section's body, verbatim>
```

- `<id>` is `--unit`; without it, the first id of the build README's front-matter `ids:` line. With
  neither, render refuses. Without `--unit` the opening sentence reads `This handoff is for build
  <slug>, and names no single unit.` and the marker carries `unit=-`.
- The `Not supplied` line is present only when an optional key resolved to nothing.
- Blocks follow the role's `reads` order, then its `charter` order. One blank line separates every
  block; the file ends with exactly one LF and is written with LF line endings.
- Nothing time-varying is in the bytes, so a render repeated over the same inputs is byte-identical;
  the date is in the file name only.

### The two hashes

- `## Role` is the first line exactly `## Role` after the marker; `## Task` the first line exactly
  `## Task` after it. The role section runs from the first byte of its heading line to the byte
  before the `## Task` line; the task section from the first byte of its heading line to the end.
- Each section's bytes have CRLF folded to LF before hashing, and nothing else is normalized. The
  writer ends the file with exactly one LF, so the task section ends with one. A CRLF working copy
  therefore hashes like its blob, and a blank line added after rendering is an edit `check` refuses.
  This is the span and the fold `TOOL-aOrientedCast-7` hashes: the `## Task` line through the end of
  the file, LF-folded.
- The catalogue's checker refuses a `## ` line in a role body or an overlay, so a role section cannot
  contain a line that ends it early; the role's own `## House rules` heading sits inside it.
- `check <file>` reads the one marker line, recomputes both hashes, compares each, and compares the
  marker's `path` with the file's repo-relative path. It prints one line naming each mismatch and
  exits 1, or prints the path and both hashes and exits 0.

### Sources

| Key | Source | Resolves to nothing when |
|---|---|---|
| `task:<field>` | the card's `## task` field with the label the build's interface 6 maps the field to, read by `KICK-aOrientedCast-1`'s grammar; the value keeps its line breaks | no card, the field absent or repeated, or its value empty or a placeholder |
| `card:<heading>` | the lines under the card's last `## <heading>`, up to the next `## ` heading or READY line, verbatim, blank edges trimmed | no card, no such section, or nothing under it |
| `brief:<sub-head>` | the brief record's `### <Sub-head>` under `## The brief`, matched ignoring case, up to the next `###` or `##` heading | no record, or the sub-head absent or empty |
| `input:<name>` | `--input <name>=<value>`; `spec` and `prompt` are paths that must name a file inside the repository and are written repo-relative | the argument is absent |
| charter `§<n>` | the governing doc's section, through the catalogue library's locator and reader | never, once the catalogue's checker is green; a miss refuses |

The card is `--card <path>` when given. Otherwise the renderer resolves the kickoff checker, through
the library's inline kit resolver for the home `session-kickoff` and the file `manifest-check.sh`,
then the one tracked file of that name, and runs it as
`bash <checker> --card --path --session <CLAUDE_CODE_SESSION_ID>` with stdin closed and a 30-second
bound. An unset variable, an unresolvable checker or a printed path naming no file leaves the card
absent, and the refusal or the `Not supplied` line names which.

The brief record is `--input prompt=<path>` when given. Otherwise it is the one file under
`<MEMORY_ROOT>/builds/<slug>/prompts/` carrying both a `## The prompt` line and a `## The brief`
line. Two or more such files refuse, naming them and `--input prompt=`.

`MEMORY_ROOT` is read from `.memory-tree.conf` by the library's conf reader, the hooks kit's grammar.
An absent conf or key exits 2.

### The command line

```text
python tools/roles/handoff.py render --role <name> --build <slug> [--unit <id>] [--card <path>]
                                     [--input <key>=<value>]... [--out <path> | --stdout] [--part full|task]
python tools/roles/handoff.py harness-args <harness>
python tools/roles/handoff.py check <file>
```

- `render` writes the file and prints its repo-relative path. With `--part task` it prints the marker
  line, a blank line and the `## Task` section instead of the path. With `--stdout` it writes nothing
  and prints the whole file, or that part. The marker's `path` is the path the file has or would
  have. Everything printed is written to standard output as UTF-8 bytes with LF line endings, so a
  Windows console adds no carriage return.
- `--input` names one of `spec`, `diff`, `question` and `prompt`. A name outside those, or one the role
  does not read, exits 2, except `prompt`, which is always accepted because it also names the brief
  record. `diff` is one line; `question` is free text.
- `--unit` must read `<FAMILY>-<slug>-<digits>` with the slug equal to `--build`, else exit 2. The
  build folder must exist, else exit 1. An unknown role exits 1 naming the catalogue's slots.
- A relative path given to `--card`, `--out` or an `--input` is read from the repository root.
- `--out` names a path under the build's `prompts/` folder and may overwrite; a path elsewhere exits
  2, because the spawn guard admits a marker only under that folder. The derived path never
  collides, because its `<n>` is one above the highest already used for that date and id.
- `harness-args` takes the harness's script name without its extension: `unattended-build`,
  `unattended-unit` or `tier2-review`. It unions the `stages` tables of every workflow whose harness
  path ends in that script. A stage key mapped to two different roles across those workflows exits 1;
  a name no workflow's harness carries exits 1. It prints `{}` for a harness whose workflows declare
  no stage.
- Exit 0 on success, 1 on a refusal naming its key, file or role, 2 on usage or an unarmed
  environment: no repository, no `MEMORY_ROOT`, no `CHARTER`.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `handoff.py` with verbs `render`, `harness-args`, `check` | CLI | none: a file and its verbs |
| `RolesError` | Python type, reused | minted by `TOOL-aOrientedCast-1`; the renderer raises it and mints no type of its own |
| `render_handoff`, `resolve_card_path`, `resolve_kickoff_checker`, `resolve_brief_record`, `extract_task_fields`, `extract_card_section`, `extract_brief_section`, `derive_prompt_name`, `derive_section_sha`, `check_handoff`, `print_harness_args`, `main` | functions | `py.function`; `--suggest <name> --as py.function` answered OK for each |
| `gov:handoff` | marker head | none: the build's interface 7 |
| `## Role`, `## Task`, `### charter §<n>` | file headings | none: the build's interface 7 |

### Files touched (estimate)

`tools/roles/handoff.py` · `tools/roles/README.md` · `memory/map/features/roles.md` · `memory/map/generated/symbols.json`

### Rollout

- Inert until a caller runs it. No hook reads its files until `TOOL-aOrientedCast-7`.
- Its first live callers are `KICK-aOrientedCast-2`'s router and, for the harness map, the callers of
  `TOOL-aOrientedCast-4` and `TOOL-aOrientedCast-5`.
- A rendered file under `prompts/` is a record bound by its `**Serves:**` line; it is committed with
  or after the spec of the unit it names, never before, or check 21 counts it unbound.
- The pass runs `gen_map.py --write` before its commit, because new functions stale `symbols.json`.

### Alternatives rejected

- **The card located by joining the common dir and the session id here.** That is the location rule
  the kickoff checker owns, spelled twice (§8 F1).
- **Reading the card through the hooks kit's reader.** It is JavaScript inside a hook script, reached
  only by feeding the hook a crafted payload.
- **The brief record found by file name.** Names vary by kind and tail; the two headings are what
  makes a record a brief, and the measured corpus has one per build at most.
- **Hashing the whole file.** The marker sits in the file, so a whole-file hash would contain itself;
  the spawn guard needs the task section's hash alone, because a native-typed spawn carries only it.
- **Ignoring an `--input` the role does not read.** A caller routing the wrong input to a role would
  get a prompt without it and no word; refusing names the mismatch.
- **A JSON or YAML prompt file.** Every tool reads Markdown, and the file is read by agents first.

## 5. Production-readiness checklist

- security — the renderer writes only under the build's `prompts/` folder; `spec` and `prompt`
  inputs are refused outside the repository. The session id is passed to the
  kickoff checker as an argument, and the checker refuses a separator or `..`. A rendered file
  carries card and brief text verbatim, so a secret in either reaches the agent and the committed
  record; the charter's §5 rule that secrets never enter memory is the guard.
- perf / scale — at most three spawns: the git toplevel, the git listing when the receipt and the
  probes miss the checker, and the checker itself. The charter sections dominate the file's size.
- error / empty / loading states — every refusal names the key and the source that came back empty;
  nothing is written on a refusal; an optional key's absence is said in the file.
- observability — `render` prints the path it wrote; `check` prints both hashes; `harness-args`
  prints exactly what the harness will receive.
- risks — the card default rests on `CLAUDE_CODE_SESSION_ID`, measured on one CLI; without it the
  renderer needs `--card`. The task grammar is implemented twice, in the kickoff checker's shell and
  here; AC10 renders values from a card that checker accepted, which is the cross-check.
- testing — every criterion observed on a fixture build in a local clone, RED on a staged break
  where it names one; no suite file is added.
- migration — none: a new script.
- user docs — the kit README's renderer section.

## 6. Acceptance criteria

The fixture is a `git clone --local` of the pass's HEAD at `%TEMP%/t2c`, holding a fixture build
folder for the slug `zFixtureCast`: a README whose front matter names `ids: TOOL-zFixtureCast-1`, a
spec whose H1 carries that id, a brief record in the kickoff checker's brief shape under its
`prompts/`, and a card file holding a `## task` section with all eight fields filled, a `## route`
section and a READY line. Every command below runs in the clone's root, and `handoff.py` in a
bullet stands for the script this unit adds, `python tools/roles/handoff.py`.

- **AC1** — When `handoff.py render --role gov-builder --build zFixtureCast --unit TOOL-zFixtureCast-1 --card <card> --input spec=<spec> --stdout`
  runs twice, both outputs are byte-identical under `cmp`; line 1 reads
  `**Serves:** journal TOOL-zFixtureCast-1`, the marker line names `role=gov-builder` and
  `unit=TOOL-zFixtureCast-1`, and `## Task` holds `### input:spec`, `### card:route` and
  `### brief:non-goals` in that order, then one `### charter` block per id of the role's `charter`.
  Red when: two renders differ, or a block is missing or out of declared order.
- **AC2** — When that render runs without `--stdout`, it prints a path under the fixture build's
  `prompts/` ending `-prompt-TOOL-zFixtureCast-1-1-builder.md`; a second render prints the same path
  with `-2-builder.md`; and `handoff.py check <path>` exits 0 for each.
  Red when: a render overwrites the first file, or `check` refuses a file render wrote.
- **AC3** — When one byte inside the `## Task` section of a rendered file is edited, `check` exits 1
  naming `task-sha`; when one byte inside `## Role` is edited instead, it names `role-sha`; when an
  unedited file is copied under another name, it names the marker's `path`.
  Red when: an edited or relocated file passes.
- **AC4** — When a rendered file is rewritten in place with CRLF line endings by
  `python -c "import sys; p = sys.argv[1]; b = open(p, 'rb').read(); open(p, 'wb').write(b.replace(b'\n', b'\r\n'))" <path>`,
  `check` exits 0 and prints the same two hashes it printed before.
  Red when: line endings move a hash.
- **AC5** — When `handoff.py render --role gov-spec-writer --build zFixtureCast --unit TOOL-zFixtureCast-1 --stdout`
  runs after the fixture's brief record is moved out of `prompts/`, it exits 1 naming `brief:goal` and
  the folder it searched, and the `prompts/` listing is unchanged; with a second record carrying both
  brief headings added instead, it exits 1 naming both files and `--input prompt=`.
  Red when: a role is rendered with a required brief key missing, or an ambiguous brief is resolved by
  guess.
- **AC6** — When `handoff.py render --role gov-session --build zFixtureCast --input question=handover --stdout`
  runs with `CLAUDE_CODE_SESSION_ID` unset and no `--card`, it exits 0 and its `## Task` carries one
  `Not supplied, optional:` line naming `task:todo` and `card:route`; when the variable names a session
  whose card `bash skills/session-kickoff/manifest-check.sh --card --write --session t2fx` wrote and
  `--card --append` filled, the output carries `### task:todo` and `### card:route` from that card.
  Red when: an absent optional key is dropped without the line, or the default card is not the one the
  kickoff checker's `--card --path` prints.
- **AC7** — When the AC1 render runs with `--part task --stdout`, the output equals the marker line,
  a blank line, and the file's `## Task` section byte for byte, and
  `python -c "import hashlib, sys; t = sys.stdin.read(); print(hashlib.sha256(t[t.index('## Task'):].encode()).hexdigest()[:12])"`
  over that output prints the marker's `task-sha`.
  Red when: the task part carries other bytes, or its hash disagrees with the marker.
- **AC8** — When `handoff.py harness-args tier2-review` runs, it prints
  `{"diffFinder":"gov-diff-reviewer","skeptic":"gov-skeptic","specFinder":"gov-spec-reviewer","synthesis":"gov-synthesizer"}`;
  `unattended-build` prints `{"disposal":"gov-spec-writer","specWriter":"gov-spec-writer"}`;
  `unattended-unit` prints `{"builder":"gov-builder"}`; and `nope` exits 1. With the fixture's
  `spec-review` entry mapping `skeptic` to `gov-synthesizer`, `tier2-review` exits 1 naming `skeptic`.
  Red when: a mapping differs from the workflow table, or a conflict is resolved silently.
  figure: the printed objects are DERIVED from the workflow table at observation time; the strings
  above are its contents as `TOOL-aOrientedCast-1` specifies them.
- **AC9** — When the AC1 output's `### charter §11` block is compared by `python -c` with the §11 body
  the catalogue library's `extract_charter_sections` reads from `AGENTS.md`, they are equal; when the
  clone's `.memory-tree.conf` has its `CHARTER` line deleted, render exits 2 naming `CHARTER`.
  Red when: a charter block differs from its section, or a render without a declared charter proceeds.
- **AC10** — When the fixture card's `## task` is the body `KICK-aOrientedCast-1`'s AC2 appended, the
  gov-session render's `### task:todo` block holds that body's To-do value without its qualifier; when
  the To-do value is `…`, the block is absent and `task:todo` is named on the `Not supplied` line; and
  when the clone's gov-session role is edited to read `task:todo` without `?`, render exits 1 naming
  `task:todo` and the card path.
  Red when: a qualifier leaks into a value, or a placeholder is rendered as a value.
- **AC11** — When render runs for gov-builder with `--input foo=x`, it exits 2 naming `foo`; with
  `--input diff=a..b`, it exits 2 naming `input:diff` as a key gov-builder does not read; with
  `--input spec=` naming a path outside the repository, it exits 1 naming the path; with
  `--unit TOOL-zOtherCast-1`, it exits 2 naming the slug mismatch.
  Red when: an unknown, unread or out-of-tree input is accepted.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `remote literals (kit code names no remote)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

The renderer adds no leg and no suite: every criterion is a direct observation of the fixture, and
the close's bar grades the script through the legs above and through `roles catalogue`, the leg
`TOOL-aOrientedCast-1` adds, which re-renders the README region this unit's prose sits beside.

## 8. Open questions

- **F1 — How does render find the session's card when no `--card` is given?** The card's location is
  the kickoff checker's rule.
  (a) Call `--card --path --session` with the session id `CLAUDE_CODE_SESSION_ID` carries, the checker
  resolved through the receipt, the probes, then the one tracked file of that name. One spawn, and the
  rule stays in the checker.
  (b) Call the hooks kit's card reader. It is JavaScript in a hook script and answers a crafted hook
  payload, not a command line.
  (c) Require `--card` on every call. Correct, and it moves the location rule into every caller.
  Recommendation: (a), with (c)'s flag kept as the override and as the only route when the variable is
  unset.
  RESOLVED (agent, 2026-10-11, delegated): (a). It is the one option that keeps the location rule in
  one file and still needs no flag in a live session.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` over "compose an agent prompt file from a role block and task
inputs read from the session card, the build brief and a governing doc section, and hash both parts"
ranked only generic readers and builders, `read_text`, `read_conf` and `build_fixture` among them, and
no renderer: no existing seam fits the composition, which is new. The orientation probe of this build
had already run the same question and named the review harness's `renderPromptLine` and the kickoff
checker's `add_card_body`, neither of which composes a file. What this unit extends rather than
re-implements: the kickoff checker's `--card --path` verb for the card's location, its
`BRIEF_SKELETON` shape for the brief's headings, `KICK-aOrientedCast-1`'s field grammar for task
values, and the catalogue library of `TOOL-aOrientedCast-1` for the role, the conf, the charter and
the kit resolver. The brief selector was measured, not assumed: 26 prompt records carry
`## The prompt`, one carries `## The brief` too, and the 25 run mandates without a brief are the
near-misses the two-heading predicate leaves out.

Recall terms used: `SubagentStart route context card brief prompt record Serves journal handoff
session id orientation card path hash` — which surfaced `KICK-aReplayedCard-1` and
`TOOL-aGraftedHelix-2` (the card's location and its common-dir home), `TOOL-aGraftedHelix-8`,
`TOOL-aRoutedQuill-4` (the subagent route context and its payload probe), `KICK-aRoutedQuill-1` (the
brief skeleton) and `KICK-aMendedFleet-4`.
