# TOOL-aSightedSkeptic-7 — an intensity argument whose light setting announces the lenses it skips

**Status:** CLOSED · rev-2 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 7 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 TOOL-aSightedSkeptic-10 TOOL-aSightedSkeptic-13 |
| [2026-10-01-build-TOOL-aSightedSkeptic-7-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-7-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-2-3-fold-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-2-3-fold-brief.md) | journal | TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-7-2-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-7-2-build-brief.md) | journal | — |
| [2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md](../reviews/2026-10-01-review-TOOL-aSightedSkeptic-1-closing-diff-round1.md) | diff-review | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.template.js` runs every finder lens on every diff, while the review
protocol it ships beside says heavy multi-lens review over already-hardened code manufactures
refuted noise and tells the reader to review light. This unit gives the caller an `args.intensity`
of `'full'` or `'light'`. A light diff review runs a declared subset of the lenses, sweeps the
caller's whole checklist across the lenses that do run, and says in its log, its report and its
return which lenses it skipped.

## 2. Scope (IN)

- **S1** — `args.intensity` is read in the prelude, beside the `kind` refusal and before any agent
  spawns. Absent, it is `'full'`. Present, it must be a string and one of `full` and `light`; any
  other value or type throws `tier2-review: \`intensity\` must be one of full | light. Got <JSON of
  the value>.` The `args` header block gains an `intensity:` line naming both values and the default.
  The harness never picks `light` itself. Observed by AC1, AC2, AC9.
- **S2** — A spec audit given `intensity: 'light'` is refused by its own message, which says the spec
  kind has no light subset (§8 F2). `intensity: 'full'` is accepted on both kinds and changes nothing
  for the spec kind. Observed by AC1.
- **S3** — `LIGHT_LENSES`, a top-level array LITERAL of lens keys, sits beside `DIFF_LENSES` and holds
  `correctness`, `seams` and `verification` (§8 F1). A load-time check, run on every run of either
  kind and before the Resume phase, throws naming `LIGHT_LENSES` when the literal is empty or names a
  key `DIFF_LENSES` does not carry. Observed by AC5.
- **S4** — The skip happens INSIDE the Find thunk. `skippedLenses` is derived once: empty for the
  spec kind and for `'full'`, otherwise the keys of `LENSES` absent from `LIGHT_LENSES`, in `LENSES`
  order. The thunk's first arm returns, for a key in `skippedLenses`, a resolved sentinel
  `{ lens, path: '', findings: [], skipped: true }` and dispatches nothing. The receiver line
  `const LENSES = isSpec ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers` and the
  `boundedParallel(LENSES.map(...))` fan are unchanged in shape. The resume reuse loop passes over a
  skipped key, so no `reused find:<key>` line names a lens that will not run. Observed by AC2, AC8.
- **S5** — The counts read the sentinel as neither live nor dead. `lensesDead` counts null returns
  only; the live set holds the non-null, non-skipped returns; the every-lens-dead return fires when
  every lens that RAN died; and every lens denominator in a log line, a `note` or the RUN INTEGRITY
  block, and the success return's `agents`, use the running count, `LENSES.length` less the skipped
  count. `deadLensLabels` and `pending` never name a skipped lens. Observed by AC3.
- **S6** — A light run is announced. Before the Find phase it logs one `WARNING:` line naming every
  skipped key and saying their briefs were not run. The synthesis prompt states the intensity in the
  review-shape sentence on every run, and on a light run the RUN INTEGRITY block gains a clause
  naming each skipped key, saying their classes were swept only through the checklist shares, and
  telling the synthesis not to describe the run as a full review. The verdict token set is unchanged.
  Every return carries `intensity` and `skippedLenses`, on every exit path. A `lensNotes` key naming a
  skipped lens reached no prompt, so the log's `WARNING:` line and RUN INTEGRITY report it apart, as
  `lens notes for skipped lenses, unread`, and never as supplied for a lens that ran (rev-2).
  Observed by AC3, AC4.
- **S7** — The checklist split of `TOOL-aSightedSkeptic-4` is taken over the lenses that RUN: on a
  light run every item of `CHECKLIST_ITEMS` is assigned to exactly one lens outside `skippedLenses`,
  so a skipped lens takes no share and no item is lost with it. Observed by AC6.
- **S8** — `intensity` joins the `inputPrint` fingerprint, so a light run and a full run over the
  same other inputs derive different review keys and never reuse each other's lens files.
  `REVIEW_SHAPE` and the kit version are not touched. Observed by AC7.
- **S9** — `tools/workflows/README.md` documents `intensity`: both values, the default, that only the
  caller picks it, that a light run names its skipped lenses in its return and its report, and that
  a diff crossing a trust boundary is not one to review light. Observed by AC9.
- **S10** — The arms of §6 are written into `tools/workflows/tier2-review.test.sh`, each observed RED
  against the pre-change script, and its `FLOOR_ASSERTIONS` rises by the number of assertions this
  unit adds. The suite is not run in the pass. Observed by AC1, AC2, AC3, AC4, AC5, AC6, AC7.

## 3. Non-goals (OUT)

- Choosing the intensity automatically from the diff's size or history. The caller decides.
- Passing `intensity` from `tools/workflows/unattended-build.js` or any other caller. Every existing
  caller passes none and keeps `'full'`, byte-for-byte the review it gets today apart from the
  review-shape sentence.
- A light subset for the spec kind. S2 refuses it.
- Retuning `LIGHT_LENSES` from per-lens yield. That needs the lens-labelled ledger of
  `TOOL-aSightedSkeptic-8` and enough runs to read it; the literal is one edit away when they exist.
- Special handling of `args.lensNotes` naming a skipped lens. It names a lens of the current kind, so
  `TOOL-aSightedSkeptic-5`'s check accepts it, and the WARNING line names the skipped lens. S6's
  "unread" wording (rev-2) is reporting, not handling: the key is still accepted and still keyed.
- `MAX_VERIFIERS`, the verify batching, `tools/hooks/agent-cap.js`, `REVIEW_SHAPE` and the version.
- Any governance carrier. `memory/guides/REVIEW-PROTOCOL.md` says "Review light, or skip" and its
  M8 counterpart in `memory/guides/BUILD-METHOD.md` shows an invocation without `intensity`; both
  stay as they are and the main loop parks the wording for the owner.

### Edges

- **consumes-from** `TOOL-aSightedSkeptic-5` — the five `DIFF_LENSES` keys `LIGHT_LENSES` names;
  without `verification` the S3 check refuses every run.
- **consumes-from** `TOOL-aSightedSkeptic-4` — `args.checklist`, `CHECKLIST_ITEMS` and the per-lens
  split S7 narrows to the running lenses; without them AC6 has no input.
- **hands-off** `TOOL-aSightedSkeptic-8` — the ledger and the appendix it adds. A skipped lens raises
  no finding, so it contributes no ledger row, and the `ledger` and `confirmedFindings` keys join the
  same returns that carry `intensity` and `skippedLenses`.
- **hands-off** external — the REVIEW-PROTOCOL and BUILD-METHOD M8 wording, to the owner under the
  build's no-carrier rule.

## 4. Design

### Evidence

Read at `ef1dcdb6` on 2026-10-01, PINNED to that sha; the render `tools/workflows/tier2-review.js`
equals the template after `{{FANOUT_CAP}}` is substituted with 5, measured by the AC8 `sed | diff`.

- The Find fan is `boundedParallel(LENSES.map((L) => () => reusedLens.has(L.key) ?
  Promise.resolve(...) : agent(...)))` (template lines 484-522). Reuse already skips a dispatch
  inside the thunk, which is the seam S4 extends.
- `liveResults = finderResults.filter(Boolean)` and `lensesDead = LENSES.length - liveResults.length`
  (lines 528-529). A skipped lens returning null would count as dead and turn every light run into
  `deferred-platform`; hence the sentinel.
- `LENSES.length` is the denominator at lines 529, 546-547, 553, 562, 697 and 759, and `agents` adds
  it at line 935.
- `inputPrint` prints `context`, `byDesign` and `priorFindings` (line 396); the shared brief's
  invariant 5 puts every new input field into it in the unit that adds it.
- `tools/workflows/unattended-build.js:940` reads `lensesDead === 0` to call a spec-audit round
  clean. S2 keeps the spec kind off the light path, and S5 keeps a skip out of `lensesDead`.
- The protocol text the mechanism serves: `memory/guides/REVIEW-PROTOCOL.md` line 207, "Match
  intensity to target richness", and the same page's "Default configuration: 3–6 primed finder
  lenses".

### Data model

```
args.intensity   'full' | 'light'      optional; absent -> 'full'; anything else REFUSES
LIGHT_LENSES     ['correctness', 'seams', 'verification']   literal; checked against DIFF_LENSES
skippedLenses    string[]              derived; [] unless kind is diff-review and intensity is light
return.intensity      'full' | 'light'  every exit path
return.skippedLenses  string[]          every exit path; [] on a full run
```

### Spellings

```
tier2-review: `intensity` must be one of full | light. Got <json>.
tier2-review: a spec-audit has no light lens subset; `intensity` must be full or absent. Got "light".
tier2-review: LIGHT_LENSES names <key>, which DIFF_LENSES does not carry.
WARNING: intensity light — the <k1>, <k2> lens(es) were NOT run; their classes are swept only through the checklist shares
```

### Inventory

Minted: `LIGHT_LENSES`, `skippedLenses` and the return fields `intensity` and `skippedLenses`. None
is a function definition, so no `js.function` cell grades them; `.lexicon.conf` grades names a
definition leads with.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (the render, regenerated in the same commit)
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`

### Rollout

Default-off by construction: an absent `intensity` is `'full'`, and every existing caller passes
none. The key moves for every run because the print gains a field, which `REVIEW_SHAPE` already
moved once for the build, so no new reuse loss is introduced.

### Alternatives rejected

- **A skipped lens returns null.** Null is how a dead agent reaches the script, so every light run
  would exit `deferred-platform` with the skipped lenses pending forever.
- **Fan over a filtered receiver** (`LENSES.filter(...)`). `tools/hooks/agent-cap.js` denies a
  receiver it cannot size, and the build's invariant 4 forbids reshaping it.
- **A third lens literal, `LIGHT_DIFF_LENSES`, selected by a second ternary.** The hook admits one
  marked receiver of two literal branches; a third set multiplies receivers for a subset the thunk
  can express.

## 5. Production-readiness checklist

- security — a light run does not run the `security` lens. The caller picks it, the README says a
  diff crossing a trust boundary is not one to review light, and the report and return name the
  skip. No new input reaches a shell: `intensity` is checked against a closed set before use.
- perf / scale — a light run dispatches three finder agents instead of five; the verify stage is
  unchanged and stays capped by `MAX_VERIFIERS`.
- error / empty / loading states — a bad value refuses before any spawn (S1, S2); an empty or stale
  `LIGHT_LENSES` refuses every run (S3); a light run whose running lenses all die defers naming only
  them (S5).
- observability — one WARNING line, a RUN INTEGRITY clause, and two return fields per run.
- risks — the light subset is chosen from a sample that carries no lens labels (§8 F1); a light run
  can miss a security defect that the security lens alone would have found. Both are stated in the
  README and the report rather than hidden.
- testing — the §6 arms in `tools/workflows/tier2-review.test.sh`, each observed RED against the
  pre-change script; the suite runs once, at VERIFYING.
- migration — none: absent is the old behaviour.
- user docs — `tools/workflows/README.md` (S9); the harness's `args` header (S1).

## 6. Acceptance criteria

- **AC1** — Arms `intensity: an unknown value is refused`, `intensity: a non-string is refused`,
  `intensity: light on a diff review proceeds`, `intensity: absent proceeds`,
  `intensity: light on a spec audit is refused` and `intensity: full on a spec audit proceeds` pass
  in the prelude half of the harness self-test named under §7, the refusals matching `intensity`.
  Red when: the validator is absent and `'medium'` proceeds, or it refuses every value.
- **AC2** — Arm `intensity: light dispatches only the light lenses` passes: a light diff run's
  `find:` labels are exactly `find:correctness find:seams find:verification`, and a run with no
  `intensity` dispatches all five `DIFF_LENSES`.
  Red when: a light run dispatches `find:security` or `find:intent`, or an absent value runs fewer
  than five.
- **AC3** — Arm `intensity: a skipped lens is neither live nor dead` passes: a light run where every
  running lens returns exits `complete` with `lensesDead` 0, `intensity` `light`, `skippedLenses`
  `security intent` and an `agents` count holding three lenses; a light run whose three running
  lenses all return null exits `deferred-platform` with `pending` naming exactly those three.
  Red when: a skip is counted dead, or the every-lens-dead test still compares against
  `LENSES.length`.
- **AC4** — Arm `intensity: a light run announces its skipped lenses` passes: the light run's log
  holds a `WARNING:` line naming `security` and `intent`, and its `synth` prompt's RUN INTEGRITY
  block names both and the word `light`; a full run's `synth` prompt names the intensity `full` and
  carries no skipped-lens clause.
  Red when: a lens is skipped silently, or the full run's report is told lenses were skipped.
  Arm `intensity: a lens note for a skipped lens is reported unread` passes too (rev-2): a light run
  given `lensNotes {security: …}` carries, in RUN INTEGRITY,
  `lens notes supplied for: no lens that ran; lens notes for skipped lenses, unread: security.`,
  never `lens notes supplied for: security`, and logs a `WARNING:` line naming `unread: security`.
  Red when: a note no prompt carried is reported as supplied for a lens.
- **AC5** — Arm `intensity: LIGHT_LENSES must name live lenses` passes: a copy of the script whose
  `LIGHT_LENSES` literal names `verificaton` throws naming `LIGHT_LENSES` with no agent traced, and
  so does a copy whose literal is empty.
  Red when: a renamed lens empties the light set and a light run reviews nothing while reporting
  clean.
- **AC6** — Arm `intensity: every checklist item reaches a running lens` passes: a light run given a
  six-item `checklist` carries each item's text in exactly one `find:` prompt, and the full run over
  the same checklist does too.
  Red when: the split is taken over all five lenses and the items assigned to `security` or
  `intent` reach no prompt.
  fixture: needs `args.checklist` from `TOOL-aSightedSkeptic-4`, built before this unit.
- **AC7** — Arm `intensity: the key differs by intensity` passes: a light run's `key` differs from a
  full run's over identical other args, a `correctness` lens file carrying the full run's key is
  dispatched in the light run, and one carrying the light run's own key is reused.
  Red when: `intensity` is left out of `inputPrint`.
- **AC8** — When `node tools/workflows/check-workflow-syntax.js` and
  `bash tools/workflows/check-verifier-fanout.sh` run, both exit 0, and
  `sed 's/{{FANOUT_CAP}}/5/g' tools/workflows/tier2-review.template.js | diff - tools/workflows/tier2-review.js`
  prints nothing.
  Red when: the thunk's skip arm reshapes the receiver and the hook denies the harness, or the render
  was hand-edited or not regenerated.
- **AC9** — When `grep -c 'intensity' tools/workflows/README.md` runs it prints at least 1, where BASE
  prints 0, and the existing arm `the args header documents all` passes with `intensity` among the
  fields read off `a`.
  Red when: the new argument is read and documented nowhere.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `verifier fan-out self-test` · `review-join ban (no ref-keyed join)` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `tier2-review self-test` · `unattended-build self-test` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/workflows/tier2-review.test.sh` · the seven arm groups of AC1 to AC7, prelude and whole-script, each staged RED on the pre-change script · `FLOOR_ASSERTIONS` raised by the assertions added

The harness cannot observe a live agent obeying the RUN INTEGRITY clause; the arms read the prompt
it is handed, which is what the self-test's own header says it grades.

## 8. Open questions

- **F1 — Which lenses does a light run keep?** The evidence is the owner's 84-finding sample, PINNED
  at 2026-10-01 in the build's spec brief: runtime defects 42, could-not-fail checks 16, stale text
  12, spec mismatch 6, and 8 unclassed. The sample carries no lens labels, so mapping a class to a
  lens is a judgement: runtime defects to `correctness`, could-not-fail checks to `verification`,
  stale text (two carriers of one fact disagreeing) to `seams`, spec mismatch to `intent`. Options:
  (a) `correctness`, `verification`, 58 of 76 classed findings, two lenses; (b) `correctness`,
  `seams`, `verification`, 70 of 76, three lenses; (c) `correctness`, `verification`, `security`,
  58 of 76 plus a class the sample does not count; (d) `correctness`, `verification`, `intent`, 64 of
  76. (a) falls below the review protocol's stated three to six lenses, a carrier this build may not
  edit, so it leaves that text contradicted; (c) rests its third lens on no count, and the protocol
  names defence-in-depth findings over hardened code as the noise a light review exists to cut;
  (d) covers fewer classed findings than (b) at the same cost. Recommendation (b). RESOLVED (agent,
  2026-10-01, delegated): (b), the survivor covering the most classed findings inside the
  protocol's stated lens range; the checklist split (S7) still sweeps every class on the three.
- **F2 — What does the spec kind do with `intensity: 'light'`?** (a) Refuse. (b) Ignore it and
  announce. The spec kind's four lenses are M4's catalogue and no light subset of them is defined;
  ignoring would hand a caller a full audit it asked not to pay for, and announce it only in a log.
  The shared brief's invariant 3 makes a value outside what the kind accepts a refusal. Recommendation
  (a). RESOLVED (agent, 2026-10-01, delegated): (a), refuse; `'full'` stays legal on both kinds.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the owner's mandate, the build's spec brief, and the
  harness template and its self-test read at `ef1dcdb6`.
- rev-2 · 2026-10-01 · fold of closing review round 1, L6 (finding 11; its sibling finding 7 was
  refuted as by design under the §3 non-goal): RUN INTEGRITY listed a light run's note for a skipped
  lens as supplied. S6 now reports such notes apart as unread, in the log and RUN INTEGRITY, which is
  wording only and leaves the non-goal standing. AC4 gains the arm.

## 10. Reuse audit

The probe `python tools/codebase-map/reuse_lookup.py "review harness runs a reduced set of finder
lenses for a small diff"` returned only name-stem neighbours outside `tools/workflows/` (`run`,
`build_run_model`, `resolve_pattern_sets`), none of them a seam for this change, and it reports
`unscanned layers: .sh`. No existing seam fits outside the harness, so the seams extended are the
harness's own, read at source: the reuse arm of the Find thunk (template line 486), which already
skips a dispatch in place; the `KINDS` refusal (lines 132-140), which S1 and S2 copy in shape; the
`inputPrint` fingerprint (line 396); and the RUN INTEGRITY block (lines 758-764). The recall query
put `memory/guides/REVIEW-PROTOCOL.md`'s "Match intensity to target richness" and the archived
charter's "review light or skip" at the top, the rule this unit gives a mechanism, and found no
record of a light mode built or refused before.

Recall terms used: `python tools/memory-recall/query.py "how should a review harness skip finder lenses for a light review of a small or hardened diff" --terms "tier2-review lens intensity light skipped lenses fan-out agent-cap thunk precision hardened RUN INTEGRITY"`
