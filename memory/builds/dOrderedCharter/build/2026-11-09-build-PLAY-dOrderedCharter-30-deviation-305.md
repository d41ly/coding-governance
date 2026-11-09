# PLAY-dOrderedCharter-30 deviation 305 — the tools practice and the wiring guide name the charter's tools section by its heading

**Serves:** deviation PLAY-dOrderedCharter-30

- **Departs from:** `PLAY-dOrderedCharter-30@rev-6` [Scope]
- **Hand-off:** spec-to-code
- **Before:** the scope changes the catalogue's two retired rows, their foundation entries and the readers of those tags, and leaves the `practice.tools` row and the rest of `WIRE-INTO-PROJECT.md` as they are.
- **After:** the `practice.tools` line reads "Rely on the tools under this charter's 'Tools to rely on' before re-deriving anything they answer, ..." where it read "the tools in section 3", and the wiring guide's codebase-map bullet names the charter's "Tools to rely on" section where it named the charter's section 3; `AGENTS.md` is re-rendered with both practice changes.
- **Cause:** builder discovery
- **Reason:** unit 2 retired the charter's numbered sections, and the build brief for this unit names these two readers in its files touched as still citing one, to be named by heading in this pass.
- **Evidence:** `AGENTS.md`'s tools heading is "Tools to rely on"; the re-render rewrote the `[tools]` line and the practice region alone, and the render's check then read the region as matching a fresh render.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-30
