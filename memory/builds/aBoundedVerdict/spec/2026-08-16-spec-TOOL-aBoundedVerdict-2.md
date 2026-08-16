# TOOL-aBoundedVerdict-2 — a halted run records WHY, in a vocabulary something reads

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

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
  delegates; a unit awaits owner scope approval the mandate does not supply; a unit's acceptance or
  gates could not be derived; the repository state at start was outside what the mandate reaches; a
  gate is red and its fix lies outside the mandate's scope.
- **S2** — `--abort <slug> --reason <text> --code <CODE>`, with the code REQUIRED and validated
  against the effective vocabulary. An unlisted code is refused naming the legal set.
- **S3** — the code is recorded as its own authored fact through the existing fact writer, not
  buried in the reason prose, so a reader is a field read rather than a parse.
- **S4** — a project may APPEND members through a new `.unattended.conf` key and may not delete a
  core member. The core set's size is pinned shrink-only by its OWN new conf key, deliberately not
  by extending the existing two-field floor.
- **S5** — three readers, because a vocabulary with no reader is decoration and this kit says so
  about its own phase writer: `--status` names the code on its single line; `--resume` names it and
  states that the run is finished rather than resumable; and a new leg check asserts that every
  tracked run-state file whose phase is the aborted terminal carries a code in the effective
  vocabulary.
- **S6** — the wrap-up derivation gains the code as a derived row, so the one turn the owner gets
  opens with why the run stopped.
- **S7** — the protocol's phase and verb sections, the conf's key table, the rendered Skill, and the
  kit version constants.

## 3. Non-goals (OUT)

- **No new phase member, terminal or otherwise, and no move of the core phase floor or the terminal
  set.** This is the unit's central design decision and the owner ratified it against the
  measurements. A phase added to the core set is refused by the driver's own guard with a message
  naming two verbs that cannot write it; added as non-terminal it wedges the next run's preflight
  forever; and the protocol's phase list is joined to the driver's by no gate, so either drifts
  silently.
- No code on the landed terminal. A landing needs no reason.
- No code on a park. Parking is unit 5's mechanism and a park is not a halt.
- No retrofit of existing terminal records. The leg check applies to records the new verb wrote; the
  enumeration and the disposition for older ones are in §4.
- No claim that the code is trustworthy. The run writes it, as it writes every other authored fact,
  and the protocol's boundary section already states what that is worth.

## 4. Design

### Data model

The vocabulary is a driver constant, read by the leg the same way the leg already reads the core
phase and Definition-of-Done sets from the driver rather than restating them. The effective set is
the core set plus the project's declared extras, composed the way the phase set already is.

The size pin gets its own conf key rather than a third field on the existing floor. That existing
key parses by taking the text before the first colon and after the last, so a three-field value
would silently drop the middle one — and this repo has already been burned by that key, where a
malformed value disarmed both pins at once. A separate key is one more line of conf and no new
failure mode; an extended key is one fewer line and a silent hole.

| Fact | Written by | Read by |
|---|---|---|
| the phase | the terminal producers | thirteen in-kit readers, all on the terminal binary |
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
| awaiting scope approval | a unit whose status says it awaits the owner's scope approval | approve or amend the scope |
| acceptance underivable | the kickoff engine's fifth interactive exit | supply the acceptance check, or split the unit |
| precondition unmet | the kickoff engine's first three interactive exits | repair the repository state |
| gate red out of scope | a red gate whose fix the mandate does not reach | authorise the fix, or widen the mandate |

The mapping is the unit's real content. A code set that did not correspond one-to-one with the
enumerated exits would be a vocabulary invented ahead of its callers, which is what the phase
vocabulary already is.

### Migration

Existing terminal records carry no code. The leg check must not red them, and must not be written so
loosely that it never fires either. The disposition: the check applies to a record whose aborted
phase claim was written at or after the kit version this unit ships, which the record already
carries no field for — so the check keys instead on the presence of the code fact, with the
currently-tracked codeless aborted records enumerated once and registered. The enumeration is
mechanical and small; it is committed under this build's `build/` folder rather than asserted.

### Rollout

The verb's new required argument is a breaking change for any caller. The callers are the rendered
Skill and the kickoff engine's prose, both in this repository, both under parity gates that will red
if they are not updated in the same commit. That is the rollout: there is no external caller,
and the gates enforce it rather than a checklist.

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

`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` and its sibling ·
`tools/unattended/unattended.test.sh` · `.unattended.conf` · `tools/unattended/kit.toml` ·
`tools/unattended/PROTOCOL.template.md` and the installed protocol ·
`tools/unattended/SKILL.template.md` and the rendered Skill · `skills/session-kickoff/SKILL.md`
(the exits' abort disposition names the code) · `memory/guides/BUILD-METHOD.md`'s wrap-up table ·
`.memory-tree.conf` (arms floors) · the kit version constants.

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
  `bash tools/unattended/check-unattended.sh` reds naming the file, except for the records §4's
  enumeration registered. Arm in `tools/unattended/check-unattended.test.sh`.
- **AC5** — When the core vocabulary shrinks below its declared floor,
  `bash tools/unattended/check-unattended.sh` reds; when the floor key is absent or malformed, it
  refuses rather than passing with the pin disarmed.
- **AC6** — When the leg reads the vocabulary, it reads it from the driver:
  `grep -c 'REVIEW\|SCOPE-APPROVAL' tools/unattended/check-unattended.sh` finds no member spelled in
  the leg.
- **AC7** — When the Skill and protocol are re-rendered,
  `bash tools/unattended/adopt-unattended.sh --check` reports in sync with no surviving placeholder
  shape, and `bash tools/check-kit-versions.sh` is green with both unattended constants moved.
- **AC8** — `python tools/memory-tree/check-arms.py --check` exits 0 with both unattended
  `ARMS_FLOORS` entries raised, and `GATE_FULL=1 bash tools/run-gates.sh` is green.

## 7. Gates

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/adopt-unattended.sh --check` ·
`tools/unattended/adopt-unattended.test.sh` · `tools/check-kit-versions.sh` ·
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
