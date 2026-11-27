# TOOL-dTotalRecall-36 — every code writer of a record writes its `Caused-by` line, so the causes check stays green on the records written after its seed

**Status:** CLOSED · rev-5 · 2026-11-23 · node d · Tier-2 · base 462d20f3 · streams tooling · order 17 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-36-deviation-361.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-deviation-361.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-36-deviation-362.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-deviation-362.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-22-build-TOOL-dTotalRecall-36-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dTotalRecall-36-1-acceptance-ledger.md) | log | — |
| [2026-11-22-build-TOOL-dTotalRecall-36-1-builder-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-36-1-builder-return.md) | journal | — |
| [2026-11-22-build-TOOL-dTotalRecall-36-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-36-reground-return.md) | research | — |
| [2026-11-23-build-TOOL-dTotalRecall-36-fold-return.md](../build/2026-11-23-build-TOOL-dTotalRecall-36-fold-return.md) | research | — |
| [2026-11-23-build-TOOL-dTotalRecall-36-widen-5.md](../build/2026-11-23-build-TOOL-dTotalRecall-36-widen-5.md) | widen | — |
| [2026-11-23-build-TOOL-dTotalRecall-36-widen-6.md](../build/2026-11-23-build-TOOL-dTotalRecall-36-widen-6.md) | widen | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-22-prompt-TOOL-dTotalRecall-36-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-36-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-36-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-36-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-36-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-36-reground-spec-writer.md) | log | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-36-fold-brief.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-36-fold-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-36-fold-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-36-fold-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |
| [2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md](../reviews/2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md) | diff-review | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 TOOL-dTotalRecall-114 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. `TOOL-dTotalRecall-19`, CLOSED
at `6ea003891`, reds every tracked Markdown record that has no `<path> -` row of the `legacy-records`
population, is not a root kind and carries no resolving `Caused-by`
(`tools/memory-tree/record_causes.py#check_causes`; a typed kind whose row's fields declare none is
graded on its Serves units, `#derive_record_cause`). That population was seeded once, shrink-only, at
its landing (`memory/project/legacy-records.txt`). Only the door writes a cause: `gov_record.py new
<kind> --caused-by <target>`, through `tools/memory-tree/build_records.py#write_new_record`, writes a
`**Caused-by:**` line under the Serves line, or a typed kind's `- **Caused-by:**` field. Every other
writer keeps writing records with no cause line after the seed, each re-read at HEAD `e0cd68745`:

- the review harness's binding line (`tools/workflows/tier2-review.template.js#renderAuditBinding`, and
  the synthesis instruction's diff-kind binding sentence beside it);
- the build harness's clean-round record line (the `pinnedLine` of
  `tools/workflows/unattended-build.template.js`'s clean-round block);
- the roles kit's prompt record head and agent ledger (`tools/roles/handoff.py#render_handoff` and
  `#write_agent_ledger`);
- the runlog run record (`tools/runlog/record.py#render_markdown`);
- the as-built view head (`tools/memory-tree/asbuilt_view.py#VIEW_HEAD`);
- the loop kit's upstream record (`tools/loop/upstream.py#write_upstream_record`), the driver's
  spec-audit chain record (`tools/unattended/unattended.sh#write_chain_round`) and the backlog
  migration's census (`tools/memory-tree/migrate_backlog.py#render_census`), the writers the census
  finds at HEAD beyond the five read at base (§8 F3).

The next record any of them writes reds `record causes (causes and orphans over the legacy population)`.
This unit makes each of those writers write `**Caused-by:**`, the run record's through the rule S4
mints and `TOOL-dTotalRecall-48` calls at order 18 (§8 F4), says so in the binding grammar a
hand-writer reads, backfills the records this run wrote between the seed and this pass, and adds a
writer census to the causes check so the next writer that omits the line is red at its own pass. It
repairs `TOOL-dTotalRecall-19`.

## 2. Scope (IN)

- **S1** — The review harness renders the cause line. `renderCauseLine(ids)` in
  `tools/workflows/tier2-review.template.js` returns `**Caused-by:** <the first id, bare>`, with any
  `@rev-<n>` pin stripped. The synthesis instruction names it as the record's second line, directly
  under the binding line, on both kinds, and its ordered-opening sentence ("THE RECORD'S OPENING IS
  ORDERED") counts it: for the spec kind it sits inside the `<<<SERVES` block the agent copies verbatim,
  and for the diff kind the instruction spells it from the first unit id of the diff.
  `tools/workflows/tier2-review.js` is re-rendered from the template by the kit's `[[regenerate]]` render
  (`tools/workflows/kit.toml`). Observed by AC1.
- **S2** — The build harness's clean-round record. The `nextAction` text of
  `tools/workflows/unattended-build.template.js`'s clean-round block, which hands the caller `pinnedLine`
  as line 1, names line 2 as `**Caused-by:** <owed[0]>`, and `tools/workflows/unattended-build.js` is
  re-rendered the same way. Observed by AC2.
- **S3** — The roles kit. `render_handoff` in `tools/roles/handoff.py` writes `**Caused-by:** <unit id>`
  on the line after the prompt record's `**Serves:**` line, ahead of any `**Load gaps:**` line, and the
  agent ledger `write_agent_ledger` creates writes `**Caused-by:** <its first id>` under its Serves line.
  Rewriting an existing ledger's Serves line keeps a cause line already present and inserts one where
  none is; a doubled one is a header `tools/memory-tree/tree_lib.py#read_header_edges` refuses, which
  `check_causes` reports as `its header is refused`. Observed by AC3.
- **S4** — The runlog run record's cause rule and the as-built view. Two functions are minted in
  `tools/runlog/record.py`. `render_cause_line(serves)` returns `**Caused-by:** <the first served id>`:
  the first of the ids sorted by `#derive_unit_key`, as `#render_serves` sorts them, bare, never the
  `N..M` run `render_serves` writes, since a cause resolves as a family id or a record key
  (`tools/memory-tree/record_causes.py#check_cause_target`) and a run is neither.
  `check_cause_line(ln, line, served)`, the sibling of `#check_serves_line`, returns that function's
  finding shape, `(ln, "cause", <why>)`, for a line that is not `**Caused-by:** <target>` and for a
  target outside `served`, the served ids, bare. This unit wires neither function into a reader or a
  writer. `#render_markdown` keeps its six-line head and `#check_record_lines` keeps its fixed head,
  both as at HEAD: wiring the check there reds `runlog record schema` on every tracked run record at
  this unit's tip, and writing the line from the render reds `runlog selftest`, whose
  `test_record_duration_derived_mark` grades a render with `check_record_lines` (§8 F4). Both wirings
  are `TOOL-dTotalRecall-48`'s at order 18: its S1 calls `check_cause_line` from `check_record_lines`
  over a head that admits the line, its S2 narrows the check to shape, and its S3 writes
  `render_cause_line`'s line from `render_markdown`. `VIEW_HEAD` in
  `tools/memory-tree/asbuilt_view.py` writes `**Caused-by:** {serves}` under its Serves line, and the
  pass re-renders the view `.memory-tree.conf`'s `DESIGN_VIEW` names through `gen_build_index.py
  --write`; `VIEW_HEAD`'s parity with its pinned instrument is `TOOL-dTotalRecall-49`'s, at order 18.
  Observed by AC4.
- **S5** — The grammar a hand-writer reads. The "Record bindings — how a record names its spec" section
  of `tools/memory-tree/HYGIENE.template.md` states that a record written after the causes seed carries
  `**Caused-by:** <target>` within the first `BIND_HEAD_LINES` lines (`tree_lib.py#BIND_HEAD_LINES`), and
  names `gov_record.py new <kind> --caused-by <target>` as the door that writes it. The render reaches
  `memory/HYGIENE.md` through `adopt-memory-tree.sh --render`. NOT OBSERVED by a criterion: a prose
  rule, held equal to its render by the `kit/dogfood doc parity` leg at the close.
- **S6** — The backfill. Every tracked `.md` record that `check_causes` reds as causeless at this unit's
  pass base (no `<path> -` row in `legacy-records`, a kind that is not a root, no `Caused-by`) gains
  `**Caused-by:** <its first Serves id>`, the id bare with any `@rev-<n>` pin cut, on the line after its
  Serves line, in this unit's pass commit. These are the records the run wrote between unit 19's seed
  and this pass, its prompt records first among them; each gains a cause `check_cause_target` resolves,
  a unit id the corpus defines. At HEAD `e0cd68745` the set is empty: `record_causes.py --check` prints
  `0 causeless` over 10668 Markdown records, 10657 of them legacy (DERIVED 2026-11-23 by AC5's
  command), so the pass derives it again at its base and an empty set backfills nothing. A non-Markdown
  record is never graded (`record_causes.py`'s docstring, "WHAT IT DOES NOT CHECK") and is
  `TOOL-dTotalRecall-51`'s. S6 inserts into no record whose own
  reader holds its head's bytes: a run record (`record.py#check_record_lines`' fixed head, until
  `TOOL-dTotalRecall-48`) and a `-chain-rounds.md` record (append-only by `check-unattended.sh`'s prefix
  rule). Each such record at the pass base is named in the pass's deviation record and left to
  `TOOL-dTotalRecall-47`'s verb; this build's folder tracks none at HEAD (DERIVED 2026-11-22,
  `git ls-files 'memory/builds/dTotalRecall/build/*-chain-rounds.md' 'memory/builds/dTotalRecall/build/*-runlog-*.md'`
  prints nothing). Observed by AC5.
- **S7** — The writer census, `check_cause_writers(root)` in `tools/memory-tree/record_causes.py`, run by
  `--check` beside `check_causes`. Its population is the alias census's: every tracked `*.py`, `*.sh` or
  `*.js` file under the tool root `record_kinds.py#derive_tool_rel` gives, read through
  `read_code_paths(root, tool_rel)`, the walk this unit extracts from `record_kinds.py#check_alias_compares`,
  which then calls it; test-named files excepted (`*.test.sh`, `selftest.py`, `test_*.py`). A census
  file spells a `**Serves:** ` literal and no `Caused-by`. It is red unless `CAUSE_WRITER_KEPT` in the
  same module keys it with a reason, for a file whose Serves literals are fixture, instruction or
  reader-prefix text only (§8 F3); each key is the file's path under the tool root, spelled in parts as
  `record_kinds.py#ALIAS_COMPARE_KEPT` spells its keys, so the install-prefix ban reads no kit path. Its
  output takes `check_alias_compares`' shape: one `cause-writer · <path>:<line> · kept <reason>` or
  `· red` line per census file at its first Serves literal, then a count line. The candidate predicate
  is run over the real tree before the constant is written, and the pass commit's `Decided:` trailer
  names each kept file. Observed by AC6.
- **S8** — The writers the census holds at HEAD beyond S1 to S4 (§8 F3). `write_upstream_record` in
  `tools/loop/upstream.py` writes `**Caused-by:** <unit>` on the line after its Serves line; where it
  still calls `re.fullmatch(ID, unit)`, which raises `TypeError` since `TOOL-dTotalRecall-5` made
  `build_records.ID` an `id_grammar.py#SlugPattern`, the pass spells it `ID.fullmatch(unit)`.
  `write_chain_round` in `tools/unattended/unattended.sh` writes `**Caused-by:** <named>` on the line
  after a new chain record's Serves line, and `derive_chain_verdict`'s head rule in the same file, which
  skips the head's `# `, Serves and `Appended by` lines before the first round row, skips a
  `**Caused-by:** ` line too, since it otherwise reads it as a malformed round row and refuses at check
  118. `render_census` in `tools/memory-tree/migrate_backlog.py` writes `**Caused-by:** <unit_id>` on
  the line after its Serves line; `render_worksheet`'s comment form stays `TOOL-dTotalRecall-53` S10's.
  Observed by AC7.

## 3. Non-goals (OUT)

- The causes check, the orphan check, the legacy population and the door's `--caused-by` and `--edge`:
  `TOOL-dTotalRecall-19`'s, landed at `6ea003891`. This unit changes no rule of theirs.
- Calling `check_cause_line` from `check_record_lines`, and writing `render_cause_line`'s line from
  `render_markdown`: `TOOL-dTotalRecall-48`'s S1 and S3 (S4, §8 F4).
- A cause richer than the first served unit. Each writer here serves a unit or an instrument, and the
  first of them is the cause the legacy reading already assumes (`TOOL-dTotalRecall-19` S8). A writer
  with a better-known cause, such as dWellOiledMachine's intake, writes that one when it lands.
- Rewriting a legacy record. S6 touches only records the population lacks.
- Proving that a census file writes the line at run time. The census grades spelling; each writer's
  own criterion grades behaviour.

### Edges

- **consumes-from** `TOOL-dTotalRecall-19` — `check_causes`, the legacy population `legacy-records`
  and the door's `--caused-by`, whose cause grammar every writer here emits and whose module the
  writer census joins
- **hands-off** `TOOL-dTotalRecall-47` — S6's backfill rule, which that unit applies as a verb at its later tip (the round-1 audit of units 36 to 43, id 3)
- **hands-off** `TOOL-dTotalRecall-48` — `render_cause_line` and `check_cause_line` in `tools/runlog/record.py`, which that unit wires into `render_markdown` and `check_record_lines`, admitting the cause line into the run record's fixed head, and narrows to shape (the round-1 audit of units 36 to 43, id 30; §8 F4)
- **hands-off** `TOOL-dTotalRecall-49` — `VIEW_HEAD`'s cause line, which that unit takes back out, and `CAUSE_WRITER_KEPT`, whose reasons it widens (the round-1 audit of units 36 to 43, id 31)
- **hands-off** `TOOL-dTotalRecall-50` — `check_cause_writers`, whose population that unit widens to the build folders' scripts (the round-1 audit of units 36 to 43, id 32)
- **hands-off** `TOOL-dTotalRecall-51` — S5's Record bindings sentence and S6's backfill, whose non-markdown records that unit gives their comment-prefixed form (the round-1 audit of units 36 to 43, id 40)
- **hands-off** `TOOL-dTotalRecall-53` — the writer census, `CAUSE_WRITER_KEPT`, AC4 and the writers `migrate_backlog.py` and the guide's record heads, which that unit extends (the round-1 audit of units 36 to 43, ids 4, 5, 14, 15, 16, 28, 29, 33, 34 and 41)
- **hands-off** `TOOL-dTotalRecall-60` — its AC4 arm in `tools/runlog/selftest.py`, rewritten to unit 48's narrowed rule at unit 48's pass (its §8 F2), which that unit's S21 finds present (the round-1 audit of units 44 to 53, id 30)

## 4. Design

### The head each writer emits

```markdown
**Serves:** spec-audit TOOL-dTotalRecall-19@rev-1 TOOL-dTotalRecall-36@rev-1
**Caused-by:** TOOL-dTotalRecall-19
# Tier-2 review: ...
```

The cause line sits directly under the binding line wherever the writer puts that line (first on a
review, a prompt record and a census; third under a title on an upstream record, a chain record and,
from `TOOL-dTotalRecall-48`'s pass, a run record). It falls inside the first
`tools/memory-tree/tree_lib.py#BIND_HEAD_LINES` unfenced lines, where `tree_lib.py#read_header_edges`
reads an untyped record's column-0 `**Caused-by:**` and refuses a key given twice. Check 21's
binding-head window (`tree_lib.py#read_bindings`) still finds the Serves line where it was. The target
is a bare unit id: `tools/memory-tree/record_causes.py#check_cause_target` resolves a family id the
corpus defines or a record key, and a pinned `@rev-<n>` token or an `N..M` run is neither.

### The census

| Census file at HEAD | Disposition |
|---|---|
| `tools/workflows/tier2-review.template.js`, `unattended-build.template.js` and their renders | S1 and S2 write the line |
| `tools/roles/handoff.py` | S3 writes the line |
| `tools/runlog/record.py` | S4 spells it in `render_cause_line` and `check_cause_line`; unit 48 writes it |
| `tools/memory-tree/asbuilt_view.py` | S4 writes the line |
| `tools/loop/upstream.py`, `tools/unattended/unattended.sh`, `tools/memory-tree/migrate_backlog.py` | S8 writes the line |
| `tools/loop/placement.py`, `tools/memory-tree/seen_red.py`, `tools/playbook/instruction_units.py`, `tools/policy/check_policy.py` | kept: fixture text |
| `tools/memory-tree/adopt-memory-tree.sh` | kept: instruction text |
| `tools/workflows/replay_scorer.py`, `tools/workflows/review_replay.py` | kept: reader-prefix, fixture and docstring text |

The table is the reading at HEAD `e0cd68745` (DERIVED 2026-11-23: the census holds 17 files, ten written
and seven kept), from `git grep -l -F '**Serves:** ' -- 'tools/*.py' 'tools/*.js' 'tools/*.sh'
':!tools/*.test.sh' ':!tools/*selftest.py' ':!tools/*test_*.py'` less each file `git grep -q -F
Caused-by` matches. The nine files that spell both are off the census, unit 19's `gov_record.py` and
`record_causes.py` among them (DERIVED 2026-11-23, the same two commands). The census itself is derived
at every run and never typed.

### Inventory

Minted: `renderCauseLine` in the review harness, `render_cause_line` and `check_cause_line` in
`tools/runlog/record.py`, `check_cause_writers`, `CAUSE_WRITER_KEPT` and the plant
`writer-without-cause` (a `record_causes.py#PLANTS` member) in `tools/memory-tree/record_causes.py`, and
`read_code_paths` in `tools/memory-tree/record_kinds.py`. Naming cells: each Python name is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass, and `renderCauseLine`
under the JavaScript cell; each leads with a `.lexicon.conf` VERBS verb (`render`, `check`, `read`).

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/roles/handoff.py`
- `tools/roles/selftest.py`
- `tools/runlog/record.py`
- `tools/runlog/selftest.py`
- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/record_kinds.py` (`read_code_paths`, extracted from `check_alias_compares`)
- `tools/memory-tree/migrate_backlog.py`
- `tools/memory-tree/check-memory-hygiene.test.sh` (the census arm)
- `tools/memory-tree/HYGIENE.template.md`
- `tools/loop/upstream.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh` (the chain-record arm)
- `memory/HYGIENE.md` (the render)
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (re-rendered by
  `gen_build_index.py --write` over S4's `VIEW_HEAD`)
- `memory/builds/dTotalRecall/prompts/` (S6's backfill)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Grade only the kinds whose writer is the door, and exempt the rest with an ask each.** It keeps
  the leg green by narrowing what P35 covers, and every review, prompt and run record of the next
  build would sit outside the rule this build lands.
- **Re-seed the legacy population at this pass.** The ledger is shrink-only (`TOOL-dTotalRecall-19`
  S7), so a re-seed is refused, and it would launder exactly the records the rule is about.
- **A second walk over the tool root's code files beside the alias census's.** It is the kind's second
  instance copied, which the charter's reuse rule refuses; the walk is extracted once (S7).
- **Write the run record's cause line from `render_markdown` at this pass.** The fixed head refuses
  its line 4 until `TOOL-dTotalRecall-48`, so `runlog selftest` reds at this unit's tip (§8 F4).

## 5. Production-readiness checklist

- security — no new write surface: each writer gains one line in a file it already writes.
- perf / scale — the census is one walk over the tool root's tracked code files per check run, the
  alias census's walk.
- error / empty / loading states — a census file with no reason in `CAUSE_WRITER_KEPT` is red and
  named; a count line with no red is a pass, because every writer was found and each writes the line.
- observability — `--check` names each census file and its first Serves literal's line.
- risks — the census grades spelling, so a writer that spells `Caused-by` in a comment and never
  writes it passes the census; the causes check itself still reds the record it writes. Between this
  pass and `TOOL-dTotalRecall-48`, a run record `render_markdown` writes carries no cause, and the
  causes leg reds it; the driver writes one at its close (`tools/unattended/unattended.sh#write_run_record`),
  after order 18. Between this pass and `TOOL-dTotalRecall-49` the view's cause line departs from its
  instrument.
- testing — AC1 to AC7 by the pass; the arms of §7 at the close.
- migration — S6's backfill of this run's own records, nothing landed.
- user docs — none under `help/`: no page covers record heads; `memory/HYGIENE.md` carries S5.

## 6. Acceptance criteria

- **AC1** — When a `node -e` probe loads `tools/workflows/tier2-review.js`'s body with
  `new Function(...)` and returns `renderCauseLine`, as the TOOL-dTrueNorth-5 AC2 arm of the review
  harness's self-test loads `renderAuditBinding`, the call over the ids
  `TOOL-x-1@rev-2` and `TOOL-x-2` returns `**Caused-by:** TOOL-x-1`; and
  `grep -c "Caused-by" tools/workflows/tier2-review.js` counts the instruction text on both kinds'
  branches.
  Red when: the pin is kept on the target, or the diff kind's instruction names no cause line.
- **AC2** — When `grep -n "Caused-by" tools/workflows/unattended-build.js` runs at the pass tip, the
  clean-round `nextAction` text names line 2 as the cause line beside `pinnedLine`.
  Red when: the clean-round record the caller writes is instructed with the binding line alone.
- **AC3** — When `python tools/roles/handoff.py` writes a prompt record for a fixture unit in a
  scratch clone under the system temp directory, the line after its Serves line is
  `**Caused-by:** <the unit id>`, the fixture spec's id, the resolving cause; when the agent ledger is
  created and then rewritten with a second id, `grep -c "Caused-by"` over it prints `1`, its cause
  the first id.
  Red when: the rewrite path drops or doubles the cause line.
  fixture: a scratch clone with one build folder and one spec, whose id is the cause each record
  names; the pass makes it.
- **AC4** — When a `python -c` probe from `tools/runlog/` calls
  `record.render_cause_line(["X-xFixtureRun-2", "X-xFixtureRun-1"])`, it returns
  `**Caused-by:** X-xFixtureRun-1`, while `record.render_serves` over the same ids returns
  `X-xFixtureRun-1..2`; `record.check_cause_line` at line 4 over the served set
  `["X-xFixtureRun-1", "X-xFixtureRun-2"]` returns no finding for that line, and one finding each for
  `""` and for `**Caused-by:** X-xFixtureRun-9`; and `inspect.getsource` of `record.render_markdown`
  and of `record.check_record_lines` names neither function. When a probe from `tools/memory-tree/`
  formats `asbuilt_view.VIEW_HEAD` with `serves="FIX-y-6"`, `instrument="x"`, `sha="0"` and `count=0`,
  the text holds `**Caused-by:** FIX-y-6`.
  Red when: the cause is a run, the head check passes a head without a cause or with an unserved one,
  either function is wired into the render or the fixed head at this tip, or the view carries no cause.
  fixture: the runlog self-test's `FX_SLUG` ids, since `render_serves(["TOOL-x-1", "TOOL-x-2"])` returns
  `TOOL-x-1--0 TOOL-x-2--0` (DERIVED 2026-11-23 by a `python -c` probe from `tools/runlog/` at `e0cd68745`).
- **AC5** — When `python record_causes.py --check` runs from `tools/memory-tree/` at the pass tip, it
  prints `0 causeless`, and `git diff --stat <pass base>..HEAD` lists each record S6 backfilled, each
  one's resolving cause its first Serves id.
  Red when: a Markdown record this run wrote after unit 19's seed still carries no cause.
  figure: the backfilled set is DERIVED at the pass base by the same command; it is empty at `e0cd68745`.
- **AC6** — When `python record_causes.py --check` runs in a scratch copy of the
  tree where `tools/roles/handoff.py`'s two cause lines are cut, it exits 1 naming `handoff.py` under
  the writer census; at the pass tip the census names no file outside `CAUSE_WRITER_KEPT`; and
  `python record_kinds.py --check`'s `alias-compare` count line reads as it did at the pass base.
  Red when: the census reads only the registry's writer cells, so a writer the registry does not
  name escapes it, or the extracted walk changes the alias census's population.
  fixture: a scratch copy under the system temp directory; the pass makes it.
- **AC7** — When a `python -c` probe from `tools/memory-tree/` prints line 2 of
  `migrate_backlog.render_census("TOOL-x-1", "abc", {"corpus": [], "findings": [], "conservation": []})`,
  it prints `**Caused-by:** TOOL-x-1`; when a `python -c` probe from `tools/loop/` calls
  `upstream.write_upstream_record` over `upstream.build_fixture_repo()` with `FX_BUILD`, `FX_UNIT` and
  `FX_ITEM`, the record's line after its Serves line is `**Caused-by:**` and `FX_UNIT`
  (`FIX-dUpstream-1`, the fixture repo's unit and the resolving cause); and when
  `bash tools/unattended/unattended.sh --record-round` writes a new chain record in a scratch clone, the
  line after its Serves line is `**Caused-by:** <the named id>`, the scratch spec's id and the
  resolving cause, and `--chain-verdict` over it exits as over the same record without that line.
  Red when: a writer is kept to clear the census instead of writing the line, or the chain reader
  refuses the cause line as a round row.
  fixture: the chain half needs a scratch clone with a build folder and a spec, whose id the record
  names; the pass makes it.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `kit/dogfood doc parity` · `memory hygiene` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `policy fixtures` · `scratch-guard self-test` · `unattended kit gate` · `memory-hygiene self-test` · `record-kinds` · `backlog migration selftest` · `loop upstream fixtures` · `install-prefix (shipped surface)` · `chain-packet self-test` · `record causes (causes and orphans over the legacy population)`

The leg `record causes (causes and orphans over the legacy population)` runs `--check`, which the
census joins; it landed with `TOOL-dTotalRecall-19` at `6ea003891`. `chain-packet self-test` and
`policy fixtures` are owed by the as-built view's path, whose folder both guards name.

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC6 · the writer census plant `record_causes.py --fixture --plant writer-without-cause`, a fixture code file spelling a Serves literal and no cause, staged by cutting `check_cause_writers` from `--check` · none
New arm: tools/workflows/tier2-review.test.sh · covers AC1 · a pin on `renderCauseLine`'s output beside the `renderAuditBinding` pin, staged by returning the pinned id · none
New arm: tools/runlog/selftest.py · covers AC4 · `render_cause_line` over a run of two ids, and `check_cause_line` over a cut cause line and over an unserved cause, staged by `check_cause_line` returning no finding · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · a chain record carrying its cause line read by `--chain-verdict`, staged by cutting the head rule's `**Caused-by:**` skip · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — May this unit change `HYGIENE.template.md`, a governance carrier, to state the cause line?**
  Options: (a) yes, under the build's grant, the cause line being cl-dClosedLoop-0230's "each record's
  header (Serves, Made-by, Caused-by)"; (b) no, leaving hand-writers to learn the rule from the red.
  (b) leaves every hand-written record of the next build red with no instruction that prevents it.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 5, the grant the README's `may:` line names.
  grants: PLAY-dClosedLoop-3 HYGIENE.template.md's Record bindings section states the cause line ·
  widens: none · relaxes: none
- **F3 — The census at HEAD holds writers and a reader-prefix file §2 did not name; what disposes them?**
  Read at `ed5a7d523`: `write_upstream_record`, `write_chain_round` and `render_census` write records
  with no cause, and `replay_scorer.py`'s Serves literals are reader prefixes (`SERVES_PREFIX`,
  `SPEC_SERVES_PREFIX`) and fixtures. Options: (a) S8 makes the three writers write the line, and
  `CAUSE_WRITER_KEPT`'s reasons admit reader-prefix text beside fixture and instruction text, the reason
  `TOOL-dTotalRecall-53` S8 names for `review_replay.py`; (b) keep the writers with a fixture reason;
  (c) leave them red until a later unit. (b) keeps a file on a reason that is false, which S7 forbids;
  (c) fails AC6 at this unit's own tip. RESOLVED (agent, 2026-11-22, delegated): (a), the sole survivor,
  per `2026-11-22-prompt-TOOL-dTotalRecall-36-reground-brief`; `TOOL-dTotalRecall-53` S7 and S8 then find
  `render_census`'s line and the reason present. widens: none · relaxes: none
- **F4 — Who writes the run record's cause line, when the fixed head refuses it until
  `TOOL-dTotalRecall-48`?** `check_record_lines` grades lines 1 to 6 as fixed text, line 4 blank, and
  `runlog selftest`'s `test_record_duration_derived_mark` grades a `render_record` output with it and
  expects no finding (`tools/runlog/selftest.py#test_record_duration_derived_mark`). Options: (a) this
  unit writes the line from `render_markdown` and admits it into the head; (b) this unit mints the rule
  as `render_cause_line` and the check as `check_cause_line`, wires neither, and unit 48's S1 and S3
  wire both at order 18; (c) this unit writes the line and leaves the head to unit 48. (a) is unit 48's
  S1, which its rev-3 owns; (c) reds `runlog selftest` at this unit's tip. RESOLVED (agent, 2026-11-23,
  delegated): (b), the sole survivor, per `2026-11-23-prompt-TOOL-dTotalRecall-36-fold-brief` item 1;
  unit 48's S3 already writes "the cause line `TOOL-dTotalRecall-36` S4 gives it". widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-47, TOOL-dTotalRecall-48, TOOL-dTotalRecall-49, TOOL-dTotalRecall-50, TOOL-dTotalRecall-51, TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.
- rev-4 · 2026-11-22 · §1 · S1 to S8 · §3 · §4 · §5 · §6 AC1, AC4 to AC7 · §7 · §8 F3 added · §10 · per
  `2026-11-22-prompt-TOOL-dTotalRecall-36-reground-brief`, re-grounded at `ed5a7d523`: every line cite is
  a symbol; the census is re-derived and S8 adds its three new writers (F3); the walk is extracted from
  unit 40's alias census; S6 backfills Markdown only and leaves the run and chain records whose heads
  their readers hold; the run record's cause is never a run; AC4's view half supplies every placeholder;
  the census arm moves to `check-memory-hygiene.test.sh`; the leg line gains the legs its paths trip.
- rev-5 · 2026-11-23 · §1 · S3 · S4 · S6 · §3 · §4 · §5 · §6 AC3 to AC5, AC7 · §7 · §8 F4 added · §10 ·
  per `2026-11-23-prompt-TOOL-dTotalRecall-36-fold-brief`, re-read at `e0cd68745` over unit 19 as landed
  at `6ea003891`: S4 mints `render_cause_line` and `check_cause_line` and wires neither, unit 48 wiring
  both (F4); AC4 takes the self-test's `X-xFixtureRun` ids; the cause, header-reader and door claims
  cite unit 19's code; each criterion that writes a record names its resolving cause; Files touched
  gains the as-built view, and the leg line its two guarded legs and the record causes leg.

## 10. Reuse audit

The seams extended are the writers themselves, each at the line that already writes the binding
(`tools/workflows/tier2-review.template.js#renderAuditBinding`, the clean-round `pinnedLine` of
`tools/workflows/unattended-build.template.js`, `tools/roles/handoff.py#render_handoff` and
`#write_agent_ledger`, `tools/runlog/record.py#render_serves`, whose `#derive_unit_key` sort
`render_cause_line` reuses, and `#check_serves_line`, whose finding shape `check_cause_line` takes,
`tools/memory-tree/asbuilt_view.py#VIEW_HEAD`,
`tools/loop/upstream.py#write_upstream_record`, `tools/unattended/unattended.sh#write_chain_round` and
`tools/memory-tree/migrate_backlog.py#render_census`); `TOOL-dTotalRecall-19`'s `record_causes.py`, whose
`--check` the census joins and whose `--fixture --plant` the census plant extends; and
`TOOL-dTotalRecall-40`'s alias census, `record_kinds.py#check_alias_compares` with
`#ALIAS_COMPARE_KEPT`, `#derive_tool_rel` and `#read_tracked`, whose population walk S7 extracts as
`read_code_paths` and whose file-keyed keep map and line shape the census takes. The lookup
`python tools/codebase-map/reuse_lookup.py "census of code files spelling a literal with a kept map of reasons"`
ranked name-stem neighbours (`census` in `merge-rows.py`, `write_fixture_files`, `write_file`) and not
the alias census, found by reading unit 40's landed code; the base lookup
`python tools/codebase-map/reuse_lookup.py "record writer emits a cause header line"` ranked `write`,
`write_text`, `records` and `emit` and no writer inventory. The recall probe returned the promotion
precedent `TOOL-cMendedVintage-19` and the dSafePassage promoted specs, which place a repair after its
unit.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
