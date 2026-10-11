# TOOL-aOrientedCast-8 — the roles kit is an adopter default: installed, rendered and reported at install and update

**Status:** INPROGRESS · rev-4 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 |
| [2026-10-11-prompt-TOOL-aOrientedCast-8-1-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-8-1-fold-brief.md) | journal | TOOL-aOrientedCast-6 |
| [2026-10-11-prompt-TOOL-aOrientedCast-8-2-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-8-2-fold-brief.md) | journal | — |
| [2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md) | journal | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-9 |

<!-- /gen:spec-records -->

## 1. Goal

The role catalogue, its native agent types and the `/build` Skill bind only where they are installed
and rendered, and today no adopter receives them. This unit registers the roles kit, makes it a
member of govkit's default selection, declares what each of its files and legs is to an adopter,
completes its one adopter so it renders `.claude/agents/`, `.claude/roles.json` and the `/build`
Skill at install and at update behind one `--check` the bar runs, and makes `check-wiring.sh` report
an install left unrendered or rendered with CR bytes. It follows `TOOL-aRoutedQuill-5`'s shape for a
default that arrives wired.

## 2. Scope (IN)

- **S1** — `tools/govkit/registry.toml` gains an `[[entry]]` with `id = "roles"` and
  `descriptor = "{prefix}/roles/kit.toml"`, and `[selection] default` gains `"roles"` after
  `"check-wiring"` with a comment naming this unit. Observed by AC1 and AC2.
- **S2** — `tools/roles/kit.toml`, which `TOOL-aOrientedCast-1` leaves identity-only, declares every
  file the kit ships by role:
  - `include = "**"`, `role = "engine"`: the base role files, `workflows.toml`, the library, the
    checker, the renderers, the adopter, the README and the Skill template, overwritten on every
    update.
  - `role = "seed"`: the ten house overlays under `house/`, each named literally, because a list
    include claims literal paths only. An adopter receives each once and owns it afterwards.
  - `role = "project-owned"`: `adopt-roles.test.sh` and every other `*.test.sh` or fixture file the
    kit holds when this unit builds, each named literally, so the payload withholds them. A
    `--selftest` flag inside a shipped script ships with that script as `engine`.
  - `role = "rendered"`: `SKILL.template.md`, `to = ".claude/skills/build/SKILL.md"`, with
    `placeholders = ["KIT_DIR", "TOOL_ROOT", "MEMORY_ROOT"]`, the three tokens the adopter
    substitutes by their literal spellings.

  Observed by AC2, AC3 and AC8.
- **S3** — The descriptor's dependencies:
  - `requires = ["kickoff-manifest", "memory-tree"]`. The card every `task:` and `card:` input is
    read from is written by the kickoff kit's card writer. `roles_lib.py` and the adopter read the
    memory root and the governing doc's path from `.memory-tree.conf`.
  - `requires_if` names `review-harness`, which ships the three harnesses `workflows.toml` names;
    §8 F1 settles why it is not a plain requirement.
  - `[config]` declares `.memory-tree.conf`, owned by `memory-tree`, with `MEMORY_ROOT` and
    `CHARTER` among its optional keys.

  Observed by AC2.
- **S4** — `tools/roles/adopt-roles.sh`, which `KICK-aOrientedCast-2` creates to render the Skill,
  gains the agent render in both modes. `--scaffold` also runs `render_agents.py --write` and passes
  its output through, the restart notice included. `--check` also runs `render_agents.py --check`
  and exits 1 when either compare fails, naming each stale or absent artifact and the `--scaffold`
  remedy. The usage refusal, the token substitution and the stage binding stay as that unit builds
  them. A governing doc that `CHARTER` in `.memory-tree.conf` leaves blank, absent or naming no file
  is a declared outcome, not a refusal (§8 F3): both modes still render or compare the Skill, skip
  the agent types and the role index, print one line naming the missing doc and the `CHARTER` key,
  and exit 3. Observed by AC4, AC5 and AC13.
- **S5** — The descriptor wires the adopter as govkit expects of a kit with a `rendered` row:
  `[adopt]` and `[[regenerate]]` run `--scaffold`, so an update re-renders unless
  `GOVKIT_RERENDER=0` declines it; `[check]` runs `--check`; and `[[outcome]]` reads code 0 with
  `.claude/roles.json` present as `adopted`. A second `[[outcome]]` reads code 3 with the rendered
  Skill present as `no-governing-doc`, `ok = true`, so an apply whose adopter met no governing doc
  succeeds, as the memory-tree kit's `not-rendered-here` row is accepted. Observed by AC1, AC4 and
  AC13.
- **S6** — Every leg the roles kit carries is claimed, each with the subject and ceiling its
  manifest row carries:
  - `roles render wiring`, which `TOOL-aOrientedCast-3` lands running `render_agents.py --check`, has
    its manifest `argv` re-pointed at `adopt-roles.sh --check` and is claimed as a `[[gate_leg]]`,
    `subject = "repo"`. One leg grades the agent types, the index and the Skill together.
  - `roles render selftest` is claimed as a `[[gate_leg]]`, `subject = "kit"`.
  - `roles catalogue`, `TOOL-aOrientedCast-1`'s, is claimed as a `[[gate_leg]]`,
    `subject = "repo"` (§8 F2).
  - `roles adopter self-test`, which S12 adds, is carried by an `[[exempt_leg]]` row in the
    registry, because its suite is withheld from the payload.

  Observed by AC1 and AC9.
- **S7** — The descriptor declares the kit's outputs:
  - A `[[generated]]` row for `.claude/agents` and one for `.claude/roles.json`, each with
    `generator = "render_agents.py"`. The unattended kit then reads a pass's re-render as a generated
    write rather than an undeclared one.
  - Three `[[lf_pin]]` rows, for `.claude/agents/*.md`, `.claude/roles.json` and
    `.claude/skills/build/SKILL.md`, because `--check` byte-compares all three.

  Observed by AC1 and AC3.
- **S8** — `tools/check-wiring.sh` gains `check_roles`, called after `check_routed`:
  - `skip` when no roles kit resolves, through the receipt first and then the probe, by its
    `workflows.toml`.
  - `UNWIRED` naming the doc and the `CHARTER` key when the kit resolves and `CHARTER` in
    `.memory-tree.conf` is blank, absent or names no file (§8 F3). This is read first, so the line
    names the cause rather than the artifacts it left unrendered. The remedy names writing that doc,
    `adopt-roles.sh --scaffold` and a new session.
  - `UNWIRED` when the kit resolves and any of these is absent: `.claude/roles.json`; a
    `.claude/agents/<name>.md` for a role file not declaring `agent: false`; the rendered Skill. The
    remedy names `adopt-roles.sh --scaffold` and a new session.
  - One `note` per harness path the role index lists that the tree does not hold, naming the kit
    that ships it.
  - `ok` otherwise.

  `check_eol`'s population gains a third named glob, the tracked `.claude/agents/*.md` and
  `.claude/roles.json` carrying the `eol=lf` pin, so a CRLF render is reported and `--fix` rewrites
  it as it does a rendered Skill. `tools/check-wiring.test.sh` gains the arms for both, and one for
  the missing governing doc. Observed by AC6 and AC13.
- **S9** — `tools/check-kit-versions.sh` gains the roles kit's carrier row: the kit resolved by its
  `roles_lib.py`, a `need` row for `KIT_ROLES_VERSION` there, and a pair check that the
  `gov:kit roles@` marker in the kit's README equals that constant. Observed by AC10.
- **S10** — `tools/govkit/selftest.py` gains two module-level functions `main()` calls, so a slice
  can run either alone:
  - `check_roles_default`, over gov's own registry and descriptors: `roles` is in the default set
    and the default's requirements close over it; `roles` without `kickoff-manifest` is an
    unsatisfied requirement; an aged registry lacking `roles` makes `derive_default_gained` gain it
    and an unmoved one gains nothing; the house rows are `seed`, the Skill row is `rendered` with a
    `[[regenerate]]` present, and the test rows are `project-owned`.
  - `check_roles_install`, a default `apply` into a scratch target holding, before the apply, a
    governing doc at the path the memory-tree seed writes as `CHARTER`, copied from gov's own
    `AGENTS.md`: the role index, nine agent types, ten seeded house overlays and the Skill are
    present; the target's `adopt-roles.sh --check` exits 0; its `check-wiring.sh --check` reads `ok`
    for `roles`, and `UNWIRED` once the index is absent. With `charter=False` it writes no doc, and
    asserts AC13's shape instead.

  The default-plan arm in `main()` re-pins its `SIDE|rendered`, `seed` and `ORDER|project-owned`
  figures to the plan this unit produces. Observed by AC2, AC3 and AC4.
- **S11** — `WIRE-INTO-PROJECT.md` gains a section anchored `<!-- govkit:entry roles -->` after the
  lexicon kit's section. It says what the default install renders, that the house overlays are the
  adopter's to edit, that a session must restart before it can spawn a newly rendered agent type,
  and that the `/build` route needs the review harness. The "Result" list gains the rendered agent
  types and the Skill. The kit's README gains an adopting section. Observed by AC7.
- **S12** — `tools/roles/adopt-roles.test.sh`, the adopter's self-test, holds the regression arms
  `KICK-aOrientedCast-2` hands this unit: a stage heading naming a workflow at the wrong stage, a
  catalogue workflow no heading names, a token surviving the substitution, a byte appended to a
  rendered agent type, and an unknown argument. It prints its executed assertion count against a
  floor in the shape `check-testsuite-counts.sh` reads, and its leg `roles adopter self-test` enters
  `tools/gate-legs.json` (`kit`, `selftests`, ceiling 300, unguarded) with a row in
  `tools/run-gates/selftest-budgets.txt`. Observed by AC11.
- **S13** — The map's generated artifacts are regenerated for the new shell and Python functions,
  and the roles kit's dossier claims `roles adopter self-test`; the other leg names are already
  claimed there by `TOOL-aOrientedCast-1` and `TOOL-aOrientedCast-3`. Observed by AC9.
- **S14** — The roles kit's files stop spelling what the install-prefix ban reads as a kit path.
  `check-install-prefix.sh --offenders` names nine keys in three files earlier units of this build
  created, and none is a path into a sibling kit: three are front-matter key tuples whose quoted
  `"tools"` is followed by a comma and a quoted segment (the predicate's rule 1), and six are the
  agent-render self-test's fixture layout, which types the `roles` and `workflows` kit names as quoted
  path segments or under a literal prefix (rules 3 and 4). Each is respelled, never waived, since the
  ban carries no waiver:
  - `tools/roles/roles_lib.py` `FRONT_MATTER_KEYS` and `tools/roles/render_agents.py` `CLAUDE_KEYS`
    become `tuple("<key> <key> …".split())` over the same keys in the same order, because
    `CLAUDE_KEYS`'s order is the order a rendered type carries them.
  - `tools/roles/check_roles.py`'s agent-role loop reads `for k in "tools model".split():`.
  - `build_fixture`'s kit directory is `root / "toolroot" / KIT_DIR.name`, the kit's own directory
    derived from `__file__`, as the authoring rule asks of a kit's own name.
  - `build_fixture`'s harness directory, and the expected harness paths in `run_selftest`'s arms 5 and
    10, are the drained spellings the fixture's own workflow table already writes, formatted with its
    tool root: `"{prefix}/workflows/a.js".format(prefix="toolroot")`, its `missing.js` sibling, and the
    parent of the first for the stub directory. The expected values then come from the table's
    spelling rather than a second literal of it.

  Observed by AC12.

## 3. Non-goals (OUT)

- The catalogue, the library, the handoff renderer, the agent render and the Skill. This unit
  installs and claims them and writes none of their content beyond S14's respelling.
- The role arms of the write gate and the spawn guard. They ship in the hooks kit, already a default,
  and arm on `.claude/roles.json`, which this unit is what renders at an adopter.
- Moving the review harness into the default selection (§8 F1).
- New shapes in `tools/govkit/matrix.py`. Fixture targets go through `tools/govkit/selftest.py`
  functions a slice can run; the matrix's shape 6 already installs the default and runs at the close.
- Gov's own `.governance/deploy.toml` `kits` array, which is the charter unit's.
- A kit-version bump. The roles, check-wiring and check-kit-versions kits move once, after this
  build's last unit.

### Edges

- **consumes-from** `TOOL-aOrientedCast-1` — the kit directory, its identity-only `kit.toml`,
  `roles_lib.py` with `KIT_ROLES_VERSION`, the README's `gov:kit roles@` marker, the `agents/` and
  `house/` layout, `workflows.toml`, the `roles catalogue` leg, and the dossier claiming the kit's
  keys. Without them there is nothing to register, install or claim.
- **consumes-from** `TOOL-aOrientedCast-3` — `render_agents.py --write` and `--check`, the
  `roles render wiring` and `roles render selftest` legs, and gov's committed render. Without them the
  adopter renders no agent type and there is no leg to re-point.
- **consumes-from** `KICK-aOrientedCast-2` — `SKILL.template.md`, `adopt-roles.sh` with
  `render_skill`, its two modes and its three tokens, and gov's committed Skill. Without them there is
  no adopter to complete and the `rendered` row names no template.
- **hands-off** `PLAY-aOrientedCast-1` — the `roles` registry entry that the charter's `kit:roles`
  fence and gov's `kits` array name.
- **hands-off** external — whether `review-harness` joins the default selection, which widens every
  adopter's install and is the owner's to decide (§8 F1).
- **hands-off** external — an ask: whether the memory-tree seed or govkit derives `CHARTER` from
  the path the playbook lands at, so a default install's governing doc is the one it installed. It
  changes another kit's install behaviour, a public surface M3's veto 2 keeps for the owner (§8 F3).

## 4. Design

### Evidence

Read at `744e55db` on 2026-10-11, which is BASE `646d4a73` plus this build's three record commits.
The sibling specs of this build were read as they stood while this one was written.

- The default selection is `tools/govkit/registry.toml:38-51`. No entry is `roles`.
  `TOOL-aRoutedQuill-5` added `agent-cap`, `settings-merge` and `check-wiring` there, and
  `update --write` installs an entry the default gained after a receipt's vintage
  (`derive_default_gained`, `tools/govkit/govkit.py:970`), running its adopter as `apply` would.
- `TOOL-aOrientedCast-1`'s spec leaves `kit.toml` with no `[[files]]` row and hands this unit the
  registry entry, the default selection, every file's govkit role and the version-gate carrier row;
  its `roles catalogue` leg is `repo`, ceiling 120, unguarded. `TOOL-aOrientedCast-3`'s spec lands
  `roles render wiring` (`repo`, `wiring`, ceiling 300) and `roles render selftest` (`kit`,
  `selftests`, ceiling 300), both unguarded, and hands this unit the re-pointing, the claims and the
  wiring check's report of an unrendered or CRLF render. `KICK-aOrientedCast-2`'s spec creates the
  adopter with `--scaffold`, `--check` and `render_skill` and the three tokens, adds no leg of its
  own, and hands this unit the agent render inside the adopter, the placeholder declaration, the leg
  over its check mode and the regression arms for its stage binding and surviving-token refusal.
- A requirement orders an install and never pulls a kit in, and `apply` refuses a selection whose
  requirement is unsatisfied (`derive_install_order`, `derive_unsatisfied_requires`,
  `govkit.py:905-969`). A `requires_if` row is a declaration selfcheck grades and installs nothing,
  and its kit must be a registry entry (`govkit.py:2427-2443`);
  `tools/govkit/entries/check-wiring.kit.toml:9` is the precedent with no condition key.
- The roles `ROLE_KINDS` admits are `engine`, `seed`, `rendered`, `generated`, `project-owned`,
  `merged` and `forked` (`govkit.py:3641-3649`). `update` never rewrites a `seed` row and reports a
  moved one (`:8082`), and re-runs the adopter for a `rendered` one (`:8085`).
- A `[[generated]]` row needs a path whose only tokens are `{memory_root}`, `{map_root}` or `{kit}`,
  a generator file beside the descriptor and a reason (`govkit.py:2398-2413`). The unattended kit
  reads every descriptor's rows into its generated set (`tools/unattended/lib-unattended.sh:717-736`).
  `govkit.py selfcheck` reports 6 such rows at `744e55db`.
- The kit-placeholders gate reads the `[adopt]` argv's script textually and admits only a
  `{kit}/*.sh` (`tools/check-kit-placeholders.py:86`, `:124-142`); the adopter substitutes all
  three tokens by their literal spellings.
- `tools/runlog/kit.toml` is the closest shape: an engine `**` rule, literal `project-owned` rows,
  one `rendered` Skill row, an adopter with `--scaffold` and `--check`, a `[[regenerate]]`, an
  `[[outcome]]`, an unguarded wiring leg and an `[[lf_pin]]` for the render.
- Selfcheck reds a manifest leg no registered descriptor claims and no `[[exempt_leg]]` carries, a
  leg both exempted and claimed, a descriptor leg whose subject or ceiling disagrees with the
  manifest (`govkit.py:2760-2876`), and a leg naming its own descriptor's `project-owned` path, which
  moves to an `[[exempt_leg]]` row (`:3129-3131`). It reds a depth-1 path under the tool root that is
  neither an entry nor an exemption.
- `tools/govkit/check_runbook_parity.py:60` pins 18 problems as an EQUALITY, and each problem is a
  registry entry with no anchored runbook section. `WIRE-INTO-PROJECT.md:609` anchors the lexicon
  kit, and `:658` opens section 4.
- `check-wiring.sh` resolves a kit file through the receipt and then the probe (`resolve_kit_file`,
  `tools/check-wiring.sh:478`). Only `UNWIRED` moves its exit code (`:1767`), the arms run in order
  at `:1753-1764`, and `check_eol`'s population is two named globs (`:1022-1026`).
- `tools/check-kit-versions.sh` resolves each carrier's kit by an anchor file (`:116-118`), and its
  rows are a declaration; it reports 16 carriers clean at `744e55db`.
- `tools/run-gates/selftest-budgets.txt` must carry a row for every held self-test leg, and
  `unattended adopter e2e` is the precedent row for an adopter's suite.
- The default-plan arm pins `SIDE|rendered` at 5 (`tools/govkit/selftest.py:5998`) and `seed` at 3
  with `ORDER|project-owned` at 31 (`:6027-6028`), inside `main()`, which a slice cannot reach.
- The agent-type probe recorded under this build's `build/` folder measured a definition created in a
  running session as not spawnable, citing `TOOL-aReplayedCard-5`.

### The adopter, after this unit

| Mode | Writes | Exit |
|---|---|---|
| `--scaffold` | the rendered Skill, `.claude/agents/<name>.md` per agent role, `.claude/roles.json` | 0; 1 a token survived, a stage disagrees or the agent render refused; 2 a derivation or the conf failed; 3 no governing doc at `CHARTER`, the Skill alone written and the doc and key named |
| `--check` | a temporary Skill render only | 0 fresh; 1 each stale or absent artifact named, with `--scaffold`; 2 as above; 3 no governing doc at `CHARTER`, the Skill alone compared and the doc and key named |
| anything else | nothing | 2, usage |

### The legs, after this unit

| Leg | argv | Subject | Claimed by |
|---|---|---|---|
| `roles catalogue` | `check_roles.py` | repo | `[[gate_leg]]` |
| `roles render wiring` | `adopt-roles.sh --check`, re-pointed from `render_agents.py --check` | repo | `[[gate_leg]]` |
| `roles render selftest` | `render_agents.py --selftest` | kit | `[[gate_leg]]` |
| `roles adopter self-test` | `adopt-roles.test.sh` | kit | registry `[[exempt_leg]]` |

### The check-wiring arm, in lines

```text
skip     roles     — the roles kit is not installed here
UNWIRED  roles     — the roles kit is installed and CHARTER in .memory-tree.conf names <doc>, which is not a file, so no agent type is rendered. Fix: write that doc or point CHARTER at it, run bash <kit>/adopt-roles.sh --scaffold, then start a new session
UNWIRED  roles     — the roles kit is installed and <artifact> is not rendered, so no role agent can be spawned and the role-aware gates are unarmed. Fix: bash <kit>/adopt-roles.sh --scaffold, then start a new session
note     roles     — <harness path> is named by the role index and absent here; /build cannot drive it until the review harness is installed
ok       roles     — <n> agent types, the role index and the /build Skill are rendered
```

The harness half reads the role index with the resolved python and is a `note` naming its cause when
none resolves. The arm's header states what it does not check: whether a rendered file is fresh,
which is the leg's question, and whether a house overlay is sensible, which is `roles catalogue`'s.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `check_roles` | function in `check-wiring.sh` | `sh.function`; `lexicon.py --suggest` answered OK |
| `check_roles_default`, `check_roles_install` | functions in `selftest.py` | `py.function`; each answered OK |
| `roles adopter self-test` | gate leg | none |

### Files touched (estimate)

`tools/govkit/registry.toml` · `tools/govkit/subject-pins.tsv` · `tools/govkit/selftest.py` · `tools/roles/kit.toml` · `tools/roles/adopt-roles.sh` · `tools/roles/adopt-roles.test.sh` · `tools/roles/README.md` · `tools/roles/roles_lib.py` · `tools/roles/check_roles.py` · `tools/roles/render_agents.py` · `tools/gate-legs.json` · `tools/run-gates/selftest-budgets.txt` · `tools/check-wiring.sh` · `tools/check-wiring.test.sh` · `tools/check-kit-versions.sh` · `WIRE-INTO-PROJECT.md` · `memory/map/features/roles.md` · `memory/map/generated/symbols.json` · `memory/guides/SESSION-KICKOFF.md`

### Rollout

- Lands at order 7, before `PLAY-aOrientedCast-1` at 8, because the charter's fence needs this
  unit's registry entry; that spec's §8 F1 resolved the swap.
- In gov, `adopt-roles.sh --scaffold` writes bytes identical to what the catalogue's renderers
  already committed, so gov's tree does not move; AC5 is that observation.
- `tools/gate-legs.json` is watched, so the unit's commit re-stamps `last-audit` in the kickoff
  manifest, naming its parent. `govkit.py selfcheck --write` regenerates the subject pins after the
  leg rows move.
- The budget row is PINNED by declaration at 60 seconds, the file's floor, and re-priced from the
  first measured run.
- This session's hooks and SessionStart run from the primary tree, so the new `check-wiring` arm
  reaches this session only after landing.
- At an adopter, the next `govkit update --write` prints `default-gained` for `roles`, installs it,
  seeds the house overlays and runs the adopter. Its role-aware gates arm on the role index from that
  update, which is the owner's no-warn-phase ruling reaching adopters. The update leaves everything
  staged for the adopter to read, and the agent types are spawnable from the next session.

### Alternatives rejected

- **A second shipped leg over the same output.** `TOOL-aOrientedCast-3` named its wiring leg for this
  unit so one row is re-pointed; two legs would grade one adopter's render twice.
- **Declaring the agent types as `rendered` rows.** A `rendered` row is one template with
  substituted tokens, and an agent type is the base role, the house overlay and front matter composed
  by a program. `[[generated]]` is the declaration for a program's output.
- **Leaving the outputs undeclared.** Every unattended pass that edits a role file would then have
  to list `.claude/agents` in its `--dispatch` write set, or be counted as writing outside it.
- **Grading freshness in `check-wiring.sh`.** It runs at SessionStart on hosts that may lack
  python; presence is cheap and freshness is the leg's.
- **Matrix shapes for the install.** A matrix run costs the suite; a `selftest.py` function costs one
  apply and can be sliced, which is how the brief asks fixture targets to run.

## 5. Production-readiness checklist

- security — Every default adopter gains `.claude/agents/` definitions whose bodies are gov's role
  blocks plus the adopter's own house overlays. The role index arms the role-aware write gate and
  spawn guard, which narrow writes rather than widen them. The adopter writes only under `.claude/`
  and refuses an unrecognised mode.
- perf / scale — `--check` is two renders and two byte compares, seconds per bar. The new
  `check-wiring` arm is a few `test -f` calls and one python read.
- error / empty / loading states — An install that rendered nothing reads `UNWIRED` naming the
  remedy. A role index naming an absent harness reads `note`. An empty house overlay adds nothing to
  its role.
- observability — `default-gained`, the adopter's written paths and its restart line, the leg's
  stale-artifact lines, and one `check-wiring` line per state.
- risks — Every default adopter's main loop is refused spec and product writes from its first update
  after the role-aware gates land, which is the intended change. A session that ran the update
  cannot spawn the new types until it restarts. An adopter whose governing doc lacks a section a role
  names reds `roles catalogue`. The selftest's default-plan pins move, and the matrix's shape 6 now
  runs the roles adopter inside its default install.
- testing — Arms in `tools/govkit/selftest.py`, `tools/check-wiring.test.sh` and the adopter's own
  suite, each observed through a slice.
- migration — `govkit update --write` is the migration, through `derive_default_gained`.
- user docs — the anchored runbook section and the kit README's adopting section (S11).

## 6. Acceptance criteria

`govkit apply` copies gov's COMMITTED bytes into the target, so AC3, AC4 and AC13 are observable
only after the pass commit. They are observed against the committed tree, and their ledger lines
land in a follow-up commit carrying `Pass: none`. This is the one unit of the build whose acceptance
follows its commit.

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 with `0 unclaimed`, every
  roles-kit leg is counted claimed or exempt, and its generated-outputs note counts the two rows this
  unit declares beside every other descriptor's.
  Red when: the descriptor ships a `rendered` row with no `[[regenerate]]`, a `[[generated]]` row is
  malformed or declared twice, or a claimed leg's subject or ceiling disagrees with the manifest.
  figure: DERIVED; the note read 6 rows at `744e55db`, and other units of this build may add rows.
- **AC2** — When `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import selftest as s; s.check_roles_default(); print(s.FAILURES)"`
  runs, it prints `[]`. With `"roles",` taken out of the registry's default set, a staged break
  restored afterwards, it prints a failure naming the default-set arm.
  Red when: `roles` is not a default, a default requirement is unsatisfied, the card writer is not a
  requirement, the aged registry gains nothing, or a house row is not `seed`.
- **AC3** — When `python tools/govkit/govkit.py plan --target <scratch>` runs against a scratch target
  under a short `%TEMP%` root holding matrix shape 6's `deploy.toml` and no `kits` list, the plan
  previews the ten house overlays as `seed` writes, the Skill as a `SIDE` rendered row, the kit's
  test files as `ORDER` project-owned rows, and three `.gitattributes` rows. Its mark counts equal
  the figures `grep -n "SIDE|rendered\|write|seed\|ORDER|project-owned" tools/govkit/selftest.py`
  shows the default-plan arm pinning.
  Red when: an overlay previews as an engine write, the Skill row is absent, or a pin disagrees.
  figure: DERIVED from the plan output at observation.
  fixture: a scratch target, built the way matrix shape 6 builds one.
- **AC4** — When `python -c "import sys, pathlib, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; s.check_roles_install(pathlib.Path(tempfile.mkdtemp(prefix='or'))); print(s.FAILURES)"`
  runs, it prints `[]`, and the scratch target it installed holds `roles.json`, nine `gov-*.md`
  agent types, ten house overlays and the `/build` Skill. With the agent render staged out of the
  adopter's `--scaffold`, it prints a failure naming a missing agent type.
  Red when: the install leaves an artifact unrendered, or an absent harness reads `UNWIRED`.
  cost: one default apply into a scratch target under `%TEMP%`, minutes.
  fixture: matrix shape 6's target plus a governing doc at the seed's `CHARTER` path, copied from
  gov's `AGENTS.md` before the apply, since the shape lands the playbook under the target's docs folder as PARALLEL.md.
- **AC5** — When `bash <prefix>/roles/adopt-roles.sh --check` runs in gov, where the prefix is
  `tools`, it exits 0. After one byte is appended to `gov-builder.md` under `.claude/agents/`, it
  exits 1 naming that file and the `--scaffold` remedy. `bash <prefix>/roles/adopt-roles.sh --scaffold`
  then restores it, and `git diff --exit-code -- .claude/` exits 0. The same holds for a byte
  appended to the Skill.
  Red when: a stale render passes, or the scaffold writes bytes the renderers' own `--check` rejects.
- **AC6** — When the role index is deleted in the AC4 target, `bash <prefix>/check-wiring.sh --check`
  prints `UNWIRED  roles` naming `roles.json` and `adopt-roles.sh --scaffold` and exits 1, and
  `--session` prints the same line and exits 0. After `--scaffold` it prints `ok`, and one `note` per
  harness the role index names and the target lacks. With CR bytes written into one rendered agent
  type, the eol arm names that file. A slice of the check-wiring self-test holding its prologue and
  the new roles block passes, and fails with `check_roles` staged to print `ok` unconditionally.
  Red when: an unrendered install reads `ok` or `skip`, a CRLF agent type passes the eol arm, or an
  absent harness reads `UNWIRED`.
- **AC7** — When `python tools/govkit/check_runbook_parity.py` runs, it prints `18 problem(s) · pin 18`
  and no line naming `roles`, and `grep -n "govkit:entry roles" WIRE-INTO-PROJECT.md` prints one line.
  Red when: the registry carries `roles` with no anchored section, or the section's body is empty.
- **AC8** — When `python tools/check-kit-placeholders.py` runs, it exits 0, and its `--list` row for
  the roles kit names `adopt-roles.sh` with no missing token. With one extra token declared on the
  Skill row, a staged break, it exits 1 naming that token.
  Red when: a declared token is not substituted in the adopter, or the kit's row is absent.
- **AC9** — When `grep -c "roles render wiring" tools/gate-legs.json` runs it prints 1 and the row's
  argv names `adopt-roles.sh --check`, and `python tools/codebase-map/test_codebase_map.py` passes.
  Red when: a second leg grades the same render, the re-pointed row still runs the agent render
  alone, a roles-kit leg is unclaimed by the dossier, or the generated symbols are stale.
- **AC10** — When `bash tools/check-kit-versions.sh` runs, it prints `clean` over one carrier more
  than the 16 it counted at `744e55db`. With the README's `gov:kit roles@` marker changed to a
  value the constant does not hold, a staged break, it exits 1 naming the README.
  Red when: the roles kit's constant or marker can drift with this gate green.
  figure: PINNED at `744e55db`; a carrier another unit adds moves the base.
- **AC11** — When a slice of the adopter's self-test holding its prologue and one arm runs, once per
  arm, each passes against the adopter as built, and each fails against a copy with the behaviour it
  pins staged out: the stage binding, the surviving-token refusal, the agent-type compare and the
  usage refusal. `bash tools/check-testsuite-counts.sh` then reports the suite's count shape clean.
  Red when: an arm passes against the copy whose behaviour it pins was staged out.
  cost: four slices, each seconds.
- **AC12** — When `bash tools/check-install-prefix.sh --offenders` runs, it prints no key naming
  `tools/roles/check_roles.py`, `tools/roles/render_agents.py` or `tools/roles/roles_lib.py`, where it
  printed the nine of S14 at `8bf164d40`. Each file's own behaviour is then re-observed by its existing
  direct check: `python tools/roles/check_roles.py` exits 0 over gov's catalogue, and exits 1 naming
  `R2` and `'tools' is absent on an agent role` with the `tools:` line deleted from
  `gov-builder.agent.md` under the kit's `agents/`, a staged break restored afterwards;
  `python tools/roles/render_agents.py --selftest` prints PASS with its assertion count unmoved; and
  `python tools/roles/render_agents.py --check` exits 0 over gov's committed render, so the key order
  a rendered type carries did not move.
  Red when: any of the nine keys still prints, the ban is answered by a waiver or a marker, a
  respelled tuple changes a key or its order, or the self-test's fixture lays out a different tree.
  figure: PINNED at `8bf164d40`; another unit adding a roles-kit offender moves the set.
- **AC13** — When `python -c "import sys, pathlib, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; s.check_roles_install(pathlib.Path(tempfile.mkdtemp(prefix='or')), charter=False); print(s.FAILURES)"`
  runs, it prints `[]`: in matrix shape 6's target with no doc at `CHARTER`, the default `apply`
  exits 0, the `/build` Skill is rendered, no `.claude/agents/` file and no `.claude/roles.json` is
  written, and the target's `check-wiring.sh --check` prints `UNWIRED  roles` naming the doc and
  `CHARTER`.
  Red when: the adopter exits an undeclared code on an absent governing doc. That is the adopter at
  rev-3 behaviour, which the builder observed failing the apply with `R0 — CHARTER names AGENTS.md,
  which is not a file` and exit 1.
  cost: one default apply into a scratch target under `%TEMP%`, minutes.
  fixture: matrix shape 6's target as it builds one, with no governing doc written.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit runbook parity` · `govkit refusal join` · `check-wiring self-test` · `kit placeholders (a declared token its adopter substitutes)` · `install-prefix (shipped surface)` · `remote literals (kit code names no remote)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `playbook parity` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `roles catalogue` · `roles render selftest` · `transition-audit arms` · `straggler-guard arms` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `spec tokens (a spec's own names resolve)`

The roles kit's legs this unit claims and re-points, `roles catalogue`, `roles render wiring` and
`roles render selftest`, and the one it adds, `roles adopter self-test`, are kept off the line above
because none is in the manifest at BASE and the leg join reads the manifest as it stands; they enter
it at orders 1, 3 and here, and the close's bar runs every leg. At rev-3 `roles catalogue` and
`roles render selftest` join the line, because S14 re-observes both and orders 1 and 3 have put them
in the manifest; `install-prefix (shipped surface)`, S14's own leg, was already on it.

New arm: tools/govkit/selftest.py · covers AC2 AC3 AC4 AC13 · a registry default without roles, an aged registry stubbed through blob_at, a descriptor whose house rows are engine, an adopter whose agent render is staged out, and the rev-3 adopter meeting no governing doc · none

New arm: tools/check-wiring.test.sh · covers AC6 AC13 · a fixture holding the roles kit with no role index rendered, then with one, then with a CRLF agent type, then with no doc at CHARTER, then a fixture without the kit · none

New arm: tools/roles/adopt-roles.test.sh · covers AC11 · copies of the adopter with its stage binding, its surviving-token refusal, its agent compare or its usage refusal staged out · a new floor at the suite's first count

## 8. Open questions

- **F1 — Does `roles` require `review-harness`, and does that kit join the default selection?**
  `/build` and the harness-arguments verb drive the three harnesses `workflows.toml` names, and all
  three ship in `review-harness`, which is not a default.
  (a) A plain requirement, with `review-harness` joining the default so the default closes. Every
  default adopter can run `/build` out of the box, and every default install gains a kit the owner's
  ruling did not name.
  (b) A `requires_if` row, which installs nothing, plus the `check-wiring` note naming each absent
  harness. The role agents, the handoffs and the gates work everywhere, and `/build` needs the
  adopter to install the review harness.
  (c) A plain requirement with only `roles` joining the default, which makes `apply` refuse every
  default install. It fails AC4.
  Recommendation: (b). Option (a) widens what every adopter installs by an entry the owner did not
  rule on, which is veto 2's public-surface clause and so not a delegated pick; (c) fails a criterion.
  The widening goes to the wrap-up as the owner's follow-up.
  RESOLVED (agent, 2026-10-11, delegated): (b), a `requires_if` row and a `check-wiring` note per absent harness.
  Re-decided at rev-2 by the M2 cross-read's finding 9. As first written, the catalogue checker's R9
  and the agent render refused a harness the tree does not hold, so (b) failed AC4 at every default
  install. Both now admit it with a `note` line (`TOOL-aOrientedCast-1` R9, `TOOL-aOrientedCast-3`
  S3), so (b) stands: `review-harness` stays optional and its absence is a `note` on all three
  readers.
- **F2 — Does `roles catalogue` ship to adopters, or stay gov's alone?**
  The checker grades the shipped role files against the adopter's own governing doc and the
  adopter's own house overlays, so its subject is the adopter's tree.
  (a) Ship it as a `repo` leg. An overlay an adopter breaks, or a charter that lost a section a role
  needs, reds on the adopter's bar before a handoff refuses at run time.
  (b) Carry it by an `[[exempt_leg]]` row. An adopter learns of a broken overlay only when a handoff
  refuses.
  Recommendation: (a). It is the option that catches the adopter's own defect earliest, and neither
  option widens an install, a surface or a governance carrier.
  RESOLVED (agent, 2026-10-11, delegated): (a), a `[[gate_leg]]` with `subject = "repo"`.
- **F3 — What does the adopter do when no governing doc sits at `CHARTER`?**
  The builder ran a default `plan` and `apply` from `DEPLOY_REGISTRY_DEFAULT` into a scratch target
  where the playbook lands under the target's docs folder as PARALLEL.md, and the memory-tree seed writes
  `CHARTER="AGENTS.md"`, which no file holds. `--scaffold` printed `R0 — CHARTER names AGENTS.md,
  which is not a file` and exited 1, and govkit fails an apply whose adopter exits with no declared
  outcome (`tools/govkit/govkit.py` near line 7750). Every default install without a governing doc
  at `CHARTER` failed, and AC4's nine agent types could not be observed in the shape-6 fixture.
  (1) A declared outcome. The adopter still renders the Skill, skips the agent types and the role
  index, prints one line naming the missing doc and the conf key, and exits 3, which S5 declares as
  an accepted `[[outcome]]`; `check-wiring`'s roles arm reports `UNWIRED roles` naming the same doc.
  (2) Derive `CHARTER` from the playbook's path in the memory-tree seed or in govkit. That changes
  another kit's install behaviour, a public surface M3's veto 2 keeps for the owner, so it is filed
  as a §3 Edge `hands-off` for an ask.
  (3) Declare a governing doc only in the AC3 and AC4 fixtures. Real adopters stay broken.
  Recommendation: (1). It is the only option that makes a real default install succeed without
  moving another kit's surface, and it names the defect where an adopter reads it.
  RESOLVED (agent, 2026-10-11, delegated): (1), exit 3 declared as `no-governing-doc` and an
  `UNWIRED roles` line naming the doc.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · §4 · the M2 cross-read's findings 9 and 11. The header reads `order 7` and the
  Rollout lands this unit at 7, before `PLAY-aOrientedCast-1`, as that spec's §8 F1 resolved. §8 F1
  is re-decided by the catalogue checker's R9: `review-harness` stays optional, and its absence is a
  `note`.
- rev-3 · 2026-10-11 · §2 · §3 · §4 · §6 · §7 · the build passes' finding that the install-prefix ban
  reds at the close on nine keys in the roles kit's checker, library and agent renderer, files earlier
  units of this build created. S14 respells each, AC12 observes the keys gone and each file's own
  checks unmoved, the non-goal on the kit's content admits that respelling, the three files join
  Files touched, and the two roles legs S14 re-observes join §7. This unit owns it because it already
  edits the roles kit to register and wire it.
- rev-4 · 2026-10-11 · §2 · §3 · §4 · §6 · §7 · §8 · the builder's finding that a default install
  with no governing doc at `CHARTER` fails the apply, because the adopter exits 1 and S5 declares
  only code 0. §8 F3 resolves it to option 1: S4's exit table and S5's outcomes gain exit 3 as
  `no-governing-doc`, S8 reports `UNWIRED roles` naming the doc, S10's install arm writes a doc for
  AC4's fixture and takes `charter=False` for AC13, the new criterion, and a §3 Edge files the
  `CHARTER` derivation as an ask. §6's preamble states that AC3, AC4 and AC13 are observed after the
  pass commit, with their ledger lines in a `Pass: none` follow-up.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "an adopter script renders agent definitions, a generated
role index and a skill at install and update, with a check mode a gate leg runs, and the wiring
checker reports an unrendered install"` ranked `render` in `tools/unattended/adopt-unattended.sh`
and `tools/memory-recall/adopt-memory-recall.sh`, `wired` in `tools/check-wiring.sh` and
`resolve_generated_indexes` in `tools/unattended/lib-unattended.sh` as seams. The extended seams are
the adopter `KICK-aOrientedCast-2` creates on the runlog kit's shape (`tools/runlog/adopt-runlog.sh`,
`--scaffold` and `--check` with `render_skill`), `resolve_kit_file` and `check_eol` in
`tools/check-wiring.sh`, `resolve_carrier_kit` and `need` in `tools/check-kit-versions.sh`,
`derive_default_gained` and `derive_unsatisfied_requires` in `tools/govkit/govkit.py`, which the
selftest functions call as the `TOOL-aRoutedQuill-5` arms do, and the `[[generated]]` reader the
unattended kit already runs. No new deployer code is written.

Recall terms used: `default-selection default-gained rendered regenerate GOVKIT_RERENDER adopter
seed project-owned check-wiring requires_if runbook-parity registry` — which surfaced
`TOOL-aRoutedQuill-5` and its F1 and F2, `TOOL-bQuiltedLantern-1` (a kit with a rendered row
declares a `[[regenerate]]`), `TOOL-dRetiredFork-29` and `DEPL-cMendedVintage-5` on the re-render an
update runs.
