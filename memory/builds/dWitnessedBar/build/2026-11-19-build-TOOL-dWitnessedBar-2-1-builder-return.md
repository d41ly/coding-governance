**Serves:** journal TOOL-dWitnessedBar-2

# TOOL-dWitnessedBar-2 — builder return 1 (run `wf_297d3007-93e`), committed 7f3e24092b9c6da7a87362ca7157bf0c49eec368

## Why

TOOL-dWitnessedBar-2 is built as its rev-4 spec says. It is committed as one pass commit with a `Pass: TOOL-dWitnessedBar-2` trailer, and the spec header is set to CLOSED (2026-11-20) in that same commit. The commit check added `Commit-Checked: unattended@1.129` to this commit, which shows S4 working on a real commit.

## Summary

Built TOOL-dWitnessedBar-2 and committed it as 7f3e24092b9c (base 795eccc80fb4). No gate, suite or bar ran. Every criterion was checked with a probe of this unit's own code; those probes stand in for section 7's legs, which the close still owes.

**What was built:**
- **Bypass record:** `write_bypass_line` writes one `decision=bypass` line to `runlog/pushes.log`. It is byte-identical in `tools/push-main.sh` and `.githooks/pre-push`.
- **Lander:** an UNGATED landing now writes an `ungated-landing` line. Its `tree_verdict` comes from the `local-hook` reader (GREEN, RED or none).
- **Lander policy check:** `check_landing_verdict` reads `hooks.bypass`. Under `refused` it asks the new `verdict_backends.py off-node` verb and refuses the landing unless `verdict` names an off-node backend.
- **Pre-push hook:** reads `hooks.bypass` at R inside `read_policy_at`. It walks the pushed range with the new `commit_trailers.py unchecked` verb and records each pass commit that has no `Commit-Checked:` trailer. Under `refused` it refuses with `bypass-refused` (run-log decision `refuse-bypass`) from exactly two sites.
- **Commit check:** `check_commit_message` adds `Commit-Checked: unattended@<version>` on its admitting path. A failed append prints one line and still admits, so no new refusal site.
- **Pass-order leg:** `check-pass-order.sh` lists unwitnessed pass commits past the `git log -S` anchor. It exits 1 under `refused`, prints a note under `allowed`, and `--preview` lists them under either value. The summary line says when there is no anchor.
- **Trailer key:** `Commit-Checked` is added as a row in `edges.toml` and to `FLOOR_KEYS` in all three `commit_trailers.py` copies; the three blocks are byte-identical.
- **Docs:** the catalogue row gets its summary and usage, the key is drained from `unsummarised-keys.txt`, and `help/reference/policy.md` is re-rendered. `help/tags.md`, `tools/runlog/README.md` and `tools/run-gates/README.md` are updated, and `symbols.json`, the build index and the acceptance ledger are in the commit.

**Probes that ran (each stands in for the named suite or leg):**
- **AC1:** the AC1 grep counts 1 in each of the three files. The reader-coverage regex from `check_policy.py`, run on non-comment lines, finds the key in all three. `policy.py get hooks.bypass --explain` prints `allowed` from the catalogue default. Stands in for `policy fixtures`.
- **AC2:** a lander copy in a scratch repo pushed through a hook that leaves no allow record. It exited 4 and wrote the `ungated-landing` line with `tree_verdict=none`; with a planted GREEN per-tree verdict the line read `tree_verdict=GREEN`. Stands in for `push-main self-test`.
- **AC3 and AC4:** real pushes through a scratch copy of the hook.
  - Under `allowed`, the push proceeded and only the unwitnessed commit was recorded.
  - Under `refused` with `verdict = peer-node`, it was refused (`bypass-refused`), the record was still written, and the END line read `decision=refuse-bypass`.
  - Under `refused` with `verdict = local-hook`, it was refused naming `peer-node, remote-ci`.
  - Stands in for `pre-push self-test` and `pre-push run-log line`.
- **AC3, live:** this pass commit carries the trailer, and `unchecked HEAD~1..HEAD` omits it.
- **AC5:** `off-node --backend local-hook` exits 1 naming `peer-node, remote-ci`. The `lander-refused` plant held 3 of 3, and `lander-peer` still holds 2 of 2.
- **AC6:** a copy of `check-pass-order.sh` over a planted history exits 1 under `refused`, 0 with a note under `allowed`, and 0 with the commit listed under `--preview`. The no-anchor case exits 0 and says so. Stands in for `pass-order history`.
- **AC7:** all three greps print lines, and the first one prints the key's `## ` heading.
- **Write-path parity:** `write_bypass_line` diffs identical between `tools/push-main.sh` and `.githooks/pre-push`.
- **Naming lexicon:** answered OK for all four names.

**Owed at the close:**
- Every leg on section 7's line.
- RED-first for the four `New arm:` lines. The arms are `BYP AC2`, `BYP S2` (the parity check) and `44` in `push-main.test.sh`; the three `BP` arms in `pre-push.test.sh`; `BYP` and its exit-table row (`bypass-refused`, 2 sites) in `pre-push.runlog.test.sh`; and the `unwitnessed` and `no anchor` arms in `check-pass-order.test.sh`.

**Possible reds at the bar, outside this unit's declared paths:**
- The `--shell-role` leg's ledger (`memory/project/shell-role.txt`) may red: it treats a grown shell file as a finding, and this unit grows `.githooks/pre-push`, `tools/push-main.sh`, `check-pass-order.sh`, `unattended.sh` and the four suites.
- `run-gates.gov.test.sh`'s list of plants does not include `lander-refused`; arm 44 runs it instead.
- Existing `pre-push.test.sh` arms that push with an R and have no memory-tree kit now get one extra stdout line: "hook-bypass walk did NOT run".
- The existing `check-pass-order.test.sh` fixtures already did not copy `commit_trailers.py`; this unit leaves that as it was, and the new arm's fixture does copy it.

**Branches with no test arm:**
- Under `refused`, the lander's "no registry answers" exit and its exit for an `off-node` refusal (exit 2).
- Under `refused`, the hook's "walk did not run" refusal.
- The leg's exit 2 when `unchecked` cannot read.

**Changes beyond the spec's wording:** both are recorded as `Decided:` trailers and in the ledger.
- A `lander-refused` fixture plant in `verdict_backends.py`, which arm 44 runs the same way arm 43 runs `lander-peer`.
- Under `refused`, the hook also refuses when the trailer reader does not resolve (deny by default). This sits inside the spec's two refusal sites.

**One stale citation in the spec:** S3 names `cmd_prepared` as the second caller of `check_push_allow`. The call is actually in the attended path at the top level of `push-main.sh`. The behaviour the spec describes (exit 4) still holds.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` ran. Two classes were acted on: the reader's stderr note being parsed as a commit (guarded by accepting only SHA-shaped lines, in both the hook and the leg), and a spawn idiom in the leg (replaced with a counter). `inherited-git-dir-pins-the-work-tree-to-the-cwd` was checked and the new code is clear of it. `refusal-branch-with-no-arm` is the list of branches above. No command hit its timeout.

Files are in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3:
- memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-2-1-acceptance-ledger.md
- tools/push-main.sh
- .githooks/pre-push
- tools/unattended/check-pass-order.sh
- tools/run-gates/verdict_backends.py
