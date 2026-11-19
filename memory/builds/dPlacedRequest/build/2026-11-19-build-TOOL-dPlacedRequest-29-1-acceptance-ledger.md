# TOOL-dPlacedRequest-29 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-29

The unit was built from its spec at rev-3 (PINNED) on base `0080f3432`. The driver's fence act,
`tools/unattended/unattended.sh#write_fence_beat`, takes `--after <tip>`: the same one read, and the
fence line on the new tip only where the `lease` column reads `mine`, `<tip>` is on the new tip's
first-parent chain and the two epochs are equal; every other reading is `lease refused — epoch-fence`,
exit 1, a foreign holder keeping its own cause word. The lander's
`tools/push-main.sh#derive_push_failure` re-reads a moved lease through
`tools/push-main.sh#read_fence_line`, now handed the tip read, and prints the class `refenced` on a
fence line, `fenced` otherwise; both attempt loops, `tools/push-main.sh#cmd_land` and the attended
loop, take `refenced` as one more attempt with no re-prepare. No function was minted, so the naming
lexicon had nothing to grade, and no `fail` site joined the driver: its refusal ceiling is untouched.

The spec's line citations were resolved by symbol before the first edit; they had drifted with
TOOL-dPlacedRequest-15's lander (`derive_push_failure` and both loops sit lower in the tree than the
spec's ranges), and every symbol, flag and class the spec names was found as described. AC1 names the
slug `tFix`; the fixture is TOOL-dPlacedRequest-15's, whose lease is `fx`, and the arms use it.
The `refenced` line is S3's text verbatim, `push-main: the lease moved under this holder's own write;
re-fencing on <tip8> (attempt <n>/<max>)`, `<n>` the attempt it is about to make; AC1's "prints
`refenced`" is observed as that line.

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe script in the
run's scratch directory over a fixture under the node's short temp path, the shape of
TOOL-dPlacedRequest-15's lander fixture: a bare origin, clone A whose `.githooks/pre-push` is a stub
writing the allow record and running, once, a planted script from clone B, leases on, the lander
copied in and the driver beside it as a one-line launcher of this tree's driver, clone A's session
`sA` holding lease `fx` under fleet tag `a`.

**Evidences:** TOOL-dPlacedRequest-29
- AC1 — the planted script pushed the lease one commit on, parented on the tip, its record copied:
  git refused the atomic push (`cannot lock ref … is at <planted> but expected <tip read>`), the lander
  printed `push-main: the lease moved under this holder's own write; re-fencing on <planted8> (attempt
  2/3)` (PINNED), the second fence read fenced on the planted commit, and `--land --slug fx` exited 0
  (PINNED) printing `landed main`, no `re-preparing` line. The origin's default branch was clone A's
  HEAD, whose first parent was the pre-landing tip, and the lease tip's first parent was the planted
  commit.
- AC2 — the planted commit raised the epoch to 2 (PINNED) under session `sB`: the re-fence printed
  `lease refused — live-holder · fx/build · node a · session sB …`, the lander printed `push-main:
  fenced — the lease …` and exited 1 (PINNED), the default branch unmoved and the lease the planted
  commit.
- AC3 — over lease `f3`: the fence's own beat pushed onto the lease, `--after <old tip>` printed `fence
  — refs/gov/leases/f3/build <beat> <new beat>`, exit 0 (PINNED); an epoch-plus-one commit by the same
  session parented on the beat, `--after <beat>`, printed `lease refused — epoch-fence · f3/build ·
  node a · session sA …`, exit 1 (PINNED); a parentless commit carrying the beat's record, `--after
  <old tip>`, the same line, exit 1 (PINNED), while `--after` that parentless tip itself printed a fence
  line, so the refusal before it was the ancestry's.
- AC4 — `grep -n -- '--after\|refenced' tools/unattended/VERBS.template.md tools/push-main.sh` found the
  verbs guide's `fence` row naming `--lease fence build <slug> --after <tip>` and the lander's header
  naming `refenced`; `memory/guides/UNATTENDED-VERBS.md` is a byte-for-byte copy (`cmp` silent).
- S1 refusals — `fence build fNone --after <tip>` printed `lease refused — epoch-fence · fNone/build ·
  no lease on the remote`, exit 1 (PINNED); a 12-hex `--after` (PINNED) printed `lease not written —
  --after takes the full sha of the lease tip a fence read: …`, exit 2 (PINNED); `renew build f3
  --after <tip>` printed `lease not written — --after belongs to --lease fence alone`, exit 2 (PINNED);
  with `RUN_CLAIMS="off"` the plain fence still printed `fence — none · leases are off`, exit 0 (PINNED),
  and `--after` printed `lease refused — epoch-fence · f3/build · leases are off, so no lease
  re-fences`, exit 1 (PINNED).

**Owed at the close.**
- The `New arm:` line on `tools/push-main.test.sh`: arms 52 and 53, 2 (DERIVED) `ok`/`bad` pairs over
  a fixture made again after arm 51, the stub hook gaining a once-only planted script from clone B.
  RED-first against TOOL-dPlacedRequest-15's lander, which classifies both moves `fenced`, so 52 exits 1.
- The `New arm:` line on `tools/unattended/unattended.test.sh`: 7 (DERIVED) `same` assertions in the
  region-eight fence block, `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` each raised by 7 (DERIVED), and the
  DPR15 arm naming the fence act's usage line re-spelled with `[--after <tip>]`. RED-first against the
  fence act without `--after`, which refuses the flag. Waived for this build's landing by README rule 8,
  its clean reading owed with PLAY-dClosedLoop-14.
- The legs the spec's section 7 names.
