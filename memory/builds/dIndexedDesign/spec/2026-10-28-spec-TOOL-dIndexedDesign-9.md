# TOOL-dIndexedDesign-9 — spec sections named by tag across tiers: one heading rule, one reader and its twins, and the tagged canon behind a cutoff

**Status:** OPEN · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 1 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0391@17b40187 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-c.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-c.md) | research | TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

A spec's section number means a different section on each tier: Tier-1 drops `Production-readiness
checklist`, so its Acceptance criteria is `## 5.`, its Open questions `## 7.` and its Revision log
`## 8.` (`memory/TEMPLATE-SPEC.md:172-207`), and two live readers still read the number's value and
misread every Tier-1 spec (gap-design-10). This unit names each section by a tag that survives
reordering and tier, `## [section.<seg>] <Title>`, gives the memory-tree kit one reader of a section by
tag, moves every reader of the spec format onto that rule, and lets the canon demand tags from a dated
cutoff, with both heading forms readable while the corpus migrates (walkthrough D3, :466-467; CV2,
:813, :826-832; v2 P11, :895-899).

## 2. Scope (IN)

Every reader below accepts BOTH heading forms always; only the canon and the skeleton writer read the
cutoff. Base line numbers are at `57bc3b91`, where `tools/` and `skills/` are byte-identical to the
scout's reading at `66934d2d4`.

- **S1** — The heading rule and the tag table, in `tools/memory-tree/design_lib.py` beside
  `read_spec_edges` (:543). `SPEC_SECTION_TAGS`, one row per canonical title: `Goal` `section.goal`,
  `Scope (IN)` `section.scope`, `Non-goals (OUT)` `section.non-goals`, `Design` `section.design`,
  `Production-readiness checklist` `section.readiness`, `Acceptance criteria` `section.acceptance`,
  `Gates` `section.gates`, `Open questions` `section.open-questions`, `Revision log`
  `section.revision-log`, `Reuse audit` `section.reuse-audit`. A line is a section heading when it is
  `## <n>. <Title>` with `<n>` any ordinal, or `## [section.<seg>] <Title>` with `section.<seg>` the
  tag the table gives `<Title>`; a tagged heading whose tag is not its title's is no section heading.
  Observed by AC1.
- **S2** — The reader, shared interface I1: `read_spec_headings(text)` returns `[(line, tag, title)]`
  for every section heading outside a fence (`tree_lib.unfenced_lines`), a trailing CR stripped; and
  `read_spec_section(text, tag)` returns the body of the FIRST heading carrying `tag`, up to the next
  `## ` line, or None when none does, a duplicate later heading never read. The ordinal's value is
  never read. CLI: `design_lib.py --section <tag> <path>...` prints each file's body or
  `design-lib: <path> has no <tag> section`, exit 1 when any has none; `design_lib.py --section-table`
  prints the table, one `<tag> <title>` line per row. Observed by AC1 and AC2.
- **S3** — The cutoff, `SPEC_TAGS_CUTOFF` in `.memory-tree.conf`, blank meaning off, declared blank in
  this repo and in `tools/memory-tree/.memory-tree.conf.example` with its comment (§8 F1). At or after
  it by FILENAME date, check 12's Tier-2 canon compare (`check-memory-hygiene.sh:1901-1919`, compared
  at :2631-2633, diffed at :2738) wants the TAGGED canon, built once per run from `SPEC_CANON10`
  (or `SPEC_CANON` before `SPEC10_CUTOFF`) and the table `design_lib.py --section-table` prints, and
  the Tier-1 arm (:2479-2495) takes only tagged headings as canonical; before it, both arms are
  byte-for-byte today's. A spec mixing the two forms is red on either side of the date. Observed by AC3.
- **S4** — The hygiene engine's title-keyed sites accept the tagged form of their own title, each
  spelling its title and tag pair inside the awk program as a regex literal: :2091, :2156, :2157,
  :2164, :2275, :2317, :2346, :2347, :2481, :2488, :2490, :2519, :2559, :2613, :3306, and the §10
  evidence arm at :2698, which today matches `## 10.` alone. Observed by AC4.
- **S5** — The unattended kit's twins: `plan_state`'s four section matches
  (`tools/unattended/unattended.sh:4492-4495`) and `read_consumes_from`'s Non-goals match
  (`tools/unattended/lib-unattended.sh:364`) accept `## [section.<seg>] <Title>` for their titles,
  spelled as regex literals inside the awk so the slice the marker-contract harness lifts carries them
  (the comment at `unattended.sh:4438-4443`). `plan_state` keeps its one-token contract. Observed by
  AC5.
- **S6** — The Python twins outside memory-tree, each a regex keyed on its title and tag pair:
  `extract_open_questions` (`tools/runlog/model.py:1444-1453`), which reads `## 8.` and so returns a
  Tier-1 spec's Revision log; `S10_RE` (`tools/memory-recall/check-recall.py:447`); `_SEC10`
  (`tools/codebase-map/replay-phrases.py:139`). Observed by AC6 and AC8.
- **S7** — `tools/workflows/review_replay.py` keys a section by tag: `SECTION_REF` (:67) also reads
  `[section.<seg>]`; `ITEM_SECTIONS` (:70) maps `S`, `AC` and `F` to `section.scope`,
  `section.acceptance` and `section.open-questions`; a numeric `§<n>` or `section <n>` maps through the
  ordinals of the subject spec at its pinned blob, read from the record's `Reviewed:` line
  (`extract_subject_pins`), and through the Tier-2 canon only when that blob is unreadable, which the
  candidate line says. Observed by AC7.
- **S8** — The memory-tree and repo-root Python readers accept the tagged form: `GATES_HEAD` and
  `AC_HEAD` (`tools/check-spec-tokens.py:343`, :365) and `read_spec_edges`' Non-goals match
  (`design_lib.py:557`), each through `read_spec_headings`. Observed by AC8.
- **S9** — `gen_build_index.py --new-spec`: `render_spec_skeleton` (:8617) writes each skeleton
  heading as `## [section.<seg>] <Title>` when today's date is at or after `SPEC_TAGS_CUTOFF`, the tag
  read from `SPEC_SECTION_TAGS`, and refuses a skeleton title the table lacks; blank or before, it
  writes today's numbered headings. Bodies stay keyed by `SPEC_TITLE_NUMBERS` (:8589). Observed by AC9.
- **S10** — The prompt texts name sections by tag: the five `SPEC_LENSES` briefs and the finding
  address example (`tools/workflows/tier2-review.template.js:814-834`, :1206, e.g. "a `[section.scope]`
  item no `[section.acceptance]` criterion observes", address `[section.scope] S5`) and the three spec
  writer lines of `tools/workflows/unattended-build.template.js` (:908, :911, :994); the renders
  `tier2-review.js` and `unattended-build.js` re-rendered. Observed by AC10.
- **S11** — Contract 3 in `tools/memory-tree/marker-contract.test.sh`, the agreement the twins cannot
  get by import: one case table of headings, each with the tag it is or `none`, run through
  `read_spec_section`, the sliced `plan_state` and `read_consumes_from`, the Python twins of S6 and the
  hygiene engine over a fixture repo, each reader's verdict compared per row. Rows: the ten numbered
  titles at Tier-2 ordinals, the Tier-1 ordinals, the ten tagged headings, a tag naming another
  title's section, a tagged heading with an ordinal too, an unknown tag, an indented heading and a
  fenced one. Observed by AC11.
- **S12** — The format document: `tools/memory-tree/SPEC-TEMPLATE.template.md` gains a section
  `SPEC_TAGS_CUTOFF — sections named by tag` stating the heading rule, the table by pointer to
  `design_lib.py --section-table`, that readers take both forms, and what the cutoff moves;
  `memory/TEMPLATE-SPEC.md` is its render. Observed by AC12.

## 3. Non-goals (OUT)

- Readers of other documents: the protocol's section 8 and 13 (`check-unattended.sh:3247`, :3447,
  :3450) and the charter's first section (`tools/roles/roles_lib.py:61`). They belong to P11's wider
  migration, not to the spec format.
- Arming `SPEC_TAGS_CUTOFF` in this repo, and any change to the section SET: `TOOL-dIndexedDesign-7`
  redesigns the format, trials it and arms the cutoff (§8 F1).
- Retagging a landed spec: specs dated before an armed cutoff keep the numbered canon and are never
  retrofitted (`TEMPLATE-SPEC.md:11-12`).
- `SPEC_TITLE_NUMBERS`: it keys skeleton bodies by title and reads no spec, and TOOL-dTotalRecall-43
  S25 holds a parity arm against it. Unchanged.
- The dead `SEC` and `extract_section` (`check-spec-tokens.py:314`, :514), which nothing calls: no
  reader, so no misread. Untouched.
- TOOL-dTotalRecall-9's section table (its §4, keyed `heading = "1. Goal"`): never edited here; §8 F3
  states the ask.
- Renaming `§<n>` references in prose records: positional prose is the convergence build's.

### Edges

- **hands-off** `TOOL-dIndexedDesign-12` — `read_spec_section`, with `read_spec_headings`, which names the section each `**Edges:**` line sits under
- **hands-off** `TOOL-dIndexedDesign-7` — `read_spec_section`, the tag table and `SPEC_TAGS_CUTOFF`, which the redesigned canon arms after its trial
- **hands-off** `TOOL-dIndexedDesign-6` — `read_spec_section`, the reader its interface and scope axes read sections through
- **hands-off** `TOOL-dIndexedDesign-8` — `read_spec_section`, the reader its feature-interface section is read through
- **hands-off** `TOOL-dIndexedDesign-4` — `read_spec_section`, the reader of the `section.reuse-audit` body its §10 arm checks
- **hands-off** `TOOL-dIndexedDesign-20` — `read_spec_section`, the reader its inventory join reads an amending spec's `section.goal` and `section.scope` through
- **consumes-from** external — the README `may: PLAY-dClosedLoop-3` grant for the format document (§8 F2); nothing unbuilt
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 7, 8, 11, 12, 26, 35, 36 and 42, each a scope item of that batch unit

## 4. Design

### The heading rule, once

```
section heading = "## " ( <ordinal> ". " | "[" <tag> "] " ) <Title> [ws] CR?
  <ordinal>     any digits; its value is never read
  <tag>         SPEC_SECTION_TAGS[<Title>]; any other tag makes the line no section heading
first occurrence of a tag binds; a heading inside a fence is not a heading
```

`## [section.acceptance] Acceptance criteria` and `## 5. Acceptance criteria` are the same section on
any tier. `## [section.gates] Acceptance criteria` is neither section, so a mistyped tag reads as a
missing section and THIN or check 12 says so, rather than one reader taking it by tag and another by
title. `## 6. [section.acceptance] Acceptance criteria` is no heading of either form.

### Why twins and not one import

The unattended kit grades sections in awk, and the marker-contract harness slices `plan_state` out of
the shipped bytes (`marker-contract.test.sh:281-284`), so its rule must be a literal inside the slice.
runlog, memory-recall, codebase-map and workflows are other kits; a kit does not import a sibling
(PLAY-dOrderedCharter-7 §4, "The policy reads"). Each twin spells its own title and tag pair, so no
twin carries the table, and contract 3 is the agreement: it is where the rule lives as data, the way
contract 2 holds the section-8 mark (`marker-contract.test.sh:247-275`).

### The canon under the cutoff

```
SPEC_TAGS_CUTOFF blank or later than the filename date:
  Tier-2: SPEC_CANON / SPEC_CANON10 exactly, as today      Tier-1: numbered titles, as today
SPEC_TAGS_CUTOFF at or before the filename date:
  Tier-2: each canon line "## <n>. <Title>" written "## [<tag>] <Title>"
  Tier-1: the eight titles in canonical order, each tagged, readiness and reuse audit optional
```

The table reaches the engine through ONE `"$_PY" design_lib.py --section-table` call per run, made
only when the key is set; the engine already resolves `_PY` (`check-memory-hygiene.sh:492`). A failed
call with the key set is a refusal naming the key, never a silent fall back to the numbered canon.

### review_replay's key

A finding address `x.md:§5 AC2` on a Tier-1 subject and `x.md:AC2` were two keys, 5 and 6, so a
known finding and its candidate never matched. Both are now `section.acceptance`: the item kind maps by
tag, and the number maps through the subject's own headings at the blob its `Reviewed:` line pins.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `SPEC_SECTION_TAGS` | Python constant, `design_lib.py` | none, no `py.constant` cell is declared |
| `read_spec_headings`, `read_spec_section` | Python functions, `design_lib.py` | `py.function` |
| `--section`, `--section-table` | flags of `design_lib.py` | none |
| `SPEC_TAGS_CUTOFF` | `.memory-tree.conf` key | none |
| the ten `section.*` tags | heading tags | none |

### Migration

None forced. Every reader takes both forms from this unit on, so a spec of either form reads the same.
The canon and the skeleton move only when `SPEC_TAGS_CUTOFF` is set, forward from its date.

### Rollout

One pass: reader and table, the twins, contract 3, then the canon arm and the skeleton writer behind the
blank key, then the prompts and the template. Each step leaves the tree green, because the key ships
blank.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S1, S2, S8
- `tools/memory-tree/check-memory-hygiene.sh`: S3, S4, and `KIT_MEMORY_TREE_VERSION`
- `tools/memory-tree/check-memory-hygiene.test.sh`: S3, S4 fixtures
- `tools/memory-tree/gen_build_index.py`: S9
- `tools/memory-tree/marker-contract.test.sh`: S11
- `tools/memory-tree/SPEC-TEMPLATE.template.md`, and `memory/TEMPLATE-SPEC.md` its render: S12
- `.memory-tree.conf`, `tools/memory-tree/.memory-tree.conf.example`: S3
- `tools/unattended/unattended.sh`, `tools/unattended/lib-unattended.sh`: S5
- `tools/runlog/model.py`, `tools/runlog/selftest.py`: S6
- `tools/memory-recall/check-recall.py`, `tools/codebase-map/replay-phrases.py`: S6
- `tools/workflows/review_replay.py`: S7
- `tools/check-spec-tokens.py`: S8
- `tools/workflows/tier2-review.template.js`, `tools/workflows/unattended-build.template.js`: S10;
  `tools/workflows/tier2-review.js` and `tools/workflows/unattended-build.js` their renders

### Alternatives rejected

- **Key every reader on the tag alone, and refuse a numbered heading.** Lost to the walkthrough's
  "both formats stay readable while the corpus migrates" (:466-467) and to the 401 landed specs
  TOOL-dBriefedPass-1 counted, none of which carries a tag.
- **Key every reader on the title alone and make the tag decoration.** Lost to the mismatched-tag row of
  contract 3: a title-keyed awk reads `## [section.gates] Acceptance criteria` as acceptance while a
  tag-keyed reader reads it as gates, so two readers disagree on one byte string.
- **One import of `read_spec_section` in every kit.** Lost to the slice: `plan_state` is graded from
  the driver's shipped bytes, where an import from a second kit does not exist, and to the sibling-import
  rule (PLAY-dOrderedCharter-7 §4).
- **Arm the cutoff in this repo here.** Lost to D3: the new format becomes the default after its trial
  against the old (walkthrough :465-467), which is `TOOL-dIndexedDesign-7`'s.

## 5. Production-readiness checklist

- security — no write path; every change is a reader, one `--section-table` subprocess per hygiene run
  under a set key, and a skeleton writer that already writes.
- perf / scale — the engine stays one awk over the population; the table is one Python call per run,
  made only when the key is set; review_replay adds one `git cat-file` per subject spec.
- error / empty / loading states — a missing section is None and the CLI's named line, never an empty
  string; a failed table read under a set key refuses naming the key; an unreadable subject blob in
  review_replay is named on its candidate line.
- observability — `--section` and `--section-table` print what each reader sees; contract 3 prints
  each disagreeing row with the reader that disagreed.
- risks — 30 code sites in 10 files move at once; contract 3 and the hygiene fixture pair are the net,
  and the key ships blank so no landed spec changes verdict.
- testing — AC1 to AC12 by a pass, and the arms of §7 at the close.
- migration — none forced (§4 Migration).
- user docs — the spec format's own document is S12; no page under `help/` covers the spec format.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/design_lib.py --section section.open-questions` runs over
  four scratch specs, a Tier-1 one numbered, a Tier-1 one tagged, a Tier-2 one numbered and a Tier-2 one
  tagged, each holding `- **F1 — x?**` under Open questions and `- rev-1` under Revision log, it prints
  the F1 line for all four and never the rev line; over a fifth whose heading is
  `## [section.gates] Open questions` it prints `has no section.open-questions section`, exit 1.
  Red when: the number's value is read, or a mismatched tag is admitted.
- **AC2** — When `design_lib.py --section section.gates` runs over a scratch spec holding two Gates
  headings, one inside a fenced block and one carrying a trailing CR, it prints the first unfenced
  heading's body only.
  Red when: a fenced heading binds, a CR hides a heading, or the later duplicate is read.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 12` runs over a scratch tree whose
  conf sets `SPEC_TAGS_CUTOFF=2026-11-01`, a tagged Tier-2 spec and a tagged Tier-1 spec dated
  2026-11-02 pass, a numbered one dated 2026-11-02 and a tagged one dated 2026-10-30 are each red
  naming the canon, and a spec mixing both forms is red; with the key blank, the numbered specs pass
  and both tagged ones are red.
  fixture: the scratch conf arms `SPEC_FORMAT_CUTOFF`, `SPEC10_CUTOFF`, `SPEC_TIER1_CUTOFF` and
  `SPEC_TAGS_CUTOFF`; the last is in no conf before this unit.
  Red when: the canon reads one form for every date, or a mixed spec passes.
- **AC4** — When `check-memory-hygiene.sh --only 12` runs over a scratch pair, one numbered and one
  tagged copy of the same Tier-2 spec, each planting an acceptance bullet with no backticked token, a
  scope item naming no criterion, an empty §10, a revision entry with no scope and an unresolved F-item
  at `CLOSED`, it prints the same five findings for both files.
  Red when: any arm finds the planted break in one form and not the other.
- **AC5** — When `plan_state`, sliced out of `unattended.sh` from its `plan_state()` line to the first
  column-0 `}` after it and sourced in `bash`, grades a tagged Tier-1 scratch spec with an unresolved F-item, it prints `FORKED`, and with the F-item
  resolved, `READY`; `read_consumes_from` over a tagged spec prints its `consumes-from` ids.
  Red when: a tagged spec grades `THIN`, or its edges read empty.
- **AC6** — When `python -c "import model; print(model.extract_open_questions(open(p).read()))"` runs
  from `tools/runlog/` over the numbered and the tagged Tier-1 scratch specs of AC1, it prints the F1
  line for both and the rev line for neither: the clause's seen-red case, read correctly by tag where
  the ordinal reads the Revision log.
  Red when: the `## 8.` read is restored, which prints the rev line for the numbered spec.
- **AC7** — When `python tools/workflows/review_replay.py --selftest` runs, its section-ref cases include
  `x.md:AC2` and `x.md:section 5` over a Tier-1 subject both reading `section.acceptance`, and
  `x.md:[section.scope] S5` reading `section.scope`, and they pass.
  Red when: `ITEM_SECTIONS` maps by number, or a numeric ref ignores the subject's own ordinals.
- **AC8** — When `check-recall.py`, `replay-phrases.py`, `check-spec-tokens.py` and `read_spec_edges` read
  the tagged Tier-2 scratch spec of AC1 and its numbered twin, each finds the same Reuse audit, Gates,
  Acceptance criteria and Edges in both: `check-spec-tokens.py`, run from a scratch repository tracking
  the two, prints the same leg-join and witness lines for each, and a `python -c` call of each other
  reader prints the same section body for each.
  Red when: a reader keyed on `## 10.` or `^## [0-9]+[.]` misses the tagged section.
- **AC9** — When `python tools/memory-tree/gen_build_index.py --new-spec tFix-1 --tier 1` runs in a
  scratch tree whose conf sets `SPEC_TAGS_CUTOFF` to a date at or before today, every `##` heading
  written is `## [section.<seg>] <Title>`, and `--tier 2` writes the ten; with the key blank, both write
  today's numbered headings.
  Red when: the cutoff is ignored, or a title is written with no tag.
- **AC10** — When `grep -nE "section[- ][0-9]" tools/workflows/tier2-review.template.js` runs over the
  `SPEC_LENSES` briefs and the address example, it finds no section number, and `grep -c "\[section\."`
  finds the tags; `unattended-build.template.js` :908, :911 and :994 name `[section.gates]` and
  `[section.reuse-audit]`; each render is byte-equal to its template's render.
  Red when: a lens brief or the address format still names a section by number.
- **AC11** — When each reader S11 names reads one scratch spec per row of S11's case table
  (`read_spec_section` and the S6 twins by `python -c`, the AC5 slice of `plan_state`,
  `read_consumes_from`, and `check-memory-hygiene.sh --only 12` over a scratch repository), each prints
  the verdict its row states; with the slice's Open questions literal staged back to an ordinal match,
  the sliced `plan_state` misreads the Tier-1 row.
  Red when: a reader's verdict differs from its row and nothing prints the difference.
- **AC12** — When `grep -n "SPEC_TAGS_CUTOFF" tools/memory-tree/SPEC-TEMPLATE.template.md
  memory/TEMPLATE-SPEC.md` runs, both carry the section and the heading rule, and the render matches its
  template.
  Red when: the format document does not state the rule, or the render drifts.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `marker contracts` · `build-index selftest` · `runlog selftest` · `review-replay selftest` · `recall floor` · `recall floor arms` · `codebase-map kit selftest` · `spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `tier2-review self-test` · `unattended-build self-test` · `workflow script syntax` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `unattended kit gate` · `pass-order history` · `routed-commits selftest` · `pre-push run-log line` · `run-gates run-log line` · `verifier fan-out self-test` · `review-join self-test` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `policy fixtures`

New arm: tools/memory-tree/marker-contract.test.sh · covers AC5 AC11 · contract 3's case table, staged by one reader keyed back on an ordinal · none

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC3 AC4 · the tagged canon under a set `SPEC_TAGS_CUTOFF` and the numbered-and-tagged pair, staged by the canon reading one form for every date · none

New arm: tools/runlog/selftest.py · covers AC6 · a Tier-1 spec whose Open questions is `## 7.`, staged by restoring the `## 8.` read · none

New arm: tools/workflows/review_replay.py · covers AC7 · the Tier-1 subject's `AC2` and `section 5` refs, staged by `ITEM_SECTIONS` mapping by number · none

New arm: tools/memory-tree/gen_build_index.py · covers AC9 · `--new-spec` under a set and a blank `SPEC_TAGS_CUTOFF`, staged by writing numbered headings under the set key · none

## 8. Open questions

- **F1 — Does this unit arm `SPEC_TAGS_CUTOFF` in this repo?** Options: (a) declare it blank here and in
  the example conf, every reader taking both forms at once and `TOOL-dIndexedDesign-7` arming it after
  its trial; (b) arm it at the landing date, so every spec written after it is tagged. v2's walkthrough
  answers it: the redesigned format "is trialled against the old on real units before it becomes the
  default" (:465-466), and (b) would make the current section set the default ahead of that trial and
  then move the canon a second time when unit 7 redesigns it. Rung 1. RESOLVED (agent, 2026-10-28,
  delegated): (a). widens: none · relaxes: none
- **F2 — The format document is a governance carrier (BUILD-METHOD M11).** Options: (a) state the rule
  in `SPEC-TEMPLATE.template.md` and its render under the README's grant, the clause naming spec
  sections by tag; (b) state it only in `design_lib.py`'s docstring. (b) leaves a spec writer learning
  the rule from a refusal, the defect PLAY-dClosedLoop-22 files for the binding lines. Rung 3 with
  veto 2 lifted by the grant. RESOLVED (agent, 2026-10-28, delegated): (a). grants: PLAY-dClosedLoop-3
  the tagged-heading section of the spec template and its render. widens: none · relaxes: none
- **F3 — TOOL-dTotalRecall-9's section table keys legacy headings with their ordinal (`heading = "1.
  Goal"`, its §4 "The section table") and its AC3 spells `section.acceptance-criteria`.** It is a parent's
  spec and is never edited here. Options: (a) an ask in dTotalRecall's `BACKLOG.md`; (b) a deviation
  record here. (b) records a departure from this clause, which this unit does not make. Rung 3.
  RESOLVED (agent, 2026-10-28, delegated): (a). The ask, filed by the main loop: target dTotalRecall,
  "the `spec` row's `sections` table keys a legacy heading on its title with the ordinal stripped, and
  spells each tag as `design_lib.SPEC_SECTION_TAGS` does" · accept "a Tier-1 spec's
  `## 5. Acceptance criteria` resolves as `section.acceptance` through the section extractor, and a
  parity arm holds the `sections` column equal to `design_lib.py --section-table`". widens: none ·
  relaxes: none
- **F4 — How do readers in other kits reach the rule?** Options: (a) a twin regex per reader, held by
  contract 3's case table; (b) each kit imports `design_lib` through an inline `resolve_kit_dir` and a
  declared `requires_if` row; (c) a shared shell file sourced by both shell kits. (b) cannot reach
  `plan_state`, which is graded from sliced bytes, and breaks the sibling-import rule
  (PLAY-dOrderedCharter-7 §4); (c) is the cross-kit edge contract 2 exists to forbid. (a) reuses the
  marker-contract harness, the seam M5 found. Rung 3. RESOLVED (agent, 2026-10-28, delegated): (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 9 and gap-design-10, the brief's I1 and
  unit 9 row, scout C's reader population, walkthrough D3 and CV2, and v2 P11, every site re-read at base
  `57bc3b91`.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from edge of TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.

## 10. Reuse audit

The seam extended is `design_lib.py`'s spec readers: `read_spec_edges` (`tools/memory-tree/design_lib.py:543`)
already walks sections by title, and `read_spec_section` sits beside it on `tree_lib.unfenced_lines`. The
title-keyed precedent is TOOL-dBriefedPass-1's `plan_state` (`unattended.sh:4467-4495`) and check 12's
Tier-1 arm (`check-memory-hygiene.sh:2479-2495`); the agreement seam is `marker-contract.test.sh`, whose
contract 2 already holds two kits' section-8 readers to one case table. `python
tools/codebase-map/reuse_lookup.py "read one spec section by its name whatever its number or tier"` ranked
name stems (`read`, `read_text`) and `read_spec_revisions` (a SEAM at fan-in 5, which reads revisions,
not sections) and `parse_spec_h1`; no section reader exists, so `read_spec_section` is new beside its
siblings. Where the scout and source disagree: the comment at `unattended.sh:4479-4481` cites sibling
readers at hygiene :880, :939 and :1326, which hold unrelated text at base (they are :2091, :2346 and
:3306); `SPEC_TITLE_NUMBERS`, which the scout lists in group A, reads no spec heading and is left alone
(§3); `unattended-build.template.js` :908 and :911 name "section 7", two prompt sites the scout's census
did not list, now in S10. The recall query returned scout C's row, TOOL-dBriefedPass-1's decision row
(the title-keyed classifier, 4 of 401 specs regraded) and TOOL-dTieredTribunal-17's ask, which that unit
closed.

Recall terms used: `python tools/memory-recall/query.py "how do readers find a spec section when Tier-1 numbers its sections differently" --terms "section ordinal Tier-1 heading title plan_state extract_open_questions SPEC_CANON tag reader cutoff"`
