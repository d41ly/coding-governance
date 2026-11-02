**Serves:** diff-review TOOL-dSafePassage-92 TOOL-dSafePassage-93

# Closing diff review, round 5: dSafePassage, the round-4 fix units TOOL-dSafePassage-92 and -93

2026-11-01 · Tier-2 · on `branch/unattended-dsafepassage-567339` · adversarial fan through `tier2-review.js` (5 finder lenses, then 2 skeptic batches, then this synthesis). This round reviews the units promoted from round 4 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-90-91-closing-diff-round4.md`). It does not review round 4's subject again. The spec audit is `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-92-93-spec-audit-round1.md`. Both units edit only test arms in `tools/govkit/selftest.py`. Neither changes product behaviour.

Subjects reviewed:

- 92: in `check_floor_bash`, one nested `test_floor_fallback(tail)` predicate grades the `[dSP-91 L2]` tail for a crash. It forgives a `FileNotFoundError` or an `OSError` subclass only when the tail shows a `subprocess.py` frame. `read_stub_tail` takes every tail from `run_step_isolated`. Seven `[dSP-92]` shapes cover the predicate.
- 93: `run_in_gov` gains a `root` keyword. A `[dSP-93]` hard-link arm triggers 90's link-or-alias refusal text and asserts that both names keep gov's original bytes and their link identity. 93's ledger narrows 91's `set_environ` claim.

**Reviewed range:** `2e6d48453881b97b7dd0f9a8f981b0beb28b7595...c86d51fa50b73d62fa9aa255423abf911ab5afe3`. **ROUND 5.**

## Verdict: CLEAN WITH FIXES

There is no blocker and no high. There is one medium: the new `[dSP-92]` predicate cannot tell the stub's fallback spawn apart from a spawn that crashes inside `resolve_bash`, so `[dSP-91 L2]` can read "falls back to bare bash" for a stub that never reached the fallback (item 1). There is one low: `read_stub_tail` leaves a bytecode cache behind that a future same-size shape could read stale (item 2). Both defects are in test code, and the current product code behaves correctly in both. One fix was judged sound. One was rejected, and this report gives the skeptic's corrected fix for it.

Review shape: intensity full, raw 2, confirmed 2, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| verification | yes | 0 | 0 | 0 | 0 | 0 | - |
| intent | yes | 0 | 0 | 0 | 0 | 0 | - |

Adjudicated tally by item: 2 items, of which 0 are blocker, 0 high, 1 medium and 1 low. By raw confirmed finding: 2 findings, of which 0 are blocker, 0 high, 1 medium (id 1) and 1 low (id 2). No findings were merged, so each item covers one finding.

### Run integrity

- Lenses: 5 of 5 returned, 0 died. Skeptic batches: 2 of 2 returned, 0 died.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 1 judged sound, 1 judged unsound, 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 left ungraded by the skeptic, 1 re-graded by the skeptic (id 1, from high to medium).
- Unverified findings: 0 answered uncertain by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were `gov-diff-reviewer`, the skeptic batches `gov-skeptic`, and the synthesis `gov-synthesizer`.
- Intent: no spec was supplied to the fan. `context` was the caller's statement, read beside the range's commit messages.
- Checklist: none was swept, because none is present. The zero counts on the security, verification and intent lenses are not evidence that this project's recurring bug classes are absent.
- By design: the caller's byDesign list.

## MEDIUM

### 1. `test_floor_fallback` cannot tell the fallback spawn from a spawn that crashes inside `resolve_bash` (id 1)

**Where:** `tools/govkit/selftest.py:4465-4468`, the `spawn_failed` branch of `test_floor_fallback` inside `check_floor_bash`, which grades the `[dSP-91 L2]` tail.

**What is wrong:** the predicate sets `spawn_failed` when the tail contains `subprocess.py"` and its last non-blank line starts with `OSError` or a direct subclass name. It then forgives the crash without checking which frame made the spawn. Any `OSError` raised out of a spawn before `tools/govkit/steps/python_floor.py:36` therefore grades as the fallback. One example is `check_runs` in `upgrade_steps.py:396-400` with its `except OSError` narrowed. The predicate's other needles are `python_floor.py:`, `upgrade_steps.Refusal` and `Set GOV_BASH`, and the colon form never appears in a traceback frame line. On Windows the `subprocess.py` frames fill the whole 20-line tail, so the `python_floor.py` and `upgrade_steps.py` frames that would show where the crash came from are cut off. This range introduced the gap. At the base, L2 still required `bash` or `python-floor.sh` in the tail and did not forgive a traceback.

**Consequence:** the finder reproduced this on node a (Windows, Python 3.15). It changed `check_runs`' `except OSError` to `except ValueError` in a scratch copy of the stub's step module and ran the floor witness through `run_step_isolated` on path87 with GOV_BASH unset. The stub raised out of `resolve_bash` on the text-file bash and never reached line 36. The tail was 20 lines of `subprocess.py` frames ending in `OSError: [WinError 216] ...`, and the predicate, copied verbatim, returned True. A stand-in `resolve_shell_argv` that calls `subprocess.run(["dsp92-absent"])` gives a byte-identical tail, so the seven `[dSP-92]` shapes all pass while the predicate cannot see which spawn failed. So `[dSP-91 L2]` would stay green on the regression it exists to catch.

**Why medium, not the finder's high:** the skeptic regraded it because the effect is contained. It needs a regression that does not exist today. The named regression is also caught elsewhere: the arm at `selftest.py:18498-18513` points GOV_BASH at a missing file, so a `check_runs` that no longer catches `OSError` lets `FileNotFoundError` escape there, and that arm goes red. What is actually wrong is that the `[dSP-91 L2]` label promises "falls back to bare bash", and the arm cannot tell that apart from a spawn crash inside `resolve_bash`.

**Fix (REJECTED by the skeptic; the skeptic's corrected fix):** inside the GOV_BASH-unset `set_environ` block of `[dSP-91 L2]`, save `us._BASH` and set it to `None`. Assert that `us.resolve_shell_argv(["bash", "x"]) == ["bash", "x"]` and that the call raises nothing. Restore `us._BASH` in a `finally`. Keep `test_floor_fallback` grading the tail only. Do not add a `want=False` `[dSP-92]` tail shape for a stand-in that spawns an absent program, because its tail is byte-identical to the `want=True` "finds no bash" shape. Use the `check_runs` `except ValueError` regression as the red probe of the new in-process assertion.

**Left-shift gate:** commit the `check_runs` `except ValueError` regression as a mutation arm beside `[dSP-91 L2]`, so the in-process assertion's red state is measured on every run. Add a checklist entry for the class: a check that forgives a crash by its tail must prove where the crash came from, and where a truncated tail cannot show that, the check must grade the call in-process.

## LOW

### 2. `read_stub_tail` leaves the stand-in's bytecode cache between shapes (id 2)

**Where:** `tools/govkit/selftest.py:4493-4499`, `read_stub_tail`, which rewrites `stub92/upgrade_steps.py` and then calls `run_step_isolated`.

**What is wrong:** `tools/govkit/steps/python_floor.py:27-30` loads the stand-in through `spec_from_file_location` and `exec_module`. The stub runs under `python -I`, which does not stop bytecode writes. Nothing in `upgrade_steps.py` or `selftest.py` sets `-B`, `dont_write_bytecode` or `PYTHONDONTWRITEBYTECODE`. The loader therefore writes `dsp92/govkit/__pycache__/upgrade_steps.cpython-315.pyc`, and it accepts that cache when the source's whole-second mtime and its size both match. Each rewrite lands within the same second as the one before, so only the source size tells the shapes apart. The skeptic confirmed this in the scratchpad: under `python -I`, two module bodies of the same size written in the same second both printed the first body's result, and the `.pyc` was left behind.

**Consequence:** no current check is affected. Today's four bodies differ in size (69 bytes for the absent-bash body, 61 for the raise body, and the other two are longer). The None shape has no source, so `get_data` raises before any cache is read. A future shape the same size as the one before it would silently grade the previous shape's tail. That shape's check would then certify what it does not run.

**Fix (judged SOUND by the skeptic):** in `read_stub_tail`, before each write or unlink, remove the cache with `shutil.rmtree(stub92 / "__pycache__", ignore_errors=True)`. Alternatively, add a nonce line such as `# shape N` so each body has a unique length. The build's probe: within one second, write two `resolve_shell_argv` bodies of the same length, one returning `["dsp92-absent"]` and one raising `RuntimeError`. Without the fix, the second run's tail shows `FileNotFoundError`, which is wrong. With the fix, it shows `RuntimeError`.

**Left-shift gate:** commit the same-length two-body probe as a permanent arm beside the `[dSP-92]` shapes, so a stale cache goes red on every run. Add a checklist entry for the class: a test that rewrites a Python module and re-imports it within one process run must clear `__pycache__` or run with bytecode writes off.

review-shape kind=diff-review round=5 intensity=full at=synth raw=2 confirmed=2 refuted=0 unverified=0 blocker=0 high=0 medium=1 low=1 agents=8 out-tokens=69541

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/govkit/selftest.py:4465 | high | medium | confirmed | Confirmed from the code. At selftest.py:4465-4468, test_floor_fallback sets spawn_failed when the tail contains 'subprocess.py"' and its last non-blank line starts with OSError or a direct subclass name. It then forgives the crash and never looks at which frame made the spawn. Any OSError raised out of a spawn before python_floor.py:36, such as one from check_runs in upgrade_steps.py:396-400 if its `except OSError` were narrowed, therefore grades as 'the fallback'. The predicate's only other needles are 'python_floor.py:', 'upgrade_steps.Refusal' and 'Set GOV_BASH', and the colon form never appears in a traceback frame line. This diff introduced the gap. At the base, L2 still required 'bash' or 'python-floor.sh' in the tail and did not forgive a traceback. I graded it medium, not high, because the effect is contained. It needs a regression that does not exist today, and the regression the finder names is already caught elsewhere. The arm at selftest.py:18498-18513 points GOV_BASH at a missing file, so a check_runs that no longer catches OSError lets FileNotFoundError escape there, and that arm goes red instead of reading a Refusal. What is actually wrong is that the [dSP-91 L2] label promises 'falls back to bare bash', and the arm cannot tell that apart from a spawn crash inside resolve_bash. | unsound | - |
| 2 | seams | tools/govkit/selftest.py:4497 | low | low | confirmed | read_stub_tail is new in this range: the base selftest.py has no match for it. At tools/govkit/selftest.py:4493-4499 it rewrites stub92/upgrade_steps.py and then calls run_step_isolated. python_floor.py:27-30 loads that module through spec_from_file_location and exec_module. Nothing in upgrade_steps.py or selftest.py sets -B, dont_write_bytecode or PYTHONDONTWRITEBYTECODE, and -I does not stop bytecode writes, so the loader writes __pycache__/upgrade_steps.cpython-315.pyc and checks it against the source's whole-second mtime and its size. I tested this in the scratchpad: under python -I, I wrote two module bodies of the same size in the same second. The second run printed the first body's result (AAAA twice), and m.cpython-315.pyc was left behind. The hazard is real. The finder is right that it is only latent: today's four bodies differ in size, and the None shape has no source, so get_data raises before any cache is read. No current check grades a stale module. That is why the grade is low. | sound | - |
