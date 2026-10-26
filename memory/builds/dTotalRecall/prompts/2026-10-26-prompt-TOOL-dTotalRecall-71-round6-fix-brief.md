**Serves:** research TOOL-dTotalRecall-71

# Round-6 fix brief — dTotalRecall, the checks the round-6 promotions owe before their commit

The round-6 spec audit's disposal (`unattended-build.js` run `wf_004eef34-88f`) wrote the promoted specs
TOOL-dTotalRecall-71 to -76 under `memory/builds/dTotalRecall/spec/` and folded each hands-off edge into the spec it
names. Nothing of it is committed yet. Hygiene checks 2, 5, 12, 21 and 25 read clean. Clear every
`python tools/check-spec-tokens.py` hit below, changing nothing else in any spec's design.

- Units 71 to 76 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump.
- Your role admits the hygiene gate and the lexicon only. The files are staged in this worktree, so run the hygiene
  gate in place afterwards. Do not commit and do not run the build-index generator.

## F1 · paths in acceptance criteria that do not exist at HEAD

In §6 cite a file this build or a parent will CREATE by its basename and keep its full path in §2, §4 and Files
touched. A fixture's example path, and a path spelled inside a backticked Python one-liner, read as untracked paths:
describe the fixture path in prose, and move a one-liner that names a path into a command that takes the path as an
argument, or cite it by basename. The hits:
- unit 73: the one-liner `print(tree_lib.resolve_kept_registration(pathlib.Path('../..').resolve()).home)"`,
  `memory/project/census-kept-paths.txt`, `docs/memory/project/census-kept-paths.txt` (a fixture example)
- unit 76: `root>/project/census-kept-paths.txt`, `docs/memory/project/census-kept-paths.txt` (fixture examples),
  `tools/memory-tree/record_causes.py`, `tools/lib/legacy_ledger.py`, the one-liner `json.load(open('tools/gate-legs.json'))`

## F2 · a suite named as an acceptance observation

Unit 76 names `tools/govkit/selftest.py` in a criterion. A suite is not an acceptance observation: observe the checker
on a staged break or a fixture of the unit's own code, and move the suite to a `New arm:` line in §7.

## F3 · a guarded leg missing from §7

Unit 76's §4 Files touched names `tools/gate-lint/legacy_ledger.py`, which trips the guard of leg
`shell-hygiene selftest`; add it to unit 76's §7 leg line.

## Return

The list of files you edited, one line each on what changed, and the last line of the hygiene gate run.
