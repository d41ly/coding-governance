# TOOL-dBoundRoles-86 — the shell-write arm reads operands and redirects per simple command

**Status:** CLOSED · rev-1 · 2026-11-24 · node a · Tier-2 · base f3ec096a8 · streams tooling · order 40

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 TOOL-dBoundRoles-93 |
| [2026-11-24-build-TOOL-dBoundRoles-86-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dBoundRoles-86-1-acceptance-ledger.md) | journal | — |
| [2026-11-24-build-TOOL-dBoundRoles-86-deviation-861.md](../build/2026-11-24-build-TOOL-dBoundRoles-86-deviation-861.md) | deviation | — |
| [2026-11-24-build-TOOL-dBoundRoles-86-widen-17.md](../build/2026-11-24-build-TOOL-dBoundRoles-86-widen-17.md) | widen | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-86-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-86-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-86-spec-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-86-spec-brief.md) | journal | — |
| [2026-11-24-review-TOOL-dBoundRoles-86-closing-diff-review-round2.md](../reviews/2026-11-24-review-TOOL-dBoundRoles-86-closing-diff-review-round2.md) | diff-review | TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 |

<!-- /gen:spec-records -->

## 1. Goal

`scanWriteTargets` reads a write's operands and redirects off raw text, so a role agent's write is
judged on a word that is not its target: a real write is admitted and an ordinary command is refused.
This unit reads both from the simple commands `scanCommandHeads` yields, closing item B1 of
`memory/builds/dBoundRoles/reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md`
(findings 2, 3, 27 and 28).

## 2. Scope (IN)

- **S1** — Operands per simple command. `scanWriteTargets` takes the operands of `tee`, `touch`,
  `mkdir`, the PowerShell write cmdlets, `cp`, `mv`, `install` and `rsync` from the `argv` of each
  entry `scanCommandHeads` returns. A write word counts as the head, by basename, or as an unquoted
  word at any later place of the same simple command, as it does at base. The any-argument words take
  every operand after the word, with no bound on their number. The last-argument words take the last
  operand. Observed by AC1.
- **S2** — The target-directory option. `cp`, `mv` and `install` carrying `-t <dir>`, a short cluster
  ending in `t`, `-t<dir>`, `--target-directory <dir>` or `--target-directory=<dir>` write `<dir>`, and
  their operands are sources (§8 F2). `rsync` is not read so. Observed by AC1.
- **S3** — Redirects. One reader, `scanRedirects`, matches each redirect operator in the string-blanked,
  comment-blanked view after any character, and reads its word after the whole operator, past blanks and
  a line continuation. `scanCommandHeads` calls it before it splits a command, so every operator and its
  word leave `argv` wherever they stand, and in inline mode each output redirect is an entry of its own.
  The operators are those of the table in §4. Observed by AC2 and AC5.
- **S4** — The exclusions. No target comes from a process substitution, from a duplication or a close of
  a descriptor, from a comparison inside `[[ ]]` at command position or inside balanced `(( ))`, or from a
  backslash-escaped operator. A preceding `=` or `-` excludes nothing. The comparison and backslash
  exclusions do not apply to a PowerShell command, where neither spelling is that syntax, so
  `scanWriteTargets` takes the tool name and `checkShellWrites` passes it. Observed by AC3.
- **S5** — Substitutions in operand position. In inline mode an unquoted `$( )`, `<( )` or `>( )` is
  scanned as a command of its own and stands in the outer command as one word, so an operand after it is
  still read; a word opening with `<(` or `>(` is no target. Observed by AC1.
- **S6** — The quoted word. `scanCommandHeads` reads, without its quotes, a double-quoted word whose text holds
  an escaped quote, the escaping backslash gone too, so a `bash -c` body is read as the shell reads it.
  Observed by AC5.
- **S7** — The texts. The header of `tools/hooks/scratch-guard.js`, its list of what escapes, the
  comments of `scanWriteTargets` and `scanCommandHeads`, and the sections of `tools/hooks/README.md` on
  the fifth check and the write-target guard state the shapes read and the escapes of §4. Observed by AC7.
- **S8** — The arm family. The owning suite gains one table-driven family over spelling, role and
  expected verdict, each row run once at a target outside the role's class and once at a target in no
  repository, so a new spelling owes both. `FLOOR_ASSERTIONS` and its comment move by the rows the
  family prints, and the suite's row in `tools/run-gates/selftest-budgets.txt` is re-priced. Observed by
  AC8; the family's red and green are the main loop's at the close, by §7's `New arm:` lines.

**Readers:** by name: `tools/hooks/scratch-guard.js` (`checkCommand`, the scratch verdict, which passes
no tool name; `checkShellWrites`; and, of `scanCommandHeads`, `scanWriteTargets`, `checkRoleGate` and
`checkPollWait`), `tools/hooks/scratch-guard.test.sh` (its `scan_targets` helper and the rows that run
the hook) and `tools/hooks/README.md` (the census that replays commands through `scanCommandHeads`) ·
by value: `checkCommand` sees the targets of §4's table it missed, and no longer sees the stray words;
`checkShellWrites` sees the same set and judges each as it does at base; `checkRoleGate` and
`checkPollWait` ask for no inline entry, so they see no redirect entry and no substitution entry, they
no longer see a head `1` after `2>&1`, and they see the words that follow a redirect in one command.

## 3. Non-goals (OUT)

- An in-place write behind a shell reserved word, item H1: `TOOL-dBoundRoles-87` builds it after this
  unit, over the same function. A `cp` or a `touch` behind a reserved word is read here, by S1's any
  place, as it is at base.
- The options of `sed` and `perl`, items M1 and M2, and the rows of item L3: other units of this set.
- A variable, a `cd`, a command inside double quotes, or a full shell tokenizer.
- The value options of the any-argument words (`mkdir -m 755`), which read as targets at base and after.
- Any change to what `checkShellWrites` decides about a target it is handed.

### Edges

none

## 4. Design

### Evidence

Read at HEAD `c31769972`, whose `tools/` tree equals base `f3ec096a8`'s. Every item was probed on
2026-11-24 by calling the exported functions of `tools/hooks/scratch-guard.js@f71f3b8c` in node:

- `scanWriteTargets` (`tools/hooks/scratch-guard.js@f71f3b8c:547`) returned `2>/dev/null`, `2>`, `hi` and
  `note` as the destination of a `cp` trailed by `2>/dev/null`, by `2>&1`, by an `echo hi` line and by a
  comment; it returned `git` and `status` as targets of a `mkdir` followed by a `git status` line.
- It returned no target for `echo a>F`, `cat>F`, `echo x >|F`, `echo x >&F` and `echo a=>F`; the target
  `>F` for `&>>F`; and a lone backslash for a redirect continued on the next line.
- It returned a target for `[[ a > b ]]` and for `(( a > b ))`.
- `checkShellWrites` (`tools/hooks/scratch-guard.js@f71f3b8c:2116`) over this checkout: gov-spec-writer's
  `cp` of a file into `tools/` is denied and the same trailed by `2>/dev/null` is admitted with a
  witness; gov-skeptic's `mkdir -p` outside the repository is denied when trailed by `2>/dev/null` or by a
  `git status` line; gov-skeptic's glued redirect into `tools/` is admitted.
- A backslash-continued `cp` destination is read today and stays read.
- Two shapes the report does not name fall to the same cause: `cp a 2>&1 F` and `cp a >|LOG F` end at the
  `&` and the `|` of the operator, and an unquoted `cp $(echo a) F` is denied on `a`, not on `F`. Reading
  `argv` alone would admit the last, which is why S5 is in scope.

### The redirect operators

Located in the view; `F` is the word read.

| spelling | target | why |
|---|---|---|
| `>F`, `>>F`, `n>F`, `n>>F`, `{v}>F` | `F` | glued or spaced, after any character |
| `>\|F` | `F` | the noclobber override |
| `&>F`, `&>>F` | `F` | both streams |
| `<>F` | `F` | opened for reading and writing |
| `>&F`, `>& F` | `F` | `F` not digits, digits with `-`, or `-`, read to the word's end |
| `*>F` | `F` | PowerShell only: the `*` is the operator's |
| `n>&m`, `n>&-`, `n<&m` | none | a duplication or a close |
| `<F`, `<<TAG`, `<<<W` | none | the word leaves `argv` as today |
| `>(`, `<(` | none | a process substitution |

A digit run is the descriptor only at the start of a word, so `a2>F` is the word `a2` and a redirect.
The word ends at unquoted whitespace, `;`, `|`, `&`, `(`, `)`, `<` or `>`, so `>A>B` is two targets.
`readTokenAt` stays the reader of the git, `cd` and temp-root tokens, unchanged.

### The flow

1. `scanCommandHeads` blanks strings and comments as it does, then calls `scanRedirects(cmd, view, tool)`,
   which returns the targets and the view with each operator and its word blanked to the same length, so
   every offset holds. The word-level redirect filter in its loop is deleted.
2. A line continuation in the view is blanked, so it splits nothing and is no word.
3. In inline mode, the redirect targets are pushed as `{ redirect }` entries, and each innermost
   `$(`, `<(` or `>(` span is scanned through the same function at the same depth and masked by a filler
   of the same length, until none is left. An unbalanced span stays as it is and splits as today.
4. Each ordinary inline entry also carries `raw`, its `argv` words with their quotes kept, so a quoted
   `install` is no write word and a quoted operand is still read.
5. `scanWriteTargets` adds each `redirect`, then for each entry the operands of its write words, the
   in-place operands and the patch targets, each `value` and `why` pair once.

The comparison exclusion blanks the arrows of a `(( ))` span whose parentheses balance up to the closing
pair, which the fallback `((echo x) > F; (true))` does not, and of a `[[ ... ]]` span on one line opening
at command position, which `echo [[ a > F ]]` does not.

### Observed on real commands

The design was written as a scratch copy of the hook on 2026-11-24 and replayed on node a over the
recorded Bash and PowerShell commands of the node's transcripts, 11190 distinct ones (PINNED, that
reading). `checkCommand` newly refused three, each a real `cp` or redirect under `/tmp` that a following
`||` or `2>/dev/null` had hidden, and stopped refusing one, an `awk` program read as a `mkdir` operand
across a newline. No command's `checkPollWait` row moved. Every target that disappeared was a stray word.
Over the string literals of `tools/hooks/scratch-guard.test.sh` the two verdicts differ on prose labels
alone, so no command row moves.

### What still escapes, for the header and the README

A redirect or a command inside a quoted `$( )` or backticks; a comparison spelled in more than one nested
parenthesis level, or one across lines, which refuses rather than admits; an unquoted arrow inside
`${ }`, which reads as a redirect, quoting being the remedy; a PowerShell operand built in parentheses;
a PowerShell alias or a cmdlet the list does not name; the `-d` form of `install`, of which the last
operand is read; and every escape the header names today.

### Inventory

Minted: `scanRedirects`, an accepted `js.function` name by `python tools/lexicon/lexicon.py --suggest
scanRedirects --as js.function`; the constant for the comparison span, under no declared cell; the
fields `redirect` and `raw` of an inline entry; and the suite's `scan_shell_spellings`, accepted for
`sh.function`. `REDIRECT`, `WRITE_ANY_ARG` and `WRITE_LAST_ARG` keep their names; the last two become
lists of words.

### Migration

None.

### Rollout

Live at landing, at order 40. The kit's version moved to `1.52` in this build with
`TOOL-dBoundRoles-25`, so no further bump is made here.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/README.md`
- `tools/run-gates/selftest-budgets.txt`

### Alternatives rejected

- **Bound the raw-text walk at a newline and skip redirect words.** Finding 27's skeptic found it loses
  the continued destination; it also leaves comments and mid-command operators.
- **Read a write word at the head only.** `sudo cp`, `xargs touch`, `git mv` and a `cp` behind a reserved
  word are read at base and would be lost.
- **Exclude a preceding `=` or `-`.** `echo a=>f` and `echo -> f` are real redirects (finding 2).
- **Match redirects in `scanWriteTargets` beside the reader.** Two parsers would answer one question, and
  a `-c` body would be read for operands and not for redirects (§8 F1).

## 5. Production-readiness checklist

- security — narrows what a role agent's shell write may reach; no new write path, and a throw still
  refuses a role agent.
- perf / scale — one more linear pass per command; the replay saw no command over 200 ms.
- error / empty / loading states — an unbalanced span or a missing word yields no target and no throw.
- observability — the refusal names the true target and shape, where it named a stray word.
- risks — a wider redirect match refuses an ordinary command; AC6 replays the recorded ones and §4 states
  the reading the design was chosen on.
- testing — AC1 to AC6 by direct call; the family of §7 at the close.
- migration — none.
- user docs — `tools/hooks/README.md` per S7; no page under `help/` states these shapes.

## 6. Acceptance criteria

Each of AC1 to AC5 calls exported functions of `tools/hooks/scratch-guard.js` through `node -e`. `F` is a
path under `tools/` and `S` one outside every repository.

- **AC1** — When `scanWriteTargets` reads `cp a F` plain, with a line continuation before `F`, and trailed
  by each of `2>/dev/null`, `2>&1`, a comment and a following command line, then `cp a 2>&1 F`,
  `cp a >|S F`, `cp $(echo a) F`, `cp <(echo a) F`, `sudo cp a F`, `if cp a F`, `cp -t F a` and
  `cp --target-directory=F a`, the one `cp destination` is `F` each time; and reading `mkdir -p S` trailed
  by `2>/dev/null` and by a `git status` line, its `mkdir` targets are `S` alone; and `grep -n 'install' x`
  returns none.
  Red when: an operand is read past its simple command or lost with it, or a redirect word, a comment or
  the next line's command is an operand, as at base.
- **AC2** — When `scanWriteTargets` reads each output row of §4's table over `F`, glued and spaced (the
  `*>F` row with the tool name `PowerShell`), then `echo a=>F`, `echo -> F`, `echo x >F>S`, a redirect
  continued on the next line, and `bash -c 'echo x > F'`, each returns `F` as a `redirect` target, with no
  operator character in it.
  Red when: an operator needs a separator before it, or `>|`, `&>>` or `>&` is not one operator.
- **AC3** — When `scanWriteTargets` reads `x 2>&1`, `x >&-`, `x <F`, `tee >(cat)`, `[[ a > b ]]`,
  `if [[ a > b ]]; then :; fi`, `(( a > b ))`, `echo $(( 3>2 ))`, `echo a \> b`, `echo "a->b"` and a comment
  holding an arrow, it returns none; and `echo [[ a > F ]]`, `[[ a > b ]] && echo x > F`,
  `((echo x) > F; (true))`, and `((echo x > F))` with the tool name `PowerShell`, each return `F`.
  Red when: an excluded spelling refuses a role's ordinary command, or an exclusion hides a real redirect.
- **AC4** — When `checkShellWrites` reads each deny spelling of the report's step five over `F`, from a
  payload whose `agent_type` is `gov-skeptic` and whose `cwd` is this checkout's root, it returns a `deny`
  naming `F`; the same spelling over `S`, and each admit spelling of its step six, returns null. With
  `gov-spec-writer`, a `cp` from `S` to `F` trailed by `2>/dev/null` returns a `deny`.
  Red when: a role's write is judged on any word but its target.
- **AC5** — When `scanCommandHeads` reads `bash a.sh 2>&1 --x`, it returns one entry whose `argv` is `a.sh`
  and `--x`, carrying neither `redirect` nor `raw`; reading `bash -c "echo \"see > b\""` in inline mode, it
  returns no `redirect` entry.
  Red when: an operator splits its simple command, or a quoted arrow of a `-c` body reads as a redirect.
- **AC6** — When a pass probe replays the recorded commands of the node's transcripts through
  `checkCommand` and `checkPollWait` of the base blob and of the built file, each command the built file
  newly refuses writes the target it names, and no polling row moves but on a command whose words after a
  redirect carry it.
  Red when: the wider match refuses an ordinary command.
  cost: about two minutes.
  fixture: the transcripts under the operator's `.claude/projects`; a node with none records that.
  figure: the count of commands replayed is DERIVED at observation time.
- **AC7** — When `grep -n "scanRedirects" tools/hooks/scratch-guard.js` runs, the header and both function
  comments name it, and `grep -n "TOOL-dBoundRoles-86" tools/hooks/README.md` prints a line in the fifth
  check's section and one in the write-target guard's.
  Red when: the contract texts still state the shapes read at base.
- **AC8** — When `grep -n "TOOL-dBoundRoles-86" tools/hooks/scratch-guard.test.sh tools/run-gates/selftest-budgets.txt`
  runs, it prints the family's comment, the floor's comment line and the suite's budget row; and
  `grep -n "^FLOOR_ASSERTIONS=" tools/hooks/scratch-guard.test.sh` prints the pin at the pass's base plus
  the rows that comment counts.
  Red when: the family lands with no floor move or an unpriced row.
  figure: the pin is 465, PINNED at this spec's writing; the new one is DERIVED from the pass's count.

## 7. Gates

`scratch-guard self-test` · `format-guard self-test` · `spawn-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `lexicon naming predicates` · `policy fixtures` · `run-gates gov canary` · `measure-legs selftest` · `testsuite counts (every bar self-test prints one)` · `every held leg is budgeted, every budget row resolves` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 AC4 · the spelling family run through `checkShellWrites` over the write gate's fixture, one node program, two rows per spelling, staged by the base scanner, against which every report spelling's deny row or admit row fails · `FLOOR_ASSERTIONS` by the rows it prints
New arm: tools/hooks/scratch-guard.test.sh · covers AC2 AC3 AC5 · `scan_targets` rows for the exact value of each operator of §4's table and of the target-directory option, staged by a redirect pattern that needs a separator before it · `FLOOR_ASSERTIONS` by the rows it prints

## 8. Open questions

- **F1 — Where are redirects read?** Options: (a) in `scanCommandHeads`, through `scanRedirects`, emitting
  entries in inline mode; (b) in `scanWriteTargets`, over the outer view, the reader dropping redirect
  words on its own. (b) keeps two parsers of one syntax and leaves a redirect in a `bash -c` body unread.
  RESOLVED (agent, 2026-11-24, delegated): (a), which meets every criterion of the report's fix and leaves
  fewer escapes. options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: the shapes the
  scanner reads, by a redirect in a `-c` body · relaxes: none
- **F2 — Does the target-directory option of `cp`, `mv` and `install` name the destination?** Options:
  (a) it does; (b) the last operand stays the destination and the header names the option as an escape.
  (b) leaves a write judged on a source, the class this unit closes. RESOLVED (agent, 2026-11-24,
  delegated): (a), the option that leaves no follow-up. options: (a) > (b) · pick: (a) · admitted-by:
  principle.p18 · widens: the shapes the scanner reads, by that option · relaxes: none
- **F3 — Do the comparison and backslash exclusions apply to a PowerShell command?** Options: (a) no, by
  the tool name; (b) yes, both tools read alike. Under (b) a nested PowerShell redirect in `(( ))`, read
  at base, is lost. RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) ·
  admitted-by: principle.p18 · widens: none · relaxes: none
- **F4 — How is an operand after an unquoted substitution read?** Options: (a) mask each unquoted
  substitution and scan it apart, S5; (b) split at its parenthesis and name the rest an escape. (b) admits
  `cp $(echo a) F`, which base refuses. RESOLVED (agent, 2026-11-24, delegated): (a), since (b) relaxes a
  refusal. options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-24 · initial draft, from the brief
  `2026-11-24-prompt-TOOL-dBoundRoles-86-spec-brief` and item B1 of
  `2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1`.

## 10. Reuse audit

The seams extended are `tools/hooks/scratch-guard.js#scanCommandHeads`, which already drops redirections,
strips comments and splits a command, `tools/hooks/scratch-guard.js#scanWriteTargets`, its one write-target
reader, and the suite's `scan_targets` and `run_shell_write` helpers over the write gate's fixture.
`python tools/codebase-map/reuse_lookup.py "read a shell command's write targets and operands"` ranked
`read_text`, `read` and `write`, name-stem hits and no shell reader, so no existing seam fits beyond the
one in this file. `TOOL-dRankedPlan-39` and `TOOL-dRankedPlan-46` extend the shell reader of another kit,
and a copy-installed hook imports none. The recall probe returned `TOOL-dBoundRoles-7`, the unit that made
this scanner the role boundary, and the review item.

Recall terms used: `python tools/memory-recall/query.py "what did earlier units decide about scanWriteTargets and the shell-write arm" --terms "scratch-guard scanWriteTargets scanCommandHeads checkShellWrites redirect operand cp destination role agent allowance writes none escape list"`
