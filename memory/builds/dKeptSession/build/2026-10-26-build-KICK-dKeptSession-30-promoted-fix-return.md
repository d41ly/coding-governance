**Serves:** research KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-44

# The promoted-fix pass's return — dKeptSession

The writer's final return, extracted from its transcript by script, never retyped.

I fixed all 14 hits in place. `check-memory-hygiene.sh --only 2,12,25` exits 0 and reports no finding on any dKeptSession spec. Its only dKeptSession lines are check 25's "did not grade … READER NOT IN TREE" notes on specs 1, 2 and 3, which I did not touch. I did not run `check-spec-tokens.py`, since it is not a gate this role may run, so the main loop's re-run is the first real check of these fixes.

I changed only the hit lines, plus the rewrapping needed to keep the house line width. Every `**Derived:**` line, §3 edge and §8 mark is unchanged. All four files I edited are promoted specs, so they stay at the rev their header carries. KICK-28 is untouched, so its rev-2 §9 line was not extended. I committed nothing.

1. **KICK-dKeptSession-36, `[path]` ×2 (AC1, AC2).** Each `C:/Windows/System32/bash.exe` now reads "the Windows `System32` bash, the WSL launcher". AC1's red case and AC2's override probe still say the same thing. The §4 Evidence mention was not a hit and stays as it was.
2. **KICK-dKeptSession-40, `[path]` (AC1).** `tools/policy/policy.py` became `policy.py` "runs in the policy kit". The full path stays in §2, §4 and Files touched.
3. **KICK-dKeptSession-43, `[path]` (AC1).** The command is now `bash actions-free.fixture.sh --plant item-skipped` "runs in the hooks kit". I kept the `item — skipped: …` token on one line.
4. **KICK-dKeptSession-44, `[path]` ×7 (§6).** Each path is now a basename with its kit named in prose:
   - AC5 and AC7: `mail-notice.js`
   - AC8: `actions-free.fixture.sh`
   - AC18: `position.py`
   - AC34: `test -e context-fill.jsonl` "in the runlog kit's fixtures"
   - AC36: `presets.py`
   - AC14 no longer names `tools/loop/selftest.py`; see hit 5.

   AC36 also had `tools/loop/scenario.py`, which the checker never graded because its backtick span was split across a line break. I basenamed it to `scenario.py` and put the span back on one line.
5. **KICK-dKeptSession-44, `[bar]` (AC14).** AC14 now reads: "When a probe stubs `subprocess.run` and calls `position.py`'s `read_mail_interrupts` and `derive_parent_reach` over a fixture build, each recorded `argv[0]` is `resolve_bash()`'s path." §7 already has a `New arm: tools/loop/selftest.py` line covering AC14, so no new line was needed.
6. **KICK-dKeptSession-28 to 44, `[handoff]` `render_playbook.py --fleet-tags`.** KICK-44 does read this call: it is why S27 adds `playbook-render`. So I named the token in KICK-44's S27 rather than changing KICK-28's bullet: "…`requires` gains `playbook-render`, the kit `check_mail_recipient`'s `render_playbook.py --fleet-tags` call reads (`KICK-dKeptSession-28` S3)."
7. **KICK-dKeptSession-36 to 44, `[handoff]` `loop_lib.py`.** KICK-44's S16 now ends "…`KICK-dKeptSession-36`'s `resolve_bash`, imported from `loop_lib.py`."

Files changed:
- `C:\projects\coding-governance\.claude\worktrees\unattended-dkeptsession-dd0ede\memory\builds\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-36.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dkeptsession-dd0ede\memory\builds\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-40.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dkeptsession-dd0ede\memory\builds\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-43.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dkeptsession-dd0ede\memory\builds\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-44.md`
