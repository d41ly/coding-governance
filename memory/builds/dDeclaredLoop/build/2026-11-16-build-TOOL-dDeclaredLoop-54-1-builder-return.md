**Serves:** journal TOOL-dDeclaredLoop-54

# Builder return — TOOL-dDeclaredLoop-54, dispatch 1: its forks carry no resolution mark, AC3 reads the plants' exit contract unit 33 did not build, and the per-level fill sits where no plant reaches it

## Why

DIVERGENCE: three spec defects, found by the pre-write sweep of memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-54.md (rev-3) against HEAD 685e21957. The first one blocks the commit outright.

(1) Section 8: F3, F4 and F5 carry no resolution mark. Each ends with "Recommendation (a); the spec body is written on it." and nothing more. The spec is dated 2026-10-24, which is on or after FORK_ITEM_CUTOFF 2026-09-30 in .memory-tree.conf, so hygiene check 12 grades each F-item on its own. The function check_span_mark in tools/memory-tree/check-memory-hygiene.sh finds no `RESOLVED (agent|owner, <date>[, delegated])` in those three spans. The pre-commit hook's staged hygiene leg would therefore refuse the CLOSED commit with "§8 F-items carrying no conforming resolution mark ...: F3, F4, F5". The task says these forks are marked; they are not. Only F1 and F2 carry marks. Fix: each of F3 to F5 needs a mark such as `RESOLVED (agent, 2026-11-16, delegated): (a)` with its widens/relaxes line. The header also needs the `ratified <date>` pointer the template asks for.

(2) AC3 and §4 "The termination rule" use the exit-code contract of unit 33's rev-6. The built module uses a different one. In unit 33's built termination.py, `--fixture --plant <case>` exits 0 when the plant holds and 1 when it is MISSED. The inner check's exit is printed as a line, `loop: fixture · <case> · check exit 1`. I probed it: `python termination.py --fixture --plant dead-end` printed the finding `terminal · build stuck`, then `check exit 1`, then `held`, and exited 0. So "`python termination.py --fixture --plant unit-dead-end` exits 1" as written would observe a missed plant. AC3 has to say: exits 0, ending `loop: fixture · unit-dead-end · held`, after a `check exit 1` line and a `terminal` finding naming `unit reviewed`.

(3) S4 and §4 put the per-level fill in `read_termination_inputs`. In the built module, the composition's `terminal` is built in `derive_termination_composition`, as `{"build": list(tables["terminal"])}`. Both `read_termination_inputs` and every in-memory plant call that function. The plants include dead-end, and the new unit-dead-end would too. A fill in `read_termination_inputs` would never reach the unit-dead-end plant, so AC3 could not hold. S4 should name `derive_termination_composition` as the place that calls `read_terminal_set` for each level of `tables["states"]`. While revising, S5 or S4 could also name termination.py's own docstring as a carrier. Three passages there say the feature and unit levels print unchecked: THE RULES `terminal` paragraph, the `check` paragraph ("each unchecked level"), and WHAT THIS DOES NOT CHECK ("until TOOL-dDeclaredLoop-54 declares their sets"). `derive_unchecked_levels` and the dead-end plant's expectation `derive_unchecked_levels(composition) == ["feature", "unit"]` both go under S4.

Everything else in the sweep still holds at HEAD. `read_transition_rows`, `check_transition_tables` (which compares the written `from` against the build's terminal at every level), `derive_from_states`, `PLANTS` and `write_table_plant` read as the spec cites them. No feature or unit row uses `@open`. VERB_OFFENDER_PIN is 1215. `lexicon.py --suggest read_terminal_set --as py.function` prints OK. REFUSAL_CEILINGS holds unattended.sh at 343. No path in the files-touched list is on SESSION-KICKOFF.md's watch line. No product file was written, so there is no patch to save. The worktree is clean at base.

## Summary

I did not build or commit anything. The spec has three defects, so I'm returning a divergence; the details are in `why`. The worktree is clean at base 685e219575327e914d9e9c510fe5964d54b67a32.

**Checks that ran (all read-only):**
- I read the spec, the brief and the build method in full, and compared the spec's claims with tools/loop/loop_table.py, tools/loop/termination.py, tools/loop/loop.toml, help/loop.md and tools/loop/README.md at HEAD. This stands in for the spec-tokens and sweep part of the memory hygiene gate.
- I read the per-fork reading rule in check 12 (check_span_mark in tools/memory-tree/check-memory-hygiene.sh) without running the script. It stands in for the hygiene check that would refuse the CLOSED commit.
- `python tools/lexicon/lexicon.py --suggest read_terminal_set --as py.function` printed OK. This stands in for the lexicon naming leg.
- One probe of the built module: `python termination.py --fixture --plant dead-end` exited 0, ending with `held`. That shows AC3's expected exit 1 contradicts how the module's plants report.

**What the spec needs (rev-4):**
- F3, F4 and F5 need resolution marks.
- AC3 needs the exit contract the built plants use.
- S4 should place the per-level fill in `derive_termination_composition`.

**Not done:**
- I did not run `--brief` to record the brief, because it writes a build record and this pass commits nothing. The next dispatch should record it.
- I did not run `gotchas.py --for-diff`, because there is no commit to check.
- No new test arms were added, so none is owed at the close.
