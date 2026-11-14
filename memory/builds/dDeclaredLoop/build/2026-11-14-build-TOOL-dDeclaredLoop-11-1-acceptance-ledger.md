# TOOL-dDeclaredLoop-11 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-11

No merge bar, no self-test suite and no gate leg ran in this pass, and `loop_checklist.py check --selftest`,
the new leg's command, was not run as a command. The criteria were observed on node `d` (win32) by probes
of the unit's own code: `check`, each plant run one at a time as `--fixture --plant <case>`, `show` on a
mapped and an absent handle, the self-test's case loop called in-process with two plants kept, and the
`grep` commands the criteria spell. The unarmed paths were observed over a copy of the loop kit in the
session scratch folder, with no driver beside it and then with a driver whose `DOD_CORE` line is empty,
removed after.

RED observed in this pass, on a break made in-process and never on disk: with `check_checklist_rows`
dropping its core-handle refusals, the map checked one way only, the self-test's `missing-handle` case
printed FAIL, exit 0 where 1 was owed, and the self-test exited 1.

Owed to the close: every leg the spec's section 7 names; the `loop checklist tags` leg itself, with the
RED-first observation its `New arm:` line names, the failing case staged by the `missing-handle` plant;
and the core meta-check over the new leg's `enforces`, which AC6 names.

**Evidences:** TOOL-dDeclaredLoop-11
- AC1 — `loop: checklist` — `python loop_checklist.py check` exited 0 printing one `loop: checklist`
  line per handle of the two registry lines, `loop: checklist DOD_CORE · gates-green · item.test.verdict`
  first, then one `loop: checklist-count` line per registry, reading 13 and 17 handles, each all mapped. PINNED 2026-11-14
- AC2 — `unmapped-check` — `--plant missing-handle` exited 1 with `DOD_CORE unmapped-check has no
  [[checklist]] row mapping it onto an item`; `--plant stale-row` exited 1 naming the row of
  `retired-check`, a handle `DOD_CORE` does not hold; `--plant two-rows` exited 1 naming the second
  `gates-green` row and the row that maps it already.
- AC3 — `item.deploy.nosuch` — `--plant undeclared-item` exited 1 naming the `gates-green` row mapping
  onto `item.deploy.nosuch`, which no `[[item]]` row declares; `--plant bare-item` exited 1 naming the
  `landed-via-lander` row mapping onto `deploy.land`, which opens no item step.
- AC4 — `number` — `--plant numbered-row` exited 1 naming the key `number` on the `gates-green` row;
  `--plant bad-registry` exited 1 naming the registry `DOD_EXTRA`.
- AC5 — `show nosuch` — `show reuse-probed` printed `DOD_CORE item.design.seams`, exit 0, and
  `show nosuch` exited 2; over the kit copy with no driver beside it, `show reuse-probed` still printed
  that line while `check` exited 2 naming where it looked.
- AC6 — `principle.p11` — `grep -n '"loop checklist tags"' tools/gate-legs.json` found the leg row, its
  argv naming `loop_checklist.py`, `check` and `--selftest` and its `enforces` holding `principle.p11`;
  `grep -n 'loop checklist tags' tools/govkit/registry.toml` found its `[[exempt_leg]]` row; and
  `grep -n 'loop_checklist.py show' help/loop.md` found the section. The core meta-check is a gate and
  was not run; it is owed to the close.
