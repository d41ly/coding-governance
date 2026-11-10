# PLAY-dOrderedCharter-76 — the units reference page, each page's unit line and its check, the unit-usage class, and the reds PLAY-dOrderedCharter-37's pass left

**Status:** CLOSED · rev-1 · 2026-11-10 · node a · Tier-2 · base f66d97aea · streams playbook · order 37 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 |
| [2026-11-10-build-PLAY-dOrderedCharter-76-1-builder-return.md](../build/2026-11-10-build-PLAY-dOrderedCharter-76-1-builder-return.md) | journal | — |
| [2026-11-10-build-PLAY-dOrderedCharter-76-ledger.md](../build/2026-11-10-build-PLAY-dOrderedCharter-76-ledger.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-76-1-spec-writer.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-76-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-76-build-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-76-build-brief.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-76-spec-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-76-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

PLAY-dOrderedCharter-37's pass, built at `19648821f`, rendered three reference pages and left its
later commit to land once PLAY-dOrderedCharter-40's unit rows were tracked (that spec's section 8 F8,
F10 and F11). The rows are tracked since `c91c26904`, and PLAY-dOrderedCharter-37 is CLOSED, so its
text is frozen and that later commit is this unit. It lands the units reference page, a unit line on
every reference, concept and task page with the docs leg's check over them, and the `unit-usage`
class in the step gate's registry and the docs leg's rows, so every user-facing unit is documented
from the row that defines it (P42).

It also clears what the main loop found after PLAY-dOrderedCharter-37's pass: the core meta-check and
the layers check each red on that pass's work, the `unit-usage` plant stages nothing on a CRLF
checkout, and `help/step-gate.md` lists none of the four classes this build added. No pass reopens
PLAY-dOrderedCharter-37.

## 2. Scope (IN)

- **S1** — The reference declaration's later rows. `tools/playbook/references.toml` gains the units
  row, `registry` `doc.reference.units`, its `h1`, `reader`
  `{prefix}/playbook/render_playbook.py:read_unit_reference_rows` and `page`
  `help/reference/units.md`. Every row gains a `unit`, the instruction unit its page documents: the
  policy row `unit.policy-schema`, the drive row `unit.drive-table`, the kinds row
  `unit.kinds-register` and the units row `unit.unit-registry`. The `h1` is owed because the `doc`
  namespace's purpose arm reads each `[[reference]]` row's `h1` (PLAY-dOrderedCharter-40's section 8
  F4). The file's header comment names the `unit` key. Observed by AC2.
- **S2** — The units page, rendered. `python tools/playbook/render_playbook.py --reference` writes
  the four declared pages, the units page new and each page carrying its row's unit line, which
  `tools/playbook/render_playbook.py#render_reference_page` already writes from a row's `unit`. A
  rendered summary escapes `<`, `>` and `&`, so a placeholder such as `<prefix>` in a unit's `text`
  or `<name>` in a kind's summary shows on the page rather than reading as an HTML tag (section 8 F6).
  Observed by AC1.
- **S3** — The `unit-usage` class. `tools/govkit/surface-classes.toml` gains its `[[class]]` row,
  reader `read_unit_usage_members`, plant `write_unit_usage_plant` and witness
  `{prefix}/playbook/pins.py:read_change_successors`, each landed in
  `tools/playbook/render_playbook.py` or `tools/playbook/pins.py` already. `tools/govkit/usage.toml`
  gains its `[[class]]` row, usage `synopsis`, `rows` `read_unit_reference_rows`, the units page's
  own reader. Both rows and the units page land in one commit, so no member of the class is ever
  unanchored (PLAY-dOrderedCharter-37's section 8 F8). Observed by AC4.
- **S4** — One row removal for both unit plants. `tools/playbook/instruction_units.py` gains
  `remove_unit_row(root, unit)`: it reads the unit's manifest as bytes, finds the same row through
  `tools/playbook/instruction_units.py#parse_unit_rows` over those bytes, so its body is in the
  file's own line endings, takes it out, writes the file and stages it, and raises a `ValueError`
  naming the tag and the manifest where the bytes hold no such row.
  `tools/playbook/pins.py#write_unit_plant` and
  `tools/playbook/render_playbook.py#write_unit_usage_plant` each call it instead of matching the
  body themselves (section 8 F3). The instruction units fixture gains the plant `row-removal`.
  Observed by AC4 and AC5.
- **S5** — The unit-line check. `tools/govkit/docs_leg.py` gains `check_unit_lines`, run from
  `tools/govkit/docs_leg.py#read_docs_state`. It reads each `<!-- unit: <tag> -->` line outside a
  fence on every page under `help/`, through `tools/govkit/docs_leg.py#read_page_lines`. Three
  findings: `UNIT`, a line whose tag is no member of the `unit` class (section 8 F4); `UNLINKED`, a
  page under `help/reference/`, `help/concepts/` or `help/tasks/` with no unit line; `UNPAGED`, a
  `unit-usage` member whose tag no resolved line names. The check arms when the `unit-usage` class
  is registered. The summary line ends `· unit lines <n> resolved`, or `· unit lines unarmed` while
  it is not. The leg's fixture gains the plant `unit-lines`, and the govkit selftest's docs cases
  gain its rows. Observed by AC3.
- **S6** — The authored pages. `help/concepts/instruction-layer.md` and
  `help/tasks/change-a-gov-rule.md` each open with `<!-- unit: unit.unit-registry -->`, and the
  concept page links the units page beside the three it links. `help/README.md` gains the units
  page's index line. `help/docs-leg.md` documents the unit line, its three findings and the
  `unit-lines` plant. Observed by AC3 and AC8.
- **S7** — The two help legs enforce P42. In `tools/gate-legs.json`, `help reference pages` and
  `help page commands` each gain `enforces: ["principle.p42"]`, and the commit deletes the now-stale
  `principle.p42` row from `tools/playbook/core-pending.txt`, as PLAY-dOrderedCharter-20's pass did for
  `principle.p11` at `0bbaaa17d` (section 8 F1). Observed by AC6.
  **Readers:** by name: `tools/playbook/principles.toml`, whose registry row holds the tag and stays,
  and `tools/gate-legs.json`, whose two rows name it after this commit · by value:
  `tools/playbook/core.py#run_meta_check`, which reads the row through `read_pending`, counts it on
  its `pending ·` line and reds it as stale once a leg enforces its principle; no check compares
  that count, the two `pending · principle` strings in `tools/playbook/core.py` being its own
  fixture's (a grep at f66d97aea).
- **S8** — The renderer's edge into govkit, declared. `tools/playbook/kit.toml`'s `optional` list
  gains a row for `render_playbook.py` at `point.runtime.install-target`, the point
  `tools/policy/kit.toml` declares for the policy kit's own edge into govkit, its fallback that
  `--reference` refuses naming the absent docs leg (section 8 F2). Observed by AC7.
- **S9** — The step gate's page, current. `help/step-gate.md` stops typing its class table: it
  points at `python tools/govkit/step_gate.py --list`, which prints each registered class with its
  member count and summary, and at `tools/govkit/surface-classes.toml`, keeping its sentence on how
  a member is spelled. Its opening sentence names the vanishing members by example rather than as a
  closed list (section 8 F5). Observed by AC9.

## 3. Non-goals (OUT)

- What PLAY-dOrderedCharter-37's pass landed: the three reference pages' content, the run arm, the
  `drive` and `kind` classes, the authored pages' text beyond S6, and the two leg rows' argv.
- The two help legs' rows in `tools/run-gates/ceiling-evidence.txt`, owed at PLAY-dOrderedCharter-37's
  close from measured runs (its builder return).
- Any change to the four unit rows in `tools/playbook/instructions.toml`, their `scope` or their
  `text`: PLAY-dOrderedCharter-40's, and its section 8 F2.
- `tools/playbook/instructions_edit.py#derive_candidate`'s own row match: it parses the manifest's
  bytes it then rewrites, so its body is already in the file's line endings (section 8 F3).
- Whether a tag on a unit line is the right unit for its page, and the back links
  TOOL-dTotalRecall-26 S9 specs over the same `<!-- unit: <tag> -->` lines.
- Any edit to the text of PLAY-dOrderedCharter-37, PLAY-dOrderedCharter-40 or
  PLAY-dOrderedCharter-33, each CLOSED.

This unit rests on three CLOSED units it does not declare as edges. A consumes-from edge into a CLOSED
spec reds memory hygiene's edge check unless that spec declares a hands-off back, and a CLOSED spec's
text is frozen, so each dependency is named here, as PLAY-dOrderedCharter-75 names its own.
PLAY-dOrderedCharter-37 built the render, the docs leg's `synopsis` shape, the reader and plant S3
registers, and the two legs S7 changes; without them S1 to S3 have nothing to declare.
PLAY-dOrderedCharter-40 tracked the four unit rows and the reference rows' `h1`; without them the
units page is an empty population the render refuses and no unit line resolves.
PLAY-dOrderedCharter-33 built the witness S3 registers, and its later commit `4dd011712`
registered the `unit` class S5 resolves against and fixed the CRLF match S4 shares. PLAY-dOrderedCharter-37 declares a hands-off to
PLAY-dOrderedCharter-55 for its AC1 four-page half, AC8 and AC10's `unit-usage` half; this unit
observes those as its AC1, AC3 and AC4.

### Edges

none

## 4. Design

### Evidence

Read at `f66d97aea`.

- `tools/playbook/references.toml` holds three `[[reference]]` rows, each with an `h1` and none with
  a `unit`. `tools/playbook/instructions.toml` holds four `[[unit]]` rows, each carrying a `usage`,
  the first `unit.policy-schema` (PINNED, counted then).
- `tools/playbook/render_playbook.py#render_reference_page` writes `<!-- unit: <tag> -->` where a
  row has a `unit`, and the summary as written, so `help/reference/kinds.md` already shows
  `skills/<name>/` in prose, where a Markdown viewer reads `<name>` as a tag. It is the one prose
  line on the three pages holding `<`, `>` or `&` (PINNED, a scan of the pages' unfenced lines).
- `tools/playbook/render_playbook.py#write_unit_usage_plant` takes its row out with
  `replace(u.body, '', 1)` over the file's bytes. `tools/playbook/instruction_units.py#read_unit_rows`
  reads a manifest with universal newlines, so `u.body` holds LF, and the step gate's fixture clone
  checks out CRLF under `core.autocrlf`; PLAY-dOrderedCharter-33's deviation 336 observed the same
  defect stage nothing in `tools/playbook/pins.py#write_unit_plant` and fixed it there with a
  `\n` to `\r\n` swap. `tools/playbook/instruction_units.py#parse_unit_rows` cuts each body from the
  text it is handed, so over the file's own bytes a body keeps the file's line endings.
- `tools/gate-legs.json`'s rows `help reference pages` and `help page commands` carry no `enforces`
  and no `guard`, and `tools/playbook/core-pending.txt` holds no `leg` row for either and a
  `principle.p42` row armed by dGroundRules. `tools/playbook/core.py#run_meta_check` reds a leg named
  by no `enforces` and no pending row, and reds a pending row whose item a leg enforces. P42's row in
  `tools/playbook/principles.toml` lists `cl-dClosedLoop-0067` among its clauses, the clause
  PLAY-dOrderedCharter-37 carries whole, whose checks the two legs are.
- `tools/playbook/render_playbook.py#read_fingerprint_lines` calls
  `resolve_kit_dir('govkit', 'docs_leg.py', engine_dir)`, a `probe` edge in the layers check's terms
  (`tools/playbook/check_layers.py`, its docstring). `govkit` is a `homes` entry of the expansion row
  `layer.distribution` in `tools/playbook/layers.toml`, and `tools/playbook/kit.toml`, layer
  `layer.instruction`, a core row, lists one `optional` row, for `gov_tag.py`. The policy kit, the same
  layer, lists `policy.py` and `check_policy.py` at `point.runtime.install-target`, which the core row
  `layer.runtime` declares.
- `help/step-gate.md` types a nine-row class table, `file` to `entry`.
  `tools/govkit/surface-classes.toml` holds twelve rows, the nine and `drive`, `kind` and `unit`
  (PINNED, counted then), and this unit adds `unit-usage`. `tools/govkit/step_gate.py#main`'s
  `--list` prints `step-gate: <id> · <n> members · <summary>` per row.
- Readers of what this unit retires or moves (PINNED, `git grep` outside the builds folder at
  `f66d97aea`): `principle.p42` is spelled by `tools/playbook/principles.toml` and
  `tools/playbook/core-pending.txt` only; `step-gate.md` is spelled by two links, in
  `help/README.md` and `help/docs-leg.md`, and no tool parses the page's table; `u.body` is spelled
  in the two plants named above.

### Data model

```toml
# tools/playbook/references.toml, the new row; each of the three landed rows gains its `unit` line
[[reference]]
registry = "doc.reference.units"
h1 = "The unit registry's reference page, one section per instruction unit carrying a usage"
reader = "{prefix}/playbook/render_playbook.py:read_unit_reference_rows"
page = "help/reference/units.md"
unit = "unit.unit-registry"
```

```toml
# tools/govkit/surface-classes.toml
[[class]]
id = "unit-usage"
reader = "{prefix}/playbook/render_playbook.py:read_unit_usage_members"
plant = "{prefix}/playbook/render_playbook.py:write_unit_usage_plant"
summary = "each gov instruction unit carrying a usage, by its tag, the units help/reference/units.md documents"
witness = "{prefix}/playbook/pins.py:read_change_successors"

# tools/govkit/usage.toml
[[class]]
class = "unit-usage"
usage = "synopsis"
rows = "{prefix}/playbook/render_playbook.py:read_unit_reference_rows"
why = "a unit carrying a usage is its text and its usage, which its instructions.toml row states; help/reference/units.md renders them"
```

```toml
# tools/playbook/kit.toml, the second optional row
{ part = "render_playbook.py", point = "point.runtime.install-target", fallback = "--reference refuses naming the absent docs leg; the reference pages are gov's own" },
```

```json
"enforces": ["principle.p42"]
```

### The shared row removal

```python
# tools/playbook/instruction_units.py
def remove_unit_row(root, unit) -> None:
    """`unit`'s row taken out of its manifest under `root`, matched in the file's own bytes, and staged."""
    path = pathlib.Path(root) / unit.path
    text = path.read_bytes().decode("utf-8")
    held = [u for u in parse_unit_rows(text, unit.path)[0] if u.index == unit.index and u.tag == unit.tag]
    if not held:
        raise ValueError(f"{unit.path} holds no row {unit.tag} in its bytes")
    path.write_bytes(text.replace(held[0].body, "", 1).encode("utf-8"))
    run_git(root, "add", "--", unit.path)
```

Each plant keeps its own choice of row and its member id, and calls the helper for the bytes:
`write_unit_plant` passes the clone's first unit, `write_unit_usage_plant` the first carrying a
`usage`. The `row-removal` arm writes a two-row manifest in CRLF bytes, takes the first row out
through the helper, checks the second row's bytes intact and the first tag absent, then hands it a
unit whose row the bytes no longer hold and checks the `ValueError` names its tag.

### The unit-line check

```python
# tools/govkit/docs_leg.py
UNIT_LINE_RE = re.compile(r"^\s*<!--\s*unit:\s*(?P<tag>\S+)\s*-->\s*$")
UNIT_PAGE_DIRS = ("help/reference/", "help/concepts/", "help/tasks/")

def check_unit_lines(root, pages, class_ids, population) -> tuple:
    """(resolved lines, or None while `unit-usage` is unregistered; findings; non-verdict states)"""
```

A line resolves when `unit:<tag>` is in the population the leg already holds, which the `unit`
class's reader fills with every gov unit tag (`tools/playbook/pins.py#read_unit_members`). With
`unit-usage` registered and `unit` not, nothing can resolve, so the check adds the state `class
unit-usage is registered and class unit is not, so no unit line can resolve`, and the leg exits 2.
The findings print under `help.enforce` as the leg's others do:

```
docs: UNIT help/concepts/fx.md:1 unit.nowhere: names no gov unit
docs: UNLINKED help/tasks/fx.md: a page under help/reference/, help/concepts/ or help/tasks/ with no unit line
docs: UNPAGED unit-usage:unit.fx: no page's unit line names it
```

The new field goes last on the summary line, so the selftest's `none` row, which reads the line up
to its `commands` count, still matches. The `unit-lines` plant registers `unit` and `unit-usage` in
the fixture's class list, each a `none` class row in its `usage.toml`, adds `unit:unit.fx` and
`unit-usage:unit.fx` to its population, and writes `help/concepts/fx.md` opening with a line naming
`unit.nowhere` and `help/tasks/fx.md` with none. One plant reds all three findings. The selftest's
`_docs_cases` in `tools/govkit/selftest.py` gains three rows on it, exit 1, one per finding.
PLAY-dOrderedCharter-37's spec named this plant `unresolved-unit`; it was never built, and the new
name says it plants all three.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `remove_unit_row`, `arm_row_removal` and the plant `row-removal` | `tools/playbook/instruction_units.py` | the lexicon's `py.function` predicate, each `OK` at design |
| `check_unit_lines`, `UNIT_LINE_RE`, `UNIT_PAGE_DIRS`, the plant `unit-lines`, the findings `UNIT`, `UNLINKED` and `UNPAGED` | `tools/govkit/docs_leg.py` | the lexicon's `py.function` predicate for the function; no cell declares constants |
| the class id `unit-usage` | `tools/govkit/surface-classes.toml`, `tools/govkit/usage.toml` | the step gate's class-row refusals and the docs leg's `CLASS` finding |
| the tag `doc.reference.units`, its `h1`, and the `unit` key on four rows | `tools/playbook/references.toml` | the tag shape check and the `doc` namespace's purpose arm |
| the page `help/reference/units.md` | `help/` | the render's orphan refusal |

### Files touched (estimate)

- `tools/playbook/references.toml` (the units row, four `unit` keys, the header comment)
- `tools/playbook/render_playbook.py` (the summary escape, the plant's call to the helper)
- `tools/playbook/instruction_units.py` (`remove_unit_row` and its fixture arm)
- `tools/playbook/pins.py` (the plant's call to the helper)
- `tools/playbook/kit.toml` (the optional row)
- `tools/playbook/core-pending.txt` (the `principle.p42` row)
- `tools/gate-legs.json` (two `enforces`)
- `tools/govkit/surface-classes.toml`
- `tools/govkit/usage.toml`
- `tools/govkit/docs_leg.py` (the check and its plant)
- `tools/govkit/selftest.py` (three docs cases)
- `help/reference/units.md` (new, rendered), `help/reference/kinds.md` (re-rendered, the escape)
- `help/concepts/instruction-layer.md`, `help/tasks/change-a-gov-rule.md`, `help/README.md`
- `help/docs-leg.md`, `help/step-gate.md`

### Rollout

Live at landing, order 37, after PLAY-dOrderedCharter-40 and PLAY-dOrderedCharter-33's later commit,
in one pass commit. Within it: the helper and the two plants first; then both class rows; then the
reference rows and the escape, and `--reference`, which reads the new class's fingerprints from the
docs leg; then the unit-line check and the pages' unit lines; then the leg rows, the pending row and
the optional row. No member of `unit-usage` is unanchored at any commit, and no docs-undocumented row
is written for one.

### Alternatives rejected

| Option | Why not |
|---|---|
| Reopen PLAY-dOrderedCharter-37 for its later commit | A CLOSED spec is frozen; moving it live made the spec-token check red its AC12 at `--dispatch` |
| A `leg` pending row for each help leg | Grows a list its header declares shrink-only, and names an arming build for a leg that already checks its clause (section 8 F1) |
| A second copy of the CRLF swap in the `unit-usage` plant | The copy the reuse rule refuses at a kind's second instance (section 8 F3) |
| Four typed rows added to the step gate page's table | A typed inventory beside the registry that owns it, stale again at the next class (section 8 F5) |

## 5. Production-readiness checklist

- security: N/A — no new write path or input boundary; the helper writes only the scratch clone a
  step gate fixture hands a plant, and the escape narrows what a rendered page passes to a viewer.
- perf / scale: one more reference page and one more class reader, each over four rows; the
  unit-line check reads lines of pages the leg already reads and runs no child process (section 8
  F4).
- error / empty / loading states: the check prints `unit lines unarmed` while `unit-usage` is
  unregistered, and refuses, exit 2, when `unit-usage` is registered without `unit`. What it does not
  check: whether a line names the unit its page documents; a unit line inside a fence; a page outside
  the three folders, the tutorial and the root pages among them. What the layers check no longer sees
  after S8: any later edge from `tools/playbook/render_playbook.py` into a non-core kit, since an
  optional row allows every edge of its file, as it does for `policy.py`. What the core meta-check
  does not see after S7: which of P42's clauses a leg checks; it counts the principle enforced once
  any leg names it.
- observability: the docs leg's summary line counts resolved unit lines, and each finding names the
  page and line or the member.
- risks: from this commit a unit row carrying a `usage` that vanishes reds the step gate under two
  classes, `unit` and `unit-usage`, until a change record or a step row witnesses it.
  PLAY-dOrderedCharter-33's `unit` plant now reds both members, and `--with-row` names every redded
  member, so its case holds.
  The escape re-renders `help/reference/kinds.md`, whose anchors do not move, the fingerprint being
  the row's and not the page's.
- testing: AC1 to AC9, each a direct command, a fixture plant or a grep; the suite arms on the
  `New arm:` lines in section 7.
- migration: additive; rows and keys added, one pending row deleted from a shrink-only list, one
  page rendered, two re-rendered or edited.
- user docs: the units page, `help/docs-leg.md` for the unit line and its findings, and
  `help/step-gate.md` (S6, S9).

## 6. Acceptance criteria

Each planted case runs in a fresh scratch clone of the repository, `git clone -q --shared . <tmp>`,
with that clone's own tools.

- **AC1** — When `python tools/playbook/render_playbook.py --reference --check` runs after the pass,
  it exits 0 printing `render-playbook: reference · 4 page(s) checked · 0 drifted`; in a scratch
  clone whose `tools/playbook/instructions.toml` has one row's `usage` edited, the clone's own
  `python tools/playbook/render_playbook.py --reference --check` exits 1 printing a `DRIFT` line
  naming the units page. Over the tree, `git grep -n "skills/&lt;name&gt;/" -- help/reference/kinds.md`
  finds one line and `git grep -c "&lt;prefix&gt;" -- help/reference` counts two on the units page.
  Red when: the units page drifts from its rows and the check passes, or a summary's placeholder is
  written as a bare tag.
  figure: PINNED, four declared pages, and two unit texts spelling `<prefix>`, counted at f66d97aea.
- **AC2** — When `git grep -c "^unit = " -- tools/playbook/references.toml` and
  `git grep -c "^h1 = " -- tools/playbook/references.toml` run after the pass, each counts 4; and
  `python tools/playbook/gov_tag.py show doc.reference.units` exits 0 naming the declaration's row.
  Red when: a reference row carries no `unit`, or the units row carries no `h1` and the tags leg's
  purpose arm reds its tag.
  permission: where the builder's role may not run the tag resolver, the main loop observes it at
  the close.
- **AC3** — When `python tools/govkit/docs_leg.py` runs after the pass, its summary line ends
  `unit lines <n> resolved` with `<n>` at least 6, and it prints no `UNIT`, `UNLINKED`, `UNPAGED` or
  `UNDOCUMENTED` line and no line naming a `unit-usage:` member; and
  `python tools/govkit/docs_leg.py --fixture --plant unit-lines` exits 1 printing a `UNIT` line
  naming `unit.nowhere`, an `UNLINKED` line naming the fixture's task page and an `UNPAGED` line
  naming `unit-usage:unit.fx`, while `python tools/govkit/docs_leg.py --fixture --plant none` prints
  `unit lines unarmed`.
  Red when: a page links no unit, a user-facing unit has no page, an unresolved line passes, or the
  check grades an unregistered class and reads green.
  figure: PINNED floor, six lines at design: the four reference pages, the concept page and the task
  page; the count DERIVED at observation.
- **AC4** — When `python tools/govkit/step_gate.py --list` runs after the pass, it prints
  `step-gate: unit-usage · 4 members`; `python tools/govkit/step_gate.py --fixture --plant unit-usage`
  exits 1 printing `step-gate: RED unit-usage:unit.policy-schema vanished`, and with `--with-row`
  exits 0; and `python tools/govkit/docs_leg.py` prints no `CLASS` line.
  Red when: the plant stages nothing on a CRLF checkout and the fixture reads nothing vanished, or a
  class row lands without its partner row.
  figure: PINNED, four unit rows each carrying a usage at f66d97aea, the first `unit.policy-schema`.
- **AC5** — When `python tools/playbook/instruction_units.py fixture --plant row-removal` runs after
  the pass, it exits 0 with every expectation `ok`: a CRLF manifest's first row taken out, its second
  row's bytes intact, and a `ValueError` naming the tag of a row the bytes no longer hold. And
  `git grep -nF "u.body" -- tools/playbook/render_playbook.py tools/playbook/pins.py` prints nothing
  while `git grep -n "remove_unit_row" -- tools/playbook/render_playbook.py tools/playbook/pins.py`
  prints a line in each file.
  Red when: either plant keeps its own body match, or the helper matches nothing in CRLF bytes.
- **AC6** — When `git grep -n "principle.p42" -- tools/playbook/core-pending.txt` runs after the pass,
  it prints nothing, and `git grep -c "principle.p42" -- tools/gate-legs.json` counts 2; and
  `python tools/playbook/core.py meta-check` prints no line naming `help reference pages`,
  `help page commands` or `principle.p42`.
  Red when: either leg carries no `enforces` and no pending row, or the `principle.p42` row stays
  once a leg enforces it.
  permission: the builder's role may not run the meta-check (PLAY-dOrderedCharter-33's later-commit
  return), so the main loop observes it at the close.
- **AC7** — When `python tools/playbook/check_layers.py --list` runs after the pass, its `edge` line
  for the `probe` from `tools/playbook/render_playbook.py` into `govkit` ends `allowed`, and
  `python tools/playbook/check_layers.py` prints no `RED` line naming that file.
  Red when: no optional row of the renderer's descriptor names the file, and the edge stays red.
  permission: as AC6, the main loop observes it at the close where the builder's role may not.
- **AC8** — When `git grep -c "<!-- unit: unit.unit-registry -->" -- help/concepts help/tasks` runs
  after the pass, it counts one line on each of the two pages;
  `git grep -n "units.md" -- help/README.md help/concepts/instruction-layer.md` finds the index line
  and the concept page's link; and `git grep -n "UNLINKED" -- help/docs-leg.md` finds the page's
  list of what the leg reds.
  Red when: an authored page ships with no unit line, the units page is unlinked, or the leg's page
  does not document the new findings.
- **AC9** — When `git grep -n "step_gate.py --list" -- help/step-gate.md` runs after the pass, it finds
  the page's pointer to the class list, and `git grep -n "^| Class |" -- help/step-gate.md` prints
  nothing; `python tools/govkit/step_gate.py --list` prints a line for each of `unit`, `drive`,
  `kind` and `unit-usage`.
  Red when: the page types a class inventory beside the registry, or points at nothing that lists
  the classes.

## 7. Gates

`docs` · `step-gate` · `help reference pages` · `help page commands` · `core meta-check` · `layer dependencies (the core never depends on an expansion)` · `tags (the resolver's checks)` · `instruction units selftest` · `playbook render selftest` · `playbook render wiring` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The core meta-check and the layers check are red at `f66d97aea` on PLAY-dOrderedCharter-37's pass, as
section 1 says; the main loop observes both green at the close (AC6, AC7). The
`govkit acceptance matrix` leg is recorded red at HEAD for the renderer's dependency that
PLAY-dOrderedCharter-73 parked for the owner, as PLAY-dOrderedCharter-75's gates section records; this
unit adds no import-time edge to it. The guarded legs on the line are the ones the files touched trip:
`policy fixtures` for the renderer and its descriptor, the govkit legs and `recall floor arms` for
`tools/govkit/`, and the run-gates and `measure-legs selftest` legs for `tools/gate-legs.json`.

New arm: tools/govkit/selftest.py · covers AC3 AC4 · `_docs_cases` gains three `unit-lines` rows, red before `check_unit_lines` lands; `check_step_gate_fixture` derives a `unit-usage` case from the new class row, red with the row registered and `write_unit_usage_plant` still matching LF bytes, which on a CRLF fixture clone stages nothing · none
New arm: tools/playbook/instruction_units.py · covers AC5 · the fixture plant `row-removal`, red before `remove_unit_row` exists · none

## 8. Open questions

- **F1 — How the two help legs meet the core meta-check.** Re-read at `f66d97aea`, neither leg
  carries `enforces` and neither has a pending row, so the meta-check reds both (section 4 Evidence).
  Options: (a) both legs `enforces: ["principle.p42"]`, and the `principle.p42` pending row deleted,
  which the meta-check otherwise reds as stale; (b) a `leg` pending row for each, armed by
  dWitnessedBar as the list's other `leg` rows are; (c) (a) for `help reference pages` only, (b) for
  `help page commands`. (b) and (c) grow a list whose header declares it shrink-only, a follow-up row
  each to drain, for legs that already check a clause of P42: `cl-dClosedLoop-0067` is one of P42's
  clauses in `tools/playbook/principles.toml`, and PLAY-dOrderedCharter-37 carries it whole, its
  rendered pages and every shown command run. (a) leaves no row to drain, and repeats
  PLAY-dOrderedCharter-20's step for p11 at `0bbaaa17d`. What (a) does not check is in section 5.
  RESOLVED (agent, 2026-11-10, delegated): (a), the most feature-rich, no follow-up left. widens:
  none · relaxes: none
- **F2 — How the renderer's probe of the docs leg meets the layers check.** Re-read at `f66d97aea`,
  core kit `playbook-render` probes expansion home `govkit` in
  `tools/playbook/render_playbook.py#read_fingerprint_lines`, and no optional row names the file.
  Options: (a) an optional row for `render_playbook.py` at `point.runtime.install-target`, the point
  the policy kit, the same layer, takes for its own edge into govkit; (b) the probe moved into a new
  module of its own and the optional row naming that module, so the grant covers one function; (c)
  a new point declared on `layer.instruction` in `tools/playbook/layers.toml`; (d) the render reading
  fingerprints from a file the docs leg writes, a generated artifact. (c) changes the layer register,
  a governance carrier, the build method's second veto; (d) is a new generated artifact, a unit of its
  own by the build method's M2, and a second copy of what `--fingerprints` prints. (a) and (b) both
  meet AC7. (b) narrows the grant but adds a module for one function, where every optional row in the
  tree names a whole file; (a) is one row in the descriptor's own grammar and reuses the policy kit's
  seam, and section 5 states what it stops the layers check seeing. RESOLVED (agent, 2026-11-10,
  delegated): (a), by the tie-break, fewer open questions and then reuse of a seam. widens: none ·
  relaxes: the layers check's reading of `tools/playbook/render_playbook.py`, from every non-core edge
  graded to every such edge allowed
- **F3 — Where the shared row removal lives, and how it matches.** Two plants take a unit row out of
  its manifest: `tools/playbook/pins.py#write_unit_plant`, fixed for CRLF by a `\n` swap at
  `4dd011712`, and `tools/playbook/render_playbook.py#write_unit_usage_plant`, still matching LF.
  Options: (a) `remove_unit_row` in `tools/playbook/instruction_units.py`, beside the reader whose LF
  bodies cause the defect, re-parsing the file's own bytes through `parse_unit_rows`; (b) the swap
  copied into the second plant; (c) the swap moved into a function of `tools/playbook/pins.py` the
  renderer imports. (b) is the copy the reuse rule refuses at a kind's second instance. (c) shares
  the swap, which assumes one line ending across a file, from the module of one class. (a) shares one
  match that holds for any line endings the file holds, from the module both plants already import.
  `tools/playbook/instructions_edit.py#derive_candidate` stays out: it parses the bytes it rewrites,
  so it never had the defect. RESOLVED (agent, 2026-11-10, delegated): (a), the most feature-rich.
  widens: none · relaxes: none
- **F4 — How the unit-line check resolves a line's tag.** PLAY-dOrderedCharter-37's S4 specced one
  `gov_tag.py show <tag>` child per distinct tag, about 1.5 s each (PINNED there at `e0768687d`).
  Options: (a) as specced; (b) membership of `unit:<tag>` in the population the leg already reads,
  which the `unit` class registered at `4dd011712` fills with every gov unit tag. `show` answers a tag
  only a retired row holds with that row and exit 0 (`tools/playbook/gov_tag.py`, its docstring and
  its `show` branch), so (a) resolves a line naming a retired unit; (b) reds it, and runs no child.
  Both meet AC3. (b) needs the `unit` class registered, and refuses, exit 2, where it is not.
  RESOLVED (agent, 2026-11-10, delegated): (b), the most feature-rich, a retired unit's line red.
  widens: none · relaxes: none
- **F5 — How `help/step-gate.md` lists the classes.** Its table types nine classes and the registry
  holds twelve at `f66d97aea`, thirteen after S3. Options: (a) the four missing rows typed into
  the table; (b) the table's place taken by a pointer to `python tools/govkit/step_gate.py --list`,
  which prints each class's id, count and summary from the registry, and to the registry file; (c) a
  reference page rendered from the registry's rows. (c) is a new registry page with members no class
  anchors, a unit of its own. (a) and (b) both meet AC9; (a) leaves the table to drift again at the
  next class, a typed inventory beside its source, where (b) leaves no follow-up. RESOLVED (agent,
  2026-11-10, delegated): (b), the most feature-rich, fewest follow-ups. widens: none · relaxes: none
- **F6 — What a rendered summary does with `<`, `>` and `&`.** Two of the four unit texts spell
  `<prefix>`, and the kinds page already shows `skills/<name>/` in prose, which a Markdown viewer
  reads as a tag and hides (section 4 Evidence). Options: (a) the render escapes the three characters
  in a summary; (b) the summary written as its row states it; (c) the summary set in a code span. (b)
  ships a units page whose rule lines hide their path. (c) changes how every summary reads, prose set
  as code. (a) changes the bytes of the one kinds line and the units page and no anchor, the
  fingerprint being the row's. RESOLVED (agent, 2026-11-10, delegated): (a), the most feature-rich.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft, from `2026-11-10-prompt-PLAY-dOrderedCharter-76-spec-brief.md`:
  PLAY-dOrderedCharter-37's later commit, refused at `--dispatch` when its CLOSED spec went live,
  carried onto a new unit. Its section 8 F8, F10 and F11 scope is S1, S2, S3 and S5 here, its S8 is
  S6, and its AC1 four-page half, AC8 and AC10's `unit-usage` half are AC1, AC3 and AC4. The four
  items the main loop found after `19648821f` are S7, S8, S4 and S9, with F1, F2, F3 and F5; F4 and
  F6 are new.

## 10. Reuse audit

The seams extended: the reference declaration and its render,
`tools/playbook/render_playbook.py#render_reference_pages`, which reads the new row with no new code
and writes the unit line from it; the step gate's class registry, `tools/govkit/surface-classes.toml`,
and the docs leg's class rows, `tools/govkit/usage.toml`, each joined by a row; the docs leg's state
reader, `tools/govkit/docs_leg.py#read_docs_state`, with its fence-aware line reader
`tools/govkit/docs_leg.py#read_page_lines` and the population it already holds; the instruction unit
parser `tools/playbook/instruction_units.py#parse_unit_rows`, which the shared removal re-runs over the
file's bytes; and the policy kit's optional row in `tools/policy/kit.toml`, the precedent S8 follows.
Re-run at `f66d97aea`, `python tools/codebase-map/reuse_lookup.py "remove an instruction unit row from
its manifest in the file's own line endings"` ranked `parse_unit_rows` the first seam in the
playbook kit, behind name-stem hits in suite files, and `read_units` and `check_unit_row` after it;
`python tools/codebase-map/reuse_lookup.py "check each help page names the unit it documents"` ranked
name-stem hits only, no unit-line reader, so the check is new code inside the docs leg's existing
state reader. The recall query returned PLAY-dOrderedCharter-37's S4 and its later-commit brief,
PLAY-dOrderedCharter-37's builder return listing the later commit's scope, and TOOL-dTotalRecall-26's
S9, which reads the same `<!-- unit: <tag> -->` lines and so fixes their grammar as specced.

Recall terms used: `python tools/memory-recall/query.py "how does a help page link to the instruction unit it documents and how is the unit line checked" --terms "unit line help page unit-usage class reference row docs leg check_unit_lines later commit units page"`
