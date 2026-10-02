**Serves:** journal TOOL-aSightedSkeptic-13

# Build brief — TOOL-aSightedSkeptic-13

Build `TOOL-aSightedSkeptic-13` from its spec,
`memory/builds/aSightedSkeptic/spec/2026-10-02-spec-TOOL-aSightedSkeptic-13.md`, and nothing else.
The spec is already committed by the main loop.

FAST DIFF-SCOPED CHECKS ONLY, NOTHING HELD. The run is in BUILDING, so the gate-guard refuses any
`*.test.sh`, `run-gates.sh` and `GATE_*=` prefix at the tool call. Observe each new arm RED with a
SLICE of `tools/unattended/check-unattended.test.sh`: copy its prologue plus only your new block into
a temp script INSIDE `tools/unattended/` (named without a `.test.sh` suffix, deleted before you
commit), run it against the pre-change gate (expect red) and the changed gate (expect green). Bound
every command at 900 s. Running `bash tools/unattended/check-unattended.sh` directly with `REPORT=1`
is allowed (it is a gate leg, not a self-test suite) to measure check 23's count before and after; it
takes up to ~50 min on this node, so run it at most twice, in the background, and never alongside
the slice.

Also allowed: `bash tools/check-kit-versions.sh`, `python tools/govkit/govkit.py selfcheck`,
`python tools/lexicon/lexicon.py --check` and `--suggest`, `bash tools/check-install-prefix.sh`,
`bash skills/session-kickoff/manifest-check.sh`, `python tools/memory-tree/gen_build_index.py --write`,
`python tools/codebase-map/gen_map.py --write`, `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD`.

Use Write/Edit for every file change; never write source through a bash heredoc into Python, and
never edit a `.sh` with Python text mode (bare CR survives only in binary mode). ONE code commit whose
subject carries the unit id, ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
and a `Decided:` line per choice the spec did not make; set the spec's status to CLOSED in that
commit. If the pre-commit hook demands a manifest re-stamp or an index re-render, do it in the same
commit. Do not run `--dispatch`; the main loop has, with the full write set.

Return: files written, the before and after check-23 counts with the command, the arms and how each
fails on the parent, the new pin, the kit version carriers moved, and anything skipped with why.
