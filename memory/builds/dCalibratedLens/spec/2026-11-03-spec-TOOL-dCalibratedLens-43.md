# TOOL-dCalibratedLens-43 — `read_loop_records` lists the loop-review folder by prefix and filters by its id rule in Python, and a plant proves the listing is never empty

**Status:** DEFERRED · rev-1 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 3 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |
| [2026-11-03-build-TOOL-dCalibratedLens-43-deviation-431.md](../build/2026-11-03-build-TOOL-dCalibratedLens-43-deviation-431.md) | deviation | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 11, HIGH, item H2 of the round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`). `TOOL-dCalibratedLens-41` S11
and unit 3's r2 id-38 bullet prescribe `git ls-tree -r --name-only HEAD --
'memory/loop-review/*-loop-review-*.md'`. `git ls-tree` matches its paths as literal prefixes, never
as globs: the skeptic's re-run printed 0 names for a glob and the records for the folder prefix. Built
as written, the one reader of earlier records answers an empty list on every tree, so every caller
reads no history (units 5 S7, 6 S6, 15 S6, 16 S6, 17 S5 and unit 28's budget reader) and unit 6
falls back to 96,000 B. This unit makes the listing the folder prefix with the id rule applied in
Python, and adds the plant that proves the reader lists what is committed, skips what is not, and
never answers empty over a planted record. It repairs `TOOL-dCalibratedLens-3`, which builds the
reader.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text. Unit 3 (rev-4,
  r3 id 11) and unit 41 S11 (rev-2, id 11): `read_loop_records` lists
  `git ls-tree -r --name-only HEAD -- memory/loop-review/` and keeps a name only when
  `fnmatch.fnmatchcase(name, "memory/loop-review/*-loop-review-*.md")` holds, the revision it reads
  each record at and never the index. Unit 6 (rev-4, r3 id 11): its seventh criterion's plant also
  asserts that the committed record is in the listing, so its answer is non-empty. Observed by AC1.
- **S2** — The proof, a `--fixture` plant `records-listed` of `python loop_review.py --fixture` in
  `tools/loop/loop_review.py`. In a scratch repository it commits two loop-review records under
  their id rule and one file under `memory/loop-review/` that the rule does not match, then stages
  a third loop-review record without committing it, and calls `read_loop_records`. It holds when the
  answer lists exactly the two committed records, in file-name date order. It prints
  `records-listed — ok · 2 records`, and otherwise `records-listed — FAIL` with the names it read.
  Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Listing through `git ls-files`, the review's other wording. It reads the index, so a staged and
  uncommitted record would be listed and then read at `HEAD`, where it does not exist.
- A spec-token check that reds a `git ls-tree` pathspec carrying a glob metacharacter, the finding's
  left-shift line. The pathspec is spelled once, in the reader this unit holds.
- The reader's ordering and window: unit 3's id-30 bullet, unchanged.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-3` — `read_loop_records` and the `--fixture` frame of `loop_review.py`, which the plant calls; without them there is no reader to hold

## 4. Design

### Evidence

- The skeptic's probe on this repository: `git ls-tree -r --name-only HEAD --
  'memory/builds/*/prompts/*-run-mandate*.md'` printed 0 names, `git ls-files` over the same glob 21,
  and the folder prefix `memory/builds/dCalibratedLens/prompts/` 11 (finding id 11's row).
- `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-3.md:343-345`: the r2
  id-38 bullet's glob form.
- `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-41.md:70-73`: S11, the
  same command.
- `tools/memory-tree/tree_lib.py:278-299`: `read_git_output`, which raises `OSError` on a failed git
  call and returns bytes otherwise, the call the listing goes through.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `records-listed` | `--fixture` plant name | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2, the plant; the listing of S1 is unit 3's own code

### Alternatives rejected

- **`:(glob)` pathspec magic on `git ls-tree`.** Probed at base (2026-11-03): `ls-tree` answers
  `fatal: ... pathspec magic not supported by this command: 'glob'`.
- **`git grep -l` over `HEAD`.** It lists by content, not by name, and needs a pattern every record
  carries.

## 5. Production-readiness checklist

- security — reads only; the listing's argv is constant.
- perf / scale — one `ls-tree` over one folder per walk.
- error / empty / loading states — an empty folder answers `[]`; the plant holds that a planted
  record is listed, so an empty answer over a record reds.
- observability — the plant prints the names it read on failure.
- risks — a record kind added under `memory/loop-review/` with another id rule: the Python filter
  keeps only the loop-review rule.
- testing — AC1 and AC2 by the pass.
- migration — N/A: no record exists at base.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python loop_review.py --fixture --plant records-listed` runs from the loop kit
  directory, it prints `records-listed — ok · 2 records`.
  Red when: the listing answers no record, lists the staged one, or lists the non-matching file.
  permission: `read_loop_records` is unit 3's, built at order 2.
- **AC2** — When the plant runs with the listing staged as the glob pathspec
  `memory/loop-review/*-loop-review-*.md` passed to `git ls-tree`, it prints
  `records-listed — FAIL` with no name read.
  Red when: the glob form passes, so the empty listing is unobserved.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC1 AC2 · the `records-listed` plant, staged red by the glob pathspec passed to `git ls-tree` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, promoted from id 11 (HIGH, item H2) of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`; units 3, 6 and 41 amended at the disposal
  (their rev-4, rev-4 and rev-2).

## 10. Reuse audit

The seam extended is unit 3's `read_loop_records` and its `--fixture` frame, and the git call goes
through `tree_lib.read_git_output`, the shared reader. `python tools/codebase-map/reuse_lookup.py
"list committed files under a folder at a revision and filter them by a glob"` ranked name stems
only (`corpus_files`, `read_id_list`, `resolve_kit_file`); none lists a revision's tree by prefix,
and the loop kit is absent at base, so the listing stays in unit 3's reader.

Recall terms used: `python tools/memory-recall/query.py "how does a fixture plant refuse an
interface or a listing that answers nothing" --terms "fixture plant case unread signature
derive_record_kind ls-tree pathspec glob empty listing vacuous"`
