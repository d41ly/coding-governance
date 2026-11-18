# TOOL-dDeclaredLoop-23 red-fix 2 — verdict epoch (kit version dates the engine) fixed in c922be2e

**Serves:** red-fix TOOL-dDeclaredLoop-23

- **Leg:** verdict epoch (kit version dates the engine)
- **Red line:** verdict-epoch: FAILED — tools/memory-tree/commit_trailers.py is imported by tools/memory-tree/routed_commits.py and is not in DELEGATES, so a change to it moves a verdict this gate never dates; add it to DELEGATES
- **Files:** tools/memory-tree/check-verdict-epoch.sh
- **Commit:** c922be2eaf34b4230b6773086ce7b539ce56b1b2
- **Rerun:** bash tools/memory-tree/check-verdict-epoch.sh, exit 0
- **Caused-by:** TOOL-dDeclaredLoop-23
