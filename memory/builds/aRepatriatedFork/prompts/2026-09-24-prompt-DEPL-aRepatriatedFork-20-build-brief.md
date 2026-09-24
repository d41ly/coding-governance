# Build brief — DEPL-aRepatriatedFork-20

**Serves:** journal DEPL-aRepatriatedFork-20

## What you are handed

The spec at `memory/builds/aRepatriatedFork/spec/2026-09-23-spec-DEPL-aRepatriatedFork-20.md` is the design, and its §8 is resolved in place: every fork carries a
`RESOLVED` mark naming who decided it. Build what it says. Where the code disagrees with the spec,
change the spec first, as a rev-N bump with its §9 line naming the section, scope id or acceptance id
it moved; a §9 line naming none of those reds hygiene check 12.

The build's rules are in the `## Build-level rules` slot of `memory/builds/aRepatriatedFork/README.md`,
and they bind this unit: a fork retires only when gov's bytes run verbatim at the adopter, an adopter
fix is reproduced at gov HEAD before it is absorbed, a path fix is a derivation or a render and never
a new conf key for layout, no new bar leg lands without its ceiling and testsuite-count row, and a
new gate's red case is observed before it lands.

## This unit WRITES inCMS, and only in one place

This is the one unit whose work lands in another repository, and its spec's `### Rollout` already
says how: the migration runs in an inCMS worktree and lands on inCMS's `main` through inCMS's own
lander, and that merge and that push each need the OWNER'S ask, which this unattended run does not
carry. So:

- Create ONE worktree for the whole unit: `git -C C:/projects/incms/main worktree add
  C:/projects/incms/main/.claude/worktrees/converge-arf20 -b converge/aRepatriatedFork-20 <inCMS main
  HEAD>`, which is where inCMS keeps its worktrees. Record the base sha. Do all inCMS work there, and
  commit there on that branch.
- NEVER push that branch, NEVER merge it, NEVER commit, stash, check out or reset anything in
  `C:/projects/incms/main` itself or in any other inCMS worktree. Another session is active on
  inCMS's `main` and has moved it several times today.
- NicoCares is untouched: this unit's §3 excludes it.
- The unit cannot CLOSE: AC1 and AC7 observe inCMS AFTER its landing, which the owner has to ask
  for. Set the spec status header to `BLOCKED` in your gov commit, not CLOSED, and write why in its
  §9 line: the migration is prepared on `converge/aRepatriatedFork-20` at the sha you name, and the
  landing is the owner's. Observe every other criterion on that branch, and write the acceptance
  ledger for the ones you observed. Mark AC1 and AC7 `deferred` with the reason.
- §8's resolutions bind: every `status:` value and every gotcha declaration is DERIVED from that
  build's or record's own evidence, never a bulk default. What no evidence decides is LISTED BY NAME
  in a journal record under `memory/builds/aRepatriatedFork/build/` in gov, and left unauthored in
  the branch. Return the count of each list in `summary`.
- The migration script(s) live in the inCMS branch, beside inCMS's own `scripts/memory-reorg/`
  steps (S6). Gov commits only records: the spec, the ledger, the journal record, the brief.
- inCMS's own bar is NOT run in this pass either. Run the direct checks the ACs name, in the
  converge worktree, and name in `summary` which inCMS legs the owner's landing will owe.
- If the whole migration cannot be completed in one pass, commit what is done on the inCMS branch,
  record exactly what remains in the journal record, set the gov spec to BLOCKED as above, and
  return. A partial branch that says what it lacks is worth more than a pass that runs out of time.

## Traps this repo has already paid for

- The working copy may hold CRLF. Edit files with the editor tools, or with Python in BINARY mode; a
  text-mode `open()` or a multi-line `str.replace` over CRLF silently matches nothing or eats bare CRs.
- Backslash escapes die inside Bash heredocs. Author scripts and fixtures with the file tools.
- A new Python function name is graded by the lexicon leg: ask
  `python3 tools/lexicon/lexicon.py --suggest <name> --as <cell>` before naming it.
- Touching a kit's shipped bytes owes that kit's version stamp in every carrier.
  `python tools/govkit/govkit.py selfcheck` names a carrier you missed; run it after such a change.
- `python tools/memory-tree/gen_build_index.py --write` sees tracked files only: `git add` a new file
  before rendering.
- `git rev-parse "<rev>:.claude/x"` is mangled by MSYS; use `git ls-tree <rev> -- <path>`.
- A unit that ends BLOCKED still owes the acceptance ledger for every criterion it observed, in
  the grammar of `memory/HYGIENE.md` under "Acceptance ledger": a record under
  `memory/builds/aRepatriatedFork/build/` named `<date>-build-<unit-id>-1-acceptance-ledger.md`.
- Run `python tools/lexicon/lexicon.py` and `bash tools/check-install-prefix.sh` in gov before
  committing there; both must exit 0.

## What to return

`summary` names the direct check each acceptance criterion was observed by, and any criterion only
the merge bar or a self-test suite can observe, which the main loop runs once at the close.
