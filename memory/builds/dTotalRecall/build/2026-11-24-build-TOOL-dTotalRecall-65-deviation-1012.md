# TOOL-dTotalRecall-65 deviation 1012 — the kickoff manifest is re-stamped in this pass, and the fixture plants of units 58 and 60 read a registry row

**Serves:** deviation TOOL-dTotalRecall-65

- **Departs from:** `TOOL-dTotalRecall-65@rev-5` [§2 S4; §3; §4 "Files touched"; §5 risks]
- **Hand-off:** spec-to-code
- **Before:** the spec leaves the kickoff manifest's re-stamp to TOOL-dTotalRecall-69 and the ratchet leg red until it, and its S4 re-points two plants, `kept-row-drained` and `kept-row-editable`.
- **After:** the pass commit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`; the plant `reason-on-other-file` (unit 60) writes its row into its fixture's registry and its suite hit names the registry; `record_kinds.py`'s plant `marker-in-kept-script` (unit 58) keeps a script of its own fixture, `record_kinds.py#FIXTURE_KEPT_SCRIPT`, by a row of that fixture's registry.
- **Cause:** builder discovery
- **Reason:** the pre-commit hook's C5s arm refuses a commit that stages `.memory-tree.conf`, a watched path, without a changed `last-audit`, and the build brief asks for the stamp in the same commit; units 58 and 60 added the two plants after rev-5 was written, each passing the retired `kept` argument or reading the engine's table, and section 4 has the builder re-derive the readers.
- **Evidence:** the pass commit of TOOL-dTotalRecall-65, its brief `2026-11-24-prompt-TOOL-dTotalRecall-65-build-brief.md` and its acceptance ledger `2026-11-24-build-TOOL-dTotalRecall-65-1-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-65
- **Made-by:** lease-dTotalRecall
