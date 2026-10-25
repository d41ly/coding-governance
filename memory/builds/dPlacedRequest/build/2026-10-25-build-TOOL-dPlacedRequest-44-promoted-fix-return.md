**Serves:** research TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49

# The promoted-fix pass — dPlacedRequest round 3, its return

The return of the gov-spec-writer dispatched from `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-8-spec-writer.md`, run direct/a9186d71a68ba310c, extracted from its transcript by script.

I fixed all 10 hits in the six specs and nothing else: no product code, no commit, no index render. The six edited specs are staged. `check-memory-hygiene.sh --only 2,12,25` now exits 0 with no hit on dPlacedRequest. I did not run `check-spec-tokens.py`; that is the main loop's to run.

The first time I ran the hygiene checks, my own new rev-2 log lines in 44–48 failed check 12 because they named no section. I changed their section field to `header above §1`, since there is no earlier example of logging a `**Derived:**` line edit. The second run was clean. If you want a different section token there, it's a one-word sed.

Each spec's rev went from rev-1 to rev-2 in its status header, with a matching §9 line.

| Hit | Spec | Disposition |
|---|---|---|
| [carries] unbound | TOOL-dPlacedRequest-44 | Fixed. `**Derived:** PLAY-dClosedLoop-2` sits at column 0 below the status header and its blank line, placed as in TOOL-dPlacedRequest-35 line 5. |
| [carries] unbound | TOOL-dPlacedRequest-45 | Fixed, same line. |
| [carries] unbound | TOOL-dPlacedRequest-46 | Fixed, same line. |
| [carries] unbound | TOOL-dPlacedRequest-47 | Fixed, same line. |
| [carries] unbound | TOOL-dPlacedRequest-48 | Fixed, same line. |
| [carries] unbound | TOOL-dPlacedRequest-49 | Fixed, same line. |
| [path] `help/loop.md` | TOOL-dPlacedRequest-49 AC17 | Fixed. The page doesn't exist yet; TOOL-dPlacedRequest-3 S7 creates it. AC17 now reads `` `grep -n 'follow-leases' loop.md` runs in `help/` ``, the form units 3, 6, 7 and 8 already use. The full path stays in S17 and §5. |
| [bar] `scratch-guard.test.sh` | TOOL-dPlacedRequest-49 AC16 | Fixed. AC16 now runs `readCard` directly, which `tools/hooks/scratch-guard.js:1615` exports. It sets `SCRATCH_GUARD_CARD_READ_BOUND_MS=500` over a stub checker that sleeps 30 s and expects no card within 2 s. The grep now names `tools/hooks/scratch-guard.js`. The suite stays on its §7 `New arm:` line. |
| [bar] `manifest-check.test.sh` | TOOL-dPlacedRequest-49 AC22 | Fixed. AC22 now runs `derive_claims_line` in a scratch tree with `.unattended.conf`, where the resolved `unattended.sh` is a stub that writes `boom` to stderr only and exits 1. That matches how `manifest-check.sh` finds its driver (`resolve_kit_file unattended unattended.sh`). The suite stays on its `New arm:` line. |
| check 12, failure mode, AC26 | TOOL-dPlacedRequest-49 | Fixed. AC26 already had a red case, but `Red` and `when:` were split across a line break. The check joins a criterion's lines and looks for the exact text `red when:` (`check-memory-hygiene.sh:1994`), so the split hid it. I moved `Red when:` onto one line; the wording is unchanged. |

Files edited, all under `C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\`:
- `2026-10-25-spec-TOOL-dPlacedRequest-44.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-45.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-46.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-47.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-48.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-49.md`
