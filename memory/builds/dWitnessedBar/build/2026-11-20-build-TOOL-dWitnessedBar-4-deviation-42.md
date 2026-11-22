# TOOL-dWitnessedBar-4 deviation 42 — Test's exit checks the tree the move names, and the hook's scoped path reads only the pushed tree

**Serves:** deviation TOOL-dWitnessedBar-4

- **Departs from:** `TOOL-dWitnessedBar-4@rev-5 [S6, S3]`
- **Hand-off:** spec-to-code
- **Before:** S6 has the move at `item.test.exit` refuse unless its `tree` names a GREEN full `gate-verdict/<tree hash>` "for the tree `verdict.tree` selects". S3 has the hook's bar-record candidates, `check_bar_base` and the cover pass read the pushed tree's two per-tree files.
- **After:** `check_tree_verdict` in `tools/loop/loop_transition.py` refuses, exit 1 naming the tree, where the move names no tree, a value that is no tree hash, no full per-tree verdict, one naming another tree, or one not reading GREEN; it does not derive which tree `verdict.tree` selects, so the caller names the merge's tree or the tip's, and its docstring says so. In `.githooks/pre-push` the scoped path's candidates are the pushed tree's two files, as S3 says, and `check_bar_base` reads the full file of the base's own tree; so a scoped verdict is a candidate only for the tree the cover pass reads first, and the suite's arms over an ANCESTOR record adopted as a scoped base (25b, BG AC18, slot AC1-AC3, AC5, AC6, PM AC12, TOOL-aFrugalTurnstile-15 AC1, TOOL-aFrugalTurnstile-16 AC1), and over the hook's own writer (BG AC4, AC5, AC12, AC13), leave the suite with the behaviour.
- **Cause:** builder discovery
- **Reason:** the transition writer has no fact naming the prepared merge or the build tip at the move, and §4's item table makes `item.test.exit` record the tree Test verified, which the caller holds; a derivation would need a definition of "the build's tip" the spec does not give. The pushed tree's files are the whole candidate set S3 names, so a record for an ancestor tree is never read.
- **Evidence:** `tools/loop/loop_transition.py#check_tree_verdict`, `.githooks/pre-push#check_bar_base`, `.githooks/pre-push#check_cover_record`, `.githooks/pre-push.test.sh`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** PLAY-dClosedLoop-2
