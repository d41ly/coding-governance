**Serves:** diff-review TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64

# Closing diff review, round 1: the dPlacedRequest Entry build

Node `d` · 2026-11-20 · Tier-2 · on `branch/unattended-dplacedrequest-42a7be`. This was an adversarial fan through `tier2-review.js`: 5 finder lenses, then 5 skeptic batches, then this synthesis. The range is the whole of dPlacedRequest, the Entry build of the dClosedLoop chain. It holds 63 Tier-2 units (TOOL-dPlacedRequest-1 to -64; there is no -22) that close 18 owned gaps across concurrency, orientation and flow. It is 313 commits over 318 files, +40179/−6221. (PINNED)

**Reviewed range:** `9e21ac760dc0a43d6ed007396922722ccee98d57...95c3103ad4d50a921228af623d34be493f807ff7`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No blocker was confirmed. Two HIGH items and two MEDIUM items stand open.

The first HIGH is in `scratch-guard`'s kickoff-checker resolution. On a narrow path it runs a tracked `manifest-check.sh` from the commit or edit target's repository inside PreToolUse. That is code execution across a trust boundary, and the base hook had no such path.

The second HIGH is a half-applied edit in `check_claim_writable`. It dropped the `lease:foreign-stale` row. As a result, `--lease take-over` can no longer take a dead holder's lease, and the stale hint can never print.

Both MEDIUMs are missing regression checks. Most of the card-store fixture's plants are on no gate. The S20 exact-match node resolver has no arm that tells it apart from the substring rule.

Fold all four before the build closes.

## Review shape

Intensity full, raw 5, confirmed 4, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.80.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 0 | 1 | 0 | 0 | 0 | 0.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |

- Adjudicated tally by item: 0 BLOCKER, 2 HIGH (H1, H2), 2 MEDIUM (M1, M2), 0 LOW, which is 4 items.
- Adjudicated tally by raw confirmed finding: 0 BLOCKER, 2 HIGH (ids 1, 3), 2 MEDIUM (ids 4, 5), 0 LOW, which is 4 findings.
- No findings were merged. Each item holds one confirmed id.
- I re-grade nothing. Id 4 takes its binding MEDIUM, which the skeptic set from the finder's HIGH.
- No twin was flagged. The one refuted finding (id 2, request consent hashed over the submitted bytes and not the stored copy) is a different defect from every confirmed one, and no same-address pair was shown.
- Intent input: 1 spec document was supplied as `specs`, beside the range's commit messages.
- Checklist: 94 items, acquired by the harness from `--for-diff 9e21ac760dc0a43d6ed007396922722ccee98d57..95c3103ad4d50a921228af623d34be493f807ff7`. Each item was assigned to exactly one of 5 lenses: security 19, correctness 19, seams 19, verification 19, intent 18.
- By design: the caller's byDesign, plus 2 invariants from the checklist's by-design block.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified.
- 0 orphaned duplicate refutations were demoted to unverified.
- 0 duplicate refutations were counted as merged confirmations.
- 0 spurious verdicts were discarded.
- 0 duplicates.
- Fixes on confirmed findings: 3 judged sound, 0 judged UNSOUND, 1 judged INSTANCE-ONLY (it cures the cited instance and leaves its class standing), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (id 4, HIGH to MEDIUM).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Shown to synthesis: 1 refuted finding and 0 same-address pairs.
- Dispositions: unclassed is `refuse`, 94 class slugs were handed, and 202 leg names were read from `tools/gate-legs.json`.

Every count above is zero where it should be, so the run is complete.

## HIGH

### H1 — scratch-guard runs the target repository's `manifest-check.sh` inside PreToolUse (id 1)

- **Where:** `tools/hooks/scratch-guard.js@e21b4d65:711`. The callers are `readCard` (:759-787), `checkOriented` (:891-907) and the write gate (:1983).
- **What is wrong:** `resolveKickoffChecker` has three rungs:
  1. the kit resolver, run from `__dirname`;
  2. the hook's own toplevel;
  3. the toplevel of `cwd`.

  `cwd` is the parent of the common dir of the commit target, or of the edit target. The third rung runs `git ls-files -- manifest-check.sh '*/manifest-check.sh'` there. If exactly one file matches, `readCard` executes it with `spawnSync(bash, [engine, '--card', '--path', ...])`. This happens inside PreToolUse, before any allow or deny. The base hook only read `<common>/orientation/<sid>.md` and ran nothing. The `[__dirname, cwd]` walk came in with 66b4cd4f4 (TOOL-dPlacedRequest-2).
- **Consequence:** Rungs 1 and 2 both miss when the hook's repository has no session-kickoff receipt row and tracks zero, or two or more, copies of `manifest-check.sh`. They also miss when the hook sits outside any git repository. That is the normal shape in an adopter: scratch-guard is copy-installed in the repository, and the kickoff skill is junction-installed per machine, so it is not tracked. In that case the following runs a tracked file from an untrusted clone with the agent's privileges, even if the commit itself would be denied:
  - a `git -C <clone> commit ...`;
  - an Edit under a routed tree in another repository.

  In this repository rung 1 throws, and only rung 2 (the single tracked copy) stops the walk. The path is narrow, but the result is code execution across a trust boundary.
- **Fix (judged SOUND by the skeptic):**
  - Resolve the checker only from the hook's own install: rung 1 (the receipt or probes from `__dirname`) and rung 2 (the hook's own toplevel).
  - Remove `cwd` from the `[__dirname, cwd]` list, so a target repository's tracked file is never executed.
  - Where neither rung answers, return null so the card reads as absent ("no kickoff checker resolves").
- **Left-shift gate:** add a `scratch-guard self-test` arm with three fixtures:
  - a scratch clone that tracks a `manifest-check.sh` which writes a marker file;
  - a hook directory whose repository tracks two copies;
  - a `git -C <clone> commit` fed to the hook.

  The marker must appear against the pre-fix hook and must not appear after the fix. Record the class, a hook executing code it resolved from the target tree, in the bug-class checklist.

### H2 — `check_claim_writable` lost its `lease:foreign-stale` row, so stale leases cannot be taken over (id 3)

- **Where:** `tools/unattended/unattended.sh@0e8038fd:2926`. That is the lease column of `check_claim_writable`, lines 2908-2926. The hint is read at :4235.
- **What is wrong:** Commit b7e369eeb (TOOL-dPlacedRequest-16) put the new `lease:foreign-released` row in place of the `lease:foreign-stale` row instead of beside it. The stale row came in with 71f85d59f, inside this range. It set `CW_ACT=take-announced` for `take-over` and `CW_HINT=take-over` for `acquire`. Now a foreign stale lease falls through to the catch-all `lease:*) CW_CAUSE=live-holder; return 1` for every act. `CW_HINT` is now only reset (:2412, :2809) and read (:4235). Its suffix, `stale, so --lease take-over takes it`, can never print.
- **Consequence:** This path is reached whenever a lease holder dies, because its lease is then classified `foreign-stale`.
  - `--lease acquire` and `--lease take-over` both print `lease refused — live-holder` and exit 1. A stale build, unit, run or request lease therefore cannot be recovered through the documented verbs.
  - The refusal hides that the lease is stale.
  - In `run_entry_claim`, a patch or repeat whose build lease is stale is routed as a live holder. It stamps `wait-since:`, exits 4 until `flow.wait-ceiling`, then raises an owner item instead of being told to take over.
  - This contradicts `tools/unattended/STOPS.template.md:364` and the function's own header (:2784-2785).
  - The run columns' stale rows (:2940, :2943) still stand, so only the `--lease` verb path is broken.
  - Nothing is written wrongly and no data is lost.
- **Fix (judged SOUND by the skeptic):** put this row back beside the `lease:foreign-released` row, above `lease:*`:

  `lease:foreign-stale) case "$la" in take-over) CW_ACT=take-announced ;; acquire) CW_CAUSE=live-holder; CW_HINT=take-over; return 1 ;; *) CW_CAUSE=live-holder; return 1 ;; esac ;;`
- **Left-shift gate:** add two checks to the `unattended-build self-test`.
  - **Probe arm:** in a bare-remote fixture, plant a lease whose renewing beat was first seen longer ago than `leases.expiry-hours`. Assert that `--lease acquire build <slug>` from another session exits 1 with `stale, so --lease take-over takes it`. Assert that `--lease take-over build <slug>` exits 0, takes at epoch +1 and announces the take. The table at `tools/unattended/unattended.test.sh@f814cdb0:18269` checks only a refusal, and acquire gives one anyway, so it cannot see this loss.
  - **Static check:** every `CW_*` name the verbs read has an assignment in `check_claim_writable`.

## MEDIUM

### M1 — the suite runs 8 of card-store.fixture.sh's plants, and the rest are on no gate (id 4)

- **Where:** `skills/session-kickoff/manifest-check.test.sh@f227fdc7:2383`. The floor comment is at :2446.
- **What is wrong:** The suite's plant loop is typed by hand with 8 cases: publish, publish-off, publish-unwritten, publish-hung, follow-rerender, lookup, terminal-route and close-follow-twice. The fixture is new in this diff. Its `PLANTS` list (`skills/session-kickoff/card-store.fixture.sh@9d4246db:24-27`) holds 30 cases. The finder counted 33. Either way, 22 or more are never run by any gate, suite or runner. The only references to card-store under tools/, skills/ and .github/ are this suite and the deployer-registry exemption. The plants left out include:
  - publish-late (34/43 AC17, the remote-ref `unknown` outcome);
  - lookup-hung (AC11, the `CARD_FETCH_BOUND` lookup bound);
  - lookup-upstream (AC9) and lookup-offline;
  - replay (AC12, no FETCH_HEAD write);
  - store-*, follow-per-step/fixed and snapshot-*;
  - context-* and partial-* (including the RESUME.md restart act).
- **Consequence:** A later regression in the bounded lookup, the `unknown` publish outcome, the upstream lookup, replay's FETCH_HEAD, or the store/follow/snapshot/resume policies would land green.
  - The acceptance ledgers of units 2, 34 and 43 cite these plants as evidence, but the plants ran once by hand. The 43 ledger admits this for publish-late.
  - The floor comment still says "five" plants.
  - Nothing wrong ships today, so the grade is MEDIUM. The skeptic re-graded it from the finder's HIGH, and that grade is binding.
- **Fix (judged SOUND by the skeptic):**
  - Have the suite read its plant list from `card-store.fixture.sh --list` instead of a hand-typed list, so a new plant joins the gate automatically.
  - Add a liveness check that the number of plants run equals the number `--list` prints.
  - Raise `FLOOR_ASSERTIONS` by the plants added, and re-price the leg's budget.
  - Observe one newly gated plant go red, for example lookup-hung against the engine from before unit 34.
- **Left-shift gate:** the `manifest-check self-test` leg carries the `--list` liveness check. A fixture whose plant list the suite does not consume in full then reds the bar.

### M2 — no arm tells the S20 exact-match node resolver from the substring rule it replaced (id 5)

- **Where:** `tools/run-gates/run-selftests.sh@79545478:450`. The registry fixture is at `tools/run-gates/run-selftests.test.sh@382f88e6:395-396`.
- **What is wrong:** TOOL-dPlacedRequest-43 S20 changed `resolve_node_tag` from `case "$user" in *"$tok"*` to exact equality. `run-selftests.test.sh` is not in the diff, and no existing arm can tell the two rules apart:
  - Its only registry fixture writes a row whose token is exactly `${USERNAME:-$USER}`, which both rules match.
  - The no-row arm (:1319) deletes that row, which both rules refuse.
  - The arm at :1569 exercises only the `GOV_NODE` path.

  Spec 43's AC20 probe uses fleet users, none of which is a strict substring that pulls in an earlier row. So AC20 passes under the substring rule as well.
- **Consequence:** If the resolver reverted to the substring rule, every arm would stay green. A pooled run would then key its evidence on the wrong node tag again, which is the S20 defect itself. The changed rule has no check that can fail.
- **Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** add a fixture arm for each resolver that S20 changed.
  - In `run-selftests.test.sh`, put a strict-substring row (for example the user's first character, tag `s`) above the exact row `t`. Assert that the pooled evidence is keyed on `t`.
  - In `manifest-check.test.sh`, run `--card` with `USERNAME` set to the registry row's user in upper case. Assert that the row's tag is derived, not `UNKNOWN`.
  - Observe each arm go red against the line before the change: the substring `case`, and the case-sensitive `mu==user`.
  - Raise each suite's floor.

  The finder proposed only the `run-selftests.test.sh` arm, red against the pre-change `case` line, with that suite's floor raised by one. That cures the cited instance alone and leaves the `manifest-check.sh` resolver unguarded.
- **Left-shift gate:** the arms belong in the `run-selftests self-test` and `manifest-check self-test` legs. As a class rule: a change to a matching predicate owes an arm whose input the old predicate and the new one answer differently.

review-shape kind=diff-review round=1 intensity=full at=synth raw=5 confirmed=4 refuted=1 merged=0 unverified=0 blocker=0 high=2 medium=2 low=0 agents=11 out-tokens=90118 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=2 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/hooks/scratch-guard.js@e21b4d65:711 | high | high | confirmed | Confirmed by reading tools/hooks/scratch-guard.js@e21b4d65:704-722 and 759-787. resolveKickoffChecker tries the kit resolver from __dirname first, then walks `[__dirname, cwd]`. The cwd step runs `git ls-files -- manifest-check.sh '*/manifest-check.sh'` in that tree's toplevel and returns the single tracked hit. readCard then runs it as `spawnSync(bash, [engine, '--card','--path',...])`. In checkOriented (:891-907), cwd is the parent of the common dir of the commit target (`git -C <clone> commit` resolves start -> resolveToplevel -> resolveCommonDir), and this runs inside PreToolUse before any allow or deny. The write-gate caller at :1983 does the same with the edit target's common dir. The base hook ran nothing: `git show 9e21ac76:tools/hooks/scratch-guard.js` has no checker resolution, and the `[__dirname, cwd]` loop came in with 66b4cd4f4 (TOOL-dPlacedRequest-2), so this diff introduced it. In gov, rung 2 answers (the tree tracks exactly one copy, skills/session-kickoff/manifest-check.sh), so here the third rung is reached only if a second tracked copy appears. In an adopter, scratch-guard is copy-installed in-repo at <prefix>/hooks, and the kickoff skill is junction-installed per machine and not tracked. There rungs 1 and 2 can both miss, and any cross-repo commit or edit target that tracks exactly one manifest-check.sh has that file executed. The sibling resolvers (handoff.py resolve_card_path, unattended.sh resolve_kickoff_checker) run in the repo the tool itself operates on, not in an arbitrary hook target, so they are not the same exposure. The consequence is code execution across a trust boundary on a narrow but reachable path, which is high. | sound | - | new:hook-executes-code-resolved-from-its-target |
| 2 | correctness | tools/unattended/unattended.sh@0e8038fd:4692:4692 | medium | - | refuted | The code is as the finder says. At tools/unattended/unattended.sh@0e8038fd:4678-4694 the copy is skipped when a stored copy that folds equal already exists. The `.typed` blob is `git hash-object --no-filters` of the submitted file `$f`, and check_request_consent at 4971-4973 hashes the stored copy. A CRLF twin from a second session therefore records a line that never matches. This outcome is specified, though. Spec memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md S14 (lines 112-119) says the blob is of the submitted bytes, and that 'a second session submitting a CRLF twin of stored words keeps the first copy and reads no consent, as a re-wrapped twin already does.' The comment at 4689-4690 implements that rule. The security model binds consent to the bytes a session typed. Reading no consent for bytes the stored copy does not hold is the designed fail-closed result, not a mis-binding. The 'recorded' line reports the remote record, which was written correctly. So this is by design. At most it is a UX gap in the success line, outside the claim as stated. | unsound | - | - |
| 3 | seams | tools/unattended/unattended.sh@0e8038fd:2926 | high | high | confirmed | Confirmed. The defect was introduced inside this diff, not before it. At 95c3103ad, check_claim_writable's lease column (tools/unattended/unattended.sh@0e8038fd:2908-2926) has rows for none, offered, mine, same, foreign-released, foreign-tombstone and foreign-terminal, and then the catch-all `lease:*) CW_CAUSE=live-holder; return 1`. There is no `lease:foreign-stale` row. `git log -S` shows that row was added in 71f85d59f and removed in b7e369eeb, both inside the range. `git show b7e369eeb` shows the stale row (the one that set `CW_ACT=take-announced` for take-over and `CW_HINT=take-over` for acquire) swapped out for the foreign-released row. The base 9e21ac760 has no CW_HINT at all, so this is not pre-existing. Today CW_HINT is only reset (lines 2412 and 2809) and read (line 4235), so the hint text `stale, so --lease take-over takes it` can never print. In lease mode a dead holder's lease is classified `foreign-$c_verdict`, which is `foreign-stale` (line ~2847). That falls through to `lease:*`, so both `--lease acquire` and `--lease take-over` print `lease refused — live-holder` and exit 1. This contradicts tools/unattended/STOPS.template.md:364 ('refused live-holder, naming take-over \| take, announced, epoch +1'). It also contradicts the function's own header comment at lines 2784-2785. The run columns' stale rows at lines 2940 and 2943 still exist, so only the --lease verb path is broken. The test table at tools/unattended/unattended.test.sh@f814cdb0:18269 checks only a lease-mode refusal, which acquire would give anyway, so it does not catch the take-over loss. Graded high: the path is reachable whenever a lease holder dies, and a stale lease cannot be recovered through the documented verb, but nothing is written wrongly and no data is lost. | sound | - | class:amendment-leaves-its-other-half-standing |
| 4 | verification | skills/session-kickoff/manifest-check.test.sh@f227fdc7:2383 | high | medium | confirmed | The finding holds. At skills/session-kickoff/manifest-check.test.sh@f227fdc7:2383 the plant loop is hand-typed with 8 cases: publish, publish-off, publish-unwritten, publish-hung, follow-rerender, lookup, terminal-route and close-follow-twice. The PLANTS variable in skills/session-kickoff/card-store.fixture.sh@9d4246db:24-27 lists 30 cases, not 33, so 22 are never run by the suite. Among them are publish-late, lookup-hung, lookup-upstream, lookup-offline, replay, store-*, follow-per-step/fixed, snapshot-*, context-* and partial-*. A grep of tools/, skills/ and .github/ finds card-store only in this suite and in tools/govkit/registry.toml, so no other gate runs those plants. The fixture is new in this diff (it is absent at the base). Spec 34 §7 line 503 and spec 43 §7 line 431 name card-store.fixture.sh itself as the 'New arm' home for AC7/9/11/12/39 and AC17, and the fixture is on no leg. The 43 ledger (lines 66-67) admits that publish-late is not in the suite's list. The floor comment at line 2446 still says 'five' plants while the loop runs 8. I grade it medium, not high: nothing wrong ships today. The effect is that a later regression in the bounded lookup, the remote-ref 'unknown' outcome, replay's FETCH_HEAD or the store/follow/resume policies would land green. That is a contained coverage gap, and no current check certifies something false. | sound | - | class:observed-by-claim-no-arm-discharges |
| 5 | verification | tools/run-gates/run-selftests.sh@79545478:450 | medium | medium | confirmed | The finding holds. In the diff, tools/run-gates/run-selftests.sh@79545478:450 changes the match from `case "$user" in *"$tok"*` to `[ "$user" != "$tok" ] \|\| ...`, and run-selftests.test.sh is not in the diff (the --stat for tools/run-gates/ lists only post-merge.sh, run-selftests.sh and selftest-budgets.txt). The only registry fixture, at tools/run-gates/run-selftests.test.sh@382f88e6:395-396, writes one row whose token is exactly `${USERNAME:-$USER}`, and both rules match that. The arm at 1319 deletes the row, and both rules refuse then. The arm at 1569 adds row `u` with user someone-else and exercises only the GOV_NODE path. No arm plants a token that is a strict substring of the user. The spec's own check doesn't cover it either. AC20 in spec 43 is a one-time probe that sets USERNAME to each fleet.toml user, and none of those users (daily-agent, agent5, agent-0, d41ly) is a strict substring that would pull in an earlier row. So the substring rule passes AC20 as well. A revert would stay green. Severity is medium because the consequence is a missing regression check, not a wrong result shipped now. | instance | - | class:rule-stated-with-no-check-that-fails |
