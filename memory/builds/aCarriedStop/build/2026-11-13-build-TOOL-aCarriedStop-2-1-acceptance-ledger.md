# Acceptance ledger — TOOL-aCarriedStop-2

**Serves:** journal TOOL-aCarriedStop-2

Built against spec rev-1 in one pass commit. AC1 to AC3 are driver runs the builder made in the pass, on node a, in the spec's probe fixture, each from a fresh fixture. AC4 and AC5 are the criteria's own commands over the worktree. No suite, gate leg or bar ran in the pass. Owed to the main loop at the close: the new suite arm's red-then-green run, against the driver at `cfda7001` and then this one, and the legs of the spec's Gates section.

**Evidences:** TOOL-aCarriedStop-2
- AC1 — `git ls-files '*-chain-rounds.md'` — under the root `mem+ory` the owner-stop call exited 1 and printed the check 118 opening, the folder refusal naming the path's class, and the cited path; the listing then printed nothing and the build held no `build/` folder.
- AC2 — `run --chain-verdict dFix` — under `memory` the nested path, the bare folder, the name holding a space and the spec path each exited 1 with the check 118 opening, the folder refusal and its path; the `..` path exited 1 with the untracked-file refusal; the stop record then recorded at exit 0, and the verdict printed the criterion's STOP line, byte for byte.
- AC3 — `run --chain-verdict dFix` — after the commit and the appended `a+b.md` row it exited 1 and printed the check 118 opening followed by the criterion's hand-edit text, ending in the appended row.
- AC4 — `grep -c 'file name leaves' tools/unattended/unattended.sh` — the four counts printed 1, 1, 0 and 319, in the criterion's order. (PINNED, 2026-11-13)
- AC5 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` — it printed nothing after the adopter's re-render; the whole-path class grep printed 1 over the template and 1 over the help page, and the file-name class grep printed 0 over each.
