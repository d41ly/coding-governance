**Serves:** research TOOL-dFairHearing-1 TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18

# Token-fix brief — the spec-token check over the first spec pass

Fix the 14 hits `python tools/check-spec-tokens.py` reports over the staged dFairHearing specs, so it exits 0, changing nothing else.

- Each `[path]` hit is a backticked path-shaped token in a §6 Acceptance criterion that `git ls-files` does not track. Cite a file the build run will create, a `rev:path` or an example literal by BASENAME, or without a slash, in §6; full paths stay in §2 and §4, which the join does not read. Correct a wrong path: `tools/gotchas.py` is `tools/memory-tree/gotchas.py`, and `{prefix}/unattended/unattended.sh` is `tools/unattended/unattended.sh`.
- The `[handoff]` hit: TOOL-dFairHearing-1 hands `parse_known_set` to TOOL-dFairHearing-18, whose spec never names it. Name it in unit 18 where it reads the known-set file, or correct unit 1's bullet.
- The specs are uncommitted at rev-1 and unaudited, so edit them in place with no rev bump.
- Do not commit, do not stage, and do not run the build-index generator. Re-run the check, and report its exit code and its last line.

## The hits, verbatim

- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md [path] `6cfd21619:memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-12.md [path] `3708a705:tools/workflows/review_replay.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-12.md [path] `b0fe68f30:no/such/file.json` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-14.md [path] `tools/workflows/replay_scorer.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-14.md [path] `tools/workflows/replay_scorer.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-15.md [path] `tools/gotchas.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md [path] `{prefix}/unattended/unattended.sh` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md [path] `tools/workflows/replay_scorer.py` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md [path] `extract_tag_ref('memory/x.md:[walk-table]` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md [path] `('memory/x.md',` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md [path] `extract_tag_ref('C:/r/x.md:[a]` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md [path] `('/r/x.md',` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md [path] `tools/workflows/lenses.toml` — not tracked by git ls-files
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md [handoff] `TOOL-dFairHearing-1>TOOL-dFairHearing-18:parse_known_set` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
