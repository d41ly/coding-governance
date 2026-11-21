**Serves:** research TOOL-dPlacedRequest-100

# Owner ruling — the landing merge takes the protected skill files through a plain git merge

## The prompt

> Yes, merge it

— owner, 2026-11-21, answering the run's hand-off under `owner-decision`, whose parked decision
`landing-merge-protected-skills` asked whether the landing merge of `origin/main` may take the sandbox-protected
`.claude/skills/lexicon/SKILL.md` and `.claude/skills/unattended/SKILL.md` through a plain `git merge`.

## How the run applies it

- The run merges `origin/main` into its branch with `git merge`, resolves the conflicts the merge leaves, and goes on to
  the prepare, the flagged bar and the close.
- The ruling covers this landing's merge alone; a later merge touching protected skill files asks again.
