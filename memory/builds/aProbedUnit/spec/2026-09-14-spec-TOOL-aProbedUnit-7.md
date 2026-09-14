# TOOL-aProbedUnit-7 — disposal by severity, on any confirmed finding

**Status:** SPECCED · rev-3 · 2026-09-14 · node a · Tier-2 · base 1b000d1a · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md) | journal | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 |
| [2026-09-14-prompt-TOOL-aProbedUnit-7-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-7-1-build-brief.md) | journal | — |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round2.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round2.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 |

<!-- /gen:spec-records -->

## 1. Goal

The DISPOSAL stage of `tools/workflows/unattended-build.template.js` runs whenever the audit round
CONFIRMED a finding, on a `CONVERGED` verdict too, and disposes by SEVERITY: a blocker or high is
PROMOTED to a unit, a medium or low is FOLDED into its spec. Today the stage runs only on a
non-`CONVERGED` verdict and disposes by NATURE, so a round that converges with eight highs, six
mediums and one low — the recorded shape at
`memory/builds/aCollapsedScan/reviews/2026-08-26-review-TOOL-aCollapsedScan-4-spec-audit-round1.md`
— disposes nothing, and the roster is handed out over fifteen confirmed findings. The owner's rule
is the build README's build-level rules, 2026-09-14: PROMOTE keeps M4's meaning, a blocker or high
becomes a UNIT.

## 2. Scope (IN)

- **S1** — The stage's predicate moves from the verdict to the confirmed count. In
  `tools/workflows/unattended-build.template.js` the `verdict === 'CONVERGED'` skip at line 725
  becomes a `confirmed === 0` skip, announced with the count and the round; a positive count runs
  the stage on every verdict and announces `disposing by severity`, with `on CONVERGED too` when
  that is the verdict. Observed by AC1 and AC2.
- **S2** — The counts the stage decides on are READ, not assumed. Beside the blocker refusal at
  lines 587-593 a second refusal names `confirmed` and `highs`: each must be an integer and
  `blockers + highs` may not exceed `confirmed`, because `tier2-review.js` returns `confirmed` as
  the size of the skeptic-confirmed set and `blockers`/`highs` as the synthesis pass's counts within
  it. A degraded value is a refusal, never a zero. Observed by AC3.
- **S3** — The stage prompt disposes by severity and is mode-aware. It names the report, the three
  counts and the rule; PROMOTE routes through `--rescope --act add` in unattended mode and through
  a build README roster row in attended mode, where that verb `fail 48`s; FOLD is a rev-N bump with
  its section 9 line; nothing is parked, waived, retired or re-reviewed; the agent returns
  `promoted` and `folded` as counts of FINDINGS by report id and names promoted unit ids in
  `summary`. Observed by AC1 and AC4.
- **S4** — `DISPOSAL_SCHEMA` at lines 320-329 requires `promoted` and `folded` integers, and the
  guard at line 752 refuses a return whose `promoted + folded + standing.length` is not
  `confirmed`, with the same empty roster and a note naming the mismatch. Every non-throwing exit
  past the stage carries `promoted` and `folded` beside `standing`, the attended every-unit-terminal
  return included. Observed by AC1, AC4 and AC5.
- **S5** — The file's own header stops saying the disposal clause is unreachable in attended mode
  (lines 55-58), the two comment blocks that restate the verdict predicate (lines 613-615 and
  704-719) say the confirmed-count one, and the exported `meta.phases[2].detail` at line 9, which
  every `meta`-scanning reader sees, says the stage disposes every confirmed finding by severity
  rather than `every blocker still standing`. The render `tools/workflows/unattended-build.js` is
  re-made by `bash tools/workflows/check-protocol-parity.test.sh --render` in the same commit.
  Observed by AC6.
- **S6** — M4 of `tools/memory-tree/BUILD-METHOD.template.md`, two sentences: the disposal
  sentence at line 140 becomes the severity rule, and the late-blocker sentence at line 143, which
  says a blocker confirmed after `CONVERGED` "takes the exit's own disposition, FOLD or PROMOTE",
  says it takes the severity rule's disposition, because under this rule a `CONVERGED` exit records
  no disposition and a blocker is never folded, so "the exit's own" has no referent. Both are sized
  in section 4 against M1's byte cap; the render `memory/guides/BUILD-METHOD.md` is re-made by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` and the kickoff manifest `last-audit`
  is re-stamped in the same commit, because that render is on its watch line. Observed by AC7.
- **S7** — The unattended kit's prose carriers say the rule once each and point rather than
  paraphrase: the `CONVERGED` and `NON-CONVERGENT` bullets of `tools/unattended/SKILL.template.md`
  and the `--review` bullet of `tools/unattended/VERBS.template.md`, re-rendered by
  `bash tools/unattended/adopt-unattended.sh`; and the driver's own by-nature disposal prose,
  four places: the `fail 37` for a round on an ended subject at
  `tools/unattended/unattended.sh:4096`, whose `fold or promote` clause becomes the severity
  rule's; `review_exit_note`'s two sentences at `:4025` to `:4026`, which open `every blocker
  still standing was FOLDED` and `every blocker still standing is PROMOTED` and print on every
  terminal echo, the `BOUNDED` one unit 6 adds included, so each names the severity rule's half
  it records instead; and the requires-disposition `fail 37` at `:4107`, whose `because the
  method admits BOTH fold and promote at the exit` clause and its `M4 admits BOTH` comment at
  `:4101` to `:4103` say the severity rule decides which value the exit records. The four suite
  arms that quote those messages move to the new words. Observed by AC8 and AC9.
- **S8** — `tools/workflows/unattended-build.test.sh`: the fixtures carry the callee's real keys
  (`confirmed`, `highs`), the default disposal double reconciles with the count it is paired with,
  the two arms quoting `blockers were not disposed` and the header arm at line 376 move to the new
  text, and the arms section 4 lists observe S1-S5. Observed by AC1 through AC6 for the arms,
  and by AC10 for the suite's own text and its whole run.

## 3. Non-goals (OUT)

- **The `--review` row grammar and its `disposition` field do not move.** `verb_review` at
  `tools/unattended/unattended.sh:4104-4115` refuses `--disposition` on a `CONVERGED` round and
  check 2 of `tools/unattended/check-unattended.sh` reads the field only on a `NON-CONVERGENT` or
  `CEILING` exit (lines 512-517). A `CONVERGED` round that this unit disposes therefore leaves no
  disposition in the run-state file; section 5 states the cost. Whether the driver should accept one
  there is `TOOL-aProbedUnit-6`'s seam and is left as an edge. At every OTHER terminal exit the
  field stays REQUIRED, by the 2026-09-01 ruling spec 6 section 8 F1 cites, and the harness
  recorder as unit 6 leaves it retries a refused terminal exit with `--disposition promote`; so
  `CONVERGED` is the one exit this stage disposes with nothing in the record, and the only one.
  The driver edits here are WORDS only — the two `fail 37` messages at
  `tools/unattended/unattended.sh:4096` and `:4107`, the comment above the second, and
  `review_exit_note`'s two sentences at `:4025` to `:4026` — never a grammar, a branch count, a
  trigger or a case: the `BOUNDED` member of the state gate is unit 6's and is read as it leaves
  it.
- **No convergence rule moves.** `review_state`, the round bound and the `BOUNDED` exit are
  `TOOL-aProbedUnit-6`; the sentence in M4 that states them is that unit's, and this unit edits
  the disposal sentence beside it and the late-blocker sentence three lines down, both of which
  state disposal and neither of which states convergence.
- **The promoted unit's audit is not run by this stage.** A sidechain agent holds no `Workflow`
  tool, so the disposal agent cannot audit the spec it authors. The existing rule stands: a promoted
  unit is audited as a SPEC, its own `--subject <id>` loop, by the caller before dispatch, and
  `specs-reviewed` at `--close` is what refuses one that was not.
- **No backlog row is edited in the pass.** `memory/backlog` is a `SHARED_RECORDS` member at
  `.unattended.conf:206`, and `--dispatch` at `tools/unattended/unattended.sh:4773-4777` refuses a
  declaration overlapping one. The brief assigns `TOOL-aProvenReuse-3`'s status flip to this unit;
  it is rerouted to the closing pass below, with the residual the brief names.
- **No kit version moves.** The build-level rules assign every bump to the closing pass.
- **The hand-out carries counts, not ids.** Promoted unit ids live in the `rescope · add` rows the
  driver writes and in the agent's `summary`; section 8 F1 records the choice.
- **No codebase-map key moves.** The unit mints no workflow script, leg, hook or skill; the
  `review-harnesses` dossier names the harness and no predicate, so its prose does not rot.

### Edges

No sibling edge. This unit shares files with the round-bound unit ahead of it — M4's paragraph,
the Skill's review-state list, the VERBS `--review` bullet, the harness template, and the driver
line whose grep unit 6 widens and whose words this unit rewrites — and reads each as that unit
leaves it, but none of its criteria rests on anything that unit builds: every edit here lands the
same with or without it. That is SEQUENCE, which the `order` verb already declares, and the
Rollout sub-head states the overlap.

- **consumes-from** external — the return contract of `tools/workflows/tier2-review.js`: `confirmed`
  is an integer on the synthesis path (line 610) and `[]` on the three paths that also yield
  `blockers: null` (lines 375, 385, 478), and `highs` is the synthesis pass's adjudicated count
  (line 631). S2's refusal is written against exactly that; a callee that started returning a count
  on a degraded path would need S2 re-read.
- **hands-off** external — the status flip of backlog row `TOOL-aProvenReuse-3` at
  `memory/backlog/TOOL.md:338` to CLOSED, owed by the closing pass, which is not a dispatched pass
  and may open the shared records. Residual to write into the row: a promoted spec defect's unit is
  the mechanism that closes it, so M2's one-mechanism rule is satisfied by construction and the
  regress the row feared is bounded by unit 6's round bound.
- **hands-off** external — a `--disposition` on a `CONVERGED` exit, if the record ever needs one,
  is a driver and check-2 change on the round-bound unit's seam, `verb_review`'s state gate and
  check 2's awk; nothing here demands it.
- **hands-off** external — the direct run of `bash tools/workflows/unattended-build.test.sh` at the
  close, whole, once: the suite is on no bar and no `tools/gate-legs.json` row names it, so nothing
  at `--close` or the push boundary runs it. AC10's suite half is the criterion that owns that
  run, ledgered `observed at --close`; section 7 states the cost.
- **hands-off** external — whether the workflows kit's own version moves for this edit. Its
  `version_from` is `tier2-review.js` (`tools/workflows/kit.toml:6`), which this unit does not
  touch, and the harness's `unattended-build@1.0` marker on line 3 is paired by no leg. The
  build-level rules list three kits to bump and this one is not among them; the closing pass decides.

## 4. Design

### The predicate, and why it is the count

`tier2-review.js` returns four integers the harness can decide on: `confirmed`, the size of the set
the skeptics confirmed at any severity; `blockers` and `highs`, the synthesis pass's counts within
it (`tools/workflows/tier2-review.js:571-574`, required by the schema at 583-588); and `refuted`.
The verdict token comes from the driver and is a property of the blocker SEQUENCE. `CONVERGED`
means zero blockers this round and says nothing about highs, mediums or lows — so a predicate on
the verdict is a predicate on the wrong integer, and the stage skipped exactly the rounds the owner's
rule is about. Read at `tools/workflows/unattended-build.template.js:725`, the skip is
`if (verdict === 'CONVERGED')`. It becomes:

```js
let stood = [], promoted = 0, folded = 0
if (au.confirmed === 0) {
  log('disposal: skipped — round ' + roundNo + ' confirmed no finding, so nothing stands to dispose')
} else {
  log('disposal: ' + au.confirmed + ' confirmed finding(s) stand at a ' + verdict + ' exit · blockers ' +
    au.blockers + ' · highs ' + au.highs + ' — disposing by severity' +
    (verdict === 'CONVERGED' ? ', on CONVERGED too' : ''))
  const d = await agent(GROUND + <the prompt below>, { label: 'dispose:' + slug, phase: 'Disposal', schema: DISPOSAL_SCHEMA })
  …
}
```

`au` at line 655 gains `confirmed: auRaw.confirmed, highs: auRaw.highs`. The skip line keeps its
`disposal: skipped` prefix, which the AC4 arm at `tools/workflows/unattended-build.test.sh:462`
greps; its reason text changes because the reason did.

### The refusal, beside the one that exists

`confirmed` is an integer only on the synthesis path (`tier2-review.js:610`). On the three early
returns it is `[]`, and each of those also yields `blockers: null`, which the refusal at lines
587-593 already catches first. So on every path that reaches the stage today the count IS an
integer, and the refusal below is written for the callee that changes, not the one that exists —
because `undefined > 0` is `false`, and a `confirmed` key that quietly went missing would skip the
stage on every round, which is the false-clean shape this file refuses three times by name. Placed
directly after the blocker refusal, before `lastReport`:

```js
if (!Number.isInteger(auRaw.confirmed) || !Number.isInteger(auRaw.highs) ||
    auRaw.blockers + auRaw.highs > auRaw.confirmed) {
  throw new Error(
    'unattended-build: the AUDIT sub-workflow returned confirmed ' + JSON.stringify(auRaw.confirmed) +
      ', blockers ' + auRaw.blockers + ', highs ' + JSON.stringify(auRaw.highs) + ' at round ' +
      roundNo + '. `blockers` and `highs` count CONFIRMED findings, so each is an integer and their ' +
      'sum is at most `confirmed`; a count that cannot be read is a DEGRADED run and is never ' +
      'rounded to zero.',
  )
}
```

One refusal, one message, one arm, because the three conditions have one remedy: the callee's
return cannot be read as the contract it declares. It fires in BOTH modes, ahead of the
`CONVERGING` return at line 674, so the attended fixture at `unattended-build.test.sh:280` with
two blockers and no `confirmed` key would throw here — which is why S8 gives every fixture the
callee's real keys rather than exempting the attended path.

### The prompt

Mode-aware in one clause, on the same `attended ?` the file already uses for `GROUND`:

```
BEFORE ANY UNIT IS DISPATCHED, DISPOSE of every CONFIRMED finding in `<lastReport>` — the audit
exited <verdict> with <confirmed> confirmed, <blockers> at BLOCKER and <highs> at HIGH. Open the
report and take each confirmed finding at the severity the report gives it. BUILD-METHOD M4 disposes
BY SEVERITY and admits no third route. PROMOTE every BLOCKER and every HIGH:
  [unattended] run `<DRIVER> --rescope <slug> --act add --item <id> --reason <text>`, the reason
               being the report id and severity of the finding it closes,
  [attended]   add its row to the build README's authored Units table, because the recording verbs
               are unavailable with no run-state file,
then author its spec at its tier with a mechanism that CLOSES the finding — the change to the design
and the artifact that proves it — so it is audited once as a spec and built like any other. FOLD
every MEDIUM and every LOW into the spec it belongs to, as a rev-N bump with its section 9 line.
Never parked, never waived, never retired, never re-reviewed. Return `promoted` and `folded` as
counts of FINDINGS by report id, each id counted exactly once across the two and `standing`; name
every promoted unit id in `summary`; and NAME in `standing` every finding you did NOT dispose.
```

The old prompt reported `au.blockers` as "confirmed", which was the wrong integer under the same
name; the new one reports all three under their own. The old prompt also spelled the promotion
command without `--reason`, which `verb_rescope` refuses with `fail 48` and the driver's own
header at `tools/unattended/unattended.sh:14` lists as required, so the disposal agent's first
promotion as spelled was refused; the flag is spelled now, and V1 asserts the longer substring.
The attended clause exists because
`--rescope` `fail 48`s without a run-state file, which the file's own comments at lines 909-916
record as the mode-blind defect one layer down, and until this unit the stage was unreachable in
that mode so the contradiction was never live.

### The schema and the reconciling guard

```js
const DISPOSAL_SCHEMA = {
  type: 'object',
  required: ['disposed', 'standing', 'promoted', 'folded', 'summary'],
  additionalProperties: true,
  properties: {
    disposed: { type: 'boolean' },
    standing: { type: 'array', items: { type: 'string' } },
    promoted: { type: 'integer' },
    folded: { type: 'integer' },
    summary: { type: 'string' },
  },
}
```

The guard at line 752 gains the reconciliation. Every confirmed finding is promoted, folded or
named standing, and the prompt says so; a return whose three numbers do not add to `confirmed` is
self-contradictory in the way `{disposed: true, standing: ['b1']}` was, which the comment at lines
744-750 records clearing the old guard and handing out the full roster. The refusal keeps the
existing shape, empty roster and a note, and the reason is chosen in the order the existing arms
read it:

```js
stood = Array.isArray(d && d.standing) ? d.standing : []
const counted = Number.isInteger(d && d.promoted) && Number.isInteger(d && d.folded)
promoted = counted ? d.promoted : null
folded = counted ? d.folded : null
if (!d || d.disposed !== true || stood.length || !counted ||
    d.promoted + d.folded + stood.length !== au.confirmed) {
  const why = !d ? 'the disposal stage returned nothing at all'
    : stood.length ? stood.join(', ')
    : !counted ? 'the stage returned no integer promoted/folded counts'
    : d.disposed !== true ? 'the stage answered disposed:false with nothing standing'
    : 'the counts do not reconcile — promoted ' + d.promoted + ' + folded ' + d.folded +
      ' + standing ' + stood.length + ' is not confirmed ' + au.confirmed
  log('disposal: NOT done — ' + why)
  return { …, standing: stood, promoted: promoted, folded: folded,
    note: 'DEGRADED — findings were not disposed: ' + why + '. No roster is handed out: a roster ' +
      'minus the units a finding touches is a judgement this runtime cannot make.' }
}
log('disposal: done — promoted ' + promoted + ' · folded ' + folded + ' — ' + (typeof d.summary === 'string' ? d.summary : ''))
```

`null` on the degraded return where the stage returned no integer, the same rule the audit adapter
states at lines 625-629: an absent count is a stated absence, never a zero. On the skip path both
are honest zeros. The note's noun moves from `blockers` to `findings` because a standing high is
now the ordinary case; the two arms quoting the old noun move with it.

### The hand-out

`promoted` and `folded` join `standing` on the three returns past the stage — the DEGRADED one
above, the attended every-unit-terminal return at line 851 and the main return at line 883 —
under the rule the file states at lines 895-899: an empty list said out loud is a different fact
from a missing key. The `CONVERGING` return at line 676 precedes the stage and carries none of the
three, as today. The `note` at lines 925-933 is unchanged: a `CONVERGED` exit that disposed is not
degraded, and a `NON-CONVERGENT` one still is.

### The comments that describe a shape the file no longer has

Four blocks restate the verdict predicate and would describe a stage that no longer exists, which
is the drift class the file names at lines 100-101 about itself. The first is not a comment: it
is the exported `meta`, the one description every reader that scans workflow metadata sees
without opening the body.

| Lines | Today | After |
|---|---|---|
| 9 | `meta.phases[2].detail`: `dispose every blocker still standing over the whole spec set, then hand out the roster` | `dispose every confirmed finding by severity over the whole spec set, then hand out the roster` |
| 55-58 | `M4's BLOCKER-DISPOSAL CLAUSE IS UNREACHABLE HERE` — attended mode reaches the hand-out only at zero blockers, the `CONVERGED` one | the clause is `REACHABLE HERE SINCE TOOL-aProbedUnit-7`: the stage runs on the confirmed count, so attended mode reaches it at zero blockers with highs, mediums or lows standing; what it loses there is the `--rescope` row, a promotion being a README roster row and a spec with no amendment record |
| 613-615 | `so a run needing M4's blocker disposal cannot get one here` | a run needing M4's disposal reaches it through the confirmed count and not through the verdict |
| 704-719 | the stage runs on `NON-CONVERGENT` and `CEILING`, the two states that guarantee standing blockers; `ON CONVERGED THE STAGE ANNOUNCES ITS SKIP` | the stage runs on any confirmed finding and disposes by severity; on a confirmed count of zero it announces the skip |

With line 9 and the prompt at line 730 both moved, `blocker still standing` prints zero times in
the template and the render, which is the retired-phrase grep AC6 carries: a phrase retired once
should not be findable in any carrier.

The header arm at `unattended-build.test.sh:376` greps `UNREACHABLE HERE` and re-points to
`REACHABLE HERE SINCE`; a header left saying the old thing would keep that arm green and the file
lying, which is the pair S5 exists to prevent.

### The method carrier, and its bytes

`tools/memory-tree/BUILD-METHOD.template.md` is the source and `memory/guides/BUILD-METHOD.md` the
render, diffed by the `kit/dogfood doc parity` leg whose printed fix `--render` OVERWRITES the
render; `TOOL-aRatifiedRulings-1` §4 records observing that on a render-only edit. Edit the
template, render, commit both. Measured on 2026-09-14 at base `1b000d1a` with `stat -c%s` and
`wc -l`: template 26768 bytes, render 26743 bytes, 340 lines each; M1's cap is 27648 bytes and 350
lines, the byte half binding, and the recorded high-water in `tools/template-size-highwater.txt`
is 26941. The disposal sentence at line 140, PINNED at 228 bytes:

```
**At the exit every blocker still standing is DISPOSED**: FOLD a defect in a document the review read, PROMOTE one needing a mechanism this build lacks and audit it as a SPEC; never parked, waived or re-reviewed. Both terminate.
```

becomes, at 303 bytes:

```
**At the exit every CONFIRMED finding is DISPOSED BY SEVERITY, on CONVERGED too**: a BLOCKER or HIGH is PROMOTED to a unit whose mechanism closes it, audited as a SPEC; a MEDIUM or LOW is FOLDED into its spec as a rev-N bump with a §9 line; never parked, waived, retired or re-reviewed. Both terminate.
```

Plus 75 bytes, no line moves: the paragraph is one wrapped line in both files and the sentence
sits inside it. The sentence carries no decision id and no path, for the reason
`TOOL-aRatifiedRulings-1` §4 gives: the template ships to adopters where an id names nothing.
`retired` joins the never-list because the Skill's bullet already carries it and the method did
not, which was two answers.

The second carrier is three lines down, at line 143, inside the sentence `TOOL-aLeakedHandle-6`
landed on 2026-09-13 for a blocker confirmed after `CONVERGED`. Its clause, PINNED at 74 bytes:

```
takes the exit's own disposition, FOLD or PROMOTE, and never another round
```

becomes, at 61 bytes:

```
takes the severity rule's disposition and never another round
```

Minus 13, no line moves. Under the severity rule "the exit's own disposition" has no referent: a
`CONVERGED` exit records none, and a blocker is never folded. The rest of that sentence — never
another round, `--review` refuses and names the route — is the ruling's and stands; this unit
narrows what the disposition IS, not when it happens, and section 10 names the ruling.

Net plus 62 bytes for the file. Measured on 2026-09-14 by staging the line-140 swap into a copy
of both files: template 26843, render 26818, 340 lines each; the line-143 swap is 13 bytes on
the same wrapped-line shape and is computed rather than re-staged, so template 26830, render
26805, 843 bytes under the cap and 136 under the high-water — PINNED at base `1b000d1a`, and AC7
derives the live figures, because units 1 and 6 edit the same file ahead of this one and their
deltas are theirs to state.

### The Skill and VERBS

`tools/unattended/SKILL.template.md`, the state list at lines 630-647 as unit 6 leaves it. The
`CONVERGED` bullet gains one clause, spelled so its own words are greppable: the loop is done for
that subject, and its confirmed highs, mediums and lows are `still disposed` by the severity rule
the next bullet states — `still disposed` is a phrase the file does not carry at base and AC8
counts it. The `NON-CONVERGENT` bullet's disposal sentences — from `every blocker still standing
is DISPOSED` to `a promoted unit is audited as a SPEC` — become: every CONFIRMED finding is
DISPOSED BY SEVERITY, and that holds at `CONVERGED` too; a BLOCKER or HIGH is PROMOTED, becoming a
UNIT whose mechanism CLOSES the finding, specced at its tier, audited as a SPEC, built, closed; a
MEDIUM or LOW is FOLDED into the spec it belongs to as a `rev-N` bump with its §9 line. The
`never RETIRED` sentence and the `--disposition` recording sentence stay as unit 6 leaves them.

`tools/unattended/VERBS.template.md`, the `--review` bullet at lines 102-113: the clause `Both
values are legal, because the method admits folding a blocker back into the specs it belongs to as
readily as promoting it to a unit` is false under the severity rule, since a blocker is never
folded. It becomes a pointer, spelled with the words `severity rule`, which the file does not
carry at base: which value the run records follows the severity rule the Skill's exit bullet
states, and a record naming neither leaves the gate inferring one from ids. One statement in the
Skill, one pointer here, the rule itself in M4 — the shape the carriers already have.

Both renders, `.claude/skills/unattended/SKILL.md` and `memory/guides/UNATTENDED-VERBS.md`, are
re-made by `bash tools/unattended/adopt-unattended.sh` in the same commit, and the
`unattended skill wiring` leg diffs them.

### The driver's own words

`tools/unattended/unattended.sh:4096`, the `fail 37` for a round on a subject whose loop already
ended, says a blocker confirmed on it now is `DISPOSED under the build method's M4, fold or
promote, and never re-rounded`. That message is the check-37 half of `TOOL-aLeakedHandle-6`'s
ruling and points at the M4 sentence this unit rewrites, so left alone it is the driver's own
refusal pointing at the old rule. The clause becomes `DISPOSED under the build method's M4 by the
severity rule, and never re-rounded`; the branch, its number, its trigger and its grep — which
unit 6 widens to `BOUNDED` on the line above — do not move. The three suite arms that quote the
message, at `tools/unattended/unattended.test.sh:4589`, `:4601` and `:4609`, move to the new
words, so `harness arms` still finds the branch armed. `fold or promote` then prints zero times
in the driver and in its suite; the one other carrier of those words, check 2's refusal in
`tools/unattended/check-unattended.sh:537`, speaks of the FIELD's two legal values and not of the
rule, and stays.

That message is not the driver's only by-nature disposal prose. Verified at base,
`grep -c 'blocker still standing' tools/unattended/unattended.sh` prints 3 — `:3969`, inside the
comment block unit 6 rewrites ahead of this pass, and `:4025` and `:4026`, the two sentences of
`review_exit_note`, which every terminal echo prints, unit 6's `BOUNDED` echo included. After the
M4 swap a `--disposition fold` at a `NON-CONVERGENT`, `CEILING` or `BOUNDED` exit would make the
driver assert "every blocker still standing was FOLDED into the specs it belongs to", which M4
then forbids — one echo line carrying two answers. The two sentences become the severity rule's
halves: `fold` prints that every MEDIUM and LOW confirmed at this exit was `FOLDED into the specs
it belongs to`, which is the recorded disposition, and that the severity rule never folds a
BLOCKER or HIGH; `promote` prints that every BLOCKER and HIGH confirmed at this exit is
`PROMOTED` to a unit of this build, specced at its tier and built, and that a MEDIUM or LOW is
folded. The two substrings the suite already reads — `PROMOTED` at `unattended.test.sh:4597`
and `FOLDED into the specs it belongs to` at `:4643` — are kept verbatim inside the new
sentences, so those two arms stand and pass for the reason they were written; the function's
`*)` arm and the header above it at `:4020` to `:4022` are untouched.

The fourth carrier is the requires-disposition `fail 37` at `:4107`, whose clause `because the
method admits BOTH fold and promote at the exit` cites a rule M4 no longer states, and the
comment at `:4101` to `:4103` above the state gate, `M4 admits BOTH`. The clause becomes
`because the severity rule decides which of fold and promote the exit records`, keeping the
`and a record naming neither leaves the gate inferring one from ids` half and the legal-values
tail; the comment says M4 disposes by severity and the field records which value the exit took.
The case that guards it — `NON-CONVERGENT|CEILING|BOUNDED)` as unit 6 leaves it — does not
move. The arm at `unattended.test.sh:4634` quotes the old clause and MOVES with it, so four
suite arms move in this pass, not three; spec 6 rev-4 corrects its own "stands unchanged" for
that arm. `admits BOTH` then prints zero times in the driver, where at base it prints 2, and
zero in the suite, where at base it prints 1.

### The suite

`tools/workflows/unattended-build.test.sh` evaluates the RENDER (`$F` at line 18 is
`unattended-build.js`) with stub hooks, so the pass edits the template, renders, then observes.
Four fixture moves and seven arms, V7 being one `has` line added to an arm that exists:

- `review_out` at line 95 takes `<blockers> [confirmed] [highs]`, `confirmed` defaulting to the
  blocker count and `highs` to 0, and emits both keys. The comment above it says the double returns
  the callee's real keys; `confirmed` is one it omitted.
- The 18 inline fixtures of the shape `"workflow":{"blockers":N,"report":"r.md"}` with an integer
  `N` gain `"confirmed":N,"highs":0` by one substitution; the two carrying `"blockers":null` at
  lines 169 and 286 stay, since the blocker refusal fires first and that is what they arm.
- `returns` at lines 101-102 builds its default disposal from its count argument —
  `{"disposed":true,"standing":[],"promoted":<count>,"folded":0,"summary":"ok"}` — so the arms at
  lines 501, 538 and 605 that pair `NON-CONVERGENT 2` with the default still reconcile and still
  receive the full roster. `DISPOSE_OK` at line 90 gains `"promoted":0,"folded":0` for the arms that
  name it at a count of zero, where the stage is skipped. No helper is minted.
- Lines 471 and 590 quote `DEGRADED — findings were not disposed`; line 376 quotes
  `REACHABLE HERE SINCE`; the AC4 label at lines 457-463 says the skip is on a confirmed count of
  zero, since the arm now observes that predicate.

The arms, in the suite's own `has`/`hasnt_`/`same` style, all reading the trace or the RESULT line:

| Arm | Fixture | Asserts |
|---|---|---|
| V1 | `CONVERGED`, `review_out 0 4 1`, disposal `{disposed:true, standing:[], promoted:1, folded:3, summary:"d"}` | `agent:dispose:tB` in the trace; the log carries `disposing by severity, on CONVERGED too`; the prompt line carries `1 at HIGH` and `--rescope tB --act add --item <id> --reason`; RESULT carries `"promoted":1,"folded":3` and `"roster":[{` |
| V2 | `CONVERGED`, `review_out 0` | `disposal: skipped`; no `agent:dispose:`; RESULT carries `"promoted":0,"folded":0` (the AC4 arm, extended) |
| V3 | `CONVERGED`, `review_out 0 3 0`, disposal `{disposed:true, standing:[], promoted:1, folded:1, summary:"x"}` | `"roster":[]`; the note carries `do not reconcile`; RESULT carries `"promoted":1,"folded":1`; `disposal: done` absent |
| V4 | workflow `{"blockers":0,"report":"r.md"}` with no `confirmed`; and `{"blockers":2,"confirmed":1,"highs":0,"report":"r.md"}` | each THROWs; the message names `confirmed`; `phase:Disposal` absent |
| V5 | `A_UNITS`, workflow `{"blockers":0,"confirmed":2,"highs":0,…}`, disposal `{promoted:0, folded:2, …}` | `agent:dispose:tB` in the trace; the prompt line carries `authored Units table` and NOT `--rescope tB`; RESULT carries `"promoted":0,"folded":2` — the attended MAIN return, since `A_UNITS` is `READY`, carrying the counts the stage returned rather than the default double's |
| V7 | `T_UNITS`, the existing arm at line 493 | RESULT carries `"promoted":0,"folded":0` beside the `"standing":` it already asserts — the attended every-unit-terminal return at line 851, the one return no other arm reaches, carrying both keys as stated zeros rather than omitting them |
| V6 | the header slice `$HDR` | carries `REACHABLE HERE SINCE` (the moved arm at line 376) |

The failing case is observed before the harness edit: with the fixtures and arms staged and the
render UNCHANGED, V1 lacks `agent:dispose:`, V3 hands out a full roster, V4's first invocation
returns a RESULT, V5 spawns nothing, V6 greps the old literal and V7's RESULT carries neither key
— six reds, V2 excepted, because the old skip line shares the prefix. That run is not the suite
whole: section 7 says how one arm is run alone.

### Inventory

No identifier is minted in a graded cell. `promoted` and `folded` are JSON keys of an existing
schema; the guards are inline in an existing block; the suite gains no function. The lexicon has
nothing to grade.

### Rollout

The pass writes `tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js`
by `--render`, `tools/workflows/unattended-build.test.sh`,
`tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md` by `--render`,
`tools/unattended/SKILL.template.md`, `tools/unattended/VERBS.template.md`, their two renders by the
adopter, `tools/unattended/unattended.sh` (the words of two messages, two exit-note sentences
and one comment) and `tools/unattended/unattended.test.sh` (the four `hit` literals quoting
them),
`memory/guides/SESSION-KICKOFF.md` (the `last-audit` line only), its own spec header, the
build README and the two generated indexes every pass re-renders, and its acceptance ledger under
the build's `build/` folder, declared by file. It is sequenced last by its `order` verb and after
unit 6 in particular, which edits the same M4 paragraph, Skill list, VERBS bullet, harness
template and driver line; every carrier is read as unit 6 leaves it. Landing owes no data step: `DISPOSAL_SCHEMA`
binds an agent return inside one program run, a run-state file written before this unit reads
identically after it, and the hand-out's two new keys are additive.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/workflows/unattended-build.template.js` | one refusal added; `au` gains two fields; the stage's predicate, log lines, prompt, schema, guard and three returns; `meta.phases[2].detail` and three comment blocks |
| `tools/workflows/unattended-build.js` | re-rendered |
| `tools/workflows/unattended-build.test.sh` | `review_out`, `returns`, `DISPOSE_OK`, 18 fixtures, three literals moved, one label, six arms and one `has` line on a seventh |
| `tools/memory-tree/BUILD-METHOD.template.md` | two sentences replaced in M4, at lines 140 and 143 |
| `memory/guides/BUILD-METHOD.md` | re-rendered |
| `tools/unattended/SKILL.template.md` | two bullets in the review-state list |
| `tools/unattended/VERBS.template.md` | one clause in the `--review` bullet |
| `.claude/skills/unattended/SKILL.md`, `memory/guides/UNATTENDED-VERBS.md` | re-rendered |
| `tools/unattended/unattended.sh` | words only: the `fail 37` messages at lines 4096 and 4107, the comment at 4101-4103, and `review_exit_note`'s two sentences at 4025-4026 |
| `tools/unattended/unattended.test.sh` | the four `hit` literals quoting those messages, lines 4589, 4601, 4609 and 4634; the `PROMOTED` and `FOLDED into the specs it belongs to` arms at 4597 and 4643 stand |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamped |

### Alternatives rejected

- **Leave the predicate on the verdict and add `highs > 0` to it.** Mediums and lows stay
  undisposed, which is half the owner's rule; and `highs` is one severity where `confirmed` is the
  set.
- **Carry a `promotedIds` array on the hand-out.** The `rescope · add` row is the record and
  `--plan` is the caller's re-read; a second carrier of the same ids is two answers. Section 8 F1.
- **Accept a return whose counts do not reconcile and log it.** That is the `{disposed: true,
  standing: ['b1']}` defect with different keys; the file records what it cost.
- **Tolerate an absent `confirmed` by reading it as zero.** The blocker refusal exists because a
  null read as zero made every degraded audit look clean; the same integer one key over gets the
  same refusal.
- **Add an arm filter to the suite so one arm can run alone.** Sourcing its preamble does that
  today at no edit; section 7 spells it.
- **Edit the backlog row in the pass.** Refused by `fail 49` at declaration, so it cannot be done
  honestly; the closing pass owns it.

## 5. Production-readiness checklist

- security — N/A. Three prompt sentences, one refusal, one schema and one guard inside a sidechain
  program; no write path opens.
- perf / scale — one more agent spawn on every round that confirms a finding at `CONVERGED`, which
  used to be free; that spawn is the owner's rule. The method grows by 62 bytes net against M7's
  whole-file re-read.
- error / empty / loading states — a count that cannot be read throws; a return that does not
  reconcile hands out no roster and says why; a zero count skips and says so. Each is an arm.
- observability — THE COST, stated plainly: a `CONVERGED` round that this unit disposes records NO
  disposition in the run-state file, because `verb_review` refuses `--disposition` there and check
  2 reads the field only on the two non-`CONVERGED` exits. Its promotions are visible as
  `rescope · add` rows and its folds as rev bumps with §9 lines; the hand-out carries the split;
  nothing joins the three. Check 2's promote-demands-new-ids clause therefore does not grade a
  `CONVERGED` exit's promotions.
- risks — a synthesis pass that under-counts `blockers` or `highs` is not caught here: S2 refuses
  more than `confirmed`, never fewer, since a synthesis that classified a confirmed finding as
  medium is a judgement and not a contradiction. The disposal agent reads the report's own severity
  table, so the harness's integers steer the announcement and the reconciliation, not the split.
- testing — the harness arms section 4 tables, each observed RED against the unchanged render one
  at a time, V2 excepted; one driver-suite arm run alone; the grep pairs of AC6 to AC10. The suites
  whole and every leg are the close's; AC10 owns the one direct harness-suite run, and section 7
  prices it.
- migration — N/A. No record grammar, conf key or file format changes; two additive JSON keys.
- user docs — the method and the Skill are the documents and both move here; VERBS points.

## 6. Acceptance criteria

The pass observes each criterion by the single arm or the grep it names; every leg and every
suite whole is the close's, and a ledger row for that half reads `observed at --close`, per the
build README's rules.

- **AC1** — When one arm is run alone against the landed render — from `tools/workflows`, with the
  suite's preamble sourced up to its first arm, `run_wf "$UNITS" "$(returns CONVERGED 0 '<V1 disposal>')"`
  after `review_out` is redefined to emit `confirmed 4` and `highs 1` — the trace holds
  `agent:dispose:tB`, the log line `disposing by severity, on CONVERGED too`, a prompt line carrying
  `--rescope tB --act add --item` and `--reason`, and a RESULT line carrying `"promoted":1,"folded":3`
  and `"roster":[{`.
  Red when: the trace lacks `agent:dispose:` — the predicate is still the verdict — or the RESULT
  lacks either key, or the prompt line names no `--rescope`.
  fixture: the preamble is `sed -n '1,/^# ---- AC2: THE ARGS GUARD/p' unattended-build.test.sh`,
  sourced in a shell whose working directory is `tools/workflows` so `HERE` resolves; those lines
  define every helper and run no arm.
- **AC2** — When the same single-arm run pairs `CONVERGED` with `review_out 0`, the trace holds
  `disposal: skipped` and no `agent:dispose:` line, and the RESULT carries `"promoted":0,"folded":0`
  and `"roster":[{`.
  Red when: an agent is spawned at a confirmed count of zero, or the RESULT lacks the two keys,
  which would mean the skip path carries a missing key where the file's rule demands a stated zero.
- **AC3** — When the single-arm run hands the harness a workflow return of
  `{"blockers":0,"report":"r.md"}` with no `confirmed` key, and again `{"blockers":2,"confirmed":1,"highs":0,"report":"r.md"}`,
  each prints a `THROW` line whose message names `confirmed`, and neither trace holds
  `phase:Disposal`.
  Red when: either returns a RESULT line, meaning an unreadable or contradictory count was read as
  a number and the stage decided on it.
- **AC4** — When the single-arm run uses `A_UNITS` with a workflow return of
  `{"blockers":0,"confirmed":2,"highs":0,"report":"r.md"}` and a disposal double returning
  `promoted 0, folded 2`, the trace holds `agent:dispose:tB`, its prompt line carries
  `authored Units table` and does not carry `--rescope tB`, and the RESULT line carries
  `"promoted":0,"folded":2`; and when the existing `T_UNITS` arm is run alone, its RESULT line
  carries `"promoted":0,"folded":0` beside the `"standing":` it already asserts.
  Red when: the attended prompt orders `--rescope`, which `fail 48`s with no run-state file, or no
  agent is spawned at all, which is the header's old claim still true; or either attended return
  omits the two keys, which the file's own rule at lines 895-899 refuses as a missing key standing
  in for a stated zero.
- **AC5** — When the single-arm run pairs `CONVERGED` and `review_out 0 3 0` with a disposal
  double returning `{"disposed":true,"standing":[],"promoted":1,"folded":1,"summary":"x"}`, the
  RESULT carries `"roster":[]` and `"promoted":1,"folded":1`, the note carries `do not reconcile`,
  and the trace lacks `disposal: done`.
  Red when: a full roster is handed out over a return whose counts leave one confirmed finding
  unaccounted for, the shape the F4 arm at `tools/workflows/unattended-build.test.sh:588` already
  refuses for a named standing blocker.
- **AC6** — When `grep -c 'REACHABLE HERE SINCE' tools/workflows/unattended-build.template.js`
  and the same grep over `tools/workflows/unattended-build.js` run at the landed tip, each prints
  `1`; `grep -c 'UNREACHABLE HERE'` over both prints `0`; and `grep -c 'blocker still standing'`
  over both prints `0`, where at base it prints `2`, lines 9 and 730. The `workflow script
  syntax` leg, `node tools/workflows/check-workflow-syntax.js`, and the `review-protocol parity`
  leg, `bash tools/workflows/check-protocol-parity.test.sh`, are observed at `--close`, the
  second printing no `DRIFT`.
  Red when: the render disagrees with the template, which a template-only edit without `--render`
  produces and the parity leg names at the close; or the header still says the clause is
  unreachable, which keeps the old arm at line 376 green over a false comment; or the exported
  `meta` still describes disposal by nature; or the syntax leg refuses the file, which is what an
  unbalanced ternary inside the prompt string looks like.
- **AC7** — When `grep -cF 'DISPOSED BY SEVERITY' memory/guides/BUILD-METHOD.md` and the same
  grep over `tools/memory-tree/BUILD-METHOD.template.md` run at the landed tip, each prints `1`;
  `grep -cF "takes the severity rule's disposition"` over both prints `1` and
  `grep -cF 'FOLD or PROMOTE'` over both prints `0`, where at base it prints `1`; `wc -l` over the
  render prints at most 350; and `wc -c` over the render prints exactly 62 more than the same
  path read by `git show` from the pass's parent commit. The `kit/dogfood doc parity` leg,
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` printing `shipped and installed docs
  agree`; the `build-method size` leg, `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md`
  printing `template-size OK` with a figure at or below the 27648 in
  `tools/template-size-limits.txt`; and the `kickoff-manifest ratchet` leg,
  `bash skills/session-kickoff/manifest-check.sh` reporting no watched file changed since
  `last-audit`, are observed at `--close`.
  Red when: a count prints `0` where `1` is expected, or `1` where `0` is; or the delta is not
  62, meaning a swap moved more than its sentence; or, at the close, the parity leg prints
  `DRIFT`, the render passes 27648, which is `fail 2`, or the ratchet names
  `memory/guides/BUILD-METHOD.md` as changed after the stamp, meaning the render landed without
  the same-commit re-stamp.
  figure: the cap is DERIVED at observation from `tools/template-size-limits.txt`; the 62-byte
  delta is PINNED from the two sentence measurements in section 4 at base `1b000d1a`; the
  whole-file figures there are PINNED before units 1 and 6 landed their edits, so a
  `TEMPLATE-SIZE WARN` past 26941 is advisory and is reported, not red.
- **AC8** — When `grep -c 'DISPOSED BY SEVERITY' tools/unattended/SKILL.template.md` and the
  same grep over `.claude/skills/unattended/SKILL.md` run at the landed tip, each prints `1`;
  `grep -c 'still disposed'` over both prints `1`, where at base it prints `0`;
  `grep -c 'severity rule' tools/unattended/VERBS.template.md` and the same over
  `memory/guides/UNATTENDED-VERBS.md` each print `1`, where at base each prints `0`; and
  `grep -c 'as readily as promoting' tools/unattended/VERBS.template.md` prints `0`. The
  `unattended skill wiring` leg, `bash tools/unattended/adopt-unattended.sh --check`, is observed
  at `--close`.
  Red when: `--check` reports drift at the close, which a template edit without the adopter run
  produces; or the Skill still disposes by nature; or the `CONVERGED` bullet was left saying
  nothing about disposal, which the `NON-CONVERGENT` grep alone cannot see; or VERBS lost its
  false clause without gaining the pointer, which the absence grep alone cannot see; or VERBS
  still says a blocker may be folded.
- **AC9** — When `grep -c 'fold or promote' tools/unattended/unattended.sh` runs at the landed
  tip it prints `0`, where at base it prints `1`; the same grep over
  `tools/unattended/unattended.test.sh` prints `0`, where at base it prints `3`;
  `grep -c 'blocker still standing' tools/unattended/unattended.sh` prints `0`, where at base it
  prints `3` at `:3969`, `:4025` and `:4026` — the first sits in the comment block unit 6
  rewrites ahead of this pass, so the count when this pass opens is 2 or 3 and the tip is `0`
  either way; `grep -c 'admits BOTH' tools/unattended/unattended.sh` prints `0`, where at base it
  prints `2` at `:4101` and `:4107`, and the same grep over `tools/unattended/unattended.test.sh`
  prints `0`, where at base it prints `1` at `:4634`;
  `grep -c 'by the severity rule, and never re-rounded' tools/unattended/unattended.sh` prints
  `1`; `grep -c 'PROMOTED to a unit of this build' tools/unattended/unattended.sh` and
  `grep -c 'FOLDED into the specs it belongs to' tools/unattended/unattended.sh` each print `1`,
  as at base — the substrings the standing arms at `:4597` and `:4643` read, kept inside the
  rewritten sentences; and one of the
  four arms quoting a rewritten message, run alone by the form spec 6 section 4's suite paragraph
  gives — the preamble sourced, `bcsetup`, then the arm's `bcopen` block through its `hit` line —
  is silent, where against the driver at base it prints `FAIL missing`. The `harness arms` leg is
  observed at `--close`.
  Red when: the driver's refusal still points at the old rule; or an exit note still asserts that
  standing blockers were folded, which the `blocker still standing` grep alone sees; or the
  requires-disposition refusal still cites a rule M4 no longer states; or an arm still quotes the
  old words, which reds the message and the arm together; or a rewritten sentence dropped a
  substring a standing arm reads, so an arm this unit did not touch reds; or the branch reads as
  unarmed at the close because an arm's literal and its message drifted apart.
- **AC10** — When `grep -c 'blockers were not disposed' tools/workflows/unattended-build.test.sh`
  runs at the landed tip it prints `0`, where at base it prints `2`, lines 471 and 590;
  `grep -c 'UNREACHABLE HERE'` over the same file prints `0`, where at base it prints `1`, line
  376; and `grep -c 'REACHABLE HERE SINCE'` over it prints `1`, where at base it prints `0`. The
  suite whole — `bash tools/workflows/unattended-build.test.sh` redirected to a file and never
  read through `tail` — prints no `FAIL` line and its `--- <n> arms` line, the suite's own at
  line 902, reads 237 plus the assertion lines this unit adds; that half is observed at
  `--close`, and it is the one run that loads every fixture S8 moves, where the pass's single
  arms paste their own.
  Red when: a literal at 471, 590 or 376 still quotes the old noun or the old header claim, so
  an arm passes over a message the render no longer prints, or a header arm stays green over a
  false comment; or, at the close, a `FAIL` line, or an arms figure below 237 plus the
  additions, which is an arm de-collected rather than one that passed.
  figure: 237 is PINNED from the 2026-09-14 run at `270611cd` section 7 records; the additions
  are DERIVED as the `has`, `hasnt_` and `same` lines this pass's diff adds, each of which
  increments the suite's `n`.

## 7. Gates

`workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit/dogfood doc parity` · `build-method size` · `kickoff-manifest ratchet` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `method carriers (every pointer declared)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

These are what `--close` runs, once, over the whole build. The PASS does not run them, nor any
suite: it verifies with the single-arm runs AC1 through AC5 describe, against the render, then
the grep pairs of AC6 through AC10 and AC9's one driver-suite arm run alone. Where a criterion
also names a leg or a suite whole — the syntax and parity legs in AC6, the three method legs in
AC7, the wiring leg in AC8, `harness arms` in AC9, the harness suite whole in AC10 — that half
is the close's observation of the same criterion, and its ledger row reads `observed at
--close`. Chunks and guards, read from
`tools/gate-legs.json` on 2026-09-14: `workflow script syntax` is `wiring`, unguarded;
`review-protocol parity`, `harness arms`, `method carriers`, `spec tokens` and
`kit/dogfood doc parity` are `declarations`, the last guarded on six paths that this pass's diff
cannot miss because `--render` rewrites `memory/guides/BUILD-METHOD.md`; `build-method size` is
`product`; `kickoff-manifest ratchet` and `memory hygiene` are `records`; `unattended skill
wiring` is `wiring`. `harness arms` joins the list because this pass now rewrites the words of a
`fail 37` message and the three arms that quote it, and that leg is what reads the pair. None
is `selftests`.

`tools/workflows/unattended-build.test.sh` is on NO bar: no row in `tools/gate-legs.json` names it
and no budget row exists for it, so neither `GATE_FULL=1` nor `GATE_SELFTESTS=1` reaches it. The
compensating check is one direct run at the close, whole, redirected to a file and never read
through `tail`: measured on node `a` on 2026-09-14 at `270611cd`, 237 arms, exit 0, 335 s. After
this unit the arm count is 237 plus the additions and the suite's own `--- <n> arms` line is the
figure; AC10's suite half is the criterion that owns the run and the row that reads
`observed at --close`. The per-arm form the pass uses is AC1's preamble source.

New arm: `tools/workflows/unattended-build.test.sh` · V1, V3, V4, V5 and V6 each stage their red
against the unchanged render, one arm at a time · no floor exists in this suite.

Moved arm: `tools/workflows/unattended-build.test.sh` · lines 376, 471 and 590 quote the new
literals; the AC4 arm at 457-463 is re-labelled and extended into V2; the `T_UNITS` arm at 493
gains V7's one `has` line · no floor.

Moved arm: `tools/unattended/unattended.test.sh` · the four `hit` literals at 4589, 4601, 4609
and 4634 quote the two rewritten `fail 37` messages; the `PROMOTED` and `FOLDED into the specs
it belongs to` arms at 4597 and 4643 stand, their substrings kept; no arm is added or removed ·
`FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` do not move, because the executed count does not.

## 8. Open questions

- **F1 — does the hand-out carry the promoted unit ids, or only the count?** Option A, the count:
  the brief's shape; the ids are in the `rescope · add` rows and in `summary`, and the caller's
  contract is to re-read `--plan <slug> --paths` between dispatches. Option B, a `promotedIds` array
  beside the count: the caller reads which units to audit from the return. Recommendation: A.
  RESOLVED (agent, 2026-09-14, delegated): A. The run-state row is the record and a second carrier
  of the same ids is two answers; the caller already re-reads `--plan`, and `specs-reviewed` at
  `--close` refuses a promoted spec no review names whichever carrier the caller read. Veto 2 is
  not tripped either way; A leaves fewer open questions.
- **F2 — does a return whose counts do not add to `confirmed` refuse, or log?** Option A, refuse
  with the empty roster: the existing guard's shape, one more clause. Option B, log the mismatch and
  hand out: the stage's `summary` outranks its numbers. Recommendation: A.
  RESOLVED (agent, 2026-09-14, delegated): A. B is the `disposed: true, standing: ['b1']` defect
  the file records clearing the old guard, with the contradiction moved into two integers; the
  file's rule is that a stage's report of what it did NOT do outranks its summary. Veto 3 is not
  tripped: the refusal narrows the hand-out, it widens nothing.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft, from the brief and the owner's severity ruling in the build
  README. Two departures from the brief, each with its reason in §3: the backlog row flip is the
  closing pass's, because `fail 49` refuses the declaration; and the stage prompt is mode-aware,
  because the brief's predicate makes the stage reachable in attended mode where `--rescope`
  refuses.
- rev-2 · 2026-09-14 · folded the round-1 spec audit: clusters B (id 22 — AC6 to AC8 reduced to their grep pairs, the six leg runs at `--close`), E (id 48 — the recorder as unit 6 leaves it, in §3), K (id 52 — the line-143 sentence and the `fail 37` message at `unattended.sh:4096` join the carriers, minus 13 bytes, `TOOL-aLeakedHandle-6` in §10, AC9), M (ids 15, 16 — AC4's RESULT keys and V7, AC8's `still disposed` and `severity rule` greps), S (id 46 — `meta.phases[2].detail`, AC6's retired-phrase grep), T (id 45 — `--reason` on the promotion command).
- rev-3 · 2026-09-14 · §3 · §4 · §5 · §7 · S7 · S8 · AC9 · AC10 · folded the round-2 spec audit: clusters D (id 5 — AC10, the harness suite's own text by three greps in the pass and its whole run at `--close`, the row S8 and the §3 hands-off bullet lacked), G (id 28 — `review_exit_note`'s two sentences at `unattended.sh:4025` to `:4026` and the `:4107` clause with its `:4101` to `:4103` comment join S7 with severity-rule wording; AC9's zero-count greps over `blocker still standing`, base 3, and `admits BOTH`, base 2 in the driver and 1 in the suite — the audit wrote 1 for the driver and the tree says 2; the `:4634` arm moves with the clause, four arms not three, with spec 6 rev-4 corrected in the same fold).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "dispose every confirmed review finding by severity,
promoting a blocker or high to a unit and folding a medium or low into its spec"`, run on
2026-09-14 at `270611cd`, reported `scan coverage: 71 files scanned | 0 parse skips | unscanned
layers: .sh` and ranked drift-audit and govkit Python symbols, none of them this seam. The harness
is a `.js` the map scans and its suite is a `.sh` it does not, so the probe is blind to half of
this unit and no claim here rests on it.

The seam EXISTS and was found by reading source: the DISPOSAL stage at
`tools/workflows/unattended-build.template.js:704-774` with its `DISPOSAL_SCHEMA` at 320-329 and
the `standing` guard at 751-772, which this unit extends rather than replaces; the blocker refusal
at 587-593, whose shape the new refusal copies; and `tier2-review.js`'s return at 607-646, which
already carries `confirmed`, `blockers` and `highs`, so no callee changes. On the suite side the
seam is `run_wf`, `review_out`, `returns` and the `has`/`hasnt_` helpers of
`tools/workflows/unattended-build.test.sh`; the arms mint nothing. The recall probe returned the
build that wrote the stage, `TOOL-aHoistedPass-6`, whose spec cites the skip as the
`CONVERGED`-only path; `TOOL-aStagedLane-2`, which recorded that attended mode never composes the
disposal clause and cites it at `unattended-build.js:473`, STALE against source where the skip sits
at line 725; and `TOOL-aProvenReuse-3` as the open row this ruling answers. The
`aCollapsedScan-4` round-1 record was the hit that put a real number on the defect: zero blockers,
eight highs, six mediums, one low, `CONVERGED`. The round-1 audit added a ruling the probe had
missed: `TOOL-aLeakedHandle-6`, the owner's ruling of 2026-09-13 in `memory/DECISIONS.md` that a
blocker found on a CONVERGED subject is disposed under M4 and never re-rounded, which landed the
line-143 sentence and the `fail 37` message this unit rewrites. This unit NARROWS that ruling:
"never re-rounded" and the driver's refusal stand untouched, and only what the disposition IS —
"the exit's own, FOLD or PROMOTE" — becomes the severity rule's, because under that rule a
`CONVERGED` exit has no disposition of its own to take. It does not supersede it.

Recall terms used: `python tools/memory-recall/query.py "what disposes a confirmed review finding
at a spec-audit exit, and why does the disposal stage skip on CONVERGED" --terms "disposal fold
promote severity blocker high medium low rescope add unit spec-audit converged skip"`.
