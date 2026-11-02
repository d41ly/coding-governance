# TOOL-dSafePassage-49 deviation 181 — the walk's `rev-parse` refusal runs after the candidate's config read

**Serves:** deviation TOOL-dSafePassage-49

- **Departs from:** TOOL-dSafePassage-49@rev-6 [S7]
- **Hand-off:** spec-to-code
- **Before:** S7 has each candidate TOOL-dSafePassage-47 S1 classifies also run `git --git-dir=<c> rev-parse --git-dir`, and §3 hands TOOL-dSafePassage-51 the ordering "S7's `rev-parse` run only after a config read that exited 0".
- **After:** `read_target_repositories` in `tools/govkit/upgrade_steps.py` runs the `rev-parse` for each `modules/` candidate as the walk dequeues it, after `read_config` read that repository's config with exit 0 and before its own `modules/` is walked; a non-zero exit refuses naming the candidate. That is the ordering §3 hands TOOL-dSafePassage-51, built here.
- **Cause:** builder discovery
- **Reason:** run at classification, the `rev-parse` exits 128 on the `submodule-config-malformed` plant's unterminated `[core` too, so that plant's refusal stops naming `.git/modules/sub/config does not read` and TOOL-dSafePassage-45's AC9 row and the fixture's own expectation go red; after the read, the malformed config keeps its own refusal and the unknown-format repository, whose read exits 0 with a warning, meets this one.
- **Evidence:** this unit's acceptance ledger: `fixture isolation --plant submodule-config-malformed` still refuses naming `.git/modules/sub/config does not read`, and `--plant submodule-format-unknown` refuses naming `/.git/modules/sub: git will not open this repository`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-49, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-51
- **Caused-by:** TOOL-dSafePassage-49
