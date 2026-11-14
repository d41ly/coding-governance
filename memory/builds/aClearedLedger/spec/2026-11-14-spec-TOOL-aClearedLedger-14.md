# TOOL-aClearedLedger-14 — the gate guard never reads a quoted character as a redirection operator, and the frozen quoted-read regex is restated whole

**Status:** CLOSED · rev-2 · 2026-11-14 · node a · Tier-2 · base 8db6f4be · streams tooling · order 14 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-build-TOOL-aClearedLedger-1-2-observations.md](../build/2026-11-14-build-TOOL-aClearedLedger-1-2-observations.md) | journal | TOOL-aClearedLedger-1 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 TOOL-aClearedLedger-11 TOOL-aClearedLedger-12 TOOL-aClearedLedger-13 TOOL-aClearedLedger-15 TOOL-aClearedLedger-16 |
| [2026-11-14-build-TOOL-aClearedLedger-14-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aClearedLedger-14-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-prompt-TOOL-aClearedLedger-14-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-14-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aClearedLedger-14-brief.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-14-brief.md) | research | — |
| [2026-11-14-review-TOOL-aClearedLedger-14-diff-review-round4.md](../reviews/2026-11-14-review-TOOL-aClearedLedger-14-diff-review-round4.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

Round 3 of the closing diff review found that the gate guard reads a quoted `&` glued before a `>`
as part of a redirection, so it drops an argument bash passes, and that a regex in a frozen spec's
table cell renders split. This unit makes the hook treat any quoted character as an argument, as
bash does, arms the quoted `&` and the quoted `>`, and restates the regex where it renders whole.
The three texts that list where the spec lint reads more than the hook name the difference this
opens.
It is the batch the build method promotes from the review's items L1 and L2.

## 2. Scope (IN)

The review is
`memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-11-12-13-diff-review-round3.md`.
Each item below names the review item it closes.

- **S1** — Item L2. `readTokenAt` of `tools/unattended/gate-guard.js` records `quotedAt`, where the
  word's first quote opened, and reads on past an unquoted `>` or `<` only while the word so far
  holds no quoting and matches `^\d*[<>]*$`. It returns `quotedAt` with the word (section 4, "The
  quoted fact"). Observed by AC1 and AC2.
- **S2** — Item L2. `scanSegments` hands each token list on with a parallel array `quotedAt`, and
  keeps a quoted empty word by that fact in place of its own quote-character test. Observed by AC2.
- **S3** — Item L2. The redirection read in `scanDenyHits` reads a word as a redirection only when
  the operator `REDIRECT_RE` matches ends before the word's quoting opens. Observed by AC1.
- **S4** — Item L2. `tools/unattended/gate-guard.test.sh` gains the two allow arms of section 4,
  "The arms": one quoted `&` and one quoted `>`, each glued before a `>`. Observed by AC3.
- **S5** — Item L2. `FLOOR_ASSERTIONS` of that suite rises by the count of those arms, with a
  `RAISED` comment line in the file's own form. Observed by AC4.
- **S6** — Item L2. The docstrings of `readTokenAt`, `scanSegments` and `scanDenyHits` and the
  comment inside the changed branch say what S1 to S3 make true. NOT OBSERVED: no probe tells a
  true comment from a stale one, and the closing review reads them against the code.
- **S7** — Item L1. Section 4, "What this corrects in the frozen specs", restates the quoted-read
  regex of TOOL-aClearedLedger-13 in a fenced block, as the correction of record, and says why the
  frozen cell renders split. Every table row of this spec splits into its header's cell count.
  Observed by AC5.
- **S8** — Item L2, fork F1. The header comment of `tools/unattended/gate-guard.js`, the paragraph
  of `tools/unattended/README.md` on row D6 and the docstring of `check_bar` in
  `tools/check-spec-tokens.py` each gain the quoted-operator difference in their list of spellings
  the lint reads and the hook does not (section 4, "The texts"). No code of
  `tools/check-spec-tokens.py` changes. Observed by AC6.

## 3. Non-goals (OUT)

- Any change to the code of `tools/check-spec-tokens.py`, and any change to its suite. The brief
  excluded the file whole; the owner's ruling on fork F1 admits the docstring of `check_bar` alone.
- Any edit to a CLOSED spec. The frozen cell of TOOL-aClearedLedger-13 keeps its bytes, and every
  correction to it or to TOOL-aClearedLedger-12 is stated here.
- The review's left-shift line under L2: one arm per quoted operator character, `&`, `>`, `<` and
  a digit, glued before a redirection. The brief asks for two arms. The probe of AC1 reads the
  wider set once, and section 4, "What it does not check", names what no arm feeds.
- The review's left-shift line under L1: a table-shape check in the record lint for every table
  under `memory/`. That is a gate of its own, a separate unit. AC5 runs the same predicate over
  this one spec.
- Any edit to `REDIRECT_RE`. Its `&` alternative names bash's `&>` spelling, and section 4 says why
  no word reaches it once this unit is built.
- Any edit to `checkSuiteLeg`, to the head grammar of `scanDenyHits`, or to
  `tools/hooks/scratch-guard.js`, whose `readTokenAt` is a separate copy returning a bare string.
- Any other sentence of `tools/unattended/README.md` or of the hook's header comment.
- A lowered floor, a waived arm, any index render, and any kit version, which the lander's `mint`
  moves.

### Edges

- **consumes-from** external — the read-on guard in `readTokenAt` that TOOL-aClearedLedger-12
  built and this unit narrows, and that unit's rows file, which AC1 re-reads. Both siblings are
  CLOSED, so each edge is prose and not a join.
- **consumes-from** external — the planted block's last arms that TOOL-aClearedLedger-13 built,
  which this unit's arms follow, the floor it left at `64673441`, and its rows file.
- **hands-off** external — one arm per quoted operator character, and the table-shape gate under
  `memory/`, the two left-shift lines of the review.

## 4. Design

### Evidence

Read at `64673441`, the branch tip. The blobs are `tools/unattended/gate-guard.js@77894998`,
`tools/unattended/gate-guard.test.sh@f5a82b10`, `tools/check-spec-tokens.py@2b28752d` and
`memory/builds/aClearedLedger/spec/2026-11-14-spec-TOOL-aClearedLedger-13.md@b50a3aa9`.

- **The read-on test ignores quoting.** The branch at `tools/unattended/gate-guard.js@77894998:402`
  reads on while the word so far matches the operator prefix, and nothing in `readTokenAt` records
  that a character came from inside quotes. An unquoted `&` ends the word at the break set on the
  line above, so an `&` in the word so far was always quoted.
- **The drop ignores quoting too.** `gate-guard.js#scanDenyHits` runs `REDIRECT_RE` over each bare
  token string. A quoted `>` that ends its word is therefore a bare operator, and the word after it
  is skipped as its target. So curing `readTokenAt` alone leaves the quoted `>` dropped: a scratch
  copy holding only that cure still read `--selftest '>'>x.log` as the leg (PINNED, 2026-11-14).
- **Bash reads every quoted character as an argument.** In the session scratchpad,
  `printf '[%s]' a '&'>x.log` writes `[a][&]` to the file, and the same holds for `'>'`, `'2'` and
  `''2` glued before the `>`. `printf '[%s]' a '>' x.log` prints `[a][>][x.log]`. (PINNED,
  2026-11-14.) Any quoting in a word, an empty pair included, stops it being an operator or a
  descriptor.
- **The position, not the presence, of the quoting decides.** A scratch copy that kept any word
  holding quoting read `--selftest 2>"x.log"` and `>>"$LOG"` as arguments, a miss for a real
  redirection (PINNED, 2026-11-14). The quote there opens after the operator.
- **The `|&` alternative of the read-on test is unreachable once S1 is built.** An unquoted `&`
  breaks the word, and a quoted one sets `quotedAt`, which ends the word before the test is read.
  Dropping the alternative changes no row of the probe (PINNED, 2026-11-14). For the same reason
  the `&` alternative of `REDIRECT_RE` drops no word: a word holding an `&` holds a quoted one,
  whose quoting opens inside the operator, so the drop test of S3 keeps the word.
- **The design was prototyped.** A scratch copy of the hook holding S1 to S3 read every row of this
  spec's rows file, of TOOL-aClearedLedger-12's and of TOOL-aClearedLedger-13's as its expected
  column says (PINNED, 2026-11-14). The copy is outside the repository and is not the build.
- **No arm quotes an operator character.** No `run_planted` line of `gate-guard.test.sh@f5a82b10`
  carries `'&'` or `'>'`.

### The quoted fact

One fact, where the word's first quote opened, is computed once in `readTokenAt` and read in two
places. It is `-1` for a word that holds no quoting.

```js
// readTokenAt
let quotedAt = -1
// ... the branch that opens a quote:
quote = ch
if (quotedAt < 0) quotedAt = out.length
// ... the read-on branch:
} else if ((ch === '>' || ch === '<') && !brace && out !== '' && (quotedAt >= 0 || !/^\d*[<>]*$/.test(out))) {
// ... the return:
return { text: out, end: i, quotedAt }
```

```js
// scanSegments, readSegment
const quotedAt = []
if (t.text !== '' || t.quotedAt >= 0) { toks.push(t.text); quotedAt.push(t.quotedAt) }
while (toks.length && /^(then|do|else)$/.test(toks[0])) { toks.shift(); quotedAt.shift() }
toks.quotedAt = quotedAt
```

```js
// scanDenyHits, the candidate loop
const q = toks.quotedAt[j]
const redir = REDIRECT_RE.exec(toks[j])
if (!redir || (q >= 0 && q < redir[0].length)) words.push(toks[j])
else if (redir[0] === toks[j]) j++   // a bare operator: its target is the next word
```

The read-on test is the record's class-level fix: a word reads on past `>` or `<` only while every
character in it is unquoted and the whole is digits and then `<` and `>`. Its `&` alternative goes,
because "Evidence" shows no word reaches it. The drop test is the same rule seen from the token: an
operator is the operator only when none of it was quoted. A quote opening after the operator, as in
`2>"x.log"`, leaves the word a redirection.

`scanSegments` keeps its return shape, a list of arrays of strings, so every comparison in the head
grammar of `scanDenyHits` is untouched. Each array carries `quotedAt` as a property. The old test
`/["']/.test(cmd.slice(at, t.end))` asked the same question of the same bytes, and S2 replaces it
with the fact.

The docstring of `readTokenAt` says that a word ends before an unquoted `>` or `<` once it holds
quoting or anything but descriptor digits and operator characters, and that it returns where its
quoting opened. The comment in the branch says the same and no longer calls the pattern the prefix
`REDIRECT_RE` reads. The docstring of `scanSegments` names the `quotedAt` array, and the one of
`scanDenyHits` says a word whose quoting opens inside its operator is a word.

### The arms

Both arms join the block that opens `TOOL-aClearedLedger-13: the head-less segment`, after its last
`run_planted` line and before `F=$(build_fixture VERIFYING)`, so the 900 manifest is planted
(PINNED, 2026-11-14, at `f5a82b10`). A comment line naming this unit and item L2 sits above them.
Each runs through `run_planted` against `"$B"` and expects exit 0: bash runs the leg with one more
argument, a scoped spelling and not the leg, as the arm `D6 the same leg with a case word` holds.

| Arm | Name | Command fed |
|---|---|---|
| 1 | `D6 a quoted & glued before a redirection is an argument -> allow` | `"$M_FLAG '&'>x.log"` |
| 2 | `D6 a quoted > glued before a redirection is an argument -> allow` | `"$M_FLAG '>'>x.log"` |

Each command is double-quoted in the suite, so its single quotes reach the payload as typed. The
suite's payload liveness guard keeps an allow arm from passing on an empty payload.

`FLOOR_ASSERTIONS` moves from 217 to 219 (DERIVED: the floor TOOL-aClearedLedger-13 left at
`64673441`, plus one assertion per arm of this table). A comment line
`RAISED 217 -> 219 at TOOL-aClearedLedger-14` sits above the line for TOOL-aClearedLedger-13 and
names both arms. If the file's floor is no longer the value it holds at `f5a82b10` when the
builder opens it, the builder adds the arm count to the value found and says so in the ledger.

### The texts

The owner ruled fork F1 as C. Rows U1 to U7 are spellings the lint reads as hits and the hook,
once S1 to S3 are built, reads as a scoped run (PINNED, 2026-11-14, at `64673441`): the lint takes
the quote characters out of a word before it reads the redirection. Each text below lists them as
one more entry of the list TOOL-aClearedLedger-13 wrote, with no count word, and carries the
phrase `quoted operator character`, which AC6 reads.

| Text | Where the entry goes | What it says |
|---|---|---|
| header comment of `gate-guard.js`, row D6 | the list after "reads these spellings this row does not" | a quoted operator character before a redirection (`'&'>x.log`, `'>' x.log`), which this row keeps as an argument |
| `tools/unattended/README.md`, the paragraph on row D6 | the list after "reads these spellings the hook does not" | the same entry |
| docstring of `check_bar` | the list after "These are hits here and not there" | a quoted operator character before a redirection, which this reader reads with its quotes out and the hook keeps as an argument |

Each list keeps its other entries and their order, and the new entry sits before the `bash -c`
entry that closes it. The docstring is the only change to `tools/check-spec-tokens.py`.

### The probe

The rows file. Each row is `[id, command, hook]`, the shape of TOOL-aClearedLedger-12's, and the
legs are staged, so no ceiling re-derivation moves a row.

```json
[
["U1", "python t/over.py --selftest '&'>x.log", "miss"],
["U2", "python t/over.py --selftest '>'>x.log", "miss"],
["U3", "python t/over.py --selftest '2'>x.log", "miss"],
["U4", "python t/over.py --selftest \"&\">x.log", "miss"],
["U5", "python t/over.py --selftest ''2>x.log", "miss"],
["U6", "python t/over.py --selftest '>' x.log", "miss"],
["U7", "python t/over.py --selftest '<'<in", "miss"],
["U8", "python t/over.py --selftest 2>\"x.log\"", "hit"],
["U9", "python t/over.py --selftest >>\"$LOG\"", "hit"],
["U10", "python t/over.py --selftest>\"my log.txt\"", "hit"],
["U11", "python t/over.py --selftest 2>x.log", "hit"],
["U12", "python t/over.py --selftest '&'", "miss"]
]
```

Rows U1 and U2 are the arms' spellings. Rows U3 to U7 are the other quoted operator characters,
glued or spaced, which no arm feeds. Rows U8 to U10 have a quote opening after the operator and
must stay redirections. Row U11 is the unquoted control, and row U12 a quoted `&` with no
redirection, a miss before and after.

The probe, saved by the pass in the session scratchpad and run from the worktree's toplevel as
`node <probe file> <rows file>`. Its first two lines read the token stream of one command, and it
reads the rows files of TOOL-aClearedLedger-12 and TOOL-aClearedLedger-13 unchanged: a four-column
row gives its hook column as the third element.

```js
const fs = require('fs'), path = require('path')
const g = require(path.resolve('tools/unattended/gate-guard.js'))
const legs = [
  { name: 'over', ceiling: 301, words: ['t/over.py', '--selftest'] },
  { name: 'cases', ceiling: 301, words: ['t/cases.py', '--fixture', '--strict-from', 'x/'] },
]
const s = `a '&'>x b '>'>y c '2'>z d ''2>w e 2>"v" f >>"$L"`
const t = g.scanSegments(s, g.buildCommandView(s))[0]
console.log(t.join())
console.log(t.quotedAt === undefined ? 'no quotedAt' : t.quotedAt.join())
let bad = 0
for (const [id, cmd, want] of JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))) {
  const cand = []
  g.scanDenyHits(cmd, g.buildCommandView(cmd), 0, 'Bash', cand)
  const got = cand.some((c) => g.checkSuiteLeg(c, legs)) ? 'hit' : 'miss'
  if (got !== want) { bad++; console.log(id, 'read', got, 'want', want) }
}
console.log('rows wrong:', bad)
```

### What this corrects in the frozen specs

The specs of TOOL-aClearedLedger-12 and TOOL-aClearedLedger-13 are CLOSED and keep their text.
Where either and this spec differ, this spec is the rule.

The quoted read of TOOL-aClearedLedger-13, section 4, "The two reads", is this expression, as
`check_bar` holds it at `tools/check-spec-tokens.py@2b28752d:538`:

```python
re.findall(r"(?:[^\s\"']|\"[^\"]*\"|'[^']*'|[\"'])+", command)
```

The frozen cell at
`memory/builds/aClearedLedger/spec/2026-11-14-spec-TOOL-aClearedLedger-13.md@b50a3aa9:162` holds
the same bytes in a code span. A GFM table splits a row at every `|` not escaped as `\|`, a code
span included, and each alternation of the pattern puts one unescaped `|` in the cell.
The row splits into 6 cells against a header of 3 (PINNED, 2026-11-14, by AC5's probe at `b50a3aa9`).
GFM ignores every cell past the header's count. The rendered regex stops at its first alternative,
its closing backtick falls in a dropped cell, and the "What it is for" column shows a piece of the
pattern in place of its purpose. The block above is the text to read and copy.

| Frozen statement | Correction |
|---|---|
| TOOL-aClearedLedger-13, "The two reads", the quoted row's middle cell | the fenced expression above |
| TOOL-aClearedLedger-12, "The guard": the read-on pattern is the operator prefix `REDIRECT_RE` reads | the pattern is `^\d*[<>]*$` and a word holding quoting never reads on, by "The quoted fact" |
| TOOL-aClearedLedger-12, "What it does not check": a quoted `&` glued to a redirection is read as one redirection word | the word ends at the `>`, and the `&` is kept as an argument |
| TOOL-aClearedLedger-12, section 5, risks: the same spelling | no longer a risk once S1 to S3 are built |
| TOOL-aClearedLedger-12, "Alternatives rejected": the narrower pattern is set aside for the record's form | the narrower pattern holds, joined to the quoted test |

### The table probe

AC5 runs this from the worktree's toplevel as
`python <probe file> <this spec> <the spec of TOOL-aClearedLedger-13>`. It reads tables outside
fenced blocks only.

```python
import re, sys
F = "`" * 3
spec, frozen = (open(p, encoding="utf-8").read() for p in sys.argv[1:3])
code = open("tools/check-spec-tokens.py", encoding="utf-8").read()
fence = re.search(F + r"python\n(re\.findall\(.*\))\n" + F, spec).group(1)
print("restated in check_bar:", fence in code)
def cells(row): return len(re.split(r"(?<!\\)\|", row.strip()[1:-1]))
lines = frozen.splitlines()
row = next(l for l in lines if l.startswith("| quoted |"))
head = next(l for l in lines if l.startswith("| Read |"))
print("frozen row cells:", cells(row), "header cells:", cells(head))
bare = re.sub(F + r".*?" + F, "", spec, flags=re.S)
bad = 0
for block in re.findall(r"(?:^\|.*\n)+", bare, re.M):
    rows = block.splitlines()
    bad += sum(cells(r) != cells(rows[0]) for r in rows)
print("rows off their header:", bad)
```

### What it does not check

- No arm reds when the read-on clause `quotedAt >= 0` alone is taken out. With the drop test in
  place the joined word, `&>x.log` say, is kept as an argument, so every D6 verdict holds. The
  clause's own effect is on the tokens, which AC2 reads, and on row D4's head: `bash '2'>x.test.sh`
  is denied without it and allowed with it (PINNED, 2026-11-14), and no arm feeds that spelling.
- No arm feeds a quoted digit, a quoted `<`, an empty quoted pair, or a spaced quoted operator.
  The probe of AC1 reads each once, at build time, and no gate re-reads them.
- An empty quoted pair glued before a redirection, `''>x.log`. The word so far is empty, so it
  reads on as before, and the candidate keeps `>x.log` where bash passes an empty argument. Both
  spellings are longer than the leg, so the verdict agrees.
- The spec lint's answer for any row. `check_bar` reads rows U1 to U7 as hits (PINNED,
  2026-11-14), an over-read "The texts" lists, and no criterion runs `check_bar`.
- That the texts say what the code does. AC6 greps the phrase; the closing review reads the
  sentence against the code.
- A PowerShell-only spelling. The probe feeds every row as a `Bash` payload.
- The real manifest's legs. The probe's legs are staged, and the arms read the planted manifest.
- Markdown rendering. AC5 counts cells by the GFM split rule; it does not run a renderer.

### Inventory

This unit mints one identifier, `quotedAt`. It is a field of the object `readTokenAt` returns and
a property of each token array `scanSegments` returns. The lexicon's cells grade function and
type names, `js.function` and `js.type`, and no cell grades a field. `readTokenAt`,
`scanSegments` and `scanDenyHits` keep their names and signatures.

### Migration

None. No stored shape moves.

### Rollout

No switch. The hook binds where it binds today, before `VERIFYING` on a branch with a run record.
Every verdict that moves is a deny that becomes an allow on a spelling bash runs as a scoped suite.

### Files touched (estimate)

- `tools/unattended/gate-guard.js`
- `tools/unattended/gate-guard.test.sh`
- `tools/unattended/README.md`
- `tools/check-spec-tokens.py`

### Alternatives rejected

- **The read-on clause alone**, the record's text taken without a second site. A scratch copy
  holding it still read `--selftest '>'>x.log` as the leg, so arm 2 would fail with the clause
  built (PINNED, 2026-11-14). The drop in `scanDenyHits` re-reads the quoted `>` as an operator.
- **Any quoting makes a word an argument**, a boolean in place of the position. It reads
  `2>"x.log"` and `>>"$LOG"` as arguments, rows U8 to U10, a miss for a redirection bash makes.
- **Removing the `|&` branch alone**, the finder's fix. The review's skeptic judged it
  instance-only: a quoted `>` or digit glued before a `>` stays an operator.
- **Tokens as objects carrying their quoting.** Every comparison in the head grammar of
  `scanDenyHits` reads a token as a string, so the change would reach rows D1 to D5 for one fact
  that only the candidate loop reads.
- **Escaping each `|` in the frozen cell**, the record's first fix for L1. The cell is in a CLOSED
  spec, which this repository does not rewrite. The brief asks for the restatement here.

## 5. Production-readiness checklist

- security — N/A — a hygiene rule that fails open, as the hook's header states of itself. The
  change turns a deny into an allow only where bash passes a quoted character as an argument, and
  adds no read, write or grant.
- perf / scale — one integer per word, one array per simple command, and one comparison per
  redirection match.
- error / empty / loading states — a word holding only a quoted empty pair is kept as today. A
  bare unquoted operator with no target after it is read as one operator word, as today.
- observability — the deny text is unchanged and names the leg, as today.
- risks — a spelling the lint reads and the hook now allows, rows U1 to U7, which "The texts"
  lists. No arm isolates the read-on clause ("What it does not check").
- testing — AC1 to AC6 are probes a pass runs. The arms of section 7 are the main loop's.
- migration — N/A — no stored shape moves.
- user docs — `tools/unattended/README.md`, S8. No page under `help/` names the hook's rows.

## 6. Acceptance criteria

The probes and the rows file are section 4's. The older rows files are the JSON blocks of the
specs of TOOL-aClearedLedger-12 and TOOL-aClearedLedger-13, each saved as its own file.

- **AC1** — When the probe of "The probe" runs through `node` against
  `tools/unattended/gate-guard.js` and this spec's rows file, its last line reads `rows wrong: 0`,
  and it reads the same over each older rows file.
  Red when: the drop test is absent, which names rows U2, U6 and U7; the drop test keeps any word
  holding quoting, which names rows U8 to U10; or the hook is as at `64673441`, which names rows U1
  to U7.
  figure: at `64673441` the run over this spec's rows prints `rows wrong: 7`, and over each older
  rows file `rows wrong: 0` (PINNED, 2026-11-14).
- **AC2** — When the same probe runs through `node`, its first line reads
  `a,&,>x,b,>,>y,c,2,>z,d,2,>w,e,2>v,f,>>$L` and its second reads
  `-1,0,-1,-1,0,-1,-1,0,-1,-1,0,-1,-1,2,-1,2`.
  Red when: the read-on clause is absent, which prints `b,>>y` and `c,2>z` on the first line, or
  `scanSegments` does not hand the array on, which prints `no quotedAt`.
  figure: at `64673441` the lines read `a,&>x,b,>>y,c,2>z,d,2>w,e,2>v,f,>>$L` and `no quotedAt`
  (PINNED, 2026-11-14).
- **AC3** — When `grep -c 'run_planted "D6 a quoted . glued before a redirection is an argument -> allow"' tools/unattended/gate-guard.test.sh`
  runs, it prints 2.
  Red when: an arm of section 4's arm table is absent or runs outside `run_planted`.
  figure: 2 is DERIVED, the row count of that table; at `f5a82b10` the command prints 0.
- **AC4** — When `grep -c '^FLOOR_ASSERTIONS=219$' tools/unattended/gate-guard.test.sh` runs it
  prints 1, and `grep -c 'RAISED 217 -> 219 at TOOL-aClearedLedger-14' tools/unattended/gate-guard.test.sh`
  prints 1.
  Red when: the floor did not follow the arms the suite gained.
  figure: 219 is DERIVED, the floor at `f5a82b10` plus the count AC3 prints.
- **AC5** — When the table probe of section 4 runs through `python` over this spec and
  `memory/builds/aClearedLedger/spec/2026-11-14-spec-TOOL-aClearedLedger-13.md`, it prints
  `restated in check_bar: True`, then `frozen row cells: 6 header cells: 3`, then
  `rows off their header: 0`.
  Red when: the fenced expression differs from the one `check_bar` holds, the frozen row no longer
  splits as this spec says, or a table row of this spec holds an unescaped `|`.
  figure: 6 and 3 are PINNED, 2026-11-14, over the frozen spec at `b50a3aa9`.
- **AC6** — When `grep -c 'quoted operator character' tools/unattended/gate-guard.js tools/unattended/README.md tools/check-spec-tokens.py`
  runs, it prints 1 or more for every file. And when the code probe below runs through `python`
  from the worktree's toplevel, before the unit's commit, it prints `code unchanged: True`.
  Red when: a text does not name the difference, or any change to `tools/check-spec-tokens.py`
  reaches its syntax tree outside the docstring of `check_bar`.
  figure: at `64673441` the grep prints 0 for every file (PINNED, 2026-11-14). The code probe
  prints True at HEAD, True after a docstring-only edit and False after an edit to `check_bar`'s
  code, each in a scratch repository (PINNED, 2026-11-14).

The code probe. It parses the file at HEAD and in the worktree, blanks the docstring of
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

`tools/gate-legs.json` names the hook's suite nowhere (PINNED, 2026-11-14, at `64673441`). The
main loop runs that suite at the close, on a frozen clone, and the bar once after the last unit.
Before the suite's green run the main loop observes each arm below RED on the failing case its line
names, with the arms in place, and GREEN once the case is restored. A green run prints an `ok` line
for each arm of section 4's arm table, no line opening `FAIL`, and a total at or above
`FLOOR_ASSERTIONS`. The main loop also runs every leg on the line below at the close. The
docstring of `check_bar` trips the exact guard `{prefix}/check-spec-tokens.py`, which three legs
carry, and the spec-token suite reads that file. No arm is added for the texts: AC6 reads them.

`spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `spec-tokens self-test`

New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC3 · arm 1, the quoted `&`; the failing case is the hook put back to its blob `77894998`, which reads `'&'>x.log` on as one word and drops it as an `&>` redirection, so the arm exits 2. The drop test alone does not stage it, because the clause already ends the word at the `>` · `FLOOR_ASSERTIONS` 217 to 219, DERIVED, shared by both arms
New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC3 · arm 2, the quoted `>`; the failing case is the drop test taken out of the candidate loop of `scanDenyHits`, so the quoted `>` is a bare operator that skips `>x.log` as its target, and the arm exits 2 · the same floor move

## 8. Open questions

- **F1 — Do the texts that list the hook's differences from the spec lint gain this unit's new
  difference now?** TOOL-aClearedLedger-13 made three texts list every spelling the lint reads and
  the hook does not: the header comment of `tools/unattended/gate-guard.js`, the paragraph of
  `tools/unattended/README.md` on row D6, and the docstring of `check_bar`. After this unit, rows
  U1 to U7 are such spellings. The brief puts `tools/check-spec-tokens.py` out of scope, so the
  docstring cannot move here.
  - A: the header comment and the README gain "a quoted operator character glued before a
    redirection" now, and the docstring is handed off. The texts disagree with each other until
    the hand-off lands.
  - B: no text moves here. This spec records the difference, and the three texts take it together
    in a later unit, or in the shared spelling list ask TOOL-aDeferredBar-20 owns. The texts stay
    alike and stay incomplete, as they already are for a separator inside a quoted run.
  - C: the owner lifts the non-goal for that one docstring sentence, and all three texts move in
    this unit. It adds a comment-only change to a file the brief excluded.
  - Recommendation: B. Nothing any text says becomes false, since each lists spellings the lint
    reads and makes no claim to be complete, and a partial move would make two texts contradict a
    third.
  RESOLVED (owner, 2026-11-14): C — all three texts list the new difference in this unit

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.
- rev-2 · 2026-11-14 · §1 §3 §4 §5 §7 §8 S8 AC6 · the owner's ruling of 2026-11-14 on fork F1,
  option C: S8 and "The texts" add the quoted-operator difference to the three texts, the
  docstring of `check_bar` alone admitted in `tools/check-spec-tokens.py`; AC6 observes them; the
  estimate gains the README and that file, and the leg line the legs its guard owes.

## 10. Reuse audit

The seam is the word reader itself, `tools/unattended/gate-guard.js#readTokenAt`, and the token
list `scanSegments` already hands to `scanDenyHits`. The fact rides on that list, and the test it
replaces in `scanSegments` asked the same question of the same bytes. The arms join the planted
block through `run_planted` and `$M_FLAG`, which exist. `python tools/codebase-map/reuse_lookup.py
"record where quoting starts in a shell word so a quoted character is never read as a redirection
operator, in the gate guard hook's word reader and its redirection drop"` ranked name-stem
neighbours only, `read_text` and `read` among them, and named no word reader that tracks quoting,
so for a shared quote-aware tokenizer no existing seam fits. `tools/hooks/scratch-guard.js#readTokenAt`
returns a bare string with no quote position, and the hook may not require it, as
TOOL-aClearedLedger-12's audit records. The quoted read in `check_bar` is Python in a repository-root
tool and is out of this brief. The hits agreed with source.

Recall terms used: gate-guard readTokenAt quotedAt REDIRECT_RE redirection quoted operator
scanSegments scanDenyHits run_planted planted manifest FLOOR_ASSERTIONS GFM table cell pipe
