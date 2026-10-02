# TOOL-aSightedSkeptic-9 — the replay benchmark: a review scored for recall against a past round

**Status:** CLOSED · rev-3 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 9 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-10 TOOL-aSightedSkeptic-13 |
| [2026-10-01-build-TOOL-aSightedSkeptic-9-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-9-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-build-TOOL-aSightedSkeptic-9-2-live-replay.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-9-2-live-replay.md) | journal | — |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-2-3-fold-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-2-3-fold-brief.md) | journal | TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-9-2-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-9-2-build-brief.md) | journal | — |
| [2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md](../reviews/2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md) | diff-review | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 |

<!-- /gen:spec-records -->

## 1. Goal

Make the review harness's recall measurable. A stdlib Python tool reads a past closing diff review's
confirmed findings and its reviewed range, and scores a candidate review of that same range against
them. The candidate is the appendix unit 8 adds to every report. Today nothing in this repo can say
whether a lens set or a prompt change finds MORE of what a previous review proved real. Every
harness change in this build is therefore chosen by argument, and this unit is what lets the next
one be chosen by measurement.

## 2. Scope (IN)

- **S1** — A new tool, review_replay.py, in the review-harness kit directory. It is stdlib only,
  runs under the repo's python launcher, and names no path outside its own kit by literal, its
  docstring's usage lines included. Every population it reads arrives as an argument. Observed by
  AC1 and AC4.
- **S2** — The KNOWN set. `--known <record>` extracts a past diff-review record's confirmed
  findings, each with its location as file and line, plus the record's reviewed range. Two record
  shapes are read, in this order, and each has its own UNIT. A record carrying the unit-8 appendix
  is read from that appendix, one known entry per RAW confirmed finding. Any other record is read
  from its legacy item table, one entry per adjudicated item (§4, "Known-set extraction"). The
  `replay: known` line prints the unit. Observed by AC1.
- **S3** — The LIVENESS assertion on the known set. The record's own stated confirmed count must be
  reproduced from what was extracted, or the record is REFUSED with exit 2, naming both numbers.
  A record with zero scorable items is refused the same way. This is the guard against a parser that
  returns some of a population and reads as success. Observed by AC1 and AC2.
- **S4** — The CANDIDATE set. `--candidate <report>` reads the `## Appendix — every finding` table of
  a report written by the harness after unit 8. Columns are found by HEADER NAME, never by position.
  Only rows whose `verdict` is `confirmed` are candidates. The confirmed row count must equal the
  report's stated confirmed count, else exit 2. An absent appendix is exit 2. A confirmed row whose
  ref names no file and line is UNSCORABLE: the candidate line prints their count, and a report
  whose confirmed rows are all unscorable is refused with exit 2. One function maps appendix rows to
  candidates, and both `main` and the self-test call it. Observed by AC1.
- **S5** — The SCORE. A known item is MATCHED when some candidate is in the same file and within a
  declared line window, `--window`, default 10. The tool prints matched, missed and candidate-only
  findings, a per-lens line of candidate confirmed and matched counts, and recall as matched over
  scorable known items. It decides nothing: a scored run exits 0 at any recall. Observed by AC1.
- **S6** — The CORPUS. `--corpus <dir>...` walks the given directories for markdown records whose
  first non-blank line is the harness's own `**Serves:** diff-review` binding line. It lists each
  record that passes S3 and whose range resolves in this clone, with its round, base, head and
  scorable item count. It ends with one summary line: records scanned, listed, and refused per
  reason, which sum to the scanned count. Range resolution is ONE git process for the whole corpus.
  Observed by AC3 and AC5.
- **S7** — `--selftest`, with inline fixtures and no file or git access. It runs a declared, named
  set of arms, including one that MUST score below 1.0, and fails when the number of arms run
  differs from the number declared. Observed by AC1 and AC2.
- **S8** — A held gate leg, `review-replay selftest`, running the S7 flag. It is declared in
  `tools/gate-legs.json` and as a `[[gate_leg]]` in `tools/workflows/kit.toml`, with subject `kit`,
  chunk `selftests` and NO guard, so it runs on every self-test bar. It is claimed in the review-harnesses map
  dossier, and the generated subject pins and map artifacts are re-rendered in the same commit.
  Observed by AC6.
- **S9** — The kit README documents the three modes, the live-replay procedure in §4, and what the
  score does not mean. Observed by AC7.
- **S10** — The LIVE replay: one real harness run over a past round-1 range, scored by S5. It is the
  main loop's act at `VERIFYING` and not a unit pass's. Observed by AC8.

## 3. Non-goals (OUT)

- No `Workflow` run from inside the tool. A workflow script cannot be launched from Python, and a
  unit pass does not hold the tool. The live replay is the main loop's (S10).
- No precision figure against ground truth. A candidate-only finding may be a real defect the past
  review missed, so it is listed and never counted as a false positive.
- No A/B mode comparing two harness versions in one call. Two scored runs printed side by side are
  the comparison, and the owner reads them.
- No JSON ledger input. The harness return value carries `ledger` and `confirmedFindings` (unit 8),
  but a return value is not on disk unless a caller writes it. The report appendix is the durable
  artifact every caller already has.
- No change to `tools/workflows/tier2-review.template.js` or its render. This unit reads the report
  the harness writes and edits nothing in the harness.
- No version move. Invariant 9 of the shared brief moves the harness version once, in unit 5, for
  the whole build. The new file ships under that one move.
- No governance carrier is edited (shared brief invariant 8). M8's invocation block in the build
  method does not mention the replay, and this unit does not add it there. If the owner wants the
  close to run a replay, that is a carrier edit, and the main loop parks it.
- Not a merge-bar leg. The leg in S8 is held under the 2026-08-23 kit-self-test ruling and runs only
  when the self-tests are asked for.

### Edges

- **consumes-from** `TOOL-aSightedSkeptic-8` — the `## Appendix — every finding` table, its header
  names `id`, `lens`, `ref`, `severity`, `skepticSeverity`, `verdict`, `reason` and `fixVerdict`, the
  finding field `lens`, and the report's stated confirmed count. Without that appendix S4 has no
  input, and AC8 cannot run.
- **consumes-from** external — the `Workflow` tool, held only by the main loop, which runs the live
  replay of S10.
- **hands-off** external — the live replay and its acceptance-ledger line, owed by the main loop at
  `VERIFYING` after every unit of this build is built.

## 4. Design

One file, one `main`, plain functions, no classes. Every text read names `encoding="utf-8"`, which
the `encoding posture` leg grades. Exit codes are 0 for a scored run or a listed corpus, 1 for a
red self-test, and 2 for any refusal or argument error.

### Known-set extraction

The unit of a known finding depends on the record's era, and the `replay: known` line prints it.
A LEGACY record's unit is the ADJUDICATED ITEM, not the raw confirmed finding: it does not carry
the text or location of each raw finding, only item rows naming the raw ids they merged. F2
records the probe that decided this, and F2 governs the legacy path. An APPENDIX record's unit is
the RAW confirmed finding (`raw-finding`), because the unit-8 appendix carries one row per raw
finding, so a defect two lenses confirmed counts twice there. Recall from the two eras is in
different units, and the printed unit is what keeps a reader from comparing them as one.

Read in order, first hit wins:

1. **Appendix.** The record carries the unit-8 appendix heading. Rows whose `verdict` column is
   `confirmed` are the items, and each row's `ref` is its location. Liveness: the confirmed row
   count equals the record's stated confirmed count. Unit 8 pins the cell encoding, and this reader
   inverts it: a row splits on a `|` that no backslash precedes, `\|` reads as a literal bar, and a
   cell reading `-` is an absent value. A confirmed row whose `ref` is `-` is unscorable. Rows end
   at a newline only, after CRLF is normalised: `str.splitlines` also breaks on U+2028, `\x85` and
   others a cell may carry, and one cut row would end the table and drop every row after it.
2. **Legacy item table.** A row is an item row when its first cell is an item id, its second cell is
   a severity word in any case and with or without bold, and its LAST cell is a list of raw finding
   ids and nothing else. The location is the FIRST backticked file-and-line token in the row.
   Liveness: the union of the raw ids across every item row equals the record's stated confirmed
   count.

```text
| F1 | **BLOCKER** | `tools/workflows/kit.toml:61` | the claim | 3, 8 |      <- item row
| B1 | BLOCKER | 8 | §2 S6, §6 AC6 | the claim |                            <- not an item row
```

The stated confirmed count is the first number following the word `confirmed`, matched ignoring
case, with up to six non-word characters between them. That is the review-shape line the harness
asks every synthesis to write. An item row with no file-and-line token is UNSCORABLE. It is counted
and printed, and it leaves the recall denominator. The range is the first token of the form
hex-dot-dot-hex or hex-dot-dot-dot-hex, each side 7 to 40 hex characters. A range ending in a symbolic
name such as `HEAD` matches nothing and the record is refused as having no range.

### Matching

Both sides normalise a ref by stripping surrounding backticks, turning `\` into `/`, turning a
leading drive prefix such as `C:/` into `/` so the absolute suffix survives, and stripping a
leading `./`. A ref reading `<file>:<line>-<line>` takes its first line. Two paths name the
same file when they are equal, or when one ends with `/` followed by the other. That admits the
basename-only refs older records carry, at a known ceiling: two files sharing a basename can match.
The upgrade, if a scored run ever shows the collision, is to require the longer path on both sides.
A line matches when the absolute difference is at most `--window`. A known item matches when ANY
candidate matches it. A candidate that matches no known item is candidate-only.

### Output

```text
replay: known <record> · unit <raw-finding|adjudicated-item> · range <base>..<head> · items <n> · scorable <m> · unscorable <u>
replay: candidate <report> · confirmed <c> · unscorable <u> · window <w>
MATCHED         <known location>  <-  <candidate ref>  [<lens>]
MISSED          <known location>  <item id>
CANDIDATE-ONLY  <candidate ref>  [<lens>]
per-lens: <lens> confirmed <c> matched <k> · ...
replay: recall <k>/<m> = <0.00>
```

`--corpus` prints one line per listed record, `<path> · round <n|?> · <base>..<head> · scorable <m>`,
then `corpus: scanned <s> · listed <l> · refused <reason> <k> · ...`. The round is read from the
record's own `Round:` line, else from a `round<N>` filename tail, else printed as `?`. Ranges are
resolved by ONE `git cat-file --batch-check` process fed every sha, in the directory `--repo` names,
which defaults to the current one. On node `a` a git spawn costs about 751 ms (PINNED, the owner
memory on git spawn cost), so a spawn per record would cost minutes over the 194 records this tree
holds.

### Self-test arms

Each arm is a named function call over inline strings, and the runner prints `ok <name>` or
`FAIL <name>: <why>`, then `selftest: <passed>/<declared> arms`. It exits 1 on any failure, and also
when fewer arms ran than were declared.

| arm | what it pins |
|---|---|
| `known-legacy-parse` | two item rows naming raw ids 1, 2 and 3 against a stated count of 3 give two items |
| `known-liveness-refuses` | the same rows against a stated count of 4 are refused, both numbers named |
| `known-non-item-row` | a row whose last cell is prose is not an item row |
| `known-unscorable` | an item row with no file-and-line token is counted and leaves the denominator |
| `known-range` | both dot forms extract, and a range ending in `HEAD` is refused |
| `appendix-by-header` | appendix columns in a shuffled order are read by name |
| `appendix-cell-encoding` | a `\|` inside a cell does not split it, and a `ref` of `-` is unscorable |
| `appendix-liveness-refuses` | confirmed rows differing from the stated count are refused |
| `appendix-absent-refuses` | a report with no appendix heading is refused |
| `score-miss` | two known items, one matched: recall 0.50, and the other is printed MISSED |
| `score-refuted-ignored` | a refuted row at a known location does not match it |
| `window-edge` | a difference equal to the window matches, and one more line does not |
| `path-suffix` | a basename matches its full path, and two directories sharing a basename do not |
| `candidate-only` | a confirmed candidate matching nothing is listed as candidate-only |
| `known-unit-raw` | two confirmed appendix rows at one location are two `raw-finding` entries, and each header prints its unit |
| `drive-ref-candidate` | drive-lettered candidate refs, slash and backslash, parse and match a repo-relative known item |
| `drive-ref-known` | a drive-lettered known appendix ref is scorable and matches a repo-relative candidate |
| `candidate-unscorable-refuses` | all-unscorable confirmed candidates are refused; one unscorable of two is counted on the candidate line |
| `appendix-u2028-row` | a U+2028 inside a cell, on a CRLF table, cuts no row |

### Live replay — the main loop's procedure at VERIFYING

1. List: `python3 tools/workflows/review_replay.py --corpus memory/builds`, then pick a round-1 row.
2. Check out the record's head detached, in a short directory under `%TEMP%`, never inside the
   worktree: `git worktree add --detach <dir> <head>`.
3. Run `Workflow` with the run branch's `tools/workflows/tier2-review.js` as the script, `repo` set
   to that checkout, the record's base and head, round 1, no `priorFindings`, and a `reviewDir`
   inside the checkout. Every other argument is what this build's own close passes.
4. Score: `--known <record> --candidate <the report the run wrote>`.
5. Write the printed recall, matched, missed and per-lens lines to the acceptance ledger, then
   `git worktree remove` the checkout.

### Inventory

New Python function names, each answered OK by `python tools/lexicon/lexicon.py --suggest <name>
--as py.function` on 2026-10-01: `main`, `run_selftest`, `parse_record_findings`,
`parse_appendix_rows`, `extract_line_ref`, `extract_range`, `extract_stated_count`,
`check_same_file`, `measure_recall`, `scan_corpus`, `resolve_commits`, `print_score`,
`print_corpus`, and at rev-3 `parse_candidates` and the self-test's nested `render_score`. The file name grades in no cell, because `py.file` is undeclared in `.lexicon.conf`.
New gate leg name: `review-replay selftest`.

### Files touched (estimate)

- review_replay.py, new, in the kit directory
- `tools/workflows/README.md` — a section for the tool
- `tools/workflows/kit.toml` — one `[[gate_leg]]`
- `tools/gate-legs.json` — one leg, subject `kit`, chunk `selftests`, no guard, ceiling 300
- `tools/govkit/subject-pins.tsv` — regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `memory/map/features/review-harnesses.md` — the leg claimed, and one prose line naming the tool
- `memory/map/generated/MAP.md` and `memory/map/generated/inventories.json` — re-rendered

### Alternatives rejected

- **Score raw confirmed findings.** Rejected by probe: the raw text never reaches a past record
  (F2).
- **Liveness from a stated ITEM tally.** Only 6 of 135 probed records state one (PINNED,
  2026-10-01, at `5db41963`), and a raw count never equals an item count once a synthesis merges.
- **Match on any ref in an item row.** Item rows quote spec and test sites as context, so a
  candidate at a context site would match the defect. The first ref is the location column in every
  row shape probed.
- **Reuse a scorer from another kit.** See §10.

## 5. Production-readiness checklist

- security — The tool reads files and runs one git subprocess with an argv list, never a shell
  string. Shas reach git only after matching the hex shape. Nothing is written.
- perf / scale — One git process per corpus run, and S6 pins it. A record is read once. The corpus
  is a few hundred files.
- error / empty / loading states — Every refusal is exit 2 with a reason naming the numbers that
  disagreed. An empty corpus directory is a refusal and not an empty listing, because a scan that saw
  nothing must not read as a corpus with nothing replayable.
- observability — The corpus summary line counts every scanned record into exactly one bucket, and
  the score prints every known item as matched, missed or unscorable.
- risks — Legacy records are free prose that a synthesis wrote, so most are refused. The probe
  passed 24 of 78 table-bearing records on liveness and 8 on liveness plus a resolving range (PINNED,
  2026-10-01, at `5db41963`; `--corpus` re-derives it). That is enough for the live replay. A
  refused record is never scored, which keeps a silent partial extraction out of every score.
- testing — `--selftest` (S7), its held leg (S8), and the staged break of AC2.
- migration — N/A — a new file and a new leg. Nothing existing changes shape.
- user docs — The kit README section (S9). This repo keeps no `help/` tree.

## 6. Acceptance criteria

`$KIT` below is the review-harness kit directory, which in this repository is the directory holding `tools/workflows/tier2-review.template.js`; the tool is named through it because it does not exist until this unit builds it.

- **AC1** — When `python3 $KIT/review_replay.py --selftest` runs, it prints `ok` for every
  arm in the §4 table, `score-miss` included, and `selftest: 19/19 arms`, then exits 0.
  Red when: any arm fails, or fewer arms run than are declared.
  figure: 19 is PINNED, the row count of the §4 arm table.
- **AC2** — When a scratch copy of the tool has its known-set liveness comparison deleted, and
  `python3 <copy> --selftest` runs, `known-liveness-refuses` prints `FAIL` and the run exits 1.
  Red when: the copy still exits 0, which means the arm cannot observe the guard it names.
  fixture: the copy lives under the session scratchpad and is never committed.
- **AC3** — When `python3 $KIT/review_replay.py --corpus memory/builds` runs on this tree,
  it lists at least one record at `round 1`, and its summary line's listed and refused counts sum to
  its scanned count. Red when: zero records are listed, or the counts do not sum.
  figure: DERIVED at observation. The scratch probe found 4 round-1 candidates (PINNED, 2026-10-01).
- **AC4** — When `grep -nE "memory/|tools/" $KIT/review_replay.py` runs, it prints
  nothing, because the docstring spells its usage by basename and every population is an argument.
  Red when: any line names a path outside the kit, which an adopter installing the kit at another
  prefix would not hold.
  fixture: the file exists only after the unit is built.
- **AC5** — When `GIT_TRACE=1 python3 $KIT/review_replay.py --corpus memory/builds` runs,
  `git cat-file` appears in the trace exactly once. Red when: it appears once per record.
- **AC6** — When `python tools/govkit/govkit.py selfcheck` and
  `python3 tools/codebase-map/check_gate_coverage.py` run, both pass, and `tools/gate-legs.json`
  holds the review-replay selftest leg with subject `kit`, chunk `selftests` and no `guard` key, and
  `python tools/check-spec-tokens.py` exits 0.
  Red when: the descriptor and the manifest disagree, the subject pin is stale, or no dossier claims
  the leg.
- **AC7** — When `grep -c "review_replay.py" tools/workflows/README.md` runs, it prints at least 4:
  the three modes and the live-replay step. Red when: the README names fewer.
- **AC8** — When the main loop runs the §4 live-replay procedure on one round-1 record listed by
  `--corpus`, `--known <record> --candidate <report>` exits 0 and prints a `replay: recall` line,
  and the main loop writes that line, with the record path and range, to the acceptance ledger.
  Red when: either input is refused, or the run wrote no report.
  permission: the `Workflow` tool, which only the main loop holds.
  cost: one full review fan, five lenses plus the skeptic batches and one synthesis.
  fixture: a candidate report carrying the unit-8 appendix, which exists only once unit 8 is built.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `run-gates canary` · `run-gates gov canary` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `codebase-map gate coverage` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `review-replay selftest`

The new leg is the one this unit adds. The four `tools/workflows/` self-tests, the two canaries,
the three `tools/govkit/` legs and the two recall-floor legs are owed because the §4 file estimate
trips their guards. The close runs all of them once, on the bar. The kit-epoch leg is satisfied by
unit 5's single version move and not by this unit.

New arm: none in a suite. The self-test lives in the tool's own `--selftest` flag, and AC2 stages
its failing case.

## 8. Open questions

- **F1 — Does the tool get a gate leg, or stay on demand?**
  Options: (a) on demand only, with the main loop running `--selftest` at `VERIFYING`; (b) a held
  leg with subject `kit` and chunk `selftests`, mirroring `shell-hygiene selftest` in the gate-lint
  kit; (c) an arm inside the harness's existing shell self-test. Option (c) mixes a Python tool into a
  Node-in-bash suite that resolves no Python today. Option (a) leaves a self-test nothing declares,
  against the charter's declared-population rule. Option (b) costs the meta-gates the
  new-leg gotcha lists, all named in §7. Veto 2 does not fire, because a held kit self-test leg is an
  existing kind in this kit's descriptor and runs on no automatic bar.
  RESOLVED (agent, 2026-10-01, delegated): (b), the held leg. It is the most feature-rich survivor,
  and it reuses the gate-lint seam.
- **FACT-QUESTION · F2 — Is a known finding a raw confirmed finding or an adjudicated item?**
  Probe: read the findings sections of past diff-review records for a per-raw-finding location.
  Observation that decides it: records list ITEMS with a raw-id column, and state that refuted and
  merged raw text did not reach the synthesis. Liveness: a record listing raw findings one per row
  would show a row count equal to its stated confirmed count, and the dMendedRecall round-1 record
  shows 1 row against 2 raw.
  RESOLVED (agent, 2026-10-01, delegated): the adjudicated item, with the raw-id union as the
  liveness check.
- **F3 — What is the default match window?**
  Options: an exact line; 10 lines; the whole file. An exact line misses every finding a synthesis
  re-pinned. A whole-file match credits any finding in a large file. The dMendedRecall round-1
  record merged two raw findings at adjacent lines of one function into one item.
  RESOLVED (agent, 2026-10-01, delegated): 10 lines, PINNED as a judgement and not a measurement,
  and adjustable per run with `--window`.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, authored under the run mandate with no spec audit (owner,
  2026-10-01).
- rev-2 · 2026-10-01 · built. §7 names the new leg `review-replay selftest` now that it exists in
  `tools/gate-legs.json`. §4's file estimate missed one write the new held leg owes: a budget row in
  `tools/run-gates/selftest-budgets.txt`, which grades every held leg, so the build adds it.
- rev-3 · 2026-10-01 · folds the round-1 closing review's replay-side findings
  (`2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md`). M1 (findings 5, 21): S2 and
  §4 said every known set is adjudicated items while rule 1 and the code take one per raw appendix
  row; the documents now state the built behaviour, the header prints the unit, and
  `known-unit-raw` pins it. M2 (finding 4): §4 Matching strips a drive prefix, arms on both sides.
  M4 (finding 17): S4 gains the candidate unscorable count and its refusal. L2 parser side
  (finding 3): rows split on a newline only, `appendix-u2028-row`. L4 (finding 18): S4 names the one
  row-to-candidate function `parse_candidates`. Five arms, AC1 14 to 19. The leg's guard is
  REMOVED (S8, AC6, §4 Files touched): a guard on `tools/workflows/` made the spec-tokens guards
  join demand the leg of four live aRepatriatedFork specs naming that kit, and the self-test costs
  about a second, so it runs unguarded like `template size gate selftest`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "score a review report's findings against a past review
record's confirmed findings"` was run. Its top scoring hit is `score` in `tools/memory-recall/bench.py`
(fan-in 3). It scores RANKED retrieval lists against a query fixture, which is a different shape,
and it lives in another kit, which the kit-literal ban forbids a kit file to import. The
`tools/runlog/` hits parse run records and not review records. So no existing seam fits for the
scorer itself. The seam this unit EXTENDS is the self-test shape in `tools/gate-lint/sh_hygiene.py`,
where `run_selftest` is dispatched by `main` on `--selftest`, together with that kit's held
`[[gate_leg]]` pair in `tools/gate-lint/kit.toml`. M12's candidates for known-set extraction and
the probe that rejected each are in §4, "Alternatives rejected", and in F2.

Recall terms used: `python tools/memory-recall/query.py "has a past review's recall been measured by
replaying the review harness over an old range and scoring against its confirmed findings" --terms
"tier2-review recall replay confirmed findings precision diff-review record round-1 range lens yield
benchmark selftest liveness"`. No record measured recall before. The closest are the
dTieredTribunal backlog rows on counters the synthesis never receives.
