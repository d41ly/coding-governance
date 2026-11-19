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
The `refenced` line is S3's text verbatim,
`push-main: the lease moved under this holder's own write; re-fencing on <tip8> (attempt <n>/<max>)`,
`<n>` the attempt it is about to make; AC1's "prints
`refenced`" is observed as that line.

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe script in the
run's scratch directory over a fixture under the node's short temp path, the shape of
TOOL-dPlacedRequest-15's lander fixture: a bare origin, clone A whose `.githooks/pre-push` is a stub
writing the allow record and running, once, a planted script from clone B, leases on, the lander
copied in and the driver beside it as a one-line launcher of this tree's driver, clone A's session
`sA` holding lease `fx` under fleet tag `a`.

**Evidences:** TOOL-dPlacedRequest-29
- AC1 — the class was `refenced`, not `fenced`: the planted script pushed the lease one commit on,
  parented on the tip, its record copied; git refused the atomic push (`cannot lock ref`), and the
  lander printed `the lease moved under this holder's own write` with
  `re-fencing on <planted8> (attempt 2/3)` (PINNED). The second fence read fenced on the planted
  commit, and `--land --slug fx` exited 0 (PINNED) printing `landed main`, with no `re-preparing`
  line. The origin's default branch was clone A's HEAD, whose first parent was the pre-landing tip,
  and the lease tip's first parent was the planted commit.
- AC2 — the class was `fenced`: the planted commit raised the epoch to 2 (PINNED) under session `sB`;
  the re-fence printed `lease refused — live-holder · fx/build · node a · session sB …`, the lander
  printed `push-main: fenced — the lease …` and exited 1 (PINNED), the default branch unmoved and the
  lease the planted commit.
- AC3 — over lease `f3`, the fence's own beat pushed onto the lease: `--after <old tip>` printed
  `fence — refs/gov/leases/f3/build <beat> <new beat>`, exit 0 (PINNED). An epoch-plus-one commit by
  the same session parented on the beat, read with `--after <beat>`, printed
  `lease refused — epoch-fence · f3/build · node a · session sA …`, exit 1 (PINNED). A parentless
  commit carrying the beat's record, read with `--after <old tip>`, printed the same `epoch-fence`
  line, exit 1 (PINNED), while that parentless tip handed as its own `--after` printed a fence line,
  so the refusal before it was the ancestry's.
- AC4 — `grep -n -- '--after\|refenced' tools/unattended/VERBS.template.md tools/push-main.sh` found
  the verbs guide's `fence` row naming `--lease fence build <slug> --after <tip>` and the lander's
  header naming `refenced`; `memory/guides/UNATTENDED-VERBS.md` is a byte-for-byte copy (`cmp` silent).
- S1 refusals — `fence build fNone --after <tip>` printed
  `lease refused — epoch-fence · fNone/build · no lease on the remote`, exit 1 (PINNED). A 12-hex
  (PINNED) `--after` printed `lease not written — --after takes the full sha of the lease tip a fence read: …`,
  exit 2 (PINNED). `renew build f3 --after <tip>` printed
  `lease not written — --after belongs to --lease fence alone`, exit 2 (PINNED). With
  `RUN_CLAIMS="off"` the plain fence still printed `fence — none · leases are off`, exit 0 (PINNED),
  and `--after` printed `lease refused — epoch-fence · f3/build · leases are off, so no lease re-fences`,
  exit 1 (PINNED).

**Owed at the close.**
- The `New arm:` line on `tools/push-main.test.sh`: arms 52 and 53, 2 (DERIVED) `ok`/`bad` pairs over
  a fixture made again after arm 51, the stub hook gaining a once-only planted script from clone B.
  RED-first against TOOL-dPlacedRequest-15's lander, which classifies both moves `fenced`, so 52 exits 1.
- The `New arm:` line on `tools/unattended/unattended.test.sh`: 8 (DERIVED) `same` assertions in the
  region-eight fence block, `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` each raised by 8 (DERIVED), and the
  DPR15 arm naming the fence act's usage line re-spelled with `[--after <tip>]`. RED-first against the
  fence act without `--after`, which refuses the flag. Waived for this build's landing by README rule 8,
  its clean reading owed with PLAY-dClosedLoop-14.
- The legs the spec's section 7 names. The push-main self-test's budget row was not re-priced: arms 52
  and 53 add one fixture and two stub-hook landings, one of them retried, and no bar runs inside them;
  the first measured run at the close says whether the row moves.

**The checklist, acted on.** The bug-class checklist over the pass commit selected 51 (DERIVED) classes
by anchor and 6 (DERIVED) universal. Three needed a change or a check.
heredoc-escape-reaches-the-regex: the pass's own scripted edit of the lander suite turned two `printf`
lines' `\n` and line continuations into raw bytes; both were rewritten with the edit tool before the
commit, and a scan of the pass commit's `tools/` diff for control bytes found none.
fixture-passes-by-finding-nothing and liveness: the off-chain refusal could have been the epoch's or
the read's; the driver block gained an 8th (DERIVED) assertion, the parentless tip as its own `--after`
re-fencing, so the refusal before it is the ancestry's. refusal-branch-with-no-arm: every new driver
refusal (`--after` no full sha, `--after` on another act, leases off, no lease, a later epoch, an
off-chain tip) has a `same` arm, and the lander's two classes have arms 52 and 53. Branches still with
no arm, named: a re-fence answered `fence — none`, which the driver never prints under `--after`, read as
`fenced`; and a re-fence that the attempt bound then exhausts, which reaches today's "moving faster than
the gate" line. staged-break-substitutes-a-synthetic-value: the AC1 plant copies the tip's record
unchanged rather than running a real `--beat`, whose record differs in `beat-utc` and `renews` only,
neither of which the re-fence reads. inherited-git-dir-pins-the-work-tree-to-the-cwd: the hook's
planted script unsets `GIT_DIR` and `GIT_WORK_TREE` before it enters clone B. The rest read clean: the
ancestry match is whole-line equality, the re-fence is the driver's one bounded read, and no table cell
or fence was written.
