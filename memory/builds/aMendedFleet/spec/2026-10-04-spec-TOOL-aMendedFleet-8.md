# TOOL-aMendedFleet-8 — drift-audit reports `remote_ci_red_streak`

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

Remote CI has failed every run since 2026-09-29 and no record or report in this repo says so: the
drift report, which exists to say when the repo's record of itself stops matching reality, reads only
the local clone. This unit adds one report-only drift signal, `remote_ci_red_streak`, the number of
consecutive failed runs of the remote CI workflow on the default branch, newest first. A probe that
cannot reach the remote prints DEAD PROBE, never a reassuring 0.

## 2. Scope (IN)

- **S1** — A reader runs `gh run list --workflow <file> --branch <default> --limit <n> --json
  databaseId,status,conclusion,event,createdAt,headSha` in the repo root with a bounded timeout, and
  returns the parsed rows or the reason it could not. It is named under the lexicon's `read` verb.
  Observed by AC1 and AC3.
- **S2** — A pure function measures the streak over those rows, newest first, over COMPLETED runs
  only. `failure`, `timed_out` and `startup_failure` extend the streak; `success` ends it;
  `cancelled`, `skipped`, `neutral`, `stale` and `action_required` carry no verdict and are passed
  over and listed. It returns the streak, the number of verdict-bearing runs examined, whether the
  window was exhausted while still red, and the per-event streaks for `push` and `schedule`, which are
  different jobs in this workflow. It is named under the lexicon's `measure` verb. Observed by AC2.
- **S3** — The signal record, built beside its siblings and appended to `SIGNALS`, is report-only:
  `gateable` is false and the project layer declares no pin, so a streak above 0 prints
  `over pin 0 (report only)`. `of` is the verdict-bearing runs examined. `live` is DERIVED: true only
  when the reader returned rows and at least one carries a verdict. Its detail names the newest red
  run id, the newest green run id or `none in window`, the per-event streaks, and the passed-over
  runs. Observed by AC1 and AC3.
- **S4** — Three states, each distinct on the table:
  - NOT ASKED when the project layer declares no workflow, so an adopter with no remote CI reads
    neither a clean 0 nor a dead probe;
  - NOT ASKED under `--check` and `--offenders`, so the merge bar's `drift-audit records` leg never
    makes a network call for a number it does not grade;
  - DEAD PROBE when `gh` is absent, exits non-zero, times out, prints unparseable output, or returns
    no verdict-bearing run, the note naming which and quoting the first stderr line.
  Observed by AC3 and AC4.
- **S5** — The not-asked status line renders the record's own note when it carries one, and the
  existing generic sentence otherwise, so the `--check` skip does not print "this repo does not adopt
  what the signal reads" about a repo that does. No reader of that sentence exists; `git grep` finds
  only its definition. Observed by AC4.
- **S6** — The project layer gains `REMOTE_CI_WORKFLOW`: this repo's `drift_signals.py` declares
  `remote-ci.yml`, and the shipped template declares it blank with a comment saying blank is NOT
  ASKED. The engine reads it with the getattr-and-fallback its sibling optional keys use. Observed by
  AC1 and AC4.
- **S7** — The kit README's signal table gains the row, and its project-layer row names the new key.
  Observed by AC5.
- **S8** — The kit selftest gains one arm staging the pure function over canned rows and the reader's
  DEAD state, and the selftest's check floor moves by the checks it adds. NOT OBSERVED by a criterion
  here: the suite runs once at the close, and the arm is declared under `New arm:` in §7.
- **S9** — `memory/map/generated/symbols.json` is regenerated for the new definitions. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the legs that read it.

## 3. Non-goals (OUT)

- Gating on the streak. It is report-only by the owner's report; a pin set ahead of today's value
  is a scheduled refusal on the unguarded `drift-audit records` leg, the reason its report-only
  siblings give.
- Fixing the reds, which units 4, 5, 6 and the causes unit 7 adds do.
- Showing the streak on the orientation card or at the close. Units 76 and 49 read the history
  `TOOL-aMendedFleet-48` writes, and that history records `--check` runs only, where S4 makes this
  signal NOT ASKED, so neither carries the streak; a reader runs the report without `--check`.
- A second network client. `gh` is the one the brief names and the one node a is authenticated with.
- Bumping the drift-audit kit version in this unit. Many units of this build move the kit, and the
  bump is owed once, after the last move, at the close; `govkit epoch` grades it there.

### Edges

- **consumes-from** external — an authenticated `gh` on the host that runs the report, and network
  access to GitHub. Without either the signal is DEAD PROBE by design.
- **hands-off** external — the drift-audit kit version bump, owed once by the build's close.

## 4. Design

### Data model

The record is the shape every sibling returns: `signal`, `value`, `of`, `tolerance`, `gateable`,
`live`, `detail`, plus `not_asked` where S4 applies. `detail` is a list whose first entry is a
summary dict and whose remaining entries are the passed-over runs, so `--json` stays parseable by
the same consumers.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_remote_ci_runs` | function | Python function, verb `read` |
| `measure_red_streak` | function | Python function, verb `measure` |
| `build_remote_ci_red_streak` | function | Python function, verb `build` |
| `REMOTE_CI_WORKFLOW` | project-layer constant | Python constant |
| `REMOTE_CI_RUN_LIMIT` | engine constant, 30 | Python constant |
| `REMOTE_CI_TIMEOUT_S` | engine constant, 20 | Python constant |
| `remote_ci_red_streak` | signal name | none; a string key |

The default branch is the name `resolve_base_ref` already resolves, with its `refs/remotes/<remote>/`
prefix removed. The repository is the one `gh` infers from the clone's remote, so no owner/name is
declared anywhere.

### Why the `--check` skip

`main` computes every signal before it branches on mode. A `ctx` attribute set from
`args.check or args.offenders` is read by this signal alone and returns the NOT ASKED record without
spawning `gh`, so the bar's leg stays offline and its output stays deterministic.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/drift_signals.template.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- Anonymous `urllib` against the GitHub REST API. Stdlib-only and the repository is public, which
  `gh repo view --json visibility` confirmed, but it needs the owner/name parsed from the remote URL,
  a second HTTP client in a git-only kit, and an anonymous rate limit of 60 requests an hour shared
  by every process on the host. It loses on the brief, which names `gh`, and on the rate limit.
- Asking under `--check` too. One extra call on a leg with a 540 s ceiling is cheap, but it puts a
  network dependency inside the merge bar for a value no mode grades, which widens the bar's surface
  beyond what this Tier-1 unit priced.

## 5. Production-readiness checklist

- security — no token is read or printed by the kit; `gh` uses its own stored credential. The reader
  passes a fixed argv, never a shell string, and the workflow name comes from the tracked project
  layer.
- perf / scale — one `gh` call of about one to three seconds, bounded by `REMOTE_CI_TIMEOUT_S`, and
  skipped on the bar.
- error / empty / loading states — S4's three states; an in-progress newest run is passed over.
- observability — the signal is itself the observation; its detail names the run ids a reader opens.
- risks — a hosted run that is cancelled by a newer push is passed over, so it cannot fake a green.
  A window of 30 runs that is all red reports 30 with `capped` set, never a smaller figure.
- testing — AC2 stages the pure function directly; the selftest arm is S8's.
- migration — N/A — a new report row; nothing stored changes.
- user docs — the kit README row of S7.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs on node a with `gh`
  authenticated, the `remote_ci_red_streak` record has `live` true, `gateable` false and `of` above
  0, and its `value` equals the count of leading `failure` conclusions, after dropping runs with no
  verdict, in `gh run list --workflow remote-ci.yml --branch main --json status,conclusion` read in the
  same minute.
  Red when: the value disagrees with GitHub's own list, or the record is live with no run behind it.
  permission: needs network and an authenticated `gh`.
  figure: DERIVED at observation time; at writing, 15 of the last 15 runs failed.
- **AC2** — When `python -c "import sys; sys.path.insert(0, 'tools/drift-audit'); import drift_report
  as d; print(d.measure_red_streak([...]))"` runs over four canned lists, it reports 2 for
  failure, cancelled, failure, success; 0 for success, failure; the window length with the cap flag
  for an all-failure list; and no verdict for an all-cancelled list.
  Red when: a cancelled run ends or extends the streak, or a capped window reports less than its
  length.
- **AC3** — When `GH_HOST=nonexistent.invalid python tools/drift-audit/drift_report.py --json` runs,
  the record has `live` false and a note beginning `DEAD PROBE` that names the `gh` failure, and the
  human table prints `DEAD PROBE` on its row.
  Red when: an unreachable remote prints a value of 0 with a calm status.
- **AC4** — When `python tools/drift-audit/drift_report.py --check` runs with
  `GH_HOST=nonexistent.invalid` set, its table row for the signal reads `not asked` followed by the
  note naming the merge bar, its exit status is what it was before the change, and a staged break
  that deletes the `--check` branch of S4 turns the row DEAD PROBE.
  Red when: the bar's leg spawns `gh`, or the skip prints the generic not-adopted sentence.
- **AC5** — When `grep -c "remote_ci_red_streak" tools/drift-audit/README.md` runs, it reports 1, and
  `grep -c "REMOTE_CI_WORKFLOW" tools/drift-audit/README.md` reports at least 1.
  Red when: the engine lists a signal its README table does not.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `drift-audit wiring` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · a canned row list per streak rule and a reader pointed at an unreachable host · `CHECK_FLOOR` moves by the arm's checks

## 8. Open questions

- **F1** — Does the bar's `drift-audit records` leg ask the remote?
  RESOLVED (agent, 2026-10-04, delegated): no. It returns NOT ASKED under `--check` and
  `--offenders`, per S4; asking would widen the bar's surface, M3 veto 3, for a value no mode grades.
- **F2** — Which client reads the runs?
  RESOLVED (agent, 2026-10-04, delegated): `gh`, per §4's rejected alternative; the brief names it and
  the anonymous API's shared rate limit loses on measurement.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.
- rev-2 · 2026-10-04 · §3 · S9 · §4 · §7 · M2 cross-read: the §3 card-and-close line said units 76
  and 49 carry the streak, but `TOOL-aMendedFleet-48` writes `--check` readings only and S4 makes
  this signal NOT ASKED there; and the new definitions owe `symbols.json`, which units 57, 59 and 90
  regenerate and this spec omitted.

## 10. Reuse audit

The seam extended is the signal registry in `tools/drift-audit/drift_report.py`: `SIGNALS`, the
record shape every `build_` sibling returns, `_build_not_asked` for the NOT ASKED state, and the
project layer's getattr-and-fallback for optional keys, which `TRACE_GLOBS` and `TRACE_WAIVER` use.
`python tools/codebase-map/reuse_lookup.py "count consecutive failed remote CI workflow runs"`
returned name-stem neighbours only and no seam that reads a remote; `git grep` finds no `gh` call
anywhere under `tools/`, so the reader is new. The scan names `.sh` as an unscanned layer, so a shell
`gh` caller would be invisible to it, and the `git grep` covers that layer. Where the report and the
tree disagree: none for this point; the 15 of 15 red runs re-measured on 2026-10-04 match it.

Recall terms used: `python tools/memory-recall/query.py "is there a signal or check that reads remote
CI run results or GitHub Actions" --terms "remote-ci held job daily schedule red legs drift-audit
signal liveness DEAD PROBE report-only gh"`
