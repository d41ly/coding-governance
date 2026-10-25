# TOOL-dBoundRoles-19 — the roles kit's house text files moved into the overlay as level-5 units selecting their role, by their own upgrade step

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 24 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0184@923d7266 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-a.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-6 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-18 TOOL-dBoundRoles-20 TOOL-dBoundRoles-26 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |

<!-- /gen:spec-records -->

## 1. Goal

A repository's rules for a role live today in a seeded text file under the kit, `house/<role>.md`,
appended to the role under `## House rules` (`tools/roles/roles_lib.py:579-592`). A seed only adds: it
cannot amend or replace gov's text, and it is a second instruction home beside the repository's one
overlay (`gap-found-29`; IA-1, adopter-instructions.md:133-134). This unit moves the roles kit's house
text files, `house/*.md`, into `.governance/instructions.toml` as level-5 units selecting their role,
by their own upgrade step whose down restores them, renders them through the overlay's marked part,
and grades them where they now live. `house/policy.toml` stays, on the route the shapes give it.

## 2. Scope (IN)

- **S1** — The upgrade step (shared interface I21): one `[[upgrade]]` row in `tools/roles/kit.toml`,
  `id = "roles/house-overlays-to-instructions"`, in TOOL-dSafePassage-1 S1's grammar, its program
  `tools/govkit/steps/house_overlays_to_instructions.py` with `up`, `down` and `witness`, its
  `surfaces` one `file:` member per seeded `house/<slot>.md`. Observed by AC1 and AC2.
- **S2** — The up. For each `house/<slot>.md` in the target's roles kit directory, a non-empty file
  becomes one `[[unit]]` row written through `write_overlay_units` (PLAY-dOrderedCharter-32 S8, I22):
  `tag = "repo.house.<slot>"` (the `repo` namespace, PLAY-dOrderedCharter-32 S2), level 5 (`LEVELS[5]`,
  `role`, PLAY-dOrderedCharter-13 S1), selecting `role.<slot>`, its text the file's body with
  `{{MEMORY_ROOT}}` kept; then the file is removed. An empty file is removed with no unit. The up first
  writes TOOL-dSafePassage-1's before-image, so the down restores every file and the overlay
  byte-identical. The witness holds when no `house/*.md` remains and every moved body is a unit's text.
  Observed by AC1 and AC2.
  **Readers:** by name: `tools/roles/roles_lib.py` (its `render_role`) and `tools/roles/check_roles.py`
  (its R10), the two readers of a target's house text file ·
  by value: `render_role`'s `## House rules` append and R10's per-file grade, re-pointed to the units
  by S3 and S4; the kit-side readers of the shipped files are S5's clause.
- **S3** — The render. `render_role` stops reading `house/<name>.md` and appending `## House rules`;
  the role's level-5 repository units, those selecting `role.<slot>`, render in PLAY-dOrderedCharter-34
  S2's marked part, `<!-- gov:repo -->` to `<!-- /gov:repo -->`, after gov's text, read through
  `read_overlay` (PLAY-dOrderedCharter-32 S1) at the landed revision. Every consumer that hands a role
  to an agent still calls `render_role`, so the agent file and the handoff carry the same part.
  Observed by AC3.
- **S4** — The grade moves with the text. R10 in `tools/roles/check_roles.py` (:339-351) grades the
  overlay's level-5 units that select a `role.` tag instead of the files: a unit selecting a role no
  role file defines, a unit text carrying a `# ` or `## ` line, a token other than `{{MEMORY_ROOT}}`, or
  a protocol's file name, each named by its unit tag. Observed by AC4.
- **S5** — The seeds. The ten `house/*.md` files leave the kit and the seed rule of `tools/roles/kit.toml`
  (:31-40) keeps one path, `house/policy.toml`, which stays seeded and is read as the shapes route it:
  by workflow and stage only where no `roles.effort.*` key is set (TOOL-dBoundRoles-16,
  TOOL-dBoundRoles-21), until dConvergedCharter retires the seed. Observed by AC5.
  **Readers:** by name: `tools/roles/kit.toml` (the seed include list), `tools/roles/roles_lib.py`
  (`render_role`), `tools/roles/check_roles.py` (R10), `tools/roles/render_agents.py` (its self-test
  fixture writes and the `## House rules` arms), `tools/roles/adopt-roles.test.sh` (the token planted
  into `house/gov-builder.md`), `tools/govkit/selftest.py` (the OC8 checks that every house overlay is a
  seed row and that ten are seeded), `tools/roles/README.md`, `help/roles.md` and `WIRE-INTO-PROJECT.md` ·
  by value: `render_role`'s overlay append, R10's per-file walk, and the OC8 count of ten, each re-pointed
  to the overlay's level-5 units.
- **S6** — Gov first (P38). Gov's ten house files are 0 bytes at base, PINNED at `4283cb44`, so the
  step on gov's own tree removes them and writes no unit, and gov's rendered agent files are
  byte-identical before and after. Observed by AC3.
- **S7** — The prose that names the house files names the overlay: `help/roles.md` (:42-43, :126),
  `tools/roles/README.md` (:17-19, :275) and `WIRE-INTO-PROJECT.md` (:709-712), each saying a role's
  project rules are level-5 overlay units selecting it, written through the overlay's door. Observed by
  AC6.

## 3. Non-goals (OUT)

- The overlay file, its reader and writer, the `repo` namespace, levels and the marked part:
  PLAY-dOrderedCharter-32's, -13's and -34's, called here.
- The step kind, the before-image, `update`'s step order and the step gate: TOOL-dSafePassage-1's and
  -10's.
- The role tags `role.<slot>`: TOOL-dBoundRoles-14's, read here as the units' `select`.
- `house/policy.toml`'s fold into `roles.effort.*` keys and gate grants, and the seed's retirement:
  TOOL-dBoundRoles-21's re-pointing and dConvergedCharter's fold.
- A repository amending or replacing gov's role text through `amends` or `supersedes`: the overlay's
  composition does that for any unit (PLAY-dOrderedCharter-32 S4); a moved house file only adds, as it
  did.
- Renaming the two reviewers' units when they merge: TOOL-dBoundRoles-18 re-keys every overlay
  `select` the merge touches, these units included.

### Edges

- **consumes-from** `TOOL-dBoundRoles-14` — `role.<slot>`, the role tag each moved house unit's `select` names; without it a unit selects no role
- **consumes-from** external — PLAY-dOrderedCharter-32 S1, S2 and S8, -13 S1 and -34 S2, and TOOL-dSafePassage-1 S1 to S3, each specced and unbuilt at base `4ed9e567`; without them there is no overlay to move into and no step kind to move by

## 4. Design

### The row each file becomes

```toml
# .governance/instructions.toml, written by write_overlay_units, ordered by level then tag
[[unit]]
tag = "repo.house.gov-builder"
level = 5                       # LEVELS[5], "role"
select = ["role.gov-builder"]   # PLAY-dOrderedCharter-32 F1: S10's placement field, spelled as its reader lands it
text = """
<the body of house/gov-builder.md, verbatim>
"""
```

The tag is `repo.house.<slot>`: overlay units must sit in the `repo` namespace (PLAY-dOrderedCharter-32
S2), and `house` keeps the origin legible. The slot is the file stem, which `load_roles` already treats
as the role's identity (`roles_lib.py:330-336`) and which TOOL-dBoundRoles-14's `role.<slot>` tag
spells.

### The step

```toml
# tools/roles/kit.toml
[[upgrade]]
id = "roles/house-overlays-to-instructions"
up = ["python", "{gov}/govkit/steps/house_overlays_to_instructions.py", "up", "{target}", "{prefix}"]
down = ["python", "{gov}/govkit/steps/house_overlays_to_instructions.py", "down", "{target}", "{prefix}"]
witness = ["python", "{gov}/govkit/steps/house_overlays_to_instructions.py", "witness", "{target}", "{prefix}"]
surfaces = ["file:{prefix}/roles/house/gov-builder.md", "…one per seeded overlay…"]
needs-target = false
```

The program lives beside the precedent steps, `tools/govkit/steps/`, where TOOL-dSafePassage-1 S6 puts
agent-cap's and PLAY-dOrderedCharter-31 S4 puts `adopter_rules_to_overlay.py`, the exact precedent: a
seed's adopter text moved into the overlay by a step whose down restores it. The roles kit directory is
located in the target through `resolve_kit_dir("roles", "roles_lib.py", here)`, so an adopter that homed
the kit elsewhere is found by its receipt. A unit whose tag the overlay already holds refuses the up
and leaves both files byte-identical, as `write_overlay_units` refuses (PLAY-dOrderedCharter-32 S8).

### The render

```
render_role(kit_dir, name, memory_root) at base       after
  base body                                           base body
  "## House rules" + house/<name>.md, if non-empty    <!-- gov:repo --> units selecting role.<name> <!-- /gov:repo -->
```

`render_role` is the one composition every route calls (`roles_lib.py:11-13` docstring), so moving its
input moves the agent file, the handoff's `## Role` section and the role-sha that hashes it together.

### Inventory

Minted: the step id `roles/house-overlays-to-instructions`; the program
`tools/govkit/steps/house_overlays_to_instructions.py` (its name asked of `python tools/lexicon/lexicon.py
--suggest`); the unit tags `repo.house.<slot>`.

### Migration

The step is the migration. On gov's tree it removes ten empty files and writes nothing. On an adopter's
tree it moves each non-empty overlay into one unit, and a down restores the files.

### Rollout

The render reads the overlay from landing; the step runs at the adopter's next `update`. Between the
two, an adopter whose house file still exists keeps it unread, so `check_roles.py` prints one note per
remaining `house/*.md` naming the step that moves it, never a silent drop.

### Files touched (estimate)

- `tools/roles/kit.toml` (the `[[upgrade]]` row, the seed list)
- `tools/govkit/steps/house_overlays_to_instructions.py` (new)
- `tools/roles/roles_lib.py` (`render_role`)
- `tools/roles/check_roles.py` (R10 over the units, the leftover-file note)
- `tools/roles/render_agents.py` (its fixtures and arms)
- `tools/roles/adopt-roles.test.sh` (the token plant re-pointed, the arm of §7)
- `tools/govkit/selftest.py` (the OC8 checks re-pointed, the arm of §7)
- `tools/roles/house/` (the ten `.md` files removed; `policy.toml` stays)
- `.claude/agents/` and `.claude/roles.json` (renders, by `tools/roles/render_agents.py`)
- `tools/roles/README.md`, `help/roles.md`, `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- **Keep the files and read them as units.** Two homes for one kind of instruction; the overlay's
  composition and its report would not see them.
- **The program under `tools/roles/`.** Every specced step program sits under `tools/govkit/steps/`;
  a second location is a second place the step gate and `update` must look.
- **One unit for all ten roles.** A unit selects; ten rules for ten roles in one unit select ten roles
  and render each role's rules into every other.

## 5. Production-readiness checklist

- security — the overlay is the guarded instruction home (PLAY-dOrderedCharter-32); the step writes it
  only through its one writer, and the before-image makes the move reversible.
- perf / scale — ten files at most per target, once.
- error / empty / loading states — an empty file moves to nothing; a tag already present refuses with
  both files untouched; a leftover file after landing is a printed note.
- observability — the step's witness and the update report's instruction delta list each moved unit.
- risks — an adopter who edits a house file after landing and before update has that edit moved by the
  step, since the up reads the file as it is then; the down restores it.
- testing — the step's up, down and witness on a fixture target, and the render and R10 plants; the arms
  of §7 observed RED then GREEN by the main loop at the close.
- migration — the step, per §4.
- user docs — `help/roles.md` per S7.

## 6. Acceptance criteria

- **AC1** — When `python house_overlays_to_instructions.py up <fixture> tools` runs over a fixture target
  whose house text file for `gov-builder` holds one line and whose other nine are empty, the target's
  overlay gains one `[[unit]]` with tag `repo.house.gov-builder`, level 5 and select `role.gov-builder`,
  its text that line, no `.md` file remains in the target's roles `house` directory, and `witness`
  exits 0.
  Red when: an empty overlay writes a unit, a non-empty one is removed with no unit, or a file remains.
  fixture: a short-pathed target under `%TEMP%` holding a roles install and no overlay.
- **AC2** — When `down` runs after AC1's up, the ten files and the overlay are byte-identical to the
  fixture before the up, and `witness` exits 1.
  Red when: the down leaves the unit in the overlay or a file missing.
- **AC3** — When `bash adopt-roles.sh --scaffold` runs on AC1's target after the up, its
  `.claude/agents/gov-builder.md` carries the moved line between `<!-- gov:repo -->` and
  `<!-- /gov:repo -->` and no `## House rules` heading; on gov's own tree after the step, every agent file
  is byte-identical to its render before.
  Red when: the render still reads the house file, or drops the unit's text.
- **AC4** — When `python check_roles.py` runs on a fixture whose overlay holds a level-5 unit selecting
  `role.gov-nobody`, and one whose text carries a `## ` line, it exits 1 naming each unit's tag under R10.
  Red when: a unit selecting no role, or carrying a heading, passes.
- **AC5** — When `grep -n "house/" kit.toml` runs in `tools/roles/`, the only path it prints under a
  seed rule is the policy file `tools/roles/house/policy.toml`, and `python handoff.py stage-efforts
  spec-write` prints the same levels before and after the unit.
  Red when: a house text file is still seeded, or the effort route moved.
- **AC6** — When `grep -n "roles/house/<" help/roles.md` runs it prints nothing, and
  `grep -n "instructions.toml" help/roles.md` names the section saying where a role's project rules go.
  Red when: a page still sends an adopter to edit a house text file.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `lexicon naming predicates` · `check-wiring self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC3 AC4 · the moved line rendered in the marked part and the two R10 plants, staged by restoring the house-file read in `render_role` · none
New arm: tools/govkit/selftest.py · covers AC1 AC2 · the step's up, down and witness on a fixture target, staged by an up that skips the before-image · none

## 8. Open questions

- **F1 — What tag does a moved house file's unit take?** Options: (a) `repo.house.<slot>`; (b)
  `repo.<slot>`; (c) `role.adopter.<slot>`. (c) is a role row's tag, not a prose unit's, and the overlay
  refuses a non-`repo` unit tag (PLAY-dOrderedCharter-32 S2); (b) loses the origin, so a later unit the
  repository writes for the same role collides with it. RESOLVED (agent, 2026-10-25, delegated): (a),
  rung 3. options: (a) > (b) > (c) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes:
  none
- **F2 — Where does the step program live?** Options: (a) `tools/govkit/steps/`, beside every specced
  step; (b) `tools/roles/steps/`, as scout A read it. (b) is a second home for step programs.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, tie-broken by reuse of the precedent of
  PLAY-dOrderedCharter-31 S4. options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens:
  none · relaxes: none
- **F3 — The overlay, its writer, the marked part and the step kind are dOrderedCharter's and
  dSafePassage's, specced and unbuilt at base `4ed9e567`.** Options: (a) build against the specs and
  re-ground at the build run; (b) restate them. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, the
  brief's rule; the build run stops this unit if a section is still absent then. options: (a) > (b) ·
  pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 19, the brief's I21 and I22, scout A's row for
  cl-0184, and PLAY-dOrderedCharter-31, -32, -34 and TOOL-dSafePassage-1 at base `4ed9e567`.

## 10. Reuse audit

The seams extended are `render_role` (`tools/roles/roles_lib.py:579-592`), the one composition every
route calls; R10 (`tools/roles/check_roles.py:339-351`); the kit descriptor's seed rule
(`tools/roles/kit.toml:31-40`); and the precedent step PLAY-dOrderedCharter-31 S4, whose
`adopter_rules_to_overlay.py` moves another seed's adopter text into the same overlay through the same
writer. `python tools/codebase-map/reuse_lookup.py "move seeded role overlay text into the instruction
overlay"` ranked text helpers (`read_text`, `write_text`, `load_text`) and the kit's `seed` test helpers,
none a mover, which matches scout A: no overlay exists at base. The recall probe returned scout A's row,
this build's brief row and the night pass's clause rewrite; none disagreed with source. Scout A read the
seed rows at `kit.toml:35-40`; at `4283cb44` the rule opens at `:31` with its comment and its include list
spans `:35-39`.

Recall terms used: `python tools/memory-recall/query.py "how do the roles kit house overlay files move into the instruction overlay" --terms "house overlay level-5 unit instructions.toml write_overlay_units upgrade step seed render_role House rules"`
