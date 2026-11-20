# TOOL-dPlacedRequest-49 — the round-2 promotions' minors: one bound per question, traps before takes, every carrier observed, and criteria that can fail

**Status:** CLOSED · rev-7 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 26 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 |
| [2026-10-25-build-TOOL-dPlacedRequest-49-deviation-491.md](../build/2026-10-25-build-TOOL-dPlacedRequest-49-deviation-491.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-build-TOOL-dPlacedRequest-49-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-49-1-acceptance-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-12-pass-red-fix-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-12-pass-red-fix-brief.md) | research | TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-49-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-49-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-49-order-26-reground-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-49-order-26-reground-brief.md) | research | TOOL-dPlacedRequest-51 |
| [2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 |
| [2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`)
exited BOUNDED with 39 confirmed findings. Its blocker and four highs are units 44 to 48. This unit
is the batch `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`
makes of the rest: 22 MEDIUM and 12 LOW findings by raw id, one scope item per id, each naming its
finding and, in brackets, the review item holding it. Criterion ACn observes item Sn.

Every unit the minors land on is now CLOSED, and the charter's P19 keeps built work out of in-place
rewrites, so no item edits a spec and the builder writes none. Re-grounded on 2026-11-20 against the
tree at `3007c7e52`, each item is one of three kinds, and the scope ids are kept so the siblings that
cite them still resolve:

| Kind | Items |
|---|---|
| builds a product change still owed | S2, S5, S6, S8, S20, S23, S26, S28, S32, S33, S34 |
| observes built code by a probe | S12, S22 |
| closed by a landed unit, or resolved in §4 as text a closed spec froze | the other twenty-one |

## 2. Scope (IN)

- **S1** — finding 1 (M1). Closed by `TOOL-dPlacedRequest-43` S16: the card publish has its own
  bound, `CARD_PUBLISH_BOUND` at 140 (`skills/session-kickoff/manifest-check.sh@d55b7b28:1803`), read
  by `skills/session-kickoff/manifest-check.sh#write_card`'s `--card-ref write` call alone. Spec 33's
  S2 is frozen text. NOT OBSERVED here: spec 43's AC16 observed it at that unit's pass.
- **S2** — finding 22 (M1). The lookup keeps a reader's bound inside the claims cell's.
  `CARD_FETCH_BOUND`'s default goes from 20 to 15 (`skills/session-kickoff/manifest-check.sh@d55b7b28:1799`),
  equal to `CARD_CLAIMS_BOUND` (`skills/session-kickoff/manifest-check.sh@d55b7b28:268`) and to the
  15 s kill bound TOOL-aGraftedHelix-2 sets for a remote read in `memory/DECISIONS.md`, PINNED.
  `skills/session-kickoff/manifest-check.sh#read_card_ref`, its one reader, spells no
  `CARD_PUBLISH_BOUND`, and a lookup the bound kills still reads the next store. Observed by AC2.
- **S3** — finding 5 (M2). Resolved in §4, "The closed specs' text": spec 34's AC59 stays as built,
  and the build's one version-bump oracle is `TOOL-dPlacedRequest-44`'s §4 block, run once at the
  close. NOT OBSERVED here: no product code moves.
- **S4** — finding 9 (M3). Resolved in §4: spec 39's AC1 and its sketch are frozen text, and the order
  S6 builds arms the trap before the take, so the plant of the `DPR39 AC1` rows sits under it.
  Observed by AC6.
- **S5** — finding 14 (M3), the skeptic's corrected fix. `tools/lib/gov-feed.sh#write_dir_lock` writes
  `owner` first and `until` second, on the first take and on the re-take after a break, so a taken lock
  always carries its token and `remove_dir_lock` can match it. Today it writes `until` first.
  Observed by AC5.
- **S6** — finding 34 (M3). In `tools/lib/gov-feed.sh#add_feed_event`'s subshell the `EXIT` trap is
  installed before `write_dir_lock_wait` and acts only when `_fl_mine` is set; `write_dir_lock` sets
  `_fl_mine=1` in the same shell right after each successful `mkdir`. The trap clears the lock
  directory when `_fl_mine` is set and `owner` is absent or reads this call's token. Today the trap is
  armed after the take, and the block's header names that gap among what it does not check; the
  header is restated, and the readers anchored on the trap's line follow it: the `DPR39` block's
  plants in `tools/unattended/unattended.test.sh` and the two release plants
  `tools/lib/resolve-python.test.sh#write_feed_plant` writes. Observed by AC6.
- **S7** — finding 11 (M4). Resolved by S8: spec 36's AC3 is frozen text, and S8's arm grades every
  carrier its population lists, inline or sourced. Observed by AC8.
- **S8** — finding 35 (M4). `tools/lib/resolve-python.test.sh#check_feed_copies` sources, per
  carrier, that carrier's own `health_log_sh` cut; else the cut in the one sibling file the carrier
  sources by a column-0 `. "$KIT_DIR/<name>"` line, as `tools/unattended/unattended.sh` sources
  `lib-unattended.sh` (`tools/unattended/unattended.sh@ac121932:130`); the canonical `gov-feed.sh`
  reads the canonical `health-log.sh` beside it. A carrier with neither fails
  `<file>: no health_log_sh beside gov_feed_sh`. Today every copy runs after the canonical cut, so a
  carrier lacking the appender passes. Observed by AC8.
- **S9** — finding 15 (M5). Closed by `TOOL-dPlacedRequest-38`: `check_feed_copies` hands its two
  cuts to its `env -i` shell as positional arguments and reads no `c` or `h` from the caller, so the
  green case reaches the factory; the probes of specs 36 and 37 are frozen text. NOT OBSERVED here:
  that arm runs the green case on every carrier.
- **S10** — finding 39 (L1). Closed with S9, by the same arm. NOT OBSERVED here: as S9.
- **S11** — finding 36 (M6). Closed by `TOOL-dPlacedRequest-41` and `TOOL-dPlacedRequest-42`: the
  queue line's tip field is written in one place, `tools/unattended/unattended.sh#add_gov_queue`,
  `-` for an empty tip, and read in one, `tools/unattended/unattended.sh#write_gov_queue`; the chain
  reads the commit field through `read_gov_queue_head`, never the tip, so no helper is minted, as
  spec 43's S8 rules. NOT OBSERVED here: the `DPR41 AC1` and `DPR41 AC2` rows chain an offline
  create's release on its commit and flush both.
- **S12** — finding 7 (L2). The encoding's red half. The `DPR41 AC2` row is its green half, the flush
  of tOff's empty-tip line creating the ref; a probe runs that chain over a scratch copy of the driver
  whose decode line in `write_gov_queue` is cut, and the flush writes no tOff ref. An observation of
  built code. Observed by AC12.
- **S13** — finding 4 (M7). Closed by `TOOL-dPlacedRequest-43` S22: the spec-token checker's size
  join, `tools/check-spec-tokens.py#scan_spec_sizes`, reads the live specs alone, and spec 34 is
  CLOSED. NOT OBSERVED here: no live spec the finding names remains.
- **S14** — finding 19 (L3). Resolved in §4: spec 43 as built carries no 50111 figure, and the commit
  it was measured at stands in §4. NOT OBSERVED here: spec text only.
- **S15** — finding 20 (M8). Resolved in §4, which records the scratch-guard spawns the finding
  named. NOT OBSERVED here: spec text only.
- **S16** — finding 25 (L4). Closed by `TOOL-dPlacedRequest-43` S18: `readCard`'s bound is the named
  constant `CARD_PATH_BOUND_MS` (`tools/hooks/scratch-guard.js@e21b4d65:696`), and both of
  `tools/hooks/scratch-guard.js#readCard`'s spawns pass `runLiveness`' option set; its arm reads the
  bound from the hook's source, so no override is built (F5). NOT OBSERVED here: the `AC18` rows of
  `tools/hooks/scratch-guard.test.sh` observe it.
- **S17** — finding 2 (M9). Closed by `TOOL-dPlacedRequest-43` S6, which `TOOL-dPlacedRequest-21`
  built: `help/loop.md` states the offline outcome by exit, `refuse` exit 1 and any other value exit 4
  (`help/loop.md@d1d75226:861`), and carries no `follow-leases` cause row. NOT OBSERVED here: no page
  changes.
- **S18** — finding 3 (M10). Closed by `TOOL-dPlacedRequest-43` S17:
  `skills/session-kickoff/card-store.fixture.sh --plant publish-late` runs a stub driver that lands the
  ref and sleeps past `CARD_PUBLISH_BOUND=2`, and reads `remote-ref unknown`. NOT OBSERVED here: that
  plant observes it.
- **S19** — finding 8 (M11). Closed by `TOOL-dPlacedRequest-43`, whose AC15 as built expects a
  `foreign-` class with no `prior-session` fact planted. NOT OBSERVED here: the `DPR43 AC15` row.
- **S20** — finding 10 (M12). `check_feed_copies` asserts that its `add_feed_event` call grew the
  scratch common dir's `gov-feed.log` by one line, else `<file>: add_feed_event appended <n> lines`,
  and a plant whose append step reads `$ROOT` after the lock reds on that assertion alone. The
  commit-once half is built by `TOOL-dPlacedRequest-38`: the arm commits in its scratch repository and
  passes `git rev-parse HEAD`. Observed by AC20.
- **S21** — finding 23 (M13). Closed by `TOOL-dPlacedRequest-43` S19:
  `skills/session-kickoff/manifest-check.sh#run_driver_bounded` prints nothing, returns 125 with
  `CARD_REF_WHY` naming why where no driver runs, and each of its four callers prints its own line.
  NOT OBSERVED here: the no-conf rows of `skills/session-kickoff/card-store.fixture.sh` and
  `skills/session-kickoff/manifest-check.test.sh` read the callers' lines.
- **S22** — finding 28 (M14). Built by `TOOL-dPlacedRequest-43` S19:
  `skills/session-kickoff/manifest-check.sh#derive_claims_line` passes `"$sd/out" "$sd/err"` to
  `run_driver_bounded`, and its failure branch reads both. Left, its observation over a driver whose
  failure reaches stderr alone, which no row stages. An observation of built code. Observed by AC22.
- **S23** — finding 24 (M15). The three node resolvers agree on `GOV_NODE` (F4).
  `skills/session-kickoff/manifest-check.sh#derive_node_tag` reads a `GOV_NODE` naming a tag of its
  registry table first and prints that row; one naming no row prints `node — UNKNOWN:` with the
  reason; unset, it matches the user as today. `tools/run-gates/run-selftests.sh#resolve_node_tag` and
  `tools/unattended/lib-unattended.sh#resolve_fleet_tag` already answer `GOV_NODE` first. The probe
  that compares the three runs with `GOV_NODE` and `USER` unset. Observed by AC23.
- **S24** — finding 27 (M16). Resolved in §4: units 36 to 39 are CLOSED, built in sequence, and
  `--dispatch` refuses two passes whose declared paths meet. NOT OBSERVED here: spec text only.
- **S25** — finding 37 (M17). Closed by `TOOL-dPlacedRequest-43` S30, its race placed by
  `TOOL-dPlacedRequest-48`: `tools/unattended/unattended.sh#write_request_record` takes
  `requests.lock` through `write_dir_lock_wait` with the 5 s wait its two siblings pass, PINNED;
  a busy lock prints `request — <key> · not written · requests.lock busy` and exits 2, and the driver
  holds no third retry loop. Spec 37's S1 is frozen text, and the request section joins S33's
  comment. NOT OBSERVED here: the `DPR43 AC30` and `DPR48 AC1` rows observe it.
- **S26** — finding 38 (M18), the skeptic's corrected fix.
  `tools/unattended/unattended.sh#read_gov_queue_head` returns 1 when the ref's newest queued line
  fails the four-field shape or names a commit `git cat-file -e` does not find, and
  `tools/unattended/unattended.sh#run_lease_verb`'s offline arm then releases its hold and prints
  `lease not written — <tail> · queued commit unreadable; nothing queued`, exit 2, nothing appended.
  Today it passes over a line whose commit field is empty and reads the record of any commit a line
  names, present or not. Queued commits stay out of every ref, as now. Observed by AC26.
- **S27** — finding 6 (L5). Closed by `TOOL-dPlacedRequest-34` S35: the `RUN_CLAIMS` row of
  `tools/unattended/PROTOCOL.template.md` names the lease ref the driver writes under `LEASE_NS` and
  cites the stops guide's lease section (`tools/unattended/PROTOCOL.template.md@75dda3fa:524`).
  NOT OBSERVED here: no row changes.
- **S28** — finding 12 (L6). An id-less `--lease status` gets its own arm row. The driver's `--lease`
  arm sends `status` to `print_lease_status` before `run_lease_verb` is reached
  (`tools/unattended/unattended.sh@ac121932:19063`), so the verb's exempt list never sees it; the
  row's red is a copy whose `status` branch is cut, which then meets the verb's act check and exits 2.
  Observed by AC28.
- **S29** — finding 13 (L7). Closed by `TOOL-dPlacedRequest-43` S25: `tools/unattended/README.md`
  names `node-lock-broken` and `node-guard-cleared`. Observed by AC34, which reads each token apart.
- **S30** — finding 17 (L8). Resolved in §4: spec 36's Goal is frozen text, and the
  stale-break outcome as the code gives it stands in §4. NOT OBSERVED here: spec text only.
- **S31** — finding 18 (L9). Resolved in §4: spec 38's perf line is frozen text, and the arm's
  wall-clock bound is the ceiling its leg declares. NOT OBSERVED here: spec text only.
- **S32** — finding 29 (L10). `check_feed_copies`' population is listed with the parity loop's
  pathspec (`tools/lib/resolve-python.test.sh@ef268dfa:481`), the canonical kept in it; today it
  greps with none (`tools/lib/resolve-python.test.sh@ef268dfa:541`). Observed by AC32.
- **S33** — finding 30 (L11). The comment above `NODE_LOCK_BOUND=10` (`tools/lib/gov-feed.sh@4856b7ba:18`)
  lists every section the bound covers: the feed append, the queue's append and its flush's two file
  passes, the offline write's hold through `write_gov_queue_hold` from its read of the queue through
  its append, and `write_request_record`. Its justification, today "local file work alone", names
  the longest of them, measured once on node a at this unit's pass with its date, under the bound.
  Observed by AC33.
- **S34** — finding 31 (L12). The health-event sentence of `tools/unattended/README.md`
  (`tools/unattended/README.md@a5907a87:280`) names `lease-yielded`, which `write_gov_queue` appends,
  so every event token `add_health_event` is passed in the driver and the `gov_feed_sh` block is
  documented. Observed by AC34.

## 3. Non-goals (OUT)

- No edit to any spec: every unit the minors land on is CLOSED, and P19 keeps each as built.
- No second mechanism for the blocker or a high: units 44 to 48 own those.
- No new gate leg and no lint over spec criteria: each arm joins an existing suite.
- No override of `readCard`'s bound (F5) and no queue-tip helper (S11).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-2` — the card-store fixture, whose `publish-late` plant S18 finds built; no item edits it
- **consumes-from** `TOOL-dPlacedRequest-24` — `write_dir_lock` and `write_dir_lock_wait`, whose write order S5 sets and whose take S6 arms the trap before
- **consumes-from** `TOOL-dPlacedRequest-33` — `--card-ref write`, whose bound S1 finds built
- **consumes-from** `TOOL-dPlacedRequest-34` — AC59, which S3 leaves as built, and the protocol row S27 finds closed
- **consumes-from** `TOOL-dPlacedRequest-36` — the carrier rule S7 and S8 grade, and the Goal S30 resolves in §4
- **consumes-from** `TOOL-dPlacedRequest-37` — the node lock bound S33 documents, and the probes S9 finds closed
- **consumes-from** `TOOL-dPlacedRequest-38` — `check_feed_copies`, which S8, S20 and S32 extend
- **consumes-from** `TOOL-dPlacedRequest-39` — the contained append, whose trap S6 arms before the take
- **consumes-from** `TOOL-dPlacedRequest-40` — the exempt `status` act, which S28's row observes with no session
- **consumes-from** `TOOL-dPlacedRequest-41` — the offline write's read of the newest queued commit, which S26 refuses when unreadable, and the `DPR41` rows S11 and S12 read
- **consumes-from** `TOOL-dPlacedRequest-42` — the offline create's empty-tip line, which S11 finds written in one place
- **consumes-from** `TOOL-dPlacedRequest-43` — its S6, S16 to S19, S22, S25 and S30 as built, which S1, S13, S16 to S19, S21, S22, S25 and S29 find closed or observe
- **consumes-from** `TOOL-dPlacedRequest-44` — the version-bump oracle, which S3 names as the build's one
- **hands-off** `TOOL-dPlacedRequest-52` — S1, S3, S6 to S8, S13, S21 and S25 as this rev leaves them, the criteria AC7, AC13, AC24, AC30 and AC31 an earlier rev carried, and §5, which that unit's items for findings 4, 6, 7, 11, 14, 18, 20, 21, 25, 26 and 32 amend or, for S25's retry, read as the placed race's bound

## 4. Design

### The contained append, in order (S5, S6)

```
add_feed_event ref commit           (caller's shell: dir, tree, as TOOL-dPlacedRequest-39)
  ( _fl_mine=
    trap '[ -n "$_fl_mine" ] && owner absent or == tok && rm -rf "$d/gov-feed.lock"' EXIT
    write_dir_lock_wait "$d/gov-feed.lock" "$tok" "$NODE_LOCK_BOUND" node 5 || exit 3
        mkdir ok -> _fl_mine=1; owner <- tok; until <- EPOCHSECONDS + NODE_LOCK_BOUND
    key check, counter, append )
```

An abort anywhere after the `mkdir` finds the flag set and either no `owner` or this token, so the
lock never outlives the subshell. A busy take, exit 3, finds the flag empty and leaves the holder's
lock, as the `DPR39` busy row asserts.

### The offline refusal (S26)

```
run_lease_verb, offline arm, under write_gov_queue_hold:
  hd=$(read_gov_queue_head ref queue) || { remove_gov_queue_hold; lease not written — <tail> · queued commit unreadable; nothing queued; return 2; }
read_gov_queue_head: the ref's newest line, whatever its commit field
  ref · tip - or 40 hex · commit 40 hex · queued-utc ISO, and git cat-file -e <commit>^{commit} -> the commit, 0
  any other shape, or a commit the object store lacks                                           -> nothing, 1
  no line of the ref                                                                           -> nothing, 0
```

`add_gov_queue`'s dedupe read keeps ignoring the return, so a head it cannot read never dedupes.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `_fl_mine` | flag `write_dir_lock` sets and `add_feed_event`'s trap reads | none declared |

### The closed specs' text (S3, S4, S7, S9, S10, S14, S15, S24, S30, S31)

The closing mechanism is P19: a CLOSED spec is a frozen record, so its text stands as built, and the
fact each finding asked for stands here, or in the code an item of this unit builds.

- S3: spec 34's AC59 keeps the `git diff` form its acceptance ledger observed. The build carries one
  oracle, spec 44's §4 block, which the close runs once on the prepared merge.
- S4 and S7: frozen criteria whose product change S6 and S8 build.
- S9 and S10: frozen probes; the arm as built runs the green case.
- S14: spec 34 at `dfb9b0d3` measures 50111 bytes (PINNED 2026-11-20, `git show` of that blob, carriage returns stripped, through `wc -c`).
- S15: `tools/hooks/scratch-guard.js#readCard` spawns the kickoff engine and `cygpath`, each under
  `CARD_PATH_BOUND_MS` with the kill signal; `tools/hooks/scratch-guard.js#checkAuthorizedReadme`'s
  `runGit` passes no `timeout`, and `tools/hooks/scratch-guard.js#readOpenReds`' passes one.
- S24: the order 5 group is built and CLOSED, so its sequence decides nothing further.
- S30: `tools/run-gates/post-merge.sh` runs `set -u` with no errexit (`tools/run-gates/post-merge.sh@89a90f01:26`),
  and since `TOOL-dPlacedRequest-39` contained the append, a name the append reads that the carrier
  lacks loses the event and prints one NOTE while the carrier carries on. The abort the Goal named
  was the bound's `REMOTE_BOUND` arithmetic, which `TOOL-dPlacedRequest-37` made a pinned literal.
- S31: the carrier arm runs inside the `python resolver (behaviour + inline parity + idiom ban)` leg,
  whose `ceiling` in `tools/gate-legs.json` is 350, PINNED 2026-11-20.

### Evidence

Probed 2026-11-20 at `3007c7e52`:

- `CARD_FETCH_BOUND` defaults to 20, `CARD_CLAIMS_BOUND` to 15 and `CARD_PUBLISH_BOUND` to 140, at
  the blob pins S1 and S2 cite (`d55b7b28`).
- `write_dir_lock` writes `until`, then `owner`; `add_feed_event` arms its trap after
  `write_dir_lock_wait` returns.
- `check_feed_copies` cuts `health_log_sh` from `$HERE/health-log.sh` for every copy, asserts no feed
  line, and greps its population with no pathspec.
- `read_gov_queue_head` passes over a line whose commit field is empty, and `read_claims cached` reads
  the queued commit through `git cat-file commit` with its stderr discarded, so an absent commit reads
  as an empty record.
- `grep -c 'sleep 0.05'` prints 2 over `tools/unattended/unattended.sh`, one in its `gov_feed_sh` cut
  and one in `init_bounded`, and 1 over `tools/lib/gov-feed.sh`, PINNED.
- `derive_node_tag` reads `USERNAME`, else `USER`, and never `GOV_NODE`; `resolve_node_tag` and
  `resolve_fleet_tag` answer `GOV_NODE` first.
- The README's event sentence names `claim-taken-over`, `node-lock-broken` and `node-guard-cleared`;
  `write_gov_queue` passes `lease-yielded` at two sites.
- The `DPR40` rows run prune, flush, fence and the holder acts with no session, and no row runs
  `--lease status` with none.

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: S5, S6, S33, with its carried copies in `tools/unattended/unattended.sh`,
  `tools/run-gates/post-merge.sh` and `tools/push-main.sh`
- `tools/unattended/unattended.sh`: S26
- `tools/unattended/unattended.test.sh`: S6's plant anchors and the arms of §7
- `tools/lib/resolve-python.test.sh`: S6's release plants, S8, S20, S32
- `skills/session-kickoff/manifest-check.sh`: S2, S23
- `skills/session-kickoff/manifest-check.test.sh`: S23's arm
- `memory/guides/SESSION-KICKOFF.md`: its `last-audit` re-stamp, since S2 and S23 edit a path its
  `watch:` line names
- `help/orientation-card.md`: S23, one sentence on what the card's `node —` cell reads
- `tools/unattended/README.md`: S34
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads

### Alternatives rejected

- **Two batches.** S5, S6 and S33 write the `gov_feed_sh` block carried into
  `tools/unattended/unattended.sh`, which S26 writes too, so no split gives
  `doc.build-method#m6-passes-commits-parallelism` two disjoint write sets.
- **Each closed spec revised in place.** P19 keeps built work out of in-place rewrites; the fact
  stands in §4 instead.
- **One bound for the publish and the lookup.** A read would wait out a writer's 140 s, PINNED; two
  questions get two constants, as unit 43 built.
- **A queue-tip helper.** One writer and one reader of the field leave it nothing to route.

## 5. Production-readiness checklist

- security — S6 never clears a lock another writer took; S26 refuses a chain on a commit it cannot
  read and queues nothing.
- perf / scale — S2 holds a hung lookup to 15 s, PINNED; S31's leg ceiling bounds the carrier arm.
- error / empty / loading states — S8 fails an empty population and a carrier with no appender; S26
  and S28 each name an outcome.
- observability — S8's and S20's reds name the carrier; S34 documents every emitted event.
- risks — S5 and S6 change a block every carrier holds, carried byte-identical by the parity row; S23
  changes the card's `node —` cell wherever `GOV_NODE` is set.
- testing — the probes of §6 and the arms of §7.
- migration — none: no stored format changes.
- user docs — the kit README (S34) and `help/orientation-card.md` (S23); `help/orientation-card.md`
  names the card's fetch bound without a figure, so S2 changes no page.

## 6. Acceptance criteria

The fixtures are the named units': unit 1's lease fixture of the unattended kit's suite, a
clone and a bare origin from `write_lease_fixture`, for the driver, `RUN_CLAIMS=on`; the `DPR39`
block's scratch repository and `gov_feed_sh` cut for the feed block.

- **AC2** — When `awk` reads the defaults of `CARD_FETCH_BOUND` and `CARD_CLAIMS_BOUND` from
  `skills/session-kickoff/manifest-check.sh`, the first is at most the second, and the body of
  `read_card_ref` spells no `CARD_PUBLISH_BOUND`. Red when: the lookup's default exceeds the claims
  cell's, as the base's 20 does.
  figure: both read DERIVED by the `awk`; 20 at the base PINNED 2026-11-20.
- **AC5** — When `: "$GOVFEED_PLANT_UNSET"` is planted in a scratch cut of `write_dir_lock` on the line
  after its first write and a fresh take runs under `set -u` in a subshell, the lock directory's
  `owner` reads the token and no `until` exists. Red when: the cut writes `until` first, so the abort
  leaves a lock with no owner.
- **AC6** — When that plant sits between the `mkdir` and the first write of the `gov_feed_sh` cut and
  `bash -c 'set -u; . "$1"; add_feed_event refs/gov/bar-red "$2"; echo after' _ "$s/cut.sh" "$h"` runs
  under `env -i` in the scratch repository, it prints `after`, no `gov-feed.lock` remains, and a
  second clean call appends one line; over a live lock another token holds, the busy call leaves it.
  Red when: a cut whose trap is armed after the take leaves the lock, or a trap without the flag
  clears the holder's lock.
- **AC8** — When a probe cuts `check_feed_copies` and `blk` from the Python resolver's suite
  and runs them over a scratch carrier holding `gov_feed_sh` without `health_log_sh` and sourcing
  nothing, it prints `no health_log_sh beside gov_feed_sh` and returns 1; over the real population it
  returns 0, `tools/unattended/unattended.sh` read through `lib-unattended.sh`. Red when: the arm
  sources the canonical appender for every copy.
- **AC12** — When a probe sourcing `write_lease_fixture` and `run_lease_arm` from
  the unattended kit's suite replays the `DPR41` tOff chain, an offline acquire, an offline
  release and a flush once the origin returns, over a scratch copy of the driver whose
  `[ "$tip" != - ] || tip=""` line is cut and whose `KIT_DIR` is the kit's, as the `DPR41` copy sets
  it, the origin holds no `refs/gov/leases/tOff/build`; over the driver it reads `withdrawn`.
  Red when: both read alike, so the encoding is never read.
- **AC20** — When the cut `check_feed_copies` runs over a canonical copy whose append step reads
  `$ROOT` on the line after the trap, it prints `add_feed_event appended 0 lines` for that copy and
  returns 1; over the real population it returns 0. Red when: the arm passes a copy whose append
  never writes.
- **AC22** — When `manifest-check.sh --card --write` runs in a scratch tree holding `.unattended.conf`
  whose resolved `unattended.sh` is a stub that writes `boom` to stderr only and exits 1, the card's
  claims cell reads `claims — skipped: boom`. Red when: a copy whose call passes `/dev/null` as the
  err file reads `--claims exited 1 and printed nothing`.
- **AC23** — When a probe runs `derive_node_tag`, `resolve_node_tag` and `resolve_fleet_tag` under
  `env -u GOV_NODE -u USER USERNAME=<row user>` for each row of `tools/playbook/fleet.toml`, each
  prints that row's tag; under `GOV_NODE=a` with another row's user, all three print `a`; and a
  `GOV_NODE` naming no row makes the cell read `node — UNKNOWN:`. Red when: an ambient `GOV_NODE`
  answers the user case, or `derive_node_tag` prints the user's row while the other two print `a`.
- **AC26** — When the newest queued line for tOff names an absent sha, or is cut to three fields, and
  an offline `--lease release build tOff --as withdrawn` runs, it prints `queued commit unreadable`,
  exits 2, and `gov-queue.log` is unchanged; over a readable newest line the same release queues one
  line. Red when: the write chains on garbage, or falls back to an older line or the cached tip.
- **AC28** — When `env -u CLAUDE_CODE_SESSION_ID bash tools/unattended/unattended.sh --lease status build tFix`
  runs in the lease fixture's clone, it exits 0 and prints one `lease —` line; a scratch copy whose
  `--lease` arm has its `status` branch cut exits 2. Red when: a session gate reaches the status read.
- **AC32** — When the arm's population command runs in a scratch repository holding `a.sh` and
  `notes.md`, each carrying `# >>> gov_feed_sh` at column 0, it lists `a.sh` alone, and
  `grep -n "git grep -l '^# >>> gov_feed_sh'" tools/lib/resolve-python.test.sh` shows the parity
  loop's pathspec on that line. Red when: a record joins the population.
- **AC33** — When `awk` reads the comment above `NODE_LOCK_BOUND=10` in `tools/lib/gov-feed.sh`, it
  names `add_feed_event`, `add_gov_queue`, `write_gov_queue`, `write_gov_queue_hold` and
  `write_request_record`, and a measured longest section with its node and date, PINNED, under the
  bound. Red when: the bound is justified against sections it does not name.
- **AC34** — When a probe lists each event token `add_health_event` is passed in
  `tools/unattended/unattended.sh` and `tools/lib/gov-feed.sh`, each `$4` stem expanded by the stems
  `write_dir_lock` is called with, and runs one `grep -c` per token over `tools/unattended/README.md`,
  each prints at least 1, `lease-yielded` included. Red when: an emitted event is undocumented, or one
  combined count hides a miss.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `format-guard self-test` · `push-main self-test` · `run-selftests self-test` · `tier2-review self-test` · `policy fixtures` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC5 AC6 AC26 AC28 · the owner-first plant, the plant between `mkdir` and the first write, an absent and a three-field queued head, and a copy with the `status` branch cut, each staged against the code as at the base · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/lib/resolve-python.test.sh · covers AC8 AC20 AC32 · a scratch carrier lacking the appender, a copy reading `$ROOT` after the lock, and a quoting record, staged against unit 38's arm as built · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC23 · a `GOV_NODE` naming row `a` under another row's user, staged against `derive_node_tag` reading the user alone · none

## 8. Open questions

- **F1 — What bounds the card publish and the card lookup (S1, S2)?** (a) Two constants, the
  publish's 140 s and the lookup's 15 s, PINNED; (b) one constant at 140 s, PINNED, as unit 43 F3 read;
  (c) the bound passed into the driver. (b) holds a read past the remote-read bound; (c) adds a flag
  for one caller. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, finding 1's fix judged sound
  and finding 22's skeptic-corrected fix. widens: none · relaxes: none
- **F2 — How is the feed lock cleared on an abort inside the factory (S5, S6)?** (a) Owner first, and
  a flag-guarded trap armed before the take; (b) the trap after the take, as unit 39 reads; (c) the
  trap clearing any lock it finds. (b) leaves an ownerless lock to its deadline; (c) can clear another
  writer's lock. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the skeptic's corrected fix for
  finding 14 and finding 34's fix. widens: none · relaxes: none
- **F3 — What closes finding 27 at order 26 (S24)?** (a) Each spec records its sequence; (b) the
  orders renumbered; (c) a render that marks meeting write sets. (b) moves nothing after those units
  are built; (c) is a third parser of Files touched beside the spec-token checker's and the driver's.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the finding's second fix. widens: none ·
  relaxes: none
- **F4 — Does the card's node cell answer `GOV_NODE` (S23)?** (a) Yes: `derive_node_tag` reads a
  `GOV_NODE` naming a registry row first, as `resolve_node_tag` and `resolve_fleet_tag` do; (b) no:
  the cell names the user's row, and the probe's `GOV_NODE` case is left out; (c) the cell prints both.
  (b) leaves the three resolvers disagreeing on a node that sets `GOV_NODE`; (c) prints two answers to
  one question. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; finding 24's second case asks the three
  resolvers to agree under `GOV_NODE`, two of the three already answer it first, and the card's cell
  is the one that disagrees. widens: none · relaxes: none
- **F5 — Does `readCard` take an override of its bound for its arm (S16)?** (a) No: the constant
  `TOOL-dPlacedRequest-43` named stands, and its arm reads the bound from the hook's source; (b) a
  `SCRATCH_GUARD_CARD_READ_BOUND_MS` override, as rev-6 wrote. (b) adds a second channel the hook
  reads, for an arm speed no criterion asks. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; finding 25 asked for a named constant and its
  citation, both built, and an environment override the hook reads is a channel this unit does not
  need. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-2 promotions' 22 MEDIUM
  and 12 LOW findings.
- rev-2 · 2026-10-25 · header above §1, §6 · the round-3 promotions' fix brief: the `**Derived:** PLAY-dClosedLoop-2` line binding this unit; AC16 and AC22 observe `readCard` and `derive_claims_line` over their stubs rather than naming the suites, which stay on their `New arm:` lines; AC17 cites the page this build creates by its basename; AC26's `Red when:` is joined onto one line.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.
- rev-4 · 2026-11-19 · §2 S4, S5, S6 · §3 Edges · §4 Evidence and the sketch · §6 AC5, AC29 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit` finding 15 (H3): the node lock is the shared `write_dir_lock` family, which `TOOL-dPlacedRequest-24` rev-5 S1 moves into `gov_feed_sh`, so every name of the lock factory this spec spells is that family's: S5's write order and S6's `_fl_mine` land in that shared factory, and the guard event reads `node-guard-cleared` under the stem `node`. §7 also names `tier2-review self-test`, the leg(s) the spec-token guard join names for this spec's Files touched. §6 AC6 sources the cut by an argument path, `$s/cut.sh`, as the source join requires.
- rev-5 · 2026-11-19 · §2 S13, S16 · §6 AC13, AC16 · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`: finding 2 (H1), S13 and AC13 re-pin unit 34's
  size on the disposal's dated measurement, 47885 at rev-12 (a figure rev-6 corrected);
  finding 14 (L8), S16 spells
  `runLiveness`' whole option set and AC16 plants a grandchild holding stdout; finding 23 (M11), §7
  names `policy fixtures`.
- rev-6 · 2026-11-19 · §2 S13, S15, S25 · §3 Edges · §4 Files touched · §6 AC13, AC15, AC35 · §7 ·
  §9 rev-5 · §10 · folds `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: findings 1, 6 and 13
  (M1), 47885 at rev-12, the measured row sizes and a cut in prose here; finding 8 (M4), AC15 reads
  `checkAuthorizedReadme`'s body; finding 12 (L4), S25 calls unit 24's `write_dir_lock_wait` (AC35);
  finding 17 (M8), the map in this pass.
- rev-7 · 2026-11-20 · §1 · §2 S1 to S34 · §3 · §4 · §5 · §6 AC2 to AC34 · §7 · §8 F1 F3 F4 F5 · §10 ·
  re-grounded by `2026-11-20-prompt-TOOL-dPlacedRequest-49-order-26-reground-brief`: every unit the
  minors land on is CLOSED, so no item edits a spec (P19). Closed by the units they name: S1, S11,
  S13, S16 to S19, S21, S25, S27 and S29; resolved in §4's "The closed specs' text": S3, S4, S7, S9,
  S10, S14, S15, S24, S30 and S31; narrowed to probes of built code: S12 and S22; left to build: S2,
  S5, S6, S8, S20, S23, S26, S28 and S32 to S34. S2 reads the base's default of 20; S23 gains the card
  cell's `GOV_NODE` read (F4); S16's override is not built (F5); S25's busy line, S26's refusal and
  S28's dispatch amended to the tree's spellings; S31 to the leg's declared ceiling and S33 to the
  code's comment; the criteria of closed items taken out, with the scratch-guard and card-store arm
  lines and their Files touched rows; the kickoff manifest and the card's help page added to Files
  touched; every line citation to `path#symbol` or a blob pin, the build method's sections to their
  alias tags, and F1 and F3 pinned.

## 10. Reuse audit

Each item extends the unit its finding names. The seams: the `CARD_*_BOUND` default pattern
(`skills/session-kickoff/manifest-check.sh@d55b7b28:268`) for S2; the shared lock factory
`tools/lib/gov-feed.sh#write_dir_lock` and the contained append `tools/lib/gov-feed.sh#add_feed_event`
for S5 and S6; `tools/lib/resolve-python.test.sh#check_feed_copies` and the parity loop's pathspec for
S8, S20 and S32; `tools/unattended/unattended.sh#read_gov_queue_head` for S26;
`skills/session-kickoff/manifest-check.sh#derive_node_tag` for S23; and the `DPR40` block for S28.
The compare-and-swap ref writer, `write_claim` with `read_claims`, is not extended: S26's refusal sits
ahead of the `read_claims cached` call, and no item writes a governance ref.
`python tools/codebase-map/reuse_lookup.py "a lock directory whose owner is written before its
deadline and cleared by a trap armed before the take"`, run 2026-11-20, ranked `before`, `arm`,
`armed` and `run_arms`, name stems only, none the lock factory. `python tools/memory-recall/query.py
"how are a spec audit's minor findings batched into one unit after the units they land on closed"`
with the terms below, run 2026-11-20, returned KICK-dKeptSession-65, -64, -56 and -63 and the reground
brief of `TOOL-dPlacedRequest-43`, batches and regroundings of the same kind; none disagrees with
source.

Recall terms used: minors batch closed spec P19 in-place rewrite reground observation narrowed remaining product change
