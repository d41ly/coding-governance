# PLAY-dOrderedCharter-47 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-47

Each line is a probe this pass ran with the pass applied, at rev-3 of the spec: `gov_tag.py --fixture
--plant positional-forked-before` building its scratch repository, a `python -c` over that run and over
`positional.read_grandfathered`, or `positional.py check` from the repository root. The `tags positional
selftest` leg, the `tags (the resolver's checks)` leg, the gates the spec's section 7 names, the merge bar and
the `New arm:` line's RED-first observation are the main loop's at the close: a role agent runs none of
them. This record cites no code line, so the arm it describes reads nothing new in it; the fixture's
citations are written here as the cited file and its line number.

**Evidences:** PLAY-dOrderedCharter-47
- AC1 — a `python -c` reading `L` through `tree_lib.read_adding_commits` prints `L fe22fcf80a26dfa9d942af3e27b49b3db4371847 matches git log tail -1: True` against `git -C tools/playbook log --diff-filter=A --format=%H -- positional.py | tail -1`; `read_grandfathered` over the 37 specs of this build dated 2026-10-23 returns all 37 (`missing: []`); the descendant set holds 4 commits and shares 0 with `git rev-list L^`. `positional.py check` over the tree stays `0 unlisted, 0 grandfathered, 0 stale`, `green · 0 red`
- AC2 — `positional-forked-before` — exit 0: after the side branch's merge `positional — grandfathered: memory/builds/x/build/record.md` naming `x.py` line 1 `(added in 4e877f32, before the check)` and `tags: green · 0 red`; the record written after the merge reds as `tags: positional · unlisted · memory/builds/x/build/after.md` naming `x.py` line 2, `tags: RED · 1 red`; the plant's line `the pre-fork record: rc=0; a record after the merge: rc=1; ...`. With `read_grandfathered` patched to the base rule (grandfathering nothing) the plant exits 1, `the pre-fork record: rc=1`. OWED to the main loop: the arm's RED-first observation in the `tags positional selftest` leg
- AC3 — the same plant moves the pre-fork record to `tools/notes.md` on its own side branch and merges it: `tags: positional · unlisted · tools/notes.md` naming `x.py` line 1, `the pre-fork record moved under tools: rc=1`. With `read_grandfathered` patched to grandfather every path, not only the records, the plant exits 1, `moved under tools: rc=0`. The four new selftest rows each match that run's exit and output in a `python -c` over `SELFTEST_ROWS`
