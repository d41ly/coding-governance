**Serves:** diff-review TOOL-dPavedRoad-1 TOOL-dPavedRoad-2 TOOL-dPavedRoad-3 TOOL-dPavedRoad-4

# Tier-2 diff review — dPavedRoad, the cumulative diff landing on main, ROUND 1

*Finders gov-diff-reviewer (five lenses), skeptic batches gov-skeptic, synthesis gov-synthesizer.*

**Reviewed range:** 14320c985a8b76b0499914f1ff403b9d4fdb8dac...166c1fef7505f9373c9921b7338398b028878c02

## Verdict: CLEAN WITH FIXES

There is no blocker and no high finding. 11 items carry fixes: 5 medium and 6 low. By raw confirmed finding the count is 13: 0 blocker, 0 high, 5 medium, 8 low. One item merges three findings (ids 5, 12, 14) on a single defect.

Neither `specs` nor `context` was supplied to this review. The lenses read only the range's commit messages for intent.

## Review shape

Round 1. Intensity full, raw 14, confirmed 13, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.93.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 7 | 6 | 1 | 0 | 0 | 0 | 0.86 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally: 11 items (0 blocker, 0 high, 5 medium, 6 low). The same tally by raw confirmed finding is 13 (0 blocker, 0 high, 5 medium, 8 low).

## Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fix verdicts on confirmed findings: 12 judged sound, 1 judged UNSOUND (id 3, whose skeptic's corrected fix is written below), 0 instance-only, 0 none proposed, 0 not judged.
- Severity: 0 confirmed findings ungraded by the skeptic. 1 was re-graded by the skeptic (id 13, medium to low).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Checklist: 51 items, each assigned to exactly one of the 5 lenses (security 11, correctness 10, seams 10, verification 10, intent 10).
- By design: none supplied. There was no caller byDesign and the block held 0 entries.
- Refuted findings shown: 1. Same-address pairs shown: 0. No refuted finding is a twin of a confirmed one.
- Every lens and skeptic batch returned. Nothing died, so the run is complete on its own counters.

## Items

### M1 — The spec writer's gate grant admits the full corpus-wide leg, not the `--spec` run it was meant for (id 1, medium)

- **Where:** `tools/roles/house/policy.toml:27`, rendered at `.claude/roles.json:66`.
- **What is wrong:** gov-spec-writer gained the gate grant `spec tokens (a spec's own names resolve)`. scratch-guard's `checkGateLeg` (`tools/hooks/scratch-guard.js:1374-1378`) treats a command as a G1 leg only when its argv exactly equals the leg's argv. That argv is `python {prefix}/check-spec-tokens.py` with no operands (`tools/gate-legs.json:1758-1762`). So `--spec <path>` is never a leg, and every role may run it with or without a grant. The grant's only effect is to admit the bare, corpus-wide leg for the writer. `gov-spec-writer.agent.md:36-38` says the writer runs `--spec` and "run[s] no other gate".
- **Consequence:** The allowlist admits the very run the role's prose forbids. It also reads as if the role gate enforced `--spec`, which will mislead the next change. The command only reads files, so the harm is contained.
- **Fix (skeptic: sound):** Remove `spec tokens (a spec's own names resolve)` from `[gates] gov-spec-writer` in `policy.toml` and re-render `.claude/roles.json`, because `--spec` needs no grant. If the grant is meant to document the self-check, make enforcement match the `--spec` form instead, for example with a leg-variant row whose argv carries `--spec`. In both cases add a scratch-guard suite arm: for agent_type gov-spec-writer, deny the bare `python tools/check-spec-tokens.py` and admit `--spec <path>`.
- **Left-shift gate:** Extend `roles catalogue` / `policy check` so that every role gate grant must name a leg whose argv form the role's agent file actually runs. A grant that admits a run its prose excludes should go red.

### M2 — `brief:prompt` reads the last `## The prompt` section, while the spec-audit reader takes the first (id 2, medium)

- **Where:** `tools/roles/handoff.py:381`.
- **What is wrong:** `brief:prompt` is read with `extract_card_section`, which keeps the LAST matching heading because lines 153-165 reset `found` on every match. `unattended.sh read_audit_ask_record` (`tools/unattended/unattended.sh:3755`) and `extract_brief_section` both stop at the FIRST `## The prompt`. That gives two answers to the question "which section holds the owner's words".
- **Consequence:** On a brief record with a second column-0 `## The prompt` heading, for example one quoted under `## Drawn from the session`, the spec writer's required `brief:prompt` block carries words that are not the owner's, and nothing reports it. A probe confirmed this: handoff returned `second` while the audit reader returned `first owner words`. No record in the repo has two such headings today, so the path is narrow. This diff introduced the divergence.
- **Fix (skeptic: sound):** Read the FIRST `## The prompt` section for `brief:prompt`, matching `unattended.sh` and `PROMPT_HEAD_RE`'s record selection. Use a first-wins extractor, or give `extract_card_section` a first/last parameter. Add one adopt-roles arm whose fixture has two `## The prompt` headings and asserts that the first section is rendered.
- **Left-shift gate:** Add a `roles adopter self-test` arm with a duplicate-heading fixture. Also add a project checklist entry under `two-answers-to-one-question`: every reader of a brief section names the same selection rule.

### M3 — The refusal of climbing, absolute, drive or `-` handoff marker paths has no arm that can fail (id 6, medium)

- **Where:** `tools/hooks/format-guard.js:433-434` (`readHandoffVia`).
- **What is wrong:** This condition is the only filter between a `gov:handoff` marker path and a child-process argv, because `agent-cap.js extractHandoffMarker` matches `path=(\S+)` unfiltered. The suite's one marker (`format-guard.test.sh:464`) uses the safe `memory/builds/tBuild/prompts/x.md`. The `../x` at line 475 is a Workflow runId, not a marker. Spec TOOL-dPavedRoad-2 AC4 has a Red-when for exactly this case.
- **Consequence:** Deleting any clause of the condition leaves `format-guard self-test` green. Today's code is correct, but nothing guards it against a regression.
- **Fix (skeptic: sound):** Add PR2 arms to `format-guard.test.sh` for marker paths `../x.md`, `/abs/x.md`, `C:/x.md` and `-x.md`. Each arm asserts that the stop blocks, that STUB_LOG stays empty, and that the reason keeps the `handoff.py agents --run` sentence. Raise FLOOR_ASSERTIONS by the count.
- **Left-shift gate:** `harness arms (fail branches armed or pinned)` should require an arm for every Red-when a spec AC names. The arms above discharge this one.

### M4 — The primary prompt source, the Agent call's `input.prompt`, is never exercised (id 7, medium)

- **Where:** `tools/hooks/format-guard.js:426` (`readHandoffVia`, lines 424-436).
- **What is wrong:** The function reads `calls.get(toolUseId).input.prompt` first and falls back to `r.prompt`. The suite's `call()` helper (`format-guard.test.sh:450`) always writes `input: {}`. The only marked scenario (line 471) puts the marker on the result's `prompt`, so only the fallback runs. No other suite calls `extractTurnAgents` or `deriveOwedLines`.
- **Consequence:** A real Agent tool_use carries its prompt in `input.prompt`. If that branch broke (a wrong field, or call/result maps keyed wrongly), the suite would stay green while every real marked agent silently lost its derived line. The effect stays inside the derived-line convenience.
- **Fix (skeptic: sound):** Add an `agent-marked-input` scenario whose `call()` puts the marker in `input.prompt` and whose result carries no `prompt`. Assert that the reason holds `- $A1` and that STUB_LOG holds `--handoff memory/builds/tBuild/prompts/x.md`.
- **Left-shift gate:** Add a project checklist entry: a primary-then-fallback read needs one fixture per source, with the fallback absent in the primary's fixture.

### M5 — Under `--staged`, the payload findings' `own` gating has no arm in either direction (id 9, medium)

- **Where:** `tools/memory-tree/check-memory-hygiene.sh:2945` (the `own` guard on the external-sibling arm X and the payloadless arm E, lines 2951-2966).
- **What is wrong:** The PR4 fixture (`check-memory-hygiene.test.sh:4456-4465`) has only `hands-off`/`consumes-from` bullets naming `ARCH-tPair-N`, plus `none` and no-block. It has no `external` bullet naming a sibling and no payloadless bullet. The existing payload arms (test lines 936-942 and 1310) run in full mode only.
- **Consequence:** Removing the `own` guards would let unstaged siblings red a commit for payload defects it did not touch, which is the red on honest work this unit set out to remove. Inverting `own` would silence a staged spec's own payload defect. In either case the suite stays green.
- **Fix (skeptic: sound):** In the PR4 tree, add one unstaged sibling with a `- **hands-off** external — ... ARCH-tPair-7` bullet and one with a payloadless bullet. Assert that neither is reported when an unrelated sibling is staged, and that each is reported when it is staged itself.
- **Left-shift gate:** `memory-hygiene self-test` should hold one staged and one unstaged arm for every finding a `--staged` run gates by ownership.

### L1 — The parity comment names the wrong function as the owner of the empty-to-`unknown` rule (id 3, low)

- **Where:** `tools/hooks/format-guard.js:305`. The doc comment is at lines 283-285.
- **What is wrong:** The comment says mapping an empty value to `unknown` is "render_shape_line's rule in handoff.py". `render_shape_line` (`handoff.py:714-725`) does not map empty values. Its caller does, at `handoff.py:920` (`fields = {k: UNKNOWN if v is None or v == "" else v ...}`). End to end, handoff.py's output matches the hook. Only the named function is wrong.
- **Consequence:** There is no behaviour change. Someone keeping the two ports in step would look for the rule in the wrong function.
- **Fix (skeptic: the finder's fix was UNSOUND; this is the skeptic's corrected fix):** Reword the comment to say that an empty value becomes `unknown` by the rule handoff.py applies to its fields before calling `render_shape_line` (handoff.py line 920). Do not move the mapping into `render_shape_line`.
- **Left-shift gate:** None fits a comment. Add a project checklist entry: a cross-port parity comment cites the file:line of the rule it mirrors.

### L2 — Two conf comments still say `--staged` holds the edge joins (id 4, low)

- **Where:** `tools/memory-tree/.memory-tree.conf.example:100-101` and `.memory-tree.conf:369-372` (the comment above `SPEC_EDGES_CUTOFF`).
- **What is wrong:** TOOL-dPavedRoad-4 replaced the `--staged` hold on check 12's reciprocity, order and payload joins with a narrowed run. It updated HYGIENE.md, HYGIENE.template.md, TEMPLATE-SPEC.md, SPEC-TEMPLATE.template.md and the script header. It missed these two comments, which still say the joins "are held there and say so" and "are HELD under `--staged` with an announce line".
- **Consequence:** These are comments only. An adopter reading the example conf, or a maintainer reading the live conf, is told the opposite of what the script now prints at `check-memory-hygiene.sh:2932`.
- **Fix (skeptic: sound):** Reword both comments to match HYGIENE.template.md. The SHAPE arm grades only the staged specs. The three joins read each staged spec's whole build from the worktree and report an edge when either of its ends is staged. Add both conf comments to the inventory of places that state this behaviour.
- **Left-shift gate:** A grep-based retirement sweep belongs in the unit's close. Any phrase the diff retires (`HELD under --staged`) is searched across tracked files, conf examples included.

### L3 — The check 29/30 skip notice lost its space: `UNEXERCISEDhere` (ids 5, 12, 14, low)

Three lenses found this one defect, so it is a single item.

- **Where:** `tools/memory-tree/check-memory-hygiene.test.sh:4425`.
- **What is wrong:** The TOOL-dPavedRoad-4 commit changed `...so their 24 arms are UNEXERCISED here` to `UNEXERCISEDhere`. No spec asked for this edit. The sibling skip lines at 3529, 3613, 3670 and 4087 keep the space.
- **Consequence:** The effect is cosmetic. The notice prints a run-together word, and a grep for `UNEXERCISED here` misses it. `n_skip` is unchanged, and no reader in `tools/` parses the phrase.
- **Fix (skeptic: sound, on all three):** Restore `...so their 24 arms are UNEXERCISED here`.
- **Left-shift gate:** None fits. Add a project checklist entry: a build commit's diff touches no line outside its spec's named surface. A hunk-to-spec scope check at close would catch it.

### L4 — The rule that withholds an off-shape derived line has no arm (id 8, low)

- **Where:** `tools/hooks/format-guard.js:595-597`.
- **What is wrong:** S3 of TOOL-dPavedRoad-2 claims to be "Observed by AC5, AC10 and AC11". However, the stub (`format-guard.test.sh:505-520`) prints only on-shape lines (A1, R1, A2, A3, R2, R3), and no arm greps for `off its charter shape`. Only AC5's one-shot probe at close ever saw the rule go red.
- **Consequence:** If the shape filter were dropped (for example to `carrying[0]`), the suite would stay green and the block reason could print a line that does not clear its defect when pasted. The pasted line would simply be blocked again, so the effect is small.
- **Fix (skeptic: sound):** Give the stub a selector or flag file under which it prints one off-shape `- agent — … /a1` line. Assert that the reason does not contain it, that the `handoff.py agents` sentence stays, and that stderr holds `off its charter shape`.
- **Left-shift gate:** `harness arms (fail branches armed or pinned)` should require every "Observed by" claim in a spec to name an arm that greps the claimed witness.

### L5 — The `--spec` suppression of stale high-water rows has no arm (id 11, low)

- **Where:** `tools/check-spec-tokens.py:1875-1876` (`sz_stale = []` under `named_specs is not None`).
- **What is wrong:** The onespec fixture is built by `scratch()` (test lines 341-367), which writes no `template-size-highwater.txt`, and the PR1 block adds none. The only high-water arms live in the size fixture (lines 1402-1425), which never runs `--spec`.
- **Consequence:** Deleting line 1876 leaves all seven PR1 arms green. A writer running `--spec` in a tree that holds a high-water row for another live spec would then get a false STALE HIGH-WATER red. The guard is correct today.
- **Fix (skeptic: sound):** In the onespec fixture, write a high-water row for the tracked tOne-1 spec, padded past the ceiling as in lines 1402-1425. Assert that the `--spec $os_spec` run carries no `STALE HIGH-WATER` row, and raise FLOOR_ASSERTIONS.
- **Left-shift gate:** `spec-tokens self-test` should seed every population a `--spec` suppression empties, so each suppression has a row to suppress.

### L6 — `--spec` skips the two stale-row arms silently and reports `0 stale row(s)` (id 13, low; finder graded medium, skeptic re-graded low)

- **Where:** `tools/check-spec-tokens.py:1876` (stale high-water), about line 1931 (stale-waiver loop over `()`), and the summary at line 2057.
- **What is wrong:** S2 of TOOL-dPavedRoad-1 (`memory/builds/dPavedRoad/spec/2026-11-10-spec-TOOL-dPavedRoad-1.md:27-31`) says each of the four arms `--spec` does not run "says so on its report line". Only the carries and packet joins say so. The two stale arms are emptied silently, and a red `--spec` run ends with `N unwaived hit(s), 0 stale row(s)`. The spec also contradicts itself, because its section 4 (line 137) says "Every other line keeps its text".
- **Consequence:** An arm that never graded anything reports zero, so an empty population reads as a pass. The exit code is correct. The summary line prints only on a run that is already red, and the full run at close grades both stale arms. The skeptic graded this low because the only effect is misleading report text. This report adopts the skeptic's grade.
- **Fix (skeptic: sound):** Under `named_specs is not None`, print one line such as `spec-tokens: stale-waiver and stale high-water arms · skipped under --spec`. Drop `0 stale row(s)` from the line-2057 summary, or replace it with `stale rows not graded`. Add a suite arm that greps for the line under `--spec`. Alternatively, revise S2 to match section 4 so that the spec states one rule.
- **Left-shift gate:** `spec-tokens self-test` should require a `skipped under --spec` arm for each arm `--spec` does not run.

## Refuted

id 10 (verification, `tools/memory-tree/check-memory-hygiene.sh:3505`) was refuted as by design. The script header (lines 3369-3374) and spec TOOL-dPavedRoad-4 §3/§4 both state that a cross-build record evidencing a graded unit is read only by the full run. It is not a twin of any confirmed finding. It is not reinstated or counted.

review-shape kind=diff-review round=1 intensity=full at=synth raw=14 confirmed=13 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=5 low=8 agents=11 out-tokens=96897
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/roles/house/policy.toml:27 | medium | medium | confirmed | This diff adds the grant at policy.toml:27 and the rendered copy at .claude/roles.json:66. checkGateLeg (scratch-guard.js:1374-1378) matches a leg only when the argv has the same length and the same words. The leg's argv is `{prefix}/check-spec-tokens.py` with no operands (gate-legs.json:1758-1762). So a `--spec <path>` run is never a G1 leg. It is not a G2 runner or a G3 suite either, so checkRoleGate admits it for every role whether or not the role holds a grant. The only thing the grant changes is that the bare corpus-wide leg is now admitted for gov-spec-writer. gov-spec-writer.agent.md:36-38, also changed in this diff, says the writer may run `--spec` and "run no other gate". The allowlist therefore admits the run the prose forbids, and it reads as if the role gate enforced `--spec`. The consequence is contained: the command only reads, and the prose and the allowlist are misleading. | sound | - | new:grant-admits-the-leg-not-its-variant |
| 2 | correctness | tools/roles/handoff.py:381 | medium | medium | confirmed | handoff.py:381 reads brief:prompt with extract_card_section, which keeps the LAST matching heading (lines 153-165 reset `found` on every match). unattended.sh read_audit_ask_record (line 3755) turns on at the first `## The prompt` and exits at the next `## ` heading, so it reads the FIRST section. extract_brief_section reads the first match too. On a record with two column-0 `## The prompt` headings, the two readers disagree. The writer's required brief:prompt block then carries the later text, and nothing reports it. No record in this repo has two such headings, so the path is narrow, but this diff introduced the divergence. | sound | - | class:two-answers-to-one-question |
| 3 | correctness | tools/hooks/format-guard.js:305 | low | low | confirmed | The comment at format-guard.js:283-285 says the empty-to-`unknown` mapping is render_shape_line's rule. render_shape_line (handoff.py:714-725) does not map empty values. The mapping lives in its caller in handoff.py at line 920 (`fields = {k: UNKNOWN if v is None or v == "" else v ...}`), so what handoff.py prints end to end matches the hook. Only the function the comment names is wrong. It has no effect on behaviour. | unsound | - | new:parity-comment-names-the-wrong-function |
| 4 | seams | tools/memory-tree/.memory-tree.conf.example:100 | low | low | confirmed | At 166c1fef7, tools/memory-tree/.memory-tree.conf.example:100-101 still says the reciprocity, order and payload JOINS 'are held there and say so'. .memory-tree.conf:369-372 still says they 'are HELD under `--staged` with an announce line'. The diff rewrote the matching lines in memory/HYGIENE.md and HYGIENE.template.md ('read each staged spec's whole build from the worktree and report an edge either of whose ends is staged'), and check-memory-hygiene.sh:2932 now prints that the joins grade each staged spec against its build. So the diff made both comments wrong. They are comments only and change no behaviour. | sound | retirement-inventory-misses-readers-by-value | class:retirement-inventory-misses-readers-by-value |
| 5 | seams | tools/memory-tree/check-memory-hygiene.test.sh:4425 | low | low | confirmed | At 14320c985, check-memory-hygiene.test.sh:4425 reads 'their 24 arms are UNEXERCISED here'. At 166c1fef7 it reads 'UNEXERCISEDhere'. Every other skip line in the file (3529, 3613, 3670, 4087) keeps the space. Only the echoed text is affected; the n_skip count is unchanged. | sound | - | new:unrequested-edit-rides-a-unit-commit |
| 6 | verification | tools/hooks/format-guard.js:433 | medium | medium | confirmed | format-guard.js:433-434 (readHandoffVia, added by this diff) returns null for a marker path that is absolute, drive-qualified, starts with '-', or holds a '..' segment. agent-cap.js extractHandoffMarker matches path=(\S+) and filters nothing, so this condition is the only filter. The one gov:handoff marker in format-guard.test.sh (line 464) uses the safe path memory/builds/tBuild/prompts/x.md. The PR2 block (606-639) never uses a climbing, absolute, drive or '-' path, and the '../x' at line 475 is a runId. Spec TOOL-dPavedRoad-2 AC4 has a Red-when for exactly this case ('a climbing path reaches via'), yet deleting any clause of the condition leaves the suite green. The effect is contained: today's code is correct and nothing guards it against a future regression. | sound | rule-stated-with-no-check-that-fails | class:rule-stated-with-no-check-that-fails |
| 7 | verification | tools/hooks/format-guard.js:426 | medium | medium | confirmed | readHandoffVia (format-guard.js:424-436) is new in this diff; base has no readHandoffVia. It reads calls.get(toolUseId).input.prompt first and falls back to r.prompt. The suite's call() helper at format-guard.test.sh:450 always writes `input: {}`. The only marked scenario, agent-marked at line 471, puts the marker on the result's `prompt`. No other suite calls extractTurnAgents or deriveOwedLines (I grepped tools/). So the input.prompt branch, which is the primary source, never runs in the gate. Breaking it would leave the suite green. The effect stays inside the derived-line convenience. | sound | - | new:fixture-exercises-only-the-fallback |
| 8 | verification | tools/hooks/format-guard.js:595 | low | low | confirmed | The withholding rule at format-guard.js:595-597 (find a line matching shapes[q.head].re, otherwise the witness 'off its charter shape') is new. The stub at format-guard.test.sh:505-520 prints only A1, R1, A2, A3, R2 and R3, and all of them are on-shape. No arm greps for 'off its charter shape' (I grepped the suite), and no suite calls deriveOwedLines directly. Spec dPavedRoad-2 S3/AC5 describes a probe, not a gate arm. Dropping the shape filter would leave the gate green. If that happened, a pasted line would simply be blocked again, so the effect is small. | sound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 9 | verification | tools/memory-tree/check-memory-hygiene.sh:2945 | medium | medium | confirmed | At base the --staged run held the edge joins entirely. The `own` guard on the external-sibling arm (X) and the payloadless arm (E) at check-memory-hygiene.sh:2951-2966 is new. The PR4 fixture (test lines 4456-4465) declares only `- **hands-off**/**consumes-from** \`ARCH-tPair-N\`` bullets, plus `none` and no-block. None is an `external` bullet naming a sibling and none is a payloadless bullet, so neither direction of `own` on those arms is exercised under --staged. The payload arms that do exist run in full mode only. Removing or inverting `own` would leave the suite green. | sound | - | class:rule-stated-with-no-check-that-fails |
| 10 | verification | tools/memory-tree/check-memory-hygiene.sh:3505 | medium | - | refuted | This is by design, and the diff says so. The script header at tools/memory-tree/check-memory-hygiene.sh:3369-3374 states that under --staged both listings keep only `_SBUILD` folders and that 'a record in another build evidencing a graded unit is read only by the full run'. So the header does not contradict the behaviour; it describes it. The unit's spec, memory/builds/dPavedRoad/spec/2026-11-10-spec-TOOL-dPavedRoad-4.md, also declares 'No cross-build ledger read under `--staged`' as a non-goal (§3, around line 63) and measures 0 of 1210 Evidences lines as cross-build. Its §4 HYGIENE bullet repeats that such a record 'is read only by the full run'. The tOther fixture record is placed on purpose to prove AC4: the record stream must not read past `_SBUILD`. A staged tOther record therefore selects nothing under --staged, as the spec intends, and the full run still grades it. | unsound | invariant-held-on-one-admission-path | - |
| 11 | verification | tools/check-spec-tokens.py:1876 | low | low | confirmed | This diff introduced `sz_stale = []` under `named_specs is not None` (tools/check-spec-tokens.py:1875-1876). The base has no such line. The new onespec fixture (check-spec-tokens.test.sh, the PR1 block) is built by `scratch()` (lines 341-367). That function writes no template-size-limits.txt and no template-size-highwater.txt, and the PR1 block adds neither. So no high-water row exists for the one-spec population to mark stale. The only high-water arms are in the separate size fixture (lines 1402-1425), which never runs --spec. Deleting line 1876 would therefore leave every PR1 arm green. The guard is correct today, so this is a test gap with no current wrong output. | sound | - | class:fixture-passes-by-finding-nothing |
| 12 | verification | tools/memory-tree/check-memory-hygiene.test.sh:4425 | low | low | confirmed | The diff changes the line at check-memory-hygiene.test.sh:4425 from 'UNEXERCISED here' to 'UNEXERCISEDhere'. The base read 'UNEXERCISED here', and the sibling skip lines at 3529, 3613, 3670 and 4087 all still read 'UNEXERCISED here'. A search of tools/ found no script that parses the phrase, so the effect is cosmetic. | sound | - | new:unrequested-edit-rides-a-unit-commit |
| 13 | intent | tools/check-spec-tokens.py:1876 | medium | low | confirmed | The spec text and the code match the finding. S2 of memory/builds/dPavedRoad/spec/2026-11-10-spec-TOOL-dPavedRoad-1.md (lines 27-31) says each of the four arms that do not run 'says so on its report line', and it names the stale-waiver and stale high-water arms. In tools/check-spec-tokens.py, both arms are emptied silently under --spec: line 1876 sets `sz_stale = []`, and the waiver loop at about 1931 iterates `()`. No line says these arms were skipped, while the carries and packet lines do say 'skipped under --spec'. A red --spec run ends with `N unwaived hit(s), 0 stale row(s)` (line 2057), which reports zero for arms that never ran. The diff introduced this, because --spec is new. The spec is also inconsistent: section 4 (line 137) says 'Every other line keeps its text'. The consequence is contained. The exit code is correct; that summary line prints only on a run already red for hits; the docstring says a --spec green is not the bar's green; and the full run at close grades both stale arms. So the only effect is misleading report text, which I grade low. | sound | - | class:vacuous-selector-empty-population |
| 14 | intent | tools/memory-tree/check-memory-hygiene.test.sh:4425 | low | low | confirmed | The base 14320c98 has `...so their 24 arms are UNEXERCISED here` at tools/memory-tree/check-memory-hygiene.test.sh:4425. The diff changes it to `UNEXERCISEDhere`. No spec asks for this, and all four sibling skip messages (lines 3529, 3613, 3670, 4087) keep `UNEXERCISED here`. The effect is cosmetic: the n_skip count is unchanged. | sound | - | new:unrequested-edit-rides-a-unit-commit |
