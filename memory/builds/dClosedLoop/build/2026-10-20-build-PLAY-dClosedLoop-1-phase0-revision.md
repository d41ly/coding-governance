# Phase 0 revision: the fifteen findings on P0.1, P0.2, P0.4 and P0.7, verified, with the owner's two questions

**Serves:** research PLAY-dClosedLoop-1

The proposal that `build/…-phase0-revision-brief.md` asked for. Dispatch 234's builder built P0.6, then stopped
before P0.1 and P0.2 and returned thirteen findings. The carries builder (dispatch 235) and the schedule red tests
(dispatch 237) added one each. This record checks each finding against the source it cites, read for this record,
and gives its options, a recommendation and the plan text as it would read. It edits nothing: not the plan, not v2,
not an instrument and not any other record. The owner decides, and a later dispatch applies.

**Conventions.**
- These are the plan's own. `build/` is `memory/builds/dClosedLoop/build/`, and a file there is named by its suffix.
  ER and v2 are as the plan defines them, and "plan:N" is line N of `build/…-execution-plan.md`.
- VERBS is `memory/guides/UNATTENDED-VERBS.md`, and "lib" is `tools/unattended/lib-unattended.sh`.
- The one probe is `d238/passreaders.py` in this session's scratch folder. Under five pass readers, it counts a
  build's spec revisions after each unit's first pass, and it classifies what each revision changed.
- An id no build has minted is written `missing:<id>`.

## [verdicts]

| # | The finding, in short | Verdict | Plan text it changes | Group |
|---|---|---|---|---|
| 1 | Row 3's union reading makes a `Pass: none` commit a pass | CONFIRMED | P0.1 row 3 | fix |
| 2 | Generated-region re-renders are listed as members | PARTLY: 8 of the 9 change only a gen region; the ninth is a Status flip plus a re-render. All 9 are listed | P0.1, a new false-red row | fix |
| 3 | Divergence hand-backs have no named source or address | CONFIRMED | P0.1's further arms | fix |
| 4 | An `amended rev-N` row has no join address | CONFIRMED | P0.1 row 7 | fix |
| 5 | No audited-revision pin exists | PARTLY: the grammar allows one and one old record carries it; nothing writes one today | P0.1's further arms; P0.2's sources | fix |
| 6 | Nothing says how the report learns the run kind | CONFIRMED | P0.2, its name | fix |
| 7 | Under `report` every plant exits 0; row 5's exit unstated | CONFIRMED | P0.1's chain values and acceptance | **owner** |
| 8 | The `approver` plant turns green under `author-recorded` | CONFIRMED | P0.1 row 6; plan:719 | fix |
| 9 | Decision ids in the `missing:` form inside the instrument | CONFIRMED | P0.1 row 6; one P0.8 sentence | **owner** |
| 10 | `missing:` fixture ids fail the H1 and backlog grammars | CONFIRMED | P0.1's opening paragraph | fix |
| 11 | P0.7's bare-id check goes red on the opening's own ids | CONFIRMED | P0.7 | fix |
| 12 | The report's blob line is assigned to no builder | CONFIRMED | P0.1 row 10; P0.2's list | fix |
| 13 | `asbuilt.py` reads its baseline unpinned | CONFIRMED | P0.1, a new row | fix |
| 14 | The token arm misses a carrier moved in by a `**Moved:**` line | CONFIRMED | P0.1 row 1 | fix |
| 15 | The schedule script discards row 9's note | CONFIRMED | P0.4 row 9 | fix |

Thirteen are CONFIRMED, two PARTLY and none REFUTED. Two fixes touch an owner answer, and `[owner]` asks about them.
The other thirteen follow from the plan's own answers and change none of them. v2 is unchanged throughout.

P0.3 needs no change. Its field 1 already prints and pins each instrument's blob (plan:257). The recommended fix for
finding 9 spares it a re-pin.

## [owner]

Two questions. No other fix changes or reads against an answer. Finding 6 applies README rule 1, from answer 1
(ER:84) and "dTrueNorth's extra unit (Recommended)" (ER:232). Finding 8 applies "A deviation, your values
(Recommended)" (ER:189). Each leaves its answer as given.

**Q1, finding 7: a moved design baseline under `report`.** The answers it reads against are answer 3, "departures are
recorded and explained at the end, nothing is parked or blocked - the build must go through to completion."
(ER:103-104), and "Report, as read (Recommended)" (ER:255).
- **Listed first (Recommended).** A v2 whose `Baseline:` no longer matches the pinned sha counts as a member that no
  record can join. It goes first in the report, `report` exits 0 and `refuse` exits 1, so nothing stops a run. You see
  it at the top of the next departures report, and P0.7's "0 members" check goes red on it.
- **Exit 2 under both policies.** README rule 4's close sequence stops on it, and the run waits for you. That is a
  park, against answer 3.

**Q2, finding 9: P0.8's rows 1 and 6 name the ids they approve.** The answer it reads against is "Hold, on to Phase 1
(Recommended)" (ER:461), with the rows standing as quoted.
- **Rows 1 and 6 name the ids (Recommended).** Row 1 adds dTrueNorth's extra unit's id, which the opening mints in the
  same landing. Row 6 adds `cl-dClosedLoop-0120`. Row 3 already names `cl-dClosedLoop-0004`. What each row decides is
  unchanged. The approver arm then holds no decision id: it looks up the cited id in `memory/DECISIONS.md`.
- **The instrument maps row numbers to ids.** It holds the nine ids in the `missing:` form until the rows land, and
  strips the prefix when comparing. That makes a second typed copy of the nine ids.
- **The ids are written into `deviations.py` once P0.8's rows exist.** Before the landing, every packet is rendered
  again. After it, an owner-asked `--repin` landing is needed (plan:282-284).

## [decisions] The two findings the owner decides

### Finding 7: plants under `report`, and row 5's exit

> Policy versus plants: under the default `report` every plant exits 0; the plan should say whether plants are read
> under `refuse`, and give the exit code for row 5's refused Baseline.

**Verdict: CONFIRMED.** The finding holds on three counts:
- Under `report`, the instrument "prints every member and exits 0" (plan:158-160).
- P0.1's table and acceptance say only that a plant is "red", and that every plant "exits as its row says"
  (plan:139-151, :163). Under the default policy, no plant can be red.
- Row 5 says to "refuse a v2 whose `Baseline:` differs" (plan:145), but gives no exit code and no policy. Today the
  instrument reads the baseline from v2's working tree (`deviations.py:132-136`), so a re-pointed line moves the
  reference silently.

**Options.**
1. **(Recommended) Plants read under `refuse`, and a moved baseline is a member.** Every plant runs under `--policy
   refuse`, where red means exit 1. It runs again under `report`, where it exits 0 and lists its member. With the pin
   in the instrument, the clause arm still measures against `59ff8f2ac`, so the measurement stays honest. The moved
   `Baseline:` line is listed first, as a member no record joins. This is [owner] Q1's first option.
2. Exit 2 under both policies, as "nothing measured". This is [owner] Q1's second option.

**Revised text**, P0.1's "owner's chain values" paragraph (plan:158-160):

> **The owner's chain values.** Answer 3 also reaches the instruments (ER:126-127). `deviations.py` takes `--policy
> report|refuse`, which defaults to `report`. `report` lists every member and exits 0. `refuse` exits 1 on an
> unjoined member, or on an approver the chain's value refuses (row 6). Every plant in the table above runs under
> `--policy refuse`, where its "red" is exit 1. It runs again under `report`, where it exits 0 and lists its member.
> A v2 whose `Baseline:` differs from the pinned `59ff8f2ac` (row 5) is counted as a member and listed first under
> both policies, as "v2's Baseline moved from 59ff8f2ac to <sha>". No record joins it, since only the owner's re-pin
> moves the pin. Exit 2 keeps its meaning, "nothing measured". Plants: one unjoined member exits 0 and is listed under
> `report`, and exits 1 under `refuse`; a re-pointed `Baseline:` exits 0 and is listed first under `report`, and
> exits 1 under `refuse`.

P0.1's acceptance, first bullet (plan:163):

> - Every plant above exits as its row says under `--policy refuse`, and exits 0 under `report` with its member
>   listed.

P0.7's `deviations.py` check (plan:535) stays as written. A moved baseline is a member, so "printing 0 members"
covers it.

### Finding 9: decision ids in the `missing:` form

> Decision ids: ids written `missing:` in the instrument mean either the approver arm strips the prefix, or
> `deviations.py` is edited when P0.8 lands and every packet is re-pinned.

**Verdict: CONFIRMED.**
- Row 6 names its rows by number: "P0.8 row 3 for the `cl-dClosedLoop-0004` record, row 1 only for the extra unit's
  deviation-2 record, row 6 for dPlacedRequest's record" (plan:146).
- Dispatch 234's brief fixes the nine ids and requires that "in any instrument string or fixture they appear in the
  `missing:` form until the rows land" (`build/…-phase0-brief-deviations.md:46-50`).
- An arm that compares that literal against a landed record's bare citation therefore never matches, unless it
  strips the prefix.
- Every packet pins `deviations.py`'s blob (plan:257). The pin arm goes red on a moved blob (plan:278-280), and a
  blob moves only through `--repin` in an owner-asked landing (plan:282-284).
- One correction to the finding: an edit made before the opening lands needs no `--repin`. The packets are simply
  rendered again in the branch.

**Options.**
1. **(Recommended) Derive the row from what it names.** The instrument carries no decision id. It looks up the cited id
   in `memory/DECISIONS.md` and requires the row to name the record's departure. Rows 1 and 6 must name their ids;
   row 3 already does (plan:552). This is [owner] Q2's first option.
2. Map row numbers to ids in the `missing:` form, and strip the prefix when comparing.
3. Write the ids into `deviations.py` once the rows exist, then render the packets again or re-pin them.

**Revised text.** P0.1 row 6's Fix cell is given in full under finding 8. Its citation sentence, the part this question
decides, reads:

> One naming the owner must cite a decision id whose row `memory/DECISIONS.md` holds at the advertised default-branch
> tip (`origin/main`; under `--report`, `P`). That row must name the record's `**Departs from:**` clause id, or the
> unit its `**Follow-through:** new unit <id>` names. The instrument holds no decision id. P0.8's row 3 qualifies by
> naming `cl-dClosedLoop-0004`, row 6 by naming `cl-dClosedLoop-0120`, and row 1 by naming dTrueNorth's extra unit.
> Row 5 names neither, and fails.

One sentence for P0.8, after its list and before its acceptance (plan:598). P0.8 lies outside the brief's five sections, so it is named here for
the dispatch that applies this:

> Row 1 names dTrueNorth's extra unit by the id the opening mints for it, and row 6 names `cl-dClosedLoop-0120`; row 3
> already names `cl-dClosedLoop-0004`. P0.1 row 6's approver arm reads these names.

## [fixes] The thirteen that follow from the plan's own answers

### Finding 1: which commit is a pass

> Row 3 (which commit is a pass): the fix says to read a pass "as `routed_commits.py:22-26` does", but those lines say
> their union reading is not the pass reader. The harness commits every spec as `spec(<slug>): <ids>` with `Pass:
> none` (`unattended-build.js:1182`). Under the union reading, `Pass: none` keeps the subject's ids, so the spec or
> records commit becomes the unit's first pass, and every later revision becomes a member, which contradicts the
> plan's own `[constraints]` row. Measured on dRenderedAnchor's 7 specs: union counts 19 after-pass revisions, against
> 9 for today's trailer-only reading; its first "pass" for unit 1 is `f576bd192`, a `Pass: none` records commit. The
> driver's own reader is no fix: it counts 17, taking trailer-less status flips like `0f787ab62` as the pass.

**Verdict: CONFIRMED.**

The sources say what the finding says:
- `tools/memory-tree/routed_commits.py:22-26`: "`Pass: none` adds none and keeps the subject's … that reader decides
  which commit is a unit's pass, this leg only whether a commit is attributed to any unit."
- `tools/workflows/unattended-build.js:1182` commits each spec as `spec(<slug>): <ids>` with `--trailer 'Pass: none'`.

The probe over dRenderedAnchor's seven specs reproduces the finding's counts exactly:

| Reader | After-pass revisions |
|---|---|
| Today's (`deviations.py:150`) | 9 |
| The union | 19 |
| The driver's `read_attribution_tokens` (lib:1052-1063) | 17 |

Under the union reader, every unit's first "pass" is a records commit that touches no product path. For unit 1 that is
`f576bd192`, the commit that opens the build, which carries `Pass: none` and comes before the spec exists. Unit 3's
`rev-2`, written before its real pass (`9084a5868`), becomes a member. That contradicts plan:124 ("A spec revised
before its unit's first `Pass:` commit is no member") and plan:797 ("Revise it before its first `Pass:` commit").

The driver's reader takes `0f787ab62`. Its `Pass: none` sits outside the message's last paragraph, so git reads no
trailer and the subject wins. The driver's build-commit predicate (`build_commit`, lib:1095) also counts 17. The
reason is that this repo declares `GENERATED_INDEXES=""` (`.unattended.conf:406`), so the status flip's `memory/LIVE.md`
re-render counts as a write outside the build's record surface (lib:1187-1191).

**Options.**
1. **(Recommended) A pass is a trailer naming the unit, or a trailer-less product commit naming it.** On
   dRenderedAnchor this counts 9, from the same seven first passes as today's reading. It still catches the escape the
   deviation return found: a pass named only in its subject, where "209 of 722 commits touching `tools/` or `skills/`
   since 2026-10-01 have no `Pass:` trailer" (`build/…-research-exec-deviation.md:70-72`). It also keeps v2's "joined
   at the commit through the routed-commit attribution" (v2:1764). The routed-commit attribution decides which commits
   belong to a unit, and this reader picks the passes among them.
2. Today's trailer-only reading, with row 3 withdrawn and its escape moved to `[deviations]` "What nothing catches".
   This also counts 9, but a trailer-less product commit is never a pass.
3. The union as written: 19, against plan:124 and :797.
4. The driver's reader, or `build_commit`: 17, with status flips taken as passes.

**Revised text**, P0.1 row 3 (plan:143). The escape cell is unchanged.

> **Fix:** A unit's first pass is the oldest commit reachable from `HEAD` that does one of two things:
> - it carries a `Pass:` trailer naming the unit, read from git's trailer block as `read_attribution_tokens` reads it
>   (`tools/unattended/lib-unattended.sh:1052-1063`), where `Pass: none` names no unit;
> - or it carries no `Pass:` trailer, names the unit as a whole token in its subject, and writes a path outside every
>   `memory/builds/` folder, `memory/LIVE.md`, `memory/ledger/`, `memory/DECISIONS.md` and
>   `memory/project/readme-contract.txt`.
>
> It is the routed-commit attribution (`tools/memory-tree/routed_commits.py:22-26`), narrowed to the commits that are
> passes. A `Pass: none` spec or records commit (`tools/workflows/unattended-build.js:1182`) belongs to the unit but
> is not its pass, so a spec revised before its pass stays outside the population ([constraints]).
>
> **Plant:** A product commit with no trailer and the id only in its subject, then a revision: red. Controls, each no
> member: a `Pass: none` commit naming the unit in its subject, then a revision; a records-only status flip with no
> trailer naming the unit, then a revision.

### Finding 2: generated regions in the population

> Row 8 / the population: only Status-only edits are excepted. All 9 of the 9 after-pass revisions the trailer reading
> counts on dRenderedAnchor change only a `<!-- gen:... -->` region (the spec-records region, re-rendered as later
> records land). Each would be listed "recorded by nobody".

**Verdict: PARTLY.**
- `deviations.py:157-158` strips only the `**Status:**` line before comparing.
- Of the nine revisions, eight change only the `gen:spec-records` region. The ninth, `3cb77d1e2`, flips the Status
  line from CLOSED to INPROGRESS and adds a spec-records row in the same commit, so it is neither Status-only nor
  gen-only.
- No revision is Status-only, so all nine are listed, as the finding says.
- With the Status line and the gen regions removed together, all nine are unchanged.

The detail matters for the fix: stripping the gen regions alone would still list `3cb77d1e2`.

**Options.**
1. **(Recommended) Except a revision whose text is unchanged once the Status line and every gen region are removed.**
   The regions are stripped by `GEN_REGION_AWK` (lib:1045), read from that file and never copied. That is the one
   strip check 23 uses, and its comment asks for no second copy (lib:1039-1043).
2. Except only gen-only revisions. That still lists `3cb77d1e2`.
3. Read revisions as distinct header `rev-N` values. A material edit made without a rev bump would then escape, which
   is the undeclared departure the join exists to catch.

This reads v2:1764's "green on a status-only edit" as "an edit that changes no authored line". dTrueNorth's product
join takes the plant suite as its acceptance (D3, plan:1190-1193). D3's record should name this exception beside its
stricter plants, so the product inherits it openly.

**Revised text**, a new P0.1 row after row 8 (plan:148):

> | False red: a revision that changes only generated regions, or its `**Status:**` line and generated regions in one
> commit, is a member, since only a Status-only change is excepted (`deviations.py:157-158`) | Except a revision whose
> text is unchanged once its `**Status:**` line and every `<!-- gen:... -->` region are removed. The regions are
> stripped by `GEN_REGION_AWK` (`tools/unattended/lib-unattended.sh:1045`), read from that file and never copied, so
> check 23 and the instrument strip one way. Like that strip, it cannot tell a hand edit inside a region from a render
> (`:1042-1043`) | A spec-records re-render after the pass: green. A Status flip and a re-render in one commit: green. A
> re-render with one acceptance line changed: red |

### Finding 3: divergence hand-backs

> Hand-backs: no RUN.md row records one. The only trace is the `prompts/` revision record the `/build` skill writes,
> whose Goal opens `DIVERGENCE:`. The plan should name that source and its join address.

**Verdict: CONFIRMED.**
- The builder's hand-back is a return field: `diverged` is set when `why` opens `DIVERGENCE:`
  (`tools/workflows/unattended-unit.js:348`).
- The `/build` Skill then writes "a revision record under the build's `prompts/` holding `## The brief` and no `## The
  prompt`, its Goal the builder's `why` verbatim" (`.claude/skills/build/SKILL.md:68`).
- An unattended run is told to handle it "as the `/build` Skill's stage 5 does" (VERBS:758-760).
- RUN.md's rows are rescope acts, briefs, dispatches and parks (VERBS:697-721). None records a hand-back, and no
  driver or checker line reads `diverged`.
- The plan names hand-backs as members but gives neither a source nor an address (plan:153-156, :174).
- Real records have this shape, for example
  `memory/builds/dRedressedBar/prompts/2026-10-14-prompt-TOOL-dRedressedBar-2-2-revision.md`, whose Goal opens
  `DIVERGENCE: spec …`.

**Options.**
1. **(Recommended) Read the revision records.** The address is `<unit>@rev-N`: the unit is the one its `**Serves:**`
   line names, and N is the spec header's revision at the commit that added the record. That is the revision the
   builder was handed. This is the same address a revision member and an `amended` row use (finding 4), so one record
   joins all three.
2. Have the driver write a hand-back row. That is product code, which phase 0 does not write.

**Revised text** is in P0.1's further-arms paragraph, given under finding 5.

### Finding 4: the `amended rev-N` join address

> Ledger rows: an `amended rev-N` row names no record, so its join address is unstated.

**Verdict: CONFIRMED.**
- The ledger form is `- AC2 — amended rev-<n> — the change, and the section 9 line that logs it`, under an
  `**Evidences:** <id>` block of a `journal` record (`memory/HYGIENE.md:603-606`). It names a revision and no record.
- Row 7 says only "Read `amended rev-N` from the ledgers", with the plant "a ledger row with no record: red"
  (plan:147).
- The rescope rows of the further-arms paragraph (plan:153-156) have the same gap, though they are not one of the
  fifteen. The revised text under finding 5 gives each arm one address.

**Options.**
1. **(Recommended) Address it as `<unit>@rev-<N-1>`.** That is the revision the amendment departed from, the same way
   `deviations.py:126` addresses a revision member.
2. Require the ledger line to name its record. That would change the ledger grammar, which the memory-tree kit owns.

**Revised text**, P0.1 row 7's Fix and Plant cells (plan:147):

> **Fix:** Read `amended rev-N` from the ledgers. Each `amended rev-N` line under an `**Evidences:** <unit>` block of
> a `journal` record (`memory/HYGIENE.md:603-606`) is a member, addressed `<unit>@rev-<N-1>`, the revision the
> amendment departed from, as a revision member is addressed. It joins the record departing from that address. A
> hand-back and a revision of the same change carry the same address, so one record joins all three.
>
> **Plant:** A spec quoting `cl-dClosedLoop-0004`: green. A ledger row `amended rev-3` with no record departing from
> `<unit>@rev-2`: red. The same row with that record: green.

### Finding 5: the audited revision

> Audited revision: P0.2 lists revisions "after the pinned audited revision", but no such pin exists in the tree.

**Verdict: PARTLY.**
- `memory/HYGIENE.md:578` lets a `**Serves:**` id carry "a trailing `@rev-N`, which is recorded and never validated".
- One record in the tree carries one: `memory/builds/aPacedTurnstile/reviews/2026-08-20-review-TOOL-aPacedTurnstile-14.md:3`.
- The spec-audit harness writes the binding line with ids only (`tools/workflows/tier2-review.js:1794-1795`), so no
  chain audit will carry a pin until `cl-dClosedLoop-0005` makes one (v2:1764). That clause is dTrueNorth's, built
  inside dTrueNorth's own run, after that run's audit.
- The arm matters from dGroundRules on. A build run that revises a spec before its first pass (plan:797) is exactly
  the case it exists for.

**Options.**
1. **(Recommended) Read the pin wherever an audit record carries one.** A unit with no pin adds nothing to this arm, and
   the report says so.
2. Drop the term until `cl-dClosedLoop-0005` lands. The report would then need its own switch, which is a second
   report-switch step.

**Revised text**, replacing P0.1's "Two more population arms" paragraph (plan:153-156). It also carries findings 3
and 4:

> **Three more population arms.** `deviations.py` also reads these as members:
> - **Rescope rows.** The `add`, `retire` and `supersede` rows from `RUN.md` and every rotated `RUN.*.md`. An `add`
>   joins the record whose `**Follow-through:**` is `new unit <item>`. A `retire` or `supersede` joins the record
>   departing from `<item>@rev-N`, where N is the item's header revision at the row's commit. The planned `defer`
>   rows a spec run writes for its own roster units are not members.
> - **Divergence hand-backs.** Each revision record under the build's `prompts/` whose `### Goal` opens
>   `DIVERGENCE:`. That is the record the `/build` Skill's stage 5 writes, and VERBS:758-760 has a run follow it
>   (`.claude/skills/build/SKILL.md:68`); no `RUN.md` row records a hand-back. It is addressed `<unit>@rev-N`, where
>   the unit is the one its `**Serves:**` line names and N is the spec header's revision at the commit that added the
>   record. It joins the record departing from that address, hand-off `spec-to-code`.
> - **Revisions after the audited revision.** Each commit of a unit's spec that is not an ancestor of the commit
>   adding the newest `spec-audit` record whose `**Serves:**` line pins `<unit>@rev-N` (`memory/HYGIENE.md:578`),
>   addressed `<unit>@rev-N`. Row 8's Status-and-generated exception applies. Today's audit harness writes no pin
>   (`tools/workflows/tier2-review.js:1794-1795`), so a unit without one adds nothing here and the report prints "no
>   audit pin" for it. `cl-dClosedLoop-0005`, which dTrueNorth lands, writes the pin for every later chain audit.
>
> Plants:
> - an add row with no record, and a hand-back with no record, are each listed as unjoined;
> - a spec run's routine defer rows are not listed;
> - a `prompts/` fix record whose Goal does not open `DIVERGENCE:` is no member;
> - an audit record pinning `@rev-1`, then a material edit before any pass: listed. The same edit with no pin: not
>   listed, and the report prints "no audit pin".

P0.2's first source (plan:173):

> - the population for the build: clause moves, revisions after the first pass, revisions after the audited revision
>   a `spec-audit` record pins, ledger `amended` rows, and the rescope rows and divergence hand-backs, all as P0.1's
>   further arms read them;

### Finding 6: the run kind

> Run kind: the report's run kind (spec or build) needs README rule 1's test; nothing says how the instrument gets it.

**Verdict: CONFIRMED.**
- P0.2 names the report by run kind (plan:213-215), and rule 4 uses those names (plan:368-369). Neither says how
  `deviations.py` learns the kind.
- README rule 1's test reads two things at the run's baseline commit: an open ask in the build's `BACKLOG.md`, and a
  starting roster with a unit `MISSING` (plan:356-361).
- A run's `RUN.md` records that commit as `base:`, as in `memory/builds/aBatchedArm/RUN.md`.

**Options.**
1. **(Recommended) Derive it from `base:` and rule 1's test**, which is the same test the extra unit's driver applies
   (plan:638-643).
2. Have the run pass `--kind spec|build`. That is a typed fact beside the tree, which the charter's [derive] rule
   forbids.

**Revised text**, appended to P0.2's "Its name" paragraph (plan:213-215):

> The run kind is derived, never passed. `--report` reads `base:` from the build's live `RUN.md` and applies README
> rule 1's test at that commit:
> - the build's `BACKLOG.md` there holds an open ask, read by the memory-tree kit's row grammar
>   (`tools/memory-tree/row_grammar.py:211`);
> - and a `roster:units` unit of the README there has no spec whose H1 defines it (`tree_lib.parse_spec_h1`).
>
> When both hold, the run is a spec run and the report is named `-departures-spec.md`. Otherwise it is named
> `-departures-build.md`. With no live `RUN.md`, `--report` exits 2 and writes nothing.
>
> Plants:
> - an open ask and one `MISSING` unit at `base:`: `-departures-spec.md`;
> - the same with every unit specced: `-departures-build.md`;
> - no ask and every unit `MISSING`, as in dTrueNorth's whole run: `-departures-build.md`;
> - no live `RUN.md`: exit 2.

### Finding 8: the approver plant under `author-recorded`

> Row 6: under `author-recorded` the existing `approver` plant turns green; the plan should say what replaces it, and
> `[phase-1]`'s "approver below its risk" loses its meaning.

**Verdict: CONFIRMED.**
- Today's `approver` plant writes `author` on a stricter record, which red only under the by-risk compare
  (`deviations.py:81-87`, `:194-195`).
- Row 6 makes "any recorded approver role" pass under `author-recorded` (plan:146), so the plant goes green.
- plan:719 still says "`refuse` exits 1 on an unjoined member or an approver below its risk". Under the chain's value
  no approver is below a risk. The owner chose those values for the interim check (ER:189), and D5's return to
  `by-risk` after the chain is the product keys' job (plan:1372).

**Options.**
1. **(Recommended) Remove the by-risk compare.** A role in the grammar passes, and the old plant becomes a green
   control. The charter's [yagni] rule says delete rather than disable, and the chain never reads `by-risk`.
2. Keep by-risk behind an `--approval` switch. That is scaffolding nothing in the chain calls.

**Revised text**, P0.1 row 6 (plan:146). The citation sentence is [owner] Q2's:

> **Fix:** Under the chain's value `author-recorded` (ER:103-104, :189), the by-risk compare
> (`deviations.py:81-87`) is removed. An approver passes when its `**Approver:**` opens with a role the record
> grammar names, `author`, `spec writer` or `owner` (`deviations.py:14`), whatever the risk. One naming the owner must
> cite a decision id whose row `memory/DECISIONS.md` holds at the advertised default-branch tip (`origin/main`; under
> `--report`, `P`). That row must name the record's `**Departs from:**` clause id, or the unit its `**Follow-through:**
> new unit <id>` names. The instrument holds no decision id. Every later departure's approver is the run's author role,
> citing the ruling, never `owner`.
>
> **Plant:** These are red:
> - an approver line missing, or naming no role;
> - "owner" with no id;
> - an owner approver citing only an ER line;
> - one citing a row that names neither the clause nor the unit (P0.8 row 5);
> - one citing row 1 for a unit a spec run added;
> - one citing an id no row holds.
>
> The `approver` plant, `author` on a stricter record, is now a green control: red before the fix, green after.

plan:719, the Design-exit row:

> At its Design exit, `carries.py --build dTrueNorth --exit` and `deviations.py --policy refuse`, by hand, since
> nothing in the bar runs them yet. `refuse` exits 1 on an unjoined member, or on an approver `author-recorded`
> refuses (P0.1 row 6); the chain's runs keep `report`.

### Finding 10: fixture ids and the grammars

> Fixture ids: `missing:` ids fail the generator's H1 and backlog grammars; a fixture family declared in the fixture
> repo's own conf would work.

**Verdict: CONFIRMED.**
- A spec's defining H1 must open `<FAMILY>-<slug>-<seq>` (`tools/memory-tree/tree_lib.py:219`), and a backlog row its
  id (`tools/memory-tree/row_grammar.py:211`). A `missing:` id fits neither.
- The tree's roster grammar matches only the families `.memory-tree.conf:42` declares
  (`tools/memory-tree/gen_build_index.py:806-818`). So an id in a family declared only inside a temporary repository
  joins nothing in the tree, and P0.6's predicate, which uses that grammar, prints nothing for it.
- P0.1's plants need real histories: rows 4 and 8, and the further arms. So does P0.2's range plant.
- The in-memory fixtures that P0.6 marked parse no H1, and keep their verdicts (the dispatch 234 evidence,
  `build/…-phase0-deviations-instruments.md:36-56`).

**Options.**
1. **(Recommended) A fixture family declared in the temporary repository's own conf.** It is used only by plants that
   write files.
2. `missing:` ids everywhere, with the plants skipping the readers that parse an H1. That loses the coverage of those
   readers.
3. Ids assembled at run time, so no literal appears in source. That hides an id from the very predicate P0.6 runs, so
   the guard no longer sees its class.

**Revised text**, appended to P0.1's opening paragraph (plan:134-137):

> A plant that needs a git history builds it in a temporary repository whose `.memory-tree.conf` declares one fixture
> family. Every fixture id there is `<that family>-<chain slug>-<n>`, so the fixture's H1 (`tree_lib.py:219`) and
> backlog rows (`row_grammar.py:211`) parse, while the tree's grammar, which matches only declared families
> (`gen_build_index.py:806-818`), joins none of them. The in-memory fixtures keep their `missing:` ids, since nothing
> parses them as ids.

### Finding 11: P0.7's bare-id check after the opening

> P0.7: the bare-id predicate will print the ids the opening mints, so "must print nothing" goes red as written.

**Verdict: CONFIRMED.**
- The predicate's own docstring says it: "Once the opening mints a build's roster and its ask, those ids are cited
  legitimately, and this predicate still reports every citation outside the generator's own skips"
  (`build/…-bare-ids.py:16-18`).
- The generator skips only a build's README for its own slug (`gen_build_index.py:800`). So each opened build's
  `BACKLOG.md` ask, each packet's roster rows (P0.3 field 9) and P0.8 row 1's citation of the extra unit all print.
- P0.7 runs the predicate on the committed opening and requires nothing printed (plan:535).

**Options.**
1. **(Recommended) Run the predicate at the opening commit's parent, and add an `--opened` mode for the opening
   itself.** The mode prints each chain-slug id the generator joins that the opening did not mint. That checks the
   true invariant: each build's joined ids are exactly the ids it minted.
2. Have the predicate skip minted ids by default. That blurs what it means before the opening (P0.6).
3. Drop the P0.7 check. That loses the guard.

**Revised text**, the P0.7 checks row (plan:535). The bare-id clause becomes:

> the generator-grammar bare-id predicate (P0.6) at the opening commit's parent, which must print nothing; and
> `bare-ids.py --opened` at the opening commit, which prints each chain-slug id the generator joins that is neither a
> `roster:units` id of its build's opened README nor that build's carry-forward ask, and must print nothing;

The red-tests row (plan:536) adds: "a bare chain id of an opened build planted in a record makes `--opened` print one
line".

### Finding 12: the report's blob line

> Row 10: "every report prints each instrument's blob hash" falls into `deviations.py --report`, which no brief
> assigns.

**Verdict: CONFIRMED.**
- Row 10's Fix says "Every report and packet prints each instrument's blob hash" (plan:150).
- Dispatch 234's brief excludes the row: "Rows 1, 2 and 10 are other units'" (`build/…-phase0-brief-deviations.md:39`).
- The packet brief takes only "P0.1 row 10's pin arm" (`build/…-phase0-brief-packet.md:12`).
- P0.2's list does not name the blob.

**Options.**
1. **(Recommended) P0.2's report prints the blobs in its head, and the deviations builder owns that.** A side effect
   is that an instrument edited between `--write` and `--check` goes red in the byte compare.
2. Narrow row 10 to packets. The report would then carry no trace of the instruments that produced it.

**Revised text.** In P0.1 row 10's Fix cell (plan:150), "Every report and packet prints" becomes "The departures report
(P0.2) and every packet (P0.3) print". The rest of the cell is unchanged.

Before P0.2's "What it lists" (plan:198):

> Its head names each instrument's blob at `HEAD`, `git rev-parse HEAD:<path>`, for `carries.py`, `deviations.py` and
> `asbuilt.py`, and for `packet.py` once it exists (P0.1 row 10).

P0.2's red tests (plan:228-245) add: "an instrument changed by one byte after `--write`: the byte compare goes red on
the head line".

### Finding 13: `asbuilt.py`'s baseline

> `asbuilt.py` reads its baseline unpinned, the same class as row 5.

**Verdict: CONFIRMED.** `asbuilt.py:130-136` reads `Baseline:` from v2's working tree and renders from whatever sha it
names, exactly as `deviations.py:132-136` does. Row 5 pins only `deviations.py` (plan:145).

**Options.**
1. **(Recommended) `asbuilt.py` reads the pin `deviations.py` carries.** It already imports that module
   (`asbuilt.py:35-37`), so the pin stays one fact in one file.
2. A second pin constant in `asbuilt.py`. That is two copies of one sha.

**Revised text**, a new P0.1 row after row 5 (plan:145):

> | The as-built view renders from v2's working-tree `Baseline:` too (`build/…-asbuilt.py:130-136`) | `asbuilt.py`
> renders from the pin `deviations.py` carries, which it already imports (`asbuilt.py:35-37`), and reports a
> differing `Baseline:` as a finding | Loosen `cl-dClosedLoop-0119`, re-point: `asbuilt.py --check` exits 1, and the
> view still renders from `59ff8f2ac` |

### Finding 14: the token arm and a `**Moved:**` carrier

> The token arm reads only the owner build's own specs, so a clause correctly moved by a `**Moved:**` line reds its
> token whenever its owner build is measured too, though the carrying spec holds the token.

**Verdict: CONFIRMED.**
- `carries.py:251` builds `texts` from the owner build's specs alone.
- `carries.py:259` joins only the carriers found in `texts`. So a carrier in another build's folder, admitted by a
  `**Moved:**` line (`:223`), adds nothing to the joined text.
- `real_specs` reads every chain build (`carries.py:124-133`), and `--build` filters only the findings, so the owner
  is measured whenever both builds have specs.
- The carries builder's probe saw it: "``dGroundRules: cl-dClosedLoop-0007's token `.governance/policy.toml` appears
  in none of its carriers``, though the dTrueNorth spec that carries the clause holds the token"
  (`build/…-phase0-carries-instruments.md:145-148`).

**Options.**
1. **(Recommended) The token arm reads every carrier's text, from whichever measured build's folder holds it.**
2. Skip the token arm for a moved clause. That loses the check the move must still pass.

**Revised text**, appended to P0.1 row 1's Fix and Plant cells (plan:141):

> **Fix, appended:** The token arm reads every carrier's text, from whichever measured build's folder holds it
> (`carries.py:251`, `:259` read only the owner build's).
>
> **Plant, appended:** A `**Moved:**` line naming the clause to this build, its token in the carrier, with the owner
> build measured too: green, red before. The same carrier without the token: red.

### Finding 15: the schedule script's row 9 note

> Row 9 of P0.4 differs: `run()` builds the "claim absent from that run, left unpinned" note and `main()` discards it
> (script lines 373-374), though the script's docstring says it is printed.

**Verdict: CONFIRMED.**
- `run()` appends "claimed on <node>, absent from this run: left unpinned" (`build/…-schedule.py:273`) and returns
  the notes (`:284`).
- `main()` binds them to `_` (`:373`) and prints the makespan alone (`:374`).
- The docstring promises the note is printed (`:27`), and P0.4 row 9 expects it (plan:321).
- The red-tests record measured the figure 273 and the node set a and d, with no note
  (`build/…-phase0-schedule-redtests.md:373-376`).

**Options.**
1. **(Recommended) Print the notes on the "a and d alone" line.** It is the only warning that a claimed run is missing
   from that figure.
2. Drop the note from row 9 and from the docstring.

**Revised text**, P0.4 row 9's Result cell (plan:321):

> "a and d alone" reads 273, the same as with no claim, from a and d only. The line carries the note that the claim
> is absent from that run and left unpinned, which the script's lines 373-374 print from the notes `run()` returns.
> Seen red on the script before this fold, which put the claim on a hidden pace-1 node and printed 216.

## [builder]

The revised acceptance for the deviations builder, in the order it would build. P0.6 is done (`60d041ba5`). Each item
names its observation and the command that makes it. Plant names are proposals, and the builder may rename them
through the naming lexicon.

The order follows dependency:
- The fixture repository comes first, because every plant that writes files runs inside it.
- The pin comes next, because every later plant measures against it.
- The population's readers follow, then its joins, then the policy over all of them.
- The report comes last, because it renders what the rest computes.

1. **The fixture repository** (finding 10). A helper builds a temporary git repository whose `.memory-tree.conf`
   declares one fixture family. A fixture spec's H1 parses there: `tree_lib.parse_spec_h1` returns its id. At the tip,
   `python -B build/…-bare-ids.py` exits 0 and prints nothing.
2. **The pin** (row 5; finding 13; finding 7 as [owner] Q1 answers). `deviations.py` holds `59ff8f2ac04a967751eae00de6856afbea66c033`,
   and `asbuilt.py` reads it from there.
   - `deviations.py --fixture --plant baseline`: exit 0 under `report`, with the moved baseline listed first; exit 1
     under `--policy refuse`.
   - `asbuilt.py --fixture --plant baseline`: exit 1, and the view renders from the pin.
3. **The pass reader** (row 3; finding 1). Under `--policy refuse`:
   - `--plant subject-pass` exits 1;
   - `--plant pass-none` and `--plant status-flip` each exit 0 with no member.

   A scratch probe imports the reader and runs it over dRenderedAnchor's seven specs. It prints the same seven first
   passes as the trailer-only reading, beginning `40d657e2e`, and 9 after-pass revisions.
4. **Not an ancestor of the pass** (row 4). `--plant two-branch` exits 1 under `refuse`.
5. **Header revisions** (row 8). `--plant header-rev` exits 0: a status-only commit, then a record at the header's
   `rev-1`.
6. **The Status-and-generated exception** (finding 2). `--plant gen` and `--plant status-gen` each exit 0, and
   `--plant gen-text` exits 1 under `refuse`. Over dRenderedAnchor, the step-3 probe prints 0 of the 9 as members.
   `grep -n GEN_REGION_AWK` on `deviations.py` shows the strip read from `tools/unattended/lib-unattended.sh`, not
   copied into the instrument.
7. **The ledger arm** (row 7; finding 4). `--plant quote` exits 0, `--plant amended` exits 1 under `refuse`, and
   `--plant amended-joined` exits 0. Every finding line names its address as `<unit>@rev-<N-1>`.
8. **The approver arm** (row 6; findings 8 and 9 as [owner] Q2 answers). These exit 1 under `refuse`, each against a
   fixture `DECISIONS.md`:
   - `--plant approver-none`
   - `--plant owner-bare`
   - `--plant owner-er`
   - `--plant owner-row5`
   - `--plant owner-row1-added`
   - `--plant owner-unknown-id`

   `--plant approver` exits 0, red before the fix. `grep -n "PLAY-dClosedLoop" build/…-deviations.py` prints only
   fixture lines.
9. **The further arms** (findings 3 and 5; the rescope addresses). These exit 1 under `refuse`:
   - `--plant add`, an add row with no record;
   - `--plant handback`, a hand-back with no record;
   - `--plant audit-pin`, an edit after a pinned audit.

   These exit 0 with no member:
   - `--plant defer`, a spec run's routine defer rows;
   - `--plant fix-record`, a `prompts/` record whose Goal is not `DIVERGENCE:`;
   - `--plant audit-nopin`, which also prints "no audit pin".
10. **The policy** (finding 7). Every plant in items 2 to 9 exits as stated there under `--policy refuse`. Under
    `report`, each exits 0 and lists its member. `--plant clause` exits 0 under `report` and 1 under `refuse`.
11. **Row 9's placement.** The docstring says the instruments run on the prepared merge, after `--prepare`.
    `grep -n -- "--prepare" build/…-deviations.py` shows it.
12. **The departures report** (P0.2; findings 6 and 12). `--report <slug> --fixture` lists each population plant of
    items 2 to 9.
    - Its head names each instrument's blob, and `git rev-parse HEAD:<path>` agrees.
    - The run-kind plants give `-departures-spec.md`, `-departures-build.md`, `-departures-build.md` and exit 2, as
      finding 6 states.
    - Every P0.2 red test gives its stated result, each arm-removed control green where the plan names one. That
      includes the new one: an instrument changed by one byte after `--write` makes the byte compare go red.
13. **The bare-id predicate's opened mode** (finding 11). In a scratch clone, one chain README is opened with
    `roster:units` rows and an ask, then `gen_build_index.py --write` runs.
    - `bare-ids.py --opened` exits 0 and prints nothing.
    - A bare id of that build planted in a record prints one line.
    - A roster id cited in a record but removed from `roster:units` prints one line.
14. **Today's tree.** `deviations.py` exits 0 with 0 members, and `asbuilt.py --check` exits 0.
15. **The evidence.** Every command above, with its exit code and the line that proves it, before and after each fix,
    is listed in the build's evidence record, as `build/…-phase0-deviations-instruments.md` holds P0.6's.

**Not this builder's.**
- Finding 14 reopens `carries.py` row 1, which is the carries builder's (`07942b449`).
- Finding 15 is the schedule script's two-line print, after which P0.4's rows are re-run.
- Finding 11's P0.7 rows, and finding 9's P0.8 sentence, go to the main loop.
- Row 10's packet half is already in the packet brief (`build/…-phase0-brief-packet.md:12`).
