**Serves:** spec-audit TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5

# Spec audit round 1 — the five-unit spec set of dBriefedPass, before any code

*Node d, 2026-09-01, round 1, unattended prompt-mode run under a standing mandate. Finder lenses over the five specs, the build README and the driver they modify, then batched skeptics prompted to REFUTE each finding by re-deriving it against the source at the pinned blobs. Every citation below was re-checked against the tree by the author of this record before it was graded.*

**Reviewed subjects, each pinned at the blob it was read at:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md@671e2c0dd0ef` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md@648f59f7ca47` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md@a7bf661a1eaa` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md@9bf3e696add7` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md@f710f6c75a46`. **ROUND 1.**

## Verdict: BLOCKED

The count sits below this heading and never on it, because that line's token is a closed set and a tally appended to it turns a machine-comparable token into prose.

BLOCKED on five findings, and they are five of a kind rather than five unrelated defects. Three of them (B1, B2, B3) say the same thing at three addresses: **this set schedules work whose cost it never measured.** Unit 2 declares a verb whose three prose carriers unit 5 owns three orders later, so the bar reds at unit 2 and stays red until unit 5 lands. Unit 5 adds a sentence to a file with sixteen bytes of headroom, and asserts the budget holds afterwards under the words "Measured, not assumed". Unit 5's authoritative inventory omits the template half of a render pair a merge-bar leg byte-compares. None of the three is a style ask; each of them reds a leg on the way to its own Definition of Done.

The other two (B4, B5) are the more serious pair, because they are not oversights inside a document — they are **the spec set disagreeing with a binding record.** Unit 4 ships concurrent build-pass dispatch through a Workflow sidechain, which is precisely route R2 of `TOOL-cBriefedPilot-21`, whose ratified verdict is `parallelism route: none` and whose open re-opening row names the two experiments that were never run. Spec 4 cites none of it. And this build's own README carries an owner ruling from this run's one turn — "The harness calls `--review` and obeys its verdict" — which no unit in the set implements: spec 4 contains zero occurrences of `--review`, and its four stages run in a straight line with no re-entry.

Nothing here says the build is wrong. The two defects it targets are real, and the title-keyed fix in unit 1 is well chosen. What is wrong is the *set*: read as five documents that must agree, they do not agree on ordering, on the classifier's interface, on which unit owns the history leg, or on whether the harness converges.

## Review shape

- raw 63, confirmed 13, refuted 50, unverified 0, precision 0.21.
- confirmed by severity: **5 BLOCKER · 5 HIGH · 2 MEDIUM · 1 LOW**.
- confirmed blockers: 5.

Precision is measured over the whole raw population of 63 and not over a survivor subset. Nothing was demoted or merged away before grading, and the two multi-lens clusters below are reported as filed rather than collapsed, so this figure stays comparable with the earlier rounds in this corpus.

**0.21 is low, and the reason is worth recording rather than explaining away.** A pre-code spec audit has no executable subject: a lens can only assert that a document fails to say something, and "fails to say" is the easiest claim in the world to manufacture. Fifty of sixty-three findings were refuted, most of them by a skeptic pointing at a sentence the lens had not read. The thirteen that survived did so because each one joins a spec sentence to a *machine* — a gate leg, a byte count, an awk program, a printf format, a ratified decision id — and the machine is what refused to move. That is the shape a spec-audit finding has to have here, and it is the tuning note for round 2: prime the lenses to hunt joins to executable sources, not to hunt missing prose.

**Two adjudications in this record differ from the severity the verify stage returned, and both concern promotion.** B5 arrived as HIGH and is graded BLOCKER: an owner ruling recorded in this build's own README at this run's single turn, implemented by no unit, is the same class as B4 and not a lesser one — it is the rule that made leaving the convergence loop uncapped safe to accept. B3 arrived as BLOCKER and stays there, but on a narrower ground than it was filed under: its fix is nominally one inventory row, and it is a blocker because that row runs into B2's budget wall, not because a row is missing.

**The line between BLOCKER and HIGH in this record.** BLOCKER = the defect cannot be closed inside the unit as scoped — it needs a cross-unit reorder, a byte-budget decision, or an owner ruling — or the spec contradicts a binding recorded decision. HIGH = closeable inside one document, but as written the unit ships something that does not work or cannot fail. The line is stated because the mid-severity findings below are genuinely near it, and a later reader deserves to know which way it was drawn.

## Round 1 — no prior round

There is no round 0 to converge against, so the loop's exit condition is not yet in play. What round 2 owes is a strictly smaller blocker count and a DISPOSED verdict on every one of the five below. H1/H2 and the B2/B3 pair are each ONE fix surface reached twice, so a round 2 that closes them will see the count fall faster than the fix count.

---

# BLOCKERS — 5

## B1 (finding 1) — unit 2 declares a verb whose carriers unit 5 owns, three orders later

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md` §2 S1, and §7 Gates. Against `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 S3/S7.

Check 26 of `tools/unattended/check-unattended.sh` (`:2005-2058`) loops every id in `VERBS_SLUG` + `VERBS_INLINE` and joins each to **three** carriers: the driver's own `#   unattended.sh <verb> ` header line, `$SHIP` = `tools/unattended/PROTOCOL.template.md`, and `$tmpl` = `tools/unattended/SKILL.template.md`. Both files exist in the tree, so both `[ -f ]` guards are live and neither arm is skipped. `--brief` takes a slug, and `unattended.sh:91` makes `VERBS_SLUG` membership the dispatch itself, so unit 2 cannot ship the verb without joining that set.

Two of the three carriers are unit 5's edits at order 5. Spec 2 carries no §2 item and no §6 criterion for any carrier row. `unattended kit gate` in `tools/gate-legs.json` carries **no `guard` key** — verified by reading the manifest, guard `None`, ceiling 16040 — so it runs on every bar, guarded by nothing. The moment unit 2 adds `--brief` to `VERBS_SLUG` at `unattended.sh:86`, the bar goes red with three check-26 failures and stays red through units 3 and 4 until unit 5 lands. Spec 2's own §7 names `unattended kit gate` as a gate it must pass, which is unachievable at order 2 as specced, and every unit between them inherits a red bar it did not cause.

**Fix:** Add a §2 item to spec 2 requiring the header usage line plus the `PROTOCOL.template.md` and `SKILL.template.md` verb rows in the SAME unit — or state explicitly that units 2 and 5's verb rows land in one commit and move those rows out of spec 5 S3/S7. Then add a §6 criterion observing `bash tools/unattended/check-unattended.sh` green with `--brief` declared.

**Left-shift gate:** A hygiene check over spec §7 gate lists. For every gate name a spec's §7 backticks, resolve it against `tools/gate-legs.json`; if the leg is **unguarded** — meaning it runs on every bar and cannot be deferred — require at least one §6 criterion backticking that same leg name. A spec that names an always-on gate with no criterion observing it is carrying gate debt with no witness, which is exactly the shape here. Pair it with a `--verb-carriers <verb>` report mode on `check-unattended.sh` that prints the three carrier sites a proposed verb would need, so the ordering cost is visible while the spec is being written rather than at the first red bar.

## B2 (finding 16) — S5 and AC5 of unit 5 cannot both be satisfied; sixteen bytes of headroom

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 S5 against §6 AC5.

S5 adds one sentence to `memory/guides/BUILD-METHOD.md` M6, and AC5 requires the file to stay inside its declared 24 KB budget afterwards. Measured against the tracked blob: **`memory/guides/BUILD-METHOD.md` is 24560 bytes.** The file's own M1 declares "Budget: ≤24 KB, ≤350 lines" with "The BYTE half binds first". 24576 − 24560 = **16 bytes of headroom**, and the file is already over budget if the declared 24 KB is read as 24000 rather than 24576.

No sentence naming the harness fits in sixteen bytes. So the unit either lands over a stated constraint or drops the edit that is its whole point. AC5 says "Measured, not assumed" while never having measured the current headroom, so the criterion reads as verified when its premise is false — the criterion is the carrier that would suppress the next reader's check.

**Fix:** Add a §2 scope item declaring what M6 bytes are DELETED to pay for the sentence, or record an owner budget bump in §4 Migration with the new figure, then restate AC5 against that figure. Measure `memory/guides/BUILD-METHOD.md` **and** `tools/memory-tree/BUILD-METHOD.template.md` before writing the number — see B3, they are a pair and the template has five bytes.

**Left-shift gate:** Extend `tools/memory-tree/check-method-carriers.sh` with a **headroom assertion**: a file carrying a self-declared LOCAL byte budget must sit at least a declared margin under it, so the wall reds while there is still room to act rather than at the commit that crosses it. Two properties matter and neither is optional. First, the budget must be declared in resolved BYTES, not in an ambiguous "24 KB" that means 24000 to one reader and 24576 to another — that ambiguity is itself half of this finding. Second, the check must read the budget from the file that declares it and the size from the blob, never from a number typed into the checker, or the gate becomes the next thing to go stale.

## B3 (finding 17) — the inventory omits the template half of a byte-compared render pair

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §4 Inventory (the seven rows) and §7 Gates, against §2 S5/S6.

`memory/guides/BUILD-METHOD.md` is a RENDER of `tools/memory-tree/BUILD-METHOD.template.md` — rendered by `tools/memory-tree/adopt-memory-tree.sh:93`, byte-paired by `tools/memory-tree/kit-dogfood-parity.test.sh:53` as merge-bar leg `kit/dogfood doc parity`. That leg's guard list in `tools/gate-legs.json` includes both `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/`, so editing the render alone is guaranteed to wake the leg and red it.

Spec 5's inventory table lists BUILD-METHOD.md as a source graded by the method-carriers leg and names no template row; §4 declares the seven rows to be the complete list of files touched; and S6's "both rendered copies" names only the protocol and the skill. An implementer who follows the authoritative inventory edits the render alone and reds a leg no section of the spec mentions — §7's gate list also omits `kit/dogfood doc parity`, so nothing in the document would have caught it before the bar did.

This is graded a blocker rather than a missing row because the row runs straight into B2: the template blob is **24571 bytes**, so it carries the same budget wall with five bytes instead of sixteen. The fix is not "add a row", it is "make the budget decision, then add the row".

**Fix:** Add an eighth inventory row — `tools/memory-tree/BUILD-METHOD.template.md | the M6 sentence | kit/dogfood doc parity` — extend S6 to say the BUILD-METHOD render is regenerated too, and add `kit/dogfood doc parity` to §7. Resolve B2's budget on both files in the same edit.

**Left-shift gate:** A spec-layer check that derives render pairs LIVE and joins them to spec inventories. The adopters already name their pairs — `adopt-memory-tree.sh` renders `memory/guides/BUILD-METHOD.md` from `tools/memory-tree/BUILD-METHOD.template.md`, and the sibling kits do the same — so the pair set is enumerable from the adopt scripts with no committed second copy. The check: if a spec's §4 inventory names one half of a render pair, it must name the other half too. Derive the pairs from the adopters at check time, never from a list typed into the checker, and assert the derived pair set is non-empty so a broken derivation reds instead of passing over nothing.

## B4 (finding 49) — unit 4 ships route R2, whose ratified verdict is `parallelism route: none`

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md` §2 S4, and §4 "Alternatives rejected".

Concurrent build-pass dispatch was already hunted in this corpus and the recorded verdict is **`parallelism route: none`** — `TOOL-cBriefedPilot-21`, evidence at `memory/builds/cBriefedPilot/build/2026-08-15-build-TOOL-cBriefedPilot-15-2-parallelism-routes.md`, verdict token verified at line 5 of that record. The Workflow-sidechain route **R2 cleared E1 and E2 and FAILED the standard on E3 and E4.** The same record names **R5** — one git worktree per concurrent pass — as the checkout shape "any surviving dispatch route would need for E4", and E4 is *"each pass can commit at its own end without the two commits racing one index"*. `TOOL-cBriefedPilot-28` is still OPEN at `memory/backlog/TOOL.md:131`, naming exactly what would re-open it: "R2+R5 needs E3 and E4 RUN (they never were)".

S4 ships R2 without R5 — one `agent()` per unit through `boundedParallel`, into one worktree with one index — and cites none of this, not in S4, not in Alternatives rejected, not anywhere in the document. The index race is separately a recorded local gotcha in this repo (*shared primary tree, shared index*). And separately again: M6 requires the WRITE SETS of concurrent passes to be written down and recorded through `--dispatch`; S4 keys concurrency on the order value alone, which is not a write-set.

The severity is not about whether the race will fire. It is that the build ships a mechanism whose governing recorded verdict says no mechanism exists, so the spec set and the decision corpus disagree about a shipped capability.

**Fix:** Cite `TOOL-cBriefedPilot-21` and `TOOL-cBriefedPilot-28` in §4, then take one of two branches and record which. (a) Restrict S4 to strictly sequential dispatch until E3 and E4 are RUN, recording the cut in §3 the way the other cuts are recorded. (b) Put R5's per-pass worktree in scope and add two acceptance criteria that **OBSERVE** E3 and E4 rather than argue them.

**Left-shift gate:** A spec-audit leg over the decision corpus using the shipped offline retrieval CLI. For each spec, query `python tools/memory-recall/query.py` with the spec's H1 and §2 scope terms; if the result set contains a RATIFIED decision whose id appears nowhere in the spec, red with that id named. This is the "prior art these specs missed" class made mechanical, and the corpus is already indexed for it. Two cautions to build in: the leg needs a precision threshold or it becomes noise a reader learns to ignore, and it must red loudly when the index is missing or empty rather than reporting a clean zero — a retrieval check with no liveness assertion is the reassuring-zero shape this repo refuses elsewhere.

## B5 (finding 55) — the owner-ruled review loop is implemented by no unit

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md` §2 S2, and §4 "Rollout". Against `memory/builds/dBriefedPass/README.md` § Build-level rules.

*Filed HIGH by the verify stage. Adjudicated BLOCKER here.*

S2 declares "four stages in fixed order: SPEC, AUDIT, FOLD, BUILD" with "A unit reaches BUILD only by having passed through the three before it in the same program run", and no loop anywhere. S3's AUDIT delegates to `tier2-review.js` once. S6's re-entry sub-flow is for units added mid-build, not for review rounds.

Grepped across the set: **spec 4 contains zero occurrences of `--review` and zero of `converg`.** Specs 1, 3 and 5 carry no `--review` either; the single hit anywhere in the set is spec 2's park-kinds table. Meanwhile this build's README states, verbatim, as an owner ruling dated 2026-09-01 at this run's one turn: *"Convergence stays; no review-round cap. … The harness calls `--review` and obeys its verdict."*

The shipped `review_state` reports four states — CONVERGED, NON-CONVERGENT, CEILING, CONVERGING — and BUILD-METHOD M4 bounds the audit by convergence with a runaway backstop, requiring a BLOCKED round to re-arm on a strictly smaller blocker count and every surviving blocker to be DISPOSED at the exit. A strictly linear SPEC→AUDIT→FOLD→BUILD run performs exactly one review round and then builds, which is the shape M4 forbids.

This is graded a blocker on the same ground as B4 and not a lesser one. The owner declined a review-round cap **because** the harness would obey the convergence verdict; that ruling is the safety argument for leaving the loop uncapped, and the unit that owns the stage contract does not implement it. Under M2's sub-spec agreement rule this is a defect in exactly one document, and the document is spec 4.

**Fix:** S2 gains the AUDIT→FOLD→AUDIT loop keyed on the `--review` verdict token, with the stage list restated as three sequential stages plus a converging pair. Add acceptance criteria asserting that a CONVERGING verdict re-enters AUDIT, and that NON-CONVERGENT and CEILING both exit to BUILD with the promotion M4 requires.

**Left-shift gate:** A hygiene check joining a build README's `## Build-level rules` bullets to the spec set. Every rule bullet must name the unit id that implements it, and that unit's spec must contain the rule's key token — here, `--review`. An owner ruling recorded in the master record and implemented by no unit is a silent authorization gap, and it is cheap to catch because both documents are already parsed by `gen_build_index.py`. Make the token join explicit in the bullet rather than inferred, so the check grades a declared claim instead of guessing at prose.

---

# HIGH — 5

## H1 (finding 36) — `plan_state`'s refusal has no channel, and the DoD call site discards it

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md` §2 S3 and §4 (no refusal contract).

S3 makes a duplicate title a REFUSAL, but `plan_state`'s contract is one bare token on stdout, and the driver records at `unattended.sh:3237` that widening that output was **deliberately declined** because two harnesses slice the function body: "the caller receives one bare token … The grade is a single token by design." §4 never says what the refusal emits.

A refusal token falls through `verb_plan`'s `case "$state" in THIN|FORKED) … READY)` at `:2074` with no branch, and `build-complete`'s term is the bare `[ "$(plan_state "$_bcsp")" = THIN ]` at `:3271`, which discards the exit status entirely. So a duplicate-title spec is silently NOT THIN, and a CLOSED unit built against it passes the Definition of Done. The new guard would be invisible at the one place the grade decides a landing. §4's files-touched estimate is "the `plan_state` awk program" plus the test — the call sites are excluded from scope.

**Fix:** Add a §4 sub-heading stating the refusal channel: `plan_state` prints nothing on stdout, writes the message to stderr naming file and title, and exits non-zero; and BOTH call sites must treat a non-zero exit as a hard failure — `verb_plan` reports it in the row, `build-complete` returns 1. Add a criterion observing the build-complete arm, not only the message.

**Left-shift gate:** An arms check over single-token classifiers. For a function whose contract is one printed token, assert that the set of tokens it can emit equals the set of branches enumerated at every call site — the union of `case` patterns and string comparisons. A token with no branch is an unhandled outcome by construction. `tools/memory-tree/check-arms.py` is the right shape to extend. Stage the break and confirm the check goes RED on a token with no branch before wiring it, because a predicate over a small enum is exactly the kind that quietly matches nothing.

## H2 (finding 22) — the same defect, seen from the non-goal it contradicts

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md` §2 S3 against §3 non-goal 4, and against `2026-09-01-spec-TOOL-dBriefedPass-3.md` §2 S1 / §4 step 3.

*One defect with H1, reached by a second lens. Reported as filed; one fix closes both.*

S3 introduces a third `plan_state` outcome beside the state tokens, while §3 asserts that `--close`'s THIN term "does not change which specs the term grades". The refusal is not gated by `SPEC_THIN_CUTOFF` and reaches the comparison at `:3271` regardless, so the non-goal is false either way the refusal is implemented: a hard abort changes the graded population `--plan` and `--close` walk, and a printed non-THIN token is swallowed by the string equality and grades clean.

Spec 3 inherits it. Its two consumers — S1's dispatch refusal and §4 step 3's predicate — enumerate only MISSING and THIN, so a duplicate-title spec passes the history join as well.

**Fix:** State the refusal's mechanism in spec 1 §2 and its behaviour at each of the two existing call sites, then add a matching clause to spec 3 S1 and §4 step 3 saying a refusal is treated as a failure to grade rather than as a pass. Correct or delete §3 non-goal 4, which is not true under either implementation.

**Left-shift gate:** The emit side is covered by H1's arms check. The consumer half wants its own leg: a check that a §3 non-goal asserting "X does not change Y" names the predicate that would detect a change to Y. A non-goal with no observable is an assertion about nothing, and it is the cheapest false-confidence carrier a spec has.

## H3 (finding 37) — the declared BRIEF row cannot be produced by the writer the unit joins

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md` §4 Data model (the `- brief · …` row) against §2 S1/S4/S5.

`park()` at `unattended.sh:3710` writes `printf '\n%s %s · item %s%s · reason %s\n'` — a leading ISO-Z timestamp, then kind, then `· item <item>`, an optional `· step N`, then `· reason <reason>`. Every reader greps that timestamped grammar: the `kinds_re` counters at `:2713` and `:3553` match `^[0-9][0-9-]*T[0-9:]*Z (…) · item `, and `recorded_waivers` takes the token between ` · item ` and ` · reason `. §4's dash-led four-field row has no `item`, no `reason` and no timestamp.

S4 puts `brief` in `PARK_KINDS`, and check 27 of `check-unattended.sh` (`:2077-2090`) fails in both directions, including "the driver declares a parked kind that no `park()` call site ever writes". So the unit as specified reds the same unguarded kit gate as B1, while S5's `--status` split — derived from `PARK_KINDS` minus the owed set, which is precisely the alternation those counters walk — counts a row its regex cannot match.

**Fix:** Replace the §4 row with the park grammar and state the field mapping — `park "$rel" brief "<unit-id>" "<sha256-12> <repo-relative path>"`. If a bespoke row shape is genuinely wanted, drop S4's `PARK_KINDS` membership and name the reader that parses the new shape. Add a criterion asserting check 27 stays green.

**Left-shift gate:** A check that any §4 Data model row describing a run-state line is matched against the `park()` printf format **derived live from the driver**, not against a copy. The format string is one grep away and the field names are in it, so the join is mechanical: a declared row missing a mandatory field reds at spec time instead of at the first bar. Same rule as B3's — derive the format, never restate it.

## H4 (finding 38) — AC6 asserts a stale message that nothing in scope emits

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md` §2 S3 and §6 AC6, with no reader named in §4.

S3 claims an edited brief "reports as stale, the same join `--record-piece` uses". That staleness is computed by a different program over a different artifact. `record_piece` (`unattended.sh:4044`) writes a separate record FILE under a records root with a `hash:` field; the stale VERDICT is produced by `check-playbook.sh`, which prints `stale=` at `:615` by comparing that record file against the piece's current hash, and the driver only parses the enumerator's counts (`_sc=${_counts#*stale=}` at `:3039`).

**Nothing anywhere recomputes a hash recorded in a run-state parked row**, and S1–S7 add no reader. S5 gives `--status` a count, not a staleness check, and AC1's idempotence means a re-run over an edited file writes a second line rather than reporting stale. So AC6 cannot be met by anything this unit builds: the recorded hash is decoration, and the record's central advertised property — readable as stale — is untrue on landing day.

**Fix:** Name the reader in §4. Either `--status` recomputes each brief row's hash and prints STALE beside it, or a `build-complete` term refuses a stale brief. Then restate AC6 against that command by name.

**Left-shift gate:** Extend the acceptance-witness rule: a §6 criterion asserting that some output is EMITTED must backtick the command that emits it, and that command must appear in the unit's §2 or §4. A criterion asserting a message with no producer in scope is a could-not-fail criterion, and at review time it is indistinguishable from a satisfied one — which is how this one reached a confirmed finding rather than a builder's error.

## H5 (finding 40) — spec 3 requires a message spec 1's classifier cannot produce

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §2 S1 and AC2.

S1 requires the dispatch refusal to name "the section that is empty". `plan_state` (`unattended.sh:1649-1712`) has no per-section output: its map is built and consumed inside its own awk END block, and the driver states the constraint as a DESIGN decision at `:3231-3237` — "The message names the UNIT and NOT the empty section … widening that output would ripple into two harnesses that SLICE the function body. The grade is a single token by design."

Spec 1, the unit that owns the classifier, adds no such output, lists no such scope item, and commits in S5 to both slicing harnesses continuing to pass. So AC2 is unmeetable within either unit's declared scope without an unpriced widening of an interface the source pins deliberately, or a second predicate over the same question. Neither spec names which, and no section prices the ripple the source warns about. Two units of one build disagree about the classifier's interface.

**Fix:** Weaken S1 and AC2 to name the unit and the STATE only — the wording `build-complete` already uses and defends — or add an explicit scope item to spec 1 exposing the section map on a second channel, with the slicing harnesses' contract restated there and the ripple priced.

**Left-shift gate:** A cross-spec ownership check. If spec X carries a criterion asserting behaviour of a file that appears in spec Y's §4 inventory, spec Y must carry a §2 scope item covering that behaviour. The inventories are already structured tables and the ids are already family-qualified, so the join needs no new authoring. This is the generic form of the defect B1 and H5 both instantiate: one unit spending another unit's scope.

---

# MEDIUM — 2

## M1 (finding 26) — the README roster and spec 5 disagree about which unit ships the history leg

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 (whole) and §3 non-goal 4, against `memory/builds/dBriefedPass/README.md` generated units region, row 5.

The README's roster row 5 describes unit 5 as "the carriers declare the harness the route, **and the gate leg reads history**". Spec 5's H1 reads "…and the brief the obligation", its §3 puts a machine check out of scope, and it assigns `PASS_ORDER_CUTOFF` and the history leg to `TOOL-dBriefedPass-3` — where spec 3's S3/S4/S6 do own them.

The roster is M2's detect source and the master overview, so the main record claims unit 5 ships a mechanism its own spec explicitly declines. A reader picking the build up after a compaction gets two answers to one question, and M2 says a disagreement between the overview and a sub-spec is a defect in exactly one document.

**Fix:** Rewrite the units-region mechanism cell for unit 5 to match spec 5's H1. If the roster is the correct one instead, move the leg into spec 5's scope and delete spec 3's S3/S4/S6. Name the corrected document in the losing side's §9 revision line either way.

**Left-shift gate:** Assert in `gen_build_index.py` that each unit's roster mechanism cell and its spec H1 agree on the unit's owned mechanism tokens — or, better, derive the mechanism cell FROM the spec H1 so the authored copy stops existing. The second is the stronger fix and it is available here, because this is a generated region already, and one fact in one place beats two facts a checker reconciles.

## M2 (finding 61) — BUILD-METHOD M2 states the grading in the ordinals unit 1 abandons

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md` §3 non-goals, and `2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 S5.

`memory/guides/BUILD-METHOD.md` M2 states the classification in ORDINALS — line 44: "**THIN** — §2 Scope, §6 Acceptance or §7 Gates is empty, a placeholder, or names nothing observable"; line 45: "**FORKED** — §8 Open questions carries an unresolved item." That is exactly the keying unit 1 abandons. Unit 5's carrier edit touches M6 only ("M6 gains ONE sentence … and nothing else"), and unit 1's non-goals name `check-memory-hygiene.sh`, the spec canon, the corpus and `SPEC_THIN_CUTOFF` — never M2.

The consequence is sharper than a stale doc. **Today the method and the classifier agree**: both are ordinal-keyed and both are wrong for Tier-1 in the same way, so a run following M2 and the machine reach the same answer. After this build they disagree on precisely the Tier-1-shaped specs — and `TOOL-dBriefedPass-3` turns the machine's half into a hard `--dispatch` refusal. Two answers to one question, with the binding procedure holding the losing one, in a build that ships a dedicated carrier unit already editing that file and not carrying it.

**Fix:** Add M2's THIN/FORKED sentences to unit 5's carrier inventory as one row graded by the method-carriers leg, restating them as section TITLES; or scope the M2 edit into unit 1 and say so in its non-goals. Note that this lands on the same file as B2 and B3 and must be paid for out of the same byte budget.

**Left-shift gate:** `check-method-carriers.sh` gains an assertion that M2's classification sentence names the same keys the classifier actually uses, derived from `plan_state`'s own awk program rather than from a list in the checker. This is the exact "value stated in prose beside the source that owns it" class the charter names, and it is gateable here because both halves are machine-readable.

---

# LOW — 1

## L1 (finding 29) — AC1 runs a JavaScript file through bash

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md` §6 AC1 against §2 S7.

AC1 invokes the syntax checker as `bash tools/workflows/check-workflow-syntax.js`. `tools/workflows/kit.toml:59` declares it as `argv = ["node", "{kit}/check-workflow-syntax.js"]`, the file opens `#!/usr/bin/env node`, its own usage line says `node …`, and the `gate-legs.json` row is `["node", …]`. Ran both against a real target: `bash …` exits 2, `node …` exits 0. AC1 as written — "accepts the file" — cannot pass.

Graded LOW rather than higher on one specific ground, and the finding as filed overstated this half: it fails **loudly**, at exit 2, so it is a visible error rather than a check that cannot fail. It is still a verified error in the one criterion that proves S7.

**Fix:** Rewrite AC1 as `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-build.js`, matching the declared argv.

**Left-shift gate:** A check that every backticked command in a §6 criterion has its interpreter matching `argv[0]` of the owning `kit.toml` declaration. The kit descriptors are a declared population already — that is what makes this derivable — so the join needs no new authoring, and it catches the whole class rather than this instance.

---

## Left-shift summary

Eleven distinct gates are proposed above, and the useful thing about them is how few mechanisms they actually are.

**B3, H3, M2 and L1 all reduce to one rule: a spec may not restate a value the tree already owns** — a render pair, a printf format, a classifier's keys, an interpreter. It must join to the source and let the join red. **B1 and H4 reduce to a second: a criterion naming a gate or a message must name what produces it.** **B4 and B5 reduce to a third: a claim contradicting a ratified decision or an owner ruling should red before it is built, not after.**

If only one is built, build the second. Six of the thirteen findings here are criteria asserting something with no producer in scope, and every one of them would have read as satisfied on landing day.

## What this round did not check

This is a pre-code audit. It grades the five documents and their joins to the tree at the pinned blobs; it does not grade any implementation, because none exists. Three consequences worth stating so a green round 2 is not misread.

Nothing here asserts the specs' *goals* are wrong — both targeted defects are real, and unit 1's title-keyed fix is well chosen.

Nothing here exercises the harness, `plan_state`, or the proposed gate leg. Every claim about their runtime behaviour is read from source, plus the two commands actually run for L1.

The refuted 50 are refuted as *findings*, not certified as *correct*. A lens that failed to make its case leaves the underlying question open, not answered.
