# Brief — aSwiftRefusal: round 1's mediums and lows, promoted to TOOL-aSwiftRefusal-4

**Serves:** research TOOL-aSwiftRefusal-4

## The brief

### Goal
Close every confirmed finding of `reviews/2026-11-10-review-TOOL-aSwiftRefusal-1-3-closing-diff-round1.md` (CLEAN WITH FIXES: M1 to M4, L1 to L3) in one batched unit, as M4 of the build method promotes a diff exit's mediums and lows. Each item's fix is the one that record judged SOUND; for M4 it is the skeptic's class-level fix, not the finder's instance fix.

### Items
1. M1 — `verb_rescope`'s idempotence and `check_unit_deferred` agree: a same-reason defer row after a later dispatch row of that unit is a new deferral and is appended, not "already recorded". An arm runs defer, re-dispatch, same-reason re-defer and asserts the unit reads deferred.
2. M4 — `check_unit_deferred` moves to the shared kit library `tools/unattended/lib-unattended.sh`, and check 23 of `tools/unattended/check-unattended.sh` asks the same release question `read_open_passes` asks (terminal by spec status, or deferred): a released unit's window ends at its release, so a sibling's write admitted after it is not charged to the released unit. `check-unattended.test.sh` arms for a DEFERRED unit and a WONTDO unit whose path a sibling then writes, each asserting no dodged-join line names the released unit.
3. M3 — a region-four arm runs `--audit` over a dispatched unit set to DEFERRED with a defer row and asserts it is neither open nor STALLED, then set back to INPROGRESS and listed again.
4. M2 and L1 — `FLOOR_SHARD_3` and `FLOOR_ASSERTIONS` in `tools/unattended/unattended.test.sh` pin the TOOL-aSwiftRefusal-1 and -2 region-3 arms, and every new arm of this unit, each with a RAISED comment counted off the arms' own lines; the -1 ordering arm gains a positive control that reaches the stub checker and hits the spec-token refusal text.
5. L2 — `--check-commit`'s header comment names the deferred skip it leaves out on purpose, and why.
6. L3 — the `--audit` sentence of `tools/unattended/VERBS.template.md` and its copy `memory/guides/UNATTENDED-VERBS.md` says a deferred unit is left out too; the two stay byte-equal past the marker line.

### Acceptance
Each item's arm or probe, as the review record's Fix lines state them, observed red at 17308b6c3 and green after. Every existing arm of the driver suite and the gate suite stays green.

### Gates
unattended kit self-test (the driver suite and the gate suite) · unattended kit gate · shell hygiene legs · lexicon naming predicates · kit epoch · kit version markers · docs · memory hygiene · spec tokens · pass-order history · routed commits · brief-recorded; then the full bar at the lander.

### Non-goals
Any change to units 1 to 3's behaviour beyond what an item names. `pass_commit`, `check_pass_open` and `read_pass_declarations`. The dOrderedCharter branch.

### Limitations
`tools/unattended/check-unattended.sh` carries raw CR bytes in its awk regexes: edit it in binary mode. Kit versions move through the lander's `mint`. Unit agents run no gate legs or suites; the main loop observes each new arm red then green at the close.

### Reuse
The review record names each seam. `check_unit_deferred` (TOOL-aSwiftRefusal-2) is the one predicate; `read_open_passes`' terminal skip and check 23's existing exclusion blocks are the shapes to follow.
