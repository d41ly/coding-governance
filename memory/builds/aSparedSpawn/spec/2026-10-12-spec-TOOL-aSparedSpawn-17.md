# TOOL-aSparedSpawn-17 — an executed red under a cached ok erases the entry and quarantines the leg

**Status:** OPEN · rev-1 · 2026-10-12 · node a · Tier-2 · base 8444f597 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-prompt-TOOL-aSparedSpawn-17-build-brief.md](../prompts/2026-10-12-prompt-TOOL-aSparedSpawn-17-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Close HIGH finding 3 (H1) of the round-1 closing review
(`memory/builds/aSparedSpawn/reviews/2026-10-12-review-TOOL-aSparedSpawn-1-15-closing-diff-round1.md`).
When the age bound forces a leg to execute, or any execution runs under a key whose cache entry
reads `ok`, a red result today leaves that `ok` in place with a fresh age allowance, so a retried
push of the same sha can land green on a leg that just went red there. After this unit every such
red erases the entry and quarantines the leg, as the sampled-disagreement branch already does.

## 2. Scope (IN)

Every site was re-read at f479ba42, whose `tools/run-gates/run-gates.sh` is unchanged at 8444f597;
line numbers are that tree's.

- **S1** — In `tools/run-gates/run-gates.sh`'s reuse path, a leg that executes while its key holds a
  cached `ok`, and whose effective result is red, erases that entry and is quarantined, as the
  sampled-disagreement branch at `:4562` does. Today only `*.sampled` legs reach that branch, so an
  age-forced execution (`:3097`-`:3102`) or any other execution under a cached key that reds leaves
  the stale `ok` in place. The branch's population widens to every executed leg whose effective rc
  is non-zero and whose key holds an `ok` entry. A sampled leg keeps its classifying re-run and its
  two lines. A leg that was not sampled takes the effective rc as its verdict, which is already its
  serial retry's where it had one, prints `cache disagreement · <leg> · <key>`, loses the entry and
  is quarantined against its row hash. Observed by AC1 and AC2.
- **S2** — The `$WORK/$i.aged` marker written at `:3100` stays written and gains a reader:
  `TOOL-aSparedSpawn-16` S17 prints a tail from it in `report_one`. This unit's widened
  branch does not need the marker, since its population already contains every aged execution.
  NOT OBSERVED by a criterion of this unit: the reader is observed by that unit's AC18.
- **S3** — Evidence-suite arms in `tools/run-gates/run-gates.evidence.test.sh` for the aged case and
  the plain-bar case, and `FLOOR_ASSERTIONS` rises by their executed assertions with a
  `RAISED <old> -> <new> by TOOL-aSparedSpawn-17` line, marked OWED in the ledger until the suite
  runs at VERIFYING. Observed by AC3.
- **S4** — `tools/run-gates/README.md`'s reuse section says an executed red against a cached `ok`
  erases the entry and quarantines the leg, whatever drew the execution. Observed by AC4.

## 3. Non-goals (OUT)

- The age counter's keying, finding 12, which is `TOOL-aSparedSpawn-16` S11. The arms here reach the
  age bound through whichever counter the tree holds when they are built.
- A tail on the leg's line for a sampled or aged execution, findings 14 and 22, which is
  `TOOL-aSparedSpawn-16` S17.
- Running any suite or the bar inside the build pass, and a kit version bump, which the main loop
  makes once after the build's last unit.

### Edges

- **hands-off** `TOOL-aSparedSpawn-16` — the reader of the `$WORK/$i.aged` marker, a tail that
  `report_one` prints on the leg's own line.

## 4. Design

The loop after `run_leg_retry` iterates `"$WORK"/*.sampled` today. It becomes one pass over every
leg index whose `$WORK/$i.rc` names an execution, skipping `reuse`, `ondemand`, `skip` and
`docskip` as the cache block does. For each, the effective rc is `$WORK/$i.retry.rc` where it exists,
else `$WORK/$i.rc`. A leg with a `.sampled` marker runs the existing branch unchanged. Any other leg
whose effective rc is non-zero, whose `INPUT_KEYS[$i]` is a measured key, and whose cache entry under
that key reads `ok` runs the branch's red-again arm: the `cache disagreement` line, the entry erased,
the quarantine file written. No extra run is spent on it, because its retry already gave a second
observation where one was due.

The loop spawns nothing per leg: every read is a builtin `read`. The one-leg and two-leg fork counts
in `memory/project/fork-ceilings.txt` therefore do not move, and the new code adds no site to
`memory/project/spawn-idiom-sites.txt`; the builder re-runs both of `TOOL-aSparedSpawn-16`'s
measuring commands, its AC2 and AC3, to confirm it.

### Inventory

No new function, variable family or file kind is minted. New arms reuse the evidence suite's
`ru_repo`, `ru_run` and `write_ru_legs` helpers, so the lexicon leg sees no new definition.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/README.md`

### Alternatives rejected

- **Read `.aged` in the existing loop and leave other executions alone.** A plain bar or a push-mode
  bar can execute a leg whose key holds an `ok` too, so an age-only reader leaves the same stale
  entry in place on those paths.
- **Re-run every non-sampled red once more to classify it.** The serial retry already re-ran a red
  leg, and a second classifying run doubles a red bar's tail for a label.
- **Delete the `.aged` write.** `TOOL-aSparedSpawn-16` S17 reads it to say on the leg's line why the
  leg executed, which the record cannot otherwise tell from an ordinary miss.

## 5. Production-readiness checklist

- security: closes the path by which a push could land green on a leg that just went red at that sha under a stale cached `ok`; no new input or write path.
- perf / scale: one builtin pass over the leg indices after the pool drains, and no spawn.
- error / empty / loading states: an unreadable entry or an unmeasured key is skipped, which leaves nothing to erase; a failed quarantine write prints the existing line.
- observability: the existing `cache disagreement` line names every erase, so a reader counting disagreements sees the new population without a new verb.
- risks: a leg that reds once on a plain bar under a cached `ok` is quarantined until its manifest row changes, the cost the sampled branch already pays for a flaky leg.
- testing: two evidence arms, the aged case and the plain-bar case, each observed red at f479ba42's code first.
- migration: none for data; an existing stale `ok` is erased the first time its leg executes red.
- user docs: `tools/run-gates/README.md`'s reuse section states the widened rule.

## 6. Acceptance criteria

- **AC1** — When a scratch repository's one-leg bar earns an `ok`, the leg's consecutive-reuse count
  is set to 10, and the runner runs again with `GATE_REUSE=1` and `GATE_REUSE_SAMPLE=0` while the leg
  exits 1, the run prints `cache disagreement` naming the leg, the entry under its key is gone, and a
  quarantine file exists. Red when: the entry survives the aged red, which is f479ba42's behaviour.
  fixture: the evidence suite's `ru_repo` shape, built in a scratch directory; the count lives in an
  `age.*` file at f479ba42 and in the entry once `TOOL-aSparedSpawn-16` S11 lands.
- **AC2** — When the same scratch repository runs a plain bar, with no `GATE_REUSE`, while its leg
  exits 1 and its key holds an `ok`, the entry is erased and the leg quarantined, and the next
  `GATE_REUSE=1` run prints `GATE ok` for it rather than `GATE reuse`. Red when: a plain bar's red
  leaves the entry, or the next reuse run reuses the leg.
- **AC3** — When `grep -n 'by TOOL-aSparedSpawn-17' tools/run-gates/run-gates.evidence.test.sh` runs,
  it prints one `RAISED` line, and `FLOOR_ASSERTIONS` is that line's new value. Red when: no such
  line exists.
  permission: whether the floor sits at or below the executed count is observed when the suite runs
  at VERIFYING, and the ledger marks it OWED until then.
- **AC4** — When `grep -n 'whatever drew the execution' tools/run-gates/README.md` runs, it prints
  the reuse section's rule. Red when: the README still describes the erase for a sampled leg alone.

## 7. Gates

`run-gates evidence` · `run-gates canary` · `run-gates gov canary` · `run-gates turnstile` ·
`run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `pre-push run-log line` ·
`harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` ·
`spawn budget (forks per hot entrypoint)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 · an aged leg and a plain bar's leg each exiting 1 against a cached ok · FLOOR_ASSERTIONS, by S3

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft, from `TOOL-aSparedSpawn-16` rev-1's S5, AC5 and AC9, promoted to
  a unit of its own by the converged closing review under the owner rulings of 2026-10-04.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "quarantine a leg whose cached ok disagrees with an executed red"`
ranks generic `ok` and `leg` helpers and no reuse seam; no new seam is built. This unit widens the
existing sampled-disagreement quarantine path after `run_leg_retry` in
`tools/run-gates/run-gates.sh` (TOOL-aSparedSpawn-13 S6) rather than adding a second erase, and its
skip set is the one the cache block already uses.

Recall terms used: cache disagreement quarantine sampled age bound aged reuse stale ok erase entry
run_leg_retry GATE_REUSE_SAMPLE push reuse
