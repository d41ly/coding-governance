# TOOL-aBoundedVerdict-2 — a halted run records WHY, in a vocabulary something reads

**Status:** SPECCED · rev-4 · 2026-08-17 · node a · Tier-2 · base febba16b · streams tooling

## 1. Goal

A run that cannot finish reaches exactly one non-landing terminal, and that terminal carries no
machine-legible reason: the free-text abort reason is parsed by nothing, and the kind field the
helper already writes is read by nothing. Give the abort verb a required halt code over a kit-owned
vocabulary, and give that vocabulary readers, so an owner returning to a stopped run learns why it
stopped without reading prose.

## 2. Scope (IN)

- **S1** — a kit-owned core halt vocabulary in the driver, one member per halt site this build's
  research actually enumerated, and no member invented for symmetry: the review budget was exhausted
  with the unit not clean; a fork survived the method's vetoes with no resolution the mandate
  delegates; a unit awaits owner scope approval the mandate does not supply; a unit is blocked on an
  EXTERNAL PREREQUISITE, which is a different owner turn from an unapproved scope and is the case
  `TOOL-aBoundedVerdict-3` S1 routes here; a unit's acceptance or gates could not be derived; the
  repository state at start was outside what the mandate reaches; a gate is red and its fix lies
  outside the mandate's scope.
- **S2** — `--abort <slug> --reason <text> --code <CODE>`, with the code REQUIRED and validated
  against the effective vocabulary. An unlisted code is refused naming the legal set.
- **S3** — the code is recorded as an AUTHORED FACT through the existing fact writer, not buried in
  the reason prose, so a reader is a field read rather than a parse. It is therefore the region's
  NINTH fact, and S7 moves the pin that says eight rather than leaving the spec silently in breach
  of it. The justification is the protocol's own membership test — nothing in the tree derives the
  code, and only the run knows it — and the shape: a halt code is a per-run SINGLETON that three
  readers read by key, which is what a fact is for. **The in-tree precedent is now exact**: the
  eighth fact, the roster frozen at landing, is a singleton written by a TERMINAL verb, which is the
  same shape this code has. A tracked sibling spec declined what is now a ninth fact and added a park
  KIND instead, and that remains the right answer for append-only history; it is the wrong answer for
  a singleton nobody would grep a region to recount. `TOOL-aBoundedVerdict-1`
  takes the park-kind route for exactly that reason, so this build uses both shapes deliberately and
  moves the pin exactly once.
- **S4** — two new `.unattended.conf` keys, spelled here rather than described, in the shape the
  existing `PHASES_EXTRA` / `DOD_EXTRA` / `CORE_FLOOR` trio already sets:
  - `HALT_CODES_EXTRA` — OPTIONAL, empty legal, the project's appended members.
  - `HALT_FLOOR` — REQUIRED, a single integer, the shrink-only size of the kit's core set. Undeclared
    or malformed is a refusal, not a defaulted value, matching how the existing floor key behaves.

  Both are added to the adopter's seed conf as well as this repo's, because the seed is what a real
  adopter copies and a gate-required key missing from it reds the unattended leg's first check on
  install with no gate here noticing. Rev-2 asserted both were named and named neither, which is the
  defect round 1 raised, restated rather than fixed.
- **S5** — three readers, because a vocabulary with no reader is decoration and this kit says so
  about its own phase writer: `--status` names the code on its single line; `--resume` names it and
  states that the run is finished rather than resumable; and a new leg check asserts that every
  tracked run-state file whose phase is the aborted terminal carries a code in the effective
  vocabulary.
- **S6** — the wrap-up gains the code, so the one turn the owner gets opens with why the run stopped.
  It lands in the PROTOCOL's wrap-up rows, which are already in this unit's write set, and NOT in the
  build method's derivation table — F3 recommends leaving the method alone on its own pointer rule,
  and rev-2 pre-applied that recommendation to the files list while leaving the scope item pointing
  at the method. If F3 is resolved the other way, `memory/guides/BUILD-METHOD.md` and its kit
  template join Files touched, and the manifest re-stamp and read-path clauses apply with them.
- **S7** — the EIGHT-FACT PIN moves to nine, in every place it is spelled, because it has now moved
  THREE times and left a stale reader every time — the third move landed while this spec was open,
  which is the argument for enumerating the sites rather than trusting a builder to find them. The
  three carriers now disagree three ways, and each needs its own edit:
  - the "exactly eight facts and nothing else" sentence in `tools/unattended/PROTOCOL.template.md`
    and the installed `memory/guides/UNATTENDED-PROTOCOL.md` — currently correct at eight, moving to
    nine — plus the closed enumeration beneath it, which gains the code as its NINTH entry;
  - the driver comment in `unattended.sh`'s resume path, which says the region carries FIVE and has
    been stale across two moves;
  - **BOTH** count statements in `memory/map/features/unattended.md`, which say SEVEN — one as a bare
    numeral before "of them", one before "facts".

  Nothing counts the facts, so no leg catches a missed one. Read the current value from the protocol
  at build time rather than from this bullet: it was seven when this spec was drafted.
- **S8** — the protocol's phase and verb sections, the conf's key table, the adopter's seed conf, the
  rendered Skill, and the kit version constants.
- **S9** — the three documented CALL SITES of the abort verb gain the new required argument, and one
  arm asserts they cannot silently stop carrying it. No existing gate joins a documented invocation
  to the driver's argument set — the adopter check, the protocol parity check and the kickoff-engine
  check are all copy-parity or literal-string tests — so without this the full bar stays green while
  every documented invocation is missing a required argument.

## 3. Non-goals (OUT)

- **No new phase member, terminal or otherwise, and no move of the core phase floor or the terminal
  set.** This is the unit's central design decision and the owner ratified it against the
  measurements. A phase added to the core set is refused by the driver's own guard with a message
  naming two verbs that cannot write it; added as non-terminal it wedges the next run's preflight
  forever; and the protocol's phase list is joined to the driver's by no gate, so either drifts
  silently.
- No code on the landed terminal. A landing needs no reason.
- No code on a park. Parking is unit 5's mechanism and a park is not a halt.
- No retrofit of existing terminal records BEYOND the one §4 enumerates. Exactly one tracked record
  claims the aborted terminal without a code, it is named, and it is migrated by this unit's commit.
  A blanket no-retrofit rule was the rev-3 position and rested on a population that was zero at the
  old base and is not at this one.
- No claim that the code is trustworthy. The run writes it, as it writes every other authored fact,
  and the protocol's boundary section already states what that is worth.

## 4. Design

### Data model

The vocabulary is a driver constant, read by the leg the same way the leg already reads the core
phase and Definition-of-Done sets from the driver rather than restating them. The effective set is
the core set plus the project's declared extras, composed the way the phase set already is.

The size pin gets its own conf key rather than a third field on the existing floor. The rationale
rev-1 gave for that — that a three-field value is dropped in silence — is FALSE and was refuted
against source: the existing key's parser matches a three-field value on its reject arm first and
fires a named refusal saying it wants two integers separated by a colon, a guard added precisely
because a malformed value once disarmed both pins. The decision survives on the grounds that
actually hold: the floor key is a two-field contract whose malformed-value guard is written for
exactly two fields, so widening it means editing that guard and its arm, while a separate key costs
one conf line, one entry in the leg's required-key loop, and no change to a working refusal.

| Fact | Written by | Read by |
|---|---|---|
| the phase | the terminal producers | every in-kit reader, all on the terminal binary |
| the halt code | the abort verb | `--status`, `--resume`, the new leg check, the wrap-up |
| the free-text reason | the abort verb, through the park helper | a human, and the bypass-flag grep |

The three coexist deliberately. The code is for a machine and for a glance; the reason is for the
owner and stays free text, because a code set that tried to carry the specifics would grow without
bound.

### Inventory

Each core member exists because the research found a real site that reaches it, and each names the
owner turn it needs:

| Code | Reached from | The owner turn it names |
|---|---|---|
| review budget exhausted | unit 1's cap refusal | the unit's design is not converging; re-scope or split it |
| fork unresolvable | the method's vetoes 2 and 3, and a scope fork | decide the fork |
| awaiting scope approval | a unit at the awaiting-approval status that is NEITHER reachable at the pinned base NOR authored by this run — the residual `TOOL-aBoundedVerdict-3` S1's three cases do not cover, reached when a spec arrives on the run's own branch from elsewhere | approve or amend the scope |
| blocked on an external prerequisite | a unit whose status names a prerequisite outside the run | clear the prerequisite |
| acceptance underivable | the kickoff engine's fifth interactive exit | supply the acceptance check, or split the unit |
| precondition unmet | the kickoff engine's first three interactive exits | repair the repository state |
| gate red out of scope | a red gate whose fix the mandate does not reach | authorise the fix, or widen the mandate |

The mapping is the unit's real content. A code set that did not correspond one-to-one with the
enumerated exits would be a vocabulary invented ahead of its callers, which is what the phase
vocabulary already is.

### Migration

**The population is ONE, named, and it must be retrofitted — re-measured at the merge base.** There
are four tracked run-state files. Three claim the LANDED terminal; `memory/builds/dClosedLexicon/RUN.md`
claims ABORTED and carries no code. Rev-2 said the population was zero, which was true at the old
base and false at this one: that record landed while this spec was open.

So AC4's leg check has a live subject and would red the merge bar the day it lands. The disposition
is a RETROFIT of that one record, enumerated here rather than waived:

- The code is `fork unresolvable`, and it is read from the record rather than invented. Its own
  parked text says the two candidate resolutions are not resolver calls "under a mandate that does
  not delegate scope" and that its unit is BLOCKED — which is that member's definition.
- It is a DATA migration performed by this unit's commit, not a driver verb. The driver refuses to
  move a terminal record on purpose, and nothing here changes that refusal.
- One record, named in Files touched. No waiver registry, no cutoff, no enumeration file: a
  one-row registry would need a path, a grammar and a reader, which is more machinery than the row
  it holds.

**Re-measure before building.** The population moves every time a run aborts, and it moved once
already inside this build. The count is not carried out of this paragraph.

The corpus therefore DOES exercise the new check, which is better than rev-2's position: the red arm
has a live subject as well as fixtures in `tools/unattended/check-unattended.test.sh`, rather than
fixtures alone.

### Rollout

The verb's new required argument is a breaking change for every caller, and rev-1's claim that the
existing gates enforce the update was verified FALSE. There are three documented call sites, not
two: the Skill template and its render, the protocol template and its installed copy, and the
kickoff engine. Every gate over them is a copy-parity or literal-string test — the adopter check
compares the render against its template and conf, the leg compares the shipped protocol against the
installed one, and the kickoff check asserts two literal strings and an exit count. **No gate joins a
documented invocation to the driver's argument set.** So all three could keep omitting the argument
with the full bar green, and the first unattended run to follow the Skill would meet a refusal on
the one exit that exists for a run which cannot proceed.

S9 is the rollout, and it has teeth: the three sites are an explicit scope item, and a source-level
arm asserts that every tracked file spelling the abort invocation also spells the code argument.

### The kickoff engine's size budget

S9 edits `skills/session-kickoff/SKILL.md`, which rides a HARD gate leg no other unit in this build
touches and which this spec's §7 did not name. The file is 18215 bytes against an 18432 ceiling —
217 under, at 98.8% — and the edit is the code argument on the one abort line plus a code named on
each code-bearing exit, measured at 102 bytes against a scratch copy, landing at 18317 with 115 to
spare. **It fits, and the finding is that nothing in the spec knew the margin existed.**

The INVOCATION moved at the merge base and the spec must not carry the old one: the ceiling is no
longer a positional. `tools/gate-legs.json`'s argv is now `bash tools/check-template-size.sh
skills/session-kickoff/SKILL.md` with no number, and the limit is DECLARED in the new
`tools/template-size-limits.txt`. So a unit growing that file spends against a declared limit rather
than one spelled in a leg, and the builder re-measures through the leg's own argv rather than
through either number here.

### Alternatives rejected

- **A new terminal phase plus a producer verb.** What the owner first asked for. Measured cost: each
  new terminal needs its own producer, each producer's refusal branch needs an armed assertion in a
  leg that took eighteen minutes to run on the probe host, the core floor moves, and the protocol's
  prose phase list drifts from the driver's with no gate joining them. Rejected by the owner on those
  measurements.
- **A non-terminal halt phase.** Writable today with a three-line diff, and it wedges the fleet: the
  record counts as live forever, so the next run's preflight is hard-blocked and resume tells every
  future session to carry on. Reproduced.
- **A reason-code convention with no validation.** Costs nothing — appending one to a real tracked
  run-state file leaves both gates green, which is exactly the problem. A convention nothing checks
  is a convention that is followed until the first hurry.
- **Reusing the park helper's kind field as the vocabulary.** Tempting: the field exists and is
  already distinct per call site. Rejected because the kind describes the LINE's grammar, not the
  run's disposition, and overloading it would put two meanings on the field whose single meaning was
  itself the product of a review finding.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the vocabulary, the verb, and the stale five-fact comment in the
resume path) · `tools/unattended/check-unattended.sh` and its sibling ·
`tools/unattended/unattended.test.sh` · `.unattended.conf` ·
`tools/unattended/.unattended.conf.example` — the seed a real adopter copies, which nothing
validates against the required-key set · `tools/unattended/kit.toml` ·
`tools/unattended/PROTOCOL.template.md` and the installed protocol (the verb section, the phase
section, and the seven-fact pin with its enumeration) · `tools/unattended/SKILL.template.md` and the
rendered Skill · `skills/session-kickoff/SKILL.md` (the exits' abort disposition names the code) ·
`memory/builds/dClosedLexicon/RUN.md` — the ONE tracked record §4's migration retrofits ·
`memory/map/features/unattended.md` (BOTH fact counts) · `tools/unattended/check-unattended.sh`'s
header check COUNT and the matching count in `AGENTS.md`'s gate-suite bullet, which S5 moves by one
and which no gate observes — `TOOL-aBoundedVerdict-1` moves it again, so the two units state their
moves one apart rather than both writing the same number ·
`memory/guides/SESSION-KICKOFF.md` (the manifest re-stamp; `.unattended.conf` and the kickoff engine
are both on its watch list) · the kit version constants.

## 5. Production-readiness checklist

- security — N/A as a surface, but the code is a run-authored field and the spec says so where a
  reader could otherwise mistake it for evidence.
- perf / scale — N/A. One extra field read per record per leg run.
- a11y — N/A.
- i18n — the codes are identifiers, not prose, and are not translated.
- error / empty / loading states — an undeclared extras key, an empty effective set, an unlisted
  code, and a missing code are four distinct refusals. An empty effective vocabulary must refuse
  rather than accept everything, on the same rule the phase set already follows.
- observability — S5 is the whole point of the unit; without a reader this is the decoration the
  protocol warns about, and §3 says so.
- risks — the real risk is vocabulary rot: a code nobody can reach, or a halt with no code that
  fits. §8 carries both as forks.
- testing + left-shift gates — the leg check plus an arm per refusal branch. The left-shift for the
  wrong-lever risk is the one-to-one mapping table in §4: a future code with no enumerated site is
  visibly a new row with an empty middle column.
- migration / rollback — §4's migration paragraph; rollback removes the required argument, and
  records written with a code stay readable because the field is additive.
- user docs — the protocol's verb and conf tables, and the rendered Skill.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --abort <slug> --reason r` runs with no code,
  it refuses naming the legal set, and the record is unchanged. Asserted on the on-disk effect.
- **AC2** — When the code is outside the effective vocabulary, the verb refuses; when it is a
  project extra declared in `.unattended.conf`, it is accepted. Both arms in
  `tools/unattended/unattended.test.sh`.
- **AC3** — When a run aborts with a code, `bash tools/unattended/unattended.sh --status <slug>` and
  `--resume <slug>` both name it, and resume states the run is finished rather than resumable.
- **AC4** — When a tracked run-state file claims the aborted terminal and carries no code fact,
  `bash tools/unattended/check-unattended.sh` reds naming the file. No exemption clause and no
  waiver: the one tracked record in that state is migrated by this unit, so the check is green over
  the real tree on the day it lands, and both arms also live in
  `tools/unattended/check-unattended.test.sh` fixtures.
- **AC4a** — When `memory/builds/dClosedLexicon/RUN.md` is read after the migration, it carries the
  `fork unresolvable` code, and `bash tools/unattended/check-unattended.sh` is green over the whole
  tracked population re-measured at build time rather than at the count this spec states.
- **AC5** — When the core vocabulary shrinks below its declared floor,
  `bash tools/unattended/check-unattended.sh` reds; when the floor key is absent or malformed, it
  refuses rather than passing with the pin disarmed.
- **AC6** — When the leg reads the vocabulary, it reads it from the driver, asserted as the
  COMPLEMENT rather than as a prefix grep: the leg's only reference to the vocabulary is the
  `core_of` helper call taking the key as its argument, and no member token appears in
  `tools/unattended/check-unattended.sh` under a word-anchored grep of the members themselves. The
  prefix alternation rev-1 proposed cannot distinguish a member from an unrelated identifier, and
  `TOOL-aBoundedVerdict-1` lands a constant whose name that alternation would have matched.
- **AC7** — When every tracked file spelling the abort invocation is greped, each also spells the
  code argument — all three documented call sites — and the arm that asserts it lives in
  `tools/unattended/unattended.test.sh`.
- **AC8** — When the region's fact count is greped across the FIVE statements it is spelled in, none
  states a stale count. The pattern is NUMBER-AGNOSTIC, not an alternation of the values that happen
  to be stale today —
  `grep -rniE '(one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+)[[:space:]]+(facts|of them)' tools/unattended/ memory/guides/ memory/map/`
  returns only statements naming the current count. Rev-3's two-value alternation would have returned
  nothing while two carriers still said `eight`, because the pin moved after it was written — the
  criterion failing in exactly the way it exists to prevent, one word later. The pin has moved three
  times and a value-listing pattern has been wrong at every move.
- **AC9** — When `skills/session-kickoff/SKILL.md` is edited,
  `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` is green — no positional; the
  ceiling is declared in `tools/template-size-limits.txt` — re-measured rather than assumed.
- **AC10** — When the Skill and protocol are re-rendered,
  `bash tools/unattended/adopt-unattended.sh --check` reports in sync with no surviving placeholder
  shape, and `bash tools/check-kit-versions.sh` is green with both unattended constants moved.
- **AC11** — When any NEW `fail` branch exists, it is armed in that gate's sibling test or pinned in
  `memory/project/unarmed-branches.txt` with its reason, and `python tools/memory-tree/check-arms.py
  --check` exits 0. `ARMS_FLOORS` moves only where `--report` shows the measured counts grew.
- **AC12** — `GATE_FULL=1 bash tools/run-gates.sh` is green.

## 7. Gates

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/adopt-unattended.sh --check` ·
`tools/unattended/adopt-unattended.test.sh` · `tools/check-kit-versions.sh` ·
`tools/check-template-size.sh skills/session-kickoff/SKILL.md` — the hard leg on the kickoff engine,
at 98.8% of the ceiling declared in `tools/template-size-limits.txt` · `skills/session-kickoff/manifest-check.sh` ·
`tools/memory-tree/check-memory-hygiene.sh` — this unit edits two files under the memory root and
grows a read-path member, and rev-2's gate list omitted it ·
`python tools/memory-tree/corpus_ids.py --report` for the read-path share ·
`python tools/memory-tree/check-arms.py` · `tools/memory-tree/kit-dogfood-parity.test.sh` ·
`python tools/codebase-map/test_codebase_map.py` · `python tools/drift-audit/drift_report.py
--check` · `bash tools/run-gates.sh`.

## 8. Open questions

- **F1 — what does a run do when no code fits?** Options: add a catch-all member, which is a hole
  that will swallow the vocabulary within a few runs; require the project to declare an extra, which
  stalls a run at the moment it is trying to stop; or refuse to abort, which is the worst of the
  three. Recommendation: no catch-all, and the unclassifiable case aborts under the closest code with
  the specifics in the free-text reason — with the mismatch itself worth a backlog row when it
  happens.
- **F2 — does the leg assert the code is REACHABLE, not merely legal?** A member no verb can produce
  is the phase vocabulary's disease. A reachability assertion would grep the callers for each member.
  Recommendation: not in this unit. The one-to-one table in §4 is the human-readable form of the same
  claim, and a grep-based reachability check over prose callers is the kind of predicate this repo
  has found vacuous twice.
- **F3 — does the wrap-up row in the build method make this a cross-kit change?** The wrap-up
  derivation lives in the memory-tree kit's rendered method document, so S6 moves a memory-tree
  carrier for an unattended-kit reason. Options: put the row there anyway, since the method already
  points at the unattended protocol for exactly this kind of fact; or leave the method alone and let
  the code reach the owner through the protocol only. Recommendation: leave the method alone —
  its own rule is that a fact stated in it and in a carrier it points at is a defect in it.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. Records that the owner ratified the code-over-phase decision
  against the measured cost of both, so §3's central non-goal is a decision and not an omission.
- rev-2 · 2026-08-16 · folded the M4 spec audit's first round. The set-level blocker: the code is an
  EIGHTH authored fact in a region the binding protocol pins at seven, which rev-1 neither named nor
  moved while a tracked sibling spec answered the identical question the other way by name. S3 now
  argues the fact shape on the protocol's own membership test and on the singleton-versus-history
  distinction, and S7 moves the pin in all four places it is spelled — including a driver comment
  that was already stale at five. The rollout claimed two callers under enforcing gates; there are
  three and no gate joins any of them to the argument set, so S9 and AC7 replace the claim. Added
  the seventh member for a unit blocked on an external prerequisite, which
  `TOOL-aBoundedVerdict-3` routes here and the six-member set excluded. Added the kickoff engine's
  measured size budget and its hard gate leg, the adopter's seed conf, the map dossier's fact count,
  and the manifest re-stamp. The floor-key rationale rested on a false claim about the existing
  parser and is restated on grounds that hold. AC6's prefix grep would have broken under the unit
  that lands after this one and is replaced by the complement assertion.
- rev-3 · 2026-08-16 · folded round 2. S4 asserted "Both keys are NAMED in the design" and named
  neither — round 1's finding restated rather than fixed — so both are now spelled, with which is
  required and which optional. The migration's exemption, its registry and its enumeration all
  answered a question the tree does not ask: the measured population of codeless aborted records is
  ZERO, both tracked run-state files being landed, and the recording the enumeration would have gone
  into is read by no gate. The pin's dossier statement is TWO statements, not one, and the completeness
  grep as written misses the bare-numeral form. The wrap-up scope item still pointed at the build
  method after the files list had already dropped it on this spec's own recommendation; it now lands
  in the protocol and says what changes if the fork resolves the other way. The awaiting-approval
  member had lost its last routing site to the stall unit's three cases and is narrowed to the
  residual they leave. Added the hygiene gate and the read-path reporter to §7, and the leg's own
  check count to Files touched, sequenced against the other unit that moves it.

- rev-4 · 2026-08-17 · M7 REGROUND onto the new merge base, and the most affected spec. BLOCKER: the
  migration said the population of codeless aborted records was zero; at the new base it is ONE, a
  named tracked record that this unit's own leg check would have redded the bar on at landing — it is
  now a stated one-record retrofit rather than a claim of nothing to do. The authored-region pin moved
  from seven to eight under the spec, so the halt code is the NINTH fact, not the eighth, and the
  in-tree precedent is now exact: the eighth fact is a singleton written by a terminal verb. The
  completeness grep is rewritten NUMBER-AGNOSTIC — the two-value alternation would have returned
  nothing while two carriers still said eight, the criterion failing exactly as it exists to prevent.
  The kickoff size leg lost its positional; the ceiling now lives in a declared limits file.
## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "terminal phase for a run that cannot continue"` returns
the unattended conf and the driver and no third seam, which is consistent with the research finding
that no reader of the phase exists outside the kit. Three existing seams are extended rather than
duplicated: the driver-side core-set constant with the leg reading it through the same helper that
already reads the phase and Definition-of-Done sets; the authored-fact writer, unchanged; and the
conf's required-key loop. The one seam deliberately NOT reused is the existing two-field size floor,
for the parse reason §4 gives.

Recall terms used, recorded for the reground: halt code abort terminal phase vocabulary shrink-only
floor run-state authored fact status resume reader unattended driver conf declaration.
