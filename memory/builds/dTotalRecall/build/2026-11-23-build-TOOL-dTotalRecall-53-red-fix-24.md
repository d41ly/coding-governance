# TOOL-dTotalRecall-53 red-fix 24 — install-prefix (shipped surface) fixed in 6cb81cf0

**Serves:** red-fix TOOL-dTotalRecall-53

- **Leg:** install-prefix (shipped surface)
- **Red line:** install-prefix: memory_measure.py's parent-relative plant set its working directory under the memory-tree kit's path
- **Files:** tools/runlog/memory_measure.py
- **Commit:** 6cb81cf0c5fe85cb5a8ff272d07be53b4430608d
- **Rerun:** bash tools/check-install-prefix.sh: clean, 0 kit-path spellings; the parent-relative fixture still counts its 250 shell bytes (DERIVED 2026-11-23, `memory_measure.py#print_memory_fixture`)
- **Caused-by:** TOOL-dTotalRecall-53
