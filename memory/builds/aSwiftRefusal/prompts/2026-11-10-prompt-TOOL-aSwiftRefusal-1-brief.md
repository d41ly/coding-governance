# Brief — aSwiftRefusal: `--dispatch` refuses cheaply first, and a deferral stops blocking

**Serves:** research TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3

## The prompt

> Fix three defects in the unattended kit's `--dispatch` verb (`tools/unattended/unattended.sh#verb_dispatch`, with `read_open_passes`, `check_pass_open` and the library's `pass_commit` in `tools/unattended/lib-unattended.sh`). Route the work through `/session-kickoff` and this repository's own spec-then-build flow; the owner asked why so many unit dispatches are refused and wants it addressed before the remaining rearchitecture builds run.

The task as the session that started this one relayed it, on 2026-11-09. It states the owner's turn: the owner reported that unit refusals waste large amounts of time and tokens across a multi-build rearchitecture, asked whether to fix it now, and the answer was yes, as a separate kit fix on main while dOrderedCharter finishes on its own branch.

## The brief

### Goal
Every `--dispatch` refusal decidable from the run-state file and the spec headers arrives before the spec-token run, and a unit set aside with `--rescope --act defer` neither blocks the order gate nor keeps its open passes reserved.

### Items
1. `verb_dispatch` runs the `SPEC_TOKENS_CLI` block after every check that needs no tree-wide scan: the order gate, the edge and cycle refusals, the hold gate, the `--writes` path refusals, the shared-record refusals, the generator pairing and condition 1. Every refusal's text stays unchanged, so the existing arms in `tools/unattended/*.test.sh` still match. [planned TOOL-aSwiftRefusal-1]
2. The order gate lets an earlier-order unit pass when it is deferred: its spec reads DEFERRED and its latest `rescope · item defer` row comes after every `dispatch` row naming it. A consumer of a deferred unit stays blocked by the edge refusal. [planned TOOL-aSwiftRefusal-2]
3. `read_open_passes` leaves out every key of a deferred unit, by the same predicate, and names each released key on stderr, as its terminal-status skip does. [planned TOOL-aSwiftRefusal-3]

### Acceptance
1. With `SPEC_TOKENS_CLI` naming a checker that exits 1, an out-of-order dispatch reds with the order gate's text and a sibling-overlap dispatch reds with condition 1's text, and neither prints the spec-token refusal. At BASE both arms red, because the spec-token refusal arrives first.
2. A unit at order 2 dispatches while the only order-1 unit reads DEFERRED and carries a defer row. At BASE it is refused by the order gate.
3. The order-1 unit with a defer row but a spec reading INPROGRESS still blocks. So does one whose dispatch row follows its defer row.
4. A sibling declaring a path that a deferred, dispatched unit declared is admitted, and stderr names the released key. At BASE condition 1 refuses it.
5. A unit re-dispatched after its defer row reserves its paths again.
6. Every existing `--dispatch` arm stays green.

### Gates
unattended kit self-test (the driver suite) · unattended kit gate · shell hygiene legs · lexicon naming predicates · kit epoch · kit version markers · docs · memory hygiene · spec tokens · pass-order history · routed commits · brief-recorded; then the full bar at the lander.

### Non-goals
The dOrderedCharter branch and its records. `pass_commit`, `check_pass_open` and `check_commit_message`. The edge refusal: a consumer of a deferred unit stays blocked. The spec-token checker itself. Any new rescope act. The hold gate's own cost.

### Limitations
Kit versions move through the lander's `mint`, not by hand. Unit agents run no gate legs or suites; the main loop observes each new arm red then green at the close. The three units write the same two files, so they build in order.

### Reuse
`read_open_passes`' terminal-status skip is the shape for item 3, stderr line included. The order gate's dispatch-row grep is the row reader to share. Ask TOOL-aRoutedQuill-13 states item 2 and its accept clause; this build closes it. Recall returned TOOL-dGroundRules-66 and -70 for `read_open_passes`, and aDeferredBar F3 for why the spec-token check runs inside `--dispatch`.

## Drawn from the session

> unit 37's first dispatch was refused on paths deferred unit 31 still held (released only by a spec commit carrying `Pass: PLAY-dOrderedCharter-31`, 9e16b1b49); unit 40 was refused twice by the order gate on deferred unit 39, and is being worked around by moving spec 40 to order 37. Each of the three refusals came after the full spec-token run.
— agent, the starting session's brief, 2026-11-09

> 2026-11-09T18:31:02Z dispatch · item e0768687 PLAY-dOrderedCharter-31 · reason tools/govkit/registry.toml …
> 2026-11-09T18:39:21Z rescope · item defer PLAY-dOrderedCharter-31 · reason third divergence in this run …
— agent, dOrderedCharter's RUN.md: unit 31 was deferred on 2026-11-04 and dispatched again on 2026-11-09, so a defer row alone does not decide a deferral; a dispatch after it re-takes the unit

## Owner confirmation

Asked: whether to fix the `--dispatch` refusals now, while dOrderedCharter finishes on its own branch.
Answer: "the answer was yes, as a separate kit fix on main" — relayed by the starting session, 2026-11-09.
