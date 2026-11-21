# TOOL-dPlacedRequest-24 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-24

The unit was built from its spec at rev-8 on base `d1b37939a`, starting from the first dispatch's
partial patch for S1 to S4, whose S5 branch (the `ls-remote` read and the `landed` line in
`tools/unattended/unattended.sh#write_gov_queue`) was removed with the spec's S5. The shared
`write_dir_lock` family, `read_proc_token`, `check_proc_gone` and `PT_TOKEN` now sit in the
`gov_feed_sh` block (`tools/lib/gov-feed.sh#write_dir_lock`), carried byte-identical by the driver and
`tools/run-gates/post-merge.sh`, with `NODE_LOCK_BOUND` and the retrying take
`tools/lib/gov-feed.sh#write_dir_lock_wait` beside them; `add_feed_event`, `add_gov_queue` and
`write_gov_queue` take their locks through it. Each criterion below was observed by a probe: the
driver's `--lease` verb and its functions sourced in process over a scratch clone and bare origin
under the node's short temp path, `RUN_CLAIMS` on, `USERNAME=daily-agent`, the origin renamed away,
built by the suite's own `mkconf` and `write_lease_fixture` evaluated alone. No gate, suite or bar
ran in this pass; the arm the spec's §7 declares and its RED-first observation are owed at the close.

**Evidences:** TOOL-dPlacedRequest-24
- AC1 — offline, the first `--lease acquire build tOff` exited 0 printing `queued · epoch 1` and the
  second exited 0 printing `lease — queued — already · tOff/build`; `grep -c ''` over
  `gov-queue.log` printed 1 (DERIVED).
- AC3 — with `gov-queue.lock` planted holding a live `until`, `add_gov_queue` exited 2 after
  4217090 microseconds, inside 6 s (DERIVED); the offline `--lease acquire build tBusy` exited 2
  printing `lease not written — gov-queue.lock busy`, and the queue's `cksum` was unchanged (DERIVED).
  With `write_dir_lock` wrapped by `eval` of `declare -f` as `write_dir_lock_once`, counting each try
  and removing the planted lock after a busy one, `add_gov_queue` exited 0 after 2 tries and the queue
  grew from 1 line to 2 (DERIVED).
- AC4 — with `write_gov_ref` stubbed to append a `tQ2` line while the `tQ1` line is pushed,
  `write_gov_queue` printed `flushed` for `tQ1`, exited 0, and the file then held exactly the `tQ2`
  line (DERIVED).
- AC5 — two background breakers called `write_dir_lock` with stem `node` on one planted lock whose
  `until` had passed, meeting at an `rm` shim first on each one's PATH: over 3 runs each, 1 printed
  `taken` and the health log gained 1 `node-lock-broken` line (DERIVED). Over a scratch copy of the
  driver with the `.break` guard cut, the same probe printed `taken` twice and 2 events in each of 3
  runs (DERIVED). The shim's liveness is the marker count: 1 breaker reached it on the guarded copy and
  2 on the cut one (DERIVED). The shim path must be a POSIX path: a `C:/` path splits PATH on its
  colon, and the probe then ran green on both copies, so the suite's arm counts the marker too.
- AC6 — the `awk` cut of each `gov_feed_sh` block from `gov-feed.sh`, `unattended.sh` and
  `post-merge.sh` compared equal under `cmp`, each defining `write_dir_lock` once (DERIVED).
  `grep -n 'gov-feed.lock' gov-feed.sh` printed 3 lines (DERIVED): one argument of
  `write_dir_lock_wait`, S2's retrying take of `write_dir_lock`, and two of `remove_dir_lock`; no line
  takes the lock by a `mkdir` of its own.
- AC7 — `grep -c '^write_dir_lock()'` over `tools/unattended/unattended.sh` printed 1, and over the
  `awk` cut of its `gov_feed_sh` block printed 1 (DERIVED); the `git grep` for a node-lock factory
  under `tools` printed nothing, and the `awk` over the build's specs outside each revision log printed
  nothing (DERIVED).
- The suite block `TOOL-dPlacedRequest-24 — THE OFFLINE QUEUE UNDER ONE NODE LOCK` adds 9
  region-eight assertions, 7 `same` and 2 `hit` (DERIVED), so `FLOOR_ASSERTIONS` moves 3562 to 3571
  and `FLOOR_SHARD_8` 796 to 805 (DERIVED). Its steps were run as the probe above; the block itself was
  not run, and its RED-first observation against `TOOL-dPlacedRequest-1`'s unlocked queue and the
  guard-cut copy is the close's.
- `gen_map.py --check` read `symbols.json` stale before `--write` and exited 0 after it (DERIVED).
