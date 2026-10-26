# TOOL-dSafePassage-12 — gov's remote CI at the interpreter floor, read from its one declaration, with the floor's preflight as the bar's first step

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0029@4aeb7648 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-12-deviation-112.md](../build/2026-10-23-build-TOOL-dSafePassage-12-deviation-112.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-13 |
| [2026-10-26-prompt-TOOL-dSafePassage-12-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-12-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-8 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |

<!-- /gen:spec-records -->

## 1. Goal

Every job of `.github/workflows/remote-ci.yml` that runs Python sets up Python at the floor, in the
same landing that raises it (AP-30). The version is read from the floor's one declaration, and the
action is pinned by full commit sha. The floor's preflight is the bar's first step. The floor step
is applied to gov's own tree first, with its witness recorded. Today the workflow runs
`windows-latest` with no setup step at all, and each job takes whatever `resolve_python` finds
(`gap-tool-23`).

## 2. Scope (IN)

- **S1** — Each of the four jobs runs Python, which makes all of them in scope: `history-audit`
  runs the hygiene engine (`remote-ci.yml:73`), `bar` runs the merge bar (`:106`), `held-plan`
  resolves Python itself (`:163-164`), and `held` does too (`:314-315`). Each job gains two steps,
  placed after the step that puts the tree on disk and before the first step that runs Python.
  The `floor` step reads the declaration and the `Python at the floor` step sets it up.
  Observed by AC1.
- **S2** — The setup step is `actions/setup-python`, GitHub-owned like the workflow's two other
  actions, and pinned by its full commit sha with its tag in the comment beside it (`:27`, `:58`,
  `:118`). The pin is read from `git ls-remote --tags https://github.com/actions/setup-python` at
  build time, the way TOOL-dDerivedDocket-32's ledger read the other two. Observed by AC2.
- **S3** — The version is read from its one declaration. The `floor` step reads
  `tools/lib/python-floor.txt` from the tree the job just put on disk. It refuses any content but
  `<major>.<minor>`, and writes `floor=<value>` to `$GITHUB_OUTPUT`. The setup step's
  `python-version` is `${{ steps.floor.outputs.floor }}`, so no version is typed in the workflow.
  Observed by AC3 and AC5.
- **S4** — The floor's preflight is the bar's first step. In the `bar` job, the step after the
  setup runs `bash tools/lib/python-floor.sh preflight` from the primary tree, before the merge bar
  step (`:104-106`). No step between the setup and the preflight runs Python. Observed by AC4.
- **S5** — The header comment says what is new and what it does not check. It names the setup and
  the preflight under "WHAT RUNS". "No permanent gate grades this file's text" (`:15`) is amended:
  TOOL-dSafePassage-11's floor query reads its `python-version` lines, and nothing else grades the
  file. Observed by AC6.
- **S6** — The floor step is applied to gov's own tree, with its witness recorded, so gov is the
  first tree it migrates. TOOL-dSafePassage-8's lander runs `lib/python-floor-3.15` on gov's tree
  in this landing's prepared merge and records it in gov's receipt. This unit observes that record
  at the close. Observed by AC7.
- **S7** — The setup is live on GitHub's runner. The first push of the landing runs the four jobs
  at the floor. Observed by AC8.

## 3. Non-goals (OUT)

- The floor's declaration, its preflight and the resolver's refusal. They are
  TOOL-dSafePassage-11's.
- The lander's gov-first walk. It is TOOL-dSafePassage-8's.
- The CI that dShippedRelease emits for adopters, a Linux runner and a matrix of versions.
- A permanent gate over the workflow's job set. The file's own precedent, stated at `:15-16`, is a
  contract observed by staged breaks on a scratch copy and recorded in the acceptance ledger (§8 F1).
- Quoting the launcher that the `held` step splices into `bash -c` (`:317`). The toolcache path
  carries no space, as §5 records.
- Any other action, trigger, permission or timeout.

### Edges

- **consumes-from** `TOOL-dSafePassage-11` — the declaration `python-floor.txt`, `python-floor.sh preflight` and the floor query `python_floor.py check`; without them S3 has nothing to read, S4 nothing to run and AC3's query nothing to grade
- **consumes-from** `TOOL-dSafePassage-8` — the lander's gov-first walk, which records `lib/python-floor-3.15` in gov's source-mode receipt; without it AC7 observes nothing
- **consumes-from** external — GitHub's `actions/setup-python` serving Python 3.15 for `windows-latest`, which is UNVERIFIED on 2026-10-23 and is observed by AC8
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built

## 4. Design

### The two steps, per job

Spelled once here, and placed in each of the four jobs, after the job's last git-only step and
before its first step that runs Python. `<tree>` is `tree` in `history-audit` and `held-plan`, and
`${{ env.PRIMARY_TREE }}` in `bar` and `held`, whose trees are cloned there.

```yaml
      - name: the floor, read from its one declaration
        id: floor
        working-directory: <tree>
        run: |
          floor=$(tr -d '\r\n' < tools/lib/python-floor.txt) || floor=""
          if ! [[ "$floor" =~ ^[0-9]+\.[0-9]+$ ]]; then
            echo "floor: tools/lib/python-floor.txt holds '$floor', not <major>.<minor>" >&2
            exit 1
          fi
          echo "floor=$floor" >> "$GITHUB_OUTPUT"
      - name: Python at the floor
        uses: actions/setup-python@<40-hex sha> # v<tag>
        with:
          python-version: ${{ steps.floor.outputs.floor }}
```

The validation runs before anything is written to `$GITHUB_OUTPUT`, so a value carrying a newline
cannot add an output line of its own. The `${{ }}` value reaches only the action's input, never a
shell. The sha read on 2026-10-23 for the newest tag, v7.1.0, was
`6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`. That value is PINNED as of that date, and the build
pass reads it again, since a newer tag may exist by then.

### The bar's first step

In `bar`, between the setup and `the merge bar, every leg guard ignored, walled inside the job
limit`:

```yaml
      - name: the floor's preflight, the bar's first step
        working-directory: ${{ env.PRIMARY_TREE }}
        run: bash tools/lib/python-floor.sh preflight
```

It prints the interpreter the resolver accepted and its version, or the resolver's refusal, and
it exits 1 on that refusal before the bar starts. The local bar needs no such step. It resolves
Python before its first leg (`tools/run-gates/run-gates.sh:218`), and the resolver refuses below
the floor (TOOL-dSafePassage-11 S2).

### Which interpreter each job then resolves

`setup-python` puts the toolcache interpreter on `PATH`. The resolver passes over any candidate
below the floor and any that does not run, such as the Store stub. It takes the first at the floor,
and from that landing on it prints its direct executable (TOOL-dSafePassage-11 S3). No
`GOV_PYTHON` is set, because the floor check makes the choice deterministic among the candidates
`PATH` offers.

### Inventory

Minted: the step id `floor` in each of the four jobs, read only by that job's setup step. No file,
function, conf key, policy key or gate leg is minted.

### Rollout

The workflow lands with TOOL-dSafePassage-11 in this build's one landing, because the clause is
"in the landing that raises it". The first push to main after the landing runs the four jobs at
the floor. A runner without Python 3.15 fails the setup step loudly; it does not fall through to
an older interpreter.

### Files touched (estimate)

- `.github/workflows/remote-ci.yml`

### Alternatives rejected

- **`python-version-file:` pointing at the declaration.** The input's handling of a path outside
  the workspace is UNVERIFIED, and `bar` and `held` clone outside it, to `PRIMARY_TREE`. One
  explicit read serves all four jobs alike and validates the value.
- **A literal `python-version: '3.15'`.** It types the fact a second time, and TOOL-dSafePassage-11's
  query reds it.
- **The preflight as a leg of the bar.** The legs run concurrently, so a leg has no "first". The
  local bar's resolver already refuses below the floor (§8 F2).

## 5. Production-readiness checklist

- security: one more GitHub-owned action, pinned by full sha like the other two, under the same
  `contents: read`, on no event a fork can trigger. The floor value is validated before it reaches
  `$GITHUB_OUTPUT`, and it reaches the action's input only.
- perf / scale: one setup per job. The toolcache install is cached on hosted runners, and the
  measured cost is AC8's.
- error / empty / loading states: an absent or malformed declaration fails the `floor` step and
  names the file. A version the action cannot serve fails the setup step. A below-floor result
  fails the preflight in `bar` and the resolver in the other three jobs.
- observability: the `floor` step's output line, the action's own log of the version installed,
  and the preflight's line naming the interpreter.
- risks: if the action cannot serve 3.15 on `windows-latest`, every job fails, and this is
  UNVERIFIED until AC8. The `held` step splices `$PY` unquoted into `bash -c` (`:317`). A
  toolcache path with no space is safe, and a space would break it. That is recorded here and not
  fixed (§3).
- testing: the probes of §6 over the file and over a scratch copy with staged breaks, recorded in
  the acceptance ledger as `:15-16`'s precedent does. TOOL-dSafePassage-11's query arm reads the
  `python-version` lines permanently.
- migration: N/A — a CI file gains steps, and no data or adopter surface moves.
- user docs: N/A — gov's own CI is no user-facing surface, and no `help/` page describes it.

## 6. Acceptance criteria

- **AC1** — When `awk '/^jobs:/{f=1;next} f&&/^  [a-z][a-z-]*:$/{j=$1;n[j]=0} f&&/uses: actions\/setup-python@/{n[j]++} END{for(k in n)print k, n[k]}' .github/workflows/remote-ci.yml`
  runs, it prints `history-audit: 1`, `bar: 1`, `held-plan: 1` and `held: 1`, and no other line.
  Red when: a job that runs Python has no setup step. Staged on a scratch copy by deleting the
  `held` job's setup step, the probe prints `held: 0`.
- **AC2** — When `grep -cE 'uses: actions/setup-python@[0-9a-f]{40} # v[0-9]+\.[0-9]+\.[0-9]+$' .github/workflows/remote-ci.yml`
  and `grep -c 'uses: actions/setup-python@' .github/workflows/remote-ci.yml` run, both print `4`.
  Red when: a setup step is pinned by tag or branch, staged on a scratch copy as `@v7`.
- **AC3** — When `grep -c 'python-version: ${{ steps.floor.outputs.floor }}' .github/workflows/remote-ci.yml`
  runs, it prints `4`. When `python "tools/lib/python_floor.py" check` runs, it names no line of
  the workflow and exits 0. On a scratch copy with one setup step's input staged as
  `python-version: '3.14'`, it names that line of `.github/workflows/remote-ci.yml` and exits 1.
  Red when: a version is typed in the workflow instead of read from the declaration.
- **AC4** — When `awk '/^  bar:/{f=1;next} /^  [a-z][a-z-]*:$/{f=0} f&&/- name:/{print NR": "$0}' .github/workflows/remote-ci.yml`
  runs, `the floor, read from its one declaration`, `Python at the floor` and `the floor's
  preflight, the bar's first step` print after `origin/HEAD resolves before any bar command runs`
  and in that order, with no step
  between them. The next step printed after the preflight is `the merge bar, every leg guard
  ignored, walled inside the job limit`.
  Red when: the preflight follows the bar, is missing, or has a step running Python ahead of it.
  Staged on a scratch copy by moving the preflight below the bar step, the order inverts.
- **AC5** — When the `floor` step's `run:` body, cut from the file with `awk`, runs under `bash` in
  a scratch directory whose declaration holds `3.15` and with `GITHUB_OUTPUT` set to a scratch
  file, it appends `floor=3.15` and exits 0. With the declaration holding `3.15` and a second line
  `x=1`, it exits 1 naming the declaration, and the output file gains no line.
  Red when: the value is written before it is validated, or the newline-joined value passes.
  fixture: the run's scratch directory.
- **AC6** — When `grep -n 'python_floor.py\|setup-python\|preflight' .github/workflows/remote-ci.yml`
  runs, the header comment names the setup and the preflight under "WHAT RUNS", and names the
  floor query beside the sentence about permanent gates.
  Red when: the header still says that no permanent gate grades the file.
- **AC7** — When `git show "HEAD:.governance/install.json"` is read on the prepared merge, after
  the close's `push-main.sh --prepare`, its `steps` holds `lib/python-floor-3.15` with state
  `applied`.
  Red when: the landing reaches the remote before gov's tree has run the step.
  permission: the prepare is the main loop's, at the close. No unit pass runs the lander.
- **AC8** — When remote CI's first run on the landed sha completes, the `bar` job's log shows the
  setup installing 3.15, and shows the preflight naming a 3.15 interpreter before the bar's first
  leg.
  Red when: any of the four jobs fails at its `floor`, setup or preflight step.
  permission: remote CI runs only on a push to main, which is the lander's. It is observed after
  the landing and recorded in the acceptance ledger.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`.github/workflows/remote-ci.yml` trips no leg's guard. The leg named first carries
TOOL-dSafePassage-11's floor-query arm, which reads this file's `python-version` lines, and this
unit adds no arm (§8 F1). What nothing checks permanently: that every job keeps its setup step,
and that the preflight stays first. AC1 and AC4 observe both once, by staged breaks on a scratch
copy.

## 8. Open questions

- **F1 — Does a permanent arm hold the job set, or staged breaks recorded in the ledger?** Options:
  (a) staged breaks on a scratch copy, recorded in the acceptance ledger, which is the file's own
  contract (`remote-ci.yml:15-16`, TOOL-dDerivedDocket-32), with TOOL-dSafePassage-11's query
  reading the `python-version` lines permanently; (b) a new arm parsing the workflow's jobs, which
  needs a YAML reader the stdlib does not ship (veto 2) or an awk grammar of the file's indentation.
  RESOLVED (agent, 2026-10-23, delegated): (a). The literal pin, the failure most likely to
  return, is held by the query, and (b)'s reader is a new dependency. Rung 3.
  widens: none · relaxes: none
- **F2 — Is "the bar's first step" a step of the `bar` job or a leg of the bar?** Options: a step
  of the `bar` job, before `run-gates.sh`; a preflight run by `run-gates.sh` before its first leg.
  The clause's subject is remote CI's jobs, and `run-gates.sh` already resolves Python before any
  leg (`tools/run-gates/run-gates.sh:218`), so the second option adds nothing the resolver does not
  refuse. RESOLVED (agent, 2026-10-23, delegated): a step of the `bar` job. Rung 3.
  widens: none · relaxes: none
- **F3 — How is "applied to gov's own tree with its witness recorded" observed, when the lander
  is TOOL-dSafePassage-8's?** Options: this unit runs the walk on its own worktree and commits the
  receipt, which would make the branch and the lander write one file; this unit observes the
  receipt the lander writes into the prepared merge. RESOLVED (agent, 2026-10-23, delegated): the
  latter (AC7), because only a landing writes gov's receipt (TOOL-dSafePassage-8 §4). Rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-26`; no other section moved.

## 10. Reuse audit

The seam extended is the workflow's own step grammar and pinning rule: the GitHub-owned actions
pinned by sha with the tag beside them (`.github/workflows/remote-ci.yml:58`, `:118`), and the
`held-plan` step's write to `$GITHUB_OUTPUT` (`:269-270`), which is the shape the `floor` step
uses. The version comes from TOOL-dSafePassage-11's declaration. `reuse_lookup.py "set up a python
interpreter in a CI job pinned by commit sha"` ranked `build_commit`, `resolve_python` and
`resolve_pattern_sets`, and none of them is a CI seam. The map scans no `.github/` file, so the
workflow is outside its population, and its hits disagree with source on that point only. The
recall probe found the answers-fold review's M5 (`2026-10-18-review-PLAY-dClosedLoop-1-answers-fold-a.md:105`),
whose corrected fix this unit builds. It also found TOOL-dDerivedDocket-32's ledger, whose sha
reads by `git ls-remote --tags` this unit repeats.

Recall terms used: `python tools/memory-recall/query.py "how does remote CI set up the python interpreter and pin its actions by commit sha" --terms "remote-ci windows-latest setup-python pinned sha floor history-audit bar held held-plan resolver"`
