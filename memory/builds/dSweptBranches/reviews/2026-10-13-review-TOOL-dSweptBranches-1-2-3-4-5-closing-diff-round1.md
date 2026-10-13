**Serves:** diff-review TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5

# Tier-2 closing diff review: dSweptBranches, ROUND 1

*This is the closing review of build dSweptBranches (gov, node `d`, 2026-10-13): the new shipped
kit `tools/branch-reconcile/`, built as TOOL-dSweptBranches-1..5. It covers the cumulative diff at
the integration boundary. The fan ran through `tier2-review.js`: five finder lenses, then five
skeptic batches prompted to REFUTE, then this synthesis. Every finding below survived its skeptic.
The author of this report re-read the load-bearing lines in the tree rather than transcribing them
from a lens: the containment filter in read_dirt (`branch_reconcile.py:255-271`), check_worktree's
`if st is None: return None` and the probe predicate (`:630-678`), derive_action's keeps
(`:798-815`), remove_worktree's fallback (`:880-900`) and the lease-less push (`:970-985`).*

**Reviewed range:** a8f0e195a2d80a6d1480e4992aec6565342e35ea...0ac2418c05fad32467e20a93f04b8546383a1c4d. **ROUND:** 1.

## Verdict: BLOCKED

Two blockers survived. The first (id 23) is reproduced data loss: `--write` removes a deletable
linked worktree together with a live, uncommitted worktree nested inside it. The second (id 18) is
a selftest that certifies the primary-worktree and default-branch keeps while neither keep is ever
the thing that saves anything. Seventeen HIGH findings sit behind them. Most are the same costly
error from the security model: unlanded or ungraded content reads deletable on a narrow path. The
kit is a deletion tool, so narrow paths still end in `rm -rf`. It does not land until the blockers
and the HIGH data-loss items are folded and re-reviewed.

## Review shape

Intensity full: raw 30, confirmed 28, refuted 2, unverified 0 (0 uncertain), precision 0.93.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| seams | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |
| verification | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| intent | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |

The adjudicated tally, counted two ways:

- **By item:** 2 BLOCKER, 10 HIGH, 4 MEDIUM, 3 LOW, which is 19 items.
- **By raw confirmed finding:** 2 blocker, 17 high, 5 medium, 4 low, which is 28 findings.

Several items merge findings that several lenses reported independently:

- H1 merges ids 2, 9, 15 and 26 (status not read, HEAD decides).
- H3 merges ids 4, 11 and 25 (the patch predicate's absolute drift).
- H4 merges ids 3 and 13 (the probe name predicate).
- H5 merges ids 5 and 24 (the rotated predicate accepts an edited row).
- M1 merges ids 20 and 28 (the write fixture lacks SUPERSEDED and a stash).
- L1 merges ids 17 and 30 (no skip line without a memory tree).

**Run integrity.** Every count that would mark the run incomplete is zero, so the run is complete:

- Lenses: 5 of 5 returned, 0 died.
- Skeptic batches: 5 of 5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 22 judged sound, 6 judged UNSOUND (ids 1, 3, 4, 7, 13 and 23; each
  skeptic's corrected fix is written below, never the rejected one), 0 with no fix proposed, 0 not
  judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 2 re-graded by the skeptic (ids 1 and
  15, each from blocker to high).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 7 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 17 items, each assigned to exactly one of 5 lenses (security 4, correctness 4,
  seams 3, verification 3, intent 3).
- By design: the caller's byDesign list.

## Asked-for surfaces with no finding

The brief asked for four surfaces to be reported whether or not they produced a finding.

- **Remote/default ladder.** The inlined `remote_ladder_py` block (`branch_reconcile.py:78-130`) is
  byte-identical to the canonical block in `tools/lib/resolve_remote.py:16-68`. This author checked
  it by hashing both marker-delimited bodies, and the digests match. The ladder's consumer is a
  separate story: H6 (id 6) shows that derive_action discards the ladder's observed remote HEAD.
- **Adopter names.** No shipped file under `tools/branch-reconcile/` names an adopter. A grep for
  the known adopter names returned nothing. `selftest.py` is withheld through `kit.toml`'s
  `include`, and the gov-only leg is carried by an `[[exempt_leg]]` row.
- **Literal `tools/` paths.** No literal `tools/` segment appears in `branch_reconcile.py`,
  `README.md` or `SKILL.template.md`. The only occurrences in `adopt-branch-reconcile.sh` are its
  own refusal check (`:71-73`) and the comment describing it.
- **Byte-stability of the report.** No lens raised a finding. This author did not re-run the
  determinism arm, so read that as the lenses' silence and not as a fresh measurement.

## BLOCKER

### B1. `--write` removes a live worktree nested inside a deletable one (id 23)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:268` (read_dirt's containment filter).
  Nothing in derive_action (`:798`), build_rows or write_deletions checks the reverse direction.
- **Grade:** blocker, which is the binding grade. This report agrees: it is reproduced, it is
  reachable by the routine "session in a linked worktree makes harness worktrees under its own
  `.claude/worktrees/`" layout, and the loss cannot be recovered.
- **Defect:** read_dirt drops an untracked path that IS another worktree, for every worktree. Spec
  1 scoped that drop to the primary. It is checked one way only. Write mode never asks whether a
  worktree it removes CONTAINS a kept worktree.
- **Impact:** reproduced on a throwaway fixture with the shipped CLI. Linked worktree X (MERGED,
  old) held worktree Y at `X/.claude/worktrees/Y`, and Y held an untracked `precious.txt`. The
  report graded Y `UNMERGED-LIVE · keep` and X `MERGED · remove worktree`. `--write` printed
  `removed — worktree X · git worktree remove`, and `precious.txt` was gone. The recovery manifest
  records HEAD shas only.
- **Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):**
  1. In build_rows, compute each worktree row's base action with derive_action first.
  2. Before building the `kept` branch set, demote every `remove worktree` row to
     `keep · contains kept worktree <name>` when `check_under(other_path, its_path)` holds for any
     worktree row whose base action is not `remove worktree`. Containment is transitive, so one pass
     suffices.
  3. Only then build `kept` from the final worktree actions and derive the local-branch actions.
     Doing it after the actions are assigned, as the finder proposed, leaves X's branch reading
     `delete branch` in the report while write mode keeps it as still checked out.
  4. Add a selftest arm with the nested-in-linked fixture, and observe it red first.
- **Left-shift gate:** this class is containment filtered in one direction and acted on in the
  other. Add a selftest invariant run over every write fixture: no `remove worktree` row's path is
  an ancestor of any kept row's path. Add a §10 checklist entry: "a filter that hides X inside Y owes
  a guard that acting on Y spares X".

### B2. The write arm never exercises the primary-worktree or default-branch keeps (id 18)

- **Where:** `tools/branch-reconcile/selftest.py:606` (arm_write). The untested keeps are
  `branch_reconcile.py:805-809` and the name filter at `:976`.
- **Grade:** blocker, which is the binding grade. The rubric names a check that certifies what it
  does not check, and the uncovered protection is the costliest error class in the security model.
  The exclusion code is correct today.
- **Defect:** arm_write runs every `--write` from the primary, which has `main` checked out. The
  primary therefore reads IN-PROGRESS (invoking) and is kept by its verdict. Local `main` is saved by
  `kept_branches` and by write_deletions' `still` set. Remote `main` is filtered by the separate
  `names != inv['branch']` line.
- **Impact:** measured by mutation. Deleting the `worktree/primary` keep, or both default-branch
  name checks, leaves arm_write at 12 passed, 0 failed. Spec 3 AC2 says it reds "when ... the default
  branch is not excluded". Two reachable paths have no check:
  - `--root` run from a linked worktree reads a clean, old primary as MERGED. Only the kind clause
    then stops remove_worktree, whose git refusal falls through to `rm -rf` on the primary and its
    `.git`.
  - A primary checked out on a feature branch leaves local `main` MERGED. Only the name clause
    stops `git branch -D main`.
- **Fix (judged SOUND by the skeptic):** add a write arm that checks the primary out on another
  branch (or detaches it), runs `main()` with `--root` pointed at a linked worktree, at
  `--fresh-hours 0`. Assert that the primary directory and local `main` both survive, and that
  their rows carry `keep · the primary worktree` and `keep · the default branch`. Observe it red with
  each clause removed. The skeptic notes that write_deletions' redundant name guard cannot red alone
  while derive_action keeps the row, so that mutation reds through the row-text assertions only.
- **Left-shift gate:** this class is a keep that is never the deciding keep. Make every keep in
  derive_action carry a mutation arm in selftest.py: a table of (clause, fixture) pairs, each run
  with the clause removed and expected red. A clause added to derive_action without a row in that
  table reds the selftest.

## HIGH

### H1. A worktree whose status was never read takes its HEAD's verdict and is `rm -rf`'d (ids 2, 9, 15, 26)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:641` (`if st is None: return None`; id 15
  anchors it at `:640`). read_dirt returns None at `:261-262`.
- **Grade:** high for all four, which is the binding grade. The skeptic re-graded id 15 from blocker
  to high. This report agrees: the trigger is a directory that exists while its status cannot be
  read (a missing `.git` file, a corrupt index, a dubious-ownership refusal), which is narrow, and
  the consequence is data loss.
- **Defect:** `w["dirt"]` is None for a prunable worktree, a missing directory or a failed
  `git status`. check_worktree returns None, so the HEAD's ref ladder decides the row. The
  `status not read` flag is printed, and nothing reads it. read_newest_activity reads only the HEAD
  commit time when dirt is None, so dirty-file mtimes cannot raise IN-PROGRESS either.
- **Impact:** reproduced twice. A worktree at `main`'s tip whose `.git` file was gone, holding an
  untracked file, read `MERGED · remove worktree · prunable · status not read`. `--write` logged
  `rm -rf after git refused (validation failed ...)`, and the directory and its file were gone,
  exit 0. This contradicts spec 2 S5 and S1.6 and README line 109. The BY-DESIGN `rm -rf` fallback
  assumes the content was graded, and here it was not.
- **Fix (judged SOUND by the skeptics, ids 2, 9, 15 and 26):** in check_worktree, when `st is None`
  and `os.path.lexists(w["path"])`, return `(UNKNOWN, "worktree status could not be read; its
  content is ungraded")`. Only a prunable worktree whose directory is truly gone may fall through to
  the HEAD's verdict and be pruned. Have read_worktrees record why status was not read. Add a
  selftest arm: a prunable worktree whose directory still holds an untracked file must read UNKNOWN
  and survive `--write`. The census arm's prunable fixture deletes its directory first, so it never
  covered this case.
- **Left-shift gate:** this class is an undecided predicate read as "no objection". Add a selftest
  property arm: for every fixture row whose evidence says `not read`, assert its verdict is not in
  DELETABLE. Add a §10 checklist entry: "a predicate returning None means undecided, and undecided
  never falls through to a deletable verdict".

### H2. A foreign repository at a registered worktree path is graded on the stale HEAD and `rm -rf`'d (id 1)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:894` (remove_worktree's fallback), with the
  readable test in read_worktrees at `:318`.
- **Grade:** high, which is the binding grade. The finder graded it blocker and the skeptic
  re-graded it high. This report agrees: a worktree directory has to be replaced by another
  repository, which is narrow.
- **Defect:** git flags a worktree prunable only when `<path>/.git` does not exist, so a `.git`
  DIRECTORY there reads as a readable worktree. read_dirt then reads the foreign repository's
  status, which is clean, and the row takes the stale registered HEAD's verdict.
  `git worktree remove` refuses with `is not a .git file`, and the fallback runs `rm -rf` without
  checking what the path holds.
- **Impact:** reproduced with `git worktree add ../wt; rm -rf ../wt; git init ../wt`, then a commit
  there. `--write --fresh-hours 0` printed `removed — ... rm -rf after git refused (... is not a .git
  file ...)`, and the foreign repository and its unpushed commit were gone. The manifest records
  only the stale worktree HEAD.
- **Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):**
  1. In read_worktrees, when `os.path.lexists(path)`, require `<path>/.git` to be a FILE whose
     `git -C <path> rev-parse --git-common-dir`, normalized with derive_key, equals the inventory
     root's common dir. Otherwise mark the row foreign and grade it UNKNOWN in check_worktree.
  2. In remove_worktree, when the path does not exist, run only `git worktree prune` and report
     removed.
  3. Otherwise, run the `rm -rf` fallback only when the same `.git`-file and common-dir check passes.
  4. Add a selftest arm with a foreign repository at a registered path that must read UNKNOWN and
     survive `--write`.
  Running `rm -rf` only after the check, without step 2, would turn the prunable-but-gone case into
  a failure with exit 1.
- **Left-shift gate:** this class is an identity assumed from a registry and not re-proved at the
  path. Add a §10 checklist entry: "before a recursive delete, prove the target belongs to this
  repository's common dir".

### H3. The `patch` predicate covers a commit with an unrelated same-subject commit (ids 4, 11, 25)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:546` (derive_coverage, `:543-548`).
- **Grade:** high for all three, which is the binding grade. It needs a same-subject commit on the
  default side since the merge base, and every other unique commit covered.
- **Defect:** a candidate with the identical subject matches when its `-U0` +/- line multiset
  differs by at most DRIFT_LINES=4, an absolute bound. read_patch_lines drops the file headers, so
  file names never enter the comparison. `{-a,+b}` against `{-p,+q}` differs by exactly 4. A
  binary-only or mode-only commit has an empty multiset and matches any same-subject commit of at
  most 4 lines.
- **Impact:** reproduced. Branch `fix: typo` adding `b.txt` and an unrelated `fix: typo` on `main`
  adding `c.txt` read `SUPERSEDED · covered: patch 1`. Generic subjects (`fix typo`, `wip`,
  `records`) make it reachable, `--write` deletes the branch, and `--remote` deletes the remote copy.
- **Fix:** the skeptic judged ids 11 and 25's fixes SOUND and REJECTED id 4's. The corrected fix for
  id 4 agrees with the sound ones. Apply this once:
  1. Require both patches to touch the same file set (read_files equality).
  2. Refuse a match when either multiset is empty.
  3. Keep `drift <= DRIFT_LINES`, and additionally require `common = sum((a & b).values())` to be
     greater than 0 and greater than the drift.
  4. Add negative arms to arm_patch: two same-subject one-line commits on disjoint lines, and on
     different files, must read UNMERGED-LIVE.
  Do not use id 4's rejected example bound `drift <= min(4, common/2)`. It breaks the spec's own AC1
  arm, where `two.txt` shares 6 lines and drifts by 4. The `common > drift` rule keeps both AC1
  fixtures green.
- **Left-shift gate:** this class is a similarity predicate with no negative arm. Require every
  coverage predicate in derive_coverage to carry a negative arm built from the predicate's boundary,
  meaning the smallest input that sits exactly on the bound. A selftest table keyed by predicate name
  makes a predicate without a negative row red.

### H4. An untracked probe counts as covered on a bare name substring anywhere in the default tree (ids 3, 13)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:673` (check_worktree's probe clause).
- **Grade:** high for both, which is the binding grade. It needs a name collision, a deletable HEAD
  and activity past the freshness bound.
- **Defect:** each extracted case name passes `git grep -F -q -e <name>` over the whole default
  tree. That is an unanchored substring match in any file, and the probe's body is never compared.
  `it("works")` captures `works`, and `test_parse` matches inside `test_parse_args` or in prose.
- **Impact:** an idle worktree holding an untracked test file full of new code plus one generically
  named case reads `probe ...: its case landed as a test`. The worktree takes its HEAD's deletable
  verdict, and `--write` deletes a file that has no git object and no manifest entry.
- **Fix (both REJECTED by the skeptics; these are the corrected fixes, composed):**
  1. From id 13's correction: anchor each case to the declaration form it was extracted with, using
     `git grep -E -q` over the default tip, the name ERE-escaped, and POSIX classes rather than a
     backslash-s class: `def[[:space:]]+<name>[[:space:]]*[(]` for a Python case,
     `(it|test)[(][[:space:]]*["']<escaped>["']` for a JS case, and
     `^[[:space:]]*arm[[:space:]]+"<escaped>"` for an arm. Keep the blob clause unchanged.
  2. From id 3's correction: anchoring alone still collides when another default-branch test
     declares the same generic name with a different body. So also require every non-blank line of
     the probe to exist in a file that matched the declaration, checked with `git grep -F -x` per
     stripped line restricted to those files. Otherwise the probe is uncovered.
  3. Add negative arms: the default holds only a longer name with the probe's name as its prefix,
     and the default holds the name only in prose or under another body. Observe each red before
     the fix.
- **Left-shift gate:** the same predicate negative-arm table as H3. Add a §10 checklist entry: "a
  name match is not a content match; a coverage predicate compares the bytes it claims are covered".

### H5. The `rotated` predicate covers a commit that edits an existing row (ids 5, 24)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:562` (the rotated arm), with derive_row_ids
  at `:451-465` and check_row_on_default at `:441-448`. Id 24 anchors it at `:461`.
- **Grade:** high for both, which is the binding grade. Every unique commit must be a row-only edit
  that no other predicate covers.
- **Defect:** derive_row_ids keeps only the id heading each added line and ignores removed lines.
  check_row_on_default asks only whether a row headed by that id exists at the default tip. An edit
  in place (`| TOOL-x-1 | OPEN |` to `| TOOL-x-1 | DONE |`) is satisfied by the OPEN row still on
  the default.
- **Impact:** reproduced. A branch rewriting `| TOOL-aSlug-1 | fix x | open |` to a RESOLVED row with
  new text read `SUPERSEDED · delete branch · covered: rotated 1`. This repo's routine records commit
  is exactly that shape.
- **Fix (judged SOUND by the skeptics, ids 5 and 24):** require the exact text of each added row
  line, stripped, to exist under the memory root at the default tip, for example with
  `git grep -F -x -q -e <line> <default> -- <mem>`, instead of accepting any row with the same id.
  A byte-identical move still matches, and any mismatch errs toward keeping the branch. Add a
  row-edit negative arm to arm_rotated.
- **Left-shift gate:** the predicate negative-arm table from H3, with a row-edit row for `rotated`.

### H6. The default-branch exclusion ignores the remote's own HEAD branch (id 6)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:805` (derive_action), and `:143`, where
  resolve_default discards `_observed`. write_deletions filters only `inv['branch']` (`:976`).
- **Grade:** high, which is the binding grade. It needs a `GOV_DEFAULT_BRANCH` override that
  disagrees with the remote HEAD.
- **Defect:** only the branch the ladder chose is excluded by name. The remote's observed default
  and the other candidate of the main/master fallback are not.
- **Impact:** with `GOV_DEFAULT_BRANCH=develop`, `origin/HEAD -> main`, and `main` an ancestor of
  `develop` (a gitflow layout), `origin/main` reads `delete remote branch (--remote)` and goes into
  the push. A bare remote does not refuse to delete its HEAD branch. Local `main` reads
  `delete branch` too.
- **Fix (judged SOUND by the skeptic):** keep `_observed` from resolve_remote. Exclude every one of
  `{branch, observed}` by name before the verdict is read, both locally and as `<remote>/<name>`,
  and filter them out of the push list in write_deletions. Add a selftest arm where
  `GOV_DEFAULT_BRANCH` differs from the remote HEAD.
- **Left-shift gate:** fold this into B2's keep-mutation table: one fixture per default-branch
  source (override, observed remote HEAD, fallback), each asserting `keep · the default branch`.

### H7. The remote deletion is a lease-less `git push --delete` (id 7)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:979` (write_deletions).
- **Grade:** high, which is the binding grade. It needs `--remote`, a stale or racing tracking ref
  and a concurrent push, and the pushing node usually still holds its commits.
- **Defect:** the verdict was graded from `refs/remotes/<remote>/<n>` as this clone last saw it, and
  the tool never fetches. The push deletes whatever the server holds. The BY-DESIGN no-fetch note
  covers the missing fetch, not deleting a sha that was never graded.
- **Impact:** node B pushes to a branch whose stale tracking ref reads MERGED on node A.
  `--write --remote` on A deletes B's new tip on the server, and the manifest records only the
  stale sha. Even with the skill's fetch, a fetch-to-push window remains.
- **Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):**
  1. Delete remote branches with one lease per ref in the same push:
     `git push --force-with-lease=refs/heads/<n>:<graded tip> ... <remote> :refs/heads/<n> ...`.
     Add `--atomic` if a single refusal should keep every ref.
  2. Report a refused ref as failed.
  3. Keep `git branch -D` for local branches, but immediately before it, skip a branch as moved
     when `refs/heads/<n>` no longer equals the graded tip. Do not switch to `git update-ref -d`,
     which loses `branch -D`'s refusal to delete a checked-out branch and leaves the `branch.<n>`
     config section behind.
  4. Add an arm that advances the bare remote's branch after the fetch and asserts it survives.
- **Left-shift gate:** this class is an act on a ref that was read earlier. Add a §10 checklist
  entry: "every ref deletion carries the sha it graded, as a lease or a compare-and-delete".

### H8. A merge commit's own content is never graded (id 10)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:538` (derive_coverage's merge arm), and
  check_equivalent's trust in `git cherry`.
- **Grade:** high, which is the binding grade. It needs an evil merge whose sibling commits all
  landed by patch. The sha stays recoverable from the manifest until gc.
- **Defect:** for any commit in `<default>..<tip>`, every parent is either in that range or an
  ancestor of the default, so the merge rule is a tautology. Every merge counts as `merge` with its
  diff unread. check_equivalent runs first and trusts `git cherry`, which skips merges.
- **Impact:** reproduced. Branch z had `build(dFoo): TOOL-dFoo-1 — f`, then `merge main into z`
  adding `evil.txt`, and `main` cherry-picked f. z read `EQUIVALENT · delete branch · git cherry:
  all 1 commit(s) already applied`, while `evil.txt`'s bytes exist nowhere on `main`.
- **Fix (judged SOUND by the skeptic):** cover a merge only when it introduces nothing of its own:
  an empty `git show --remerge-diff --format= <merge>` (git 2.36 or later), or `git diff-tree --cc`
  printing no hunks, else a `git merge-tree --write-tree <p1> <p2>` result equal to the merge's
  tree. Apply the same test in check_equivalent before trusting `git cherry` when
  `git rev-list --merges <default>..<tip>` is non-empty. Add a fixture holding an evil merge.
- **Left-shift gate:** add a §10 checklist entry: "a predicate that always holds over its population
  is not a predicate; run it over the real tree and a negative fixture before relying on it".

### H9. Uncommitted submodule content reads covered by `None == None` (id 27)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:663` (check_worktree's changed-path loop).
- **Grade:** high, which is the binding grade. It needs a linked worktree with a submodule holding
  modified or untracked content.
- **Defect:** parse_status adds a submodule path to `changed` for any `S...` record, but counts
  drift only for a pointer change. For `S.M.` or `S..U`, drift is 0. The submodule directory fails
  `is_file`, so it is absent from `have`, and read_default_tree keeps blobs only, so the gitlink is
  absent from `tree`. `have.get(p) == tree.get(p)` is then `None == None`, which grades it
  `sub matches main`.
- **Impact:** the worktree takes its HEAD's deletable verdict. `git worktree remove` refuses
  worktrees with submodules, and the `rm -rf` fallback deletes the uncommitted submodule work.
- **Fix (judged SOUND by the skeptic):** grade a changed path that is a directory, or a gitlink in
  the status record, as unknown (`submodule content`). Treat a path as absent only when
  `not os.path.lexists(path)` and p is not in the default tree. Extend the census submodule fixture
  with modified submodule content.
- **Left-shift gate:** add a §10 checklist entry: "an equality between two lookups is guarded
  against both sides missing".

### H10. No check covers a staged or unstaged tracked edit when content is graded (id 19)

- **Where:** `tools/branch-reconcile/selftest.py:411` (arm_content, `:385-427`); the uncovered
  branch is `branch_reconcile.py:662-667`.
- **Grade:** high, which is the binding grade. The code is correct today, but spec 2 says AC7
  observes this S5 clause, and that will mislead the next change.
- **Defect:** arm_content seeds a landed merge, a landed probe, an untracked file and two clean
  worktrees at `--fresh-hours 0`. The only tracked edits are in arm_census's sibling, which runs
  under the default bound and reads IN-PROGRESS before content is graded.
- **Impact:** measured by mutation. Changing `uncovered.append(f"changed {p}")` to `covered.append`
  leaves arm_census, arm_content and arm_write green (32 passed, 0 failed). With that mutation a
  worktree whose only unlanded work is an edited tracked file reads MERGED and is removed.
- **Fix (judged SOUND by the skeptic):** in arm_content, add a worktree on `main` with one tracked
  file edited unstaged and one staged, both to bytes the default lacks, and assert UNMERGED-LIVE with
  `changed <path>` in the evidence. Add a second worktree whose edit restores the default's bytes,
  and assert it reads its HEAD's verdict. Observe red with the uncovered branch flipped.
- **Left-shift gate:** every `uncovered.append` site in check_worktree gets a row in the same
  mutation table as B2: flip it to covered and expect red.

## MEDIUM

### M1. The write fixture holds no SUPERSEDED row and no stash entry (ids 20, 28)

- **Where:** `tools/branch-reconcile/selftest.py:601` (id 20) and `:600` (id 28), in
  seed_write_fixture (`:554-584`).
- **Grade:** medium for both, which is the binding grade. It is a contained test gap.
- **Defect:** the check named "the fixture holds one row of each verdict" asserts five verdicts,
  with no SUPERSEDED. Spec 3 AC2 asks for one of each, SUPERSEDED named among the deleted. No stash
  exists in the write fixture.
- **Impact:** measured by mutation. Dropping SUPERSEDED from DELETABLE (`:49`) leaves arm_write
  green, and so does deleting the `kind == "stash"` keep (`:803-804`). Without that keep a
  SUPERSEDED stash falls through to `delete remote branch (--remote)`, and the push gets a name
  sliced from `stash@{n}`.
- **Fix (judged SOUND by the skeptics, ids 20 and 28):** add a SUPERSEDED branch (a rebased copy, or
  arm_noop's net-zero branch) with a worktree carrying covered dirty content, and a SUPERSEDED stash
  (arm_stash's landed stash), to seed_write_fixture. Include SUPERSEDED in the asserted set. Assert
  the branch and worktree are gone after `--write`, the stash list is unchanged after
  `--write --remote`, and the push carries only branch names.
- **Left-shift gate:** derive the asserted verdict set from the module's verdict constant instead of
  a hand-typed list, so a fixture missing a verdict reds.

### M2. Gitignored files are deleted without a word (id 8)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:260` (read_dirt's `git status` call).
- **Grade:** medium, which is the binding grade. The loss is contained to ignored, mostly
  regenerable state.
- **Defect:** `git status` runs without `--ignored`, and parse_status has no `!` branch. A worktree
  graded "content covered" loses its ignored files to `git worktree remove --force --force` or the
  fallback.
- **Impact:** a worktree-local `.env`, a local database or scratch output is deleted, and no
  evidence line, manifest entry, spec or README names it. The charter gives each unit its own
  databases.
- **Fix (judged SOUND by the skeptic):** read ignored paths too (`--ignored=matching`, which reports
  a wholly ignored directory as one entry). Then either name them in the evidence (`ignored <n>`),
  or grade a worktree UNKNOWN when it holds ignored files outside a declared disposable set (such as
  `node_modules` or build output). At minimum, state in the README that ignored files are deleted.
- **Left-shift gate:** add a §10 checklist entry: "a status read that feeds a delete names what it
  does not read".

### M3. The AC5 seam check runs in the caller's environment (id 21)

- **Where:** `tools/branch-reconcile/selftest.py:228` (arm_census, `:225-232`). Checklist class C9.
- **Grade:** medium, which is the binding grade.
- **Defect:** the block calls `BR.read_inventory` and `BR.build_rows` in-process outside
  `seed_environ()`. run_git and resolve_remote then read the caller's `GOV_REMOTE`,
  `GOV_DEFAULT_BRANCH`, `GIT_DIR`, `GIT_INDEX_FILE` and global config. That contradicts the
  module docstring's claim that the caller's environment is held out.
- **Impact:** reproduced. With `GOV_REMOTE=origin` exported, arm_census raises a Refusal and fails,
  and its remaining checks are lost. Under a hook's exported `GIT_DIR`, the call inventories the
  hook's repository and passes vacuously.
- **Fix (judged SOUND by the skeptic):** wrap the AC5 block in `with seed_environ():`, as arm_remover
  and arm_write already do. Add an arm that runs with `GOV_REMOTE` set to a non-fixture name in the
  outer environment, to prove the hold-out.
- **Left-shift gate:** C9 is already a checklist class. Make it a gate: a selftest-lint that refuses
  an in-process `BR.` call in selftest.py outside a `with seed_environ()` block.

### M4. The skeleton-link arm uses a dangling link and counts a skip as PASS (id 22)

- **Where:** `tools/branch-reconcile/selftest.py:493` (build_skeleton_remover, `:487-500`), with the
  skip at `:526-532`.
- **Grade:** medium, which is the binding grade. check_holds_file itself is correct.
- **Defect:** the link targets the nonexistent `/c/nonexistent/pnpm/target`, so a link-following
  walk finds no file and AC2 stays green on POSIX. On this Windows node it reds only by crashing on
  WinError 123. When `os.symlink` fails, the arm prints `skipped`, but the check has already
  counted as PASS with no link seen.
- **Impact:** spec 4 AC2 is meant to red when the walk follows a link, and on POSIX it does not.
  Nothing checks that a link target's content outside the worktree survives removal.
- **Fix (judged SOUND by the skeptic):** point one skeleton link at a scratch directory outside the
  worktree that holds a regular file. Assert the worktree is removed and the target file still
  exists, which reds a link-following walk on every OS. When `os.symlink` fails, record the check as
  skipped, not PASS, and keep it out of the PASS count.
- **Left-shift gate:** charter rule `[gate]` already says a skip is not coverage. Gate it in the
  selftest harness: a check that prints `skipped` may not also increment the PASS count.

## LOW

### L1. A repository with no memory tree gets no skip line (ids 17, 30)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:374` (id 17) and `:384` (id 30), in
  read_memory_root (`:374-386`).
- **Grade:** low for both, which is the binding grade. The predicates find no rows and err toward
  not-covered, so only the announcement is missing.
- **Defect:** spec 2 section 4 says a repository with no memory tree skips the records, rotated and
  run-record predicates, announced. read_memory_root silently defaults to `memory`, and nothing
  writes a skip.
- **Fix (judged SOUND by the skeptics, ids 17 and 30):** when `.memory-tree.conf` is absent and the
  memory root does not exist at the default tip, set
  `inv["skips"]["records/rotated/run-record predicates"] = "no memory tree"` and skip those three
  branches in derive_coverage and check_in_progress. Alternatively, amend spec 2 section 4 to
  describe the default.
- **Left-shift gate:** add a fixture with no memory tree to the census arm and assert the `skipped`
  line.

### L2. Spec 3 still names `write_trace` (id 14)

- **Where:** `memory/builds/dSweptBranches/spec/2026-10-13-spec-TOOL-dSweptBranches-3.md:67`, and
  line 101 (AC1). Checklist class C17.
- **Grade:** low, which is the binding grade. It is documentation only.
- **Defect:** rev-2 renamed the trace to `WRITE_TRACE` and changed when it is appended (before each
  act), but section 4 and AC1 still name `write_trace`, which no module exposes.
- **Fix (judged SOUND by the skeptic):** change `write_trace` to `WRITE_TRACE` at lines 67 and 101,
  and say there that each act is recorded before it runs.
- **Left-shift gate:** spec-tokens already pins symbols a spec names. Extend its scope to the
  build's specs so a backticked identifier absent from the kit's source reds.

### L3. An uncreatable manifest directory exits 1 with a traceback, not 2 with a refusal (id 29)

- **Where:** `tools/branch-reconcile/branch_reconcile.py:925` (write_manifest's `base.mkdir`).
- **Grade:** low, which is the binding grade. Nothing is deleted, because the manifest is written
  before any removal.
- **Defect:** the mkdir sits outside the try that converts OSError into Refusal, and main catches
  only Refusal. Spec 3 S2 says a manifest that cannot be written refuses with exit 2.
- **Fix (judged SOUND by the skeptic):** move the mkdir inside the try that converts OSError into
  Refusal.
- **Left-shift gate:** add a write arm that makes the manifest directory uncreatable (a file at its
  path) and asserts exit 2 and an untouched fixture.

## Refuted

- **Id 12** (correctness, `branch_reconcile.py:979`) was refuted as a duplicate of id 7: the same
  lease-less push, the same impact and the same fix. Its extra local `branch -D` window adds nothing
  reachable, since the tool reads and deletes local refs in one process and re-checks for a
  checked-out branch just before.
- **Id 16** (seams, `branch_reconcile.py:812`) was refuted. Overriding a worktree lock with a
  doubled `--force` is the owner-specified removal (brief item 5, spec 4 S1, README:122), not an
  oversight. Keeping every locked worktree would reverse that, and is an owner decision, not a
  review fold.

review-shape kind=diff-review round=1 intensity=full at=synth raw=30 confirmed=28 refuted=2 unverified=0 blocker=2 high=17 medium=5 low=4 agents=11 out-tokens=219854

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/branch-reconcile/branch_reconcile.py:894 | blocker | high | confirmed | read_worktrees (branch_reconcile.py:318) treats a worktree as readable when it is not flagged prunable and its path is a directory. git flags prunable only when <path>/.git does not exist, so a .git DIRECTORY there is not prunable. read_dirt then runs git status and --git-path index inside the foreign repository, so a clean, idle foreign repo produces no uncovered content, and the row takes the stale registered HEAD's verdict, for example MERGED. In git worktree remove, validate_worktree refuses with 'is not a .git file', and remove_worktree (line 891) falls straight to rm -rf with no check of what the path holds. The foreign repository's history is gone and the manifest cannot restore it. The by-design rm -rf fallback assumes the graded content belongs to this worktree, and here it does not. The path is narrow: a worktree directory has to be replaced by another repository. On the fix: making remove_worktree run rm -rf only after the .git-file check passes also stops the prunable-but-gone case (path absent), which today is cleaned up by the fallback and prune. That case would then report failed and exit 1, which breaks a sibling path. | unsound | - |
| 2 | security | tools/branch-reconcile/branch_reconcile.py:641 | high | high | confirmed | When a worktree is prunable or git status fails (read_dirt returns None on rc!=0, for example dubious ownership), its dirt is None. read_newest_activity then reads only the HEAD commit time, and check_worktree returns None at `if st is None` (line 641). The ladder falls to the HEAD's ref verdict, and a stale merged HEAD reads MERGED with `remove worktree`. For a prunable worktree whose directory still exists but has lost its .git file, git worktree remove fails validation and rm -rf deletes the ungraded files. This contradicts spec-2 S5, which says content is graded first and only covered content lets the HEAD verdict decide. The path is narrow (a missing .git file, or status failing) but leads to data loss. The fix is sound: the bare primary has no HEAD and is kept by derive_action anyway, and a prunable worktree whose directory is gone still falls through and is pruned. | sound | - |
| 3 | security | tools/branch-reconcile/branch_reconcile.py:673 | high | high | confirmed | check_worktree (line 673) counts a probe as covered when each captured name passes `git grep -F -q -e <name>` over the whole default tree. The capture for it("works") is just `works`, and test_foo also matches inside test_foobar or in prose. A generic case name therefore covers a probe whose body is entirely new. Untracked content then lets the HEAD's deletable verdict decide, and --write deletes it. The deleted file has no git object and the manifest does not record it, so it cannot be recovered. The spec words the predicate loosely ('found by git grep -F'), but its intent is that the probe's case exists as a test there, and a name hit in unrelated text does not show that. Reaching it needs an idle worktree holding an untracked test file with a generic name. On the fix: matching the declaring form still collides when a different test on the default branch declares the same generic name with a different body, and it("works") is common in JS suites. 'Nothing beyond case bodies' never compares those bodies, so the fix does not cure the defect. | unsound | - |
| 4 | security | tools/branch-reconcile/branch_reconcile.py:546 | high | high | confirmed | derive_coverage (line 546) matches a candidate with the identical subject when sum(((a-b)+(b-a)).values()) <= 4. Take two unrelated one-line edits, {+x,-y} and {+p,-q}, under the same subject: their symmetric difference is exactly 4, so the branch commit reads `patch` and the branch reads SUPERSEDED and is deleted. Commits whose only change is a binary file or a file mode have zero +/- lines, and they match any same-subject commit with at most 4 lines. The spec does set an absolute bound, but its intent is a rebased copy, and here nothing is shared. Reaching this needs a same-subject commit on the default side since the merge base. On the fix: its example bound, drift <= min(4, common/2), breaks the spec's own AC1 arm. In selftest.py:262/266, two.txt shares 6 lines and drifts by 4, and 4 > 6/2 = 3, so that rebased copy would no longer match. The fix's other stated rule (common non-empty and larger than the drift) does pass both AC1 fixtures. | unsound | - |
| 5 | security | tools/branch-reconcile/branch_reconcile.py:562 | high | high | confirmed | derive_row_ids collects only the ids that head added lines and ignores removed lines. check_row_on_default (line 441) then asks only whether a row headed by that id exists under the memory root at the default tip. Take a commit that edits a row in place, `-\| TOOL-x-1 \| OPEN \|` / `+\| TOOL-x-1 \| DONE \|`. Its id already heads the OPEN row on the default branch, so the commit reads `rotated`, and a branch that is otherwise covered reads SUPERSEDED and is deleted. The selftest has only the byte-identical archive-move arm. The intent in the prompt is a row rotated into an archive, not an edited row. The fix is sound: an exact-line match is satisfied by a row moved byte-identically, and any mismatch errs toward keeping the branch. | sound | - |
| 6 | security | tools/branch-reconcile/branch_reconcile.py:805 | high | high | confirmed | resolve_default discards _observed (line 143), and derive_action (line 805) and write_deletions exclude only inv['branch']. With GOV_DEFAULT_BRANCH=develop and <remote>/HEAD -> main, main is not excluded. In a gitflow layout main is an ancestor of develop, so main reads MERGED: the local copy is `delete branch`, and <remote>/main is `delete remote branch (--remote)` and goes into the one push --delete. The resolve_remote docstring itself treats GOV_DEFAULT_BRANCH as possibly differing from the observed remote HEAD. The security model names any deletion of the default branch as the costly error. The path is narrow because it needs an override that disagrees with the remote HEAD. | sound | - |
| 7 | security | tools/branch-reconcile/branch_reconcile.py:979 | high | high | confirmed | write_deletions (branch_reconcile.py:979) runs `git push <remote> --delete <names>` with no lease. The verdict was graded from refs/remotes/<remote>/<n> as this clone last saw it, and the tool never fetches (README:14). The BY-DESIGN note covers the missing fetch, not deleting a sha that was never graded. In a multi-node repo, node B pushes to a branch whose stale tracking ref reads MERGED on node A. A run of `--write --remote` on A then deletes the server branch with B's new commits on it. The manifest records only the stale tracking sha, so it cannot restore them. Even with the skill's fetch, a fetch-to-push window remains. The path is narrow: it needs --remote, a stale or racing ref and a concurrent push, and B usually still holds the commits locally. It is still the costly error the security model names. Fix: the push lease cures the remote defect. The local half is unsound: `git update-ref -d` has none of `branch -D`'s refusal to delete a checked-out branch, and it leaves the branch.<n> config section behind. | unsound | - |
| 8 | security | tools/branch-reconcile/branch_reconcile.py:260 | medium | medium | confirmed | read_dirt (line 260) runs `git status --porcelain=v2 -z --untracked-files=all` without --ignored, and parse_status has no '!' branch. So check_worktree never sees gitignored files and grades the worktree 'content covered'. `git worktree remove --force --force`, and the rm -rf fallback, then delete those ignored files: a worktree-local .env, a local database, scratch output. Nothing in the evidence, the manifest, the spec or the README names this. The effect is contained to ignored, mostly regenerable state, hence medium. Fix: --ignored=matching reports a wholly ignored directory such as node_modules/ as one entry, so the read stays cheap. Grading UNKNOWN outside a disposable set, or naming the ignored files in the evidence, cures the silent loss. | sound | - |
| 9 | correctness | tools/branch-reconcile/branch_reconcile.py:641 | high | high | confirmed | read_worktrees sets w['dirt']=None for a prunable or bare worktree, a missing directory, or a failed `git status` (read_dirt returns None on rc!=0). check_worktree then returns None at `if st is None: return None` (line 641), past the freshness check, which reads only the HEAD commit time when dirt is None. The row is graded by its HEAD alone. A worktree at an old merged HEAD whose .git file is gone is listed prunable while its directory still exists. It reads MERGED, and derive_action gives it 'remove worktree'. In remove_worktree, git fails validation ('.git' does not exist) and the GNU rm -rf fallback runs with no content walk, so untracked files the tool never read are deleted. The BY-DESIGN premise ('only rows already graded deletable (content covered) reach it') fails: this content was never read. Spec S3 only says a prunable worktree's state is not read and the row says so. It does not say such a row may be deleted. The path is narrow: a prunable worktree whose directory still exists, or a status failure such as dubious ownership. | sound | - |
| 10 | correctness | tools/branch-reconcile/branch_reconcile.py:538 | high | high | confirmed | In derive_coverage, a commit in `<default>..<tip>` has parents that are either in that range ('unique') or reachable from the default (check_ancestor). So `all(p in unique or check_ancestor(inv, p) for p in parents)` always holds, and every merge counts as 'merge' with its own diff never read. check_equivalent runs before check_superseded and trusts `git cherry`, which skips merge commits. So a branch whose only non-merge commit was cherry-picked to the default reads EQUIVALENT, with 'all 1 commit(s) already applied', even when its merge commit adds content (an evil merge or a conflict resolution) that exists nowhere on the default. check_noop would catch it, but EQUIVALENT is decided before check_superseded is reached. The deletion is recoverable from the manifest sha until gc, but the false deletable verdict is the security model's costly error. The path is narrow: an evil merge whose sibling commits all landed by patch. | sound | - |
| 11 | correctness | tools/branch-reconcile/branch_reconcile.py:546 | high | high | confirmed | read_patch_lines drops the +++/--- headers, so the patch multiset carries no file names. The patch predicate accepts any same-subject commit on the default whose +/- multiset differs by <= DRIFT_LINES=4, an absolute bound. Any patch of at most two changed lines (one -/+ pair) therefore matches every same-subject commit on the default of the same size. That holds even when the two share no line and touch different files: {-a,+b} against {-p,+q} differs by exactly 4. The spec text matches the code literally (spec-2 line 39), but its stated intent (line 40, and the prompt) is 'a rebased copy that drifted by a line or two'. Two disjoint one-line patches are not that, so the commit counts as covered by 'patch' and the branch reads SUPERSEDED. The path is narrow: it needs an identical generic subject between the merge-base and the default tip, and every other unique commit covered as well. It is still a false deletable verdict. I checked the fix against arm_patch's fixture: one.txt shares 5 lines with a drift of 2, two.txt shares 6 with a drift of 4, and both satisfy either proposed bound with the same file set. The fix keeps that arm green and rejects the disjoint case. | sound | - |
| 12 | correctness | tools/branch-reconcile/branch_reconcile.py:979 | high | - | refuted | Duplicate of finding 7: the same defect (the lease-less `git push <remote> --delete` at branch_reconcile.py:979, which deletes a moved remote tip graded from a stale tracking ref), the same impact and the same fix. Finding 7 also already names the local `branch -D` analogue. The extra branch -D window adds nothing reachable: the tool reads the local refs and deletes them in one process, and checks again for a branch still checked out just before. Fix: the push lease is sound. The local half rests on a false premise: `git update-ref -d` does not keep the checked-out guard that `branch -D` has, and it leaves the branch.<n> config section behind. | unsound | - |
| 13 | correctness | tools/branch-reconcile/branch_reconcile.py:673 | high | high | confirmed | branch_reconcile.py:673 runs `git grep -F -q -e <name> <default_ref>` over the whole default tree, so the match is an unanchored substring in any file. A probe `def test_parse(` extracts `test_parse`, and any default file holding `test_parse_args` or prose naming it covers it. A JS it("...") or arm phrase is covered by the phrase appearing in any doc. The probe's other content is never compared. Covered content lets the worktree fall to its HEAD's ref verdict, so a MERGED HEAD reads `remove worktree` and --write deletes the probe. Spec 2 S5 does name `git grep -F`, but the owner's prompt asks that 'the probe's case exists as a test there', and no BY-DESIGN item covers the looser check. The path needs a name collision, a deletable HEAD and activity past the freshness bound, so it is narrow: high. Fix: the anchoring cures the collision. Its 'compare the probe's blob' alternative collapses into the existing blob clause and removes the case-landed coverage that AC7's probe fixture exercises. Its 'no other top-level content' alternative has no definition that a probe with imports or helpers could pass. A backslash-s class in `git grep -E` also depends on the regex library. | unsound | - |
| 14 | correctness | memory/builds/dSweptBranches/spec/2026-10-13-spec-TOOL-dSweptBranches-3.md:67 | low | low | confirmed | Spec 3 line 67 (section 4) and line 101 (AC1) still say `write_trace`. The module exposes `WRITE_TRACE`. Only the rev-2 revision log names `WRITE_TRACE` and records that each act is logged before it runs. The base spec had no code to disagree with, so the diff introduced the mismatch. It is documentation only and changes no behaviour. | sound | C17 |
| 15 | seams | tools/branch-reconcile/branch_reconcile.py:640 | blocker | high | confirmed | read_worktrees sets w['dirt'] = None for any prunable worktree, and read_dirt returns None on a non-zero `git status`. check_worktree (line 640) then returns None. read_newest_activity counts only the HEAD's commit time when dirt is None, so dirty-file mtimes cannot trigger IN-PROGRESS either. The HEAD's ref ladder decides the row, and a MERGED HEAD gives `remove worktree`, because derive_action never reads 'status not read'. remove_worktree's `git worktree remove --force --force` refuses a worktree whose .git is missing. The `rm -rf` fallback then deletes the directory with its ungraded content, matching the finder's reproduction. This breaks spec 2 S5, and the BY-DESIGN rm -rf item assumes the content was already graded. The trigger needs a directory that still exists but whose status cannot be read: a missing gitfile, a corrupt index or an ownership refusal. That is a narrow path with a data-loss consequence: high. | sound | - |
| 16 | seams | tools/branch-reconcile/branch_reconcile.py:812 | medium | - | refuted | Overriding a lock is the design the owner's prompt specified, not an oversight. Brief item 5 names `git worktree remove --force --force` as the removal, and spec 4 S1 and README:122 repeat it. A doubled --force is git's documented lock override. A deletable verdict also requires every content element to be covered. Spec 3's keeps (the default branch, the primary, a stash entry, a branch checked out in a kept worktree) do not include a lock. A medium finding whose premise contradicts the stated intent is refuted. Fix: keeping every locked worktree reverses the owner-specified removal and would never sweep a harness worktree its creator locked. That needs an owner decision, not a review fold. | unsound | - |
| 17 | seams | tools/branch-reconcile/branch_reconcile.py:374 | low | low | confirmed | Spec 2 section 4 says a repository with no memory tree skips the records, rotated and run-record predicates, announced. read_memory_root (line 374) silently falls back to `memory`, and nothing writes a skip for it, so no `skipped` line is emitted for that gap. The predicates still run against an absent tree and find no rows, which errs toward not-covered. The verdict effect is negligible. What remains is the report failing to announce a capability gap: low. | sound | - |
| 18 | verification | tools/branch-reconcile/selftest.py:606 | blocker | blocker | confirmed | arm_write runs `run_main('--root', repo, ...)` from the primary, which has main checked out. The primary therefore reads IN-PROGRESS (invoking), so its action is `keep` even without the `worktree/primary` clause. Local main is saved by kept_branches (the primary is not removed) and by write_deletions' `still` set, even with both name clauses removed. Remote main is filtered by the separate `names != inv['branch']` line, so AC3 still passes. Every AC2 and AC3 assertion survives removing the primary keep and the default-branch name keeps, while spec 3 AC2 says 'Red when ... the default branch is not excluded'. The exclusion code is present and correct today. The shipped check still certifies a protection it never exercises, on the costliest error class in the security model: blocker by the rubric. On the fix: the redundant `r['name'] == inv['branch']` guard in write_deletions cannot red alone while derive_action keeps the row, so 'red with each clause removed' holds through the row-text assertions only. The fix is otherwise sound. | sound | - |
| 19 | verification | tools/branch-reconcile/selftest.py:411 | high | high | confirmed | arm_content (selftest.py:385-427) seeds only a landed merge, a landed probe, an untracked file and two clean worktrees at --fresh-hours 0; no worktree holds a staged or unstaged tracked edit when content is graded. The only such edits are in arm_census's sibling, which runs under the default bound and reads IN-PROGRESS before check_worktree grades content. arm_write's worktrees are clean. So the `changed <p>` branch at branch_reconcile.py:662-667, the S5 clause spec 2 says AC7 observes, has no failing check, and a mutation there would let a worktree whose only unlanded work is an edited tracked file read MERGED and be removed. The code is correct today, but spec 2 says AC7 certifies a clause no check covers, and that will mislead the next change. | sound | - |
| 20 | verification | tools/branch-reconcile/selftest.py:601 | medium | medium | confirmed | seed_write_fixture (selftest.py:554-584) builds MERGED, EQUIVALENT, UNMERGED-LIVE, IN-PROGRESS and UNKNOWN rows only. The check at :601 asserts exactly that set, while spec 3 AC2 asks for a fixture holding one row of each verdict, with SUPERSEDED rows gone. No stash exists in the write fixture. So neither SUPERSEDED in DELETABLE (:49) nor the stash keep in derive_action (:803-804) is exercised under --write. Without the stash keep, a SUPERSEDED stash falls through to `delete remote branch (--remote)`, and write_deletions slices its name as a remote branch. The code is correct today. The effect is a contained test gap. | sound | - |
| 21 | verification | tools/branch-reconcile/selftest.py:228 | medium | medium | confirmed | In arm_census, the AC5 block (selftest.py:225-232) calls BR.read_inventory and BR.build_rows in-process outside seed_environ. selftest.main sets only the module-level ENV dict and never os.environ. BR.run_git and resolve_remote's read() spawn git with the inherited environment, and resolve_remote reads os.environ['GOV_REMOTE'] directly. An exported GOV_REMOTE naming anything but `upstream` therefore raises Refusal, the arm counts as `arm_census raised`, and the arm's remaining checks are lost. An exported GIT_DIR, as in a hook, redirects the inventory. This contradicts the module docstring's claim that the caller's environment is held out. arm_remover and arm_write wrap their in-process calls, so this block is the outlier. | sound | C9 |
| 22 | verification | tools/branch-reconcile/selftest.py:493 | medium | medium | confirmed | build_skeleton_remover (selftest.py:487-500) links to the nonexistent `/c/nonexistent/pnpm/target`. A walk that followed that link would find no file, so on POSIX AC2 stays green. That contradicts spec 4 AC2's `Red when: ... the walk follows a link`. When os.symlink fails, :530-532 prints `skipped` but the check at :526 has already counted as PASS with no link seen, so a skip reads as coverage. Nothing asserts that a link target outside the worktree survives removal. check_holds_file itself is correct (follow_symlinks=False plus the reparse-point skip), so the effect is a contained test gap. | sound | - |
| 23 | intent | tools/branch-reconcile/branch_reconcile.py:268 | blocker | blocker | confirmed | Reproduced on a throwaway fixture with the shipped CLI. Linked worktree X on a branch at main held worktree Y at X/.claude/worktrees/Y with an untracked precious.txt. The report graded Y `UNMERGED-LIVE · keep` and X `MERGED · remove worktree`, because read_dirt (:268) drops Y's directory from X's untracked set. `--write` printed `removed — worktree X · git worktree remove`, and precious.txt was gone. The recovery manifest records only HEAD shas, so the uncommitted file cannot be recovered. Neither derive_action nor build_rows nor write_deletions checks whether a removed worktree contains a kept one. A session working in a linked worktree that creates harness worktrees under its own .claude/worktrees reaches this path, and it deletes unlanded work. The proposed fix demotes the row only after the actions are assigned, so the `kept` set and the local-branch actions are already derived. X's branch would then read `delete branch` in the report while write mode keeps it as still checked out. The report would contradict what write mode does. | unsound | C10 |
| 24 | intent | tools/branch-reconcile/branch_reconcile.py:461 | high | high | confirmed | Reproduced. A branch whose one commit rewrites memory/TOOL.md's `\| TOOL-aSlug-1 \| fix x \| open \|` to `\| TOOL-aSlug-1 \| fixed by new diagnosis z \| RESOLVED \|` read `SUPERSEDED · delete branch · covered: rotated 1`. derive_row_ids (:451-465) keeps only the added line's leading id and ignores the removed line. check_row_on_default (:441-448) is satisfied by the old row with that id still on the default. Spec 2 S2's wording permits this, but the prompt's intent is a row rotated into an archive, and an edited row is content the default lacks. Write mode then deletes the branch, which is recoverable only from the manifest. The path is narrow: every unique commit must be a row-only edit under the memory root that no other predicate covers. | sound | - |
| 25 | intent | tools/branch-reconcile/branch_reconcile.py:546 | high | high | confirmed | derive_coverage (branch_reconcile.py:543-548) accepts any by_subject candidate from <mb>..<default> whose -U0 +/- line multisets differ by <= DRIFT_LINES (4), with no requirement that the patches share any line or file. Branch `fix: typo` (+unique work in b.txt) vs default `fix: typo` (+other in c.txt) differ by 2 lines, so it is covered as `patch`; binary or mode-only commits give empty Counters and match any same-subject commit of <=4 lines. Spec 2 S2 states the rule literally, but its own design text and the brief scope it to a rebased copy that drifted, and this case is not in the BY DESIGN list. Unlanded work reads SUPERSEDED and write mode deletes the branch. That needs a subject collision and a tiny patch, so the path is narrow. The recovery manifest keeps the sha recoverable until gc. | sound | - |
| 26 | intent | tools/branch-reconcile/branch_reconcile.py:641 | high | high | confirmed | read_dirt returns None when `git status` exits non-zero (line 261-262), and read_worktrees calls it for every readable, existing directory. check_worktree then returns None at line 641 and the HEAD ladder decides. build_rows only appends a `status not read` flag, and derive_action still yields `remove worktree` for a deletable verdict. That contradicts spec 2 S1.6 (UNKNOWN when a predicate the outcome depended on could not run) and README line 109. A corrupt index, a broken .git file or dubious ownership on a multi-user node gets an existing worktree with unexamined uncommitted content removed, with rm -rf as the fallback. That is unrecoverable loss on a narrow path. | sound | - |
| 27 | intent | tools/branch-reconcile/branch_reconcile.py:663 | high | high | confirmed | parse_status appends a submodule path to `changed` for any S... record but counts drift only for S C.. (pointer change), so S.M. or S..U (modified or untracked content inside the submodule) gives drift 0. In check_worktree the submodule directory fails is_file, so it is absent from `have`. read_default_tree keeps only blobs, so a gitlink is absent from `tree`, and `have.get(p) == tree.get(p)` is None == None, which grades it covered (`sub matches main`). The worktree then takes its HEAD's deletable verdict. git worktree remove refuses worktrees that contain submodules, so the rm -rf fallback deletes the uncommitted submodule work. That breaks spec 2 S5 and is data loss on a narrow path. | sound | - |
| 28 | intent | tools/branch-reconcile/selftest.py:600 | medium | medium | confirmed | seed_write_fixture (selftest.py:554) builds MERGED, EQUIVALENT, UNMERGED-LIVE, IN-PROGRESS (open-br) and UNKNOWN (orphan-br) rows only. The check labelled `the fixture holds one row of each verdict` asserts those five, contrary to spec 3 AC2 (`one row of each verdict`, SUPERSEDED named among the deleted). No other arm asserts the action on a SUPERSEDED row, since the patch, landing, records, rotated, noop and stash arms read verdicts only. A regression that drops SUPERSEDED from the acted-on set, or mishandles a covered dirty worktree, stays green. The effect is a test gap, with no shipped wrong result. | sound | - |
| 29 | intent | tools/branch-reconcile/branch_reconcile.py:925 | low | low | confirmed | write_manifest calls base.mkdir (line 925) outside the try that converts OSError to Refusal, and main catches only Refusal. An uncreatable directory raises a traceback with exit 1 instead of spec 3 S2's refusal with exit 2. Nothing is deleted, because the manifest is written before any removal. | sound | - |
| 30 | intent | tools/branch-reconcile/branch_reconcile.py:384 | low | low | confirmed | read_memory_root silently defaults to `memory` (line 374-386), and the only inv['skips'] writers are the merge-tree probe and the derive_verdict exception wrapper. A repository with no memory tree therefore gets no `skipped` line for records, rotated or the run-record IN-PROGRESS source, contrary to spec 2 section 4. The predicates simply never match, which is conservative, so the effect is a missing announcement only. | sound | - |
