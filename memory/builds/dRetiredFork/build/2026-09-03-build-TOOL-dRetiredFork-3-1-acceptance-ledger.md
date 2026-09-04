# TOOL-dRetiredFork-3 — acceptance ledger

**Serves:** journal TOOL-dRetiredFork-3

**Evidences:** TOOL-dRetiredFork-3
- AC1 — `python3 tools/memory-tree/gen_build_index.py --check` — an indented key staged into `memory/builds/dPromptedSeam/README.md` produced `header present but unparseable — line 3: front-matter key is indented`, named the file, printed the header region, and exited 1; the header was restored after
- AC2 — `python3 tools/memory-tree/gen_build_index.py --check` — with that path carrying a waiver row and the index regenerated, exit 0 with `build-index: 1 header(s) tolerated by waiver` and 535 artifacts instead of 540, the tolerated build correctly dropping out
- AC3 — `python3 tools/memory-tree/gen_build_index.py --check` — a row naming `memory/builds/ghost/README.md` exited 1 with `1 row(s) name a path the tree does not track, so the exception outlived the header it excused`
- AC4 — `python3 tools/memory-tree/gen_build_index.py --check` — with the registry moved aside, exit 1 naming it `absent` and refusing to default it to empty
- AC5 — `python3 tools/memory-tree/gen_build_index.py --check` — a clean run prints `build-index: 0 header(s) tolerated by waiver` and then the unchanged `build-index: clean (540 artifact(s))`, differing from the pre-change output by exactly that one line
- AC6 — `tools/memory-tree/kit.toml` — the `stale-header-waiver` `[[hole]]` ships the file with its header and no rows, and its discharge probe exits 1 (UNARMED) against the empty registry rather than passing silently
- AC7 — `bash tools/memory-tree/check-memory-hygiene.sh` — exits 0 with `F:stale-header-waiver.txt` added to check 3's whitelist case in this same commit
- AC8 — `bash tools/check-kit-versions.sh` — exits 0 after the bump to 2.58 across all seven carriers
