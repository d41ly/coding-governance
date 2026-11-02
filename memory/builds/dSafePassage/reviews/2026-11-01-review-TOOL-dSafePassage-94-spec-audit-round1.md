**Serves:** spec-audit TOOL-dSafePassage-94@rev-1

# Review: round-1 spec audit of TOOL-dSafePassage-94

This review was promoted from the round-5 closing diff review (memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-92-93-closing-diff-round5.md). TOOL-dSafePassage-94 edits only check_floor_bash in tools/govkit/selftest.py. A nested read_fallback_argv asserts in process that resolve_shell_argv(["bash", "x"]) returns its argv while _BASH is unset, and a narrowed copy of check_runs serves as an always-run red. read_stub_tail clears the stand-in's __pycache__ and pins its mtime before each shape, and a same-length two-body probe serves as its red.

Reviewed: memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md@cbfa76c8a58dab61c5922c7f87e5dd37f29fd2b2

ROUND: 1

## Verdict: CLEAN WITH FIXES

There are 0 blockers and 0 highs. The tally is 1 medium and 6 lows, counted the same way by item (7 items) and by raw confirmed finding (7 findings). The medium must be fixed in the spec before the build starts. The lows can be folded in during the same edit.

Review shape: intensity full, raw 7, confirmed 7, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 0 | 0 | 0 | 0 | 0 | - |
| failure-envelope | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

Run integrity:
- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 4/4 returned, 0 died.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fix verdicts on confirmed findings: 5 sound, 2 UNSOUND (ids 5 and 7, where the skeptic's corrected fix is the one written below), 0 with no fix proposed, 0 not judged.
- Severity: 0 findings were left ungraded by the skeptic. 1 was re-graded (id 4, medium to low).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: no spec was supplied as intent. `context` was the caller's own statement.
- Checklist: none was swept, because none exists. A zero count is not evidence that the project's recurring bug classes are absent.
- By design: the caller's byDesign.
- Move check: no checked subject moved.

Every lens returned. The blast-radius lens's zero is therefore a real empty result. It is still bounded by the generic brief and the missing checklist.

## MEDIUM

### M1 (id 1): no criterion decides S3's mtime pin

- **Where:** memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md. Section 2 S3 conflicts with section 6 AC2 and AC3. Section 4 "S3" and "Measured" are also affected.
- **What is wrong:** S3 lists the pinned mtime, `os.utime(stub92 / "upgrade_steps.py", ns=(0, 0))`, as an IN item. No acceptance criterion checks it:
  - AC3 greps only the `shutil.rmtree` line.
  - AC2 says the rmtree break makes the third check fail "on every run" but sets no run count.
  - The spec quotes three figures for that break: "every run" in AC2, "3 of 3" in the Measured table, "9 of 9" in the S3 prose.
- **Consequence:**
  - A build can omit the `os.utime` line, or put it before `write_text`, which resets the mtime.
  - AC1 still passes, because the rmtree clears the cache. AC3 still passes.
  - AC2's break goes red in only about 2 of 3 runs. The spec's own sample is 4 of 6. Because AC2 names no count, a single red run satisfies it.
  - The shipped left-shift arm would then be the flaky red that section 4 "Alternatives rejected" rejects.
  - The effect is contained to a test arm. No product behaviour changes.
- **Fix (judged SOUND by the skeptic):**
  - In AC3, add `git grep -n -F 'os.utime(stub92 / "upgrade_steps.py", ns=(0, 0))' -- tools/govkit/selftest.py`. It must print exactly one line, inside `read_stub_tail` and after the `write_text` line.
  - In AC2, give the rmtree break a fixed run count. Run AC1's command N times (for example 6, the sample that showed the 4-of-6 flake) and require the third `[dSP-94]` FAIL in all N.
  - Make the S3 prose, the Measured table and AC2 quote the same figure.
- **Left-shift gate:** every IN item in a spec's section 2 must be named by at least one acceptance criterion. A spec-lint leg can cross-reference the S-items against the AC text. Any AC that claims "every run" must state its N.

## LOW

### L1 (id 2): S1 claims the `finally` restore is observed, and section 5 says it is not

- **Where:** the same spec. Section 2 S1 ("Observed by AC1, AC2 and AC3") conflicts with the section 5 risks.
- **What is wrong:** S1 requires restoring `steps._BASH` in a `finally` and says AC1-AC3 observe all of S1. Section 5 says no check observes that restore.
- **Consequence:** a build that drops the `finally`, or restores before the call, passes every criterion. That leaves `us._BASH` as None, and later arms re-resolve bash from PATH. The effect is contained, but S1 tells the next reader the restore is covered.
- **Fix (judged SOUND by the skeptic):** do one of the following.
  - Change S1's "Observed by" line to name the gap ("the finally restore is not observed; section 5").
  - Or add a fourth `[dSP-94]` check right after the `with` block, `us._BASH == bash87`, and add the cut-`finally` break to AC2. This check holds after a correct restore: selftest.py:4440 fills the cache, the witness runs are subprocesses, and upgrade_steps.py:392-394 returns the cached value. With the `finally` cut, the check goes red.
- **Left-shift gate:** a spec-lint check should flag any S-item whose "Observed by" claim names a sub-item that section 5 lists as unobserved.

### L2 (id 3): S1's line citation for `test_floor_fallback` is one line short

- **Where:** the same spec, section 2 S1.
- **What is wrong:** S1 cites `test_floor_fallback` as `:4458-4467`, but the function ends at tools/govkit/selftest.py:4468, which is its `return` line.
- **Consequence:** cosmetic only. The function is not edited.
- **Fix (judged SOUND by the skeptic):** change the citation to `:4458-4468`.
- **Left-shift gate:** a citation checker should resolve `file:a-b` ranges that name a def and confirm the range covers the whole body, up to the next dedent.

### L3 (id 4): S2 builds its own staged copy instead of using `build_staged_copy`

The finder graded this medium. The skeptic re-graded it low, and low is the binding grade. I agree with low: S2 keeps `__file__` on the real HERE, and resolve_shell_argv and resolve_bash read no sibling module, so nothing wrong ships.

- **Where:** the same spec, section 4 "S2: the regression, staged in a copy", and section 10.
- **What is wrong:**
  - S2 stages upgrade_steps.py in memory, using `types.ModuleType` plus `exec(compile(...replace(...)))`.
  - It does not use `build_staged_copy` (TOOL-dSafePassage-71, tools/govkit/selftest.py:3640). That helper is the suite's one seam for staging a break in upgrade_steps.py, and selftest.py:3176-3185 already loads its output in process.
  - Section 10 cites selftest.py:7734-7736 as precedent, but that code stages govkit.py. It then concludes that no seam exists.
  - The dSP-71 AC4 guard (read_handpicked_copies, selftest.py:3650-3659) exempts paths rooted at `HERE`, so it cannot see S2.
- **Consequence:** the suite gets a second idiom for staging the engine, which is the kind of duplication dSP-71 collapsed. Section 10 also misleads the next reuse audit.
- **Fix (judged SOUND by the skeptic):**
  - Rewrite S2 on the selftest.py:3176-3185 shape:
    - `src94 = (HERE / "upgrade_steps.py").read_text(encoding="utf-8")`
    - `spec = importlib.util.spec_from_file_location("dsp94_upgrade_steps", build_staged_copy(tmp / "dsp94-narrowed", src94.replace(old, new)))`
    - `steps94 = importlib.util.module_from_spec(spec)`
    - `spec.loader.exec_module(steps94)`
  - Fold `src94.count(old) == 1` into the second `[dSP-94]` check, as `[dSP-87 AC6]` does.
  - Correct section 10 to cite build_staged_copy and selftest.py:3176-3185 as the seam S2 extends.
  - At build time, re-run AC2's third break (the replacement given back `except OSError:`) on the rewritten S2.
- **Left-shift gate:** widen the read_handpicked_copies guard so that it also flags in-memory `exec(compile(... "upgrade_steps.py" ...))` staging, including paths rooted at HERE.

### L4 (id 5): section 5 claims a raising read becomes a FAIL, but only the call is guarded

- **Where:** the same spec. Section 4 "S1: the read" and "S2: the regression, staged in a copy". Section 5 error states.
- **What is wrong:** only the resolve_shell_argv call sits inside the `try`. Two other steps run outside any guard:
  - building steps94 (the compile and exec of the copy);
  - `held = steps._BASH`, which raises if the memo is renamed.
  
  Section 5 says a read that raises "is recorded as a FAIL with its repr, not a crash of the suite". That holds only for the call.
- **Consequence:** an exception from either step escapes check_floor_bash (called at tools/govkit/selftest.py:4427) and then check_step_isolation. Every later check in main (selftest.py:5608-5614) is skipped, and the operator sees one traceback instead of a labelled `[dSP-94]` FAIL. The failure is loud, not a false green, so the effect is contained.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** do one of the following.
  - Build steps94 inside a `try`. On an exception, record `check("[dSP-94] the staged copy of upgrade_steps.py loads", False, repr(e))` and skip the second read. In read_fallback_argv, read the memo in its own guard before the restoring `try` (`try: held = steps._BASH` / `except AttributeError as e: return e`), then do the clear, the call and the `finally` exactly as S1 has them.
  - Or change section 5 to say that a failed copy build aborts the suite by design.
- **Left-shift gate:** add a checklist entry that every "recorded as a FAIL, not a crash" claim in section 5 must name the exact statements its guard covers.

### L5 (id 6): S2's `.replace` assumes, without checking, that the anchor occurs exactly once

- **Where:** the same spec, section 4 "S2: the regression, staged in a copy".
- **What is wrong:** S2 calls `str.replace` with no count and no check on how many times the anchor occurs. "Occurs once" was measured once at build time and nothing enforces it. The cited precedent (selftest.py:7731-7733) refuses with STAGE FAILED when the count is not 1.
- **Consequence:** if the anchor ever occurs twice or more, every site is narrowed. The second `[dSP-94]` check could then go green on an OSError from a site other than check_runs, while still claiming "check_runs narrowed". The first check remains the real gate, so the effect is contained.
- **Fix (judged SOUND by the skeptic):** put `src.count(anchor) == 1` in the second `[dSP-94]` check's condition and report the count in its detail. Alternatively, pass `count=1` and assert the count separately.
- **Left-shift gate:** a selftest lint should flag any `.replace(` on a staged upgrade_steps.py source that is not paired with a `.count(...) == 1` assertion.

### L6 (id 7): nothing proves the probe can move, either when no bytecode is written or when the cache removal fails silently

- **Where:** the same spec. Section 4 "S3: the cache removed" and "S4". Section 6 AC2 ("the third fails, on every run").
- **What is wrong:**
  - S4's red depends on the stub writing bytecode under `stub92/__pycache__`, and nothing asserts that a .pyc was ever written.
  - S3 removes the cache with `ignore_errors=True`, so a failed removal is silent.
  - Only node a was measured, but AC2 claims "every run".
- **Consequence:** on a node that writes no bytecode, cutting the rmtree cannot move the third check, and nothing reports that. The arm reads as coverage while it cannot go red. Such a node is unlikely, because the runner spawns with `-I` and stub92 is a writable scratch directory. No product result changes.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):**
  - After `read_stub_tail(absent94)`, add `any((stub92 / "__pycache__").glob("upgrade_steps.*.pyc"))` to the third `[dSP-94]` check's condition, or give it its own `[dSP-94]` check.
  - Keep `ignore_errors=True`.
  - After the rmtree in read_stub_tail, assert `not (stub92 / "__pycache__").exists()`.
- **Left-shift gate:** add a checklist entry that every always-run red must also assert the precondition that makes it movable.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=7 confirmed=7 refuted=0 unverified=0 blocker=0 high=0 medium=1 low=6 agents=10 out-tokens=89865

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md:section 2 S3 against section 6 AC2/AC3 (and section 4 "S3" / "Measured") | medium | medium | confirmed | I read the pinned blob cbfa76c8. S3 (lines 41-44) lists the os.utime pin as an IN item, and line 177 holds the pin line. AC3 (lines 300-303) greps only the shutil.rmtree line. AC2 (line 294) says the rmtree break makes the third check fail 'on every run' but gives no run count. No criterion names os.utime at all. The S3 prose at lines 185-186 says the probe went red in only 4 of 6 runs without the pin. So a build that leaves the pin out still passes AC1 and AC3, and its AC2 rmtree break is red only most of the time. A single red run satisfies AC2 as written. The figures also disagree: line 186 says 9 of 9, line 220 says 3 of 3, and AC2 says every run. The current read_stub_tail (selftest.py:4493-4499) has neither the rmtree nor the utime line, so nothing guards the pin today. The effect is contained: a test arm that can go flaky, with no product behaviour change. So medium. | sound | - |
| 2 | coherence | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md:section 2 S1 ('Observed by AC1, AC2 and AC3') against section 5 risks | low | low | confirmed | In the pinned blob, S1 (lines 33-36) requires the finally that restores steps._BASH and closes with 'Observed by AC1, AC2 and AC3'. Section 5 (lines 269-271) says 'The finally restoring _BASH is not observed by any check'. That is a real contradiction inside the spec, and no criterion would catch a build that cuts the finally. The consequence is a misleading coverage claim: a cut finally leaves us._BASH None, and later code re-resolves bash from PATH. The spec states that effect itself, so it is contained. Low. The fix is sound. selftest.py:4440 fills the cache with bash87 = us.resolve_bash(). The two witness runs in between happen in a subprocess through run_step_isolated, so they do not change the parent's us._BASH. upgrade_steps.py:392-394 returns the cached _BASH. So us._BASH == bash87 holds after a correct restore. With the finally cut, the cache stays None, because on that PATH resolve_bash raises the Refusal and never refills it, and the check goes red. | sound | - |
| 3 | grounding | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md:section 2 S1 | low | low | confirmed | Blob cbfa76c8 matches the working file. Spec line 35 cites `test_floor_fallback` (`:4458-4467`). I read selftest.py 4458-4469: line 4458 is the def, 4467 is `crashed = ...`, 4468 is `return not crashed and not any(...)` and 4469 is blank. So the function ends at 4468 and the citation is one line short. The function is not edited, so the only effect is on the citation. | sound | - |
| 4 | reuse | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md:section 4 "S2: the regression, staged in a copy" and section 10 | medium | low | confirmed | Re-probed and the facts hold. Spec S2 (lines 148-152) stages upgrade_steps.py in memory with `types.ModuleType` plus `exec(compile((HERE / "upgrade_steps.py").read_text(...).replace(...)))`. Section 10 (line 343) cites selftest.py:7734-7736 as the precedent, but that code stages GOVKIT (`govkit_ungraded`), not upgrade_steps.py. It concludes 'no existing seam fits a factory'. build_staged_copy exists at selftest.py:3640 (dSP-71 S1) and is the suite's helper for staging an upgrade_steps.py break. selftest.py:3176-3185 loads its result in process with spec_from_file_location and exec_module. The read_handpicked_copies regex at :3654 exempts `HERE`, so the dSP-71 AC4 guard cannot see S2. The reuse audit therefore missed a real seam, and the arm adds a second idiom. I grade this low, not medium. The hazard dSP-71 guards is a copy in another directory that misses a sibling. That cannot happen here: S2 keeps `__file__` on the real HERE, and resolve_shell_argv/resolve_bash (upgrade_steps.py:392-440) read no sibling. The current design ships no wrong result. The cost is a stale reuse-audit statement and a divergent idiom. | sound | - |
| 5 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md:section 4 "S1: the read" / "S2: the regression, staged in a copy"; section 5 error states | low | low | confirmed | Confirmed against the pinned blob. In S1, `held = steps._BASH` and `steps._BASH = None` come before `try:`, and the try covers only the resolve_shell_argv call. In S2 the steps94 ModuleType, compile and exec run with no guard at all. §5 (blob lines 265-266) says 'a read that raises is recorded as a FAIL with its repr, not a crash of the suite', but that only holds for the call. I traced the escape path: check_floor_bash is called at selftest.py:4427 inside check_step_isolation (def at :3684), and main runs check_step_walk, check_staged_copies, check_step_rollback and the rest after it at :5608-5614 with no try between them. So an exception from the copy's build would skip the rest of the suite. The 7734-7736 precedent is unguarded too. The failure is loud, not a false green, and the only defect is §5 claiming more than the design gives, so I grade it low. | unsound | - |
| 6 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md:section 4 "S2: the regression, staged in a copy" | low | low | confirmed | Confirmed. The spec's S2 uses an unguarded str.replace with no count. Its only basis for 'occurs once' is a build-time measurement. I re-ran the count command and it printed 1, so the claim is true today but nothing enforces it. The cited precedent at selftest.py:7731-7733 does enforce it: `if len(_guard) != 1: return f"STAGE FAILED: ..."`, then replace with count 1. S2 handles a missing anchor (the second check reads FAIL), but with two or more matches it would narrow every site, and the second check could go green on an OSError from somewhere other than check_runs. The first [dSP-94] check is still the real gate, so the effect is contained. I grade it low. | sound | - |
| 7 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md:section 4 "S3: the cache removed" and "S4"; section 6 AC2 ("the third fails, on every run") | low | low | confirmed | I read blob cbfa76c8 and the claim holds for the spec. S3 (line 171) removes the cache with `shutil.rmtree(stub92 / "__pycache__", ignore_errors=True)`. S4's check (lines 196-201) tests only `len(second94) == len(absent94) and "dsp94-second" in tail94`, so nothing asserts that a .pyc was ever written. On a node that writes no bytecode, cutting the rmtree cannot move the third check, and nothing reports that. §4 'Measured' records node a only and says Linux was not measured. AC2 (line 294) still says 'the third fails, on every run'. python_floor.py:26-30 loads the stand-in through spec_from_file_location/exec_module, which writes a cache only when bytecode writing is on. The path is unlikely, though. The runner spawns with `-I` (upgrade_steps.py:1465), which ignores PYTHONDONTWRITEBYTECODE and PYTHONPYCACHEPREFIX. I found no `-B` in upgrade_steps.py or selftest.py. stub92 is a scratch directory the selftest creates, so it is writable. The 'held-open .pyc' half is weaker still: CPython closes the .pyc after reading it. No product result changes, and the worst case is a test arm that cannot go red on an exotic node, so low. | unsound | - |
