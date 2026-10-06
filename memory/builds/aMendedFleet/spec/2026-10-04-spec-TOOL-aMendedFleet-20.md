# TOOL-aMendedFleet-20 — `--new-spec` writes a skeleton that already carries every shape a cutoff demands

**Status:** CLOSED · rev-2 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

A new spec meets its rules one bar cycle at a time. The dated cutoff keys in `.memory-tree.conf`
each add a shape a spec must carry, and an author copying the template skeleton learns the missing
ones from a red leg, one per cycle; the report's own case was a new folder surfacing four rules over
four cycles. This unit adds
`gen_build_index.py --new-spec`, which writes a spec whose header is filled and whose body already
carries every shape those keys demand, with each part only an author can write left as a marked
slot that check 12 refuses until it is filled.

## 2. Scope (IN)

- **S1** — A new mode, `gen_build_index.py --new-spec <ID> --tier <1|2> [--order <n>] [--base <sha>]`,
  writes `<MEMORY_ROOT>/builds/<slug>/spec/<today>-spec-<ID>.md` and prints the path it wrote and
  how many fill slots the file carries. It writes nothing else and stages nothing. Observed by AC1
  and AC4.
- **S2** — The status header is filled, never a slot: status `OPEN`, `rev-1`, today's date, node
  from the slug's first letter, the given tier, `base` as the eight-hex form of `--base` or of
  `HEAD` resolved to a commit, `streams` from the id's family through the conf's `FAMILIES` map,
  and `order <n>` only when `--order` is given. Observed by AC1 and AC5.
- **S3** — The body's `##` headings are READ from the skeleton fence of the installed
  `<MEMORY_ROOT>/TEMPLATE-SPEC.md`, in its order, so the section canon keeps one spelling. Under
  them the generator writes the shapes the §4 table names: a scope item naming `AC1`, the
  `### Edges` sub-head reading `none`, the `### Files touched (estimate)` sub-head, one §5 bullet per
  `READINESS_ROWS` row, an acceptance bullet with a backticked token and a `Red when:` clause, a §7
  leg line, a §8 reading `none`, a complete rev-1 line in §9, and a §10 probe slot followed by a
  `Recall terms used:` slot. Observed by AC1, AC2 and AC5.
- **S4** — Check 12's skeleton-placeholder pattern in `tools/memory-tree/check-memory-hygiene.sh`
  gains the fill marker as a third alternative, so a slot left unfilled is refused on both tiers
  by the reason check 12 already prints. Observed by AC1 and AC3.
- **S5** — Refusals, each exiting non-zero before any file is written: no `--tier`, or a tier other
  than 1 or 2; an id that does not parse as family, slug and seq; a family `FAMILIES` does not
  declare; a slug with no tracked build README; an id that a spec under that build already carries
  in its H1; a target file that exists; a `--base` that does not resolve to a commit; an `--order`
  that is not a positive integer. Observed by AC4.
- **S6** — The kit README's scaffold paragraph names `--new-spec`, its arguments, the fill marker
  and the two commands an author runs after filling. Observed by AC6.
- **S7** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Rendering the build index or staging the new file. Under concurrent writers that would contend on
  one git index and one `memory/LIVE.md`; the author stages and renders, as this build's own spec
  writers are told to (§8 F3).
- Filling the §7 leg line from the paths an author will touch. The guard join lives in
  `tools/check-spec-tokens.py`, a repo-root tool this kit file may not name, and the paths do not
  exist when the skeleton is written.
- Teaching the unattended planning verb's THIN predicate the fill marker. A skeleton whose slots are
  unfilled grades READY there, because THIN reads only empty sections; check 12 still refuses it
  at the bar. That predicate belongs to the unattended kit, and spelling this kit's marker there is
  a cross-kit literal; it is filed as an ask at this build's close.
- `--doctor`, which is unit 19's mechanism and reads an existing folder rather than writing a file.
- Any change to `memory/TEMPLATE-SPEC.md`. Its rule that both tiers stay free of skeleton
  placeholders already covers a third placeholder token.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; no file below moved between it and `6a88fbf7`.

- `cmd_new_build` in `tools/memory-tree/gen_build_index.py` is the kit's one scaffold. It parses
  its own arguments in `read_new_build_args`, refuses with `Problem`, writes through `write_text`,
  and is dispatched from `main` inside the `Problem` handler. `read_discipline_map` already turns
  `FAMILIES` into a family-to-discipline map.
- Check 12's placeholder test is one awk line over the unfenced body, matching two literal skeleton
  tokens, on both tiers, and printing `unfilled skeleton placeholder`. A fenced block is not read.
- The skeleton fence in `memory/TEMPLATE-SPEC.md` carries the ten `##` headings and `### Edges`.
  It names `### Files touched (estimate)` only in prose, so the generator writes that sub-head itself.
- `git grep` finds the fill marker in no tracked file, so arming it reds no landed spec.

### What each cutoff demands, and what the skeleton writes

| Key | Shape it demands of a new spec | What the skeleton writes |
|---|---|---|
| `SPEC_FORMAT_CUTOFF` | a parseable header, no skeleton placeholder | S2's header; slots refused until filled |
| `STREAMS_CUTOFF` | `streams` in the header | the family's discipline |
| `SPEC10_CUTOFF`, `SPEC10_EVIDENCE_CUTOFF` | ten sections; §10 probe then terms | the template's headings; two §10 slots |
| `FORK_MARK_CUTOFF`, `FORK_ITEM_CUTOFF` | §8 `none` or F-items | `none` |
| `SPEC_WITNESS_CUTOFF`, `SPEC_FAILURE_MODE_CUTOFF` | a backticked token and `Red when:` per AC | one AC carrying both |
| `SCOPE_JOIN_CUTOFF` | each scope item names an AC | S1 naming AC1 |
| `REV_SCOPE_CUTOFF` | a scope field from rev-2 on | rev-1, which is exempt |
| `SPEC_EDGES_CUTOFF`, `SPEC_HANDOFF_CUTOFF` | `### Edges` holding bullets or `none` | `none` |
| `READINESS_ROWS_CUTOFF` | the declared §5 rows | one bullet per declared row |
| `SPEC_LEGLINE_CUTOFF` | a §7 line of backticked names | one backticked leg slot |
| `SPEC_GUARD_LEGS_CUTOFF`, `SPEC_DIRECT_CUTOFF` | owed legs named; no bar invocation | no path and no invocation |
| `BASE_RESOLVE_CUTOFF` | a `base` that resolves | a resolved sha |

The skeleton is the strictest shape and does not branch on any key. Every shape in the table is
legal on a spec a key does not reach, and a new spec is dated today, past the one key that selects
between two canons. The remaining keys in the conf shape asks, ledgers and review records, never a
spec body.

### The fill marker

This spec never spells the marker outside a fenced block, because check 12 would then refuse this
spec once S4 lands. Its bytes, and the shape of one slot:

```
FILL_MARKER = "<fill:"
<fill: what the author writes here>
<fill: leg>          # the one slot on the §7 leg line
```

### Inventory

- `cmd_new_spec`, `read_new_spec_args`, `render_spec_skeleton`, `NEW_SPEC_USAGE` and `FILL_MARKER`,
  all in `gen_build_index.py`. The lexicon leg grades each definition; a refused name takes its
  `--suggest` answer at build time and this list is amended with a rev bump.
- The `--new-spec` token joins the mode list `main` accepts and its usage line.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Copy the template skeleton verbatim.** Its bodies are instructions, and most of them satisfy the
  shape rules as written, so an author who never fills a section is never told. The template says so
  in its §10 note.
- **A literal ten-heading canon in the generator.** A second spelling of the canon beside the
  template's and check 12's; reading the installed template keeps one.
- **Per-key branching.** Every shape is legal before its key's date, so branching buys no correct
  output the strictest shape lacks, and costs one code path per key.

## 5. Production-readiness checklist

- security — writes one file under the memory root, at a path built from a validated id; the id
  regex admits no separator, so no `..` can reach the path.
- perf / scale — one template read and one conf read; well under a second.
- error / empty / loading states — every refusal exits before the write, so a refused call leaves
  no file; a template with no skeleton fence is a refusal naming the file.
- observability — the printed slot count says how much is left to write.
- risks — an adopter's template that renames a heading is followed, because the headings are read;
  one that drops the fence makes the mode refuse rather than guess.
- testing — a `--selftest` arm for the render, and direct calls in a scratch clone for the rest.
- migration — none; the new placeholder alternative matches no tracked file.
- user docs — the kit README, S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --new-spec <id> --tier 2` runs in a
  `git clone --local` of the unit's branch under `%TEMP%`, for this build's next unminted id, and
  the file it prints is staged, `bash tools/memory-tree/check-memory-hygiene.sh --staged` names
  that file under check 12 with `unfilled skeleton placeholder` and with no other check-12 reason.
  Red when: any shape reason, a canon, edges, readiness-row, F-item, §10, witness, failure-mode or
  scope-join finding, names the file.
  cost: one staged hygiene run in the clone, minutes rather than seconds.
  fixture: the clone and the unminted id; the tree holds neither today.
- **AC2** — When every slot of that file is filled by
  `sed -i -E -e 's/<fill[:] leg>/memory hygiene/' -e 's/<fill[:] [^>]*>/no existing seam fits/g'`
  and AC1's staged run repeats, no check-12 reason names the file, and
  `python tools/check-spec-tokens.py` reports no hit naming it.
  Red when: a check-12 reason or a spec-tokens hit names the filled file.
- **AC3** — When the fill-marker alternative is deleted from check 12's placeholder pattern in
  `tools/memory-tree/check-memory-hygiene.sh` as a staged break and AC1's run repeats on the
  unfilled file, check 12 names nothing about it.
  Red when: check 12 still names the file, meaning the refusal came from another rule, or a shape
  reason appears, meaning the skeleton was not shape-complete.
- **AC4** — When `gen_build_index.py --new-spec` is called in that clone once per S5
  refusal, among them with `TOOL-aMendedFleet-10`, which a spec already carries, each exits
  non-zero naming its conflict, and `git status --porcelain` prints nothing afterwards.
  Red when: any call exits 0 or leaves a file behind.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, an arm rendering the
  skeleton from a fixture template and conf finds every `##` heading of the fixture fence in order,
  one §5 bullet per fixture `READINESS_ROWS` row, a header matching check 12's header pattern, and
  `order` only when the arm passed it.
  Red when: a fixture heading is absent or out of order, or a row is missing.
  cost: the generator's whole self-test, about ninety seconds on node a.
- **AC6** — When `grep -n -- "--new-spec" tools/memory-tree/README.md` runs, the scaffold paragraph
  names the mode, `--tier`, `--order`, `--base` and the fill marker.
  Red when: the paragraph names none of them.

## 7. Gates

`build-index selftest` · `memory hygiene` · `memory-hygiene self-test` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py --selftest · the skeleton render over a fixture template, staged red by dropping one heading from the render · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · a fixture spec carrying one fill slot, staged red by deleting the marker alternative · none

## 8. Open questions

- **F1 — How does an unfilled slot stay refused?**
  Options: a new marker joins check 12's placeholder pattern; each slot reuses one of the two
  tokens check 12 already refuses; slots carry plain prose. Plain prose passes every shape rule, the
  exact failure the template warns about, and the reused tokens are a date and an id that mean
  nothing in a slot.
  RESOLVED (agent, 2026-10-04, delegated): a new marker, refused by check 12 on both tiers.
- **F2 — Where do the section headings come from?**
  Options: the installed template's skeleton fence; a literal canon in the generator. The literal
  is a third spelling beside the template and check 12.
  RESOLVED (agent, 2026-10-04, delegated): read from the installed template.
- **F3 — Does the mode stage the file and render the index, as `--new-build` does?**
  Options: stage and render; write only. `--new-build` renders because its promise is a filled
  README region. Here a render rewrites shared generated files, and this build's own spec stage
  runs several writers at once that are told not to stage or render for that reason.
  RESOLVED (agent, 2026-10-04, delegated): write only, and print the stage and render commands.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `cmd_new_build`, check 12's placeholder line, the
  template's skeleton fence and every cutoff key in the conf at base.
- rev-2 · 2026-10-04 · §2 S7 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.

## 10. Reuse audit

The seam extended is the kit's scaffold, `cmd_new_build` in `tools/memory-tree/gen_build_index.py`,
with its argument parser, `write_text`, `read_discipline_map` and the `Problem` refusal path; the
headings come from `memory/TEMPLATE-SPEC.md`, which `adopt-memory-tree.sh` renders with the conf's
readiness rows. `python tools/codebase-map/reuse_lookup.py "write a new spec skeleton file with a
filled status header"` named `write_text` and `parse_spec_h1` in `tools/memory-tree/tree_lib.py`,
which S5's duplicate-id refusal reuses, and no function that writes a spec, so no spec writer
exists to extend. Recall named `TOOL-dDerivedDocket-15`, which specified the `--new-build`
scaffold, and `TOOL-aRuledParchment-1`, which shipped check 12. The report and the tree agree on
the count: 22 cutoff keys in the conf, PINNED, counted 2026-10-04 at `6a88fbf7` with
`grep -cE '^[A-Z0-9_]*_CUTOFF=' .memory-tree.conf`. The §4 table sorts them; the five it leaves out
shape asks, ledgers and review records.

Recall terms used: `python tools/memory-recall/query.py "is there a scaffold that writes a new spec file which already satisfies the spec format cutoffs" --terms "new-spec skeleton scaffold TEMPLATE-SPEC check 12 cutoff placeholder status header new-build doctor spec format"`
