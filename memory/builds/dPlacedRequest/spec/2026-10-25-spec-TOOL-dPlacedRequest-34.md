# TOOL-dPlacedRequest-34 — the round-1 spec audit's minors: one fetch and one cache, honest censuses and counts, every reader of a moved name, and bounded walks

**Status:** INPROGRESS · rev-14 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 22 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 |
| [2026-10-25-build-TOOL-dPlacedRequest-34-deviation-341.md](../build/2026-10-25-build-TOOL-dPlacedRequest-34-deviation-341.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-34-deviation-342.md](../build/2026-10-25-build-TOOL-dPlacedRequest-34-deviation-342.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md) | research | TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-26-build-TOOL-dPlacedRequest-34-deviation-343.md](../build/2026-10-26-build-TOOL-dPlacedRequest-34-deviation-343.md) | deviation | — |
| [2026-11-19-build-TOOL-dPlacedRequest-34-design-notes.md](../build/2026-11-19-build-TOOL-dPlacedRequest-34-design-notes.md) | research | — |
| [2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md) | journal | — |
| [2026-11-20-build-TOOL-dPlacedRequest-34-red-fix-28.md](../build/2026-11-20-build-TOOL-dPlacedRequest-34-red-fix-28.md) | red-fix | — |
| [2026-11-20-build-TOOL-dPlacedRequest-34-red-fix-29.md](../build/2026-11-20-build-TOOL-dPlacedRequest-34-red-fix-29.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 |
| [2026-10-26-prompt-TOOL-dPlacedRequest-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dPlacedRequest-1-parents-reground.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-21 |
| [2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-16 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-12-pass-red-fix-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-12-pass-red-fix-brief.md) | research | TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-34-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-34-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-34-item-divergence-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-34-item-divergence-brief.md) | research | — |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 |
| [2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`)
confirmed 70 findings, its eleven highs units 23 to 33. This unit is BUILD-METHOD M4's batch of the
other 50 MEDIUM and 9 LOW, one item per raw id naming its finding and review item. At order 22 each
item amends its named unit's code. ACn observes Sn.

## 2. Scope (IN)

- **S1** — finding 2 (M1). Over unit 27's per-ref rule, two deletions of one ref around a re-create
  leave two deletion lines in `gov-feed.log`. Observed by AC1.
- **S2** — finding 11 (M2). Over unit 28's `read_feed_lease_tip`, an offer over a pruned, sighted unit
  tombstone exits 1 printing `tombstone`. Observed by AC2.
- **S3** — finding 3 (M3). `read_feed_lease_tip` skips deletion events for the ref's newest real
  commit, so a create after `--lease prune` parents on the pruned tip at its epoch plus one. Observed
  by AC3.
- **S4** — finding 61 (M4), the skeptic's fix. A feed-named commit `git cat-file -e` cannot read prints
  `unreadable`: a build or unit lease create refuses `epoch-fence`, and a cadence or legacy run claim
  takes unit 16's plain create. Observed by AC4.
- **S5** — finding 4 (M5). Every governance fetch lands in `refs/gov/remote/` through `observe_remote`
  with `--no-write-fetch-head`, then calls `add_feed_sightings`, the card lookup (S12) and unit 14 S3's
  request read included. `write_gov_ref`'s success exit is `write_feed_success <ref> <commit or
  empty>` in `gov_feed_sh`, which sets or clears the cache ref and appends, and joins unit 13's
  `FEED_WRITER_HELPER_FNS`. Observed by AC5.
- **S6** — finding 35 (M5). The lander's fenced push (unit 15 S5) calls `write_feed_success` in place
  of `add_feed_event`, so the cache names the landed beat. Observed by AC6.
- **S7** — finding 5 (M6). Route rule R7 (unit 2 S9) reads `refs/gov/remote/builds/<slug>/card`, the
  cache ref a publish sets, so a terminal follow refuses the next route there. Observed by AC7.
- **S8** — finding 25 (M6). No code writes or reads `refs/gov/builds/<slug>/card` locally.
  **Readers:** by name: READER NOT IN TREE, since its only readers, unit 2's S6 refspec and S9's R7,
  move here. by value: NO VALUE READERS, since nothing counts the local ref. Observed by AC8.
- **S9** — finding 65 (M6). The lookup fetches from the remote `resolve_claim_remote` resolves, never a
  literal `origin`. Observed by AC9.
- **S10** — finding 33 (M7). The kickoff engine sets no `GOVREF_` name and calls no `write_gov_ref`;
  it writes by `--card-ref write` (unit 33) and reads by `--card-ref lookup`. Observed by AC10.
- **S11** — finding 66 (M7). The engine runs `--card-ref lookup` into a file under `timeout -k 2
  "$CARD_FETCH_BOUND"`, stdin `/dev/null`; a silent driver reads the next store, printing `evidence`.
  Observed by AC11.
- **S12** — finding 32 (M8). `--card-ref lookup <slug>` is read-only: it fetches
  `+refs/gov/builds/<slug>/card:refs/gov/remote/builds/<slug>/card` in S5's shape from S9's remote and
  prints the commit id and message, or `card-ref — off`. `print_replay` calls it, so a replay writes
  no `FETCH_HEAD`. Observed by AC12.
- **S13** — finding 34 (M9). The kickoff engine carries no `gov_ref_sh` or `gov_feed_sh` block, so the
  `python resolver` guard needs no `skills/` path. Observed by AC13.
- **S14** — finding 7 (M10). `--entry-claim` never queues its create nor writes a folder: an
  unanswered read answers as §4's table says, which unit 3's `awaiting` row and unit 21 S5's
  `offline` row route. Observed by AC14.
- **S15** — finding 71 (M10). With no queued claim, no flush lands a folderless claim and no yield
  loses one; a rerun reads the slug claimed or taken. Observed by AC15.
- **S16** — finding 8 (M11). `scan_feed_writers` reads each `name() {` to its column-0 `}` as a scope,
  and a file's top-level body as one more. Observed by AC16.
- **S17** — finding 70 (M12). The census joins `\`-continued lines first, and flags a scope holding a
  `push` and a `--force-with-lease`, or a variable assigned it, that calls no helper-list name. Both
  limbs of unit 13's census read the joined lines, comments skipped. Observed by AC17.
- **S18** — finding 9 (M13). `placement.py --fixture --plant claim-lines` asserts `record` prints the
  block's `disposition`, `build`, `playbook`, `reason`, `scenarios` and `facts` lines and no earlier
  block's, `check:` or `placer:` line, as unit 4's AC8 reads. Observed by AC18.
- **S19** — finding 10 (M14). Unit 20 AC6's history check reads what the fence guarantees: epochs never
  fall, none under A's session reads n+1, and each rise is a holder change. Observed by AC19.
- **S20** — finding 13 (M15). Unit 3's `item.entry.orient` row carries `map = "base"`, as unit 6 §3
  says. Observed by AC20.
- **S21** — finding 14 (M16). With five refusals, unit 14's places 2 to 5 print `1/4` to `4/4` and the
  sixth exits 3 printing `pre-claim budget exhausted`. Observed by AC21.
- **S22** — finding 15 (M17). `--lease status <kind> <name> [<sub>]` is read-only and prints `<tail>
  <fleet tag> <session> <status> <verdict> <epoch>` TAB-separated, or `lease — none · <tail>`;
  `placement.py check` reads it, never `--claims`. Observed by AC22.
- **S23** — finding 16 (M18). With `RUN_CLAIMS` off, every `--lease` act but `fence` prints `lease —
  off · <tail>`, writes nothing and exits 0; `fence` keeps unit 15 S2's line. Observed by AC23.
- **S24** — finding 37 (M19). The pre-push claim fast path (`.githooks/pre-push:851-870`) accepts a
  `tree 0` candidate whose first parent is `missing` or a `tree 0` commit, adding `<sha>^^{tree}` to
  its one `cat-file --batch-check`. Observed by AC24.
- **S25** — finding 23 (M19), the skeptic's fix. A parented claim beat pushed alone sources no
  `straggler-guard.sh`, staged against the base predicate (`:866`). Observed by AC25.
- **S26** — finding 24 (M20). `memory/map/features/unattended-stops.md` (`:58-66`) describes the
  parented chain and the default-branch-only clear, and the claim block's header stops saying the hook
  clears both verdict files on every push. **Readers:** by name: `claim-push.lock`, spelled there at
  `:61-65` and by `memory/gotchas/decision-re-derived-by-a-second-process.md:66` and `:74`, both
  rewritten. by value: NO VALUE READERS after unit 11 S6. Observed by AC26.
- **S27** — finding 49 (M20). That gotcha gains a dated paragraph naming unit 11's removal of the lock
  and what serialises the two pushes now. Observed by AC27.
- **S28** — finding 26 (M21), the skeptic's fix. `readCard` resolves bash in
  `tools/lib/resolve_bash.py#resolve_bash`'s run-each-candidate order, as
  `tools/policy/policy-mirror.js#resolveBash` ports it, probing `test -f` on the checker it runs
  (`TOOL-dWitnessedBar-26`'s `resolve_bash.js` once landed); it folds `/c/…` output through
  `tools/hooks/scratch-guard.js#buildNativePath` and reads a silent checker as no card, named.
  Observed by AC28.
- **S29** — finding 27 (M22). Unit 1's fixture is hermetic: `render_playbook.py --fleet-tag` takes
  `--fleet <path>`, the fixture plants `fleet.toml` and `COMPUTERNAME`, and an empty-`host` row
  resolves by user. Observed by AC29.
- **S30** — finding 38 (M22). `resolve_fleet_tag` asks `read_fleet` by user alone, case-folded,
  honouring a `GOV_NODE` that names a `fleet.toml` tag; `--host` is dropped. **Readers:** by name:
  READER NOT IN TREE, since `--host` and its caller are unit 1 S11's. by value: NO VALUE READERS.
  Observed by AC30.
- **S31** — finding 28 (M23), the skeptic's fix. `loop placement fixtures` (unit 4) and `loop claim
  fixtures` (unit 21) each state a subject, a chunk, a ceiling and their unit's `enforces` in
  `tools/gate-legs.json`, and a `selftest-budgets.txt` row when held. Observed by AC31.
- **S32** — finding 47 (M23). Per leg, `tools/govkit/subject-pins.tsv` gains its row and
  `memory/map/features/loop.md` claims its key. Observed by AC32.
- **S33** — finding 36 (M24). Over unit 24's `write_dir_lock`, two breakers racing one stale
  `gov-feed.lock` append unique `seq` values. Observed by AC33.
- **S34** — finding 39 (M25). `loop_lib.load_tree_lib` takes a module name and its `need` tuple, keeping
  its skew refusal; `tools/loop/request.py` and every loop module load memory-tree modules only through
  it. Observed by AC34.
- **S35** — finding 44 (M26). Every reader of the moved claim ref follows it:
  `tools/unattended/resume-tick.test.sh`'s GH1 AC12 and GH11 AC1 arms (`:872-909`) read
  `refs/gov/leases/tRun/build`; `tools/unattended/.unattended.conf.example:159` and `:163`,
  `.unattended.conf:156`, `tools/unattended/PROTOCOL.template.md:521`,
  `tools/unattended/VERBS.template.md:279` with their renders, and
  `memory/map/features/unattended-stops.md:56` name `refs/gov/leases/<slug>/build`. **Readers:**
  by name: `refs/gov/runs/<slug>`, spelled by each file listed. by value: NO VALUE READERS beyond
  `read_claims`' legacy read (unit 1 S4). Observed by AC35.
- **S36** — finding 45 (M27). `skills/session-kickoff/SKILL.md` stays within its
  `tools/template-size-limits.txt` row, read at build time: units 2, 3 and 9's resume text lives in
  `skills/session-kickoff/RESUME.md`, pointed at in one line. Observed by AC36.
- **S37** — finding 46 (M28). `memory/guides/UNATTENDED-PROTOCOL.md` stays within its row, read at
  build time: the verbs guide names unit 5's third opt-in source and the protocol points there; unit
  43 S21's shorter `RUN_CLAIMS` row nets S35's bytes against the row's zero headroom. Observed by
  AC37.
- **S38** — finding 48 (M29). A unit minting or deleting a function regenerates the map in its own
  pass; this pass's `gen_map.py --write` re-checks `memory/map/generated/` over the final tree, so `symbols.json` names every minted function and none deleted. **Readers:** by name:
  READER NOT IN TREE, since TOOL-aPiecewiseGrade-6 renamed `write_claim_push_lock`'s family. by value:
  NO VALUE READERS. Observed by AC38.
- **S39** — finding 50 (M30). `derive_claims_line`'s ranking gains `released`, hidden past
  `CARD_CLAIMS_HIDE_S` as `stale` and `terminal` are. Observed by AC39.
- **S40** — finding 57 (M31). The offline queue writes `-` for an empty cached tip, as `CLAIM_ROWS`
  does (`tools/unattended/unattended.sh:2112-2113`), and the flush maps `-` back to empty. Observed by
  AC40.
- **S41** — finding 58 (M32), F-S41. With no record, `--request-draw` creates it from the kept copy
  `<git-common-dir>/requests/<key>.md` that `--request` wrote, by `write_request_record` under no
  session once `request.py key` keys it to `<key>`; with neither it exits 2 naming `--request
  <file>`, creating nothing (`tools/unattended/unattended.sh#run_request_draw`, unit 14). No flag is
  added. Observed by AC41.
- **S42** — finding 59 (M33). A draw site reading exit 2 stops: `place` prints `placement: pre-claim
  draw not recorded — <why>` and writes no block, and `entry.claim` exits 2. Observed by AC42.
- **S43** — finding 60 (M34). The age pass is one streaming `git log --first-parent` over the cached
  lease refs piped to an `awk` that resolves each tail at its renewing beat, its tenure's start (unit
  26) or a commit sighted over `leases.expiry-hours` ago (`stale`), and exits once all resolve.
  Observed by AC43.
- **S44** — finding 62 (M35). Unit 12's S6 refuses a subject, item or fork holding a byte below 0x20
  or 0x7f, exit 2 naming the field. Observed by AC44.
- **S45** — finding 63 (M36). A failed cache-ref update prints one `feed: NOTE -` line, still appends
  and returns 0; unit 12 S1 refuses an encoded segment over 200 bytes. Observed by AC45.
- **S46** — finding 67 (M37), the skeptic's fix. `RESUME.md`'s `restart-item`: `git add -A`; commit
  to `partial/<slug>/<sid8>`, suffixed `-2` on a clash; verify the branch by `git rev-parse`; only then
  restore the tree, else refuse naming the cause. Observed by AC46.
- **S47** — finding 68 (M38). `probe.pin` writes the head to `<key>.probe.md`, its blob recorded
  before `run`, which refuses a moved head; a later trigger opens `<key>.probe-2.md`. Observed by
  AC47.
- **S48** — finding 69 (M39). `write-set` reads a spec of any status through `--path-tokens
  --files-touched --any-status`, printing `unarmed — write-set: <spec> lists no path` on none.
  Observed by AC48.
- **S49** — finding 72 (M40). `--lease offer` refuses `offered` over an open offer, and a `--to` naming
  the caller's bare tag or `<tag>/<own session>`; another session on the caller's tag lands (unit 20
  S1). Observed by AC49.
- **S50** — finding 73 (M41). A manifest bullet is its `- ` line plus each following line indented two
  or more spaces, up to the next bullet or blank line, joined by single spaces. Observed by AC50.
- **S51** — finding 12 (L1). Each of unit 8 §4's thirteen items is seeded. Observed by AC51.
- **S52** — finding 17 (L2). `check_probe_outcomes` exempts `item.probe.*` rows. Observed by AC52.
- **S53** — finding 18 (L3). Every inline `gov_ref_sh` and `gov_feed_sh` copy, the lander's included,
  cuts equal to its canonical, and §7 names `python resolver`. Observed by AC53.
- **S54** — finding 19 (L4). The offer refuses a build or unit tombstone with `tombstone`, `terminal`
  kept for cadence and legacy claims. Observed by AC54.
- **S55** — finding 29 (L5). Unit 18 AC4's parity probe prints `unarmed — tag_index.py does not
  resolve` and exits 2 while `tools/playbook/tag_index.py` is absent. Observed by AC55.
- **S56** — finding 30 (L6). The two commit-size figures are restated from measured commits in the
  design record. Observed by AC56.
- **S57** — finding 31 (L7). The design record states the one `refs/gov` deletion in product code
  outside the lease namespace, through `remove_gov_ref`, in place of unit 16 §10's sentence.
  Observed by AC57.
- **S58** — finding 40 (L8). `tools/loop/request.py` is new in this build, in dDeclaredLoop's loop kit,
  and §3 carries the edge unit 19 omits. Observed by AC58.
- **S59** — finding 41 (L9), the skeptic's fix. No commit hand-moves `KIT_UNATTENDED_VERSION` or
  `KIT_RUN_GATES_VERSION`; the lander mints them (TOOL-aMendedFleet-65). Observed by AC59.

## 3. Non-goals (OUT)

- No high finding: units 23 to 33.
- No second mechanism for a twin: S1 and S2 observe units 27 and 28.
- No change to I6's record keys or I11's content key.
- No re-wording of any reviewed spec: each item states its correction here and amends the code.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-1` — the lease verbs, fleet tag resolver, offline queue and moved claim ref
- **consumes-from** `TOOL-dPlacedRequest-2` — the card's lookup, route rule R7 and the resume act
- **consumes-from** `TOOL-dPlacedRequest-3` — the entry items' rows and outcome table
- **consumes-from** `TOOL-dPlacedRequest-4` — `placement.py` and its new leg
- **consumes-from** `TOOL-dPlacedRequest-5` — its protocol clause
- **consumes-from** `TOOL-dPlacedRequest-6` — the `map` slot declarations
- **consumes-from** `TOOL-dPlacedRequest-7` — the probe pin and `check_probe_outcomes`
- **consumes-from** `TOOL-dPlacedRequest-8` — the seed resolver and `--path-tokens`
- **consumes-from** `TOOL-dPlacedRequest-9` — the manifest conversion and its kickoff sentence
- **consumes-from** `TOOL-dPlacedRequest-10` — `placement.py record`'s new lines
- **consumes-from** `TOOL-dPlacedRequest-11` — the parented claim commit, `remove_gov_ref` and the lock's retirement
- **consumes-from** `TOOL-dPlacedRequest-12` — the register record and its encoder
- **consumes-from** `TOOL-dPlacedRequest-13` — the feed's success exit, sightings, census and its helper list
- **consumes-from** `TOOL-dPlacedRequest-14` — the draw verb and its sites
- **consumes-from** `TOOL-dPlacedRequest-15` — the lander's fenced beat and inline block
- **consumes-from** `TOOL-dPlacedRequest-16` — `released` and the prune
- **consumes-from** `TOOL-dPlacedRequest-17` — the age pass
- **consumes-from** `TOOL-dPlacedRequest-18` — its parity probe
- **consumes-from** `TOOL-dPlacedRequest-19` — `request.py` and `--request`
- **consumes-from** `TOOL-dPlacedRequest-20` — the offer act and its history check
- **consumes-from** `TOOL-dPlacedRequest-20` — S1's `--to <tag>/<session>` form, which S49 admits for another session
- **consumes-from** `TOOL-dPlacedRequest-21` — `--entry-claim` and its new leg
- **consumes-from** `TOOL-dPlacedRequest-24` — the guarded node lock factory and the queue line
- **consumes-from** `TOOL-dPlacedRequest-26` — the tenure-bounded walk
- **consumes-from** `TOOL-dPlacedRequest-27` — the per-ref append rule
- **consumes-from** `TOOL-dPlacedRequest-28` — `read_feed_lease_tip`
- **consumes-from** `TOOL-dPlacedRequest-33` — the `--card-ref` verb
- **consumes-from** external — dDeclaredLoop's loop kit `tools/loop/` and `loop_lib.load_tree_lib` (TOOL-dDeclaredLoop-19, -20, -92), which S34 and S58 extend
- **consumes-from** `TOOL-dPlacedRequest-40` — the exempt act list, which `--lease status` joins by name
- **hands-off** `TOOL-dPlacedRequest-35` — S43's bounded walk, whose stops that unit orders with the tenure first
- **hands-off** `TOOL-dPlacedRequest-43` — this spec's size, S30, S35, S40, AC35, AC38 and AC59, which that unit's items keep, correct and re-observe
- **hands-off** `TOOL-dPlacedRequest-49` — AC59, which that unit's item for finding 5 points at unit 44's oracle
- **hands-off** `TOOL-dPlacedRequest-52` — AC59's observation, which that unit's item for finding 11 restates as the oracle's header line
- **hands-off** `TOOL-dPlacedRequest-54` — AC59, which that unit cuts to one line pointing at 44 AC1
- **hands-off** `TOOL-dPlacedRequest-57` — AC59, from which that unit drops the base
- **hands-off** `TOOL-dPlacedRequest-59` — this spec's size, which that unit cuts in prose if over 48128
- **hands-off** external — `TOOL-dWitnessedBar-26`'s site census, which gains `scratch-guard.js`'s `readCard` (S28)

## 4. Design

The evidence, the walk's reasoning (S43), the commit sizes (S56), the deletion (S57), `readCard`'s
cost (S28) and the alternatives rejected are in the design record
`memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-34-design-notes.md`.

### The claim offline (S14, S15)

| `leases.offline` | `--entry-claim`, remote unanswered | exit | unit 3 outcome |
|---|---|---|---|
| `warn`, `follow-leases` | `claim not written — offline` | 4 | `awaiting` |
| `refuse` | `lease refused — offline` | 1 | `refused` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `write_feed_success` | shell function, in `gov_feed_sh` | `write`, OK |
| `--card-ref lookup` | driver verb act | none |
| `--lease status` | driver verb act | none |
| `--any-status` | `--path-tokens` flag | none |
| `--fleet` | `render_playbook.py --fleet-tag` flag | none |
| `skills/session-kickoff/RESUME.md` | kickoff engine guide | none |
| `claim not written — offline`, `lease — off`, `placement: pre-claim draw not recorded` | output lines | none |

### Files touched (estimate)

- `tools/lib/gov-feed.sh`
- `tools/lib/gov-ref.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/resume-tick.test.sh`
- `tools/unattended/.unattended.conf.example`
- `.unattended.conf`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/STOPS.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `tools/run-gates/post-merge.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `.githooks/pre-push`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/card-store.fixture.sh`
- `skills/session-kickoff/SKILL.md`
- `skills/session-kickoff/RESUME.md`
- `tools/playbook/render_playbook.py`
- `tools/loop/loop_lib.py`
- `tools/loop/request.py`
- `tools/loop/placement.py`
- `tools/loop/budget.py`
- `tools/loop/claim.py`
- `tools/loop/probe.py`
- `tools/loop/loop.toml`
- `tools/govkit/steps/kickoff_facts_to_overlay.py`
- `.githooks/pre-push.test.sh`
- `tools/gate-legs.json`
- `tools/run-gates/selftest-budgets.txt`
- `tools/govkit/subject-pins.tsv`
- `memory/map/features/loop.md`
- `memory/map/features/unattended-stops.md`
- `memory/gotchas/decision-re-derived-by-a-second-process.md`
- `memory/map/generated/symbols.json`
- `tools/lib/resolve-python.test.sh`
- `help/loop.md`

## 5. Production-readiness checklist

- security — S44 closes key-line injection; S10 to S13 leave the engine no writer; S23 states the
  off outcome.
- perf / scale — S24 restores the claim fast path; S43 bounds the age pass; S12 spares `FETCH_HEAD`.
- error / empty / loading states — S4, S42 and S45 each name an outcome left undefined.
- observability — every new outcome is one named line.
- risks — S36 moves kickoff text behind one pointer; S43's early `stale` is the verdict anyway.
- testing — the probes of §6 and the arms of §7.
- migration — none: every item lands before anything it amends ships.
- user docs — the verbs, stops and protocol guides, `RESUME.md`, and `help/loop.md`'s `--lease` and
  `--card-ref` anchors, refreshed for `status` and `lookup`.

## 6. Acceptance criteria

Fixtures are the named unit's own unless an item names one.

- **AC1** — When a probe deletes, re-creates and deletes one ref through `write_gov_ref`, the feed
  holds two deletion lines for it. Red when: the second deletion is dropped.
- **AC2** — When `--lease offer unit tFix TOOL-tFix-2 --to b` runs over a deleted, sighted unit
  tombstone, it exits 1 printing `tombstone`. Red when: the offer re-creates it.
- **AC3** — When `--lease prune` deletes a terminal run lease at epoch 3 and `--lease acquire run
  maintain 2026-10` follows on that node, the record reads `epoch: 4` parented on the pruned tip.
  Red when: the create restarts at 1.
- **AC4** — When `git prune --expire=now` makes the feed-named commit unreadable, a unit lease
  acquire exits 1 printing `epoch-fence` and a run lease acquire creates at epoch 1. Red when: a
  build or unit lease restarts its epoch.
- **AC5** — When clone A writes a card over clone B's card commit, `--feed check` exits 0. Red when: a
  commit fetched outside the sighting hook reads `missing`.
- **AC6** — When unit 15's fixture lands a fenced push, `git rev-parse
  refs/gov/remote/leases/tFix/build` names the beat and `--feed check` exits 0. Red when: it prints
  `extra`.
- **AC7** — When `--card --follow --terminal` runs and a same-node route to that build follows with
  no lookup, `manifest-check.sh` refuses it naming R7. Red when: R7 reads a ref no publish moved.
- **AC8** — When `git grep -n 'refs/gov/builds/[^ ]*:refs/gov/builds'` runs over
  `skills/session-kickoff/manifest-check.sh` and `tools/unattended/unattended.sh`, it prints nothing.
  Red when: a second local card name remains.
- **AC9** — When `card-store.fixture.sh --plant lookup` runs in a clone whose remote is `upstream`,
  the lookup reads the card. Red when: the fetch names `origin`.
- **AC10** — When `grep -n 'GOVREF_\|write_gov_ref' skills/session-kickoff/manifest-check.sh` runs,
  it prints nothing. Red when: the engine holds the writer's contract.
- **AC11** — When `card-store.fixture.sh --plant lookup-hung` runs with a silent stub driver, the
  lookup prints `evidence` within the bound plus 3 s. Red when: it hangs.
- **AC12** — When `card-store.fixture.sh --plant replay` runs, `FETCH_HEAD`'s mtime is unchanged.
  Red when: a replay writes it.
- **AC13** — When `git grep -n '# >>> gov_ref_sh\|# >>> gov_feed_sh' -- skills/` runs, it prints
  nothing. Red when: an unguarded copy ships in the engine.
- **AC14** — When the origin is renamed away and `--entry-claim` runs, it exits 4 printing `claim not
  written — offline`, nothing queued and no README; under planted `refuse`, 1 printing `offline`.
  Red when: a claim queues or a folder is written.
- **AC15** — When the origin returns after another node claims the slug and `--entry-claim` reruns,
  it prints the slug-taken line. Red when: a claim lands folderless or is lost silently.
- **AC16** — When `scan_feed_writers` reads a file whose top-level body pushes with
  `--force-with-lease` and never appends, it prints that line; over `tools/push-main.sh`, nothing.
  Red when: a top-level writer escapes, or a correct one is flagged.
- **AC17** — When it reads a `\`-wrapped push, a `git push "${args[@]}"` whose array holds
  `--force-with-lease`, neither appending, and a `\`-wrapped plain push of `refs/gov/mail/fx/a/s1`, it
  prints all three. Red when: any escapes.
- **AC18** — When `python placement.py --fixture --plant claim-lines` runs after unit 10's lines land,
  it passes, printing the six claim lines and no history. Red when: unit 10's lines red it.
- **AC19** — When `TOOL-dPlacedRequest-20`'s fixture runs the corrected check over a chain of renews and an offer it
  passes, and with a take at a fallen epoch it fails. Red when: either verdict inverts.
- **AC20** — When `python loop_lib.py --check` runs, it lists `item.entry.orient` with `map base`.
  Red when: the item reads `map none`.
- **AC21** — When unit 14's fixture plants five refusals, places 2 to 5 print `1/4` to `4/4` and the
  sixth exits 3 printing `pre-claim budget exhausted`. Red when: a count is off by one.
- **AC22** — When two same-node sessions read one build lease, `--lease status build tFix` prints the
  holder's session and `placement.py check` refuses `amend` for the other. Red when: a session reads
  another's lease as its own.
- **AC23** — With `RUN_CLAIMS` off, `--lease acquire build tFix` prints `lease — off · tFix/build`,
  exits 0 and writes nothing, and `--lease fence build tFix` prints `fence — none`. Red when: an off
  switch writes, hangs or refuses.
- **AC24** — When `.githooks/pre-push` reads, in a scratch clone, one stdin line pushing a parented
  claim beat alone, a stub `straggler-guard.sh` beside it prints no marker. Red when: the parented
  shape takes the slow path.
- **AC25** — When that line is fed to a scratch hook staged back to the base `<sha>^ missing` test, the
  stub prints its marker. Red when: the two predicates read alike.
- **AC26** — When `git grep -n 'claim-push.lock' -- memory/map/features/ memory/gotchas/` runs, it
  hits only the gotcha's dated paragraph. Red when: a reader still calls the lock live.
- **AC27** — When `grep -n 'TOOL-dPlacedRequest-11'` runs over the S26 gotcha, a dated paragraph
  names the lock's removal. Red when: the gotcha stops at the lock.
- **AC28** — When a `node -e` probe calls `readCard` with a stub checker printing a `/c/` path, it
  reads the card at the `C:/` path; with a non-running bash first on PATH and a working one second,
  it reads the card. Red when: the MSYS path, or a stub bash, reads as no card.
- **AC29** — When unit 1's fixture plants a `fleet.toml` with an empty-host row and a `COMPUTERNAME`,
  `--lease acquire build tFix` takes `fleet-tag` from that row. Red when: it rests on the machine.
- **AC30** — When `USERNAME` matches a row in another case and `GOV_NODE` is unset, the tag resolves;
  with `GOV_NODE` naming an unregistered tag, the verb exits 2. Red when: case or host refuses a node.
- **AC31** — When `python -c` reads `tools/gate-legs.json`, both legs carry a subject, a chunk, a
  ceiling and a non-empty `enforces`. Red when: a leg lacks one.
- **AC32** — When `python tools/govkit/govkit.py selfcheck` and `gen_map.py --check` run, both exit 0
  with the two legs present. Red when: a pin row or claim is missing.
- **AC33** — When two background appenders break one planted stale `gov-feed.lock`, `cut -f1
  gov-feed.log | sort | uniq -d` prints nothing. Red when: two events share a `seq`.
- **AC34** — When `git grep -n -F 'resolve_kit_dir("memory-tree"' -- tools/loop/` runs, it prints only
  `loop_lib.py`'s loader; with a skewed kit planted, `request.py key` prints the named refusal.
  Red when: an ImportError escapes, or a second module resolves the kit.
- **AC35** — When `git grep -n 'refs/gov/runs/<slug>\|refs/gov/runs/tRun'` runs over S35's files, it
  prints only legacy-read mentions. Red when: a reader still names the old home.
- **AC36** — When `tr -d '\r' < skills/session-kickoff/SKILL.md | wc -c` runs, it prints at most the
  figure `awk -F'\t' '$1=="skills/session-kickoff/SKILL.md"{print $2}' tools/template-size-limits.txt`
  prints, and `grep -n RESUME.md skills/session-kickoff/SKILL.md` finds the pointer. Red when: the
  size leg reds.
- **AC37** — When `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c` runs, it prints at most
  that path's figure in `tools/template-size-limits.txt`, read as AC36 reads it. Red when: the
  protocol size leg reds.
- **AC38** — When `python tools/codebase-map/gen_map.py --check` runs, it exits 0 and `grep -c
  check_claim_push_clear memory/map/generated/symbols.json`, a name unit 11 S6 deletes, prints 0.
  Red when: the map is stale.
- **AC39** — When `manifest-check.sh --card --write` runs over a fixture holding a `released` lease,
  it prints a `claims —` count line, not `skipped:`. Red when: `released` hides the cell.
- **AC40** — When unit 1's AC7 queues an offline create and the origin returns, `--lease flush` lands
  it. Red when: the empty field shifts the line.
- **AC41** — When unit 14's fixture runs `--request-draw 0123456789ab --cause route-back --item
  item.entry.place` with no record and no kept copy, it exits 2 naming `--request <file>` and the
  origin holds no such ref; when it deletes a recorded key's ref from the origin, keeping the kept
  copy, the same draw exits 0 printing its row over a re-created parentless record. Red when: a
  kept copy creates no record, or a draw with neither writes one.
- **AC42** — When unit 14's fixture plants `--plant unreachable`, `place` prints `pre-claim draw not
  recorded` and writes no block. Red when: placement proceeds.
- **AC43** — When `--claims` reads a planted 10,000-commit lease chain whose last 50 commits were
  sighted within the bound, it runs at least five times faster than a copy walking every commit.
  Red when: the walk reads the whole chain. figure: DERIVED, a ratio of two timings.
- **AC44** — When `--register problem` runs with a subject holding `\nsession: x`, it exits 2 naming
  `subject` and builds no commit. Red when: a key line is injected.
- **AC45** — When a probe holds `<git-common-dir>/refs/gov/remote/runs/tFix.lock` and writes the ref,
  `write_gov_ref` returns 0 with one `feed: NOTE -` line and the event appended; a 201-byte encoded
  subject is refused. Red when: a landed write returns non-zero.
- **AC46** — When `grep -n` runs over `RESUME.md` for `git add -A`, the suffix, `git rev-parse` and
  "restore only after", each is found in order. Red when: the restore comes first.
- **AC47** — When unit 7's fixture edits a probe's head between `pin` and `run`, `run` exits non-zero
  naming it; a second trigger writes `<key>.probe-2.md`. Red when: the pin is unchecked or a verdict
  is overwritten.
- **AC48** — When `python loop_lib.py seed item.build.unit-pass --unit <closed unit>` runs over a
  CLOSED fixture spec it prints its paths, and over one listing none `unarmed — write-set`. Red when:
  a closed write set reads empty.
- **AC49** — When clone A runs `--lease offer` over B's open offer to itself, it exits 1 printing
  `offered`; under `CLAUDE_CODE_SESSION_ID=s1`, `--to a` and `--to a/s1` exit 1 and `--to a/s2` lands
  as `offer: a/s2`. Red when: a node re-offers to itself, or the own-node offer is refused.
- **AC50** — When the manifest step's `up` runs over a §B holding one wrapped bullet, the unit row's
  `text` carries the whole bullet. Red when: it is truncated.
- **AC51** — When `python loop_lib.py seed` runs for each of unit 8 §4's thirteen item tags, each
  prints a seed or an `unarmed —` line. Red when: an item is unseeded.
- **AC52** — When `python loop_lib.py --check` runs over unit 7's rows it exits 0, and over a role row
  outside `item.probe.*` lacking `probe`, 1. Red when: the rule refuses its own rows.
- **AC53** — When `awk` cuts every `gov_ref_sh` and `gov_feed_sh` block in the tree, `cmp` finds each
  equal to its canonical cut. Red when: a copy drifts.
- **AC54** — When `--lease offer` runs over a build tombstone, it exits 1 printing `tombstone`.
  Red when: the cause reads `terminal`.
- **AC55** — When unit 18's parity probe runs with `tag_index.py` absent, it exits 2 printing
  `unarmed`. Red when: it reads as green.
- **AC56** — When `git cat-file -s` reads a lease commit in unit 1's fixture, it is within 15% of the
  design record's 630 bytes. Red when: that figure is off by more. figure: DERIVED at observation.
- **AC57** — When `git grep -n remove_red_ref -- tools/run-gates/post-merge.sh` runs, it prints the
  definition, whose body calls `remove_gov_ref`, and one call. Red when: the design record's
  account is false.
- **AC58** — When `git ls-files -- tools/loop` runs at the close it lists `request.py`, and `git
  cat-file -e` of that path at `c63aabbb` fails. Red when: the file pre-dates this build.
- **AC59** — When `git diff c63aabbb..HEAD -- tools/unattended/unattended.sh
  tools/run-gates/run-gates.sh` is grepped for `^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION=` before the
  lander's mint, it prints nothing. Red when: a branch commit hand-bumps a version.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `docs` · `branch-guard self-test` · `pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `push-main self-test` · `transition-audit arms` · `straggler-guard arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `playbook render selftest` · `kickoff engine size <=18KiB` · `unattended protocol size` · `codebase-map coverage + freshness` · `codebase-map gate coverage` · `harness arms (fail branches armed or pinned)` · `tier2-review self-test` · `policy fixtures`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC14 AC15 AC22 AC23 AC33 AC40 AC43 AC45 AC49 AC54 · each item's plant, staged against the unit it amends · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/push-main.test.sh · covers AC6 · the fenced landing's cache ref, staged against `add_feed_event` alone · its assertion count raised
New arm: .githooks/pre-push.test.sh · covers AC24 AC25 · a parented claim beat pushed alone, staged against the base `<sha>^ missing` predicate · its assertion count raised
New arm: tools/hooks/scratch-guard.test.sh · covers AC28 · a stub checker printing a `/c/` path and a stub bash first on PATH, staged against a bare `bash`, no fold and an existence-only resolver · none
New arm: tools/lib/resolve-python.test.sh · covers AC28 · a 2j row holding `readCard`'s order to `resolve_bash.py`'s, staged by a reorder · none
New arm: skills/session-kickoff/card-store.fixture.sh · covers AC7 AC9 AC11 AC12 AC39 · the terminal-route, hung-lookup, replay and released plants, staged against `TOOL-dPlacedRequest-2`'s local ref and fetch · none

## 8. Open questions

- **F1 — Where does the kickoff text that overflows SKILL.md go (S36)?** (a) `RESUME.md`; (b) a trim
  elsewhere, cutting other units' text; (c) a raised limit, an owner's ceiling. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How is the claim's offline outcome stated once (S14)?** (a) It never queues, `offline`
  routing to `awaiting` but under `refuse`; (b) a queued claim is `awaiting`, needing a yield to reach
  an ended session. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F3 — How is the age pass bounded (S43)?** (a) A streaming walk stopping at the first commit
  sighted before the window; (b) per-ref `git log -n`, a process per ref; (c) a `renewed-by` key,
  widening I6. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — Does `read_path_tokens` admit a backslash (S48)?** (a) No, unit 8's AC7 kept; (b) yes,
  amending a reader every caller of `read_files_touched` shares. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F-S41 — How does a draw create a request record it cannot find, when the landed draw already
  reads the clone's kept copy?** (a) S41 and AC41 are rewritten around the kept copy: the draw
  creates the record from `<git-common-dir>/requests/<key>.md` and refuses, naming the request verb,
  when no kept copy exists; (b) a `--request-text` flag as a second path. RESOLVED (agent,
  2026-11-20, delegated): (a), rung 3; one path for one act, the landed draw already holds it, and
  the kept copy is what the request verb wrote. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft from the round-1 audit's minors.
- rev-2 · 2026-10-25 · fix brief: under the ceiling; S8, S26, S30, S35, S38 answer check 25; S33 names
  `write_node_lock`; AC24, AC25, AC28 observe; built files by basename.
- rev-3 · 2026-10-25 · §3 · round-2 edge mirrors to units 40, 35, 43.
- rev-4 · 2026-10-25 · round-2 fix brief: under the ceiling, §4's fetch diagram and census into S5,
  S16, S17, edge lists cut, siblings spelled unit N.
- rev-5 · 2026-10-25 · §3 · round-3 edge mirror to unit 49.
- rev-6 · 2026-10-25 · §3 · round-4 edge mirror to unit 52.
- rev-7 · 2026-10-25 · round-4 fix brief: at most 47104 bytes, unit 43 S22's target, repetition cut
  and prose tightened; no item, criterion, edge or fork dropped.
- rev-8 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edge to `TOOL-dPlacedRequest-54`, mirroring its consumes-from.
- rev-9 · 2026-10-25 · §3 · round-5 edge mirrors to units 57, 59.
- rev-10 · 2026-10-26 · §2 S31 · §6 AC31, AC34 · re-grounded on dDeclaredLoop at `783f1ad3a` and
  dOrderedCharter at `462d20f35` by `build/2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md`,
  rows 78 and 80: both legs carry `enforces`; AC34's grep narrows to the memory-tree call, as
  TOOL-dDeclaredLoop-12 S4 puts playbook calls in `loop_lib.py`.
- rev-11 · 2026-11-19 · §2 S17, S33, S36, S37, S49 · §3 Edges · §4 Sizes · §6 AC17, AC36, AC37, AC38, AC49 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit`: finding 9 (H2), S36 and S37 and their criteria read each file's limit row in
  `tools/template-size-limits.txt` by path at build time, the protocol's headroom is zero and S35's
  added bytes are netted by TOOL-dPlacedRequest-43 S21; finding 15 (H3), S33 names the shared
  `write_dir_lock`; finding 22 (H5), S49 refuses only the caller's bare tag or its own session and
  AC49 lands an own-node offer to another session, with the consumes-from edge mirroring
  TOOL-dPlacedRequest-20's hands-off; finding 30 (L8), S17 restates the census's second limb and AC17
  plants a wrapped plain push; finding 39 (L9), AC38 greps a name present at the base. §7 also names `tier2-review self-test`, `policy fixtures`, the leg(s) the spec-token guard join names for this spec's Files touched.
- rev-12 · 2026-11-19 · §1 · §2 · §3 Edges · §4 · §5 · §6 · §7 · §8 · §10 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`: finding 2 (H1), cut under 48128 bytes, DERIVED, before
  it leaves DEFERRED, §4's evidence, walk, sizes, deletion and cost moved to the design record, no item,
  criterion, edge or fork dropped; finding 28 (H4), S57 and AC57 name `remove_gov_ref`;
  finding 17 (M5), S5 and S17 name unit 13's helper list.
- rev-13 · 2026-11-19 · §2 S28, S38 · §3 · §4 · §5 · §6 AC28 · §7 · §8 · §10 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: findings 11 (M5, S28, AC28), 16 (M7, `docs`)
  and 17 (M8, S38 a final re-check only).
- rev-14 · 2026-11-20 · §2 S41 · §6 AC41 · §8 F-S41 · folds
  `2026-11-20-prompt-TOOL-dPlacedRequest-34-item-divergence-brief`: S41 and AC41 restated over the
  kept copy `run_request_draw` already reads, the `--request-text` flag dropped; no other item moved.

## 10. Reuse audit

Each item extends its named unit's seam and the base code §2 and the design record cite, with the
claim fetch (`tools/unattended/unattended.sh:2136`) and the claims cell
(`skills/session-kickoff/manifest-check.sh:645-700`). `python tools/codebase-map/reuse_lookup.py` over
"append an event only when the ref's newest event differs" ranked name stems only
(`add_health_event`, `claims`): no seam fits beyond the units named. `python
tools/memory-recall/query.py` over "how does the feed avoid appending a retried write twice" returned
units 2 and 13 and the audit's items; none disagrees with source. S28 takes `resolveBash`'s order, not
`tools/roles/handoff.py`'s existence-only one.

Recall terms used: feed sightings cache census card lookup FETCH_HEAD parity size limit offline claim walk bound
