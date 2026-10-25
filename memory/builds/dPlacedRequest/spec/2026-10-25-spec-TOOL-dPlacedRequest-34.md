# TOOL-dPlacedRequest-34 — the round-1 spec audit's minors: one fetch and one cache, honest censuses and counts, every reader of a moved name, and bounded walks

**Status:** OPEN · rev-9 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 22 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 |
| [2026-10-25-build-TOOL-dPlacedRequest-34-deviation-341.md](../build/2026-10-25-build-TOOL-dPlacedRequest-34-deviation-341.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md) | research | TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`) exited
CONVERGED with 70 confirmed findings, its eleven highs units 23 to 33. This unit is BUILD-METHOD M4's
batch of the other 50 MEDIUM and 9 LOW: one item per raw id, naming its finding and, in brackets, its
review item (M1 to M41, L1 to L9). At order 22, after every unit, each item amends its named unit's
code. Findings 2 and 11 are the medium twins of H6 and H7 (§3); findings 12, 32, 41, 50 and 73 carry
the skeptic's binding re-grade. Criterion ACn observes item Sn.

## 2. Scope (IN)

- **S1** — finding 2 (M1). Over unit 27's per-ref append rule, two deletions of one ref around a re-create
  leave two deletion lines in `gov-feed.log`. Observed by AC1.
- **S2** — finding 11 (M2). Over unit 28's `read_feed_lease_tip`, an offer over a pruned, once sighted unit
  tombstone exits 1 printing `tombstone`. Observed by AC2.
- **S3** — finding 3 (M3). `read_feed_lease_tip` skips deletion events (`commit` 40 zeros) for the ref's
  newest event with a real commit, so a same-node create after `--lease prune` parents on the pruned tip
  at its epoch plus one. Observed by AC3.
- **S4** — finding 61 (M4), the skeptic's fix. When the feed-named commit is unreadable (`git cat-file -e`
  fails), `read_feed_lease_tip` prints `unreadable`: a build or unit lease create refuses `epoch-fence`
  naming the ref, writing nothing; a cadence `run` lease or legacy run claim falls to the plain create
  unit 16's §5 accepts under the queued-claim age. Observed by AC4.
- **S5** — finding 4 (M5). Every governance fetch lands in `refs/gov/remote/` through `observe_remote` with
  `--no-write-fetch-head`, then calls `add_feed_sightings`: the card lookup (S12) and the request draw's
  read of `refs/gov/requests/<key>` (unit 14's S3) take `read_claims`' fetch shape. The success exit is one
  `gov_feed_sh` function, `write_feed_success <ref> <commit or empty>`, setting or clearing the cache ref,
  then appending; `write_gov_ref` calls it, and `scan_feed_writers` names it, `add_feed_event` and
  `write_gov_ref` as what a pusher must call. Observed by AC5.
- **S6** — finding 35 (M5). The lander's fenced push (unit 15's S5) calls
  `write_feed_success <lease ref> <beat>` in place of `add_feed_event`, so the cache names the landed beat
  and `--feed check` reads no `extra`. Observed by AC6.
- **S7** — finding 5 (M6). Route rule R7 (unit 2's S9) reads `refs/gov/remote/builds/<slug>/card`, the cache
  ref a publish sets, so a session's own terminal follow refuses its next route to that build, no lookup
  between. Observed by AC7.
- **S8** — finding 25 (M6). The card has one local name: no code writes or reads
  `refs/gov/builds/<slug>/card` locally. **Readers:** by name: READER NOT IN TREE, since its only readers,
  unit 2's S6 fetch refspec and S9's R7, are this build's and both move here. by value:
  NO VALUE READERS, since nothing else counts or compares the local ref. Observed by AC8.
- **S9** — finding 65 (M6). The lookup's fetch names the remote `resolve_claim_remote` resolves, never a
  literal `origin`. Observed by AC9.
- **S10** — finding 33 (M7). The kickoff engine sets no `GOVREF_RUNNER`, `GOVREF_REMOTE` or `GOVREF_GITDIR`
  and calls no `write_gov_ref`: after unit 33 its one remote write is the driver's `--card-ref write`, its
  lookup `--card-ref lookup` (S12). Observed by AC10.
- **S11** — finding 66 (M7). The lookup is bounded as the publish is: the engine runs `--card-ref lookup`
  into a file under `timeout -k 2 "$CARD_FETCH_BOUND"`, stdin from `/dev/null`, and a silent driver
  reads the next store, printing the `evidence` verdict. Observed by AC11.
- **S12** — finding 32 (M8). `unattended.sh --card-ref lookup <slug>` is read-only: it fetches
  `+refs/gov/builds/<slug>/card:refs/gov/remote/builds/<slug>/card` in S5's shape from S9's remote and
  prints the commit id and message; `RUN_CLAIMS` off prints `card-ref — off`, reading nothing.
  `print_replay`'s lookup calls it, so a replay writes no `FETCH_HEAD`, as TOOL-aGraftedHelix-2 decided.
  Observed by AC12.
- **S13** — finding 34 (M9). The kickoff engine carries no inline parity block, so the `python resolver`
  leg's guard needs no `skills/` path: no `gov_ref_sh` or `gov_feed_sh` marker under `skills/`.
  Observed by AC13.
- **S14** — finding 7 (M10). `--entry-claim` never queues its create, nor writes a build folder: an
  unanswered read answers as §4's table says. Unit 3 §4's `awaiting` row names this `offline`, and unit
  21 S5's `offline` row routes there. Observed by AC14.
- **S15** — finding 71 (M10). With no queued claim, no flush lands a claim no folder follows and no yield
  loses one the session believes held; the next `--entry-claim` reads the slug claimed or taken.
  Observed by AC15.
- **S16** — finding 8 (M11). `scan_feed_writers` reads each `name() {` to its column-0 `}` as a scope, and a
  file's top-level body outside them as one more, paired alike. Observed by AC16.
- **S17** — finding 70 (M12). The census joins `\`-continued lines before matching, and flags a scope
  holding a `push` and a `--force-with-lease`, or a variable assigned it, that calls none of the three S5
  names. Observed by AC17.
- **S18** — finding 9 (M13). Unit 4's AC8 reads "the block's claim lines and no history":
  `placement.py --fixture --plant claim-lines` asserts `record` prints the block's `disposition`, `build`,
  `playbook`, `reason`, `scenarios` and `facts`, and no earlier block's line, `check:` or `placer:`.
  Observed by AC18.
- **S19** — finding 10 (M14). Unit 20 AC6's history check reads what the fence guarantees: epochs never fall
  on the first-parent chain, no commit under A's session carries epoch n+1, and each increment
  coincides with a holder change, over a fresh fixture whose lease A reads as foreign and stale.
  Observed by AC19.
- **S20** — finding 13 (M15). Unit 3's `item.entry.orient` row carries `map = "base"`, so unit 6 §3's "which
  declares `map` there" is true. Observed by AC20.
- **S21** — finding 14 (M16). Unit 14 AC1's arithmetic: with five refusals, places 2 to 5 print `1/4` to
  `4/4`; the sixth `place` exits 3 printing `pre-claim budget exhausted`, writing no block.
  Observed by AC21.
- **S22** — finding 15 (M17). `unattended.sh --lease status <kind> <name> [<sub>]` is read-only and prints
  one TAB line, `<tail> <fleet tag> <session> <status> <verdict> <epoch>`, or `lease — none · <tail>`;
  `placement.py check` decides "free or this session's" by it, never by `--claims`' five fields.
  Observed by AC22.
- **S23** — finding 16 (M18). With `RUN_CLAIMS` off, every `--lease` act but `fence` prints
  `lease — off · <tail>`, writes nothing and exits 0; `fence` keeps unit 15 S2's
  `fence — none · leases are off`. Unit 21's patch and repeat claim proceeds leaseless on `off`.
  Observed by AC23.
- **S24** — finding 37 (M19). The pre-push claim fast path (`.githooks/pre-push:851-870`) accepts a
  `tree 0` candidate whose first parent reads `missing` or has a `tree 0` tree, adding `<sha>^^{tree}` to
  the one `cat-file --batch-check` query. Observed by AC24.
- **S25** — finding 23 (M19), the skeptic's fix. A parented claim beat pushed alone does not source
  `straggler-guard.sh`, staged against the base predicate (`:866`), which accepts only `<sha>^ missing`; the
  hook's comment at `:845-847` names both shapes. Observed by AC25.
- **S26** — finding 24 (M20). `memory/map/features/unattended-stops.md` describes the parented claim chain
  and the default-branch-only verdict clear in place of `claim-push.lock`, its `.break` guard and the marker
  wait (`:58-66`), and the claim block's header comment in `unattended.sh` stops saying the hook clears
  both verdict files on every push. **Readers:** by name: `claim-push.lock`, spelled there at
  `:61-65` and by `memory/gotchas/decision-re-derived-by-a-second-process.md:66` and `:74`, both
  rewritten here. by value: NO VALUE READERS, since no code reads the lock's path after unit 11's S6.
  Observed by AC26.
- **S27** — finding 49 (M20). The gotcha S26 rewrites gains a dated paragraph naming unit 11's removal of
  the lock and what now serialises the two pushes. Observed by AC27.
- **S28** — finding 26 (M21), the skeptic's fix. `readCard` in `tools/hooks/scratch-guard.js` resolves bash
  as `tools/roles/handoff.py`'s `resolve_bash` does (`:225`), never a bare `bash`, folds the checker's
  `/c/…` output through `buildNativePath` (`:819`), and reads a silent checker as no card, named; §4
  states its per-call cost. Observed by AC28.
- **S29** — finding 27 (M22). Unit 1's fixture is hermetic: `render_playbook.py --fleet-tag` takes
  `--fleet <path>`, the fixture plants its own `fleet.toml` and `COMPUTERNAME`, and an empty-`host` row
  resolves by its user. Observed by AC29.
- **S30** — finding 38 (M22). `resolve_fleet_tag` asks `read_fleet` by user alone, case-folded, honouring
  `GOV_NODE` validated against `fleet.toml`'s tags as `resolve_node_tag` does; `--host` is dropped.
  `derive_node_tag` and `resolve_node_tag` (§4) stay: they read the governance file's `## Node registry`
  table, a different registry. **Readers:** by name: READER NOT IN TREE, since `--fleet-tag`'s `--host`
  and its one caller are unit 1 S11's, this build's own.
  by value: NO VALUE READERS, since the host only selected a row. Observed by AC30.
- **S31** — finding 28 (M23), the skeptic's fix. The two new legs, `loop placement fixtures` (unit 4) and
  `loop claim fixtures` (unit 21), each state a subject, a chunk and a ceiling in `tools/gate-legs.json`,
  and a `selftest-budgets.txt` row when held; no `ceiling-evidence.txt` row, as that file is generated
  and an unbacked leg is no failure. Observed by AC31.
- **S32** — finding 47 (M23). Per leg, `tools/govkit/subject-pins.tsv` gains its row by
  `python tools/govkit/govkit.py selfcheck --write`, `memory/map/features/loop.md` claims the leg's key, and
  S38's regeneration carries both. Observed by AC32.
- **S33** — finding 36 (M24). Over unit 24's guarded factory `write_node_lock`, which takes
  `gov-feed.lock`, two breakers racing one planted stale feed lock append unique `seq` values, retiring
  unit 13 §5's accepted "two events one `seq`". Observed by AC33.
- **S34** — finding 39 (M25). `loop_lib.load_tree_lib` becomes a loader taking a module name and its `need`
  tuple, keeping its by-name version-skew refusal; `tools/loop/request.py` imports `derive_content_key`
  through it, never `resolve_kit_dir`, and the loop kit loads memory-tree modules only through it.
  Observed by AC34.
- **S35** — finding 44 (M26). Every reader of the moved run-claim ref follows the lease:
  `tools/unattended/resume-tick.test.sh`'s GH1 AC12 and GH11 AC1 arms (`:872-909`) read
  `refs/gov/leases/tRun/build`; `tools/unattended/.unattended.conf.example:159` and `:163`,
  `.unattended.conf:156`, `tools/unattended/PROTOCOL.template.md:521`,
  `tools/unattended/VERBS.template.md:279` with their renders, and
  `memory/map/features/unattended-stops.md:56` name `refs/gov/leases/<slug>/build`. **Readers:** by name:
  `refs/gov/runs/<slug>` as the claim's home, spelled by each file listed. by value: NO VALUE READERS beyond
  `read_claims`' legacy read, which unit 1's S4 keeps. Observed by AC35.
- **S36** — finding 45 (M27). `skills/session-kickoff/SKILL.md` stays within its 18432-byte limit
  (`tools/template-size-limits.txt:60`): unit 2 S7's resume acts, unit 3's stand-in paragraph and unit 9's
  ratchet sentence live in `skills/session-kickoff/RESUME.md`, which SKILL.md points at in one line.
  Observed by AC36.
- **S37** — finding 46 (M28). `memory/guides/UNATTENDED-PROTOCOL.md` stays within its 66860-byte limit
  (`tools/template-size-limits.txt:143`): the verbs guide names unit 5's third source of the spec-audit
  opt-in, and the protocol's sentence points there at no byte cost. Observed by AC37.
- **S38** — finding 48 (M29). `python tools/codebase-map/gen_map.py --write` regenerates
  `memory/map/generated/` once over the build's final tree, so `symbols.json` names every function the build
  minted and none it deleted, such as the four claim-push lock functions. **Readers:** by name:
  `write_claim_push_lock` and its three siblings, spelled by `symbols.json`, regenerated here. by value:
  NO VALUE READERS, since nothing counts a generated index. Observed by AC38.
- **S39** — finding 50 (M30). `derive_claims_line`'s ranking (§4) gains `released`, hidden past
  `CARD_CLAIMS_HIDE_S` as `stale` and `terminal` are. Observed by AC39.
- **S40** — finding 57 (M31). The offline queue writes `-` for an empty cached tip, as `CLAIM_ROWS` does for
  an unknown field (`tools/unattended/unattended.sh:2112-2113`), and the flush maps `-` back to the empty
  expected sha. Observed by AC40.
- **S41** — finding 58 (M32).
  `--request-draw <content key> --cause <c> --item <tag> [--request-text <file>]` passes the file to unit
  19's `--request <file>` when the ref is absent; with neither, it refuses naming `--request`.
  Observed by AC41.
- **S42** — finding 59 (M33). A draw site reading exit 2 stops: `place` prints
  `placement: pre-claim draw not recorded — <why>`, writing no block, and `entry.claim` exits 2 on the
  same line. Observed by AC42.
- **S43** — finding 60 (M34). The age pass's walk is bounded (§4): one streaming `git log --first-parent`
  over the cached lease refs, no `--topo-order`, piped to the `awk`, which resolves a tail at its renewing
  beat, its tenure's start (unit 26) or the first commit the feed sighted over `leases.expiry-hours` ago,
  which reads `stale`, and exits once every tail resolves, so `git log` stops on the closed pipe.
  Observed by AC43.
- **S44** — finding 62 (M35). Unit 12's S6 refuses a subject, item or fork holding a byte below 0x20 or
  0x7f before building a commit, exit 2 naming the field. Observed by AC44.
- **S45** — finding 63 (M36). A failed cache-ref update in `write_feed_success` prints one `feed: NOTE -`
  line, still appends and keeps rc 0; unit 12 S1's encoded segment is refused over 200 bytes.
  Observed by AC45.
- **S46** — finding 67 (M37), the skeptic's fix. The `restart-item` act, in S36's `RESUME.md`, reads in
  order: `git add -A`; commit to `partial/<slug>/<sid8>`, taking `-2`, `-3` and on when the name exists;
  verify by `git rev-parse` that the branch names the new commit; restore the tree only after that, else
  refuse naming the cause. Observed by AC46.
- **S47** — finding 68 (M38). An entry-time probe's pin: `probe.pin` writes the head to `<key>.probe.md`,
  recording its blob in the trigger record before `run`, which refuses a moved head blob; a trigger after
  a returned probe opens `<key>.probe-2.md`, numbered, never overwriting. Observed by AC47.
- **S48** — finding 69 (M39). `write-set` reads a unit's spec whatever its status, through
  `--path-tokens --files-touched --any-status`, printing `unarmed — write-set: <spec> lists no path` on an
  empty list; the token rule stays as unit 8's AC7 freezes it, a backslash path no token.
  Observed by AC48.
- **S49** — finding 72 (M40). `--lease offer` refuses `offered` over a record whose offer is still open, to
  anyone, and refuses a `--to` naming the caller's own tag. Observed by AC49.
- **S50** — finding 73 (M41). A manifest bullet is its `- ` line plus each following line indented two or
  more spaces, up to the next bullet or blank line, joined by single spaces. Observed by AC50.
- **S51** — finding 12 (L1). Each of the thirteen items of unit 8 §4's table is seeded. Observed by AC51.
- **S52** — finding 17 (L2). `check_probe_outcomes` exempts `item.probe.*` rows, so unit 7's own rows pass
  `--check` and no designer probes a probe. Observed by AC52.
- **S53** — finding 18 (L3). Every inline copy of `gov_ref_sh` and `gov_feed_sh` left, the lander's
  included, cuts equal to its canonical block, and §7 names the `python resolver` leg.
  Observed by AC53.
- **S54** — finding 19 (L4). The offer refuses a build or unit lease tombstone with `tombstone`, `terminal`
  kept for cadence and legacy terminal claims. Observed by AC54.
- **S55** — finding 29 (L5). Unit 18 AC4's parity probe prints `unarmed — tag_index.py does not resolve` and
  exits 2 when `tools/playbook/tag_index.py` is absent, which PLAY-dOrderedCharter-19, DEFERRED, mints.
  Observed by AC55.
- **S56** — finding 30 (L6). The two size figures restated from measured commits (§4).
  Observed by AC56.
- **S57** — finding 31 (L7). §4 records the one `refs/gov` deletion in product code outside the lease
  namespace, in place of unit 16 §10's sentence. Observed by AC57.
- **S58** — finding 40 (L8). `tools/loop/request.py` is new in this build, in dDeclaredLoop's loop kit,
  and this spec's §3 carries the edge unit 19 omits. Observed by AC58.
- **S59** — finding 41 (L9), the skeptic's fix. No commit of this build moves `KIT_UNATTENDED_VERSION` or
  `KIT_RUN_GATES_VERSION` by hand; the lander mints them (TOOL-aMendedFleet-65). Observed by AC59.

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
- **consumes-from** `TOOL-dPlacedRequest-11` — the parented claim commit and the lock's retirement
- **consumes-from** `TOOL-dPlacedRequest-12` — the register record and its encoder
- **consumes-from** `TOOL-dPlacedRequest-13` — the feed's success exit, sightings and census
- **consumes-from** `TOOL-dPlacedRequest-14` — the draw verb and its sites
- **consumes-from** `TOOL-dPlacedRequest-15` — the lander's fenced beat and inline block
- **consumes-from** `TOOL-dPlacedRequest-16` — `released` and the prune
- **consumes-from** `TOOL-dPlacedRequest-17` — the age pass
- **consumes-from** `TOOL-dPlacedRequest-18` — its parity probe
- **consumes-from** `TOOL-dPlacedRequest-19` — `request.py` and `--request`
- **consumes-from** `TOOL-dPlacedRequest-20` — the offer act and its history check
- **consumes-from** `TOOL-dPlacedRequest-21` — `--entry-claim` and its new leg
- **consumes-from** `TOOL-dPlacedRequest-24` — the guarded node lock factory and the queue line
- **consumes-from** `TOOL-dPlacedRequest-26` — the tenure-bounded walk
- **consumes-from** `TOOL-dPlacedRequest-27` — the per-ref append rule
- **consumes-from** `TOOL-dPlacedRequest-28` — `read_feed_lease_tip`
- **consumes-from** `TOOL-dPlacedRequest-33` — the `--card-ref` verb
- **consumes-from** external — dDeclaredLoop's loop kit `tools/loop/`, built before this run, with its `kit.toml`, `selftest.py` and `loop_lib.load_tree_lib` (TOOL-dDeclaredLoop-19, -20, -92), which S34 and S58 extend
- **consumes-from** `TOOL-dPlacedRequest-40` — the exempt act list, which `--lease status` joins by name when S22 mints it
- **hands-off** `TOOL-dPlacedRequest-35` — S43's bounded walk, whose stops that unit orders with the tenure first
- **hands-off** `TOOL-dPlacedRequest-43` — this spec's size, S30's reason, S35's protocol bytes, S40's tip readers and AC35, AC38 and AC59, which that unit's items for findings 7, 10, 11, 20, 23, 25, 27, 28 and 30 cut, correct and re-observe
- **hands-off** `TOOL-dPlacedRequest-49` — AC59, which that unit's item for finding 5 points at unit 44's oracle
- **hands-off** `TOOL-dPlacedRequest-52` — AC59's observation, which that unit's item for finding 11 restates as the oracle's header line, exit 0 and no `KIT_` line
- **hands-off** `TOOL-dPlacedRequest-54` — AC59, which that unit cuts to one line pointing at 44 AC1 on the prepared merge
- **hands-off** `TOOL-dPlacedRequest-57` — AC59, from which that unit drops the base
- **hands-off** `TOOL-dPlacedRequest-59` — this spec's size, which that unit cuts in prose if over 48128

## 4. Design

### Evidence

- Minted code is cited by unit and item, base code by path and line, each read here.
- `derive_claims_line` ranks `live held unknown stale terminal` (`skills/session-kickoff/manifest-check.sh:662`),
  any other verdict falling to `skipped:`.
- `read_files_touched`'s `awk` sets `term` on CLOSED or WONTDO (`tools/unattended/unattended.sh:3398`),
  reads only `ft && !term` (`:3400`), tests tokens at `:3404`.
- `resolve_node_tag` honours `GOV_NODE` against the registry tags and lower-cases the user
  (`tools/run-gates/run-selftests.sh:293-310`); `derive_node_tag` matches `USERNAME` against the
  `## Node registry` Machine/user cell (`skills/session-kickoff/manifest-check.sh:375-400`); `read_fleet`
  is `tools/playbook/render_playbook.py:347`, `check_user_clash` `:381`; `fleet.toml` spells one host
  `COMPEETO-AGENT` (`:23`) and leaves one empty (`:44`).
- `readCard` is `tools/hooks/scratch-guard.js:667`, called at `:774`; `resolve_bash`'s MSYS fold is
  `tools/roles/handoff.py:279`.
- `symbols.json` indexes the four lock functions (`memory/map/generated/symbols.json:3826`, `:3831`,
  `:15301`, `:24166`).
- Sizes, measured 2026-10-25 (PINNED): S36's `SKILL.md` 18310 of 18432 bytes, S37's protocol 66859 of
  66860.
- `derive_content_key` is `tools/memory-tree/row_grammar.py:1475`; `git ls-files tools/loop` prints
  nothing at the pinned base `c63aabbb`.

### The claim offline (S14, S15)

| `leases.offline` | `--entry-claim`, remote unanswered | exit | unit 3 outcome |
|---|---|---|---|
| `warn`, `follow-leases` | `claim not written — offline` | 4 | `awaiting` |
| `refuse` | `lease refused — offline` | 1 | `refused` |

### The bounded walk (S43)

`git log --first-parent --format='%x01%H%n%B' <cached lease and legacy refs> | awk`, the `awk` loading
each commit's feed `seen-utc` against a threshold of now less `leases.expiry-hours`, an ISO string. In
one first-parent chain `git log` emits a child before its parent whatever the dates, as a parent enters
the walk only after its child; across chains, date order costs interleaving only. A commit sighted
before the threshold makes the verdict `stale` whatever lies further back, since on one node a parent
is sighted no later than its child. The walk reads at most
each lease's commits sighted within `leases.expiry-hours`, plus that interleaving.

### Measured sizes (S56)

Measured 2026-10-25 (PINNED) by `git cat-file -s` over five `refs/gov/remote/runs` tips: a
parentless claim commit is 380 to 390 bytes, so a parented one, a 48-byte `parent` line more, is about
430, not "sub-400" (unit 11's §4); a lease commit, nine keys more, is about 630, so one written each
minute for a day is about 0.9 MB of loose objects, not "under 0.6 MB" (unit 17's §4). Nothing in
either unit branches on the figure.

### The one deletion outside leases (S57)

Correcting unit 16's §10, which finds no `refs/gov` deletion outside fixtures: post-merge's
`remove_red_ref` (`tools/run-gates/post-merge.sh:301`, called at `:392`) deletes `refs/gov/bar-red` on
every green after a red, kept by unit 11 through `write_gov_ref`, outside the lease namespace its S7
guards.

### `readCard`'s cost (S28)

One `bash manifest-check.sh --card --path --session <sid>` per guarded write, about 0.3 s on a
Git-for-Windows node (the review's measurement, PINNED 2026-10-25), under the hook's existing spawn
bound; a node where bash does not resolve reads no card, named.

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

### Alternatives rejected

- **Two batches.** Nearly every item shares `unattended.sh`, the `gov_feed_sh` block or the kickoff
  engine, so no split gives M6 two disjoint write sets.
- **A `renewed-by` key (S43) or a backslash token (S48).** F3 and F4 record why.

## 5. Production-readiness checklist

- security — S44 closes register key-line injection; S10 to S13 leave the engine no writer; S23 states
  the switch-off outcome.
- perf / scale — S24 restores the claim push's fast path; S43 bounds the age pass; S12 takes the
  replay's fetch off `FETCH_HEAD`.
- error / empty / loading states — S4, S42 and S45 each name an outcome left undefined.
- observability — every new outcome is one named line.
- risks — S36 moves kickoff text behind one pointer; S43's early `stale` is the verdict anyway.
- testing — the probes of §6 and the arms of §7.
- migration — none: every item lands before anything it amends ships.
- user docs — the verbs, stops and protocol guides and `RESUME.md`; no `help/` page covers these kits.

## 6. Acceptance criteria

Fixtures are the named unit's own unless an item names one.

- **AC1** — When a probe deletes, re-creates and deletes one ref through `write_gov_ref`, the feed holds two
  deletion lines for it. Red when: the second deletion is dropped.
- **AC2** — When `--lease offer unit tFix TOOL-tFix-2 --to b` runs over a deleted, sighted unit tombstone, it
  exits 1 printing `tombstone`. Red when: the offer re-creates it.
- **AC3** — When `--lease prune` deletes a terminal run lease at epoch 3 and
  `--lease acquire run maintain 2026-10` runs on the same node, the new record reads `epoch: 4` parented on
  the pruned tip. Red when: the create reads the deletion event and restarts at 1.
- **AC4** — When `git prune --expire=now` makes the feed-named commit unreadable after its cache ref is
  gone, a unit lease acquire exits 1 printing `epoch-fence`, and a run lease acquire creates at epoch 1.
  Red when: a build or unit lease restarts its epoch.
- **AC5** — When clone A writes a card over clone B's card commit, `bash unattended.sh --feed check` exits
  0. Red when: a commit fetched outside the sighting hook reads `missing`.
- **AC6** — When unit 15's fixture lands a fenced push, `git rev-parse refs/gov/remote/leases/tFix/build`
  names the beat and `--feed check` exits 0. Red when: the
  check prints `extra`.
- **AC7** — When `--card --follow --terminal` runs and a same-node append routing to that build follows, no
  ref planted and no lookup, `manifest-check.sh` refuses it naming R7. Red when: R7 reads a ref
  the publish never moved.
- **AC8** — When `git grep -n 'refs/gov/builds/[^ ]*:refs/gov/builds'` runs over
  `skills/session-kickoff/manifest-check.sh` and `tools/unattended/unattended.sh`, it prints nothing.
  Red when: a second local name for the card remains.
- **AC9** — When `card-store.fixture.sh --plant lookup` runs in a clone whose one remote is named
  `upstream`, the lookup reads the card. Red when: the fetch names a literal `origin`.
- **AC10** — When `grep -n 'GOVREF_\|write_gov_ref' skills/session-kickoff/manifest-check.sh` runs, it
  prints nothing. Red when: the engine holds the writer's caller contract.
- **AC11** — When `card-store.fixture.sh --plant lookup-hung` runs with a silent stub driver, the lookup
  prints `evidence` within the bound plus 3 s. Red when: the lookup hangs.
- **AC12** — When `card-store.fixture.sh --plant replay` runs, `FETCH_HEAD`'s mtime is unchanged. Red when:
  a replay writes `FETCH_HEAD`.
- **AC13** — When `git grep -n '# >>> gov_ref_sh\|# >>> gov_feed_sh' -- skills/` runs, it prints nothing.
  Red when: an unguarded copy ships in the engine.
- **AC14** — When the origin is renamed away and `--entry-claim` runs under the default `leases.offline`, it
  exits 4 printing `claim not written — offline`, `gov-queue.log` gains nothing and no README is written;
  under planted `refuse` it exits 1 printing `offline`. Red when: a claim queues or a folder is written.
- **AC15** — When the origin returns after another node claims the slug and `--entry-claim` reruns, it
  prints the slug-taken line. Red when: a claim lands with no folder, or is lost silently.
- **AC16** — When `scan_feed_writers` reads a scratch file whose top-level body pushes with
  `--force-with-lease`, never appending, it prints that line; over `tools/push-main.sh`, nothing.
  Red when: a top-level writer escapes, or the correct one is flagged.
- **AC17** — When it reads plants holding a `\`-wrapped push and a `git push "${args[@]}"` whose array holds
  `--force-with-lease`, each with no append, it prints both. Red when: either escapes.
- **AC18** — When `python placement.py --fixture --plant claim-lines` runs after unit 10's lines land, it
  passes, printing the block's six claim lines, no history. Red when: unit 10's lines red it.
- **AC19** — When `TOOL-dPlacedRequest-20`'s fixture runs the corrected history check over a chain
  holding renews and an offer, it passes; with a planted take at a fallen epoch it fails.
  Red when: a correct chain fails or a fallen epoch passes.
- **AC20** — When `python loop_lib.py --check` runs, it lists `item.entry.orient` with `map base`. Red when:
  the item defaults to `map none`.
- **AC21** — When unit 14's fixture plants five refusals, places 2 to 5 print `1/4` to `4/4`, the sixth
  exiting 3 printing `pre-claim budget exhausted`. Red when: a count is off by one.
- **AC22** — When two same-node sessions hold and read one build lease, `--lease status build tFix` prints
  the holder's session, and `placement.py check` refuses `amend` for the other. Red when: a same-node
  session reads another's lease as its own.
- **AC23** — With `RUN_CLAIMS` off, `--lease acquire build tFix` prints `lease — off · tFix/build` and
  exits 0, the origin unchanged, and `--lease fence build tFix` prints `fence — none`. Red when: an off
  switch writes, hangs or refuses.
- **AC24** — When `.githooks/pre-push` reads, in a scratch clone, one stdin line pushing a parented claim
  beat alone, beside a stub `straggler-guard.sh` printing a marker, no marker prints. Red when: the
  parented shape takes the slow path.
- **AC25** — When the same line is fed to a scratch copy of the hook staged back to the base
  `<sha>^ missing` test, the stub prints its marker. Red when: the two predicates read alike.
- **AC26** — When `git grep -n 'claim-push.lock' -- memory/map/features/ memory/gotchas/` runs, its only
  hits are in the gotcha's dated paragraph naming unit 11. Red when: a reader still calls the lock live.
- **AC27** — When `grep -n 'TOOL-dPlacedRequest-11' memory/gotchas/decision-re-derived-by-a-second-process.md`
  runs, a dated paragraph names the lock's removal. Red when: the gotcha's history stops at the lock.
- **AC28** — When a `node -e` probe calls the exported `readCard` with a stub checker printing a `/c/` path,
  it reads the card at the `C:/` path. Red when: the MSYS path reads as no card.
- **AC29** — When unit 1's fixture plants its own `fleet.toml` with an empty-host row and a `COMPUTERNAME`,
  `--lease acquire build tFix` writes `fleet-tag` from that row. Red when: the result rests on the machine.
- **AC30** — When `USERNAME` matches a row in another case and `GOV_NODE` is unset, the tag resolves; with
  `GOV_NODE` naming an unregistered tag, the verb exits 2. Red when: case or host refuses a node.
- **AC31** — When `python -c` reads `tools/gate-legs.json`, both legs carry a subject, a chunk and a
  ceiling. Red when: a leg lacks one.
- **AC32** — When `python tools/govkit/govkit.py selfcheck` and `python tools/codebase-map/gen_map.py --check`
  run, both exit 0 with the two legs present. Red when: a pin
  row or dossier claim is missing.
- **AC33** — When two background appenders break one planted stale `gov-feed.lock`,
  `cut -f1 gov-feed.log | sort | uniq -d` prints nothing. Red when: two events share a `seq`.
- **AC34** — When `git grep -n resolve_kit_dir -- tools/loop/` runs, it prints only `loop_lib.py`'s loader;
  with a skewed memory-tree kit planted, `request.py key` prints the named refusal. Red when: a raw
  ImportError escapes.
- **AC35** — When `git grep -n 'refs/gov/runs/<slug>\|refs/gov/runs/tRun'` runs over the files S35 lists, it
  prints only legacy-read mentions. Red when: a reader still names the old home.
- **AC36** — When `wc -c skills/session-kickoff/SKILL.md` runs, it prints at most 18432, and
  `grep -n RESUME.md skills/session-kickoff/SKILL.md` finds the pointer. Red when: the size leg reds.
- **AC37** — When `wc -c memory/guides/UNATTENDED-PROTOCOL.md` runs, it prints at most 66860. Red when: the
  protocol size leg reds.
- **AC38** — When `python tools/codebase-map/gen_map.py --check` runs, it exits 0 and
  `grep -c claim_push_lock memory/map/generated/symbols.json` prints 0. Red when: the map is stale.
- **AC39** — When `manifest-check.sh --card --write` runs over a fixture holding a `released` lease, it
  prints a `claims —` count line, not `skipped:`. Red when: `released` hides the cell.
- **AC40** — When unit 1's AC7 queues an offline create and the origin returns, `--lease flush` lands it.
  Red when: the empty field shifts the line, so the create never lands.
- **AC41** — When `--request-draw <key> --cause refused --item item.entry.place --request-text req.md` runs
  with no ref, the ref is created, the draw recorded; with neither, it exits 2 naming `--request`.
  Red when: the branch has no file to pass.
- **AC42** — When unit 14's fixture plants `--plant unreachable`, `place` prints
  `pre-claim draw not recorded` and writes no block. Red when: placement proceeds unbounded.
- **AC43** — When `--claims` reads a planted 10,000-commit lease chain whose last 50 commits were
  sighted within the bound, it runs at least five times faster than a scratch copy walking every commit.
  Red when: the walk reads the whole chain.
  figure: DERIVED at observation, as a ratio of the two timings.
- **AC44** — When `--register problem` runs with a subject holding `\nsession: x`, it exits 2 naming
  `subject` and builds no commit. Red when: a key line is injected.
- **AC45** — When a probe holds `<git-common-dir>/refs/gov/remote/runs/tFix.lock` and writes the ref,
  `write_gov_ref` returns 0, printing one `feed: NOTE -` line, and the event is appended; a 201-byte encoded
  subject is refused. Red when: a landed write returns non-zero.
- **AC46** — When `grep -n` runs over `RESUME.md` for `git add -A`, the numbered suffix, `git rev-parse` and
  "restore only after", each is found in that order. Red when: the restore precedes its verified commit.
- **AC47** — When unit 7's fixture edits an entry-time probe's head between `pin` and `run`, `run` exits
  non-zero naming the moved head; a second trigger after a returned probe writes `<key>.probe-2.md`,
  `<key>.probe.md` unchanged. Red when: the pin is unchecked or a verdict is overwritten.
- **AC48** — When `python loop_lib.py seed item.build.unit-pass --unit <closed unit>` runs over a CLOSED
  fixture spec, it prints its paths; over one listing none, `unarmed — write-set`. Red when: a closed
  unit's write set reads empty.
- **AC49** — When clone A runs `--lease offer` over B's open offer to itself, it exits 1 printing `offered`;
  `--to` its own tag also exits 1. Red when: a node re-offers to itself.
- **AC50** — When the manifest step's `up` runs over a §B holding one wrapped bullet, the unit row's `text`
  carries the whole bullet. Red when: the text is truncated.
- **AC51** — When `python loop_lib.py seed` runs for each of unit 8 §4's thirteen item tags, each prints a
  seed or an `unarmed —` line. Red when: an item is unseeded.
- **AC52** — When `python loop_lib.py --check` runs over unit 7's rows, it exits 0; over a planted role row
  outside `item.probe.*` lacking `probe`, 1. Red when: the rule refuses its own rows.
- **AC53** — When `awk` cuts every `gov_ref_sh` and `gov_feed_sh` block in the tree, `cmp` finds each
  equal to its canonical cut. Red when: a copy drifts unobserved.
- **AC54** — When `--lease offer` runs over a build tombstone, it exits 1 printing `tombstone`. Red when:
  the cause reads `terminal`.
- **AC55** — When unit 18's parity probe runs with `tag_index.py` absent, it exits 2 printing `unarmed`.
  Red when: it reads as green.
- **AC56** — When `git cat-file -s` reads a lease commit in unit 1's fixture, it is within 15% of §4's
  630 bytes. Red when: §4's figure is off by more. figure: DERIVED at observation.
- **AC57** — When `git grep -n remove_red_ref -- tools/run-gates/post-merge.sh` runs, it prints the
  definition and its one call. Red when: §4's record of the deletion is false.
- **AC58** — When `git ls-files -- tools/loop` runs at the close it lists `request.py`, and `git cat-file -e`
  of that path at `c63aabbb` fails. Red when: the file pre-dates this build.
- **AC59** — When `git diff c63aabbb..HEAD -- tools/unattended/unattended.sh tools/run-gates/run-gates.sh`
  is grepped for `^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION=` before the lander's mint, it prints nothing.
  Red when: a branch commit hand-bumps a version.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `branch-guard self-test` · `pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `push-main self-test` · `transition-audit arms` · `straggler-guard arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `playbook render selftest` · `kickoff engine size <=18KiB` · `unattended protocol size` · `codebase-map coverage + freshness` · `codebase-map gate coverage` · `harness arms (fail branches armed or pinned)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC14 AC15 AC22 AC23 AC33 AC40 AC43 AC45 AC49 AC54 · each item's plant, staged against the unit it amends · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/push-main.test.sh · covers AC6 · the fenced landing's cache ref, staged against `add_feed_event` alone · the suite's assertion count raised by the arm added
New arm: .githooks/pre-push.test.sh · covers AC24 AC25 · a parented claim beat pushed alone, staged against the base `<sha>^ missing` predicate · the suite's assertion count raised by the arm added
New arm: tools/hooks/scratch-guard.test.sh · covers AC28 · a stub checker printing a `/c/` path, staged against a bare `bash` and no fold · none
New arm: skills/session-kickoff/card-store.fixture.sh · covers AC7 AC9 AC11 AC12 AC39 · the terminal-route, hung-lookup, replay and released plants, staged against `TOOL-dPlacedRequest-2`'s local ref and fetch · none

## 8. Open questions

- **F1 — Where does the kickoff text that overflows SKILL.md go (S36)?** (a)
  `skills/session-kickoff/RESUME.md`, pointed at in one line; (b) an equal trim elsewhere in SKILL.md;
  (c) raise the limit. (c) is an owner's ceiling; (b) cuts text other units wrote.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How is the claim's offline outcome stated once (S14)?** (a) The claim never queues, `offline`
  routing to `awaiting` under every value but `refuse`; (b) a queued claim is `awaiting` and a flush
  lands it. (b) needs a yield to reach an ended session. RESOLVED (agent, 2026-10-25, delegated): (a),
  rung 3. widens: none · relaxes: none
- **F3 — How is the age pass bounded (S43)?** (a) A streaming walk stopping at the first commit
  sighted before the expiry window; (b) per-ref windows of `git log -n`; (c) a `renewed-by` record key.
  (b) spends a process per ref per read; (c) widens I6. RESOLVED (agent, 2026-10-25, delegated): (a),
  rung 3. widens: none · relaxes: none
- **F4 — Does `read_path_tokens` admit a backslash (S48)?** (a) No: the backslash case leaves
  unit 8's AC4 and AC7 is kept; (b) yes, amending AC7, a reader every caller of `read_files_touched`
  shares. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3.
  widens: none · relaxes: none

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

## 10. Reuse audit

Each item extends its named unit's seam and the base code §2 and §4 cite, with the claim fetch
(`tools/unattended/unattended.sh:2136`) and the claims cell (`skills/session-kickoff/manifest-check.sh:645-700`).
`python tools/codebase-map/reuse_lookup.py` over "append an event only when the ref's newest event
differs" and "publish the build card ref through the driver behind the claims switch" ranked name
stems only (`add_health_event`, `claims`, `build_commit`): no seam fits beyond the units named.
`python tools/memory-recall/query.py` over "how is the build card published to the remote" and "how
does the feed avoid appending a retried write twice" returned units 2 and 13, the brief and the
audit's items; none disagrees with source.

Recall terms used: feed sightings cache census card lookup FETCH_HEAD parity size limit offline claim walk bound
