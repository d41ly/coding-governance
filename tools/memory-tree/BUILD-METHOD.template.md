<!-- gov:kit memory-tree@2.19 -->
# The build method — how a multi-pass build runs

## M1 — What this is

Binding for any build of more than one pass, attended or not. Template §1 defines a READY unit and a DONE unit;
this is the middle. It is a PROCEDURE — nothing here grades a run, and the merge bar is `{{TOOL_ROOT}}run-gates.sh`.
**Budget: ≤20 KB, ≤250 lines** (`memory/HYGIENE.md` rule 6); it grows only by DISPLACEMENT, because M7 re-reads it
WHOLE at every pass boundary and a method too expensive to re-read is skipped exactly when it is needed.

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
`memory/builds/<slug>/spec/`. **The README's `ids:` key is NOT a roster** — it is a reservation range written as
ranges and unions (`<FAMILY>-<slug>-1..-9`), and reading it as a unit list silently drops every unit after the first. A
unit's spec is the file under `spec/` whose status header carries the id. Shape, tiers and sub-spec form are
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
diverge, change the spec first (rev bump + §9 line), then code.

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

**What is delegated.** A standing mandate delegates the owner's resolver authority for the named build only, and
only for forks the specs already state. It does not delegate SCOPE: a fork whose options differ in *what gets built*
is not yours — park it. With no mandate, forks go to the owner and this section is preparation.

**Ratify the most FEATURE-RICH option** — most stated acceptance criteria satisfied, fewest follow-ups left open —
after these vetoes, in order. Discard any option that:

1. fails an acceptance criterion or gate already written in the spec, or violates a §3 Non-goal;
2. needs a new external dependency, install location, public surface, or a change to a governance carrier;
3. widens a security, data or write surface beyond what the unit's risk tier priced.

Vetoes 2 and 3 are owner turns. Tie-break: fewer open questions, then reuse of a seam M5 found. **No survivors →
park**, never the least-bad option.

**Mark it in place** per `memory/TEMPLATE-SPEC.md` §8, naming resolver and authority, never `(owner, …)` for a
decision the owner did not make. **Keep §8's first non-blank line machine-legal** (`none — the forks below are
RESOLVED …`): the hygiene gate reads that line and nothing else, so without it the spec reds the moment its status
goes CLOSED.

## M4 — The spec audit — review every unreviewed spec before its code

**Which.** Every spec with no review record naming it. A spec whose rev moved since its last review, or that you
authored this run, is unreviewed.

**Not the harness.** `{{TOOL_ROOT}}workflows/tier2-review.js` reviews DIFFS with code-shaped lenses. It cannot be
pointed at a document, and calling a spec "reviewed" by it is false.

**Run it as a `Workflow` script, not as direct `Agent` spawns.** The direct-spawn budget is keyed per PROMPT TURN
and an unattended run has no next user prompt to reset it: three specs audited by direct spawns exhaust it mid-set,
and the remaining lenses are refused with nobody to read the refusal. Agents inside a `Workflow` sidechain are not
counted against it. Shape: `memory/guides/REVIEW-PROTOCOL.md` — primed lenses → batched skeptics defaulting to
REFUTE → one synthesis — **under its fan-out and concurrency caps, read there and not repeated here.**

**Lenses: 3–5, primed with the mandate, the overview and the spec format.** The catalogue —
underspecification, contradiction, unstated assumption, prior art — with what each hunts, is in
`{{KIT_DIR}}/README.md`.

**Record it** under `memory/builds/<slug>/reviews/` per `memory/HYGIENE.md` check 5's filename grammar, opening with
the literal line `## Verdict: CLEAN` — or `CLEAN WITH FIXES`, or `BLOCKED`. Most existing review records carry no
verdict line; write it anyway, because M9 derives from these records. **Carry the binding line** check 21 requires —
`**Serves:** spec-audit <the ids you reviewed>` — which is what makes "every spec with no review record naming it"
answerable from the tree instead of from memory. Grammar: `memory/HYGIENE.md`, "Record bindings". **Fold fixes into the spec** (rev bump + §9
line), then **STOP**: once a synthesis pass calls the design clean, stop reviewing that spec.

## M5 — Recall and reuse

The obligation is `memory/TEMPLATE-SPEC.md` §10 and is machine-checked there. Satisfy it once for the SET, not per
spec, in this order — map dossier first, decision records second:

```bash
python {{TOOL_ROOT}}codebase-map/reuse_lookup.py "<behaviour phrase, not a symbol name>"
python {{TOOL_ROOT}}memory-recall/query.py "<question in plain English>" --terms "<8-14 words in this corpus's jargon>"
```

The recall CLI is offline and cannot coin terms — you write them, 8–14, or it exits 2 saying so. **Write into the
spec's §10** the seam you will extend, cited by path, or an explicit "no existing seam fits" with the evidence —
**and the recall terms you used**, because composing them is the expensive half and M7 re-runs the query.

Two rules you cannot afford to look up: **a probe exits 0 on a miss**, so "nothing found" is an ANSWER to record,
never a failure to retry with softer words; and **a hit can be STALE**, so verify any claim about current code
against source before building on it and say in §10 where the two disagreed. The rest of the probe-failure
taxonomy — blind layers, absent tools, which phrasing to try next — is in `{{KIT_DIR}}/README.md`.

## M6 — Passes, commits, parallelism

**A PASS is exactly one of:** a spec authored · a spec reviewed · a review's fixes folded in · a unit built · the
closing diff review. Nothing else is a pass.

**Commit at the end of every pass**, on the run's branch, with the unit id in the subject. Then run the bug-class
checklist over what you just committed, and act on it before the next pass begins:

```bash
python {{KIT_DIR}}/gotchas.py --for-diff HEAD~1..HEAD
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

**Sequence is the default; parallelism is a claim you substantiate.** Two passes run concurrently only if: (1) their
WRITE sets — actual paths, written down before dispatch — do not intersect; (2) neither writes a file the other
reads as a contract (conf, template, interface, generator input) or as an acceptance input, and neither depends on
the other's output either way; (3) neither touches a shared mutable record — `memory/DECISIONS.md`,
`memory/backlog/*.md`, the build README, the run-state file, or any generated index with its generator. If you
cannot write both path lists down, the work is not known to be disjoint — sequence it. The fan-out and concurrency
CEILINGS are `memory/guides/REVIEW-PROTOCOL.md`'s; this is about WHICH work is parallel, never HOW MUCH.

## M7 — Regrounding

You cannot observe your own compaction — do not try. **Reground at every pass boundary, unconditionally.** A commit
is something you perform; regrounding always is cheaper than the one rebuild caused by a boundary crossed blind.

Self-probe, two questions you must answer without scrolling back: *the current unit's id and what its §6 Acceptance
says*, and *the phase and its witness*. If either is not already in your head, you are regrounding whether or not
anything was compacted. Read in this order, and nothing else:

1. `git log --oneline -5` — under a mandate, `bash {{TOOL_ROOT}}unattended/unattended.sh --resume <slug>`.
2. The build's authored record whole (under a mandate `memory/builds/<slug>/RUN.md`, which survived compaction and
   process death where your context did not) — mandate, phase, witness, parked entries.
3. **This file, whole.** It is capped so this stays cheap.
4. The CURRENT sub-spec, whole — that one, not the set, which was read in M2 and is on disk.
5. Re-run the recall probe with the terms recorded in that spec's §10.

Then continue. **Regrounding never re-opens a resolved fork and never re-reviews a clean spec** — the §8 marks and
the review records outrank your recollection. Keep passes small: a compaction landing mid-pass is not caught until the next boundary.

## M8 — Closing the build

Bug classes FIRST — run the M6 checklist over `<BASE>..HEAD`; its output is a lens brief for the review, not a
report filed after it. Then ONE adversarial review of the cumulative diff, from the run's pinned BASE (an immutable
sha, never a moving ref) to the tip. Per-pass reviews do not substitute: they re-scan overlapping code and never see
the seam between two passes.

```
Workflow { scriptPath: '{{TOOL_ROOT}}workflows/tier2-review.js',
           args: { repo: '<abs repo path>', base: '<BASE sha>', head: 'HEAD',
                   reviewDir: 'memory/builds/<slug>/reviews' } }
```

**Pass `reviewDir` explicitly** — its default is repo-root-relative and writes the report outside the memory tree,
where nothing indexes it. The harness names the file it wrote: **rename it to `memory/HYGIENE.md` check 5's
recording grammar before the next gate run**, or check 5 reds on a free-named file. A closing review is a
`diff-review`, not a `spec-audit`: give it `**Serves:** diff-review <every id in the diff>` and do not let it stand
in for the per-spec pass M4 owns — the two answer different questions and only one of them is about a design.

Fix every blocker, then re-review the FIX, not the diff again. A blocker unfixable inside the mandate's scope is a
park, not a waiver, and its unit does not close. Left-shift every confirmed finding — a regression gate, or a
`memory/gotchas/` class when the class cannot be gated; a finding fixed and not left-shifted returns. **Landing** —
merge and push authorization, the lander, the bypass ban, conflict reconciliation — is template §1 Landing and
`memory/guides/UNATTENDED-PROTOCOL.md`.

## M9 — The wrap-up — a derivation, not a recollection

Composed last, read first, after every fact is on disk. **Derive each row. If you cannot name the file a line came
from, the line does not go in.**

| item | derived from |
|---|---|
| build log and slug | `memory/builds/<slug>/` + generated `memory/LIVE.md` and `memory/ledger/<month>.md` |
| decisions taken | every §8 `RESOLVED` mark across the spec set (M3) + the `memory/DECISIONS.md` rows this build minted |
| problems resolved | each review record's `## Verdict` line and its blockers/highs (M4, M8) + the bug classes the checklist selected |
| open / parked | every parked entry in the authored record (M6) with question, options and reason, plus any recorded DoD override |
| repo state | branch · shas · gate verdict · under a mandate the phase claim and its witness |

**Completeness test, the only one that matters:** every row has a source on disk. A field you cannot cite a source
for is not "unknown" — it is work that did not happen, and *that* is the line the wrap-up leads with. **Format is
template §16's** — payload first, ONE state block at the bottom — but its routine-completion length budget does not
apply: §16 budgets a completion message, and this is the only turn the owner gets for the entire build.

## M10 — If the run is unattended

Two deltas, and no others. The contract — mandate, run state, phases, witnesses, DoD, keepalive, landing — is
`memory/guides/UNATTENDED-PROTOCOL.md`, deliberately not paraphrased here.

- **Nobody reads the transcript.** Speak only when it changes what happens next: a refusal, an abort, a park, the
  wrap-up. Anything you would have said goes to a file — a park to the run-state file, a decision to the spec, a
  finding to a review record. **Never ask:** there is nobody to answer, so a question is a stall. The substitutes
  are derive, park and abort; Step 5b says which one per exit.
- **The keepalive is yours on both ends** — the store is in-memory and session-scoped, so no script can reach it.
  Create it before preflight, reap it before the wrap-up. Both halves: protocol §5.

## M11 — Where everything else lives — read these, do not restate them

The carriers, what each owns, and when to load it: **`{{KIT_DIR}}/README.md`, section "The method's
pointer table"**. The six are `skills/session-kickoff/SKILL.md`, `memory/TEMPLATE-SPEC.md`,
`memory/guides/REVIEW-PROTOCOL.md`, `memory/HYGIENE.md`, the governance template with its companion, and
`memory/guides/UNATTENDED-PROTOCOL.md`. Names here, scopes there — one hop, and this file stays re-readable.

*The memory root is spelled `memory/` throughout; an adopter whose `MEMORY_ROOT` differs renames it here, the same
caveat `HYGIENE.template.md` carries.*
