# TOOL-dSafePassage-26 deviation 180 — the step module still loads govkit lazily for four readers it borrows

**Serves:** deviation TOOL-dSafePassage-26

- **Departs from:** TOOL-dSafePassage-26@rev-11 [§2 S4]
- **Hand-off:** spec-to-code
- **Before:** S4 says the step module carries the remote ladder inline "so it imports nothing from `govkit.py`".
- **After:** `tools/govkit/upgrade_steps.py` carries the ladder inline between `remote_ladder_py` markers and holds the landing base, the revision-blob reader and the atomic writer itself, so none of those reaches govkit, and it has no `import` of govkit, AC3's probe. Its `load_govkit` still loads the deployer by path, at call time, for the readers it borrows: the tool root, the `{prefix}` token, the kit-dir resolver and the staging journal's name.
- **Cause:** builder discovery
- **Reason:** those readers live in govkit and S4 names only the ladder; moving each is outside this unit's items, and a call-time load is no import edge, which is what unit 3's §8 F1 forbids.
- **Evidence:** an `ast` probe of `tools/govkit/upgrade_steps.py` found no `Import` or `ImportFrom` naming govkit, and `git grep -c "^# >>> remote_ladder_py" -- tools/govkit/upgrade_steps.py` printed 1 (this unit's acceptance ledger, AC3).
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-26, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-26
