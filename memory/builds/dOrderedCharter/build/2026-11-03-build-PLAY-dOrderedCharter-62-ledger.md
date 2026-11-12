# PLAY-dOrderedCharter-62 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-62

Each line is a probe this pass ran in the worktree or under the run's scratch path, and what it
printed. The layer leg, the plant table in `adopt-playbook.sh --selftest`, the resolve-python leg's
parity and idiom-ban arms and the `New arm:` line's RED-first observation are the main loop's at the
close; a role agent runs none of them.

**Evidences:** PLAY-dOrderedCharter-62
- AC1 — `--fixture --plant flat-slotted --list` — exit 0, `layers: edge tools/flatgo:2 · shell · flatkit -> expkit · allowed` and `1 allowed, 0 red; 0 contract red(s)`; a scratch copy with `parts = {o.get("part") for o in src["optional"]}` restored printed the same edge `· red` and exited 1
- AC2 — `--fixture --plant flat-literal` — exit 1, `layers: RED descriptor tools/govkit/entries/flatkit.kit.toml's optional row part 'tools/flatgo' spells the tool root literally: spell it {prefix}/flatgo`, the edge itself still allowed
- AC3 — `grep -n 'replace("{prefix}' tools/playbook/check_layers.py` — printed only the two lines inside the `resolve_prefix_token` block; the `sed -n '/^# >>> resolve_prefix_token/,/^# <<< resolve_prefix_token/p'` extracts of `tools/lib/resolve_prefix_token.py` and `tools/playbook/check_layers.py` hashed identically under `md5sum`
- AC4 — `diff` — the `layers: edge` lines of `check_layers.py --list` saved before the first edit (40) against those after the pass: no output; the summary still reads `0 allowed, 40 red; 0 contract red(s)`
- AC5 — `grep -n '{prefix}/<file>' tools/playbook/README.md tools/playbook/check_layers.py` — printed the README's `optional` paragraph and the docstring's register paragraph
