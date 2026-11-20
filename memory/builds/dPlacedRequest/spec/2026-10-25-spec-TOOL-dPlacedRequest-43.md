# TOOL-dPlacedRequest-43 — the round-1 promotions' minors: behavioural class checks, honest outcomes, every reader of a changed spelling, and the sizes kept

**Status:** DEFERRED · rev-11 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 24 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 |
| [2026-10-25-build-TOOL-dPlacedRequest-43-deviation-431.md](../build/2026-10-25-build-TOOL-dPlacedRequest-43-deviation-431.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-43-deviation-432.md](../build/2026-10-25-build-TOOL-dPlacedRequest-43-deviation-432.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-12-pass-red-fix-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-12-pass-red-fix-brief.md) | research | TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-43-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-43-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-43-reground-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-43-reground-brief.md) | research | — |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-35 |
| [2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
exited CONVERGED with 42 confirmed findings. Its eight highs are units 35 to 42. This unit is the
batch the build method's M4 makes of the rest
(`memory/guides/BUILD-METHOD.md#m4--the-spec-audit--owed-only-where-the-build-or-its-project-declares-it`):
24 MEDIUM and 10 LOW findings, one scope item per raw id, each naming its finding and, in brackets,
the review item holding it (M1 to M22, L1 to L9). Three items hold a MEDIUM and a LOW finding of one
defect (M7 and L8, M8 and L7, M9 and L9); each finding still gets its own item. The minors land on
units built since, so this unit sits above every unit of the build, at order 24, after unit 35 at 23.
Criterion ACn observes item Sn.

Re-grounded at rev-11 against the tree, before dispatch. Each item says where it stands, by
`path#symbol`. Thirteen items are closed by the landed unit each names and keep their number with no
criterion: S5, S6, S8, S10, S12, S13, S21, S25, S26, S27, S29, S31 and S34. Seven are reduced to
an observation of code a landed unit built: S1, S2, S3, S4, S7, S15 and S32. S11 is answered in this
spec's text, S22 measures and names but cuts nothing, and S24 runs `TOOL-dPlacedRequest-44`'s oracle.
What is built is S9, S14, S16 to S20, S23, S28, S30 and S33.

## 2. Scope (IN)

- **S1** — finding 3 (M1). A strict claim read never queues, observed by behaviour. The split is
  `TOOL-dPlacedRequest-23`'s, whose arm drives `--preflight` alone and leaves the take-over and
  `--close` to this unit: over its AC1 fixture under planted `warn`, `--resume tOff`
  (`tools/unattended/unattended.sh#run_takeover`, reached from `verb_resume` there) and `--close tOff`
  (`tools/unattended/unattended.sh#verb_close`) exit non-zero printing `check 109`, `gov-queue.log`
  unchanged. An observation of built code. Observed by AC1.
- **S2** — finding 37 (M1). The same, seen from the queue: a sourced driver with a logging
  `add_gov_queue` stub runs `print_claims`, `verb_preflight`'s claim, `run_takeover` and
  `verb_close`, all in `tools/unattended/unattended.sh`, after a failed strict read, and the stub
  logs no call. An observation of built code. Observed by AC2.
- **S3** — finding 4 (M2). `TOOL-dPlacedRequest-28` S4's class observed by behaviour, narrowed to the
  acts its arm does not drive. Every create reads the feed through one call,
  `tools/unattended/unattended.sh#write_claim`'s `read_feed_lease_tip` read when `CW_ACT` is
  `create`, and unit 28's arm observes the offer and the `--preflight` claim parented on the feed's
  commit (its AC2 and AC5). Left: `--lease acquire` and `--lease take-over`, each a create over an
  absent lease (`tools/unattended/unattended.sh#check_claim_writable`'s `lease:none` row), over a
  `released` lease the feed sighted and the origin no longer holds, each yield a commit parented on
  the feed's commit at its epoch plus one. Observed by AC3.
- **S4** — finding 19 (M2). The tombstone refusal on the same paths. Unit 28's arm observes it for
  the offer, `--lease acquire`, `--preflight` and the driver's take-over column, over a real feed
  tombstone rather than a stub. Left: `--lease take-over` over a tombstone the feed sighted and the
  origin no longer holds exits 1 printing `tombstone`, nothing written. Observed by AC4.
- **S5** — finding 5 (M3). Closed by `TOOL-dPlacedRequest-33`: its arm's stub `git` logs every call
  and the off check counts only `fetch` and `push`, with a liveness half under the switch on.
  NOT OBSERVED here: that arm observes it.
- **S6** — finding 6 (M4). Closed by `TOOL-dPlacedRequest-21`: `--entry-claim` routes an offline
  cause through `tools/loop/claim.py#run_claim_verb`, `refuse-offline` under `refuse` and
  `wait-offline` under any other value, exit 4, and `tools/loop/loop.toml`'s `item.entry.claim`
  lists its outcomes without a per-value row. NOT OBSERVED here: `claim.py`'s `slug-taken` plant
  observes the exit 4.
- **S7** — finding 7 (M5). The queue line's empty-tip encoding is built:
  `tools/unattended/unattended.sh#add_gov_queue` writes `-` for an empty expected tip
  (`TOOL-dPlacedRequest-1`) and `tools/unattended/unattended.sh#write_gov_queue` reads it back as
  empty. Left, its observation on a line an `IFS` read would shift: `IFS=$'\t' read -r ref tip
  commit utc` over an offline create's line reads a 40-hex `commit`. Observed by AC7.
- **S8** — finding 25 (M13). Closed by `TOOL-dPlacedRequest-24` and `TOOL-dPlacedRequest-41`: the
  cached-tip field is written in one place and read in one, and the append-once test compares
  commits, never the field, so no one-sided compare of the empty spelling exists and no helper is
  minted (§8 F1). **Readers:** by name: `add_gov_queue`, which writes the field, `write_gov_queue`,
  which maps it back to empty before its compare-and-swap, and `read_gov_queue_head`, which reads the
  commit field alone. by value: `write_gov_ref`, called by `write_gov_queue` with the mapped tip as
  its expected sha, the one compare of the value. NOT OBSERVED here: unit 24's arm observes the
  re-run offline create's one line.
- **S9** — finding 8 (M6). The stops guide's `leases.offline` row names its population as the
  `--lease` verbs, the soft and quiet claim callers and `--entry-claim`: under `refuse` the claim
  exits 1, and under any other value it prints `claim not written — offline` and exits 4, queueing
  nothing (`tools/loop/claim.py#run_claim_verb`, `TOOL-dPlacedRequest-21` S2 and S5). Today the row
  says the key governs the `--lease` verbs and the soft and quiet claim callers alone. Observed by
  AC9.
- **S10** — finding 9 (L1). Closed by `TOOL-dPlacedRequest-31`: its arm plants a session-only line
  beside the stored copy and expects no consent, staged against the base predicate. NOT OBSERVED
  here: that arm observes it.
- **S11** — finding 10 (L2). `TOOL-dPlacedRequest-34` S10, S13, AC10 and AC13 restate
  `TOOL-dPlacedRequest-33` S2, S3 and AC4. The line naming unit 33 the closing mechanism of round-1
  findings 33 and 34 lands in this spec's §4, "The closing mechanism (S11)", and neither spec 33
  nor spec 34 is edited, both CLOSED (§8 F4). Observed by AC11.
- **S12** — finding 11 (L3). Closed by `TOOL-dPlacedRequest-34` S35: the one `refs/gov/runs` mention
  left in `tools/unattended/VERBS.template.md` names a legacy claim's `node` field, never a claim's
  home. NOT OBSERVED here: nothing remains to observe.
- **S13** — finding 12 (L4). Closed by `TOOL-dPlacedRequest-24`: every line of
  `tools/lib/gov-feed.sh` spelling `gov-feed.lock` sits in `add_feed_event` as its
  `write_dir_lock_wait` call or its `remove_dir_lock` trap. NOT OBSERVED here: nothing remains.
- **S14** — finding 15 (M7). The `.typed` append in
  `tools/unattended/unattended.sh#write_request_record` and the read in
  `tools/unattended/unattended.sh#check_request_consent` hash with `git hash-object --no-filters --`,
  so the blob is of the submitted bytes on every node's config, as the verbs guide's `--request`
  entry and `help/loop.md` already state. The collision compare now folds whitespace
  (`derive_request_fold`, `TOOL-dPlacedRequest-30`), so a second session submitting a CRLF twin of
  stored words keeps the first copy and reads no consent, as a re-wrapped twin already does.
  Observed by AC14.
- **S15** — finding 16 (M8). The identity rule as the code reads it is built:
  `tools/unattended/unattended.sh#check_claim_writable`'s `lease` mode reads `mine` only for present,
  equal sessions and equal tags and reads no keepalive (`TOOL-dPlacedRequest-32` S3), and the run
  columns read `mine` only for an equal keepalive and session, with the prior-session and take-over
  rows. Left, its observation on a run column. Observed by AC15.
- **S16** — finding 17 (M9). The card publish has its own bound (§8 F7):
  `CARD_PUBLISH_BOUND=${CARD_PUBLISH_BOUND:-140}` declared beside `CARD_FETCH_BOUND` in
  `skills/session-kickoff/manifest-check.sh`, read by `write_build_card`'s `--card-ref write` call
  alone, above the write verb's worst case of two `REMOTE_BOUND` calls plus the feed lock's wait.
  `CARD_FETCH_BOUND` keeps its default for `read_card_ref`'s lookup, a reader. Observed by AC16.
  figure: 140 PINNED by this item; 20, the lookup's default today, PINNED 2026-11-20.
- **S17** — finding 43 (L9). A killed publish, `write_build_card`'s kill arm, prints `card —
  remote-ref unknown: no answer within <n>s`, never `not written`, and a write that landed before the
  kill reaches the feed at the next sighting (`TOOL-dPlacedRequest-13` S4). A killed lookup,
  `read_card_ref`, wrote nothing and keeps `not written`. `help/orientation-card.md` names both.
  Observed by AC17.
- **S18** — finding 18 (M10). `readCard`'s two `spawnSync` calls, the checker's `--card --path` and
  its `cygpath` fold, pass the whole option set `tools/unattended/stop-guard.js#runLiveness` passes:
  the timeout, `killSignal: 'SIGKILL'`, `stdio: ['ignore', 'pipe', 'pipe']` in place of `input: ''`,
  and `windowsHide: true`. Both already pass the timeout
  (`tools/hooks/scratch-guard.js#CARD_PATH_BOUND_MS`) and `windowsHide`; the kill signal and the
  closed stdin are left. A checker that does not answer reads as no card, named. Observed by AC18.
- **S19** — finding 22 (M11). One helper, `run_driver_bounded <bound> <out> <err> <verb args>`, in
  `skills/session-kickoff/manifest-check.sh`, runs the driver under the bound and reads the kill; it
  calls `resolve_card_driver` for the timeout probe, the conf check and the kit resolve, the seam
  `TOOL-dPlacedRequest-34` S10 extracted for the card's two calls. `derive_overlaps_line`,
  `derive_claims_line`, `read_card_ref` and `write_build_card` call it, so the bounded driver call is
  spelled once. Observed by AC19.
- **S20** — finding 23 (M12). `TOOL-dPlacedRequest-34` S30's reason is corrected in the code's
  comments: `skills/session-kickoff/manifest-check.sh#derive_node_tag` and
  `tools/run-gates/run-selftests.sh#resolve_node_tag` read the governance file's `## Node registry`
  table, which `tools/playbook/render_playbook.py#derive_node_table` renders from `fleet.toml`, so
  one registry; they stay because both kits read the rendered table, not the playbook kit. Each is
  brought to `tools/playbook/render_playbook.py#read_fleet_tag`'s rule, the user case-folded and
  equal to the row's user, which `tools/unattended/lib-unattended.sh#resolve_fleet_tag` asks.
  Today `derive_node_tag` compares case-sensitively and `resolve_node_tag` by substring. Observed by
  AC20.
- **S21** — finding 27 (M14). Closed by `TOOL-dPlacedRequest-34` S35 and the size row as raised
  since: the rendered protocol measures within its row in `tools/template-size-limits.txt`.
  NOT OBSERVED here: the `unattended protocol size` leg reads the row.
  figure: 68369 against the row's 68374, measured CR-stripped, PINNED 2026-11-20.
- **S22** — finding 28 (M15). Narrowed to the live specs (§8 F5). After the pass renders the records
  regions, the spec-token checker's size join (`tools/check-spec-tokens.py#scan_spec_sizes`) reads
  every live spec of this build, OPEN, SPECCED, INPROGRESS or BLOCKED, against the class cap
  `tools/check-spec-tokens.py#read_size_ceilings` answers. A spec it names over the cap is named in
  the pass's return as an owed spec-writer cut; the pass edits no spec. A CLOSED or DEFERRED spec is
  outside the join and is neither measured nor cut. Observed by AC22.
- **S23** — finding 29 (M16). The `.typed` line's two-field grammar is built
  (`TOOL-dPlacedRequest-31`), and unit 5's `relayed` plant writes it. Left: the plant hashes as S14's
  writer does, `--no-filters`, so the plant's blob is the writer's on every config.
  **Readers:** by name: `write_typed_request`, the plant, `write_request_record`, the writer, and
  `check_request_consent`, the read; `tools/unattended/VERBS.template.md` and `help/loop.md` describe
  the line. by value: `check_request_consent` alone compares a line's blob, and S14 states its read.
  Observed by AC23.
- **S24** — finding 30 (M17). The version-bump oracle reads the build's own commits: AC24 runs
  `TOOL-dPlacedRequest-44`'s §4 oracle, which names the parent it walks, prints the range and count it
  walked, and refuses an empty walk (§8 F6). That unit owns the oracle's text; this unit builds
  nothing for S24. Observed by AC24.
- **S25** — finding 31 (L6). Closed by `TOOL-dPlacedRequest-24`: `tools/unattended/README.md`'s
  health-event sentence names `node-lock-broken` and `node-guard-cleared` for the feed's and the
  queue's locks. NOT OBSERVED here: nothing remains.
- **S26** — finding 21 (L6). Closed by `TOOL-dPlacedRequest-24`: `tools/lib/gov-feed.sh`'s lock
  factory passes `<stem>-lock-broken` and `<stem>-guard-cleared`, and the README spells both for each
  stem in use, `node` and `spec-tokens`. NOT OBSERVED here: nothing remains.
- **S27** — finding 34 (M18). Closed by `TOOL-dPlacedRequest-24`, which has no confirming read: the
  flush reads the push's own status in `tools/unattended/unattended.sh#write_gov_ref`, a lost race
  answered by the remote, and `write_gov_queue` keeps a line on any write that did not complete.
  NOT OBSERVED here: no confirming read remains to observe.
- **S28** — finding 35 (M19). The lander's re-fence keeps `TOOL-dPlacedRequest-15` S2's `lease
  refused — offline` apart: `tools/unattended/unattended.sh#write_fence_beat` prints it for an
  unanswered `--after` read, `tools/push-main.sh#read_fence_line` returns it apart from every other
  refusal, and `tools/push-main.sh#derive_push_failure` maps it to `unreachable` (exit 1, no abort
  remedy), keeping `fenced` for a read that answered. Today every refusal there is `fenced`.
  Observed by AC28.
- **S29** — finding 38 (M20). Closed by `TOOL-dPlacedRequest-26` and `TOOL-dPlacedRequest-35`: their
  arms read a take-over that is a one-commit tenure, sighted a minute ago, `live`. NOT OBSERVED here:
  those arms observe the tip case.
- **S30** — finding 39 (M21). `write_request_record` takes `write_dir_lock_wait` on
  `<git-common-dir>/requests.lock`, stem `node`, around the fold compare, the `cp --` copy into a
  temporary file and its `mv -n` into the store, and the `.typed` append, and releases it with
  `remove_dir_lock` on every way out. A racing second call re-runs the compare after the first's copy
  and is refused `collision`. A lock still busy after the wait prints `request — <key> · not written
  · requests.lock busy` and exits 2, writing nothing; the verbs guide and `help/loop.md` name it.
  Observed by AC30.
  figure: the wait is the queue's, 5 s, PINNED.
- **S31** — finding 40 (L7). Closed by `TOOL-dPlacedRequest-32`: the `lease` mode of
  `check_claim_writable` compares no keepalive, so differing sessions never read `mine` there.
  NOT OBSERVED here: that mode takes no keepalive to compare.
- **S32** — finding 41 (M22). The order is built: `tools/unattended/unattended.sh#run_lease_verb`
  answers `RUN_CLAIMS` off before its identity refusal (`TOOL-dPlacedRequest-34` S23). Left, its
  observation on an id-less acquire. Observed by AC32.
- **S33** — finding 42 (L8). Consent does not survive an end-of-line rewrite of the stored copy,
  S14's hash read. Observed by AC33.
- **S34** — finding 20 (L5). Closed by `TOOL-dPlacedRequest-11`: no tracked file outside the records
  spells `check_claim_push_clear` or `claim_push_lock`, and the map holds neither. NOT OBSERVED here:
  nothing remains.

## 3. Non-goals (OUT)

- No second mechanism for a high: units 35 to 42 own those.
- No edit to any other spec. A CLOSED spec stays as built (§8 F4 and F5), and a DEFERRED sibling
  is re-grounded at its own dispatch.
- No oracle script and no placed-race arm: units 44 and 48 own them (§8 F6).
- No new gate leg: each arm joins an existing suite.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-1` — the queue line's encoding and `resolve_fleet_tag`, which S7 observes and S20 matches
- **consumes-from** `TOOL-dPlacedRequest-3` — `item.entry.claim`'s outcomes, which S6 found closed by `TOOL-dPlacedRequest-21`
- **consumes-from** `TOOL-dPlacedRequest-5` — the `relayed` plant, which S23 makes hash as the writer does
- **consumes-from** `TOOL-dPlacedRequest-19` — `--request`'s writer and the `.typed` file, which S14 and S30 amend
- **consumes-from** `TOOL-dPlacedRequest-21` — `--entry-claim`'s use of `leases.offline`, which S9 names in the guide
- **consumes-from** `TOOL-dPlacedRequest-23` — the strict callers' split, which S1 and S2 observe
- **consumes-from** `TOOL-dPlacedRequest-24` — the node lock's `write_dir_lock_wait`, which S30 reuses
- **consumes-from** `TOOL-dPlacedRequest-26` — the tenure walk, whose tip case S29 found observed
- **consumes-from** `TOOL-dPlacedRequest-28` — `write_claim`'s feed read, which S3 and S4 observe on the acts its arm leaves
- **consumes-from** `TOOL-dPlacedRequest-29` — the re-fence act and its classifier, which S28 amends
- **consumes-from** `TOOL-dPlacedRequest-30` — `--request`'s fold compare, which S30 locks
- **consumes-from** `TOOL-dPlacedRequest-31` — the `.typed` line and the consent read, which S14 and S33 amend
- **consumes-from** `TOOL-dPlacedRequest-32` — the identity rule, which S15 observes
- **consumes-from** `TOOL-dPlacedRequest-33` — `--card-ref write` and its engine call, which S16, S17 and S19 amend and S11 names
- **consumes-from** `TOOL-dPlacedRequest-34` — `resolve_card_driver`, `readCard`, the lookup and `--lease`'s off answer, which S16 to S20 amend and S32 observes
- **hands-off** `TOOL-dPlacedRequest-44` — its §4 oracle, which AC24 runs and that unit owns; its S3 is folded here at rev-11
- **hands-off** `TOOL-dPlacedRequest-48` — the placed-race arm AC30 names, built against S30's lock; its S4 is folded here at rev-11, and the copy its stub keys on is `cp --` into a temporary file, then `mv -n`
- **hands-off** `TOOL-dPlacedRequest-49` — S8, S15 to S20, S22, S30 and their criteria, which that unit's items for the round-3 audit's minors re-point, re-bound and re-observe at its own re-grounding
- **hands-off** `TOOL-dPlacedRequest-52` — S19 and its sketch, S22, AC22 and S30, which that unit's items for findings 5, 7 and 20 pin and rewrite; AC22 reads the checker's cap since rev-11
- **hands-off** `TOOL-dPlacedRequest-56` — AC24, which that unit's item for finding 13 restates as the oracle's header line and exit 0
- **hands-off** `TOOL-dPlacedRequest-59` — AC24, which that unit's item for finding 16 gives the run's base
- **hands-off** `TOOL-dPlacedRequest-63` — AC24, which that unit's item for finding 1 gives the `base:` fact of `RUN.md`

## 4. Design

### Evidence

- Strict callers, all in `tools/unattended/unattended.sh`: `print_claims`, `verb_preflight`,
  `run_takeover` (from `verb_resume`) and `verb_close`, each `read_claims strict`. Unit 23's arm
  header names the take-over and `--close` as this unit's to observe
  (`tools/unattended/unattended.test.sh`, its `TOOL-dPlacedRequest-23` block).
- The bounded driver call, four times: `derive_overlaps_line` and `derive_claims_line` each run the
  probe, the conf check and the kit resolve themselves, then `GOV_RUNLOG=0 timeout -k 2`;
  `read_card_ref` and `write_build_card` reach the same three checks through `resolve_card_driver`
  (all `skills/session-kickoff/manifest-check.sh`). The memory, map, pockets and CLI cells bound
  python or `claude`, not the driver, and stay as they are.
- `--request`'s store write (`tools/unattended/unattended.sh#write_request_record`): the fold
  compare, then `cp --` into `<key>.md.<pid>` and `mv -n` into `<key>.md`, then the `.typed` append
  of a plain `hash-object --` blob, under no lock. `mv -n` keeps a racing loser from overwriting the
  copy, and the loser still exits 0 with its words unkept and its `.typed` line added.
- The size join, read on 2026-11-20 by `python tools/check-spec-tokens.py`:
  it graded 30 live specs tree-wide (PINNED 2026-11-20);
  its ceiling was 49152 bytes from the template-size limits file's class row (PINNED 2026-11-20),
  the policy file declaring none, under `budgets.enforce = "warn"`. No spec of this build was live:
  units 1 to 42, 46 and 47 CLOSED, the rest DEFERRED.
  This spec measured 39888 bytes at rev-10 (PINNED 2026-11-20).

### The closing mechanism (S11)

`TOOL-dPlacedRequest-33` is the closing mechanism of round-1 findings 33 and 34: its S2 and S3 build
what `TOOL-dPlacedRequest-34` S10 and S13 restate, and its AC4 observes what that spec's AC10 and
AC13 re-observe.

### The re-fence outcomes (S28)

| `--after` read | Line | Lander class | Exit |
|---|---|---|---|
| answered, same holder, on chain, same epoch | `fence — …` | `refenced` | retry |
| answered, otherwise | `lease refused — epoch-fence` | `fenced` | 1, `--abort … claim-lost` |
| no answer | `lease refused — offline` | `unreachable` | 1, no abort remedy |

### The bounded call (S19)

```
run_driver_bounded <bound> <out> <err> <verb args>  -> rc of the verb
  resolve_card_driver fails             -> rc 125, CARD_REF_WHY says why; the caller prints its skip line
  GOV_RUNLOG=0 timeout -k 2 <bound> bash "$CARD_DRV" <verb args> </dev/null >"<out>" 2>"<err>"
  rc 124 or 137                          -> the caller prints its kill line
```

### The requests lock (S30)

```
write_request_record <file>
  ... key, tag, session, common dir, as today
  write_dir_lock_wait "$cdir/requests.lock" <token> "$NODE_LOCK_BOUND" node 5 || busy line, rc 2
  fold compare -> collision (rc 2) | cp -- into a temporary file, mv -n | .typed append
  remove_dir_lock "$cdir/requests.lock" <token>   # on every way out of the block
  ... the record's push, as today, with no lock held
```

### Inventory

- `run_driver_bounded`, S19's helper: cell `sh.function`, which the naming lexicon grades OK.
- `CARD_PUBLISH_BOUND`, S16's bound: a shell constant, a cell the lexicon declares none for.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S14, S30
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/unattended/STOPS.template.md` and `memory/guides/UNATTENDED-STOPS.md`: S9
- `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`: S28, S30
- `help/loop.md`: S30; `help/orientation-card.md`: S17
- `skills/session-kickoff/manifest-check.sh`: S16, S17, S19, S20
- `skills/session-kickoff/card-store.fixture.sh`: S17's plant
- `tools/hooks/scratch-guard.js` and `tools/hooks/scratch-guard.test.sh`: S18
- `tools/push-main.sh` and `tools/push-main.test.sh`: S28
- `tools/run-gates/run-selftests.sh`: S20
- `tools/loop/placement.py`: S23
- `memory/guides/SESSION-KICKOFF.md`: its `last-audit` re-stamp, since its `watch:` line names
  `manifest-check.sh` and `run-selftests.sh`
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass, since S19 mints a function the symbol extractor reads

### Alternatives rejected

- **Two batches.** M4 makes a review's minors one unit, and the narrowed items fit one pass.
- **S20 by re-pointing both shell resolvers at `read_fleet`.** Neither kit carries the playbook kit,
  and the rendered table is the copy each adopter holds.
- **S19 as a new resolver beside `resolve_card_driver`.** That seam already holds the three checks
  for two of the four calls; a second copy is the defect finding 22 names.

## 5. Production-readiness checklist

- security — S14 and S33 bind consent to bytes; S30 closes a racing write of the stored words.
- perf / scale — S18 kills a hung checker at `CARD_PATH_BOUND_MS`; S19 is one helper for four calls.
- error / empty / loading states — S17, S28 and S30 each name an outcome for no answer or a busy lock.
- observability — S30's lock takes the `node` stem, whose break events the README already lists.
- risks — S16 lets a hung remote hold the READY append up to `CARD_PUBLISH_BOUND`, the cost of never
  killing a writer mid-write.
- testing — the probes of §6 and the arms of §7.
- migration — none: every surface is new in this build.
- user docs — the stops and verbs guides, `help/loop.md` for `--request` and
  `help/orientation-card.md` for the card's outcomes; this unit adds no verb.

## 6. Acceptance criteria

The fixtures are the named units': unit 1's AC7 clone and bare origin for the driver, unit 28's
sighted-lease feed, unit 2's card store fixture for the engine, unit 19's two clones for requests,
each `RUN_CLAIMS=on` unless stated.

- **AC1** — When `--resume tOff` and `--close tOff` run over a renamed-away origin under planted
  `warn`, each exits non-zero printing `check 109` and `gov-queue.log` is unchanged. Red when: a
  scratch copy's lease writer queues whenever its read failed.
- **AC2** — When a probe sources the driver with an `add_gov_queue` stub appending to `q.log` and runs
  the four strict callers over the failed read, `q.log` is empty. Red when: a strict caller reaches
  the queue through the writer.
- **AC3** — When `--lease acquire` and `--lease take-over` each run over a `released` lease the feed
  sighted and the origin no longer holds, each new commit's parent under
  `git rev-list --parents -n1` is the feed's commit. Red when: a staged `write_claim` with its feed
  read cut builds a parentless commit.
- **AC4** — When `--lease take-over` runs over a build tombstone the feed sighted and the origin no
  longer holds, it exits 1 printing `tombstone` and the origin holds no such ref. Red when: the
  take-over revives it.
- **AC7** — When an offline create of `tOff` is queued and `IFS=$'\t' read -r ref tip commit utc`
  reads its line, `commit` matches `^[0-9a-f]{40}$`. Red when: an empty field shifts the line.
- **AC9** — When `grep 'leases.offline' memory/guides/UNATTENDED-STOPS.md | grep -c 'entry-claim'`
  runs, it prints at least 1. Red when: the guide's population omits a reader.
- **AC11** — When `grep -n 'closing mechanism of round-1 findings 33 and 34' 2026-10-25-spec-TOOL-dPlacedRequest-43.md`
  runs, it prints a line naming `TOOL-dPlacedRequest-33`, and `git diff` of this unit's pass touches
  no spec. Red when: the naming line is written into a CLOSED spec.
- **AC14** — When a CRLF `a.md` is requested under `core.autocrlf=true`, its `.typed` blob equals
  `git hash-object --no-filters a.md`. Red when: the filtered blob is written.
- **AC15** — When `check_claim_writable` runs sourced in `take-over` mode over a record of session
  `s1` and keepalive `k1`, from session `s2` with keepalive `k1` and no `prior-session` fact, its
  `CW_CLS` is a `foreign-` class. Red when: a staged run column reads the keepalive alone as `mine`.
- **AC16** — When `awk` reads `CARD_PUBLISH_BOUND`'s default from `manifest-check.sh` and
  `REMOTE_BOUND` from `unattended.sh`, the first exceeds twice the second plus 5, and
  `CARD_FETCH_BOUND`'s default is unchanged. Red when: the writer runs under a reader's bound.
- **AC17** — When `bash skills/session-kickoff/card-store.fixture.sh --plant publish-late` runs a stub
  driver whose lookup answers and whose write lands the ref, then sleeps past `CARD_PUBLISH_BOUND=2`,
  the append prints `card — remote-ref unknown`. Red when: a landed write reads `not written`.
- **AC18** — When a `node -e` probe calls `readCard` with a stub checker that never answers, it
  returns no card, named, within the bound plus 1 s (PINNED); with a stub that backgrounds a sleeping child
  holding stdout and exits, it returns no card within the same; and `grep -c "killSignal: 'SIGKILL'"`
  over `readCard`'s body, cut from `function readCard(` to the next line opening `function `, prints
  2. Red when: the hook waits on a hung checker or a grandchild's pipe.
  figure: the bound DERIVED from `CARD_PATH_BOUND_MS` at the probe; the 1 s margin PINNED.
- **AC19** — When `grep -cE 'timeout -k 2 .* bash ' skills/session-kickoff/manifest-check.sh` runs, it
  prints 1, the line inside `run_driver_bounded`. Red when: a call site copies the bounded call.
- **AC20** — When a probe sets `USERNAME` to each `fleet.toml` row's user, in its own case and folded
  to upper case, `derive_node_tag`, `resolve_node_tag` and `resolve_fleet_tag` print that row's tag.
  Red when: two resolvers disagree.
- **AC22** — When `python tools/check-spec-tokens.py` runs after `gen_build_index.py --write` at this
  unit's pass, its `size join` line and each `BUDGET WARN` or `size <-` row naming a spec of this
  build are copied into the pass's return, each such spec named there as an owed spec-writer cut,
  and the pass's diff touches no spec. Red when: a live spec of the build is over the cap and the
  return names no cut.
  figure: the cap DERIVED at the run by `read_size_ceilings`; 49152 on 2026-11-20 PINNED.
- **AC23** — When `python tools/loop/placement.py --fixture --plant relayed` runs, it passes, and
  `grep -c 'hash-object", "--no-filters' tools/loop/placement.py` prints 1. Red when: the plant
  hashes through the clean filter.
- **AC24** — When the oracle `TOOL-dPlacedRequest-44` §4 states runs on the prepared merge, it prints
  its `version oracle:` line naming a non-zero count and no `KIT_` version line after it. Red when: a
  mint from main reads as a hand-bump, or the walk reads no commit of the build.
- **AC28** — When a stub kills the `--after` read, `push-main.sh` prints `unreachable`, not
  `fenced`. Red when: a hiccup tells a holder to abort.
- **AC30** — When a live `requests.lock` is planted in the common dir and `--request a.md` runs, it
  exits 2 within 6 s (PINNED) printing `requests.lock busy`, the store and the origin unchanged; the race
  itself is observed by `TOOL-dPlacedRequest-48`'s placed-race arm at that unit's pass. Red when:
  `--request` writes under a held lock.
  figure: the 6 s ceiling PINNED, the queue's wait plus 1 s.
- **AC32** — When `env -u CLAUDE_CODE_SESSION_ID` runs `--lease acquire build tFix` with `RUN_CLAIMS`
  off, it prints `lease — off` and exits 0. Red when: the identity test runs first.
- **AC33** — When a CRLF copy of `a.md` replaces the stored copy after `s1`'s request,
  `check_request_consent` in `s1` returns 1. Red when: the filtered blob matches.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `format-guard self-test` · `push-main self-test` · `run-selftests self-test` · `unattended protocol size` · `codebase-map coverage + freshness` · `tier2-review self-test` · `policy fixtures`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC7 AC14 AC15 AC30 AC32 AC33 · each item's plant, staged against the unit it amends or observes · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/push-main.test.sh · covers AC28 · a killed `--after` read, staged against the epoch-fence mapping · the suite's assertion count raised by the arm added
New arm: tools/hooks/scratch-guard.test.sh · covers AC18 · a stub checker that never answers, staged against the spawn with no kill signal · the suite's assertion count raised by the arm added
New arm: skills/session-kickoff/card-store.fixture.sh · covers AC17 · the `publish-late` plant, staged against the `not written` kill line · none

## 8. Open questions

- **F1 — Is the empty tip spelled once (S8)?** (a) One `derive_queue_tip` both readers call; (b) each
  reader normalises. (b) is the one-sided compare finding 25 names. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound. widens: none · relaxes: none. At rev-11 the
  tree meets (a)'s intent with no helper: one writer and one reader of the field, and the append-once
  test compares commits.
- **F2 — How do the node-tag resolvers stop disagreeing (S20)?** (a) Corrected reason and a parity
  probe over `fleet.toml`; (b) both re-pointed at `read_fleet`. (b) needs the playbook kit inside two
  copy-installed kits. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's second fix.
  widens: none · relaxes: none
- **F3 — What bounds the card publish (S16)?** (a) A 140 s default (PINNED) above the verb's worst
  case; (b) the bound passed into the driver. (b) adds a flag to a verb for one caller. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the review's first fix. widens: none · relaxes: none
- **F4 — Closed specs: where does S11's naming line land?** (a) In this spec's §4, with spec 33 and
  spec 34 untouched; (b) as a rev bump of spec 33, as rev-10 wrote it. RESOLVED (agent, 2026-11-20,
  delegated): (a), rung 3; both specs are CLOSED and the charter's P19 keeps built work out of
  in-place rewrites, and a builder writes no spec. widens: none · relaxes: none
- **F5 — Size: which specs does S22 measure, and does it cut?** (a) The live specs the checker's size
  join grades, against the cap it reads, each one over named as an owed spec-writer cut; (b) every
  spec under `spec/` at 48128, cut in place, as rev-10 wrote it. RESOLVED (agent, 2026-11-20,
  delegated): (a), rung 3; the join grades OPEN, SPECCED, INPROGRESS and BLOCKED specs alone, a
  CLOSED spec over the figure is no hit, P19 forbids cutting one, and a builder writes no spec.
  widens: none · relaxes: none
- **F6 — Promoted: fold units 44 S3 and 48 S4 now, or leave them to rewrite this spec at order 25?**
  (a) Fold now: AC24 runs unit 44's §4 oracle and AC30 names unit 48's placed-race arm, this unit
  building the lock and neither the arm nor the oracle's text; (b) leave both in-place rewrites to
  order 25. RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; this spec is still DEFERRED, so
  the rewrite those units order is a spec act done here once, before it is built, and never on a
  CLOSED spec. widens: none · relaxes: none
- **F7 — Which name carries S16's publish bound?** (a) A new `CARD_PUBLISH_BOUND` read by the write
  alone, `CARD_FETCH_BOUND` kept for the lookup; (b) `CARD_FETCH_BOUND` raised, which since
  `TOOL-dPlacedRequest-34` also bounds the lookup. RESOLVED (agent, 2026-11-20, delegated): (a),
  rung 3; the lookup is a reader the session's card waits on, and the tree moved the fetch bound
  onto it after F3 was written. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-1 promotions' 24 MEDIUM
  and 10 LOW findings.
- rev-2 · 2026-10-25 · §7 leg line adds `agent-cap self-test`, `verifier fan-out self-test`,
  `review-join self-test` and `hook destinations self-test`, the legs whose `hooks/` guard
  `tools/hooks/scratch-guard.js` trips.
- rev-3 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-44 and TOOL-dPlacedRequest-48 and TOOL-dPlacedRequest-49.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edge to `TOOL-dPlacedRequest-56`, mirroring its consumes-from.
- rev-6 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edge to `TOOL-dPlacedRequest-59`, mirroring its consumes-from.
- rev-7 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edge to `TOOL-dPlacedRequest-63`, mirroring its consumes-from.
- rev-8 · 2026-11-19 · §2 S13, S21, S25, S30 · §4 The claim offline · §6 AC13, AC21, AC25, AC34 · §10 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit`:
  finding 10 (H2), S21 and AC21 read the protocol's limit row by path at build time, its headroom is
  zero, and S21's shorter row nets `TOOL-dPlacedRequest-34` S35's added bytes; finding 15 (H3), the
  node lock is the shared `write_dir_lock` family under the stem `node`; finding 39 (L9), AC34 greps
  only `check_claim_push_clear`, a name the map holds at the base. §7 also names `tier2-review self-test`, the leg(s) the spec-token guard join names for this spec's Files touched.
- rev-9 · 2026-11-19 · §2 S18, S22 · §4 Files touched · §6 AC18, AC22 · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`: finding 2 (H1), S22 and AC22 read 48128 on
  one dated measurement, the cut already made at the disposal; finding 14 (L8), S18 spells
  `runLiveness`' whole option set and AC18 plants a grandchild holding stdout; finding 23 (M11), §7
  names `policy fixtures`.
- rev-10 · 2026-11-19 · §2 S22 · §4 Evidence, Files touched · §5 · §6 AC18, AC22 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: findings 1, 6 and 13 (M1), unit 34 measured
  47885 bytes at rev-12, PINNED 2026-11-19, no cut already made; finding 14 (L5), S22 and AC22 measure and cut every
  live spec of the set over 48128; finding 8 (M4), §4 names both `spawnSync('git'` calls and AC18
  counts `windowsHide` in `readCard`'s body; finding 16 (M7), the user-docs line; finding 17 (M8),
  the map in this pass.
- rev-11 · 2026-11-20 · §1 · §2 S1 to S34 · §3 Edges · §4 Evidence, The closing mechanism, The bounded
  call, The requests lock, Files touched, Alternatives rejected · §5 · §6 AC1 to AC33 · §7 · §8 F1, F4 to
  F7 · re-grounded before dispatch by `2026-11-20-prompt-TOOL-dPlacedRequest-43-reground-brief`: each
  item probed against the tree and cited by `path#symbol`; S5, S6, S8, S10, S12, S13, S21, S25 to S27,
  S29, S31 and S34 closed by the units they name, their criteria taken out; S1 to S4, S7, S15 and S32
  narrowed to observations of built code; S11's naming line lands in §4, spec 33 and spec 34 untouched
  (F4); S22 measures the live specs with the checker's size join and names an owed cut, cutting
  nothing (F5); `TOOL-dPlacedRequest-44` S3 and `TOOL-dPlacedRequest-48` S4 folded here, AC24 running
  unit 44's §4 oracle and AC30 naming unit 48's placed-race arm (F6); S16's bound named
  `CARD_PUBLISH_BOUND` (F7); S18, S19, S20, S23, S28 and S30 amended to the symbols the tree holds;
  line citations swapped for symbol citations.

## 10. Reuse audit

Each item extends the code its finding names, and the new code extends four seams:
`TOOL-dPlacedRequest-24`'s `write_dir_lock_wait` for S30, the queue's own hold
(`tools/unattended/unattended.sh#write_gov_queue_hold`) its pattern; `resolve_card_driver`
(`skills/session-kickoff/manifest-check.sh#resolve_card_driver`), which S19's helper calls for the
checks two of its four callers already share; the `CARD_*_BOUND` default declarations for S16; and
`tools/unattended/stop-guard.js#runLiveness`'s option set for S18.
`python tools/codebase-map/reuse_lookup.py "bounded driver call from the kickoff engine with a timeout"`
ranked `engine`, `drive`, `run_driver` and `boundedParallel`, name stems only, none the engine's
call; `"node-local directory lock around a check then copy"` ranked `check`, `checks` and
`check_line`, none a lock. `python tools/memory-recall/query.py` over a minors batch re-grounded
before build returned KICK-dKeptSession-65 and -64 and TOOL-aEvidencedLens-20, batches of the same
kind; none disagrees with source.

Recall terms used: minors batch reground closed spec P19 in-place rewrite promoted fix fold size join live spec owed cut
