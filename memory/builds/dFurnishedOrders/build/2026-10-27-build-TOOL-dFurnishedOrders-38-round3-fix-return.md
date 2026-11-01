**Serves:** research TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42

# Round-3 fix pass — dFurnishedOrders, its return

The return of the agent dispatched from `memory/builds/dFurnishedOrders/prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-1-3-spec-writer.md`, run direct/a023e847a1e89f139, extracted from its transcript by script.

I fixed the path and suite-name lines in units 39, 40, 41 and 42. I could not run `python tools/check-spec-tokens.py` myself: scratch-guard blocks that gate for my role. So nothing yet confirms the checker is quiet, and you need to re-run it on the real tree.

**What I could check instead:**
- **A probe of my own.** It uses the checker's own rules, copied: it reads only the bullets in each acceptance-criteria section and the leg lines in each gates section (`tools/check-spec-tokens.py:1510-1588`). Before my edits it found 31 of your 32 lines. After them it finds none on units 38 to 42. The 32nd line is something my probe does not model. I also ran the checker's line-number check for `path:line` citations over these specs and it found nothing.
- **Hygiene checks 2, 12 and 25** pass (exit 0) in a throwaway clone. They failed at first only because the clone lacked the staged review file. The final run had the whole `dFurnishedOrders` folder and `memory/LIVE.md` committed.

**What changed** (acceptance sections, plus the matching prose in 40 §1 and 42 S11):
- **Unit 39:** AC1 and AC3 now name the new file by its basename, as "the canonical run_bounded.py S1 creates". The full path stays in §2, §4 and Files touched.
- **Unit 40:** the fixture suites (run.test.sh, mine.test.sh in two places) and the receipt's drift-audit-code.js path are now described in words, not backticked paths. That covers §1 and AC1 to AC3.
- **Unit 41:**
  - AC1 and AC2 run "the step, retired_dispatch_args.py at S1's path".
  - Fixture files in AC3, AC5 and AC6 are now written under `<target>/…`, a placeholder the specs already use and the checker skips.
  - Suite-named fixtures in AC3 and AC5 are described in words: x.test.sh, mine.test.sh, selftest.py and the copied pre-push runlog suite.
- **Unit 42:**
  - The payload path `memory/notes/x.md` in AC7 (and S11 to match) became "a note x.md under `memory/notes/`".
  - `tools/roles/role-schema.toml` in AC8 became the basename `role-schema.toml`, because TOOL-dBoundRoles-2 creates that file. The full path stays in S13.

**Two things that differ from the brief:**
- **The placeholder does not clear a suite name.** R2 says the placeholder spelling fixes a fixture's suite name, but it doesn't for `*.test.sh` or `*selftest.py` names. The checker's suite pattern (`tools/check-spec-tokens.py:390-395`) allows any directory in front of the name, so `<target>/scripts/run.test.sh` is still flagged. Every fixture with a suite name is therefore described in words.
- **No `New arm:` lines changed.** None of these criteria actually ran a real suite; each named a file inside a scratch fixture. The existing arms in §7 of 39, 40 and 41 already cover the affected criteria.

All four specs stay `rev-1` with no §9 line, and unit 38 is untouched. I committed nothing and edited nothing outside the spec folder.

Edited files:
- C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-39.md
- C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-40.md
- C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-41.md
- C:\projects\coding-governance\.claude\worktrees\unattended-furnished-orders-b4ef78\memory\builds\dFurnishedOrders\spec\2026-10-27-spec-TOOL-dFurnishedOrders-42.md

My probe script: C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-furnished-orders-b4ef78\56bbd6e7-78b5-422f-b186-74bf31f37f19\scratchpad\probe.py
