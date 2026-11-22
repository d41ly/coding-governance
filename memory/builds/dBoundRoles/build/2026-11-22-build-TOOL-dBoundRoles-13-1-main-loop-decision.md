**Serves:** journal TOOL-dBoundRoles-13

# TOOL-dBoundRoles-13 — the main loop's decision over the first builder's divergence

Run `wf_44b97275-54b`, started at `c5f15de0f` on rev-6, wrote nothing and committed nothing. No spec writer can be
spawned directly on this run (the session's spawn guard predates TOOL-dBoundRoles-17's `item=`), so the main loop
decides each returned item by M3 as a delegated resolution, and the next builder builds them under the one deviation
record its write set names. widens: none · relaxes: none.

1. `tools/playbook/instruction_units.py` joins the write set: the pass re-pins the handed cases of `ORDER_CASES`
   (their bytes and task-sha) for the fact line, and the close runs the `instruction units selftest` leg.
2. Rollout term 4 takes the trim route the spec already allows where the unattended Skill render can lose the added
   bytes without dropping a rule. Only where it cannot does the pass raise the size row, and the main loop then commits
   the `memory/DECISIONS.md` row, whose text the builder returns, in the records commit that follows the merge.
3. AC1's arm calls `render_handoff` with the `task:` keys filtered, as arm 22 of `tools/roles/adopt-roles.test.sh`
   does, since the roles-kit fixture holds no kickoff checker.
4. The fact-class helper takes the root as well as the key, `derive_fact_class(key, root)`, reading a record's status
   header and the memory root from it. A typed argument's key hashes the fixed argv `--input`, NUL, `<name>`, so a
   claimed fact is told from a witnessed command run by its argv hash.
5. An explicit `--card <path>` is keyed by its repository-relative path when it sits inside the repository, else by
   `card/<stem>`.
6. The builder re-grounds the moved citations in `tools/roles/handoff.py` and `tools/hooks/agent-cap.js` at HEAD; the
   spawn step goes after TOOL-dBoundRoles-6's role-sha step and before the description step.
