**Serves:** diff-review KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11

# Tier-2 closing diff review — aOrientedCast, ROUND 1

*Round 1 of the closing review (BUILD-METHOD M8) of build aOrientedCast: 14 units, all CLOSED.
Every agent a governed session spawns is now handed a rendered role. The diff adds the roles kit
(`tools/roles/`), the To-do and Reuse task fields with a READY refusal, `roles`/`efforts` on the
three harnesses, a charter delegation bullet, the default govkit install, and three hook arms:
scratch-guard's role arm, agent-cap rule 6, and scratch-guard's checkRoleGate. Node `a`,
2026-10-12. Every judge ran untyped, because this session's agent registry predates
`.claude/agents`.*

Reviewed range: `646d4a73581393acbf42f33864a9808c96d00a0c...b6afa3c024e967a9bd05d27942296f8f57f94a07` · ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker survived. Thirteen findings were confirmed and none refuted. They come down to ten
items, three of which are high on the binding grades. The worst defect is one missing tab on row 94
of `tools/run-gates/selftest-budgets.txt`, which four lenses found independently. The second is a
seeded `policy.toml` that names a lexicon leg a default install does not have, which reds the
roles catalogue and render on such a target. Neither ships a wrong result silently. Both are
one-line or few-line fixes, and every item below carries a left-shift gate suggestion.

## Review shape

Intensity full, raw 13, confirmed 13, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| seams | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 0 blocker, 2 high, 5 medium, 3 low. By raw confirmed finding: 0 blocker,
3 high, 7 medium, 3 low. The row-94 defect is split across two items because its four findings
carry two different binding grades (ids 3 and 11 high, ids 8 and 13 medium), and items merge only
within one grade.

### Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0
  duplicates.
- Fixes on confirmed findings: 9 judged sound, 4 judged unsound, 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 2 re-graded by the skeptic (ids 10
  and 13, high to medium).
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.

Every counter is zero where it matters, so this run is complete. Fourteen spec documents were
supplied as `specs`, beside the range's commit messages. The checklist held 84 items, each assigned
to exactly one lens: security 17, correctness 17, seams 17, verification 17, intent 16. By-design
items came from the caller's byDesign. The stated security model holds that the hooks are routing
guards and not a security boundary, so every hook finding below is graded on that basis: the
push-boundary bar is the guarantee.

## Findings

### H1 [high] — `roles render selftest` budget row has no argv column (ids 3, 11)

`tools/run-gates/selftest-budgets.txt:94`. The row is `roles render selftest<TAB>60<TAB>measured
1.3s …`, one tab short. It is the only 3-field row in the file. `read_population`
(`run-selftests.sh:558-561`) takes f[2] as the argv, so the prose becomes the command and the
gate-legs.json leg (`python {prefix}/roles/render_agents.py --selftest`) is never looked up. The
serial loop, the pooled sweep, `--attribute` and `foreign-prefix.gov.test.sh` all execute
`measured …` and exit 127. A `--kit <prefix>/roles` run drops the row outright, because the prose
does not contain the kit path, and reads clean without running the self-test. `--check` passes the
row because its reverse arm only inspects slash-bearing tokens and the prose has none.

- Fix (judged SOUND by the skeptic): insert the empty argv column, giving
  `roles render selftest<TAB>60<TAB><TAB>measured 1.3s …`, matching row 93 and every sibling.
- Left-shift gate: make `run-selftests.sh --check` refuse any data row whose tab-field count is not
  4, and any non-empty argv whose first word is neither a known launcher nor a path-bearing token.
  Stage the 3-field row, observe RED, then unstage.

### H2 [high] — the seeded policy names a leg a default install lacks (id 7)

`tools/roles/house/policy.toml:26`. The seed grants `"lexicon naming predicates"` to
gov-spec-writer and gov-builder. Only the lexicon kit declares that leg, and lexicon is not in the
default selection while roles now is. On a target with a manifest runner, govkit writes
`<prefix>/gate-legs.json` from the selected kits only, so `roles_lib.load_policy` raises R12. That
reds `check_roles.py` (the roles catalogue leg), makes `render_agents.py --check/--write` exit 2
(the roles render wiring leg, adopt-roles `--check`/`--scaffold`, and the `[[regenerate]]` on
update), and makes `handoff.py stage-efforts` exit 1, so `/build` and the unattended verbs cannot
compute `efforts`. The govkit default-install arm misses it because its DEPLOY_FULL fixture declares
no `[gate_runner]`.

- Fix (judged SOUND by the skeptic): do not ship gov-specific leg names in the seed. Either list
  only legs of required kits (`"memory hygiene"`) in the shipped `policy.toml` and keep gov's
  lexicon grant in gov's own house copy, or make `load_policy` treat a `[gates]` name the manifest
  lacks as a note (its kit is not installed) rather than an R12 defect.
- Left-shift gate: a govkit selftest arm that does a default apply WITH a `[gate_runner]` manifest
  and then runs `adopt-roles.sh --check` and `check_roles.py`, expecting exit 0.

### M1 [medium] — the same row-94 defect, at its medium binding grade (ids 8, 13)

`tools/run-gates/selftest-budgets.txt:94`. This is H1's defect. The seams lens graded it medium, and
the intent lens's high was re-graded medium by its skeptic: the runner fails loudly with a red row,
and the self-test still runs as its own manifest leg under run-gates. I would grade it with H1 as
high, because a kit-filtered run reads clean while skipping the suite (id 11's path), but the
binding grade stands.

- Fix (judged SOUND by the skeptic on both ids): H1's one-tab fix closes both.
- Left-shift gate: H1's field-count refusal in `--check`.

### M2 [medium] — checkRoleGate admits a launcher with more than one option (ids 1, 4)

`tools/hooks/scratch-guard.js:1270`. `scanCommandHeads` steps past exactly one launcher option, so
an option's argument or a second option becomes the head. Probed against the shipped hook as
gov-builder: `bash -o pipefail tools/run-gates/run-gates.sh` (head `pipefail`),
`python -X utf8 tools/govkit/selftest.py` (head `utf8`), `bash -e -x tools/hooks/agent-cap.test.sh`
(head `-x`) and `bash -e -c 'bash tools/run-gates/run-gates.sh'` (head `-c`, body never scanned) are
all admitted, while plain `bash tools/run-gates/run-gates.sh` is refused as G2. `env -u FOO bash …`
leaves `-u` as the head, and `exec`, `command` and `nice` are absent from `GATE_PREFIX_WORDS`. The
code follows the TOOL-aOrientedCast-11 spec's "a launcher … with one option", but the same spec says
G2 matches the runner "in any form", and the declared ceiling does not name launcher options.

- Fix. Id 1's fix was judged SOUND; id 4's finder fix was REJECTED, and the skeptic's corrected fix
  is the one to write, since it subsumes id 1's. Loop over every leading word of a shell launcher
  that starts with `-` or `+`, stopping after `--` (consumed). A word in
  `-o +o -O +O --rcfile --init-file` consumes the next word. A cluster containing `c` scans the
  following word once as a body (depth 0) and ends the segment. A cluster containing `n` ends the
  segment. For python and py, loop the same way: `-W`, `-X` and `-Q` consume the next word, and a
  cluster ending in `c` or `m` ends the segment. For node, `-r`, `--require` and `--import` consume
  the next word, and `-e`, `--eval`, `-p` and `--print` end the segment. From id 1's sound fix, add
  `exec`, `command` and `nice` to `GATE_PREFIX_WORDS`, and skip `env`'s own options (with `-u
  NAME`'s argument) before the head.
- Left-shift gate: refused probe rows in `scratch-guard.test.sh` for `bash -o pipefail <runner>`,
  `bash -e -x <runner>`, `bash -O extglob <runner>`, `bash -e -c '<runner>'` and
  `python -X utf8 <selftest.py>`, each expecting exit 2. Keep `bash -n <suite>` as an exit-0
  near-miss.

### M3 [medium] — rule 6 and checkRoleGate arm from the payload cwd only (id 2)

`tools/hooks/agent-cap.js:2256` and `tools/hooks/scratch-guard.js:1372`. Both resolve the checkout
root from the payload cwd and never read `CLAUDE_PROJECT_DIR`. When the main session's persistent
Bash cwd has left the checkout (for example into the scratchpad), both arms add no rule and print
nothing, though `.claude/roles.json` exists. Built-in `subagent_type`s, freeform prompts and inline
Workflow scripts are then admitted. The sibling `checkRouted` and `renderRouteContext` anchor on
`env.CLAUDE_PROJECT_DIR || cwd`, so the guards disagree on which repo the session is in.

- Fix: the finder's fix was REJECTED. The skeptic's corrected fix: resolve the root from the
  payload cwd first, as the spec says, and fall back to `process.env.CLAUDE_PROJECT_DIR` only when
  the cwd has no checkout root. If neither has a root, keep the no-rule path and print one witness
  line naming the unresolved cwd. Do the same in `checkRoleGate`.
- Left-shift gate: an `agent-cap.test.sh` arm with cwd set to a non-repo temp dir and
  `CLAUDE_PROJECT_DIR` set to the fixture repo, in which a built-in `subagent_type` must exit 2, and
  a twin `scratch-guard.test.sh` arm for a gate command under the same setup.

### M4 [medium] — the untyped byte-identity arms are pinned to a historical sha (id 10)

`tools/workflows/unattended-build.test.sh:2599`. The OC4 AC1 arms (`run $i untyped` at about :2610
and `child $m untyped` at about :2666) compare current untyped prompts with harnesses read from
`git show 646d4a73:…`. TOOL-aOrientedCast-11 (3a40e7daf) then changed unattended-build.js's GROUND
and unattended-unit.js's unconditional "NO GATE, SUITE OR BAR" paragraph without touching the
suite, so these arms now go red at the close's bar. Every later legitimate edit to untyped prompt
text will red them again. The finder graded high; the skeptic re-graded medium because the failure
is loud and nothing wrong ships.

- Fix: the finder's fix was REJECTED. The skeptic's corrected fix: delete the fixed-sha byte
  comparisons. In their place, (a) assert that each untyped-only span is present in the untyped
  prompts: the criterion craft, "DO NOT WRITE PRODUCT CODE", the reuse craft, and the edge-join
  rationale in the disposal. (b) Assert that each typed-only span is absent from them: the "This
  stage runs as the … agent type" stamp, "a why that opens DIVERGENCE:", and "changes nothing else
  in the spec". (c) Optionally, compare byte for byte a run with no `roles` key against a run with
  `roles: {}` under the current harness.
- Left-shift gate: the corrected arms are themselves the gate. Add to the §10 checklist the class
  "a test oracle read from a literal historical sha", which reds on every legitimate later edit.

### M5 [medium] — no committed check runs `handoff.py` (id 12)

`tools/hooks/agent-cap.test.sh:2220`. The rule 6 arms build their marker and task-sha with an
inline Python copy, so they stay green if `handoff.py`'s hashed span or CRLF fold drifts from
`agent-cap.js`'s `extractTaskSection`/`buildTaskDigest`. `handoff.py` hard-codes `TASK_LABELS`
(line 54) where `manifest-check.sh` reads `TASK_SKELETON` at run time. None of render, check,
harness-args or stage-efforts has a committed arm; the TOOL-aOrientedCast-2 ledger shows its
criteria were observed by hand. The suite comment "AC6 holds the renderer itself against the hook"
names an arm that does not exist.

- Fix: the finder's fix was REJECTED. The skeptic's corrected fix: put the renderer-against-hook
  agreement arm in `agent-cap.test.sh`. Run `handoff.py render --part task --stdout` over a fixture
  card, brief and spec, pass the output as the Agent prompt, expect exit 0, and expect
  `handoff.py check` to re-derive the hook's task-sha. Add `{prefix}/roles/` to the
  `agent-cap self-test` leg's guard in gate-legs.json so a `handoff.py` edit triggers the arm. Make
  the arm SKIP out loud when the roles kit is not installed beside the hooks kit. Have `handoff.py`
  derive its labels from `manifest-check.sh --task-skeleton`, which it already locates as
  `KICKOFF_CHECKER`, instead of the hard-coded `TASK_LABELS`. Reword the suite comment to name the
  arm.
- Left-shift gate: the agreement arm above, under the widened leg guard.

### L1 [low] — the two task-field parsers strip the colon differently (id 5)

`skills/session-kickoff/manifest-check.sh:1079`. The awk `value()` tests for `:` right after the
paren strip without trimming first, while `handoff.py:126-134` strips whitespace and then the `:`.
For `- **OUT / non-goals** (explicit cut-line) : …`, awk yields `: …` (not a placeholder, so READY
is admitted) and `handoff.py` yields `…` (a placeholder, so every render reading `task:out`
refuses). The kickoff gate certifies a field the renderer then rejects.

- Fix (judged SOUND by the skeptic): in `value()`, trim `r` after the paren strip and before the
  `:` test, matching Python's `v = v.strip()` at that step.
- Left-shift gate: a KC fixture row with a space before the colon. M5's move of `handoff.py` onto
  `--task-skeleton` narrows this class further.

### L2 [low] — adopt-roles reads MEMORY_ROOT with a second parser (id 6)

`tools/roles/adopt-roles.sh:65`. A bare `sed 's/^MEMORY_ROOT=//'` reads the key, while the same
script reads CHARTER through `roles_lib.read_conf_key`, and the Python renderers read MEMORY_ROOT
that way too. With `export MEMORY_ROOT=memory` the adopter exits 2. With `MEMORY_ROOT=memory  #
note` the comment is substituted into every `{{MEMORY_ROOT}}` of the `/build` Skill.

- Fix (judged SOUND by the skeptic): read MEMORY_ROOT through the same `"$PY" -B -c …
  roles_lib.read_conf_key(…)` call already used for CHARTER, which means resolving `PY` before line
  65, or reuse check-wiring's export- and comment-aware sed. Apply the same change to
  `adopt-roles.test.sh` line 31.
- Left-shift gate: an `adopt-roles.test.sh` arm with a conf written as `export MEMORY_ROOT=…  #
  note`, asserting the rendered Skill and agent types carry the same root.

### L3 [low] — check-wiring reports roles ok over a broken index (id 9)

`tools/check-wiring.sh:1596`. When `.claude/roles.json` does not parse, `check_roles` prints a note
(line 1586) and then falls through to `ok roles …`. The hooks fail closed on a broken index, so
SessionStart reports green in the state that refuses every role write and spawn.

- Fix (judged SOUND by the skeptic): when the python read fails, report `UNWIRED  roles —
  .claude/roles.json does not parse as the role index; re-render with adopt-roles.sh --scaffold`,
  increment `unwired` and return. Keep the note only for the case where python itself is absent.
- Left-shift gate: a check-wiring self-test arm with a truncated `.claude/roles.json`, expecting
  `UNWIRED`.

review-shape kind=diff-review round=1 intensity=full at=synth raw=13 confirmed=13 refuted=0 unverified=0 blocker=0 high=3 medium=7 low=3 agents=11 out-tokens=223474

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/hooks/scratch-guard.js:1270 | medium | medium | confirmed | I reproduced this against the shipped hook. Using require('./tools/hooks/scratch-guard.js').checkRoleGate with agent_type gov-builder and the repo cwd, `bash -o pipefail tools/run-gates/run-gates.sh`, `python -X utf8 tools/govkit/selftest.py` and `bash -e -x tools/hooks/agent-cap.test.sh` all return null (admit), while plain `bash tools/run-gates/run-gates.sh` is denied as G2. The cause is scanCommandHeads (scratch-guard.js:1266-1278). It consumes only one leading option, so the option's argument (`pipefail`, `utf8`) or a second option (`-x`) becomes the head. That head has no slash, is not a runner or suite basename and carries no --selftest, so the command is admitted. `env -u FOO ...` goes the same way: once env is skipped, `-u` becomes the head. The spec (TOOL-11, 'The rows') does say 'a launcher ... with one option', so the code follows its own spec. But the same spec says G2 matches a runner 'in any form', and F2 says the runner and suite rows 'catch every expensive class whatever its arguments'. The declared ceiling (S8) names interpreters, aliases, functions and assembled paths, not ordinary launcher options. No owner ruling covers this. The effect is contained: the hooks are routing guards and the push-boundary bar is the guarantee, so the cost is a role agent running the bar or a suite mid-build. That makes it medium. | sound | - |
| 2 | security | tools/hooks/agent-cap.js:2256 | medium | medium | confirmed | Rule 6 in agent-cap.js (around line 2256) arms from resolveCheckoutRoot(data.cwd \|\| process.cwd()), and checkRoleGate (scratch-guard.js) returns null when resolveToplevel(cwd) finds nothing. Neither one reads CLAUDE_PROJECT_DIR. The sibling checkRouted (line 1131) and renderRouteContext (line 1411) anchor on `env.CLAUDE_PROJECT_DIR \|\| cwd`. The TOOL-7 spec (S2) and the TOOL-11 spec (order step 3) do name the payload cwd. Still, 'no toplevel above cwd → null' was meant for a session that is not in a governed repo, and no owner ruling covers a governed session whose shell cwd has left the checkout. The case is reachable: the main session's Bash cwd persists, and the harness points temp work at a scratchpad outside the repo, so after a `cd` there both arms add no rule and print nothing. The effect is contained to a routing guard that the stated security model already treats as bypassable, so it is medium. | unsound | - |
| 3 | correctness | tools/run-gates/selftest-budgets.txt:94 | high | high | confirmed | Row 94 of selftest-budgets.txt (`roles render selftest`) has a single tab between `60` and the note. The `cat -A` output shows `roles render selftest^I60^Imeasured 1.3s ...`, while every sibling row shows `^I<budget>^I^I<note>`. read_population (run-selftests.sh:561) takes f[2] as the argv, and here f[2] is the prose note. Because that argv is non-empty, the gate-legs.json leg (tools/gate-legs.json:1604) is never looked up, and the row is printed as `ok` with the prose as its argv. The run loop then `eval`s that prose, gets 127 ('measured: command not found') and reports FAIL. So `python tools/roles/render_agents.py --selftest` never runs from the runner. The row was added by this diff; it is absent at the base. The runner reports a wrong verdict on every run and points the next reader at the renderer, which is not broken. | sound | hand-named-gate-list-green-while-the-bar-reds |
| 4 | correctness | tools/hooks/scratch-guard.js:1270 | medium | medium | confirmed | scratch-guard.js:1266-1281 steps past exactly one launcher option. For `bash -o pipefail tools/run-gates/run-gates.sh`, opt=`-o` is not a c-cluster and not `-n`, so k++ makes the head `pipefail`. Its basename is not in GATE_RUNNERS, G3 does not match, and checkGateLeg returns null because the head has no slash, so checkRoleGate admits the command. `bash -e -x <runner>` leaves the head `-x`. `bash -e -c '<runner>'` leaves the head `-c` and its body is never rescanned. The code follows spec TOOL-11 section 4's 'a launcher ... with one option', but the same spec's G2 row says 'in any form', and the ceiling the header states (lines 116-119: interpreter, alias, function, assembled path, `$(...)` in quotes, scoped leg variant) does not list multi-option launchers. No BY DESIGN ruling covers it. The effect is contained: a role agent can run the bar or self-tests it should not, and the push-boundary bar remains the guarantee. That makes it medium. | unsound | a-view-fix-trades-one-blindness-for-another |
| 5 | correctness | skills/session-kickoff/manifest-check.sh:1079 | low | low | confirmed | Both parsers are new in this diff. In awk, value() (manifest-check.sh:1071-1081) trims, strips the paren group, then tests `substr(r,1,1)==":"` with no trim in between. The remainder ` : …` starts with a space, so the colon survives and the trimmed value `: …` passes placeholder(), because after removing dots and ellipses it is `: `, which is non-empty. handoff.py:126-134 calls `v.strip()` after the paren strip and before the colon test, which yields `…`, a placeholder. handoff.py:290 then refuses it. The comment block at 1043-1052 calls this 'the one grammar' that the renderer reads by, so the two disagree on input the kickoff gate admits. The case needs an odd space before the colon, so the effect is contained: a later render refuses with a clear message. Low. | sound | second-implementation-is-not-a-second-opinion |
| 6 | correctness | tools/roles/adopt-roles.sh:65 | low | low | confirmed | adopt-roles.sh is new. Line 65 reads MEMORY_ROOT with a bare `^MEMORY_ROOT=` sed. Line 168-171 of the same script reads CHARTER through roles_lib.read_conf_key, which accepts `export ` and a trailing ` # comment`. With `export MEMORY_ROOT=memory` the sed matches nothing and the script exits 2 at line 66. With `MEMORY_ROOT=memory  # note` the comment is kept and substituted into every `{{MEMORY_ROOT}}` of the /build Skill at line 117, while the Python renderers read `memory`. The sibling adopt-drift-audit.sh uses the same bare-sed shape, but the inconsistency inside this one file is new. It needs a conf written with export or a trailing comment, so the effect is narrow. Low. | sound | second-implementation-is-not-a-second-opinion |
| 7 | seams | tools/roles/house/policy.toml:26 | high | high | confirmed | tools/roles/kit.toml ships house/policy.toml as a `seed`, byte for byte. Its [gates] names 'lexicon naming predicates', a leg that only tools/lexicon/kit.toml:159 declares. lexicon is not in registry.toml's default selection, while roles now is. On a manifest-runner target, govkit writes <prefix>/gate-legs.json from the selected kits' [[gate_leg]] rows only (govkit.py, around line 4060). run-gates' [gate_runner_seed] places that file at {prefix}/gate-legs.json, which is exactly the path load_policy reads (kit_dir.parent/gate-legs.json). I ran load_policy in memory with a leg set that lacks the lexicon leg. It raised two R12 lines: "'lexicon naming predicates' names no leg of …gate-legs.json". load_policy is called by check_roles.py:268, render_agents.py:114 and handoff.py:380, so the catalogue leg, the render (and therefore adopt-roles --check/--scaffold and the [[regenerate]]) and stage-efforts all refuse. The failure appears only when gate-legs.json reads and the lexicon kit is not selected, which is the common default-install-with-runner case. It is not universal, because a target with no manifest gets a note instead. So: high. | sound | borrowed-seed-inherits-its-head-state |
| 8 | seams | tools/run-gates/selftest-budgets.txt:94 | medium | medium | confirmed | cat -A shows that row 94 is 'roles render selftest^I60^Imeasured 1.3s …'. awk confirms it is the only row in the file with 3 fields; every other row has 4. In read_population (run-selftests.sh:561), argv = f[2], which is the prose. Because that is non-empty, the gate-legs.json argv fallback is never taken. The run and attribute paths then `eval "$argv"` (lines 1842 and 1974), and the eval runs 'measured …', which exits 127. The --check reverse arm only inspects tokens that contain '/', and the prose has none ('2026-10-11,', 'x1.5' and 'TOOL-aOrientedCast-3' all lack one). So the declaration leg 'every held leg is budgeted, every budget row resolves' passes the malformed row. The effect is contained. The bar itself runs the leg from gate-legs.json, and only run-selftests' run, calibrate and attribute modes are affected, where the suite reads red rather than ever reading falsely green. The row is new in this diff: the base has no roles rows. | sound | - |
| 9 | seams | tools/check-wiring.sh:1596 | low | low | confirmed | In check-wiring.sh check_roles, when the python read of .claude/roles.json fails, the function prints a 'note' line and then falls through to the unconditional 'ok roles …' echo. Per the stated security model, the hooks fail closed on a broken index. So SessionStart reports roles as ok in a state where role-gated writes and spawns are refused. The degradation is printed as a note, not hidden, and the arm's header says it checks presence only. The effect is therefore a misleading verdict label, with no behavioural consequence. This is low. The code is new in this diff. | sound | degradation-known-but-unreported |
| 10 | verification | tools/workflows/unattended-build.test.sh:2599 | high | medium | confirmed | The arms at unattended-build.test.sh:2609-2611 and :2665-2667 compare every untyped promptjson with a run of the harnesses read from `git show 646d4a73:...`. 3a40e7daf (TOOL-aOrientedCast-11) then changed unattended-build.js GROUND unconditionally, in both the 'No stage of this program runs the merge bar...' sentence and the 'No gate, suite or bar runs inside a unit pass' sentence. GROUND reaches every spawned prompt. The same commit changed unattended-unit.js's unconditional PROMPT paragraph 'NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS'. The test file was last touched by 96f536d51, before 3a40e7daf, and its commit message says no suite was run. So every untyped prompt now differs from the 646d4a73 rendering, and the three 'run $i untyped' and two 'child $m untyped' byte-identity arms go red. A tree without 646d4a73 makes them SKIP out loud. That SKIP is a stated design choice, so I do not count it as a defect. The failure is loud: the close's bar goes red and nothing wrong ships. The effect is therefore contained (medium). Separately, pinning a historical sha makes the arms red again on every later legitimate edit to untyped prompt text. | unsound | - |
| 11 | verification | tools/run-gates/selftest-budgets.txt:94 | high | high | confirmed | The `roles render selftest` row at selftest-budgets.txt:94 has 3 tab-separated fields, where its neighbours have 4 (name, budget, empty argv, reason). The declaration parser at run-selftests.sh:558-561 takes f[2] as the argv, so it reads the prose 'measured 1.3s on node a 2026-10-11, one direct run of the argv...'. Because that argv is non-empty, it never resolves through gate-legs.json, which holds a correct 'roles render selftest' leg (python {prefix}/roles/render_agents.py --selftest). The run loop then evals the prose at :1842, which exits 127, so the self-test never runs through this runner. The `--kit <prefix>/roles` filter drops the row, because the prose does not contain the kit path (:580). A kit-filtered run therefore reads clean while skipping the self-test. That is a check certifying what it does not check, on a narrow path. The `--check` reverse pass (:796-806) only inspects tokens that contain '/', and this prose has none, so the malformed row passes. The row came in with this build (TOOL-aOrientedCast-3/8). In a full run the 127 shows as a FAIL, which is why this is high rather than blocker. | sound | - |
| 12 | verification | tools/hooks/agent-cap.test.sh:2220 | medium | medium | confirmed | No committed check runs tools/roles/handoff.py. The only grep hits are refusal strings that name it in agent-cap.test.sh and scratch-guard.test.sh. render_agents.py --selftest and adopt-roles.test.sh do not exercise it. The rule 6 arms build their marker and task-sha with an inline Python copy (agent-cap.test.sh:2219-2240). handoff.py hard-codes TASK_LABELS (handoff.py:54). manifest-check.sh:78-80 declares TASK_SKELETON the label source that is read at run time, precisely so that readers cannot diverge. The spec chose this: TOOL-7 section 7 says AC6 runs once at the build pass and 'adds no arm', and TOOL-2 says 'The renderer adds no leg and no suite'. The BY DESIGN list does not cover it, though. The suite comment 'AC6 holds the renderer itself against the hook' sits above the rule 6 arms, where it implies an arm that does not exist (rule6 arms cover AC1-AC5 only). The hook and the renderer can drift in hashed span, CRLF fold or labels with no check going red. No behaviour is wrong today, so the effect is contained (medium). | unsound | two-readers-of-one-config-one-re-derived |
| 13 | intent | tools/run-gates/selftest-budgets.txt:94 | high | medium | confirmed | Confirmed. tools/run-gates/selftest-budgets.txt:94 has 3 tab-separated fields. The other 93 data rows all have 4. read_population (run-selftests.sh:558-561) takes f[2] as argv, which here is the reading prose. Because argv is non-empty, the gate-legs.json lookup for 'roles render selftest' (gate-legs.json:1604, `python {prefix}/roles/render_agents.py --selftest`) is skipped. The serial loop (eval at :1974), the pooled sweep (bash -c at :1272), --attribute (:1842) and foreign-prefix.gov.test.sh, which runs every --list row, all execute 'measured 1.3s ...'. That command exits 127, so render_agents.py --selftest never runs under the self-test runner and the row reports FAIL. --check (:786-806) still passes the row because none of the prose tokens contains a slash. The row was introduced in this diff (TOOL-aOrientedCast-3). Graded medium, not high: the failure is loud (a red row), not a false green. The same self-test still runs as its own manifest leg under run-gates, so its coverage there is intact. | sound | - |
