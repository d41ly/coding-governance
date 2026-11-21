# TOOL-dPlacedRequest-2 red-fix 49 — shell hygiene (a stage committed with no staged-diff test) fixed in b833648b

**Serves:** red-fix TOOL-dPlacedRequest-2

- **Leg:** shell hygiene (a stage committed with no staged-diff test)
- **Red line:** skills/session-kickoff/manifest-check.sh commits the card snapshot after its add with no staged-diff test between them
- **Files:** memory/guides/SESSION-KICKOFF.md, skills/session-kickoff/manifest-check.sh, skills/session-kickoff/manifest-check.test.sh, tools/run-gates/run-selftests.sh
- **Commit:** b833648b1cac7a7ad2d451b4d3f84b145e3f7821
- **Rerun:** python3 tools/gate-lint/sh_hygiene.py --stage-commits memory/project/stage-commit-sites.txt . :!*.test.sh :!memory/
- **Caused-by:** TOOL-dPlacedRequest-2
