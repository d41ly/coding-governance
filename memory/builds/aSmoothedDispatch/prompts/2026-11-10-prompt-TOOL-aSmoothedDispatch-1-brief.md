# Brief — aSmoothedDispatch: five mechanical refusals that cost every unattended run turns and re-dispatches

**Serves:** research TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6

## The prompt

> Can we analyze this build for any refusals/problems that have been costing it time and agent runs/reruns and build quick fixes? There are many more build runs in this set and so far they've been progressing painfully slow due to various mechanical obstacles.

— owner, 2026-11-09, after dFairHearing landed. The follow-up answer was "Yes, build 1–5".

## The brief

### Goal
Remove five refusals that the unattended driver and the scratch-guard hook raise on mechanically mis-shaped or out-of-scope input, so a run stops spending turns, spec rewrites and builder re-dispatches on them. Every refusal that guards a real defect keeps refusing.

### Items
1. `tools/unattended/unattended.sh`'s argument loop: `--writes` consumes every following argument up to the next one starting with `--`, and a value holding whitespace splits into its paths. Today `--writes a b c` declares `a` and refuses `b` with check 14 ("unknown argument"), and a quoted list refuses with check 49 (whitespace). [planned TOOL-aSmoothedDispatch-1]
2. `verb_dispatch`: a `--writes` path that is the run's own run-state file is dropped from the declaration with one printed note, instead of refusing with check 49. Every pass commit carries that file, and `--check-commit` already admits it. A path that only CONTAINS it, such as a directory, keeps refusing. [planned TOOL-aSmoothedDispatch-2]
3. `unattended.sh --help` and `-h` print the verb list the check 14 refusal already derives, plus a pointer to `memory/guides/UNATTENDED-VERBS.md`, and exit 0. [planned TOOL-aSmoothedDispatch-3]
4. `verb_dispatch`'s spec-token check, which runs `SPEC_TOKENS_CLI` over the whole live tree, refuses only on hits in the dispatching build's own specs. A hit in another build's spec prints a note and does not refuse, since the bar still grades the whole tree. A green result is cached under the git dir, keyed on a hash of every input the checker reads, and a dispatch whose key matches skips the run. The spec writer decides whether scoping needs a checker flag or a filter on its output. [planned TOOL-aSmoothedDispatch-4]
5. `tools/hooks/scratch-guard.js`'s "a role agent runs no gate" rule admits `gov-spec-writer` running `tools/check-spec-tokens.py` scoped to one spec, the one it wrote, and nothing else. This lets the writer find its own token misses before dispatch. It advances TOOL-dFairHearing-54. [planned TOOL-aSmoothedDispatch-5]
6. A builder's product write is not refused when the session card's `## route` names a CLOSED unit while the build's run-state file holds an open `--dispatch` row for another unit. Either `--dispatch` appends that unit's route to the card, or scratch-guard admits a unit with an open dispatch row. The spec writer picks the one that keeps one source. [planned TOOL-aSmoothedDispatch-6]

### Acceptance
1. A fixture `--dispatch <slug> --pass <id> --writes a b c` declares three paths, and `--writes "a b"` declares two. Before the fix each refuses (check 14, then check 49).
2. A fixture dispatch naming the run-state file in `--writes` succeeds with the note and declares the other paths. A directory containing the run-state file still refuses with check 49.
3. `unattended.sh --help` exits 0 and prints the verb list; before the fix it exits 1 with check 14.
4. A fixture with a token hit only in a foreign build's spec dispatches with a note, and a hit in the dispatching build's spec still refuses. A second dispatch with unchanged inputs skips the checker, which the fixture observes, and any change to an input re-runs it.
5. A `gov-spec-writer` Bash call running the spec-token checker over one spec is admitted. The same call with no scope, or any other gate, is still refused.
6. A fixture card routing a CLOSED unit, with an open dispatch row for an INPROGRESS unit, admits the builder's Edit on a product path. With no open dispatch row the Edit is refused as today.

### Gates
The touched kits' gate legs and self-test arms (unattended kit gate, unattended kit self-test, hooks scratch-guard self-test), spec tokens, memory hygiene, lexicon naming predicates, kit epoch, kit version markers; then the full bar once, at the landing.

### Non-goals
The `--close` bar and its fail-fast order; the role prompts for heredoc quoting, sleep polling or `/tmp`; the bar's own whole-tree spec-token leg, which stays whole-tree; asks TOOL-dFairHearing-52, -53, -55 and -56; any refusal guarding a real defect, such as paths overlapping siblings or a generated index declared with its generator.

### Limitations
Kit versions move through the lander's `mint`, not by hand. Unit agents run no gate legs; the main loop runs them after each pass. Units 1, 2, 3, 4 and 6 share `unattended.sh`, so they build one at a time.

### Reuse
- Unit 1 extends the `--writes)` arm of the argument loop (`DP_WRITES`), and unit 3 reuses `verb_list`, which check 14 already calls.
- Unit 4 wraps the existing `SPEC_TOKENS_CLI` call in `verb_dispatch`.
- Units 5 and 6 extend scratch-guard's role-gate allowlist and its route reader (`## route` lines).
- Recall returned TOOL-cMendedVintage-13 (the run-state file is append-only by class) and the dUnstalledConvoy lib-fix review (the run-state file rides every pass commit).

## Drawn from the session

> --dispatch refused 20 times on check 14 · --dispatch refused 12 times on check 49
— agent, the runlog model of dFairHearing, 2026-11-09

> BLOCKED by scratch-guard: this Edit targets …/tools/workflows/replay_scorer.py, a product path under ROUTED_PATHS entry `tools/` … and no unit its card … routes is buildable: TOOL-dFairHearing-12: Tier-2 at CLOSED
— agent, a dFairHearing builder transcript, 2026-11-03

## Owner confirmation

Asked: "Build fixes 1–5 as one new build, attended?"
Answer: "Yes, build 1–5"

Asked: "Should the fix build (slug aSmoothedDispatch, about 6 Tier-2 units in the unattended and hooks kits) declare `spec-audit:`? If yes, a spec reviewer audits every spec before any code is written."
Answer: "No audit"
