**Serves:** spec-audit TOOL-dPlacedRequest-27@rev-1 TOOL-dPlacedRequest-23@rev-1 TOOL-dPlacedRequest-24@rev-2 TOOL-dPlacedRequest-25@rev-1 TOOL-dPlacedRequest-26@rev-1 TOOL-dPlacedRequest-28@rev-1 TOOL-dPlacedRequest-29@rev-1 TOOL-dPlacedRequest-30@rev-2 TOOL-dPlacedRequest-31@rev-2 TOOL-dPlacedRequest-32@rev-2 TOOL-dPlacedRequest-33@rev-2 TOOL-dPlacedRequest-34@rev-2

# Tier-2 spec audit — build dPlacedRequest, the 12 round-1 promotion specs TOOL-dPlacedRequest-23 to -34, ROUND 1

*Adversarial pre-code pass over the twelve specs the round-1 spec audit promoted, 2026-10-25. Five lenses
found; five skeptic batches tried to refute each finding; this report is synthesised only from the
findings that survived. Finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis
gov-synthesizer.*

Reviewed: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-27.md@e7afb9595b559acb877bdc31a8c377c8ea34057f, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-23.md@b8adeec7944681f9ed08a64e74d145f9c60759d6, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md@0ad66829a0759328fbf6129169c288fbff4beab2, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-25.md@e8850dd95cec21df5a6501a6193cb42f324afd9c, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-26.md@2305eecc1e456210eaf87efef0f850ea0e9ed285, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md@ec6b05c6a44757bcb871c55072c5eca0bcf96d2e, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-29.md@1cf94caee57628febd271e6128e53cb453ce651a, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-30.md@bbab7ab3551da52452a240ae24f456fb964bd258, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md@83cc38ae0736b7f3180b43a5fb293cb70045dcae, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md@3a520d2e425b4ceb4ce8bd65f937e6794957bd5b, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md@0e8ffd149b61d96b1427829030a67c82368ecd0d, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md@297799719025b21d5bc83c42a1d764e80a72718b

ROUND 1

## Verdict: CLEAN WITH FIXES

No finding stands at BLOCKER. Eight confirmed findings stand at HIGH, and every one must be folded into its spec before the build runs. By item: 0 BLOCKER, 5 HIGH, 22 MEDIUM, 9 LOW, 36 items in all. By raw confirmed finding: 0 BLOCKER, 8 HIGH, 24 MEDIUM, 10 LOW, 42 in all. Three defects appear twice because their findings carry different binding grades: the plain `git hash-object` binding (M7 at MEDIUM, L8 at LOW), the keepalive identity rule (M8 at MEDIUM, L7 at LOW) and the card publish's kill outcome (M9 at MEDIUM, L9 at LOW). Each is fixed once, by the MEDIUM item's fix. H5 and M4 touch the same AC5 of TOOL-dPlacedRequest-28; H5's behavioural arm replaces it.

Review shape: intensity full, raw 43, confirmed 42, refuted 1, unverified 0 (0 uncertain), precision 0.98.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 12 | 12 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 9 | 8 | 1 | 0 | 0 | 0.89 |
| reuse | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 12 | 12 | 0 | 0 | 0 | 1.00 |

**Run integrity.**
- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdict hygiene: 0 contradictory verdicts and 0 orphaned duplicate refutations demoted to unverified; 0 spurious verdicts discarded; 0 duplicates.
- Fixes on confirmed findings: 41 judged sound, 1 judged UNSOUND, 0 none proposed, 0 not judged. The UNSOUND fix (id 33) is replaced below by the skeptic's corrected fix; the rejected proposal is never written as the fix.
- Severity: 0 ungraded by the skeptic; 3 re-graded by the skeptic (25 high to medium, 35 high to medium, 40 medium to low). The synthesis keeps every binding grade.
- Unverified: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: 22 spec documents supplied as `specs`, as sibling context.
- Checklist: 52 items, each assigned to exactly one lens (coherence 11, grounding 11, reuse 10, blast-radius 10, failure-envelope 10).
- By design: 1 invariant from the checklist's by-design block.
- Move check: no checked subject moved.

Refuted and not reported: id 14 (the queue lock's retry already carries a stated 5 s wall-clock bound, and AC3 observes it).

---

## HIGH

### H1 — The node-lock factory is not self-contained in the `gov_feed_sh` block (ids 2, 13, 24, 32)

- **Where:** TOOL-dPlacedRequest-24 §2 S1, §4 Evidence and Files touched, §6 AC6.
- **What is wrong:** S1 builds `write_node_lock` and its siblings from `write_claim_push_lock`'s bodies, renamed, and places them in the byte-identical `gov_feed_sh` block. Those bodies (unattended.sh:2331-2354 at c63aabbb) read `REMOTE_BOUND` and `$ROOT` and call `add_health_event` and `resolve_health_log`. Two carriers of the block, `tools/run-gates/post-merge.sh` (TOOL-13) and `tools/push-main.sh` (TOOL-15), define none of these names and run under `set -u` (post-merge.sh:26, push-main.sh:64). Files touched also omits push-main.sh.
- **Consequence:** the first lock take in a carrier evaluates `$(( $EPOCHSECONDS + REMOTE_BOUND + 10 ))` and aborts with `REMOTE_BOUND: unbound variable`, rc 127 (re-probed). post-merge.sh dies at its bar-red marker write; the lander dies after its push has landed. The stale-break path also expands an unbound `$ROOT` and calls undefined functions, losing the `node-lock-broken` event. AC6 only `cmp`s the copies and AC5 runs the factory inside the driver, so the gates stay green.
- **Fix (judged sound for all four findings):** state in S1 the factory's environment contract. The `until` deadline comes from an argument or a block-local default (for example `${NODE_LOCK_BOUND:-70}`), never `REMOTE_BOUND`. The health event goes through a function the block itself carries, or through `health_log_sh` carried beside it in every carrier, or is guarded with `command -v add_health_event`; it uses the common dir the block already resolves, never `$ROOT`; the component label is passed in, not hardcoded as `unattended`. Add tools/push-main.sh to Files touched and to AC6's `cmp`. Add an AC that sources each carrier's cut (post-merge.sh and push-main.sh) into `bash -c 'set -u; …'` with no driver globals, takes a fresh lock and breaks a planted stale `gov-feed.lock`, and exits 0 with no lock left held. The staged break is the verbatim claim-push body.
- **Gate:** a parity-leg arm that sources every inline `gov_feed_sh` copy under `set -u` with an empty environment and exercises its lock functions, beside the existing byte `cmp`.

### H2 — The bounded walk's early-stale rule can fire before the tenure stop (id 1)

- **Where:** TOOL-dPlacedRequest-34 §2 S43 and §4 "The bounded walk (S43)", read with TOOL-dPlacedRequest-26 S1 and AC1.
- **What is wrong:** S43 and §4 list three walk stops (the renewing beat, the tenure's start, the first commit sighted more than `leases.expiry-hours` ago) without ordering them, and §4 says the old commit "makes the verdict stale whatever lies further back". TOOL-26 stops at the first commit whose epoch differs from the tip's.
- **Consequence:** in TOOL-26 AC1's chain (epoch-2 take-over sighted a minute ago over an epoch-1 commit sighted 25 h ago) a build that checks the threshold first reads the fresh take-over `stale` at once, reopening the defect TOOL-26 closes. TOOL-34 lands at order 22, long after TOOL-26 at order 5, and AC43 only times the walk.
- **Fix (judged sound):** state the order in S43 and the §4 pseudo-code: a commit whose epoch differs from the tip's ends the tenure first, and age is taken from the tenure's start. The threshold applies only to commits inside the tip's tenure; reword "whatever lies further back" to "within the tenure". Add a criterion that re-runs TOOL-26 AC1's chain under the bounded walk and expects `live`.
- **Gate:** a lease-fixture arm re-run at every later unit touching the walk: the TOOL-26 AC1 chain must read `live`.

### H3 — The identity refusal blocks every `--lease` act, including node and maintenance acts (id 26)

- **Where:** TOOL-dPlacedRequest-32 §2 S4.
- **What is wrong:** S4 refuses every `--lease <act>` with exit 2 when there is no session and no keepalive, exempting only the driver's run claim. Acts that need no holder identity fall under it: `--lease prune` (run by dWellOiledMachine's supervisor, TOOL-16), `--lease flush` (TOOL-1), `--lease fence` on its `fence — none` path (TOOL-15 S2) and TOOL-34 S22's read-only `--lease status`.
- **Consequence:** a headless supervisor's prune always exits 2, so run tombstones are never pruned; a sessionless flush never drains the queue; the lander's fence from a terminal or CI gets exit 2 where TOOL-15 promises exit 0. AC3 tests only `acquire`.
- **Fix (judged sound):** have S4 name the holder acts it gates (acquire, take-over, renew, release, offer) and exempt prune, flush, status and fence; state that the `RUN_CLAIMS`-off answer comes before the identity check (see M22). Add a criterion running `env -u CLAUDE_CODE_SESSION_ID unattended.sh --lease prune`, `--lease flush` and `--lease fence build tFix` (switch off), each exiting 0, staged red against the blanket refusal. Add hands-off edges to TOOL-16, -15, -34 and the external dWellOiledMachine consumer.
- **Gate:** a checklist entry, "a new guard on a verb names every act it reaches and every act it exempts".

### H4 — The queue's append-once key drops a different offline write to the same lease (id 33)

- **Where:** TOOL-dPlacedRequest-24 §2 S3 and §4 "Alternatives rejected" (the dedupe key).
- **What is wrong:** S3 drops any write whose (ref, cached tip) matches a queued line, printing `queued — already`. Offline, TOOL-1 S10 builds every write on the cached tip and moves no ref, so an acquire followed by a release, renew or take-over of the same ref share one key.
- **Consequence:** an offline release after an offline acquire is silently discarded while the user is told it was queued. The flush lands the acquire, and the remote shows a lease the node believes it released, held until expiry or for ever under `leases.renewal none`.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** a second offline write to a ref that already has a queued line builds on that line's queued commit, records that commit as its tip, and is appended, so the flush pushes the chain in order. Keep the (ref, cached tip) dedupe only for a write whose record body, less its stamps, equals the queued one. AC: an offline acquire then an offline release queues two chained lines, and after `--lease flush` the remote record reads released.
- **Gate:** a queue-fixture arm that runs each pair of distinct offline acts on one ref and asserts the flushed remote ends in the last act's state.

### H5 — The tombstone check misses the offline create, and AC5 checks a spelling (id 36)

- **Where:** TOOL-dPlacedRequest-28 §2 S2 (the list of creates) and §6 AC5.
- **What is wrong:** S2 requires `read_feed_lease_tip` only for writes "whose read finds the ref absent on the remote". TOOL-1 S10's offline branch never reads the remote and builds on the cached tip; when that tip is empty it queues a parentless epoch-1 create without consulting the feed. AC5 matches only the literal `build_gov_commit ""`, so a create passed `"$tip"` escapes it.
- **Consequence:** after a tombstone is deleted outside the kit and a pruning fetch drops its cache ref, an offline `--lease acquire` queues a create whose compare-and-swap on the absent ref lands at flush, bringing the closed build back as held at epoch 1.
- **Fix (judged sound):** state the class in S2: every lease commit built on an empty parent, whether the remote answered absent or the offline branch found no cached tip, calls `read_feed_lease_tip` first (the feed is node-local and readable offline). Replace AC5's spelling grep with a behavioural arm: an offline acquire over a sighted, deleted tombstone exits 1 printing `tombstone`, and `gov-queue.log` gains nothing.
- **Gate:** a checklist entry, "a class check observes behaviour, never one spelling of a call".

---

## MEDIUM

### M1 — TOOL-23 AC3 cannot see a strict caller that reaches the queue through the writer (ids 3, 37)

- **Where:** TOOL-dPlacedRequest-23 §6 AC3, observing §2 S1.
- **What is wrong:** AC3 flags only a function body spelling both `read_claims strict` and `add_gov_queue`. §4 puts the queue call in the lease writer's offline branch, which strict callers (`run_takeover`, `verb_close` and the others at :2202, :7477, :9037, :10839) reach through `check_claim_writable` and the writer. AC1 and AC2 run only `--preflight`.
- **Consequence:** AC3 is green whatever the call graph, so the take-over and `--close` guarantee has no observation; a writer that queues after a failed strict read passes.
- **Fix (judged sound for both findings):** replace AC3 with behavioural arms: over AC1's renamed-away origin under planted `warn`, a take-over and a `--close` each exit non-zero printing `check 109` with `gov-queue.log` unchanged; or a sourced-driver probe with a logging `add_gov_queue` stub that is never invoked for any strict caller after a failed strict read. The planted break is a scratch copy whose writer queues whenever the read failed.
- **Gate:** the same checklist entry as H5, "a class check observes behaviour, never one spelling of a call".

### M2 — TOOL-28 AC5's literal `build_gov_commit ""` matches no create the sibling specs spell (ids 4, 19)

- **Where:** TOOL-dPlacedRequest-28 §6 AC5, observing §2 S4.
- **What is wrong:** every lease writer passes a variable tip (TOOL-20:34 `build_gov_commit <tip read>`, TOOL-11:45 `build_gov_commit "$CW_SHA"`), empty on a create. AC5 greps only the literal `""`.
- **Consequence:** a second parentless create such as the planted `write_lease_offer` case passes, and a correct build lists no function, contradicting AC5's own expectation. The "one create path" check certifies nothing; AC1 to AC3 still exercise the offer by behaviour.
- **Fix (judged sound for both findings):** observe S4 behaviourally: over a planted feed naming the ref, every create path (acquire, take-over, run claim, offer) yields a commit with a parent (`git rev-list --parents -n1`), or with `read_feed_lease_tip` stubbed to print `tombstone`, each refuses. Alternatively list every body that calls `build_gov_commit` and spells `refs/gov/leases` or `derive_lease_ref` but not `read_feed_lease_tip`. H5's offline arm is added beside it.
- **Gate:** as H5.

### M3 — TOOL-33 AC5 fails on a correct build (id 5)

- **Where:** TOOL-dPlacedRequest-33 §6 AC5.
- **What is wrong:** AC5 requires a logging `git` stub on PATH to log no call, but the driver runs `GIT rev-parse --show-toplevel` unconditionally at startup (unattended.sh:546) before reading the conf or dispatching a verb.
- **Consequence:** a correct `--card-ref write` that tests `RUN_CLAIMS` first still reds AC5, so the builder must rewrite the criterion ad hoc.
- **Fix (judged sound):** have the stub log only remote-touching subcommands (`fetch`, `ls-remote`, `push`) and require none logged, or assert no call after the startup `rev-parse`.
- **Gate:** a checklist entry, "a staged criterion is run green against a correct build before it is written down".

### M4 — `leases.offline: follow-leases` has two outcomes for `--entry-claim` (id 6)

- **Where:** TOOL-dPlacedRequest-34 §2 S14 and §4 "The claim offline (S14, S15)", against TOOL-dPlacedRequest-3's outcome table.
- **What is wrong:** S14 routes `follow-leases` to exit 4 / `awaiting` and amends only TOOL-3's awaiting row; TOOL-3's `refused` row still lists `offline under refuse or follow-leases`. AC14 tests only the default and `refuse`.
- **Consequence:** a placer reading TOOL-3 files an ask and treats the slug as refused while the verb exited 4 for a wait.
- **Fix (judged sound):** have S14 also strike `follow-leases` from TOOL-3's `refused` row (or route it to `refused` consistently), and add a `follow-leases` arm to AC14 with its exit code and outcome.
- **Gate:** a checklist entry, "an amendment to another spec's table edits every row the changed value appears in".

### M5 — S40's empty-tip encoding is ordered after the criteria that depend on it (id 7)

- **Where:** TOOL-dPlacedRequest-34 §2 S40 and §6 AC40, against TOOL-dPlacedRequest-1 AC7 and TOOL-dPlacedRequest-24 AC1/AC2.
- **What is wrong:** AC40 repeats TOOL-1 AC7's flush clause word for word. TOOL-1 (order 3) and TOOL-24 (order 4) already queue and flush a create of tOff; TOOL-24:72-73 defers the `-` placeholder to TOOL-34 (order 22).
- **Consequence:** either units 1 and 24 cannot pass their own criteria, including TOOL-24's dedupe keyed on the cached-tip field, or AC40 is green before TOOL-34 is built and can never red.
- **Fix (judged sound):** move the empty-tip encoding into TOOL-24, which owns the queue line's format and dedupe key, at order 4; otherwise give AC40 an observation that is red on TOOL-1's queue as built, such as a queue line read back field by field with an empty tip.
- **Gate:** a build-order check, "every criterion is red at its own unit's base", recorded in the project bug-class checklist.

### M6 — TOOL-23 closes the `leases.offline` population without `--entry-claim` (id 8)

- **Where:** TOOL-dPlacedRequest-23 §2 S2 and S3.
- **What is wrong:** S2 declares the key's one population as `run_lease_verb` plus soft and quiet `read_claims` callers that write a lease, and S3 writes that into the stops guide. TOOL-21 S2/S5 hands `--entry-claim`'s unanswered write to `leases.offline`, and TOOL-34 S14 reads its `refuse` value.
- **Consequence:** the stops guide states a closed population that omits a real reader, so the next change to the key misses `--entry-claim`.
- **Fix (judged sound):** add `--entry-claim` (TOOL-21's claim-ref write, with TOOL-34 S14's outcome) to S2's population and S3's guide sentence, or phrase it as "every non-strict reader, `--entry-claim` included".
- **Gate:** a checklist entry, "a closed population of a config key is checked by `git grep` of the key over the spec set".

### M7 — Consent is bound to filtered content, not the submitted bytes (id 15; same defect as L8)

- **Where:** TOOL-dPlacedRequest-31 §2 S1-S2, §4 "The line and the read", §10.
- **What is wrong:** plain `git hash-object <file>` runs the clean filter; under this clone's `core.autocrlf=true` and `* text=auto` a CRLF file and its LF twin hash alike (probed). TOOL-30 compares the same store with byte-exact `cmp -s`.
- **Consequence:** the "these exact bytes" guarantee does not hold; units 30 and 31 disagree on a CR-only re-submission (30 refuses it as a collision, 31 grants consent across it); the blob also depends on per-node git config.
- **Fix (judged sound):** use `git hash-object --no-filters <file>` in both the `.typed` append and `check_request_consent`. Add an AC: a CRLF copy of a.md planted as the stored copy makes consent return 1.
- **Gate:** a grep criterion in the consent leg: no `git hash-object` without `--no-filters` in the request paths.

### M8 — The id-less identity path misstates today's rule and widens `mine` (id 16; same defect as L7)

- **Where:** TOOL-dPlacedRequest-32 §2 S3, §4 "The identity rule" and Evidence.
- **What is wrong:** the spec calls the keepalive path "today's keepalive comparison", but unattended.sh:2260 requires keepalive AND session equal, with :2261-2263's prior-session and take-over rows. §4's pseudo-code also drops S3's "either session absent" condition.
- **Consequence:** built from §4, a record whose session differs but whose keepalive matches reads `mine`, including a resumed run's prior session in `take-over` mode, which today reads `same`. AC5's "as today" does not observe it.
- **Fix (judged sound):** restate the rule against the code: `mine = (both sessions present, equal, tags equal) or (either session none and both keepalives present and equal)`, keeping :2261-2263's rows unchanged. Add an AC: two present, differing sessions with equal keepalives in take-over mode read `same`.
- **Gate:** a checklist entry, "a spec claiming 'as today' quotes the base line it preserves".

### M9 — The card publish runs a writer under a reader's kill bound (id 17; same defect as L9)

- **Where:** TOOL-dPlacedRequest-33 §2 S2, §4 "The publish, end to end", §5 risks.
- **What is wrong:** `--card-ref write`, a compare-and-swap writer, runs under `timeout -k 2 "$CARD_FETCH_BOUND"`, a bound copied from the read-only claims cell. `CARD_FETCH_BOUND` has no value anywhere, against the driver's 60 s `REMOTE_BOUND` per remote call.
- **Consequence:** a kill after the push lands prints `remote-ref not written`, a false outcome, and the feed misses the event; a kill inside `add_feed_event` leaves a `gov-feed.lock` held about 70 s, so other governance writes on the node skip their feed line.
- **Fix (judged sound):** declare `CARD_FETCH_BOUND`'s value and require it to exceed the verb's own worst case (2 x `REMOTE_BOUND` + 10), or pass the bound into the driver so it bounds its own remote calls and is never killed mid-write. Word the kill line "outcome unknown", not "not written". Add a fixture plant whose stub driver writes then sleeps past the bound, and check the card line does not claim the ref absent.
- **Gate:** a checklist entry, "a `timeout` around a writer states what a kill after the write reports".

### M10 — `readCard`'s cited spawn bound does not exist (id 18)

- **Where:** TOOL-dPlacedRequest-34 §4 "`readCard`'s cost (S28)" and §2 S28.
- **What is wrong:** §4 says the new bash call is "bounded by the hook's existing spawn bound"; scratch-guard.js's only `spawnSync` (:710) passes no `timeout`.
- **Consequence:** a builder adds no timeout; a hung checker blocks every guarded Edit or Write until the harness kills the hook, and S28's "a checker that does not answer reads as no card" has no mechanism.
- **Fix (judged sound):** specify `spawnSync(bash, args, { timeout: <ms>, killSignal: 'SIGKILL' })` with the value stated. Add to AC28 a stub checker that sleeps past the bound and must read as no card, named, within bound plus 1 s.
- **Gate:** a hooks-leg grep: every `spawnSync` in tools/hooks/ passes a `timeout`.

### M11 — The bounded driver call is copied a third and fourth time instead of extracted (id 22)

- **Where:** TOOL-dPlacedRequest-33 §2 S2 and §10; TOOL-dPlacedRequest-34 §2 S11.
- **What is wrong:** manifest-check.sh already holds the bounded driver call twice (`derive_overlaps_line` :555-564, `derive_claims_line` :647-655). TOOL-33 copies it for the publish and TOOL-34 S11 for the lookup, against the charter's [reuse] rule (extract at the second instance).
- **Consequence:** four copies of the conf check, kit resolve, `timeout -k 1 5 true` probe, scratch capture, `GOV_RUNLOG=0 timeout -k 2` call and 124/kill reading; a fix to one step drifts across the others.
- **Fix (judged sound):** extract one helper in manifest-check.sh, for example `run_driver_bounded <cell> <bound> <verb args…>`, that prints its skip reason or leaves output in a scratch file and returns the verb's rc; route both existing cells and both new calls through it. Add a criterion: `grep -c 'timeout -k 1 5 true' skills/session-kickoff/manifest-check.sh` prints 1. Name `derive_overlaps_line` in §10 as the kind's other instance.
- **Gate:** the grep count above as a standing kickoff-leg assertion.

### M12 — S30's reason for keeping three node-tag resolvers is false (id 23)

- **Where:** TOOL-dPlacedRequest-34 §2 S30 and §4 Evidence on `derive_node_tag` / `resolve_node_tag`.
- **What is wrong:** S30 says those resolvers read "a different registry", the governance file's `## Node registry` table. That table is rendered from tools/playbook/fleet.toml by render_playbook.py's `derive_node_table` (:424-430), as TOOL-aDistilledCharter-2 decided, so it is the same registry.
- **Consequence:** three match rules (exact case-folded, substring, Machine/user cell) answer one question; the lease's `fleet-tag` can disagree with the card's and the sweep's tag, and the sentence tells the next reader the split is deliberate.
- **Fix (judged sound):** rewrite S30. Either re-point both resolvers at one user-keyed lookup (`read_fleet` by user, case-folded, honouring `GOV_NODE`), or state the adopter-without-fleet.toml case that requires the table, cite `derive_node_table` as its source, and add a parity criterion: for every fleet.toml row the three resolvers give the same tag.
- **Gate:** the parity criterion above, kept as a standing fleet-leg arm.

### M13 — S40's `-` spelling strands TOOL-24's dedupe reader (id 25)

- **Where:** TOOL-dPlacedRequest-34 §2 S40, with TOOL-dPlacedRequest-24 S3.
- **What is wrong:** S40 changes the queue line's empty cached tip to `-` and names only the flush as a mapping-back reader. TOOL-24 S3's append-once test compares the stored tip with the new one, still empty on a create.
- **Consequence:** if the normalisation is applied on one side only, an offline create compares `''` with `-`, re-queues on a re-run and the flush yields spuriously, reopening the duplicate-queue defect TOOL-24 closes; TOOL-24 AC1 reds.
- **Fix (judged sound):** add a **Readers:** clause to S40 naming `add_gov_queue`'s dedupe and `write_gov_queue`'s resolved-line rewrite; normalise the tip once in a helper both append and dedupe call. Extend AC40: an offline acquire of an absent ref twice leaves `grep -c '' gov-queue.log` at 1, staged red against a raw-empty compare. (M5 moves the encoding into TOOL-24, which also places this reader inside its owner.)
- **Note on grade:** the skeptic re-graded this from high to medium: it depends on where the builder places the normalisation, and TOOL-24 AC1 would show it if run.
- **Gate:** a checklist entry, "a spelling change carries a Readers clause listing every reader found by `git grep`".

### M14 — S35's 8 extra bytes push the protocol over its size ceiling (id 27)

- **Where:** TOOL-dPlacedRequest-34 §2 S35 and S37, §6 AC37.
- **What is wrong:** S35 rewrites PROTOCOL.template.md:521 from `refs/gov/runs/<slug>` to `refs/gov/leases/<slug>/build`, 8 bytes longer. The rendered memory/guides/UNATTENDED-PROTOCOL.md is 66859 bytes against a 66860 ceiling (template-size-limits.txt:143). S37 budgets only TOOL-5's sentence.
- **Consequence:** the protocol renders at about 66867 bytes; AC37 and the `unattended protocol size` leg go red, and the builder trims unnamed text or raises the ceiling unrecorded.
- **Fix (judged sound):** have S37 budget S35's 8 bytes too: name a trim of at least that size, or move the `RUN_CLAIMS` row's ref spelling into the stops guide behind the existing `UNATTENDED-STOPS.md` §7 pointer. Restate in §4 the measured headroom after both edits.
- **Gate:** a checklist entry, "every edit to a file within 1 KiB of its ceiling is byte-budgeted in the spec".

### M15 — The TOOL-34 spec itself is over the live-spec ceiling (id 28)

- **Where:** memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md, whole file (the `gen:spec-records` region, lines 7-15).
- **What is wrong:** the file is 50111 bytes against the 49152 `memory/builds/*/spec/` ceiling, with no high-water row. The promoted fix cut it to 49043; the regenerated spec-records table added 1067 bytes.
- **Consequence:** the `spec tokens` size join reds at the bar; every further record bound to the unit grows the table again, so 109 bytes of headroom cannot hold.
- **Fix (judged sound):** cut the spec at least 1067 bytes plus margin under 49152, for example by moving §2's per-finding brackets or §4 "Measured sizes" into a research record, or split the batch into two specs by write set; measure after the records render.
- **Gate:** the existing size leg already catches it; run it after the records render, not before.

### M16 — TOOL-31's new `.typed` grammar strands two readers of the old spelling (id 29)

- **Where:** TOOL-dPlacedRequest-31 §2 S1 and §3 Edges.
- **What is wrong:** S1 changes the line from `<session>` to `<session><TAB><blob>` and S2 reads any other shape as no consent. TOOL-5 AC3's `relayed` plant (built at order 19, after this unit at 11) and TOOL-19 §4's table ("one session id per line") still use the old spelling; the spec has no hands-off edge to TOOL-5 and no Readers clause.
- **Consequence:** a plant writing the bare session reds TOOL-5 AC3's passing half, or tempts the builder to loosen the predicate back to session-only.
- **Fix (judged sound):** add a hands-off edge to TOOL-5 naming the new grammar; add a **Readers:** clause to S1 naming TOOL-5 AC3's plant and TOOL-19 §4's table; state the plant writes `<session>\t<git hash-object of requests/<key>.md>`.
- **Gate:** as M13.

### M17 — AC59's version-bump oracle diffs from a historical sha (id 30)

- **Where:** TOOL-dPlacedRequest-34 §6 AC59 (S59).
- **What is wrong:** AC59 greps `git diff c63aabbb..HEAD` of unattended.sh and run-gates.sh for a moved `KIT_*_VERSION`. The close runs on the prepared merge, which includes main's later landings and an earlier prepare's mint.
- **Consequence:** another build's minted bump shows as a hand-bump on this branch, a false red at the close for reasons outside the build. Latent today (the diff is empty).
- **Fix (judged sound):** restrict to the build's own non-merge commits: `git log --no-merges -p c63aabbb..HEAD -- tools/unattended/unattended.sh tools/run-gates/run-gates.sh | grep -E '^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION='`, excluding `mint:` commits; or diff from `git merge-base origin/main HEAD` on the branch tip before prepare.
- **Gate:** a checklist entry, "a test oracle never diffs from a fixed historical sha".

### M18 — A failed confirming read after a lost flush push is treated as a yield (id 34)

- **Where:** TOOL-dPlacedRequest-24 §2 S5 and §4 "The queue under the lock".
- **What is wrong:** S5 maps the confirming `ls-remote` by tip value only ("equal -> landed, any other tip -> yield"); a failed or timed-out read falls into the yield branch.
- **Consequence:** the line is dropped with a `lease-yielded` event even when the commit landed, the false yield this unit exists to remove.
- **Fix (judged sound):** a failed or timed-out `ls-remote` keeps the line (rc 2 semantics) and prints one `queue: NOTE -` line. Add an AC with a stub `observe_remote` failing on the confirming read: the line stays and no `lease-yielded` line is written.
- **Gate:** a checklist entry, "every remote read's outcome table has a row for no answer".

### M19 — The lander's re-fence reports a transient read failure as a lost lease (id 35)

- **Where:** TOOL-dPlacedRequest-29 §2 S1 and S2.
- **What is wrong:** S1 prints `lease refused — epoch-fence` for "any other reading", and S2 maps every refusal to TOOL-15's `fenced`, whose remedy is `--abort <slug> --code claim-lost`. TOOL-15 keeps a separate `offline` cause for a failed read.
- **Consequence:** a remote hiccup during the re-fence read tells a run that still holds its lease to abort as claim-lost; a recoverable aborted landing.
- **Fix (judged sound):** keep TOOL-15 S2's `lease refused — offline` for an unanswered read and reserve `epoch-fence` for a read that answered with a risen epoch, foreign holder or off-chain tip; map `offline` to `unreachable` (exit 1, no abort remedy). Add an AC with a stub that kills the `--after` read: the lander prints `unreachable`, not `fenced`.
- **Note on grade:** the skeptic re-graded this from high to medium: the path is narrow and the effect is a recoverable aborted landing, not lost data.
- **Gate:** as M18.

### M20 — TOOL-26's walk pseudo-code never tests the tip itself (id 38)

- **Where:** TOOL-dPlacedRequest-26 §4 "The walk, per gov-claim tail".
- **What is wrong:** the first commit only sets the tip and tenure epoch; the renewing-beat test and `oldest-of-tenure = this commit` sit under "each later commit", contradicting S2 and S3.
- **Consequence:** a just-renewed lease is aged from an older beat and can read `stale` early; a one-commit tenure (AC1's own fresh take-over) is aged from nothing, giving `unknown` or a wrong age.
- **Fix (judged sound):** set the tenure epoch from the tip, then for each commit, tip included: stop if the epoch differs, else record the renewing beat if `renews` is yes or absent and none is held, and set oldest-of-tenure. Add an AC: a one-commit tenure whose tip is `renews: yes`, sighted a minute ago, reads `live`.
- **Gate:** the lease-fixture arm of H2, extended with the one-commit tenure.

### M21 — Concurrent `--request` calls can overwrite each other's stored words (id 39)

- **Where:** TOOL-dPlacedRequest-30 §2 S1 and §4 "The order of --request".
- **What is wrong:** the collision test (`cmp -s`, then copy when absent) is check-then-act on a node-local store with no lock and no create-only write.
- **Consequence:** two same-node calls with different words under one key both copy; one session's words are silently replaced while both succeed, and TOOL-31 then denies the overwritten session consent without saying why.
- **Fix (judged sound):** make the store write create-only and atomic (temp file plus `ln`, or a `mkdir` guard), or take TOOL-24's `write_node_lock` on a `requests.lock` around compare, copy and `.typed` append, so the loser re-runs the compare and gets the collision refusal. Add an AC with two background `--request` calls of differing files: exactly one exits 2 printing `collision`.
- **Gate:** a checklist entry, "every check-then-write on a shared store names its lock or atomic create".

### M22 — The identity refusal and the `RUN_CLAIMS`-off answer are unordered (id 41)

- **Where:** TOOL-dPlacedRequest-32 §2 S4, with TOOL-dPlacedRequest-34 S23.
- **What is wrong:** TOOL-32 S4 exits 2 on no session and no keepalive; TOOL-34 S23 has every `--lease` act print `lease — off` and exit 0 with `RUN_CLAIMS` off. Neither spec orders the two guards.
- **Consequence:** a dark-by-default adopter under a harness with no session id gets exit 2 or exit 0 by the builder's choice; exit 2 breaks AC23's promise and can stop a landing that should push as today.
- **Fix (judged sound):** order the guards: the `RUN_CLAIMS`-off answer comes before any identity test, stated in both specs' design blocks. Add an AC: `env -u CLAUDE_CODE_SESSION_ID` with `RUN_CLAIMS` off, `--lease acquire build tFix` prints `lease — off` and exits 0. (H3 relies on the same order.)
- **Gate:** a checklist entry, "two guards on one verb state their order".

---

## LOW

### L1 — TOOL-31 AC2 is already green on the code it replaces (id 9)

- **Where:** TOOL-dPlacedRequest-31 §6 AC2.
- **What is wrong and consequence:** TOOL-19's base predicate passes only on a whole line equal to the session id, so the planted `s2<TAB><blob>` already returns 1; the arm is never observed red, and only AC1 exercises the binding.
- **Fix (judged sound):** stage AC2 against a planted session-only line `s2` beside a stored copy s2 never submitted, expecting 1 after this unit and 0 on the base predicate; or drop AC2 and say AC1 carries the case.

### L2 — TOOL-34 S10/S13 re-observe what TOOL-33 already closed (id 10)

- **Where:** TOOL-dPlacedRequest-34 §2 S10, S13; §6 AC10, AC13.
- **What is wrong and consequence:** AC13's `git grep` is word for word TOOL-33 AC4, and S10/AC10 restate TOOL-33 S2/S3; TOOL-33 lands at order 13, so both criteria are green before TOOL-34 (order 22) and the batch's accounting overstates what it observes.
- **Fix (judged sound):** cite TOOL-33 S2/S3 as the closing mechanism and mark AC10/AC13 as re-observations, or fold findings 33 and 34 into TOOL-33's item list and drop the duplicates.

### L3 — AC35's pattern cannot match the `refs/gov/runs/*` reader S35 lists (id 11)

- **Where:** TOOL-dPlacedRequest-34 §2 S35, §6 AC35.
- **What is wrong and consequence:** VERBS.template.md:279 spells `'refs/gov/runs/*'`, which AC35's `refs/gov/runs/<slug>\|refs/gov/runs/tRun` does not match, so the leftover sentence can survive the migration with AC35 green.
- **Fix (judged sound):** widen AC35's pattern to `refs/gov/runs` and keep the "only legacy-read mentions" judgement, or give VERBS:279 its own grep.

### L4 — AC6 reds a correct build that spells `gov-feed.lock` at the release (id 12)

- **Where:** TOOL-dPlacedRequest-24 §6 AC6.
- **What is wrong and consequence:** AC6 requires the path only as `write_node_lock`'s argument, but the feed must also release through `remove_node_lock` and the factory keeps the claim-push comment; the builder must reinterpret the criterion.
- **Fix (judged sound):** require every line spelling `gov-feed.lock` to be a `write_node_lock`/`remove_node_lock` call or a comment, and no `mkdir`/`rmdir` of it to remain in gov-feed.sh.

### L5 — AC38's grep misses `check_claim_push_clear` (id 20)

- **Where:** TOOL-dPlacedRequest-34 §2 S38, §4 Evidence, §6 AC38.
- **What is wrong and consequence:** the "four" claim-push functions are three `*claim_push_lock*` names plus `check_claim_push_clear` (push-main.sh, symbols.json:3826); if it survives, AC38's `grep -c claim_push_lock` still prints 0.
- **Fix (judged sound):** name `check_claim_push_clear` in S38's Readers and grep `claim_push_lock\|check_claim_push_clear`.

### L6 — The renamed node-lock health events are undocumented (ids 21, 31)

- **Where:** TOOL-dPlacedRequest-24 §2 S1 Readers clause and §4 Files touched.
- **What is wrong and consequence:** TOOL-11 S7 drops `claim-push-lock-broken` and `claim-push-guard-cleared` from tools/unattended/README.md:246-252; TOOL-24 mints `node-lock-broken` and `node-lock-guard-cleared` without adding them, so the README lists neither and an operator finds undocumented health-log lines.
- **Fix (judged sound for both findings):** add tools/unattended/README.md to Files touched; have S1 add both events to the health-event sentence, naming the feed and queue locks; add an AC grepping the README for both names.

### L7 — TOOL-32's identity pseudo-code drops S3's "either session absent" condition (id 40; same defect as M8)

- **Where:** TOOL-dPlacedRequest-32 §4 "The identity rule" versus §2 S3.
- **What is wrong and consequence:** `mine = (sessions present, equal, tags equal) or (keepalives present and equal)` lets a matching keepalive alone make `mine` when both sessions are present and differ; today's :2260 needs both equal.
- **Fix (judged sound):** fixed by M8's restated rule and its take-over AC.
- **Note on grade:** the skeptic re-graded this from medium to low: the pseudo-code is scoped to the lease mode, step-checklist leases write keepalive `absent`, and today's prior-session row already treats a cross-session keepalive match as mine.

### L8 — Plain `git hash-object` makes consent survive an end-of-line rewrite (id 42; same defect as M7)

- **Where:** TOOL-dPlacedRequest-31 §2 S1-S2 and §4 "The line and the read".
- **What is wrong and consequence:** under `core.autocrlf=true` and `* text=auto` a CRLF file and its LF twin share a blob (re-probed), so consent survives a line-ending rewrite of the stored copy and disagrees with TOOL-30's `cmp -s`.
- **Fix (judged sound):** fixed by M7: `git hash-object --no-filters` on both sides, plus the CRLF-rewrite AC.

### L9 — The card publish's kill line can misreport a landed write (id 43; same defect as M9)

- **Where:** TOOL-dPlacedRequest-33 §2 S2 and §4 "The publish, end to end" (killed row).
- **What is wrong and consequence:** a kill after the compare-and-swap push prints `card — remote-ref not written`; the feed misses the write until a later sighting, while the next publish's CAS reads the real tip, so no ref is corrupted.
- **Fix (judged sound):** word the outcome `card — remote-ref unknown: no answer within <n>s`, and name in S2 that a kill after the push leaves the feed append to the next sighting (TOOL-34 S5). M9's fix carries the bound and the fixture plant.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=43 confirmed=42 refuted=1 unverified=0 blocker=0 high=8 medium=24 low=10 agents=11 out-tokens=219412
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 2 S43, section 4 "The bounded walk (S43)" | high | high | confirmed | Re-read TOOL-34:189-193 (S43) and :329-340 (§4). Both list three ways a walk can stop (the renewing beat, the tenure's start, the first commit sighted before the threshold) without ordering them. §4 adds that a commit sighted before the threshold 'makes the verdict stale whatever lies further back'. TOOL-26:34-36 stops the walk at the first commit whose epoch differs. TOOL-26 AC1 (:123-127) has the epoch-2 tip sighted a minute ago with the epoch-1 commit sighted 25 h ago behind it, and expects `live`. In that chain the tenure-start stop and the threshold stop fire on the same epoch-1 commit, and the text never says which wins. A build that checks the threshold first reads a fresh take-over `stale`. Order: TOOL-26 is step 5 and TOOL-34 step 22 (README build-order), and AC43 only times the walk. | sound | - |
| 2 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 2 S1, section 4 Evidence | high | high | confirmed | TOOL-24 S1 (:38-50) says the factory's bodies are write_claim_push_lock and its siblings, renamed and placed in the byte-identical gov_feed_sh block. At unattended.sh:2338 and :2351 those bodies call `add_health_event "$(resolve_health_log "$ROOT")"`. grep finds no ROOT= assignment and no add_health_event or resolve_health_log in tools/push-main.sh or tools/run-gates/post-merge.sh (push-main.sh's single ROOT match is not an assignment), and both files run `set -u` (push-main.sh:64, post-merge.sh:26). The block's carriers are named in TOOL-15:58/165 (push-main) and TOOL-11:203, TOOL-13:183 and TOOL-24:130 (post-merge). On the stale-break path an unbound $ROOT aborts the carrier. TOOL-24 says nothing about how the block reaches the health log. | sound | - |
| 3 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-23.md:section 6 AC3 (observing section 2 S1) | medium | medium | confirmed | TOOL-23 §4 (:82-84) puts the policy read and the queue in the lease writer's offline branch, which is a separate helper. AC3 (:127-130) only flags a function body that spells both `read_claims strict` and `add_gov_queue`, so a strict caller that reaches the queue through the writer is invisible to it. AC1 and AC2 (:117-126) run only `--preflight`, so nothing covers run_takeover or verb_close behaviourally. AC3's planted case calls add_gov_queue directly, which is not the shape the design produces. | sound | a-helper-extraction-blinds-a-per-function-rule |
| 4 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md:section 6 AC5 (observing section 2 S4) | medium | medium | confirmed | grep over the spec set shows the lease writers spell a variable tip: TOOL-20:34 `build_gov_commit <tip read> <message>` and TOOL-11:45 `build_gov_commit "$CW_SHA"`. TOOL-28 AC5 (:137-141) matches only the literal `build_gov_commit ""`. A second parentless create spelled with an empty variable therefore passes, and a correct never-named branch that passes a variable makes AC5 list nothing. The S4 class check certifies nothing. | sound | - |
| 5 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md:section 6 AC5 | medium | medium | confirmed | unattended.sh:546 runs `ROOT="$(GIT rev-parse --show-toplevel ...)"` unconditionally, and GIT is defined at lib-unattended.sh:61 as `git -c ... "$@"`. That happens before the conf, and so RUN_CLAIMS, is read and before any verb is dispatched. A logging git stub on PATH therefore always logs at least that one call, so TOOL-33 AC5 (:170-173), 'the stub logged no call', fails on a correct build. | sound | - |
| 6 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 2 S14, section 4 "The claim offline (S14, S15)" | medium | medium | confirmed | TOOL-34's §4 table (:316-319) routes `warn` and `follow-leases` to exit 4 and `awaiting`, and S14 (:75-78) amends only TOOL-3's awaiting row. TOOL-3's outcome table still lists, in its `refused` row, '`offline` under `refuse` or `follow-leases`', so follow-leases has two outcomes. AC14 (:473-476) tests only the default and `refuse`. | sound | two-answers-to-one-question |
| 7 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 2 S40, section 6 AC40 | medium | medium | confirmed | TOOL-34 AC40 (:535-536) is TOOL-1 AC7's flush clause ('with the origin restored, `--lease flush` creates the ref', :350-352). AC7 is at step 3 and TOOL-24's AC1/AC2 on tOff at step 4, while TOOL-34 is at step 22 (README build-order). TOOL-24:72-73 defers the `-` placeholder to TOOL-34. So either the earlier criteria cannot pass, or AC40 is already green before TOOL-34 is built and cannot fail. | sound | - |
| 8 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-23.md:section 2 S2 and S3 | medium | medium | confirmed | TOOL-23 S2 (:36-40) closes the population of `leases.offline` to run_lease_verb plus the soft and quiet read_claims callers that write a lease, and S3 (:41-46) writes the same statement into the stops guide. TOOL-21 S2 (:49-51) and its `offline` row (:73) hand --entry-claim's unanswered write to `leases.offline`, and TOOL-34 S14 reads `refuse` there. --entry-claim is neither run_lease_verb nor a read_claims caller, so the guide would name a population that leaves out a real reader of the key. | sound | - |
| 9 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md:section 6 AC2 | low | low | confirmed | TOOL-19 S5 (:56-57, :120) returns 0 only when this session's id is a whole line of .typed. The line `s2<TAB><blob>` that TOOL-31 AC2 (:105-107) plants is not the line `s2`, so the base predicate already returns 1. AC2 is therefore green before the unit is built and cannot be observed red against the code it replaces. AC1 carries the binding case. | sound | - |
| 10 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 2 S10, S13; section 6 AC10, AC13 | low | low | confirmed | TOOL-34.md:61-63 (S10) and :72-74 (S13), with AC10 :465-466 and AC13 :471-472, restate what TOOL-33 S3 (:52-54) deletes. AC13's git grep is word-for-word TOOL-33 AC4 (:167-168). README rows 176/185 put TOOL-33 at order 13 and TOOL-34 at order 22, so both criteria are already green when TOOL-34 is built and cannot fail. S10 does say 'after TOOL-dPlacedRequest-33', but its AC is still reported as observing finding 33 closed. The effect is on how findings are accounted for, not on behaviour. | sound | - |
| 11 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 2 S35, section 6 AC35 | low | low | confirmed | S35 (TOOL-34.md:156-164) lists tools/unattended/VERBS.template.md:279 as a reader that must name refs/gov/leases/<slug>/build. Line 279 reads `'refs/gov/runs/*'` still shows a leftover one. AC35 (:525) greps 'refs/gov/runs/<slug>\\|refs/gov/runs/tRun', which cannot match `refs/gov/runs/*`, so the criterion never observes that file or its renders. | sound | - |
| 12 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 6 AC6 | low | low | confirmed | TOOL-24 S1 (:37-40) gives the factory remove_node_lock <dir> <token>, and the feed must release gov-feed.lock through it. AC6 (:184-187) requires grep -n 'gov-feed.lock' gov-feed.sh to name the lock 'only as write_node_lock's argument'. A correct build that spells the path in the release call fails AC6 unless the path happens to be held in a variable. This is criterion wording only. | sound | - |
| 13 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 2 S1, section 4 Evidence and Files touched | high | high | confirmed | git show c63aabbb:tools/unattended/unattended.sh:2331-2354: write_claim_push_lock evaluates `$(( $EPOCHSECONDS + REMOTE_BOUND + 10 ))` and calls add_health_event "$(resolve_health_log "$ROOT")". TOOL-24 S1 makes the factory these bodies renamed, inline byte-identical in every gov_feed_sh copy. TOOL-13:38-39 puts the block in post-merge.sh, and TOOL-15:58/:165 puts it in push-main.sh. At the base, grep over push-main.sh and post-merge.sh finds no REMOTE_BOUND, add_health_event, resolve_health_log or ROOT=, and both scripts run under set -u (:64 and :26). An unset REMOTE_BOUND in an arithmetic expansion under set -u aborts a non-interactive shell, so the first feed append dies. TOOL-24's Files touched also omits push-main.sh. | sound | - |
| 14 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 2 S2 and S3, section 6 AC3 | medium | - | refuted | The cited section already states a wall-clock bound. S2 and S3 say 'for up to 5 s', and the §4 sketch says '(50 ms retries, 5 s)'. Neither specifies 100 counted tries. My re-probe of 100 mkdir+sleep 0.05 iterations did take 12.0 s here, but that only shows a counted loop would violate the spec's own 5 s bound, and AC3's 'within 6 s' would catch it, which is the criterion doing its job. The spec as written is not defective. | sound | - |
| 15 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md:section 2 S1-S2, section 4 'The line and the read', section 10 | medium | medium | confirmed | TOOL-31 :32, :59-62 and :67 bind consent with plain `git hash-object` and call it evidence of 'these exact bytes'. This clone has core.autocrlf=true (system gitconfig) and .gitattributes `* text=auto`. My probe hashed an LF file and its CRLF twin in a scratch dir: plain hash-object gave 422c2b7a... for both, while --no-filters gave 422c2b7a... and c30dea8a... TOOL-30 :64/:69 compares with byte-exact cmp -s, so the two units disagree on a CR-only re-submission. | sound | - |
| 16 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md:section 2 S3, section 4 'The identity rule' and Evidence | medium | medium | confirmed | At the base, unattended.sh:2260 reads `if [ "$c_ka" = "$ka" ] && [ "$c_sess" = "$sid" ]; then cls=mine`, comparing keepalive AND session. :2261 adds prior-session mine only when mode != take-over, and :2263 gives `same` for take-over. TOOL-32 S3 (:40-43) conditions the keepalive path on either session being absent and calls it 'today's keepalive comparison'. That is not today's rule. §4's pseudo-code (:77-78) also drops the either-absent condition: `or (keepalive != absent and record keepalive != absent and equal)`. Two present, differing sessions with equal keepalives would therefore read `mine`, and AC5 does not observe that case. | sound | - |
| 17 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md:section 2 S2, section 4 'The publish, end to end', section 5 risks | medium | medium | confirmed | TOOL-33 S2 (:46-49) and §4 :98 run `--card-ref write`, a CAS-push writer, under `timeout -k 2 $CARD_FETCH_BOUND`, and print 'remote-ref not written: no answer within <n>s' on a kill. A kill after the push lands therefore reports a false outcome. CARD_FETCH_BOUND has no value anywhere: the only definition-like line is TOOL-2's inventory row 201, 'none declared', and grep finds it in no code. The base lock's `until` is EPOCHSECONDS+REMOTE_BOUND+10 (:2348), so a kill inside the feed append leaves a ~70 s lock. §5 :144 likens this to the claims cell, but that cell kills the read-only --claims. | sound | - |
| 18 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 4 "`readCard`'s cost (S28)", section 2 S28 | medium | medium | confirmed | TOOL-34 §4 (:357-361) says readCard's bash call is 'bounded by the hook's existing spawn bound'. tools/hooks/scratch-guard.js has a single spawnSync, at :710 (`spawnSync('git', args, { cwd: toplevel, encoding: 'utf8' })`), with no timeout option, and readCard (:667-676) spawns nothing. No spawn bound exists, so S28's 'a checker that does not answer reads as no card' has no mechanism, and AC28 does not test a hung checker. | sound | - |
| 19 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md:section 2 S4, section 6 AC5 | medium | medium | confirmed | Spec 28 AC5 (lines 137-141) checks function bodies that spell the literal `build_gov_commit ""`. TOOL-11 S3 (line 45) has callers write `build_gov_commit "$CW_SHA"`, and TOOL-20 S1 (line 34) has the offer call `build_gov_commit <tip read> <message>`, a variable that is empty on an absent lease. So a second parentless create that passes an empty variable is never listed, and the planted write_lease_offer case slips past the awk. The check certifies a spelling, not the behaviour. I graded it medium because AC1 to AC3 still exercise the offer over a tombstone and an unnamed ref by behaviour. | sound | - |
| 20 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 2 S38, section 4 Evidence, section 6 AC38 | low | low | confirmed | symbols.json has check_claim_push_clear at :3826 with file tools/push-main.sh, plus three *claim_push_lock* ids at :3831, :15301 and :24166. Spec 34 S38 (line 175) says 'the four claim-push lock functions' and names only `write_claim_push_lock and its three siblings`. AC38 (line 532) greps `claim_push_lock`, which does not match check_claim_push_clear. If that function survives, gen_map --check stays green (the map is current) and the grep prints 0. | sound | - |
| 21 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 2 S1 Readers, section 4 Files touched | low | low | confirmed | tools/unattended/README.md:249-250 documents claim-push-lock-broken and claim-push-guard-cleared. TOOL-11 S7 (lines 70-71) drops them from the README. Spec 24 S1 (line 43) mints node-lock-broken and node-lock-guard-cleared, but its Files touched (lines 126-134) lists no README and no AC greps for the new names. The kit README's health-event list therefore omits two events that are still emitted. This is a documentation gap only. | sound | - |
| 22 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md:section 2 S2, section 10 (and TOOL-dPlacedRequest-34 section 2 S11) | medium | medium | confirmed | manifest-check.sh has the bounded driver call twice: `timeout -k 1 5 true` at :560 and :651, and `GOV_RUNLOG=0 timeout -k 2` at :564 and :655, in derive_overlaps_line and derive_claims_line. Spec 33 S2 (lines 44-46) and section 10 (line 204) copy it 'in shape' for the publish. Spec 34 S11 (lines 64-65) copies it again for the lookup. AGENTS.md:16 [reuse] says to extract a factory at a kind's second instance, never a copy. Spec 33 has no alternatives-rejected entry or non-goal that withholds the extraction. | sound | - |
| 23 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 2 S30 (and section 4 Evidence on derive_node_tag / resolve_node_tag) | medium | medium | confirmed | Spec 34 S30 (lines 135-136) keeps derive_node_tag and resolve_node_tag because they read 'a different registry' and says '§4 says so'. §4 (lines 288-292) only describes their match rules and says nothing about a different registry. coding-governance-agents.template.md:101-103 has `## Node registry` then {{NODE_TABLE}}, and render_playbook.py:424-430 derive_node_table builds that table from read_fleet over FLEET_NAME. The table is a rendered view of fleet.toml, so the stated justification is false and will mislead the next change. | sound | - |
| 24 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 2 S1 (and section 4 Files touched) | high | high | confirmed | unattended.sh:2331-2354 write_claim_push_lock reads REMOTE_BOUND (`$(( $EPOCHSECONDS + REMOTE_BOUND + 10 ))`), $ROOT, add_health_event and resolve_health_log. Spec 24 S1 (lines 36-43) moves these bodies, renamed, into gov_feed_sh, and S2 routes add_feed_event's gov-feed.lock through write_node_lock. TOOL-13 (lines 38-39) carries gov_feed_sh inline in post-merge.sh. post-merge.sh:26 and push-main.sh:64 run `set -u`, and grep finds no REMOTE_BOUND, ROOT=, add_health_event or resolve_health_log in either file. Re-running the probe printed 'REMOTE_BOUND: unbound variable' with rc=127, and neither 'after' nor 'end' was printed. AC6 checks byte parity only. | sound | - |
| 25 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 2 S40 (with TOOL-dPlacedRequest-24 S3) | high | medium | confirmed | Spec 34 S40 (lines 181-183) changes the queue line's empty cached tip to `-`. It has no Readers clause and names only the flush as the mapping-back reader. Spec 24 S3 (lines 53-55) dedupes on 'a line whose ref and cached tip equal the new one', and its AC1 (lines 164-166) runs the offline create twice. Nothing in S40 forces the normalisation to apply on both sides of the compare, so a raw-empty compare against the stored `-` re-queues and AC1 of spec 24 reds. I graded it medium because it depends on where the builder places the normalisation, and spec 24's AC1 would show it if run. | sound | a-spelling-change-strands-its-readers |
| 26 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md:section 2 S4 | high | high | confirmed | Spec 32 S4 (lines 44-47) refuses every `--lease <act>` with exit 2 when there is no session and no keepalive, with nothing read. It exempts only the driver's run claim. Spec 16:66/80/93 has dWellOiledMachine's supervisor run `--lease prune` on its cadence, TOOL-1:100 has `--lease flush`, and TOOL-15 S2 (lines 39-40) promises `fence — none`, exit 0, when RUN_CLAIMS is off. All of these fall under the blanket refusal, and the only criterion, AC3 (line 117), tests acquire alone. | sound | - |
| 27 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 2 S35 / S37 (section 6 AC37) | medium | medium | confirmed | cmp found the template and the render identical. `tr -d '\r' \| wc -c` printed 66859, and template-size-limits.txt:143 sets the limit at 66860. PROTOCOL.template.md:521 spells `refs/gov/runs/<slug>`, which S35 (lines 156-161) rewrites to `refs/gov/leases/<slug>/build`, 8 bytes longer. S37 (lines 169-171) budgets only TOOL-5's sentence 'at no byte cost'. No other spec trims the protocol, so AC37 and the size leg would go red. | sound | - |
| 28 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:whole file (the gen:spec-records region, lines 7-15) | medium | medium | confirmed | Re-probed: `wc -c` of -34.md prints 50111 (its blob matches the pin 297799719). tools/template-size-limits.txt:167 sets `memory/builds/*/spec/` to 49152. tools/template-size-highwater.txt has no dPlacedRequest row. The gen:spec-records region is 1067 bytes. The promoted-fix return at line 24 records 49043 bytes with '109 bytes to spare'. The rendered records region pushed the spec back over the ceiling, so the size leg reds at the bar. The bar catches it, so the effect is contained. | sound | - |
| 29 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md:section 2 S1 and section 3 Edges | medium | medium | confirmed | -31 S1 changes the line to `<session><TAB><blob>`, and S2 says 'A line of another shape reads as no consent'. -31's only edge is consumes-from TOOL-19. It has no hands-off to TOOL-5 and no Readers clause. TOOL-5 AC3 (5.md:200-202) says 'with the line planted it passes', without saying what the line looks like. TOOL-5 runs at build-order step 19, after -31 at step 11. TOOL-19:120 still says 'one session id per line'. A plant that writes the old bare-session shape reds AC3, or tempts the builder to loosen the predicate. | sound | a-spelling-change-strands-its-readers |
| 30 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:section 6 AC59 (S59) | medium | medium | confirmed | AC59 (-34.md:581-583) diffs from the fixed sha c63aabbb to HEAD. `git log c63aabbb..origin/main` already shows 60d60e694, so main has moved past the base. The phrase 'before the lander's mint' only keeps out this landing's own mint. The README (:41) closes on the prepared merge and repeats the close after a re-prepare. At that point HEAD contains main's later landings, including version bumps other builds minted, plus an earlier prepare's mint. The diff would then show a moved KIT_*_VERSION that no branch commit hand-bumped. Today `git diff c63aabbb..origin/main` on the two files is empty, so this is a latent false red, and its effect is contained. | sound | test-oracle-read-from-a-historical-sha |
| 31 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 2 S1 Readers clause and section 4 Files touched | low | low | confirmed | tools/unattended/README.md:246-252 is the sentence that lists the health events, and it names claim-push-lock-broken and claim-push-guard-cleared. TOOL-11 S7 (-11.md:72-73) drops those two names. -24 S1 mints node-lock-broken and node-lock-guard-cleared. Its Files touched list (:126-134) has no README.md, and its Readers clause hands the README over to TOOL-11. After both units the README names neither the old events nor the new ones. Only the documentation is affected. | sound | - |
| 32 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 2 S1 (the factory bodies) and section 6 AC6 | high | high | confirmed | `git show c63aabbb:tools/unattended/unattended.sh` lines 2331-2354 show write_claim_push_lock writing `$(( $EPOCHSECONDS + REMOTE_BOUND + 10 ))` and calling `add_health_event "$(resolve_health_log "$ROOT")"`. -24 S1 says the factory bodies are these bodies 'renamed', placed in gov_feed_sh, which post-merge.sh carries inline. A grep of post-merge.sh and push-main.sh for REMOTE_BOUND, add_health_event and resolve_health_log finds 0 in each. post-merge.sh:26 is `set -u`. TOOL-13 (:172) has post-merge's bar-red write go through add_feed_event, so the first lock take there dies on an unbound variable. AC6 (-24:184-187) only cmp's the cuts and greps names, so it passes without ever taking the lock outside the driver. | sound | - |
| 33 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 2 S3 and section 4 'Alternatives rejected' (dedupe key) | high | high | confirmed | -24 S3 (:54-57) drops any write whose ref and cached tip match a queued line, printing `queued — already`. TOOL-1 S10 (1.md:96-102) builds every offline write on the cached tip and creates no ref, so the cached tip does not move while offline. Example: a node that holds a lease runs an offline renew or acquire, then an offline release of the same ref. The release shares the key and is silently dropped, even though the user is told it is queued. The flush then lands only the first write, so the remote shows a lease the node believes it released. -24 only considers a re-run of the same act (AC1). | unsound | - |
| 34 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md:section 2 S5 and section 4 'The queue under the lock' | medium | medium | confirmed | -24 S5 (:63-66) and the pseudo-code at :111 split the outcome only by tip value: 'equal -> landed, any other tip -> yield'. No outcome is given for an ls-remote that fails or hits its bound, so an empty read falls into the yield branch. That drops the line and writes a lease-yielded event even when the push actually landed, which is the false yield this unit exists to remove. Keeping the line is safe: the next flush's compare-and-swap loses again, and a confirming read that answers then resolves the line as landed. | sound | - |
| 35 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-29.md:section 2 S1 ('Any other reading prints ... epoch-fence') and S2 | high | medium | confirmed | -29 S1 (:34-39) says 'Any other reading prints `lease refused — epoch-fence`', and S2 (:40-43) maps every refusal to TOOL-15's `fenced`. TOOL-15:120 has a separate result for a failed read, `lease refused — offline`. TOOL-15:151 gives `fenced` the remedy `--abort <slug> --code claim-lost`. Even if S1's 'as S2 does' kept `offline`, -29 S2 would still turn that refusal into `fenced`. So a transient failure of the re-fence read tells a run that still holds its lease to abort as claim-lost. The path is narrow, since the ls-remote just before it succeeded. The effect is a recoverable aborted landing, not lost data, so I grade it medium. | sound | - |
| 36 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md:section 2 S2 (the list of creates) and section 6 AC5 | high | high | confirmed | -28 S2 (:37-41) limits the creates that call read_feed_lease_tip to writes 'whose read finds the ref absent on the remote'. The offline branch of TOOL-1 S10 never reads the remote and builds on the cached tip. If the cached tip is empty, for example after a tombstone was deleted outside the kit and a pruning fetch dropped its cache ref, the offline acquire queues a parentless epoch-1 create without checking the feed. TOOL-16 S6's age rule only refuses lines past the age bound, so a fresh line's compare-and-swap on the absent ref lands it, bringing the closed build back as held. AC5 (:137-141) only matches the literal `build_gov_commit ""`, so a create passed `"$tip"` escapes it. S4 claims the whole class, but AC5 checks only that one spelling. | sound | - |
| 37 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-23.md:section 6 AC3 | medium | medium | confirmed | TOOL-23 §4 (lines 82-84) puts the policy read and queue in the lease writer's offline branch, while AC3 (lines 127-130) only greps for a function body spelling both `read_claims strict` and `add_gov_queue`. `grep -n add_gov_queue tools/unattended/unattended.sh` printed nothing, so the queue does not exist yet. Today's strict callers (:2202, :7477, :9037, :10839) reach writes through check_claim_writable and the writer, never directly. Built as designed, no function will spell both names, so AC3 is green whatever the call graph is. Its 'Red when: a strict caller can queue a write' is only caught for a direct-call plant, not for a writer whose offline branch queues after a failed strict read. AC1 still observes the behaviour, so the effect is contained. | sound | - |
| 38 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-26.md:section 4 'The walk, per gov-claim tail' | medium | medium | confirmed | TOOL-26 §4 lines 71-79: the first commit only sets the tip and the tenure epoch. The `renews yes -> renewing beat` and `oldest-of-tenure = this commit` steps sit under 'each later commit'. So a renewing tip is never the beat, and a one-commit tenure ends with neither value set. This contradicts S2 ('the newest commit of the tenure whose renews reads yes') and S3 ('aged from its first commit'), which would be the tip in a one-commit tenure. A builder following the pseudo-code ages a lease from the wrong commit or from nothing. | sound | - |
| 39 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-30.md:section 2 S1 and section 4 'The order of --request' | medium | medium | confirmed | TOOL-30 §4 (the order of --request) is cmp -s, then copy when absent. No lock or create-only write appears in it (`grep -n lock` on the TOOL-30 spec printed nothing), and TOOL-19 S2 says 'keeping the first copy when one exists' with no mechanism. Two concurrent same-node --request calls with different words under one key can both see the copy absent and both copy, so one text is overwritten while both succeed. That is the defect TOOL-30 exists to close, on a narrow concurrent path. write_node_lock exists in TOOL-24 (line 38) for the fix to reuse. | sound | - |
| 40 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md:section 4 'The identity rule' versus section 2 S3 | medium | low | confirmed | TOOL-32 §4's pseudo-code `mine(lease) = (sessions present, equal, tags equal) or (keepalives present and equal)` makes a record mine on an equal keepalive even when both sessions are present and differ. S3 (lines 40-43) allows the keepalive path only 'with either absent'. The divergence is real, and today's row (:2260) needs keepalive and session both equal. The finding overstates its reach, though. The pseudo-code is scoped to the lease mode only, not 'every mode, take-over included'. TOOL-1 (line 178) says step-checklist leases write keepalive `absent`, so the keepalive arm only bites for a keepalive-carrying holder, and today's prior-session row already treats a keepalive match across sessions as mine. The effect is a spec inconsistency with a narrow, contained behaviour change. | sound | - |
| 41 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md:section 2 S4 (with TOOL-dPlacedRequest-34 S23) | medium | medium | confirmed | TOOL-32 S4 (lines 44-47): --lease <act> with no session and no keepalive exits 2. TOOL-34 S23 (lines 104-107): with RUN_CLAIMS off every --lease act prints `lease — off` and exits 0, and fence prints `fence — none`. AC23 is red when an off switch refuses. `grep RUN_CLAIMS` on the TOOL-32 spec printed nothing, and neither spec orders the two guards. When both hold, an adopter on the default `off` with no session id gets exit 2 or exit 0 depending on the order the builder picks. | sound | two-guards-one-question-two-answers |
| 42 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md:section 2 S1-S2 and section 4 'The line and the read' | low | low | confirmed | Re-probed in my scratch directory. A CRLF file and its LF twin both hash to 75633a73... under plain `git hash-object`. With --no-filters the CRLF file gives 3d4a1ab2... and the LF file gives 75633a73.... `core.autocrlf` is true and .gitattributes:2 is `* text=auto`. TOOL-31 lines 32, 59 and 62 use plain `git hash-object` yet claim 'evidence of these exact bytes' (line 67), so an end-of-line rewrite of the stored copy keeps consent, and the result disagrees with TOOL-30's byte-exact cmp. | sound | - |
| 43 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md:section 2 S2 and section 4 'The publish, end to end' (killed row) | low | low | confirmed | TOOL-33 S2 (lines 46-49) and §4's table map a kill to `card — remote-ref not written: no answer within <n>s`. The kill wraps the whole driver call under `timeout -k 2 $CARD_FETCH_BOUND`, so it can land after the compare-and-swap push succeeded, and the line then misreports the write. The next publish's CAS reads the real tip, so only the message and the feed are affected. | sound | - |
