# PLAY-dOrderedCharter-26 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-26

Each line is a probe this pass ran with the pass applied, at rev-7 of the spec: `positional.py`'s own CLI
from the repository root, `gov_tag.py --fixture --plant <case>` building each plant's scratch repository,
or a `python -c` and a `grep`. The `tags positional selftest` leg, the `tags (the resolver's checks)` leg,
the policy legs, the codebase-map gate, the merge bar and each `New arm:` line's RED-first observation are
the main loop's at the close: a role agent runs none of them. This record cites no code line, so the arm
it describes reads nothing new in it.

**Evidences:** PLAY-dOrderedCharter-26
- AC1 — `positional-seed` — exit 0: `seeded 3 file:line rows, and joined 1 section rows the list lacked`, then `seed: the list holds every expected row and no other`, `a second seed: rc=1` naming the three file:line rows it holds, and the fixture's `check` green over 3 file:line and 2 section rows. OWED to the main loop: the `tags positional selftest` arm's RED-first observation
- AC2 — `positional-new` — exit 1, two reds, each `tags: positional · unlisted · memory/guides/ALPHA.md · <ref> · <remedy>`: the planted code citation naming `positional.py pin memory/guides/ALPHA.md`, and the build method's `M9` naming the alias row's tag; then `without the plants: rc=0`
- AC3 — `positional-stale` — exit 0 over every step: `removed: rc=1, stale named` (`stale · ... · positional.py shrink drops the row`), `shrink dropped 1 stale rows`, `after shrink: 1 rows, rc=0`, then a new citation planted: `shrink dropped 0 stale rows`, `a new citation planted: shrink left 1 rows, rc=1`
- AC4 — `positional-listed --set tags.positional=refuse` — exit 1, `tags: positional · listed · ... · tags.positional is refuse` for the listed citation and the listed `M5`, `tags: RED · 2 red`; with no `--set` the same plant exits 0, `tags: green · 0 red`
- AC5 — `positional-new --set tags.positional=report` — exit 0, both unlisted references printed under `tags: positional · report · unlisted`, `tags: green · 0 red`
- AC6 — `positional-symbol` — exit 1, one red `symbol · memory/guides/ALPHA.md:17 · ... defines no ghost`; the record's ghost `symbol, frozen record, printed`; `8 symbol citations read, 1 red, 1 printed, 1 passed over at another suffix` (the `.toml` span), the defined Python, shell and JavaScript symbols resolving; the `script:` usage id in a comment, the `purpose-source` value in a `.toml`, the `.py` string and the doubled-backtick span read nothing; `without the live ghost: rc=0`
- AC7 — `positional-pinned` — exit 1: `5 pins read, 2 red, 1 printed`, the pin at a real blob and the pin at a commit resolving, the unknown oid red as `00000000 is missing` and the line past the blob's end red as `holds 3 lines, not line 9`, the frozen record's unknown oid `pin, frozen record, printed`; `without the live bad pins: rc=0`
- AC8 — `positional-pin` — exit 0: `pin rewrote the citation to the blob at HEAD; check: rc=0`, the citation rewritten to the fixture code file at its 8-hex blob, and `pin outside the repository: rc=1, nothing written` after `pin refused · ... is no file inside ...`
- AC9 — `git grep -n "@<sha8>:"` over the five producer sources prints the pinned form in each: the review protocol template, the diff reviewer's role, the tier2-review template, and both drift-audit templates; their rendered copies carry the same lines
- AC10 — `positional.py seed` over the tree printed `seeded 36786 file:line rows, and joined 4 section rows the list lacked`; `positional.py check` then exits 0: `shrink-only · 36786 file:line and 1992 section rows listed, 0 unlisted, 0 stale; 30 pins read, 0 red, 30 printed; 6 symbol citations read, 0 red, 6 printed, 10 passed over at another suffix`, `green · 0 red`; every one of the 1992 rows `gov_tag.py --list-positional` prints is on the list. The tree moved since the spec's pin, so the seed joined 4 section rows where the spec counted 2; its figure is DERIVED at observation. OWED to the main loop: the `positional` arm's RED-first observation inside the `tags (the resolver's checks)` leg
- AC11 — the `tomllib` probe prints `[('dOrderedCharter', True, True)]`; `policy.py lists --check` exits 0, `green · 0 finding(s)`; `grep -c -x -F tags.positional` over `unsummarised-keys.txt` counts 0 (this host's git grep has no `-x`); `read_policy_value("tags.positional", root)` is one line of `positional.py`. The mirror `.governance/policy.json` is regenerated in the commit after this pass
- AC12 — `git grep -n -E '^gate-legs = \[.*"tags positional selftest"'` over the playbook dossier prints its line 11, the `gate-legs` claim; `MAP.md` prints `| tags positional selftest | playbook |` after `gen_map.py --write`
