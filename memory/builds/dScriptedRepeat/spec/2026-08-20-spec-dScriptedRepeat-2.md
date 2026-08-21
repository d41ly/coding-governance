# TOOL-dScriptedRepeat-2 — the PLAYBOOK TEMPLATE, derived then frozen

**Status:** CLOSED · rev-4 · 2026-08-21 · node d · Tier-2 · base d2a40aa8 · streams tooling · ratified 2026-08-20

## 1. Goal

Ship the template a playbook is written from: a closed section canon derived from the reference
corpus and the instruction-design literature, frozen and marked human-curated, with a per-segment
length budget the checker DERIVES rather than a number typed into prose.

## 2. Scope (IN)

- **S1.** `tools/unattended/PLAYBOOK-TEMPLATE.template.md`, plus THE ADOPTER WORK THAT SHIPS IT.
  `adopt-unattended.sh` never reads `kit.toml`: it hardcodes exactly two destinations at `:137` and
  `:140`, renders one and copies the other, and its own comment at `:197` says "The adopter installs
  TWO artifacts, so --check verifies two." The `[[files]]` rows are read by `govkit.py` for deployment
  PLACEMENT, not by this kit's adopter. So this unit edits `adopt-unattended.sh` — a third destination,
  a third `--check` arm with its own not-installed and drifted refusals, the placeholder arm, and that
  comment — plus the `[[lf_pin]]` row. Without those edits nothing renders a third artifact and AC3 is
  an observation nobody can make.
- **S2.** The SECTION CANON, twelve required sections in fixed order, listed in §4. Every one is
  required-with-a-declared-null: a section that genuinely does not apply keeps its heading and carries
  the single line `none — <why>`. This is the memory kit's own `N/A — <why>` rule for spec sections,
  reused rather than reinvented.
- **S3.** The DECLARATION BLOCK at the head of the file — one fenced TOML block holding every
  machine-read declaration, so a reader sees the whole machine contract at once and unit 3's checker has
  one parse. Its key set is the UNION of what units 3, 4, 5, 7 and 8 declare, listed in ONE place with
  an owning-unit column and enumerated nowhere else. The previous revision enumerated the keys here and
  was wrong within the same build: unit 7 declares an eighth key this list did not carry, unit 5 reads a
  per-piece checks key nothing declared, and the reader list named unit 6 (which reads none of it) while
  omitting unit 8 (which reads `outputs`).
- **S4.** The EXEMPLAR RULE, stated in the template and enforced in unit 3: every sentence quoted in a
  playbook as an illustration is PROHIBITED OUTPUT unless it is a tracked fixture. Derived from a
  measured failure, not a preference — see §4.
- **S5.** The per-segment LENGTH BUDGET. The checker derives it and prints it; the template states the
  rule and not the number. A segment is one addressable section, because a pass re-reads its segment
  rather than the file.
- **S6.** The FREEZE. The template ships with a `curated:` line naming the human who ratified it and
  the date, and a re-derivation mode that regenerates a CANDIDATE canon from a corpus for comparison
  without overwriting the frozen one.
- **S7.** The derivation record: which section of which reference playbook fills each canon section,
  and what does NOT fit. Written into this build's `build/` folder, not the template.

## 3. Non-goals (OUT)

- No migration of the two reference playbooks. They are another repo's production artifacts and fork
  11's soft grammar exists precisely so this build does not require one.
- No content-kind opinions. The template does not know what an article or an image is; fork 7 holds.
- No producer adapters, no model ids, no tool names. Those are playbook prose per fork 7.
- No checker in this unit. The template is a document; unit 3 is the gate over it. Two mechanisms,
  two specs, per M2.
- No prescribed step COUNT. The floor is declared per playbook by its author, never by the kit.

## 4. Design

### The section canon

Twelve required, in order. The derivation for each is in §10's record; the short form is which
reference fills it.

| # | Section | Job | Filled by |
|---|---|---|---|
| 1 | Identity and provenance | what this makes · ratification id and date · evidence links · `curated:` | both |
| 2 | Ground rules | the non-negotiable frame every piece inherits | both |
| 3 | Inputs and preconditions | what must exist before a piece can start | both |
| 4 | Outputs | the declared paths, the piece GRAIN, what one piece physically is | neither, explicitly |
| 5 | The step checklist | numbered steps, each tagged `GATE` or `CHECK` | PLAYBOOK; HYBRID via §2 and §5 |
| 6 | The producer recipe | the slotted scaffold and which slots vary | HYBRID |
| 7 | Per-piece checks | passes over ONE piece, each with a binary anchored verdict | PLAYBOOK checklist D |
| 8 | Set-scoped checks | passes over ALL N | PLAYBOOK D13 and its corpus invariants |
| 9 | Declared gate legs | the leg registry, the coverage mode, the named refusal | PLAYBOOK by reference |
| 10 | Ruled out — do not re-try | the negative knowledge, dated and attributed | both |
| 11 | Measured failure modes | failure classes with observed RATES | HYBRID |
| 12 | Corrections to this file | this playbook's own prior claims, superseded and dated | PLAYBOOK, inline |

Section 4 is filled by NEITHER reference and that is the finding, not an oversight: both encode their
output locations in prose that a machine cannot read, which is why the reference checker can validate
a plan row and cannot validate that a piece landed anywhere. Section 8 exists as invariants in one
reference and as no section in either.

### The declaration block

One fenced TOML block, immediately after section 1's heading, holding every machine-read value. One
block rather than per-section keys because a reader must be able to see the whole machine contract at
once, and because unit 3's checker then has one parse.

The key table lives in the template itself with an owning-unit column, and unit 3 gates the JOIN in
both directions — a declared key no unit owns REDS, and a unit reading a key the block does not declare
REDS — the same both-directions join unit 10 already uses for the directive table. Their semantics
belong to the units that read them and are specced there, never restated here; that restatement is
exactly what went stale.

### The exemplar rule

**Every sentence quoted in a playbook as an illustration is PROHIBITED OUTPUT unless it is a tracked
fixture.** This is the highest-value single rule in the template and it is derived from measurement,
not taste: in the reference corpus one checklist's own example phrase shipped verbatim in 8 of 9
articles, its model refusal in 5 of 9, and its three named props matched one body's prose exactly.
The reference's own conclusion is the rule — an exemplar in a checklist that N writers read is a
template, whatever the surrounding paragraph calls it. For a mode whose entire purpose is N pieces
from one document, this is the characteristic failure, and it is invisible to every per-piece check.

### Length, and why the number is not here

The external evidence is that instruction-following degrades sharply with instruction-set length, with
a measured cliff around six thousand words, and that first-answer accuracy falls steeply with step
count. The reference playbook is well past that cliff as one document. The template's answer is not a
smaller playbook, which would lose the negative knowledge that makes it valuable, but ADDRESSABILITY:
a pass reads the SEGMENT its step lives in and re-reads it per piece rather than inheriting it. The
budget is therefore per segment, derived by the checker from the declared canon, and printed on every
run. No number appears in the template or in this spec, because a count of a derived population in
prose is the class this repo bans.

### Alternatives rejected

**A prose companion plus a data file.** Rejected: the reference corpus already demonstrates the
failure — its checklist and its checker disagreed about whether a leg was blocking for two days, and a
spec sized four invariants wrongly on the strength of it. One document with a declaration block keeps
the contract beside the prose that explains it.

**Deriving the canon and shipping it underived.** Rejected on this repo's own established answer: a
derived table nobody edited is a mirror of the corpus, which is the one shape a template must not
have. Hence S6's freeze and the `curated:` line.

**A hard section-equality canon.** Rejected by fork 11's evidence, which measured that the only
in-repo hard canon grandfathers by TOTAL exemption and therefore FORBIDS an old file from conforming
early — a wall in front of "updates existing playbooks".

## 5. Production-readiness checklist

- security — a playbook is prose an agent executes against. It can name a command. The template
  neither sandboxes nor validates what a step instructs, and unit 3's gate reads SHAPE only. Stated
  here rather than discovered: a malicious playbook is a malicious document, and the boundary is
  protocol §9's, unchanged.
- perf / scale — the length budget is the perf story. It is derived and printed, never asserted.
- a11y — N/A, a markdown document.
- i18n — the canon's section headings are ASCII and fixed; a playbook's prose is not constrained.
- error / empty / loading states — a section present but EMPTY must red; a section carrying
  `none — <why>` must pass. These are two different states and unit 3 distinguishes them.
- observability — the checker prints the derived budget and the drain census on every run, so a
  playbook's health is visible without reading it.
- risks — the canon is twelve sections and one reference fills ten. The declared-null escape is what
  keeps that from being a distortion, and §8 F1 asks whether twelve is right.
- testing + left-shift gates — unit 3 owns the gate. This unit's own acceptance is that both
  references map onto the canon with every mismatch NAMED rather than forced.
- migration / rollback — the template is new; nothing migrates. An adopter without it is unaffected.
- user docs — the template IS the user doc for playbook authors. The kit README gains a pointer.

## 6. Acceptance criteria

- **AC1** — When both reference playbooks are mapped onto the canon, every one of the twelve sections
  is either FILLED or carries an explicit non-fit note in the derivation record at
  `memory/builds/dScriptedRepeat/build/`. No section is silently skipped.
- **AC2** — When the recipe-shaped reference is mapped, the sections it cannot fill resolve to
  `none — <why>` rather than to invented content, and the record names which and why.
- **AC3** — When `bash tools/unattended/adopt-unattended.sh --check` runs against a tree where the
  third artifact is missing, it REFUSES; and when the installed copy has drifted from the shipped
  template, it REFUSES with a distinct message. Two arms against the specific new `--check` arm S1 adds,
  because a byte-compare that no code path produces is not an acceptance criterion.
- **AC3b** — When a playbook's declaration block carries a key absent from the template's owning-unit
  key table, `bash tools/unattended/check-playbook.sh` REDS. That direction has a machine source on both
  sides — the template's table and the playbook's block — and is staged and observed. The REVERSE
  direction, "a unit reads a key the block does not declare", is a documented CHECK and says so in the
  leg header: what a unit reads exists only as spec prose, so unlike unit 10's directive join there is no
  second machine source to compare against. Its first victim would have been this build's own artifact,
  since no spec declared the per-piece checks key unit 5 reads — now declared by unit 5 S7b.
- **AC4** — When the template is read, the exemplar rule appears in `PLAYBOOK-TEMPLATE.template.md` and the template ITSELF quotes
  no sentence as a model except ones marked prohibited or pointing at a tracked fixture. Self-applying,
  and observed by reading, because a template that violates its own loudest rule teaches the violation.
- **AC5** — When `curated:` is absent or empty, `bash tools/unattended/check-playbook.sh` REDS, with no
  run binding involved. The rule is unit 3 S9c's and this line states the same one — the previous
  revision and unit 3 F2 carried two different answers, and the freeze is fork 4's only machine
  consequence, so it may not depend on which spec a reader opens first.
- **AC6** — When the re-derivation mode runs over a corpus, it writes a CANDIDATE canon to a separate
  path and leaves the frozen template byte-identical, verified by `git status --porcelain`.

## 7. Gates

`bash tools/unattended/check-unattended.sh` · the new validity leg from unit 3 ·
`bash tools/unattended/adopt-unattended.sh --check` for the render · `bash tools/run-gates/run-gates.sh`.
The template is a kit-shipped document, so it also acquires a `gov:kit` version marker and joins the
`kit version markers` leg — a carrier this repo has a recorded defect about, where a fix naming one
carrier of several landed in only one.

## 8. Open questions

none — every fork below is RESOLVED in place.

- **F1 — is twelve the right canon size?** RESOLVED (agent, 2026-08-20, delegated): the twelve stand
  as REQUIRED, and a section exceeding the derived per-segment budget is SPLIT, never dropped. The
  measurement decides how a section is SEGMENTED, which is a rendering question; it does not decide
  which sections exist, which is scope. Dropping a required section to fit a budget would lose the
  negative knowledge §4 argues is the template's most valuable content, and would trade a measured
  problem for an unmeasured one.
- **F2 — where the template physically lives in an adopting repo.** RESOLVED (agent, 2026-08-20,
  delegated): `{memory_root}/guides/PLAYBOOK-TEMPLATE.md`, beside `BUILD-METHOD.md`, because both are
  documents an author reads while working and neither is a protocol. This ADDS to the read path, which
  is what made it a question — and the owner raised `READ_PATH_CEILING` on 2026-08-20 with this build's
  spend named in the argument, so the constraint that made it doubtful is discharged rather than
  ignored.

## 9. Revision log

- rev-4 · 2026-08-21 · CLOSED: built and landed on main at c8e0436, full bar GREEN 90/90 before
  the merge and again over the merged tree.
- rev-4 · 2026-08-20 · folded the round-2 spec audit, which returned BLOCKED at precision 0.625 over
  the fold range. Every change here repairs a place where two sentences in this build ordered opposite
  implementations and neither was marked the loser.
- rev-3 · 2026-08-20 · pre-code fork sweep under the mandate (M3). Every §8 fork RESOLVED in
  place with its resolver and authority named, and §8's first non-blank line made machine-legal —
  the driver classified nine of eleven specs FORKED on that line alone.
- rev-1 · 2026-08-20 · initial draft. Canon derived from the corpus-anatomy and
  external-instruction-design records; section 4 and section 8 identified as filled by neither
  reference; the exemplar rule lifted from the reference's own measured failure.
- rev-2 · 2026-08-20 · folded the M4 spec audit. F14 pulled the adopter work in scope after the audit
  showed `adopt-unattended.sh` never reads `kit.toml` and hardcodes two destinations, making AC3 an
  observation nothing could make. F15 replaced the enumerated key list with a pointer plus a
  both-directions join, because the enumeration was already wrong against three other specs in the same
  build. F13 aligned AC5 with unit 3's resolution of the same question.

## 10. Reuse audit

Two seams are reused rather than rebuilt, and a third this spec claimed turned out to be false. The RENDER path is `kit.toml`'s existing
`[[files]] role = "rendered"` mechanism with a `to =` target and a placeholder list, already used for
the Skill and the protocol — but that mechanism drives govkit's deployment PLACEMENT and is NOT read by
this kit's own `adopt-unattended.sh`, which hardcodes two destinations. So the render costs adopter
edits after all and S1 carries them; what is genuinely reused is the render, byte-compare and `--check`
SHAPE, a pattern rather than a free ride. The DECLARED-NULL escape is the
memory kit's `N/A — <why>` rule for spec sections, which already has a working gate and an observed
failing case. The DERIVE-THEN-FREEZE discipline with a `curated:` mark is the lexicon kit's, whose
specs establish that a derived vocabulary nobody edited is a mirror of its subject — and whose adopter
refuses to re-scaffold over an existing conf, which is why S6 specifies a re-derivation mode that
writes elsewhere: a one-way door is exactly wrong for a mode whose second verb is updating existing
playbooks. Recall terms used: template render placeholder canon section required null declared freeze
curated derive corpus mirror adopter parity kit version marker guide read path.
