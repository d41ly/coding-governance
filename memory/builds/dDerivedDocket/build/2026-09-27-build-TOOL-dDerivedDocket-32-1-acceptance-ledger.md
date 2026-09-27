# TOOL-dDerivedDocket-32 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-32

Remote CI is built as one file, `.github/workflows/remote-ci.yml`, on `windows-latest` under Git-Bash
with `contents: read` and two GitHub-owned actions pinned by commit sha: `actions/checkout` v6.1.0 and
`actions/upload-artifact` v6.0.0, each sha read from `git ls-remote --tags` of its repository on
2026-09-27. On a push to main, `history-audit` runs the hygiene engine over a full-history checkout
and asserts the `memory-hygiene: check 25 ` prefix, and `bar` clones anonymously to
`C:/projects/coding-governance`, pins the pushed sha with `git checkout -B main`, runs the full bar
under `GATE_WALL=20400` (the window is 16040 to under 21600) and uploads `gate-logs` and any
last-failure file as `bar-<sha>`. Daily and on dispatch, `held-plan` derives one entry per `--list`
row and `held` runs each one as the sweep runs a suite, output written as it runs. The plan reads
the cap from the `held` job's own `timeout-minutes` rather than carrying a second 360.
`.gitattributes` pins `.github/workflows/*.yml` to LF, `.lexicon.conf` declares `yml::dark` and
re-stamps `ratified=` in its own form, and `.governance/deploy.toml` drops the `ci_file` answer. The
charter region was re-rendered by `adopt-playbook.sh --target .`, which moved only the CI line.
Its merge-bar section trims the 307-byte passage to a pointer at `tools/unattended/README.md`, which
now carries the moved fact. The follow-up sentence became one naming the workflow and its jobs.
`AGENTS.md` reads 63562 CR-stripped against 63691 at the parent. Both runner headers name the
schedule and still carry the compensating-check wording. The unattended header's "no NEW FAIL" had
been split across two lines, so it is re-flowed onto one.

The spec moved to rev-6 before the code: six line citations moved on the tree. AC12 was amended at
the same rev after running it, as its line below says. Rev-7 followed the bug-class checklist over
the built unit, which named `bounded-through-a-pipe-is-unbounded`: `timeout` bounds the suite and
not `tee`, which reads until its last writer closes. So the held run step now declares a per-entry
step timeout that the plan derives from the run bound. S9 and AC11 say so, and every reading below
was taken again over the rev-7 workflow.

No merge bar, no gate leg and no suite ran in this pass. The direct checks, and what each stands in for:

- a scratch reader of the workflow file, run on the real file and then on 23 scratch copies, one
  staged break each for every AC1, AC2, AC4, AC10 and AC13 break the spec names plus AC11's step
  timeout. Every break reddened the read written for it, and the copy was deleted after each run.
  This stands in for the absent permanent gate (§8 F2).
- the `held-plan` step's own body, extracted from the workflow and run by hand over the real
  `--list`. It took 72 rows and ran 72 one-row checks, then was re-run under four staged arms.
- the `held` step's own body over two synthetic entries, with a `python3` stub on `PATH`.
- `check-memory-hygiene.sh`, `adopt-playbook.sh`, `render_playbook.py` and `drift_report.py`, each
  run only inside scratch clones of a scratch commit carrying this unit's staged tree (F8 (a)).

The last group stands in for the `memory hygiene`, `playbook render wiring` and `drift-audit records`
legs, which run at the post-build bar. AC4, AC6, AC8 and AC9 carry `permission:` lines deferring
their leg readings to that bar, so none of them has a line here. The direct reads taken for them:

- AC4: the workflow's own `GATE_WALL=20400` and `timeout-minutes: 360`, and 16040 from the verb's
  predicate over the manifest.
- AC6: `yml::dark` in `LANGS`, and no `.github/` glob in the registry's `[surface]`.
- AC8: the write-mode render and the greps. `ci_file` counts 0. The absence grep counts 0 over both
  headers. `remote-ci.yml` and `no NEW FAIL` count 1 in each header. `stop receiving them too`
  counts 0 in the charter, and `adopters stop receiving` counts 1 in the kit README, which counts 0
  `tools/`. A scratch render with `.github/workflows/` removed exited 1 with
  `REFUSED — CI_FILE is derived by probe`, in write mode and under `--check`.
- AC9: in a scratch clone with the stamp reverted to 2026-09-05, `drift_report.py --check` exited 1
  naming `lexicon_ratified_older_than_language_surface = 1 (pin 0)`. The same signal read 0 at the
  re-stamp.

The drift report's other red in those clones, `non_terminal_specs_cited_by_product_source` 3 over
pin 2, reads the same in a clone of the parent `17841e72`, and cites three ids in files this unit
does not touch.

**Evidences:** TOOL-dDerivedDocket-32
- AC1 — `fetch-depth: 0` — the three counts read 3, 3 and 3. The scratch reader passed every
  property on the real file. Ten staged breaks each reddened their own property: `fetch-depth`
  deleted, `persist-credentials` deleted, the autocrlf step moved after a checkout, its `--global`
  dropped, the sha pin deleted, one job on `ubuntu-latest`, one `set-head` step deleted, one
  `shell: bash` deleted, a `${{ secrets.X }}` clone URL, and one `symbolic-ref` step deleted.
- AC2 — `uses:` — `grep -nE 'uses:'` lists five lines, each `actions/` pinned by 40 hex plus its tag
  comment. A tag in place of the sha, and a `someone/` action pinned by a 40-hex sha, each reddened
  the same pattern test.
- AC3 — `memory-hygiene: check 25` — the full clone printed the DORMANT line and the liveness step
  exited 0 over it. The engine itself exited 1, on check 23 alone. That check lists every closed
  unit's criteria still owed a ledger line, and this unit's share is AC4, AC6, AC8 and AC9, the
  four deferred above. The exit-0 half is therefore owed to the run after the orchestrator writes
  those lines. The `--depth 1 file://` clone read `--is-shallow-repository` `true` and printed the
  identical dormant line. A shallow clone of a builds-mode commit printed
  `check 25 DEAD PROBE — this is a SHALLOW repository`. The liveness step exited 1 with every
  check 25 line removed, and exited 1 again when the word `check` was the only match.
- AC5 — `held-plan` — 72 entries, whose union by name equals `--list`'s 72 rows, no name twice, every
  argv equal to its row. All 72 `--kit "<argv>" --list` checks selected exactly their own row. Four
  staged arms each exited 1 and emitted no matrix: one entry dropped (the union check named it), a
  key cut to `tools/unattended` (twelve rows selected), an unparseable row (named, plus the count
  mismatch), and a 257-row fixture (named the 256-entry limit).
- AC7 — `git check-attr eol` — reads `eol: lf`, and `git ls-files --eol` reads
  `i/lf w/lf attr/text eol=lf` for the staged file.
- AC10 — `if: always()` — the two uploads carry `if: always()` twice and `if-no-files-found: error`
  twice. The copy step names `gate-logs` under `if: always()`, and `held` tees into
  `../held-<safe>.log`, the workspace path its upload names. Three breaks each reddened their own
  read: an upload's `if: always()` deleted, the copy step's deleted, and the `tee` removed.
- AC11 — `platform-bounded` — every bound equals budget times `sweep-ceiling-factor` 2. The cap is
  21000 s, from `timeout-minutes: 360` in the `held` job. The one marked suite,
  `unattended gate selftest`, is the only row over the cap and runs at 21000. Every other row runs
  at its own bound. Every `step_minutes` equals the run bound plus 65 s rounded up to minutes, the
  largest 352 against the job's 360. The run step declares it, and a copy with that line deleted
  reddened the read.
- AC12 — amended rev-6 — the write-mode diff at a second path changed two lines, the registry row
  carrying the whole path and the preamble's project name carrying its final segment, so the
  criterion now names both. The other readings: --check printed the DRIFT line and exited 1; write
  mode printed PRIMARY_TREE_A derived as the second path; with origin/HEAD deleted the drift report
  exited 2 with "cannot resolve a default branch"; after set-head it no longer refused on its base
  ref. The bar job clones to the primary-tree path.
- AC13 — `branches: [main]` — `on:` holds exactly push to main, schedule and workflow_dispatch, and
  each job's `if:` routes it to its own triggers. Three breaks each reddened their own read:
  `branches: [master]`, an added `pull_request_target`, and the bar job's `if:` deleted.
- AC14 — `held-probe` — with a `python3` stub that exits 9009 (49 under MSYS) first on `PATH`, the
  probe entry resolved `python`, exited 0 and left `held-probe` in the workspace file. The sleeper
  under a 5 s bound exited 124 with its printed line in the file. A copy with the argv rewrite
  removed exited 49, failing on the stub.
