# PLAY-dOrderedCharter-54 deviation 542 — the spec cites the method's spec-set section by its alias tag

**Serves:** deviation PLAY-dOrderedCharter-54

- **Departs from:** `PLAY-dOrderedCharter-54@rev-3` [Non-goals]
- **Hand-off:** spec-revised
- **Before:** the Non-goals bullet on a help page and fork F6 cite the build method's spec-set section by its bare section code.
- **After:** both cite it as `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`, the alias row's tag, and nothing else in the spec moves.
- **Cause:** builder discovery
- **Reason:** the tags check reds a bare positional citation of a method section in tracked text and names the alias tag to cite; a CLOSED spec is frozen, so the citation is replaced in the pass that closes it, at the main loop's direction.
- **Evidence:** the tags check's positional row named this spec, the bare citation and the alias tag, the only tag red in the tree before this pass.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-26
