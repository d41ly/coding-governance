# PLAY-dOrderedCharter-88 — the `repo` namespace reads its purpose path-only, and the reader join counts a unit scoped `reader.every` as selected by every reader

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-2 · base 9b9e829df · streams tooling · order 49 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 PLAY-dOrderedCharter-84 PLAY-dOrderedCharter-85 PLAY-dOrderedCharter-86 PLAY-dOrderedCharter-87 |
| [2026-11-12-build-PLAY-dOrderedCharter-88-1-builder-return.md](../build/2026-11-12-build-PLAY-dOrderedCharter-88-1-builder-return.md) | journal | — |
| [2026-11-12-build-PLAY-dOrderedCharter-88-deviation-881.md](../build/2026-11-12-build-PLAY-dOrderedCharter-88-deviation-881.md) | deviation | — |
| [2026-11-12-build-PLAY-dOrderedCharter-88-ledger.md](../build/2026-11-12-build-PLAY-dOrderedCharter-88-ledger.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-88-1-spec-writer.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-88-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-88-build-brief.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-88-build-brief.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-88-spec-brief.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-88-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's bar over the prepared merge `422abe7c3` red the `tags (the resolver's checks)` leg with 11
findings. The upgrade step `playbook/adopter-rules-to-overlay` wrote gov's nine adopter rules into the
overlay as level-0 `repo` units, each scoped `reader.every`. Nine reds say each unit lacks the `help`
field the `repo` namespace's purpose source asks for. Two say `reader.driver` and `reader.subagent`
select no unit. HEAD holds no overlay, so no bar before the lander's prepare saw either.

This unit fixes both at the class, for every adopter whose rules the step converts. The `repo` row
reads its members' purpose path-only, since no writer of an overlay unit asks for `help`. The reader
join counts a unit scoped `reader.every` as selected by every declared reader, the rule both
load-set readers already apply. The next `--prepare` and close then read no tags red.

## 2. Scope (IN)

- **S1** — In `tools/playbook/namespaces.toml`, the `repo` row's `purpose-source` changes from
  `.governance/instructions.toml#help` to `.governance/instructions.toml`. The arm then prints the
  namespace path-only and grades no member's field. Observed by AC1 and AC6.
- **S2** — In `tools/playbook/tag_index.py`, `check_namespace_joins` gains a keyword-only parameter
  `every`, the wildcard reader tag, with no default. In the selecting branch, after `dec` is read,
  when `every` is among the namespace's selectors, every declared member counts as selecting the
  units `every` selects. The function's docstring gains one sentence saying so, with the phrase
  `every reader loads` on one line. Observed by AC1, AC3 and AC4.
- **S3** — In `tools/playbook/gov_tag.py`, `run_check` passes `every=instruction_units.EVERY` to
  `check_namespace_joins`, its one caller. The module already imports `instruction_units`. Observed
  by AC1 and AC3.
- **S4** — The tag resolver's plants. The `dead-selector` plant declares `reader.one` and
  `reader.ghost` and scopes its unit `reader.one`, and its second half writes `reader.one` alone. A new
  plant, `every-selector`, declares `reader.every` and `reader.ghost` and scopes one unit
  `reader.every`. It joins the plant names in `PLANTS` and the shape plants in `SHAPE_PLANTS` of
  `tools/playbook/gov_tag.py`, beside `dead-selector`. `tools/playbook/adopt-playbook.sh` gains its
  row in the tag resolver's plant rows, and that block's comment gains one clause naming it.
  Observed by AC3 and AC4.
- **S5** — The join's two prose readers say the new rule. `help/tags.md`'s join item and
  `tools/playbook/README.md`'s joins sentence each say that a unit scoped `reader.every` is selected
  by every reader. Each spells the phrase `every reader loads` on one line. Observed by AC5.

## 3. Non-goals (OUT)

- Any change to the wording of an adopter rule, or to the rows the step writes.
- A `help` field on any overlay row, written by the step or by hand.
- Retiring `reader.driver` or `reader.subagent`, or editing `tools/playbook/readers.toml`.
- The `practice` namespace's join. It has no wildcard member, and the rule in S2 never fires for it.
- The `unit` namespace's purpose source, `#help`, which gov's four kit units satisfy.
- `database is locked` on the shared tag index, which red the `instruction edits (manifest checks)`
  leg at the same close. It is contention between two legs reading one index, and this unit does
  not touch the index.
- A version bump of the playbook kit. The lander mints kit versions into the prepared merge
  (`tools/push-main.sh@c7cd70b9:26-29`).

### Edges

- **consumes-from** external — PLAY-dOrderedCharter-87's upgrade step, CLOSED, whose level-0
  `adopter-rule` rows, each scoped `reader.every`, are the population both reds come from.
- **hands-off** external — the main loop re-runs `bash tools/push-main.sh --prepare --slug dOrderedCharter`
  and then the close's bar over the new prepared merge (section 7).
- **hands-off** external — the index contention named in the non-goals, for the main loop to
  re-run or schedule apart if it recurs.

## 4. Design

### Evidence

Read at `9b9e829df`. A role agent's scratch guard refuses the tags leg's command, so each figure
below comes from a probe that calls the two arms, `check_namespace_purpose` and
`check_namespace_joins`, over a scratch clone. The clone keeps its history, has a local `main` at
`origin/main`, and has `origin/HEAD` set to `main`. In it, `adopter_rules_to_overlay.py up .` wrote
an overlay byte-identical to the merge's, apart from line endings (PINNED, `diff` against
`fold88/instructions-over-merge-422abe7c.toml`), and the probe committed it.

- The reds reproduced (PINNED, the probe at `9b9e829df`). The two arms read 2 join reds and 9
  purpose reds, the same 11 lines the merge's log ends with.
- Where the nine come from. The `repo` row's source is `.governance/instructions.toml#help`
  (`tools/playbook/namespaces.toml@ec810577:105-112`). The arm grades each member at a `.toml` path
  for the field on its row, and reds a member that lacks it
  (`tools/playbook/tag_index.py@243b435f:1266-1278`). The step writes `tag`, `level`, `type`, `scope`
  and `text` and no `help` (`tools/govkit/steps/adopter_rules_to_overlay.py@afcfe177:107-111`).
- No writer of an overlay unit asks for `help`. The schema requires only `tag`, `level` and `type`
  (`tools/playbook/instruction_units.py@6e7d4f51:199`). The overlay page's sample unit carries no
  `help` (`help/overlay.md@34b82136:13-21`). So an adopter who follows that page reds the same arm.
- No tree has graded a `repo` member's purpose. With no overlay served, the arm prints the row
  `pending` and grades nothing (`tools/playbook/tag_index.py@243b435f:1248-1250`). HEAD holds no
  overlay, and the one tree that held one was the merge, which is on no branch.
- Where the two come from. A `selects` namespace whose members are not units is graded once some
  unit's `scope` names one of its tags. Then each declared member that no selector row names reds
  (`tools/playbook/tag_index.py@243b435f:1134-1146`). Gov's four kit units carry no `scope`, so at
  HEAD the reader join prints `unarmed`. The step's nine rows each select `reader.every`, which arms
  the join, and `reader.driver` and `reader.subagent` are then named by no selector
  (`tools/playbook/readers.toml@285fd399:11`, `tools/playbook/readers.toml@285fd399:15`).
- The join disagrees with the selection rule. A document's units are those whose `scope` holds its
  selector or `reader.every` (`tools/playbook/instruction_units.py@6e7d4f51:473-478`). Every reader's
  load set begins with the units scoped `reader.every`
  (`tools/playbook/load_sets.py@055efbb3:246`). So `reader.driver` does select the nine units, and
  the join is the only reader that says it does not.
- The instruction-edits reader carries the same reds. Its `check_tree` runs the tag check and adds
  its reds (`tools/playbook/instructions_edit.py@57e11a29:525-528`), through `run_tag_check`, which
  calls the same `run_check` (`tools/playbook/instructions_edit.py@57e11a29:425-433`).

### The purpose source (S1)

```toml
purpose-source = ".governance/instructions.toml"
```

A `<path>` source with no `#` prints the namespace path-only and grades no member
(`tools/playbook/tag_index.py@243b435f:1251-1253`). The path is still not served at HEAD, so the
row stays `pending` there. Over a tree holding an overlay, the purpose summary reads
`tags: purpose · 7 graded over 131 members, 3 path-only, pending 0` (PINNED, the probe with S1 to
S3 applied). At the merge it read 8 graded over 140 members, 2 path-only.

### The join (S2, S3)

The lines added in the selecting branch, directly after `dec = declared.get(ns, {})`:

```python
            if every in sel:  # a unit scoped `every` is in each member's load set
                sel = {**{t: sel[every] for t in dec}, **sel}
```

Each declared member gains the wildcard's selector row as its own, so it is not unclaimed. A
member some unit names keeps its own row, which `**sel` writes last. No added tag is undeclared, so
the stale direction is unchanged. The wildcard enters as a parameter because `tag_index` does not
import `instruction_units`, and an import would join it to the extractors' version closure
(section 4, "Alternatives rejected").

Over the stepped clone with S1 to S3 applied, both arms read 0 reds (PINNED, the probe). The
overlay's 13 rows also read 0 reds through `check_unit_row` and `check_statement`, the two row
checks the instruction-edits reader applies (PINNED, a second probe).

### The plants (S4)

The `dead-selector` plant scopes its unit `reader.every`, so under S2 its ghost reader selects that
unit. Measured: with S2 and S3 applied and the plant unedited, it exits 0 and its second half prints
`rc=0` (PINNED). Its expectation is a declared reader that selects nothing, so S4 re-spells it with
no wildcard. With the plant re-spelled it exits 1, prints
`` `reader.ghost` is declared and selects no unit``, and its second half prints
`without reader.ghost: rc=0` (PINNED). Its two existing rows in `tools/playbook/adopt-playbook.sh`
(`tools/playbook/adopt-playbook.sh@526aeb8c:324-326`) hold as written.

The new `every-selector` plant holds what `dead-selector` held before, without its layer line:

```python
    "every-selector": (FIXTURE_UNIT_ROW + derive_fixture_row("reader", "tag_index:extract_reader", "selects"), {
        f"{FIXTURE_KIT}/readers.toml": '[[reader]]\ntag = "reader.every"\n\n[[reader]]\ntag = "reader.ghost"\n',
        "tools/corekit/instructions.toml": '[[unit]]\ntag = "unit.alpha"\nscope = ["reader.every"]\n'}),
```

Its row in the selftest's plant rows:

```text
every-selector $_tk|0|tags: green · 0 red|is declared and selects no unit
```

Under S2 it exits 0 and prints `tags: green · 0 red`. With S2's lines removed and the call left
passing `every`, it exits 1 printing `` `reader.ghost` is declared and selects no unit`` (PINNED,
both at `9b9e829df` in the clone). Wrap the `PLANTS` tuple's line under the `line length` leg.

### Other legs that read the overlay or the `repo` namespace

The close's bar over the merge was green on every other leg (the spec brief). These legs read the
overlay or the registry's `repo` row: `instruction edits (manifest checks)`,
`instruction grammar (statement types, provenance lock)`, `instruction render (one renderer of record)`,
`playbook parity`, `writing practice (records and units)`, `edges (every declared edge parses, is registered and resolves)`
and `lexicon naming predicates`. S1 moves only the `purpose-source` value, which only the tags
purpose arm reads, and S2 moves only the join. So of these, only the tags leg and the
instruction-edits reader see a change, the second through `run_tag_check`. None was run over the
clone by this writer: the scratch guard refuses each leg's command to a role agent.

### What it does not check

- An overlay unit's `help` is never graded. The row prints path-only, counted on the purpose line.
  This takes no coverage away, because no tree has graded it (section 4, "Evidence").
- Once any unit is scoped `reader.every`, no reader member reds as selecting nothing. A reader route
  that loads only the units every reader loads is read as live, which is what its load set says.
- Removing the last unit scoped `reader.every` re-arms the join on the named selectors alone. Under
  gov's tree that returns it to `unarmed`, as at HEAD.
- The rule keys on the one wildcard tag the caller passes. A second wildcard would need its own
  pass.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| the keyword parameter `every` of `check_namespace_joins` | `tools/playbook/tag_index.py` | a parameter, not a name the lexicon grades |
| the plant `every-selector` | `tools/playbook/gov_tag.py`, `tools/playbook/adopt-playbook.sh` | no cell grades a plant name |
| the fixture reader tag `reader.one` | `tools/playbook/gov_tag.py` | no cell grades a fixture tag |

No function is minted.

### Migration

None. The registry row is shipped data, and no tree has graded the field it stops asking for. The
next `--prepare` merges afresh from the run branch and runs the deployer's update over it
(`tools/push-main.sh@c7cd70b9:1015`).

### Rollout

No switch. S1 widens nothing a landed tree graded, and S2 matches the selection rule the load sets
already apply.

### Files touched (estimate)

- `tools/playbook/namespaces.toml` (S1)
- `tools/playbook/tag_index.py` (S2, S5)
- `tools/playbook/gov_tag.py` (S3, S4)
- `tools/playbook/adopt-playbook.sh` (S4)
- `help/tags.md`, `tools/playbook/README.md` (S5)

### Alternatives rejected

- **The step writes a `help` on each row.** It has no rationale to write, so the value is one
  constant across nine rows that says what `adopter-rule` already says. The rule's own text is no
  option either: `check_rationale_apart` reds a unit whose `help` is rendered in a document
  (`tools/playbook/writing_practice.py@c129baaa:304-310`), and that leg reads the overlay's units
  (`tools/playbook/writing_practice.py@c129baaa:129-131`).
- **The join arms on kit units' selectors only.** The overlay's selections are real ones, so this
  hides them, and gov's join would print `unarmed` for good.
- **Retiring `reader.driver` and `reader.subagent`.** Each is a load route a document or a role can
  select, and both are selected by every unit scoped `reader.every`. Retiring them adds change
  records and help edits and leaves the join's disagreement with the load sets in place.
- **`tag_index` imports `EVERY` itself.** Its import closure would grow from 7 modules to 28
  (PINNED, `derive_module_closure` over both modules at `9b9e829df`), so an edit to any of 21 more
  modules would re-parse every blob its extractors read. The caller already holds the module.

## 5. Production-readiness checklist

- security — No write path and no input boundary. Both changes sit inside read-only checks.
- perf / scale — One dict built per armed `selects` namespace whose selectors hold the wildcard.
- error / empty / loading states — With no overlay the `repo` row prints `pending`, as before. With
  no unit scoped by a reader the join prints `unarmed`, as before.
- observability — The purpose summary counts `repo` among the path-only rows. The join prints no new
  line.
- risks — The probes called the two arms on scratch clones, not the whole leg. The main loop's
  `--prepare` and close are the observation over the real walk (section 7).
- testing — AC3 and AC4 are the resolver's own plants. AC1 and AC2 are the main loop's runs of the
  two legs over a stepped clone.
- migration — None (section 4, "Migration").
- user docs — `help/tags.md`'s join item (S5).

## 6. Acceptance criteria

The commands of AC1 and AC2 run in a throwaway clone of the pass's tip. The clone keeps its history,
has a local `main` at `origin/main`, and has `origin/HEAD` set by `git remote set-head origin main`.
In it, `python tools/govkit/steps/adopter_rules_to_overlay.py up .` runs first and its output is
committed. No one runs them in the run's worktree.

- **AC1** — When `python tools/playbook/gov_tag.py check` runs in that clone, it exits 0, prints
  `tags: green · 0 red` and `tags: purpose · 7 graded over 131 members, 3 path-only, pending 0`, and
  prints no line holding `lacks help` or `is declared and selects no unit`.
  Red when: the base code reads 9 purpose reds naming `repo.rule-` and 2 join reds naming
  `reader.driver` and `reader.subagent`, as the merge's log does.
  figure: PINNED, the two arms by probe over clones at `9b9e829df`, 11 reds before and 0 after; the
  leg's other arms were green over the merge (the spec brief).
  permission: the main loop runs the check; a role agent's scratch guard refuses this leg's command.
- **AC2** — When `python tools/playbook/instructions_edit.py check` runs in that clone, it exits 0 and
  ends `instructions-edit: check · 13 row(s)` then `instructions-edit: check · 0 red`.
  Red when: the tag reds of AC1 reach it through its tag check.
  figure: PINNED, the overlay's rows through the two row checks at 0 red; the tag part is AC1's.
  permission: the main loop runs the check; a role agent's scratch guard refuses this leg's command.
- **AC3** — When `python tools/playbook/gov_tag.py --fixture --plant every-selector --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new`
  runs after the build, it exits 0, prints `tags: green · 0 red`, and prints no line holding
  `is declared and selects no unit`.
  Red when: S2 is absent, so the plant exits 1 printing `` `reader.ghost` is declared and selects no unit``.
  figure: PINNED, the plant over the clone at `9b9e829df` with and without S2's lines.
- **AC4** — When `python tools/playbook/gov_tag.py --fixture --plant dead-selector --set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new`
  runs after the build, it exits 1, prints `` `reader.ghost` is declared and selects no unit``, and
  prints `without reader.ghost: rc=0`.
  Red when: the plant still scopes its unit `reader.every`, so under S2 it exits 0.
  figure: PINNED, the plant over the clone at `9b9e829df`, unedited and re-spelled.
- **AC5** — When `git grep -l "every reader loads" -- help/tags.md tools/playbook/README.md tools/playbook/tag_index.py`
  runs after the build, it lists all three files.
  Red when: a prose reader of the join does not say the wildcard's rule.
- **AC6** — When `python tools/playbook/gov_tag.py check` runs over the pass's own tree, which holds
  no overlay, it exits 0 and prints a line opening `tags: purpose · pending repo`.
  Red when: S1 breaks the registry row, so the check refuses it with exit 2.
  permission: the main loop runs the check at the close.

## 7. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `line length` · `docs` · `spec tokens (a spec's own names resolve)`

The guarded legs the estimated paths trip are `govkit acceptance matrix` and
`playbook render selftest` (DERIVED, the spec-token checker's `--legs-for` over the estimate at
`9b9e829df`, broad guards set aside; `help/tags.md` trips none). The rest carry no guard and run on
every change. The tags leg is the one that red. The instruction-edits leg carries its reds. The
lexicon leg reads the registry's words, and `docs` grades the help page.

After this unit lands on the run branch, the main loop re-runs
`bash tools/push-main.sh --prepare --slug dOrderedCharter` and then the close's bar over the new
prepared merge. That bar is where AC1's leg first reads gov's own walked overlay.

New arm: tools/playbook/gov_tag.py · covers AC3 AC4 · the `every-selector` plant, which the join before S2 reds as `reader.ghost` selecting no unit, and its row in the plant rows of tools/playbook/adopt-playbook.sh · none

## 8. Open questions

- **F1 — Where does the `repo` purpose fix live?** The arm asks each overlay unit for `help`, and no
  writer of an overlay unit supplies one.
  - (a) The registry's `repo` row reads its purpose path-only, `.governance/instructions.toml`. One
    line of shipped data, so it holds for every adopter, and it removes no grade any tree has run.
    This is the recommendation.
  - (b) The step writes a `help` on each row. It has no rationale to write, so the value is one
    constant, and hand-written overlay units still red.
  - (c) The arm reads an `adopter-rule` row's purpose from its `text`. That puts statement-type
    knowledge into a namespace-generic arm, and the text is not a rationale.

  RESOLVED (agent, 2026-11-12, delegated): (a), under the owner's standing ruling of 2026-11-10 to
  take each fork's recommendation.
- **F2 — Where does the reader join fix live?** The join reds two readers that the load sets say
  select every unit scoped `reader.every`.
  - (a) The join counts a unit scoped `reader.every` as selected by every declared reader, the
    wildcard passed in by the caller. The join then agrees with the load sets for every adopter.
    This is the recommendation.
  - (b) The selecting direction arms on kit units' selectors only. It hides real selections, and
    gov's join stays `unarmed` for good.
  - (c) `reader.driver` and `reader.subagent` are retired. Each is a live load route, and the
    join's disagreement with the load sets stays.

  RESOLVED (agent, 2026-11-12, delegated): (a), under the owner's standing ruling of 2026-11-10 to
  take each fork's recommendation.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft, from
  `2026-11-12-prompt-PLAY-dOrderedCharter-88-1-spec-writer.md`. The 11 reds were reproduced on a
  scratch clone of `9b9e829df` by a probe of the two arms. F1 and F2 were resolved under the owner's
  standing ruling.

## 10. Reuse audit

This unit extends existing seams and adds no mechanism. S1 uses the path-only form the purpose arm
already reads (`tools/playbook/tag_index.py@243b435f:1251-1253`). S2 adds two lines to the one join,
`check_namespace_joins`, and takes the wildcard from its one spelling, `EVERY` in
`tools/playbook/instruction_units.py@6e7d4f51:191`, which the selection reader uses. The plant joins
`SHAPE_PLANTS` beside `dead-selector`. `tools/codebase-map/reuse_lookup.py` ranked
`read_namespaces` in `tools/playbook/tag_index.py`, the registry's reader, which S1's row passes
through unchanged, and `parse_unit_rows` in `tools/playbook/instruction_units.py`, the unit rows'
reader, which this unit does not touch. The rest it ranked were generic readers in other kits. No
other seam fits: the join and the purpose arm each have one home, read above.

Recall terms used: `reuse_lookup.py "a selects namespace join counts a wildcard reader selector, and a namespace purpose source reads path-only"` and `reuse_lookup.py "check_namespace_joins selector reader.every derive_unit_selection load set purpose-source path-only"`
