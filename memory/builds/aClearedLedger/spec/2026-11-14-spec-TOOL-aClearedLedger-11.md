# TOOL-aClearedLedger-11 — the gate guard's row D6 and the spec checker's bar join read one command alike, and each new branch has an arm that can fail

**Status:** CLOSED · rev-1 · 2026-11-14 · node a · Tier-2 · base 8db6f4be · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aClearedLedger-11-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aClearedLedger-11-1-acceptance-ledger.md) | journal | — |
| [2026-11-13-prompt-TOOL-aClearedLedger-11-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-11-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-aClearedLedger-11-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-11-brief.md) | research | — |
| [2026-11-14-review-TOOL-aClearedLedger-11-12-13-diff-review-round3.md](../reviews/2026-11-14-review-TOOL-aClearedLedger-11-12-13-diff-review-round3.md) | diff-review | TOOL-aClearedLedger-12 TOOL-aClearedLedger-13 |
| [2026-11-14-review-TOOL-aClearedLedger-11-diff-review-round2.md](../reviews/2026-11-14-review-TOOL-aClearedLedger-11-diff-review-round2.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review confirmed that the two readers of the over-bound suite rule answer
differently for one command, and that five new branches have no arm that can fail. This unit gives
both readers one match rule, arms each branch, and corrects one message clause. It is the batch
the build method's M4 promotes from the review's items M1 to M7, L1 and L2.

## 2. Scope (IN)

The review is
`memory/builds/aClearedLedger/reviews/2026-11-13-review-TOOL-aClearedLedger-1-2-3-4-5-6-7-9-10-diff-review-round1.md`.
Each item below names the review item it closes.

- **S1** — Item M1. Row D6 of `tools/unattended/gate-guard.js` matches a leg's script at any word
  of a simple command, whatever the launcher grammar resolved as the head. Observed by AC1.
- **S2** — Item M2. In both readers a changed option value is no scoped variant. After a leg's
  direct-check word an option name must equal the leg's, and the value after it may be any word.
  Observed by AC1 and AC2.
- **S3** — Item M3. In both readers a word names a leg's script with leading `./` segments taken
  off, and by a trailing path in either direction. In the hook a word ends at an unquoted `>` or
  `<`; in `tools/check-spec-tokens.py` a word is cut at its first one. Observed by AC1, AC2 and AC3.
- **S4** — Item M4. `check_bar` splits a token on the hook's separator set and reads each word
  with its quote characters taken out. Observed by AC2.
- **S5** — The texts say what S1 to S4 make true, and name each gap this unit keeps: the header
  comment of `tools/unattended/gate-guard.js`, the paragraph of `tools/unattended/README.md` headed
  "The act is refused at the tool call", and the docstring of `check_bar` with the comment above
  `SIMPLE_COMMAND_SPLIT`. Observed by AC4 for the header and the README. The docstring and the
  comment are NOT OBSERVED: no probe tells a true comment from a stale one, and the closing review
  reads them against the code.
- **S6** — Item M5. `tools/unattended/gate-guard.test.sh` gains two arms that send a row D2 hit
  beside a row D6 candidate, one with the manifest absent and one with it unparsable, each
  expecting a deny. Observed by AC5 for the behaviour and AC10 for the arms.
- **S7** — Item M6. `tools/check-spec-tokens.test.sh` gains two command-line arms over a scratch
  manifest whose row carries a `ceiling`: one above the bound that reds with the leg named, one at
  the bound that is clean. Observed by AC9.
- **S8** — Item M7. The staged spellings assertion of `tools/check-spec-tokens.test.sh` gains the
  redirected, the piped and the backslash spelling, and the call with no set. Two staged
  assertions join it for S2 to S4. Observed by AC2 for the branches and AC9 for the arms.
- **S9** — The arm class "a manifest suite in flag form" of `tools/unattended/gate-guard.test.sh`
  gains the arms of S1 to S3 (section 4, "The hook's suite"). Observed by AC1 and AC3, whose rows
  are the arms' payloads, and by AC10.
- **S10** — Item L1. The same class gains one arm that spells the planted leg by a backslashed,
  upper-case path. Observed by AC1, row R9, and by AC10.
- **S11** — Item L2. Check 8 of `tools/check-template-size.sh` introduces the reader's refusal
  with the clause `The policy reader refused:`, which is true for every source. Observed by AC6.
- **S12** — The `last-audit` value of `memory/guides/SESSION-KICKOFF.md` is re-stamped in the
  unit's closing commit, with a delta line in the commit message. S11 moves a file its `watch:`
  line names. Observed by AC7.
- **S13** — Each suite's `FLOOR_ASSERTIONS` rises by the count of assertions this unit adds to it.
  Observed by AC8.
- **S14** — The tracked tree gains no `[bar]` hit from S2 to S4. Observed by AC11.

## 3. Non-goals (OUT)

- Item H1 of the review. It is the main loop's observation record and no code.
- One fixture file of spellings read by both suites, the left-shift line under items M1 to M4.
  Ask TOOL-aDeferredBar-20 already owns that mechanism. Each suite here stages its own rows.
- The arm the review's left-shift line under item L2 names for the template size gate's suite.
  The brief asks for the clause alone.
- Any edit to the pattern `BAR`, to `DIRECT_CHECK_BOUND` or to `DIRECT_CHECK_WORDS` in either file.
- Any edit to `tools/gate-legs.json`. No ceiling, argv or guard moves.
- Rows D1 to D5 of the hook, except what S3's word break gives them (section 4, "The word break").
- A resolve of a path against the payload's working directory (section 4, "Alternatives rejected").
- Any edit to a CLOSED spec. Units 3, 5 and 7 are frozen, and each correction is stated here.
- A lowered floor, a waived arm, and any kit version, which the lander's `mint` moves.

### Edges

- **consumes-from** external — the gate manifest's `chunk`, `argv` and `ceiling` fields as the
  run-gates kit writes them. Both readers arm on them and neither writes them.
- **hands-off** external — ask TOOL-aDeferredBar-20, the one spelling list both suites would read.
  Until it is built, the equality of the two suites' staged rows is held by this spec's table alone.
- **hands-off** external — item H1 of the review, which the main loop records before landing.

## 4. Design

### Evidence

Read at `f2680896`, the branch tip. The blobs are `tools/unattended/gate-guard.js@c72cb323` and
`tools/check-spec-tokens.py@34fce99b`.

- **The hook builds its candidate from the head alone.** `gate-guard.js#scanDenyHits` pushes
  `{ head, words }` only when a head was resolved, and `gate-guard.js#checkSuiteLeg` compares that
  head to the leg's script. A launcher the grammar does not skip is itself the head.
- **The hook compares later words by equality.** `checkSuiteLeg` wants each later word equal to the
  leg's word at that place, so a changed directory after `--strict-from` is a miss.
  `tools/policy/check_policy.py#USAGE` reads `--fixture [--strict-from <dir>] [<case>]`: the
  directory scopes nothing.
- **The word reader has no redirection break.** `gate-guard.js#readTokenAt` ends a word at
  whitespace and at `;`, `|`, `&`, `(`, `)`, `{`, `}` and a backtick. A glued `>x.log` stays in
  the word.
- **The lint splits on four separators.** `check-spec-tokens.py#SIMPLE_COMMAND_SPLIT` is `&&`,
  `;`, `|` and `(`, and `check_bar` compares whitespace words with their quotes on.
- **Both readers were probed on staged legs.** The table of "The spelling table" was fed to the
  hook's exports and to `check_bar`, with nothing run. The hook read 13 of its rows against the
  expected column (PINNED, 2026-11-14, at `f2680896`), and `check_bar` read 13 of its rows against
  it (PINNED, 2026-11-14, at `f2680896`).
- **The rule below was prototyped.** A patched copy of each reader, kept in the session scratchpad
  and outside the repository, read every row as its expected column says (PINNED, 2026-11-14).
  The copies are not the build: the builder writes the rule from this section.
- **The two fail-open arms cannot tell their branch from the outer catch.** `gate-guard.js#main`
  wraps `checkCommand` in a catch that exits 0, and `readSuiteLegs` runs inside `checkCommand`.
- **`main` derives the set and no arm reads it.** `check-spec-tokens.py#main` passes
  `derive_flag_suites(rows)` to three `check_bar` call sites. No scratch manifest a command-line
  arm writes carries a `ceiling`.
- **Check 8 states a cause it did not test.** `tools/check-template-size.sh@006622b6:352` prints
  the clause whenever the captured answer has a second line, with no test of `SOURCE`.
  `budgets.py resolve` answers a per-key refusal with source `default`.

### The one rule

Both readers hold this rule, each in its own words and sharing no code. A leg is the manifest row's
argv from its script word on, as `readSuiteLegs` and `derive_flag_suites` already return it. `at`
is the place of the leg's first `DIRECT_CHECK_WORDS` member.

A simple command spells a leg when one of its words is a script word and the candidate, that word
and every word after it, holds all three rules. Every script word is tried in order.

1. **The script word.** The word is folded: `\` to `/`, lower case, leading `./` segments taken
   off. A folded word that is not empty is a script word when it equals the leg's script lower-cased,
   ends with `/` and that script, or is itself a trailing path of that script after a `/`.
2. **Length and reach.** The candidate has no more words than the leg, and it reaches `at`. Each
   word up to and including `at` equals the leg's word at that place.
3. **The words after `at`.** Each equals the leg's word at that place, with one latitude: where the
   leg's word does not open with `-` and the leg's word before it does, the candidate's word may be
   any word. That place is an option's value.

Rule 3 is the stricter of the two forms the review records for item M2, and it is the one both of
the skeptic's judgements hold under. The looser form reads any option after `at` as a hit, which
denies `--fixture --list`; the judgement on finding 9 calls that unsound against the hook's own <!-- PINNED 2026-11-14 -->
header. Under rule 3 a changed directory is a hit, a case word is a miss by the option name, and a
case word after the full argv is a miss by length.

Redirection words are taken out before the compare in both readers, as today.

### The hook

**The candidate.** `scanDenyHits` pushes `{ words }` for a simple command when `candidates` is
passed, the resolved head carries no D2 to D4 row, and `words` holds a `DIRECT_CHECK_WORDS`
member. `words` is every word of the simple command, the launcher words included, with redirection
words taken out as today. The push no longer waits on a resolved head: a segment the grammar left
with no head, behind `python -m` say, is a candidate too. The field `head` goes, because no reader
is left for it.

**The match.** `checkSuiteLeg(candidate, legs)` applies the one rule to `candidate.words` and
returns the first leg that holds, or null. A leg whose argv carries no direct-check word never
matches, as today.

**The deny.** The hit's token names the leg's script as the manifest spells it, then the leg's
name and ceiling in the form the row prints today.

**The word break.** `readTokenAt` ends a word before an unquoted `>` or `<` when the word read so
far is not empty, is not all digits, and is not inside `${ }`. An operator that opens a word, bare
or behind a file-descriptor digit, is read as today, so `REDIRECT_RE` still drops it and its glued
target. The reader is shared, so rows D2 to D4 gain the break too: `bash <suite>.test.sh>x.log`
has `<suite>.test.sh` as its head and is a row D4 hit. At `f2680896` that command is no hit
(PINNED, 2026-11-14).

The word-break probe, the argument of `node -p` from the worktree's toplevel:

```js
const g = require('./tools/unattended/gate-guard.js'), c = 'bash x/y.test.sh>x.log'
g.scanDenyHits(c, g.buildCommandView(c), 0, 'Bash').map((h) => h.row).join()
```

The fail-open probe. The pass builds the scratch fixture TOOL-aClearedLedger-3's section 4 calls <!-- PINNED 2026-11-14 -->
`<F>`, copies the hook to `<F>/kit/gate-guard.js`, and feeds that copy with `node` a `Bash`
payload whose `cwd` is `<F>` and whose command is the line below. The copy reads its manifest at
`<F>/gate-legs.json`.

```
bash x/run-selftests.sh; python t/over.py --selftest
```

**The order in `checkCommand`** is unchanged: the manifest is read once, after a live run is found.

### The lint

`SIMPLE_COMMAND_SPLIT` becomes the hook's separator set: `;`, `|`, `(`, `)`, `{`, `}`, a
backtick, a newline, and an `&` that neither follows nor precedes a `>`. The two exclusions keep
`2>&1` and `&>` whole. `check_bar` then reads each simple command's words in this order.

1. Every `'` and `"` character is taken out of the word. A word left empty is skipped.
2. A word that `REDIRECTION` matches at its start is a redirection: it is skipped, and so is the
   next word when the operator stood bare.
3. Any other word is cut at its first `>` or `<`.
4. The one rule runs over the words that are left, for each member of `flag_suites`.

Taking every quote character out, and not one balanced layer, is what makes the body of
`bash -c "<script> --selftest"` read as the hook's row D5 reads it. Two cautions from the review's
merged finding 4 bind the builder. A bare `&` must split and never survive as a word. A quote
character must never be a separator, or a quoted script path and its flag fall into two commands.

`BAR`, `derive_flag_suites`, the hit clause and the three call sites in `main` stay as they are.

### The spelling table

One table, two expected columns. The legs are staged, so no ceiling re-derivation moves a row. Each
row is `[id, command, hook, lint]`. The fence is the JSON file both probes read.

```json
[
["R1", "python t/over.py --selftest", "hit", "hit"],
["R2", "\"$PY\" t/over.py --selftest", "hit", "hit"],
["R3", "python.exe t/over.py --selftest", "hit", "hit"],
["R4", "python3 -u -B t/over.py --selftest", "hit", "hit"],
["R5", "if python t/over.py --selftest; then :; fi", "hit", "hit"],
["R6", "/usr/bin/python3 t/over.py --selftest", "hit", "hit"],
["R7", "cd t && python over.py --selftest", "hit", "hit"],
["R8", "python ./over.py --selftest", "hit", "hit"],
["R9", "python T\\Over.py --selftest", "hit", "hit"],
["R10", "python t/over.py --selftest>x.log", "hit", "hit"],
["R11", "python t/over.py --selftest > x.log 2>&1", "hit", "hit"],
["R12", "python t/over.py --selftest | tail -1", "hit", "hit"],
["R13", "x=$(python t/over.py --selftest)", "hit", "hit"],
["R14", "(cd t && python over.py --selftest)", "hit", "hit"],
["R15", "`python t/over.py --selftest`", "hit", "hit"],
["R16", "python t/over.py --selftest & wait", "hit", "hit"],
["R17", "python \"t/over.py\" --selftest", "hit", "hit"],
["R18", "bash -c \"python t/over.py --selftest\"", "hit", "hit"],
["R19", "{ python t/over.py --selftest; }", "hit", "hit"],
["R20", "echo a\npython t/over.py --selftest", "hit", "hit"],
["R21", "python t/cases.py --fixture", "hit", "hit"],
["R22", "python t/cases.py --fixture --strict-from other/", "hit", "hit"],
["R23", "python t/cases.py --fixture one-case", "miss", "miss"],
["R24", "python t/cases.py --fixture --strict-from other/ one-case", "miss", "miss"],
["R25", "python t/cases.py --fixture --list", "miss", "miss"],
["R26", "python t/over.py --selftest --quiet", "miss", "miss"],
["R27", "grep -c selftest t/over.py", "miss", "miss"],
["R28", "python t/over.py", "miss", "miss"],
["R29", "python -m pdb t/over.py --selftest", "hit", "hit"],
["R30", "\"${PY}\" t/over.py --selftest 2>&1 | tee x.log", "hit", "hit"],
["R31", "python t/over.py --selftest 2>x.log", "hit", "hit"],
["R32", "echo t/over.py --selftest", "hit", "hit"],
["R33", "git log --grep 'over.py --selftest'", "miss", "hit"],
["R34", "printf '%s' \"$(python t/over.py --selftest)\"", "hit", "hit"],
["R35", "bash -c 'bash -c \"python t/over.py --selftest\"'", "miss", "hit"]
]
```

Rows R33 and R35 are the two places the columns differ, and both are kept gaps. The hook blanks a
quoted string and opens one `bash -c` body; the lint has no quote state and no depth. In both rows
the lint is the reader that over-reads, so no spelling the hook denies is admitted by the lint.
Row R32 is a gap both readers share: an unquoted mention at an argument position reads as a run.

Probe H, saved by the pass in the session scratchpad and run from the worktree's toplevel as
`node <probe file> <rows file>`:

```js
const fs = require('fs'), path = require('path')
const g = require(path.resolve('tools/unattended/gate-guard.js'))
const legs = [
  { name: 'over', ceiling: 301, words: ['t/over.py', '--selftest'] },
  { name: 'cases', ceiling: 301, words: ['t/cases.py', '--fixture', '--strict-from', 'x/'] },
]
let bad = 0
for (const [id, cmd, want] of JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))) {
  const cand = []
  g.scanDenyHits(cmd, g.buildCommandView(cmd), 0, 'Bash', cand)
  const got = cand.some((c) => g.checkSuiteLeg(c, legs)) ? 'hit' : 'miss'
  if (got !== want) { bad++; console.log(id, 'read', got, 'want', want) }
}
console.log('rows wrong:', bad)
```

Probe C, saved the same way and run as `python <probe file> <rows file>`:

```python
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("cst", "tools/check-spec-tokens.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
staged = m.derive_flag_suites([
    {"name": "over", "chunk": "selftests", "ceiling": 301, "argv": ["python", "{prefix}/t/over.py", "--selftest"]},
    {"name": "cases", "chunk": "selftests", "ceiling": 301,
     "argv": ["python", "{prefix}/t/cases.py", "--fixture", "--strict-from", "x/"]}])
bad = 0
for rid, cmd, _hook, want in json.load(open(sys.argv[1], encoding="utf-8")):
    got = "hit" if m.check_bar(cmd, staged) else "miss"
    if got != want:
        bad += 1; print(rid, "read", got, "want", want)
print("rows wrong:", bad, "· no set:", bool(m.check_bar("python t/over.py --selftest")))
```

### The hook's suite

Every arm below joins the block that opens `TOOL-aClearedLedger-3: a manifest suite in flag form`
and runs through `run_planted`, at `BUILDING`. `$M_FLAG` and `$M_FIX` are that block's own. Arms 1
to 11 and arm 14 sit while the 900 manifest is planted.

| Arm | Command fed | Exit | Item |
|---|---|---|---|
| 1 | `"$PY"` in place of the launcher of `$M_FLAG`, the variable unexpanded | 2 | M1 |
| 2 | `python.exe` in place of the launcher of `$M_FLAG` | 2 | M1 |
| 3 | `python3 -u -B` in place of the launcher of `$M_FLAG` | 2 | M1 |
| 4 | `if $M_FLAG; then :; fi` | 2 | M1 |
| 5 | `/usr/bin/python3` in place of the launcher of `$M_FLAG` | 2 | M1 |
| 6 | `$M_FIX --strict-from other/` | 2 | M2 |
| 7 | `$M_FIX --strict-from other/ one-case` | 0 | M2 |
| 8 | `cd` into the planted kit directory, `&&`, the launcher and the script's file name, `--selftest` | 2 | M3 |
| 9 | the launcher, `./` and the script's file name, `--selftest` | 2 | M3 |
| 10 | `$M_FIX>x.log`, the redirection glued | 2 | M3 |
| 11 | the suite's own `$D4` with `>x.log` glued, through `run` and the hook in place | 2 | M3 |
| 12 | a runner word, `;`, `$M_FLAG`, placed after the manifest is deleted | 2 | M5 |
| 13 | the same command, placed after the manifest is written as `{` | 2 | M5 |
| 14 | `python3 C:\repo\ZZ-KIT\PLANTED_SUITE.py --selftest` | 2 | L1 |

The existing arm `D6 the same leg with a case word -> allow` stays and is the M2 control. Arm 12's
runner word is `bash ${PFX}${RUN_GATES}/run-selftests.sh`, a row D2 hit. Arm 14's payload is built
by `json.dumps` in `run`, so its backslashes reach the hook.

`FLOOR_ASSERTIONS` moves from 196 to 210 (DERIVED: the floor at `f2680896` plus the fourteen arms
of this table), with a `RAISED` comment line in the file's own form.

### The lint's suite

**The staged spellings assertion** keeps its one line of output. Its tuple gains four entries
after the three it holds, and the expected list becomes
`[True, False, False, True, True, True, False]`:

| Entry | Expected | Branch it reaches |
|---|---|---|
| `python t/over.py --selftest > x.log 2>&1` | hit | the redirection skip |
| `python t/over.py --selftest \| tail -1` | hit | the simple-command split |
| `python T\over.py --selftest` | hit | the `\` and case fold |
| `python t/over.py --selftest`, called with no set | no hit | the set is the cause |

The skeptic's caution binds the third entry. The probe is a `python -c` string whose stderr is
merged into its output, and a bare `\o` in a literal prints a SyntaxWarning onto output line 1.
The backslash is written doubled in the source, or the literal is raw.

**Two staged assertions join it**, each one line of output and one `arm ok` or `arm FAIL` line.

| Assertion | Tokens over the staged `over` and `plant` legs | Expected |
|---|---|---|
| the wrapper spellings | rows R2, R7, R8, R10 and R13 to R18 of the table, spelled for the staged `over` leg | every one a hit |
| the option pair | `python t/plant.py fixture --strict y`, then `--other y` in place of `--strict y`, then `--strict x one` | hit, no hit, no hit |

**Two command-line arms** use the `arm` helper over a scratch repository of the kind the block
headed `AC1` of the bar join builds. Its manifest keeps the `real leg` row and gains
`{"name":"slow suite","chunk":"selftests","ceiling":301,"argv":["python","{prefix}/x/slow.py","--selftest"]}`.
The script is tracked there, so no other join reds. The acceptance bullet of a spec dated after the
conf's `SPEC_DIRECT_CUTOFF` backticks the launcher, the script under the suite's prefix and
`--selftest`.

| Arm | Ceiling in the row | Expected |
|---|---|---|
| above the bound | 301 | exit 1, and the output carries ``this spells the manifest leg `slow suite`, a suite by its declared ceiling of 301 s`` |
| at the bound | 300 | exit 0, and the output carries no `[bar]` |

`FLOOR_ASSERTIONS` moves from 248 to 252 (DERIVED: the floor at `f2680896` plus the two staged
assertions and the two command-line arms), with a comment line in the file's own form.

### Check 8's clause

The line `The cap is the handed-in default because the policy reader refused:` becomes
`The policy reader refused:`. Nothing else in the `fail 8` call moves, so the refusal is still
printed once and the exit is untouched. The review records why the other cure was set aside: a
guard on `SOURCE = constant` would withhold the refusal on the per-key path, where check 2 never
runs to carry it. Before the edit the builder runs `git grep -n "handed-in default because"` and
confirms no reader pins the old clause.

### The manifest stamp

`tools/check-template-size.sh` is on the `watch:` line of `memory/guides/SESSION-KICKOFF.md`, so
the staged leg of `skills/session-kickoff/manifest-check.sh` refuses the unit's commit without a
moved `last-audit` line. The builder follows the stamp rule of
`skills/session-kickoff/SKILL.md`, as TOOL-aClearedLedger-7 S5 did. The section B lines naming the
file are re-read, the `last-audit` line alone is rewritten with the present datetime and
`git rev-parse HEAD`, and the commit message carries the `manifest-audit:` delta line.

### The texts

The header comment's row D6 paragraph and the README paragraph each state the rule and these kept
gaps. Both carry the phrase `share a file name`, which AC4 reads.

| Gap kept | Readers |
|---|---|
| two files that share a file name, or a trailing path, read alike | both |
| an unquoted mention of a script and its direct-check word at an argument position reads as a run | both |
| a path assembled at run time, a module name after `-m` with no path, and a python heredoc | both |
| a spelling whose option name differs from the leg's is read as scoped, whatever the script does with it | both |
| a suite the manifest does not declare, or declares in another chunk; the manifest is read uncommitted | both |
| a quoted mention, and a `bash -c` body inside another, are hits in the lint and not in the hook | lint |

The docstring of `check_bar` says the last row of itself. The comment above `SIMPLE_COMMAND_SPLIT`
stops presenting the split as narrower than the hook's.

### What this corrects in the frozen specs

The specs of units 3, 5 and 7 are CLOSED and keep their text. Where they and this spec differ,
this spec is the rule.

| Frozen statement | Correction |
|---|---|
| TOOL-aClearedLedger-3, "Row D6", rule 1: the candidate's head names the script | any word of the simple command may, by the one rule's rule 1 |
| TOOL-aClearedLedger-3, rule 2, and TOOL-aClearedLedger-5, rule 2: each later word equals the leg's | an option's value may differ, by the one rule's rule 3 |
| TOOL-aClearedLedger-3, "What it does not check": an extra option is a scoped variant | still a miss; a changed option value is a hit |
| TOOL-aClearedLedger-5, "What it does not check": a bare file name, and a leg behind a variable | both are read; a variable in the script's own path is still unread |
| TOOL-aClearedLedger-5, section 4: a simple command lies between four separators | the hook's separator set |
| TOOL-aClearedLedger-7, S3: the clause says the cap is the handed-in default | the clause says the reader refused, for every source |

### What it does not check

- That the two suites' staged rows stay equal to each other. Ask TOOL-aDeferredBar-20 owns that.
- The real manifest's legs through either probe. The legs are staged, and the parity arm of each
  suite still grades the real population in its plain argv form.
- A PowerShell-only spelling of any row. Probe H feeds every row as a `Bash` payload.
- An unquoted `>` or `<` that is no redirection, a comparison in a PowerShell expression say. The
  word ends there too.
- Check 8's wording under a refusal beyond the two greps of AC6.
- That the stamp's datetime advanced. AC7 reads the staged sha alone.

### Inventory

This unit mints no identifier. `SIMPLE_COMMAND_SPLIT`, `checkSuiteLeg`, `readTokenAt` and
`check_bar` keep their names, and the candidate object loses its `head` field.

### Migration

None. No stored shape moves, and an install with no manifest above the kit keeps rows D1 to D5.

### Rollout

No switch. The hook binds only where it binds today, before `VERIFYING` on a branch with a run
record. The lint grades only a live spec dated at or after `SPEC_DIRECT_CUTOFF`.

### Files touched (estimate)

- `tools/unattended/gate-guard.js`
- `tools/unattended/gate-guard.test.sh`
- `tools/unattended/README.md`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/check-template-size.sh`
- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **Any option after the direct-check word is a hit**, the looser form of item M2. It denies a
  read-only verb after `--fixture`, which the judgement on finding 9 refuses.
- **Searching later words only when the head is no path**, finding 5's proposal. A path-shaped
  interpreter still becomes the head. The review judged it instance-only.
- **Resolving the word against the payload's working directory**, finding 2's proposal. A `cd`
  inside the command leaves that directory at the repository root. The review judged it
  instance-only.
- **Stripping one balanced layer of quotes**, finding 3's proposal. Both `bash -c` forms still
  miss. The review judged it instance-only.
- **Splitting on quote characters.** A quoted script path and its flag never share a candidate.
- **Guarding check 8's clause on `SOURCE = constant`.** It withholds the refusal on the path the
  finding names.
- **One shared spelling file now.** It is a new artifact with an owner, ask TOOL-aDeferredBar-20,
  and a batch of review fixes is not where a second mechanism lands.

## 5. Production-readiness checklist

- security — N/A — a hygiene rule that fails open and a spec lint, as each states of itself. The
  change widens what is refused and adds no read, write or grant.
- perf / scale — a command with no direct-check word still costs one scan and no file read, which
  AC3 observes. The match is a loop over the candidate's words and the manifest's over-bound legs.
- error / empty / loading states — an absent, unparsable or non-list manifest still answers the
  empty list, and S6 arms it. A word that folds to nothing is no script word.
- observability — the deny names the leg's script, its manifest name and its ceiling. The lint's
  hit clause is unchanged.
- risks — the wider match denies a command that only mentions a script beside its direct-check
  word, unquoted. Section 4 names it as a kept gap in both texts. A file-name match can name the
  wrong file where two kits share one. Each over-bound leg's file name is carried by one tracked
  file alone (PINNED, 2026-11-14, at `f2680896`, from `git ls-files` joined to `derive_flag_suites`).
- testing — AC1 to AC7 are probes a pass runs. The arms of section 7 are the main loop's.
- migration — N/A — no stored shape moves.
- user docs — `tools/unattended/README.md`, S5. No page under `help/` names the hook's rows.

## 6. Acceptance criteria

Probes H and C and the rows file are section 4's. AC8 to AC11 are the main loop's, because a role
agent's pass runs no suite and no manifest leg.

- **AC1** — When probe H runs through `node` against `tools/unattended/gate-guard.js` and the rows
  file, its last line reads `rows wrong: 0`.
  Red when: the candidate is built from the head alone, a later word is compared by equality, a
  file name or a `./` path is no script word, or a word does not end at a glued `>`.
  figure: at `f2680896` the probe prints `rows wrong: 13` (PINNED, 2026-11-14).
- **AC2** — When probe C runs through `python` against `tools/check-spec-tokens.py` and the rows
  file, its last line reads `rows wrong: 0 · no set: False`.
  Red when: the split lacks a member of the hook's separator set, a quote stays on a word, a word
  is not cut at `>`, or rule 3 is an equality.
  figure: at `f2680896` the probe prints `rows wrong: 13` (PINNED, 2026-11-14).
- **AC3** — When the word-break probe of section 4 runs through `node -p` it prints `D4`, and when the candidate probe of TOOL-aClearedLedger-3's section 4 runs
  through `node -e` it still prints `0 0 1`.
  Red when: the word break is absent, which prints an empty line, or every launched script became
  a candidate, which prints `0 1 1`.
- **AC4** — When `grep -c 'share a file name' tools/unattended/README.md` runs it prints 1 or
  more, and `grep -c 'share a file name' tools/unattended/gate-guard.js` prints 1 or more.
  Red when: a text still presents the trailing-path match as one-directional. Both print 0 at
  `f2680896`.
- **AC5** — When the fail-open probe of section 4 feeds its payload to a copy of `gate-guard.js`
  with no `gate-legs.json` above it, the copy exits 2 and its stderr holds `runner:`. It does the
  same with a `gate-legs.json` above it holding `{`.
  Red when: a manifest read that throws reaches the catch in `main`, which exits 0.
- **AC6** — When `grep -c 'The policy reader refused:' tools/check-template-size.sh` runs it
  prints 1, `grep -c 'handed-in default because' tools/check-template-size.sh` prints 0, and
  `grep -c 'fail 8 ' tools/check-template-size.sh` prints 1.
  Red when: the clause still names the handed-in default, or a second `fail 8` branch was added.
- **AC7** — When the unit's files are staged and
  `git diff --cached -U0 -- memory/guides/SESSION-KICKOFF.md | grep -c "^+last-audit: .* @ $(git rev-parse HEAD)\$"`
  runs, it prints 1.
  Red when: the stamp is not staged with the watched file, or its sha is not the commit's parent.
- **AC8** — When `grep -h '^FLOOR_ASSERTIONS=' tools/unattended/gate-guard.test.sh tools/check-spec-tokens.test.sh`
  runs, it prints `FLOOR_ASSERTIONS=210` and `FLOOR_ASSERTIONS=252`.
  Red when: a floor did not follow the arms its suite gained.
  figure: both are DERIVED, the floors at `f2680896` plus fourteen and plus four.
- **AC9** — When the main loop runs the lint's suite the `New arm:` lines of section 7 name, on a
  frozen clone, the output holds no line opening `arm FAIL`, holds an `arm ok` line for each of the
  two command-line arms and the three staged assertions, and ends `PASS (` with a total at or
  above `FLOOR_ASSERTIONS`.
  Red when: `main` stops joining the manifest, or a branch of `check_bar` regresses.
  permission: the main loop's; a role agent's hook refuses a suite.
- **AC10** — When the main loop runs the hook's suite the `New arm:` lines of section 7 name, on a
  frozen clone, the output holds no line opening `FAIL`, holds an `ok` line for each arm of
  section 4's table, and ends `PASS (` with a total at or above `FLOOR_ASSERTIONS`.
  Red when: a spelling of the table walks past row D6, or a throw in the manifest read is caught
  by `main`.
  permission: the main loop's; the suite is withheld and runs through the unattended kit's runner.
- **AC11** — When the main loop runs the leg `spec tokens (a spec's own names resolve)` by its own
  argv over the tree, the output holds no row carrying `[bar]`.
  Red when: a live spec at or after `SPEC_DIRECT_CUTOFF` spells an over-bound leg in a form the
  wider reader now sees.
  permission: the main loop's; the command is a leg's own.

## 7. Gates

The main loop runs both suites at the close and the bar once after the last unit. The hook's
suite is withheld from the manifest. Each arm below is observed RED on its staged break and GREEN
once restored.

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `template size gate selftest` · `charter size` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `lexicon naming predicates`

New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC10 · arms 1 to 5 of section 4's table; the failing case is `checkSuiteLeg` reading the candidate's first word alone · `FLOOR_ASSERTIONS` 196 to 210, DERIVED, shared by every arm of this suite
New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC10 · arms 6 and 7; the failing case is rule 3 written as an equality, which reds arm 6, and rule 2's length test dropped, which reds arm 7 · the same floor move
New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC3 AC10 · arms 8 to 11; the failing case is the fold without the `./` strip and the reverse trailing path, which reds arms 8 and 9, and `readTokenAt` without the redirection break, which reds arms 10 and 11 · the same floor move
New arm: `tools/unattended/gate-guard.test.sh` · covers AC5 AC10 · arms 12 and 13; the failing case is `readSuiteLegs` with its try and catch taken out, so the throw reaches `main` and each arm exits 0 · the same floor move
New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC10 · arm 14; the failing case is the script-word fold without its `\` replace, and again without its lower-casing · the same floor move
New arm: `tools/check-spec-tokens.test.sh` · covers AC2 AC9 · the staged spellings assertion, changed; the failing case is each of the redirection skip, the split and the fold neutered in turn, and each flips one entry · none
New arm: `tools/check-spec-tokens.test.sh` · covers AC2 AC9 · the wrapper spellings assertion; the failing case is `SIMPLE_COMMAND_SPLIT` put back to its four separators · `FLOOR_ASSERTIONS` 248 to 252, DERIVED, shared by every new arm of this suite
New arm: `tools/check-spec-tokens.test.sh` · covers AC2 AC9 · the option pair assertion; the failing case is rule 3 written as an equality · the same floor move
New arm: `tools/check-spec-tokens.test.sh` · covers AC9 · the command-line arm above the bound; the failing case is `main` passing an empty set to `check_bar` · the same floor move
New arm: `tools/check-spec-tokens.test.sh` · covers AC9 · the command-line arm at the bound; the failing case is `derive_flag_suites` admitting a row at the bound · the same floor move

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.

## 10. Reuse audit

The seams are the two readers themselves: `tools/unattended/gate-guard.js#checkSuiteLeg` with the
candidate block of `scanDenyHits` and the word reader `readTokenAt`, and
`tools/check-spec-tokens.py#check_bar` with `SIMPLE_COMMAND_SPLIT`. Every arm joins a block that
exists: `run_planted` and `build_manifest` in the hook's suite, the `arm` helper and the staged
direct-check probe in the lint's. `python tools/codebase-map/reuse_lookup.py "decide whether a
shell command runs a self-test suite the gate manifest declares above a ceiling, in a hook and in
a spec lint"` ranked name-stem neighbours only, `resolve_shell_argv` among them, and named no
shared word reader, so for one tokenizer serving both files no existing seam fits: one reader is
JavaScript in a copy-installed kit and the other is a repository-root python tool.
`tools/hooks/scratch-guard.js#scanCommandHeads` was read for its redirection rule, which the hook
already copies. The recall probe returned the specs of units 3 and 5 and ask TOOL-aDeferredBar-20,
which section 3 hands the shared spelling list to. The hits agreed with source.

Recall terms used: gate-guard check_bar D6 DIRECT_CHECK_BOUND flag-form suite manifest ceiling
parity simple-command redirection launcher scoped-variant
