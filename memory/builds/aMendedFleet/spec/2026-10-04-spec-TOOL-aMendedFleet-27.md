# TOOL-aMendedFleet-27 — recall excludes archived versioned snapshots by a declared pattern, and an arm proves a live line answers instead

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 27

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

The recall corpus is every tracked markdown file under the memory root, and that includes eleven
archived versioned snapshots of the charter template. A charter question returns the same rule
from up to nine of them, superseded text filling alternate ranks of the top twenty. This unit adds
one declared conf key whose patterns the ONE corpus walk excludes, declares it in this repo for the
versioned snapshots, and adds a self-test arm whose question is answered by a live line and must not
be answered by its archived copies.

## 2. Scope (IN)

- **S1** — `tools/memory-recall/recall_conf.py` reads `RECALL_EXCLUDE`: space-separated,
  repo-relative glob patterns, blank or absent meaning nothing is excluded. The resolved patterns
  join `Conf.digest()`, beside the declared extra sources, so a warm cache built before a change is
  rebuilt. The module's own print mode shows the resolved value. Observed by AC3.
- **S2** — `corpus_files` in `tools/memory-recall/extract.py` leaves out every path matching a
  pattern, on both of its paths, the measurement path pinned to a revision and the query path with
  untracked files, because it is the one walk both call. Observed by AC1, AC2.
- **S3** — A pattern that matches no corpus path prints one line to standard error naming it, the
  same shape the walk already prints for a declared source that is absent, so a mistyped pattern is
  announced rather than silent. Observed by AC4.
- **S4** — `.memory-tree.conf` declares `RECALL_EXCLUDE` for the versioned snapshot names under the
  archive, a comment above it giving the measurement and naming what stays: the rotated decision
  log and the archived ledger shards. Observed by AC1.
- **S5** — `tools/memory-recall/selftest.py` gains one arm, the gold arm. Its fixture corpus holds
  a live guide stating one rule and two archived versioned copies of it; with the key declared, the
  question's hits include the live line and no copy; with the key blank, the copies return. The
  `SELFTEST_ARMS` pin moves with its dated provenance line. NOT OBSERVED by a pass: the suite is a
  self-test the close runs, and a pass runs none.
- **S6** — The kit README's conf-key table gains the key's row, with its blank meaning and its
  announcement. Observed by AC5.

## 3. Non-goals (OUT)

- Indexing `AGENTS.md` or the charter template at the repository root. Both are outside the memory
  root, and the declared-sources route extracts `KEY=value` lines only. The rendered charter reaches
  every session through `CLAUDE.md` already, so an index copy would answer with text the session is
  holding.
- A gold question in the floor's own fixture. Its targets are record ids, and a charter line has
  none; units 28 and 29 of this build own the floor and the gold set.
- Excluding the rotated decision log or the archived ledger shards. The synthesis measured 16 of the
  22 archive top-1 hits as the rotated log, and those are legitimate answers.
- Deleting the snapshots. They stay tracked and readable; only retrieval stops serving them.
- Moving the memory-recall kit version, which this build moves once after the last pass that touches
  the kit.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; none of the files below moved between it and `580dc980`.

- `corpus_files` in `tools/memory-recall/extract.py` is the one corpus walk: markdown under the
  memory root from `git ls-files` or `git ls-tree` at a revision, untracked files added on the query
  path. The query cache keys freshness on `Conf.digest()` in `tools/memory-recall/recall_conf.py`,
  whose blob already carries the declared extra sources for the reason S1 gives.
- `RECALL_EXTRA_SOURCES` in `.memory-tree.conf` is declared, never globbed, because it ADDS answers.
  An exclusion can only take answers away, and a glob is what keeps a new snapshot from being missed.
- `memory/archive/` tracks eleven files whose names end in a version suffix of two digits joined by
  hyphens, three of `coding-governance-agents.template` and eight of `parallel-coding-governance.template`,
  plus `memory/archive/DECISIONS.2026-08-10.md` and four ledger shards.
- A scratch scan of those eleven: none carries an id-anchored line and none carries an id from
  `tools/memory-recall/recall-fixture.json`, so the floor's record set and its score cannot move.
- `python tools/memory-recall/query.py` with the charter question and terms recorded in §10 returned
  snapshots at ranks 4, 6, 8, 10, 12, 14, 16, 18 and 20. PINNED, measured 2026-10-04 at `580dc980`.

### Mechanism

The conf line this repo declares:

```
RECALL_EXCLUDE="memory/archive/*-v-[0-9]*-[0-9]*.md"
```

Matching uses the standard library's shell-style matcher over the repo-relative path, so `*` spans
a slash; the pattern is anchored at the memory root's archive directory to keep that from mattering.

### Inventory

No new function. The key is read where `RECALL_EXTRA_SOURCES` is read and filtered where the walk
already filters by extension; the arm is a test function under the selftest's existing naming.

### Files touched (estimate)

- `tools/memory-recall/recall_conf.py`
- `tools/memory-recall/extract.py`
- `tools/memory-recall/selftest.py`
- `tools/memory-recall/README.md`
- `.memory-tree.conf`

### Alternatives rejected

- **A literal glob in `corpus_files`.** It guesses an adopter's archive naming, and it cannot be
  turned off.
- **Ranking snapshots down instead of excluding them.** They are the same rule restated; a lower
  rank still spends a session's reading on text it must then discard.
- **Moving the snapshots out of the memory root.** That moves history other records cite by path,
  for a retrieval concern the conf can state.

## 5. Production-readiness checklist

- security — N/A: a read-side filter over tracked paths; no write path.
- perf / scale — one pattern match per corpus path; the corpus shrinks by about 440 KB.
- error / empty / loading states — blank excludes nothing; a pattern matching nothing is announced
  by S3; the digest move rebuilds a stale cache once.
- observability — S3's line and the module's print mode.
- risks — a broad pattern hides live records; the announcement names zero-match patterns only, so
  the declared pattern is scoped to the archive and the comment above it carries the measurement.
- testing — direct runs on the tree and a scratch clone, plus S5's arm.
- migration — every node's warm cache rebuilds once, on its first query after the change.
- user docs — S6's README row.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/query.py` runs on the tree after the pass with the
  question and terms recorded in §10, it prints at least ten hits and none of them is a path under
  `memory/archive/` with a versioned name. Red when: a snapshot path appears, or fewer than ten hits
  print, which would mean the corpus lost more than the snapshots.
  cost: the first query after the change rebuilds the cache.
  figure: the hit count DERIVED at observation time.
- **AC2** — When, in a `git clone --local` of the unit's branch under `%TEMP%`, the key is blanked in
  `.memory-tree.conf` as the staged break, the same query again returns snapshot paths.
  Red when: the snapshots stay out with the key blank, which would mean the walk excludes them by
  something other than the declaration.
- **AC3** — When `python tools/memory-recall/recall_conf.py` runs before and after the key's value
  changes in that clone, it prints the resolved `RECALL_EXCLUDE` and two different `CONF_DIGEST`
  values. Red when: the digest holds, so a warm cache would keep serving the snapshots.
- **AC4** — When, in that clone, the key names a pattern that matches nothing, the standard error of
  `python tools/memory-recall/query.py` carries one line naming that pattern.
  Red when: the zero-match pattern is silent.
- **AC5** — When `grep -n "RECALL_EXCLUDE" tools/memory-recall/README.md .memory-tree.conf` runs,
  the README's conf-key table carries the row and the conf carries the declaration under its comment.
  Red when: either file lacks the key.

## 7. Gates

`recall floor` · `recall floor arms` · `memory-recall kit selftest` · `hook destinations self-test` · `row-keyed merge driver replay` · `transition-audit arms` · `straggler-guard arms` · `kit/dogfood doc parity` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-recall/selftest.py · the gold arm of S5, a live guide and two versioned copies, staged red by blanking the key in its fixture conf · SELFTEST_ARMS moves by one

## 8. Open questions

- **F1 — A conf key or a literal glob?**
  Options: one glob in `corpus_files`; a declared key. The glob guesses every adopter's archive
  naming and cannot be turned off; the key costs one conf line and a digest entry.
  RESOLVED (agent, 2026-10-04, delegated): a declared key, `RECALL_EXCLUDE`.
- **F2 — Where is the gold arm answered by a live charter line?**
  Options: a question in the floor's fixture; an arm in the gov-only floor test; an arm in the
  adopter-run selftest over its own fixture corpus. The floor's targets are record ids and a charter
  line has none, and the charter itself is outside the corpus by design (§3). The selftest arm states
  the property, a live line answers and its archived copies do not, over a corpus that can fail.
  RESOLVED (agent, 2026-10-04, delegated): an arm in the adopter-run selftest.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `corpus_files`, `Conf.digest()`, the archive listing and a
  charter query on the tree.

## 10. Reuse audit

The seam is `corpus_files` in `tools/memory-recall/extract.py`, the one corpus walk both callers
share, extended by one filter; the key is read beside `RECALL_EXTRA_SOURCES` in
`tools/memory-recall/recall_conf.py` and joins the digest blob that key already joins.
`python tools/codebase-map/reuse_lookup.py "exclude archived files from the retrieval corpus walk"`
named `corpus_files` as a seam at fan-in 3, with `walk` in the memory-tree kit and `load_corpus` in
the codebase-map kit, neither a recall corpus. Recall returned `TOOL-aWalkedCorpus-1`, which
collapsed two corpus enumerators into this one walk so that a widening is taught once, and
`TOOL-aKeyedAnnotation-6`, which asks that a declared source yielding nothing be announced; S3 is
that announcement for the exclusion. Where the report and the tree disagree: the report proposed
skipping `AGENTS.md`, and it is not indexed today, because the corpus is rooted at the memory root.

The charter question AC1 re-runs: `python tools/memory-recall/query.py "what does the charter say about session-scoping every new id with a node tag slug" --terms "slug node tag CamelCase adjective-noun minted once per session collision grep re-roll FAMILY seq"`

Recall terms used: `python tools/memory-recall/query.py "why are archived versioned charter snapshots in the recall corpus and was excluding them considered" --terms "recall corpus corpus_files archive snapshot template-v exclude RECALL_EXTRA_SOURCES durable stale charter MEMORY_ROOT"`
