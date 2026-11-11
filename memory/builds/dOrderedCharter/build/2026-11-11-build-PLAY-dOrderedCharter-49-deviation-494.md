# PLAY-dOrderedCharter-49 deviation 494 — a serves trailer's targets are its comma-split value

**Serves:** deviation PLAY-dOrderedCharter-49

- **Departs from:** `PLAY-dOrderedCharter-49@rev-9` [Scope]
- **Hand-off:** spec-to-code
- **Before:** S26 reads a `serves` trailer value as edges only when `derive_target_fault` passes every target, the targets being the whitespace- or comma-split value the trailer adapter has always read.
- **After:** a `serves` value is graded on its comma-split targets, so a prose value fails the grammar on its spaces and is counted unread; every other trailer key keeps the whitespace- or comma-split read.
- **Cause:** builder discovery
- **Reason:** the grammar's native id form matches any bare word, so a whitespace split turns the prose `Pass: the whole build` into three well-formed targets and reads it as edges, the case S26 exists to stop; the comma split keeps a list of ids an edge list and leaves prose unread.
- **Evidence:** a probe of `tools/playbook/edge_grammar.py#parse_edge_target` read `the`, `whole` and `build` each as the `id` form, and the `prose-pass` plant read three edges from that value before the change and none after it.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-28
