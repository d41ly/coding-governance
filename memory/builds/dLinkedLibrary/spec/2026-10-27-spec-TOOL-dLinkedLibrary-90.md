# TOOL-dLinkedLibrary-90 — the CI census reads every CI file through one decoder that drops a UTF-8 BOM and every line's CR, in every dialect

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 34 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-27-build-TOOL-dLinkedLibrary-87-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-87-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-91 |
| [2026-10-27-build-TOOL-dLinkedLibrary-90-deviation-901.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-90-deviation-901.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-87-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-87-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-91 |
| [2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-91 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 81 to 86
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md`) confirmed
finding **id 33 at HIGH**, report item **H4**. No other id shares the item.

`TOOL-dLinkedLibrary-86` S2 strips each line's trailing CR, and no census spec says how a CI file is
decoded, so a leading U+FEFF survives a plain UTF-8 decode. A BOM-led first line, `before_script: [npm
publish]`, `variables: *creds`, `default: *base` or `include:`, then no longer matches its key: the
file-wide and global-key refusals do not fire and the jobs grade `importable`. 86 AC2 plants CRLF in the
GitLab and GitHub files and never in `azure-pipelines.yml`.

This unit gives the census one CI-file decoder, which every dialect's reader takes its lines from: it
drops a leading BOM and strips the CR from every line. It plants a BOM-led CRLF file in each dialect. It
repairs `TOOL-dLinkedLibrary-86` and builds one step after it (order 34).

## 2. Scope (IN)

- **S1** — The decoder. `tools/memory-tree/adopt_program.py` holds one function, `ci_lines`, that
  takes a CI file's bytes as the census reads them at the scanned SHA and returns its lines. It decodes
  with `utf-8-sig`, which reads past one leading U+FEFF, using `errors="replace"`, and strips one trailing CR
  from every line. Observed by AC1 to AC4.
- **S2** — One path. The GitHub, GitLab and Azure job readers of the `ci-job` class take their lines
  from `ci_lines` and decode a CI file nowhere else, so 86 S2's CR strip happens once, in S1, before 77's
  header, 73's extent, 78 S2's continuation and every refusal pattern apply. Observed by AC4.
- **S3** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of its
  own whose CI file opens with the bytes `EF BB BF` and ends every line with CR LF: a `.gitlab-ci.yml`
  whose first line is `before_script: [npm publish]`, over two plain jobs, `test` running `npm test` and
  `lint` running `npm run lint`; an `azure-pipelines.yml` whose first line is `jobs:`, holding a job
  `publish` whose step `- bash: |` block holds `npm publish` and a job `test` whose step is `- script: npm
  test`; and a GitHub workflow under `.github/workflows/` whose first line is `jobs:`, holding a job
  `release` whose step is `- run: npm publish` and a job `test` whose step is `- run: npm test`. Observed
  by AC1 to AC3.

## 3. Non-goals (OUT)

- UTF-16 or other non-UTF-8 CI files: GitLab, GitHub and Azure read their pipeline files as UTF-8, and
  §5 states what S1's replacement does with stray bytes.
- What a refusal reads: 63, 71, 77, 78, 79 and 84 are unchanged; this unit changes only the text they
  receive.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-86` — S2's per-line CR strip and AC2's CRLF plants, which S1 and S2 move into one decoder that also drops a BOM, extended to every dialect (id 33)
- **consumes-from** `TOOL-dLinkedLibrary-84` — S3's global `before_script:` reading, which S3's BOM-led GitLab plant grades through (id 33)
- **hands-off** `TOOL-dLinkedLibrary-92` — S3's BOM-led CRLF plants, which unit 92 commits as raw bytes and proves kept before AC1 to AC3 grade them (id 7)
- **hands-off** `TOOL-dLinkedLibrary-93` — S1's `ci_lines` and S2's one read path, which unit 93 gives a stated LF-only split and a refusal for every other line break (id 21)
- **hands-off** `TOOL-dLinkedLibrary-96` — S1, S2, S3, AC4, §7 and §10, which unit 96's S5 to S9 widen to every CI-text reader, plant and seat on `read_blobs_at` at this unit's pass, and the map re-render, by S12 (ids 4, 18, 28, 8, 14, 11)

## 4. Design

### Evidence

- 86 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-86.md`, S2) strips only the trailing CR; 86 AC2 plants CRLF
  in a `.gitlab-ci.yml` and a GitHub workflow.
- `git grep -n "utf-8-sig" -- tools` prints one decode, in `tools/gate-lint/ps-hygiene.py:161`, and no
  census reader; `tools/memory-tree/adopt_program.py` is absent at base.
- `tools/drift-audit/drift_report.py:136-137` strips a leading `﻿` from a conf because a BOM-led file
  is a real Windows artifact.
- 63 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-63.md`, S1) reads Azure's `bash` key, so the Azure plant's
  `- bash: |` block is a line the census reads.

### Why a BOM hides a whole file

With the BOM kept, the first line reads `﻿jobs:` or `﻿before_script:`. A reader matching a
column-0 key misses it, so the census either finds no job in the file or misses a key that reaches
every job. Neither prints a refusal, and the first prints no row at all, which no refusal criterion
sees; S3's Azure and GitHub plants therefore require both jobs' rows to exist.

### Rollout

Order 34, one step after `TOOL-dLinkedLibrary-86`, whose CR strip S1 absorbs.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S3

### Alternatives rejected

- **Stripping U+FEFF in each dialect reader.** Three copies of one rule, and the next reader misses it;
  S2's single path is the class closed.
- **Strict decoding that refuses a file which is not valid UTF-8.** A stray byte would raise inside the
  census; replacement keeps every ASCII key byte, so each key and refusal pattern still matches.

## 5. Production-readiness checklist

- security — closes the import of jobs from a BOM-led CI file whose first line carries a key that
  refuses; deny by default holds on Windows-saved files.
- perf / scale — one decode per CI file, as before.
- error / empty / loading states — an empty file decodes to no lines; a stray non-UTF-8 byte becomes
  U+FFFD and the key bytes around it still match.
- observability — unchanged: each refusal names its reason as before.
- risks — a UTF-16 file decodes to text matching no key and prints no row; no forge reads such a file.
- testing — S3's plants under `adopt_program.py --fixture`, AC4's structural probe.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — none under `help/`: no refusal or reason changes.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both plain
  jobs of the BOM-led CRLF `.gitlab-ci.yml` read `refused: npm publish`.
  Red when: the BOM is kept and the first line's `before_script:` reaches no job.
- **AC2** — When the same plant runs, the BOM-led CRLF `azure-pipelines.yml` prints a row for each of its
  two jobs, `publish` reading `refused: npm publish` and `test` reading `importable`.
  Red when: the BOM hides `jobs:` and no row prints, or a CR on `- bash: |` reads the block as a plain
  scalar.
- **AC3** — When the same plant runs, the BOM-led CRLF GitHub workflow prints a row for each of its two
  jobs, `release` reading `refused: npm publish` and `test` reading `importable`.
  Red when: the BOM hides `jobs:` and no row prints.
- **AC4** — When `python -I -c` walks `adopt_program.py` with `ast`, it prints one `decode` call whose
  encoding is `utf-8-sig`, inside `ci_lines`, prints each dialect reader of the `ci-job` class beside its
  call of `ci_lines`, and prints no other `decode` call inside those readers; over a scratch copy whose
  Azure reader decodes its own bytes with `utf-8`, it names that reader.
  Red when: a dialect reads a CI file by a second decode that keeps the BOM.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's three BOM-led CRLF trees, one per dialect, the failing case staged by a plain `utf-8` decode · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 81 to 86, id 33 (HIGH, item
  H4).
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 92, 93 and 96, the mirrors of the
  consumes-from edges their specs declare, promoted from the spec audit of units 87 to 91;
  no scope or criterion moved.

## 10. Reuse audit

The seam extended is the census's CI-file read inside `TOOL-dLinkedLibrary-8`'s `ci-job` class in
`tools/memory-tree/adopt_program.py`, where 86 S2 already strips the CR; S1 makes that one function.
`python tools/codebase-map/reuse_lookup.py "decode a text file stripping a utf-8 byte order mark and crlf
line endings"` ranked `read_text`, `write_text`, `check_line` and `load_text`. The nearest,
`read_text` in `tools/memory-tree/tree_lib.py:383-387`, opens a worktree path and decodes plain `utf-8`,
so it keeps a BOM and reads no blob at a SHA; no existing seam fits beyond the census being extended.

Recall terms used: `python tools/memory-recall/query.py "how is a ci file decoded with a byte order mark or crlf" --terms "census ci-job bom utf-8-sig crlf decode line ending reader dialect refused"`
