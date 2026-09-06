# TOOL-dTracedLattice-3 — acceptance ledger

**Serves:** journal TOOL-dTracedLattice-3

**Evidences:** TOOL-dTracedLattice-3
- AC1 — `python3 tools/codebase-map/selftest.py` — the arm `backlog: written outside the worktree (AC1)` asserts the destination is not relative to the repo root. Observed RED against the pre-fix `map_root(root) / "reinvention-backlog.md"`, which named the file inside `memory/map/`. Asserted on the DESTINATION rather than by running a whole digest into a scratch repo: where the write goes is the property, and a fixture running the digest would grade the digest
- AC2 — `python tools/codebase-map/map_diff.py HEAD..HEAD --converge` — an empty range produces `collision_flags: 0` and creates no file at the destination, checked by `test -f` against a path deleted first. The write is inside `if flags:` and again inside `if added:`
- AC3 — `python tools/codebase-map/map_diff.py 6ec402bd..HEAD --converge` — `-> 9 row(s) appended to C:/projects/coding-governance/.git/codebase-map/reinvention-backlog.md`. The path is now outside the worktree, so `relative_to(root)` no longer resolves and the ABSOLUTE spelling is printed: a reader has to be able to open it
- AC4 — `memory/backlog/TOOL.md` — supplied to `TOOL-dTracedLattice-1` per S3 and landed by that unit alone, which is the M6 clause-3 reason this unit does not edit the row. The `TOOL-aScouredKit-16` row no longer claims the backlog is tracked, permanent, or shipped to adopters
- AC5 — `tools/codebase-map/README.md` — the `map_diff.py` entry states the destination, why the common dir and never `--git-dir`, that the old location is named and never deleted, and the TRUE claim about references: no gate leg and no hook runs `--converge`, and it is NOT unreferenced — `WIRE-INTO-PROJECT.md`, `reuse-lookup.agent.md` and `selftest.py` all reach it
- AC6 — `python3 tools/codebase-map/selftest.py` — the arm `backlog: follows --git-common-dir (AC6)` resolves BOTH `--git-dir` and `--git-common-dir` and asserts the write followed the latter and not the former. It SKIPS LOUDLY where the two are the same path, which is every non-linked checkout, so it cannot pass by being unable to tell them apart. Observed RED against the pre-fix destination
- AC7 — `python3 tools/codebase-map/selftest.py` — the arm `backlog: the legacy file is named, never deleted (AC7)` asserts `render_legacy_note` returns `""` with no legacy file and, with one, a note naming the old path, the new path, and that nothing was deleted — then asserts the file is still there. Also observed live: a planted `memory/map/reinvention-backlog.md` produced the note on a real `--converge` run
- S1 — `derive_backlog_path` — the destination, with the reason the tree cannot be summarised in one clause: ONE consumer resolves the common dir (`tools/memory-recall/query.py:233`), while the gate runner and the lander use `--git-dir` for records meant to die with their worktree. It fails OPEN back into the map tree where git cannot answer at all, because this is a WARN path and refusing to report a convergence signal over a failed subprocess is the worse trade

## Why the migration note is its own function

`render_legacy_note` was inline until the arm needed it. A `--converge` run in a clean fixture —
which is what AC1 grades — never reaches the migration case, because the case exists only for a tree
carrying the pre-move file. Extracting it is what let AC7 be armed at all rather than asserted about.

## What this ledger does not evidence

No arm runs `--converge` end to end in a scratch git repo. The digest, the collision detector and the
backlog dedup already have their own arms; what this unit changed is the destination and the report,
and both are graded directly. An adopter whose git binary is missing gets the fail-open path back
into the map tree, which is deliberate and is untested.
