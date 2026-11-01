# TOOL-dEasedEffort-1 — acceptance ledger

**Serves:** journal TOOL-dEasedEffort-1

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran, from the worktree
root: the `load_policy` probe AC1 names, `handoff.py stage-efforts` for the four workflows, and the
greps AC4 and AC5 name, each before the edit and again after it. The run before the edit printed the
spec's "Today" column, and the AC4 grep printed `tools/roles/README.md:184`, so each criterion was
seen on its failing side first.

AC3 is the main loop's, after this pass (the spec's Rollout step 2), and its line lands with the
render. A read-only probe of the resolved levels against the `effort:` lines under `.claude/agents/`
named `gov-builder`, `gov-diff-reviewer`, `gov-orienter` and `gov-skeptic` as lagging and the other
five as current, which is the four-line move that render owes. Owed to the main loop at the close
(M8): every leg the spec's section 7 lists. The spec declares no `New arm:`, so no RED-first
observation is owed.

**Evidences:** TOOL-dEasedEffort-1
- AC1 — `load_policy` — the probe printed `gov-builder=high gov-diff-reviewer=medium gov-orienter=high gov-researcher=medium gov-reuse-scout=medium gov-skeptic=medium gov-spec-reviewer=medium gov-spec-writer=high gov-synthesizer=high`, so R12 raised nothing, and `git diff --cached --numstat 2a6f3975` over the staged `tools/roles/house/policy.toml` printed 4 added and 4 deleted.
- AC2 — `{"builder":"high"}` — `stage-efforts build` printed `{"builder":"high"}`, `spec-write` printed `{"builder":"high","disposal":"high","skeptic":"medium","specFinder":"medium","specWriter":"high","synthesis":"medium"}`, `spec-review` printed `{"skeptic":"medium","specFinder":"medium","synthesis":"medium"}`, and `closing-review` printed `{"diffFinder":"medium","skeptic":"medium","synthesis":"high"}`.
- AC4 — `tools/roles/README.md:184` — the `git grep` printed that line before the edit and nothing after it, exit 1, over `help` and `tools/roles/README.md`.
- AC5 — `handoff.py stage-efforts` — the `grep -c` printed `1`, and that command's output gives `synthesis` the level `medium` in `spec-review` and `high` in `closing-review`, the two levels the sentence states.
