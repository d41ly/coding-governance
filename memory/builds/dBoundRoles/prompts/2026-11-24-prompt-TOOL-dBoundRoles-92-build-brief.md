**Serves:** journal TOOL-dBoundRoles-92

# Build brief — TOOL-dBoundRoles-92

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run at its close. The closing diff review's round 1,
  `memory/builds/dBoundRoles/reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md`, is BLOCKED, and
  its items are promoted into TOOL-dBoundRoles-86 to TOOL-dBoundRoles-92, built in that order. This is build order
  46. Every unit before it in the build-order table of `memory/builds/dBoundRoles/README.md` is CLOSED, and its
  acceptance ledger and deviation records under `memory/builds/dBoundRoles/build/` say what it left.
- TOOL-dBoundRoles-86 to TOOL-dBoundRoles-91 are built; read each one's ledger and deviation record before you touch a
  file it wrote, `tools/hooks/scratch-guard.js` (86, 87), `tools/roles/spawn-guard.js` (88), `tools/loop/placement.py` and
  `tools/roles/handoff.py` (89, 91), the workflow harnesses (90). The scratch guard's suite floor is 591 after 87.
- `lexicon.py --check` reads its verb offenders at this run's inherited count over its pin; that red is not yours.
- A scope item beside the spec's, inside your write set, recorded in your deviation record and in your ledger: the
  main loop's reading of `govkit selftest` at this run's tip against its BASE leaves four own failures, all in
  `tools/govkit/selftest.py` and all from TOOL-dBoundRoles-25's retirement of the spawn guard from the hooks kit. Fix each
  in the suite, where the expectation is stale, and not in the product: the `aQuenchedHarness-3 AC2b` loop still names
  the leg `agent-cap self-test`, whose `[[exempt_leg]]` row is now `spawn-guard self-test`; and the `[dDL-57]` cases AC1,
  AC2 LIVENESS and AC4 LIVENESS plant a claim of `kickoff-manifest`, `memory-tree`, `roles` and `run-gates`, while
  `tools/roles/kit.toml` now requires `agent-cap` and `policy` beside `loop`, so the claim owes those two for each case to
  grade the loop edge it was written for. AC1's planted receipt and its route needle move with it. Verify each by a
  one-case slice of the file, never the suite, and red first against the present expectation.
- Verify each claim the spec makes about current code against source before your first write, and hand a claim that no
  longer holds back as a divergence rather than building around it. If the fix is mechanical, make the change inside
  the write set and record it in the deviation record. Any path outside the set: name it in your return and do not
  write it.
- Every earlier unit's spec is CLOSED and frozen: the main loop's decision
  `build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md` binds. Write no spec text but your own status
  cell; a change to what a CLOSED spec states is ONE deviation record of this unit carrying the restated text.
- Name every new helper with a verb the naming lexicon declares (`lexicon.py --suggest <name> --as py.function`, or the
  cell of its language), and give every new verb, key or reader its usage anchor on the `help/` page the spec names
  (stamps from `python tools/govkit/docs_leg.py --fingerprints`); a row an anchor drains from
  `memory/project/docs-undocumented.txt` leaves that list in the same commit. If a change moves the charter's render,
  run the playbook kit's `adopt-playbook.sh --target .` and commit `AGENTS.md` and `.governance/instructions.lock`.
- In every record, name a bare line citation in words, never as `path:line`, and never set a number before a counted
  noun. Spell every fixture key from parts. Every scratch tree and staged break runs under `%TEMP%` or the scratch
  directory, never in the tree.
- Generated outputs are admitted undeclared and belong in the pass commit: every file `gen_build_index.py --write`
  rewrites, the dClosedLoop as-built view, the map generator's output, the charter render and the docs reference pages.
- Every new Python text read or write, subprocess call included, names `encoding="utf-8"`, and every JavaScript one
  names its encoding. No shipped file spells a kit path literally: build a path from a variable or from the file's own
  location. Every code citation in a record names its full path. The pass legs red on each of these.
- A live hook of this session reads `tools/hooks/scratch-guard.js` and `tools/roles/spawn-guard.js` of the run worktree.
  You edit your own pass worktree, so a half-written hook there affects nothing.
- The build run's BASE is `8b8b1374c`. `.claude/agents/` and `.claude/roles.json` are renders: rewrite them only with
  `tools/roles/render_agents.py`; every other generated copy the spec names is re-rendered by its own renderer.
- The policy guard admits a commit touching a guarded path (`tools/policy/guarded-paths.txt`, among them
  `.claude/roles.json`, the rendered agent files and `.governance/` files) only on the live run's branch. If the
  pre-commit hook refuses your pass commit for that reason alone, never route around it: save the whole staged pass
  as a binary patch (`git diff --cached --binary`) and its full commit message under the scratch directory, check the
  patch applies with `git apply --check --index` at your base, and return `committed: false` naming both files and
  the guarded paths. The main loop applies and commits it on the run's branch.
- A plant or arm you add to a suite moves its row in `tools/run-gates/selftest-budgets.txt`: re-price that row's
  `plants=` token where it has one and scale its ceiling by the count, as the rows re-priced in this run did, and raise
  the suite's `FLOOR_ASSERTIONS` by the assertions you add, with a comment term naming this unit.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-92`, its final trailer block carrying `Pass: TOOL-dBoundRoles-92` beside
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage explicit
  paths only, never `git add -A`.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-92-1-acceptance-ledger.md` in the
  pass commit: one line per criterion of the spec's acceptance section, each leading with a backticked token that
  criterion itself spells, never wrapped across a line.
- In every record you write, cite code as `path#symbol` or a blob-pinned `path@<blob8>:<line>`, and put a pin (a sha or
  `DERIVED`) on any line quoting a count of lines, files or units.
- The call carries `passBase`, so record nothing in the run-state file. A file on the kickoff manifest's `watch:` list
  needs the manifest re-stamped in the same commit, and a stale codebase map needs the map generator's output.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, `2026-11-24-build-TOOL-dBoundRoles-92-deviation-921.md`; its
  values are `report` and `author-recorded`.
