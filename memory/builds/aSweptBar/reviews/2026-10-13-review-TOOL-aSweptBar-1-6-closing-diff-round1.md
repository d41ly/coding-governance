**Serves:** diff-review TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6

# Closing diff review, round 1: aSweptBar, the full bar's reds over local main swept unit by unit

Node `a` · 2026-10-13 · Tier-2 · on `branch/full-repo-bar-tests-2591de` · adversarial fan through the review harness: 5 finder lenses (gov-diff-reviewer), then 5 skeptic batches (gov-skeptic), then this synthesis (gov-synthesizer). The range is the cumulative diff landing on `main` for all six aSweptBar units. It re-arms stale suite fixtures, declares three engine self-tests whole, fixes the evidence and pre-push suites' standalone reds, applies the shipped-surface bans' remedies, converts the re-grown fork idioms, and re-measures the build's records, pins and ceilings.

**Reviewed range:** `53b258844a56b00b4489405aff7cd575e4a80b37...bc024b8b1202b79c8b4a08bfd1a9654a1ecd2dd5`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or a high. Nothing in the range ships a wrong result on a live path today. The three MEDIUM items are two test-coverage gaps and one instrument that fails loudly when run from its own folder. The F2 refusal-set derivation in `unattended-build.test.sh` misses the eight verbs dispatched through handlers not named `verb_*`, and its comment claims full coverage. The rewritten pre-push 25b arm dropped the only assertion of the hook's non-runner FULL refusal reason. Seven build-folder instruments source the Python resolver through a path that breaks when the script is invoked by bare filename. The four LOW items are a stale comment, a lost file pointer in gov's rendered spec template, an untested environment guard, and a closed spec whose S5 contradicts the code that closed it. Each fix is small and local, and each item carries a left-shift gate.

## Review shape

Intensity **full** · raw **13** · confirmed **11** · refuted **2** · unverified **0** (0 uncertain) · precision **0.85**.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| seams | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| verification | yes | 4 | 2 | 2 | 0 | 0 | 0.50 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

The 11 confirmed findings collapse to **7 items**. The merges are mine, made at write time, and each joins findings of one binding grade only. Ids 1, 4 and 8 are one defect seen by three lenses: the F2 refusal-set derivation keys on `verb_*` function names. Ids 3 and 6 are one defect: the bare-filename resolver path in seven build-folder instruments. Ids 2 and 13 are one defect: the lineage block's stale control header.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 3 MEDIUM · 4 LOW** (7 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 6 MEDIUM · 5 LOW** (11 findings).

Every id keeps its bracketed binding grade, and I re-grade none. The skeptic re-graded three findings, and I agree with each. Ids 3 and 6 rose from low to medium because a re-runnable instrument that exits 2 before measuring is a behavioural defect, not a cosmetic one. Id 9 fell from medium to low because the guard it covers is correct today and the untested path needs a caller to export `LBC`.

One caveat on grade. Ids 1, 4 and 8 carry the rubric's "will mislead the next change" wording, which describes HIGH, and id 1's skeptic used it. The binding grade is MEDIUM, and I keep it there. No current attended prompt issues any of the eight missed verbs, and the gap is a test arm's coverage rather than a shipped refusal.

The two refuted findings, ids 7 and 10, are listed with their reasons in the appendix. Id 7 claimed the 25b rewrite left hook lines 1754 and 1792 unguarded, and the skeptic showed arms that red when either breaks. Id 11 is the narrower state the refutation left standing. Id 10 claimed `run-held-wsl.sh --setup` lacks a test, and the skeptic showed the wiring is correct and `check-remote-literals.sh` already reds the regression the finding feared.

## Run integrity

- Lenses **5/5** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates.
- Fixes on confirmed findings: **9** judged sound, **2** judged UNSOUND (ids 2 and 5), **0** none proposed, **0** NOT JUDGED. An unjudged fix is the finder's proposal and nothing more.
- Severity on confirmed findings: **0** ungraded by the skeptic, **3** re-graded by the skeptic (ids 3, 6 and 9).
- Unverified findings: **0** answered UNCERTAIN, **0** with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

Every stage returned and every pipeline counter is zero, so no lens or batch is missing from this finding set. The run is still not a full sweep, for three reasons.

- **Intent:** neither `specs` nor `context` was supplied. The lenses had only the range's commit messages to judge intent by, so a defect visible only against a spec's acceptance criteria may be missed. Ids 11 and 12 were found from the code and the spec file in the tree, not from a supplied spec.
- **Checklist:** NONE swept, because it was absent. A zero count here is not evidence that the project's recurring bug classes are absent from this range.
- **By design:** none supplied, with no caller `byDesign` list and no block. The lenses could not discount intended behaviour, and the refutations had to establish that on their own.

The security lens returned zero findings. On a range of test fixtures, build records and comment-level remedies that is plausible, but with no checklist and no specs it is not proof of absence.

What this synthesis checked itself. It re-read `tools/run-gates/run-gates.evidence.test.sh:1464-1471` at HEAD and found the header still describing a `GATE_REUSE=1` control, which confirms L1's premise. It also checked `tools/hooks/format-guard.test.sh:17`, which holds `HERE=.; [[ $0 == */* ]] && HERE=${0%/*}`. The id-6 skeptic's correction is that this guard keys on `$0`, not `BASH_SOURCE[0]`. M2's fix applies the same guard to `BASH_SOURCE[0]`. The remaining findings rest on the skeptics' verification and were not re-executed here.

## MEDIUM

### M1. The F2 no-run-state refusal set misses every verb dispatched through a handler not named `verb_*` (ids 1, 4, 8)

`tools/workflows/unattended-build.test.sh:1037-1041` (the awk), and the comment above it.

The rewritten F2 arm derives its refusal set from functions named `verb_*` whose body calls `check_run_state "`. Over `tools/unattended/unattended.sh` at HEAD that yields 15 verbs: `--abort`, `--attest`, `--brief`, `--close`, `--dispatch`, `--landed`, `--park`, `--phase`, `--propose`, `--record-piece`, `--record-set`, `--rescope`, `--resume`, `--review` and `--status`. But 23 functions call `check_run_state`. The driver's `case "$VERB" in` dispatch at `unattended.sh:14307-14332` routes eight more verbs to handlers with other names, and each of those refuses without a run-state file.

- `--hold` → `run_hold` (6717)
- `--handoff` → `run_handoff` (6992)
- `--settle` → `run_settle` (7074)
- `--beat` → `write_claim_beat` (2473)
- `--audit` → `print_audit` (8320)
- `--register-task` → `write_task_register` (8439)
- `--liveness` → `print_liveness` (8675)
- `--authorization` → `print_authorization` (10606)

The new comment says the set covers "every verb whose body refuses through `check_run_state`" and that the arm "keeps holding when a seventh verb joins it". Both claims are false for any verb dispatched through a helper. If the attended child prompt in `unattended-unit.js` ever gained an instruction such as `--hold tB` or `--settle tB`, the child would halt the same way `--dispatch` and `--brief` did, and every F2 absence row would still pass. The base awk derived zero verbs, so both the narrowed coverage, now reported green, and the false comment come from this diff. No current attended prompt names any of the eight, so nothing ships wrong today.

**Fix (skeptic judged SOUND, all three findings):** derive the set from the dispatch table, not from function names. Parse each `--flag) handler ...` arm of the `case "$VERB" in` block. Collect every function whose body, from `handler() {` to the next top-level function, contains `check_run_state "`. Keep each flag whose handler is in that set. Then pin the result against `VERBS_SLUG` or a fixed count, and add a liveness assertion that `--hold`, `--settle` and `--audit` are in the derived set. That way a predicate that drops non-`verb_*` handlers reds.

**Left-shift gate:** a derivation-liveness assertion in the arm itself. Print the derived set and its near misses once over the real tree, then assert a known helper-dispatched verb such as `--hold` is present. More generally, any arm that derives its population by a name predicate should pin the population's size against an independent source, here the dispatch table.

### M2. Seven build-folder instruments cannot find the Python resolver when run by bare filename (ids 3, 6)

`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh:10` and `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh:25`, plus the same line in aPairedSlots-1 (`ab-instrument`, line 39) and aSparedSpawn-10, -11, -12 and -15.

This diff added `. "${BASH_SOURCE[0]%/*}/../../../../tools/lib/resolve-python.sh" || exit 2` to each instrument. Invoked as `bash <name>.sh` from its own build folder, `BASH_SOURCE[0]` holds no slash. `%/*` then leaves the filename unchanged, and the path becomes `<name>.sh/../../../../tools/lib/resolve-python.sh`. Both skeptics ran it from the build folder. The source fails with "Not a directory", and the instrument exits 2 before measuring anything, including under Git Bash on Windows. These records exist to be re-run (charter §8 keeps an instrument beside its result rows), and each usage line reads `bash <this> ...`, so the bare form is the documented one. Any path with a slash, such as `./<name>.sh` or a repo-root path, works. The failure is loud and the workaround is trivial, so the effect is contained.

**Fix (skeptic judged SOUND, both findings):** in each of the seven instruments, use the guard `tools/hooks/format-guard.test.sh:17` adopted in this diff, applied to `BASH_SOURCE[0]` rather than `$0`:

`_d=.; [[ ${BASH_SOURCE[0]} == */* ]] && _d=${BASH_SOURCE[0]%/*}; . "$_d/../../../../tools/lib/resolve-python.sh" || exit 2`

**Left-shift gate:** a lint over `memory/builds/*/build/*.sh` and kit shell that flags `${BASH_SOURCE[0]%/*}` or `${0%/*}` without a preceding `== */*` guard. A cheaper alternative is a smoke arm that runs each committed instrument's resolver line from its own directory by bare filename.

### M3. No arm now asserts the pre-push hook's non-runner FULL refusal (id 11)

`.githooks/pre-push.test.sh:479-483` (arm 25b), against the hook's force at `.githooks/pre-push:1753-1755`.

At base, 25b was the only test that matched the FULL force reason "the bar this push runs is not this kit's runner, so no runner stamp is a candidate". TOOL-aFrugalTurnstile-1 AC4 specifies that outcome, and the 25b header still cites it. The fix commit rewrote 25b to match only `*"scoped gate"*"bar green"*"from this git dir's gate-bar-green "*`, so it now covers a non-runner bar that has its own gate-bar-green two landings back. A grep over `.githooks`, `tools` and `skills` test files finds no other assertion of the force text. Lines 1554 and 2351/2353 are the run-record skip message, which is different text. The LIN AC12 other-bar arm (1168-1177) checks only that the reuse knobs are unset. The path is still reachable: when `bar_record=other` (`pre-push:1739`) and no gate-bar-green candidate exists, the hook keeps force set and pushes FULL with that reason. A dropped or reworded reason, or a FULL that falls back to another reason, would ship unseen. The fix brief said "No other arm moves", yet this arm's AC4 coverage was replaced rather than kept. The core AC4 guarantee, that no runner stamp scopes a non-runner bar, is still guarded, because the new 25b reds if a runner stamp is adopted. The loss is confined to the FULL-with-reason outcome.

**Fix (skeptic judged SOUND):** keep the new 25b. Add a 25c in the same fixture where the push has no gate-bar-green candidate to adopt. Either delete this git dir's gate-bar-green records before the push, or push a tree whose lineage holds only the runner stamp. Assert `*"FULL gate"*"is not this kit's runner"*`, and confirm 25c is red with the hook's `if [ "$bar_record" = other ]` block disabled.

**Left-shift gate:** when an arm is rewritten, check that each user-visible reason string the old arm matched is still matched by some arm. A diff-time check can grep the old arm's patterns against the post-change suite and flag any string that drops to zero matches.

## LOW

### L1. The lineage block's header still describes the retired `GATE_REUSE=1` control (ids 2, 13)

`tools/run-gates/run-gates.evidence.test.sh:1469-1471`.

The header reads "EVERY REFUSAL ARM CARRIES ITS CONTROL: a GATE_REUSE=1 run after the lineage run must reuse `pa` from the cache under the same key." This diff rewrote `check_lin_control` (now lines 1487-1496). It runs no bar and compares field 4 of `pa`'s row in the saved ledger `$tmp/ru.led` with `read_ru_key pa`, and its own comment says "Not the cache's env mode". The header now names a mechanism that no longer exists and contradicts the function comment 20 lines below. The next editor of these arms gets two opposing accounts of what the control proves. This is comment-only, and test behaviour is unchanged.

**Fix:** the skeptic judged id 13's fix SOUND and REJECTED id 2's fix. The corrected fix replaces id 2's proposal and is consistent with id 13's. Rewrite only lines 1469-1471 to say what the control does now. Each refusal arm's control, `check_lin_control`, checks that `pa`'s row in the saved ledger carries the input key (field 4) the lineage run computed, so a key that never matched cannot pass the refusal arm. Keep the line 1467-1468 sentence saying the opt-in control runs the cache's `env` mode, because AC6 still runs `GATE_REUSE=1`.

**Left-shift gate:** in a self-review of a diff that rewrites a function, grep the enclosing block's header for the old function's mechanism words. Here those are `GATE_REUSE=1` and `reuse \`pa\``.

### L2. Gov's rendered spec template no longer names its review protocol file (id 5)

`tools/memory-tree/SPEC-TEMPLATE.template.md:384`, rendered into `memory/TEMPLATE-SPEC.md:384`.

Commit 96b17341b turned the literal into `{{REVIEW_PROTOCOL}}`. `tools/lib/render-doc.sh:191/198` resolves that token only through `rendered_at("review-harness", ...)`, which reads `.governance/install.json`. Gov has no install receipt, so the rendered gov copy now reads "the review protocol of this repo". At base the same line read "the review protocol (`REVIEW-PROTOCOL.md`, review-harness kit)", and gov keeps the protocol at `memory/guides/REVIEW-PROTOCOL.md`. Gov's `BUILD-METHOD.md:130` already rendered this way at base. The change is wording only, but the file pointer is gone from the template gov's spec writers copy.

**Fix (skeptic REJECTED the finder's fix; this is the corrected fix):** make the `gov_source == "."` resolution of `{{REVIEW_PROTOCOL}}` in all three byte-identical copies of the `render_doc` block: `tools/lib/render-doc.sh`, `tools/memory-tree/adopt-memory-tree.sh` and `tools/memory-tree/kit-dogfood-parity.test.sh`. Answer with the tracked path of `REVIEW-PROTOCOL.md` under the memory root, the way `{{SPEC_TOKEN_CHECKER}}` already does. Then re-render `memory/TEMPLATE-SPEC.md`. The finder's proposal named only two of the three copies, which would break their byte parity.

**Left-shift gate:** a render-doc arm that renders each template in source mode (`gov_source == "."`) and fails when a token falls back to its generic phrase while the source repo has the named file. Here that file is `memory/guides/REVIEW-PROTOCOL.md`.

### L3. The new `getval` empty-first guard has no arm that fails without it (id 9)

`skills/session-kickoff/manifest-check.sh:366`.

The diff converted `getval` to `printf -v` and added `printf -v "$2" '%s' ''` so an exported `LBC` cannot survive an absent key. That reason is stated in the comment at line 361. Before, `LBC=$(getval …)` always assigned `LBC`. Now `LBC` has no initialiser: `LA`, `WATCH_RAW` and `VP_RAW` are set to "" at 1355, but `LBC` is not. So without line 366, an `LBC` exported by a caller would hide a missing `last-body-change` key. Check 2's refusal at 1365 would never fire, and check 9 would measure from a foreign baseline. The finder's probe confirmed the mutant: with line 366 removed, `LBC` reads `[deadbeef]`. A grep for `LBC` in `manifest-check.test.sh` finds nothing. The `run` helper (line 24) inherits the caller's environment, and arm C2 (577) runs with `LBC` unset, so it passes against the mutant. Behaviour is correct today. The skeptic re-graded this from medium to low because the path needs an exported `LBC`.

**Fix (skeptic judged SOUND):** extend arm C2 to also run the checker under `env LBC=<a valid 40-hex sha of the fixture>` over the same key-dropped manifest. Assert the same "lacks a last-body-change value" refusal, and confirm it goes red with line 366 removed.

**Left-shift gate:** every guard added against environment leakage gets a paired arm that pre-sets the leaking variable. A self-review rule can enforce this: a new line whose comment cites "exported" or "survive" needs a test that exports the named variable.

### L4. The closed spec's S5 says the plain earning bar stamps nothing, and the code says it does (id 12)

`memory/builds/aSweptBar/spec/2026-10-13-spec-TOOL-aSweptBar-3.md:112`.

S5 reads: "A plain bar between lines 1510 and 1511 earns it on the fixed, clean tree and stamps nothing, because only a full bar stamps." The code bc024b8b1 added at `run-gates.evidence.test.sh:1519-1521` says the opposite: "A plain bar on a clean tree stamps a full green too (the AC8 control above), removed before the opt-in run." It then runs `ru_run >/dev/null; rm -f "$RU_GD/gate-full-green"`. The commit message confirms this stamp caused the AC6 red that reopened the unit. bc024b8b1 touched the spec (2 lines) but left S5 unchanged. The status line reads CLOSED rev-2, and the revision log has no row for the correction. Anyone who later reasons from this spec about which bars stamp `gate-full-green` will be misled. Code behaviour is not affected.

**Fix (skeptic judged SOUND):** add a rev-3 revision-log row. Restate S5 to say a plain bar on a clean tree also stamps a full green, so the arm removes that stamp before the opt-in run. Cite bc024b8b1's probe: red with the stamp kept, green with it removed.

**Left-shift gate:** at close, when a fix commit's message names a cause the spec states the opposite of, the closer re-reads the spec's design steps against the fix diff. A cheap form is a close-time prompt: does any spec step assert behaviour the fix commit had to undo?

review-shape kind=diff-review round=1 intensity=full at=synth raw=13 confirmed=11 refuted=2 unverified=0 blocker=0 high=0 medium=6 low=5 agents=11 out-tokens=145955

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/workflows/unattended-build.test.sh:1037 | medium | medium | confirmed | I ran the head awk (unattended-build.test.sh:1037-1041) against tools/unattended/unattended.sh at bc024b8b1. It derives 15 verbs: abort, attest, brief, close, dispatch, landed, park, phase, propose, record-piece, record-set, rescope, resume, review and status. Mapping every `check_run_state "` call to the function it sits in gives 23 functions. Eight of them are not named verb_*: run_hold, run_handoff, run_settle, write_claim_beat, print_audit, write_task_register, print_liveness and print_authorization. The `case "$VERB"` dispatch at unattended.sh:14308-14331 routes --hold, --handoff, --settle, --beat, --audit, --register-task, --liveness and --authorization to exactly those handlers. So all eight refuse without a run-state file, and the derived set leaves them out. This diff wrote both the new predicate and the new comment ('every verb whose body refuses through `check_run_state`'). The base awk derived zero verbs from the base driver, so the narrowed coverage, now reported green, and the false comment both come from this diff. Today's attended prompt in unattended-unit.js issues none of the eight, so nothing ships wrong now. The effect is a coverage gap that also misleads the next change, so I grade it medium. | sound | - |
| 2 | correctness | tools/run-gates/run-gates.evidence.test.sh:1467 | low | low | confirmed | run-gates.evidence.test.sh:1469-1471 still says 'EVERY REFUSAL ARM CARRIES ITS CONTROL: a GATE_REUSE=1 run after the lineage run must reuse `pa` from the cache under the same key'. This diff replaced check_lin_control (lines 1487-1493). The new version runs nothing: it compares field 4 of pa's row in $tmp/ru.led with read_ru_key pa, and its own comment says the env mode's key can never equal a full bar's key. The header now describes a control that no longer exists. It is a comment only, with no effect on behaviour. | unsound | - |
| 3 | correctness | memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh:10 | low | medium | confirmed | This diff adds `. "${BASH_SOURCE[0]%/*}/../../../../tools/lib/resolve-python.sh" \|\| exit 2` to the seven named instruments (aBriskPreflight-7 line 10, aPairedSlots-1 line 39, and aSparedSpawn-10, -11, -15, -2 and -12). The base copy of ab-prep.sh had no such line. I ran the probe from memory/builds/aBriskPreflight/build with the bare file name. `${s%/*}` left the file name unchanged, `[ -f ]` said notfound, and sourcing failed with 'Not a directory', even under Git Bash on this Windows host. Invoked as `bash <name>.sh` from its own directory, the instrument exits 2 before measuring anything. Any path containing a slash works. It is a real behavioural defect, but contained and loud. | sound | - |
| 4 | seams | tools/workflows/unattended-build.test.sh:1037 | medium | medium | confirmed | I ran the head awk (unattended-build.test.sh:1037-1041) over tools/unattended/unattended.sh. It prints exactly the 15 verbs the finder listed. The dispatch `case "$VERB" in` at unattended.sh:14307-14332 sends --audit, --register-task, --liveness, --authorization, --hold, --handoff, --settle and --beat to print_audit, write_task_register, print_liveness, print_authorization, run_hold, run_handoff, run_settle and write_claim_beat. Each of those calls `check_run_state "$rel"` (lines 8320, 8439, 8675, 10606, 6717, 6992, 7074, 2473). So none of the eight gets an F2 absence arm. That contradicts the new comment, which says the set is every verb that refuses through check_run_state. The derivation is this diff's rewrite: the base awk matched `fail 4N "no run-state file` and derived nothing at all. No current attended prompt names any of the eight, so the effect is a coverage gap with no live instance. | sound | - |
| 5 | seams | tools/memory-tree/SPEC-TEMPLATE.template.md:384 | low | low | confirmed | At base, memory/TEMPLATE-SPEC.md:384 read 'the review protocol (`REVIEW-PROTOCOL.md`, review-harness kit)'. At head, the template has `{{REVIEW_PROTOCOL}}` (commit 96b17341b), and render-doc.sh:191/198 resolves that token only through rendered_at() from .governance/install.json. Gov has no install.json, so the rendered gov copy now reads 'the review protocol of this repo'. Gov's BUILD-METHOD.md:130 already rendered this way at base. The change is wording only, but the file pointer did disappear from this doc. | unsound | - |
| 6 | seams | memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh:25 | low | medium | confirmed | This diff added the line `. "${BASH_SOURCE[0]%/*}/../../../../tools/lib/resolve-python.sh" \|\| exit 2` (width-ab.sh:25). I ran `bash 2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh` from memory/builds/aSparedSpawn/build. It printed 'line 25: 2026-10-11-...-width-ab.sh/../../../../tools/lib/resolve-python.sh: Not a directory' and the record exits 2 before doing any work. The `./` form resolves correctly from the same folder. Grep confirms the same line in the six other records named. The failure is loud and the workaround is trivial, so the effect is contained. One correction: format-guard.test.sh does not contain the cited idiom, though the idiom works as written. | sound | - |
| 7 | verification | .githooks/pre-push.test.sh:481 | medium | - | refuted | Both hook lines the finding names are still covered by arms that fail when they break. Line 1754 (`force=` for bar_record=other): the new 25b puts the runner stamp 1 landing back and the bar record 2 back. If that force is dropped, nearest-wins keeps the runner stamp (_sel_d=lag=1, and the record's 2 is not less), so the line names gate-full-green and 25b's `from this git dir's gate-bar-green` pattern goes red. Line 1792, the finder's own mutant `force=$_bar_why`: the BG wrapper-bar fixtures (wrap-bar.sh, classed `other` at 1739) make their first push with no runner stamp and no record. Under the mutant, _sel_d is empty and _bar_why is empty, so force becomes empty and the decision turns scoped (RUNLOG_DECISION=scoped). write_bar_green then writes gate-bar-green.scoped instead of a kind-full gate-bar-green. 'BG slot AC1' (asserts gate-bar-green kind full sha c1) and BG AC17 (expects `full bar green M from this git dir's gate-bar-green`) would both go red. So the claim that every suite stays green under that mutant does not hold. Only the narrower state (runner stamp present, no record) lacks a decision-line assertion, and the finding shows no mutant that breaks only that state. | sound | - |
| 8 | verification | tools/workflows/unattended-build.test.sh:1040 | medium | medium | confirmed | I ran the new awk over tools/unattended/unattended.sh. It yields 15 verbs (--abort … --status) and none of --hold, --handoff or --settle. The dispatch at unattended.sh:14319-14321 sends those to run_hold, run_handoff and run_settle. Each calls check_run_state (6717 'run to hold', 6992, 7074 'run to settle'), and check_run_state (798) does `fail 10 "no run-state file…"`. The diff rewrote both the predicate and its comment ("every verb whose body refuses through check_run_state"). unattended.sh itself is unchanged in the range, and the base predicate derived 0 verbs, so this incomplete set is new in this diff. There is no live miss today: unattended-unit.js names none of these verbs in instruction form. The effect is contained to a test arm whose comment overstates its coverage. | sound | - |
| 9 | verification | skills/session-kickoff/manifest-check.sh:366 | medium | low | confirmed | The diff converted getval to `printf -v` and added `printf -v "$2" '%s' ''` at manifest-check.sh:366. Before, `LBC=$(getval …)` always assigned LBC. Now LBC has no initialiser (LA, WATCH_RAW and VP_RAW are set to "" at 1355, LBC is not), so without line 366 an exported LBC would survive an absent key and suppress the check-2 refusal at 1365. A grep for LBC in manifest-check.test.sh finds nothing. The `run` helper (line 24) inherits the caller's environment, and arm C2 (577) runs with LBC unset, so it passes with the line removed. The guard is real but has no arm that fails without it. The path needs an exported LBC and behaviour is correct today, so the consequence is a contained coverage gap. | sound | - |
| 10 | verification | tools/run-gates/run-held-wsl.sh:212 | medium | - | refuted | The coverage claim is true but there is no defect, and part of the stated consequence is false. I checked: no *.test.sh or selftest invokes run-held-wsl.sh. held_halves.py only names it as SHIM in partition argv. resolve-python.test.sh:178 (row remote_ladder_sh) checks byte parity only. However, the --setup caller at run-held-wsl.sh:212-215 is correct as written. resolve_remote_sh's rc 1 goes to print_refusal "$RR_WHY". The ladder's documented rc 0 with an empty RR_REMOTE goes to the no-remote refusal. get-url reads "$RR_REMOTE". The finding says 'reading origin again stays green', which is false. tools/check-remote-literals.sh shape 5 ('a remedy — ... get-url ... then the name') reds a `git remote get-url origin` in kit code, and that gate is the one that flagged this exact line (brief TOOL-aSweptBar-1 item 4). Spec TOOL-aSweptBar-4 AC5 also greps that 'get-url origin' counts 0. What is left is that the two adjacent refusal messages could be swapped without a test noticing. Either way the outcome is an exit-2 refusal in a hand-run, once-per-node operator mode. That untested state is the same as the base, where the hardcoded-origin line was also unexercised. A missing test over correct two-line wiring, with no wrong result reachable, is not a bug. | sound | - |
| 11 | intent | .githooks/pre-push.test.sh:481 | medium | medium | confirmed | Verified. At base, pre-push.test.sh:478 was the only test that matched "is not this kit's runner" against the FULL force reason at .githooks/pre-push:1754. At HEAD, 25b (line 479-483) matches only *"scoped gate"*"bar green"*"from this git dir's gate-bar-green "*. A git grep over .githooks, tools and skills finds no other assertion of that force text. Lines 1554 and 2351/2353 are the run-record skip message, which is different text. The LIN AC12 other-bar arm (1168-1177) checks only that the reuse knobs are unset. The path is still reachable: when bar_record=other (pre-push:1739) and no gate-bar-green candidate exists, the hook keeps force set at 1753-1755 and pushes FULL with that reason. Nothing now pins that outcome or its reason. The new 25b does still red if a runner stamp is adopted, because the stamp sits nearer than the bar record. So AC4's core 'no runner stamp scopes a non-runner bar' remains guarded, and the loss is contained to the FULL-with-reason outcome. | sound | - |
| 12 | intent | memory/builds/aSweptBar/spec/2026-10-13-spec-TOOL-aSweptBar-3.md:112 | low | low | confirmed | At HEAD, spec line 112 reads 'A plain bar between lines 1510 and 1511 earns it on the fixed, clean tree and stamps nothing, because only a full bar stamps.' The code bc024b8b1 added at run-gates.evidence.test.sh:1519-1521 says the opposite: 'A plain bar on a clean tree stamps a full green too (the AC8 control above), removed before the opt-in run.' The code then runs `ru_run >/dev/null; rm -f "$RU_GD/gate-full-green"`. The commit message confirms that this stamp caused the AC6 red. bc024b8b1 touched the spec (2 lines) but left S5 unchanged. Its status line reads CLOSED rev-2, and the revision log has no row for this correction. The record is wrong but code behaviour is not affected. | sound | - |
| 13 | intent | tools/run-gates/run-gates.evidence.test.sh:1469 | low | low | confirmed | Confirmed. At the base, check_lin_control (base line 1484) copied ru.led back and ran `ru_run GATE_REUSE=1`, which is the mechanism the header at base 1466-1468 describes. The diff rewrote it (now lines 1487-1496) so that it runs no bar and only compares pa's ledger field 4 against `read_ru_key pa`. Its new comment says 'Not the cache's env mode'. The header at lines 1469-1471 was left unchanged and still says the control is 'a GATE_REUSE=1 run after the lineage run must reuse `pa`'. The diff therefore made the header stale, and it now contradicts the function comment 20 lines below. It is comment-only and test behaviour is unchanged, so the grade is low. | sound | - |
