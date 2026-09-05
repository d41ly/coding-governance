**Serves:** spec-audit TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3

# aStagedLane — spec audit of the three-unit set, round 4

*Node `a`, 2026-09-04. A Tier-2 adversarial pass over the three remaining specs at rev-5, with the
ROUND-3 FOLD as the primary subject. Blocker counts have run 4, 2, 1 across rounds 1 through 3 and
every finding was folded, so this round was scoped to decide whether the loop ends. Rev-5 added a
great deal of new prose — unit 1's S2e waiver registry, S2f `--preview` mode, the inclusive
pre-anchor window, the split ceiling readings and the six-count liveness line; unit 2's `planState`
field and its enumerated state vocabulary; unit 3's corrections — and that new prose is again where
the findings sit. A primed finder fan, a skeptic stage prompted to REFUTE each finding, one
synthesis. Every claim any finding makes about the existing tree was re-run at source before it was
written here, and the command and its output are quoted inline wherever the claim is load-bearing.*

**Round: 4.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-1.md@787728dd6d9bd1b22f354ae095a13eb1c24e02df`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-2.md@a58c6e260c1919f0136514c07bc8a0cbd69e376a`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-3.md@916df7e280a00715326c87f72fa7b8d5d7a908ee`

## Verdict: BLOCKED

Three blockers, three highs, one medium, one low. The loop does not end here. Two of the three
blockers sit in one paragraph — unit 2's S4, the `planState` contract rev-5 added — and both were
introduced BY the rev-5 fold rather than carried into it, which is the fourth consecutive round in
which the previous round's fold text is the highest-yield surface. The third blocker is unit 1's
S2e waiver registry, which rev-5 added to make that unit landable and which, as written, is itself
unlandable.

The pattern this round is narrower than a general prose-quality problem and worth naming: rev-5
introduced two new CONTRACTS — a `planState` field on the harness input and a waiver registry under
`memory/project/` — and neither was specified to the standard this spec set applies to everything
else. A contract needs a value domain, a resolution point and a carrier. Between them the two new
contracts are missing all three.

## The findings

| # | Sev | Unit | Address | One line |
|---|---|---|---|---|
| B1 | blocker | 2 | §2 S4 | The enumerated `planState` vocabulary is not the vocabulary `--plan` emits |
| B2 | blocker | 1 | §2 S2e, §4 | The waiver registry has no filename, no row format, and reds the hygiene leg |
| B3 | blocker | 2 | §2 S4, §6 | `planState` has no resolution TIME, and all three stages run in one invocation |
| H1 | high | 1 | §2 S4, §6 AC5 | `gate-legs.json` cannot carry the reading S4 puts beside it, and AC5 passes untouched |
| H2 | high | 2 | §6 AC4 | AC4's two halves cannot both hold, so one will be silently dropped |
| H3 | high | 3 | §6 AC6 | `check-review-join.sh` cannot make the observation AC6 names |
| M1 | medium | 1 | §3 | The first non-goal forbids exactly what S2e now performs |
| L1 | low | 2 | §5, §6 | The one error state §5 declares has no criterion observing it |

---

## B1 — blocker — unit 2, §2 S4, the enumerated state vocabulary

**Address:** `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-2.md`, section 2 S4,
with section 6 AC4, AC11 and AC12.

S4 declares a closed five-token state set — `MISSING`, `THIN` and `FORKED` refuse, `DONE` skips,
`READY` builds — and cites `unattended.sh:2144` as its authority. That line does not say what S4
says it says. Read whole:

```
case "$st" in CLOSED|WONTDO) [ "$state" = "READY" ] && state="DONE" || state="DONE ($state)" ;; esac
```

S4 quotes the `READY` half and drops the else-branch on the same line. A terminal unit whose spec
does not grade READY prints a COMPOSITE — `DONE (THIN)`, `DONE (FORKED)`, `DONE (MISSING)` — and
`unattended.sh:2132` emits a sixth shape that is in no branch of that case at all,
`NO TRACKED SPEC (rendered row without one)`. The driver's own comment three lines above states the
rule the spec missed: the grade is printed beside `DONE`, never in place of it.

This is not a hypothetical population. Measured over the real corpus, taking the third column of
each roster:

```
$ bash tools/unattended/unattended.sh --plan aPrunedCeremony   ->  3 DONE, 2 DONE (THIN), 1 DONE (FORKED)
$ bash tools/unattended/unattended.sh --plan cBriefedPilot     -> 20 DONE, 3 DONE (FORKED)
$ bash tools/unattended/unattended.sh --plan aBoundedCeiling   ->  3 DONE, 3 DONE (THIN)
$ bash tools/unattended/unattended.sh --plan aLeasedGauntlet   ->  1 DONE (FORKED)
$ bash tools/unattended/unattended.sh --plan dGaugedVintage    -> 13 DONE
```

`dGaugedVintage` is the one build S4 cites, and it is the only one of the five that produces the
uniform `DONE` column S4 generalizes from.

S4 assigns behaviour to no value outside its five, and §5's out-of-set refusal covers `mode` only.
So the shipped behaviour on a closed-but-THIN unit is whatever the builder guesses, and the three
natural readings diverge on the same input. A substring test for `FORKED` refuses a terminal unit
and halts the attended run at unit one on any build carrying a forked closed spec — which is
round-1 B4's failure shape recurring for the third time, inside the fold that claimed to close it. A
substring test for `DONE` skips it. A strict closed-set equality test refuses a value the driver
legitimately prints, with no defined branch to refuse it on.

**Fix.** Take the vocabulary from `verb_plan`'s actual third column rather than from a hand-written
list. State that a terminal grade may carry a parenthesised sub-state; that `DONE` and
`DONE (<anything>)` both SKIP; that `NO TRACKED SPEC` refuses; and — the part S4 is missing
entirely — that any value matching none of the enumerated shapes REFUSES and names the value it
received, rather than falling through. Equivalently, S4 may put the normalization on the caller and
say so, but then it must say that the caller normalizes to the leading token, because "resolved by
the caller from `--plan`" does not currently specify any transformation at all.

**Left-shift gate.** Add an arm to `tools/workflows/unattended-build.test.sh` that feeds the build
stage the literal third column of `bash tools/unattended/unattended.sh --plan cBriefedPilot` — a
real roster carrying three `DONE (FORKED)` rows — and asserts every row is graded and none refused.
That arm reds today, cannot be satisfied by a hand-written double, and covers the class rather than
the instance: any future state token the driver learns to print flows into it for free.

---

## B2 — blocker — unit 1, §2 S2e and §4 Files touched

**Address:** `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-1.md`, section 2 S2e,
against section 4's Files-touched paragraph and section 7.

S2e makes the whole unit landable on "a DECLARED per-unit waiver registry at `memory/project/`" and
then names no file, no row grammar, no absent-file behaviour and no way for the leg to locate it.
Section 4 has no design paragraph for it, and its estimate still reads "Five files, two of them
declarations", enumerating `check-pass-order.sh`, its test, `run-unattended-gates.sh`,
`gate-legs.json` and the kit descriptor. Neither the registry nor `.unattended.conf` is among them.

That is a specification gap on its own. What makes it a blocker is that the registry as described
lands RED, which is the same unlandable posture rev-5 exists to remove.

`memory/project/` has a CLOSED filename set. `tools/memory-tree/check-memory-hygiene.sh:389-421`
whitelists it by NAME — eleven case arms, matching exactly the eleven tracked registries — with a
fall-through `F:*` arm that accepts only names listed in `PROJECT_REGISTRY_EXTRA`. That key is not
declared in `.memory-tree.conf` (`grep -c` returns 0, so it stays the shipped blank). A tracked file
under `memory/project/` outside the whitelist fails `HYGIENE check 3 FAILED — unexpected entries
(structure)`. And the `memory hygiene` row in `tools/gate-legs.json` carries no `guard` key at all,
so it runs on every bar — including the full bar section 7 puts on this unit.

The two most recent registries confirm the shape: `trace-waiver.txt` and `readme-contract.txt` each
got an explicit case arm. Adding a registry here is a two-file act, and the spec asks for one file
it does not name.

There is a second, independent fork S2e does not address. `check-pass-order.sh` is a copy-installed
kit file that reads every project-specific value out of `.unattended.conf` — `MEMORY_ROOT`,
`PASS_ORDER_CUTOFF`, `GENERATED_INDEXES`, `SHARED_RECORDS` — and exits 2 without that file at line
55, precisely because a path spelled into shipped bytes resolves to nothing in an adopter installed
at another prefix. No adopter has a `memory/project/` at all. The in-repo registries S2e would
imitate (`check-spec-tokens.py:46`, `check-testsuite-counts.sh:28`) are gov-internal tools that DO
hardcode, and are not the precedent this leg gets to follow. With the absent-file case unspecified,
one reading reds every adopter's merge bar on a file they have never heard of, and the other
silently disarms AC15's stale-entry refusal.

AC14 and AC15 both grade against a surface the spec does not declare. AC14 asks that `--preview`'s
violation set equal "the set S2e's waiver registry declares"; AC15 asks that a stale entry red.
Neither has a file, a format or a lookup to grade against.

**Fix.** S2e names the file under `$MEMORY_ROOT/project/` (the leg already derives `MEMORY_ROOT`, so
no literal is needed) or introduces a new `.unattended.conf` key whose BLANK value means the empty
set, the way `PASS_ORDER_CUTOFF` and `RECALL_CLI` already do. It states the row format —
`<unit-id><TAB><reason>`, matching the shape `memory/project/spec-token-waivers.txt` already uses.
It states that an absent file is the empty set and is ANNOUNCED rather than a refusal, so an
adopter's copy neither reds nor silently disarms. And it adds declaring that filename in
`.memory-tree.conf`'s `PROJECT_REGISTRY_EXTRA` to scope. Section 4 then lists both new files and
corrects its count from five.

**Left-shift gate.** The registry is a declared population, so assert it in both directions the way
`check-spec-tokens.py` already does for its own waiver file: an entry naming a violation that no
longer exists REDS (which is AC15), and a violation with no entry REDS (which is the leg's normal
verdict). Separately, and cheaper: a spec lint that flags any path literal introduced in a spec's
§2 that does not also appear in that spec's §4 Files-touched paragraph. This exact omission —
a scope item creating a tracked file that §4 never counts — is now the second instance in this build
alone, after rev-2's missing `gate-legs.json` which S4's own text records.

---

## B3 — blocker — unit 2, §2 S4 and §6

**Address:** `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-2.md`, section 2 S4,
and section 6, which contains no criterion for it.

S4 makes `planState` a caller-resolved field on each `units[]` entry and refuses `MISSING` and
`THIN` at the BUILD stage. It never says WHEN the caller resolves it. That omission is fatal because
of how the harness is actually structured.

`tools/workflows/unattended-build.js` runs SPEC, then AUDIT, then BUILD inside ONE invocation. The
only early return before BUILD is the `CONVERGING` gate at line 439, and `review_state` prints
CONVERGED at a blocker count of zero regardless of round, so a round-1 clean audit reaches BUILD in
the same invocation that ran SPEC. The input contract is `units: [{ id, order, specPath, briefPath }]`
(line 70), it arrives ONCE as invocation args, pre-ordered, and the script has no filesystem with
which to re-resolve anything.

So on a fresh build — the path the SPEC stage exists for — the caller's entry-time `--plan` reports
`MISSING` for exactly the units the spec stage is about to author. `verb_plan`'s `missing_units`
loop prints `MISSING` for every planned unit nobody has specced. S4 then refuses `MISSING` at BUILD.
The harness cannot complete the SPEC-to-BUILD path that is this unit's entire goal.

Section 6 confirms the gap rather than closing it. AC1 stops at "reaches the build stage". AC4, AC11
and AC12 are all entry-time refusal arms. No criterion anywhere observes a unit that is specced by
stage 1 and then built by stage 3 in one attended run — which is the ordinary case.

This is round-1 B4's failure shape recurring one fold later, and it is distinct from B1: B1 is about
which VALUES the field can hold, this is about WHEN it is read.

**Fix.** State the resolution time in S4. Either the spec stage's own `authored` and `alreadyPresent`
lists promote a unit out of `MISSING`/`THIN` for the remainder of that invocation, or the build stage
grades `planState` only for units absent from those lists. Then add a criterion observing an attended
run over a unit that enters `MISSING`, is authored by the spec stage, and is reached by the build
stage in the same invocation.

**Left-shift gate.** One arm in `tools/workflows/unattended-build.test.sh` driving SPEC then BUILD in
a single invocation over a unit whose entry `planState` is `MISSING`, asserting the build stage
reaches it. It is the smallest thing that fails if the promotion is missing, and it is the arm whose
absence let this through.

---

## H1 — high — unit 1, §2 S4, with §6 AC5

**Address:** `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-1.md`, section 2 S4,
against section 6 AC5 and section 7.

S4 requires the ceiling re-declared "with the reading written beside it, in BOTH carriers that
declare one", and closes "each with its reading and its conditions written beside it". One of those
two carriers cannot hold prose.

`tools/gate-legs.json` is strict JSON over a closed key set. Measured: 93 rows, and the union of all
keys across all of them is exactly `argv ceiling chunk guard impure name subject`. That set is
pinned by `tools/run-gates/run-gates.test.sh:97-116` — the `run-gates canary` leg — which fails on
any stray key, and the file is parsed with `json.load` by the canary AND by `run-gates.sh` itself at
line 849. A comment does not merely red the canary; it stops the whole bar from parsing its
manifest. A builder following S4 literally reds the bar.

The other carrier has no such problem, which is what makes the asymmetry worth stating rather than
splitting the difference: `BUDGET_pass_order_history=90` in `run-unattended-gates.sh` already
carries its reading as a shell comment on the same line, exactly as S4 asks.

AC5 then fails to catch any of this, and fails in the could-not-fail shape this spec set polices
elsewhere. Its manifest clause asks only that the `pass-order history` row "carries a ceiling at
least as large". That row already reads `"ceiling": 900`, against S4's loaded reading of 463 s. The
clause passes with the file untouched, so it names no observation. Section 2 and section 6 are
therefore giving different instructions about the same carrier, and the loaded reading S4 says
belongs beside the manifest row has nowhere at all to live.

This is the exact class rev-5 fixed one criterion above it, in AC5's own sibling clause about
`check-verifier-fanout.sh` — and in the same edit it left this half standing.

**Fix.** S4 states that the manifest row cannot carry prose, and routes the loaded reading plus its
conditions to the leg's own header in `check-pass-order.sh`, leaving the JSON row a bare integer.
AC5's manifest clause names the expected ceiling VALUE and where its provenance is recorded, rather
than an inequality the unmodified file satisfies.

**Left-shift gate.** The canary already gates the JSON side and needs nothing. The gap is on the
criterion side: before landing, run every §6 acceptance command over the PRE-change tree and require
a documented RED for each. An AC that passes on the unmodified tree is an assertion about nothing,
and this is the third one this build has shipped past a fold — AC3 at rev-3, AC5's fanout clause at
rev-5, and this.

---

## H2 — high — unit 2, §6 AC4

**Address:** `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-2.md`, section 6 AC4.

AC4 demands both that the arm exercise a unit whose `planState` is `FORKED`, AND that the arm be fed
"the REAL `--plan` output of a closed build on disk rather than a hand-written roster". Those two
halves cannot both hold.

`unattended.sh:2144` rewrites every `CLOSED`/`WONTDO` unit to `DONE` or `DONE (<grade>)`, so a
closed build's real `--plan` output can never contain a bare `FORKED`. Reproduced across every build
on disk: bare `FORKED` rows appear only under `INPROGRESS`, `OPEN` or `SPECCED` units, never in a
build whose units are all terminal. And a caller normalization that DID produce `FORKED` from
`DONE (FORKED)` would refuse a terminal unit, contradicting S4's own DONE-skips rule.

So the builder must silently drop one half. The half most likely dropped is the real-roster
requirement, because it is the newer and the more inconvenient — and it is the only defence against
exactly the hand-written double that hid the `DONE` case through four revisions. An acceptance
criterion no arm can meet is worse than an absent one, because it reads as coverage.

The rev-5 log confirms the mis-attachment: the real-roster requirement was motivated by the `DONE`
discovery, which is AC11's subject, and it was attached to AC4.

**Fix.** Move the real-roster requirement to AC11, where a closed build is the right fixture and the
subject is a `DONE` unit. Leave AC4's `FORKED` arm on a NON-terminal unit and say so explicitly, or
source it from a build with an open unit whose spec carries an unresolved fork.

**Left-shift gate.** Covered by B1's suggested arm, which is the positive form of the same
observation: feed the stage a real roster and assert what it does with every row it actually
contains, rather than asserting a token the fixture cannot produce.

---

## H3 — high — unit 3, §6 AC6

**Address:** `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-3.md`, section 6 AC6.

AC6 requires that `check-review-join.sh` "counts the new wave". That gate cannot make that
observation. Measured on the unmodified tree:

```
$ bash tools/workflows/check-review-join.sh --explain
  tools/workflows/unattended-build.js — agent(1) falsy-drop(0) => not judged · 0 arity counter(s), best read 0
$ bash tools/workflows/check-review-join.sh ; echo $?
0
```

The gate's own trailer states the limit plainly: `NOT CHECKED HERE (this is a source scan) ... that a
SECOND wave is counted too — the counters are tallied per FILE`. So the criterion is unfalsifiable in
both directions. The gate cannot judge a file with no falsy drop, and where it can judge one, it
tallies per file rather than per wave. AC6 is satisfied by the tree exactly as it stands, having
observed nothing — again the class rev-5 fixed one criterion above it, in AC5, for
`check-verifier-fanout.sh`.

It also hides a real obligation. If the S5 merge drops falsy writer returns, the file becomes JUDGED,
and it will then need a dead-agent arity counter bound BEFORE the filter. No scope item in section 2
asks for that, so the day AC6 becomes checkable is the day it fails for a reason nothing specified.

**Fix.** Restate AC6 as an `--explain` observation: `tools/workflows/unattended-build.js` is reported
JUDGED with an arity counter read more than once. Add a line to S5 requiring the wave's arity be
taken before any falsy filter. Or drop the claim entirely and state that the gate does not reach this
file — which is honest and costs nothing.

**Left-shift gate.** Same as H1's: run each §6 command over the pre-change tree and require a
documented RED. Every one of the three could-not-fail criteria this build has shipped would have been
caught by that one step, and it costs one terminal invocation per criterion.

---

## M1 — medium — unit 1, §3, first non-goal

**Address:** `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-1.md`, section 3,
lines 149-151, against section 2 S2e and section 5's risk line.

The first non-goal still reads: not auditing the existing corpus for builds this widening will red,
and a build the widened leg reds is a finding for whoever lands it, not a migration this unit
performs. Rev-5's S2e performs exactly that audit — naming `DEPL-dGaugedVintage-12` at `9ba3757d`
and `-13` at `34492bb6` — and exactly that migration, a waiver registry listing them. Section 5's
risk line records the result as MEASURED, and S2f builds a `--preview` mode whose stated purpose is
repeating the audit.

Two answers to one question inside one document, and the half the fold left standing is the one a
builder reading section 3 first would scope the registry out on — shipping the unit in the
unlandable state rev-5 exists to fix. A reviewer grading against section 3 will call S2e scope creep.
This is the amendment-leaves-its-other-half-standing class the sibling spec's own rev-5 log names.

**Fix.** Rewrite the first non-goal to say what is still out of scope — a general corpus migration,
or rewriting any landed build — and point at S2e for the two ids the audit found and their
disposition.

**Left-shift gate.** Not mechanically gateable at reasonable cost; it belongs on the §10 recurring-
class checklist as a documented manual check: when a fold adds a scope item, re-read the non-goals
for the clause that forbade it. This build has now produced three instances of the class across three
folds, which is what earns it a checklist row rather than another one-off correction.

---

## L1 — low — unit 2, §5 error states, against §6

**Address:** `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-2.md`, section 5
error/empty/loading states, against section 6.

Section 5 states that a `mode` value outside the closed pair must refuse, not default. No acceptance
criterion observes that refusal. AC1 exercises `attended`, AC2 an absent `mode`, AC3 the null blocker
count, AC12 a missing `planState`; S6's arm list names no invalid-mode arm either.

The gap is inconsistent with this spec's own standard — it arms every other refusal it adds, and
rev-4 added AC10 for precisely this reason, recording that rev-3 had observed only one third of S3.
A gate whose failing case has never been observed is an assertion about nothing, and this is the one
error state section 5 declares.

**Fix.** Add a criterion: an out-of-set `mode` value makes the harness refuse at entry with a message
naming the value it was given.

**Left-shift gate.** Genuinely cheap and worth having as a lint: every declared error state in a
spec's §5 has at least one §6 criterion referencing it. It is a string-match over two sections of the
same file, it would have caught this one, and it generalizes to every spec in the corpus.

---

## Review shape

Raw 39, confirmed 14, refuted 25, unverified 0, precision 0.36. The 14 confirmed findings consolidate
to the 8 reported above: four of them were the same S4 vocabulary defect (B1), two the same AC4
defect (H2), two the same ceiling-carrier defect (H1), and two the same waiver-registry defect (B2).

Precision at 0.36 is below the ~0.5 floor the charter names as the point to tighten scope or priming
rather than add agents. That reading is expected on a fourth pass over a shrinking surface and is not
by itself an argument for another wide round: the same three specs have now been read four times, and
the marginal finder is mostly re-reporting. Round 5, if the fold produces one, should be scoped to the
rev-6 diff and its immediate context rather than to the three documents whole.

Every tree claim in this report was re-run at source before it was written. The commands and their
outputs are quoted inline where the claim is load-bearing, and the three subject blobs were confirmed
against `git hash-object` before reading.
