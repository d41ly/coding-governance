# TOOL-dPlacedRequest-34 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-34

The unit was built from its spec at rev-13 (PINNED) on base `be1af09ba`, a sweep of the round-1 spec
audit's minors written before most of this run's units landed. Each item was probed against the tree
first: where a later unit had already done the work, no code changed and the probe is recorded below;
where it was owed and buildable it was built; S41 conflicts with the tree and is listed under "Items
diverged"; S43 and S47 are owed and were not built in this pass. The spec therefore stays INPROGRESS.

No gate, suite or bar ran in this pass, and no `--selftest`. Each observation below is a probe of the
changed code on the run's node, 2026-11-20: an in-process call, the driver or a kit CLI over a scratch
fixture, or the unit's own `card-store.fixture.sh --plant <case>`. A criterion only a gate or a suite
observes, and every `New arm:` line's RED-first reading, is the close's (the build method's M8).

## What was built

- **S4** — `tools/unattended/unattended.sh#read_feed_lease_tip` prints `unreadable <commit>` for a feed
  commit git cannot read; `tools/unattended/unattended.sh#write_claim` refuses a build or unit create
  over it (return 1, `epoch-fence` at the verb) and gives a cadence or legacy claim the plain create.
- **S5, S6** — `write_feed_success` is minted in the `gov_feed_sh` block of `tools/lib/gov-feed.sh`:
  it sets or clears the cache ref, prints one `feed: NOTE -` line where git cannot move it, and appends.
  `tools/lib/gov-ref.sh#write_gov_ref`'s success exit calls it, it joins `FEED_WRITER_HELPER_FNS`, and
  `tools/push-main.sh#write_effect_push` calls it for the fenced beat. Both blocks were copied byte for
  byte into `tools/unattended/unattended.sh`, `tools/run-gates/post-merge.sh` and `tools/push-main.sh`.
- **S7 to S13** — the driver gains `--card-ref lookup <slug>`
  (`tools/unattended/unattended.sh#print_card_ref`): read-only, the remote `resolve_claim_remote`
  resolves, the write's pruned glob fetch into `refs/gov/remote/builds/<slug>/*` with
  `--no-write-fetch-head`, then the sightings. The kickoff engine's
  `skills/session-kickoff/manifest-check.sh#read_card_ref` runs it
  under `timeout -k 2 "$CARD_FETCH_BOUND"`, stdin closed, through `skills/session-kickoff/manifest-check.sh#resolve_card_driver`;
  R7, the stored-card read and the replay's re-key read the cache ref; the local ref and its
  `update-ref` are gone; the engine's inline `gov_feed_sh` block is removed. The fetch spells the glob
  `+refs/gov/builds/<slug>/*` the write already uses rather than S12's single refspec, because a single
  refspec over an absent card exits non-zero through `observe_remote`, which discards stderr, so "no
  card" could not be told from "no answer"; the cache ref it lands is the same name.
- **S14, S15** — already in the tree (unit 21): no queue, no folder; no code changed.
- **S16, S17** — `tools/lib/gov-feed.sh#scan_feed_writers` joins `\`-continued lines, skips comments,
  judges each function and each file's top-level body as a scope, flags a scope holding a push and a
  lease flag anywhere in it with no helper call, and reads both limbs over the joined lines. Its push
  word no longer matches inside `push-main`.
- **S22** — `--lease status <kind> <name> [<sub>]` (`tools/unattended/unattended.sh#print_lease_status`)
  prints one TAB-separated line with the holder's session; `tools/loop/placement.py#read_build_lease`
  reads it and admits a live or held lease only under this node's tag AND this session.
- **S23** — every `--lease` act but `fence` prints `lease — off · <tail>` and exits 0 with RUN_CLAIMS
  off; the prune arm of the driver suite that read exit 2 now reads that line.
- **S24** — the pre-push fast path in `.githooks/pre-push` asks `<sha>^^{tree}` in its one batch and
  admits a `tree 0` candidate whose first parent is missing or is a `tree 0` commit.
- **S26, S27, S35** — `memory/map/features/unattended-stops.md` and the claim readers name
  `refs/gov/leases/<slug>/build`; the gotcha `decision-re-derived-by-a-second-process` gains its dated
  paragraph and no longer calls the lock live; the resume-tick arms read the lease ref.
- **S28** — `tools/hooks/scratch-guard.js#resolveCardBash` runs each candidate in
  `tools/policy/policy-mirror.js#resolveBash`'s order with `test -f` on the checker;
  `tools/hooks/scratch-guard.js#readCard` folds through `tools/hooks/scratch-guard.js#buildNativePath`.
- **S29, S30** — `tools/playbook/render_playbook.py#read_fleet_tag` takes GOV_NODE as `node` and no host;
  `--fleet-tag` takes `--fleet <path>` and `--node`; `tools/unattended/lib-unattended.sh#resolve_fleet_tag`
  passes GOV_NODE and no `--host`.
- **S34** — `tools/loop/loop_lib.py#load_tree_lib` takes a module and its `need` tuple; `request.py`,
  `read_actor_base`, `read_builds_dir` and `loop_items.py` reach the memory-tree kit only through it or
  its loader.
- **S36, S46** — `skills/session-kickoff/RESUME.md` holds units 2, 3 and 9's card and resume text and
  the ordered `restart-item` act; `SKILL.md` points there in one line.
- **S42** — `placement.py` prints `placement: pre-claim draw not recorded — <why>` on a draw that
  answered exit 2; `tools/unattended/unattended.sh#run_entry_claim` exits 2 on a route-back draw not
  recorded.
- **S48** — `--path-tokens --files-touched --any-status` reads a terminal spec;
  `tools/loop/loop_lib.py#resolve_item_seed` passes it and prints
  `unarmed — write-set: <spec> lists no path` on none.
- **S49, S54** — `tools/unattended/unattended.sh#check_claim_writable` refuses an offer over any open
  offer `offered` and over a build or unit tombstone `tombstone`; `run_lease_verb` refuses a `--to`
  naming the caller's own tag or session. The driver suite's unit-20 arm that read `terminal` over a
  unit tombstone now reads `tombstone`.
- **S50** — `tools/govkit/steps/kickoff_facts_to_overlay.py#parse_fact_bullets` joins a bullet's lines
  indented two or more spaces.
- **S55** — the cadence parity arm reds `unarmed — tag_index.py does not resolve` instead of counting
  two assertions it never ran.

## Already satisfied by the tree

S1 (unit 27), S2 and S3 (unit 28), S18 (unit 10's plant asserts the exact six lines), S20 (unit 3),
S21 (unit 14's plant), S31 and S32 (both legs carry subject, chunk, ceiling and `enforces`, pinned and
claimed), S33 (unit 24's guarded break), S37 (the verbs guide names the `placement` source), S39
(`released` ranked and hidden), S40 (`-` written and mapped back), S44 and S45 (unit 12), S51
(thirteen, DERIVED, `seed =` rows in `tools/loop/loop.toml`), S52, S53, S56 and S57 (the design
record), S58, S59 (no commit of this build hand-bumps a version).

## Items diverged

- **S41** — the tree's `tools/unattended/unattended.sh#run_request_draw` (unit 14) creates an absent
  request record from the clone's kept copy `<git-common-dir>/requests/<key>.md` and refuses naming
  `--request <file>` with neither; S41 adds a `--request-text <file>` driver flag for the same act.
  Building it adds a second path to one act and a changed usage line. Options: (a) restate S41 and AC41
  over the kept copy, the tree's design; (b) add the flag beside it.

## Owed, not built in this pass

- **S43** — the streaming, early-stopping age walk in `read_claims`; its stops are ordered with the
  tenure by unit 35, still DEFERRED.
- **S47** — the probe pin's recorded head blob and the `<key>.probe-2.md` re-trigger in
  `tools/loop/probe.py#write_probe_pin`.

First-pass readings, restated one criterion per line in the block that closes this record:
- AC1 — over a scratch bare remote, a create, a `remove_gov_ref`, a re-create and a second delete of
  `refs/gov/runs/tFix` left 2 (DERIVED) deletion lines in `gov-feed.log`.
- AC5, AC6 — owed to the close: the driver suite's feed arm and `tools/push-main.test.sh`'s fenced
  landing. The cmp of every `gov_feed_sh` and `gov_ref_sh` copy against its canonical cut read equal.
- AC7 — `card-store.fixture.sh --plant terminal-route` held: a route to the terminal build refused R7
  with no lookup, the card unchanged.
- AC8, AC10, AC13 — the three greps over the working tree printed nothing.
- AC9 — `--plant lookup-upstream` held: a clone whose one remote is `upstream` read the card re-derived.
- AC11 — `--plant lookup-hung` held: `evidence` with 4 s (DERIVED) over the control, a bound of 4 s (PINNED, `CARD_FETCH_BOUND`)
  (PINNED) plus 3 s (PINNED).
- AC12 — `--plant replay` held: `FETCH_HEAD`'s mtime unchanged. `lookup`, `lookup-offline`, `publish`,
  `publish-off`, `publish-unwritten` and `publish-hung` held too.
- AC16, AC17 — the census flagged a top-level writer, a wrapped push at its first line, an array-held
  lease and a wrapped plain push of `refs/gov/mail/fx/a/s1`; over `tools/push-main.sh` it named only the
  helper the file does not define, and over every carrier with both libs it printed nothing.
- AC22 — owed to the close: two sessions over one remote lease. `--lease status build tFix` with leases
  off printed `lease — off · tFix/build`.
- AC23 — acquire, flush and prune printed `lease — off · <tail>` and exit 0; fence printed
  `fence — none · leases are off`.
- AC24 — over a scratch repository the predicate admitted a parentless claim and a claim parented on a
  claim and refused an empty-tree commit on a file commit; AC25's staged base is the close's arm.
- AC26, AC27 — `git grep claim-push.lock` over the features and gotchas hits only the dated paragraph,
  which names `TOOL-dPlacedRequest-11`.
- AC28 — a `node -e` probe of `readCard` with a non-running `bash.exe` first on PATH and Git's second read
  the card a stub checker printed as `/c/…`; a silent checker read as no card, named.
- AC30 — `D41LY` resolved `d`; GOV_NODE `c` resolved `c` for an unknown user; GOV_NODE `zz` refused
  naming GOV_NODE.
- AC34 — `git grep -F 'resolve_kit_dir("memory-tree"' -- tools/loop/` printed only
  `tools/loop/loop_lib.py#read_memory_tree`; `load_tree_lib("row_grammar", (…, "no_such_name"))`
  raised the named LoopError; `request.py key` keyed a text.
- AC35 — the greps over S35's files print only legacy-read mentions.
- AC36 — `SKILL.md` measures 18354 (DERIVED) of its row's 18432 (PINNED); the pointer is found.
- AC37 — the protocol measures 68369 (DERIVED) of its row's 68374 (PINNED).
- AC38 — `gen_map.py --write` ran; `grep -c check_claim_push_clear` printed 0 (DERIVED).
- AC44, AC45 — a subject holding a newline printed `the subject carries a control byte`, exit 2; an
  encoded subject over 200 bytes (PINNED) was refused; a held `<common>/refs/gov/remote/runs/tFix.lock`
  gave rc 0, 1 (DERIVED) `feed: NOTE -` line and the event appended.
- AC46 — `git add -A`, the `-2` suffix, `git rev-parse` and "restore only after" are found in that order.
- AC48 — `resolve_item_seed` over CLOSED `TOOL-dPlacedRequest-3` printed its paths.
- AC49 — `--to a` and `--to a/s1` under session `s1` on tag `a` exited 1 `offered`; the open-offer and
  other-session halves are the close's arm.
- AC50 — a wrapped bullet's row text carried all three lines joined.
- AC56 — this node's one cached lease commit measured 525 bytes (DERIVED), 16.7% (DERIVED) under the
  record's 630 (PINNED); the fixture reading is the close's.
- AC57, AC58 — as the design record says; `request.py` is absent at `c63aabbb`.
- AC2, AC3, AC4, AC14, AC15, AC33, AC40, AC43, AC54 — owed to the close's driver-suite arms.

## Second pass, 2026-11-20 — the owed items, on base `81409da27`

The unit was re-dispatched at rev-14 (PINNED) for what the first pass left: S43 and S47, owed; S41,
diverged and since restated over the kept copy; and the four suite arms named and not written. This
section supersedes "Items diverged" and "Owed, not built in this pass" above. No gate, suite or bar
ran, and no `--selftest`; each reading below is a probe of the changed code on this node.

- **S43 built** — `tools/unattended/unattended.sh#read_claims` streams one `git log --first-parent`
  over every row's tip into an `awk` that stops each row, in S43's order, at its renewing beat (a
  commit of the tip's epoch whose `renews` is `yes` or absent), at its tenure's start (the first
  commit of another epoch ends it, the oldest commit read standing for the beat), or at a commit the
  feed first sighted before now less `leases.expiry-hours` (`stale`), and exits once every row is
  resolved. The renewing-beat stop is read inside the tenure, so no age is read across an epoch
  change; TOOL-dPlacedRequest-35 owns the order's own arms. The ages still come from
  `read_first_seen`. Two staged copies in `tools/unattended/unattended.test.sh` that cut the old walk's
  literals (DPR17's `beat-utc.sh`, DPR26's `cross.sh`) now cut the new walk's lines.
- **S47 built** — `tools/loop/probe.py#write_probe_pin` records an entry-time head's git blob as the
  trigger record's `Head` (`tools/loop/probe.py#read_head_blob`), and
  `tools/loop/probe.py#run_probe_rerun` refuses, exit 2, a head whose blob moved
  (`tools/loop/probe.py#check_probe_head`); `tools/loop/probe.py#write_probe_trigger` opens
  `<key>.probe-trigger-2.md` once the newest probe returned, its pin writing `<key>.probe-2.md`
  (`tools/loop/probe.py#derive_request_probe_paths`). `help/loop.md` says both.
- **S41 holds as rev-14 states it** — `tools/unattended/unattended.sh#run_request_draw` creates an
  absent record from the kept copy under no session and refuses naming `--request <file>` with
  neither; no code changed. AC41's arm is the loop kit's `unreachable` plant in `tools/loop/budget.py`.
- **Arms written** — `tools/push-main.test.sh` 42b (AC6), `.githooks/pre-push.test.sh` 9c (AC24,
  AC25, with a control that the stub is reachable), `tools/hooks/scratch-guard.test.sh` AC28 (i) and
  (ii), and `tools/lib/resolve-python.test.sh` 2j's third row (readCard's order).

**Observations, this pass:**

- AC41 — `python tools/loop/budget.py --fixture --plant unreachable` held: `--request-draw
  0123456789ab` exited 2 naming `--request <file>` and the origin held no such ref; the recorded key's
  ref deleted from the origin, the draw exited 0 printing `draw · route-back · item.entry.place · 1/4`
  over a two-commit chain whose create is parentless.
- AC43 — over a planted 10000-commit (PINNED) chain, the newest 50 (PINNED) sighted 60 s (PINNED) before
  the read and the rest 172800 s (PINNED) before it, `--claims` read `tBig` `stale` from both a scratch copy of the driver at
  `81409da27` and this pass's; the whole verb took 1229 ms (DERIVED) against 1611 ms (DERIVED), a
  ratio of 1.31 (DERIVED), the rest of the verb's fetch, sightings and spawns being fixed cost on this
  node. The log alone read 139 to 142 ms (DERIVED) whole and 34 to 49 ms (DERIVED) streamed and
  stopped after 51 (PINNED) commits. AC43's five-fold figure is not met by the whole verb on this node;
  the close's arm, waived with its suite by README rule 8, owes the reading.
- The walk against the old one — nine (PINNED) random plants of 6 (PINNED) leases each, epochs rising,
  `renews` mixed, dates skewed across and within chains and every commit sighted, read the same
  name, node, status and verdict from both copies.
- AC47 — `python tools/loop/probe.py --fixture --plant <case>` held for `pin` (the trigger's `Head`
  is the stored head's blob), `entry-time` (a head edited between `pin` and `run` exits 2 naming the
  record, no run line) and `refusals` (a trigger after the probe returned opens
  `<key>.probe-trigger-2.md`, its pin `<key>.probe-2.md`, the first verdict's bytes unchanged). With
  the head check removed and the re-trigger restored to its refusal, `entry-time` and `refusals` each
  printed MISSED; both restored.
- AC28 — a `node -e` probe of `readCard` read the card with a non-running `bash.exe` first on PATH,
  and printed `no card` with `resolveCardBash` staged to a bare `bash`; with GOV_BASH set and only
  node's directory on PATH, a checker printing the card's `/c/` spelling read the card at a native
  path, and printed `null` with `buildNativePath`'s fold removed. readCard's candidate list with the
  spawn stubbed read `GB`, both PATH bashes, then Git for Windows' two and `bash`, the JS port's order.
- AC6, AC24, AC25 — the arms are written and not run here; the base predicate the 9c arm stages was
  checked by `sed` to change the one line it names.

**Owed to the close** (the build method's M8): each `New arm:` line's RED then GREEN, namely
`tools/push-main.test.sh` 42b against `add_feed_event` alone, `.githooks/pre-push.test.sh` 9c
(staged inside the arm), `tools/hooks/scratch-guard.test.sh` AC28 against a bare `bash`, an
existence-only resolver and no fold, `tools/lib/resolve-python.test.sh` 2j's third row against a
reorder, and the driver suite's arms waived by README rule 8; the `loop budget fixtures` and `loop
probe fixtures` legs over their extended plants, whose budget rows were not re-priced.

## The ledger, one line per criterion

Each line names the probe that made its reading, or says the reading is owed: a criterion only the
driver suite observes is owed to its arms in `tools/unattended/unattended.test.sh`, waived for this
build's landing by README rule 8, and every other owed arm is the close's (the build method's M8).

**Evidences:** TOOL-dPlacedRequest-34
- AC1 — `write_gov_ref` — over a scratch bare remote, a create, a `remove_gov_ref`, a re-create and a
  second delete of one ref left 2 (DERIVED) deletion lines in `gov-feed.log` (first pass).
- AC2 — `tombstone` — not observed in a pass: TOOL-dPlacedRequest-28's tombstone read was already in
  the tree; the reading is the driver suite's, owed.
- AC3 — `--lease prune` — not observed in a pass: TOOL-dPlacedRequest-28's `read_feed_lease_tip` was
  already in the tree; the reading is the driver suite's, owed.
- AC4 — `epoch-fence` — not observed in a pass: `tools/unattended/unattended.sh#write_claim` refuses a
  build or unit create over an `unreadable` feed commit (first pass, read); the reading is the driver
  suite's, owed.
- AC5 — `--feed check` — not observed in a pass: the driver suite's feed arm is owed; every
  `gov_feed_sh` and `gov_ref_sh` copy cut equal to its canonical (first pass).
- AC6 — `--feed check` — the arm `tools/push-main.test.sh` 42b reads the cache ref against the beat
  and `--feed check`'s exit; written this pass, its RED and GREEN owed at the close.
- AC7 — `manifest-check.sh` — `card-store.fixture.sh --plant terminal-route` held: a route to the
  terminal build refused R7 with no lookup (first pass).
- AC8 — `tools/unattended/unattended.sh` — the grep over it and the kickoff engine printed nothing
  (first pass).
- AC9 — `upstream` — `card-store.fixture.sh --plant lookup-upstream` held: a clone whose one remote is
  `upstream` read the card (first pass).
- AC10 — `skills/session-kickoff/manifest-check.sh` — the grep for `GOVREF_` and `write_gov_ref`
  printed nothing (first pass).
- AC11 — `card-store.fixture.sh --plant lookup-hung` — held: `evidence` within the bound of 4 s (PINNED, `CARD_FETCH_BOUND`)
  (PINNED) plus 3 s (PINNED) (first pass).
- AC12 — `card-store.fixture.sh --plant replay` — held: `FETCH_HEAD`'s mtime unchanged (first pass).
- AC13 — `skills/` — the grep for an inline `gov_ref_sh` or `gov_feed_sh` block printed nothing
  (first pass).
- AC14 — `--entry-claim` — not observed in a pass: TOOL-dPlacedRequest-21's no-queue, no-folder claim
  was already in the tree; the reading is the driver suite's, owed.
- AC15 — `--entry-claim` — not observed in a pass, as AC14; owed to the driver suite.
- AC16 — `scan_feed_writers` — a planted top-level writer was flagged, and over `tools/push-main.sh`
  it named only the helper the file does not define (first pass).
- AC17 — `--force-with-lease` — the census flagged a wrapped push, an array-held lease and a wrapped
  plain push of `refs/gov/mail/fx/a/s1` (first pass).
- AC18 — `python placement.py --fixture --plant claim-lines` — not run in a pass: TOOL-dPlacedRequest-10's
  plant asserts the six lines already (first pass, read); owed to the `loop placement fixtures` leg.
- AC19 — `TOOL-dPlacedRequest-20` — not observed in a pass: that unit's history check was already in
  the tree; owed to its fixture at the close.
- AC20 — `item.entry.orient` — not run in a pass: TOOL-dPlacedRequest-3's row already carries
  `map = "base"` (first pass, read); `python loop_lib.py --check` is owed at the close.
- AC21 — `1/4` — not run in a pass: TOOL-dPlacedRequest-14's `placement-loop` plant prints `1/4` to
  `4/4` and `pre-claim budget exhausted` (its own ledger); owed to `loop budget fixtures`.
- AC22 — `--lease status build tFix` — with leases off it printed `lease — off · tFix/build` (first
  pass); the two-session reading is the driver suite's, owed.
- AC23 — `lease — off · tFix/build` — acquire, flush and prune printed `lease — off · <tail>` and exit
  0, and fence `fence — none · leases are off` (first pass).
- AC24 — `straggler-guard.sh` — the predicate admitted a parentless claim and a claim parented on a
  claim over a scratch repository (first pass); the arm `.githooks/pre-push.test.sh` 9c is written
  this pass, owed at the close.
- AC25 — `<sha>^ missing` — `sed` staged the arm's base copy back to that one test and changed only
  that line; the arm's reading is owed at the close.
- AC26 — `claim-push.lock` — `git grep` over the features and gotchas hit only the dated paragraph
  (first pass).
- AC27 — `TOOL-dPlacedRequest-11` — the gotcha's dated paragraph names it (first pass).
- AC28 — `readCard` — a `node -e` probe read the card past a non-running `bash.exe` first on PATH and
  at a native path from a `/c/` answer, and read no card with each of a bare `bash` and no fold
  staged (this pass).
- AC29 — `fleet.toml` — not observed in a pass: `render_playbook.py --fleet-tag` takes `--fleet`
  (first pass, built); the fixture reading is the driver suite's, owed.
- AC30 — `GOV_NODE` — `D41LY` resolved `d`, GOV_NODE `c` resolved `c`, GOV_NODE `zz` refused naming
  GOV_NODE (first pass).
- AC31 — `tools/gate-legs.json` — both legs carry subject, chunk, ceiling and `enforces` (first pass,
  read).
- AC32 — `gen_map.py --check` — not run in a pass: both legs' pin rows and claims were read present
  (first pass); `govkit.py selfcheck` and `gen_map.py --check` are owed at the close.
- AC33 — `gov-feed.lock` — not observed in a pass: TOOL-dPlacedRequest-24's guarded break was already
  in the tree; owed to the driver suite.
- AC34 — `request.py key` — `git grep` printed only `tools/loop/loop_lib.py#read_memory_tree`'s call,
  a missing name raised the named LoopError, and `request.py key` keyed a text (first pass).
- AC35 — `refs/gov/runs/tRun` — the greps over S35's files printed only legacy-read mentions (first
  pass).
- AC36 — `skills/session-kickoff/SKILL.md` — 18354 bytes (DERIVED) of its row's 18432 (PINNED), the
  pointer found (first pass).
- AC37 — `tools/template-size-limits.txt` — the protocol measured 68369 bytes (DERIVED) of its row's
  68374 (PINNED) (first pass).
- AC38 — `gen_map.py --check` — `gen_map.py --write` ran over this pass's tree; `grep -c
  check_claim_push_clear` printed 0 (DERIVED) (first pass); the `--check` reading is owed at the close.
- AC39 — `released` — not observed in a pass: `derive_claims_line` already ranks and hides `released`
  (first pass, read); the `card-store.fixture.sh` plant is owed at the close.
- AC40 — `--lease flush` — not observed in a pass: `-` is written and mapped back already (first
  pass, read); owed to the driver suite.
- AC41 — `--request <file>` — `python tools/loop/budget.py --fixture --plant unreachable` held: no
  record and no kept copy exited 2 naming it, no ref created; a deleted record was created again from
  the kept copy, parentless, under a `1/4` row (this pass).
- AC42 — `--plant unreachable` — held: `place` printed `pre-claim draw not recorded` and wrote no block
  (this pass).
- AC43 — `--claims` — over a 10000-commit (PINNED) chain both copies read `stale`; the whole verb's
  ratio is 1.31 (DERIVED), short of five, its fixed cost dominating; the walk's log read 139 ms
  (DERIVED) whole and 34 ms (DERIVED) streamed (this pass). The suite arm is owed and waived.
- AC44 — `subject` — a subject holding a newline printed `the subject carries a control byte`, exit 2
  (first pass).
- AC45 — `feed: NOTE -` — a held `<common>/refs/gov/remote/runs/tFix.lock` gave rc 0, one line and the
  event appended; a 201-byte encoded subject was refused (first pass).
- AC46 — `git add -A` — it, the `-2` suffix, `git rev-parse` and "restore only after" are found in
  that order in `RESUME.md` (first pass).
- AC47 — `<key>.probe-2.md` — `probe.py --fixture --plant entry-time` and `--plant refusals` held, and
  each printed MISSED with its half staged away (this pass).
- AC48 — `unarmed — write-set` — `resolve_item_seed` over CLOSED `TOOL-dPlacedRequest-3` printed its
  paths (first pass); the no-path half is owed at the close.
- AC49 — `--to a/s1` — under session `s1` on tag `a`, `--to a` and `--to a/s1` exited 1 `offered`
  (first pass); the open-offer and other-session halves are the driver suite's, owed.
- AC50 — `text` — a wrapped bullet's row `text` carried all three lines joined (first pass).
- AC51 — `unarmed —` — 13 (DERIVED) `seed =` rows in `tools/loop/loop.toml` (first pass, read); the
  per-tag `python loop_lib.py seed` reading is owed at the close.
- AC52 — `item.probe.*` — not run in a pass: `check_probe_outcomes` exempts those rows already (first
  pass, read); `python loop_lib.py --check` is owed at the close.
- AC53 — `gov_feed_sh` — the `cmp` of every `gov_feed_sh` and `gov_ref_sh` copy against its canonical
  cut read equal (first pass).
- AC54 — `tombstone` — not observed in a pass: `check_claim_writable` refuses a build tombstone
  `tombstone` (first pass, built); owed to the driver suite.
- AC55 — `unarmed` — the cadence parity arm reds `unarmed — tag_index.py does not resolve` (first
  pass, built); its reading is owed at the close.
- AC56 — `git cat-file -s` — this node's one cached lease commit measured 525 bytes (DERIVED), 16.7%
  (DERIVED) under the design record's 630 (PINNED) (first pass); the fixture reading is owed.
- AC57 — `remove_gov_ref` — `remove_red_ref`'s body calls it, as the design record says (first pass).
- AC58 — `request.py` — it is absent at `c63aabbb` (first pass).
- AC59 — `^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION=` — no commit of this unit's two passes moves either
  version line; the close's diff reading is owed.
