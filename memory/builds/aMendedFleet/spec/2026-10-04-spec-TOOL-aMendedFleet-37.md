# TOOL-aMendedFleet-37 — dossier freshness is derived from git, and drift-audit reports the dossiers older than their paths

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 37

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A codebase-map dossier's prose is the one part of the map nothing grades: the `codebase-map coverage
+ freshness` leg byte-compares the generated artifacts and checks the claimed keys, and no check
reads whether the prose was re-read after the code it describes moved. The review sampled six
dossiers and found three carrying false prose, and measured that 23 of 84 feature touches refreshed
their dossier. This unit DERIVES each dossier's freshness from git, with no stamp anyone has to
remember: a dossier is older than its paths when a commit touching a path it claims is not an
ancestor of the dossier's own last commit. The codebase-map kit computes it, `map_diff.py` prints it
for the whole history or for one range, and drift-audit reports the count as a report-only signal
with a shrink-only pin.

## 2. Scope (IN)

- **S1** — A pure function in `tools/codebase-map/map_lib.py`, `measure_dossier_staleness`, takes a
  commit list (sha, parents, touched paths), the loaded map tree and the map root, and returns one
  record per feature dossier: its last commit, whether it is stale, how many commits touching its
  claimed paths are not ancestors of that last commit, and the newest such commit. A path is claimed
  by the attribution `attribute_paths` already performs, keyed attributors and dossier globs alike,
  so the map keeps ONE answer to "which feature owns this path". Every path under the map root is
  left out of the claimed side, because the map's own records are not the code a dossier describes,
  and refreshing one dossier must never stale another. Observed by AC1 and AC2.
- **S2** — A reader in `tools/codebase-map/map_diff.py`, `read_commit_paths`, runs ONE `git log` in
  topological order printing each commit's sha, its parents and its touched paths, over either the
  whole history at HEAD or one `<base>..<head>` range, and computes ancestry in process from the
  parents it printed. It asks `git rev-parse --is-shallow-repository` first and reports a shallow
  clone as unmeasurable rather than measuring an amputated history. Observed by AC2 and AC5.
- **S3** — `map_diff.py --stale-dossiers` prints the result, and `--json` prints it as one object.
  The range positional becomes optional in this mode only: with none the scope is every commit
  reachable from HEAD, and with `<base>..<head>` it is the commits in that range, which lists the
  dossiers a range touched and did not refresh. The existing `require_adopted_root` refusal runs
  before this mode as it does before the digest. Observed by AC1, AC3 and AC7.
- **S4** — A drift signal, `dossiers_older_than_their_paths`, built by `build_stale_dossiers` in
  `tools/drift-audit/drift_report.py` and appended to `SIGNALS`, reads `map_diff.py --stale-dossiers
  --json` through a reader `read_stale_dossiers` that resolves the kit with the existing
  `resolve_kit_dir`, the way `read_asks_projection` reaches the memory-tree generator. Its `value` is
  the stale count, `of` the dossiers measured, `gateable` false, and `live` the JSON's own liveness;
  its detail lists the stale dossiers most-behind first. Observed by AC4.
- **S5** — Three states, each distinct on the drift table:
  - NOT ASKED when the codebase-map kit does not resolve beside drift-audit, or when `map_diff.py`
    exits 2 because the root carries no `.codebase-map.conf`;
  - DEAD PROBE when the history is shallow, when no commit in the scope touches any dossier's claimed
    paths, or when `map_diff.py` exits otherwise or prints unparseable output, the note quoting why;
  - a value otherwise.
  Observed by AC5 and AC6.
- **S6** — The pin is shrink-only: `drift_signals.py` seeds `PINS` at the value measured when the
  unit is built, with the measurement written beside it, and adds a `RATCHETS` row so raising it
  needs an `<old> -> <new>` justification in place, the shape its report-only sibling
  `source_cited_ids_resolving_to_no_record` already takes. Observed by AC8.
- **S7** — The drift-audit README's signal table gains the row, and the codebase-map README's
  `map_diff.py` entry and the module docstring's usage block name `--stale-dossiers`. Observed by AC9.
- **S8** — `memory/map/generated/symbols.json` is regenerated for the new definitions, and the
  `codebase-map` dossier's prose is refreshed in the same commit, since this unit touches its paths.
  Observed by AC10.
- **S9** — Self-test arms: the codebase-map selftest stages a fixture history for S1 to S3 and
  extends its unadopted-root refusal arm with the new mode; the drift-audit selftest stages the
  three states of S5 over canned output, and its `CHECK_FLOOR` moves by the checks it adds.
  NOT OBSERVED by a criterion here: the suites run once at the close, and the arms are declared
  under `New arm:` in §7.

## 3. Non-goals (OUT)

- The close-time "touched, not refreshed" block in `tools/unattended/unattended.sh`. §8 F1 splits it
  into a unit the run adds; S3's range mode is the reader that unit calls.
- Gating on the count. It is report-only by the report's own wording, and a pin set ahead of today's
  value would be a scheduled refusal on the unguarded `drift-audit records` leg.
- Excluding version-marker-only edits from the claimed side. §8 F2 measured it and it does not move
  the verdict.
- `FOUNDATION.md`. Its globs name shared substrate rather than one feature, so "the dossier was not
  re-read after its code moved" asks a different question there. A follow-up can add it.
- Stamping a `last-reviewed` date into dossiers. A stamp is the remembered thing this unit exists to
  replace.
- Bumping the codebase-map or drift-audit kit versions. Many units of this build move both kits, and
  the bump is owed once, after the last move, at the close.
- Refreshing the dossiers the new signal names. Draining the pin is follow-up work, one re-read each.

### Edges

- **consumes-from** external — a full clone: in a shallow one the signal is DEAD PROBE by design.
- **hands-off** external — the close-time "touched, not refreshed" block, which F1 moves to a unit the
  run adds to this build; it reads S3's range mode and builds nothing of its own.
- **hands-off** external — the codebase-map and drift-audit kit version bumps, owed once at the close.

## 4. Design

### Data model

`map_diff.py --stale-dossiers --json` prints one object:

| Field | Meaning |
|---|---|
| `scope` | `HEAD`, or the `<base>..<head>` range as given |
| `of` | dossiers measured: in whole-history scope every feature dossier with a commit of its own; in range scope the dossiers whose claimed paths the range touched |
| `stale` | how many of those are stale |
| `live` | false when the clone is shallow, in either scope, or when no commit touched any claimed path in whole-history scope; an untouched range is a true empty answer |
| `note` | why `live` is false, or which dossiers were left out of `of` because no commit carries them yet |
| `dossiers` | one row per measured dossier: `feature`, `dossier`, `refreshed`, `stale`, `behind`, `newest` |

`refreshed` is the dossier's last commit at head. `behind` counts the commits in scope touching a
claimed path that are not ancestors of `refreshed`, and `newest` is the first of them in topological
order. In range scope a dossier last committed before the range has every in-range touch behind it,
since no commit in `<base>..<head>` is an ancestor of a commit outside it.

### The rule, and why ancestry rather than dates

Stale means `behind` > 0. A date comparison would call a dossier refreshed on a parallel branch fresh
against code it never saw, so the rule asks the graph. The log prints no paths for a merge commit by
default, which is the right reading: the commits a merge brings in are measured themselves, and a
change made only in a conflict resolution is not seen. That gap is stated in the README row.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `measure_dossier_staleness` | function, `map_lib.py` | Python function, verb `measure` |
| `read_commit_paths` | function, `map_diff.py` | Python function, verb `read` |
| `render_stale_dossiers` | function, `map_diff.py` | Python function, verb `render` |
| `--stale-dossiers` | `map_diff.py` flag | none; the lexicon declares no flag cell |
| `read_stale_dossiers` | function, `drift_report.py` | Python function, verb `read` |
| `build_stale_dossiers` | function, `drift_report.py` | Python function, verb `build` |
| `dossiers_older_than_their_paths` | signal name | none; a string key |

Each function name was asked of the lexicon with `--suggest <name> --as py.function`, and each
answered OK.

### Rollout

Unit 38 deletes the `--converge` mode from the same `map_diff.py` and runs after this unit. This unit
leaves that mode and its helpers untouched, so the two diffs meet only at the argument parser and the
module docstring. The first run of the signal on this tree reads roughly the probe's 26 of 27; that is
the measurement the pin is seeded from, not a defect.

### Files touched (estimate)

- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/map_diff.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`
- `memory/map/features/codebase-map.md`

### Alternatives rejected

- Computing the rule inside drift-audit. It would spell the map's glob attribution a second time,
  and the two spellings would drift; the kit that owns the dossiers owns the answer, and drift-audit
  reads it the way it already reads the memory-tree generator.
- One `git log` per dossier. Measured on node a, where a git spawn costs about 0.75 s, that is about
  20 s for 27 dossiers against 0.7 s for one log pass with in-process ancestry.
- A new entrypoint. `map_diff.py` already owns range attribution, and session kickoff's Step 1
  already calls it; a range question belongs there.

## 5. Production-readiness checklist

- security — read-only: a fixed argv to `git`, no shell string, no write anywhere.
- perf / scale — one `git log` and one shallow probe per run; the probe measured 0.7 s over 4125
  commits and 27 dossiers on node a, PINNED 2026-10-04. History grows linearly and so does the cost.
- error / empty / loading states — S5's three states; an uncommitted dossier is named in `note` and
  left out of `of` rather than read as stale or fresh.
- observability — the signal's detail is the worklist, most-behind first, each row naming the newest
  commit a re-reader should start from.
- risks — the count sits near its population on day one, so it reads as noise until dossiers are
  refreshed; the pin and its RATCHETS row make that a declared drain rather than a silent one. A
  version-marker sweep stales every kit's dossier, which F2 measured and accepted.
- testing — AC2 and AC3 stage the rule on a scratch clone; the selftest arms are S9's.
- migration — N/A — a new report row and a new mode; nothing stored changes.
- user docs — the two README rows of S7.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/map_diff.py --stale-dossiers --json` runs at the
  worktree root, it exits 0 with `live` true, `of` equal to the count `git ls-files
  memory/map/features` prints less any dossier named in `note`, and for the `codebase-map` row a
  `refreshed` sha equal to what `git log -1 --format=%H -- memory/map/features/codebase-map.md`
  prints.
  Red when: a dossier whose claimed paths moved after its last commit reads `stale` false, or `of`
  counts a dossier with no commit.
  figure: DERIVED at observation time; the probe read 26 stale of 27 at writing.
- **AC2** — When, in a scratch clone of the unit's tip under a short `%TEMP%` path, a commit touches
  only `memory/map/features/codebase-map.md`, then a commit appends a comment line to
  `tools/codebase-map/rank_harness.py`, then a commit touches only a file under `memory/map/generated`,
  `map_diff.py --stale-dossiers --json` after the first commit reads the `codebase-map` row `stale`
  false, after the second reads it `stale` true with `newest` equal to that commit's sha, and after the
  third still reads `behind` 1.
  Red when: a map-root-only commit stales the dossier, or a code commit after the refresh does not.
- **AC3** — When, in that clone, `python tools/codebase-map/map_diff.py <base>..HEAD --stale-dossiers`
  runs over a range holding the code commit and no dossier commit, it lists `codebase-map`; over a
  range holding the code commit followed by a commit refreshing the dossier, it lists nothing for
  `codebase-map`.
  Red when: a range that refreshed the dossier after its code change still lists it, or one that did
  not is silent.
- **AC4** — When `python tools/drift-audit/drift_report.py --json` runs at the worktree root, the
  `dossiers_older_than_their_paths` record has `gateable` false, `live` true, `value` equal to the
  `stale` field AC1 printed, and `tolerance` equal to its `PINS` entry in
  `tools/drift-audit/drift_signals.py`.
  Red when: the drift value and the map's own count disagree.
- **AC5** — When `git clone --depth 1` makes a shallow clone of the unit's tip, from a `file://` URL
  so the depth applies, under a short `%TEMP%` path and `python tools/codebase-map/map_diff.py --stale-dossiers --json` runs in it, `live` is false
  and `note` names the shallow history, and `python tools/drift-audit/drift_report.py` there prints
  `DEAD PROBE` on the signal's row.
  Red when: a shallow clone prints a count with `live` true.
- **AC6** — When `.codebase-map.conf` is deleted in a scratch clone and `python
  tools/drift-audit/drift_report.py --json` runs there, the record carries `not_asked` with a note
  naming the missing map, and its `value` is not read as a clean 0 on the human table.
  Red when: an unadopted map reports a count or a DEAD PROBE.
- **AC7** — When `CODEBASE_MAP_ROOT` names an empty directory and `python
  tools/codebase-map/map_diff.py --stale-dossiers` runs, it exits 2 with `refused` on stderr and
  prints nothing on stdout.
  Red when: an unadopted root prints an all-fresh answer at exit 0.
- **AC8** — When the new `PINS` entry in `tools/drift-audit/drift_signals.py` is raised by one in the
  working tree with no `<old> -> <new>` comment and `python tools/drift-audit/drift_report.py --check
  --base-ref HEAD` runs, it exits 1 naming `dossiers_older_than_their_paths`; restoring the line
  returns it to its prior exit.
  Red when: the pin can be raised silently.
- **AC9** — When `grep -c "dossiers_older_than_their_paths" tools/drift-audit/README.md` runs it
  reports 1, and `grep -c -e "--stale-dossiers" tools/codebase-map/README.md` reports at least 1.
  Red when: the engine ships a signal or a mode its README does not name.
- **AC10** — When `python tools/codebase-map/gen_map.py --check` runs after the unit's commit it exits
  0, and `python tools/codebase-map/map_diff.py --stale-dossiers` there does not list `codebase-map`.
  Red when: the regenerated artifact is stale, or the unit that ships the rule leaves its own dossier
  older than its paths.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `recall floor` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/codebase-map/selftest.py` · a fixture repository with one dossier, a refresh commit, a code commit and a map-root-only commit, read whole and by range, plus `--stale-dossiers` added to the unadopted-root refusal arm · none
New arm: `tools/drift-audit/selftest.py` · canned `map_diff.py` output for a value, a `live` false object, unparseable text and an exit 2 · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — Is the close-time "touched, not refreshed" list part of this mechanism?
  RESOLVED (agent, 2026-10-04, delegated): split — the close-time block in
  `tools/unattended/unattended.sh` moves to a new unit the run adds. It is a consumer in another kit
  with its own `.unattended.conf` declaration, since `MAP_CLI` names `reuse_lookup.py` and not
  `map_diff.py`, and node d's live build is rewriting that kit; units 49 and 66 are each one close
  block for the same reason. This unit ships the range mode that block calls.
- **FACT-QUESTION · F2** — Do version-marker-only edits need excluding from the claimed side?
  Probe: a read-only script over this tree's whole history at the worktree HEAD, applying the rule
  three ways — as written, without map-root paths, and also without commits whose every changed
  line on a claimed path matches a kit-version marker. Liveness: the marker filter moved per-dossier
  counts, `playbook-mode` from 62 commits behind to 10, so it can produce a different answer.
  RESOLVED (agent, 2026-10-04, delegated): no. The stale count read 26, 26 and 25 of 27, so the
  filter changes one verdict, and it needs every commit's patch: the patch log alone was 28 MB and
  6.5 s over the product paths, and the probe applying it took 68 s, against 0.7 s without it.
  The map-root exclusion is kept for correctness, S1's reason, not for the count.
- **F3** — Which entrypoint carries the rule?
  RESOLVED (agent, 2026-10-04, delegated): `map_diff.py --stale-dossiers`, per §4's rejected
  alternatives; it owns range attribution and one more mode costs no new file.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.

## 10. Reuse audit

The seam extended is `attribute_paths` in `tools/codebase-map/map_lib.py`, the map's one answer to
which feature owns a path, plus `load_map_tree` for the dossiers and their globs; on the drift side,
`SIGNALS`, `_build_not_asked`, `resolve_kit_dir` and the subprocess shape of `read_asks_projection`.
`python tools/codebase-map/reuse_lookup.py "compare a dossier's last commit with the newest commit on
the paths it claims"` ranked `attribute_paths`, `load_dossier_texts` and `parse_dossier` from the map
kit and name-stem neighbours elsewhere, and no function that compares commit ancestry for a dossier;
the scan names `.sh` as unscanned, and `git grep` over the shell layer finds no dossier freshness
reader either. The recall probe confirmed nothing grades prose freshness: two records state that the
`codebase-map coverage + freshness` leg tests keys and artifacts and none of them notices stale
prose. Where the report and the tree disagree: the report's 3 of 6 sampled dossiers carrying false
prose was not re-sampled; the derivation re-measured 26 of 27 dossiers older than their paths at
`580dc980`, which is consistent with its 23 of 84 touches refreshed.

Recall terms used: `python tools/memory-recall/query.py "is dossier prose freshness checked against
the commits on the paths a dossier claims" --terms "codebase-map dossier prose freshness stale
refresh on touch globs drift-audit signal shrink-only pin map_diff"`
