**Serves:** journal TOOL-dBoundRoles-12

# TOOL-dBoundRoles-12 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `5e079419b`. The place probes built the placement fixture repository with
`tools/loop/placement.py#write_placement_fixture` under the host temp folder, wrote each return with
`tools/loop/placement.py#render_fixture_return` and ran `placement.py place --request 3f9c2a71d0e4 --return <file>`
there as a process; the verb probes ran `tools/roles/handoff.py check-return-file --role gov-orienter` over scratch
return files in this tree. No gate, suite or bar ran in the pass, and no plant ran through `--fixture`: the
`return-untyped` and `return-wrong-role` plants of `loop placement fixtures`, the arm the spec's `New arm:` line
declares, their RED-first observation and the legs its gate line lists are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-12
- AC1 — `return-untyped` — a return carrying `answers` and the placement lines and no `outcome` line exited 1 printing `placement: refused — return — outcome — a required field is absent`, and the request's `.placement` file did not exist; one reading `outcome: oriented` exited 1 naming the outcome as not `placed`, still no file; the same return with `outcome: placed` exited 0 printing `placement: placed — continue dLive` and the file held one block, with no `outcome` or `answers` line in it. OWED: the `return-untyped` plant and its RED-first observation, the `check-return-file` run removed from `place`, at the close.
- AC2 — `gov-researcher` — a valid return answering the fixture's `orders/gov-researcher.md`, whose marker reads `role=gov-researcher`, exited 1 printing `placement: refused — return — answers — the return answers a gov-researcher work order, orders/gov-researcher.md, not a gov-orienter one`; one answering `.memory-tree.conf`, a file with no marker, and one naming no work order each exited 1 naming the cause, and no block was written; re-pointed at `orders/gov-orienter.md` it exited 0 and one block was appended. Over this tree, a return answering a real builder work order under `memory/builds/aBatchedPacket/prompts/` exited 1 naming `gov-builder`, its marker read after the record's `**Serves:**` line. OWED: the `return-wrong-role` plant and its RED-first observation at the close.
- AC3 — `placement.py check` — `grep -n "placement.py check" SKILL.template.md` in `tools/roles/` names Stage 1's check step at `tools/roles/SKILL.template.md@0e735b14:51`, after its record step naming `placement.py place --request <content key> --return <file>` at `tools/roles/SKILL.template.md@0e735b14:50`; `bash tools/roles/adopt-roles.sh --scaffold` rendered `.claude/skills/build/SKILL.md`, which carries the same commands at `.claude/skills/build/SKILL.md@fb08557a:50-51` with the tool root `tools/` substituted.
- AC4 — `outcome` — `check_return("gov-orienter", "card: the session card\n")` returned `['outcome — a required field is absent']`, and over `outcome: placed` with `disposition`, `reason`, `evidence` and `observations` lines it returned `[]`, at base, since the template `TOOL-dBoundRoles-2` typed is unchanged.
- AC5 — `placement.py` — `grep -n "placement.py" help/roles.md` names the step S5 adds, `help/roles.md@db1ebc63:21-22`, step 2 of "How a task reaches an agent", the scout's placement return recorded with `placement.py place` and checked with `placement.py check`.
