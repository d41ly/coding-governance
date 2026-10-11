# Acceptance ledger — TOOL-dRemeasuredRender-1

**Serves:** journal TOOL-dRemeasuredRender-1

Built on `c922c7e2`. Each bare site was rewritten by inserting the scrub at the offset the scanner's
remedy line names, in the original line, so a trailing comment the remedy line drops is kept. Two
rounds converged: the first rewrote 58 lines, the second found 0 GATED. Base was observed in a
detached worktree at `17472e21`.

A probe in the session scratchpad, two fresh repositories and `GIT_DIR` exported at the second:
the bare `git -C <a>/sub rev-parse --show-toplevel` answered `<a>/sub`, the scrubbed form answered
`<a>`, and in a clean environment both answered `<a>`. So the scrub is a no-op for a suite run
from a clean environment, and the fix where a hook exports `GIT_DIR`. No touched suite assigns
`GIT_DIR` at a probe site: the two that assign it do so as a prefix on one subject invocation.

One scanner blind spot was found and filed rather than adopted: `TOOL-dRemeasuredRender-2`.

**Evidences:** TOOL-dRemeasuredRender-1
- AC1 — `sh_hygiene.py --location-probes` — with no registry and no pathspec it printed `[GATED] 0 site(s) in 0 file(s)` and `[scrubbed] 95`, rc 0; at base it printed `[GATED] 58 site(s) in 30 file(s)`
- AC2 — `:!*.test.sh` — gov's row with that token dropped exited 0 here; the same argv at base exited 1 over 58 GATED sites, and the row as shipped at base exited 0
- AC3 — `bash -n` — all 30 touched suites parse; over the staged diff, 58 changed lines each equal their base line with one `unset GIT_DIR GIT_WORK_TREE; ` removed, and 0 differ otherwise

## Owed at the close

The 24 touched suites outside `tools/unattended/` run as the legs the spec's §7 names, in the
close's flagged bar. The six `tools/unattended/` suites are not run; their full run is handed to the
owner in the wrap-up.
