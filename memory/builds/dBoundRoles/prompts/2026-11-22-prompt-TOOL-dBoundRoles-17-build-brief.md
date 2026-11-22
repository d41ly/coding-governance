**Serves:** journal TOOL-dBoundRoles-17

# Build brief — TOOL-dBoundRoles-17

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run, building every DEFERRED spec in the build-order table's order. This is build order
  8. Built and CLOSED so far: TOOL-dBoundRoles-14 at `7a58950fb`, TOOL-dBoundRoles-2 at `8795c820a` and
  TOOL-dBoundRoles-1 at `3b479f2fe`, TOOL-dBoundRoles-37 at `5f7f208fd`, TOOL-dBoundRoles-21 at `4c2cf2a3d`,
  TOOL-dBoundRoles-22 at `8463d5212` (ordered `[[workflow.stages]]` rows, `derive_stage_map`, `read_agent_limit`) and
  TOOL-dBoundRoles-49 at `fa3e705e1` (`derive_seed_expected` and the S3 overlay check in `tools/govkit/selftest.py`) and
  TOOL-dBoundRoles-54 at `ff44a3ec1` (`load_kit_roster`, `derive_overlay_expected`, `derive_overlay_drift`, the two-way
  overlay checks), TOOL-dBoundRoles-55 at `5e3109bd2` (the empty-roster refusal) and TOOL-dBoundRoles-16 at `901778344`
  (the five `[[kind]]` rows, each entry's `kind`, `checklist` and `orientation`, every role's `shapes`, the factories)
  and TOOL-dBoundRoles-15 at `3a53454b3` (each role's `budget`, `render_static_block`, R5 over the whole block): the `role` and `field` tag namespaces, every role
  file's `never:`, `return:`, `layer:` and `acts-as:`, the merged `gov-reviewer`, the four new roles and the roster by
  layer. Build on those as they stand.
- Every roster spec was re-grounded on HEAD before this dispatch, so its citations hold at HEAD or name the earlier
  unit that changes them. Still verify each claim the spec makes about current code against source before your first
  write, and hand a claim that no longer holds back as a divergence rather than building around it.
- This is the fourth dispatch. The third builder (run `wf_913518d6-7fc`) built most of the unit, then found
  `tools/playbook/instruction_units.py#arm_work_order` pinning the marker's bytes; rev-8 adds that reader, the file and
  its leg. Its partial build is `p17/TOOL-dBoundRoles-17-wip.patch` in the session scratchpad, with the seeded home
  `p17/work-order-legacy.txt.wip`: re-apply the patch with `git apply --index`, check it against rev-8, then finish the
  docs, hygiene check 3, the template row, the help page, the usage row, the manifest re-stamp and the ledger.
- Earlier: this was the third dispatch. The second builder (run `wf_25370bd3-656`) found the help page and usage row the docs
  rule owes, the kickoff manifest re-stamp, a render route a builder may not run, the return predicate's two readings
  and readers with no field record; rev-7 folds all five (§8 F6 for the predicate). The pass edits only
  `tools/memory-tree/HYGIENE.template.md`: the main loop renders `memory/HYGIENE.md` in a follow-up commit, so do not
  write it. The pass re-stamps the kickoff manifest `memory/guides/SESSION-KICKOFF.md`.
- Earlier: this was the second dispatch. The first builder (run `wf_1aee65de-95e`) found a positional `MARKER_RE` reader in
  `tools/roles/render_agents.py`, a seeded file only a later unit admitted, and one stale count; rev-6 folds all three,
  and this unit now admits `F:work-order-legacy.txt` in hygiene check 3 itself (§8 F5), its guide row rendered into
  `memory/HYGIENE.md` by `kit-dogfood-parity.test.sh --render`.
- Generated outputs are admitted undeclared and belong in the pass commit: `.claude/roles.json` and `.claude/agents/` as
  `render_agents.py --write` renders them, every file `gen_build_index.py --write` rewrites, the dClosedLoop as-built
  view and the map generator's output. Any other path outside the declared set: name it in your return and do not
  write it. A CLOSED spec is frozen; if this spec asks you to edit one, hand that back as a divergence.
- The return checker this spec calls `validate_return` in prose is named `check_return` (TOOL-dBoundRoles-5 §8 F7,
  the lexicon's answer); that unit mints it later, so name it `check_return` wherever you write it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-17`, its final trailer block carrying `Pass: TOOL-dBoundRoles-17` beside
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage explicit
  paths only, never `git add -A`.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-17-1-acceptance-ledger.md` in the
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
