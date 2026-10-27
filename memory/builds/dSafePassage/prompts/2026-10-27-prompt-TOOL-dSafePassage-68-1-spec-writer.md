**Serves:** research TOOL-dSafePassage-68

# Brief: the upgrade-walk leg's stand-in step runner stops drifting from the function it replaces

## The prompt

No owner prompt. After TOOL-dSafePassage-40, the build run's main loop ran `python tools/govkit/upgrade_walk.py --case kill --step lib/python-floor-3.15`, which no unit pass may run. It exited 2. The run adopts the fix under M10.

## The brief

### Goal

Every child walk the upgrade-walk leg spawns runs `update` to completion again. The leg's stand-in for `upgrade_steps.run_step_isolated` accepts and forwards whatever the real function accepts, so a later parameter added to the real one cannot break the leg silently again.

**What was measured** at HEAD `6055cdf18`. The child walk's `update` dies at the first step witness with `TypeError: run() takes 4 positional arguments but 5 were given`, raised from `run_step_reread` (`tools/govkit/upgrade_steps.py:1298`), which calls `run_step_isolated(row, phase, target, gov_root, to)`. TOOL-dSafePassage-26 (dfcef45a7) gave `run_step_isolated` a fifth parameter, `to: str | None = None` (`:1096`), for its `{to}` placeholder. The leg's child script, embedded in `tools/govkit/upgrade_walk.py` at about `:340-397`, swaps in `def run(row, phase, target, gov_root)` and calls `real_run(row, phase, target, gov_root)`. So every case's `up` walk fails, which means `up`, `down`, `reup`, `plants`, `skip`, `fail` and `kill` all fail. The leg reports only `exit 1`, because the traceback comes before any `govkit: N problem(s)` line. The probe script and its log are `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/probe_up40.py` and `probe_up40.log`.

### Items

1. **Author `memory/builds/dSafePassage/spec/2026-10-27-spec-TOOL-dSafePassage-68.md`** as a Tier-2 micro-spec with these properties:
   - status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 7`, `**Derived:** TOOL-dSafePassage-26`;
   - `consumes-from` TOOL-dSafePassage-5 and -26.
   
   Its scope has two parts:
   - (a) The stand-in forwards the real signature, by `*args, **kwargs` pass-through or by an explicit `to` parameter. Decide from the code and say why.
   - (b) The class gets gated so the next signature change reds a cheap check instead of the hour-long leg. For example, the leg's selftest compares the stand-in's parameters with `inspect.signature(upgrade_steps.run_step_isolated)`, or calls the stand-in with the real function's full parameter list.
   
   Also decide whether the leg should print the child's last lines when a walk exits with no count line. The leg would then have named this traceback instead of `exit 1`. A choice you cannot derive from the code is a fork in §8, with your recommendation. Its acceptance criteria must be observable without running the whole leg: a selftest-arm probe or `python -c`. Each criterion needs a Red-when and a `New arm:` line.
2. **Add its row** to the README's authored `roster:units` table.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- The spec is conforming: status header, `**Derived:**` line, §6 with a Red-when, §7 with a `New arm:` line, and §10 reuse naming the child script as the seam.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, and no edit to a CLOSED spec.
- No commit and no stage into the real index.
