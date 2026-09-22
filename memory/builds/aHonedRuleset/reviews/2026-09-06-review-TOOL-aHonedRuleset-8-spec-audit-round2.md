**Serves:** spec-audit TOOL-aHonedRuleset-8

# aHonedRuleset — spec audit of unit 8, round 2

*Node `a`, 2026-09-06. Four finder lenses read the rev-6 text of the unit-8 spec, five skeptic
batches were run to REFUTE each candidate, and this is the consolidation. Round 1 graded rev-5 and
returned BLOCKED with two blockers; all fourteen of its findings were folded at rev-6, and the rev-6
log line in §9 was read first as the map of what moved. Every surviving claim about source was re-run
against the tree before it was kept — the runbook, the govkit engine, `refusal_join.py`,
`check_runbook_parity.py`, `matrix.py` and the sibling spec were read at source, never through the
spec's description of them. This round grades the SPEC, not the tree; nothing here is a finding about
the deployer's own behaviour except where the spec asserts that behaviour and the assertion is false.*

Subject, pinned at the blob it was read at:

- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-8.md@5430a5ef7a028cb95ae70372bf17cf71c89f8b15`

**ROUND: 2.**

## Verdict: BLOCKED

One blocker. It is round 1's B1 surviving its own fold, one layer further down. rev-6 answered B1 by
reasoning carefully about what `govkit apply` does on the runbook path and adding a WIRING step to
S3 — but the runbook's fresh path never invokes `apply` or `update` at all. Measured: `grep -n apply
WIRE-INTO-PROJECT.md` returns eight hits and every one is prose; the sole fresh-path command is
`intake` at `:82`, and `cmd_intake` writes `.governance/deploy.toml` and returns without copying a
byte. So §4's whole rev-6 chain — "`apply` takes the ordered-not-emitted branch … the payload lands
and no leg runs" — describes a run the runbook does not ask anyone to make, S3's new wiring step
tells an operator to wire an engine that was never copied into their tree, AC17's two admissible
outcomes are both unobservable from "the runbook's own command", and `memory/backlog/TOOL.md:6`
carries the same false premise outward in capitals.

Five HIGH findings follow, then four MEDIUM and two LOW. The dominant class is the one round 1 named
and rev-6 claimed to have fixed: **an amendment that leaves its other half standing.** Six of the
twelve entries below are rev-6 edits that were never carried into the carriers that describe them —
S6 added a seventh edited file while six separate counts still read six; S3 grew to three edits while
§4's table, §8 F4's byte price and §6's AC9 all still describe two; and three documents point at a §3
bullet the fold never wrote. The fold repaired the instances round 1 listed and reproduced the class.

The blocker is a spec edit, not a fork re-opening. So are all eleven other entries. The unit is
buildable the moment B1 and the HIGH set land.

---

## Review shape

- Raw findings: **33**. Confirmed: **22**. Refuted: **11**. Unverified: **0**. Precision: **0.67**
  (up from round 1's 0.56 over the same lens set and the same skeptic protocol).
- Round 1 for comparison: BLOCKED, 2 blockers / 5 HIGH / 6 MEDIUM / 1 LOW, precision 0.56.
- The 22 confirmed findings consolidate into the **12 entries** below. The pipeline's dedup reported
  zero duplicates because none were byte-identical, but four clusters are the same defect seen
  through different lenses; each entry names the raw ids it carries, so nothing is lost and nothing
  is counted twice. Adjudicated severity is MINE and is stated per entry; where it differs from the
  raw grade, the entry says why.

### Run integrity

- lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory verdict(s)
  demoted to unverified, 0 spurious verdict(s) discarded, 0 duplicate(s).

Every integrity count is zero, so this run is **complete**: the finding set is not truncated by a
dead lens or a lost skeptic batch, and a zero count in it is evidence, not silence. The one place
this report reports an absence as a finding — S6 having no acceptance criterion — was verified by
reading §6 in full at the pinned blob, not inferred from a lens returning nothing.

---

## Findings

| # | Sev | Address | Defect | Raw ids |
|---|---|---|---|---|
| B1 | BLOCKER | §4 *What the runbook path actually yields*, §2 S3 third edit, §6 AC17 | The runbook's fresh path never runs `apply`; the whole rev-6 B1 fold reasons about a run that does not happen | 18 |
| H1 | HIGH | §4 Files touched + Rollout, §3 `last-audit`, §5 security + rollback, §8 F3, §10 | S6 edits a SEVENTH file that appears in no table row while six counts still read six | 3, 9, 19, 25 |
| H2 | HIGH | §3 (absent bullet), cited from §4:188, §9 rev-6, `memory/backlog/TOOL.md:6` | Three documents point at a §3 gate-runner boundary that was never written | 8, 21 |
| H3 | HIGH | §2 S3, *Third, the WIRING step* | "exactly as the sibling sections name theirs" is false at all six cited lines, and following it reds AC6 | 10, 27 |
| H4 | HIGH | §6 AC9, against §2 S3 | AC9 still counts the rev-5 two-edit S3, so B1's entire remedy has no criterion that can fail | 1 |
| H5 | HIGH | §2 S6, §5 testing, §7 `govkit refusal join` | `DEPL-aHoistedPass-1` already claims the same `244 → 246` for a different pair of branches in the same file | 24 |
| M1 | MEDIUM | §2 S6, first sentence, with §7's refusal-join bullet | S6 states the ledger convention as its prose half only and cites neither the precedent nor the standing disposition | 11, 20, 28 |
| M2 | MEDIUM | §6 (no criterion for S6) | S6 is the only scope item with no acceptance criterion, and no gate can see it either | 12, 22, 29 |
| M3 | MEDIUM | §6 AC11, renderer-list clause | AC11 grades the one wrong placement rev-6 found, not the class S3's rule forbids | 5 |
| M4 | MEDIUM | §8 F4 byte bullet, §4 Files-touched row for the runbook | The owner ruling on S3's bytes was given roughly half of S3's bytes | 13, 30 |
| L1 | LOW | §8 F4, *The option TAKEN* (:943) | Points at "S2's own placement paragraph"; the placement rule is S3's | 15 |
| L2 | LOW | §8 F1, Correction 1 | `matrix.py:66` is blank; the cited pin is at `:63` | 16 |

---

## B1 — BLOCKER. The runbook path the whole rev-6 fold reasons about is a path the runbook never asks anyone to run

**Address:** §4, *What the runbook path actually yields, and why S3 needs a third edit*; with §2 S3's
third edit and §6 AC17. Raw id 18.

rev-6 closed round 1's B1 by tracing what `govkit apply` does when a target's `deploy.toml` names an
entry whose leg is ordered rather than emitted, and by adding a WIRING step to S3 on the strength of
that trace. The trace is correct about `apply`. It is wrong that the runbook's fresh path runs it.

Measured at source:

- `grep -n apply WIRE-INTO-PROJECT.md` returns `:309`, `:373`, `:589`, `:635`, `:638`, `:876`, `:878`,
  `:883` — every one prose. There is no `govkit.py apply` command block anywhere in the runbook.
- §2's install is exactly `:81-85`: one `intake --kits …` plus two `adopt-playbook.sh` calls.
- `cmd_intake` writes `.governance/deploy.toml` and returns (`tools/govkit/govkit.py:8225-8229`). It
  copies nothing and emits no leg. `adopt-playbook.sh` contains no `cp` at all, which §4's own
  *Alternatives rejected* bullet already records ("renders the charter region and copies nothing
  else"). Every per-kit section installs by hand with `cp -r` (`:153`, `:309`, `:373`).
- The strings §4 reasons about — `gate legs: ORDERED, not emitted` — live at `govkit.py:5066` and
  `:5104` inside `_cmd_apply`. Only §5b at `:589` asserts `apply` is the fresh path, and no numbered
  section runs it.

Three consequences the fold did not price. First, S3's new WIRING step instructs an operator to wire
`check-microformats` into a gate runner when the engine was never copied into their tree — strictly
worse than ordered-not-emitted, and the exact class the deployer names at `govkit.py:5083-5086` ("a
leg whose engine gov never ships … a human then does the work"). Second, AC17 says "installed with
the runbook's own command" and then admits only the two outcomes an `apply` run can produce; since
`intake` neither emits nor orders anything, the criterion silently grades a command the builder has
to invent. Third, the backlog row at `memory/backlog/TOOL.md:6` carries the premise outside this spec
in capitals — "THE PAYLOAD LANDS AND NO LEG RUNS" — where a future reader will take it as measured.

**Fix.** Add the measured fact to §4: the runbook's fresh path contains no `apply`/`update`
invocation, so the §2 outcome today is a `deploy.toml` naming the entry with no engine in the tree.
Then either bring the missing install step into S3's scope, or record it as a second explicit
boundary beside `TOOL-aHonedRuleset-15` and correct that backlog row. Restate AC17 to name the exact
command sequence the scratch install runs (`intake` then `apply`), and add a THIRD admissible
outcome — payload absent — so the criterion can report what the runbook actually yields rather than
only the two an `apply` run can produce.

**Left-shift gate.** A `runbook install-path` leg: parse `WIRE-INTO-PROJECT.md`'s fenced command
blocks, collect the `govkit.py` subcommands they actually invoke, and red when the runbook's prose
asserts a verb (`apply`, `update`) that no fenced block in the fresh path runs. This is the "a value
stated in prose beside the source that owns it rots" rule applied to a runbook, and it is a dozen
lines against a document that already carries machine-readable anchors. It is also the only leg in
this report that would have caught the blocker in BOTH rounds.

---

## H1 — HIGH. S6 edits a seventh file that no table row names, and six counts still read six

**Address:** §4 *Files touched (estimate)* and *Rollout*; §3's `last-audit` bullet; §5's security and
migration/rollback bullets; §8 F3; §10. Raw ids 3, 9, 19, 25 (three lenses graded HIGH, one MEDIUM;
adjudicated HIGH — the table is the builder's checklist and a scope item with no row does not land).

S6, new at rev-6, requires a ledger comment in `tools/govkit/refusal_join.py` (its ledger is that
file's `:42-118`, `BRANCH_PIN` at `:41`). That is a seventh edited file. Verified by direct count:
§4's Files-touched table has exactly six rows — `registry.toml`, `check-microformats.kit.toml`,
`WIRE-INTO-PROJECT.md`, `govkit.py`, `check-line-length.kit.toml`, `selftest.py` — and none of them
is that file. Every dependent count is stale in step:

- `:333` Rollout — "Six files, one atom."
- `:346` — "Three files at rev-2, six at rev-3."
- `:103` §3 — "none of this unit's SIX files is on it."
- `:392` §5 security — "re-priced at rev-6 against §4's SIX files."
- `:438` §5 migration/rollback — "`git revert` of one commit restores all six files."
- `:848-849` §8 F3 — refuses the fenced-charter option partly for "adding a seventh file to a unit
  that already grew from three to six", which now describes the unit's own state.

The harm is concrete: a builder working the table never opens `refusal_join.py`, so S6 silently does
not land — and since S6 also has no acceptance criterion (M2) and no gate can see it (the pin is
shrink-only), it is invisible twice over. The revert claim understates what one `git revert` touches.
§3's `last-audit` non-goal states a verification it performed over six paths and asserts it over
seven; the CONCLUSION survives — `refusal_join.py` is absent from the `watch:` list at
`memory/guides/SESSION-KICKOFF.md:6`, confirmed — but the criterion as written does not reach the
seventh path.

**Fix.** Add the row `tools/govkit/refusal_join.py | S6 — a ledger comment naming the two new
branches`; change six to seven at `:333`, `:346`, `:103`, `:392` and `:438`; re-state §3's watch-list
bullet as verified over the seven-file set; and drop or re-word F3's "seventh file" clause so it
stops arguing against a cost the unit already carries.

**Left-shift gate.** A memory-tree hygiene check over SPECCED specs: every filesystem path named in a
§2 scope item must appear as a row in §4's Files-touched table, and the table's row count must equal
every spelled-out number in the document that claims to be that count. Both halves are grep-shaped —
the paths are already in backticks, and the number words are a closed set. This same leg catches M4's
half of the S3 pricing drift, which is why it is the highest-value gate in this report after B1's.

---

## H2 — HIGH. Three documents point at a §3 boundary bullet that was never written

**Address:** §3 (the absent bullet), cited from §4:188, §9's rev-6 entry at `:1062`, and
`memory/backlog/TOOL.md:6`. Raw ids 8, 21.

Read in full, §3 spans `:78-110` and holds exactly seven bullets: no charter byte moves; the charter
does not name the gate; no selection-expanding machinery; the two guards assert rather than expand;
the other four conditional entries keep their classification; no `last-audit` re-stamp; and
`TOOL-aScouredKit-23`/`TOOL-dSpentCeiling-4` cited not answered. None mentions a gate runner and none
mentions `TOOL-aHonedRuleset-15`. `grep -n 'aHonedRuleset-15'` hits only `:188`, `:387` and `:1062`.

Yet §4:188 reads "it is filed as `TOOL-aHonedRuleset-15` rather than fixed here. §3 records the
boundary"; §9's rev-6 line reads "§3 records that fixing the runbook's missing gate RUNNER is out";
and the backlog row that hands the follow-up to its owner says the unit "recorded the boundary in its
§3". The only record is a §4 *Alternatives rejected* bullet at `:383-388`.

§3 is the section a builder reads to learn what is OUT and a closing reviewer reads to grade scope
creep. A closing diff that quietly wired `run-gates` into the runbook would contradict no §3 line.
And one copy of the false pointer lives outside this spec entirely, in the backlog, where the owner
who follows it finds nothing.

**Fix.** Add the §3 bullet — the runbook's missing gate RUNNER is out of scope; `run-gates` is absent
from the runbook's `--kits` example for every kit it lists; measured here, filed as
`TOOL-aHonedRuleset-15`; AC17 observes which outcome an install produces. Alternatively, if §4's
Alternatives entry is meant to be the sole carrier, repoint §4:188, §9's rev-6 line and
`memory/backlog/TOOL.md:6` at §4.

**Left-shift gate.** A hygiene check on backlog-row provenance: when a backlog row says a unit
"recorded … in its §N", assert that the named spec's section N mentions the row's own id. The rows
and the specs are both in the memory tree, the id format is fixed, and the section headings are
numbered — this is a few lines of Python in the existing hygiene gate, and it catches the one copy of
this defect that escapes the spec.

---

## H3 — HIGH. S3 reconciles its new wiring step with the carried-prefix ban by a claim of sibling parity that is false at every line it cites

**Address:** §2 S3, *Third, the WIRING step*, against §4's carried-prefix constraint and §6 AC6. Raw
ids 10, 27.

S3 says the wiring instruction "keeps S3's entry-id-and-no-file-path discipline: it names the leg by
the id an operator already typed, exactly as the sibling sections name theirs." Read at the six lines
S3 itself cites, not one sibling names its leg by a govkit entry id:

- `:178` — `bash tools/memory-tree/check-memory-hygiene.sh`
- `:262` — `python tools/drift-audit/selftest.py`, plus two more `tools/drift-audit/*` commands
- `:402` — `python3 tools/memory-recall/selftest.py` in a fenced block
- `:525` — `bash tools/check-wiring.test.sh`
- `:351` and `:786` — `<GATE_FILE>` / `<kit>/` tokens

Four spell literal `tools/` paths and zero spell an entry id. The two halves of S3's sentence cannot
both be satisfied. A builder who follows "exactly as the sibling sections name theirs" writes `bash
tools/check-microformats.sh`, which the epoch-2 predicate counts as a loose file directly under
`tools/` that exists in the tree, raising `WIRE-INTO-PROJECT.md` from 47 to 48 in
`tools/install-prefix-carried.txt` — the `ROSE` verdict `--write-ratchet` cannot absorb, and a
straight AC6 failure, which is the exact outcome §4 spends a section preventing. A builder who
follows "no file path" ships the one wiring instruction in the document that withholds its command.

The binding half of the sentence is correct, so a careful builder is safe. But the false clause is
the ground on which the new step is reconciled with the ban and sold as reuse of an established
pattern — the same wrong-facts-under-a-right-answer class the rev-6 M5 fold corrected two bullets
away in this very section.

**Fix.** Drop the false equivalence and name the one path-free form available: instruct the operator
to add the leg by its `tools/gate-legs.json` leg NAME (`micro-format definitions`), or in the
`{prefix}`-token form the descriptor's own argv uses — and state explicitly that S3 DIVERGES from the
siblings' literal-path style because the carried-prefix ban forbids that style in this document.

**Left-shift gate.** No gate reaches a spec's claim about sibling prose, so this one left-shifts into
the §10 checklist: **a spec sentence asserting parity with existing text ("exactly as X does", "the
way the siblings do") must quote one of the cited lines verbatim, or it is not a verified claim.**
Round 1 confirmed the same shape (M5) and round 2 found it again in the same paragraph, which is what
promotes it from an instance to a checklist row.

---

## H4 — HIGH. AC9 still grades the rev-5 two-edit S3, so the blocker fix has no criterion that can fail

**Address:** §6 AC9, against §2 S3's third edit. Raw id 1.

AC9 reads: `grep -c 'check-microformats' WIRE-INTO-PROJECT.md` returns **at least 3** against the 0
measured at base — "the `--kits` id, the anchor and the sentence". That enumeration is the rev-5
two-edit S3, verbatim. §2 now specifies THREE edits, the third of which is B1's entire remedy.

So a build that lands the anchor plus its one sentence and omits the wiring instruction returns 3 and
passes. AC11 needs only a non-empty body, the census at 8, and no `runbook-parity:` line naming the
entry — all satisfied. AC17 admits the ordered-not-emitted outcome explicitly. Nothing else in §6
counts runbook hits. The unit's own blocker fix is therefore unobserved, and the adopter is left in
exactly the state B1 identified. Confirmed live that nothing in the install path compensates:
`run-gates` is the sole `gate_runner_seed` declarer (`tools/run-gates/kit.toml:105`, read at
`govkit.py:8171-8172`).

**Fix.** Raise AC9's threshold to at least 4 and add the wiring mention to its enumeration. Better:
add a criterion that greps the anchor's DERIVED body — anchor line to the `memory-tree` anchor — for
the leg-wiring instruction naming both the local gate runner and CI, the way the sibling sections at
`:178`, `:262`, `:351`, `:402` and `:525` name theirs.

**Left-shift gate.** Same leg as M2's: **every `S<n>` in §2 must be named by at least one criterion in
§6.** That alone does not catch H4, since S3 is named by four ACs. The half that does catch it is the
charter's own §7 rule applied to acceptance criteria — *no count of a derived population is written
in prose*: an AC whose threshold is a typed integer over an artifact the spec itself enumerates
should state the count as derived from the scope item, so growing the scope item moves the threshold.
Add that as a §10 checklist row: **when a scope item's edit count changes, every AC that counts its
artifacts is re-derived, not carried.**

---

## H5 — HIGH. A specced sibling already claims the same `244 → 246` for a different pair of branches in the same file

**Address:** §2 S6, §5's testing bullet, §7's `govkit refusal join` bullet. Raw id 24.

Verified in both directions. `memory/builds/aHoistedPass/spec/2026-09-04-spec-DEPL-aHoistedPass-1.md`
is SPECCED, `streams deployer`, and:

- its §3:47 lists "Moving `BRANCH_PIN` or `FILE_PIN` in `tools/govkit/refusal_join.py`" as a non-goal;
- its `:179-184` gives the reason — a `217 → 219` move "would write a ledger entry claiming two new
  branches took the pin to the population, when the population is 246" — and files re-baselining as
  its own backlog row;
- its AC9 at `:262-263` reads "a branch count exactly two higher than the 244 measured at this base,
  with `BRANCH_PIN` unmoved at 217" — for ITS OWN two new refusal branches, not S4/S5's.

Live now: `python tools/govkit/refusal_join.py` prints `244 branch(es) across 4 module(s)`, exit 0;
`BRANCH_PIN = 217` at `:41`.

Two SPECCED units in the same `deployer` stream each claim `244 → 246` for a different pair of
branches in the same file. Whichever lands second lands with a false figure in its own spec and a
ledger comment that is wrong on the day it is written. Aggravating: this spec cites
`DEPL-aHoistedPass-1` six times, including its §3 at `:40-41` — seven lines above the `BRANCH_PIN`
non-goal it missed — and re-derives a disposition already on record, which is the recall-failure
class the rev-6 H4 fold corrected for `TOOL-dScaffoldedMirror-15`.

**Fix.** S6 cites `DEPL-aHoistedPass-1` §3 and `:179-184` as the standing disposition it follows, and
states the count as a DELTA (+2 over the population measured at this unit's landing) rather than the
absolute 246, with one sentence saying the absolute depends on which of the two units lands first.
§5's testing bullet and §7's refusal-join bullet take the same wording.

**Left-shift gate.** A drift-audit probe: for every SPECCED spec in the memory tree, re-resolve any
stated absolute count over a live-measured population in `tools/govkit/refusal_join.py` (the figures
are already spelled as `NNN branch(es)`) and red when a SPECCED spec's figure no longer matches the
live value plus its own declared delta. Cheap, stdlib, and it fires the moment either unit lands.
The broader rule it enforces is already charter law: state the delta, derive the absolute.

---

## M1 — MEDIUM. S6 states the ledger convention as its prose half only, and cites neither the precedent nor the standing disposition

**Address:** §2 S6, first sentence, with §7's `govkit refusal join` bullet. Raw ids 11, 20, 28 (one
lens graded HIGH; **adjudicated MEDIUM**, and the downgrade is deliberate — see below).

S6 states the convention as "every unit adding refusal branches names them and states armed or
unarmed". Verified in the file: every ledger row at `refusal_join.py:42-118` is an `X -> Y` PIN
RAISE — 216→217, 215→216, 214→215, 212→214, 210→212, 208→210, 197→208, 190→197, 185→190, 180→185,
161→180, 141→161, 135→141. The `141 -> 161` row (`TOOL-dUnstalledConvoy-26`) records a trailing floor
as "the state this file's own convention forbids: a floor that trails the population stops catching
the matcher going blind", and raises to the live count for that reason. S6 writes the first row in
the file's history that names branches without moving the pin, while the pin is 27 behind and S6's
own arms take the population to 246.

The three raw lenses all prescribed raising the pin. **I do not carry that prescription**, and this
is where the severity drops: H5's sibling ruling supplies a legitimate reason to decline the raise —
a `217 → 219` move would assert a relationship that does not hold on a base already 27 stale, and
re-baselining is its own act with its own reason, filed as its own row. S6's DECISION is defensible.
What is defective is that S6 states half a convention as the whole of it, invokes that file's
authority for the half it keeps, and cites neither the `141 -> 161` precedent nor the sibling that
already re-decided the question. A future reader greps S6 and learns the convention is note-only,
which quietly retires the raise the file's doctrine depends on. §7's "S6 is the written record that a
shrink-only floor structurally cannot be" is true and is not the same as engaging the precedent.

**Fix.** S6 states the convention completely — name the branches, state armed/unarmed, AND raise the
pin — cites the `141 -> 161` row and `TOOL-dUnstalledConvoy-26` as the precedent for the raise, then
says explicitly that this unit declines the raise on `DEPL-aHoistedPass-1`'s recorded reason. §7's
bullet takes the same correction, so the trailing floor reads as a known deferral with an owner
rather than as an acceptable property.

**Left-shift gate.** The pin ledger's own header is the natural home: state in `refusal_join.py:39-41`
that a unit which adds branches without raising the pin must name the row or spec that defers the
raise. Then a one-line check in the `govkit refusal join` leg — when the live population exceeds
`BRANCH_PIN` by more than a declared slack, print a NAMED deferral line or red. That converts a
silent 27-behind floor into a signal, which is the charter's liveness rule applied to a pin.

---

## M2 — MEDIUM. S6 is the only scope item with no acceptance criterion, and no gate can see it either

**Address:** §6, the AC list. Raw ids 12, 22, 29.

Verified by reading §6 in full at the pinned blob. It runs AC1-AC9, AC11, AC17, AC12-AC16, AC10.
`S6` occurs in the spec only at `:65`, `:435`, `:560` and `:1073` — never inside §6 — and grepping
that range for `refusal`, `ledger`, `244` or `246` returns nothing. Every other scope item is
observed: S1 by AC1, S2 by AC2/AC3/AC9, S3 by AC6/AC9/AC11/AC17, S4 by AC12/AC13, S5 by AC14/AC15.
AC16 observes the selftest arms S6 cites as reaching the branches, not the ledger comment itself.

No gate compensates. §7 says so in its own words: the pin is shrink-only and already 27 behind, so it
cannot detect growth at all. AC10's full bar does run the `govkit refusal join` leg (guarded on
`tools/govkit/`, which this unit stages), so "still exits 0" is incidentally covered — but the ledger
comment landing and the exactly-two growth are not, and cannot be.

The 246 figure is not free-standing either. `_is_refusal` at `refusal_join.py:135-138` matches a
`<obj>.fail(...)` call ONLY as a bare `ast.Expr` statement, so an arm written as an assignment, a
comprehension, a ternary or a call routed through a helper contributes zero and the ledger comment is
false on the day it lands. (`enumerate_branches` at `:146-153` also walks every `FunctionDef` and then
that function's whole subtree, so an arm placed in a nested helper is double-counted;
`selfcheck()` has no nested defs today, so that shape only appears if the builder introduces one.)

**Fix.** Add an AC, modelled on the sibling's AC9 which already carries exactly this observation over
the same file and the same base count: after the commit, `python tools/govkit/refusal_join.py` exits
0 and reports a branch count exactly two higher than the count measured immediately before the
commit, `BRANCH_PIN` is unmoved at 217, and the ledger comment names both branches with their
armed/unarmed status. State in S4/S5 that each arm must be a bare `r.fail(...)` expression statement
written directly in `selfcheck()`, since that is what makes the figure true.

**Left-shift gate.** The single best gate in this report, and it is four lines: **a hygiene check that
every `S<n>` declared in a spec's §2 is named by at least one criterion in §6.** Both sections are
numbered, both markers are fixed strings, and the check is a set difference. It catches this finding,
it catches the same shape the build already filed as `TOOL-aHonedRuleset-12`, and it would have
caught round 1's equivalent. Run it over the whole `memory/builds/` corpus before wiring it, per the
charter's rule about testing a predicate against the real tree first.

---

## M3 — MEDIUM. AC11 grades the one wrong placement rev-6 happened to find, not the class S3's rule forbids

**Address:** §6 AC11, the renderer-list clause, against §2 S3's PLACEMENT paragraph. Raw id 5.

S3 states a precise rule: the new anchor goes immediately ABOVE `<!-- govkit:entry memory-tree -->`.
AC11 grades a proxy for it — the `playbook` section's derived body still contains the renderer list —
which observes only the mid-`playbook` placement rev-6 found.

Verified at source: `check_runbook_parity.py:71-81` derives a section body as every line from one
anchor to the next and grades ONLY emptiness; the problem and census lines count anchors and
problems, nothing about order. `:35`'s anchor regex imposes no position. The live anchor sequence is
`:55 :73 :150 :215 :299 :357 :497`. So an anchor dropped anywhere AFTER the `memory-tree` anchor —
end of file included, which is the failure mode rev-5 priced, or mid-`drift-audit`, or mid-`push-main`
— leaves the `playbook` body intact with its renderer list, keeps both bodies non-empty, takes
problems 18→17 and the census to 8, and passes every clause of AC11 while re-parenting a different
section's tail. That is B2's harm, one section over. Nothing else covers it: the checker sits in no
`tools/gate-legs.json` row, so AC10 cannot see it either.

**Fix.** Replace the proxy with the rule. Assert the anchor sequence in `WIRE-INTO-PROJECT.md` is
`… playbook, check-microformats, memory-tree …` by grepping `-n` for `govkit:entry` and comparing the
ordering, and keep the renderer-list grep as the corroborating observation rather than the whole of
it.

**Left-shift gate.** Teach `check_runbook_parity.py` the order it already parses: a declared expected
anchor sequence, red on reorder or on an anchor landing outside its declared slot. The checker
already builds the anchor list to derive bodies, so this is a comparison against a literal, not new
parsing. Charter §7 names this shape by hand — *gate the CLASS, not the instance*.

---

## M4 — MEDIUM. The owner ruling on S3's bytes was given roughly half of S3's bytes

**Address:** §8 F4, *The real byte cost against what was budgeted* (`:905-906`, restated `:1009`), and
§4's Files-touched row for `WIRE-INTO-PROJECT.md` (`:341`). Raw ids 13, 30.

§2 S3 says "Three edits to `WIRE-INTO-PROJECT.md`" and enumerates First/Second/Third; §9's rev-6 line
confirms the third was added at rev-6 as the B1 remedy. Neither carrier that prices S3 moved:

- §4's row still reads "the id added to the `--kits` example at line 82, plus an anchor line and one
  sentence as its body" — two edits, a direct §2/§4 contradiction a builder reads as the checklist.
- F4 still prices 19 B (id) + ~193 B (sentence) + 40 B (anchor) = "~254 rather than ~212, a 20%
  increase on a scope item that was 0.31% of the document, taking it to roughly 0.37%". There is no
  line for the wiring instruction anywhere.

The magnitude matters: the sibling wiring blocks S3 is told to copy run 287 B at `:262-266` and 473 B
at `:351-355`, so the real S3 cost is at least double what the ruling was shown. F4 is the owner
ruling on whether S3's bytes earn their place in an uncapped document, and `TOOL-aScouredKit-23`'s
uncapped-growth concern — which F4 explicitly declines to answer while citing its figure — is
understated by about the same factor.

Stated honestly, one sub-claim does not survive: F4's ANCHORING decision does not flip, because the
254-vs-212 arithmetic compares anchored against unanchored and the wiring step sits on both sides of
that comparison. The stale carriers are real regardless.

**Fix.** Re-measure S3 with the wiring instruction included, restate F4's cost bullet and its
percentages against the three-edit total and the current document size, and extend §4's row to name
all three edits.

**Left-shift gate.** Covered by H1's scope-item↔table lint, extended one step: the Files-touched row
for a file must name as many edits as the scope item declares for it ("Three edits" against a row
describing two is a countable mismatch). Same leg, same grep, one extra assertion.

---

## L1 — LOW. F4's pointer to the placement rule names the wrong scope item

**Address:** §8 F4, *The option TAKEN* bullet, `:943`. Raw id 15.

The bullet says "The rule is now stated in S2's own placement paragraph and pinned against the
EXISTING anchors". S2 (`:26-29`) is the descriptor edit — delete `selectable = "conditional"` at line
14 and rewrite the header — and carries no placement text. The PLACEMENT paragraph is S3's, at
`:40-50`. This is the pointer a builder follows to find the rule B2 was raised to install, and it
sends them to the wrong scope item, in the same fold that added the rule.

**Fix.** `S2's own placement paragraph` → `S3's own placement paragraph`.

**Left-shift gate.** Partially reachable: a spec lint asserting every `S<n>` / `AC<n>` cross-reference
resolves to a declared item catches dangling references but not this one, since S2 exists. The
catching half is a §10 checklist row — **an intra-spec pointer added in the same fold as the thing it
points at is checked by opening the target once** — which is cheap and is the only honest answer for
a class grep cannot see.

---

## L2 — LOW. `matrix.py:66` is a blank line; the cited pin is at `:63`

**Address:** §8 F1, Correction 1. Raw id 16.

Resolved live and at the spec's declared base. `"line length": "NOT ADOPTED — no declaration at"`
sits at `tools/govkit/matrix.py:63`; `:65` closes the dict and `:66` is blank.
`git log 94958534..HEAD -- tools/govkit/matrix.py` is empty and the base blob has identical
numbering, so the pin was never right and did not drift. The spec's other two `matrix.py` pins in the
same rev (`:48`, `:61`) are correct, which rules out a whole-file offset. A reader verifying the
surviving half of F1's class argument lands on a blank line.

**Fix.** Re-pin to `matrix.py:63`, or cite the key by name (`"line length"` in the expected-verdict
table) the way F4 switched its runbook citations to entry ids at this same rev.

**Left-shift gate.** A `file:line` pin resolver over SPECCED specs: for every `` `path:NN` ``
citation, red when the path does not exist, when the line is blank, or when the line does not contain
the token the spec quotes beside it. Run it against the spec's declared base blob so a moving tree
does not produce noise. This one leg would have caught L2 and would have caught the two round-1
citation findings, which is what earns it a place despite the severity.

---

## What round 1 asked for, and what rev-6 actually did

Read against §9's rev-6 log line, which is accurate about what it moved:

- **B2 (anchor placement) is CLOSED.** S3 now pins placement against the existing anchors and AC11
  gained the renderer-list clause. What remains is M3's residue — the criterion grades the instance
  rev-6 found rather than the class the rule forbids — which is a narrower finding than B2 was.
- **B1 (payload lands, nothing runs) is NOT closed.** rev-6 answered it with a correct trace of the
  wrong command. B1 above is the same defect, verified one layer down.
- **The five round-1 HIGHs and the AC-tautology corrections landed** and were re-verified here; AC7
  and AC8 now carry the revision, and the 8-byte template headroom finding is correctly recorded.
- **The fold reproduced its own dominant class.** Round 1's headline was "a scope fold never carried
  into the sections that describe the scope", found four times. Round 2 finds it six times, all of
  them introduced by the rev-6 fold: H1 (S6's seventh file against six counts), H2 (a §3 bullet three
  documents cite and nobody wrote), H4 (AC9 grading the pre-fold S3), M4 (F4 and §4 pricing the
  pre-fold S3), and half of M2. That is the argument for landing M2's four-line §2↔§6 lint and H1's
  scope-item↔table lint in this build rather than filing them: the class has now survived two folds
  by hand, which is the charter's own test for when a check stops being a preference.

## Not carried

Eleven raw findings were refuted by the skeptic pass and are not listed. Three deserve a line so the
fold does not re-litigate them: the claim that AC10's full bar cannot see `refusal_join.py` at all
(it can — the leg is guarded on `tools/govkit/`, which this unit stages; what it cannot see is
growth); the claim that F4's anchoring RULING flips on the unpriced wiring bytes (it does not — the
step sits on both sides of the comparison); and the claim that §3's `last-audit` conclusion is wrong
(it is right — `refusal_join.py` is absent from the `watch:` list; only the stated verification's
scope is stale, which is H1).

## Landing bar for round 3

Land B1 and the five HIGHs, then re-run this audit against the rev-7 blob. H1, H2 and H4 are single
edits each. B1 needs a measured paragraph and an AC17 rewrite, and it needs the backlog row corrected
in the same commit, because that row is the copy that leaves the spec.
