# TOOL-dTotalRecall-2 — the one `record` write door, `gov_record.py new <kind>`, grown from the record factory: minting under a claim or lease, idempotent and content-addressed, rendering and refusing

**Status:** DEFERRED · rev-11 · 2026-11-22 · node d · Tier-2 · base 462d20f3 · streams tooling · order 12 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0213@bfd195a1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-a.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-7 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-25 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md](../build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-2-deviation-22.md](../build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-22.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-2-deviation-23.md](../build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-23.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-02-build-TOOL-dTotalRecall-2-deviation-24.md](../build/2026-11-02-build-TOOL-dTotalRecall-2-deviation-24.md) | deviation | — |
| [2026-11-03-build-TOOL-dTotalRecall-2-deviation-25.md](../build/2026-11-03-build-TOOL-dTotalRecall-2-deviation-25.md) | deviation | — |
| [2026-11-03-build-TOOL-dTotalRecall-2-owner-fork-returns.md](../build/2026-11-03-build-TOOL-dTotalRecall-2-owner-fork-returns.md) | research | TOOL-dTotalRecall-1 |
| [2026-11-22-build-TOOL-dTotalRecall-2-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-2-reground-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-reground.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-4 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-15 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-43 TOOL-dTotalRecall-76 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-14 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-02-prompt-TOOL-dTotalRecall-2-1-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dTotalRecall-2-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dTotalRecall-2-owner-fork.md](../prompts/2026-11-02-prompt-TOOL-dTotalRecall-2-owner-fork.md) | research | — |
| [2026-11-03-prompt-TOOL-dTotalRecall-2-1-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dTotalRecall-2-1-spec-writer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dTotalRecall-2-owner-fork.md](../prompts/2026-11-03-prompt-TOOL-dTotalRecall-2-owner-fork.md) | research | TOOL-dTotalRecall-1 |
| [2026-11-22-prompt-TOOL-dTotalRecall-2-carries-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-2-carries-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-2-carries-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-2-carries-spec-writer.md) | log | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-2-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-2-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-2-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-2-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-1 TOOL-dTotalRecall-13 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-16 TOOL-dTotalRecall-25 TOOL-dTotalRecall-5 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-22 TOOL-dTotalRecall-3 TOOL-dTotalRecall-7 TOOL-dTotalRecall-11 TOOL-dTotalRecall-10 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-9 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-20 TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26 TOOL-dTotalRecall-12 |

<!-- /gen:spec-records -->

## 1. Goal

One write command, `record`, standing as `python gov_record.py new <kind>` the way `gov_tag.py` stands
in for `gov tag`, is the door of every record kind the registry names it the writer of: it mints the
record's id under the build's claim or lease, is idempotent and content-addressed, renders the kind's
template from its schema, and refuses an invalid value at the write boundary
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:316-346`, P30).
Today the factory's `write_record` and its six per-kind `new <kind>` doors, the two scaffolds
(`gen_build_index.py --new-build` and `--new-spec`) and runlog's `write_record` write records; none
takes its kind from the registry, nothing mints a `<seq>`, and nothing makes a replayed write a no-op.

## 2. Scope (IN)

- **S1** — The CLI `tools/memory-tree/gov_record.py`, verb `new <kind>` with `--build <slug>`,
  `--unit <id>`, `--title <text>`, `--name <stem>` (§8 F8) and repeated `--field <Name>=<value>`, a thin
  adapter over one function, `write_new_record(root, kind, build, unit, title, fields, name=None)`, in
  PLAY-dOrderedCharter-7 S7's factory `tools/memory-tree/build_records.py`. For a typed kind
  (`tree_lib.TYPED_RECORD_KINDS`) it ends in `build_records.py#write_record`, the writer every factory
  door already shares, so there is no third writer. The factory's `new <kind>` doors
  (`build_records.py#DOORS`) are untouched and stay their kinds' doors (§8 F7). The verbs `find` and
  `show` are TOOL-dTotalRecall-9's. Observed by AC1.
- **S2** — The kind's row: the door reads `<kind>`'s `[[record-kind]]` row through
  `record_kinds.py#read_record_kinds` (I1) and refuses, exit 2, a kind with no row and a kind whose
  `writer` is not `gov_record.py new <kind>`, naming that writer, since each kind has one door and the
  registry names it; a kind whose writer is a factory door, `build_records.py new <kind>`, is refused
  so, naming that door (§8 F7). Observed by AC1 and AC9.
- **S3** — Rendering: the record's text is `record_kinds.py#render_template` for the row (the
  `--template <kind>` skeleton: `# <unit id> <kind> <n> — <title>` on a factory-sourced row, else
  `# <title>`, the `**Serves:** <kind> <unit id>` line and one `- **<Key>:** ` line per field in the
  row's order, the layout `write_record` writes), each field line filled with the caller's value; a
  `--field` key the row does not name follows in the caller's order, for the kind's check to decide.
  A row whose `schema.form` is not `fields` is written only by a kind handler (S7). Observed by AC8.
- **S4** — Refusal at the write boundary: the rendered bytes are parsed back, before anything is
  written, by the predicate that grades the kind: for a typed kind the reader the factory's `read`
  verb dispatches to (`deviation_join.py#read_record` for `deviation`), that dispatch moved out of
  `build_records.py#main` into `check_typed_record(rel, text, kind)`, which the verb and the door both
  call; for any other `fields` row `record_kinds.py#derive_field_lines` over the row's fields, a missing
  or out-of-order field a finding. Any finding exits 2 naming the field and the reason, and nothing is
  written; `write_record`'s one-line-value refusal stands behind it. The door adds no validator of its
  own. Observed by AC2.
- **S5** — Content-addressed and idempotent: `derive_content_key(kind, fields, given=None)`, the formula
  of `tools/roles/handoff.py#derive_section_sha` (the first 12 hex digits of the SHA-256 of the
  LF-folded text), over the kind name, the given `--name` where the row mints none, and the field
  values in schema order. A record of the kind whose re-derived key matches is the same write: the
  door prints `exists <path>` and exits 0. A different value under an existing id is refused, naming
  the record. Observed by AC3, AC4 and AC10.
- **S6** — Minting under the build's claim or lease, by the row's `id-rule`, per §4 "Minting". The
  lease rung reads the class field §8 F6's ask adds to `--lease status`; that ask is unfiled at HEAD
  (DERIVED: `grep -c seventh memory/builds/dPlacedRequest/BACKLOG.md` prints 0), and this build's run
  files it before the pass. Observed by AC5 and AC6.
- **S7** — The two scaffolds become kinds of the door: `new build-readme <slug> --asks <IDLIST>` runs
  `gen_build_index.py#cmd_new_build` and `new spec <id> --tier 1|2 [--order <n>] [--base <sha>]` runs
  `gen_build_index.py#cmd_new_spec`, each imported, never copied, after `check_mint_authority`. Each
  takes every flag its scaffold takes (`#NEW_BUILD_USAGE`, `#NEW_SPEC_USAGE`), parsed by
  `#read_new_build_args` and `#read_new_spec_args` and passed through unchanged; each prints its
  scaffold's lines and stages what its scaffold stages (`cmd_new_build` its README and contract row,
  `cmd_new_spec` nothing, its own rule), and a `Problem` exits 2 as `refused <kind>: <why>`. A
  scaffold's own refusals, an id a spec H1 already carries and a slug `check_slug_claimed` finds, are
  its replay rule. The `writer` cells of the `build-readme` and `spec` rows become
  `gov_record.py new build-readme` and `gov_record.py new spec`. Forwarding `--new-build` and
  `--new-spec` to the door is TOOL-dTotalRecall-20's. Observed by AC4 and AC7.
- **S9** — Each registry row whose `writer` is `hand` and whose `schema.form` is `fields` (`log`,
  `research`, `design-record` and `deviation` at HEAD, DERIVED by AC9's probe, and any other the pass
  finds) takes `writer = "gov_record.py new <kind>"`, each kind read through `tree_lib.py#resolve_kind`
  (TOOL-dTotalRecall-18, CLOSED: a dependency, no edge), so `journal` is never written; a `hand` row of
  another form keeps `hand`, and the pass commit's `Decided:` trailer names the unit or kit owning its
  door (`backlog-row`: TOOL-dTotalRecall-7's ask door; `dossier`: the codebase-map kit). The view region
  is re-rendered by `record_kinds.py --write`. Observed by AC9.
- **S8** — The file `write_new_record` writes is staged with `git add`, as `cmd_new_build` stages its
  README; the door commits nothing, and prints `wrote <path>` with the content key. Observed by AC3.

## 3. Non-goals (OUT)

- The header lines `**Made-by:**` and `**Caused-by:**` and the section `**Edges:**` lines, and the
  causes and orphan checks: TOOL-dTotalRecall-19's, written through this door.
- The ask kind's acceptance at filing: TOOL-dTotalRecall-7's; the shape-run kind: TOOL-dTotalRecall-11's.
- Appending a landed record write to the change feed: TOOL-dTotalRecall-24's.
- The claim and counter refs and their writer: TOOL-dTotalRecall-3's; the slug grammar:
  TOOL-dTotalRecall-5's; the README schema: TOOL-dTotalRecall-4's.
- runlog's run record: its door is runlog's own `write_record` (`tools/runlog/record.py#write_record`),
  in a kit that does not require memory-tree, and the `run-record` row names that door, so
  `new run-record` refuses naming it (S2).
- Adopting the factory's `new <kind>` doors, whose writers compute fields no `--field` may carry
  (`build_records.py#write_red_fix`'s `Files` and `Commit`, `#write_override`'s `Value`): §8 F7.
- Editing or versioning a record in place: `new` writes a new record or replays one; a kind whose
  lifecycle is current-state is edited by its own verb.
- Generated kinds (a view, the index, symbols): written by their generators, which the registry names.

### Edges

- **consumes-from** `TOOL-dTotalRecall-1` — `record-kinds.toml` and `--template`, the rows naming each
  kind's schema, id rule, writer and check, read by `read_record_kinds`, the template `render_template`
  the door fills and the field check `derive_field_lines`
- **consumes-from** `TOOL-dTotalRecall-5` — `id_grammar.py#derive_slug_grammar`, read through
  `gen_build_index.py#read_slug_grammar`, whose `mint_re` and `record` the `build-readme` kind writes
  against
- **consumes-from** `TOOL-dTotalRecall-4` — `FRONT_MATTER_KEYS`, which the `build-readme` kind's front
  matter is validated against
- **consumes-from** `TOOL-dTotalRecall-3` — `refs/gov/claims/`, the slug claim and the ask-family
  counter the door mints under through `gov-claim.sh`, its exit table and `claimant-key` line, and
  the claim's `session` key the claim rung reads
- **hands-off** `TOOL-dTotalRecall-9` — `gov_record.py`, the door CLI that gains the `find` and `show`
  verbs
- **hands-off** `TOOL-dTotalRecall-7` — `gov_record.py`, whose `new ask` refuses an ask without its
  acceptance under `asks.acceptance`
- **hands-off** `TOOL-dTotalRecall-11` — `gov_record.py`, through which the shape-run kind's records
  are written
- **hands-off** `TOOL-dTotalRecall-19` — `gov_record.py`, which gains the header lines and the
  section edge lines, spelled `**Edges:** type=target[,target]` one per type, and the missing-cause
  refusal
- **hands-off** `TOOL-dTotalRecall-24` — `gov_record.py`, whose writes, once landed, unit 24's lander
  hook appends to the change feed through `add_feed_event`; the door appends nothing itself
- **hands-off** `TOOL-dTotalRecall-20` — `gov_record.py`, to which the `--new-build` and `--new-spec`
  shims forward, every flag passed through unchanged
- **consumes-from** external — PLAY-dOrderedCharter-7 S7/S8's `tools/memory-tree/build_records.py`,
  its `write_record`, its `read` verb's per-kind readers and its `DOORS`; TOOL-dPlacedRequest-1's build
  lease `refs/gov/leases/<slug>/build`, read from the remote by `read_claims`, and its holder read
  through TOOL-dPlacedRequest-34 S22's read-only `--lease status build <slug>`, §8 F6's pick
- **hands-off** `TOOL-dTotalRecall-43` — `gov_record.py`, its writer refusal, its hand-row rewrite, its value refusal and its mint, which that unit changes for the round-1 audit's ids 5, 8, 9, 50 and 60
- **hands-off** `TOOL-dTotalRecall-79` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 71 to 76, id 1)
- **hands-off** `TOOL-dTotalRecall-80` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 71 to 76, id 16)
- **hands-off** `TOOL-dTotalRecall-81` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 71 to 76, id 37)
- **hands-off** `TOOL-dTotalRecall-82` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 71 to 76, id 10)
- **hands-off** `TOOL-dTotalRecall-83` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 71 to 76, id 9)
- **hands-off** `TOOL-dTotalRecall-84` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 71 to 76, id 36)
- **hands-off** `TOOL-dTotalRecall-85` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 71 to 76, id 11)
- **hands-off** `TOOL-dTotalRecall-86` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 71 to 76, id 38)
- **hands-off** `TOOL-dTotalRecall-88` — `gov_record.py new deviation`, the door that batch writes every deviation record through (the round-1 audit of units 71 to 76, id 17)
- **hands-off** `TOOL-dTotalRecall-89` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 77 to 88, id 1)
- **hands-off** `TOOL-dTotalRecall-90` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 77 to 88, id 22)
- **hands-off** `TOOL-dTotalRecall-91` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 77 to 88, id 23)
- **hands-off** `TOOL-dTotalRecall-92` — `gov_record.py new deviation`, the door that batch writes every deviation and correcting record through (the round-1 audit of units 77 to 88, ids 2, 3, 5, 6, 11, 12, 15, 16, 17, 27)
- **hands-off** `TOOL-dTotalRecall-93` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 89 to 92, id 1)
- **hands-off** `TOOL-dTotalRecall-94` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 89 to 92, id 28)
- **hands-off** `TOOL-dTotalRecall-95` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 89 to 92, id 2)
- **hands-off** `TOOL-dTotalRecall-96` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 89 to 92, id 12)
- **hands-off** `TOOL-dTotalRecall-98` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 89 to 92, id 15)
- **hands-off** `TOOL-dTotalRecall-99` — `gov_record.py new deviation`, the door that unit writes its deviation records through (the round-1 audit of units 89 to 92, id 29)
- **hands-off** `TOOL-dTotalRecall-100` — `gov_record.py new deviation`, the door that batch writes every deviation, correcting, withdrawing and re-stating record through (the round-1 audit of units 89 to 92, ids 3, 4, 6, 7, 13, 19, 23, 24, 31)

## 4. Design

### The command

```
python gov_record.py new <kind> [--build <slug>] [--unit <id>] [--title <text>] [--name <stem>] [--field <Name>=<value>]...
python gov_record.py new build-readme <slug> --asks <IDLIST>
python gov_record.py new spec <id> --tier 1|2 [--order <n>] [--base <sha>]
```

| Exit | stdout | Meaning |
|---|---|---|
| 0 | `wrote <path> key <content key>` | written and staged |
| 0 | `exists <path> key <content key>` | the same write, a no-op |
| 2 | `refused <kind>: <why>` | no row, another door, an invalid value, a different value under an existing id, or no authority to mint |
| 4 | `waiting offline <ref>` | a counter mint offline under `warn` or `follow-leases`; nothing written |

A `--field` value is taken verbatim; the door never reads a value from the environment or a file the
caller did not name.

A kind whose input is not a field list takes a handler of its own inside `gov_record.py`, keyed by
the kind name in one table `KIND_HANDLERS`, with its own flags. This unit adds two, `build-readme` and
`spec`, each a forward ending in its scaffold's own write (S7); a later unit's handler
(TOOL-dTotalRecall-7's `ask`, TOOL-dTotalRecall-11's `shape-run`) ends in `write_new_record`'s mint,
idempotence and refusal path.

### Minting

The row's `id-rule` is the record's name grammar (TOOL-dTotalRecall-1's data model), and the door
mints each placeholder it holds.

| Placeholder | Minted as | Authority checked first |
|---|---|---|
| `<n>` | `write_record`'s next free `<n>` in the build's `build/` folder, opened exclusive | the build's lease or claim |
| `<seq>` of an ask id | `gov-claim.sh ask <FAMILY> <slug> --claimant <content key>` | the counter ref itself |
| `<slug>` of a build | `cmd_new_build`'s claim through `gov-claim.sh slug` (TOOL-dTotalRecall-3 S7), after `mint_re` | the slug claim itself |
| `<date>` | today, as an ISO date | none |
| `<unit id>` | the caller's `--unit`, an id the tree defines | none |
| a given id, such as a spec's | the caller's id, minted by its session | the build's lease or claim |
| none: an empty `id-rule` | the caller's `--name`, one path segment, placed in the row's `home` with `<build>` for its `builds/*/` segment (§8 F8) | the build's lease or claim |

An empty-`id-rule` write is refused, exit 2, naming `--name`, where the flag is absent, where the
placed path misses the row's `home` glob, and where a typed kind's name grammar
(`build_records.py#derive_record_name`) matches it, naming that kind, since such a path is graded by
that kind alone (`record_kinds.py`'s module docstring).

The build's authority, in order: the lease `refs/gov/leases/<slug>/build` (TOOL-dPlacedRequest-1)
held by this session, read through TOOL-dPlacedRequest-34 S22's read-only `--lease status build
<slug>` (`tools/unattended/unattended.sh#print_lease_status`), §8 F6's pick, the driver found by
`backlog.py#resolve_kit_dir`. It prints `<tail> <fleet tag> <session> <status> <verdict> <epoch>` and
the class field F6 asks for: `mine` admits, any other class refuses naming the fleet tag and session;
`lease — none` and `lease — off` read as no lease; `lease not written`, exit 2, refuses naming the
line, an unread authority never being a pass. `--claims` cannot serve: it cuts its rows to five fields
with no session (`unattended.sh#print_claims`), while a lease is `mine` only where its fleet tag and
session match (the `lease`-mode block above `unattended.sh#check_claim_writable`).
`tools/loop/placement.py#read_build_lease` makes that comparison itself over the six fields today;
F6's class field keeps this door from being its second copy. `read_claims` fetches
`refs/gov/leases/*` from the remote in one bounded fetch (`unattended.sh#read_claims`), so the lease
read is the remote's, never a local-only ref. Else the slug claim `refs/gov/claims/<slug>` whose
`session` key is this session's (TOOL-dTotalRecall-3's claim keys; TOOL-dPlacedRequest-21's claim body,
`tools/loop/claim.py#render_claim_body`, carries `session` too); a lease or claim held by another
refuses, naming the holder. A build with neither, every build opened before TOOL-dTotalRecall-3, mints
under the charter's per-session rule and prints `minted under the session rule: no claim or lease for <slug>`;
a tree where the unattended kit does not resolve prints `unarmed — no unattended kit` first.
The offline value passed to `gov-claim.sh` is `read_policy_value("leases.offline", root)` (I8), the
memory-tree kit's landed `tools/memory-tree/tree_lib.py#read_policy_value`, since TOOL-dTotalRecall-8
mints no `policy_value.py`.

The content key is the `--claimant` a counter mint passes, written as its `claimant-key:` line, so a
replayed `new` returns the id the first call minted (TOOL-dTotalRecall-3 S4); a slug claim's key is
`cmd_new_build`'s (its S7), which also keeps the mint grammar, `gov-claim.sh` checking the admit
grammar alone. Offline, nothing is queued and no provisional id returned (its §8 F7): under `refuse`
the counter's exit 2 is the door's `refused`, and under `warn` and `follow-leases` its exit 4
`waiting offline <ref>` is printed and the door exits 4, writing nothing. A remote-less clone's
`local <ref> · no remote` (its §8 F9) mints no id, so the door refuses it, exit 2, naming the line.

### Idempotence

In order: the row (S2), the render and its refusal (S4), then the listing: the door lists the kind's
home (tracked and staged files matching the row's `home`; for a typed kind those its name grammar
matches), parses each with the kind's check, and re-derives its content key. An equal key is
`exists`; a record holding the requested given id with a different key is a refusal; otherwise the
door reads the authority and mints. The key is derived from the record's fields, never stored in it,
so it is one fact in one place.

### Inventory

Minted: `tools/memory-tree/gov_record.py` with the verb `new`, its flags `--title` and `--name` and the
table `KIND_HANDLERS`; `write_new_record`, `derive_content_key`, `check_mint_authority` and
`check_typed_record` in `build_records.py`. Naming cells: each function was asked of the lexicon's
`--suggest` under `--as py.function` on 2026-11-22 and printed `OK`. The module is never named
`record.py`, which would collide with `tools/runlog/record.py`.

### Migration

None. Every record already written keeps its form; the door writes new ones. The rows of kinds the
door writes at this pass are read from the registry and named in the pass commit's `Decided:` trailer.

### Files touched (estimate)

- `tools/memory-tree/gov_record.py` (new; shipped by the kit's `include = "**"` engine rule in
  `tools/memory-tree/kit.toml`, so no `[[files]]` row)
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/record-kinds.toml` (the `writer` cells of `build-readme`, `spec` and S9's rows)
- `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` (the `gen:record-kinds` region, whose
  `Writer` column `record_kinds.py --write` re-renders)
- `tools/memory-tree/check-memory-hygiene.test.sh` (the arms of §7)
- `tools/memory-tree/README.md` (the door's usage)

### Alternatives rejected

- **A new module beside the factory.** The factory is the record writer's second instance; a third
  writer is a copy (scout A, Shared 2).
- **Validate values with a schema validator of the door's own.** The kind's check already refuses a
  bad record; a second validator can disagree with it. Round-tripping through the check makes the
  write boundary and the gate one predicate.
- **Store the content key in the record.** A stored key is typed beside the fields it describes and
  can go stale under a hand edit; the door re-derives it.
- **Import `derive_section_sha` from the roles kit.** memory-tree requires no kit; the door uses the
  same formula over its own input, named `derive_content_key`.

## 5. Production-readiness checklist

- security — the door is the write boundary for authored record structure: every value is checked by
  the kind's own check before a byte is written, a kind's door is enforced from the registry, minting
  checks the build's lease or claim and refuses another holder, and the door commits nothing.
- perf / scale — one listing of the kind's home per call; a build's `build/` folder holds at most a
  few hundred records.
- error / empty / loading states — every refusal names the kind and the cause, and writes nothing; a
  missing registry refuses naming `record-kinds.toml`.
- observability — every call prints the path and the content key.
- risks — a legacy build mints under the session rule, which is today's rule; the named line says so.
- testing — AC1 to AC10 by a pass; the arms of §7 at the close.
- migration — none, as §4 says.
- user docs — the kit README names the door. The pages under `help/` showing a record command show
  the factory's doors (`help/charter.md`, `help/loop.md`, `help/red-fix-lane.md`), which stay those
  kinds' doors (§8 F7), so none goes stale; no page shows a write of a kind this door takes.

## 6. Acceptance criteria

- **AC1** — When `python gov_record.py new nosuch` runs in a scratch clone, it exits 2 naming
  `record-kinds.toml`; when the clone's registry row for a planted kind `planted` names
  `writer = "runlog"`, `gov_record.py new planted` exits 2 naming `runlog`.
  Red when: an unregistered kind, or a kind with another door, is written.
- **AC2** — When `gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-2 --title t`
  runs in a scratch clone with `--field Risk=bogus` and the other required fields, it exits 2 naming
  `Risk`, and `git status --porcelain` is empty.
  Red when: the value reaches disk, or a validator other than the kind's check decides.
- **AC3** — When the same complete `gov_record.py new deviation` call runs twice in a scratch clone,
  the first prints `wrote` and stages one file, and the second prints `exists` with the same path and
  key, and the clone holds one new file.
  Red when: a replay writes a second record.
- **AC4** — When the call runs a third time with one field changed, it writes a second record whose
  `<n>` is one higher; and when `gov_record.py new spec TOOL-dTotalRecall-2` runs in a scratch clone of
  the pass tip whose remote holds no lease or claim, it exits 2 naming the existing spec.
  Red when: a different value overwrites a record, or an existing id is re-written.
- **AC5** — When the fixture's bare remote holds the lease `refs/gov/leases/xLeased/build` held by
  another session, `gov_record.py new deviation --build xLeased …` run in a clone of it exits 2 naming
  the holder; with no lease and the claim ref `refs/gov/claims/xLeased` carrying this session's
  `session` it writes; with neither it writes and prints `minted under the session rule`.
  Red when: the door mints without reading the build's authority, or a lease the remote holds is
  missed because only the clone's refs are read.
- **AC6** — When a fixture registry row `planted-ask` whose `id-rule` is `<FAMILY>-<slug>-<seq>.md` is
  written twice with equal fields through `gov_record.py new` against a bare fixture remote under
  `%TEMP%/<short>`, both calls print the same id and the counter ref's tip moves once.
  Red when: the content key is not passed as the claimant, so a replay mints twice.
- **AC7** — When `gov_record.py new spec TOOL-xNew-1` runs in a fixture clone holding build `xNew`, the
  written file is byte-equal to what `gen_build_index.py --new-spec TOOL-xNew-1` writes in a twin
  clone; and `gov_record.py new build-readme dLoop --asks <IDLIST>` against a fixture remote writes the
  README with its `slug-grammar:` line and creates `refs/gov/claims/dLoop`.
  Red when: the door copies a scaffold instead of calling it, or skips the claim.
- **AC8** — When `python tools/memory-tree/build_records.py read <path>` reads the record AC3 wrote, it
  exits 0, and the file's first `**Serves:**` line is `**Serves:** deviation TOOL-dTotalRecall-2`.
  Red when: the template the door renders fails its own kind's check.
- **AC9** — When a probe reads `record-kinds.toml` with `tomllib` at the pass tip, no row whose
  `schema.form` is `fields` has `writer = "hand"`, and the `research`, `log` and `deviation` rows'
  writers are `gov_record.py new <kind>`; each row whose writer is `build_records.py new <kind>` keeps
  it, and `gov_record.py new exception` exits 2 naming `build_records.py new exception`.
  Red when: a kind the door can write is still registered as hand-written, or the door writes a kind
  whose factory door computes its fields.
- **AC10** — When `gov_record.py new research --build dTotalRecall --unit TOOL-dTotalRecall-2 --title t
  --name 2026-11-22-build-TOOL-dTotalRecall-2-probe` runs in a scratch clone, it writes that stem's
  `.md` in the clone's `dTotalRecall` `build/` folder, whose first `**Serves:**` line is `**Serves:** research TOOL-dTotalRecall-2`; the same call with no `--name` exits
  2 naming `--name`, and with `--name 2026-11-22-build-TOOL-dTotalRecall-2-deviation-9` exits 2 naming
  `deviation`.
  Red when: a record of a row with no name grammar is written under a name the door invented, or under
  a typed kind's grammar.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `record-kinds` · `build-index selftest` · `verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `routed-commits selftest` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 · the door's arms, each a `gov_record.py new` call in a scratch clone over a bare remote, AC7's twin clones among them, staged by dropping the key comparison, the authority read and the `--name` grammar test in turn · none

## 8. Open questions

- **F1 — Is `record` a new module or the factory grown?** Options: (a) `gov_record.py` as a thin CLI
  over a function in PLAY-dOrderedCharter-7 S7's `build_records.py`, its `new` verb calling the same
  function; (b) a new writer module. (b) is a third writer. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 1, the layer's "It extends the writers that exist" (`layer-memory.md:343-346`) and the
  brief's I2. widens: none · relaxes: none
- **F2 — What validates a value?** Options: (a) the kind's own check over the rendered bytes; (b) a
  schema validator in the door. (b) can disagree with the check that grades the same record later.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich: one predicate at write
  and at the gate. widens: none · relaxes: none
- **F3 — A build opened before claims exist has no claim and no lease.** Options: (a) mint under the
  per-session rule with a named line; (b) refuse. (b) makes the door unusable for every build in the
  tree today, this one included. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3; the per-session
  rule is the charter's `[ids]` rule these builds were minted under; the departure from the clause's
  "under the build's claim or lease" is recorded beside this spec as deviation 21
  (`2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md`). widens: none · relaxes: none
- **F4 — Does the door write runlog's run record?** Options: (a) no: the registry names runlog's
  `write_record` as that kind's door, and `new run` refuses naming it; (b) yes, by importing runlog.
  (b) makes memory-tree depend on a kit it does not require. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 1, the layer's "Each kind has one door, and the registry names it" (`layer-memory.md:348`).
  widens: none · relaxes: none
- **F5 — The parents are specced and not built.** PLAY-dOrderedCharter-7's factory and the lease
  reader are DEFERRED at `462d20f3`. RESOLVED (agent, 2026-10-26, delegated): this spec calls them as
  their specs name them, and the build run re-grounds on the landed code, rung 1 (the brief's chain
  rule). widens: none · relaxes: none
- **F6 — Through which surface does the door read whether this session holds the build lease?**
  `--claims` prints five fields and no session (`unattended.sh#print_claims`), and no
  read-only verb of that unit prints a lease's `session`. Options: (a) an ask to dPlacedRequest for a
  holder verb over `read_claims`, printing a lease's `fleet-tag`, `session` and its `lease`-mode class
  (`mine` or foreign), the five-field `--claims` shape kept; (b) an ask for a `session` column on
  `--claims`, which breaks that unit's AC10 and the shape TOOL-dDeclaredLoop-8 S7 extends; (c) the
  door parses the lease commit's `session:` key itself, a second parser of the record its S2 keeps in
  `read_claims`; (d) `--claims`' node column alone, so two sessions of one node both mint under one
  lease. Recommendation: (a). RESOLVED (owner, 2026-11-03): (a), served by TOOL-dPlacedRequest-34
  S22's `--lease status`, narrowing the owner's 2026-11-02 pick of (a) as one new read-only holder
  verb over `read_claims` widened by `epoch`, whose `epoch` served TOOL-dWellOiledMachine-6 §8 F4,
  resolved by the owner on 2026-10-29 to a read-only `epoch` verb over `read_claims` naming this
  verb as its best home. The holder verb is S22's `--lease status build <slug>`, read-only, printing
  one TAB line `<tail> <fleet tag> <session> <status> <verdict> <epoch>`, or `lease — none · <tail>`
  (`unattended.sh#print_lease_status`, landed): it carries `fleet-tag`, `session` and `epoch`,
  and lacks the class. The ask narrows to one column, a seventh TAB field holding the `lease`-mode
  class (`mine` or foreign, the block above `unattended.sh#check_claim_writable`), appended after `<epoch>`; the six-field
  prefix stays, since `read_lease_epoch` (DEPL-dShippedRelease-138 S48) reads the sixth field. One
  ask, filed once by this build's run, which builds before dWellOiledMachine, serves this unit's S6
  and §4 "Minting", TOOL-dWellOiledMachine-58 S4 (c) and S5, TOOL-dWellOiledMachine-41 S2's driver
  check and TOOL-dWellOiledMachine-6 S6 and S7. The row the build run files in dPlacedRequest's
  `BACKLOG.md`: "a seventh TAB field on TOOL-dPlacedRequest-34 S22's `--lease status`, the lease's
  `lease`-mode class (`mine` or foreign), the six-field prefix kept". The pass builds the lease rung
  of §4 "Minting" against `--lease status` and parses no lease commit itself.
  widens: the `--lease status` class column · relaxes: none
- **F7 — Does the door write a kind whose writer is a factory door?** At HEAD six rows name
  `build_records.py new <kind>` (`build_records.py#DOORS`), and their writers compute fields from git and
  policy (`#write_red_fix`'s `Files` and `Commit`, `#write_override`'s `Value`); the `deviation` row the
  admit clause meant is `hand` (TOOL-dTotalRecall-1 landed it so). Options: (a) admit each and forward
  its flags to the factory's `new`, a second command writing one kind with no content key behind it;
  (b) refuse each naming its door, as any other door is refused; (c) write it from `--field`, skipping
  the computed fields. (c) widens a write surface past the kind's checks. RESOLVED (agent, 2026-11-22,
  delegated): (b), the most feature-rich survivor, tie-broken by fewer open questions: one door per
  kind, the registry naming it (`layer-memory.md:348`), and no replay gap. widens: none · relaxes: none
- **F8 — How is a record of a `fields` row with an empty `id-rule` named?** `log`, `research` and
  `design-record` carry `id-rule = ""` and are no typed kinds, so `write_record` refuses them and no
  grammar mints their names. Options: (a) a given name, `--name <stem>`, checked against the row's
  `home` and every typed kind's name grammar, the minting table's given-id row; (b) the door invents a
  grammar per row, a second minter beside `tools/roles/handoff.py`'s for prompts; (c) S9 leaves those
  rows `hand`, failing AC9. RESOLVED (agent, 2026-11-22, delegated): (a), (c) vetoed by AC9 and (b)
  leaving more open; the key takes the name (S5), so two records serving one unit differ.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 2, the brief's shared interfaces I1 to
  I4 and I8, scout A's row for cl-0213, and the scaffolds read at `fb872a37e`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved. The Carries pin re-pinned from `09982ca6` to `bfd195a1`, the hash the as-built view gives cl-dClosedLoop-0213 once deviation 21 states its whole clause as After.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-79, TOOL-dTotalRecall-80, TOOL-dTotalRecall-81, TOOL-dTotalRecall-82, TOOL-dTotalRecall-83, TOOL-dTotalRecall-84, TOOL-dTotalRecall-85, TOOL-dTotalRecall-86, TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-89, TOOL-dTotalRecall-90, TOOL-dTotalRecall-91, TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.
- rev-5 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-93, TOOL-dTotalRecall-94, TOOL-dTotalRecall-95, TOOL-dTotalRecall-96, TOOL-dTotalRecall-98, TOOL-dTotalRecall-99, TOOL-dTotalRecall-100, each the other end of an edge a
  unit the round-1 spec audit of units 89 to 92 promoted wrote; nothing else moved.
- rev-6 · 2026-10-26 · §2 S2, S9 · §3 the external edge · §4 "Minting" · §6 AC5, AC9 · §8 F6 added ·
  the parents' re-ground, rows 8 and 9 of `2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md`:
  the lease holder is read through the verb F6 asks for, never `--claims`, and AC5 plants the lease on
  the bare remote; S2, S9 and AC9 follow unit 1 rev-4, whose `deviation` row names the factory.
- rev-7 · 2026-11-02 · §3 the external edge · §4 "Minting" · §8 F6 · F6 resolved by the owner to (a),
  per the brief `2026-11-02-prompt-TOOL-dTotalRecall-2-1-spec-writer`: the holder verb is the picked
  route, widened by `epoch` for TOOL-dWellOiledMachine-6 §8 F4, and the fork holds the ask's row.
- rev-8 · 2026-11-03 · §3 the external edge · §4 "Minting" · §8 F6 · the owner re-picked F6 on
  2026-11-03, per the brief `2026-11-03-prompt-TOOL-dTotalRecall-2-1-spec-writer`: the holder is read
  through TOOL-dPlacedRequest-34 S22's `--lease status build <slug>`, the ask narrows to a seventh TAB
  field holding the `lease`-mode class, the six-field prefix kept, and the ask serves S6 and §4
  "Minting", not S2 and S9.
- rev-9 · 2026-11-22 · §3 Edges · §4 "Minting" · §7 · per
  `2026-11-22-prompt-TOOL-dTotalRecall-16-unit8-edges-brief`: the `consumes-from TOOL-dTotalRecall-8`
  bullet is deleted, since that unit mints no `policy_value.py`, and §4 "Minting" names the landed
  `tree_lib.py#read_policy_value` as the read; the leg line gains `policy fixtures`, whose guard
  `tools/memory-tree/build_records.py` trips. No criterion moved.
- rev-10 · 2026-11-22 · §1 · §2 S1 to S9 · §3 · §4 · §5 · §6 AC2, AC4 to AC9, AC10 added · §7 · §8 F6
  citations, F7 and F8 added · §10 · per `2026-11-22-prompt-TOOL-dTotalRecall-2-reground-spec-writer`:
  re-grounded on HEAD `803a3b802`. The landed factory's `write_record` and `DOORS` replace the planned
  `new` verb (F7); `log`, `research` and `design-record` take a given `--name` (F8); the forwards keep
  their scaffolds' staging and replay refusals; the claim rung reads `session`; the counter's replay,
  offline and no-remote answers follow TOOL-dTotalRecall-3 rev-4 (exit 4 added); `deviation` is `hand`
  at HEAD, so S9 moves it; code citations re-pointed to `#symbol`; the arms move to the memory-hygiene
  self-test and the leg line gains the legs the touched files' guards name.
- rev-11 · 2026-11-22 · §4 "Minting" · per `2026-11-22-prompt-TOOL-dTotalRecall-2-carries-spec-writer`:
  the paragraph is rewrapped so cl-dClosedLoop-0213's token `minted under the session rule: no claim or lease for <slug>`
  stands whole on one line, as the clause carries it; no word changed.

## 10. Reuse audit

The seam extended is PLAY-dOrderedCharter-7 S7's record factory `tools/memory-tree/build_records.py`,
landed: its field grammar `#FIELD` and kind table `#KINDS`, the shared writer `#write_record` the door
ends in, and the `read` verb's per-kind dispatch in `#main`, moved into `check_typed_record` for the
door and the verb both (the deviation reader `deviation_join.py#read_record` among them); with
`record_kinds.py#read_record_kinds`, `#render_template` and `#derive_field_lines` (TOOL-dTotalRecall-1),
the two scaffolds `gen_build_index.py#cmd_new_build` and `#cmd_new_spec` called as kinds, and the
content-key formula of `tools/roles/handoff.py#derive_section_sha`. The lookup,
`python tools/codebase-map/reuse_lookup.py "write a typed record from a schema idempotently and refuse invalid field values"`,
listed `write_record`, `render_record` and `check_records` (`tools/runlog/record.py#write_record`,
`#render_record`, `#check_records`) and `read_records` (`deviation_join.py`); runlog's writer stays its
own kind's door (§8 F4). The recall probe returned scout A's row, the layer's `[contract]` and the
brief's I2; scout A's lines held at `fb872a37e`, and every citation above was re-read at `803a3b802`.

Recall terms used: `python tools/memory-recall/query.py "which command writes typed memory records idempotently from a schema" --terms "record door build_records new kind content key derive_section_sha idempotent template schema refuse mint"`
