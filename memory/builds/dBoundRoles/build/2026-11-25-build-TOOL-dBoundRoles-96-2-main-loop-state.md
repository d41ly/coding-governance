**Serves:** journal TOOL-dBoundRoles-96

# dBoundRoles — the main loop's state after TOOL-dBoundRoles-96

## The security review

Round 1 over TOOL-dBoundRoles-95, run `wf_db3b7d40-50e`, is the record
`../reviews/2026-11-25-review-TOOL-dBoundRoles-95-security-diff-review-round1.md`. Round 2 over its fold, run `wf_511215d7-b73`,
base `a911378eb`, head `b25b031a2`, is CONVERGED: its lenses raised a single low, refuted as older than the fold, so the
harness wrote no report. The refuted finding says no plant reaches the guard-self refusal of the list path off a live run; the
skeptic read that gap as the base's own.

## The first reconcile, dropped

`origin/main` `3d6c1702a` was merged uncommitted, resolved, reviewed by run `wf_c81f2130-2e9` and folded, and never
committed: main's `actions.free` guard, live in the merged tree, refused the commit while the position engine read no item in
flight. The owner ruled "Fix the engine on main", then "Branch, before re-merge (Recommended)": the staged merge was dropped
at `735060358`. Its tree is `c2c9bf42e`. The review's record and the patches that rebuild that tree are in the session's
scratch directory, `save/`, outside this repository. What the redo owes, found there:

- `checkRedLane` of `tools/hooks/scratch-guard.js` keeps the `governed` read; the first resolution lost it and the suite caught it.
- Rule 9 and its rows move to `tools/roles/spawn-guard.js` and its suite, with `rule 9` in the lists of the roles and hooks READMEs;
  `tools/hooks/actions-free.fixture.sh` takes the guard from its caller, and the leg guard of `spawn-guard self-test` names the fixture.
- The class of `deriveActClass` reads the write scan with the payload's cwd and tool, and the git shapes and heads the same tool's view.
- The verdict store's key of `tools/unattended/check-pass-order.sh` carries `FORK_RECORD_CUTOFF`, whose date is re-derived past the
  newest spec on the merged tree; that suite's fixture lacks `commit_trailers.py`, which no bar leg runs.
- The velocity preset's `roles.retries` is above the catalogue's maximum of this build, TOOL-dBoundRoles-92.
- The hooks kit's version is past the one both sides took; `selftest-budgets.txt` keeps one `plants=` token a row.

## Owed by this build, found reading the driver shards

- Region four of the unattended driver's suite: older fixtures dispatch a spec with no `Open questions` section, which grades FORKED as at
  BASE, and TOOL-dBoundRoles-11's hold now refuses. The fixtures owe the section. Region three's reds match the tip before the
  merge and are not compared with BASE. The other regions are unread.
- The bar's own reds of `../prompts/2026-11-25-prompt-TOOL-dBoundRoles-93-close-resume.md` stand.

## Waiting

On `origin/main`: the Red-fix gate fix, "A, list at parent (Recommended)", and the position engine fix, "Fix the engine on main". Then the
owner's disposition records, by the command the engine fix names, as records alone; then one reconcile with both, its review and direct
suite runs, `--authorization`, and the close with "No, plain bar".
