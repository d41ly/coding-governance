**Serves:** research TOOL-dQuietDisk-1

# Owner ruling — build on dWitnessedBar's prepared merge, land only after it lands

## The prompt

> Yes, build now

— owner, 2026-11-22, relayed by the parent session (the analysis session that started this run). The question put
to the owner was dQuietDisk's two options of 2026-11-22 00:00:
- (a) keep waiting for dWitnessedBar to land;
- (b) build on its prepared land branch now, and land only after it lands.

The parent recommended (b). It relayed the ruling as: "Build dQuietDisk on dWitnessedBar's prepared merge (f1af151e9,
or its current land tip). Do NOT land until dWitnessedBar has landed on main, then rebase or re-merge onto its
landing and run your bar there. If dWitnessedBar's red fixes collide with your units, record the conflict and
reconcile at your merge."

## How the run applies it

- **The build base.** The run branch merges dWitnessedBar's land tip, `branch/unattended-dwitnessedbar-2ed3b3` at
  `ed833f684`, which carries its prepared merge `f1af151e9` onto origin/main `c2a407b03`. That merge commit is the
  base every spec is re-grounded on and every before reading is taken at.
- **No landing before dWitnessedBar's.** The run does not move to VERIFYING, close or land until dWitnessedBar's
  landing merge is on main, which the registered `wait-dwitnessedbar-landing` task watches. It then re-merges main,
  so a red fix that collides with a unit is reconciled at that merge and recorded. The bar runs there.
- **The closing review reads this build's own diff.** Its round-1 base is the merge commit that brought
  dWitnessedBar in, not the run's pinned BASE `c95ef6216`. A range from BASE would hand the reviewers dWitnessedBar's
  commits, which its own closing review already read.
