# TOOL-aRatifiedRulings-1 — acceptance ledger

**Serves:** journal TOOL-aRatifiedRulings-1

Every observation below was made on node `a` on 2026-09-13 over the working tree this unit
commits, unless a line says otherwise. The two suite files AC4 reads are named by path so a later
reader can re-derive the counts rather than trust them.

**Evidences:** TOOL-aRatifiedRulings-1
- AC1 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — prints `kit-parity: shipped and installed docs agree (4 pairs, rendered for 'tools/memory-tree')`, exit 0, after `--render` re-made all four live docs from their templates. `grep -cF "CONVERGED is terminal for its subject"` prints `1` over `memory/guides/BUILD-METHOD.md` and `1` over `tools/memory-tree/BUILD-METHOD.template.md`; `grep -cF "by anything but that review's own fold"` prints `1` over each. The `Red when:` half was not re-staged here: section 4 records the render-only edit producing `DRIFT` on 2026-09-13 at base, and this pass edited the template and rendered, so the DRIFT path was never entered
- AC2 — `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` — prints `template-size OK — BUILD-METHOD.md: 26743 / 27648 bytes (905 under, 96.7%)` and no `TEMPLATE-SIZE WARN` line; `wc -l` prints `340`. Both figures are the ones section 4 pinned from the staged measurement, reproduced exactly, and 26743 is 198 under the 26941 row in `tools/template-size-highwater.txt`, so no `--bump` was owed and none was made
- AC3 — `python3 tools/memory-tree/check-arms.py --check` — with the message at `unattended.sh:4096` extended and both arms still quoting the old text it exited 1 with one line, `tools/unattended/unattended.sh:4096 check 37 branch 10 has no POSITIVE assertion naming its own failure text ("...a blocker confirmed on it now is DISPOSED under the build method's M4, fold or promote, and never re-rounded") and is not pinned`. With the two arms moved and the new arm added it exits 0 printing nothing, and `--report` lists `check 37 branch 10  line 4096  ARMED`. The staged half was observed BEFORE the arm edit was made, as the criterion's fixture note requires
- AC4 — `bash tools/unattended/unattended.test.sh --shard 2/2` — run twice with `> <file> 2>&1`, once over a frozen copy of the kit dir holding the landed driver and once over a copy whose `unattended.sh:4096` message was reverted to the base text (`git show HEAD:tools/unattended/unattended.sh` at `da9b9a33`). The reverted run's file holds `FAIL missing:` followed by the new signature exactly 3 times and the landed run's file holds it 0 times; both hold `MARK review-loop` once. Whole-file `^FAIL` counts are 56 and 53, and the sorted set difference between them is exactly those three lines plus one `PROTOCOL.template.md` line that differs only by the copy's path — the shard's pre-existing failure population `TOOL-aTracedSpawn-3` names, identical on both sides, which is why the exit status (1 on both) is not the observation. Neither file carries `FAIL executed`, so both runs cleared the 510 shard floor. Wall clock 1808 s and 1805 s, run concurrently
- AC5 — `review · item C1 · reason` — in the landed run the new block's `hit` and `same` both passed: the file carries no `FAIL missing:` line for the signature and no `FAIL a refused round on a converged subject wrote nothing` line, and the region's `MARK review-loop` is present. The positive artifact that the block RAN rather than being skipped is the reverted run over the same suite bytes: its third `FAIL missing:` is followed by `GOT: UNATTENDED check 37 FAILED — ...would rewrite that history: C1`, which is branch 10 refusing subject `C1` — reachable only after round 1 recorded a terminal token for `C1`, so the `CLEAN WITH FIXES` round at zero blockers was written as `CONVERGED` and the `BLOCKED` round was refused rather than recorded. The `same` arm read `1` in both runs, never `2` or `0`
- AC6 — `bash skills/session-kickoff/manifest-check.sh` — exits 0 over the staged tree with `last-audit` re-stamped to `2026-09-13T16:22:17+03:00 @ 9fac2b53b625032b93be6a09c0bf99f912ae35dd`, the sha being `git merge-base origin/main HEAD` per the stamp rule, and the commit message carries the delta line. `--staged` from the pre-commit hook exits 0 as well. Two watched files move in this commit, `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/check-memory-hygiene.sh`, so check 5 had two reasons to red without the stamp
- AC7 — amended rev-4 — the criterion expected `kit-versions: 0 problem(s)` on stdout, a line `tools/check-kit-versions.sh` never prints: its only summary line is failure-only at `:270` behind `[ "$fails" = 0 ] && exit 0`. Section 9's rev-4 line logs it. What the corrected criterion asks was observed: `bash tools/check-kit-versions.sh` exits 0 with empty stdout; `KIT_MEMORY_TREE_VERSION=2.70` at `check-memory-hygiene.sh:20` with its same-line marker; all four tracked `tools/memory-tree/*.template.md` markers read `gov:kit memory-tree@2.70`; `grep -c '^KIT_UNATTENDED_VERSION=1\.19 ' tools/unattended/*.sh` reports `1` for exactly `unattended.sh`, `check-unattended.sh`, `check-pass-order.sh` and `check-brief-recorded.sh` and `0` for the other eleven files. The `-G` join and the epoch gate's second clean form need the pass commit to exist and are recorded in the follow-up section below

## How the two AC4 runs were staged

Each run is `bash <copy>/unattended.test.sh --shard 2/2 > <file> 2>&1` over a frozen copy of
`tools/unattended/` taken after the driver and suite edits were final, so no later edit to the
worktree could reach either run and the two copies differ in exactly one line, the branch 10
message. The suite anchors on `$HERE` alone — every path it reads is `$HERE/<kit file>` — which is
what makes a directory copy a complete fixture. The copies and their output files sat under a short
root in the user temp directory rather than the session scratchpad, because that path length is a
recorded trap on this node. The two output files are not committed: the figures above are what
they hold, and a reader re-deriving them re-runs the pair.

## Observed after the pass commit existed

The `-G` join in AC7 and the epoch gate's second clean form are properties of the commit and could
not be observed before it was made. The records commit that follows the pass commit appends them
to this ledger, below this line.
