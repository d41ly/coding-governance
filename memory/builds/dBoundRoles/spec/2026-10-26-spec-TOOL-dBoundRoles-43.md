# TOOL-dBoundRoles-43 — the round-1 audit's 46 roles-code minors: one grammar each for returns, shapes and slots, one reader and writer each, bounded readers, resumable steps, and the registries they feed

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 28 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 |
| [2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md) | research | TOOL-dBoundRoles-37 TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-44 |
| [2026-10-26-build-TOOL-dBoundRoles-43-round1-size-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-43-round1-size-return.md) | research | TOOL-dBoundRoles-3 TOOL-dBoundRoles-24 TOOL-dBoundRoles-44 |
| [2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md) | research | TOOL-dBoundRoles-45 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |
| [2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-37-round1-fix-brief.md) | research | TOOL-dBoundRoles-37 TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 |
| [2026-10-26-prompt-TOOL-dBoundRoles-43-round1-size-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-43-round1-size-brief.md) | research | TOOL-dBoundRoles-3 TOOL-dBoundRoles-24 |
| [2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md) | research | TOOL-dBoundRoles-45 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |
| [2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 26 unit specs
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`) confirmed
six HIGH findings, `TOOL-dBoundRoles-37` to `-42`, and 43 MEDIUM and 14 LOW, which M4 batches in two by M6
(§4). This unit takes the 34 MEDIUM and 12 LOW that write or read the roles code, hooks, govkit steps and
playbook extractor, each id named on its item in §2; `TOOL-dBoundRoles-44` takes the other 11 (§3). Each
id is its own item, even where the report merged two; ids 47 and 53 are the MEDIUM halves of `-37` and
`-41`. Items keep their pre-split numbers, so eleven S-numbers are absent.

## 2. Scope (IN)

- **S1** — id 1. A one-value set is a legal return type. `parse_return_template` in
  `tools/roles/roles_lib.py` reads `type := … | value ("|" value)*`; R2 refuses an empty set and a value named
  twice, not a set of one. The five one-value templates of unit 2 §4 (`gov-spec-writer` `done`,
  `gov-skeptic` `judged`, `gov-synthesizer` `reported`, `gov-orienter` `oriented`, `gov-session` `sent`) pass,
  and the grammar line in `tools/roles/README.md` says so. Observed by AC1.
- **S2** — id 2. Unit 25's AC3 answered. No unit builds a shape refusal (unit 16 §8 F3; unit 25 §3 moves
  each rule unchanged), so a rev bump of unit 25's spec, its §9 line naming id 2 and this unit, made by its
  pass or else this one, amends AC3 to the moved `checkHarnessCall` refusing a `roles` value naming no
  agent-true role, answered AMENDED in its ledger (§8 F3). Observed by AC2.
- **S5** — id 6. The prompt writer refuses through the arm. `gov-prompt-writer`'s `return` drops `refused`
  from its own `outcome` set, leaving `outcome:framed, …` (legal under S1), and `--framed-by`'s refusal (unit
  4 S3) reads unit 26's composed arm, `outcome: refused`, so unit 26's no-redeclaration rule holds on gov's
  tree (§8 F5). Observed by AC5.
  **Readers:** by name: `tools/roles/handoff.py` (unit 4 S3's refusal) and `tools/roles/check_roles.py` (unit
  26's no-redeclaration rule); READER NOT IN TREE: the role file, which unit 4 adds after base · by value:
  `validate_return`, which reads a refused return against unit 26's arm.
- **S6** — id 7. The ceiling reads the grant where the index does. `render_agent_file` and `render_handoff`,
  both `render_role` callers, pass the legs of the role's `gates` field, the house `[gates]` row as
  fallback, through the `check_gate_names` path unit 21 S6 gives `render_roles_index`, so each rendered
  `## Ceiling` lists the legs `.claude/roles.json` grants. Observed by AC6.
- **S7** — id 8. The `budget` row in unit 2's grammar. `tools/roles/role-schema.toml` holds one `[[field]]`
  row `key = "budget"`, `owner = "gov"`, `shape = "int"`, `required = "every"`, with no `type` or `meaning`
  key; `FRONT_MATTER_KEYS` gains `budget` by derivation; the shape table gains `int`, a non-negative decimal
  integer. Observed by AC7.
- **S8** — id 32. Every later row has a shape. The rows units 1, 16 and 21 add each name a shape of unit 2's
  closed table: `shapes` and `gates` are `list`, and the table gains, stated in the README, `tag`, a tag of
  the namespace the row's `ns` key names (`layer`), and `choice`, one value of the list its `values` key
  names or of the constant it names (`acts-as`, `effort`). `load_role_schema` reads every row without
  refusal (§8 F4). Observed by AC8.
- **S9** — id 9. The house step moves every seeded overlay. Unit 19's step `surfaces` and its seed-rule edit
  act on every `house/*.md` the roles descriptor seeds at unit 19's parent commit, unit 1's four new overlays
  among them, never a typed ten. Observed by AC9.
- **S10** — id 10. An old reviewer's house text reaches the merged role. Where unit 18's up carries an old
  stem's house text, it writes a level-5 `[[unit]]` selecting `role.gov-reviewer` through
  `write_overlay_units`, tagged `repo.house.gov-reviewer.<stem>`, not an append to `house/gov-reviewer.md`,
  which unit 19's render no longer reads; unit 18's ledger answers AC6 AMENDED. Observed by AC10.
  **Readers:** by name: `tools/roles/roles_lib.py:584` (`render_role`), `tools/roles/check_roles.py:340` (R10)
  and `tools/roles/kit.toml:36-39` (the seed include); READER NOT IN TREE: the merged role's house file, unit
  1's · by value: `render_role`, rendering the text (`roles_lib.py:591`), and R10, counting it (`:342`).
- **S11** — id 11. One spelling of a repository role's slot. The slot is the overlay row's bare `<name>`: the
  index key, the agent file stem and the actor id `role:<name>` spell it, and the tag `role.adopter.<name>`
  maps to it by one stated rule in `roles_lib.py`. The composition refuses a repository role named as a gov
  slot. Unit 20's ledger answers AC6 AMENDED, its actor patch spelled `role:triager` (§8 F6). Observed by
  AC11.
- **S12** — id 12. The stand-in case under the new default. `tools/roles/adopt-roles.test.sh`'s stand-in case
  (unit 15 AC2) sets `roles.no-spawn = "recorded-stand-in"` in its fixture policy, and a sibling case without
  it expects the default's refusal naming `roles.no-spawn` (§8 F7). Observed by AC12.
- **S13** — id 13. The refusal arm inside the composition. `render_role` composes the arm into
  `## Return` after the role's template, from `role-schema.toml`'s `[return.refusal]` table, and
  `render_agents.py` appends nothing, so the arm sits inside `render_static_block`, R5's budget and the
  `role-sha`. Observed by AC13.
- **S14** — id 36. Both routes carry one return block. For every agent-true role, the `## Return` section
  of `.claude/agents/<slot>.md` is byte-equal to the one `handoff.py render --role <slot>` writes under
  `## Role`, and `gov-session`'s handoff carries `outcome: refused` once. Observed by AC14.
- **S15** — id 24. The gone reviewers leave the carrier registry. `memory/project/method-carriers.txt` holds
  no row for `.claude/agents/gov-spec-reviewer.md` or `.claude/agents/gov-diff-reviewer.md`. Observed by AC15.
- **S16** — id 46. Every agent file naming the method is declared. Each `.claude/agents/*.md` naming
  `BUILD-METHOD.md` has one `<path> · <why>` row in `method-carriers.txt`. Observed by AC16.
- **S17** — id 25. The adopter's registry follows the merge. `tools/govkit/steps/reviewer_merge.py`'s up
  replaces every row of the target's `<memory root>/project/method-carriers.txt` naming either old type with
  one `.claude/agents/gov-reviewer.md` row, de-duplicated, the file in its before-image and its down; govkit case
  `reviewer-merge-carriers` holds it. Observed by AC17.
- **S19** — id 27. Hooks read the policy through the reader alone. Over `tools/hooks/scratch-guard.js`
  and `tools/roles/spawn-guard.js`, the hooks reading the three keys after unit 25,
  `git grep -n -E "policy\.toml|\.governance/"` prints only the `readPolicy` import and locator lines.
  Observed by AC19.
- **S21** — id 31. One Python policy reader in the roles kit. `read_policy_setting` (unit 21 S1) is the only
  reader: unit 15's `instructions.task-charter` read (`None` meaning `when-not-static`), unit 10's
  `roles.no-spawn`, unit 11's key and unit 5's `roles.retries` each call it, and no file under `tools/roles/`
  runs `policy.py get` as a subprocess or imports `resolve` outside it. Observed by AC21.
- **S22** — id 35. `WRITE_FOLDERS` has one home, `roles_lib.py`: `render_role`,
  `derive_allowance` and `check_roles.py`, as `lib.WRITE_FOLDERS`, read it, and `roles_lib.py` imports
  nothing from `check_roles.py`. Observed by AC22.
- **S23** — id 37. One writer of the overlay. `reviewer_merge.py`'s value edit of
  `.governance/instructions.toml` goes through `write_overlay_units` in `tools/playbook/overlay.py`, given a
  re-key mode mapping old tag values to new, so the one writer keeps its ordering and its byte-identical
  file on refusal. No `write_overlay_values` exists (§8 F8). Observed by AC23.
- **S24** — id 38. An extractor declares the adopter role form. `extract_role` in
  `tools/playbook/tag_index.py` also yields `role.adopter.<name>` for each `[[role]]` row of
  `instructions.toml`, the `role` row of `tools/playbook/namespaces.toml` names that file in its
  `source`, and `gov_tag.py --fixture` gains the plant `role-rows-adopter`. Observed by AC24.
- **S25** — id 63. A cited adopter role is declared. In the fixture, an actor patch citing
  `role.adopter.triager` leaves unit 14 S6's cited-but-undeclared join green, and the join reds naming the
  citation once the overlay row is removed. Observed by AC25.
  **Readers:** by name: READER NOT IN TREE: the row and its citation live in the plant S24 adds to the tag
  fixture of PLAY-dOrderedCharter-19 S13, unbuilt at base · by value: `check_namespace_joins`, unit 14 S6's
  join, which compares the citation with the extractor's declarations.
- **S27** — id 44. The retired suite leaves the count registry. `memory/project/testsuite-count-waivers.txt`
  holds no `tools/hooks/agent-cap.test.sh` row, and `tools/roles/spawn-guard.test.sh` prints
  `PASS (<n> assertions)` against a pinned `FLOOR_ASSERTIONS`, the form the count check reads, so it needs
  no row. Observed by AC27.
  **Readers:** by name: `memory/project/testsuite-count-waivers.txt` (row 10) and
  `tools/check-testsuite-counts.sh:45` · by value: `tools/check-testsuite-counts.sh:145`, which reds a waiver
  naming a suite the manifest does not run.
- **S28** — id 45. Citations of deleted files are waived where they cannot move.
  `memory/project/spec-token-waivers.txt` gains one row each for `tools/hooks/agent-cap.js` and
  `tools/hooks/agent-cap.test.sh`, its reason naming `aDeclaredBound-4` and every live dBoundRoles spec citing
  them at the pass, and one row for `tools/roles/house/gov-diff-reviewer.md`, its reason naming unit 18 AC6,
  never a basename (§8 F16). Observed by AC28.
  **Readers:** by name: the live specs citing the paths, listed at the pass by git grep,
  `memory/builds/aDeclaredBound/spec/2026-08-18-spec-TOOL-aDeclaredBound-4.md` among them at base, and
  `memory/project/spec-token-waivers.txt` · by value: `tools/check-spec-tokens.py`, which reds an untracked
  citation, reads the registry (`:256`) and reds a stale row (`:1666`).
- **S29** — id 47. The install case's docstring states the derivation. `check_roles_install`'s docstring
  (`tools/govkit/selftest.py:2769`) says the case expects one agent type per agent-true role and every seeded
  house overlay, as `TOOL-dBoundRoles-37`'s `derive_roles_expected` computes, with no number. Observed by
  AC29.
- **S32** — id 50. Every stage reader reads the rows. `print_stage_efforts` and every `.get("stages")` reader
  at the build run's base (`tools/roles/handoff.py:463`, `:484`; `tools/roles/roles_lib.py:443`, `:576`;
  `tools/roles/check_roles.py:297`) read unit 22's rows through `load_workflows` and `derive_stage_map`.
  Observed by AC32.
- **S34** — id 53. The anchor check's false-red rate re-measured. The pass counts the tracked specs and
  brief records under `memory/builds/` holding a backticked `blob:`, `record:` or `cmd:` span, renders a
  builder work order handing each such file of this build as `input:spec` through `TOOL-dBoundRoles-41`'s
  graded text, and records both counts in its ledger; one handing unit 24's spec renders. Observed by AC34.
- **S35** — id 54. One allowance block, named. Unit 7's `readWorkOrderAllowance` reads the `### allowance`
  heading of the task section outside every fence, walked by `TOOL-dBoundRoles-38`'s `readUnfencedLines`:
  more than one denies the write, naming the count, and one inside a handed block's fence is content; the
  plant `allowance-shadowed` holds it. Observed by AC35.
- **S36** — id 55. Framing fields cannot forge executor lines. Before `--framed-by` places a framing field,
  the render refuses it when any line matches `^#{1,3} `, `FACT_RE`, `MARKER_RE` or `^Framed by:`, naming the
  field and the line. Unit 4 §5's "no new write path" is answered in its ledger. Observed by AC36.
- **S37** — id 57. The reviewers' step restores itself. `reviewer_merge.py`'s up restores every path from its
  before-image and exits 1 on any failure after the image is written, and its step row declares
  `resume = "atomic"` (§8 F11). Observed by AC37.
- **S38** — id 58. The house step re-runs over its partial state. `house_overlays_to_instructions.py`'s up
  skips a file whose unit already holds a byte-equal text, removes that file, and refuses only on a tag
  holding different text (§8 F12). Observed by AC38.
  **Readers:** by name: S10's three overlay readers and `tools/roles/render_agents.py:323-329`, whose
  self-test fixture writes one; READER NOT IN TREE: the step program, unit 19's · by value: S10's
  `render_role` read, until unit 19 re-points it to the level-5 unit.
- **S39** — id 59. A large work order keeps its allowance. `readWorkOrderAllowance` reads the transcript's
  first JSONL line whole up to 8 MiB, denying past it, and denies a typed agent whose first record does not
  parse rather than fall back to the class verdict. Unit 13's ledger answers its Migration's assumption of specs
  under 49152 bytes with the measured count. Observed by AC39.
- **S40** — id 60. A broken policy read never locks the driver out. `checkDriverRead` admits, with one
  witness line, when `readPolicy` throws or returns a refusal; a plant `policy-refusal` holds it (§8 F13).
  Observed by AC40.
- **S41** — id 61. Rule 7 is kept where the roles kit is absent. `spawn_guard_pack.py`'s up, on a
  target with the policy kit and no roles kit, exits non-zero naming the roles kit as rule 7's home and its
  install command, leaving `agent-cap.js` wired; its witness checks the same; a govkit case holds it.
  Observed by AC41.
  **Readers:** by name: `.claude/settings.json:9`, `tools/settings-merge.py:117` (`HOOK_MARKER`),
  `tools/hooks/kit.toml` and the rest unit 25 S8 lists; READER NOT IN TREE: the step program, unit 25's
  · by value: `.claude/settings.json`'s `Workflow|Agent` matcher, which runs the wired hook and rule 7.
- **S43** — id 64. The placement return is the scout's own. `tools/loop/placement.py place --return <file>`
  takes `--agent <agent-id>` and refuses unless the file equals that agent's last assistant text, found
  through S56's `resolve_agent_transcript`, and its `.meta.json` names `gov-orienter`. The build Skill's
  orientation step passes `--agent` (§8 F15). Observed by AC43.
- **S44** — id 15. The work order joins the read-key families. `"work-order"` is in
  `READ_FAMILIES["input"]` (unit 14 S4), not a `READ_KEYS` literal, and `gov-prompt-writer`'s `reads` is
  spelled `field.input.question, field.input.work-order`. Observed by AC44.
- **S45** — id 33. The driver cannot retype the work order. `handoff.py`'s `--input` admission refuses
  `work-order`, which only `render --for` fills. Observed by AC45.
- **S46** — id 14. The orienter's full template. `gov-orienter`'s `return` spells `outcome` with its closed
  set, `card`, and the four placement keys typed as `TOOL-dPlacedRequest-4` S3 and S4 spell them, and a return
  carrying all six validates. Observed by AC46.
- **S49** — id 18. The floor applies at unit 22's steps. `check_effort_floor` applies at steps 4 to 6 of unit
  22's effort order: the house file, the stage row's `effort` and the role's declared `effort`. Observed by
  AC49.
- **S50** — id 19. Every rule-6 change moves with the guard. `tools/roles/spawn-guard.js` carries unit 3's
  card binding, unit 13's fact re-cut and `TOOL-dBoundRoles-38`'s fence-aware readers, each with its planted
  payload in `spawn-guard.test.sh`. Observed by AC50.
- **S51** — id 20. The `none` roles at unit 9's pass. The roles `.claude/roles.json` gives `writes = none`
  after unit 1, `gov-session` included, are listed in this unit's ledger with what each writes in its
  workflow, and none writes a repository file. Observed by AC51.
- **S52** — id 29. Each role's headroom over the real block. For every role, `budget` less the bytes of
  `render_static_block` over the tree units 2 and 15 leave is recorded in this unit's ledger, and none is
  negative. Observed by AC52.
- **S53** — id 30. The blob key agrees with its precedent. `derive_fact_key`'s `blob12` for a file equals the
  first 12 hex digits `git hash-object` prints for its LF bytes, the call `verb_brief` makes at
  `tools/unattended/unattended.sh:13029`. Observed by AC53.
- **S54** — id 34. `handoff.py` keeps no vocabulary of its own. `TASK_FIELDS` is `lib.READ_FAMILIES["task"]`,
  and `INPUT_NAMES` is `READ_FAMILIES["input"]` less a named tuple of render-filled inputs,
  `RENDER_FILLED_INPUTS`, holding `work-order`. Observed by AC54.
- **S55** — id 39. One transcript reader. `load_agent_transcript` (`tools/roles/handoff.py:616`) also returns
  the first `user` record's text and the last assistant text; `check-return` reads through it, reads the
  marker with `extract_prompt_marker` and checks ids with `PATH_ID_RE`, and walks no JSONL of its own.
  Observed by AC55.
- **S56** — id 40. The transcript resolver is callable. `resolve_agent_transcript(session_dir, agent_id)` is a
  module-level function of `handoff.py` in place of the closure `read_transcript` (`handoff.py:825-828`), and
  `print_agent_lines`, `--framed-by` and S43 call it. Observed by AC56.
- **S57** — id 41. One copy of the session layout. `RUN_ID_RE`, `WORKFLOW_RUNS_DIR` and the session
  directory's derivation sit in `scratch-guard.js`'s exports; `format-guard.js` imports them in
  place of its own (`format-guard.js:101-103`), and `readWorkOrderAllowance` uses them. Observed by AC57.

## 3. Non-goals (OUT)

- Rewording the specs of units 1 to 26 (§4); S2 amends by M2's AMEND act.
- The HIGH findings: `TOOL-dBoundRoles-37` to `-42`, whose mechanisms S29 and S34 build on.
- The 11 minors of `TOOL-dBoundRoles-44`: ids 3, 5, 16, 17, 26, 28, 43, 48, 49, 51 and 62.
- The report's left-shift gates: the spec-lint joins, the build-order check, the checklist entries and
  the duplicate-constant gate. No clause of this build names them; the items' criteria and §7's arms are
  this batch's regressions.
- A shape binding for a `Workflow` call's roles: dWellOiledMachine's, per unit 16 §8 F3.

### Edges

- **consumes-from** `TOOL-dBoundRoles-1` — the merged roster and the reviewer files it removes (S15, S16, S28)
- **consumes-from** `TOOL-dBoundRoles-2` — `parse_return_template`, the shape table and `render_role` (S1, S7, S8, S13)
- **consumes-from** `TOOL-dBoundRoles-3` — `derive_allowance` and the card binding (S22, S50)
- **consumes-from** `TOOL-dBoundRoles-4` — `gov-prompt-writer`, `--framed-by` and its transcript read (S5, S36, S44, S45, S56)
- **consumes-from** `TOOL-dBoundRoles-5` — `check-return` and `roles.retries` (S21, S55)
- **consumes-from** `TOOL-dBoundRoles-7` — `readWorkOrderAllowance` (S35, S39, S57)
- **consumes-from** `TOOL-dBoundRoles-9` — the `none` class, whose population S51 re-derives
- **consumes-from** `TOOL-dBoundRoles-10` — `checkDriverRead`, `roles.no-spawn` and AC6 (S12, S19, S21, S40)
- **consumes-from** `TOOL-dBoundRoles-11` — its policy key, which S21 routes through `read_policy_setting`
- **consumes-from** `TOOL-dBoundRoles-12` — the orientation return and the placement step (S43, S46)
- **consumes-from** `TOOL-dBoundRoles-13` — `derive_fact_key` and the Migration's size claim (S39, S53)
- **consumes-from** `TOOL-dBoundRoles-14` — `READ_FAMILIES`, `extract_role` and the cited-but-undeclared join (S24, S25, S44, S54)
- **consumes-from** `TOOL-dBoundRoles-15` — the `budget` row, `render_static_block` and the charter read (S7, S21, S52)
- **consumes-from** `TOOL-dBoundRoles-16` — §8 F3, under which S2 answers unit 25's AC3
- **consumes-from** `TOOL-dBoundRoles-18` — the reviewers' step program (S10, S17, S23, S37)
- **consumes-from** `TOOL-dBoundRoles-19` — the house step and its seed rule (S9, S38)
- **consumes-from** `TOOL-dBoundRoles-20` — the composition and the repository role's tag (S11, S24, S25)
- **consumes-from** `TOOL-dBoundRoles-21` — `read_policy_setting` and the `gates` field (S6, S21)
- **consumes-from** `TOOL-dBoundRoles-22` — the stage rows and the effort order (S32, S49)
- **consumes-from** `TOOL-dBoundRoles-23` — `check_effort_floor` (S49)
- **consumes-from** `TOOL-dBoundRoles-24` — the anchor check (S34)
- **consumes-from** `TOOL-dBoundRoles-25` — the pack, the retirement and its step (S2, S19, S27, S28, S41, S50)
- **consumes-from** `TOOL-dBoundRoles-26` — the refusal arm (S5, S13, S14)
- **consumes-from** `TOOL-dBoundRoles-37` — `derive_roles_expected`, whose docstring S29 writes
- **consumes-from** `TOOL-dBoundRoles-38` — `readUnfencedLines`, which S35 walks
- **consumes-from** `TOOL-dBoundRoles-39` — the route test in `check-return`, which S55's transcript read serves
- **consumes-from** `TOOL-dBoundRoles-41` — the graded text (S34)
- **consumes-from** `TOOL-dBoundRoles-42` — the class table, whose count and spec-token rows S27 and S28 dispose
- **hands-off** `TOOL-dBoundRoles-50` — §7, S41's lines, S2's rev bump and S34's counts, which unit 50 completes (ids 4, 5, 6, 22, 29, 30)
- **hands-off** `TOOL-dBoundRoles-58` — S56's `resolve_agent_transcript`, into which unit 58 folds unit 50's second resolver (id 25 of the round-1 audit of units 45 to 51)

## 4. Design

### Why two units

M6 admits two batches with disjoint write sets that neither read each other's writes as a contract or
acceptance input nor share a mutable record. This unit holds every item writing or reading the roles kit,
hooks, govkit steps and self-test, playbook extractor or `tools/loop/placement.py`, and the registry items
reading those outputs: S16 greps what S5, S6 and S13 render, S27 counts S50's suite, S2 and S28 sit with
S50's guard. `TOOL-dBoundRoles-44` holds the docs, Skills, hygiene check, gotcha pages, dead-path rows,
workflows suites' role maps and build README. The Files touched lists share no path; unit 44 reads the
base tree and names the hook files by a path nothing here moves. Neither touches `memory/DECISIONS.md`,
a backlog shard, the run-state file or a generator with its index.

### How an item closes

The batch builds after the units it repairs. Each item states the built tree's end state; the pass does
what is missing or records that a landed unit left it. A contradicted landed criterion (S2, S10, S11) is
answered AMENDED in that unit's ledger; only S2 revises a spec.

### The slot rule S11 states

```
tag role.<slot>          a gov role, slot = the role file's stem
tag role.adopter.<name>  a repository role, slot = <name>; refused where <name> is a gov slot
```

A slot is an agent type and reaches paths, so it satisfies `PATH_ID_RE` (`tools/roles/handoff.py:121`),
which a dot fails.

### Inventory

Minted: the shapes `int`, `tag` and `choice`; the tag rule of S11; `rekey` as a mode of
`write_overlay_units`; the plants `allowance-shadowed`, `policy-refusal` and `role-rows-adopter`; the
govkit cases `reviewer-merge-carriers` and the roles-kit-absent case of S41; `RENDER_FILLED_INPUTS`;
`resolve_agent_transcript`; and the `--agent` flag of `placement.py place`. Each function and constant is asked of `python tools/lexicon/lexicon.py --suggest
<name>` with its `--as` cell.

### Migration

An adopter's one-value `outcome` set becomes legal (S1); its `method-carriers.txt` is re-keyed by the
reviewers' step (S17). No other stored data changes.

### Rollout

Live at landing, at order 28, after every unit it repairs.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/role-schema.toml`
- `tools/roles/check_roles.py`
- `tools/roles/render_agents.py`
- `tools/roles/handoff.py`
- `tools/roles/agents/gov-prompt-writer.agent.md`
- `tools/roles/agents/gov-orienter.agent.md`
- `tools/roles/README.md`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/spawn-guard.js`
- `tools/roles/spawn-guard.test.sh`
- `tools/roles/SKILL.template.md`, rendered to `.claude/skills/build/SKILL.md`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/format-guard.js`
- `tools/govkit/selftest.py`
- `tools/govkit/steps/reviewer_merge.py`
- `tools/govkit/steps/house_overlays_to_instructions.py`
- `tools/govkit/steps/spawn_guard_pack.py`
- `tools/playbook/overlay.py`
- `tools/playbook/tag_index.py`
- `tools/playbook/namespaces.toml`
- `tools/playbook/gov_tag.py`
- `tools/loop/placement.py`
- `memory/project/method-carriers.txt`
- `memory/project/testsuite-count-waivers.txt`
- `memory/project/spec-token-waivers.txt`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md`

### Alternatives rejected

- **A cut between code and records.** S16, S27 and S28 read the code's outputs (§4).
- **Folding each fix into its unit's spec now.** M4 refuses a fold at the exit.

## 5. Production-readiness checklist

- security — S35, S36, S39 and S43 narrow forging and fall-back paths; S40 lets the driver repair a broken
  policy; S41 refuses rather than drop a guard. No new write path but S23's mode.
- perf / scale — S39 reads a first record of at most 8 MiB; the rest are greps and existing reads.
- error / empty / loading states — S37 and S38 recover after a kill; S40 states a throw's verdict.
- observability — every new refusal names its rule, field or line.
- risks — S2 amends a criterion of unit 25.
- testing — by probe, grep, fixture, plant or a one-case slice; the arms of §7 at the close.
- migration — as §4 says.
- user docs — `help/roles.md` is `TOOL-dBoundRoles-44`'s; no item here changes a page.

## 6. Acceptance criteria

The slice below is
`python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.<case function>(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`,
from the repo root: one govkit case function, no suite.

- **AC1** — When `python tools/roles/check_roles.py` runs over gov's built tree it exits 0, and
  `python -c "import roles_lib as r; print(r.parse_return_template('outcome:done'))"` in `tools/roles/` prints
  one entry whose type is the one-value tuple `('done',)`.
  Red when: R2 refuses a set of one, so the five templates red.
- **AC2** — When `grep -n 'AC3' <unit 25's acceptance ledger>` runs, its answer is AMENDED naming the
  revision, unit 25's §9 logs it naming id 2, and the moved spawn guard exits 2 on a `Workflow` payload whose
  `args.roles` names a role that is not agent-true.
  Red when: AC3 is answered OBSERVED with no refusal behind it.
- **AC5** — When the prompt writer's role file is read, the `outcome` set of its `return:` line holds no
  `refused`, and `check_roles.py` over gov's tree exits 0.
  Red when: the role redeclares the arm, or the checker admits it.
- **AC6** — When a probe compares each rendered agent file's `gate legs:` line under `## Ceiling` with
  `.claude/roles.json`'s `gates` for that slot, every pair is equal and `gov-builder`'s is not `none`.
  Red when: the ceiling reads the moved house row and renders none.
- **AC7** — When `python -c` calls `roles_lib.load_role_schema()` it returns a `budget` row with shape `int`
  and required `every`, and `grep -n '"budget"' tools/roles/roles_lib.py` prints no tuple literal.
  Red when: the row carries `type`, or `budget` is typed beside the schema.
- **AC8** — When `python -c` loads every role-schema row through `load_role_schema`, none raises `RolesError`
  and each row's shape keys the README's shape table.
  Red when: a later row names a shape the table lacks, so every roles run refuses at load.
- **AC9** — When a probe reads unit 19's step row in `tools/roles/kit.toml`, its `surfaces` equal one `file:`
  member per `house/*.md` that file's seed row lists as `git show` prints it at unit 19's parent.
  Red when: the step names a typed ten and leaves unit 1's overlays seeded.
  figure: DERIVED from the parent commit at observation time.
- **AC10** — When the reviewers' step's up runs on a fixture target whose old diff reviewer's house file holds
  one line, its overlay gains a level-5 unit selecting `role.gov-reviewer` holding it, and the merged role's
  re-rendered agent file carries it between `<!-- gov:repo -->` and its close.
  Red when: the text is appended to a house file no render reads.
- **AC11** — When `check_roles.py` and the index render run in unit 20's fixture, `.claude/roles.json` keys
  the repository role `triager`, `check_item_roles` resolves `role:triager`, and a repository role named
  `gov-builder` is refused.
  Red when: the index, the actor and the tag spell the slot two ways.
- **AC12** — When `grep -n 'recorded-stand-in' tools/roles/adopt-roles.test.sh` runs, it names the stand-in
  case, and `handoff.py render --stand-in` in a fixture with `roles.no-spawn` unset exits non-zero naming it.
  Red when: the stand-in case leans on the old default.
- **AC13** — When `grep -c "outcome: refused"` runs over every file under `.claude/agents/`, each counts 1,
  and `grep -n "outcome: refused" tools/roles/render_agents.py` prints nothing.
  Red when: the arm is appended outside `render_role`, unseen by R5 and the role-sha.
- **AC14** — When a probe extracts `## Return` from `.claude/agents/gov-builder.md` and from
  `handoff.py render --role gov-builder --build tFix --stdout`, they are byte-equal, and
  `handoff.py render --role gov-session … --stdout` carries `outcome: refused` once.
  Red when: the two routes compose different return blocks.
- **AC15** — When `grep -c -E 'gov-(spec|diff)-reviewer' memory/project/method-carriers.txt` runs, it prints
  0. Red when: a declared carrier names a file that is gone.
- **AC16** — When `comm -23` compares the sorted output of `grep -l BUILD-METHOD .claude/agents/*.md` with the
  sorted first fields of `memory/project/method-carriers.txt`, it prints nothing.
  Red when: a rendered agent file names the method undeclared.
- **AC17** — When the slice runs the `reviewer-merge-carriers` case, whose up meets a registry naming both old
  types, the registry holds one row for the merged role's agent file, the down restores it byte-identical,
  and `FAILURES` prints empty.
  Red when: the adopter's registry keeps a row for a deleted type.
- **AC19** — When `git grep -n -E "policy\.toml|\.governance/"` runs over `tools/hooks/scratch-guard.js` and
  the roles pack's spawn guard, it prints only `readPolicy`'s import and locator lines; over a scratch copy
  that reads the policy file with `fs` it prints that line too.
  Red when: a hook parses the policy file beside the reader.
- **AC21** — When `git grep -n -E "policy\.py.*get|from policy import|import policy" -- 'tools/roles/*.py'`
  runs, it prints only lines inside `read_policy_setting`.
  Red when: a second policy reader exists in the roles kit.
- **AC22** — When `git grep -n "^WRITE_FOLDERS = " -- tools/roles` runs it prints one line, in
  `tools/roles/roles_lib.py`, and `grep -n "import check_roles" tools/roles/roles_lib.py` prints nothing.
  Red when: the library imports its importer, or the folders are copied.
- **AC23** — When the reviewers' step program is read, only its `write_overlay_units` call opens the overlay
  for writing, and that function in re-key mode on a fixture overlay with a refused value leaves the file
  byte-identical.
  Red when: the step writes the overlay through a second writer.
- **AC24** — When the tag fixture runs with `--plant role-rows-adopter`, the index holds
  `role.adopter.triager`.
  Red when: an overlay role row yields no tag.
- **AC25** — When the plant's actor patch cites `role.adopter.triager`, the cited-but-undeclared join is
  green; with the overlay row removed it reds naming the citation's path and line.
  Red when: an adopter role citation reds while declared, or passes while undeclared.
- **AC27** — When `grep -c 'agent-cap.test' memory/project/testsuite-count-waivers.txt` runs it prints 0, and
  the pack's suite holds a `PASS ($n assertions)` line beside its `FLOOR_ASSERTIONS`.
  Red when: the waiver names a suite no leg runs, or the new suite prints no count.
- **AC28** — When `memory/project/spec-token-waivers.txt` is read, it holds one row per retired hook path
  and one for the old diff reviewer's house file, each reason naming the citing specs.
  Red when: a live spec's citation of a deleted file has no row.
- **AC29** — When `grep -n -E 'nine agent types|ten seeded' tools/govkit/selftest.py` runs it prints nothing.
  Red when: the docstring keeps the counts the code no longer types.
- **AC32** — When `git grep -n '\.get("stages")' -- tools/roles` runs it prints only lines inside
  `load_workflows`, and `python tools/roles/handoff.py stage-efforts build` in the roles fixture exits 0.
  Red when: a reader still needs the inline table, so `stage-efforts` refuses every workflow.
- **AC34** — When this unit's ledger is read, it holds the two counts of S34, and
  `handoff.py render --role gov-builder --input spec=<unit 24's spec> --stdout` exits 0 in the roles fixture.
  Red when: a work order handing spec 24 refuses on its own grammar spans.
- **AC35** — When the `allowance-shadowed` plant hands a spec whose fenced content holds a wider
  `### allowance`, the narrower authored block governs; with a second authored block outside every fence the
  write is denied naming the count.
  Red when: a first-match reader takes a shadow block.
- **AC36** — When `--framed-by` reads a fixture return whose `job` holds a `### allowance` line and a fact
  line, the render exits non-zero naming `job` and the first offending line.
  Red when: a framing field places an executor-shaped line in the hashed task.
- **AC37** — When the slice runs S37's case, stubbing `render_agents.py` to exit 1 during the reviewers' up,
  every before-image path is byte-identical and the up exits 1; a re-run without the stub completes.
  Red when: a failure after re-keying leaves the target half-migrated.
- **AC38** — When the house step is killed after writing a unit and before removing its file, a re-run
  completes and `witness` exits 0; with the unit's text changed, the re-run refuses naming the tag.
  Red when: the step refuses its own partial state.
- **AC39** — When `readWorkOrderAllowance` reads a fixture transcript whose first record is 300 KB with an
  allowance block at its end, the allowance narrows the write; with that record truncated mid-JSON the write
  is denied for the typed agent.
  Red when: a large work order falls back to the class verdict.
- **AC40** — When the `policy-refusal` plant makes `readPolicy` throw, `checkDriverRead` admits a `Read` and
  prints one witness line.
  Red when: a broken mirror locks the driver out of the reads that repair it.
- **AC41** — When the slice runs S41's case, an up on a target with the hooks and policy kits and no roles
  kit, it exits non-zero naming the roles kit and its install command, and `.claude/settings.json` still
  wires the retired hook.
  Red when: the up drops rule 7 with a witness that exits 0.
- **AC43** — When the placement verb runs with
  `--return <hand-written file> --agent <a gov-orienter agent id>`, it refuses naming the byte mismatch; with
  the agent's own last text it records the placement.
  Red when: driver-typed text becomes an agent placement.
- **AC44** — When `python -c` calls `roles_lib.parse_read_key('field.input.work-order')` it returns
  `('input:work-order', False)`, and the prompt writer's role file spells `field.input.work-order` on its
  reads line.
  Red when: the work order is a literal beside the families.
- **AC45** — When `handoff.py render --role gov-researcher --input work-order=x` runs, it exits non-zero
  naming `work-order`.
  Red when: the driver can retype the work order.
- **AC46** — When `validate_return("gov-orienter", text)` checks a return carrying `outcome`, `card` and the
  four placement keys, it returns no defect, and `parse_return_template` over the role's `return` lists all
  six.
  Red when: the template drops `outcome` or `card`.
- **AC49** — When R12 runs over a fixture whose `build` stage row sets `effort = "low"` and no policy key, it
  reds naming the floor.
  Red when: the floor misses the stage row's step.
- **AC50** — When the pack's `spawn-guard` hook reads a payload whose card binding is broken, one whose handed
  spec moved after rendering, and one quoting a marker inside its fence, it denies the first two and admits
  the third.
  Red when: a rule-6 change was left behind in the deleted hook.
- **AC51** — When `python -c` lists the slots `.claude/roles.json` gives `writes` `none`, the list equals the
  one in this unit's ledger.
  Red when: the population is the base tree's.
- **AC52** — When a probe prints `budget - len(render_static_block(...))` per role over the built tree, no
  value is negative and each is in this unit's ledger.
  Red when: a role's block exceeds its budget unseen.
- **AC53** — When `python -c` compares `roles_lib.derive_fact_key` on a scratch LF file with `git hash-object`
  on it, the first 12 hex digits agree.
  Red when: the key and its precedent hash differently.
- **AC54** — When `grep -nE '^(TASK_FIELDS|INPUT_NAMES) = \(' tools/roles/handoff.py` runs it prints nothing,
  and `grep -n 'RENDER_FILLED_INPUTS' tools/roles/handoff.py` names the tuple.
  Red when: `handoff.py` keeps a literal vocabulary.
- **AC55** — When `python -c` calls `load_agent_transcript` on a fixture transcript, the result holds the
  first user record's text and the last assistant text, and `check-return`'s body holds no `json.loads` of its
  own.
  Red when: two readers walk one transcript.
- **AC56** — When `grep -n "def read_transcript" tools/roles/handoff.py` runs it prints nothing, and
  `grep -n "^def resolve_agent_transcript" tools/roles/handoff.py` prints one line.
  Red when: the resolver is still a closure.
- **AC57** — When `grep -nE "^const (RUN_ID_RE|WORKFLOW_RUNS_DIR) " tools/hooks/format-guard.js` runs it
  prints nothing, and `node -e` requiring `tools/hooks/scratch-guard.js` reads both names from its exports.
  Red when: the layout is typed twice.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `template size <=48KiB` · `memory hygiene` · `method carriers (every pointer declared)` · `testsuite counts (every bar self-test prints one)` · `playbook render selftest` · `check-wiring self-test` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC12 AC34 AC36 AC45 · the stand-in per `roles.no-spawn` value, a render handing spec 24, a forged framing heading and a CLI `work-order`, staged by a `render_handoff` admitting a forged field · none
New arm: tools/hooks/scratch-guard.test.sh · covers AC35 AC39 AC40 · `allowance-shadowed`, a 300 KB first record and `policy-refusal`, staged by a first-match allowance reader · none
New arm: tools/govkit/selftest.py · covers AC17 AC37 AC38 AC41 · `reviewer-merge-carriers`, a stubbed render failure, a killed house step and a roles-kit-less target, staged by an up that skips its restore · none
New arm: tools/roles/spawn-guard.test.sh · covers AC50 · the card-binding, moved-fact and fenced-marker payloads, staged by a pack without the fact re-cut · `FLOOR_ASSERTIONS` raised

## 8. Open questions

F9 and F14 moved to `TOOL-dBoundRoles-44` with S31 and S42.

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause; veto 1 discards (b). RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens:
  none · relaxes: none
- **F2 — One-value sets, or a second outcome for five roles (id 1)?** Options: (a) admit a set of one; (b) a
  second outcome per role, which no `returns` sentence names. RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 3, fewest follow-ups. widens: none · relaxes: none
- **F3 — Build the shape refusal, or amend unit 25 AC3 (id 2)?** Options: (a) refuse a role lacking the
  harness's kind, re-opening unit 16 §8 F3, which M7 forbids; (b) amend AC3 to the moved rule's refusal.
  RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the one survivor. widens: none · relaxes: none
- **F4 — Which shapes join unit 2's table (ids 8, 32)?** Options: (a) `int`, `tag` and `choice`; (b) one shape
  per key. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F5 — Where does the prompt writer's refusal live (id 6)?** Options: (a) unit 26's arm, its own `refused`
  dropped; (b) its own copy, which unit 26 §4 forbids. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F6 — The repository slot's spelling (id 11)?** Options: (a) `adopter.<name>`, which fails `PATH_ID_RE`;
  (b) the bare `<name>` with §4's tag rule; (c) `adopter-<name>`, changing the `role.adopter.<name>` form
  units 14 and 20 hand off. RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the one survivor. widens:
  none · relaxes: none
- **F7 — Fix the stand-in case in the suite or in unit 15's AC (id 12)?** Options: (a) the fixture sets
  `recorded-stand-in`, a sibling case asserting the default; (b) amend unit 15 AC2, the default untested.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F8 — A re-key mode in the one writer, or a second door (id 37)?** Options: (a) a mode of
  `write_overlay_units`; (b) a sibling function; (c) the step's own edit; (b) and (c) are second writers
  PLAY-dOrderedCharter-32 S8 rules out. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none ·
  relaxes: none
- **F10 — Name the heading, or require exactly one (id 54)?** Options: (a) the heading in the `boundaries`
  slot, a name unit 23 owns; (b) one heading outside every fence, deny on more. RESOLVED (agent, 2026-10-26,
  delegated): (b), rung 3, on `TOOL-dBoundRoles-38`'s walker. widens: none · relaxes: none
- **F11 — Atomic, or a resume over the after-state (id 57)?** Options: (a) `resume = "atomic"` with a restore
  on failure; (b) a hash per carrier per step against the after-state. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F12 — Skip equal units, or atomic (id 58)?** Options: (a) skip a byte-equal unit and remove its file, as
  the row promises; (b) `resume = "atomic"`. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens:
  none · relaxes: none
- **F13 — On a policy refusal, admit the read or refuse search tools (id 60)?** Options: (a) admit with a
  witness; (b) refuse `Grep` and `Glob` on a fault not the driver's. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F15 — `--from-agent` in place of `--return`, or `--agent` beside it (id 64)?** Options: (a) replace
  `--return`, changing `TOOL-dPlacedRequest-4` S1's interface; (b) bind it with `--agent`. RESOLVED (agent,
  2026-10-26, delegated): (b), rung 3, additive. widens: none · relaxes: none
- **F16 — Waive or reword the citations of deleted files (id 45)?** Options: (a) spec-token waiver rows; (b) a
  basename, red once the files are gone, or prose, rewriting other builds' criteria. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 26 unit specs: 34
  MEDIUM and 12 LOW findings, each its own scope item; the other 11 minors are `TOOL-dBoundRoles-44`'s.
- rev-2 · 2026-10-26 · §3 · edge to TOOL-dBoundRoles-50, the round-1 minors of units 37 to 44; reworded
  for size, nothing moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-58, the minors batch of the round-1 audit of units 45 to 51; nothing else moved.

## 10. Reuse audit

Each item extends the seam its §2 entry names.
`python tools/codebase-map/reuse_lookup.py "one reader of a value shared by several kits instead of a copy per caller"`
ranked only generic stems and the kit locator (`read`, `read_text`, `kit_rel`, `resolve_kit_dir`), so no seam fits beyond those.

Recall terms used: `python tools/memory-recall/query.py "which minor defects of the roles build specs need a second reader or writer removed" --terms "read_policy_setting WRITE_FOLDERS write_overlay_units load_agent_transcript READ_FAMILIES method-carriers dead-path waiver gotcha"`
