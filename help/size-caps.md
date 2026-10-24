# The size caps, one switch: `budgets.enforce`

**What it is.** Many gates refuse a file for being too big: the charter template over 48 KiB, a
guide over its byte or line cap, a manifest line over 400 bytes, a role body over its slot's ceiling.
Every such cap now reads ONE switch in the policy file, `budgets.enforce`, and it **warns** by
default: a file over its cap prints a `BUDGET WARN` line and the gate passes. Set the switch to
`refuse` and every cap refuses as it used to. A cap you want refusing whatever the switch says goes
in `budgets.pinned`.

The caps are listed, one row each, in the census `tools/policy/caps.toml`: the name a cap goes by
under `budgets.*`, its class, its unit, the gate that measures it and where its value is declared
today. The policy kit's `budgets.py` answers every gate's question, so the switch and the pins live
in one place.

## How to use it

- **Keep the default.** With no `[budgets]` table, `budgets.enforce` is `warn`. A breach prints, for
  example:

  ```text
  BUDGET WARN — AGENTS.md · AGENTS.md · 20481 bytes over 20480 · budgets.enforce is warn
  ```

- **Make every cap refuse:**

  ```toml
  [budgets]
  enforce = "refuse"
  ```

- **Keep one cap refusing under `warn`:** name it in `budgets.pinned`, by its census name:

  ```toml
  [budgets]
  pinned = ["AGENTS.md", "manifest-line"]
  ```

  The refusal names the rule that set it, `budgets.pinned names it` or `budgets.enforce is refuse`.

- **Ask what a cap is:** `python tools/policy/budgets.py resolve AGENTS.md` prints one row,
  `<cap> <value> <mode> <source>`, tab-separated. `python tools/policy/budgets.py check AGENTS.md
  25000` prints the verdict line and exits 1 when it refuses. Both read the policy file **as
  committed at the landed revision**, as `policy.py get` does, never your working tree.

## Which caps sit outside the switch

A cap whose consumer drops what is over it, or a check of correctness, is no size budget, and the
switch never reaches it:

- **consumer limits** keep their own behaviour: the orientation card's 8192 bytes, Codex's 32 KiB of
  project instructions (announced by the agent-instructions adopter), a runlog record, a codebase-map
  feature card and a hook's 10000-character context.
- **correctness checks** keep refusing under `warn`: the template-size gate's checks 3, 5 and 6 (a
  record or a declared limit that is not a number, and a document whose own `**Budget:` line disagrees
  with its row), the spec-token checker's refusal of a limits row that is not a number, and the
  charter's cited files outside any cap.

`budgets.pinned` refuses a name outside the switch, and a name the census does not hold.

## Where each cap's value is declared today

No value moved: every cap keeps the value its home holds.

- **The template-size limits file**, `tools/template-size-limits.txt`, holds the charter template,
  `AGENTS.md`, the kickoff engine, the build method, the unattended protocol and Skill, and the class
  row for every live spec. `budgets.py` is its one reader, at the landed revision, so under `refuse`
  or a pin a raise lands before the growth it pays for.
- **`.memory-tree.conf`** holds the memory tree's guide, index, build README, dossier and entry caps
  and the universal-gotchas budget, each falling back to the hygiene engine's own default.
- **A declaration beside its gate** holds the line-length rows and the build README's slot ceilings.
- **A constant in the gate** holds the rest: role bodies, the one-line rule, the roster line, the
  manifest's caps and the recall export.

A cap can take a value from the policy file too, `budgets."AGENTS.md" = 21000` say, but a cap held
both there and in its legacy home refuses rather than picking one, and a family cap (line lengths,
README slots, role bodies, one value per subject) takes no value from the policy file at all.

## Without the policy kit

A gate that finds no policy kit beside it refuses every breach as it did before, and says once why.
