# PLAY-dOrderedCharter-25 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-25

Each line is a probe this pass ran with the pass applied, at rev-7 of the spec: `gov_tag.py --fixture --plant <case>`
building each case's scratch repository, `gov_tag.py bundle` and `gov_tag.py check --only` over this tree, or a
`python -c` and a `grep`. The `tags bundle selftest` leg, the `tags (the resolver's checks)` leg, the `edges` leg,
the policy legs, the codebase-map gate, the merge bar and the `New arm:` line's RED-first observation are the main
loop's at the close: a role agent runs none of them. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-25
- AC1 — `bundle-manifest` — exit 0: the first line `tags: bundle · practice.land · tools/corekit/core.tags:1-1 · tag · 14 bytes`, then `members · part-of · 2 rows` (the guide section's `3-6` and the record's `whole`), `instructions · instructs · 1 row`, `cites · 1 row` at the guide's `7-9`, every row `path:span · type · bytes`; `refs practice.land` printed the one citation the cites row holds, and the plant said `cites equal to refs`
- AC2 — `bundle-fold` — exit 0: `fold: 21 rows printed of 50, folded [('tools/alpha/', 'cites', 30)]; --under tools/alpha/ listed 30 rows unfolded`, the fold row `tools/alpha/ · cites · 30 rows · ... · open with --under tools/alpha/`
- AC3 — `bundle-rows-values` — exit 0: `rows values: 20 -> 10 rows folded, 40 -> 21 rows folded, 80 -> 45 rows`, each value set by `--set tags.bundle-rows=<n>` over the 45-row bundle
- AC4 — `bundle-inline` — exit 0: `inline: 2 of 5 rows inlined, 140 of 200 bytes, every range whole True`; the third row (70 bytes) would pass 200 and stays a manifest row, and so does the fifth (33 bytes) that would have fitted after it
- AC5 — `bundle-mode-values` — exit 0: `manifest --inline rc=2` printing `tags.bundle is manifest, which refuses --inline`, `inline bare rc=2` printing `inlining needs its byte budget, --bytes <n>`, `inline --bytes rc=0` inlined, `both bare rc=0` with no content inlined, `both --inline rc=0` inlined
- AC6 — `bundle-unregistered-type` — exit 1: `tags: type-registered · memory/notes/site.md:1 · relates-to · is no type of edges.toml's closed set`, then `with part-of=practice.land: rc=0`; over this tree `check --only type-registered` printed `green · 8165 edge(s), 0 red`
- AC7 — `bundle-dangling-target` — exit 1: `tags: target-resolves · memory/notes/site.md:1 · instructs=practice.nosuch · resolves to no row of the tag index`, then `with instructs=practice.land: rc=0`; over this tree `check --only target-resolves` printed `green · 8165 edge(s), 0 red`
- AC8 — `bundle-empty-sections` — exit 0: `instructions · instructs · searched-empty` and `regions · not-installed: dTotalRecall's span extractors feed it; the fallback is the whole-file range each row names`
- AC9 — `tags.bundle` — the `tomllib` probe printed `[('tags.bundle', 'dOrderedCharter', True, True), ('tags.bundle-rows', 'dOrderedCharter', True, True)]`; `policy.py lists --check` exited 0, `green · 0 finding(s)`, after `lists --write` drained both names; `grep -x` over `unsummarised-keys.txt` found no line (this host's git grep has no `-x`); the `git grep` over `tools/playbook` printed both `read_policy_value` lines in `gov_tag.py`
- AC10 — `git grep -n -E '^gate-legs = \[.*"tags bundle selftest"' -- memory/map/features/playbook.md` printed the dossier's line 11; `grep -F "tags bundle selftest"` printed one line each in `subject-pins.tsv` (written by `govkit.py selfcheck --write`), the playbook `kit.toml` and `MAP.md` (after `gen_map.py --write`); `owed_rows.py --base HEAD` printed `0 rows owed since HEAD · 1 deferred`, the ceiling-evidence row left to the close
