# TOOL-dMindYourWords-15 — build records kept out of the graded population by a path selector

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 3 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0276@c565a516 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-14-reuse-scout-d.md](../build/2026-10-29-build-TOOL-dMindYourWords-14-reuse-scout-d.md) | research | TOOL-dMindYourWords-14 TOOL-dMindYourWords-17 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-1 TOOL-dMindYourWords-14 TOOL-dMindYourWords-12 TOOL-dMindYourWords-11 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-9 TOOL-dMindYourWords-16 TOOL-dMindYourWords-13 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

Give the lexicon a path selector, the `OUT_OF_SCOPE:` block, and declare `memory/builds/**` in it, so
build records leave the graded population, and re-arm the `py.file` and `py.constant` cells it was
waiting for. Today 167 verb offenders sit under `memory/builds/` inside the pin, a record's new
extension reds the wiring leg, and both cells are declared off because a record's filename follows
the recording grammar and can never meet a code convention (gap-lex-04, ask TOOL-aSurfacedLexicon-23).

## 2. Scope (IN)

- **S1** — The block. `OUT_OF_SCOPE:` joins `BLOCK_KEYS` (`tools/lexicon/lexicon_conf.py:37`) with one
  `_BLOCK_PARSERS` row (`:401`), `_parse_out_of_scope`, over the generic `_parse_rows` (`:187`): each
  row is `<glob>  <reason>`, returned as `{glob: reason}` in declaration order. Refused, naming the
  line: a row with no reason, a glob that is absolute, carries a `\` or a `..` segment, and a repeated
  glob (`_parse_rows`' own refusal). The block inherits TOOL-dMindYourWords-14's repeated-header
  refusal through `load_conf`. Observed by AC4.
- **S2** — The predicate, I17. `check_out_of_scope(rel, rows)` in `lexicon_conf.py` returns the reason
  of the first row whose glob matches the repo-relative POSIX path `rel` under stdlib `fnmatchcase`,
  or `None`; `lexicon.py` imports it beside `load_conf`. `fnmatchcase` and not `fnmatch`, which folds
  case on Windows (`tools/codebase-map/map_lib.py:29-30`); the kit is copy-installed and imports no
  `map_lib`. Observed by AC5.
- **S3** — The walk honours it. `scan_corpus` (`tools/lexicon/lexicon.py:2262-2321`) gains two keyword
  parameters, `scope_rows` and `out_of_scope`: a tracked file `check_out_of_scope` matches is never
  extracted and never yielded, and its path and reason go into the caller's `out_of_scope` dict. The
  4-tuple stays, so every unpacking caller is unchanged. Because the walk is the one population, an
  out-of-scope file also leaves the undeclared-extension census (`present_exts`, `:3023`), the DEAD
  PROBE test and the coverage denominator. `measure_pass` (`:2821`) passes the conf's rows. Observed by
  AC1, AC2 and AC3.
- **S4** — The class. An out-of-scope file is the `out-of-scope` tally class of TOOL-dMindYourWords-1
  S1, counted in files on the class line; `--list` prints one line per row,
  `out-of-scope <glob> <n> file(s) — <reason>`, so each exclusion carries its source. A row matching no
  tracked file is a refusal, `DEAD SCOPE ROW`, naming the row, since an empty selector reads as
  coverage. Observed by AC1, AC2 and AC4.
- **S5** — The same decision for the merge-loss check. `check_merge_losses` keeps a changed path only
  when `check_out_of_scope` returns `None` for it (`lexicon.py:4240`), so `read_defs_at_sha`, or
  TOOL-dTotalRecall-13's `read_defs_at` it adapts at the build run's base, reads no record; the
  working tree's conf supplies the rows. Observed by AC8.
- **S6** — The scaffold. `scaffold_lexicon.py` passes its seed rows to its walk (`:230`) and seeds
  `OUT_OF_SCOPE:` with `memory/builds/**` and its reason only when a tracked file matches it, so a fresh
  adopter without build records gets no dead row. Observed by AC9.
- **S7** — This repository's declaration. `.lexicon.conf` gains `OUT_OF_SCOPE:` with the row
  `memory/builds/**  build records: their names follow the recording grammar, not a code convention`,
  and the `CELLS:` rows `py.file  snake` and `py.constant  screaming`. The violations those two cells
  grade outside records join TOOL-dMindYourWords-1's debt ledger as `py.file.conv` and
  `py.constant.conv` rows in this pass, never as new `PINS:` rows, and the record rows leave it as
  drains. Observed by AC6.
- **S8** — The stale claims corrected in place: the paragraph saying both cells graded clean
  (`.lexicon.conf:549-564`, the claim at `:556`) and the `py.file` paragraph (`:541-547`) state the
  selector and the re-arm instead, and the `<-- ARMED` row of the `py.constant` readings (`:411`), which
  the selftest compares with the graded figure `--check` prints (`tools/lexicon/selftest.py:2409`), is
  re-measured at the pass. Observed by AC7.
- **S9** — The legs' `doc_reads`. Both lexicon legs declare `doc_reads = ["{memory_root}/builds/"]`
  (`tools/lexicon/kit.toml:168`, `:175`, rendered at `tools/gate-legs.json:1476`, `:1502`); with records
  out of the population the key drops from both, so each leg runs on every doc-only push (§8 F3).
  **Readers:** by name: `tools/lexicon/kit.toml`, `tools/gate-legs.json`, `tools/govkit/govkit.py`
  (the manifest compare at `:2801-2868` and `derive_doc_reads` at `:6020`), `tools/run-gates/run-gates.sh`
  (`:2841-2847`) · by value: the runner's docs mode (`run-gates.sh:421-440`), which runs a leg declaring
  `doc_reads` only when one of its paths moved and runs a leg without the key on every doc push.
  Observed by AC10.
- **S10** — The record-only `LANGS` rows. `html::dark`, `svg::dark`, `log::dark` and `out::dark`
  (`.lexicon.conf:24`) were each declared for build records (L-6, and the stamps at `:357-370`); a dark
  row whose extension no in-scope tracked file carries at the pass is deleted from the `LANGS` line, and
  `ratified` is re-stamped in the same commit with its note, since `signal_lexicon_ratified_stale`
  compares the stamp with the last `LANGS` edit (`tools/drift-audit/drift_report.py:1318`).
  **Readers:** by name: `.lexicon.conf` · by value: the undeclared-extension census and the inert-row
  report in `measure_pass` (`lexicon.py:3023-3025`), and `signal_lexicon_ratified_stale`, which reads
  the `LANGS` line's last commit date. Observed by AC11.
- **S11** — The docs: `tools/lexicon/README.md` gains the `OUT_OF_SCOPE:` block beside the `CELLS`
  grammar, and `KIT_LEXICON_VERSION` moves. NOT OBSERVED as behaviour: prose, read by the Skill render
  check.

## 3. Non-goals (OUT)

- A `CELLS` selector kind over paths: `SELECTOR_KINDS` (`lexicon_conf.py:72`) selects by name and
  routes a name to another convention, and `_SEL_LIT_RE` (`:86`) forbids `/`; a selector cannot
  exclude (§4 "Alternatives rejected").
- The drift-audit signals' own walk over `lex.tracked_files` (`tools/drift-audit/drift_report.py:1296`)
  and the index state at commit: TOOL-dMindYourWords-16 and TOOL-dMindYourWords-9 call
  `check_out_of_scope`. TOOL-dMindYourWords-12's `read_defs_at` caller passes it too.
- Renaming the 73 re-armed violations: they are debt in the one pin, as scout D's interface 7 and the
  lexicon review's `[classes]` settle; draining them is ordinary debt work.
- Test files: they stay graded (lexicon review:216).
- Declaring a planted fixture tree in this repository: no tracked tree plants a name the lexicon
  grades today, so a row for one would be a `DEAD SCOPE ROW`; the unit that commits such a tree adds
  its row.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `Offender.grade`, whose out-of-scope tally class S4 fills, and the debt ledger S7's rows join; without it the re-armed violations have no pin
- **consumes-from** `TOOL-dMindYourWords-14` — `load_conf`, whose repeated-header refusal the `OUT_OF_SCOPE:` block inherits
- **hands-off** `TOOL-dMindYourWords-12` — `check_out_of_scope`, which its caller of the primitive passes as a path filter
- **hands-off** `TOOL-dMindYourWords-9` — `check_out_of_scope`, which its commit arm applies to the staged set
- **hands-off** `TOOL-dMindYourWords-16` — `check_out_of_scope`, which the leg pack's drift signals apply to their walk
- **hands-off** `TOOL-dMindYourWords-8` — `check_out_of_scope`, through which its manifest reader skips a record
- **consumes-from** external — TOOL-dTotalRecall-13 S2's `read_defs_at`, an ancestor build's, which `read_defs_at_sha` adapts at the build run's base
- **consumes-from** `TOOL-dMindYourWords-27` — the ledger home `.lexicon-debt.txt`, which S7's rows join, in place of `memory/project/lexicon-debt.txt` (review id 45)
- **hands-off** `TOOL-dMindYourWords-29` — the `LANGS` rows S10 takes out and `check_out_of_scope`, which the minors batch repairs (review ids 36, 57)

## 4. Design

### Evidence

Read at `ba8b3c8c4`; no product file differs from base `ccd1292e`.

- `scan_corpus` is the one walk; `tracked_files` (`lexicon.py:410`) has one call site in it (`:2289`),
  and its two callers are `measure_pass` (`:2821`) and `scaffold_lexicon.py:230`.
- `SELECTOR_KINDS = ("prefix", "decorator", "returns")` (`lexicon_conf.py:72`) and `_SEL_LIT_RE`
  (`:86`) admit no path.
- Measured with the kit's own `scan_file_stems` and `scan_module_constants` over `.lexicon.conf` at
  `ba8b3c8c4`: `py.file` grades 157 names with 62 violations, 51 under `memory/builds/` and 11 outside;
  `py.constant` grades 2,110 with 251 violations, 189 in records and 62 outside. `python
  tools/lexicon/lexicon.py --offenders` reads 167 verb offender keys under `memory/builds/`. All
  PINNED at that sha; S7 and AC6 re-derive them at the pass.
- Outside `memory/builds/` no tracked file carries `.html`, `.svg`, `.log` or `.out` (`git ls-files`
  at `ba8b3c8c4`), and the stamps at `.lexicon.conf:357-370` record each row as declared for records.
- `doc_reads` is all or nothing: a leg declaring it runs on a doc-only push only when one of its
  paths moved, and a leg without it runs on every doc push (`tools/govkit/govkit.py:6020-6040`,
  `tools/run-gates/run-gates.sh:421-440`); the doc class is `memory/` and five root files
  (`.githooks/gate-env.sh:108`).

### The block and the walk

```
OUT_OF_SCOPE:
  memory/builds/**  build records: their names follow the recording grammar, not a code convention
```

```python
def scan_corpus(root, declared, sets=None, *, scope_rows=None, out_of_scope=None):
    for rel in tracked_files(root):
        if scope_rows:
            reason = check_out_of_scope(rel, scope_rows)
            if reason is not None:
                if out_of_scope is not None:
                    out_of_scope[rel] = reason
                continue
        ...  # unchanged
```

`fnmatchcase("memory/builds/a/b.py", "memory/builds/**")` is true because `*` crosses `/` in
`fnmatch`; a row may still spell `**` for the reader. `DEAD SCOPE ROW` is computed in `measure_pass`
by matching each row against the tracked path list it already holds, one string test per path and row.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `OUT_OF_SCOPE:` | conf block | none |
| `check_out_of_scope` | function, `lexicon_conf.py` | `py.function`, answered OK by `--suggest` at `ba8b3c8c4` |
| `_parse_out_of_scope` | function, `lexicon_conf.py` | `py.function`, answered OK by `--suggest` at `ba8b3c8c4` |
| `scope_rows`, `out_of_scope` | keyword parameters of `scan_corpus` | none |
| `DEAD SCOPE ROW` | refusal text | none |

### Migration

In this pass the ledger's rows under `memory/builds/` leave as drains and the 73 re-armed violations
arrive. Against the base, which holds no ledger before this build lands, the base half reads
unresolved (TOOL-dMindYourWords-1 §4 "Rollout"), so the arrivals need no widening record. An adopter
gains the block empty and its conf parses unchanged.

### Rollout

Live at landing in this repository by S7's row. An adopter is untouched until it declares a row or
re-scaffolds.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1, S2
- `tools/lexicon/lexicon.py`: S3, S4, S5, `KIT_LEXICON_VERSION`
- `tools/lexicon/scaffold_lexicon.py`: S6
- `tools/lexicon/selftest.py`: the arms of §7
- `tools/lexicon/README.md`: S11
- `tools/lexicon/kit.toml` and its render `tools/gate-legs.json`: S9
- `.lexicon.conf`: S7, S8, S10
- `memory/project/lexicon-debt.txt`: S7's rows

### Alternatives rejected

- **A third `CELLS` selector kind, the ask's first option.** A selector routes a name to a convention
  and cannot remove it from P1, the undeclared-extension census or the pin; test: P1 grades every
  extracted function whatever the `CELLS` rows say (`lexicon.py:2941`), so a path selector there would
  re-case records and still count them.
- **Excluding after extraction, yielding an out-of-scope file with no definitions.** The interface
  table's first spelling of I17. A yielded file stays in `present_exts`, so `.html` and `.svg` would
  still need `LANGS` rows, the case the clause closes; and extracting a record first lets a record that
  does not parse red the leg.
- **Waivers for the record names.** They key on bare text corpus-wide (`load_waivers`, `:2324`) and
  carry no path; the refused class TOOL-aSurfacedLexicon-15 names.
- **Keeping `doc_reads` on `{memory_root}/`.** It fires on nearly every doc push, records included,
  while naming a population the leg no longer reads; the absent key says what is true.

## 5. Production-readiness checklist

- security — a glob is refused when absolute, back-slashed or climbing (`..`), so a row cannot name a
  path outside the repository; the selector only narrows what is graded, and every exclusion prints.
- perf / scale — records are no longer read or parsed, about 8,700 tracked files at `ba8b3c8c4`, so the
  walk gets cheaper; S4's dead-row test is one string match per path and row.
- error / empty / loading states — no block means no exclusion and today's behaviour; a dead row
  refuses by name.
- observability — `--list` prints each row with its file count and reason; the class line counts files.
- risks — a broad glob hides product code from the gate; every row prints its count on `--list`, and
  TOOL-dMindYourWords-11 puts the block under the vocabulary write path.
- testing — the arms of §7.
- migration — §4 "Migration".
- user docs — `tools/lexicon/README.md`; no `help/` page covers the lexicon.

## 6. Acceptance criteria

- **AC1** — When `python lexicon.py --list` runs on a fixture holding
  `<fixture>/memory/builds/x/build/2026-01-01-build-T-1-probe.py` with `def frobnicate_it()`, it lists that
  offender; with `OUT_OF_SCOPE:` declaring `memory/builds/**`, it does not, prints `out-of-scope
  memory/builds/** 1 file(s)` with the reason, and the class line reads `out-of-scope=1 file(s)`.
  Red when: a record-shaped offender is graded with the row declared, the clause's planted case.
- **AC2** — When the fixture instead holds `<fixture>/tools/demo/fixtures/case/plant.py` with a planted offender
  and the conf declares `tools/demo/fixtures/**  a planted fixture tree`, `python lexicon.py` grades
  it before the row and not after.
  Red when: a declared fixture tree stays graded, the clause's second planted case.
- **AC3** — When the fixture tracks `<fixture>/memory/builds/x/a.weird` and `LANGS` declares no `weird`,
  `python lexicon.py` reds naming the undeclared extension; with the row declared it does not.
  Red when: an out-of-scope file still feeds the extension census.
- **AC4** — When `python lexicon_conf.py --print-rows OUT_OF_SCOPE <conf>` runs on a planted row with no
  reason, one starting `/`, one carrying `..`, and one repeated, each exits non-zero naming its line;
  and `python lexicon.py` on a row matching no tracked file exits 1 naming `DEAD SCOPE ROW`.
  Red when: a malformed or dead row parses as a selector.
- **AC5** — When `python -c "import lexicon_conf as c; print(c.check_out_of_scope('memory/builds/a/b.py',
  {'memory/builds/**': 'records'}))"` runs beside the kit, it prints `records`; for `'tools/a.py'` and for
  `'Memory/Builds/a/b.py'` it prints `None`.
  Red when: the match folds case, or misses a nested record.
- **AC6** — When `python tools/lexicon/lexicon.py` runs at the pass, it prints a `py.file.conv` and a
  `py.constant.conv` row; `grep -cE "py\.(file|constant)\.conv" lexicon-debt.txt` run in `memory/project/`
  prints the violation count those two rows print; and `grep -c "^memory/builds/" lexicon-debt.txt`
  run there prints 0.
  Red when: a re-armed violation sits outside the one ledger, or a record row stays in it.
  figure: DERIVED at the pass; 73 rows and 167 drains at `ba8b3c8c4` are §4's PINNED readings.
- **AC7** — When `grep -c "both cells graded clean" .lexicon.conf` runs at the pass, it prints 0, and
  the figure on the `<-- ARMED` row equals the `py.constant` graded figure `python
  tools/lexicon/lexicon.py` prints.
  Red when: the stale claim or the stale figure is left, which the selftest's AC5 arm reads.
- **AC8** — When `python lexicon.py --merge-losses <a>..<b>` runs over a fixture merge that loses a
  definition only under `memory/builds/`, it exits 0 with the row declared and 1 without it.
  Red when: the merge-loss check grades a record the corpus walk excludes.
- **AC9** — When `bash adopt-lexicon.sh --scaffold` runs in a fixture tracking a file under
  `memory/builds/`, the conf carries the `memory/builds/**` row; in a fixture tracking none, it carries
  no `OUT_OF_SCOPE:` row.
  Red when: the scaffold seeds a dead row, or grades an adopter's records.
- **AC10** — When `grep -c doc_reads tools/lexicon/kit.toml` runs, it prints 0, and neither lexicon row
  of `tools/gate-legs.json` carries the key after the render.
  Red when: a leg still declares a doc path it no longer reads.
- **AC11** — When `grep -cE "(html|svg|log|out)::dark" .lexicon.conf` runs at the pass, it prints 0,
  `python tools/lexicon/lexicon.py` names no undeclared or inert extension, and the `ratified` date
  equals the date of the commit that edits the `LANGS` line.
  Red when: a record-only row is kept, or the `LANGS` edit leaves the stamp older than it.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `codebase-map kit selftest` · `drift-audit selftest` · `drift-audit records` · `govkit acceptance matrix` · `straggler-guard arms` · `policy fixtures` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `recall floor` · `recall floor arms` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC8 AC9 · planted record, fixture-tree and odd-extension files with and without the row, the parser's four refusals, a dead row, a fixture merge and two scaffold runs; its failing case the record-shaped offender graded with the row declared · none

## 8. Open questions

- **F1 — Where does the exclusion live?** Options: (a) a block the one corpus walk honours, so every
  population built from the walk loses the file; (b) a third `CELLS` selector kind; (c) a filter on the
  offender list after grading. (b) cannot remove a name from P1 or the census, and (c) leaves records
  in the census and parsed. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the ask's second
  option, "an exclusion glob the population walk honours" (TOOL-aSurfacedLexicon-23). widens: none · relaxes: none
- **F2 — Is an out-of-scope file yielded with no definitions, or not yielded?** Options: (a) not
  yielded, its path and reason in the caller's side table, the class counted in files; (b) yielded with
  `defs` empty, as the interface table first spelled it. (b) keeps a record's extension in the census,
  which fails the gap's own case (gap-lex-04: "an undeclared record extension refuses the wiring leg").
  RESOLVED (agent, 2026-10-29, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — What happens to the legs' `doc_reads`?** Options: (a) drop the key; (b) re-declare it as
  `{memory_root}/`; (c) keep `{memory_root}/builds/`. (c) skips the leg on a doc push adding a new
  extension under `memory/` outside records, which the census still reads, and (b) fires on nearly
  every doc push while naming no population. RESOLVED (agent, 2026-10-29, delegated): (a), rung 1: the
  lexicon review's `[fixes]` "drops or re-justifies them once the selector lands" (lexicon review:465-467),
  and the absent key runs the leg, failing toward coverage. widens: none · relaxes: none
- **F4 — Do the re-armed cells' outside violations become pin rows or renames?** Options: (a) rows of
  TOOL-dMindYourWords-1's debt ledger; (b) per-cell `PINS:` rows; (c) rename the 73 first. (b) is the
  block the clause beside this one retires, and (c) is debt work the clause does not ask. RESOLVED
  (agent, 2026-10-29, delegated): (a), rung 1: the lexicon review's `[classes]` "its cells counted
  inside the one pin" and scout D's interface 7. widens: none · relaxes: none
- **F5 — Is a planted fixture tree in this repository declared now?** Options: (a) no: the clause's
  fixture-tree case is planted in the selftest's own repository, and the unit that commits such a tree
  adds its row; (b) seed a row for a tree no unit has committed. (b) is a `DEAD SCOPE ROW` at landing.
  RESOLVED (agent, 2026-10-29, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Items 15, the lexicon review's `[classes]`,
  `[fixes]` and L-6, gap-lex-04, ask TOOL-aSurfacedLexicon-23, scout D's row 2 and its interfaces 2,
  3 and 7, and the spec brief's I17.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (TOOL-dMindYourWords-27, TOOL-dMindYourWords-29); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are `scan_corpus` (`tools/lexicon/lexicon.py:2262`), the one walk, and the block
grammar (`BLOCK_KEYS` and `_BLOCK_PARSERS`, `tools/lexicon/lexicon_conf.py:37`, `:401`, with
`_parse_rows`); `fnmatchcase` is the matcher `tools/codebase-map/map_lib.py:44` imports for the same
Windows reason. `python tools/codebase-map/reuse_lookup.py "exclude paths matching a declared glob from
a corpus walk"` ranked `walk` (`tools/memory-tree/corpus_ids.py`), `load_corpus` and `corpus_files`
(`tools/memory-recall/extract.py`) and `attribute_paths` (`map_lib.py`); each walks its own kit's
corpus and none is importable by a copy-installed kit that imports no sibling, so the selector is new
inside the lexicon's own walk. Scout D's row 2 holds against source at `ba8b3c8c4`: the measured
populations re-derive exactly. One disagreement with the interface table: I17 yielded an out-of-scope
file, and source shows the census reads every yielded file (`lexicon.py:3023`), so S3 does not yield it
(§8 F2). The recall probe surfaced ask TOOL-aSurfacedLexicon-23, whose second option this unit takes.

Recall terms used: `python tools/memory-recall/query.py "how are build records kept out of the lexicon graded population by a path selector" --terms "lexicon path selector memory/builds out of scope scan_corpus py.file py.constant re-arm TOOL-aSurfacedLexicon-23 doc_reads"`
