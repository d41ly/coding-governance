**Serves:** diff-review TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92

# dBoundRoles — Tier-2 CLOSING DIFF review, round 2

*2026-11-24. The subject is the FOLD of round 1: units TOOL-dBoundRoles-86 to TOOL-dBoundRoles-92, every one CLOSED.*
*Roles: finders gov-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.*
*Intent: 7 spec documents supplied as `specs`, beside the range's commit messages.*
*Checklist: 102 items, acquired by the harness from `--for-diff f3ec096a83f63cac1ff056b7df11820845fb722b..3c9b6ad0ed85759e8ccd90863ff0369c361eb224`, each assigned to exactly one of 5 lenses: security 21, correctness 21, seams 20, verification 20, intent 20.*
*By design: the caller's byDesign, and 1 invariant from the checklist's by-design block.*
*Security model: the hooks are fail-closed and advisory against an agent, not against an adversary with shell access.*
*Every citation in the body is blob-pinned as `<path>@<sha8>:<line>` at the reviewed head.*

**Range reviewed: f3ec096a83f63cac1ff056b7df11820845fb722b...3c9b6ad0ed85759e8ccd90863ff0369c361eb224**

**Round: 2.**

## Verdict: CLEAN WITH FIXES

No item is a BLOCKER or a HIGH.
All nine items are MEDIUM.
M1 is the only defect in shipped behaviour: the fold made a PowerShell in-place edit inside a block yield a phantom target `}`, so a permitted edit is refused.
M2 to M7 are missing or vacuous arms over code that reads correctly today.
M8 and M9 are two leg guards that skip a check this fold added.
M9 leaves round 1's item M10 partly open, and M8 leaves the control built for round 1's item M5 unreached on a guarded bar.
No confirmed finding says that round 1's BLOCKER or one of its HIGHs still stands.
I recommend folding M1, M8 and M9, which are small.
The arms of M2 to M7 can be folded with them or filed.

## Review shape

Intensity full, raw 17, confirmed 9, refuted 8, merged 0, unverified 0 (0 uncertain), precision 0.53.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 0 | 2 | 0 | 0 | 0 | 0.00 |
| correctness | yes | 5 | 1 | 4 | 0 | 0 | 0 | 0.20 |
| seams | yes | 2 | 0 | 2 | 0 | 0 | 0 | 0.00 |
| verification | yes | 6 | 6 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 9 items (0 blocker, 0 high, 9 medium, 0 low).
Adjudicated tally by raw confirmed finding: 9 (0 blocker, 0 high, 9 medium, 0 low).
The two tallies agree because each item holds exactly one finding.
Every confirmed finding takes its binding grade; none was regraded here.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 6 judged sound, 0 judged UNSOUND, 3 judged INSTANCE-ONLY (findings 6, 10, 14), 0 none proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing, so each such item carries the skeptic's class-level fix.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 2 RE-GRADED by the skeptic (findings 10 and 11, each from high to medium).
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 8. Same-address pairs shown: 1.
- Dispositions: unclassed is `refuse`; 102 class slugs handed; 224 leg names read from tools/gate-legs.json.

Every count that would mark the run incomplete is zero.

The one same-address pair is confirmed 14 and refuted 2, and it is not a twin.
Finding 14 is the missing arms over the PowerShell reading the fold built.
Finding 2 claimed that PowerShell's backtick quote and here-strings are not read at all.
No other refuted claim describes the defect of a confirmed finding, so no twin is flagged.

## MEDIUM

### M1. A stepped `{` makes a PowerShell block's closing brace an in-place target (finding 6)

**Where:** `SHELL_RESERVED_WORDS`, which steps `{`, at `tools/hooks/scratch-guard.js@690899c6:2318`.
The target is taken in `scanInPlaceOperands`, at `tools/hooks/scratch-guard.js@690899c6:600`.
The finder's own address, `tools/hooks/scratch-guard.js@690899c6:236`, is a blank line at head.

**What is wrong:** TOOL-dBoundRoles-87 steps the word `{`, so the in-place reader now reaches a command inside a PowerShell script block.
PowerShell needs no `;` before `}`, so the closing brace is a word of that command and is read as a file.
At the base, `{ sed -i s/a/b/ tools/x }`, `if ($c) { sed -i s/a/b/ tools/x }` and `{ perl -pi -e s/a/b/ tools/x }` return no target.
At head each returns `tools/x` and a phantom target `}`.

**Consequence:** a permitted in-place edit is refused over a file nobody writes.
It fails closed, and adding `;` before the brace avoids it.
Only this in-place part is confirmed.
The `cp` destination `}`, the extra `}` of `Set-Content` and the miss on a glued block such as `{Set-Content tools/x a}` are identical at the base, so they are pre-existing.

**Grade:** MEDIUM, as bound.

**Fix (the skeptic's class-level fix):** for PowerShell, blank block braces to a separator in the view before `scanRedirects` runs.
Match each brace pair, and skip both ends of a pair opened by `${`, `@{` or `stash@{`, so that redirect words, operands and heads all stop at the block.
Add arms for spaced and glued blocks, for `sed -i`, `cp` and a redirect, and for `${d}/x` and `@{}` operands left whole.
The finder's proposal, splitting in `scanCommandHeads`' `seg`, cures the cited instance alone: `scanRedirects` runs first on the unsplit view, so `{echo a >tools/x}` still gives `tools/x}`.

**Left-shift:** `class:a-view-fix-trades-one-blindness-for-another`, with the block arms standing in the `scratch-guard self-test` leg.

### M2. No arm fails when an unquoted substitution's body is not scanned (finding 10)

**Where:** the recursive push in `scanCommandHeads`, at `tools/hooks/scratch-guard.js@690899c6:2406`.
The family it lacks rows in opens at `tools/hooks/scratch-guard.test.sh@346ebb16:1855`.

**What is wrong:** TOOL-dBoundRoles-86 S5 scans each unquoted `$( )`, `<( )` and `>( )` as a command of its own.
The only substitution rows are `cp $(echo a) d`, its family twin and `tee >(cat) <(y)`, and none writes inside the substitution.
With the push removed, every BR86, BR87 and BR92 row and every SW86 spelling stays green.

**Consequence:** with the push removed, `x=$(touch q)`, `echo $(echo x > q)`, `cat <(touch q)` and the nested form go from `q` to no target, and the base read all four.
The span is then masked, so a regression would admit every role write inside an unquoted substitution with the suite green.
The shipped code is correct.

**Grade:** MEDIUM, as bound; the skeptic lowered it from high because only a regression arm is missing.

**Fix (the skeptic's class-level fix):** add SW86 deny rows `x=$(touch @)`, `echo $(echo x > @)`, `cat <(touch @)` and the nested `$(echo $(touch @))`, and an admit row `echo $(( 3>2 ))`.
Add one more deny row whose operand follows a nested substitution, `cp $(echo $(echo a)) @`, so that removing the outermost pop misaligns the operand it reads.
Observe each red against its own mutant: the push cut, the pop cut, and the `$((` body bounds changed.
The finder's proposal cures the cited instance alone: its nested row stays denied when the pop is removed.

**Left-shift:** `class:observed-by-claim-no-arm-discharges`, with the rows standing in the `scratch-guard self-test` leg.

### M3. No arm holds the any-place write word, nor its unquoted-only half (finding 11)

**Where:** the name test of `scanWriteOperands`, at `tools/hooks/scratch-guard.js@690899c6:540`.

**What is wrong:** TOOL-dBoundRoles-86 S1 and AC1 read a write word at any later place of a simple command, and only where it is unquoted.
The suite holds no `sudo`, `xargs` or `git mv` command, and no quoted write word as an argument of another command.
The family row meant for it, `if cp a @`, became a head match once TOOL-dBoundRoles-87 stepped the reserved words.

**Consequence:** a head-only test leaves every row green while `sudo cp a q`, `xargs touch q` and `git mv a q` lose their target.
Comparing the dequoted word also leaves every row green while `grep -n 'install' q` becomes a false `install` destination.
The shipped code is correct.

**Grade:** MEDIUM, as bound; the skeptic lowered it from high because it is a regression gap.

**Fix (judged sound):** add SW86 rows that deny `sudo cp a @`, `xargs touch @` and `git mv a @`, and that admit `grep -n 'install' @` and `grep -n "install" @`.
Observe them red under the head-only mutant and under the dequoted-word mutant.

**Left-shift:** `class:observed-by-claim-no-arm-discharges`, with the rows standing in the `scratch-guard self-test` leg.

### M4. The bare `-I` row cannot fail (finding 12)

**Where:** the row at `tools/hooks/scratch-guard.test.sh@346ebb16:1678`.
The code it should hold is the `-I` consumption at `tools/hooks/scratch-guard.js@690899c6:617`.

**What is wrong:** the row's command is `perl -I lib -pi -e 1 x.py`.
With the consumption line removed, and at the base, it still reads `x.py:perl -i`, because `lib` fills the script slot instead.
TOOL-dBoundRoles-92 AC1 says the row is red when a detached `-I` value is read as the script, and this row does not observe that.

**Consequence:** the detached-value half of round 1's item M1 is unverified.
A regression would refuse a role's ordinary command again with the suite green.

**Grade:** MEDIUM, as bound.

**Fix (judged sound):** replace the command with, or add, `perl -I lib -pi s/a/b/ x.py`, wanting `x.py:perl -i`.
Observe it red by removing line 617: the mutant and the base both return `s/a/b/` beside `x.py`.

**Left-shift:** `class:fixture-passes-by-finding-nothing`, with the row standing in the `scratch-guard self-test` leg.

### M5. The quoted-arrow row does not hold the escaped-quote reading of S6 (finding 13)

**Where:** the row at `tools/hooks/scratch-guard.test.sh@346ebb16:1718`.
The code it should hold is `readWordText`, at `tools/hooks/scratch-guard.js@690899c6:450`.

**What is wrong:** TOOL-dBoundRoles-86 S6 reads a double-quoted word without the backslash of an escaped quote.
With `readWordText` keeping the backslash, the row stays green, because the body still blanks its quoted run.

**Consequence:** under that mutant, `bash -c "sed -i s/a/b/ \"q.py\""` goes from `q.py` to `\` and `q.py\`, and `bash -c "echo x > \"q r\""` from `q r` to `\`.
A `-c` body with quoted operands can regress to a verdict on a word that is not its target, the class round 1's B1 closed.
The shipped code is correct.

**Grade:** MEDIUM, as bound.

**Fix (judged sound):** add `scan_targets` wanting `q.py:sed -i` over `bash -c "sed -i s/a/b/ \"q.py\""`, and one for the redirect into a quoted word, `bash -c "echo x > \"q r\""`.
Observe both red by keeping the backslash.

**Left-shift:** `class:fixture-passes-by-finding-nothing`, with the rows standing in the `scratch-guard self-test` leg.

### M6. The new PowerShell reading has almost no arm (finding 14)

**Where:** the PowerShell branch of `buildCommandView`, at `tools/hooks/scratch-guard.js@690899c6:393`.
The `tool` is passed by `checkRoleGate`, at `tools/hooks/scratch-guard.js@690899c6:2630` and `tools/hooks/scratch-guard.js@690899c6:2631`, and the `-c` body clears it at `tools/hooks/scratch-guard.js@690899c6:2359`.

**What is wrong:** six parts of the reading can each be removed with every fold row green.
They are the backslash-before-quote rule, the `<# #>` blanking, the merge of `*>&1`, the open-quote token, the `tool: undefined` of a `-c` body, and the `tool` passed to the gate and poll arms.
No PowerShell row of the suite holds a backslash-quote or a block comment.
The backtick continuation does have a row.

**Consequence:** dropping the backslash rule takes `ls "C:\x\"; touch q` from `q` to no target, so a write after a path ending in a backslash would be admitted unseen.
The poll arm on the same spelling with `sleep 30` gives P3 with the tool and nothing without it.
The shipped code is correct.

**Grade:** MEDIUM, as bound.

**Fix (the skeptic's class-level fix):**

1. Add the SW86 PowerShell deny row `ls "C:\x\"; touch @`.
2. Add two `run_role_bash` PowerShell rows whose gate runner and whose `sleep 30` follow a `"C:\x\";` word.
3. Add PowerShell `scan_targets` rows: a multi-line `<# x\n y > f\n#> ls` wanting none, `<# c #> touch q` wanting `q:touch`, and `mkdir d *>&1` wanting `d:mkdir`.
4. Add a PowerShell `cp a "C:\x\"` row for the open-quote token.
5. Add a PowerShell `bash -c` body holding a Bash-escaped quote before a write, for `tool: undefined`.
6. Observe each red under its own mutant.

The finder's proposal cures the cited instance alone: its `<# x > f #> ls` and `x *>&1` rows read none with and without the tool, and it proposes no row for the `-c` body.

**Left-shift:** `class:observed-by-claim-no-arm-discharges`, with the rows standing in the `scratch-guard self-test` leg.

### M7. The declaration verb's role refusal, non-git refusal and root resolution have no arm (finding 15)

**Where:** the role composition refusal at `tools/loop/loop_lib.py@46446b33:1521`, and the non-git refusal at `tools/loop/loop_lib.py@46446b33:1947`.

**What is wrong:** TOOL-dBoundRoles-91 S3 and S4 and its AC8 own four behaviours that no plant reaches.
They are the refused role composition, the non-git refusal, the working-directory default, and the toplevel resolved from a subdirectory.
Every verb call in the code passes `--root <toplevel>` over roles that compose, and `declaration-refused` reaches the item composition alone.
AC8 stands only as a one-off observation in the acceptance ledger.

**Consequence:** dropping the refusals check would hand out a partly composed role's allowance.
Using the raw path would make a subdirectory compose as unarmed, which is AC8's own red.
The `loop item kind` leg stays green in both cases.
The shipped code is correct.

**Grade:** MEDIUM, as bound.

**Fix (judged sound):** add two plants.
The first writes a role overlay that `compose_roles` refuses, and owes exit 1 with `the role composition does not read` and no JSON.
The second runs the verb with its cwd and `--root` at a subdirectory, owing the composed repository item, and at a non-git directory, owing `sits in no git work tree` and exit 1.
Stage them red by dropping the refusals check and by passing the raw path.

**Left-shift:** `class:observed-by-claim-no-arm-discharges`, with the plants standing in the `loop item kind` leg.

### M8. The `govkit selftest` guard misses the return-check files its new control reads (finding 16)

**Where:** the `govkit selftest` row, at `tools/govkit/registry.toml@0d6b082f:797`.
The control is in `check_stop_replay`, at `tools/govkit/selftest.py@daadc481:3320`.

**What is wrong:** TOOL-dBoundRoles-92 S5 added a positive control that reds when the installed return-check shim grades nothing.
The leg that runs it guards `govkit/`, `hooks/kit.toml`, `settings-merge.py`, `codebase-map/kit.toml` and `process-monitor/census.py`, and no path of the roles kit.
The `--legs-for` probe lists no `govkit selftest` leg for `tools/roles/return-check.sh` or `tools/roles/handoff.py`.
The narrow row stands at the base, but this fold put the control behind it and widened sibling guards of the same class.

**Consequence:** an edit to the shim alone, such as one that ends it in `exit 0`, skips the check built to catch it, and a guarded bar stays green.
A `GATE_FULL=1` run still reaches it.

**Grade:** MEDIUM, as bound.

**Fix (judged sound):** add `{prefix}/roles/return-check.sh`, `{prefix}/roles/return-check.fragment.json`, `{prefix}/roles/handoff.py`, `{prefix}/roles/roles_lib.py` and `{prefix}/policy/` to the row's guard, or `{prefix}/roles/` and `{prefix}/policy/`.
Re-render `tools/gate-legs.json` with `leg_factory.py --write`.
Confirm with the `--legs-for` probe that the leg appears under `tools/roles/return-check.sh`.

**Left-shift:** `class:held-suite-guard-misses-a-sibling-kit`, checked by the `--legs-for` probe at the fold.

### M9. The `spawn-guard self-test` guard misses the index and the harnesses its suite reads (finding 17)

**Where:** the `spawn-guard self-test` row's guard, at `tools/govkit/registry.toml@0d6b082f:1226`.
The rows that read the missing files are at `tools/roles/spawn-guard.test.sh@cc5d39e3:1358`, `tools/roles/spawn-guard.test.sh@cc5d39e3:1365` and `tools/roles/spawn-guard.test.sh@cc5d39e3:1394`.

**What is wrong:** TOOL-dBoundRoles-92 S10 says this row guards the files its suite reads, and TOOL-dBoundRoles-88 assigns `.claude/roles.json` and the declared harnesses to it through round 1's item M10.
The built guard lists neither, apart from `spec-audit-optin.js`.
The BR88 rows of this range read the real index and copy and scan each declared harness.
The `--legs-for` probe lists no `spawn-guard self-test` row for `tools/workflows/unattended-build.js` or `.claude/roles.json`.
AC16 names four other paths, so it passes with the gap standing.

**Consequence:** an edit to a harness or to the index skips the real-harness rows.
A harness with a nested `workflow()` call by variable, an unlisted path, or a trailing comment spelling `workflow(` can land.
Every later Workflow call to it is then refused, because `checkHarnessClosure` refuses what it cannot place.
The call-time refusal fails closed, so the cost is a stuck harness.

**Grade:** MEDIUM, as bound.

**Fix (judged sound):** add `.claude/roles.json` and `{prefix}/workflows/` to the row's guard, the second replacing the single `spec-audit-optin.js` entry.
Re-render `tools/gate-legs.json` with `leg_factory.py --write`.
Confirm the leg under both paths with the `--legs-for` probe.

**Left-shift:** `class:held-suite-guard-misses-a-sibling-kit`, checked by the `--legs-for` probe at the fold.

## Dispositions

| id | item | disposition |
|---|---|---|
| 6 | M1 | class:a-view-fix-trades-one-blindness-for-another |
| 10 | M2 | class:observed-by-claim-no-arm-discharges |
| 11 | M3 | class:observed-by-claim-no-arm-discharges |
| 12 | M4 | class:fixture-passes-by-finding-nothing |
| 13 | M5 | class:fixture-passes-by-finding-nothing |
| 14 | M6 | class:observed-by-claim-no-arm-discharges |
| 15 | M7 | class:observed-by-claim-no-arm-discharges |
| 16 | M8 | class:held-suite-guard-misses-a-sibling-kit |
| 17 | M9 | class:held-suite-guard-misses-a-sibling-kit |

review-shape kind=diff-review round=2 intensity=full at=synth raw=17 confirmed=9 refuted=8 merged=0 unverified=0 blocker=0 high=0 medium=9 low=0 agents=11 out-tokens=130946 trigger=owed shape=- efforts=- role-sha=-
review-round round=2 limit=3 prior=10 count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/hooks/scratch-guard.js@690899c6:2399 | high | - | refuted | PRE-EXISTING. The behaviour is real at head. At f3ec096a8, scanCommandHeads (line 2257) already calls buildCommandView before the same comment regex. I ran base and head side by side: `# don't\ncp a tools/x` and `# don't\necho x > tools/F` give no target in both, and `# don't\nbash tools/run-gates/run-gates.sh` gives no head in both. The `# it's\n...` trailing twin gave base only a junk word (`its\necho x > tools/F`). That was an accident of B1's raw operand walk and never resolved to tools/F. The unit-86 spec keeps string and comment blanking 'as it does'. Fix: it cures `#` comments, but a multi-line PowerShell `<# it's #>` block still opens a quote. | instance | - | - |
| 2 | security | tools/hooks/scratch-guard.js@690899c6:393 | medium | - | refuted | PRE-EXISTING. Base and head agree on each probe. The PowerShell here-string holding `don't` piped to Set-Content gives no target in both, and its `dont` twin gives tools/F in both. `"a`"b" > tools/F` gives no target in both. Base buildCommandView had no backtick or here-string reading either. The fold's PowerShell mode only drops the backslash escape and did not introduce or newly expose this. | sound | - | - |
| 3 | correctness | tools/hooks/scratch-guard.js@690899c6:2399 | blocker | - | refuted | PRE-EXISTING. I probed base and head with real backslashes. `# don't\ncp`, `ls # don't\nsed -i`, `echo it\'s > tools/x`, `grep 'it'\''s' f\nsed -i`, PowerShell `# don't\nSet-Content` and `<# it's #>\nSet-Content` give no target at either sha. The quote pairing without an outside-quote backslash, and the order before comment blanking, are the same at f3ec096a8. B1 covered raw operand and redirect reading, not quote pairing. | sound | invariant-held-on-one-admission-path | - |
| 4 | correctness | tools/hooks/scratch-guard.js@690899c6:354 | high | - | refuted | PRE-EXISTING. readHeredocBodies and its opener regex are untouched by the diff. `grep -q a <<<word\ncp a tools/x` and `(( n = 1<<k ))\ncp a tools/x` give no target at both base and head, so the write was equally hidden before the fold. | sound | - | - |
| 5 | correctness | tools/hooks/scratch-guard.js@690899c6:697 | medium | - | refuted | Pre-existing. I loaded the base and head scratch-guard.js and ran both. The probe with a quoted directory ending in a backslash before WriteAllText returns [] at the base and [] at head, and the plain WriteAllText call is found in both. `const view = buildCommandView(cmd)` and the opener scan after it are the same bytes at the base (lines 547-548). The fold neither introduced nor widened this miss. It threaded the tool into a different scan and left this one as it was. | instance | two-readers-of-one-config-one-re-derived | - |
| 6 | correctness | tools/hooks/scratch-guard.js@690899c6:236 | medium | medium | confirmed | Confirmed only for the in-place part, which this fold introduced. With tool PowerShell, `{ sed -i s/a/b/ tools/x }`, `if ($c) { sed -i s/a/b/ tools/x }` and `{ perl -pi -e s/a/b/ tools/x }` return [] at the base. At head they return tools/x plus a phantom target `}`. TOOL-87 steps `{`, and scanInPlaceOperands then takes the closing brace as a file. PowerShell needs no `;` before `}`, so a permitted in-place edit is refused over a file nobody writes. It fails closed and adding `;` avoids it, so the effect is contained. The cp destination `}`, the Set-Content extra `}` and the glued-block miss are identical at the base, so they are pre-existing. The header's escape list names no brace case. The fix splits segments in scanCommandHeads' `seg`, but scanRedirects runs first on the unsplit view, and `{echo a >tools/x}` gives `tools/x}` in both trees, so redirect words keep the brace. | instance | - | class:a-view-fix-trades-one-blindness-for-another |
| 7 | correctness | tools/hooks/scratch-guard.js@690899c6:263 | low | - | refuted | Pre-existing. `perl -d:Trial -e1 tools/x` returns the `perl -i` target tools/x at the base and the same at head. The fold fixed the M1 switches its spec listed (MmIFCDxV) and did not change how `-d:` reads. It neither introduced this misread nor made it reachable. It is also a fail-closed false refusal on a rare debugger spelling. | sound | - | - |
| 8 | seams | tools/hooks/scratch-guard.js@690899c6:2397 | high | - | refuted | Pre-existing. The behaviour is real: `# don't` followed by cp, tee, sed -i or a redirect returns [] and the gate runner yields 0 heads. I ran the base and head modules side by side and both give the same answer on those probes, and the finder concedes it for the two write probes. At the base scanCommandHeads (line 2257) also calls buildCommandView before the comment replace, so the order is unchanged. The base's checkShellWrites and role-gate arms had the same exposure, so the fold made nothing reachable. Round 1's B1 covers operands, redirect spellings and trailing comments read as operands. It does not list an apostrophe in a comment opening a quoted run. For the trailing-comment form `cp a tools/x # don't`, the fold improved the result: the base gave `dont` and head gives tools/x. | instance | a-pair-exists-and-it-is-the-wrong-one | - |
| 9 | seams | tools/hooks/scratch-guard.js@690899c6:697 | medium | - | refuted | Pre-existing. I compiled both blobs in memory and ran the PowerShell command with a quoted path ending in a backslash followed by the [IO.File] write call. Head f3ec096a's successor 3c9b6ad0 returns [], and base f3ec096a also returns []. The line `const view = buildCommandView(cmd)` stands unchanged from base line 548, and no target base read is lost. Deviation 861 states the quoting repair for targets the base reads, and it lists the command heads, checkRoleGate and checkPollWait. The proposed one-line change does make the probe return a.py, but the defect is outside this diff. | sound | kit-argument-dropped-at-an-inner-call | - |
| 10 | verification | tools/hooks/scratch-guard.js@690899c6:2406 | high | medium | confirmed | Cutting the recursive push at tools/hooks/scratch-guard.js@690899c6:2406 turns `x=$(touch q)`, `echo $(echo x > q)`, `cat <(touch q)` and the nested form from q to []; base read all four. I read the BR86 rows, the SW86 family, the BR87 program and the older touch/tee/mkdir/cp rows: none writes inside an unquoted substitution. The only substitution rows are `cp $(echo a) d`, its family twin and `tee >(cat) <(y)`, which hold no inner write. S5 is therefore unguarded. The shipped code is correct, so the consequence is a missing regression arm, hence medium. Fix: the deny rows kill the cut-push mutant, but the nested `$(echo $(touch @))` row does not kill removal of the outermost pop. With the pop gone both spans are still scanned and the target still denied; only the text after the span is misaligned. | instance | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 11 | verification | tools/hooks/scratch-guard.js@690899c6:540 | high | medium | confirmed | The head-only mutant turns `sudo cp a q`, `xargs touch q` and `git mv a q` into [], while `if cp a q` stays read because reserved words are now stepped. Comparing the dequoted word makes `grep -n 'install' q` a false install destination. The suite has no sudo, xargs or `git mv` command and no quoted write word as an argument to another command; every other write-word row has it at the head. AC1 of the spec names `sudo cp` and the grep case, yet no standing arm holds either. The code is correct today, so this is a regression gap: medium. The proposed rows discriminate both mutants. | sound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 12 | verification | tools/hooks/scratch-guard.test.sh@346ebb16:1678 | medium | medium | confirmed | With the `-I` consumption line removed, and also at base, `perl -I lib -pi -e 1 x.py` still returns x.py:perl -i: `lib` fills the script slot, so the row cannot fail. Spec 92 AC1 says it is red when a detached -I value is read as the script, which this row does not observe. `perl -I lib -pi s/a/b/ x.py` gives x.py alone at head and `s/a/b/` plus x.py under both the mutant and base, so the proposed fixture discriminates. The effect is limited to one unverified perl option form. | sound | - | class:fixture-passes-by-finding-nothing |
| 13 | verification | tools/hooks/scratch-guard.test.sh@346ebb16:1718 | medium | medium | confirmed | I mutated a copy of the hook so readWordText keeps the backslash. The row's command read [] under both copies, so the row does not hold S6. `bash -c "sed -i s/a/b/ \"q.py\""` went from [q.py] to [\, q.py\], and `bash -c "echo x > \"q r\""` from [q r] to [\]. The only other rows with an escaped quote in a -c body are none. The spec's S6 is new in this fold, and the shipped code is correct, so the effect is a coverage gap. The proposed rows differ under the mutant, so they go red. | sound | - | class:fixture-passes-by-finding-nothing |
| 14 | verification | tools/hooks/scratch-guard.js@690899c6:393 | medium | medium | confirmed | Dropping `tool !== 'PowerShell'` from buildCommandView turns `ls "C:\x\"; touch q` from [q] into [], a lost target. checkPollWait on the same spelling with `sleep 30` gives P3 with the tool and null without it. The PowerShell rows in the suite are 516, 517, 1510, 1520, 1713, 1870, 1885 and 1886, and none holds a backslash-quote or a block comment. The PowerShell reading and both tool arguments are new in this diff. The backtick continuation does have a row (1870), which narrows the claim slightly. The fix only partly works: two of its rows, `<# x > f #> ls` and `x *>&1`, read [] with and without the tool, so they are vacuous. It also proposes no row for the -c body's `tool: undefined`. | instance | - | class:observed-by-claim-no-arm-discharges |
| 15 | verification | tools/loop/loop_lib.py@46446b33:1521 | medium | medium | confirmed | A grep finds both refusal strings only at their definition sites (tools/loop/loop_lib.py@46446b33:1521 and :1947). run_scratch_declaration always passes `--root <top>`. `declaration-refused` asserts only the item composition's refusal. read_item_declaration also passes --root. AC8 appears only as a one-off observation in the acceptance ledger. The code is correct as shipped, so this is a coverage gap over new S3 and S4 behaviour. The proposed plants exercise each branch. | sound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 16 | intent | tools/govkit/registry.toml@0d6b082f:797 | medium | medium | confirmed | The --legs-for probe lists no govkit selftest leg under return-check.sh or handoff.py. The guard in registry.toml names govkit/, hooks/kit.toml, settings-merge.py, codebase-map/kit.toml and census.py only. The narrow guard row stands at base, but this fold put the M5 positive control there as the left-shift gate for an edit to the shim. The fold also widened sibling guards for the same class (deviation 921 item 8) and left this row out. An edit to the shim alone therefore skips the new check on a guarded bar. A GATE_FULL run still reaches it, so the effect is contained. The fix adds the files the control reads. | sound | held-suite-guard-misses-a-sibling-kit | class:held-suite-guard-misses-a-sibling-kit |
| 17 | intent | tools/govkit/registry.toml@0d6b082f:1226 | medium | medium | confirmed | Observed: the guard at tools/govkit/registry.toml@0d6b082f:1226 lists neither .claude/roles.json nor any harness except spec-audit-optin.js. My --legs-for probe over tools/workflows/unattended-build.js and .claude/roles.json printed no `spawn-guard self-test` row under either; spec-audit-optin.js printed one. The BR88 rows this range added (tools/roles/spawn-guard.test.sh@cc5d39e3:1358, 1365, 1394) read $ROOTDIR/.claude/roles.json and copy and scan each declared harness from the real tree. The index declares three, all under tools/workflows/. TOOL-dBoundRoles-88's non-goal says the new arm reads the declared harnesses and .claude/roles.json, 'which that list does not hold', and assigns the guard list to item M10. TOOL-dBoundRoles-92 S10 states the goal as the files the suite reads, but its position text and AC16 omit those paths, so AC16 passes with the gap. The unattended-build suite only names the guard and does not replace these rows. Contained: a skipped leg lets a bad harness land, but the call-time refusal fails closed, so the cost is a stuck harness. Fix: every declared harness is under {prefix}/workflows/, and other rows already use guard entries outside the prefix (the .claude/ entry in the lexicon kit.toml), so both additions are legal and cover the inputs the range added. | sound | held-suite-guard-misses-a-sibling-kit | class:held-suite-guard-misses-a-sibling-kit |
