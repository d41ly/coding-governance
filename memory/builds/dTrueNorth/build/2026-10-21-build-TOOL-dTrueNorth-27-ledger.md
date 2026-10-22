# TOOL-dTrueNorth-27 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-27

No merge bar, no self-test suite and no gate leg ran in this pass: the role's hook refused
`sh_hygiene.py` and the spec-token checker as legs, so every leg command an AC names is owed to the
close, where the plain bar grades the nine legs `2026-10-22-build-TOOL-dTrueNorth-27-bar1.log`
printed red. The naming lexicon answered the three functions the pass mints
(`--suggest <name> --as py.function`, OK for each). Each line below is a probe of the changed code over `f221e1135`, with its
red side observed over HEAD's file where one is named. Fixture repositories sat under short `%TEMP%`
paths with no hook installed. The `New arm:` lines' RED-first observations are owed to the close.

**Evidences:** TOOL-dTrueNorth-27
- AC1 — `grep -c 'TOOL-dTrueNorth-' memory/guides/SESSION-KICKOFF.md` — printed 4, the four
  section B bullets of 324, 262, 193 and 251 bytes, each under the 400-byte cap; `last-body-change`
  and `last-audit` both name `f221e1135`, the HEAD this pass was built on, re-stamped in the commit
  that edits the two watched files. The `manifest-check.sh` and `--only manifest-check` runs are owed.
- AC2 — `tools/memory-tree/check-memory-hygiene.sh` — checks 29 and 30 print their lines by
  parameter expansion; the file's raw `<<<` count fell 25 to 23, the two printing loops, and
  `git diff --stat origin/main -- memory/project/substitution-fed-loops.txt` printed nothing. The
  registry leg is owed.
- AC3 — `git diff --stat origin/main -- memory/project/spawn-idiom-sites.txt` — printed nothing; each
  site of section 4's table reads its no-fork form in the diff. The `--spawn-idioms` leg is owed.
- AC4 — `memory/project/fork-ceilings.txt` — unchanged against `origin/main`; over a scratch fixture
  (`probe_c9.sh`, the hygiene suite's check-29 fixture rebuilt from this kit) the full run printed
  checks 29 and 30 from check 9's one generator process, with no verdict marker line left in check
  9's own block. The `fork-count.sh --only memory-hygiene` count is owed.
- AC5 — `python tools/memory-tree/gen_build_index.py --check --with-verdicts` — in the tree it
  printed `build-index: verdict 29 exit 0`, `build-index: verdict 30 exit 0` and
  `build-index: verdicts end` above `--check`'s lines, and each section split as check 29 and 30
  split it equalled its standalone verb byte for byte. Over the scratch fixture the full run's check 29 and 30 lines
  and FAILED blocks equalled the `--only 29` and `--only 30` runs red (a planted uncarried clause, a
  gap record) and green; a planted traceback gave both checks their unreadable branch.
- AC6 — `tools/check-spec-tokens.py` — by `grep` over it, its suite,
  `tools/memory-tree/deviation_join.py`, `tools/memory-tree/gen_build_index.py` and
  `tools/memory-tree/tree_lib.py`, none of the thirteen spellings stands: no `HERE / "memory-tree"`,
  no `$HERE/memory-tree/design_lib.py`, no `tools/fix-` in the deviation fixture, no
  `"tools", "workflows"` join in the generator selftest, and `<prefix>/check-playbook-parity.sh:334`
  in `tree_lib.py`. The `bash tools/check-install-prefix.sh --list` run is owed to the close.
- AC7 — `tools/lib/resolve_kit_dir.py` — `diff` of its block against the checker's between
  `# >>> resolve_kit_dir` and `# <<< resolve_kit_dir` printed nothing; from a scratch repository's
  `tools/` the resolver raised `LookupError` naming the receipt, `tools/memory-tree` and
  `memory-tree`, the text the checker's `REFUSING` line carries. The copied checker's own run, and
  `--legs-for`, were refused as the spec-token leg and are owed.
- AC8 — `src/` — the deviation fixture, routing `src/` through `FIXTURE_ROUTED`, ran as
  `deviation_join.py --fixture` exit 0 with every base member joined, and `asbuilt_view.py --fixture`
  rendered its dated view with `findings 0`, exit 0. Both selftests,
  `python tools/memory-tree/deviation_join.py --selftest` and
  `python tools/memory-tree/gen_build_index.py --selftest`, are owed to the close.
- AC9 — `tools/unattended/unattended.sh` — a probe reading the driver and its suite found branch 23's
  message free of command substitution and its arm the whole printed message, signature run
  included, and branch 24's prefix arm running to `or the word external`; over HEAD's two files the
  23 message held `$(readme_of …)`, its arm stopped short and the 24 arm did not reach the run. The
  `check-arms.py --check` and `--report` reads are owed.
- AC10 — `grep -c 'TOOL-dTrueNorth-28' memory/DECISIONS.md` — printed 1; `REFUSAL_CEILINGS` reads
  `tools/unattended/unattended.sh:323:2026-10-22:TOOL-dTrueNorth-28`. The ceiling line is owed.
- AC11 — `git grep -c 'PLAY-dClosedLoop-1' -- tools/memory-tree/asbuilt_view.py tools/memory-tree/gen_build_index.py`
  — printed nothing, and `--write` moved `memory/LIVE.md`'s Landed-unclosed count for dClosedLoop
  from 1 to 0. The `drift_report.py --check` run is owed.
- AC12 — `asbuilt_view.derive_head_names` — the argument `"memory/design/view.md"` raised
  `DesignRefusal` opening `DESIGN_VIEW memory/design/view.md is not named`; the live `DESIGN_VIEW`
  gave `PLAY-dClosedLoop-1` and `build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py`, and
  `gen_build_index.py --write` re-rendered the live view with no byte moved.
- AC13 — `grep -n -B2 '"cutoff_keys_armed": 36' tools/drift-audit/drift_signals.py` — showed the
  `34 -> 36` reason naming `TOOL-dTrueNorth-28`, `SPEC_CARRIES_CUTOFF` and `SPEC_AUDIT_PIN_CUTOFF`
  on the two lines above the pin. The `drift_report.py --check` reading is owed.
- AC14 — `tools/memory-tree/deviation_join.py` — `grep -n origin` over it printed nothing: `REF`
  retired, both docstrings and the fixture's remote-tracking ref line gone. The
  `check-remote-literals.sh` run is owed.
- AC15 — `python tools/memory-tree/deviation_join.py --approval author-recorded` — in the tree, no
  line says `DECISIONS.md is unread`; in a scratch clone `deviation_join.read_decision_ref` returned
  `None` and the ladder's text, opening `GOV_REMOTE names no-such-remote, which is no remote`, with
  `GOV_REMOTE` exported, and `origin/main` with it unset.
- AC16 — `tools/memory-tree/deviation_join.py` — govkit's update and re-render sentence predicate,
  copied into a probe, found 0 sentences across the kit's tracked files, and 1 in HEAD's file, the
  `add_plant` paragraph pairing `files.update` with `re-rendered`. The `govkit selfcheck` run is owed.
- AC17 — `python tools/memory-tree/deviation_join.py --approval author-recorded` — 30 records, none
  malformed and none refused, the rescope add of `TOOL-dTrueNorth-27` joining
  `2026-10-22-build-TOOL-dTrueNorth-27-deviation-28`; under `--approval by-risk` its header read
  `refused 5`, deviation-20, -21, -26, -29 and -30 on `refused:` lines and deviation-28 on none.

The `New arm:` lines of this unit on the Python selftests were observed at the close, in a scratch clone of `e583a7f42` with the breaks of `2026-10-22-build-TOOL-dTrueNorth-29-arm-breaks.md` staged one set at a time: under the `gen_build_index.py` selftest, breaks `u27-usage`, `u27-sections` and `u27-head-names`, 4 of its 5 arms red; under the `gen_build_index.py` selftest, break `u27-head-fixed`, 2 of its 5 arms red; under the `asbuilt_view.py` selftest, breaks `u27-head-fixed` and `u27-head-names`, its 1 arm red; under the `routed_commits.py` selftest, which runs `deviation_join.py`'s plant arms, break `u27-ref`, its 1 arm line red. Each staged break was restored with a checkout, and at `92a0dcb96` every one of those selftests printed all arms held. Its lines on the shell suites the flagged bar runs are owed with that bar, which the owner deferred past this landing.
