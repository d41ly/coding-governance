# PLAY-dOrderedCharter-3 deviation 34 — the envelope plants build a small tree in gov's layout, and the gate reads each render

**Serves:** deviation PLAY-dOrderedCharter-3

- **Departs from:** `PLAY-dOrderedCharter-3@rev-12` [Acceptance criteria]
- **Hand-off:** spec-to-code
- **Before:** AC5 plants each defect in a scratch tree copied from gov; S5 has the gate compare each source's envelope lines with the registry's rendering.
- **After:** each plant writes a small tree in gov's layout, a charter whose Protocols line names one guide, that guide, the held build method, the charter's entry file, the registry, the renderer table and the held row's size row, and plants its defect there; the gate reads each registered document's own envelope, the render, and reads no source.
- **Cause:** builder discovery
- **Reason:** a copy of gov's tree carries gov's own state into a self-test: until the main loop re-renders the agent files after this pass, and in any tree whose agent files lag a render, every plant would read red before its defect is planted, so no plant could observe its own defect. A source is not read because the kit and dogfood parity legs already hold each source byte-equal to its render, so comparing the render compares the source, and the charter's and the agent files' envelopes are written by their renderers and sit in no source at all.
- **Evidence:** ten plants driven by a scratch probe of the arm functions, each in a throwaway repository, each printing `ok` for its green and red expectations; `envelopes --check --root .` over this tree before the agent re-render named the nine agent files and nothing else.
- **Risk:** loosening
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-3
