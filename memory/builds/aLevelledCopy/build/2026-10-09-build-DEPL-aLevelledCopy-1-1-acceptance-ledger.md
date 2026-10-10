# DEPL-aLevelledCopy-1 — acceptance ledger

**Serves:** journal DEPL-aLevelledCopy-1

No merge bar and no self-test suite ran in this pass. The criteria were observed by running the one
new selftest function alone, `check_mode_carry`, under the default `%TEMP%`. It passed 26 of 26
assertions in 137 s on node a. Every arm was then observed RED by a scratch driver. The driver
handed `measure_mode_carry` a staged copy of `govkit.py` and fed the results through the suite's
own `check`, so each red is a named entry in `s.FAILURES`. The `govkit.py` read with `git show` at
base `ce9192c0` redded AC1, AC4 and AC7. The seven staged breaks redded their named arms: the S4
mode arm disabled (AC1), the rule mirrored both ways (AC2 and AC6), the `how == "table"` guard
dropped from the S3 carry line (AC3), the old mode expression restored in `land_through_index`
(AC4), `mode_to` dropped from the snapshot predicate (AC5), the memo removed from
`read_tree_modes` (AC7), and the S5 note turned into a failure (AC8). Each break's fixture stayed
live, and the unbroken function is green again. The hold-region scan, `check_hold_region`, passed
5 of 5 over the new refusal site. The close still owes the whole `govkit selftest` suite,
`govkit selfcheck`, the lexicon leg and memory hygiene.

**Evidences:** DEPL-aLevelledCopy-1
- AC1 — `mode-carry` — the read-only `update` printed one `mode-carry` line for the hook reading
  `100644 -> 100755`. After `--write`, `git ls-files -s` reported 100755 with the blob oid unchanged,
  and a second read-only `update` printed no `mode-carry` line. Base `ce9192c0` left the hook 100644
  and printed no line, and disabling the S4 arm redded the write half.
- AC2 — `--write` — the adopter's 100755 row got no `mode-carry` line, and `--write` landed
  `own v2` at 100755 according to `git ls-files -s`. The mirrored rule landed it at 100644 and redded
  both halves.
- AC3 — `seed` — a `seed` row gov made 100755 got no `mode-carry` line, and `--write` left it 100644.
  Dropping the table guard printed a `mode-carry` line for it and redded the arm.
- AC4 — `stale` — the read-only run printed the `stale` line and the `mode-carry` line for
  `both.sh`, and one `--write` left `both v2` at 100755. The old mode expression in
  `land_through_index` left it 100644.
- AC5 — `git ls-files -s` — the kit's check went `landed-but-inert` after a mode-only carry, the run
  printed ROLLED BACK, and `git ls-files -s` reported 100644 again. Without `mode_to` in the
  snapshot predicate the hook stayed 100755.
- AC6 — `resolve_landed_mode` — `check_mode_carry` called it over the five S1 rows plus three more,
  and all eight returned the table's result. The mirrored copy changed the adopter's 100755 and the
  symlink, and both of those calls redded.
- AC7 — `ls-tree -r` — under `GIT_TRACE` written to a file, a read-only `update` over five engine
  rows showed one `ls-tree -r -z` at the target commit and no per-path `ls-tree`. With the memo
  removed, the trace showed one `ls-tree -r` per row.
- AC8 — `govkit check` — after the hook went back to 100644 with `update-index --chmod=-x`,
  `govkit check` printed the note naming the path, 100644, 100755 and the remedy, and it exited 0
  before the edit and 0 after. Turning the note into a failure made it exit 1, and the arm redded.
- AC9 — `s.FAILURES` — every staged break named above put its arm's label in `s.FAILURES`, on a
  fixture whose liveness checks passed. This is the build-time observation rev-2 describes.
