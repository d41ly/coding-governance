**Serves:** diff-review TOOL-aPiecewiseGrade-5 TOOL-aPiecewiseGrade-6

# Tier-2 diff review: Build aPiecewiseGrade fold (TOOL-aPiecewiseGrade-5, TOOL-aPiecewiseGrade-6), round 2

Provenance: an attended Tier-2 review of the fold only. Finders were gov-diff-reviewer, skeptic batches were gov-skeptic, and synthesis was gov-synthesizer. Intent came from 3 spec documents supplied as `specs`, read beside the range's commit messages.

Range: 4cdddad5cdcb2173f62c2d598bdbbca51378b12c...be79820d036f9d7bbcb8969c0411416135e14023 (round 1's tip to HEAD). Round: 2.

## Verdict: CLEAN WITH FIXES

Both folds close their round-1 items in the shipped code. No finding shows a lock left held on a return, a live checker's lock broken, claim-push behaviour moved, or a counter mismatch that stays silent. Each confirmed finding is a missing regression arm, so a future change could undo a guard the fold added and the suite would stay green. Tally: 2 items, 0 blocker, 0 high, 1 medium, 1 low. By raw confirmed finding: 2 confirmed, 0 blocker, 0 high, 1 medium, 1 low.

Review shape: intensity full, raw 2, confirmed 2, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |

Run integrity: lenses 5/5 returned, 0 DIED. Skeptic batches 2/2 returned, 0 DIED. 0 contradictory verdicts were demoted to unverified, 0 orphaned duplicate refutations were demoted, 0 duplicate refutations were counted as merged confirmations, 0 spurious verdicts were discarded, and there were 0 duplicates. Fixes on confirmed findings: 1 judged sound, 0 judged UNSOUND, 1 judged INSTANCE-ONLY, 0 none proposed, 0 NOT JUDGED. Severity on confirmed findings: 0 UNGRADED, 0 RE-GRADED by the skeptic. Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict. Lens notes: none supplied, so every lens ran on the kit's generic brief. The checklist held 54 items, acquired with --for-diff 4cdddad5c..HEAD, split security 11, correctness 11, seams 11, verification 11, intent 10. By design: the caller's byDesign plus 1 invariant from the checklist's by-design block. Refuted findings shown: 0. Same-address pairs shown: 0. No twin flags. The run is complete: every count above is zero where it must be.

## Items

### 1. MEDIUM: the foreign-runtime clause of the lock stale check has no arm that can fail (id 1)

- Where: tools/unattended/unattended.sh@13a5efd0:2563, in check_dir_lock_stale.
- What is wrong: before it reads a recorded pid as gone, the stale check requires `[ "$w" = "${HOSTNAME:-}:${OSTYPE:-}" ]`. Spec 6 S9 (spec line 225) lists this as one of the four conditions for reading a process as gone. The new pg6 block in tools/unattended/unattended.test.sh (lines 7966-8091) writes every pid plant through write_pg6_pid, which calls write_dir_lock_pid. That function always stamps the local runtime. So no plant carries a foreign runtime field: not AC3, AC10, AC11, the three AC12 plants, or the four AC13 kinds (driver, checker, stampless, pending). The staged RED-first list (spec line 650) leaves this clause out.
- Consequence: deleting the clause leaves the driver suite green. After that regression, a lock held by a live checker from another runtime, such as WSL beside MSYS on one worktree, reads as dead when its pid is missing from this process table. The lock is then broken while that checker runs, which reopens round 1's same-slug sweep overlap. The skeptic narrowed the claim: reading the runtime from the wrong column would make every local plant read as live, and AC12 would fail. Only the deletion mutation survives.
- Grade: medium (binding). The shipped code is correct, and the effect is limited to an undetected future regression.
- Fix (judged SOUND by the skeptic): add a `foreign` kind to the AC13 loop. It writes a pid.driver line with a dead pid and the runtime field `otherhost:otheros`, directly with printf because write_dir_lock_pid stamps the local runtime, and no checker file. Expect `foreign:1:w-x`, meaning the run is busy and the owner is kept. Stage RED by deleting the runtime clause at tools/unattended/unattended.sh@13a5efd0:2563.
- Left-shift gate: make every condition in a stale or liveness predicate a required RED-first entry in the spec's staged list. The `harness arms (fail branches armed or pinned)` leg could then require one arm per `&&`/`||` clause of check_dir_lock_stale.
- Disposition: class:refusal-branch-with-no-arm.

### 2. LOW: the counter key-set guards (S3 raise, S4 cache miss) have no permanent arm (id 2)

- Where: tools/check-spec-tokens.py@7ecdf1aa:2066 (S4: `if got[2].keys() != set(SPEC_COUNTERS): return None` in read_spec_cache), and tools/check-spec-tokens.py@7ecdf1aa:2448 (S3's KeyError raise, lines 2448-2449).
- What is wrong: the suite diff (+15/-1 in tools/check-spec-tokens.test.sh) adds only the four nonzero arms at 568, 1070, 1081 and 2132. The PG1 cache arms (2379-2517) tamper with `key`, `.inputs` and an unparseable .json. None drops or renames a counter in a cached entry's `counts`, and none makes `scan_live_spec` return another key set. The spec's AC3 and AC4 are observed only by the one-shot `$SCRATCH/pg5.sh` probe, which spec §4 (line 281) removes after the pass.
- Consequence: after the close, deleting line 2066 or lines 2448-2449 leaves `spec-tokens self-test` green. Without S4, an edited cached entry with a valid key and a dropped counter counts as a hit. If S3 is also gone, that spec's counter is summed short with no message. Only an edit to the checker or the cache can reach this today.
- Grade: low (binding). These guards protect invariants, and today's output is correct. What is missing is a regression guard.
- Fix (judged INSTANCE-ONLY by the skeptic; the class-level fix follows): add two permanent arms.
  1. A `cache dropped` arm: take PG1's warm cache, delete `ao_bad` from one entry's `counts`, recompute nothing else, and expect that spec in graded.list and stdout equal to the plain run. It reds when line 2066 is deleted, because S3 then raises.
  2. A fresh-path mutant arm: load the checker with importlib, wrap `scan_live_spec` so the `counts` it returns lacks one SPEC_COUNTERS key, call `main([])` uncached, and expect a KeyError naming that counter. It reds when lines 2448-2449 are deleted, because the run then sums short and exits normally.

  The finder proposed only the `cache dropped` arm, staged RED by deleting line 2066. That cures the cited S4 instance alone and leaves the S3 raise without an arm.
- Left-shift gate: an acceptance criterion observed only by a `$SCRATCH` probe that the spec removes after the pass should be refused at close unless a permanent suite arm discharges it. This could be a check in `spec tokens (the pass's own spec)` or in `harness arms (fail branches armed or pinned)`.
- Disposition: class:observed-by-claim-no-arm-discharges.

review-shape kind=diff-review round=2 intensity=full at=synth raw=2 confirmed=2 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=1 low=1 agents=8 out-tokens=58854
review-round round=2 limit=- prior=0 count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | verification | tools/unattended/unattended.sh@13a5efd0:2563 | medium | medium | confirmed | I confirmed the main claim against the code. At tools/unattended/unattended.sh@13a5efd0:2563, check_dir_lock_stale requires `[ "$w" = "${HOSTNAME:-}:${OSTYPE:-}" ]` before it treats a recorded pid as gone. Every pid plant in the new pg6 block (unattended.test.sh 7966-8091) is written through write_pg6_pid, which calls write_dir_lock_pid, and that function always stamps the local runtime. That covers AC3, AC10, AC11, the three AC12 plants and the four AC13 kinds (driver, checker, stampless, pending). None of them carries a foreign runtime field, and a grep for foreign, OSTYPE or otherhost finds nothing in the block. If the clause is deleted, every plant still reads the same way, so the suite stays green. That leaves spec 6 S9's foreign-runtime row (spec line 225) with no arm that can fail. One part of the finder's claim is wrong: reading the runtime from the wrong column (for example $t) would make every local plant read as live, and AC12's 'three locks ... are broken and logged' check would fail. So only the deletion mutation survives. This is a gap in verification that the fold introduced. The shipped code is correct today, and the effect is contained to a future regression going undetected, so it is medium. | sound | - | class:refusal-branch-with-no-arm |
| 2 | verification | tools/check-spec-tokens.py@7ecdf1aa:2066 | low | low | confirmed | Confirmed. At tools/check-spec-tokens.py@7ecdf1aa:2066, `if got[2].keys() != set(SPEC_COUNTERS): return None` is S4, and lines 2448-2449 hold S3's KeyError raise. The suite diff over 4cdddad5c..be79820d0 is +15/-1 in tools/check-spec-tokens.test.sh: it adds the nonzero arms at 568, 1070, 1081 and 2132 and nothing that edits a cached entry's `counts`. The PG1 cache arms at 2379-2517 tamper only `key`, `.inputs` and an unparseable .json (the forge arm at 2458-2486). They never drop or rename a counter, and no arm monkeypatches `scan_live_spec` to return another key set. The spec's AC3 and AC4 are observed only by `$SCRATCH/pg5.sh`, which spec §4 (line 281) says is removed after the pass. So deleting either guard leaves the self-test green. None of the BY DESIGN items covers this: the owed red-then-green observations apply to arms that exist. Graded low because the guards are invariants reached only by editing the checker or the cache, and today's code behaves correctly. The gap is a regression guard that is missing, not wrong output. | instance | - | class:observed-by-claim-no-arm-discharges |
