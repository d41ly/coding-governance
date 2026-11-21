**Serves:** journal TOOL-dWitnessedBar-110

# TOOL-dWitnessedBar-110 — builder return 1 (run `wf_13dae94e-10b`), committed 8443f6d857f558a179aff2deabb0e3a0e663240a

## Why

Every claim the spec makes about current code still holds at base 4bfcda23f, including unit 109's landed extract_message_lines, _ATTRIBUTION_FIXTURE, A4 and A6. So TOOL-dWitnessedBar-110 was built as written, with no divergence, and committed as one pass commit. Its trailers are Pass: TOOL-dWitnessedBar-110 and the charter's Co-Authored-By line, and the spec status is set to CLOSED in the same commit.

## Summary

Built TOOL-dWitnessedBar-110 in commit 8443f6d85 on base 4bfcda23f. The commit-msg hook admitted it and added Commit-Checked: unattended@1.129.

**What changed:**
- **S1 to S3, verify-peer:** `run_verify_peer` in `tools/run-gates/verdict_backends.py` now hands its bar `GATE_RUN_ID=vp-<secrets.token_hex(8)>` and publishes a slot only when the slot's `run_id` equals that id, at both the read and the re-read. The `before` read, its refusal and the `env.pop` call are gone. The plant's stub modes write the id they are given, and the new `redok` and `foreign` modes bring it to ten scenarios. The docstrings and `help/verdict-backends.md` now describe this.
- **S4, the unarmed message:** in `tools/unattended/unattended.sh`, the exit-0 branch of `check_commit_message` now prints `unattended: --check-commit did not check attribution: <reason>` when the charter names no trailer. It is one line rewritten as one, and the code-line count stays 9793.
- **S6 and S7, trailing whitespace:** `extract_message_lines` now strips trailing whitespace from each kept line, and `_ATTRIBUTION_FIXTURE` gains a seventh case. The same edit went into all three `commit_trailers.py` copies.
- **S5:** `tools/unattended/unattended.test.sh` gains the unarmed arm after A4 and one more `hit` in A6.
- **S8:** the floor harness in `.githooks/pre-push.test.sh` gains revision R4, its bindings and the row `AC1 nopy R4 every-red push-selected refused`.
- **S9:** two new sentences in `help/tags.md`.
- **S10, the shell-role ledger:** `ratchet.py widen` wrote record widen-30, and the two suite rows were set to their measured counts, 13973 and 2417. A `Decided:` trailer records why, as unit 109 did.
- **Records:** the acceptance ledger `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-110-1-acceptance-ledger.md`, the output of `gen_build_index --write` (LIVE.md, backlog/TOOL.md, the build README and the spec's records table), and RUN.md.

**Checks that ran** (fixtures and probes only; no gate, suite or bar):
- **AC1 to AC3:** `python tools/run-gates/verdict_backends.py --fixture --plant peer-stale-slot` printed `10 of 10 scenario(s) held · all held` and exited 0. The foreign scenario was refused `at run s-foreign`, and both tags read `run_id\tvp-`. Stands in for the `run-gates gov canary` leg.
- **AC6:** a `python -I` probe of all three copies read `ok` for the charter's trailer followed by a space and a tab, and `refused` for the 5.5 value followed by a space. The three marker blocks are identical. Stands in for the `python resolver (… inline parity …)` leg.
- **AC7:** `tools/lib/commit_trailers.py --fixture` exited 0 and printed the seventh case's `ok` line. A scratch copy with the `rstrip()` taken out printed `FAIL, the case plants ok` and exited 1, so this arm was seen red at the pass.
- **AC9:** `scan_policy_bytes` and `derive_strictest`, extracted from `.githooks/pre-push`, read R4's text as every-red, push-selected and refused. With the `"$2.$3")` arm removed they read nothing. Stands in for the `pre-push self-test` leg.
- **AC5:** the S4 branch, run over the real `attribution` verb, printed the reason for a charter with no fact line and for an absent charter, and nothing for `ok`.
- **AC3, AC4 and AC10:** the greps return what each criterion expects.
- **AC11:** `sh_hygiene.py --shell-role --measure` matches every row (`portability` leg).
- **Other:** `bash -n` on the three shell files, and `gen_map.py --check` exited 0, so the codebase map is not stale and no function was added. The pre-commit memory-hygiene `--staged` run passed, with one warn-only notice that the build README entry is 376 characters against a budget of 350.

**Owed at the close:**
- **New arm RED-first observations:**
  - the plant's `foreign` scenario against HEAD's before-and-after test, and the `redok` scenario with `and rc != 0` dropped, which should print MISSED and exit 3 (AC2);
  - the unattended suite's unarmed arm against the silent `0)` branch, and A6's seventh `hit` against the compare without `rstrip()` (AC8);
  - the R4 row with the `"$2.$3")` arm removed, inside the pre-push self-test.
- **Legs:** run-gates gov canary, pre-push self-test, python resolver, python reads, portability, scratch-guard self-test, tier2-review self-test, recall floor and recall floor arms, memory hygiene and spec tokens.
- **The unattended suite:** it runs arm S5 and A6's seventh `hit`. Per the owner's standing instruction it was not run in this pass.

**Bug-class checklist:** `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` selected 63 classes. I acted on these:
- **heredoc-escape:** my first attempt at the S6/S7 edit went through a heredoc and garbled the backslashes. Its own assertion stopped it before anything was written, and I redid the edit from a script file.
- **retirement-inventory-misses-readers-by-value:** `git grep` finds no reader left of `does not read before the bar`, `run_id\ts-red`, `run_id\ts-clean` or `after three refusals`.
- **refusal-branch-with-no-arm:** the new unarmed message and the `after != nonce` refusal each have an arm. The `again != nonce` re-read refusal had no arm before this unit either.
- **portability:** the edits to the three copies were byte-for-byte LF.

**Split:** as spec §4 states, this batch splits into three disjoint product write sets: verdict_backends.py with its help page; unattended.sh, the trailer copies, the unattended suite and tags.md; and pre-push.test.sh. The second and third share shell-role.txt and the widen record.
