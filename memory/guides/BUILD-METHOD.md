<!-- gov:kit memory-tree@2.31 -->
# The build method — how a multi-pass build runs

## M1 — What this is

Binding for any build of more than one pass, attended or not. Template §1 defines a READY unit and a DONE unit;
this is the middle. It is a PROCEDURE — nothing here grades a run, and the merge bar is `tools/run-gates/run-gates.sh`.
**Budget: ≤24 KB, ≤310 lines**, a LOCAL constraint and not rule 6's — that rule gives a guide far more, and this file is stricter for its own reason: M7 re-reads it
WHOLE at every pass boundary and a method too expensive to re-read is skipped exactly when it is needed.
It rose from ≤20 KB / ≤250 lines when M12 landed, and again to ≤24 KB / ≤310 on 2026-08-21 — both owner
calls, because the figure is a stated constraint of a document rather than a measurement of one. The
second: two builds added rules here concurrently and both parents fitted the old cap alone, so nothing
was droppable and the constraint moved instead of the content. No gate enforces this pair, which is why
exceeding it silently was the one option not taken.
governance carrier and M3's veto 2 makes changing one an owner turn rather than an agent's.

`M<n>` is a section of THIS file, `§<n>` of another document. **The one rule about this file:** nothing here is
stated anywhere else in this repo — every generic obligation is POINTED AT via M11, and a rule appearing both here
and in an M11 carrier is a defect HERE. Drift resolves by deletion, not adjudication.

**The loop.** Decompose and classify the spec set (M2) → ground it with the two probes (M5) → author MISSING,
thicken THIN, resolve every fork (M2, M3) → review every unreviewed spec (M4) → build in passes, committing and
regrounding at each boundary (M6, M7) → review the cumulative diff (M8) → derive the wrap-up (M9). Everything
before "build in passes" precedes the first line of code, and a reground never re-runs it: re-running re-opens
closed forks.

## M2 — The spec set — decompose, detect, classify, act

**Decompose first**, before anything is classified: **one mechanism per spec.** A separate document, gate, adopter
or generated artifact is a separate unit with its own id and spec. Two mechanisms in one spec make a "unit built"
pass unreviewable — the closing diff cannot tell which half a finding lands on.

**Detect.** The roster is the build README's authored Units table where one exists, else the conforming specs under
`memory/builds/<slug>/spec/`. **`ids:` is not it either** — it is DERIVED and rewritten by the index generator, so it
answers "which ids exist", never "which units are planned", and a planned unit cannot be added to it by hand. A unit's spec is the file under `spec/` whose status header carries the id. Shape, tiers and sub-spec form are
`memory/TEMPLATE-SPEC.md`. Rebuild the roster after any fork resolution that adds a unit.

**Classify, first match wins.** Write it into the build README before acting on it.

1. **MISSING** — no conforming spec carries the id.
2. **THIN** — §2 Scope, §6 Acceptance or §7 Gates is empty, a placeholder, or names nothing observable.
3. **FORKED** — §8 Open questions carries an unresolved item.
4. **READY** — none of the above, and §10 Reuse audit is filled where the format requires it.

**Act.** **MISSING → author the spec, then re-classify.** *Authoring a spec is allowed:* the rule that a run may not
write its own mandate is about AUTHORIZATION — the mandate authorizes, the spec is the WORK. Write it at the tier
`memory/guides/SESSION-KICKOFF.md` assigns, same slug and folder; a spec you wrote this run is unreviewed by definition.
**THIN → fill it as a `rev-N` bump on the existing file** with its §9 line, never a second file for a unit that has
one — that is how a spec set stops agreeing with itself. **FORKED → M3.** **READY → build what it says**; to
diverge, change the spec first (rev bump + §9 line), then code. **AMEND → RETIRE (status `WONTDO`), SUPERSEDE
(replacement authored, original retired) or ADD**, when building uncovers what speccing could not; each owes a
recorded amendment. An id in the units region at the pinned BASE may never LEAVE it, so retiring is a status
flip.

**Hard floor.** Never build a MISSING or THIN unit; "I will spec it afterwards" is the same act with the record
written last. When ACCEPTANCE or GATES cannot be *derived* from the goal, the code or the prior records, the
disposition is the kickoff engine's Step 5b exit 5 — read it there. This file does not restate it and must not
contradict it.

**Sub-specs must AGREE with the main spec.** Before the first code pass, cross-read on four axes: **scope** (nothing
a sub-spec puts IN is OUT in the overview or a sibling) · **interface** (any name, path, signature or config key
spelled twice is spelled identically) · **ordering** (no sub-spec depends on a unit sequenced after it) ·
**acceptance** (the overview's is implied by the union of the sub-specs'). A disagreement is a defect in exactly ONE
document: fix that one, bump its rev, name what disagreed in its §9 line. Never build the intersection and never let
code arbitrate between two specs; a disagreement that is a choice rather than an error is a fork (M3).

## M3 — Forks — the decision rule, and the limit of your authority

Sweep §8 across the whole set before any code, including forks M2 just created. Resolved mid-build is a rewrite;
resolved before it, a decision.

**What is delegated.** A standing mandate delegates the owner's resolver authority for the named build only —
the forks its specs state, AND that build's own scope by M2's AMEND acts. Two bounds: the README's GOAL
statement is what a run may not amend, and the delegation does not reach veto 2's governance-carrier clause,
M1's own budget included. Vetoes 1 and 3 stand. A fork the goal cannot survive is still not yours — park it.
With no mandate, forks go to the owner and this is preparation.

**Ratify the most FEATURE-RICH option** — most stated acceptance criteria satisfied, fewest follow-ups left open —
after these vetoes, in order. Discard any option that:

1. fails an acceptance criterion or gate already written in the spec, or violates a §3 Non-goal;
2. needs a new external dependency, install location, public surface, or a change to a governance carrier;
3. widens a security, data or write surface beyond what the unit's risk tier priced.

Vetoes 2 and 3 are owner turns, **and that COLLAPSES onto the park rule rather than sitting beside it**: if the
only surviving option trips one of them, no resolver the mandate delegates exists, so the fork is parked exactly as
if nothing had survived. A veto is not a licence to take the vetoed option, and "owner turn" three lines above the
park sentence has been read as though it were. Tie-break: fewer open questions, then reuse of a seam M5 found.
**No survivors → park**, never the least-bad option.

**A FACT-QUESTION is a fork a stated PROBE decides — the one kind a run may resolve without an owner.** Mark it
with the `FACT-QUESTION · ` prefix the §8 readers recognise; legal only when the spec names the probe, the
observation that decides it, and a LIVENESS assertion that the probe can produce a negative. Take the winner only
when it falls out of the observation; the moment a preference is needed the rule above governs.

**A probe READS, it does not build.** It measures existing artifacts and may not construct an arm of the fork to
watch it behave: building one is not an M6 pass kind, so it inherits no commit, no regrounding and no gate, and it
puts code before the fork is resolved — a rewrite, not a decision.

**Counter-rule.** An observation that decides a fork by making a signal read ZERO is refused: that is the
vacuous-selector class, and a probe cannot tell "satisfied" from "matched nothing". A real fork here was resolved
AGAINST the better measurement for that reason, so a testing rule without this exception gets it wrong.

**Mark it in place** per `memory/TEMPLATE-SPEC.md` §8, naming resolver and authority, never `(owner, …)` for a
decision the owner did not make. The mark must be the documented SHAPE — the word, then
`(<owner|agent>, <date>[, delegated])` — and it may WRAP. Both readers grade the SECTION, not each item: with any
item present ONLY a conforming mark resolves it, the first line does not vote, and §8 says what that cannot see.

## M4 — The spec audit — review every unreviewed spec before its code

**Which.** Every spec with no review record naming it. A spec whose rev moved since its last review, or that you
authored this run, is unreviewed.

**Not the harness.** `tier2-review.js` reviews DIFFS; a spec is not code, so calling one reviewed by it is false.

**Run it as a `Workflow` script, not as direct `Agent` spawns.** The direct-spawn budget is keyed per PROMPT TURN
and an unattended run has no next user prompt to reset it: three specs audited by direct spawns exhaust it mid-set,
and the remaining lenses are refused with nobody to read the refusal. Agents inside a `Workflow` sidechain are not
counted against it. Shape: `memory/guides/REVIEW-PROTOCOL.md` — primed lenses → batched skeptics defaulting to
REFUTE → one synthesis — **under its fan-out and concurrency caps, read there and not repeated here.**

**Lenses: 3–5, primed with the mandate, the overview and the spec format.** The catalogue —
underspecification, contradiction, unstated assumption, prior art — with what each hunts, is in
`tools/memory-tree/README.md`.

**Record it** under `memory/builds/<slug>/reviews/` per `memory/HYGIENE.md` check 5's filename grammar, opening with
the literal line `## Verdict: CLEAN` — or `CLEAN WITH FIXES`, or `BLOCKED`. Most existing review records carry no
verdict line; write it anyway, because M9 derives from these records. **Carry the binding line** check 21 requires —
`**Serves:** spec-audit <the ids you reviewed>` — which is what makes "every spec with no review record naming it"
answerable from the tree instead of from memory. Grammar: `memory/HYGIENE.md`, "Record bindings". **Fold fixes into the spec** (rev bump + §9
line), then **STOP**: once a synthesis pass calls the design clean, stop reviewing that spec.

**A BLOCKED verdict has a disposition, and until now it had none.** The loop is bounded by CONVERGENCE, not a round count: a round re-arms only if its confirmed-blocker count is STRICTLY SMALLER than the one before — not merely "changed", which a 2, 1, 2 oscillation satisfies forever. **At the exit every blocker still standing is PROMOTED** to a unit of this build, specced at its tier and built; not parked, not waived, not re-reviewed, and audited as a SPEC, which is what makes promotion terminate. **Folding a round's own fixes does not re-arm the loop** — the fold is what the next round measures. A runaway ceiling backstops a defect in the predicate; reaching it is itself a defect, so the run promotes and lands anyway and says so in its output AND the build README.

## M5 — Recall and reuse

The obligation is `memory/TEMPLATE-SPEC.md` §10 and is machine-checked there. Satisfy it once for the SET, not per
spec, in this order — map dossier first, decision records second:

```bash
python tools/codebase-map/reuse_lookup.py "<behaviour phrase, not a symbol name>"
python tools/memory-recall/query.py "<question in plain English>" --terms "<8-14 words in this corpus's jargon>"
```

The recall CLI is offline and cannot coin terms — you write them, 8–14, or it exits 2 saying so. **Write into the
spec's §10** the seam you will extend, cited by path, or an explicit "no existing seam fits" with the evidence —
**and the recall terms you used**, because composing them is the expensive half and M7 re-runs the query.

Two rules you cannot afford to look up: **a probe exits 0 on a miss**, so "nothing found" is an ANSWER to record,
never a failure to retry with softer words; and **a hit can be STALE**, so verify any claim about current code
against source before building on it and say in §10 where the two disagreed. The rest of the probe-failure
taxonomy — blind layers, absent tools, which phrasing to try next — is in `tools/memory-tree/README.md`.

**"No existing seam fits" is where M12 begins.** A build whose solution is already chosen stops here; one
started from an owner's prose has not chosen yet, and M12 is how it does.

## M6 — Passes, commits, parallelism

**A PASS is exactly one of:** a spec authored · a spec reviewed · a review's fixes folded in · a unit built · the
closing diff review. Nothing else is a pass.

**Commit at the end of every pass**, on the run's branch, with the unit id in the subject. Then run the bug-class
checklist over what you just committed, and act on it before the next pass begins:

```bash
python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD
```

**It takes a COMMITTED range, so it runs after the commit, not before it.** Staged-but-uncommitted work is not in
`HEAD`, so the pre-commit spelling `<pass-base>..HEAD` resolves to an empty range and prints "touches no file" —
which reads as a clean checklist and is not one. Its stdout IS the checklist and it always exits 0 — finish it, do
not read its status. If a class it names is already violated, that is the next pass. Then the diff-scoped
gates for what the pass touched; the full bar runs ONCE, at the push boundary. A pass whose gate is red is not
followed by another: fix it, or park it with the reason. A pass that produced no change commits nothing and says so.

**Parking, at any point.** Write the *question*, the *options you saw*, and the *reason you refused* into the
build's authored record. A bare "parked" is indistinguishable from "forgotten", and M9 is where the owner gets the
turn you did not take.

**Parallelism is REQUIRED where disjointness is PROVEN; sequence is the fallback.** Two passes MUST run
concurrently when, and may only when: (1) their WRITE sets — actual paths, written down before dispatch — do
not intersect; (2) neither writes a file the other reads as a contract (conf, template, interface, generator
input) or as an acceptance input, and neither depends on the other's output either way; (3) neither touches a
shared mutable record — `memory/DECISIONS.md`, `memory/backlog/*.md`, the run-state file, or a generated index
TOGETHER WITH its generator. If you cannot write both path lists down, the work is not known to be disjoint —
sequence it. Both lists are RECORDED, not merely written: the unattended kit's `--dispatch`.

The fan-out and concurrency CEILINGS are the review protocol's; this is about WHICH work is parallel, never HOW
MUCH. Why clause 3 is worded as it is, and the vacuous form it replaced, is in the memory-tree README.

## M7 — Regrounding

You cannot observe your own compaction — do not try. **Reground at every pass boundary, unconditionally.** A commit
is something you perform; regrounding always is cheaper than the one rebuild caused by a boundary crossed blind.

Self-probe, two questions you must answer without scrolling back: *the current unit's id and what its §6 Acceptance
says*, and *the phase and its witness*. If either is not already in your head, you are regrounding whether or not
anything was compacted. Read in this order, and nothing else:

1. `git log --oneline -5` — under a mandate, `bash tools/unattended/unattended.sh --resume <slug>`.
2. The build's authored record whole (under a mandate `memory/builds/<slug>/RUN.md`, which survived compaction and
   process death where your context did not) — mandate, phase, witness, parked entries.
3. **This file, whole.** It is capped so this stays cheap.
4. The CURRENT sub-spec, whole — that one, not the set, which was read in M2 and is on disk.
5. Re-run the recall probe with the terms recorded in that spec's §10.

Then continue. **Regrounding never re-opens a resolved fork and never re-reviews a clean spec** — the §8 marks and
the review records outrank your recollection. Keep passes small: a compaction landing mid-pass is not caught until the next boundary.

## M8 — Closing the build

Bug classes FIRST — the M6 checklist over `<BASE>..HEAD`, ALWAYS that full range and on EVERY round: a class a
fold REINTRODUCES stays selected even where the fold's own files would not select it, and the probe costs seconds.
Its output is a lens brief, not a report filed after. Then ONE adversarial review — round 1 from the run's pinned
BASE (an immutable sha, never a moving ref) to the tip; round N>1 from round N-1's RECORDED TIP, so it reads the
FOLD that round introduced instead of re-reading fixes, and passes that round's confirmed set as `priorFindings`.
The harness refuses a base that is not a sha once the round is above 1. Per-pass reviews do not substitute: they
re-scan overlapping code and never see the seam between two passes.

```
Workflow { scriptPath: 'tools/workflows/tier2-review.js',
           args: { repo: '<abs repo path>', base: '<sha: BASE at round 1, round N-1's tip after>',
                   head: 'HEAD', round: <n>, priorFindings: [<round N-1's confirmed set>],
                   reviewDir: 'memory/builds/<slug>/reviews' } }
```

**Pass `reviewDir` explicitly** — its default is repo-root-relative and writes the report outside the memory tree,
where nothing indexes it. The harness names the file it wrote: **rename it to `memory/HYGIENE.md` check 5's
recording grammar before the next gate run**, or check 5 reds on a free-named file. A closing review is a
`diff-review`, not a `spec-audit`: give it `**Serves:** diff-review <every id in the diff>` and do not let it stand
in for the per-spec pass M4 owns — the two answer different questions and only one of them is about a design.

Fix every blocker, then re-review the FIX, not the diff again. A blocker unfixable inside the mandate's scope is a
park, not a waiver, and its unit does not close. Left-shift every confirmed finding — a regression gate, or a
`memory/gotchas/` class when the class cannot be gated; a finding fixed and not left-shifted returns.

**Re-read the build README against the code before closing** — every owner ruling and every sentence naming a shipped mechanism. `readme_mechanism_drift` reports only the pairs that spell it identically; the fold owns the rest.

**Landing** —
merge and push authorization, the lander, the bypass ban, conflict reconciliation, when a build may land — is
template §1 Landing and
`memory/guides/UNATTENDED-PROTOCOL.md`.

## M9 — The wrap-up — a derivation, not a recollection

Composed last, read first, after every fact is on disk. **Derive each row. If you cannot name the file a line came
from, the line does not go in.**

| item | derived from |
|---|---|
| build log and slug | `memory/builds/<slug>/` + generated `memory/LIVE.md` and `memory/ledger/<month>.md` |
| decisions taken | every §8 `RESOLVED` mark across the spec set (M3) + the `memory/DECISIONS.md` rows this build minted |
| problems resolved | each review record's `## Verdict` line and its blockers/highs (M4, M8) + the bug classes the checklist selected |
| open / parked | every `surfaced`-class parked entry in the authored record (M6) with question, options and reason, plus any recorded DoD override or directive waiver. `history`-class entries — a review round, say — are append-only sequence, carry no question, and are not the owner's to adjudicate |
| repo state | branch · shas · gate verdict · under a mandate the phase claim and its witness |

**Completeness test, the only one that matters:** every row has a source on disk. A field you cannot cite a source
for is not "unknown" — it is work that did not happen, and *that* is the line the wrap-up leads with. **Format is
template §16's** — payload first, ONE state block at the bottom — but its routine-completion length budget does not
apply: §16 budgets a completion message, and this is the only turn the owner gets for the entire build.

## M10 — If the run is unattended

Three deltas, and no others. The contract — mandate, run state, phases, witnesses, DoD, keepalive, landing — is
`memory/guides/UNATTENDED-PROTOCOL.md`, deliberately not paraphrased here.

- **Nobody reads the transcript.** Speak only when it changes what happens next: a refusal, an abort, a park, the
  wrap-up. Anything you would have said goes to a file — a park to the run-state file, a decision to the spec, a
  finding to a review record. **Never ask:** there is nobody to answer, so a question is a stall. The substitutes
  are derive, park and abort; Step 5b says which one per exit.
- **The keepalive is yours on both ends** — the store is in-memory and session-scoped, so no script can reach it.
  Create it before preflight, reap it before the wrap-up. Both halves: protocol §5.
- **A directive recorded as waived at preflight is relaxed for that run only.** The vocabulary, the waiver act,
  its record and what it cannot reach are protocol §10.

## M11 — Where everything else lives — read these, do not restate them

The carriers, what each owns, and when to load it: **`tools/memory-tree/README.md`, section "The method's
pointer table"**. The six are `skills/session-kickoff/SKILL.md`, `memory/TEMPLATE-SPEC.md`,
`memory/guides/REVIEW-PROTOCOL.md`, `memory/HYGIENE.md`, the governance template with its companion, and
`memory/guides/UNATTENDED-PROTOCOL.md`. Names here, scopes there — one hop, and this file stays re-readable.

*The memory root is spelled `memory/` throughout; an adopter whose `MEMORY_ROOT` differs renames it here, the same
caveat `HYGIENE.template.md` carries.*

## M12 — Research, test, choose — when the solution is not given

Reached from M5's "no existing seam fits", and only there. A build whose specs already name a solution passes
through unchanged; one started from an owner's prose does not, because nobody has chosen yet.

**This adds no PASS kind.** M6's set is closed and neither research nor testing is in it. The work happens INSIDE
the passes that set does name — it is what "a spec authored" costs when the spec must decide between candidates
first — and under a mandate the run occupies the `RESEARCHING` and `TESTING` positions while doing it. Commit
boundaries and reground points stay exactly where M6 and M7 put them.

**Find CANDIDATES, plural.** One candidate is not a choice, it is the first idea with a record attached. Two or
three differing in MECHANISM is the shape; stop where a further candidate would differ only in detail. "Only one
mechanism exists here" is a legitimate answer to RECORD, never a quota to fill — and it is a claim, so it owes the
same evidence a pick does.

**TEST before choosing, and test what DISCRIMINATES.** A candidate is tested by the smallest artifact that could
refute it — a probe, a fixture, a measurement against the real tree — never by argument, and never by a test every
candidate passes. Write down what would make each candidate LOSE before running anything: a test whose result
cannot change the pick is not a test, it is a rehearsal. A test that cannot fail is the same defect the merge bar
is full of gates against, one level up.

**Choose by M3's rule**, which already governs picking among options: the most feature-rich survivor after
M3's vetoes, tie-broken by fewer open questions and then by reuse of a seam M5 found. M3's limit on your
authority holds here too, and M3 is the one place it is stated.

**Record the LOSS, not just the win.** §10 already names the seam and the recall terms; this section adds one thing
to it — for each candidate tested and rejected, the test that rejected it. A rejected candidate with no recorded
test is indistinguishable from one nobody tried, and the next build pays to re-run it.
