# TOOL-dDeclaredLoop-61 — every draw row carries a draw id, so two identical parallel draws stay two rows

**Status:** CLOSED · rev-3 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 30 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-61-deviation-611.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-61-deviation-611.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-61-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-61-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-61-deviation-612.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-61-deviation-612.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-61-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-61-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-61-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-61-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-61-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-61-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 53 at HIGH**, its item **H4**, which it shares with id 38; id 38 is
`TOOL-dDeclaredLoop-62`. A draw row is `draw · <cause> · <item> · <spent>/<total>`, the draw half of
`ROW` in `tools/loop/budget.py#ROW`, written by `tools/loop/budget.py#record_draw`, and it carries no
unit, sha or time. Two worktrees making the same draw on one item, each typing the figure its own
history saw, append byte-identical lines. `.gitattributes` merges transition records with `union`, and
its own comment says union keeps two byte-identical appended rows once
(`.gitattributes@eab9e190:113`); the module's does-not-check paragraph says the same
(`tools/loop/budget.py@dec43c70:64`). Two skeptics reproduced such a merge at rc 0 holding one draw row. The
budget counts one draw fewer per collision, exactly when parallel worktrees draw on the same thing, and
the typed-versus-derived note `TOOL-dDeclaredLoop-49` S2 built never fires, because one row is left.
This unit makes every row unique, the half of the fix that lets any merge keep both. It repairs
`TOOL-dDeclaredLoop-49`.

## 2. Scope (IN)

- **S1** — The draw row grammar gains a trailing field, the draw id: `draw · <cause> · <item> ·
  <spent>/<total> · <draw-id>`, the id `<UTC yyyymmddThhmmssZ>-<6 hex>`, the hex from
  `secrets.token_hex(3)` at write time. `record_draw` mints one id per draw row and writes it on every
  home it writes: a log-record row, a run-state row, and the row it hands the transition writer in
  `lines`. A patch build's row keeps its ` · budget <origin>` suffix after the id (§8 F2). The first log
  record's copy of run-state rows, `TOOL-dDeclaredLoop-30` S9's, carries the id with the row. `ROW`
  gains the id as an optional seventh group, so a row written before this unit still reads; a freeze
  row carries no id. This amends `TOOL-dDeclaredLoop-30` S3's grammar by one field. Observed by AC1, AC3.
- **S2** — `spent` counts draw rows by draw id in `tools/loop/budget.py#read_budget_rows`: two rows
  carrying one id are one draw, and a row carrying no id counts as its own draw, so no landed record's
  count moves. A row whose last field is neither the figure nor a draw id stays outside the grammar and
  is refused by name, as the reader refuses any such row today (§8 F3). The `draws` and `disagree`
  answers follow the counted rows, so `count_returns` and the ordinal note read the same population.
  This refines the count `TOOL-dDeclaredLoop-30` S3 built. Observed by AC1, AC2.
- **S3** — A draw riding a `Gov-Transition` trailer, `TOOL-dDeclaredLoop-48` S2's `draw=` field, carries
  no id: its commit is its identity, and two such draws are two commits.
  `tools/loop/budget.py#render_budget_fields` formats the cause, item and figures alone, and
  `tools/loop/budget.py#read_trailer_rows` reads each trailer as its own id-less row, so the built
  code keeps this once `ROW` admits the id. Observed by AC3.
- **S4** — The `parallel-append` plant `TOOL-dDeclaredLoop-49` built, which already merges two branches
  under the attribute `git check-attr merge` answers for a transition record path, draws the same cause
  on the same item on both sides, so the two appended rows differ in their draw id alone (§8 F4). Its
  `PLANTS` text says so. Observed by AC1.
- **S5** — One new plant, `draw-id-rows`, joins `PLANTS`: id-less rows, a repeated id and a malformed id
  read from one log record. Observed by AC2.
- **S6** — The plants whose needles pin a row's end compare each row with its id cut by `ROW`'s id group,
  and assert the id where a home writes one; no plant spells the id's pattern a second time. §5's
  table lists the needles. Observed by AC1, AC3.
- **S7** — `help/loop.md`'s rework-budget section states the id: the row's grammar, that the trailer's
  `draw=` carries none, and that two parallel draws stay two rows. The module docstring's rows and
  does-not-check paragraphs say the same. NOT OBSERVED by a criterion: prose, read at review.

## 3. Non-goals (OUT)

- Which merge driver `.gitattributes` names for transition records, and its comment's weighing:
  `TOOL-dDeclaredLoop-62`, which takes this unit's id as what keeps two rows apart.
- Rewriting landed rows to carry an id: S2 reads them as they are.
- One dedup function shared with `TOOL-dDeclaredLoop-60`'s archive read, and a `--explain` surface: the
  round-3 spec audit's ids 3, 13 and 23, batched into `TOOL-dDeclaredLoop-75`. No `--explain` exists
  on `budget.py` at the tip, and this unit adds none.
- A checklist entry that every merged append-only record carries a unique field, the finding's
  left-shift: the class is recorded at the close; S4 is this record's identical-rows fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-49` — the typed-figure note and the union attribute for transition records, whose rows this unit makes distinct
- **hands-off** `TOOL-dDeclaredLoop-62` — the draw id, the field that keeps two identical draws two lines under any merge driver
- **hands-off** `TOOL-dDeclaredLoop-75` — the draw id and its row grammar, the id written before any ` · budget <slug>` suffix (§8 F2), for that unit's dedup function, `--explain` and order items (the round-3 spec audit's ids 3, 13, 14, 23 and 33); this pass keeps the `loop budget fixtures` leg green (id 31)

## 4. Design

### Evidence

- The skeptic's reproduction, id 38 and id 53 of the report: two branches each appending
  `draw · review-round · item.a · 2/10` under `merge=union` merged at rc 0 with one such row.
- `.gitattributes@eab9e190:113`, the comment on the transition-record line: union "keeps two
  byte-identical appended rows once".
- `tools/loop/budget.py#write_budget_rows`: a run-state row opens with a UTC stamp at second
  resolution; a log-record row has no such field.
- `tools/loop/budget.py#record_draw` builds its one draw row from the cause, item and figures, and hands
  it to every home: the transition writer's `lines`, the newest log record, or the run-state file with
  the patch suffix appended (`row + suffix`).
- `tools/loop/budget.py#read_budget_rows` refuses any row `ROW` does not fullmatch, and strips a
  ` · budget <slug>` suffix with `SUFFIXED` before it reads the grammar.

### The row

```
draw · review-round · TOOL-dX · 3/10 · 20261024T153012Z-4fa1c9
<ts> draw · patch:dXPatch · item.a · 1/4 · 20261024T153012Z-0b7e22 · budget dX
draw=review-round@TOOL-dX@3+10                                  (a trailer: no id)
```

`ROW`'s draw alternative becomes `draw · (\S+) · (\S+) · (\d+)/(\d+)(?: · (<id>))?`, the id pattern
`[0-9]{8}T[0-9]{6}Z-[0-9a-f]{6}` written once, inside `ROW`. Groups 1 to 6 keep their numbers, so the
carried-row sort and `render_budget_fields` read as they do. Six hex digits PINNED by the design beside
a second-resolution time make a collision need two draws in one second drawing the same 24 bits PINNED,
and S2 would then count one draw fewer, the defect's own bound at a rate this unit does not measure.
The id is never compared across builds.

### The count

```
seen = set()
for row in rows:                       # rows as read today, in order
    hit = ROW.fullmatch(row)           # no match: refused, as today
    freeze row: as today
    id = hit.group(7)
    if id and id in seen: continue     # a copy of a draw already counted
    seen.add(id) when id
    draws.append(...); ordinal note as today
```

`rows` in the answer stays every row read, so a plant or caller printing them sees the copies too.

### Inventory

- The draw id field and `ROW`'s seventh group; `import secrets`.
- The `PLANTS` key `draw-id-rows`.
- No function and no module constant is minted: the id is formatted inside `record_draw`, and the
  plants cut it through `ROW`, so `VERB_OFFENDER_PIN` and the lexicon's `py.constant` cell do not move.

### Files touched (estimate)

- `tools/loop/budget.py`
- `help/loop.md`
- `tools/run-gates/selftest-budgets.txt`

### Alternatives rejected

- **The drawing commit's sha.** A row is written before its commit exists, so the sha cannot be in it.
- **A worktree name.** Two runs in one worktree, one after the other, draw the same row again.
- **Collapsing twins by their run-state timestamp.** Two distinct draws in one second would read as one;
  the round-3 spec audit's id 3 rules the id the only dedup key.

## 5. Production-readiness checklist

- security — `secrets` draws the hex; no new surface, flag or verb.
- perf / scale — one more field per row and one set per read; the selftest gains one plant.
- error / empty / loading states — a row whose last field is not a draw id is outside the grammar, and
  `read_budget_rows` refuses it naming the row, as it refuses any malformed row today, so `draw` prints
  `loop: budget · refused · ...` and exits 2 (§8 F3). A build with no draw reads `0/<total>`.
- observability — the id is in the `<row>` of `draw`'s `loop: budget · drawn · <row>` line and in each
  `disagrees` line, so a repeated or missing id is visible where the row is printed.
- risks — what this change could newly red, and what keeps each green, read at branch
  `unattended-declared-loop-d56bf0`, `a68d80da`, through `git show`:
  - the callers: `read_budget_rows`, `record_draw`, `render_budget_fields`, `write_budget_rows` and
    `budget_state` are called from `tools/loop/budget.py` and `tools/loop/loop_transition.py#write_transition`
    alone. The transition writer passes `record_draw`'s rows to `write_transition_record`,
    `write_budget_rows` or `render_budget_fields`; the first two write the row as given, and the third
    reads `ROW`'s groups 3 to 6, so a trailer never carries the id. `tools/memory-tree/build_records.py#write_record`
    refuses a line only for a newline or a field shape, which the id is not.
  - `loop budget fixtures`, the module's own plants at the tip, sixteen PINNED by the grep below. These
    needles, nine PINNED at `a68d80da`, pin a row's end and red under the id, each kept green by S6's cut:

    | Plant | Needle at the tip | Under S1 |
    |---|---|---|
    | `mint-each-lap` | every draw row ends `/8` | `read_rows` answers rows with the id cut |
    | `before-freeze` | the rows equal four literal rows | the same cut |
    | `driver-draws` | the run-state rows equal `owed` | the cut on its own comprehension |
    | `pre-spec` | the first record's draw lines equal `owed` | the cut, and AC3's id assertion |
    | `trailer-only` | the run-state file holds the `1/6` row then a newline | the row read through `ROW`, the id asserted |
    | `log-dropped` | the record holds the `1/4` row then a newline | the same |
    | `patch-trailer-only` | the row, ` · budget tFix`, a newline | the id between the figure and the suffix |
    | `parallel-append` | the rows equal two literal rows | S4's one item, the cut, the ids differing |
    | `parallel-append` | the third draw's line ends ` 3/4` | its row read through `ROW` |

    Substring needles stay green as the id follows the figure: `unrecorded`, `patch-draw`, `pre-spec`'s
    run-state check and `mint-each-lap`'s printed `<n>/8`. `re-entry`, `stale-verdict`, `route-backs`,
    `unknown-cause`, `value` and `spent-spec-round` read freeze rows, states, counts or nothing drawn.
    `run_selftest` reads `PLANTS`, so the new plant joins the leg with no edit.
  - `loop transition record`, `loop adapt fixtures` and `loop composition fixtures`: their moves reach
    `record_draw` through `write_transition`, and `git grep` finds no draw-row needle in
    `tools/loop/loop_transition.py`, `adapt.py`, `composition.py`, `position.py` or `scenario.py`.
    `check_transition_channels` compares a record's `**Key:**` fields with its trailer, never its rows.
  - the driver, `tools/unattended/unattended.sh`: untouched. `run_budget_draw` relays the script's first
    line, whose `<row>` gains the id; `tools/unattended/unattended.test.sh` holds no draw-row or
    `budget · drawn` needle, nor does any file under `tools/workflows/`, `tools/runlog/` or
    `tools/drift-audit/`. The refusal census `tools/memory-tree/check-arms.py` reads counts the tracked
    `*.sh` files that define `fail() {` (`tools/memory-tree/check-arms.py@36e38fb2:10`), so `budget.py`
    is outside it: `REFUSAL_CEILINGS` keeps the
    driver at 329 PINNED in `.memory-tree.conf` at the tip, and `TOOL-dDeclaredLoop-32`'s committed
    raise to 332 PINNED is its own. `tools/unattended/unattended.families.txt` counts nothing this unit
    writes.
  - `lexicon naming predicates`: no function and no module constant is minted, so `VERB_OFFENDER_PIN`
    stays 1215 PINNED and `SUFFIX_OFFENDER_PIN` 0 PINNED (`.lexicon.conf` at the tip). A builder who
    adds a nested helper runs `python tools/lexicon/lexicon.py --suggest <name> --as py.function` first.
  - `help page commands`: no verb or flag is added; `draw-id-rows` is a value of `--plant=`, which the
    row `script:{prefix}/loop/budget.py` already lists, so `tools/govkit/usage.toml` is not written and
    the three budget anchors on `help/loop.md` keep their fingerprints, which hash the usage row alone
    (`tools/govkit/docs_leg.py#derive_usage_fingerprint`). The edited paragraphs carry no command.
  - `every held leg is budgeted, every budget row resolves`: the `loop budget fixtures` row of
    `tools/run-gates/selftest-budgets.txt` is 336 PINNED, a proxy of 224 seconds PINNED over sixteen
    PINNED direct-CLI plant readings x1.5. It is re-priced with `draw-id-rows`' direct-CLI reading added,
    x1.5, its prose counting the plants `PLANTS` holds and naming this unit, as `TOOL-dDeclaredLoop-49`
    re-priced it.
    The leg's `ceiling` of 300 PINNED in `tools/gate-legs.json` is a hang bound the proxy stays under, so
    the manifest is not written.
  - `install-prefix (shipped surface)`: `budget.py` ships under the loop kit, so its docstring and
    messages name no kit path; the help page and the budgets file do not ship with the kit.
  - `kit epoch (shipped bytes move, the version moves)`: the loop kit's shipped bytes move, so its version
    is owed at the lander, as that leg prints.
  - `encoding posture (text IO names its encoding)` and `python reads (a name never bound, an import
    outside its guard)`: the plants write through `write_budget_rows` and `write_fixture_files`, and the
    one import is the stdlib's `secrets` at the module's top.
  - not written, each with its reason: `tools/gate-legs.json` and `tools/govkit/subject-pins.tsv`, since
    no leg is added; `tools/govkit/registry.toml`, since no row moves; `check-verdict-epoch.sh`'s
    `DELEGATES`, which lists memory-tree modules alone; the `[[upgrade]]` rows, since no landed record
    is rewritten; the kickoff manifest, whose `watch:` line in `memory/guides/SESSION-KICKOFF.md` names
    none of the three files; the map's generated files, since no symbol is minted and
    `memory/map/generated/symbols.json` records names, kinds and files alone; `.gitattributes`, which is
    `TOOL-dDeclaredLoop-62`'s; and `memory/project/positional-refs.txt`, which holds no row for this spec.
  - the shared records: the pass writes neither `memory/DECISIONS.md` nor
    `memory/project/readme-contract.txt`, the `SHARED_RECORDS` of `.unattended.conf`. No decision row is
    owed: no ceiling, pin or size row rises.
  - the counts re-derive with:

```
B=branch/unattended-declared-loop-d56bf0
git grep -n -e read_budget_rows -e record_draw -e render_budget_fields -e write_budget_rows -e budget_state "$B" -- tools
git show "$B:tools/loop/budget.py" | grep -c -E '^(PLANTS = \{| {10})"[a-z-]+": "'          # 16
git show "$B:tools/run-gates/selftest-budgets.txt" | grep '^loop budget fixtures'           # 336
git show "$B:.lexicon.conf" | grep -E '^(VERB|SUFFIX)_OFFENDER_PIN'                        # 1215, 0
git grep -n -E 'draw · |budget · drawn' "$B" -- tools ':!tools/loop/budget.py'               # none
```

- dependency — order 30, built beside `TOOL-dDeclaredLoop-31`, `TOOL-dDeclaredLoop-60` and
  `TOOL-dDeclaredLoop-62`, read on their committed specs at rev-3, rev-3 and rev-2, and after
  `TOOL-dDeclaredLoop-32`, read on its committed rev-5. 60 widens the run-state files
  `read_budget_rows` reads; this unit edits that function's per-row loop and `ROW`, so whichever lands
  second keeps the other's hunk. 60's S4 skips a copy by its timestamp; the id here is the key the
  round-3 audit's id 3 rules for, and `TOOL-dDeclaredLoop-75` S1 reconciles the two. 62 rests its
  driver on this id and builds after this unit within the order; its AC1 plant observes what S4's
  extended `parallel-append` observes, a fold its writer may take. 31 touches no file here. 32 adds a
  `target` branch to `main` and its usage row; this unit touches neither, and 32's driver relays the
  draw's first line, whose shape keeps `loop: budget · drawn · <row>`. `TOOL-dDeclaredLoop-34` is
  deferred against ask TOOL-dDeclaredLoop-113 and shares no file. Every code claim was read on the
  branch through `git show`; the reuse probes and the spec-token checker ran on the worktree at
  `179486e8`.
- testing — AC1 to AC3 as plants; the arm under §7, observed RED then GREEN at the close.
- migration — none: S2 reads id-less rows, and no landed transition record is rewritten.
- user docs — S7's paragraphs in `help/loop.md`: the row grammar at `help/loop.md@aba9e3c4:1294`, the
  trailer's id-less `draw=`, and the union sentence at `help/loop.md@aba9e3c4:1316` restated for rows that differ by id.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/budget.py --fixture --plant parallel-append` draws `fix-pass` on
  `TOOL-tFix-1` on `main` and on the branch `side`, each typing `1/4`, and merges `side` under the
  attribute `git check-attr merge` answers for the record, the merged record holds two draw rows equal
  with their ids cut and carrying two different ids, `budget_state` answers `unfrozen 2/4`, and the
  third draw's first line carries `3/4` then its id while its second ends `typed 1, derived 2`; the
  plant prints `held`.
  Red when: the rows carry no id, union keeps the identical row once, and the state reads `unfrozen 1/4`.
  figure: PINNED, the plant's base of 4 under the default `4+2` with no freeze row.
- **AC2** — When `python tools/loop/budget.py --fixture --plant draw-id-rows` appends to one log record
  two byte-identical id-less draw rows, `budget_state` answers `unfrozen 2/4`; after one id-bearing row
  appended twice it answers `unfrozen 3/4`; after a row ending ` · not-an-id` it raises the ValueError
  naming that row as outside its grammar; the plant prints `held`.
  Red when: id-less rows collapse, a repeated id counts twice, or a malformed id reads as a draw.
- **AC3** — When `python tools/loop/budget.py --fixture --plant <case>` runs `pre-spec`, `trailer-only`,
  `log-dropped` and `patch-trailer-only`, every draw row a log record or a run-state file holds carries
  a last field matching `^[0-9]{8}T[0-9]{6}Z-[0-9a-f]{6}$`, before ` · budget tFix` on the patch build's
  row; `pre-spec`'s first record carries its two copied rows with the ids their run-state rows carry;
  and `trailer-only`'s backward move carries `draw=route-back@item.build.unit-pass@2+6`; each prints
  `held`.
  Red when: a home writes the old grammar, the copy loses the id, or the trailer's field carries one.

## 7. Gates

`loop budget fixtures` · `loop transition record` · `loop adapt fixtures` · `loop composition fixtures` · `lexicon naming predicates` · `help page commands` · `every held leg is budgeted, every budget row resolves` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/budget.py · covers AC1 AC2 AC3 · the extended `parallel-append`, `pre-spec`, `trailer-only`, `log-dropped` and `patch-trailer-only` plants and the new `draw-id-rows`, each failing case staged by the plant hunks applied over the tip's id-less `ROW` and `record_draw` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Where does the id sit on a patch build's suffixed row?** `TOOL-dDeclaredLoop-75` S15 writes the
  order `[ · budget <slug>] · <draw-id>`. Options: (a) that order, the id last, which makes `SUFFIXED`
  match the suffix before an optional id and makes `record_draw` place the suffix inside the row; (b)
  the id inside the row and the suffix after it, which `record_draw`'s `row + suffix` and `SUFFIXED`'s
  strip already produce and read, so every home's row is one `ROW` grammar once the suffix is stripped.
  (b) writes less code and keeps one grammar; 75 S15 and S16 then read as this order, a sibling text
  its re-grounding takes. Recommendation: (b). RESOLVED (agent, 2026-11-16, delegated): (b), by rung 3.
  widens: none · relaxes: none
- **F3 — What does the reader do with a row whose last field is not a draw id?** Options: (a) refuse it
  as outside the grammar, as `read_budget_rows` refuses every malformed row at the tip; (b) count it as
  its own draw and name it, as rev-2 of this spec wrote. No writer produces one, so it is a hand edit;
  (b) needs a second note kind and lets a typo pass as a draw. Recommendation: (a). RESOLVED (agent,
  2026-11-16, delegated): (a), by rung 3. widens: none · relaxes: none
- **F4 — Does the identical-rows merge get a plant of its own?** Options: (a) a new
  `parallel-append-identical` plant beside `parallel-append`; (b) the built `parallel-append`, which
  already copies the tree's attribute and merges two branches, drawing one item on both sides. The
  identical case is the harder one for union and subsumes the distinct one, and (b) adds no plant time.
  Recommendation: (b). RESOLVED (agent, 2026-11-16, delegated): (b), by rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 53 (HIGH, item H4, shared
  with id 38).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-75, written by the round-3 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-16 · §1 to §10 · S1 to S7 · AC1 to AC3 · §8 F2 to F4 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `a68d80da`, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-61-1-spec-writer`: S2 refines the count 30 S3 built; the id
  sits before a patch row's suffix (F2); a malformed id is refused (F3); the identical merge rides the
  built `parallel-append` plant (F4) and `legacy-rows` and `id-on-every-home` become one new plant and
  the existing home plants; the `--explain` claim leaves, as no such surface exists; the help page and
  the budgets row join the write set; the nine row-end needles and the budgets are swept in §5.

## 10. Reuse audit

The seam is `TOOL-dDeclaredLoop-30`'s own row writer and reader in `tools/loop/budget.py`, `record_draw`
and `read_budget_rows`; the id is one field on the grammar `ROW` owns, and the identical-rows fixture is
`TOOL-dDeclaredLoop-49`'s `parallel-append` plant, extended. `python tools/codebase-map/reuse_lookup.py
"unique field on an appended row so a merge keeps both"` ranked `rows`, `row`, `merge`
(`tools/memory-tree/merge-rows.py`, `tools/settings-merge.py`), `field`, `parse_unit_rows` and
`extract_row`; `merge-rows.py` keys a row by its id or a digest of its stripped text
(`tools/memory-tree/merge-rows.py@66778f37:80`), which makes an identical row one row, so no existing seam
supplies uniqueness. `python tools/codebase-map/reuse_lookup.py "mint a random id for a written row"`
ranked the same row names and no id minter, and `git grep -e token_hex -e uuid4` over `tools/loop` and
`tools/lib` on the branch finds none, so the id is the stdlib's `secrets.token_hex` inside `record_draw`.

Recall terms used: budget draw row grammar unique id parallel worktree identical append merge union collapse spent token_hex mint random id
