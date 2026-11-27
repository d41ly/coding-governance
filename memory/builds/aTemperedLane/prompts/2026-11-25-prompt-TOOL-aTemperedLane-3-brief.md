# Brief — aTemperedLane: the closing review's medium and low items, one batch

**Serves:** research TOOL-aTemperedLane-3
**Caused-by:** TOOL-aTemperedLane-3

## The prompt

> No words of the owner's ask for this unit: it is the closing review's exit (`doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`). The
> review is `memory/builds/aTemperedLane/reviews/2026-11-25-review-TOOL-aTemperedLane-1-closing-diff-review-round1.md`.

## The brief

### Goal
Close the review's five items M1, M2, M3, L1 and L2: one false claim corrected and pinned, and four
coverage gaps given their arms. No verdict of `routed_commits.py` changes.

### Items
1. M1: keep the code. A guarded list absent from the working tree, deleted by the fix commit or by
   any later one, leaves only the `.governance/` prefix, whatever the first parent's list holds. Say
   so in the module docstring's L2 NOT-checked list, the help page's "What it does not check" and
   the `routed_commits.py` row of the kit README; narrow the help page's "still guards" sentence to
   "a line the commit itself removes, the list still being present, still guards"; narrow the build
   README's third Expected-improvements bullet the same way. An arm pins it: a fix commit deletes the
   list and edits `src/b.txt`, which its parent's list names, the disk copy removed, and the verb
   names no L2 for `src/b.txt`.
2. M2: two arms beside AC5 of unit 2, a first parent whose list is not UTF-8 and one whose list path
   is a directory, each graded by the working list; `build_fixture` accepts bytes. Staged red by
   `got[sha] = []` in the except (the non-UTF-8 arm).
3. M3: an arm over a trailered merge in a fixture of its own, the side lineage's list omitting
   `src/b.txt` and the first parent's naming it, expecting L2. Staged red by `parents[-1]`.
4. L1: an arm that stubs `run_git` with a stream cut before a header, one cut inside a body, and one
   with a tree answer before a blob: two Refusals, then None followed by the right body.
5. L2: in `marker-contract.test.sh`, a check that `gen_build_index.check_marker_line`,
   `routed_commits.check_marker_line` and `tree_lib.check_marker_line` are one object.

### Acceptance
Each arm red on its staged break and green restored; the nine shas of the first brief still exit 0.

### Gates
`routed commits name a specced unit` · `routed-commits selftest` · `marker contracts` ·
`policy fixtures` · `lexicon naming predicates` · `docs` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)`

### Non-goals
- Any change to a verdict, a predicate, a git-call figure or a finding's wording.
- The refuted finding 2.

### Limitations
- Those of the first brief, `2026-11-25-prompt-TOOL-aTemperedLane-1-brief.md`, hold.

### Reuse
The review's own corrected fixes; `routed_commits.py`'s `parentlist` fixture and its KIT stub.

## Drawn from the session

> M1 keeps the code: the base behaved the same way, and the owner chose the rule with its fallback.
— agent, 2026-11-25

## Owner confirmation

Asked: Which L2 rule should land?
Answer: A: list at parent
