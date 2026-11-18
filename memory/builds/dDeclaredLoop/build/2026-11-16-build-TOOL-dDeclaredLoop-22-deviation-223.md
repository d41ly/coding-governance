# TOOL-dDeclaredLoop-22 deviation 223 — the census and the Skill row re-based over TOOL-dDeclaredLoop-20, and the signals' anchor global

**Serves:** deviation TOOL-dDeclaredLoop-22

- **Departs from:** `TOOL-dDeclaredLoop-22@rev-4` [§5]
- **Hand-off:** spec-to-code
- **Before:** §5's sweep and "Budgets and records" raise the driver's refusal ceiling from 335 PINNED to 337 PINNED and the unattended Skill render's no-headroom size row from 10848 PINNED to 10893 PINNED, figures read at `c7f4ef116` before TOOL-dDeclaredLoop-20 landed; §4's inventory names `_rs_why` and `_rs_tier2` as the driver globals `derive_review_signals` sets.
- **After:** the ceiling rises from 338 PINNED to 340 PINNED and the Skill row from 10922 PINNED to 10967 PINNED, the figures TOOL-dDeclaredLoop-20 left at the base of this pass, as the decision row TOOL-dDeclaredLoop-22 landed ahead re-bases them; the census read 333 PINNED branches and 5 PINNED sites at the base and 335 PINNED and 5 PINNED at the commit, and the render 10967 PINNED bytes CR-stripped. `derive_review_signals` also sets `_rs_anchor`, the region's lowest-numbered unit id, so the record's anchor comes from the one region read §5 prices rather than a second read in `run_recommend`; the factory's fixture lifts its bindings check into `check_bindings`, now shared by the `typed-kinds` and `recommendation` plants.
- **Cause:** builder discovery
- **Reason:** TOOL-dDeclaredLoop-20 raised both figures after rev-4 was written, and the spec states the anchor and the plant's bindings check without naming where either is computed.
- **Evidence:** the TOOL-dDeclaredLoop-22 row of `memory/DECISIONS.md`, the `REFUSAL_CEILINGS` line of `.memory-tree.conf` and the Skill row of `tools/template-size-limits.txt` at the base of this pass and at its commit, `tools/unattended/unattended.sh#derive_review_signals` and `tools/memory-tree/build_records.py#check_bindings`.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-20
