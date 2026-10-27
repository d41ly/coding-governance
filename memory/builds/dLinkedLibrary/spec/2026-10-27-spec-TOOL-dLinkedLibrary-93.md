# TOOL-dLinkedLibrary-93 — the CI decoder splits on LF alone and refuses every job of a file holding any other line break

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 35 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-93-deviation-931.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-93-deviation-931.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 87 to 91
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md`) confirmed
finding **id 21 at HIGH**, report item **H2**. No other id shares the item.

`TOOL-dLinkedLibrary-90` S1's `ci_lines` strips one trailing CR from every line and never says what
splits a line. YAML treats a lone CR as a break, and GitLab's libyaml break test also accepts U+0085,
U+2028 and U+2029; other forges' parsers disagree on those. Split on LF only, a top-level `include:`
after a lone CR reads as part of the line before it, 71 S2's file-wide refusal never fires, and the
jobs grade `importable`. Split with `splitlines()`, a NEL inside a job line makes a column-0 key the
forge may not see. No single split matches every forge.

This unit makes the split deny by default: `ci_lines` splits on LF alone, and a file holding any other
character a YAML parser may read as a break refuses every job it holds. It repairs
`TOOL-dLinkedLibrary-90` and builds one step after it (order 35).

## 2. Scope (IN)

- **S1** — The split. In `tools/memory-tree/adopt_program.py`, `ci_lines` (90 S1) splits the decoded
  text on U+000A alone and strips one trailing U+000D from each line. It returns its lines and the first
  unreadable break, or none. An unreadable break is a U+000D not followed by U+000A, a U+0085, a U+2028
  or a U+2029, in file order. Observed by AC1 to AC3.
- **S2** — The refusal. A file whose `ci_lines` returns an unreadable break refuses every job its
  dialect reader finds, each reading `refused: unreadable line break U+<hex>`, the hex being the four
  upper-case digits of that first break. The refusal goes through `TOOL-dLinkedLibrary-71` S2's one
  file-wide function, the reason text being this unit's, in every dialect: 90 S2 routes the GitHub,
  GitLab and Azure readers through `ci_lines`. Observed by AC1 to AC3.
- **S3** — The plants, cases of `adopt_program.py --fixture --plant ci-census`, each a scratch tree of its
  own. Four `.gitlab-ci.yml` files, each LF-ended except for one planted character, holding a job `test`
  whose line `  script: [npm test]` is followed by the planted character and then `include: remote.yml`,
  and a job `lint` running `npm run lint` after it: the character is a lone CR in the first, U+0085 in the
  second, U+2028 in the third and U+2029 in the fourth. A GitHub workflow and an `azure-pipelines.yml`,
  each opening with the comment line `# saved by a legacy editor` ended by a lone CR and holding two plain
  jobs, `release` running `./release.sh` and `test` running `npm test`. Observed by AC1 and AC2.
- **S4** — What stays readable. A CR followed by LF is a line end and never an unreadable break, so 90
  S3's BOM-led CRLF trees read as 90 AC1 to AC3 state. Observed by AC3.
- **S5** — The page. `help/adopt.md`'s census section carries the sentence "A CI file holding a line
  break other than LF or CR LF, a lone CR, U+0085, U+2028 or U+2029, refuses every job in the file as
  `unreadable line break`, because forges disagree on whether it ends a line." Observed by AC5.

## 3. Non-goals (OUT)

- Reading the file the way one forge's parser does: the census stays a text reader, as 63 §3 keeps it,
  and refuses what forges disagree on.
- A bug-class checklist entry that every security text reader names its line-break set: the report's
  left-shift, a separate record this unit does not write.
- U+000B, U+000C and other characters no YAML parser reads as a break: they stay inside a line.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-90` — S1's `ci_lines` and S2's one read path, which S1 gives a stated split and S2 a refusal for every break outside it (id 21)
- **consumes-from** `TOOL-dLinkedLibrary-71` — S2's one file-wide refusal function, which S2 calls with the `unreadable line break` reason (id 21)
- **hands-off** `TOOL-dLinkedLibrary-96` — S2's call into 71 S2's file-wide function, which unit 96 lists among the call sites 91 AC17 prints (id 21)
- **hands-off** `TOOL-dLinkedLibrary-102` — S1 to S3, §5 and AC3, which unit 102's S4 to S7 plant, order and record at this unit's pass, §4's cites, by its S20, and the naming leg at this pass, by its S21 (ids 4, 26, 19, 12, 8, 20)

## 4. Design

### Evidence

- 90 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-90.md:36-39`) names the decode and the CR strip and no
  split; 90 §5 (`:99-110`) covers stray bytes and empty files only.
- 71 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-71.md`, S2) refuses every job of a file holding a
  top-level `include:`; 86 S7 makes it one function every file-wide hit calls, the reason text the
  caller's.
- A scratch repository under `%TEMP%` on this node, under the inherited `core.autocrlf=true`, committed
  a file holding a lone CR before `include:` and `git cat-file -p HEAD:a.yml | od -c` still showed the
  `\r` (PINNED, 2026-10-27): git's text conversion folds CR LF only, so S3's lone-CR plants keep their
  byte. U+0085, U+2028 and U+2029 are multi-byte UTF-8 and no conversion touches them.
- 90 S1 decodes with `errors="replace"`, so a stray single byte `85` reads U+FFFD, not U+0085; only an
  encoded NEL is a break here.

### A GitLab file under S1 and S2

```text
test:
  script: [npm test]<U+0085>include: remote.yml     # refused: unreadable line break U+0085
lint:
  script: [npm run lint]                             # refused: unreadable line break U+0085
```

Under an LF-only split with no S2 the `include:` sits inside `test`'s line and both jobs read
`importable`. Under `splitlines()` it is a top-level key and both read `refused: opaque step include
remote.yml`, the reason of a parser the forge may not match. S2's reason tells this unit's rule from
both.

### Rollout

Order 35, one step after `TOOL-dLinkedLibrary-90`, beside `TOOL-dLinkedLibrary-91` and
`TOOL-dLinkedLibrary-92`. All three write `adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences
the passes. If the pass adds a function, it re-renders the generated map with `python
tools/codebase-map/gen_map.py --write` where its `--check` exits 1, in the pass commit.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4
- `help/adopt.md`: S5
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: the Rollout re-render

### Alternatives rejected

- **Splitting on every YAML break.** GitLab's parser would agree and other forges' would not, so a
  file reads one way here and another at a forge; the refusal holds for every parser.
- **Splitting on LF and saying nothing of the rest.** It is the defect: a lone CR hides a top-level
  key from the census.
- **Refusing only the job whose line holds the break.** A break can make a column-0 key out of a job
  line, so the file's job set itself is unknown; S2 refuses all of it, as 71 S2 does for `include:`.

## 5. Production-readiness checklist

- security — closes the import of jobs from a CI file whose line structure forges read differently;
  deny by default.
- perf / scale — one scan of the decoded text per file.
- error / empty / loading states — an empty file holds no break; a stray byte reads U+FFFD and is no
  break.
- observability — each refusal names the break's code point.
- risks — a file saved by a legacy Mac editor refuses its jobs; the owner may rule a job in.
- testing — S3's plants under `adopt_program.py --fixture`, AC4's scratch copies.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — `help/adopt.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both jobs of
  each of S3's four `.gitlab-ci.yml` trees read `refused: unreadable line break` with, in turn, `U+000D`,
  `U+0085`, `U+2028` and `U+2029`.
  Red when: a break character outside LF is split on, or not seen, and the jobs read another reason or
  `importable`.
- **AC2** — When the same plant runs, both jobs of S3's GitHub workflow and of its `azure-pipelines.yml`
  read `refused: unreadable line break U+000D`.
  Red when: a dialect reader splits its own text and misses the lone CR.
- **AC3** — When the same plant runs, no line of 90 S3's three BOM-led CRLF trees reads `unreadable line
  break`.
  Red when: a CR before LF is taken for a lone CR.
- **AC4** — When a scratch copy of `adopt_program.py` without S1's break scan runs the same plant by
  `python -I`, both jobs of the lone-CR GitLab tree print `importable`; when a copy whose `ci_lines`
  splits with `splitlines()` and holds no scan runs it, both jobs of the U+0085 tree print `refused:
  opaque step include remote.yml`.
  Red when: a staged break leaves AC1's reason in place, so the plant does not discriminate the rule.
- **AC5** — When `grep -n 'unreadable line break'` runs over the help page `adopt.md` (its path in
  Files touched) at this tip, it prints S5's sentence, and over the page at this pass's start, read with
  `git show`, it prints nothing.
  Red when: the refusal ships with no line on the page.

## 7. Gates

`codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 · the `ci-census` plant's four GitLab break trees and its GitHub and Azure lone-CR trees, the failing case staged by an LF-only split with no break scan · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 87 to 91, id 21 (HIGH, item
  H2), on the skeptic's corrected fix.
- rev-2 · 2026-10-27 · §3 · the hands-off edge to unit 102, the mirror of the
  consumes-from edge its spec declares, promoted from the spec audit of units 92 to 96;
  no scope or criterion moved.

## 10. Reuse audit

The seam extended is 90 S1's `ci_lines` in `tools/memory-tree/adopt_program.py`, with
`TOOL-dLinkedLibrary-71` S2's one file-wide refusal function reused for the refusal. `python
tools/codebase-map/reuse_lookup.py "split text into lines on line feed only and refuse other line
breaks"` ranked `read_text`, `write_text`, `check_line` and `CensusRefused`; `CensusRefused`
(`tools/process-monitor/census.py`) is a process census's error and reads no CI file, so no existing
seam fits beyond the decoder being extended.

Recall terms used: `python tools/memory-recall/query.py "what splits a ci file into lines and which line breaks does the census refuse" --terms "census ci_lines line break lone cr nel decode refused file-wide include dialect reader"`
