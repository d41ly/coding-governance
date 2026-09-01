# TOOL-dFoldedVerdict-1 — the driver records which disposition a review exit took

**Status:** SPECCED · rev-1 · 2026-09-01 · node d · Tier-2 · base adc0543c · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`BUILD-METHOD.md` M4 admits two dispositions at a non-convergent review exit, FOLD and PROMOTE, and
the rendered Skill tells a run to record which it took with `--disposition fold|promote`
(`.claude/skills/unattended/SKILL.md:619`). The driver refuses that flag today: it is not in the
argument parser, so it falls through to refusal 14 at `tools/unattended/unattended.sh:4828`. This
unit builds the driver half — the flag parses, validates against a closed set, is required exactly
where an exit occurs, and is written onto the `review` round row `verb_review` already appends.

## 2. Scope (IN)

- **S1** — `--review` accepts `--disposition <value>`. A new `RV_DISPOSITION=""` initialiser joins
  `RV_SUBJECT=""; RV_BLOCKERS=""` at `unattended.sh:317`; a new `case` arm joins `--subject` and
  `--blockers` at `:4809-4810`; and the value is passed as `verb_review`'s FIFTH positional from the
  dispatch at `:4848`. `verb_review`'s signature comment at `:3903` and its `local` line at `:3904`
  both gain the parameter.
- **S2** — the value is validated against a CLOSED set held in a named constant
  `REVIEW_DISPOSITIONS="fold|promote"`, declared beside `REVIEW_VERDICTS` at `unattended.sh:466`. The
  refusal renders the constant rather than a retyped literal, exactly as the `--verdict` refusal at
  `:3910-3913` renders `REVIEW_VERDICTS`.
- **S2a** — the constant is spelled `REVIEW_DISPOSITIONS`, and the name is load-bearing rather than
  taste. `tools/memory-tree/marker-contract.test.sh:369` reads the verdict vocabulary with an
  anchored `sed` whose pattern begins `^REVIEW_VERDICTS="`, so a constant whose name started with
  that string would be picked up by contract 3 and compared against the hygiene engine's three
  verdict tokens. Verified at source; a name that merely reads well would have redded the
  `marker contracts` leg.
- **S3** — the STATE GATE. The flag is REQUIRED when `review_state` returns `NON-CONVERGENT` or
  `CEILING`, and REFUSED when it returns `CONVERGED` or `CONVERGING`. The trigger is the computed
  STATE and never `--verdict`, whose closed set at `:466` contains none of those four tokens. Both
  branches sit between `state=$(review_state "$prior" "$blockers")` at `:3955` and the `park` call at
  `:3964`, which is the only window where the state exists and nothing has been written yet.
- **S3a** — ORDERING of the two refusals, decided here rather than left to fall out of the edit. The
  closed-set check of S2 runs with the other argument validations, above `:3955`, because a value
  outside the set is malformed input whatever the state is; the state gate of S3 runs after `:3955`,
  because before that call there is nothing to key on. The consequence to test: `--disposition
  nonsense` on a CONVERGING round produces the CLOSED-SET refusal, not the state refusal, and AC3
  pins that one answer so an arm cannot pass against either.
- **S4** — WHERE THE FIELD SITS. It is appended to the free-text reason string `verb_review` composes
  at `:3964`, after the state token `note` adds at `:3956-3959`, producing
  `verdict <v> · blockers <n> · NON-CONVERGENT · disposition fold`. It is NOT a new `park()`
  parameter and NOT the existing fifth `step` slot, which is `--propose`'s declared field
  (`unattended.sh:4071`). Section 4 states why it cannot go after the reason.
- **S5** — the two SUCCESS lines at `:3968` and `:3969` name the recorded disposition. Both hard-code
  promotion today, in the sentence a run reads at the moment it exits, so without this item the
  driver would refuse a fold and then tell the run it had promoted.
- **S6** — the header invocation line at `unattended.sh:17` gains the flag. That line is the carrier
  `usage()` RENDERS from at `:108-116`, so it is the only place the argument shape has to be written.
- **S7** — a positive test arm in `tools/unattended/unattended.test.sh` for EACH new `fail` branch,
  quoting its message text verbatim up to the first interpolation. This is machine-required, not
  housekeeping: `tools/memory-tree/check-arms.py` reds at `:243-254` on any unarmed branch that is
  not pinned in `memory/project/unarmed-branches.txt`.
- **S8** — the two EXISTING driver-driven calls that now reach an exit without the flag are updated
  in the same commit, or the suite refuses them: `unattended.test.sh:4468` (subject `F1 (fork)`,
  blockers 2 after 2) and `:4475` (subject `S1`, blockers 2 after 2). Both compute `NON-CONVERGENT`
  today, and after S3 both are refusals.
- **S8a** — `:4475` records `--disposition promote`, deliberately. The arm at `:4477` asserts the
  literal `PROMOTED` in that call's stdout, and S5's promote sentence keeps the word, so the existing
  assertion keeps its meaning instead of being rewritten to match new output. A second arm covers the
  fold sentence. The row assertion at `:4478` greps a SUBSTRING ending `· NON-CONVERGENT`, so S4's
  placement AFTER the state token leaves it matching — verified by reading the pattern, and it is the
  reason the field goes after the token rather than before it.

## 3. Non-goals (OUT)

- **N1 — the checker.** `TOOL-dFoldedVerdict-2` owns clause 3 of check 2 in
  `tools/unattended/check-unattended.sh:246-317`: the second arm that reads the recorded disposition
  instead of the unit-id delta, the two messages at `:311` and `:313` that say a subject "exited
  without converging", the aggregate text at `:317` that says "exited without promoting", and the
  date cutoff the build README makes mandatory. Nothing in this unit edits that file.
- **N1a — a hazard handed to that unit, not a scope claim.** `memory/project/unarmed-branches.txt`
  pins three unarmed `check-unattended.sh` check-2 branches at ordinals 9, 10 and 11, and
  `check-arms.py` assigns ordinals by line order within a check. A new `fail 2` branch inserted above
  them shifts all three and reds `harness arms (fail branches armed or pinned)` with a message that
  reads like a rewording. This unit's own branches are `fail 37`, and no check-37 row is pinned.
- **N2 — retrofitting the field onto landed run-state files.** `TOOL-dFoldedVerdict-3` owns the
  labelled retrofit that clears the red on `origin/main`, and supersedes `TOOL-aClosedDocket-4`.
- **N3 — inferring the disposition.** A run that reaches an exit without recording one gets a
  refusal, never a guess. A driver-written fact exists because an authored claim is not evidence, and
  an inferred one is worse than authored.
- **N4 — the harness prose at `tools/workflows/unattended-build.js:245`.** It hands an agent a
  `--review` invocation with no disposition. That string is an INSTRUCTION, not an executed call —
  verified by reading the surrounding stage — so the cost of leaving it is one refusal that names
  both legal values and tells the agent what to add, rather than a silent stall. A follow-up, and it
  belongs to whichever unit next touches that harness.
- **N5 — a `marker-contract.test.sh` contract pairing `REVIEW_DISPOSITIONS` against M4's two words.**
  Contract 3 exists because a driver-written verdict token can be REFUSED by ANOTHER KIT's gate on an
  append-only record. That cross-kit edge does not exist for the disposition until unit 2's clause
  reads it, and M4's prose is not a machine reader of the field. Named as an available left-shift in
  section 5, not built here.
- **N6 — two pre-existing defects this unit neither creates nor closes.** `TOOL-dHonouredPark-8`:
  `--review` keys convergence on `--subject` alone, so a spec audit and a closing diff review collide
  when both name the build slug, and after S3 a colliding subject would be asked for a disposition
  belonging to the other loop. `TOOL-aProvenReuse-3`: a NON-CONVERGENT exit whose subject is a SPEC
  has no legal PROMOTE, which is the argument for FOLD and therefore for this unit, but closing it is
  an M4 change and not a driver change.
- **N7 — new readers.** `verb_status` counts review rows by KIND through `nnoted` at
  `unattended.sh:2782` and never parses the reason, and `BUILD-METHOD` M9 excludes `history`-class
  entries from the wrap-up. Neither reads the field, and this spec claims neither.

## 4. Design

### Data model

The row `park()` emits is, from its printf at `unattended.sh:3804`:

```
<ts> <kind> · item <item>[ · step <step>] · reason <reason>
```

`verb_review` calls it at `:3964` with a reason built as `verdict <verdict> · blockers <blockers>`
plus `note`, where `note` is ` · <STATE>` for the three terminal states and empty for `CONVERGING`.
The disposition is appended to that fourth argument, giving:

```
2026-09-01T00:00:00Z review · item S1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition fold
```

### Why it cannot go after the reason

`reason` is LINE-FINAL, and `park()`'s own header at `:3797-3801` records that two live readers
recover a field by matching UP TO it. Verified at source: `recorded_waivers` at `:1155-1161` takes the
handle with a `sed` whose pattern ends at ` · reason .*$`, and check 17 of
`check-unattended.sh:1116-1117` splits the same line into `wh` by trimming everything from the first
` · reason ` and `wr` by taking everything after it. A SIXTH positional appended after the reason
would change the emitted grammar for all nine parked kinds at once, and on a waiver row `wr` would
silently absorb it — the field would be written and read by nothing, which is the failure mode this
kit calls a row nothing counts. The fifth slot is not available either: `step` is `--propose`'s
declared field (`:4071`) and sits BETWEEN item and reason precisely so that it is not line-final. So
the disposition is not a `park()` parameter at all. It is text the caller composes into the reason it
already builds, which is the route the terminal state token took, for the same reason.

### The five readers of a review row, and why a trailing field is invisible to each

Every one was opened; none is a guess.

| Reader | Site | How it splits | Effect of a trailing field |
|---|---|---|---|
| `review_counts` | `unattended.sh:3889-3901` | first ` · reason `, then matches `blockers <n>` | none, the count is matched and not positional |
| `review_last_reason` | `unattended.sh:3875-3887` | same split, returns the whole tail | the tail grows, and no consumer parses past a glob |
| the terminal-round guard | `unattended.sh:3951` | strips through the last ` · reason `, then greps an unanchored alternation of the three states | none |
| the closing-review DoD term | `unattended.sh:3479-3486` | `review_last_reason`, then unanchored globs on the three states | none |
| clause 3 of check 2 | `check-unattended.sh:281-300` | first ` · reason `, then an unanchored match on the two exit states | none, and this is the reader unit 2 extends |

### Why the flag is required only at an exit

A `--disposition` on a CONVERGING or CONVERGED round is a field with no referent: nothing has been
disposed. Requiring it exactly when the state is terminal-without-convergence means the fact and the
condition it describes are created by the same call, and a row carrying it in any other state is a
refusal rather than a tolerated extra. This is `TOOL-aClosedDocket-4` S1 as ratified on 2026-08-31,
carried forward unchanged; that unit is superseded by `TOOL-dFoldedVerdict-3` and is cited here as
the source of the rule.

### Why CEILING requires one too

`CEILING` is an exit, and clause 3 sets its per-subject "needs a disposition" flag for
`NON-CONVERGENT` and `CEILING` alike (`check-unattended.sh:296`), so a CEILING exit that recorded
nothing leaves unit 2's reader with the same hole. M4 prescribes promotion at a ceiling, but a value
the driver forces is a constant rather than an observation, and a constant cannot be evidence for the
clause that reads it. Section 8 Q2 carries the one consequence: accepting `fold` there means the
driver permits an exception to a sentence the Skill and M4 both state.

### The refusal and success texts, spelled here because an arm must quote them

`check-arms.py` matches a branch to its arm on the message text up to the first interpolation, so
these are contract and not draft.

- closed set — `--review names a disposition outside the closed set, and a disposition nothing can
  compare is prose in a field; legal dispositions: ` then the constant.
- present off an exit — `--review carries a --disposition on a round that is not an exit, and a
  disposition with nothing disposed is a field with no referent; only NON-CONVERGENT and CEILING take
  one, and this round computed: ` then the state.
- absent at an exit — `--review reached an exit with no --disposition, and M4 admits two: fold, when
  every standing blocker was folded into a document the review already read, and promote, when one
  needs a mechanism this build lacks. Recording neither is indistinguishable from disposing of
  nothing; this round computed: ` then the state.

Each message's interpolation is its LAST field, so the signature `check-arms.py` pins is the whole
sentence rather than a fragment. The NON-CONVERGENT success line at `:3968` keeps its promote
sentence verbatim and gains a fold sentence beside it; the CEILING line at `:3969` replaces "The run
promotes and lands anyway" with the recorded disposition and keeps the rest.

### Files touched (estimate)

| Path | Items |
|---|---|
| `tools/unattended/unattended.sh` | S1, S2, S2a, S3, S3a, S4, S5, S6 |
| `tools/unattended/unattended.test.sh` | S7, S8, S8a |

### Alternatives rejected

- **A new `--fold` verb.** A verb owes carrier rows in three documents — check 26 at
  `check-unattended.sh:2005-2057` joins `VERBS_SLUG` and `VERBS_INLINE` against the driver's own
  header, the protocol's verb section and the Skill's invocations. A flag owes none of that, verified
  by reading that check: it iterates verb names only, and no gate in this kit joins a FLAG set
  against any carrier. So the cheap surface is the flag, and the expensive one would be a second verb
  for a fact the first already has.
- **Reusing `--verdict`'s vocabulary.** `REVIEW_VERDICTS` describes what the ROUND found; a
  disposition describes what the RUN did about the exit. One enum answering two questions is the
  shape this kit refuses by name. Carried from `TOOL-aClosedDocket-4` Q2.
- **Writing the disposition through `park()`'s `step` slot.** It is `--propose`'s declared field with
  its own reader, and overloading it would give one slot two meanings across nine kinds.

### Rollout

This unit lands alone and is inert until `TOOL-dFoldedVerdict-2` reads the field: a recorded
disposition that nothing reads costs one token on a row. The reverse order is the dangerous one — a
checker that demands a field no verb can write reds every exit.

## 5. Production-readiness checklist

- **Security** — N/A. One flag on a local verb, whose value is validated against a closed set before
  it reaches the record; the subject guards at `:3944-3950` already cover the free-text field.
- **Perf / scale** — N/A. One string comparison and one appended token per `--review` call.
- **a11y** — N/A. A shell driver with no user interface.
- **i18n** — N/A. Kit-internal English, as with every other refusal in this driver.
- **Error / empty / loading states** — three refusals, from S2 and S3, each naming what is legal. An
  empty `--disposition ""` is indistinguishable from an absent flag and is handled by the
  absent-at-exit refusal, which is the correct outcome and is stated so no reader has to derive it.
- **Observability** — the round row carries the field, and unit 2's clause is its reader. Nothing
  else reads it; N7 names the two readers claimed for this field elsewhere that do not read.
- **Risks** — the live one is S8: two existing driver-driven calls in the suite reach an exit and
  would be refused. They are named by line, and the suite may not be run here (section 7), so AC7
  witnesses them by direct invocation instead of by the suite.
- **Testing + left-shift gates** — S7's arms, and `harness arms (fail branches armed or pinned)` is
  the machine that demands them. Available left-shift not taken: N5's marker contract.
- **Migration / rollback** — no state moves. Landed run-state files are untouched (N2), and a revert
  is a revert.
- **User docs** — none owed. `tools/unattended/SKILL.template.md:619` already documents the flag and
  its two values, which is the defect this unit closes rather than a document it must write.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --review <slug> --subject S1 --verdict BLOCKED
  --blockers 2 --disposition fold` is run on a fixture whose prior round recorded 2 blockers, the
  run-state file gains a row ending `· NON-CONVERGENT · disposition fold`, observed by reading
  `memory/builds/<slug>/RUN.md` and not by reading the source.
- **AC2** — When the same call passes `--disposition nonsense`, it is REFUSED and the message names
  the legal set rendered from `REVIEW_DISPOSITIONS`, observed in the stdout of
  `bash tools/unattended/unattended.sh --review`.
- **AC3** — When `--disposition nonsense` is passed on a round whose computed state is `CONVERGING`,
  the refusal emitted is the CLOSED-SET one and not the state one, observed in that same stdout. This
  pins S3a's ordering; without it an arm passes against either refusal and the ordering is untested.
- **AC4** — When a first round for a fresh subject is recorded with `--disposition fold`, it is
  REFUSED naming `NON-CONVERGENT` and `CEILING` as the states that take one, because `review_state`
  returns `CONVERGING` there. Observed by running `bash tools/unattended/unattended.sh --review` on a
  subject with no prior row.
- **AC5** — When a round reaches `NON-CONVERGENT` with no `--disposition`, it is REFUSED and the
  message names both `fold` and `promote`, observed in the stdout of
  `bash tools/unattended/unattended.sh --review`.
- **AC6** — When any of AC2 through AC5 is refused, the run-state file is byte-identical to what it
  was before the call, observed with `git diff --stat` over the fixture's `RUN.md`. This is what
  proves the refusals sit above the `park` call at `unattended.sh:3964`.
- **AC7** — When the fixture drives the two sequences the suite drives at
  `tools/unattended/unattended.test.sh:4468` and `:4475`, each with a `--disposition` added, both
  succeed and the stdout of the second still contains `PROMOTED`. Witnessed by DIRECT invocation of
  `bash tools/unattended/unattended.sh --review` on a scratch fixture, NOT by running
  `tools/unattended/unattended.test.sh` — a standing owner instruction forbids running the unattended
  kit self-tests, and this criterion says so rather than depending on a suite it may not run.
- **AC8** — When `python tools/memory-tree/check-arms.py --check` is run, it exits 0. Each new `fail
  37` branch has a positive assertion in `tools/unattended/unattended.test.sh` naming its own failure
  text, and an unarmed branch that is not pinned in `memory/project/unarmed-branches.txt` reds this
  static scan. It is a scan and not the self-test suite, so it may be run here.
- **AC9** — When `python tools/memory-tree/check-arms.py --report` is read, the
  `tools/unattended/unattended.sh` row shows its branch and armed counts BOTH risen by the number of
  branches added. The floors of `104:101` in `ARMS_FLOORS` are one-sided upward and sit far below the
  measured `190:184`, so no floor moves and no floor edit is owed — stated because the ratified
  `TOOL-aClosedDocket-4` AC9 asserted the opposite in both directions and it is false against
  `tools/memory-tree/check-arms.py:283-291`.
- **AC10** — When `bash tools/unattended/check-unattended.sh` is run over the tree, it exits with the
  status it had at BASE `adc0543c`. The clause it grades is unit 2's, so this criterion asserts that
  the driver change moved nothing on the leg, not that the leg turned green.
- **AC11** — When `bash tools/memory-tree/marker-contract.test.sh` is run, it exits 0, proving S2a:
  the new constant did not enter contract 3's anchored `REVIEW_VERDICTS` read.
- **AC12** — When the driver's usage text is emitted, its `--review` line carries `--disposition`.
  Observed by running `bash tools/unattended/unattended.sh` with no verb, which renders the usage
  from the header at `unattended.sh:108-116`, and that render is S6's only observable.

## 7. Gates

Named from `tools/gate-legs.json`, read at authoring time.

- `unattended kit gate` — unguarded, reaches this unit, and AC10 is its criterion.
- `unattended skill wiring` — unguarded; it diffs the rendered Skill against a fresh render of
  `SKILL.template.md`. This unit edits neither, so it must stay green untouched.
- `harness arms (fail branches armed or pinned)` — unguarded, and the leg that makes S7 mandatory.
- `marker contracts` — unguarded, and the leg S2a exists to keep green.
- `kit version markers` — unguarded. It asserts that the `unattended` version carriers AGREE, never
  that they move; section 8 Q3 carries whether they move on this unit.
- `memory hygiene` — unguarded, and the leg this spec file itself answers to.
- `lexicon naming predicates` — its guard names `tools/`, so it runs. It grades nothing here: `sh` is
  declared DARK in `.lexicon.conf`, so no shell identifier this unit adds is read by it. Written down
  because a green row on a leg that cannot see the change is not coverage.

What no gate here checks: whether the disposition a run recorded is the CORRECT one for its blockers.
No predicate reads intent. Clause 3, once unit 2 lands, grades that a disposition WAS recorded.

## 8. Open questions

- **Q1 — FACT-QUESTION · does a new trailing field on the reason survive every reader of the review
  row?** RESOLVED (agent, 2026-09-01). The probe is reading every reader at source, and the
  observation that decides it is where each one splits the line; the section 4 table records all
  five, with file and line. All five split at the FIRST ` · reason ` or match unanchored, so a token
  appended inside the reason tail is invisible to each. LIVENESS: the probe can produce a negative — a
  reader splitting on the LAST separator, or anchoring its state match to end-of-line, would have made
  S4 unbuildable as written, and `unattended.sh:3951` does strip through the LAST ` · reason `, which
  is exactly the shape that would have failed had the reason itself ever contained the separator.
- **Q2 — at `CEILING`, does the driver accept `fold`, or force `promote`?** Options: (a) accept
  either, as section 4 argues, so the field is an observation rather than a constant; (b) refuse
  `fold`, matching `tools/unattended/SKILL.template.md:623` and M4, which both say the run promotes
  and lands anyway at a ceiling. Recommendation: (a). A forced value is not evidence for the clause
  that reads it, and a ceiling is a predicate defect rather than a statement about what the run
  actually did with its blockers. The cost of (a) is honest and is stated: the driver then permits an
  exception to a sentence two documents make, and closing that is a document edit for a later unit.
- **Q3 — does `KIT_UNATTENDED_VERSION` move on this unit, or once for the build?** Six units of this
  build touch the kit, and the version has nine carriers — the constant plus a same-line marker in
  `unattended.sh`, `check-unattended.sh` and `check-pass-order.sh`, all three
  `tools/unattended/*.template.md` files, and their three renders. Verified against
  `tools/check-kit-versions.sh:144-172`, which asserts they AGREE and never that they move; the
  `verdict epoch (kit version dates the engine)` leg is hardcoded to the memory-tree engine, so no
  gate forces a bump here. Recommendation: once, on the build's last landing unit, so six units do
  not collide on nine files. Noted because `TOOL-aClosedDocket-4` S6 put the bump inside this unit
  and named only eight of the nine carriers, omitting `check-pass-order.sh`.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft. Takes `TOOL-aClosedDocket-4`'s ratified scope for the DRIVER
  half only; that unit is superseded by `TOOL-dFoldedVerdict-3` and its gate half is
  `TOOL-dFoldedVerdict-2`. Three of its claims were re-verified at source and did not hold at this
  tree: its S6 named two shell version carriers where there are three, its AC9 asserted an
  `ARMS_FLOORS` raise that is not owed and a red that does not occur, and neither it nor its round-1
  audit named the two existing test call sites (S8) that the required-at-exit rule turns into
  refusals. Added S2a, S3a, S8a, the five-reader table and Q3, none of which appear in `-4`.

## 10. Reuse audit

Three seams, all extended in place, none new. `verb_review` at `tools/unattended/unattended.sh:3903`
already computes the state and writes the round row, so S1 and S4 add a field to a line that exists.
Its `--verdict` refusal against the closed `REVIEW_VERDICTS` set at `:3910-3913` is the shape S2
copies. `park()` at `:3796` is the row writer, and section 4 records why the new field goes into the
reason its caller composes rather than into a new parameter of it.

The map probe run for this unit was `python tools/codebase-map/reuse_lookup.py` with the phrase
"recording the disposition a review round took onto the round row a driver already writes". It
returned `write` and `write_text` in `tools/memory-tree/` as its top-ranked seams, plus `records` in
`gotchas.py`. All three were opened and REJECTED: they write the memory tree's generated artifacts and
none of them touches a run-state record. The one hit pointing at the right place is the
affordance-seam row for the `unattended` kit, which names `.unattended.conf` rather than the function;
the seam itself was located by reading `unattended.sh`, and the map's `unattended` dossier does not
carry `verb_review` at the granularity this unit needed.

Recall terms used: `unattended driver review round park row reason line-final closed-set refusal
disposition fold promote non-convergent ceiling subject`. It returned `TOOL-dMispairedQuote-7` and
`TOOL-dBriefedPass-9`, the two backlog rows that measured this defect live; `TOOL-aProvenReuse-3`, on
why a spec-subject exit has no legal PROMOTE, which is the argument for FOLD; `TOOL-dHonouredPark-8`,
the subject collision N6 names; and `TOOL-dCarriedReceipt-1`, on prior rounds not being recoverable
across runs, which is why the row and not a recollection is the record.

Where a hit was STALE: `TOOL-aClosedDocket-4` cites `unattended.sh:444`, `:3500`, `:3533-3535`,
`:3578` and `:3591-3592` for the verdict set, `review_state` and the success lines. None of those line
numbers holds at BASE `adc0543c`; the same code is at `:466`, `:3859`, `:3910-3913`, `:3955` and
`:3968-3969`. Every citation in this spec was re-read at this tree.
