# PLAY-dOrderedCharter-9 deviation 94 — the kit prefix, the render's refusals and a third reader of the old selector spelling, as built

**Serves:** deviation PLAY-dOrderedCharter-9

- **Departs from:** `PLAY-dOrderedCharter-9@rev-5 [Scope, Design]`
- **Hand-off:** spec-to-code
- **Before:** S2 names `<prefix>` the parent of the module's own kit directory and mints no reader of it; S3's readers clause names the readers of `select` in `edge_grammar.py`, `edges.toml` and `help/tags.md`; S4 renders a `fact` from "its probe or command" and says a refused policy read refuses the render, naming no exception; the design's files touched name seven files.
- **After:** `derive_kit_prefix` reads the prefix once from `git rev-parse --show-prefix` of the module's own directory, `tools` in gov, and `read_units` reads the manifests git tracks; every render refusal, a refused policy read, a command that fails and a source that is neither `policy:` nor `cmd:`, raises `UnitRowError` naming the unit, the source and the reader's line; a `probe:<name>` source refuses, since no probe registry exists to run it through; `resolve_extractor_module` serves any module of its own kit directory a registry's directory lacks; `tools/playbook/tag_bundle.py`'s bundle fixture writes its unit row's selector as `scope`; and the files touched also hold `tools/playbook/tag_bundle.py`, `memory/map/features/session-kickoff.md` and the generated map.
- **Cause:** builder discovery
- **Reason:** the prefix is a fact of the install, so a fixture tree under the host temp directory reads the same `tools` the gov tree does; S4's refusal needs one exception its callers catch, and the module's own is the one S2 mints; the production-readiness checklist runs a probe "only through the source's own registered probe", and none is registered; the bundle fixture's `select` row was a third reader of the old spelling, and its `bundle-manifest` plant counts one `instructs` row from it; the kickoff dossier still named the marker fallback unit 12 replaced, which the brief carries.
- **Evidence:** `instruction_units.py fixture --plant <case>` ran green for each of its twelve plants; `gov_tag.py --fixture --plant bundle-manifest` printed `instructions · instructs · 1 row`; `git grep -n -F 'select = [' -- tools/playbook/` printed nothing.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-9
