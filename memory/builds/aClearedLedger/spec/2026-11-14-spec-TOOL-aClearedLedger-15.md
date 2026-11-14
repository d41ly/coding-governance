# TOOL-aClearedLedger-15 — the gate guard reads a redirection operator from unquoted text only, so a quoted character opening a glued target stays the target's

**Status:** SPECCED · rev-1 · 2026-11-14 · node a · Tier-2 · base 8db6f4be · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-prompt-TOOL-aClearedLedger-15-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-15-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aClearedLedger-15-brief.md](../prompts/2026-11-14-prompt-TOOL-aClearedLedger-15-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Round 4 of the closing diff review found that the drop test TOOL-aClearedLedger-14 added to
`scanDenyHits` measures the operator over the whole word, quoted characters included. So a glued
target that opens with a quoted `>`, as in `>'>x.log'`, makes the redirection look like an
argument, and row D6 allows the over-bound suite that the base denied. This unit matches
`REDIRECT_RE` against the text before the word's quoting alone, as the record's fix states, and arms
both spellings the record names. It is item H1 of that record.

## 2. Scope (IN)

The review is
`memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-14-diff-review-round4.md`.
Each item below names the review item it closes.

- **S1** — Item H1. In the candidate loop of `scanDenyHits` in `tools/unattended/gate-guard.js`, a
  word whose `quotedAt` is 0 or more is matched by `REDIRECT_RE` on its unquoted prefix
  `toks[j].slice(0, q)` alone. It is a redirection only if that prefix matches. A word with no
  quoting is matched whole, as today (section 4). Observed by AC1.
- **S2** — Item H1. The bare-operator step, which skips the next word as the target, fires only for
  a word with no quoting whose match is the whole word. Observed by AC1.
- **S3** — Item H1. `tools/unattended/gate-guard.test.sh` gains the two `run_planted` deny arms of
  section 4, "The arms", `$M_FLAG >'>x.log'` and `$M_FLAG 2>'>x.log'`. Observed by AC2.
- **S4** — Item H1. `FLOOR_ASSERTIONS` of that suite rises by the count of those arms, with a
  `RAISED` comment line in the file's own form. Observed by AC3.
- **S5** — Item H1. The docstring of `scanDenyHits` and the comments on the two changed lines say
  what S1 and S2 make true. NOT OBSERVED: no probe tells a true comment from a stale one, and the
  closing review reads them against the code.
- **S6** — Item H1. Section 4, "What this corrects in the frozen spec", states each statement of
  TOOL-aClearedLedger-14 that S1 and S2 make false, with its correction. NOT OBSERVED: it is text of
  this spec and not changed code, and the closing review reads it.

## 3. Non-goals (OUT)

- The record's items M1, L1, L2 and L3. TOOL-aClearedLedger-16 takes them.
- Any change to `tools/check-spec-tokens.py`, to `tools/unattended/README.md`, or to the header
  comment of `tools/unattended/gate-guard.js`. None of them describes how the drop test measures.
- Any edit to `REDIRECT_RE`, to `readTokenAt`, to `scanSegments` or to `checkSuiteLeg`. The `&`
  alternative of `REDIRECT_RE` matches no prefix once S1 is built, since an unquoted `&` ends a word; taking it out
  is not in the record's fix.
- The record's left-shift line: one deny arm for each quoted operator character an allow arm
  quotes. The brief asks for two arms. The probe of AC1 reads a quoted `<` and a double-quoted `>`
  once, and section 4, "What it does not check", names them.
- Any edit to a CLOSED spec, a lowered floor, a waived arm, any index render, and any kit version,
  which the lander's `mint` moves.

### Edges

- **consumes-from** external — the drop test and the quoted fact TOOL-aClearedLedger-14 built, its
  two allow arms, which must stay green, its floor, and its rows file, which AC1 re-reads. That
  sibling is CLOSED, so the edge is prose and not a join.
- **hands-off** `TOOL-aClearedLedger-16` — the candidate loop of `scanDenyHits` as section 4, "The
  drop", leaves it, whose keep-as-word predicate is `!redir`, and the floor of
  `tools/unattended/gate-guard.test.sh` this unit leaves, from which that unit derives its own move.

## 4. Design

### Evidence

Read at `998b627a`, the branch tip. The blobs are `tools/unattended/gate-guard.js@07723a18` and
`tools/unattended/gate-guard.test.sh@8d3a1720`.

- **The drop test measures across the quote.** The candidate loop at
  `tools/unattended/gate-guard.js@07723a18:620-623` runs `REDIRECT_RE` over the whole word and
  keeps it as an argument when `q < redir[0].length`. In `>'>x.log'` the reader adds the quoted `>`
  to the word, `tools/unattended/gate-guard.js@07723a18:397-399`, so the word is `>>x.log` with
  `quotedAt` 1. `REDIRECT_RE`, `tools/unattended/gate-guard.js@07723a18:486`, matches `>>`, two
  characters, and 1 is less than 2, so the word is kept.
- **Bash reads both spellings as a redirection.** In the session scratchpad,
  `printf '[%s]' a >'>x.log'` wrote `[a]` to a file named `>x.log`, and `printf '[%s]' b 2>'>y.log'`
  printed `[b]` and made a file named `>y.log` (PINNED, 2026-11-14).
- **The base denied them.** The hook at `64673441` read rows W1 and W2 of "The probe" as the leg,
  and the hook at `998b627a` reads them as a miss (PINNED, 2026-11-14).
- **The bare step skips a word bash keeps.** At `07723a18:623` a word whose match is the whole word
  skips the next word, quoting or not. `>''` is the word `>` with `quotedAt` 1, so in
  `--selftest >'' extra` the hook skips `extra`. Bash reads `>''` as a redirection to an empty file
  name and keeps `extra` as an argument; it then fails the redirection, printing
  `: No such file or directory` with exit 1, and runs nothing (PINNED, 2026-11-14).
- **The design was prototyped.** A scratch copy of the hook holding S1 and S2 read every row of
  this spec's rows file, and of the rows files of TOOL-aClearedLedger-12, TOOL-aClearedLedger-13
  and TOOL-aClearedLedger-14, as its expected column says (PINNED, 2026-11-14). The copy is outside
  the repository and is not the build.

### The drop

```js
// scanDenyHits, the candidate loop
const q = toks.quotedAt[j]
const redir = REDIRECT_RE.exec(q < 0 ? toks[j] : toks[j].slice(0, q))   // the operator is unquoted text
if (!redir) words.push(toks[j])
else if (q < 0 && redir[0] === toks[j]) j++   // a bare unquoted operator: its target is the next word
```

The operator is read from the characters before the word's quoting, since a quoted character is
never part of an operator. When that prefix matches, the word is a redirection whose target is
glued, quoted or not, and it is dropped. When it does not match, the quoting opened inside the
would-be operator, as in `'&'>x.log` or `2'>'x`, and the word is an argument. Where the quote opens
after a complete operator, the prefix is that operator, so `2>"x.log"` and `>'>x.log'` are both
redirections. A word holding quoting is never a bare operator: `>''` carries its empty target
glued.

The docstring of `scanDenyHits` keeps its paragraph on redirections and replaces its last two
sentences on quoting with these: a word holding quoting is a redirection only when the text before
its quoting starts with an operator `REDIRECT_RE` matches, so `'&'` and `2'>'x` are words, and
`2>"x.log"` and `>'>x.log'` are redirections. Only a word with no quoting can be a bare operator
whose target is the next word.

### The arms

Both arms join the block that opens `TOOL-aClearedLedger-14, review item L2`, after its last
`run_planted` line and before `F=$(build_fixture VERIFYING)`, at
`tools/unattended/gate-guard.test.sh@8d3a1720:825-826`, so the 900 manifest is planted. A comment
line naming this unit and review round 4's item H1 sits above them. Each runs through
`run_planted` against `"$B"` and expects exit 2: bash runs the leg with its output redirected, so
the words are the leg's.

| Arm | Name | Command fed |
|---|---|---|
| 1 | `D6 a quoted > opening a glued target after > -> deny` | `"$M_FLAG >'>x.log'"` |
| 2 | `D6 a quoted > opening a glued target after 2> -> deny` | `"$M_FLAG 2>'>x.log'"` |

Each command is double-quoted in the suite, so its single quotes reach the payload as typed. Each
pairs with the allow arm `D6 a quoted > glued before a redirection is an argument -> allow` of
TOOL-aClearedLedger-14: the same quoted `>`, once before an operator and once after one.

`FLOOR_ASSERTIONS` moves from 219 to 221 (DERIVED: the floor at `8d3a1720`, plus one assertion per
arm of this table). A comment line `RAISED 219 -> 221 at TOOL-aClearedLedger-15` sits above the
line for TOOL-aClearedLedger-14 and names both arms. If the file's floor is no longer 219 when
the builder opens it, the builder adds the arm count to the value found and says so in the ledger.

### The probe

The rows file. Each row is `[id, command, hook]`, the shape of TOOL-aClearedLedger-14's, and the
legs are staged, so no ceiling re-derivation moves a row.

```json
[
["W1", "python t/over.py --selftest >'>x.log'", "hit"],
["W2", "python t/over.py --selftest 2>'>x.log'", "hit"],
["W3", "python t/over.py --selftest >\">x.log\"", "hit"],
["W4", "python t/over.py --selftest <'<<in'", "hit"],
["W5", "python t/over.py --selftest >>'>x.log'", "hit"],
["W6", "python t/over.py --selftest >'' extra", "miss"],
["W7", "python t/over.py --selftest '&'>x.log", "miss"],
["W8", "python t/over.py --selftest '>'>x.log", "miss"],
["W9", "python t/over.py --selftest 2'>'x.log", "miss"],
["W10", "python t/over.py --selftest 2>\"x.log\"", "hit"],
["W11", "python t/over.py --selftest >> \"$LOG\"", "hit"],
["W12", "python t/over.py --selftest 2>x.log", "hit"]
]
```

Rows W1 and W2 are the arms' spellings. Rows W3 and W4 open a glued target with a double-quoted
`>` and a quoted `<`. Row W5 is a two-character operator, which the hook at `998b627a` already
reads, and row W6 is the bare step of S2. Rows W7 to W9 quote inside the would-be operator and must
stay words. Rows W10 to W12 are the controls: a quote after the operator, a spaced quoted target,
and no quoting.

The probe, saved by the pass in the session scratchpad and run from the worktree's toplevel as
`node <probe file> <rows file>`. It reads the rows files of TOOL-aClearedLedger-12,
TOOL-aClearedLedger-13 and TOOL-aClearedLedger-14 unchanged, each saved from that spec's JSON
block: a four-column row gives its hook column as the third element.

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

### What this corrects in the frozen spec

The spec of TOOL-aClearedLedger-14 is CLOSED and keeps its text, at blob `d68ef567`. Where it and
this spec differ, this spec is the rule.

| Frozen statement | Correction |
|---|---|
| S3: a word is a redirection only when the operator `REDIRECT_RE` matches ends before the word's quoting opens | a word holding quoting is a redirection only when the text before its quoting matches `REDIRECT_RE`, by "The drop" |
| "The quoted fact", the block of the candidate loop | the block of "The drop" |
| "The quoted fact": the drop test is the same rule seen from the token | the rule holds, and the token measure is the unquoted prefix; a match over the whole word reads a quoted target into the operator |
| "Evidence": the `&` alternative of `REDIRECT_RE` drops no word because the quoting opens inside the operator | it drops no word because `REDIRECT_RE` reads only unquoted text, where an `&` has already ended the word |
| "Rollout": every verdict that moves is a deny that becomes an allow on a spelling bash runs as a scoped suite | that build also allowed `>'>x.log'` and `2>'>x.log'`, which bash runs as the leg; this unit denies them again |
| "What it does not check" | a quoted operator character opening a glued target was missing from the list, and no arm or probe row fed it |

### What it does not check

- No arm feeds a double-quoted `>` or a quoted `<` opening a glued target, rows W3 and W4. The
  probe of AC1 reads each once, at build time, and no gate re-reads them.
- No arm feeds row W6, the bare step for a word holding quoting. Bash runs no command there, so
  neither verdict lets a suite run.
- No arm feeds row W10, a quote opening after a complete operator with no operator character
  inside it. A drop test that keeps every word holding quoting reds arms 1 and 2, which read rows
  W1 and W2 as a miss under it (PINNED, 2026-11-14, by a scratch mutant). So that weakening is
  covered here, but no arm here pins the plain quoted target on its own. TOOL-aClearedLedger-16
  owns the deny arms for that case.
- A PowerShell-only spelling. The probe feeds every row as a `Bash` payload.
- The real manifest's legs. The probe's legs are staged, and the arms read the planted manifest.

### Inventory

This unit mints no identifier. `scanDenyHits`, `REDIRECT_RE` and `quotedAt` keep their names and
shapes.

### Migration

None. No stored shape moves.

### Rollout

No switch. The hook binds where it binds today, before `VERIFYING` on a branch with a run record.
Two verdict classes move. A quoted operator character opening a glued target, rows W1 to W4, goes
from allow to deny, which is the base's verdict. A word holding quoting whose prefix is the whole
operator, row W6, goes from deny to allow, on a command bash refuses to run.

### Files touched (estimate)

- `tools/unattended/gate-guard.js`
- `tools/unattended/gate-guard.test.sh`

### Alternatives rejected

- **A greedy length test with the quote moved earlier**, some variant of `q < redir[0].length`. Any
  compare of the quote offset against a match over quoted text reads a quoted target character into
  the operator; the prefix match never sees one.
- **Any quoting makes a word an argument.** It reads rows W1 to W5 and W10 as a miss, each a
  redirection bash makes (PINNED, 2026-11-14, by a scratch mutant).
- **Keeping the bare step for a word holding quoting.** It reads row W6 as a hit, skipping an
  argument bash keeps (PINNED, 2026-11-14, by a scratch mutant), and item 1 of the brief keeps the
  step for an unquoted word alone.

## 5. Production-readiness checklist

- security — the hook is a hygiene rule that fails open, as its header states. This unit turns the
  allow the base denied back into a deny, and adds no read, write or grant.
- perf / scale — one string slice per quoted word in the candidate loop.
- error / empty / loading states — a word holding only a quoted empty pair keeps no prefix and is a
  word, as today. A word whose prefix matches and whose quoting is empty, `>''`, is a redirection.
- observability — the deny text is unchanged and names the leg, as today.
- risks — rows W3, W4 and W6 are read by the probe once and by no arm ("What it does not check").
- testing — AC1 to AC3 are probes a pass runs. The arms of section 7 are the main loop's.
- migration — N/A — no stored shape moves.
- user docs — N/A — no page under `help/` names the hook's rows, and `tools/unattended/README.md`
  does not describe how the drop measures.

## 6. Acceptance criteria

The probe and the rows file are section 4's. The older rows files are the JSON blocks of the specs
of TOOL-aClearedLedger-12, TOOL-aClearedLedger-13 and TOOL-aClearedLedger-14, each saved as its own
file.

- **AC1** — When the probe of "The probe" runs through `node` against
  `tools/unattended/gate-guard.js` and this spec's rows file, its last line reads `rows wrong: 0`,
  and it reads the same over each older rows file.
  Red when: the drop test measures across the quote, which names rows W1 to W4 and W6; the bare
  step fires for a word holding quoting, which names row W6; or the drop test keeps any word
  holding quoting, which names rows W1 to W5 and W10.
  figure: at `998b627a` the run over this spec's rows prints `rows wrong: 5`, and over each older
  rows file `rows wrong: 0` (PINNED, 2026-11-14).
- **AC2** — When
  `grep -cE '^run_planted "D6 a quoted > opening a glued target after 2?> -> deny" +2 "\$B" "\$M_FLAG 2?>.>x\.log."$' tools/unattended/gate-guard.test.sh`
  runs, it prints 2.
  Red when: an arm of section 4's arm table is absent, expects another exit, or runs outside
  `run_planted`.
  figure: 2 is DERIVED, the row count of that table; at `8d3a1720` the command prints 0 (PINNED,
  2026-11-14).
- **AC3** — When `grep -c '^FLOOR_ASSERTIONS=221$' tools/unattended/gate-guard.test.sh` runs it
  prints 1, and `grep -c 'RAISED 219 -> 221 at TOOL-aClearedLedger-15' tools/unattended/gate-guard.test.sh`
  prints 1.
  Red when: the floor did not follow the arms the suite gained.
  figure: 221 is DERIVED, the floor 219 at `8d3a1720` plus the count AC2 prints.

## 7. Gates

`tools/gate-legs.json` names the hook's suite nowhere (PINNED, 2026-11-14, at `998b627a`), and the
hook denies that suite at BUILDING. The main loop runs it at the close, on a frozen clone, and the
bar once after the last unit. Before the suite's green run the main loop observes each arm below
RED on the failing case its line names, with the arms in place, and GREEN once the case is
restored. A green run prints an `ok` line for each arm of section 4's arm table and for both allow
arms of TOOL-aClearedLedger-14, no line opening `FAIL`, and a total at or above
`FLOOR_ASSERTIONS`. The main loop also runs the legs on the line below at the close. Both files
under the estimate trip only the broad `{prefix}/` guard, which the checker excludes.

`spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC2 · arm 1, `$M_FLAG >'>x.log'`; the failing case is `tools/unattended/gate-guard.js` put back to its blob `07723a18`, the hook at `998b627a`, which keeps `>>x.log` as an argument, so the arm exits 0 where it expects 2 · `FLOOR_ASSERTIONS` 219 to 221, DERIVED, shared by both arms
New arm: `tools/unattended/gate-guard.test.sh` · covers AC1 AC2 · arm 2, `$M_FLAG 2>'>x.log'`; the same failing case, the hook at blob `07723a18`, which keeps `2>>x.log` as an argument, so the arm exits 0 · the same floor move

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.

## 10. Reuse audit

The seam is the candidate loop of `tools/unattended/gate-guard.js#scanDenyHits` and the
`quotedAt` array `scanSegments` already hands it; the fix changes the string `REDIRECT_RE` reads
and one condition, and adds no reader. The arms join the planted block through `run_planted` and
`$M_FLAG`, which exist. `python tools/codebase-map/reuse_lookup.py "measure a shell redirection
operator over only the unquoted text before a word's quoting, so a quoted character in a glued
target is never read into the operator"` ranked name-stem neighbours only, `read_text` and `read`
among them, and named no shared quote-aware redirection reader, so no existing seam fits beyond the
loop itself. `tools/hooks/scratch-guard.js#readTokenAt` returns a bare string with no quote
position, as TOOL-aClearedLedger-14's audit records. The hits agreed with source.

Recall terms used: gate-guard scanDenyHits REDIRECT_RE quotedAt unquoted prefix glued redirection
target quoted operator run_planted planted manifest FLOOR_ASSERTIONS
