# TOOL-dTotalRecall-12 red-fix 23 — install-prefix (shipped surface) fixed in 3e1f2194

**Serves:** red-fix TOOL-dTotalRecall-12

- **Leg:** install-prefix (shipped surface)
- **Red line:** install-prefix: memory_measure.py's fixture spelled the harness run folder as a kit-shaped literal segment
- **Files:** tools/runlog/memory_measure.py
- **Commit:** 3e1f219405a65fecc41c46b301647450e50719a0
- **Rerun:** bash tools/check-install-prefix.sh: clean, 0 kit-path spellings
- **Caused-by:** TOOL-dTotalRecall-12
