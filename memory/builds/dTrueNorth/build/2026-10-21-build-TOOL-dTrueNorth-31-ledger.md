# TOOL-dTrueNorth-31 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-31

No merge bar, no self-test suite and no gate leg ran in this pass. Each line below is a probe of the
changed code over `ef8fd59d0`, its red side observed against `ef8fd59d0`'s own file where one is
named, the changed file swapped for its `git show HEAD:` copy in a scratch kit. Fixture repositories
sat under a short `%TEMP%` path with no hook installed. The six `New arm:` lines of the spec, and
AC13's gate run over the tree, are owed to the close, RED-first and then GREEN.

**Evidences:** TOOL-dTrueNorth-31
- AC1 — `read_consumes_from --scan` — over four scratch specs (`none until` a backticked
  `ARCH-tRun-1` then prose; bare `none` with dash prose; backticked `none` with dash prose;
  `none until the reader lands`) it printed one line, the first spec's path and a tab, and ids mode
  printed nothing for any; the HEAD lib printed nothing in `--scan` mode for all four.
- AC2 — `main(["x", "--check", "--with-verdicts"])` — a child loading `gen_build_index.py` by path
  with the three verbs patched, stdout and stderr on one pipe, printed `verdict 29 exit 0`, `n29`,
  `verdict 30 exit 0`, `verdicts end`, `n9`, `drift` in that order; the HEAD generator printed `n29`
  and `n9` ahead of the first marker.
- AC3 — `asbuilt_view.check_view_merge(root, "v.md")` — in a scratch repository whose tracked
  `.gitattributes` held no merge line, under `GIT_CONFIG_GLOBAL` naming a `core.attributesFile` with
  `*.md merge=ours` (plain `check-attr` answered `ours`), the finding named DESIGN_VIEW and
  `unspecified`; with the global unset and `v.md merge=ours` in `info/attributes`, the finding named
  `.git/info/attributes`; with `w.md merge=ours` there and the tracked line `v.md merge=ours`, None;
  the tracked line alone, None. The HEAD check returned None in all four. `build_view_fixture` under
  `--template=` built with no `hooks` or `info` directory and read no finding.
- AC4 — `deviation_join.read_decision_ref(<scratch>)` — with `GIT_DIR` exported to this checkout's
  git directory, which has `origin`, a remote-less scratch repository answered `('main', '')` and
  `GIT_DIR` held its value after; the HEAD join answered `('origin/main', '')`.
- AC5 — `gen_build_index.scan_glob_readers` — over a scratch copy of the kit's modules beside the
  planted module it named `planted23.GUARDED`, `planted23.PLANTED`, `planted23.Planted.read_method`
  and `planted23.read_planted`; the HEAD walk named the second and fourth only. Over
  `tools/memory-tree/` it named the five readers §4 lists.
- AC6 — the S6 recording — with `subprocess.run` stubbed and every leak name exported, a scratch copy
  of `routed_commits.run_git` with `env=` taken out printed `routed_commits leaks inherits`, and the
  kit's own runners printed `AC1 design_lib leaks [] routed_commits leaks [] second list False`; the
  base reading of the no-env runner printed `[]`.
- AC7 — an `ast` read of `probes23` — the `deviation_join.read_population` and
  `gen_build_index.derive_audit_writers` values are lambdas calling those readers, neither calling
  `read_adding_commits`. Over an `audit-pin` deviation fixture the population row read one audit and
  one hand-back member, both dated, unmoved under each of the four pathspec modes.
- AC8 — `deviation_join.measure_fixture` — the base fixture read `ref` `main` before the remote and
  `origin/main` with 5 rows after `add_fixture_remote`; the `owner-unknown-id` fixture with the same
  remote and a run-branch row `FIX-dClosedLoop-99` read `origin/main`, its rows lacking the id, and
  the report render printed `its approver cites FIX-dClosedLoop-99, which no row of DECISIONS.md holds
  at origin/main`; rows read at the run branch's tip held the id, the red direction.
- AC9 — `GOV_DEFAULT_BRANCH=trunk python tools/memory-tree/deviation_join.py --fixture --plant rotated --policy refuse`
  — exit 0, no `unread at trunk` line; the HEAD join exited 1 printing one.
- AC10 — `grep -c` — `or the word external or none:\$_c_bad` in `unattended.sh` printed 1,
  `or the word external or none` in `unattended.test.sh` printed 3, `or the word external:` in
  `unattended.sh` printed 0.
- AC11 — `load_design_lib()` twice — under a namesake `design_lib` from a scratch file, the checker
  printed `same True caught True slot-namesake True`; the HEAD checker printed `same False caught False`.
- AC12 — the AC2 child with `cmd_check_asbuilt` raising `KeyError("planted")` — `verdict 30 exit 2`
  then `build-index: KeyError: 'planted'`, then `verdicts end`, `n9`, `drift`, exit 0; the HEAD
  generator died with the traceback before `--check` ran.
- AC13 — the closure line's counting expression over the review's 13 scanned paths printed
  `11 sibling module(s) and 2 other scanned file(s)`, over the control fixture's three `2 and 1`;
  `grep -c '2 sibling module(s) and 1 other scanned file(s)'` in the suite printed 1. The gate run
  over the tree is a leg, refused to this role, and owed to the close.
- AC14 — `grep -c -F -- '- **consumes-from** none — it builds on nothing'` in the suite printed 1.
  In a scratch clone of the branch carrying this driver, TOOL-dTrueNorth-30's CLOSED spec rewritten
  to that bare bullet, `--dispatch dTrueNorth --pass TOOL-dTrueNorth-31` printed `dispatch declared`;
  rewritten to `none until` a backticked `TOOL-dTrueNorth-31`, it failed check 49 ending
  `or the word external or none: memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-30.md`.
- AC15 — `grep -c -E '\$HERE"?/memory-tree'` in `check-spec-tokens.test.sh` printed 0, and
  `grep -c '"\$MEMORY_TREE"'` printed 6.
- AC16 — `python tools/memory-tree/deviation_join.py --approval author-recorded` — after `--write`
  with both records staged, exit 0, its head line `records 34 (0 malformed) · refused 0`, and no
  `refused:` or malformed line naming deviation-33 or deviation-34; the view re-rendered to 34
  deviation records.
