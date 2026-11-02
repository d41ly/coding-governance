# TOOL-dSafePassage-97 — the round-8 closing review's five wording lows: spec 96's text corrected in one table

**Status:** CLOSED · rev-1 · 2026-11-01 · node a · Tier-2 · base ab71837da · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md](../build/2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 TOOL-dSafePassage-84 TOOL-dSafePassage-86 TOOL-dSafePassage-87 TOOL-dSafePassage-88 TOOL-dSafePassage-89 TOOL-dSafePassage-90 TOOL-dSafePassage-91 TOOL-dSafePassage-92 TOOL-dSafePassage-93 TOOL-dSafePassage-94 TOOL-dSafePassage-95 TOOL-dSafePassage-96 TOOL-dSafePassage-98 TOOL-dSafePassage-99 TOOL-dSafePassage-100 TOOL-dSafePassage-101 TOOL-dSafePassage-102 TOOL-dSafePassage-103 TOOL-dSafePassage-104 |
| [2026-11-01-build-TOOL-dSafePassage-97-ledger.md](../build/2026-11-01-build-TOOL-dSafePassage-97-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-97-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-97-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-97-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-97-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-97-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-97-spec-brief.md) | research | — |
| [2026-11-01-review-TOOL-dSafePassage-97-closing-diff-round9.md](../reviews/2026-11-01-review-TOOL-dSafePassage-97-closing-diff-round9.md) | diff-review | TOOL-dSafePassage-96 |

<!-- /gen:spec-records -->

## 1. Goal

The round-8 closing diff review of TOOL-dSafePassage-96 confirmed five low items and found 96's code
correct. All five are wording defects in 96's spec, which went CLOSED before its round-1 spec audit
was folded. 96 is frozen, so this unit carries each correction in one table, the way
TOOL-dSafePassage-95 carried 94's. It writes no product code. Its only build output is its
acceptance ledger.

## 2. Scope (IN)

- **S1** — the corrections table under §4 "Corrections to 96's text": one row per review item, 1 to
  5. Each row names the review ids it closes, quotes 96's text at `ab71837da` by line, and gives the
  corrected reading. Item 4's row takes the skeptic's corrected fix for id 8. Observed by AC1 and AC2.
- **S2** — the `--legs-for` output that item 2's row rests on, pasted under §4 "The leg query".
  Observed by AC4.
- **S3** — the build pass writes its acceptance ledger and nothing else. No file under the tools
  directory moves, and 96's authored text stays as it is at `ab71837da`. Observed by AC3.

## 3. Non-goals (OUT)

- Any hand edit of the authored text of
  `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md`, which is CLOSED. Its
  generated records block is re-rendered when this round's review is filed, and that is not an edit
  by this unit.
- Any edit of 96's acceptance ledger. Item 1's row states the reading that holds for its line 19.
- Product code. Item 3's fix also narrows the comment at `tools/govkit/selftest.py:4494`. This unit
  does not make that edit. Item 3's row states the comment's corrected reading.
- The review's left-shift gates: the shared one, a CLOSED flip refused while a spec audit is
  unfolded, and the five per-item gates. The main loop owns them.
- A twice-run arm for `check_floor_bash`. The review asks for wording, not an arm.

### Edges

- **hands-off** external — the narrowed comment at `tools/govkit/selftest.py:4494`, a product-code
  edit this unit does not make. The main loop decides whether a later unit makes it.
- **hands-off** external — the review's shared left-shift gate on the CLOSED flip, for the main loop.

## 4. Design

Every line of 96's spec cited here holds at `ab71837da`. Its authored text there is byte-identical
to the build commit `cc668aa42`'s, and to the working tree's when this spec was written. Its line
numbers are not: `ab71837da` added one row to its generated records block, so at `cc668aa42` each
cited line after line 1 sits one line earlier, 112 for 113. The review's cites mix the two trees.
`tools` at `ab71837da` is byte-identical to `cc668aa42`'s (`git diff --quiet`). Every `selftest.py`
line cited here holds at the tree it names. These were read on 2026-11-01 on node a.

### Corrections to 96's text

96 is CLOSED and frozen. Each row is the reading that holds at `ab71837da`. The third column quotes
96's text verbatim, one quoted fragment per cited line or range. AC2 checks each fragment against
96's blob at `ab71837da`.

| Item | Ids | 96 at `ab71837da` | Correct reading |
|---|---|---|---|
| 1 | 2, 14 | line 60: 'git archive 744d2551 tools'; line 178: 'git archive HEAD tools'; line 188: 'kind of scratch repository'; line 196: 'kind of scratch repository' | AC2 reads a scratch repository made from the built tools directory. That is `git archive HEAD tools` once the build commit `cc668aa42` is HEAD, or `git archive 744d2551 tools` with the built `tools/govkit/selftest.py` copied over it. AC3 and AC4 inherit it through "the same kind of scratch repository". Before `cc668aa42`, `tools` at HEAD matched `744d2551`, so a run then read the base result: a loud red, not a false green. 96's ledger owes AC2 to AC4 in the same words at its line 19, and this reading holds there too. |
| 2 | 3, 7, 12, 15 | line 212: 'lexicon naming predicates'; line 217: 'the five legs whose guard covers the selftest file'; line 218-219: 'guarded by the file itself. The rest are 95' | `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py` names 17 legs, pasted under "The leg query". Five have a specific guard: the four guarded by `tools/govkit/`, and `policy fixtures`, guarded by the file itself. Twelve trip through the broad `tools/` guard, `lexicon naming predicates` among them. They run on the bar as well and are expected unchanged. The leg line's other three names carry no guard. So line 212's leg line stands, and lines 217-219 leave out the twelve. |
| 3 | 6, 10, 16 | line 1: 'a reused tmp stages afresh'; line 94: 'TOOL-dSafePassage-96: a reused tmp stages afresh'; line 98: 'The bar is unaffected either way.' | S3's rerun safety covers only a direct `check_floor_bash(tmp)` call, which is what AC1 runs. The one caller, `check_step_isolation` (`selftest.py:3684` at `ab71837da`), runs `quiet_target.mkdir(parents=True)` with no `exist_ok` at `:4404`, before its call at `:4427`. So on a reused `tmp` it raises `FileExistsError` before `check_floor_bash` is reached, and its other `build_staged_copy` calls are single-use per `tmp` too. The bar's fresh `TemporaryDirectory` is what keeps them safe. The comment at `selftest.py:4494` at `ab71837da` makes the same claim in code and reads the same way. |
| 4 | 4, 8, 13, 17 | line 113: 'replacement of 95 given back'; line 187: 'When the narrowed copy'; line 214: 'replacement and by the' | The break is TOOL-dSafePassage-95's S4, whose heading is spec 95's line 170. Spec 96 defines only S1 to S3, at its lines 64 and 85. One spelling serves all three lines: "the TOOL-dSafePassage-95 S4 replacement given back `except OSError:`". That replacement is the `src94.replace(anchor94, ...)` line: `selftest.py:4496` at `744d2551`, and `:4497` at `ab71837da`, because S3's `rmtree` line sits above it. Any cite of that line names its tree. This is the skeptic's corrected fix for id 8. |
| 5 | 5, 9, 18 | line 195: 'and its restore line are cut from'; line 214: 'covers AC2 AC3 AC4'; line 215: 'covers AC2 AC4' | Both arms cover AC4, and each staging column names AC4's break. Line 214's reads: staged red by the TOOL-dSafePassage-95 S4 replacement given back `except OSError:` (AC3), by the `steps._BASH = None` cut (AC2) and by the `finally` cut (AC4). Line 215's reads: staged red by the `steps._BASH = None` cut (AC2) and by the `finally` cut (AC4). Both covers lists stand, because 96's Measured row at line 116 shows the `finally` cut turning both `[dSP-95]` checks red over S1 to S3. |

### The leg query

`python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py`, run at `ab71837da` on
2026-11-01 on node a, printed this. `tools/gate-legs.json` is byte-identical there and at
`cc668aa42`. AC4 re-derives the leg lines.

```text
tools/govkit/selftest.py
  python resolver (behaviour + inline parity + idiom ban) <- tools/ [wiring/kit] broad
  push-main self-test <- tools/ [selftests/kit] broad
  check-wiring self-test <- tools/ [selftests/kit] broad
  settings-merge selftest <- tools/ [selftests/kit] broad
  recall floor arms <- tools/govkit/ [selftests/repo]
  run-gates canary <- tools/ [selftests/repo] broad
  run-gates evidence <- tools/ [selftests/kit] broad
  foreign-prefix parity (every self-test at three prefixes) <- tools/ [selftests/repo] broad
  install-prefix self-test <- tools/ [selftests/kit] broad
  dead-path carriers self-test <- tools/ [selftests/kit] broad
  govkit selftest <- tools/govkit/ [selftests/kit]
  lexicon naming predicates <- tools/ [declarations/repo] broad
  govkit refusal join <- tools/govkit/ [declarations/repo]
  govkit acceptance matrix <- tools/govkit/ [declarations/repo]
  policy fixtures <- tools/govkit/selftest.py [selftests/kit]
  spec-tokens self-test <- tools/ [selftests/kit] broad
  kit-placeholders self-test <- tools/ [selftests/kit] broad
legs-for: 76 of 148 legs carry no guard and run whatever changed
```

### Inventory

No local, function, constant, type, file, check label, flag, conf key, gate leg or receipt field is
minted. The naming lexicon grades nothing new.

### Migration

None.

### Rollout

Live at landing, at order 16. The corrections are read from this spec. Nothing executes them.

### Files touched (estimate)

- `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-97-ledger.md`, the
  acceptance ledger and the build's only write.

### Alternatives rejected

- **An erratum record beside 96.** The review allows one. A unit carries the corrections with
  criteria and a ledger, as 95 did for 94, and the build's roster counts it.
- **A row per cited line.** The brief asks for one row per item. Item 4 and item 5 share line 214,
  and one row per item keeps each id on one row.
- **Narrowing the `selftest.py:4494` comment here.** It is product code, which the brief rules out.
  §3 hands it off.

## 5. Production-readiness checklist

- security: N/A — no write path, spawn or surface. The build writes one record under this build's
  folder.
- perf / scale: N/A — no code runs. AC4's query takes a few seconds.
- error / empty / loading states: N/A — no code changes.
- observability: AC2 prints the cited fragments that do not hold, and AC4 prints the leg count.
- risks: 96's spec keeps its uncorrected text, so a reader of 96 alone still meets it. The
  correction lives here, and the records block 96 renders names this round's review.
- testing: AC1 to AC4. No arm is added (§7).
- migration: N/A — no data or state changes.
- user docs: N/A — no page under `help/` describes the selftest's floor checks or 96's spec.

## 6. Acceptance criteria

- **AC1** — When
  `python -c "import re; p = 'memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-'; t = open(p + '97.md', encoding='utf-8').read(); rows = re.findall(r'(?m)^\| (\d) \| ([\d, ]+) \|', t); print(sorted(int(i) for i, _ in rows), sorted(int(x) for _, ids in rows for x in ids.split(',')))"`
  runs from the repository root, it prints `[1, 2, 3, 4, 5]` and then
  `[2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18]`: every item and every confirmed id of
  the round-8 review, each once.
  Red when: an item's row is missing or an id is left off its row. With item 3's row cut from a
  copy of this spec, it prints `[1, 2, 4, 5]` and a list without 6, 10 and 16, measured.
- **AC2** — When
  `python -c "import re, subprocess; p = 'memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-'; s = subprocess.run(['git', 'show', 'ab71837da:' + p + '96.md'], capture_output=True, encoding='utf-8').stdout.splitlines(); t = open(p + '97.md', encoding='utf-8').read(); c = [m for r in re.findall(r'(?m)^\| \d \| [\d, ]+ \| (.*?) \|', t) for m in re.findall(r\"line (\d+)(?:-(\d+))?: '([^']+)'\", r)]; print(len(c), [m for m in c if m[2] not in ' '.join(s[int(m[0]) - 1:int(m[1] or m[0])])])"`
  runs from the repository root, it prints `16 []`: the table quotes 16 fragments, and each is on
  the line or range it cites in 96's blob at `ab71837da`.
  Red when: a row cites a line that does not hold its quoted text. With item 2's `line 217` changed
  to `line 216` in a copy of this spec, the list names that fragment, measured.
  figure: 16 is DERIVED from the table at observation time, and the command counts it.
- **AC3** — When
  `python -c "import re, subprocess; p = 'memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md'; f = lambda t: re.sub(r'(?s)gen:spec-records.*/gen:spec-records', '', t); print(f(subprocess.run(['git', 'show', 'ab71837da:' + p], capture_output=True, encoding='utf-8').stdout) == f(open(p, encoding='utf-8').read()))"`
  runs from the repository root at the build pass's commit, it prints `True`. And
  `git diff --numstat ab71837da -- tools` prints nothing. 96's spec is read with its generated
  records block stripped, because the generator re-renders that block when this round's review is
  filed. The diff reads `tools` alone for the same reason.
  Red when: the build hand-edits 96's authored text or writes a file under the tools directory. The
  same comparison with 96's spec commit `d07da781e` in place of the working tree prints `False`,
  because the Status line differs, measured. The diff with `744d2551` in place of `ab71837da` prints
  one line, `5 2` for the selftest file, measured.
- **AC4** — When
  `python -c "import re, subprocess; p = 'memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-'; t = open(p + '97.md', encoding='utf-8').read(); want = [l for l in re.search(r'(?s)~~~text\n(.*?)~~~'.replace('~', chr(96)), t).group(1).splitlines() if ' <- ' in l]; got = [l for l in subprocess.run(['python', 'tools/check-spec-tokens.py', '--legs-for', 'tools/govkit/selftest.py'], capture_output=True, encoding='utf-8').stdout.splitlines() if ' <- ' in l]; print(want == got, len(got), sum(l.endswith(' broad') for l in got))"`
  runs from the repository root, it prints `True 17 12`: the pasted leg lines match a live query,
  17 legs with 12 broad.
  Red when: the pasted block and the live query differ. With the `policy fixtures` line cut from a
  copy of this spec's block, it prints `False 17 12`, measured.
  figure: 17 and 12 are DERIVED by the live query. A manifest change that moves either also turns
  the first field `False`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

No `New arm:` line. This unit changes no product code and adds or moves no gate arm, so the close
has no arm to observe red and then green. The leg line names `recall floor` and `recall floor arms`
because the ledger path under §4 "Files touched" trips their `memory/` guard. That is all
`python tools/check-spec-tokens.py --legs-for` names for a ledger in this build's folder, measured
over 96's ledger. `memory hygiene` and `spec tokens (a spec's own names resolve)` carry no guard and
grade this spec and its ledger.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-97-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-97-spec-brief.md`.
  It closes the round-8 closing diff review,
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-96-closing-diff-round8.md`:
  items 1, 2, 3 and 5 at the skeptic's sound fix, and item 4 at the corrected fix for id 8. Each
  is carried as one row of §4 "Corrections to 96's text". Every cited line was read at `ab71837da`.

## 10. Reuse audit

The seam is 95's "Corrections to 94's text" sub-head
(`memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:205-216`). It is a table
carrying a CLOSED spec's corrections in the unit that follows it. This unit uses its shape. It adds
an ids column and verbatim fragments that AC2 checks. No code seam is touched: `tools/govkit/`,
`tools/lib/` and `tools/push-main.sh` are not edited.
`python tools/codebase-map/reuse_lookup.py "carry corrections to a closed spec's text in a later unit's corrections table"`
ranked text and spec helpers by name stem, such as `read_text` and `read_spec_revisions`. None of
them carries corrections, so no code seam fits a records-only unit. The recall probe ranked 95's
table, which is the seam above. It also ranked `TOOL-aEvidencedLens-17`, under which a closing
review's lows batch into one unit, which is what this unit is.

Recall terms used: `python tools/memory-recall/query.py "how are corrections to a CLOSED spec's wording carried when its audit was not folded before the flip" --terms "erratum CLOSED frozen corrections table promoted unit spec-audit fold wording low closing review records block"`
