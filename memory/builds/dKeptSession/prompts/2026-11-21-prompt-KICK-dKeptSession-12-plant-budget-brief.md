**Serves:** research KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-26 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18

# Brief — dKeptSession: the plant-count class, checked across fifteen open specs

## The prompt

> /unattended dKeptSession

## The brief

### Goal

Unit 20's pass legs went red on the held-leg budget check because its spec did not anticipate it. The
`loop scenario fixtures` row in `tools/run-gates/selftest-budgets.txt` carries a `plants=<n>` token, and
`check_plant_tokens` grades it against the count the module's `PLANTS` holds once imported. Unit 20 added three
plants and did not list the budgets file, so the red was fixed in the red-fix lane. Earlier, unit 1 hit the same
red on the `loop factories fixtures` row. The writer of `2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief`
found the same gap in spec 13: it adds a `boundary` plant to `tools/loop/position.py` against a `plants=31` row.

A grep finds fifteen open specs that mention adding plants and never name `selftest-budgets.txt`: 12, 13, 14,
15, 26, 37, 38, 7, 35, 11, 52, 53, 17, 61 and 18. Some are false hits. Check each spec, and fix the ones the
class reaches.

### Items

1. F-plant-budget: for each spec, list every plant, case or fixture it adds to a module that a `selftest-budgets.txt` row prices with a `plants=<n>` token (read the rows and `check_plant_tokens` in `tools/run-gates/` for which rows carry one). Use the count each module holds at this tree, plus the plants the specs ordered before yours add (see the build README's gen:build-order). Where a unit moves a count:
   - `tools/run-gates/selftest-budgets.txt` joins Files touched;
   - the spec names the row, the token's old and new value, and how the ceiling is re-priced. The new plants' wall times are PINNED as estimates for the builder to read, with the leg's ceiling still clearing its evidenced maximum;
   - section 7's leg line carries `every held leg is budgeted, every budget row resolves`.
   Where a spec adds no plant to such a row, say so and leave it at its rev.
2. F-behaviour: run or read each changed criterion's command and confirm the exit and output it names. No `path:number` token stands unless it is a blob pin. Keep within the live-spec size cap, pin every figure, and leave no fork open; a fork you rule is marked `RESOLVED (agent, 2026-11-21, delegated): <option>, rung <n>; <reason>. widens: <value|none> · relaxes: <value|none>`.

### Acceptance

Each spec you changed is at a new rev, with one revision-log line that names this brief by its file stem.
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession <its id>` report nothing for each.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip, and no spec outside these fifteen. KICK-dKeptSession-32
is being built: read it, never write it.
