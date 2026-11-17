# TOOL-dDeclaredLoop-116 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-116

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on this
node (win32), at rev-1 of the spec, over the working tree, by the first dispatch, which started from the
base `1c489a95e`. The new plant ran alone by `--fixture --plant`, standing in for the `loop budget
fixtures` leg; the plants `ending`, `unattended-root` and `no-own-conf-read` of `budget.py`,
`parent-in-extra-phase` of `loop_parents.py`, `record-written` of `upstream.py`, `steps` of
`position.py`, `owner-approves` of `adapt.py` and `conf-readers-declared` of `loop_lib.py` each ran alone
and held, standing in for their legs only as far as those plants reach. The sweep re-run at the base held
every design claim: `PLANTS` of `budget.py` held 33 PINNED keys, the `get("MEMORY_ROOT")` grep over the
loop modules printed 6 PINNED lines, the lexicon offender pin read 1215 PINNED, and each of the five
readers read its root as the spec's site table says. No function, flag or verb is minted, and no shell
file, shared record, budget row or watched kickoff path is written.

The plant was first run with S6 alone in place, before S1 to S5: it printed `MISSED` with one clause per
reader, each the answer the spec's plant table names as today's, so the arm is seen red here; the close
still owes its RED-first observation on the staged break. The acceptance read the spec marked UNVERIFIED
for the budget scratch is reached: the position line names the acceptance record under the records root.

Owed to the close: every leg the spec's gates list names; and RED-first, on its one `New arm:` line, the
`driver-root-readers` plant with S1 to S5 reverted, owed to print `MISSED` naming each reader.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/budget.py --fixture --plant driver-root-readers` with the five readers S1 to S5 rewrote
restored from the commit before the pass exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-116
- AC1 — `disposed continue` — `python tools/loop/budget.py --fixture --plant driver-root-readers` exited 0, its `ending` line ending `disposed continue` and its last line `loop: fixture · driver-root-readers · held`.
- AC2 — `-acceptance-` — the same run's `position` line read `records/builds/tFix/README.md@` and `records/builds/tFix/build/2026-01-01-build-TOOL-tFix-1-acceptance-1.md@`, its reason the unlanded parent, not a missing README.
- AC3 — `tPar` — the same run's `parents` line printed the one key `tPar`, and the plant's check that its text holds `phase: ABORTED` held.
- AC4 — `upstream` — the same run's `upstream` line printed `records/builds/tFix/build/2026-01-01-build-TOOL-tFix-1-upstream-1.md`, and the plant's check that the file exists held.
- AC5 — `records root:` — the same run's `builds-dir` line printed `records/builds · none` and its `builds-dir disagree` line `none · records root: .unattended.conf says records, .memory-tree.conf says memory — the driver writes under records`.
- AC6 — `reader call` — `derive_conf_reads` over the four modules answered no `reader call` row (`loop_parents.py` answers its one pre-existing `conf name`, a plant description), and the grep printed 2 PINNED lines, both inside `tools/loop/loop_lib.py#resolve_memory_root_source`.
- AC7 — `resolve_memory_root` — the grep named it in the `loop_parents.py` module docstring and in the `read_withdrawn_parents` paragraph of `tools/loop/README.md`, each as the builds folder's source, and `git grep -n "records root:" -- help/loop.md` printed the actor-list sentence.
