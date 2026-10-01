**Serves:** journal TOOL-aSightedSkeptic-10

# Build brief — TOOL-aSightedSkeptic-10

Build `TOOL-aSightedSkeptic-10` from its spec,
`memory/builds/aSightedSkeptic/spec/2026-10-01-spec-TOOL-aSightedSkeptic-10.md`, and nothing else.
The closing review's H1 and H2 name the exact breaks to stage.

FAST DIFF-SCOPED CHECKS ONLY, NOTHING HELD. The run is in BUILDING, so the suite itself,
`run-gates.sh`, `GATE_*=` prefixes and every held leg are refused at the tool call. Observe each new
arm RED by a stub evaluation in the scratchpad that slices the suite's runner to your new arms (the
way the earlier units did), run against the template with the review's staged break applied and
re-rendered, then restore both files with `git checkout -- <files>` and confirm `git status` is clean
before the next break. The main loop runs the whole suite once at VERIFYING.

The other allowed checks: `node tools/workflows/check-workflow-syntax.js`,
`bash tools/workflows/check-verifier-fanout.sh`, `bash tools/workflows/check-review-join.sh`,
`bash tools/workflows/check-protocol-parity.test.sh --render`, `bash tools/check-kit-versions.sh`,
`python tools/memory-tree/gotchas.py --for-paths <paths>`, `python tools/memory-tree/gen_build_index.py --write`.

Commit the spec FIRST is already done by the main loop. ONE code commit whose subject carries the
unit id, ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and a `Decided:` line
per choice the spec did not make. Set the spec's status to CLOSED in that commit. Do not run
`--dispatch`; the main loop has.

Return, in `summary`: the arms added, the break each was observed RED against with the failing
line, the final pass count and floor, the gotcha record's path, and anything skipped with why.
