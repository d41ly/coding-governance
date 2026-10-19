**Serves:** diff-review PLAY-dClosedLoop-1

# Tier-2 review: the night pass two of PLAY-dClosedLoop-1 (run A)

Provenance: run A of two independent runs on the same diff. Round 1. Finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

Range: e1a54ac672b37d558bf5095608e9b378827b414a...ad54fe38875a1e95c3b8cd39aad19ff276ad3d7f

## Verdict: CLEAN WITH FIXES

There are no blockers.
One item is high: the problem register's create-only key admits one problem per path and cannot name a dotfile path.
By item, the tally is 0 blocker, 1 high, 20 medium and 4 low (25 items).
By raw confirmed finding, it is 0 blocker, 1 high, 26 medium and 4 low (31 findings).
This was a light-intensity run, so it is not a full review.
The security and intent lenses did not run, and their classes were covered only through the checklist items shared out to the other lenses.

## Subjects reviewed

The diff is the night pass two, worked unattended at the owner's word. Its record is `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`. It was reviewed as a design change.

- 0657a8667 opens the record with the owner's seven points verbatim and the research handoffs.
- 43bd58baa, point 1: scenarios (NT-1 to NT-9).
- f27b6e3b2, point 2: aScoutedSeam and `build.reuse-check` (NT-10 to NT-13).
- dff70c5f8, point 3: storage, the SQLite index and the mail refs (NT-14 to NT-17).
- da51d45c4, point 4: handoffs, the registers and the derived message ids (NT-18 to NT-21).
- d171bcb47, point 5: caps and `budgets.enforce` (NT-22 and NT-23).
- 723abc12b, point 6: bug classes (NT-24 to NT-26).
- ad54fe388, point 7: agent-cap and `runtime.agents-in-flight` (NT-27 and NT-28).

## Review shape

Intensity light: raw 41, confirmed 31, refuted 10, unverified 0 (0 uncertain), precision 0.76.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 15 | 11 | 4 | 0 | 0 | 0.73 |
| seams | yes | 14 | 12 | 2 | 0 | 0 | 0.86 |
| verification | yes | 12 | 8 | 4 | 0 | 0 | 0.67 |

### Run integrity

- All 3 of 3 lenses returned, and none died.
- All 5 of 5 skeptic batches returned, and none died.
- No contradictory verdict was demoted to unverified, no spurious verdict was discarded, and there were no duplicates.
- Fixes on confirmed findings: 30 judged sound, 1 judged UNSOUND (id 30, whose corrected fix is given below), 0 with no fix proposed, 0 not judged.
- Severity: the skeptic graded every confirmed finding, and re-graded 2 of them from high to medium (ids 1 and 30).
- Unverified findings: none.
- No lens notes were supplied, so every lens ran on the kit's generic brief.
- Intent: 33 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 26 items, shared out as correctness 9, seams 9 and verification 8.
- The finding set is complete for the three lenses that ran. It is not evidence about the security or intent classes.

## Items

Paths below are under `memory/builds/dClosedLoop/build/`, shortened as v2 (`2026-10-14-…-architecture-v2.md`), night (`2026-10-19-…-night-pass-two.md`), systems, fates, flow-steps, coordination, layer-instruction, layer-roles and flow-roles-adoption.

### HIGH

#### H1. The problem register keeps one problem per path and cannot key dotfile paths (id 2)

- **Where:** v2:1502 (dPlacedRequest).
- **What is wrong:** Problems live at `refs/gov/problems/<subject key>`, each ref "written once … refused when it exists". A second, distinct problem on the same path is refused. `git check-ref-format` rejects `refs/gov/problems/.governance/policy.toml`, `.githooks/pre-push`, `x.lock` and any key with a space. The handoffs research (prior-art S3) keys problems by subject for intersection only and never makes them create-only per subject; the fold added that rule.
- **Consequence:** Every later problem on a file is lost, and its refusal reads as a duplicate. No problem can be filed against the policy file, the hooks or `.claude/`, the design's most guarded paths.
- **Fix (the skeptic judged it sound):** Key each problem as `refs/gov/problems/<encoded subject>/<problem id>`, the id derived from the finder's act and the problem's content. Encode the subject into a legal ref (escape a leading dot, `.lock`, spaces, `:` and `~`). Keep create-only on the full key. Add red arms for two distinct problems on one path and for a dotfile path.
- **Left-shift gate:** A design check that runs every ref template the records name through `git check-ref-format` over the tree's real paths, including dotfiles.

### MEDIUM

#### M1. dGroundRules re-points agent-cap's readers but keeps its 1..5 clamp and its script rules (id 1)

- **Where:** v2:1497 (dGroundRules), against night:534 and `tools/hooks/agent-cap.js:107`, `:492`, `:500`, `:553`, `:1653-1654`, `:2266`.
- **What is wrong:** The clause retires the slot ledger, `.agent-cap.conf`, the AGENT_CAP refusal and the print mode, and re-points their readers to `runtime.agents-in-flight`. The night record's point 7 table also gives dGroundRules the raw `parallel`/`pipeline` ban and the concurrency half of the bound rule, but no v2 clause carries them. agent-cap.js holds every bound at `min(declared, 5)` and refuses a declared cap outside 1..5.
- **Consequence:** Until dBoundRoles retires agent-cap.js, an owner raise above 5 (NT-28) stays clamped at 5, or blocks every spawn if the re-pointed reader feeds the 1..5 validation. The fold lands in the night record but not in v2. The skeptic graded this medium because the finder's "denies every call" holds only on the second reading.
- **Fix (the skeptic judged it sound):** In the same dGroundRules unit, retire rule 1 and the concurrency half of rule 3, and drop the 1..5 validation and the `min(…,5)` clamp. Add an arm: with `runtime.agents-in-flight = 8` planted, a direct spawn and a registered harness call are both admitted.
- **Left-shift gate:** A fold-landing check: every row of a night record's "rule moved to" table must match a clause in the named build's v2 row.

#### M2. The over-budget refusal survives in the layer records after point 5 moved it under `budgets.enforce` (ids 3, 21)

- **Where:** layer-instruction:461-468 (R-C), layer-roles:76 and :380-381, `2026-10-19-…-adopter-instructions.md:170` and :202.
- **What is wrong:** Point 5 narrowed `instructions.checks` to a missing required unit and put the size half under `budgets.enforce`, warning by default (v2:706, :798, :1024, systems:207). These lines still say the render refuses a set over budget, that `instructions.checks=warn` lets an over-budget set load, and that a block over its budget is refused. The diff edited both layer files elsewhere and left these lines.
- **Consequence:** These are the sources the dOrderedCharter and dBoundRoles builders read. A builder following them wires a hard refusal under the old switch, against the owner's directed default.
- **Fix (the skeptic judged it sound):** Revise each sentence, with a revision note: over budget warns or refuses as `budgets.enforce` says, a harness's own limit still refuses, and a set missing a required unit is refused under `instructions.checks`.
- **Left-shift gate:** A stale-text sweep run by each fold: grep the design records for every phrase the fold's [Folded] list names as replaced (here "refuses a set over budget", "over its budget is refused").

#### M3. The night record says the harness settings queue, but the direct-spawn setting refuses (ids 4, 24)

- **Where:** night:514-515, against `research-agent-cap.md:87-88`; dGroundRules' witness at v2:1497.
- **What is wrong:** The record says the harness settings "queue where agent-cap refused". The research says `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` refuses a direct spawn with "Do not retry" and is not enforced under ultracode. Only the Workflow setting queues. The table's "retired: the harness queues" row is correct for Workflow script rules only.
- **Consequence:** The design expects a direct spawn over the limit to wait when it fails, and under ultracode direct spawns are unbounded. dGroundRules' witness exercises only a Workflow run.
- **Fix (the skeptic judged it sound):** Correct the sentence: Workflow agents queue, a direct spawn over the limit is refused and must be retried, and the direct setting is exempt under ultracode. Add a direct-spawn arm to dGroundRules' acceptance that records whether it is refused or queued. Record the ultracode exemption as a gap owned by the build whose ledger closes it.
- **Left-shift gate:** A research-fidelity checklist entry: each claim a fold attributes to a research return cites the return's line, and the reviewer checks the quote.

#### M4. Point 5 drops the research's third kept class and NT-22 never offers its pick (id 6)

- **Where:** night:395 ([p5-caps] item 1), night:60 (dispatch 134 row), night:581 (NT-22), against `research-caps.md:111-114`.
- **What is wrong:** The research keeps three classes outside the switch, the third being format-defining grammar limits (the one-line 200 chars, entry lengths). The record says "Two things stay outside it" and folds the opposite, putting line and entry lengths under the switch, without saying it departs from the research. NT-22's options never include the research's pick.
- **Consequence:** The owner rules on a fork that hides the research's recommendation. Under `warn` a one-line rule over its grammar length passes, and a parser relying on that format can misread it.
- **Fix (the skeptic judged it sound):** Report the third class in [p5-caps] and the dispatch row. Add the research's pick to NT-22 as an option (grammar limits keep refusing), or state why the fold departs from it.
- **Left-shift gate:** A fork-row check: each NT fork whose section cites a research pick must list that pick among its options.

#### M5. No build owns retiring the per-pass checklist and the prebuild (ids 7, 35)

- **Where:** night:457-458 and NT-24 (night:583); v2:1505 (dFurnishedOrders), v2:1513 (dScopedBuild).
- **What is wrong:** Point 6 says the unattended per-pass checklist and the prebuild retire. No v2, gap-register, flow-steps or fates clause retires them; dFurnishedOrders changes only its work-order field. dScopedBuild still carries "the checklist witnessed", closing gap-build-04. The product still runs them: `tools/unattended/SKILL.template.md:121` and `tools/memory-tree/BUILD-METHOD.template.md:190` run `gotchas.py --for-diff HEAD~1..HEAD`, `:168` runs `--for-paths`, and the research names `unattended-build.template.js:561`, `unattended-unit.js:322` and the `prebuild` at `unattended-unit.js:43-51`.
- **Consequence:** Selection by write set, at its measured 18%, keeps running after the chain lands, and one build clause witnesses what the fold retires.
- **Fix (the skeptic judged it sound):** Add the retirement to the build that owns the unattended driver (dWellOiledMachine, or dFurnishedOrders beside its field): the Skill's per-pass call, BUILD-METHOD's prebuild and `--for-paths` lines and the `prebuild` hook, readers inventoried by value, an upgrade step, and a check red on a planted pass that still calls `gotchas.py --for-paths`. Revise dScopedBuild's "checklist witnessed" to match.
- **Left-shift gate:** An ownership check: every "retires" in a night record's answer names a build row whose clause carries that retirement.

#### M6. The mail ref is keyed by node, not by writer, and two records name different keys (id 9)

- **Where:** coordination:100 and v2:1503 (dKeptSession), against `memory-plan:237` and night:265.
- **What is wrong:** The ref is `refs/gov/mail/<slug>/<fleet tag>`, and a fleet tag names a node (coordination:93-103). memory-plan, revised in this diff, says `<sender>`, a sender being (fleet tag, session, build). The research measured 80 attempts for 80 messages with 8 writers on 8 refs, one writer per ref.
- **Consequence:** Several sessions on one node (which `build.unit-holders` invites) share a ref and contend under compare-and-swap, so the cited 1.0x figure does not apply to the fold's own key.
- **Fix (the skeptic judged it sound):** Key the ref by the writer, `refs/gov/mail/<slug>/<fleet tag>/<session>`, or state that one node's sessions serialise. Use one template in coordination, v2 and the memory plan.
- **Left-shift gate:** A template-consistency check that extracts every `refs/gov/...` template from the design records and reds when one ref has two spellings. Id 29 (L4) is the low-graded record of the same inconsistency.

#### M7. Derived message ids collide for distinct messages and are undefined for senders with no act (id 10)

- **Where:** v2:1503 (dKeptSession), night:325.
- **What is wrong:** The id is derived from the sender's act, item, kind and subject, and a repeated id is refused as a duplicate. Two `ack`s or `answer`s from one item to two different messages on one subject derive one id. The owner and attended sessions post too (coordination item 7) and have no act. The answered id, a field of every message, is left out of the key.
- **Consequence:** The second legitimate ack is refused as a retried post, and the transition gate waits forever for a reply that cannot be written.
- **Fix (the skeptic judged it sound):** Derive the id from the sender's session or act, the item and pass, the kind, the subject and the answered id (or a content digest). Plant two acks to two different messages from one item and require both to land; plant a retried identical post and require it refused.
- **Left-shift gate:** A bug-class checklist entry for idempotency keys: list the distinct legitimate events that share every key field.

#### M8. The index keys path-derived rows by blob alone (id 11)

- **Where:** systems:188-191, the same keying in v2's dOrderedCharter and dTotalRecall clauses.
- **What is wrong:** The fold says rows are keyed by blob and "a tree is a set of blobs". A tree is a set of (path, blob) entries: `git ls-tree -r e1a54ac67` shows 8 blobs at 24 paths. Path-derived rows (the `doc` namespace, `path#symbol`, `path:line` citations) cannot be keyed by blob alone. The research's probe schema keyed by path.
- **Consequence:** `gov tag where` returns one or an ambiguous path, and deleting one copy can drop rows the other copy needs, against "a deleted file rebuilds to identical rows".
- **Fix (the skeptic judged it sound):** State that the index keeps a (tree, path) to blob table, keys content rows by blob and path-derived rows by (path, blob). Add a rebuild-equality arm over a planted tree where one blob sits at two paths and one is deleted.
- **Left-shift gate:** A test fixture with a duplicated blob, required by any index-keying clause.

#### M9. `budgets.enforce` lists `record` with no meaning or arm (id 16)

- **Where:** v2:1112, night:394; readers at v2:706, :798, :1111, systems:207; witness at v2:1497.
- **What is wrong:** The row offers `warn, refuse, record`, carried over from the retired `annotations.budget`. Every reader is binary (warns or refuses), and the witness plants only `warn` and `refuse`. Under the research, `warn` already journals every breach, so `record` is undistinguished.
- **Consequence:** An owner who selects `record` gets undefined behaviour while the catalogue reads complete.
- **Fix (the skeptic judged it sound):** Drop `record` from the row and night:394, or define it (counted in the value ledger, not shown) and add its arm to dGroundRules' witness: an over-cap file that passes silently and leaves a ledger row.
- **Left-shift gate:** Class `policy-value-with-no-route`: a catalogue check that every listed value of a key has a named arm in some build's witness.

#### M10. The fates record still keeps agent-cap.js (id 17)

- **Where:** fates:160.
- **What is wrong:** The row reads STAYS ("spawn-guard pack; its arm becomes a fragment; slot reservation added (dWellOiledMachine)"). Point 7 retires `tools/hooks/agent-cap.js` in dBoundRoles (night:540, v2 dBoundRoles). The diff edited only fates' `gov-session` row.
- **Consequence:** A chain build reading the fates record keeps agent-cap.js and adds a reservation to it.
- **Fix (the skeptic judged it sound):** Revise the row to RETIRED: rules moved per [p7-agent-cap]'s table, the file retired in dBoundRoles with an upgrade step, pending NT-27.
- **Left-shift gate:** A fates-sync check: a tool named as retiring in any v2 row cannot read STAYS in the fates table.

#### M11. The fates record still selects bug classes by write set (ids 18, 34)

- **Where:** fates:103.
- **What is wrong:** The `gotchas.py` row says classes are "handed by write set through `gotchas.py --for-paths` (dFurnishedOrders)". v2 dFurnishedOrders now renders them "from the classes the unit's spec names, never selected by its write set" (point 6, pending NT-24).
- **Consequence:** Two records contradict each other, and a retirement inventory reading fates keeps `--for-paths` as a live surface.
- **Fix (the skeptic judged it sound):** Revise the row: classes ride the work order as the unit's spec names them; `--for-paths` serving retires with the per-pass checklist and the prebuild (point 6, pending NT-24); review keeps selection by range minus fully gated classes (NT-25).
- **Left-shift gate:** The fates-sync check of M10, extended to each row's cited build clause.

#### M12. The systems shapes registry still bounds the agent cap by `FANOUT_CAP` (ids 19, 32)

- **Where:** systems:426 (cited also as :425).
- **What is wrong:** It reads "The agent cap is bounded by agent-cap's `FANOUT_CAP`, never a new value". The same diff retired `FANOUT_CAP` into `runtime.agents-in-flight` at v2:924, v2:1504 and layer-runtime:942, and point 7's [Folded] list omits this bullet.
- **Consequence:** A dBoundRoles builder reading the systems record bounds shapes by a conf key dGroundRules deletes.
- **Fix (the skeptic judged it sound):** Revise to: each stage's agent cap is at or under `runtime.agents-in-flight` (revised 2026-10-19, the night pass two, point 7; it was agent-cap's `FANOUT_CAP`).
- **Left-shift gate:** A retired-identifier sweep: after a fold retires a name, grep the live design records for it outside revision notes.

#### M13. The adoption record's fixed set still names `FANOUT_CAP` (id 33)

- **Where:** flow-roles-adoption:198.
- **What is wrong:** The fixed set, the rows a repository patch may never widen, lists "Shapes: the kinds, `FANOUT_CAP`'s bound and the five lens slots". The diff edited the same list at :191-193 and left this line.
- **Consequence:** A check derived from the list pins a key that no longer exists or never pins `runtime.agents-in-flight`, so an overlay could widen a shape's fan past the owner's limit unchecked.
- **Fix (the skeptic judged it sound):** Replace it with "each stage's cap at or under `runtime.agents-in-flight`", marked revised by the night pass two, point 7, pending NT-27.
- **Left-shift gate:** Class `amendment-leaves-its-other-half-standing`, caught by the retired-identifier sweep of M12. Id 20 (L3) is the low-graded record of the same line.

#### M14. The in-flight ledger counts a Workflow's agents twice (id 22)

- **Where:** v2:1509 (dWellOiledMachine), layer-runtime:436-438.
- **What is wrong:** A Workflow call reserves its declared fan, and each of its agents also claims a slot at SubagentStart. Admission compares agents in flight plus reservations to the limit, and nothing draws the reservation down as the call's own agents claim. The reservation is held until the run's saved result.
- **Consequence:** At limit 5 a running fan-3 Workflow counts as 6, so a direct spawn the limit allows is refused.
- **Fix (the skeptic judged it sound):** State that a Workflow agent's SubagentStart claim converts one slot of its call's reservation, matched by run or parent id. Plant: limit 5, a fan-3 Workflow running, one direct spawn admitted.
- **Left-shift gate:** A checklist entry for reservation ledgers: every claim path names the reservation it consumes.

#### M15. Between dGroundRules and the ledger, the session-wide limit is unenforced and untested (ids 23, 30)

- **Where:** v2:1002 (the key's row), v2:1497 (dGroundRules), night:518-520; `research-agent-cap.md:87`, :89, :97.
- **What is wrong:** The key bounds agents in flight in one session, direct spawns and Workflow agents together. dGroundRules renders it into two harness settings, one per scope (direct spawns, one Workflow run), and retires agent-cap's slot ledger in the same unit. The total arms only with dWellOiledMachine's ledger, after a spike that may fail. The only check is a four-agent Workflow overlapping at most two under a limit of two; nothing tests direct spawns. The spike-fail fallback names no split rule and no carrier for "one live run per session". The catalogue row states neither the interim split nor the ultracode exemption, and no gap records the shortfall. The skeptic graded id 30 medium: the check does not claim the combined bound, so "certifies" overstated it.
- **Consequence:** At a limit of N a session can hold N direct agents plus N per Workflow run, 2N or more, through the window and indefinitely if the spike fails.
- **Fix:** For id 30 the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix. Add a direct-spawn arm to dGroundRules: with the key at 2, three background Agents never overlap more than two. Have the catalogue row state the interim enforcement (separate direct and per-Workflow-run budgets each equal to the key) and the ultracode exception. Land the combined-total red case in dWellOiledMachine with the in-flight ledger, seen red before the ledger and green after. For id 23 (judged sound): have dGroundRules record the interim meaning as a gap, and name the fallback's split rule (for example direct = ceil(N/2), Workflow = floor(N/2)) and the item that enforces one live run per session, each with a planted witness.
- **Left-shift gate:** Class `rule-stated-with-no-check-that-fails`: a catalogue check that a key's stated scope has a witness arm per scope it names, from the build that first reads the key.

#### M16. A declined scenario promotion has no record and is re-raised every review (id 27)

- **Where:** v2:1516 (dCalibratedLens), night:114-115.
- **What is wrong:** Under `flow.promote: loop-proposes`, the Loop Review proposes a scenario from a change two or more builds carried, for the owner to ratify. Nothing records a decline or suppresses re-proposal.
- **Consequence:** Each weekly Loop Review re-raises an item the owner already refused. The tree fixed this class for `loop.propose`'s retire proposals with keep records (layer-expansions:259, :263).
- **Fix (the skeptic judged it sound):** Record a decline keyed by the change's content, suppressing the proposal until a build carries a changed form. Plant a declined proposal that is not re-raised next review.
- **Left-shift gate:** Class `owner-item-without-its-reject-outcome`: a check that every owner-ratified proposal names its decline record.

#### M17. `build.reuse-check` has no route for a disputed row (id 28)

- **Where:** flow-steps:232, v2:1513 (dScopedBuild).
- **What is wrong:** A `duplicate` or `bypassed` row routes only to a fix pass. The acceptance bars are 29 and 31 of 35, so wrong rows are expected, yet the builder cannot dispute one and re-entry is unbounded.
- **Consequence:** A false positive cycles the unit through scope, reuse-check and fix pass with no owner route, or forces a rewrite toward a wrong "nearest existing symbol".
- **Fix (the skeptic judged it sound):** Let the fix pass return `disputed` with a reason, routed to the closing review or an owner item. Bound reuse-check re-entries per unit. Plant a false `duplicate` to exercise the route.
- **Left-shift gate:** Class `route-names-an-output-its-actor-never-emits`: a flow-steps check that each step judged by an imperfect scout has a dispute outcome and a re-entry bound.

#### M18. `budgets.enforce`'s check is one file, not a census, and never tests what must stay outside it (id 31)

- **Where:** v2:1497 (dGroundRules), v2:1499 (dOrderedCharter); `research-caps.md:9`, gap-found-34.
- **What is wrong:** The switch is read by every gate enforcing a size cap, with consumer limits and correctness checks left outside. Its only check is one over-cap file under `warn` and `refuse`. Nothing exercises the 24 caps (18 refusing), the `record` value, or the halves that must stay outside.
- **Consequence:** A gate keeping its own hard refusal passes, and so does a correctness refusal (a missing required unit, a harness-limit overflow) wired to the switch, which would warn under the default.
- **Fix (the skeptic judged it sound):** Make the check a census: every leg the caps research lists is planted over its cap under each of `warn`, `refuse` and `record`, red if any ignores the switch. Add red arms where `warn` still refuses a set missing a required unit and a composition over a harness's own limit.
- **Left-shift gate:** Class `rule-stated-with-no-check-that-fails`: a switch "read by every X" carries a census witness over the inventory of X.

#### M19. The `gov-session` retirement names no reader inventory and no check (id 36)

- **Where:** v2:1509 (dWellOiledMachine).
- **What is wrong:** The clause retires `gov-session` with an upgrade step only. Other retirements in v2 inventory readers by value (agent-cap at :1504, /build at :1517, the receipt schema at :1498). `git grep gov-session ad54fe388` finds AGENTS.md, `tools/hooks/agent-cap.test.sh`, `tools/hooks/scratch-guard.test.sh`, `tools/roles/README.md`, `adopt-roles.test.sh`, `agents/gov-session.agent.md`, `check_roles.py`, `kit.toml` and `workflows.toml`.
- **Consequence:** The retirement leaves dangling roster rows or red tests, and no check goes red on a surviving reader.
- **Fix (the skeptic judged it sound):** Inventory those readers by value, re-point each to the `intake` message or the placement offer in the same unit, and see the check red on a planted leftover reference to `gov-session.agent.md`.
- **Left-shift gate:** Class `retirement-inventory-misses-readers-by-value`: a design check that every "retired" clause names its reader inventory and its red check.

#### M20. Units past the reuse-check's cap of sixty read clean (id 37)

- **Where:** flow-steps:232, night:191.
- **What is wrong:** Added units are "capped at sixty with an overflow line". The join requires only that every listed unit has a row, and the outcome is "clean → the unit built". Unlisted units are never checked and the step still reads clean. The cap from aScoutedSeam bounds the prompt, not the step's verdict.
- **Consequence:** On large units, where duplicates are likeliest, a skip reads as a pass. The closing review still runs afterwards, which contains the effect.
- **Fix (the skeptic judged it sound):** Make an overflow line non-clean: route the remainder to a further pass, or record it as an unchecked set the closing review must answer. Plant 61 added units whose 61st is a duplicate, which must not read clean.
- **Left-shift gate:** A checklist entry: any capped input list makes its overflow an explicit outcome, never clean.

### LOW

#### L1. The night record and review-system still state what point 7 refuted (id 12)

- **Where:** night:36, :77, :144; `review-system` line 166.
- **What is wrong:** Night:144 ("Caps above five wait on point 7") has no pointer to point 7's answer. Review-system:166, new in this diff, says "the hook counts slots", but the hook retires and v2's dFairHearing gives that check to the merge bar. Lines 36 and 77 describe how the pass ran and today's state, so they are milder.
- **Consequence:** A reader can take the wrong carrier from the prose; behaviour is unaffected.
- **Fix (the skeptic judged it sound):** Add revision notes at night:36 and night:144 ("settled by point 7"). In review-system:166 change "the hook counts slots" to "the merge bar's harness check counts slots".
- **Left-shift gate:** The retired-identifier sweep of M12, run over the night record's own earlier sections.

#### L2. The gotchas population is misstated (id 13)

- **Where:** night:442, against `research-gotchas.md:55`.
- **What is wrong:** The record says the lookup ran on "47 closed reviews whose appendices carry a classes column". The research found 66 such appendices, 47 with a range, and 19 design reviews excluded.
- **Consequence:** The population and its exclusions are hidden. The cited figures (6.2%, 82 of 1,317) are unaffected.
- **Fix (the skeptic judged it sound):** Revise to: of the 66 review appendices with a classes column, the 47 that carry a range.
- **Left-shift gate:** A checklist entry: a figure names its population and its exclusions.

#### L3. The adoption record's fixed set names `FANOUT_CAP` (id 20)

- **Where:** flow-roles-adoption:198.
- **What is wrong:** The same stale line as M13, graded low by this finder and skeptic because v2 is the authority and names the new key.
- **Consequence:** Wording only.
- **Fix (the skeptic judged it sound):** Replace it with "`runtime.agents-in-flight`'s bound on each stage's cap", citing point 7. M13's fix covers this.
- **Left-shift gate:** As M13.

#### L4. coordination and memory-plan spell the mail ref differently (id 29)

- **Where:** coordination:100, :103; `memory-plan:237`; night:265.
- **What is wrong:** The same defect as M6, graded low: the ref "one per sender" is keyed `<fleet tag>` while a sender is (fleet tag, session, build), and memory-plan keys it `<sender>`. The research (prior-art probe B', measured return :153) measured one writer per ref.
- **Consequence:** An inconsistency between records; the contention consequence is carried by M6.
- **Fix (the skeptic judged it sound):** Key the ref by the full sender, `refs/gov/mail/<slug>/<fleet tag>/<session>`, or state that one node serialises its sessions' posts. Make memory-plan:237 match. M6's fix covers this.
- **Left-shift gate:** As M6.

## Refuted, for the record

Ten findings were refuted (ids 5, 8, 14, 15, 25, 26, 38, 39, 40, 41); the appendix gives each reason. Id 15 duplicates id 16. Id 26's fix was judged unsound, but the finding itself was refuted.

review-shape kind=diff-review round=1 intensity=light at=synth raw=41 confirmed=31 refuted=10 unverified=0 blocker=0 high=1 medium=26 low=4 agents=9 out-tokens=186064

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1497 | high | medium | confirmed | v2:1497's dGroundRules clause retires only agent-cap's slot ledger, `.agent-cap.conf`, the AGENT_CAP refusal and the print mode, and re-points their readers. The night record's point 7 table (night-pass-two:534) assigns 'the raw `parallel` and `pipeline` ban, and the concurrency half of the bound rule' to dGroundRules. No clause in v2, and none in the layer-runtime diff, carries that retirement. In tools/hooks/agent-cap.js, the script rules hold every bound to EFFECTIVE_CAP, which is min(declared, MAX_VERIFIERS=5) (:492, :553, :2266), and :1653-1654 refuse a declared cap outside 1..5. So a limit the owner raises above 5 stays clamped at 5 by agent-cap's script rules until dBoundRoles, or blocks outright if the re-pointed reader feeds agent-cap's 1..5 validation. Either way the fold lands in the night record and not in v2. The finder's 'denies every call' holds only on the second reading. | sound | - |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1502 | high | high | confirmed | v2:1502 (dPlacedRequest) defines create-only registers, 'each ref written once by compare-and-swap and refused when it exists', with problems at `refs/gov/problems/<subject key>` keyed by a path. Under that rule a second, distinct problem on the same path is refused. I re-ran `git check-ref-format`: refs/gov/problems/.governance/policy.toml, .githooks/pre-push, x.lock and a key with a space are all BAD, while tools/x.py is OK. The handoffs research (prior-art S3 at :307) only requires that a problem's subject intersect a later item's seed. Neither research return makes problems create-only per subject. Built as written, the register loses problems and cannot key the guarded dotfile paths. | sound | - |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:461 | medium | medium | confirmed | The point 5 fold (night-pass-two [p5-caps] items 1-2, v2's `instructions.checks` row) narrows `instructions.checks` to a missing required unit and moves the over-budget half under `budgets.enforce`. The cited text still states the replaced behaviour: layer-instruction:461-468 ('The render refuses a set over budget' and 'Under `instructions.checks=warn`, the set loads whole'), layer-roles:76 and :380-381 ('A block over its budget is refused'), and adopter-instructions:202 ('the render refuses'). This diff edited layer-instruction only at :292 and left R-C as it was. These are design sources the dOrderedCharter and dBoundRoles builders read. | sound | - |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:515 | medium | medium | confirmed | night-pass-two:515 says the harness settings 'queue where agent-cap refused', covering both settings. research-agent-cap:87 says `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` 'refuses with "Do not retry". It is not enforced under ultracode', and :88 says only the Workflow setting's queued agent() calls wait. The record misstates its return for direct spawns and omits the ultracode exemption. | sound | - |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1002 | medium | - | refuted | The design states the scopes it enforces truthfully. dGroundRules' clause (v2:1497) says the harness settings cover 'one session's direct spawns and one Workflow run'. The session-wide total is assigned explicitly to dWellOiledMachine's in-flight ledger (v2 dWellOiledMachine row; night-pass-two:518-522), and the fallback is named there: 'the limit split between direct and Workflow budgets with one live run per session', which follows research-agent-cap:140. The catalogue row gives the key's meaning, staged to its enforcer. How the split divides the value is unit-level detail, owed to the chain builds by design. This is not a misstatement introduced by the fold. | sound | - |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:395 | medium | medium | confirmed | research-caps section 6 (:111-114) keeps three classes outside the switch, the third being 'grammar limits that define a format (the one-line 200 chars, entry lengths)'. night-pass-two [p5-caps] item 1 says 'Two things stay outside it' and folds the opposite: 'Line and entry lengths are size caps too, so they fall under the switch'. It does not say that this departs from the research. The dispatch 134 outcome row (line 60) also lists only consumer limits and correctness checks. NT-22's options (night-pass-two:581) offer no option matching the research's pick. The record misreports its return. | sound | - |
| 7 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1505 | medium | medium | confirmed | NT-24 (night-pass-two:583) and [p6-gotchas] item 1 say the unattended per-pass checklist and the prebuild retire. I grepped v2, the gap register, flow-steps and fates for prebuild, per-pass checklist, for-diff and for-paths: no build row retires them. v2 changes only dFurnishedOrders' field (:1505) and dFairHearing's charter line. The product still runs them: tools/unattended/SKILL.template.md:121 and tools/memory-tree/BUILD-METHOD.template.md:190 run `gotchas.py --for-diff HEAD~1..HEAD` per pass, and :168 runs `--for-paths`. The fates record (:103) still says classes are 'handed by write set through `gotchas.py --for-paths` (dFurnishedOrders)'. | sound | - |
| 8 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1500 | medium | - | refuted | The ancestry is as the finder states: dLinkedLibrary descends from dDeclaredLoop, which descends from dFairHearing. But the claim that the filter 'has no data' when dFairHearing lands is not borne out. research-gotchas:109-111 measured gate status from 'each class record as it stands today' (50 fully gated, 14 partly gated, 84 ungated). The class records already carry 'Gated by …' declarations, which tools/memory-tree/gotchas.py reads through DECLARES_RE (:74), and several memory/gotchas records carry them. dLinkedLibrary formalises the three-valued field. dFairHearing's filter can run on the status the records hold today, so the unit is not unrunnable. | sound | - |
| 9 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md:100 | medium | medium | confirmed | coordination:100 and v2:1503 (dKeptSession) key the mail ref as `refs/gov/mail/<slug>/<fleet tag>`, while memory-plan:237, revised in this diff, says `refs/gov/mail/<slug>/<sender>`. Two records name different keys for one ref, though night-pass-two:265 claims all three were revised alike. coordination:93-103 makes the fleet tag a node identity, while a sender is fleet tag, session and build. research-storage-measured:114 measured 80 attempts for 80 messages with 8 writers on 8 refs, so the 1.0x figure assumes one ref per writer. Several sessions on one node (NT-20's unit holders) would share a fleet-tag ref and contend under compare-and-swap. | sound | - |
| 10 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1503 | medium | medium | confirmed | Line 1503 of v2 (dKeptSession) says: 'each message's id derived from its sender's act, its item, its kind and its subject, so a retried post is refused as a duplicate'. Night-pass-two:325 says the same. The handoffs prior-art return (:300) derives the id from (sender act, item, kind, subject). Coordination item 6 defines each message as carrying 'the id it answers', and its closed kind set includes `answer` and `ack`. Every transition is refused while a message addressed to the build is neither answered nor acknowledged. So one item that acks two distinct `changed` notices on one interface derives one id twice, and the second ack is refused. Item 7 says the owner may post by hand through the same verbs, and the owner has no act to derive from. The derivation is new in this diff. | sound | - |
| 11 | correctness | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:188 | medium | medium | confirmed | Systems.md:188-191 is new in this diff. It says the index's 'rows are keyed by blob, and a tree is a set of blobs', and that 'a deleted file rebuilds to identical rows'. I re-ran `git ls-tree -r e1a54ac67` and found 8 blobs at 24 paths. Path-derived rows (`path#symbol` addresses, `path:line` citations, the doc namespace) cannot be keyed by blob alone. The research's own probe schema (research-night2-instruments:1685, :2132) keyed nodes by file or path rather than by blob alone, so the fold overstates the measured design. | sound | - |
| 12 | correctness | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:36 | low | low | confirmed | Review-system.md line 166 is absent at base, so this diff added it. It says the harness keeps a five-slot literal 'so the hook counts slots'. Night-pass-two's point 7 table moves 'the verifier total, the loop markers and the lens count' to 'the merge bar's harness checks' (dFairHearing, dBoundRoles), and agent-cap.js retires, so the new line names a retired carrier. Night-pass-two:144 ('Caps above five wait on point 7') is a forward note that the record's own point 7 later settles, and it carries no pointer to that answer. Line 36 describes how the pass ran, and line 77 describes today's state, so both are milder. The impact is cosmetic or misleading prose only. | sound | - |
| 13 | correctness | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:442 | low | low | confirmed | Night-pass-two:442 says the lookup ran 'at the head of each of 47 closed reviews whose appendices carry a classes column'. Research-gotchas.md:55 says 66 review appendices have a classes column, 47 of them carry a 40-hex range, and 19 dClosedLoop design reviews are excluded. The record's phrasing presents 47 as the whole population with the column, and the 19 exclusions go unstated. The figures cited (6.2%, 82 of 1,317) are unaffected. | sound | - |
| 14 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1504 | low | - | refuted | Red on a stage whose cap exceeds the limit is the stated invariant, not an accident. Night-pass-two:126-127 says 'each cap at or under the repository's agent limit', and :141 says 'caps under the agent limit'. dBoundRoles patches role fields in the overlay, and workflow entries are data that a repository's own entries can override, so a lowered limit is met by an overlay rather than an edit to gov's files. Whether to clamp or to refuse re-argues the pending NT-8 recommendation. The finder graded this low, I could not establish a defect, and so it is refuted. | sound | - |
| 15 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1497 | low | - | refuted | This duplicates finding 16. Finding 16 cites the same dGroundRules witness at v2:1497, which plants an over-cap file only under `warn` and `refuse`, as part of the broader defect that `record` has no meaning or arm under `budgets.enforce`. The observation itself is true: v2:1112 lists 'warn, refuse, record', and the 1497 witness exercises only `warn` and `refuse`. | sound | - |
| 16 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1112 | medium | medium | confirmed | The catalogue row at v2:1112 lists `budgets.enforce` as 'warn, refuse, record', and night-pass-two:394 names `record` as one of 'the other values'. Every reader of the key in the diff is binary. v2:798 says a breach 'warns or refuses as `budgets.enforce` says', v2:1111 says 'whether a breach warns or refuses is `budgets.enforce`'s', and the 1497 witness plants the file under `warn` and `refuse` only. The base's `annotations.budget` row (base v2:1103) had 'refuse, warn, record', so `record` was carried over with no meaning defined under the new switch. The research (caps:98) prints and journals every breach even on a pass, so `record` is undistinguished from `warn`. | sound | policy-value-with-no-route |
| 17 | seams | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:160 | medium | medium | confirmed | Fates.md:160 still reads `agent-cap.js` ... STAYS \| spawn-guard pack; its arm becomes a fragment; slot reservation added (dWellOiledMachine). Night-pass-two:540 says `tools/hooks/agent-cap.js` 'retires in dBoundRoles once its last rule has moved', and its table moves each rule elsewhere. The diff touched fates.md for the gov-session row only (1 line changed), so it treats the record as live, yet left this row contradicting point 7. | sound | - |
| 18 | seams | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:103 | medium | medium | confirmed | Fates.md:103 still says `gotchas.py` classes are 'handed by write set through `gotchas.py --for-paths` (dFurnishedOrders)'. In this diff, v2's dFurnishedOrders row now renders classes 'from the classes the unit's spec names, never selected by its write set (SA-7, revised by the night pass two, point 6, pending NT-24)'. NT-25 keeps review's selection by range minus fully gated classes. The diff did not touch this fates row, so it states the selection the fold replaced. | sound | - |
| 19 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:426 | medium | medium | confirmed | systems.md:426 still reads 'The agent cap is bounded by agent-cap's `FANOUT_CAP`, never a new value.' The same diff revised the matching clause in v2's dBoundRoles row (:1504, 'an agent cap bounded by `runtime.agents-in-flight` (revised by the night pass two, point 7: it was agent-cap's `FANOUT_CAP`)'), v2:924 and layer-runtime:942, so this is a live design bullet the point-7 fold missed. The night pass two's point-7 [Folded] list does not name the systems record's registry bullet. Because the fold made it stale, it is in scope. | sound | - |
| 20 | seams | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:198 | low | low | confirmed | flow-roles-adoption.md:198 still lists "Shapes: the kinds, `FANOUT_CAP`'s bound and the five lens slots" as a fixed field. The diff revised the bullet two lines above it (:191-193), but this one still names the carrier that point 7 retired (v2:924, v2:1504). It is a live design list, not a dated snapshot. The effect is limited to wording, because v2 is the authority and names the new key. | sound | - |
| 21 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:461 | medium | medium | confirmed | layer-instruction.md:461-462 says 'The render refuses a set over budget'. layer-roles.md:76 says "R-C's render refuses a set over budget", and :380-381 says 'A block over its budget is refused'. The diff touched both files elsewhere and left these lines alone. Meanwhile v2:706 and :798 and systems:208 now say that a breach warns or refuses as `budgets.enforce` says, warning by default, and v2:1024 narrows `instructions.checks` to missing units. The owner directed warn as the default ([words], point 5). adopter-instructions:170 and :202 still say 'the render refuses', too. | sound | - |
| 22 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1509 | medium | medium | confirmed | In v2:1509 the dWellOiledMachine ledger claims a slot per agent at SubagentStart. It admits a spawn 'while the agents in flight and the reservations stay under `runtime.agents-in-flight`', and a Workflow call reserves its declared fan. layer-runtime:436-438 holds a Workflow reservation until 'the run's saved result'. Nothing draws the reservation down as that call's own agents claim slots, so a running fan-3 Workflow counts as 6. That is not the 'agents in flight' the key's row (v2:1002) defines. | sound | - |
| 23 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1002 | medium | medium | confirmed | v2:1002 defines the key as agents in flight in one session, 'its direct spawns and Workflow agents together'. dGroundRules (v2:1497) renders it only into the harness settings, 'for one session's direct spawns and one Workflow run'. The total ledger arms later, in dWellOiledMachine, and only after the spike. research-agent-cap.md:97 itself says the harness caps lose as the only enforcer ('The workflow cap applies per run, so two runs give 2N'). Neither the night pass two's 'Left open' nor the new gaps (gap-rt-34, gap-roles-30) record that interim shortfall. The fallback's split rule and its 'one live run per session' carrier are unnamed, too. The new key's stated meaning therefore has no enforcement path in that window, and no record says so. | sound | policy-value-with-no-route |
| 24 | seams | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:515 | medium | medium | confirmed | night-pass-two.md:514-515 says the harness settings, covering 'one session's direct spawns and one Workflow run', 'queue where agent-cap refused'. research-agent-cap.md:87 says `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` makes the Agent tool refuse with 'Do not retry' and is not enforced under ultracode. Only the Workflow setting queues (:88). The record misstates its return for the direct setting and omits the ultracode exemption. dGroundRules' witness (v2:1497) exercises only a Workflow run. The table row 'retired: the harness queues' concerns Workflow script rules and is correct for them, so the impact is narrower than the finder claims, but the misstatement is real. | sound | - |
| 25 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1066 | medium | - | refuted | v2:1066 offers `build.push` values, and under P10 they are owner options whose trade-offs are the choice itself. The default `every-item` is the recommendation (NT-19) and carries the witness at v2:1509. Under a non-default value, a successor deriving `next` from the pushed branch re-runs the units it cannot see witnessed. That is the safe, correct consequence of choosing less frequent pushes, not a wrong result. The closing review then receives the re-run units' rows, so it does not miss them. A per-value take-over arm is unit-level detail owed to dWellOiledMachine (by design). What remains asks for a different push semantics, which re-argues a pending fork. | sound | policy-value-with-no-route |
| 26 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1016 | low | - | refuted | v2:1016 defines `mailbox.notice` as 'when a session is shown unread message ids', with `mailbox.reads` an independent key (v2:1015) that allows `transitions-only`. Under `mailbox.reads = transitions-only`, `every-item` shows ids at each item while `off` shows none between reads, so the two values are distinguishable. They coincide only when reads is `every-item`. NT-17's shorthand wording does not make the catalogued values identical. | unsound | policy-value-with-no-route |
| 27 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1516 | medium | medium | confirmed | v2:1516 (dCalibratedLens) and night-pass-two:114-115 give the Loop Review a scenario-promotion proposal from 'a recorded change two or more builds carried', ratified by the owner. Nothing records a decline or suppresses a re-proposal. The tree already names this defect class, 'owner-item-without-its-reject-outcome' (expansions-reviews-compared:278, :436), and fixed it for `loop.propose`'s retire proposals with keep records (layer-expansions:259, :263). The new promotion proposal repeats the class. | sound | owner-item-without-its-reject-outcome |
| 28 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:232 | medium | medium | confirmed | I read flow-steps.md:232. In the new `build.reuse-check` row the Then cell reads 'clean -> the unit built; a `duplicate` or `bypassed` row -> a fix pass on the unit'. v2:1513 dScopedBuild says the same: 'a `duplicate` or `bypassed` row routing to a fix pass'. The acceptance bars are 29 and 31 of 35, so the design itself expects some wrong rows. Neither record gives the fix pass any outcome that disputes a row, any bound on re-entry, or any route to an owner or the closing review. Other rows in the same table do give such routes, for example `build.scope`'s warned/reported/refused. The defect is new in this diff and its effect is contained to one item's loop. | sound | route-names-an-output-its-actor-never-emits |
| 29 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md:100 | low | low | confirmed | coordination.md:100 keys the ref `refs/gov/mail/<slug>/<fleet tag>`, and :103 defines a sender as '(fleet tag, session, build)'. memory-plan.md:237 keys it `refs/gov/mail/<slug>/<sender>`. The night-pass-two record at :265 repeats `<fleet tag>`. The prior-art probe B' (research-storage-prior-art.md:29) and the measured return (:153) both measured one writer per ref, keyed by node or sender. So two sessions on one node do share one compare-and-swap chain, and two records name the key differently. Both are new text in this diff. The effect is only an inconsistency between records. | sound | - |
| 30 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1497 | high | medium | confirmed | v2:1002 says the key bounds 'agents in flight in one session, its direct spawns and Workflow agents together'. dGroundRules' clause (v2:1497) renders it 'into the harness's own concurrency settings for one session's direct spawns and one Workflow run' and is seen only on 'a Workflow run of four agents overlaps at most two under a limit of two'. No arm tests direct spawns. The combined total depends on the in-flight ledger, and night-pass-two:518-520 says that ledger is armed only after the spike; until then 'the limit splits into direct and Workflow budgets'. The catalogue row does not state that split. research-agent-cap.md says the direct-spawn setting is 'not enforced under ultracode' and that it is ambiguous whether workflow agents count toward the Agent-tool total, and grep finds 'ultracode' nowhere in v2 or the night-pass record. One correction to the finding: the check does not claim the combined bound, so 'certifies' overstates it. What remains is a design-text gap with contained effect, so medium rather than high. | unsound | rule-stated-with-no-check-that-fails |
| 31 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1497 | medium | medium | confirmed | v2:1497 says dGroundRules' `budgets.enforce` is 'the one switch every gate enforcing a size cap ... reads', with consumer limits and correctness checks 'left outside it'. Its only check is 'a planted over-cap file that warns under `warn` and refuses under `refuse`'. The caps research counts 24 caps, 18 of them refusing (research-caps.md:9; gap-tool-24). gap-found-34 records the correctness/size split as the defect. Yet neither dGroundRules nor dOrderedCharter's narrowed `instructions.checks` (v2:1499) plants a missing-required-unit case under `warn`, and no arm exercises `record`. Elsewhere this clause's checks are per-key censuses, for example 'a planted empty value for each such key the catalogue holds'. So a gate that keeps its own hard refusal, or a correctness check left wired to the switch, would pass. | sound | rule-stated-with-no-check-that-fails |
| 32 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:425 | medium | medium | confirmed | systems.md:426 (cited as 425) still reads 'The agent cap is bounded by agent-cap's `FANOUT_CAP`, never a new value'. v2:924 and v2:1504 now retire `FANOUT_CAP` into `runtime.agents-in-flight`. The diff revised many other lines of this record, including the Kinds bullet, but left this one. One correction to the finding: the Kinds bullet does not say 'at or under the repository's agent limit'. Even so, a live record still names the retired carrier, which is exactly the stale text the review asked about. | sound | - |
| 33 | verification | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:198 | medium | medium | confirmed | flow-roles-adoption.md:198 still lists 'Shapes: the kinds, `FANOUT_CAP`'s bound and the five lens slots' in the fixed set. The diff edited the same list at :191-193 for the splice but left this line. Point 7 retires `FANOUT_CAP` into `runtime.agents-in-flight`, so the fixed set names a carrier that no longer exists. | sound | amendment-leaves-its-other-half-standing |
| 34 | verification | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md:103 | medium | medium | confirmed | fates.md:103 still reads 'handed by write set through `gotchas.py --for-paths` (dFurnishedOrders)' and cites v2 dFurnishedOrders. The diff changed this file in one line only, the gov-session row. v2 dFurnishedOrders now says bug classes are rendered 'from the classes the unit's spec names, never selected by its write set (... point 6, pending NT-24)'. The two records now contradict each other. | sound | - |
| 35 | verification | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:457 | medium | medium | confirmed | night-pass-two.md:457-458 says 'the unattended per-pass checklist and the prebuild go with it'. Grep finds no 'prebuild' or 'per-pass' clause in v2 or flow-steps. The dFurnishedOrders revision changes only how the work-order field is selected. Worse, v2:1513 dScopedBuild still carries 'the checklist witnessed', closing gap-build-04 ('The per-pass bug-class checklist is unverified'). So the one build clause that mentions it still witnesses it rather than retiring it. No unit owns the retirement, its readers or a check. | sound | - |
| 36 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1509 | medium | medium | confirmed | v2:1509 dWellOiledMachine says '`gov-session` retired with an upgrade step: a hand-off ... becomes an `intake` message or a unit offered at placement'. It names no reader inventory and no check. Other retirements in v2 do: agent-cap at :1504 'its readers inventoried by value', /build at :1517, receipt schema at :1498. `git grep gov-session ad54fe388` lists AGENTS.md, tools/hooks/agent-cap.test.sh, tools/hooks/scratch-guard.test.sh, tools/roles/README.md, adopt-roles.test.sh, agents/gov-session.agent.md, check_roles.py, kit.toml and workflows.toml, as the finding says. | sound | retirement-inventory-misses-readers-by-value |
| 37 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:232 | medium | medium | confirmed | flow-steps.md:232 is new in f27b6e3b2. The `build.reuse-check` row lists added units "capped at sixty with an overflow line". Its proof is "every listed unit and every MUST has one row", and its outcome is "clean -> the unit built". Units past the cap are not listed, so the join never sees them, and no outcome treats an overflow line as anything but clean. The cap comes from aScoutedSeam's prompt principle (950e7c867: input lists "capped with an overflow line"). That principle bounds what is put in front of the agent. It says nothing about the step reading clean when coverage is partial. The night-pass-two record (line 191) folds the cap the same way. The effect is contained: the closing review still runs after this step, so this is medium. | sound | - |
| 38 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1507 | medium | - | refuted | The clause at architecture-v2.md:1507 is a design-level planned unit. The harness's by-design list says unit-level detail is absent and owed to the chain builds, and how a class's status gets set and checked is that kind of detail. No rule in BUILD-METHOD or REVIEW-PROTOCOL requires every design clause to name a red case, and many v2 clauses name none. The tree also already has a precedent the dLinkedLibrary spec would extend: gotchas.py check 18 (check_invariant) resolves an invariant record's `Guarded by` tokens against tracked paths or names in the leg manifest. So the gap the finding names is a missing spec detail, not a defect in the fold's text. It was graded medium and cannot be established as a design defect. | sound | rule-stated-with-no-check-that-fails |
| 39 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1516 | medium | - | refuted | The two dCalibratedLens clauses at architecture-v2.md:1516 state their behaviour: promotion from changes two or more builds carried, owner ratification, a move only at a step boundary and only if the build complies, and an owner item only for new or grown breaches. That is the design surface. Planted red cases are unit-level detail, which the by-design list leaves to the chain builds, and no protocol rule requires each design clause to carry a seen case. Many sibling clauses carry none. The finding shows no contradiction between these clauses and P9, NT-23 or the records. It only shows that tests are still owed, which is by design. | sound | rule-stated-with-no-check-that-fails |
| 40 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1503 | low | - | refuted | The dKeptSession clause at architecture-v2.md:1503 states the constraint outright: a scenario's preset slot is "never a key presets never touch". `runtime.agents-in-flight` is on the never-touch list at lines 1192-1198. So the design forbids the override the finding describes. Whether the unit spec adds a red arm for it is unit-level detail owed to the chain build. The finding names no contradiction in the text, only a check not yet written, which the by-design list covers. | sound | rule-stated-with-no-check-that-fails |
| 41 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1499 | low | - | refuted | The dOrderedCharter clause at architecture-v2.md:1499 is itself the owning clause: it states the property "rebuilt from nothing to identical rows" on the build that owns the index. The night-pass-two record at line 275 lists the rebuild-equality test under "Left open, each measured by the build that owns it". So the record discloses the owed test and assigns it to that build, and the finding's "no owning clause" is contradicted by the text. The specific planted-case test is unit-level detail, owed by design. | sound | rule-stated-with-no-check-that-fails |
