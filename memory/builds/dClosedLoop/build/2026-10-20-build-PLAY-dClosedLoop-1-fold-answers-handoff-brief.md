# Fold answers handoff brief: the whole-design audit's fork-answer writers

**Serves:** research PLAY-dClosedLoop-1

A fork-answer writer's handoff renders its goal, items, acceptance, gates and non-goals from this brief record, through
`handoff.py render --input prompt=<this file>`. The six fold writers brought 35 forks to the owner. Two pairs were
merged, so the owner answered 33 questions on 2026-10-20. This pass folds the answers in two parallel halves, each
as one script that runs after the six fold scripts.

## The prompt

Fold the owner's answers to your half of the fold's forks, as one fold script.

## The brief

### Goal

Fold the owner's answer to each fork your brief (`input:spec`) assigns you into dClosedLoop's design records, as the
six fold scripts leave them, exactly as the owner chose, including where the owner chose an option that was not the
recommendation. Write every edit into one fold script in your scratch folder that runs after the six, and give each
new clause a placeholder id that the main loop's mint step numbers.

### Items

Each fork your brief assigns you, in its order, with the owner's answer.

### Acceptance

- Every assigned fork is folded as answered, or says what stops it, with its evidence from the folded records.
- The fold script applies after `fold-1.py` to `fold-6.py`: each `sub` and `insert_before` matches exactly once in
  the text those scripts leave.
- Each new clause ends with a placeholder id of your writer number, and no edit moves `[clause-ids]`' next id.
- An answer that needs a choice the owner did not make is a fork, unfolded.

### Gates

None of the bar's legs. You may run the build's dry run on your own folder, as your brief says, and report its
verdict.

### Non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or `WIRE-INTO-PROJECT.md`,
  and no `AGENTS.md` re-render.
- No unit specs for the chain builds, and no status change to an existing build or ask.
- No edit to the audit's own records: its reports, returns, briefs, the round record and the fold inventory.
- No edit to the six fold scripts or the build's instruments, and nothing read from, or written to, the sealed copy.
