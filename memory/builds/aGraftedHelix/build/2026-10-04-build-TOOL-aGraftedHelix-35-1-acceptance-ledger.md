# Acceptance ledger — TOOL-aGraftedHelix-35

**Serves:** journal TOOL-aGraftedHelix-35

Node `a`, 2026-10-06. The build commit is `cea1a8af`, over the pass's parent `7a8b2173`, the spec
commit. No merge bar and no self-test suite ran in this pass. AC1 to AC4 ran as a slice generated
into the session scratchpad, `gh35-slice.sh`: the build-harness suite's prologue with its kit dir
pinned and its layout dir a short path under `%TEMP%`, the engine pin, the GH15 spec commit block, the
GH16 lines that derive the kit dir, and the GH35 block, 49 assertions, green at `cea1a8af`. Each
staged break was a scratch copy of the render read through the slice's `SLICE_F` override, so the
shipped render was never edited: the parent render, `git show 7a8b2173:tools/workflows/unattended-build.js`,
and four copies of the new render with one line each replaced. The whole suite, and the bar, are the
main loop's, at VERIFYING.

**Evidences:** TOOL-aGraftedHelix-35
- AC1 — `NEW/CHANGED invariant inv-build` — the step-6 command extracted from the commit prompt and run in the three-commit fixture printed the base's read point, the item, and `# by design — 1` over `inv-base` alone; the resolver's extracted command printed the same read point; fed back as the doubles' checklists, the audit's `wargs:` checklist carried the item under `# by design — 0` with neither entry. On the parent render the extracted command was `--for-diff HEAD~1..HEAD`, which in the fixture printed `# by design — 2` over `inv-base` and `inv-build`, and eight of the nine arms failed; the ninth, the resolver's read point, held because the parent's resolver was already pinned.
- AC2 — `inv-two` — the rewritten GH15 arm read the merged checklist opening `# r-head`, `# invariants are read at r-point`, the label and `# c-head`, then `# by design — 1` over `inv-one` alone, with no `inv-two` and no `c-point`; on the parent render the opening arm and all three rewritten arms failed, the second input's entry and read-point line both present.
- AC3 — `inv-keep` — the omission arm read `# by design — 1` over `inv-keep` closing the checklist string, no `- inv-q — ` or `- inv-z — ` entry, and both NEW/CHANGED items in order; with the name filter cut in a render copy (`return true`) its first three arms failed and nothing else did.
- AC4 — `prompt:commit:specs:tB:` — a 40-hex `base` with the audit on put the pinned `--for-paths --base` command with `$(git diff --no-renames --name-only HEAD~1..HEAD)` on that prompt line and on the label line, and logged `merged with the spec commit 89abcdef0123's --for-paths at base fedcba987654 (its by-design block left out)`; no `base` and `origin/main` with the audit off kept `--for-diff HEAD~1..HEAD` and logged the WARNING; a 40-hex `base` with the audit off was pinned and logged none. Staged: the pinned branch cut failed 11 arms, the warning deleted failed the two WARNING arms, and the shape test dropped failed both `origin/main` arms.
- AC5 — `git status --porcelain tools/workflows/` — printed nothing at `cea1a8af` after `--render`; `node tools/workflows/check-workflow-syntax.js` printed `6 workflow script(s) parsed clean`; `python tools/workflows/check_by_design_parity.py tools/memory-tree` exited 0 with agreement for both templates; `grep -c "by-design block left out"` printed 1 for the README and 2 for the render; `grep -c "s --for-diff output"` printed 0 for the render.
- AC6 — `bash tools/check-kit-versions.sh` — printed `kit-versions: clean — 16 declared carrier(s) under tools/`; `python tools/govkit/govkit.py epoch --base 7a8b21732` printed `epoch: review-harness · clean · 1.41` and no other entry off clean or skip; line 3 of `tools/workflows/unattended-build.js` moved from `1.10` at `7a8b2173` to `1.11`, and the suite's `BT3-AC7` pin reads `1.11`, green in the slice.
