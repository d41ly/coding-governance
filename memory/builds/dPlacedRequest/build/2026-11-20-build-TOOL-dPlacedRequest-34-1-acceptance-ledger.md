# TOOL-dPlacedRequest-34 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-34

The unit was built from its spec at rev-13 (PINNED) on base `52d334e87`, a sweep of the round-1 spec
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

**Evidences:** TOOL-dPlacedRequest-34
- AC1 — over a scratch bare remote, a create, a `remove_gov_ref`, a re-create and a second delete of
  `refs/gov/runs/tFix` left 2 (DERIVED) deletion lines in `gov-feed.log`.
- AC5, AC6 — owed to the close: the driver suite's feed arm and `tools/push-main.test.sh`'s fenced
  landing. The cmp of every `gov_feed_sh` and `gov_ref_sh` copy against its canonical cut read equal.
- AC7 — `card-store.fixture.sh --plant terminal-route` held: a route to the terminal build refused R7
  with no lookup, the card unchanged.
- AC8, AC10, AC13 — the three greps over the working tree printed nothing.
- AC9 — `--plant lookup-upstream` held: a clone whose one remote is `upstream` read the card re-derived.
- AC11 — `--plant lookup-hung` held: `evidence` with 4 s (DERIVED) over the control, a bound of 4 s
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
