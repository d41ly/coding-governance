# PLAY-dOrderedCharter-80 — the second close bar's own product reds, each leg left green by the narrowest fix it demands

**Status:** CLOSED · rev-1 · 2026-11-11 · node a · Tier-2 · base 80a2a55af · streams playbook · order 42 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 |
| [2026-11-11-build-PLAY-dOrderedCharter-80-1-builder-return.md](../build/2026-11-11-build-PLAY-dOrderedCharter-80-1-builder-return.md) | journal | — |
| [2026-11-11-build-PLAY-dOrderedCharter-80-ledger.md](../build/2026-11-11-build-PLAY-dOrderedCharter-80-ledger.md) | journal | — |
| [2026-11-11-prompt-PLAY-dOrderedCharter-80-1-spec-writer.md](../prompts/2026-11-11-prompt-PLAY-dOrderedCharter-80-1-spec-writer.md) | journal | — |
| [2026-11-11-prompt-PLAY-dOrderedCharter-80-build-brief.md](../prompts/2026-11-11-prompt-PLAY-dOrderedCharter-80-build-brief.md) | journal | — |
| [2026-11-11-prompt-PLAY-dOrderedCharter-80-spec-brief.md](../prompts/2026-11-11-prompt-PLAY-dOrderedCharter-80-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's bar over `daf84987f` failed eight legs. The memory hygiene leg is the main loop's, the
policy check's five `review.*` findings are the merge base's, and the main loop cleared the one
record-only carrier at `80a2a55af`. This unit is the rest: every red whose fix writes under `tools/`
or into the runbook, batched as PLAY-dOrderedCharter-77 batched the previous close's, so that each
leg in section 6's table reads green after one pass. It changes no behaviour a leg does not demand.

## 2. Scope (IN)

- **S1** — Install prefix. The shape-5 arm of `tools/govkit/matrix.py` that asserts the template
  landed beside the engine, `tools/govkit/matrix.py@c7baadce:848`, reads the template's destination
  off the `playbook-render` descriptor already in scope: the `[[files]]` row whose `include` holds
  the template's name, its `to` resolved by `govkit.resolve_tokens` against
  `govkit.target_context(g, deploy, "playbook-render", descs["playbook-render"][0])`, the form the
  settings-merge arm at `tools/govkit/matrix.py@c7baadce:330` uses. The `deploy` read at
  `tools/govkit/matrix.py@c7baadce:854` moves above the arm. Observed by AC1.
- **S2** — Dead-path carriers. `tools/dead-path-waivers.txt` gains two rows, one per surface line
  of the `[[retired]]` row `agent-instructions` that names the deleted adopter,
  `tools/govkit/registry.toml@7b1f4bec:206` and `tools/govkit/registry.toml@7b1f4bec:209`. The
  registry is not edited: a landed `[[retired]]` row is frozen and its surfaces are what the step
  gate witnesses a vanished member by. Observed by AC2.
  **Readers:** by name: `tools/govkit/registry.toml`, whose two retired surfaces spell the deleted
  adopter's path, and `tools/dead-path-waivers.txt`, whose two rows S2 adds spell it after the pass;
  `.governance/install.json` spells it too and the lander's `update` rewrites it (section 3)
  · by value: `tools/check-dead-paths.sh`, which matches each row's text against its carrier, and
  `tools/govkit/step_gate.py`, which witnesses the vanished file by the surfaces naming it.
- **S3** — Govkit selfcheck, check 7c. `tools/govkit/govkit.py` gains `derive_root_shipped(descs)`,
  the population of a seventh guard class `root-shipped`: every source a `root_relative` `[[files]]`
  rule ships whose path holds no `/`, read through the existing `rule_sources`. Check 7c appends
  `root-shipped` beside `root-conf` at `tools/govkit/govkit.py@8169d5d9:2416`. Observed by AC3.
- **S4** — Govkit selfcheck, the cross-entry argv. The `micro-format definitions` leg of
  `tools/govkit/entries/check-microformats.kit.toml@20f4ff96:49` keeps two argv elements, `bash` and
  the gate, and the comment block above it says why. `tools/check-microformats.sh` takes no
  argument as reading the template beside the playbook-render kit, found through the inline
  `resolve_python` and `resolve_kit_dir` blocks it gains, byte-identical to their canonicals, with
  `render_playbook.py` the anchor; where the resolver refuses, no python runs, or the kit directory
  holds no template, it reads gov's root template as today. An argument still wins. Its header,
  `tools/check-microformats.test.sh` (one arm) and the runbook's argv sentence at
  `WIRE-INTO-PROJECT.md@1e37ebc8:232` follow. The matrix's argv-resolution arm for the leg needs no
  edit: it resolves the two elements left. Observed by AC4 and AC5.
- **S5** — Kit epoch. `govkit.derive_epoch_state` returns `skip` with
  `skip · no declared version · moved: none` for an entry with no shipped source whose
  `version_from` declares `none`, and `broken` as today for one that declares a file. It never runs
  `git log` with an empty path list. `tools/govkit/selftest.py#check_epoch_verb` gains a fileless
  entry. Observed by AC6.
- **S6** — Runbook parity. `PROBLEM_PIN` in `tools/govkit/check_runbook_parity.py@d2ceb0e5:60`
  moves 18 to 17, its comment gaining a re-measured line. Observed by AC7.
- **S7** — Acceptance matrix, default and aged installs. `tools/govkit/matrix.py` gains
  `render_deploy_tail(kits, fixed)`, the `kits` line, the `[answers]` header and one stub per
  placeholder the playbook entry declares, `- stated` where its default is a bullet and `stated`
  otherwise, with `fixed` over the stubs. Shape 5's derivation at
  `tools/govkit/matrix.py@c7baadce:820` moves into it, and shapes 5, 6 and 7 each call it once.
  Shapes 6 and 7 share their five fixed answers through one constant, `INSTALL_ANSWERS`. Shape 6
  passes the registry's default selection as its `kits`. Observed by AC8.
- **S8** — The render self-test's two cross-os arms. In
  `tools/playbook/render_playbook.py#run_selftest`, each fixture target the gov's-template half
  builds gains a document registry at `iu.derive_kit_rel(iu.DOCUMENTS)`, one row from `build_map_rows` naming `AGENTS.md` at level 0,
  written after `write_template`. The render's `{{INSTRUCTION_MAP}}` reads the target's registry
  (`tools/playbook/render_playbook.py@96eb006f:1743`), and the fixture held none. Observed by AC9.
- **S9** — The render self-test's legacy-placeholder arm. Its current-major marker is
  `f'v{TEMPLATE_MAJOR}.0'` in place of the literal `v4.0`, and its label spells the same value.
  Observed by AC10.
- **S10** — The render self-test's default-route arm moves to the playbook kit's gov-only fixture.
  `tools/playbook/instruction_units.py` gains the plant `drive-default-route`,
  `arm_drive_default_route`, asserting over
  `render_playbook.read_drive_rows(KIT_DIR, ["unattended", "roles"])` what the arm at
  `tools/playbook/render_playbook.py@96eb006f:2749` asserts, under the same label, and that arm and
  its unarmed branch leave `run_selftest` (section 8 F1). Observed by AC11.

## 3. Non-goals (OUT)

- The `policy check` leg's five `review.*` reader findings, which the merge base's dFairHearing owns.
- `.governance/install.json`'s two dead-path carriers, which the lander's `update` rewrites.
- The memory hygiene leg and every record-only offender, the main loop's.
- The owed epoch versions, which the lander mints at the push boundary by design.
- Whether `playbook-render` requires the `unattended` or `roles` kit: section 8 F1 takes an option
  that needs no new requirement.
- The cross-os arm's existing unarmed branch for an install holding no gov template, and the
  shipped render self-test's other arms, which the matrix reads green at HEAD.
- Raising any shrink-only count: S6 lowers its pin, S2 adds rows a deleted name must keep.

This unit rests on CLOSED units it does not declare as edges, as PLAY-dOrderedCharter-77 does,
since a consumes-from edge into a CLOSED spec reds memory hygiene's edge check.
PLAY-dOrderedCharter-31 retired the adopter S2 waives and the seeded template whose entry S5 grades.
PLAY-dOrderedCharter-34 moved the template beside the engine, which S1, S3 and S4 follow.
PLAY-dOrderedCharter-2 raised the template major S9 reads, and PLAY-dOrderedCharter-4 the map S8
plants for. PLAY-dOrderedCharter-23 minted the arm S10 moves.

### Edges

none

## 4. Design

### Evidence

Read at `80a2a55af`. The bar's logs are its run over `daf84987f`, and the commit between touches no
file under `tools/`, so every offender below stands at the base.

- Install prefix: one kit-path spelling on one line, `tools/govkit/matrix.py@c7baadce:848` (PINNED, the
  leg's log over daf84987f).
- Dead paths: five hits. The two `.governance/install.json` lines are out of scope, the
  `.lexicon.conf` line was repointed at `80a2a55af`, and the two registry lines are S2's. The step
  gate witnesses a vanished member by a `[[retired]]` row whose `surfaces` names it, as the module
  docstring of `tools/govkit/step_gate.py` states, and at the bar it read `9 vanished · 9 witnessed`
  (PINNED, its log). The registry's own comment above its `[[retired]]` rows says a landed row is
  frozen.
- Govkit selfcheck: `govkit: 2 problem(s)` (PINNED, its log). The guard
  `tools/gate-legs.json@094abe94:1789` of `playbook render selftest` names the root template, which
  `tools/playbook/kit.toml@9947ba76:61` ships through a `root_relative` include. A probe of the
  descriptors at the base finds that include the only root-level source any `root_relative` rule
  ships, and disjoint from `derive_root_confs`'s five confs (DERIVED, a read of the descriptors).
- Kit epoch: `epoch: playbook · FAILED · no engine/seed/rendered/merged source to measure` (PINNED,
  its log). The playbook entry ships no file since PLAY-dOrderedCharter-31 and declares
  `version_from = { none = … }`. `tools/govkit/govkit.py@8169d5d9:13952` returns `broken` on an
  empty path list before it reads `version_from`, and `cmd_mint` fails on `broken`, so the
  lander's mint fails too. A probe calling `derive_epoch_state` with a fileless desc returns `broken` for both a
  `none` and a `file` declaration at the base.
- Runbook parity: `17 problem(s) · pin 18` (PINNED, its log), the retired `agent-instructions`
  entry having carried no anchored section.
- Matrix, default install: `render-playbook: REFUSED — … declares no kits`. Shape 6 writes no
  `kits` at `tools/govkit/matrix.py@c7baadce:900`. Aged install: `CI_FILE is derived by probe
  ci_file, it returned nothing for this target` (PINNED, the matrix's log). Shape 7 writes five
  fixed answers and no placeholder stub at `tools/govkit/matrix.py@c7baadce:958`.
- Matrix, scratch install: `render_playbook.selftest FAILED — 4 of 199 arm(s)` (PINNED, the
  matrix's log). Reproduced by this writer with a probe of each arm's own lines over gov's engine:
  - The cross-os arms, `tools/playbook/render_playbook.py@96eb006f:2709`, refuse with `the document
    registry … does not read` over gov's tree as well: the template carries `{{INSTRUCTION_MAP}}`,
    which reads the target's registry, and no fixture plants one. With a one-row registry planted,
    gov's template renders both with and without `drop_blocks = ["cross-os"]`.
  - The legacy arm, `tools/playbook/render_playbook.py@96eb006f:2815`, plants `v4.0`, and
    `TEMPLATE_MAJOR` is 5 since PLAY-dOrderedCharter-2
    (`tools/playbook/render_playbook.py@96eb006f:536`).
    A v4.0 template is now a previous major, so `--check` prints the reseed note and exits 0, over
    gov's tree as well; a `v5.0` marker refuses with `legacy v3 placeholder`. The attribution's
    reading, that `--check` read the template beside the engine, does not hold: the log names the
    planted template under the fixture's temporary directory.
  - The default-route arm reads the `unattended` and `roles` descriptors, which the scratch install
    does not hold. Over gov's tree it passes. Its guard `if gov_tpl.is_file()` was written to tell
    gov's tree from an install, and stopped telling them apart when PLAY-dOrderedCharter-34 shipped
    the template beside the engine.
  So three of the four arms red over gov's own tree too (UNVERIFIED by the suite itself, which this
  writer's role may not run; AC9 and AC10 carry the permission line).
- Micro-format gate: the inline blocks S4 adds measure zero sites in every class the shell hygiene
  scan counts, by `sh_hygiene.scan_file` and `scan_spawn_file` over the two blocks as
  `tools/check-template-size.sh` carries them (DERIVED at the base).

### The selfcheck class

```python
def derive_root_shipped(descs: dict) -> set[str]:
    """The `root-shipped` guard class's population. PLAY-dOrderedCharter-80 S3. Every source a
    `root_relative` [[files]] rule ships from the repo root, derived as `derive_root_confs` derives
    the root confs, so a root file no descriptor ships still falls into no class and reds 7c."""
    return {s for d, _p in descs.values() for rule in d.get("files") or []
            if rule.get("root_relative") for s in rule_sources(d, rule) if "/" not in s}
```

### The epoch verdict

```python
vf = desc.get("version_from") or {}
if not paths:
    if "none" in vf:   # a fileless entry declaring no version: nothing to measure, nothing owed
        return "skip", "skip · no declared version · moved: none", "", 0
    return "broken", f"FAILED · no {'/'.join(EPOCH_ROLES)} source to measure", "", 0
if "none" in vf or not vf.get("file"):
    ...   # unchanged: the moved list over a non-empty path list
```

### The micro-format gate's subject

Before `cd "$ROOT"`, with `$1` empty: `_self_dir` takes the no-fork `case "${BASH_SOURCE[0]:-}"`
form of `tools/check-template-size.sh@acbcf7c3:207`; `_py=$(resolve_python "")`, then
`_kd=$(resolve_kit_dir "$_py" playbook render_playbook.py "$_self_dir")`, each with stderr
discarded. `FILE` is `$_kd/coding-governance-agents.template.md` where both succeed and that file
exists, else `coding-governance-agents.template.md` as at `tools/check-microformats.sh@a57b591d:29`.
The resolver runs before the `cd` because its relative `here` reads against the caller's directory.
At gov the probe finds `tools/playbook`, which holds no template, so gov reads its root template;
at an install the receipt row of `render_playbook.py` names the kit and its template is there.

### The moved arm

```python
def arm_drive_default_route(c):
    """PLAY-dOrderedCharter-23, moved by PLAY-dOrderedCharter-80 S10: the shipped unattended and roles
    descriptors render the unattended start line once, the attended /build line directly under it."""
    from render_playbook import Refusal, read_drive_rows, render_drive_line
    try:
        drive, got = [render_drive_line(r) for r in read_drive_rows(KIT_DIR, ["unattended", "roles"])], None
    except Refusal as e:
        drive, got = [], str(e)
    ...   # the two expected lines and the check, as at render_playbook.py's arm
```

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `derive_root_shipped` | `tools/govkit/govkit.py` | `py.function`, `OK` by `--suggest` at design |
| the class `root-shipped` | check 7c of `tools/govkit/govkit.py` | none |
| `render_deploy_tail` | `tools/govkit/matrix.py` | `py.function`, `OK` by `--suggest` at design |
| `INSTALL_ANSWERS` | `tools/govkit/matrix.py` | no cell declares constants |
| `arm_drive_default_route`, the plant `drive-default-route` | `tools/playbook/instruction_units.py` | `py.function`, `OK` by `--suggest` at design; the fixture's `PLANTS` |
| two waiver rows | `tools/dead-path-waivers.txt` | the file's row grammar |

The two waiver rows, tab-separated as the file's header states:

```
{prefix}/govkit/registry.toml<TAB>1<TAB>"file:{prefix}/agent-instructions/adopt-agent-instructions.sh",<TAB><reason>
{prefix}/govkit/registry.toml<TAB>1<TAB>"installable:{prefix}/agent-instructions/adopt-agent-instructions.sh",<TAB><reason>
```

The reason, the same on both: a `[[retired]]` row's surfaces name what the retired entry shipped,
so `update` withdraws the file from an adopter's tree that still holds it and the step gate
witnesses the vanished member; a landed row is frozen. It is the file's migration class.

### Files touched (estimate)

- `tools/govkit/matrix.py` (S1, S7)
- `tools/dead-path-waivers.txt` (S2)
- `tools/govkit/govkit.py` (S3, S5), `tools/govkit/selftest.py` (S5)
- `tools/govkit/entries/check-microformats.kit.toml`, `tools/check-microformats.sh`,
  `tools/check-microformats.test.sh`, `WIRE-INTO-PROJECT.md` (S4)
- `tools/govkit/check_runbook_parity.py` (S6)
- `tools/playbook/render_playbook.py` (S8, S9, S10), `tools/playbook/instruction_units.py` (S10)

### Rollout

Live at landing, order 42, in one pass commit. S4's descriptor row and gate land together, so no
commit declares a leg whose argv the gate cannot read. An adopter's next `update` re-emits the
`micro-format definitions` leg with two argv elements, and its gate reads the same template.

### Alternatives rejected

| Option | Why not |
|---|---|
| Edit the two retired surfaces off the registry | The step gate witnesses a vanished member by them, and a landed `[[retired]]` row is frozen |
| `root-shipped` folded into `derive_root_confs` | One class would then mean two facts, a conf a leg reads and a file a kit ships |
| The micro-format leg keeps its argv and `[adopt] via` | The selfcheck's own hint; it couples the entries' prefixes, where a resolver finds the kit wherever it is homed |
| `playbook-render` ships a copy of the document registry for the cross-os arms | The arm renders a fixture target, whose registry is the input; a one-row fixture is all it reads |
| The legacy arm's marker typed as `v5.0` | Reds again at the next major; `TEMPLATE_MAJOR` is the one value |

## 5. Production-readiness checklist

- security: N/A — no write path, input boundary or grant changes. S4's resolver reads the install
  receipt through the canonical block, which skips a row escaping the tree.
- perf / scale: S4 adds two python spawns to a no-argument run of the micro-format gate; an argument
  spawns none. S10 moves one arm between two suites.
- error / empty / loading states: S4 falls back to gov's root template wherever the kit's template
  is not found, so a target lacking python or the renderer kit exits 2 naming the missing file, as
  today. What S4 does not check: a renderer kit found whose template is absent while gov's root
  holds another reads the root one. What S3 does not check: a root-relative include that is a glob,
  which `rule_sources` excludes. What S5 does not check: whether a `none` entry should declare a
  version; the declaration is taken as written.
- observability: every leg prints its own verdict. S5's skip line names the entry and `moved: none`.
- risks: S7's stubs reach every kit of the default selection, and an install may red on a later
  step once the two named refusals clear; the pass hands that back rather than widening. S10's arm
  runs only on gov's bar, where `instruction units selftest` is an `[[exempt_leg]]`
  (`tools/govkit/registry.toml@7b1f4bec:783`), so a target's install no longer checks the default
  route; no target holds both kits' descriptors without holding gov's tree's intent for them.
- testing: AC1 to AC11, each a direct command, a probe or a grep; the suite arms are the `New arm:`
  lines in section 7.
- migration: in-place edits and two additive rows. An adopter's emitted `micro-format definitions`
  leg loses one argv element at its next `update`; its verdict is unchanged.
- user docs: `WIRE-INTO-PROJECT.md`'s micro-format section states the two-element argv and where the
  gate finds the template (S4). No `help/` page names the gate's argv.

## 6. Acceptance criteria

Each leg the bar failed, and the criterion that shows it green:

| Leg | Criteria |
|---|---|
| `install-prefix (shipped surface)` | AC1 |
| `dead-path carriers (deleted files still named)` | AC2 |
| `govkit selfcheck` | AC3, AC4 |
| `micro-format definitions` | AC5 |
| `kit epoch (shipped bytes move, the version moves)` | AC6 |
| `govkit runbook parity` | AC7 |
| `govkit acceptance matrix` | AC8, with AC9, AC10 and AC11 |

A criterion that runs a leg's own checker or a suite is the main loop's at the close wherever the
builder's role may not run it.

- **AC1** — When `bash tools/check-install-prefix.sh` runs after the pass, it exits 0 and its
  summary opens `install-prefix: clean —`; and `git grep -n "PFX / \"playbook\"" -- tools/govkit/matrix.py`
  prints nothing.
  Red when: the shape-5 arm still spells the playbook kit's directory.
  figure: PINNED, one spelling on one line in the bar's log over daf84987f.
- **AC2** — When `bash tools/check-dead-paths.sh` runs after the pass, it prints no hit line
  naming `tools/govkit/registry.toml` and no stale waiver; its only hits are the two
  `.governance/install.json` lines this unit leaves to the lander. And
  `git grep -c "adopt-agent-instructions.sh" -- tools/dead-path-waivers.txt` counts 2.
  Red when: a registry carrier stays unwaived, or a row's text misses its carrier and reads stale.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs after the pass, it prints no line
  holding `guard pathspec`; and
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import govkit as g; print(sorted(g.derive_root_shipped({'k': ({'files': [{'include': ['A.md'], 'root_relative': True}, {'include': ['C.md']}]}, None)})))"`
  prints `['A.md']`.
  Red when: the root template's guard falls into no class, or the class admits a source no
  `root_relative` rule ships.
- **AC4** — When `python tools/govkit/govkit.py selfcheck` runs after the pass, it exits 0, prints
  no line holding `govkit: entry 'check-microformats'`, and its `govkit: cross-entry argv:` line
  ends `0 naming a file only another entry ships`.
  Red when: the leg's argv still names a file another entry ships.
- **AC5** — When `bash tools/check-microformats.sh` runs over the tree with no argument after the
  pass, it prints `microformats OK —`; and in a scratch git repository holding a copy of the gate
  beside a `playbook` directory with an empty `render_playbook.py` and a conforming template, and a
  fence-less template at its root, the copy run with no argument exits 0, then exits 2 printing
  `not delimited by exactly one fence pair` once the kit's template is taken away.
  Red when: a no-argument run reads gov's root path where the kit's template is installed, or reads
  nothing where it is not.
  fixture: built by the command; S4's suite arm builds the same tree.
- **AC6** — When `python tools/govkit/govkit.py epoch` runs after the pass, it prints
  `epoch: playbook · skip · no declared version · moved: none` and no line holding `FAILED`; and
  `python -c "import sys, pathlib; sys.path.insert(0, 'tools/govkit'); import govkit as g; r = pathlib.Path('.').resolve(); print(g.derive_epoch_state(r, 'fx', {'version_from': {'none': 'x'}}, 'HEAD~1')[0], g.derive_epoch_state(r, 'fx', {'version_from': {'file': 'a.py', 'pattern': '^V'}}, 'HEAD~1')[0])"`
  prints `skip broken`, where the base prints `broken broken`.
  Red when: a fileless entry declaring no version reads broken, or one declaring a file stops
  reading broken.
- **AC7** — When `python tools/govkit/check_runbook_parity.py` runs after the pass, it exits 0
  printing `17 problem(s) · pin 17`.
  Red when: the pin stays above the count.
  figure: PINNED, 17 problems in the bar's log over daf84987f.
- **AC8** — When `python tools/govkit/matrix.py` runs after the pass, it prints `ok` for
  `default install: apply completes` and for `aged install: apply from the aged vintage completes`;
  and `git grep -c "render_deploy_tail(" -- tools/govkit/matrix.py` counts 4.
  Red when: a shape writes its deploy file without the stubs, or shape 6 without `kits`.
  cost: one matrix run; its evidenced maximum is 218.8 s on node a (PINNED, `tools/run-gates/ceiling-evidence.txt`).
  permission: the main loop runs it at the close, since a role agent's scratch guard refuses a
  scratch install (PLAY-dOrderedCharter-72 AC6).
- **AC9** — When `python tools/playbook/render_playbook.py --selftest` runs over the tree after the
  pass, it prints `render_playbook.selftest OK` and no `arm FAIL` line holding `drop_blocks cross-os`.
  Red when: a cross-os fixture target holds no document registry and the map refuses.
  permission: the main loop runs it; a role agent's scratch guard refuses a suite.
- **AC10** — When `python tools/playbook/render_playbook.py --selftest` runs over the tree after the
  pass, it prints no `arm FAIL` line holding `legacy placeholder`; and
  `git grep -n "'v4.0', 'legacy" -- tools/playbook/render_playbook.py` prints nothing.
  Red when: the arm plants a marker below the engine's major and reads the reseed note as a pass's
  opposite.
  permission: the main loop runs it, as AC9.
- **AC11** — When `python tools/playbook/instruction_units.py fixture --plant drive-default-route`
  runs after the pass, it exits 0 printing a line holding
  `ok · the unattended start line renders once, with the attended /build line directly under it`;
  `git grep -c "the unattended start line renders once" -- tools/playbook/render_playbook.py` counts
  0; and in AC8's run the matrix prints `ok` for
  `scratch install: leg 'playbook render selftest' prints its stated verdict where it was installed`
  and closes `govkit-matrix: all arms held`.
  Red when: the shipped self-test still reads a kit the install lacks, or the moved arm stops
  asserting the two lines.

## 7. Gates

`install-prefix (shipped surface)` · `dead-path carriers (deleted files still named)` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `govkit runbook parity` · `govkit acceptance matrix` · `micro-format definitions` · `micro-format gate selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `shell hygiene (a fork spent on builtin work)` · `harness arms (fail branches armed or pinned)` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `playbook render selftest` · `instruction units selftest` · `policy fixtures` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

The guarded legs on the line are those the files touched trip: the govkit legs and `recall floor
arms` for `tools/govkit/`, `micro-format gate selftest` and the matrix for the gate, `playbook
render selftest` for the playbook, and `policy fixtures` for the govkit, entries and playbook files.
The resolver's parity leg grades S4's two inline copies.

New arm: tools/check-microformats.test.sh · covers AC5 · a gate copy beside a `playbook` dir holding `render_playbook.py` and a conforming template, with a fence-less root template, read with no argument: exit 0, then exit 2 once the kit's template is gone; red before S4 because the copy reads the root template · none
New arm: tools/govkit/selftest.py · covers AC6 · `check_epoch_verb`'s fixture registry gains a fileless entry declaring `version_from = { none = … }`, whose epoch line must read `skip · no declared version · moved: none`; red before S5, which prints it FAILED · none
New arm: tools/playbook/render_playbook.py · covers AC9 AC10 · the cross-os arms' targets gain a one-row registry and the legacy arm plants the engine's own major; both red at the base over gov's tree · none
New arm: tools/playbook/instruction_units.py · covers AC11 · the plant `drive-default-route`, moved from the render self-test; its failing case is a scratch clone whose `tools/roles/kit.toml` lacks the `/build` start row, which the plant must red; red before S10 because no plant of that name exists · none

## 8. Open questions

- **F1 — Where the default-route arm runs, now that an install can lack the kits it reads.** The
  arm asserts that the shipped `unattended` and `roles` descriptors render the unattended start line
  with the `/build` line under it. A scratch install of `playbook-render` holds neither descriptor.
  Options: (a) the arm builds its own fixture registry and descriptors, typing the two rows in the
  arm; (b) `playbook-render` ships or requires both kits' descriptors; (c) the arm moves to the
  playbook kit's gov-only fixture, `instruction_units.py fixture`, whose leg is an `[[exempt_leg]]`
  because its plants reach kits a target may not hold, and where a kit not found reds the case.
  (a) mirrors the subject: dropping a row from either descriptor would no longer red it. (b) adds an
  install requirement for one self-test arm, the option PLAY-dOrderedCharter-73 parked for the owner.
  (c) keeps the arm's subject and its failing case, and its home's registry row already states the
  rule. RESOLVED (agent, 2026-11-11, delegated): (c), the owner's 2026-11-10 order to take the forks'
  recommendations, and the registry's own seam. widens: none · relaxes: the shipped render
  self-test, which no longer checks the default route at an install

## 9. Revision log

- rev-1 · 2026-11-11 · initial draft, from `2026-11-11-prompt-PLAY-dOrderedCharter-80-spec-brief.md`,
  every offender re-read at `80a2a55af` against the bar's logs over `daf84987f`. The four render
  self-test arms were probed over gov's engine: three red there too, and the legacy arm's cause is
  the template major, not the template it reads.
- rev-1 · 2026-11-11 · S2 · its item gains the **Readers:** clause memory hygiene's check 25 asks of
  an item naming a retired entry's surfaces; no design text moved, and the rev stays.

## 10. Reuse audit

Every fix extends a seam the tree holds. Run at `80a2a55af`,
`python tools/codebase-map/reuse_lookup.py "a flat gate finds the charter template beside the renderer kit in this install"`
ranked `resolve_kit_dir` first, a SEAM at fan-in 58 and 107 installs, then `derive_kit_prefix`,
`derive_kit_file`, `derive_kit_rel` and `derive_template_rel`: S4 carries the inline
`resolve_kit_dir` block as `tools/check-template-size.sh@acbcf7c3:259` does, and S8 plants through
`derive_kit_rel` as `check_map_arms` does. S3 extends `derive_root_confs`'s pattern and reads
through `rule_sources`; S5 edits `derive_epoch_state`, the one function `epoch` and `mint` share;
S7 extracts shape 5's stub derivation at its third use; S10 joins the drive plants of
`instruction_units.py`'s `PLANTS`, beside `arm_drive_bad_role`; S2 extends the waiver file's
migration class. No new mechanism is minted. The recall query returned PLAY-dOrderedCharter-77's
section 10, whose F2 moved three legs to gov-only rows by the same rule F1 applies, and
PLAY-dOrderedCharter-34's reuse audit, which shipped the template beside the engine through
`root_relative` rules.

Recall terms used: `python tools/memory-recall/query.py "how does a shipped gate find a file another kit lands, and how does a selftest arm read gov-only descriptors" --terms "resolve_kit_dir root_relative template beside engine selftest arm gov-only exempt_leg scratch install document registry drive rows"`
