**Serves:** journal TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4

# Build brief — aPrimedIndex, every unit

The run's main loop builds every unit INLINE, one at a time, in the order 1, 2, 3, 4. Units 3 and 4
share `order 3` and write disjoint files, but both call unit 2's verb, so the inline author
sequences them rather than delegating them as a concurrent pair. The spec is the design; this brief
adds what a pass must do beyond it. The mandate is the owner's prompt beside this file,
`2026-10-11-prompt-TOOL-aPrimedIndex-1.md`.

1. **Declare, then stage by name.** `--dispatch` names every path a pass writes before its commit,
   and the commit stages exactly those plus the run record, `memory/builds/aPrimedIndex/RUN.md`,
   which carries the pass's `--brief` and `--dispatch` rows. Never `git add -A`.
2. **Start from the measured drafts.** The probe's drafts sit in the session scratchpad:
   `regen.py`, `patch_u1.py` (the descriptor edits), `patch_u23_runner.py` (the runner's verbs and
   preflight) and `canary_arm.sh` (arm 1r). Each was run in the scratch clone `pi1`; re-verify each
   against the spec before committing it, and change the spec first where they disagree.
3. **No merge bar, no self-test suite, no `*.test.sh` run whole.** A criterion is observed directly:
   the verb on a scratch clone, or one canary arm run as a slice from inside the kit directory, with
   the slice deleted before the commit (`gen_map.py` reads untracked files).
4. **Observe every new arm RED first**: stage its break in a scratch copy, see `FAIL`, restore, see
   it pass. Both observations go in the ledger paragraph.
5. **The acceptance ledger is owed: every unit is Tier-2.**
   `memory/builds/aPrimedIndex/build/2026-10-11-build-TOOL-aPrimedIndex-<n>-1-acceptance-ledger.md`,
   in the grammar of `memory/HYGIENE.md`, "Acceptance ledger".
6. **Regenerate the codebase map in the pass that moves a symbol**, `gen_map.py --write`, declared
   first. A new kit file may also need a dossier claim in `memory/map/features/run-gates.md`.
7. **The kickoff manifest watches `tools/run-gates/run-gates.sh`.** The pass that edits it adds the
   `--regen` verbs to the manifest's gate commands and re-stamps `last-audit` and
   `last-body-change`, with a delta line in the commit message.
8. **No kit-version bump by hand.** The lander mints the versions a landing owes.
9. **After every commit, run the bug-class checklist** over it: `gotchas.py --for-diff HEAD~1..HEAD`.
