# TOOL-aAnsweredPark-1 — acceptance ledger

**Serves:** journal TOOL-aAnsweredPark-1
**Caused-by:** TOOL-aAnsweredPark-1

One builder pass over base `8277fed4b`. No merge bar, no self-test suite and no gate leg ran in it; each
line below is a direct CLI call or a `python -c` probe of the changed code.

**Evidences:** TOOL-aAnsweredPark-1
- AC1 — `python tools/loop/position.py --fixture --plant parked-decisions` printed `unanswered` awaiting with T, `answered` act with none, its record a read line by the plant's own predicate, `untracked` awaiting, and `held`; `--plant owner-decision` printed the interrupt line ending `answer item.parked.2026-01-01t00-00-00z` and `held`.
- AC2 — the same `parked-decisions` run printed `other-row` and `no-reason` awaiting with T.
- AC3 — the same `parked-decisions` run printed `other-word` awaiting with T.
- AC4 — the same `parked-decisions` run printed `one-second` awaiting with T ending `.2` alone.
- AC5 — `python tools/loop/position.py --fixture --plant parked-kinds` printed `no-question` act with none.
- AC6 — the same `parked-kinds` run printed `hold-resumed` and `hold-passed` act, `hold-live` awaiting on `hold host-owner-action · until owner`, and `held`.
- AC7 — `python tools/loop/adapt.py --fixture --plant owner-approves` ended `held`, the change released by its disposition record; the `grep -c` of the signature printed 1.
- AC8 — `grep -nE "FX_OWED|handover\[.owed.\]|PARKED_ROW" tools/loop/position.py` printed nothing, and the `steps` plant ended `held`.
- AC9 — `grep -c "replaces the interrupt wording of" tools/loop/position.py help/loop.md` counted 1 in each, the other three sentences beside it, and the grep for `every owed entry stands` printed nothing.
- AC10 — `read_open_decisions` over a shared clone at `18ba9d38` returned six open rows, the six tags the criterion lists, and no record path; the clone was removed.
- seen-red — `loop position fixtures` — red `ace7f1eec` — green `ace7f1eec` — `parked-decisions`: the base engine's interrupt loop put back reds `answered` and `one-second` and, its tag unprinted, the other five; settled fixed true reds all but `answered`; the tag compare dropped reds `other-row`; the word test dropped reds `other-word`; the Reason test dropped reds `no-reason`
- seen-red — `loop position fixtures` — red `ace7f1eec` — green `ace7f1eec` — `parked-kinds`: the base engine's interrupt loop and unconditional hold put back red `no-question` and `hold-resumed`; the hold branch removed reds `hold-live`; the passed test fixed false reds `hold-passed`

## Owed to the close

Every leg section 7 of the spec names. The two arms `parked-decisions` and `parked-kinds` were not
observed in this pass; the main loop saw each red and then green afterwards, at `ace7f1eec`, and the
two seen-red lines above record it.
