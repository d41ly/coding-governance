# TOOL-aRepatriatedFork-39 — hygiene check 14 counts present-tense citations only, as check 15 does

**Status:** CLOSED · rev-2 · 2026-09-28 · node a · Tier-1 · base 869209ed · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-28-build-TOOL-aRepatriatedFork-39-1-acceptance-ledger.md](../build/2026-09-28-build-TOOL-aRepatriatedFork-39-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Check 14 calls an id an orphan when it is cited anywhere under the memory root and defined nowhere.
Check 15 grades dead paths only in the present-tense corpus, because a record of a moment and an
append-only file cannot be repaired. At inCMS the wide population makes 330 orphans, and only 4 of
them sit in a present-tense file. Two populations for one corpus is two answers to one question.
Owner ruling, 2026-09-28: check 14 counts present-tense citations only, the way check 15 scopes.

## 2. Scope (IN)

- **S1** — `walk()` in `corpus_ids.py` decides once per file whether that file is present tense.
  The test is the one check 15 already uses: the `present` set minus the append-only set the engine
  prints. Id citations are recorded only from such files, and so are dead-path citations. One
  predicate, read by both checks, never a second copy. Observed by AC1.
- **S2** — The waiver registry is not a citation. An id cited only by
  `project/id-orphan-waiver.txt` is no orphan, so its row is stale. The stale message says which of
  the two reasons applies: the id now resolves, or no present-tense file cites it. Observed by AC2.
- **S3** — `--measure` and `--report` derive their orphan count from the same walk, so the
  `ORPHAN_ID_PIN` that `--measure` prints and the count check 14 grades agree. Observed by AC3.
- **S4** — The rule text in `HYGIENE.template.md` names the population, and `memory/HYGIENE.md` is
  re-rendered from it. The rotation fixture in the hygiene suite cites its moved id from a
  present-tense file, so its unstaged-archive arm still tests membership. memory-tree takes its
  version bump in every carrier. Observed by AC4.

## 3. Non-goals (OUT)

- Check 13's claim set, which the same research found wider than its rule. That is a separate ruling.
- Skipping a family the conf declares as cited-and-never-homed (the research's 14-K). Under a
  present-tense population, inCMS's `PKG` citations fall out without it.
- Gov's own pin. It is 0 and stays 0.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — the orphan population inCMS arms check 14 against. The
  research measured it at 4 present-tense orphans against 330 wide ones.

## 4. Design

### Evidence

At inCMS `905e99b68`, `corpus_ids.py --measure` printed `ORPHAN_ID_PIN="330"`. A read-only
research pass sieved the 330 into nine groups. Only 19 of them are cited in a present-tense file once
the waiver itself is excluded, and 15 of those 19 sit in append-only files. That leaves 4, the
number inCMS's retired engine would have graded.

In gov, `walk()` held the present-tense test inline, as a `continue` guarding the dead-path harvest.
The id harvest sat above it and read every file in the corpus. `checks()`, `cmd_report` and
`_measure_lines` each subtract `defs` from `cites`, so moving the test ahead of the id harvest
moves all three counts together.

The waiver file sits under `project/`, which is present tense, so every row cited itself. A waived
id that nothing else cited stayed an orphan, and its row could never go stale. At inCMS that is 27
rows the research measured as stale once the waiver is excluded.

### Inventory

No new function. `walk()` computes one boolean per file and both harvests read it.

### Files touched (estimate)

`corpus_ids.py` and its selftest, the rotation fixture in `check-memory-hygiene.test.sh`,
`HYGIENE.template.md` and its rendering, and the memory-tree version carriers.

### Alternatives rejected

- A second present-tense regex in `checks()`. That is two answers to one question, the class this
  unit exists to close.
- Keeping the waiver as a citation. That keeps 27 inCMS rows alive by self-citation and blinds the
  stale guard.

## 6. Acceptance criteria

- **AC1** — In `corpus_ids.py --selftest`, an id cited only in an archive file and in append-only
  `DECISIONS.md` produces no finding, and a dead path on the same lines produces none either. The
  arm fails on the 869209ed engine. The present-tense control, an id cited in `README.md`, reds on
  both engines.
  Red when: an id cited only outside the present-tense corpus is still graded an orphan.
- **AC2** — In `corpus_ids.py --selftest`, a waiver row whose id only the waiver and an archive cite
  reds as a stale row, naming the no-present-tense-citation reason. The arm fails on the 869209ed
  engine, which reads the row as waiving a live orphan.
  Red when: the waiver's own rows keep their ids alive.
- **AC3** — Over one fixture, the `ORPHAN_ID_PIN` that `_measure_lines` returns equals the number of
  orphans check 14 reports.
  Red when: the measured pin and the graded count differ.
- **AC4** — The full `check-memory-hygiene.sh` run exits 0 on gov's tree. The hygiene suite's
  rotation block passes when sliced. `bash tools/check-kit-versions.sh` exits 0, and
  `python tools/govkit/govkit.py epoch --base f8fdd873` reports no FAILED entry.
  Red when: a carrier keeps 2.99, or the unstaged-archive arm stops flagging its id.

## 7. Gates

`memory hygiene` · `corpus-ids selftest` · `memory-hygiene self-test` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `kit/dogfood doc parity`

New arm: `tools/memory-tree/corpus_ids.py` · `check 14 grades present-tense citations only` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-28 · initial draft, from the owner's ruling.
- rev-2 · 2026-09-28 · S1 · S2 · S3 · S4 · AC1 · AC2 · AC3 · AC4 · built. Every new arm red on the
  869209ed engine, the present-tense control red on both, and the rotation fixture's old spelling
  red on the new engine. Gov's pin stays 0.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "decide whether a memory file is present tense for a
corpus citation check"` ranked `checks` in `corpus_ids.py` and `corpus_files` in the recall kit. It
names no predicate, because the one that exists is the inline `present` regex and append-only test
in `walk()`. This unit reuses that test for check 14 rather than writing a second one.

Recall terms used: `orphan ids present tense check 14 check 15 dead path citation append-only waiver
ORPHAN_ID_PIN corpus_ids walk`.
