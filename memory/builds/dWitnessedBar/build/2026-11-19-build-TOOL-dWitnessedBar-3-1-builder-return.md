**Serves:** journal TOOL-dWitnessedBar-3

# TOOL-dWitnessedBar-3 — builder return 1 (run `wf_61d7a898-fd8`), committed 9991872c0

## Why

TOOL-dWitnessedBar-3 is built and committed as one pass commit. The spec was buildable as written, so there was no divergence. All of AC1 to AC8 except one AC8 clause (see below) were observed with probes of the changed code. Every other criterion only a gate or a suite can see is listed in the summary for the close to run.

## Summary

TOOL-dWitnessedBar-3 is committed as 9991872c0 on top of 816d4aa91. The spec header reads CLOSED at 2026-11-20. The commit carries `Pass: TOOL-dWitnessedBar-3`, the Gov-Policy and Proof trailers that policy_edit.py asked for, and three `Decided:` lines.

**What was built**
- **Block table:** new `tools/run-gates/lib-verdict.sh` with `derive_red_blocks`. It is on the runner's KF3 list.
- **Runner:**
  - It reads `GATE_VERDICT_BLOCKS` once and then unsets it. An absent value counts as every-red and the summary says so.
  - The attribution record now has ten fields, with `blocks` ninth.
  - Each `GATE attr` line ends `· blocks` or `· passes`, and the summary adds the value and the blocking count.
  - The inherited-green stamp is written only when every red passes, and it records `blocks`.
- **Post-merge:** the scrub now unsets `GATE_VERDICT_BLOCKS`.
- **Pre-push hook:**
  - It reads `verdict.blocks` at R through `policy.py get --rev`. A copy of the policy kit inside the pushed tree is vetted first.
  - It exports `GATE_VERDICT_BLOCKS`.
  - `check_inherited_verdict` lands a red only when every row reads `pass`, and it is asked under every value.
  - Under every value except every-red, `classify_docs` treats a doc-only push as before and the age bound is exported.
  - A stamp is accepted only when its `blocks` equals the value at R.
- **Unattended driver:**
  - New `read_gate_blocks`.
  - `read_gates_record` decides from field 9: land, hold, or other.
  - `write_inherited_asks` files one ask per row reading `pass`, and the ask names the class.
  - `gates-green` hands the value to the bar and runs the new `run_verdict_route` on every red bar.
- **`tools/run-gates/verdict_flow.py`:**
  - `route` and `judge`, plus `--fixture route` and `--fixture red-route`.
  - `judge` reaches the loop and policy kits by running them as subprocesses.
  - `judge` exits 2 until the `items --tag` verb that TOOL-dWitnessedBar-100 asks for lands.
- **Upgrade step:** new row `govkit/inherited-red-to-verdict-blocks` with script `tools/govkit/steps/inherited_red.py`.
- **Gov's own files:**
  - `.githooks/gate-env.sh` no longer sets `INHERITED_RED`.
  - `.governance/policy.toml` now has `verdict.blocks = "own-mixed-contended"`, written through `policy_edit.py`. That tool also wrote the change record `memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-3-change-1.md`, which I declared with `--dispatch` before staging it.
- **Re-pointed to the new key:**
  - Code: govkit's `POLICY_KEYS` and its self-test, the policy kit's `GATE_ENV_MARKS` mark, the legacy fixture in `check_policy.py`, and the two catalogue rows' summary and usage.
  - Generated lists: `unsummarised-keys.txt` and `legacy-homes.txt`, rewritten by `lists --write`; `help/reference/policy.md`, re-rendered; one new row appended to `landed-steps.txt`.
  - Docs: the run-gates README (it now has a "Which red blocks" section and a migration note), the STOPS and PROTOCOL templates and their two copies under `memory/guides/`, and the comments in `.unattended.conf` and `.unattended.conf.example`.
  - The three suites: `run-gates.test.sh`, `pre-push.test.sh` and `unattended.test.sh`.
- **Kickoff manifest:** `last-audit` re-stamped, with one claim corrected (the `GATE_ATTRIBUTE` line no longer says report-only).
- **Records:** the acceptance ledger is written, and `gen_build_index --write` and `gen_map --write` outputs are committed.
- **Write set:** every staged path was inside the declared set.

**Checks that ran** — none is a gate or suite. They stand in for the runner, hook, unattended and policy suite legs.
- AC1: the section 6 command printed the four rows of the table; the `bogus` row equals every-red.
- AC2: the grep counted 7 lines naming `lib-verdict.sh` in `run-gates.sh` (DERIVED from the builder's probe).
- AC3: `--fixture route` passed, including a red the attribution leaves out.
- AC4:
  - The section 6 `eval` printed `rc 0` over the all-pass dir and `rc 1 y reads OWN and blocks` over the other.
  - End to end, I ran the real hook over two fixture repos under `%TEMP%/vbh`. A MIXED red was refused under own-mixed-contended at R and landed under own-only at R.
- AC5: `--fixture red-route` passed, and the import grep printed nothing.
- AC6: the grep lists only the step row, `inherited_red.py`, and the README migration note.
- AC7: `up`, `down` and `witness` over five scratch targets; `down` restored each byte for byte (`diff -r` empty).
- AC8: both greps printed 0 and 2.
- Driver: I sliced out `read_gate_policy`, `read_gates_record` and `run_verdict_route` and ran them over planted run dirs.

**Owed at the close**
- Every section 7 leg.
- RED-first observation of both `New arm:` lines:
  - `run-gates.test.sh` TOOL-dWitnessedBar-3 AC2 arms. Stage the break by dropping `lib-verdict.sh` from the KF3 list, or by writing the stamp on INHERITED instead of `pass`.
  - `pre-push.test.sh` TOOL-dWitnessedBar-3 AC4 arms. Stage the break by testing the class in `check_inherited_verdict`, or by dropping the stamp's `blocks` comparison.
- The re-pointed arms of `unattended.test.sh`, under the README's waiver rule.
- `.governance/policy.json` must be re-rendered by `policy.py mirror --write` in the next commit, as `guard.py` and section 4 Rollout require. It is not in this commit.
- The one AC8 clause not observed: `policy.py get verdict.blocks` with no `--rev` reads the landed revision, so it prints own-mixed-contended only after landing; this needs re-checking after landing.

**Bug-class checklist** (`gotchas.py --for-diff HEAD~1..HEAD`) ran and I acted on what it named:
- The new runner knob `GATE_VERDICT_BLOCKS` is in the hook suite's inert-knob class, in place of the retired one.
- Every reader of the attribution record by position is re-pointed: hook, driver, and the fixtures that copy the kit (they now copy `lib-verdict.sh`).
- No new name collides in the long functions.
- The commit diff has no stray control bytes.

No command went past its time limit.
