# TOOL-dSafePassage-10 — the step gate: the adopter-visible surface population diffed between a landing's base and its tip

**Status:** DEFERRED · rev-3 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0027@46290183 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-10-deviation-110.md](../build/2026-10-23-build-TOOL-dSafePassage-10-deviation-110.md) | deviation | — |
| [2026-10-24-build-TOOL-dSafePassage-10-deviation-154.md](../build/2026-10-24-build-TOOL-dSafePassage-10-deviation-154.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |
| [2026-10-24-prompt-TOOL-dSafePassage-1-dgroundrules-reground.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-dgroundrules-reground.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-11 TOOL-dSafePassage-13 |
| [2026-10-24-prompt-TOOL-dSafePassage-10-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-10-1-spec-writer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-10-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-10-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-8 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |

<!-- /gen:spec-records -->

## 1. Goal

A landing that makes an adopter-visible member vanish, by a rename, a removal or a retirement, with
no `[[upgrade]]` or `[[retired]]` row naming it in `surfaces`, reds at a new leg, `step-gate`, before
it reaches any adopter. Today nothing reds it: a renamed installed file, hook entry, command, agent
or conf key reaches adopters with nothing to carry them across, and a removed registry entry refuses
their whole update (`gap-deploy-25`, closed by this unit). It is P38's "a landing that removes,
renames or retires such a surface with no step reds at dSafePassage's step gate (SA-11)".

## 2. Scope (IN)

- **S1** — The class registry, `tools/govkit/surface-classes.toml`: one `[[class]]` row per class of
  adopter-visible member, each naming its class id, its reader, its plant and a summary, with an
  optional own-record witness. Nine rows ship, one per class the clause names (§4 "### Data model").
  A later build's class joins by adding its own row, and that row both arms the join and plants its
  own red, because a row naming no plant is refused (S5). Observed by AC1, AC7 and AC8.
- **S2** — The one population reader, `read_surface_population` in `tools/govkit/step_gate.py`, which
  runs every class row's reader over one tree and returns members spelled `<class>:<name>` (brief
  S6). It is the reader the docs leg imports. Observed by AC1 and AC12.
- **S3** — The gate. It resolves the landing's base, reads the population at the base and at the
  tip, and computes each member present at the base and absent at the tip. A member is witnessed when
  some `[[upgrade]]` or `[[retired]]` row at the tip names it in `surfaces`, or when its class's own
  change record names its successor. Every unwitnessed member is a red line, and the gate exits 1.
  A content-only edit changes no member and needs no row. Observed by AC2, AC3, AC4, AC5, AC6, AC7
  and AC12.
- **S4** — The own-record witness: a class row whose `witness` names a reader of that class's own
  change record reads that record as its one witness, in place of a step row. Observed by AC9.
- **S5** — The refusals, exit 2 with the reason: a registered class whose population at the tip is
  empty, a class row with no reader or no plant, a reader that will not load, and a base that does
  not resolve. Observed by AC8 and AC10.
- **S6** — One base rule. The base resolution inside `cmd_epoch` (`tools/govkit/govkit.py:13446-13474`)
  is extracted into `resolve_landing_base`, which `cmd_epoch` and the gate both call, so the two legs
  that grade a landing's range read one base. Observed by AC10.
- **S7** — The fixture, on the gate's own CLI: `--fixture --plant <case>` builds a scratch clone,
  commits one plant on it and grades that range, and `--with-row` adds a conforming witness row
  naming the planted member. The plants are each class row's own plant and `content-edit`, plus four
  plants of the registry's own shape for S4 and S5. Observed by AC2 to AC9.
- **S8** — The leg row `step-gate` in `tools/gate-legs.json`, and the rows a new leg owes the
  meta-gates that grade it: an `[[exempt_leg]]` row in `tools/govkit/registry.toml`, a row in
  `tools/govkit/subject-pins.tsv`, a row in `tools/run-gates/ceiling-evidence.txt` and the name in
  the `gate-legs` list of `memory/map/features/govkit.md`. Observed by AC11.
- **S9** — The docs: a page `help/step-gate.md` saying what the gate reds, how a landing answers it
  with a row, and how a later class joins, and its line in `help/README.md`. Observed by AC13.

## 3. Non-goals (OUT)

- The `[[upgrade]]` and `[[retired]]` row grammar, its one reader and the frozen-row check: all
  TOOL-dSafePassage-1's. This unit reads `surfaces` through that reader and parses no row itself.
- The docs leg, its usage rows and its fingerprints: TOOL-dSafePassage-13, which imports S2's reader.
- A change of meaning behind an unchanged name. P38 gives that to the review, and a name-keyed
  population cannot see it.
- Whether a step row's up actually carries the member it names: the `upgrade-walk` leg's question
  (TOOL-dSafePassage-5), never this one's.
- The later classes v2 names, among them record-kind schemas and gov's instruction-unit tags. Each
  joins with its own row when its build lands it.
- The fates-table conformance arm the supersession research proposes (`research-supersession.md`
  section 5). No clause of this build's row carries it.
- Running any step, or writing any row for a member the gate reds. The landing's author writes the
  row; the gate only names what is missing.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — the `[[upgrade]]` and `[[retired]]` grammar (brief S1, S2) and its one reader in `tools/govkit/upgrade_steps.py` (brief S3); without it the gate has no `surfaces` to read and every vanished member is red
- **consumes-from** `TOOL-dSafePassage-8` — gov's source-mode receipt `.governance/install.json` (brief S10), the population of the `file` class; without it that class is empty and the gate refuses
- **consumes-from** external — dGroundRules' policy schema catalogue (`cl-dClosedLoop-0007`), `tools/policy/catalogue.toml` (TOOL-dGroundRules-1 S3), whose `[[key]]` names are the population of the `policy` class; without it that class is empty and the gate refuses
- **hands-off** `TOOL-dSafePassage-13` — the one population reader of S2, which the docs leg imports over the same class registry rather than reading members a second way
- **hands-off** external — each later build whose class joins the registry writes its own class row, its reader and its plant, as the clause's "each later class joining" sets
- **hands-off** `TOOL-dSafePassage-21` — the file class reading gov's planned destinations when the tree carries no source receipt, the repair of finding 5
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built

## 4. Design

### Data model

The class row, in `tools/govkit/surface-classes.toml`:

```toml
[[class]]
id = "agent"                                   # the <class> half of every member id
reader = "govkit/step_gate.py:read_agent_members"   # <path under the tool root>:<function>
plant = "govkit/step_gate.py:write_agent_plant"     # stages one vanished member in a clone
summary = "each role agent an adopter's roles kit renders, by its stem"
# witness = "<path>:<function>"   optional: a reader of the class's own change record
```

A reader is `reader(root: pathlib.Path) -> set[str]`, the member names over one tree. A plant is
`plant(clone: pathlib.Path) -> str`, which edits and stages one change in the clone and returns the
member id it made vanish. A witness reader is `witness(root) -> set[str]`, the names its record gives
a successor. All three are loaded from the TIP's tree, so one predicate grades both sides (§8 F2).

The nine classes. A member id is `<class>:<name>`, split on its first colon, and this table is the
one spelling every `surfaces` value in this build uses (§8 F4):

| Class | A member is | Read from |
|---|---|---|
| `file` | each `files` row's `path` in gov's source-mode receipt | `.governance/install.json` (TOOL-dSafePassage-8) |
| `installable` | each destination a descriptor survivor of a role in `EPOCH_ROLES` resolves to under `canonical_ctx` | `read_descriptors` and `resolve_entry`, as `cmd_shipped --epoch` reads them (`govkit.py:13283-13311`) |
| `hook` | each tracked `*.fragment.json` file's `name` | the fragment files, the population `run_fragment_merges` wires (`govkit.py:6109-6177`) |
| `command` | each survivor destination shaped `.claude/skills/<name>/SKILL.md`, as `<name>` | the same survivors as `installable` |
| `agent` | each `<name>` of a tracked `tools/roles/agents/<name>.agent.md` | `git ls-files` over the roles kit's agents |
| `conf` | each key a descriptor's `[config]` declares in `required_keys_gate`, `required_keys_render` or `defaults`, as `<conf file>#<KEY>` | the descriptors, the lists `read_conf_key_gaps` reads (`govkit.py:5194-5200`) |
| `policy` | each `[[key]]` row's `name` in the policy schema catalogue | `<root>/tools/policy/catalogue.toml` (TOOL-dGroundRules-1 S3) parsed with `tomllib`, so the base worktree and the tip each read their own catalogue (§8 F6) |
| `verb` | each verb a declared usage source states, as `<cli>:<verb>` | `VERB_SOURCES`: `govkit.py`'s `USAGE` lines (`govkit.py:13588-13599`) and `unattended.sh`'s usage header (`unattended.sh:5-24`, which its own `usage()` reads at `:135-147`) |
| `entry` | each registry `[[entry]]` row's `id` | `load_registry` (`govkit.py:247-268`) |

A path-valued name, in the `file` and `installable` classes, spells a path under the tool root with
the `{prefix}` token in place of the root `derive_tool_root` returns (`govkit.py:154`), so
`installable:{prefix}/hooks/agent-cap.js` names the same member at every install prefix and a row
written in gov names what an adopter sees. A path outside the tool root is spelled as it is.

What a class reader does not see, stated so no reader of a green line takes it for more: a conf key a
kit reads and never declares in `[config]`; a verb of a CLI that no `VERB_SOURCES` row names; an
agent or Skill an adopter wrote for itself. Each is a reader's population, and a wider reader joins
by changing its class row.

### The gate, `tools/govkit/step_gate.py`

```
python tools/govkit/step_gate.py [--base <rev>]
python tools/govkit/step_gate.py --list
python tools/govkit/step_gate.py --print-base [--base <rev>]
python tools/govkit/step_gate.py --fixture --plant <case> [--with-row]
```

1. **The base.** `resolve_landing_base(root, base)` in `govkit.py`, extracted from `cmd_epoch`
   unchanged: an explicit `--base`, else a non-zero `GATE_PUSH_BASE`, else the merge-base with the
   default branch the remote ladder names (`resolve_remote`). It returns `(sha, boundary, refusal)`,
   and `cmd_epoch` keeps printing its own lines from that triple. An unresolvable base is exit 2.
2. **The classes** come from the tip's `tools/govkit/surface-classes.toml` (`read_surface_classes`).
   A row missing `id`, `reader` or `plant`, a duplicate `id`, or a reader or plant that will not load
   is exit 2 naming the row.
3. **The tip population** is `read_surface_population(root, classes)` over the working tree the leg
   runs in, which at the lander is the prepared merge.
4. **The base population** is `read_base_population(root, sha, classes)`: a detached worktree at the
   base under `tempfile.mkdtemp`, added with `--no-checkout`, a non-cone sparse pattern `/*` and
   `!/memory/`, then checked out, the same readers run over it, and the worktree removed in a
   `finally`. `memory/` is excluded because no class reads it, and it was 5384 of 5834 tracked paths
   at `3708a705` (PINNED, measured by `git ls-files`). A worktree that will not add is exit 2.
5. **The witnesses** are `read_witnessed_members(root, classes)`: the union of every `surfaces`
   value on every `[[upgrade]]` row (the descriptors and `tools/govkit/steps.toml`) and every
   `[[retired]]` row (`tools/govkit/registry.toml`) at the tip, read through TOOL-dSafePassage-1's
   reader, plus each class's own-record witness names, prefixed with that class.
6. **The verdict.** `derive_vanished_members(base_pop, tip_pop)` is the base set minus the tip set.
   Each vanished member no witness names prints one red line and the gate exits 1. Before that, a
   class whose tip population is empty is exit 2, because a green over an empty class grades nothing.
   A class empty at the base only is the class joining in this range, and that is no finding.

Output, every line prefixed `step-gate:`:

```
step-gate: base 3708a705 (merge-base with origin/main) · tip the working tree
step-gate: 9 classes · 412 members at the tip · 2 vanished · 1 witnessed
step-gate: RED agent:gov-skeptic vanished with no [[upgrade]] or [[retired]] row naming it in surfaces
```

The figures in that sample are illustrative; every count is DERIVED at the run.

The leg row: `{"name": "step-gate", "argv": ["python", "{prefix}/govkit/step_gate.py"], "chunk":
"declarations", "subject": "repo", "reads": {...}}`, with no `guard`, because the classes span
`tools/`, `skills/`, `.claude/` and `.governance/` and a guarded leg would skip a landing that moves
a member outside its guard. Its `reads` declares `base` and `history`, as `kit epoch (shipped bytes
move, the version moves)` declares them (`tools/gate-legs.json:1433`), since its verdict is a function
of the base it resolves and not of the tree alone. Its `ceiling` is the measured time (§5).

### The fixture

`--fixture --plant <case>` clones the working repository at HEAD with `git clone --no-checkout
--shared` into `tempfile.mkdtemp(prefix="sg-")`, sets the same sparse pattern, checks out, applies the
plant, commits it, and runs the gate with `--base` at the clone's pre-plant commit. `--with-row` then
adds one witness row naming the planted member through `write_witness_row`: a `[[retired]]` row in
the clone's `tools/govkit/registry.toml` for an `entry` member, and an `[[upgrade]]` row in the
clone's `tools/govkit/steps.toml` otherwise, each in brief S1's and S2's grammar. The clone is removed
in a `finally`. The cases:

| Case | What it stages | Exit, no row | Exit, with row |
|---|---|---|---|
| `<class id>`, each of the nine | that class row's own plant | 1 | 0 |
| `content-edit` | one byte appended to an installed engine file | 0 | 0 |
| `empty-class` | a class row whose reader returns nothing | 2 | 2 |
| `no-plant` | a class row with no `plant` | 2 | 2 |
| `own-record` | a fixture class whose `witness` names the vanished member | 0 | 0 |
| `own-record-unnamed` | the same class, its `witness` naming another member | 1 | 0 |

The plants of the four classes the clause seeds red: `installable` renames one installed file (a
`git mv` of its source and its rule's `to`); `agent` renames one agent file; `entry` deletes one
registry `[[entry]]` row with its descriptor; `policy` deletes one `[[key]]` table from the clone's
`tools/policy/catalogue.toml`.

### Inventory

Minted: the module `tools/govkit/step_gate.py`; the file `tools/govkit/surface-classes.toml` and its
`[[class]]` keys `id`, `reader`, `plant`, `witness` and `summary`; the nine class ids of the table
above; the constant `VERB_SOURCES`; the functions `read_surface_classes`,
`read_surface_population`, `read_base_population`, `read_witnessed_members`,
`derive_vanished_members`, `check_step_gate`, `write_witness_row` and `main` in the module, one
`read_<class>_members` reader and one `write_<class>_plant` plant per class, `write_content_plant`,
and `resolve_landing_base` in `govkit.py`; the CLI flags `--base`, `--list`, `--print-base`,
`--fixture`, `--plant` and `--with-row`; the leg name `step-gate`; the output prefix `step-gate:`.
Naming cells: every minted function passes `py.function`, checked with
`tools/lexicon/lexicon.py --suggest <name> --as py.function`, OK for all of them; a module file, a
TOML key and a class id fall in no declared cell.

### Migration

Additive. No adopter carries anything this unit writes, since the deployer never travels
(`tools/govkit/registry.toml`, the `[[exempt_leg]]` rows for its legs). The `epoch` extraction moves
no line `cmd_epoch` prints.

### Rollout

Live at landing as a refusing leg. It grades its own landing's range, and this unit makes no member
vanish, so its first run is green when every class reads non-empty, which needs TOOL-dSafePassage-8's
receipt and dGroundRules' catalogue landed first (§3 Edges). The build run lands those two before
this unit by its order. `govkit.py` is also written by TOOL-dSafePassage-6 and TOOL-dSafePassage-9,
so the three passes sequence by M6's disjointness rule rather than run concurrently.

### Files touched (estimate)

- `tools/govkit/step_gate.py` (new)
- `tools/govkit/surface-classes.toml` (new)
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/gate-legs.json`
- `tools/run-gates/ceiling-evidence.txt`
- `memory/map/features/govkit.md`
- `help/step-gate.md` (new)
- `help/README.md`

### Alternatives rejected

- **Reading the base through blob reads at a commit** (`git cat-file`, as `blob_at` does). Every
  reader in the table walks a tree on disk, `resolve_entry` and `load_registry` among them, so each
  would need a second implementation reading blobs, and two readers of one population is the class
  the charter's one-fact rule names. §8 F1.
- **A committed snapshot of the population**, diffed at each landing. It is an inventory typed beside
  what it describes, which the charter's derive rule refuses.
- **An arm inside `govkit selfcheck`.** The clause names a leg, and selfcheck grades one tree with no
  base. §8 F5.
- **Keying `installable` on sources.** A source that moves while its destination stays is invisible
  to an adopter, so a source key would red a change no adopter sees.

## 5. Production-readiness checklist

- security: the gate reads and writes nothing in the graded tree; the readers it loads come from gov's own tip, the trust the leg already has; the fixture writes only inside its own temp clone and removes it.
- perf / scale: one population read per side and one sparse worktree of about 450 paths, DERIVED from `git ls-files` at the run; the leg's `ceiling` is set from its measured time at the build pass, recorded in `tools/run-gates/ceiling-evidence.txt`.
- error / empty / loading states: an empty class at the tip, a malformed class row, an unloadable reader and an unresolvable base each exit 2 with the reason, never a green over nothing.
- observability: one summary line with the class count, member count, vanished and witnessed counts, then one line per red member naming its id.
- risks: a sibling unit spelling a member id its own way, so its row witnesses nothing (§8 F4); a CI checkout too shallow for the merge-base, which refuses exactly as `epoch` refuses.
- testing: the fixture plants of §4, run by AC2 to AC9 and by the new selftest arm (§7).
- migration: additive; §4 "### Migration".
- user docs: `help/step-gate.md` and its `help/README.md` line (S9).

## 6. Acceptance criteria

- **AC1** — When `python "tools/govkit/step_gate.py" --list` runs on the tree after the pass, it prints
  one line per class row of the class registry, nine lines, each naming its class id and a non-zero
  member count at the tip.
  Red when: a class reader returns nothing on gov's own tree, or the list is typed in the module
  rather than read from the registry.
  figure: nine is PINNED to the rows this unit ships; each count is DERIVED at the run.
- **AC2** — When `python "tools/govkit/step_gate.py" --fixture --plant installable` runs, it exits 1
  with a `RED installable:` line naming the renamed file's old destination; with `--with-row` added it
  exits 0.
  Red when: the class keys on sources rather than destinations, or the witness union does not read
  `surfaces` from the `[[upgrade]]` rows.
  cost: one scratch clone per run, seconds to tens of seconds, measured at the build pass.
- **AC3** — When `python "tools/govkit/step_gate.py" --fixture --plant agent` runs, it exits 1 with a
  `RED agent:` line naming the old agent stem; with `--with-row` it exits 0.
  Red when: the agent class reads the rendered `.claude/agents` copies, which a rename in the kit does
  not move until a render.
- **AC4** — When `python "tools/govkit/step_gate.py" --fixture --plant entry` runs, it exits 1 with a
  `RED entry:` line naming the deleted registry entry; with `--with-row`, which writes a `[[retired]]`
  row naming it, it exits 0.
  Red when: the witness union reads the `[[upgrade]]` rows and not the registry's `[[retired]]` rows.
- **AC5** — When `python "tools/govkit/step_gate.py" --fixture --plant policy` runs, it exits 1 with a
  `RED policy:` line naming the deleted catalogue key; with `--with-row` it exits 0.
  Red when: the policy class is absent from the registry, reads the repository's set values in
  place of the catalogue's keys, or reads one fixed `catalogue.toml` rather than the one under the
  root it is given, so base and tip read one catalogue and nothing vanishes.
  fixture: needs dGroundRules' catalogue landed, which the build run lands first (§3 Edges).
- **AC6** — When `python "tools/govkit/step_gate.py" --fixture --plant content-edit` runs, it exits 0
  and its summary line reports 0 vanished.
  Red when: a member is keyed on bytes or a blob id, so an edit reads as a vanish.
- **AC7** — When `python "tools/govkit/step_gate.py" --fixture --plant <class>` runs for each of `file`,
  `hook`, `command`, `conf` and `verb`, each exits 1 naming one member of its class, and each exits 0
  with `--with-row`.
  Red when: a class row's plant stages nothing its reader sees, so the row arms no red.
- **AC8** — When `python "tools/govkit/step_gate.py" --fixture --plant empty-class` runs, it exits 2
  naming the class whose tip population is empty; `--plant no-plant` exits 2 naming the row that lacks
  a `plant`.
  Red when: an empty class is skipped and the gate exits 0, or a class row is accepted with no plant.
- **AC9** — When `python "tools/govkit/step_gate.py" --fixture --plant own-record` runs, it exits 0 with
  the vanished member counted as witnessed; `--plant own-record-unnamed` exits 1 naming it.
  Red when: a class's `witness` reader is never called, or is called in place of the step rows rather
  than beside them.
- **AC10** — When `python "tools/govkit/step_gate.py" --print-base --base HEAD~1` runs, it prints the
  sha `git rev-parse HEAD~1` prints; with no `--base` it prints the sha `git merge-base origin/main HEAD`
  prints; and `git grep -n -e "resolve_landing_base(" -- tools/govkit` finds one definition, in
  `tools/govkit/govkit.py`, and a call from `cmd_epoch` and from the gate.
  Red when: the gate resolves its base by its own code, so the two legs can grade different ranges.
- **AC11** — When `git grep -n -F "step-gate" -- tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt memory/map/features/govkit.md`
  runs, each of the five files carries the leg's name once.
  Red when: the leg row lands without one of the rows a new leg owes its meta-gates.
- **AC12** — When `python "tools/govkit/step_gate.py" --base HEAD` runs on the tree after the pass, it
  exits 0 with 0 vanished and a non-zero member count in every class.
  Red when: a class is empty on gov's own tree, or base and tip at one commit report a vanish.
- **AC13** — When `git grep -n -e "step-gate" -- help/` runs, it finds the page and its line in the
  help index.
  Red when: the leg ships with no page under `help/`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `recall floor` · `recall floor arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The new leg `step-gate` is not on the list above, since the list names legs the manifest holds
today; the main loop observes it at the close through the arm lines below.

New arm: tools/govkit/step_gate.py · covers AC12 · the new `step-gate` leg itself, its failing case staged by committing any class row's plant onto a scratch clone · none
New arm: tools/govkit/selftest.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · a new arm runs the gate's fixture over every class row's plant with and without `--with-row` and over `content-edit`, `empty-class`, `no-plant`, `own-record` and `own-record-unnamed`, asserting each exit · none

## 8. Open questions

- **F1 — How the base side's population is read.** Options: (a) a detached sparse worktree at the
  base, the tip's readers run over it; (b) every reader rewritten to read blobs at a commit; (c) a
  committed snapshot of the population. (b) is a second implementation of each reader, and (c) an
  inventory typed beside what it describes. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3:
  it survives both rejected options' vetoes and reuses every govkit reader unmodified, the tie-break
  M3 names. widens: none · relaxes: none
- **F2 — Whose readers grade the base: the base's or the tip's.** Options: each side's own readers;
  the tip's readers over both trees. With each side's own, a reader changed in the range compares two
  predicates and reads a predicate change as a vanish. RESOLVED (agent, 2026-10-23, delegated): the
  tip's, rung 3, so a class joining in a range also reads the base and is never red for its own
  arrival. widens: none · relaxes: none
- **F3 — The sources of the `conf`, `verb` and `command` classes, which the clause names without a
  source.** Options: each class read from what gov already declares (the `[config]` lists, the two
  declared usage texts, the Skill destinations); a scan of every shipped file for keys and verbs.
  A scan has no closed grammar to match against, so its population is a guess. RESOLVED (agent,
  2026-10-23, delegated): the declared sources, rung 3, with what each does not see stated in §4
  "### Data model". The clause names the classes and not their readers, so this departs from no text
  of it, and a wider reader joins by changing its row. widens: none · relaxes: none
- **F4 — The spelling of a member id across this build.** TOOL-dSafePassage-1's legacy-home steps,
  TOOL-dSafePassage-3's and TOOL-dSafePassage-11's steps each write `surfaces` values, and their
  writers run beside this one. Options: each spec spells members its own way; this spec's class table
  is the one spelling. RESOLVED (agent, 2026-10-23, delegated): the class table of §4, the brief's S6
  making this unit the owner of the population, rung 1. The M2 interface cross-read before the first
  code pass fixes any sibling spelling in that sibling's spec, with a rev bump. Read at writing:
  TOOL-dSafePassage-13's spec copies this table's nine ids; TOOL-dSafePassage-1's example rows spell
  `conf-key:` where this table spells `conf`, and its own §8 F6 defers that spelling to this
  registry, so the fix is a `conf` spelling there. Its `file:{prefix}/...` spelling already matches
  §4's `{prefix}` rule. widens: none · relaxes: none
- **F5 — A leg of its own, or an arm of an existing leg.** Options: a new leg `step-gate`; an arm of
  `govkit selfcheck`; an arm of `kit epoch (shipped bytes move, the version moves)`. The clause says
  "a leg", and the brief's S7 fixes the name. RESOLVED (agent, 2026-10-23, delegated): the new leg,
  rung 1, with every row the meta-gates owe it (S8). widens: none · relaxes: none
- **F6 — How the `policy` class reads the catalogue's keys.** Options:
  (a) `read_policy_key`, the bash `KEY=value` parser of the legacy homes, which gains no TOML parse
  (TOOL-dGroundRules-2 S8); (b) `load_catalogue(kit)` imported from the policy kit, which a sibling
  kit may not import (TOOL-dGroundRules-1, `:105`); (c) a `git show <rev>:<path>` blob read, F1's
  rejected option (b) for one class, with no revision to name for a tip that is a working tree;
  (d) `tomllib` over `<root>/tools/policy/catalogue.toml`, taking each `[[key]]` row's `name`.
  RESOLVED (agent, 2026-10-24, delegated): (d), rung 1, TOOL-dGroundRules-1's catalogue (S3, its
  loader at `:171`) and its sibling-kit rule (`:105`); the root is the tip's tree or F1's base
  worktree, so both revisions are read. TOOL-dGroundRules-11's AC5 reads the catalogue the same
  way. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-21`, `TOOL-dSafePassage-26`; no other section moved.
- rev-3 · 2026-10-24 · §3 · §4 · §6 · §8 · re-grounded on dGroundRules' landed specs by the cross-check record `../build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`, rows 33 and 34: the `policy` class reads `tools/policy/catalogue.toml`'s `[[key]]` names with `tomllib` under each side's root, the Edge, the class row, the plant and AC5 name that file, and F6 is re-resolved on rung 1.

## 10. Reuse audit

The seams extended are in `tools/govkit/govkit.py`: `cmd_epoch`'s base resolution (`:13446-13474`),
extracted into `resolve_landing_base` at its second caller, the charter's factory rule; the survivor
derivation `resolve_entry` (`:452-495`) filtered by `EPOCH_ROLES` (`:13311`), as `cmd_shipped`
(`:13283-13306`) already reads it; `load_registry` (`:247-268`); the `[config]` key lists as
`read_conf_key_gaps` reads them (`:5194-5200`); and `USAGE` (`:13588-13599`) beside
`tools/unattended/unattended.sh`'s header (`:5-24`, read by its own `usage()` at `:135-147`).
`reuse_lookup.py "diff the adopter-visible surface population between a base commit and the tip"`
ranked `population` (`tools/govkit/refusal_join.py:189`), which lists govkit's own Python files and
is no adopter surface, `resolve_compare_base` (`tools/codebase-map/map_lib.py:1502`), a copy of the
bar's base rule that its docstring says is copied because a kit may not read a sibling kit and that
reads no `GATE_PUSH_BASE`, and `read_commit_paths` (`tools/codebase-map/map_diff.py`), the paths a
commit touched rather than a population. `reuse_lookup.py "grade a landing from GATE_PUSH_BASE against
the merge-base with the default branch"` ranked no base resolver inside govkit, because `cmd_epoch`'s
is inline, which is why S6 extracts it. No existing seam reads a member population by class, so the
gate is new and every reader under it is an existing govkit read. Where a record and the source
disagree: the supersession research cites the verdict grid at `govkit.py:8048` and `_cmd_update` at
`:8777`; at `3708a705` they sit at `:8419-8429` and `:9154`. The recall probe found the clause, the
shape audit's step-gate finding (`reviews/2026-10-18-review-PLAY-dClosedLoop-1-shape-audit-b.md:259`)
and SA-11's answer, "Yes, the gate (Recommended)".

Recall terms used: `python tools/memory-recall/query.py "how does a landing that renames or removes an adopter-visible surface get caught before it reaches adopters" --terms "step gate surface population upgrade retired successor rename removal registry entry agent policy key"`
