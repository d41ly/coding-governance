# TOOL-dPlacedRequest-36 — the node-lock factory writes its health events through the lock's own common dir

**Status:** INPROGRESS · rev-5 · 2026-11-19 · node a · Tier-2 · base c63aabbb · streams tooling · order 5 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-36-deviation-361.md](../build/2026-10-25-build-TOOL-dPlacedRequest-36-deviation-361.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-36-deviation-362.md](../build/2026-10-25-build-TOOL-dPlacedRequest-36-deviation-362.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-build-TOOL-dPlacedRequest-36-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dPlacedRequest-36-1-acceptance-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
confirmed **finding 2 at HIGH**. It shares item **H1**, "the node-lock factory is not self-contained
in the `gov_feed_sh` block", with findings 13, 24 and 32, which `TOOL-dPlacedRequest-37`,
`TOOL-dPlacedRequest-38` and `TOOL-dPlacedRequest-39` close. `TOOL-dPlacedRequest-24` S1 makes the
factory the claim-push lock's bodies renamed, and those bodies write their health events with
`add_health_event "$(resolve_health_log "$ROOT")" unattended …` (`tools/unattended/unattended.sh:2338`
and `:2351` at the pinned base). `tools/run-gates/post-merge.sh`, a carrier of the block, defines no
`ROOT`, `add_health_event` or `resolve_health_log` and runs under `set -u` (`:26`), so a stale break
there aborts the carrier and loses the event; the spec says nothing about how the block reaches the
health log. This unit repairs `TOOL-dPlacedRequest-24` at order 5: the events go through the lock's
own directory and the health appender every carrier holds beside the block.

## 2. Scope (IN)

- **S1** — The event path. `write_dir_lock`, the shared factory `TOOL-dPlacedRequest-24` S1 moves
  into the block, writes its `<stem>-guard-cleared` and `<stem>-lock-broken` events with
  `add_health_event "$(resolve_health_log "${ROOT:-${1%/*}}")" unattended <event> <lock dir>`. The
  driver defines `ROOT`, so its spec-tokens lock, which lives in the sidecar dir, logs where it does
  today. A carrier with no `ROOT` asks git once, from the lock's parent, which for every node lock is
  the git common dir, so the factory reads no unset name under `set -u`. The source token stays
  `unattended`, the kit that ships the factory, and the stem `node` names the lock in the event.
  Observed by AC1 and AC2.
- **S2** — The appender beside the block. Every file carrying `gov_feed_sh` carries the
  `health_log_sh` block too, inline and byte-identical: `tools/run-gates/post-merge.sh` gains it, and
  `tools/unattended/unattended.sh` already has it through `lib-unattended.sh` (`:63-110`), which it
  sources at `:101`. The canonical `gov-feed.sh` header states the requirement. The existing
  `health_log_sh` parity row finds the new copy by `git grep`, so no row is added. Observed by AC3.

## 3. Non-goals (OUT)

- No change to the deadline the factory writes: finding 13's, `TOOL-dPlacedRequest-37`.
- No standing arm over every carrier: finding 24's, `TOOL-dPlacedRequest-38`.
- No containment of an abort inside the append: finding 32's, `TOOL-dPlacedRequest-39`.
- No change to the health log's format or cap: `tools/lib/health-log.sh`'s.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-24` — `write_dir_lock` and its two health events, whose writer this unit makes self-contained; without the factory there is no event to route
- **hands-off** `TOOL-dPlacedRequest-15` — `tools/push-main.sh`, which carries the `health_log_sh` block beside `gov_feed_sh` when that unit inlines the block, so the lander's stale break writes its event
- **hands-off** `TOOL-dPlacedRequest-49` — the Goal, S2, AC1 to AC3 and §4, which that unit's items for findings 11, 15, 17 and 27 reword, fix and observe over every carrier
- **hands-off** `TOOL-dPlacedRequest-52` — AC3, which that unit's item for finding 6 points at `TOOL-dPlacedRequest-38`'s carrier arm

## 4. Design

### Evidence

- The shared factory's events: `tools/unattended/unattended.sh#write_dir_lock` writes
  `<stem>-guard-cleared` and `<stem>-lock-broken`, each with
  `add_health_event "$(resolve_health_log "$ROOT")" unattended …`; its spec-tokens caller's lock is
  `spec-tokens.<slug>.lock` under `resolve_sidecar_dir`, not the common dir
  (`tools/unattended/unattended.sh#init_spec_token_check`).
- `health_log_sh` (`tools/lib/health-log.sh:14-61`) defines `derive_health_log <common-dir>`, which
  prints `<common-dir>/health.log` and spawns nothing, and `add_health_event`, which never fails its
  caller. Its inline copies today: `check-wiring.sh`, `run-gates.sh`, `lib-unattended.sh` and
  `manifest-check.sh`; `post-merge.sh` and `push-main.sh` carry none.
- `TOOL-dPlacedRequest-13` §4 places `gov-feed.lock` in the common dir and `TOOL-dPlacedRequest-24`
  S2 places `gov-queue.lock` there.

### The break, end to end

```
write_dir_lock <common>/gov-feed.lock <token> "$NODE_LOCK_BOUND" node
  mkdir fails, lock stale, guard taken, lock re-made
  add_health_event "$(resolve_health_log "${ROOT:-<common>}")" unattended node-lock-broken <common>/gov-feed.lock
```

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: the factory's two event calls and the header's carrier requirement
- `tools/unattended/unattended.sh`: the inline block, carried
- `tools/run-gates/post-merge.sh`: the inline block, carried, and the `health_log_sh` block inline
- `tools/unattended/unattended.test.sh`: the break-event arms
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Alternatives rejected

- **Guard the call with `command -v add_health_event`.** A carrier without the appender would lose
  the event silently, the outcome the finding names.
- **Pass the component label in.** No reader of the health log tells carriers apart by source, and
  the lock path in the detail field already names the common dir.
- **`derive_health_log` of the lock's parent, this unit's rev-3 path.** The factory is shared, and its
  spec-tokens lock lives in the sidecar dir, so that path would move the spec-tokens events out of the
  repository's health log.

## 5. Production-readiness checklist

- security — none: the log stays in the common dir and is never pushed.
- perf / scale — one `git` spawn per break, as today, and none on a take.
- error / empty / loading states — `add_health_event` prints one `health: NOTE -` line and returns 0
  on any failure, so a break never fails on its event.
- observability — the two events now reach the log from every carrier.
- risks — `post-merge.sh` grows by the `health_log_sh` block, about 40 lines.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — none: the kit README's event list is finding 21's and 31's, items of
  `TOOL-dPlacedRequest-43`.

## 6. Acceptance criteria

The probe cuts each block with `awk` from its `# >>> <stem>` line to its `# <<< <stem>` line, runs in
a scratch git repository, and sets `REMOTE_BOUND=60` so it observes the event path alone, whatever
`TOOL-dPlacedRequest-37` has built.

- **AC1** — When `env -i PATH="$PATH" bash -c 'set -u; REMOTE_BOUND=60; <health_log_sh cut>; <gov_feed_sh
  cut>; write_dir_lock "$c/gov-feed.lock" t1 10 node'` runs, both cuts taken from `post-merge.sh`,
  over a planted `gov-feed.lock` whose `until` has passed, it exits 0, and `health.log` in `$c` gains
  one line whose source is `unattended` and event `node-lock-broken`.
  Red when: the break expands `ROOT` unguarded, the staged case being the factory's event call as
  `write_dir_lock` spells it in `tools/unattended/unattended.sh`, which aborts on `ROOT: unbound
  variable`.
- **AC2** — When the same probe plants a `gov-feed.lock.break` guard older than one minute, the call
  returns 1, the guard is gone, and `health.log` in `$c` gains one `node-guard-cleared` line with
  source `unattended`.
  Red when: the guard-cleared path needs a name the carrier lacks.
- **AC3** — When `grep -c '^# >>> health_log_sh' tools/run-gates/post-merge.sh` runs, it prints 1.
  Red when: a carrier holds the factory with no health appender beside it.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `tier2-review self-test` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the break and guard-cleared events over a planted stale lock, staged against the verbatim claim-push body · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How does the block reach the health log in a carrier with no driver?** (a) `derive_health_log`
  of the lock's parent, with `health_log_sh` carried beside the block; (b) the call guarded by
  `command -v`; (c) a second appender inside `gov_feed_sh`. (b) drops the event where it matters;
  (c) is a second copy of the appender the `health_log_sh` parity row exists to prevent.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's fix judged sound and the charter's
  `[reuse]` rule. widens: none · relaxes: none. Rev-4 keeps (a)'s carriage and reaches the log through
  `resolve_health_log "${ROOT:-<lock's parent>}"`, because the shared factory's spec-tokens lock is
  not in the common dir.

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  2 (HIGH, item H1, shared with findings 13, 24 and 32).
- rev-2 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.
- rev-4 · 2026-11-19 · §2 S1 · §3 Edges · §4 Evidence, The break end to end, Alternatives rejected ·
  §5 · §6 AC1, AC2 · §8 F1 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit` finding 15 (H3): the event path is the shared
  `write_dir_lock`'s, reaching the log by `ROOT` where the driver sets it and from the lock's parent
  where no `ROOT` exists, so the spec-tokens caller keeps its log; events read `node-lock-broken` and
  `node-guard-cleared` under the stem `node`. §7 also names `scratch-guard self-test`, `tier2-review self-test`, the leg(s) the spec-token guard join names for this spec's Files touched. AC1 names the factory in prose, the path-token join reading no anchor inside a criterion.
- rev-5 · 2026-11-19 · §4 Files touched · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.

## 10. Reuse audit

The seam extended is the `health_log_sh` block (`tools/lib/health-log.sh:14-61`), its
`derive_health_log` and `add_health_event` reused unchanged and carried into one more file under its
existing parity row (`tools/lib/resolve-python.test.sh:180`). `python
tools/codebase-map/reuse_lookup.py "write a health event from a copy-installed block without the repo
root"` ranked `add_health_event` among name-stem hits (`write`, `repo_root`), naming its nine
carriers; it is the seam. `python tools/memory-recall/query.py "how does an inline block write a
health event without the repo root"` returned scout A's row 4, this audit's H1 and TOOL-aPairedSlots-10
on the appender's inline copies; none disagrees with source.

Recall terms used: health_log_sh derive_health_log add_health_event common dir inline block carrier gov_feed_sh node-lock-broken
