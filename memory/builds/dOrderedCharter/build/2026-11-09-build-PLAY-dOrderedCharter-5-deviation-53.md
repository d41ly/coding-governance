# PLAY-dOrderedCharter-5 deviation 53 — both work-order cases re-pinned, the code slot's absent line included

**Serves:** deviation PLAY-dOrderedCharter-5

- **Departs from:** `PLAY-dOrderedCharter-5@rev-6` [Scope (IN)]
- **Hand-off:** spec-to-code
- **Before:** S3 re-pins the `every slot` case of `ORDER_CASES` in `tools/playbook/instruction_units.py#arm_work_order` to the bytes the unranked render prints, and points its slot swap at the `opening` and `reads` slots.
- **After:** both cases are re-pinned, and the shared `ORDER_HEAD` opening's `Not supplied` line now names `input:code` beside `input:spec`. The swap moves `opening` and `reads` as S3 says.
- **Cause:** builder discovery
- **Reason:** at this branch's head, before this pass, both cases already differed from what the render prints: `PLAY-dOrderedCharter-27` gave every role an optional `input:code` key, so the absent-inputs line names it too and both task hashes moved. Re-pinning one case would leave the `instruction units selftest` leg red on the other.
- **Evidence:** a hand-run copy of the arm's fixture, with the roles kit alone in a fresh repository under the system temp folder, printed `DIFFERS` for both cases over `git archive HEAD` of the kits. Over the pass applied it printed `PINNED` for both, and the opening-and-reads swap moved the bytes.
- **Risk:** none
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-27
