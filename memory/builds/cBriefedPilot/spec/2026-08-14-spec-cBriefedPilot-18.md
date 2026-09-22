# TOOL-cBriefedPilot-18 — the contract describes the directive layer, and publishes only what exists

**Status:** CLOSED · rev-5 · 2026-08-16 · node c · Tier-2 · base 37c05e1b · streams tooling+playbook · ratified 2026-08-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-15-review-TOOL-cBriefedPilot-1-1.md](../reviews/2026-08-15-review-TOOL-cBriefedPilot-1-1.md) | spec-audit | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |
| [2026-08-16-review-TOOL-cBriefedPilot-1-2.md](../reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md) | diff-review | TOOL-cBriefedPilot-1 TOOL-cBriefedPilot-2 TOOL-cBriefedPilot-3 TOOL-cBriefedPilot-4 TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-6 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-9 TOOL-cBriefedPilot-10 TOOL-cBriefedPilot-11 TOOL-cBriefedPilot-12 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-15 TOOL-cBriefedPilot-16 TOOL-cBriefedPilot-17 TOOL-cBriefedPilot-19 TOOL-cBriefedPilot-20 TOOL-cBriefedPilot-21 TOOL-cBriefedPilot-22 |

<!-- /gen:spec-records -->

## 1. Goal

Make the binding contract describe the layer this build installed: a new §10 for the directive
mechanism, a fourth parked kind, a spill exemption that keeps waiver entries readable, two new
Definition-of-Done rows with the count sentence that names them, and the layer's name in the
playbook's domain-rules enumeration. It lands late on purpose — the contract publishes only what
already exists.

## 2. Scope (IN)

- **S1** — a new §10 in the protocol pair carrying the directive MECHANISM and ZERO handle names:
  kit-owned, waivable only at preflight with a reason, recorded as a parked entry, never a DoD
  override, never removing a gate, plus one sentence pointing at the rendered Skill's table as the
  handle list.
- **S2** — §2 fact 3 enumerates FOUR kinds the parked region holds: a parked decision, an abort
  reason, a recorded DoD override, an owner directive waiver. `park()`'s kind argument is already the
  discriminator, so this names what the code does rather than asking it to do more.
- **S3** — §2's spill rule gains one clause: waiver entries are not spillable.
- **S4** — §4 gains a row for `build-complete` and a row for `closing-review-recorded`, and the
  count sentence at line 138 of `memory/guides/UNATTENDED-PROTOCOL.md` moves from six to eight.
- **S5** — §1 gains the owner's act clause — they author nothing per run except the reason text of a
  directive waiver, which `--preflight` records on their behalf — and the statement that the build
  method is a RUN-TIME dependency of this kit, which is what unit 4's preflight refusal enforces.
- **S6** — §7's `--preflight` bullet names `--waive <handle> --reason <text>` as accepted there and
  by no other verb; and §7's `--plan` bullet drops the sentence that the verb cannot see a planned
  unit with no spec, which unit 6 makes false. The Skill's matching `--plan` blurb is unit 11's S5.
- **S7** — §8's declaration table gains `DIRECTIVES_EXTRA` and `DIRECTIVES_FLOOR`, with
  `DIRECTIVES_FLOOR` marked mandatory for the same reason `CORE_FLOOR` is.
- **S8** — `parallel-coding-governance.domain-rules.md`'s unattended bullet gains the default
  directive set and its named waiver to its enumeration of what the contract carries.
- **S9** — the `verb_resume` comment at `tools/unattended/unattended.sh:909` says the authored region
  carries five facts against the protocol's seven. One word, in the unit that opens §2 anyway.
- **S10** — `memory/project/method-carriers.txt` gains a row for
  `tools/unattended/PROTOCOL.template.md`, because S1 and S5 make it mention `BUILD-METHOD.md` and
  the carriers leg keys on that basename. The live twin is excluded by the leg's `memory/*` rule.
- **S11** — both halves of the pair move in ONE commit. Leg check 10 byte-compares them and would
  otherwise red on the first of two.
- **S12b** — §1's preamble reads `Three properties, all mechanical:` over FOUR bullets, in BOTH
  halves. It is the same class as the `:909` five-against-seven comment S9 already fixes, in the very
  section S12 rewrites. It becomes `Four properties, all mechanical`.
- **S12** — §1's roster bullet stops reading opt-in by presence. For an unattended build the roster
  marker pair is REQUIRED, per the owner's P3, and the enforcement it names is `build-complete`'s
  term 1 rather than a second rule. The immutability half of that bullet is unchanged: the slice
  still may not move under the run, and it is still `authorization-reachable` that says so. Without
  this clause the binding contract states the opposite of the owner's REQUIRE and no unit corrects
  it — unit 7's S5 defers the statement here and this spec did not claim it.

## 3. Non-goals (OUT)

- **The two Definition-of-Done items themselves.** Units 7 and 8 build them and raise `CORE_FLOOR`'s
  DoD half from six to eight, one each. This unit publishes rows for items that already exist; the
  dependency on 3, 7, 8, 13 and 16 is what makes that sentence true.
- **Naming a single handle in §10.** Zero handles in the contract means zero to keep in step across
  three spellings.
- **The §3 phase vocabulary.** This build adds no phase, and §3 takes no edit.
- **The join that reads these two tables.** Unit 22 extends leg check 16 arm A to §3's phase list and
  §4's DoD table. This unit adds rows and changes no shape, which is the whole precondition.
- **The version marker at line 1 of both halves.** Unit 19.
- **`tools/unattended/kit.toml`'s key lists.** `DIRECTIVES_FLOOR` has to reach the deployer's machine-
  read declaration, because unit 12's arm C refuses it undeclared and an adopter would otherwise
  deploy green and red their own `unattended kit gate`. It lands in unit 12's S9, with the branch
  that creates the obligation, rather than here where it would leave that gap open across six units.
- **M6, M8, M9 and M10.** The build method's own edits are units 15 and 16, and M1 forbids this
  contract restating any of them.

## 4. Design

### §10, and why it names no handles

The list of handles exists three times already once this build lands: `DIRECTIVES_CORE` in the
driver, the table in the rendered Skill, and leg check 16's join between them. A fourth spelling in
the binding contract would be the copy that rots, and the domain-rules companion already refuses
exactly that move for the protocol as a whole. So §10 states the mechanism and points: the registry
is kit-owned and shrink-only, a waiver is taken at preflight and nowhere else, it carries a required
reason, it is recorded as a parked entry, it relaxes a DIRECTIVE and never a gate, and it is never a
Definition-of-Done override. The handle list is the Skill's table, named by one sentence.

The per-handle checkability classification — machine-checked, internal consistency over run-written
tokens, observed by nothing — stays in the build README. It is an argued-once classification and it
belongs where the argument is.

### The spill rule, and why waivers are exempt

Waiver entries are written at preflight, so they are permanently the OLDEST entries in the parked
region. §2's budget spills oldest-first at 8 KB. The first spill therefore evicts exactly the lines
leg check 17 grades, after which check 17 passes by finding nothing and M9's wrap-up row derives from
a region that no longer holds them. The exemption is one clause.

Measured, and stated because it changes what this clause is: no spill is implemented. `grep` over
`tools/unattended/unattended.sh` and `check-unattended.sh` finds no spill path at all — §2's budget
is prose with no code behind it today. So the clause does not correct an implementation, it
constrains the one that gets written, and that is the cheapest moment to write it down.

### The count sentence, located

Measured: §4's count is the sentence at line 138 of `memory/guides/UNATTENDED-PROTOCOL.md` —
"Six kit-owned core items." The floor sentence at lines 150-151 carries no number and needs no edit.
Both halves are at the same line number, because they are byte-identical.

### The pair is byte-identical today

Measured: `diff` over the two halves after CRLF normalisation is empty, and neither half contains the
string `tools/`, so leg check 10's prefix substitution is a no-op on this pair. Every edit below is
applied twice, byte for byte, in one commit.

### The two table shapes unit 22 will join

§3's phase list is one inline run of backticked tokens; §4's Definition-of-Done table's first column
is a backticked item name. Unit 22 joins `PHASES_CORE` and `DOD_CORE` against exactly those two
shapes, so this unit adds rows and touches neither shape.

The join is on the ITEM NAME and not on the checker column. `DOD_CORE` will spell
`build-complete:machine`, because that suffix is a two-state budget switch — it decides whether an
unmet item spends the `--close` override budget — while §4's "Checked by" column is where the honest
classification goes. Both rows say `machine` in the constant and carry their real limit in the
Asserts cell: `build-complete` reads spec status tokens the run itself writes and routes them through
a region the run re-renders; `closing-review-recorded` joins on a BASE the run pinned. Neither is an
authorization verdict and §9 already says why nothing here is.

### Data model

| Protocol section | Edit |
|---|---|
| §1 | the owner's act clause; the build method as a run-time dependency; the roster REQUIRED, not opt-in (S12) |
| §2 fact 3 | four kinds, enumerated |
| §2 spill | waiver entries are not spillable |
| §4 | two rows, and six becomes eight in the count sentence |
| §7 | `--preflight` names `--waive <handle> --reason <text>`; `--plan` drops its unspecced-unit caveat |
| §8 | `DIRECTIVES_EXTRA` and `DIRECTIVES_FLOOR` |
| §10 | new, last, mechanism only |

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/PROTOCOL.template.md` | S1-S7 and S12 |
| `memory/guides/UNATTENDED-PROTOCOL.md` | the same bytes, same commit (S11) |
| `parallel-coding-governance.domain-rules.md` | S8 |
| `tools/unattended/unattended.sh` | S9, one word at `:909` |
| `memory/project/method-carriers.txt` | S10, one row |

### Migration

None for an adopter who has not installed the kit. An adopter who has takes the new protocol on their
next render and must declare `DIRECTIVES_FLOOR`, which unit 12's arm C refuses as undeclared exactly
as `CORE_FLOOR` is refused. That refusal is unit 12's, named here because §8's table is where the
adopter reads about it.

### Alternatives rejected

- **§10 enumerating the eleven handles.** Rejected: a fourth spelling of one list inside the document
  whose companion says the contract is not paraphrased.
- **A `waivers:` eighth authored fact.** Rejected in unit 3. §2's seven-fact count is unchanged, and
  the fourth parked KIND is what carries the record.
- **Paraphrasing §10 into the domain-rules companion.** Refused by that companion's own sentence.
  S8 adds a NAME to an enumeration written as a complete list; it states no rule.
- **A §6 Landing sentence.** See §8 — the design pass named one and did not state it.

## 5. Production-readiness checklist

- security — contract text. The spill exemption is what keeps a security-relevant record readable,
  and nothing gates it; it is a rule for an implementation that does not exist yet.
- perf / scale — the protocol is 18,214 B against the guides cap of 61,440 B and 270 lines against
  750, so hygiene check 6 is not close. Check 16's read path is the binding budget: measured 68,989 B
  across six files against a `READ_PATH_CEILING` of 86,476, and this unit spends about 1 KB of the
  17,487 B of headroom.
- a11y · i18n — N/A.
- error / empty / loading states — N/A, no runtime surface. The one runtime edit is a comment.
- observability — N/A.
- risks — the two halves diverging. S11 is the control and leg check 10 is the detector.
- testing + left-shift gates — `unattended kit gate` check 10, `method carriers`, `memory hygiene`.
  Unit 22 is what will hold §4's rows to `DOD_CORE`; until it lands the two are joined by review only.
- migration / rollback — see §4. Reverting is a single revert of one commit by construction.
- user docs — this IS the user doc, and the domain-rules bullet is its index entry.

## 6. Acceptance criteria

- **AC1** — When both halves are edited, `bash tools/unattended/check-unattended.sh` check 10 is
  green; when only one half is edited, it reds naming both paths.
- **AC2** — The protocol's §10 contains no member of `DIRECTIVES_CORE`, checked by grepping the
  eleven handles against both halves and finding zero hits.
- **AC3** — §2's fact 3 enumerates four kinds, and `waiver` is one of them.
- **AC4** — §4's table carries a `build-complete` row and a `closing-review-recorded` row, and the
  count sentence reads eight.
- **AC5** — `bash tools/memory-tree/check-method-carriers.sh` is green with the new row and reds with
  the row removed, because `PROTOCOL.template.md` now mentions `BUILD-METHOD.md`.
- **AC6** — `python tools/memory-tree/corpus_ids.py --report` shows the read-path total still under
  `READ_PATH_CEILING` after the edit, observed rather than assumed, and `memory hygiene` check 16 is
  green.
- **AC7** — `git diff --name-only` for this commit names `parallel-coding-governance.domain-rules.md`
  and does NOT name `parallel-coding-governance.template.md`, and the domain-rules unattended bullet
  enumerates the default directive set and its named waiver.
- **AC8** — `tools/unattended/unattended.sh:909` reads seven, and no other count in the driver
  disagrees with the protocol's §2.
- **AC9b** — §1's stated property count equals the number of bullets that follow it, observed in
  BOTH halves. A count asserted against prose is the defect this build keeps finding, so the check is
  the comparison and not the literal word.
- **AC9** — §1's roster bullet in both halves no longer reads `Opt-in by presence`, grepped and
  found zero, and names `build-complete` as what enforces the requirement.
- **AC10** — §7's `--plan` bullet no longer says the verb cannot see a planned unit with no spec,
  and `--plan` run over a fixture whose roster names an unspecced id prints the row the bullet used
  to deny — the observation that the document and unit 6's behaviour now agree.

## 7. Gates

`unattended kit gate` (check 10 especially) · `unattended gate selftest` · `method carriers` ·
`method-carriers self-test` · `memory hygiene (20 checks)` · `template size ≤32 KiB` ·
`unattended driver selftest` (the `:909` comment is a non-functional edit and must move nothing) ·
the full bar at the push boundary.

## 8. Open questions

none — the fork this spec carried was RESOLVED (owner, 2026-08-15) and §6's Landing takes no
  edit. What is recorded here instead is a PARTIAL BUILD, because two scope items describe behaviour
  that does not exist.

  **S4 and S12 are NOT BUILT.** S4 adds §4 rows for `build-complete` and `closing-review-recorded`
  and moves the count six to eight; S12 makes the roster REQUIRED and names `build-complete`'s
  term 1 as the enforcement. Units 7 and 8 are PARKED, so neither item is in `DOD_CORE` and no
  term 1 exists. Writing them would put the binding contract in the position this whole build
  keeps finding others in: a record describing a rule nobody shipped. The count would say eight
  over six rows, which is the same defect S12b fixes two sections up.

  The other eleven items ARE built, because each documents something that shipped: §10 the
  directive layer (units 2, 3, 9, 10), §2's fourth parked kind and its spill rule (unit 3), §1's
  run-time dependency (unit 4), §7's `--waive` and `--plan` bullets (units 3, 6), §8's two
  declarations (unit 2).


none — the fork below is RESOLVED (agent, 2026-08-15, delegated): option (a) — protocol §6 Landing takes no edit.

  Option (b) was VETOED under M3 rule 2: it writes a rule into a governance carrier that already
  states it one document over, which is the two-answers-to-one-question defect this build exists to
  avoid. The design pass already rejected D11's second half on the same ground, and the close-time
  consequence is already printed by name at the point of use.

**What is the §6 sentence the design pass called DELTA 3?** The folded design's §0 re-affirms
"DELTA 3 (protocol §6's one sentence)" and never states the sentence; the converged design it
supersedes is not in this tree and no commit ever added it, so the text is unrecoverable rather than
merely unread. Options: (a) §6 Landing takes no edit; (b) §6 gains a sentence saying a waived
`land-once-done` still owes `--override build-complete --reason` at close. Recommendation: (a). The
design pass already rejected D11's second half on the ground that M8's landing pointer resolves
through the protocol's `build-complete` row, so writing the same rule into §6 as well is the
two-answers-to-one-question defect one document over. Measured, the close-time consequence is already
told to whoever needs it: `unattended.sh:946` prints the unmet item by name, which is the exact
argument `--override` takes. Resolver: owner.

**RESOLVED at authoring: §4's checker column stays prose and the join is name-only.** `DOD_CORE`
spells both new items `:machine` because the suffix drives the override budget and has two states;
§4's Asserts cell carries the honest limit. Adding a third suffix value would change `dod_met`'s
branching to express a distinction that is prose. This is the spec author's decision, not a fork the
owner declined, and it is recorded because unit 22's join depends on it.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds 2a, 2b, 2c, 2d, 2e, 2f, 2j and 2k
  from that pass. Adds three measurements it did not make: the pair is byte-identical today and
  contains no `tools/` spelling, so check 10's prefix substitution is inert on it; no spill is
  implemented anywhere in the kit; and `check-method-carriers.sh` keys on the BASENAME
  `BUILD-METHOD.md`, which is what makes S10's row real rather than stale.
- rev-2 · 2026-08-14 · three edits that siblings put IN and this spec did not claim, found on the
  cross-read. S12 is new: unit 7's S5 defers the P3 roster obligation to "the protocol by unit 18",
  and measured, `memory/guides/UNATTENDED-PROTOCOL.md:31` reads "Opt-in by presence" — so the binding
  contract would have stated the opposite of the owner's REQUIRE with no unit correcting it. S6 gains
  §7's `--plan` bullet, which unit 6 falsifies and unit 6's own §5 assigns here. And §3 now names
  `kit.toml`'s key list as unit 12's, because it was in nobody's scope: unit 12 arm C refuses an
  undeclared `DIRECTIVES_FLOOR` and the deployer's `required_keys_gate` would never have gained it.
  AC7 replaced: `template size` is green on an empty commit, so it observed nothing about this change.

- rev-3 · 2026-08-15 · §8 resolved under the standing mandate for `cBriefedPilot`; the pick and the reasoning are in §8. Header gains the ratified pointer.

- rev-4 · 2026-08-15 · §8's audit fold. S12b and AC9b: §1 reads `Three properties` over FOUR bullets in both halves, in
  the very section S12 rewrites — the same class as the five-against-seven comment S9 fixes.

- rev-5 · 2026-08-15 · built PARTIALLY and the omission is in §8. S4 and S12 describe the two
  Definition-of-Done items units 7 and 8 park, so they would document behaviour that does not
  exist — including a count of eight over six rows. Eleven items built; both halves moved in one
  commit, as S11 requires.
## 10. Reuse audit

- **The protocol pair itself, `tools/unattended/PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md`** — the seam extended. It is a document pair with a
  byte-comparison leg already on the bar; this unit adds sections to it and adds no mechanism.
- **`park()`'s kind argument in `tools/unattended/unattended.sh`** — the discriminator §2's fact 3
  enumerates. S2 documents an existing capability; unit 3 adds the fourth kind's writer.
- **`memory/project/method-carriers.txt`** — the registry, extended by one row. Keyed on path alone,
  so the row cannot go stale from an edit above it.
- **`parallel-coding-governance.domain-rules.md`'s unattended block** — the kit-conditional section
  that already exists for exactly this kind of addition, which is why nothing lands in the byte-gated
  template.

No new seam is created. The one thing with no existing seam is a spill implementation, and S3 is a
rule about it rather than the thing itself.

Recall terms used: unattended protocol contract section parked kind spill budget waiver directive
Definition of Done override domain rules enumeration carrier pair render.
