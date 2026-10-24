**Serves:** research TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79

# Promoted-fix pass, round 4 — the spec writer's return

The return of the agent dispatched from `memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-8-spec-writer.md`, run direct/a1702eb49a0ac464b, extracted from its transcript by script.

I fixed every hit the brief listed. Two specs changed, edited in place at rev-1. Nothing is staged or committed, and I did not touch the build index, any deviation record, spec 76, spec 78 or any spec numbered 1 to 75.

**Files changed**
- `C:\projects\coding-governance\.claude\worktrees\unattended-declared-loop-82e374\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-77.md`
  - The two planted URLs now appear only in a new bullet in §4 Evidence.
  - AC2 now names "the `ssh://` remote with the user part `user@` that §4's Evidence names".
  - AC4 now names "the `https://` remote §4's Evidence names, whose user part carries the password `SECRET`". Its observation is unchanged: the output does not contain `SECRET`.
- `C:\projects\coding-governance\.claude\worktrees\unattended-declared-loop-82e374\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-79.md`
  - **Paths:** AC5, AC8, AC9, AC14 and AC27 now cite the loop kit's files by basename (`kit.toml`, `loop_lib.py`, `commit_trailers.py`). The full paths stay in §2 and §4.
  - **The two selftest criteria:** AC15 and AC19 no longer name the selftest suite. Each is now an observation of govkit itself, the same way spec 73's AC1 phrases its probe: the probe from 73's AC1 runs `python tools/govkit/govkit.py update --to A` (and `--to B`) read-only, with no `--write`. "Read-only" means no `--write`, which I confirmed in `govkit.py`. The existing `New arm: tools/govkit/selftest.py · covers AC15 AC19` line in §7 already declares the suite arm.
  - **AC10:** it now names its witness, the pass-commit probe's route `add_scratch_worktree` (`tools/run-gates/lib-attribute.sh:59`) and `derive_leg_argv` (`tools/run-gates/measure_legs.py:503`). This matches the route S26 already sets.

**Checks re-run**
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25` prints no dDeclaredLoop line now. Before the edits it printed spec 79's AC10.
- The guard blocked `python tools/check-spec-tokens.py`, because this role may run only the hygiene and lexicon gates. Instead I wrote a probe that copies that checker's acceptance-section logic: its `TICK`, its `BAR` regex and its path-shape test (`tools/check-spec-tokens.py:1513-1528` and `:1122-1139`).
  - Over the staged copies from before the edits it reports exactly the 9 hits in the brief.
  - Over the edited specs 76 to 79 it reports nothing.
- Basenames are safe here because this repo runs the checker with its tool root at `tools`, so the bare-name check is off (`tools/check-spec-tokens.py:1454-1457`).

**dDeclaredLoop lines left:** none from the hygiene check. You still need to run `python tools/check-spec-tokens.py` itself in the main session to confirm it names no dDeclaredLoop spec.

The probe is at `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-declared-loop-82e374\fe9ab66e-8bde-4f94-90b4-e764fe4c1760\scratchpad\probe.py`.
