# Brief — aIndexedAnchor: the anchor gate reads the tree being committed

**Serves:** research TOOL-aIndexedAnchor-1

The prompt arrived as the first message of a session started from another session, which found the red while
landing aTemperedLane. Its task paragraphs are quoted below.

## The prompt

> `test_anchor_resolves_at_head` in `tools/codebase-map/test_codebase_map.py` (and its `.template.py` twin), added by TOOL-dTotalRecall-125 S4, reds in pre-commit on an honest merge of `origin/main` into a branch.
> Cause: `load_map_tree` reads the dossiers from the working tree, which already holds main's new `[paths].symbols` anchors. `map_diff.read_anchor_hashes(root, commits, tree, map_rel)` then resolves them at `HEAD`, which during a merge commit is the branch's old tip, where main's new definitions do not exist yet.
> Seen 2026-11-28 merging origin/main 9dcc07a99 into `branch/redfix-lane-generated-4a0972`. Red: `lexicon: tools/lexicon/extract_code.py::extract_text` and `::read_defs_at`, both defined at origin/main and in the staged tree. That session committed the same tree with origin/main as first parent instead, as `dbcf84d4f`.
> Done means:
> - The check resolves anchors against the tree being committed (the index under pre-commit, `HEAD` elsewhere), or otherwise reads the dossier and the definitions from one source.
> - One arm reproduces the merge case, seen red on the current code and green after.
> - A rename that really drops an anchored definition still reds.
> - Run through `/session-kickoff`, with a spec first; it lands via `bash tools/push-main.sh`.

## The brief

### Goal
The anchor gate resolves each `[paths].symbols` key at the index, the tree the next commit carries, so a merge
commit's pre-commit grades the merge and not the branch's old tip.

### Items
1. One reader in `map_diff.py`, `read_unheld_anchors(root, tree, map_rel)`, answers `<feature>: <key>` for each
   anchor the index defines no such name for, or None on a shallow clone; the gate and its template twin
   assert on it. The gate's name says HEAD, so it is renamed (`memory/map/generated/symbols.json` names it).
2. A selftest arm in `tools/codebase-map/selftest.py`, in the real-git fixture style of
   `test_anchored_dossier_staleness`: a base commit anchors `a.py::f`; one branch adds `def h` and the key
   `a.py::h`; the other commits an unrelated file and runs `git merge --no-ff --no-commit`. The reader over the
   working-tree dossier answers `[]`; after a staged rename of `h` to `h2` it answers `["x: a.py::h"]`; after
   that merge is committed it still does.

### Acceptance
The new arm, seen red with the reader at `HEAD` and green at the index; the rename half red in both.

### Gates
`codebase-map coverage + freshness`, and every leg the spec's files trip.

### Non-goals
`map_diff.py --stale-dossiers`, which keeps reading at HEAD; `load_map_tree`; the pre-commit hook; any lexicon
or aTemperedLane file.

### Limitations
The template twin stays byte-identical to the gate. On a clean tree the index is HEAD's tree, so the bar's
verdict there does not move. Pre-commit runs the gate as leg `codebase-map coverage + freshness`
(`tools/gate-legs.json`, precommit argv `test_codebase_map.py --precommit`) through `run-gates.sh --precommit`,
after `.githooks/pre-commit` unsets `GIT_INDEX_FILE`, so its git reads the repository's own index, which holds
the merge result.

### Reuse
`map_diff.read_anchor_hashes(root, commits, tree, map_rel, head="HEAD")` already takes the revision as `head`
and feeds `f"{rev}:{path}"` to one `git cat-file --batch`; `head=""` spells `:<path>`, the index's stage-0 blob,
so the fix passes that rather than adding a blob reader. The arm's staged red is the reader at `head="HEAD"`,
which makes its merge half name `x: a.py::h`. Recall answered nothing
inside its bound. Recall terms used: anchor symbols paths.symbols read_anchor_hashes HEAD index pre-commit merge
dossier dTotalRecall-125.

## Drawn from the session

> `load_map_tree` reads the dossiers from the working tree, which already holds main's new `[paths].symbols` anchors.
— the session that started this one, 2026-11-28

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: the starting session's task is the go: "Run through `/session-kickoff`, with a spec first; it lands via `bash tools/push-main.sh`."

## route
- build: aIndexedAnchor
- unit: TOOL-aIndexedAnchor-1 · spec memory/builds/aIndexedAnchor/spec/2026-11-28-spec-TOOL-aIndexedAnchor-1.md
- brief: memory/builds/aIndexedAnchor/prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-1-brief.md
