# PLAY-dConvergedCharter-9 — Skills as level-4 thin entries from their commands' drive rows, renamed `gov-<name>` by upgrade step, the old names forwarded, the prefix and stale-path arms

**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 18 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0483@5b53c82b whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md](../build/2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md) | research | PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-15 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |

<!-- /gen:spec-records -->

## 1. Goal

gov's five remaining rendered Skills carry their own procedures and bare names (gap-found-13,
gap-found-28): `/memory-recall`, `/runlog`, `/lexicon`, `/drift-audit` and `/cleanup`. This unit makes
each a level-4 thin entry generated from the `[[drive]]` row of the command it runs, never hand-written,
described "Use when …, runs …", installed with that command, and named `gov-<name>`. `/gov-recall` over
`gov why` and `record find` and `/gov-runlog` over `gov trace` are core. `/gov-lexicon`, `/gov-drift`
and `/gov-cleanup` ship with their kits. Each rename is an upgrade step, the old name forwarded for
`install.deprecation-window` releases, with its readers by path and by value re-pointed here: each kit's
`to`, `probe` and `pattern` rows, the adopt scripts and the self-tests' line-ending rows among them. A
planted stale `probe` path is red, and the Skill kind's conformance gate refuses a gov-rendered Skill
without the prefix (SK-2).

## 2. Scope (IN)

- **S1** — The drive rows. Each Skill's command gains a `[[drive]]` row (PLAY-dOrderedCharter-6 S1:
  `stage`, `role`, `command`, `when`) carrying `skill = "gov-<name>"` (I19, unit 10), in the descriptor of
  the kit that ships the command, per §4 "The five". `/gov-recall` is two rows sharing one `skill`, one
  for `gov why` (TOOL-dWellOiledMachine-34 S5) and one for `record find` (TOOL-dTotalRecall-9 S3), both in
  the core runtime kit's descriptor `tools/runtime/kit.toml`; `/gov-runlog` is one row there for
  `gov trace` (TOOL-dWellOiledMachine-34 S2). Observed by AC1.
- **S2** — The entries rendered. Unit 10's `skills` scope renders `.claude/skills/gov-<name>/SKILL.md`
  for each distinct `skill` value: front matter `name` the value and `description` the rows'
  `Use when <when>, runs <command>.` sentences in row order, and a body naming the command and the tags
  it enters, with no procedure. The five kits' `SKILL.template.md` files are removed and their legacy
  rows leave `tools/playbook/instructions-legacy.txt`. Observed by AC1 and AC2.
  **Readers:** by name: `tools/lexicon/kit.toml:74`, `tools/drift-audit/kit.toml:54`,
  `tools/branch-reconcile/kit.toml:32`, `tools/memory-recall/kit.toml:63` and `tools/runlog/kit.toml:50`
  (each `[[files]]` row's `include`), and the five adopt scripts that render them,
  `tools/lexicon/adopt-lexicon.sh:246`, `tools/drift-audit/adopt-drift-audit.sh:66`,
  `tools/branch-reconcile/adopt-branch-reconcile.sh:45`, `tools/memory-recall/adopt-memory-recall.sh:238`
  and `tools/runlog/adopt-runlog.sh:66`; `tools/drift-audit/README.md:104` · by value: NO VALUE READERS, no
  file counts or compares a template's bytes outside the adopt scripts' own `--check`, which the by-name
  half lists.
- **S3** — Installed with the command. Each entry's `[[files]]` row (`role = "rendered"`, `to` the
  gov- path) and its `[[regenerate]]` argv, `render_playbook.py --render-scope skills`, sit in the
  descriptor that ships the command. For `/gov-lexicon`, `/gov-drift` and `/gov-cleanup` that is the same
  kit, `to` re-pointed; for the core two it is `tools/runtime/kit.toml`, and the memory-recall and runlog
  kits keep no Skill row. Each kit adopter's Skill arm calls the one renderer, `--render-scope skills`
  and `--check-render --scope skills`, in place of its own render code, the way PLAY-dOrderedCharter-20
  S5 makes `adopt-roles.sh` a caller. Observed by AC3.
- **S4** — The renames as upgrade steps. One step program `tools/govkit/steps/skill_rename.py
  up|down|witness <target> <old> <new>`, and five `[[upgrade]]` rows in the old Skill's kit descriptor
  (the precedent `agent-cap/fanout-cap-to-agents-in-flight`, `tools/hooks/kit.toml:138-145`), ids
  `memory-recall/skill-to-gov-recall`, `runlog/skill-to-gov-runlog`, `lexicon/skill-to-gov-lexicon`,
  `drift-audit/skill-to-gov-drift` and `branch-reconcile/skill-to-gov-cleanup`, each with `surfaces =
  ["path:.claude/skills/<old>/SKILL.md"]`. The UP withdraws the old render where its bytes equal the old
  kit's render, as `adopt-branch-reconcile.sh --scaffold` withdrew `/branch-reconcile` at kit 1.4
  (`tools/branch-reconcile/README.md:169-172`), and names and keeps a file that is not. The DOWN restores
  it byte-identical. The WITNESS exits 0 when the old path holds no kit render. Observed by AC4.
- **S5** — The old names forwarded. Five `[[shim]]` rows in `tools/govkit/shims.toml`, `kind = "skill"`
  (I3, unit 17), `from = ".claude/skills/<old>/SKILL.md"`, `to = ".claude/skills/gov-<new>/SKILL.md"`,
  `closed = false`. Each stays open until `install.deprecation-window` releases are cut, which
  `check_shim_windows` holds while `read_releases` is the stand-in returning none
  (`tools/govkit/shims.py:302-305`). Removing a row once its window closes is unit 20's exit check, not
  this unit's. Observed by AC5.
- **S6** — The readers re-pointed, by path and by value, re-derived at the first pass by `derive_readers`
  (I1). Pinned at `d8a12f046` they are: each kit's `to`, `probe` and `pattern` rows (§4 "The five"); the
  `.gitattributes` Skill lines `:119`, `:125`, `:132`, `:281` and `:285`, those unit 19's class pins leave
  standing (I14); the self-tests `tools/memory-recall/selftest.py:1364`, `tools/runlog/selftest.py:8075`,
  `tools/govkit/selftest.py:7558`, `tools/govkit/matrix.py:298`, `tools/govkit/upgrade_walk.py:1008` and
  `tools/govkit/fixtures/release-0/plants.toml:99`; and the prose in
  `coding-governance-agents.template.md:124-146` (rendered to `AGENTS.md`), `WIRE-INTO-PROJECT.md`, the
  five kit READMEs and `tools/lexicon/LEXICON.md`. Observed by AC6 and AC7.
- **S7** — The stale-path arm. `core skills conformance` (PLAY-dOrderedCharter-7 S6) gains
  `check_skill_paths(root)`: every descriptor `to`, `probe` (`must_exist` and `must_not_exist`) and
  `[[lf_pin]]` `pattern` under `.claude/skills/` must name the directory of a `skill` value some
  `[[drive]]` row declares, or the `from` of an open `skill` shim row. Descriptors are read through
  `read_kit_rows(root)` (DEPL-dShippedRelease-10 S6), so the core reaches them with no govkit. Each red
  names the descriptor, the key and the path. Observed by AC6.
- **S8** — The prefix arm. The `kind.skill` row's population widens from `skills/*/SKILL.md` to also
  `.claude/skills/*/SKILL.md` (I20), and `check_skill_prefix(root)` reds a gov-rendered Skill whose
  `name` lacks `gov-`: a `skill` value of a `[[drive]]` row, or a `SKILL.md` a `[[target]]` row with
  `renderer = "playbook:skills"` claims. A Skill the repository writes itself, claimed by no such row, is
  never graded for the prefix. Observed by AC8.

## 3. Non-goals (OUT)

- The `skills` scope, its renderer and the `[[drive]]` row's `skill` key: unit 10's (I18, I19). This
  unit adds the rows and the five entries those render.
- The `skill` shim kind and its forwarder bytes: unit 17's (I3). This unit adds five rows of it.
- The per-kit Skill wiring `--check` arms and legs that remain once the entries render: unit 8's,
  each with its last document.
- `/build`, `/unattended` and `/session-kickoff`: units 17, 12 and 16 retire them; none is renamed.
- Closing a shim when its window ends, and the exit check over pending steps: unit 20's.
- The commands themselves: `gov why`, `gov trace` (TOOL-dWellOiledMachine-34) and `record find`
  (TOOL-dTotalRecall-9).
- The line-ending class pins: unit 19's. This unit re-points only the per-Skill lines it leaves.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-11` — `derive_readers`, the reader inventory by path and by value S6 re-derives at its first pass and re-points
- **consumes-from** `PLAY-dConvergedCharter-17` — `KINDS`, holding `skill`, so S5's five forwarder rows validate in `shims.toml`
- **consumes-from** `PLAY-dConvergedCharter-19` — `.gitattributes`, its class pins, so S6 re-points only the per-Skill lines the class leaves standing
- **consumes-from** `PLAY-dConvergedCharter-10` — `renderers.toml`, the `skills` scope's `[[target]]` row and the `skill` key of `[[drive]]` that S2 renders and S8 reads
- **consumes-from** external — PLAY-dOrderedCharter-6 and -7, TOOL-dDeclaredLoop-18, TOOL-dWellOiledMachine-34, TOOL-dTotalRecall-9 and DEPL-dShippedRelease-10 S6, each DEFERRED at base and built before this unit's build pass

## 4. Design

### Evidence

Read at `d8a12f046`; no product file differs from base `0d1c1dda`.

- `.claude/skills/` holds seven rendered Skills: `build`, `cleanup`, `drift-audit`, `lexicon`,
  `memory-recall`, `runlog` and `unattended`, each rendered from its kit's `SKILL.template.md` (`name:`
  at line 2 of each). `skills/session-kickoff/SKILL.md` is the authored one.
- `KINDS = ("command", "hook", "module")` at `tools/govkit/shims.py:48`, and a row's `from` and `to` must
  be `.sh`, `.js` or `.py` of one language (`:95-97`), so a `SKILL.md` row needs unit 17's `skill` kind.
- `install.deprecation-window` is `tools/policy/catalogue.toml:1666-1671`, allowed `0`, `1`, `2`, `4`,
  default `2`.
- The only `[[upgrade]]` row in a descriptor is `tools/hooks/kit.toml:138-145`; its program is
  `tools/govkit/steps/fanout_cap.py`.
- `/cleanup` was renamed from `/branch-reconcile` at kit 1.4 by its adopter withdrawing the old render
  (`tools/branch-reconcile/README.md:169-172`): no step, no forwarder. This unit is the first rename
  shipped as a step.
- Scout B row 9 holds against source at `d8a12f046`, line numbers included.

### The five

| Old | New | Command(s) | Drive row in | `to`, `probe`, `pattern` at base |
|---|---|---|---|---|
| `/memory-recall` | `/gov-recall` | `gov why`, `record find` | `tools/runtime/kit.toml` | `tools/memory-recall/kit.toml:63`, `:102`, `:115` |
| `/runlog` | `/gov-runlog` | `gov trace` | `tools/runtime/kit.toml` | `tools/runlog/kit.toml:50`, `:85`, `:116` |
| `/lexicon` | `/gov-lexicon` | `lexicon.py --suggest` | `tools/lexicon/kit.toml` | `tools/lexicon/kit.toml:74`, `:115` and `:145`, `:194` |
| `/drift-audit` | `/gov-drift` | `drift_report.py` | `tools/drift-audit/kit.toml` | `tools/drift-audit/kit.toml:54`, none, `:151` |
| `/cleanup` | `/gov-cleanup` | `branch_reconcile.py` | `tools/branch-reconcile/kit.toml` | `tools/branch-reconcile/kit.toml:32`, `:51`, `:64` |

A kit's command named here is the one its Skill runs today; the build pass reads it from the kit's
`[[command]]` row (TOOL-dDeclaredLoop-18) once that lands, and the `when` from the Skill's description.

### Inventory

Minted: the step program `tools/govkit/steps/skill_rename.py` with its fixture verb `--fixture --plant
<case>` (cases `rename`, `edited`, `absent`); the five step ids of S4; `check_skill_paths` and
`check_skill_prefix`, each asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at
`d8a12f046`: OK; the plant cases `skill-stale-probe` and `skill-no-prefix` on `core.py fixture --plant`.

### Migration

Per adopter, `govkit update` runs each step: the new entry is rendered by the `[[regenerate]]` argv, the
UP withdraws the old render, and `shims.py --write` renders the forwarder at the old path. A rollback's
DOWN restores the old render and the forwarder is not written.

### Files touched (estimate)

- `tools/runtime/kit.toml`
- `tools/lexicon/kit.toml`, `tools/drift-audit/kit.toml`, `tools/branch-reconcile/kit.toml`,
  `tools/memory-recall/kit.toml`, `tools/runlog/kit.toml`
- `tools/lexicon/SKILL.template.md`, `tools/drift-audit/SKILL.template.md`,
  `tools/branch-reconcile/SKILL.template.md`, `tools/memory-recall/SKILL.template.md`,
  `tools/runlog/SKILL.template.md` (removed)
- `tools/lexicon/adopt-lexicon.sh`, `tools/drift-audit/adopt-drift-audit.sh`,
  `tools/branch-reconcile/adopt-branch-reconcile.sh`, `tools/memory-recall/adopt-memory-recall.sh`,
  `tools/runlog/adopt-runlog.sh`
- `.claude/skills/` (five entries rendered, five forwarders)
- `tools/govkit/shims.toml`, `tools/govkit/steps/skill_rename.py`
- `tools/playbook/core.py`, `tools/playbook/kinds.toml`, `tools/playbook/instructions-legacy.txt`
- `.gitattributes`, `coding-governance-agents.template.md`, `WIRE-INTO-PROJECT.md`
- `tools/lexicon/README.md`, `tools/lexicon/LEXICON.md`, `tools/drift-audit/README.md`,
  `tools/branch-reconcile/README.md`, `tools/memory-recall/README.md`, `tools/runlog/README.md`
- `tools/memory-recall/selftest.py`, `tools/runlog/selftest.py`, `tools/govkit/selftest.py`,
  `tools/govkit/matrix.py`, `tools/govkit/upgrade_walk.py`, `tools/govkit/fixtures/release-0/plants.toml`

### Alternatives rejected

- **The rename done by each adopter's `--scaffold`, as kit 1.4 did `/cleanup`.** Rejected by the
  clause, which ships each rename as an upgrade step, and by the precedent's own README: `govkit update`
  "does not move a rendered file whose template stayed put" (`tools/branch-reconcile/README.md:169`), so
  an adopter that never re-runs the scaffold keeps the old name with no forwarder.
- **One step program per rename.** Rejected by the reuse rule's second-instance clause: five renames
  share one UP, DOWN and WITNESS that differ only in two names, so one program takes them as arguments.
- **The prefix arm keyed on the directory name alone.** Rejected because a repository's own Skill may
  carry any name, and the clause refuses only a gov-rendered one: the arm needs the drive row or the
  `skills` target to tell the two apart.

## 5. Production-readiness checklist

- security — the step writes only under `.claude/skills/<old>/` in its target, and withdraws a file
  only when its bytes equal the kit's render; any other file is named and kept.
- perf / scale — five rows, one descriptor read per arm.
- error / empty / loading states — an adopter with no old Skill is a witness-true no-op; a hand-edited
  old Skill is kept and named, and the step still records applied.
- observability — the UP names what it withdrew or kept; each arm names descriptor, key and path.
- risks — a reader the inventory misses keeps an old path; the stale-path arm reds any descriptor row,
  and the forwarder catches a prose reader for the window.
- testing — the step's three plant cases and the gate's two, each in a throwaway tree.
- migration — §4 "Migration".
- user docs — the five kit READMEs, `WIRE-INTO-PROJECT.md` and the charter's Skill lines name the new
  names.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --render-scope skills` runs after the unit
  lands, `.claude/skills/` holds `gov-recall`, `gov-runlog`, `gov-lexicon`, `gov-drift` and `gov-cleanup`,
  each `description` opening `Use when` and naming its command, the `gov-recall` entry's naming both
  `gov why` and `record find`, and the `gov-runlog` entry's naming `gov trace`.
  Red when: an entry carries a procedure, or a description is typed rather than rendered from its rows.
- **AC2** — When `git ls-files -- tools | grep -c SKILL.template.md` runs after the unit lands, it prints
  0, the five kits' templates gone and `/build`'s and `/unattended`'s with units 17 and 12, and
  `grep -c -E "skills/(cleanup|drift-audit|lexicon|memory-recall|runlog)/" instructions-legacy.txt`
  prints 0.
  Red when: a renamed Skill still has a hand-written template or a legacy row.
- **AC3** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs after the unit lands, it exits 0
  through `--check-render --scope skills` and holds no render code of its own for the Skill.
  Red when: the adopter renders the entry itself beside the one renderer.
- **AC4** — When `python skill_rename.py --fixture --plant rename` runs, the UP withdraws the old
  render and the WITNESS exits 0, the DOWN restores it byte-identical, and the `edited` plant keeps a
  hand-edited old Skill and names it.
  Red when: an edited Skill is withdrawn, or the DOWN differs by a byte.
- **AC5** — When `python tools/govkit/shims.py --check` runs after the unit lands, the five `skill` rows
  are open and each forwarder at an old path matches its render.
  Red when: a row is closed while `read_releases` returns none, or a forwarder is missing.
- **AC6** — When `python core.py fixture --plant skill-stale-probe` plants `probe = { must_exist =
  ".claude/skills/lexicon/SKILL.md" }` in a descriptor with no open shim from that path, `core skills
  conformance` exits 1 naming the descriptor, `probe` and the path; with the shim row open it exits 0.
  Red when: the stale probe passes, or a forwarded path reds.
- **AC7** — When `git grep -n -E "\.claude/skills/(cleanup|drift-audit|lexicon|memory-recall|runlog)/"
  -- . ':!memory'` runs after the unit lands, every hit is `tools/govkit/shims.toml` or a forwarder.
  Red when: a `to`, `probe` or `pattern` row, an adopt script or a self-test names an old path.
  figure: the reader set is PINNED at `d8a12f046` in S6 and DERIVED again at the build's first pass.
- **AC8** — When `python core.py fixture --plant skill-no-prefix` adds a `[[drive]]` row with `skill =
  "recall"`, `core skills conformance` exits 1 naming `recall`; a repository's own planted Skill
  named `notes`, claimed by no `skills` target, passes.
  Red when: a gov-rendered Skill without `gov-` passes, or a repository's own Skill is graded.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `policy fixtures` · `drift-audit selftest` · `branch-reconcile selftest` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The parent legs `core skills conformance` and `instruction render (one renderer of record)` run S7, S8
and AC1 once they land; neither is in the manifest at base.

New arm: tools/playbook/core.py · covers AC6 AC8 · the plants `skill-stale-probe` and `skill-no-prefix`, the failing cases a stale `probe` with no open shim and a drive row's `skill` without `gov-` · none
New arm: tools/govkit/steps/skill_rename.py · covers AC4 · the plants `rename`, `edited` and `absent`, the failing case an edited old Skill withdrawn · none

## 8. Open questions

- **F1 — Where is a core Skill's drive row, and which kit installs it?** Options: (a) the kit that
  ships its command, `tools/runtime/kit.toml` for `gov why` and `gov trace`; (b) the memory-recall and
  runlog kits, as today. RESOLVED (agent, 2026-11-03, delegated): (a), rung 1: the clause installs each
  entry "with that command" and calls both core (fates `:203`). widens: none · relaxes: none
- **F2 — One entry over two commands.** Options: (a) two `[[drive]]` rows sharing `skill =
  "gov-recall"`, rendered as one entry; (b) one row whose `command` holds both. (b) breaks
  PLAY-dOrderedCharter-6 S1's one-command row. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3;
  the renderer's one-entry-per-`skill` rule is asked of unit 10's writer in this build, not a parent.
  widens: none · relaxes: none
- **F3 — Where do the stale-path and prefix arms live?** Options: (a) both in `core skills
  conformance`, the Skill kind's gate; (b) the stale-path arm in govkit's selfcheck. The clause names
  the Skill kind's gate for the prefix, and the descriptors reach the core through `read_kit_rows`
  with no govkit. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3, one gate for the kind.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Item 9, layer-instruction R-F (`:514-525`), the
  fates row `:203`, scout B row 9 and findings 7 and 8, and the spec brief's I3, I14, I19 and I20.

## 10. Reuse audit

The seams extended are the `[[drive]]` row (PLAY-dOrderedCharter-6 S1) and unit 10's `skills` scope, the
shim row grammar (`read_shim_rows`, `tools/govkit/shims.py:60`) with unit 17's `skill` kind, the
descriptor `[[upgrade]]` row and its step-program shape (`tools/hooks/kit.toml:138-145`,
`tools/govkit/steps/fanout_cap.py`), and `core skills conformance` (PLAY-dOrderedCharter-7 S6).
`python tools/codebase-map/reuse_lookup.py "render a Skill entry from a command row and rename it with a
forwarder"` ranked name-stem hits only (`rows`, `row`, `render`, `extract_row`, `resolve_entry`); none
renames a rendered file across an upgrade, so `skill_rename.py` is new, on the step-program seam. Scout B
row 9 holds against source at `d8a12f046`; its finding 8 (no `skill` kind) is unit 17's, and the
`.sh`/`.js`/`.py` rule at `shims.py:95-97` is a second constraint that unit owes for a `SKILL.md` row.

Recall terms used: `python tools/memory-recall/query.py "how are gov's Skills renamed with a gov prefix and forwarded" --terms "Skill rename gov- prefix thin entry drive row forwarder shim deprecation-window probe pattern"`
