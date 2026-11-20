# TOOL-dPlacedRequest-52 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-52

The unit was built from its spec at rev-10 on base `ce4a81a9a`. Built: S3 and S4, the placed race's
attempt loop in `tools/unattended/unattended.test.sh`; S19, the skip signal in
`skills/session-kickoff/manifest-check.sh#run_driver_bounded` and its four callers; S20, the guarded
trap of `tools/lib/gov-feed.sh#add_feed_event`, its header, the three carried copies and the release
plant's text in `tools/lib/resolve-python.test.sh`; S25 and S26, the trimmed `renews:` match in
`tools/unattended/unattended.sh#read_claims` and the `DPR46 AC3` loop's three new tips. S5, S9 and S10
are observed by probe or owed. No gate, suite or bar ran in this pass. Every reading below is a probe
of the changed code: a cut of a function or a loop sourced over a stub, or an `awk` or `grep` over a
file, each run under the session scratch or the node's short temp path.

**Evidences:** TOOL-dPlacedRequest-52
- AC5 — `awk '/^write_request_record\(\)/{f=1} f; f&&/^}/{exit}'` over the driver, then `grep -n 'cp -- '`, printed one line naming `$key.md.$$`, after the `write_dir_lock_wait` line and before the `remove_dir_lock` line of the cut. (DERIVED)
- AC10 — `sed '/^## 9\./,$d'` over spec 43 piped to `grep -o 47104 | wc -l` printed 0, and the same cut holds `read_size_ceilings`. (PINNED)
- AC19 — the four callers and `resolve_card_driver`, cut from the engine and sourced over a stub driver that prints `FAILED: boom` and exits 125, with CARD_REF_WHY holding a stale reason: the claims cell printed `claims — skipped: FAILED: boom`, the overlaps cell `overlaps — skipped: FAILED: boom`, and the lookup set `--card-ref lookup exited 125 and printed no card-ref line`. (DERIVED)
- AC19 — the same cut with no `.unattended.conf` printed `claims — skipped: no .unattended.conf in this tree`, and so did the overlaps cell and the lookup. (DERIVED)
- AC19 — RED: the engine at HEAD, cut the same way, printed `claims — skipped: a stale reason from an earlier lookup`, and its lookup kept an empty reason. (DERIVED)
- AC20 — the canonical `gov_feed_sh` cut, sourced in its own shell that arms the trap line read from it, takes the lock with `write_dir_lock`, then stages a peer: with the `.break` guard made and the lock re-made with no `owner` the lock was kept; with no guard and no `owner` it was cleared; with `owner` reading another token it was kept; with nothing staged, this writer's own, it was released. (DERIVED)
- AC20 — RED: a copy whose trap drops the guard test cleared the guarded lock. (DERIVED)
- AC3 — the attempt loop, cut from the suite and sourced over a stub `run_request_arm` whose B appends a `node-lock-broken` line naming `requests.lock` on the first attempt, printed that attempt discarded as a placement overrun naming `node-lock-broken on requests.lock`, and kept the second. (DERIVED)
- AC4 — the same cut, its bound read from a stub driver line `NODE_LOCK_BOUND=1`, with B sleeping past it on the first attempt only, discarded that attempt with its seconds and kept the second; with B sleeping past it on every attempt it printed three discards and the row read `request race placed past the lock bound`; `jobs -p` printed nothing after each. (DERIVED)
- AC4 — with no `held` announced, the same cut stopped after one attempt and read `request race never placed`. (DERIVED)
- AC26 — the new match line run alone over `renews:`, `renews: `, `renews: yes ` and `renews:no` read the values empty, empty, `yes` and `no`. (DERIVED)
- AC26 — `git commit-tree -m` kept the trailing space of a `renews: ` line and the bare `renews:` line, read back by `git cat-file -p`, git on node a. (PINNED)
- AC25 — the suite's two scratch copies built from the driver alone: the stop-on-any copy carries `rn[c] != "no"` once and the yes stop not at all, and the space-match copy the old match once and the trimmed match not at all. (DERIVED)

## Readings beside the criteria

- The four `gov_feed_sh` copies read one `cksum` after the splice, as unit 49 left them before it. (DERIVED)
- The release plant's text in the resolver suite matches one line of the canonical, `grep -cxF` printing 1. (DERIVED)
- `bash -n` read every changed shell file clean. (DERIVED)
- `gen_map.py --write` changed nothing: the diff mints, renames and deletes no function. (DERIVED)

## Items diverged

- S19 names the fourth caller `write_card`; the tree's fourth caller of `run_driver_bounded` is `write_build_card`, the publish, and `write_card` calls the driver nowhere. Built over the four callers the item defines by their call, the publish's arm included.
- The trap sketch in the spec's section 4 wraps the trap over two lines with a `\`; the trap is built on one line, the shape the `DPR39` and `DPR49` mutations anchor on, which the same section says the new line keeps.
- AC9 is not observed here: its `size join` line is the spec-tokens leg's output, which a role agent may not run. Spec 7 and spec 34 measure over the cap the criterion pins; whether the join reads them as live is the leg's.

## Owed at the close

- AC9, by the `spec tokens` leg.
- AC1, AC3, AC4, AC20, AC25 and AC26 in the suite run, and each `New arm:` line's RED-first observation: the race block's staged sleep of 11 s (PINNED) after `pr_t0` on the first attempt and on every attempt, and AC1 with `SCRIPT` at `3fc16744c`; the trap arm's unguarded copy; the renews loop's two copies.
- AC19's suite arm in `manifest-check.test.sh`, and its RED against callers reading rc 125 alone.
- The legs the spec's Gates section names, run once by the main loop.
