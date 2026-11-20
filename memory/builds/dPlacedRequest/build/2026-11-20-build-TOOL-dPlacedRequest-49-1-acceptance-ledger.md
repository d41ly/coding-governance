# TOOL-dPlacedRequest-49 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-49

The unit was built from its spec at rev-7 on base `e292371f8`. Built: S2, S5, S6, S8, S20, S23, S26,
S28, S32, S33 and S34; probed: S12 and S22; nothing for the items the spec's §4 closes or resolves.
`tools/lib/gov-feed.sh#write_dir_lock` sets `_fl_mine=1` once its `mkdir` lands and writes `owner`
before `until`; `tools/lib/gov-feed.sh#add_feed_event`'s subshell empties `_fl_mine`, arms its `EXIT`
trap before `write_dir_lock_wait`, and the trap, acting only on the flag, clears the lock directory
where `owner` is absent or reads the call's token. The `gov_feed_sh` block, its `NODE_LOCK_BOUND`
comment restated (S33), was spliced byte-identically into the driver, the post-merge hook and the
lander. `tools/unattended/unattended.sh#read_gov_queue_head` reads the ref's newest queued line whole
and returns 1 on a line of another shape or a commit `cat-file -e` does not find, and the offline arm
of `tools/unattended/unattended.sh#run_lease_verb` then releases its hold and refuses.
`skills/session-kickoff/manifest-check.sh#derive_node_tag` answers `GOV_NODE` first, and
`CARD_FETCH_BOUND` defaults to `CARD_CLAIMS_BOUND`'s figure. The resolver suite's carrier arm reads
the appender each carrier reaches, counts the appended line, and lists its population through the
new `tools/lib/resolve-python.test.sh#read_feed_carriers`. No gate, suite or bar ran in this pass:
every criterion below was observed by a probe of the changed code over a scratch fixture, the lease
fixture being the unattended suite's own `write_lease_fixture`, `run_lease_arm` and `run_offer_arm`
cut from the suite and sourced, under the node's short temp path.

**Evidences:** TOOL-dPlacedRequest-49
- AC2 — `awk` over the engine read `CARD_FETCH_BOUND` 15 and `CARD_CLAIMS_BOUND` 15, the first at (DERIVED)
  most the second, and no `CARD_PUBLISH_BOUND` in `read_card_ref`'s body; at the base it read the (DERIVED)
  fetch default 20, red. (PINNED)
- AC5 — with `: "$GOVFEED_PLANT_UNSET"` on the line after `write_dir_lock`'s first write, a fresh
  take under `set -u` in a subshell left `owner` reading `tok-1` and no `until`; the base cut, which
  writes `until` first, left `until` and no `owner`.
- AC6 — with the plant between the take's `mkdir` and its first write, the call under `env -i` in a
  scratch repository printed `after` and bash's unbound-name line and left no `gov-feed.lock`; a
  second, clean call appended 1 line. A busy call over a live lock held by `other`, and over a live (DERIVED)
  lock with no `owner`, each printed the lock-busy NOTE and kept the holder's lock. RED: the base
  cut, its trap armed after the take, left the lock; the new cut with the `_fl_mine` guard cut
  cleared the ownerless holder's lock.
- AC8 — the carrier arm cut from the resolver suite, run over a scratch carrier holding the block
  with no appender and sourcing nothing, printed `<file>: no health_log_sh beside gov_feed_sh` and
  returned 1; over the real population, the canonical, the lander, the post-merge hook and the
  driver, read through its `lib-unattended.sh`, it returned 0 and printed nothing. The base arm
  passed the bare carrier.
- AC12 — the `DPR41` tOff chain, an online acquire of tOn, the origin renamed away, an offline
  acquire and release of tOff, the origin restored and a flush, read over the driver a flush exit of
  0, tOff `withdrawn` on the origin; over a copy whose `[ "$tip" != - ] || tip=""` line is cut, the (DERIVED)
  flush exited 2 and the origin held no `refs/gov/leases/tOff/build`. (DERIVED)
- AC20 — the cut arm over a canonical plant whose take line opens with `[ -n "${ROOT:-}" ] || exit 0`,
  the line after the trap, printed `<file>: add_feed_event appended 0 lines` and returned 1; the base (DERIVED)
  arm passed it.
- AC22 — `manifest-check.sh --card --write` in a scratch tree whose `.unattended.conf` resolves a
  stub driver writing `boom` to stderr alone and exiting 1 read `claims — skipped: boom`. RED: a copy (DERIVED)
  passing `/dev/null` as the err file over a present, empty err file read `claims — skipped:
  --claims exited 1 and printed nothing`; the same copy with no err file at all printed no claims
  cell, its awk unable to open the file.
- AC23 — over the real registry with `GOV_NODE` and `USER` unset, each `fleet.toml` row's user read
  that row's tag from `derive_node_tag`, `resolve_node_tag` and `resolve_fleet_tag` alike, rows a to
  d; `GOV_NODE=a` under row b's user read `a|a|a`; `GOV_NODE=w` read `node — UNKNOWN: GOV_NODE w
  names no Tag cell in AGENTS.md`. The base engine read `b|a|a` and `node — b · agent5 @
  DESKTOP-3J1O6CD` for the same two.
- AC26 — an offline `--lease release build tOff --as withdrawn` over a newest queued line naming
  an absent sha, and over that line cut to three fields, each printed `lease not written —
  tOff/build · queued commit unreadable; nothing queued`, exited 2 and left `gov-queue.log` (DERIVED)
  byte-identical; over the readable line it queued a second line, exit 0. The base driver was (DERIVED)
  refused `live-holder` on the absent sha, an empty record read as the chain's, and queued on the
  three-field line, exit 0. (DERIVED)
- AC28 — `--lease status build tFix` with `CLAUDE_CODE_SESSION_ID` unset in the lease fixture's
  clone exited 0 and printed `lease — none · tFix/build`; a copy with the `status` branch cut exited (DERIVED)
  2 printing the act check's `not 'status'` line. (DERIVED)
- AC32 — the population command over a scratch repository tracking `a.sh` and `notes.md`, each
  carrying `# >>> gov_feed_sh` at column 0, listed `a.sh` alone; the base command listed both. The
  line `git grep -l '^# >>> gov_feed_sh'` in the resolver suite carries the parity loop's pathspec.
- AC33 — `awk` over the comments above `NODE_LOCK_BOUND=10` found `add_feed_event`,
  `add_gov_queue`, `write_gov_queue`, `write_gov_queue_hold` and `write_request_record` once each,
  and the measurement `measured once on node d on 2026-11-20` with its figure pinned in the code; (PINNED)
  the base comment named none of them.
- AC34 — every event token passed to `add_health_event` in the driver and the canonical, each `$4`
  stem expanded by the stems `write_dir_lock` is called with, counted apart over the kit README:
  `claim-taken-over`, `lease-yielded`, `node-lock-broken`, `node-guard-cleared`,
  `spec-tokens-lock-broken` and `spec-tokens-guard-cleared` each read at least 1; at the base (DERIVED)
  `lease-yielded` read 0. (DERIVED)
- S33's measurement — over a driver copy logging every node lock's take and release, an online
  acquire, an offline acquire and release, a flush and a `--request` on node d held `gov-queue.lock`
  longest, through the offline acquire's hold: 1.412 s against the 10 s bound. (PINNED)
  The feed lock's longest hold read 0.083 s and `requests.lock`'s 0.104 s. (PINNED)
- Parity and syntax — `cksum` of the `gov_feed_sh` cut read one sum in all 4 files; `bash -n` read (DERIVED)
  every changed shell file clean, the three suites included through scratch copies.
- The arms' fixtures — a probe applying the unattended suite's new `sed` scripts, as written in the
  file, to the driver's cut read each one moving its line: the owner and until swap, the two plants
  after the first write, the plant after `_fl_mine=1`, the trap moved after the take and the trap's
  guard cut; the new block's two driver copies read `1 0` for their staged lines. (DERIVED)

## Items diverged

- S33 names node a for its measurement; this pass ran on node d (`d41ly`, `fleet.toml`'s row d),
  so the comment names node d.
- S20's plant: a bare `$ROOT` read under `set -u` prints bash's unbound-name line, which the arm's
  stderr check reds first, so no bare read reds "on that assertion alone". The plant reads `ROOT`
  through `${ROOT:-}` and skips the append, which only the line count catches.
- AC22's red as the spec spells it holds only where the err file exists; with none, the claims cell
  is not printed at all. Both readings are recorded above.

## Owed at the close

- The spec's `New arm:` lines: `tools/unattended/unattended.test.sh` (AC5, AC6, AC26, AC28), 21 (DERIVED)
  region-eight assertions, `FLOOR_ASSERTIONS` 4003 to 4024 and `FLOOR_SHARD_8` 1222 to 1243, (DERIVED)
  waived for this build's landing by README rule 8; `tools/lib/resolve-python.test.sh` section 2a's
  three new rows (AC8, AC20, AC32); and `skills/session-kickoff/manifest-check.test.sh`'s AC23 rows, (DERIVED)
  its `FLOOR_ASSERTIONS` 370 to 374, with `GOV_NODE` unset at the fixture's top so the AC4 rows keep (DERIVED)
  reading the user. Each RED-first observation is the close's.
- The positional citations of the three carriers past the `gov_feed_sh` block, which the restated
  comments move, read by the pass legs.
- The legs the spec's Gates section names, run once by the main loop, the spawn budget among them:
  `read_gov_queue_head` now runs one `cat-file` where a queued line exists.
