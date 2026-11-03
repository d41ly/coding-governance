# PLAY-dOrderedCharter-10 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-10

Each line is a probe this pass ran in the worktree at 5c76b68a0 with the pass applied, or a plant
`gov_tag.py --fixture` built in its own scratch repository under the temp root. The `tags` leg over the
tree, the playbook render selftest, the lexicon selftest, the layer check, the resolve-python parity rows
and every `New arm:` line's RED-first observation are the main loop's at the close: a role agent runs
none of them.

**Evidences:** PLAY-dOrderedCharter-10
- AC1 — `derive_namespace_state` — a probe importing `tag_index.py` with its own SQLite file under the scratch root, running `derive_context`, `load_view`, `derive_namespace_state`, `check_resolves` at `charter-only`, `check_retired` and `check_owned` over the tree, printed ten namespaces `{'doc': 117, 'kind': 0, 'kit': 30, 'layer': 12, 'level': 0, 'practice': 0, 'principle': 0, 'reader': 3, 'repo': 0, 'unit': 0}`, `layer rows 12 layer count 12 equal`, `kit tags 30 registry 30 only-index [] only-registry []`, `resolves 0 retired 0 owned 0 sum 0` and `file names 45 graded 9 unresolved 0` (43 `kit.toml` spans at the base, two more this pass's own pages add); `check_tag_shape` graded 162 tags with 0 reds and `check_namespace_joins` 0 reds. OWED to the main loop: the `tags` leg over the tree and its `layer.Memory` RED-first arm
- AC2 — `--plant bad-ns` — exit 1, `tools/corekit/instructions.toml:2 · shape · step.build · namespace 'step' is not registered`
- AC3 — `--plant bad-seg` — exit 1, `tools/corekit/core.tags:5 · shape · layer.Memory · segment 'Memory' is outside [a-z0-9][a-z0-9-]*`; `--plant long-tag` exit 1, `· over 64 bytes (66)`
- AC4 — `--plant ns-word` — exit 1, `tools/corekit/core.tags:5 · shape · practice.repo.x · first segment 'repo' is a namespace word`; `--plant none` exit 0, `tags: green · 0 red`, over `practice.land` and `practice.memory`
- AC5 — `--plant escaped-word` — exit 1, `tools/playbook/namespaces.toml · shape · namespace row 'a.b' is outside seg, so no tag is graded against it`, and the planted `a.b.c` red as `namespace 'a' is not registered`
- AC6 — `--plant unregistered-cite` — exit 1, ``memory/guides/ALPHA.md:11 · join · `layer.nowhere` is cited and undeclared in layer``; `--plant dead-selector` exit 1, ``tools/playbook/readers.toml:5 · join · `reader.ghost` is declared and selects no unit``, its second half without `reader.ghost` printing `tags: green · 0 red` and `rc=0` with `join layer · 3 unused, a descriptor (not red): layer.memory layer.memory.lexicon layer.memory.recall`; `--plant file-name` exit 0 with `1 file names not graded`, its second half with no tracked `kit.toml` printing ``· unresolved · `kit.toml` names no row`` and `rc=1`
- AC7 — `--plant empty-ns` — exit 0, `tags: join kind · unarmed: its source declares nothing, so neither direction is graded`, the cited `kind.x` counted as `tags: unarmed kind (1 not graded)` and never red
- AC8 — `lexicon.py --tags` — the criterion's `printf` pipe exited 1 printing `lexicon: tag practice.repo.x · first segment 'repo' is a namespace word` and `2 graded, 1 refused`, no line naming `layer.memory`; a kit copy beside a fixture registry of `practice`, `repo`, `layer` and `a.b` refused only `practice.repo.x` of four names; in a scratch copy of `tools/playbook/` and `tools/memory-tree/` with no lexicon kit, `--plant none` printed `slot point.instruction.name-check · not-installed: the shape check stands alone` and exited 0, and `--plant ns-word` exited 1 on the shape check alone. OWED to the main loop: the lexicon selftest's new `--tags` arm and its RED-first observation
