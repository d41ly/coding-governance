# PLAY-dOrderedCharter-78 deviation 782 — the runlog self-test's window arms read the duration's marked form

**Serves:** deviation PLAY-dOrderedCharter-78

- **Departs from:** `PLAY-dOrderedCharter-78@rev-1` [Scope]
- **Hand-off:** spec-to-code
- **Before:** S8 has `tools/runlog/selftest.py` gain one arm, and names `scan_time_slots` as the one reader whose word the second template might contradict.
- **After:** three existing arms re-expect the Summary `duration` fact in the marked form, the window and placement arms' `<n>s · DERIVED from the window`, and the absent-window arm's `- · DERIVED from the window`; the docstrings of `scan_time_slots` and `derive_int_slots` say an alternative carries no slot or the first template's own.
- **Cause:** builder discovery
- **Reason:** those arms compare the rendered fact with the bare count and the bare `-`, so the render S8 asks for would red them; every Summary fact writes its first template, so a model with no window fills the slot with `-` and keeps the mark, as the `window` fact keeps its ` to `. Each arm's claim, the value is the difference of the two bounds or absent, is unchanged.
- **Evidence:** a probe over `python tools/runlog/runlog.py record dOrderedCharter` read the line `- duration: <n>s · DERIVED from the window`, and `check_fact_value` admitted that form, the bare count and `- · DERIVED from the window` (PINNED, at 5403142e4 with the pass applied).
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-78
