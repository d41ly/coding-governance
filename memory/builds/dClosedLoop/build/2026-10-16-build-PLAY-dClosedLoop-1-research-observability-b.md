# Research: the observability expansion, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 52's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-19-researcher.md`, which dispatch 51 ran
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`.

---

## 1. Verdict

Observability owns readings: values measured over accumulated state, node state or time. It also owns the two cadence steps that act on them, Maintain and the Loop Review. Core witnesses stay with the core. The test for which side a signal falls on: if a change under grading causes its value and committed history reproduces it, it is a core witness. Otherwise it is a reading.

The layer attaches as a journal reader, as command adapters (one per detector and per direct fix), and through `maintain.host`. It declares four extension points of its own: detectors, safe fixes, metric sources and events.

Without it the core still lands builds. The card's slots then say "not installed", nothing runs on a cadence, and the loop closes through requests alone (P6). The design I pick is **A** below. The bar's 7 gateable drift signals must move into core gates first, because today a core leg invokes this expansion's kit.

## 2. Today

| Part | What it does | Measured use | file:line |
|---|---|---|---|
| drift-audit | 27 signals with liveness; `--check` reds only on gateable signals | 7 gateable, 20 report-only; 15 nonzero; 2 DEAD; 30.5 s wall (the docstring says "seconds") | `tools/drift-audit/drift_report.py:3518-3530`, `:35`; pins `drift_signals.py:243-356` |
| `drift-audit records` leg | the core bar runs `drift_report.py --check` | every bar | `tools/gate-legs.json:1034-1049` |
| drift history | `--check` appends 27 rows per reading, node-local | 838 rows, 31 readings, 2026-10-08 to 10-16 | `drift_report.py:3750-3822` |
| process census | SessionStart/PostToolUse hook runs `reap.py --sweep --dry-run` and forces `report` | conf says `reap-orphans`, but the hook never kills; 0 flagged of 25 scoped now | `procmon-hook.js:28-29,119,124`; `.process-monitor.conf` |
| health log | self-heal events in a 4-field TSV, capped at 500 | 7 lines; 16 producer call sites | `tools/lib/health_log.py:10-28`; `run-gates.sh:1747-5139`; `resume-tick.sh:348-405` |
| runlog journal | `v=1` key=value grammar, 3 producers | driver 1,964 / gates 79 / pushes 262 lines; "Nothing prunes the journals" | `tools/runlog/README.md:5-8,568` |
| runlog run record | tracked, closed-schema record of one run | 20 files, with a schema leg | `tools/runlog/record.py:763-766`; `gate-legs.json:987-991` |
| run-state `RUN.md` | unattended run state (Runtime/Flow) | 89 tracked | `git ls-files '*RUN.md'` |
| gate ledger | last state per leg, rewritten every run | 118 rows, all `ok`; not a history | `run-gates.sh:5214-5256` |
| gate-run dir | per-leg `.leg` rows, 5 runs kept | 6 entries | `run-gates.sh:2556-2589` |
| gate health | `runlog journal --by-leg` | 78 bars; 54 of 140 legs ever red, 86 never | `README.md:18-24` |
| branch-reconcile | verdicts for worktrees, branches and stashes; `--write` removes landed ones | 51 MERGED, 6 IN-PROGRESS, 5 UNMERGED-LIVE | `branch_reconcile.py:1198-1203` |
| card cells | `drift —` and `health —` read those files, never re-run | already render `skipped: <why>` | `manifest-check.sh:441-472,600-614` |
| dormancy | LIVE.md marks a build dormant after 21 days | 21 of 25 | `gen_build_index.py:1768-1798` |
| map freshness | coverage and freshness leg, plus a stale-dossier signal | 25 of 31, pin 26 | gate-legs `codebase-map coverage + freshness` |
| adopter currency | `census.py` classifies DRIFT blobs | run by hand | `tools/govkit/census.py:10,276` |
| outbox orders | govkit writes orders into the adopter's `.governance/outbox/` | gov holds none | `govkit.py:4330,5412` |
| stall recorder | StopFailure line per bound run | node-local | `stall-recorder.js:1-25` |
| CI nightly | held legs on a cron, read-only | `contents: read`; "blocks nothing" | `remote-ci.yml:11,33-38,124-127,273-276` |

**Records against the code:**
- **Stale dossiers.** gap-maint-06 says 28 of 31. Today it reads 25, under pin 26.
- **Dead CI probe.** The research's "`remote_ci_red_streak` cannot move" does not name a cause. Measured, `gh` is absent on this node (`gh: command not found`), and under `--check` the signal is not-asked (`drift_report.py:3381-3395`).
- **One grammar.** runlog says "Three producers", but the common dir holds six grammars: runlog, health.log, drift-history, gate-ledger, stall logs and gate-run.
- **Bug classes.** 122 in the research, 128 today.

Measuring commands, outputs abridged:
```
$ python tools/drift-audit/drift_report.py            # at ee2eee68
  shrink_only_lists_not_shrinking 3 5 over pin 0 · run_records_nonterminal_but_merged 10 98 over pin 2
  legs_retried_after_timeout 3 43 over pin 0 · discarded_work_landed DEAD PROBE for 27 readings
  remote_ci_red_streak DEAD PROBE · dossiers_older_than_their_paths 25 31 ok (pin 26)
$ python tools/runlog/runlog.py journal --producer gates --by-leg --legs tools/gate-legs.json
  rows 140 never-red 86 bars 78
$ cut -f3 .git/gate-ledger.tsv | sort | uniq -c        ->  118 ok
$ grep -n "Retention" tools/runlog/README.md            ->  568: Nothing prunes the journals
$ awk '...' .git/gotchas front matter keys              ->  name 128 description 128 kind 128 universal 88 decision 3
$ grep -liE '^#+ .*confirmed' reviews/*.md | wc -l      ->  57 of 530
$ git tag | wc -l                                       ->  3 (all archive/*; no release tag)
```

## 3. Attach points

| Attach point | Declared in | What the core does without the layer |
|---|---|---|
| journal readers | layer-runtime `[extend]` :746 | writes the journal; nothing reads it; retention per `runtime.journal` |
| command adapters (detectors, reap, prune, census) | `[extend]` :739 | none run on a cadence; reaping is the supervisor's own act-ceiling only |
| hook packs (session-start breach) | `[extend]` :742 | no breach event |
| host adapters, via `maintain.host` | `[schedule]` :690-706 | no cadence items scheduled |
| notification adapters (`maintain.on-breach=report`) | `[extend]` :745 | none |
| cadence lease keyed by period | `[schedule]` :702-705 | unused |
| card cells `drift —`, `health —` (optional slots) | `manifest-check.sh:492-498` | render `not installed: observability — no core fallback` |
| stage review item 7, "cost to the value ledger" | flow `[review]` :675 | slot renders not installed; cost stays in the review record |
| Plan's triage intake (asks, proposals) | flow `[maintain]` :580, `[review]` :681 | requests only (P6) |
| patch build at Design | flow :625-626 | opened by requests only |

**Needed, and declared by no section I was handed:**
1. A **reading source** point that integrations fill. `remote_ci_red_streak` needs a CI adapter, so this is an expansion depending on an expansion, and P28 names no point for it.
2. **Event producers** for `maintain.events`. `default-branch-red` has no live detector. `release-verify-failed` has no producer, since no release tag exists.
3. **A record-kind registration for expansions** in the memory contract. I did not read layer-memory, so whether this is declared is unverified.
4. **Flow's cadence-step point.** layer-flow says Maintain is "a cadence step of the observability expansion" (flow.md:723), but I was not handed its `[extend]`.

## 4. Candidates

| | A. Registered detectors, journal-read, period record (**pick**) | B. Committed reading store | C. Detectors bind in the bar | D. Remote-hosted Maintain |
|---|---|---|---|---|
| Mechanism | Each detector registers as a command adapter carrying scope, pin, owner, events and fix. Maintain reads repo-scope detectors in a clean checkout at the base sha, and node-scope ones per node. Readings go to the journal. One maintenance record per period, via `record` | every reading is written as a tracked record, and history is read from the trail | every signal over pin, or dead, reds a bar leg (research §5 B) | CI cron runs the detectors and files asks |
| Losing test | Loses if repo-scope readings at one sha are not reproducible, or if a record per period swamps the trail | Loses if readings are derivable ([memory]) or not a function of the sha | Loses if the offenders it would red are outside the change it grades | Loses if Maintain's detectors need node state, or CI cannot write |
| Result | **Survives, with a constraint.** Some readings vary, but only on dirty trees and node-scope signals, so repo-scope readings need a clean base checkout (`maintain.reading-tree`). Volume is ~30 commits a month against 1,598 memory-only, +1.9% | **Loses.** 14 of 108 repeated (head, base, signal) groups vary, so committed numbers would not reproduce. 24 of 27 signals are re-derivable from the sha. On one node it would have committed 837 rows in 9 days | **Loses.** It would red this branch on 3 over-pin signals with 15 offenders (5 registry files, 10 `RUN.md`, 1 node leg), and 0 of them are in the branch's diff. It also makes the core bar depend on an expansion (P28) | **Loses as the Maintain host.** 7 register entries are node-scope (census, worktrees, gate-run, health, stall, gates.log, fleet), and CI holds `contents: read`. It survives only as `cloud-routine` for repo-scope detectors |

Commands:
```
$ awk -F'\t' 'NR>1{k=$2"|"$4"|"$5; ...}' .git/drift-history.tsv
  VARIES 409b4f5d|5822c97e|shrink_only_lists_not_shrinking  2/5 3/5   ...
  head|base|signal groups read more than once: 108  varying: 14
$ python drift_report.py --json | (offenders of the 3 over-pin signals)
  memory/project/{curation-debt,unarmed-branches,trace-waiver}.txt regrown;
  10 memory/builds/*/RUN.md HELD/BUILDING; run-gates canary retried 4
$ git diff --name-only $(git merge-base HEAD origin/main) HEAD | cut -d/ -f1-3 | sort | uniq -c
  memory/builds/dClosedLoop 128, memory/gotchas 7, memory/map 6, ... (no offender path)
$ grep -nE "permissions|contents:" .github/workflows/remote-ci.yml   ->  37: permissions: 38: contents: read
```

**The line (Q1).**

| Core witness, from a committed or hook-written verdict | Observability reading |
|---|---|
| bar and verifier verdicts; the lander; leases, claims, act and return records; transitions in spec-header history | the 20 report-only drift signals; process census; reconcile verdicts; gate health and flakes from the journal; health and stall events; dormancy; map staleness; currency; outbox; review yield; cycle times; value ledger |
| the 7 gateable signals (`ledger_rows`, `non_terminal_specs`, `handkept`, `closed_specs`, `lexicon_verbs_unused`, `lexicon_ratified`, `cutoff_keys_armed`), all change-caused, moved into the owning core layer's gates | |

**The run record** stays at `memory/builds/<slug>/build/<date>-build-<uid>-runlog-<key>.md` (`record.py:766`). It becomes a kind that observability declares, written through `record`. `RUN.md` is run state, not this record: the brief's "run record" names two different things.

**`runtime.journal`** should select retention, not readers. Readers register themselves, and the core keeps nothing today (`README.md:568`; driver.log is 441 KB).

## 5. The contract, filled

| Field | Observability's entry |
|---|---|
| tag and definition | `layer.observability`: reads signals about the loop and the runtime, never typed, and acts on them through Maintain and the Loop Review, only through the flow |
| instruction units | Maintain's run rules (fixes only from the declared set; anything else filed); the admission rule (no detector without a pin and an owner); the Loop Review's proposal rule; the card cell texts |
| engine kits | drift-audit (report-only half); runlog (reader and run record); branch-reconcile (reading, plus a prune adapter); process-monitor's readings (reaping stays Runtime's); codebase-map's stale-dossier reader; govkit census (registered by distribution); a Maintain cadence program and a value-ledger generator (dCalibratedLens) |
| record kinds | detector registry entry (tracked data); maintenance record; Loop Review record; value ledger (generated view); run record. Drift history is a journal-reader store, not a record |
| extension points declared | **detectors** (instrument, scope, population, pin or baseline, direction, owner, events, fix, dead-after); **safe fixes** (name, then a direct adapter or a patch-build template); **metric sources**; **events** (name, producer, detector subset) |
| extension points used | journal readers, command adapters, hook packs, host adapters, notification adapters; Flow's Plan intake and patch entry; memory's record kinds; card slots |
| policies and gates | keys in section 6. Gates: an admission check (every detector pinned, owned and live); a maintenance-record schema leg; a fixes-in-set witness; the value-ledger derivation leg |

**Register entry, and the owner rule.** The owner is derived, never typed: it is the writer of the record kind or engine state that the detector's offenders are rows of, as the memory contract's `writer` field says. Node state (processes, worktrees) belongs to Runtime. A detector whose owner cannot be derived, or which has no pin, is refused at registration.

| # | Detector | Layer (owner by the rule) | Pin today | Owner today | A check reads it |
|---|---|---|---|---|---|
| 1 | lexicon_marginal_offense_rate | instruction | none | none | no |
| 2 | ledger_rows_contradicting_git | memory | none (empty by declaration) | none | yes (gateable) |
| 3 | non_terminal_specs_cited_by_product_source | flow | baseline set | none | yes |
| 4 | shrink_only_lists_not_shrinking | memory | 0* | none | no |
| 5 | handkept_inventories_disagreeing_with_source | instruction | 0 | none | yes |
| 6 | dangling_pointers_in_own_ledger | memory | none | none | no |
| 7 | closed_specs_with_no_product_commit | flow | baseline set | none | yes |
| 8 | lexicon_verbs_declared_but_unused | instruction | 0 | none | yes |
| 9 | lexicon_ratified_older_than_language_surface | instruction | 0 | none | yes |
| 10 | live_backlog_rows_per_shard | flow (Plan) | none | none | no |
| 11, 13, 14, 19 | asks_disposed_overrides, backlog_asks_contested, backlog_evidence_sha, backlog_stragglers | flow (Plan) | 0* | none | no |
| 12 | readme_mechanism_drift | memory | 4 | none | no |
| 15 | backlog_asks_unlabelled | flow (Plan) | 447 | none | no |
| 16 | open_asks_cited_by_product_source | flow (Plan) | none | none | no |
| 17 | cutoff_keys_armed | instruction (policy) | 34 | none | yes |
| 18 | source_cited_ids_resolving_to_no_record | memory | 2 | none | no |
| 20 | run_records_nonterminal_but_merged | runtime | 2 | none | no |
| 21 | aborted_work_landed | runtime | 0 | none | no |
| 22 | discarded_work_landed | runtime | none; DEAD for 27 readings | none | no |
| 23 | legs_retried_after_timeout (node) | flow (Test) | 0* | none | no |
| 24 | fleet_over_budget (node) | memory | 0* | none | no |
| 25 | remote_ci_red_streak | flow (Test), via integrations | 0*; DEAD | none | no |
| 26 | dossiers_older_than_their_paths | memory (map) | 26 | none | no |
| 27 | live_builds_without_activity | flow (Plan) | none | none | no |
| 28 | process census (node) | runtime | age ceiling 14400 s | none (reap is manual) | no |
| 29 | branch and worktree reconcile (node) | runtime | none | none (`/cleanup`) | no |
| 30 | gate health, from gates.log (node) | flow (Test) | none | none | no |
| 31 | leg ceilings | flow (Test) | ceiling-evidence | run-gates | yes (leg) |
| 32 | map coverage and freshness | memory (map) | baseline.toml | codebase-map | yes (leg) |
| 33 | recall floor | memory (recall) | floor | memory-recall | yes (leg) |
| 34 | LIVE.md dormancy | flow (Plan) | 21 days | none | no |
| 35 | health log events (node) | runtime | none | none | card only |
| 36 | stall log (node) | runtime | none | none | `--liveness` only |
| 37 | adopter currency | distribution | none | none | no |
| 38 | outbox orders (in the adopter) | distribution | none | none | govkit check |
| 39 | session wiring | runtime | none | check-wiring (auto-wires) | wiring legs |
| 40 | memory hygiene on the default branch | memory | n/a | none: no event reads it | no |

`0*` is the default tolerance, not a declared PINS row. Five signals have no pin (1, 6, 10, 16, 27), and no signal carries an owner field (`grep owner drift_report.py drift_signals.py` finds only a comment).

## 6. Items and policies

**Maintain** (`maintain.*`):

| Tag | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `maintain.lease` | executor | takes the cadence lease for (cadence or event key, period) | lease via `record` | held elsewhere: skip; taken: `read` |
| `maintain.read` | command, one per detector | repo scope: clean detached checkout at the base sha; node scope: this node | `ev=reading` journal lines (detector, sha, value, of, key_hash) | dead past `maintain.dead-after`: `file`; over pin: `file` or `patch`; ok: nothing |
| `maintain.direct` | command (reap, prune-landed) | `reap.py --sweep`; `branch_reconcile --write` on MERGED only | health.log `tree-killed`; next verdict shows the set gone | survivor: `file` |
| `maintain.patch` | executor | opens a patch build at Design per fix in `maintain.fixes` that changes tracked content | the patch intake cites (detector, key_hash) | `patch.ratify` |
| `maintain.file` | command (`record`, ask kind) | renders an ask from the keyed reading: SEV from the register, `seen ... run <instrument> --offenders`, `accept <detector> ≤ pin`, `verify` | an ask whose key is (detector, key_hash); an open ask with the same key gets a `seen` row, not a new ask | Plan triage, owner from the register |
| `maintain.levels` | command (the bar, held profile) | slow levels and held legs | a verdict record | red: `file`, owned by Test |
| `maintain.currency` | command (census, registered by distribution) | probes each adopter | reading | DRIFT: `file` |
| `maintain.release` | command | cuts the tag and notes when `release.cadence` is due | tag plus notes | a failed verify raises the event |
| `maintain.record` | command (`record`) | writes checked, fixed and filed | the maintenance record, which is the period witness | releases the lease |
| `maintain.event.<e>` | executor | carries only the detectors whose `events` name `e`; keyed by (e, sha) | as above | as above |

**Loop Review** (`review.loop.*`):

| Tag | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `review.loop.lease` | executor | takes the period lease | lease | |
| `review.loop.gather` | command | reads the metric sources (below) | metric set in the record | a missing source renders searched-none |
| `review.loop.price` | command | regenerates the value ledger | ledger blob | |
| `review.loop.propose` | command | for rows with 0 catches in `review.loop.window-days`, proposes retire or merge; re-derives caps | proposals | |
| `review.loop.file` | command (`record`) | files each proposal into Plan triage with its ledger row | an ask | `review.loop.retire`: owner breakpoint, or demote first |
| `review.loop.record` | command | writes the Loop Review record | record | |

**Metric sources**, and their state today:

| Metric | Source | State today |
|---|---|---|
| cycle times | spec-header history in git | 1,544 specs; derivable |
| review yield | review records | parseable in 57 of 530 |
| catches | verdict records | none committed: the gate ledger holds `ok` only, gate-run keeps 5 runs, gates.log is node-local with no attribution |
| cost | ceiling-evidence | tracked, 147 lines |
| flakes | the journal `retried` status, `legs_retried` | available |
| bypasses | none | 0 journal lines |
| records overhead | git log | derivable |
| surface | gate-legs (140), gotchas (128), registries | derivable |

**Value ledger.** Home: the library, as a generated view (exact path owed to the memory contract). One row per governed item:

| Field | Meaning |
|---|---|
| kind | leg, rule, bug class, detector or lens |
| id | |
| since | sha |
| cost | seconds or tokens, and the runs counted |
| catches | own, attributed |
| false reds | |
| last_catch | |
| window | |
| state | |

**Keys:**

| Key | Allowed | Default | Why |
|---|---|---|---|
| `runtime.journal` | days, or `all` | 60 (≥ `review.loop.window-days`) | nothing prunes today (`README.md:568`) |
| `observability.run-record` | per-run, on-anomaly, none | per-run | today's behaviour; on-anomaly answers gap-maint-04 |
| `maintain.reading-tree` | clean-base, worktree | clean-base | 14 of 108 readings varied |
| `maintain.detector-admission` | refuse-unowned, report-unowned | refuse-unowned | 0 of 27 signals are owned |
| `maintain.dead-after` | readings | 10 | the existing "limit 10" in drift-report's header |
| `review.loop.catch-source` | verdict-records, node-journal | verdict-records | node-local catches are invisible to other nodes |

## 7. Gaps

| Gap | How the pick closes it |
|---|---|
| gap-maint-01 | cadence items under the period lease, hosted by `maintain.host` |
| gap-maint-02 | admission requires a pin and a derived owner; dead probes filed after 10 readings |
| gap-maint-05 | the `close finished run records` fix becomes patch builds |
| gap-maint-06 | `regenerate stale` becomes patch builds |
| gap-maint-07 | reaping becomes `maintain.direct`; ratchet and timeout readings are filed |
| gap-maint-08 | pins and owners for the offense-rate and dangling-pointer signals |
| gap-maint-03 | partly: the Loop Review and value ledger are dCalibratedLens's, and blocked on `gap-obs-2` |

Not closed: gap-maint-04, which belongs to dConvergedCharter. The pick adds about 30 records a month to it.

**New gaps:**

| Id | Evidence |
|---|---|
| `gap-obs-1` | a core leg invokes the expansion kit (`gate-legs.json:1034-1049`), so the 7 gateable signals must move into core gates |
| `gap-obs-2` | no committed catch history (`run-gates.sh:5214-5256`, `:2556`); 0 catch fields on 128 bug classes; review yield parseable in 57 of 530 |
| `gap-obs-3` | six node-local grammars, and none of runlog's journals has a retention bound (`README.md:568`) |
| `gap-obs-4` | event producers are missing: `remote_ci_red_streak` is dead (`gh` absent, offline under `--check`), and no release tag exists |
| `gap-obs-5` | readings depend on the tree they are taken in: 14 of 108 groups vary |
| `gap-obs-6` | no declared point lets an expansion consume another expansion's adapter (the remote CI reading) |

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| The 7 gateable drift signals | move into the owning core layers' gates / declare drift-audit core | **Move.** They are change-caused witnesses, and a core leg calling an expansion breaks P28 |
| Period witness | a committed record every period / a pushed ref plus a record only when something was fixed or filed | **A committed record every period.** It is +1.9% on records, and one witness is visible on every node |
| Catch source for the value ledger | Test's verdict record carries per-leg reds with attribution / Maintain publishes the node journals | **Verdict records**, committed history (P2) |
| `runtime.journal` | retention in days / a reader selector | **Retention**, because readers already register |
| Unowned detectors | refuse / admit as report-only with a sunset | **Refuse.** 20 report-only signals with 0 owners are what gap-maint-02 measures |
| Expansion-on-expansion | declare a reading-source point that integrations fill / keep remote CI out of observability | **Declare the point**, since `default-branch-red` needs it |
