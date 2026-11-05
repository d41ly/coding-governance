# Acceptance ledger — TOOL-dFairHearing-31

**Serves:** journal TOOL-dFairHearing-31

Built against spec rev-3 at pass commit `748770f09`, whose parent is `363219765`. The main loop drafted
this ledger at the close from the builder return. `version_lines.py` is the spec's script byte for
byte, written under the pass's scratch directory, and the fixture repositories under `%TEMP%` were
removed after the probe. No suite, gate or bar ran in the pass. The spec's Gates section declares no
new arm, and its legs are owed to the close.

**Evidences:** TOOL-dFairHearing-31
- AC1 — `python version_lines.py .` — at the commit it printed `base 8bec4cefd957d194660a8d7c2916f420b7299074 from origin/main`, which equals `git merge-base HEAD origin/main`, printed no `-` line and exited 0
- AC2 — `GATE_BASE=nosuchref` — it exited 2 printing `version-lines: no base, nothing diffed: GATE_BASE does not resolve: nosuchref`. `GOV_REMOTE=nosuch` exited 2 with the remote ladder's own refusal, and neither printed a `base` line. In the clone under `%TEMP%/fvb` with its remote removed, it exited 2 printing `no base, nothing diffed: no remote, or its HEAD names no default branch`
- AC3 — `-const KIT_X_VERSION = '1.0'` — in the clone under `%TEMP%/fvb`, cloned from the one-commit `%TEMP%/fva`, branch `work` rewrote the line to `'1.1'` in `tools/hooks/x.js`. With this repository's `tools/lib` as the second argument, the probe printed that line and exited 1

## Supersessions

Each one is named by a hands-off bullet in this unit's spec, in `TOOL-dFairHearing-23`'s form. S1 and S2's base stands against units 33 and 34.

- S3's constant alternative and AC1's clause that no constant line changed — answered by `TOOL-dFairHearing-33`'s S1 to S3 and AC1 to AC3
- S3's four-directory pathspec, its marker alternative and AC1's clause that no marker line changed — answered by `TOOL-dFairHearing-34`'s S1 to S3 and AC1 to AC3
- S1's computation in the script, the merge-base of `HEAD` with `GATE_BASE` — answered by `TOOL-dFairHearing-36`'s S11 to S13 and AC8. `GATE_BASE` is taken unchanged, and the ladder base is read through `resolve_compare_base`
