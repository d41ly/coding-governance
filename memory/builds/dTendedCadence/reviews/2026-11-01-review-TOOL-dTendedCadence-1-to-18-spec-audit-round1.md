**Serves:** spec-audit TOOL-dTendedCadence-1@rev-1 TOOL-dTendedCadence-10@rev-1 TOOL-dTendedCadence-11@rev-1 TOOL-dTendedCadence-12@rev-1 TOOL-dTendedCadence-13@rev-1 TOOL-dTendedCadence-14@rev-1 TOOL-dTendedCadence-15@rev-1 TOOL-dTendedCadence-16@rev-1 TOOL-dTendedCadence-17@rev-1 TOOL-dTendedCadence-18@rev-1 TOOL-dTendedCadence-2@rev-1 TOOL-dTendedCadence-3@rev-1 TOOL-dTendedCadence-4@rev-1 TOOL-dTendedCadence-5@rev-1 TOOL-dTendedCadence-6@rev-1 TOOL-dTendedCadence-7@rev-1 TOOL-dTendedCadence-8@rev-1 TOOL-dTendedCadence-9@rev-1

# Tier-2 review: the spec audit of dTendedCadence's 18 unit specs, TOOL-dTendedCadence-1 to -18 (round 1)

Provenance: this is a Tier-2 spec audit at full intensity, run on 2026-11-01 over the 18 unit specs landed at the spec commit `0cde7925d`. Five lenses ran first, with gov-spec-reviewer as the finders. Five skeptic batches followed (gov-skeptic), then synthesis (gov-synthesizer). One spec document was supplied as `specs`, as sibling context.

Reviewed: memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md@acf7675d8a3fea5a5b0d553be01c267be3b30651, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-10.md@ca0d10bc332b7fbccbfbb48a6d26c27ff801da59, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-11.md@50b3ad1ff0fe41067334f56d221b69e69a3b2c07, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-12.md@645e155f66e62606ebce5abb15dd5d7c512fe99f, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-13.md@970fb782559a77f35a25b5e744e55f8613785b23, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-14.md@7698c8783fae8121eb4fad948d7def8ffbc8ee0e, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md@59f019a07193e20fec54f53047d9c78a60ad201f, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-16.md@c02b71dee772ff1196fcd74ae03c7641af58cb3e, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-17.md@2c4d4a66b408fdc78bc6e47208f62066d990e47f, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-18.md@b0e2afda7a87b46ec25cbf05a144b2ec74be2ab6, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-2.md@bb8c9a2a26e8c59330ee52023eb8e4ae46d529aa, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-3.md@be6e4c95c655df034c9f8a8be4fdebaec2e32fdc, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-4.md@3dc4308aac8fe3e83decf2f52e5d884baa06bb60, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-5.md@7e5db0faf0d52a5658066c37c3200d3495c50971, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-6.md@b13b425f288994173febe5bf01c4849b14591aad, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-7.md@b8b86e551f3f9455a153b0f38d07f09aa9dfe2c9, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-8.md@9150f3d7b6c5969e36493f12c8e488c2b40ead5f, memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-9.md@d121a58bcffec87ed149ce7e99ffa467bf2ec3b5

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker survived. What stands is 12 high items (13 findings), 29 medium items (30 findings) and 9 low items (10 findings), and every item has a fix. Each fix amends spec text before the affected unit builds. Two clusters must be settled before any unit at build order 2 or 3 starts. The first is the maintenance record's contract in unit 6 (H1, H2, H8): its key grammar, its `over-pin:` derivation, and which record the red leg reads. The second is who owns the `[[reading]]` key `route` (H3, M11). Units 6 and 8 are built first, so every later unit inherits whatever these settle.

## Review shape

The review ran at intensity full: raw 53, confirmed 53, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 20 | 20 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 15 | 15 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 0 blocker, 12 high, 29 medium, 9 low (50 items).
Adjudicated tally by raw confirmed finding: 0 blocker, 13 high, 30 medium, 10 low (53 findings).

Merges, each within one binding grade:
- Ids 1 and 39 (high) are one item. Both say unit 6's key grammar refuses the `s-<12hex>` and `<period>.<node>` keys.
- Ids 21 and 49 (medium) are one item. Both say units 8, 17 and 9 define the `route` value set incompatibly.
- Ids 19 and 38 (low) are one item. Both say the unit that creates `help/maintain.md` cannot write its `help/README.md` line.

Some findings describe one defect but carry different binding grades, so they stay separate items, cross-referenced here:
- Id 4 (high, H3) and ids 21 and 49 (medium, M11) are the `route` conflict. Fix them as one change.
- Id 42 (high, H10, the period in the text) and id 11 (medium, M7, the missing text and filer parameters) both concern unit 11's repeat intake. Fix them together.
- Id 5 (high, H4, the head is never committed) and id 28 (medium, M15, no filtered reader) both concern the security review's base.
- Id 17 (low, L2) and id 26 (medium, M13) are the second-policy-adapter defect. M13 carries the full fix and L2 is closed by it.
- Id 15 (medium, M10) and id 32 (medium, M16) both concern kit-version carriers, and their fixes pull in opposite directions. Id 32 cites push-main.sh: the lander mints the bump and a branch owes none. Settle that rule first, then apply id 15's carrier and leg listing only where a branch-side move remains.

Re-graded by the skeptic, and bound at that grade:
- Id 3: high to medium.
- Id 14: medium to high, because a merge-bar leg that can never red is a check certifying what it does not check.
- Id 21: high to medium, because the conflict surfaces as a red at landing.
- Id 22: medium to low, because the stale counts are in comments and docs.

The synthesis judges each binding grade right. One more note: id 21's impact, read alone, would sit with id 4 at high. It is bound at medium and kept apart for that reason only.

## Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 51 were judged sound and 2 were judged UNSOUND. The UNSOUND ones are ids 46 and 50, and each carries the skeptic's corrected fix below. 0 had no fix proposed and 0 were NOT JUDGED.
- Severity on confirmed findings: 0 were ungraded by the skeptic and 4 were re-graded by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Checklist: none was swept, because this project has no bug-class checklist yet. A zero count in any class is therefore not evidence that the project's recurring bug classes are absent.
- By design: none supplied. There was no caller byDesign and no block.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 1 spec document supplied as `specs`, as sibling context.
- Move check: no checked subject moved.

Every counter that gates completeness is zero, so this run is complete. Its coverage is still bounded by the generic lens brief and the absent checklist.

## High

### H1. Unit 6's record-key grammar refuses the every-session key and the node-pass key (ids 1, 39)

- **Where:** spec-6 §4 "The maintenance record", the key grammar held at the write boundary (:202-206). It conflicts with spec-2 S1/AC3 (:241-243) and spec-16 S6 (:93-94).
- **What is wrong:** The writer admits only `^\d{4}-(\d{2}-\d{2}|W\d{2})$` or `^[a-z0-9][a-z0-9-]*\.[0-9a-f]{12}$`, and anything else exits 2. Unit 2 mints `s-<12hex>` for `maintain.cadence: every-session`. Unit 16 hands `item.maintain.record` the key `<period>.<node>`. Both fail both patterns: `s-0123456789ab`, `2026-11-01.node-a` and `2026-W44.daily-pc` are all refused.
- **Consequence:** Under every-session, and on every node pass under the default `maintain.node-readings: every-node` once ask TOOL-dTendedCadence-32 lands, the record step exits 2. The walk then exits 1 (unit 1 S2), and the lease is released as a hand-over. The period re-runs on every wake and never closes. Each re-run repeats its filings, and no record is written. That loses the node's `unread-nodes:` line and the `retrofit-heat:` share that unit 9 S7 reads back.
- **Fix (judged SOUND by the skeptic, both findings):** Unit 6 should own the whole key class. It should name every family its siblings produce (daily and weekly period, `<event>.<sha12>`, `s-<12hex>`, and `<period>.<node>` with a stated node grammar), with one regex per family that still keeps a key from becoming a path. AC8/AC9 should get a planted case per family, plus `../escape`. The alternative is for units 2 and 16 to derive keys the existing grammar admits.
- **Left-shift gate:** a selftest arm in `maintenance.py` that feeds it every key each sibling's derivation function produces. The keys should be sourced from those functions, not typed by hand.

### H2. Unit 6 derives `over-pin:` lines from `over`, not from the route a reading reached (id 2)

- **Where:** spec-6 §4 "The maintenance record", the `over-pin:` derivation (:224-225). It conflicts with spec-15 S3/S4, spec-16 S8/AC7, spec-17 S11/AC7 and spec-14 S4.
- **What is wrong:** `over-pin:` is written as "the `keys` of every reading with `over` true". Unit 8 S5 defines `over` as live, pinned and over its pin. That set includes unit 14's log band (over the pin, with nothing filed) and `route = "ask"` readings already filed as asks. Units 16 and 17 say those readings never reach the leg. It also includes readings a direct fix just cleared. The stdin already carries a `route` field (spec-6:222), but the derivation ignores it.
- **Consequence:** Under `maintain.on-breach: red-leg`, unit 15's leg counts every `over-pin:` line and reds on readings the bands deliberately absorbed. That defeats the bands, and the AC7 of units 16 and 17 ("the red leg stays green") cannot pass on a correct build of unit 6.
- **Fix (judged SOUND by the skeptic):** Derive `over-pin:` lines only from readings whose stdin `route` is `held`, which unit 1 S6 already passes. Add an AC8 case: a reading that is `over` with route `filed` or `log` writes no `over-pin:` line.
- **Left-shift gate:** a bug-class checklist entry: "a record line derived from a raw measurement flag where a routed outcome exists".

### H3. The `[[reading]]` key `route` has three incompatible definitions and its edges run backwards (id 4)

- **Where:** spec-17 §2 S11 and §6 AC10 (:123-125, :285). It conflicts with spec-8 §4 "The row" and "The check" and AC3 (:127, :152, :103), spec-9 S4 (:78-79) and spec-16 S7.
- **What is wrong:**
  - Unit 8, at build order 3, mints `route` with the values `patch | file`, allowed only on a row with no fix. Its check refuses any other value.
  - Unit 17, at order 13, says it "adds" the key with the one value `ask` and refuses any other. AC10 refuses `route = "file"`.
  - Unit 9 says it adds `patch` to unit 17's key.
  - Unit 16 declares `ask`.
  - The §3 edges run 17→9 and 17→16, while unit 8, the real minter, hands the key to nobody. Unit 8's hand-off line even says unit 17 registers `route = "patch"`.
- **Consequence:** Built in order, unit 8's check refuses the `route = "ask"` rows of units 16 and 17 as a `# readings:` finding, which reds `drift-audit records`. Unit 17's AC10 then refuses the `file` value that unit 8 admits and uses as its default.
- **Fix (judged SOUND by the skeptic):** Make unit 8 the single owner of `route` and its whole value set: spell `patch | file | ask`, each with its meaning. Units 17 and 9 cite the key rather than add it. Re-point the edges to 8 → 9, 16 and 17. Change AC10's refusal case to an unknown value such as `route = "page"`. Apply this together with M11.
- **Left-shift gate:** a spec-audit checklist entry: "a key or value set claimed as 'added' by more than one unit". A grep arm over `spec/*.md` can flag "adds the key" phrasing for a key that another spec's §4 already defines.

### H4. The security review's `security-head` is never committed, so every weekly run reviews from the period start (id 5)

- **Where:** spec-13 §2 S3 (:47-48) and S6 (:78-84). It conflicts with spec-6 S6 (:89-91) and spec-1 S6 (:95-98).
- **What is wrong:** S3 takes the next base from the newest COMMITTED maintenance record carrying `security-head`. But S1 makes `security_review.py run` its own `[[adapter]]` cadence row. It writes the head through unit 6's writer, which commits nothing, and only the Maintain walk files the records-only landing intake. Unit 13 files no intake. The two programs also both key a weekly record `2026-W44`, so under `maintain.cadence: weekly` they write the same file `<date>-maintenance-2026-W44.md`.
- **Consequence:** Every run falls back to "the first-parent commit at or before the period start". Landings between the last review and the start of the week are never reviewed, which is a silent gap in a security control. AC2 and AC8 still pass, because AC2 plants a committed record and AC8 reads the uncommitted file.
- **Fix (judged SOUND by the skeptic):**
  - Have unit 13 S6 file the record's landing as unit 1 S6 does, through a cadence intake whose `--filer` names the review. The alternative is to carry `security-head` in a committed home unit 13 owns.
  - Add an AC that chains two runs with no planted record and observes the second run's base equal the first run's head.
  - Give the review a key distinct from Maintain's.
  - See M15 for the reader this base needs.
- **Left-shift gate:** a bug-class checklist entry: "a value read back 'from the newest committed record' with no named commit path for the write".

### H5. Unit 7 marks the served-text record non-gateable, yet its kept leg relies on it being gateable (id 14)

- **Where:** spec-7 §2 S2 (:56-57) against S3. The factory contract is in spec-18 S1.
- **What is wrong:** S2 sets the `dead_paths_in_served_text` record's `gateable` to false, "so `drift_report.py --check` gates nothing of it". S3 relies on it being "its one gateable signal at bound 0, so the exit is 1". Unit 18's `run_signal_leg` returns 1 only "when a gateable record is over or dead".
- **Consequence:** Built as S2 says, the kept merge-bar leg `dead-path carriers` can never red. That is a check certifying what it does not check. Built as S3 says, `--check` gates the record inside `drift-audit records` instead. (Re-graded medium to high by the skeptic.)
- **Fix (judged SOUND by the skeptic):** Have `dead_pointers.py --leg` mark the record gateable, or pass it as gateable to `run_signal_leg`. Keep the `SIGNALS` copy report-only, and state that split in S2.
- **Left-shift gate:** a selftest arm for every `run_signal_leg` caller that plants one offender and requires exit 1. A leg that cannot red then fails its own selftest.

### H6. Unit 2's session-start hook renders as `node .../maintain_session.py` (id 30)

- **Where:** spec-2 §2 S5, the fragment (:81-82), and §4 Files touched.
- **What is wrong:** The fragment carries no `interpreter` key. `tools/settings-merge.py` therefore renders the command with its default, `node`. Its closed interpreter set is `("node", "bash")` (:247-248), so `python` cannot be expressed, and `load_fragment` refuses any other value. `settings-merge.py` is not in Files touched. The procmon template the fragment copies is a `.js` hook.
- **Consequence:** This repository's `.claude/settings.json` gets a command that fails at every session start, so the session-start host never ticks. `settings-merge.py --check` and `hosts.py ready session-start` still report the hook wired and ready, so AC8 certifies a hook that cannot run. Adding `"interpreter": "python"` makes `--scaffold` fail instead. A bare `python` would also hit the MS-Store stub that `resolve-python.sh` exists to avoid.
- **Fix (judged SOUND by the skeptic):** Add `tools/settings-merge.py` and its `--selftest` arms to §4. Choose how the hook launches and spell the result in S5's fragment. One option is a `bash` interpreter running a small `maintain-session.sh` that resolves python through `tools/lib/resolve-python.sh`. Another is a widened `_INTERPRETERS` with its own validation. Add an AC that runs the rendered command from the merged settings and observes the hook execute, not only that `--check` reports it wired.
- **Left-shift gate:** a `settings-merge.py --check` arm that refuses a hook whose script extension does not match its interpreter (`.py` under `node`).

### H7. Unit 18 moves `PRODUCT_GLOBS` but leaves the adopter instructions pointing at `drift_signals.py` (id 31)

- **Where:** spec-18 §2 S4 (:102-123), its Readers list, and §4 Files touched.
- **What is wrong:** S4 moves `PRODUCT_GLOBS`, `EVIDENCE_GLOBS` and the `TRACE_*` declarations into `tools/loop/flow_layer.py`. Its Readers list claims to be "found by git grep for the names at base", yet it omits `WIRE-INTO-PROJECT.md:439` and the `Next:` text in `adopt-drift-audit.sh:261`. Both tell adopters to fill `PRODUCT_GLOBS` in `drift_signals.py`.
- **Consequence:** Every adopter who follows the docs fills a declaration that the flow signals no longer read. The flow signals then measure an empty product population from the unfilled seed in `flow_layer.py`. The adopter's own `--check` passes, because it tests existence only.
- **Fix (judged SOUND by the skeptic):**
  - Add `WIRE-INTO-PROJECT.md` (around :439) and `tools/drift-audit/adopt-drift-audit.sh` (around :261) to S4's Readers and to §4, both redirected to `flow_layer.py`.
  - Review `tools/memory-tree/.memory-tree.conf.example:461` and `tools/memory-tree/gen_build_index.py:1962`, which name `EVIDENCE_GLOBS` in refusal text.
  - Add an AC grep that no shipped instruction names `drift_signals.py` as the home of `PRODUCT_GLOBS`.
- **Left-shift gate:** a checklist entry: "a moved declaration whose Readers list was not built from a whole-tree `git grep` including docs and adopter heredocs".

### H8. The red leg reads the newest committed record of any run kind (id 40)

- **Where:** spec-15 §2 S4 (:74-84). Related text is in spec-6 (:26-27, S6 :85-87) and spec-8 S5 (:53-58).
- **What is wrong:** The leg counts `over-pin:` lines only in the newest committed maintenance record. Three cases break that:
  - An event run reads only its event's rows but still writes a record.
  - The security review writes records too, but the skeptic marked this sub-case less certain, because that write goes into the period's own record.
  - Under `record-when: on-finding`, a clean run writes nothing.
- **Consequence:** Under `red-leg`, one `default-branch-red` event run greens the leg while period offenders still stand, so the check certifies what it did not read. Under `on-finding`, the leg stays red after the offenders are cleared, because no clean record replaces the old one.
- **Fix (judged SOUND by the skeptic):**
  - Have the leg read the newest committed record written by a full period run.
  - Define how a record marks its run kind, for example a `**Run:** period|event|security` field that the kind's `fields` form grades.
  - Make `on-finding` still write a record whenever the previous committed record carried `over-pin:` lines.
  - Add two AC4 cases: an event-run record newer than an offending period record keeps the leg red, and a clean run after an over-pin record writes a clean record.
- **Left-shift gate:** a checklist entry: "a gate reading 'the newest record' of a kind written by more than one run shape".

### H9. Unit 9's sweep offender key includes `reads` and `touches`, so it changes every period (id 41)

- **Where:** spec-9 §2 S2, the detail row (:63-66), and S5, the recurrence claim. The risks line is at :226-228.
- **What is wrong:** The detail row is `{"path","population","reads","touches"}`. The I5 offender key is `json.dumps(extract_unlocated(d), sort_keys=True)` (drift_report.py:4007), which drops only line locators (:3734-3743). The read counts differ every period and between nodes.
- **Consequence:** Each period files a new intake rather than a `seen` row. Under `hot-first`, that intake ratifies and places a new patch build, so one path is swept again period after period. S5's claim that "a target unchanged next period adds a seen row" is false. So is the claim that "two nodes ranking one target file one intake".
- **Fix (judged SOUND by the skeptic):** Keep only stable identity in the detail row, `{"path", "population"}`. Carry `reads` and `touches` in the reading's JSON or the intake text, as unit 5 S2 does. Add a criterion: two runs whose read counts differ for one target produce byte-equal offender keys.
- **Left-shift gate:** a drift-audit selftest arm that renders each `[[reading]]`'s offender keys twice over perturbed counts and requires equal keys. Also a checklist entry: "a volatile measurement inside an identity key".

### H10. Unit 11's repeat intake text carries the period, so every cycle files a fresh intake (id 42)

- **Where:** spec-11 §4 "The intake" (:121-126) against §2 S6. The filing mechanism is spec-8 I6 and AC7 (:209-210, :292-294).
- **What is wrong:** The text ends with `cycle: <daily|weekly> <period>`. Unit 8's filing detects a recurrence only by content key, and it requires the text to carry "no value, period or SHA". Unit 8's AC7 names a period in the text as its red case.
- **Consequence:** S6's guarantee that "a cycle whose build has not finished never stacks a second build" fails. Every cycle files a fresh intake, and once ask TOOL-dTendedCadence-21 lands, it also places a fresh repeat build while the previous one is still open. AC6 can pass only on a planted intake.
- **Fix (judged SOUND by the skeptic):** Drop the period from the text. Keep `repeat <path>`, `playbook:`, `pieces:` and `cycle: <kind>`, so the content key depends on the playbook path alone. Add an AC: two `--cycle weekly` runs under `2026-W44` and `2026-W45` produce one intake with two receipts. Fix this together with M7.
- **Left-shift gate:** a shared `intake text` lint, run by every caller of unit 8's filing, that refuses a period, SHA or date pattern in the text.

### H11. `defer dormant` writes a tracked transition record that nothing commits or lands (id 43)

- **Where:** spec-3 §2 S6 (:91-96) and §5 security (:190, :196). The walk's rule is in spec-1 (:98, S6 and F4 :293-299), and dispose is defined in dRankedPlan-4 S3.
- **What is wrong:** `item.maintain.direct` runs `loop_transition.py dispose`, which writes a tracked transition record through `write_transition`. The walk commits nothing, and only the maintenance record has a landing intake. Unit 3 itself admits "the one tracked write is dispose's", and says that tracked content belongs to `maintain.patch`.
- **Consequence:** The move is applied only in the checkout where the cadence runs, and stays uncommitted there. Spec 1 F4 vetoes exactly that outcome for the record. Other nodes and the default branch never see the transition. A clean-base reading still reads the build as dormant, so the move is re-proposed and re-applied every period, and the checkout is left dirty.
- **Fix (judged SOUND by the skeptic):** Route `defer dormant` as `patch`: file a records-only intake per disposable build, whose patch build runs `dispose` and lands it. The alternative is to state the commit-and-land path and price it in §5. Add an AC asserting that `git status --porcelain` is unchanged after `maintain.py` applies `defer dormant`.
- **Left-shift gate:** a walk-level selftest asserting a clean `git status --porcelain` after a full `maintain.py` run over a fixture. The same gate catches M22.

### H12. A regressed offender whose ask has closed is absorbed as a `seen` receipt forever (id 45)

- **Where:** spec-15 §2 S2, the ordering of step (1) open ask and step (2) intake (:55-65). Compare spec-8 (:202-205).
- **What is wrong:** Step (1) matches only a live ask (OPEN, BLOCKED or DEFERRED). When the ask has closed, as fixed then regressed, or as WONTDO, step (2) re-files the same stable text. Its content key is already on record, so the filing only appends a receipt with route `seen`, and nothing re-places the ask. Unit 8 has a `survivor` branch for this case, but only for patch intakes. Unit 15 has none.
- **Consequence:** After an ask for one (reading, offender key) closes, every later breach of that offender is silently absorbed. A regressed offender never reaches triage again, and the run prints `seen`, which reads as handled.
- **Fix (judged SOUND by the skeptic):** Add the closed-ask case to step (1). When the marker is found only in a CLOSED or WONTDO ask, file the breach as a new ask whose text carries the closed ask's id, so the content key differs. The alternative is to route it through `survivor` as unit 8 does. Add an AC2 plant: a CLOSED ask carrying the marker must produce a fresh filing.
- **Left-shift gate:** a checklist entry: "a dedupe keyed on a record whose lifecycle can close, with no closed-state branch".

## Medium

### M1. No walk reads `outside`-scoped readings, so the remote-CI reading never routes (id 3)

- **Where:** spec-1 §2 S4 (:72-73). It conflicts with spec-8 §4 "The row" and "The 27 rows" (:122, :137-138, :170) and spec-16 S6 (:88-89).
- **What is wrong:** Unit 8 defines three scopes and puts `remote_ci_red_streak` in `outside`. Unit 1's period run reads only `scope = "repo"` rows, and unit 16's node pass reads only `scope = "node"` rows.
- **Consequence:** The reading never enters a Maintain run. Its liveness (dead past `maintain.dead-after`, unit 18 S8) is never routed to `item.maintain.file`, so gap-maint-11 stays open. Unit 18 AC8 drives `drift_report.py --readings` directly and so does not notice. (Re-graded high to medium by the skeptic.)
- **Fix (judged SOUND by the skeptic):** State in unit 1 S4 which run reads `outside` rows, most likely the period run, since they are fleet-wide. Add an AC in which a planted `outside` reading, dead past its limit, reaches `item.maintain.file` under `GOV_CADENCE_KEY=<period>`.
- **Left-shift gate:** a drift-audit selftest asserting that every declared `scope` value is read by at least one run.

### M2. Unit 1 AC2's item order contradicts the shared `order_by_needs` tie rule (id 6)

- **Where:** spec-1 §6 AC2 (:232-233) and §4 "The rows" (:162-167, :175).
- **What is wrong:** `read` and `levels` both need only `lease`. `order_by_needs` (dDeclaredLoop-12, govkit.py:936-946) sorts each ready round, so `levels` runs before `read`. AC2 requires lease, read, levels.
- **Consequence:** AC2 cannot pass on a correct build. The builder must either rewrite the shared tie rule or hand-order the walk, and the spec's own Alternatives section rejects hand-ordering.
- **Fix (judged SOUND by the skeptic):** Change AC2 and the §4 sentence to the helper's real order (lease, levels, read, patch, file, record), or assert only that each item runs after its needs.
- **Left-shift gate:** a checklist entry: "an AC asserting a total order the topological helper does not define".

### M3. Unit 3's ACs need the node pass, which builds five orders later (id 7)

- **Where:** spec-3 §2 S5 (:79, :89-90) and §6 AC3/AC4 (:225-232). The build order is in the README (:146, :151).
- **What is wrong:** Unit 3, at order 9, registers `idle_processes_past_ceiling` and `landed_branches_unpruned` with `scope = "node"`, read by unit 16's node pass at order 14. AC3 and AC4 run the period walk, which reads only `repo` rows.
- **Consequence:** At unit 3's build, neither reading reaches `item.maintain.direct`, so AC3 and AC4 cannot pass.
- **Fix (judged SOUND by the skeptic):** Pick one:
  - make the two readings repo-run (or `outside`);
  - move the node pass ahead of unit 3 in the build order;
  - rewrite AC3 and AC4 to call `run_direct_fixes` directly and leave walk routing to unit 16's ACs.
- **Left-shift gate:** a spec-audit check that every AC's command depends only on units at or before its own build order.

### M4. Unit 16 AC7 and unit 9 AC4 run the period walk over node-scoped readings (id 8)

- **Where:** spec-16 §6 AC7 (:281-285) against its own S6 (:96-97) and AC5 (:275). The same issue is in spec-9 S4 (:75) and AC4 (:255-257).
- **What is wrong:** Both ACs run plain `python maintain.py` to file node-scoped readings (`acts_past_ceiling_with_no_outcome`, `maintain.retrofit-heat`). Under the default `every-node`, the period run does not read node rows.
- **Consequence:** Nothing is filed, so neither criterion can pass on a correct build.
- **Fix (judged SOUND by the skeptic):** Run both as the node pass, `GOV_CADENCE_KEY=<period>.<node> python maintain.py --scope node`, or plant `maintain.node-readings = "lease-holder"`.
- **Left-shift gate:** the same order and scope check as M3, extended to compare each AC's invocation scope with the reading's declared `scope`.

### M5. Recurrence is observed two incompatible ways: a second receipt or a `seen` clause (id 9)

- **Where:** spec-8 §2 S7 and AC8 (:209-212, :295-297) and spec-15 (:61-64). These conflict with spec-9 AC4 (:255-257), spec-16 AC7 (:281-284), spec-17 AC7 (:268-271) and spec-11 S6.
- **What is wrong:** Units 8 and 15 record a recurrence with no placed ask by appending a second receipt (AC8 "lists two receipts"). Units 9, 16 and 17 expect "one `seen` row/clause" and "no second receipt". A `seen` clause needs an open ask in a `BACKLOG.md`, and no fixture plants one. The period lease witness also stops two runs in one period.
- **Consequence:** Those ACs contradict unit 8's AC8 and cannot pass on a build of units 8 and 15 as written.
- **Fix (judged SOUND by the skeptic):** Rewrite those ACs to unit 8's observation: a second filing of the same content key appends a receipt and creates no second intake. Plant an `OPEN` ask carrying the marker wherever a `seen` clause is the claim, and run the two periods under distinct keys.
- **Left-shift gate:** a checklist entry: "an AC naming a recurrence observation the owning unit does not produce".

### M6. Unit 15's intake text includes band and probe, so its content key is not stable (id 10)

- **Where:** spec-15 §2 S2, the ask text and its content key (:62-68). It conflicts with spec-8 (:201, :209-210).
- **What is wrong:** S2 says the text carries no period "so its content key is the filing key's". But the clause tail adds `data band <band>`, and in the diagnose band `data probe <probe record>`. Both can change between periods for one offender, and `request.py key` hashes the text bytes.
- **Consequence:** A move from diagnose to act, or a new probe record, files a second intake for one (reading, offender key). AC2 never varies the band.
- **Fix (judged SOUND by the skeptic):** Key the intake on the stable head only (marker, reading, offender key, `accept`), and carry band and probe as receipt or seen data. The alternative is to derive the content key from the filing key. Add an AC2 case where the band changes between two keys and one intake still results.
- **Left-shift gate:** the intake-text lint suggested in H10, extended to refuse band and probe fields in the hashed head.

### M7. Unit 11 files through a unit-8 call that takes no text or filer (id 11)

- **Where:** spec-11 §2 S5/S6 (:67-70) and §4 "The intake" (:121-126). The call is defined in spec-8 S7 (:65-70) and §4 (:199-206).
- **What is wrong:** `write_patch_intake(root, reading, key)` renders a fixed text and hard-codes `--filer item.maintain.patch`. Unit 11 files with its own text and filer `playbook-cycle-<cycle>`, and its text carries `cycle: <cycle> <period>`.
- **Consequence:** The call as specced does not exist. With the period in the text, S6's "`seen`, no second intake" never follows from unit 8's mechanism. AC6 passes only against the stub "recording filer".
- **Fix (judged SOUND by the skeptic):** Have unit 8 expose the filing with text and filer as parameters (I6 already says unit 11's filer is its row's name). Drop the period from unit 11's text (see H10), or key the recurrence explicitly on `(playbook-cycle, <path>)`. Run AC6 against the real filer.
- **Left-shift gate:** a checklist entry: "an AC that passes only against a stub of a sibling's interface".

### M8. Unit 3 adds two signals but not their README signal-table rows (id 12)

- **Where:** spec-3 §2 S5 (:77-90) and S9 (:109).
- **What is wrong:** Unit 3 adds `idle_processes_past_ceiling` and `landed_branches_unpruned` to `SIGNALS` but never adds them to drift-audit's README `## The signals` table. Units 7, 9, 12, 16 and 17 all add their rows.
- **Consequence:** `signal_handkept` (drift_signals.py:215-236) is gateable at tolerance 0 and counts every missing name. That reds the bar, and it does so even before unit 18, since `handkept` is already gateable.
- **Fix (judged SOUND by the skeptic):** Add to unit 3 S9: "the README signal table gains the two rows". Add an AC grepping each name in `tools/drift-audit/README.md`.
- **Left-shift gate:** the existing `handkept` leg already catches this at build. Add a spec-audit checklist entry: "a new `SIGNALS` entry without its README row in Files touched".

### M9. Unit 3 assumes pin 0 for `live_builds_without_activity`, but unit 4 seeds the measured value (id 13)

- **Where:** spec-3 §2 S6 against spec-4 S5 (:76-81).
- **What is wrong:** Unit 3 (order 9) says the reading's "pin is 0, so each dormant build reaches the act band". Unit 4 (order 4) seeds gov's pin for each repo-scoped reading of its five at the measured value when that value is above 0. At base `f4597719`, `memory/LIVE.md` holds 22 dormant rows.
- **Consequence:** Gov's pin will be 22, so `defer dormant` proposes nothing for the builds already dormant. AC6's fixture can pass while the dogfood tree never runs the fix.
- **Fix (judged SOUND by the skeptic):** Settle one answer. Either unit 3 sets that pin to 0 and unit 4 S5 names it as an exception, or unit 3 states that the fix acts only past the measured pin.
- **Left-shift gate:** a checklist entry: "a unit relying on a pin value that an earlier unit seeds differently".

### M10. Units that change drift-audit's shipped bytes name neither the version carriers nor `kit epoch` and `kit version markers` (id 15)

- **Where:** spec-6 §4 Files touched and §7 Gates, and every unit changing `tools/drift-audit/` (units 1, 3-8, 12 and 14-18).
- **What is wrong:** `kit epoch` reds any shipped-byte move that no `KIT_DRIFT_AUDIT_VERSION` commit dates. `kit version markers` (check-kit-versions.sh:347-364) requires the README marker and `tools/workflows/drift-audit-{code,state}.js` meta.version to match. Only units 2, 9, 11 and 13 mention the version, and none of them lists the workflow files.
- **Consequence:** Files touched is each unit's `--dispatch --writes` set. A unit landing a drift-audit change cannot write the carriers, so the bar reds `kit epoch` or `kit version markers` at that landing.
- **Fix (judged SOUND by the skeptic):** Every unit touching `tools/drift-audit/` lists `KIT_DRIFT_AUDIT_VERSION`, the README marker and the two `tools/workflows/drift-audit-*.template.js` sources with their renders. Each also adds `kit epoch` and `kit version markers` to §7. Reconcile this with M16 first: if the lander mints the bump (push-main.sh), only whatever branch-side duty remains should be listed.
- **Left-shift gate:** a spec-audit arm that, for any spec whose Files touched names a kit path, requires that kit's version legs in §7.

### M11. Units 8 and 17 state contradictory `route` value sets (ids 21, 49)

- **Where:** spec-8 §4 "The row" and "The check" (:127, :133-140, :152, :103). It conflicts with spec-17 §2 S11 and AC10 (:123-130, :285-289), spec-9 S4 (:78) and spec-16 (:120, :194, AC6 :277).
- **What is wrong:**
  - Unit 8 admits only `patch` and `file`, and says unit 17 registers `route = "patch"`.
  - Unit 17 says the key's "one value here" is `ask`, refuses any other, and its AC10 refuses `file`.
  - Unit 9 claims to add `patch` to unit 17's key.
  - Unit 16 registers four `route = "ask"` rows.
  - This is the same defect as H3, kept as a separate item at its binding grade. (Id 21 was re-graded high to medium by the skeptic.)
- **Consequence:** Unit 8's `check_reading_rows`, built at order 3, refuses every `ask` row with `<name>: route ask …`, which reds `drift-audit records` when unit 16 or 17 lands. A builder cannot satisfy both specs, and the next builder of a route value is misled about which set holds.
- **Fix (judged SOUND by the skeptic, both findings):** Spec 8, as the row's owner, states the closed set once: `ask | patch | file`. It gives each value's meaning, the default `file` when there is no `fix`, and the "not beside a fix" rule, and its hand-off says spec 17 registers `ask`. Specs 17 and 9 cite the set rather than add values, and spec 17 AC10 is rewritten against the set. Add a spec-8 AC fixture in which a `route = "ask"` row passes.
- **Left-shift gate:** as H3.

### M12. Unit 16's evidence says one node-scoped reading exists when there are four (id 23)

- **Where:** spec-16 §4 Evidence, first sentence (:167).
- **What is wrong:** It calls `signal_dangling_pointers` "the one node-scoped reading at this base". `measure_legs_retried_after_timeout` (drift_report.py:3125-3133) and `fleet_over_budget` (:3245-3250) loop over every git dir, `backlog_stragglers` reads this clone's refs, and spec-8 (:169) registers all four as `node`.
- **Consequence:** A builder or reviewer reasoning from this paragraph will miss that S6's node pass and `derive_node_reading_turn` also govern the bar-retry, fleet-budget and straggler readings. That includes what `unread-nodes:` and the node pass skip under `lease-holder`.
- **Fix (judged SOUND by the skeptic):** List the four node-scoped readings that spec 8's table registers, and state that S6's node pass and turn rule cover them. Add an AC5 plant that holds one of them to the node pass.
- **Left-shift gate:** a checklist entry: "an evidence claim of 'the one X at this base' not backed by a grep of the registry".

### M13. Unit 4 S6's single policy adapter is bypassed by units 2, 6 and 13 (id 26)

- **Where:** spec-13 §2 S2 (:39), spec-2 §2 S3 (:56) and spec-6 §2 S6 (:85), against spec-4 S6 (about :82-92) and PLAY-dOrderedCharter-7 §4 "The policy reads".
- **What is wrong:** Three units write their own policy reader inside drift-audit: `read_review_mode`, the `maintain.events` selector, and `read_record_when`. Unit 4 S6 already defines `read_policy_value` and `PolicyRefused` as the kit's one adapter. Its caller list leaves out units 2, 6 and 13.
- **Consequence:** drift-audit ships four policy readers that will drift on `--explain`, timeout and refusal handling, which breaks the one-adapter contract.
- **Fix (judged SOUND by the skeptic):**
  - Unit 13 S2: call `read_policy_value("maintain.security-review", root)` and map `PolicyRefused` to its `refused` line.
  - Unit 2 S3: call `read_policy_value("maintain.events", root)`.
  - Unit 6 S6 (order 2, before unit 4): either define `read_policy_value` and `PolicyRefused` there, which unit 4 S6 allows ("unless an earlier pass of this build defined it"), with `read_record_when` a one-line caller of it, or re-point `read_record_when` once unit 4 lands.
  - Add units 2, 6 and 13 to unit 4 S6's caller list.
  - Each unit's AC greps for `read_policy_value("<key>"` in its module, as units 15-17 already do.
  - This also closes L2.
- **Left-shift gate:** an idiom-ban arm refusing `policy.py get` subprocess spawns in `tools/drift-audit/*.py` outside the adapter.

### M14. Unit 16 re-derives runlog's "closed" and "has an anomaly" rules instead of calling them (id 27)

- **Where:** spec-16 §2 S2 (:59-60) and §10 (:376-384), against spec-6 S2/S3 (:50-61).
- **What is wrong:** `measure_unrecorded_runs` is "decided by TOOL-dTendedCadence-6's own rule", but the spec never names that rule's seams. Those are `derive_closing_end` and `scan_anomalies`, which carry the four new kinds. §10 names `read_journal` and `resolve_record_path` as "called, never copied", but neither seam.
- **Consequence:** A drift-audit copy of the rule can miss the `refusal`, `ceiling-breach`, `dead-probe` or `red-bar` kinds, or count a `--landed` close differently. Under `on-anomaly`, the reading then files asks on a wrong count.
- **Fix (judged SOUND by the skeptic):** In S2, name and call the seam. Ask runlog's own answer per run, either through `runlog.py record <slug>` without `--write`, or by calling `derive_closing_end(model)` and `scan_anomalies(model)` through the route used for `read_journal`. Add an AC that plants a run whose only anomaly is a `refusal` under `on-anomaly` and asserts it counts.
- **Left-shift gate:** a checklist entry: "a reading 'decided by unit N's rule' with no named callable".

### M15. The security review's base needs a filtered reader that unit 6 does not offer (id 28)

- **Where:** spec-13 §2 S3 (:47-48), against spec-6 §2 S7 (:92-96) and the member defaults (about :196, :221-225).
- **What is wrong:** S3 takes "the newest committed maintenance record carrying one [security-head]" without citing `read_newest_record`. That reader returns only the newest record, with no filter. Unit 6 writes `security-head: none` when the member is missing, so the newest record often answers nothing.
- **Consequence:** The builder writes a second git-history walker in `security_review.py`. Its "newest" rule and its `git show`-not-working-tree discipline can then diverge from the one that units 15 F3 and 6 S7 settled.
- **Fix (judged SOUND by the skeptic):** Extend the existing reader. In unit 6 S7, give `read_newest_record(root, carrying=None)` a field filter that returns the newest committed record whose named line is not `none`. Unit 13 S3 calls `read_newest_record(root, carrying="security-head")` and cites it in §3 Edges and §10. Add a unit 6 AC with two committed records, the later one carrying `security-head: none`, where the filtered call returns the earlier one. See H4.
- **Left-shift gate:** an idiom-ban arm refusing `git log`/`git show` walks over the maintenance home outside `maintenance.py`.

### M16. Units 2, 11 and 13 hand-bump kit versions on the branch, against the lander's mint (id 32)

- **Where:** spec-2 §2 S9 and §4 (:113, :184), spec-11 S7 (:81-82, :148, :152) and spec-13 S9 (:109, :175).
- **What is wrong:** Each spec has the branch move `KIT_DRIFT_AUDIT_VERSION` "once per pass". Unit 11 also moves `KIT_UNATTENDED_VERSION`. Each lists only the constant's file. push-main.sh:26-31 says kit versions are minted at the lander and "a branch therefore owes no bump".
- **Consequence:** A bump of `drift_report.py` alone leaves five carriers at 1.30: the README marker and four `tools/workflows/drift-audit-*.js` and `.template.js` files. That reds `kit version markers`. For unattended, `check-unattended.sh`, `check-pass-order.sh`, `check-brief-recorded.sh` and every `*.template.md` marker stay behind. Per-pass bumps also stack with `govkit.py mint`, so the version moves by an arbitrary amount per landing.
- **Fix (judged SOUND by the skeptic):** Remove the "moves once per pass" sentence and the version rows from specs 2, 11 and 13. State that the lander mints the bump (`govkit.py mint`, TOOL-aMendedFleet-65) and that the build owes none. If a branch bump is kept, list every carrier that `write_version_carriers` and check-kit-versions.sh read, and name `kit version markers` in §7. Reconcile with M10.
- **Left-shift gate:** a spec-audit grep refusing "KIT_*_VERSION" moves in a spec's Files touched, citing push-main.sh.

### M17. Unit 6's replacement text pushes the unattended SKILL.md render past its size cap (id 33)

- **Where:** spec-6 §2 S5, Readers by value (:68-78), and §7.
- **What is wrong:** S5 claims the renders' bytes "only fall". But it replaces the 78-byte command line at SKILL.md:159 with a longer sentence. `.claude/skills/unattended/SKILL.md` is at 10237 bytes against a 10240 cap (template-size-limits.txt:154).
- **Consequence:** The render crosses its cap and `unattended skill size`, which §7 lists, goes red at the unit's close. The spec's claim tells the builder not to look.
- **Fix (judged SOUND by the skeptic):** Correct S5's by-value line to 10237/10240. Either delete the `## Record the run` section outright, or name the bytes trimmed elsewhere. Add an AC asserting that `wc -c .claude/skills/unattended/SKILL.md` stays at or under 10240.
- **Left-shift gate:** a checklist entry: "an edit to a capped render with no headroom figure in the spec".

### M18. Unit 10's new rendered agent is not declared in `method-carriers.txt` (id 34)

- **Where:** spec-10 §4 Files touched and §7.
- **What is wrong:** `.claude/agents/gov-maintainer.md` will carry the charter line `A build of more than one pass: memory/guides/BUILD-METHOD.md`, as all 9 rendered agents do (method-carriers.txt:25-33). The spec adds no row and names no `method carriers` leg.
- **Consequence:** `check-method-carriers.sh` check 3 fails on an undeclared mention, which reds the bar at the unit's close.
- **Fix (judged SOUND by the skeptic):** Add `memory/project/method-carriers.txt`, with one `.claude/agents/gov-maintainer.md · rendered role agent; ...` row, to §4. Add `method carriers (every pointer declared)` to §7.
- **Left-shift gate:** a checklist entry: "a new rendered agent or charter carrier with no method-carriers row".

### M19. Unit 18 moves the `TRACE_CUTOFF` comment that `method-carriers.txt` declares (id 35)

- **Where:** spec-18 §2 S4 (:102-105) and §4 Files touched (:281-308).
- **What is wrong:** The `TRACE_CUTOFF` block names `memory/guides/BUILD-METHOD.md` (drift_signals.py:44), and `method-carriers.txt` declares a row for it. The block moves to `tools/loop/flow_layer.py`, but `method-carriers.txt` is not in §4 and §7 names no leg.
- **Consequence:** `check-method-carriers.sh` fails twice: check 3 on the undeclared mention in `flow_layer.py`, and check 4 on the stale `drift_signals.py` row.
- **Fix (judged SOUND by the skeptic):** Add `memory/project/method-carriers.txt` to §4. Re-key the row to `tools/loop/flow_layer.py`, and to the template too if the template keeps the comment. Name `method carriers (every pointer declared)` in §7.
- **Left-shift gate:** as M18, extended to any moved block that carries a method pointer.

### M20. New gate legs and a new hook are claimed by no codebase-map dossier (id 36)

- **Where:** spec-15 §4 Files touched (`maintain breach record`, :193), spec-2 (the SessionStart hook, :86, :185) and spec-18 S5 (six new legs).
- **What is wrong:** Each spec adds a key to a codebase-map inventory, but none lists the dossier that claims it, and `baseline.toml` refuses new keys (test_codebase_map.py:9-15). Spec 18 lists only `features/playbook.md` and `generated/`.
- **Consequence:** `codebase-map coverage + freshness`, an unguarded leg, reds on each unclaimed key. Specs 15 and 2 also leave `memory/map/generated/inventories.json` and `MAP.md` stale.
- **Fix (judged SOUND by the skeptic):**
  - Spec 15: add a dossier claim for `maintain breach record`, and re-render `memory/map/generated/`.
  - Spec 2: claim the hook key in a dossier, as `process-monitor.md` claims its hook, and re-render.
  - Spec 18: claim the two memory legs in `memory/map/features/memory-tree-hygiene.md` and the two flow legs in the loop kit's dossier.
  - Each spec names `codebase-map coverage + freshness` in §7.
- **Left-shift gate:** a spec-audit arm: a spec whose Files touched names `tools/gate-legs.json` or a settings fragment must also name a `memory/map/features/` file.

### M21. Edits to watched files owe a kickoff-manifest re-stamp that no unit budgets (id 37)

- **Where:** spec-15 §4 and §7 (:193), spec-7 (:79-85) and spec-18 (all three edit `tools/gate-legs.json`), and spec-9 (:195, which edits `skills/session-kickoff/manifest-check.sh`).
- **What is wrong:** Both files are on the watch list in `memory/guides/SESSION-KICKOFF.md`'s audit block. No spec lists the re-stamp or names `kickoff-manifest ratchet`.
- **Consequence:** `manifest-check.sh` C5 (:1524-1541) fails, which reds `kickoff-manifest ratchet` until someone audits the manifest's claims and re-stamps `last-audit`. That audit is unbudgeted work.
- **Fix (judged SOUND by the skeptic):** Add `memory/guides/SESSION-KICKOFF.md` (the §B claims re-checked and `last-audit` re-stamped) to §4 of specs 7, 9, 15 and 18, and name `kickoff-manifest ratchet` in their §7. The alternative is to assign the re-stamp to one closing unit of the build.
- **Left-shift gate:** a spec-audit arm that intersects each spec's Files touched with the manifest's watch list and requires the re-stamp.

### M22. Unit 15's `seen` clause is a tracked edit with no commit route (id 44)

- **Where:** spec-15 §2 S2 step (1) (:55-61) and §5 security (:214-216).
- **What is wrong:** The walk re-renders a `SCOPE` row in another home's tracked `BACKLOG.md`. §5 calls this "the one tracked write outside an intake", but no AC or section names a commit or landing route, and the walk commits nothing (spec-1:98).
- **Consequence:** The clauses never reach the default branch. A second node's `git grep` dedupe sees none and adds its own, and the walk leaves a tracked file dirty.
- **Fix (judged SOUND by the skeptic):** Carry the `seen` clause through the same records-only patch intake that lands the maintenance record, or record recurrence only as an intake receipt. State in §5 which commit lands the row. Add an AC asserting the walk leaves `git status --porcelain` empty.
- **Left-shift gate:** as H11, a clean `git status --porcelain` after a full walk.

### M23. The record's landing intake carries the readings JSON through a redacting, capped writer (id 46)

- **Where:** spec-1 §2 S6, the record's landing intake (:95-98), with spec-6's stdin grammar (:221-225) and dWellOiledMachine-4 S2 (:54).
- **What is wrong:** The intake carries "the record's key, its base and its readings as JSON" so the patch build can re-write the record. The intake writer redacts through `render_redacted` and cuts at `INTAKE_CAP_BYTES` (65536), and spec 6 itself expects records to pass 64 KiB. Neither spec states an exit for empty, non-JSON or incomplete stdin.
- **Consequence:** A period with many offenders produces a truncated or redacted payload. The patch build then lands no record, or lands one whose `over-pin:` lines were silently cut, and the red leg (unit 15) and the next security base (unit 13) read that record as truth.
- **Fix (REJECTED by the skeptic; the skeptic's corrected fix):** Carry only the record's key and base, plus a digest of the readings, in the landing intake. Have the patch build re-derive the readings at that base with `drift_report.py --readings` before `maintenance.py write`. Have unit 6 S6 exit 2 on stdin that is empty, not JSON, or missing required members. Add an AC with a 70 KiB readings set that lands intact.
- **Left-shift gate:** a checklist entry: "a machine payload routed through a human-text channel that redacts or caps".

### M24. The clean-base scratch worktree path is fixed by sha alone and leaks on a kill (id 47)

- **Where:** spec-18 §2 S7 (:148-154) and §5 security (:325).
- **What is wrong:** The worktree sits at `<git-common-dir>/maintain-read/<sha12>` and is removed on context-manager exit. Unit 1 S4 runs `--readings` as a bounded subprocess that a timeout kills, and a kill skips that exit. A period run and an event run at one base hold different leases.
- **Consequence:** A killed reading leaves the worktree registered. The next run's `git worktree add` then fails on the existing path, and the reading goes dead. Two concurrent runs collide, and one run's cleanup removes the tree the other is reading.
- **Fix (judged SOUND by the skeptic):** Suffix the path with the pid or a random token, as post-merge does (`gate-pm.<pid>`). Prune or remove stale `maintain-read/*` entries before adding. State the kill case in §5. Add an AC7 case with a pre-existing directory at the path.
- **Left-shift gate:** a checklist entry: "a scratch path keyed on content alone, with no pid or token".

### M25. `closed_runs_with_no_run_record` counts unbound runs, which never get a record (id 48)

- **Where:** spec-16 §2 S2, the population (:55-62).
- **What is wrong:** The population is every closed run that owes a record under `per-run` or `on-anomaly`, with no exclusion for runs that served no spec unit. Spec 6 F2 leaves those runs unrecorded (record.py:1183-1186, runlog.py:424-429).
- **Consequence:** Every unbound closed run reads as missing and is filed as an ask. Every later period then adds a `seen` clause for a record that will never exist.
- **Fix (judged SOUND by the skeptic):** Add "and that served a spec unit (`derive_serves`)" to S2's population. Add an AC2 plant of an unbound closed run that reads `0 of 0`.
- **Left-shift gate:** M14's fix, calling runlog's own rule, removes the class.

### M26. `idle_processes_past_ceiling` has no detail rows, so a reap always reads `fixed` (id 50)

- **Where:** spec-3 §2 S5 (:80-82) against S4 (:72-74).
- **What is wrong:** The reading is the dry sweep's `targets` count alone (reap.py:413-416 prints only counts). Offender keys come only from detail rows (render_drift_offenders, :3985-4022). S4 judges `fixed` by an empty offender set.
- **Consequence:** After a reap the outcome is always `fixed`, even when targets survive, and survivors are never filed. Spec-8 AC5, "every over one carrying at least one key", also reds on this row.
- **Fix (REJECTED by the skeptic; the skeptic's corrected fix):** Give `measure_idle_processes` one detail row per reap target, keyed by a stable identity such as name and cmdline rather than the pid, which is not stable across periods. S4's empty-offender-set test and the survivor filing then both work. Add an AC3 case where a planted target survives the reap and is filed under its key.
- **Left-shift gate:** spec-8 AC5 already catches it at build. Add a checklist entry: "a count-only reading routed to a fix judged by offender set".

### M27. A hand-over re-runs the whole walk and repeats its side effects (id 51)

- **Where:** spec-1 §2 S2 (:58-59), against spec-8 (:210-216).
- **What is wrong:** An item that raises exits 1, the lease is released as a hand-over, and "the next wake runs the period again" from the start. Unit 8 relies on "the period lease's witness stops a second run of the same period", but a hand-over is exactly that second run. No spec states a re-run contract.
- **Consequence:** Each re-run files another receipt for every standing offender, each counted as a recurrence, and re-applies direct fixes.
- **Fix (judged SOUND by the skeptic):** State the re-run contract. Either key each filing receipt by (period key, offender) so a re-run within one period adds nothing, or record per-item completion under the lease and resume after the last completed item. Add an AC in which a stub `file` body raises, the walk re-runs, and one receipt per offender remains.
- **Left-shift gate:** a checklist entry: "a retry path that re-executes side-effecting steps without an idempotence key".

### M28. Unit 12's `git blame` has no revision, so a dirty line yields the all-zero sha (id 52)

- **Where:** spec-12 §2 S3 (:52-54), under `maintain.reading-tree: worktree`.
- **What is wrong:** S3 says the notes are read "at HEAD" but spells the blame as `git blame --porcelain` per file with no revision. That form blames the working file, so an uncommitted line reports `0000000…`.
- **Consequence:** Under `worktree`, where the node's checkout is often dirty, `git show X:path` fails and `X..HEAD` is not a valid range. The member is mis-judged, or the reading goes dead.
- **Fix (judged SOUND by the skeptic):** Spell the blame as `git blame --porcelain HEAD -- <file>`, and the scan as reading HEAD's blobs. Add an AC5 case with an uncommitted edit to the note line.
- **Left-shift gate:** an idiom-ban arm refusing `git blame` without an explicit revision in `tools/drift-audit/*.py`.

### M29. Security findings keyed `<path>:<line>` split on moved lines and merge at one line (id 53)

- **Where:** spec-13 §2 S5 (:71-75).
- **What is wrong:** A finding's offender key is `<path>:<line>` alone. Unit 15 S2 hashes it verbatim. drift_report.py:3999-4001 drops trailing `:<digits>` for exactly this reason.
- **Consequence:**
  - A finding re-reported after unrelated edits move its line files a second ask, which contradicts S5's own `seen` claim.
  - Two distinct findings at one line fold into one ask, and the second is lost.
- **Fix (judged SOUND by the skeptic):** Key a finding by path plus a normalized title, or by the finding's own id where the harness gives one, never by line number. Add an AC7 plant of one finding re-reported at a shifted line and two findings at one line.
- **Left-shift gate:** as H9, a selftest that perturbs locators and requires stable keys.

## Low

### L1. Unit 16 names a `kind` for `standing_directives_not_promoted` that no unit declares (id 16)

- **Where:** spec-16 §2 S7 (:111-113).
- **What is wrong:** The row's `kind` is "the one TOOL-dTendedCadence-4 declares for the auto-memory population". Unit 4 declares no such kind, and unit 7 S5 says that row carries no `kind`.
- **Consequence:** The builder has no value to write, so the owner derivation and admission are undecidable from the text.
- **Fix (judged SOUND by the skeptic):** State the value. Either it has no `kind`, so a node-scoped row derives `layer.runtime` under unit 4 S1, or name a registry kind.
- **Left-shift gate:** a checklist entry: "a value cited from a sibling spec that the sibling does not state".

### L2. Unit 4 S6 calls its adapter the kit's only one, but units 2, 6 and 13 add their own (id 17)

- **Where:** spec-4 §2 S6.
- **What is wrong:** S6 says every drift-audit caller uses `read_policy_value` and none writes a second adapter. Units 6 (`read_record_when`), 13 (`read_review_mode`) and 2 (the `maintain.events` selector) each spawn their own.
- **Consequence:** The kit ends with four policy readers, against the rule that units 1, 3, 9 and 14-18 rely on.
- **Fix (judged SOUND by the skeptic):** Have units 6, 13 and 2 call `read_policy_value("<key>", root)`. Because unit 6 precedes unit 4, either move the adapter into unit 6 or let unit 4 re-point `read_record_when`. M13 carries the same fix in full.
- **Left-shift gate:** as M13.

### L3. Unit 18 S11 leaves the five moved signals ambiguous in the README signal table (id 18)

- **Where:** spec-18 §2 S11 (:184-186), against S4, S6 and AC3.
- **What is wrong:** S6 removes the five `[[reading]]` rows, and S4 has `handkept` compare the README table with the `[[reading]]` names. S11 says the "signal table points at the three legs for the five", which reads as the rows staying in the table.
- **Consequence:** If the rows stay, `read_signal_table_names` (drift_signals.py:226-227) counts 5 extras and AC3 fails.
- **Fix (judged SOUND by the skeptic):** Say in S11 that the five rows leave the table and that the pointer to the three legs is prose outside it.
- **Left-shift gate:** the `handkept` leg catches it at build. No new gate is needed.

### L4. The unit that creates `help/maintain.md` cannot write its `help/README.md` line (ids 19, 38)

- **Where:** spec-15 §2 S10 and §4 (:113, :199), against spec-4 §4 Files touched (:217), with spec-1, spec-14 and spec-18.
- **What is wrong:** S10 says the page and its index line are written "by the first unit of this build whose build pass reaches them". By build order that unit is unit 4, and unit 4's Files touched lists `help/maintain.md` but not `help/README.md`. Units 14 and 18 omit it too. The page does not exist today.
- **Consequence:** The page lands unindexed until order 7, or unit 4's builder writes a file its spec does not declare. The effect is on docs only.
- **Fix (judged SOUND by the skeptic, both findings):** Give the page creation and the index line to unit 4: put `help/README.md` in its §4, with a criterion grepping the line. Change unit 15 S10 to "the line exists", editing it rather than conditionally creating it.
- **Left-shift gate:** a checklist entry: "a conditional 'first unit that reaches it' write with no named owner".

### L5. Unit 17 gives two behaviours for a refused policy read (id 20)

- **Where:** spec-17 §2 S4 (:75-76) against §5 error states (:224-225).
- **What is wrong:** S4 says a refused read takes "the default `file` with its `NOTE:` line". §5 says it is "`not asked`, naming it".
- **Consequence:** The builder has two behaviours for one case, and no criterion decides between them.
- **Fix (judged SOUND by the skeptic):** Keep S4's answer, which matches unit 15 F5. Add an AC4 case with the policy kit removed.
- **Left-shift gate:** none beyond M13's single adapter, which fixes the refusal behaviour in one place.

### L6. Unit 10 says the workflows registry names no entry count, but four sites say "ten" (id 22)

- **Where:** spec-10 §4 "Files touched (estimate)", the `tools/roles/workflows.toml` line (:186).
- **What is wrong:** The claim "its header comment names no count of entries" is false. The count "ten" appears at `workflows.toml:1` and `:4`, `check_roles.py:31`, and `tools/roles/README.md:4` and `:275`. Unit 10 S3 also adds an eleventh house overlay.
- **Consequence:** Adding the eleventh workflow leaves "ten" in the header, the checker's rule text and the user-facing README. (Re-graded medium to low by the skeptic, because the stale counts are in comments and docs.)
- **Fix (judged SOUND by the skeptic):** Remove the false claim. Add the count sites to Files touched. Add a criterion that `grep -n -i 'the ten\|ten declared\|one of the ten' tools/roles` finds no stale count after landing.
- **Left-shift gate:** a checklist entry: "a spelled-out entry count in a registry header or README".

### L7. Unit 15 cites the wrong lines for `--check`'s over-pin status (id 24)

- **Where:** spec-15 §4 Evidence (:23, :152).
- **What is wrong:** It cites `drift_report.py:4404-4417`, which are the not-asked, empty and DEAD PROBE branches. The over-pin lines are at `:4427-4438`, as units 14 and 4 correct.
- **Consequence:** A misdirected citation only, with no effect on behaviour.
- **Fix (judged SOUND by the skeptic):** Change the citation to `drift_report.py:4427-4438`.
- **Left-shift gate:** none; a citation slip.

### L8. Unit 5's rejected alternative miscounts the feature dossiers (id 25)

- **Where:** spec-5 §4 "Alternatives rejected", last bullet (:138).
- **What is wrong:** It says the alternative "rewrites 31 dossiers". The tree holds 32 feature dossiers, and 31 is the packet's older count.
- **Consequence:** A wrong count in a rejected alternative only, with no effect on behaviour.
- **Fix (judged SOUND by the skeptic):** Say 32, or drop the number: "rewrites every dossier's content".
- **Left-shift gate:** none; a count slip.

### L9. Unit 13 rebuilds the scratch-worktree context manager that unit 18 specs (id 29)

- **Where:** spec-13 §2 S4 (:56) and §10 (:316), against spec-18 S7 (:148ff).
- **What is wrong:** `security_review.py` builds its own detached scratch worktree under the git common dir with cleanup, citing only the shell helper `add_scratch_worktree`. Unit 18 S7, eleven orders earlier in the same kit, specs that logic as the context manager `resolve_reading_tree`.
- **Consequence:** Two Python copies of the logic can drift in cleanup, and one may leak worktrees.
- **Fix (judged SOUND by the skeptic):** In unit 18 S7, factor the worktree half into a context manager in `drift_report.py`, for example `add_detached_worktree(root, sha, subdir)`, which `resolve_reading_tree` calls. Unit 13 S4 calls it with `head` and subdir `security-review`, and cites unit 18 S7 in §3 Edges and §10. Carry M24's pid-suffix fix into the shared helper.
- **Left-shift gate:** an idiom-ban arm refusing `git worktree add` in `tools/drift-audit/*.py` outside the shared helper.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=53 confirmed=53 refuted=0 unverified=0 blocker=0 high=13 medium=30 low=10 agents=11 out-tokens=233817

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-6.md:section 4 "The maintenance record" (key grammar), against TOOL-dTendedCadence-2 S1/AC3 and TOOL-dTendedCadence-16 S6 | high | high | confirmed | Unit 6 spec lines 203-206 list only the period key and `<event>.<sha12>`, held to `^\d{4}-(\d{2}-\d{2}\|W\d{2})$` or `^[a-z0-9][a-z0-9-]*\.[0-9a-f]{12}$`, and anything else exits 2. Unit 2 AC3 (spec-2:241-243) derives `s-` plus 12 hex, which has no dot and so fails both patterns. Unit 16 S6 (spec-16:93-94) hands `item.maintain.record` the key `<period>.<node>`, and a node name is not 12 hex, so that fails too. grep found no other key family named anywhere in unit 6. The node pass is the default `every-node` path, so its record is refused. | sound | - |
| 2 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-6.md:section 4 "The maintenance record" (the `over-pin:` derivation), against TOOL-dTendedCadence-15 S3/S4, -16 S8/AC7, -17 S11/AC7, -14 S4 | high | high | confirmed | spec-6:224-225 says the `over-pin:` lines are 'the `keys` of every reading with `over` true'. Unit 8 S5 (spec-8:55-56) defines `over` as live, pinned and over its pin. Unit 14's log band (spec-14:127, S4) is over the pin with nothing filed, and unit 17 S11 (spec-17:123-129) and unit 16 S8 (spec-16:119-126) route `ask` rows to `filed`/`seen` and say they are never an over-pin line. The stdin carries a `route` field (spec-6:222), yet the derivation ignores it. Unit 15 S4 counts every over-pin line and exits 1 above 0. | sound | - |
| 3 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md:section 2 S4, against TOOL-dTendedCadence-8 section 4 "The row"/"The 27 rows" and TOOL-dTendedCadence-16 S6 | high | medium | confirmed | Unit 8 (spec-8:122, :137-138, :170) puts `remote_ci_red_streak` in scope `outside`. Unit 1 S4 (spec-1:72-73) reads repo records in the period run and leaves node records to the node pass. Unit 16 S6 (spec-16:88-89) runs over the `scope = "node"` rows alone. grep over units 1, 16 and 18 found no run that reads `outside` rows. Unit 18 S8 sets `live = "gh"` on that row, but no walk routes it. | sound | - |
| 4 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-17.md:section 2 S11 and section 6 AC10, against TOOL-dTendedCadence-8 section 4 "The row"/"The check"/AC3, TOOL-dTendedCadence-9 S4, TOOL-dTendedCadence-16 S7 | high | high | confirmed | spec-8:127 gives `route` the values `patch \| file`, only on a row with no fix, and the check (:152) refuses `route` outside `patch` and `file`. spec-17:123-125 says the reader admits `route` with the one value `ask`, refuses any other, and that unit 9 adds `patch`. spec-17 AC10 (:285) refuses `route = "file"`. spec-9:78-79 says it adds `patch` to unit 17's key. The §3 edges run 17→9 and 17→16 (spec-17:151-152, spec-9:147, spec-16:158). Unit 8's hands-off to 17 (:103) even names `route = "patch"`. As written, unit 8's check would refuse unit 16's and unit 17's `ask` rows. | sound | - |
| 5 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-13.md:section 2 S3 and S6, against TOOL-dTendedCadence-6 S6 and TOOL-dTendedCadence-1 S6 | high | high | confirmed | spec-13 S1 (:32-37) makes `security_review.py run` its own `[[adapter]]` cadence row. S3 (:47-48) reads the base from the newest COMMITTED record carrying `security-head`. S6 (:78-84) writes the head through unit 6's writer, and grep found no intake or landing in unit 13. spec-6:89-91 says the writer commits nothing and that only the Maintain walk files the records-only landing intake (spec-1:95-98). grep for `security` in spec-1 shows Maintain never carries a security-head. So the head is never committed, and every run falls back to the start of the period. Both programs also key a weekly record `2026-W44`. | sound | - |
| 6 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md:section 6 AC2 and section 4 "The rows" | medium | medium | confirmed | In unit 1's needs table (spec-1:162-167), `read` and `levels` both need only `lease`. dDeclaredLoop-12:156-160 defines `order_by_needs` as govkit's `derive_install_order` loop. govkit.py:936-946 computes each round's ready set with `sorted(...)` and extends it as a batch. Round 2 is therefore sorted(['item.maintain.levels','item.maintain.read']), with levels first. spec-1:175 and AC2 (:232-233) require lease, read, levels. | sound | - |
| 7 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-3.md:section 2 S5 and section 6 AC3/AC4 (ordering) | medium | medium | confirmed | spec-3:79 and :89-90 register both readings with `scope = "node"`, read by unit 16's node pass. AC3 and AC4 (spec-3:225-232) run `GOV_CADENCE_KEY=2026-11-01 python maintain.py`, the period walk, which reads only repo records (spec-1:72-73). README build order: unit 3 is order 9 (:146) and unit 16 is order 14 (:151). No fixture note in AC3 or AC4 defers them. | sound | - |
| 8 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-16.md:section 6 AC7 (and TOOL-dTendedCadence-9 AC4) | medium | medium | confirmed | spec-16 AC7 (:281-285) runs `python maintain.py` twice over the node fixture for the node-scoped `acts_past_ceiling_with_no_outcome`. S6 (:96-97) says that under `every-node` the period run does not read node rows, and its own AC5 red-when (:275) reds a period run that reads them. spec-9 S4 (:75) registers `scope = "node"`, and AC4 (:255-257) likewise runs `python maintain.py`. Neither plants `lease-holder` or runs `--scope node`. | sound | - |
| 9 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-8.md:section 2 S7/AC8, against TOOL-dTendedCadence-9 AC4, -16 AC7, -17 AC7, -11 S6 | medium | medium | confirmed | spec-8:209-212 says a second filing appends one receipt, which is the recurrence's `seen` row. AC8 (:295-297) expects two receipts. spec-15:61-64 files the same way when no open ask carries the marker. spec-9 AC4 (:255-257) expects 'one `seen` row ... and writes no second receipt'. spec-17 AC7 (:268-271) and spec-16 AC7 (:281-284) expect a `seen` clause on an ask and no second receipt, but no planted open `BACKLOG.md` ask exists for step (1) to find. Both runs also lack distinct period keys. | sound | - |
| 10 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:section 2 S2 (the ask text and its content key) | medium | medium | confirmed | spec-15:62-63 says the text carries no period 'so its content key is the filing key's'. Yet :65-68 add `data band <band>` and, in the diagnose band, `data probe <probe record>` to the tail. spec-8:201 and :209-210 take the content key from `request.py key` over the text bytes. A band change from diagnose to act, or a new probe record, changes the bytes, so a second intake is filed whenever no placed ask carries the marker yet. | sound | - |
| 11 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-11.md:section 2 S5/S6 and section 4 "The intake", against TOOL-dTendedCadence-8 S7 | medium | medium | confirmed | spec-8 S7 (:65-70) and §4 (:199-206) define `write_patch_intake(root, reading, key)`. It renders its own text and hard-codes `--filer item.maintain.patch`, so no parameter takes a caller's text or filer. spec-11 S5 (:67-70) files through that filing with filer `playbook-cycle-<cycle>` and its own text, and §4 (:121-126) puts `cycle: <daily\|weekly> <period>` in the text. A new period then gives a new content key, so S6's `seen`-with-no-second-intake never follows from unit 8's mechanism. AC6 runs against a recording filer (:232). | sound | - |
| 12 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-3.md:section 2 S5 and S9 (README signal table) | medium | medium | confirmed | spec-3 S5 (lines 77-90) adds `idle_processes_past_ceiling` and `landed_branches_unpruned` to `SIGNALS`. S9 (:109) only has the README name `maintain_fixes.py` and adds no signal-table rows. Units 7, 9, 12, 16 and 17 each say their README signal table gains the row. I checked the gate source: drift_signals.py:215-236 reads the `## The signals` table against `ctx.signal_names`, and drift_report.py:4320 builds that from SIGNALS. signal_handkept returns tolerance 0 and gateable True, and counts every missing name. So the two missing rows red the check. That happens even before unit 18, since `handkept` is already gateable today. | sound | - |
| 13 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-3.md:section 2 S6, against TOOL-dTendedCadence-4 S5 | medium | medium | confirmed | spec-3 is order 9 and spec-4 is order 4. spec-3 S6 says the reading 'is pinless at this base' and that 'its pin is 0'. spec-4 S5 (:76-81) seeds a gov pin for each repo-scoped one of the five at its measured value when that value is above 0, and `live_builds_without_activity` is one of the five. At base f4597719, `git show f4597719:memory/LIVE.md \| grep -c '\| dormant \|'` printed 22. So unit 4 pins it at 22, and the builds already dormant never reach the act band unless unit 3 overrides that pin. The two specs disagree. | sound | - |
| 14 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-7.md:section 2 S2 against S3 | medium | high | confirmed | spec-7 S2 (:56-57) says the `dead_paths_in_served_text` record has `gateable` false, 'so `drift_report.py --check` gates nothing of it'. S3 calls it 'its one gateable signal at bound 0, so the exit is 1'. spec-18 S1 says `run_signal_leg` returns 1 only 'when a gateable record is over or dead'. Built as S2 says, the kept merge-bar leg `dead-path carriers` can never red. That is a check certifying what it does not check, reached through an internal contradiction. | sound | - |
| 15 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-6.md:section 4 Files touched / section 7 Gates (and every unit that changes drift-audit's shipped bytes) | medium | medium | confirmed | A grep for KIT_DRIFT_AUDIT_VERSION or 'kit epoch' over the specs matches only units 2, 9, 11 and 13 (orders 18, 15, 16 and 17). Units changing drift-audit at earlier orders (6, 8, 4, 14, 18, 15, 3, 7 and others) list neither the bump nor the legs. govkit.py cmd_epoch reds any shipped-byte move that no version-value commit dates. check-kit-versions.sh:347-364 needs the README marker and tools/workflows/drift-audit-{code,state}.js meta.version to equal the constant, and even the four bumping units do not list those workflow files in Files touched. A pass gated before order 15 reds `kit epoch`. | sound | - |
| 16 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-16.md:section 2 S7 (`standing_directives_not_promoted` row) | low | low | confirmed | spec-16 S7 (:111-113) takes the `standing_directives_not_promoted` kind from 'the one TOOL-dTendedCadence-4 declares for the auto-memory population'. A grep of spec-4 finds no such kind: its only mention of dangling_pointers concerns tolerance and pins. spec-7 S5 says that row carries 'no `kind`'. So the value is not stated, although no `kind` plus node scope would derive `layer.runtime` under unit 4 S1. | sound | - |
| 17 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-4.md:section 2 S6 ('drift-audit's one policy adapter') | low | low | confirmed | spec-4 S6 says every later drift-audit caller calls `read_policy_value` and none writes a second adapter. spec-13 S2 (:38-40) instead describes `read_review_mode` as its own bounded `policy.py get` subprocess through an inline `resolve_kit_dir`, with its own exit-2 message. spec-2 S3 (:56-57) spawns its own `policy.py get maintain.events` subprocess. Neither is in unit 4's list of callers. spec-6's `read_record_when` precedes unit 4 and says only 'through I2'. | sound | - |
| 18 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-18.md:section 2 S11 against S4/S6 and AC3 | low | low | confirmed | spec-18 S6 removes the five `[[reading]]` rows. S4 has `handkept` compare the README `## The signals` first-column names with the `[[reading]]` names. S11 (:184-186) says the 'signal table points at the three legs for the five', which reads as rows kept in the table. Each such row would count as an extra in `read_signal_table_names` (drift_signals.py:226-227), and the specs do not settle it. | sound | - |
| 19 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:section 2 S10, against TOOL-dTendedCadence-4 section 4 Files touched | low | low | confirmed | spec-15 S10 has the first unit to reach the page write it and its `help/README.md` line. Among the help files the specs list, only spec-15 (:199, order 7) names `help/README.md`. spec-4 (:217, order 4) and spec-1, 14 and 18 list `help/maintain.md` without it. `ls help/` shows no maintain.md today. So the page is created before any unit with write rights to the index. | sound | - |
| 20 | coherence | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-17.md:section 2 S4 against section 5 error states | low | low | confirmed | spec-17 S4 (:75-76) says 'A refused read takes I2's answer, the default `file` with its `NOTE:` line'. Section 5 (:224-225) says 'a refused policy read: `not asked`, naming it'. These are two behaviours for one case, and no criterion settles which applies. | sound | - |
| 21 | grounding | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-8.md:section 4 "The row" and "The check" (the `route` key) | high | medium | confirmed | spec-8 :127 reads `optional: patch \| file`. Its check table at :152 refuses a `route` outside `patch` or `file`, and :103 says unit 17 registers `route = "patch"`. spec-17 S11 says the reader admits `route` with the one value `ask`, and that unit 9 adds `patch`. spec-16 :120, :194 and AC6 (:277) register four rows with `route = "ask"`. Unit 8, at order 3, would refuse them. The conflict surfaces as a red at landing, so it is contained. | sound | - |
| 22 | grounding | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-10.md:section 4 "Files touched (estimate)", the `tools/roles/workflows.toml` line | medium | low | confirmed | The grep printed workflows.toml:1 ('the ten workflows') and :4 ('one of the ten'), check_roles.py:31 ('a missing name of the ten'), README.md:4 ('ten declared WORKFLOWS') and README.md:275 ('The ten house overlays'). tools/roles/house holds ten overlay .md files, and unit 10 S3 adds gov-maintainer.md as an eleventh, so that count goes stale too. spec-10 :186's claim 'its header comment names no count of entries' is false. The stale counts are in comments, a docstring and docs, with no effect on behaviour. | sound | - |
| 23 | grounding | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-16.md:section 4 Evidence, first sentence | medium | medium | confirmed | Spec-16:167 reads 'The one node-scoped reading at this base is `signal_dangling_pointers`'. drift_report.py:3125-3133 (measure_legs_retried_after_timeout) and :3245-3250 (fleet_over_budget) both loop `for base in read_git_dirs(ctx)`, and spec-8:169 registers dangling_pointers_in_own_ledger, legs_retried_after_timeout, fleet_over_budget and backlog_stragglers as `node`. So the sentence is false, and it misleads whoever reasons about what the node pass covers. | sound | - |
| 24 | grounding | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:section 4 Evidence, first sentence | low | low | confirmed | Spec-15 lines 23 and 152 cite drift_report.py:4404-4417. sed over 4404-4440 shows those lines hold the not-asked, empty and DEAD PROBE statuses. `OVER PIN ... gateable` sits at about :4428 and `over pin ... (report only)` at about :4438. Spec-14:23/116 cite :4427-4438, and spec-14:288 corrects the scout's citation. The error is only in the citation. | sound | - |
| 25 | grounding | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-5.md:section 4 "Alternatives rejected", last bullet | low | low | confirmed | `ls memory/map/features/*.md \| wc -l` printed 32, and every entry is a feature dossier. The '31' comes from the older gap-maint-06 count in the packet (prompt:119). Spec-5:138 says 31. The wrong count is in a rejected alternative only. | sound | - |
| 26 | reuse | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-13.md:section 2 S2 (with TOOL-dTendedCadence-2 §2 S3 and TOOL-dTendedCadence-6 §2 S6) | medium | medium | confirmed | Spec-13:39 and spec-2:56 read their keys through a raw `policy.py get` subprocess, and spec-6:85 has its own `read_record_when`, all inside drift-audit. Neither 13 nor 2 mentions read_policy_value. Spec-4 S6 (around lines 82-92) defines the one adapter and lists only -1, -3, -9, -14, -15, -16, -17 and -18 as callers. Spec-6 is order 2 and spec-4 is order 4, so the allowance 'unless an earlier pass defined it' applies. Built as written, drift-audit ships several readers whose refusal and timeout handling can diverge. | sound | - |
| 27 | reuse | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-16.md:section 2 S2 and section 10 | medium | medium | confirmed | Spec-16:59-60 says only 'decided by TOOL-dTendedCadence-6's own rule (per-run every closed run, on-anomaly a run with an anomaly)'. grep finds neither derive_closing_end nor scan_anomalies in spec-16, and §10 (376-384) lists read_journal and resolve_record_path as 'called, never copied' but names no close or anomaly seam. Spec-6 S2/S3 (lines 50-61) puts that rule in derive_closing_end and scan_anomalies (model.py:1307 exists) and adds four new kinds. A drift-audit copy of the rule could diverge from it. | sound | - |
| 28 | reuse | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-13.md:section 2 S3 (against TOOL-dTendedCadence-6 §2 S7) | medium | medium | confirmed | Spec-13:47-48 takes its base from 'the newest committed maintenance record carrying one' and never cites read_newest_record. Spec-6 S7 (lines 92-96) returns only the newest record, with no filter. Spec-6 makes a missing member take the example's value, `security-head: none` (around 196 and 221-225). So a period record written after the review can carry none, and S3 needs a second history walker that can diverge from the F3 'newest' rule. | sound | - |
| 29 | reuse | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-13.md:section 2 S4 and section 10 | low | low | confirmed | Spec-13:56 and :316 cite only the shell helper add_scratch_worktree (lib-attribute.sh:59), and grep finds no resolve_reading_tree in spec-13. Spec-18 S7 (line 148ff, order 6) specs the Python context manager that adds a detached worktree under the git common dir and removes it on exit. Spec-13 is order 17 in the same kit, so it would duplicate that logic. | sound | - |
| 30 | blast-radius | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-2.md:section 2 S5 (the fragment) and section 4 Files touched | high | high | confirmed | settings-merge.py:247-248 reads `_INTERPRETERS = ("node", "bash")` with default `node`. load_fragment raises on any other interpreter, and render_command emits `{interpreter} "${CLAUDE_PROJECT_DIR}/{hook_path}"`. Spec-2:81-82's fragment has no interpreter key and points at maintain_session.py, and grep finds 'interpreter' nowhere in spec-2. The merged command would be `node .../maintain_session.py`, which fails at every session start while `--check` still reports the hook wired. The procmon template it copies is a .js hook. | sound | - |
| 31 | blast-radius | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-18.md:section 2 S4 (PRODUCT_GLOBS etc. move to tools/loop/flow_layer.py) and section 4 Files touched | high | high | confirmed | git grep shows WIRE-INTO-PROJECT.md:439 'Fill `<prefix>/drift-audit/drift_signals.py` — `PRODUCT_GLOBS` at minimum' and adopt-drift-audit.sh:261 'Fill $KIT_REL/drift_signals.py — PRODUCT_GLOBS at minimum.'. Spec-18 S4 (lines 102-123) moves PRODUCT_GLOBS to tools/loop/flow_layer.py, and its Readers list names neither file, although it claims to be 'found by git grep for the names at base'. Adopters following the docs would fill a declaration the flow signals no longer read. | sound | - |
| 32 | blast-radius | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-2.md:section 2 S9 / section 4 Files touched; same text in spec-11 S7 and spec-13 S9 | medium | medium | confirmed | push-main.sh:26-31 says 'KIT VERSIONS ARE MINTED HERE, NOT ON A BRANCH ... A branch therefore owes no bump'. Spec-2:113/184, spec-11:81-82/148/152 and spec-13:109/175 each require a per-pass hand move of the constant and list only its file. check-kit-versions.sh:342-361 requires the README marker and the workflow markers to equal KIT_DRIFT_AUDIT_VERSION, and grep shows five carriers at 1.30 (README plus four workflows), none listed. A hand bump of drift_report.py alone reds that leg. | sound | - |
| 33 | blast-radius | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-6.md:section 2 S5 (Readers · by value) and section 7 | medium | medium | confirmed | `wc -c .claude/skills/unattended/SKILL.md` printed 10237, and template-size-limits.txt:154 caps it at 10240. SKILL.md:159 holds the 78-byte command line that spec-6 S5 (lines 68-78) replaces with a longer sentence about the terminal verbs writing the record. The same S5 asserts the renders' bytes 'only fall'. As written the render crosses its cap and `unattended skill size` goes red. The bar would catch that, so the effect is contained. | sound | - |
| 34 | blast-radius | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-10.md:section 4 Files touched and section 7 | medium | medium | confirmed | All 9 rendered agents carry `- A build of more than one pass: memory/guides/BUILD-METHOD.md` (grep -n: e.g. gov-builder.md:64, gov-reuse-scout.md:31), and method-carriers.txt:25-33 declares one row for each of them. Spec-10 S6 and section 4 render `.claude/agents/gov-maintainer.md`, which will carry the same charter line. grep finds no `method-carriers` or `method carriers` in spec-10's section 4 or its section 7 leg line. check-method-carriers.sh fails check 3 on an undeclared mention. The bar goes red at the close, but the effect is contained and the build will see it. | sound | - |
| 35 | blast-radius | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-18.md:section 2 S4 (TRACE_CUTOFF moves) and section 4 Files touched | medium | medium | confirmed | drift_signals.py:44 is the only BUILD-METHOD mention in that file, and it sits inside the TRACE_CUTOFF comment block. method-carriers.txt has the row `tools/drift-audit/drift_signals.py · TRACE_CUTOFF cites the commit...`. Spec-18 S4 (:102-105) moves TRACE_CUTOFF with its values to tools/loop/flow_layer.py and flow_layer.template.py. Section 4 (:281-308) does not list method-carriers.txt, and section 7 does not name the leg. Once the block moves, check 4 (stale row) and check 3 (undeclared flow_layer.py) both fire. | sound | - |
| 36 | blast-radius | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:section 4 Files touched (the new `maintain breach record` leg); same omission in spec-2 (the new SessionStart harness hook) and spec-18 S5 (six new legs) | medium | medium | confirmed | test_codebase_map.py:9-15 says to claim a new key in a dossier and says baseline.toml never gains one. map_extractors.py:141-171 keys harness hooks as `<event> <script>` from settings.json, and dossiers do claim them (agent-cap.md:25). Spec-2 adds a SessionStart hook `tools/drift-audit/maintain_session.py` merged into .claude/settings.json (:86, :185). Spec-15 adds the leg `maintain breach record` to gate-legs.json (:193). Neither spec lists any memory/map file. Spec-18 lists only features/playbook.md and generated/, and says nothing about which dossier claims its six legs. So the coverage leg reds on at least the keys from spec 2 and spec 15. | sound | - |
| 37 | blast-radius | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:section 4 Files touched / section 7 (tools/gate-legs.json); same in spec-7, spec-18 (gate-legs.json) and spec-9 (skills/session-kickoff/manifest-check.sh) | medium | medium | confirmed | SESSION-KICKOFF.md's audit block watches tools/gate-legs.json and skills/session-kickoff/manifest-check.sh. manifest-check.sh:1524-1541 (C5) fails when a watch-touching commit is not an ancestor of a last-audit re-stamp. Specs 7, 15 and 18 edit gate-legs.json (spec-15:193, spec-18 files list, spec-7:79-85), and spec-9:195 edits manifest-check.sh. grep for SESSION-KICKOFF or kickoff-manifest over the spec set finds nothing, and BUILD-METHOD has no re-stamp step either. So the kickoff-manifest ratchet goes red, and nothing in the plan budgets the fix. | sound | - |
| 38 | blast-radius | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:section 2 S10 and section 4 Files touched (help/README.md); the corresponding omission in spec-4, spec-14 and spec-18 | low | low | confirmed | `ls help` shows no maintain.md. In build order (README:89-106) specs 10, 6 and 8 come first and none of them edits help/maintain.md. Spec-4 (order 4) is the first to edit it (:217), yet only spec-15 (:113, :199) lists help/README.md. Spec-15 S10 makes the index line conditional on 'the first unit whose build pass reaches them', but spec-4's section 4 does not declare that file, so its builder either writes an undeclared file or leaves the page unindexed until order 7. The effect is on docs only. | sound | - |
| 39 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-6.md:section 4 "The maintenance record" (the key grammar held at the write boundary), against TOOL-dTendedCadence-2 AC3 and TOOL-dTendedCadence-16 S6 | high | high | confirmed | Spec-6:202-206 holds the record key to `^\d{4}-(\d{2}-\d{2}\|W\d{2})$` or `^[a-z0-9][a-z0-9-]*\.[0-9a-f]{12}$`, and says anything else exits 2. Spec-2 AC3 (:241-243) mints `s-` followed by 12 hex for every-session, and spec-16 (:93) runs item.maintain.record under `<period>.<node>`. I re-ran python over both regexes: s-0123456789ab False, 2026-11-01.node-a False, 2026-W44.daily-pc False, 2026-11-01 True. So the every-session cadence and every node pass fail at the record step. | sound | - |
| 40 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:section 2 S4 (the red leg reads the newest committed record) | high | high | confirmed | Spec-15 S4 (:74-84) counts the `over-pin:` lines of the newest committed maintenance record of any kind. Spec-6:26-27 writes one record per period or event run, and spec-8 S5 (:53-58) has `--event` read only its event's rows, so a newer event-run record with no over-pin lines greens the leg while period offenders still stand. Spec-6 S6 (:85-87) has on-finding write nothing on a clean run, so an older over-pin record stays newest and the leg stays red after the offenders clear. I found no run-kind field and no AC covering either case. (The security-head sub-case is less certain, since that write goes into the period's own record.) | sound | - |
| 41 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-9.md:section 2 S2 (the detail row) and S5 (the recurrence claim) | high | high | confirmed | Spec-9:63-66 puts the detail row `{"path","population","reads","touches"}` in the offender key. drift_report.py:3734-3743 (extract_unlocated) drops only `line`/`lines` and a trailing `:<digits>`, and :4007 builds the key as json.dumps(extract_unlocated(d), sort_keys=True). Read counts differ every period and between nodes, so S5's 'unchanged target adds a seen row' and the risks line's 'two nodes ... one intake' (:226-228) do not hold. Each period files a new sweep intake for the same path. | sound | - |
| 42 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-11.md:section 4 "The intake" against section 2 S6 | high | high | confirmed | Spec-11's intake text (:121-126) ends with `cycle: <daily\|weekly> <period>`. The filing is spec-8's I6, whose recurrence detection depends on the text carrying 'no value, period or SHA' (spec-8:209-210), and spec-8 AC7 (:292-294) names a period in the text as the red case. So every cycle gets a fresh content key and a fresh intake, and S6's 'never stacks a second build' fails on real cycles. | sound | - |
| 43 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-3.md:section 2 S6 and section 5 security | high | high | confirmed | Spec-3 S6 (:91-96) runs `loop_transition.py dispose` from item.maintain.direct, and dRankedPlan-4 S3 (:48-55) has dispose record the move through write_transition, a tracked record. Spec-3 :196 admits 'the one tracked write is dispose's', and :190 itself says tracked content belongs to maintain.patch. Spec-1:98 says 'The walk commits nothing', and only the maintenance record has a landing intake (spec-1 S6, F4, :293-299). loop_transition.py does not exist at this base, so nothing commits the transition. It stays uncommitted on one node, and every other node and the default branch never see it. | sound | - |
| 44 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:section 2 S2 step (1) and section 5 security | medium | medium | confirmed | Spec-15 S2 step (1) (:55-61) re-renders a SCOPE row in another home's tracked BACKLOG.md through render_scope_row, and section 5 (:214-216) admits this is 'the one tracked write outside an intake'. No AC or section names a commit or landing route for that write, and spec-1:98 says the walk commits nothing. So the seen clause stays a dirty working-tree edit on one node, and the dedupe a second node runs through git grep never sees it. | sound | - |
| 45 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:section 2 S2, the order (1) open ask, (2) intake | high | high | confirmed | Spec-15 S2 (:55-65) step (1) only matches an ask confirmed live (OPEN, BLOCKED or DEFERRED). Step (2) re-files the same stable text with no period, and a content key already on record 'appends the recurrence's receipt to that intake, route seen'. dWellOiledMachine-4 S1 confirms that typing the same text again only appends a receipt. A grep of spec 15 for closed/wontdo/regress/survivor finds no branch for an ask that has closed. Spec 8 (:202-205) has a survivor branch, but only for patch intakes whose build is CLOSED or WONTDO. So once the ask closes, a regressed offender gets only receipts and is never placed again. That is a wrong result on a narrow path, and it is printed as `seen`. | sound | - |
| 46 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md:section 2 S6 (the record's landing intake) | medium | medium | confirmed | Spec-1 S6 (:95-98) files the landing intake with the record's key, base and readings as JSON for the patch build to re-write from. dWellOiledMachine-4 S2 (:54) redacts the text through render_redacted and cuts it at INTAKE_CAP_BYTES (65536). Spec-6 itself expects records to pass 64 KiB (risks line), and its stdin grammar (:221-225) states no exit for empty, non-JSON or incomplete input. Neither spec covers a capped or redacted payload. | unsound | - |
| 47 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-18.md:section 2 S7 and section 5 security | medium | medium | confirmed | Spec-18 S7 (:148-154) puts the worktree at `<git-common-dir>/maintain-read/<sha12>`, a path fixed by the sha alone, and removes it on context-manager exit. Spec-1 S4 runs `--readings` as a bounded subprocess, and a timeout kill skips that exit. lib-attribute.sh:59 runs a plain `git worktree add --detach "$1" "$2"`, which fails when the path already exists. post-merge.sh:10 shows the repo's own pattern of a pid suffix (`gate-pm.<pid>`). Section 5 (:325) claims removal 'on every exit path' and does not mention a kill. A period run and an event run at one base hold different leases, so their paths collide. | sound | - |
| 48 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-16.md:section 2 S2 (closed_runs_with_no_run_record population) | medium | medium | confirmed | Spec-16 S2 (:55-62) counts every closed run that owes a record, glossing 'per-run every closed run', and does not exclude unbound runs. Spec-6 F2 resolves that a run serving no unit stays unrecorded. record.py:1183-1186 returns None when `not serves`, and runlog.py:424-429 prints the unbound skip and writes nothing. So an unbound run's record is never at the resolved path, and S2 as written counts it as missing every period. | sound | - |
| 49 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-17.md:section 2 S11 and AC10, against TOOL-dTendedCadence-8 section 4 "The check" and TOOL-dTendedCadence-9 S4 | medium | medium | confirmed | The three specs contradict each other. Spec-8 (:133-140) says a row with no fix may name `patch` and otherwise defaults to `file`, and its check table (:152) refuses a route outside `patch` and `file`, so `ask` is refused. Its hand-off (:103) says spec 17 registers `route = "patch"`. Spec-17 S11 (:123-130) says the key's 'one value here' is `ask`, that it refuses any other value, and that spec 9 adds `patch`. Spec-17 AC10 (:285-289) requires `route = "file"` to be refused. Spec-9 S4 (:78) claims `patch` as 'the value this unit adds' to a key spec 17 introduces. | sound | - |
| 50 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-3.md:section 2 S5 (idle_processes_past_ceiling) against S4 (fixed = empty offender set) | medium | medium | confirmed | Spec-3 S5 (:80-82) defines idle_processes_past_ceiling only by its value, the targets count from reap.py's summary line, and names no detail rows. reap.py:413-416 prints that summary with counts only. drift_report.py render_drift_offenders (:3985-4022) builds keys only from detail rows, and spec-8 AC5 (:283-286) reds a reading that is over its pin with no keys. Spec-3 S4 (:72-74) judges `fixed` by an empty offender set, so a reading with no keys always reads fixed, and survivors are never handed to run_breach_route. | unsound | - |
| 51 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md:section 2 S2 (an item body that raises exits 1 and the period re-runs) | medium | medium | confirmed | Spec-1 S2 (:58-59): an item that raises exits 1, the lease is released as a hand-over, and 'the next wake runs the period again', from the start of the walk. Spec-8 (:214-216) relies on 'the period lease's witness stops a second run of the same period', but a hand-over is exactly that second run. Re-filing the stable text appends another receipt (spec-8 :210-212 counts each receipt as a recurrence's seen row), and direct fixes run again. No spec states a re-run contract. | sound | - |
| 52 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-12.md:section 2 S3 (head commit X by git blame) under maintain.reading-tree: worktree | medium | medium | confirmed | Spec-12 S3 (:52-54) says scan_annotations reads 'at HEAD' but spells the blame as 'one git blame --porcelain per file', with no revision. Without a revision, git blame reads the working file and reports an uncommitted line as the all-zero sha. The row is scope repo, and under `maintain.reading-tree: worktree` spec-18 S7 yields the node's own checkout. scan_annotations does not exist yet (grep of tools/ finds no definition), so only the spec governs, and it leaves X undefined for a dirty line. That breaks `X..HEAD` for git log -L. | sound | - |
| 53 | failure-envelope | memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-13.md:section 2 S5 (offender key `<path>:<line>`) | medium | medium | confirmed | Spec-13 S5 (:71-75) keys a finding as `<path>:<line>` and claims a re-report adds a seen clause rather than a second ask. Spec-15 S2 hashes `<reading>\t<offender key>` verbatim, so a line moved by an unrelated edit produces a new key and a second ask. Two findings at one line share a key and fold into one ask. drift_report.py:3999-4001 drops trailing `:<digits>` for exactly this reason ('an unrelated edit above a finding moves its line'). | sound | - |
