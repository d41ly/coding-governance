# Acceptance ledger — DEPL-aHalvedInstall-3

**Serves:** journal DEPL-aHalvedInstall-3

Built at `18dcb54f`; the version bumps it owed ride `1bfa4d01`. The arm is selfcheck check 3b-iii
in `tools/govkit/govkit.py`. It was observed RED with all seven descriptors staged back to their
base text, and again with one stated reason staged to whitespace. The existing 7l prose arm also
redded on this unit's own descriptor comment — a re-render claim that did not name the flag — and
the comment was reworded rather than the arm touched.

**Evidences:** DEPL-aHalvedInstall-3
- AC1 — `python tools/govkit/govkit.py selfcheck` — exit 0, `adopters: 13 descriptor(s) declare one, 7 with [[regenerate]], 6 with a stated why_no_regenerate`; `tools/playbook/kit.toml` carries the block
- AC2 — amended rev-2 — `build_region` applied to its own output over the render selftest's fixture returned identical bytes and kept the authored prose (section 9, rev-2)
- AC3 — `python tools/govkit/govkit.py selfcheck` — with the seven descriptors at base text it named agent-cap, agent-instructions, codebase-map, playbook-render, process-monitor, run-gates and settings-merge
- AC4 — `python tools/govkit/govkit.py selfcheck` — every reason stated: exit 0; `why_no_regenerate = "   "` in run-gates: names run-gates
- AC5 — `python tools/govkit/govkit.py epoch` — `--base cd90f7fa` prints no `FAILED` line at `1bfa4d01`
- AC6 — `selfcheck` — `[aHI-3 AC6]` stages playbook-render's block away and a whitespace reason into run-gates; 3b-iii names each, and each is green again on restore
- AC7 — `bash tools/playbook/adopt-playbook.sh --selftest` — 24 arms OK; with `write_region` staged to append, `1 of 24` fails, naming the run-twice arm (`f92c7452`)
