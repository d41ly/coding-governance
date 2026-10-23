# TOOL-dGroundRules-26 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-26

No merge bar, gate leg or self-test suite ran in this pass. The naming lexicon ran (`lexicon.py
--check`, OK) and `--suggest build_source_snapshot --as py.function` answered OK. Each criterion was
observed before the commit by the case's own CLI on the worktree, or by a scratch probe that clones
the worktree `--shared` under the system temp directory, copies the built `check_policy.py` into the
clone uncommitted, plants the criterion's break there, and calls `run_fixture("adopter-fresh-target")`
in process with `remove_repo` wrapped so the target's receipt can be read before it is removed.

The case is red at this branch's HEAD for a reason this unit does not own: over a fresh target,
`arm_mirror_parity`, `arm_mirror_landed` and `arm_mirror_readers` each print one finding, eight
`WRONG` lines across the two `--check` runs. A clean clone of HEAD 4c1f59cc running HEAD's own case
printed the same eight lines (50 assertions, 8 wrong), and TOOL-dGroundRules-5's ledger hands them to
TOOL-dGroundRules-21 S5 and S15. Every observation below names which lines are those eight.

**Evidences:** TOOL-dGroundRules-26
- AC1 — `python check_policy.py --fixture adopter-fresh-target` — on the worktree, HEAD 4c1f59cc with
  this unit's edits uncommitted, it printed "adopter-fresh-target: installing from snapshot 719567f3
  of the working tree over HEAD 4c1f59cc", the source's `git rev-parse HEAD` being
  4c1f59ccd345374182bdf06598aff6eba8b5d8c2; `apply` then exited 0 and laid 11 receipt rows. The probe's run printed
  "installing from snapshot e2d1718f ... over HEAD 4c1f59cc", and the target's receipt read
  `gov_commit` e2d1718ffeecd633a9984937b927822c8269b4d6, the snapshot's HEAD, whose parent was
  4c1f59cc, with `gov_source` naming the snapshot's directory.
- AC2 — `adopt-policy.sh` — in the probe's clone, one byte of `adopt-policy.sh` changed (the first
  closing `fi` made `fx`) and left uncommitted: the case printed "WRONG: govkit.py apply --kits policy
  exited 1", carrying govkit's "adopt-policy.sh: line 96: syntax error: unexpected end of file", 10
  assertions, 1 wrong. With the break reverted it printed no `WRONG` naming the adopter: `apply`
  exited 0, and only the eight mirror-arm lines named above remained, 50 assertions, 8 wrong. The
  wholly green reverted run is the close's, once TOOL-dGroundRules-21 has settled those eight.
- AC3 — `does not resolve at` — in the probe's clone, a commit deleting `policy.py` (HEAD 9fc52a3c),
  the file then restored untracked: the case printed "installing from snapshot 5143353b ... over HEAD
  9fc52a3c", the output held `does not resolve at` zero times, `apply` exited 0, and the receipt's
  row `tools/policy/policy.py` named a file present in the target.
- AC4 — `git count-objects -v` — over the worktree carrying uncommitted edits to `check_policy.py`
  and this unit's spec, before the AC1 run: `count: 115`, `size: 679`; after it: `count: 115`,
  `size: 679`.

A failed step was probed too: `build_source_snapshot` over a directory that is no repository raised
"the snapshot's clone step exited 128: fatal: '<dir>' does not appear to be a git repository", and no
`pol-` directory remained under the system temp directory. Run with `GIT_DIR` and `GIT_INDEX_FILE`
exported to paths that do not exist, it still built a snapshot whose parent was 4c1f59cc.

The red-first observation of the `New arm:` line, and the `policy fixtures` leg itself, are left for
the close.
