# TOOL-aBoundedVerdict-14 — an adversarial round after the first reviews the fold, not the build

**Status:** SPECCED · rev-3 · 2026-08-19 · node c · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

A second closing review re-reads the entire cumulative diff, including every fix the first round
produced, because the review harness carries no round number, no prior-findings input and no
narrowing — and the build method tells the caller to pass the run's pinned BASE every time. Scope
round N to the fold round N-1 introduced, and hand it what round N-1 already confirmed.

## 2. Scope (IN)

- **S1** — `tier2-review.js` accepts `args.priorFindings`: the confirmed findings of the preceding
  round, as an array of objects carrying at least a ref and a claim. It reaches every finder lens as
  its own labelled section, distinct from `byDesign`.
- **S2** — `tier2-review.js` accepts `args.round` (an integer, default 1) and states it in the report
  and in every lens brief, so a finder knows whether it is reading a build or a fold.
- **S3** — the harness REFUSES a `base` that is not an immutable sha when `round > 1`, and warns on
  one at round 1. The default `origin/main` is a moving ref, which the method forbids two paragraphs
  above the invocation it documents; a string check enforces it without the harness needing repo
  access, which it does not have.
- **S4** — the report names the resolved base AND the tip, both as shas, so round N+1 has an
  immutable scope boundary to read. Today the harness instructs `${base}...${head}` where `head`
  defaults to the literal `HEAD` (`tier2-review.js:66`) — a moving ref recorded as provenance, and
  that is the defect. **Rev-2 corrects rev-1's supporting measurement**, which was false in its
  load-bearing half: ELEVEN records do name a `sha..sha` range, so "none names a usable tip" is
  refuted. What holds is that a HARNESS-written record pins a moving ref by default, and that no
  record's tip is derivable when it does.
- **S5** — `BUILD-METHOD.md` M8 gains the fix-round invocation: round 1 from the run's pinned BASE to
  the tip; round N>1 from round N-1's recorded tip to the current tip, with round N-1's confirmed
  findings passed as `priorFindings`. **The bug-class checklist keeps the FULL range on every round**
  (`gotchas.py --for-diff <BASE>..HEAD`), per F3 — M8 must state the two scopes as two sentences, so
  the review narrowing cannot be read as narrowing the checklist. The existing sentence "re-review the FIX, not the diff again"
  becomes an instruction a caller can execute rather than an intention.
- **S6** — the synth-death hole is closed. Lens and skeptic deaths are counted and reported; a dead
  synthesis returns `report: null` with a `complete`-shaped note and every confirmed finding is lost
  with nothing logged. Mirror the existing guard: set an `UNVERIFIED:` note and `log()` the confirmed
  list so the findings survive in the transcript.
- **S7** — the harness's SYNTH PROMPT instructs the record's binding line, kind and ids included.
  **Rev-2 corrects rev-1's premise, which was wrong in both halves**: `grep -ni serves
  tools/workflows/tier2-review.js` returns nothing, so the harness writes no binding line at all —
  and it does not write the record either, it instructs the synth AGENT to write it (`:307`). So the
  work is a prompt change, and the observable is the agent's output. The line must carry BOTH a kind
  and at least one id: a kind with no id is MALFORMED under `memory/HYGIENE.md`'s grammar, so
  emitting `**Serves:** diff-review` alone would trade a missing line for an unparseable one. The
  FILENAME's id projection stays with M8's rename, which check 21's fourth branch also requires and
  which a harness with no repo access cannot perform.

## 3. Non-goals (OUT)

- Not the loop's exit rule, and not what a `BLOCKED` verdict means. Fold-scoping makes each round
  cheap and convergent; deciding when the loop STOPS and what happens to a residual blocker is
  `TOOL-aBoundedVerdict-1`. This unit is why that unit's convergence rule is affordable, and it is
  independently useful without it.
- Not the verdict vocabulary. A machine-readable verdict token is `TOOL-aBoundedVerdict-2`'s.
- Not the fan-out or concurrency caps. `memory/guides/REVIEW-PROTOCOL.md` owns both and this unit
  changes neither the lens count nor the verifier arity.
- Not the spec-audit path (M4). A spec audit is not run by this harness — the harness reviews diffs
  with code-shaped lenses and cannot be pointed at a document — so nothing here touches M4's loop.
- No new workflow harness, and no second review script. The two knobs this unit needs already exist
  as parameters; what is missing is that they are never filled.
- Not a change to how a review record is NAMED. The round already appears in the filename grammar,
  and `memory/HYGIENE.md` owns it.

## 4. Design

### Data model

Two new `args` keys and one refusal, on a harness that already parses `args` defensively:

```
{ repo, base, head, round: <int, default 1>,
  priorFindings: [ { ref, claim, severity? }, … ],
  context, byDesign, reviewDir }
```

`priorFindings` is deliberately NOT merged into `byDesign`. They are different instructions: `byDesign`
says *this is intended, do not report it*, while a prior finding says *this was reported and fixed —
check the fix, and do not re-raise the original*. Collapsing them loses the second half, which is the
half this unit exists for. The audit measured `byDesign` supplied by no caller anywhere in the tree,
so smuggling the brief through it would put load-bearing content in a field with a zero-use history.

### The scope boundary, and where it comes from

Round N's base is round N-1's TIP. That value has to be readable, and today it is not: `head` defaults
to the literal `HEAD` and the report records `<base>...HEAD`, so a later round reading that record
learns nothing. S4 makes the harness resolve and record both endpoints, which is what turns "review
the fold" from an instruction into a derivation.

The harness cannot run git — it has no filesystem access, which its own comments state. So S3's
enforcement is a STRING check on the shape of what it was handed, not a resolution. That is enough to
convert a silent wrong-scope into a loud refusal, and it is the whole mechanism: the caller resolves,
the harness refuses anything that does not look resolved.

### Inventory

| Concern | Today | After |
|---|---|---|
| round N>1's diff | the whole cumulative diff, fixes included | round N-1's tip to HEAD |
| what round N knows of round N-1 | nothing | its confirmed findings, in a labelled section |
| the round number | absent from the harness entirely | an argument, stated in every brief and the report |
| a moving-ref base | silently accepted, and the default | refused at round > 1, warned at round 1 |
| the recorded range | `<base>...HEAD` | two shas |
| a dead synthesis | `report: null`, note reads complete, findings lost | `UNVERIFIED:` note, findings logged |
| the record's `**Serves:**` | no kind token; check 21 reds until hand-edited | written with `diff-review` |

### Migration

None on disk, and no existing review record is rewritten. A caller that passes neither new key gets
today's behaviour with one difference: a moving-ref `base` now warns. That is deliberate — the 25
records naming a range are history, and S4 changes only what is written from here.

One honest limit, stated because a later reader will ask: this unit cannot make round 2 of a review
that has ALREADY happened fold-scoped. The tip it would need was never recorded. Every build in the
corpus with multiple rounds keeps its full-diff rounds as history.

### Rollout

S6 and S7 first — they are independent of the fold work, and S7 removes a manual step from every
closing review immediately. Then S1-S4 in the harness. S5 last, because the method must not instruct
an invocation the harness does not yet accept.

### Files touched (estimate)

`tools/workflows/tier2-review.js` (two args, one refusal, the lens brief, the report line, the synth
guard, the `Serves:` kind) · `memory/guides/BUILD-METHOD.md` M8 and
`tools/memory-tree/BUILD-METHOD.template.md` (S5, both halves — the kit/dogfood parity leg compares
them) · `tools/workflows/check-workflow-syntax.js` is a gate, not a change ·
`memory/map/features/build-method.md` (the dossier claims the fix-round invocation) ·
`memory/backlog/TOOL.md` (`TOOL-aLoosenedCeiling-6` closes on S7).

### Alternatives rejected

- **Pass the prior findings through `byDesign`.** Rejected in Data model: it conflates two
  instructions and loses the one that matters.
- **Have the harness resolve the shas itself.** Rejected on capability, not taste: the script has no
  filesystem or repo access. An agent could be spawned to resolve them, which costs an agent per
  review to compute two values the caller already holds.
- **Derive round N's base from the review RECORDS on disk.** Rejected for the reason
  `TOOL-aBoundedVerdict-1` rejected counting rounds from records: every filename evasion is legal, the
  sequence is unbounded, and a family-qualified record is ambiguous with a unit id. Also circular —
  the tip is missing from those records, which is what S4 fixes.
- **Make `round` mandatory.** Rejected: every existing caller omits it, and a mandatory field turns a
  compatible improvement into a breaking change for a harness other builds invoke.
- **Scope round N with `git diff` pathspecs limited to the files round N-1's findings named.** A
  narrower fold still, and rejected: a fix legitimately touches files no finding named, and a pathspec
  scope would hide exactly the collateral the fold review exists to catch.

## 5. Production-readiness checklist

- **security** — `priorFindings` content reaches an agent prompt verbatim. It originates from this
  repo's own prior round rather than from an external surface, so it is not an injection boundary; it
  is worth one review look that a finding's text cannot terminate the brief's own delimiters.
- **perf / scale** — strictly cheaper. A fold-scoped round reads a smaller diff. `priorFindings` adds
  a bounded number of lines to each lens prompt.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — the empty `priorFindings` case is round 1 and must read as
  "none", never as an empty section implying the prior round found nothing. S6 is the error-state half.
- **observability** — S2 puts the round in the report; S4 puts two shas there; S6 stops a dead synth
  reporting as a clean one.
- **risks** — the real one is a fold-scoped round MISSING a defect that only shows against the full
  diff — a fix that is locally right and globally wrong. Mitigation is that round 1 is always full-diff
  from the pinned BASE, so the whole diff is reviewed exactly once, and the fold rounds review what
  round 1 could not have seen. That reasoning belongs in M8 and is written there by S5.
- **testing + left-shift gates** — `check-workflow-syntax.js` and `check-verifier-fanout.sh` already
  gate the harness's source; neither can see an argument that is never filled, so the left-shift for
  THIS class is S3's refusal, which fails loudly at the call rather than silently in the scope.
- **migration / rollback** — none on disk; revert is the two args.
- **user docs** — M8 in both halves, and the build-method dossier.

## 6. Acceptance criteria

- **AC1** — When `tier2-review.js` is invoked with `round: 2` and a `base` of `origin/main`, it throws
  a refusal naming the moving ref; with an immutable sha it proceeds. Two arms.
- **AC2** — When invoked with `priorFindings`, every finder lens prompt contains a section labelled for
  prior findings, distinct from the `BY DESIGN` section — asserted by reading the constructed prompt in
  a harness-level arm rather than by running a review.
- **AC3** — When the report is written, its opening range line names two shas and contains no literal
  `HEAD` — the observation that gives round N+1 a boundary to read.
- **AC4** — When the synthesis agent returns null, the harness's return value carries a note beginning
  `UNVERIFIED:` and the confirmed findings appear in the `log()` stream; against the shipped harness the
  note reads as a completed run.
- **AC5** — When a review is run end to end, the record the synth agent writes opens with a
  `**Serves:**` line containing `diff-review` AND at least one id, and
  `bash tools/memory-tree/check-memory-hygiene.sh` check 21 is clean over it once M8's rename has
  been performed. Rev-2: the rename stays a hand step — check 21's fourth branch requires the
  FILENAME to project an id, and the harness has no repo access to rename anything.
- **AC6** — When `memory/guides/BUILD-METHOD.md` and
  `tools/memory-tree/BUILD-METHOD.template.md` are compared, M8's fix-round invocation is present and
  byte-identical in both, and `bash tools/memory-tree/kit-dogfood-parity.test.sh` is clean.
- **AC7** — When `node tools/workflows/check-workflow-syntax.js tools/workflows/tier2-review.js` and
  `bash tools/workflows/check-verifier-fanout.sh` run after the change, both are clean — the arity and
  parse rules are unaffected by the new arguments.
- **AC8** — When a two-round review is run end to end on a scratch branch, round 2's `git diff` command
  names round 1's recorded tip as its base, observed in round 2's own report under
  `memory/builds/<slug>/reviews/`.

## 7. Gates

`bash tools/run-gates/run-gates.sh` whole, and specifically: `review-harness gates`
(`tools/workflows/check-workflow-syntax.js`, `tools/workflows/check-review-join.sh`) ·
`verifier fan-out` (`tools/workflows/check-verifier-fanout.sh`) · `memory/` hygiene check 21 ·
`kit/dogfood doc parity` (`tools/memory-tree/kit-dogfood-parity.test.sh`) ·
`codebase-map coverage + freshness` · `kit version markers`.

## 8. Open questions

- **F1 — is `round` an integer the caller passes, or does the harness infer it from `priorFindings`
  being non-empty?** Inference costs no argument and is right in every case anyone will actually run.
  An explicit integer is readable in the report and lets round 3 say three. **Recommendation: accept
  the integer, and infer `round: 2` when `priorFindings` is non-empty and `round` is absent** — so a
  caller cannot silently get a round-1 brief while handing over prior findings.
  RESOLVED (agent, 2026-08-19, delegated): both, as recommended. Mechanism-only fork; the inference is
  what stops the two arguments disagreeing.

- **F2 — does S3 refuse a short sha?** `base` is joined on by `closing-review-recorded` at a 7-char
  floor, and git's default abbreviation here is 7. A 40-hex requirement would refuse the spelling the
  corpus actually uses. **Recommendation: require 7+ hex and nothing but hex** — the same floor the
  driver's join already uses, for the same measured reason.

- **F3 — should a fold-scoped round N re-run the bug-class checklist over the fold range only, or
  over the full range?** M8 runs `gotchas.py --for-diff` as the lens brief before the review.
  RESOLVED (owner, 2026-08-19): **the FULL range, `BASE..HEAD`, on every round.** So the review scope
  narrows to the fold and the checklist scope does not, which is deliberate asymmetry rather than an
  inconsistency: a class the fold REINTRODUCES stays selected even when the fold's own files would not
  select it, and `gotchas.py` is stdlib and seconds, so the round pays almost nothing for it. S5 states
  both scopes explicitly, in one sentence each, because a reader who sees only "round N reviews the
  fold" will otherwise narrow the checklist too.

## 9. Revision log

- rev-2 · 2026-08-19 · folded the M4 spec audit. **S7's premise was wrong in both halves**: the
  harness writes no binding line at all rather than a kind-less one, and it does not write the record
  — it instructs the synth agent to. So the change is to the prompt and the observable is the agent's
  output; and the line must carry a kind AND an id, because a kind alone is malformed under the
  binding grammar. AC5 is rewritten and the filename rename stays with M8, which check 21 also
  requires and a harness with no repo access cannot do. **S4's measurement is corrected**: eleven
  records DO name a sha-to-sha range, refuting rev-1's "none names a usable tip". The defect that
  survives is the harness default writing the literal `HEAD`.
- rev-1 · 2026-08-19 · initial draft. Derived from the owner's third report and from the close-path
  audit's highs 23 and 22, plus `TOOL-aLoosenedCeiling-6` from the TOOL backlog, which S7 closes. F1
  and F2 resolved under the delegated fork rule; F3 raised to the owner as a scope fork.

- rev-3 · 2026-08-19 · F3 resolved by the owner: the bug-class checklist keeps the FULL `BASE..HEAD`
  range on every round while the review narrows to the fold. S5 now states both scopes explicitly,
  because the asymmetry is deliberate and a reader who sees only the narrowing will apply it to both.
  The grounds: a class the fold reintroduces stays selected even when the fold's own files would not
  select it, and the probe is stdlib and seconds.

## 10. Reuse audit

The seams are the harness's own existing parameters, and naming them is what makes this unit small:
`args.base` and `args.byDesign` are already parsed, already validated defensively, and already reach
every lens — `tools/workflows/tier2-review.js:65-71` and `:156-158`. Nothing new is built in the
fan-out, the join, or the report path. The synth guard in S6 is a copy of the guard the same file
already applies to its finder and skeptic stages, cited in its own comments as S1 and S2 of
`TOOL-aGuardedTally-1`.

The second seam is `memory/HYGIENE.md`'s record-binding grammar, whose closed `<kind>` set already
contains `diff-review` — S7 writes an existing token rather than inventing one.

Recall terms used, at the SET level for this build: `closing review round cap blocked verdict
adversarial diff fold unattended close build-complete DoD stall halt`. The pass returned
`REVIEW-PROTOCOL.md` and `agent-cap.topLevelArgs` as the review-adjacent seams, both of which this
unit deliberately does not touch (§3).
