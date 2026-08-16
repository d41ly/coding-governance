# TOOL-aBoundedVerdict-5 — parking becomes a verb instead of a hand-edit

**Status:** OPEN · rev-3 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

The build method names parking as the substitute for asking an absent owner and demands the
question, the options seen and the reason be written into the run's authored record — but the driver
exposes no verb that writes one. `park()` exists with exactly two callers, both internal to other
verbs, so a run following the method must hand-edit the authored region of a file the kit calls
generated and whose grammar the driver owns. Give parking a verb.

## 2. Scope (IN)

- **S1** — `unattended.sh --park <slug> --question <text> --options <text> --reason <text>`, routing
  through the existing `park()` helper with a `park` kind, and staging the file as every other
  writer does.
- **S2** — all three fields are required. A park missing any one of them is refused, because the
  method's own words are that a bare park is indistinguishable from a forgotten one, and the driver
  is the only place that distinction can be enforced.
- **S3** — the same bypass-flag refusal the abort verb already carries applies to all three fields.
  The gate greps the run-state file whole for the declared flag, so a truthful park text naming it
  would red the bar permanently on a record no verb can rewrite.
- **S4** — `--park` refuses a terminal record, through the single existing refusal rather than a
  fourth copy of that rule.
- **S5** — `--status` reports the DECISION-kind parked count alongside the phase, so a run that
  parked everything and reached the close is visible without reading the file. Decisions only, and
  the same qualifier as S6: a status line inflated by review rounds would report the opposite of what
  it is for.
- **S6** — the Definition-of-Done item asserting that parked decisions reached the wrap-up gains a
  countable observable. The attestation's VALUE carries the number surfaced, and the close verb
  refuses when that integer does not equal the number of **DECISION-kind** parked lines in the
  record. The qualifier is load-bearing and is spelled in every place the count appears — S5's status
  line, the inventory row and the acceptance criteria — because `TOOL-aBoundedVerdict-1` adds a
  `record`-kind line that must not be counted, and an unqualified count is the exact failure S7
  exists to prevent. The item stays agent-attested — a machine cannot observe a wrap-up — but "I
  surfaced them" becomes "I surfaced four decisions, and the record holds four". Three constraints
  bound the shape:
  - It extends the existing key's value rather than adding a field. The current predicate matches the
    key with a yes-or-true value and tolerates trailing text, so a richer value costs no new authored
    fact and does not touch the region's seven-fact pin.
  - **The refusal lives in the close verb ONLY.** The evaluator is shared: the abort verb calls it for
    the same item, and the abort verb writes its own parked line. A refusal in the shared helper would
    block the exit that exists for a run which cannot proceed, which is the hazard the driver's own
    comment warns about by name. The abort path keeps the existing attestation test unchanged.
  - **The close verb's OWN override park is excluded from the count.** Measured: the Definition-of-Done
    loop evaluates the attestation, and only afterwards does the verb append its override line. So a
    close carrying an override validates against N and leaves N+1 on disk, and a count that included
    it could never be satisfied. The exclusion is stated here and armed by an acceptance fixture
    carrying an override, because the arm that does not carry one passes either way.
- **S7** — the parked region's KINDS become a declared two-class taxonomy, because this unit is the
  first to need the distinction and `TOOL-aBoundedVerdict-1` depends on it. A **decision** kind is
  one the owner must be shown — the existing abort and override kinds, and this unit's park. A
  **record** kind is history the owner need not adjudicate, of which `TOOL-aBoundedVerdict-1`'s
  review round is the first. S6's count ranges over DECISION kinds only. Without this, a build's
  review rounds would inflate the count of decisions a run must surface, and the two units would
  disagree about what a parked line is.
- **S7a** — the DECISION set is a driver constant beside the existing core phase and
  Definition-of-Done sets, read by the leg through the same helper that already reads those. A
  taxonomy declared only in prose has no machine home, no shrink-only pin and nothing to read it —
  which is the decoration this kit already names as a defect in its own phase writer, and which the
  vocabulary unit avoids by giving its codes all three.
- **S7b** — the taxonomy is ARMED, and the arm must be able to fail. At this unit's landing every
  existing kind is a decision kind, so an implementation that counts every parked line satisfies any
  fixture built only from today's kinds. The acceptance fixture therefore carries a `record`-kind
  line explicitly, and `TOOL-aBoundedVerdict-1` carries the mirror case, so the interface is armed on
  both sides of the gap between the two units.
- **S7c** — the method's wrap-up derivation row is NOT this unit's, and rev-2 wrongly implied it was.
  That row says every parked entry with its question, options and reason — a shape a review line does
  not carry — and narrowing it is `TOOL-aBoundedVerdict-1`'s, which already has the method in its
  write set and lands after this unit's taxonomy exists. This spec's §3 keeps method rules out of
  scope and now says which unit owns the consequence.
- **S8** — the protocol's verb section and the parked-decisions rows gain the verb and the taxonomy,
  and the rendered Skill gains the call.

## 3. Non-goals (OUT)

- No change to what parking MEANS, to when a run must park, or to which situations park rather than
  abort. Those rules live in the build method and the kickoff engine and this unit does not move
  them. Unit 3 is where a new disposition is written.
- No unpark. A parked entry is a record for the owner's turn, not a queue the run drains, and a verb
  that removed one would let a run erase the only turn the owner gets.
- No machine verdict on whether a park is a good park. The three fields are checked for presence,
  not for quality.
- No change to the spill rule for the authored region's size budget. The verb makes parks more
  likely, which makes the spill more likely to matter — that is a real consequence and it gets a
  backlog row rather than a scope item, because the rule already exists and is already gated.

## 4. Design

### Data model

`park()` appends one line carrying a timestamp, a kind, an item and a reason. The verb supplies
`park` as the kind, uses the question as the item, and composes the reason field from the options
and the reason so the three facts land on one line without changing the helper's signature. The
helper's own history is the argument for not changing it: the kind became an argument precisely
because a single hardcoded grammar made an abort arrive wearing the label of an override that never
happened.

The authored region's anchor ban binds here. A parked line must not lead with a dash or a pipe
followed by an id, because that would anchor the id under this build folder and make the build a
claimant of it — and a park naming a unit elsewhere is exactly the shape that collides. The existing
helper's output already leads with a timestamp, so the ban is satisfied by construction and the
verb must not reformat it.

### Inventory

| Concern | Today | After |
|---|---|---|
| writing a park | hand-edit of the authored region | `--park` |
| callers of `park()` | the abort verb and the close verb's override | those two plus `--park` |
| a park's required fields | none — the method asks in prose | three, refused by the driver |
| seeing that a run parked | read the file | `--status` reports the count |
| the attested Definition-of-Done item | a grep for a line the run writes about itself | the same grep, plus a close-verb refusal when the attested COUNT does not equal the DECISION-kind parked-line count, excluding the verb's own override line |

S6 is the part worth stating plainly: it does not make the item machine-checked. It narrows one
specific dishonesty — a record with parked entries and an attestation that does not account for them
— and leaves the general case exactly as attested as it was, since the run authors both numbers. The
protocol's own boundary section is the model for saying so.

### Alternatives rejected

- **Leave it a hand-edit and document the format.** This is today's state plus prose. The authored
  region's grammar is the driver's, the file is staged by the driver, and a documented hand-edit is a
  second writer of one grammar. Rejected on the two-answers-to-one-question class.
- **Fold `--park` into the abort verb as a non-terminal mode.** Rejected: an abort is terminal by
  definition and a mode flag that makes a terminal verb non-terminal is the shape the kit already
  refused once when it separated the phase writer from the terminal producers.
- **Make the parked-decisions item fully machine-checked.** There is nothing to check it against. The
  wrap-up is a chat turn, and no artifact records that the owner read one. Rejected as unbuildable,
  which is a better answer than a check that reads a line the run writes about itself and calls it a
  verdict.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.test.sh` · `tools/unattended/PROTOCOL.template.md` and the
installed protocol · `tools/unattended/SKILL.template.md` and the rendered Skill ·
`.memory-tree.conf` (the arms floor for the driver) · `memory/guides/SESSION-KICKOFF.md` (the
manifest re-stamp; `.unattended.conf` and the conf are on its watch list) · the kit version
constants. The decision-set constant lands in the driver beside the existing core sets, so S7a adds
no file of its own.

## 5. Production-readiness checklist

- security — the three fields are free text appended to a tracked file the gate greps whole. S3 is
  the guard, and it is the same guard the abort reason already carries, for the same measured reason.
- perf / scale — N/A. One append per call.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a park on a slug with no run-state file, a park with an empty
  field, and a park on a terminal record are three distinct refusals with three distinct messages.
- observability — S5 is the observability, and it is the reason S5 is in scope rather than deferred:
  a verb whose output nothing reports is the decoration the protocol already warns about.
- risks — the authored region grows. The size cap and its spill rule already exist and are already
  gated, so the risk is that the spill becomes load-bearing rather than theoretical. Named in §3.
- testing + left-shift gates — every refusal branch gets an arm in the driver's sibling test, and
  the arms floor moves in the same commit.
- migration / rollback — no migration; existing run-state files are unaffected. Rollback is removing
  the verb, and a record written by it stays readable because the line grammar is unchanged.
- user docs — the protocol's verb table and the rendered Skill, both under parity gates.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --park <slug> --question q --options o
  --reason r` runs against a live run, one parked line is appended and the file is staged; arm in
  `tools/unattended/unattended.test.sh`.
- **AC2** — When any one of the three fields is missing,
  `bash tools/unattended/unattended.sh --park <slug> --question q --reason r` refuses naming the
  missing field, and the file is unchanged. Asserted on the on-disk effect, not the exit code alone.
- **AC3** — When a field spells the declared bypass flag, the verb refuses before writing, and
  `bash tools/unattended/check-unattended.sh` is green afterwards — the arm proves the refusal
  prevented the wedge rather than merely reporting it.
- **AC4** — When the record is terminal, `--park` refuses through the shared refusal. The verb is
  ADDED to the finished-record drive list in `tools/unattended/unattended.test.sh`, reusing that
  arm's existing fixture; the arm's derived phase-writer count stays at five, because the park verb
  writes no phase.
- **AC5** — When a run has parked entries, `bash tools/unattended/unattended.sh --status <slug>`
  names the DECISION-kind count on its single line, and a fixture carrying a `record`-kind line
  proves the line is excluded.
- **AC6** — When a record carries four decision-kind parked lines AND two record-kind lines and the
  attestation counts three, `bash tools/unattended/unattended.sh --close <slug>` refuses naming the
  attested item, the record key and both integers; when it counts four, the close proceeds. The
  fixture's record-kind lines are what make the arm fail under a count of all parked lines, so it
  tests the taxonomy rather than a total.
- **AC6a** — When the same close carries `--override`, it still proceeds at an attestation of four,
  proving the verb's own override line is excluded — the arm that omits the override passes either
  way and therefore proves nothing.
- **AC6b** — When the same over-counted record is ABORTED rather than closed,
  `bash tools/unattended/unattended.sh --abort <slug> --reason r` fires no such refusal, proving the
  close-verb-only placement rather than asserting it.
- **AC6c** — When the decision set is read, the leg reads it from the driver through the same helper
  that already reads the core phase and Definition-of-Done sets, and no class member is spelled in
  `tools/unattended/check-unattended.sh`.
- **AC7** — When the Skill is re-rendered, `bash tools/unattended/adopt-unattended.sh --check`
  reports in sync and the render carries no surviving placeholder shape.
- **AC8** — `python tools/memory-tree/check-arms.py --check` exits 0 with the driver's `ARMS_FLOORS`
  entry raised, and `GATE_FULL=1 bash tools/run-gates.sh` is green.

## 7. Gates

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/adopt-unattended.sh --check` ·
`tools/unattended/adopt-unattended.test.sh` · `tools/check-kit-versions.sh` ·
`python tools/memory-tree/check-arms.py` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/run-gates.sh`.

## 8. Open questions

- **F1 — does `--park` take a unit id?** A park almost always concerns one unit, and recording which
  would let the wrap-up group them. Against it: the anchor ban means the id cannot lead the line, and
  an id in the middle of free text is not a join anything can rely on. Options: no id field, and the
  question text names the unit in prose; or an explicit field placed after the timestamp.
  Recommendation: no field. The wrap-up is composed by an agent reading the record, not by a parser.
- **F2 — is S6 in this unit or its own?** It changes a Definition-of-Done item's evaluation, which is
  a different mechanism from a verb, and this build's own rule is one mechanism per spec.
  Recommendation: keep it here, because the refusal is only reachable once a verb exists to create
  the state it refuses — but this is the fork most likely to be split by review, and splitting it
  costs nothing but a sixth id.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit's first round. S6's refusal was phrased three
  different ways with no named observable and was attached to an evaluator the abort verb shares,
  which would have wedged the exit that exists for a run unable to proceed; it now names a countable
  observable carried in the existing attestation's value, and states close-verb-only placement with
  the reason. AC4's second clause read as a false claim about today's test rather than as the
  instruction it is, and is rewritten as an instruction. **Also added, and unlogged until round 2
  caught the omission:** S7, declaring the parked region's kinds as a two-class taxonomy, because the
  set-level fold gave `TOOL-aBoundedVerdict-1` a park kind whose lines must not count as decisions;
  the previous carriers item became S8.
- rev-3 · 2026-08-16 · folded round 2. The taxonomy S7 declared was contradicted by every place the
  count is actually spelled — S5, S6, the inventory row and the acceptance criteria all said parked
  lines unqualified, and only S7 said decisions — so the fold that added the taxonomy left the
  counter it exists to scope reading the other way. All four are now qualified. The taxonomy also had
  no machine home, no pin and no reader (S7a), and no arm that could fail, because every kind
  existing at this unit's landing is a decision kind (S7b) — a fixture built from today's kinds
  passes under either counter. Measured and fixed: the close verb appends its own override line AFTER
  the Definition-of-Done loop, so a count including it could never be satisfied. The method's wrap-up
  row was asserted narrowed by a unit that neither scopes nor touches the method; S7c hands it to the
  unit that does.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "record a decision the run refused to make"` names the
unattended kit's conf and the driver as the only seams, with no second implementation anywhere. The
seam this unit extends is `park()` itself, unchanged — the helper already takes the kind as an
argument, already has two callers, and already carries the comment explaining why a third caller
must not hardcode a grammar. The shared refusal helper and the staging helper are both reused as-is,
which is what keeps the new verb's branch count to the three refusals §5 enumerates.

Recall terms used, recorded for the reground: park verb parked decisions unattended driver run-state
authored region wrap-up owner turn attested Definition of Done bypass flag refusal.
