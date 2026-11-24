**Serves:** journal TOOL-dBoundRoles-69

# Build brief — TOOL-dBoundRoles-69

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run, building every DEFERRED spec in the build-order table's order. This is build order
  39. Every unit of the build-order table in `memory/builds/dBoundRoles/README.md` whose spec reads CLOSED is built;
  its acceptance ledger and deviation records under `memory/builds/dBoundRoles/build/` say what it left. The newest:
  TOOL-dBoundRoles-64 at `53cf06182` (adopter floor 245 with a term naming this unit, the `TMP_ROOT` guard of
  `check_role_reads`, the spawn guard's base 187 with terms for units 50 and 58, deviation record 643),
  TOOL-dBoundRoles-65 at `f92658ff2` (deviation record 652, the worktree comparison through `branch_reconcile` under
  `dbr63obs`, its control observed, no code), TOOL-dBoundRoles-66 at `d68dc88fa` (the spawn guard's comparison reads
  `$pass`, TOOL-dBoundRoles-46's rows under a header of their own, record 663, the failed-import observation staged),
  TOOL-dBoundRoles-67 at `6a1baff95` (the sweep by signature `7dae6faf2`, nothing selected, record 672),
  TOOL-dBoundRoles-68 at `dfc500e15` (the signature selection's control at `dbr68c`, record 682). Build on those as
  they stand.
- Every roster spec was re-grounded on HEAD before this dispatch, so its citations hold at HEAD or name the earlier
  unit that changes them. Still verify each claim the spec makes about current code against source before your first
  write, and hand a claim that no longer holds back as a divergence rather than building around it.
- The roles kit is shipped kit code: name every new helper with a verb the naming lexicon declares
  (`lexicon.py --suggest <name> --as py.function`), and give every new verb, key or reader its usage anchor on the
  `help/` page the spec names (stamps from `python tools/govkit/docs_leg.py --fingerprints`); a row an anchor drains
  from `memory/project/docs-undocumented.txt` leaves that list in the same commit. If a change moves the charter's
  render, run the playbook kit's `adopt-playbook.sh --target .` and commit `AGENTS.md` and
  `.governance/instructions.lock`. The self-test arm of section 7 runs only as the probe of your own rows, never the
  suite.
- In every record, name a bare line citation in words, never as `path:line`, and never set a number before a counted
  noun (write "the deviation record of this unit"): the positional and pinned-facts checks read both as findings.
  Spell every fixture key from parts. Every scratch tree and staged break runs under `%TEMP%`, never in the tree.
- Generated outputs are admitted undeclared and belong in the pass commit: every file `gen_build_index.py --write`
  rewrites, the dClosedLoop as-built view, the map generator's output and the charter render. If a spec claim no
  longer holds at HEAD and the fix is mechanical, make the change inside the write set and record it in the deviation
  record. Hand back as a divergence only a design choice the spec leaves open; any other path outside the set: name it
  in your return and do not write it.
- Every new Python text read or write, subprocess call included, names `encoding="utf-8"`. No shipped file spells a
  kit path literally: build a path from a variable or from the file's own location. Every code citation in a record
  names its full path. The pass legs red on each of these.
- The build run's BASE is `8b8b1374c`.
- The main loop's decision `build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md` binds over this spec
  as the owner's ruling does; read it whole before you write. Every spec this unit's items rev-bump is CLOSED and
  frozen: write no spec text but your own status cell. Where an item bumps a CLOSED spec, your one deviation record
  carries the restated text for that target, the target unit's ledger answers the criterion AMENDED naming this unit
  and that record, and a criterion that greps the frozen spec is answered AMENDED in your own ledger, read from the
  record's After text.
- Records 633, 643, 652, 663, 672 and 682 already hold restated text for specs 60 and 63 to 66. Where this unit
  restates the same text again, record 692 supersedes the earlier sentence by naming its record. Read each before you
  write.
- Unit 66 left the spawn guard's floor at 194 with 182 call sites, its comparison reading `$pass`, and no skip arm, so
  S14's recount is read on the built suite and moves the floor only where the counted class differs. S18 edits the
  arm-11 and arm-20 header comments of `tools/roles/adopt-roles.test.sh` only where they still read so.
- S7's staged observation and S13's recovery run under the named root on this host's temp folder, which reads
  `C:\Temp` in this run's shells. Leave nothing registered, and touch no other run's worktree or pass worktree.
- The ledger readings of S1 to S3 and AC14 read the AMENDED form by the decision: one line per label naming the unit
  and its record. Say in record 692 what `revisions` reads on those lines.
- A criterion label a frozen spec does not number is answered under a heading of its own outside the `**Evidences:**`
  block, as units 63 and 68 did.
- This build already holds this unit's deviation record 691, from earlier passes. Record every change the spec does
  not state in ONE new deviation record, `build/2026-11-24-build-TOOL-dBoundRoles-69-deviation-692.md` (values
  `report` and `author-recorded`).
- The policy guard admits a commit touching a guarded path (`tools/policy/guarded-paths.txt`, among them
  `.claude/roles.json`, the rendered agent files and `.governance/` files) only on the live run's branch. If the
  pre-commit hook refuses your pass commit for that reason alone, never route around it: save the whole staged pass
  as a binary patch (`git diff --cached --binary`) and its full commit message under the scratch directory, check the
  patch applies with `git apply --check --index` at your base, and return `committed: false` naming both files and
  the guarded paths. The main loop applies and commits it on the run's branch.
- A new `[[upgrade]]` step id enters `memory/project/landed-steps.txt` in the pass commit if the ratchet asks for it,
  and a plant you add to a kit's self-test moves its row in `tools/run-gates/selftest-budgets.txt`: re-price that
  row's `plants=` token and scale its ceiling by the plant count, as the rows re-priced in this run did.
- `.claude/agents/` and `.claude/roles.json` are renders: rewrite them only with `tools/roles/render_agents.py`; every
  other generated copy the spec names (the charter, the review protocol, the workflow renders, the leg manifest) is
  re-rendered by its own renderer, never edited by hand.
## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-69`, its final trailer block carrying `Pass: TOOL-dBoundRoles-69` beside
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage explicit
  paths only, never `git add -A`.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-69-1-acceptance-ledger.md` in the
  pass commit: one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- In every record you write, cite code as `path#symbol` or a blob-pinned `path@<blob8>:<line>`, never a bare
  `path:line`, and put a pin (a sha, a `path:line` or `DERIVED`) on any line quoting a count of lines, files or units.
  Never write a section number beside a counted noun (say "the legs section 7 lists"): the pinned-facts check reads it
  as an unpinned count.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list needs its
  own `--dispatch` with `--writes` naming the FULL set before you stage it, unless the call carries `passBase`, in
  which case you record nothing in the run-state file and name the extra path in your return. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`; its values are `report` and `author-recorded`.
