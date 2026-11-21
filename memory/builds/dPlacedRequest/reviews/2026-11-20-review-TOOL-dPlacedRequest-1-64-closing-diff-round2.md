**Serves:** diff-review TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64

# Closing diff review, round 2: the dPlacedRequest Entry build

Node `d` · 2026-11-20 · Tier-2 · on `branch/unattended-dplacedrequest-42a7be`. This was an adversarial fan through `tier2-review.js`: 5 finder lenses, then 4 skeptic batches, then this synthesis. The range is the whole of dPlacedRequest, the Entry build of the dClosedLoop chain: 63 Tier-2 units (TOOL-dPlacedRequest-1 to -64; there is no -22) closing 18 owned gaps across concurrency, orientation and flow. Round 2 runs over the same range as round 1 and looks for what round 1 missed.

**Reviewed range:** `9e21ac760dc0a43d6ed007396922722ccee98d57...95c3103ad4d50a921228af623d34be493f807ff7`. **ROUND 2.**

## Verdict: CLEAN WITH FIXES

No blocker was confirmed. Two HIGH items, three MEDIUM items and three LOW items stand open.

The first HIGH is in the lease fence. A run claim taken in a harness that exposes no session id reads as a foreign live holder to the run's own fence, so every such unattended landing is refused.

The second HIGH is in the lander's test suite. The fenced-landing block (arms 42 to 54) depends on the live fleet roster and the ambient `GOV_NODE`. When its fixture fails, the block skips, and the suite still prints `all cases ok`.

The MEDIUMs are a lander that reads a local re-fence failure as `claim-lost`, a build-card follow that prefers a stale cache ref over a newer unpublished card, and a budget row priced for half the placement suite.

The LOWs are a dead provenance variable, an assertion floor that left out two new rows, and a usage line that omits two exit codes.

Round 1's four confirmed items are not repeated here. Under the closing-review rule, only blockers are folded, so they carry to the exit beside these.

## Review shape

Intensity full, raw 8, confirmed 8, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

- Adjudicated tally by item: 0 BLOCKER, 2 HIGH (H1, H2), 3 MEDIUM (M1, M2, M3), 3 LOW (L1, L2, L3), which is 8 items.
- Adjudicated tally by raw confirmed finding: 0 BLOCKER, 2 HIGH (ids 7, 5), 3 MEDIUM (ids 2, 3, 1), 3 LOW (ids 4, 6, 8), which is 8 findings.
- No findings were merged. Each item holds one confirmed id.
- Ids 3 and 4 sit in the same function, `read_card_stored`. They are two defects: a wrong store precedence, and a variable nothing reads. They stay separate items.
- I re-grade nothing. Every id takes its binding grade.
- No twin was flagged. No refuted finding and no same-address pair was shown.
- The security lens returned zero findings. Every lens returned, so that zero is a real result of this run, not a gap.
- Intent input: 1 spec document was supplied as `specs`, beside the range's commit messages.
- Checklist: 94 items, acquired by the harness from `--for-diff 9e21ac760dc0a43d6ed007396922722ccee98d57..95c3103ad4d50a921228af623d34be493f807ff7`. Each item was assigned to exactly one of 5 lenses: security 19, correctness 19, seams 19, verification 19, intent 18.
- By design: the caller's byDesign, plus 2 invariants from the checklist's by-design block.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified.
- 0 orphaned duplicate refutations were demoted to unverified.
- 0 duplicate refutations were counted as merged confirmations.
- 0 spurious verdicts were discarded.
- 0 duplicates.
- Fixes on confirmed findings: 6 judged sound, 0 judged UNSOUND, 2 judged INSTANCE-ONLY (each cures the cited instance and leaves its class standing), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Shown to synthesis: 0 refuted findings and 0 same-address pairs.
- Dispositions: unclassed is `refuse`, 94 class slugs were handed, and 202 leg names were read from `tools/gate-legs.json`.

Every count above is zero where it should be, so the run is complete.

## HIGH

### H1 — the lease fence never uses the keepalive, so an id-less run's own claim refuses its landing (id 7)

- **Where:** `tools/unattended/unattended.sh@0e8038fd:2845`. Related lines: the column header (:2779-2783), the `lease:*` row (:2926), `write_fence_beat` (:4397-4408), `write_claim` (:3466-3475), and `push-main.sh` `read_fence_line` (:556-558).
- **What is wrong:** Specs 32 S3 and 40, and the stops guide, say a lease is `mine` through a keepalive when a session is absent. That fallback is never built:
  - In `mode = lease`, the `mine` row requires the fleet tag to match and both sessions to be present and equal. It never compares a keepalive.
  - `write_fence_beat` hands the column `sid=${CLAUDE_CODE_SESSION_ID:-absent}` and the fleet tag. It passes no keepalive.
  - The `same` row also needs a present session, so it cannot match either.
- **Consequence:** Take a repo with RUN_CLAIMS on, as this repo's `.unattended.conf` has it, and a harness that exposes no `CLAUDE_CODE_SESSION_ID`.
  1. `--preflight` writes `refs/gov/leases/<slug>/build` with `session: absent` and the run's keepalive.
  2. `push-main.sh --land --slug <slug>` calls `--lease fence build <slug>`.
  3. The run's own claim classes as `foreign-live`, and :2926 sets `CW_CAUSE=live-holder`.
  4. The fence prints `lease refused — live-holder · <slug>/build · …`. The lander reads that as a refusal, exits 1 and pushes nothing.

  Every unattended landing in an id-less harness is refused, and the cause names the run's own lease as a foreign holder. This contradicts spec 32's non-goal, spec 40 S2's exemption of `fence`, and `STOPS.template.md:236`. The fence is new in this range. No arm plants a run claim with `session: absent` and fences it.
- **Fix (judged SOUND by the skeptic):** either build the stated mechanism or change the statement.
  - To build it, give the lease column the record's keepalive. For example, `write_fence_beat` can read the slug's run-state `keepalive` fact and pass it in. Then in `mode = lease`, when either session is absent, read `mine` where `c_node = ka`, and `c_ka` is present on both sides, is not `absent`, and equals the handed keepalive.
  - Probe the build must run: plant a lease with `session: absent` and the run-state keepalive, then run `env -u CLAUDE_CODE_SESSION_ID unattended.sh --lease fence build <slug>`. It must print a `fence — <ref> <tip> <beat>` line. A mismatched keepalive must still be refused.
  - To change the statement instead, amend spec 32's non-goal and STOPS section 7 to say an id-less run cannot land fenced.
- **Left-shift gate:** put the probe above in the `unattended kit gate` leg as a permanent arm, with its mismatched-keepalive twin. As a class rule: an identity fallback a spec states owes an arm that removes the primary identity and asserts the fallback answers.

### H2 — the fenced-landing arms skip on fixture failure, and the suite still reports all cases ok (id 5)

- **Where:** `tools/push-main.test.sh@56c95b47:1849`. The guard is at :1668, and `write_fence_fixture` is at :1639-1658.
- **What is wrong:** The block for arms 42 to 54 runs under `if ... && write_fence_fixture; then`. Its `else` at :1849-1850 prints `skip — 42-53 ...` and does not set `fail`. The suite has no assertion floor, so it still ends `push-main.test: all cases ok`. The fixture depends on state outside itself:
  - It runs the real driver's `--lease acquire build fx` with `USERNAME=daily-agent`, piped into `grep -q '^lease — fx/build · create'`.
  - The driver's `resolve_fleet_tag` (`tools/unattended/lib-unattended.sh@2c2f08b6:207`) calls `render_playbook.py --fleet-tag` with no `--fleet` path. That reads the live `tools/playbook/fleet.toml` (`tools/playbook/render_playbook.py@16bd2ffb:3842`).
  - It passes the ambient `GOV_NODE` through, and the test never unsets it.

  The skip text also says 42-53, but the block runs arm 54.
- **Consequence:** Every arm that tests the fenced landing push silently becomes a pass in three cases:
  1. a regression in the driver's `--lease acquire`, including a change to its `lease — fx/build · create` line;
  2. a fleet roster that no longer names `daily-agent`;
  3. an adopter tree whose `fleet.toml` lacks that user.

  The arms cover fence, re-fence, unreachable versus fenced, unfenced and unparsed. The bar stays green while the lander's CAS fence goes unchecked. Probe: `render_playbook.py --fleet-tag --user nobody` exits 1, so the acquire would fail. On a node that exports `GOV_NODE`, `--fleet-tag --user agent5 --node a` printed `a`. Clone B then carries A's tag, and arm 43's `fleet-tag: b` check reds against the product rather than the fixture.
- **Fix (judged SOUND by the skeptic):**
  - Point the fixture at its own registry instead of the live one. Pass the driver a scratch `fleet.toml` holding rows for `daily-agent` and `agent5`, or set `GOV_NODE` per clone to a planted tag.
  - `unset GOV_NODE` for the block.
  - Make the `else` branch a `bad` whenever `_fn_k` and `_py_arms` both resolved but `write_fence_fixture` failed. Keep the skip only for a lander with no kit beside it.
  - Probe the build must run: rename `daily-agent` in a scratch copy of `fleet.toml` that the fixture reads. Today the suite prints the skip and `all cases ok`. After the fix it must print FAIL.
- **Left-shift gate:** give `push-main.test.sh` a `FLOOR_ASSERTIONS` pin so the `push-main self-test` leg reds when a block's arms stop running. As a class rule, for the `harness arms` leg: a fixture skip is admissible only when the dependency is genuinely absent, never when a fixture step failed.

## MEDIUM

### M1 — the lander reads a local re-fence failure as `claim-lost` (id 2)

- **Where:** `tools/push-main.sh@7a142cb6:334`. `derive_push_failure` is at :323-339, and `read_fence_line` is at :520-563.
- **What is wrong:** After a fenced push fails and the lease tip has moved, `derive_push_failure` runs the re-fence `read_fence_line "$ft"`. Only rc 0 with a fence is `refenced`, and only rc 3 is `unreachable`. Every other return is `fenced`, and the lander prints `end the run with --abort $SLUG --code claim-lost`. But `read_fence_line` also returns 1 for answers that say nothing about the lease:
  - the driver's exit-2 `lease not written` lines from `write_fence_beat` (`unattended.sh` :4387-4428), such as `this node has no row in fleet.toml` (:4397) and `the fence beat could not be built on $tail at $CW_SHA in this clone` (:4426);
  - multi-line or empty driver output, which falls to `fence read unparsed`;
  - the no-python branch (:525-529).

  The :4426 line fires only after the holder has passed the mine, same-epoch and first-parent checks. That is exactly the own-write move that TOOL-dPlacedRequest-29 S2 re-fences.
- **Consequence:** A holder whose lease moved only by its own write is told to abort the run with `claim-lost` whenever the re-fence read hits a local failure. It should have been told to retry. This contradicts the comment at :328-329 and spec 43 S28, which keep `fenced` for a read that answered. S28's outcome table has no row for exit 2. The path is narrow, and the harm is an aborted run.
- **Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):**
  - Make `derive_push_failure` classify the re-fence by what the driver answered, not by `read_fence_line`'s return code alone.
  - Map only an explicit `1:lease refused — <cause>` line, other than offline, to `fenced`.
  - Map every other outcome to `unreachable` or `unchanged`. That includes the unparsed, multi-line and empty reads, every exit-2 `lease not written` line, the no-python branch, and a `check_fence_beat` failure at :548 on a fence line the driver did answer.
  - A separate return code is fine, as long as `check_fence_beat`'s failure gets it too. The callers at :1733 and :1928 use `if ! read_fence_line`, so they still refuse on the new code.
  - Add arms for an exit-2 `lease not written — x` answer and for a bad-beat fence line on the `--after` call. Each asserts that `claim-lost` is not printed.

  The finder proposed a separate return code (for example 4) for the unparsed, `lease not written` and no-python branches, with only an explicit refusal mapped to `fenced`, and one stub-driver arm for the exit-2 case. That cures the cited instance alone and leaves the `check_fence_beat` failure classed as `fenced`.
- **Left-shift gate:** the two arms belong in the `push-main self-test` leg. As a class rule: an outcome classifier owes an arm for each non-answer its reader can return, asserting the non-answer never reaches the terminal verdict.

### M2 — a build-card follow prefers a stale cache ref over a newer unpublished card (id 3)

- **Where:** `skills/session-kickoff/manifest-check.sh@b25206f8:1921`. `read_card_stored` is at :1916-1937, the follow at :1992, the publish at :2004, and `resolve_build_card` at :2143.
- **What is wrong:** `read_card_stored` is the reader behind `write_card_follow`'s default `stored` mode. It never reads `card.store`. Whenever `refs/gov/remote/builds/<slug>/card` resolves, it takes that ref first, before the local-clone cache and the record. It checks neither whether the ref is fresh nor whether `remote-ref` is selected. `read_card_policy` is called only from `write_build_card`, `resolve_build_card`, `write_card_publish` and `write_card_follow`. `resolve_build_card` reads the same three stores filtered by `card.store`, and uses the cache only when its `# card-ref` matches the fetched tip.
- **Consequence:** With the default `card.store`:
  1. A READY publish finds the remote unreachable (:2004 fails, `remote=2`).
  2. `write_card_cache` writes the session's new tail under `# card-ref local`. The cache ref still holds an older card from an earlier lookup.
  3. At the next stage-move follow, `read_card_stored` returns the older ref's tail, with its task, route and READY.
  4. That older tail is re-rendered, published if the remote now answers, and written back over the cache.

  The build card goes back to a stale route, and the newer route is lost. With `card.store` set to `local-clone` or `build-folder` only, a leftover cache ref is still preferred on every follow. Nothing refreshes it, because only `remote-ref` runs a lookup. The effect stays within the orientation card.
- **Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):**
  - Pick the stored tail by freshness, not by a fixed order, over the stores `card.store` selects.
  - When the cache's `# card-ref` is `local` (an unpublished, newer publish) or differs from the ref's commit, the cache wins, whether or not this follow's `read_card_ref` answered.
  - The ref wins only when `remote-ref` is selected and the cache is absent or its card-ref equals the ref's commit.
  - Use the record only when `build-folder` is selected and neither of the others holds a card.
  - Add a fixture plant that publishes offline (`card-ref` unreachable) after an earlier lookup, then follows, and assert the follow's card carries the offline publish's tail. Add a variant where the remote answers again at the follow.

  The finder proposed passing `write_build_card`'s `$stores` into `read_card_stored` and preferring the cache only when the ref read did not answer, with the offline-publish plant. That cures the cited instance alone. It leaves the stale ref winning whenever the remote answers again at the follow.
- **Left-shift gate:** the two plants belong in the `manifest-check self-test` leg. As a class rule: two readers of one store policy must share one selection function, or a fixture must assert they agree.

### M3 — the placement suite's budget row prices fifteen plants; the suite now has 29 (id 1)

- **Where:** `tools/run-gates/selftest-budgets.txt@25b27c00:84`. The suite is `tools/loop/placement.py@a7f26e84`, `PLANTS`.
- **What is wrong:** The `loop placement fixtures` row prices the suite at 63 s, from a 42 s reading of "its fifteen plants" over base 7936d33ed. That row came in with c5744dcbf (TOOL-dPlacedRequest-4). Two later commits added plants and never re-measured it: (PINNED)
  - 0c9164f54 (TOOL-dPlacedRequest-10) added six scenario plants.
  - bd15cd0a4 (TOOL-dPlacedRequest-5) added eight breakpoint plants, several of which run the driver's `--preflight`, `--trigger` or `--request-consent`.

  An ast count of `PLANTS` gives 15 at c5744dcbf, 21 at 0c9164f54 and 29 at bd15cd0a4 through 95c3103ad. The same probe gives probe 18 and claim 13, which match their own rows.
- **Consequence:** The row describes a suite about half the size of the one the leg runs. At the recorded rate, 29 plants take about 81 s before the extra driver-heavy plants are counted. That is past the 63 s cost verdict and closer to the 120 s hang ceiling in `gate-legs.json`. A serial `run-selftests` reading can call the suite over budget, and a loaded node can cut it as a timeout, while the row still claims fifteen plants. (PINNED)
- **Fix (judged SOUND by the skeptic):**
  - Re-measure `python tools/loop/placement.py --fixture` over all 29 plants on the run's node.
  - Set the row to the worst reading x1.5, and rewrite its note to name the current plant count and base.
  - Check that the `gate-legs.json` ceiling of 120 still sits above the new figure.
  - Add a check that compares each loop row's stated plant count with `len(PLANTS)`.
- **Left-shift gate:** the plant-count check belongs in the `every held leg is budgeted, every budget row resolves` leg. That makes the `budget-row-not-remeasured-after-added-arms` checklist class fail mechanically for the loop kit.

## LOW

### L1 — `CARD_STORED_FROM` is set and never read (id 4)

- **Where:** `skills/session-kickoff/manifest-check.sh@b25206f8:1925`. The other assignments are at :1928 and :1931, the globals line at :1815, and the doc comment at :1917-1918.
- **What is wrong:** `read_card_stored` sets `CARD_STORED_FROM` to `ref`, `cache` or `record`, and its doc comment advertises it. Nothing in `skills/` or `tools/` reads it. Nothing read it at the introducing commit 66b4cd4f4, and `git log -G` shows only that commit and dbfe38054, both only setting it.
- **Consequence:** This is dead plumbing with no effect on behaviour. The `card —` lines from `write_build_card` never say which store the follow's tail came from. A reader of the comment will assume the provenance is reported or used, which hides the store-precedence defect in M2.
- **Fix (judged SOUND by the skeptic):** either print it, for example as ` · tail from <ref|cache|record>` on the `write_build_card` success line, or remove the variable, its three assignments and its mention in the comment.
- **Left-shift gate:** a shell-hygiene check for a global assigned in a kit script and read nowhere in the kit would catch this class. It fits beside the existing `shell hygiene` legs.

### L2 — scratch-guard's assertion floor leaves out AC28's two rows (id 6)

- **Where:** `tools/hooks/scratch-guard.test.sh@ff709691:1842`. The AC28 rows are at :1764-1765 and :1771-1772, and the floor comment is at :1797-1841.
- **What is wrong:** TOOL-dPlacedRequest-34 AC28 added two counted rows. One runs on every host. The other runs only on Windows, and other hosts print an uncounted skip at :1774. `FLOOR_ASSERTIONS` was raised only by AC10's 3 rows and AC18's 3 rows, from 390 to 396. (PINNED)
- **Consequence:** The floor is meant to catch arms made unreachable by an early exit. It now has 2 rows of slack on Windows and 1 elsewhere, so the AC28 rows could stop running without the floor going red. The floor comment's hand count also misstates which rows it pins. Behaviour is unchanged. (PINNED)
- **Fix (judged SOUND by the skeptic):** raise `FLOOR_ASSERTIONS` by the AC28 row that runs on every host, to 397. Add a comment line naming TOOL-dPlacedRequest-34 AC28's rows, including the Windows-only one, which the skip on other hosts leaves out of the count.
- **Left-shift gate:** the `testsuite counts (every bar self-test prints one)` leg could compare a suite's printed count on the gate host with its floor, and red when the slack exceeds the suite's declared host-only rows.

### L3 — the `--entry-claim` usage line omits exits 2 and 3 (id 8)

- **Where:** `tools/unattended/unattended.sh@0e8038fd:56`. `run_entry_claim` is at :4849, with its header at :4822-4823.
- **What is wrong:** The usage line lists `0 claimed, 1 refused, 4 waiting, 5 a fresh slug owed`. `run_entry_claim` also returns 2 (not written: no RUN_CLAIMS, no session, no python, unparsed route, lease not written) and 3 (the request's pre-claim budget spent). Its header comment lists 0 to 5.
- **Consequence:** A caller that scripts against `--help` reads exits 2 and 3 as undocumented. Exit 3, budget spent, is the outcome the owner most needs to act on. Behaviour is unaffected.
- **Fix (judged SOUND by the skeptic):** make the usage line list `0 claimed, 1 refused, 2 not written, 3 budget spent, 4 waiting, 5 a fresh slug owed`, matching the function header at :4822.
- **Left-shift gate:** an `unattended kit gate` check that every `return N` reachable from a mode's entry function appears in that mode's usage line would catch this class.

review-shape kind=diff-review round=2 intensity=full at=synth raw=8 confirmed=8 refuted=0 merged=0 unverified=0 blocker=0 high=2 medium=3 low=3 agents=10 out-tokens=116394 trigger=- shape=- efforts=- role-sha=-
review-round round=2 limit=- prior=2 count=2 state=NON-CONVERGENT

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/run-gates/selftest-budgets.txt:84 | medium | medium | confirmed | I checked the row and the plant count at each commit. The `loop placement fixtures` row was added at bd6a6005b (60 s, fourteen plants). c5744dcbf re-priced it to 63 s with the text 'its fifteen plants ... over base 7936d33ed'. After that the row did not change at 0c9164f54, bd15cd0a4 or 95c3103ad. An ast count of the PLANTS dict in tools/loop/placement.py gives 15 at c5744dcbf and 09a53ab5a, 21 at 0c9164f54 and de35faa4c, and 29 at bd15cd0a4, 63b9ab7aa, c6de76920 and 95c3103ad. placement.py does not exist at base 9e21ac760, so the whole suite and its row are in range. gate-legs.json runs `python {prefix}/loop/placement.py --fixture` with ceiling 120. The row therefore prices a suite about half the size of the one the leg runs. Its cost verdict misleads, and a loaded node can be cut nearer the ceiling. The effect stays inside the budget reading, so this is medium. | sound | budget-row-not-remeasured-after-added-arms | class:budget-row-not-remeasured-after-added-arms (PINNED) |
| 2 | correctness | tools/push-main.sh@7a142cb6:334 | medium | medium | confirmed | push-main.sh@95c3103ad:323-339: once the lease tip has moved, derive_push_failure calls read_fence_line "$ft". Only rc 0 with a fence is `refenced` and only rc 3 is `unreachable`; every other return is `fenced`, with '--abort $SLUG --code claim-lost'. read_fence_line (:520-563) matches only '0:fence — …', '1:lease refused — offline · …' and '1:lease refused — …'. Anything else, including multi-line or empty output, prints 'fence read unparsed' and returns 1. The no-python branch (:525-529) also returns 1. write_fence_beat in unattended.sh@95c3103ad:4387-4428 has exit-2 'lease not written' lines on the --after path. One is 'this node has no row in fleet.toml' (:4397). Another is 'the fence beat could not be built on $tail at $CW_SHA in this clone' (:4426). The second fires only after the holder has passed the mine, same-epoch and first-parent checks, which is exactly the own-write move S2 re-fences. So a local failure is reported as a lease taken by another holder. That contradicts the comment at :328-329 and spec 43 S28's 'keeping fenced for a read that answered'. S28's outcome table has no row for exit 2. read_fence_line is new in the range (absent at base), so this is in scope. The path is narrow and the harm is an aborted run rather than a retry, so this is medium. | instance | - | new:non-answer-classed-as-a-refusal |
| 3 | seams | skills/session-kickoff/manifest-check.sh@b25206f8:1921 | medium | medium | confirmed | read_card_stored is new in this diff: the base copy of manifest-check.sh has 0 occurrences. At 95c3103ad (:1919-1937) it takes refs/gov/remote/builds/<slug>/card whenever `git rev-parse --verify` resolves it, then the cache, then the record. It never reads card.store; read_card_policy is called only at :1980, :2103, :2113, :2118 and :2145. resolve_build_card (:2143) does filter by card.store and uses the cache only when its `# card-ref` matches the fetched tip. The scenario holds when traced through write_build_card. A READY publish with the remote unreachable sets remote=2, so oid stays `local` and write_card_cache writes the new tail under `# card-ref local`. The next follow in mode=stored (:1992) reads the stale local ref first and re-renders the older tail. It publishes that tail if remote-ref is now reachable, and writes it back over the cache, so the newer route is lost. Spec 2 S4 says only 'the stored build card's tail', which does not sanction preferring a stale ref over a newer unpublished cache. The effect stays within the orientation card (a stale route and task get republished). It is not a security hole or a gate, so the grade is medium. | instance | - | class:two-answers-to-one-question |
| 4 | seams | skills/session-kickoff/manifest-check.sh@b25206f8:1925 | low | low | confirmed | grep across skills/ and tools/ finds CARD_STORED_FROM only where it is set: the globals line :1815, the three assignments in read_card_stored at :1925, :1928 and :1931, and the doc comment at :1918. Nothing reads it, and write_build_card's `card —` lines do not print it. The variable is new in this diff (read_card_stored is absent at the base). It is dead plumbing with no effect on behaviour. | sound | - | new:global-set-and-never-read |
| 5 | verification | tools/push-main.test.sh@56c95b47:1849 | high | high | confirmed | The diff adds the whole block; the base push-main.test.sh has no 'fence' text at all. At 95c3103ad, write_fence_fixture ends with the real driver's `--lease acquire build fx` piped into `grep -q '^lease — fx/build · create'`. That driver runs through a wrapper that execs $HERE/unattended/unattended.sh. Its resolve_fleet_tag (tools/unattended/lib-unattended.sh@2c2f08b6:207) calls render_playbook.py --fleet-tag with no --fleet path, so render_playbook reads the fleet.toml beside the live kit (tools/playbook/render_playbook.py@16bd2ffb:3842). The take succeeds today only because the live tools/playbook/fleet.toml names daily-agent (tag a) and agent5 (tag b). It also passes GOV_NODE through, and the test never unsets it. If the acquire fails, the `else` at :1849 only echoes `skip — 42-53 ...` and leaves fail unchanged. The file has no FLOOR_ASSERTIONS, so it still ends `push-main.test: all cases ok`. A broken acquire, a changed create line or a roster without daily-agent therefore silently turns arms 42-54 into a pass. The skip text also says 42-53 while the block runs 54. All three conditions are narrow but real, so this is high. | sound | fixture-inherits-ambient-machine-state | class:fixture-inherits-ambient-machine-state |
| 6 | verification | tools/hooks/scratch-guard.test.sh@ff709691:1842 | low | low | confirmed | At 95c3103ad, the AC28 block of scratch-guard.test.sh adds counted rows: one at :1764-1765 on every host, and one at :1771-1772 that runs only on Windows (other hosts print an uncounted skip at :1774). The floor comment at :1797-1841 adds only AC10's 3 rows (393) and AC18's 3 rows (396), and FLOOR_ASSERTIONS=396 at :1842. The AC28 rows are not in the arithmetic. The floor is a minimum, so the only effect is slack: the AC28 rows could become unreachable without the pin going red. The cost is weaker coverage and a hand count that is off, with no behaviour change, so this is low. | sound | fail-count-reads-a-pattern-the-row-never-prints | new:assertion-floor-not-raised-after-added-rows (PINNED) |
| 7 | intent | tools/unattended/unattended.sh@0e8038fd:2845 | high | high | confirmed | In unattended.sh at HEAD, the lease-mode `mine` row (:2845) requires `[ -n "$sid" ] && [ "$sid" != absent ]` and never compares a keepalive. The header at :2779-2783 itself says the column 'is handed none'. write_fence_beat (:4397-4399) passes `sid=${CLAUDE_CODE_SESSION_ID:-absent}` and the fleet tag, and no keepalive. write_claim (:3466-3475) writes the run claim to the same `derive_lease_ref build <slug>` ref that the fence reads, and records `session: absent` when the run-state session is absent. The `same` row also needs a present `me`. So in an id-less harness the run's own claim classes as `foreign-<verdict>`, and :2926 `lease:*` sets live-holder. write_fence_beat then prints `lease refused — live-holder`, and push-main read_fence_line (:556-558) turns that into exit 1, nothing pushed. Spec 40 S2 exempts `fence` from the no-session refusal and says the run claim's keepalive identity is unchanged. Spec 32's non-goal and STOPS.template.md:236 say a run claim is `mine` through its keepalive. The fence column contradicts both, so the run-claim exemption is not honoured at landing. The fence is new in this range: the base has only the run-column `mine` rows. The path is narrow (RUN_CLAIMS on, in a harness that exposes no session id), so this is high. | sound | - | new:stated-identity-fallback-never-built |
| 8 | intent | tools/unattended/unattended.sh@0e8038fd:56 | low | low | confirmed | The usage line at tools/unattended/unattended.sh@0e8038fd:56 lists '0 claimed, 1 refused, 4 waiting, 5 a fresh slug owed'. run_entry_claim's body returns 2 at many sites (no RUN_CLAIMS, no session, no python, unparsed route, lease not written). It returns 3 at the budget-spent branch (`claim refused — ... the request's pre-claim budget is spent; return 3`). Its header comment (:4822-4823) lists 0-5. Only the help text is affected; behaviour is not. | sound | - | new:usage-exit-list-lags-its-function |
