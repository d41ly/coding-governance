# TOOL-dUnstuckLanding-25 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-25

No merge bar and no self-test suite ran in this pass. The driver suite's `TOOL-dMendedRecall-2` arms
were run ALONE behind a copy of the suite's own prologue, on fixture repositories under the user
temp directory. They were then run again with the HEAD copy of the driver swapped in. The restore
was taken from `ef1dcdb6` and reconciled by hand with unit 16's SEV-aware filer. The whole suites
and the gate legs are owed to the close.

**Evidences:** TOOL-dUnstuckLanding-25
- AC1 — `write_ask_views` — `grep -c` over the driver prints 3: the auto-file header's sentence, the
  definition, and the call at the end of `write_inherited_asks`. It printed 0 at HEAD. The call sits
  inside unit 16's version of the filer, counting a BLOCKER filing exactly as a HIGH one. A reused
  ask counts as nothing.
- AC2 — `f4-views-double: 1 filed` — the probe carried the prologue, the inherited-red fixture, the
  AC9 MET pair and the whole F4 slice, 31 assertions. It passed all 31 over the restored driver. Over
  the HEAD driver it failed exactly the four this AC names: both AC9 view lines, the
  `f4-views-double: 1 filed` hit, and the once-per-call count. A second probe ran the suite's whole
  `TOOL-dMendedRecall-2` section with the real generator installed, 41 assertions with no SKIP. It
  passed 41 over the restored driver and failed 18 over the HEAD driver.
- AC3 — `VERBS.template.md` — `adopt-unattended.sh` re-copied the render, and `--check` then
  printed `in sync` and exited 0.
- AC4 — `verb_status` — the entry names, in printed order: the `unattended: <slug>` opener, then
  `phase` with its three decorated forms. Those are `LANDED (attended)`, which unit 14 added and
  which takes precedence, the derived LANDED, and the explained LANDING. Then `witness`, `NONE`
  refused by fail 11, then `halt-code` and `spec-audit` before `next`. After `next` come `parked`,
  `noted`, `STALE briefs`, `briefs gone`, `resume-tick` and `orphans`. Then the asks verdict, the
  worktree verdict, and `keepalive` last. That matches the `printf` and the suffix order at HEAD.
- AC5 — `01c22e15` — a script compared every non-blank line `ef1dcdb6` added over the merge-base
  `1f915870` with the file at HEAD, for every file in that diff. `git merge-tree` names 28 files
  conflicted. Their dispositions:
  - `tools/unattended/unattended.sh` — restored by this unit: `write_ask_views`, its header
    sentences, the `filed` counter and the call. The one line still absent is the `filed=0` local,
    now spelled `today sev filed=0`. The version marker is superseded, see below.
  - `tools/unattended/VERBS.template.md` and its render `memory/guides/UNATTENDED-VERBS.md` —
    restored by this unit, 29 lines each. They are extended by `LANDED (attended)`.
  - `tools/memory-recall/selftest.py` — superseded: one of 34 added lines is absent. It copied the
    memory-tree modules into a literal `memory-tree` directory, and its successor is
    `TOOL-aRepatriatedFork-46`'s derived `mt_name`, which the merge kept on purpose. The other 33
    lines are present.
  - The 24 other conflicted files — superseded. Each added only the `unattended@1.48` marker, and
    the successor is the marker at HEAD, `unattended@1.57`. They are `.claude/skills/unattended/SKILL.md`,
    the guides `PLAYBOOK-TEMPLATE.md`, `UNATTENDED-ASKS.md`, `UNATTENDED-PROTOCOL.md` and
    `UNATTENDED-STOPS.md`, and, under `tools/unattended/`, `ASKS.template.md`,
    `PLAYBOOK-TEMPLATE.template.md`, `PROTOCOL.template.md`, `README.md`, `SKILL.template.md`,
    `STOPS.template.md`, `check-brief-recorded.sh`, `check-pass-order.sh`, `check-unattended.sh`,
    `fixture-record-one.template.md`, `fixture-record-two.template.md`, the two
    `fixture-records/` piece records, `gate-guard.js`, `playbook.fixture.md`,
    `playbook.fixture.template.md`, `run-lease.js`, `stall-recorder.js` and `stop-guard.js`.
  - The merge's unconflicted files are present: all 246 lines `unattended.test.sh` added, and every
    `memory/builds/dMendedRecall/` record. `memory/LIVE.md`, `memory/backlog/TOOL.md` and
    `memory/ledger/2026-10.md` are generated, and they add no line that is absent.
