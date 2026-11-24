**Serves:** diff-review TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85

# dBoundRoles — Tier-2 CLOSING DIFF review, round 1

*2026-11-24. The subject is the cumulative diff of the unattended build dBoundRoles, 64 units (DERIVED from its roster), every one CLOSED.*
*Roles: finders gov-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.*
*Intent: 1 spec document supplied as `specs`, beside the range's commit messages.*
*Checklist: 125 items, acquired by the harness from `--for-diff 8b8b1374c4fc89be2ae3a5aae88dafd74e6acd8e..f3ec096a83f63cac1ff056b7df11820845fb722b`, each assigned to exactly one of 5 lenses, 25 to each of security, correctness, seams, verification and intent.*
*By design: the caller's byDesign, and 2 invariants from the checklist's by-design block.*
*Security model: the hooks are fail-closed and advisory against an agent, not against an adversary with shell access.*
*Every citation is blob-pinned as `<path>@<sha8>:<line>` at the reviewed head.*

**Range reviewed: `8b8b1374c4fc89be2ae3a5aae88dafd74e6acd8e...f3ec096a83f63cac1ff056b7df11820845fb722b`**

**Round: 1.**

## Verdict: BLOCKED

One item is a BLOCKER, and it comes from raw finding 27.
The shell-write arm of scratch-guard.js judges a role's command on the wrong target, so ordinary spellings write a file the role may not write.
The same cause refuses ordinary scratch commands of the read-only roles.
Five items are HIGH.
H1 is a second, separate hole in the same arm.
H2 lets an unlanded nested review harness run under a landed parent.
H3 makes a sent-back orientation return unplaceable.
H4 re-runs stages whose side effects have already landed.
H5 cuts work orders from gov's rows alone.
Of the 14 MEDIUM items, 10 (M5 to M14) are missing or vacuous test coverage over code that reads correctly today, and one of those (M6) also carries a small product defect.
I recommend folding the BLOCKER and the HIGHs before the landing.
The MEDIUM arms and the LOWs can be folded with them or filed.
Per M8, a fold earns a round 2 over the fold itself.

## Review shape

Intensity full, raw 30, confirmed 30, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 6 | 6 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 5 | 5 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 11 | 11 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 24 items (1 blocker, 5 high, 14 medium, 4 low).
Adjudicated tally by raw confirmed finding: 30 (1 blocker, 9 high, 16 medium, 4 low).
The two tallies differ because four items hold more than one finding: B1 holds 2, 3, 27 and 28, H3 holds 5 and 29, H4 holds 6 and 11, and H5 holds 9 and 13.
Every confirmed finding takes its binding grade; none was regraded here.
No finding was refuted, so no twin is flagged.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 13 judged sound, 4 judged UNSOUND (findings 5, 9, 18, 27), 13 judged INSTANCE-ONLY, 0 none proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing, so each such item carries the skeptic's class-level fix.
- An UNSOUND fix is never written below; the skeptic's corrected fix stands in its place.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 5 RE-GRADED by the skeptic (findings 3, 5, 13, 16, 30).
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 0. Same-address pairs shown: 0.
- Dispositions: unclassed is `refuse`; 125 class slugs handed; 224 leg names read from tools/gate-legs.json.

Every count that would mark the run incomplete is zero.

## BLOCKER

### B1. The shell-write arm reads its operands and redirects off raw text, so a role's write is judged on the wrong target (findings 2, 3, 27, 28)

**Where:** `scanWriteTargets`, in `tools/hooks/scratch-guard.js@f71f3b8c:553`.
The redirect pattern `REDIRECT` is at `tools/hooks/scratch-guard.js@f71f3b8c:422`.
The last-argument walk is at `tools/hooks/scratch-guard.js@f71f3b8c:605`, and the any-argument walk stands above it.
The consumer is `checkShellWrites`, at `tools/hooks/scratch-guard.js@f71f3b8c:2116`.

**What is wrong:** TOOL-dBoundRoles-7 S3 says a role agent's shell write meets the verdict an Edit of the target meets.
The scanner predates this diff, but its use as a role boundary is new.

- The operand walk of `cp`, `mv`, `install` and `rsync` ends its segment only at `;`, `|` or `&`. It keeps redirect words, the next line's command and a trailing comment as operands, and the last of them becomes the destination (findings 3 and 27).
- The operand walk of `tee`, `touch` and `mkdir` takes the same stray words as targets (findings 3 and 28).
- `REDIRECT` needs a separator before the operator and knows neither `>|` nor `&>>` (findings 2 and 27).

The header's list of what escapes names none of these spellings.

**Consequence, admitted writes (probed at head by the skeptics):**

- For gov-spec-writer, `cp /c/Temp/b.py tools/x.py` is denied. The same command with ` 2>/dev/null`, ` 2>&1` or a following `echo hi` line is admitted with only the `allowance not located` witness.
- For gov-skeptic, `echo a > tools/x.py` is denied and `echo a>tools/x.py` is admitted.
- `cat>tools/f.py` and `echo x >|tools/f.py` are admitted for both gov-skeptic and gov-reviewer.
- `&>>` yields the mangled target `>tools/f.py`, and `>&file` is admitted.
- The allowance join of a builder is bypassed the same way.

**Consequence, false refusals (probed at head):**

- For gov-skeptic, `mkdir -p /c/Temp/x 2>/dev/null`, `mkdir -p /c/Temp/x` followed by a `git status` line, `cp tools/a.py /c/Temp/b.py 2>/dev/null`, and that `cp` followed by a `grep` line are each denied.
- These are ordinary commands of the `writes = none` roles, and the remedy printed is addressed to the driver.

**Grades:** 27 binds BLOCKER, and 2, 3 and 28 bind HIGH.
Finding 3 was raised from medium to high by its skeptic.

**Fix (corrected by the skeptic of 27, with the class-level fixes of 2, 3 and 28):**

1. Read operands per simple command from `scanCommandHeads`' argv, not from a bounded raw-text walk. That reader is continuation-aware, newline-bounded, strips comments and drops redirections with their operands, and later commands fall outside it. Feed both the any-argument and the last-argument shapes from it.
2. Skip redirect operators with their words, and discard continuation words, before choosing operands. Take the last non-option operand for `cp`, `mv`, `install` and `rsync`.
3. In the blanked view, match `&>>?`, `>>?[|]?`, `<>` and `>&` followed by anything but a digit or `-`, after any character, with the fd prefix optional. Exclude only process substitution `>(`, and comparisons inside `[[ ]]` or `(( ))`. Read the target after the whole operator.
4. Quoted arrows are already blanked, so do not exclude a preceding `=` or `-`. The exclusion of `=>` and `->` in the corrected fix of 27 conflicts with this: finding 2's skeptic showed that `echo a=>f` and `echo -> f` are real redirections. Follow finding 2's skeptic on that point.
5. Arms to see red first: trailing `2>/dev/null`, trailing `2>&1`, a following command line, a backslash-continued destination, a trailing comment, glued `a>path`, `cat>path`, `>|`, `&>>` and `>&file`, each graded for a role outside the target's class.
6. Admit arms: `mkdir -p <scratch> 2>/dev/null`, a two-line `mkdir` then `git status`, `cp` to scratch with `2>/dev/null`, `2>&1`, and a quoted `a->b`.

The finder proposals of 2, 3 and 28 cure the cited instances alone, and the finder proposal of 27 was rejected.

**Left-shift gate:** `scratch-guard self-test`. Add a table-driven family over spelling, role and expected verdict, with each deny row paired to its admit row, so a new spelling owes both.

## HIGH

### H1. In-place writes behind a shell reserved word yield no target (finding 1)

**Where:** `tools/hooks/scratch-guard.js@f71f3b8c:553`, where `scanWriteTargets` calls `scanCommandHeads(cmd, 0, { inline: true })`.
`SHELL_RESERVED_WORDS` is at `tools/hooks/scratch-guard.js@f71f3b8c:2191`.

**What is wrong:** the call omits `reserved: true`, so a `sed -i`, `perl -i`, interpreter write or `git apply` behind `then`, `do`, `else` or `{` heads no recognised simple command and yields no target.
The sibling reader `checkPollWait` passes `{ reserved: true }`.
The header's list of what escapes names `xargs` and `sudo`, not reserved words.

**Consequence:** `sed -i s/a/b/ tools/hooks/scratch-guard.js` is denied for gov-skeptic, and the same command inside `if true; then ...; fi` or `{ ...; }` is admitted.
A role declaring writes `none` or `review` edits any product or spec file in place, and a builder leaves its allowance.

**Fix (class-level, the skeptic's):** pass `{ inline: true, reserved: true }` in `scanWriteTargets`.
Also step `coproc` and `function <name>` in the reserved-word prefix loop.
`coproc sed -i` and `function f { sed -i ...; }` were probed as admitted and would stay so without that step.
Add deny arms for both beside the `then`, `do`, `else` and `{` arms, and see them red first.
The finder's proposal cures the cited instance alone.

**Left-shift gate:** `scratch-guard self-test`, with one deny arm per entry of `SHELL_RESERVED_WORDS` plus `coproc` and `function`, driven from the list so a new entry owes an arm.

### H2. Harness admission holds only the top-level harness to its landed blob (finding 4)

**Where:** `tools/roles/spawn-guard.js@139eada2:583`, where `checkHarnessLanded(entry, root)` is called.
The nested call is at `tools/workflows/unattended-build.js@4ecf3bb3:1831`.

**What is wrong:** `checkHarnessLanded` has one caller, `checkHarnessCall`, which passes the top-level `scriptPath` entry.
`unattended-build.js` then runs `workflow({ scriptPath: 'tools/workflows/tier2-review.js' }, ...)`, a runtime call inside the script that no PreToolUse hook sees.
The file's stated ceiling names agents a harness spawns through `agent()`, not a nested `workflow()`, and TOOL-dBoundRoles-25 names no such exception.

**Consequence:** with `unattended-build.js` at its landed bytes and `tier2-review.js` edited in the working tree, the edited review harness runs and its verdict is taken as landed-harness evidence.
The S3 invariant, that an edited harness never runs before the bar has read it, does not hold on the spec-audit path.

**Fix (judged sound):** hold the transitive set.
When admitting an entry, also require the landed blob for each declared harness that the script's text names in a nested `workflow({ scriptPath: '<declared harness>' ...` literal, or record nested harnesses per entry in roles.json and compare each.
Add an arm with `unattended-build.js` landed and `tier2-review.js` edited that must refuse.

**Left-shift gate:** `spawn-guard self-test`, with an arm that greps every declared harness for a nested `workflow(` literal and requires the admission to have held each callee.

### H3. The send-back orders a JSON return that `place` cannot read (findings 5, 29)

**Where:** `tools/roles/handoff.py@d123282e:1926`, in `run_return_check`.
The other reader is `read_scout_return`, at `tools/loop/placement.py@95e535e7:488`.

**What is wrong:** the return check's block reason orders every role to answer with one corrected `json` block and no field the template does not name.
`read_scout_return` parses bare `key: value` lines only.
The gov-orienter template does not name `build`, `breakpoint` or `playbook`, so a JSON return naming a build fails `check_return`, while the `key: value` reader silently ignores the same keys.
`place --agent` requires the file to equal the agent's last text byte for byte, so the driver cannot convert it.

**Consequence:** an orienter whose first placement return misses one field is sent back, answers in JSON as told, passes `check_return`, and is then refused by `place` at line 1.
The skeptic of 5 graded it medium because the refusal is loud, `--agent` is optional and a respawn recovers.
The skeptic of 29 graded it high.
Each finding keeps its binding grade.

**Fix (the skeptic's corrected fix of 5, which agrees with the sound fix of 29):** give gov-orienter's return template `build:text?, playbook:text?, breakpoint:text?` and re-render.
Make `read_scout_return` accept the fenced or whole JSON object that `check_return` graded (`extract_return_object`) as well as bare `key: value` lines.
Add a placement plant of a JSON return naming a build, put through `check-return-file` and `place`, and an arm where an orienter return lacks `outcome`, the corrected JSON the reason orders is supplied, and `place` exits 0.
The finder's rejected proposal for 5 is not written here.

**Left-shift gate:** `loop placement fixtures`, with one end-to-end plant that feeds the send-back text's own shape to every reader of that role's return.

### H4. `runWithRetries` re-runs stages whose effect has already landed (findings 6, 11)

**Where:** `tools/workflows/unattended-build.js@4ecf3bb3:2110`, the `writeRound` record stage.
The same wrapper covers the spec commit at `tools/workflows/unattended-build.js@4ecf3bb3:1382` and disposal at `tools/workflows/unattended-build.js@4ecf3bb3:2650`.
The builder in `tools/workflows/unattended-unit.js@ee9e2dbb:525` is re-run the same way.

**What is wrong:** the base called `agent()` once for the round record.
The head re-spawns the identical prompt whenever the return is null, including when the agent had already run `unattended.sh --review`.
`verb_review` refuses a repeat only where a terminal row stands; any other repeat appends a row and draws the review-round budget.
Unit 5 and deviation 53 list the wrapped stages but never consider a stage whose effect already landed.

**Consequence:** the policy default of `roles.retries` is 3, and the kit's verbs guide tells the unattended caller to pass it.
A record agent that runs the verb and then dies double-records, so a CONVERGING loop can end NON-CONVERGENT, BOUNDED or CEILING on one real audit.
If the first row was terminal, the re-run returns `terminalSubject` and the harness throws a misleading re-key error.
Disposal can promote the same findings twice.
The builder can re-run after a commit, a `--dispatch` and a `--brief`.
The path needs a null after the side effect, so it is narrow.

**Fix (class-level, both skeptics):** re-run only read-only or idempotent stages, such as the checklist, probe and blob-resolve stages.
Call `agent()` once for the round record, the spec commit and disposal in `unattended-build.js`, and for the builder in `unattended-unit.js`, so a null stops at the existing throws.
Apply the change to the templates and the renders alike.
The alternative is for each re-run prompt to read back first what the earlier attempt landed (the run-state row of the round, the spec commit, the promoted specs, a `Pass:` commit since the base) and return that instead of repeating it.
Add a null-after-write arm for each stage.
The finder proposals cure the one cited call alone.

**Left-shift gate:** `unattended-build self-test`, with a stub whose first call performs the write and returns null and an assertion of exactly one row. A static check that a stage wrapped in `runWithRetries` carries no driver-write verb would grade the class.

### H5. The `declaration` verb reads gov's rows alone, so work orders ignore the overlay (findings 9, 13)

**Where:** `tools/loop/loop_lib.py@b14af4ca:1898`, in `run_declaration_command`.

**What is wrong:** the verb reads `read_items(kit_dir)`, gov's own `loop.toml` rows, and `read_outcome_set(kit_dir, tag)`, with roles from gov's `load_roles`.
None of them takes a root or a revision.
This same diff composes and grades repository items that name `role:` actors, and admits item amendments and actor patches.
`handoff.py render --item` reaches this verb through `read_item_declaration` and passes only `--item`.

**Consequence:** a repository item such as `item.build.adopter.ship` passes the item check, but `render --item` exits 1 with `no [[item]] row declares`, so no work order can be cut for it.
An admitted amendment of a gov item's inputs, outcomes or witness is dropped, and the work order hands the pre-patch values.
An admitted actor patch is ignored, and the order is still cut for gov's actor.
No tree carries such an overlay today, so the path is narrow.

**Fix (corrected and class-level, both skeptics):** resolve the row from the composed item kind for the caller's repository, through `loop_items.read_composition` or `read_composed_items(root)` with a lazy import, and pass `--root` from `handoff.py`.
Derive outcomes from that composed row through `derive_outcome_set`, not through `read_outcome_set(kit_dir, tag)`.
Fall back to `read_items` only when the composition is unarmed, and refuse when it refuses.
Resolve roles through `compose_roles`, and normalise an actor `role:adopter.<name>` to its slot with `roles_lib.derive_repository_slot` in the declaration's role lookup and in `handoff.py`'s actor compare.
Plant an adopter item, an inputs amendment and an actor patch.
The finder's rejected proposal for 9 is not written here, and the finder's proposal for 13 cures the cited instance alone.

**Left-shift gate:** `loop item kind`, with a join that renders a declaration for every item the composed kind admits in a fixture overlay.

## MEDIUM

### M1. A perl switch value containing `i` reads as `perl -i` (finding 7)

**Where:** `tools/hooks/scratch-guard.js@f71f3b8c:475`, in `scanInPlaceOperands`.

**What is wrong:** the cluster walk tests every letter of a perl short option for `i`, including the value of a value-taking switch.

**Consequence:** `perl -MList::Util=sum -ne print tools/x.py`, `perl -MTime::Piece -e 1 a.txt` and `perl -Ilib -ne print f` are refused as in-place writes for every `writes = none` role and every allowance-bound builder. The refusal is false, and fail-closed.

**Fix (judged sound):** for perl, stop the cluster walk at `M`, `m`, `I`, `F`, `C`, `D`, `x` and `V`, the rest of the word being the value, and count a detached value for `-I`. Add rows for `-MList::Util`, `-MTime::Piece` and `-Ilib` beside a real `-pi -e`.

**Left-shift gate:** `scratch-guard self-test`.

### M2. `sed -i --` takes the script as a file (finding 8)

**Where:** `tools/hooks/scratch-guard.js@f71f3b8c:468`, the `--` branch of `scanInPlaceOperands`.

**What is wrong:** the branch pushes every word after `--` as a file, though with no `-e` or `-f` seen the first one is the script.

**Consequence:** `sed -i -- s/a/b/ out.txt` reads as writing `s/a/b/` and `out.txt`, so a builder whose allowance covers `out.txt` is refused.

**Fix (judged sound):** on `--`, mark the options ended and continue the operand logic, so the first remaining word is consumed as the script while `script` is false. Add a row. It cures both sed and perl.

**Left-shift gate:** `scratch-guard self-test`.

### M3. The unit harness hands brief and spec text unfenced to a heading reader (finding 12)

**Where:** `tools/workflows/unattended-unit.js@ee9e2dbb:299`, in `HANDED`.

**What is wrong:** every other handed block in this build is fenced by `render_handed_fence`, and the readers depend on that. `HANDED` concatenates `briefFact.text` and `specFact.text` with no fence, and `print_input_facts` only trims blank edges.

**Consequence:** `readWorkOrderAllowance` walks the first user record of the transcript, so an unfenced `## Task` with `### allowance` inside a handed text becomes the builder's own allowance. Two such headings, or an unclosed fence, deny every shell write. 1668 of 7181 tracked prompts or specs already hold an unfenced `## Task`. The effect only narrows or denies. Quoted fact and marker lines also read as executor lines.

**Fix (judged sound):** fence each text in `HANDED` with a backtick run one longer than its longest run, minimum three, as `lib.render_handed_fence` does, either in `facts` or in the unit file. Probe: a fact text carrying `## Task` and `### allowance`, read through `readWorkOrderAllowance`, must return no allowance.

**Left-shift gate:** `unattended-build self-test`, with a hostile fact text through the harness's own assembly and the guard's reader.

### M4. `roles.retries` has no maximum, and every harness refuses a value above 4 (finding 14)

**Where:** `tools/policy/catalogue.toml@4d7897c8:273`.
The refusal is at `tools/workflows/unattended-build.js@4ecf3bb3:635`, and the unit and review harnesses carry the same check.

**What is wrong:** the catalogue declares `{ type = "retry-count", min = 0 }`. The harnesses refuse above `ATTEMPTS.length - 1`, which is 4, and tell the caller to pass what `policy.py get roles.retries` prints.

**Consequence:** a policy value of 5 works on the direct route, and every harness call following the documented instruction throws before its first agent. The error blames args rather than the policy key. The failure is loud.

**Fix (judged sound):** declare `max = 4` on `roles.retries` in the catalogue, or clamp to 4 with a log line in the harnesses. Add a check joining the catalogue max to each `ATTEMPTS` length.

**Left-shift gate:** `policy fixtures`, for the join between the catalogue row and the three `ATTEMPTS` arrays.

### M5. The return-check shim has no check that fails when it stops grading (finding 16)

**Where:** `tools/roles/return-check.sh@d775fbd8:214`.

**What is wrong:** the only harness that executes the shim is govkit's `check_stop_replay`, which requires rc 0, empty stdout and no record. Arm 22 of `render_agents.py` runs `handoff.py check-return` directly and never the shim.

**Consequence:** replace the last two lines with `exit 0`, misspell the verb, or redirect its stdout, and every suite stays green while no role agent's return is ever sent back. The shipped shim reads correctly today.

**Fix (judged sound):** in `check_stop_replay` or `adopt-roles.test.sh`, add a positive control. Pipe a marked direct-spawn payload with transcript `<session>/subagents/agent-x.jsonl` and a malformed return through the installed command, and assert a `decision: block` object, rc 0 and the record. See it red against a shim whose body is `exit 0`.

**Left-shift gate:** `govkit selftest`, or `roles adopter self-test`, with that control.

### M6. The typed-refusal reader has no check, and an untyped reason can read as typed (finding 17)

**Where:** `tools/loop/position.py@077196d1:488`, in `read_refusals`.

**What is wrong:** `REFUSAL_TAIL_RE` and the split of rule, remedy and actor are exercised by no plant; `run_refusal_plant` and the `frontier-refused` plant record only `--reason probe`. `render_position_lines` prints item, key and reason only. `write_refusal` validates only the typed flags, and `check_step_fields` refuses the separator only in item and step.

**Consequence:** a regex that never matches, or a deleted split, stays green, and the actor the driver routes on is lost from the text view. A plain `--reason "x · rule r · remedy m · actor owner"` reads back as a typed refusal whose actor was never checked.

**Fix (judged sound):** add a position plant that records a refusal with `--rule`, `--remedy` and `--actor` and asserts the three fields and the trimmed reason. Print the fields in the refusal line. Refuse an untyped reason that matches the tail, with its arm.

**Left-shift gate:** `loop position fixtures`.

### M7. `write_refusal`'s new refusals are mostly untested (finding 18)

**Where:** `tools/unattended/unattended.sh@d360a6b1:16891`.

**What is wrong:** `unattended.test.sh` covers a full set with actor `driver` and the bad actor `nobody`. No arm reaches a partial set, a separator-bearing rule or remedy, or either `build:<slug>` outcome.

**Consequence:** the non-empty, separator and `build:*` lines can each be deleted with every assertion green. A separator-bearing remedy then writes a row `REFUSAL_TAIL_RE` cannot split, and the typed route is silently lost.

**Fix (the skeptic's corrected fix):** use partial-set arms with a valid actor: `--rule` and `--actor driver` without `--remedy`, and `--remedy` and `--actor driver` without `--rule`. Add a full rule and remedy without `--actor`. Add a separator-bearing rule and a separator-bearing remedy, each with a valid actor. Add `--actor build:dX` admitted, and `build:` and `build:a/b` refused. Each refusal arm asserts its own message text, a non-zero exit and unchanged bytes.

**Left-shift gate:** `harness arms (fail branches armed or pinned)`, so each `_tw` line owes an arm, backed by the unattended driver's own suite.

### M8. Most refusals of `checkFraming` have no arm (finding 19)

**Where:** `tools/roles/spawn-guard.js@139eada2:545`.

**What is wrong:** the PF fixtures plant only `spawn-unframed`, `spawn-framed` and `spawn-framed-by-researcher`, and both deny plants stop at the heading count or the role. No fixture reaches the placement, spelling, missing-file or task-sha refusal, and line 560 has no failing fixture.

**Consequence:** deleting the task-sha comparison, the placement test or the path check stays green, and a handoff naming a stale or foreign render is then admitted unnoticed. The code reads correctly today.

**Fix (class-level, the skeptic's):** add one plant per refusal, each asserting its own text: two `framing:job` headings; zero and two `Framed by:` lines; a line before the block and one after it; a malformed spelling; a path outside `builds/<build>/prompts/` and one with `..`; a missing file; a file with zero markers and one with two; a mismatched task-sha. The finder's proposal cures the cited instance alone.

**Left-shift gate:** `spawn-guard self-test`, with a check that every literal refusal text of `checkFraming` occurs in the suite.

### M9. Two of `checkFactKeys`'s three source forms are untested (finding 20)

**Where:** `tools/roles/spawn-guard.js@139eada2:319`.

**What is wrong:** the function branches on three source forms, and only the repo-relative moved-file form has rows (BR13 AC3). The card re-cut, the absolute and `..` key, and the deleted source have none.

**Consequence:** a stale card fact, a key escaping the checkout, or a deleted source can be admitted if its branch breaks, with the suite green. These are unit 13's freshness guarantees.

**Fix (class-level, the skeptic's):** add `run_spawn` rows for each form: a card fact unchanged (admitted), changed, and one whose card is absent (both refused); a `..` key with slash and with backslash, a leading-slash key and a drive-letter key, each refused as naming no path inside the checkout; and a removed source file refused. Each asserts its own refusal text. The finder's proposal cures the cited instance alone.

**Left-shift gate:** `spawn-guard self-test`, with the same refusal-text coverage check as M8.

### M10. The spawn-guard leg's guard misses the files its suite reads (finding 21)

**Where:** `tools/gate-legs.json@fc85cb7a:3102`.

**What is wrong:** the guard lists `spawn-guard.js`, its fragment, its suite and `scratch-guard.js`. The suite also reads `roles/handoff.py` (TYPED_INPUTS against INPUT_NAMES), six policy kit files and `workflows/spec-audit-optin.js`. The replaced agent-cap leg listed `lib/` and the opt-in pack, and both were dropped.

**Consequence:** an edit to those files skips the only suite that compares the hook with them, and the leg reports `skip guarded`. A typed input added to `handoff.py` without the JS list makes the hook deny every such spawn. Remote CI runs GATE_FULL=1, which contains it.

**Fix (class-level, the skeptic's):** guard `{prefix}/roles/handoff.py` and `{prefix}/roles/roles_lib.py` (READ_FAMILIES feeds INPUT_NAMES), plus `{prefix}/policy/`, `{prefix}/workflows/spec-audit-optin.js` and `{prefix}/lib/`, beside the existing four rows. The finder's proposal cures the cited instance alone.

**Left-shift gate:** `gate-leg conformance`, deriving a held suite's guard from its `resolve_kit_dir` calls and redding on a sibling read the guard omits.

### M11. The return-check wiring arm is untested (finding 22)

**Where:** `tools/check-wiring.sh@d80db82f:1880`.

**What is wrong:** the diff adds the arm and its test suite never reaches it. `check-wiring.test.sh` holds neither `return-check` nor `SubagentStop`, and its roles fixture copies no fragment.

**Consequence:** dropping the arm, or misnaming its `only` filter so the loop matches nothing, prints nothing and stays green. An unwired return check looks identical to a passing one.

**Fix (judged sound):** add an arm that seeds the roles kit with `return-check.fragment.json` and `return-check.sh`. With settings lacking the SubagentStop entry expect `UNWIRED  roles` and exit 1; with it expect ok.

**Left-shift gate:** `check-wiring self-test`.

### M12. The fork-record registry arm passes on the degraded path (finding 23)

**Where:** `tools/memory-tree/check-memory-hygiene.test.sh@807b34a1:4725`.

**What is wrong:** the F6 arm accepts either the refusal line or the note `because no principle registry was read`. The engine prints that note for every failure of its inline reader and falls back to shape-only grading.

**Consequence:** a broken reader turns the registry half of check 12 off across gov while its only arm reads green.

**Fix (judged sound):** resolve the playbook kit's `principles.toml` in the test. Where it resolves, require the refusal line for F6 and fail on the note; accept the note only where it does not. Probe by renaming `tag = ` in the engine's regex.

**Left-shift gate:** `memory-hygiene self-test`.

### M13. The harness-run transcript lookup and its size bound are untested (finding 24)

**Where:** `tools/hooks/scratch-guard.js@f71f3b8c:2029`, in `readWorkOrderAllowance`; the over-bound deny is at line 2054.

**What is wrong:** every fixture writes `<session>/subagents/agent-*.jsonl`, so nothing reaches the `subagents/workflows/<run id>/` lookup or the 8 MiB TRANSCRIPT_READ_BOUND deny.

**Consequence:** harness-stage agents are the main unattended population. If the lookup breaks, their shell writes fall back to `allowance not located`, held to the class verdict alone, unseen. The over-bound deny can be removed unseen.

**Fix (judged sound):** add one fixture transcript under `sw7sess/subagents/workflows/wf_x/` with an allowance-out write expected to deny, and one first record over 8 MiB expected to deny naming the bound.

**Left-shift gate:** `scratch-guard self-test`.

### M14. The FORKED hold's fail-closed half is untested (finding 26)

**Where:** `tools/unattended/unattended.sh@d360a6b1:18581`.

**What is wrong:** no arm reaches `read_owner_question`'s rc 1, the no-roles-kit NOTE fallback, or the `owner` answer at line 18606. The `park-build` arm has one FORKED unit, so its loop is not shown to visit a second. The passing control asserts only `miss "grades FORKED"`, which any earlier refusal satisfies.

**Consequence:** a reader refusal read as admit, a `park-build` that records only the dispatched unit, or a control that fails for another reason would all stay green. This is the gate that stops code being written against an open fork. The product code reads correctly.

**Fix (class-level, the skeptic's):** beyond the finder's arms, add a stub printing an answer outside the closed set (check 49 expected), an arm with no roles kit (the NOTE and the `resolve` answer), and one landing an `owner`-answering policy value. Keep the stub exiting 2 that expects check 49 with the reader's words, the two-FORKED-spec `park-build` arm asserting both ids, and a control asserting `dispatch declared`. The finder's proposal cures the cited instance alone.

**Left-shift gate:** `harness arms (fail branches armed or pinned)`, with the arms in the unattended driver's suite.

## LOW

### L1. A repeated `--dispatch` on a FORKED unit appends duplicate decision rows (finding 10)

**Where:** `tools/unattended/unattended.sh@d360a6b1:18587`, in the `park-item` and `park-build` answers of the FORKED hold.

**What is wrong:** the answers call `park` unconditionally, with no exact-line compare like the one `write_refusal` makes.

**Consequence:** a resume or a retrying driver appends an identical decision row each time, and the parked-decision count the close surfaces grows with duplicates of one question.

**Fix (judged sound):** before `park`, skip when the run-state already holds a decision row with the same item and reason, the compare `write_refusal` uses, and still refuse. Arm a second dispatch expecting one row.

**Left-shift gate:** `append-without-an-idempotence-key`, as a check over every `park` call that its arm re-runs the verb.

### L2. The actor row comment in `item-schema.toml` describes the state before the actor-patch check (finding 15)

**Where:** `tools/loop/item-schema.toml@19a8f30a:50`.

**What is wrong:** the comment says `check_actor_patches` refuses every actor patch until the roles kit's actor-patch check answers there. `loop_items.check_actor_patches` now runs `check_roles.py --check-actor-patch` and admits a conforming `role:adopter.<name>`.

**Consequence:** a reader is told actor patches are always refused. There is no behavioural effect.

**Fix (judged sound):** state that a patch naming a repository role is judged by `check_roles.py --check-actor-patch` and any other value is refused.

**Left-shift gate:** the `amendment-leaves-its-other-half-standing` checklist entry, since prose is not gated here.

### L3. Several shell-write shapes the contract names have no scan row (finding 25)

**Where:** `tools/hooks/scratch-guard.js@f71f3b8c:526`.
The read arm's fail-closed throw is at `tools/hooks/scratch-guard.js@f71f3b8c:2720`.

**What is wrong:** `scratch-guard.test.sh` has no row for `perl -i`, a patch's `rename to` line, `appendFileSync` or `[IO.File]::AppendAllText`, and no row makes `checkDriverRead` throw. `sed --in-place`, `write_bytes` and `WriteAllBytes` are missing too.

**Consequence:** each works today, but its regex or branch can be dropped with every row green, and a role agent's write through it would then be ungraded.

**Fix (class-level, the skeptic's):** derive rows from the whole contract: one per alternative of `INTERPRETER_WRITES` (append and bytes forms included), `sed -i` and `sed --in-place`, `perl -i`, and both patch line forms, plus the read-arm preloaded-throw rows (main loop exit 2, worker exit 0). The finder's proposal cures the cited instance alone.

**Left-shift gate:** `scratch-guard self-test`, with the row set joined to the header's contract list.

### L4. A refused orientation return is reported as a formatting defect and its route is not named (finding 30)

**Where:** `tools/loop/placement.py@95e535e7:488`, in `read_scout_return`.

**What is wrong:** `outcome: refused` is a valid orientation return and `check_scout_return` forwards it, but `read_scout_return` stops on the `rule:` line as a malformed key before it compares `outcome`. Neither the Skill nor the verbs guide names `handoff.py route-refusal`, which appears only in help/roles.md, handoff.py and the suite.

**Consequence:** a typed refusal reads as a formatting defect, and the caller has no named route. The finder's claim that Stage 1 routes every refusal back is overstated: `SKILL.template.md` sends only an `outcome: placed` return to `place`. `place` writes no placement either way.

**Fix (class-level, the skeptic's):** have `place` read `outcome`, `rule`, `remedy` and `actor` from the same return object `check_return` grades (JSON or `key: value`) before its key check, and refuse an `outcome: refused` by its own text naming `route-refusal`. Add to Stage 1 that a refused return goes through `route-refusal`, with the scout re-spawned only on a `self` route or a malformed return. The finder's proposal cures the cited instance alone.

**Left-shift gate:** `loop placement fixtures`, sharing the JSON plant of H3.

## Dispositions

| class or leg | findings |
|---|---|
| class:invariant-held-on-one-admission-path | 1, 2, 4 |
| new:operands-read-past-their-simple-command | 3, 27, 28 |
| class:two-guards-one-question-two-answers | 5, 29 |
| class:append-without-an-idempotence-key | 6, 10, 11 |
| gate:scratch-guard self-test | 7, 8 |
| class:check-grades-one-layer-of-a-layered-config | 9, 13 |
| new:handed-text-unfenced-before-a-heading-reader | 12 |
| class:policy-value-with-no-route | 14 |
| class:amendment-leaves-its-other-half-standing | 15 |
| class:refusal-branch-with-no-arm | 16, 18, 19, 20, 24, 25, 26 |
| gate:loop position fixtures | 17 |
| class:held-suite-guard-misses-a-sibling-kit | 21 |
| gate:check-wiring self-test | 22 |
| class:swallowed-delegate-reads-as-clean | 23 |
| class:forwarded-arg-opens-an-unhandled-return-shape | 30 |

review-shape kind=diff-review round=1 intensity=full at=synth raw=30 confirmed=30 refuted=0 merged=0 unverified=0 blocker=1 high=9 medium=16 low=4 agents=11 out-tokens=142384 trigger=owed shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=10 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/hooks/scratch-guard.js@f71f3b8c:553 | high | high | confirmed | Probed head: sed -i alone is DENY for gov-skeptic and gov-reviewer; 'if true; then sed -i s/a/b/ tools/f; fi' and '{ sed -i ...; }' yield no targets and null. scanWriteTargets passes {inline:true} only; scanCommandHeads steps reserved words only under opts.reserved. checkShellWrites is new in this diff, and the header's escape list names only xargs and sudo. Fix cures then/do/else/{/if/while, but SHELL_RESERVED_WORDS lacks coproc and function; 'coproc sed -i' and 'function f { sed -i ...; }' also probed as admitted and would stay so. | instance | invariant-held-on-one-admission-path | class:invariant-held-on-one-admission-path |
| 2 | security | tools/hooks/scratch-guard.js@f71f3b8c:422 | high | high | confirmed | Probed head: 'echo x>tools/f.py', 'cat>tools/f.py' and 'echo x >\|tools/f.py' give [] and null for both roles, while 'echo x > tools/f.py' is DENY. '&>>' yields the mangled target '>tools/f.py'. REDIRECT is unchanged since base, but base had no checkShellWrites: this diff made it the role-enforcement reader, and the header claims redirects are covered. The proposed regex still misses '>&file' (probed admitted; it reads '&file', and readTokenAt stops at '&'), and excluding '=' and '-' before the operator leaves 'echo a=>f' and 'echo -> f', which are real redirections, unseen. | instance | invariant-held-on-one-admission-path | class:invariant-held-on-one-admission-path |
| 3 | security | tools/hooks/scratch-guard.js@f71f3b8c:605 | medium | high | confirmed | Probed head: gov-spec-writer 'cp /c/Temp/b.py tools/x.py' is DENY, and the same with ' 2>/dev/null' is admitted with a witness, its targets being '/dev/null' and '2>/dev/null'. gov-skeptic 'cp tools/a.py /c/Temp/b.py 2>/dev/null' and 'mkdir -p /c/Temp/x 2>/dev/null' are falsely refused. The scan predates the diff but its use for role verdicts is new. The fix leaves the same phantom-operand overrun across a newline: 'cp /c/Temp/b.py tools/x.py\necho hi' yields target 'hi' and is admitted, and 'mkdir -p /c/Temp/x\ngit status' is falsely refused. | instance | - | new:operands-read-past-their-simple-command |
| 4 | security | tools/roles/spawn-guard.js@139eada2:583 | high | high | confirmed | checkHarnessLanded's one caller is checkHarnessCall, with the top-level entry; the hash covers that path only. tools/workflows/unattended-build.js@4ecf3bb3:1831 runs workflow({scriptPath:'tools/workflows/tier2-review.js'}), and spec-audit-optin.js states a nested workflow() is a runtime call inside the script that the hook does not see. An unlanded tier2-review.js therefore runs under a landed parent. The landed check is new in this diff, its text says an edited harness never runs before the bar has read it, and grep finds no nesting exception in spec 25. Narrow: spec-audit path only. The fix covers the one nested edge as a literal. | sound | invariant-held-on-one-admission-path | class:invariant-held-on-one-admission-path |
| 5 | correctness | tools/roles/handoff.py@d123282e:1926 | high | medium | confirmed | Executed: check_return('gov-orienter', JSON block) returns []; read_scout_return over such a block raises PlacementRefused at line 1. run_return_check's send-back orders one json block from every role, and .claude/skills/build/SKILL.md:51 passes --agent, which requires byte equality with the agent's text. 'Can never be recorded' is overstated: --agent is optional and a respawn recovers, and the refusal is loud, hence medium. First fix branch is insufficient: in JSON check_return rejects 'build' and 'playbook' as fields the template does not name (executed), so a placement naming a build still fails; the key: value reader silently ignores them. The second branch leaves a first JSON return broken. | unsound | - | class:two-guards-one-question-two-answers |
| 6 | correctness | tools/workflows/unattended-build.js@4ecf3bb3:2110 | high | high | confirmed | Base used a direct agent() for the round record; head wraps it in runWithRetries, which re-spawns the same prompt on null. verb_review has no duplicate check: check_review_ended refuses only where a terminal row stands, and any other repeat appends a row and draws the review-round budget. An agent that dies after running the verb therefore double-records (a repeat count can turn the loop BOUNDED), or meets the terminal refusal and throws the misleading re-key error. Deviation 53 lists the round record as wrapped but never addresses idempotency. The path is narrow. The fix cures this call only: the disposal stage, also a write that promotes, files asks and commits, is wrapped the same way at :2650. | instance | - | class:append-without-an-idempotence-key |
| 7 | correctness | tools/hooks/scratch-guard.js@f71f3b8c:475 | medium | medium | confirmed | Ran scanWriteTargets at head: `perl -MList::Util=sum -ne print tools/x.py`, `perl -MTime::Piece -e 1 a.txt` and `perl -Ilib -ne print f` each return a `perl -i` write target. The cluster loop tests every letter for `i`. scanInPlaceOperands is absent at base. The effect is a contained, fail-closed false refusal. Stopping the walk at value-taking switches, plus the detached -I operand, cures it. | sound | - | gate:scratch-guard self-test |
| 8 | correctness | tools/hooks/scratch-guard.js@f71f3b8c:468 | medium | medium | confirmed | Ran it: `sed -i -- s/a/b/ out.txt` yields the targets `s/a/b/` and `out.txt`. The `--` branch at line 468 pushes every remaining word without consuming the script when `script` is false. The function is new in this diff. The effect is a contained false refusal of a role's write. Continuing the operand logic after `--` cures it for both sed and perl. | sound | - | gate:scratch-guard self-test |
| 9 | correctness | tools/loop/loop_lib.py@b14af4ca:1898 | medium | medium | confirmed | run_declaration_command builds its rows only from read_items, which is read_item_rows over gov's loop.toml. read_item_declaration in handoff.py turns exit 1 into a refusal. The same diff's check_item_roles grades composed repository items naming `role:` actors and its role-core case admits item.build.adopter.ship, and the actor-patch seat admits patches. So an admitted repository item cannot be rendered, and amended fields are read pre-patch. The verb is new here and nothing in the unit 3 spec excludes repository items. As written the fix swaps only the row: the verb still calls read_outcome_set(kit_dir, tag), which reads the definition's own rows, so an adopter tag would still fail and an amended item's outcomes would stay pre-patch. | unsound | - | class:check-grades-one-layer-of-a-layered-config |
| 10 | correctness | tools/unattended/unattended.sh@d360a6b1:18587 | low | low | confirmed | The FORKED hold calls park unconditionally in the park-item and park-build arms. park() appends with no compare, while write_refusal does an exact-line compare. The base verb_dispatch has no FORKED hold. A repeated dispatch on a still-FORKED unit appends an identical decision row and inflates the parked-decision count. The spec's AC6 expects one row and nothing states repeats are intended. Comparing before parking in both arms cures it. | sound | - | class:append-without-an-idempotence-key |
| 11 | seams | tools/workflows/unattended-build.js@4ecf3bb3:2110 | high | high | confirmed | writeRound runs its record agent through runWithRetries, which respawns on null with the identical prompt. verb_review refuses a repeat only on a terminal subject and otherwise parks a new row, drawing the rework budget for any round after the first. A CONVERGING round recorded by an agent that then returned null is therefore recorded again with an equal count, reading NON-CONVERGENT or BOUNDED. A terminal one returns terminalSubject and throws. Base has no runWithRetries. Unit 5 specifies single-call re-runs, but it never considers a stage whose effect already landed. The path needs a null after the side effect, so it is narrow. The fix leaves the same re-run around the builder in unattended-unit.js line 525, which respawns after a commit and after the driver's dispatch and brief rows. | instance | - | class:append-without-an-idempotence-key |
| 12 | seams | tools/workflows/unattended-unit.js@ee9e2dbb:299 | medium | medium | confirmed | HANDED concatenates briefFact.text and specFact.text with no fence. print_input_facts only trims blank edges. readWorkOrderAllowance walks the first user record with readUnfencedLines, denies on an unclosed fence or on two allowance headings, and otherwise takes the first unfenced `## Task` / `### allowance`. The harness prompt has no `## Task` of its own, so handed text decides the builder's allowance. A count of tracked prompts holding a `## Task` line gave 1669. HANDED is new in this diff. The effect is contained, since it narrows or denies. Wrapping each text with the render_handed_fence rule cures it. | sound | - | new:handed-text-unfenced-before-a-heading-reader |
| 13 | seams | tools/loop/loop_lib.py@b14af4ca:1898 | medium | high | confirmed | run_declaration_command reads read_items(kit_dir), which is read_item_rows over the definition beside the file, and roles via read_role_defaults -> load_roles. Neither takes a root or a rev. handoff.read_item_declaration passes only --item, and its sole actor check is declaration.actor == 'role:'+role. handoff itself composes roles and workflows through load_composition(root), and the loop kit already has read_composed_items(root), so the layer mismatch is real. ITEM_VALUE_RE admits repository tags. An admitted overlay amend silently yields an unamended work order. It needs an overlay, which no tree has today, so the path is narrow. Fix: composing the rows cures inputs and repository items. For an actor patch, compose_roles keys a repository role by derive_repository_slot ('triager') while the actor is 'role:adopter.triager', so both the slot lookup in resolve_item_declaration and handoff's actor compare still fail for the patched role. | instance | check-grades-one-layer-of-a-layered-config | class:check-grades-one-layer-of-a-layered-config |
| 14 | seams | tools/workflows/unattended-build.js@4ecf3bb3:635 | medium | medium | confirmed | The catalogue declares roles.retries as { type = retry-count, min = 0 } with no max. All three harnesses, whose ATTEMPTS checks this diff added, throw above 4 and tell the caller to pass what policy.py get prints. The SKILL and VERBS templates say the same. The harness bound is in spec 5 S6, but nothing joins it to the catalogue. The failure is loud and before any agent, hence contained. A max key is already used by a neighbouring retry-count row, so the fix is supported. | sound | - | class:policy-value-with-no-route |
| 15 | seams | tools/loop/item-schema.toml@19a8f30a:50 | low | low | confirmed | The comment this diff added on the actor row says check_actor_patches 'refuses it until the roles kit's actor-patch check answers there'. loop_items.check_actor_patches now runs check_roles.py --check-actor-patch for role:adopter.* values and admits on exit 0. The comment is stale, with no behavioural effect. | sound | a-folded-field-leaves-its-row-shape-docs-behind | class:amendment-leaves-its-other-half-standing |
| 16 | verification | tools/roles/return-check.sh@d775fbd8:214 | high | medium | confirmed | Grep finds no test executing return-check.sh except govkit check_stop_replay, which reads the SubagentStop commands from settings. That replay requires rc 0, empty stdout and no record. render_agents arm 22 runs handoff.py check-return directly. check_stop_replay's docstring leaves direct-spawn stops to the return check's own plants, and those bypass the shim. Replacing the body with exit 0 keeps every arm green. The shipped shim works today by reading, so this is a contained coverage hole. A positive control through the installed command cures it. | sound | refusal-branch-with-no-arm | class:refusal-branch-with-no-arm |
| 17 | verification | tools/loop/position.py@077196d1:488 | medium | medium | confirmed | REFUSAL_TAIL_RE appears only in position.py's definition and use. run_refusal_plant and check_plant record and assert only '--reason probe'. render_position_lines prints item, key and reason only, so the text view drops rule, remedy and actor although the JSON keeps them. write_refusal validates only the typed flags, and check_step_fields refuses the separator only in item and step. A plain reason spelling the tail therefore reads back as typed with an unchecked actor. All of this was introduced here. | sound | refusal-branch-with-no-arm | gate:loop position fixtures |
| 18 | verification | tools/unattended/unattended.sh@d360a6b1:16891 | medium | medium | confirmed | unattended.test.sh 6801-6811 holds only a full set with actor driver and the bad actor nobody. Greps for --rule, --remedy and --actor show no other use. The partial-set, separator and build:* lines are untested. Fix: the proposed --rule-alone arm is refused by the actor case even with the non-empty check deleted, since the actor is empty. As specified it asserts only that no bytes were written, so it stays green on the very deletion the finding names. | unsound | refusal-branch-with-no-arm | class:refusal-branch-with-no-arm |
| 19 | verification | tools/roles/spawn-guard.js@139eada2:545 | medium | medium | confirmed | checkFraming (spawn-guard.js 535-564) is new in this range. The PF fixtures plant only spawn-unframed, spawn-framed and spawn-framed-by-researcher, and both deny plants stop at the heading count or the role. A fixed-string grep of the suite gives 0 for the placement, spelling, missing-file and task-sha refusals. No other Framed by: row reaches this function, because the tmark/tframed rows belong to the typed-input check. Deleting line 560 stays green. The code itself is correct today. The fix omits the malformed `Framed by:` spelling, two framing:job headings, and a file with zero or two markers, which are untested refusals of the same function. | instance | refusal-branch-with-no-arm | class:refusal-branch-with-no-arm |
| 20 | verification | tools/roles/spawn-guard.js@139eada2:319 | medium | medium | confirmed | checkFactKeys has card, outside-checkout and missing-file branches. The suite holds 0 occurrences of `card/`, `names no path inside` and `no file is there`; only BR13 AC3's moved-file rows exercise the function. The function is new (0 hits in the base agent-cap.js). The fix leaves the absolute and drive-letter key alternatives, the unreadable-card branch, and an admitted unchanged card without an arm. | instance | refusal-branch-with-no-arm | class:refusal-branch-with-no-arm |
| 21 | verification | tools/gate-legs.json@fc85cb7a:3102 | medium | medium | confirmed | The leg's guard holds four paths. The suite resolves and compares roles/handoff.py (1006-1010), copies six policy kit files into its fixtures, and copies workflows/spec-audit-optin.js. The base agent-cap leg listed lib/ and spec-audit-optin.js, and the new leg lists neither. So a local guarded bar skips the suite on those edits. Remote CI runs GATE_FULL=1, which contains the effect. The fix is incomplete: handoff.INPUT_NAMES derives from roles_lib.READ_FAMILIES, so a typed input added in roles_lib.py would still skip the leg. | instance | changed-mode-selection-ignores-doc-reads | class:held-suite-guard-misses-a-sibling-kit |
| 22 | verification | tools/check-wiring.sh@d80db82f:1880 | medium | medium | confirmed | check-wiring.sh 1880-1881 is added by the diff. check-wiring.test.sh contains neither `return-check` nor `SubagentStop`. Its roles fixture copies only workflows.toml and agents/*.agent.md, so the `-f return-check.fragment.json` branch never runs there. Dropping the arm or mistyping the filter prints nothing and stays green. govkit's selftest requires a SubagentStop command in an install, but it does not exercise this checker arm. The proposed unwired and wired pair cures it. | sound | - | gate:check-wiring self-test |
| 23 | verification | tools/memory-tree/check-memory-hygiene.test.sh@807b34a1:4725 | medium | medium | confirmed | Test lines 4724-4725 OR the F6 refusal with the note `because no principle registry was read`. The engine (check-memory-hygiene.sh 2296-2310) prints that note for any non-zero exit of the inline reader: LookupError, ImportError, a traceback, or no tag matched. In gov the playbook kit resolves, so a broken reader turns the registry grading off while F6 passes. The header comment says only that the note stands where no kit resolves, and the arm does not enforce that condition. Resolving the kit in the test independently and requiring the refusal line cures it. | sound | - | class:swallowed-delegate-reads-as-clean |
| 24 | verification | tools/hooks/scratch-guard.js@f71f3b8c:2029 | medium | medium | confirmed | scratch-guard.test.sh contains no `workflows/` or `wf_` transcript path, no `TRANSCRIPT` and no `runs past`. All its transcripts are written at <session>/subagents/agent-*.jsonl (a7 and br50). readWorkOrderAllowance and TRANSCRIPT_READ_BOUND are new in this range. Breaking the run-directory lookup yields `{ why }`, which falls back to the class verdict alone for harness-stage agents, unseen by the suite. Removing the over-bound deny is also unseen. The two proposed rows exercise both branches. | sound | refusal-branch-with-no-arm | class:refusal-branch-with-no-arm |
| 25 | verification | tools/hooks/scratch-guard.js@f71f3b8c:526 | low | low | confirmed | scratch-guard.test.sh has ten scan_targets rows (1647-1662). A grep for perl, rename to, appendFile and AppendAll in that file finds no row. The header at tools/hooks/scratch-guard.js@f71f3b8c:185-188 names perl -i, appendFileSync and `rename to`. My probe of `perl -pi -e` returns x.py, so the behaviour is right and only unpinned. No run_read row (2092-2104) makes checkDriverRead throw, so the fail-closed catch is unexercised. The fix cures the named shapes, but `sed --in-place`, also in the contract, has no row either (grep empty), nor do write_bytes and WriteAllBytes. | instance | refusal-branch-with-no-arm | class:refusal-branch-with-no-arm |
| 26 | verification | tools/unattended/unattended.sh@d360a6b1:18581 | medium | medium | confirmed | The arm at tools/unattended/unattended.test.sh@8e21d376:9112-9158 covers resolve, park-item, stop-run and park-build with one FORKED spec. Its own comment says it does not check a reader refusal or an absent roles kit. No other line in the unattended suites mentions the no-kit NOTE, 'printed no answer' or the owner answer. The passing control asserts only miss 'grades FORKED', which any earlier refusal satisfies. The product code reads correctly, so this is a coverage gap. The fix omits the no-kit fallback, the outside-the-set answer and the `owner` answer the claim names. | instance | refusal-branch-with-no-arm | class:refusal-branch-with-no-arm |
| 27 | intent | tools/hooks/scratch-guard.js@f71f3b8c:2116 | blocker | blocker | confirmed | I ran checkShellWrites. For gov-spec-writer, `cp /c/Temp/b.py tools/x.py` is denied. With 2>/dev/null, 2>&1 or a following `echo hi` line, it is admitted with only the allowance witness, the targets read being '2>/dev/null', '2>' and 'hi'. For gov-skeptic, `echo a>tools/x.py` is null and the spaced form is denied. The scanner is older, but the arm making it a role boundary is new, and neither spelling is in its escape list (tools/hooks/scratch-guard.js@f71f3b8c:200-209). The fix as written ends the segment at any newline. A backslash-continued `cp a.py \<newline> tools/x.py`, caught today (I probed it: x.py), would then escape. It also leaves `>\|`, `&>>` and a trailing `# note`, all of which I probed as missed (cp with `# note` reads 'note'). | unsound | inputs-inside-the-subjects-reach | new:operands-read-past-their-simple-command |
| 28 | intent | tools/hooks/scratch-guard.js@f71f3b8c:2116 | high | high | confirmed | I reproduced all four for gov-skeptic. mkdir with 2>/dev/null, mkdir then a `git status` line, cp to scratch with 2>/dev/null, and cp then a grep line are each denied on '2>/dev/null', 'git', '2>/dev/null' and 'tools/b'. Plain mkdir of the scratch path is admitted. These are ordinary commands of writes=none roles, and the remedy is addressed to the driver. The base had no checkShellWrites, so the refusal is new. The fix cures the cited cases through the simple-command segments. Comment words still count as operands: scanCommandHeads stripped `# note` from argv, while the current operand walk read 'note'. | instance | inputs-inside-the-subjects-reach | new:operands-read-past-their-simple-command |
| 29 | intent | tools/roles/handoff.py@d123282e:1926 | high | high | confirmed | I ran both readers. A JSON block with `build` makes check_return report 'build - a field the template does not name'. Without build, check_return is [] but read_scout_return refuses line 1. The key: value form passes both. handoff.py's block reason orders ONE corrected ```json block with no field the template does not name, so a sent-back orientation return cannot be placed. place --agent byte-binds the file to the agent's last text (check_agent_return), so the driver cannot convert it. Reading the graded object and adding the three fields cures it. | sound | forwarded-arg-opens-an-unhandled-return-shape | class:two-guards-one-question-two-answers |
| 30 | intent | tools/loop/placement.py@95e535e7:488 | medium | low | confirmed | I ran it. A valid refused return (outcome, rule, remedy, actor) gives check_return [] and read_scout_return 'line 2 is no key: value', so the docstring's `outcome` refusal is never reached and the refusal reads as a format defect. git grep finds route-refusal only in help/roles.md, handoff.py and the suite. The route claim is overstated: SKILL.template.md Stage 1 sends only an `outcome: placed` return to place, so 'a refusal of either' does not cover a refused return by instruction. place writes no placement either way. The effect is a misleading message and an unnamed route. The fix is line-oriented, so a refused return in JSON, which the same channel admits, is still refused as a malformed line 1. | instance | forwarded-arg-opens-an-unhandled-return-shape | class:forwarded-arg-opens-an-unhandled-return-shape |
