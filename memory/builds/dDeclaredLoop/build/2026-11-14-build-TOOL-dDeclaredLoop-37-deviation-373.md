# TOOL-dDeclaredLoop-37 deviation 373 — what the pass adds around the class predicate that the spec does not state

**Serves:** deviation TOOL-dDeclaredLoop-37

- **Departs from:** `TOOL-dDeclaredLoop-37@rev-3` [§4 "### The two arms"]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-37`'s spec at rev-3 has the planted arm hold when the predicate names the consumer's line and no other, has the predicate run one `git grep -n -F`, and says the predicate tells status 1 with empty output from any other failure without saying how it reads the status `run_git` discards.
- **After:** the planted arm also calls the predicate with a revision git cannot grep and holds only where that call raises `Refusal`; the `Refusal` that `run_git` raises carries the call's `status` and `out`, which the predicate reads; and the grep carries `-z`, so a hit's path and line are read by their separator and never by a colon split.
- **Cause:** builder discovery
- **Reason:** the staged break of the spec's second `New arm:` line, reading `run_git`'s failure as no hit, does not move the arm as written: a grep that finds the planted line exits zero, so no failure is read and the consumer is still named. With the unreadable-revision call in the arm, that break returns an empty list where a `Refusal` is expected and the arm fails. The same holds for AC3's `Red when:` clause, where the base run still prints its lines under that break. `run_git` returns bytes or raises, so the status had to travel on the exception; a second spawn site beside it would have spelled the pinned environment twice.
- **Evidence:** `tools/memory-tree/routed_commits.py#check_trailer_parses`, `tools/memory-tree/routed_commits.py#run_git` and the two arms at the end of `tools/memory-tree/routed_commits.py#run_selftest` at the pass commit of `TOOL-dDeclaredLoop-37`; the acceptance ledger's AC3 line and its staged-break paragraph.
- **Risk:** stricter
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-37
