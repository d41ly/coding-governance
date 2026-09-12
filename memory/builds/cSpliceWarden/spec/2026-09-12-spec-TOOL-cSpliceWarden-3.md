# TOOL-cSpliceWarden-3 — hygiene check 20 scans a rotated backlog shard

**Status:** SPECCED · rev-1 · 2026-09-12 · node c · Tier-2 · base 09a22d2b · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`row_grammar.row_docs()` keeps an archive only when its basename starts with `DECISIONS.`, so all
three rotated backlog shards are unscanned and two duplicated ids have sat in
`memory/archive/TOOL.2026-08-17.md` past a green bar since the day it was written. Widen the
population to every rotated row document, on the enumeration contract `TOOL-cSpliceWarden-2` §10
specifies.

## 2. Scope (IN)

- **S1** — `row_docs()` recognises a rotated archive by the enumeration contract: flat,
  `<STEM>.<iso-date><suffix?>.md`, `<STEM>` being `DECISIONS` or a declared `FAMILIES` value.
  Observed by **AC1**.
- **S2** — the family derivation is lifted out of `id_pattern()` so `row_docs()` and `id_pattern()`
  read ONE derivation, not two. Observed by **AC1**.
- **S3** — self-test arms: a duplicate inside a rotated BACKLOG archive is found and named with its
  lines, and a frozen non-row file under `archive/` is NOT scanned. Observed by **AC2**, **AC3**.
- **S4** — one arm asserts that check 10's shell enumeration and `row_docs()`'s Python enumeration
  select the same set over the real tree, so the contract has a grader rather than a promise.
  Observed by **AC4**.
- **S5** — `KIT_MEMORY_TREE_VERSION` bumped and `memory/map/generated/symbols.json` re-rendered in
  the same commit. Observed by **AC5**.

## 3. Non-goals (OUT)

- Moving `ROW_DUPLICATE_PIN`. It stays 3, and the ORDER is what keeps it there: unit 4 lands first.
  Measured — the widened scan returns 5 duplicates on today's tree and 3 once the evacuation drops
  the two stale rows.
- Corpus-wide id uniqueness. The dossier records that as a named gap and records why: it would red 19
  ids on day one, every one of them the designed backlog-row-plus-decision-row pair. Per-file
  uniqueness is the assertion, and the widening does not change that.
- Grading the declared `ROTATION_MODE`. Nothing in this build asserts an archive holds terminal rows
  only; see §8.

### Edges

- **consumes-from** `TOOL-cSpliceWarden-1` — that unit declares `ROTATION_MODE`, the mode whose
  archives this widening brings into scope.
- **consumes-from** `TOOL-cSpliceWarden-2` — the enumeration contract is specified in that unit's §10
  and is not restated here.
- **consumes-from** `TOOL-cSpliceWarden-4` — the evacuation must land first, or the exact-match pin
  forces a wrong-way move and a second commit to undo it.

## 4. Design

### Data model

| measurement | today | after unit 4 |
|---|---|---|
| files scanned | 6 | 9 |
| rows keyed | 698 | 859 → 793 |
| duplicate ids | 3 | 5 → 3 |
| `unkeyed` in the newly reached files | — | 0 |
| unterminated fences in the newly reached files | — | 0 |

All five figures are DERIVED — measured 2026-09-12 at `09a22d2b` by running the real `scan()` over the
real files with a widened `row_docs`, not reasoned about. Re-derive with
`python tools/memory-tree/row_grammar.py --report`.

**Why the population is not "every `.md` under `archive/`".** That sweeps in eight frozen charter
snapshots and four retired ledger shards. They contribute no keyed rows today, so the naive widening
looks harmless — measured, it changes the row count by nothing and the `loose` count by seven. But a
quoted example row inside a frozen document would then red the `unkeyed` branch on a file nobody is
permitted to edit, and the remedy would be to edit it. The contract's `FAMILIES` half exists for
that, and this is the near-miss that justifies it.

### Migration

None in this repo. For an ADOPTER the widening arrives with a kit upgrade and can red a bar with no
change of their own, because a pre-existing duplicate in a rotated shard becomes visible. Their
remedy is the duplicate, not the pin — the pin is shrink-only, so raising it is a weakening move
caused by our upgrade. That sentence goes in the kit README's upgrade note, which is part of S5.

### Files touched (estimate)

`tools/memory-tree/row_grammar.py` · `tools/memory-tree/row_grammar.py` self-test section ·
`tools/memory-tree/check-memory-hygiene.sh` (`KIT_MEMORY_TREE_VERSION` only) ·
`tools/memory-tree/README.md` (upgrade note) · `memory/map/generated/symbols.json` (RENDERED) ·
`memory/map/features/row-grammar.md` (the dossier's named gap moves).

### Alternatives rejected

- **Resolve the archive's stem against a live index, as check 10 does.** Rejected for this reader:
  deleting a shard would then silently remove its archives from the scan, which is the vacuity class
  this module's own header is about. Check 10 wants resolution because its question is "which index
  should name this"; check 20's question is "is this a row document", and a declared answer cannot
  narrow behind your back.

## 5. Production-readiness checklist

- security — N/A — a read-only scan of tracked text.
- perf / scale — 161 more rows through a regex-over-text scan, against the leg's declared ceiling.
  Noise.
- error / empty / loading states — the empty case is the one that mattered and is S3's negative arm:
  a widening that selects nothing prints what a clean scan prints.
- observability — every duplicate is named with path, id and every line it sits on, which the module
  already does and the widening inherits.
- risks — the pin is EXACT in both directions, so ordering against unit 4 is a real hazard and is
  §3's first non-goal. `check-verdict-epoch.sh` lists `row_grammar.py` as a delegate, so a
  behaviour-bearing change there forces the kit version bump in S5 or that leg reds.
- testing — AC1-AC5. The break is free: it is in the tree today.
- migration — see §4; the adopter note is the deliverable.
- user docs — `tools/memory-tree/README.md`'s upgrade note.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/row_grammar.py --report` runs after S1, its document list
  includes `memory/archive/TOOL.2026-08-14.md`, `TOOL.2026-08-17.md` and `TOOL.2026-08-17b.md`, and
  excludes every `parallel-coding-governance.template-v-2-*.md` and every `memory/archive/ledger/*.md`.
  Red when: the list is unchanged, or grows to include the frozen snapshots.
- **AC2** — When the self-test's new fixture writes a rotated backlog archive carrying one id twice,
  `python tools/memory-tree/row_grammar.py --selftest` names that archive and both line numbers.
  Red when: the arm passes before `row_docs` is widened, which would mean the fixture never entered
  the scan.
  fixture: the archive must be written BEFORE `_tree`'s `git add -A`, because `row_docs` enumerates
  through `git ls-files` — an untracked fixture passes by finding nothing.
- **AC3** — When the self-test writes a non-row `.md` under `archive/` carrying a dash-led id,
  `--selftest` does NOT report it.
  Red when: the scope negative is absent, so nothing pins the narrow predicate against the naive one.
- **AC4** — When the cross-reader arm runs, check 10's shell enumeration and `row_docs()`'s Python
  enumeration return identical sorted sets over this tree.
  Red when: one reader is edited and the other is not — the two-answers-to-one-question class this
  arm exists to convert into a red bar.
- **AC5** — When `bash tools/memory-tree/check-verdict-epoch.sh` and
  `python tools/codebase-map/map_check.py` run, both exit 0.
  Red when: the kit version did not bump for a behaviour-bearing delegate change, or `symbols.json`
  was not re-rendered for the changed signature.

## 7. Gates

`memory hygiene` · `row-grammar selftest` · `memory-hygiene self-test` · `kit version markers` · `verdict epoch (kit version dates the engine)`

New arm: `tools/memory-tree/row_grammar.py --selftest` · a rotated backlog archive carrying a duplicate id, plus a frozen non-row file under `archive/` as the scope negative · no assertion floor moves — `ARMS_FLOORS` pins shell gates defining `fail() {`, and this module is Python.

## 8. Open questions

- **F1 — nothing grades the declared `ROTATION_MODE`.** After this build,
  `memory/archive/TOOL.2026-08-17.md` is repaired and `cut` is declared and documented, but no check
  asserts that a rotated shard archive holds terminal rows only, nor that no id sits in both a shard
  and its archive. Those two assertions are the left-shift §7 asks for on the finding this whole
  build exists to repair, and without them the same archive can re-form. It is deliberately OUT of
  scope: the owner's ratified scope of 2026-09-12 covers the repair, the declaration and the widening
  of checks 10 and 20, and a new grading check was not among the extras offered or approved.
  RESOLVED (agent, 2026-09-12, delegated): filed as a backlog row under this build's slug and named
  in the wrap-up as the one left-shift this build does not complete, rather than built unasked.

## 9. Revision log

- rev-1 · 2026-09-12 · the first draft.

## 10. Reuse audit

The seam this unit extends is `row_docs()` itself, the one function that answers "which documents
carry rows"; `reuse_lookup.py "backlog archive rotation reconcile status"` ranks `load_conf`
(fan-in 15) and `read` (fan-in 8) as the shared seams inside this module, and both are reused rather
than re-implemented. The enumeration rule is NOT restated here — it is specified once in
`TOOL-cSpliceWarden-2` §10, and S4 is the arm that joins the two readers of it.
Recall terms used: `rotation archive backlog terminal carry-forward index cap shard hygiene check ratified supersede reconcile`
