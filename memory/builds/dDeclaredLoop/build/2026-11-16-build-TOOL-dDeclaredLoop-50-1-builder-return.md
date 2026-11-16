**Serves:** journal TOOL-dDeclaredLoop-50

# Builder return — TOOL-dDeclaredLoop-50, dispatch 1: units 20 and 50 each leave the four review rows' outcomes, routes, witness and owner to the other

## Why

DIVERGENCE: the spec does not say what the four rows from unit 20 hold, and the two specs point at each other for it. Spec 50 §2 S1 and §4 "The rows" set the needs, outcomes, witnesses and routes of item.review.trigger, item.review.dispose, item.review.fold and item.review.cost to "as unit 20" / "stay as TOOL-dDeclaredLoop-20 §4 gives them". Unit 20 is CLOSED (rev-5) and wrote no row (its §8 F4). Its §4 "The item rows" says the opposite: unit 50 "sets the outcome words and route targets check_program and the build table's route join admit". Unit 20's table gives only needs, a witness `by` and routes in prose. So no spec names the outcome lists, the route targets, the witness class, or the owner of trigger, fold and cost. I cannot build the rows from what the spec says. Several of unit 20's routes have no target the checks admit without a design choice. `check_program` takes only a declared item, `transition`, or `stand-in:{prefix}/<home>/<file>`. In `tools/loop/loop_table.py#check_transition_tables`, a `transition` target, or a declared item on another step, is a cross-step route. Such a route is refused unless a build row or an `[[owed-row]]` covers it. The routes in question: trigger's "not fired, the flow continues"; cost's "done"; fold's "released" and its BOUNDED/CEILING promotion; dispose's "a plan revision to plan.record" (item.plan.record is on step.plan, so that route is cross-step); dispose's landing-record patch-build intakes, ask and unverified-finding routes. Declaring the dispose row also changes how build row B10 is checked: today B10 (item.review.dispose · unit → designing) passes through the dispose `[[stand-in]]` row. Once the item is declared, it passes only if dispose routes the outcome `unit` to `transition`. §5 says B10 is unit 20's to keep true, but unit 20 wrote no row. What the spec would have to say: in §4 "The rows", for each of the four rows, the `outcomes` list; the `routes` table with each target a declared review tag, `transition` or a named `stand-in:{prefix}/...`; the witness `{ class, by }`; and the `owner` (dispose's must stay dDeclaredLoop to match its stand-in row). In §5, either a statement that dispose's `unit = "transition"` is the only cross-step route and B10 covers it, or any build or `[[owed-row]]` rows the other routes need, with those rows in Files touched. The rest of the sweep at 250b236fe holds; the summary has the detail. Nothing was written or committed and the tree is clean, so there is no patch to save.

## Summary

I built nothing and committed nothing: the spec leaves out outcomes, routes, witness class and owner for four of the six review rows (details in `why`). No product file was edited, the worktree is clean at base 250b236fe, and there is no patch file. I did not run `--dispatch` or `--brief` and changed nothing in RUN.md. RUN.md already has the brief row for C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/builds/dDeclaredLoop/prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-50-build-brief.md (its 12:10Z brief row).

Checks run: read-only probes of the tree at HEAD. They stand in for no gate, and none of the spec's §7 gates or new arms were run.

The rest of the spec's sweep held when re-run at HEAD:
- The command-row count prints `61 40 40`, as the spec says.
- `NO_STEP` is `none`.
- `check_program` has the tag branches, refusal text and return shape the spec describes.
- `ACTOR_FORM` and `ACTOR_KINDS` match the spec's actor grammar.
- Only `main` reads `check_program`'s return. The other callers ignore it: `read_items`, `tools/loop/loop_items.py` (two calls) and `tools/loop/splice.py`.
- `help/loop.md` has the "Read the loop" item with usage anchor 8a025e56, a `loop: program` example line, and a "See a refusal" item.
- `tools/loop/README.md` has the "The item programs" section and the `check_program` paragraph.
- The lexicon pin is still 1215.
- `load_sets.py derive --item` does not depend on an item's step, so `--scopes` will accept a step-none row.
- No `[[checklist]]` row names an `item.review` tag.

One thing the spec does not mention: declaring item.review.dispose makes `tools/loop/loop_table.py#check_transition_tables` check build row B10 against dispose's routes, so dispose must route the outcome `unit` to `transition`.

What the next pass owes once the spec is revised:
- The §7 legs at the close.
- The new arm's RED-first observation: the `step-none-outside-review` and `review-step-named` plants in `tools/loop/loop_lib.py`.
