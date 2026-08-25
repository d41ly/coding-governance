**Serves:** none — research that precedes the spec set; no unit of this build exists yet

# Research — one review harness for every review kind a build needs

*Node `d` · 2026-08-25 · HEAD `2ddd0db8` (`git rev-parse HEAD`) · branch
`branch/review-harness-improvements-16b470` · tree
`C:/projects/coding-governance/.claude/worktrees/playbook-mode-unattended-kit-550410`.
Research only: nothing in the repo was edited, no spec was written, no rule was changed. Every figure
below names the command that derived it; where a probe found nothing, the empty result is the answer.*

---

## Verdict

**Yes, with a named cost.** One harness can drive every review kind a build needs, because 83% of the
shipped engine already does not know what a diff is — the diff binding is 67 of 400 non-blank lines,
and 55 of those 67 are three contiguous regions, two of which are pure data. The named cost is that
three things genuinely resist parameterisation and need design, not a knob: the base-must-be-a-sha
predicate, the finding schema's integer `line`, and a verdict-plus-blocker return the engine asks its
synthesis agent for and then never reads.

**Recommended first: P1 — give `tools/workflows/tier2-review.js` a subject descriptor.** Same file,
same name, same seven trust counters on every exit path, one new `args` field carrying the kind, the
acquire sentence, the lens profile, the anchor predicate and the record-kind token. P2 (read the
`blockers` field and instruct the `## Verdict:` line) is smaller still, independently valuable, and
is the prerequisite for anything that drives the convergence loop — it can land first and alone.

---

## The measurement

### The population, and which kind the kit actually serves

| figure | value | command |
|---|---|---|
| tracked review records under `reviews/` | 156 | `git ls-files "memory/builds/*/reviews/*.md" \| wc -l` |
| build folders | 65 | `ls memory/builds/ \| wc -l` |
| kind split under `reviews/` | spec-audit 82 · diff-review 73 · journal 1 · unbound 0 | `python tools/memory-tree/gen_build_index.py --print-bindings \| awk -F'\t' '$2 ~ /\/reviews\//{print $3}' \| sort \| uniq -c` |
| kind split over ALL bound records | spec-audit 83 · diff-review 73 · journal 68 · research 20 · unbound 1 | same command without the `reviews/` filter |

The parse comes from the shipped parser, not a grep, and that matters: a whole-file grep over-counts,
because body text quotes the binding grammar. The `absent` bucket under `reviews/` is empty, so there
is no unclassified residue and the kind field is already a reliable join key.

The 83rd spec-audit record lives outside `reviews/`, at
`memory/builds/dScaffoldedMirror/build/2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md`.
The one `journal` under `reviews/` is
`memory/builds/dUnstalledConvoy/reviews/2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md`.

**The kit ships an engine for the minority kind and forbids it for the majority.** Spec audits
outnumber diff reviews 83 to 73. `memory/guides/BUILD-METHOD.md:113` is the whole of the prohibition:
"**Not the harness.** `tier2-review.js` reviews DIFFS; a spec is not code, so calling one reviewed by
it is false."

### Degradation by kind — the honest version, which is weaker than it first reads

I swept the 156 records for two signals with `scratchpad/deg.py` (whitespace-normalised, head-only
kind classification replicating `gen_build_index.py`). Results:

- **A stage of the run's own fan died: 3 records, all `spec-audit`, denominator 83.**
  `memory/builds/aSiftedPlaybook/reviews/2026-08-16-review-PLAY-aSiftedPlaybook-1-1.md` (seven of
  eight agents), `memory/builds/aBoundedVerdict/reviews/2026-08-16-review-TOOL-aBoundedVerdict-1-2.md`
  (six of nine), and
  `memory/builds/aRuledFrontispiece/reviews/2026-08-17-review-TOOL-aRuledFrontispiece-1-2.md`
  (the synthesis pass). Zero `diff-review` records, denominator 73.
- **Findings survived into the record with no skeptic verdict: 1 spec-audit and 1 diff-review.**
  `aSiftedPlaybook…-1-1.md` declares nine unverified; a `diff-review`,
  `memory/builds/dUnstalledConvoy/reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-fix.md:8`,
  declares "raw 24, confirmed 19, refuted 0, unverified 5".

**A claim that "every degraded review run in this corpus is a spec audit" does not survive its own
criterion, and this research withdraws it.** Under agent death the split is 3/0; under unjudged
findings it is 1/1. Pick one criterion and the picture is either narrow or even. The diff-review
instance also closed its own gap — the record says the five were re-read against the tree and every
one collapsed into a cluster a skeptic had already confirmed.

**The predicate itself is brittle, and I record that rather than hiding it.** My first regex missed
`aSiftedPlaybook`'s death sentence because the phrase was line-wrapped in the source, and it
false-positived on `aBoundedVerdict…-1.md` where "Six of nine highs" describes findings, not agents.
Both were fixed by hand adjudication, which is exactly why this figure is a floor and not a rate: a
hand-driven run has no machinery that forces the declaration, so a silent degradation is invisible to
any such probe by construction.

### The decisive measurement — program-emitted vs gate-enforced vs remembered

Restricting to records dated on or after `2026-08-11` — the day the M4 rule landed, per
`git log -S'Not the harness' --format='%h %ad' --date=short -- memory/guides/BUILD-METHOD.md`, which
returns `a3833757 2026-08-11` — and running `scratchpad/shape2.py`, whose predicates are spelled in
the file:

```
  records dated >= 2026-08-11 : {'diff-review': 60, 'journal': 1, 'spec-audit': 63}

  field                        spec-audit             diff-review
  review shape phrase           10/63  ( 16%)       53/60  ( 88%)
  raw+confirmed+refuted         12/63  ( 19%)       48/60  ( 80%)
  unverified counter            14/63  ( 22%)       48/60  ( 80%)
  precision figure              17/63  ( 27%)       46/60  ( 77%)
  sha...sha range                3/63  (  5%)       45/60  ( 75%)
  lens/skeptic death count       7/63  ( 11%)        1/60  (  2%)
  ## Verdict: line (GATED)      58/63  ( 92%)       49/60  ( 82%)
```

**The two helper scripts live in session scratch and are NOT tracked**, so the predicates are spelled
here rather than left behind a path that will not resolve. Kind classification in both is head-only:
the `**Serves:** <kind>` line taken from the first 12 unfenced lines, replicating
`gen_build_index.py`. The seven field predicates, applied to the whole file, case-insensitive:
`review shape` · `raw\s+\d+.{0,40}confirmed\s+\d+.{0,40}refuted\s+\d+` (dot-matches-newline) ·
`unverified\s+\d+` · `precision\s+[01]\.\d\d` ·
`\b[0-9a-f]{7,40}\.\.\.?[0-9a-f]{7,40}\b` or the same against `HEAD` ·
`lenses?\s*(dead|died)` or `skeptics?\s*(dead|died)` or `\d+\s*/\s*\d+\s*lenses` ·
`^## Verdict:` multiline. The degradation sweep normalises whitespace before matching, which is what
made it catch a line-wrapped death sentence the first attempt missed.

Every field in rows 1–5 is one the harness's synthesis prompt mandates —
`tools/workflows/tier2-review.js:342` ("State the review shape near the top — raw … precision") and
`:349` ("Open the report with a line naming the reviewed range as `${base}...${head}`"). The one field
with a **machine gate** is the last: hygiene check 22, `REVIEW_VERDICT_CUTOFF="2026-08-22"` at
`.memory-tree.conf:79`, enforced in `tools/memory-tree/check-memory-hygiene.sh`.

**The gap inverts on the gated field.** 92% against 82%, the only row where spec audits lead. So the
deficit in rows 1–5 is not that spec audits are written by less careful sessions. It is exactly this:

- a field a **program emits** → present 77–88%
- a field a **gate enforces** → present 82–92%, on both kinds
- a field only a **document asks a human to remember** → present 5–27%

Date is not the confound: only 6 of the 156 records predate August
(`git ls-files "memory/builds/*/reviews/*.md" | grep -cE '/2026-0[1-7]-'`).

Row 6 deserves its own sentence, because it cuts the other way and is the more honest reading of the
whole table: lens and skeptic mortality is reported in 11% of spec audits and **2%** of diff reviews.
The harness computes that accounting into its `note` return field
(`tools/workflows/tier2-review.js:406-415`), and the record writers overwhelmingly do not transcribe
it. So the engine's trust accounting is currently reaching the caller and dying there.

### What is NOT separated by kind

`scratchpad/wf/prec.py` (a prior lens pass, re-derived independently during verification): 43 builds
carry at least one spec-audit record over 83 records, mean 1.93 rounds, max 6; 33 builds carry at least
one diff-review record over 73 records, mean 2.21, max 10. **Rounds-needed does not separate the
kinds, and what difference exists runs against the suspicion** — diff reviews average more rounds. Do
not claim hand-driven reviews need more rounds. Do not claim they find fewer real bugs either: the
stated-precision gap (spec-audit ~0.69 over the ~29% that report a figure at all, diff-review ~0.80) is
computed over a self-selected sample of the more disciplined spec-audit runs, and is not evidence.

Exactly one record in 156 declares itself unusable, and it is a spec audit:
`memory/builds/aSiftedPlaybook/reviews/2026-08-16-review-PLAY-aSiftedPlaybook-1-1.md:7`.

### What one degraded spec audit cost

That record planned four primed lenses, three batched skeptics and one synthesis. Seven of its eight
agents died **on a weekly usage limit** (`:8-9`) — not on a bug in the script. One lens returned 18
findings; the orchestrator hand-verified 9 and left 9 unverified (`:14`). It carries a section headed
`## Owed — this is not optional coverage` (`:53`) and forbids any spec in the set going INPROGRESS on
its strength (`:68-70`). It was replaced by a fresh eight-agent run, `…-1-2.md:7`: "64 raw findings,
52 confirmed, 12 refuted, 0 unverified. This is the coverage round 1 could not buy."

Byte proxy for the waste, from `ls -la memory/builds/aSiftedPlaybook/reviews/`: round 1 is 5846 bytes
against round 2's 40662 — about 14% of the payload of the round that replaced it. **The token figure
for this run is not on disk**; a grep for `token` over the round-1 record returns nothing. The
corpus's own anchors price an eight-agent fan at roughly 1.3–2 M subagent tokens
(`memory/builds/aFusedCharter/reviews/2026-08-18-review-PLAY-aFusedCharter-1-1.md:7` — 7 agents,
1.33 M; `…-1-2.md:5` — 7 agents, 1.45 M;
`memory/builds/aTetheredRecord/build/2026-08-16-build-aTetheredRecord-1-design-pass.md:9` — 13 agents,
2.13 M). "Millions of tokens" is consistent with those anchors. The specific figure is not established.

**A correction to this build's own framing, which must be carried into any spec.** The owner's brief
says a session "introduced a bug which led to the review being discarded". The record says an
environment limit, and the orchestrator **detected and reported the degradation correctly** by hand.
A repo-wide search for a recorded bug in a hand-written review script finds nothing: the only nearby
hit is `memory/builds/aMooredAnchor/build/2026-08-11-build-TOOL-aMooredAnchor-1-1-repro.md:16`, about
a fixture-reproduction harness. Pitching this build as "sessions write buggy review scripts" will be
refuted by the first person who reads the record. The evidence that *does* hold is cost, fragility,
and the structural incompleteness the table above measures — plus the shipped-kit regression below,
which is strictly stronger.

---

## What the ban actually costs

### The engine is 83% subject-blind already

Derived at HEAD `2ddd0db8` with a clean file (`git status --porcelain tools/workflows/tier2-review.js`
empty). `wc -l tools/workflows/tier2-review.js` → 416.
`grep -c '^[[:space:]]*$' tools/workflows/tier2-review.js` → 16, so non-blank is 400. Column A is the
declared range set `28-29 65-66 68 80-95 97 103 156-177 182 184 192 194 243 343-359`, summed by
`awk '{s+=$2-$1+1} END{print s}'` → **67**. No blank falls inside an A range, so B = 400 − 67 = **333**.

| | non-blank lines | share |
|---|---|---|
| A — bytes that must change for a non-diff subject | 67 | 16.8% |
| B — subject-agnostic machinery | 333 | 83.2% |

**The diff binding is not spread through the engine.** Three contiguous regions are 55 of the 67:
the lens catalogue `:156-177` (22 lines, pure data), the synthesis provenance and binding paragraph
`:343-359` (17 lines, of which the kind token is one), and the base-must-be-a-sha check `:80-95`
(16 lines, the only genuine predicate). The residual 12 are single strings: the doc comment `:28-29`,
`base`/`head` `:65-66`, the context default `:68`, `diffCmd` `:97`, the pre-spawn log `:103`, four
finder-prompt clauses `:182 :184 :192 :194`, and the skeptic instruction `:243`.

**The harness never reads a diff.** `:97` builds a *string*, `const diffCmd = git -C ${repo} diff
${base}...${head}`, and `:182` interpolates it into a prompt — the script has no filesystem, stated
three times in its own source (`:81`, `:98-100`, `:347`). So `BUILD-METHOD.md:113` is a statement
about the engine's **prompts and finding schema**, and is false of its **machinery**.

**The engine has no concept of a review kind at all.** `grep -rn "spec-audit" tools/workflows/` exits
1 with no output. `git grep -n "diff-review" -- tools/workflows/` returns exactly one line,
`tools/workflows/tier2-review.js:357`, inside a prompt string. No variable holds it, no argument sets
it, no branch selects it. Adding a kind is not refactoring an abstraction — it is introducing the
first one, into surrounding tooling that is already kind-aware (`memory/HYGIENE.md:266` declares the
closed set, `tools/memory-tree/gen_build_index.py:383` parses it, `tools/unattended/unattended.sh`
refuses a run whose only review is a spec audit).

### The hard-won invariants a hand-written driver starts without

Every row is cited from the source comment that records it. Every one lives in Column B.

| Invariant | Lines | Born from | The defect, in the source's own words |
|---|---|---|---|
| args-must-be-an-object guard | `:32-60` | S5 / `TOOL-aGuardedTally-1` | a prose `args` string degraded to `repo = '.'`; "twice made this harness audit a DIFFERENT repository … and return confident, well-evidenced findings about code nobody asked about" |
| …its own first cut | `:38-40` | same | the guard tested `typeof a !== 'object'`, but `args` arrives as a STRING; it "refused every legitimate caller" |
| `priorFindings` kept out of `byDesign` | `:70-76` | S1/S2 / `TOOL-aBoundedVerdict-14` | collapsing the two loses the half that says "this was reported and FIXED — judge the fix" |
| round inference | `:77-79` | F1 | prior findings arriving with no `round` gave a fold a round-1 brief |
| base-must-be-a-sha | `:80-95` | S3, F2 | the default is the moving ref `origin/main`; provenance that "points at whatever main happened to be" |
| **integer-keyed verdict join** | `:128-134`, `:270-283` | U6 / `TOOL-aFoldedQuarry-2` | echo drift dropped findings from the count, and two findings at one `file:line` collapsed so BOTH inherited the last verdict |
| **dead-lens counting** | `:201-206` | S1 / `TOOL-aGuardedTally-1` | "a review returned `clean: 0 findings` with agents_done 0, four ENOTFOUND errors" — a review that reviewed nothing and reported clean |
| **dead-skeptic counting + unverified-is-not-refuted** | `:256-262`, `:285-298` | S2/AC4 | "an all-skeptics-dead run returned `all findings refuted` at precision 0.00 with lensesDead 0" |
| spurious / duplicate / conflict counters | `:270-281` | U6 | a hallucinated id rewrote a real finding's verdict; a disagreeing repeat now demotes to UNVERIFIED |
| fixed verifier count | `:229-238` | `REVIEW-PROTOCOL.md` rule | `chunk(allFindings, 5)` bounded group SIZE, "so 70 findings bought 14 skeptics — still linear" |
| bounded fan-out | `:13-20` | the concurrency rule | "a ~40-agent burst tripped the server rate limiter twice, ~3 M tokens wasted" |
| **report-anything-outstanding** | `:306-320` | U6/S7 | the old `judged === 0` early return "returned WITHOUT a report in exactly that case" |
| **synth-death hole** | `:377-386` | S6 / `TOOL-aBoundedVerdict-14` | "`synth === null` returned `report:null` with a note reading `complete` and every confirmed finding was lost with nothing logged" |
| trust counts on every exit | `:388-416` | H1 | "a caller that only ever sees `{confirmed, precision}` cannot tell a full review from one where half the lenses died" |
| the binding-line instruction | `:350-359` | S7 | before it, `grep -ni serves` over the file "returned NOTHING, so it wrote no binding line at all" |

Five of these are **false-clean** classes — a review that reviewed nothing, judged nothing, or lost
everything, while returning `clean` / `complete` / `all findings refuted`. Their failure mode is a
confident green report. The bold rows are those five.

The measured price of getting two of them wrong is on record at `memory/guides/REVIEW-PROTOCOL.md:27-31`:
one skeptic per finding cost 47 agents / 3.65 M subagent tokens against 9 / 0.81 M batched, and
upstream the same mistake at scale ran "six consecutive reviews of one spec at 79 / 54 / 48 / 37
agents, ~36 M subagent tokens".

### The strongest evidence is not hypothetical — the kit has already regressed this twice

`grep -nE 'lensesDead|skepticsDead|assignedIds|spurious|conflicts' tools/workflows/drift-audit-state.js
tools/workflows/drift-audit-code.js` exits 1 with **no output**. Both siblings run the identical
pipeline — `boundedParallel`, `chunk`, `MAX_VERIFIERS`, a lens fan, batched default-refute skeptics,
one synthesis — and neither carries the all-lenses-dead early return, the skeptic-death counter, the
assigned-id check on a verdict, the spurious/duplicate/conflict counters, or the synth-death guard.
Worse, `tools/workflows/drift-audit-state.js:378` returns `lensesRun: LENSES.map((L) => L.slug)` — the
**configured** set — so a dead lens is invisible to the caller, and `:387` returns
`report: synth && synth.path`, which says nothing when the synthesis dies.

**Three files in one directory implement one pipeline three times, and two of them are missing every
hardening the third has learned. The bar is green over all of it.** This is
`TOOL-dUnstalledConvoy-16` (`memory/backlog/TOOL.md:18`) — "a correction to a claim held by SEVERAL
carriers lands in one of them and nothing notices" — realised in executable code rather than prose.
The case for one engine does not need to speculate about per-session regressions.

---

## The review kinds a build needs

Derived by reading `memory/guides/BUILD-METHOD.md` (M1–M12), `memory/HYGIENE.md` and
`memory/TEMPLATE-SPEC.md` whole. The method imposes more review-shaped obligations than it names
review kinds; the ones with no record kind of their own are listed because a kit that "drives any kind
of review" has to decide whether they are in scope.

| Kind / obligation | Subject | Lens catalogue | Termination rule | Record kind | What the harness would need |
|---|---|---|---|---|---|
| **M4 spec audit** (`BUILD-METHOD.md:110-130`) | every spec with no review record naming it; a spec whose rev moved is unreviewed | 3–5, declared as PROSE at `tools/memory-tree/README.md:206-214`: underspecification · contradiction · unstated assumption · prior art | "Fold fixes into the spec (rev bump + §9 line), then **STOP**: once a synthesis pass calls the design clean" | `spec-audit` | a spec-path acquire sentence, the four-lens profile, a non-sha anchor predicate, the `spec-audit` token |
| **M8 diff review, round 1** (`:211-230`) | the cumulative diff `<BASE>...HEAD`, BASE an immutable sha | the shipped four, hardcoded at `tier2-review.js:156-177` | one round, then the fix loop | `diff-review` | nothing — this is what exists |
| **Fold review, round N>1** (`:214-215`) | round N−1's recorded tip, so it reads the fold rather than re-reading fixes | the same four; the only round-awareness is one prompt sentence at `:184` | the harness refuses an unpinned base above round 1 (`:85-95`) | `diff-review` — **no round axis exists** | a round field on the record, and the fold instructions the measurement named (read the body at HEAD, not the revision log; fold deletions rather than appending negations) |
| **Spec fold round** (implied by M4's rev rule) | the spec after the fold | unstated — M4 gives no round-N brief | see the seam below | `spec-audit`, byte-identical to round 1 | a reviewed-rev axis; the `rev-N` anchor does not match `/^[0-9a-f]{7,40}$/` |
| **M4 BLOCKED convergence loop** (`:132`) | the same spec or spec set again | unstated | "a round re-arms only if its confirmed-blocker count is STRICTLY SMALLER than the one before"; runaway ceiling backstops | `spec-audit` per round | **the confirmed-blocker count**, which the engine asks for and never reads |
| **M4 blocker promotion exit** (`:132`) | every blocker still standing | n/a | promoted to a unit, specced and built, "audited as a SPEC, which is what makes promotion terminate" | the promoted blocker becomes a spec; the promotion EVENT has no kind | the identities of the promoted set, which nothing records today |
| **M8 re-review-the-FIX** (`:232`) | the fix, not the diff again | unstated | "A blocker unfixable inside the mandate's scope is a park, not a waiver" | unstated; folded into the next `diff-review` | a subject that is a set of commits, not a range |
| **M2 classification sweep** (`:38-43`) | every spec — §2, §6, §7, §8, §10 | four predicates, first match wins | single pass, re-run after a fork adds a unit | none — written into the build README | in scope only if the kit wants to drive it |
| **M2 sub-spec cross-read** (`:60-65`) | every sub-spec against the overview and its siblings | four axes: scope · interface · ordering · acceptance | one pass, before the first code pass | none — "Nothing can check that you performed it" | same |
| **M3 fork sweep** (`:69`) | §8 of every spec | the veto ladder at `:78-82` | one pass, before any code | none — resolved in place in §8 | same |
| **M6 per-pass bug-class checklist** (`:165-172`) | `HEAD~1..HEAD` | whatever `python tools/memory-tree/gotchas.py --for-diff` selects | "its stdout IS the checklist and it always exits 0" | none | already a program; it is a lens BRIEF source, not a review |
| **M13-shaped research pass** (not in M-numbering) | documents and records | ad hoc per pass | ad hoc | `research` — 20 exist | already exercised through the batched shape twice, un-harnessed both times |

Three findings from this table matter more than the rest.

**A fold does not need a fifth kind.** `memory/HYGIENE.md:266-267` closes the vocabulary at
`spec-audit · diff-review · journal · research`, and a fold review genuinely reads whatever its subject
is. Measured on the one build that ran both loops to completion, `dFramedEntrypoint`: the round-1 and
round-2 spec-audit records carry **byte-identical** binding lines, and the three diff-review rounds
likewise. Adding `fold-review` would make one field answer two questions, which is this repo's own
`two-answers-to-one-question` class. What is missing is a **round** axis and a **reviewed-rev** axis.
The grammar already admits a trailing `@rev-N` (`memory/HYGIENE.md:270`), which is "recorded and never
validated" and used by exactly 1 of 156 records
(`grep -rlc '@rev-[0-9]' memory/builds/*/reviews/*.md | wc -l`).

**M4 contradicts itself at the fold seam, and only on one path.** `:110` says a spec whose rev moved
is unreviewed; `:129-130` says fold then STOP; `memory/TEMPLATE-SPEC.md:66` says `rev-<N>` bumps on any
material change, review fold-ins included. `:132` resolves it for the BLOCKED path — "Folding a
round's own fixes does not re-arm the loop — the fold is what the next round measures" — but `:110` was
never amended, so the selection rule still reads as a contradiction to anyone applying it literally.
**On a `CLEAN WITH FIXES` verdict there is no next round, so the fold text is measured by nothing.**
Two build READMEs record that as settled practice (`memory/builds/aBranchedMandate/README.md:228`,
`memory/builds/aPromptedMandate/README.md:97`: "The fold itself is unreviewed, by M4's stop rule").

**The fold is where the findings are, and the class is not in this repo.** The measurement lives in
machine-local auto-memory at
`C:/Users/d41ly/.claude/projects/C--projects-coding-governance/memory/fold-text-is-unreviewed-surface.md`:
on `dFramedEntrypoint`, round 2 returned 62 surviving findings of which 25 were created by the fold and
17 were the fold misreading its own finding — 42 of 62, against only 20 that round 1 had missed.
`ls memory/gotchas/ | grep -i fold` exits 1 with no output, and `ls memory/gotchas/*.md | wc -l`
returns 32. So `gotchas.py --for-diff`, which is the checklist M6 and M8 hand every reviewer, **cannot
emit the highest-value class discovered on the most recent build**, because the class does not exist
as a repo record.

**Nothing checks that a spec audit happened.** `DOD_CORE` at `tools/unattended/unattended.sh:249` holds
ten items and none is a spec-audit item. `tools/gate-legs.json` holds 85 legs
(`python -c "import json;print(len(json.load(open('tools/gate-legs.json'))))"`), of which nine mention
review/workflow/agent-cap/verifier and every one grades the harness or the record format, never
coverage. The only trace is a report-only line in a generated README region,
`tools/memory-tree/gen_build_index.py:769-778`, whose own comment concedes that "a spec audited at
rev-1 and since bumped does not appear here. An 'unreviewed' label would be a coverage claim the data
cannot support." **The one obligation `BUILD-METHOD.md:55` calls a hard floor has zero enforcement.**

---

## Constraints any design must fit

### The caps

The bounds live in `tools/hooks/agent-cap.js` and nowhere else; that file is the only authority and a
number restated beside it is the drift class this repo gates
(`tools/check-agent-cap-restatement.sh` bans a bound-word × number × noun in live markdown, and
`tools/check-playbook-parity.sh` machine-compares five pairs against it). **Read once on 2026-08-25 with
`grep -n '^const \(CAP\|MAX_VERIFIERS\|MAX_LENSES\|FIXED_MARK\)' tools/hooks/agent-cap.js`**, purely so
the shapes below are legible: `CAP` at `:55` = 5, `FIXED_MARK` at `:113`, `MAX_VERIFIERS` at `:114` = 5,
`MAX_LENSES` at `:119` = 5. Treat those digits as stale the moment this record is committed; the file
decides.

`CAP` is worth flagging separately: it decides nothing. Every verdict resolves through `boundedK`
against `MAX_VERIFIERS` or counts against `MAX_LENSES`, and `check-playbook-parity.sh:116` compares the
playbook's helper width against `MAX_VERIFIERS`, never against `CAP`. It is a fourth carrier of the
number that nothing machine-compares — a sixth parity pair candidate, or a deletion.

### The runtime

A workflow script has **no filesystem and cannot import**. Stated at
`tools/workflows/tier2-review.js:98-100`
("a probe was written, then removed rather than shipped unverified") and at
`memory/guides/REVIEW-PROTOCOL.md:146` ("scripts cannot `import`, so inline the helper"). Consequences,
and they are load-bearing for the proposals:

- **A lens catalogue cannot be read from a declaration file by the harness.** Everything the script
  branches on must arrive through `args`, as a string the script parses itself — `args` arrives as a
  STRING even when the caller hands it JSON (`tier2-review.js:37-40`).
- **A spawned agent DOES hold tools.** `:182` instructs a lens to run a shell command and then
  `Read`/`Grep`. So a kind's **prompt content** can live in a file a child reads; a kind's **fan-out
  shape** cannot, because the orchestrator has to size the array and the hook has to see the size in
  the source.
- **A sidechain agent holds no `Agent` tool at all** — measured 2026-08-15 and recorded at
  `memory/guides/REVIEW-PROTOCOL.md:97-103`, "The capability is ABSENT rather than unpoliced". So a
  design where the harness delegates a whole review kind to a child that runs its own lenses degrades
  to a single-agent review with no adversarial stage. This cannot be relaxed by policy.
- **A `Workflow` harness is the only shape that scales past a handful of agents unattended.** Direct
  spawns are budgeted per PROMPT TURN and an unattended run has no next prompt
  (`BUILD-METHOD.md:115-117`).

Also live at HEAD, and worth a spec line of its own: `tools/workflows/drift-audit-state.js:47` is
`const a = args || {}` with **no** `JSON.parse`, so handed a string it silently falls back to
`REPO = '.'` — the exact wrong-repository defect `tier2-review.js:32-40` was hardened against.

### The dialect the hook accepts

Re-run live against `tools/hooks/agent-cap.js` at HEAD `2ddd0db8`, piping a synthetic
`{tool_name:'Workflow', tool_input:{script}}` payload:

| Shape | Result |
|---|---|
| `const KINDS = {spec:[…], diff:[…]}; const LENSES = KINDS[args.kind]` | **rc=2, DENIED** — "fanned over `LENSES`, which this file does not show to be bounded" |
| `const LENSES = args.kind === 'spec' ? SPEC : DIFF // gov:fixed-verifiers` | **rc=0, ALLOWED** |
| `const LENSES = args.kind === 'spec' ? SPEC : args.customLenses // gov:fixed-verifiers` | **rc=0, ALLOWED** — see the hole below |
| `ALL.filter((L) => args.lenses.includes(L)) // gov:fixed-verifiers` | ALLOWED — the shape `tools/workflows/drift-audit-state.js:224` already ships |

**So a kind-parameterised harness is expressible in exactly one dialect: sibling top-level array
literals selected by a MARKED ternary or a MARKED `.filter`.** Any design that reaches for a map,
object or registry of lens sets is denied at the tool call and must be re-shaped before it can run at
all. That is the good failure mode, but it will look like the kit is broken, so it belongs in the spec.

Two further authoring traps, both OPEN backlog rows, both live: a trailing semicolon on the constant
declaration breaks the binder (`const CAP = 5;` denies, `const CAP = 5` passes — reproduced with two
files differing in one byte), and `tools/hooks/agent-cap.js` blesses an identifier bound from an EMPTY
array literal and never re-examines it (`TOOL-aCandidStub-1`, `memory/backlog/TOOL.md:51`).

**A live hole in the marked-derivation branch.** Row 3 above is a defeat: a `gov:fixed-verifiers`-marked
ternary whose OTHER branch is caller-supplied passes, letting an args-supplied array of any length reach
`agent()` once per element. The cause is that the branch accepts when *one* non-self reference is
bounded, so the other branch is never examined. This is the same defeat the `<expr> || <int>` binder
was deleted for — "a caller-settable knob wearing a constant's clothes". **If a design is built on the
marked-ternary dialect, it sits directly on top of this hole**, and tightening it should be part of the
same spec set. The growth form is correctly refused.

### The enforcement gap, demonstrated

The **only** mechanism in this repo that can see an ad-hoc, session-authored review harness is the
PreToolUse hook, and it reads the inline `script` string directly. Proven by running it, not inferred:
a payload carrying a three-line ad-hoc per-finding fan-out returns rc=2. Every file-scoped gate is
blind to that modality by construction —
`git ls-files --cached --others --exclude-standard -- '*.js' | grep -E '^tools/.*\.js$' | wc -l`
returns 7 of the 10 tracked-or-untracked `.js` files, and all three JS gates filter to that same
`^tools/.*\.js$` population. A script saved to `memory/builds/<slug>/` is invisible even when tracked.

**And the two enforcement points disagree.** A cap-compliant ad-hoc harness carrying four classic
review defects — a ref-keyed join, an uncounted `filter(Boolean)`, `refuted = total - confirmed`, no
unverified bucket — returns **rc=0 from the hook** and **rc=1 from
`tools/workflows/check-review-join.sh`**
on the identical bytes. Only the gate that cannot see inline scripts catches the defect.
`tools/workflows/check-verifier-fanout.sh:15-18` faces the same limit and *solves* it by delegating to
the hook, "which no file-scoped gate can ever see". `check-review-join.sh` has no such second entry
point, and `grep -n verdictByRef tools/hooks/agent-cap.js` exits 1.

**M4 forces every spec audit into the one modality the join gate is blind to**, and that gate's own
header says the class "has no runtime signal — a mis-keyed harness reports a clean bill".

### What a hook can and cannot additionally enforce, measured against the real tree

| Candidate predicate | Verdict |
|---|---|
| ref-keyed join ban | **READY TO LIFT.** The awk already exists in `check-review-join.sh:72-92`; it runs clean over the three shipped harnesses. A port, not a new predicate. Comment stripping is load-bearing — `tier2-review.js:256` necessarily SPELLS the banned expression while documenting it. |
| require an `unverified` token | **LOW FP, cheap.** All three harnesses carry it. Satisfiable by a comment, so weak — but not defeated by spelling. |
| uncounted `filter(Boolean)` | **MEASURABLE, and it REDS TWO SHIPPED HARNESSES.** Four of six code-level sites have no death count nearby, all four in the drift-audit siblings. Not false positives — live instances the original symptom never reached. "Counted" must mean the dropped count reaches a RETURNED field, or `drift-audit-code.js` passes on a log line. |
| ban `refuted = total - confirmed` | **HIGH FP as written.** The grep over `tools/**/*.js` returns exactly one hit and it is the comment documenting the retired defect. Invert to the whitelist above; a blacklist "bans a spelling and not the defect". |
| ban an early return with no report | **DO NOT ATTEMPT.** `tier2-review.js` has three legitimate `report: null` returns, each guarded by a semantic condition a static scan cannot evaluate. It would red the reference harness three times. |

### What a new gate leg costs

`tools/gate-legs.json` has **no ceiling field** — the key union across its 85 legs is exactly
`['argv', 'chunk', 'guard', 'impure', 'name', 'subject']`. Cost is measured and durable anyway:
`<git-dir>/gate-ledger.tsv` on this worktree holds 93 rows summing 5899.0 s, floored by a 2013.7 s
unattended shard. The nine review-area legs sum **50.188 s**, and the five whose `subject` is `repo`
sum **3.783 s**:

```sh
awk -F'\t' '$1=="review-protocol parity (kit vs dogfood)" || $1=="review-join ban (no ref-keyed join)" \
 || $1=="workflow script syntax" || $1=="agent-cap restatement" || $1=="verifier fan-out" \
 {s+=$2; n++} END{printf "%d legs  %.3f s\n", n, s}' "$(git rev-parse --git-dir)/gate-ledger.tsv"
```

A sub-second scanner does not move the bar. What a new leg does need: a `[[gate_leg]]` block in
`tools/workflows/kit.toml` **and** a matching row in `tools/gate-legs.json` with identical `subject`, a
`guard` decision (the three existing repo-subject scanners carry none, which is right for a scanner
whose subject is the repository), and **its failing case observed before it lands** — both sibling
scanners ship a self-test doing exactly that.

---

## Prior art — what is already ruled on

**1. `tier2-review-indexed.js` never existed here, and only its JOIN was ever wanted.**
`git log --all --oneline -- '*tier2-review-indexed*'` returns empty;
`git rev-list --all --objects | grep -i 'tier2-review'` returns 11 objects, every one named
`tools/workflows/tier2-review.js`. Adopting the upstream file wholesale was refused **three times**, on
one consistent ground: the incoming engine drops trust counters this harness already reports
(`memory/builds/aFoldedQuarry/spec/2026-08-08-spec-aFoldedQuarry-1.md:53-54`; the u6 unit spec `:56-57`
and `:121-123`; and
`memory/builds/aFerriedDossier/build/2026-08-16-build-aFerriedDossier-1-incms-adopter-handoff.md:116-118`).
**This is a price on any replacement engine, not a ban on generalisation.** Any replacement must carry
all seven counters on EVERY exit path or it is the same refusal on a different filename.

**2. Renaming `tier2-review.js` is refused.** Same spec, `:53-55`: `AGENTS.md`, `README.md` and
`WIRE-INTO-PROJECT.md` name it, and all three still do at HEAD.

**3. A flat round CAP was withdrawn by the owner on a 90-record measurement. Do not re-propose it.**
`memory/builds/aBoundedVerdict/build/2026-08-18-build-TOOL-aBoundedVerdict-1-review-loop-design.md`
supersedes a two-round cap "on the owner's instruction that the cap was the wrong move", after
measuring 90 records: BLOCKED 36, CLEAN WITH FIXES 6, **CLEAN 0**. "A cap does not give the loop an
exit; it relocates the stall from round 8 to round 2 … The cap is withdrawn as the mechanism."
Convergence plus promotion landed instead. **`memory/DECISIONS.md:68` is STALE against this** — it
still reads "the tier-2 review cap is TWO rounds per subject, a driver FILE CONSTANT". The log is
append-only, so this is expected mechanics; cite the design record and the CLOSED rev-13 spec, never
that row.

**4. The loop half already generalises across both kinds. Only the single-pass engine does not.**
`memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md:85-87` S5: "the SUBJECT is
the spec document for a method spec-audit round, and the BUILD SLUG for the method's closing diff
review. One predicate, two denominators." `tools/unattended/SKILL.template.md:483` says the same. The
convergence verb, the closed verdict vocabulary, the promotion rule, the runaway ceiling and the leg
that grades them are all kind-blind. **Re-proposing loop mechanics re-opens a settled design and
collides with an owner ratification.**

**5. The convergence loop is already implemented, gated and durable — as `unattended.sh --review`.**
`review_state()` is a four-state ladder (`0 → CONVERGED`; `count >= prev → NON-CONVERGENT`;
`n+1 >= ceiling → CEILING`; else `CONVERGING`) whose prior counts are DERIVED from the run-state line
set, so there is no round-count fact to parse. Three holes: it exists **only for unattended runs**
(`git ls-files "memory/builds/*/RUN*.md" | wc -l` returns 22, of which four carry a `review · item` row
— `aBoundedVerdict`, `dFramedEntrypoint`, `dScaffoldedMirror`, `dUnstalledConvoy` — against 156 review
records); the promoted SET has no identities, only a count, which the grading leg concedes in its own
comment; and the SUBJECT is free text at inconsistent granularity (`dFramedEntrypoint` ran one group
over eight specs while `dUnstalledConvoy` keyed on a single id). An unrecorded round hides exactly the
oscillation the predicate exists to catch: I ran the predicate directly and `5 → [2 unrecorded] → 4`
returns `CONVERGING` while `5 → 2 → 4` returns `NON-CONVERGENT`.
**And `BUILD-METHOD.md` M4 never mentions the verb that carries its own loop's state** —
`grep -n -- "--review\|--dispatch\|unattended.sh" memory/guides/BUILD-METHOD.md` returns exactly two
lines, `:185` and `:199`, both outside M4.

**6. The kit ALREADY ships a document-review harness.** `tools/workflows/drift-audit-state.js` is
versioned, gated and shipped; its subjects are the memory tree, `AGENTS.md`, `tools/gate-legs.json` and
`memory/LIVE.md`; and its lens set is a DATA LITERAL with a caller-side selector at `:224`:
`const LENSES = a.lenses && a.lenses.length ? ALL_LENSES.filter((L) =>
a.lenses.includes(L.slug)) : ALL_LENSES // gov:fixed-verifiers`.
It was added 2026-08-05, before the rule was written. **So "a review harness cannot be pointed at a
document" is FALSE of the kit and true only of one file in it.** The generalisation is not novel here;
it is unfinished.

**7. The M4 ban was never examined on merits.** It began as a documentation build's SCOPE exclusion
(`memory/builds/aWrittenMethod/spec/2026-08-11-spec-aWrittenMethod-1.md`, §3, alongside "No enforcement"
and "No new gate leg"). Its wording history via
`git log --oneline -S"Not the harness" -- memory/guides/BUILD-METHOD.md`: `a3833757` (2026-08-11)
PRESENT with a mechanism clause — "reviews DIFFS with code-shaped lenses. **It cannot be pointed at a
document**"; `ff913011` (2026-08-20) GONE, deleted rather than displaced; `570f8100` (2026-08-21)
restored but shortened to "a spec is not code", the mechanism clause dropped **with no recorded
decision**. The deletion was caught by an adversarial round (F11), not by a gate. Its one appearance as
a weighed alternative
(`memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md:355-357`) rests on a
present-tense capability claim: "The harness reviews diffs and cannot perform a method spec audit at
all." **A build proposing to change M4 is not overturning a considered ruling — it is the first pass to
examine it deliberately.** The rule at HEAD states a conclusion whose stated ground is a category
assertion that is not falsifiable, having replaced a mechanism claim that was.

**8. The batched shape has already driven a SPEC review successfully — cite the precision, not the
agent counts.** `memory/builds/aBatchedTribunal/spec/2026-08-09-spec-aBatchedTribunal-1.md:203`:
"Measured on this spec's own review: 18 confirmed / 20 raw, 0 unverified", by 5 batched skeptics.
**Do NOT cite "47 → 9 agents on a spec audit":** four carriers give two readings of which review that
pair measured, and a prior review already caught a mis-citation in the same passage
(`memory/builds/aUnmannedHelm/reviews/2026-08-10-review-TOOL-aUnmannedHelm-1-1.md:83`).

**9. The charter's "factory at instance #2" rule does NOT apply cleanly here, and a proposal that
claims it does will be refuted.** `AGENTS.md:303` instructs "Route Workflow fan-out through the bounded
helpers, **inlined because scripts cannot import**", and `:319` states the runtime constraint outright.
That is an on-record, reasoned instruction to duplicate exactly the helpers the three harnesses
duplicate. `AGENTS.md:365`'s per-kind map also names a different kind for this repo — "kits are the
kind". The one-engine argument must rest on the **measured** regression in prior art item 6/the
anatomy section, not on a §12 obligation.

**10. A shipped kit file cannot police a script that is never a file.**
`memory/archive/DECISIONS.2026-08-10.md:48` (`TOOL-aBatchedTribunal-1b`): "the enforcement point is the
`Workflow` TOOL CALL, not a file gate … the offending script was never a file and `tools/**/*.js` could
not contain it." **Shipping a better engine does not close the hole.** Say so plainly in any spec
rather than implying the engine is enforcement — that is exactly the class §7 of the charter calls a
structural check reading as a semantic one.

**11. Nothing in the corpus refuses generalisation on merits.** Probes:
`grep -rniE "review kind|kinds of review|subject kind|reviewKind|args\.kind" tools/ memory/` returns
four hits, all prose, none in code — no harness anywhere takes a review-kind parameter. Two
`memory-recall` queries over the decision corpus returned 40 hits each with no refusal on merits.
`grep -n "OPEN" memory/backlog/PLAY.md` and the same over `KICK.md`, filtered for review terms, return
nothing.

---

## The proposals

Ranked by value per unit of cost. Every one is a proposal, not a decision; the owner narrows.
No id of this build's own family is cited anywhere, because no spec defines one yet.

---

### P1 — A subject descriptor on the existing engine · **RECOMMENDED**

**What.** `tools/workflows/tier2-review.js` gains one `args` field carrying a review kind, and five
things become per-kind: the acquire sentence handed to the finders (a shell command for a diff, a
`Read` instruction for a spec set), the lens profile, the `context` default, the anchor predicate, and
the `**Serves:** <kind>` token at `:357`. Same file, same name, same seven counters, same exit paths.

**Cost.** Small and nameable. 55 of the 67 diff-bound lines are three regions and two of them are pure
data; the spec-audit lens catalogue already exists as prose at `tools/memory-tree/README.md:206-214`,
so the largest block is a copy job. Genuinely new work is three items: (a) the anchor predicate must
dispatch per kind — a spec's `rev-N` cannot match `/^[0-9a-f]{7,40}$/`, and the spec's own `base <sha8>`
would satisfy the check while proving nothing, which is a check that cannot fail; (b) the finding
schema needs an additive optional `where: {type:'string'}` for section-shaped addresses, because
`underspecification`'s whole finding is *the absence of a line*; (c) the lens array must be authored as
sibling literals with a marked selector, not a registry (see Constraints).

**Buys.** The measured 5–27% completeness on the majority kind becomes the 77–88% the minority already
has, for the price of one output-kind parameter. The seven trust counters stop being re-derived.
The record's kind token becomes program-emitted rather than hand-typed.

**Gate.** Auto-covered the day it lands, at zero new gate cost: `check-review-join.sh` scans every
`.js` under `tools/` with no marker filter, and `check-verifier-fanout.sh` plus
`check-workflow-syntax.js` both select on the `export const meta` marker the file already carries.
A new leg asserting the kind token is one of the closed four would be a sub-second `subject: repo`
scanner.

**Breaks.** `tools/unattended/unattended.sh`'s `closing-review-recorded` refuses a run whose only review
is a spec audit — "a spec audit cannot stand in for a closing review". An engine that can emit both
kinds must not blur that, and the spec must say so. Also five-plus version-marker sites per
`TOOL-aBoundedVerdict-29`, and the `{kit}/*.js` LF pin.

**Closes.** `TOOL-aDeclaredBound-6` (`memory/backlog/TOOL.md:144`) for free on any header rewrite —
verified live at HEAD: `:5` says "concurrency-capped (≤5)", `:154` says "ONE ≤6-wide wave", and the code
fans at the helper's default. The row's own line citation is stale (it says 128); fix both sites.

---

### P2 — Read the `blockers` count and instruct the `## Verdict:` line ·
**RECOMMENDED, can land first and alone**

**What.** Two edits. The synthesis prompt already asks for `{path, blockers, highs, summary}` at `:360`
and schemas them at `:369-370`; `required` at `:366` is `['path','summary']` and **neither count is ever
read** — `grep -n 'blockers\|highs' tools/workflows/tier2-review.js` returns 341, 360, 369, 370 and
nothing in the return block, which reads only `synth?.path` and `synth?.summary`. Make them required,
return them, and instruct the synthesis agent to open the record with the literal `## Verdict:` line
from the closed set.

**Cost.** One return field and one prompt sentence. This is the smallest change in the whole set.

**Buys.** The number M4's convergence loop is bounded by becomes readable off a run. Today the
strictly-smaller predicate is fed by a human typing a count into a park row. This is the prerequisite
for P4 and for any automated loop, and it is worth doing even if nothing else here is built.

**Gate.** Hygiene check 22 already grades the `## Verdict:` token forward-only from
`REVIEW_VERDICT_CUTOFF="2026-08-22"` (`.memory-tree.conf:79`). It states its own limit — "What it does
NOT check: whether the verdict is TRUE" — and that limit stays.

**Breaks.** Nothing. Making a schema property required could red a synthesis that omits it; the
existing synth-death guard already handles a null synthesis, so the failure is loud rather than silent.

**Closes.** No backlog row directly. It unblocks `TOOL-aBoundedVerdict-8` (`:120`), whose stated
precondition — cap, park verb and halt code all landed — is now met.

---

### P3 — The lens catalogue becomes declared data · **VIABLE**

**What.** Move the four M4 lens briefs out of `tools/memory-tree/README.md` prose and into a declaration
the caller passes through `args`, with the README rendering from it (or byte-compared against it) so
there is one text. The same treatment for the four diff lenses currently literal at `:156-177`.

**Cost.** Constrained by the runtime: the harness cannot read a file, so the catalogue reaches it as
`args`, and the ARRAY must still be sized in the source for the hook. A caller-side declaration plus
sibling literals whose briefs come from `args` satisfies both.

**Buys.** ~90 words stop being retyped per build. A grep for the four lens names across every
`.js`, `.py`, `.sh`, `.toml`, `.json` and `.conf` file in the tree
--include=*.js --include=*.py --include=*.sh --include=*.toml --include=*.json --include=*.conf .`
returns three hits, all incidental comment prose — **the catalogue reaches no program today.** It also
makes the catalogue gateable the way `tools/gate-legs.json` made the leg list gateable.

**Gate.** A parity leg comparing the declaration against the README, in the shape
`tools/workflows/check-protocol-parity.test.sh` already uses for `REVIEW-PROTOCOL.md`.

**Breaks.** `check-protocol-parity.test.sh` byte-compares `memory/guides/REVIEW-PROTOCOL.md` against its
shipped template and reds on any surviving `{{…}}`, so any protocol prose touched here needs a
same-commit re-render.

**Closes.** No backlog row.

---

### P4 — Drive the convergence LOOP, not just one pass · **VIABLE**

**What.** Two halves, and only one is new. (a) Give the attended path a home for the review row set —
today `verb_review` fails hard without a `RUN.md`, which exists only for unattended runs. (b) Add one
pointer line to M4 naming the verb that carries its own loop's state.

**Cost.** Far lower than the brief assumes: the predicate, the closed verdict vocabulary, the runaway
ceiling and the grading leg all exist and are self-tested. This is wiring, not a build. The genuinely
new part is (a), plus closing the three recorded holes — the promoted set has no identities, the
subject is free text at inconsistent granularity, and an unrecorded round hides an oscillation.

**Buys.** A driver that RUNS the rounds cannot skip recording one, knows the subject ids, and holds the
confirmed set — which closes all three holes structurally rather than by asking a human to remember.

**Gate.** `tools/unattended/check-unattended.sh` already grades the loop. Note its declared blind spot:
it is **skipped entirely** when the run-state file carries no `review` row — absence reads as clean,
which is the `fixture-passes-by-finding-nothing` shape applied to the loop's own gate.

**Breaks.** Re-opens nothing if scoped to a home and a pointer. **It DOES collide with a settled design
if it touches the predicate or proposes a round count** — see prior art items 3 and 4.

**Closes.** `TOOL-aBoundedVerdict-8` (`memory/backlog/TOOL.md:120`).

---

### P5 — Close the enforcement gap at the hook · **VIABLE, and the only lever that reaches the failure**

**What.** Lift `check-review-join.sh`'s awk predicate into `tools/hooks/agent-cap.js` (or a sibling
PreToolUse hook on the same matcher), and add the whitelist form — a script containing both `verdict`
and `agent(` must contain the token `unverified`. Optionally add the uncounted-`filter(Boolean)`
predicate, defined as "the dropped count reaches a RETURNED field".

**Cost.** The join predicate is a port of a working awk, not a new invention, and it runs clean over
the three shipped harnesses. Comment stripping is mandatory and already solved there. The
`filter(Boolean)` predicate is the hardest to define precisely and would red two shipped harnesses on
first run — correctly, per the section above, which is a reason to wire it and fix them, not a reason
to skip it.

**Buys.** This is the **only** mechanism that reaches a hand-rolled driver. A shipped engine makes the
good path cheap; it cannot make the bad path impossible. Say that explicitly in any spec.

**Gate.** `tools/workflows/check-verifier-fanout.sh:72-77` already shows the shape — a file gate that
delegates to the hook so both entry points share one predicate.

**Breaks.** Any inline script anyone is currently running that carries a ref-keyed join. That is the
point. Also: `TOOL-aNumeralWarden-2` (`:49`) records that the hook's enclosing-opener walk is defeated
by two nested wrappers or 59 lines of distance, so a restructured harness can fall outside the guard.

**Closes.** No row directly; it is the left-shift `TOOL-aScannedThrottle-10` (`:163`) asks for, and
that row's rule applies — **a new gate is not landed until its failing case has been observed.**

---

### P6 — The rule edits each option implies · **VIABLE (this is the owner's call, not a tooling change)**

**What each option needs, stated so the owner can price them separately:**

- **M4 `:113`** — P1 makes "Not the harness" false. The honest replacement is not a deletion but a
  restoration of the mechanism clause the rule lost in `570f8100`, re-pointed: name what the harness
  needs to be given for a spec, so the rule stays falsifiable.
- **M4 `:110` vs `:129-132`** — the fold seam. `:132` already resolves it for BLOCKED; `:110` was never
  amended. Either amend `:110` or state that the `CLEAN WITH FIXES` fold is deliberately unmeasured.
  Two build READMEs already treat the latter as settled, so this is a ratification, not a discovery.
- **M4** — one pointer line naming `--review`, per P4.
- **M8 `:227`** — the harness names its own file and M8 requires a rename to check 5's grammar before
  the next gate run. A kind-aware engine could name it correctly; that is a spec decision.
- **`REVIEW-PROTOCOL.md:171`** — "3–6 primed finder lenses" contradicts the hook's `MAX_LENSES` in
  **four** carriers, including the same file that records the ratification at 5 (`:185-188`). A caller
  who follows the sentence and writes six lenses is denied at the tool call. Fix all four.
- **Binding grammar** — if a round or reviewed-rev axis lands (P10), `memory/HYGIENE.md` gains it.

**Cost.** The multi-carrier class. `TOOL-dUnstalledConvoy-16` (`:18`) records the exact failure: a
correction landed in `REVIEW-PROTOCOL.md` while `coding-governance-agents.template.md` and its render
`AGENTS.md` kept the refuted sentence and SHIPPED it to every adopter. **A rule change about review
kinds has at least four carriers.** Budget for a same-commit re-render and the parity leg.

**Breaks.** `tools/check-agent-cap-restatement.sh` BANS a new bound-word × number × noun in live
markdown. The default disposition for a new review-shaped number in prose is to delete it and point at
the file; joining `check-playbook-parity.sh`'s five pairs is the exception that buys a keepable digit.

**Closes.** No row directly.

---

### P7 — An engine/profile split, folding the drift audits in ·
**VIABLE, expensive, and partly priced by prior art**

**What.** One engine file carrying a profile table (spec-audit · diff-review · drift-state ·
drift-code · research), with the two drift audits retired into profiles of it.

**Cost.** High, and the runtime forecloses the obvious shape: **scripts cannot import**, so an
engine/profile split cannot be a code-sharing split. It is either one large file with profiles inside
it, or a renderer that emits N files from one source and a parity gate over the emission. The second is
a new build in itself.

**Buys.** The one thing P1 does not: it fixes the measured regression. The two drift-audit siblings
would gain every counter they lack, and the pipeline would stop being implemented three times.

**Gate.** The same three JS gates, plus a parity gate if a renderer is used.

**Breaks.** It walks into the refusal in prior art item 1 unless every counter survives on every exit
path of every profile, and into item 2 if the filename moves. `TOOL-aBoundedVerdict-29` (`:152`) prices
the version bump: five marker sites, and a previous 1.4→1.5 bump took three rounds to settle.

**Closes.** `TOOL-dUnstalledConvoy-16`'s instance in executable code, though not the row itself.

**Recommendation.** Viable but not first. If the owner wants the regression fixed sooner and cheaper,
the same benefit is available by simply porting the seven counters into the two drift-audit files —
which is not a proposal about review kinds at all, and would be a separate, small row.

---

### P8 — A sibling spec-audit harness (`tools/workflows/spec-audit.js`) · **REFUSED-BY-PRIOR-ART**

**What.** A second engine beside `tier2-review.js`, spec-shaped.

**Why refused.** It is instance #4 of a pipeline whose instances #2 and #3 already lost every hardening
instance #1 learned, with every gate green over the loss. Shipping a fourth copy is the documented
failure repeated deliberately. It also re-enters the refusal in prior art item 1 unless it carries all
seven counters — at which point it is a copy of `tier2-review.js` with a different lens table, which is
P1 with extra files.

**If the owner wants it anyway:** the honest form is P7's renderer, not a hand-maintained sibling.

---

### P9 — A record-shape gate · **VIABLE, and an alternative to P1 rather than a complement**

**What.** Extend the hygiene checks so a review record must carry the review-shape line, the range or
subject anchor, and the unverified counter — the fields the measurement shows are present 77–88% when
a program emits them and 5–27% when a document asks.

**Cost.** One check in `tools/memory-tree/check-memory-hygiene.sh` plus a forward-only cutoff, exactly
the shape check 22 already uses. Nothing in `tools/gate-legs.json` grades review-record shape today:
`grep -n 'precision\|review shape' tools/memory-tree/check-memory-hygiene.sh` is empty.

**Buys.** The same completeness P1 buys, by the other mechanism. **The corpus says either mechanism
works and prose does not** — that is what the 92%-vs-82% inversion on the gated field measures.

**Breaks.** A forward-only cutoff is mandatory; anchoring the fields retroactively would make the check
unsatisfiable against most of the corpus, exactly as `unattended.sh` records for the verdict grammar
("`^## Verdict: CLEAN` matches zero of this corpus's 46 records").

**Closes.** No row.

**Recommendation.** Cheaper than P1 and strictly weaker: a gate grades what reached the record, and
cannot make a degraded run declare itself. Best as a companion to P1, worth doing alone if P1 is
declined.

---

### P10 — A round axis and a reviewed-rev axis on the record · **VIABLE**

**What.** Two new recorded fields, emitted by the driver rather than typed: the round number and the
reviewed `rev-N` (or blob sha) of the subject. **Not** a fifth record kind.

**Cost.** The binding grammar already admits a trailing `@rev-N`, "recorded and never validated", used
by exactly one record. Validating it and having a program write it is the change.

**Buys.** It makes M4's own question answerable from the tree. `gen_build_index.py:769-778` today
renders "Ids no `spec-audit` record has ever named" and concedes in its own comment that a spec audited
at rev-1 and since bumped does not appear — so the report-only join cannot answer "is this spec
unreviewed". **A kit that stamps the reviewed rev makes the existing join gateable for free.**

**Gate.** Promote the report-only region to a check, once the data can support the claim. Until then it
must stay report-only, and the current comment is the honest statement of why.

**Breaks.** Nothing at HEAD; the qualifier is already legal.

**Closes.** No row.

---

### P11 — Tighten the marked-derivation branch in `agent-cap.js` ·
**VIABLE, and a prerequisite for P1's dialect**

**What.** Require EVERY non-self reference in a marked derivation to be bounded, not merely one.

**Cost.** One predicate change, plus the charter's rule: run it over the real tree first and print hits
AND near-misses. `tools/workflows/drift-audit-state.js:224` is the only shipped user of that branch, so
the population is one.

**Buys.** Closes the reproduced hole where a marked ternary's caller-supplied branch reaches `agent()`
once per element — the same defeat the `<expr> || <int>` binder was deleted for.

**Gate.** `tools/hooks/agent-cap.js`'s own self-test, which must observe the new failing case.

**Breaks.** Any script relying on the loose form. One is shipped and would need re-shaping.

**Closes.** No row. It is adjacent to `TOOL-dFramedEntrypoint-1` (`:6`) and `TOOL-aCandidStub-1` (`:51`),
neither of which it closes.

---

### P12 — Left-shift the fold class into `memory/gotchas/` · **RECOMMENDED, and the cheapest item here**

**What.** One record file. `memory/gotchas/` holds 32 files
(`ls memory/gotchas/*.md | wc -l`) and `ls memory/gotchas/ | grep -i fold` exits 1 with no output. The
class — a fold writes text nobody reviewed, and it is where the findings are — is measured (42 of 62
round-2 findings on `dFramedEntrypoint`) and lives only in machine-local auto-memory.

**Cost.** A record file with anchors and a declared resolution, per hygiene checks 18 and 19. Its
natural anchors — `memory/guides/BUILD-METHOD.md` and `tools/workflows/tier2-review.js` — are both real
tracked paths, so it is anchorable.

**Buys.** `python tools/memory-tree/gotchas.py --for-diff <base>..<head>` is the checklist M6 and M8 hand
every reviewer, and it can only emit classes that exist as records. **The highest-value class
discovered on the most recent build is currently invisible to it.** No code change.

**Gate.** The existing hygiene checks over `memory/gotchas/`.

**Breaks.** Nothing. I did not check whether adding it breaches `UNIVERSAL_BUDGET`.

**Closes.** No row.

**Related, and separable:** the fold instructions the measurement named — verify a did-not-land claim by
reading the body at HEAD rather than the revision log, and fold DELETIONS rather than appending
negations — reach no prompt today (`grep -n "revision log" tools/workflows/tier2-review.js` returns no
match). The harness carries exactly one sentence of fold priming, at `:184`. Extending it costs prompt
text, not architecture, and belongs wherever the kind profiles land.

---

### Ranking, in one list

| # | Proposal | Disposition |
|---|---|---|
| P1 | subject descriptor on the existing engine | **RECOMMENDED** |
| P2 | read `blockers`, instruct `## Verdict:` | **RECOMMENDED** — can land first and alone |
| P12 | fold class into `memory/gotchas/` | **RECOMMENDED** — cheapest, no code |
| P5 | close the enforcement gap at the hook | VIABLE — the only lever reaching an inline script |
| P4 | drive the convergence loop | VIABLE — wiring, not a build |
| P3 | lens catalogue as declared data | VIABLE |
| P9 | record-shape gate | VIABLE — alternative to P1, strictly weaker |
| P10 | round + reviewed-rev axes | VIABLE |
| P11 | tighten the marked-derivation branch | VIABLE — prerequisite if P1 uses that dialect |
| P6 | the M4/M8/`REVIEW-PROTOCOL` rule edits | VIABLE — owner's call, four carriers |
| P7 | engine/profile split | VIABLE, expensive, partly priced by prior art |
| P8 | sibling spec-audit harness | **REFUSED-BY-PRIOR-ART** |

---

## What this research did NOT establish

**Claims raised in this pass that were REFUTED by the skeptic stage and are recorded here as
refutations, not facts.** Anyone writing a spec from this record must not reinstate them.

- **"Every recorded degraded review run is a spec audit — 4/83 against 0/73."** Refuted. The 0/73 does
  not survive its own criterion; a `diff-review` declares five unjudged findings. Under a consistent
  criterion the split is 3/0 on agent death or 1/1 on unjudged findings. The measurement section states
  the surviving version.
- **"The stage-death hole recurs across two weeks."** Refuted — the three records are dated 2026-08-16,
  2026-08-16 and 2026-08-17. **Two days, two of them the same day.** The likeliest reading is one
  exhausted usage window, not a defect class recurring across sessions.
- **"All 83 spec-audit records were driven by something other than the shipped harness."** Refuted as
  over-reaching. The harness's hard-coded binding line landed only on 2026-08-19
  (`git log -S"Serves:** diff-review" -- tools/workflows/tier2-review.js`), and before that it wrote no
  binding line at all — so for the 66 records predating it, the harness could have driven the run and a
  human typed the token. The structural argument covers only the later 17. What holds is the weaker,
  measured claim: **the corpus cannot say how 146 of 157 reviews were driven.**
- **"At least six Column-B defects are false-clean classes."** Five of the six citations support it;
  the sixth (the wrong-repository defect) is expressly the opposite case — it returned confident
  findings about the wrong code rather than reporting clean. The table above says five.
- **"The charter owed a factory at instance #2 and no waiver exists."** Refuted by the charter itself:
  `AGENTS.md:303` and `:319` instruct inlining because scripts cannot import, and `:365`'s per-kind map
  names kits, not harnesses, as the kind here.
- **"There is no verdict concept in the engine at all."** Refuted in part — `:335` mentions unverified
  findings inside the synthesis prompt, and `:360/:369-370` request and schema a blocker count. What is
  absent is any instruction to EMIT the `## Verdict:` line, and any READ of the blocker count. P2 is
  scoped to the narrower, true version.
- **"Only four things resist parameterisation" / "the method imposes fourteen review-shaped
  obligations" / "three .js engines under `tools/workflows/`".** All three are underived or wrong
  counts. There are **four** `.js` files matching `git ls-files | grep -i workflow` (the fourth is the
  syntax gate). The obligation table above is presented as what I read, not as an exhaustive census.
- **"A new review-harness leg costs 1.7 s."** Wrong number. The five `subject: repo` review-area legs
  sum **3.783 s** on this worktree's ledger; 1.7 s corresponds to a different set of four. The
  conclusion — a sub-second scanner does not move a bar floored by a 2013 s shard — is unaffected.

**Questions this pass could not answer.**

- **How any spec audit in this corpus was actually driven.** Only 11 of 156 records name a workflow run
  id and exactly one names a script path. The record shape never required the drive mechanism, and the
  protocol explains why nothing can recover it: the ad-hoc review script is inline and never a file.
  **Any provenance a kit wants must be EMITTED by the driver; retrofitting it from the corpus is
  impossible.**
- **How many distinct sessions wrote their own review script.** Not derivable. The upper bound is 43
  distinct build slugs carrying a spec-audit record, across all four registered nodes, and a build slug
  is not a session.
- **Whether `meta.phases` can be built from `args`.** Not established — no measurement exists of whether
  the Workflow runtime reads `meta` before evaluating the body. If kinds want different phase names,
  that question must be settled first. What IS established is narrower: two gates select their
  population by the literal regex `^\s*export\s+const\s+meta\s*=`, so a harness spelling its export any
  other way silently drops out of both.
- **Whether a `PreToolUse` hook fires inside a sidechain.** Recorded as UNMEASURED at
  `memory/guides/REVIEW-PROTOCOL.md:101-103`; the experiment never ran because the matcher covers tools
  a sidechain does not hold.
- **Whether adding the fold class breaches `UNIVERSAL_BUDGET`.** Not checked.
- **Which review the 47-agent measurement was taken on.** Four carriers, two readings. Not resolved
  here and not resolvable from the corpus.
- **The token cost of `aSiftedPlaybook`'s round-1 loss.** Not on disk. Only a byte proxy (14%) and
  comparable-fan anchors (1.3–2 M) exist.
- **Whether a spec finding should be addressed by section or by `file:line`.** No record in the corpus
  examines the trade.
  `memory/builds/aGuardedTally/prompts/2026-08-03-prompt-TOOL-aGuardedTally-1-1.md:39-40`
  shows the corpus's own spec audits citing by section OR `file:line`, and that is the whole of the
  prior art.
- **What a spec fold's immutable boundary is.** A blob sha passes the existing regex unchanged and is a
  true content hash; `rev-N` is the semantically right anchor and does not pass. Nobody has decided.
- **The `CLEAN WITH FIXES` fold path has never been measured**, because on that path no round runs to
  measure it. The 42-of-62 fold measurement was taken on a BLOCKED build — the one path the method
  already covers.

**Probes that returned nothing, recorded as answers.**

- `git log --all --oneline -- '*tier2-review-indexed*'` → empty. The file has no object in this repo's
  history.
- `grep -rn "spec-audit" tools/workflows/` → exit 1, no output.
- `grep -rniE "review kind|kinds of review|subject kind|reviewKind|args\.kind" tools/ memory/` → four
  hits, all prose, none in code.
- `grep -nE 'lensesDead|skepticsDead|assignedIds|spurious|conflicts' tools/workflows/drift-audit-state.js
  tools/workflows/drift-audit-code.js` → exit 1, no output.
- `ls memory/gotchas/ | grep -i fold` → exit 1, no output.
- `grep -n verdictByRef tools/hooks/agent-cap.js` → exit 1.
- `grep -n "revision log" tools/workflows/tier2-review.js` → no match.
- `grep -n "OPEN" memory/backlog/PLAY.md` filtered for review terms → empty; same for `KICK.md`.
  `DEPL.md` returns two OPEN rows, neither about reviews.
- `ls memory/map/features/` → 17 dossiers, **none for the review harness**; `workflows` (`:45`) and
  `tier2-review.js` (`:55`) both still sit unclaimed in `memory/map/baseline.toml`. Per the charter's
  DoR, a design pass over this area owes that dossier.

**The review shape of THIS research pass.**

Five primed lenses (corpus · anatomy · kinds · constraints · priorart) → batched skeptics defaulting to
refute → one synthesis, under the caps the hook resolves. Raw claims raised **61**, numbered 1..61 with
no gaps. Confirmed **51**. Refuted **10** — ids 2, 5, 9, 11, 14, 24, 25, 26, 48, 58, every one
enumerated above. Unverified **0**. Precision 51/61 = **0.836**.

**Coverage and mortality, stated rather than assumed.** All five lenses returned — five detail files
exist and every one carries evidence. Zero claims came back without a usable verdict, which is the only
evidence available that no skeptic batch was lost; I did not observe an agent-count return, so
"no skeptic died" is an inference from the empty unverified bucket rather than a measurement. **The
synthesis stage of this pass is this record, written by hand**, so it has no death to report and no
independent adjudication either.

One methodological caveat about that precision figure, which is the kind of thing this record exists to
say out loud: several refutations were partial — the skeptic confirmed a claim's substance and refuted
a count, a date span, or a line citation inside its evidence. Those are recorded as refutations because
that is the conservative reading, so 0.836 understates how much of the finding set survived and
overstates how much was wrong. **Six of the ten refutations (9, 11, 14, 25, 26, 48) left the underlying
observation standing and killed only a number attached to it**; four (2, 5, 24, 58) reached the
substance. Line-number drift of one to five lines was pervasive across citations in the lens outputs;
every citation reproduced in **this** record was re-run against HEAD `2ddd0db8` before it was written
down, and the ones I could not re-run are named above.
