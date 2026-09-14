**Serves:** journal TOOL-aBatchedArm-5 TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3

# Fix brief — the closing diff review's findings, before the one gate pass

The closing diff review of build aBatchedArm, round 1, is
`memory/builds/aBatchedArm/reviews/2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round1.md`:
BLOCKED, 20 confirmed rows in 13 defects D1–D13, precision 0.95, every citation re-verified by the
report's author. Read it WHOLE first; each defect carries file:line, the failing state, the fix and
a left-shift. This brief is the order and the rules, not a restatement.

## The rulings, and what this pass may run

Every unit is built, so the owner's "no gate until every unit is built" is satisfied; the ONE gate
pass follows this fix pass. This pass may run: every seconds-long static gate the review names on
its rows (`python tools/lexicon/lexicon.py`, `python tools/codebase-map/test_codebase_map.py`,
`python tools/codebase-map/gen_map.py --write`, `bash tools/check-install-prefix.sh`,
`bash tools/check-line-length.sh`, `run-selftests.sh --check/--list/--rank`, `bash -n`); the
runner's self-test `bash tools/run-gates/run-selftests.test.sh` ONCE, direct and timed with
`date +%s`, on a frozen `git clone --local` under a short `$TEMP` path — the review's step 2 needs
its observed wall to re-declare the leg's ceiling and budget row; and the new linter and its test.
It may NOT run `check-unattended.test.sh` in any mode or shard, the other unattended suites, the
bar, or `run-unattended-gates.sh`; those are the gate pass's, after this.

## The order (the review's own, with the rulings applied)

1. **D1 — the lexicon leg.** Rename the two unit-3 helpers and the unit-1 helper to table verbs,
   every call site in the same commit: `replay_landed_main` → `run_landed_replay`,
   `topo_capture` → `read_topo`, `emitted` → `check_emitted` — the last one also in
   `tools/unattended/check-arms-groups.sh` (rule A keys on the helper name) and its `.test.sh`, and
   in the sentinel's own `FAIL emitted:` text, which becomes `FAIL check_emitted:` so the name and
   the message agree; the phrase `expected set not yet observed` stays verbatim because D3's regex
   keys on it. Do NOT re-declare `VERB_OFFENDER_PIN`; read `python tools/lexicon/lexicon.py` on the
   tree and it must print offenders 984 over pin 984. Spec prose keeps the old names as history.
2. **D2 — the codebase-map leg.** Claim `unattended arms-groups selftest` under `gate-legs` in
   `memory/map/features/unattended.md`, run `python tools/codebase-map/gen_map.py --write`, commit
   the regenerated artifacts in the same commit, and run
   `python tools/codebase-map/test_codebase_map.py` to see it green.
3. **D5 and D6 — the two dead arms in `run-selftests.test.sh`.** D5: wrap the calibrate arm's
   subject in `( … )` exactly as its siblings at the review's `:598` and `:646` do. D6: keep the
   refusal phrase `so the run would be killed before its` contiguous on one echo line in
   `run-selftests.sh`. Then the ONE direct timed run of `bash tools/run-gates/run-selftests.test.sh`
   on a frozen clone; from its wall, re-declare the `run-selftests self-test` ceiling in
   `tools/gate-legs.json` and its budget row in `tools/run-gates/selftest-budgets.txt` (reading ×1.5,
   the condition named: direct, frozen clone, this node, beside whatever `ps` shows). If D9's
   `walled 1` arm flakes in that run, assert only the `walled 1` token as the review says. Every
   other new arm must be GREEN in that run or fixed; paste the run's `PASS`/`FAIL` line and the
   wall.
4. **D4 — the five green-only trailers.** The design-consistent fix: each of
   `tools/unattended/adopt-unattended.test.sh`, `cross-component.test.sh`, `check-playbook.test.sh`,
   `check-arms-groups.test.sh` and `unattended.test.sh` prints one unconditional
   `echo "  ($n assertions executed)"` line before its `[ "$st" = 0 ] && echo "PASS …"` line — the
   alternative `SWEEP_TRAILER_RX` already recognises — so a red-but-complete run carries its
   trailer. Update `selftest-pooled-evidence.txt`'s header if it names any of them. Add the
   review's left-shift `--check` arm: for every row not declared `no-trailer`, the row's script
   carries a trailer print outside a `[ "$st" = 0 ] &&` guard, red by name otherwise — static,
   seconds, observed RED on a scratch copy first.
5. **D3 and D7 — the runner.** (a) `SWEEP_NOBASELINE_RX='expected set not yet observed'` beside
   `SWEEP_TRAILER_RX`; a hit is `untrailed` at calibrate (no reading, RED, the row named) and
   `MISMATCH` under `--pooled`. (b) persist each row's `$d/out` before the EXIT trap fires, to
   `$(git rev-parse --git-dir)/gate-logs/selftests/<row>.out`, and print that path on every
   non-`ok` row. (c) D7: `sound=1`, cleared in the three unsound branches, the writer wrapped in it,
   `readings NOT written: this calibrate was unsound` and exit 1 otherwise, the RED summary naming
   the cause. Add the two left-shift arms the review names (sentinel row → RED untrailed, evidence
   file byte-unchanged; unsound calibrate → evidence file byte-unchanged), each observed RED on the
   fixture first — they are seconds.
6. **D8, D10, D11, D12** — each a few lines, each with its arm where the review names one.
7. **D3(a) — the landing order.** Re-state in `memory/builds/aBatchedArm/RUN.md` (a `## Landing
   order` block under the authored half) and in unit 5's spec S5 (a rev-8 §9 line): the eight
   direct shard runs → the paste of each group's observed set into its `check_emitted` call, the
   run named beside it → re-run until no `FAIL check_emitted:` line → the calibrate → commit the
   evidence → `run-unattended-gates.sh --pooled` GREEN → the flip. D13 is re-measured at those
   shard runs, not here.

Commit per numbered step, subject `aBatchedArm closing fix <n>: …`, the Co-Authored-By trailer;
`python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` after each and act on it. Every `.sh`
edit at the byte level (LF committed; the Edit tool or binary-mode scripts; no backslash escapes
through heredocs). The manifest ratchet: `run-selftests.sh` is on the `watch:` line, so
`last-audit` is re-stamped at the merge-base in the same commit as its first edit.

## What done looks like

- `python tools/lexicon/lexicon.py` → offenders at pin; `python tools/codebase-map/test_codebase_map.py`
  green; `bash tools/run-gates/run-selftests.sh --check` green; install-prefix, line-length,
  memory hygiene, `gen_build_index.py --check-format` green.
- The direct `run-selftests.test.sh` run GREEN, its wall pasted, the ceiling and budget row
  re-declared from it.
- A closing-fix ledger at
  `memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-5-2-closing-fix-ledger.md`
  (`**Serves:** journal` the four ids above) listing each defect, its commit, and the observation
  that closed it — or, for D13, that it is owed at the shard runs.
- Return the list of commits and any defect you could not close, with why.
