# Session kickoff — orienting from a card, and resuming a routed build

The kickoff engine's `SKILL.md` points here in one line (TOOL-dPlacedRequest-34 S36), so the engine
stays within its size row. Everything below applies only when a card is in context; with none, the
engine's steps run in full.

## Step 1 from an `orientation —` card

With an `orientation —` card in context, Step 1's one call is `rev-parse HEAD`, plus fetch + ff when
the card's `tree —` cell reads the default branch and `clean`. While HEAD equals the cell's BASE, take
branch, BASE, dirty count, worktree count and recent subjects from the card, running no
`branch --show-current`, `status --short` or `worktree list`. A `now —` line (the replay's, never
stored) is fresh for HEAD, branch and dirty count: take them from it. A mismatch or no card → the
full call.

## Already oriented

A card whose last READY line is not `READY — none yet` is oriented (`kickoff.runs` at
`no-ready-card`, a stand-in dRankedPlan arms): re-orient from its `## task`, `## read`, `## records`,
`## classes`, `## open` and `## pockets`, then go to Step 5's hand-back, not re-running Steps 2 to 4.
No such card → the full kickoff.

## Step 2b's repair of a `## pockets` fact

In Step 2b's repair, a §B fact that is a level-2 unit the card prints under `## pockets` is repaired
by proposal, a stale one with `propose edit` and a missing one with
`instructions_edit.py propose add --manifest overlay`; the sub-sections that stay guide text are
fixed as Step 2b says.

## Resume

A replayed card whose `## route` names a build is first re-keyed from that build's card, then the
replay prints `route — re-checked · <verdict>`, a `resume —` line (resume.context) and
`partial — <n> uncommitted path(s) · resume.partial: <value>`. Take that value's act before any new
work. A re-check other than `ok` is a route that no longer holds: kick off again.

- `continue-item` keeps the work and continues the routed item, its witness still owed.
- `ask-owner` asks the owner what to do with the work, or, under a mandate, parks the item with the
  paths named.
- `restart-item` keeps the work on the side branch `partial/<slug>/<sid8>` (`<sid8>` the session id's
  first eight characters) and then restores the tree to `HEAD`, so nothing is lost. In this order,
  stopping at the first step that fails:
  1. `git add -A`, so untracked work is kept too.
  2. `c=$(git commit-tree "$(git write-tree)" -p HEAD -m "partial: <slug> <item>")`, the work as
     one commit on `HEAD`, leaving the branch and the tree where they are.
  3. `git branch partial/<slug>/<sid8> "$c"`; where that branch exists, the suffix `-2` instead
     (`partial/<slug>/<sid8>-2`, then `-3`), never a move of a branch another restart wrote.
  4. `git rev-parse --verify -q refs/heads/<that branch>` must print `$c`.
  5. Then restore only after that check prints `$c`: `git reset --hard HEAD`.

  A step that fails stops the act with the tree untouched and refuses naming the cause: the step,
  its command and what git printed.
