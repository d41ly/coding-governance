# TOOL-dDeclaredLoop-43 deviation 433 — the guarded write's nested helper named with a declared verb

**Serves:** deviation TOOL-dDeclaredLoop-43

- **Departs from:** `TOOL-dDeclaredLoop-43@rev-3` [§4 "### The write"]
- **Hand-off:** spec-to-code
- **Before:** the block's body names its one nested helper `replace_target`.
- **After:** the helper is `write_target`, its body and every call of it as the spec's block writes them, in all three byte-identical copies of the `guarded_write_py` block; the plant's own nested helpers in `tools/loop/guard.py#run_guard_plant` lead with `run`, `read`, `write` and `check`.
- **Cause:** builder discovery
- **Reason:** the naming lexicon declares no verb `replace`: its suggest verb answered that `replace` is not in the declared table, while `write_target` leads with `write`, which the declaration carries; the block is carried three times, so the spec's name would add three verb offenders against a pin that does not rise.
- **Evidence:** `python tools/lexicon/lexicon.py --suggest replace_target --as py.function` and the same call for `write_target`, run in this pass; the acceptance ledger `2026-11-15-build-TOOL-dDeclaredLoop-43-1-acceptance-ledger.md`.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-build-TOOL-dDeclaredLoop-43-1-acceptance-ledger
