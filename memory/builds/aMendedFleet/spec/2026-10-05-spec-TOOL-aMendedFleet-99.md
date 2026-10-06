# TOOL-aMendedFleet-99 — the held job runs its suites from the tree path the bar job uses

**Status:** CLOSED · rev-1 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · order 100

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

Two suites red on every daily held run for a host reason the census filed as cause C3. The `held`
job in `.github/workflows/remote-ci.yml` gets its tree from `actions/checkout` under the workspace,
`D:/a/coding-governance/coding-governance/tree`, while the `bar` job clones to the primary-tree path
`C:/projects/coding-governance`. The suites were written for that second shape. The manifest-check
suite clones the tree with `git clone --local` into a temp root on `C:`, and from `D:` that clone
fails with `Improper link`. The process-monitor adopter suite checks the tracked
`.process-monitor.conf`, whose roots name the primary-tree path, and on the runner that path does
not exist. This unit makes the `held` job obtain its tree the way the `bar` job does, so both suites
run where every recorded green was earned. It also records the recurrence in the gotcha that owns
this class.

## 2. Scope (IN)

- **S1** — The `held` job obtains its tree by the `bar` job's own recipe: an anonymous
  `git clone "$GITHUB_SERVER_URL/$GITHUB_REPOSITORY.git" "$PRIMARY_TREE"`, then
  `git checkout -B main "$GITHUB_SHA"` inside it, then the existing step asserting that
  `refs/remotes/origin/HEAD` resolves. Its `actions/checkout` step and its `git remote set-head`
  step are retired, because the clone writes the full history and sets `origin/HEAD` itself, and
  every later step's `working-directory: tree` becomes `${{ env.PRIMARY_TREE }}`. The job's display
  name, matrix, timeouts and run-step body are unchanged. Observed by AC1 and AC2.
  **Readers:** by name: `.github/workflows/remote-ci.yml` alone spells the held job's
  `actions/checkout` step, its `git remote set-head` step and its `working-directory: tree` lines;
  the `history-audit` and `held-plan` jobs keep their own copies, which this unit does not touch.
  by value: the held job's later steps, which read the tree at its working directory, and the
  `held-plan` job's `awk` program, which reads the held job's job-level `timeout-minutes` line and
  is observed unchanged by AC2.
- **S2** — `PRIMARY_TREE` is declared once, in a workflow-level `env:` block, with the value the
  `bar` job declares today, and the `bar` job's own job-level `env:` block is removed, so the path
  is one fact in one place and the two jobs cannot name different trees. Observed by AC1.
  **Readers:** by name: the `bar` job's clone, pin, origin-HEAD and bar steps and its record-copy
  step, which spell `PRIMARY_TREE`; and the `held` job's steps S1 writes. by value: the clone
  destination, which `tools/playbook/render_playbook.py` derives `PRIMARY_TREE_A` from when the
  bar renders the charter; the value does not change, so that reader sees the same path.
- **S3** — The held log path `HELD_OUT` is anchored at the workspace rather than at `..` relative to
  the tree, and the run step converts it with `cygpath -u` before `tee` writes it, because the
  upload step resolves `held-<safe>.log` against the workspace and fails on a missing file. Observed
  by AC3.
- **S4** — The workflow's header paragraph that says why the bar clones to the primary-tree path
  gains the held job and its reason: the tracked conf's roots and the temp root's volume.
  NOT OBSERVED — a comment no reader parses; the closing diff review reads it.
- **S5** — `memory/gotchas/fixture-inherits-ambient-machine-state.md` gains an "It bit again"
  paragraph naming the checkout's path and the volume it shares with the temp root as ambient state,
  anchored on the workflow and on the two suites, and its ambient-state list gains that entry.
  `memory/gotchas/INDEX.md` is re-rendered by `python tools/memory-tree/gotchas.py --write` in the
  same commit. Observed by AC4.

## 3. Non-goals (OUT)

- Making either suite portable to a checkout on another volume or at another path. That is the
  class the gotcha records; the remote CI host is made to match the shape every node has, for the
  same reason the `bar` job already clones there.
- The `history-audit` and `held-plan` jobs. Neither runs a suite that reads the tree's path or
  volume, and moving them buys nothing the census observed.
- Any other cause the census filed against these two suites. The census did not observe whether a
  stdio-codec or bare-`bash` failure also reds them, because each run stopped at C3 first; those are
  causes C1 and C2, units `TOOL-aMendedFleet-97` and `TOOL-aMendedFleet-98`.
- Renaming the held jobs. Unit `TOOL-aMendedFleet-9` reads them as `held <suite name>`.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; `git diff --stat 7af5f564 HEAD` is empty for every file below at HEAD
`34a99ad1`, and node d's branch `origin/branch/unattended-build-closing-f90fd9` carries the same held
job unchanged, so there are no bytes of node d's to reuse.

- `.github/workflows/remote-ci.yml` gives the `bar` job a job-level `PRIMARY_TREE:
  C:/projects/coding-governance`, clones there and pins `$GITHUB_SHA`. Its header says why: the
  charter renders that path from wherever the clone sits. The `held` job uses `actions/checkout`
  with `path: tree` and runs every step with `working-directory: tree`; `HELD_OUT` is
  `../held-${{ matrix.safe }}.log`, and the upload step's `path` is the same name with
  `if-no-files-found: error`.
- The run step sets `TMPDIR` to a fresh `mktemp -d`, which on the runner's Git-Bash is under the
  user temp directory on `C:`.
- `skills/session-kickoff/manifest-check.test.sh` line 699 runs `git clone -q --local "$GOVROOT"
  "$CCLONE"` with `$CCLONE` under that temp root. The census quotes the runner's `fatal: failed to
  create link ... Improper link` and the 103 FAIL lines that follow from the missing fixture. That
  the message is the cross-volume hard-link error rather than a link restriction of the `D:` volume
  itself is UNVERIFIED; both readings are cured by putting the tree on the temp root's volume.
- `tools/process-monitor/adopt-process-monitor.sh` line 142 refuses a `PROCMON_ROOTS` entry that is
  not a directory, and `.process-monitor.conf` line 31 declares `C:/projects/coding-governance` and
  its MSYS spelling. Push run `37220352485` printed `GATE ok    process-monitor wiring` from the
  `bar` job's clone at that path.
- Ran on node a at base: the AC1 program prints `None held ${{ matrix.name }} ['-', 'tree'] 1`, and
  the `held-plan` job's `awk` program prints `360`.

### Mechanism

The `held` job's checkout block becomes a copy of the `bar` job's: the global autocrlf step it
already has, the clone, the pin, and the origin-HEAD assertion, in that order. The clone needs no
credential, as the `bar` job's does not, and writes the full history, which is what
`fetch-depth: 0` bought. `actions/checkout` refuses a `path` outside the workspace, so the clone is a
plain `git clone`, which is why the `bar` job uses one.

S2 moves the declaration up one level. GitHub Actions makes a workflow-level `env` visible to every
job's steps and to `working-directory` expressions, which is all either job reads.

S3 sets `HELD_OUT: ${{ github.workspace }}/held-${{ matrix.safe }}.log`. On the Windows runner that
expression expands with backslashes, so the run step writes to `$(cygpath -u "$HELD_OUT")`, which
the `held-plan` job already relies on `cygpath` for.

### Files touched (estimate)

- `.github/workflows/remote-ci.yml`
- `memory/gotchas/fixture-inherits-ambient-machine-state.md`
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- **Patch the two suites instead.** `--no-hardlinks` on the manifest-check clone fixes one suite,
  but the process-monitor arm grades the tracked conf, whose roots are this repository's real
  primary tree, and rewriting a tracked conf to suit a CI host is the inverse of the fix. The `bar`
  job already chose the host-side route for the same class.
- **Point `TMPDIR` at a directory on `D:`.** It cures the clone and leaves the conf's roots missing.
- **A second job-level `PRIMARY_TREE` on the held job.** Two copies of one path, the drift S2 closes.

## 5. Production-readiness checklist

- security — no new credential, permission or event; the clone is anonymous and read-only, as the
  `bar` job's already is.
- perf / scale — a full clone per held matrix entry where a full-history checkout ran before; the
  same objects cross the wire.
- error / empty / loading states — a failed clone fails its step and the job, as in the `bar` job.
- observability — the held logs keep their names and upload exactly as before.
- risks — the first scheduled run after landing is the only place the change runs; AC5 reads it.
- testing — AC1 to AC4 are seconds on node a; AC5 is the remote observation.
- migration — N/A: no data or conf moves.
- user docs — N/A: no user-facing surface; the gotcha is the record.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys,yaml; w=yaml.safe_load(open(sys.argv[1],encoding='utf-8')); h=w['jobs']['held']; s=h['steps']; print(w.get('env',{}).get('PRIMARY_TREE'), h['name'], sorted({x.get('working-directory','-') for x in s}), sum('checkout@' in x.get('uses','') for x in s))" .github/workflows/remote-ci.yml`
  runs on node a, it prints `C:/projects/coding-governance`, the unchanged `held ${{ matrix.name }}`,
  a working-directory set of `-` and `${{ env.PRIMARY_TREE }}` only, and `0`.
  Red when: the held job keeps its `actions/checkout` step or a `working-directory: tree`, or
  `PRIMARY_TREE` stays job-level; at base it prints `None`, `tree` and `1`.
- **AC2** — When the `held-plan` job's own reader,
  `awk '/^  [A-Za-z0-9_-]+:[[:space:]]*$/ { held = ($1 == "held:") } held && /^    timeout-minutes:[[:space:]]/ { print $2; exit }' .github/workflows/remote-ci.yml`,
  runs on node a, it prints `360`.
  Red when: the edit moves or re-indents the held job's job-level `timeout-minutes` line, so the plan
  refuses every scheduled run with `the held job declares no usable timeout-minutes`.
- **AC3** — When `grep -n 'HELD_OUT' .github/workflows/remote-ci.yml` runs, the env line's value
  begins `${{ github.workspace }}/` and the line that runs `tee` passes it through `cygpath -u`.
  Red when: the value stays `../held-` relative, which under the moved working directory writes the
  log beside the clone, outside the workspace, and the upload fails every held job.
- **AC4** — When `python tools/memory-tree/gotchas.py --for-paths .github/workflows/remote-ci.yml`
  runs, its checklist lists `fixture-inherits-ambient-machine-state`, and
  `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: S5's paragraph carries no backticked workflow path, so the class stays unselected for a
  diff to the workflow, as it is at base; or `INDEX.md` was not re-rendered and check 17 reds.
- **AC5** — When the first scheduled run of `remote-ci.yml` after landing completes,
  `gh run view <run id> --log-failed` carries no `Improper link` line in the
  `held manifest-check self-test` job and no `FAIL test_shipped_conf_is_accepted` line in the
  `held process-monitor adopter selftest` job.
  Red when: the clone lands off the temp root's volume or at another path, so either line returns.
  permission: remote CI after landing, which no unit pass can trigger.
  cost: up to one day, the schedule's period.
  fixture: node a holds no second volume beside its temp root, so the cross-volume failure cannot be
  staged here; the census's three runs are the before-reading.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

The workflow carries no permanent gate, as its header says; AC1 to AC3 are its contract checks, and
AC5 is the remote observation.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the census journal's C3 row and the workflow, the two
  suites and the conf at base, with AC1 and AC2's programs run on node a at base.

## 10. Reuse audit

The seam is the `bar` job's clone recipe in `.github/workflows/remote-ci.yml`, landed by
`TOOL-dDerivedDocket-32`, which S1 copies step for step; no symbol-level seam fits.
`python tools/codebase-map/reuse_lookup.py "remote CI job clones the repository to the primary tree path before running"`
returned only name-stem neighbours such as `resolve_session_tree` in `tools/runlog/extract.py`, and
it prints `unscanned layers: .sh`, so it cannot see a workflow or a shell seam at all; the seam was
found by reading the workflow. Recall returned the round-1 spec audit of that unit, which records
that `actions/checkout` cannot place a tree outside the workspace and so the `bar` job clones, and
the gotcha `memory/gotchas/fixture-inherits-ambient-machine-state.md`, which names the launch path
and `TEMP` shape as ambient state already.

Where the report and the tree disagree: the brief's census row is confirmed at HEAD with one
qualification. The census reads `Improper link` as a cross-volume failure; that reading is
UNVERIFIED here, and the fix does not depend on it.

Recall terms used: `python tools/memory-recall/query.py "why does the remote CI bar job clone to the primary tree path instead of the checkout workspace, and do held self-tests depend on that path" --terms "remote-ci held job bar PRIMARY_TREE clone checkout workspace primary-tree path hosted runner windows-latest volume"`
