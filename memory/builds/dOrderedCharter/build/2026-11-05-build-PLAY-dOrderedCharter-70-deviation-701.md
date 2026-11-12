# PLAY-dOrderedCharter-70 deviation 701 — the four withheld lists print as `project-owned` rows, as built

**Serves:** deviation PLAY-dOrderedCharter-70

- **Departs from:** `PLAY-dOrderedCharter-70@rev-1` [Acceptance criteria]
- **Hand-off:** spec-to-code
- **Before:** AC14 says that when `python tools/govkit/govkit.py shipped` runs, no row names any of the four withheld files.
- **After:** `shipped` prints one `playbook-render	project-owned` row for each of the four, and no `engine` row names any of them.
- **Cause:** design defect
- **Reason:** the verb prints every descriptor survivor with its role, `project-owned` included, so the `[[files]]` block S10 and the Design section require is the row AC14's sentence forbids; no build satisfies both as written. AC14's Red-when is an adopter still receiving a file, and none does: `project-owned` is outside the landable roles. Deviation 671 of PLAY-dOrderedCharter-67 is the same reading of the same verb.
- **Evidence:** `tools/govkit/govkit.py#cmd_shipped` filters a role only under `--epoch`; before this pass `shipped` printed the four as `playbook-render	engine` rows, and `run-gates	project-owned	tools/run-gates/windows-only-legs.txt` is the precedent the Design section cites.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-70
