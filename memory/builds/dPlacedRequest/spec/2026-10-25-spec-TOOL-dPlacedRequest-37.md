# TOOL-dPlacedRequest-37 — the node lock's deadline is the block's own bound, never the driver's `REMOTE_BOUND`

**Status:** CLOSED · rev-6 · 2026-11-19 · node a · Tier-2 · base c63aabbb · streams tooling · order 5 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-37-deviation-371.md](../build/2026-10-25-build-TOOL-dPlacedRequest-37-deviation-371.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-37-deviation-372.md](../build/2026-10-25-build-TOOL-dPlacedRequest-37-deviation-372.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-build-TOOL-dPlacedRequest-37-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dPlacedRequest-37-1-acceptance-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
confirmed **finding 13 at HIGH**. It shares item **H1**, "the node-lock factory is not self-contained
in the `gov_feed_sh` block", with findings 2, 24 and 32, which `TOOL-dPlacedRequest-36`,
`TOOL-dPlacedRequest-38` and `TOOL-dPlacedRequest-39` close. The base's claim-push take wrote a
deadline of `$(( $EPOCHSECONDS + REMOTE_BOUND + 10 ))` (`tools/unattended/unattended.sh:2347` at the
pinned base), a take `TOOL-dPlacedRequest-11` S6 deletes. `REMOTE_BOUND` is the driver's (`:162`);
`tools/run-gates/post-merge.sh` and `tools/push-main.sh` define none and run under `set -u` (`:26`,
`:64`), so a node-lock take reading it aborts there with `REMOTE_BOUND: unbound variable`.
`TOOL-dPlacedRequest-24` S2 now mints `NODE_LOCK_BOUND=10` at the top of the block and passes it as the
shared `write_dir_lock`'s hold. This unit is that constant's guard at order 5: an arm proving a take in
a carrier with no driver name writes its deadline, a grep that no line of the block reads
`REMOTE_BOUND`, and the bash 5 floor the deadline's `EPOCHSECONDS` needs.

## 2. Scope (IN)

- **S1** — The block's own bound, guarded. `NODE_LOCK_BOUND=10`, which `TOOL-dPlacedRequest-24` S2
  assigns at the block's top, is the hold every node-lock take in the block passes the shared
  `write_dir_lock`, `write_dir_lock <lock dir> <token> "$NODE_LOCK_BOUND" node`, so `until` reads
  `$(( EPOCHSECONDS + NODE_LOCK_BOUND ))`; no line of the block reads `REMOTE_BOUND`. Ten seconds covers a holder's whole critical section, since no node lock is
  held across a network call (`TOOL-dPlacedRequest-24` §3), and it is twice the 5 s retry a waiter
  spends. Observed by AC1 and AC2.
- **S2** — The lander's copy. `tools/push-main.sh` carries no `gov_feed_sh` block at order 5; it gains
  one at `TOOL-dPlacedRequest-15` S5 (order 9), cut-equal to the canonical, so it takes the lock with
  this bound and no driver name. That unit's §4 names `tools/push-main.sh` among its files, and
  `TOOL-dPlacedRequest-13`'s `gov_feed_sh` parity row finds the copy by `git grep` once it exists.
  NOT OBSERVED here: the copy is built after this unit, and `TOOL-dPlacedRequest-38`'s carrier arm
  reads it at the close.
- **S3** — The bash floor. The deadline reads `EPOCHSECONDS`, a bash 5 variable. `add_feed_event`,
  the one node-lock take a carrier other than the driver reaches, tests `[ -n "${EPOCHSECONDS:-}" ]`
  before its take; unset, it prints one `feed: NOTE - no EPOCHSECONDS, bash 5 or later is required`
  line and returns 0, the feed's never-fail rule, without touching the lock or the log. The driver's
  queue takes need no test, since the driver reads `EPOCHSECONDS` unguarded elsewhere. Observed by
  AC3.

## 3. Non-goals (OUT)

- No change to the health event path: finding 2's, `TOOL-dPlacedRequest-36`.
- No standing arm over every carrier: finding 24's, `TOOL-dPlacedRequest-38`.
- No change to the staleness rule: `check_dir_lock_stale` reads `until` as it does today
  (`tools/unattended/unattended.sh#check_dir_lock_stale`).
- No environment override of the bound: a lock deadline is no operator knob.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-24` — `write_dir_lock` and `NODE_LOCK_BOUND`, which that unit's S2 mints and this unit guards; without them there is no deadline to guard
- **hands-off** `TOOL-dPlacedRequest-15` — `tools/push-main.sh`'s inline `gov_feed_sh` copy, which carries `NODE_LOCK_BOUND` and so takes the lock under `set -u` with no driver name
- **hands-off** `TOOL-dPlacedRequest-49` — S1, AC1 and §4, which that unit's items for findings 15, 27, 30 and 37 fix, sequence and bound against every section the lock covers
- **hands-off** `TOOL-dPlacedRequest-52` — `NODE_LOCK_BOUND`, which that unit's items for findings 12 and 31 name as the placed race's margin and its discard bound

## 4. Design

### Evidence

- `write_dir_lock` writes `$(( $EPOCHSECONDS + $3 ))` into `until`, its third argument the hold
  (`tools/unattended/unattended.sh#write_dir_lock`). History, not a live reader: `write_claim` passed
  `$(( REMOTE_BOUND + 10 ))` for the claim-push lock (`tools/unattended/unattended.sh@875eaadf:2773`),
  a take `TOOL-dPlacedRequest-11` S6 deletes, and the base's `write_claim_push_lock` wrote the same sum
  (`unattended.sh:2347` at the pinned base).
- `grep -n 'REMOTE_BOUND'` over `post-merge.sh` and `push-main.sh` prints nothing at the base; both
  set `set -u`.
- `grep -c EPOCHSECONDS` at `61b4ebae6` counts 5 in `tools/unattended/unattended.sh`, 38 in
  `tools/run-gates/run-gates.sh`, 0 in `tools/run-gates/post-merge.sh` and 2 in `tools/push-main.sh`,
  both inside `check_claim_push_clear`, which `TOOL-dPlacedRequest-11` S6 deletes; no file tests
  `BASH_VERSINFO`. So after this build only the driver proves bash 5 by use, which S3's test answers.

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: `add_feed_event`'s `EPOCHSECONDS` test
- `tools/unattended/unattended.sh`: the inline block, carried
- `tools/run-gates/post-merge.sh`: the inline block, carried
- `tools/unattended/unattended.test.sh`: the deadline arm
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `feed: NOTE - no EPOCHSECONDS` | output line | none |

### Alternatives rejected

- **`${NODE_LOCK_BOUND:-70}`, the review's example.** An environment default is a second channel that
  leaves no diff, and 70 s is the claim-push lock's push window, which no node lock covers; a crash
  inside the feed's append would cost every append on the node 70 s of `feed: NOTE` lines.
- **A figure typed at every call.** Both callers would type the same number; they pass the one
  constant through the shared factory's hold argument instead.

## 5. Production-readiness checklist

- security — none.
- perf / scale — none: one arithmetic expansion.
- error / empty / loading states — a crashed holder's lock is breakable 10 s after its take, not 70.
- observability — `until` holds the bare epoch as before.
- risks — a holder stalled more than 10 s inside its microsecond section can be broken while live;
  the guarded break then admits one breaker, as `TOOL-dPlacedRequest-24` §5 states.
- testing — the probes of §6 and the arm in §7.
- migration — none: the factory is new in this build.
- user docs — none: no guide states the lock's deadline.

## 6. Acceptance criteria

The probe cuts the `gov_feed_sh` block with `awk` from `# >>> gov_feed_sh` to `# <<< gov_feed_sh` and
runs in a scratch git repository with common dir `$c`.

- **AC1** — When `env -i PATH="$PATH" bash -c 'set -u; <gov_feed_sh cut of post-merge.sh>;
  write_dir_lock "$c/gov-feed.lock" t1 "$NODE_LOCK_BOUND" node; echo rc=$?'` runs with no
  `REMOTE_BOUND` set, it prints `rc=0` and `$c/gov-feed.lock/until` reads a value within 1 of
  `EPOCHSECONDS` plus 10.
  Red when: the bound reads a driver name, the staged case being a cut whose constant line is
  replaced by `NODE_LOCK_BOUND=$(( REMOTE_BOUND + 10 ))`, which prints `REMOTE_BOUND: unbound variable`.
- **AC2** — When `awk` cuts `gov_feed_sh` from `gov-feed.sh` and `grep -c 'REMOTE_BOUND'` runs over
  the cut, it prints 0, and `grep -c '^NODE_LOCK_BOUND=10$'` over it prints 1.
  Red when: a later edit routes the deadline back through the driver's bound.
- **AC3** — When `env -i PATH="$PATH" c="$c" bash -c 'set -u; unset EPOCHSECONDS; <gov_feed_sh cut of
  post-merge.sh>; GOVFEED_DIR=$c add_feed_event refs/gov/runs/tFix <commit>; echo rc=$?'` runs in the
  scratch repository, it prints one `feed: NOTE -` line naming `EPOCHSECONDS` and `rc=0`, and
  `$c/gov-feed.log` and `$c/gov-feed.lock` are absent.
  Red when: a bash without `EPOCHSECONDS` aborts the carrier or takes the lock with an empty deadline,
  the staged case being a cut with the test removed.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `tier2-review self-test` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC3 · the deadline written by a take with no driver name set, staged against the verbatim claim-push body, and a take with `EPOCHSECONDS` unset, staged by cutting S3's test · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What bounds a node lock's deadline?** (a) A block constant of 10 s; (b) the review's
  `${NODE_LOCK_BOUND:-70}`; (c) an argument per call. (b) keeps a push window no node lock spans and
  opens an environment channel; (c) passes one figure twice. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound with its example value replaced by the
  bound the holder's section needs. widens: none · relaxes: none. Rev-4: the shared factory takes its
  hold as an argument, so (a)'s constant is what each take passes; no call types a figure.

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  13 (HIGH, item H1, shared with findings 2, 24 and 32).
- rev-2 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.
- rev-4 · 2026-11-19 · §2 S1 · §3 Non-goals, Edges · §4 Evidence, Alternatives rejected · §6 AC1 · §8
  F1 · §10 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit` finding 15 (H3): the factory is the shared `write_dir_lock`, whose hold
  argument carries `NODE_LOCK_BOUND`, and AC1 takes the lock through the feed's own call. §7 also names `scratch-guard self-test`, `tier2-review self-test`, the leg(s) the spec-token guard join names for this spec's Files touched.
- rev-5 · 2026-11-19 · §1 · §2 S1, S3 · §3 Edges · §4 Evidence, Files touched, Inventory · §6 AC3 · §7 ·
  folds `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`: finding 1 (M1), `NODE_LOCK_BOUND` is
  minted by TOOL-dPlacedRequest-24 S2, so this unit narrows to its guard and the Goal no longer says
  unit 24 builds the factory from the claim-push body; finding 4 (L1), Evidence cites `write_claim`'s
  take as history; finding 11 (L5), the bash 5 floor rests on no code the build deletes, S3 tests
  `EPOCHSECONDS` before the feed's take, observed by AC3.
- rev-6 · 2026-11-19 · §4 Files touched · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-24`'s factory, the shared `write_dir_lock`
(`tools/unattended/unattended.sh#write_dir_lock`); only the hold its node-lock callers pass is new. `python
tools/codebase-map/reuse_lookup.py "lock deadline bound for a node-local mkdir lock"` returned name-stem
hits only (`read_bound_key`, `boundedParallel`), none a lock deadline; `read_bound_key` reads a conf
key, which a lock's deadline is not. `python tools/memory-recall/query.py "what bounds the node lock
deadline"` returned TOOL-aGraftedHelix-37, whose spec sets the claim-push lock's `until` rule, and
scout A's row; neither disagrees with source.

Recall terms used: node lock deadline until REMOTE_BOUND claim-push.lock mkdir stale break gov-feed.lock bound
