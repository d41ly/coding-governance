# TOOL-aMendedFleet-58 — gate yield per leg is reported from the gates journal

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 58

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The gate runner appends one line per bar to `<git-common-dir>/runlog/gates.log`, naming each leg
that went red, and nothing reads those lines per leg. So nobody can say which legs ever catch
anything: the review counted 41 of 61 always-run legs that never went red in 50 bars. This unit adds
a report mode to the journal verb, `runlog.py journal --producer gates --by-leg`, which prints one
row per leg with how many bars it reddened, and, given the leg manifest, also lists every leg that
never went red in the window and whether it runs on every bar. It reports; it removes no leg.

## 2. Scope (IN)

- **S1** — THE MODE. `--by-leg` on the `journal` verb in `tools/runlog/runlog.py`, legal only with
  `--producer gates`; with any other producer it exits 2 naming the refusal. It reads the journal
  through `read_journal`, as the verb already does, and prints on stdout one JSON object per leg,
  `{"leg", "red", "bars", "last_red", "in_manifest", "always_run"}`, ordered by `red` descending
  then name. Observed by AC1 and AC4.
- **S2** — THE WINDOW. `bars` is the number of journal lines whose `verdict` is `GREEN` or `RED`; a
  line reading `NONE` ran no leg and is counted on stderr apart. `red` is the number of those lines
  naming the leg in a `fail.<n>` field, and `last_red` is the `started` of the newest. stderr carries
  one line naming the window's first and last `started`, the bar count, the red-bar count, the
  NONE count and an `other` count of lines whose verdict is none of the three, which are never read
  as bars. A window of zero bars prints no rows. Observed by AC1.
- **S3** — THE CAP AND THE LIVENESS. The writer caps named failures at twenty and counts the rest
  into `fail_more`; the mode sums `fail_more` into an `unattributed` count on stderr. A line whose
  `failed` differs from its named failures plus `fail_more` is counted as `mismatched` on stderr and
  still read, because a mismatch is the writer disagreeing with itself, which a yield figure must not
  hide. Observed by AC3.
- **S4** — THE POPULATION. `--legs <manifest>` names a gate-leg manifest by path, read as JSON.
  Every leg it names prints, `red` 0 included; a leg named in the journal and absent from it prints
  with `in_manifest` false. `always_run` is true for a leg with no guard whose `subject` is not `kit`
  and whose `chunk` is not `selftests`, the runner's own held rule, and null without `--legs`, as
  `in_manifest` is; `--legs` without `--by-leg` exits 2.
  Without `--legs` only legs that went red print, and stderr says never-red legs are not listed
  because no population was given. Observed by AC1 and AC2.
- **S5** — `build_leg_yield` in `tools/runlog/runlog.py` holds S2 to S4 over parsed lines and an
  optional manifest list, so the arms call it without a journal on disk. Observed through AC1.
- **S6** — The kit README's command-line section and the runlog Skill's source template name the
  mode, and `.claude/skills/runlog/SKILL.md` is re-rendered by
  `bash tools/runlog/adopt-runlog.sh --scaffold`.
  Observed by AC5.
- **S7** — Self-test arms in `tools/runlog/selftest.py` over a fixture journal: a capped line, a
  mismatched line, a `NONE` line, and a manifest holding a leg the journal never names. NOT OBSERVED
  by a criterion here: the suite runs once at the close, and the arms are declared under `New arm:`
  in §7.
- **S8** — `memory/map/generated/symbols.json` is regenerated for the new definition. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Removing, demoting or re-guarding any leg. The report is the input to that ruling, which is the
  owner's.
- Knowing which legs RAN on a bar. The journal names only failures, so `bars` is an upper bound on
  how often a guarded or held leg ran; stderr says so. The per-run `<i>.leg` rows hold the exact set
  for the handful of runs the runner keeps, and no unit of this build reads them for yield; unit 59
  reads the `<i>.retry.leg` rows and the verdicts beside them, not the `<i>.leg` rows.
- A drift signal or a gate over yield. Report-only, per the review's item.
- Reading another clone's journal: journals never leave their clone.
- Bumping the runlog kit version, owed once at the close.

### Edges

- **hands-off** external — the runlog kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `725b1449`, whose bytes under `tools/runlog/` and `tools/run-gates/` equal
base `7af5f564`'s.

- `python tools/runlog/runlog.py journal --producer gates` read 53 lines, 0 bad, all `ev` `once`,
  from 2026-09-21 to 2026-10-04 on node a: 30 GREEN, 20 RED, 3 NONE. PINNED, measured 2026-10-04.
- Every line's `failed` equals its named `fail.<n>` fields plus `fail_more`; no line was capped.
- Joined to `tools/gate-legs.json` at HEAD, 53 legs are always-run by the held rule and 35 of them
  never went red in the window. The review's 41 of 61 was measured at `ac65de998` against that
  tree's manifest. PINNED, measured 2026-10-04; S4 re-derives it.
- The writer is `tools/run-gates/run-gates.sh`, whose `RUNLOG_FAIL_CAP` is 20 and which spells a
  RETRIED leg by the status its retry ended on, so a leg that passed on its retry is not a red here.

### Inventory

- `build_leg_yield` — cell `py.function`; answered OK from
  `python tools/lexicon/lexicon.py --suggest build_leg_yield --as py.function`.
- `--by-leg` and `--legs` — flags of the `journal` verb; no naming cell grades flags.

### Files touched (estimate)

- `tools/runlog/runlog.py`
- `tools/runlog/selftest.py`
- `tools/runlog/README.md`
- `tools/runlog/SKILL.template.md`
- `.claude/skills/runlog/SKILL.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Read the gate ledger.** `<git-dir>/gate-ledger.tsv` keeps one row per leg, the last observation,
  not a series; it cannot count reds.
- **Derive the leg population from the manifest at each bar's `head`.** One `git show` per distinct
  manifest blob in the window, and still only an upper bound on what ran; the window's population is
  the manifest the caller names, which says so.
- **A new verb.** The mode is a view of one producer's lines, which is what `journal` already reads;
  a second verb would be a second reader of the same file.

## 5. Production-readiness checklist

- security — N/A: reads this clone's own journal and a file the caller names.
- perf / scale — one pass over the journal; one JSON read for `--legs`.
- error / empty / loading states — an absent journal prints the verb's existing absent line and
  exits 0; an empty one prints no rows and the zero window; an unreadable `--legs` exits 2 naming the
  path; a non-gates producer exits 2.
- observability — the window, `unattributed` and `mismatched` lines on stderr.
- risks — a guarded leg's `bars` overstates its runs; stated in §3 and on stderr.
- testing — AC1 to AC5 here; the arms in S7.
- migration — N/A: nothing stored changes, and the verb's output without the flag is unchanged.
- user docs — the README and Skill lines in S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/runlog/runlog.py journal --producer gates --by-leg --legs tools/gate-legs.json`
  runs at the worktree root on node a, stdout carries one row for every leg the manifest names, the
  `memory hygiene` row's `red` equals the number of journal lines naming it, counted by
  `python tools/runlog/runlog.py journal --producer gates` piped to `grep -c '"memory hygiene"'`, and
  stderr names the window's bar count.
  Red when: a leg's red count disagrees with the journal, or a manifest leg is missing from stdout.
  fixture: node a's common-dir journal, 53 lines at writing; a clone with none prints the absent line.
  figure: DERIVED at observation time; the journal grows with every bar.
- **AC2** — When the same command runs without `--legs`, no row carries `red` 0, and stderr carries
  the line saying never-red legs are not listed.
  Red when: a mode with no population prints a clean list that silently omits every never-red leg.
- **AC3** — When, in a scratch repository under a short `%TEMP%` path, the gates journal under its
  git dir's runlog directory holds one RED line whose `failed` is 3 with one `fail.1` and no `fail_more`, and one RED line with
  `fail_more` 2, and `python <worktree>/tools/runlog/runlog.py journal --producer gates --by-leg`
  runs there, stderr reads `mismatched=1` and `unattributed=2`.
  Red when: a writer disagreeing with itself, or a capped line, is folded into the counts unseen.
  cost: seconds; the scratch repository is the only thing written.
- **AC4** — When `python tools/runlog/runlog.py journal --producer driver --by-leg` runs, it exits 2
  and stderr names `--producer gates` as the only producer the mode reads.
  Red when: the mode reads another producer's lines as gate verdicts.
- **AC5** — When `grep -n "by-leg" tools/runlog/README.md .claude/skills/runlog/SKILL.md` runs, each
  file hits, and `bash tools/runlog/adopt-runlog.sh --check` exits 0.
  Red when: the mode ships undocumented, or the rendered Skill is stale.

## 7. Gates

`runlog selftest` · `runlog record schema` · `runlog skill wiring` · `run-gates run-log line` · `pre-push run-log line` · `check-wiring self-test` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/runlog/selftest.py` · a fixture journal with a capped line, a mismatched line, a NONE line and a never-named manifest leg, staged red by dropping `fail_more` from the sum · `ASSERTION_FLOOR` moves by the assertions the arms add

## 8. Open questions

- **F1** — Where does yield live: a runlog mode, a drift-audit signal, or a run-gates flag?
  The brief names a mode over the journal verb; a drift signal would gate-shape a report the review
  calls low-medium value, and a run-gates flag would make the writer its own reader.
  RESOLVED (agent, 2026-10-04, delegated): a mode of `runlog.py journal`, per S1.
- **F2** — The review's item says the mode shares one parser with unit 59's retry grouping. They
  read different files: this mode reads journal lines through `read_journal`; unit 59 reads
  `<i>.retry.leg` rows under every git dir, inside the drift-audit kit, which may not import a
  sibling kit's module.
  RESOLVED (agent, 2026-10-04, delegated): no shared module; the two key their rows by the leg name
  the manifest spells, which is the only thing their inputs share. Unit 59's spec records the same.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the report's roadmap item 6 ([B#24]) and a tally of node
  a's gates journal against the manifest at base.
- rev-2 · 2026-10-04 · §3 · M2 cross-read: §3 called the per-run `<i>.leg` rows unit 59's
  population, but `TOOL-aMendedFleet-59` S2 reads only the verdicts and the `<i>.retry.leg` rows.
- rev-3 · 2026-10-05 · S2, S4 · built: S2 gains the `other` verdict count and the zero-bar
  window's empty row set, S4 the null `in_manifest` without `--legs` and the refusal of `--legs`
  alone, each a case the rev-2 text left unstated.

## 10. Reuse audit

The seams extended are `cmd_journal` in `tools/runlog/runlog.py`, which already resolves the journal
root and reads the producer file, and `read_journal` and `PRODUCER_FILES` in
`tools/runlog/runlog_lib.py`, reused unchanged. `python tools/codebase-map/reuse_lookup.py "count how
often each gate leg went red across recorded merge bar runs"` returned `build_run_model` and the
record helpers in `tools/runlog/model.py` and `tools/runlog/record.py`, which join one run's
sources and count nothing per leg, and `build_nonterminal_merged_runs` in drift-audit, which reads
run records rather than bars; no existing seam counts reds per leg, so the count sits beside the
verb that reads the lines. The scan names `.sh` as unscanned, and the one shell file involved,
`tools/run-gates/run-gates.sh`, is read for its writer's field contract and not edited. Recall
returned `TOOL-aProbedUnit-8`, the ruling that no leg runs inside a pass, which every criterion here
follows, and `TOOL-aScannedThrottle-6` on leg dilation, which says per-leg wall clock is not this
report's to state. Where the report and the tree disagree: 41 of 61 always-run legs never red at
`ac65de998`; 35 of 53 at writing, against today's manifest and a journal of 50 bars.

Recall terms used: `python tools/memory-recall/query.py "which gate legs never go red and how is
gate yield measured from the gates journal" --terms "gates.log runlog journal producer gates
fail_more leg yield never-red merge bar verdict RED"`
