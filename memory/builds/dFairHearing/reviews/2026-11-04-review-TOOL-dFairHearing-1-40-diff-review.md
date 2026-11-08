**Serves:** diff-review TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40

# Tier-2 diff review — Build dFairHearing, the 38 units reworking the review harness

Provenance: tier2-review harness, kind diff-review, round 1, intensity full, five lenses (security, correctness, seams, verification, intent), skeptic-verified, synthesized 2026-11-04 on branch/unattended-dfairhearing-fe4e9c. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

Reviewed: 8bec4cefd957d194660a8d7c2916f420b7299074...bc4bb6e1751a3f0229c22ac3cb56090603ff0d5c

Round: 1

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or a high. The 8 confirmed findings form 8 items: 5 medium and 3 low.

Each one needs a fix or a gate before the build closes.

The run is complete, since every lens and every skeptic batch returned.

Review shape: intensity full, raw 9, confirmed 8, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.89. Adjudicated tally by item: 8 items (0 blocker, 0 high, 5 medium, 3 low). By raw confirmed finding: 8 (0 blocker, 0 high, 5 medium, 3 low).

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 0 | 1 | 0 | 0 | 0 | 0.00 |

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified.
- Merges and discards: 0 duplicate refutations were counted as merged confirmations, 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 8 judged sound, 0 UNSOUND, 0 INSTANCE-ONLY, 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic and 1 RE-GRADED by the skeptic (id 1, high to medium).
- Unverified findings: 0 answered UNCERTAIN and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 1 spec document was supplied as `specs`, read beside the range's commit messages.
- Checklist: the harness acquired 62 items from `--for-diff 8bec4cefd957d194660a8d7c2916f420b7299074..HEAD`, each assigned to one lens: security 13, correctness 13, seams 12, verification 12, intent 12.
- By design: no caller `byDesign` was supplied, and the block held 0 entries.
- The record shows 1 refuted finding and 0 same-address pairs.
- Dispositions: unclassed is `refuse`. The run was handed 62 class slugs and read 149 leg names from tools/gate-legs.json.
- Twins: no refuted finding reads as the same defect as a confirmed one. Refuted id 9 is a help-page wording claim about `MAX_VERIFIERS`, and confirmed id 8 is a check_policy.py comment about rule 5's coverage. They are different defects.

## Items

### 1. MEDIUM — the checklist agent's command line pastes unchecked `base` and `head` (id 1)

- **Where:** tools/workflows/tier2-review.template.js:1428, and the rendered tools/workflows/tier2-review.js:1523.
- **What is wrong:** The checklist agent added by TOOL-dFairHearing-15 is told to run `python <checker> --for-diff ${base}..${head}`, with the caller's raw `base` and `head` pasted in unquoted. At round 1 nothing validates either value before this agent spawns. `head` (line 250, `a.head || 'HEAD'`) is never checked. `base` gets only a WARNING log when it is not 7 to 40 hex characters (lines 968-976).
- **Consequence:** A call with `head: 'HEAD; <cmd>'` or `base: 'abc $(<cmd>)'` logs a warning and goes on. The first agent spawned has a shell, and its prompt tells it to run a line carrying `<cmd>`. That breaks the harness's rule that it refuses unsafe args before any agent. The same diff refuses `"`, `$` and a backtick in `repo` (S33) for this very reason.
- **Grade:** medium, the skeptic's binding grade (the finder graded high). The class predates this diff: at the base, the resume probe already pasted raw `${base}^{commit}` and `${head}^{commit}` into a `git rev-parse` line (base:1021, now 1597). Both fields come from the calling session, not from outside input.
- **Fix (judged SOUND by the skeptic):** Before the checklist spawn, at every round, refuse any `base` or `head` that does not match a closed ref grammar, and name the field in the error. An example grammar is `/^[0-9A-Za-z._\/~^-]+$/` with no leading `-`, or PINNED_SHA for `base`. A better fix is to have the agent run the command on the probe-resolved FULL_SHA `baseSha`/`headSha`. Required probe: call the harness at round 1 with `head:'HEAD;echo PWNED'` and no checklist, and assert that it throws before the first `agent()` call.
- **Left-shift gate:** add a tier2-review.test.sh arm that drives every caller field that reaches a prompt's shell line (`base`, `head`, `repo`) with a metacharacter value, and asserts a refusal before any agent spawns. This also covers the resume probe at line 1597.

### 2. MEDIUM — checkDisposition and renderCell disagree on how a `none` reason's cell is encoded (id 2)

- **Where:** tools/workflows/tier2-review.template.js:3053 (checkDisposition), :2445 (renderCell) and :2752-2753 (the DISPOSITIONS prompt).
- **What is wrong:** checkDisposition refuses a `none` reason that holds a raw `|` or a line break, saying it would break its appendix row. renderCell already folds line breaks and escapes every `|` as `\|`, so the check refuses the one spelling that round-trips cleanly. The spelling the prompt asks for, a pipe written as `\|`, passes the check. renderCell then escapes it a second time, and it reads back with a stray backslash. The two rules come from TOOL-dFairHearing-8 and -23.
- **Consequence:** If the reason holds a raw `a | b`, the whole disposition set is refused. Dispositions become null, every appendix disposition cell stays `-`, and an owner-rules run raises no owner items. If the reason is written `a \| b`, renderCell emits `a \\| b`, and replay_scorer reads it back as `none — a \| b`. The skeptic's probe confirmed both paths.
- **Grade:** medium, binding. The effect stays inside the disposition cells and the owner items.
- **Fix (judged SOUND by the skeptic):** Let renderCell own the cell encoding. Drop the raw-pipe and line-break arm from checkDisposition's `none` branch, and keep only the non-empty-reason test. Reword the DISPOSITIONS prompt so it no longer asks for a pipe written as `\|`. Add a tier2-review.test.sh arm that takes a `none` reason holding a raw `|` and a newline through the disposition check and renderAppendix. The arm asserts that the set is accepted and that replay_scorer.parse_appendix_rows reads back the reason as written.
- **Left-shift gate:** the round-trip arm above. It fails whenever the writer's encoding and the reader's decoding disagree.

### 3. MEDIUM — unattended-build's audit forward drops the `twin` and `unclassed` pin arguments (id 3)

- **Where:** tools/workflows/unattended-build.template.js:1752-1759, with the args block at :230-239.
- **What is wrong:** The audit call forwards only `optIn`, `preset` and `lensNotes` from review_pin.py's output, under a comment saying they go "as `review_pin.py` printed them". review_pin.py:121-124 also prints `twin` and `unclassed` as review-call arguments. Those keys are not forwarded, not refused and not documented. A grep for `twin|unclassed|fixJudge` in the template returns nothing.
- **Consequence:** A caller who passes a pinned `twin: "always"` or `unclassed: "reason"` gets a tier2-review run at the defaults `twin: never` and `unclassed: refuse` (tier2-review.template.js:322/334), and nothing logs the change. The audit then reports an untwinned, refuse-classed run as if it had honoured the pin.
- **Grade:** medium, binding. The effect stays inside the audit's policy and corrupts no data.
- **Fix (judged SOUND by the skeptic):** Forward `twin`, `unclassed` and `fixJudge` the same way, e.g. `...(a.twin !== undefined ? { twin: a.twin } : {})`. Document them in the args block at lines 230-239. Add an arm to unattended-build.test.sh that asserts the audit call carries a passed `twin`. The alternative is to refuse those keys by name at unattended-build's boundary.
- **Left-shift gate:** an unattended-build.test.sh arm that takes every key review_pin.py prints and asserts each is either forwarded or refused by name. A new pin key then fails the suite until it gets a route.

### 4. MEDIUM — spec-audit-optin.js finds the hooks kit at a hard-coded sibling path (id 4)

- **Where:** tools/workflows/spec-audit-optin.js:24, with its counterpart at tools/hooks/agent-cap.js:965.
- **What is wrong:** The pack, new in this diff, loads its required readers (agent-cap.js, scratch-guard.js) only from `dirname(__dirname)/hooks`. agent-cap's checkOptinPackPresent finds the pack through resolveKitDir, which reads the install receipt first. The two sides of one seam resolve the same sibling by different rules.
- **Consequence:** If an adopter homes the hooks kit somewhere else through a receipt row, agent-cap sees the pack and admits the call. The pack's loadReaders then throws, and the deny at :259-261 blocks every spec-audit Workflow call. Its message says "Install the hooks kit beside the review kit" even though the kit is installed.
- **Grade:** medium, binding. Renamed-home installs are a narrow path, and the result is a false deny, not a false admit.
- **Fix (judged SOUND by the skeptic):** Resolve HOOKS_DIR with an inline copy of the resolveKitDir block, `resolveKitDir('hooks', 'agent-cap.js', __dirname)`. Hold that copy to resolve_kit_dir.py through resolve-python.test.sh's parity table, as agent-cap's copy is held. Add a spec-audit-optin.test.sh arm whose receipt row places the hooks kit outside `<prefix>/hooks/`, and assert that it admits a dated opt-in.
- **Left-shift gate:** the resolve-python parity table, extended to the new copy, plus a static ban on a hard-coded `dirname(__dirname)/<kit>` sibling path in kit code.

### 5. MEDIUM — the AC19 quoting arm drives only the diff preset but claims every prompt (id 7)

- **Where:** tools/workflows/tier2-review.test.sh:734-746.
- **What is wrong:** The FH40 AC19 arm says every `git -C` quotes `repo`, but it builds only `DIFF` with repo `C:/x y/z`. Three spec-only sites are left unchecked: the probe's hash-object ask (template:1594), and the spec acquire sentence's hash-object (1823) and diff (1825). The only spec-prompt checks, at lines 2216 and 2219, test the substrings without the quoting. The skeptic corrected one part of the finding. The round-2 fold line at 1765 is covered by line 2190's exact `git -C "/tmp/r" diff P40 D40` assertion.
- **Consequence:** If any of the three sites goes back to a bare `git -C ${repo}`, the suite stays green. A spec audit on a repo path with a space would then split the path in every lens's and the probe's hash-object command.
- **Grade:** medium, binding. This is a test-coverage gap with no runtime effect.
- **Fix (judged SOUND by the skeptic):** Run the same spaced-repo check over SPEC at round 1, and over a SPEC round-2 fold whose subject's prevBlob differs from its blob. Assert that every `git -C` match in those traces equals `git -C "C:/x y/z"`. Then confirm the suite goes red when the quotes are stripped from line 1594 or 1823 alone, and raise FLOOR_ASSERTIONS by the number of arms added.
- **Left-shift gate:** the arm above, driven over every preset the harness ships, not over one.

### 6. LOW — check_ungated has no caller outside its selftest (id 5)

- **Where:** tools/memory-tree/gotchas.py:433, with the check_gate_token docstring at :405.
- **What is wrong:** This diff added `check_ungated`, `extract_gated_scope` and the GATED_* regexes, and units 23, 27, 32 and 37 refined them. The `--all-ungated` flag that would call them never landed. Grepping tools/ and skills/ finds only the definition, the docstrings and the selftest arms at 979-1017. The docstring at 405 says `check_ungated` "counts it ungated and announces it as a note", as if a live path called it.
- **Consequence:** The code is dead outside the selftest. The next change may assume that an ungated-class reader is wired when nothing calls it.
- **Grade:** low, binding. Nothing breaks at runtime.
- **Fix (judged SOUND by the skeptic):** State in both docstrings that `check_ungated` has no caller until a `--all-ungated` flag lands, or remove it until that unit. If it stays, record it in the bug-class checklist so the flag's unit wires it in.
- **Left-shift gate:** a bug-class checklist entry for a function whose only caller is its own selftest, since no current leg finds such code.

### 7. LOW — kit.toml names the leg-manifest argument `legManifest`, but the harness reads `gateManifest` (id 6)

- **Where:** tools/workflows/kit.toml:78.
- **What is wrong:** The comment says the default `TOOL_ROOT` fills "its `legManifest` argument". The harness reads `a.gateManifest` (tier2-review.template.js:896, rendered :181, 886, 894), and README.md:431/446 also say `gateManifest`. Nothing in tools/ reads `legManifest`.
- **Consequence:** An adopter who follows the descriptor and passes `legManifest` has it silently ignored. Every `gate:` disposition is then judged against `{{TOOL_ROOT}}gate-legs.json`, not against the manifest the caller chose.
- **Grade:** low, binding. Only a comment is wrong, and the README and the harness's input block both name the right key.
- **Fix (judged SOUND by the skeptic):** Rename it to `gateManifest` in the kit.toml comment.
- **Left-shift gate:** extend the spec-tokens leg, or a sibling check, so a backticked argument name in a kit.toml comment must resolve to an `a.<name>` read in the kit's harness.

### 8. LOW — a check_policy.py comment says limit-hook-writer-split runs rule 5's check, but it does not (id 8)

- **Where:** tools/policy/check_policy.py:2947-2948, in `limit-hook-rules-kept`. The writer-split case is at about lines 3018-3043.
- **What is wrong:** The new comment says rules 2 and 5 left the hook for the review kit, "whose checks `limit-hook-writer-split` runs". That case runs only check-verifier-fanout.js, which holds rule 2. Nothing in check_policy.py runs check-review-join.js, which holds rule 5. Meanwhile the same edit flipped the ref-keyed-join row from `has("ref-keyed verdict join")` to `admits`.
- **Consequence:** A reader will think this suite still exercises rule 5's ref-keyed-join ban under a landed limit. Only check-review-join.test.sh (line 271) checks it, so a later edit that drops that arm would look covered here.
- **Grade:** low, binding. The defect is in a comment only, and no behaviour changes.
- **Fix (judged SOUND by the skeptic):** Narrow the comment to say that rule 2 is check-verifier-fanout.js, which `limit-hook-writer-split` runs, and rule 5 is check-review-join.js, checked by check-review-join.test.sh. Or add one row in the `limit-hook-writer-split` style that runs check-review-join.js over a `m.set(f.ref, v)` case and expects exit 1.
- **Left-shift gate:** the added check-review-join.js row. It turns the comment's claim into an executed check.

## Dispositions

| id | disposition | reason |
|---|---|---|
| 1 | new:unvalidated-arg-reaches-an-agent-shell-line | A caller field reaches a shell-holding agent's command line without passing a closed grammar. No handed class names that. |
| 2 | class:pipe-in-a-code-span-splits-a-table-cell | The defect is how a pipe is encoded in an appendix table cell, where the check and the renderer disagree. |
| 3 | class:policy-value-with-no-route | The pinned `twin` and `unclassed` policy values have no route from unattended-build to the review harness. |
| 4 | class:two-answers-to-one-question | agent-cap and the pack answer "where is the sibling kit" by two different rules. |
| 5 | new:helper-whose-only-caller-is-its-selftest | Code that is refined over several units but called only by its own selftest. No handed class names that. |
| 6 | new:doc-names-an-argument-the-code-never-reads | A descriptor comment names an argument key the harness never reads. |
| 7 | class:criterion-asserts-what-its-own-command-cannot-show | The arm's label claims every prompt, but its command drives only the diff preset. |
| 8 | new:comment-claims-a-check-the-case-does-not-run | A test comment attributes coverage to a case that does not execute the named check. |

review-shape kind=diff-review round=1 intensity=full at=synth raw=9 confirmed=8 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=5 low=3 agents=11 out-tokens=83026
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/workflows/tier2-review.template.js:1428 | high | medium | confirmed | The claim holds. template:1428 (rendered tier2-review.js:1523) pastes raw `${base}..${head}` into a shell command line for the new checklist agent. `head` (line 250) is never validated. `base` only gets a log('WARNING') at round 1 (lines 968-977). The checklist spawn at line 1421 is the first agent, and it comes before the resume probe. The class is not new, though. At the base commit, the resume probe already pasted raw `${base}^{commit}` and `${head}^{commit}` into a `git rev-parse` line (base:1021, now 1597). So the same caller-supplied fields already reached a shell-holding agent's prompt, and the diff adds a second instance rather than opening a new hole. Both fields are set by the calling session, not by outside input. I grade it medium: the containment was already broken before this diff. | sound | - | new:unvalidated-arg-reaches-an-agent-shell-line |
| 2 | correctness | tools/workflows/tier2-review.template.js:3053 | medium | medium | confirmed | Confirmed against the code. renderCell (line 2445) is renderPromptLine, which folds line breaks, plus `.replace(/\\|/g,'\\\|')`. Line 3097 builds the cell as 'none — ' + x.reason, and renderAppendix passes it through renderCell. checkDisposition line 3053 refuses `/(^\|[^\\])\\|\|[\r\n]/`, so it rejects a raw pipe or newline that renderCell would have encoded safely. The DISPOSITIONS prompt (line 2753) asks for a pipe written as `\\|`. That spelling passes the check, and renderCell then escapes it again as `\\\|`. replay_scorer CELL_SPLIT `(?<!\\)\\|` does not split there, and its replace('\\\|','\|') leaves `a \\| b`, which carries a stray backslash. Both sides of the disagreement come from this range (TOOL-dFairHearing-8 and -23), and checkDisposition is absent at the base. A refusal sets the whole dispositions set to null, so the effect stays inside the disposition cells and the owner items. That makes it medium. | sound | pipe-in-a-code-span-splits-a-table-cell | class:pipe-in-a-code-span-splits-a-table-cell |
| 3 | seams | tools/workflows/unattended-build.template.js:1755 | medium | medium | confirmed | At unattended-build.template.js:1752-1759 the audit call forwards only a.optIn, a.preset and a.lensNotes, under a comment saying they go 'as `review_pin.py` printed them'. review_pin.py:121-124 also prints `twin` and `unclassed` as review-call arguments. A grep of unattended-build.template.js for twin, unclassed or fixJudge finds nothing: those keys are not forwarded, not refused, and not in the args block at 230-239. tier2-review.template.js:322 and :334 then fall back to 'never' and 'refuse'. The forward is new in this diff (TOOL-dFairHearing-3 S10, -9 S5) and the pin keys came from units 8 and 11, so the seam gap belongs to this diff. A caller that copies review_pin's whole line into unattended-build loses its twin and unclassed policy without a word. The effect stays inside the audit's policy and does not corrupt data, so it is medium. | sound | - | class:policy-value-with-no-route |
| 4 | seams | tools/workflows/spec-audit-optin.js:24 | medium | medium | confirmed | spec-audit-optin.js is new in this diff (it is absent at the base). Line 24 hard-codes HOOKS_DIR to dirname(__dirname)/hooks, and loadReaders requires agent-cap.js and scratch-guard.js only from there. agent-cap.js:965 finds the pack through resolveKitDir('workflows','spec-audit-optin.js',__dirname), which reads the receipt first; resolve_kit_dir.py says it exists for kits an adopter has homed under a renamed directory. On an install where the hooks kit is homed through a receipt row and is not a sibling 'hooks' dir, agent-cap admits the call because the pack is present. The pack's loadReaders then throws, and the deny at :259-261 blocks every Workflow call that may be a spec audit, saying 'Install the hooks kit beside the review kit', even though the hooks kit is installed. The path is reachable on renamed-home installs, which is narrow, and its effect is a false deny rather than a false admit, so it is medium. No other workflows/*.js hard-codes a sibling hooks dir. | sound | - | class:two-answers-to-one-question |
| 5 | seams | tools/memory-tree/gotchas.py:433 | low | low | confirmed | `check_ungated`, `extract_gated_scope` and the GATED_* regexes are not at base 8bec4cef, so this diff added them. Grepping tools/ and skills/ for check_ungated or all-ungated finds hits only in tools/memory-tree/gotchas.py: the definition at 433, the check_gate_token docstring at 405, and the selftest arms at 979-1017. There is also a stale .pyc. No `--all-ungated` flag exists anywhere. Spec TOOL-dFairHearing-23 line 134 says there is no such flag yet and that whichever unit adds one will call `check_ungated`. So the code is dead outside the selftest. The docstring at 405 says it 'counts it ungated and announces it as a note' as if something calls it, which could mislead the next reader. Nothing breaks at runtime, so this is low. | sound | - | new:helper-whose-only-caller-is-its-selftest |
| 6 | seams | tools/workflows/kit.toml:78 | low | low | confirmed | kit.toml:78 calls the default `TOOL_ROOT` fills 'its `legManifest` argument'. The rendered harness reads `gateManifest` (tier2-review.js:181, 886, 894), and README.md:431/446 also say `gateManifest`. Grepping tools/ for legManifest finds only this comment. The base kit.toml has no legManifest, so this diff introduced it. Only a comment is wrong, and the README and the harness's own input block name the right key, so this is low. | sound | - | new:doc-names-an-argument-the-code-never-reads |
| 7 | verification | tools/workflows/tier2-review.test.sh:736 | medium | medium | confirmed | Partly true. The FH40 AC19 arm at tier2-review.test.sh:734-746 builds only `DIFF` with repo 'C:/x y/z'. The spec-only quoted sites at template lines 1594 (probe hash-object), 1823 (hash-object) and 1825 (`diff <blob> -- <path>`) sit in isSpec branches. No assertion in the suite checks that those sites are quoted: line 2216 checks only for the substring 'hash-object', and line 2219 only for 'diff <blob> -- <path>'. So if any of them went back to a bare `git -C ${repo}`, the suite would stay green, and the arm's label 'every prompt' claims more than it checks. One correction to the finding: the fold line at 1765 IS covered. Line 2190 asserts the exact line `git -C "/tmp/r" diff P40 D40` on a round-2 SPEC fold, so stripping the quotes there would turn the suite red. The gap is a test-coverage gap with no runtime effect, so medium. | sound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 8 | verification | tools/policy/check_policy.py:2948 | low | low | confirmed | This diff introduced the comment at check_policy.py:2947-2948 (commit 886c11fea) and changed the ref-keyed-join row from has("ref-keyed verdict join") to admits. The limit-hook-writer-split case (around lines 3018-3043) only invokes check-verifier-fanout.js. grep finds no reference to check-review-join in check_policy.py. So the comment's claim that writer-split runs the review kit's checks for both rule 2 and rule 5 is wrong for rule 5, which only check-review-join.test.sh exercises (line 271, the m.set(f.ref, v) case). The defect is in a comment only, with no behaviour change. | sound | - | new:comment-claims-a-check-the-case-does-not-run |
| 9 | intent | help/agent-limit.md:10 | low | - | refuted | help/agent-limit.md:10-11 does say the verify total 'is the agent-cap hook's `MAX_VERIFIERS`', and this diff does not touch the page. But the sentence is still true: tools/hooks/agent-cap.js:400 still defines `const MAX_VERIFIERS = 5`, and :395 records that the constant stays there even though no rule in the file reads it. The sentence names where the number lives. It does not say the hook enforces it when a call is made. The section the finder points to, 'What the agent-cap hook refuses' (line 49 on), describes only rule 7, so nothing on the page says the hook bounds a Workflow's verify stage. Other current docs use the same wording: tools/hooks/README.md:9 ('the verify-stage TOTAL is `agent-cap.js`'s `MAX_VERIFIERS`'), memory/guides/REVIEW-PROTOCOL.md:7-9, and WIRE-INTO-PROJECT.md:998 ('the hook's `MAX_VERIFIERS`'). WIRE-INTO-PROJECT.md:998 also names the hook as the constant's home, so it does not disagree with the page as the finder says. Whether a reader takes the sentence as an enforcement claim is a matter of reading. The finder graded this low and I could not establish a real misleading consequence, so it is refuted. | instance | - | - |
