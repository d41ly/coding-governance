# PLAY-dOrderedCharter-40 deviation 402 — the two help pages the doc namespace's new source stales

**Serves:** deviation PLAY-dOrderedCharter-40

- **Departs from:** `PLAY-dOrderedCharter-40@rev-5` [Design]
- **Hand-off:** spec-to-code
- **Before:** the files touched are the instruction manifest, the reference declaration, the tag index, the namespace registry, the tag resolver and the playbook adopter, and no page under help/.
- **After:** the pass also updates help/tags.md, whose `doc` row now names the document registry's rows and each reference row's `registry` tag, and help/concepts/instruction-layer.md, whose units section names gov's first units and whose reference-pages section names each row's `h1` and the registry tag the resolver reads at that row.
- **Cause:** builder discovery
- **Reason:** the charter's docs rule holds a user-facing change open until its page under help/ is current, and once the `doc` namespace reads the reference declaration and its rows carry `h1`, both pages describe the namespace and the declaration as they stood before this pass.
- **Evidence:** read against the pass's design before the edit, help/tags.md's `doc` row named only the charter, the guides and the two memory documents, and the concept page named a row's registry, reader and page and nothing else.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-40
