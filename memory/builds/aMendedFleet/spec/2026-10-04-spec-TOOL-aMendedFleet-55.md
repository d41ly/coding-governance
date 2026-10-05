# TOOL-aMendedFleet-55 — drift reports `open_asks_cited_by_product_source`, report-only

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 55

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

54 of the 457 live asks are cited by tracked product source, and in the review's sample of five, two
had already been fixed and still read OPEN, with KEEP triage rows written after their fixes landed.
Nothing reports the pair. Drift already asks the same question of specs:
`non_terminal_specs_cited_by_product_source` flags a non-terminal spec whose id product source
cites. This unit adds its sibling for asks, `open_asks_cited_by_product_source`, over the
generator's own live ask projection and the same evidence globs, report-only until a sampled
precision figure exists, because source legitimately cites an ask it has not fixed yet.

## 2. Scope (IN)

- **S1** — A new builder `build_open_asks_cited_by_source` in `tools/drift-audit/drift_report.py`,
  listed in `SIGNALS` beside the other backlog signals, takes its population from
  `read_asks_or_skip` with `all_rows` false: every ask the generator's live projection returns, with
  no status rule of its own. Observed by AC1.
- **S2** — The citation test is signal 2's: a whole-word fixed-string match over `EVIDENCE_GLOBS`,
  so test files and fixtures are not evidence and `-1` never matches inside `-11`. It runs as ONE
  `git grep -o -w -F -f -` with the ids on standard input, so the argument list does not grow with
  the backlog. `value` is the count of live asks cited, `of` the count of live asks, and each detail
  row carries the ask id, its projected status and up to three citing paths, sorted by id. The record
  also carries `evidence_files`, the tracked-file count of `EVIDENCE_GLOBS`, and `live` requires both
  a non-empty population and a non-zero `evidence_files`, the second liveness half signal 2 already
  carries. Observed by AC1, AC2, AC3.
- **S3** — Report-only: `gateable` false, with the pinless `tolerance` unit 51 introduces. A shards
  backlog, or no tracked per-build backlog, reads not asked through `read_asks_or_skip`. Observed by
  AC1.
- **S4** — The drift-audit README's `## The signals` table gains the row for the new signal, saying
  it is report-only until a sampled precision exists, in the same commit, so the hand-kept signal
  unit 52 re-arms keeps reading 0. Observed by AC4.
- **S5** — Self-test arms in `tools/drift-audit/selftest.py` over the existing builds-mode fixture: a
  live ask cited from product source counts, the same id cited only from a `*.test.sh` file does not,
  a sibling id one digit longer does not count for the shorter id, and an unreadable projection reads
  not live. NOT OBSERVED by a criterion here: the suite runs once at the close, and the arms are
  declared under `New arm:` in §7.
- **S6** — `memory/map/generated/symbols.json` is regenerated for the new definition. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the legs that read it.

## 3. Non-goals (OUT)

- Disposing any cited ask. Unit 14 disposes the fixed-but-OPEN asks the review named; this signal
  lists candidates and decides none.
- Gating. Forward references are false positives by construction, and no precision has been sampled.
- A third ask parser. The population is the generator's projection, which every builds-mode signal
  already reads.
- Excluding an ask cited only from the drift kit's own comments. Such a citation is a real pointer
  from code to an ask, and a carve-out is a waiver list nobody drains.
- The drift-audit kit version bump, owed once at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-51` — the pinless `tolerance` form S3 uses.
- **hands-off** external — sampling the signal's precision before anyone proposes gating it.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at worktree HEAD `725b1449`, whose `tools/` bytes equal base `7af5f564`'s.

- `python tools/memory-tree/gen_build_index.py --asks --json` returned 457 live asks over 106 files:
  444 OPEN, 8 SPECCED, 4 DEFERRED and 1 INPROGRESS.
- A scratch probe applying S2 over this repo's `EVIDENCE_GLOBS` found 54 of them cited, every one
  OPEN, matching the source synthesis's 54 exactly. PINNED, measured 2026-10-04.
- `git grep -o -h -w -F -f -` reads its patterns from standard input in this repo's git; measured on
  two ids before writing S2.
- `read_asks_projection` caches each projection shape on the context, so this signal adds no
  generator spawn to a run that already reads the live shape.

### Inventory

- `build_open_asks_cited_by_source` — cell `py.function`; answered OK by
  `python tools/lexicon/lexicon.py --suggest build_open_asks_cited_by_source --as py.function`.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **One `git grep` per ask, as signal 2 runs one per spec.** 457 spawns at about 0.75 s each on node
  `a` is minutes added to a seconds-tier report.
- **The ids on the command line.** About 12 KB of argument today and growing with the backlog toward
  the Windows command-line limit.
- **`migrate_backlog.py`'s triage worksheet, which the synthesis suggests reusing.** It is the
  one-shot switch-over's legacy-row machinery; its citation predicate `check_names_id` is the same
  whole-token rule `-w` already applies, and the live projection is the ask parser the drift kit
  already shares.

## 5. Production-readiness checklist

- security — N/A: reads tracked files and the generator's projection; prints ids and paths.
- perf / scale — one `git grep` spawn; the live projection is shared with the other backlog signals.
- error / empty / loading states — not asked under shards or with no backlog; not live when the
  projection cannot be read or the evidence globs resolve to nothing.
- observability — each detail row names the ask, its status and where it is cited.
- risks — a forward reference reads as fixed; report-only, so the cost is a line a triager dismisses.
- testing — AC1 to AC4 here; the arms in S5.
- migration — N/A: nothing stored changes.
- user docs — S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs on this repo, the
  `open_asks_cited_by_product_source` record has `live` true and `gateable` false, its `of` equals the
  length of the `asks` array `python tools/memory-tree/gen_build_index.py --asks --json` prints, and
  its `value` is at least 1.
  Red when: the population differs from the generator's live projection, or the record is dead.
  figure: DERIVED at observation time; 54 of 457 at writing, before unit 14's dispositions.
- **AC2** — When a comment naming one live ask id the record's detail does not list is appended to
  `tools/drift-audit/drift_report.py` in the working tree and the report runs again, `value` rises by
  exactly one and the detail lists that id with `tools/drift-audit/drift_report.py` among its
  citing paths; reverting the line restores the count.
  Red when: a product-source citation is missed.
- **AC3** — When the same comment is appended instead to
  `tools/runlog/fixtures/driver-torn.txt`, a fixture file `EVIDENCE_GLOBS` excludes, and the
  report runs again, `value` does not move.
  Red when: a test-file citation counts as evidence.
- **AC4** — When `grep -c "open_asks_cited_by_product_source" tools/drift-audit/README.md` runs it
  reports at least 1, and the `handkept_inventories_disagreeing_with_source` record of
  `python tools/drift-audit/drift_report.py --json` reads `value` 0.
  Red when: the README table omits the new signal.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · a builds-mode fixture with an ask cited from product source, from a test file only, and by a longer sibling id · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — Which asks form the population?
  Options: OPEN asks only, as the signal's name reads; every ask the generator's live projection
  returns. A status filter here would be a second liveness rule beside the generator's.
  RESOLVED (agent, 2026-10-04, delegated): the live projection, per S1, with each row's status in
  the detail.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#59] and a scratch probe of live
  asks against `EVIDENCE_GLOBS` at base.
- rev-2 · 2026-10-04 · S6 · §4 · §7 · M2 cross-read: the new definition owes `symbols.json`, which
  units 57, 59 and 90 regenerate for theirs and this spec omitted.

## 10. Reuse audit

The seams extended are `read_asks_or_skip` and `read_asks_projection`, the generator projection every
builds-mode signal reads, and the citation predicate and `EVIDENCE_GLOBS` population of
`signal_spec_status`, all in `tools/drift-audit/drift_report.py` and its project layer.
`python tools/codebase-map/reuse_lookup.py "find open asks whose id is cited by tracked product
source"` returned `tracked` in govkit, `render_ask_row` and `check_id` in the backlog module and
`build_lang_mode_findings` in this kit, name-stem neighbours none of which joins an ask to a citation;
no existing seam fits the join itself, so it lives in the builder over the two seams above. The scan
names `.sh` as unscanned; no shell file is involved. Recall returned unit 14, which disposes the
fixed-but-OPEN asks this lists, `TOOL-aBoundedVerdict-30`, the prefix bug that put `-w` into signal
2, and `TOOL-dCarriedReceipt-4`, a spec deliberately never closed that signal 2 must live beside,
the same forward-reference shape that keeps this one report-only. Where the report and the tree
disagree: nowhere; 54 re-measured exactly.

Recall terms used: `python tools/memory-recall/query.py "how should drift detect open asks already
fixed by product code" --terms "open_asks_cited_by_product_source fixed-but-OPEN asks product source
citation EVIDENCE_GLOBS non_terminal_specs_cited_by_product_source triage KEEP report-only"`
