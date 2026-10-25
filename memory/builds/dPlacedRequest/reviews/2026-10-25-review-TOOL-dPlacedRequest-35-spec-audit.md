**Serves:** spec-audit TOOL-dPlacedRequest-36@rev-1 TOOL-dPlacedRequest-37@rev-1 TOOL-dPlacedRequest-38@rev-1 TOOL-dPlacedRequest-39@rev-1 TOOL-dPlacedRequest-41@rev-1 TOOL-dPlacedRequest-42@rev-1 TOOL-dPlacedRequest-40@rev-1 TOOL-dPlacedRequest-35@rev-1 TOOL-dPlacedRequest-43@rev-2

# Tier-2 spec audit — build dPlacedRequest, the round-2 promotion specs TOOL-dPlacedRequest-35 to -43, ROUND 1

*This is an adversarial pre-code pass over the nine specs that the round-2 spec audit promoted, dated 2026-10-25. Five lenses found defects, and five skeptic batches tried to refute each finding. This report is synthesised only from the findings that survived. Finders were gov-spec-reviewer, skeptic batches gov-skeptic, and synthesis gov-synthesizer.*

Reviewed: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-36.md@52dbcacbcedd2f20ab7e7511fe3dc45751d78873, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-37.md@d106215ded7db48eecd02deecb944c6e3fa36c5a, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-38.md@36152e20d9c80ef78dce3897972dcfb00950aef9, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md@7190d816c50f5776e87a9aaed9103092b287f7fb, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-41.md@1085407db938db1dd70cb438ce2b10821227c0da, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-42.md@30a91da6a7e10b1ae13b2df3f16635211ee95600, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-40.md@c13e304711b7fc69303d2c019ade3d631cb3b098, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-35.md@9c3b7aa09984cce5625960d3620b61f404e67afa, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md@ec1f0916f9857a0eeeb05a4a3553e8c335ec862a

ROUND 1

## Verdict: BLOCKED

One blocker stands: AC24's version-bump oracle reads no commit of the build on the prepared merge, so it certifies a check it does not perform (B1).
By item, the tally is 35 items: 1 blocker, 4 high, 18 medium and 12 low.
By raw confirmed finding, it is 39: 1 blocker, 4 high, 22 medium and 12 low.
Several items name a defect next to a sibling item at a different binding grade. Each says so, and no finding is counted twice.

## Review shape

The review ran at intensity full: raw 39, confirmed 39, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |

**Run integrity.**
- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions and discards: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified. 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 36 were judged sound and 3 were judged UNSOUND (ids 14, 22 and 38). 0 had no fix proposed, and 0 were NOT JUDGED.
- Severity on confirmed findings: 0 were UNGRADED and 5 were RE-GRADED by the skeptic (ids 6, 7, 20, 26 and 34).
- Unverified findings: 0 were answered UNCERTAIN, and 0 had no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

Because every count above is zero where it should be, this run is complete.

- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and synthesis gov-synthesizer.
- Intent: 34 spec documents were supplied as `specs`, as sibling context.
- Checklist: 49 items, each assigned to exactly one of 5 lenses: coherence 10, grounding 10, reuse 10, blast-radius 10, failure-envelope 9.
- By design: 2 invariants came from the checklist's by-design block.
- Move check: no checked subject moved.

Every fix below was judged by a skeptic. Where a skeptic rejected the finder's fix, the skeptic's corrected fix is the one written here.

## Blocker

### B1 — AC24's first-parent walk on the prepared merge reads none of the build's commits (id 26)

- **Where:** `TOOL-dPlacedRequest-43` §2 S24 and §6 AC24.
- **What is wrong:** S24 rewrites the version-bump oracle as `git log --first-parent --no-merges ... c63aabbb..HEAD`, and AC24 runs it on the prepared merge. `push-main.sh:921` builds that merge with `-p "$R" -p "$oldb"`, so its first parent is main's tip. A walk from that merge drops the merge itself (`--no-merges`) and then follows main's own line, which holds no non-merge commit since c63aabbb. The build's commits sit only on the second parent.
- **Consequence:** AC24 prints nothing whether or not a branch commit hand-bumps `KIT_UNATTENDED_VERSION` or `KIT_RUN_GATES_VERSION`. It certifies "no hand-bump" without reading a single commit of the build. The defect is new: review 23's suggested fix (M17) had no `--first-parent`.
- **Fix (judged sound):**
  - On the prepared merge, walk the build's side: `git log --no-merges --invert-grep --grep='^mint:' -p HEAD^1..HEAD^2 -- tools/unattended/unattended.sh tools/run-gates/run-gates.sh`.
  - On the branch tip before prepare, use `$(git merge-base origin/main HEAD)..HEAD`.
  - State in AC24 which of the two it reads.
  - Stage the red case in a scratch clone: prepare a branch commit that bumps `KIT_UNATTENDED_VERSION`. The corrected command must print the `+KIT_UNATTENDED_VERSION=` line, and the S24 command as written prints nothing.
- **Severity note:** the finder graded this high. The skeptic regraded it blocker, because a check that certifies what it does not check is a blocker under the rubric.
- **Related:** H1 (id 21) is the reuse lens's report of the same walk, bound at high. M2 (id 5) covers the old AC59 oracle left standing beside it.
- **Gate:** add a bug-class checklist entry: "a history oracle run on a prepared merge must name which parent it walks." Also add a lint over spec ACs that flags `--first-parent` paired with "prepared merge".

## High

### H1 — the same version-bump walk, reported by the reuse lens (id 21)

- **Where:** `TOOL-dPlacedRequest-43` §2 S24 and §6 AC24.
- **What is wrong:** this is the defect B1 describes. The reuse lens reported it on its own, and its binding grade is high, so it stays a separate item and is counted once here. From the prepared merge, `--first-parent` walks main's line and `--no-merges` drops the merge, so no branch commit is shown. AC24 prints nothing whatever the branch did.
- **Consequence:** it certifies a check it does not perform. That is the defect unit 34's AC59 was being corrected for in the first place.
- **Fix (judged sound):**
  - Walk the branch side: `git log --no-merges --invert-grep --grep='^mint:' -p HEAD^1..HEAD^2` on the prepared merge, and `c63aabbb..HEAD` on the unmerged branch.
  - Better still, pin the oracle to the branch ref rather than to HEAD.
  - Add a Red-when the build stages in a scratch clone: prepare a branch commit that hand-bumps `KIT_UNATTENDED_VERSION=`, and the grep must print that line.
- **Gate:** the same entry as B1. One fix closes both items.

### H2 — the lease walk reads a `renews: -` (never-expiring) lease as stale (id 32)

- **Where:** `TOOL-dPlacedRequest-35` §2 S1 and S2, and §4 "The walk, per tail".
- **What is wrong:** the new stop order handles only `renews` values of `yes` and absent. A commit carrying `renews: -` matches neither the epoch-change stop nor the renewing-beat stop, so it reaches the `seen-utc < threshold -> stale` test.
- **Consequence:** under `leases.renewal none`, every commit is `renews: -`. Every held lease then reads `stale` after `leases.expiry-hours`, and another node may take it over. This contradicts three specs:
  - TOOL-dPlacedRequest-17 S3 and AC4, which say a lease sighted 1,000 hours ago is never stale.
  - TOOL-dPlacedRequest-26 S2.
  - TOOL-dPlacedRequest-25's row for `none`.
- **Fix (judged sound):**
  - Add the `-` class to S1 as its own stop, ahead of the threshold test: a commit inside the tenure whose `renews` reads `-` resolves the tail by TOOL-dPlacedRequest-17 S3's never-stale rule.
  - Add the same line to the §4 pseudo-code.
  - Add an AC: a one-tenure chain whose tip is `renews: -`, sighted 1,000 hours ago, prints `live`. It is red when the threshold test runs on a `-` commit.
- **Gate:** make a fixture row that runs the walk over every `renews` value class (`yes`, absent, `-`). Every rewrite of a stop order must enumerate the classes of its input field.

### H3 — an unsighted commit compares as the empty string and reads stale, not unknown (id 33)

- **Where:** `TOOL-dPlacedRequest-35` §2 S1 step (3), the §4 pseudo-code `seen-utc < threshold`, and §5 error and empty states.
- **What is wrong:** the threshold test is a string compare. In awk an unset `seen-utc`, and the `-` placeholder too, sorts before every ISO stamp. §5 covers only an "unsighted tenure start".
- **Consequence:** a feed can be empty or missing, for example after a fresh upgrade before `--feed rebuild`, or after the feed is deleted. A tip can also be one the feed has not yet sighted. In any of these cases every affected lease row reads `stale` and may be taken over. TOOL-dPlacedRequest-17 (17:47, with its AC at 17:196-197) requires `unknown` and never `stale`.
- **Fix (judged sound):**
  - Add a stop ahead of step (3): a commit inside the tenure that the feed has not sighted is never tested against the threshold.
  - A tip or renewing beat with no sighting resolves `unknown`, with age `-`.
  - Write the §4 test as `seen-utc set and seen-utc < threshold`.
  - Add an AC: over an empty feed under a non-empty cache, every row prints `unknown` and none prints `stale`.
- **Gate:** add a bug-class checklist entry: "a string compare against a timestamp must guard unset and placeholder values".

### H4 — AC30's two background calls never place the race, so it passes without the lock (id 16)

- **Where:** `TOOL-dPlacedRequest-43` §6 AC30 (item S30).
- **What is wrong:** AC30 starts two background `--request` calls and expects exactly one `collision`. Nothing places the second call inside the first call's compare-to-copy window. Without a lock, the calls almost always run one after the other, the second call's compare sees the first call's copy, and it is refused `collision` anyway.
- **Consequence:** the AC is green on unlocked code. A missing or wrong `requests.lock` around the compare, the copy and the `.typed` append ships undetected. That is the racing overwrite of stored words that S30 and §5 security claim to close.
- **Fix (judged sound):**
  - Place the race deterministically with a test hook or stub that blocks the first call after its compare and before its copy, for example on a FIFO or a marker file.
  - Start the second call, and assert that it exits 2 with `collision` or waits on the lock. Then release the first call.
  - Stage the red against a scratch copy with the lock removed, and confirm that copy reds.
- **Related:** M17 (id 37) covers the unspecified busy path of the same lock.
- **Gate:** checklist class C22, fixed-sleep-does-not-place-a-signal. A concurrency AC must name the hook that places the interleaving.

## Medium

### M1 — S16 raises the shared `CARD_FETCH_BOUND` to a writer's 140 s, which also bounds the read-only lookup (ids 1, 22)

- **Where:** `TOOL-dPlacedRequest-43` §2 S16, §6 AC16 and §8 F3. These conflict with TOOL-dPlacedRequest-2 S6 and TOOL-dPlacedRequest-34 S11.
- **What is wrong:** three call sites use the same name:
  - Unit 2 S6 bounds its card fetch with it.
  - Unit 34 S11 runs `--card-ref lookup` under `timeout -k 2 "$CARD_FETCH_BOUND"`.
  - Unit 33 runs the publish under it.

  S16 gives that one constant a default of 140 s. F3 never weighed a separate bound for the lookup.
- **Consequence:** a lookup against a hung remote, during kickoff or `print_replay`, now waits far longer before falling back to the next store. The driver's `observe_remote` is killed at REMOTE_BOUND=60, so the wait is about 65 s rather than the full 140, but that is still more than four times the 15 s claims cell. It also runs against TOOL-aGraftedHelix-2's 15 s kill bound for a remote read (DECISIONS.md:218).
  - AC16's Red-when, "the writer runs under a reader's bound", is turned around: now the reader runs under the writer's bound.
  - The constant had no value before this change, so this is a new default, not a regression from an old one.
- **Fix (finding 1's fix judged sound; finding 22's fix judged UNSOUND, so the skeptic's corrected fix is written here):**
  - Mint `CARD_PUBLISH_BOUND=${CARD_PUBLISH_BOUND:-140}` and use it only for the `--card-ref write` call. Update spec 33 S2 and its sketch at 33:100.
  - Keep `CARD_FETCH_BOUND` as the lookup's reader bound, at or under 15 s.
  - Point AC16 at the publish constant.
  - Switch AC17's publish-late stub from `CARD_FETCH_BOUND=2` to `CARD_PUBLISH_BOUND=2`.
  - Add a check that the lookup call site does not read `CARD_PUBLISH_BOUND`, and a criterion that the lookup's bound is still at most the claims cell's.
- **Gate:** add a checklist entry, two-answers-to-one-question: "raising a shared bound names every call site that reads it".

### M2 — S24 adds a corrected oracle but leaves 34's defective AC59 in force (id 5)

- **Where:** `TOOL-dPlacedRequest-43` §2 S24, §6 AC24 and §3, against TOOL-dPlacedRequest-34 AC59.
- **What is wrong:** §3 allows edits to unit 34's criteria only for S11 and S22. AC59, with its `git diff c63aabbb..HEAD` oracle, therefore stays in force next to AC24. AC24 also prints nothing at HEAD today, so it observes nothing the unit changes.
- **Consequence:** at the close on a prepared merge, 34 AC59 reds on version bumps minted on main, which is finding 30's false red, while 43 AC24 reads green. The build carries two contradictory answers to one question.
- **Fix (judged sound):**
  - Make S24 an edit of 34's AC59 command, alongside S11 and S22 in §3's exception list, so that a single oracle remains.
  - Stage AC24's red as the `git diff` form, run over a branch that merged a `mint:` commit from main.
  - Use the corrected walk from B1.
- **Gate:** add a checklist entry: "a spec that corrects another spec's criterion edits it in place and lists it in §3".

### M3 — the feed append's EXIT trap is armed after the lock take (ids 9, 14, 34)

- **Where:** `TOOL-dPlacedRequest-39` §2 S2, §4 "The append" and §6 AC1.
- **What is wrong:** the subshell runs `write_node_lock … || exit 3` first and sets `trap 'remove_node_lock …' EXIT` on the line after. Three things follow.
  - **Finding 9:** AC1 plants its unbound name "directly after the lock take", which is before the trap exists. A build faithful to §4 therefore leaves `gov-feed.lock` held and fails AC1, so the AC and the design disagree.
  - **Findings 14 and 34:** the factory inherits the claim-push body, which runs `mkdir`, then the `until` write, then the `owner` write. An abort inside the factory leaves a lock with no `until` and no `owner`, and no trap is set. That abort is exactly H1's REMOTE_BOUND class. Even an armed trap could not clear such a lock, because `remove_node_lock` removes only when the owner token matches.
  - **Combined:** S2's claim that "an abort leaves no gov-feed.lock" is false in this window. The S3 non-goal ("any such name, present or future") overclaims.
- **Consequence:** with no `until` file, `check_*_lock_stale` falls back to the two-minute mtime test. For about two minutes, every feed append on the node waits 5 s and drops its event with a `lock busy` NOTE. AC1 still certifies that no lock remains.
- **Fix (findings 9 and 34 judged sound; finding 14's fix judged UNSOUND, so the skeptic's corrected fix is written here):**
  - Inside the factory, write `owner` before `until`, so a taken lock always carries its token.
  - Inside the subshell, install the EXIT trap before calling `write_node_lock`, guarded by a flag such as `_fl_mine`. `write_node_lock` sets the flag in the same subshell, right after its own successful `mkdir`.
  - The trap removes the lock dir when the flag is set and the owner file is either absent or reads this token.
  - State the order in S2.
  - Add an AC that plants the unbound name inside `write_node_lock`, between the `mkdir` and the `until` write. It asserts that no `gov-feed.lock` remains, that the next append succeeds, and that the carrier prints `after`.
- **Severity note:** the skeptic regraded id 34 from high to medium, because the damage is about two minutes of dropped appends.
- **Gate:** add a checklist entry: "a cleanup trap is armed before the resource it guards is taken; a lock's owner token is written first".

### M4 — the rule that every `gov_feed_sh` carrier carries `health_log_sh` is checked on one file only (ids 11, 35)

- **Where:** `TOOL-dPlacedRequest-36` §2 S2 and §6 AC3, with TOOL-dPlacedRequest-38 §3 and TOOL-dPlacedRequest-15.
- **What is wrong:** S2 states a class, "every file carrying gov_feed_sh carries health_log_sh, inline", but AC3 greps only `post-merge.sh`.
  - Unit 38 §3 hands carriage to this AC, and unit 38's arm sources the canonical `health-log.sh` rather than the carrier's own copy.
  - Unit 15 consumes the rule for `tools/push-main.sh` with no scope item or AC.
  - "Inline" does not describe `unattended.sh`, which gets the block by sourcing `lib-unattended.sh`.
- **Consequence:** suppose `push-main.sh` gains `gov_feed_sh` without `health_log_sh`. Its stale-lock break calls an undefined `add_health_event`, and the event is lost with a `command not found` on stderr. Every check stays green. A per-file "inline" predicate would also falsely red on `unattended.sh`.
- **Fix (judged sound):**
  - Restate AC3 over the population: for every file that `git grep -l '^# >>> gov_feed_sh' -- '*.sh'` lists, that file, or the one file it sources (name `unattended.sh` → `lib-unattended.sh` explicitly), carries `^# >>> health_log_sh`.
  - The check reds naming the file, and an empty population also reds.
  - Observe the red by planting a scratch carrier that holds `gov_feed_sh` alone.
  - Reword S2 from "inline" to "inline or sourced".
  - Alternatively, have unit 38's arm cut the carrier's own `health_log_sh`, red when it is absent.
- **Gate:** checklist class C6. An AC for a class rule iterates the population and reds when that population is empty.

### M5 — the `env -i` probes drop `$c` and abort before the factory runs (id 15)

- **Where:** `TOOL-dPlacedRequest-37` §6 AC1, `TOOL-dPlacedRequest-36` §6 AC1 and AC2, and `TOOL-dPlacedRequest-38` §4 "The arm".
- **What is wrong:** each probe runs `env -i PATH="$PATH" bash -c 'set -u; ... "$c/gov-feed.lock" ...'`. `env -i` strips `c`, so under `set -u` the inner shell aborts with `c: unbound variable` (rc 127).
- **Consequence:** the green case and the red case fail the same way. The criteria cannot tell a self-contained block from a broken one, and 38's arm reds every copy. A builder who "fixes" this by dropping `set -u` or `env -i` removes the very thing the criteria test.
- **Fix (judged sound):** pass the scratch common dir explicitly, for example `env -i PATH="$PATH" c="$c" bash -c '...'`. Do this in 36 AC1 and AC2, 37 AC1, and 38 §4 and S1. Pass the commit for `add_feed_event` the same way.
- **Related:** L1 (id 39) is the failure-envelope lens's report of the same defect, bound at low.
- **Gate:** add a lint over spec ACs that flags `env -i … bash -c '…$name…'` where `name` is not passed through `env -i`.

### M6 — S8's tip-field reader inventory is stale after unit 41, and AC8 targets a retired key (id 36)

- **Where:** `TOOL-dPlacedRequest-43` §2 S8 (Readers line) and §6 AC8.
- **What is wrong:** S8 changes how the queue line spells an empty tip (to `-`). Its Readers line lists only the readers minted by units 1 and 24, including 24 S3's ref-and-cached-tip dedupe, which TOOL-dPlacedRequest-41 S2 replaces. It omits three things:
  - 41 S1's newest-queued-line base.
  - 41 S3's per-ref chain rule in the flush.
  - 42 S2's writer, which queues "with an empty expected tip".
- **Consequence:** a builder following S8 routes only the named functions through `derive_queue_tip`. AC8's red case ("one side compares the raw empty field with -") targets the dedupe key that 41 retired, so AC8 can pass while a stranded reader stays broken.
- **Fix (judged sound):**
  - Name every reader and writer of the tip field across the build: `add_gov_queue`'s newest-line lookup and base (41 S1), `write_gov_queue`'s per-ref chain and compare-and-swap (41 S3, 24 S4 and S5), and the offline create writer (42 S2).
  - Retarget AC8 at 41's chain: queue an offline create with an empty tip, then a release on the same ref. The release's parent must be the create's commit, and the flush must land both.
- **Related:** L2 (id 7) is the coherence lens's narrower report on AC8's dedupe half, bound at low.
- **Gate:** checklist class a-spelling-change-strands-its-readers. A spelling change greps the whole spec set for readers, not only the units that minted the field.

### M7 — AC22's 47104-byte ceiling cannot be reached by the cuts S22 and S11 name (id 4)

- **Where:** `TOOL-dPlacedRequest-43` §6 AC22 (S22, S11).
- **What is wrong:** unit 34 measures 48821 bytes at HEAD, not the 50111 that §4 pins. The named cuts total about 1.7–1.8 KB, which leaves about 47.0–47.1 KB. S22 and S11 then require additions: a cite line, a line naming unit 33, a §9 rev line and a records row for the new research record.
- **Consequence:** a build that does exactly what the spec names lands at roughly 47.4–47.8 KB and fails AC22. Otherwise the builder must cut text the spec never names.
- **Fix (judged sound):**
  - Re-measure unit 34 at its current revision (48821).
  - Then either name further sections to move to the research record, enough to clear 47104 with the additions counted, or set the target from that measurement, still under 49152.
  - Replace §4's pinned 50111 figure.
- **Related:** L3 (id 19) covers the stale pin itself, bound at low.
- **Gate:** add a checklist entry: "a size ceiling in an AC is computed from a measurement at the spec's own base, with the named additions counted".

### M8 — the evidence for the `readCard` timeout points at the wrong `spawnSync` (id 20)

- **Where:** `TOOL-dPlacedRequest-43` §4 Evidence (S18).
- **What is wrong:** the evidence says "`scratch-guard.js`'s one `spawnSync` (`:710`) passes no `timeout`". Line 710 is `runGit` inside `checkAuthorizedReadme`, which spawns `git`. `readCard` (:667) spawns nothing at the base. Its bash call is added by TOOL-dPlacedRequest-34 S28, after which the file holds more than one `spawnSync`.
- **Consequence:** a builder may put the 5 s timeout on the README-authorisation git call. That leaves the hung-checker case S18 targets unbounded.
- **Fix (judged sound):** cite `readCard`'s bash spawn as the one added by TOOL-dPlacedRequest-34 S28, not `:710`, and drop "one spawnSync".
- **Severity note:** the finder graded this low. The skeptic regraded it medium, because a misplaced bound leaves the target call unbounded.
- **Related:** L4 (id 25) covers the same pointer together with the literal bound, bound at low.
- **Gate:** a line cite in evidence names the function as well as the line.

### M9 — AC6's grep half cannot fail, and S6's help-page change is observed by nothing (id 2)

- **Where:** `TOOL-dPlacedRequest-43` §6 AC6 (S6).
- **What is wrong:** the defective cause list lives in unit 3's spec table and in `help/loop.md`, not in `loop.toml`. Unit 3's toml rows carry only `outcomes`, `routes` and witness fields.
  - `grep -n 'follow-leases'` over `loop.toml` therefore prints nothing whether or not the defect stands.
  - Where a cause line does appear, it spells `refuse`, not `refused`.
  - §5 says no `help/` page is touched, although S6 edits `help/loop.md`.
- **Consequence:** a build that leaves `help/loop.md` listing `offline` under `refused` for `follow-leases` passes AC6. Only the behavioural half (exit 4) observes anything.
- **Fix (judged sound):**
  - Point the static half at the surface that carries the cause list: `grep -n 'follow-leases' help/loop.md` must name it only on the `awaiting` row.
  - Stage the red against the current wording "offline under refuse or follow-leases".
  - Add `help/loop.md` to §5's user docs.
- **Gate:** checklist class fixture-passes-by-finding-nothing. A static AC is staged red against the current text before it counts.

### M10 — AC17's `--plant publish-late` has no runner, no file and no arm (id 3)

- **Where:** `TOOL-dPlacedRequest-43` §6 AC17, §4 Files touched and §7.
- **What is wrong:** no spec defines `publish-late`. The card-store fixture `skills/session-kickoff/card-store.fixture.sh` comes from unit 2 S12, with arms added by units 33 and 34. It is absent from unit 43's Files touched and from §7, and AC17 does not name its runner.
- **Consequence:** the builder is never told to add the plant, and S17's new kill line has no lasting arm.
- **Fix (judged sound):**
  - Name the runner: `skills/session-kickoff/card-store.fixture.sh --plant publish-late`.
  - Add that file to §4 Files touched.
  - Add a §7 line: "New arm: `skills/session-kickoff/card-store.fixture.sh` · covers AC17 · a stub driver that writes the ref then sleeps past the bound set to 2, staged against the `not written` kill line". Per M1, the bound is `CARD_PUBLISH_BOUND`.
- **Gate:** checklist class observed-by-claim-no-arm-discharges. Every plant named in an AC is defined in a file listed under Files touched.

### M11 — AC15 expects `same` without planting the prior-session fact that yields it (id 8)

- **Where:** `TOOL-dPlacedRequest-43` §6 AC15 (S15).
- **What is wrong:** AC15 plants two present, differing sessions with equal keepalives in `take-over` mode and expects class `same`. At `unattended.sh:2263`, the take-over row yields `same` only when the run-state `prior-session` fact names the record's session and its keepalive matches. AC15 plants no such fact.
- **Consequence:** a correct build, which keeps the rows unchanged as S15 requires, reads `foreign-<verdict>`. AC15 therefore cannot pass on such a build.
- **Fix (judged sound):** have AC15 plant the run-state `prior-session` fact naming the record's session, plus the matching `keepalive` fact, and then expect `same`. Or keep the fixture as it is and expect a `foreign-` class, as AC31 does for `lease` mode.
- **Gate:** an AC's expected output is traced through the code rows it names before the spec is promoted.

### M12 — 38's carrier arm calls `add_feed_event` on an unborn repository, so it never reaches the lock path (id 10)

- **Where:** `TOOL-dPlacedRequest-38` §2 S1, §4 "The arm" and §5 perf.
- **What is wrong:** the arm runs "one git init per copy" and calls `add_feed_event refs/gov/bar-red <commit>` without naming a commit. Before the lock is taken, the caller's shell runs `git rev-parse <commit>^{tree}`. On an unborn repository that read fails, and the call returns 0 with a NOTE.
- **Consequence:** the lock, key check, counter and append never run. The arm checks only rc, stderr and the absence of a lock dir, never that `gov-feed.log` grew. It therefore reads green on a copy whose append body reads a carrier-only name, which is exactly the class finding 24 asks it to catch.
- **Fix (judged sound):**
  - In S1, commit once in the scratch repository and pass that commit's sha (or HEAD).
  - Have the arm assert that `gov-feed.log` gained one line after the call.
  - Stage a red: a copy whose append step reads `$ROOT` after the lock.
- **Gate:** an arm asserts the positive effect of the path it exercises, not only the absence of failure.

### M13 — the `run_driver_bounded` print contract overrides two callers' outcome lines (id 23)

- **Where:** `TOOL-dPlacedRequest-43` §2 S19 and §4 "The bounded call (S19)".
- **What is wrong:** the helper prints `<cell> — skipped: <why>` when there is no conf, no driver or no `timeout -k`. Two of its four callers have different required outcomes:
  - The card publish (unit 33 S2) must print `card — remote-ref not written: <reason>`.
  - The lookup (unit 34 S11) must fall through quietly to the next store.
- **Consequence:** built as sketched, the extraction either breaks unit 33's criteria or forces each caller to re-wrap the helper's output, which is the duplication S19 sets out to remove.
- **Fix (judged sound):**
  - Have the helper print nothing and return a distinct code per skip reason, with the reason in a variable such as `RDB_WHY`.
  - Each caller prints its own line: `overlaps — skipped:`, `claims — skipped:`, `card — remote-ref not written:`, or the lookup's fall-through.
  - State in S19 that the four callers' outcome lines are unchanged.
  - Add to AC19 a publish case with no `.unattended.conf` that must print `card — remote-ref not written: ...`.
- **Gate:** add a checklist entry: "an extraction lists each caller's outcome lines and keeps them".

### M14 — `run_driver_bounded` drops the stderr that `derive_claims_line` reads on failure (id 28)

- **Where:** `TOOL-dPlacedRequest-43` §2 S19 and §4 "The bounded call (S19)".
- **What is wrong:** the sketch captures stdout only (`>"$RDB_OUT"`). `derive_claims_line` captures `2>"$sd/err"` (manifest-check.sh:655), and its failure branch reads both files (:690-695). The overlaps read sends stderr to /dev/null, and S19 does not say which of the two behaviours the helper keeps.
- **Consequence:** a `--claims` run that fails with its error only on stderr shows `--claims exited <rc> and printed nothing` in the card. The stderr text leaks to the caller's stream.
- **Fix (judged sound):**
  - Have the helper capture stderr to a second file, `$RDB_ERR`, and have the claims caller keep reading both files in its failure branch.
  - Name `derive_claims_line`'s `$sd/err` read as a consumer under S19.
  - Add `skills/session-kickoff/manifest-check.test.sh` to Files touched, with an arm whose stub driver writes only to stderr and exits 1, asserting that the claims cell shows that line.
- **Gate:** the same checklist entry as M13. An extraction enumerates every stream each caller reads.

### M15 — AC20's probe inherits the machine's `GOV_NODE` (id 24)

- **Where:** `TOOL-dPlacedRequest-43` §6 AC20 (S20).
- **What is wrong:** AC20 sets only `USERNAME`, but `resolve_node_tag` returns `GOV_NODE` before it reads any user (run-selftests.sh:294). Unit 34 S30 makes `resolve_fleet_tag` honour `GOV_NODE` too.
- **Consequence:** on a node that exports `GOV_NODE`, AC20 falsely reds on every row with another tag. On the row that matches, it passes without testing user matching. aBatchedArm already hit this class and fixed it in D12.
- **Fix (judged sound):** run the probe as `env -u GOV_NODE -u USER USERNAME=<row user> ...`, or under `env -i` with PATH. Add a second case: with `GOV_NODE` set to a registered tag, all three resolvers print that tag.
- **Gate:** checklist class fixture-inherits-ambient-machine-state. Every resolver probe unsets the resolver's override variables.

### M16 — units 36, 37 and 39 share order 5 but write the same four files (id 27)

- **Where:** the `order 5` status lines of `TOOL-dPlacedRequest-36`, `-37` and `-39`, and their §4 Files touched.
- **What is wrong:** the build index renders order 5 as one parallel group (16, 26, 36, 37, 38, 39 and 41, Parallel yes). Units 36, 37 and 39 each write `tools/lib/gov-feed.sh`, `unattended.sh`, `post-merge.sh` and `unattended.test.sh`, and each re-carries the same `gov_feed_sh` block. Unit 38's arm is red until 36 and 37 land.
- **Consequence:** the rendered order presents as parallel what BUILD-METHOD's parallel-when-disjoint rule forbids. `--dispatch`'s write-set check would still sequence the passes, so the harm is a misleading index.
- **Fix (judged sound):**
  - Give 36, 37 and 39 distinct order values, for example 5, 6 and 7, with 38 after them, and move the downstream orders.
  - Or merge the three block edits into one unit, since they share item H1.
  - State in each spec's §4 that its write set intersects its siblings' and that the passes run in sequence.
- **Gate:** make `gen_build_index.py` refuse an order group whose units' Files touched intersect.

### M17 — S30 makes `--request` a third node-lock caller with no busy outcome (id 37)

- **Where:** `TOOL-dPlacedRequest-43` §2 S30 and §6 AC30.
- **What is wrong:** `write_node_lock` is single-shot: it returns 0 when taken and 1 when busy. 24 S2 gives the 50 ms × 5 s retry and a named busy refusal only to the feed and queue callers. S30 gives `requests.lock` no retry, no refusal line and no exit code. 37 S1 sizes its 10 s bound for "both callers" only.
- **Consequence:** AC30's second call can meet a busy lock and exit with an unspecified status. The race then surfaces as an unnamed failure or a flaky AC.
- **Fix (judged sound):**
  - State in S30 that `--request` retries `requests.lock` every 50 ms for up to 5 s, as 24 S2's two locks do.
  - A lock it cannot take prints a named refusal (for example `request not written — requests.lock busy`), exits 2 and writes nothing.
  - Add an AC that holds `requests.lock` planted and fresh, and asserts that refusal.
  - Add a line to 37 S1 naming the request section as covered by the 10 s bound.
- **Gate:** add a checklist entry: "a new caller of a shared lock factory states its busy outcome".

### M18 — 41's offline write has no outcome for an unreadable queued commit (id 38)

- **Where:** `TOOL-dPlacedRequest-41` §2 S1, §4 "The offline write" and §5 error and empty states.
- **What is wrong:** the next offline write reads the newest queued commit's record and parents on it. Queued commits are unreferenced loose objects, so `git gc` can prune them, and a queued line can be truncated or malformed. The spec says nothing about either case.
- **Consequence:** on a long offline session, the next write may abort, chain on garbage, or fall back to the cached tip. Falling back recreates the silent-drop shape this unit closes. The queued release is lost or never queued.
- **Fix (judged UNSOUND, so the skeptic's corrected fix is written here):**
  - State the outcome: when `git cat-file -e` does not find a queued line's commit, or the line's fields fail the line shape, the new write is refused with a named `queue: NOTE` line and exit 2, and nothing is appended.
  - Add an AC that plants a queued line naming an absent sha and asserts the refusal.
  - Keep queued commits out of any ref.
- **Gate:** add a checklist entry: "a hard input read from a prior write names its unreadable and malformed outcomes".

## Low

### L1 — the `env -i` probes drop `$c`, reported by the failure-envelope lens (id 39)

- **Where:** `TOOL-dPlacedRequest-38` §4 "The arm", `TOOL-dPlacedRequest-36` AC1 and `TOOL-dPlacedRequest-37` AC1.
- **What is wrong:** this is the defect M5 describes, and its binding grade is low. The skeptic's reason for low is that the failure is loud, so a builder corrects it on the first run.
- **Fix (judged sound):** `env -i PATH="$PATH" HOME="$HOME" c="$c" bash -c '...'`, in 38 §4, 36 AC1 and 37 AC1.
- **Gate:** the same lint as M5.

### L2 — AC8's dedupe half is green whatever the tip encoding, after unit 41 (id 7)

- **Where:** `TOOL-dPlacedRequest-43` §2 S8 and §6 AC8, against TOOL-dPlacedRequest-41 S1 and S2.
- **What is wrong:** after unit 41, a second offline create builds on `q.commit` and dedupes by record, so the `grep -c` printing 1 never compares tip fields. S8 still lists `add_gov_queue`'s base as a reader of the field. The flush half of AC8 still observes the encoding.
- **Fix (judged sound):**
  - Restate S8's readers as `write_gov_queue`'s compare-and-swap and the resolved-line rewrite, plus unit 42's empty-tip create as the writer.
  - Drop the dedupe half of AC8, or recast it: "a flush of a `-` line creates the ref, and a scratch copy whose compare-and-swap reads `-` literally fails to push".
- **Severity note:** the finder graded this medium. The skeptic regraded it low, because the gap is partial.
- **Related:** M6 (id 36).
- **Gate:** the same as M6.

### L3 — §4 pins a stale 50111-byte size for unit 34 (id 19)

- **Where:** `TOOL-dPlacedRequest-43` §4 Evidence (sizes) and S22.
- **What is wrong:** 50111 is the size at dfb9b0d30. The round-2 fold, commit 6ff06ef26, rewrote spec 34, which is 48821 bytes at HEAD.
- **Consequence:** the cut is planned against a figure the tree no longer holds.
- **Fix (judged sound):** re-measure spec 34 at the build's base and restate the pin, or cite the measuring commit (dfb9b0d30) beside the figure.
- **Related:** M7 (id 4).
- **Gate:** a PINNED figure carries the commit at which it was measured.

### L4 — the `readCard` spawn citation is wrong, and S18 hard-codes the bound (id 25)

- **Where:** `TOOL-dPlacedRequest-43` §4 Evidence (the scratch-guard bullet) and §2 S18.
- **What is wrong:** `:710` is `checkAuthorizedReadme`'s `runGit`, not `readCard`. S18 also writes the bound as a bare `timeout: 5000`, although `stop-guard.js` already has a bounded bash-spawn shape with a named constant and an env override.
- **Consequence:** AC18's arm must wait out the full 5 s.
- **Fix (judged sound):**
  - Re-point the evidence: `readCard` (`scratch-guard.js:667`) has no spawn at the base, and unit 34 S28 adds it.
  - Name `tools/unattended/stop-guard.js:106-114` (`runLiveness`, with `LIVENESS_BOUND_MS` and its `STOP_GUARD_LIVENESS_BOUND_MS` override, `timeout: bound, killSignal: 'SIGKILL'`) as the shape to follow.
  - Spell the bound as a named constant, for example `CARD_READ_BOUND_MS = 5000`, with an env override for the test arm.
- **Related:** M8 (id 20).
- **Gate:** checklist reuse class. A new bound reuses the sibling hook's bounded-spawn shape.

### L5 — AC21 only counts bytes and is already green (id 6)

- **Where:** `TOOL-dPlacedRequest-43` §6 AC21 (S21).
- **What is wrong:** the protocol measures 66859 bytes against a limit of 66860 today. AC21 never observes S21's content change: that the `RUN_CLAIMS` row names no ref and cites STOPS §7.
- **Consequence:** a build that trims 8 bytes anywhere passes, and the row keeps naming the moved ref.
- **Fix (judged sound):**
  - Add a content observation: `grep -n 'RUN_CLAIMS' tools/unattended/PROTOCOL.template.md`, where the row names no `refs/gov/` path and cites `UNATTENDED-STOPS.md` §7.
  - Keep the size check as a second clause, measured after unit 34 S35.
- **Severity note:** the finder graded this medium. The skeptic regraded it low, because the effect is stale prose.
- **Gate:** an AC observes the item's content change, not only a side measure.

### L6 — no criterion runs an id-less `--lease status` (id 12)

- **Where:** `TOOL-dPlacedRequest-40` §2 S2 and §6.
- **What is wrong:** S2 exempts `status` and claims it is observed by AC1–AC3, which exercise only prune, flush and fence. Unit 34 has no such case either.
- **Consequence:** if `status` is left off the exempt branch, the deny-by-default case refuses a read-only act, and nothing reds.
- **Fix (judged sound):** add an AC, to unit 40 or to 34 next to its AC22: `env -u CLAUDE_CODE_SESSION_ID … --lease status build tFix` exits 0 and prints the status line. Stage it against a scratch copy that leaves `status` off the exempt list.
- **Gate:** every member of an enumerated exempt set has its own AC.

### L7 — AC25's single `grep -c` over an alternation cannot decide "each" (id 13)

- **Where:** `TOOL-dPlacedRequest-43` §6 AC25 (S25).
- **What is wrong:** AC25 prints one combined count, so a README naming only `node-lock-broken` passes.
- **Fix (judged sound):** run one `grep -c` per event and require each to be at least 1.
- **Gate:** add a lint flagging `grep -c` over `\|` in an AC that says "each".

### L8 — 36's Goal says a stale break aborts the carrier; it only loses the event (id 17)

- **Where:** `TOOL-dPlacedRequest-36` §1 Goal.
- **What is wrong:** `$ROOT` is expanded inside `$(resolve_health_log "$ROOT")`, so only the subshell dies. `post-merge.sh` has `set -u` with no errexit, so the script carries on after rc 127.
- **Consequence:** the mechanism is misdescribed, and the next change may misread the guard's purpose.
- **Fix (judged sound):** restate the Goal: on the stale-break path, the event is lost and two error lines reach stderr. The carrier is killed only by finding 13's arithmetic on REMOTE_BOUND, which TOOL-dPlacedRequest-37 owns.
- **Gate:** none fits. Add a checklist entry: "a claimed abort names the shell options that make it one".

### L9 — 38's "well under a second" perf claim is untimed and wrong on Windows (id 18)

- **Where:** `TOOL-dPlacedRequest-38` §5 perf and scale.
- **What is wrong:** a lighter proxy took about 1.9–2.2 s on this Windows node.
- **Consequence:** the claim misstates the parity leg's budget.
- **Fix (judged sound):** time the arm once on a Windows node when it is built and state the measured figure, or drop the sub-second claim.
- **Gate:** a perf claim carries a measurement and the node it was measured on.

### L10 — 38's carrier arm greps its population with no pathspec (id 29)

- **Where:** `TOOL-dPlacedRequest-38` §2 S1 and §4 "The arm".
- **What is wrong:** a bare `git grep -l '^# >>> gov_feed_sh'` differs from the PARITY_ROWS loop's `-- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md` and its exclude prefix.
- **Consequence:** a Markdown record quoting the marker at column 0 would join the arm's population, causing a false red. The defect is latent, since no such record exists today.
- **Fix (judged sound):** reuse the parity loop's `copies` list for the `gov_feed_sh` row, plus the canonical file. At minimum, use the loop's pathspec.
- **Gate:** checklist class two-readers-of-one-config-one-re-derived.

### L11 — 37's 10 s lock bound is justified as "microseconds" without naming the sections it covers (id 30)

- **Where:** `TOOL-dPlacedRequest-37` §2 S1 and §5 risks.
- **What is wrong:** unit 41's offline write, unit 42's create and unit 43 S30's request copy each hold a node lock across several git spawns. S1 names none of them.
- **Consequence:** the justification is wrong. The sections will probably still finish inside 10 s.
- **Fix (judged sound):** list the sections the bound covers, and re-justify 10 s against the longest of them, measured once on this node. Alternatively, keep the commit building outside `gov-queue.lock`.
- **Gate:** a lock bound lists every critical section it covers.

### L12 — AC26's red-when claims more than its probe checks; `lease-yielded` is undocumented (id 31)

- **Where:** `TOOL-dPlacedRequest-43` §2 S26 and §6 AC26.
- **What is wrong:** the probe lists only the events from the `gov_feed_sh` cut. The driver's `lease-yielded` event, emitted per units 1, 24 and 41, is not in `tools/unattended/README.md`.
- **Consequence:** the README stays incomplete while AC26 is green.
- **Fix (judged sound):** widen S26 and AC26 to every event token passed to `add_health_event`, and add `lease-yielded` to the README sentence. Or narrow the red-when to the `gov_feed_sh` block's events and file the driver-wide gap as its own item.
- **Gate:** an AC's red-when matches the population its probe reads.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=39 confirmed=39 refuted=0 unverified=0 blocker=1 high=4 medium=22 low=12 agents=11 out-tokens=75454

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S16, section 8 F3 (against TOOL-dPlacedRequest-2 S6 and TOOL-dPlacedRequest-34 S11) | medium | medium | confirmed | Unit 2 line 79 bounds the S6 lookup under `CARD_FETCH_BOUND`, and unit 34 line 65 (S11) runs `--card-ref lookup` under `timeout -k 2 "$CARD_FETCH_BOUND"`. Unit 33 lines 47 and 100 run the publish under the same name. Unit 43 S16 (line 80) gives that one shared constant a default of 140. Two corrections to the finding. First, the constant had no value before: manifest-check.sh declares only OVERLAP 10, CLI 5 and CLAIMS 15, and review-23 line 158 says it 'has no value anywhere'. Second, the driver's lookup goes through observe_remote, which is killed at REMOTE_BOUND=60 (unattended.sh:162 and :484), so a hung remote holds the lookup for about 65 s rather than the full 140. That is still more than four times the 15 s claims cell. The lookup is a read on the kickoff and replay path, and F3 never weighed a separate bound for it. The effect is a slower read, so the damage is contained. | sound | two-answers-to-one-question |
| 2 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 6 AC6 (S6) | medium | medium | confirmed | In unit 3 (lines 111-136) the toml rows carry only `outcomes`, `routes` and witness fields. The cause list sits in the spec's markdown table at line 186 ('`offline` under `refuse` or `follow-leases`') and in the help page that S7 creates (line 71, `help/loop.md`). So `grep -n 'follow-leases'` over loop.toml prints nothing whether or not the defect is fixed, and AC6's static half cannot go red. Unit 43's §4 Files touched names 'its help page' for S6, but AC6 never reads it. §5 also says 'no `help/` page covers the driver' and leaves the page out of its user docs. The behavioural half (exit 4) does observe something, so the damage is contained. | sound | fixture-passes-by-finding-nothing |
| 3 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 6 AC17, section 4 Files touched, section 7 | medium | medium | confirmed | `grep -rn publish-late` finds the plant only at unit 43 line 280: no spec defines it. Unit 43's §4 Files touched (lines 200-214) does not include `card-store.fixture.sh`. Its §7 arms (lines 322-324) cover AC1-4, 7, 8, 10, 14, 15 and 27-33, plus AC28 and AC18, and none covers AC17. AC17 does not name its runner either. Only the §6 preamble points loosely at 'unit 2's card store fixture'. The finder's attribution is slightly off: the fixture comes from unit 2 S12 (line 119), and units 33 and 34 add arms to it. The defect stands anyway: the builder is never told to add the plant, and S17's kill line has no lasting arm. | sound | observed-by-claim-no-arm-discharges |
| 4 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 6 AC22 (S22, S11) | medium | medium | confirmed | I re-measured unit 34. `git cat-file -s` gives 48821, against the 50111 PINNED at unit 43 line 179, so that figure is stale. The cuts S22 and S11 name measure: 'Measured sizes' 483, 'The one deletion outside leases' 347, S10 (lines 61-63) 283, S13 (lines 72-74) 240, AC10 288 and AC13 159. They total about 1800, which leaves about 47021. S22 and S11 then add a cite line, a line naming unit 33, a §9 rev line and a rendered records row for the new research record; the existing rows run about 150-300 bytes each. That puts the result at roughly 47.4-47.6 KB, over AC22's 47104. So a build that does only what the spec names fails AC22. | sound | - |
| 5 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S24, section 6 AC24, section 3 (against TOOL-dPlacedRequest-34 AC59) | medium | medium | confirmed | Unit 34 line 556 (AC59) still runs `git diff c63aabbb..HEAD`. Unit 43 §3 (lines 145-146) allows edits to unit 34's criteria only for S11 and S22, so S24 leaves AC59 standing next to AC24's corrected `git log` oracle. Unit 34's hands-off edge (line 270) says unit 43 will 're-observe' AC59, but its text is never corrected. I ran S24's git log pipeline at HEAD: it printed 0 matches, so AC24 is already green today. The `git diff` form also printed 0 today. Its false red only appears once main's mint commits are merged in. | sound | two-answers-to-one-question |
| 6 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 6 AC21 (S21) | medium | low | confirmed | `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md \| wc -c` printed 66859, against the limit of 66860 at template-size-limits.txt:143. One nuance: unit 34 S35 adds 8 bytes and lands earlier (order 22, before 43 at order 24), so at build time AC21 does need some cut. Still, AC21 only counts bytes. It never checks S21's content change, the PROTOCOL.template.md:521 row naming no ref and citing STOPS §7. A build that trims 8 bytes anywhere passes. The cost is small: the row keeps naming the moved ref, which reads as stale prose, not wrong behaviour. | sound | - |
| 7 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S8, section 6 AC8 (against TOOL-dPlacedRequest-41 S1, S2) | medium | low | confirmed | Unit 41 (order 5) S1 and S2 (lines 32-39, 66) build on `q ? q.commit : cached tip` and dedupe by a record compare 'less stamps'. That replaces unit 24 S3's ref-and-cached-tip key. A second offline create of tOff therefore finds the queued line, builds on q.commit and prints `queued — already` without comparing any tip field. AC8's `grep -c` printing 1 is then green whatever encoding is used. S8 (lines 55-57) still lists `add_gov_queue`'s base as a reader of the field, which is out of date. The flush half of AC8 still observes the encoding, so the gap is partial. | sound | - |
| 8 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 6 AC15 (S15) | medium | medium | confirmed | I read unattended.sh:2254-2264. `me` is CLAUDE_CODE_SESSION_ID and `ps` is set only from a run-state `prior-session` fact. Take a record in s1 and a caller in s2 with equal keepalives in take-over mode. Row 2260 fails because the sessions differ, 2261 is excluded in take-over, and 2262 fails because c_sess is not me. Row 2263 gives `same` only when `ps` contains c_sess and c_ka equals the keepalive fact. AC15 plants no such fact, so a build that keeps the rows unchanged, as S15 requires, reads `foreign-<verdict>`. The review's own consequence (review-23 line 151) speaks of 'a resumed run's prior session', which presupposes that fact. | sound | - |
| 9 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md:section 6 AC1 against section 4 'The append' and S2 | medium | medium | confirmed | Re-read -39.md:68-69. The subshell's first line is `write_node_lock "$dir/gov-feed.lock" "$tok" \|\| exit 3` and its second is `trap 'remove_node_lock …' EXIT`. AC1 (:115-118) plants `: "$GOVFEED_PLANT_UNSET"` 'directly after the lock take' and requires that no gov-feed.lock remain. A plant placed there literally runs before the trap exists, so a build faithful to §4 leaves the lock held and fails AC1. Unless the builder silently reorders the design, the AC and the design disagree. | sound | - |
| 10 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-38.md:section 2 S1, section 4 'The arm', section 5 perf | medium | medium | confirmed | -38.md S1 and §4 run the arm 'inside a scratch repository' and call `add_feed_event refs/gov/bar-red <commit>` without naming the commit. §5 perf says 'five calls and one `git init` per copy', so no commit is made. -13.md:107-109 and -39.md:67 read the tree with `git rev-parse <commit>^{tree}` in the caller's shell before the lock. On an unborn repository that read fails before the lock, key check, counter or append runs, and the arm checks only rc, stderr and the absence of a lock dir, never that gov-feed.log grew. So a copy whose append body reads a carrier-only name passes. The arm's own 'What it does not check' does not disclose this gap. Unit 39 §6, by contrast, explicitly uses 'one commit `$h`'. | sound | - |
| 11 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-36.md:section 2 S2, section 6 AC3 (with TOOL-dPlacedRequest-38 section 3) | medium | medium | confirmed | -36.md S2 states the class 'Every file carrying gov_feed_sh carries the health_log_sh block too, inline'. AC3 (:122) greps only post-merge.sh. -38.md §3 disowns carriage and points at 36 AC3, and its arm sources the canonical health-log.sh. grep -n health_log_sh on spec -15 shows only :90, a consumes-from edge, with no scope item or AC. On the tree, `grep -c '^# >>> health_log_sh'` gives unattended.sh:0, lib-unattended.sh:1 and push-main.sh:0, and unattended.sh:101 sources lib-unattended.sh. So push-main.sh's future carriage is observed nowhere, and 'inline' does not describe unattended.sh, which gets the block by sourcing. | sound | two-answers-to-one-question |
| 12 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-40.md:section 2 S2, section 6 | low | low | confirmed | -40.md S2 says the exempt set (prune, flush, fence, status) is 'Observed by AC1, AC2 and AC3'. Those ACs (:112-121) exercise prune, flush and fence only. In -34.md, the only status criterion is AC22 (:468), which uses two same-node sessions, and no criterion runs an id-less `--lease status`. A `status` left off the exempt branch would be refused by deny-by-default and nothing would go red. | sound | - |
| 13 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 6 AC25 (S25) | low | low | confirmed | -43.md:297-298 says AC25 runs `grep -c 'node-lock-broken\\|node-lock-guard-cleared' tools/unattended/README.md` and expects 'at least 1 for each'. grep -c over an alternation prints one combined count of matching lines, so it cannot decide 'each', and a README naming only one event passes. AC26's per-event probe may cover this in practice, so the effect is limited to the criterion's wording. | sound | - |
| 14 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md:section 2 S2, section 4 "The append" | medium | medium | confirmed | The factory is modelled on write_claim_push_lock (unattended.sh:2331-2354). It mkdirs the lock, then writes `until` with `$(( $EPOCHSECONDS + REMOTE_BOUND + 10 ))` (:2347), then `owner`. In §4 of -39 the EXIT trap is set only after `write_node_lock … \|\| exit 3` returns. An unbound name between the mkdir and the until write ends the subshell with the dir made, no until file, no owner file and no trap, so S2's claim 'an abort leaves no gov-feed.lock' is false there. With no until, check_*_lock_stale falls back to the two-minute mtime test (:2329), so later appends report lock-busy for about two minutes. -39.md §3 says the unit 'bounds the damage of any such name, present or future', and AC1 plants only after the take. The finder's scratch probe shape is consistent with this. | unsound | - |
| 15 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-37.md:section 6 AC1 (also TOOL-dPlacedRequest-36 section 6 AC1/AC2 and TOOL-dPlacedRequest-38 section 4 "The arm") | medium | medium | confirmed | Re-probed: `c=$S; export c; env -i PATH="$PATH" bash -c 'set -u; echo "$c/x"; echo reached'` printed `bash: line 1: c: unbound variable` and rc=127. The commands in -37.md AC1 (:106-108), -36.md AC1/AC2 (:112-115) and -38.md §4 (env -i PATH HOME only) all expand `$c` inside the single-quoted body without passing it through env -i. As written they abort before the factory runs, on both the green case and the red case, so they cannot tell a good copy from a bad one. | sound | - |
| 16 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 6 AC30 (item S30) | high | high | confirmed | -43.md:307-308 says AC30 starts 'two background `--request` calls … exactly one exits 2 printing `collision`. Red when: both copy.' Neither S30 (:128-130) nor AC30 places the second call inside the first one's compare-to-copy window. On unlocked code the calls usually run one after the other, the second compare sees the first's stored copy, and per -30.md S1 it is refused collision. So the AC goes green without the requests.lock it is meant to certify, and the racing overwrite that §5 security claims to close ships unobserved. It is graded high rather than blocker because the defect it would miss occurs only on a narrow race path. | sound | fixed-sleep-does-not-place-a-signal |
| 17 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-36.md:section 1 Goal | low | low | confirmed | Spec 36:27-28 says a stale break "aborts the carrier". grep over tools/run-gates/post-merge.sh found `set -u` at :26 and no errexit or pipefail. The only trap is an EXIT trap at :363. No ROOT, add_health_event or resolve_health_log is defined there. `$ROOT` is expanded inside `$(...)`, so the unbound-variable error kills only that subshell. The undefined function gives rc 127, and without errexit the script carries on. The event is lost but the carrier survives. The abort that does happen comes from arithmetic on REMOTE_BOUND, which spec 37:27 owns. Only the wording is wrong; the design is unaffected. | sound | - |
| 18 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-38.md:section 5 perf / scale | low | low | confirmed | Spec 38:93 says "well under a second" and gives no timing. I re-ran a lighter proxy under scratch (four copies of env -i bash: git init, an empty commit, two rev-parse calls, two date calls, two mkdir/rmdir cycles). It printed real 0m1.938s. The sub-second figure is wrong on this Windows node. The effect is limited to the stated budget. | sound | - |
| 19 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 4 Evidence (sizes) and S22 | low | low | confirmed | `git cat-file -s dfb9b0d30:<spec 34>` printed 50111 and HEAD printed 48821. `git log` shows 6ff06ef26 rewrote spec 34 after dfb9b0d30. The pin at spec 43:179 is stale, which affects only how the cut is planned. AC22's ceiling of 47104 still holds the line. | sound | - |
| 20 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 4 Evidence (S18) | low | medium | confirmed | grep for spawnSync in tools/hooks/scratch-guard.js found only :709 (the require) and :710 (`runGit = ... spawnSync('git', ...)`). readCard at :666-677 does fs.readFileSync and spawns nothing. Spec 43:176's "one spawnSync (:710)" points at the README-authorization git call, not readCard's checker call. A builder following it could put the timeout on the wrong call. S18's own text does name readCard's bash call, which softens this a little. | sound | - |
| 21 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S24 and section 6 AC24 | high | high | confirmed | push-main.sh:921 runs `git commit-tree ... -p "$R" -p "$oldb"`, so the prepared merge's first parent is the main tip. Spec 43:113 S24 runs `git log --first-parent --no-merges ... c63aabbb..HEAD`, and AC24 (:295-296) runs it on the prepared merge. That walks main's line and drops the merge, so no branch commit is ever read. A branch hand-bump goes unseen, and AC24 passes whatever the branch did. | sound | a-merge-of-the-default-branch-read-as-additions |
| 22 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S16, section 6 AC16, section 8 F3 | medium | medium | confirmed | CARD_FETCH_BOUND is also the read-only lookup's bound. Spec 2:79 fetches the card ref under it, and spec 34:65 (S11) runs `--card-ref lookup` under `timeout -k 2 "$CARD_FETCH_BOUND"`, falling back to the next store on no answer. Spec 43 S16 raises its default to 140 s and never splits the lookup off. A hung remote would then stall the lookup for 140 s, against TOOL-aGraftedHelix-2's 15 s kill bound for a remote read (DECISIONS.md:218). AC16's Red-when is turned around. | unsound | - |
| 23 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S19 and section 4 'The bounded call (S19)' | medium | medium | confirmed | Spec 43 §4's sketch has the helper print `<cell> — skipped: <why>` on no conf, no driver or no timeout -k. Spec 33:47-49 requires `card — remote-ref not written: <that reason>` for those same cases. Spec 34:64-66 S11 requires the lookup to fall through to the next store with the `evidence` verdict. S19 (:89-92) names both as callers and never says their outcome lines are kept. | sound | - |
| 24 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 6 AC20 (item S20) | medium | medium | confirmed | run-selftests.sh:294 checks GOV_NODE first in resolve_node_tag. Spec 34:131 and :281 make the resolvers honour GOV_NODE. The aBatchedArm ledger at :142 (D12) records the same leak and its `unset GOV_NODE` fix. AC20 (spec 43:287-288) sets only USERNAME, so on a node that exports GOV_NODE it answers from the environment. It then either reds falsely or passes without testing user matching. The damage is confined to this test. | sound | fixture-inherits-ambient-machine-state |
| 25 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 4 Evidence (the scratch-guard bullet) and section 2 S18 | low | low | confirmed | Spec 43 line 176 reads "`scratch-guard.js`'s one `spawnSync` (`:710`) passes no `timeout`; `readCard` is at `:667`". In tools/hooks/scratch-guard.js, readCard (line 667) only calls fs.readFileSync. The spawnSync near :710 is checkAuthorizedReadme's runGit (`spawnSync('git', args, { cwd: toplevel, encoding: 'utf8' })`), so the citation names the wrong call. Spec 43 S18 (line 86) writes the bound as the literal `timeout: 5000`. stop-guard.js:97-114 already has the shape to copy: a named `LIVENESS_BOUND_MS` constant, the `STOP_GUARD_LIVENESS_BOUND_MS` env override, and `timeout: bound, killSignal: 'SIGKILL'`. readCard's bash spawn comes from spec 34 S28 (line 123), as the fix says. The wrong pointer could mislead a builder, but nothing changes at runtime, so low. | sound | - |
| 26 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S24 and section 6 AC24 | high | blocker | confirmed | tools/push-main.sh:921 builds the prepared merge with `commit-tree ... -p "$R" -p "$oldb"`, and line 947 prints `first parent ${R:0:8} (the advertised tip)`. S24 (spec 43:112-114) uses `git log --first-parent --no-merges ... c63aabbb..HEAD`, and AC24 (line 295) runs it on the prepared merge. On that commit the first-parent walk follows main. Re-probed: `git log --first-parent --no-merges --oneline c63aabbb..origin/main` printed nothing, and `rev-list --first-parent --count` printed 1, so main's line since the base is a single merge. From the branch tip the same walk lists 11 commits. So on the prepared merge AC24 prints nothing whether or not a branch commit hand-bumps the version. It certifies 'no hand-bump' without reading a single build commit, which the rubric grades blocker. | sound | test-oracle-read-from-a-historical-sha |
| 27 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-36.md:Status line `order 5` (also TOOL-dPlacedRequest-37 and TOOL-dPlacedRequest-39 `order 5`), section 4 Files touched | medium | medium | confirmed | README.md:180 renders order 5 as one parallel group: 16, 26, 36, 37, 38, 39 and 41, Parallel yes. gen_build_index.py's render_order docstring says units that share an order value are the parallel group. Section 4 of each of specs 36, 37 and 39 lists the same four files: tools/lib/gov-feed.sh, post-merge.sh, unattended.sh and unattended.test.sh. Spec 38 §5 (lines 96-97) says its arm is red until 36 and 37 land, which makes them its acceptance input. BUILD-METHOD's parallel-when-disjoint rule (lines 209-216) forbids running such passes together. None of specs 36-39 states the passes run in sequence. The rendered order misleads dispatch, but --dispatch's write-set rule would still sequence them, so the harm is contained: medium. | sound | - |
| 28 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S19 and section 4 'The bounded call (S19)' | medium | medium | confirmed | manifest-check.sh:655 runs the claims read with `>"$sd/out" 2>"$sd/err"`, and the failure-branch awk (lines 690-695) reads both `"$sd/out" "$sd/err"`. The overlaps read at line 564 sends stderr to /dev/null. Spec 43's S19 sketch (lines 194-197) captures only `>"$RDB_OUT"`, has no stderr file and does not say which behaviour the helper keeps. Built as sketched, a --claims run that fails with its error only on stderr would show 'printed nothing' in the card, and the stderr text would leak to the caller's stream. The effect is limited to one card cell, so medium. | sound | - |
| 29 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-38.md:section 2 S1 and section 4 'The arm' | low | low | confirmed | resolve-python.test.sh:218 finds copies with `git grep -l "^# >>> $stem" -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md \| grep -v "^$excl"`. Spec 38 (lines 33 and 59) uses a bare `git grep -l '^# >>> gov_feed_sh'` with no pathspec. `git grep -c '^# >>> ' -- '*.md'` lists spec-11 and other records, so a record quoting a block marker at column 0 already exists in this repo. No .md quotes the gov_feed_sh marker today, so the false red is latent. Since the two readers of one population can disagree, I grade it low. | sound | two-readers-of-one-config-one-re-derived |
| 30 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-37.md:section 2 S1 and section 5 risks | low | low | confirmed | Spec 37 S1 (lines 34-38) justifies 10 s as covering 'a holder's whole critical section', and §5 (line 95) calls it a 'microsecond section'. Spec 41 §4 (lines 63-72) holds gov-queue.lock while it reads the queue, builds the act with parent base, compares records and appends. Spec 43 S30 (line 128) holds requests.lock around a compare, a copy and the append. These sections run several local git spawns, not microseconds, and S1 does not name them. They will probably still finish well inside 10 s, but the justification is wrong and the covered sections are not listed, which could mislead the next change. Low. | sound | - |
| 31 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S26 and section 6 AC26 | low | low | confirmed | tools/unattended/README.md:246-252 is the sentence that lists the events the driver appends (run-resumed, claim-taken-over and others). `grep lease-yielded` over the README printed nothing. lease-yielded is emitted per specs 1 (S-row at line 102 and the table at 263), 24 and 41, and spec 43 S25 adds only node-lock-broken and node-lock-guard-cleared. S26 is scoped to events the gov_feed_sh cut emits, while AC26's red-when ('a new event lands undocumented') claims more. The README would stay incomplete with AC26 green. Only documentation is affected, so low. | sound | - |
| 32 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-35.md:section 2 S1 and S2, section 4 "The walk, per tail" | high | high | confirmed | Spec 35 S1 (lines 33-38) and §4 (lines 64-68) stop on `renews yes or absent` as the renewing beat; the next step is the `seen-utc < threshold -> resolve stale` test. A `renews: -` commit matches neither the epoch-change stop nor the renewing beat, so it reaches the threshold test. Spec 17:46 says a `renews: -` beat never reads stale. Spec 17 AC4 (lines 186-188) requires a commit sighted 1,000 hours ago to print `live`. Spec 26:41 keeps that rule, and spec 25 AC2 says `leases.renewal none` writes `renews: -`. Built as written, every lease under renewal none reads stale after expiry-hours and can be taken over. This holds only under that setting, so high. | sound | - |
| 33 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-35.md:section 2 S1 step (3), section 4 pseudo-code `seen-utc < threshold`, section 5 error/empty states | high | high | confirmed | 35.md §4 pseudo-code reads `seen-utc < threshold -> resolve stale`, and nothing in S1 or §4 guards an unsighted commit. §5 covers only 'an unsighted tenure start'. 34's S43 walk ('load the feed's seen-utc per commit') does not handle the unsighted case either. I re-ran the awk check: an uninitialised seen[x] < "2026-10-24T14:00:00Z" printed 'uninit stale', and the '-' placeholder (17.md:37) also compares less ('dash stale'). On an empty or missing feed, a non-renewing tip goes straight to this test and resolves stale, which breaks 17.md:47 and AC 17.md:196-197 ('never stale'). The path is narrow (an empty feed or an unsighted tip), but on it the walk returns a wrong verdict that permits a take-over. | sound | - |
| 34 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md:section 2 S2, section 4 "The append" (trap armed after `write_node_lock`), section 6 AC1 | high | medium | confirmed | `git show c63aabbb:tools/unattended/unattended.sh` lines 2331-2354 confirm the order the factory inherits (24.md:39-41 says the bodies are the claim-push bodies): mkdir, then the `until` printf, then the `owner` printf. remove_claim_push_lock removes only when owner matches, and check_claim_push_lock_stale falls back to `-mmin +2`. 39.md:68-69 arms the EXIT trap only after `write_node_lock ... \|\| exit 3`, and AC1 (39.md:115-116) plants after the take. So an abort inside the factory between mkdir and the owner write leaves an ownerless lock for about 2 minutes. 37 removes the present REMOTE_BOUND instance, but 39's non-goal claims to cover 'any such name, present or future', and this window falls outside what AC1 observes. The damage is contained: appends are dropped with NOTE lines for about 2 minutes. | sound | - |
| 35 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-36.md:section 2 S2, section 6 AC3 | medium | medium | confirmed | 36.md:122, AC3, greps post-merge.sh only, while S2 (36.md:40-44) states the rule for every carrier. 38.md:46-47 hands carriage to 36 AC3, and the 38 arm (38.md:60) sources the canonical health-log.sh cut, not the carrier's own. 15.md:90 consumes the rule for push-main.sh and has no AC on it (15.md:168 grades only the gov_feed_sh parity). `git grep -l '^# >>> gov_feed_sh'` currently lists nothing, so the population does not exist yet and nothing checks push-main's carriage when it arrives. If push-main omits the block, its stale-lock break hits an undefined add_health_event and the event is lost, which is contained. | sound | - |
| 36 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S8 (Readers line) and section 6 AC8 | medium | medium | confirmed | 43.md:54-58: S8's Readers line names add_gov_queue's base and write_gov_queue's CAS and rewrite as minted by units 1 and 24. 41.md:36-39 replaces 24 S3's ref-and-cached-tip dedupe with a record compare, and 41.md:65-70 adds a newest-queued-line lookup and the `q ? q.commit : cached tip` tip write. 42.md:38-39 adds an empty-tip create writer. Under 41, a second offline create finds a queued line, builds on it (42 S1) and dedupes by record, so AC8's first half (one line after two creates) no longer touches the tip encoding. Its red case ('compares the raw empty field with -') targets the key that 41 retired. The flush half still exercises write_gov_queue's CAS. The reader inventory is stale and AC8 is weaker than it claims. The finder's q.commit-shift scenario holds only if a writer bypasses derive_queue_tip, so the effect is contained. | sound | a-spelling-change-strands-its-readers |
| 37 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md:section 2 S30, section 6 AC30 | medium | medium | confirmed | 43.md:128-130 (S30) takes write_node_lock on requests.lock and gives no busy outcome, retry or exit code. AC30 (43.md:305-306) covers only the collision. 24.md:39 makes write_node_lock single-shot (0 taken or 1 busy), and 24.md:51-58 gives the 50 ms x 5 s retry and a named busy refusal with exit 2 to the feed and queue callers only. 37.md:36-38 sizes the 10 s bound against those callers, and 37.md:87 says 'Both callers'. A third caller with an undefined busy path is a real gap that could make AC30 flaky or produce an unnamed failure. The effect is contained. | sound | - |
| 38 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-41.md:section 2 S1, section 4 "The offline write", section 5 error/empty states | medium | medium | confirmed | 41.md:33-35 builds the next offline write on the newest queued commit and reads its record (41.md:107: one git cat-file per write). 1.md:103 says 'No value creates a ref, local or remote, while offline', so queued commits are unreferenced loose objects that gc can prune after its expiry. A grep over the spec set for prune, gc, reachability or a queued ref found nothing that keeps them reachable. 41 §5 covers only 'a chain whose head is lost' at flush, not an unreadable or malformed queued line at write time. The outcome is unspecified on a long-offline path, and the damage is contained to that ref's queue. | unsound | - |
| 39 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-38.md:section 4 "The arm" (also TOOL-dPlacedRequest-36 AC1 and TOOL-dPlacedRequest-37 AC1) | low | low | confirmed | 38.md:61-65, 36.md:112-113 and 37.md:106-107 each run `env -i PATH=... [HOME=...] bash -c '... "$c/gov-feed.lock" ...'` with $c inside single quotes. env -i clears the environment, so c is unset in the child, and under set -u the call aborts with 'c: unbound variable'. As written, every probe reds at once. The failure is loud, so a builder corrects it on the first run. That makes it a spec-text error with no shipped behavioural effect. | sound | - |
