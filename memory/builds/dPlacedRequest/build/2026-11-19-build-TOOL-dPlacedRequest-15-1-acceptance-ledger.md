# TOOL-dPlacedRequest-15 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-15

The unit was built from its spec at rev-6 (PINNED) on base `a1c5630e4`. The driver gains the `fence` act of
`--lease`, `tools/unattended/unattended.sh#write_fence_beat`, dispatched for `build <slug>` only. The lander
gains `tools/push-main.sh#read_fence_line`, `tools/push-main.sh#check_fence_beat` and
`tools/push-main.sh#write_effect_push`, the one push both landing paths now make, and carries the
`gov_feed_sh` and `health_log_sh` blocks inline, byte-identical to the lib dir's canonicals (a python
comparison of the cut blocks read `True` for both). `tools/push-main.sh#derive_push_failure` keeps its order
of evidence and reads the lease once on `unchanged` only, printing `fenced` or `unfenced`. The attended
landing takes `--slug`, held to the build-folder grammar.

The spec's citations were resolved by symbol before the first edit: `build_gov_commit` is parented on the
tip read since TOOL-dPlacedRequest-11, the `lease` column of `check_claim_writable` reads `mine` on fleet
tag and session, `scan_feed_writers` holds `add_feed_event` as a helper, and the two effect pushes were
the `git push` lines of `cmd_land` and the attended path. No new refusal site of the `exit` kind joined either script, so the
driver stays under its refusal ceiling: every fence refusal reaches the existing exit of the landing's
`case` through `cls=refused`.

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe script in the run's
scratch directory over a fixture under the node's short temp path: a bare origin, clone A whose
`.githooks/pre-push` is a stub writing the allow record `check_push_allow` reads, clone B, leases on, the
lander copied in and the driver beside it as a one-line launcher of this tree's driver, clone A's session
`sA` holding lease `fx` under fleet tag `a`, and clone B taking it as fleet tag `b` under the same session.

**Evidences:** TOOL-dPlacedRequest-15
- AC2 — the stub hook ran clone B's `--lease take-over build fx` during clone A's `--land --slug fx`;
  the lander exited 1 (PINNED) printing `push-main: fenced — the lease refs/gov/leases/fx/build was taken
  after the fence read it at <tip> …`, the origin's default branch held the same sha before and after, and
  the lease tip's record read `fleet-tag: b`.
- AC3 — a stub driver printing a fence line whose beat is its tip: exit 1 (PINNED), `the fence beat <sha> IS
  the lease tip …` from `check_fence_beat`, the default branch and the lease tip unchanged.
- AC4 — `--land --slug fx` exited 0 (PINNED); the origin's default branch was clone A's HEAD, the lease tip
  was the beat, `git rev-parse <beat>^` was the tip read, the beat's record read `renews: no`, and clone A's
  `gov-feed.log` held 1 line (PINNED) naming the lease ref at the beat. `scan_feed_writers` over the tracked
  population the lib suite reads printed nothing; over a copy of the lander without the
  `add_feed_event` line beside the canonical `gov-ref.sh` it printed the copy's push line and
  returned 1 (PINNED).
- AC5 — against the lease clone B held the lander exited 1 (PINNED) printing `lease refused — live-holder ·
  fx/build · node b …`, nothing moved; the driver under `RUN_CLAIMS="off"` printed `fence — none · leases
  are off`, exit 0 (PINNED), and the landing exited 0 with the lease tip unmoved; over a remote with no
  lease the driver printed `fence — none · no lease on the remote`, exit 0 (PINNED).
- AC6 — with `receive.advertiseAtomic false` on the origin, git printed `fatal: the receiving end does not
  support --atomic push`, the lander exited 1 (PINNED) printing `push-main: unfenced — the remote refused
  the atomic push …`, and the default branch and the lease tip were unchanged.
- AC7 — `push-main.sh --slug fx` on clone A's `main` printed the fence line and exited 0 (PINNED), the
  beat parented on the tip read; the next no-argument landing printed 0 (PINNED) fence lines, exited 0 and
  left the lease tip unmoved. `--slug 'a b'` exited 2 (PINNED) naming the build-folder grammar.
- AC8 — `grep -n "lease fence"` and `grep -n "LANDER --slug"` over `tools/unattended/VERBS.template.md`
  each found a line; `memory/guides/UNATTENDED-VERBS.md` is a byte-for-byte copy (`cmp` silent).
- AC9 — a stub driver exiting 2 printing nothing: exit 1 (PINNED), `push-main: fence read unparsed — exit 2
  · (empty)`; a stub exiting 0 printing two `fence — none` lines: exit 1 (PINNED), `fence read unparsed —
  exit 0 · fence — none · leases are off` (PINNED); the default branch and the lease tip unchanged.
- No driver beside the lander: `fence — none · no unattended driver beside this lander, so no lease is
  fenced`, exit 0 (PINNED), the lease tip unmoved.

**Owed at the close.**
- AC1, the real remote's `--atomic` push of two scratch refs under `refs/gov/probe/`: this pass may push to
  no remote but a scratch origin of its own, so the observation is the main loop's.
- The `New arm:` line on `tools/push-main.test.sh`: arms 42 to 49, 8 (DERIVED) `ok`/`bad` pairs over the
  fixture above, RED-first against the base lander, which pushes one ref, moves no lease and refuses the
  attended `--slug`.
- The `New arm:` line on `tools/unattended/unattended.test.sh`: the region-eight block `TOOL-dPlacedRequest-15`,
  6 (DERIVED) `same` assertions, RED-first against the base driver, which has no `fence` act; the floors rose
  by the same 6 (DERIVED), `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8`. Waived for this build's landing by README
  rule 8.
- The legs the spec's section 7 names, the `gov_feed_sh` parity and carrier rows of the lib suite among them,
  which now read the lander as a carrier.
