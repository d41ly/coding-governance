# TOOL-aClearedLedger-16 — the drop test's deny side is armed, an empty quoted pair ends its word at a redirection, and three texts state what the code holds

**Status:** CLOSED · rev-1 · 2026-11-14 · node a · Tier-2 · base 8db6f4be · streams tooling · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aClearedLedger-16-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aClearedLedger-16-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-prompt-TOOL-aClearedLedger-16-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-16-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aClearedLedger-16-brief.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-16-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Round 4 of the closing diff review confirmed one MEDIUM item and three LOW items against the
quoted read TOOL-aClearedLedger-14 built, and the build method batches them into this unit. It arms
the deny side of the drop test in `scanDenyHits`, ends a word holding only an empty quoted pair at
an unquoted `>` or `<` as bash ends it, and corrects one example in two texts and one stated reason
in a lint docstring.

## 2. Scope (IN)

The review is
`memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-14-diff-review-round4.md`.
Each item below names the review item it closes.

- **S1** — Item M1. `tools/unattended/gate-guard.test.sh` gains the deny arms of section 4, "The
  arms": the leg with a double-quoted target glued to `>`, and the same glued to `2>`. Observed by
  AC3 and AC4.
- **S2** — Item M1. `FLOOR_ASSERTIONS` of that suite rises by the row count of the arm table from
  the value TOOL-aClearedLedger-15 leaves, with a `RAISED` comment line in the file's own form.
  Observed by AC5.
- **S3** — Item L1. The read-on branch of `readTokenAt` in `tools/unattended/gate-guard.js` loses
  its clause `out !== '' &&`, so a word whose quoting is empty ends at an unquoted `>` or `<` as
  every word holding quoting does (section 4, "The empty pair"). Observed by AC1 and AC2.
- **S4** — Item L1. The docstring of `readTokenAt` and the comment in the changed branch say an
  empty pair is included. NOT OBSERVED: no probe tells a true comment from a stale one, and the
  closing review reads them against the code.
- **S5** — Item L2. The header comment of `tools/unattended/gate-guard.js` and the paragraph of
  `tools/unattended/README.md` on row D6 give `'>'>x.log` as the quoted-operator example where they
  now give `'>' x.log` (section 4, "The texts"). Observed by AC6.
- **S6** — Item L3. The docstring of `check_bar` in `tools/check-spec-tokens.py` gives both reasons
  the lint over-reads a quoted operator character, in the record's wording. No code of that file
  changes. Observed by AC7.

## 3. Non-goals (OUT)

- Item H1 of the record, the drop test measured over the unquoted prefix. TOOL-aClearedLedger-15
  builds it, and this unit builds on the loop that unit leaves.
- Any change to the code of `tools/check-spec-tokens.py`, and any change to its suite. The
  docstring of `check_bar` is the only edit there.
- The record's left-shift lines: the `harness arms` leg extended so a spec row confirmed only by a
  build-time probe names its arm (M1); a token-level arm for `"">x.log` (L1); the checklist class
  that makes a prose example name its arm (L2); a spec-tokens self-test arm per spelling naming the
  lint stage that over-reads it (L3). Each is a gate or arm of its own, outside the brief's items.
- An arm for the empty pair. Its D6 verdict is a miss before and after S3, so no `run_planted` arm
  can tell the two reads apart; section 4, "What it does not check", names what goes unarmed.
- Any other sentence of `tools/unattended/README.md` or of the hook's header comment.
- Any edit to a CLOSED spec or a sibling spec, a lowered floor, a waived arm, any index render,
  and any kit version, which the lander's `mint` moves.

### Edges

- **consumes-from** `TOOL-aClearedLedger-15` — the candidate loop of `scanDenyHits` that unit
  leaves, whose keep-as-word test is `!redir` over the unquoted prefix, which this unit's failing
  case weakens; its arms, after which this unit's arms sit; and the floor it leaves, from which
  this unit derives its own move. Without it the failing case of section 7 names a predicate that
  is not in the file.
- **consumes-from** external — the quoted fact `quotedAt` and the read-on branch of `readTokenAt`
  that TOOL-aClearedLedger-14 built, the two texts and the docstring it extended, and its rows
  file, which AC3 re-reads. That unit is CLOSED, so the edge is prose and not a join.
- **hands-off** external — the record's four left-shift lines, each a gate or arm of its own.

## 4. Design

### Evidence

Read at `998b627a`, the branch tip. The blobs are `tools/unattended/gate-guard.js@07723a18`,
`tools/unattended/gate-guard.test.sh@8d3a1720`, `tools/unattended/README.md@0d61b8b1`,
`tools/check-spec-tokens.py@40b55ac9` and
`memory/builds/aClearedLedger/spec/2026-11-14-spec-TOOL-aClearedLedger-14.md@d68ef567`.

- **No arm feeds the deny side of the drop test.** The arms of the 900 block at
  `tools/unattended/gate-guard.test.sh@8d3a1720:784-825` quote a redirection target only spaced,
  `>> "$LOG"`, where the bare-operator step skips it without reading `q`. A scratch copy of the
  hook with its keep-as-word test weakened to `!redir || q >= 0` read `>"x.log"` and `2>"x.log"`
  as a miss, rows V1 and V2 of "The probe", and the same weakening over a scratch copy holding the
  drop of TOOL-aClearedLedger-15 read them as a miss too (PINNED, 2026-11-14). The unweakened
  copies read both as a hit.
- **The arms of TOOL-aClearedLedger-15 red under the same weakening.** `>'>x.log'` and
  `2>'>x.log'` also open their quote after a complete operator, and the weakened copy read them as
  a miss (PINNED, 2026-11-14). That spec's "What it does not check" says no arm reds there; once
  its arms land, theirs do too. This unit's arms still own the plain spelling the record names.
- **The empty pair reads on.** The branch at `tools/unattended/gate-guard.js@07723a18:408` tests
  `out !== ''` first, and after `""` the word so far is empty, so in `"">x.log` the `>` is read
  into the word: one token `>x.log` with `quotedAt` 0.
- **The clause adds nothing once quoting is tested.** `^\d*[<>]*$` matches the empty string, so
  for an unquoted empty word `!/^\d*[<>]*$/.test(out)` is already false. Deleting `out !== '' &&`
  changes the condition only where the word is empty and holds quoting, which is the record's
  form `(out !== '' || quotedAt >= 0)` exactly. A scratch copy holding the deletion and one
  holding the record's form printed identical probe output (PINNED, 2026-11-14).
- **No zero-length token follows.** A word holding quoting has moved the reader past its quote
  characters, so the token's end is past its start and the stop in `scanSegments` on
  `t.end <= at` is not reached. The probe's token line continues past each pair.
- **Bash reads the empty pair as an argument.** TOOL-aClearedLedger-14 pinned that any quoting, an
  empty pair included, stops a word being an operator. `bash "">x.test.sh` therefore runs no
  script: the suite name is the redirection target.
- **One row D4 verdict moves.** The reader is shared, so `bash "">x.test.sh` and
  `bash ''>k/a.test.sh` move from a D4 deny to no row, and `bash k/a.test.sh "">x.log` stays D4
  (PINNED, 2026-11-14, on the scratch copy). Every row of the rows files of TOOL-aClearedLedger-12,
  TOOL-aClearedLedger-13 and TOOL-aClearedLedger-14 reads as its expected column says, with and
  without S3 (PINNED, 2026-11-14). No line of the suite at `8d3a1720` glues an empty pair before
  a `>` or `<` (PINNED, 2026-11-14).
- **The two texts give a spaced argument as the example.** The header comment at
  `tools/unattended/gate-guard.js@07723a18:68` and `tools/unattended/README.md@0d61b8b1:129` give
  `'>' x.log`, a quoted `>` argument and then a plain one, which holds no redirection. The example
  `'>'>x.log` is pinned by the allow arm at `tools/unattended/gate-guard.test.sh@8d3a1720:825`.
- **The docstring names one reason for two spellings.** The clause at
  `tools/check-spec-tokens.py@40b55ac9:531` says the lint reads the word with its quotes out.
  `SIMPLE_COMMAND_SPLIT` at `tools/check-spec-tokens.py@40b55ac9:479` has no quote state, so
  `--selftest '&'>x.log` splits into two commands before any word is read, and
  `--selftest '>'>x.log` stays one command whose word `>>x.log` is dropped as a redirection. Both
  are hits (PINNED, 2026-11-14, by the docstring probe of section 6).

### The arms

Both arms join the 900 block after the last `run_planted` line of the arms TOOL-aClearedLedger-15
adds, which follow the block that opens `TOOL-aClearedLedger-14, review item L2`, and before
`F=$(build_fixture VERIFYING)`. A comment line naming this unit and review round 4's item M1 sits
above them: a quote opening after a complete operator leaves a glued redirection, so the target is
dropped and the words are the leg's. Each runs through `run_planted` against `"$B"` and expects
exit 2.

| Arm | Name | Command fed |
|---|---|---|
| 1 | `D6 the leg with a quoted target glued to > -> deny` | `"$M_FLAG >\"x.log\""` |
| 2 | `D6 the leg with a quoted target glued to 2> -> deny` | `"$M_FLAG 2>\"x.log\""` |

Each command is double-quoted in the suite with its inner quotes escaped, so `>"x.log"` reaches the
payload as typed. Arm 2 is row U8 of TOOL-aClearedLedger-14, and arm 1 its single-operator form.

`FLOOR_ASSERTIONS` rises by the row count of this table from the value the file holds when the
builder opens it, the floor TOOL-aClearedLedger-15 leaves (DERIVED). A comment line
`RAISED <found> -> <found plus the row count> at TOOL-aClearedLedger-16` sits above the line for
TOOL-aClearedLedger-15, in the file's own form, and names both arms.

### The empty pair

```js
// readTokenAt, the read-on branch: the clause `out !== '' &&` is deleted
} else if ((ch === '>' || ch === '<') && !brace && (quotedAt >= 0 || !/^\d*[<>]*$/.test(out))) {
```

A word holding quoting ends at an unquoted `>` or `<`, an empty pair included, and an unquoted
word reads on while it is descriptor digits and operator characters, the empty word included. So
`"">x.log` is an empty quoted word, which `scanSegments` keeps through `t.quotedAt >= 0`, and then
the redirection `>x.log`, which `scanDenyHits` drops.

The docstring sentence of `readTokenAt` "once it holds quoting" reads "once it holds quoting, an
empty pair included". The comment in the branch gains one sentence naming this unit: `"">x.log`
is an empty argument and then a redirection. Nothing else in the file changes for S3.

### The texts

In the header comment of `tools/unattended/gate-guard.js` and in the paragraph of
`tools/unattended/README.md` on row D6, the parenthesis `` (`'&'>x.log`, `'>' x.log`) `` becomes
`` (`'&'>x.log`, `'>'>x.log`) ``. The two examples have the same length, so neither line rewraps.

The clause of the `check_bar` docstring that opens "a quoted operator character before a
redirection" and ends before "and a `bash -c` body inside another" is replaced, so the docstring's
last four lines read as below. The wrap is part of the text: AC7 greps two phrases, each on one
line.

```text
    a glued variable prefix (`${DIR}<script>`, which splits here at the braces); a quoted mention;
    a quoted operator character before a redirection, which the hook keeps as an argument: a
    quoted `&` splits the command here because the split pattern has no quote state, and a quoted
    `>` is read with its quotes out and dropped as a redirection; and a `bash -c` body inside
    another."""
```

### The probe

The rows file. Each row is `[id, command, hook]`, the shape of TOOL-aClearedLedger-14's, and the
legs are staged, so no ceiling re-derivation moves a row.

```json
[
["V1", "python t/over.py --selftest >\"x.log\"", "hit"],
["V2", "python t/over.py --selftest 2>\"x.log\"", "hit"],
["V3", "python t/over.py --selftest \"\">x.log", "miss"],
["V4", "python t/over.py --selftest ''<in", "miss"],
["V5", "python t/over.py --selftest \"\" >x.log", "miss"],
["V6", "python t/over.py --selftest >x.log", "hit"]
]
```

Rows V1 and V2 are the arms' spellings. Rows V3 and V4 glue an empty pair before an operator, a
miss before and after S3. Row V5 is the spaced control and row V6 the unquoted one.

The probe, saved by the pass in the session scratchpad and run from the worktree's toplevel as
`node <probe file> <rows file>`. Its first two lines read the token stream of one command, its
third the D2 to D4 rows of three, and it reads the rows files of TOOL-aClearedLedger-12,
TOOL-aClearedLedger-13 and TOOL-aClearedLedger-14 unchanged: a four-column row gives its hook column
as the third element.

```js
const fs = require('fs'), path = require('path')
const g = require(path.resolve('tools/unattended/gate-guard.js'))
const legs = [
  { name: 'over', ceiling: 301, words: ['t/over.py', '--selftest'] },
  { name: 'cases', ceiling: 301, words: ['t/cases.py', '--fixture', '--strict-from', 'x/'] },
]
const s = `a "">x b ''<y c "" >z d ''2>w`
const t = g.scanSegments(s, g.buildCommandView(s))[0]
console.log(t.join())
console.log(t.quotedAt.join())
const rows = (c) => g.scanDenyHits(c, g.buildCommandView(c), 0, 'Bash').map((h) => h.row).join('+') || '-'
console.log(['bash "">x.test.sh', `bash ''>k/a.test.sh`, 'bash k/a.test.sh "">x.log'].map(rows).join(' '))
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

The spec of TOOL-aClearedLedger-14 is CLOSED and keeps its text, at blob `d68ef567`. Where it and
this spec differ, this spec is the rule.

| Frozen statement | Correction |
|---|---|
| "The quoted fact": the read-on branch tests `out !== ''` first | the clause is gone, by "The empty pair" |
| "What it does not check": `''>x.log` reads on, and the candidate keeps `>x.log` | the word ends at the `>`, and the candidate keeps an empty word, as bash passes one |
| "What it does not check" leaves out rows U8 to U10, a quote opening after the operator | arms 1 and 2 here feed U8 and its single-operator form; U9 and U10 stay unarmed, by "What it does not check" here |
| "The texts", the example `'>' x.log` | the example `'>'>x.log`, by "The texts" here |
| "The texts", the reason the `check_bar` docstring gives | both reasons, by "The texts" here |

### What it does not check

- No arm feeds an empty pair glued before an operator, rows V3 and V4. Their D6 verdict is a miss
  before and after S3. The D4 verdict that moves, `bash "">x.test.sh`, is fed by no arm. AC1 and
  AC2 read both once, at build time, and no gate re-reads them.
- No arm feeds a glued `>>` with a quoted target or a quoted target holding a space, rows U9 and
  U10 of TOOL-aClearedLedger-14. AC3 reads them once, through that spec's rows file.
- The arms are not the only arms the weakening reds. The arms of TOOL-aClearedLedger-15 red under
  it too ("Evidence"), so the RED observation shows each arm can fail, not that it alone guards
  the deny side.
- That the docstring's two reasons stay true. The docstring probe reads the split and the hit at
  build time; no suite arm names the lint stage that over-reads each spelling.
- That the texts say what the code does. AC6 and AC7 grep the phrases; the closing review reads
  each sentence against the code.
- A PowerShell-only spelling. The probe feeds every row as a `Bash` payload.
- The real manifest's legs. The probe's legs are staged, and the arms read the planted manifest.

### Inventory

This unit mints no identifier. `readTokenAt`, `scanSegments`, `scanDenyHits`, `quotedAt` and
`check_bar` keep their names and signatures.

### Migration

None. No stored shape moves.

### Rollout

No switch. The hook binds where it binds today, before `VERIFYING` on a branch with a run record.
One verdict class moves: a row D4 deny becomes no row where an empty quoted pair is glued before a
redirection whose target is the suite word, a command in which bash runs no suite. Every D6
verdict holds.

### Files touched (estimate)

- `tools/unattended/gate-guard.js`
- `tools/unattended/gate-guard.test.sh`
- `tools/unattended/README.md`
- `tools/check-spec-tokens.py`

### Alternatives rejected

- **The record's form `(out !== '' || quotedAt >= 0)`.** It is the same condition, since the
  operator pattern matches the empty word ("Evidence"), and it keeps a clause that decides nothing.
- **Narrowing the comment instead**, the record's second form for L1. Brief item 2 asks for the
  first, and bash reads the pair as an argument.
- **An arm through `run_planted` for the empty pair.** Its D6 verdict does not move, so the arm
  could not red on the read it is meant to guard.
- **Describing `'>' x.log` separately as a quoted argument**, the record's second form for L2.
  Brief item 3 asks for the example the allow arm pins.
- **The record's arm text `"$M_FLAG"' >"x.log"'`.** It feeds the same bytes, and one double-quoted
  string per command is the form the neighbouring arms use, which AC4 greps whole.

## 5. Production-readiness checklist

- security — N/A — a hygiene rule that fails open, as the hook's header states of itself. S3 turns
  a D4 deny into no row only where the suite word is a redirection target and bash runs no suite.
  S1 adds deny arms. No read, write or grant is added.
- perf / scale — one comparison fewer per glued operator in `readTokenAt`.
- error / empty / loading states — a word holding only an empty quoted pair is kept, as today,
  and now ends at a glued operator. An unquoted word opening with an operator reads on, as today.
- observability — the deny text is unchanged and names the leg, as today.
- risks — the empty pair and the D4 verdict that moves are read by no arm ("What it does not
  check").
- testing — AC1 to AC7 are probes a pass runs. The arms of section 7 are the main loop's.
- migration — N/A — no stored shape moves.
- user docs — `tools/unattended/README.md`, S5. No page under `help/` names the hook's rows.

## 6. Acceptance criteria

The probe and the rows file are section 4's. The older rows files are the JSON blocks of the specs
of TOOL-aClearedLedger-12, TOOL-aClearedLedger-13 and TOOL-aClearedLedger-14, each saved as its own
file. Every probe runs from the worktree's toplevel, before the unit's commit.

- **AC1** — When the probe of "The probe" runs through `node`, its first line reads
  `a,,>x,b,,<y,c,,>z,d,2,>w` and its second reads `-1,0,-1,-1,0,-1,-1,0,-1,-1,0,-1`.
  Red when: the clause `out !== ''` still gates the branch, which prints `a,>x,b,<y,c,,>z,d,2,>w`
  and `-1,0,-1,0,-1,0,-1,-1,0,-1`.
  figure: the red lines are what the hook at `998b627a` prints (PINNED, 2026-11-14).
- **AC2** — When the same probe runs through `node`, its third line reads `- - D4`.
  Red when: the empty pair still reads on, which prints `D4 D4 D4`.
  figure: `D4 D4 D4` at `998b627a` (PINNED, 2026-11-14).
- **AC3** — When the probe runs through `node` against `tools/unattended/gate-guard.js` and this
  spec's rows file, its last line reads `rows wrong: 0`, and it reads the same over each older rows
  file.
  Red when: the keep-as-word test keeps any word holding quoting, which names rows V1 and V2 here
  and rows U8 to U10 of TOOL-aClearedLedger-14.
  figure: under that weakening a scratch copy printed `rows wrong: 2` here and `rows wrong: 3` over
  the rows file of TOOL-aClearedLedger-14 (PINNED, 2026-11-14).
- **AC4** — When
  `grep -cE '^run_planted "D6 the leg with a quoted target glued to 2?> -> deny" +2 "\$B" "\$M_FLAG 2?>\\"x\.log\\""$' tools/unattended/gate-guard.test.sh`
  runs, it prints 2.
  Red when: an arm of section 4's arm table is absent, expects another exit, feeds another
  command, or runs outside `run_planted`.
  figure: 2 is DERIVED, the row count of that table; at `8d3a1720` the command prints 0 (PINNED,
  2026-11-14).
- **AC5** — When the floor probe below runs through `bash`, it prints `rise: 2` and then `1`.
  Red when: the floor did not follow the arms, which prints `rise: 0` and `0`.
  figure: 2 is DERIVED, the count AC4 prints; the floor it rises from is whatever `HEAD` holds.
- **AC6** — When `grep -cF "'>' x.log" tools/unattended/gate-guard.js tools/unattended/README.md`
  runs it prints 0 for each file, and when
  `grep -c "'&'>x.log., .'>'>x.log" tools/unattended/gate-guard.js tools/unattended/README.md` runs
  it prints 1 for each file.
  Red when: either text still gives the spaced example.
  figure: at `998b627a` the commands print 1 for each file and 0 for each file (PINNED,
  2026-11-14).
- **AC7** — When
  `grep -c "splits the command here because the split pattern has no" tools/check-spec-tokens.py`
  runs it prints 1, and
  `grep -c "which this reader reads with its quotes out" tools/check-spec-tokens.py` prints 0. And
  the docstring probe below, run through `python`, prints `'&'>x.log commands: 2 hit: True` and then
  `'>'>x.log commands: 1 hit: True`, and the code probe below prints `code unchanged: True`.
  Red when: the docstring keeps the single reason, the split gains quote state so the first reason
  goes false, or any change reaches the syntax tree outside the docstring of `check_bar`.
  figure: at `998b627a` the greps print 0 and 1 and the docstring probe prints both lines (PINNED,
  2026-11-14). The code probe is TOOL-aClearedLedger-14's, whose True and False cases it pinned.

The floor probe.

```bash
f=tools/unattended/gate-guard.test.sh
a=$(git show HEAD:$f | sed -n 's/^FLOOR_ASSERTIONS=//p')
b=$(sed -n 's/^FLOOR_ASSERTIONS=//p' $f)
echo "rise: $((b - a))"
grep -c "^# RAISED $a -> $b at TOOL-aClearedLedger-16" $f
```

The docstring probe. It loads the lint by path and feeds both spellings with one staged leg.

```python
import importlib.util
spec = importlib.util.spec_from_file_location("cst", "tools/check-spec-tokens.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
legs = [("over", 301, ("t/over.py", "--selftest"))]
for tail in ("'&'>x.log", "'>'>x.log"):
    cmd = "python3 t/over.py --selftest " + tail
    print(tail, "commands:", len(m.SIMPLE_COMMAND_SPLIT.split(cmd)), "hit:", m.check_bar(cmd, legs) is not None)
```

The code probe. It parses the file at `HEAD` and in the worktree, blanks the docstring of
`check_bar` in both, and compares the trees, which carry no line numbers or comments.

```python
import ast, subprocess as s
f = "tools/check-spec-tokens.py"
a = [ast.parse(t) for t in (s.check_output(["git", "show", "HEAD:" + f], encoding="utf-8"),
                            open(f, encoding="utf-8").read())]
for t in a:
    for n in ast.walk(t):
        if isinstance(n, ast.FunctionDef) and n.name == "check_bar":
            n.body[0].value.value = ""
print("code unchanged:", ast.dump(a[0]) == ast.dump(a[1]))
```

## 7. Gates

`tools/gate-legs.json` names the hook's suite nowhere (PINNED, 2026-11-14, at `998b627a`), and the
hook denies that suite at BUILDING. The main loop runs it at the close, on a frozen clone, and the
bar once after the last unit. Before the suite's green run the main loop observes each arm below
RED on the failing case its line names, with the arms in place, and GREEN once the case is
restored. A green run prints an `ok` line for each arm of section 4's arm table, no line opening
`FAIL`, and a total at or above `FLOOR_ASSERTIONS`. The main loop also runs every leg on the line
below at the close. The docstring of `check_bar` trips the exact guard
`{prefix}/check-spec-tokens.py`, and the spec-token suite reads that file. No arm is added for S3
or the texts: AC1, AC2, AC6 and AC7 read them.

`spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `spec-tokens self-test`

New arm: `tools/unattended/gate-guard.test.sh` · covers AC3 AC4 · arm 1, `>"x.log"`; the failing case is the keep-as-word test of the candidate loop in `scanDenyHits`, `!redir` as TOOL-aClearedLedger-15 leaves it, weakened to `!redir || q >= 0`, so the glued target is kept as the word `>x.log` and the arm exits 0 where it expects 2 · `FLOOR_ASSERTIONS` by the arm table's row count, DERIVED from the floor TOOL-aClearedLedger-15 leaves, shared by both arms
New arm: `tools/unattended/gate-guard.test.sh` · covers AC3 AC4 · arm 2, `2>"x.log"`; the same weakening, which keeps `2>x.log` as a word, so the arm exits 0 · the same floor move

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.

## 10. Reuse audit

The seams are the read-on branch of `tools/unattended/gate-guard.js#readTokenAt`, which loses one
clause, and the planted block of `tools/unattended/gate-guard.test.sh`, which the arms join through
`run_planted` and `$M_FLAG`. The texts are the lines TOOL-aClearedLedger-14 wrote. `python
tools/codebase-map/reuse_lookup.py "end a shell word holding an empty quoted pair at a glued
redirection operator, and arm the deny side of a redirection drop test"` ranked name-stem
neighbours only, `arm`, `pair` and `run_arms` among them, and named no quote-aware word reader, so
for a shared reader no existing seam fits beyond the branch itself.
`tools/hooks/scratch-guard.js#readTokenAt` returns a bare string with no quote position, as
TOOL-aClearedLedger-14's audit records. The recall query ranked the specs of
TOOL-aClearedLedger-14 and TOOL-aClearedLedger-15 first; both agreed with source.

Recall terms used: gate-guard readTokenAt quotedAt REDIRECT_RE redirection quoted empty pair
run_planted FLOOR_ASSERTIONS check_bar SIMPLE_COMMAND_SPLIT docstring
