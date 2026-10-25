# TOOL-dGroundRules-34 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-34

No merge bar, no gate leg and no self-test suite ran in this pass. The build is the third dispatch's
saved patch, applied at `74d17b3a0` over `TOOL-dGroundRules-36`'s `check_guard_trace` change with no
conflict, and every criterion below was re-probed after it: `--fixture <case>` runs of
`tools/policy/check_policy.py` on the branch, `python -c` calls of its functions, and each literal
staging applied by a script under the run's scratchpad to a `git clone --local` of the branch, the
build committed there, under `%TEMP%/c34-<staging>`. Every fixture run also prints the guard-trace
`WRONG` lines this build's known reds name (`tools/template-size-limits.txt`, the kit descriptors,
and in a primary checkout `.git/index` and `.git/info/exclude`, the last the exclude-file read
`TOOL-dGroundRules-38` keeps out of the trace); the case lines themselves are quoted below. Criteria
AC11, AC12, AC15, AC16, AC32 and AC36 carry stripped spellings their restating units spell whole,
and each is observed through that unit's spelling. Owed at the close: AC6, AC25, AC30 and AC31,
which the workflows render in `tools/workflows/check-protocol-parity.test.sh` observes, and the
red-first observation of every `New arm:` line of §7.

**Evidences:** TOOL-dGroundRules-34
- AC1 — `build_source_snapshot` — over a fixture repository with `committed.txt`, an untracked `kept.txt` and a `local.lock` its `.git/info/exclude` names, the snapshot's `ls-tree -r --name-only HEAD` listed `['committed.txt', 'kept.txt']`: `kept.txt` in, `local.lock` out.
- AC2 — `git -C <r> ls-files -co --exclude-standard` — on the same fixture its sorted output equalled the snapshot's sorted `ls-tree` (`AC2 equal: True`); over this worktree both counted 6516 paths, none on either side only.
- AC3 — `git rev-parse --path-format=absolute --git-common-dir` — its parent, `C:\projects\coding-governance`, snapshotted to 6478 files, of which the `.claude/(worktrees/|scheduled_tasks.lock|mailbox/)` pattern matched `0`.
- AC4 — `inner` — a fixture repository holding an untracked nested repository `inner/` with one commit raised `the snapshot holds inner as a gitlink the source's index does not carry: a nested repository no ignore rule covers; ignore it in .../p34/n/.git/info/exclude`, naming `info/exclude`.
- AC5 — `grep -c "KIT_AGENT_CAP_VERSION" tools/workflows/check-protocol-parity.test.sh` — printed `0`.
- AC6 — `gov:fixed-verifiers` — owed at the close: the writer-marker staging is the workflows render's arm in `tools/workflows/check-protocol-parity.test.sh`, a gate leg this pass does not run.
- AC7 — `GOVKIT_LINES` — the `ast` probe printed nothing on the built `check_policy.py`.
- AC8 — `--fixture adopter-fresh-target` — with `govkit.py` renamed in a scratch clone, it printed `WRONG: no deployer to install with: looked at C:/Users/daily-agent/AppData/Local/Temp/c34-ac8/tools/govkit/govkit.py`, and `--fixture budgets-ships-join` printed `the deployer is located · WRONG: no deployer to install with: looked at` the same path.
- AC9 — `run_govkit("<repo>/tools", "<repo>", "plan")` — raised `run_govkit: .../unattended-dgroundrules-e47ae1/tools is no root build_source_snapshot made of ...; take build_source_snapshot first`, before any process started.
- AC10 — `build_source_snapshot` — a `git clone --local` made outside it printed `.../p34/lc is no root build_source_snapshot made of .../p34/a`, and the swapped call printed `.../p34/a is no root build_source_snapshot made of <the snapshot>`.
- AC11 — `arm_cap_census` — through `TOOL-dGroundRules-39` S2's spelling, `tools/govkit/registry.toml` and `vendor/gov/govkit/registry.toml` in a receipt-less repository: `python check_policy.py --repo <t>` printed the one finding `tools/govkit/registry.toml, vendor/gov/govkit/registry.toml: 2 govkit/registry.toml candidates, so the tool root is not guessed`, beside the framework's `population: zero` line.
- AC12 — `registry.toml` — through `TOOL-dGroundRules-39` S1's spelling, `tools/govkit/registry.toml`, `a/b/c/govkit/registry.toml` at depth 3 and a top-level `registry.toml`: `arm_cap_census · 33 finding(s) · 33 census row(s) joined`, every enforcer missing under `tools/`, and `0` ambiguity lines.
- AC13 — `--fixture census-ambiguous-registry` — printed `RED as planted`, `green unplanted` and `0 wrong`; with `derive_census_tree`'s two-candidate branch staged off in a scratch clone, it printed `WRONG: no finding names tools/govkit/registry.toml, vendor/gov/govkit/registry.toml`.
- AC14 — `git -C <t> ls-files --others "*registry.toml"` — over AC11's repository it listed `tools/govkit/registry.toml` and `vendor/gov/govkit/registry.toml`: the directory above `govkit/` is one segment, then two.
- AC15 — `True` — through `TOOL-dGroundRules-40`'s `PAIRS_PY`, `design_lib.check_writes_intersect` printed `True` then `False`.
- AC16 — `0` — through `TOOL-dGroundRules-40`'s `PAIRS_SH`, whole paths, `overlaps` printed `0` then `1`.
- AC17 — `TOOL-dGroundRules-40` — observed by that unit's AC3 under `RAW_BOTH`; this unit runs no command for it (rev-9).
- AC18 — `--fixture budgets-census-join` — printed `a request for no-such-cap · red naming it` and `a census row with no case · red naming it`, and no case `WRONG`; its one `WRONG` is the guard trace's `tools/template-size-limits.txt`.
- AC19 — `census-ambiguous-registry` — one `--fixture` run per case: `budgets-census-join` and `census-receiptless-target` printed no case `WRONG` (each only the known `tools/template-size-limits.txt` guard-trace line), and `census-adopter-receipt`, `census-default-adopter` and `census-ambiguous-registry` printed `0 wrong`.
- AC20 — `arm_schema` — a probe built the install-day target with `build_install_target`, ran `apply`, wrote a `policy.toml` with `on-invalid = "refuse"` and `budgets.enforce = "bogus"`, staged the install, and ran the installed `adopt-policy.sh --scaffold`: exit 2, `policy-check: arm_schema · 1 finding(s)`, `budgets.enforce: "bogus" is not one of ["warn", "refuse"]`, and no `mirror deferred`.
- AC21 — `prefix` — receipts holding `C:/x` and `/x` printed `its prefix is not of the shape the deployer writes`, and `..\\x` (JSON-escaped, the file holding one backslash) printed the same line, one finding each.
- AC22 — `probe_answer` — with `"{probe_answer}"` staged into the policy kit's `[adopt]` argv in a scratch clone, `--fixture adopter-fresh-target` printed `WRONG: the deployer's intake --kits policy,run-gates,memory-tree exited 2: govkit: the selected kits need answer(s) probe_answer and none was supplied. Refusing to invent one`.
- AC23 — `read_deploy_answers("<repo>")` — returned `manifest_path`, `memory_root`, `playbook_dir`, `playbook_path` and `user_skills`, with no `govkit-selftest:` line; with `DEPLOY_FULL` renamed in a scratch copy's selftest.py it raised `no [answers] table of DEPLOY_FULL to install with in .../p34f/tools/govkit/selftest.py`.
- AC24 — `git cat-file -e <the snapshot sha8 it printed>` — over a clone carrying one uncommitted edit, `--fixture adopter-fresh-target` printed snapshot `c40d46a9` and the command exited 128 in the source; with the snapshot's git calls staged to `GIT_DIR=<source>/.git` it printed `4b17a901` and the command exited 0.
- AC25 — `gov:fixed-writers` — owed at the close, through the workflows render's version staging in `tools/workflows/check-protocol-parity.test.sh`.
- AC26 — `ORDER_ROWS | wc -l` — printed 19, and `TOOL-dGroundRules-43`'s `ORDERS` printed 19.
- AC27 — `git ls-files -co --exclude-standard | wc -l` — the snapshot line read `· 6516 files · 5.1s` and the count over the same tree was 6516 (6510 on an earlier run, while another pass wrote untracked prompts; the snapshot's own list and `ls-files` matched path for path).
- AC28 — `WRONG` — the AC2 probe run from `%TEMP%/p34/elsewhere` printed none, and the lists were equal.
- AC29 — `gov_source` — `--fixture adopter-fresh-target` printed `156 assertion(s) executed · 0 wrong`; with `run_govkit` staged to run the source's own deployer past its refusal it printed `WRONG: the receipt's gov_source is 'C:\\Users\\daily-agent\\AppData\\Local\\Temp\\c34-ac29', not the snapshot`.
- AC30 — `does not admit the writer split:` — owed at the close, through AC6's staging in the workflows render.
- AC31 — `exited 1 with no reason` — owed at the close, through the workflows render; the fallback reads `the agent-cap hook exited $_ub_rc with no reason` in `tools/workflows/check-protocol-parity.test.sh`.
- AC32 — `165` — through `TOOL-dGroundRules-43`'s `EVIDENCE`, the build README spelled whole: `git show f4d31452a:memory/builds/dGroundRules/README.md | grep -n "gen:build-order"` printed `165` and `179`.
- AC33 — `run_in_gov` — `grep` printed lines 1193 and 1195, both inside `run_govkit`'s docstring, and `GOVKIT_LINES` printed nothing.
- AC34 — `suite-invalidated-by-a-commit-under-it` — `gotchas.py --for-paths tools/govkit/govkit.py` named it and `test-oracle-read-from-a-historical-sha`; the `build_source_snapshot` grep printed line 67, the new paragraph.
- AC35 — `git diff --name-only C~1 C -- "memory/builds/*/README.md"` — at `2999b6394`, the `TOOL-dGroundRules-32` pass commit writing READMEs, it printed the eight §4 names and `memory/builds/dGroundRules/README.md`; its other pass commit `5412bbecd` printed none.
- AC36 — `mirror deferred` — through `TOOL-dGroundRules-41` S3's spelling, the `## Install` section of `help/policy.md` holds it: the count printed `1`.
- AC37 — `invalid` — `tools/policy/README.md` line 631, the `arm_cap_census` row, and line 628, the `legacy-homes` row, each carry it.
- AC38 — `git -C <t> status --porcelain` — `build_install_target("p", ids)` over the closure `policy, run-gates, memory-tree` left `0` `[gate_runner` headers, printed nothing, and `apply` through `run_govkit` exited 0.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: AC8 govkit.py renamed -> budgets-ships-join and adopter-fresh-target `WRONG: no govkit kit holding govkit.py in this install: looked in ...`; AC13 derive_census_tree answers source at first candidate -> census-ambiguous-registry `WRONG: no finding names ... '2 govkit/registry.toml candidates'`; AC18 (designed) census join findings kept only for adopter -> budgets-census-join `WRONG: []` and `WRONG: [('zz-planted', ...)]` (2 wrong); AC19 its red is AC13's break; AC22 {probe_answer} in [adopt] -> `WRONG: ... need answer(s) probe_answer`; AC29 run_govkit past SNAPSHOT_ROOTS -> `WRONG: the receipt's gov_source is ... not the snapshot`. GREEN `223 assertion(s) executed · 0 wrong`, census cases 0 wrong. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: adopt-policy.test.sh with adopt-policy.sh at 75b1ffe59^: `FAIL --scaffold over an invalid policy file on install day refuses`; check-protocol-parity.test.sh writer-marker arm (AC6): unit 30's writer_mark run, rc 1.
