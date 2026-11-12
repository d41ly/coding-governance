# PLAY-dOrderedCharter-87 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-87

Each line is a probe this pass ran at rev-1 of the spec, over a throwaway clone of `585277aed` with the pass
committed on it, the clone keeping its history, a local `main` at `origin/main` and `origin/HEAD` set to `main`.
The worktree's three product files are byte-identical to the probed ones (PINNED, `cmp` of each). No leg, suite or
bar ran in the pass: where a line says "owed" the main loop observes it after every unit is terminal. AC1 called the
leg's own entry, `run_check` in `tools/playbook/instructions_edit.py`, from a probe, as the spec's evidence did.

**Evidences:** PLAY-dOrderedCharter-87
- AC1 — `instructions-edit: check · 0 red` — after `up .` over the pass, `run_check` returned exit 0, no line opening `instruction-units: red`, and ended `instructions-edit: check · 13 row(s)` then `instructions-edit: check · 0 red`; over the base clone the same probe returned exit 1 with 18 such lines (PINNED, that probe run, both trees). The leg itself is owed: the main loop runs it.
- AC2 — `ADOPTER_RULES` — with AC1's `up` committed, `render_playbook.py --render-scope charter` exited 0, its notes held `units     ADOPTER_RULES — no [charter] adopter_rules · 9 level-0 unit(s) after it`, and `git diff --exit-code -- AGENTS.md` exited 0, the blob `30520e73945057365a62c810c7b97d355485e3b0` before and after; the lock moved in line endings only, 0 content lines under `--ignore-cr-at-eol` (PINNED, that probe run).
- AC3 — `repo.rule-01-fx` — `instruction_units.py fixture --plant statements` exited 0 printing `instruction-units:   ok · a well-formed adopter-rule (repo.rule-01-fx) passes` and `instruction-units: fixture · green · 0 expectation(s) failed` (PINNED, that plant run).
- AC4 — `unit.carried` — `instruction_units.py fixture --plant schema` exited 0 with an `ok` line holding `unit.carried reds naming the manifest` and the field `type`, and the green line; with S2's three lines removed it exited 1, the row `FAILED` over `schema · 2 row(s) · 0 red` (PINNED, both plant runs). The arm's RED-first observation at the close is still the main loop's, per the spec's `New arm:` line.
- AC5 — `adopter-rules: witness` — after `up .`, `witness .` exited 0 printing `adopter-rules: witness · no [charter] adopter_rules, and each of its 9 rule(s) is a unit: applied`; `down .` printed `adopter-rules: down · restored .governance/deploy.toml, .governance/instructions.toml`, and `git status --porcelain` printed nothing (PINNED, that probe run).
- AC6 — `carries no text` — with the line `-   ` added to the key, `up .` exited 1 printing `adopter-rules: up refused · the converted rows break the instruction-unit grammar:` and a line naming `carries no text`, and `git status --porcelain` listed only ` M .governance/deploy.toml`; over the base clone the same edit made `up .` exit 0 writing ten rows (PINNED, that probe run, both trees).
- AC7 — `adopter-rule` — the paragraph sits in `help/overlay.md` under "Add a unit", after its example row (PINNED, the pass's diff). The `docs` leg is owed.

**Owed to the close.** Every leg of the spec's Gates section, the `New arm:` line's RED-first observation, and the `--prepare` re-run the spec hands off. The codebase map generator's `--write` over the pass clone moved no file (PINNED, `git status` after it).
