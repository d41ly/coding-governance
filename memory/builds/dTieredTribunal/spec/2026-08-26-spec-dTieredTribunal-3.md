# TOOL-dTieredTribunal-3 — the two drift-audit harnesses gain the trust accounting their sibling already carries

**Status:** INPROGRESS · rev-4 · 2026-08-26 · node a · Tier-2 · base da9e4cd2 · order 2 · streams tooling · ratified 2026-08-26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-2 |
| [2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round2.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round2.md) | spec-audit | TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-2 |
| [2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round3.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round3.md) | spec-audit | TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-2 |

<!-- /gen:spec-records -->

## 1. Goal

Three files in `tools/workflows/` implement one review pipeline three times, and two of them carry
only two of the guards the third learned from shipped defects. Section 4's Inventory is the derived
list and this sentence agrees with it rather than rounding it up. `drift-audit-state.js` reports
the CONFIGURED lens set rather than the surviving one, so a dead lens is invisible to its caller.
Neither sibling counts a dead lens, a dead skeptic, a spurious verdict or a contradictory one, and
both resolve a disagreeing repeat by keeping whichever verdict arrived first. The merge bar is green
over all of it. Port the accounting, so the two siblings can no longer report a clean bill for a run
that reviewed or judged nothing. One further hardening in `tier2-review.js` is deliberately left
unported and is named in section 3, so this unit claims the accounting rather than the whole delta.

## 2. Scope (IN)

- **S1** — both siblings count dead lenses. `drift-audit-state.js:234` and
  `drift-audit-code.js:218` each do `finderResults.filter(Boolean)` and discard the drop count; each
  gains a `lensesDead` value derived as the configured count minus the surviving count.
- **S2** — both siblings count dead skeptic batches, derived the same way over their verdict batches
  at `drift-audit-state.js:306` and `drift-audit-code.js:287`.
- **S3** — `drift-audit-state.js:378` stops returning `LENSES.map((L) => L.slug)`, the CONFIGURED
  set, and returns `lensesRun` as the surviving lens COUNT, an integer, in the shape
  `tier2-review.js:400` already uses AT THE PINNED BASE. That citation is a base pin, not a live one:
  unit 1 is `order 1` and edits the same file, so the line will have moved by the time this unit is
  built. Section 4's Inventory carries the same disclosure for the same reason. `drift-audit-code.js` returns no lens information at all today
  and gains the same `lensesRun` plus `lensesDead` pair. Neither sibling returns lens SLUGS: the
  slug list is out of scope and section 4 records why.
- **S4** — both siblings gain the all-lenses-dead early return: when every configured lens failed to
  return, log that nothing was reviewed and return with the counters, rather than proceeding to
  synthesize a report over an empty finding set. The predicate is
  `LENSES.length > 0 && lensesDead === LENSES.length`, never `lensesDead === LENSES.length` alone.
  `drift-audit-state.js:224` builds `LENSES` by filtering `ALL_LENSES` against a caller-supplied slug
  list, so a caller passing a typo'd slug yields an empty array and the bare predicate reads
  `0 === 0`. That reports a misconfiguration as a degraded run, which is this repo's own
  vacuous-selector-empty-population class. A zero-length `LENSES` therefore takes its own branch and
  returns a distinct `note` naming the misconfiguration rather than the lens deaths.
  `drift-audit-code.js:116` declares `LENSES` as a literal with no caller filter, so its lens set
  cannot be empty; it takes the same guarded predicate anyway, because these two files are copies of
  one another and a guard present in only one of them is the divergence this unit exists to close.
- **S5** — both siblings count a spurious verdict, an agreeing duplicate, and a contradictory repeat,
  and a contradictory repeat DEMOTES its finding to unverified rather than keeping the first
  verdict. This replaces the first-write-wins guard `if (typeof v.id === 'number' && !vmap.has(v.id))`
  that both files carry, at `drift-audit-state.js:308` and `drift-audit-code.js:289`. The verdict
  vocabulary in these two files is TERNARY where `tier2-review.js` is binary: both enum
  `['confirmed', 'refuted', 'partial']`, at `drift-audit-state.js:252` and
  `drift-audit-code.js:239`. The rule is therefore stated over TOKENS and not over agreement in the
  abstract. A repeat whose verdict token is identical to the standing one increments `duplicates`. A
  repeat whose verdict token differs from the standing one is a conflict and demotes the finding to
  unverified. `partial` is a distinct token, so a `partial` arriving against a standing `confirmed`
  is a conflict and is not partial agreement. A demoted finding carries its own reason string naming
  the two tokens that disagreed: today a finding absent from `vmap` renders
  `reason: 'no verdict returned'` at `drift-audit-state.js:316`, which is false of a demotion, where
  two verdicts did return, and that false reason is serialized into the synthesis prompt and into
  the report. A `severityCorrection` carried by a demoted verdict is discarded with it. That loss is
  stated rather than left silent, and this unit adds no field to carry it. It has a downstream
  consequence worth naming, because a demotion is new behaviour: `drift-audit-code.js:309` derives
  `downgrades` by counting `judged` entries whose verdict is `partial` and which carry a
  `severityCorrection`, and returns that as `severityCorrections`, which is interpolated into the
  synthesis prompt. A `partial` demoted to unverified therefore leaves that count, correctly, because
  the verdict was withdrawn. It is stated here so a builder does not read the drop as a bug.
- **S6** — both siblings gain the synthesis-death log: when the synthesis agent returns null, log
  every confirmed and unverified finding before returning, so the findings are not lost silently.
- **S7** — every return block carries the same field set. There are FOUR exits per sibling after
  this unit, not two, and each carries `lensesRun`, `lensesDead`, `skepticsDead`, `conflicts`,
  `duplicates`, `spurious` and `note`. They are the success return, the all-lenses-dead return S4
  adds, the zero-configured-lenses return S4 adds beside it, and the synthesis-death path, which S6
  makes loud but which falls through to the success return rather than exiting on its own. An earlier
  revision of this bullet said "the success path AND the new early path" and counted one new exit
  where S4 creates two, which is exactly the asymmetry this unit exists to remove.
  Each file's `note` distinguishes a complete run from a degraded one, in the shape
  `tools/workflows/tier2-review.js` already uses.
- **S8** — each ported guard carries a comment naming the unit that originally earned it in
  `tier2-review.js`, so the provenance travels with the code rather than being re-lost.
- **S9** — the drift-audit kit version moves from `1.6` to `1.7`, at every site
  `tools/check-kit-versions.sh:169-194` binds together. Those sites are
  `tools/drift-audit/drift_report.py:51` (`KIT_DRIFT_AUDIT_VERSION = "1.6"`), the
  `gov:kit drift-audit@1.6` marker at `tools/drift-audit/README.md:3`, and the `version:` line and
  the `gov:kit drift-audit@1.6` marker at lines 3 and 15 of EACH sibling. The checker asserts each
  sibling's `meta.version` equals the kit constant and that its own inline marker equals its
  `meta.version`, so a partial bump reds the unguarded `kit version markers` leg. The bump is owed
  because the harnesses ship the kit's return contract and this unit changes it.
  The README edit is NOT the marker byte alone. `tools/drift-audit/README.md:7` carries a
  `Migrating 1.0 to 1.1` paragraph stating what an adopter must change and why, which is this kit's
  established convention for a contract move, and a bump that skips it leaves an adopter reading a
  migration note for a version two behind. S9 adds the matching paragraph, and it is headed BREAKING,
  because this move is. Its content is what an adopter has to know and no more, in this order. First,
  `lensesRun` in `drift-audit-state.js` was an ARRAY of slug strings and becomes an INTEGER, so a
  caller reading it as a list breaks; section 4 Migration carries the evidence that no tracked caller
  does. Second, the return objects gain the other six fields and those are additive, so an adopter
  passing the same `args` needs no edit. Third, a run whose lenses all died now returns early instead
  of synthesizing a report over nothing. An earlier revision of this bullet called the whole move
  additive, which contradicted section 4 Migration of this same spec.
- **S10** — `memory/map/features/review-harnesses.md` has its Gaps section refreshed in the same
  commit as the code. Its first bullet states this unit's delta as live fact, and landing this unit
  falsifies every clause of it, including the two an earlier revision of this bullet did not
  enumerate: that `drift-audit-code.js` returns no lens information at all, and that both siblings
  resolve a disagreeing repeat by keeping whichever arrived first. Three gaps stay standing, and one
  of them is CORRECTED rather than frozen. The `args` parse bullet currently names only
  `drift-audit-state.js`. The defect is live in BOTH siblings, at `drift-audit-state.js:47` and
  `drift-audit-code.js:48`, which are byte-identical, and which is what section 3 and backlog row
  `TOOL-dTieredTribunal-4` both record. The refresh widens that bullet to both files. The other two
  stay verbatim: the absent review-KIND parameter, and the inline-script modality no file gate can
  see.

## 3. Non-goals (OUT)

- **Merging the three files into one engine.** That is the research record's engine-and-profile
  proposal, priced as expensive, and the runtime forecloses the obvious shape because workflow
  scripts cannot import. This unit duplicates the guards deliberately, which the governance template
  already instructs for exactly this runtime reason.
- **Any review-KIND parameter, on any of the three files.** Parked at the build level.
- **The `args`-must-be-an-object guard, deliberately NOT ported.** `tier2-review.js:32-60` parses a
  string `args` as JSON and then refuses anything without an explicit `repo`. Both siblings are
  `const a = args || {}` with no parse, at `drift-audit-state.js:47` and `drift-audit-code.js:48`,
  so a caller handing either one a prose string falls back to `REPO = '.'` and audits whatever
  directory the process is standing in. The defect is real, live in both files, and worse than a
  false clean: the recorded consequence in the source file's own comment is auditing a DIFFERENT
  repository twice and returning confident findings about it. It is excluded here because it is an
  input-validation change on a different surface from the accounting, and it survives this build as
  backlog row `TOOL-dTieredTribunal-4` rather than as an unwritten intention.
- **Changing either sibling's lenses, prompts, subjects, caps, or output paths.** The audits keep
  finding what they find; only the accounting around them changes.
- **Changing `tools/workflows/tier2-review.js`.** That file is the source being copied FROM, and the
  unit before this one is the only one that edits it.
- **A shared helper file.** Workflow scripts cannot import, so there is nowhere to put one.
- **Tightening the fan-out guard's marked-derivation branch.** `drift-audit-state.js:224` uses that
  branch and the research reproduced a hole in it. Fixing the hook is a separate unit and is a
  follow-up, recorded in section 8.

## 4. Design

### Inventory

The delta this unit PORTS, derived by reading all three files at the pinned base. Every row is a
guard present in `tier2-review.js` and absent from both siblings. The table lists the ported set and
is NOT the whole delta: the `args` parse-then-validate guard is a further absence, it has no row
here, and section 3 records why it is excluded.

| Guard | In `tier2-review.js` | In either sibling |
|---|---|---|
| dead-lens count | `:206` | absent |
| all-lenses-dead early return | `:213` guard, `:215` return | absent |
| dead-skeptic count | derived over its verdict results | absent |
| spurious-verdict count | `:277` | absent |
| duplicate-verdict count | `:280` | absent |
| contradictory repeat demotes to unverified | `:281` and `:283` | absent, first write wins |
| synthesis-death log | `:381` | absent |
| surviving lens count on the return | `:400` | `state.js` returns the configured set, `code.js` returns none |

TWO further absences are out of scope, and both are named, because a completeness disclosure that
names one of two is worse than none at all. The first is the `args`-must-be-an-object guard, carried
by section 3 and by backlog row `TOOL-dTieredTribunal-4`. The second is `tier2-review.js:220-225`,
the nothing-raised early return, which neither sibling has and which this unit does not add. It fires
when the lenses lived and raised nothing, a state distinct from every exit S4 adds.

Two guards are already present in both siblings and are NOT in scope: the orchestrator-assigned
integer join key, and the rule that a finding with no verdict is unverified rather than refuted.
Both were verified by reading the files rather than assumed.

### Data model

Each sibling's return block gains `lensesRun` as the SURVIVING count, `lensesDead`, `skepticsDead`,
`conflicts`, `duplicates`, `spurious`, and a `note` string. The existing `counts` object and
`precision` are unchanged.

`lensesRun` is an integer in both siblings after this unit, and no slug list replaces it. The
survivor identities are not returned because they are not derivable at the point the return is
built: `r.lens` is agent-typed free text with no enum, invited by the prompt rather than assigned by
the harness, and `finderResults.filter(Boolean)` has already destroyed the index alignment that
would let the harness answer the question from its own configuration. `r.lens` is DISPLAY ONLY, the
same status `tier2-review.js` gives `ref`, and it is never the source of a count. A future unit
wanting the survivor identities computes them from position before the filter and returns them under
a distinct key; overloading `lensesRun` with them is the echo-drift shape the integer join exists to
kill.

BOTH new early returns carry those seven fields, not one. S4 creates two branches and they are not
interchangeable. On the all-lenses-dead branch `lensesRun` is zero, `lensesDead` equals the
configured count, `skepticsDead` is zero because no skeptic ran, and `note` names the lens deaths. On
the zero-configured-lenses branch all three counts are zero and `note` names the MISCONFIGURATION
instead, because reporting a typo'd slug list as a degraded run is the vacuous-selector class S4
exists to refuse. Both carry the report and summary null.

One field is deliberately NOT in the seven and is named here so the omission is not read as an
oversight. `drift-audit-code.js:369` returns `severityCorrections`, derived from `downgrades` at
`:309`, and it belongs to that sibling alone. It stays where it is, on the success return only,
because it counts an adjudication that cannot have happened on any path where the pipeline exited
early. S7's seven-field list is closed over the fields BOTH siblings share.

This is the property the prior-art refusal insists on: every counter on every exit path, or the port
is the same refusal on a different filename.

### Migration

This unit contains exactly one BREAKING shape change, and it is `lensesRun` in
`drift-audit-state.js:378`. That field is an ARRAY of slug strings today and becomes an integer, so
its type and its meaning both change. Every other field in this unit is additive. The safety
argument is not that nothing changes — it is that no tracked caller reads either sibling's return
shape, so the change has no reader to break. That was verified rather than assumed: a repo-wide
search for `lensesRun` at the pinned base finds it only where the three harnesses WRITE it, and
nowhere reading it. A caller that did read `lensesRun` as a list would break loudly on a type error
rather than silently on a wrong value.

The second behavioural change a caller can observe is the new early return, which fires only when
every configured lens died, a case that today produces a synthesized report over an empty finding
set.

### Files touched (estimate)

- `tools/workflows/drift-audit-state.js` and `tools/workflows/drift-audit-code.js` — the ported
  accounting, S1 through S8.
- `tools/drift-audit/drift_report.py` and `tools/drift-audit/README.md` — the kit version bump S9
  owes outside `tools/workflows/`.
- `memory/map/features/review-harnesses.md` — the dossier whose Gaps section this unit falsifies,
  refreshed under S10 in the same commit as the code.

No re-render of `memory/map/generated/` is owed. S10 edits dossier PROSE only and leaves the
`[claims]` block untouched, and the generated artifacts carry claims rather than prose, so
`codebase-map coverage + freshness` has nothing new to compare. No kit descriptor row names either
sibling, so none is updated. Of the three scanners that grade these files,
`tools/workflows/check-review-join.sh` takes every `tools/**/*.js` with no marker filter, while
`check-verifier-fanout.sh` and `check-workflow-syntax.js` both select on the `export const meta =`
marker that both siblings carry and must keep.

### Alternatives rejected

- **A rendered engine emitting all three files from one source, with a parity gate.** Rejected as a
  build in itself, and it walks into the recorded refusal on any replacement engine unless every
  counter survives on every exit path of every profile, which is what this unit does directly and
  cheaply.
- **Leaving `drift-audit-code.js` alone because it returns no lens information at all.** Rejected:
  returning nothing is not safer than returning the wrong thing, it is the same false-clean with
  fewer words.
- **Making the contradictory-repeat rule last-write-wins instead of demote-to-unverified.** Rejected.
  Two skeptics disagreeing is exactly the state where the harness does not know, and the recorded
  defect that produced the current rule in the sibling was a last-write-wins collision.
- **Collapsing any `partial` against a `confirmed` into `partial` rather than into a conflict.**
  Rejected. The two tokens are two different answers from two skeptics about one finding, and the
  harness has no ground for preferring the weaker one; a token mismatch is a conflict whatever the
  tokens are.
- **Returning the surviving lens slugs alongside or instead of the count.** Rejected for this unit,
  on the derivation recorded under Data model above.

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path, and no new outbound request. The one live
  input-validation gap in these files is named as a non-goal in section 3 and carried out of this
  build as `TOOL-dTieredTribunal-4`.
- perf / scale — N/A. No new agent, and the new early return strictly reduces work by skipping a
  synthesis over an empty set.
- a11y — N/A. These are workflow scripts with no user interface.
- i18n — N/A. Same reason.
- error / empty / loading states — this unit IS the empty-state work. The all-lenses-dead path, the
  zero-configured-lens path and the dead-synthesis path are three of the FOUR empty states this
  subject has, and none of the three is currently handled. The fourth is the nothing-raised path —
  the lenses lived and returned no findings — which `tier2-review.js:220-225` handles and neither
  sibling has. It is named in section 4 as out of scope and is named here too, because a unit whose
  whole subject is exit-path accounting may not count its own subject differently in two sections.
- observability — the counters ARE the observability. A caller can currently not tell a full audit
  from one where half the lenses died.
- risks — the demote-to-unverified rule can move a finding out of the confirmed set that the
  first-write-wins rule would have confirmed. That is the intended correction and it lowers reported
  precision on a degraded run, which is the honest number.
- testing + left-shift gates — the acceptance observations are direct reads of both files plus the
  three shipped scanners and `tools/check-kit-versions.sh`. A new leg asserting that a return block
  names a field would be satisfiable by its own comment prose, which is the class the merge bar is
  full of gates against.
- migration / rollback — revert the files named under Files touched, together and not singly.
- user docs — none. Both scripts are agent-facing and their headers are their documentation.

## 6. Acceptance criteria

- **AC1** — When `grep -nE 'lensesDead|skepticsDead|spurious|conflicts|duplicates|note:' tools/workflows/drift-audit-state.js tools/workflows/drift-audit-code.js`
  runs, it returns hits in both files. At the pinned base that command exits non-zero with no output,
  which was run rather than assumed. This criterion observes presence only; AC8 is the one that binds
  the fields to a return block.
- **AC2** — When `drift-audit-state.js` is read, its return no longer contains
  `lensesRun: LENSES.map((L) => L.slug)`. When EACH sibling is read, the value it returns for
  `lensesRun` is an integer derived from the length of the post-`filter(Boolean)` survivor array
  rather than from any `r.lens` string. Both files, because `drift-audit-code.js` returns no lens
  information today and gains the field new, so a criterion scoped to its sibling alone would let it
  ship the configured count. That is the precise defect this unit ports a guard to prevent.
- **AC3** — When each sibling's verdict-join loop is read, a verdict carrying an id the run never
  assigned increments a `spurious` counter; a repeat whose token equals the standing one increments
  `duplicates`; and a repeat whose token differs from the standing one removes that finding from the
  confirmed set. When a demoted finding is read in the `judged` map, its `reason` is not
  `'no verdict returned'` and names the two tokens that disagreed.
- **AC4** — When each sibling is read, an all-lenses-dead condition returns above its
  `const synth = await agent(` call, at `drift-audit-state.js:332` and `drift-audit-code.js:316` at
  the pinned base, and that early return carries `lensesDead` and `skepticsDead` exactly as the
  success return does. The condition tests `LENSES.length > 0` as well as
  `lensesDead === LENSES.length`, and a zero-length `LENSES` reaches a different branch with a
  different `note`.
- **AC5** — When each sibling is read, a falsy `synth` is logged together with every confirmed and
  unverified finding before the function returns, matching the guard in
  `tools/workflows/tier2-review.js`.
- **AC6** — When `node tools/workflows/check-workflow-syntax.js` runs, it exits zero over both
  edited files.
- **AC7** — When `bash tools/workflows/check-review-join.sh` and
  `bash tools/workflows/check-verifier-fanout.sh` run, both stay green over both edited files.
- **AC8** — When the THREE return blocks of each sibling are read — the success return, the
  all-lenses-dead return and the zero-configured-lenses return — each names all seven of
  `lensesRun`, `lensesDead`, `skepticsDead`, `conflicts`, `duplicates`, `spurious` and `note`. A
  field present in one block and absent from another fails this criterion, because that asymmetry is
  the defect this unit ports the guards to prevent. Three blocks and not two: S4 creates two early
  branches, and a criterion naming one of them leaves six of the seven fields unbound on the other.
  `severityCorrections` is outside this criterion by section 4's Data model, which says why.
- **AC8b** — When
  `grep -n 'dTieredTribunal-3' tools/workflows/drift-audit-state.js tools/workflows/drift-audit-code.js`
  runs, it returns a hit adjacent to every guard S8 covers in both files, and reading each hit shows
  the comment naming the unit that originally earned that guard in `tier2-review.js`. `grep -n` and
  not `grep -c`: a count per file cannot show WHERE the comments are, and the criterion is about
  their placement, which is also why the second clause is an act of reading rather than something the
  grep itself asserts. Spec-1's AC7 states the identical obligation the identical way. S8 was the
  only scope item in this spec no criterion observed, and section 10 rests the whole port on that
  provenance travelling with the code.
- **AC9** — When `bash tools/check-kit-versions.sh` runs, it exits zero, and
  `grep -rn 'drift-audit@1\.6' tools/drift-audit/ tools/workflows/` returns no hits.
- **AC9b** — When `tools/drift-audit/README.md` is read at HEAD, it carries a migration paragraph
  naming the move to the new version, in the shape its existing `Migrating 1.0 to 1.1` paragraph
  uses, and that paragraph is marked BREAKING and states all three clauses S9 requires: the
  `lensesRun` array-to-integer change first, then that the other six added fields are additive, then
  the new early return. A paragraph calling the move additive fails this criterion, because section 4
  Migration of this spec says the opposite. A marker byte moved without any paragraph satisfies
  `check-kit-versions.sh` and still leaves the adopter reading a note for the wrong version.
- **AC10** — When `memory/map/features/review-harnesses.md` is read at HEAD after this unit lands,
  its Gaps section no longer claims ANY of the ten clauses below, which are S10's enumeration
  expanded to one clause per claim: that the two siblings
  lack the dead-lens count, the all-lenses-dead early return, the dead-skeptic count, the spurious
  counter, the duplicate counter, the conflict counter or the synthesis-death log; that
  `drift-audit-state.js` returns the configured lens set; that `drift-audit-code.js` returns no lens
  information at all; and that both resolve a disagreeing repeat by keeping whichever arrived first.
  Its `args` bullet names BOTH siblings and both line numbers. Its other two remaining gaps, the
  absent review-KIND parameter and the inline-script modality, are unchanged from today.

## 7. Gates

This unit adds no gate leg. Every name and every guard below was read from `tools/gate-legs.json`
rather than typed from memory. The list is the legs whose SUBJECT this unit touches, and it is NOT
the run's full leg set, so a builder runs the bar and reads the manifest, never this paragraph, for
what will execute.

TWO INDEPENDENT THINGS DECIDE WHETHER A LEG RUNS, and reading only the guard is how this paragraph
was wrong on its first draft. A `guard` scopes a leg to a diff. A `subject` of `kit` makes
`tools/run-gates/run-gates.sh:741` HOLD the leg entirely unless `GATE_SELFTESTS=1` is set, whatever
its guard says. So an unguarded leg does NOT run on every bar, and a guarded leg that arms may still
be held. A Definition of Done therefore needs the run that sets both `GATE_SELFTESTS=1` and
`GATE_FULL=1`.

Carrying no guard AND `subject: repo`, so they run on every bar and this unit must not red any:
`workflow script syntax`, `review-join ban (no ref-keyed join)`, `verifier fan-out`,
`agent-cap restatement`, `kit version markers`, `drift-audit wiring`, `drift-audit records`,
`codebase-map coverage + freshness` and `memory hygiene`.

Guarded on `tools/workflows/`, so the two harness edits ARM them. Only the last actually runs on a
default bar: `review-join self-test` and `verifier fan-out self-test` both carry `subject: kit` and
are held, while `review-protocol parity (kit vs dogfood)` is `subject: repo` and runs.

`drift-audit selftest` is guarded on `tools/drift-audit/` and `tools/lib/` and on nothing else, so a
diff confined to `tools/workflows/` cannot arm it. It arms for this unit only because S9 edits
`tools/drift-audit/drift_report.py` and `tools/drift-audit/README.md`, and it is named here for that
reason alone. A build that drops S9 drops this leg with it. It is also `subject: kit`, so arming it
still leaves it held until `GATE_SELFTESTS=1`.

## 8. Open questions

- **F1 — should the ported spurious and conflict counters also be asserted by a gate, rather than
  only read?** The research measured a candidate hook predicate for an uncounted `filter(Boolean)`
  and found it would red BOTH of these files, correctly, as live instances. Options seen: port the
  guards only and leave the predicate for a later unit; or port the guards and wire the predicate in
  the same unit, which requires observing its failing case and re-running it over the whole tree
  first. RESOLVED (agent, 2026-08-26, delegated): port the guards only. The predicate is a change to
  `tools/hooks/agent-cap.js`, which is the enforcement point the review protocol binds, and the
  research also reproduced a separate live hole in that file's marked-derivation branch. Wiring one
  predicate into a file with a known open hole, inside a unit whose subject is two other files, is
  two mechanisms in one spec. Follow-up: the hook work is its own unit and this run does not open it.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft, authored by the unattended run under the standing mandate.
- rev-2 · 2026-08-26 · spec-audit round 1 folded. Findings 7, 16 and 47: `lensesRun` is the
  surviving COUNT in S3 and in section 4, and Migration now states plainly that this is a breaking
  type-and-meaning change on `drift-audit-state.js:378` rather than claiming every field is
  additive. Finding 33: the slug list is refused rather than derived, and section 4 records that
  `r.lens` is display-only — this departs from the finding's proposed fix, which was to derive
  survivors from position, because the count is what the return needs. Findings 17 and 50:
  `memory/map/features/review-harnesses.md` joins Files touched, S10 requires its Gaps section
  refreshed in the same commit, and AC10 reads it at HEAD. Finding 29: the inventory citations move
  to `:206`, `:213` with `:215`, and `:400`, aligning the all-lenses-dead return with spec-1 S3.
  Finding 9: S4 splits the predicate so an empty `LENSES` takes its own branch, and it now records
  that only `drift-audit-state.js:224` can produce one — `drift-audit-code.js:116` is a literal.
  Finding 36: S5 states the rule over the ternary token set both siblings enum, where a token
  mismatch of any kind is a conflict; this follows the ratified reading rather than the finding's
  proposed `partial`-collapses-to-`partial` rule, and S5 also gives the demotion its own reason
  string. S1 through S8 keep their round-1 numbering so the review record's citations still resolve.
  Finding 8: AC1 gains `duplicates` and `note:`, and AC8 is the new return-block-scoped criterion.
  Finding 49: section 3 names the un-ported `args` guard explicitly and cites backlog row
  `TOOL-dTieredTribunal-4`; section 1 no longer claims the siblings lack every hardening. Finding
  28: the header tail carries `ratified 2026-08-26` for F1. Findings 24 and 39: section 7 is
  rewritten from `tools/gate-legs.json` with each leg's guard stated, and its opening paragraph now
  says the list is not the run's full leg set. Finding 39's version half is REFUSED as it was
  written: it asked section 4 to record no bump, and S9 records a bump from `1.6` to `1.7` instead,
  at every site `tools/check-kit-versions.sh:169-194` binds, with AC9 observing it — this unit
  changes the return contract the harnesses ship. The rationale is narrower than an earlier revision
  of this sentence claimed, and the difference matters. `check-kit-versions.sh` asserts internal
  CONSISTENCY only, so a behavioural change carrying NO bump at all leaves the constant, the README
  marker and both siblings' pairs equal, and the leg green. What it catches is a PARTIAL bump, which
  is what S9's own sentence says. The bump is owed by the contract change, not by the gate. `drift-audit selftest` is KEPT rather than
  removed, which is the one place this fold departs from the ratified decision set: the removal was
  derived for a diff confined to `tools/workflows/`, and S9 puts two files under
  `tools/drift-audit/` in scope, which arms that leg.

- rev-3 · 2026-08-26 · folded spec-audit round 2, the record at
  `memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round2.md`.
  Eight edits closing round-2 findings 3, 4, 6, 7, 12, 15, 20, 21, 28, 31, 32 and 36. Counted from
  that enumeration and not beside it: eight edits, twelve findings. 3 and 20 are one defect:
  rev-2 gave S4 two new exits and left S7, section 4 and AC8 each governing one, so S7 now enumerates
  FOUR exits per sibling and names the synthesis-death path among them. 12 widened AC2 to both
  siblings — it was scoped to `drift-audit-state.js` alone, which would have let `drift-audit-code.js`
  ship the configured count, the exact defect being ported against. 4 and 15 added AC8b: S8, the
  provenance-comment obligation section 10 rests the whole port on, was the only scope item no
  criterion observed. 7 and 36 corrected S10, which had FROZEN a dossier bullet that is itself wrong —
  the `args` defect is live in both siblings, not just one — so the refresh now widens it rather than
  preserving it. 21 widened AC10 from six clauses to the eight S10 enumerates. 6 corrected the
  finding-39 rationale: `check-kit-versions.sh` asserts internal CONSISTENCY, so a change with NO bump
  leaves it green, and only a PARTIAL bump reds. 28 named the second out-of-scope absence,
  `tier2-review.js:220-225`. 31's headline was a misreading and is recorded as such, but its
  underlying point stands and S5 now names `severityCorrections` and rules on a demoted `partial`.
  32 widened S9 beyond the marker byte: `tools/drift-audit/README.md` carries a migration paragraph
  per contract move as this kit's convention, and a bump skipping it leaves an adopter reading a note
  for the wrong version. AC9b observes it.

- rev-4 · 2026-08-26 · folded spec-audit round 3, the record at
  `memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round3.md`.
  Round 3 CONVERGED at zero blockers, the sequence being 3 then 2 then 0, so this is the last fold the
  count-bounded rule asks for. Seven edits here, closing round-3 findings 1, 2, 4, 5, 6, 9, 10, 14,
  15, 17, 22, 24, 26, 27 and 29. Stated from the enumeration rather than beside it: seven edits,
  fifteen findings, and the two numbers are counted from the list in this sentence.
  1, 9, 15, 22 and 29 are five lenses on one defect and it is a FOLD_WRONG of my own: rev-3 widened
  S7 to four exits and left section 4 Data model and AC8 each governing one, so six of the seven
  fields were unbound on the zero-configured branch. Both now name all three return blocks, and the
  Data model states what differs between the two early branches rather than calling them the same.
  The `severityCorrections` rider is answered in the same edit: it belongs to `drift-audit-code.js`
  alone, stays on the success return, and is named as deliberately outside S7's closed seven.
  2 and 10: S9's mandated migration text called the move additive while section 4 Migration of this
  same spec names `lensesRun` array-to-integer as BREAKING. S9 and AC9b now lead with the break.
  6 and 24: AC8b used `grep -c`, which prints one count per file and no positions, for a criterion
  about placement. It is `grep -n` now, matching spec-1's AC7 for the identical obligation.
  4 and 27: AC10 said eight clauses over a list of ten. 5, 14, 17 and 26: section 5 said three empty
  states while section 4 named a fourth, in a unit whose subject is exit-path accounting.

## 10. Reuse audit

The seam is `tools/workflows/tier2-review.js`, which already implements every guard this unit ports,
each one beside a comment naming the defect that earned it. This unit copies from that file rather
than inventing a predicate, and the copy is deliberate: the governance template instructs inlining in
this runtime because workflow scripts cannot import, so a shared helper is not available.

`tools/codebase-map/reuse_lookup.py` was run for the phrase naming a review harness that drives
lenses and skeptics over a subject. It returned `tier2-review.js`, `drift-audit-state.js` and
`drift-audit-code.js` together under the `workflow-scripts` inventory key, which is the population
this unit is about. All four keys under that inventory are claimed by
`memory/map/features/review-harnesses.md`, which is the dossier S10 refreshes.

Recall terms used with `tools/memory-recall/query.py`: `tier2-review harness lens skeptic verdict
spec-audit diff-review blockers convergence trust counters unverified fan-out`. That query returned
the aFoldedQuarry integer-join record, the aGuardedTally dead-lens record and the aBoundedVerdict
synthesis-death record. All three describe guards this unit ports, and all three confirm the guards
were earned by observed defects rather than designed in advance.
