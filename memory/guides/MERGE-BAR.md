# The merge bar — how it behaves

Read this before you run, scope or debug a bar, and before a push. It is the body of `AGENTS.md`'s
merge-bar section, which keeps only what a session needs before it opens this file.

**The leg list is `tools/gate-legs.json`. Read it there and nowhere else.** Each leg's rationale is
its own script header, and the machinery around a leg is its dossier under `memory/map/features/`.
This section used to enumerate all seventy while telling the reader, two paragraphs in, to read the
split from the manifest — 26 KB of prose restating a file that cannot go stale, in front of the file
that can. What survives here is what a session cannot get anywhere else.

**Guards scope a run, never a verdict.** MOST self-test legs carry a `guard` in the manifest naming
the kit dir they exercise, so a records-only commit runs only the legs that check this repo's actual
state. Not all do, and the split is DERIVED from `tools/gate-legs.json` rather than counted here —
an unguarded leg runs on every bar, which is the whole point of leaving it unguarded. `GATE_FULL=1` bypasses every guard, and `.githooks/pre-push` DECIDES whether to set it rather
than setting it unconditionally, forcing a total run when no recorded full green covers the pushed tip, when that green is more than a declared
number of first-parent landings behind it, when its tree fingerprint does not reproduce at the sha it names, when
the leg manifest itself moved, or when the push runs the kit self-tests and the recorded green was
earned with them held. That last one is COVERAGE and not equality — a green that covered MORE still
satisfies a push that needs less, and a stamp with no such key at all reads as HELD. A guard can therefore scope the authoritative run too, and a
too-narrow guard cost an early signal rather than a wrong merge verdict. A guard naming an untracked path would
skip forever and silently, so the run-gates canary refuses one.

**How the bar behaves**, because none of this is derivable from the manifest. Legs run through a
bounded pool whose width is DECLARED rather than computed: `tools/run-gates/gate-profiles.txt` maps
the detected cores and RAM to a named row of knobs, the runner prints the row it chose before the
first leg verdict, and `GATE_JOBS` overrides the width alone. That row also declares a whole-run
`wall` (`GATE_WALL` overrides): a breach kills the outstanding legs and REDS naming them. Legs are safe together because each
heavy one is hermetic — its own `mktemp -d` scratch repo, never the real tree. Order is
scheduled longest-first from a timing cache the runner resolves and NAMES on its own profile line,
while REPORTING is
always manifest order, so output is byte-stable whatever the width and a corrupt cache costs wall
clock only. **A KIT'S SELF-TESTS ARE NOT ON THIS BAR.** Owner ruling, 2026-08-23, and the first kit to take it is
`unattended`: why, and what left its descriptor, is `tools/unattended/README.md`.
What stayed are the legs whose subject is the REPOSITORY rather than the
kit, because those go stale with nobody editing it; which, and how many, are its
`tools/unattended/` rows in `tools/gate-legs.json`. On demand:
`bash tools/unattended/run-unattended-gates.sh --serial`. The compensating check is written into that kit's
descriptor, because an exemption is not coverage (§7).

Do not read a leg COUNT out of this paragraph; `tools/gate-legs.json` owns it and prose beside a
source that owns a number is the rule this file keeps breaking.

Every leg's output is persisted
per-leg under `<git-dir>/gate-logs/`, redacted; a RED run also leaves `gate-last-failure.txt`, which
only the next RED run overwrites. Never pipe the bar through `tail` — it discards the failing row;
read the durable summary instead.

**The push boundary is where the bar binds.** The inherited-red policy that `AGENTS.md`'s merge-bar
section names classifies on the remote ref, the validated tree must be the pushed tip, and
`--no-verify` bypasses. `GOV_GATE_CMD` may
name only a script this repo tracks, unmodified, and it must also EQUAL the kit's own runner or the
`GATE_CMD` a committed `.unattended.conf` declares at the pushed sha. Anything else is refused before a bar runs;
`GOV_GATE_CMD_TEST=1` is the one test escape, labelled `bar: STUB` and denied a lander marker
(`TOOL-aRepatriatedFork-5`). The hook reads the default branch from the remote it is pushing to,
refuses a dirty tree and a `HEAD` the bar moved, hands the bar `GATE_PUSH_BASE` from git's own ref
line, and leaves each refusal as a token in `<git-dir>/pre-push-refusal`, which the lander reads
instead of the push's output. A repository may declare a branch bar, `GOV_BRANCH_GATE_CMD`, in
`.githooks/gate-env.sh`; undeclared, a branch push stays ungated (`TOOL-aRepatriatedFork-8`).
A doc-only push, every path in `GATE_DOC_PATHS` at R, skips a DECLARED leg whose `doc_reads` did not
move; any worktree's full green serves every push. The `core.hooksPath` in effect decides whose
hook gates your push, a per-worktree fact (the hookspath-resolves-into-another-checkout gotcha); check H REPORTS a divergence. A tracked pre-commit fast leg sits beside it and also enforces the
branch guard, refusing a primary-tree commit off the default branch (`GOV_DEFAULT_BRANCH` pins it).
A SessionStart hook runs `tools/check-wiring.sh --session`, which auto-sets an unset
`core.hooksPath` and never clobbers a set one, so a fresh clone self-heals rather than running with
dormant gates. Remote CI is `.github/workflows/remote-ci.yml`: `history-audit` and `bar` on every
push to main, `held-plan` and `held` running the held self-tests daily. It detects after landing,
and no job is a required check.

**Two protocols are BINDING, and they are rules rather than leg descriptions.**

- `memory/guides/REVIEW-PROTOCOL.md` — a review's verify stage spawns **at most the total
  `tools/hooks/agent-cap.js` resolves** (the batch grows, the agent count never does), and how many
  run at once is a **second bound held as its own constant in that same file**. Both are file
  constants there and are written nowhere else, so this line points instead of restating. Enforced
  at the tool call by that hook, which sees the inline script where the rule actually gets
  broken, and on the bar by a leg that delegates to that same hook rather than re-implementing it.
  The marker grammar it enforces is `tools/hooks/README.md`. Ready-made harness:
  `tools/workflows/tier2-review.js`.
- `memory/guides/UNATTENDED-PROTOCOL.md` — a run that will merge and push with no owner turn replaces
  the explicit-ask checkpoint with a committed standing mandate, §1 Landing's one substitute.
  The BASE that mandate hangs on is OBSERVED from the remote's own HEAD advertisement, never read
  from a local ref and never named by the environment; both of those were reproduced bypasses. §9
  states plainly what a check running under the run's own uid can and cannot buy.

Before theorizing about drift, run `python tools/drift-audit/drift_report.py` — seconds, no agents,
and it answers whether this repo's records still describe it. Before a review, run
`python tools/memory-tree/gotchas.py --for-diff <base>..<head>` — its stdout IS the bug-class
checklist for that diff.
