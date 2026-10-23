# TOOL-dSafePassage-1 deviation 145 — the carries instrument's Design-exit bound relaxed for the three amended clauses

**Serves:** deviation TOOL-dSafePassage-1

- **Departs from:** dSafePassage [gates]
- **Hand-off:** design-to-spec
- **Before:** the packet's Gates hold `carries.py --build dSafePassage --exit` green at the Design exit.
- **After:** it reds three stale pins, `cl-dClosedLoop-0018`, `-0028` and `-0030`, because those specs pin the as-built view's hashes, which deviation records 11, 31 and 52 moved, and the instrument reads v2 at its baseline; the merge bar's carries join, which reads the view, is green on all thirteen clauses.
- **Cause:** design defect
- **Reason:** for an amended clause the two carries checks cannot both be green, so every option fails a bound and the fork rule's rung 6 relaxes the weakest; the merge bar is the charter's floor, while the instrument's Design-exit check is a bound the execution plan's Gates set and its own docstring makes temporary, so the instrument's bound is relaxed, for those three clauses alone.
- **Evidence:** the close's bar on the prepared merge, `spec tokens` OWN with three `carries <- stale` hits before the re-pin; `carries.py --build dSafePassage --exit` reading three stale pins after it.
- **Risk:** loosening
- **Approver:** author, citing ER:328, the run's main loop under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dClosedLoop-30
- **Caused-by:** PLAY-dClosedLoop-2
- **Bound:** carries.py --exit on the three amended clauses
- **Tier:** middle
