# TOOL-aClearedLedger-13 — the spec lint reads a half-glued redirection and a quoted value as the hook does, and each new branch and reworded clause has an arm that can fail

**Status:** SPECCED · rev-1 · 2026-11-14 · node a · Tier-2 · base 8db6f4be · streams tooling · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-prompt-TOOL-aClearedLedger-13-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-13-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aClearedLedger-13-brief.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-13-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Round 2 of the closing diff review confirmed that `check_bar` under-reads the gate guard on two
spellings, that two new branches and one reworded clause have no arm that can fail, and that three
texts miscount the lint's over-reads. This unit cures the two under-reads, arms each branch and the
clause, and makes the texts list what the code does. It is the batch the build method's M4
promotes from the review's items M1 to M4, L1 and L2.

## 2. Scope (IN)

The review is
`memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-11-diff-review-round2.md`.
Each item below names the review item it closes.

- **S1** — Item M1. In `check_bar` of `tools/check-spec-tokens.py` everything from a word's first
  `<` or `>` on is a redirection, and a redirection whose operator ends the word takes the next
  word as its target (section 4, "The redirection rule"). Observed by AC1.
- **S2** — Item M2. `check_bar` reads each simple command twice, once by whitespace and once
  keeping a quoted run whole, and a leg spelled by either read is a hit (section 4, "The two
  reads"). Observed by AC1.
- **S3** — Item M3. `tools/unattended/gate-guard.test.sh` gains one deny arm that feeds the planted
  leg behind `python3 -m pdb`. Observed by AC2 for the payload and AC3 for the arm.
- **S4** — Item M4. The wrapper spellings assertion of `tools/check-spec-tokens.test.sh` gains two
  spellings only the `&` lookarounds of `SIMPLE_COMMAND_SPLIT` admit, and the comment above that
  pattern states the two places the split differs from the hook's. Observed by AC1 and AC5 for the
  spellings and by AC6 for the comment.
- **S5** — Item L1. The header comment of `tools/unattended/gate-guard.js`, the paragraph of
  `tools/unattended/README.md` headed "The act is refused at the tool call" and the docstring of
  `check_bar` each list the spellings the lint reads and the hook does not, with no count word.
  The hook's own gap list gains the redirection that carries an `&` ahead of the direct-check
  word. Observed by AC2 for the listed differences and AC6 for the texts.
- **S6** — Items M4 and L1. `tools/unattended/gate-guard.test.sh` gains two allow arms that pin
  the two differences S5 newly lists, so a text that says the hook misses a spelling has an arm
  that fails when the hook reads it. Observed by AC2 and AC3.
- **S7** — Items M1, M2 and L1. The wrapper spellings assertion of `tools/check-spec-tokens.test.sh`
  gains the entries of section 4, "The lint's suite". Observed by AC5.
- **S8** — Item L2. `tools/check-template-size.test.sh` gains two arms beside arm A25 that stage a
  reader refusal on a run that reaches check 8, through a second parameter of `build_cap_repo`.
  Observed by AC7.
- **S9** — `FLOOR_ASSERTIONS` of `tools/unattended/gate-guard.test.sh` rises by the count of arms
  S3 and S6 add, from the value TOOL-aClearedLedger-12 leaves. Observed by AC4.
- **S10** — A commit of this unit that moves a file on the `watch:` line of
  `memory/guides/SESSION-KICKOFF.md` re-stamps `last-audit` by the stamp rule of
  `skills/session-kickoff/SKILL.md`. No file of section 4's estimate is on that line. Observed by
  AC8.

## 3. Non-goals (OUT)

- Item H1 of the review. It is TOOL-aClearedLedger-12.
- Any edit to the code of `tools/unattended/gate-guard.js`. This unit moves its header comment
  alone. The redirection ahead of the flag stays a gap the texts name (section 4, "Alternatives
  rejected").
- Any edit to `tools/check-template-size.sh`. Its clause is right; only its arm was absent.
- One fixture file of spellings read by both suites, the left-shift line under items M1, M2, M4
  and L1. Ask TOOL-aDeferredBar-20 owns that mechanism. Each suite here stages its own rows.
- Any edit to the pattern `BAR`, to `SIMPLE_COMMAND_SPLIT`, to `DIRECT_CHECK_BOUND`, to
  `DIRECT_CHECK_WORDS` or to `derive_flag_suites`.
- Any edit to `tools/gate-legs.json`.
- Any edit to a CLOSED spec, or to the spec of TOOL-aClearedLedger-12. Each correction to
  TOOL-aClearedLedger-11 is stated here.
- A lowered floor, a waived arm, and any kit version, which the lander's `mint` moves.

### Edges

- **consumes-from** external — the guard in `readTokenAt` and the appended-spelling arms that
  TOOL-aClearedLedger-12 builds, whose spec is authored beside this one. Without the guard row T3
  of section 4 reads as a miss in the hook, and the floor S9 moves is that unit's.
- **consumes-from** external — the planted-manifest arm block, the wrapper spellings assertion and
  the cap-repository fixture that TOOL-aClearedLedger-11 and earlier units built.
- **hands-off** external — ask TOOL-aDeferredBar-20, the one spelling list both suites would read.
  Until it is built, the equality of the two suites' staged rows is held by section 4's table.

## 4. Design

### Evidence

Read at `a54346ee`, the branch tip. The blobs are `tools/check-spec-tokens.py@4a71f25e`,
`tools/unattended/gate-guard.js@e3e8092e`, `tools/check-spec-tokens.test.sh@3a1456b4`,
`tools/unattended/gate-guard.test.sh@61442a16` and `tools/check-template-size.test.sh@7f7d31f6`.

- **The lint cuts a word and keeps its target.** `check-spec-tokens.py#check_bar` appends the word
  cut at its first `<` or `>` and sets `drop_next` only for a word `REDIRECTION` matches at its
  start. A bare `>&` matches `REDIRECTION` short of its end, so its target stays too.
- **The lint splits before it unquotes.** `check_bar` splits a simple command on whitespace and
  then takes the quote characters out of each word.
- **The hook keeps a quoted run one word.** `gate-guard.js#readTokenAt` holds a quote state.
- **The quoted read alone loses a hit.** The review's corrected fix for item M2 replaces the
  whitespace split. A scratch copy holding only that read answers no hit for
  `bash -c "python t/over.py --selftest"`, which the hook denies through row D5 and which the
  wrapper spellings assertion expects as a hit (PINNED, 2026-11-14, at `a54346ee`). The quoted
  body is then one word.
- **The hook cuts a command at every `&`.** `gate-guard.js#scanSegments` splits on each `&` of the
  view, and `readTokenAt` ends a word at one. A scratch copy whose `scanSegments` alone kept an `&`
  beside a `>` read every row of "The spelling table" as before (PINNED, 2026-11-14): the token
  loop stops at the `&` the word reader will not pass.
- **The lint splits inside `${ }`.** `SIMPLE_COMMAND_SPLIT` holds `{` and `}` with no brace state.
  `scanSegments` and `readTokenAt` both hold one.
- **No arm feeds a head-less segment.** No `run_planted` line of the hook's suite carries ` -m `.
- **No arm prints check 8's clause.** The check 8 arms of the template size suite build their
  repository with `build_cap_repo`, whose policy file the reader accepts. That suite pins no
  assertion count: it ends on its own fail counter.
- **The reader answers a refused file with a row and a refusal.** In a scratch repository of the
  shape `build_cap_repo` builds, with `enforce = "bogus"` in the policy file,
  `budgets.py resolve AGENTS.md=default:49152` exits 0 and prints the row
  `AGENTS.md`, `49152`, `refuse`, `constant` and then one line opening `policy: refused`
  (PINNED, 2026-11-14, at `a54346ee`).
- **Both readers were probed on staged legs.** Probes H and C of TOOL-aClearedLedger-11's
  section 4 were fed the rows of "The spelling table", with nothing run. At `a54346ee` probe C
  prints `rows wrong: 9` (PINNED, 2026-11-14) and probe H prints `rows wrong: 1` (PINNED,
  2026-11-14), row T3, which is item H1.
- **The rule below was prototyped.** A scratch copy of the lint holding "The redirection rule" and
  "The two reads", beside a scratch copy of the hook holding TOOL-aClearedLedger-12's guard, read
  every row of this spec's table and of TOOL-aClearedLedger-11's table as its expected column says
  (PINNED, 2026-11-14). The copies are outside the repository and are not the build.

### The redirection rule

`check_bar` reads each word, with its quote characters out, against one pattern that matches the
whole word:

```python
REDIRECTION = re.compile(r"(.*?)&?[<>]+&?(.*)", re.S)   # used with fullmatch
```

Group 1 is what stands before the operator and group 2 is the target glued behind it. For a word
the pattern matches:

1. The next word is dropped when group 2 is empty. The operator stood bare or ended the word, so
   its target is the next word.
2. Group 1 is kept as the word, unless it is empty or all digits. All digits is a file
   descriptor, which is the test `readTokenAt` makes before it ends a word.

A word the pattern does not match is kept whole. `REDIRECTION` keeps its name and takes this
value; its one reader is `check_bar`, so the old value and the `re.split` beside it go.

The review's sketch of the pattern puts the digits in a group of their own after a lazy group 1.
That form reads `over2>x.log` as the word `over`. Rule 2 is the hook's own test instead, so a
digit run counts as a descriptor only when it is the whole of what precedes the operator.

### The two reads

For each simple command `check_bar` builds two raw word lists and runs "The redirection rule" and
the leg match over each. A leg spelled by either is a hit.

| Read | Raw words | What it is for |
|---|---|---|
| flat | `command.split()`, as today | a quoted body read as words: `bash -c "<script> --selftest"` |
| quoted | `re.findall(r"(?:[^\s\"']|\"[^\"]*\"|'[^']*'|[\"'])+", command)` | a quoted run holding a space stays one word |

The quoted read is the review's corrected fix for item M2, unchanged. It does no escape
processing, so a backslash survives for the `\` to `/` fold. The flat read is kept beside it for
the reason "Evidence" records. Every hit of today's reader is a hit of the flat read, so the
change adds hits and removes none.

The leg match, `BAR`, `SIMPLE_COMMAND_SPLIT`, `derive_flag_suites`, the hit clause and the three
call sites in `main` stay as they are.

### The spelling table

One table, two expected columns. Each row is `[id, command, hook, lint]`, the shape of
TOOL-aClearedLedger-11's table, so its probes H and C read this file unchanged. The hook column is
the hook as TOOL-aClearedLedger-12 leaves it. The fence is the JSON file both probes read.

```json
[
["T1", "python t/over.py --selftest> x.log", "hit", "hit"],
["T2", "python t/over.py --selftest< in", "hit", "hit"],
["T3", "python t/over.py --selftest>> x.log", "hit", "hit"],
["T4", "python t/over.py --selftest<<< x", "hit", "hit"],
["T5", "python t/over.py --selftest&> x.log", "hit", "hit"],
["T6", "python t/over.py --selftest >& x.log", "hit", "hit"],
["T7", "python t/over.py --selftest 2>& 1", "hit", "hit"],
["T8", "python t/over.py --selftest > \"my log.txt\"", "hit", "hit"],
["T9", "python t/cases.py --fixture --strict-from \"my dir/\"", "hit", "hit"],
["T10", "python t/cases.py --fixture --strict-from \"my dir/\" one-case", "miss", "miss"],
["T11", "bash -c \"python t/over.py --selftest\"", "hit", "hit"],
["T12", "python T\\Over.py --selftest 2>x.log", "hit", "hit"],
["T13", "python -m pdb t/over.py --selftest", "hit", "hit"],
["T14", "python t/over.py 2>&1 --selftest", "miss", "hit"],
["T15", "python t/over.py &>x.log --selftest", "miss", "hit"],
["T16", "python ${DIR}t/over.py --selftest", "miss", "hit"],
["T17", "git log --grep 'over.py --selftest'", "miss", "hit"],
["T18", "bash -c 'bash -c \"python t/over.py --selftest\"'", "miss", "hit"],
["T19", "python t/over.py --selftest --quiet > \"my log.txt\"", "miss", "miss"]
]
```

Rows T1 to T7 are item M1 and rows T8 to T10 item M2. Row T11 is the hit the flat read keeps, and
row T12 the backslash and the descriptor digits. Row T13 is item M3's payload. Rows T14 to T18 are
the places the columns differ, and in each the lint is the reader that over-reads:

| Rows | The difference | Cause |
|---|---|---|
| T14, T15 | a redirection carrying `&` ahead of the direct-check word | the hook cuts the command at the `&` |
| T16 | a glued variable prefix, `${DIR}<script>` | the lint splits at `{` and `}`, the hook keeps the word |
| T17 | a quoted mention | the lint has no quote state |
| T18 | a `bash -c` body inside another | the lint has no depth |

Rows T14 and T15 are a gap of the hook: bash runs the suite, and the hook reads two commands.

### The lint's suite

`WRAPPER_SPELLINGS` gains nine entries after the ten it holds (PINNED, 2026-11-14, at `3a1456b4`).
Each is single-quoted in the array, as its neighbours are, so `${DIR}` and each `"` reach the probe
as typed.

| Entry | Item | Row |
|---|---|---|
| `python t/over.py --selftest> x.log` | M1 | T1 |
| `python t/over.py --selftest<<< x` | M1 | T4 |
| `python t/over.py --selftest&> x.log` | M1 | T5 |
| `python t/over.py --selftest >& x.log` | M1 | T6 |
| `python t/over.py --selftest > "my log.txt"` | M2 | T8 |
| `python t/plant.py fixture --strict "my dir/"` | M2 | T9, spelled for the staged `plant` leg |
| `python t/over.py 2>&1 --selftest` | M4 | T14 |
| `python t/over.py &>x.log --selftest` | M4 | T15 |
| `python ${DIR}t/over.py --selftest` | L1 | T16 |

The assertion stays one line of output and one `arm ok` or `arm FAIL` line, so no assertion is
added and this suite's `FLOOR_ASSERTIONS` does not move. Its label says a staged leg, since one
entry now spells `plant`. The quoted value sits here and not in the option pair assertion: that
probe's body is single-quoted and its tokens are double-quoted strings, so it cannot spell a `"`.

The entry `bash -c "python t/over.py --selftest"`, which the array holds today, is the arm of the
flat read: with the quoted read alone it is no hit.

### The hook's suite

Three arms join the block that opens `TOOL-aClearedLedger-11: the spellings the closing review
walked past row D6`, after the arms TOOL-aClearedLedger-12 adds and before `build_fixture
VERIFYING`, so the 900 manifest is planted (PINNED, 2026-11-14, at `61442a16`). Each runs through
`run_planted` against `"$B"`. `$M_REST` and `$M_FLAG` are that block's own.

| Arm | Label | Command fed | Exit | Item |
|---|---|---|---|---|
| 1 | `D6 the leg behind python3 -m pdb -> deny` | `python3 -m pdb $M_REST` | 2 | M3 |
| 2 | `D6 a kept gap: a 2>&1 ahead of the flag -> allow` | `${M_FLAG% --selftest} 2>&1 --selftest` | 0 | M4 |
| 3 | `D6 a kept gap: a glued variable prefix -> allow` | `python3 ${DIR}zz-kit/planted_suite.py --selftest`, single-quoted so `${DIR}` is literal | 0 | L1 |

Arms 2 and 3 pin a miss on purpose. Each is the hook's half of a difference the texts state, and
each fails on the day the hook reads the spelling, which is the day the texts must move. The
suite's payload liveness guard is what keeps an allow arm from passing on an empty payload.

`FLOOR_ASSERTIONS` rises by the three arms of this table (DERIVED: the value
TOOL-aClearedLedger-12 leaves in the file, plus one assertion per arm). A `RAISED` comment line in
the file's own form names both values and this unit, above the line for TOOL-aClearedLedger-12.

### The template size suite

`build_cap_repo` takes a second parameter, the `enforce` value its policy file carries, defaulting
to `warn`. The calls the suite holds pass one argument and are unchanged.

Two arms follow arm A25b:

| Arm | Staging | Helper | Expects |
|---|---|---|---|
| A25c | `build_cap_repo 40960 bogus` | `expect_out`, exit 1, through `run_cap_gate` | the output holds `The policy reader refused:` |
| A25d | the same repository | `expect_absent`, exit 1, through `run_cap_gate` | the output does not hold `handed-in default because` |

The reader refuses the whole policy file, answers the handed-in default with source `constant`
and prints its refusal after the row ("Evidence"). The default is above the limit check 8 reads
through `budgets.py home codex-instructions`, so check 8 is reached with a refusal to print.
`tools/check-template-size.sh@cfc1e876` was read for this and not run: the answer's first line
fills `MAX_BYTES`, the lines after it fill `_refused`, and the exit is 1 because the `home` verb
answered. This is the review's corrected form: beside A25, never beside A19b, whose run exits at
check 5.

The suite pins no assertion count, so no floor moves.

### The texts

Each of the three texts lists the lint's over-reads and carries no count of them. A count typed
beside a list is the value that went stale. All three carry the phrases `glued variable prefix`
and `ahead of the direct-check word`, which AC6 reads.

| Text | What it says after this unit |
|---|---|
| header comment of `gate-guard.js`, row D6 | the gap list gains: a redirection carrying `&` ahead of the direct-check word cuts the command there. Its last sentence lists the four differences of "The spelling table" |
| `tools/unattended/README.md`, the paragraph on row D6 | the same gap and the same list |
| docstring of `check_bar` | the redirection rule and the two reads in this file's own words, and the same list in place of the sentence on two places |
| comment above `SIMPLE_COMMAND_SPLIT` | the separator characters are the hook's, and the split differs from the hook's in two places: an `&` beside a `>` does not split here and does there, and the braces of `${ }` split here and not there. In both the lint reads more |

The comment's sentence that both readers cut one command into the same simple commands goes.

### What this corrects in the frozen spec

The spec of TOOL-aClearedLedger-11 is CLOSED and keeps its text. Where it and this spec differ,
this spec is the rule.

| Frozen statement | Correction |
|---|---|
| S3 and "The lint", step 3: a word is cut at its first `>` or `<` | everything from the operator on is a redirection, and a bare tail drops the next word |
| S4 and "The lint", step 1: each word is read with its quote characters out | two reads, and the quoted one keeps a quoted run whole |
| "The lint": `SIMPLE_COMMAND_SPLIT` becomes the hook's separator set | the characters are the hook's; the split differs in the two places "The texts" names |
| "The spelling table": rows R33 and R35 are the two places the columns differ | four kinds of spelling differ, rows T14 to T18 of this spec |
| The same paragraph: no spelling the hook denies is admitted by the lint | true for every row of both tables once this unit and TOOL-aClearedLedger-12 are built |
| "The texts", last table row, and S5: the lint's over-reads are two | a list of four, with no count |
| Section 3: the arm for the template size gate's suite is out | arms A25c and A25d are that arm |
| AC1, row R29: `python -m pdb` is observed by the probe alone | arm 1 of "The hook's suite" feeds it |

### What it does not check

- That the two suites' staged rows stay equal to each other. Ask TOOL-aDeferredBar-20 owns that.
- That the list of differences is complete. The probes read the rows of two tables and no more.
- A separator inside a quoted run. `SIMPLE_COMMAND_SPLIT` has no quote state, so a quoted value
  holding `;` or `|` is still cut, and the lint reads the pieces.
- A PowerShell-only spelling of any row. Probe H feeds every row as a `Bash` payload.
- The real manifest's legs through either probe. The legs are staged.
- The docstring and the comments beyond the greps of AC6. The closing review reads them against
  the code.
- Check 8's output through a criterion. A role agent's pass runs no gate, so the printed clause is
  the arms' to observe.

### Inventory

This unit mints no identifier. `REDIRECTION`, `check_bar`, `WRAPPER_SPELLINGS` and
`build_cap_repo` keep their names. The quoted read's pattern is written in `check_bar` at its one
use.

### Migration

None. No stored shape moves.

### Rollout

No switch. The lint grades only a live spec dated at or after `SPEC_DIRECT_CUTOFF`. Every spelling
the wider reader newly refuses is one the hook already refuses inside a build pass.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/unattended/gate-guard.js`
- `tools/unattended/gate-guard.test.sh`
- `tools/unattended/README.md`
- `tools/check-template-size.test.sh`

### Alternatives rejected

- **The quoted read in place of the flat read**, the review's corrected fix for item M2 taken
  alone. Test: a scratch copy with that read alone, fed TOOL-aClearedLedger-11's table. It read
  row R18 as no hit, a spelling the hook denies, and rows R33 and R35 as no hit (PINNED,
  2026-11-14). The under-read rejects it.
- **`shlex.split`**, the finder's fix for item M2. The review's skeptic rejected it: it eats an
  unquoted backslash, which breaks the `\` to `/` fold.
- **Setting `drop_next` only when the remainder is empty or `>` and `&`**, finding 4's fix for
  item M1. The review judged it instance-only: `--selftest<<< x` and `--selftest&> x.log` stay
  lint misses.
- **Making the hook read a redirection ahead of the flag**, the first branch of the review's fix
  for item M4. Test: a scratch copy whose `scanSegments` alone kept an `&` beside a `>` changed no
  row. A copy that also changed `readTokenAt` read rows T14 and T15 as hits and rows T5 to T7 as
  misses (PINNED, 2026-11-14). The cure reaches the word reader every row shares, which the
  skeptic's caution excludes and which TOOL-aClearedLedger-12 has just settled. The brief asks for
  the lint's arm and a true comment, which is the review's second branch.
- **Keeping `${ }` one word in the lint**, the second branch of the review's fix for item L1. It
  needs a brace state a split pattern cannot hold, and it makes the lint pass a spelling of an
  over-bound suite that bash runs. The brief asks that the texts agree with the code.
- **Arm A25c beside A19b**, the finder's fix for item L2. The review's skeptic rejected it: that
  run exits at check 5.
- **One shared spelling file now.** It is a new artifact with an owner, ask TOOL-aDeferredBar-20.

## 5. Production-readiness checklist

- security — N/A — a spec lint and a hook's comment. The lint refuses more and adds no read, write
  or grant.
- perf / scale — `check_bar` runs the leg match over two word lists in place of one, per simple
  command of a backticked token.
- error / empty / loading states — a word that is only an operator yields no word, and an
  operator that ends the command drops nothing.
- observability — the lint's hit clause is unchanged and names the leg and its ceiling.
- risks — the wider reader may red a live spec that spells an over-bound leg in a form it now
  reads. Section 7 names the leg that shows it. The quoted read has no escape processing, so an
  escaped quote inside a quoted run ends the run early; the flat read still sees its words.
- testing — AC1 to AC8 are probes a pass runs. The arms of section 7 are the main loop's.
- migration — N/A — no stored shape moves.
- user docs — `tools/unattended/README.md`, S5. No page under `help/` names the hook's rows.

## 6. Acceptance criteria

Probes H and C are those of TOOL-aClearedLedger-11's section 4, saved as that section says. The
rows file is this spec's table, and the older rows file is that spec's.

- **AC1** — When probe C runs through `python` against `tools/check-spec-tokens.py` and the rows
  file, its last line reads `rows wrong: 0 · no set: False`, and it reads the same over the older
  rows file.
  Red when: a word's target survives its operator, which names rows T1 to T7; the quoted read is
  absent, which names rows T8 and T9; or the flat read is absent, which names row T11 here and
  row R18 there.
  figure: at `a54346ee` the first run prints `rows wrong: 9` (PINNED, 2026-11-14).
- **AC2** — When probe H runs through `node` against `tools/unattended/gate-guard.js` and the rows
  file, its last line reads `rows wrong: 0`.
  Red when: the hook reads a spelling the texts list as a difference, which names a row of T14 to
  T18, or a head-less segment yields no candidate, which names row T13.
  fixture: the tree must hold TOOL-aClearedLedger-12's guard. Without it the probe names row T3.
- **AC3** — When `grep -c 'run_planted "D6 the leg behind python3 -m pdb' tools/unattended/gate-guard.test.sh`
  runs it prints 1, and `grep -c 'run_planted "D6 a kept gap: ' tools/unattended/gate-guard.test.sh`
  prints 2.
  Red when: an arm of "The hook's suite" is absent or runs outside `run_planted`.
  figure: both are DERIVED, the rows of that table; at `61442a16` each command prints 0.
- **AC4** — When the unit's files are staged and
  `git diff --cached -U0 -- tools/unattended/gate-guard.test.sh | grep '^[-+]FLOOR_ASSERTIONS='`
  runs, it prints one removed line and one added line, and the added value is the removed value
  plus 3.
  Red when: the floor did not follow the arms the suite gained.
  figure: 3 is DERIVED, the row count of the table in "The hook's suite".
- **AC5** — When `grep -c -e '--selftest> x.log' -e '--selftest<<< x' -e '--selftest&> x.log' -e '--selftest >& x.log' -e '"my log.txt"' -e '"my dir/"' -e '2>&1 --selftest' -e '&>x.log --selftest' -e '${DIR}t/over.py' tools/check-spec-tokens.test.sh`
  runs it prints 9 or more, and
  `git diff --cached -- tools/check-spec-tokens.test.sh | grep -c '^[-+]FLOOR_ASSERTIONS='`
  prints 0.
  Red when: an entry of "The lint's suite" is absent, or the floor moved for an assertion that
  was not added.
  figure: 9 is DERIVED, the rows of that table, one line each; at `3a1456b4` the first command
  prints 0.
- **AC6** — When `grep -c 'glued variable prefix' tools/unattended/gate-guard.js tools/unattended/README.md tools/check-spec-tokens.py`
  and `grep -c 'ahead of the direct-check word' tools/unattended/gate-guard.js tools/unattended/README.md tools/check-spec-tokens.py`
  run, each prints 1 or more for every file. When
  `grep -c 'two spellings' tools/unattended/gate-guard.js tools/unattended/README.md` and
  `grep -c -e 'in two places' -e 'the same simple commands' tools/check-spec-tokens.py`
  run, each prints 0 for every file.
  Red when: a text still counts two over-reads, or the comment still claims one cut.
  figure: at `a54346ee` the first two commands print 0 for every file, the third prints 1 for
  each file and the fourth prints 2 (PINNED, 2026-11-14).
- **AC7** — When the pass builds the scratch repository of "The cap fixture probe" below and runs
  `python tools/policy/budgets.py resolve AGENTS.md=default:49152` in it with stderr merged, the
  command exits 0, its first line's fourth field is `constant`, a later line opens
  `policy: refused`, and the first line's second field is above the third field that
  `python tools/policy/budgets.py home codex-instructions` prints there. And
  `grep -c -e 'A25c ' -e 'A25d ' tools/check-template-size.test.sh` prints 2.
  Red when: the staged policy file does not make the reader refuse, the cap it answers is inside
  the limit so check 8 is never reached, or an arm is absent.
  figure: both fields are DERIVED at observation time, and 2 is the row count of the arm table.
- **AC8** — When the unit's files are staged and
  `git diff --cached --name-only | grep -cxFf <(sed -n 's/^watch: //p' memory/guides/SESSION-KICKOFF.md | tr ';' '\n' | sed 's/^ *//')`
  runs, it prints 0.
  Red when: a watched file is staged. The commit then owes the `last-audit` stamp and its
  `manifest-audit:` delta line, and the pass stages the stamp before it commits.

The cap fixture probe. `<F>` is a new directory in the session scratchpad, and the block runs from
the worktree's toplevel. It is `build_cap_repo 40960 bogus` written out by hand.

```bash
mkdir -p "$F/tools/policy" "$F/tools/playbook" "$F/.governance"
cp -R tools/policy/. "$F/tools/policy/"
cp tools/playbook/render_playbook.py "$F/tools/playbook/"
tr -d '\r' < AGENTS.md > "$F/AGENTS.md"
printf '# no AGENTS.md row\n' > "$F/tools/template-size-limits.txt"
printf '[budgets]\nenforce = "bogus"\n"AGENTS.md" = 40960\n' > "$F/.governance/policy.toml"
git -C "$F" init -q && git -C "$F" symbolic-ref HEAD refs/heads/main && git -C "$F" add -A \
  && git -C "$F" -c user.name=t -c user.email=t@t.test -c commit.gpgsign=false commit -qm fixture
(cd "$F" && python tools/policy/budgets.py resolve AGENTS.md=default:49152 2>&1; echo "exit $?")
(cd "$F" && python tools/policy/budgets.py home codex-instructions)
```

## 7. Gates

The main loop runs the three suites at the close, on a frozen clone, and the bar once after the
last unit. The hook's suite is withheld from the manifest and runs through the unattended kit's
runner. Before each suite's green run the main loop observes each arm below RED on the failing
case its line names, with the arms in place, and GREEN once the case is restored. A green run of
the lint's suite prints the wrapper spellings line as `arm ok`; of the hook's suite, an `ok` line
for each arm of section 4's table, no line opening `FAIL`, and a total at or above
`FLOOR_ASSERTIONS`; of the template size suite, an `arm ok` line for A25c and for A25d.

The main loop also runs the first leg below by its own argv over the tree and reads its output for
a row carrying `[bar]`: a live spec that spells an over-bound leg in a form the wider reader now
sees is fixed in that spec, never waived.

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `template size gate selftest` · `install-prefix (shipped surface)` · `lexicon naming predicates`

New arm: `tools/unattended/gate-guard.test.sh` · covers AC2 AC3 · arm 1 of "The hook's suite"; the failing case is `if (head === null) continue` put back ahead of the `cls` line of `scanDenyHits`, so the segment yields no candidate and the arm exits 0 · `FLOOR_ASSERTIONS` up by the three arms of that table, DERIVED from the value TOOL-aClearedLedger-12 leaves, shared by every arm of this suite
New arm: `tools/unattended/gate-guard.test.sh` · covers AC2 AC3 · arm 2; the failing case is the gap closed, `scanSegments` and `readTokenAt` both keeping an `&` beside a `>` inside the word, so the leg is read and the arm exits 2 · the same floor move
New arm: `tools/unattended/gate-guard.test.sh` · covers AC2 AC3 · arm 3; the failing case is the brace state of `scanSegments` taken out, so the command is cut at `{` and `}`, the leg is read and the arm exits 2 · the same floor move
New arm: `tools/check-spec-tokens.test.sh` · covers AC1 AC5 · the wrapper spellings assertion, widened by the four entries of item M1; the failing case is the redirection rule's first step taken out, so a target survives its operator · none, no assertion is added
New arm: `tools/check-spec-tokens.test.sh` · covers AC1 AC5 · the same assertion, the two entries of item M2; the failing case is the quoted read taken out, leaving the flat read alone · none
New arm: `tools/check-spec-tokens.test.sh` · covers AC1 AC5 · the same assertion, the two entries of item M4; the failing case is the `&` alternative of `SIMPLE_COMMAND_SPLIT` put back to a plain `&` in the set · none
New arm: `tools/check-spec-tokens.test.sh` · covers AC1 AC5 · the same assertion, the entry of item L1; the failing case is `{` and `}` taken out of `SIMPLE_COMMAND_SPLIT` · none
New arm: `tools/check-spec-tokens.test.sh` · covers AC1 · the same assertion's standing entry `bash -c "python t/over.py --selftest"`, now the arm of the flat read; the failing case is the flat read taken out, leaving the quoted read alone · none
New arm: `tools/check-template-size.test.sh` · covers AC7 · arm A25c; the failing case is the `${_refused:+…}` expansion taken out of the `fail 8` call of `tools/check-template-size.sh`, which the suite copies into its scratch repository, so the clause is not printed · none, the suite pins no assertion count
New arm: `tools/check-template-size.test.sh` · covers AC7 · arm A25d; the failing case is the clause put back to its wording before TOOL-aClearedLedger-11, which names the handed-in default · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.

## 10. Reuse audit

The seams are the readers and suites that exist: `tools/check-spec-tokens.py#check_bar` with its
`REDIRECTION` pattern, the `WRAPPER_SPELLINGS` array and its staged assertion in the lint's suite,
`run_planted` over the planted manifest in the hook's suite, and `build_cap_repo` with
`run_cap_gate` in the template size suite. Probes H and C are TOOL-aClearedLedger-11's, read
unchanged. `python tools/codebase-map/reuse_lookup.py "split a shell command into words keeping a
quoted value with a space as one word and dropping redirection words, in a spec lint that mirrors
a hook"` ranked name-stem neighbours only, `resolve_shell_argv` and `scan_shell_lines` among them,
and named no shared word reader, so for one tokenizer serving both readers no existing seam fits:
one is JavaScript in a copy-installed kit and the other a repository-root python tool. The recall
probe returned the specs of TOOL-aClearedLedger-11 and TOOL-aClearedLedger-12, the review record
and ask TOOL-aDeferredBar-20, which section 3 hands the shared spelling list to. The hits agreed
with source, with one exception recorded in section 4: the review's corrected fix for item M2,
taken alone, loses a hit the hook makes.

Recall terms used: check_bar gate-guard D6 redirection drop_next quote-aware tokenise
WRAPPER_SPELLINGS over-read lookaround SIMPLE_COMMAND_SPLIT build_cap_repo policy reader refused
