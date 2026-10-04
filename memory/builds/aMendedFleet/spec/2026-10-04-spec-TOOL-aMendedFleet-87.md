# TOOL-aMendedFleet-87 — a query joins changed paths to the gate legs that guard them

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 87

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A reviewer or an unattended builder holding a set of changed paths cannot ask which gate legs those
paths trip. The join exists, but only inside the spec-token checker's guards arm, which reads a
spec's files-touched list and drops broad guards; the bar's own guard evaluation is a `git diff`
per leg inside the runner. This unit exposes the same join as a query: given paths, print every leg
whose `guard` in `tools/gate-legs.json` each path trips, so the blast radius of a change is one
command and agrees with the spec gate by construction.

## 2. Scope (IN)

- **S1** — `tools/check-spec-tokens.py` gains `--legs-for <path>...`. It loads the manifest through
  the existing `derive_legs_path` and `resolve_prefix_token` reads, and joins each path to each
  leg's guards through the existing `check_guard_trips`, in a new `derive_tripped_legs(path, rows)`.
  The mode runs before the spec walk, so it needs no tracked spec and grades none. A single `-`
  argument reads the paths from stdin, one per line, so a range is
  `git diff --name-only` piped in. Observed by AC1 and AC2.
- **S2** — Output, one block per path: the path, then one line per tripped leg,
  `  <leg> <- <guard> [<chunk>/<subject>]`, with ` broad` appended where the guard is in the broad
  set `derive_guarded_legs` returns; a path tripping nothing prints `  no guarded leg`. One footer
  line, `legs-for: <u> of <t> legs carry no guard and run whatever changed`, counted from the
  manifest. The chunk and subject are printed as the manifest holds them; the query does not restate
  the runner's hold rule. Exit 0. Observed by AC1, AC3 and AC4.
- **S3** — A path no tracked file equals or sits under prints `(not tracked at HEAD)` after it and is
  still joined, because a range's deleted files are legitimate input. When EVERY path given is
  untracked the mode exits 2 naming them: a query over nothing but typos answers nothing.
  Observed by AC3.
- **S4** — A guard carrying `*`, `?` or `[` is printed as `UNEVALUATED <leg> <- <guard>` under every
  path, never joined, because `check_guard_trips` compares literal pathspecs and the runner's
  `git diff` would expand it. Observed by AC5.
- **S5** — The module docstring's usage block and the `spec-tokens` dossier's affordance list name
  `--legs-for`. Observed by AC6.

## 3. Non-goals (OUT)

- The reverse direction, leg to paths. A leg's guard list IS that answer, and `git ls-files` over it
  lists the files; nothing needs joining.
- Restating the runner's hold rule. Whether a held leg runs is `tools/run-gates/run-gates.sh`'s
  decision; the query prints the two fields it reads and lets the reader apply it.
- Changing the spec guards join, its broad floor or its waivers. The query shares the helpers and
  adds a mode; the default run is unchanged.
- Wiring the query into kickoff or the review harness. Unit 78 points kickoff at its context
  commands and owns that decision.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; `git diff --stat 7af5f564 HEAD` over every file below is empty at
`8312d315`.

- `tools/gate-legs.json` declares 124 legs, 66 of them with a `guard`, 151 guard entries in all,
  none carrying `*`, `?` or `[`. Figures PINNED as read on node a; AC1 re-derives the unguarded
  count.
- `check_guard_trips` in `tools/check-spec-tokens.py` matches the exact path or anything under the
  guard as a directory, which is git's literal pathspec reading and the one `changed` in
  `tools/run-gates/run-gates.sh` applies through `git diff --quiet BASE -- <pathspecs>`.
- `derive_guarded_legs` splits out guards carried by more than `BROAD_LEG_FLOOR` (5) legs. At
  writing that is six guards, `tools/lib/` the widest at 33 legs. The spec join excludes them; this
  query keeps and marks them, because a broad leg still runs.
- `main` walks tracked specs and refuses an empty spec set BEFORE it reads the manifest, so the new
  mode branches ahead of that walk.

### Inventory

| Name | Kind | Cell |
|---|---|---|
| `derive_tripped_legs` | function in `check-spec-tokens.py` | `py.function`; `--suggest` answered OK |
| `--legs-for` | CLI flag | none |

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `memory/map/features/spec-tokens.md`

### Alternatives rejected

- **A flag on the gate runner.** It owns the authoritative guard evaluation, but it answers against a
  BASE and a working tree, not for arbitrary paths, and a mode in a 2000-line bash runner puts the
  bar itself in the diff for a read-only query.
- **A mode of the map digest.** The digest already attributes a range to features, but the
  codebase-map kit would have to name the run-gates manifest by literal, which the charter's §12
  bans for a kit file.
- **A new standalone script.** A second reader of the manifest and a second copy of the trip rule;
  the spec join and the query could then disagree, which is the defect the reuse avoids.

## 5. Production-readiness checklist

- security — N/A — a read of a tracked manifest and `git ls-files`.
- perf / scale — one manifest read and one `git ls-files`; the join is 151 guards per path.
- error / empty / loading states — an all-untracked query exits 2; a path tripping nothing says so;
  a malformed manifest takes the existing parse refusal.
- observability — the footer states the unguarded count on every run, so a reader sees what the
  per-path lines cannot show.
- risks — a future glob guard would diverge from the runner; S4 prints it as unevaluated rather than
  guessing.
- testing — arms in the checker's suite at the close, declared in §7; AC1 to AC6 run directly.
- migration — N/A — a new mode; the default run is unchanged.
- user docs — S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py --legs-for tools/codebase-map/map_diff.py` runs
  after the unit's commit, it prints `codebase-map kit selftest`, `codebase-map gate coverage` and
  `codebase-map adopter e2e` each with its guard, and a footer whose unguarded count equals the
  number of rows in `tools/gate-legs.json` with no `guard` key.
  Red when: a guarded leg is missing, or the footer miscounts.
  figure: DERIVED from the manifest at observation; 58 of 124 at writing.
- **AC2** — When `git diff --name-only HEAD~1..HEAD` is piped into
  `python tools/check-spec-tokens.py --legs-for -` after the unit's commit, it prints one block per
  path the commit changed.
  Red when: stdin is not read, or a path is dropped.
- **AC3** — When `python tools/check-spec-tokens.py --legs-for nosuchpath` runs, it exits 2 naming
  the path; and when the same path is given after `tools/codebase-map/map_diff.py`, it exits 0 and
  marks only the second as not tracked.
  Red when: an all-untracked query exits 0 with `no guarded leg`.
- **AC4** — When `python tools/check-spec-tokens.py --legs-for tools/lib/resolve_kit_dir.py` runs, its
  lines under the `tools/lib/` guard each end in `broad`.
  Red when: the spec join's broad exclusion leaks into the query and those legs are absent.
- **AC5** — When a scratch clone under the TEMP root rewrites one leg's guard in its
  `tools/gate-legs.json` to `tools/codebase-map/*.py`, the AC1 command in it prints that leg after
  `UNEVALUATED`; and when it deletes that leg's `guard` key instead, the leg is absent and the footer
  count is one higher.
  Red when: a glob guard is joined as a literal, or the query reads anything but the live manifest.
- **AC6** — When `git grep -n -e "--legs-for" -- tools/check-spec-tokens.py
  memory/map/features/spec-tokens.md` runs after the unit's commit, it hits both files.
  Red when: the mode is undocumented in either place.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `recall floor` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · a scratch manifest with one exact-file guard, one directory guard and one glob guard, asserting the trip set, the UNEVALUATED line and the exit-2 refusal, staged red by joining the glob guard as a literal · none

## 8. Open questions

- **F1 — Where does the query live?**
  Options: a mode of the spec-token checker; a flag on the gate runner; a mode of the map digest; a
  new script. §4 rejects the last three.
  RESOLVED (agent, 2026-10-04, delegated): a mode of the spec-token checker. It reuses the trip rule
  the spec gate already grades with, so the two cannot disagree, and it touches no kit.
- **F2 — Does the query include broad guards, which the spec join excludes?**
  RESOLVED (agent, 2026-10-04, delegated): yes, marked. The spec join excludes them because naming
  them on every spec adds no information; a blast-radius query that omitted legs which will run
  would understate the radius.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#46], `check_guard_trips`,
  `derive_guarded_legs` and the manifest at base.

## 10. Reuse audit

The seams extended are `check_guard_trips`, `derive_guarded_legs`, `derive_legs_path` and
`resolve_prefix_token` in `tools/check-spec-tokens.py`, the guards join `TOOL-aBlindedTrial-8`
built. `python tools/codebase-map/reuse_lookup.py "which gate legs guard a changed path"` returned
`attribute_paths`, which joins paths to dossiers rather than legs, `resolve_gate_path`, which finds
the installed map gate file, and the run-gates affordance seam `LEGS_FILE`; none joins a path to a
leg. The probe printed `unscanned layers: .sh`, and the shell reader it cannot see is the runner's
`changed`, which evaluates guards against a BASE and is not callable for arbitrary paths. The recall
probe returned `TOOL-aBlindedTrial-8` and its spec naming `derive_guarded_legs`, and a prior-art
record pointing at the runner's serial guard pass as the diff-scoped precedent. Where the report and
the tree disagree: nowhere; the report names the join as missing and no query exists at base.

Recall terms used: `python tools/memory-recall/query.py "is there a query that answers which gate
legs a set of changed paths trips through their guards" --terms "gate-legs.json guard pathspec leg
blast-radius changed paths check_guard_trips derive_guarded_legs run-gates skip guarded NEAR"`
