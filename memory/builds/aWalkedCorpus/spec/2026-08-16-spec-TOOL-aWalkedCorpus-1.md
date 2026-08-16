# TOOL-aWalkedCorpus-1 — the two corpus enumerators become one

**Status:** SPECCED · rev-1 · 2026-08-16 · node a · Tier-2 · base b4f0cf1c · streams tooling

## 1. Goal

`memory-recall` walks its corpus in two places. Every widening has to teach both, and the last one
nearly shipped teaching only the first. Reduce it to one walk with an explicit parameter for the one
axis the two callers genuinely differ on, and correct the landed claim that this was already
recorded as a follow-up.

## 2. Scope (IN)

- **S1 — one enumerator, one axis of difference.** `extract.corpus_files(repo, rev)` lists TRACKED
  `.md` under `MEMORY_ROOT`; `query.corpus_files(repo)` lists tracked AND
  untracked-not-ignored, deliberately, because "a note written this session and not yet committed is
  exactly what a session needs to find" while the measurement path stays pinnable to a rev. That
  difference is REAL and is preserved: the surviving function takes it as a parameter rather than
  being duplicated for it.
- **S2 — the declared extra sources move with it.** `aDeclaredCeiling` added
  `resolve_declared_sources` and had to call it from both walks and from the digest. After S1 there
  is one call site inside the enumerator, and the callers stop knowing about it.
- **S3 — the false claim is corrected at its source.**
  `memory/builds/aDeclaredCeiling/spec/2026-08-16-spec-TOOL-aDeclaredCeiling-2.md:98` says
  "Recorded as the follow-up it is." It is amended in place to say what actually happened: the
  deferral was stated, no row was minted, and both were caught when the build was asked what it had
  left. The spec is CLOSED, so this is an amendment plus a rev bump and a §9 line — never a rewrite
  of what that unit built.
- **S4 — the backlog row closes.** `TOOL-aWalkedCorpus-1` in `memory/backlog/TOOL.md` moves to
  CLOSED. A row saying "unify the two walks" is not discharged by unifying them and leaving it open.
- **S5 — the arms.** `tools/memory-recall/selftest.py` gains one: the two callers see the two
  different file sets they are entitled to — an untracked-not-ignored note is visible to the query
  path and absent from the measurement path at a rev. That property is the whole reason the
  duplication existed, and nothing currently asserts it.

## 3. Non-goals (OUT)

- **Changing what either caller RETRIEVES.** This is a refactor: the same files reach the same
  index. S5 exists to prove that rather than to assert it.
- **Touching `bench.py`'s own corpus handling.** It consumes an extracted data dir, not a walk.
- **The recall quality floor.** `TOOL-aWalkedCorpus-2`, and it is sequenced after this unit so its
  measurement is taken against the corpus this one leaves.

## 4. Design

### What the two walks actually differ on

| | `extract.corpus_files` | `query.corpus_files` |
|---|---|---|
| tracked | yes | yes |
| untracked-not-ignored | no | YES |
| pinnable to a `rev` | yes | no |

Those are one axis, not two: "include the working tree's uncommitted additions" and "read a
revision instead" are the same switch seen from both ends. A single
`corpus_files(repo, rev=None, include_untracked=False)` covers both callers, with `rev` and
`include_untracked` mutually exclusive — a revision has no untracked files, and a call passing both
is a caller error worth refusing rather than silently resolving.

### Why not simply have query.py call extract's

Because the difference is real and would be lost. `query.py`'s docstring records it as deliberate,
and dropping untracked files from the query path would break the property a session depends on. The
duplication is the wrong fix for a genuine difference; a parameter is the right one.

### Where the risk is

The refactor is small and the danger is not in the code — it is that a silent behaviour change here
is invisible until someone's note stops being findable. S5 is written against exactly that: a real
untracked file, visible to one caller and not the other.

### Files touched

| File | Change |
|---|---|
| `tools/memory-recall/extract.py` | S1's parameterised walk, S2's single call site |
| `tools/memory-recall/query.py` | its own walk deleted; calls the shared one |
| `tools/memory-recall/selftest.py` | S5 |
| `memory/builds/aDeclaredCeiling/spec/2026-08-16-spec-TOOL-aDeclaredCeiling-2.md` | S3 + rev bump |
| `memory/backlog/TOOL.md` | S4 |

No depth-1 `tools/` path is created, so no `govkit` row is owed. `extract.py` is in the
verdict-epoch gate's DELEGATE set, so `KIT_MEMORY_TREE_VERSION` moves with this commit, and
`KIT_MEMORY_RECALL_VERSION` moves because the kit's own behaviour is refactored.

## 5. Production-readiness checklist

- security / perf / a11y / i18n — N/A. One function replaces two.
- error / empty / loading states — a call passing both `rev` and `include_untracked` is refused by
  name rather than resolved, per §4.
- observability — unchanged; neither walk prints.
- risks — a silent narrowing of the query path, invisible until a note goes missing. S5 is the guard
  and it is the reason this unit is Tier-2 rather than a tidy-up.
- testing + left-shift gates — S5, plus both kit versions moving so a stale cache cannot answer.
- migration / rollback — revert; the index is a derived cache.
- user docs — none: the walk is internal and the kit README documents the corpus, not the function.

## 6. Acceptance criteria

- **AC1** — When `grep -c "^def corpus_files" tools/memory-recall/extract.py
  tools/memory-recall/query.py` runs, it returns 1 and 0. One definition survives.
- **AC2** — When an untracked-not-ignored `.md` is created under `MEMORY_ROOT`, the QUERY path
  indexes it and the MEASUREMENT path at a rev does not. Both halves observed, because a refactor
  that quietly unified them would pass a one-sided check.
- **AC3** — When a caller passes both `rev` and `include_untracked`, it is refused by name.
- **AC4** — When `python tools/memory-recall/query.py` runs before and after this change on the same
  tree, the index reports the same record and chunk counts. The refactor moves no document.
- **AC5** — When `python tools/memory-recall/selftest.py` runs it exits 0, and inverting S5's arm
  reds it naming that arm.
- **AC6** — When `memory/builds/aDeclaredCeiling/spec/2026-08-16-spec-TOOL-aDeclaredCeiling-2.md:98`
  is read, it no longer claims a follow-up was recorded, and that spec's rev and §9 have both moved.
- **AC7** — When `grep -n "aWalkedCorpus-1" memory/backlog/TOOL.md` runs, the row is CLOSED.
- **AC8** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs it exits 0, so
  `KIT_MEMORY_TREE_VERSION` moved with the delegate.
- **AC9** — When `bash tools/run-gates.sh` runs, it is green.

## 7. Gates

- `python tools/memory-recall/selftest.py` — the kit's arms.
- `bash tools/memory-recall/adopt-memory-recall.sh --check` — Skill/conf parity.
- `bash tools/memory-tree/check-verdict-epoch.sh` · `bash tools/check-kit-versions.sh`.
- `bash tools/memory-tree/check-memory-hygiene.sh` — a CLOSED spec is edited.
- `python tools/drift-audit/drift_report.py --check` — confirm no signal moves.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. The cleanup was deferred by `TOOL-aDeclaredCeiling-2` §4 with
  the words "Recorded as the follow-up it is", and no row was minted — found when the build was
  asked what it had left, not by a review. S3 exists because a deferral nobody recorded and a
  deferral nobody made are indistinguishable a month later.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "enumerate the corpus of documents an index is built
from"` — the seam this unit collapses is `extract.corpus_files`, which the codebase map already
surfaces as the measurement path. There is no new seam; the unit REMOVES one.

`python tools/memory-recall/query.py "why does the query path see files the measurement path does
not" --terms "corpus enumerator tracked untracked ignored rev pinnable measurement query walk index
staged uncommitted"` — run before writing S1, and it is the reason the difference is preserved
rather than flattened: `query.py`'s own docstring is the record, and it states the intent directly.
Recorded per M5 including the terms, because M7 re-runs this query at the pass boundary.

**Verified against source rather than trusted:** both walks were read end to end before S1 was
written, and the table in §4 is measured from them, not inferred from their names — the failure that
produced a fabricated kit description two builds ago.
