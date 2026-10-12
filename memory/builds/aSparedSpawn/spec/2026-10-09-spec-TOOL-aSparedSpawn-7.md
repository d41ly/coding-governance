# TOOL-aSparedSpawn-7 — `--only` selectors for the unattended gate and the hygiene gate, each naming what ran

**Status:** CLOSED · rev-2 · 2026-10-12 · node a · Tier-2 · base 22efab65 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aSparedSpawn-7-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aSparedSpawn-7-acceptance-ledger.md) | journal | — |
| [2026-10-11-build-TOOL-aSparedSpawn-7-census.sh](../build/2026-10-11-build-TOOL-aSparedSpawn-7-census.sh) | journal | — |
| [2026-10-11-build-TOOL-aSparedSpawn-7-direct-checks.sh](../build/2026-10-11-build-TOOL-aSparedSpawn-7-direct-checks.sh) | journal | — |
| [2026-10-11-prompt-TOOL-aSparedSpawn-7-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aSparedSpawn-7-build-brief.md) | journal | — |
| [2026-10-12-review-TOOL-aSparedSpawn-1-15-closing-diff-round1.md](../reviews/2026-10-12-review-TOOL-aSparedSpawn-1-15-closing-diff-round1.md) | diff-review | TOOL-aSparedSpawn-1 TOOL-aSparedSpawn-2 TOOL-aSparedSpawn-3 TOOL-aSparedSpawn-4 TOOL-aSparedSpawn-5 TOOL-aSparedSpawn-6 TOOL-aSparedSpawn-8 TOOL-aSparedSpawn-9 TOOL-aSparedSpawn-10 TOOL-aSparedSpawn-11 TOOL-aSparedSpawn-12 TOOL-aSparedSpawn-13 TOOL-aSparedSpawn-14 TOOL-aSparedSpawn-15 |

<!-- /gen:spec-records -->

## 1. Goal

Let a self-test arm pay for the one check it asks about. `check-unattended.sh` gains `--only core`
and `--only <N>`, and `check-memory-hygiene.sh` gains `--only N[,M]`. Each prints a mandatory stdout
line naming the checks that ran and exits 2 when a requested check never ran, so a scoped arm can
never pass on silence. The research estimates about 4300-6500 s of pool work saved in the gate suite,
conditional on S1's measurement, and about 270 s quiet and 1500 s pool in the hygiene suite
(`research2-inprocess` §5; `research-memorytree-suites` lever 3; both static estimates).

## 2. Scope (IN)

- **S1** — The traced census, before code. One conforming-fixture run of `check-unattended.sh` under
  `PS4='+$EPOCHREALTIME $LINENO '`, its spawns and seconds attributed to check headers, giving `f`, the
  share of the 28 region plus the post-28 checks. Recorded with its instrument under the build folder.
  The conforming fixture is a clone of this repository at the pass commit, which the merge bar holds
  green. The instrument, `2026-10-11-build-TOOL-aSparedSpawn-7-census.sh`, lands in the pass; its one
  run is owed at VERIFYING, because a whole-leg run is barred inside a pass, and S2 does not land
  before `f` is recorded. The same run observes AC2 and AC5 on that clone. Observed by AC1.
- **S2** — `check-unattended.sh` parser. Inside the existing argv sentinel pair
  (`check-unattended.sh:141-149`), `--only` accepts `28` as today, `core`, and any `N` among the
  post-28 check headers, read from the running file by the `_o28_nums` awk (`:5372-5377`) and never
  typed. `--skip 28` is unchanged. Anything else exits 2: a value that is neither `core` nor digits
  inside the sentinel pair, and a number naming no post-28 header right after it. The comment line
  inside check 39 that opened `# ---- check 1 refuses` read as a check 1 header to that awk and is
  reworded, so `1` is not selectable and `--only 28` no longer announces a check 1 skip.
  Observed by AC2, AC4.
- **S3** — `check-unattended.sh` guards. `--only core` runs the prologue and the region guarded at
  `:325`, and skips the 28 region (`:4792`) and the post-28 branch, announcing each skip as `--only 28`
  does today (`:5360-5383`). `--only <N>` skips the core and 28 regions; each `# ---- check N` block
  after the 28 region opens with `check_selected N`, called once per header and never inside a loop.
  Producers stay unguarded: the conf import, the warm-ups, `core_of` and the per-record facts.
  The audit (every name assigned in the core region and read after the 28 region, and every name one
  post-28 block assigns and another reads) found four producers. Three move above the core guard:
  the driver-constant parse with `core_of` and the four core sets read beside it, `KITREL` with
  `PREFIX`, and the directive splitter that builds `core`, `corescope` and `coresec`. The fourth is
  check 48's list of the kit's shell files, which check 51 reads, so it runs ahead of check 48's
  guard. The warm-ups and the per-record facts stay inside the core region: no check after the 28
  region reads them. The post-28 branch opens on `if [ "$SCOPE" = only28 ] || [ "$SCOPE" = core ]`,
  and `--only core` announces its skips there in `--only 28`'s words. A number naming a core check
  and a post-28 header both (15) selects the post-28 block alone. Observed by AC2, AC3.
- **S4** — The liveness line, on stdout, under ANY `--only` including `28`:
  `check-unattended: --only <sel> ran checks <sorted ran set>; skipped <the rest of the header set>`.
  A requested check that never reached its guard exits 2 with the line
  `check N was requested and no guard for it ran, so its verdict would be silence`. The header's contract (`check-unattended.sh:12`) names the
  line as a FOURTH exit-0 exception, since three are named there already; an unscoped run prints
  nothing new. Observed by AC2, AC3, AC5.
- **S5** — `check-memory-hygiene.sh --only N[,M]`. Each check block opens with
  `check_selected <ids>`, where a delegated block names every id it grades at once, such as the
  13-16 classifier block (`check-memory-hygiene.sh:2486`) and check 25 inside check 12's block
  (`:2419`). The selectable set is derived from the running file's own `check_selected` calls. A
  requested id no call names exits 2 before any check runs; one that never reached its call exits 2
  after. `--only` with `--staged`, `--offenders` or a print mode exits 2. Producers stay unguarded:
  checks 1-5 remain the prefix `--print-index-set` returns after (`:812`). Checks 6, 7 and 8 share
  the `derive_waived` state the curation-debt stale-entry guard reads, so their three blocks and
  that guard each call `check_selected 6 7 8` and run as one unit. The grandfather stale-line guard
  builds its tracked set unguarded, grades its legacy half under `check_selected 5` and its debt
  half under `check_selected 6 7 8`. The index set and the view set stay producers.
  Observed by AC6, AC7.
- **S6** — The hygiene liveness line on stdout, `HYGIENE --only <sel> ran checks <sorted ran set>`,
  named in the header (`check-memory-hygiene.sh:20-21`) as a third exit-0 channel. Observed by AC6.
- **S7** — Projection parity arms in both suites, in PARTITION form: the set of lines the unscoped
  run prints equals the union of the lines the scoped runs print, over every selectable id, with the
  liveness lines set aside. One comparison reads every check's lines at once, so a scoped run that
  drops or adds a verdict reds it whichever check it was. The gate suite compares on its pristine
  fixture and on that fixture with one staged red in the 28 region and one after it; the hygiene
  suite compares on its main fixture, which is red across most checks. A red fixture per check is
  dropped: the partition grades every check's lines on every fixture it runs. Observed by AC8.
- **S8** — Scoped arms. Both suites gain a `run_scoped <sel>` helper that runs one selection and
  asserts its liveness line and the absence of the unreached-guard refusal; every scoped arm this
  unit adds calls it, and the existing `--only 28` arms assert the new line. The migration of the
  existing unscoped arms moves OUT of this unit: each migrated arm's equivalence is observable only
  by a suite run, which a pass may not make, and several hundred arms rewritten unobserved is the
  hand-patch shape the build's gotchas record. The main loop files it. Observed by AC9.

## 3. Non-goals (OUT)

- Per-check selection inside checks 1-27 of `check-unattended.sh` (the research's stage B). Those
  checks share state, and `TOOL-aGradedDoorway-7` rejected decomposing them. That rejection rested
  on user CPU: check bodies were 9.5 % of wall, with `user 12.1 s` against `sys 43.9 s`
  (`memory/builds/aGradedDoorway/build/2026-08-29-build-TOOL-aGradedDoorway-7-1-s3-cost-split.md:27-35`,
  rejection at `:58-61`). The same record counts on the order of 500 process creations per run
  (`:50-53`), and the research notes those spawns are issued from inside the check bodies
  (`memory/builds/aMeteredSweep/build/2026-10-08-build-TOOL-aMeteredSweep-1-research-govkit-unattended.md:332-335`).
  So the question is reopened, and S1's trace is what settles it; a later unit acts on it.
- Changing which checks the unscoped merge-bar run executes or prints.
- The fused hygiene delegate bundle and the re-entry removal (memorytree levers 4 and 8).
- The transition-audit suite's single-check runs.

### Edges

- **consumes-from** `TOOL-aSparedSpawn-6` — the driver restructured as `load_driver_conf` and
  `main`. Checks that read the driver's source (`core_of`, the check 26 sentinel, checks 39, 48 and 51)
  and check 30, which launches the driver per leg run, get projection parity fixtures written against
  that shape; landing first would build them against bytes the next unit moves. The arm-inventory
  comparison is that unit's procedure, reused.

## 4. Design

### The guard

```bash
# <ids…> -> 0 when any id is selected, and then EVERY id of the block is recorded as ran, because
# the block runs whole. Unscoped: always 0.
check_selected() { [ -z "$ONLY" ] && return 0; local i
  for i in "$@"; do case " $ONLY " in *" $i "*) RAN="$RAN $*"; return 0 ;; esac; done; return 1; }
```

So `--only 14` runs the 13-16 classifier block and its line names all four ids, which is true.

Each guarded block becomes `if check_selected 30; then … fi` around the statements that emit or
consume a verdict. Unscoped, the guard is one builtin test, so the merge-bar run's spawn count does
not move. After the last check, each requested id is looked up in `RAN`; a miss exits 2. Under
`check-unattended.sh`, `ONLY` holds `core`, `28` or one `N`; under `check-memory-hygiene.sh` it holds
the comma list split into words.

### Why the liveness line is mandatory

A negative assertion under `--only` passes vacuously when the check it negates never ran: the
charter's "a skip must announce itself". The line names what ran, `run_scoped` asserts it, and the
exit-2 refusal turns a guard that the selected path never reached into a red instead of a silence.
The guard is called at headers and never in loops, because a loop over an empty population would
never register its check.

### Dependencies to audit while guarding

- `check-unattended.sh`: a post-28 check that silently reads state computed by checks 1-27 gets an
  empty value under `--only N`. `set -u` catches an unbound read; S7's projection parity catches an
  initialised empty one.
- `check-memory-hygiene.sh`: check 6 computes `INDEX_SET` for the print mode and the delegates, so the
  computation stays unguarded and only check 6's verdict block is guarded. Check 23 reads staged
  state, and checks 12 and 25 share one selection.

### Migration

1. S1's trace, recorded.
2. The `check-unattended.sh` parser, guards and line (S2-S4), with its parity arms.
3. The hygiene selector and line (S5, S6), with its parity arms.
4. The scoped arms (S8). The migration of the existing arms, with its inventory comparison
   (`check-arms.py --report` rows with the line column dropped, the `--emit-floors` tokens, the sorted
   assertion multiset with the `--only` argument stripped, and each suite's PASS count), is the
   follow-on unit's procedure and is not run here.

`check-memory-hygiene.sh` is in `check-verdict-epoch.sh`'s scan set, so the memory-tree kit owes its
version bump in every carrier `check-kit-versions.sh` derives. The unattended kit bump is shared with
`TOOL-aSparedSpawn-6`: whichever lands last bumps once.

### Inventory

New identifiers: `check_selected` (verb `check`) and `run_scoped` (verb `run`); variables `ONLY` and
`RAN` in both gates. No new flag name: check 26 joins `--<name>` flags only (`read_argv_flags`,
`check-unattended.sh:171-176`), so new values of `--only` add no check-26 obligation.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh` — parser values, guards, the line, the contract header.
- `tools/unattended/check-unattended.test.sh` — parity arms, `run_scoped`, migrated arms.
- `tools/memory-tree/check-memory-hygiene.sh` — the selector, guards, the line, the header.
- `tools/memory-tree/check-memory-hygiene.test.sh` — parity arms, `run_scoped`, the new arms.
- `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-7-census.sh` — S1's instrument.

`memory/HYGIENE.md` and its template are NOT touched: the usage line lives in the gate's header,
which HYGIENE.md already names as the single enforcement, and the kit version carriers are bumped by
the main loop once after the last unit.

### Alternatives rejected

- **Splitting checks 1-27 now.** Rejected by `TOOL-aGradedDoorway-7` and not reopened until S1's
  trace measures the spawns inside those bodies.
- **An environment selector such as `HYGIENE_ONLY`.** A flag sits in the argv region check 26 joins;
  an environment variable leaks into nested runs and is invisible in a log.
- **Batching conf variants into one hygiene run.** Refuted in `aRatifiedRulings-3` §4: rc 0 over
  several keys names none of them on failure.
- **A typed list of selectable checks.** It goes quiet on the first check added after it; the set is
  derived from the running file, as `_o28_nums` already does.

## 5. Production-readiness checklist

- security: N/A — no new input beyond a closed set of argv values, each refused with exit 2 when unknown.
- perf / scale: estimated 4300-6500 s pool (gate suite, `f` unmeasured) and 270 s quiet / 1500 s pool (hygiene suite).
- error / empty / loading states: an unknown selector, an unreached guard or a forbidden flag combination exits 2.
- observability: the mandatory liveness line on stdout under every `--only`; skips keep their announcements.
- risks: a post-28 or delegated check reading state its guard skipped; a vacuous negative arm; the PASS count read wrong.
- testing: projection parity per selectable id on a conforming and a red fixture, plus staged unreached-guard breaks.
- migration: none for callers; the unscoped run is byte-identical, and two kit versions bump.
- user docs: the usage lines in both gates' headers and `memory/HYGIENE.md`; no `help/` surface exists.

## 6. Acceptance criteria

- **AC1** — When `check-unattended.sh` runs once on the conforming fixture under a `PS4` of
  `$EPOCHREALTIME` and `$LINENO`, its seconds and spawns per check header are recorded with the
  instrument under the build folder, giving `f`. Red when: S2 lands with no recorded `f`.
  figure: PINNED at the trace's date, node and sha.
- **AC2** — When `bash tools/unattended/check-unattended.sh --only core` runs on the conforming
  fixture, it exits 0 and stdout carries exactly one line opening
  `check-unattended: --only core ran checks`, naming every skipped post-28 check. Red when: the line is absent or a post-28 check runs.
- **AC3** — When `--only 30` runs with the `check_selected 30` call staged out of
  `tools/unattended/check-unattended.sh`, it exits 2 with the line
  `check 30 was requested and no guard for it ran`. Red when: it exits 0 or prints no refusal.
- **AC4** — When `--only 5` or `--only 99` is passed to `tools/unattended/check-unattended.sh`, it
  exits 2 before any check runs. Red when: either value starts a check.
- **AC5** — When `bash tools/unattended/check-unattended.sh` runs unscoped on the conforming fixture,
  it exits 0 with no output, as its header's contract says. Red when: the liveness line or any new
  line appears unscoped.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 12` runs on a clean fixture
  tree, it exits 0 and stdout carries `HYGIENE --only 12 ran checks 12 25`; with that block's
  `check_selected` staged out, it exits 2 naming check 12. Red when: the line is absent or the
  staged break exits 0.
- **AC7** — When `--only 12` is combined with `--staged` or `--offenders`, or names an id no
  `check_selected` call carries, `tools/memory-tree/check-memory-hygiene.sh` exits 2.
  Red when: any of those combinations runs a check.
- **AC8** — When the projection parity arms run, the set of lines the unscoped run prints equals the
  union of the lines the `--only` runs print over `core`, `28` and each post-28 `N`, on the gate
  suite's pristine fixture and on it with a staged 28-region red and a staged check 39 red, and over
  every hygiene selectable id on the hygiene suite's main fixture. Red when: a staged guard placed
  around a producer makes a scoped run drop or add a verdict and the arm stays green.
  permission: the two suites are held; the owner runs them on demand, and VERIFYING observes this.
- **AC9** — When the suites run, every `run_scoped` call asserts its liveness line and the absence
  of the unreached-guard refusal, and the existing `--only 28` arms assert the liveness line.
  Red when: a scoped arm reads no liveness line, or carries a negative on an unselected check.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `run-gates canary` · `run-gates evidence` · `foreign-prefix parity (every self-test at three prefixes)` · `install-prefix self-test` · `dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` · `kit-placeholders self-test` · `verdict-epoch self-test` · `memory-hygiene self-test` · `row-keyed merge driver replay` · `kit/dogfood doc parity` · `build-index selftest` · `corpus-ids selftest` · `gotchas selftest` · `row-grammar selftest` · `backlog migration selftest` · `check-arms selftest` · `transition-audit arms` · `straggler-guard arms` · `recall floor` · `recall floor arms` · `unattended kit gate` · `memory hygiene` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `verdict epoch (kit version dates the engine)`

New arm: tools/unattended/check-unattended.test.sh · covers AC2 AC3 AC4 AC8 · a staged-out check_selected call and an unknown selector · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC6 AC7 AC8 · a staged-out check_selected call and a forbidden flag pair · FLOOR_ASSERTIONS, raised by the added arms

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-12 · §2 §4 §6 S1 S2 S3 S4 S5 S7 S8 AC8 AC9 · the pass's reading of the code: S1's run is
  owed at VERIFYING on a clone of the tree, S2 refuses a non-numeric value in the sentinel and drops
  a comment line that read as a check 1 header, S3 names the four producers its audit found and the
  anchor `--only core` shares, S4's exception is the FOURTH, S5 makes 6, 7 and 8 one unit over their
  shared waiver state, S7 takes the partition form, S8 moves the migration of existing arms out, and
  the HYGIENE.md pair leaves the file list.

## 10. Reuse audit

The probe, `tools/codebase-map/reuse_lookup.py`, asked "scope a checker run to selected checks and
announce which ran", names no selector seam; its hits are name-stem neighbours such as `scope` in the driver suite
and `derive_scope` in process-monitor, neither of which gates a check. The seam extended is in-tree
and invisible to the probe because it is not a function: the `SCOPE` parser inside the argv sentinel
pair (`check-unattended.sh:140-149`) and the header-derived `_o28_nums` awk (`:5372-5377`).

Recall terms used: only-selector check-unattended check-memory-hygiene scope skip28 announce liveness aGradedDoorway cost-split spawns
