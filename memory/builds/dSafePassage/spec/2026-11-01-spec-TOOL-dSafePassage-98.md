# TOOL-dSafePassage-98 — the round-9 closing review's one low: 97's S3 narrowed to what its AC3 reads

**Status:** CLOSED · rev-1 · 2026-11-01 · node a · Tier-2 · base e3038fea6 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md](../build/2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 TOOL-dSafePassage-84 TOOL-dSafePassage-86 TOOL-dSafePassage-87 TOOL-dSafePassage-88 TOOL-dSafePassage-89 TOOL-dSafePassage-90 TOOL-dSafePassage-91 TOOL-dSafePassage-92 TOOL-dSafePassage-93 TOOL-dSafePassage-94 TOOL-dSafePassage-95 TOOL-dSafePassage-96 TOOL-dSafePassage-97 TOOL-dSafePassage-99 TOOL-dSafePassage-100 TOOL-dSafePassage-101 TOOL-dSafePassage-102 TOOL-dSafePassage-103 TOOL-dSafePassage-104 |
| [2026-11-01-build-TOOL-dSafePassage-98-ledger.md](../build/2026-11-01-build-TOOL-dSafePassage-98-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-98-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-98-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-98-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-98-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-98-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-98-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-9 closing diff review of TOOL-dSafePassage-97 confirmed one low, id 4. 97's S3 says its
build pass writes its acceptance ledger "and nothing else", but its build commit `e3038fea6` writes
four paths, and its AC3 reads only 96's authored text and the tools directory. 97 is CLOSED, so
this unit carries the narrowed reading in one corrections row, with the skeptic's write-set probe.
It writes no product code. Its build output is its acceptance ledger.

## 2. Scope (IN)

- **S1** — the corrections table under §4 "Correction to 97's text": one row, item 1, closing id 4.
  It quotes 97's text at `e3038fea6` by line and gives the narrowed reading of 97's S3. The reading
  is the skeptic's corrected fix, not the finder's. Observed by AC1.
- **S2** — the skeptic's write-set probe, `git diff --name-only e3038fea6^ e3038fea6`, its output
  pasted under §4 "The write-set probe". It is the observation that shows an unintended write by
  97's build pass. Observed by AC2. The 96 ledger half of the skeptic's fix, the ledger unchanged
  from `ab71837da` to `e3038fea6`, is observed by AC3.
- **S3** — this unit's own build pass hand-edits neither 96's nor 97's authored text, and moves no
  file under the tools directory. It claims no write set: its build output is its acceptance
  ledger, and its build commit also carries 98's status flip and the generated renders, as
  `e3038fea6` did for 97. Observed by AC4.

## 3. Non-goals (OUT)

- Any hand edit of the authored text of
  `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-97.md`, which is CLOSED. Its
  generated records block is re-rendered when the round-9 review is filed, and that is not an edit
  by this unit.
- Any edit of 96's spec or 96's ledger.
- Product code of any kind.
- The review's left-shift gate: the bug-class checklist entry for a scope line that claims a write
  set, and the `check-spec-tokens` warning on an S-line saying "nothing else". The main loop owns
  them.
- A second correction. The review confirms one item, and its four refuted ids need no row.

### Edges

- **hands-off** external — the review's left-shift gate on write-set scope lines, for the main loop.

## 4. Design

Every line of 97's spec cited here holds at `e3038fea6`, which is HEAD when this spec was written.
The round-9 review serves 97, so filing it re-renders 97's records block and moves every later line
of 97 down one. So the cites name `e3038fea6`, and AC1 reads 97's blob there, not the working
tree. Every command result below was measured on 2026-11-01 on node a.

### Correction to 97's text

97 is CLOSED and frozen. The row is the reading that holds at `e3038fea6`. The third column quotes
97's text verbatim, one fragment per cited line. AC1 checks each fragment against 97's blob there.

| Item | Ids | 97 at `e3038fea6` | Correct reading |
|---|---|---|---|
| 1 | 4 | line 33: 'the build pass writes its acceptance ledger and nothing else'; line 34: 'Observed by AC3.'; line 168: 'or writes a file under the tools directory' | S3 claims only what AC3 reads. 96's authored text, with its generated records block stripped, is unchanged from `ab71837da`, and no file under the tools directory moves. S3 claims no write set. The build commit `e3038fea6` writes the four paths under "The write-set probe": 97's ledger, 97's spec for its status flip and one records row, the generated regions of the build README, and the run's brief and dispatch rows in RUN.md. None is 96's spec, 96's ledger or a path under the tools directory. 96's ledger, which 97's §3 rules out at its line 42, is unchanged: `git diff --quiet ab71837da e3038fea6` over that ledger exits 0. AC3 owns that observation, and AC2 owns the write set. |

### The write-set probe

`git diff --name-only e3038fea6^ e3038fea6`, run on 2026-11-01 on node a, printed this. It lists
97's build commit against its own parent, `83931ecb5`. AC2 re-derives it.

```text
memory/builds/dSafePassage/README.md
memory/builds/dSafePassage/RUN.md
memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-97-ledger.md
memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-97.md
```

The README change in `e3038fea6` is inside its generated regions only. The RUN.md change is two
rows the run's dispatcher appends, a brief row and a dispatch row.

### Inventory

No local, function, constant, type, file, check label, flag, conf key, gate leg or receipt field is
minted. The naming lexicon grades nothing new.

### Migration

None.

### Rollout

Live at landing, at order 16. The correction is read from this spec. Nothing executes it.

### Files touched (estimate)

- `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-98-ledger.md`, the
  acceptance ledger and the build's output.

### Alternatives rejected

- **The finder's fix.** The skeptic judged it UNSOUND. The review's line 50 gives the corrected
  fix, which runs the write-set probe against the build commit's own parent, and S2 carries that.
- **An erratum record beside 97.** A unit carries the correction with criteria and a ledger, as 97
  did for 96, and the build's roster counts it.
- **Restating 98's own write set as a closed list.** The build commit's renders are the generator's
  and the dispatcher's, not this unit's design. S3 claims only what AC4 reads, which is the class
  of defect id 4 names.

## 5. Production-readiness checklist

- security: N/A — no write path, spawn or surface. The build writes one record under this build's
  folder.
- perf / scale: N/A — no code runs. Each command takes under a second.
- error / empty / loading states: N/A — no code changes.
- observability: AC1 prints the cited fragments that do not hold, and AC2 prints any path under the
  tools directory or of 96 in the write set.
- risks: 97's spec keeps its overclaimed S3, so a reader of 97 alone still meets it. The
  correction lives here, and 97's records block names the round-9 review once it is filed.
- testing: AC1 to AC4. No arm is added (§7).
- migration: N/A — no data or state changes.
- user docs: N/A — no page under `help/` describes 97's spec or a unit's write set.

## 6. Acceptance criteria

- **AC1** — When
  `python -c "import re, subprocess; p = 'memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-'; s = subprocess.run(['git', 'show', 'e3038fea6:' + p + '97.md'], capture_output=True, encoding='utf-8').stdout.splitlines(); t = open(p + '98.md', encoding='utf-8').read(); rows = re.findall(r'(?m)^\| (\d) \| ([\d, ]+) \| (.*?) \|', t); c = [m for r in rows for m in re.findall(r\"line (\d+): '([^']+)'\", r[2])]; print([(i, ids) for i, ids, _ in rows], len(c), [m for m in c if m[1] not in s[int(m[0]) - 1]])"`
  runs from the repository root, it prints `[('1', '4')] 3 []`: one row, carrying id 4, whose three
  quoted fragments each sit on the line they cite in 97's blob at `e3038fea6`.
  Red when: the row is missing or cites a line that does not hold its quoted text. With the row's
  `line 34` changed to `line 35` in a copy of this spec, the list names that fragment, measured.
  figure: 3 is DERIVED from the row at observation time, and the command counts it.
- **AC2** — When
  `python -c "import re, subprocess; t = open('memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-' + '98.md', encoding='utf-8').read(); want = re.search(r'(?s)~~~text\n(.*?)~~~'.replace('~', chr(96)), t).group(1).splitlines(); got = subprocess.run(['git', 'diff', '--name-only', 'e3038fea6^', 'e3038fea6'], capture_output=True, encoding='utf-8').stdout.splitlines(); print(want == got, len(got), [l for l in got if l.startswith('tools') or 'dSafePassage-96' in l])"`
  runs from the repository root, it prints `True 4 []`: the pasted write set matches the live
  probe, four paths, none under the tools directory and none of 96's.
  Red when: the pasted block and the live probe differ, or the build commit wrote a path under the
  tools directory. With 96's build commit `cc668aa42` in place of `e3038fea6` in the command, it
  prints `False 5` and a third field naming the govkit selftest file, 96's spec and 96's ledger,
  measured.
  figure: 4 is DERIVED by the live probe. The commit is immutable, so the figure cannot move.
- **AC3** — When
  `git diff --quiet ab71837da e3038fea6 -- memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-96-ledger.md`
  runs from the repository root, it exits 0: 97's build left 96's ledger as it was at `ab71837da`.
  Red when: a commit in that range edits 96's ledger. With `744d2551` in place of `ab71837da`, the
  same command exits 1, because 96's build commit `cc668aa42` wrote that ledger, measured.
- **AC4** — When
  `python -c "import re, subprocess; p = 'memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-'; f = lambda t: re.sub(r'(?s)gen:spec-records.*/gen:spec-records', '', t); print([f(subprocess.run(['git', 'show', 'e3038fea6:' + p + n], capture_output=True, encoding='utf-8').stdout) == f(open(p + n, encoding='utf-8').read()) for n in ('96.md', '97.md')])"`
  runs from the repository root at the build pass's commit, it prints `[True, True]`. And
  `git diff --numstat e3038fea6 -- tools` prints nothing. Each spec is read with its generated
  records block stripped, because filing the round-9 review re-renders both blocks.
  Red when: the build hand-edits 96's or 97's authored text, or writes a file under the tools
  directory. The same comparison with 97's spec commit `2ec06177f` in place of `e3038fea6` prints
  `[True, False]`, because 97's Status line differs, measured. The diff with `744d2551` in place of
  `e3038fea6` prints one line for the selftest file, measured.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

No `New arm:` line. This unit changes no product code and adds or moves no gate arm, so the close
has no arm to observe red and then green. The leg line names `recall floor` and `recall floor arms`
because the ledger path under §4 "Files touched" trips their `memory/` guard in
`tools/gate-legs.json`, read on 2026-11-01. `memory hygiene` and
`spec tokens (a spec's own names resolve)` carry no guard and grade this spec and its ledger.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-98-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-98-spec-brief.md`.
  It closes the round-9 closing diff review,
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-97-closing-diff-round9.md`:
  its one item, id 4, at the skeptic's corrected fix, carried as the one row of §4 "Correction to
  97's text". Every cited line was read at `e3038fea6`.

## 10. Reuse audit

The seam is 97's "Corrections to 96's text" sub-head
(`memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-97.md:64-76` at `e3038fea6`).
It is a table carrying a CLOSED spec's corrections in the unit that follows it, with verbatim
fragments a criterion checks against the CLOSED blob. This unit uses its shape for one row. No code
seam is touched: `tools/govkit/`, `tools/lib/` and `tools/push-main.sh` are not edited.
`python tools/codebase-map/reuse_lookup.py "narrow a closed spec's scope line that claims a write set, observed by the build commit's name-only diff"`
ranked write and build helpers by name stem, such as `write_text` and `build_commit`. None of them
carries corrections, so no code seam fits a records-only unit. The recall probe ranked the round-9
review's own fix, which this unit carries, and `TOOL-aEvidencedLens-20`, whose S3 derives a closing
write set rather than typing one.

Recall terms used: `python tools/memory-recall/query.py "how is a CLOSED spec's overclaimed write-set scope line narrowed in a later unit" --terms "write set nothing else name-only diff build commit parent CLOSED frozen corrections table overclaim scope line"`
