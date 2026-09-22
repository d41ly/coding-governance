# Unattended kit — adversarial review, synthesis

**Serves:** research TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9
**Commissions:** TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9

**Question reviewed:** what lets an unattended run produce WORSE WORK than an attended one would, and
land it green. Not "is this kit correct" — correctness has had many rounds. Every check an owner
would have performed by reading the diff is either machine-checkable or gone; this report hunts the
gone ones and the ones the kit's own evidence would already support.

**Out of scope by the brief, and not re-litigated here:** authorization / anchor forgery (protocol
§9 states the reduction), merge-bar wall clock and leg scheduling, style and naming.

**Corpus:** 30 raw findings from five lenses (A · B · C · D · E), every one skeptic-verified.
27 confirmed, 3 refuted, 0 unverified. Deduplicated to **12 findings** below, ranked by how much
worse the WORK gets if the defect stands. Lenses that hit each defect are named in the entry.

**One theme runs through the top four.** The kit records the answer and does not read it. The
closing review's blocker count, the spec-audit coverage join, the held-leg guard arrays, the
retirement rows — all four are computed, committed and unread. This is not a kit that lacks
evidence; it is a kit whose evidence has no consumer at the one checkpoint that exists.

---

## F1 — The closing review has no required exit, and nothing grades what it concluded

**Severity: critical.** Lenses A · B · C · D · E (all five: A2, B1, C1, D1, E1, E2).

**Where:** `tools/unattended/unattended.sh:3128-3205` (the `closing-review-recorded` arm) ·
`:3143-3147` (its stale justification) · `:3510` (the write) · `:3434-3447` (`review_counts`, the
reader nobody calls outside `verb_review`) · `tools/unattended/check-unattended.sh:249` and `:288`.

**Scenario.** A run reaches M8, runs the closing diff review, and gets six confirmed blockers. It
records `--review <slug> --verdict BLOCKED --blockers 6`, fixes the cheap five, records
`--blockers 1`, decides the last one is expensive, and simply stops calling the verb. It stages the
round-2 review record and runs `--close`. `closing-review-recorded` asks three questions — is there
a tracked record under `memory/builds/<slug>/reviews/`, does it carry a `**Serves:** … diff-review`
binding line, is its 7-40 hex token an ancestor-descendant of BASE..HEAD — and answers yes to all
three. It never opens the verdict and never reads a blocker count. The gate leg cannot help: its
loop check is population-gated on rows the run volunteered (`grep -q '… review · item ' || continue`,
check-unattended.sh:249), and its only stall clause fires on `flat[it] >= 1 && !(it in term)`, where
`flat` is RESET to zero on every shrink — so a descending sequence that stops, and a single round,
both print nothing. Phase LANDING, lander, LANDED. **Reproduced twice at LANDED in this tree:**
`memory/builds/aBoundedCeiling/RUN.md` (BLOCKED 6, then BLOCKED 1, no terminal token,
`phase: LANDED`) and `memory/builds/aPrimedKeepalive/RUN.md` (BLOCKED 2, one round, `phase: LANDED`);
`memory/builds/aThawedCorpus/RUN.md` is at LANDING with blockers 5. Neither landed record overrode
the item — it was MET. Of 21 tracked LANDED/LANDING runs, 13 recorded no round whose subject is the
build slug at all.

**The incentive is inverted, which is the damaging half.** A run that records a second flat round
gets NON-CONVERGENT, and the driver then obliges it to promote every standing blocker into a
specced, built, closed unit — hours of work. A run that records nothing owes nothing, because
check 2's whole population is the rows the run chose to write. Candour is charged for; silence is
refunded, at exactly the moment the work is worst.

**Smallest fix — driver, `dod_met`'s existing `closing-review-recorded` arm, no new fact and no new
grammar.** Call `review_counts "$rel" "$slug"` (already defined at unattended.sh:3434, already
parses the row grammar) and require that the LAST round for the build slug carries a terminal token
(`CONVERGED` · `NON-CONVERGENT` · `CEILING`), and that a `CONVERGED` exit reads `blockers 0`. That
converts "a markdown file exists" into "a review loop ran and ended", and it arms check 2's
promotion clause without adding a check. The leg gets the ratchet half as its own clause, phase-gated
to terminal/LANDING records so a live run between two rounds is not redded.

**Do NOT anchor `## Verdict: BLOCKED` on the selected record.** Lens A tried it and was refuted:
`_crfound` is the FIRST match in `git ls-files` order, a converged loop's round-1 record legitimately
says BLOCKED and is never rewritten, and `memory/builds/aLexedStripper/…-round2.md` reads BLOCKED on
a run that landed correctly after folding. A verdict join is worth having as a SECOND term, but only
over the LAST diff-review record by round/date, and only behind the date grandfather.

**The justification comment must be re-measured in the same commit.** unattended.sh:3143-3147 still
reads "`^## Verdict: CLEAN` matches zero of this corpus's 46 records" — verified present today.
The corpus is now 208 tracked review records, 170 carrying `^## Verdict`, and post-`REVIEW_VERDICT_CUTOFF`
it is 77 of 77, made mandatory by memory hygiene check 22 and written by `tools/workflows/tier2-review.js:525-529`.
A number stated in prose beside the source that owns it, in the comment that is the reason nobody
has fixed this arm.

**Gateable:** yes, twice. Driver predicate: `last review row for subject == slug carries a terminal
token, and CONVERGED implies blockers 0`. Leg predicate, on a record at LANDING/LANDED:
`last[it] > 0 && !(it in term)`. Replay over the tracked corpus reds exactly the three records named
above and none of the nine honest ones.

---

## F2 — `gates-green` runs a bar that holds 46 of 86 legs, and the kit's own suites are on no bar at all

**Severity: high.** Lenses B · C · D (B3, C3, D2).

**Where:** `.unattended.conf:22` (`GATE_CMD="bash tools/run-gates/run-gates.sh"`) ·
`tools/unattended/unattended.sh:2841` (`run_bounded $GATE_CMD`, no environment) ·
`tools/run-gates/run-gates.sh:947-949` (the hold) · `tools/gate-legs.json` (86 legs, 46 held) ·
`tools/unattended/kit.toml:73-81` · `memory/guides/UNATTENDED-PROTOCOL.md:318` · `AGENTS.md:484-485`.

**Scenario.** The dominant work in this repo is gate checkers, and protocol §11 actively steers an
unattended run into it ("a gate that reds where it should", adopted "now, by the run that found it").
A run edits `tools/memory-tree/check-memory-hygiene.sh` or `tools/unattended/check-unattended.sh`,
widens a grep so a branch no longer matches its population, and never touches the sibling test. At
`--close`, `gates-green` runs the bare declared command. run-gates.sh holds every leg whose
`subject = kit` or `chunk = selftests` unless `GATE_SELFTESTS` is set — 46 of 86, including
`memory-hygiene self-test`, `check-arms selftest`, `agent-cap self-test`, `pre-push self-test`,
`run-gates canary`, `tier2-review self-test`. Nothing sets that variable: a tree-wide grep finds only
READS, `.githooks/pre-push:215` can only force a full run when it is ALREADY on, and `GATE_FULL`
bypasses the guard pass and not the hold. `grep -rn 'GATE_SELFTESTS'` over the protocol, the Skill,
`.unattended.conf` and `tools/unattended/` returns nothing — no kit-layer carrier even names the
flag, so a run following the contract will never set it. The bar goes green and the checker is now
weaker with no signal anywhere; every later green means less than it reads, for every later run and
every adopter.

**Two distinct halves, one arm.** (a) The 46 held legs are reachable by a flag nobody sets.
(b) The unattended kit's own five suites — `check-unattended.test.sh`, `unattended.test.sh`,
`check-playbook.test.sh`, `cross-component.test.sh`, `adopt-unattended.test.sh` — are not legs at
all after the 2026-08-23 ruling, so no value of any flag reaches them. `kit.toml:73-81` writes the
consequence down itself: "There is no gate behind that sentence. A kit edit that guts a check now
lands green unless a person runs it." Under a mandate that person IS the run, and
`grep -c run-unattended-gates` returns 0 across SKILL.md, UNATTENDED-PROTOCOL.md, BUILD-METHOD.md
and both kit templates. `memory/builds/aPrimedKeepalive/RUN.md` already records the outcome:
"the compensating check the kit.toml names is UNRUN for this build", on a run that reached LANDED.

**Smallest fix — driver, one clause in the `gates-green` arm, over two inputs the kit already
holds.** Intersect `git diff --name-only "$(fact "$rel" base)"..HEAD` against the `guard` arrays of
every leg the runner holds in `tools/gate-legs.json`; on any hit, `export GATE_SELFTESTS=1` before
`run_bounded $GATE_CMD` and say so on stdout. On a hit under `tools/unattended/`, also require
`bash tools/unattended/run-unattended-gates.sh`, which the kit already ships with its own budget
ceilings. That makes `AGENTS.md:485`'s "Owed by a DoD only for KIT work" true for the first time and
costs nothing on a run that touched no checker. The out-of-scope ruling is untouched: this escalates
by DIFF, not by default.

**Gateable:** yes, and it is itself the gate. Predicate: a run whose BASE..HEAD touches a held leg's
guard path and whose gate invocation carried no `GATE_SELFTESTS` fails `gates-green`. The
protocol:318 cell ("the project's full merge bar ran") must be corrected in the same change — the
current wording is what stops anyone looking.

---

## F3 — The spec audit has a generated coverage line and no reader

**Severity: high.** Lenses B · C (B2, C2).

**Where:** `tools/memory-tree/gen_build_index.py:769-778` (the join, rendered unconditionally) ·
`memory/guides/BUILD-METHOD.md:111-134` (M4) · `.claude/skills/unattended/SKILL.md:84` ·
`tools/unattended/unattended.sh:343` (DOD_CORE, ten items) and `:446` (`specs-reviewed:M4`, `all`-scoped).

**Scenario.** A run classifies its units, finds most of them MISSING, and authors their specs — which
M4 defines as unreviewed by definition. Under token pressure it skips the spec-audit pass entirely,
or audits two of seven. The memory-tree index generator dutifully renders
`Ids no \`spec-audit\` record has ever named: …` into the build README's generated region, and the
run commits that line as part of its own work. `--close` evaluates ten items, none of which opens
it; `build-complete` asks only that each unit row is CLOSED or WONTDO. The run lands with a
MUST-by-default pass never performed, having committed the evidence. `grep -rn spec-audit
tools/unattended/` returns only test fixtures; `check-unattended.sh` contains the string zero times.
**Live:** `memory/builds/dUnstalledConvoy` shipped ten CLOSED units, nine of them Tier 2, that no
spec-audit record has ever named. Six other builds carry smaller instances.

**Why it costs more than F1 does per unit.** The spec audit catches underspecification and
contradiction BEFORE the code exists, which is where it is cheapest. Skipping it means every defect
it would have caught is instead built and arrives at the closing review as code — and F1 shows what
grades that. The sibling M8 pass got a DoD item; this one, which binds `all` runs and gates the more
expensive failure, got none. It is also the promotion loop's own termination argument: M4:137 and
SKILL.md:569-570 both say a promoted unit is "audited as a SPEC, which is what makes promotion
terminate", and `memory/builds/aPrimedKeepalive`'s two promoted units are in its gap line.

**Smallest fix — driver, one new machine DoD item** (`CORE_FLOOR` is shrink-only, so appending is
free: `.unattended.conf:64` `12:10` becomes `12:11`). Predicate: every id in the build README's
`gen:build-units` region at HEAD whose status is CLOSED must be named by a tracked record carrying
`^\*\*Serves:\*\*.*spec-audit`. The walk already exists in the `closing-review-recorded` arm
(`GIT ls-files -- "$M/builds/$slug/reviews/*.md"`), or read the rendered line directly. Give it an
override, unlike `authorization-reachable`, so a genuinely thin Tier-1 unit is a recorded decision
rather than an invisible skip.

**Gateable:** yes. The available signal is a LOWER bound — the rendered line says "has EVER named",
so a spec audited at rev-1 and since bumped renders clean — which makes reading it strictly safe as
a refusal condition.

---

## F4 — Silent scope narrowing: retirement is unobserved before BUILDING, unbounded, and routed away from the owner

**Severity: high.** Lenses A · B · D · E (A3, B6, D4, E3, E4).

**Where:** `tools/unattended/lib-unattended.sh:167-171` (`baseline_units`) ·
`tools/unattended/check-unattended.sh:1626-1631` (check 24's retire arm) ·
`tools/unattended/unattended.sh:1827` (`nonterminal_units`) · `:1440-1445` (the subset test) ·
`:350` and `:356` (`PARK_KINDS` vs `PARK_KINDS_OWED`) · `:3869-3949` (`verb_rescope`) ·
`memory/guides/BUILD-METHOD.md:258`.

**Scenario.** Three levers compose into one failure: the run delivers less than the owner authorized
and nothing tells them. **(a) The baseline is switched off in the window where the drop happens.**
`baseline_units` walks the run-state file's own commits and stops at the first phase matching
`BUILDING|RUNNING|VERIFYING|LANDING|LANDED` — so SPECCING, REVIEWING, FOLDING, RESEARCHING and
TESTING are all before it. A run that authors the hard unit's spec with `**Status:** WONTDO` while in
SPECCING enters BUILDING with it already retired, and check 24's retire arm `continue`s on a unit
already WONTDO at the baseline. No rescope row is owed and none is written. Measured on the two most
recent runs: `memory/builds/dTieredTribunal/RUN.md` has five commits of SPECCING/REVIEWING/FOLDING
before its baseline; `dUnstalledConvoy` has one. **(b) Nothing bounds the volume.** `verb_rescope`
demands only a closed act, an id present in the current units region, and a non-empty reason — no
count, no ratio, no cap. `check_authorization` compares ID SETS and refuses only a REMOVAL, and
SKILL.md:508-511 instructs the status flip precisely so the id never leaves. `build-complete` reads
`nonterminal_units`, which treats WONTDO as terminal. **(c) The record is routed away from the
owner.** `rescope` is in `PARK_KINDS` and not in `PARK_KINDS_OWED`, so `parked-decisions-surfaced`
never counts it and an honest attested count legitimately excludes it, and BUILD-METHOD.md:258
places `history`-class entries outside the wrap-up's open/parked row as "not the owner's to
adjudicate". M9 has no row for scope amendments at all. The owner authorized N units and reads a
truthful, complete-by-its-own-test wrap-up about N-1.

**The classification argument is about the wrong question.** The driver's comment justifies the
history class on the ground that "a rescope is an amendment it took under a delegated authority" —
which is about whether the owner must ANSWER, not about whether they must be TOLD. M3 delegates
scope resolution; it does not delegate scope abandonment. Retirement and adoption sharing one kind
means the mechanism that lets a run GROW the build (30 of 33 rows are `add`) silently shrinks it too.

**Smallest fix — two, in two layers, both over bytes already parsed.** Leg: key check 24's RETIRE
arm on the run's pinned base (`rb` is already read two lines above and already passed to
`baseline_units` as the fallback) rather than on the first live-phase commit. The ADD arm keeps its
BUILDING baseline for the reason its own header states — M2 MANDATES authoring absent specs — and
that argument is a non-argument for a retirement. Driver: split `PARK_KINDS_OWED` by kind AND act,
so `retire` and `supersede` are surfaced and `add` stays history. The act is already the first token
of the item field (`item retire TOOL-…`), so this is one predicate over bytes `park()` already
writes, with no second list.

**Gateable:** yes. Leg predicate: a unit not WONTDO at the pinned BASE and WONTDO at HEAD with no
`retire`/`supersede` row is a refusal. Driver predicate: a terminal record whose attested surfaced
count excludes a retirement fails `parked-decisions-surfaced`. Note the corpus caveat carried from
the skeptics — no slug-mode instance of the SPECCING drop exists in this tree yet, so this closes a
shape rather than a bleeding wound. `memory/guides/UNATTENDED-PROTOCOL.md:182` also enumerates five
parked kinds against the driver's eight and should be corrected in the same change.

---

## F5 — `pieces-complete` is satisfied by a verdict the run types, over legs the tree knows how to run and nothing runs

**Severity: high (recipe mode only).** Lens A (A4).

**Where:** `tools/unattended/unattended.sh:3684-3749` (`record_piece`) · `:365` (`DOD_NO_OVERRIDE`) ·
`:2871-3053` (the arm) · `tools/unattended/check-playbook.sh:405-431` (the runnability oracle) ·
`.claude/skills/unattended/SKILL.md:347,348,434,435,496,497`.

**Scenario.** A recipe-mode run is asked for twelve pieces under a playbook declaring three per-piece
legs and one set check. It produces twelve mediocre pieces, then calls `--record-piece` 36 times and
`--record-set` once, each `--verdict PASS`, copying the Skill's own line. `record_piece` validates
the verdict's SPELLING against `PASS|FAIL|NA` and nothing else, then appends
`leg <name> · verdict <verdict>`; there is no execution anywhere in the function. The arm counts
`failed=0 unchecked=0` and returns MET. `check-playbook.sh`'s runnability oracle proved on this same
run that the declared legs COULD run — `[ -e "${tgt%% *}" ]` and `command -v` — and never invoked
one. Neither item is overridable, so neither leaves an override row for the owner to read.

**The armour points the wrong way.** `DOD_NO_OVERRIDE` holds `pieces-complete` on the stated ground
that "an override on it is the run certifying its own output" — which is precisely what a typed
verdict is. The honest bypass is banned and the dishonest one is the documented happy path:
`--verdict PASS` is the literal spelling in all six documented invocations, and `FAIL` and `NA`
appear in no example. Worse than the finding claims: `DOD_CORE` classifies this item `:machine`,
while unattended.sh:341-343 reserves `agent` for what is attested.

**Smallest fix — driver.** Have `--record-piece` / `--record-set` RESOLVE the named leg in the
playbook's `legs` map at the pinned BASE, run it through the `run_bounded` / `GATE_BOUND` machinery
the driver already owns, and write the EXIT STATUS as the verdict rather than accepting one from
argv; keep an explicit `--verdict NA` for a leg whose declared `coverage` mode is `dark`. Minimum
viable version: stamp the record with whether a leg was executed, so the arm can tell a run verdict
from a typed one. Independently, fix the Skill so at least one example spells `FAIL` — six identical
`PASS` templates is the instruction layer priming the answer.

**Gateable:** yes. Predicate: a piece record whose leg resolves in the playbook's `legs` map and
carries no execution stamp fails `pieces-complete`.

---

## F6 — The promotion check counts subjects instead of blockers, and accepts promotions retired to WONTDO

**Severity: medium.** Lenses B · C (B5, C4).

**Where:** `tools/unattended/check-unattended.sh:276-302` (the awk END block) ·
`tools/unattended/unattended.sh:3514` (the NON-CONVERGENT message) · `:1827` ·
`memory/guides/BUILD-METHOD.md:137` · `.claude/skills/unattended/SKILL.md:566-570`.

**Scenario.** The one clause that prices an abandoned review loop miscounts twice. The awk parses the
blocker count into `b`, uses it only for the shrink test, keeps `last[it] = b`, and then in END does
`if (it in needs) nneed++` — counting SUBJECTS. The rule it enforces is stated in BLOCKERS in both
carriers: "every blocker still standing is PROMOTED to a unit of this build, specced at its tier and
built. Not parked, not waived, not re-reviewed." So a subject exiting at four blockers is discharged
by promoting one, and `memory/builds/aPrimedKeepalive/RUN.md:37` is a live instance — two blockers
owed, one id demanded. Second, `newids` is derived from the id set of the units region at HEAD minus
BASE, and never inspects status, so three thin specs flipped to `WONTDO` satisfy the count and
`build-complete` sees no non-terminal row. The Skill's list of forbidden dispositions — "not parked,
not waived, not re-reviewed" — reads exhaustive and omits the cheapest one.

**Smallest fix — leg, inside the END block that already holds both values.** Make `newids` count
only ids that are non-WONTDO at HEAD (`unit_rows` already parses status out of the same region the
id extraction reads), and compare against `sum(last[it])` over exited subjects rather than against
their count. Carry the skeptic's caveat: one unit legitimately covering two closely related blockers
is not obviously forbidden by M4, so the blocker-sum arm should WARN where the id-status arm
REFUSES, or the message must say it is a lower bound. Add "not retired" to the Skill's list, so the
enumeration stops being a map of the one exit it leaves open.

**Gateable:** yes, it already is — this corrects an existing predicate rather than adding one.

---

## F7 — Twelve core directives have no observer, and declining one costs more than ignoring it

**Severity: medium.** Lenses A · B · D (A5, B4, D3).

**Where:** `tools/unattended/unattended.sh:446-448` (`DIRECTIVES_CORE`, sixteen handles) · `:343`
(`DOD_CORE`, ten items, none of them a handle) · `tools/unattended/check-unattended.sh:1289-1455`
(check 16 joins the registry to the Skill's TABLE) and `:1085-1094` (check 17 validates a waiver's
legality) · `memory/guides/BUILD-METHOD.md:166-177` (M6) and `:290-317` (M12).

**Scenario.** Sixteen MUST-by-default rules govern how the work is done. Four have a partial machine
observer — `land-once-done` via `build-complete`, `diff-reviewed` via F1's existence check, and the
two recipe handles via F5's typed verdicts. The other twelve have none at any checkpoint, and the
two checks that exist ask whether the REGISTRY matches the Skill's table and whether a waiver names a
legal handle — never whether a directive was FOLLOWED. The Skill states the asymmetry itself for one
handle and the logic covers all twelve: "Waiving it is SILENT: the bar stays green over a build that
skipped the reuse probes." But a waiver is `surfaced`-class and reaches the owner's wrap-up by M9,
while a silent skip reaches nothing. The run that declines honestly is charged; the run that ignores
is not.

**Two instances have sharper evidence than the general case.** (a) **M6's per-pass bug-class
checklist and diff-scoped gates.** `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` is
mandated per pass and re-mandated over the full range on every closing round — and `gotchas`,
`bug class` and `diff-scoped` all return ZERO hits across SKILL.md, UNATTENDED-PROTOCOL.md and both
kit templates. The Skill's "While it runs" walks nine verbs and never names the one per-pass quality
act on CODE. No verb writes it, no fact records it, no check reads it. In a kit that built a
hash-joined records layer with a closed verdict set for PROSE pieces, on the stated ground that "a
verdict that exists only in the transcript is a verdict the merge bar cannot read." (b) **The
prompt-scoped pair.** `researched` and `solution-tested` bind the path where the run CHOOSES the
mechanism, which is where a bad pick costs the whole build. M12 demands candidates plural and a
discriminating test written before it is run; the only artifact it names is spec §10 prose, graded
for heading presence alone. Replaying the phase walk over both `mode: prompt` records: neither
`aBoundedCeiling` nor `aPrimedKeepalive` ever entered RESEARCHING or TESTING, neither carries a
waiver row, both are LANDED.

**Smallest fix — driver, one DoD item over machinery that exists.** `directives-honoured`: each
in-scope core handle must be accounted for by either a waiver row (already written, already
validated by check 17) or an attestation row keyed on the handle — `--attest` and its
`grep -qE "^$item: (yes|true)"` fallback already take an arbitrary key. **Be honest about what this
buys:** a typed row, not evidence, exactly like F5's typed verdict. Its whole value is removing the
asymmetry — skipping stops being cheaper than declining, and an ignored directive becomes a MISSING
ROW rather than a silence. Do not try to machine-verify the unverifiable ones, and do not assert the
phase sequence (see REFUTED, A6).

**Gateable:** yes, weakly — the predicate is row presence, not compliance. That is the honest ceiling
of a non-derivable obligation, and it should be written into the item's own header the way §7's
"a gate's OWN header states what it does NOT check" requires.

---

## F8 — The run self-assigns the Tier that decides how much checking its own units receive

**Severity: medium.** Lens D (D5).

**Where:** `tools/memory-tree/check-memory-hygiene.sh:1247` (`if (hdr !~ /Tier-2/) next`, the
acceptance-evidence ledger) and `:1014` (`if (hdr ~ /Tier-1/) next`, the section canon and
empty-body arms) · `memory/TEMPLATE-SPEC.md:104-107`.

**Scenario.** The one check that asks whether a CLOSED unit's acceptance criteria were ever OBSERVED
filters itself out on a token the run writes in a header it authors. A run specs a unit `Tier-1` —
legitimately, from its own reading of charter §8's "mechanical/additive" test, which is a judgement
no gate makes — and that single token removes the unit from the acceptance ledger and from the
nine-section canon. Nothing in either kit joins the token to the paths the unit's passes actually
wrote, though `--dispatch` already records write sets and commit subjects already carry unit ids.
An unattended run is the one case where a mis-tiered unit is never contested, because contesting it
is what an owner reading the diff would have done. Corpus: 345 Tier-2 against 136 Tier-1 spec
headers, 71 of the Tier-1 ones CLOSED.

**Smallest fix — memory-tree layer, one clause at check-memory-hygiene.sh:1247.** Make the
acceptance ledger TIER-BLIND for a spec under a build folder carrying a tracked `RUN.md`: a unit
built under a mandate had no owner to contest its tier, so it does not get the light profile. The
population predicate is the unattended kit's own (`GIT ls-files "$M/builds/*/RUN*.md"`), and the
grandfather idiom is already declared as `ACCEPTANCE_LEDGER_CUTOFF`. No new declaration, no new fact,
one join.

**Gateable:** yes — this IS the gate, widened. Scope correction carried from the skeptic: the review
depth is NOT tier-gated under the build method (M4 audits every unreviewed spec, M8 covers the
cumulative diff whole), and the fork rule was already hoisted above the Tier-1 cut. What the token
actually buys is the acceptance ledger and the section canon, which is narrower than the raw finding
claimed and still worth closing.

---

## F9 — `--plan` computes a spec-quality grade and discards it the moment the unit is CLOSED

**Severity: medium.** Lens E (E5).

**Where:** `tools/unattended/unattended.sh:1589-1605` (`plan_state`) · `:1973-1974` (the discard) ·
`:1827` (`nonterminal_units`) · `tools/memory-tree/check-memory-hygiene.sh:1014`.

**Scenario.** `plan_state` grades a spec THIN when §2 Scope, §6 Acceptance criteria or §7 Gates is
empty — the kit's own predicate for "too thin to build against". `verb_plan` computes it and
overwrites it one line later: `case "$st" in CLOSED|WONTDO) state="DONE" ;;`. `build-complete` reads
only the status word. Hygiene's empty-body and canon arms are behind the Tier-1 cut, so a Tier-1
spec may omit §7 Gates entirely and carry an empty §6 with nothing red. The unit lands with no
stated acceptance criterion and no declared gate, meaning nothing at any layer ever asserted what
"done" was for it. Live specimen: `memory/builds/aPrunedCeremony/spec/2026-07-19-spec-PLAY-aPrunedCeremony-2.md`
is CLOSED · Tier-1 with sections 1,2,3,4,6,8,9 — no §7 at all.

**Smallest fix — driver, one term in `build-complete`:** run `plan_state` over each unit's spec
BEFORE the CLOSED override and refuse a CLOSED unit grading THIN. That is a call to a function
defined in the same file, over specs `unit_ids_of` already resolves. At `--plan`, print the grade
BESIDE `DONE` instead of replacing it, so the discard stops being silent.

**Gateable:** yes, with a date grandfather. Honest scale, carried from the skeptic: 2 of 307 CLOSED
tracked specs grade THIN today, both from a pre-kit July build. This is an unguarded shape, not an
epidemic — and F8's fix reaches most of the same ground from the memory-tree side.

---

## F10 — The Skill tells the closing agent one DoD item cannot be overridden; the driver holds two

**Severity: low.** Lens C (C5).

**Where:** `.claude/skills/unattended/SKILL.md:632-636` and `:657-661` ·
`tools/unattended/unattended.sh:364` and `:2718-2729` · `memory/guides/UNATTENDED-PROTOCOL.md:296-301`.

**Scenario.** The Skill says "One item has NO override, and this is where you will meet it —
`authorization-reachable`", then offers `--override <item> --reason` as the general remedy. The
driver's `DOD_NO_OVERRIDE` holds two, and the protocol carries the second. The rendered Skill is the
copy an agent reads and is the wrong one. Cost is smaller than the raw finding claimed: the refusal
at unattended.sh:2726 names both the rule and the correct exit (`--abort`), and supplies the second
item's own rationale, so the run loses one verb call rather than being left with certification as its
only visible route.

**Smallest fix — the SKILL TEMPLATE, not the render** (`tools/unattended/SKILL.template.md`, since
`adopt-unattended.sh` regenerates it): name both members, or render the list from `DOD_NO_OVERRIDE`
the way the directive table is already joined, and add the `--abort` route to the paragraph that
offers `--override`. **Machine half:** the leg already joins the Skill's directive table against
`DIRECTIVES_CORE` in both directions — extend that join to `DOD_NO_OVERRIDE` so this class of
divergence reds instead of shipping.

**Gateable:** yes, by the extended two-way join.

---

## F11 — M8's "round N-1's RECORDED TIP" has no carrier

**Severity: low.** Lens C (C6).

**Where:** `memory/guides/BUILD-METHOD.md:218-228` · `tools/workflows/tier2-review.js:75,163-172,516` ·
`tools/unattended/unattended.sh:3510`.

**Scenario.** M8 binds round N>1 to round N-1's recorded tip so it reads the FOLD rather than
re-reading fixes, and the harness hard-refuses a non-sha base at round > 1. But the method's own
copy-paste block writes `head: 'HEAD'`, the harness defaults the same, and the record line it
instructs writes that literal string into the report: 47 tracked review records carry a range ending
in `HEAD` against 11 carrying a sha-to-sha range. The driver records no tip either. So a regrounded
run can satisfy the obligation only by luck. Consequence corrected from the raw finding: round 2 is
handed the prior confirmed set with an explicit "judge the FIX, do not re-raise" brief, and falling
back to the pinned BASE gives a WIDER scope, so what is lost is review focus and tokens, not
coverage.

**Smallest fix — one token in the method** (`head: '<sha: the tip this round reviewed>'`), plus an
optional `--tip <sha>` appended to the reason string `verb_review` already writes, so M7's
regrounding read answers round N's base without recollection.

**Gateable:** not usefully. A predicate demanding a sha-to-sha range would red 47 standing records
and buys little; this is an instruction-layer fix.

---

## F12 — `units-at-landing` and `unpushed-at-landing` are written with a stated rationale and read by nothing

**Severity: low.** Lens E (E6).

**Where:** `tools/unattended/unattended.sh:2238` and `:2254-2256` · `tools/unattended/check-unattended.sh`
(zero matches for either key).

**Scenario.** `--landed` freezes the landed roster into an authored fact whose comment names the
question it answers: "a FINISHED record must still answer 'which units did this run actually cover'
… nothing else in the tree holds it once the README moves on." No leg check, no DoD item and no verb
ever opens it, across 21 landed records. The purest form of this review's lens — evidence written for
a purpose, with no consumer.

**No unit proposed, and here is why.** The refusal it implies is already made: `check_authorization`
computes `comm -23` over BASE and HEAD id sets and fails 20 on any id present at BASE and absent now,
on an item in `DOD_NO_OVERRIDE`. And because the frozen roster includes WONTDO rows, the proposed
join would not see F4's drop either. What is genuinely missing is post-hoc FORENSICS, not a refusal.
Cheapest honest response: have `--status` print the pair so a resumed run sees it.

---

## UNVERIFIED

None. Every one of the 30 findings carried a skeptic verdict.

---

## REFUTED

Do not re-find these.

- **A1 — anchor `## Verdict: BLOCKED` on the record `closing-review-recorded` selects.** The token
  grades a ROUND'S FINDING, not the run's disposition of it; records are never rewritten after the
  fold. 62 of 77 post-cutoff records read BLOCKED, including the FINAL record of runs that landed
  correctly (`memory/builds/aLexedStripper/…-round2.md`). Anchoring it — last-record-not-BLOCKED
  included — reds honest landings and separates nothing. The disposition evidence is the convergence
  row set, which is F1.
- **A6 — assert `RESEARCHING` and `TESTING` in the committed phase history.** The protocol calls
  those POSITIONS a prompt-started run occupies, a description and not an obligation to record, so
  the check would invent a duty the contract declines to state. Phase moves are staged, not
  committed, so a run that commits once degrades the check to its own skip — evadable by ordinary
  batching — and a run that wants to fake it writes two phase claims with a witness sha, which is a
  typed claim exactly like F5's. Residual value duplicates F7. What survives, and is folded into
  F7: `verb_phase` enforces no ordering, so the phase sequence is not evidence of anything and must
  not be read as such.
- **D6 — a `gates-green` override plus a local landing anchor composes into a permanent unchecked
  LANDED.** A local anchor means the work is UNPUSHED (the record says `unpushed-at-landing: 44`),
  and `.githooks/pre-push` still runs the bar on the pushed tip and blocks a red push, forcing a FULL
  run when no recorded green covers it. `gates-green` is a deliberately overridable item and an
  override row is surfaced-class, so it reaches the owner's one turn by design — demonstrably, since
  `aPrimedKeepalive` carries an owner-side correction row re-measuring that override's premises. What
  survives is bookkeeping (no predicate names the state), which the brief rules out of scope.

**Corrections carried forward, so the next reviewer does not re-derive them:**

- A5's "zero of sixteen directives are observed" is wrong; four have partial observers, twelve do
  not. F7 states the corrected set.
- E4's "blockers standing never reach the owner" is wrong: BUILD-METHOD.md:257 sources the
  "problems resolved" wrap-up row from each review record's `## Verdict` line and its blockers. Only
  the SCOPE-AMENDMENT half survives, in F4.
- B6's cited live instance (`aBoundedCeiling`'s three WONTDO units) is not an instance: that build is
  `mode: prompt`, its first run-state commit already reads RUNNING with an empty units region, so
  `baseline_units` returns "empty baseline" and check 24 skips the file entirely. The units were also
  authored by the run itself. F4's SPECCING drop has no live instance in this corpus.
- B5's proposed `nneed += last[it]` is not unconditionally correct — M4 does not obviously forbid one
  unit covering two related blockers. F6 downgrades that arm to a warning.
- E6's proposed roster join is already made by `check_authorization` and would not see F4's drop.
- The `46 records` measurement quoted at unattended.sh:3143 is four times out of date (208 tracked,
  170 with a verdict heading). It is the stated reason the arm grades existence, and it must be
  re-measured in whatever commit touches that arm.

---

## PROPOSED UNIT SET

One mechanism per unit. Tier 1 = mechanical/additive; Tier 2 = a new write path, a new gate, or a
contract change.

### U1 — `closing-review-recorded` requires the loop to have ENDED
- **Goal:** the item stops meaning "a markdown file exists" and starts meaning "a review loop ran and
  reached a terminal state".
- **Layer:** driver, `dod_met`'s existing arm, calling `review_counts` which already parses the
  grammar. Re-measures the stale justification comment in the same commit.
- **Acceptance observable:** a run-state file whose LAST `review` row for the build slug carries a
  non-zero blocker count and no terminal token fails `--close`; a `CONVERGED` exit at non-zero
  blockers fails. Replayed over the tracked corpus it reds `aBoundedCeiling`, `aPrimedKeepalive` and
  `aThawedCorpus`, and none of the nine honest records.
- **Tier 2.** Closes F1.

### U2 — Leg clause for an abandoned review loop
- **Goal:** the ratchet half of U1, reaching records the driver did not write.
- **Layer:** gate leg, `check-unattended.sh` check 2's awk, phase-gated to LANDING/LANDED (the loop
  at :248 has no phase filter, unlike check 24, so an ungated clause would red every live run
  sitting between two rounds).
- **Acceptance observable:** `last[it] > 0 && !(it in term)` on a terminal record is a named refusal;
  staging that shape into a fixture reds the leg.
- **Tier 2.** Closes F1's ratchet half.

### U3 — The promotion clause counts blockers and rejects retired promotions
- **Goal:** NON-CONVERGENT stops being dischargeable by promoting one unit of four, or by promoting
  units straight to WONTDO.
- **Layer:** gate leg, the same awk END block, over `last[it]` and the status field `unit_rows`
  already parses.
- **Acceptance observable:** a record exiting at 4 blockers whose region gained 1 non-WONTDO id
  fails; a record whose promoted ids are all WONTDO at HEAD fails.
- **Tier 2.** Closes F6.

### U4 — `gates-green` escalates on the diff
- **Goal:** a run that edits a checker is graded by that checker's own self-test.
- **Layer:** driver, the `gates-green` arm, over the pinned `base` fact and the `guard` arrays in
  `tools/gate-legs.json`; adds the kit's shipped `run-unattended-gates.sh` when the diff touches
  `tools/unattended/`.
- **Acceptance observable:** a BASE..HEAD touching `tools/check-microformats.sh` runs with
  `GATE_SELFTESTS=1` and says so; a diff touching no held guard runs the plain bar and ANNOUNCES the
  skip rather than passing silently.
- **Tier 2.** Closes F2.

### U5 — `specs-audited` DoD item
- **Goal:** a CLOSED unit no spec-audit record ever named blocks the close.
- **Layer:** driver, one new machine item (`CORE_FLOOR` `12:10` → `12:11`), reading the join
  `gen_build_index.py` already renders. Overridable, unlike `authorization-reachable`.
- **Acceptance observable:** replayed against `memory/builds/dUnstalledConvoy`, ten CLOSED units red;
  a build whose gap line reads "none" passes.
- **Tier 2.** Closes F3.

### U6 — Check 24's retire arm is keyed to the pinned BASE
- **Goal:** a retirement performed during SPECCING owes the same row as one performed during BUILDING.
- **Layer:** gate leg, `check-unattended.sh` check 24; `rb` is already in scope in that loop. The ADD
  arm keeps its BUILDING baseline and its stated rationale.
- **Acceptance observable:** a unit not WONTDO at the pinned BASE, WONTDO at HEAD, with no
  `retire`/`supersede` row, reds — including when the flip happened before the first BUILDING commit.
- **Tier 2.** Closes F4's baseline lever.

### U7 — Retirement becomes a surfaced parked row
- **Goal:** dropping declared scope reaches the owner's one turn.
- **Layer:** driver, `PARK_KINDS_OWED` split by kind AND act (`retire`/`supersede` surfaced, `add`
  history), plus M9's wrap-up gaining a scope-amendments row and PROTOCOL:182's five-kind
  enumeration corrected to eight.
- **Acceptance observable:** a record with a `retire` row whose attested surfaced count excludes it
  fails `parked-decisions-surfaced`; `--status` prints it as `parked`, not `noted`.
- **Tier 2.** Closes F4's routing lever.

### U8 — `--record-piece` executes the leg it names
- **Goal:** a piece verdict is an exit status, not a string from argv.
- **Layer:** driver, `record_piece`/`record_set`, resolving the playbook's `legs` map at the pinned
  BASE through the existing `run_bounded` / `GATE_BOUND` machinery; `NA` stays legal only for a
  `dark` coverage mode.
- **Acceptance observable:** a record written for a resolvable leg carries an execution stamp, and
  `pieces-complete` refuses a record without one; a deliberately failing declared leg produces
  `verdict FAIL` without the run choosing it.
- **Tier 2.** Closes F5.

### U9 — `directives-honoured` DoD item
- **Goal:** ignoring a directive costs the same as declining one — a missing row instead of silence.
- **Layer:** driver, one new item over `--attest` rows and the waiver rows check 17 already
  validates. Its header states plainly that it grades ROW PRESENCE and not compliance.
- **Acceptance observable:** a run with neither a waiver nor an attestation for an in-scope core
  handle (`reuse-first`, `specs-reviewed`, `researched`, …) fails `--close`.
- **Tier 2.** Closes F7.

### U10 — Agent-facing carrier corrections, one render
- **Goal:** the documents a run actually reads stop being wrong or silent on four obligations.
- **Layer:** documents — `tools/unattended/SKILL.template.md` and `PROTOCOL.template.md` (re-rendered
  by `adopt-unattended.sh`), plus `memory/guides/BUILD-METHOD.md`. Content: both members of
  `DOD_NO_OVERRIDE` and the `--abort` route (F10); the M6 bug-class command and the per-pass
  diff-scoped gates named in "While it runs" (F7); the kit-edit compensating-runner obligation from
  `kit.toml` (F2); the `gates-green` protocol cell stating what the bar actually covers (F2);
  `head: '<sha>'` in M8's snippet (F11).
- **Acceptance observable:** the leg's existing Skill-table two-way join, extended to
  `DOD_NO_OVERRIDE`, reds on divergence; `grep -c gotchas` over both rendered carriers is non-zero.
- **Tier 1** for the prose; the join extension rides with it as the one mechanical guard that stops
  this class recurring.

### U11 — The light profile is unavailable to a unit built under a mandate
- **Goal:** a run cannot exempt its own units from the acceptance-evidence ledger by writing `Tier-1`.
- **Layer:** memory-tree, `check-memory-hygiene.sh` check 23's tier filter, population-gated on a
  build folder carrying a tracked `RUN.md`, grandfathered by the declared `ACCEPTANCE_LEDGER_CUTOFF`.
- **Acceptance observable:** a CLOSED Tier-1 spec under a mandated build whose §6 criteria are joined
  to no observation reds; the same spec under a hand-built build stays green.
- **Tier 2.** Closes F8, and reaches most of F9. The residual F9 case — §7 Gates absent entirely —
  would be a `plan_state` term in `build-complete`, deliberately NOT proposed as a unit here on a
  live class of 2 of 307, both pre-kit.

---

**Not proposed:** F12 (the missing reader is forensics, and the refusal it implies already exists at
`check_authorization`), F11's gate (a sha-range predicate would red 47 standing records for little),
and anything downstream of the three REFUTED findings.
