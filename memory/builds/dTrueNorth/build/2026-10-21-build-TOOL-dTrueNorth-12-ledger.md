# TOOL-dTrueNorth-12 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-12

No merge bar, no self-test suite and no gate leg ran in this pass but the naming lexicon
(`lexicon.py --check`, OK, after one rename it asked for). Every criterion below was observed by a
probe of the changed code on `0bf5e896b`'s working tree: the module's own CLI over its fixture, in
two scratch repositories under the user temp directory, short-named; and two scratch scripts loading
`tools/memory-tree/deviation_join.py` by path. The red half of AC1, AC3 and AC7 was observed by the
same calls with `HEAD`'s module put back in the scratch tree. The probes stand in for the
`routed-commits selftest` leg; that leg, `routed commits name a specced unit`, `govkit selfcheck`,
the run-gates canaries, `measure-legs selftest`, `install-prefix (shipped surface)`, `lexicon naming
predicates`, `memory hygiene` and `spec tokens (a spec's own names resolve)`, and the `New arm:`
line's RED-first observation, are owed to the close.

S2's search for a further held plant: every plant was built singly under the kit's strip and under
the identity strip, and only `gen` and `status-gen` changed verdict, both already in `STRIP_PLANTS`,
so none was added.

**Evidences:** TOOL-dTrueNorth-12
- AC1 — `deviation: SKIP` — in a scratch git repository holding `tools/lib/` and `tools/memory-tree/`
  alone, `--fixture --plant status-only --policy refuse` printed the one SKIP line, its reason the
  resolver's three places looked and its tail `· status-only header-rev gen status-gen gen-text`, and
  exited 0; `--fixture --plant pass-revision --policy refuse` printed the SKIP line and exited 1;
  `--fixture --plant record-late --host routed-commits` printed the SKIP line, then the host's
  `deviation: RANGE` line with `1 recorded late` and FIX-dTrueNorth-28's revision `recorded after its
  departure`, no `REFUSED` line, exit 0. `HEAD`'s module there exited 2 on both fixture calls.
- AC2 — `read_gen_region_awk()` — on the tree it returned a string equal to the `sed -n` line's
  output (`equal to sed: True`); with a `resolve` stub raising `LookupError('stub: nothing here')` it
  raised `LookupError` reading `the unattended kit's lib-unattended.sh, which holds GEN_REGION_AWK,
  does not resolve: stub: nothing here`. The module holds no copy of the awk.
- AC3 — `.memory-tree.conf` — in a clone of `e5fa131d3` with every `DESIGN_*` key blanked and the
  `DESIGN_RECORD` file deleted, the 36 plants of `PLANTS` each exited as `PLANT_EXITS` states, 0
  mismatches, `unmeasured` exit 2; `below-risk` and `owner-cause` exited 1 under `--approval by-risk`.
  `HEAD`'s module in that clone exited 2, `nothing measured — the fixture copies this tree's
  DESIGN_RECORD [chain] and DESIGN_VIEW`.
- AC4 — `{prefix}` — the AC's `json.load` line printed
  `[['{prefix}/lib/', '{prefix}/memory-tree/', '{prefix}/unattended/lib-unattended.sh']]`.
- AC5 — `requires_if` — `grep -n 'kit = "unattended"'` printed line 8 once, its row
  `{ kit = "unattended", when_any_key_set = ["DESIGN_RECORD", "DESIGN_BASELINE", "DESIGN_VIEW"]`;
  `tomllib` read one such row with those three keys.
- AC6 — `measure_fixture` — over `build_fixture` of the base and each plant of `PLANTS` but
  `unmeasured` the probe read member counts whose increments sum, with `BASE_MEMBERS` 6, to N = 29;
  `--fixture` in the AC3 clone exited 0 printing `members 29` and `1 recorded late`, its one
  `recorded after its departure` line FIX-dTrueNorth-28's, the `record-late` plant's unit.
  `check_composed_run` over those counts held, and with `owner-er` put on `owner-bare`'s clause it
  redded at 28 members.
- AC7 — `nothing measured` — in AC1's repository with one commit holding a `.memory-tree.conf` that
  declares `DESIGN_RECORD`, `DESIGN_BASELINE` and a `DESIGN_VIEW` naming no file, `--policy report`
  exited 2, `deviation: nothing measured — the generated-region strip cannot be read, ...: the
  unattended kit's lib-unattended.sh, which holds GEN_REGION_AWK, does not resolve: ...`, naming no
  view; `HEAD`'s module there exited 2 naming `DESIGN_VIEW`.

The `New arm:` lines of this unit on the Python selftests were observed at the close, in a scratch clone of `e583a7f42` with the breaks of `2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md` staged one set at a time: under the `routed_commits.py` selftest, which runs `deviation_join.py`'s plant arms, break `u12-stub-ignored`, 1 of its 2 arm lines red. Each staged break was restored with a checkout, and at `92a0dcb96` every one of those selftests printed all arms held. Its lines on the shell suites the flagged bar runs are owed with that bar, which the owner deferred past this landing.
