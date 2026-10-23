# TOOL-dFairHearing-2 — the design-audit preset of the spec-audit kind, chosen by a preset argument

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 2 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0069@a762d009 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-2-deviation-28.md](../build/2026-10-23-build-TOOL-dFairHearing-2-deviation-28.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-mark-rewrap-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-mark-rewrap-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-16 TOOL-dFairHearing-23 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

A design or architecture record is audited today with the unit-spec lenses, whose briefs aim at a
unit spec's numbered sections, and every defect found after the runtime design's two rounds fell
outside them (gap-review-04, HIGH). This unit adds the design-audit preset (RV-1): a `preset` argument
of the `spec-audit` kind that selects a third five-slot literal, filled from five catalogue rows
aimed at design records: coherence, grounding flagging untested assumptions, reuse held to precedent,
failure-envelope extended to trust boundaries, and alternatives-and-cost in place of blast-radius. It
ships dark (shared interface S9): the argument defaults to `unit-spec`, and nothing passes
`design-audit` until the owed replay's verdict.

## 2. Scope (IN)

- **S1** — `tier2-review.template.js` takes a `preset` argument: a closed set `PRESETS` of
  `unit-spec` (the default) and `design-audit`, refused by name outside it, and refused whenever it
  is given beside the `diff-review` kind, validated where `intensity` is (:210-217) and before any
  agent. The kind stays `spec-audit`, so the binding line and the hook's spec-audit opt-in are
  untouched. Observed by AC1.
- **S2** — A third literal, `DESIGN_LENSES`, marked `// gov:lens-slots design-audit` and filled by the
  render, and the marked receiver becomes
  `const LENSES = !isSpec ? DIFF_LENSES : preset === 'design-audit' ? DESIGN_LENSES : SPEC_LENSES // gov:fixed-verifiers`.
  Observed by AC2, AC3 and AC5.
- **S3** — Five rows in `tools/workflows/lenses.toml`, `default_in = ["design-audit"]`, with the
  briefs §4 states. `coherence`, `grounding`, `reuse` and `failure-envelope` reuse their keys in rows
  of their own (TOOL-dFairHearing-13 §8 F2); `alternatives-and-cost` is a new key. The unit-spec and
  diff rows do not move. Observed by AC2 and AC3.
- **S4** — `preset` joins the review key's input print when it is not `unit-spec`, so a design-audit
  run never reuses a unit-spec run's lens files on the same subjects, and every key a run without
  the argument derives is unchanged. Observed by AC4.
- **S5** — A spec audit announces its preset: a log line before the first agent when it is not the
  default, a `preset:` line in the synthesis's RUN INTEGRITY block (:1773), and `preset` on every
  return of the spec kind, beside `intensity`. Observed by AC6.
- **S6** — The input header block (:91-139), which the suite asserts against the fields the harness
  reads, lists `preset`; `tools/workflows/README.md` documents it beside `intensity`. Observed by AC7.
- **S7** — The dark switch (S9): no caller in this unit passes `design-audit`. Observed by AC8.

## 3. Non-goals (OUT)

- Who passes `design-audit`. `review.pin` maps the pinned revisions' record kind to `preset`, behind
  its own default, and the build harness forwards the argument: `TOOL-dFairHearing-3`. Design's
  breakpoint is that stand-in until dDeclaredLoop's `review.trigger` lands.
- Flipping the default for design records: the blind replay at blob `767187aa` decides it
  (`TOOL-dFairHearing-1`, S9).
- The `whole-design` preset: `TOOL-dFairHearing-18` adds it to `PRESETS` with its literal.
- Opt-in lenses on this preset: `TOOL-dFairHearing-3`.
- A refusal of `design-audit` over unit-spec subjects: a manual call may pass it for any spec audit
  (the review-system record, `[lenses]`, its line 131; §8 F3).
- `REVIEW_SHAPE` (:970): the new prompts run only under a key `preset` already separates (S4), and no
  existing prompt changes.
- A change to the review-shape record line, `renderShapeLine` (:78-83), which records parse.

### Edges

- **consumes-from** `TOOL-dFairHearing-13` — the catalogue, the renderer and the slot count; without them the third literal has no source and no bound
- **hands-off** `TOOL-dFairHearing-3` — `review.pin`'s mapping of design records to `design-audit`, held behind its default, and the build harness forwarding `preset`
- **hands-off** `TOOL-dFairHearing-9` — the preset names per-preset lens notes are keyed by
- **hands-off** `TOOL-dFairHearing-11` — the `preset` argument its `design-records` twin setting reads
- **hands-off** `TOOL-dFairHearing-1` — the replay verdict that keeps or flips the unit-spec preset for design records
- **hands-off** `TOOL-dFairHearing-18` — the closed set of the `preset` argument and the marked receiver its `whole-design` literal joins
- **hands-off** `TOOL-dFairHearing-23` — finding ids 8 and 35 of the round-1 spec audit: the whole-design literal and receiver branch, with AC1's refusal arm rewritten to refuse another unknown preset (its S15, AC8), and AC4's key arm re-derived from the current `REVIEW_SHAPE` (its S29, AC20)

## 4. Design

### Evidence

- `intensity` is the shape this argument copies: a closed set refused outside it and refused on the
  kind that has no such subset, before any agent (`tools/workflows/tier2-review.template.js:210-217`).
- A spec subject is a path with a `builds/<slug>/spec/` segment and every other subject a design
  subject (`SPEC_SUBJECT_PATH`, :313-317), so a design record is already a legal subject; only its
  lenses are wrong.
- The spec briefs name unit-spec structure: `coherence` reads "a section-2 item no section-6
  criterion observes" and "section 4 Design against section 7 Gates"; `grounding` "every claim
  sections 4 and 10 make"; `blast-radius` "section 4's files-touched list" (:814-829). A design
  record carries none of those sections.
- The hook admits a nested ternary of literals on the marked receiver: measured 2026-10-23, a copy of
  `tools/workflows/tier2-review.js` carrying a third five-element literal and this receiver exits 0
  from `node tools/hooks/agent-cap.js --only=scripts`, while a sixth slot planted in the same copy
  exits 2. The lens research's shape table records the same (`[shape]`, "per-stage preset").
- The review key's print already adds a field only when it departs from its default, so old keys hold
  (`workerType` and `roles` at :975-987).

### The five rows

Each brief is one line in the catalogue; the wrapping below is this document's.

```toml
[[lens]]
key = "coherence"
kinds = ["spec-audit"]
presets = ["design-audit"]
default_in = ["design-audit"]
optin = false
brief = "Coherence: does the design record agree with itself and with the records it cites? Report a stated goal, requirement or invariant no mechanism in the record delivers; one rule, name, path, key or number stated two ways; a step that depends on one ordered after it; two mechanisms claiming one file, one owner or one landing slot; and, across the subjects and the sibling context, a decision one record takes that another contradicts."

[[lens]]
key = "grounding"
# kinds, presets, default_in and optin as above
brief = "Grounding: is every claim the design makes about the world TRUE where the subjects stand? Check each claim about existing code, a tool's flags or output, a record, a count, a platform behaviour or a cost against the source, never against the design. Flag every load-bearing claim that rests on a docs line or a single observation as an untested assumption, name the observation that would overturn it, and probe it where the probe rules allow. Hunt the traps this platform sets: MSYS argument and path rewriting, drive-letter and backslash paths, CRLF in a working copy and a text-mode read that drops a CR, and a stated wall-clock goal nobody timed."

[[lens]]
key = "reuse"
brief = "Reuse and precedent: functionality is reused and extended, never rebuilt, and every choice keeps faith with what was decided. Report a mechanism that rebuilds an existing function, checker, gate leg, driver verb or record shape; and a choice that re-opens a decision row, an owner ruling or a decided ask, or drops a condition a ruling rested on, naming the id and quoting both texts. Probe before you claim: the codebase-map kit's reuse_lookup.py with a behaviour phrase, the memory-recall kit's query.py with a plain-English question and 8-14 --terms in this corpus's own jargon, and grep. THE BAR: a finding names the existing seam, record or ruling by path or id AND quotes the design text that duplicates or contradicts it."

[[lens]]
key = "failure-envelope"
brief = "Failure envelope and trust boundaries: what will the built system meet that the design never says it handles? Report the input classes it is silent on (empty, malformed, multi-line, unterminated, huge, concurrent), signals, partial failure and a dead dependency; every trust boundary the design creates or relies on, an enforcement a rule, a setting, a second path or a dead dependency bypasses, input trusted without validation, and a guarded action left allowed on failure; and a design that names one instance where the class was meant."

[[lens]]
key = "alternatives-and-cost"
brief = "Alternatives and cost: is there a materially simpler or cheaper mechanism meeting the same contract, and what does this one cost? Report an existing seam, a checker in place of an agent, or one process in place of many that meets the same requirement or invariant, saying which; and every agent, session, spawn, token and wall-clock cost the design adds that carries no ceiling, no enforcer, or a ceiling nobody measured."
```

The briefs compose the review-system record's design-audit set (`[lenses]`, lines 118-125) with the
lens research's assumptions, precedent, security, alternatives and cost briefs (its `[candidates]`,
lines 136-160), with every unit-spec section reference taken out.

### The argument

```js
const PRESETS = ['unit-spec', 'design-audit']
const preset = a.preset === undefined ? 'unit-spec' : a.preset
// refused, by name, before any agent: given beside the diff kind; not a member of PRESETS
```

`PRESETS` sits beside the literals it selects among. Its members other than the default each name a
marked literal, and the marked literals other than `diff-review` each name a member, which AC5
observes; the render's rule 8 ties the catalogue to the same markers.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (its render)
- `tools/workflows/lenses.toml`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`

### Alternatives rejected

- **Today's spec briefs shared by both presets**, one row each with `default_in` naming both. The
  briefs would keep their section references, which is the measured cause of gap-review-04 (§8 F1).
- **The harness choosing the preset from its subjects.** The clause chooses it by an argument a
  caller passes, and an inference would ship the behaviour live, not dark (§8 F2).
- **A fourth kind, `design-audit`.** It would change the binding line, the record-kind vocabulary and
  every reader keyed on two kinds; the review-system record keeps the kind for that reason.

## 5. Production-readiness checklist

- security — no new surface: one closed-set string argument, refused outside its set before any agent.
- perf / scale — the same five finders and the same verifier total; no agent added.
- error / empty / loading states — an absent argument is the default and changes nothing; an empty
  string is refused as outside the set.
- observability — the log line, the RUN INTEGRITY line and the return field say which preset ran.
- risks — a design-audit run's findings are not comparable with a unit-spec run's lens by lens; the
  replay owns that comparison (`TOOL-dFairHearing-1`).
- testing — AC1 to AC8; the arms in §7.
- migration — none: every existing call omits the argument and keeps its lenses and its review key.
- user docs — `tools/workflows/README.md`; no `help/` page covers the review harness.

## 6. Acceptance criteria

- **AC1** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js`, cut
  as `tools/workflows/tier2-review.test.sh:67-81` cuts it, with `kind: 'spec-audit'` and one design
  subject, `preset: 'design-audit'` proceeds; `preset: 'whole-design'` throws naming
  `unit-spec | design-audit`; `preset: 7` throws; and `kind: 'diff-review'` with `preset: 'unit-spec'`
  throws naming the diff kind.
  Red when: any of the three refusals proceeds, or the design-audit call throws.
- **AC2** — When `python 'tools/workflows/render_lenses.py' 'tools/workflows/lenses.toml' < tools/workflows/tier2-review.template.js`
  runs, the literal marked `gov:lens-slots design-audit` holds five slots whose keys read, in order,
  `coherence`, `grounding`, `reuse`, `failure-envelope`, `alternatives-and-cost`, and the `key:` and
  brief lines of the `unit-spec` and `diff-review` literals equal base's, in order.
  Red when: the design literal lacks a row or carries a unit-spec brief, or a default literal moved.
- **AC3** — When a scratch AsyncFunction run of `tools/workflows/tier2-review.js`, the shape
  the tier2-review suite's full-run arms use, stubs `agent` to record each
  finder prompt and runs one spec audit with `preset: 'design-audit'` and one without, the first's
  five finder prompts carry the five design briefs and the second's carry the base spec briefs.
  Red when: the design-audit run is fanned over `SPEC_LENSES`, or the default run's prompts moved.
  cost: a scratch harness modelled on that suite's stub agents.
- **AC4** — When the same probe reads the review key both runs derive over the same subjects, the
  keys differ, and the run without `preset` derives the key base's harness derives for those args.
  Red when: one key serves both presets, or an existing caller's key moved.
- **AC5** — When `bash tools/workflows/check-verifier-fanout.sh tools/workflows/tier2-review.js`
  runs, it exits 0 and its slot line counts three literals; and when a node probe reads the
  `PRESETS` literal and the `gov:lens-slots` marker names of `tools/workflows/tier2-review.template.js`,
  the members other than `unit-spec` equal the marker names other than `unit-spec` and `diff-review`.
  Red when: the hook denies the nested receiver, or a preset has no literal or a literal no preset.
- **AC6** — When the AC3 probe reads the return of the design-audit run and of a design-audit run
  whose finders find nothing, each carries `preset: 'design-audit'`, and the synthesis prompt it
  recorded carries `preset: design-audit` in its RUN INTEGRITY block.
  Red when: an exit path drops the field, or the report cannot tell which lenses ran.
- **AC7** — When `grep -n "preset" tools/workflows/tier2-review.template.js` runs, the input header
  block above `let cfg = args` carries a `preset:` line; and `grep -c "preset" tools/workflows/README.md`
  counts at least one.
  Red when: the argument is read but undeclared, which the suite's header arm reds.
- **AC8** — When `git grep -n "preset: 'design-audit'" -- tools/` runs, every hit is in a file named
  `*.test.sh`.
  Red when: a caller passes the preset before the replay's verdict, so the behaviour ships live.

## 7. Gates

`tier2-review self-test` · `verifier fan-out` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC3 AC4 AC6 · the three refusals, a design-audit run's finder prompts and review key against a default run's, and its returns, red against the base harness that reads no `preset` · FLOOR_ASSERTIONS in that suite, raised by the arms added

## 8. Open questions

- **F1 — Which briefs do the design-audit lenses run?** (a) Today's spec briefs for the four shared
  concerns, one row each listed in both presets, plus the new lens. (b) A design brief per lens, in
  rows of their own under the same keys. (a) keeps "section-2 item", "sections 4 and 10" and "section
  4 Design against section 7 Gates" in the prompts a design record is audited with, the measured
  cause of gap-review-04, and so fails the clause's "for design and architecture records". (b) costs
  five briefs and keeps the unit-spec preset unchanged, as the review-system record requires.
  Recommendation (b). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (b).
  widens: none · relaxes: none
- **F2 — Who chooses the preset?** (a) The harness infers `design-audit` when every subject is a
  design subject. (b) The caller passes `preset`, and `review.pin` maps the pinned revisions' record
  kind to it behind its own default. The clause says a `preset` argument Design's breakpoint passes,
  and S9 ships the behaviour dark; (a) fails both. Recommendation (b). Rung 1, v2's
  `cl-dClosedLoop-0069`. RESOLVED (agent, 2026-10-23, delegated): (b). widens: none · relaxes: none
- **F3 — Is `design-audit` refused over unit-spec subjects?** (a) Refused unless every subject is a
  design subject. (b) Legal for any spec audit. The review-system record says "A manual call may pass
  it for any spec audit" (`[lenses]`, line 131), and the replay may audit a mixed set.
  Recommendation (b). Rung 1. RESOLVED (agent, 2026-10-23, delegated): (b).
  widens: none · relaxes: none
- **F4 — Does the build's grant lift veto 2 for the harness edit?** `tools/workflows/` is a governance
  carrier on `PLAY-dClosedLoop-10`'s list. `cl-dClosedLoop-0069` names the design-audit preset, its
  `preset` argument and its five lenses. RESOLVED (agent, 2026-10-23, delegated): lifted by
  `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the review harness's preset argument and
  the design-audit lens rows · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.

## 10. Reuse audit

The seams extended are the marked receiver and its literals in
`tools/workflows/tier2-review.template.js` (:774-842), now rendered from TOOL-dFairHearing-13's
catalogue, and the `intensity` refusal (:210-217), whose closed-set shape the argument copies. The
review key's conditional fields (:975-987) are the precedent for joining the print without moving an
old key. `python tools/codebase-map/reuse_lookup.py "validate a closed-set caller argument before any
agent spawns"` returned only name-stem neighbours (`before`, `resolve_pattern_sets`, `renderAgentLabel`),
none a closed-set validator, so the precedent is the one read in the template rather than a seam the
lookup sees. No hit disagreed with source. The recall query's eighth hit, the debt-folds review
(`memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md:55`), records
that a preset with no item routing it changes nothing; `TOOL-dFairHearing-3`'s `review.pin` is that
route.

Recall terms used: `python tools/memory-recall/query.py "which lens set audits a design record rather
than a unit spec" --terms "design-audit preset RV-1 spec-audit kind design record unit-spec
SPEC_LENSES alternatives-and-cost gap-review-04"`
