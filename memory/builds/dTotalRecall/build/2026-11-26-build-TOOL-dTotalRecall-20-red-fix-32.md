# TOOL-dTotalRecall-20 red-fix 32 — routed commits name a specced unit fixed in d6067829

**Serves:** red-fix TOOL-dTotalRecall-20

- **Leg:** routed commits name a specced unit
- **Red line:** a Red-fix commit is outside the inline lane's limits: d0e02120 L1 size: 2 path(s), 69 line(s); the bound is 3 and 60
- **Files:** help/red-fix-lane.md, tools/memory-tree/README.md, tools/memory-tree/routed_commits.py
- **Commit:** d6067829e715dbb5eb916c351febd8d0ada0f0f4
- **Rerun:** python tools/memory-tree/routed_commits.py --red-fix-limits d0e02120b: d0e02120 is inside all four, bound 3 path(s), 69 line(s); the suite runs in the landing bar, gate-guard refusing it while the run is HELD
- **Caused-by:** TOOL-dTotalRecall-20
