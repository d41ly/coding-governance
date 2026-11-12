# PLAY-dOrderedCharter-34 deviation 348 — update's relay of the delta lines is observed by govkit's own scratch adopter

**Serves:** deviation PLAY-dOrderedCharter-34

- **Departs from:** `PLAY-dOrderedCharter-34@rev-10` [Acceptance criteria, AC8]
- **Hand-off:** spec-to-code
- **Before:** AC8's second half runs `govkit.py update` on the composition fixture's scratch adopter and finds the heading and the same lines the fixture's `delta` plant prints.
- **After:** the composition fixture's `delta` plant prints the six state lines and the widening from `render_delta_report` over its tree, and the relay is observed by the govkit selftest arm the section on gates declares: a scratch gov and adopter whose regenerate prints the six state lines, a widening and one foreign line, `update` relaying the seven under `govkit update — composition: 7 line(s)` and dropping the foreign one.
- **Cause:** builder discovery
- **Reason:** the composition fixture builds a bare repository with no install receipt, and `update` reads a receipt and a gov checkout; the govkit selftest already builds that pair for every regenerate arm, so the arm reuses it rather than the fixture growing a second installer.
- **Evidence:** `tools/govkit/govkit.py#derive_composition_lines`, over the arm's seven lines and its foreign line, kept the seven and dropped the foreign one in a probe; the arm sits in `tools/govkit/selftest.py#check_update_safety`.
- **Risk:** low. The relay reads the regenerate's stdout, which is the renderer's in a real install; the arm's stand-in prints the renderer's exact widths.
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-34
