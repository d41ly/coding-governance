# TOOL-dQuietDisk-10 — `check-wiring.test.sh` takes its scratch repositories from the template cache

**Status:** SPECCED · rev-2 · 2026-11-20 · node d · Tier-2 · base 609cd40b · streams tooling · order 3 · ratified 2026-11-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md) | research | TOOL-dQuietDisk-8 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-wiring.test.sh` builds its seed repository itself and spends one `git config` process
per arm that wants its hooks wired. This unit takes both base repositories from TOOL-dQuietDisk-7's
template cache, built once per runner invocation and copied per arm, so the suite spends fewer git
processes for the same 255 arms with the same RED and GREEN results.

## 2. Scope (IN)

- **S1** — The seed `newrepo` copies from becomes the template `newrepo`, built by unit 7's bash
  face from the builder that is today's inline seed block (`tools/check-wiring.test.sh@609cd40b1:45-49`).
  `newrepo` copies that template's path with `cp -a` per call, as it copies the seed today
  (`tools/check-wiring.test.sh@609cd40b1:50-52`). The suite's own `NEWREPO_SEED` build and its
  `trap` go. Observed by AC1 and AC3.
- **S2** — A second template, `newrepo-wired`: the same builder followed by
  `git config core.hooksPath .githooks`. `newrepo wired` copies it. The ten sites that spell
  `newrepo; git config core.hooksPath .githooks` call `newrepo wired` instead (lines 404, 1343,
  1348, 1841, 1935, 1958, 2013, 2220, 2306 and 2366 at `609cd40b1`). The site at line 398, which
  writes `./.githooks`, and the site at line 2290, which writes an out-of-tree path, keep their own
  `git config`. Observed by AC1 and AC2.
- **S3** — Each template's key is unit 7's kit tree hash plus a discriminator naming this suite, the
  template name and the digest of its builder text, so an edit to either builder builds a new
  template. Observed by AC4.
- **S4** — At an install where the factory's bash face is not on disk, the suite still runs: it
  carries that face as unit 7 ships it to a copy-installed suite, and sources no file under gov's lib
  directory. Observed by AC5.
- **S5** — Under unit 7's switch at its other value, today's behaviour, every `newrepo` call builds
  its repository from the builder, as the suite did before `TOOL-aSparedSpawn-9`. That branch lives
  in the factory, not in this suite. Observed by AC2.
- **S6** — The arm set and every arm's verdict are unchanged. Observed by AC6.
- **S7** — The saving is counted: git processes and peak and residual temp entries, before and
  after. Observed by AC7.

## 3. Non-goals (OUT)

- `tools/check-wiring.sh` itself. Of the 3,786 git processes the analysis measured in one run, 1,679
  are `ls-files` (`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`,
  §2). Those come from the checker re-listing the tree on each of its 133 invocations
  (`chk`/`chke`, counted at `609cd40b1`), not from fixtures. TOOL-dQuietDisk-26 carries that one
  listing per invocation, at order 4, after this unit has moved the suite (F1).
- A read-only checkout shared by reading arms. The suite's header names an auto-fix mode
  (`tools/check-wiring.test.sh@609cd40b1:2`), so which arms write is a per-arm question. Every
  `newrepo` arm keeps its own copy.
- The single-use fixtures (lines 410, 1448-1478, 1718 and 2267 at `609cd40b1`). A template built
  once and used once costs what the inline build costs.
- The owned, swept scratch root for `newrepo`'s `mktemp -d`: TOOL-dQuietDisk-9.
- The factory itself, its switch and how its bash face ships: TOOL-dQuietDisk-7.
- `memory/gotchas/` records and gate-lint rows for the R1 rule: asks TOOL-dQuietDisk-20 and -23.

### Edges

- **consumes-from** `TOOL-dQuietDisk-7` — the bash face that builds a template once per runner invocation and hands back its path, its key composition admitting a caller's discriminator, its switch, and a form a copy-installed suite can carry inline. Without the inline form a shipped copy of this suite reds on arrival, the class `tools/govkit/entries/check-line-length.kit.toml@609cd40b1:29-35` records.
- **hands-off** `TOOL-dQuietDisk-19` — the suite's before and after readings, taken in a scratch `git clone --shared`.
- **hands-off** `TOOL-dQuietDisk-26` — the checker's per-invocation `ls-files`, `ls-tree` and `check-attr` reads, one each per invocation, and the two arms that pin them, added to the suite this unit moves.

## 4. Design

### The two templates

```bash
# builder for template `newrepo` (today's seed block, moved verbatim)
git init -q --template= -b main && mkdir .githooks \
  && printf '#!/bin/sh\nexit 0\n' > .githooks/pre-commit && chmod +x .githooks/pre-commit \
  && git add --chmod=+x .githooks/pre-commit && git commit -q -m init
# builder for template `newrepo-wired`: the same, then
git config core.hooksPath .githooks
```

`newrepo [wired]` asks the factory for the template's path, then `D=$(mktemp -d); cp -a
"$TPL/." "$D/"; cd "$D"`. `cleanup` is unchanged.

The environment the suite exports for identity and line endings
(`tools/check-wiring.test.sh@609cd40b1:34-35`) is exported before the factory runs a builder, so the
template's commit carries the same author and the same `core.autocrlf` reading as today's seed.

### Why a copy and not a clone per arm

Measured on 2026-11-20 in the scratchpad, on a seed built by today's block (PINNED, git for Windows
on node d):

| Per-arm form | git processes | entries created | State an arm can read |
|---|---|---|---|
| `cp -a` of the seed (today) | 0 | 28 | identical to the seed |
| `git clone --shared --template=` | 1 | 27 | adds `origin`, `refs/remotes/origin/*` and `branch.main` upstream |
| `git worktree add --detach` | 1 | 4, plus 10 in the template's `.git/worktrees` | detached `HEAD` |

A clone spends one more process for one fewer entry and adds remote state the remote and
`core.sshCommand` arms read. A worktree detaches `HEAD`. The copy face is kept.

### The saving, derived from the code at `609cd40b1`

| Source | Before | After |
|---|---|---|
| The seed build | 3 git processes per suite run | 3 per runner invocation per template, 6 for the two |
| `newrepo; git config core.hooksPath .githooks` | 1 per site per call, 10 static sites | 0 |
| `newrepo` copies | 0 git, 28 entries each | the same |

The bound: a run spends at least 7 fewer git processes than before, and more where a wired site sits
in a loop or a repeated function. Temp entries rise by at most the second template's 28. The figure
is DERIVED from these static counts; unit 19 measures the real one. The suite's larger cost, the
checker's own per-check listing, is TOOL-dQuietDisk-26's, so this bound counts fixtures only.

### Files touched (estimate)

`tools/check-wiring.test.sh`

### Alternatives rejected

- A per-arm `git clone --shared` (unit 7's default mutating face): rejected on the table above.
- A per-arm `git worktree add --detach`: rejected on the table above; also leaves one
  `.git/worktrees` entry per arm to prune.
- Folding the single-use inline fixtures onto templates: no saving, more code.

## 5. Production-readiness checklist

- security: N/A — no new write path, input or surface; templates live under the runner's owned scratch.
- perf / scale: at least 7 fewer git processes per run (§4); temp entries rise by at most 28.
- error / empty / loading states: a failed template build exits 2 as a failed seed build does today
  (`tools/check-wiring.test.sh@609cd40b1:49`).
- observability: none added; the suite's per-arm `ok`/`FAIL` lines are unchanged.
- risks: a template built from a tree a commit moved mid-run
  (`memory/gotchas/suite-invalidated-by-a-commit-under-it.md`); the key carries the builder digest
  and the factory's kit tree hash, so a new tree builds a new template.
- testing: AC1 to AC5 are probes of this unit's code; AC6 and AC7 run the suite and are the main loop's.
- migration: N/A — the suite carries no state between runs.
- user docs: N/A — a test-internal change; no `help/` page describes the suite's fixtures.

## 6. Acceptance criteria

- **AC1** — When the probe extracts `newrepo` from the edited suite and runs it twice in a scratch
  dir under `GIT_TRACE2_EVENT=<dir>`, once plain and once as `newrepo wired`, each call adds 0
  trace files after the template exists. `git -C "$D" config --local core.hooksPath` prints
  `.githooks` for the wired copy and nothing for the plain one.
  Red when: the wired copy carries no `core.hooksPath`, or a call spawns git.
- **AC2** — When the same probe builds one plain and one wired repository under unit 7's switch at
  each of its two values, `git ls-files -s`, `git for-each-ref`, `git config --local --list` and
  `git log --format=%T%x09%an%x09%ae` read byte-identical across the two values, and identical to a
  repository built by today's `newrepo; git config core.hooksPath .githooks`.
  Red when: a template-built copy differs from the per-call build in any of the four reads.
- **AC3** — When `grep -c 'NEWREPO_SEED' tools/check-wiring.test.sh` runs after the change, it
  prints 0, and `grep -c 'newrepo; git config core.hooksPath .githooks' tools/check-wiring.test.sh`
  prints 0.
  Red when: a seed build or a wired site survives beside the template.
- **AC4** — When the probe edits the `newrepo-wired` builder text in a scratch copy of the suite
  and asks the factory for the template, the factory builds a new template rather than returning the
  old path.
  Red when: the key omits the builder digest and the old template is reused.
- **AC5** — When `grep -nE '(^|[;&|] *)(\.|source) .*/lib/' tools/check-wiring.test.sh` runs, it
  prints nothing, and the factory's bash face appears in the suite as the inline form unit 7 ships.
  Red when: the suite sources a file under gov's lib directory, which no adopter holds.
- **AC6** — When the main loop runs `bash tools/lib/extract-arms.sh` over the suite at the build
  base and at the unit's commit, both inventories hold the same 255 labels with the same verdicts,
  and the suite's `PASS` total is the same.
  Red when: an arm is lost, added or changes verdict.
  permission: a role pass may not run a self-test suite (`tools/unattended/gate-guard.js` row D4);
  the main loop observes this at VERIFYING.
  cost: two suite runs, about 300 s each (the analysis, §2).
- **AC7** — When the main loop runs the suite in a scratch `git clone --shared` with
  `GIT_TRACE2_EVENT`, `TEMP`, `TMP` and `TMPDIR` pointed at scratch dirs, before and after, the git
  process count falls by at least 7 and the residual temp entries are 0 both times.
  Red when: the count does not fall, or an entry remains after the run.
  permission: as AC6.
  figure: the bound 7 is DERIVED from §4's static count at `609cd40b1`; the measured counts are
  TOOL-dQuietDisk-19's record.
  fixture: the adopter half is a scratch target that `python tools/govkit/govkit.py apply` installs
  the check-wiring kit into, where the main loop runs the shipped suite; `tools/govkit/fixtures/`
  holds no adopter tree with this kit today. `python tools/govkit/govkit.py check --target
  C:/projects/incms/main` and `--target C:/projects/nicocares/main`, run read-only from gov, read
  the same before and after.

## 7. Gates

`check-wiring self-test`

New arm: tools/check-wiring.test.sh · covers AC2 · a `newrepo wired` arm stages a template whose builder drops the `git config`, and the hook-mode arm reds · none

## 8. Open questions

- **F1** — Does this build add a unit for `tools/check-wiring.sh`'s per-invocation re-listing?
  The suite's measured cost is the subject: 1,679 `ls-files` and 421 `check-attr` of 3,786 git
  processes (the analysis, §2), against at least 7 this unit saves. The prompt names check-wiring
  as a biggest target (the prompt record's Fix 2).
  - (a) No unit; the main loop files an ask naming the listing. One follow-up stays open.
  - (b) ADD a unit: one `git ls-files -s` per invocation, read in-process by every check that
    re-lists today, with the checker's findings byte-identical on the suite's 255 arms. It closes the
    follow-up and is a separate mechanism, so it is its own unit (BUILD-METHOD M2).
  - Recommendation: (b). It is the most feature-rich option, and no veto applies: it adds no
    dependency, surface or carrier change, and widens no write surface.
  - RESOLVED (agent, 2026-11-20, delegated): (b). TOOL-dQuietDisk-26 now carries
    `check-wiring.sh`'s one listing at order 4, and this unit stays on the suite's fixtures at
    order 3.

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-20 · §3 · §4 · §8 · F1 resolved (b) under
  `2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task`: the listing non-goal and the bound point at
  TOOL-dQuietDisk-26, and the external hand-off becomes an edge to it.

## 10. Reuse audit

The seam is TOOL-dQuietDisk-7's template factory, which generalises `tools/lib/lib-selftest.sh`
`build_fixture` (`tools/lib/lib-selftest.sh@609cd40b1:77-88`) and folds in this suite's own
`NEWREPO_SEED` (TOOL-aSparedSpawn-9 S3), which already builds once and copies per call.
`python tools/codebase-map/reuse_lookup.py "build a scratch fixture repository once and clone it per test case"`
ranked `build_fixture` (`tools/lib/lib-selftest.sh`), `build_target` and `build_scratch_gov`
(`tools/govkit/fixture_target.py`) as seams; no candidate is a per-arm copy face, so this unit uses
the factory's template path and keeps the suite's copy. Chain owner: dWitnessedBar (Test, gate health
and budgets). Its branch changes 20 lines of this suite between `9e21ac760` and `609cd40b1`, an
inline `refuse_wrong_shell` block and one dependency list, and no fixture line, so this unit builds on
its tip copy and nothing overlaps.

Recall terms used: `python tools/memory-recall/query.py "how do the check-wiring self-test fixtures build their scratch repositories" --terms "newrepo NEWREPO_SEED template fixture seed copy clone shared worktree selftest check-wiring hooksPath"`
