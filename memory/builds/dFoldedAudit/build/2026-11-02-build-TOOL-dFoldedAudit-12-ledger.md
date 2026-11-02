# TOOL-dFoldedAudit-12 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-12

The acceptance criteria were observed by this unit's builder over the tree of this commit, with no gate, suite or bar. AC1 to AC7 ran `node degraded-fixture.js <case>`, the stub runner section 6 defines, written under the run's scratch from the AsyncFunction shape of `run_wf` and evaluating `tools/workflows/unattended-build.js` in strict schema mode, over the suite's `UNITS` and the FA3 doubles. Over the parent render the five cases printed 11, 3, 0, 2 and 1 failures, the 0 being `undeclared`, and over this commit's render all five were green. AC8 ran the two greps. Each new arm's RED-first observation is the close's, and it is not recorded here.

The three `New arm:` blocks share the fixture's rows and needles, and they never ran. `bash -n` parsed the file. The fixture is the evidence for the criteria, and the arms are owed as written.

**Evidences:** TOOL-dFoldedAudit-12

- AC1 — `node degraded-fixture.js held-exit` — a confirmed BLOCKER at a held `BOUNDED` with a dead stage returned, `disposal: NOT done` was traced, and `note` held `--record-round tB --subject tB-spec-set-r1 --audited "A-tB-1 A-tB-2"`, `--blockers 1 --highs 0`, `--chain-verdict tB` and `--finding <id>/<severity>/<nature>/<spec>[,<spec>]/<unit>/<rev>`.
- AC2 — `node degraded-fixture.js refused-return` — one confirmed HIGH at zero blockers, with a stage return carrying a sibling edit beside an empty `promotedIds`, traced `disposal: NOT done`, and `note` held `--blockers 0 --highs 1` and `--chain-verdict tB` and lacked `the resume route` and `and dispatch from`.
- AC3 — `node degraded-fixture.js held-exit` — `commit the disposal's folds and specs`, `--record-round`, `commit the chain record it staged` and `--chain-verdict` read in that order, and `note` held `CONTINUE: re-invoke this harness with round: 2`, `STOP: dispatch every unit` and `HOLD: run the recipe it prints`.
- AC4 — `node degraded-fixture.js refused-return` — the RESULT carried the refused `local` row at id 7 and the sibling edit, so both were in reach, and `note` lacked `--finding 7/` and `--sibling A-tB-`, and the RESULT held no `chainRecord`.
- AC5 — `node degraded-fixture.js undeclared` — one HIGH at zero blockers and a dead stage with no `disposal`: `note` held `--plan tB --paths`, ended `the resume route.`, and lacked `--record-round` and `--chain-verdict`.
- AC6 — `node degraded-fixture.js local-fold` — `nextAction` held `RECORD this round: commit the disposal's folds and specs, run `, then that round's `--record-round`, then `, then commit the chain record it staged. Then run `, then `--chain-verdict tB`, in that order.
- AC7 — `node degraded-fixture.js clean-round` — `nextAction` held `Commit the record, then run `, `commit the chain record it staged` and `--chain-verdict tB`, in that order.
- AC8 — `grep -c 'commit the chain record it staged' tools/workflows/unattended-build.js` printed 1 and `grep -c 'renderChainStep(' tools/workflows/unattended-build.js` printed 4.

Beyond section 6. S5 was compared whole: `node degraded-fixture.js differential` ran six undeclared shapes, two dead stages, a refused return, a promotion, a clean round and a round with nothing standing, against the parent render, and every trace and RESULT was byte-identical.

Seven breaks staged on scratch copies each moved the fixture from green to red at the case the spec names: the join left below the stage threw `Cannot access 'auditedIds' before initialization` on `held-exit` and `refused-return`, the dispatch ending restored reddened both, the declared branch taken unconditionally reddened `undeclared`, `renderChainStep` with no commit clause reddened `held-exit`, `local-fold` and `clean-round`, the refused lists rendered and a `chainRecord` key each reddened `refused-return`, and the disposal's commit moved behind the record reddened `held-exit`. That grades the fixture and is no `New arm:` observation.

Owed at the close: the bar, and the three `New arm:` lines of section 7, each RED on its staged break and GREEN once restored. `FLOOR_ASSERTIONS` moved 778 to 815, 37 assertions counted off the block's own lines and not measured.
