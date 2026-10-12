# Brief — cListedCensus: ps-hygiene grades tracked files, not a walk

**Serves:** research TOOL-cListedCensus-1

## The prompt

> In coding-governance (C:/projects/coding-governance, remote origin d41ly/coding-governance), tools/gate-lint/ps-hygiene.py builds its population with `root.rglob("*.ps1")` plus a SKIP_DIRS prune. An adopter that keeps linked worktrees INSIDE the primary tree (NicoCares d41ly/nc keeps them at `.claude/worktrees/<name>/`, untracked) gets every sibling checkout's .ps1 graded. On 2026-10-11 nc's push-main.sh went red on 6 findings, all in untracked nested-worktree copies, and the run-gates red-leg attribution re-ran the leg in a fresh worktree (no nested worktrees), saw green, and labelled the red OWN, refusing the landing.
>
> nc fixed it locally as `nc carve-out 34/4` (PKG-bIndexedHarrow-1, nc commit bcc6f8a4 on branch branch/interesting-hugle-a7aa84; nc's backlog row PKG-bIndexedHarrow-2 is the upstream ask). The previous local fix (PKG-bStitchedFerry-3, 2026-09-11) was erased by a govkit pull because it was never upstreamed — that is why this must land in gov.
>
> Task: change tools/gate-lint/ps-hygiene.py so `scan(root)` takes its population from `git ls-files -z -- '*.ps1'` run with cwd=root (same shape as the sibling tools/gate-lint/sh_hygiene.py `scan_tree`): a non-zero git exit raises OSError -> main prints it and exits 2; zero tracked .ps1 files is a refusal (exit 2, "graded NOTHING — that is a refusal and not a pass"), mirroring sh_hygiene; drop SKIP_DIRS (it existed only to prune the walk); `scan` returns (findings, scanned) and main reports "N tracked .ps1 file(s)". The nc file at C:/projects/incms/main/vendor/nicocares-package/.claude/worktrees/interesting-hugle-a7aa84/scripts/gate-lint/ps-hygiene.py (or `git -C C:/projects/incms/main/vendor/nicocares-package show bcc6f8a4:scripts/gate-lint/ps-hygiene.py`) is the reference implementation — take it minus the `# nc carve-out 34/4` comment block, and keep the module docstring's exit-code and TRACKED-not-walked paragraphs. Consider adding --selftest arms over a scratch git repo: a tracked BOM-less non-ASCII .ps1 reds, an untracked copy under `.claude/worktrees/x/` does not, not-a-repo exits 2, empty tracked set exits 2 (hold GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE out of the env during it, as sh_hygiene's selftest does). Follow gov's own AGENTS.md/CLAUDE.md (mint a slug, records, gate bar); merging to gov main and pushing need the owner's explicit ask.

## The brief

### Goal
`tools/gate-lint/ps-hygiene.py` grades the `.ps1` files the index holds instead of every `.ps1` on
disk under the root, so worktrees an adopter parks inside its tree are never graded, and a probe that
died or an empty population refuses with exit 2.

### Items
1. The population is `git ls-files -z -- '*.ps1'` with `cwd` at the root; `SKIP_DIRS` goes.
2. A failed listing and a zero count each exit 2; the report lines count tracked files.
3. `--selftest` arms over a scratch repository: tracked bad reds, untracked copy under
   `.claude/worktrees/x/` does not, not-a-repo and an empty tracked set each refuse.
4. The kit README, the root README's kit line and the gate-lint dossier say what the scanner does now.
5. A gov class record for a walk from the root that reads other worktrees.

### Acceptance
Spec §6: AC1 the selftest arms, each observed red under a staged break; AC2 nc's primary tree, BASE
exits 1 on worktree copies and the new scanner exits 0; AC3 gov's tree refuses with exit 2; AC4 the
class record is selected for the scanner's path.

### Gates
`bash tools/run-gates/run-gates.sh`, plus `python tools/gate-lint/ps-hygiene.py --selftest`, which no
leg runs.

### Non-goals
No leg for the scanner and no `kit.toml` edit. No `.psm1`. No fix for other walks. No `GIT_DIR` scrub
in the scanner's own listing. No merge and no push without the owner's ask.

### Limitations
The scanner ships to adopters by copy, so its exit codes are their contract: an adopter with no
tracked `.ps1` that wired it goes red, and the README has to say so.

### Reuse
`scan_tree` and the scratch-repository selftest block in `tools/gate-lint/sh_hygiene.py`; nc
`bcc6f8a4`. Recall returned `TOOL-cMendedVintage-2`, `TOOL-aLeakedHandle-1` and
`TOOL-aRepatriatedFork-3`.

## Drawn from the session

> Tier 2 (Recommended)
— owner, the kickoff's tier question

> No (Recommended)
— owner, the kickoff's spec-audit question

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: go
