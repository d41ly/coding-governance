**Serves:** research KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-44

# Promoted-fix brief — dKeptSession, the fourteen check-spec-tokens hits over the round-1 promotions

The round-1 spec audit (`unattended-build.js` run `wf_bb16c3ea-d12`, record
`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`) promoted
`KICK-dKeptSession-30` to `-44` and folded a hands-off edge to each into the roster specs. The main loop then ran
`tools/check-spec-tokens.py`: 14 unwaived hits, listed below. Hygiene checks 2, 12 and 25 are clean; keep them so.

Fix exactly these hits, in place, keeping every `**Derived:**` line, §3 edge and §8 mark as it stands. The promoted
specs are uncommitted, so they stay at the rev their header carries; a roster spec you edit is already at rev-2
from the disposal's fold, so add your change to that rev-2 §9 line rather than bumping again. Write nothing else,
commit nothing, and return each hit with what you changed. The spec brief,
`memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md`, still binds every rule;
its "What the last four spec runs had to fix" list is the remedy for each class below.

## The hits

1. `2026-10-26-spec-KICK-dKeptSession-36.md` · `[path]` ×2 · `C:/Windows/System32/bash.exe` reads as an untracked
   path. It names a machine binary, not a repository file: describe it without a path-shaped backticked token (for
   example, the Windows `System32` bash, the WSL launcher), keeping the observation it supports.
2. `2026-10-26-spec-KICK-dKeptSession-40.md` · `[path]` · `tools/policy/policy.py` in §6. Cite it by basename
   (`policy.py`) in §6, keeping the full path in §2, §4 and Files touched.
3. `2026-10-26-spec-KICK-dKeptSession-43.md` · `[path]` · `tools/hooks/actions-free.fixture.sh` in §6: basename it.
4. `2026-10-26-spec-KICK-dKeptSession-44.md` · `[path]` ×7 · `tools/unattended/mail-notice.js` (twice),
   `tools/hooks/actions-free.fixture.sh`, `tools/loop/selftest.py`, `tools/loop/position.py`,
   `tools/runlog/fixtures/context-fill.jsonl`, `tools/policy/presets.py` in §6: basename each.
5. `2026-10-26-spec-KICK-dKeptSession-44.md` · `[bar]` · an acceptance criterion names `tools/loop/selftest.py`, a
   suite. Observe the checker on a staged break or a fixture instead, and move the suite to a `New arm:` line in
   §7 if it gains an arm.
6. `2026-10-26-spec-KICK-dKeptSession-28.md` · `[handoff]` · its §3 hands `render_playbook.py --fleet-tags` to
   KICK-dKeptSession-44, whose spec never names it. Name the token where KICK-44 reads it, if it does; otherwise
   correct KICK-28's bullet to the token KICK-44 reads, keeping the pair reciprocal.
7. `2026-10-26-spec-KICK-dKeptSession-36.md` · `[handoff]` · its §3 hands `loop_lib.py` to KICK-dKeptSession-44, whose
   spec never names it: the same remedy as 6.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm it prints no finding on
a dKeptSession spec. The main loop re-runs `check-spec-tokens.py`.
