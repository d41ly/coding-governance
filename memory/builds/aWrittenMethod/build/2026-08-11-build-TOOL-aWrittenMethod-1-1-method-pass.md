# Design pass 2 — the method draft, before trimming

**Serves:** journal TOOL-aWrittenMethod-1

**What this is:** the draft build-method text produced by design pass 2, kept verbatim as the CONTENT
SOURCE for `TOOL-aWrittenMethod-1` S1. The spec's job is to trim this to the S1 budget and render it;
this file is what "trimmed to budget" is measured against, and the spec's AC0 grades the rendered
guide against it.

**What it is NOT:** the deliverable. The deliverable is
`tools/memory-tree/BUILD-METHOD.template.md` and its render at `memory/guides/BUILD-METHOD.md`. This
draft is un-trimmed, spells paths literally rather than as template placeholders, and carries seven
defects the pass-2 adversarial stage found and the spec folds as B1 through B7. Do not copy it into
the template unchanged.

**Measured at capture:** 240 lines, 17,282 bytes. The S1 budget is 220 lines and 15,000 bytes on the
RENDERED copy, so roughly 20 lines and 2,300 bytes come out. The named spill target for anything
worth keeping but not worth the budget is `tools/memory-tree/README.md`, which is outside the hygiene
index set.

The sections below are the draft as produced. Section numbering M1 through M11 is the draft's own.

---

<!-- rendered by tools/memory-tree/adopt-memory-tree.sh from BUILD-METHOD.template.md — do not hand-edit -->
# The build method — how a multi-pass build runs

## M1 — What this is

Binding for any build of more than one pass, attended or not. Template §1 defines a READY unit and a DONE unit; this
is the middle. It is a PROCEDURE — nothing here grades a run; the merge bar is `bash tools/run-gates.sh` and this file
does not change it. **Budget: ≤20 KB, ≤250 lines** (`memory/HYGIENE.md` rule 6 caps this file). It grows only by
DISPLACEMENT — M7 re-reads it WHOLE at every pass boundary, and a method too expensive to re-read is skipped exactly
when it is needed.

**Reading the references.** `M<n>` is a section of THIS file; `§<n>` is always a section of another document — a
spec's, the template's, the protocol's. **The one rule about this file.** Nothing here is stated anywhere else in this
repo; every generic obligation is POINTED AT via M11. A rule appearing both here and in an M11 carrier is a defect
HERE — delete it here. Drift resolves by deletion, not adjudication.

**The loop.** Classify the spec set (M2) → ground it with the two probes (M5) → close it: author MISSING, thicken
THIN, resolve every fork (M2, M3) → review every unreviewed spec (M4) → build in passes, committing and regrounding at
each boundary (M6, M7) → review the cumulative diff (M8) → derive the wrap-up (M9). Everything before "build in
passes" precedes the first line of code, and a reground never re-runs it: re-running re-opens closed forks.

## M2 — The spec set — detect, classify, act

**Detect.** The roster is the ids in `memory/builds/<slug>/README.md`'s overview (unattended: and in the mandate). A
unit's spec is the conforming file under that build's `spec/` whose status header carries the id. Spec shape, tiers,
sub-spec form: `memory/TEMPLATE-SPEC.md`. Rebuild the roster after any fork resolution that adds a unit.

**Classify, first match wins.** Write it into the build README before acting on it.

1. **MISSING** — no conforming spec carries the id.
2. **THIN** — §2 Scope, §6 Acceptance or §7 Gates is empty, a placeholder, or names nothing observable.
3. **FORKED** — §8 Open questions carries an unresolved item.
4. **READY** — none of the above, and §10 Reuse audit is filled where the format requires it.

**Act.**

- **MISSING → author the spec, then re-classify.** *Authoring a spec is allowed:* the rule that a run may not write
  its own mandate is about AUTHORIZATION — the mandate is the authorization, the spec is the WORK. Write it at the
  tier `.claude/SESSION-KICKOFF.md` assigns, same slug, same folder. A spec you wrote this run is unreviewed by
  definition (M4).
- **THIN → fill it as a `rev-N` bump on the existing file**, with its §9 line. Never open a second file for a unit
  that already has one — that is how a spec set stops agreeing with itself.
- **FORKED → M3.**
- **READY → build what it says.** To diverge, change the spec first (rev bump + §9 line), then code.

**Hard floor.** If ACCEPTANCE or GATES cannot be *derived* from the goal, the code or the prior records, the unit is
not buildable: park it (M6), set BLOCKED, continue with the set — the kickoff engine's Step 5b exit 5 applied per
unit, and there is no second posture. Never build a MISSING or THIN unit; "I will spec it afterwards" is the same act
with the record written last.

**Sub-specs must AGREE with the main spec.** Before the first code pass, cross-read on four axes: **scope** (nothing a
sub-spec puts IN is OUT in the overview or a sibling) · **interface** (any name, path, signature or config key spelled
twice is spelled identically) · **ordering** (no sub-spec depends on a unit sequenced after it) · **acceptance** (the
overview's is implied by the union of the sub-specs', no orphan clause either side). A disagreement is a defect in
exactly ONE document: fix that one, bump its rev, name what disagreed in its §9 line. Never build the intersection,
and never let code arbitrate between two specs. A disagreement that is a choice rather than an error is a fork (M3).
*Judgment, not procedure: this is a read you perform and its only trace is the §9 line.*

## M3 — Forks — the decision rule, and the limit of your authority

Sweep §8 across the whole set before any code, including forks M2 just created. Resolved mid-build is a rewrite;
resolved before it, a decision.

**What is delegated.** A standing mandate delegates the owner's resolver authority for the named build only, and only
for forks the specs already state. It does not delegate SCOPE: a fork whose options differ in *what gets built* is not
yours — park it. With no mandate, forks go to the owner and this section is preparation.

**Ratify the most FEATURE-RICH option** — most stated acceptance criteria satisfied, fewest follow-ups left open —
after these vetoes, in order. Discard any option that:

1. fails an acceptance criterion or a gate already written in the spec, or violates a §3 Non-goal;
2. needs a new external dependency, install location, public surface, or a change to a governance carrier;
3. widens a security, data or write surface beyond what the unit's risk tier priced.

Vetoes 2 and 3 are owner turns. Tie-break: fewer open questions, then reuse of a seam M5 found. **No survivors →
park** — never the least-bad option. *Judgment, not procedure: vetoes 2 and 3 are what a run under token pressure
reads generously; park is the brake.*

**Mark it in place** per `memory/TEMPLATE-SPEC.md` §8, naming resolver and authority — `RESOLVED (agent, <date>, per
<mandate-ref>): <pick>`, never `(owner, …)` for a decision the owner did not make. **Keep §8's first non-blank line
machine-legal** (`none — the forks below are RESOLVED …`): the hygiene gate reads that line and nothing else, so
without it the spec reds the moment its status goes CLOSED.

## M4 — The spec audit — review every unreviewed spec before its code

**Which.** Every spec with no review record naming it. A spec whose rev moved since its last review is unreviewed
again. A spec you authored this run is unreviewed.

**Not the harness.** `tools/workflows/tier2-review.js` reviews DIFFS — fixed diff command, code-shaped lenses. It
cannot be pointed at a document, and calling a spec "reviewed" by it is false. Run this by hand in the shape
`memory/guides/REVIEW-PROTOCOL.md` defines — primed lenses → batched skeptics defaulting to REFUTE → one synthesis —
**under its fan-out and concurrency caps, read there and not repeated here.**

**Lenses (3–5), primed with the mandate, the overview and the spec format:** **underspecification** (which §2 item has
no §6 criterion; which §6 criterion names no observation) · **contradiction** (§2 vs §3; sub-spec vs main spec on M2's
four axes; §4 Design vs §7 Gates) · **unstated assumption** (what must be true of existing code for §4 to work that §4
never says and §10 never checked) · **prior art** (has a record already decided this — recall probe, M5).

**Record it** under `memory/builds/<slug>/reviews/` per `memory/HYGIENE.md` check 5's filename grammar, opening with
the literal line `## Verdict: CLEAN` — or `CLEAN WITH FIXES`, or `BLOCKED`. Most existing review records here carry no
verdict line; write it anyway, because M9 derives from these records and a wrap-up that must re-read every review is a
wrap-up written from memory.

**Fold fixes into the spec** (rev bump + §9 line), then **STOP** — once a synthesis pass calls the design clean, stop
reviewing that spec.

## M5 — Recall and reuse

The obligation is `memory/TEMPLATE-SPEC.md` §10 and is machine-checked there. This is how to satisfy it — once for the
SET, not per spec, in this order:

```bash
python tools/codebase-map/reuse_lookup.py "<behaviour phrase, not a symbol name>"
python tools/memory-recall/query.py "<question in plain English>" --terms "<8-14 words in this corpus's jargon>"
```

Map dossier first, decision records second (kickoff Step 4's order). The recall CLI is offline and cannot coin terms —
you write them, 8–14, or it exits 2 saying so. **Write into the spec's §10:** the seam you will extend, cited by path,
or an explicit "no existing seam fits" with the evidence — **and the recall terms you used.** Composing terms is the
expensive half of the probe, M7 re-runs the query after a compaction, and terms nobody wrote down are re-derived worse
each time. (§10 is their home: the run-state file's authored region is closed to derivable facts.)

**Never read a probe's exit status as a verdict — these exit 0 on a miss.** A clean "nothing found" is an ANSWER:
record it as the no-seam evidence and do NOT re-run the probe with softer words until it says something. A
partial-recall or blind-layer notice means the probe cannot see that layer at all — here **bash is recall-dark**, so
the gates, adopters and hooks that ARE the product never surface as seams; `grep` that layer specifically and say so
in §10. A miss on one phrasing is not absence: try the behaviour, then the artifact noun, once. An absent tool does
not remove the obligation — grep the tree and the nearest record, and write in §10 what you did instead. Extend the
seam you found; a second implementation is justified in §10, before the code.

## M6 — Passes, commits, parallelism

**A PASS is exactly one of:** a spec authored · a spec reviewed · a review's fixes folded in · a unit built · the
closing diff review. Nothing else is a pass.

**Commit at the end of every pass**, on the run's branch, with the unit id in the subject. Before each commit run
`python tools/memory-tree/gotchas.py --for-diff <pass-base>..HEAD`. Its stdout IS the checklist and it always exits 0
— finish it, do not read its status. Then the diff-scoped gates for what the pass touched; the full bar runs ONCE, at
the push boundary. A pass whose gate is red is not followed by another: fix it, or park it with the reason. A pass
that produced no change commits nothing and says so.

**Parking, at any point.** Write the *question*, the *options you saw*, and the *reason you refused* into the build's
authored record. A bare "parked" is indistinguishable from "forgotten", and M9 is where the owner gets the turn you
did not take.

**Sequence is the default; parallelism is a claim you substantiate.** Two passes run concurrently only if:

1. their WRITE sets — actual paths, written down before dispatch — do not intersect;
2. neither writes a file the other reads as a contract (conf, template, interface, generator input) or as an
  acceptance input, and neither depends on the other's output in either direction;
3. neither touches a shared mutable record: `memory/DECISIONS.md`, `memory/backlog/*.md`, the build README, the
  run-state file, or any generated index together with its generator.

If you cannot write both path lists down, the work is not known to be disjoint — sequence it. The fan-out and
concurrency CEILINGS are `memory/guides/REVIEW-PROTOCOL.md`'s; this section is about WHICH work is parallel, never HOW
MUCH.

## M7 — Regrounding

You cannot observe your own compaction — do not try. **Reground at every pass boundary, unconditionally.** A commit is
something you perform; regrounding always is cheaper than the one rebuild caused by a boundary crossed blind.

Self-probe, two questions you must answer without scrolling back: *the current unit's id and what its §6 Acceptance
says*, and *the phase and its witness*. If either is not already in your head, you are regrounding whether or not
anything was compacted. Read in this order, and nothing else:

1. `git log --oneline -5` — under a mandate, `bash tools/unattended/unattended.sh --resume <slug>`.
2. The build's authored record whole (under a mandate `memory/builds/<slug>/RUN.md`: it survived compaction and
  process death, your context did not) — mandate, phase, witness, parked entries.
3. **This file, whole.** It is capped so this stays cheap.
4. The CURRENT sub-spec, whole — that one, not the set. The set was read in M2 and is on disk.
5. Re-run the recall probe with the terms recorded in that spec's §10.

Then continue. **Regrounding never re-opens a resolved fork and never re-reviews a clean spec** — the §8 marks and the
review records outrank your recollection. *Honest limit: a compaction landing mid-pass is not caught until the next
boundary. Keep passes small; that is the only mitigation.*

## M8 — Closing the build

Bug classes FIRST — run the M6 checklist over `<BASE>..HEAD`; its output is a lens brief for the review, not a report
filed after it. Then ONE adversarial review of the cumulative diff, from the run's pinned BASE (an immutable sha,
never a moving ref) to the tip. Per-pass reviews do not substitute: they re-scan overlapping code and never see the
seam between two passes.

```
Workflow { scriptPath: 'tools/workflows/tier2-review.js',
           args: { repo: '<abs repo path>', base: '<BASE sha>', head: 'HEAD',
                   reviewDir: 'memory/builds/<slug>/reviews' } }
```

**Pass `reviewDir` explicitly** — its default is repo-root-relative and writes the report outside the memory tree,
where nothing indexes it.

Fix every blocker, then re-review the FIX, not the diff again. A blocker unfixable inside the mandate's scope is a
park, not a waiver, and its unit does not close. Left-shift every confirmed finding — a regression gate, or a
`memory/gotchas/` class when the class cannot be gated; a finding fixed and not left-shifted returns. **Landing** —
merge and push authorization, the lander, the bypass ban, conflict reconciliation — is template §1 Landing and
`memory/guides/UNATTENDED-PROTOCOL.md`, not restated here.

## M9 — The wrap-up — a derivation, not a recollection

Composed last, read first, after every fact is on disk. **Derive each row. If you cannot name the file a line came
from, the line does not go in.**

| item | derived from |
|---|---|
| build log and slug | `memory/builds/<slug>/` + generated `memory/LIVE.md` and `memory/ledger/<month>.md`; under a mandate `RUN.md`'s generated region is already a byte-compared copy of that slice |
| decisions taken | every §8 `RESOLVED` mark across the spec set (M3) + the `memory/DECISIONS.md` rows this build minted |
| problems resolved | each review record's `## Verdict` line and its blockers/highs (M4, M8) + the bug classes the checklist selected |
| open / parked | every parked entry in the authored record (M6) with question, options and reason — plus any recorded DoD override with its item and reason |
| repo state | branch · shas · gate verdict · under a mandate the phase claim and its witness (`--status <slug>`) |

**Completeness test, the only one that matters:** every row has a source on disk. A field you cannot cite a source for
is not "unknown" — it is work that did not happen, and *that* is the line the wrap-up leads with. **Format is template
§16's** — payload first, ONE state block at the bottom — but **its routine-completion length budget does not apply
here:** §16 budgets a completion message, and this is the only turn the owner gets for the entire build. Ordering
binds; length does not.

## M10 — If the run is unattended

Two deltas, and no others. The contract — mandate, run state, phases, witnesses, DoD, keepalive, landing — is
`memory/guides/UNATTENDED-PROTOCOL.md`, deliberately not paraphrased here.

- **Nobody reads the transcript.** Speak only when it changes what happens next: a refusal, an abort, a park, the
  wrap-up. Anything you would have said to the owner goes to a file — a park to the run-state file, a decision to the
  spec, a finding to a review record. **Never ask:** there is nobody to answer, so a question is a stall. The
  substitutes are derive, park, abort; the kickoff engine's Step 5b says which one per exit, and there is no fourth.
- **The keepalive is yours on both ends** — the store is in-memory and session-scoped, so no script can reach it.
  Create it before preflight, reap it before the wrap-up. Both halves: protocol §5.

## M11 — Where everything else lives — read these, do not restate them

- `skills/session-kickoff/SKILL.md` + `.claude/SESSION-KICKOFF.md` — starting a unit, closed scope, the tier rule, the
  six interactive exits.
- `memory/TEMPLATE-SPEC.md` — spec sections, tiers, sub-spec form, the §8 mark grammar, the §10 reuse audit.
- `memory/guides/REVIEW-PROTOCOL.md` — the fan-out and concurrency caps, find→verify→synthesize, the stop rule.
- `memory/HYGIENE.md` — record placement, filename grammar, size budgets, the status vocabulary.
- `parallel-coding-governance.template.md` §1, §7, §8, §16 + `…domain-rules.md` §7, §10, §12 — DoR, DoD, landing, gate
  discipline, diff-scoping, the final-message format.
- `memory/guides/UNATTENDED-PROTOCOL.md` — mandate, run state, phases and witnesses, DoD, keepalive, landing.
