**Serves:** spec-audit TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5

# Spec audit round 2 — the five-unit spec set of dBriefedPass at rev-2, after the round-1 fold

*Node d, 2026-09-01, round 2, unattended prompt-mode run under a standing mandate. Finder lenses primed on the FOLD — every rev-2 edit, the new scope items, the reworded non-goals, the new acceptance criteria and the §9 revision logs — then batched skeptics prompted to REFUTE each finding by re-deriving it against the source at the pinned blobs. Round 1's tuning note was applied as the priming rule: a finding survives here only when it joins a spec sentence to a machine, so the lenses hunted joins to executable sources rather than missing prose. Every citation below was re-checked against the tree by the author of this record before it was graded.*

**Reviewed subjects, each pinned at the blob it was read at:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md@a73a9483eff6` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md@8278791c9ef7` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md@e455b75d33ae` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md@7eb81f4e3fc3` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md@986f74c7bf28`. **ROUND 2.**

## Verdict: BLOCKED

The count sits below this heading and never on it. The token above is drawn from a closed set of three, and a tally or a qualifier appended to it turns a machine-comparable token into prose.

BLOCKED on two findings, down from five. **The loop re-arms under BUILD-METHOD M4: the blocker count is strictly smaller, and all five of round 1's blockers are DISPOSED — none of them is re-raised below.** That is the good news and it is real.

The bad news is the shape of the two survivors. **Neither B1 nor B2 is a round-1 blocker, and neither was created by the fold.** Both are pre-existing defects in spec 3 that round 1 walked past — verified by diffing `c5ceb93e..24ddc653`, which shows the fold touched only spec 3's S1, §4 step 3, AC2 and §9, leaving S3, S4, S5, S6, §5 and §7 exactly as round 1 read them. Round 1 spent its budget on the cross-spec ordering axis and on unit 4's decision-corpus conflicts, and it did not audit unit 3's own gate story at all. So the blocker count fell because five defects were fixed, not because the set got two rounds of scrutiny.

The two blockers say one thing between them: **unit 3's product is a merge-bar refusal, and unit 3 has no working account of how it reaches the merge bar.** B1 is a conf key whose protocol carrier no unit owns, which reds an unguarded leg from unit 3 through landing. B2 is three of unit 3's own items — S3, S6 and §5 — that cannot all be satisfied, because the check is put inside a script whose only gate row is the leg §5 forbids widening, and §3's own non-goal closes the escape. H3 completes the picture: even if both are resolved, no criterion in §6 observes the manifest row, so the leg could ship registered nowhere and green.

**Thirteen of the twenty confirmed findings were caused by the fold**, which is 65% and sits squarely on the 42-of-62 (68%) figure this corpus records for the same phenomenon. The fold was correct to attempt every fix it attempted; what it did not do is re-read the sections its own edits invalidated. Five of the thirteen are one sentence in one document going stale because a neighbouring sentence moved — spec 5's inventory row, spec 1's observability bullet, spec 5's S7. That is a cheap class to close and it is the whole difference between round 3 being short and round 3 being another 41 findings.

## Review shape

- raw 41, confirmed 20, refuted 21, unverified 0, precision 0.49.
- confirmed by severity: **2 BLOCKER · 10 HIGH · 7 MEDIUM · 1 LOW**.
- confirmed blockers: 2.
- confirmed findings caused by the round-1 fold: 13 of 20. Pre-existing and missed by round 1: 7.

Precision is measured over the whole raw population of 41 and not over a survivor subset. Nothing was demoted or merged away before grading, and the three multi-lens clusters below are reported as filed rather than collapsed, so this figure stays comparable with round 1 and with the earlier rounds in this corpus.

**Precision rose from 0.21 to 0.49, and the tuning note is why.** Round 1 recorded that fifty of its sixty-three findings were refuted, most by a skeptic pointing at a sentence the lens had not read, and prescribed the fix: prime for joins to executable sources rather than for missing prose. That priming was applied here, and the raw population fell from 63 to 41 while the confirmed count rose from 13 to 20. The finding rate per raw filing more than doubled. This is worth recording as a reusable result: **on a pre-code spec audit, priming the lens for the JOIN rather than for the gap is worth roughly 2x precision**, and it costs nothing but the prompt.

**Three clusters, reported as filed.** H7/H8/H9 (findings 36, 31, 13) are one defect — spec 5's S7 against spec 2's S8 — reached from the ordering, scope and ownership axes; M4 (finding 10) is the same defect reached from the criterion axis, and is graded a medium because it is the axis on which the fix is smallest. H1/H2 (findings 14, 6) are one defect in spec 4 reached from the interface and data-model axes. M5/M6/M7 (findings 19, 40, 9) are one stale table cell in spec 5's inventory. **Four fix surfaces close eight of the twenty.**

**The line between BLOCKER and HIGH in this record is round 1's, unchanged.** BLOCKER = the defect cannot be closed inside the unit as scoped; it needs a cross-unit scope addition, a budget decision, or an owner ruling. HIGH = closeable inside one document, but as written the unit ships something that does not work or cannot fail. The line is restated because two findings below sit close to it and a later reader deserves to know which way it was drawn.

**No promotions and no demotions in this record.** Round 1 made two promotions and documented them; round 2 makes none, and the one that was seriously considered is stated here rather than left silent. **H1/H2 are the descendants of round 1's B5**, the owner-ruled review loop that no unit implemented. The fold implemented it — S2b now carries the convergence loop and the four verdict tokens are correct — but keyed it on "the caller-supplied review callback", a channel that neither S1 nor §4's args table declares and that the Workflow boundary cannot carry, since `tier2-review.js:48` records that `args` arrives as a STRING. So the owner ruling still has no implementation that can run. It is graded HIGH rather than BLOCKER because the fix is entirely inside one document and both findings name it: make the AUDIT stage's return the verdict channel. **The escalation rule is explicit — if round 3 leaves H1/H2 open, they re-inherit B5's blocker grade**, because at that point an owner ruling recorded at this run's single turn has survived two folds unimplemented, and the safety argument for leaving the review loop uncapped will have failed twice.

## Round 1 → round 2: what the fold disposed of, and what it created

All five round-1 blockers are DISPOSED. None is re-raised.

- **B1** (unit 2 declares a verb whose carriers unit 5 owns) — disposed by spec 2's new S8, which moves all three check-26 carriers to order 2. The move is correct. It left four residues: H5, H7, H8, H9, plus M4 and M5/M6/M7, because spec 5's S7 and its inventory table were not re-read after the rows left them.
- **B2** (BUILD-METHOD's sixteen bytes of headroom) — disposed. Not re-raised, and the byte figures are quoted in H4 only as the measurement AC6 rests on.
- **B3** (the inventory omits the template half of a byte-compared render pair) — disposed for BUILD-METHOD. The same shape was then re-created one document over, at spec 2, by B1's own fix: see H5.
- **B4** (unit 4 ships route R2 against a ratified `parallelism route: none`) — disposed. Not re-raised.
- **B5** (the owner-ruled review loop implemented by no unit) — implemented, on a channel that cannot exist: H1 and H2.

What the fold created, stated as a rule rather than a list. **Every one of the thirteen fold-caused findings is a sentence that was true before a neighbouring sentence moved, and false after.** Spec 5's S3 was rewritten to decline the `--brief` rows and its §4 inventory cell still says "two verbs". Spec 1's S3 was rewritten to bind the first occurrence and its §5 observability bullet still describes the refusal that was removed. Spec 5's S7 was reworded from `--brief` to "the verbs this build adds" in the same commit that moved that exact row into spec 2's S8. Spec 2 gained S8 and neither §4's file list nor §7's gate list gained the four files and one leg S8 now touches. Not one of these is a judgement call; each is a plain contradiction inside a single document, discoverable by re-reading the sections adjacent to every edit.

---

# BLOCKERS — 2

## B1 (finding 35) — a conf key with no protocol carrier, reddening every bar from unit 3 to landing

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §2 S4 and §4 Files touched. Against `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §3.

Check 22 of `tools/unattended/check-unattended.sh` (`:1281-1317`) joins conf keys in **both directions**. It derives `doc_keys` from the first table column of section 8 of `memory/guides/UNATTENDED-PROTOCOL.md`, and `ex_keys` from `^[A-Z_]+=` in `.unattended.conf.example`; it fails on `undocumented` (example minus doc) and separately on `proj_extra` (the repo-root `.unattended.conf` minus doc). Measured now, the two sets are identical at **28 keys**.

Spec 3 S4 declares `PASS_ORDER_CUTOFF` into both `.unattended.conf` and `tools/unattended/.unattended.conf.example`, its §4 Files touched names no protocol file, and its Migration seeds the key to a real date. So **both failure directions fire at once**. The leg that carries check 22 is `unattended kit gate`, and its row in `tools/gate-legs.json` has **no `guard` key** — verified, guard `None`, ceiling 16040 — so it runs on every bar. The red arrives when unit 3 lands and persists through units 4 and 5 to landing.

No unit owns the fix. Spec 5 is the unit that owns every protocol carrier in this build, and its §3 declines this key explicitly: *"No new conf key is added by this unit. `PASS_ORDER_CUTOFF` belongs to `TOOL-dBriefedPass-3`, and so does the history-reading gate leg."* The fold strengthened that sentence; it did not create the hole. `TOOL-cSettledDocket-14` is OPEN at `memory/backlog/TOOL.md:140` and already states the governing rule — every key the engine reads appears in the protocol's key table and the shipped conf example — and it is not on this review's known-open exclusion list.

This is graded a blocker on round 1's own line and for round 1's own reason: it is B1's class one axis over, it cannot be closed inside unit 3 as scoped because unit 3's file list contains no protocol carrier and unit 5 has refused it in writing, and resolving it is a cross-unit scope decision rather than a document edit.

**Fix:** Add an S-item to spec 3 naming `tools/unattended/PROTOCOL.template.md` section 8 and the regenerated `memory/guides/UNATTENDED-PROTOCOL.md` as carriers this unit edits **in the same commit as the conf key** — check 22 reads the RENDER for `doc_keys` and check 10 byte-diffs the pair, so both halves must move. Extend §4 Files touched with both. Add an acceptance criterion asserting `bash tools/unattended/check-unattended.sh` green with the key declared, which is the mirror of spec 2's AC7. Then delete the sentence in spec 5 §3 that declines it, so the two documents agree.

**Left-shift gate:** Generalize B1's proposed carrier check from verbs to **every declared population the kit joins across files**. `check-unattended.sh` already knows three of them — verbs (check 26), conf keys (check 22), park kinds (check 27) — and each is a set derived from one source and asserted against N carriers. Add a `--carriers <kind> <member>` report mode that prints, for a proposed member, every carrier site it would need and which check joins each. Then add a spec-layer leg: if a spec's §2 declares a new member of any of those populations, its §4 Files touched must name every carrier that member's own check will demand. Derive the carrier list from the checker at check time, never from a list typed into the spec gate, and assert the derived list is non-empty so a broken derivation reds rather than passing over nothing.

## B2 (finding 24) — unit 3's S3, S6 and §5 are jointly unsatisfiable

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §2 S3 and S6, with §5 Performance and §3's non-goal.

S3 puts the new history check **inside** `tools/unattended/check-unattended.sh`. S6 and §5 require it to ship as **its own gate leg with its own ceiling**. That script's argv contract admits no such thing.

`check-unattended.sh:85-90` accepts exactly `""`, `--only 28` and `--skip 28`, and exits 2 on anything else with the message *"checks 1-27 share state and are one unit"*. Nothing in the tree invokes either selector. The only `gate-legs.json` row pointing at that script is `unattended kit gate`, argv `["bash","tools/unattended/check-unattended.sh"]`, ceiling 16040, no guard. So a check added to that file runs **inside** the leg §5 says it must not widen — and §5 justifies its shape on a live cost record, `TOOL-aCollapsedScan-4`, still OPEN with `unattended kit gate` roughly 44 s over `BUDGET_kit_gate=120`. A second manifest row pointing at the same script would re-run all 28 checks and grade the whole leg against the new ceiling.

The obvious escape — scope the existing row with a selector — is closed by the unit's own §3 non-goal: *"No existing gate leg is scoped, relaxed or exempted to make room for this one."* And §4 Files touched names no new script, so nothing inside the unit resolves it.

Graded a blocker because the three items are jointly unsatisfiable as written and the resolution is a scope-and-budget decision, not a wording fix. Pre-existing: the fold did not touch S3, S6, §3 or §5.

**Fix:** Pick one branch and say which in §4.

(a) Put the history join in a NEW script — `tools/unattended/check-pass-order.sh` is the obvious name — add it to §4 Files touched, and keep S6's own leg row and its own ceiling. This is the branch §5's reasoning actually wants.

(b) Keep the check in `check-unattended.sh`, drop S6's separate-leg claim, and price the addition against `BUDGET_kit_gate=120` in §5 with an acceptance criterion that MEASURES the leg's new wall time rather than asserting it. This branch needs an owner ruling on a leg already over budget, so say so in §3 rather than absorbing it silently.

**Left-shift gate:** A spec-layer consistency check over §2 items that name a gate mechanism. When a spec item says a check ships as its own leg, resolve the script it names against `tools/gate-legs.json`: if that script already appears in a row, the spec must either name a new file in §4 Files touched or declare the existing row as its host and restate its ceiling. This is mechanical because both halves are declared — the spec's file list and the manifest's argv — and it catches the general class: **a spec that specifies a delivery vehicle its own file list cannot build.** Pair it with a ceiling assertion, so a unit adding work to a leg already over its declared budget reds while the spec is being written rather than at the first timing run.

---

# HIGH — 10

## H1 (finding 14) — the convergence loop keys on a channel the invocation contract does not carry

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md` §2 S2b and §6 AC7, against §2 S1 and §4 Data model.

*This is round 1's B5, implemented. Read the promotion note in the Review shape section before grading it lightly.*

S2b and AC7 key the entire convergence loop on **"the caller-supplied review callback"**. S1 enumerates a five-field args object — `repo`, `slug`, `base`, `units`, `briefDir` — and §4's args table, whose own title is *"why the harness cannot derive it"* and which is therefore the authoritative interface, carries the same five and no callback. S1's guard validates only `repo`.

The channel cannot exist. `tier2-review.js:48` records in its own comment that the Workflow tool delivers `args` as a **STRING** even when the caller hands it JSON, which the script then JSON-parses — so a function cannot ride the object it would have to arrive in. §3 separately states the script has no filesystem, so it cannot call `--review` itself either. The four verdict tokens are real and correctly quoted: `unattended.sh:3768-3771` prints CONVERGED, NON-CONVERGENT, CEILING and CONVERGING. They are produced by a shell verb the sidechain cannot run, and S5 names only "a schema-validated object" with no verdict field in it.

So AC7's four arms have nothing to inject, and the fold's central new mechanism is keyed on a token no section of the spec supplies.

**Fix:** Declare the channel, and prefer the form that adds no field. The AUDIT stage's own `workflow()` call already returns `{confirmed, blockers, highs, …}` — `tier2-review.js:383` — so name the AUDIT agent as the actor that runs `--review <subject> <blockers>` and returns its verdict token, add that field to S5's schema, and restate S2b and AC7 against that return value instead of a callback. Add an arm to AC2 refusing a run whose audit stage returns no verdict token, so a silent absence cannot read as CONVERGED.

**Left-shift gate:** A harness-contract check that joins a spec's §6 criteria to its own §4 interface table. Every identifier a criterion names as an INPUT must appear in the declared args table or in a declared stage return. This is the "a criterion naming a thing must name what produces it" rule from round 1's left-shift summary, applied to interfaces rather than to messages, and it is the second time this exact class has been the most expensive finding in a round. Build it once and it grades every future harness spec.

## H2 (finding 6) — the same defect from the data-model axis: S2b's input is declared nowhere

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md` §2 S2b and §4 Data model.

Filed independently and confirmed independently, so it is reported as filed. The observation it adds to H1 is about failure mode rather than about the interface: **no criterion in §6 could fail if the harness never received a callback at all.** The loop would run zero times, the run would exit after one audit round, and every criterion in the document would still be satisfied. AC7 exercises four states of a callback the args contract has no slot for, which means the loop is tested against a fixture shape the shipped harness cannot be invoked with — a test that passes on a mechanism that never ran.

**Fix:** H1's fix closes this one. Additionally give §6 an arm asserting the loop executed at least once — count the audit rounds and assert the count is ≥1 — so an absent verdict source reds instead of reading as convergence on the first pass.

**Left-shift gate:** The general form of the arm above. Any criterion asserting a loop, retry or convergence property must also assert the ITERATION COUNT is non-zero. A convergence test that passes when zero iterations ran is the reassuring-zero shape this repo refuses in its probes, one layer up, and it is cheap to state as a review-checklist entry even where it cannot be gated.

## H3 (finding 3) — the unit whose product is a merge-bar refusal never observes its own manifest row

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §2 S6 and §7 Gates.

S6 registers the new check in `tools/gate-legs.json` with a declared ceiling and has **no §6 criterion at all**. AC5 and AC6 observe the CHECKER — a staged fixture reds it, the clean fixture is green — and both pass when the script is invoked by hand. AC7 observes its liveness line. Nothing observes the manifest row. A unit whose entire product is a merge-bar refusal can therefore ship fully green with the leg registered nowhere, running on no bar, ever.

§7 compounds it by leaning on a leg that does not exist: **`gate manifest shape` appears in exactly one place in the whole tree, which is this spec's own §7 at line 133.** The check that actually enforces a declared ceiling is `run-gates.gov.test.sh:261`, under the leg `run-gates gov canary` at `gate-legs.json:776` — a leg §7 never names.

This is downstream of B2. The row H3 asks §6 to observe is the row B2 has not decided the shape of yet, so fix B2 first and then write this criterion against whichever branch was taken.

**Fix:** Add an acceptance criterion that READS the manifest: the new leg's row is present in `tools/gate-legs.json` with a numeric `ceiling`, and `bash tools/run-gates/run-gates.sh` schedules it, witnessed by the run-gates unbounded-leg warning naming zero new legs. Correct §7 to `run-gates gov canary` and `run-gates canary`, which are the legs that actually grade a manifest row.

**Left-shift gate:** Resolve every gate name a spec backticks in §7 against `tools/gate-legs.json` and red on a name that resolves to nothing. This is one `grep -F` per name against a file that already exists, it would have caught `gate manifest shape` and `unattended driver selftest` and `marker contract (4 readers)` in one pass — four findings in this record between them — and it is the single cheapest gate proposed anywhere in either round. **If exactly one gate is built from this review, build this one.**

## H4 (finding 1) — the fold's headline scope item has no criterion that can fail

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md` §2 S6, against §6 AC6 and AC7.

S6 is new in the fold and it closes round 1's M2: BUILD-METHOD M2 states the grading in the ordinals unit 1 abandons. The work S6 actually specifies — restating M2's THIN and FORKED sentences in section TITLES rather than ordinals — has **no criterion that could fail**. AC6 requires `wc -c` at most the pre-edit 24560 and 24571 bytes, and AC7 requires `kit-dogfood-parity.test.sh` green. **Both are satisfied by making no edit at all.**

The consequence is exact. Unit 1 can land green with `memory/guides/BUILD-METHOD.md:44-45` still reading `§2 Scope, §6 Acceptance or §7 Gates` and `§8 Open questions` — precisely the ordinal keying the classifier abandons — so the method and the machine disagree on exactly the Tier-1 specs that `TOOL-dBriefedPass-3` then hard-refuses. The parity leg cannot catch it: `kit-dogfood-parity.test.sh:53` byte-compares the render pair against each other, and its own header says a claim false in both halves is green forever. M1 states plainly that no gate enforces the byte budget, so AC6 is a manual measurement of a null edit. §7's other legs read pointers, not M2's wording. S7 even sanctions dropping S6 without any observation of the park.

**Fix:** Add a criterion that observes the CONTENT. `grep -c '§[0-9]'` over M2's classification list returns 0 in **both** `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md`, and the THIN and FORKED lines name `Scope`, `Acceptance criteria`, `Gates` and `Open questions` by title. Observe it RED against the shipped bytes first, the way AC2 already is.

**Left-shift gate:** A null-edit detector for acceptance criteria. Any criterion whose entire predicate is a bound (`at most N bytes`, `no more than N lines`) or an unchanged-state assertion (`leg X still green`) is satisfied by an empty diff, so a §2 item whose only criteria are of that shape is carrying no witness. Red a spec where every criterion cross-referenced to one scope item is bound-shaped or unchanged-shaped, and require at least one criterion that asserts a POSITIVE property of the new content. This is the most reusable gate in the record after H3's: **six of round 1's thirteen findings and five of round 2's twenty are criteria that cannot fail**, and they are recognizable by shape without reading the subject.

## H5 (finding 15) — B1's fix re-created B3's shape one document over

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md` §7 Gates and §4 Files touched, against §2 S8.

S8 is new in the fold. It now has this unit edit `SKILL.template.md` and regenerate `.claude/skills/unattended/SKILL.md`. §4's files list still names only the driver and its test, and §7 names no leg that grades that render pair.

`unattended skill wiring` — argv `["bash","tools/unattended/adopt-unattended.sh","--check"]`, **no `guard` key**, so it runs on every bar — renders `SKILL.template.md` to a temp file at `adopt-unattended.sh:239` and `diff`s it against the tracked Skill, reddening on a missed regeneration. That is the leg no section of this spec mentions.

The omission is specific rather than a blanket complaint, because the protocol half IS covered: check 10 at `check-unattended.sh:1236-1249` compares `PROTOCOL.template.md` to `UNATTENDED-PROTOCOL.md` inside the `unattended kit gate` leg that §7 already names. One half of S8's carrier set has a witness and the other does not.

This is round 1's B3 shape — an inventory omitting one half of a byte-compared render pair — re-created by B1's fix in a different document. It is graded HIGH rather than BLOCKER because B3's blocker grade rested entirely on the byte budget it ran into, and no budget wall applies here: the fix is four file names and one leg name.

**Fix:** Add the four carrier files to §4's list — `PROTOCOL.template.md`, `SKILL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md`, `.claude/skills/unattended/SKILL.md`. Add `unattended skill wiring` to §7. Extend AC7 to observe that leg green alongside `check-unattended.sh`.

**Left-shift gate:** B3's proposed render-pair gate, now earning its keep a second time. Derive the render pairs LIVE from the adopt scripts, which already name them, and assert that a spec §4 naming one half of a pair names the other half too. Round 1 proposed it for BUILD-METHOD and it would have caught this instance in spec 2 for free — which is the argument for building it rather than fixing the two instances by hand.

## H6 (finding 12) — the H3 fix names the wrong two readers, and AC4 and AC8 cannot both pass

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md` §4 Data model (the `kinds_re` sentence), against §2 S4 and §6 AC4 and AC8.

Both the sentence and AC8 are new in the fold. §4 says the brief row is matched by *"the `kinds_re` counters at `:2713` and `:3553`"*, and that this is *"what makes S5's `--status` split able to see these rows at all"*. Verified byte-for-byte, both of those counters are `grep -cE "^…Z (($(kinds_re "$PARK_KINDS_OWED")) · item |rescope · item …)"` — they alternate over `PARK_KINDS_OWED`, the set S4 explicitly keeps `brief` OUT of. The sentence is false for a history-class kind.

The two criteria are then mutually unsatisfiable. AC8 requires the brief row to be MATCHED by the driver's own `kinds_re` counter regex; AC4 requires `parked-decisions-surfaced` to be UNAFFECTED by any number of brief lines. An implementer satisfying AC8 against the counters §4 names has to add `brief` to `PARK_KINDS_OWED`, which inflates the surfaced-decision count `--close` grades and breaks AC4 and S4 together.

The counter that actually sees an unowed kind is `nnoted` at `unattended.sh:2726`, built from `park_kinds_unowed()` — the declared-minus-owed difference — and printed as `· noted N`.

**Fix:** Rewrite the §4 sentence to name `unattended.sh:2726` and `park_kinds_unowed()` as the reader, and to state that `:2713` and `:3553` must NOT match a brief row — **that non-match is what S4 buys**, and saying so turns the sentence from wrong into load-bearing. Restate AC8 against the `· noted N` field of `--status` rather than against `kinds_re` generically. Keep AC4 as the arm proving `· parked N` did not move.

**Left-shift gate:** This is the "a spec may not restate a value the tree already owns" rule from round 1's left-shift summary, and the mechanical form here is a line-citation check. A spec sentence citing `file:line` must be re-resolved at review time and the cited line must contain the identifier the sentence claims for it. `:2713` contains `PARK_KINDS_OWED`, the sentence claims it counts an unowed kind, and a substring check would have caught that. Cheap, and it grades the citation rather than the prose around it.

## H7 (finding 36) — S7 and S8 claim one check-26 carrier row at two different orders

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 S7, against `…-2.md` §2 S8.

*One defect with H8 and H9, reported as filed. This is the ordering axis.*

The fold reworded S7 from "the protocol's section 7 verb list gains `--brief`" to "gains the verbs this build adds" — verified in the `c5ceb93e..24ddc653` diff — **in the same commit that moved that exact row into spec 2's S8**, whose text reads *"THE VERB'S THREE PROSE CARRIERS LAND IN THIS UNIT, not at order 5."* So the two rev-2 sentences disagree about scope, and the fold created the disagreement while fixing the thing it was raised to fix.

Check 26's protocol predicate is `*$'\n'"- "?"$v"?" - "*` over `SHIP="$HERE/PROTOCOL.template.md"`, and the only rows in that file matching it are section 7's verb list — so section 7's list IS the check-26 carrier, not some second list S7 could be referring to. The build adds exactly one verb, `--brief`. S7's population and S8's protocol carrier are therefore the same single row.

Either resolution is bad. Follow S7 and defer to order 5, and `unattended kit gate` reds at unit 2 and stays red through units 3 and 4 — the precise B1 defect the fold was raised to close. Follow S8, and S7 is a no-op that will read as an omission at unit 5.

**Fix:** Reword S7 to state that the protocol's section 7 row for `--brief` landed at order 2 with the verb per `TOOL-dBriefedPass-2` S8, and that this unit adds no verb row — mirroring the wording S3 already uses for the Skill's rows. Or delete S7 and let spec 5's AC7 be the only place the join is observed. Record the correction in §9.

**Left-shift gate:** A cross-spec ownership check over a build's spec set. Parse every §2 item that names a FILE plus a REGION, and red when two units in one build claim the same pair. The set is small, the specs are already parsed by `gen_build_index.py`, and this is the exact class M2's cross-spec agreement rule asks a human to catch by reading five documents at once — which is the reading that failed here, twice, in the round that was told to do it.

## H8 (finding 31) — the same claim from the scope axis, with the inventory row compounding it

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 S7, against `…-2.md` §2 S8 and spec 5's own §4 Inventory.

Filed and confirmed independently on the scope axis of M2's cross-read. What it adds to H7 is the ARGUMENT that spec 2 used to justify the move: all three check-26 carriers must land with the verb or the unguarded leg reds through units 3 and 4. S7 contradicts that argument in the fold that was supposed to settle it, and a unit-5 builder trusting S7 re-opens the ordering question round 1 blocked on.

It also names the compounding: §4's inventory still says `SKILL.template.md` gains "two verbs, one directive row" while S3 says it carries no `--brief` rows and this unit adds no verb of its own. **B1's fix is not agreed across the two specs it touches, which is precisely the cross-spec agreement M2 requires.**

**Fix:** H7's fix, plus change the §4 inventory row for `SKILL.template.md` from "two verbs, one directive row" to "one directive row". See M5, M6 and M7 for that cell read from three other directions.

**Left-shift gate:** H7's cross-spec ownership check covers this. The additional discipline worth writing into the review checklist rather than a gate: **when a fold moves a scope item between units, both documents are edited in the same commit and both are re-read afterwards.** Every one of H7, H8, H9 and M4 exists because the source of the move was edited and the destination's neighbour was not.

## H9 (finding 13) — the same claim from the ownership axis, and S7's stated ground is false

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 S7, against §2 S3 and `…-2.md` §2 S8.

Filed and confirmed independently on the ownership axis. Two units own one edit on the four-axis scope test, and the finding adds the sharpest observation of the cluster: **S7's stated ground is contradicted by S3, three bullets above it in the same document.** S7 justifies leaving the verb list ungated on the claim that it is "joined to nothing"; S3 says in as many words that "check 26 joins a verb to three carriers and the leg that runs it is unguarded". The document argues both sides of the ordering question round 1 blocked on, in one section, at rev-2.

`PROTOCOL.template.md:437` `## 7. The verbs` is the file and section check 26 fails on at `check-unattended.sh:2044-2050`; `VERBS_SLUG` and `VERBS_INLINE` at `unattended.sh:86-89` plus all five specs make `--brief` the only verb this build adds.

**Fix:** H7's fix. Additionally, add to §9 that S7's "joined to nothing" ground was withdrawn, so a later reader does not restore it from the revision log.

**Left-shift gate:** An intra-document contradiction check is not buildable in general, but its cheapest useful form is. Where a spec cites a decision id as the GROUND for a non-goal, resolve that id and red if the same document elsewhere cites a mechanism that closes it. Here `TOOL-dUnstalledConvoy-17` grounds S7 and `check-unattended.sh` check 26 is named by S3 as closing it. See L1, which is the same citation read on its own.

## H10 (finding 5) — S5 is a no-op and AC5 names an output the driver deliberately does not produce

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md` §2 S5 and §6 AC5. Pre-existing; the fold did not touch either.

S5 says `--status` counts briefs apart from questions. That is already true the moment S4 adds `brief` to `PARK_KINDS`, with no code written, so S5 specifies no work.

AC5 is worse than a no-op under either reading. Its literal wording — `--status` prints the brief count separately from the decision count — names an output the driver **deliberately does not produce**: `unattended.sh:2721-2727` prints ONE aggregate `noted` field over every unowed kind, with the driver's own comment refusing a per-kind label, *"the unowed set is DERIVED and holds three kinds, so a label naming one of them would be wrong about the other two."* Under the loose reading, an arm asserting `noted` passes identically if the verb wrote a `proposal`, a `dispatch` or a `review` row. So the one criterion covering the history half of the classification cannot distinguish the kind it exists to prove, and satisfying its strict reading contradicts a recorded design decision in the very file the unit edits.

**Fix:** Pick one. Either state in S5 that briefs land in the existing `noted` aggregate and DELETE AC5 as a no-op, since AC4 and check 27 already carry the classification. Or specify the per-kind split S5 implies and give AC5 a falsifiable arm: with one brief and one proposal recorded, `--status` reports the two apart, and dropping `brief` from `PARK_KINDS` reds that arm. The first branch is cheaper and does not fight the driver's recorded decision.

**Left-shift gate:** H4's null-edit detector catches the S5 half — a scope item that is true before the unit starts. The AC5 half is the round-1 rule "a criterion naming a message must name what produces it", and the mechanical form is a grep: a criterion quoting an output field must find that field in a `printf`, `echo` or heredoc inside the unit's declared file set. `noted` is there; a separate brief count is not.

---

# MEDIUM — 7

## M1 (finding 17) — three specs claim a merge bar containing a leg that cannot run

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md` §7 Gates, and the same defect in `…-2.md` §7 and `…-3.md` §7. Pre-existing.

§7 names `unattended driver selftest` and `marker contract (4 readers)`. Neither resolves against `tools/gate-legs.json`, which holds 86 legs: the marker row is named **`marker contracts`**, and no leg named or resembling a driver selftest exists — the only unattended rows are `unattended kit gate` and `unattended skill wiring`.

`tools/unattended/kit.toml:60-80` records the owner ruling of 2026-08-23 under the heading *"THIS KIT'S SELF-TESTS ARE NOT GATE LEGS"*, naming `unattended.test.sh` explicitly, and makes `bash tools/unattended/run-unattended-gates.sh` the compensating condition of done for work touching `tools/unattended/`. So every arm units 1, 2 and 3 put in that suite — spec 1 S4 and S5, spec 2 S7, spec 3 S7 — is witnessed by nothing on the bar, and none of the three specs names the compensating command.

**Where the wrong name came from is worth recording**, because it changes the fix. `run-unattended-gates.sh:175` has a row literally called `driver selftest`. The spec did not invent a leg; it took a row name out of the compensating RUNNER and filed it as a merge-bar leg. That is a more honest error than it looks and a more dangerous one, because the name resolves against something real when a reader greps loosely.

**One caveat the fix must resolve rather than paper over.** `run-unattended-gates.sh:54` defaults to `--selftests`, and the kit descriptor's compensating condition is a GREEN verdict from `--selftests` pasted into the landing report. This session carries a recorded standing owner instruction that the unattended self-tests are not to be run, `--checks` being fine and `--selftests` not. I did not find that instruction restated in the tree, so I am flagging it rather than asserting it: **the specs cannot simply name `--selftests` as their witness without the owner confirming which arm they mean.** If the standing instruction holds, the three units need an explicit owner disposition for the arms they are placing in `unattended.test.sh`, and §7 should record that disposition rather than a command name.

**Fix:** Replace `marker contract (4 readers)` with `marker contracts` in all three §7 lists. Drop `unattended driver selftest` from all three. Name the compensating witness explicitly and unambiguously — the command, the arm, and the owner disposition on that arm — with its verdict owed in the landing report.

**Left-shift gate:** H3's gate-name resolution check. It closes M1 and H3 together, four wrong names in one pass, and it is the cheapest gate in this record.

## M2 (finding 16) — a stale bullet instructs the builder to re-introduce the exact defect round 1 blocked on

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md` §5 Production-readiness checklist, Observability bullet. Fold-caused.

The bullet still reads *"the refusal in S3 names the file and the duplicated title"*, after rev-2 replaced S3's refusal with a deterministic first-occurrence bind. §3 now **forbids** that output in terms — *"it adds no third outcome to `plan_state`"* … *"a refusal token would have been a new outcome"* — and spec 3's §4 step 3 depends on its absence to call MISSING and THIN "the whole refused set".

The cited mechanics hold and are why this is a defect rather than a style residue. `verb_plan`'s `case` at `unattended.sh:2074` branches only on `THIN|FORKED|READY`, and `build-complete` at `:3271` is a bare `[ "$(plan_state "$_bcsp")" = THIN ]` that discards the exit status. A refusal token would grade silently non-THIN at the one site where the grade decides a landing. A builder implementing the surviving §5 sentence re-introduces round 1's H1 in full.

**Fix:** Replace the bullet with what the unit actually emits on the duplicate path, which is nothing, and point observability at AC5's two arms — the only witness the first-occurrence rule has.

**Left-shift gate:** Not gateable, so it goes on the checklist as a fold discipline: **when a fold rewrites a §2 or §3 item, every other section citing that item by name is re-read in the same edit.** Five of this round's thirteen fold-caused findings are exactly this, and a two-minute grep for the item's identifier across its own document would have found all five.

## M3 (finding 8) — the liveness line reports two counts over a three-population check

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §2 S5 and §6 AC7. Pre-existing.

S5 declares the liveness assertion as two per-BUILD numbers — builds graded, builds skipped by the cutoff — and AC7 observes only those two. §4 step 2 creates a third, per-UNIT population: units counted `unbuilt-in-range`, which neither number reports.

§4 itself names the common case: a run whose units were built before its own BASE is *"the ordinary shape for a resumed build"*. So the ordinary case prints a reassuring `graded 1 · skipped 0` over a check that graded zero units, and no criterion can fail on it. That is the reassuring-zero reading S5 exists to prevent, in S5's own words.

Ranked first among the mediums because the charter's position on this is unambiguous — a green audit must mean the checks ran — and because the fix is one counter.

**Fix:** Make S5 declare three counts: builds graded, builds skipped by cutoff, units unbuilt-in-range. Extend AC7 with an arm over a fixture whose units all fall outside `BASE..HEAD`, asserting the unbuilt count is printed and non-zero.

**Left-shift gate:** A liveness-arity rule for the review checklist, and a candidate gate for checkers that already emit a liveness line. Every population a check ITERATES must appear in its liveness line. Where a checker's populations are enumerable — a loop over a declared set — this can be asserted mechanically; where it cannot, it is a checklist entry. Either way the rule is stated once: **a liveness line naming fewer populations than the check walks is a partial probe reporting as a whole one.**

## M4 (finding 10) — S7 has no criterion, and the criterion that exists credits another unit

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 S7. Fold-caused.

The criterion axis of the H7/H8/H9 cluster, graded medium because the fix here is the smallest of the four. S7 has no §6 criterion of its own. AC7 grades check 26 green over every verb this build declares, and **explicitly attributes the rows to `TOOL-dBriefedPass-2` S8** — so spec 5's own criterion says the edit is not this unit's, while its own scope item says it is.

`check-unattended.sh:2045-2049` matches `- ?<verb>? — ` lines in `PROTOCOL.template.md`, and section 7 of that file at line 437 is exactly that list, so the row must land at order 2 or the unguarded leg is red for three units. This build adds one verb. S7 at order 5 is a no-op or a second unit editing one list.

**Fix:** Withdraw S7 and let AC7 stand as the observation. Or restate S7 as the residual verbs check 26 does not join, and name them — there are none today, which is the point.

**Left-shift gate:** Every §2 scope item must be cross-referenced by at least one §6 criterion, and a criterion attributing its subject to a DIFFERENT unit id does not count as that reference. Both halves are mechanical against the spec template's own structure, and this single rule would have caught H4, H3, M4 and half of H10 — **four of this round's twenty findings are scope items with no criterion at all.**

## M5 (finding 19) — the inventory cell asserts what S3 negates

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §4 Inventory, the `SKILL.template.md` row, against §2 S3. Fold-caused.

*One defect with M6 and M7, reported as filed.*

The row says the Skill template gains "two verbs, one directive row". S3 at rev-2 says it *"does NOT carry the `--brief` rows"* and that what it gains is the harness plus one directive handle. Verified at rev-1 (`c5ceb93e`), S3 then read "gains the harness to its 'While it runs' verbs AND the `--brief` verb" — which is where "two verbs" came from. The fold rewrote S3 and edited the inventory table, removing the BUILD-METHOD row, and left this cell untouched.

§4's Files touched forwards to that table — *"The seven rows of the inventory table above"* — so the table is the authoritative instruction. A builder following it adds Skill verb invocations at order 5, which check 26 then requires in the driver header and the protocol too: the ordering B1 was blocked on, restored by a stale cell. The count is independently wrong under any reading, since the build adds one verb and unit 5 adds none.

**Fix:** Change the cell to "the harness in 'While it runs', one directive row" and record in §9 that the verb rows moved to `TOOL-dBriefedPass-2` S8, the same correction S3 already carries.

**Left-shift gate:** M2's fold discipline covers it. The gateable half is narrower and still worth having: where a spec §4 table and a §2 item name the same file, red when one asserts a token the other's sentence negates within the same document. Start with a small closed token list — the build's own declared verbs and kinds — rather than attempting general contradiction detection.

## M6 (finding 40) — the same cell, plus a derived count authored in prose beside the table that owns it

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §4 Inventory and §4 Files touched. Fold-caused.

Filed independently. What it adds to M5 is the second half: the same fold commit deleted the BUILD-METHOD row, leaving *"The seven rows of the inventory table above"* pointing at a six-row table.

The row-count half is the weaker claim and is reported as such — seven FILES is still right, since the `.unattended.conf` row names two and §5 says "the seven files". But it is a derived figure written in prose beside the source that owns it, which §7 of the charter bans **for exactly the reason it has already gone wrong here**: the table changed and the number did not.

**Fix:** Replace "The seven rows of the inventory table above" with "the carriers named in the inventory table above", so no count is authored beside the table that owns it. Apply M5's fix to the cell.

**Left-shift gate:** The general rule already exists in the charter and has no mechanical form for prose. The cheap approximation: red a spec sentence containing a written-out number immediately adjacent to a markdown table, and require the count to be derived or the number removed. False positives are acceptable here because the corrective action — delete the number — is always safe.

## M7 (finding 9) — the same cell, and the PROTOCOL row omits S7's edit

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §4 Inventory, rows `SKILL.template.md` and `PROTOCOL.template.md`, against §2 S3 and S7. Fold-caused.

Filed independently. It adds the second stale row: the `PROTOCOL.template.md` cell omits S7's §7 verb-list edit entirely, so §2 and §4 name two different edit sets for one unit. AC5 is a diff-scoped criterion graded against what this unit is supposed to touch, which makes the table load-bearing rather than descriptive. **This is the half of the B1 fix that was not carried through.**

**Fix:** Rewrite the Skill row per M5. Add the verb-section row to the PROTOCOL cell, or drop S7 per H7 and H9 — and if S7 is dropped, the PROTOCOL cell is already correct and only the Skill cell needs the edit. Resolve S7 first; this row's correct value depends on that answer.

**Left-shift gate:** H7's cross-spec ownership check plus M4's scope-to-criterion cross-reference between them cover this. No new mechanism is proposed for it.

---

# LOW — 1

## L1 (finding 41) — a superseded backlog row cited as the reason a carrier stays ungated

**Where:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 S7, second sentence. Pre-existing, carried through the fold.

S7 justifies not gating the protocol's verb list by citing `TOOL-dUnstalledConvoy-17` as live: *"this list is already incomplete and joined to nothing."* Both halves are false today. The driver declares 14 `VERBS_SLUG` plus 3 `VERBS_INLINE` at `unattended.sh:86,89`, and each of those 17 has exactly one `` - `--verb` — `` row in **both** `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` — including `--park` and `--attest`, the two the backlog row names as missing. Check 26 joins every declared verb to that section on an unguarded leg.

The timing makes it a clean supersession rather than a disagreement: the backlog row landed 2026-08-20 and check 26 landed 2026-08-21. The row's specific claim was closed by the check that landed the day after it.

Graded LOW because it changes no scope and reds no leg. It is in the record because it is the one sentence in S7 that tells the next reader this carrier is ungated and can be forgotten safely, and that belief is what let the row's original defect ship.

**Fix:** Reword to say check 26 joins section 7 to the driver's verb declarations in the direction that matters — every declared verb has a row — and that `TOOL-dUnstalledConvoy-17`'s remaining half is the reverse direction and the ORDERING principle, not completeness. Or drop the citation and let AC7's check-26 assertion stand alone. If S7 is withdrawn per H7, this resolves with it.

**Left-shift gate:** A citation-freshness check over decision and backlog ids quoted in specs. When a spec cites an OPEN id as the ground for a non-goal, resolve the id and compare its date against the tree: if a gate leg or check landed after that row and joins the population the row calls unjoined, red with both dates named. This is narrow enough to have precision, the corpus is already indexed for retrieval, and it catches the general class — **a superseded record carried forward as live rationale.**

---

## Left-shift summary

Nineteen gates are proposed above and they are far fewer mechanisms than that.

**Four gates would have caught fifteen of the twenty findings**, and all four are small.

1. **Resolve every gate name a spec backticks against `tools/gate-legs.json`.** One `grep -F` per name. Catches H3, M1 across three specs, and the `gate manifest shape` half of B2. Four wrong leg names in one pass. **Build this one first — it is the cheapest gate in either round.**
2. **Cross-reference every §2 scope item to at least one §6 criterion**, and reject a criterion that attributes its subject to a different unit id. Catches H3, H4, M4, and the S5 half of H10. Four scope items in this set have no criterion at all.
3. **Reject criteria that only a null edit could satisfy** — bound-shaped (`at most N bytes`) and unchanged-shaped (`leg X still green`). Catches H4, H6, H10, and would have caught round 1's H4 and M2. Recognizable by shape without reading the subject.
4. **A cross-spec ownership check over one build's spec set**: red when two units claim the same file-plus-region. Catches H7, H8, H9, M4, M7. This is M2's cross-spec agreement rule made mechanical, and the human reading of it has now failed twice on the same row.

Round 1 identified three underlying rules and all three held. **"A spec may not restate a value the tree already owns"** reappears as H6, M6 and L1. **"A criterion naming a gate or a message must name what produces it"** reappears as H1, H2, H3 and H10 — it was round 1's recommendation for the one gate to build if only one could be built, and it is again the class carrying the most findings. **"A claim contradicting a ratified decision or an owner ruling should red before it is built"** reappears as B1 against `TOOL-cSettledDocket-14`, and as H1/H2 against the README's review-loop ruling.

The new rule this round adds is a process rule rather than a gate, and it is the one with the largest measured payoff. **Thirteen of twenty findings are a sentence that went stale when a neighbouring sentence moved.** Re-reading the sections adjacent to every fold edit is free, requires no tooling, and would have removed roughly two thirds of this round's confirmed population before it was filed.

## What this round did not check

This is still a pre-code audit. It grades five documents and their joins to the tree at the pinned blobs; no implementation exists to grade. Four consequences worth stating so a green round 3 is not misread.

Nothing here re-audits the round-1 findings' fixes for correctness beyond the residues named above. The five blockers are recorded as disposed because none was re-raised by a confirmed finding, not because each fix was independently re-derived end to end.

Nothing here exercises the harness, `plan_state`, the proposed gate leg, or any check. Every claim about runtime behaviour is read from source, plus the manifest and script reads the author ran to verify B1, B2, H3, M1 and the fold-attribution figures.

The twenty-one refuted findings are refuted as FINDINGS, not certified as correct. A lens that failed to make its case leaves the underlying question open rather than answered.

**One caveat is outstanding rather than closed, and it belongs to the owner.** M1's fix names `bash tools/unattended/run-unattended-gates.sh` as the compensating witness for arms that three units are placing in `unattended.test.sh`. That script defaults to `--selftests`, and this session carries a recorded standing instruction that the unattended self-tests are not to be run. I did not find that instruction restated in the tree and did not run the suite. The specs need the owner's disposition on which arm witnesses those criteria before M1's fix can be written down as a command.
