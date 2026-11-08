# PLAY-dOrderedCharter-72 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-72

Each line is a probe this pass ran at rev-2 of the spec, from the worktree root with the pass applied. No leg, suite
or `--selftest` ran in the pass, and the role hook refused `core.py fixture` as the `core selftest` leg. The ban's
counter was read out of `tools/check-install-prefix.sh` into the run's scratch and run over the files this unit
touched; it stands in for the `install-prefix (shipped surface)` leg until the close runs it. The fixture probes
import the playbook modules and run single plants or arms in a scratch repository under the host's temp folder.
This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-72
- AC1 — `0`, `0` — `git ls-files -- tools/playbook` holds no file opening `positional-`, and `git grep -n positional -- tools/playbook/kit.toml` prints no `include` row.
- AC2 — exit 0, the base's counts — `python tools/playbook/positional.py check` printed `36786 file:line and 1992 section rows listed, 0 unlisted, 0 grandfathered, 0 stale; 199 pins read, 0 red, 92 printed; 353 symbol citations read, 0 red, 13 printed, 10 passed over at another suffix` and `producers · 12 hits, 12 kept rows, 0 unlisted, 0 stale`, the same lines the command printed over this branch's tree before the move.
- AC3 — owed as the leg — the scratch copy of the ban's counter over the 19 tool files this unit edits printed `clean — 19 tracked file(s) graded, 0 kit-path spelling(s)`, where it printed 70 spellings on 69 lines before the edits; over the whole population, with no render excluded, its only spellings sit in files beside their `.template.` source, which the leg leaves out as renders. `install-prefix: clean` itself is the main loop's.
- AC4 — the grep clean, the arm owed — `git grep -nE 'tools/|memory/builds' -- tools/playbook/namespaces.toml` printed nothing; the `pending-source` plant printed `pending reader · {prefix}/playbook/readers.toml#why` before the source lands and `member reader.every (tools/playbook/readers.toml) lacks why` after, so the token resolves. `gov_tag.py check` over the tree is the `tags` leg, the main loop's.
- AC5 — the grep clean, the drift report owed — `git grep -n PLAY-dClosedLoop-1 -- tools/playbook/namespaces.toml tools/playbook/principles.toml` printed nothing; `drift_report.py --check` is a leg's argv, the main loop's.
- AC6 — owed — the scratch install of the playbook-render and memory-tree kits is the main loop's; a probe of `render_playbook.py#write_empty_lists` over a scratch target wrote `memory/project/positional-refs.txt` and `tools/playbook/core-pending.txt`, wrote nothing on a second call, nothing on a bare target, and the positional list alone under the project folder of a conf naming another memory root.
- AC7 — exit 0 — `bash tools/memory-tree/check-memory-hygiene.sh --only 3,9,13,14,15,16` exited 0 after `gen_build_index.py --write`; `grep '^PROJECT_REGISTRY_EXTRA=' .memory-tree.conf` names `positional-producers.txt` and not `positional-refs.txt`.
- AC8 — owed — `check-dead-paths.sh` and `check-method-carriers.sh` are legs' argv, the main loop's; `memory/project/method-carriers.txt` holds no `positional` row.
- AC9 — owed, with probes — the role hook refused `core.py fixture`; an in-process probe ran core's registry, unenforced, pending, kinds, practice, instruction-unit and bypass-never arms over `write_fixture`, `0` failed, and the instruction-units tags, priority, statements and extractor plants, `0` failed, with `run_ladder_terms` over the tree at `38 source(s) · 0 red`. The `positional-seed`, `positional-producer-new`, `positional-producer-stale`, `positional-forked-before` and `pending-source` plants printed the lines their selftest rows expect. `printf 'layer.memory\n' | python tools/lexicon/lexicon.py --tags` exited 0. The six selftests are the main loop's.
- AC10 — `0`, arm owed — `grep -c positional-producers tools/govkit/selftest.py` printed `0`; the moved arm's RED and GREEN are the main loop's, under the spec's `New arm:` line.
- AC11 — nothing, then `1` — `git grep -nE 'playbook/positional-|refs.txt beside' -- help tools/playbook` printed nothing, and `grep -c 'project/positional-' help/tags.md` printed `1`.
