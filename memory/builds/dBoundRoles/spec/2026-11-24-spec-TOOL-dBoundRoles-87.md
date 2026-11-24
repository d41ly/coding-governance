# TOOL-dBoundRoles-87 — an in-place write behind a shell reserved word yields its target

**Status:** CLOSED · rev-1 · 2026-11-24 · node a · Tier-2 · base f3ec096a8 · streams tooling · order 41

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 |
| [2026-11-24-build-TOOL-dBoundRoles-87-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dBoundRoles-87-1-acceptance-ledger.md) | journal | — |
| [2026-11-24-build-TOOL-dBoundRoles-87-deviation-871.md](../build/2026-11-24-build-TOOL-dBoundRoles-87-deviation-871.md) | deviation | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-87-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-87-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-87-spec-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-87-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A `sed -i`, `perl -i`, interpreter write or `git apply` behind `then`, `do`, `else`, `{` or a sibling
word heads no simple command the shell-write scan recognises, so a role agent's write is admitted. This
unit makes the scan step the reserved words, and adds `coproc` and `function` to the words stepped,
closing item H1 of
`memory/builds/dBoundRoles/reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md`
(finding 1).

## 2. Scope (IN)

- **S1** — The scan steps the words. The call of `scanCommandHeads` in
  `tools/hooks/scratch-guard.js#scanWriteTargets` passes `reserved: true` beside the options it passes
  already. Observed by AC1.
- **S2** — `coproc` and `function`. `tools/hooks/scratch-guard.js#SHELL_RESERVED_WORDS` gains both. In the
  prefix loop of `tools/hooks/scratch-guard.js#scanCommandHeads`, `function` steps the word after it, its
  name; `coproc` steps the word after it only where the word after that opens a compound command, one of
  `{`, `if`, `while` and `until`, and the first is none of the list's words. Observed by AC1 and AC2.
- **S3** — The polling rows. `tools/hooks/scratch-guard.js#checkPollWait`, the other reader of the loop,
  reads what S2 steps: a `sleep` or a `tail` behind `coproc` or in a `function` body is a simple command
  of its own. Observed by AC2.
- **S4** — The list is readable. `SHELL_RESERVED_WORDS` joins the module's exports, so the suite's arms
  are driven from it. Observed by AC3.
- **S5** — The texts. The comment of `SHELL_RESERVED_WORDS`, which says the polling rows' scan alone steps
  it, and the paragraph of `scanCommandHeads`' comment on `opts.reserved`, name the shell-write scan and
  the name rule; the header's role-gate paragraph and its fifth-check paragraph say the words are stepped.
  Observed by AC4.
- **S6** — The arms. The owning suite gains one deny arm and its admit twin per entry of the exported
  list, from a spelling table keyed by word, and an entry with no spelling fails by name; rows for a
  named `coproc` and for the polling reader stand beside them. `FLOOR_ASSERTIONS` and its comment move by
  the rows printed, and the suite's row in `tools/run-gates/selftest-budgets.txt` is re-priced. Observed
  by AC5; their red and green are the main loop's at the close, by §7's `New arm:` lines.

**Readers:** by name: `tools/hooks/scratch-guard.js` (`scanCommandHeads`, which tests the list;
`checkPollWait` and `scanWriteTargets`, which ask for it) and `tools/hooks/scratch-guard.test.sh` (after
S4) · by value: `checkPollWait`, whose loop test reads `while` and `until` in an entry's `reserved` and so
now sees them behind `coproc`; `checkRoleGate`, which passes no `reserved` and sees nothing new;
`checkCommand` and `checkShellWrites`, which see through `scanWriteTargets` the in-place targets it now
yields.

## 3. Non-goals (OUT)

- The operand and redirect walks of `scanWriteTargets`: `TOOL-dBoundRoles-86` moves them, at the order
  before this one. This unit reads one option of one call and one loop, so it holds on that function
  whichever way the walks are laid out, and its criteria use in-place writes alone.
- The role-gate rows. They step no reserved word by design (`TOOL-aTrimmedWait-6`), and item H1 does not
  ask for it.
- `for`, `case`, `select` and `in`: the command each governs opens a later simple command, after a `;`, a
  `)` or a newline, which the scan splits at. `xargs`, `sudo` and `builtin` stay named escapes.
- A function's later call by name, a write from a script file, and an alias.

### Edges

none

## 4. Design

### Evidence

Read at HEAD `c31769972`, whose `tools/` tree equals base `f3ec096a8`'s.

- `scanWriteTargets` calls `scanCommandHeads(cmd, 0, { inline: true })`
  (`tools/hooks/scratch-guard.js@f71f3b8c:553`), `checkPollWait` passes `{ reserved: true }`
  (`tools/hooks/scratch-guard.js@f71f3b8c:2357`), and `checkRoleGate` passes nothing
  (`tools/hooks/scratch-guard.js@f71f3b8c:2479`).
- The list holds `!`, `{`, `do`, `then`, `else`, `elif`, `if`, `while` and `until`
  (`tools/hooks/scratch-guard.js@f71f3b8c:2191`), and the prefix loop steps one word of it at a time
  (`tools/hooks/scratch-guard.js@f71f3b8c:2282-2285`).
- Probed on 2026-11-24 by direct call of the exported functions: `scanWriteTargets` returned no target for
  a `sed -i` behind each word of the list, behind `coproc`, in `coproc N { }`, in `function f { }`, and for
  a `python -c` write behind `then`; `checkShellWrites` returned null for gov-skeptic's
  `if true; then sed -i ...; fi` over a path under `tools/`. `checkPollWait` returned null for
  `coproc sleep 30`, `function f { sleep 30; }` and `coproc tail -f x`.
- The change of S1 and S2, written as a scratch copy, returned the target for each of those spellings,
  both alone over the base file and over a scratch copy of the order-40 unit's design. Replayed on node a
  on 2026-11-24 over 11217 distinct recorded commands (PINNED, that reading), no `checkPollWait` row moved
  and the scratch verdict moved only on the commands the order-40 unit's spec counts.

### The step

```js
if (opts.reserved && SHELL_RESERVED_WORDS.includes(a[k])) {
  const w = a[k++]
  reserved.push(w)
  if (w === 'function' || (w === 'coproc' && NAMED_COPROC.includes(a[k + 1]) && !SHELL_RESERVED_WORDS.includes(a[k]))) k++
  continue
}
```

`coproc` takes a name only before a compound command, as Bash reads it, so `coproc sed -i ...` keeps `sed`
as the head and `coproc N { sed -i ...; }` steps `N`. A `(` after the name splits the segment already.
The block is the design's shape; the pass fits it to the function.

### Inventory

Minted: `NAMED_COPROC`, the compound openers, under no declared lexicon cell; `SHELL_RESERVED_WORDS` is
exported under its name; and the suite's `check_reserved_words`, an accepted `sh.function` name by
`python tools/lexicon/lexicon.py --suggest check_reserved_words --as sh.function`.

### Migration

None.

### Rollout

Live at landing, at order 41.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/run-gates/selftest-budgets.txt`

### Alternatives rejected

- **Pass `reserved: true` alone.** `coproc` and `function` would stay admitted, as the skeptic probed; the
  cited instance would close and its class would stand.
- **A second list for the shell-write scan.** Two readers of one shell grammar would drift; the polling
  rows gain the same words.
- **Step every word before a known write command.** `grep sed -i x` would read as a write.

## 5. Production-readiness checklist

- security — narrows what a role agent's shell write may reach; no new write path.
- perf / scale — one array test per word stepped.
- error / empty / loading states — a list word that ends its segment yields no entry, as today.
- observability — the refusal names the target and the shape, as it does for the bare command.
- risks — a polling row newly refuses a `sleep` in a `function` body or behind `coproc`, which is the wait
  the row exists for.
- testing — AC1 to AC3 by direct call; the arms of §7 at the close.
- migration — none.
- user docs — none; no page under `help/` states the words.

## 6. Acceptance criteria

Each of AC1 to AC3 calls exported functions of `tools/hooks/scratch-guard.js` through `node -e`. `F` is a
path under `tools/` and `W` the command `sed -i s/a/b/ F`.

- **AC1** — When `scanWriteTargets` reads `! W`, `{ W; }`, `for f in a; do W; done`, `if :; then W; fi`,
  `if :; then :; else W; fi`, `if :; then :; elif W; then :; fi`, `if W; then :; fi`, `while W; do :; done`,
  `until W; do :; done`, `coproc W`, `coproc N { W; }`, `coproc while W; do :; done`, `function f { W; }` and
  `bash -c 'if :; then W; fi'`, it returns `F` with `why` `sed -i` each time, and a `python -c` body opening
  `F` for writing behind `then` returns `F` as an `interpreter write`; and `checkShellWrites`, from a payload
  whose `agent_type` is `gov-skeptic` and whose `cwd` is this checkout's root, returns a `deny` for each.
  Red when: the call drops `reserved: true`, or the loop steps `coproc` or `function` without its name.
- **AC2** — When `checkPollWait` reads `coproc sleep 30` and `function f { sleep 30; }`, it returns row P3;
  `coproc while true; do sleep 1; done` returns P2 and `coproc tail -f x` returns P1; and `coproc cat x`,
  `function sleep { :; }` and `sleep 1` return null.
  Red when: a name is read as the head, or a word that names a function is read as a command.
- **AC3** — When `node -p "require('./tools/hooks/scratch-guard.js').SHELL_RESERVED_WORDS.join(' ')"` runs,
  it prints the list's words, `coproc` and `function` among them.
  Red when: the list is not exported, so the suite's arms restate it.
- **AC4** — When `grep -n "TOOL-dBoundRoles-87" tools/hooks/scratch-guard.js` runs, it prints a line in the
  list's comment, one in `scanCommandHeads`' comment and one in the header, and no line of the list's
  comment says the polling rows alone step it.
  Red when: the comment still names one reader.
- **AC5** — When `grep -n "TOOL-dBoundRoles-87" tools/hooks/scratch-guard.test.sh tools/run-gates/selftest-budgets.txt`
  runs, it prints the arms' comment, the floor's comment line and the suite's budget row; and
  `grep -n "^FLOOR_ASSERTIONS=" tools/hooks/scratch-guard.test.sh` prints the pin at the pass's base plus
  the rows that comment counts.
  Red when: the arms land with no floor move or an unpriced row.
  figure: the new pin is DERIVED from the pin at the pass's base, which the order-40 unit moves.

## 7. Gates

`scratch-guard self-test` · `format-guard self-test` · `spawn-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `lexicon naming predicates` · `policy fixtures` · `run-gates gov canary` · `measure-legs selftest` · `testsuite counts (every bar self-test prints one)` · `every held leg is budgeted, every budget row resolves` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC3 · one deny and one admit row per entry of the exported list, and the named `coproc`, run through `checkShellWrites` over the write gate's fixture in one node program, staged by dropping `reserved: true`, and by dropping `coproc` and `function` from the list, which leaves their spellings with no entry and fails by name · `FLOOR_ASSERTIONS` by the rows it prints
New arm: tools/hooks/scratch-guard.test.sh · covers AC2 · the polling rows behind `coproc` and in a `function` body with their admit twins, staged by a loop that steps neither · `FLOOR_ASSERTIONS` by the rows it prints

## 8. Open questions

- **F1 — Do `coproc` and `function` join the list, or a table of their own?** Options: (a) the list, the
  name rule in the loop; (b) a second table the loop also reads. (b) leaves the suite's arms reading two
  declarations, and item H1 asks that a new entry of the list owe an arm. RESOLVED (agent, 2026-11-24,
  delegated): (a). options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: the words the
  polling rows step, by both · relaxes: none
- **F2 — Does the role-gate scan step the words too?** Options: (a) no, as `TOOL-aTrimmedWait-6` left it;
  (b) yes. (b) changes what another arm refuses, which no clause of item H1 prices, veto 3. RESOLVED
  (agent, 2026-11-24, delegated): (a), the one survivor. options: (a) > (b) · pick: (a) · admitted-by:
  principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-24 · initial draft, from the brief
  `2026-11-24-prompt-TOOL-dBoundRoles-87-spec-brief` and item H1 of
  `2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1`.

## 10. Reuse audit

The seams extended are `tools/hooks/scratch-guard.js#scanCommandHeads`, whose `reserved` option and list
already exist, `tools/hooks/scratch-guard.js#scanWriteTargets`, and the suite's `run_shell_write` helper
over the write gate's fixture. `python tools/codebase-map/reuse_lookup.py "step a shell reserved word before
a command head"` ranked `before`, `step` and `read_head_sha`, name-stem hits and no shell reader, so no
existing seam fits beyond this one. The recall probe returned `TOOL-dRankedPlan-39`, which steps reserved
words in another kit's reader, and `TOOL-aTrimmedWait-6`, which wrote this list for the polling rows.

Recall terms used: `python tools/memory-recall/query.py "which readers step a shell reserved word before a command head" --terms "SHELL_RESERVED_WORDS scanCommandHeads reserved checkPollWait polling rows sed in place coproc function simple command role-gate arm scratch-guard"`
