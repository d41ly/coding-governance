**Serves:** journal TOOL-aSightedSkeptic-5

# Build brief — TOOL-aSightedSkeptic-5

Build `TOOL-aSightedSkeptic-5` from its spec, `memory/builds/aSightedSkeptic/spec/2026-10-01-spec-TOOL-aSightedSkeptic-5.md`, and nothing else.

You are FIRST. You set `REVIEW_SHAPE` and move the version to 1.17 (spec S3, S9). Re-key the existing self-test arms from four lenses to five (S8): every count of four lenses in the suite moves.

FAST DIFF-SCOPED CHECKS ONLY, NOTHING HELD. This pass runs NO self-test suite, no `*.test.sh`, no
`run-gates.sh`, no `GATE_*=` prefix, and no held leg — not once, not "to confirm". The checks it may
run are exactly these, each once at the end, each bounded at 300 s:

- `node tools/workflows/check-workflow-syntax.js`
- `bash tools/workflows/check-verifier-fanout.sh`
- `bash tools/workflows/check-review-join.sh`
- `bash tools/workflows/check-protocol-parity.test.sh --render` (the render MODE only — it writes the
  render; it is the one `.test.sh` invocation allowed, and only with `--render`)
- `bash tools/check-kit-versions.sh`
- `python tools/lexicon/lexicon.py --suggest <name> --as js.function` for every new function name
- a stub evaluation of your own, written to the scratchpad, that runs the edited template the way
  the self-test's second half does, to see your change take effect (optional, bounded at 120 s)
- the plain greps and seds your spec's §6 names

The self-test arms your spec's §6 names ARE written into `tools/workflows/tier2-review.test.sh` by
this pass, with `FLOOR_ASSERTIONS` raised by the count you add, and are NOT run. The main loop runs
the suite once at VERIFYING, and observes each arm RED against the pre-change script in a frozen
clone. So write each arm so it would fail on the parent commit — and say in your return which arm
fails how on the parent.

THE SPEC IS ALREADY COMMITTED. Build what it says; to diverge, change the spec first (a rev bump and
a §9 line) in the same pass, and say so. The commit is ONE code commit whose subject carries the unit
id, e.g. `build(aSightedSkeptic): TOOL-aSightedSkeptic-N — <mechanism>`, ending with the trailer
`Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and a `Decided:` line per choice you made
that the spec did not.

The source is `tools/workflows/tier2-review.template.js`. Never hand-edit
`tools/workflows/tier2-review.js`: regenerate it with the render mode above and commit both. Do not
edit `tools/hooks/agent-cap.js`, any governance carrier (`memory/guides/REVIEW-PROTOCOL.md`, its
template, `memory/guides/BUILD-METHOD.md`, its template, the charter template), or `REVIEW_SHAPE`
after unit 5 set it. Earlier units of this build are already landed on this branch — read the
template as it stands, not as the spec's BASE line numbers describe it; the line numbers in your spec
are from `ef1dcdb6` and have moved.

After the commit run `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on any
class it names that your diff already violates, in a follow-up commit of the same unit if needed.
Shared design: `memory/builds/aSightedSkeptic/prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md`.

Return, in `summary`: the files written, the checks run with their exit codes, the arms added and how
each fails on the parent, the new `FLOOR_ASSERTIONS`, and anything skipped with why.
