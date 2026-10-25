**Serves:** research TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75

# Promoted-fix pass, round 3 — the spec writer's return

The return of the agent dispatched from `memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-7-spec-writer.md`, run direct/a3a804974307f2aaa, extracted from its transcript by script.

All eight round-3 promotions are fixed. The memory hygiene check (`--only 12,25`) now prints no dDeclaredLoop line. I couldn't run `python tools/check-spec-tokens.py`: scratch-guard blocks that gate for this role, so the main session needs to run it.

In its place I wrote a local probe that copies the checker's leg-line and path rules from `tools/check-spec-tokens.py`. On the staged originals it reports exactly the 21 token hits in the brief. On the edited files it reports none.

**Files changed** (edited in place, no rev bump, nothing staged or committed, no deviation record and no spec 1–67 touched). All five are in `C:\projects\coding-governance\.claude\worktrees\unattended-declared-loop-82e374\memory\builds\dDeclaredLoop\spec\`:

- **`2026-10-24-spec-TOOL-dDeclaredLoop-68.md`**
  - **AC2:** cites `loop_witness.py` by basename, run in `tools/loop/`.
- **`2026-10-24-spec-TOOL-dDeclaredLoop-71.md`**
  - **AC1:** splits the grep into two. `tools/gate-legs.json` stays a full path; `kit.toml` is run in `tools/loop/`. The argv now reads `python breakpoints.py --fixture` under `{prefix}/loop/`.
  - **AC2:** the fixture runs in a scratch copy of `tools/loop/`.
  - **AC3:** the tracked meta files keep their full paths, and `loop.md` is grepped in `memory/map/features/`.
- **`2026-10-24-spec-TOOL-dDeclaredLoop-72.md`**
  - **AC4:** `budget.py breakpoints.py` run in `tools/loop/`.
- **`2026-10-24-spec-TOOL-dDeclaredLoop-74.md`**
  - **S1:** it retires nothing (it describes how a remote URL is normalised), so I reworded "are removed from both" to "once each is stripped of a trailing `/` and a trailing `.git`". It no longer reads as a retirement and needs no `**Readers:**` clause.
- **`2026-10-24-spec-TOOL-dDeclaredLoop-75.md`**
  - **AC3, AC11, AC17, AC32, AC33, AC35:** loop-kit files cited by basename, run in `tools/loop/`.
  - **AC14:** now reads: the install receipt `install.json` equals its copy committed at `HEAD`, read by `git show`, and `test -e .update.lock` run in the target's `.governance/outbox/` exits 1.
  - **AC21:** the `loop.md` grep is split out and run in `memory/map/features/`.
  - **AC22 (check 12):** now names the witness `git worktree add --detach`, in the same shape as AC10.
  - **§7 leg hits:** none of the four flagged names was on the leg line. They sat in a prose paragraph about legs that sibling units mint, and line wrapping had left one line made only of backticked names, which the checker reads as a leg line. I rewrapped it so no line is backticked names alone, and added that each leg is declared by the unit that mints it and that none is a leg at HEAD (I checked `tools/gate-legs.json`: it has no `loop` legs).
  - **Choice to confirm:** I did not add `New arm:` lines for these legs, because they belong to their minting units' specs, not unit 75.

**dDeclaredLoop lines left:** none from the hygiene check. For the token checker, the probe says none, pending the main session's real run.

The probe scripts are `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-declared-loop-82e374\fe9ab66e-8bde-4f94-90b4-e764fe4c1760\scratchpad\probe.py` (edited files) and `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-declared-loop-82e374\fe9ab66e-8bde-4f94-90b4-e764fe4c1760\scratchpad\probe_staged.py` (staged originals).
