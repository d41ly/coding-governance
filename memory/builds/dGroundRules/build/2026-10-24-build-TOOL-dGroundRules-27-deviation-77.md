# TOOL-dGroundRules-27 deviation 77 — the refusal case's handler is minted beside its CASES entry

**Serves:** deviation TOOL-dGroundRules-27

- **Departs from:** TOOL-dGroundRules-27@rev-4 [§4 Inventory]
- **Hand-off:** spec-to-code
- **Before:** §4 Inventory names two identifiers the unit mints: `run_govkit` and the `CASES` entry `govkit-source-root-refused`.
- **After:** the `CASES` entry's handler is a third minted identifier, the py.function `run_govkit_source_root_refused` in `tools/policy/check_policy.py`, beside the case it runs.
- **Cause:** builder discovery
- **Reason:** every `CASES` row is `(name, arm, handler)` and the handler is called with the case's name; S5's case must catch a `RuntimeError` and read its message, which no lambda can, and no existing dispatcher in the kit runs a call that must raise. The handler adds no behaviour beyond S5's, and the repo's convention is one `run_<case>` per outcome case.
- **Evidence:** `python tools/lexicon/lexicon.py --suggest run_govkit_source_root_refused --as py.function` printed `OK — run_govkit_source_root_refused leads with run, which the declaration carries, and satisfies snake for cell py.function`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dGroundRules-27, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dGroundRules-12
- **Caused-by:** TOOL-dGroundRules-27
