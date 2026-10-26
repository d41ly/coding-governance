**Serves:** research TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30

# Round-1 fix pass — dFurnishedOrders, its return

The return of the agent dispatched from `memory/builds/dFurnishedOrders/prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-2-spec-writer.md`, run direct/a47c26fcfc4ae866f, extracted from its transcript by script.

I fixed all four findings in two spec files. Both units stay `rev-1` with no §9 line, as the brief says. Nothing is committed and no index was rendered. The spec-token check was not run: scratch-guard blocks it for this role, so it still needs the main loop's run on the real tree.

**R1: suites named as acceptance observations (`[bar]`)**

- **`TOOL-dFurnishedOrders-29`, AC6.** The two suite paths that sat alone in backticks are gone. AC6 now observes S8's recipe directly in a scratch fixture:
  - Make a repo with `git init -b main` and commit a `.governance/policy.toml` holding `bypass = "never"` under `[core]`.
  - `policy.resolve("core.bypass", <scratch>)` should answer `never` with source `file`.
  - The same file in a repo with no commit should raise `Refusal`.
  - That rests on `tools/policy/policy.py`: `resolve` at :752, `derive_landed_revision` at :472, and the `Resolution` source field at :199.
  - The suite check is now a single grep, `grep -n "init -b main" tools/runlog/selftest.py tools/roles/adopt-roles.test.sh`, which the checker reads as a probe, not a run.
  - In §7, AC6 joins the covers of the `tools/roles/adopt-roles.test.sh` arm (the policy fixtures of units 11, 12 and 17) and of the `tools/runlog/selftest.py` arm (unit 3's fixture). Each arm's staged break now includes leaving a fixture's policy file uncommitted. I took that split from each unit's own `New arm:` lines.
- **`TOOL-dFurnishedOrders-30`, AC3.** S4's own code is the two suites' assertion text, so AC3 still reads them, but never runs them. Both observations are now single `git grep -n … -- <suite>` probe commands, so no suite path stands alone as a token. The `tools/workflows/unattended-build.test.sh` `New arm:` line stays as it was. I did not add AC3 to its covers, because S4 says both suites stay WAIVED by the build README's rule (README.md:51) and their arms are owed to PLAY-dClosedLoop-18.

**R2: hand-off token (`[handoff]`)**

- **`TOOL-dFurnishedOrders-29`, S24** now names "unit 4's `gotchas.py --for-names` lookup" among the slot subprocesses it bounds. That matches unit 4's hands-off bullet, and unit 4 is unedited.

**Checks I ran**

- **Bar tokens.** The checker's `BAR` regex, copied into a scratch probe and run over the acceptance bullets:
  - Before the fix (index text), it flagged `tools/runlog/selftest.py` and `tools/roles/adopt-roles.test.sh` in unit 29 and `tools/workflows/unattended-build.test.sh` in unit 30, and `--for-names` was absent from unit 29. That is the four findings.
  - After the fix, units 29, 30 and 4 print no bar token.
- **Paths.** Every path the new criteria name is tracked.
- **Hygiene checks 2, 12 and 25.** Run with `--only 2,12,25` in a throwaway clone with every spec of the folder committed: `HYGIENE --only 2,12,25 ran checks 2 12 25`, exit 0, advisory lines only. I deleted the clone afterwards.

Files are in C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec:
- 2026-10-26-spec-TOOL-dFurnishedOrders-29.md
- 2026-10-26-spec-TOOL-dFurnishedOrders-30.md
