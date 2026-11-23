# TOOL-dTotalRecall-20 red-fix 22 — install-prefix (shipped surface) fixed in d0e02120

**Serves:** red-fix TOOL-dTotalRecall-20

- **Leg:** install-prefix (shipped surface)
- **Red line:** install-prefix: the rendered verb shim blocks in gen_build_index.py spelled the kit path under the literal tool root
- **Files:** tools/govkit/shims.py, tools/memory-tree/gen_build_index.py
- **Commit:** d0e02120b3a5d99d2fdb7116f8b3a510dcec325f
- **Rerun:** bash tools/check-install-prefix.sh: clean, 0 kit-path spellings
- **Caused-by:** TOOL-dTotalRecall-20
