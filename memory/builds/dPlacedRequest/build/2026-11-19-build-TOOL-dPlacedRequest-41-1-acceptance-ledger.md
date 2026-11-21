# TOOL-dPlacedRequest-41 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-41

The unit was built from its spec at rev-3 on base `7c7516c16`. The offline branch of (PINNED)
`tools/unattended/unattended.sh#run_lease_verb` now takes `gov-queue.lock` through
`tools/unattended/unattended.sh#write_gov_queue_hold` before it reads anything, reads the ref's newest
queued commit through `tools/unattended/unattended.sh#read_gov_queue_head`, and hands it to
`tools/unattended/unattended.sh#read_claims` as `CL_QUEUED`: a `cached` read then reads that commit's
record in place of the ref's cached tip, with one `git cat-file`, and moves no ref (S1). Every exit
of the verb after the take releases the hold through
`tools/unattended/unattended.sh#remove_gov_queue_hold`, which replaces the `WL_QUEUE=""` reset at each
of them. `tools/unattended/unattended.sh#add_gov_queue` uses the hold where its caller holds it, takes
the lock itself otherwise, and returns 3, appending nothing, only where the write was built on the (PINNED)
ref's newest queued commit and the two records, less `beat-utc`, `last-fetch` and `renews`, are equal:
one `git log --no-walk=unsorted` over both commits (S2). The ref-and-cached-tip key is gone.
`tools/unattended/unattended.sh#write_gov_queue` keeps one state per ref: a line after a kept line of
its ref stays queued unpushed, and a line after a yielded one prints its own `yield` and logs its own
`lease-yielded` event, resolved (S3). Section 7 of `tools/unattended/STOPS.template.md` names the (PINNED)
chain, and `memory/guides/UNATTENDED-STOPS.md` is its byte-identical render.

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe script in the
run's scratch directory over a fixture of TOOL-dPlacedRequest-1 AC7's shape, built under the node's
short temp path: a bare origin, one clone with `RUN_CLAIMS=on`, `USERNAME=daily-agent`, session `s1`,
the suite's own `mkconf`, `write_lease_fixture`, `run_lease_arm` and `read_lease_field` read out of
`tools/unattended/unattended.test.sh` by `awk`, and the origin renamed away after one read that
answered stamped `gov-last-fetch`.

**Evidences:** TOOL-dPlacedRequest-41
- AC3 — the first offline `--lease acquire build tOff` printed `lease — tOff/build · queued · epoch 1`; (PINNED)
  the second printed `lease — queued — already · tOff/build`, both exiting 0, and (DERIVED)
  `grep -c '' gov-queue.log` printed 1. (DERIVED)
- AC1 — `--lease release build tOff --as withdrawn` offline then printed
  `lease — tOff/build · queued · epoch 1` and exited 0; the queue held 2 lines, the second's (DERIVED)
  expected-tip field equal to the first's commit, and `git rev-parse <second commit>^` printed the
  first commit. No `gov-queue.lock` remained after the verb.
- AC2 — with the origin restored, `--lease flush` exited 0 printing two `flushed` lines; the origin's (DERIVED)
  `refs/gov/leases/tOff/build` read `status: withdrawn` with the acquire commit as its parent, and the
  queue held 0 lines. (DERIVED)
- AC4 — `tOff2`'s offline acquire and release queued 2 lines; a foreign commit planted on the origin's (DERIVED)
  ref, the flush printed `yield` for both lines, the second naming that an earlier queued write of it
  yielded, the health log gained 2 `lease-yielded` lines, the origin kept the foreign commit, and the (DERIVED)
  queue held 0 lines. (DERIVED)
- The staged red, the base's driver: a checkout of `7c7516c16`'s `tools/` in a scratch repository, the (PINNED)
  same probe printed `lease not written — tOff/build holds no lease to release` for the release, 1 (DERIVED)
  queue line, and after the flush the origin's tOff read `status: live`, the lease the node released (DERIVED)
  still held; tOff2's flush yielded 1 line and left the release unqueued. The spec's red-when names (DERIVED)
  `queued — already`, the base's reading where the cached tip already holds the ref; over a create the
  base refuses the release instead, and either way the remote ends held.
- The new arm's own readings — a second probe mirroring the arm's commands line for line printed, for
  the shipped driver, `n3=1`, `queued — already`, `ac1=2 tip parent`, (DERIVED)
  `ac2=0 withdrawn parent live 2 0` and `ac4=2 2 foreign`, the tOn chain landing a take at epoch 2 on (DERIVED)
  its queued release; and for the arm's staged copy, whose cached read never reads the queued commit,
  `rel=lease not written — tOff/build holds no lease to release`, a first `ac1` field equal to `n3`,
  and `ac2=0 live no-parent released 1 0`: neither origin ref in its last act's state. Both staged (DERIVED)
  lines read once in the copy. (DERIVED)
- `bash -n` read both changed shell files clean. Three functions were minted, each named through the
  naming lexicon first: `read_gov_queue_head`, `write_gov_queue_hold` and `remove_gov_queue_hold`.
- The bug-class checklist over the pass commit selected 53 classes. One needed a change: (DERIVED)
  `refusal-branch-with-no-arm`, since S3's keep, the line after a kept line of its ref, had no arm.
  The block now drives it: tOk's offline acquire and release queued, then a first policy revision
  whose `leases.queued-claim-days` is out of range, so the flush keeps the first line by the bound.
  A probe mirroring the arm read `2 2 1` for the shipped driver, exit 2, both lines kept and one (DERIVED)
  line naming the chain's keep; and `2 2 0` for a copy with the rule's case renamed away, which (DERIVED)
  keeps the second line by the bound alone. The rest needed none: the offline branch's busy refusal
  is TOOL-dPlacedRequest-24's AC3 arm, and the chain's yield line is hit by AC4's arm; every count is
  `grep -c` over a file or over `grep -c .`; every staged copy is checked to carry its staged line;
  the doc sentence changed has no reader by its old spelling.
- The codebase map's `gen_map.py --write` refused the pass commit's arm: its shell parser read a
  single-quoted replacement inside a `${…/…/…}` expansion as an unterminated `${`. Each staged
  copy now takes its replacement from a variable, as TOOL-dPlacedRequest-17's copies do; a probe of
  the two substitutions read each copy carrying its staged line once and `bash -n` clean, and the
  map re-rendered with `symbols.json` changed for the three new functions.

## Owed at the close

- The spec's `New arm:` line: `tools/unattended/unattended.test.sh`, the region-8 (PINNED)
  TOOL-dPlacedRequest-41 block in a compound block of its own, 13 executed assertions (9 `same`, 4 (DERIVED)
  `hit`), no skip branch; `FLOOR_ASSERTIONS` 3724 to 3737 and `FLOOR_SHARD_8` 955 to 968. Its (DERIVED)
  RED-first observation inside the suite is the close's; waived for this build's landing by README
  rule 8. (PINNED)
- TOOL-dPlacedRequest-24's region-8 AC1 and AC3 arms over the changed append, and TOOL-dPlacedRequest-1 (PINNED)
  AC7 and TOOL-dPlacedRequest-16 AC6, AC7 and AC10 over the changed queue, read by the suite at the close.
- The positional citations of `tools/unattended/unattended.sh` past the queue section, which this (PINNED)
  pass's added lines move, read by the pass legs.
- The legs the spec's Gates section names, run once by the main loop.
