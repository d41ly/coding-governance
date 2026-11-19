# TOOL-dLandedOwners-4 — acceptance ledger

**Serves:** journal TOOL-dLandedOwners-4

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command, or by a `python -c` probe calling the unit's functions, from the worktree root, with the landed
revision L at `81657e77` (the remote-tracking `origin/main` at this pass). Every red was observed either
at the pass's base `01ba0a95`, on a scratch copy of that revision's `check_policy.py` under the
session's scratchpad imported ahead of the kit's, or as a staged break: one edit to a scratch copy of
this pass's `check_policy.py` imported ahead of the kit's, a scratch copy of `kit.toml` the probe set as
the module's `KIT`, or, for AC3 alone, an edit to the tracked `tools/policy/kit.toml` the install
snapshot copies, restored by `git checkout` before the next command. The fixture repositories were
made by each case's own `tempfile.mkdtemp(prefix="pol-")` under `%TEMP%` and removed by `remove_repo`;
the real repository's refs were never written.

**Evidences:** TOOL-dLandedOwners-4
- AC1 — the spec's `ROOTS` probe printed `['dDeclaredLoop', 'dSafePassage']`, then
  `2 ['tools/policy']` (PINNED, this pass). Red: on the base's copy it printed the same builds, then
  `8` (PINNED, this pass) and a set holding the policy kit's absolute path beside `tools/policy`.
- AC2 — `run_reader_carried('reader-coverage-carried')` printed `case kit-root-threaded: red`,
  `graded 1` (PINNED, this pass) and the finding for `fixture.planted`, and the `kit-modules-absent`
  line's Refusal named `<%TEMP%>/pol-<x>/r/tools/memory-tree holds no gen_build_index.py`,
  the kit copy's memory-tree directory, with no `WRONG:` on any line; it returned `(10, 0)` (PINNED, this pass).
  Red: with `derive_run_kind` loading its own modules as at the base, `case kit-root-threaded: refused`
  printed `WRONG:` and `.../tools/policy is not the kit copy's root`, naming the policy kit's own path.
- AC5 — the same call printed `case landing-other-base: green`, `graded 0` (PINNED, this pass) and the
  announce line, no `WRONG:`. Red: with `bases[b] &` deleted, `case landing-other-base: red` printed
  `WRONG: graded 1` (PINNED, this pass).
- AC6 — the same call printed `case rotated-landed: red`, `graded 1` (PINNED, this pass) and
  `fixture.planted (owner bPlanted, landed at`, no `WRONG:`. Red: with `RUN_RECORD` narrowed to
  `^RUN\.md$`, `case rotated-landed: green` printed `WRONG: graded 0` (PINNED, this pass).
- AC7 — the same call printed `case disposed-ask-landed: red` and `case roster-specced-landed: red`,
  each `graded 1` (PINNED, this pass), no `WRONG:`. Red: with `disposed.add(row.target)` replaced by
  `pass`, `case disposed-ask-landed: green` printed `WRONG: graded 0` (PINNED, this pass); with the
  last line of `derive_run_kind` returning `"spec"`, `case roster-specced-landed: green` printed
  `WRONG: graded 0` (PINNED, this pass).
- AC3 — `run_legacy_withheld_install('legacy-homes-withheld-install')` printed a `plan` and an
  `apply` line for each of `legacy-homes.txt` and `unscanned-readers.txt`, no `WRONG:`, and returned
  `(6, 0)` (PINNED, this pass), in about 19 seconds (PINNED, this pass), so the spec's UNVERIFIED cost
  of minutes did not hold here. Red: with a `[[files]]` rule including `unscanned-readers.txt` with
  `role = "engine"` staged after the `project-owned` rule, the `plan` line for it printed
  `WRONG: exit 0 · COVER [project-owned] tools/policy/unscanned-readers.txt; write [engine] tools/policy/unscanned-readers.txt`
  and the `apply` line `WRONG: ['tools/policy/unscanned-readers.txt']`, `(6, 2)` (PINNED, this pass).
  On the base's copy the case's lines named `legacy-homes.txt` alone, `(3, 0)` (PINNED, this pass).
- AC4 — `run_legacy_present('legacy-homes-present')` printed a descriptor line naming
  `unscanned-readers.txt`, `withheld from installs`, no `WRONG:`, `(3, 0)` (PINNED, this pass). Red: with
  the module's `KIT` set to a scratch copy whose `project-owned` include drops `unscanned-readers.txt`,
  that line printed `WRONG: no such rule`, `(3, 1)` (PINNED, this pass); the base's copy over the same
  scratch kit stayed green, `(2, 0)` (PINNED, this pass).
- AC8 — the spec's `FAIL` probe with `--literal-pathspecs`, `--show-prefix` and `ls-files` each printed
  a list of one finding holding `git`, that argument and `failed, so reader coverage cannot read the tree`.
  Red: on the base's copy the first printed one `which is not a tracked file` finding for
  `deviation.approval`, the second `[]`, and the third `64` (PINNED, this pass) `has no reader` findings.
- AC9 — `grep -n "runs of whitespace" help/policy.md` printed line `170` (PINNED, this pass), the
  "A declared key" bullet, and `grep -n "runs of spaces" help/policy.md` printed nothing. Red: at the
  base the second grep printed line `170` (PINNED, this pass).
- AC10 — the spec's probe printed `['legacy-homes.txt', 'unscanned-readers.txt']`; the
  `'"legacy-homes.txt"'` grep over the spec's files printed nothing, and `grep -c derive_withheld_names`
  counted `1` (PINNED, this pass) in each. `stale_edges.IGNORE` drops `legacy-homes.txt` and
  `unscanned-readers.txt` and keeps `core-pending.txt`, and `shims` and `retired_edits` import. Red: at
  the base `tools/govkit/govkit.py` held no `derive_withheld_names`, and each ignore list spelled the name.
- AC11 — the spec's probe printed `False True`, and `git grep -n "terminal at the landed revision" -- tools/ help/ README.md`
  printed nothing. Red: on the base's copy the probe printed `True False`.
- AC12 — the spec's greps found the `reader-coverage-carried` paragraph naming each sub-case
  `tools/policy/check_policy.py#RC_CARRIED` added, the `legacy-homes-withheld-install`
  text's `every withheld file`, the arm paragraph's `git read of reader coverage`, and
  `help/policy.md`'s sentence on a failed git read. Red: at the base each phrase counted `0` (PINNED, this pass).
- AC13 — `gotchas.py --for-paths tools/policy/check_policy.py` named
  `kit-argument-dropped-at-an-inner-call`, and the grep found the claim in
  `memory/map/features/policy.md` and `memory/map/generated/MAP.md`. Red: at the base the record is
  absent, so neither names the class.

Owed to the close (M8): each `New arm:` of the spec's section 7 observed RED on its staged break and
GREEN restored through `check_policy.py --fixture <case>`, recorded here under a `Pass: none` commit;
the case `adopter-fresh-target`, whose stray check now reads `derive_withheld_names` and which this
pass did not run; the govkit fixtures `stale_edges.py` and `retired_edits.py` and the shims case, whose
ignore lists now derive the names; and the legs of the spec's section 7.
