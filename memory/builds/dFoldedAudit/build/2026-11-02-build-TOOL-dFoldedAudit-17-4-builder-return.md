# dFoldedAudit — unit 17's builder return, second dispatch

**Serves:** journal TOOL-dFoldedAudit-17

Run direct/a27c06415241e12f4, summarized from its task notification.

- DIVERGENCE: pre-commit's branch guard (`.githooks/pre-commit:71-93`) refused merge commit M. The guard refuses any commit made in a primary tree while it is on a non-default branch, and the scratch clone is a primary tree. Its only overrides are `--no-verify` and `GOV_DEFAULT_BRANCH`, so the builder stopped rather than use either. Every other pre-commit leg passed.
- Staged before the refusal: AC1 held at exactly eight paths, with the merge drivers set. AC2's marker counts matched their pins, at 46 and 21, and no marker remained after resolving. AC3, AC4 and AC5 held, with `FLOOR_ASSERTIONS=215`. AC10's `gen_map.py --check` and `gen_build_index.py --check` exited 0. The staged blobs carry no CR. The staged `policy.json` is HEAD's blob.
- Not run: AC6, AC7, AC11 and AC13 need M or F. AC8, AC9 and AC12 are the main loop's at the close.
- Smaller points:
  - S7 is wrong that no §B line names the resolver floor: manifest line 223 does. Main added that line in `201eb127` and it is current, so the expected manifest delta is still none.
  - The kit spells the manifest line `manifest-audit: delta none · watch-commits-since-stamp: <n>`, and n is 13.
  - Main's side adds `docs-undocumented.txt` to `PROJECT_REGISTRY_EXTRA`, and it merges clean.
  - `gen_build_index.py --write` also rewrites dSafePassage's README generated block, the 2026-11 ledger and the dClosedLoop as-built view.
  - The `:1405` citation points at the stamp-sha rule.
- The clone was deleted, and no commit was made. The fetched tip is `84acebdc`. The run worktree is clean at `80471d36`.
- The builder's draft trailer was `Claude Opus 5`, which is the charter's, while the run's last seven commits carry `Claude Opus 5.5`. The charter's trailer governs.
