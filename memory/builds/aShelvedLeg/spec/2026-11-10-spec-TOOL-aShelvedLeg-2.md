# TOOL-aShelvedLeg-2 — the closing review's minors on the held kit gate, batched

**Status:** CLOSED · rev-1 · 2026-11-11 · node a · Tier-2 · base 5f066b0a · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aShelvedLeg-1-agent-ledger.md](../build/2026-11-10-build-TOOL-aShelvedLeg-1-agent-ledger.md) | journal | TOOL-aShelvedLeg-1 |
| [2026-11-11-build-TOOL-aShelvedLeg-2-1-acceptance-ledger.md](../build/2026-11-11-build-TOOL-aShelvedLeg-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-10-prompt-TOOL-aShelvedLeg-2-brief.md](../prompts/2026-11-10-prompt-TOOL-aShelvedLeg-2-brief.md) | research | — |
| [2026-11-11-review-TOOL-aShelvedLeg-2-closing-diff-round1.md](../reviews/2026-11-11-review-TOOL-aShelvedLeg-2-closing-diff-round1.md) | diff-review | TOOL-aShelvedLeg-1 |

<!-- /gen:spec-records -->

## 1. Goal

Every MEDIUM and LOW the closing review confirmed on TOOL-aShelvedLeg-1 is fixed in one batch, as
M4 promotes them, and each new class is recorded in `memory/gotchas/`. The findings are round 1
items 2 to 6 and round 2 id 1 (`2026-11-10-review-TOOL-aShelvedLeg-1-closing-diff-round1`,
`-round2`). The owner asked for this unit to be built next (brief, "Owner confirmation").

## 2. Scope (IN)

- **S1** — Every sentence in the unattended kit's scripts that calls `check-unattended.sh` a
  merge-bar leg, or says it runs on the merge bar or on every bar, is reworded (round 1 items 2
  and 3). The sites are the table in §4, "The sentence sites". Each reworded sentence keeps its
  argument and states that the leg is held off every automatic bar by the 2026-11-10 ruling, or
  says "run" where it said "bar run". Observed by AC1, AC2, AC3 and AC4.
- **S2** — The `--checks` comment at `run-unattended-gates.sh:560-561` names the population it
  describes, the `run_one ... checks` rows above it, instead of typing "those four" (round 1
  item 4). Observed by AC2.
- **S3** — The HELD comment above the leg's row in `tools/unattended/kit.toml` and the paragraph
  under "Running the kit's own checks" in `tools/unattended/README.md` each gain one sentence on
  changed mode (round 1 item 5). The sentence says the self-test variable at `changed` selects this
  leg by the kit's shipped sources only, never by the records its `doc_reads` names, so a change
  that moves only records leaves it held. It also says to run it with the variable at `1`, or
  through `--checks`, after such a change. Observed by AC5.
- **S4** — The leg's row in `tools/run-gates/selftest-budgets.txt` has its reading field respelled
  so the `--rank` reader's `worst of (\d+) readings (\d+)s` form matches it (round 1 item 6). The
  name, the budget 4721, the empty argv field and every fact in the reading are unchanged.
  Observed by AC6.
- **S5** — The kit-gate sentence in the no-trailer header of
  `tools/run-gates/selftest-pooled-evidence.txt` is rewritten to say this row's reading is rc only.
  It gives the reason: `check-unattended.sh` prints each failure as `UNATTENDED check <n> FAILED`,
  never as a `^FAIL` line, so the row's FAIL column is always 0. The word "likewise" is not kept,
  because the row does not get its two siblings' rc-plus-FAIL reading (round 2 id 1). The three
  `# no-trailer:` declaration lines are unchanged. Observed by AC7.
- **S6** — Three new `kind: class` records in `memory/gotchas/`, one per class the review named
  new, with `memory/gotchas/INDEX.md` re-rendered by `gotchas.py --write`. The table in §4,
  "The gotcha records", lists them. Observed by AC8.

## 3. Non-goals (OUT)

- Counting `UNATTENDED check <n> FAILED` lines in the fails column of `run-selftests.sh`. The
  fixtures of `check-unattended.test.sh` print that same line, so a new pattern would move the
  fail counts of calibrated rows and break their pooled parity. This is the skeptic's first fix
  for round 2 id 1, and the brief excludes it.
- The runner's own READ line for a declared trailer-less row (`run-selftests.sh:1640`), which
  prints "rc-plus-FAIL only" for this row too. S5 corrects the declaration's header; the runner's
  output wording is behaviour, and no script's behaviour changes here.
- A `--check` arm requiring every budget row to match a `--rank` form. The 21 rows that already
  fail it at base would have to be respelled first.
- Adding a kit-subject leg's `doc_reads` to changed-mode selection in `run-gates.sh`, and a check
  over `tools/gate-legs.json` flagging such legs. S3 states the skip instead.
- A gate over `tools/unattended/` for merge-bar wording. AC1 and AC2 are probes of this change;
  the class is `amendment-leaves-its-other-half-standing`, which already exists.
- Sentences that name a bar only as the setting of another claim. They stay true whenever the leg
  runs on a bar, as it still does with the self-test variable set. These are
  `check-unattended.sh:53` ("READ-ONLY, which is what lets it run on the bar"), `:1495`, `:1540`,
  `:2231`, `:2593` and `:4730`.
- The sentence at `PROTOCOL.template.md:48` saying "the merge bar re-derives" the `authorized-by:`
  mode, which `check-unattended.sh` does. That template renders into the governance carrier
  `memory/guides/UNATTENDED-PROTOCOL.md`, so changing it is a separate document (M2) and an owner
  turn (M3 veto 2). It is handed off below.
- Other hand-typed counts in the kit, such as "These six suites" at `run-unattended-gates.sh:557`.
  S2 fixes the count the review found wrong; S6 records the class.
- Any change to what a script does. The only non-comment line this unit changes is the
  `--attribute` help text in `run-unattended-gates.sh`.
- The kit version bump: the lander's `mint` moves it.

### Edges

- **consumes-from** `TOOL-aShelvedLeg-1` — the HELD comment, the budget row, the no-trailer
  declaration and the reworded `run-unattended-gates.sh` lines this unit corrects. That unit is
  CLOSED and its spec stays frozen; this unit is the correction on top of it.
- **hands-off** external — the review's proposed left-shift gates, which the brief's non-goals
  defer: a fail pattern per no-trailer row, a `--rank`-form arm under `--check`, and a check for
  kit-subject legs that declare `doc_reads`. The main loop files them as asks.
- **hands-off** external — the `PROTOCOL.template.md:48` sentence and its rendered twin, an owner
  turn because it is a governance carrier. The main loop files it as an ask.

## 4. Design

### Evidence

Read at 5f066b0a, the tip after TOOL-aShelvedLeg-1 was built. Its HELD comment, budget row and
no-trailer declaration do not exist at the default branch's sha, so this unit is grounded on the
tip and its header `base` names it.

- **The population is re-derived, not copied from the review.** The brief's goal covers every
  sentence that "says it runs on the merge bar". In this repo the bar is the merge bar, and
  TOOL-aBenchedProbe-1's brief, the precedent for holding a leg, asked for "any that now says the
  leg runs on the bar" to be corrected. So the predicate reads merge-bar wording and "on every
  bar" / "runs on the bar" wording. A grep for that predicate over the two `check-unattended`
  files prints 18 lines at 5f066b0a. Sixteen are sites and two are kept (Non-goals).
- **Wrapped phrases were checked.** A join of each line with the next found no phrase split across
  a line break in `tools/unattended/`.
- **The help line is text, not a comment.** `run-unattended-gates.sh:434` is an `echo` inside the
  `--help` block. Rewording it changes `--help` output and nothing else.
- **No reader pins the reworded text.** A grep of `tools/`, `skills/`, `.githooks/`, `.github/` and
  the root docs for each phrase being reworded finds only the sites themselves. The
  `drift_report.py` hits for "unguarded merge-bar leg" are about another leg.
- **Line endings.** `.gitattributes` gives all four scripts `eol=lf`. A binary read finds four bare
  CR bytes in `check-unattended.sh`, inside awk and tr literals at `:1663`, `:3107`, `:4138` and
  `:4139`, and none in the other files this unit touches. Edit `check-unattended.sh` in binary mode
  (`text-mode-read-eats-a-bare-cr`). Under Git Bash, `grep -c $'\r'` counts every line of an
  LF file, so AC4 reads bytes through Python (`msys-grep-counts-cr-on-every-line`).
- **The `--rank` reader.** `run-selftests.sh:550-555` holds two forms, and only
  `worst of (\d+) readings (\d+)s` fits a gate-run reading. The row's current reading puts
  "retained gate-run" between the count and "readings", so it falls through to unbacked. The only
  refusal pattern is `pooled@` (`:548`), which the respelled row does not carry.
- **The fails column.** `run-selftests.sh:1597` counts `grep -c '^FAIL'`.
  `check-unattended.sh:316` defines `fail()` as `echo "UNATTENDED check $1 FAILED — $2"`, and no
  line of the checker prints `FAIL` at column 0.
- **Changed mode.** `run-gates.sh:3070-3083` states the selection set: the owning kit's shipped
  sources plus the suite file, with a lag bound `GATE_SELFTESTS_MAX_LAG` of 10 by default. A leg's
  `doc_reads` is not an input. The leg's `doc_reads` are `{memory_root}/builds/`, `guides/` and
  `archive/` (`kit.toml:269`).

### The sentence sites

Line numbers at 5f066b0a. The builder re-derives them with AC1's and AC2's greps rather than
trusting this table.

| File | Line | Says now | Reword as |
|---|---|---|---|
| `check-unattended.sh` | 2 | "the merge-bar leg for the unattended-run kit" | the kit's repository gate leg, held off every automatic bar by the 2026-11-10 ruling (TOOL-aShelvedLeg-1) |
| `check-unattended.sh` | 37, 46 | "invisible on every bar run" | "invisible on every run" |
| `check-unattended.sh` | 71-73 | "It runs on the bar, the bar runs under the pre-push hook ... a false positive on the merge bar" | it can run under the pre-push hook when a pusher sets the self-test variable, and a red from another node's git there is a false positive |
| `check-unattended.sh` | 318 | "the merge-bar run's spawn count" | "an unscoped run's spawn count" |
| `check-unattended.sh` | 435 | "this is an unguarded merge-bar leg" | this is an unguarded leg in every adopter's manifest |
| `check-unattended.sh` | 2829 | "is the merge bar's own opinion" | "is this leg's own opinion" |
| `check-unattended.sh` | 3809 | "on an unguarded merge-bar leg" | "on an unguarded leg" |
| `check-unattended.sh` | 6013, 6015 | "TOLD, on every bar" and "runs on every bar of every adopter forever" | told on every run of this leg, in every adopter that runs it |
| `check-unattended.test.sh` | 244 | "the same announcement on every bar" | "on every run of the leg" |
| `check-unattended.test.sh` | 943 | "this leg is on an unguarded merge bar" | "this leg is unguarded" |
| `check-unattended.test.sh` | 2485 | "It runs on the merge bar, where a gate that writes ..." | "It is a gate, and a gate that writes ..." |
| `check-unattended.test.sh` | 3038 | "would red here, on every bar" | "would red here, on every run of this suite" |
| `check-unattended.test.sh` | 3330 | "on an unguarded merge-bar leg" | "on an unguarded leg" |
| `run-unattended-gates.sh` | 46-47, 434 | "those are repository checks and merge-bar legs" | repository checks, run here on demand; the kit gate among them is held off every automatic bar |
| `run-unattended-gates.sh` | 560-561 | "those four are REPOSITORY checks" | the `run_one ... checks` rows above are REPOSITORY checks (S2) |
| `unattended.sh` | 4844-4845 | "check 30 of the sibling checker - an UNGUARDED merge-bar leg - walks" | check 30 of the sibling checker walked, as a bar leg then and held since TOOL-aShelvedLeg-1 |

The "Reword as" column is guidance, not required text. The rules are: the sentence stays true,
it keeps its argument, and it spells none of the words AC1's and AC2's greps read. The
`unattended.sh` sentence is a dated measurement from 2026-08-26, so it moves to the past tense.

### The budget row

The reading field, with every fact kept and the count and seconds moved into the ranked form:

```
unattended kit gate	4721		worst of 5 readings 3147s on node a 2026-11-10 (retained gate-run windows), beside six foreign gate processes, x1.5. TOOL-aShelvedLeg-1 held it by owner ruling
```

Fields are tab-separated and the third is empty. Keep the empty field between the two tabs
(`empty-field-collapses-unless-it-is-last`).

### The evidence header

Rewrite only the kit-gate sentence at `selftest-pooled-evidence.txt:21-22`. It must state, with
"rc only" on one line, that the row is read on rc only, because its failures print as
`UNATTENDED check <n> FAILED` and never as `^FAIL`. The consequence follows: two different red runs
read alike. No new line of the header may begin `# no-trailer:` or `# pooled-kit:`, because
`run-selftests.sh --check` parses those prefixes.

### The gotcha records

Each record has front matter at column 0 (`name`, `description`, `kind: class`) and the sections
`## Symptom`, `## Where it bit`, `## The fix` and `## Gate`. Its anchors are the backticked
`tools/` paths in its body, and at least one must be a tracked path outside `memory/`, or check 19
reads it as inert. Its `## Gate` section opens with "There is no machine gate for this", which
`gotchas.py`'s `DECLARES_RE` reads for check 18, and says why.

| Name | Class | Anchors | Where it bit |
|---|---|---|---|
| `hand-typed-count-of-an-enumerated-population` | prose types the size of a population that code beside it enumerates, and the count goes wrong when a row is added or a sentence is rewritten around it | `tools/unattended/run-unattended-gates.sh` | round 1 item 4: "those four" over five `run_one` rows |
| `changed-mode-selection-ignores-doc-reads` | a kit-subject leg that declares `doc_reads` is selected under changed mode by its kit's shipped sources alone, so a change that moves only the records it reads leaves it held | `tools/run-gates/run-gates.sh`, `tools/gate-legs.json` | round 1 item 5: the unattended kit gate |
| `fail-count-reads-a-pattern-the-row-never-prints` | a fails column counts one line shape, and a row whose script prints its failures in another shape always reads 0, so two different reds compare equal | `tools/run-gates/run-selftests.sh`, `tools/run-gates/selftest-pooled-evidence.txt` | round 2 id 1: the kit gate row declared no-trailer |

Check 27 at `NEAR_MATCH_GATE="red:0.125"` requires a new record to name its nearest older record
when one reaches the floor. After committing the records, run
`python tools/memory-tree/row_grammar.py --check-relations`. Name any hit it prints in the record's
body, in a `## Related` line, before the pass ends.

### Inventory

Minted: the three gotcha names in the table above. No lexicon cell in this repo grades a gotcha
name; hygiene checks 17 to 19, 27 and 28 grade the records. No other identifier is minted.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/run-unattended-gates.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/kit.toml`
- `tools/unattended/README.md`
- `tools/run-gates/selftest-budgets.txt`
- `tools/run-gates/selftest-pooled-evidence.txt`
- `memory/gotchas/`
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- **Only the lines the review cited.** That leaves `check-unattended.sh:37`, `:46`, `:71`, `:318`,
  `:2829`, `:6013` and `:6015`, the test file's `:244`, `:943` and `:3038`, and `unattended.sh:4844`
  saying the same false thing. The review's own skeptic graded the instance-only fixes
  INSTANCE-ONLY for that reason.
- **Count the checker's failure lines in the fails column.** Excluded by the brief, for the pooled
  parity reason in Non-goals.
- **Add `doc_reads` to changed-mode selection.** Excluded by the brief. It changes the runner's
  selection for every kit-subject leg, which is a behaviour change on a shared contract.

## 5. Production-readiness checklist

- security — N/A: comments, one help string, one data field's text and records; no input, write
  path or surface.
- perf / scale — N/A: no code path changes.
- error / empty / loading states — N/A: no code path changes.
- observability — `run-selftests.sh --rank` ranks the leg's row instead of listing it as unbacked.
  `--help` of `run-unattended-gates.sh` stops calling the `--checks` half merge-bar legs.
- risks — the binary-mode edit of `check-unattended.sh` could fold its four bare CR bytes and change
  four awk and tr literals. AC4 observes that. A comment edit in a `.sh` file could disturb a
  heredoc or a quoted literal; AC3 observes that only comment lines and the help text moved.
- testing — AC1 to AC8, all probes of the changed files. The close's bar re-observes S4 and S5
  through the budget leg, and S6 through `memory hygiene`.
- migration — N/A: an adopter takes the reworded kit files at its next `govkit update`.
- user docs — the kit README's "Running the kit's own checks" gains S3's sentence. No page under
  `help/` names this leg or changed mode.

## 6. Acceptance criteria

- **AC1** — When
  `grep -nE 'merge[- ]bar|every bar\b|runs? on the bar\b' tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh`
  runs, it prints exactly two lines, both in `tools/unattended/check-unattended.sh`: the
  "READ-ONLY, which is what lets it run on the bar" line and the "`GATE_BOUND` is an hour" line.
  Red when: any site in §4's table for those two files keeps its wording, or a rewording spells
  "merge bar" or "every bar". At 5f066b0a it prints 18 lines.
  figure: 18 is PINNED at 5f066b0a.
- **AC2** — When
  `grep -nE 'checks and merge-bar legs|those (four|five)|UNGUARDED merge-bar' tools/unattended/run-unattended-gates.sh tools/unattended/unattended.sh`
  runs, it prints nothing.
  Red when: the header comment, the help line, the `--checks` count or the `unattended.sh:4844`
  sentence keeps its wording. At 5f066b0a it prints four lines: 47, 434 and 560, and
  `unattended.sh:4844`.
- **AC3** — When the probe below lists every changed line of the four edited scripts under
  `tools/unattended/` that is not a comment, it prints only the reworded `echo` line or lines of
  the `--attribute` help text:
  ```
  git diff -U0 5f066b0a -- tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh tools/unattended/run-unattended-gates.sh tools/unattended/unattended.sh | grep -E '^[-+][^-+]' | grep -vE '^[-+][[:space:]]*#'
  ```
  Red when: any code line, heredoc or quoted literal in those files moved.
- **AC4** — When the probe below reads `tools/unattended/check-unattended.sh` as bytes, it prints
  `4 0`, the bare CR count and the CRLF count:
  ```
  python -c "b=open('tools/unattended/check-unattended.sh','rb').read();print(b.count(b'\r'),b.count(b'\r\n'))"
  ```
  Red when: the edit went through a text-mode read and folded or doubled a CR. At 5f066b0a it
  prints `4 0`.
- **AC5** — When the two range probes below read the HELD comment in
  `tools/unattended/kit.toml` and the "Running the kit's own checks" section of
  `tools/unattended/README.md`, each prints a count of at least 1:
  ```
  awk '/HELD BY OWNER RULING, 2026-11-10/,/^name = "unattended kit gate"/' tools/unattended/kit.toml | grep -c 'GATE_SELFTESTS=changed'
  awk '/^## Running the kit/,/^## [^R]/' tools/unattended/README.md | grep -c 'GATE_SELFTESTS=changed'
  ```
  Red when: either file lacks S3's sentence, or it sits outside the leg's comment or that
  section. At 5f066b0a both print 0.
- **AC6** — When the probe below reads the leg's row of `tools/run-gates/selftest-budgets.txt`, it
  prints `4721 '' ('5', '3147')`: the budget, the empty argv field, and the count and seconds the
  `--rank` form captures:
  ```
  python -c "import re;r=[l.rstrip('\n').split('\t') for l in open('tools/run-gates/selftest-budgets.txt',encoding='utf-8') if l.startswith('unattended kit gate\t')][0];print(r[1],repr(r[2]),re.search(r'worst of (\d+) readings (\d+)s',r[3]).groups())"
  ```
  Red when: the reading keeps its old spelling, which raises `AttributeError` as it does at
  5f066b0a, or the budget or the empty argv field moved.
  permission: the main loop observes `--rank` of the runner no longer listing the row as unbacked;
  a role agent may not run it.
- **AC7** — When `awk` reads `tools/run-gates/selftest-pooled-evidence.txt` from the
  "ROWS WHOSE SUITES PRINT NO TRAILER" line to `# no-trailer: unattended kit gate`, the range
  carries "rc only" and `UNATTENDED check` and does not carry "likewise". The first command below
  prints a count beside `rc only` and beside `UNATTENDED check` and no `likewise` line, and
  `grep -c '^# no-trailer:'` over the file prints 3:
  ```
  awk '/ROWS WHOSE SUITES PRINT NO TRAILER/,/^# no-trailer: unattended kit gate/' tools/run-gates/selftest-pooled-evidence.txt | grep -oE 'rc only|UNATTENDED check|likewise' | sort | uniq -c
  grep -c '^# no-trailer:' tools/run-gates/selftest-pooled-evidence.txt
  ```
  Red when: the header still says "likewise", or it names neither the rc-only reading nor the
  checker's failure line. At 5f066b0a the range carries "likewise" and neither phrase.
  permission: the main loop observes the budget leg `every held leg is budgeted, every budget row resolves`
  staying clean; a role agent may not run the runner it calls.
- **AC8** — When `python tools/memory-tree/gotchas.py --check` runs after S6's records and the
  re-rendered `memory/gotchas/INDEX.md` are committed, it exits 0. The index lists each of the
  three names on one row, and each record's body satisfies `--declares`:
  ```
  grep -cE 'hand-typed-count-of-an-enumerated-population|changed-mode-selection-ignores-doc-reads|fail-count-reads-a-pattern-the-row-never-prints' memory/gotchas/INDEX.md
  for n in hand-typed-count-of-an-enumerated-population changed-mode-selection-ignores-doc-reads fail-count-reads-a-pattern-the-row-never-prints; do python tools/memory-tree/gotchas.py --declares < memory/gotchas/$n.md; done
  ```
  The grep prints 3 and each `--declares` prints `declares: yes`.
  Red when: a record is missing, its `## Gate` section says nothing `DECLARES_RE` reads, it derives
  no anchor, or the index was not re-rendered (check 17 names it stale).
  cost: about two minutes for `--check` on node a, measured 2026-11-10.
  permission: checks 27 and 28 are graded at the close by the `memory hygiene` leg; the pass's
  probe for them is the `row_grammar.py --check-relations` run §4 names.

## 7. Gates

`every held leg is budgeted, every budget row resolves` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `docs` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `routed commits name a specced unit` · `brief-recorded` · `recall floor` · `recall floor arms` · `policy fixtures` · `tier2-review self-test`

The budget leg re-observes S4 and S5 at the close, and `memory hygiene` re-observes S6, its checks
27 and 28 included. `recall floor` and `recall floor arms` are owed because `memory/gotchas/` sits
under their `memory/` guard. `policy fixtures` guards `tools/unattended/kit.toml`, and
`tier2-review self-test` guards `tools/unattended/unattended.sh`. Those three are held on a default
bar, and the close runs them only if it asks for the held tier. The kit epoch and version legs
expect the lander's `mint`.

No new arm: the unit adds and moves no suite arm. Each criterion is a probe of the changed files.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft.

## 10. Reuse audit

The seams are wording and row shapes that already exist, since this unit changes prose and one data
field. Item 1 reuses the held-leg wording TOOL-aShelvedLeg-1 wrote at
`run-unattended-gates.sh:8-9` and in the kit.toml HELD comment. Item 4 reuses the ranked row shape
of `tools/run-gates/selftest-budgets.txt`, for example `agent-cap self-test`'s
`worst of 7 readings 389s, x1.5`. Item 6 reuses the gotchas catalogue and its renderer,
`gotchas.py --write`. `python tools/codebase-map/reuse_lookup.py "comment says a leg runs on the
merge bar after it was held"` returned only name-stem neighbours (`run`, `legs`, `merge`, `leg`),
and none of them governs comment wording. For prose, no existing seam fits beyond the wording
cited above.

Recall returned TOOL-aBenchedProbe-1's spec brief, which asked for "any that now says the leg runs
on the bar" to be corrected when that build held three legs. That is why S1's predicate reads
"every bar" as well as merge-bar wording. Recall also returned the dDerivedDocket spec-audit
finding that a held leg owes a budget row, which TOOL-aShelvedLeg-1 already met. `gotchas.py
--for-paths` over the estimate selected `text-mode-read-eats-a-bare-cr`, which gives AC4;
`empty-field-collapses-unless-it-is-last`, which gives AC6's argv-field check; and
`amendment-leaves-its-other-half-standing`, which is S1's class.

Recall terms used: `python tools/memory-recall/query.py "how is a stale comment claiming a held leg
runs on the merge bar found and corrected, and how is a budget row reading spelled for rank"
--terms "merge-bar leg held kit gate stale comment selftest-budgets rank reading no-trailer FAIL
count changed"`
