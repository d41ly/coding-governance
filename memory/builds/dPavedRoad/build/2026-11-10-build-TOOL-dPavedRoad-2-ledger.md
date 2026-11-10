**Serves:** journal TOOL-dPavedRoad-2

# TOOL-dPavedRoad-2 — acceptance ledger

The unit as built, at spec rev-2, in commit e719dff11. `tools/hooks/format-guard.js`'s block message
now carries, verbatim, the `agent` and `returned` lines `handoff.py agents` derives for each agent it
names and the `committed` line for each new commit it names, derived only on a stop that already
blocks. `tools/hooks/agent-cap.js` exports `resolveKitDir` and `extractHandoffMarker`;
`tools/gate-legs.json` adds agent-cap.js to the format-guard self-test guard; the suite gains 20 PR2
assertions and its floor moves 129 to 149. The commit re-stamps the kickoff manifest's last-audit.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in the pass. The builder observed each
criterion with a probe of this unit's code, transcribed below from its return: the spec's own
`node -e` and `python -c` probes, `pr2-probe.js` against a scratch hook copy beside a stub
`handoff.py`, and `pr2-fixture.sh` over the suite's `seed_repo` fixture in `%TEMP%/pr2fx`.

Owed at the close: the RED-first observation of the new arm in `tools/hooks/format-guard.test.sh`
(AC10 to AC12) and the section 7 legs, the `format-guard self-test` floor of 149 among them.

**Evidences:** TOOL-dPavedRoad-2
- AC1 — the spec's `node -e` probe of `tools/hooks/format-guard.js` printed `- committed — 0123abcde · main · a, b true`.
- AC2 — `pr2-probe.js`: the stub `handoff.py` logged argv with `-B`, the session id and no `--write`, and `readHandoffLines` returned its two lines.
- AC3 — `pr2-probe.js`: with the stub exiting 1, `readHandoffLines` returned an `error` naming exit 1; the `GOV_PYTHON` fall-through and a spent bound were also covered.
- AC4 — `pr2-probe.js`: `extractTurnAgents` read the marker path through agent-cap, refused five bad marker paths (absolute, drive-qualified, `..`, leading `-`), and preferred the call's input prompt.
- AC5 — `pr2-probe.js`: `deriveOwedLines` kept the one line for `a1` and filtered out off-shape and other-agent lines.
- AC6 — `pr2-probe.js`: `renderBlockReason` printed the owed line verbatim and kept or dropped the `handoff.py agents` sentence by the count rule.
- AC7 — the spec's `node -e` probe of `tools/hooks/agent-cap.js` printed the `tools\roles` path and `function`.
- AC8 — the spec's `python -c` probe of `tools/gate-legs.json` printed `True`.
- AC9 — `grep -n "derived for it\|prints the lines" tools/hooks/README.md help/roles.md` found the new wording in both pages.
- AC10 — `pr2-fixture.sh`: a stop missing the marked agent's line blocked with `- $A1` verbatim and without the `handoff.py agents` sentence, and the stub log showed `agents --handoff` with `--session` and no `--write`.
- AC11 — `pr2-fixture.sh`: a commit whose subject holds ` · ` blocked with its derived `committed` line reading `PR2 a, b`, and pasting that line allowed.
- AC12 — `pr2-fixture.sh`: a message passing every check left the stub's log empty, and `format-guard.js` allowed.
- AC13 — the staged diff of `memory/guides/SESSION-KICKOFF.md` showed one removed and one added `last-audit:` line; the new sha equals `9116f5753`, HEAD at staging, and the new datetime is later than the old.

## New arm, observed at the close

In clones of `6681cdc80` under `%TEMP%/dpr`, by the main loop, `bash tools/hooks/format-guard.test.sh`.
RED, break one: with `deriveOwedLines` staged to return no line, it exited 1 in 48 s, 140 passed and
9 failed, every failure a PR2 arm (the derived agent, left-out agent and committed lines missing from
the reason, and the stub never called). RED, break two: with the stop staged to derive on an allow,
it exited 1 in 51 s, 147 passed and 2 failed, `PR2 an allowing stop spawns no handoff.py` among them.
GREEN: at `6681cdc80` it exited 0 in 45 s, `PASS (149 assertions)`, the floor exactly.
