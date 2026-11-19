# TOOL-dPlacedRequest-13 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-13

The unit was built from its spec at rev-8 on base `eef993a22`. Each criterion below was observed by a
probe of this unit's own code: `tools/lib/gov-ref.sh` and `tools/lib/gov-feed.sh` sourced in a
scratch bare origin and two clones under the node's short temp path, `GOVREF_RUNNER` a plain runner,
once more under `bash -u` with the same results; and `scan_feed_writers` over the named files. No
gate, suite or bar ran in this pass; the arms the spec's §7 declares and their RED-first observations
are owed at the close.

**Evidences:** TOOL-dPlacedRequest-13
- AC1 — two writes of `refs/gov/runs/tFix` through `write_gov_ref` returned 0 and left two lines,
  `seq` 1 and 2, kind `runs`, blob `4b825dc642cb6eb9a060e54bf8d69288fbee4904`, each naming its commit;
  `git rev-parse refs/gov/remote/runs/tFix` printed the second. A third write from the first tip
  returned 1, `lost the race on the lease: [rejected] (stale info)`, and the file stayed at two lines.
- AC2 — `add_feed_event refs/gov/runs/tFix <second commit>` again left two lines; a scratch copy of
  the block with the key check replaced by `false` appended a third.
- AC3 — the second clone wrote the ref twice more; the first clone's fetch into `refs/gov/remote/runs/*`
  and `add_feed_sightings refs/gov/remote/` appended exactly those two commits as `seq` 3 and 4, oldest
  first, and a second call appended nothing. Through the driver, `--claims` in a clone holding the
  repository's conf (`RUN_CLAIMS="on"`) appended another clone's fresh claim by its sighting.
- AC4 — with the AC3 feed copied aside and deleted, `write_feed refs/gov/remote/` returned 0 and its
  ref, kind, blob and commit columns equalled the copy's; a second call returned 2 naming the feed.
  `check_feed refs/gov/remote/ <copy>` exited 0; with line 2 deleted it exited 1 printing
  `missing refs/gov/runs/tFix <that commit>`, and with line 2 doubled it exited 1 printing
  `duplicate refs/gov/runs/tFix <that commit>`.
- AC5 — with `refs/gov/remote/runs/tFix` deleted, `check_feed refs/gov/remote/ gov-feed.log` exited 0
  and every `tFix` line stayed in the file.
- AC6 — `print_feed 3` printed the lines whose `seq` is 3 and 4, in file order, and nothing else.
- AC7 — `scan_feed_writers` over `unattended.sh`, `post-merge.sh`, `push-main.sh` and `.githooks/pre-push`
  printed nothing and returned 0; over a copy of `unattended.sh` with a planted function pushing with
  `--force-with-lease` and no append, it printed that copy's planted line. Before the carriers held the
  join, the same scan printed both carriers' `write_gov_ref` push lines and named `add_feed_event` as no
  function of the files read. Over every tracked `*.sh` and hook less the suites it printed nothing.
- AC8 — `awk` cuts of the `gov_feed_sh` block from `gov-feed.sh`, `unattended.sh` and `post-merge.sh`
  compared equal by `cmp`, and `grep -c '^gov_feed_sh|' resolve-python.test.sh` printed 1.
- AC9 — over a scratch file whose function calls `add_feed_event` and runs a plain
  `git push origin "$c:refs/gov/mail/fx/a/s1"`, beside the two lib files, the scan printed that line;
  with `--force-with-lease=refs/gov/mail/fx/a/s1:` added it printed nothing, and over the AC7 files it
  still printed nothing.
- AC10 — an emptied `gov-feed.seq` beside a two-line feed: the next append's `seq` was 3 and the
  counter read 3; with the counter planted `1` the next was 4; a copy reading the counter alone gave 2,
  the staged repeat. With the last line cut to its first three fields and no LF by `truncate`, the next
  append landed on a line of its own with a `seq` above every earlier one, and `check_feed` exited 1
  printing `torn` and the cut line.
- AC11 — over a scratch file whose pusher calls `my_join`, whose body calls `add_feed_event`, the scan
  printed nothing with `my_join` on `FEED_WRITER_HELPER_FNS` beside the shipped entries, printed the push
  line once it was removed, and printed `FEED_WRITER_HELPER_FNS names no_such_fn(), which is no function
  of the files read` with that entry added. `grep -c scan_feed_writers` over each cut printed 0.
- AC12 — `--feed` has a `- `--feed` — ` row in `VERBS.template.md`, an `unattended.sh --feed check`
  line in `SKILL.template.md` and three `#   unattended.sh --feed` header lines; the rendered Skill
  measures 11051 bytes CR-stripped and its row in `tools/template-size-limits.txt` reads 11051. (DERIVED)

The deletion form: `remove_gov_ref` over the probe's ref appended a line with blob `-` and 40 zeros,
and the cache ref was cleared. The driver's `--feed check`, `--feed print --from 5`,
`--feed print --from` (exit 2), `--feed rebuild` over a live feed (exit 2) and an unknown subverb (exit 2)
each answered as the verb row states.

## Owed at the close

- The two `New arm:` lines of the spec's §7, each RED-first: `tools/lib/resolve-python.test.sh` (the
  `gov_feed_sh` parity row and arm 2o, staged by a planted pushing function with no append and by a
  declared helper removed from the list), and `tools/unattended/unattended.test.sh` (the change feed
  block in region eight, under README rule 8's waiver, whose floors rose by its assertions).
- The legs §7 names, run once by the main loop; `govkit selfcheck --write` rewrote no subject pin in
  this pass.
