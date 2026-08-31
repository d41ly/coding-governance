**Serves:** spec-audit TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 TOOL-aClosedDocket-3

# aClosedDocket — spec audit of the three-unit set, round 2: the FOLD

*Node `a`, 2026-08-31. A Tier-2 adversarial pass whose SUBJECT is the round-1 fold, not the specs as
a whole: `git diff 67298753..HEAD -- memory/builds/aClosedDocket/`. A primed finder fan, a skeptic
stage prompted to REFUTE each finding, one synthesis. Every claim any finding made about existing
code was re-checked at source during synthesis before it was written down here; two claims moved on
that re-check and both are named in the finding that carried them.*

**Round: 2.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-1.md@bad2ffd210d2bd78e7f0b4d307ccc383ebc06406`
- `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-2.md@d8927d5028d7f2b8bc64515d79d506b4242352f1`
- `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-3.md@31d61ad727c2db2d98b506e2e27e98a738310081`

## Verdict: BLOCKED

Four blockers stand, and the round-1 count was three. The convergence predicate compares confirmed
blocker counts and re-arms only on a STRICTLY smaller one, so a `--review` round recording this
result against the prior `blockers 3` row returns NON-CONVERGENT. That is not a technicality to work
around — it is the exact case `TOOL-aClosedDocket-1` exists to give a disposition for, arriving
before the unit that would legalise it. Say so in the round row and take the disposition the owner
rules on, rather than re-scoring this report to make the number shrink.

Three of the four blockers are on unit 1, and they are not three views of one defect. The unit
promised a byte budget in a section that does not contain one, absorbed a merge-bar gate predicate
and a new driver-written fact under an id M2 says can hold one mechanism, and left its risk and
production-readiness paragraphs describing the rev-1 unit that no longer exists. The fourth is on
unit 2, where the fold corrected the log row's field names in scope and left the only criterion that
grades that row demanding the shape it had just removed.

The through-line is the class this repo already names. Eight of the eleven findings below are
`amendment-leaves-its-other-half-standing`: the fold edited the sentence it was pointed at and left a
scope item, an acceptance criterion, an inventory row or a readiness paragraph asserting the
opposite. Round 1 fixed what it was shown. Nothing swept the rest of the document afterwards, and
the single highest-value left-shift in this report is a mechanical sweep that would have caught five
of the eight before this round existed (see **The one gate worth building**).

**Review shape.** Raw 49 · confirmed 21 · refuted 28 · unverified 0 · precision 0.43. The 21
confirmed findings collapse to 10 distinct defects — four lenses independently found the byte budget,
four found unit 2's field names, four found unit 3's stale count, two found unit 1's stale Rollout,
and two found the ungraded fold-trace producer. One further finding (H5) was raised by the synthesis
pass's own source verification rather than by the fan, is labelled as such below, and is verified at
`tools/codebase-map/map_lib.py:113-119` and `:83-95`. Eleven findings are reported.

Precision at 0.43 is where round 1 sat and is at the floor the charter names. Over a document
corpus that has just been rewritten, that is expected rather than alarming: half the fan's yield was
re-reporting the round-1 findings the fold had already closed. A round 3 over these same three
specs should tighten the lens priming to the fold diff alone rather than add lenses.

## Findings

| # | Severity | Subject | Address |
|---|---|---|---|
| B1 | BLOCKER | AC2's byte budget has no route to satisfaction | spec-1 §2 S1a against §4 and §6 AC2 |
| B2 | BLOCKER | Two mechanisms under one id, against M2 | spec-1 §2 S1/S5/S5a |
| B3 | BLOCKER | §4 Rollout and two thirds of §5 still describe rev-1 | spec-1 §4 Rollout, §5 Security and Error states |
| B4 | BLOCKER | AC1 grades the row shape the fold removed | spec-2 §6 AC1, with §3 N3 and §8 Q1 |
| H1 | HIGH | S5a's producer is ungraded; every AC grades the consumer | spec-1 §6, against §2 S5a |
| H2 | HIGH | The kit-work self-test DoD is missing, and so are two test files | spec-1 §7 and §4 Inventory |
| H3 | HIGH | S3a's resolution guard has no acceptance criterion | spec-2 §2 S3a, against §6 |
| H4 | HIGH | "the three named in S1" names two | spec-3 §6 AC3, §4 Inventory, §3 N3 |
| H5 | HIGH | The scratch-repo rule does not redirect the log | spec-2 §2 S6/S6a, against §6 AC6a |
| M1 | MEDIUM | S3's record obligation is ungraded | spec-1 §2 S3, against §6 |
| M2 | MEDIUM | AC8 covers the SKILL carriers and not the protocol | spec-1 §6 AC8, against §4 Inventory |

---

### B1 — BLOCKER — AC2's byte budget has no route to satisfaction, and S1a says it does

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-1.md`, §2 S1a,
against §4 and §6 AC2.

S1a closes with "the replacement therefore pays for itself out of M4, and §4 names the sentences it
trims and why each trim is meaning-preserving." §4 names none. Its six blocks are Inventory, the
clause-3 vacuity note, "The authority this unit is built under", "Why a fold is the right disposition
and not a weaker one", "Alternatives rejected" and "Rollout". There is no trim list, no donor
sentence and no byte arithmetic anywhere in the document. The Inventory row says only "the
disposition sentence and its trim", which names nothing.

**Verified at source.** `wc -c` gives exactly 24549 for `memory/guides/BUILD-METHOD.md` and 24560 for
`tools/memory-tree/BUILD-METHOD.template.md`, matching AC2's two numbers. M1 declares "Budget: ≤24 KB,
≤350 lines" at `BUILD-METHOD.template.md:8`; read as 24 KiB that is 24576, leaving 27 and 16 bytes.
M3's delegation clause at `:76-77` excludes "M1's own budget included", so the run cannot raise the
cap. The sentence S1 replaces is at `BUILD-METHOD.template.md:137` — the whole line is 806 B and the
promotion sentence within it measures 217 B:

> `**At the exit every blocker still standing is PROMOTED** to a unit of this build, specced at its tier and built; not parked, not waived, not re-reviewed, and audited as a SPEC, which is what makes promotion terminate.`

The replacement must state TWO dispositions, the test that selects between them, and why each
terminates. A terse draft doing that — already dropping "not parked, not waived, not re-reviewed" and
"audited as a SPEC", both of which S1 requires each disposition to keep — measures 272 to 292 B. So
the floor deficit is 55 to 75 B and the realistic one is 80 to 120 B, against 16 B of template
headroom.

One sub-claim moved on re-check and is named rather than quietly dropped: **no gate enforces M1's
budget.** There is no `24576` literal anywhere under `tools/`, and `check-memory-hygiene.sh` has no
size arm for this file. The constraint is a rule the document states about itself and AC2 is the only
thing that would measure it. That makes the finding slightly less mechanical than round 1 implied —
nothing turns red automatically — and no less blocking, because AC2 is the criterion that closes the
unit and it is stated as a hard ceiling with no ratified exit.

**Why this blocks rather than annoys.** A builder writes the wording, measures, finds it 80 B over,
and is then holding a governance carrier it may not re-budget, mid-edit, with no ratified route
except a fork to the owner that S1a has already told it is unavailable. `aPrimedKeepalive` landed
this same template 8 B over at 24584 by exactly that path.

**Fix.** Add a §4 subsection, "The byte budget and what pays for it", in the shape
`memory/builds/dTieredTribunal/spec/2026-08-26-spec-dTieredTribunal-12.md:147-148` already uses for a
prior M4 wording change: the candidate replacement wording with its measured `wc -c`, each donor
sentence with its byte count and a one-line argument that the trim is meaning-preserving, and the
arithmetic reaching ≤24549 and ≤24560. If the arithmetic does not close, say so in §8 as an open
question with the owner-facing options — raise the cap, or move the second disposition into the KIT
README prose M4 points at — and route it as an M1 fork BEFORE building.

**Left-shift.** Two halves, and only one is gateable. Structural: a `check-memory-hygiene.sh` arm
that reds when a spec's §2 or §3 forward-references a section by number ("§4 names", "§4 states",
"settled in §8 Q3") and the named section contains no heading matching the promised noun. Content:
a `gotchas.py` class, `spec-promises-a-section-that-does-not-exist`, on the numeric-ceiling case
specifically — an AC naming a byte or line ceiling for a tracked file owes a §4 arithmetic block, and
the checklist asks for it by name at the closing diff.

---

### B2 — BLOCKER — a gate predicate and a new driver-written fact ride under an id M2 says holds one mechanism

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-1.md`, §2 S1, S5
and S5a, against BUILD-METHOD M2.

M2 reads verbatim at `tools/memory-tree/BUILD-METHOD.template.md:32-34`:

> "one mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
> unit with its own id and spec. Two mechanisms in one spec make a 'unit built' pass unreviewable —
> the closing diff cannot tell which half a finding lands on."

Rev-2 puts under one id: a governance-document sentence (S1), a change to a merge-bar GATE's
predicate (S5, `check-unattended.sh` clause 3, read at `:246-303` and it does machine-enforce
promotion as the only disposition), and a NEW driver-written run-state fact (S5a). `check-unattended.sh`
is a gate. M2 names a gate explicitly.

**The counter-argument, stated so the owner can weigh it.** Carriers that move with a rule — renders,
the SKILL restatement, kit versions — are one mechanism, and S6 and S7 are uncontroversial on that
reading. The question is whether clause 3 is a carrier of M4 or a mechanism of its own. Three things
say mechanism. It is a PREDICATE change, not a pointer refresh. S5a introduces data that did not
exist, which M2's "generated artifact" clause reaches. And the §4 authority note compounds it: the
delegation it cites, `TOOL-aProvenReuse-3`, is for the M4 ROW, and it does not name a change to the
bar — so the run would be spending a delegation on a surface the delegation does not mention, which
is the M3 veto-2 shape.

**Verified at source, and it sharpens the case.** Q3 asserts that writing the trace into the round
row "costs no new verb, no new file and no new grammar". The parser half of that is TRUE and worth
recording, because it could have been a second blocker and is not: clause 3's awk at
`check-unattended.sh:269-283` splits the row at the FIRST ` · reason ` and regex-matches the tail, and
`review_counts` at `unattended.sh:3511-3524` does the same, so a token appended after the exit token
is visible to both and disturbs neither the `blockers [0-9]+` match nor the
`CONVERGED|NON-CONVERGENT|CEILING` test. The existing suite arm at `unattended.test.sh:4183` is a
substring `grep -c` and survives an appended token too.

The GRAMMAR half is false. `verb_review` at `unattended.sh:3526` takes exactly slug, subject, verdict
and blockers; `REVIEW_VERDICTS` at `:444` is the closed set `CLEAN|CLEAN WITH FIXES|BLOCKED`; and the
`note` appended to the row is computed deterministically from `review_state`. There is no input by
which a run declares a disposition. N4 forbids a verb deciding it. So the trace needs a NEW flag in
the argument parser beside `--subject` and `--blockers` at `:4291-4292`, a refusal for a malformed
value, and — per `verb_review`'s own comment at `:3550-3552` — a LITERAL check number for that
refusal, because `check-arms` discovers a branch by its check number. That is a new verb surface, and
it is the second mechanism arriving in the open.

Worth recording alongside it, because it bears on how much the trace buys: since the driver cannot
decide the disposition, it TRANSCRIBES the run's claim. What that adds over prose in a README is
grammar, append-only placement and refusal at the moment of exit — not independent evidence. S5a's
stated rationale, "an authored claim is not evidence", is therefore not delivered in full by Q3's
mechanism. This is recorded as evidence for B2 and H1 rather than as a separate finding.

**Fix.** Split. Keep `TOOL-aClosedDocket-1` as the M4 sentence plus the driver message and the
carriers. Mint a second unit for clause 3's predicate and the fold trace, sequenced BEFORE it,
because the rule cannot land while the bar refuses it. Record the split as an M2 AMEND in the build
README's BUILD-LEVEL RULES slot. If the owner prefers one unit, that too is an M2 AMEND and needs to
be written down as one — the defect is an unrecorded exception, not the shape itself.

**Left-shift.** A `check-memory-hygiene.sh` arm over spec §4 Inventory tables: red when one spec's
Inventory names paths in two or more DECLARED kit directories AND at least one row's path matches a
tracked gate (any file named in `tools/gate-legs.json`), unless the spec carries an `M2 AMEND` marker.
It is a coarse predicate and it would have fired here on the day S5 was written. Run it over the
tracked spec corpus first and print hits and near-misses before wiring, per §7.

---

### B3 — BLOCKER — §4 Rollout and two thirds of §5 still describe the rev-1 unit

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-1.md`, §4 Rollout
and §5 Security / Error states.

Rollout reads, verbatim and untouched by the fold:

> "One commit. The change is to a document and a message; nothing is generated from it and nothing
> flips."

Against rev-2, "the change is to a document and a message" is false — S5 changes a gate predicate and
S5a adds a driver-written fact. "Nothing is generated from it" is false — §4's own Inventory lists
`memory/guides/BUILD-METHOD.md` as RENDERED, S6 as `SKILL.template.md` "and its render", and S7 as
regenerated renders. "One commit" is false — the real shape is at least three. Only "nothing flips"
survives.

§5 Security reads "N/A. Prose in a guide and one message string." §5 Error states reads "N/A; no new
predicate", on a unit whose S5 is nothing BUT a predicate change, and which the spec itself calls
load-bearing: "without this the whole unit is a rule the bar refuses."

**Verified at source.** `git diff 67298753..HEAD` on this file touches exactly one line of §5 — the
Testing bullet, rewritten to name "S5's clause-3 arm" — and touches §4 Rollout not at all. So the
fold edited one line of the readiness section and left its siblings asserting the opposite of the
line it had just corrected. §7 is likewise untouched, which is H2.

**Why this blocks rather than reads as staleness.** §4 Rollout is the unit's risk statement and the
paragraph a closing diff review reads to know what the unit was allowed to touch. "N/A; no new
predicate" reads as licence to skip the production-readiness thinking a merge-bar gate predicate
actually owes, on the one scope item the spec calls load-bearing. Under §1's DoR a Tier-2 spec owes a
readiness menu for its scope; for S5 and S5a that menu has not been run. If the owner reads these as
documentation staleness rather than as an unrun readiness pass, the finding collapses to HIGH — the
report says which reading it took and why, and does not hedge the verdict.

**Fix.** Rewrite Rollout for the rev-2 scope: the commit split (guide plus render; then the driver
message, the fold fact and clause 3; then the SKILL and PROTOCOL restatements and the two version
bumps), and state that two renders are generated from templates. Change Error states from "N/A" to
clause 3's own failure modes — a fold trace present with no exit line, an exit line carrying neither a
trace nor a promoted id, a trace on a subject whose loop never exited. Change Security from "N/A" to
one line about a run-supplied token entering a field a merge-bar gate parses, and what refuses a
malformed one.

**Left-shift.** The fold-residue sweep in **The one gate worth building** catches the Rollout half
mechanically. For the readiness half, a `gotchas.py` class: `readiness-section-outlives-its-scope` —
when a fold adds a scope item naming a predicate, a gate or a generated artifact, §5's Security,
Error states and Migration bullets are re-read and re-answered in the same edit, and a surviving
"N/A" beside such a scope item is a finding at the closing diff.

---

### B4 — BLOCKER — AC1 grades the row shape the fold removed, and it is the enforceable half

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-2.md`, §6 AC1, with
§3 N3 and §8 Q1.

The fold's own §9 records H3 replacing "rev-1's guessed field names with the measured ones and added
the `type` discriminator the existing reader filters on first". S2 now requires `type`, `at`, `query`,
`worktree`, `n_shown`, with the discriminator `"type": "lookup"`. AC1 still reads "carrying `at`,
`query`, `worktree` and `n_candidates`" — no `type`, and the field name S2 replaced. N3 and Q1 carry
the same dead spelling.

This is not a missing field, it is a contradiction in both directions. A row conforming to S2 FAILS
AC1 as written, because `n_shown` is not `n_candidates`. A row satisfying AC1 omits the discriminator.
AC1 is the ONLY criterion that observes the row's shape, so the enforceable half of the unit specifies
the shape H3 was written to delete.

**Verified at source.** `tools/memory-recall/query.py:1225` writes `"type": "query"` and `:1234`
writes `"n_shown"`. The existing reader's first filter is `grep '"type": "query"'` in the
`reuse-probed` arm — **measured at `tools/unattended/unattended.sh:3270`, not `:3268`.** S2 and four
of the fan's findings all cite `:3268`; the line is 3270. The claim is right, the citation is off by
two, and correcting it belongs in the same edit as the AC.

**Fix.** Rewrite AC1 to observe the row S2 specifies: exactly one appended row carrying
`"type": "lookup"`, `at`, `query`, `worktree` and `n_shown`, with the `type` value asserted
explicitly and an arm confirming the row survives a `grep '"type": "lookup"'` filter, because that is
the join key the arm S5 extends uses. Respell `n_candidates` as `n_shown` in N3 and in Q1's question
text, or state once in Q1 that `n_candidates` was rev-1's name for it. Correct S2's line citation to
`:3270`.

**Left-shift.** Genuinely gateable and cheap: a `check-memory-hygiene.sh` arm that collects
backticked identifier tokens appearing in a spec's §6 and reds on any that appears nowhere in that
spec's §2. `n_candidates` survives in §3 and §8 but is absent from §2 after the fold, so scoping the
permitted corpus to §2 fires here. Run it over the tracked spec corpus and print hits and near-misses
before wiring — the near-miss list is where its false-positive rate becomes visible.

---

### H1 — HIGH — S5a's producer is ungraded; every criterion grades the consumer

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-1.md`, §6, against
§2 S5a.

S5a's entire content is that the trace must be DRIVER-written and not authored. No acceptance
criterion observes a driver writing one. AC3 grades the printed MESSAGE. AC6 and AC7 both operate on
"a fixture run-state file" — a hand-authored record, which is precisely the authored claim S5a
rejects as evidence. So the set grades `check-unattended.sh`'s acceptance of a grammar a human typed,
and nothing grades the emitter.

**Verified at source.** The checker's own suite builds those fixtures with hand-authored `printf`
blobs — `tools/unattended/check-unattended.test.sh` writes review rows byte by byte at `:468`, `:476`
and `:708`. So the fixture route is the established one and it exercises the reader only.

The unit can therefore be built, pass every criterion in §6, and ship a fold trace no verb writes:
AC6 green, AC7 green, and the first real fold produces a run-state file with no trace and a red bar.
That is the same could-not-fail shape §4 already documents for clause 3 itself — a check whose fixture
supplies what the mechanism was supposed to produce. §7's honest-limit line does not cover it: it
concedes only that no predicate reads whether a run picked the RIGHT disposition, not whether the
driver emits a trace at all.

**Fix.** Add AC6b: run `bash tools/unattended/unattended.sh --review` against a live fixture driven to
a non-shrinking second round with the fold disposition declared, and observe the trace token in the
appended round row of a run-state file no hand wrote; then run `check-unattended.sh` over THAT file.
AC6 and AC7 stay as the checker's arms. Note in §5 Observability what the trace does and does not
buy, given the driver transcribes a run-supplied value (B2).

**Left-shift.** A `gotchas.py` class this corpus has now hit twice:
`fixture-supplies-what-the-mechanism-should-produce` — when a scope item requires a fact be PRODUCED
by code, at least one acceptance criterion must observe the producer, and a criterion whose input is
an authored fixture grades the consumer only. The Tier-2 checklist asks, for each scope item naming a
written fact, which criterion runs the writer.

---

### H2 — HIGH — the kit-work self-test DoD is missing, and the Inventory omits two suites that assert on the strings this unit edits

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-1.md`, §7 Gates and
§4 Inventory.

`tools/unattended/run-unattended-gates.sh:22-25` states in its own header:

> "nothing runs the self-tests automatically. A change under this directory that guts a check lands
> green. The compensating check is a person invoking this script, and the DoD for any work touching
> `tools/unattended/` is a GREEN verdict from `--selftests` pasted into the landing report."

Unit 1 edits `unattended.sh`, `check-unattended.sh`, `SKILL.template.md` and `PROTOCOL.template.md` —
all under that directory. §7 names `run-gates.sh` plus four legs, `check-kit-versions.sh` and
`check-verdict-epoch.sh`, and never names the self-test script. Units 2 and 3 both do, unit 2 with the
words "which this unit owes because it IS kit work". §7 is untouched by the fold, so it is the rev-1
gate set standing over a rev-2 scope that grew two files under `tools/unattended/`.

The Inventory omits `tools/unattended/unattended.test.sh`, which at `:4181-4183` asserts
`hit "$out" "NON-CONVERGENT"`, `hit "$out" "PROMOTED"` and an exact `grep -c` over
`review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT` — the message S4 rewrites
and the row grammar S5a extends. It also omits `check-unattended.test.sh`, which stages breaks against
the clause S5 changes.

**Why it matters here specifically.** By the 2026-08-23 ruling those suites are OFF the bar. The one
unit in the set that edits the driver and the checker is the one with no self-test obligation and no
inventory row for the suites that assert on the strings it changes, and nothing else will notice.
Unit 3's own Q1 names this repo's `arm-literal-strands-on-message-edit` class; unit 1 walks into it
with neither an AC nor a gate.

The `PROMOTED` assertion at `:4182` is the concrete hazard: S4 rewrites the NON-CONVERGENT message to
name both dispositions, and whether the token `PROMOTED` survives that rewrite is currently nobody's
stated obligation.

**Fix.** Add to §7 the sentence units 2 and 3 carry — a green `bash tools/unattended/run-unattended-gates.sh`
verdict, pasted, because this is kit work. Add `tools/unattended/unattended.test.sh` and
`tools/unattended/check-unattended.test.sh` to the §4 Inventory with what each owes: the `PROMOTED`
and `NON-CONVERGENT` arms at `:4181-4183` and the exact row literal at `:4183`, and clause 3's staged
breaks. Add an acceptance criterion that both suites pass with the edited messages.

**Left-shift.** A `check-memory-hygiene.sh` arm: when a spec's §4 Inventory names any path under a kit
directory that declares a self-test in its `kit.toml`, §7 must name that kit's self-test runner. It is
a path-set join against declarations that already exist, it fires on this spec today, and it makes the
compensating check for the 2026-08-23 exemption something a spec cannot silently omit.

---

### H3 — HIGH — S3a's resolution guard has no acceptance criterion

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-2.md`, §2 S3a,
against §6.

S3a is the fold's own addition (H4 in its §9) and nothing in §6 observes it. AC2 makes the log
DIRECTORY unwritable, which exercises the WRITE. S3a's subject is the git-dir RESOLUTION that S1
introduces as the file's first git call — a `subprocess` that raises, a git that is absent, a
`--git-common-dir` that fails.

**Verified at source.** The hole S3a names is real and exactly where it says: `query.py`'s `log_event`
has `p = log_path(repo)` on the line BEFORE its `try`, and `log_path` calls `common_git_dir`, which
runs `git rev-parse --git-common-dir`. So the seam this unit copies has the resolution outside the
guard, and a copied implementation reproduces it silently. No criterion in §6 is git-resolution-
shaped: AC1 reads the file before and after, AC2 unwritables the directory, AC6/AC6a count rows.

A build that copies `log_event`'s shape verbatim goes green on every criterion with S3a
unimplemented, while §5 claims "Testing — S6, both sides" and §7 discloses a different limit
entirely.

**Fix.** Add AC2a: with git unreachable — PATH stripped of git, or `GIT_DIR` pointed at a non-repo —
`reuse_lookup.py` still prints its candidates, exits `0`, and warns on stderr. That is the resolution
half of "never fatal", observed rather than asserted.

**Left-shift.** Fix the seam rather than only the copy, which is the cheaper diff: move
`p = log_path(repo)` INSIDE `log_event`'s `try` in `tools/memory-recall/query.py` and add an arm to
that kit's own suite. Then `reuse_lookup.py` copying the shape verbatim inherits the correct one, and
S3a becomes a property of the seam instead of a rule the next copier has to remember. File it as its
own unit — it is a change to a different kit and B2 is this set's cautionary tale about not doing
that inside someone else's id.

---

### H4 — HIGH — "the three named in S1" names two

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-3.md`, §6 AC3, §4
Inventory row, §3 N3.

H5 rewrote S1 from three arms to "the **TWO** arms" and moved the other two to N4. AC3 still reads
"no arm outside the three named in S1 changes". §4's Inventory row still reads "S1–S4 — the three arms
and their comments". N3 still prices the rejected lock "to fix three assertions".

**Verified at source**, and the line numbers check out exactly:
`tools/unattended/unattended.test.sh:4696` asserts `-lt 25` around `--preflight` and `:4709` asserts
`-lt 25` around `--close` — the two VERB wrappers S1 names. `:4651` and `:4661` assert `-lt 20` around
`run_bounded` directly — the two N4 excludes. So rev-2's count is the correct one and only the three
downstream mentions are stale.

AC3 is the sole observable for the scope boundary N4 draws, and its referent does not exist. §4's
Inventory row actively points a builder at a third arm N4 puts out of scope. The impact claim in two
of the fan's findings — that a builder could satisfy AC3's letter while breaching N4 — overstates
slightly, because N4 explicitly excludes the only candidates, so there is no third arm to find. The
defect is a checkable requirement that is false as written, in the criterion that grades H5's own
boundary. One word in three places.

**Fix.** AC3: "no arm outside the TWO named in S1 (`:4696`, `:4709`) changes" — cited by line so the
set is enumerated rather than counted. §4 Inventory row: "S1–S4 — the two verb arms and their
comments". N3: "two assertions", or "three observed failures" if that is what was meant. Add the §9
rev-3 line naming what disagreed.

**Left-shift.** The fold-residue sweep in **The one gate worth building** catches this class exactly:
"three" was deleted from S1 by the fold and survives in three other sections of the same file.

---

### H5 — HIGH — the scratch-repo rule does not redirect the log, because the kit resolves its root from its own directory

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-2.md`, §2 S6 and
S6a, against §6 AC6a.

*Raised by the synthesis pass's own source verification, not by the finder fan. It is reported with
the same evidence bar as the rest and is counted in this report's severity tally.*

S6 says "The map arm runs in a SCRATCH repo with its own git dir and NEVER against this tree." Taken
literally — create a temp git repo, `cd` into it, invoke `reuse_lookup.py` — that does not move the
log. `map_lib.repo_root()` at `tools/codebase-map/map_lib.py:113-119` returns
`resolve_root(kit_dir())`, and `kit_dir()` is "the directory holding this module". `resolve_root` at
`:83-95` documents itself as "the adopting repo's root, as a PURE function of where the kit dir sits".
Neither reads the working directory. So an arm that invokes the INSTALLED
`tools/codebase-map/reuse_lookup.py` from a scratch repo still resolves `repo_root()` to THIS tree,
and the row lands in this tree's git common dir — reproducing round 1's blocker B3, which S6 was
folded to close.

The redirect that actually works is `CODEBASE_MAP_ROOT`, checked first in `repo_root()`. It is the
kit's own established idiom: `tools/codebase-map/selftest.py` sets and unsets it around fixture work
at `:126`, `:142`, `:173`, `:857` and `:961`, and at `:388-389` deliberately strips it to test the
resolver. So the missing half of S6 is already the suite's habit — it just is not what S6 says.

AC6a is a real backstop and catches the contamination after the fact, which is why this is HIGH and
not a blocker: a builder implementing S6 literally reds AC6a and reworks. Two weaknesses in AC6a are
worth naming while it is being edited. A before/after row count cannot attribute — this is a fleet
where five worktrees of one repo run at once and S1's own rationale is that they SHARE the common dir,
so a concurrent session's genuine lookup raises the count and reds the arm for an innocent reason.
And a count comparison observes that the file did not grow, not that no row came from the suite.

**Fix.** S6 gains the operative half: the arm sets `CODEBASE_MAP_ROOT` to the scratch repo, which is
what actually moves `repo_root()`, and the scratch dir is `git init`-ed so `common_git_dir` resolves
inside it. Cite `map_lib.py:113-119` in S6 so the reason survives the next reader. Strengthen AC6a to
observe CONTENT rather than a count: assert that this tree's `lookups.jsonl` contains no row whose
`query` field matches the arm's fixture phrase, which is attributable and immune to a concurrent
session.

**Left-shift.** A `gotchas.py` class, `cwd-is-not-the-root-a-kit-resolves`: any test arm that isolates
a kit by changing directory must be checked against how that kit resolves its root, because three of
this repo's kits resolve from `__file__` and one from an environment override. Pair it with a
`selftest.py` arm asserting that `repo_root()` under a `CODEBASE_MAP_ROOT` pointed at a temp dir is
that temp dir — a two-line guard that makes the isolation mechanism itself testable.

---

### M1 — MEDIUM — S3's record obligation is ungraded

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-1.md`, §2 S3,
against §6.

S3 puts the record obligation in scope — "either disposition owes the same record", the build README's
BUILD-LEVEL RULES slot — and no criterion in §6 observes it. AC1 grades M4 for "both dispositions and
the test" only; AC2 bytes, AC3 the message, AC4 versions, AC5 pointers, AC6/AC7 the trace, AC8 the
SKILL carriers.

A replacement satisfying every criterion in §6 can omit the record obligation entirely. Under B1's
byte pressure the record clause is the most likely thing to be trimmed away, with nothing observing
its absence — the two findings compound.

The finding's second half, that no criterion grades whether a FOLDING RUN wrote the record, is weaker
and is not claimed here: §7 already concedes no predicate reads a run's disposition. The first half
stands on its own.

**Fix.** Extend AC1 to require that M4's replacement names the BUILD-LEVEL RULES slot as the record
for BOTH dispositions, or add a criterion greping the rendered guide for the slot inside the
disposition sentence.

**Left-shift.** A `gotchas.py` checklist entry rather than a gate, because the mapping is a judgement:
at the closing diff of any Tier-2 unit, walk §2's scope items and name the criterion that observes
each; a scope item with no criterion is a finding. That single question would have produced H1, H3 and
M1 in this round, which is the argument for it being a standing checklist item rather than three
separate gates.

---

### M2 — MEDIUM — AC8 covers the SKILL carriers and not the protocol that restates the rule in full

**Address.** `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-1.md`, §6 AC8,
against the §4 Inventory row for `PROTOCOL.template.md`.

AC8 greps only `tools/unattended/SKILL.template.md` and its render for promotion-only wording.
`tools/unattended/PROTOCOL.template.md:502` restates the rule in full, inside the `--review` verb
description: "at the exit every blocker still standing is promoted to a unit rather than parked."
§4's Inventory commits to editing that file "only where they restate the rule", and this is where it
restates.

**Verified at source.** `:502` is the single hit for `promot` in that file, so Q2's probe answers
cleanly and the edit is one sentence. AC5 cannot cover the gap: `check-method-carriers.sh` says in its
own header, "It does not read prose and judge whether a file restates M3. The test is structural" —
it grades pointer shape, not this sentence's content. So the one carrier Q2 was written to resolve is
the one carrier no criterion observes, and the run can land with the protocol still saying promotion
is the only disposition.

**Fix.** Extend AC8 to cover `PROTOCOL.template.md` and its render alongside the SKILL pair — same
grep, same zero-hit requirement, plus the positive half that all three state the pair of dispositions
M4 does. Note while editing that AC8's positive half currently names no command; give it one, or it
is a criterion with no observation that can fail.

**Left-shift.** Extend `check-method-carriers.sh` with a content arm scoped to ONE declared sentence
rather than to prose generally: for a registry row marked as a RESTATEMENT, the file must contain the
canonical sentence's key tokens and must not contain the retired ones. That keeps the structural
check structural — its header's promise stays true — and adds a narrow, declared content check beside
it, which is the shape §7 asks for when a structural check reads as a semantic one.

---

## The one gate worth building

Five of the eleven findings above (B3, B4, H4, and half of B1 and M2) share one shape and one cure.
The fold rewrote a scope item and left tokens it had just deleted standing elsewhere in the same
document. That is mechanical and it is checkable:

**`check-fold-residue`** — given a spec at rev-N whose §9 records a fold, diff it against rev-N−1,
collect the identifier-shaped and number-word tokens the fold DELETED from §2, and red on any that
still appears in §3, §4, §6 or §7 of the same file.

It would have fired on `n_candidates` surviving in AC1, N3 and Q1; on "three" surviving in AC3, the
Inventory row and N3; on "nothing is generated from it" surviving in Rollout after the Inventory
gained two render rows. It costs one `git show` per spec whose status header moved a revision, and it
runs only on specs that changed revision in the diff, so it is a guard-scoped leg by construction.

Per §7, stage a break and confirm RED before wiring it, and run the predicate over the tracked spec
corpus first, printing hits AND near-misses — the near-miss list is where its false-positive rate on
prose becomes visible, and this predicate touches prose.

## Hunt coverage

The round was directed at five priorities. What each returned, including where it returned nothing:

1. **`amendment-leaves-its-other-half-standing` across scope items, non-goals, criteria, inventory
   rows and §4 paragraphs.** The richest seam by a distance: B3, B4, H4, and the §4 half of B1 and
   M2. Eight of eleven findings carry this shape.
2. **Is unit 1 still one mechanism under M2, and is Q3 buildable?** B2, with the buildability analysis
   verified at source and folded into it. The parser half of Q3 is CLEAN and is recorded as such:
   clause 3's awk and `review_counts` both split at the first ` · reason ` and regex the tail, so an
   appended fold token survives both readers and the exact-literal suite arm at `:4183`. The grammar
   half is not clean — `verb_review` has no input for a disposition and `REVIEW_VERDICTS` is closed,
   so the trace needs a new flag, a new refusal and a literal check number.
3. **Unit 1's byte claim.** Verified: 24549 and 24560 exactly, 217 B for the replaced sentence,
   806 B for the whole line, 27/16 B of headroom. A conforming replacement measures 272–292 B. AC2 is
   unsatisfiable without a named trim budget, which is B1. One sub-claim corrected: no gate enforces
   M1's cap — AC2 is the only thing that would measure it.
4. **Unit 2's scratch-repo rule and AC6a.** H5. The rule is necessary and not sufficient, and AC6a is
   a real backstop with two weaknesses named.
5. **An acceptance criterion added by the fold that names no observation which could fail.** No
   independent finding. Every criterion the fold added can fail: AC6 and AC7 red on a fixture, AC2a
   red on a deleted line, AC6a reds on a row count that moves. The nearest miss is AC8's positive
   half — "and both carriers state the same pair of dispositions M4 does" names no command — and it is
   reported inside M2 rather than as a finding of its own.

## What this round did not fault

Recorded so a round 3 does not re-spend tokens here, and so a reader does not mistake silence for
absence of coverage.

- **Every line number the fold added checks out at source**, with one exception. `:4696`, `:4709`,
  `:4651`, `:4661` in `unattended.test.sh`; `:246-303` in `check-unattended.sh`; `:571-573` in
  `SKILL.template.md`; `:502` in `PROTOCOL.template.md`; `:137` in `BUILD-METHOD.template.md`; `:755`
  in `query.py`; `:193` in `unattended.sh`. The exception is S2's `unattended.sh:3268`, which is
  `:3270` — noted in B4.
- **Unit 3's fold is otherwise sound.** H5's recount is right, H6's AC2a is a genuine discriminator
  against the pre-existing `hit` assertions at `:4694` and `:4707`, and the RB_TOOK seam exists where
  §10 says. Only the count words are stale.
- **Unit 2's S6a is correct and well-argued.** `test_codebase_map.py` is template-mirrored and graded
  as adopter content; `selftest.py` is the kit's own suite. The move is right; H5 is about what the
  arm must ALSO set, not about where it lives.
- **§4's clause-3 vacuity note is honest and correctly scoped out.** It documents a second defect in
  the same clause, measured on `aProvenReuse`, and explains why S5 does not depend on it. That is the
  disclosure §7 asks for.
- **The three specs' `Serves` bindings, record tables and status headers are conformant** and the
  build README's generated units region matches at rev-2.

## Method

A primed finder fan, a skeptic stage prompted to refute each finding, one synthesis. Raw 49,
confirmed 21, refuted 28, unverified 0, precision 0.43 — measured over the fan's output, before the
synthesis pass's own source verification, which added H5 and corrected two sub-claims (B1's
"no gate enforces the cap", B4's line citation). The 21 confirmed findings collapse to 10 distinct
defects; 11 are reported.

Severity as adjudicated here: 4 blockers, 5 highs, 2 mediums. The blocker count did not shrink
against round 1's three, so the loop is NON-CONVERGENT on this subject and the disposition belongs to
the owner — which is, with some irony, the rule `TOOL-aClosedDocket-1` was written to supply.
