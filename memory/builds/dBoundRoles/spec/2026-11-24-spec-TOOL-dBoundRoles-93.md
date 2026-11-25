# TOOL-dBoundRoles-93 — the closing review's round-2 mediums: a PowerShell block is read as its own command, and the arms and leg guards the fold left out

**Status:** CLOSED · rev-1 · 2026-11-24 · node a · Tier-2 · base 3c9b6ad0e · streams tooling · order 47

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 TOOL-dBoundRoles-95 |
| [2026-11-24-build-TOOL-dBoundRoles-93-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dBoundRoles-93-1-acceptance-ledger.md) | journal | — |
| [2026-11-24-build-TOOL-dBoundRoles-93-deviation-931.md](../build/2026-11-24-build-TOOL-dBoundRoles-93-deviation-931.md) | deviation | — |
| [2026-11-24-build-TOOL-dBoundRoles-93-widen-18.md](../build/2026-11-24-build-TOOL-dBoundRoles-93-widen-18.md) | widen | — |
| [2026-11-25-build-TOOL-dBoundRoles-93-1-owner-ruling.md](../build/2026-11-25-build-TOOL-dBoundRoles-93-1-owner-ruling.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-93-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-93-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-93-spec-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-93-spec-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dBoundRoles-93-close-resume.md](../prompts/2026-11-25-prompt-TOOL-dBoundRoles-93-close-resume.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Close the mediums of the closing diff review's round 2, M1 to M9 of
`memory/builds/dBoundRoles/reviews/2026-11-24-review-TOOL-dBoundRoles-86-closing-diff-review-round2.md`.
M1 is a permitted PowerShell edit refused over a phantom target. M2 to M7 are arms over code that reads
correctly today, and M8 and M9 are leg guards that skip a check the fold added.

## 2. Scope (IN)

Each item takes the report's stated fix, the skeptic's class-level one where the report names it.

- **S1** — M1, finding 6. Where the tool is PowerShell, `scanCommandHeads`
  (`tools/hooks/scratch-guard.js@690899c6:2394`) matches each brace pair of its view before `scanRedirects`
  runs, scans the inside of each outermost block as a command of its own, and blanks the block out of the
  command that holds it (§8 F1). A pair opened by `${` or `@{`, `stash@{` being one, stays whole, and a brace
  behind a backtick or with no partner stays as it is. `checkPollWait` reads PowerShell's loop keywords from
  the view, since a loop's block no longer carries its brace into the `sleep` (§8 F2). The Bash reading does
  not move by a byte. Observed by AC1, AC2 and AC3.
  **Readers:** by name: `tools/hooks/scratch-guard.js` (`scanWriteTargets`, `checkRoleGate` and
  `checkPollWait` call `scanCommandHeads`; `checkShellWrites` and `checkCommand` read it through
  `scanWriteTargets`), `tools/hooks/scratch-guard.test.sh` and `tools/hooks/README.md` (the census that replays
  commands through it) · by value: `checkShellWrites` sees no `}` target, the operands and redirects of a
  spaced or glued block, and every operand after a block that it sees today; `checkCommand` passes no tool
  name, so it sees what it sees today; `checkRoleGate` sees the head inside a block, so a gate run in one is
  refused; `checkPollWait` sees a `sleep` or `tail` in a glued block, reads a block's duration without its
  brace, and sees a loop by its keyword.
- **S2** — M2, finding 10. The spelling family of `tools/hooks/scratch-guard.test.sh` gains the rows that write
  inside an unquoted substitution, the arithmetic admit row and the row whose operand follows a nested
  substitution. Observed by AC4.
- **S3** — M3, finding 11. The family gains the write word at a later place of a command and the quoted write
  word that is an argument. Observed by AC5.
- **S4** — M4, finding 12. The bare `-I` row at `tools/hooks/scratch-guard.test.sh@346ebb16:1678` takes a command
  whose script is a word a misread makes a file. Observed by AC6.
- **S5** — M5, finding 13. The suite gains the escaped-quote `-c` bodies, an in-place operand and a redirect.
  Observed by AC7.
- **S6** — M6, finding 14. Each part of the PowerShell reading the report lists gains a row its own mutant turns
  red, the open-quote row run with no tool name (§8 F5). Observed by AC8.
- **S7** — M7, finding 15. `tools/loop/loop_items.py` gains the plants `declaration-role-refused` and
  `declaration-root`, and `help/loop.md` names both. Observed by AC9.
- **S8** — M8, finding 16. The `govkit selftest` row of `tools/govkit/registry.toml` guards the roles and policy
  kits its positive control reads (§8 F4). Observed by AC10.
- **S9** — M9, finding 17. The `spawn-guard self-test` row guards `.claude/roles.json` and the workflows kit's
  folder, which replaces the single `spec-audit-optin.js` entry. Observed by AC11.
- **S10** — The suite's floor, the budget rows and the pages move with the items above, in the places §4
  "Floors and budgets" and "Documents" state. Observed by AC12 and AC13.

## 3. Non-goals (OUT)

- The findings the report refuted. The quote-before-comment, backtick-quote and here-string readings of
  `buildCommandView`, the `perl -d:` read and the tool-less view of `scanWriteTargets` stay as they are;
  `TOOL-dBoundRoles-94` carries them.
- Handing `checkCommand` a tool name. The write-target guard reads PowerShell as Bash today and after.
- PowerShell's keyword casing in `SHELL_RESERVED_WORDS`, its own wait cmdlets, and any new write cmdlet.
- A reserved-word step for the gate rows in Bash, which `TOOL-aTrimmedWait-6` left out on purpose.
- A derivation of leg guards from what a suite reads, and a mutant runner over the suite's rows.
- Any change to the code S2 to S7 hold, and any edit of a CLOSED spec.

`TOOL-dBoundRoles-86`, `TOOL-dBoundRoles-87`, `TOOL-dBoundRoles-88`, `TOOL-dBoundRoles-91` and
`TOOL-dBoundRoles-92` built what these items hold. Each is CLOSED, so this unit takes nothing from them and
leaves them nothing.

### Edges

none

## 4. Design

### Evidence

Probed at HEAD `7fa5e4986`, whose `tools/` tree equals base `3c9b6ad0e`'s. Each mutant is a scratch copy of the
file with the named code changed. Every defect and every missing arm still holds.

| item | probe | reading |
|---|---|---|
| M1 | `scanWriteTargets` with `PowerShell` over the report's in-place commands | `tools/x` and a phantom `}` on each; `{sed -i s/a/b/ tools/x}` and `{cp a tools/x}` yield nothing; `{echo a >tools/x}` yields `tools/x}` |
| M1, trade | the separator form of the fix over `Set-Content -Value {a} q` and `cp {a} q` | no target, where HEAD reads `q`; the form of S1 reads `q` |
| M1, polling | `checkPollWait` with `PowerShell` over `while ($true) { sleep 1 }` | HEAD refuses by P3, reading `}` as a duration; the brace fix alone, in either form, admits it |
| M2 | the recursive push, the pop and the `$((` body bounds each cut | only the rows AC4 names move, each under its own cut |
| M3 | a head-only test, then a dequoted compare, in `scanWriteOperands` | the later-place rows read nothing; `grep -n 'install' q` reads `q` |
| M4 | the `-I` line cut | `perl -I lib -pi s/a/b/ x.py` reads `s/a/b/` beside `x.py`; the standing row does not move |
| M5 | `readWordText` keeping the backslash | the in-place body reads a lone backslash and a word ending in one, the redirect body a lone backslash |
| M6 | each part cut | the reading AC8 states; `cp a "C:\x\"` moves under the open-quote cut only where no tool is handed |
| M7 | the verb run in a scratch of `build_scratch_tree` | a role row at a gov slot is refused with the composition's line, and the refusals check cut prints JSON; a raw `--root` answers `no [[item]] row declares`; a directory in no work tree is refused |
| M8, M9 | `--legs-for` over the paths of AC10 and AC11 | neither leg stands under its paths |

### The PowerShell block

`scanScriptBlocks(view)` returns the outermost `{ from, to }` spans of a blanked view, as `scanSubstitutions`
(`tools/hooks/scratch-guard.js#scanSubstitutions`) does for parentheses: one pass, a stack of open offsets, a
backtick stepping the character after it. A pair whose opener follows `$` or `@` is popped and not recorded, so
a block nested in a hash literal is still found. A recorded pair drops the recorded spans inside it.

In `scanCommandHeads`, for PowerShell alone, after the substitution mask and before the `scanRedirects` call at
`tools/hooks/scratch-guard.js@690899c6:2412`, each span's inside, sliced from `cmd`, is scanned by
`scanCommandHeads` at the same depth with the same `opts`, and the whole span becomes blanks in the view. The
view keeps its length, so offsets hold. A redirect word, an operand and a head therefore each stop at a block,
and a word after the block stays in its own command. An entry found twice, through a substitution inside a
block, is dropped by `addTarget`'s pair set, and a repeated head changes no verdict.

`checkPollWait`'s `loop` also holds, for PowerShell, where `buildCommandView(cmd, tool)` carries `while`,
`until`, `for` or `foreach`, in any case, at the start or after whitespace or one of `;&|(){}`, and then an
opening parenthesis. The last sentence of `renderPollDeny` says that a PowerShell `for` or `foreach` loop counts too.

What it does not see, stated in the file's header beside the arm's other escapes: a brace with no partner, a
block inside quotes, a block a PowerShell here-string holds, and a loop keyword spelled in a comment, which
refuses.

### Rows

A target in these rows is written `q`, or `@` where the spelling family substitutes it.

- **S1, `scan_targets` with `PowerShell`.** `{ sed -i s/a/b/ q }`, `if ($c) { perl -pi -e s/a/b/ q }`,
  `{sed -i s/a/b/ q}`, `{ cp a q }`, `{cp a q}` and `{echo a >q}` each want `q` alone;
  `Set-Content -Value {a} q` wants `q` alone; `cp a ${d}/x`, `cp a @{}`, `cp a stash@{0}` and a `cp` whose
  destination is a backtick-escaped brace pair each want that operand whole.
- **S1, polling,** in the reserved-word program beside its standing polling rows, each carrying the tool:
  `while ($true) { sleep 1 }`, `do { sleep 1 } until ($x)` and `for (;;) { sleep 1 }` want P2, `{sleep 30}` wants
  P3, `if ($c) { sleep 1 }` wants none. One `run_role_bash` PowerShell row runs the bar in a glued block and
  wants the G2 refusal.
- **S2.** Deny, `gov-researcher`, Bash: `x=$(touch @)`, `echo $(echo x > @)`, `cat <(touch @)`,
  `$(echo $(touch @))` and `cp $(echo $(echo a)) @`. Admit: `echo $(( 3>2 ))`.
- **S3.** Deny: `sudo cp a @`, `xargs touch @` and `git mv a @`. Admit: `grep -n 'install' @` and
  `grep -n "install" @`.
- **S4.** The standing row's command becomes `perl -I lib -pi s/a/b/ x.py`, wanting `x.py` alone.
- **S5.** `bash -c "sed -i s/a/b/ \"q.py\""` wants `q.py`, and `bash -c "echo x > \"q r\""` wants `q r`.
- **S6.** Deny, PowerShell: `ls "C:\x\"; touch @`, and a `bash -c '...'` whose body echoes a double-quoted word
  holding a Bash-escaped quote and then runs `touch @`. `run_role_bash`, PowerShell: the bar runner, and
  `sleep 30`, each after `ls "C:\x\";`, wanting G2 and P3. `scan_targets`, PowerShell: a comment block over lines holding
  `y > f`, then `ls`, wants none; `<# c #> touch q` wants `q`; `mkdir d *>&1` wants `d`. `scan_targets` with no
  tool: `cp a "C:\x\"` wants `C:\x\`.

### The plants

`run_scratch_declaration` (`tools/loop/loop_items.py@25925136:763`) gains the working directory and the
`--root` value it runs with, each defaulting to what it passes today, an empty `--root` leaving the option out.

- `declaration-role-refused` commits an overlay `[[role]]` row tagged at the slot of a gov role,
  `role.adopter.gov-builder`, and asks for `item.test.select`. It owes exit 1, the words
  `the role composition does not read`, and no JSON.
- `declaration-root` commits the `ship` overlay and asks for the repository item from the scratch's loop kit
  directory, once with `--root` naming that directory and once with none, each owing the composed row. Then it
  asks with `--root` at a directory made outside every repository under the host temp directory, removed after, owing exit 1
  and `sits in no git work tree`.

### Leg guards

The rows at `tools/govkit/registry.toml@0d6b082f:797` and `tools/govkit/registry.toml@0d6b082f:1226` move as S8
and S9 state: `{prefix}/roles/` and `{prefix}/policy/` join the first; `.claude/roles.json` joins the second and
`{prefix}/workflows/` replaces `{prefix}/workflows/spec-audit-optin.js`. `tools/gate-legs.json` is
rendered by `python tools/run-gates/leg_factory.py --write`, never by hand. Each folder stays at or under
`BROAD_LEG_FLOOR` of `tools/check-spec-tokens.py`, so the guards join still reads it.

### Floors and budgets

`FLOOR_ASSERTIONS` of `tools/hooks/scratch-guard.test.sh` rises by the assertions the pass adds, counted off the
added rows and said in the comment above the pin, a spelling-family row counting once per run it makes. S4
replaces a command, so it adds none. The loop fixtures have no floor.

In `tools/run-gates/selftest-budgets.txt` the `scratch-guard self-test` and `loop item kind` rows are re-priced
as that file's PINNED proxy, each saying what was added and that no suite ran, and the second moves its
`plants=` count. The main loop re-prices from its first reading.

### Documents

- `tools/hooks/README.md`: row P2 and the polling paragraph name PowerShell's loop keywords; the shell-write
  section says a PowerShell block is read as a command of its own; its escapes gain those of the header.
- `help/roles.md`: the polling bullet names PowerShell's `for` and `foreach`.
- `help/loop.md`: the plant list gains the plants of S7, with its usage marker where the help leg asks.

### Inventory

Minted: `scanScriptBlocks` (`js.function`; `python tools/lexicon/lexicon.py --suggest scanScriptBlocks --as js.function`
answers OK), and the plants `declaration-role-refused` and `declaration-root`.

### Migration

None.

### Rollout

Live at landing, at order 47. The hooks kit's version is the one this build already carries, and the landing
mints it against the remote, so no bump is made here. The `gate-legs.json` edit moves a path the kickoff
manifest watches, so that commit re-stamps its `last-audit`.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`, `tools/hooks/scratch-guard.test.sh`, `tools/hooks/README.md`
- `tools/loop/loop_items.py`
- `tools/govkit/registry.toml`, `tools/gate-legs.json`
- `tools/run-gates/selftest-budgets.txt`
- `help/roles.md`, `help/loop.md`
- `memory/guides/SESSION-KICKOFF.md`, its `last-audit` re-stamp alone

### Alternatives rejected

- **One unit per medium.** The build method's M4 batches a review's minors.
- **Splitting in the segment loop of `scanCommandHeads`,** the finder's fix. `scanRedirects` runs before it, so
  `{echo a >tools/x}` keeps its brace.

## 5. Production-readiness checklist

- security — S1 removes a false refusal and closes misses in PowerShell blocks for the write, gate and polling
  arms; F2 states the one refusal it releases. S8 and S9 widen what runs a check. No grant widens.
- perf / scale — one pass over a PowerShell view and one recursion per block; the guarded suites run on more edits.
- error / empty / loading states — an unbalanced brace and an empty block are read as today and as blank.
- observability — a refusal names the block's own simple command, never the brace.
- risks — a view every reader shares moves for PowerShell; AC2 and AC3 hold the readers S1 names.
- testing — §6 and the arms of §7.
- migration — N/A — nothing stored changes shape.
- user docs — `help/roles.md` and `help/loop.md`, as §4 states.

## 6. Acceptance criteria

Each criterion over a suite row is observed by the row's own command fed to the code, or by its block sliced with
its suite's prologue into a scratch file, never by the suite. A staged break is a scratch copy, and the mutant a
criterion names is observed by the same command over that copy.

### Scratch guard

- **AC1** — When
  `node -e "console.log(require('./tools/hooks/scratch-guard.js').scanWriteTargets(process.argv[1],'','PowerShell'))"`
  runs over each `scan_targets` row of S1 in §4, it prints that row's target alone.
  Red when: a block's closing brace or a glued block is read as at base, the block is a separator and
  `Set-Content -Value {a} q` loses `q`, or the `$`, `@` or backtick step is cut and an operand splits.
- **AC2** — When `node` calls `checkPollWait` of `tools/hooks/scratch-guard.js` with `PowerShell` over each
  polling row of S1, it answers that row's P2, P3 or null, and `scanCommandHeads` over a glued block running the
  bar yields the runner as a head.
  Red when: the loop reading is cut, so `while ($true) { sleep 1 }` is null; or the block is not scanned, so
  `{sleep 30}` is null and the head keeps its brace.
- **AC3** — When `node` compares `scanCommandHeads` and `scanWriteTargets` of `tools/hooks/scratch-guard.js` with
  those of its blob at `3c9b6ad0e`, `690899c6`, written to a scratch file by `git cat-file blob`, over every command of the suite's
  `scan_targets` rows, spelling family and reserved-word program, with `Bash` and with no tool, and in the plain,
  `reserved` and `inline` modes, each answer is equal.
  Red when: the block reading runs for another tool than PowerShell, which a Bash `{ cp a q; }` then shows.
- **AC4** — When `checkShellWrites` reads the S2 rows through the family's program `sw86.js`, every deny row
  refuses naming its target and the admit row is null; over a copy with the recursive push cut, the pop of
  `scanSubstitutions` cut, or the `$((` bounds made a plain body's, the write-inside rows, the nested-operand row
  and the arithmetic row red in that order.
  Red when: any one of those copies leaves every row green.
- **AC5** — When the same `sw86.js` reads the S3 rows, each answers its verdict; over a copy whose
  `scanWriteOperands` tests the head alone every deny row reds, and over one that compares the dequoted word
  every admit row does.
  Red when: either copy leaves every row green.
- **AC6** — When `scan_targets` reads `perl -I lib -pi s/a/b/ x.py`, it reads `x.py:perl -i` alone.
  Red when: the line that consumes a detached `-I` value is cut, and `s/a/b/` is read beside it.
- **AC7** — When `scan_targets` reads the S5 rows, it reads `q.py:sed -i` and `q r:redirect`.
  Red when: `readWordText` keeps the backslash of an escaped quote, and each row reads a lone backslash.
- **AC8** — When the S6 rows run through `sw86.js`, `scan_targets` and `run_role_bash`, each answers as §4
  states; over a copy with one part cut, that part's row reds: the backslash rule, the `<# #>` blanking, the copy
  reading of `*>&1`, the open-quote token, the `tool: undefined` of a `-c` body, and the tool handed to the gate
  scan and to `checkPollWait`.
  Red when: any one of those parts is cut and no row moves, as at base.

### Loop

- **AC9** — When `python tools/loop/loop_items.py --fixture --plant declaration-role-refused` and the same with
  `declaration-root` run, each exits 0 and its lines carry `the role composition does not read`, the repository
  item's composed row, and `sits in no git work tree`; over a scratch copy of the tool root whose
  `tools/loop/loop_lib.py` drops the refusals check, composes at the raw `--root`, defaults it elsewhere, or
  drops the work-tree test, the plant of that behaviour exits 1.
  Red when: any one of those copies leaves both plants at exit 0.

### Leg guards

- **AC10** — When `python tools/check-spec-tokens.py --legs-for -` reads `tools/roles/return-check.sh`,
  `tools/roles/return-check.fragment.json`, `tools/roles/handoff.py`, `tools/roles/roles_lib.py` and
  `tools/policy/policy.py`, one per line, `govkit selftest` stands under each path.
  Red when: one of them trips no row of that leg, as each does at base.
- **AC11** — When that command reads `.claude/roles.json` and each path its `harnesses` list names,
  `spawn-guard self-test` stands under each; and under `tools/workflows/spec-audit-optin.js` it still does.
  Red when: one of them trips no row of that leg, or the replaced entry is lost.

### Floors and documents

- **AC12** — When `git diff -U0` of the pass is read, the rise of the suite's
  `FLOOR_ASSERTIONS` equals the assertions its added lines execute, and the budget rows §4 names moved.
  Red when: a row lands under an unmoved floor, where a skipped block stays green.
- **AC13** — When `grep -n "foreach" tools/hooks/README.md help/roles.md` and
  `grep -n "declaration-root" help/loop.md` run, each file carries its line.
  Red when: a page states the polling row or the plant list as at base.

## 7. Gates

`scratch-guard self-test` · `format-guard self-test` · `spawn-guard self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `unattended-build self-test` · `policy fixtures` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `recall floor` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `loop item kind` · `help reference pages` · `help page commands` · `gate-leg conformance` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 · the block scan cut, then the separator form, then the loop reading cut · `FLOOR_ASSERTIONS`, as §4 states
New arm: tools/hooks/scratch-guard.test.sh · covers AC4 · the push, the pop, then the arithmetic bounds cut · `FLOOR_ASSERTIONS`, the same move
New arm: tools/hooks/scratch-guard.test.sh · covers AC5 · the head-only test, then the dequoted compare · `FLOOR_ASSERTIONS`, the same move
New arm: tools/hooks/scratch-guard.test.sh · covers AC6 · the detached `-I` line cut · none, the row's command replaced
New arm: tools/hooks/scratch-guard.test.sh · covers AC7 · `readWordText` keeping the backslash · `FLOOR_ASSERTIONS`, the same move
New arm: tools/hooks/scratch-guard.test.sh · covers AC8 · each part of the PowerShell reading cut in turn · `FLOOR_ASSERTIONS`, the same move
New arm: tools/loop/loop_items.py · covers AC9 · the refusals check dropped, then the raw root, the default and the work-tree test · none

## 8. Open questions

- **F1 — M1: is a block blanked to separators, or scanned as a command of its own and blanked out?** Options:
  (a) the second, the seam `scanSubstitutions` already is; (b) separators, the skeptic's wording; (c) a split in
  the segment loop. (b) loses the operand after a block, `Set-Content -Value {a} q`, which HEAD reads, so it makes
  the trade M1's own class names; (c) leaves redirect words holding the brace. (a) has the effect the skeptic
  states, words, operands and heads stopping at the block. RESOLVED (agent, 2026-11-24, delegated): (a).
  options: (a) > (b) > (c) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F2 — M1: what holds P2 in PowerShell once the brace leaves the duration?** Options: (a) read `while`,
  `until`, `for` and `foreach` before a parenthesis, from the view; (b) the first pair alone, as Bash reads;
  (c) nothing. (c) admits `while ($true) { sleep 1 }` and (b) admits `for (;;) { sleep 1 }`, and HEAD refuses
  both. RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) > (c) · pick: (a) · admitted-by:
  principle.p18 · widens: none · relaxes: a short `sleep` in a PowerShell block that is no loop's is admitted,
  as the row's own text says
- **F3 — M1: every reader of `scanCommandHeads`, or the inline mode alone?** Options: (a) every reader; (b) the
  inline mode, which the shell-write scan alone asks for. (b) leaves a gate run and a poll in a block unread and
  gives one command two views. RESOLVED (agent, 2026-11-24, delegated): (a), the report's shared view.
  options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: the gate and polling rows refuse a
  PowerShell block's command they miss today · relaxes: none
- **F4 — M8: the kits' folders or the files the control reads?** The report admits both. Options: (a)
  `{prefix}/roles/` and `{prefix}/policy/`; (b) each file. (b) misses the next file the installed command reads,
  a role's own text among them. RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) ·
  admitted-by: principle.p18 · widens: none · relaxes: none
- **F5 — M6: with which tool does the open-quote row run?** Options: (a) none, as `checkCommand` reads a
  PowerShell payload; (b) `PowerShell`, the report's wording. Under (b) the view closes the quote, and the row is
  green with the token cut. RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) ·
  admitted-by: principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-24 · initial draft, from the brief
  `2026-11-24-prompt-TOOL-dBoundRoles-93-spec-brief` and the closing review's round 2, findings 6 and 10 to 17.

## 10. Reuse audit

The seams extended are the code each item names: `tools/hooks/scratch-guard.js#scanCommandHeads` and the shape of
its neighbour `scanSubstitutions`, `checkPollWait`, the suite's `scan_targets`, `run_role_bash`, spelling family and
reserved-word program, `tools/loop/loop_items.py#run_declaration_plant`, and the registry rows that own the leg
guards. `python tools/codebase-map/reuse_lookup.py "split a PowerShell command at its script block braces before reading its write targets"`
and the same over `"scan a nested command span as a command of its own"` ranked name neighbours alone; no other
existing seam fits. `gate-guard.js` in the unattended kit keeps its own `buildCommandView` and reads no block. The
recall probe returned the round-2 report, the ask `TOOL-dBoundRoles-94` and the deviation
`2026-11-24-build-TOOL-dBoundRoles-86-deviation-861`, which states the quoting repair.

Rejected candidates and the test that rejected each: the separator form, by `Set-Content -Value {a} q` losing its
target in a scratch copy; the brace fix with no loop reading, by `while ($true) { sleep 1 }` answering null there.

Recall terms used: `python tools/memory-recall/query.py "what the closing review round 2 left untested in the PowerShell reading and which leg guards miss the files their suites read" --terms "scanCommandHeads PowerShell script-block brace buildCommandView scanRedirects checkPollWait observed-by-claim-no-arm-discharges fixture-passes-by-finding-nothing held-suite-guard-misses-a-sibling-kit a-view-fix-trades-one-blindness-for-another"`
