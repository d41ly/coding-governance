**Serves:** spec-audit TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3

# aStagedLane — spec audit of the three-unit set, round 3

*Node `a`, 2026-09-04. A Tier-2 adversarial pass over the three remaining specs at rev-4, with the
ROUND-2 FOLD as the primary subject. Round 2's findings were almost entirely defects that round 1's
fold introduced, so the rev-4 prose was the highest-yield surface again and it is where this round's
findings sit. A primed finder fan, a skeptic stage prompted to REFUTE each finding, one synthesis.
Every claim any finding makes about the existing tree was re-run at source before it was written
here, and the command and its output are quoted inline wherever the claim is load-bearing.*

**Round: 3.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-1.md@04e9cf3be15dbf00555b4e5bd3dcc8371607d2b3`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-2.md@aa0a8376e24d399df31d9bef89b5037bbf462afa`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-3.md@a475360e556f4904e5322df5f490dd8192a91dd8`

## Verdict: BLOCKED

One blocker, six highs, one medium, one low. The blocker is not a prose defect and it is not
hypothetical: unit 1's widened leg REDS on the current default branch, measured, on two units of
`DEPL-dGaugedVintage`. The leg carries `red_after_land = true` and `.githooks/pre-push` blocks a red
default-branch push, so unit 1 as specified cannot land. Everything else on this list is fold
residue — false premises about the tree, a two-site fix applied at one site, and two acceptance
criteria that cannot fail.

## The subject set shrank, and unit 4 is not graded here

`TOOL-aStagedLane-4` was RETIRED to WONTDO between rounds: round 2's blocker 1 established that it
cannot be built inside `memory/guides/BUILD-METHOD.md`'s 23 remaining bytes, and both ways to fund it
are owner turns under BUILD-METHOD M3 veto 2. That disposition is parked for the owner. It is
deliberately not a subject of this round and no finding below touches it, which is also why the
`Serves:` line names three ids rather than four.

## Shape of the run

Raw 42, confirmed 11, refuted 31, unverified 0. Precision **0.26** — well under the ~0.5 floor §8
names, and §8's own prescription applies: tighten scope and priming before adding agents, do not
widen the fan. A third pass over a twice-folded surface is exactly where precision should fall, since
the population of real defects is shrinking while the finders' appetite is not.

The 11 confirmed findings collapse to **9 distinct defects** after merging duplicates: three finders
independently hit unit 3's AC5 false premise about `check-verifier-fanout.sh`, and it is recorded
once below as finding 9. The counts in this section are the raw ones; the table's are the adjudicated
ones, and the two integers that matter — one blocker, six highs — are the table's.

## Findings

| # | Sev | Unit | Address | Defect |
|---|---|---|---|---|
| 1 | BLOCKER | 1 | §5 risks, §3 non-goal 1 | The widened leg reds on `main` today, on two landed units |
| 2 | HIGH | 1 | §2 S2c vs §2 S2, §6 AC7 | `<first>^` falls in neither window — a one-commit blind spot at the boundary |
| 3 | HIGH | 1 | §7 vs §2 S2b/S2c/S2d, §6 AC13 | The named meta-gate structurally cannot see a single new branch |
| 4 | HIGH | 1 | §2 S4, §5 perf | Two ceilings with opposite calibration rules derived from one loaded reading |
| 5 | HIGH | 2 | §2 S4 vs §4 mode table | Two answers for where `--plan` runs; AC4 grades against either |
| 6 | HIGH | 2 | §2 S4 predicate, §6 AC4 | `DONE` is not `READY` — attended mode halts on every resumed build |
| 7 | HIGH | 3 | §4 "Why the fan is permitted" | Round-2 finding 10 folded at one of its two sites; the fan's proof is now false |
| 8 | MED | 2 | §6 (absent criterion) vs §2 S5 | The fold's own remedy is the one header statement no arm reads |
| 9 | LOW | 3 | §6 AC5 | False premise about a merge-bar leg; the third clause restates the first |

---

### 1 — BLOCKER — unit 1, §5 "risks" and §3 non-goal 1

§5 says a widened population **may** red builds already landed. It does, and the count is two.

I ran S1+S2's predicate over the three run-state-free builds inside the cutoff. `DEPL-dGaugedVintage`
is squarely in the widened population: it has no `RUN.md` (`memory/builds/dGaugedVintage/` holds
`README.md`, `build`, `reviews`, `spec` and nothing else), its `opened: 2026-09-01` equals
`PASS_ORDER_CUTOFF="2026-09-01"` at `.unattended.conf:212`, and the leg's `sort -C` admits
`opened == cutoff`. Grading from the S2 folder anchor:

- `DEPL-dGaugedVintage-12` — build commit `9ba3757d`, which ADDS
  `memory/builds/dGaugedVintage/spec/2026-09-01-spec-DEPL-dGaugedVintage-12.md` in the same commit
  that changes `tools/check-install-prefix.sh` and `tools/install-prefix-carried.txt`. Its parent
  `ff12039f` holds specs 1–11 and no spec-12.
- `DEPL-dGaugedVintage-13` — build commit `34492bb6`, which ADDS its own spec-13 alongside
  `tools/drift-audit/drift_report.py`, `drift_signals.py` and `selftest.py`. Its parent is
  `9ba3757d`, which holds 1–12 and no spec-13.

Two hard build-before-spec violations, not `unbuilt-in-range`. The leg carries `red_after_land = true`
in `tools/unattended/kit.toml`, sits on the bar with an empty guard, and has no waiver mechanism.
History is append-only, §3's non-goal 3 forbids moving the cutoff, and non-goal 1 declines to audit
anything. So the unit is unlandable as written, and `.githooks/pre-push` is what will say so.

The process defect underneath is the one that matters for the next spec too: §10 never ran the
candidate predicate over the real tree. `AGENTS.md` §7 requires exactly that before wiring one, and
requires printing hits AND near-misses. Had it been run, §5 would have carried two commit shas
instead of the word "may".

**Fix.** Make the predicate run a DoR item and put its disposition in scope. Add an open question
naming `DEPL-dGaugedVintage-12` and `-13` with the three real options: raise `PASS_ORDER_CUTOFF`
past 2026-09-01, add a declared per-build waiver registry beside the leg's other declarations, or
land the two as a recorded exception. Rewrite §5's risk line from "may red" to the measured pair.

**Left-shift gate.** The leg gets a `--preview` mode that grades the live tree and prints violations
without setting exit status, and a test arm that runs it over the real `memory/builds/` and asserts
the violation set is EMPTY or is exactly the declared waiver set. A widening then cannot be armed
before it has been measured, and the waiver registry cannot silently grow — the same declared-
population posture `tools/unattended/kit.toml` already takes for the kit's own moving parts.

---

### 2 — HIGH — unit 1, §2 S2c against §2 S2 and §6 AC7

S2 pins the anchor explicitly at line 31: the reused walk "excludes its anchor, so the anchor is
taken as `<first>^`". The range is therefore `<first>`..HEAD. S2c then searches, at line 41, "the
history strictly before the anchor" — which excludes `<first>^` a second time.

`<first>^` is in neither window. That is a one-commit hole sitting exactly where AC7's fixture lands
in its most natural staging: product code committed, the build folder created in the very next
commit. S2 spends a paragraph pinning the inclusive/exclusive question at one end of the range and
AC8 arms that end; the other end gets a demonstrable gap and no criterion observing it. The unit
exists to close this boundary and ships with the flagrant case invisible at it.

**Fix.** State the pre-anchor window's endpoints in S2c the way S2 states the range's: every commit
reachable from `<first>^`, INCLUSIVE — `rev-list <first>^`, not `<first>^^`. Add to AC7 that the
violating commit is the build folder's first commit's immediate PARENT, so the boundary is pinned
rather than assumed.

**Left-shift gate.** Two fixture arms in `tools/unattended/check-pass-order.test.sh`, one on each
side of `<first>^`, and a rule for the spec template's acceptance section: a criterion that pins a
range endpoint owes a sibling criterion at the other endpoint. The cheap machine form is a checker
arm asserting the test file contains a `parent-of-first` fixture whenever the source contains a
`^`-derived anchor.

---

### 3 — HIGH — unit 1, §7 against §2 S2b/S2c/S2d and §6 AC13

§7 names `python tools/memory-tree/check-arms.py` as the gate covering "the new branches". That
gate's population is discovered as tracked `*.sh` files that DEFINE `fail() {` and carry `fail <n> "`
call sites. Measured on the subject:

- `grep -c 'fail() {' tools/unattended/check-pass-order.sh` → `0`
- `grep -c 'fail [0-9]* "' tools/unattended/check-pass-order.sh` → `0`
- `python tools/memory-tree/check-arms.py --report` lists exactly ten gates, and
  `check-pass-order.sh` is not one of them.

So a leg named in the Definition of Done will report green having seen none of S2b's fallback, S2c's
probe, or S2d's cap refusal. The leg's refusals are bare `echo` plus `exit`, and no in-scope change
brings it into the population, so this is not a near-miss that the build fixes by accident. It is the
could-not-fail shape these specs police in each other, shipped inside this unit's own gate list — and
AC4 only ratchets the arm count by at least one while the unit adds several branches.

**Fix.** Either delete `check-arms.py` from §7 and name the coverage that is real —
`tools/unattended/check-pass-order.test.sh` plus AC4's arm-count ratchet — or add a scope item giving
`check-pass-order.sh` a numbered `fail()` helper so the meta-gate's population reaches it, and say so
in §4 Files touched. The second is the better trade and it is small.

**Left-shift gate.** A leg that reds when a spec's §7 names a gate that publishes a `--report`
population, and a file the same spec's §4 lists as touched is absent from that population. It is a
narrow predicate, it is mechanical, and it catches false coverage attribution at spec time rather
than at review time.

---

### 4 — HIGH — unit 1, §2 S4 and §5 perf/scale

S4 prescribes deriving BOTH ceilings from one LOADED reading — "463 s on node `a`, measured
2026-09-04 under load … A ceiling is derived from the loaded reading, because a bound that fires on
normal concurrent execution is worse than no bound." That sentence is lifted from
`TOOL-dRetiredFork-40`, which is about `gate-legs.json` rows killed under the 8-wide pool. It belongs
to that carrier and only that one.

The `BUDGET_*` carrier already decided the opposite, in its own file. `tools/unattended/run-unattended-gates.sh:54-62`:
"IT IS CALIBRATED IDLE, AND A BUSY BOX WILL BREACH IT", and a bigger, load-tolerant figure "is WRONG
here" because it would pass the very regression the ceiling exists to catch — "this one is set to
catch the former and is EXPECTED to fire on the latter". `TOOL-aCollapsedScan-4` is CLOSED · SETTLED
on that basis and `TOOL-aCollapsedScan-9` is the OPEN question about making the shape load-aware.
Neither id appears anywhere in the spec.

So the build would raise `BUDGET_pass_order_history` from 90 to a loaded-derived figure inside the
file whose own header refuses that move, silently reversing a settled decision and reopening a parked
trade. The runner's ceiling then cannot fire on a real regression of this leg — the inert-bound class
`TOOL-dRetiredFork-40` opened for the other carrier. S4 itself says the two figures answer different
questions and then gives them one reading.

One embellishment in the finder's version is wrong and is corrected here: only `BUDGET_kit_gate`
carries the `IDLE` stamp, not every sibling declaration. It is not load-bearing.

**Fix.** Split the reading in S4. An IDLE node-`a` reading for `BUDGET_pass_order_history`, written in
the sibling form `measured N s IDLE on node a <date>` and citing `TOOL-aCollapsedScan-4`/`-9` for why
this carrier is calibrated idle; the loaded 463 s reading for the `gate-legs.json` row, citing
`TOOL-dRetiredFork-40`. AC5 then observes that both readings exist and differ in basis, not merely
that the leg finished inside its ceiling.

**Left-shift gate.** `run-unattended-gates.sh` reds on a `BUDGET_*` declaration whose trailing comment
does not carry an idle stamp with a node and a date. A ceiling arriving without its basis reds by that
fact, which is the same rule §7 already applies to a suite arriving without a ceiling.

---

### 5 — HIGH — unit 2, §2 S4 against §4's mode-boundary table

S4 puts the attended build stage's per-unit refusal on `bash tools/unattended/unattended.sh --plan
<slug>` and never says who runs it or how the state reaches the refusal. Three facts make that
unresolvable as written:

- The harness has no shell and no filesystem, by its own header.
- Its `units` input contract carries `{id, order, specPath, briefPath}` and no state field.
- §4's own table, line 108, rows `--plan` as "the CALLER, never this script", distinguishing it from
  the rows it attributes to the BUILD prompt.

So the design section and the mode table give different answers, and no scope item adds either a
caller-supplied state field or a BUILD-prompt instruction. AC4 — "the stage refuses and its message
names both the unit id and the state FORKED" — is therefore unobservable against anything but a test
double the builder writes to match whichever mechanism they picked. That is the fixture-grading-the-
fixture failure already recorded at `unattended-build.js:330-334` and in `TOOL-dRetiredFork-22`. The
contrast with S7, which names its caller-supplied mechanism and its limit in so many words, shows the
omission is an omission rather than something implied.

**Fix.** Name the mechanism in S4. Either a `units[].planState` entry the caller resolves from
`--plan` — and then say the input contract changes and that a MISSING value REFUSES rather than
defaults — or an instruction in the attended BUILD prompt, and then say AC4 observes the COMPOSED
prompt the way AC8 and AC9 do, not a refusal the script performs. Correct §4's `--plan` row to match
whichever is chosen.

**Left-shift gate.** The harness validates its `units[]` entries at entry and refuses an entry missing
a required field, with one arm in `unattended-build.test.sh`. A spec that invents a field the contract
does not carry then fails at build time instead of surviving to a closing review.

---

### 6 — HIGH — unit 2, §2 S4's refusal predicate and §6 AC4

S4 refuses "a unit whose reported state is not `READY`". `--plan`'s vocabulary includes `DONE`, and
every terminal unit reports it. `verb_plan` at `tools/unattended/unattended.sh:2144`:

    case "$st" in CLOSED|WONTDO) [ "$state" = "READY" ] && state="DONE" || state="DONE ($state)" ;; esac

Measured: `bash tools/unattended/unattended.sh --plan dGaugedVintage` prints all thirteen ids as
`CLOSED  DONE`. The harness derives `units` from `--plan`'s full roster and nothing in the spec
filters terminal ids out — §4 assigns `--plan` to the caller and the roster arrives whole.

So the first attended invocation over a resumed or partially built build refuses at unit one and names
`DONE`. That is round-1 B4's halt-at-unit-one class recurring in the rev this fold claims closed it.
It also makes attended mode STRICTER than the mode §3 says it is deliberately weaker than:
`verb_dispatch` at `:4607-4610` refuses only MISSING and THIN plus out-of-order, and refuses neither
`DONE` nor `FORKED` — while AC4 makes `FORKED` the attended refusal exemplar.

**Fix.** Enumerate the states in S4 rather than allow-listing one token: MISSING, THIN and FORKED
refuse; DONE is a SKIP with a log line naming the unit. Say whether the caller pre-filters terminal
ids or the stage does. Add an AC for the DONE-unit skip beside AC4.

**Left-shift gate.** The test arm for the refusal is fed the REAL `--plan` output of a closed build —
`dGaugedVintage` is on disk and costs nothing — rather than a hand-written roster. A double that only
ever contains `READY` cannot discover that `READY` is not what a closed unit reports.

---

### 7 — HIGH — unit 3, §4 "Why the fan is permitted"

Round-2 finding 10's fix said to delete the backlog clause "from S3c and from §4". It was deleted from
S3c only.

- S3c, lines 74-75, now carries the withdrawal: the template mandates no backlog row, `grep -c -i
  backlog memory/TEMPLATE-SPEC.md` returns 0, "the backlog half of the argument is" withdrawn.
- §4, line 124, still reads: "…AND S3c, keeping the git index and the backlog out of them" —
  byte-identical to the rev-3 text at `e99b9776:97`.

So §4 attributes to S3c a coverage S3c explicitly withdrew, inside the clause-3 argument that is the
sole licence for a parallel fan against `TOOL-cBriefedPilot-21`'s ratified `parallelism route: none`.
One sentence of the permitting proof is false about its own sibling section. The claimed builder
confusion is overstated — §4 is rationale and no AC funds a backlog prohibition — but the defect is
real, checkable, and one deletion from closed.

**Fix.** Rewrite §4's clause-3 sentence to match what S3c now says, and quote
`BUILD-METHOD.md:188`'s four named records rather than paraphrasing them, so the proof is checkable
against the clause it cites.

**Left-shift gate.** A fold-completeness check: the rev-N revision-log entry names the sections it
edited per folded finding, and a leg asserts the rev commit's diff touches every section named. This
finding is a two-site fix applied at one site, which is the only failure mode that check exists for,
and it has now happened twice in this build.

---

### 8 — MED — unit 2, §6 (absent criterion) against §2 S5

S5's rev-4 addition requires the harness header to state "that M4's blocker-disposal clause is
UNREACHABLE in attended mode, because under S3 that mode reaches BUILD only at a terminal verdict and
the clause is composed only for a non-clean one". AC6 reads the header back for the five named losses,
for their refusal/record classification, and for the S7 caller-dependence — and stops there. The M4
statement is not one of the five, so no criterion reads it.

Coverage strictly FELL across the fold: AC8's own closing sentence records that rev-3's disposal-clause
assertion was DROPPED because that clause is never composed in attended mode, and S5's header statement
is what replaced it. An observed assertion was traded for an unobserved one. The header is the only
place attended mode's limits are recorded and AC6 is the only thing that reads it, so the fold's own
remedy can ship missing with every criterion in §6 green. This is round-2 finding 8's class recurring
in the sibling unit's fold, and the sibling closed its version by adding AC9 and AC10.

**Fix.** Extend AC6 with a third clause: the header also states that M4's blocker-disposal clause is
unreachable in attended mode and why. Add the matching assertion to S6's arm list.

**Left-shift gate.** An acceptance-coverage ratchet over the spec template: count the "the header
states…" requirements in §2 and require the AC that reads that header to name the same number of
statements. Crude, and it would have caught both instances of this class in this build.

---

### 9 — LOW — unit 3, §6 AC5

*Merges three independently confirmed findings.*

AC5's third clause requires `tools/hooks/agent-cap.js` to admit the changed file when its own predicate
is run over it, justified by: "The two workflow checks exiting 0 do not answer the hook's question."
That premise is false about `tools/workflows/check-verifier-fanout.sh`, which says so in its own
header:

> THIS GATE DOES NOT IMPLEMENT THE RULE. It feeds each script to `tools/hooks/agent-cap.js` — the same
> predicate the `PreToolUse` hook applies at the `Workflow` tool call — and reports what the hook says.

Its body builds a `{tool_name:"Workflow", tool_input:{script}}` payload and pipes it to the hook with
no `--only` flag. `tools/workflows/unattended-build.js` is inside its population, and the gate is a
merge-bar leg. Run against the subject it prints `verifier-fanout: clean — 1 workflow script(s) obey
the ≤5-verifier rule` and exits 0. So the third clause has no failure mode independent of the first,
and it buys no observation while reading as extra coverage.

The residual the clause is reaching for is real, and the gate's header states it two paragraphs later:
the hook is the primary entry point because it sees the INLINE `script` string of an ad-hoc review,
which is the modality the rule exists for and which no file-scoped gate can ever see.

**Fix.** Drop the third clause and its justification, or keep it and state the real residual: one
predicate at two entry points, and the file entry point is the one this unit needs and the leg already
covers. Do not leave the false sentence where it can be copied into the file's header or a gate comment
during the build.

**Left-shift gate.** Extend the spec-audit predicate round 2 proposed for path and verb literals: when
a spec asserts that a named gate does NOT check something, require the assertion to quote a line from
that gate's own header. A claim about a gate that the gate contradicts in its first twenty lines is the
cheapest false premise in this corpus to catch, and this build has now produced it in every round.

---

## What rev-4 got right

Recorded because a report that only lists defects mis-states the fold's quality. Rev-4 closed round 2's
two blockers and most of its highs correctly and at source: unit 1's dead `skipped_norun` counter is
retired, its cost figure is now measured rather than borrowed, unit 3's slice-grouping contradiction is
resolved in favour of groups throughout, and unit 3's S3c backlog claim is withdrawn with the `grep`
that disproves it quoted inline. Finding 7 above is the one deletion that fold missed, not a sign it
was done carelessly.

The blocker is also not a prose defect and would not have been found by reading harder. It needed the
predicate run over the tree, which is a DoR item this spec set still does not have.
