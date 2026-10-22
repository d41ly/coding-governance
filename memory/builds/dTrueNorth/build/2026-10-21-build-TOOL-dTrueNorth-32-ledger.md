# TOOL-dTrueNorth-32 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-32

No merge bar, no self-test suite and no gate leg ran in this pass. Each line below is a probe of the
changed code over `1dec4fbf1`, its red side observed against that commit's own file, read through
`git archive HEAD` into a scratch kit, or against a staged break in a scratch copy where the base
already held the line under test. Fixture repositories sat under a short `%TEMP%` path with no hook
installed. The four `New arm:` lines of the spec are owed to the close, RED-first and then GREEN.

**Evidences:** TOOL-dTrueNorth-32
- AC1 — `asbuilt_view.check_view_merge(root, "v.md")` — in a scratch repository whose HEAD holds no
  `.gitattributes` and whose parent sets `v.md merge=ours`, the call returned the unguarded-view
  finding naming DESIGN_VIEW and `merge=ours` plainly, with `GIT_ATTR_SOURCE` exported naming the
  parent, and with a local `git config attr.tree` naming it; a plain `check-attr` answered `ours`
  under each, so both plants moved the read. The HEAD module returned None under both.
- AC2 — `asbuilt_view.check_view_merge(root, "v.md")` — with `[attr]keep merge=ours` committed and
  `v.md keep` in `info/attributes`, and with `v.md keep` committed and the macro in
  `info/attributes`, each returned the finding naming `.git/info/attributes` and tracked state's
  `unspecified`; with `v.md merge=ours` in both, None. The HEAD module returned None for the first
  two and the finding for the agreeing third.
- AC3 — `tools/unattended/unattended.sh` — the remedy grep printed 1 there, the rule's grep printed 4
  in `tools/unattended/unattended.test.sh`, and `or the word external or none` printed 0 in each; at
  HEAD the last printed 1 and 3.
- AC4 — `read_consumes_from --scan` — over three scratch specs it printed `one.md` and a tab,
  `two.md` and a tab, and `three.md`, a tab and `ARCH-tRun-3`; ids mode printed `ARCH-tRun-3` alone
  for the third and nothing for the first. The HEAD lib printed only the third spec's row.
- AC5 — `gen_build_index.scan_glob_readers` — over a scratch copy of the kit beside §4's planted
  module it named `planted23.outer_class`, and over `tools/memory-tree/` the five readers §4 lists;
  the HEAD walk named no `planted23.outer_class`.
- AC6 — `probes23` — an `ast` read found the `deviation_join.read_population` lambda's one set
  display holding `audit` and `handback`, and the `row_grammar._build_backlog_pathspecs` lambda's
  constants `ARCH-tOne-8` and `ARCH-tOne-9`; `grep -c 'ARCH-tOne-8'` printed 4. HEAD's two lambdas
  held neither.
- AC7 — `deviation_join.build_fixture(root, [])` — with `GIT_TEMPLATE_DIR` naming a scratch
  template whose `config` declares `[remote "origin"]`, `git -C <root> remote` printed nothing, and
  the `--template=` grep over the kit's modules printed 0; HEAD's `build_fixture` printed `origin`
  and the grep printed 4.
- AC8 — `tools/unattended/lib-unattended.sh` — the `external. nor .none. ` grep printed 0 there, and
  `its wrapped lines included` printed 2 there and 1 in `tools/unattended/unattended.sh`; at HEAD
  they printed 1 and 0.
- AC9 — `scan_glob_readers` — the AC5 probe named `planted23` and `planted23.Planted`; the grep
  for `The walk reaches every depth` printed 0 and the one for `charged to exactly one name` printed
  2 in the generator. The HEAD walk named neither.
- AC10 — `asbuilt_view.read_info_merge(root, "v.md")` — with the module's `run_git` swapped for a
  stand-in answering exit 128 with no stdout to `rev-parse`, it returned
  `('info/attributes', 'nothing, exit 128')`; with the real runner and no `info/attributes`, None.
  The HEAD module returned None for the failed read.
- AC11 — `attribute source tree` — the phrase and `untracked info/attributes` each printed at least
  1 for `tools/memory-tree/asbuilt_view.py`, `tools/memory-tree/HYGIENE.template.md` and
  `memory/HYGIENE.md`; at HEAD all three printed 0. The two HYGIENE copies differ only at the three
  placeholder lines they differed at before.
- AC12 — `gen_build_index.read_carries_coverage(t, conf)` — with a scratch checker raising its own
  `DesignRefusal` and a namesake `design_lib` in `sys.modules`, it raised the module's Problem
  holding `carries join refused` and ending `the scratch checker's own refusal`; with the catch's
  checker branch taken out in a scratch copy it escaped as `DesignRefusal`. The grep for
  `carries join refused` printed 3, against HEAD's 2.
- AC13 — `planted23.outer.inner` — the AC5 probe named it and no `planted23.outer`, and the grep
  printed 1; a scratch copy charging every enclosing scope too named `planted23.outer`.
- AC14 — `asbuilt_view.build_view_fixture(root)` — under `GIT_TEMPLATE_DIR` naming a template whose
  `info/attributes` holds `*.md merge=binary`, `read_view_inputs` answered no finding and the fixture
  held no `info/attributes`; with the init's `--template=` taken out in a scratch copy, the finding
  named `binary`. `grep -c 'system attributes file'` printed 2. The `check_template_arm` probe held
  both halves, and its second half went red with the scratch read's `--template=` taken out.
- AC15 — `GIT_CONFIG_GLOBAL` — the parity scan's derivation over the kit's modules counted 0
  spellings of the three names, against HEAD's 3; `grep -c 'GIT_CONFIG_GLOBAL'` in the hygiene suite
  printed 0; and every key the derivation reads is declared in the example conf or exempt, with no
  exemption stale, where HEAD's left `GIT_CONFIG_GLOBAL` undeclared.
