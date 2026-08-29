# TOOL-aLexedStripper-2 — `agent-cap`'s lens counter reads a template-aware view

**Status:** SPECCED · rev-1 · 2026-08-30 · node a · Tier-2 · base 19d9b328 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`fanoutFindings` in `tools/hooks/agent-cap.js` must count a lens array's elements over a view that
knows what a template literal is, so ordinary English in a lens prompt stops being counted as code
structure and a correct five-lens harness stops being denied for its prose. The guard's existing
DENY verdicts must not change.

## 2. Scope (IN)

- **S1** — `fanoutFindings` takes its `code` view from `blankLiterals(script)`, the state machine
  this file already defines at `agent-cap.js:504`, instead of the per-line
  `stripStrings(l).split('//')[0]` at `:259`.
- **S2** — Preserve the reach `blankLiterals` would remove. It blanks template CONTENTS including
  `${…}` bodies, and an interpolation can hold a real `agent(` call. Rule 5 already solved this at
  `:907` by scanning the interpolation SPANS as a second view; S1 adopts the same second view for
  rule 2 rather than inventing one.
- **S3** — Fixtures in `tools/hooks/agent-cap.test.sh` for both directions: the two false-positive
  spellings reproduced at BASE, and the fail-open shapes that must STAY denied.
- **S4** — Bump `KIT_AGENT_CAP_VERSION`.

## 3. Non-goals (OUT)

- Not touching rule 1 `offendingLines`, rule 3 `capFindings` or rule 5 `scanJoinFindings`. Only the
  bounded-receiver view moves; `capFindings` already reads `blankLiterals`.
- Not changing `CAP`, `MAX_VERIFIERS` or `MAX_LENSES`. No number moves.
- Not fixing `TOOL-aCandidStub-1` (an empty array literal grown by a later `push`) or
  `TOOL-aNumeralWarden-2` (the enclosing-opener walk defeated by distance). Both are open rows
  against this file and both are a different mechanism.
- Not fixing `TOOL-dFramedEntrypoint-1`, which is two prose sentences in `AGENTS.md` §8 and
  `tools/hooks/README.md`, not a code change.

## 4. Design

### The mechanism

Rule 2 blesses an identifier as a bounded receiver when it is assigned from an array literal whose
top-level element count is at or under `MAX_LENSES`. It measures that over `code`, built per line by
`stripStrings`, which blanks `'…'` and `"…"` and deliberately leaves backticks alone. Lens prompts
ARE backticked template literals full of English, so their punctuation reaches two counters that
expect code: the `[`/`]` join-forward walk at `:326` and `topLevelArgs` at `:562`.

### What reproduces at BASE

Measured against `tools/hooks/agent-cap.js` at `19d9b328`, each script a correct five-element lens
array fanned through `boundedParallel(…, MAX_VERIFIERS)`. Only the prose of one prompt differs.

| lens prose contains | verdict at BASE | correct verdict |
|---|---|---|
| a literal `...` | DENY | ADMIT |
| an unmatched `)` | DENY | ADMIT |
| an unmatched `(` | ADMIT | ADMIT |
| nothing unusual | ADMIT | ADMIT |

The `...` spelling is the `:344` guard `if (inner.includes('...')) return`, which reads prose
punctuation as a spread. The unmatched `)` shifts `topLevelArgs`' depth so the remaining separators
are not counted at top level. The unmatched `(` shifts it the other way and UNDER-counts, which
still satisfies `<= MAX_LENSES` and passes — so the class is asymmetric and only two of its four
spellings are visible as denials.

### What must NOT change

The prior closing-diff review of `TOOL-dTieredTribunal-11` (round 2, findings 3 and 4) recorded two
fail-OPEN escapes through this same view and specified this same fix. Re-measured at BASE, both are
now DENIED — that half landed. This unit therefore closes a false-positive class and must be proven
not to re-open the escapes those findings closed, which is what S3's second fixture group is for.

### The refusal message

The denial an operator sees names verifier arity and points at a `chunk()` recipe, which is why the
adopter's gotcha concluded the harness needed restructuring. Nothing in this unit changes the
message; the class it fires on stops existing.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — the view at `:259`, the interpolation second view, the version
  constant.
- `tools/hooks/agent-cap.test.sh` — the fixtures.

### Alternatives rejected

- **Track a `tmpl` flag inside rule 2's own loops.** The prior review offered this as its second
  option. Rejected: it is a second implementation of the state machine `blankLiterals` already is,
  in the same file, which is the two-answers-to-one-question class the bug-class checklist selected
  for this diff.
- **Teach `stripStrings` about backticks.** Rejected: `stripStrings` is per line and a template
  literal spans lines, so it cannot be made correct without becoming `blankLiterals`. Rule 5's own
  comment at `:905` states that a `${…}` is an interpolation only inside a template literal, which
  is precisely the state a per-line function does not carry.
- **Widen `MAX_LENSES`.** Rejected outright: the count is not wrong, the counter is, and the
  constant's own comment records that it was once raised to fit a miscount.

## 5. Production-readiness checklist

- security — this IS the security surface. The guard is the only mechanical control against an
  unbounded agent burst, so the acceptance criteria are written around what must stay DENIED, not
  only what must start being admitted.
- perf / scale — `blankLiterals` is one pass over the script and already runs for rules 3 and 5 on
  every call. The change removes a per-line regex pair.
- a11y — N/A, no user interface.
- i18n — the class includes non-ASCII prose. The U+2019 workaround the adopter's gotcha prescribes
  is measured ineffective against the two live spellings, and after this unit no workaround is
  needed.
- error / empty / loading states — an unterminated template literal must not swallow the rest of the
  script into a blank view. `blankLiterals` carries its `tmpl` mode across lines by design, and the
  behaviour on an unterminated one is an arm in §6.
- observability — the hook writes its verdict to stderr and exits 2; unchanged.
- risks — a fail-open regression is the whole risk. Blanking template contents without the
  interpolation second view would hide an `agent(` call written inside `${…}`, which is why S2 is
  scope and not an optimisation.
- testing + left-shift gates — fixtures in both directions, the false positives observed RED at BASE
  and the escapes observed DENY at BASE and after.
- migration / rollback — none; single-file revert.
- user docs — none. `tools/hooks/README.md` documents the marker grammar, which does not change.

## 6. Acceptance criteria

- **AC1** — When a five-element lens array whose prose contains a literal `...` is passed to
  `agent-cap.js` as a `Workflow` script, it exits `0`, against exit `2` at BASE.
- **AC2** — When the same array's prose contains an unmatched `)`, it exits `0`, against `2` at BASE.
- **AC3** — When the same array's prose contains an unmatched `(`, an em dash, and ASCII
  apostrophes, it exits `0`.
- **AC4** — When the `TOOL-dTieredTribunal-11` round-2 finding-4 script is run — `ALL.filter((L) =>`
  `` `(`.length > 0).reduce((acc, b) => args.big, [])`` marked `gov:fixed-verifiers` — it exits `2`,
  as it does at BASE.
- **AC5** — When a six-element lens array is run, it exits `2`.
- **AC6** — When an `agent(` call is written inside a `${…}` interpolation over an unbounded
  receiver, it exits `2` — the S2 second view.
- **AC7** — When a script's template literal is left unterminated, `node tools/hooks/agent-cap.js`
  still returns a verdict and does not throw.
- **AC8** — When `bash tools/hooks/agent-cap.test.sh` runs, every existing arm still passes.
- **AC9** — When each new false-positive fixture is staged against the code at BASE,
  `bash tools/hooks/agent-cap.test.sh` reports it RED, and the observation is recorded in the
  acceptance ledger.
- **AC10** — When `bash tools/check-kit-versions.sh` runs, `KIT_AGENT_CAP_VERSION` is bumped and
  well-formed.

## 7. Gates

`agent-cap self-test` · `agent-cap restatement` · `kit-versions` · `playbook parity` · and the full
bar at the push boundary. `tools/check-playbook-parity.sh` machine-compares five agent-cap values
against the charter, so a constant that moved without its prose would red there; this unit moves no
constant except the version.

## 8. Open questions

- **F1 — should rule 1 `offendingLines` take the same view?** A raw `parallel(` written inside a
  lens prompt is prose and is denied today, which is the same false-positive class one rule over.
  Against that: rule 1's ceiling is documented as deliberately fail-closed in the file header, and
  widening its blind spot is the one direction this unit's own §5 forbids without its own fixtures.
  Recommendation: leave rule 1 alone in this unit and file it. RESOLVED (agent, 2026-08-30,
  delegated): out of scope here, filed as a backlog row. It is a preference between two defensible
  readings rather than something an observation decides, and M3's rule sends a fork with no
  feature-richness difference to the option with fewer follow-ups — which is the one that does not
  touch a second rule's verdicts in a unit about the first.
- **F2 — does the interpolation second view belong in `blankLiterals` itself?** Rule 5 builds it at
  its call site from `stripStrings(raw)`. Recommendation: build it the same way rule 2 needs it,
  at the call site, matching rule 5. RESOLVED (agent, 2026-08-30, delegated): at the call site,
  mirroring rule 5 exactly. Moving it inside `blankLiterals` would change the view rules 3 and 5
  already read, which is a change to two working rules to tidy a third.

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, written from a measured reproduction at BASE `19d9b328` and
  from the prior closing-diff review that specified the same fix.

## 10. Reuse audit

`python tools/memory-recall/query.py` with the terms below returned, as its second hit,
`memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-11-closing-diff-round2.md:174`,
which states the fix this unit implements in the same words: *give `fanoutFindings` the
`blankLiterals(script)` lines instead of `stripStrings`*. Its neighbouring finding at `:248`
specifies the interpolation-preserving second view that S2 adopts. The seam is therefore already
identified and already in the tree — `blankLiterals` at `agent-cap.js:504` — and this unit wires
rule 2 to it rather than writing anything new. `tools/codebase-map/reuse_lookup.py` independently
ranked `blankLiterals` and `stripStrings` as the top two candidates for the same behaviour phrase.

Recall terms used, for M7 re-runs: `agent-cap stripStrings blankLiterals template literal lens array
bounded receiver interpolation view fan-out counter prose`.

**A hit that was STALE, recorded because M5 requires it.** That review's findings 3 and 4 are
written as fail-OPEN escapes admitted at `rc=0`. Both were re-run against BASE for this spec and
both are now DENIED, so the escape half landed and only the false-positive half remains. A spec that
had trusted the record would have claimed to close a hole that is already closed. The adopter's
`ABL-dPinnedVintage-4` is stale in the same way: it names version 1.6 and attributes the denial to
two apostrophes eating a `)`, and at 1.8 an apostrophe pair alone no longer denies — the surviving
spellings are a literal `...` and an unmatched `)`. Its prescribed workaround, U+2019 in place of
ASCII `'`, does not address either.
