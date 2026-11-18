# TOOL-dDeclaredLoop-8 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-8

No merge bar, no self-test suite and no gate leg ran in this pass, and `claims.py --selftest` was not
run. The criteria were observed on node `d` (win32) by probes of the unit's own code: each plant of
`tools/loop/claims.py` by direct CLI, and the card, the replay and `--claims` over a scratch clone of
this tree with its own bare remote under the host temp directory, the working copies of the changed
checker, driver and module copied in. The inline remote ladder was compared byte for byte with its
canonical copy, and `gen_map.py --check` exited clean after the map was regenerated.

Owed to the close: every leg the spec's section 7 names, `core meta-check` and `docs` among them; the
RED-first observation of the spec's three `New arm:` lines, `key-moves` staged red with the base left
out of the canonical form, the new manifest-check arms staged red against a `render_card` with no
`keys —` cell and a replay that prints the stored card whatever the key, and the unattended suite's
AC2 arm staged red against the driver's five-field rows; and the `loop claims fixtures` row in
`tools/run-gates/selftest-budgets.txt` read against the leg's own timing.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/claims.py --fixture --plant key-moves` with the base sha left out of the canonical key form
exited 1, and 0 once restored: RED observed.
Not observed: the arm in `skills/session-kickoff/manifest-check.test.sh`, a suite arm, left unrun for the
owner's opt-in slow-suite run.
Not observed: the arm in `tools/unattended/unattended.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.

**Evidences:** TOOL-dDeclaredLoop-8
- AC1 — `key-stable` — `python claims.py --fixture --plant key-stable` in the loop kit's folder printed the same `k1:` key over the sources in two orders and `held`; `--plant key-moves` printed two different keys once the base sha moved, and `held`; both exited 0.
- AC2 — `key-unread` — `--plant key-unread` printed a key opening `k1:?` over a `base=?` source and `verdict re-derived` over two such keys, `held`, exit 0.
- AC3 — `typed-evidence` — `--plant typed-evidence` printed `verdict evidence` for a claim of classes `view,typed` over equal keys, `held`, exit 0.
- AC4 — `remote-aged` — `--plant remote-aged` printed `fresh` for a `remote` claim inside its bound and `re-derived` for one past it, `held`, exit 0.
- AC5 — `card-keys-worktree` — `--plant card-keys-worktree` built a primary with a bare remote and a linked worktree carrying one more commit, ran `card-keys` in each, and printed two view keys over a read base that differ, `held`, exit 0.
- AC6 — `keys — view k1:` — `manifest-check.sh --card --write --session t8` in the scratch clone wrote a card whose second line opens `keys — view k1:`; in a scratch repository holding no loop kit the second line read `keys — skipped: no loop kit resolves in this tree` and the card wrote, exit 0.
- AC7 — `keys view re-derived` — in a linked worktree of the clone, a card written, its READY line replaced by a `## route` and a READY line, then a commit: `--card --replay` printed a `now —` line naming the worktree's toplevel and ending `keys view re-derived · remote evidence`, and the written card differed from the stored one in the `keys —` view key, the `tree —` cell and the `recent —` run alone, its header, `claims —` cell, remote key and TAIL byte-identical; a second replay read `keys view fresh` and the primary's unmoved replay left its card byte-identical; over a cap below the card's size the stored card printed, unwritten, with `not re-derived: over the cap`.
- AC8 — `k1:` — `unattended.sh --claims` in the clone, `RUN_CLAIMS` on, over a bare remote holding a claim on `dDeclaredLoop` and one on a slug with no run record, printed rows of six TAB fields, the sixth `k1:` over the first and `k1:?` over the second, the first equal to `claims.py key` over the claim ref and the run record's blob at the default branch's tracking ref; the card's `claims —` rows ended ` · key ` and those keys' characters after `k1:`.
- AC9 — `card-keys` — `grep -n 'card-keys' help/loop.md` hit the claim-keys section, and `grep -n 'keys —' memory/map/features/session-kickoff.md` hit the cell's paragraph naming its `view` and `remote` classes.
- AC10 — `principle.p23` — `python -m json.tool gate-legs.json` in the tools folder showed `loop claims fixtures` enforcing `principle.p23`, and `grep -c 'principle.p23' tools/playbook/core-pending.txt` printed 0; the meta-check's own reading is owed to the close.
