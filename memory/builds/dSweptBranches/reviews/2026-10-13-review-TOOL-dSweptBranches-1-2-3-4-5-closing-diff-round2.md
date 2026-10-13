**Serves:** diff-review TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5

# Tier-2 closing diff review: dSweptBranches, ROUND 2

*This round re-reviews only the fold in `f0e00195e`, which fixed round 1's two blockers. B1 adds the
containment keep in `build_rows`. B2 makes each keep the deciding keep in `arm_keeps`, and the
action reasons move from ` · ` to parentheses. Round 1's HIGH, MEDIUM and LOW items were carried to
the exit and promoted to their own units, so they are not re-reported here. The fan ran through
`tier2-review.js` at light intensity: three finder lenses, then five skeptic batches told to
REFUTE, then this synthesis. The author of this report re-read the load-bearing lines in the tree:
derive_action's keeps (`branch_reconcile.py:800-811`), the containment pass (`:1020-1028`), the
README sentence (`README.md:108-111`) and the new arm checks (`selftest.py:684-700`).*

**Reviewed range:** 0ac2418c05fad32467e20a93f04b8546383a1c4d...f0e00195e8b4745a2165baadd4444cb32b735591. **ROUND:** 2.

## Verdict: CLEAN WITH FIXES

No blocker and no HIGH finding survived. The fold closes B1 and B2. A deletable worktree that holds
a kept worktree now reads `keep (contains kept worktree …)`, and `--write` spares both. The
primary-worktree and default-branch keeps each red a row-text check when removed, and the skeptic on
refuted id 5 confirmed this. Four findings survived: two MEDIUM and two LOW, counted as 3 items
or 4 raw findings. Both MEDIUMs describe one hole. The fold added a separator check, but its
population has no stash row, so the stash keep's new spelling is unguarded. The LOWs are a README
sentence that overclaims and a containment reason that names its worktree by a different string
than the row does. This is a light run, so it is not a full review.

## Review shape

Intensity light: raw 5, confirmed 4, refuted 1, unverified 0 (0 uncertain), precision 0.80.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |

Adjudicated tally: by item, 0 BLOCKER, 0 HIGH, 1 MEDIUM, 2 LOW, so 3 items. By raw confirmed finding,
0 blocker, 0 high, 2 medium, 2 low, so 4 findings. The MEDIUM item merges ids 1 and 4, which share
one grade and one defect.

**Run integrity.**
- Lenses: 3/3 returned and 0 DIED.
- Skeptic batches: 5/5 returned and 0 DIED.
- Verdicts: 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded and there were 0 duplicates.
- Fixes on confirmed findings: 4 judged sound, 0 judged UNSOUND, 0 with no fix proposed and 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic and 0 RE-GRADED.
- Unverified findings: 0 answered UNCERTAIN and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

**Intensity: light.** The security and intent lenses were NOT run. Their classes were swept only
through the checklist shares, so this is not a full review. Three spec documents were supplied as
`specs`, beside the range's commit messages. The checklist had 4 items, each assigned to exactly one
of the 3 lenses: correctness 2, seams 1, verification 1. By design: the caller's byDesign.

**Hunted, nothing survived.** Each target below came from the brief. A light run is not evidence of
absence.
- The fold not closing B1 or B2.
- Containment computed on unnormalized paths.
- A kept-branch set derived before demotion. `kept` is built after the containment pass at `:1027`.
- An arm that passes for the wrong reason. Refuted id 5 is the only candidate, and it re-raises a gap round 1 already accepted.

The old `keep · ` spelling has one reader the fold left behind, and that reader is in the population
gap that ids 1 and 4 describe, not in the README, spec or skill.

## BLOCKER

None.

## HIGH

None.

## MEDIUM

### M1 (ids 1, 4): the separator check's population holds no stash row — `tools/branch-reconcile/selftest.py:695`

The fold added the check "no action carries the row separator, so the report parses". It runs
`BR.build_rows` over arm_keeps' fixture only. That fixture never runs `git stash`, so the check
never sees derive_action's stash keep (`branch_reconcile.py:804`), which this fold reworded. No
other arm pins that spelling: arm_stash and arm_census read verdicts and keys only, and no
`never deleted` appears in `selftest.py`. Revert the reason to `keep · a stash entry is never
deleted` and the suite stays green. `read_rows` takes `f[:7]` plus a re-joined tail, so field 6
reads a bare `keep` and the reason moves into the evidence column, while the skill's parse splits
the row into nine fields. This is the empty-population pattern that the charter's [gate] rule names.
The check's name and spec S1 ("Observed by AC2 and AC5") both claim every action. The shipped code
is correct today, so the effect is contained, and the binding grade is medium. Id 1 (correctness)
and id 4 (verification) found this independently. Id 4 adds that the fixture also has no delete or
remove row.

- **Fix (judged SOUND by the skeptic, both ids):** make the population independent of the fixture.
  Call `BR.derive_action` on one synthetic row of each kind: stash, local default, remote default,
  `worktree/primary`, and a deletable local row whose branch is in the kept set. Assert that no
  result contains ` · `. As an alternative, push one stash entry in arm_keeps' primary before
  `build_rows` runs, and assert that a stash row is present so the population cannot be empty. The
  smallest pin also works: assert in arm_stash that the stash row's field 6 equals `keep (a stash
  entry is never deleted)`.
- **Left-shift gate:** give every population check in `selftest.py` a non-empty-population
  assertion keyed to the kinds it claims, so it reds when one of those kinds is absent. If no gate
  fits, enter it in the project's bug-class checklist under C3, "fixture passes by finding
  nothing".

## LOW

### L1 (id 2): "Each keep reads `keep (<why>)`" is false for non-deletable rows — `tools/branch-reconcile/README.md:110`

The fold added the README sentence. `derive_action` still returns a bare `keep` for every verdict
outside DELETABLE (`branch_reconcile.py:810-811`), so the sentence is false for UNMERGED-LIVE,
UNKNOWN and IN-PROGRESS rows. The skill surfaces those rows first. Spec S1 made the same claim at
the base as `keep · <why>`, so the spec half is pre-existing and only respelled. Nothing parses the
column today: `selftest.py:686-692` matches only the parenthesized keeps, and `SKILL.template.md`
never mentions `keep`. The effect is on the documentation only, so the grade is low.

- **Fix (judged SOUND by the skeptic):** do one of these. Give the non-deletable keep a reason, such
  as `keep (verdict <V>)`. Or reword the README and S1 to say that a keep forced over a deletable
  verdict reads `keep (<why>)` and every other row reads a bare `keep`.
- **Left-shift gate:** add a selftest check that asserts the documented action grammar over every
  action `derive_action` can return, using the synthetic-row population from M1. A README claim
  about a column's shape then reds when the code disagrees.

### L2 (id 3): the containment reason names the kept worktree by its raw path, not its row name — `tools/branch-reconcile/branch_reconcile.py:1026`

The fold introduced this. The containment pass writes `inner[0].replace(chr(92), '/')` into the
reason. That string is the raw git worktree path. `build_rows` names each row
`os.path.relpath(path, primary)` when `check_under(path, primary)` holds (`:993-995`). B1 targets
a harness worktree under the primary's `.claude/worktrees/` that holds a nested worktree of its
own. In that layout the container reads `keep (contains kept worktree C:/…/.claude/worktrees/A/.claude/worktrees/B)`,
while B's row is named `.claude/worktrees/A/.claude/worktrees/B`. An owner or the skill cannot join
the two by string. Round 1's prescribed fix said `<name>`. AC5 says only
`keep (contains kept worktree …)`, and the selftest checks only the prefix (`selftest.py:686`).
Keep and delete behaviour do not change, so the grade is low.

- **Fix (judged SOUND by the skeptic):** build a path-to-row-name map from `wt_rows` and put the
  kept row's `r['name']` in the reason, as
  `f"keep (contains kept worktree {name_of[inner[0]]})"`. Then assert in arm_keeps that the named
  worktree is a key in the parsed rows.
- **Left-shift gate:** the arm_keeps assertion above is the gate. Generalize it so that any action
  reason naming a row must name an existing row key.

## Refuted

- **id 5 (verification, `selftest.py:702`, finder grade low).** The claim was that write_deletions'
  name guards are never the deciding guard. The skeptic found that those guards (`:966` local,
  `:975` remote push filter) are unchanged from the base and that round 1 recorded the limitation
  explicitly. B2's fix was judged SOUND on the understanding that the redundant write-path guard
  cannot red alone while derive_action keeps the row. With derive_action's default-branch clause
  removed, the `local main` and `upstream/main` row-text checks red, which meets AC5's red
  condition. The wider "every keep is the deciding keep" mutation table is round 1's left-shift
  gate, carried to the exit.

review-shape kind=diff-review round=2 intensity=light at=synth raw=5 confirmed=4 refuted=1 unverified=0 blocker=0 high=0 medium=2 low=2 agents=9 out-tokens=75609

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/branch-reconcile/selftest.py:695 | medium | medium | confirmed | arm_keeps (selftest.py:663-703) pushes no stash, so BR.build_rows(inv) at :695 yields no stash row and the separator check never sees derive_action's stash spelling (branch_reconcile.py:804), which this fold changed. The other keeps are in its population: primary, default local/remote, containment (outer), and 'checked out in a kept worktree' (x-br/y-br). No other arm reads a stash row's action. arm_stash and arm_census check only verdicts and keys. read_rows (:125-132) takes f[:7] plus a re-joined tail, so a reverted 'keep · a stash entry is never deleted' would still parse: field 6 would read 'keep' and the reason would move into evidence, and nothing would go red. This is a coverage hole in a check whose name and spec S1 ('no action carries the row separator ... Observed by AC2 and AC5') claim every action. Production code is correct today, so the effect is contained: medium. | sound | C4 |
| 2 | correctness | tools/branch-reconcile/README.md:110 | low | low | confirmed | The README sentence 'Each keep reads `keep (<why>)` in the action column' is new in this fold (README hunk +3 lines, absent at 0ac2418c). derive_action at branch_reconcile.py:810-811 still returns a bare 'keep' for every verdict outside DELETABLE, so the sentence is false for UNMERGED-LIVE, UNKNOWN and IN-PROGRESS rows. S1 claimed the same at the base as 'keep · <why>', so the spec half is pre-existing and only respelled. The README half was introduced here. No reader parses the column: selftest.py:686-692 matches only the parenthesized keeps, and SKILL.template.md never mentions 'keep'. The impact is documentation only. | sound | C4 |
| 3 | seams | tools/branch-reconcile/branch_reconcile.py:1026 | low | low | confirmed | Introduced by this fold. build_rows (branch_reconcile.py:1026) puts the raw git worktree path into the reason, with backslashes swapped for slashes: inner[0].replace(chr(92),'/'). The same function names each row os.path.relpath(path, primary) when check_under(path, primary) holds (lines 993-995). So for the B1 layout, a nested worktree under the primary, the container's reason shows an absolute path while the kept row shows a relative name, and the two do not match as strings. Round 1's prescribed fix said '<name>'. The spec's AC5 only says 'keep (contains kept worktree …)', and the selftest checks only the prefix (selftest.py:686), so nothing gates the mismatch. Nothing parses the reason: README:111 documents only 'keep (<why>)'. Keep and delete decisions do not change, and a human can still see which worktree is meant. That makes it cosmetic, so the grade is low. | sound | - |
| 4 | verification | tools/branch-reconcile/selftest.py:695 | medium | medium | confirmed | The separator check at selftest.py:694-696 was added by this fold and runs BR.build_rows over arm_keeps' fixture only. That fixture (seed_repo plus worktrees and branches) never runs `git stash`, and inv['stash'] comes from `git stash list` in that fresh repo, so the population has no stash row. derive_action's stash keep (branch_reconcile.py:804) was reworded in the same fold, and no other check pins its spelling: grep finds no 'never deleted' in selftest.py, and arm_stash checks verdicts only, through read_verdict. If that one string went back to ' · ', the check that claims the whole class would stay green, which is the empty-population pattern the charter's [gate] rule names. This is distinct from M1. The effect is contained: the shipped code is correct today, and the gap only lets one future regression through. | sound | C3 |
| 5 | verification | tools/branch-reconcile/selftest.py:702 | low | - | refuted | Not a defect the fold introduced. write_deletions' name guards (:966 local, :975 remote push filter) are unchanged from base 0ac2418c0, and they were never the deciding guard there either. Round 1 recorded this limitation explicitly. B2's fix was judged SOUND with the note that write_deletions' redundant name guard cannot red alone while derive_action keeps the row, so that mutation reds through the row-text assertions only. The fold implements exactly that. With derive_action's default-branch clause removed, the 'local main reads keep (the default branch)' and 'upstream/main reads keep (the default branch)' row checks red. That matches AC5's red condition: 'both default-branch guards are removed'. The commit claims each keep 'decides a row', and that is true of the derive_action keeps. The commit does not claim the write-path guards were seen red. The broader 'every keep is the deciding keep' mutation table is round 1's left-shift gate, carried to the exit. The finder graded this low, and it re-raises a known, accepted gap. | sound | C3 |
