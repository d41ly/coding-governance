# TOOL-dPlacedRequest-36 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-36

The unit was built from its spec at rev-5 on base `0e047f564`. TOOL-dPlacedRequest-24 had moved the (PINNED)
factory into the `gov_feed_sh` block of `tools/lib/gov-feed.sh` and both carriers, so the two event
calls of `tools/lib/gov-feed.sh#write_dir_lock` now read `resolve_health_log "${ROOT:-${1%/*}}"`, the
block's comment states how the path is found, the canonical header states the carrier requirement,
and the block was copied byte-identical into `tools/unattended/unattended.sh` and
`tools/run-gates/post-merge.sh`; post-merge gains the `health_log_sh` block inline after it. The
driver reaches the appender through `tools/unattended/lib-unattended.sh`, unchanged. Each criterion
below was observed by a probe: the spec's own `awk` cuts of both blocks from post-merge, sourced under
`env -i PATH="$PATH" bash -c 'set -u; REMOTE_BOUND=60; …'` over a scratch repository's common dir
under the node's short temp path. The staged red is a copy of the feed cut whose event calls read
`"$ROOT"`, the spelling the factory carried at the base. No gate, suite or bar ran in this pass.

**Evidences:** TOOL-dPlacedRequest-36
- AC1 — a planted `gov-feed.lock` whose `until` passed 5 s ago: `write_dir_lock "$c/gov-feed.lock" t1 (PINNED)
  10 node` exited 0, the lock's `owner` read `t1`, and `health.log` in the common dir gained 1 line (DERIVED)
  whose source is `unattended` and event `node-lock-broken`. The staged copy printed `ROOT: unbound
  variable`, exited 0 and logged 0 lines (DERIVED).
- AC2 — the same lock under a `gov-feed.lock.break` guard aged 120 s: the call returned 1, the guard (PINNED)
  was gone, and `health.log` gained 1 `node-guard-cleared` line with source `unattended` (DERIVED). The
  staged copy logged 0 lines (DERIVED).
- AC3 — `grep -c '^# >>> health_log_sh' tools/run-gates/post-merge.sh` printed 1 (DERIVED).
- Parity — `cksum` of each `awk` cut: `gov_feed_sh` read one sum in all 3 files, `health_log_sh` (DERIVED)
  one sum in `tools/lib/health-log.sh`, `tools/unattended/lib-unattended.sh` and post-merge (DERIVED).
- The driver's path — with `ROOT` set to a scratch repository, a stale `spec-tokens.x.lock` in a
  sidecar dir outside it logged `spec-tokens-lock-broken` to that repository's common dir, so the
  driver's spec-tokens events stay in the repository's log.
- `bash -n` read all 4 changed shell files clean; `gen_map.py --write` added post-merge's three (DERIVED)
  appender functions to `memory/map/generated/symbols.json`, and `--check` then exited 0 (DERIVED).
- The bug-class checklist over the pass commit selected 55 classes; none needed a change. The arm's (DERIVED)
  fixture shows it reached the rule (the lock's owner reads `t1`, the staged copy prints the unset
  name), its staged break is the base's own spelling under a `mutate` that reds a no-op, its git
  calls unset `GIT_DIR`, and its floor counts the 7 increments the suite's counter takes. (DERIVED)

## Owed at the close

- The spec's `New arm:` line: `tools/unattended/unattended.test.sh`, the region-8 (PINNED)
  TOOL-dPlacedRequest-36 block, 7 executed assertions (5 `same`, 1 `hit`, 1 `mutate`), counted on (DERIVED)
  its skip branch too; `FLOOR_ASSERTIONS` 3695 to 3702 and `FLOOR_SHARD_8` 926 to 933. The block (DERIVED)
  sourced alone with stubbed `same`, `hit` and `mutate` read 7 assertions green over this tree, and (DERIVED)
  over a scratch carrier with the appender cut and the event call unguarded it red AC3, AC1 and AC2.
  Its RED-first observation inside the suite is the close's; waived for this build's landing by README
  rule 8. (PINNED)
- The legs the spec's Gates section names, run once by the main loop.
