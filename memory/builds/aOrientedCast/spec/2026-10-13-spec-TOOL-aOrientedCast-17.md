# TOOL-aOrientedCast-17 — a role declares when it is mandatory and where its output goes, and the kit prints the charter's roster lines

**Status:** OPEN · rev-1 · 2026-10-13 · node a · Tier-2 · base 646d4a73581393acbf42f33864a9808c96d00a0c · streams tooling · order 17 · ratified 2026-10-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md) | journal | TOOL-aOrientedCast-16 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 PLAY-aOrientedCast-2 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's second addendum makes the roles a generated section of the charter: one line per role,
saying what it does, when it is mandatory to invoke it, and where its output goes. The role files
carry the first fact and lack the other two. This unit adds the two front-matter keys, grades them
in the catalogue checker, and adds the `roster` verb that composes the lines, so the playbook's
placeholder asks the roles kit for them and `roles_lib` stays the one reader of role files.

## 2. Scope (IN)

- **S1** — `FRONT_MATTER_KEYS` (`tools/roles/roles_lib.py:23-24`) and `REQUIRED_ROLE_KEYS`
  (`tools/roles/check_roles.py:66`) gain `mandatory` and `output`. Both are required and non-empty
  on every role, `agent: false` included, so a role missing either, or holding it empty, is R2 by the
  existing loop (`check_roles.py:132-134`). Observed by AC1, AC2 and AC3.
- **S2** — The checker gains R13. A role whose `mandatory` value calls it mandatory, under §4 "The
  two keys", is a defect when the `enforced-by` of the workflow entry its own `workflow` key names
  holds no hook entry and the value carries no `unenforced — <why>` clause. A `{{…}}` token other
  than `{{MEMORY_ROOT}}` in the value is an R13 defect too. Observed by AC2.
- **S3** — The checker gains R14. A role whose `writes` is `spec`, `review`, `product` or `records`
  is a defect when its `output` does not carry that class's folder spelling from §4's
  `WRITE_FOLDERS` table. A `{{…}}` token other than `{{MEMORY_ROOT}}` in `output` is an R14 defect
  on any role. Observed by AC3.
- **S4** — The checker's summary line (`check_roles.py:288-291`) adds two derived counts, the roles
  it read as mandatory and the writer outputs it graded. Observed by AC1.
- **S5** — The ten files under `tools/roles/agents/` carry the `mandatory` and `output` values of
  §4 "The values", and their `description` lines are rewritten to that table's, so every roster line
  fits a one-line rule and the roster fits the charter's byte budget. Observed by AC1 and AC4.
- **S6** — `python tools/roles/handoff.py roster` prints one line per role, as §4 "The roster verb"
  states: the line grammar, the workflow-table order, the 200-character refusal, the empty-catalogue
  refusal, and the exits. It reads `MEMORY_ROOT` and never `CHARTER`. Observed by AC4, AC5 and AC6.
- **S7** — The agent types under `.claude/agents/` are re-rendered with `render_agents.py --write`,
  so each carries its role's new description and neither new key. Observed by AC7.
- **S8** — `tools/roles/adopt-roles.test.sh` gains the roster arm of §4 "The suite arm", and its
  `FLOOR_ASSERTIONS` (`:50`) rises by the assertions that arm adds. Observed by AC5, whose break
  the arm stages at the close.
- **S9** — The prose that describes the catalogue follows: the checker's header lists R13 and R14
  and what they do not check, `handoff.py`'s docstring lists the verb, the kit README gains the
  paragraphs §4 "Documentation" names, and the roles dossier's `decisions` list and prose name this
  unit. NOT OBSERVED by a criterion: prose, read by the closing review against §4.

## 3. Non-goals (OUT)

- No `rules` key, no R4 re-key and no `## Protocols` reader: `TOOL-aOrientedCast-16`'s.
- No placeholder, probe or playbook edit: `TOOL-aOrientedCast-18`'s.
- No template edit, no charter re-render and no `help/roles.md` edit: `PLAY-aOrientedCast-2`'s,
  whose brief row assigns it the help page that describes the new section and both keys.
- No waiver registry for an inline stand-in: `TOOL-aOrientedCast-19`'s.
- No edit to `tools/roles/workflows.toml`. R13 reads its `enforced-by` entries as they are written.
- No check that a hook named in `enforced-by` exists, is wired or refuses anything: wiring is
  `check-wiring.sh`'s, and the hook's own suite grades what it refuses.
- No column for either key in the README's catalogue region: the roster prints both, and a third
  rendering of one fact is one more copy to keep fresh.
- No change to `CLAUDE_KEYS` in `tools/roles/render_agents.py:62`: an agent type carries neither key.
- No house-overlay override of either key: they ride the kit's base file, as `writes` does.
- No roles kit version move. `TOOL-aOrientedCast-19`, order 19, also writes `tools/roles/` and
  carries the set's one move to 1.3 (its AC9), under the rule §4 "Rollout" states.
- No new gate leg.

### Edges

- **consumes-from** `TOOL-aOrientedCast-16` — a catalogue checker and an agent render that read the
  v4.3 charter's tagged section 1 rules; without it R4 reds every role, so AC1's exit 0 and AC7's
  re-render of the new descriptions cannot be observed.
- **hands-off** `TOOL-aOrientedCast-18` — the playbook probe that runs `handoff.py roster` from the
  target's root and substitutes its stdout verbatim as `ROLE_ROSTER`, plus what that probe does when
  the verb fails or the roles kit predates it.
- **hands-off** `PLAY-aOrientedCast-2` — placing the `handoff.py roster` lines in the charter within
  the byte budget that unit derives and re-measures at its build, and the help page's account of
  the `mandatory` and `output` keys and the verb.

## 4. Design

Line numbers were read at `d518b483f`, the run branch's HEAD when this spec was written; the base
`646d4a73` holds no `tools/roles/`. `TOOL-aOrientedCast-16` (order 16) lands first and edits
`FRONT_MATTER_KEYS`, `REQUIRED_ROLE_KEYS`, R4 and the role files, so the builder finds each site by
its identifier.

### The two keys

Both are one-line values in the existing grammar (`roles_lib.py:8-11`): column 0, kept raw. Each
opens with a letter and carries no `: ` and no ` #`, so each stays a plain YAML scalar and a role
file stays a valid agent definition: YAML reserves a leading backtick and reads a leading brace as
a flow mapping.

| Key | Grammar | Read as | On the roster line |
|---|---|---|---|
| `mandatory` | exactly `no` | the role is optional | `Optional` |
| `mandatory` | `no — <when it is used>` | the role is optional | `Optional, <when it is used>` |
| `mandatory` | any other value, a phrase that reads after "Mandatory", such as `for every unit built` | the role is mandatory | `Mandatory <value>` |
| `mandatory` | a mandatory value carrying `unenforced — <why>` | mandatory, and no hook enforces it, by its own statement | `Mandatory <value>` |
| `output` | one line naming where the role's output goes | on a writer role, it must carry its class's folder | `Output: <value>` |

The checker reads the optional form with `NOT_MANDATORY_RE = re.compile(r"^no(?: — .+)?$")` and
the escape with `UNENFORCED_RE = re.compile(r"\bunenforced — \S")`. Case is exact: `No` reads as
mandatory.

### The checker rules

**R13**, evaluated in the loop that already joins each role to its workflow entry for R7
(`check_roles.py:247-253`), because the role loop above it runs before the table is read:

1. A `{{…}}` token in `mandatory` other than `{{MEMORY_ROOT}}`, found by `lib.TOKEN_RE`
   (`roles_lib.py:45`), is a defect naming the token, on any role.
2. Skip the role when `NOT_MANDATORY_RE` matches, or when its `workflow` names no entry (R7 already
   reports that). Otherwise count it as mandatory.
3. The entry names a hook when its `enforced-by` is a list holding a string that
   `HOOK_ENTRY_RE = re.compile(r"^[^\s/\\]+\.js(?=[\s,]|$)")` matches: a first word that is a
   `.js` script's file name. The string form `none — <why>` (`workflows.toml:28`, `:95`) names none.
4. No hook and no `UNENFORCED_RE` match is a defect:
   `roles: <path>: R13 — mandatory '<value>' calls this role mandatory, and the '<workflow>' entry's enforced-by names no hook; name the hook script there, or say 'unenforced — <why>' in the value`.

On today's table, `spec-write` and `build` open with `scratch-guard.js`, and `spec-review`,
`closing-review` and `research` with `agent-cap.js` (`workflows.toml:38`, `:48`, `:58`, `:68`,
`:86`). `orient` names the card writer `manifest-check.sh --card --append` (`:19`), `bookkeeping` a
gate leg (`:104`), and `gate-bar` a git hook (`:77`), so none of those three reads as a hook here. Why
this reading: §8 F2.

**R14**, in the role loop (`check_roles.py:124-173`), from one table beside `WRITES` (`:65`):

```python
WRITE_FOLDERS = {"spec": "{{MEMORY_ROOT}}/builds/<slug>/spec/",
                 "review": "{{MEMORY_ROOT}}/builds/<slug>/reviews/",
                 "product": "ROUTED_PATHS", "records": "{{MEMORY_ROOT}}/"}
```

1. A `{{…}}` token in `output` other than `{{MEMORY_ROOT}}` is a defect naming the token.
2. When `WRITE_FOLDERS` holds the role's `writes`, count it as a graded writer output; a value that
   does not contain that folder spelling as a substring is a defect:
   `roles: <path>: R14 — output '<value>' does not name the <class> class's folder, <folder>`.
3. A `writes: none` role's `output` is graded only by R2's non-empty rule.

The spec and product classes are the two the hooks kit's write gate grades
(`tools/hooks/scratch-guard.js:91-103`): a spec is a path under `<MEMORY_ROOT>/builds/<build>/spec/`,
a product path is one `ROUTED_PATHS` in `.memory-tree.conf` covers. A review record lives under
`memory/builds/<slug>/reviews/` (`AGENTS.md:151`). The product class has no single folder, so its
spelling is the conf key that declares its paths (§8 F4).

The summary line gains `, <n> mandatory roles, <n> writer outputs` after the count of `reads`
keys, both derived by the loops above. The header's rule list gains R13 and R14 in the shape of
R0 to R12, and its WHAT THIS DOES NOT CHECK paragraph gains three readings: a first word ending in
`.js` is read as a hook without asking whether that script exists, is wired or refuses an inline
stand-in; an `output` is not compared with where the role writes; and a `mandatory` value's
when-clause is not tested for truth.

R13 and R14 are the next free rule numbers: the header ends at R12 (`check_roles.py:30`),
`TOOL-aOrientedCast-16` mints none (its §3), and `TOOL-aOrientedCast-19` takes R15 after these.

### The roster verb

`python handoff.py roster`, a subparser beside `harness-args` and `stage-efforts`
(`tools/roles/handoff.py:426-427`), taking no argument. `print_roster(memory_root)` sits beside
`print_harness_args` and `print_stage_efforts` (`:374-409`) and composes, from `lib.load_roles` and
`lib.load_workflows`, one line per role:

```
- `<slot>`: <description> <when>. Output: <output>.
```

- `<when>` is the "On the roster line" column of §4 "The two keys": `Optional` for a value of
  exactly `no`, `Optional, <text>` for `no — <text>`, and `Mandatory <value>` otherwise.
- `{{MEMORY_ROOT}}` is replaced across the line by the conf's `MEMORY_ROOT`. A trailing `.` on the
  `mandatory` or `output` value is stripped first, so the line never doubles one.
- Order is the workflow table's: a role sorts by the file index of the entry its own `workflow` key
  names in `workflows.toml`, then by its position in that entry's `roles` list. A role whose
  `workflow` names no entry sorts after the rest, by slot. On today's table that gives
  `gov-orienter`, `gov-reuse-scout`, `gov-spec-writer`, `gov-spec-reviewer`, `gov-builder`,
  `gov-diff-reviewer`, `gov-skeptic`, `gov-synthesizer`, `gov-researcher`, `gov-session`.
- Every role is listed, `agent: false` included: `gov-session` is how work passes to another
  session, and the roster says so.
- A line longer than `ROSTER_LINE_MAX = 200` characters, counted as Python counts a `str`, refuses.
  That is the measure the playbook's one-line region applies to a rendered rule
  (`tools/playbook/render_playbook.py:126`, `:657`), spelled again because a roles kit file may not
  import a sibling kit or name it by path. The constant carries a `ponytail:` comment naming the
  playbook's one-line limit in words. A drift between the two fails closed either way: a lower
  playbook limit refuses at the charter render, and a higher one only refuses here first.
- All lines are composed before any is written. Every over-long line is named on stderr, as
  `roster line for <slot> is <n> characters, past the 200 a one-line charter rule may take; shorten
  its description, mandatory or output`, and stdout stays empty, so a probe never substitutes a
  partial roster.
- A role missing `description`, `mandatory` or `output` refuses naming the role and the key, rather
  than printing `None`. Zero role files refuse naming the empty `agents/` directory.
- Output is written as `print_harness_args` writes it, `sys.stdout.buffer` with UTF-8 bytes
  (`:391-392`), so a cp1252 console cannot mangle a non-ASCII character, such as the em dash an
  `unenforced — ` clause carries.

Exits: 0 printed; 1 on any refusal above, through `main`'s existing `RolesError` path with the
`handoff: ` prefix on stderr; 2 when the working directory is in no repository or the conf declares
no `MEMORY_ROOT`. In `main` (`:458-475`) the verb is dispatched after the `MEMORY_ROOT` read and
before `lib.resolve_charter_path`, so the roster never reads `CHARTER`: on a first install the
playbook render writes the charter, and the owner's render order is charter first, agents second.
The docstring's usage block and exit sentence gain the verb.

### The values

Two limits bind the lines. Each is at most 200 characters, the one-line region's rule. All ten
together must fit the bytes `AGENTS.md` has left under its 16384-byte ceiling once
`PLAY-aOrientedCast-2` adds its blocks: that unit's §4 "Bytes, measured" derives 1466 bytes at
`d518b483`, each line costing its UTF-8 bytes plus a newline, and re-measures at its own build.

PINNED at writing, measured on 2026-10-13 with `memory` as the memory root: the ten lines total
1383 bytes with their newlines, 83 under that budget; the longest is `gov-synthesizer`'s at 152
characters; and the two lines carrying `{{MEMORY_ROOT}}` stay within 200 for a memory root of up to
54 characters. The verb re-derives every length when it runs.

| Slot | `description` | `mandatory` | `output` |
|---|---|---|---|
| `gov-orienter` | Orients one session for one task, read-only. | no — the main loop may orient itself | the card, to the main loop |
| `gov-reuse-scout` | Finds the seam a new behaviour should extend. | no — when kickoff asks for one | the seam, to its caller |
| `gov-spec-writer` | Writes each unit's spec, never code. | for every spec written | specs in `{{MEMORY_ROOT}}/builds/<slug>/spec/` |
| `gov-spec-reviewer` | Hunts defects in a spec set, read-only. | for every spec audit owed | findings, to its harness |
| `gov-builder` | Builds one unit from its spec and commits it. | for every unit built | commits under `ROUTED_PATHS` |
| `gov-diff-reviewer` | Reviews a diff through one lens. | for every closing review | findings, to its harness |
| `gov-skeptic` | Tries to refute each finding it is handed. | for every review's findings | verdicts, to its harness |
| `gov-synthesizer` | Merges verified findings into one report. | for every review's report | a report in `{{MEMORY_ROOT}}/builds/<slug>/reviews/` |
| `gov-researcher` | Finds candidates and the test each could lose. | no — when no seam decides a design | candidates, to its caller |
| `gov-session` | Opens a handoff to another session. | no — when work leaves this session | a prompt file in the build's `prompts/` |

So the `gov-builder` line reads:

```
- `gov-builder`: Builds one unit from its spec and commits it. Mandatory for every unit built. Output: commits under `ROUTED_PATHS`.
```

The six mandatory roles are the four kinds of work the addendum's `[roles]` rule sends to a role:
spec writing, spec review, building and the closing review. Each one's own workflow names a hook,
so none needs the `unenforced` clause. The three writers are `gov-spec-writer`, `gov-builder` and
`gov-synthesizer`. Each `description` is rewritten from today's longer one, because the shipped
descriptions put the roster at 2168 bytes and seven of its lines past 200 (§8 F1). The role bodies
are unchanged.

### A charter this unit does not read

Neither R13, R14 nor the verb reads the governing doc. R13 and R14 read the role files and
`workflows.toml`; the verb reads those and `.memory-tree.conf`'s `MEMORY_ROOT`. On an adopter whose
seeded template still renders a v3.x charter, with `§` headings and no tagged rules, both behave
exactly as on gov. What the checker does there for its charter-reading rules is
`TOOL-aOrientedCast-16`'s, and whether such a charter carries the roster is the playbook's.

### The suite arm

A new arm in `tools/roles/adopt-roles.test.sh`, numbered after the suite's last arm at build time,
built with the suite's own `build_fixture` (`:54-62`), which already copies this kit into a fixture
repository with the conf's `MEMORY_ROOT`. Its assertions:

1. The fixture scaffolds and checks clean, as every arm opens.
2. `handoff.py roster`, run from the fixture root, exits 0 and prints as many lines as the fixture
   kit holds `agents/*.agent.md` files, each opening with a backticked slot after `- `.
3. With `gov-builder.agent.md`'s description lengthened by 200 characters, it exits 1, its stderr
   names `gov-builder`, and its stdout is empty.

The header's arm list gains the arm. `FLOOR_ASSERTIONS` rises by three, and its comment says which
unit raised it, as the line above it does.

### Documentation

- `tools/roles/README.md`: the opening's front-matter sentence (`:7-9`) gains "when it is mandatory
  and where its output goes"; "Editing a role" gains one sentence saying both keys ride the base
  file, so an overlay cannot change them; "The handoff renderer" gains a paragraph on the `roster`
  verb, with its line, its order, its 200-character refusal, its exits, that it reads no charter,
  and that the playbook kit's derived placeholder is its consumer; "The checker" names R13 and R14
  and says the rules are listed in the header, in place of the range "R0 to R11" (`:199-200`),
  which R12 already outgrew.
- `tools/roles/check_roles.py` and `tools/roles/handoff.py` docstrings, as above.
- `memory/map/features/roles.md`: `TOOL-aOrientedCast-17` joins its `decisions` list, and its prose
  gains one sentence on the two keys and the roster verb.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `mandatory`, `output` | front-matter keys | none: a front-matter key carries no naming cell |
| `R13`, `R14` | checker rule ids | none |
| `roster` | `handoff.py` verb | none: a CLI verb carries no naming cell |
| `print_roster` | function in `handoff.py` | `py.function`; `lexicon.py --suggest print_roster --as py.function` answered OK |
| `NOT_MANDATORY_RE`, `UNENFORCED_RE`, `HOOK_ENTRY_RE`, `WRITE_FOLDERS` | constants in `check_roles.py` | none: `--suggest <name> --as py.constant` answered that `py.constant` is undeclared |
| `ROSTER_LINE_MAX` | constant in `handoff.py` | none, as above |

### Files touched (estimate)

`tools/roles/roles_lib.py`
`tools/roles/check_roles.py`
`tools/roles/handoff.py`
`tools/roles/agents/`
`tools/roles/README.md`
`tools/roles/adopt-roles.test.sh`
`.claude/agents/`
`memory/map/features/roles.md`
`memory/map/generated/`

### Rollout

- Built after `TOOL-aOrientedCast-16`, which order 16 puts first.
- The pass re-renders the agent types with `python tools/roles/render_agents.py --write`, then runs
  `python tools/codebase-map/gen_map.py --write`, because `print_roster` stales the generated map.
  Neither touches the kickoff manifest's `watch:` list, so no `last-audit` re-stamp is owed.
- **The roles kit's version** moves from 1.2 to 1.3 once in this set, in the highest-`order` unit
  whose `### Files touched (estimate)` names a path under `tools/roles/`. Read on 2026-10-13:
  `TOOL-aOrientedCast-18`'s and `PLAY-aOrientedCast-2`'s name none, and `TOOL-aOrientedCast-19`'s,
  order 19, names several and carries the move as its AC9. So this unit moves no version. The carriers
  that unit moves are `KIT_ROLES_VERSION` at `tools/roles/roles_lib.py:18`, which
  `tools/roles/kit.toml:22` reads as `version_from` and `tools/check-kit-versions.sh:387-393`
  grades against the README's marker; the `gov:kit roles@` markers at `tools/roles/README.md:1` and
  `tools/roles/SKILL.template.md:5`, which `write_version_carriers` in
  `tools/govkit/govkit.py:798-814` moves as one basis; and the rendered
  `.claude/skills/build/SKILL.md:5`. Should that unit be retired before this one closes, the rule
  passes the move back here, and this spec takes a rev to say so.
- Adopters receive both keys and the verb with the kit at `govkit update`: the base role files are
  the kit's and are overwritten, and the seeded overlays and policy are untouched. Rollback is the
  revert of this unit's commit and a re-render.

### Alternatives rejected

- A third key for "what it does", or the description cut at its first clause: §8 F1.
- Reading "names a hook" from the word `hook`, from the target's hook wiring, or from a new typed
  key in `workflows.toml`: §8 F2.
- The verb as a `check_roles.py` flag or a new script: §8 F3.
- Substituting the conf's `ROUTED_PATHS` value into the builder's line, or leaving the product class
  ungraded: §8 F4.
- Grading the roster's line length in `check_roles.py` as well. The playbook render's one-line
  region and the verb both refuse an over-long line already, and a third grader of one limit is a
  third copy of it.

## 5. Production-readiness checklist

- security — No write path: the verb prints, and R13 and R14 read. The roster becomes charter text
  every agent reads, so its values are kit-authored front matter, reviewed like code, and an adopter
  cannot inject one through an overlay.
- perf / scale — One read per role file, one of `workflows.toml`, one of the conf and one
  `git rev-parse`: well under a second.
- error / empty / loading states — An over-long line, a missing key and an empty catalogue each
  refuse with exit 1, naming the role and nothing printed; no repository or no `MEMORY_ROOT` exits 2;
  an absent charter is not read and refuses nothing.
- observability — The checker's summary prints both new counts on every run, so a probe that read
  no mandatory role says so; every refusal names its role, key or length.
- risks — The roster's 83 bytes of headroom under gov's charter ceiling are thin: a later role or a
  longer value can overflow `AGENTS.md`, which `PLAY-aOrientedCast-2` re-measures at its build and
  whose §8 F2 routes an overflow back to these lines. An adopter memory root past 54 characters
  pushes two lines past 200 and refuses the charter render there. The `.js` reading is a spelling
  convention, and the header says so. The shorter descriptions also change what Claude Code shows
  for each agent type.
- testing — The fixture probes of §6 in the pass; the catalogue arm and the roster arm of §7,
  observed RED-first by the main loop at the close.
- migration — None beyond the kit update, as §4 "Rollout" states.
- user docs — The roles README; `help/roles.md` is `PLAY-aOrientedCast-2`'s.

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag; each runs the unit's own code on a
scratch copy or on gov's tree, or reads its output. The suite arms are under `New arm:` in §7.

Fixture A is a scratch directory under the run's scratch path holding a copy of `tools/roles/` at
`tools/roles`, a copy of `tools/gate-legs.json` at the same relative path, so the policy's `[gates]`
names resolve beside the kit, a copy of `AGENTS.md`, and a `.memory-tree.conf`
declaring `MEMORY_ROOT=memory` and `CHARTER=AGENTS.md`; its checker runs as the copied
`check_roles.py --root <fixture A>`. Fixture B is a git repository under a short `%TEMP%` root
holding a copy of `tools/roles/` at `tools/roles` and a `.memory-tree.conf` declaring only
`MEMORY_ROOT=memory`, with no charter file; its verb runs as `python tools/roles/handoff.py roster`
from the fixture root. Every staged break is restored before the next.

- **AC1** — When the copied `check_roles.py --root <fixture A>` runs over an unmodified copy, it
  exits 0, prints no `R13` or `R14` line, and its summary line reports 6 mandatory roles and 3
  writer outputs.
  Red when: a shipped role is refused by R13 or R14, or the summary carries neither count.
  figure: 6 and 3 are PINNED from §4 "The values"; the checker DERIVES both at observation.
  fixture: fixture A, built in the pass; nothing in the tree holds one today.
- **AC2** — When fixture A takes each break below, the copied `check_roles.py --root <fixture A>`
  answers as stated: `gov-orienter.agent.md`'s `mandatory` set to `for every session` exits 1 with
  an `R13` line naming that file and `orient`; that value with `, unenforced — the card writer is no
  hook` appended exits 0; `gov-builder.agent.md`'s `mandatory` line deleted exits 1 with an `R2`
  line naming `mandatory`; `gov-builder.agent.md`'s `mandatory` given a `{{TOOL_ROOT}}` token exits
  1 with an `R13` line naming it; and the `build` entry of `workflows.toml` given
  `enforced-by = ["routed commits name a specced unit"]` exits 1 with an `R13` line naming
  `gov-builder.agent.md`.
  Red when: a mandatory role under a workflow naming no hook passes, the `unenforced — ` clause does
  not lift it, or a missing or token-carrying value passes.
- **AC3** — When fixture A takes each break below, the copied `check_roles.py --root <fixture A>`
  answers as stated: `gov-spec-writer.agent.md`'s `output` set to `specs, to the main loop` exits 1
  with an `R14` line naming `spec` and `{{MEMORY_ROOT}}/builds/<slug>/spec/`;
  `gov-synthesizer.agent.md`'s set to `a report` exits 1 with an `R14` line naming `review`;
  `gov-builder.agent.md`'s set to `commits` exits 1 with an `R14` line naming `ROUTED_PATHS`;
  `gov-spec-writer.agent.md`'s given a `{{TOOL_ROOT}}` token beside its folder exits 1 with an `R14`
  line naming the token; `gov-skeptic.agent.md`'s set to `anything at all` exits 0; and
  `gov-skeptic.agent.md`'s `output` line deleted exits 1 with an `R2` line naming `output`.
  Red when: a writer's output without its class's folder passes, a non-writer's free text refuses,
  or a missing or token-carrying output passes.
- **AC4** — When `python tools/roles/handoff.py roster | python -c "import sys; ls = sys.stdin.buffer.read().decode('utf-8').splitlines(); print(len(ls), max(map(len, ls)), ls[0][:16], ls[-1][:15], any('{{' in l for l in ls))"`
  runs in the worktree, the verb exits 0 and the probe prints the count of
  `tools/roles/agents/*.agent.md` files, a longest line of at most 200, a first line naming
  `gov-orienter` and a last naming `gov-session`, and `False`; the `gov-spec-writer` line carries
  `memory/builds/<slug>/spec/`, and the `gov-reuse-scout` line carries `Optional, when kickoff`.
  And `python tools/roles/handoff.py roster | python -c "import sys; print(len(sys.stdin.buffer.read()))"`
  prints at most 1466, the roster's bytes with its newlines.
  Red when: a role is missing or doubled, the order is not the workflow table's, a line passes 200,
  an optional value prints as mandatory, a token survives, or the roster outgrows the charter's
  budget.
  figure: the line count is DERIVED from the agents directory; 152 as the longest and 1383 bytes as
  the total are PINNED in §4, and 1466 is `PLAY-aOrientedCast-2`'s budget, PINNED at `d518b483`.
- **AC5** — When fixture B's `python tools/roles/handoff.py roster` runs, it exits 0 with one line
  per role file, n being `gov-builder`'s line length; with that role's description lengthened by
  201 - n characters it exits 1, its stderr names `gov-builder`, `201` and `200`, and its stdout is
  empty; lengthened by 200 - n instead, it exits 0 and prints that line at exactly 200 characters.
  Red when: a 201-character line prints, a 200-character line refuses, or a refusal leaves a line on
  stdout.
  fixture: fixture B, a git repository under a short `%TEMP%` root, built in the pass.
- **AC6** — When fixture B's `python tools/roles/handoff.py roster` runs with every role file moved
  out of its `agents/` directory, it exits 1 with stderr naming the empty catalogue and an empty
  stdout; with the conf's `MEMORY_ROOT` line deleted, it exits 2 naming `MEMORY_ROOT`. AC5's exit 0
  is itself observed with no `CHARTER` key and no charter file.
  Red when: an empty catalogue exits 0, an unarmed root prints lines, or the verb refuses for want of
  a charter.
- **AC7** — When `python tools/roles/render_agents.py --write` and then
  `python tools/roles/render_agents.py --check` run in the worktree, the check exits 0,
  `grep -c "^description: Builds one unit from its spec" .claude/agents/gov-builder.md` prints 1, and
  `grep -lE "^(mandatory|output):" .claude/agents/gov-builder.md .claude/agents/gov-spec-writer.md`
  prints nothing.
  Red when: an agent type keeps its old description, or carries either new key.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `govkit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/check_roles.py · covers AC2 AC3 · gov-orienter's `mandatory` staged to `for every session` under the hookless `orient` entry, then gov-spec-writer's `output` staged to omit its folder, each against the shipped catalogue · none
New arm: tools/roles/adopt-roles.test.sh · covers AC5 · the roster arm, against a `handoff.py` whose 200-character refusal is staged out so the lengthened line prints · `FLOOR_ASSERTIONS` raised by the arm's assertions

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — Which text says what a role does on its roster line?**
  Options: (a) the role's `description`, Claude Code's own one-line key, rewritten so each line fits;
  (b) a third key such as `does`; (c) the shipped description cut at its first comma or semicolon.
  Measured on `d518b483f` under §4's line grammar and values: with the shipped descriptions, 7 of
  the 10 lines pass 200 and the roster is 2168 bytes; cut at the first clause, every line fits 200
  but the roster is 1551 bytes, past the 1466 `PLAY-aOrientedCast-2` derives, so both fail AC4: M3
  veto 1. The cut also drops what the clause after it says. (b) states what a role does twice in one
  file, beside the description, where the kit README's rule is that a value stated beside its owner
  rots, and the brief's row names two keys, not three.
  Recommendation: (a). One source for the fact, and the rewrite is measured in §4.
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The values" states it.
- **F2 — How does R13 read that an `enforced-by` entry "names a hook"?**
  Options: (a) the entry's first word is a `.js` script's file name; (b) the entry carries the word
  `hook`; (c) a join against the target's hook wiring, through `.claude/settings.json` or the kits'
  `*.fragment.json` files; (d) a new typed key in `workflows.toml`.
  (a) needs no change to `workflows.toml`: the five hook entries already open with their script,
  and the card writer and the two gate legs do not. (b) needs five entries reworded. (c) couples
  the catalogue leg to wiring, which `check-wiring.sh` owns, and the fragment form misses
  `agent-cap.js`, which `tools/hooks/` wires with no fragment file, so it would refuse the review
  roles of a correct table and fail AC1: M3 veto 1. (d) is a second home for what `enforced-by`
  already says, and an R6 and README region change. Tie-break between (a) and (b): (a) reuses the
  entries as written.
  Recommendation: (a), with the header saying the reading is a spelling convention.
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The checker rules" states it.
- **F3 — Which script carries the `roster` verb?**
  Options: (a) `handoff.py`, whose `harness-args` and `stage-efforts` subcommands the brief and the
  resume handoff both call verbs, and which already resolves the root and `MEMORY_ROOT`; (b) a
  `--roster` flag on `check_roles.py`, the `roles catalogue` leg's own argv; (c) a new script.
  (b) would have the playbook render invoke a gate leg's script. (c) adds a file and a second root
  and conf reader. `TOOL-aOrientedCast-18` §8 F1 chose (a) for its probe, independently.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The roster verb" states it.
- **F4 — What is the product class's folder spelling for R14?**
  Options: (a) the conf key `ROUTED_PATHS`, written as is; (b) the verb substitutes the conf's
  `ROUTED_PATHS` value into the builder's line; (c) no folder for the product class.
  (b) measured on gov: its value is 72 characters, so the builder's line grows by 60 bytes to 192
  characters and spends 60 of the roster's 83 bytes of headroom; an adopter's value is unbounded,
  so a long one pushes the line past 200 and refuses that adopter's charter render, a follow-up (a)
  never opens.
  (c) leaves one writer class ungraded, where the brief's rule names every writer role, and fails
  AC3's product break: M3 veto 1.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The checker rules" states it.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "print one line per agent role saying what it does when
it is mandatory and where its output goes"` ranked name-stem neighbours: `check_line` and
`render_line` in the runlog kit, and `RolesError`, `load_roles` and `render_role` in the roles
library. None composes a role roster, so no existing seam fits as a new module. The seams this unit
extends are `handoff.py`'s verb dispatch beside `print_harness_args` and `print_stage_efforts`
(`tools/roles/handoff.py:374-439`), the checker's role loop and its R7 join
(`tools/roles/check_roles.py:124-255`), and the front-matter key table
(`tools/roles/roles_lib.py:23-24`). The 200-character measure is the playbook's one-line region's
(`tools/playbook/render_playbook.py:126`, `:657`), spelled again because a kit file may not import a
sibling. The recall probe surfaced the owner's addendum, the brief's row and
`TOOL-aOrientedCast-1`'s account of `enforced-by`, each read against source: the account still
matches `workflows.toml`, and TOOL-aOrientedCast-6's spec brief matched the two write classes
`scratch-guard.js` grades today.

Recall terms used: `role mandatory enforced-by hook workflow roster output writes spec product review folder`
