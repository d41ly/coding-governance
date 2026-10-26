**Serves:** spec-audit KICK-dKeptSession-33@rev-1 KICK-dKeptSession-34@rev-1 KICK-dKeptSession-40@rev-1 KICK-dKeptSession-32@rev-1 KICK-dKeptSession-37@rev-1 KICK-dKeptSession-38@rev-1 KICK-dKeptSession-30@rev-1 KICK-dKeptSession-31@rev-1 KICK-dKeptSession-36@rev-1 KICK-dKeptSession-39@rev-1 KICK-dKeptSession-35@rev-1 KICK-dKeptSession-42@rev-1 KICK-dKeptSession-43@rev-1 KICK-dKeptSession-41@rev-1 KICK-dKeptSession-44@rev-1

# Tier-2 spec audit — dKeptSession, the fifteen round-1 promoted units (KICK-dKeptSession-30 to -44), ROUND 1

*This is an adversarial pre-code pass over the fifteen units that the round-1 spec audit promoted, dated 2026-10-26. Five lenses found the findings: coherence, grounding, reuse, blast-radius and failure-envelope. A skeptic then tried to refute each one. Only confirmed findings appear below. Each item gives its address, its consequence, the fix and a left-shift gate.*

Reviewed: memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-33.md@9a2279c8c8ec92170ff16713581193312bb0e2f4, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-34.md@423715e7634d983ee996a6f24a2636bf239b4c53, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-40.md@6f431d779aec5f1c09e8ca6f730484460857498e, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-32.md@911c1263272838aee085dffea12668632d754d37, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-37.md@85cf002d1d9c423cfdb906bde255b5ffbc30c3b0, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-38.md@466d770e5a0fdbf124a86c8159ee4b545c9106c6, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md@9ef2bf01e41c1cc858c7b0d360e610b8e506eb45, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-31.md@2aa02ff830e534490ca5d0d14f52de79520bf327, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-36.md@e466fda43e49b7f0e49e32544895db5a24c832af, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-39.md@b19744b7aafe7e1518813ecfe7188b03d6951cca, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-35.md@0040615ba4c83b18a22564074231bdd3454e2f94, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-42.md@c831dc3bddb57c9888c3f4709db1890c7aaa290d, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-43.md@51dc33bec1c5884a47d7d28342bd6367c3f7fa55, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-41.md@7f29406187e9a857dad75d16e1ee2939cfeafa13, memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md@c4b04705f00d067b763ffbd5776e146748d6ddd3

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker stands. Eleven high findings stand. The spec set must not go to Build until every high item below is fixed and re-audited.

By item the tally is 0 blocker, 9 high, 29 medium and 10 low, which makes 48 items. By raw confirmed finding it is 0 blocker, 11 high, 34 medium and 11 low, which makes 56. Items merge only findings that describe one defect at one binding grade.

Six defects were found at two different grades, and each grade keeps its own item. Fixing one item of each pair fixes the other.

- The hard-coded projects root: H1 (ids 28, 38, high) and M12 (id 18, medium).
- The unfiltered compact pre_tokens: H2 (id 16, high) and M25 (id 44, medium).
- The false mirror migration: H3 (ids 22, 48, high) and M8 (id 9, medium).
- The message id's act position: H4 (id 39, high) and M7 (id 8, medium).
- KICK-37 AC1 green at base: M14 (id 24, medium) and L1 (ids 12, 55, low).
- The unextracted AI_AGENT parse: M18 (id 30, medium) and L2 (id 13, low).

## Review shape

The review ran at intensity full: raw 56, confirmed 56, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 15 | 15 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 12 | 12 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 14 | 14 | 0 | 0 | 0 | 1.00 |

Run integrity:

- Lenses: 5 of 5 returned, and none died.
- Skeptic batches: 5 of 5 returned, and none died.
- Demoted or discarded verdicts: 0 contradictory, 0 orphaned duplicate refutations, 0 spurious and 0 duplicates.
- Fixes on confirmed findings: 48 judged sound, 8 judged UNSOUND, 0 with no proposal and 0 NOT JUDGED.
- Severity: 0 confirmed findings were left ungraded by the skeptic, and 11 were re-graded.
- Unverified findings: none answered UNCERTAIN, and none with no usable verdict.
- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 29 spec documents were supplied as `specs`, as sibling context.
- Checklist: 69 items, each assigned to exactly one of 5 lenses (coherence 14, grounding 14, reuse 14, blast-radius 14, failure-envelope 13).
- By design: 1 invariant from the checklist's by-design block.
- Move check: no checked subject moved.

Lens notes were not supplied, so every lens ran on the kit's generic brief.

All five lenses returned, so the finding set is complete for this round.

The skeptic re-graded eleven findings, and their binding grades are used below. Ids 1, 31, 34, 36, 37, 47 and 51 went from high to medium. Ids 12, 41 and 53 went from medium to low. Id 27 went from low to medium. I agree with all eleven grades.

The skeptic judged eight fixes UNSOUND: ids 4, 6, 14, 31, 34, 43, 49 and 53. For each of them the skeptic's corrected fix is the one written here.

## High

### H1 — The window scan's default root is a literal `~/.claude/projects`, not `resolve_projects_root` (ids 28, 38)

- **Where:** KICK-dKeptSession-30, section 2 S1 step 2 and S2, section 10.
- **What:** S1 defaults `root` to `~/.claude/projects`. S2 derives the root two ways: `measure_context_fill` takes the transcript's parent's parent, and `derive_context_fill(ev)` takes the default. `tools/runlog/extract.py:185` already has `resolve_projects_root`, which honours `--transcripts` and `$CLAUDE_CONFIG_DIR/projects` (TOOL-dLoggedFlight-6 S1). Section 10 does not name it.
- **Consequence:** On a node with CLAUDE_CONFIG_DIR set, the scan finds no observation and falls to the 200000 rung, which is the defect this unit repairs, on a narrow path. Unit 9's `derive_context_fill(ev)` reads the node's real tree, not `<dir>`, which escapes the runlog selftest's `build_arm_env` isolation.
- **Fix (skeptic judged SOUND):** Default `root` through `resolve_projects_root()`, and have `derive_context_fill` take the root its caller already resolved. Unit 9 passes its `--transcripts`/`<dir>` root, and `runlog.py context` passes `resolve_projects_root(override=args.transcripts)`. Compute the window once per (model, root) per process. Cite extract.py:185 and TOOL-dLoggedFlight-6 S1 in section 10. Add an AC that sets CLAUDE_CONFIG_DIR to a scratch config dir holding `context-window-sibling` and calls `derive_context_window('fixture-model')` with no root. It must answer the 1000000 rung, and it must be red against a copy that defaults to `~/.claude/projects`.
- **Left-shift gate:** Add a checklist entry: a spec that names a filesystem root must cite the module's existing resolver, or say why none applies.

### H2 — Compact `pre_tokens` lift every model's window, because compact events carry no model (id 16)

- **Where:** KICK-dKeptSession-30, section 2 S1 step 2, section 4 Evidence.
- **What:** S1 folds in "the largest pre_tokens of the compact events" with no model filter. `extract.py:818-821` builds compact events as {t, kind, src, trigger, pre_tokens}, with no model field.
- **Consequence:** One 1M compaction in the newest 20 transcripts puts every model on the node on the 1M rung, including the 95946-max claude-opus-4-8 that section 4 names. A 200k-window session reads a fifth of its true fill, so context.threshold never fires before the harness compacts. AC1 to AC4 use one model and no compact event, so none of them can see this.
- **Fix (skeptic judged SOUND):** In S1, count compact pre_tokens only when the compaction falls inside a session whose main usage events are on `model`, for example where the last usage before it is on `model`. Or drop pre_tokens from the observation. Add an AC with a 900000-preTokens compaction in an other-model session, and a 150000 usage on fixture-model that must still read 75%.
- **Left-shift gate:** Add a checklist entry: an aggregate keyed by a field must name, for each event kind it folds in, where that field comes from.

### H3 — The mirror migration is false: a pre-unit mirror reads FRESH, never "stale once" (ids 22, 48)

- **Where:** KICK-dKeptSession-40, section 4 Migration, section 5 risks, section 6 AC2.
- **What:** At 3c8c4718a, `policy-mirror.js:111-118` builds its input list from `Object.keys(doc.legacy_blobs)` of the stored mirror itself. A mirror rendered before this unit has no `presets.toml` key, so the store is never compared. The guard takes its input list from the state it guards.
- **Consequence:** On upgrade, and wherever an old mirror is not re-rendered, every hook (actions.free, agent-cap, mail-notice) serves the old preset values as FRESH while `policy.py get` answers the new ones. A strict repo's hooks read budgets.enforce warn while `get` reads refuse. That is the defect the unit closes. AC2 renders the mirror after the unit lands, so it never sees an old one.
- **Fix (skeptic judged SOUND):** Make the reader's input list independent of the mirror. `policy-mirror.js` treats a mirror that lacks any key of the kit's expected input set, the catalogue-adjacent `presets.toml` included, as STALE. Or render a version/inputs field the JS checks. Rewrite the Migration text to match. Add a criterion: a mirror planted without the `presets.toml` key, then a committed change to presets.toml, makes `node policy-mirror.js get hooks.bypass` report stale.
- **Left-shift gate:** Add a checklist entry: a freshness check must take its expected input list from the code, never from the artefact it checks.

### H4 — The message id's act field keeps two positions, and the child build reads the wrong one (id 39)

- **Where:** KICK-dKeptSession-31, section 2 S1 and S4.
- **What:** S1 puts `<to>` and `<content-key>` at positions 7 and 8, and says unit 22's act "joins as the ninth field". S4 supersedes only KICK-22 S2's "six fields", AC2 and KICK-5 S5. It leaves standing KICK-22 S4 ("a seventh field of S2, appended after `answers`") and KICK-22's hands-off edge to dWellOiledMachine ("whose act joins S2 as a seventh field").
- **Consequence:** dWellOiledMachine reads its contract from that hands-off edge. If it puts the act seventh, between `answers` and `to`, every id it derives disagrees with this build's id for the same message. The duplicate refusal across the two builds then fails open.
- **Fix (skeptic judged SOUND):** Add KICK-22 S4 and KICK-22's `hands-off external — dWellOiledMachine` edge to KICK-31 S4's superseded list, with the act at position 9, after `<to>` and `<content-key>`. Record that answer in KICK-22's ledger, and file the changed position as an ask row in dWellOiledMachine's BACKLOG.md, as the README's write rule allows.
- **Left-shift gate:** Add a checklist entry: a spec that changes a field order lists every sibling clause and hands-off edge that states the old order, found by grep.

### H5 — KICK-35 AC1's staged break cannot go red on its A-B-A fixture (id 3)

- **Where:** KICK-dKeptSession-35, section 6 AC1 "Red when", section 7 new arm (selftest.py), section 4 Alternatives rejected.
- **What:** KICK-31 builds the id from eight fields, kind and content-key among them. Over Design exits A, B, A, the posts are (confirmed, A), (changed, B) and (changed, A). With `--pass` dropped, no two share an id: exits 1 and 3 differ in kind, and exits 2 and 3 differ in key. AC1 also pins no interface texts.
- **Consequence:** The arm stays green with `--pass` removed. It certifies S1's Design-exit ordinal without testing it. The Alternatives line ("A to B to A ... would collide with the first notice") is false for the same reason.
- **Fix (skeptic judged SOUND):** Pin AC1's fixture so that exits 2 and 3 publish the SAME interface text, or use four exits A, B, A, B. State that the copy without `--pass` prints `mail — duplicate` on exit 3, and record that red in the build. Correct the Alternatives line to name a changed-to-changed key repeat.
- **Left-shift gate:** The class is fixture-passes-by-finding-nothing. Every staged break in a spec names the red line it prints, and the build records that red before the fix lands.

### H6 — KICK-42 S2 supersedes by first-seen, the arrival order KICK-27 forbids (id 4)

- **Where:** KICK-dKeptSession-42, section 2 S2 ("earlier by first-seen").
- **What:** S2 acks every earlier open confirmed or changed row, "earlier by first-seen". KICK-27 S5 says the check never chooses a row by first-seen, seq or fetch order. KICK-27's red case has the take-over's `changed` K2 seen first and the predecessor's `confirmed` K1 later.
- **Consequence:** check_interface_notice names K2 current, and S2 acks K2 and rows seen before it. K1 has a later first-seen, so it stays open, and KICK-5 S9's guard refuses the dependent's transition until flow.wait-ceiling (72h, or 168h under strict). That is the stall this unit exists to remove. In the mirror case, a newer `changed` seen before the current row is acked without being consumed, which AC3 forbids.
- **Fix (skeptic judged UNSOUND; the skeptic's corrected fix):** Supersede by content and order, not by arrival. Acknowledge the current row, and every open confirmed or changed row from that parent whose content-key equals the current key or that KICK-27's seq/after chain places before the current row. Leave open only a row the chain places after the current one. Add an AC3 variant using KICK-27 AC4's plant (the changed row sighted first), and observe both rows acknowledged.
- **Left-shift gate:** Add a checklist entry: a spec that orders rows must cite the ordering rule its source unit defines, and must not order by arrival.

### H7 — KICK-34 expects `policy.py get` to read a derived default that `get` refuses (id 21)

- **Where:** KICK-dKeptSession-34, section 2 S1, section 4 "The answers" table, section 6 AC1 and AC2.
- **What:** S1 says an unassigned derived row "reads with source default". AC2 expects `policy.py get <cap> --explain` to print a budgets.* cap's derived value. At 3c8c4718a, `read_default_value` (policy.py:695-698) raises DerivedDefault for every {derived=...} default, and `get` refuses it. Only budgets.py's resolve_caps reads it, by catching the refusal (budgets.py:270). No sibling spec changes that.
- **Consequence:** AC1 and AC2 cannot pass against the reader the unit extends. A builder either invents a derived-value computation inside `get`, which overwrites the evidence-derived caps and role efforts the Goal protects, or ships a criterion that stays red.
- **Fix (skeptic judged SOUND):** Restate S1 and the table: an unassigned derived row answers None from the preset step, so `get` gives dGroundRules' DerivedDefault refusal unchanged. Re-point AC2 to `python budgets.py resolve <cap>`, and AC1 to "refuses with the DerivedDefault reason, never a preset source".
- **Left-shift gate:** Add a checklist entry: every AC command is checked against the verb's current refusals at the base revision before the spec leaves Design.

### H8 — A 200k session is measured against the 1M rung on a node that runs both windows on one model (id 43)

- **Where:** KICK-dKeptSession-30, section 2 S1 rung 2, section 5 risks.
- **What:** Rung 2 takes the largest observation per model id across the newest 20 transcripts. Section 4 says the id reads `claude-opus-5-5` for both the 200k and the 1M window, and AC2 asserts that a 150k transcript beside a 900k sibling prints 15%. Section 5 prices only the opposite direction.
- **Consequence:** A 200k session on a node that has logged any 1M session reads a fifth of its real fill. `fresh-at-boundary` at 60% never fires, and the harness compacts first. Section 4 rejects "a larger pinned constant" for exactly this result.
- **Fix (skeptic judged UNSOUND; the skeptic's corrected fix):** State the mixed-window limit in S1 and in section 5 risks: every session of a model observed past 200k on the node reads the 1M rung, and a 200k session's override is CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000. Add an AC: AC2's root (150k plus a 900k sibling), read with CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000, prints 75% with source env.
- **Left-shift gate:** Add a checklist entry: section 5 risks prices both directions of every derived threshold.

### H9 — KICK-42 S1 silently acks withdrawn and superseded notices, even when the transition is then refused (id 49)

- **Where:** KICK-dKeptSession-42, section 2 S1, section 4 Alternatives rejected.
- **What:** S1 acks every open `landed`, `superseded` and `withdrawn` row before KICK-5 S9's guard reads, with no output line. Nothing makes the ack wait for the guard's verdict on the other rows.
- **Consequence:** A `withdrawn` parent notice is consumed and never shown. Under mailbox.reads=transitions-only (KICK-10 S3) the transition is the only read, so it is never surfaced at all. If an open question refuses the transition, the ack has still landed, and the next transition passes. The dependent builds on a withdrawn parent, the outcome section 4 rejects ("would let a `withdrawn` parent pass unread").
- **Fix (skeptic judged UNSOUND; the skeptic's corrected fix):** In S1, list the open rows first. Post the S1 and S2 acks only when every open row is one the writer consumes, printing one line per ack on the transition's output: `mail — acked <kind> <id> from build:<parent>`. Otherwise post no ack, and let the guard refuse, listing every open row. Add a criterion: plant a `withdrawn` and an open `question`; the transition is refused and the `withdrawn` row still reads `open`.
- **Left-shift gate:** Add a checklist entry: a consuming write that precedes a guard must be conditional on that guard's verdict, and must print what it consumed.

## Medium

### M1 — Two consumers share an order value with the unit they consume (id 1)

- **Where:** KICK-dKeptSession-38 header order 9 and section 3 Edges (consumes from KICK-37, order 9). KICK-dKeptSession-31 header order 16 (amends KICK-5's `--mail post`, order 16).
- **What:** `gen_build_index.py:1717` makes units sharing an order value one parallel group, so the README lists step 9 (13, 37, 38) and step 16 (31, 5) as parallel.
- **Consequence:** The order label is wrong. Dispatched together, KICK-38 has no read_claude_version yet and must write a second PATH read (which KICK-37 AC1 forbids) or stall. KICK-31 edits a post path KICK-5 has not written. A dispatcher following BUILD-METHOD M6 clause (2) would serialise these, so the effect is a misleading label.
- **Fix (skeptic judged SOUND):** Set KICK-38 to order 10 and KICK-31 to order 17, and shift the later orders, so each consumer comes one step after its producer. Re-render the build-order region and confirm no consumes-from edge points at the same or a later order.
- **Left-shift gate:** A build-index check that reds when a consumes-from edge points at the same or a later order.

### M2 — Seven "parallel" groups share write sets (id 2)

- **Where:** The header order of KICK-dKeptSession-37, -33, -34, -40, -32, -30, -35 and -42; section 4 Files touched.
- **What:** Each promoted unit takes the order one step after the unit it repairs, which collides with a roster unit already there. Step 2 (19, 33) shares check_policy.py. Step 4 (3, 34, 40) shares policy.py and check_policy.py. Step 6 (20, 32) shares policy.py and check_policy.py. Step 9 (13, 37, 38) shares manifest-check.sh, card-store.fixture.sh and manifest-check.test.sh, and all three move KIT_MANIFEST_VERSION. Step 13 (30, 9) shares extract.py and selftest.py. Step 16 (31, 5) shares unattended.sh, unattended.test.sh and the VERBS files. Step 25 (35, 42) shares loop_transition.py and selftest.py.
- **Consequence:** The order region contradicts BUILD-METHOD M6 clause (1). A dispatcher following it would run conflicting writers at once, with colliding version bumps. The dispatcher records write sets before it dispatches, which contains the effect.
- **Fix (skeptic judged SOUND):** Give each promoted unit an order of its own, or a distinct order inside its repaired unit's slot, so that no two units in one group share a Files-touched path. Re-render and check that every "Parallel: yes" group has disjoint Files-touched lists.
- **Left-shift gate:** A build-index check that reds a "Parallel: yes" group whose Files-touched lists intersect.

### M3 — Other loop-kit subprocesses into the driver keep an unresolved `bash` (id 5)

- **Where:** KICK-dKeptSession-36, section 2 S1 and S2, section 3 Non-goals.
- **What:** The unit routes only KICK-5's guard (and, elsewhere, KICK-42 S3's ack and KICK-44 S16 and S17) through resolve_bash. KICK-7 S4's per-dependent `--mail post` (extended by KICK-35), KICK-7 S3's bare `bash <kit>/unattended.sh --claims` in position.py and KICK-42 S2's check_interface_notice call name no resolver.
- **Consequence:** On this node a bare `bash` from Windows python reaches WSL, where the driver path does not resolve. Every dependency notice prints `notice — not posted` and never lands. KICK-42's interface check never confirms, so the dependent stays held.
- **Fix (skeptic judged SOUND):** Widen S2 to every loop-kit subprocess that runs the unattended driver: write_dependency_notices' posts (KICK-7 S4 and KICK-35), KICK-42 S2's interface check and KICK-7 S3's check in position.py. Better, route every call through one helper, for example run_driver(argv) in loop_lib.py. Add a selftest arm that greps the loop kit for any subprocess argv[0] that is not resolve_bash().
- **Left-shift gate:** That selftest arm is the gate for the class.

### M4 — The "extraction replaces it unchanged" claim has no gate behind it (id 6)

- **Where:** KICK-dKeptSession-36, section 3 ("keeps govkit's contract so that extraction replaces it unchanged"), section 4 S1, section 7 Gates.
- **What:** Section 7 names `python resolver (behaviour + inline parity + idiom ban)`, but `tools/lib/resolve-python.test.sh` PARITY_ROWS (lines 168-184) has no resolve_bash row. The tree already holds 10 `def resolve_bash` definitions.
- **Consequence:** The loop_lib.py copy is one more unparitied resolver, which KICK-44 S16 and S17 build on. A drift from govkit's candidate list or uname test goes unseen, and the promised extraction has no guarantee.
- **Fix (skeptic judged UNSOUND; the skeptic's corrected fix):** Drop the "extraction replaces it unchanged" parity claim from section 3. Name a loop selftest arm that asserts the copy refuses the System32 and WindowsApps candidates, raises on a set but unusable GOV_BASH, and runs the uname MINGW/MSYS test. In section 7, state that the python resolver leg does not check resolve_bash. A byte-for-byte parity row with govkit as canonical would go red at once, because govkit raises Refusal and S1 requires LoopError.
- **Left-shift gate:** The class is second-implementation-is-not-a-second-opinion. Add a checklist entry: a spec that claims parity with another copy names the gate that compares them, or drops the claim.

### M5 — S1 says "govkit's contract" but AC2 demands a refusal govkit does not make (ids 23, 52)

- **Where:** KICK-dKeptSession-36, section 2 S1, section 3 non-goal 3, section 6 AC2.
- **What:** govkit.py:1170-1183 accepts any GOV_BASH that runs `-c :`, with no uname test and no System32 filter on the override. `/c/Windows/System32/bash.exe -c 'uname -s'` prints Linux with rc 0. S1 places the System32 refusal and the uname test under the candidates only, yet AC2 requires a System32 GOV_BASH to raise.
- **Consequence:** A builder who copies govkit accepts `GOV_BASH=C:/Windows/System32/bash.exe`, and the guard runs the driver in WSL: the defect this unit fixes, re-entered through the override. AC2 then reds. A builder who meets AC2 diverges from govkit, which breaks the drop-in extraction claim.
- **Fix (skeptic judged SOUND):** State in S1 that the override passes the same filter as a candidate (the System32/WindowsApps refusal, and `uname -s` answering MINGW or MSYS on a Windows host), and that this departs from govkit's override handling. Drop the "keeps govkit's contract ... unchanged" claim.
- **Left-shift gate:** Add a checklist entry: a spec that copies another function's contract lists every departure from it.

### M6 — review.<stage> gets no rule in the preset store check (id 7)

- **Where:** KICK-dKeptSession-33, section 2 S2 and S4, section 6 AC1.
- **What:** The catalogue (3c8c4718a:1206-1208) gives review.<stage> the default `{ derived = "opt-in; Build owed" }`. The store assigns the concrete keys review.design and review.build. S4 exempts only S2's six rows from the standard-equals-default rule and judges by named members only S3's maintain.fixes.
- **Consequence:** KICK-1's standard-equals-default rule has no literal to compare review.design and review.build against. The check either reds the shipped store, which AC1 says exits 0, or the builder invents a rule. AC1 also counts review.<stage> as unassigned while its keys are assigned.
- **Fix (skeptic judged SOUND):** Add an S-item for review.<stage>. Its concrete keys are judged against the derived default's named members ("opt-in" for design, "owed" for build), as S3 does for maintain.fixes, and the pattern itself is counted unassigned. Add an AC that plants standard's review.build = 'off' and observes the standard-equals-default rule red.
- **Left-shift gate:** Add a checklist entry: a rule over a row class enumerates every catalogue row in the class and names the clause that judges it.

### M7 — The act's position in the message id has two answers (id 8)

- **Where:** KICK-dKeptSession-31, section 2 S1 and S4.
- **What:** This is the same defect as H4, found at medium. KICK-22 S4 and its hands-off line say the act is a seventh field after `answers`. KICK-31 says it is the ninth, and its S4 does not supersede them.
- **Consequence:** dWellOiledMachine's builder inserts the act before `to`, which reorders the fields and changes every id, so a message posted before the change and retried after it is not refused as a duplicate.
- **Fix (skeptic judged SOUND):** Add KICK-22 S4 and its "hands-off external — ... a seventh field" line to S4's superseded list, with the act as the ninth field after content-key, and answer them in KICK-22's ledger.
- **Left-shift gate:** As H4.

### M8 — A mirror rendered before KICK-40 reads fresh (id 9)

- **Where:** KICK-dKeptSession-40, section 4 Migration.
- **What:** This is the same defect as H3, found at medium. `policy-mirror.js` compares only the inputs the mirror recorded, and the JS is not in Files touched.
- **Consequence:** Mirrors rendered between KICK-2 (order 3) and this unit, or never re-rendered, keep serving old preset values.
- **Fix (skeptic judged SOUND):** Have policy-mirror.js mark the mirror stale when its legacy_blobs lacks any input that derive_mirror_inputs lists, by shipping the expected list in the mirror schema or by comparing key sets. Or state the real migration: re-render every mirror at landing, with the build re-rendering the dogfood `.governance/policy.json`. Add an AC that runs a pre-unit mirror and expects stale.
- **Left-shift gate:** As H3.

### M9 — `derive_context_fill(ev)` with no window rescans per row, under a root unit 9's fixture does not control (ids 10, 20, 45)

- **Where:** KICK-dKeptSession-30, section 2 S2, section 3 non-goal "A cache", section 5 perf.
- **What:** With no window, `derive_context_fill(ev)` derives it under the harness's default root on every call. KICK-9 S2 calls it once per main and agent file row. KICK-14 S3 runs the fill inside the boundary hook. Section 5 prices one scan (0.84 s, about 210 MB), and section 3 forbids a cache on that price.
- **Consequence:** KICK-9's fixture lives under %TEMP%, so its per-stage share reads the real root: a 900k-token fixture row reads 450% there but 90% from `runlog.py context`. `runlog.py extract --orient` pays N scans for N rows (minutes for a build with dozens of agent files, and unit 9 AC3 plants 22 or more rows). Each boundary crossing also spends a scan from KICK-44 S8's 8 s CARD_BOUNDARY_BUDGET.
- **Fix (skeptic judged SOUND):** Have KICK-9's reader pass the window from `derive_context_window(model, root=<transcript root>)`, derived once per transcript or per model per run. Or memoise derive_context_window per (model, root) per process, or give derive_context_fill a required root. State the call count in section 5, replace section 3's "One scan costs under a second" with the per-call count, and time `--orient` over the AC3 fixture. Add an AC on KICK-9's per-stage column over the context-window-sibling scenario.
- **Left-shift gate:** Add a checklist entry: a perf price in section 5 is per call times the stated call count of every named caller.

### M10 — KICK-39 is ordered after the KICK-5 pass it says breaks every record kind (id 11)

- **Where:** KICK-dKeptSession-39, header order 17 against KICK-dKeptSession-5 (order 16), section 1 Goal.
- **What:** KICK-5 S12 adds a mailbox-message factory row. PLAY-dOrderedCharter-42 S2 refuses build_records' import when the factory's kinds differ from TYPED_RECORD_KINDS (pinned by its AC2). KICK-5's section 7 names no memory-tree or build-index gate.
- **Consequence:** Built as ordered, KICK-5's pass breaks every record kind, the transition log channel included, and the break goes unseen at that pass. Adding the tuple member first breaks the equality the other way.
- **Fix (skeptic judged SOUND):** Build S1 and S2 in the same pass and commit as KICK-5 S12 (one write set), or have KICK-5 consume this unit, with the tuple member and the factory row landing together. Name "build-index selftest" in that pass's gates.
- **Left-shift gate:** Add a checklist entry: two edits held equal by an import-time check land in one write set.

### M11 — CLAUDE_CODE_MAX_CONTEXT_TOKENS is ranked first unconditionally, but the harness honours it only for non-first-party models (id 17)

- **Where:** KICK-dKeptSession-30, section 2 S1 step 1, section 4 Evidence, S5 help line.
- **What:** The installed harness reads the variable only when `yv(e)` passes, which it does not for a canonical first-party `claude-` model such as claude-opus-5-5. S1 calls it the model's real window and lets it win.
- **Consequence:** An owner who sets it, as S5's help page advises, moves this unit's fill but not the harness's compaction point. A first-party model's fill and fresh-at-boundary decision then diverge from the real window, for example a fill read against 500000 while the harness runs 1M.
- **Fix (skeptic judged SOUND):** In S1, rank the variable first only when the model is not a first-party `claude-` model (mirror the harness gate), or record it as advisory and name the gate. Re-word S5's help line to match, and correct the section 4 Evidence line to quote the gate as well as the hint text.
- **Left-shift gate:** Add a checklist entry: a platform-variable claim cites the harness code that reads it, not only its help text.

### M12 — The default root ignores CLAUDE_CONFIG_DIR and the selftest's decoy (id 18)

- **Where:** KICK-dKeptSession-30, section 2 S1 and S2, section 10.
- **What:** This is the same defect as H1, found at medium. S1 hard-codes `~/.claude/projects`, and section 10 does not name `resolve_projects_root`.
- **Consequence:** On a node with CLAUDE_CONFIG_DIR set, unit 9's rows scan the wrong tree. The runlog selftest's decoy canary (selftest.py:348-349) aims CLAUDE_CONFIG_DIR at a decoy, and a literal path bypasses it.
- **Fix (skeptic judged SOUND):** In S1, name `resolve_projects_root()` (tools/runlog/extract.py:185) as the default root, and add it to section 10.
- **Left-shift gate:** As H1.

### M13 — The window fixtures inherit CLAUDE_CODE_MAX_CONTEXT_TOKENS from the environment (ids 19, 46)

- **Where:** KICK-dKeptSession-30, section 2 S1 rung 1 and S4, section 6 AC1 to AC3.
- **What:** Rung 1 reads the variable from the process environment first. Neither S4, the selftest's DECOY_VARS scrub (selftest.py:348-356) nor `build_arm_env` (selftest.py:1514-1520) removes it.
- **Consequence:** On a node or CI runner where the owner has set it, AC1 to AC3 (90%, 15%, 75%) and KICK-14's 60%/72% criteria print env-sourced shares and go red, or a builder pins the ambient value into the fixture.
- **Fix (skeptic judged SOUND):** In S4, run the window case and every fill case with CLAUDE_CODE_MAX_CONTEXT_TOKENS removed from the child's environment, except AC4, which sets it. Or add the variable to the selftest's ambient scrub beside DECOY_VARS. Have unit 9's call pass the fixture root explicitly. Probe: run the runlog selftest with CLAUDE_CODE_MAX_CONTEXT_TOKENS=500000 exported, and see AC1 stay green.
- **Left-shift gate:** The class is fixture-inherits-ambient-machine-state. Every environment variable a reader consults joins the selftest's scrub list in the same change.

### M14 — KICK-37 AC1's command is green before the unit is built (id 24)

- **Where:** KICK-dKeptSession-37, section 6 AC1.
- **What:** `grep -c 'claude --version </dev/null' skills/session-kickoff/manifest-check.sh` prints 1 at HEAD, from the line inside derive_cli_line. "derive_cli_line calls that function" has no command.
- **Consequence:** S1's extraction has no criterion that can fail. A build that adds read_claude_version with a differently spaced redirect and leaves derive_cli_line's own read in place passes AC1, so the PATH read is written twice, which is the red AC1 names.
- **Fix (skeptic judged SOUND):** Make AC1 observable: grep that derive_cli_line's body (the lines between `derive_cli_line() {` and its closing `}`) contains `read_claude_version` and no `--version`. Or have the arm stub read_claude_version and assert that the `cli —` line uses its answer.
- **Left-shift gate:** Add a checklist entry: every AC command is run at the base revision and must be red there.

### M15 — KICK-44 S7 probes a string that does not measure PreToolUse additionalContext (id 25)

- **Where:** KICK-dKeptSession-44, section 2 S7.
- **What:** S7 re-probes the M5 fact with `grep -a -c 'hookName:`PreToolUse:'`. Its three matches are deny-decision builders. The additionalContext fact sits in a separate schema, `u({hookEventName:A("PreToolUse"),permissionDecision:...,additionalContext:o().optional()})`.
- **Consequence:** The count recorded in unit 21's ledger says nothing about the fact S6 writes into mail-notice.js's header. A harness that dropped the field would keep the same count.
- **Fix (skeptic judged SOUND):** Probe the schema itself, for example `grep -a -c 'hookEventName:A("PreToolUse"),permissionDecision'` with a check that `additionalContext` follows in the same object. Or run a stub PreToolUse hook that returns additionalContext and observe it in a `claude -p` transcript.
- **Left-shift gate:** Add a checklist entry: a platform probe states which matched text carries the fact it certifies.

### M16 — KICK-44 S20 parses a "Child builds" line that is absent for a childless parent (id 27)

- **Where:** KICK-dKeptSession-44, section 2 S20.
- **What:** `gen_build_index.py:1750-1757` prints the `- **Child builds:**` line only when there are children, and an italic no-edge sentence when there are neither parents nor children. S20 does not say what an absent line means, and AC18 tests only the two-child case.
- **Consequence:** A reader built against the many-child form throws or misparses on a childless or edge-less parent, at the transition that posts notices.
- **Fix (skeptic judged SOUND):** State in S20 that an absent "Child builds" line, or the region's no-edge sentence, reads as zero dependents, and add that case to AC18. Better, call the generator's inversion (collect + children) rather than parsing rendered markdown.
- **Left-shift gate:** The class is format-derived-from-arity. A reader of rendered output names its zero, one and many cases.

### M17 — The observation scan implies a second transcript parser beside `extract_session` (id 29)

- **Where:** KICK-dKeptSession-30, section 2 S1 step 2, section 4 "The read".
- **What:** Section 4 says the scan "runs through `extract_session` only where a line needs it", but `extract_session(tree: SessionTree, ...)` (extract.py:843) takes a tree from build_session_tree, not a line. The scan also adds a third copy of the main-transcript glob already spelled in measure_tree (:1135) and measure_ready_tree (:1209).
- **Consequence:** The builder must write a raw-line usage parser, which loses extract_session's main/agent `src` split, its per-request usage de-duplication and its `compactMetadata.preTokens` parse (:742-744). Section 4's "no new parser field" then does not hold.
- **Fix (skeptic judged SOUND):** Specify the scan as `extract_session(build_session_tree(path))` per selected main transcript, filtering events with `kind == 'usage' and src == 'main' and model == model` and `kind == 'compact'`. Allow a byte-level skip only as a pre-filter that never yields a value. Extract the `root.glob('*/*.jsonl')` plus `SID_RE` population into one helper that measure_tree, measure_ready_tree and the scan all call.
- **Left-shift gate:** Add a checklist entry: a reuse claim names the reused function's real signature.

### M18 — KICK-38 reuses an AI_AGENT parse that no unit extracts (id 30)

- **Where:** KICK-dKeptSession-38, section 2 S1 and S2, section 10.
- **What:** Section 10 reuses "derive_cli_line's AI_AGENT parse (manifest-check.sh:414-415)". That parse is inline in derive_cli_line, and KICK-37 S1 extracts only the PATH half. S1's "equals" is undefined against derive_cli_line's field-wise integer compare (a missing field reads 0).
- **Consequence:** The verdict reader spells the `claude-code_` prefix, dash-to-dot and integer parse a second time in the same file, the class KICK-37 rejects for the PATH read. A string compare disagrees with the integer compare on 2.1 against 2.1.0.
- **Fix (skeptic judged SOUND):** Add to KICK-37 S1, or to this unit, the extraction of `read_session_version` from derive_cli_line:413-414, called by both derive_cli_line and read_card_fixture_verdict. Make S1's equality derive_cli_line's integer comparison, extracted as one function. Extend unit 37's AC1, or add an AC here, so that `grep -c 'claude-code_\*' manifest-check.sh` prints 1.
- **Left-shift gate:** Add a checklist entry: a reuse audit row cites a callable, never an inline span.

### M19 — mail-notice.js requires a sibling kit's file (id 31)

- **Where:** KICK-dKeptSession-44, section 2 S9 and S27, section 4 Files touched.
- **What:** S9 binds `tools/unattended/mail-notice.js` through `readCard` and `extractRouteUnits` exported by `tools/hooks/scratch-guard.js:1615`. The hooks kit is agent-cap, which unattended's kit.toml does not require, and S27 adds only playbook-render. gate-guard.js:173-177 records that the install-prefix ban refuses such a require and that an adopter may not hold the kit.
- **Consequence:** The require reds the install-prefix ban, most likely before it ships. If it ships, an adopter with `unattended` and no `agent-cap` gets a hook that throws at require time on every PostToolUse, so a card-routed session hears no mail. AC7 runs in this repo, where both kits are present.
- **Fix (skeptic judged UNSOUND; the skeptic's corrected fix):** In S9, copy `readCard` and `extractRouteUnits` inline into mail-notice.js, naming scratch-guard.js and its line as the source, as gate-guard.js:173-177 does for buildHeredocView. Alternatively, bind only through run-lease.js's resolveLease and a card path the unattended kit owns. Add a criterion that runs `node mail-notice.js` from a scratch install holding only the unattended kit's files and exits 0. Do not keep a require of tools/hooks/scratch-guard.js, even with agent-cap added to requires.
- **Left-shift gate:** That scratch-install criterion, run for every kit hook.

### M20 — KICK-44 S33 runs `emit_progress` under a bare `timeout`, not `run_bounded` (id 32)

- **Where:** KICK-dKeptSession-44, section 2 S33, section 4 Inventory and Evidence.
- **What:** The driver's `run_bounded` with the per-call `RB_BOUND` (unattended.sh:228-265) is "the ONE bounded runner". It records the child for the orphan reaper, and it runs unbounded when no runnable `timeout` exists (GATE_BOUND_LIVE).
- **Consequence:** A hung progress reader cannot be reaped. On a host with no runnable `timeout`, every landing prints `progress not emitted`, so a capability gap reads as a reader failure.
- **Fix (skeptic judged SOUND):** Specify S33 as `RB_BOUND=$PROGRESS_BOUND run_bounded <progress argv>; RB_BOUND=""`, reading the exit and RB_OUT for the NOTE line, and cite unattended.sh:262 in section 10. Keep AC30, and add a stub case with GATE_BOUND_LIVE=0 that still emits.
- **Left-shift gate:** Add a checklist entry: a new bounded call in the driver names run_bounded, or says why not.

### M21 — The `policy fixtures` leg is missing from the policy units' section 7 (ids 34, 35)

- **Where:** Section 7 Gates of KICK-dKeptSession-33, -34 and -40, of KICK-32 (prose only), and of KICK-30, -37, -38, -39, -41, -43 and -44.
- **What:** dGroundRules' `policy fixtures` leg runs `check_policy.py --fixture`. Its guard holds `{prefix}/policy/`, help/policy.md, `{prefix}/runlog/extract.py`, `skills/session-kickoff/manifest-check.sh`, `{prefix}/memory-tree/tree_lib.py`, `{prefix}/hooks/scratch-guard.js` and `{prefix}/unattended/kit.toml`. Specs 33, 34 and 40 add check_policy arms, and the others edit guarded files, yet none names the leg in its backticked leg line. TEMPLATE-SPEC:549-550 requires it.
- **Consequence:** Once dGroundRules lands, a pass that runs only its named legs reuses a stale green for the policy fixtures, including the new arms. The bar still runs guarded legs, and spec tokens would flag the line, which contains the effect.
- **Fix (skeptic judged UNSOUND for id 34; the skeptic's corrected fix, and SOUND for id 35):** Add `policy fixtures` to the backticked leg line in section 7 of specs 30, 32, 33, 34, 37, 38, 39, 40, 41, 43 and 44. A prose mention, as in spec 32, is not what the leg join reads. Adding `policy check` is optional, since it carries no guard. Alternatively for the sibling-kit specs, state once in the build README's rules that every unit runs the legs `check-spec-tokens.py --legs-for` derives against the post-dGroundRules manifest, and cite that rule from each section 7.
- **Left-shift gate:** The class is held-suite-guard-misses-a-sibling-kit. Run `check-spec-tokens.py --legs-for` against each parent build's manifest, not only HEAD's.

### M22 — The `loop selftest` leg is missing from the loop units' section 7 (id 36)

- **Where:** Section 7 Gates of KICK-dKeptSession-35, -36, -42 and -44.
- **What:** Each edits tools/loop/ and declares a new arm in `tools/loop/selftest.py`, but none names dDeclaredLoop's `loop selftest` leg (guard `{prefix}/loop/`, TOOL-dDeclaredLoop-75:126-127). Spec 36 also edits loop_lib.py and omits `loop definition fixtures`.
- **Consequence:** The arms covering spec 42 AC1 to AC4, spec 35 AC1 and AC3, spec 36 AC2 to AC4 and spec 44 AC14, AC15, AC18 and AC26 run under no leg the units name, once the parent lands. The bar's guard-driven run and the spec-tokens join limit the effect.
- **Fix (skeptic judged SOUND):** Add `loop selftest` to section 7 of specs 35, 36, 42 and 44, and `loop definition fixtures` to spec 36. Probe: once dDeclaredLoop lands, `check-spec-tokens.py --legs-for tools/loop/selftest.py tools/loop/loop_lib.py` lists both legs.
- **Left-shift gate:** As M21.

### M23 — KICK-32 calls `cmd_scaffold` "the one caller" of a function check_policy calls five times (id 37)

- **Where:** KICK-dKeptSession-32, section 2 S2, section 4 Files touched.
- **What:** S2 makes `render_scaffold` take no default for `preset`. check_policy.py calls `render_scaffold(rows)` with one argument at :1230, :1498, :1499, :2212 and :4439.
- **Consequence:** Every existing scaffold case raises TypeError, so `policy check` and `policy fixtures` go red. The key count at check_policy.py:1230 changes meaning under a per-preset scaffold. The failure is loud and is cured during the build.
- **Fix (skeptic judged SOUND):** List the five call sites in section 4 Files touched and section 2 S2, and pass an explicit preset at each, `standard` where a fixture wants today's full table. Re-derive the line-1230 key-count expectation under the narrowed scaffold. Correct "the one caller" to the measured population.
- **Left-shift gate:** Add a checklist entry: a signature change cites a `git grep` of its callers at the base revision.

### M24 — The committed `.governance/policy.json` moves, but no spec lists it (id 40)

- **Where:** KICK-dKeptSession-40, section 4 Files touched and Migration, section 7 Gates; KICK-dKeptSession-41, section 3 and section 4.
- **What:** Spec 40 adds the store's blob to `legacy_blobs`. Spec 41 edits catalogue.toml, whose blob the render records as `catalogue_blob`, and section 3 says "policy.json does not move", which is false. Neither lists the file. Spec 41 names `policy check` only in prose, and spec 40 not at all.
- **Consequence:** At the pass, `regen.py --check` refuses on the stale mirror before the first leg, and `arm_mirror_parity` reds `policy check`. The refusal names its own remedy, so the effect is contained.
- **Fix (skeptic judged SOUND):** Add `.governance/policy.json`, rendered by `bash tools/run-gates/run-gates.sh --regen` (the policy kit's `[[generated]]` row, `policy.py mirror --write`), to Files touched in specs 40 and 41. Add `policy check` to both section 7 lists. Add an AC: `python tools/policy/policy.py mirror --check` prints `policy: mirror fresh` at the pass commit.
- **Left-shift gate:** Add a checklist entry: a spec that edits an input of a `[[generated]]` row lists the generated output in Files touched.

### M25 — An other-model compaction lifts every model's rung (id 44)

- **Where:** KICK-dKeptSession-30, section 2 S1 (the observation), section 6 AC3.
- **What:** This is the same defect as H2, found at medium. Compact events carry no model, and S1 takes the largest pre_tokens unfiltered.
- **Consequence:** A 949k Opus compaction puts a haiku or sonnet session on the 1M rung, so its fill reads a fifth of the truth. AC3 roots the fixture alone.
- **Fix (skeptic judged SOUND):** Tie each compact event to the model of its transcript's last main usage before it, or count compactions only from transcripts whose usages are all `model`. Add a criterion: AC3's root plus one transcript with a 900000 `preTokens` compaction on another model still prints `75%`.
- **Left-shift gate:** As H2.

### M26 — No criterion can fail on KICK-33 S4's "refuses any S2 row a preset assigns" (id 47)

- **Where:** KICK-dKeptSession-33, section 2 S4, section 6 AC2, section 7 arm.
- **What:** AC2 plants the prose "each cap's evidence-derived value", which check_value refuses whatever S4 does. S4 never says where check_presets reads the S2/S3 split from, and S1's computed class also holds maintain.fixes and review.<stage>.
- **Consequence:** A preset assigning a valid literal to a `budgets.*` cap or a `roles.effort.*` row loads green and overrides evidence-derived values in every repository naming that preset, the outcome section 4 rejects. If the split is taken from what the store assigns, the refusal is vacuous. It bites only on a later store edit, so the effect is contained.
- **Fix (skeptic judged SOUND):** Define the S2 set as data the check reads, separate from the store's own assignments, for example rows whose v2 cell is identical prose in all four presets, listed or derived from the catalogue. Add a criterion that plants a check_value-valid literal (for example `5`) on one `budgets.*` cap in `strict`, and expects `arm_presets` to red naming `strict` and the key.
- **Left-shift gate:** Add a checklist entry: each refusal rule has one plant that only that rule refuses.

### M27 — KICK-42's acks fail with no session id or offline, and the dependent wedges (id 50)

- **Where:** KICK-dKeptSession-42, section 2 S3, section 5 error states.
- **What:** S3 posts each ack through `--mail post`, which exits 2 with no CLAUDE_CODE_SESSION_ID (KICK-5 S1) and, under KICK-44 S30, when the origin is unreachable. The row then stays open, and the guard, reading the cache under soft, refuses.
- **Consequence:** A transition from an owner's terminal, a CI job or an offline shell is refused while any parent notice is open, and cannot clear itself. The dependent is held until the wait ceiling (72h, or 168h under strict) or a manual ack. It is held, never given a wrong result.
- **Fix (skeptic judged SOUND):** Name both cases in S3 and section 5. Have the guard treat a row the writer could not ack for a "no session id" or "fetch failed" cause as consumed-but-unrecorded, with a NOTE, or refuse with a cause naming the missing session or remote rather than `mail open`. Add a criterion running AC1 with CLAUDE_CODE_SESSION_ID unset.
- **Left-shift gate:** Add a checklist entry: section 5 prices every exit-2 cause of each verb the unit calls.

### M28 — A refused dependency notice is printed and then lost (id 51)

- **Where:** KICK-dKeptSession-35, section 2 S3, section 5 error states.
- **What:** S3 (and KICK-7 S5 for the landing) prints a refused post and lets the transition succeed. No path in the spec set posts a missed notice again. Posts refuse offline (KICK-44 S30) and with no session id (KICK-5 S1).
- **Consequence:** A lost `confirmed` or `changed` holds the dependent on "awaiting confirmed" until a later Design exit or a hand-answered confirm-request. A lost final `landed` holds a design-only dependent forever. The hold fails closed, so the effect is contained.
- **Fix (skeptic judged SOUND):** Add a retry path. The parent's next transition, or `--landed`, compares the notices its transitions owe with those its mail ref holds, and posts the missing ones; content-derived ids make a duplicate refuse safely. Alternatively, record the unposted notice in the transition record and post it at the next item boundary. Add a criterion: the post planted to exit 2 at exit 1, then a second transition, and both dependents hold the exit-1 notice.
- **Left-shift gate:** Add a checklist entry: a write that may be refused names the step that retries it, or says it is lost.

### M29 — S33's bounded call may capture through `$( )`, which waits for a grandchild (id 54)

- **Where:** KICK-dKeptSession-44, section 2 S33, section 6 AC30.
- **What:** S33 runs `emit_progress` "under `timeout`" but does not say where the output goes. AC30's stub sleeps 30 s in the foreground.
- **Consequence:** An `out=$(timeout 10 emit_progress …)` build reports `progress not emitted` on time, but `--landed` blocks until a backgrounded grandchild exits (memory/gotchas/bounded-through-a-pipe-is-unbounded.md). A foreground-sleep stub passes it. The effect is a stalled lander.
- **Fix (skeptic judged SOUND):** In S33, write the bounded call's stdout and stderr to a scratch file, as `derive_cli_line` does (`timeout -k 2 … >"$sf"`), never to a command substitution. In AC30, the stub runs `sleep 30 &` and exits 0, and the wall clock is measured.
- **Left-shift gate:** The class is bounded-through-a-pipe-is-unbounded. Every bounded-call AC stubs a backgrounded grandchild.

## Low

### L1 — KICK-37 AC1 passes at base (ids 12, 55)

- **Where:** KICK-dKeptSession-37, section 6 AC1.
- **What:** This is the same defect as M14, found at low. The grep prints 1 at HEAD, and `grep -c read_claude_version` prints 0. Section 7's arm covers AC2 and AC3, which observe S1's behaviour.
- **Consequence:** AC1 does not decide S1.
- **Fix (skeptic judged SOUND):** Observe the extraction itself: `grep -c '^read_claude_version()' manifest-check.sh` prints 1, the `claude --version` line sits between that function's open and close (an awk range), and derive_cli_line's body contains `read_claude_version`. Keep the count of 1 as the twice-written guard.
- **Left-shift gate:** As M14.

### L2 — A third AI_AGENT parse, and an undefined "equals" (id 13)

- **Where:** KICK-dKeptSession-38, section 2 S1, section 10.
- **What:** This is the same defect as M18, found at low. manifest-check.sh:405-407 already records one re-spelling of the AI_AGENT rule.
- **Consequence:** A third spelling in one file, and a possible string-versus-integer disagreement on 2.1 against 2.1.0.
- **Fix (skeptic judged SOUND):** Extract read_session_version beside read_claude_version, call it from both derive_cli_line and the reader, and state that the comparison is derive_cli_line's field-wise integer compare.
- **Left-shift gate:** As M18.

### L3 — KICK-34 AC2 passes without the unit (id 14)

- **Where:** KICK-dKeptSession-34, section 6 AC2, section 2 S1.
- **What:** KICK-2 S1 already answers None for a key a preset assigns no value. S1 covers a subset of that, as spec-34:24 admits.
- **Consequence:** AC2 reads the same with or without the unit. Only AC1's preset-every-key rewrite is new.
- **Fix (skeptic judged UNSOUND; the skeptic's corrected fix):** Observe AC2 only as a regression arm, and let AC1's rewritten preset-every-key case be this unit's discriminating criterion. Do not add a planted-assignment arm.
- **Left-shift gate:** As M14.

### L4 — KICK-32's rejected alternative is the design's own output (id 15)

- **Where:** KICK-dKeptSession-32, section 4 Alternatives rejected ("Writing only never keys").
- **What:** render_scaffold writes only literal-default rows, and KICK-33 has every preset assign every literal non-never row. So S1 writes only never keys plus comment lines. The stated reason, "rows a preset leaves unassigned would vanish", applies to no row render_scaffold writes.
- **Consequence:** A wrong rationale that would mislead the next change. The shipped file is unchanged.
- **Fix (skeptic judged SOUND):** Restate the alternative as "never keys with no comment lines" (F1's option b), rejected because the posture is hidden. Drop the claim about unassigned rows, which are derived-default rows render_scaffold already skips.
- **Left-shift gate:** None fits. Self-review of Alternatives rejected against the chosen design's output.

### L5 — KICK-39 AC1 reads a `build_records.KINDS` no spec mints (id 26)

- **Where:** KICK-dKeptSession-39, section 6 AC1.
- **What:** Neither PLAY-dOrderedCharter-42 nor -7 names `KINDS`. If it is the imported tuple, the equality holds by construction.
- **Consequence:** The probe either raises AttributeError or cannot fail. The check rests on DOC-42's import refusal alone.
- **Fix (skeptic judged SOUND):** Name the factory's per-kind table as DOC-42 spells it and compare its keys with the tuple. Or drop the second clause and cite DOC-42 S2's import refusal as the observation.
- **Left-shift gate:** Add a checklist entry: every attribute an AC reads is minted by a named spec clause.

### L6 — KICK-33 mints a predicate dGroundRules already has (id 33)

- **Where:** KICK-dKeptSession-33, section 2 S1, section 10.
- **What:** `check_derived(default)` (policy.py:132 at 3c8c4718a) already selects `{derived = …}` defaults, and render_scaffold, read_default_value and check_shape filter on it. Section 10 says no seam fits.
- **Consequence:** A second spelling (for example `"derived" in default`) can class an edge-shaped row differently from the scaffold, and KICK-32 combines the two.
- **Fix (skeptic judged SOUND):** State in S1 that `derive_derived_rows` filters with `check_derived` (rows where `check_derived(r.get('default'))` and the name is outside `never`), and cite policy.py:132 in section 10.
- **Left-shift gate:** Add a checklist entry: a reuse audit that says "no seam fits" cites the grep it ran.

### L7 — Five specs name user-doc changes no Files touched line lists (id 41)

- **Where:** Section 5 user docs against section 4 Files touched of KICK-dKeptSession-43 (help/orientation-card.md), -35, -36 and -42 (help/loop.md) and -40 (tools/policy/README.md).
- **What:** Each section 5 names a text change (35:111, 36:112, 40:106, 42:124, 43:110) that no Files touched line lists and no AC observes.
- **Consequence:** The help pages stay stale against the charter's docs rule. There is no behavioural effect.
- **Fix (skeptic judged SOUND):** Add help/orientation-card.md to spec 43's Files touched, help/loop.md to those of specs 35, 36 and 42, and tools/policy/README.md to spec 40's. Give each spec one grep AC, for example `grep -n "GOV_BASH" help/loop.md`, and `grep -n "skipped"` within orientation-card.md's actions.free section.
- **Left-shift gate:** Add a checklist entry: every path section 5 names appears in Files touched.

### L8 — KICK-44 swaps two `.memory-tree.conf` line citations (id 42)

- **Where:** KICK-dKeptSession-44, section 4 Evidence, first paragraph.
- **What:** Line 633 holds ARMS_FLOORS and line 649 holds REFUSAL_CEILINGS. The spec cites them the other way round.
- **Consequence:** Only the addresses are wrong. The values and the key names S23 edits are right.
- **Fix (skeptic judged SOUND):** Cite `ARMS_FLOORS` (`.memory-tree.conf:633`) and `REFUSAL_CEILINGS` (`:649`).
- **Left-shift gate:** None fits. Self-review.

### L9 — Section 7 names the python resolver leg but no leg that runs the loop arms (id 53)

- **Where:** Section 7 Gates of KICK-dKeptSession-36, -35 and -42.
- **What:** `tools/lib/resolve-python.test.sh` has no resolve_bash or tools/loop reference. The arms sit in `tools/loop/selftest.py`, which no named leg line runs. The python resolver leg is named correctly, because its guard `{prefix}/` trips on any tools/ path. The merge bar runs every leg anyway.
- **Consequence:** The spec does not document which leg runs its arms. What gets checked is unaffected.
- **Fix (skeptic judged UNSOUND; the skeptic's corrected fix):** Keep the leg lines as they are. Under each of the three specs' section 7, add a prose line like spec 5's: "the loop kit's leg `loop transition record` joins the manifest with TOOL-dDeclaredLoop-3; the close runs tools/loop/selftest.py there."
- **Left-shift gate:** The class is hand-named-gate-list-green-while-the-bar-reds. Section 7 names the leg that runs each new arm.

### L10 — KICK-35 has no text for the no-ordinal refusal (id 56)

- **Where:** KICK-dKeptSession-35, section 5 error states against section 2 S3.
- **What:** Section 5 says an unreadable transition log is "refused by S3's line". S3's line needs a post's rc and first line, and in that case no post runs.
- **Consequence:** The builder has no specified text and may print a fake rc. No behaviour changes.
- **Fix (skeptic judged SOUND):** Add the no-ordinal form to S3, for example `notice — not posted <kind> to build:<dependent> · no Design-exit ordinal: <why>`, and a criterion that plants an unreadable transition log.
- **Left-shift gate:** Add a checklist entry: every error state in section 5 has its printed line in section 2.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=56 confirmed=56 refuted=0 unverified=0 blocker=0 high=11 medium=34 low=11 agents=11 out-tokens=274008

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-38.md:header order 9; section 3 Edges (consumes-from KICK-dKeptSession-37); also KICK-31 header order 16 vs KICK-5 | high | medium | confirmed | I re-read the headers. KICK-38 is order 9, and its section 3 lines 57-58 consume read_claude_version from KICK-37, also order 9. KICK-31 is order 16, and its line 63 consumes KICK-5's --mail post, also order 16. gen_build_index.py:1717 says 'Units sharing an `order` value are the parallel group', and README.md lists step 9 (13, 37, 38) and step 16 (31, 5) as 'yes'. The README order is wrong. I grade it medium, not high: BUILD-METHOD's parallel-when-disjoint clause (2) ('neither depends on the other's output') would make a dispatcher that follows M6 run these in sequence, so the effect is a misleading label rather than a certain stall. | sound | - |
| 2 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-37.md:header order (and the same for KICK-33, -34, -40, -32, -30, -35, -42); section 4 Files touched | medium | medium | confirmed | I extracted the '### Files touched' lists. Step 2: 19 and 33 both list tools/policy/check_policy.py. Step 4: 3, 34 and 40 all list policy.py and check_policy.py. Step 9: 13, 37 and 38 all list manifest-check.sh, card-store.fixture.sh and manifest-check.test.sh. Step 13: 30 and 9 both list extract.py and selftest.py. Step 16: 31 and 5 both list unattended.sh, unattended.test.sh and the VERBS files. Step 25: 35 and 42 both list loop_transition.py and selftest.py. The README marks every one of these groups parallel, which contradicts BUILD-METHOD clause (1). The effect is contained, because the dispatcher records write sets before it dispatches. | sound | - |
| 3 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-35.md:section 6 AC1 Red when; section 7 New arm (selftest.py); section 4 Alternatives rejected | high | high | confirmed | KICK-31 S1 builds the id from eight fields, kind and content-key among them. KICK-7 S4 posts confirmed first and changed after that, each carrying --interface and so a content key. Over A, B, A the three posts are (confirmed, A), (changed, B) and (changed, A). Without --pass no two of them share an id: exits 1 and 3 differ in kind, and exits 2 and 3 differ in key. So the staged break AC1 names cannot go red, and the line in spec-35's Alternatives rejected ('A to B to A ... would collide with the first notice') is false. AC1 also pins no interface texts. The proposed fix works: the same text at exits 2 and 3, or A, B, A, B, gives two changed posts with an equal key and recipient, which collide once --pass is dropped. | sound | fixture-passes-by-finding-nothing |
| 4 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-42.md:section 2 S2 ('earlier by first-seen') | high | high | confirmed | spec-42:37-43 acknowledges 'every earlier open confirmed or changed ... earlier by first-seen'. spec-27 S5 says the check 'never chooses a row by first-seen, seq or fetch order'. Its red-case table has changed K2 arriving first and confirmed K1 arriving later. In that case K1 has the later first-seen, so S2 leaves it open, and KICK-5 S9's guard refuses on an open row. That is a stall on the take-over reordering path. The fix's first option is sound. Its second option, 'ack every row except a changed whose key is not current', is not: it would leave an older superseded changed (a stale key from an earlier exit) open, and that recreates the same stall. | unsound | - |
| 5 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-36.md:section 2 S1-S2 and section 3 Non-goals (scope of the bare-bash class) | medium | medium | confirmed | A grep for resolve_bash across the spec set finds it only in spec-36, spec-42:45/68 (the ack), spec-44:88-89 (S16 and S17) and spec-5:155. KICK-7 S4 (line 66) runs '--mail post ... as a subprocess' with no resolver named. KICK-7 S3 (line 41) even spells a bare 'bash <kit>/unattended.sh --claims'. KICK-42 S2 runs check_interface_notice from write_transition with no resolver. spec-36 records that a bare bash launched from Windows python reaches WSL2, and its Non-goals scope the unit to the guard and to unit 44's reads. So on this node the dependency notices, and the interface check, launch through an unresolved shell. | sound | - |
| 6 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-36.md:section 4 Design (S1 'the contract of govkit.py:1144 carried inline', section 3 'This copy keeps govkit's contract so that extraction replaces it unchanged') against section 7 Gates | medium | medium | confirmed | grep for resolve_bash, GOV_BASH and System32 in tools/lib/resolve-python.test.sh prints nothing. PARITY_ROWS (lines 168-184) has no resolve_bash row. git grep counts 10 'def resolve_bash' definitions. spec-36 section 7 names the 'inline parity' leg, and section 3 promises extraction 'unchanged', but nothing holds the copy to govkit's contract. The first fix option does not work: the parity arm compares the blocks byte for byte. govkit.py:1176 raises Refusal('govkit: GOV_BASH is set ...'), while S1 requires the loop copy to raise LoopError, so a row with govkit as the canonical would go red on the first build. | unsound | second-implementation-is-not-a-second-opinion |
| 7 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-33.md:section 2 S2 and S4 (review.<stage>), section 6 AC1 | medium | medium | confirmed | The catalogue at 3c8c4718a:1206-1208 has review.<stage> with default = { derived = "opt-in; Build owed" }. spec-33 S2 says the store assigns the concrete keys review.design and review.build, and never the pattern. S4, however, exempts only S2's six rows from the standard-equals-default rule, and judges by named members only an S3 row. KICK-1 S2's rule ('the standard table equals each row's literal catalogue default') has no literal to compare review.design or review.build against. The rule for these keys is therefore unstated: the builder either reds the store AC1 says exits 0, or invents a rule. | sound | - |
| 8 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-31.md:section 2 S1 ('KICK-dKeptSession-22 S4's act joins as the ninth field') and S4 (the superseded list) | medium | medium | confirmed | spec-22:45-46 reads 'the act is a seventh field of S2, appended after `answers`', and spec-22:65's hands-off external says the act 'joins S2 as a seventh field'. spec-31:38-39 says it 'joins as the ninth field'. spec-31 S4 supersedes only KICK-22 S2's 'six fields', AC2 and KICK-5 S5, so S4 and the hands-off line are left standing, giving the act two positions. | sound | two-answers-to-one-question |
| 9 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-40.md:section 4 Migration | medium | medium | confirmed | In git show 3c8c4718a:tools/policy/policy-mirror.js, lines 111-118, `legacy` is Object.keys(doc.legacy_blobs), and legacyStale iterates only those recorded keys. A mirror that has no presets.toml key therefore reads fresh. spec-40's Files touched lists only policy.py and check_policy.py, so the JS is not changed. The Migration line ('reads it stale once') is false. The window is narrow (mirrors rendered between this build's orders 3 and 4, or any mirror that is not re-rendered), but within it the hooks keep reading old preset values. | sound | - |
| 10 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S2 (derive_context_fill default root) | medium | medium | confirmed | spec-30 S2 (lines 45-49): measure_context_fill derives the window under the transcript's own projects root, while derive_context_fill(ev, window=None) derives it 'under the default root ... so KICK-9's per-stage rows read ... with no change to their call'. spec-9:41 calls derive_context_fill(ev), and spec-9:177-178 sets its fixture under %TEMP%. So the two readers can disagree on the same transcript, and each per-event call starts a 20-transcript scan; section 5 measures one scan at 0.84 s. | sound | - |
| 11 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-39.md:header order 17 against KICK-dKeptSession-5 (order 16); section 1 Goal | medium | medium | confirmed | KICK-5 is order 16, and its S12 adds the mailbox-message factory row. KICK-39 is order 17, and its Goal says that PLAY-dOrderedCharter-42 S2 refuses build_records' import when the kinds differ from TYPED_RECORD_KINDS, which 'breaks every kind'. PLAY-dOrderedCharter-42 AC2 (line 156) pins that set equality. spec-5 section 7 (line 326) names no build-index or memory-tree factory gate, so the break between the two passes goes unseen at KICK-5's pass. | sound | - |
| 12 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-37.md:section 6 AC1 | medium | low | confirmed | At HEAD, `grep -c 'claude --version </dev/null' skills/session-kickoff/manifest-check.sh` prints 1, at line 419 inside derive_cli_line() (line 411), and no read_claude_version exists. So AC1's only command already passes before the unit is built. Its 'inside read_claude_version' and 'derive_cli_line calls that function' clauses have no command behind them. I grade it low: AC1 states those observations in prose, and AC3 also observes S1. | sound | - |
| 13 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-38.md:section 2 S1 and section 10 Reuse audit (the AI_AGENT parse) | low | low | confirmed | manifest-check.sh:405-407 says the AI_AGENT rule is 'spelled again here', :414 parses it inline inside derive_cli_line, and :428-433 compares field by field as integers with a missing field read as 0. Spec-37 S1 pulls out only the PATH half (read_claude_version). Spec-38 S1 says 'equals the version AI_AGENT names now' and never defines equality, and its §10 reuses 'derive_cli_line's AI_AGENT parse', which no function exposes. A builder therefore writes a third copy of the parse, and a string compare would disagree with the integer compare on 2.1 against 2.1.0. | sound | - |
| 14 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-34.md:section 6 AC2 and section 2 S1 | low | low | confirmed | Spec-2 S1 (line 39) already says 'A preset that assigns the key no value answers None'. Spec-34 S1 answers None only for derived rows the preset's assignment does not hold, which is a subset of the case KICK-2 already covers, and spec-34:24 admits as much. Once KICK-2 and KICK-33 are built, AC2's preset-derived-cap read behaves the same with or without this unit, so it cannot decide the unit. Only AC1's rewrite of preset-every-key is new. | unsound | - |
| 15 | coherence | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-32.md:section 4 Alternatives rejected ('Writing only never keys') | low | low | confirmed | Spec-32 §4 Evidence: render_scaffold writes only rows that are SCAFFOLD_OWNER and not derived. Spec-33 S2 lists the unassigned rows, and all are derived-default. Its completeness rule has every preset assign every other non-never row. So S1 writes only never keys plus comment lines, which matches the strict example at :78-90. The rejected alternative 'Writing only never keys' is therefore the design's own output, and its stated reason (unassigned rows would vanish) applies to no row render_scaffold writes. | sound | - |
| 16 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S1 step 2, section 4 Evidence (extract_session fields) | high | high | confirmed | extract.py:818-821 builds compact events as {t, kind, src, trigger, pre_tokens} with no model field, while usage events carry model (:834-836). Spec-30 S1 step 2 folds in 'the largest pre_tokens of the compact events' without filtering by model. One 1M compaction therefore moves every model on the node to the 1M rung, including the 95946-max claude-opus-4-8 named in §4. AC1-AC4 use one model and no compact event, so none of them catches it. The consequence only shows on a node that mixes models, so the grade is high. | sound | - |
| 17 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S1 step 1, section 4 Evidence (the installed harness) | medium | medium | confirmed | A grep -a of /c/Users/daily-agent/.local/bin/claude.exe printed `let g=a.CLAUDE_CODE_MAX_CONTEXT_TOKENS;if(g!==void 0&&g>0&&yv(e))return g;` and `function yv(e){...let g=r.toLowerCase();return!g.startsWith("claude-")\|\|g!==s}`. The harness honours the variable only when that gate passes, which it does not for a canonical first-party claude- model. Spec-30 S1 step 1 lets the variable win unconditionally and calls it the model's real window, so for claude-opus-5-5 the computed fill can drift from the window the harness actually compacts at. | sound | - |
| 18 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S1 (root default) and S2 (derive_context_fill default root), section 10 | medium | medium | confirmed | extract.py:185-198 already defines resolve_projects_root, which returns $CLAUDE_CONFIG_DIR/projects before <home>/.claude/projects. Spec-30 S1 hard-codes '~/.claude/projects' as the default root, and §10 does not name resolve_projects_root. selftest.py:348-349 aims CLAUDE_CONFIG_DIR at a decoy, and a literal ~ path would bypass that. | sound | - |
| 19 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S4, section 6 AC1-AC3 | medium | medium | confirmed | `grep -n CLAUDE_CODE_MAX tools/runlog/selftest.py` printed nothing. selftest.py:348-356 handles only the five DECOY_VARS and GIT_*. Spec-30 S4 does not say the window case clears the variable, yet S1 reads it first. AC1-AC3's fixed percentages would therefore turn red wherever the variable is set in the environment. | sound | fixture-inherits-ambient-machine-state |
| 20 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S2 (derive_context_fill), section 3 non-goal 'A cache', section 5 perf | medium | medium | confirmed | Spec-30 S2 has derive_context_fill(ev) with no window derive the window under the default root on every call, and §3 forbids a cache. Spec-9 S2 (lines 36-42) computes context = derive_context_fill(ev) for every main and agent file row. My probe of the newest 20 main transcripts read 201 MB in 0.12 s on bytes alone, and spec-30 §5 itself measures 0.84 s per parsed scan. N rows therefore cost N scans, and §5 times only one call. | sound | - |
| 21 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-34.md:section 2 S1, section 4 'The answers' table, section 6 AC1 and AC2 | high | high | confirmed | At 3c8c4718a, policy.py:695-698 has read_default_value raise DerivedDefault for any {derived=...} default, and the docstring at :213-216 says 'get and the mirror refuse it ... the caps module alone reads it'. budgets.py:270 catches it through read_key(..., unset=policy.DerivedDefault). No sibling spec changes get's refusal, since spec-34 is the only match for DerivedDefault in the spec set. AC1's roles.effort.default 'with source default' and AC2's `policy.py get <cap> --explain` printing a derived value therefore cannot pass unless `get` computes a derived value. budgets.py has a `resolve` verb (main at :367-372), which the fix's re-point uses. | sound | - |
| 22 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-40.md:section 4 Migration | high | high | confirmed | At 3c8c4718a, policy-mirror.js:111 takes the input list from Object.keys(doc.legacy_blobs) of the mirror itself, and :117-118 and :142 mark the mirror stale only when a recorded id differs or the policy or catalogue blob differs. A mirror rendered before this unit has no presets.toml key, so that input is never compared, and with an unchanged policy file and catalogue the mirror reads FRESH. Spec-40 §4 Migration ('reads it stale once') and §5 risks are false against this code. The defect bites on the upgrade path. | sound | - |
| 23 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-36.md:section 2 S1, section 3 non-goal 3, section 6 AC2 | medium | medium | confirmed | govkit.py:1176-1183 accepts GOV_BASH whenever `<cand> -c :` exits 0, with no uname test and no System32 filter on the override. The System32/WindowsApps filter and check_runs apply only to PATH candidates. My probe of /c/Windows/System32/bash.exe -c 'uname -s' printed Linux with rc=0. A copy of govkit's contract therefore accepts the AC2 override, while spec-36 S1's added uname test and AC2's refusal leave govkit's contract. That contradicts non-goal 3's 'keeps govkit's contract so that extraction replaces it unchanged'. | sound | - |
| 24 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-37.md:section 6 AC1 | medium | medium | confirmed | `grep -c 'claude --version </dev/null' skills/session-kickoff/manifest-check.sh` prints 1 at HEAD, and the match is the line inside derive_cli_line (:418). Spec-37 AC1's command is therefore green before the unit is built. Its other half, 'derive_cli_line calls that function', names no command, so nothing in AC1 can fail on the extraction. | sound | - |
| 25 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md:section 2 S7 | medium | medium | confirmed | spec-44:60-62 S7 does probe with `grep -a -c 'hookName:`PreToolUse:'`. Over /c/Users/daily-agent/.local/bin/claude it printed 3, and all three snippets are `hookName:`PreToolUse:${n.name}`,...reason:` permission-result/deny builders. The additionalContext fact sits in a separate schema, `u({hookEventName:A("PreToolUse"),permissionDecision:...,updatedInput:...,additionalContext:o().optional()})`, which appears twice. So the recorded count does not measure the fact that S6 writes into the header. | sound | - |
| 26 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-39.md:section 6 AC1 | low | low | confirmed | spec-39:110-112 AC1 reads `build_records.KINDS`. DOC-42 S2 (:40-44) says the factory imports TYPED_RECORD_KINDS 'as its kind list' and refuses at import a per-kind table whose keys differ, but it names no `KINDS` attribute; grep over DOC-42 and DOC-7 finds none. If KINDS is the imported tuple, the equality holds by construction. If it does not exist, the probe raises. | sound | - |
| 27 | grounding | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md:section 2 S20 | low | medium | confirmed | gen_build_index.py:1750-1757 prints the italic no-edge sentence when there are neither parents nor children, and otherwise emits a `- **Child builds:**` line only `if vals`. spec-44 S20 (:100-103) reads the dependents from the 'Child builds' line and never says what an absent line means. AC18 only tests the two-child case. A reader built from S20 can fail at notice time on a childless parent, which changes behaviour, so I grade it above low. | sound | format-derived-from-arity |
| 28 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S1 step 2 and S2; section 10 | high | high | confirmed | spec-30:40-41 defaults `root` to the literal `~/.claude/projects`, and section 10 names no resolver. tools/runlog/extract.py:185-198 `resolve_projects_root` honours the override and then `$CLAUDE_CONFIG_DIR/projects`, and runlog.py:246/300/324/360 route every verb through it with `--transcripts`. S2 sends the default-root path to derive_context_fill for unit 9's rows. Built literally, a node with CLAUDE_CONFIG_DIR set gets 'no observation' and the 200000 rung: the same wrong-window consequence on a narrow path. | sound | - |
| 29 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S1 step 2; section 4 "The read" | medium | medium | confirmed | spec-30:112-113 says the scan parses lines and 'runs through `extract_session` only where a line needs it'. But extract.py:843 is `extract_session(tree: SessionTree, ...)`, and the tree comes from build_session_tree(main) at :238, so nothing can be called per line. Meanwhile §4 (:98-100) claims 'no new parser field'. The wording pushes the builder toward a raw-line parser beside extract_session's compact parse at :744. The same glob is spelled at :1135 and :1209. | sound | - |
| 30 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-38.md:section 2 S1 and S2; section 10 | medium | medium | confirmed | manifest-check.sh:413-414 holds the AI_AGENT parse inline in derive_cli_line (`case "${AI_AGENT:-}" in claude-code_*) ...`), and the comparison is field-by-field as integers with a missing field read as 0 (:427-432). spec-37 S1 (:33-38) extracts only the PATH half. spec-38 S1 (:34-35) says the recorded cli 'equals the version AI_AGENT names now', and section 10 (:148-149) cites the inline parse as reused. No unit extracts it, so a second spelling follows, and a plain string equality can disagree with the integer comparison. | sound | - |
| 31 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md:section 2 S9 (and S27's requires change); section 4 Files touched | high | medium | confirmed | spec-44:68-69 S9 binds through `readCard` and `extractRouteUnits` 'exported by tools/hooks/scratch-guard.js:1615'. Both names are in that module.exports. tools/hooks/kit.toml is id agent-cap. unattended/kit.toml:12 requires memory-tree, review-harness, settings-merge and kickoff-manifest only, and S27 adds only playbook-render. gate-guard.js:173-177 records that requiring a sibling kit's file is refused by the install-prefix ban and that an adopter may not hold the kit. The defect is real, but the ban most likely reds the build before it ships, which keeps the effect contained, so I grade it medium, not high. | unsound | - |
| 32 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md:section 2 S33; section 4 Inventory and Evidence | medium | medium | confirmed | spec-44:137-139 S33 runs emit_progress 'under `timeout`' with PROGRESS_BOUND=10. unattended.sh:233 defines RB_BOUND, :262 run_bounded, and :266-295 init_bounded, which records the child and runs unbounded when GATE_BOUND_LIVE!=1 (probed at :183-186). A bare `timeout` skips the orphan record, and on a host with no runnable timeout it fails every call, printing 'progress not emitted'. The driver does have other bare timeouts (:484, :1823), so this is not a ban. The effect is contained. | sound | - |
| 33 | reuse | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-33.md:section 2 S1; section 10 | low | low | confirmed | `git show 3c8c4718a:tools/policy/policy.py` printed `132:def check_derived(default): return isinstance(default, dict) and set(default) == {"derived"}`. spec-33:37-38 mints derive_derived_rows to select `{derived = …}` defaults, and its section 10 says no seam fits. `grep -rn check_derived memory/builds/dKeptSession` printed nothing. | sound | - |
| 34 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-33.md:section 7 Gates (likewise spec-34 section 7 and spec-40 section 7) | high | medium | confirmed | At 3c8c4718a, gate-legs.json holds `policy fixtures` (argv check_policy.py --fixture), whose guard includes `{prefix}/policy/` and help/policy.md. The section-7 leg lines of specs 33, 34 and 40 name only lexicon, memory hygiene and spec tokens. TEMPLATE-SPEC:549-550 requires the leg line to name every guard-tripped leg. tools/policy does not exist at HEAD, so the gap opens when dGroundRules lands. The bar still runs guarded legs on the diff, and spec tokens would flag the leg line, so the claim that the arm 'never runs' is overstated. I grade it medium. `policy check` has no guard, so the rule does not require it. | unsound | held-suite-guard-misses-a-sibling-kit |
| 35 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 7 Gates (likewise specs 37, 38, 39, 41, 43 and 44 section 7) | medium | medium | confirmed | The 3c8c4718a `policy fixtures` guard lists `{prefix}/runlog/extract.py`, `skills/session-kickoff/manifest-check.sh`, `{prefix}/memory-tree/tree_lib.py`, `{prefix}/hooks/scratch-guard.js`, `{prefix}/unattended/kit.toml` and `{prefix}/policy/`, which covers spec 41's catalogue. None of the named specs carries that leg in section 7. HEAD's manifest has no policy legs, so the miss opens only after dGroundRules lands, as the finder says. | sound | held-suite-guard-misses-a-sibling-kit |
| 36 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-42.md:section 7 Gates (likewise spec-35, spec-36 and spec-44 section 7) | high | medium | confirmed | `grep -c 'loop selftest'` printed 0 for specs 35, 36, 42 and 44. Each one's Files touched includes tools/loop/selftest.py, and spec 36 also has loop_lib.py. TOOL-dDeclaredLoop-75:126-127 gives the guards `loop definition fixtures` <- loop_lib.py, loop.toml and `loop selftest` <- `{prefix}/loop/`. dDeclaredLoop is a declared parent (README:9). This breaks TEMPLATE-SPEC's guard-leg rule once the parent lands. The bar's guard-driven run and the spec-tokens join limit the effect, so I grade it medium, not high. | sound | held-suite-guard-misses-a-sibling-kit |
| 37 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-32.md:section 2 S2 | high | medium | confirmed | I ran `git grep -n render_scaffold 3c8c4718a -- tools`. It printed five one-argument callers in check_policy.py (:1230, :1498, :1499, :2212, :4439), plus the def at policy.py:1313 and cmd_scaffold at :1493. Spec-32 S2 calls cmd_scaffold 'The one caller' and makes `preset` required, so a call that names none raises TypeError (AC3 even asserts this). Its Files touched lists only the new `scaffold-preset` case in check_policy.py. Built as written, the existing fixture cases go red. That failure is loud and the builder cures it during the build, so I grade it medium rather than high. | sound | - |
| 38 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S1 step 2 and S2 | high | high | confirmed | Spec-30 S1 says `root` defaults to `~/.claude/projects`. S2 derives the root two ways: the transcript's parent's parent, or the default root. extract.py:185-198 already has `resolve_projects_root`, which honours override and then CLAUDE_CONFIG_DIR, and runlog.py:246/300/324/360 route every root through it. Section 10 of spec-30 does not name it. The runlog selftest's `build_arm_env` (selftest.py:1514-1520) points every root variable at scratch, so a hard-coded `~/.claude/projects` default escapes that isolation. Unit 9's `derive_context_fill(ev)` would then read the node's real tree. On a CLAUDE_CONFIG_DIR node the window is derived from the wrong tree, which is the unit's own defect on a narrow path. | sound | two-readers-of-one-config-one-re-derived |
| 39 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-31.md:section 2 S1 and S4 | high | high | confirmed | A grep printed spec-22:65 'hands-off external — dWellOiledMachine's Runtime, whose act joins S2 as a seventh field' and spec-31:39 'joins as the ninth field'. Spec-22 S4 (lines 45-47) reads 'the act is a seventh field of S2, appended after `answers`'. Spec-31 S4's superseded list names only spec-22 S2's 'six fields', AC2, and spec-5 S5. It leaves spec-22 S4 and the hands-off edge standing, and those are the contract the child build reads. Their position contradicts this build's eight-field order. | sound | - |
| 40 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-40.md:section 4 Files touched and Migration, section 7 Gates (likewise spec-41 section 4) | medium | medium | confirmed | At 3c8c4718a, kit.toml has a [[generated]] row for `.governance/policy.json`, rendered with `mirror --write` and checked with `mirror --check`. The tracked policy.json records `catalogue_blob`. run-gates.sh runs `regen.py --check` before the first leg and refuses on a stale output, and check_policy.py:23-24 describes `arm_mirror_parity`. Spec-40 changes `legacy_blobs`, and spec-41 edits catalogue.toml. Spec-41 §3 even claims 'policy.json does not move', which is false because catalogue_blob changes. Neither spec lists policy.json in Files touched. Spec-41 §7 names the `policy check` leg only in prose, and spec-40 not at all. The effect is a loud preflight refusal that names its own remedy, so it is contained. | sound | - |
| 41 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-43.md:section 5 user docs vs section 4 Files touched (likewise specs 35, 36, 40, 42) | medium | low | confirmed | I printed the Files touched sections of specs 35, 36, 40, 42 and 43. None lists help/loop.md, help/orientation-card.md or tools/policy/README.md, yet each spec's §5 'user docs' line names a text change to one of them (35:111, 36:112, 40:106, 42:124, 43:110). No AC observes any of those changes. `grep -c GOV_BASH` on spec-5 printed 0. Only docs are left stale, with no behavioural effect, so I grade it low. | sound | - |
| 42 | blast-radius | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md:section 4 Evidence, first paragraph | low | low | confirmed | `sed -n 633p .memory-tree.conf` printed `ARMS_FLOORS=...` and line 649 printed `REFUSAL_CEILINGS=...`. Spec-44:199-200 cites REFUSAL_CEILINGS first and ARMS_FLOORS second, as (`:633`, `:649`), so the two line numbers are swapped. Only the cited addresses are wrong. | sound | - |
| 43 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S1 (rung 2), section 5 risks | high | high | confirmed | Spec-30 S1 rung 2 takes the largest observation per model across the newest 20 transcripts. §4 Evidence states the model field reads `claude-opus-5-5` whatever the window, and AC2 asserts that a 150k transcript read beside a 900k sibling prints 15%. On a node that runs both windows on one model, a 200k session is therefore measured against the 1M rung. §4 rejects 'a larger pinned constant' for exactly that result. §5 risks covers only the opposite direction. This is a wrong fill on a mixed-window node, so `fresh-at-boundary` never fires for those sessions. | unsound | - |
| 44 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S1 (the observation), section 6 AC3 | medium | medium | confirmed | `sed -n 818-821p tools/runlog/extract.py` shows the compact event built as {t, kind, src, trigger, pre_tokens} with no model key, while usage events carry `model` (:835). Spec-30 S1 filters usage events by `model` but takes 'the largest `pre_tokens` of the `compact` events' with no filter. A compaction on one model therefore lifts every model's rung. AC3 roots the fixture alone, so no criterion can see this. The effect is contained to other-model sessions on such a node. | sound | - |
| 45 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S2, section 3 (non-goal: a cache), section 5 perf | medium | medium | confirmed | Spec-30 S2 has `derive_context_fill(ev)` derive the window on every call when none is passed. Spec-9 S2 line 41 calls `derive_context_fill(ev)` once per orient row, and §5 prices one scan per call at 0.84 s. §3's non-goal ('A cache... One scan costs under a second') rests on a per-call price that ignores the number of rows. It withholds a cache but does not address the rows-times-scan cost. The fix's alternative, passing `window=` once per session, needs no cache. | sound | - |
| 46 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-30.md:section 2 S1 rung 1 and S4, section 6 AC1-AC3 | medium | medium | confirmed | Spec-30 S1 rung 1 reads CLAUDE_CODE_MAX_CONTEXT_TOKENS from the environment, and §4 quotes the harness telling owners to set it. The runlog selftest's `build_arm_env` (selftest.py:1514-1520) copies os.environ and only redirects root variables, so nothing removes this variable. Spec-30 S4 does not say to remove it either. AC1-AC3 and spec-14's 60%/72% criteria would print other shares on a node where the owner set it. The variable is unset on this node today, so the effect is a red suite on such a node, which is contained. | sound | - |
| 47 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-33.md:section 2 S4, section 6 AC2, section 7 arm | high | medium | confirmed | Spec-33 S4's rule 'refuses... any S2 row a preset assigns' has no criterion that can fail on it. AC2 plants the prose 'each cap's evidence-derived value', which §1 says check_value already refuses, so AC2 stays red whether or not S4's second rule exists. §7's arm is staged only by that prose plant. S4 also never says where check_presets reads the S2/S3 split from: S1's computed class includes both `maintain.fixes` and `review.<stage>`. It would bite only when a later store edit assigns a valid literal to a derived row, so the effect is contained. | sound | - |
| 48 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-40.md:section 4 Migration, section 6 AC2 | high | high | confirmed | `git show 3c8c4718a:tools/policy/policy-mirror.js` lines 111-118 build `legacy` from `Object.keys(doc.legacy_blobs)` of the stored mirror, and mark it stale only when one of those recorded ids differs. A mirror rendered without a presets.toml key never has the store compared, so it reads FRESH. That contradicts spec-40 §4 Migration ('reads it stale once'). AC2 renders the mirror after the unit lands, so it cannot catch this. Hooks would serve old preset values as FRESH whenever an old mirror persists without a re-render. | sound | - |
| 49 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-42.md:section 2 S1, section 4 Alternatives rejected | high | high | confirmed | I re-read spec-42 S1. It acks every open landed, superseded and withdrawn row 'before KICK-dKeptSession-5 S9's guard reads the open rows'. No output line is specified, and nothing makes the ack wait for the guard's verdict on the other rows. So a withdrawn row is acked even when an open question then refuses the transition. Spec-10 S3 says under mailbox.reads=transitions-only 'runs no read ... read at transitions'. The transition is then the only place mail is read, and S1 consumes a withdrawn notice there without showing it. That is the very 'withdrawn parent pass unread' that §4 rejects. Under the every-item default, unit 10's interrupt only shows the row if it arrived before the last item boundary. This is a narrow path, but the dependent ends up building on a parent that was withdrawn. | unsound | - |
| 50 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-42.md:section 2 S3, section 5 error states | medium | medium | confirmed | Spec-5 S8 defines `--mail ack` as 'a post of kind ack'. Spec-5 S1 says a post with no CLAUDE_CODE_SESSION_ID prints 'mail — not written: no session id' and exits 2. Spec-44 S30 makes a failed or timed-out fetch in `--mail post` exit 2. Spec-42 S3 says a failed ack leaves the row open and the guard refuses. Spec-5 S6 reads under soft, so offline the guard still reads the cache and still sees the row. Spec-42 §5 prices neither the no-session case nor the offline case. The dependent stays held until a manual ack or unit 24's deadline. The effect is contained: the run is held, never given a wrong result. | sound | - |
| 51 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-35.md:section 2 S3, section 5 error states | high | medium | confirmed | Spec-35 S3 prints a refused post and lets the transition succeed. Spec-7 S5 does the same for the landing. A grep for re-post, retry and 'owed' over the spec set finds no path that posts a missed notice again. Spec-44 S30 makes posts refuse when the origin is unreachable, and spec-5 S1 when there is no session id. The finder overstates one part. A lost `changed` does not make the dependent build against the old interface: spec-7 S3's gate recomputes the key over the current listing, finds no matching row, and holds with 'awaiting confirmed'. The real consequence is a hold that fails closed: it lasts until a later Design exit, until a confirm-request is answered by hand, or forever for a final `landed` that a design-only dependent waits on. Contained, so medium. | sound | - |
| 52 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-36.md:section 2 S1, section 6 AC2 | medium | medium | confirmed | I read govkit.py:1170-1179. The GOV_BASH path is `if check_runs(override): _BASH = override; return _BASH` with no System32 or WindowsApps test; the filter applies only inside the PATH loop. I re-ran `/c/Windows/System32/bash.exe -c 'uname -s'`: it printed Linux and rc=0. Spec-36 S1 tells the builder to carry govkit's contract, and §3 says the copy 'keeps govkit's contract so that extraction replaces it unchanged'. S1 places the System32 refusal and the uname check under 'then the candidates'. AC2, though, demands that a System32 GOV_BASH raises. The spec contradicts itself, and copying govkit as written lets the WSL launcher in through the override. | sound | - |
| 53 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-36.md:section 7 Gates (also spec-35 §7 and spec-42 §7) | medium | low | confirmed | I grepped tools/lib/resolve-python.test.sh (666 lines) for resolve_bash, loop_lib and tools/loop: no match. tools/loop does not exist at this base. So the python resolver leg does not grade the new resolver, and none of spec-35, -36 or -42's §7 leg lines names a leg that runs tools/loop/selftest.py. The finder misreads why spec-36 names the leg. Its gate-legs.json guard is `{prefix}/`, which any tools/ path trips, and TEMPLATE-SPEC §7 requires naming every leg whose guard trips. The merge bar runs every leg regardless of §7. The gap is in what the spec documents, not in what gets checked, so low. | unsound | hand-named-gate-list-green-while-the-bar-reds |
| 54 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md:section 2 S33, section 6 AC30 | medium | medium | confirmed | memory/gotchas/bounded-through-a-pipe-is-unbounded.md exists and records the class: `$( )` waits until a surviving grandchild closes the pipe, while timeout has already reported 124. Spec-44 S33 says only that emit_progress 'runs under `timeout`' with PROGRESS_BOUND=10. It does not say where the output goes. AC30 stubs the verb 'to sleep 30 s' and does measure the clock ('within 12 s'). A plain foreground sleep is killed by timeout either way, so AC30 passes for a build that captures with `$( )`, and that build blocks when the sleep is backgrounded. The defect depends on the builder's choice, and its effect is contained to a stalled lander. | sound | bounded-through-a-pipe-is-unbounded |
| 55 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-37.md:section 6 AC1 | low | low | confirmed | At HEAD, `grep -c 'claude --version </dev/null' skills/session-kickoff/manifest-check.sh` printed 1, and `grep -c read_claude_version` printed 0. AC1's command is therefore green before anything is built. Its second half, 'derive_cli_line calls that function', has no command. §7's arm covers AC2 and AC3 only. AC2 and AC3 observe the behaviour, so this is only a weak criterion. | sound | - |
| 56 | failure-envelope | memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-35.md:section 5 error states vs section 2 S3 | low | low | confirmed | Spec-35 S3's line is `notice — not posted <kind> to build:<dependent> · rc <n> · <the post's first line>`, built from a post's exit code and first line. §5 says that with an unreadable transition log 'the post is then refused by S3's line rather than posted with a guessed pass'. In that case no post runs, so there is no rc and no first line to print. No criterion plants an unreadable log. The result is an unspecified message format with no change in behaviour. | sound | - |
