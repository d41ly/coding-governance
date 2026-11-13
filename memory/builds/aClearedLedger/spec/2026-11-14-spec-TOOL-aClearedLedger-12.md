# TOOL-aClearedLedger-12 — the gate guard's word reader keeps a two-character redirection operator whole, so row D6 denies an over-bound suite whose output is appended

**Status:** SPECCED · rev-1 · 2026-11-14 · node a · Tier-2 · base 8db6f4be · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-prompt-TOOL-aClearedLedger-12-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-12-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aClearedLedger-12-brief.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-12-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The word break TOOL-aClearedLedger-11 added to `readTokenAt` also fires on the second character of
`>>`, `2>>` and `<<`, so row D6 of `tools/unattended/gate-guard.js` allows an over-bound suite
whose output is appended with a spaced operator, which it denied before that unit. This unit keeps
an operator one word and arms the appended spellings, as item H1 of the round 2 review states.

## 2. Scope (IN)

The review is
`memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-11-diff-review-round2.md`.
Every item below serves its item H1.

- **S1** — `readTokenAt` of `tools/unattended/gate-guard.js` does not end a word at an unquoted
  `>` or `<` while the word read so far is itself a redirection operator. The guard is the
  record's form, given in section 4, "The guard". Observed by AC1 and AC2.
- **S2** — `tools/unattended/gate-guard.test.sh` gains the deny arms of section 4, "The arms", one
  per appended spelling the record lists, each over the planted manifest. Observed by AC3.
- **S3** — `FLOOR_ASSERTIONS` of that suite rises by the count of those arms, with a `RAISED`
  comment line in the file's own form. Observed by AC4.
- **S4** — The docstring of `readTokenAt` and the comment inside the changed branch say what S1
  makes true. NOT OBSERVED: no probe tells a true comment from a stale one, and the closing review
  reads both against the code.

## 3. Non-goals (OUT)

- Items M1 to M4, L1 and L2 of the review. The roster gives them to TOOL-aClearedLedger-13.
- Any edit to `tools/check-spec-tokens.py` or its suite. The lint already reads the spaced
  appended spellings as hits (section 4, "Evidence").
- The whole of the review's left-shift line under H1: one deny arm per operator of the redirection
  set in both the spaced and the glued form. The brief asks for the record's listed arms. The
  probe of AC1 reads the wider set once, and section 4 says which operators no arm feeds.
- Any edit to `REDIRECT_RE`, to `scanSegments`, to `scanDenyHits` or to `checkSuiteLeg`.
- Any edit to `tools/unattended/README.md` or to the hook's header comment. Their sentence that a
  redirection hides nothing is false today and true again once S1 is built.
- Any edit to the spec of TOOL-aClearedLedger-11, which is CLOSED. Its correction is stated here.
- A lowered floor, a waived arm, and any kit version, which the lander's `mint` moves.

### Edges

- **consumes-from** external — the glued-redirection word break and the planted-manifest arm
  block that TOOL-aClearedLedger-11 built. Without them there is no break to narrow and no block
  for the arms to join.
- **hands-off** external — items M1 to M4, L1 and L2 of the review, which the build's roster gives
  TOOL-aClearedLedger-13. That unit's spec is authored beside this one, so the edge is written as
  prose and not as a join.

## 4. Design

### Evidence

Read at `a54346ee`, the branch tip. The blobs are `tools/unattended/gate-guard.js@e3e8092e` and
`tools/unattended/gate-guard.test.sh@61442a16`.

- **The break tests for digits alone.** The branch at `tools/unattended/gate-guard.js@e3e8092e:396`
  ends a word at `>` or `<` when the word so far is not empty and not all digits. A word so far of
  `>`, `2>` or `<` passes that test, so the operator's second character opens a new word.
- **The candidate then keeps the target.** In `gate-guard.js#scanDenyHits` a bare operator word
  skips the word after it. The first `>` skips the second, and the real target stays in `words` as
  an argument. `gate-guard.js#checkSuiteLeg` refuses a spelling longer than the leg.
- **Probed, nothing run.** The probe of "The probe" below was fed three copies of the hook: the
  blob at `f2680896` (the range's base), the tip, and the tip with the guard of "The guard"
  applied in the session scratchpad. Rows Q1 to Q5 read hit, miss, hit across the three copies
  (PINNED, 2026-11-14). Row Q6 reads miss, miss, hit (PINNED, 2026-11-14).
- **The token stream.** `scanSegments` over `a >> b 2>> c <<< d` gives `a,>>,b,2>>,c,<<<,d` at
  `f2680896` and with the guard applied, and `a,>,>,b,2>,>,c,<,<,<,d` at the tip (PINNED,
  2026-11-14).
- **The lint already agrees on the spaced forms.** `check-spec-tokens.py#check_bar` at
  `tools/check-spec-tokens.py@4a71f25e` reads rows Q1 to Q5 as hits (PINNED, 2026-11-14). It
  misses rows Q6 and Q13, which is the review's item M1 and not this unit's.
- **No arm feeds a spaced append.** The one redirection arm of the planted block before
  TOOL-aClearedLedger-11 feeds `> x.log 2>&1`, and that unit's two feed a glued `>x.log`.
- **An `&` reaches the word only quoted.** `scanSegments` splits on every unquoted `&`, and
  `readTokenAt` ends a word at one. The `&` of the guard is reachable through a quoted `&` alone.

### The guard

In `readTokenAt` the branch condition's last clause changes. Nothing else in the branch moves.

```js
} else if ((ch === '>' || ch === '<') && !brace && out !== '' && !/^(?:\d*|&)[<>]*$/.test(out)) {
```

The pattern is the operator prefix `REDIRECT_RE` already reads: file-descriptor digits or an `&`,
then any run of `<` and `>`. While the word so far matches it the word is still an operator, so
`>>`, `2>>`, `<<<` and a glued target read on as one word, as before TOOL-aClearedLedger-11. Once
the word holds anything else, a `>` or `<` ends it, which keeps that unit's break for
`--selftest>x.log` and for a suite word of rows D2 to D4.

The docstring of `readTokenAt` says a word ends before an unquoted `>` or `<` once it holds
anything but a redirection operator. The comment inside the branch says the same.

### The arms

Each arm joins the block that opens `TOOL-aClearedLedger-11: the spellings the closing review
walked past row D6`, after its last `run_planted` line and before `build_fixture VERIFYING`, so
the 900 manifest is planted. Each runs through `run_planted` against `"$B"` and expects exit 2.

| Arm | Name, after `D6 the leg appended ` | Command fed |
|---|---|---|
| 1 | `to a log -> deny` | `$M_FLAG >> x.log` |
| 2 | `with 2>&1 behind it -> deny` | `$M_FLAG >> x.log 2>&1` |
| 3 | `by 2>> -> deny` | `$M_FLAG 2>> err.log` |
| 4 | `to an unexpanded "$LOG" -> deny` | `$M_FLAG >> "$LOG"`, the variable and its quotes literal |

Arm 4's tail is single-quoted in the suite, so the payload `run` builds carries `"$LOG"` as typed.
Every arm's name opens `D6 the leg appended`, the string AC3 counts.

`FLOOR_ASSERTIONS` moves from 210 to 214 (DERIVED: the floor at `61442a16` plus the arms of this
table, one assertion each). A `RAISED 210 -> 214 at TOOL-aClearedLedger-12` comment line sits
above the line for TOOL-aClearedLedger-11. If the file's floor is no longer 210 when the builder
opens it, the builder adds the arm count to the value found and says so in the ledger.

### The probe

The rows file. Each row is `[id, command, hook]`, and the legs are staged, so no ceiling
re-derivation moves a row.

```json
[
["Q1", "python t/over.py --selftest >> x.log", "hit"],
["Q2", "python t/over.py --selftest >> x.log 2>&1", "hit"],
["Q3", "python t/over.py --selftest 2>> err.log", "hit"],
["Q4", "python t/over.py --selftest >> \"$LOG\"", "hit"],
["Q5", "python t/over.py --selftest << EOF", "hit"],
["Q6", "python t/over.py --selftest>> x.log", "hit"],
["Q7", "python t/over.py --selftest <<< x", "hit"],
["Q8", "python t/over.py --selftest &>> x.log", "hit"],
["Q9", "python t/over.py --selftest 2>>err.log", "hit"],
["Q10", "python t/over.py --selftest >>x.log", "hit"],
["Q11", "python t/over.py --selftest > x.log", "hit"],
["Q12", "python t/over.py --selftest>x.log", "hit"],
["Q13", "python t/over.py --selftest< in", "hit"],
["Q14", "python t/over.py --selftest 2> x.log", "hit"],
["Q15", "python t/over.py --selftest &> x.log", "hit"],
["Q16", "python t/over.py --selftest < in", "hit"],
["Q17", "python t/over.py --selftest --quiet >> x.log", "miss"],
["Q18", "python t/over.py >> x.log", "miss"],
["Q19", "python t/cases.py --fixture one-case >> x.log", "miss"]
]
```

Rows Q1 to Q4 are the arms' spellings. Row Q1 is the row the record asks the spelling table of
TOOL-aClearedLedger-11 to gain. Rows Q7 to Q16 are the spellings that hit at the tip and must
still hit. Rows Q17 to Q19 are scoped or flagless spellings that must still miss.

The probe, saved by the pass in the session scratchpad and run from the worktree's toplevel as
`node <probe file> <rows file>`:

```js
const fs = require('fs'), path = require('path')
const g = require(path.resolve('tools/unattended/gate-guard.js'))
const legs = [
  { name: 'over', ceiling: 301, words: ['t/over.py', '--selftest'] },
  { name: 'cases', ceiling: 301, words: ['t/cases.py', '--fixture', '--strict-from', 'x/'] },
]
const s = 'a >> b 2>> c <<< d'
console.log(g.scanSegments(s, g.buildCommandView(s)).join())
const rows = ['bash x/y.test.sh>x.log', 'bash x/y.test.sh >> x.log', 'bash x/y.test.sh>> x.log']
console.log(rows.map((c) => g.scanDenyHits(c, g.buildCommandView(c), 0, 'Bash').map((h) => h.row).join() || '-').join(' '))
let bad = 0
for (const [id, cmd, want] of JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))) {
  const cand = []
  g.scanDenyHits(cmd, g.buildCommandView(cmd), 0, 'Bash', cand)
  const got = cand.some((c) => g.checkSuiteLeg(c, legs)) ? 'hit' : 'miss'
  if (got !== want) { bad++; console.log(id, 'read', got, 'want', want) }
}
console.log('rows wrong:', bad)
```

### What this corrects in the frozen spec

The spec of TOOL-aClearedLedger-11 is CLOSED and keeps its text. Where it and this spec differ,
this spec is the rule.

| Frozen statement | Correction |
|---|---|
| Section 4, "The word break": the word ends when the word read so far is not empty and is not all digits | it ends when the word read so far is not empty and is not a redirection operator, by "The guard" |
| The same paragraph: an operator that opens a word is read as today | true only once this unit is built; at `e3e8092e` a two-character operator is split |
| Section 4, "The spelling table": the rows carry no appended spelling | row Q1 of this spec's rows file is that row, read as a hit by the hook and by the lint |
| Section 4, "The spelling table": no spelling the hook denies is admitted by the lint | not restored by this unit; rows Q6 and Q13 stay hook hit and lint miss until the review's item M1 is built |

### What it does not check

- No arm feeds a spaced `<<`, `<<<` or `&>>`, or the half-glued `--selftest>> x.log`. The probe of
  AC1 reads each once, at build time, and no gate re-reads them.
- A quoted `&` glued to a redirection, `'&'>x.log`. The record's form reads it as one redirection
  word, so an argument that is a literal `&` is dropped from the candidate.
- A PowerShell-only spelling. The probe feeds every row as a `Bash` payload.
- The lint's answer for any row. `check_bar` is not run by a criterion here.
- The real manifest's legs. The probe's legs are staged, and the arms read the planted manifest.

### Inventory

This unit mints no identifier. `readTokenAt` keeps its name and its signature.

### Migration

None. No stored shape moves.

### Rollout

No switch. The hook binds where it binds today, before `VERIFYING` on a branch with a run record.

### Files touched (estimate)

- `tools/unattended/gate-guard.js`
- `tools/unattended/gate-guard.test.sh`

### Alternatives rejected

- **The narrower pattern `^\d*[<>]*$`**, finding 11's form. The skeptic judged it sound too, and
  it differs from the record's form on the quoted `&` spelling alone, which it reads as an
  argument. The brief asks for the record's form, which is the prefix `REDIRECT_RE` holds.
- **Taking the break out.** Rows Q12 and Q13 and the glued row D4 arm of TOOL-aClearedLedger-11
  go back to misses.
- **Joining split operator words in `scanDenyHits`.** The split would stay in the shared reader,
  and rows D2 to D4 would still see `>`, `>` as two words.
- **One arm per operator in both forms now**, the review's left-shift line. The brief asks for
  the listed arms, and the wider set is read by the probe.

## 5. Production-readiness checklist

- security — N/A — a hygiene rule that fails open, as the hook's header states of itself. The
  change restores a deny and adds no read, write or grant.
- perf / scale — one regular-expression test replaces another, on a `>` or `<` character alone.
- error / empty / loading states — a word that is only an operator, with no target after it, is
  read as one bare operator word, as at `f2680896`.
- observability — the deny text is unchanged and names the leg, as today.
- risks — a quoted `&` glued to a redirection is read as a redirection word (section 4, "What it
  does not check"). No command in the planted block or the probe has that shape.
- testing — AC1 to AC4 are probes a pass runs. The arms of section 7 are the main loop's.
- migration — N/A — no stored shape moves.
- user docs — N/A — the paragraph of `tools/unattended/README.md` on row D6 is true again once S1
  is built, and no page under `help/` names the hook's rows.

## 6. Acceptance criteria

The probe and the rows file are section 4's.

- **AC1** — When the probe runs through `node` against `tools/unattended/gate-guard.js` and the
  rows file, its last line reads `rows wrong: 0`.
  Red when: the break still fires on an operator's second character, which names rows Q1 to Q6, or
  the break was taken out, which names rows Q12 and Q13.
  figure: at `e3e8092e` the last line reads `rows wrong: 6` (PINNED, 2026-11-14).
- **AC2** — When the same probe runs through `node`, its first line reads `a,>>,b,2>>,c,<<<,d`
  and its second reads `D4 D4 D4`.
  Red when: an operator is split, which prints `a,>,>,b,2>,>,c,<,<,<,d`, or the break was taken
  out, which prints `- D4 -`.
- **AC3** — When `grep -c 'run_planted "D6 the leg appended ' tools/unattended/gate-guard.test.sh`
  runs, it prints 4.
  Red when: an arm of section 4's table is absent or runs outside `run_planted`.
  figure: 4 is DERIVED, the row count of section 4's arm table; at `61442a16` the command prints 0.
- **AC4** — When `grep -c '^FLOOR_ASSERTIONS=214$' tools/unattended/gate-guard.test.sh` runs it
  prints 1, and `grep -c 'RAISED 210 -> 214 at TOOL-aClearedLedger-12' tools/unattended/gate-guard.test.sh`
  prints 1.
  Red when: the floor did not follow the arms the suite gained.
  figure: 214 is DERIVED, the floor at `61442a16` plus the arm count of AC3.

## 7. Gates

The hook's suite is withheld from the manifest and runs through the unattended kit's runner. The
main loop runs it at the close, on a frozen clone, and the bar once after the last unit. Before
that green run the main loop observes each arm below RED: with the guard's last clause put back to
`!/^\d+$/.test(out)` and the arms in place, the suite prints a `FAIL` line for each arm of section
4's table and for no other arm. With the guard restored the suite prints an `ok` line for each,
no line opening `FAIL`, and a total at or above `FLOOR_ASSERTIONS`. No file of this unit trips a
manifest guard, so the leg line names the legs that read the two files and this spec.

`spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)` · `lexicon naming predicates`

New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC3 · arm 1; the failing case is the guard's last clause put back to the all-digits test, so `>>` is two words and the arm exits 0 · `FLOOR_ASSERTIONS` 210 to 214, DERIVED, shared by every arm of this unit
New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC3 · arm 2; the same failing case, with `2>&1` after the target left in the candidate's tail · the same floor move
New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC3 · arm 3; the same failing case, where `2>` passes the all-digits test's negation and its second `>` opens a word · the same floor move
New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC3 · arm 4; the same failing case, with a quoted unexpanded variable as the target that stays in the candidate · the same floor move

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.

## 10. Reuse audit

The seam is the word reader itself, `tools/unattended/gate-guard.js#readTokenAt`, and the pattern
is the operator prefix its neighbour `REDIRECT_RE` already holds. The arms join the planted block
through `run_planted` and `$M_FLAG`, which exist. `python tools/codebase-map/reuse_lookup.py "end
a shell word at a glued redirection operator without splitting a two-character append operator,
in the gate guard hook's word reader"` ranked name-stem neighbours only, `resolve_shell_argv` and
`readConfKey` among them, and named no shared word reader, so for a tokenizer serving more than
this file no existing seam fits. `tools/hooks/scratch-guard.js` was not extended: the hook copies
from it and may not require it, as `buildHeredocView` records. The hits agreed with source.

Recall terms used: gate-guard readTokenAt REDIRECT_RE redirection append operator word break D6
run_planted planted manifest FLOOR_ASSERTIONS scanSegments
