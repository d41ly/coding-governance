# PLAY-dOrderedCharter-29 deviation 293 — the work-order door's glob also matches briefs, which print as frozen

**Serves:** deviation PLAY-dOrderedCharter-29

- **Departs from:** `PLAY-dOrderedCharter-29@rev-4` [Design]
- **Hand-off:** spec-to-code
- **Before:** the door list's design says each population is fixed against the landed writers, and the work-order glob is verified to match only rendered handoffs.
- **After:** the work-order row's population is `{memory_root}/builds/*/prompts/*-prompt-*[0-9]-[0-9]*-[a-z]*.md`, the `<id>-<n>-<role>` shape `tools/roles/handoff.py#derive_prompt_name` writes. Older briefs share that shape, so the glob matches them too; each is a node without the `<!-- gov:handoff ` witness, and since every one sits under the builds folder it is a frozen record the `one-door` arm prints and never reds, the rule the spec's non-goals give every arm.
- **Cause:** builder discovery
- **Reason:** the spec's own re-read says no filename glob tells a handoff from a brief, so the verification it asks for cannot pass; a probe of candidate globs over the tree found none that matched every marked handoff and no brief. The frozen-record rule keeps the real door list green, which the door criterion asks, while a hand-written work order outside the builds folder still reds.
- **Evidence:** the `one-door` arm over the real door list before the leg was registered printed the work-order population with every unwitnessed node as frozen, the pending rows for record, trailer and act, and exited 0; the `door-unlisted` plant, its population outside the builds folder, exited 1 naming the file.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-29
