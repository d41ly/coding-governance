# TOOL-aOrientedCast-1 — the role catalogue: one owner-editable agent definition per role, the workflow table, and the checker that keeps them agreeing

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-1-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md) | journal | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 |
| [2026-10-13-prompt-TOOL-aOrientedCast-1-4-owner-addendum.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-4-owner-addendum.md) | research | PLAY-aOrientedCast-1 |
| [2026-10-13-prompt-TOOL-aOrientedCast-1-5-resume-handoff.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-5-resume-handoff.md) | journal | PLAY-aOrientedCast-1 |
| [2026-10-13-prompt-TOOL-aOrientedCast-1-6-owner-addendum.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-6-owner-addendum.md) | research | TOOL-aOrientedCast-2 |
| [2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md](../reviews/2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md) | diff-review | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 |

<!-- /gen:spec-records -->

## 1. Goal

Every agent prompt in this repository is either freeform or a string literal inside a harness the
owner cannot adjust. This unit creates the `roles` kit: a catalogue of the ten workflows, one
agent-definition file per role holding the constant block its agent starts from, an empty owner
overlay per role, and a checker, gated as a leg, that keeps the role files, the workflow table and
the governing doc's section ids agreeing in both directions. Later units render, spawn and enforce
from this catalogue; this unit renders no prompt, spawns no agent and edits no harness.

## 2. Scope (IN)

- **S1** — The kit's identity: a descriptor `tools/roles/kit.toml` carrying `id`, `home`, `scope`,
  `requires` and `version_from` and no `[[files]]` row; a `README.md` whose first line is the
  `gov:kit roles@1.0` marker; and the version constant `KIT_ROLES_VERSION` in the kit's library
  module. Observed by AC10.
- **S2** — The library module `roles_lib.py`: the one reader of role files, the workflow table, the
  memory-tree conf and the governing doc's sections, plus the one composition of a role with its
  house overlay (§4 "The library"). Observed by AC1, AC12 and AC13.
- **S3** — The workflow table `workflows.toml`: one entry per workflow for all ten names of the
  build's interface 2, with the keys §4 "Data model — the workflow table" pins, including the
  `stages` table §8 F1 adds. Observed by AC1 and AC3.
- **S4** — Ten role files under `tools/roles/agents/`, one per slot key, each with the front matter
  §4 "The ten roles" tabulates and a body written to §4 "What every body says". Observed by AC1, AC2,
  AC5 and AC9.
- **S5** — Ten empty house overlays under `tools/roles/house/`, one per slot key. Observed by AC1 and
  AC4.
- **S6** — The checker `check_roles.py`, grading every rule of §4 "The checker's rules", printing the
  counts it graded and refusing a zero population. Observed by AC1 to AC8.
- **S7** — A generated catalogue region in the kit README, rendered from the workflow table and the
  role front matter by the checker's `--write` verb and compared on every check run. Observed by
  AC8.
- **S8** — The gate leg `roles catalogue` in `tools/gate-legs.json`. Observed by AC11.
- **S9** — The map and manifest records the new kit owes: a dossier `memory/map/features/roles.md`
  claiming the kit key `roles` and the gate-leg key `roles catalogue`, `memory/map/generated/symbols.json`
  regenerated, and the kickoff manifest's `last-audit` re-stamped because `tools/gate-legs.json` is in
  its `watch:`. NOT OBSERVED by a criterion: the `codebase-map coverage + freshness` and
  `kickoff-manifest ratchet` legs grade these records at the close.

## 3. Non-goals (OUT)

- The handoff renderer and its prompt file (`TOOL-aOrientedCast-2`). This unit's library composes a
  role with its overlay and nothing more.
- Rendering `.claude/agents/` or `.claude/roles.json` (`TOOL-aOrientedCast-3`).
- Any harness edit. The craft text is COPIED into the role files here; the harness strings stay
  byte-identical until `TOOL-aOrientedCast-4` and `TOOL-aOrientedCast-5` take them out.
- govkit wiring: the registry entry, the default selection, each file's govkit role and the
  version-gate carrier row are `TOOL-aOrientedCast-8`'s. Until it lands, `govkit selfcheck` names
  the new directory as unclaimed surface; the bar runs once, after it.
- Grading role prose for meaning. The checker grades shape, cross-references and size.
- A ceiling on house overlays. An overlay is the adopter's own text; its byte count is printed on
  every run and never graded.
- Grading that an `enforced-by` entry names a live hook arm or leg. The arms land in later units and
  are named by description; the README re-read at the close is that check.
- Validating `tools:` values against Claude Code's tool list, which moves with the CLI.
- The reuse-scout's content and its trigger, which belong to aScoutedSeam. The slot's body defers to
  the codebase-map kit's own instruction.
- A kit-version bump. The kit starts at 1.0.

### Edges

- **hands-off** `TOOL-aOrientedCast-2` — the library's front-matter reader, its role composition, its
  charter section reader, its conf reader and the `stages` table the harness-arguments verb reads.
- **hands-off** `TOOL-aOrientedCast-3` — the role composition every rendered agent type's body is,
  the harness path resolver its harness list derives from, and the `agent` flag.
- **hands-off** `TOOL-aOrientedCast-4` — the builder, spec-writer and disposal craft now in role
  files, which that unit takes out of the build harness prompts.
- **hands-off** `TOOL-aOrientedCast-5` — the finder, skeptic and synthesis craft now in role files;
  the severity rubric and probe rules stay in the review harness as stage protocol.
- **hands-off** `TOOL-aOrientedCast-6` — the closed `writes` vocabulary the write gate keys a role on.
- **hands-off** `TOOL-aOrientedCast-8` — the registry entry, the default selection, the govkit role of
  every file this unit creates, and the version-gate carrier row.
- **hands-off** `KICK-aOrientedCast-2` — the workflow table's stage order, which the attended router
  walks.
- **consumes-from** external — the governing doc's section headings, located through the memory-tree
  conf's `CHARTER` declaration.

## 4. Design

### Evidence

Read at `646d4a73` on 2026-10-11.

- Two kits already ship agent files named `*.agent.md`: `tools/workflows/orient.agent.md` carries
  Claude Code front matter (`name`, `description`, `tools`, `model`, `maxTurns`) and a body;
  `tools/codebase-map/reuse-lookup.agent.md` carries none.
- The front-matter grammar this repo already grades: `parse_front_matter` reads column-0
  `key: value` lines and refuses an indented key (`tools/memory-tree/gotchas.py:233-258`); the hooks
  kit reads one key the same way (`tools/hooks/scratch-guard.js:649-657`).
- The conf grammar the hooks kit reads: one regex per line, an optional `export`, a double-quoted,
  single-quoted or bare value, a trailing comment, last assignment wins
  (`tools/hooks/scratch-guard.js:770-777`).
- `.memory-tree.conf` declares `CHARTER="AGENTS.md"`, which check 16 reads as the governing doc
  (`tools/memory-tree/corpus_ids.py:692-694`). The agent-instructions kit makes `AGENTS.md` the
  canonical file that `CLAUDE.md` imports (`tools/agent-instructions/adopt-agent-instructions.sh:6-9`).
- The governing doc's sections, measured in `AGENTS.md`: `§0`, `§1`, `§2`, `§3`, `§5`, `§6`, `§7`,
  `§8`, `§9`, `§10`, `§11`, `§12`, `§14`, `§15` and `§16`, each a `## §<n> — <title>` heading; there
  is no `§4` and no `§13`. PINNED at `646d4a73`; the checker re-derives the set on every run.
- The harness craft this unit copies: the grounding preamble and the spec writer
  (`tools/workflows/unattended-build.template.js:761-788`, `:849-876`), the committer (`:1056-1080`),
  the disposal agent (`:1856-1880`), the builder (`tools/workflows/unattended-unit.js:179-225`), and
  the rubric, probe rules, finder opening and skeptic of the review harness
  (`tools/workflows/tier2-review.template.js:545-571`, `:1025-1031`).
- A kit file names nothing outside itself by literal, says anything else through a `{{…}}` token, and
  refuses an unresolved token (`tools/hooks/README.md:341-353`). Shipped documents spell a
  memory-tree path as `{{MEMORY_ROOT}}/…`, as `tools/memory-tree/BUILD-METHOD.template.md` does.
- `resolve_kit_dir` is carried inline, byte-identical, by every consumer, and a parity table grades the
  copies (`tools/lib/resolve_kit_dir.py:1-11`).
- A new directory under the tool root is a kit inventory key (`tools/codebase-map/map_extractors.py:82-95`)
  and a surface path `govkit selfcheck` asserts in both directions (`tools/govkit/registry.toml:17-31`).
- `tools/gate-legs.json` is in the kickoff manifest's `watch:` (`memory/guides/SESSION-KICKOFF.md:6`),
  and the staged leg refuses a commit touching a watched file without a re-stamp
  (`skills/session-kickoff/manifest-check.sh:1411-1425`).
- `tomllib` is already this repo's TOML reader (`tools/codebase-map/map_lib.py:42`).

### Layout

```text
tools/roles/
  kit.toml              identity only (S1); file roles arrive with TOOL-aOrientedCast-8
  README.md             architecture prose plus the generated catalogue region (S7)
  workflows.toml        the ten workflows (S3)
  roles_lib.py          the one reader and the role composition (S2)
  check_roles.py        the checker (S6)
  agents/<slot>.agent.md   ten role files (S4)
  house/<slot>.md          ten empty overlays (S5)
```

### Data model — the workflow table

One `[[workflow]]` per workflow, in stage order. The keys are the build's interface 2 plus
`stages` (§8 F1):

| Key | Value | Graded |
|---|---|---|
| `name` | one of `orient research reuse handoff spec-write spec-review build closing-review gate-bar bookkeeping` | each name exactly once |
| `stage` | an integer, `0` for an any-time workflow | an integer at or above 0 |
| `driver` | `agent`, `workflow`, `program` or `main-loop` | closed set |
| `harness` | a `{prefix}`-relative script path, a command, or `none` | a `workflow` driver's harness is a `{prefix}/<home>/<file>.js` path; one the tree does not hold is a `note`, not a defect (R9) |
| `roles` | a list of slot keys | each names a role file; an `agent` or `workflow` driver names one or more |
| `stages` | optional inline table, harness stage key to slot key | only on a `workflow` driver; each value is in this entry's `roles` and names a role whose `agent` is true; each key matches `^[a-z][A-Za-z]*$` |
| `enforced-by` | a list of entries, or the single string `none — <why>` | non-empty |
| `trigger` | one line | non-empty, no newline |

The ten entries:

| name | stage | driver | harness | roles | stages |
|---|---|---|---|---|---|
| `orient` | 1 | `main-loop` | `/session-kickoff` | `gov-orienter` | none |
| `reuse` | 2 | `agent` | `none` | `gov-reuse-scout` | none |
| `spec-write` | 3 | `workflow` | `{prefix}/workflows/unattended-build.js` | `gov-spec-writer gov-builder gov-spec-reviewer gov-skeptic gov-synthesizer` | `specWriter`, `disposal` to `gov-spec-writer`; `builder` to `gov-builder`; `specFinder`, `skeptic`, `synthesis` to `gov-spec-reviewer`, `gov-skeptic`, `gov-synthesizer` |
| `spec-review` | 4 | `workflow` | `{prefix}/workflows/tier2-review.js` | `gov-spec-reviewer gov-skeptic gov-synthesizer` | `specFinder`, `skeptic`, `synthesis` |
| `build` | 5 | `workflow` | `{prefix}/workflows/unattended-unit.js` | `gov-builder` | `builder` |
| `closing-review` | 6 | `workflow` | `{prefix}/workflows/tier2-review.js` | `gov-diff-reviewer gov-skeptic gov-synthesizer` | `diffFinder`, `skeptic`, `synthesis` |
| `gate-bar` | 7 | `program` | `bash {prefix}/run-gates/run-gates.sh` | none | none |
| `research` | 0 | `agent` | `none` | `gov-researcher` | none |
| `handoff` | 0 | `program` | `python {prefix}/roles/handoff.py render` | `gov-session` | none |
| `bookkeeping` | 0 | `main-loop` | `none` | none | none |

Each `stages` value is a role its entry's `roles` lists. The `spec-write` entry lists `gov-builder`
and the three review roles as well, as `spec-review` lists the skeptic and the synthesizer, because
its harness forwards `builder` to the unit harness through `dispatch.args` and passes `specFinder`,
`skeptic` and `synthesis` into its audit's review-harness call (`TOOL-aOrientedCast-4` §8 F2 and
F3). The `unattended-build` harness's `committer` stage appears in no table: it authors nothing and
commits through one Bash block, so it keeps today's spawn options and its harness logs that.

`enforced-by` names, by description, what refuses a bypass once this build lands:
`manifest-check.sh --card --append` for `orient`; the scratch guard's role arm for `spec-write` and
`build`, beside the `routed commits name a specced unit` leg for `build`; the spawn guard in
`agent-cap.js` for `research` and `closing-review`; the pre-push hook for `gate-bar`; the
`memory hygiene` leg for `bookkeeping`. `spec-review` names the spawn guard only because its audit
runs under roles: the guard sees the build harness's `Workflow` call, whose `roles` carries the
audit's three review keys, and never the audit's own call into the review harness. `handoff` reads
`none — a session-to-session message is no tool call the spawn guard sees`, and `reuse` reads
`none — the scout's trigger is the kickoff opt-in that aScoutedSeam owns`. `trigger` is one line per
entry, written by the builder from the brief's architecture paragraph.

The shape, pinned by one entry:

```toml
[[workflow]]
name = "build"
stage = 5
driver = "workflow"
harness = "{prefix}/workflows/unattended-unit.js"
roles = ["gov-builder"]
stages = { builder = "gov-builder" }
enforced-by = ["scratch-guard.js role arm", "routed commits name a specced unit"]
trigger = "once per unit, in stage order, after its spec is READY"
```

### Data model — role front matter

A `---` block at line 1. Every key sits at column 0 as `key: value`, one per line; an indented, a
repeated or an unknown key is refused. A list is comma-separated on one line, the form Claude Code's
own `tools:` already takes, so one reader serves both families of keys and the file stays a valid
agent definition.

| Key | Owner | Required | Value |
|---|---|---|---|
| `name` | Claude Code | yes | the slot key, equal to the file's stem before `.agent.md` |
| `description` | Claude Code | yes | one line |
| `tools` | Claude Code | when `agent` is true | comma list |
| `model` | Claude Code | when `agent` is true | `inherit` for all ten |
| `maxTurns` | Claude Code | no | an integer |
| `workflow` | gov | yes | a `workflows.toml` name whose `roles` lists this slot |
| `reads` | gov | yes | comma list of input keys, interface 5 of the build, a trailing `?` marking one optional |
| `writes` | gov | yes | exactly one of `none`, `spec`, `product`, `review`, `records` |
| `charter` | gov | yes, may be empty | comma list of `§<n>` ids |
| `returns` | gov | yes | one line |
| `agent` | gov | no | `true` or `false`, default `true` |

The `reads` vocabulary is closed and lives in the library as one constant: `task:` with `title`,
`goal`, `in`, `out`, `todo`, `reuse`, `acceptance`, `gates`; `card:` with `route`, `records`,
`classes`, `read`, `open`, `reuse`; `brief:` with `goal`, `items`, `acceptance`, `gates`,
`non-goals`; `input:` with `spec`, `diff`, `question`, `prompt`. `card:reuse` is refused without its
`?`, because that section is aScoutedSeam's and absent from every card until it lands. A key named
twice is refused.

### The ten roles

| Slot | workflow | writes | tools | reads | charter | ceiling |
|---|---|---|---|---|---|---|
| `gov-orienter` | `orient` | `none` | Read, Grep, Glob, Bash | `input:question`, `input:prompt?` | §1, §2, §5 | 3072 |
| `gov-researcher` | `research` | `none` | Read, Grep, Glob, Bash, WebSearch, WebFetch | `input:question`, `brief:goal?`, `brief:non-goals?` | §5, §12 | 3072 |
| `gov-reuse-scout` | `reuse` | `none` | Read, Grep, Glob, Bash | `input:question`, `task:in?`, `card:reuse?` | §12 | 1536 |
| `gov-spec-writer` | `spec-write` | `spec` | Read, Grep, Glob, Bash, Write, Edit | `brief:goal`, `brief:items`, `brief:acceptance`, `brief:gates`, `brief:non-goals`, `input:spec?`, `task:reuse?`, `card:route?` | §1, §7, §9, §12 | 4096 |
| `gov-spec-reviewer` | `spec-review` | `none` | Read, Grep, Glob, Bash | `input:spec`, `brief:goal?`, `brief:non-goals?` | §7, §8, §9, §10 | 4096 |
| `gov-builder` | `build` | `product` | Read, Grep, Glob, Bash, Write, Edit | `input:spec`, `card:route?`, `brief:non-goals?` | §3, §7, §9, §11, §12 | 4096 |
| `gov-diff-reviewer` | `closing-review` | `none` | Read, Grep, Glob, Bash | `input:diff`, `input:spec?` | §7, §8, §9, §10 | 4096 |
| `gov-skeptic` | `closing-review` | `none` | Read, Grep, Glob, Bash | `input:diff?`, `input:spec?` | §8, §10 | 3072 |
| `gov-synthesizer` | `closing-review` | `review` | Read, Grep, Glob, Bash, Write | `input:diff?`, `input:spec?` | §8, §16 | 3072 |
| `gov-session` | `handoff` | `none` | none, `agent: false` | `input:question`, `brief:goal?`, `task:todo?`, `card:route?` | §2, §3 | 2048 |

Every agent role carries `model: inherit`. The skeptic and the synthesizer serve both review
workflows: their `workflow` key names `closing-review`, which every build runs, and the
`spec-review` entry lists them in its `roles` as well. The charter ids are each role's need once
`omitClaudeMd` removes the charter: the builder takes §3 for the attribution trailer and §11 for the
cross-OS rules, a reviewer takes §8 and §10 for the review protocol and the project's bug classes.

The ceilings are bytes of the BASE body, CR stripped, declared as one constant in the checker keyed
by slot. PINNED at writing on 2026-10-11 as the size of an opening rather than a manual: the
builder's craft in today's harness is about 3.5 KB with its stage protocol, and the protocol stays
in the harness. A slot with no ceiling row is refused, so a new role is priced when it is added.

### What every body says

The body is the constant block its agent starts from. It is written to the owner's register — "You
are a code architect, writing a feature specification. You are not writing any code right now" —
and in that order says: who the agent is; what it produces; what it is NOT doing in this pass; what
"done" means; that it returns exactly the shape its task block or harness names; and that it leaves
owner prose and anything outside its task out of what it writes and returns. A body POINTS at the
source that owns a rule and never restates it: `{{MEMORY_ROOT}}/TEMPLATE-SPEC.md`,
`{{MEMORY_ROOT}}/guides/BUILD-METHOD.md` with the section it means, and
`{{MEMORY_ROOT}}/guides/REVIEW-PROTOCOL.md`. Stage protocol stays in the harness that owns its return
contract: schemas, the `authored` naming, driver verbs, the `Pass:` trailer, the severity rubric and
the probe rules.

| Slot | The craft its body carries |
|---|---|
| `gov-orienter` | orients one session for one task through the kickoff engine's Steps 0 to 4, read-only; mints no slug; every question it would ask becomes an `open` row with the options it saw; returns the card body |
| `gov-researcher` | finds candidates, plural, that differ in mechanism; names for each the smallest test that would make it lose; records every rejected candidate with the test that rejected it (BUILD-METHOD M12); read-only |
| `gov-reuse-scout` | finds the seam a new behaviour extends before anything is built, by following the codebase-map kit's `reuse-lookup.agent.md`; nothing more until aScoutedSeam writes the content |
| `gov-spec-writer` | designs one unit so it is functional, concise, flexible and seams into existing code; verifies every claim about current code by reading it; names a direct observation per criterion; authors only, never commits, never writes product code |
| `gov-spec-reviewer` | hunts defects in a spec set before code exists; establishes each claim with a read-only probe; checks a claim about code against the code, never against the spec's account of it |
| `gov-builder` | builds exactly one unit from its spec; the spec is the design, and a divergence is returned with the divergence named instead of resolved by editing the spec; verifies with the spec's direct check, never a bar or a suite; bounds every command |
| `gov-diff-reviewer` | reviews only the diff it is handed, reading the touched files and their immediate callers; reports concrete findings with a path and line, the impact and a fix; hunts new defects, not by-design ones |
| `gov-skeptic` | tries hard to refute each finding by reading the cited code or spec; never confirms on the finder's word |
| `gov-synthesizer` | merges verified findings into one report, one item per defect, with the verdict line the review protocol names |
| `gov-session` | opens a handoff to another session of this repository: the receiver was not in the sender's conversation, owns its own slug and kickoff, and acts on the task block alone |

### The library — `roles_lib.py`

Stdlib only. Every text read and write names `encoding="utf-8"` and folds CRLF to LF.

| Name | Does |
|---|---|
| `KIT_ROLES_VERSION` | `"1.0"`, the version `kit.toml` reads |
| `RolesError` | the one exception; its message names the file and the rule |
| `read_conf_key(path, key)` | the hooks kit's conf grammar ported line for line; `None` when the key is absent |
| `resolve_charter_path(root)` | the `CHARTER` value of `<root>/.memory-tree.conf`, refused when the conf, the key or the file is absent |
| `extract_charter_sections(text)` | `{"§<n>": body}` for every `## §<n> — ` heading, the body running to the next `## ` line, blank edges trimmed |
| `parse_front_matter(path, text)` | the grammar above, returning the keys and the body |
| `load_roles(kit_dir)` | every `agents/*.agent.md`, parsed, keyed by slot |
| `load_workflows(kit_dir)` | `workflows.toml` through `tomllib`, as a list in file order |
| `render_role(kit_dir, name, memory_root)` | the base body with `{{MEMORY_ROOT}}` substituted, then, when the overlay is non-empty, a blank line, `## House rules`, a blank line and the overlay; any other `{{…}}` token raises |
| `resolve_harness_path(tool_root, harness)` | a `{prefix}/<home>/<file>` harness resolved through the inline `resolve_kit_dir` copy, returned with whether the tree holds it; when no kit holding the file resolves, the path its first probe names, `<tool root>/<home>/<file>`, and false; a harness of any other shape raises |
| `resolve_kit_dir` | the canonical block, carried inline between its markers |

`render_role` is the one composition: the handoff renderer and the agent render both call it, so a
role reaches an agent the same way by either route.

### The checker — `check_roles.py`

`python tools/roles/check_roles.py [--root <dir>] [--write]`. The kit directory is the script's own
directory and the tool root its parent; `--root` defaults to the git toplevel of the working
directory. One line per defect, `roles: <path>: <rule> — <what>`, then one summary line naming the
counts it graded: roles, overlays, workflows, `reads` keys, charter ids and the charter path, plus
each overlay's bytes. Exit 0 clean, 1 on any defect, 2 when the check is unarmed.

| Rule | Refuses | Exit |
|---|---|---|
| R0 | no `.memory-tree.conf`, no `CHARTER` key in it, or no file at that path | 2 |
| R1 | zero role files, or zero workflow entries: a check that graded nothing is DEAD PROBE | 1 |
| R2 | a front-matter defect: an unknown, indented, repeated or missing key; `name` not the file stem; `writes` outside its set; an `agent` value that is not `true` or `false`; `tools` or `model` absent on an agent role | 1 |
| R3 | a `reads` key outside the vocabulary, named twice, or `card:reuse` without `?` | 1 |
| R4 | a `charter` id that is not `§` and digits, or that names no heading in the governing doc | 1 |
| R5 | a body that is empty, over its slot's ceiling, carries a `# ` or `## ` line, or carries a `{{…}}` token other than `{{MEMORY_ROOT}}`; a slot with no ceiling row | 1 |
| R6 | a workflow entry with an unknown, missing or repeated key, an unknown or repeated `name`, a missing name of the ten, a non-integer or negative `stage`, an unknown `driver`, or a `trigger` carrying a newline | 1 |
| R7 | a role whose `workflow` names no entry, or an entry whose `roles` does not list it | 1 |
| R8 | a `roles` entry naming no role file; an `agent` or `workflow` driver with no role; a role file no entry lists | 1 |
| R9 | a `workflow` driver whose harness is not a `{prefix}/<home>/<file>.js` path; a `stages` table on another driver, a key outside its pattern, or a value outside the entry's `roles` or naming an `agent: false` role. A well-formed harness the tree does not hold is no defect: it prints one `roles: note:` line naming the harness and its workflow, and moves no exit | 1 |
| R10 | a house overlay naming no role, or carrying a `# ` or `## ` line or a token other than `{{MEMORY_ROOT}}` | 1 |
| R11 | the README's catalogue region absent, or different from a fresh render | 1 |

`--write` renders the region and writes it, and touches nothing else. The checker's header states
what it does not check: the meaning of a body, the truth of an `enforced-by` entry, a `tools:` name,
a command harness, which is graded for presence only, and whether the kit of a harness the tree does
not hold should be installed, which is a `note` here and the wiring check's to report.

### The README's catalogue region

Between `<!-- gen:roles-catalogue -->` and `<!-- /gen:roles-catalogue -->`, two tables rendered in
file order: the workflows with every key, and the roles with `workflow`, `writes`, `reads`,
`charter`, `agent` and `returns`. The prose around it is authored: the architecture in one
paragraph, how an owner edits a role (the overlay, never the base file, because the base is
overwritten on update), where the enforcement points will live, and the checker. The README points
at sibling kits by name and spells no path outside the kit.

### The gate leg

```json
{"name": "roles catalogue", "argv": ["python", "{prefix}/roles/check_roles.py"],
 "chunk": "declarations", "subject": "repo", "ceiling": 120}
```

No `guard`: the leg reads the governing doc and the conf as well as its kit, so it runs on every bar.
The ceiling is PINNED by declaration at 120 seconds and re-priced from the first measured run.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `roles` | kit id and directory | none: a kit id carries no naming cell |
| `roles catalogue` | gate leg name | none |
| `KIT_ROLES_VERSION`, `BODY_CEILINGS`, `READ_KEYS` | Python constants | none: `--suggest KIT_ROLES_VERSION --as py.constant` answered that `py.constant` is undeclared |
| `RolesError` | Python type | `py.type`; `--suggest RolesError --as py.type` answered OK |
| `read_conf_key`, `resolve_charter_path`, `extract_charter_sections`, `parse_front_matter`, `load_roles`, `load_workflows`, `render_role`, `resolve_harness_path` | library functions | `py.function`; each answered OK |
| `check_roles`, `render_catalogue_region`, `check_catalogue_region`, `main` | checker functions | `py.function`; each answered OK |
| `gen:roles-catalogue` | README region marker | none |
| `stages` | workflow-table key | none: a TOML key |

### Files touched (estimate)

`tools/roles/kit.toml` · `tools/roles/README.md` · `tools/roles/workflows.toml` · `tools/roles/roles_lib.py` · `tools/roles/check_roles.py` · `tools/roles/agents/` · `tools/roles/house/` · `tools/gate-legs.json` · `memory/map/features/roles.md` · `memory/map/generated/symbols.json` · `memory/guides/SESSION-KICKOFF.md`

### Rollout

- Inert until a later unit reads it: nothing spawns from a role file, and the only new leg is this
  checker. A wrong role body costs nothing until `TOOL-aOrientedCast-4` passes `roles`.
- Built before `KICK-aOrientedCast-1` inside order 1: both re-stamp the kickoff manifest, so their
  write sets intersect; `KICK-aOrientedCast-1` §8 F1 records the sequencing.
- The pass commit carries the manifest's `last-audit` re-stamp with a delta line, because
  `tools/gate-legs.json` is watched, and runs `gen_map.py --write` first, because new functions stale
  `symbols.json`.
- `govkit selfcheck` reports the new directory as unclaimed until `TOOL-aOrientedCast-8` registers
  the kit; nothing runs that leg before the close.

### Alternatives rejected

- **A YAML front-matter parser.** It is a new dependency, and Claude Code's own list form already
  fits one line per key.
- **Role files as JSON or TOML.** Claude Code reads Markdown with front matter, and the agent render
  would then need a second format for the same content.
- **Ceilings in front matter.** A key an owner edits beside the body it bounds is a bound that moves
  with the thing it bounds; the checker's constant moves only by a reviewed change.
- **Stage keys mapped inside the renderer.** A second home for a fact about workflows (§8 F1).
- **The governing doc located by following `CLAUDE.md`'s import.** Two locators for one file; the
  memory-tree conf already declares it and check 16 reads that declaration (§8 F2).
- **A README table typed by hand.** A value stated beside the source that owns it rots; the region
  is rendered and compared.

## 5. Production-readiness checklist

- security — no new write path in any hook; the checker reads only and `--write` writes one region
  of the kit's own README. A role body is prompt text that later units hand to agents, so it is
  reviewed like code.
- perf / scale — ten small files, one TOML read and one read of the governing doc; no spawn except
  the git toplevel probe. Seconds.
- error / empty / loading states — an unarmed check exits 2 naming the missing piece; an empty
  catalogue is DEAD PROBE, never a pass; every defect names its file and rule.
- observability — the summary line prints every count it graded and each overlay's bytes.
- risks — the charter ids bind to the governing doc's numbering, so a charter rewrite that renumbers
  sections reds this leg, which is the intended signal. An adopter whose governing doc carries no
  `§` sections reds its own leg; `TOOL-aOrientedCast-8` decides what an adopter install declares.
  The version-gate carrier row is not this unit's.
- testing — every rule observed RED on a staged break in a scratch fixture root and GREEN restored;
  no suite file is added.
- migration — none: a new kit, new files and one new leg.
- user docs — the kit README is this kit's user doc; the generated region keeps its tables true.

## 6. Acceptance criteria

The checker is `python tools/roles/check_roles.py`, the script this unit adds; a bullet below names
it `check_roles.py` and runs it from the kit directory, `cd tools/roles`, where the bare name
resolves. The fixture for AC2 to AC8 is a scratch root under the run's scratch directory holding a
copy of the kit directory at `tools/roles`, stub files for the three harness scripts the workflow
table names under `tools/workflows`, a copy of `AGENTS.md`, and a `.memory-tree.conf` declaring
`MEMORY_ROOT` and `CHARTER`; there the copied checker runs with `--root` naming that root. Every
staged break is restored after its observation, and the checker exits 0 again once it is.

- **AC1** — When `cd tools/roles && python check_roles.py` runs in the worktree, it exits 0 and its
  summary line reports 10 roles, 10 overlays, 10 workflows and the charter path `AGENTS.md`.
  Red when: any rule fires on the shipped catalogue, or a count reads zero.
  figure: the counts are DERIVED by the checker at observation time.
- **AC2** — When the fixture's copied `check_roles.py --root <fixture>` runs after each staged break —
  the `workflow:` line deleted from `gov-builder.agent.md`; `writes: code`; a `reads` key
  `task:scope`; a key `color: red`; an indented key; `name` differing from the file stem; `card:reuse`
  without `?` — it exits 1 naming the file and R2 or R3.
  Red when: a broken front matter passes.
  fixture: built under the run's scratch directory; nothing in the tree holds one today.
- **AC3** — When, in the fixture, `gov-skeptic.agent.md` names `workflow: review`; the `build`
  entry's `roles` names `gov-auditor`; a role file `gov-extra.agent.md` is added that no entry lists;
  the `build` entry's `roles` is emptied; the `build` entry's `stages` maps `builder` to
  `gov-skeptic`; an eleventh entry is added; or the `build` entry reads
  `harness = "workflows/unattended-unit.js"` — `check_roles.py --root <fixture>` exits 1 naming the
  rule, R6 to R9, for each. When the `build` entry reads `harness = "{prefix}/workflows/nope.js"`
  instead, it exits 0 and prints one `roles: note:` line naming that harness.
  Red when: any cross-reference break passes, or a well-formed harness the tree does not hold
  refuses.
- **AC4** — When the fixture gains a house overlay for a slot `gov-ghost` that no role file names,
  or the `gov-builder` overlay gains a line `## Extra`, `check_roles.py --root <fixture>` exits 1
  naming R10; with the `gov-builder` overlay holding a plain paragraph, it exits 0 and the summary
  line prints that overlay's bytes.
  Red when: a stray or heading-carrying overlay passes, or an overlay's bytes are not printed.
- **AC5** — When the fixture's `gov-builder.agent.md` body is emptied, padded past its ceiling, given a
  `## Heading` line, or given a `{{TOOL_ROOT}}` token, `check_roles.py --root <fixture>` exits 1
  naming R5 for each.
  Red when: an empty, oversized, heading-carrying or unknown-token body passes.
- **AC6** — When a fixture role's `charter` names `§4`, `check_roles.py --root <fixture>` exits 1
  naming R4, `§4` and the charter path; when the fixture's `.memory-tree.conf` has its `CHARTER` line
  deleted, it exits 2 naming `CHARTER`.
  Red when: a charter id with no heading passes, or the unarmed checker exits 0 or 1.
- **AC7** — When the fixture's `agents` directory holds no role file, or its `workflows.toml` holds no
  entry, `check_roles.py --root <fixture>` exits 1 naming DEAD PROBE and the empty population.
  Red when: an empty catalogue exits 0.
- **AC8** — When `check_roles.py --root <fixture> --write` runs and the check runs after it, the check
  exits 0; when one cell inside the README's `gen:roles-catalogue` region is then edited, or the
  region's markers are deleted, the check exits 1 naming R11 and `--write`.
  Red when: a stale or absent region passes.
- **AC9** — When `cd tools/roles/agents && grep -L "You are not" gov-orienter.agent.md gov-researcher.agent.md gov-spec-writer.agent.md gov-spec-reviewer.agent.md gov-builder.agent.md gov-diff-reviewer.agent.md gov-skeptic.agent.md gov-synthesizer.agent.md`
  runs, it prints nothing; and `grep -c "MEMORY_ROOT}}/TEMPLATE-SPEC" gov-spec-writer.agent.md` run
  there prints at least 1.
  Red when: a body omits what its agent is not doing, or the spec writer restates the spec format
  instead of pointing at it.
- **AC10** — When `cd tools/roles && python -c "import tomllib; d = tomllib.load(open('kit.toml', 'rb')); print(d['id'], d['version_from']['file'])"`
  runs, it prints `roles roles_lib.py`; `head -1 README.md` there prints the `gov:kit roles@1.0`
  marker comment; and `grep -c '^KIT_ROLES_VERSION = "1.0"' roles_lib.py` there prints 1.
  Red when: the descriptor, the marker or the constant is missing or disagrees.
- **AC11** — When `cd tools && python -c "import json; print([l['argv'] for l in json.load(open('gate-legs.json', encoding='utf-8')) if l['name'] == 'roles catalogue'])"`
  runs, it prints one argv whose script ends in `check_roles.py`.
  Red when: the leg is absent or names another script.
- **AC12** — When `python -c "import sys; sys.path.insert(0, 'tools/roles'); import roles_lib as r; print(r.render_role('tools/roles', 'gov-spec-writer', 'memory'))"`
  runs, its output carries `memory/TEMPLATE-SPEC.md` and no `{{`; in the fixture, with the
  `gov-spec-writer` overlay holding one line, the output ends with `## House rules` and that line;
  with a `{{TOOL_ROOT}}` token in the base body the call raises `RolesError` naming the token.
  Red when: a token survives, an overlay is not appended, or an unknown token renders.
- **AC13** — When `python -c "import sys; sys.path.insert(0, 'tools/roles'); import roles_lib as r; print(sorted(r.extract_charter_sections(open('AGENTS.md', encoding='utf-8').read())))"`
  runs, it prints the fifteen ids the governing doc carries, with no `§4` and no `§13`.
  Red when: a section is missed or a non-section heading is read as one.
  figure: the fifteen are PINNED at `646d4a73`; a charter edit that adds or removes a section moves
  the figure.

## 7. Gates

`roles catalogue` is the leg this unit adds; the close's bar grades it with these:

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `remote literals (kit code names no remote)` · `dead-path carriers (deleted files still named)` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `leg ceilings clear their evidenced maximum` · `every held leg is budgeted, every budget row resolves` · `run-gates canary` · `run-gates gov canary` · `recall floor` · `recall floor arms` · `govkit selfcheck`

New arm: check_roles.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · each staged break in a scratch fixture root, against a checker that grades nothing · none

## 8. Open questions

- **F1 — Where does a harness's stage key meet the role it spawns as?** Interface 2 of the build pins
  the workflow table's keys and interface 10 the harness stage keys, and neither says which role a
  stage key takes. The harness-arguments verb of `TOOL-aOrientedCast-2` must print that mapping.
  (a) An optional `stages` inline table on a `workflow` driver's entry, graded by R9. One home for a
  fact about workflows, read by the verb and rendered into the README region.
  (b) A constant in the renderer. A second home for a workflow fact, invisible to this checker.
  (c) Derive the stage key from the slot name. Measured, it fails for four of the seven mappings:
  `gov-synthesizer` is `synthesis`, the two finders are `diffFinder` and `specFinder`, and `disposal`
  spawns as `gov-spec-writer`.
  Recommendation: (a). It adds one optional key to a file this unit creates, and no sibling reads the
  table's keys except through the library.
  RESOLVED (agent, 2026-10-11, delegated): (a), by M3. It survives every veto: it adds no
  dependency, no install location and no surface beyond the file this unit already creates, and (c)
  fails on the measured names.
- **F2 — How is the governing doc located?** (a) The memory-tree conf's `CHARTER` key, which check 16
  already reads as the governing doc, and which names the file the agent-instructions kit makes
  canonical. (b) Follow `CLAUDE.md`'s `@` import. That reads one tool's wiring, and the import is
  only one of three alias modes that kit installs. (c) Assume `AGENTS.md`, which the brief forbids.
  Recommendation: (a), refusing with exit 2 when the key is absent rather than guessing.
  RESOLVED (agent, 2026-10-11, delegated): (a). One declaration, already graded, and an unarmed
  checker refuses.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · §4 · AC3 · the M2 cross-read's findings 6 and 9, and the stage keys of its
  findings 2 and 5. The `spec-write` entry's `stages` adds `builder` and the audit's three review
  roles, and its `roles` lists them. `enforced-by` reads `none` for `handoff`, and names the spawn
  guard for `spec-review` only through its audit's roles. R9 and the library's harness resolver admit
  a harness the tree does not hold with a `note`, so AC3 stages a malformed harness instead.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` over "grade an agent role definition file's front matter
against a closed vocabulary and a workflow catalogue" ranked no grader of agent definitions; it
surfaced `readFrontMatterKey` in the hooks kit's scratch guard and the agent-cap PreToolUse key,
neither of which parses a whole block. No existing seam fits the catalogue itself: no kit reads
`*.agent.md` front matter today, the two shipped agent files are read only by the CLI. The library
reuses three seams by porting their grammar rather than importing across kits, which a kit file may
not do: `parse_front_matter` in `tools/memory-tree/gotchas.py` for the column-0 front-matter rule,
`readConfKey` in `tools/hooks/scratch-guard.js` for the conf grammar, and the canonical
`resolve_kit_dir` in `tools/lib/resolve_kit_dir.py`, carried inline under its parity table. The
governing doc is located by the `CHARTER` declaration `tools/memory-tree/corpus_ids.py` already
reads. The role bodies copy their craft from the three harnesses at the lines §4 cites.

Recall terms used: `agent definition role preamble omitClaudeMd agentType workerType lens skeptic
synthesis catalogue front matter seed overlay` — which surfaced this build's own brief records,
`TOOL-aMendedFleet-67` (judges spawned as one agent type, and the earlier finding that a custom type
could not skip the charter, which the build's probe reversed), `TOOL-dClosedLexicon-15` (a `seed`
role is landable) and the agent-type probe record of this build.
