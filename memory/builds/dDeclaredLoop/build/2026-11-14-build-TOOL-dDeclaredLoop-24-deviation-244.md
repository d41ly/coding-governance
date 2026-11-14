# TOOL-dDeclaredLoop-24 deviation 244 — the plants' scratch holds the kits the check reaches, not the whole tool root

**Serves:** deviation TOOL-dDeclaredLoop-24

- **Departs from:** `TOOL-dDeclaredLoop-24@rev-5`
- **Hand-off:** spec-to-code
- **Before:** the spec's design section "The plants": `--fixture --plant <case>` builds a scratch repository holding a copy of this working tree's tool root and the conf files the kits read.
- **After:** the scratch holds a copy, from this working tree, of the kits the check reaches, loop, playbook, memory-tree, policy and roles, each at its place under the tool root, and a memory-tree conf naming its memory root; `check --selftest` builds that scratch once and resets it to its commit before each plant (`tools/loop/loop_items.py#build_scratch_tree`, `tools/loop/loop_items.py#run_fixture`).
- **Cause:** builder discovery
- **Reason:** on node d a `git add` of the whole tool root into a scratch repository took 26 s, PINNED 2026-11-14, so one scratch per plant would put the leg's plants past its ceiling; the five kits commit in about 3 s, PINNED 2026-11-14. Every module the check and its probes run reads the same working-tree bytes either way, and a later change that reaches a sixth kit finds it absent in the scratch, where its plant exits 2 or fails, never passes.
- **Evidence:** `memory/builds/dDeclaredLoop/build/2026-11-14-build-TOOL-dDeclaredLoop-24-1-acceptance-ledger.md`, its timing paragraph.
- **Risk:** editorial
- **Approver:** author, the builder of TOOL-dDeclaredLoop-24, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-24
