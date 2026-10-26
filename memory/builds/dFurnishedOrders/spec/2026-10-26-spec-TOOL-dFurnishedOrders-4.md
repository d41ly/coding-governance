# TOOL-dFurnishedOrders-4 — the work order's optional slots in three states, and bug classes as a core field the spec names

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 4 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0195@d3ad9dda whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |

<!-- /gen:spec-records -->

## 1. Goal

Bug classes selected by the files a change touches miss at the moment of the mistake: the edited file
selects the confirmed class 18% of the time, and 1,127 checklist runs led to 45 reads of a class
(gap-mem-44, the owner's NT-24). This unit gives the work order one renderer for a field an optional
component fills, in its three states, renders the bug classes the unit's spec names as a core field of
that order, and retires every build-side selection by a write set's paths: the per-pass checklist, the
default-off `prebuild`, and the lookups in the build method's and the unattended Skill's text, with
their readers inventoried by value and an upgrade step for each.

## 2. Scope (IN)

- **S1** — The slot renderer (shared interface J4). `render_slot(point, state, body)` in
  `tools/roles/roles_lib.py` returns one block: `### <point>`, then the state line of
  PLAY-dOrderedCharter-17 S9's grammar, `slot <point> · <state>`, then, for `filled`, a blank line and
  `body`. `point` is one of `ORDER_SLOTS = ("memory", "code-notes", "legacy", "house-index", "map",
  "code", "problems", "bug-classes", "instructions")`, J4's eight heads and `instructions`, the
  feature-selected instruction block TOOL-dFurnishedOrders-18 S2 renders (its §8 F3); `state` is one of `SLOT_STATES = ("filled", "searched-empty",
  "not-installed")`, and `not-installed` renders `slot <point> · not-installed: <body>`, `body` being
  the fallback. An unknown point or state, or `filled` with an empty body, raises `RolesError` naming
  both. A slot block always carries its state line, so TOOL-dBoundRoles-23's rule for a frame slot with
  no block never applies to it. Observed by AC1.
- **S2** — The bug classes as a spec field (shared interface J5): `### Bug classes` joins the spec
  format's recurring §4 sub-heads (`tools/memory-tree/SPEC-TEMPLATE.template.md:151-154`, rendered to
  `memory/TEMPLATE-SPEC.md`), one bullet per class, `` - `<name>` — <why this unit can hit it> ``,
  `<name>` the `name` front-matter key of a `memory/gotchas/*.md` record of `kind: class`, chosen from
  the catalogue's one-line index `memory/gotchas/INDEX.md`. Observed by AC8.
- **S3** — The named lookup. `gotchas.py --for-names <name>...` (`tools/memory-tree/gotchas.py`, its
  dispatch at `:1366-1381`) prints the checklist for exactly the named class records, each
  `- [ ] <name> (named)` with its description and path, after every universal record as `--for-diff`
  prints them (`:738-739`), under a header naming the counts. A name with no record, or naming a record
  whose `kind` is not `class`, is one `HYGIENE gotchas: --for-names: <name>: <why>` line at exit 1,
  the refusal shape `--for-diff` uses for a bad range. `cmd_for_names(root, conf, names)` reads
  `records` (`:289`) and selects by name, never by anchor. Observed by AC2.
- **S4** — The core field rendered. `render_handoff` (`tools/roles/handoff.py:312`) renders
  `render_slot("bug-classes", ...)` on every order rendered for a unit, in TOOL-dBoundRoles-23's
  `boundaries` frame slot: `read_bug_class_names(spec_text)` in `roles_lib.py` takes the names from the
  `### Bug classes` sub-head of the spec the order's `input:spec` hands, and the memory-tree kit's
  `gotchas.py --for-names`, run as a subprocess found by `resolve_kit_dir("memory-tree", "gotchas.py",
  KIT_DIR)`, fills it. The states: `filled` with that stdout; `searched-empty` when the spec names no
  class or the order hands no spec; `not-installed: no memory-tree kit; read the spec's ### Bug
  classes` when the kit is absent. An exit 1 from the lookup refuses the render, naming the spec and
  the lookup's line. Observed by AC3 and AC4.
- **S5** — The build-side selections retired, per §4 "### What retires and what stays". The unit
  harness `tools/workflows/unattended-unit.js` loses its required `checklist` key and its post-commit
  instruction (`:105`, `:322`), and its optional `prebuild` key, validation, paragraph and log
  (`:43-49`, `:135-143`, `:273-281`, `:325`); its prompt tells the builder to act on its work order's
  `### bug-classes` block, the spec's named classes, before it returns; and a caller passing either
  retired key is refused before any spawn, naming the key and the upgrade step of S6. The build harness
  `tools/workflows/unattended-build.template.js` loses `CHECKLIST` (`:562-565`) and the hand-out's
  `checklist: CHECKLIST` (`:2485`). Observed by AC5 and AC6.
  **Readers:** by name: `tools/workflows/unattended-unit.js` (`:43-49`, `:105`, `:135-143`,
  `:273-281`, `:322`, `:325`), `tools/workflows/unattended-build.template.js` and its render
  `unattended-build.js` (`:562-565`, `:605-607`, `:1286`, `:1619`, `:2485`),
  `tools/workflows/unattended-build.test.sh` (the `prebuild` arms at `:1115-1134` and the hand-out's
  `checklist` arms), `tools/workflows/README.md` (`:40`), `tools/govkit/selftest.py:14562-14566`,
  whose fixture harness spells its own `CHECKLIST` line and reads no real harness, kept ·
  by value: `SPEC_COMMIT_CHECKLIST` (`:605-607`), which falls back to `CHECKLIST`'s value and is
  re-pointed by §8 F1; the two compares at `:1286` and `:1619`, which test that fallback by equality
  and are re-pointed to test `auditBase`; and every caller that passes the hand-out's `args` to
  `unattended-unit.js`, which S5's refusal names.
- **S6** — The build method and the Skill's text: BUILD-METHOD M6's per-pass checklist paragraph and
  its command (`tools/memory-tree/BUILD-METHOD.template.md:185-193`) give way to one sentence, M8's
  "the M6 checklist" (`:253`) names its command, `gotchas.py --for-diff <BASE>..HEAD`, and M5's path-set
  context (`:164-169`) keeps the bug-class lookup for kickoff's entrypoints alone, a spec naming its
  own classes under `### Bug classes`; the unattended Skill's command line
  (`tools/unattended/SKILL.template.md:121`) and the verbs file's bullet
  (`tools/unattended/VERBS.template.md:764-769`) go; `tools/roles/agents/gov-builder.agent.md:42-43`
  reads "every bug class the spec names was checked against your change". Each render follows its
  source. Observed by AC7 and AC10.
  **Readers:** by name: the renders `memory/guides/BUILD-METHOD.md`, `.claude/skills/unattended/SKILL.md`,
  `memory/guides/UNATTENDED-VERBS.md` and `.claude/agents/gov-builder.md`; the memory-tree kit's
  `[[contract]]` for `memory-tree/gotchas` (`tools/memory-tree/kit.toml:433-439`), whose `consumer`
  drops `unattended:SKILL.template.md`; `tools/unattended/README.md:51-56`,
  `tools/unattended/kit.toml:57-61` and `tools/unattended/adopt-unattended.sh:215-222` and `:575-579`,
  whose prose says the Skill names the checklist and is re-worded, `MEMORY_TREE_DIR` kept because
  `SKILL.template.md:67` and the conf stamp (`adopt-unattended.sh:596-622`) still read it ·
  by value: the `build-method size` and `unattended skill size` legs, which measure the shrunk files;
  the `kit/dogfood doc parity` leg, which compares each render with its source.
- **S7** — The upgrade steps (shared interface J21): two `[[upgrade]]` rows in TOOL-dSafePassage-1 S1's
  grammar, `unattended/retire-pass-checklist` in `tools/unattended/kit.toml` and
  `review-harness/retire-prebuild` in `tools/workflows/kit.toml` (§8 F5), each running
  `tools/govkit/steps/retired_dispatch_args.py` with `up`, `down` or `witness`, the target and the
  retired key, per §4 "### The upgrade steps". Observed by AC9.
  **Readers:** the retired keys' own readers are S5's. by name: READER NOT IN TREE — the two step
  rows are read by TOOL-dSafePassage-1's `upgrade_steps.py`, absent at base ·
  by value: NO VALUE READERS — the rows' values reach only that reader and the update walk it drives.
- **S8** — The kits' text: `tools/memory-tree/README.md`'s `gotchas.py` row names `--for-names`;
  `tools/roles/README.md` names `render_slot` and the `### bug-classes` block; `help/roles.md`'s "How a
  task reaches an agent" says a builder's order carries the classes its spec names. Observed by AC11.

## 3. Non-goals (OUT)

- The review side, which keeps selecting by range (NT-25): the spec audit's `AUDIT_CHECKLIST` over
  Files touched, `tier2-review`'s checklist and by-design block, M8's closing checklist,
  `MERGE-BAR.md:95`, and kickoff's `--for-paths` over entrypoints. The charter line "run it before any
  review" (`coding-governance-agents.template.md:118`) is TOOL-dFairHearing-15 S4's to retire.
- Which classes a spec names. The writer names them from the index; dIndexedDesign's reuse scout
  naming at most five (NT-26) is that build's arm.
- Any slot but `bug-classes`: units 11, 12, 17, 18 and 20 render theirs through S1's renderer.
- The legacy slot's fourth state `not-seeded`: TOOL-dFurnishedOrders-11 adds it to `SLOT_STATES`.
- Moving a syntactic class to a gate (night-pass-two point 6 item 3): dLinkedLibrary's.

### Edges

- **hands-off** `TOOL-dFurnishedOrders-11` — `render_slot`, through which the memory, code-notes, legacy and house-index slots render, with `not-seeded` added to its states
- **hands-off** `TOOL-dFurnishedOrders-12` — `render_slot`, through which the `map` slot renders
- **hands-off** `TOOL-dFurnishedOrders-17` — `render_slot`, through which the `code` slot renders
- **hands-off** `TOOL-dFurnishedOrders-20` — `render_slot`, through which the `problems` slot renders
- **hands-off** `TOOL-dFurnishedOrders-18` — `render_slot`, through which the code-notes slot's delivery and the `instructions` slot render
- **consumes-from** `TOOL-dFurnishedOrders-8` — `doc.build-method#m6-passes-commits-parallelism`, the slice `gov-builder` carries, so S6's edit to M6 re-renders that role's file
- **consumes-from** external — TOOL-dBoundRoles-3's work order and TOOL-dBoundRoles-23's `boundaries` frame slot, PLAY-dOrderedCharter-17 S9's slot grammar and TOOL-dSafePassage-1's `[[upgrade]]` rows and `upgrade_steps.py`, each specced and unbuilt at base

## 4. Design

### The rendered field

A builder's order for a unit whose spec names two classes:

```
### bug-classes

slot bug-classes · filled

# recurring-bug-class checklist for 2 named class(es) + 6 universal
...
- [ ] fold-text-is-unreviewed-surface (named)
      a review round's fixes are folded into fresh prose nobody has reviewed, ...
      memory/gotchas/fold-text-is-unreviewed-surface.md
```

and for one whose spec names none, `### bug-classes` then `slot bug-classes · searched-empty`. The
universals ride the field because no write set selects them: they are printed on every checklist
today (§8 F2).

### What retires and what stays

| Reader | Selects by | Fate |
|---|---|---|
| per-pass checklist: M6, Skill `:121`, verbs `:764-769`, `unattended-unit.js` `checklist`, `CHECKLIST` | the pass's diff | retired (S5, S6) |
| `prebuild` (`unattended-unit.js`, TOOL-aMendedFleet-74) | the unit's write set | retired (S5) |
| M5's lookup over "a spec's Files touched" | the spec's write set | retired (S6) |
| `gov-builder.agent.md:42-43` | the M6 checklist | re-worded (S6) |
| `SPEC_COMMIT_CHECKLIST` | the spec commit's paths, read by the audit | kept, fallback re-pointed (§8 F1) |
| `AUDIT_CHECKLIST` (`unattended-build.template.js:588`, `:1374-1460`) | Files touched, for the audit | kept, review (NT-25) |
| `tier2-review`'s checklist (`tier2-review.template.js:519-597`, `:923`) | the pinned range | kept, review |
| M8, `MERGE-BAR.md:95`, `HYGIENE.md:778-806`, `memory/gotchas/INDEX.md:9-10` | the reviewed range | kept, review |
| kickoff (`SESSION-KICKOFF.md:100`, `:113`, `:149`; `card:classes` in `roles_lib.READ_KEYS`) | entrypoints | kept, orientation |
| `memory-tree/kit.toml:437`'s contract probe | the script's own path | kept, an install witness |
| the charter line (`coding-governance-agents.template.md:118`) | a range | TOOL-dFairHearing-15 S4's |
| `unattended.sh:8262` | none | kept, a historical comment |

### The upgrade steps

```toml
# tools/unattended/kit.toml
[[upgrade]]
id = "unattended/retire-pass-checklist"
up = ["python", "{gov}/govkit/steps/retired_dispatch_args.py", "up", "{target}", "checklist"]
down = ["python", "{gov}/govkit/steps/retired_dispatch_args.py", "down", "{target}", "checklist"]
witness = ["python", "{gov}/govkit/steps/retired_dispatch_args.py", "witness", "{target}", "checklist"]
surfaces = ["workflow-arg:unattended-unit.js#checklist", "command:gotchas.py --for-diff HEAD~1..HEAD"]
needs-target = false
```

`review-harness/retire-prebuild` in `tools/workflows/kit.toml` is the same with `prebuild` and the
surface `workflow-arg:unattended-unit.js#prebuild`. The kits' own rendered files move with `update`'s
render; what an update cannot move is the adopter's own code. So `witness` exits 0 when no tracked file
of the target outside its installed kit files passes the retired key to `unattended-unit.js` or, for
`checklist`, spells the per-pass command; `up` runs the same scan, writes nothing, and exits 1 listing
each hit and its remedy, so the walk stops with the adopter's work named; `down` writes nothing and
exits 0.

### Inventory

Minted: `render_slot`, `ORDER_SLOTS`, `SLOT_STATES`, `read_bug_class_names`, `cmd_for_names`, the
`--for-names` mode, the `### Bug classes` sub-head and `### bug-classes` block, the two step ids and
`retired_dispatch_args.py`. `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
answered OK for `render_slot` and `read_bug_class_names`; the pass asks it of `cmd_for_names`.

### Migration

Specs landed before this unit carry no `### Bug classes`, so their orders render `searched-empty`,
which is true. A caller still passing `checklist` or `prebuild` is refused by name, and the upgrade
step names it at update. The rendered guides and Skill change through the kits' renders.

### Rollout

Live at landing. M6's edit changes the slice `gov-builder` carries (TOOL-dFurnishedOrders-8), so the
pass re-renders the agent files with `render_agents.py --write`.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/README.md`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/agents/gov-builder.agent.md`
- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/README.md`
- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js` (its render)
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/kit.toml`
- `tools/workflows/README.md`
- `tools/unattended/SKILL.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/kit.toml`
- `tools/unattended/README.md`
- `tools/unattended/adopt-unattended.sh`
- `tools/govkit/steps/retired_dispatch_args.py`
- `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`, `memory/guides/UNATTENDED-VERBS.md`,
  `.claude/skills/unattended/SKILL.md` (renders)
- `.claude/agents/` (renders, by `render_agents.py --write`)
- `help/roles.md`

### Alternatives rejected

- **Keep `prebuild`, default off, beside the field.** A dark switch for a selection the owner retired
  (NT-24) is scaffolding the charter's YAGNI rule deletes.
- **Serve classes from a hook on the edited path.** Measured and rejected by night-pass-two point 6
  item 2: it inherits the 18%.
- **The slot line typed at each site.** Six units render slots; one renderer is one spelling, the
  grammar PLAY-dOrderedCharter-17 S9 fixed.

## 5. Production-readiness checklist

- security — no new write path in the repository; the step program reads the target and writes
  nothing; the lookup runs a tracked script with argv.
- perf / scale — one `--for-names` subprocess per order rendered for a unit, in place of a per-pass
  `--for-diff`.
- error / empty / loading states — `searched-empty` and `not-installed` say why; an unknown class
  refuses the render; a retired key refuses the dispatch.
- observability — each state line names its slot; each refusal names the key, the class or the spec.
- risks — a spec that names no class hands its builder none; that is the owner's NT-24 trade, and
  review keeps its range checklist.
- testing — AC1 to AC11 by a pass over scratch fixtures and `node -e` stubs; the arms of §7 at the close.
- migration — as §4 says.
- user docs — `help/roles.md`, by S8.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.render_slot("map", "not-installed", "no renderer")` it
  returns `### map` then `slot map · not-installed: no renderer`; `render_slot("bug-classes", "filled",
  "x")` returns the state line, a blank line and `x`; and `render_slot("maps", "filled", "x")` and
  `render_slot("map", "empty", "")` each raise `RolesError` naming the value.
  Red when: an unknown point renders, so a sibling's typo is a silent new slot.
- **AC2** — When `python tools/memory-tree/gotchas.py --for-names fold-text-is-unreviewed-surface`
  runs over gov, it prints `- [ ] fold-text-is-unreviewed-surface (named)` and every `universal: true`
  record, and no other class; `--for-names no-such-class` exits 1 with a `HYGIENE gotchas:` line
  naming it.
  Red when: the mode falls back to anchors, or an unknown name prints an empty checklist at exit 0.
- **AC3** — When `python handoff.py render --role gov-builder` runs in a scratch adopter with an
  `input:spec` whose `### Bug classes` names one class, the task's `boundaries` part holds
  `### bug-classes`, `slot bug-classes · filled` and that class's item; with a spec carrying no such
  sub-head it holds `slot bug-classes · searched-empty`; with the memory-tree kit removed it holds
  `slot bug-classes · not-installed:`.
  Red when: an order for a unit renders no `### bug-classes` block at all.
  fixture: a scratch clone with the roles and memory-tree kits installed and a fixture build.
- **AC4** — When the AC3 spec names `no-such-class`, the render exits 1, its stderr names the spec
  and `no-such-class`, and it writes no file.
  Red when: an unknown class renders as `searched-empty`.
- **AC5** — When `grep -c "prebuild"` runs over `tools/workflows/unattended-unit.js` it prints 0, and
  a `node -e` fixture running the script over a stub `agent` with `args` carrying `checklist` throws
  before any spawn, naming `checklist` and the unattended kit's retire-pass-checklist step; without it, the
  builder's prompt names `### bug-classes`.
  Red when: a retired key is ignored, so a caller believes a checklist still runs.
- **AC6** — When `grep -n "^const CHECKLIST\|checklist: CHECKLIST"` runs over
  `tools/workflows/unattended-build.template.js` it prints nothing, and `grep -n "SPEC_COMMIT_CHECKLIST ="
  -A2` there shows its no-base branch as a `--for-diff HEAD~1..HEAD` literal.
  Red when: the spec commit's checklist loses its fallback and the audit-off hand-out carries none.
- **AC7** — When `grep -c "for-diff HEAD~1..HEAD"` runs over `memory/guides/BUILD-METHOD.md`,
  `.claude/skills/unattended/SKILL.md` and `memory/guides/UNATTENDED-VERBS.md`, each prints 0;
  `grep -c "for-diff <BASE>..HEAD"` over `memory/guides/BUILD-METHOD.md` prints at least 1; and
  `wc -c` of it is at most 30720.
  Red when: M8 still points at the retired M6 checklist, or a render keeps the per-pass line.
- **AC8** — When `grep -n "### Bug classes"` runs over `memory/TEMPLATE-SPEC.md` and over its kit
  template, each prints the recurring sub-head line.
  Red when: the template and its render disagree.
- **AC9** — When `python upgrade_steps.py list` runs in TOOL-dSafePassage-1's govkit directory, it
  names both step ids; and when `retired_dispatch_args.py witness` runs over a scratch target whose
  own script passes `"prebuild"` to `unattended-unit.js`, it exits 1 naming that file, and exits 0 once the key is removed.
  Red when: the witness passes a target that still hands a retired key.
  fixture: TOOL-dSafePassage-1's reader, absent at base.
- **AC10** — When `grep -c "checklist M6"` runs over `tools/roles/agents/gov-builder.agent.md` and
  its render it prints 0, and `grep -n "unattended:SKILL.template.md" tools/memory-tree/kit.toml`
  prints no `consumer` line of the gotchas contract.
  Red when: a contract still names a consumer that no longer runs the lookup.
- **AC11** — When `grep -n "for-names"` runs over `tools/memory-tree/README.md`, and
  `grep -n "bug-classes"` over `tools/roles/README.md` and `help/roles.md`, each prints a line.
  Red when: the docs still say the build hands the per-pass checklist.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `policy fixtures` · `gotchas selftest` · `kit/dogfood doc parity` · `build-method size` · `unattended skill size` · `unattended kit gate` · `unattended skill wiring` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py · covers AC2 · `--selftest` gains a named hit, a universal, an unnamed anchored miss and an unknown name, staged by selecting by anchor · none
New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC3 AC4 · a fixture spec naming one class, none, and an unknown one, staged by rendering no block for a spec without the sub-head · none
New arm: tools/workflows/unattended-build.test.sh · covers AC5 AC6 · the `prebuild` arms at `:1115-1134` replaced by a dispatch passing each retired key, staged by ignoring the key · none

## 8. Open questions

- **F1 — What does `SPEC_COMMIT_CHECKLIST` fall back to once `CHECKLIST` is gone (D3)?** Options:
  (a) its own `--for-diff HEAD~1..HEAD` literal, the spec commit's checklist kept as the audit's
  review-side input; (b) `AUDIT_CHECKLIST` over the spec commit's paths with no base, read from the
  working tree; (c) no spec-commit checklist without an audit base. The spec commit's diff holds the
  specs, never a unit's write set, and its checklist joins the audit (`:1610-1622`) or the audit-off
  hand-out (`:2460`), both review. (b) moves the by-design block's read from the parent to the working
  tree; (c) drops a review input. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the only
  option keeping every review input as it stands. widens: none · relaxes: none
- **F2 — Do the universal classes ride the core field (D3)?** Options: (a) yes, printed first as
  `--for-diff` prints them; (b) only the named classes; (c) only when a spec names them. A universal is
  selected by no write set, so the retirement does not reach it. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the most feature-rich survivor. widens: none · relaxes: none
- **F3 — Which frame slot carries `### bug-classes`?** Options: (a) `boundaries`, beside `### allowance`
  and the charter blocks; (b) `material`, beside the inputs. A class is a constraint on the change, not
  an input to it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, tie-broken by TOOL-dBoundRoles-23
  §4's slot meanings. widens: none · relaxes: none
- **F4 — Is a retired dispatch key refused or ignored?** Options: (a) refused before any spawn, naming
  the key and the step; (b) ignored. (b) lets a caller believe a checklist runs, the failure the
  charter's deny-by-default rule closes. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens:
  none · relaxes: none
- **FACT-QUESTION · F5 — Is `workflows/retire-prebuild` (the brief's J21) a legal step id?** Probe:
  `grep -n '^id = ' tools/workflows/kit.toml`. Observation: the descriptor's id is `review-harness`,
  and TOOL-dSafePassage-1 §4 "Data model" requires `<entry>` to equal it; the liveness assertion is that
  the same probe over `tools/unattended/kit.toml` prints `unattended`, which matches. RESOLVED (agent,
  2026-10-26, delegated): `review-harness/retire-prebuild`, rung 2. widens: none · relaxes: none
- **F6 — Does "every call of the lookup by a write set's paths" reach the review side (D3)?** Options:
  (a) build side only: M5's spec-writer lookup, the per-pass checklist and `prebuild` retire, the
  audit's Files-touched lookup and every range checklist stay; (b) every `--for-paths` caller.
  Night-pass-two point 6 items 1 and 4 (`night-pass-two.md:473-492`) retire writing-time serving and keep
  classes on review (NT-25). RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2's own source for
  the clause. widens: none · relaxes: none
- **F7 — May this unit edit the build method, the unattended Skill, the verbs file and the spec
  format?** The clause names the build method's and the unattended Skill's text, "among them", and
  the field it adds lives in the spec format. RESOLVED (agent, 2026-10-26, delegated): yes, rung 3
  with veto 2 lifted by the grant. grants: PLAY-dClosedLoop-3 BUILD-METHOD M5, M6 and M8, the
  unattended Skill and verbs file, and TEMPLATE-SPEC's recurring sub-heads. widens: none · relaxes: none
- **F8 — The parents this unit calls are specced and unbuilt at base `2193e25d`.** TOOL-dBoundRoles-3's
  work order, TOOL-dBoundRoles-23's frame, PLAY-dOrderedCharter-17 S9's grammar and TOOL-dSafePassage-1's
  rows and reader do not exist in the tree. RESOLVED (agent, 2026-10-26, delegated): the build run
  re-grounds on each at the pass, re-derives S5's and S6's readers with `git grep -n -e prebuild -e
  CHECKLIST -e "for-diff HEAD~1"`, and stops the unit if a called section is still absent then, rung 1
  (the brief's rule for DEFERRED parents). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 4, the brief's J4, J5, J21 and D3,
  scout B's row 4, and the source at `1a3ce03d`.

## 10. Reuse audit

The seams extended: `records` and `build_record` (`tools/memory-tree/gotchas.py:289`, `:271`), which
key each record by its `name`, and the checklist print (`:734-748`), which `--for-names` reuses; the
dispatch in `main` (`:1327`, `:1366-1381`); `render_handoff`'s `Not supplied, optional:` line
(`tools/roles/handoff.py:412-414`), the one absent-input rendering today, which the slot renderer
generalises; `resolve_kit_dir` (`tools/roles/roles_lib.py:97`) for the memory-tree kit. `python
tools/codebase-map/reuse_lookup.py "render an optional work order field in its filled, searched-empty
or not-installed state"` returned name-stem candidates (`search`, `note`, `render_line`), none a slot
renderer; `python tools/codebase-map/reuse_lookup.py "print the checklist items of bug class records
named by the spec"` ranked `records` in `gotchas.py` first, the seam S3 extends. The recall probe
returned scout B's row, the fates record's `RESHAPED` row for `gotchas.py` (`fates.md:66`), the
night-pass-two review's M11, TOOL-aMendedFleet-74, which made `prebuild`, and TOOL-dFairHearing-15,
which owns the review checklist and the charter line. Where scout B and source disagree: scout B
read `MEMORY_TREE_DIR` as existing only for the Skill's checklist line, and source shows
`SKILL.template.md:67` and the conf stamp read it too, so S6 re-words the adopter and keeps the key;
scout B did not list the `[[contract]]` consumer at `tools/memory-tree/kit.toml:439` or M8's pointer
at `BUILD-METHOD.template.md:253`, both readers S6 now names.

Recall terms used: `python tools/memory-recall/query.py "why does the bug-class checklist selected by
a write set retire and what replaces it in the work order" --terms "gotchas for-paths for-diff
prebuild per-pass checklist NT-24 NT-25 bug-classes slot not-installed searched-empty"`
