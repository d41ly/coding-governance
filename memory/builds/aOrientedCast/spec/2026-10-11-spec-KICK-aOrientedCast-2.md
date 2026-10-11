# KICK-aOrientedCast-2 — the attended router: after kickoff's go, `/build` drives a code build through the harness pipeline

**Status:** OPEN · rev-2 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams kickoff · order 6 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md) | research | KICK-aOrientedCast-1 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-1 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-1 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md) | journal | KICK-aOrientedCast-1 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-1 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md) | journal | PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 |

<!-- /gen:spec-records -->

## 1. Goal

An attended session that reaches kickoff's READY card and the owner's go has no route into the
harnesses an unattended run uses, so it writes specs and code inline. This unit ships the route: a
`/build` Skill, rendered by the roles kit, that walks the catalogue's workflows in stage order, hands
every agent a rendered role, and points at the carriers `/unattended` already follows instead of
copying them; and one clause in the kickoff engine's Step 5 that hands a code build to it.

## 2. Scope (IN)

- **S1** — A Skill template `tools/roles/SKILL.template.md` in the roles kit: front matter
  `name: build` and a `description`, the kit marker line, and a body routing the stages §4 "The
  Skill" lays out, each a `## Stage <n> — <workflow>` heading. Observed by AC3, AC4, AC5, AC11 and
  AC12.
- **S2** — `tools/roles/adopt-roles.sh`, the kit's adopter, created here with two modes. `--scaffold`
  renders the template to `.claude/skills/build/SKILL.md` and prints the path. `--check` renders in
  memory and byte-compares with the file on disk, carriage returns stripped from both sides, exiting 1
  and naming the path on a difference or an absent render. Any other argument exits 2
  with usage. Observed by AC1.
- **S3** — The render substitutes three tokens by their literal spellings: `{{KIT_DIR}}` and
  `{{TOOL_ROOT}}`, derived by the `.git` walk the unattended adopter uses, and `{{MEMORY_ROOT}}`, read
  from `.memory-tree.conf`. An empty derivation, an absent conf or a blank key exits 2 naming it; a
  `{{` surviving the substitution exits 1 naming its line. Observed by AC1 and AC2.
- **S4** — The render binds the Skill's stages to the catalogue. Each `## Stage <n> — <workflow>`
  heading must name a `[[workflow]]` of `tools/roles/workflows.toml` whose `stage` is `<n>`; the
  headings must run in strictly ascending stage order; and every catalogue workflow of stage 1 or more
  must be named by exactly one heading. A catalogue the reader parses zero workflows from exits 2 as a
  dead probe; any other disagreement exits 1 naming the heading and the entry. Both modes run it.
  Observed by AC2.
- **S5** — Gov's own render is committed, and `.gitattributes` pins the rendered Skill and its template
  `eol=lf`. Observed by AC1 and AC9.
- **S6** — The kickoff engine's Step 5 changes in two places and nowhere else. The hand-typed field
  list in its READY-card sentence becomes a pointer to every field `--task-skeleton` prints. One
  sentence follows the route sentence: on go, a code build continues in `/build` where the project
  ships it. The engine stays under its 18432-byte ceiling and its READY prompt string stays on one
  physical line. Observed by AC6.
- **S7** — `memory/guides/SESSION-KICKOFF.md` §B gains one bullet naming `/build` as the attended
  route, and its `last-audit` and `last-body-change` stamps move, with a delta line in the commit
  message. Observed by AC7.
- **S8** — The roles kit's dossier claims the `rendered-skills` key `build` and its prose names the
  Skill and its adopter; the generated map artifacts are regenerated for the adopter's shell function.
  Observed by AC8.
- **S9** — The roles kit's README gains a section on the Skill: what renders it, its three tokens, the
  stage binding and the session-restart note. NOT OBSERVED by a criterion: prose, read by the review
  against §4.

## 3. Non-goals (OUT)

- The reuse scout's trigger and the card's `## reuse` section, which belong to aScoutedSeam. `/build`
  reads that section when it is present and spawns no scout, §8 F2.
- The agent-type render inside the adopter, the descriptor's `rendered` row and placeholder list, the
  adopter's gate leg and the wiring check's report. All are `TOOL-aOrientedCast-8`'s; this unit lands
  the adopter with the Skill alone.
- `/unattended`'s own Skill and verbs text. Changing how an unattended run composes its harness calls
  is `TOOL-aOrientedCast-9`'s, which the M2 cross-read added for it.
- A size ceiling and gate leg for the rendered Skill. AC11 measures it once; a declared row would need
  a manifest leg and a deployer exemption inside `TOOL-aOrientedCast-8`'s write set.
- Splitting the kickoff engine, which the open ask `KICK-aReplayedCard-5` proposes for the edit after
  the headroom runs out. This edit fits and leaves 122 bytes.
- Any edit to Steps 0 to 4 or Step 5b of the engine.
- Landing. Merge and push stay the owner's explicit asks in an attended session.
- The spawn guard that admits the Skill's harness calls and spawns. `TOOL-aOrientedCast-7` owns it,
  and its Rollout section names this unit as a precondition of its landing; the Edges below carry the
  hands-off.

### Edges

- **consumes-from** `TOOL-aOrientedCast-1` — the workflow catalogue's names, stages and order, which
  the Skill's headings walk and the render binds to. Without it S4 has nothing to read.
- **consumes-from** `KICK-aOrientedCast-1` — the card's complete eight-field task section the Skill's
  precondition reads, and Step 5's stale field list it hands to this unit.
- **consumes-from** `TOOL-aOrientedCast-2` — the render verb with its task part and the
  harness-arguments verb, which every agent prompt and every harness call the Skill orders is composed
  from.
- **consumes-from** `TOOL-aOrientedCast-4` — the build harnesses' roles argument and the unit
  harness's diverged field, which the per-unit loop branches on.
- **consumes-from** `TOOL-aOrientedCast-5` — the review harness's roles argument, which the closing
  review step passes.
- **hands-off** `TOOL-aOrientedCast-8` — the agent-type render inside the adopter, its registration
  and placeholder declaration, the gate leg over its check mode, and the regression arms for the
  stage binding and the surviving-token refusal.
- **hands-off** `TOOL-aOrientedCast-7` — the spawn guard, which admits only the rendered handoffs and
  the harness calls carrying `roles` that this Skill composes, and refuses every other route.
- **hands-off** external — aScoutedSeam's kickoff unit, whose opt-in spawns the scout and writes the
  card's reuse section that the Skill's stage 2 reads when present.

## 4. Design

### Evidence

Read at HEAD `744e55db` of the run branch, whose `tools/`, `skills/`, `.claude/` and `memory/guides/`
trees equal base `646d4a73`.

- `tools/unattended/adopt-unattended.sh` renders `.claude/skills/unattended/SKILL.md` from
  `tools/unattended/SKILL.template.md` with no argument and verifies it with `--check`, CR-normalised
  on both sides, and carries no `fail()` helper because `check-arms.py` would grade a script defining
  one as a gate (its header). Its `.git` walk (lines 62-75) derives the kit's repo-relative path and its
  `TOOL_ROOT` (lines 116-117); its render (lines 423-462) substitutes each `{{TOKEN}}` literally with a
  sentinel against trailing-newline loss. The unattended template names a sibling kit as
  `{{TOOL_ROOT}}workflows/unattended-build.js`, which the install-prefix gate drains.
- `tools/workflows/unattended-build.template.js` accepts `mode: "attended"` (line 419), requires a
  `planState` on every `units[]` entry in that mode (line 2143), and hands back `dispatch` with
  `scriptPath`, `args`, `perUnit` (`unitId`, `specPath`, `briefPath`) and `resolvePathsWith`, the plan
  verb with `--paths` (lines 2268-2281). `tools/workflows/unattended-unit.js` tells an attended child
  not to call `--dispatch`, `--brief` or `--rescope`.
- `bash tools/unattended/unattended.sh --plan aOrientedCast --paths` runs with no run-state file
  read or written, and prints one `<id> TAB <spec path or -> TAB <state>` row per unit, a roster line and a
  `next:` line. Measured 42 s on node a, 2026-10-11, PINNED at that read.
- `memory/guides/UNATTENDED-VERBS.md` "While it runs", the bullet "Drive the build as ONE program",
  states the build-harness call's arguments; BUILD-METHOD M8 states the closing review's call.
- The kickoff engine is 18256 bytes, CR-stripped, against a ceiling of 18432 and a high-water of 18369
  (`tools/template-size-limits.txt`, `tools/template-size-highwater.txt`), PINNED at this read. Its Step 5
  lists four task fields by hand at lines 197-198. `tools/unattended/check-unattended.sh` and
  `tools/hooks/scratch-guard.test.sh` grep the READY prompt string as one fixed string on one line
  (gotcha `reflowed-prompt-string-reads-as-a-deleted-stop`), and the scratch-guard suite's span
  extractor reads Steps 0 to 4 only.
- `memory/guides/SESSION-KICKOFF.md` watches `skills/session-kickoff/SKILL.md`, so staging it owes a
  `last-audit` stamp; a §B edit owes `last-body-change` too (memory note "stamps are not one stamp").
- The map's `rendered-skills` set is every `SKILL.md` under `.claude/skills/`
  (`tools/codebase-map/map_extractors.py:213-215`), so a new Skill is an unclaimed key until a dossier
  claims it. A new shell function lands in the generated symbol map.
- The role catalogue (`TOOL-aOrientedCast-1`) gives the workflows `orient` 1, `reuse` 2, `spec-write`
  3, `spec-review` 4, `build` 5, `closing-review` 6 and `gate-bar` 7, and `research`, `handoff` and
  `bookkeeping` stage 0. Its `gov-spec-writer` reads five required `brief:` sub-heads, `input:spec?`,
  `task:reuse?` and `card:route?`, and no `input:question`.
- The renderer (`TOOL-aOrientedCast-2`) refuses an `--input` its role does not read, takes the brief
  record from `--input prompt=`, and otherwise picks the one record carrying both `## The prompt` and
  `## The brief`. Its `harness-args tier2-review` prints the union of the two review workflows' stages.
- The unit harness (`TOOL-aOrientedCast-4`) returns `diverged: true` when its builder stops on a
  `DIVERGENCE:` reason, and the write gate (`TOOL-aOrientedCast-6`, its S4) admits from the main loop an
  edit that changes only a spec's status and date cells.

### The adopter, in this unit's scope

| Mode | Writes | Exit |
|---|---|---|
| `--scaffold` | the rendered Skill | 0 rendered; 1 a token survived or a stage disagrees; 2 a derivation or the conf failed |
| `--check` | nothing | 0 fresh; 1 stale, absent, a surviving token or a stage disagreement, each named; 2 as above |
| anything else | nothing | 2, usage |

One shell function, `render_skill`, prints the render to standard output; both modes call it, and the
stage binding runs inside it, so `--check` grades exactly what `--scaffold` would write. The catalogue
is read with `awk` over its `[[workflow]]` blocks, taking each block's `name = "…"` and `stage = <n>`
lines; a block missing either is a disagreement named by its line. The adopter spells no install
prefix and defines no `fail()`. On a `--scaffold` that creates the Skill it prints one line saying a
session started before this write may not list `/build` until it restarts; whether a running session
picks up a new Skill is UNVERIFIED on this CLI, and the line states the conservative rule.

### The Skill

The template, which the builder writes to these sections and pointers. `handoff.py` is
`python {{KIT_DIR}}/handoff.py`, and `unattended.sh` is `bash {{TOOL_ROOT}}unattended/unattended.sh`.

```markdown
---
name: build
description: Drive an ATTENDED code build through the harness pipeline an unattended run uses - spec writers, the spec audit where the owner declared one, one builder per unit, the closing review and one bar - with every agent spawned as its rendered role. Use after /session-kickoff's READY card and the owner's go, for a build that writes product code. Do NOT use for a run that merges and pushes with no owner turn, which is /unattended, or for a change that writes no product code.
---
<!-- gov:kit roles@<the version the kit descriptor declares when this unit builds> -->

# Attended builds

This Skill is a ROUTER. The procedure is `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md`: read it WHOLE
before stage 3, and it wins any difference. The stages below are the workflows of
`{{KIT_DIR}}/workflows.toml`, in its stage order.

## Before stage 3

- The orientation card carries a READY line and a `## task` whose eight fields are filled, the brief
  sits under `{{MEMORY_ROOT}}/builds/<slug>/prompts/`, and the owner's go is quoted under its
  `## Owner confirmation`. Any of the three missing: stop, and run `/session-kickoff`.
- No run-state file exists, so this run is ATTENDED: the one driver verb used is
  `unattended.sh --plan <slug> --paths`. Merge and push each wait for the owner's explicit ask.
- A fork goes to the owner through `AskUserQuestion`, never to a park: no mandate delegates it (M3).
- You write no freeform agent prompt. A direct spawn is an `Agent` call whose `subagent_type` is the
  role and whose `prompt` is the output of `handoff.py render --role <role> --build <slug> --unit <id>
  --input <key>=<value> --part task`, unchanged. Every harness call carries `roles`, the JSON
  `handoff.py harness-args <harness>` prints.

## Stage 1 — orient

`/session-kickoff` ran it; nothing runs here.

## Stage 2 — reuse

A card carrying a `## reuse` section had its scout run at kickoff, and the spec writers read it.
Otherwise they read the card's `**Reuse:**` field. This Skill spawns no scout.

## Stage 3 — spec-write

Read `unattended.sh --plan <slug> --paths`, then call `{{TOOL_ROOT}}workflows/unattended-build.js` by
`scriptPath` as the verbs guide's "Drive the build as ONE program" bullet composes it
(`{{MEMORY_ROOT}}/guides/UNATTENDED-VERBS.md`), with these differences: `mode: 'attended'`; every
`units[]` entry carries its `planState` from that read; no `runStateExists`; `base` is the READY
line's; `roles` from `handoff.py harness-args unattended-build`; `specAudit` only where the build
README declares `spec-audit:`. Act on its `nextAction`.

## Stage 4 — spec-review

Stage 3's harness runs it as its AUDIT stage, and only where `specAudit` was passed (M4).

## Stage 5 — build

Until `--plan --paths` prints `next: none - every tracked spec is terminal`, for the next READY unit:

1. set its spec's status to INPROGRESS and its date to today, an edit touching nothing else: the
   owner's go is the approval INPROGRESS records;
2. append a `## route` naming the unit, as the brief skeleton's route lines say, through the kickoff
   check script's `--card --append`;
3. call the hand-out's `dispatch.scriptPath` with `dispatch.args` plus `unitId`, `specPath`,
   `briefPath`, and `roles` from `handoff.py harness-args unattended-unit`, on every dispatch;
4. on `diverged: true`, write a revision record under the build's `prompts/` holding `## The brief`
   and no `## The prompt`, its Goal the builder's `why` verbatim and its other four sub-heads copied
   from the build's brief; spawn `gov-spec-writer` on it with `--input spec=<path> --input
   prompt=<that record>`; then dispatch the unit again. On any other `committed: false`, stop and bring
   the `why` to the owner.

## Stage 6 — closing-review

Call `{{TOOL_ROOT}}workflows/tier2-review.js` as M8 composes it, adding `roles` from
`handoff.py harness-args tier2-review`. Each blocker's fix is a pass of the unit it lands in: write
the finding into a fix record under `prompts/`, set that unit back to INPROGRESS by the same
status-only edit, and dispatch it with that record as `briefPath`. Then re-review the fix (M8).

## Stage 7 — gate-bar

`bash {{TOOL_ROOT}}run-gates/run-gates.sh`, once, after the last unit is terminal; the governing
doc's merge-bar section decides its flags.

## Wrap-up

M9's derivation. Then ask before any merge or push.

## Shared with /unattended

| Stage | Shared carrier | Here, and why |
|---|---|---|
| orient | `/session-kickoff` | it ran before this Skill; a mandated run runs it after preflight |
| spec-write, spec-review | the build harness, M4 | `mode: 'attended'`, because no run-state file exists |
| build | the unit harness, M6 | no recording verbs; the main loop flips INPROGRESS and routes each unit |
| closing-review | M8 | identical, roles included |
| gate-bar | the merge bar | the main loop runs it; under a mandate the run's close does |
| wrap-up | M9 | identical |
| landing | template §1 | the owner's ask; a mandate lands by its protocol |
```

The brief that the builder ships is this text, the marker line carrying the version the roles kit's
descriptor declares when this unit builds. The two records stage 5 and stage 6 write are journal
records bound by `**Serves:** journal <unit-id>` and named by the prompts-folder filename grammar
check 5 grades, `<date>-prompt-<unit-id>-<n>-revision-brief.md` and `…-fix-brief.md`.

### The engine edit

| Where | BASE | After |
|---|---|---|
| Step 5, the READY-card sentence | `` `## task` (the sealed fields: scope in/out · acceptance · gates · slug or "none") `` | `` `## task` (every field `--task-skeleton` prints, and slug or "none") `` |
| Step 5, after `its skeleton says when to append its ## route.` | nothing | `` On go, a code build continues in `/build` where the project ships it. `` |

Measured with the BASE text: the parenthetical shrinks 16 bytes and the sentence adds 70, so the
engine moves 18256 → 18310, under both its high-water and its ceiling, DERIVED by the size gate at
observation. The new sentence starts its own physical line after `append its ## route.`, so the line
holding the READY prompt string is not reflowed. Step 5b, the unattended hand-back, is untouched: the
clause fires on the owner's go, so the READY stop that aStandingWrit's F1 protects stays the default.

### The manifest bullet

One §B bullet, after the orientation-card bullet: an attended code build runs through `/build` after
kickoff's go (`KICK-aOrientedCast-2`); it is rendered by `bash tools/roles/adopt-roles.sh --scaffold`
and walks the role catalogue's workflows in stage order. Both stamps move to the commit's HEAD with a
datetime later than the current one.

### Rollout

This session's skill and agent registries were read when it started, so no pass of this run invokes
`/build` or spawns a rendered role; the Skill is observed by rendering and reading it. The first real
`/build` run is a session started after this build lands. Until `TOOL-aOrientedCast-8` lands, nothing
gates the Skill's freshness, and the close's bar runs after that unit.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `adopt-roles.sh` | the kit's adopter, two modes | none: a file |
| `render_skill` | shell function | `sh.function`; `python3 tools/lexicon/lexicon.py --suggest render_skill --as sh.function` answers OK |
| `build` | `rendered-skills` map key | claimed in the roles kit's dossier |
| `/build` | Skill name | none |

### Files touched (estimate)

- `tools/roles/SKILL.template.md`
- `tools/roles/adopt-roles.sh`
- `tools/roles/README.md`
- `.claude/skills/build/SKILL.md`
- `skills/session-kickoff/SKILL.md`
- `memory/guides/SESSION-KICKOFF.md`
- `.gitattributes`
- `memory/map/features/`
- `memory/map/generated/`

### Alternatives rejected

- **A token per stage, `{{STEP:<workflow>}}`, rendered from the catalogue.** The kit-placeholders join
  reads an adopter for each declared token's literal spelling, so a parameterised family cannot be
  declared, and `TOOL-aOrientedCast-8` substitutes the Skill's tokens in the adopter for that reason.
  Authored headings bound by S4's check give the same guarantee with three fixed tokens.
- **A size row and leg like `unattended skill size`.** See §3; AC11 measures the router once.

## 5. Production-readiness checklist

- security — the Skill adds no write path of its own: every write it orders is a spec status cell, a
  card append through the kickoff checker, or a record under `prompts/`, and every product or spec
  content write goes to a role agent the write gate grades. The adopter writes one file at a derived
  path and reads no input but the template, the catalogue and the conf.
- perf / scale — the plan verb is the slowest call the loop repeats, 42 s per read on node a, PINNED
  2026-10-11; the Skill reads it once per unit, and a build of N units pays it N + 1 times.
- error / empty / loading states — a missing card field, brief or go stops before stage 3; a stage
  disagreement or a surviving token refuses the render by name; an empty catalogue read is a dead probe.
- observability — the per-unit `## route` append, the records stage 5 and stage 6 write, and the
  harnesses' own logs name every stage's type.
- risks — the stage-binding check reads `workflows.toml` with `awk`, so a reformat of that file to an
  inline form reads zero workflows and refuses rather than passing. Re-opening a CLOSED unit for a
  blocker fix is a status-only edit; whether the pass-order history leg reads a re-opened spec as
  spec-after-code is UNVERIFIED. Bug classes the checklist selects for these paths:
  `reflowed-prompt-string-reads-as-a-deleted-stop`, `shipped-checker-edit-is-an-adopter-contract-change`
  and `two-answers-to-one-question`, the last being the copy this Skill must not become.
- testing — the direct checks below; the adopter's regression arms are `TOOL-aOrientedCast-8`'s.
- migration — none for data. An adopter without the roles kit sees the engine's new clause and has no
  `/build`; the clause says "where the project ships it".
- user docs — the Skill itself, S9's README section and S7's manifest bullet.

## 6. Acceptance criteria

`adopt-roles.sh` below is the roles kit's adopter, run from the repository root as
`bash tools/roles/adopt-roles.sh`, and the rendered Skill is the file its `--scaffold` prints. A fixture
repository, where a criterion needs one, is a `git clone --local` under a short `%TEMP%` root, never
under the scratchpad.

- **AC1** — When `adopt-roles.sh --scaffold` runs in this worktree it prints the
  rendered Skill's path, the file opens with `name: build` inside its front matter and carries no `{{`,
  and `adopt-roles.sh --check` exits 0; one byte appended to the rendered Skill makes
  `--check` exit 1 naming that path, removing the render makes it exit 1 too, and restoring either
  exits 0; `adopt-roles.sh --bogus` exits 2.
  Red when: a hand edit to the Skill passes the check, or the check reads only one side's bytes.
  fixture: needs the roles kit of `TOOL-aOrientedCast-1` and its catalogue in the tree.
- **AC2** — When the fixture repository's `workflows.toml` is staged with `build` moved to stage 8,
  then with `gate-bar` deleted, then emptied of every `[[workflow]]`, and its template with a heading
  `## Stage 9 — deploy` added, and its template with a `{{NOPE}}` token, `--check` exits 1 naming the
  heading and the entry for the first two and the fourth, exits 2 naming a dead probe for the third,
  and exits 1 naming the line for the fifth; each restored file exits 0.
  Red when: the Skill's stages can drift from the catalogue, or a brace reaches the render.
- **AC3** — When `grep -c` counts each of `harness-args unattended-build`,
  `harness-args unattended-unit`, `harness-args tier2-review`, `--part task`, `mode: 'attended'`, `planState`, `diverged`, `INPROGRESS`, `## route`, `**Reuse:**`,
  `BUILD-METHOD.md` and `UNATTENDED-VERBS.md` over the rendered Skill, each prints at least 1, and the
  headings `## Stage 1 — orient` through `## Stage 7 — gate-bar` appear once each, in order.
  Red when: a stage loses its pointer, or the router routes nowhere.
- **AC4** — When `grep -oE "unattended\.sh --[a-z-]+"` runs over the rendered Skill and its output is
  sorted unique, it prints `unattended.sh --plan` and nothing else.
  Red when: the Skill orders an attended session to call a driver verb that refuses without a
  run-state file.
- **AC5** — When `grep -cE "REVIEW_ROUNDS|CONVERG|--dispatch|--park|--rescope|--close"` runs over the
  rendered Skill it prints 0, and the `## Shared with /unattended` table names `M8`, `M9` and the
  verbs guide.
  Red when: the Skill restates a carrier's rule instead of pointing at it, a second copy of the
  procedure.
- **AC6** — When `grep -c "continues in ./build. where" skills/session-kickoff/SKILL.md` runs it prints
  1, `grep -c "the sealed fields:" skills/session-kickoff/SKILL.md` prints 0 where BASE prints 1,
  `grep -qF "Ready — say go and I'll start, or adjust any field." skills/session-kickoff/SKILL.md`
  exits 0, and `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` exits 0 with no
  `WARN` line.
  Red when: the engine overruns its ceiling or high-water, the hand list survives, or the READY
  string was reflowed off one line.
  figure: the engine's bytes are DERIVED by the size gate at observation; §4 predicts 18310.
- **AC7** — When `bash skills/session-kickoff/manifest-check.sh` runs after the commit it exits 0, and
  `grep -c "runs through ./build. after" memory/guides/SESSION-KICKOFF.md` prints 1.
  Red when: the engine or §B moved without its stamp.
- **AC8** — When `git grep -n "rendered-skills = .*build" -- memory/map/features` runs it prints
  exactly one line, and `python tools/codebase-map/gen_map.py --check` exits 0.
  Red when: the Skill is an unclaimed inventory key, or the symbol map is stale for `render_skill`.
- **AC9** — When `git check-attr eol` runs over the rendered Skill and its template, both print
  `eol: lf`.
  Red when: a CRLF checkout can hold a Skill the byte compare and the wiring check's eol arm read
  differently.
- **AC10** — When `bash tools/check-install-prefix.sh --offenders` runs it prints no key naming the
  template or the adopter.
  Red when: a kit file of this unit spells a sibling kit's path by literal.
- **AC11** — When the rendered Skill is measured with carriage returns stripped, `wc -c` prints at most
  6144.
  Red when: the router grows into a procedure.
  figure: DERIVED at observation; the limit is PINNED here and is not a gate.
- **AC12** — When the attended dry run runs in a fixture repository, a `git clone --local` of the
  pass's HEAD under a short `%TEMP%` root holding a fixture build `zFixtureCast` (a README whose front
  matter names `ids: TOOL-zFixtureCast-1`, that unit's spec, and a brief record under its `prompts/`)
  and a card that `bash skills/session-kickoff/manifest-check.sh --card --write --session kx2` wrote
  and `--card --append` filled with all eight task fields and a real READY line: the
  `handoff.py render` line the rendered Skill's `## Before stage 3` section spells, run with
  `CLAUDE_CODE_SESSION_ID=kx2` and its placeholders filled as `--role gov-builder`,
  `--build zFixtureCast`, `--unit TOOL-zFixtureCast-1` and `--input spec=<that spec>`, its
  `--part task` kept, exits 0 and prints a `gov:handoff` marker line and a `## Task` section;
  `handoff.py check` on the file that marker's `path` names exits 0; and each
  `handoff.py harness-args` call the Skill orders, for `unattended-build`, `unattended-unit` and
  `tier2-review`, exits 0 and prints a non-empty JSON object.
  Red when: the render line the Skill spells refuses on a complete card, the file it writes fails its
  own check, or a harness the Skill calls has no roles to pass.
  fixture: the renderer of `TOOL-aOrientedCast-2` and a card `KICK-aOrientedCast-1` grades, built
  under `%TEMP%`; nothing in the tree holds one today.

## 7. Gates

`check-wiring self-test` · `lexicon naming predicates` · `manifest-check self-test` · `scratch-guard self-test` · `recall floor` · `recall floor arms` · `kickoff-manifest ratchet` · `kickoff engine size <=18KiB` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No suite arm lands in this unit. The adopter's check mode becomes a gate leg, and its stage-binding
and surviving-token refusals gain regression arms, in `TOOL-aOrientedCast-8`.

## 8. Open questions

- **F1 — Which program renders the Skill?** (a) The agent renderer of `TOOL-aOrientedCast-3`, as a
  third output beside the agent types and the index. (b) `tools/roles/adopt-roles.sh`, created here as
  the kit's adopter rendering the Skill alone, which `TOOL-aOrientedCast-8` extends with the agent
  render. (c) A separate Python script. A probe decides between them: `TOOL-aOrientedCast-8`'s §4 has
  the adopter substitute the Skill's tokens by literal spellings because the kit-placeholders join reads
  only the adopter, and rejects a render elsewhere by moving it into the adopter; and the brief asks for
  a byte-compared render "as the unattended kit renders its Skill", which `adopt-unattended.sh` does.
  Options (a) and (c) are each rewritten one unit later. Recommendation: (b).
  RESOLVED (agent, 2026-10-11, delegated): (b), as S2 is written.
- **F2 — Does `/build` spawn the reuse scout?** (a) Always, as a rendered `gov-reuse-scout` handoff.
  (b) Never: read the card's `## reuse` when present, else its `**Reuse:**` field. (c) Only when the
  owner opted in. Options (a) and (c) build the scout's trigger, which the brief puts in aScoutedSeam's
  later unit and §3 here excludes, M3's veto 1. Recommendation: (b).
  RESOLVED (agent, 2026-10-11, delegated): (b); the scout's opt-in at kickoff writes the section.
- **F3 — How does a closing-review blocker's fix reach product code once the main loop may not write
  it?** (a) A direct `gov-builder` spawn naming the finding. (b) A pass of the unit the blocker lands
  in, through the unit harness, with a fix record as its brief and the unit re-opened to INPROGRESS by
  a status-only edit. (c) The main loop edits the code, which the write gate refuses. Option (a) cannot
  hand the finding: `gov-builder` reads `input:spec`, `card:route?` and `brief:non-goals?`, and the
  renderer refuses an input its role does not read. Option (b) reuses the unit harness unchanged.
  Recommendation: (b).
  RESOLVED (agent, 2026-10-11, delegated): (b), as stage 6 is written.
- **F4 — How does a builder's divergence reach the spec writer?** (a) `--input question=<why>`. (b) A
  revision record under `prompts/` holding `## The brief` and no `## The prompt`, passed as `--input
  prompt=`. Option (a) exits 2: `gov-spec-writer` reads no `input:question`. Option (b) keeps the
  renderer's default brief lookup unambiguous, because that lookup counts only records carrying both
  headings. Recommendation: (b).
  RESOLVED (agent, 2026-10-11, delegated): (b), as stage 5 is written.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the unattended adopter and Skill, the two build harnesses'
  attended mode, the kickoff engine's Step 5 and its byte budget, and the role catalogue, renderer,
  unit-harness and write-gate specs of this build.
- rev-2 · 2026-10-11 · S1 · §3 · §4 · AC3 · AC12 · the M2 cross-read's findings 1 and 12. Stage 5
  passes `roles` from `handoff.py harness-args unattended-unit` on every unit dispatch, and AC3 counts
  that string. AC12 runs the attended dry run the build's acceptance names. The Edges declare the
  hands-off to the spawn guard that its consumes-from now names, and the non-goal on `/unattended`'s
  text names `TOOL-aOrientedCast-9` as its owner.

## 10. Reuse audit

The Skill's render is the unattended kit's, by shape: `adopt-unattended.sh`'s `.git` walk, its literal
token substitution with the trailing-newline sentinel, its `--check` byte compare normalised on both
sides, and its no-`fail()` rule (`tools/unattended/adopt-unattended.sh:62-75`, `:423-462`). The
attended pipeline is the harnesses' own `mode: 'attended'` (`TOOL-aStagedLane-2`), driven through the
`dispatch` hand-out the build harness already returns, so no step of the procedure is re-implemented.
`python tools/codebase-map/reuse_lookup.py "route an attended session's code build into the build
harness and unit harness after the kickoff hand-back"` returned only name-stem matches on `build`
(`build_commit`, `build_fixture`, `units` among them), none a router or a Skill render; the lookup
reads symbols and inventory keys, and the seams above were found by reading the two adopters and the
harness hand-out. Recall returned `TOOL-aStagedLane-2` (attended mode and its losses),
`TOOL-aUnmannedHelm-8` (the kickoff hand-back and its exits), aStandingWrit's review F1 (Step 5b must
not skip the READY stop by default) and `TOOL-cBriefedPilot-11` (the unattended Skill runs kickoff after
preflight), each of which shaped §4.

Recall terms used: attended mode unattended-build unattended-unit hand-back kickoff Step 5 READY router Skill planState dispatch harnessed
