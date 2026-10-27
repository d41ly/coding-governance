# TOOL-dLinkedLibrary-44 — the resolve arm's default population: every comment line of every profiled file, not only files that carry a note

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 13 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-26-build-TOOL-dLinkedLibrary-44-deviation-441.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-44-deviation-441.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 22 at HIGH**, report item **R8**. No other id shares the item.

`TOOL-dLinkedLibrary-4` S3 limits the scanned files to those `git grep -l "gov:(note|feature|end)"`
returns, and its S7 grades only comment lines of scanned files, yet its Rollout says the default
`every-comment-ref` grades the existing comment citations. At base no tracked file outside the memory
root carries those words, so the default resolve arm grades nothing. `TOOL-dLinkedLibrary-11` seeds
`annotation-resolve-legacy` from it, an empty seed, and deletes drift's
`source_cited_ids_resolving_to_no_record`, which scans every tracked non-memory file and holds 2
findings today: a green gate over an empty population takes the place of a signal that read the
citations.

This unit gives `every-comment-ref` its own population, every comment line of every tracked file
outside the memory root the lexer can profile, and keeps the `gov:` narrowing for note rows alone. It
repairs `TOOL-dLinkedLibrary-4` and builds one step after it (order 13).

## 2. Scope (IN)

- **S1** — The population. `scan_comment_lines(root, rev=None)` in `tools/memory-tree/annotations.py`
  yields `(path, line, text)` for every comment line, through `extract_comment_spans`, of every tracked
  file outside the memory root whose profile `resolve_lex_profile` finds by extension or shebang
  (`TOOL-dLinkedLibrary-4` S4), with no `gov:` narrowing. Observed by AC1 and AC3.
- **S2** — The arm. Under `every-comment-ref`, `check_resolve` (`TOOL-dLinkedLibrary-4` S7) grades S1's
  lines; under `notes` it grades `refs=` of the rows `scan_annotations` returns, whose `gov:` narrowing
  (`TOOL-dLinkedLibrary-4` S3) is unchanged and applies to note rows only. Observed by AC1 and AC2.
- **S3** — The summary says what it read. Under `every-comment-ref` the arm prints `annotations: resolve:
  <n> comment line(s) over <f> file(s) · <k> findings`; it prints `unarmed` only when no tracked file
  outside the memory root has a profile, or, under `notes`, when no note exists. Observed by AC2 and
  AC3.
- **S4** — The seed is not empty. At this pass's tip, `annotations.py check --only resolve` under the
  default reads a non-zero count of comment lines, so `TOOL-dLinkedLibrary-11`'s seed reads the
  citations the drift signal read in comments. Observed by AC3.

## 3. Non-goals (OUT)

- The citation grammar of a `memory/` path in prose (globs, placeholders, `:line` tails): id 68's item
  in `TOOL-dLinkedLibrary-52`.
- The defined-id set `check_resolve` compares against: id 31's item in `TOOL-dLinkedLibrary-52`.
- Citations outside comment lines: `TOOL-dLinkedLibrary-4` S7 grades comment lines, which is the
  clause's population; an id in a string literal is not a citation.
- The legacy ledger and the deletion of the drift builder: `TOOL-dLinkedLibrary-11`'s.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-4` — `check_resolve`, `scan_annotations` and `extract_comment_spans`, whose default population S1 and S2 widen (id 22)
- **hands-off** `TOOL-dLinkedLibrary-11` — `scan_comment_lines`, the non-empty default population its `annotation-resolve-legacy` seed reads (id 22)
- **hands-off** `TOOL-dLinkedLibrary-52` — `scan_comment_lines`, the population unit 52's citation cut reads (id 68)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-4` §4 Evidence: `git grep -n -E "gov:(note|feature|end)\b" -- tools skills
  .githooks` returns no line at base.
- `build_source_cited_ids_with_no_record` (`tools/drift-audit/drift_report.py:2204`) reads every tracked
  file outside the memory root (:2236-2250), and its pin is
  `"source_cited_ids_resolving_to_no_record": 2` (`tools/drift-audit/drift_signals.py:308`).
- At HEAD `823440497`, `git ls-files` lists 473 tracked files outside `memory/`, 262 of them `.py`,
  `.sh`, `.js` or `.ts`, the population S1 profiles (PINNED at that commit).

### The two scopes

| `annotations.resolve-scope` | Lines graded | Population read by |
|---|---|---|
| `notes` | each note's `refs=` | `scan_annotations`, narrowed to files carrying `gov:` |
| `every-comment-ref` (default) | each id and `memory/` path in any comment line | `scan_comment_lines`, every profiled tracked file |

### Files touched (estimate)

- `tools/memory-tree/annotations.py`: S1 to S3, and the plants of §6

### Alternatives rejected

- **Narrowing the default to files with a note, and saying so.** It leaves the drift signal's
  population ungraded once unit 11 deletes that signal, the empty-gate shape the finding names.
- **Reading whole files, as the drift builder does.** The clause grades comment citations; a whole-file
  scan reads string literals and fixtures as citations.

## 5. Production-readiness checklist

- security — read-only over tracked blobs, through the lexer, no shell.
- perf / scale — the lexer over every profiled file once per run, 262 source files at `823440497`; the
  `annotations` leg's ceiling bounds it.
- error / empty / loading states — S3: `unarmed` only over a tree with no profiled file.
- observability — the summary prints lines, files and findings.
- risks — existing dangling comment citations red until unit 11's legacy holds them, as
  `TOOL-dLinkedLibrary-4` §5 already says; no leg runs the arm before that unit.
- testing — the plants of §6.
- migration — none.
- user docs — `help/annotations.md` already names the two scopes; no sentence changes.

## 6. Acceptance criteria

- **AC1** — When `python annotations.py --fixture --plant comment-ref-no-note` runs `check --only resolve`
  over a tree holding no `gov:` line and one plain comment citing an undefined id of an anchored slug,
  it exits 1 naming that line.
  Red when: the default grades nothing in a tree with no note.
- **AC2** — When the same plant runs under a planted `annotations.resolve-scope = "notes"`, it prints
  `annotations: resolve: unarmed` and exits 0.
  Red when: `notes` grades plain comments, or an empty note population prints a green count.
- **AC3** — When `python annotations.py check --only resolve` runs at this pass's tip under the default,
  its summary names a non-zero count of comment lines and files.
  Red when: the default reads zero lines over a tree holding profiled source files.
  figure: DERIVED at the pass; 262 profiled source files at `823440497`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/annotations.py · covers AC1 AC2 · the `comment-ref-no-note` plant under both scopes, the failing case staged by narrowing `every-comment-ref` to files carrying `gov:` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 4 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 22
  (HIGH, item R8).

## 10. Reuse audit

The seams extended are `TOOL-dLinkedLibrary-4`'s `extract_comment_spans` and `resolve_lex_profile` in
the lexer block, read for every profiled file rather than re-implemented, and `check_resolve`, whose
population S2 selects by scope. `python tools/codebase-map/reuse_lookup.py "read the paths a shell
command reads"` ranked `read`, `read_text` and `read_conf`, none a comment scanner, so no existing seam
fits beyond the lexer block.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
