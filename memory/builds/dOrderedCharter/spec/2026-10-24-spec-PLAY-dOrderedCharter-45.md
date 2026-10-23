# PLAY-dOrderedCharter-45 — the merge driver's TOML-table class states its whole conflict envelope and proves its output parses

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 17 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-build-PLAY-dOrderedCharter-45-deviation-451.md](../build/2026-10-24-build-PLAY-dOrderedCharter-45-deviation-451.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md](../reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 79 at HIGH**, its item **H6**. `PLAY-dOrderedCharter-15` S1 adds a multi-line
`[[unit]]` table class to `tools/memory-tree/merge-rows.py`, whose row plane is one line per row
(`_ROW_RE` at `:402`), and states only "no tag lost, none duplicated". It says nothing about both
sides editing one tag's table, one side deleting a tag the other edits, a multi-line `text = """..."""`
string, or whether the merged file must still parse as TOML. A line merge would interleave two edits
of one unit's text, and a whole-table merge would silently drop one side's edit; both pass unit 15's
AC1, and the instruction manifests agents load would be corrupted across nodes at exit 0. This unit
gives the class its full envelope: a per-entry three-way merge over parsed tables, every both-sides
change a conflict, and a postcondition that the output parses and that each entry's bytes are one
side's. It repairs unit 15 and is built right after it.

## 2. Scope (IN)

- **S1** — The class, selected by path. `merge()` in `tools/memory-tree/merge-rows.py` routes a `%P`
  whose file name is `instructions.toml` to `resolve_tables(o, a, b)` before the row plane runs, so no
  line of an instruction manifest reaches `skeleton` or `resolve_rows`. This supersedes unit 15 S1's
  "gains a TOML-table class keyed by each `[[unit]]` table's `tag`, with the driver's postconditions"
  as the class's definition. Observed by AC1.
- **S2** — The entries. Each side is parsed with `tomllib` and cut into a preamble (the bytes before
  the first array-of-tables header) and one chunk per array-of-tables entry, from its header line to
  the line before the next header at column 0. An entry's key is its array name with its `tag` field,
  or with its `key` field where it has no `tag` (the overlay's `[[policy]]` rows, unit 32 S7). A chunk
  is accepted only when parsing it alone yields exactly the one entry `tomllib` read for that key from
  the whole file; any other cut, an entry with neither field, or a repeated key on one side fails
  closed. So a `"""` string holding a line that looks like a header cannot split an entry. Observed by
  AC2 and AC5.
- **S3** — The envelope, per key, against the base:

  | Base | Ours | Theirs | Result |
  |---|---|---|---|
  | present | unchanged | unchanged | base |
  | present | changed | unchanged | ours |
  | present | unchanged | changed | theirs |
  | present | changed | changed, same bytes | ours |
  | present | changed | changed, different bytes | **conflict** |
  | present | deleted | unchanged | deleted |
  | present | deleted | changed | **conflict** |
  | present | changed | deleted | **conflict** |
  | absent | added | absent | ours |
  | absent | added | added, same bytes | ours, once |
  | absent | added | added, different bytes | **conflict** |

  The preamble takes the same rule as one entry. "Changed" compares chunk bytes with line endings
  folded, so a CRLF checkout of an unchanged table is unchanged. Observed by AC3.
- **S4** — The output and its postconditions. A clean result is ours' entries in ours' order, each
  taken as S3's table says, then theirs' additions in theirs' order. Before it is written: the
  text parses with `tomllib`; its key set equals the set S3 derived, each key once; and each entry's
  chunk is byte-identical to that key's chunk on one of the three sides. A failed postcondition, or
  any conflict, writes the whole-file conflict body through `write_conflict_body`
  (`tools/memory-tree/merge-rows.py:1333`) with a label naming every conflicting key, and exits 1, as
  the driver fails closed today (`:1550-1553`). Observed by AC4.
- **S5** — The plants, through unit 15's fixture, `python tools/playbook/instructions_edit.py fixture
  --plant <case>`: `merge-both-edit`, `merge-delete-edit`, `merge-edit-delete`, `merge-multiline` (a
  `text = """..."""` value on each side, one holding a line that reads `[[unit]]`), `merge-same-add`,
  `merge-policy` (two `[[policy]]` rows of the overlay) and `merge-parse` (a side whose cut is
  ambiguous). Observed by AC1 to AC5.

## 3. Non-goals (OUT)

- The `.gitattributes` lines that route the manifests to `merge=rows`, and the manifest list: unit
  15's S1.
- The row plane, the view/shard refusal and the build backlog class: unchanged.
- Resolving a conflict automatically by any rule: every both-sides change is the author's.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-15` — the manifest list, the `.gitattributes` routing and the fixture's merge plant, which S1 selects on and S5 extends; without them no manifest reaches the driver
- **hands-off** `PLAY-dOrderedCharter-52` — the envelope made total, with rows for theirs' delete, both deletes and theirs' add, and any unlisted state a conflict (round-2 id 33)
- **hands-off** `PLAY-dOrderedCharter-55` — round-2 ids 34 and 35: the newline contract and the `TableConflict` arm of `main()`

## 4. Design

### Evidence

Read at `ce13efbe`. `_ROW_RE = re.compile(r"^\s*[-*]\s")` (`tools/memory-tree/merge-rows.py:402`) is
the driver's one partition predicate, one line at a time, and its docstring's "TWO PLANES" paragraph
says every line is ROW or STRUCTURE by that predicate alone. A `[[unit]]` table is neither shape: its
lines are `key = value` pairs, merged positionally as structure by `git merge-file`. `merge()`
(`:1227`) receives `%P` as keyword-only `path`; `main()` (`:1508`) converts any exception into
`write_conflict_body` (`:1333`), a whole-file conflict carrying both sides. Unit 15 S1 routes
`**/instructions.toml` and `.governance/instructions.toml` to `merge=rows`, and its AC1 plants two adds
and one duplicate add only.

### Flow

```
resolve_tables(o, a, b):
  for side in (o, a, b): parse with tomllib; cut into preamble + {key: chunk}; verify each chunk (S2)
  for key in union of keys: apply S3's table against base
  if any conflict: raise TableConflict(keys)          -> main writes the conflict body, exit 1
  out = ours order with S3 applied, then theirs' additions
  check S4's three postconditions                     -> raise on failure, same exit
  return out
```

### Inventory

Minted: `resolve_tables`, the exception class `TableConflict`, and the seven plant names. Naming cells:
`lexicon naming predicates` grades the Python names.

### Files touched (estimate)

- `tools/memory-tree/merge-rows.py`
- `tools/memory-tree/merge-rows.test.sh`
- `tools/playbook/instructions_edit.py` (the fixture's plants)

### Rollout

Live at landing, order 17, after unit 15 at order 16. Unit 1 shares order 17 and writes none of these
files. No manifest holds rows before unit 9's, so the first merge the class sees is a real one.

### Alternatives rejected

- **A line merge of the table's lines**, which is what the structure plane does today: it interleaves
  two edits of one `text` value and passes a "no tag lost" check.
- **Whole-table take-ours on a both-sides edit**: silent loss of theirs, the failure the driver's
  fail-closed rule exists to prevent.
- **Merging field by field inside one unit.** Two edits of different fields of one unit can each be
  right and wrong together (a `level` move and a `text` rewrite); the author reads the pair.

## 5. Production-readiness checklist

- security: no new surface; the driver still writes only `%A`.
- perf / scale: three `tomllib` parses and one per chunk, per conflicting manifest.
- error / empty / loading states: every refusal is the existing whole-file conflict with a label; a
  side that does not parse is a conflict, never a take.
- observability: the conflict label names each conflicting key, `unit.<tag>` or `policy.<key>`.
- risks: comments between two tables travel with the earlier table's chunk; a comment edited on both
  sides is a conflict on that table.
- testing: AC1 to AC5 by fixture; the driver's suite gains the arm §7 names.
- migration: none.
- user docs: the driver's docstring names the third plane, the table class, beside its two.

## 6. Acceptance criteria

- **AC1** — When `python instructions_edit.py fixture --plant merge` runs after this
  unit, the two-adds case merges with both tags once, and a probe that records which functions run
  shows `resolve_tables` ran and `skeleton` did not.
  Red when: a manifest's lines reach the row plane.
- **AC2** — When `--plant merge-multiline` runs, both sides edit other units and one holds a `text`
  string with a line reading `[[unit]]`; the merge exits 0, the output parses, and that unit's chunk is
  byte-identical to its side's.
  Red when: the string is cut at the inner line, or the output does not parse.
- **AC3** — When `--plant merge-both-edit`, `merge-delete-edit` and `merge-edit-delete` run, each exits
  1 with a whole-file conflict whose label names the tag; `merge-same-add` exits 0 with the tag once.
  Red when: a both-sides change resolves to one side, or an identical add duplicates.
- **AC4** — When `--plant merge-parse` runs over a side whose cut does not reproduce its parse, the
  merge exits 1 with the conflict body and `%A` holds both sides.
  Red when: a merge whose output fails a postcondition is written as clean.
- **AC5** — When `--plant merge-policy` runs, two `[[policy]]` rows added on each side merge keyed by
  `key`, and both sides editing one row's `default` is a conflict naming `policy.<key>`.
  Red when: a policy row is keyed by position, or merged without a key.

## 7. Gates

`row-keyed merge driver replay` · `memory hygiene` · `check-wiring self-test` · `playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `verdict epoch (kit version dates the engine)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/merge-rows.test.sh · covers AC2 AC3 AC4 AC5 · the table class over the seven plants' inputs, each failing case staged by a line merge of the same three files · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 15's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How fine the merge's grain is.** Options: (a) per entry, every both-sides change a conflict;
  (b) per field inside an entry; (c) whole file, every concurrent edit a conflict. (b) can combine two
  edits into a unit neither author wrote; (c) conflicts on every pair of independent adds, which unit
  15's AC1 requires to merge.
  RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 79 (HIGH, item H6).
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-52, PLAY-dOrderedCharter-55.

## 10. Reuse audit

The seam extended is `merge()` and `main()` in `tools/memory-tree/merge-rows.py` (`:1227`, `:1508`), the
row-keyed driver every governed index already routes through, with its fail-closed conflict writer
`write_conflict_body` (`:1333`) reused as is. `python tools/codebase-map/reuse_lookup.py "three-way
merge of keyed TOML tables with a parse postcondition"` ranked `key` (`tools/memory-tree/merge-rows.py`,
fan-in 104), `parse` and `merge` (`tools/memory-tree/merge-rows.py`, `tools/settings-merge.py`) by name
stem. `merge` is the seam; `key` keys one-line rows by id and belongs to the plane this class
bypasses, so the probe's first hit is the thing the class must not use. The recall query returned TOOL-aPacedTurnstile-10's
note that the driver fails closed, the property S4 keeps.

Recall terms used: `python tools/memory-recall/query.py "how does merge-rows resolve a conflict and what postconditions does it enforce" --terms "merge-rows driver row-keyed postcondition duplicate loss conflict three-way merge TOML table"`
