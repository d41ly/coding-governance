# PLAY-dOrderedCharter-53 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-53

Each line is a probe this pass ran, at rev-2 of the spec, from the worktree root with the pass applied:
`gov_tag.py --fixture --plant <case>` over its scratch fixture repository under the host temp directory,
one run per plant, and a `python -c` probe of the blame reader. The legs the spec's section 7 names, unit
26 S7's `tags positional selftest` over every `positional-*` plant, the merge bar, and the New arm's
RED-first observation (each of the three plants red under unit 47's per-file adding-commit rule) are the
main loop's at the close. This record cites no code line: the fixture's cited path is written `x.py` and
its line apart, where the plant printed them joined by a colon.

**Evidences:** PLAY-dOrderedCharter-53
- AC1 — `--plant positional-edited-after` exited 1, printed `positional — grandfathered: memory/builds/x/build/record.md:1` for `x.py` line 1 `(written in f83d1b4b, before the check)`, and printed `tags: positional · unlisted · memory/builds/x/build/record.md` for `x.py` line 3
- AC2 — `--plant positional-renamed-after` exited 0, printed `positional — grandfathered: memory/builds/x/build/moved.md:1` for `x.py` line 1 `(written in 9ebdc393, before the check)`, and counted `0 unlisted, 1 grandfathered`
- AC3 — `--plant positional-uncommitted` exited 1 and printed `tags: positional · unlisted · memory/builds/x/build/record.md` for `x.py` line 3, its committed line 1 still `grandfathered: memory/builds/x/build/record.md:1`
- unit 47's `--plant positional-forked-before` exited 0 and printed `the pre-fork record: rc=0; a record after the merge: rc=1; the pre-fork record moved under tools: rc=1`, its grandfathered line in the new `<path>:<line> … (written in` shape
- the blame reader over `tools/playbook/positional.py` returned one 40-hex sha per line, and over `no/such.md` raised `git blame failed for no/such.md`, the exit-2 refusal of section 5
