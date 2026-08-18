# TOOL-aPromptedMandate-2 — the RESEARCHING and TESTING phases

**Status:** SPECCED · rev-2 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

Give the research and solution-testing work a position in the run's vocabulary, so a prose-started
run that dies mid-research resumes into the right place instead of claiming a phase it is not in.

## 2. Scope (IN)

- **S1** — `RESEARCHING` and `TESTING` join `PHASES_CORE` in the driver, in run order, between
  `PREFLIGHT` and `SPECCING`.
- **S2** — `CORE_FLOOR`'s phase half moves from 10 to 12 in `.unattended.conf`, and in
  `.unattended.conf.example`.
- **S3** — protocol §3's **run-order token LIST** gains both tokens, in run order. That list — not a
  table; §3 has none — is the carrier leg check 16 arm D joins to `PHASES_CORE` in both directions,
  anchored on the line ending `in run order:`. A builder who adds prose and leaves the list reds with
  "a CORE phase is enforced by the driver and absent from the protocol's run-order list", which is
  the same leg AC3 requires green. Any per-phase meaning prose is a separate, ungated addition
  below it.
- **S4** — §3's sentence "The four middle members are named for the build method's PASS kinds" is
  rewritten. The two new members are **POSITIONS, not pass kinds**: M6 closes the pass set at five
  ("Nothing else is a pass") and neither new member is one of them. Rewriting §3 rather than widening
  M6 keeps the commit boundary and M7's reground points exactly where M6 puts them; research and test
  work commits at the boundary of the pass that consumes it.
- **S5** — `tools/unattended/.unattended.conf.example`'s `CORE_FLOOR` is corrected to the driver's
  actual set sizes and joined to them by an arm. It declares `CORE_FLOOR="10:6"` today and the DoD
  half is already stale against an eight-member `DOD_CORE`; the only arm that reads the example
  iterates key NAMES and never a value, so the header's "MEASURE, do not copy" does not self-enforce.

## 3. Non-goals (OUT)

- **Not a widening of M6's pass set.** S4 resolves the collision the other way, and the reason is in
  S4. A build-method change to accommodate a phase name would put the same fact in two documents.
- **Not `PHASES_EXTRA`.** Measured working (a phase declared there is accepted by the driver and by
  the leg), and rejected anyway: the conf's own header says the kit owns the CORE vocabulary and a
  project may only extend it. A capability the kit's own mode depends on cannot be a project's to
  omit.
- **No required SEQUENCE.** The vocabulary is a legal-values set; nothing in this unit makes a run
  pass through either phase. That obligation is unit 4's, and it belongs to the directive layer.
- No phase for the adversarial reviews — `REVIEWING` already exists and covers both.

## 4. Design

### Data model

`PHASES_CORE="PREFLIGHT RESEARCHING TESTING SPECCING REVIEWING FOLDING BUILDING RUNNING VERIFYING LANDING LANDED ABORTED"`

Adding is free against a shrink-only floor by construction — the leg asserts `nphase >= pfloor` — but
the floor is bumped anyway, because a floor left at 10 would let a later edit delete the two new
members silently, which is the exact property the floor exists to deny.

### Migration

A phase name is written into run-state files. Both names are NEW, so no landed record carries either
and no existing record changes meaning. Terminal-phase membership is untouched.

### Files touched (estimate)

`tools/unattended/unattended.sh` (one constant) · `.unattended.conf` and
`tools/unattended/.unattended.conf.example` (`CORE_FLOOR`) · `tools/unattended/PROTOCOL.template.md`
and `memory/guides/UNATTENDED-PROTOCOL.md` (§3's run-order list AND its pass-kinds sentence; they are
byte-compared by leg check 10, so both or neither) · `tools/unattended/unattended.test.sh`.

### Why the prose needs its own arm

Leg check 16 arm D joins the phase TOKENS both ways, so a missing token cannot ship. Nothing joins
the phase PROSE. That is the miscount class the leg's own DoD count-sentence arm was written after —
its comment records a table that grew to eight rows while the sentence above it still said six, in
both copies, with the parity leg green over a document contradicting itself. S4 therefore gets an arm
of its own, in that arm's shape.

## 5. Production-readiness checklist

- security — N/A
- perf / scale — N/A
- a11y / i18n — N/A
- error / empty / loading states — a phase outside the vocabulary is already a named refusal
  (measured: `check 19 FAILED — the phase is not in the declared vocabulary`)
- observability — the phase is what `--status` and `--resume` print
- risks — the two protocol copies drifting; leg check 10 byte-compares them and is the arm
- testing + left-shift gates — driver arm per phase, plus the floor arm
- migration / rollback — none needed, both names are new
- user docs — protocol §3

## 6. Acceptance criteria

- **AC1** — When `--phase <slug> RESEARCHING --witness <sha>` runs on a live record, it exits 0 and
  the recorded phase is `RESEARCHING`; same for `TESTING`.
- **AC2** — When `PHASES_CORE` is edited to drop either new member, `check-unattended.sh` fails on
  the `CORE_FLOOR` phase half by name.
- **AC3** — When `tools/unattended/check-unattended.sh` runs over this repo, it exits 0 with
  `CORE_FLOOR="12:8"` declared.
- **AC3b** — When the run-order list in `memory/guides/UNATTENDED-PROTOCOL.md` omits either new
  token, `bash tools/unattended/check-unattended.sh` fails with arm D's text "a CORE phase is
  enforced by the driver and absent from the protocol's run-order list".
- **AC3c** — When §3's pass-kinds sentence names a count that disagrees with the driver's middle-member
  count, `bash tools/unattended/check-unattended.sh` fails by name — the prose arm, in the shape of
  the existing DoD count-sentence arm.
- **AC3d** — When `tools/unattended/.unattended.conf.example`'s `CORE_FLOOR` or `DIRECTIVES_FLOOR`
  disagrees with the word counts of `PHASES_CORE`, `DOD_CORE` and `DIRECTIVES_CORE` in
  `tools/unattended/unattended.sh`, `bash tools/unattended/unattended.test.sh` fails by name.
- **AC4** — When `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md`
  are compared by leg check 10, they agree.

## 7. Gates

`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/unattended/check-unattended.test.sh` · `bash tools/check-kit-versions.sh` ·
`bash tools/run-gates.sh`

## 8. Open questions

none — the fork below is RESOLVED.

- **Core or `PHASES_EXTRA`** — RESOLVED (agent, 2026-08-18): core. The conf's own header reserves the
  core vocabulary to the kit, and the mode this build adds is a kit capability.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the M4 spec audit. S3 named a §3 "phase table" that does not exist —
  the gated carrier is the run-order token list (id 33). S4 added: the additions falsified §3's
  pass-kinds sentence and M6's closed pass set with nothing to catch it (id 6). S5 added: the example
  conf was in scope with no AC and carries a stale `:6` (id 15). Tier 1 -> 2, because the unit now
  amends a binding contract's prose.

## 10. Reuse audit

Satisfied for the SET in unit 1's §10; the seam this unit extends is the `phases()` composer in
`tools/unattended/unattended.sh`, which already joins core and extra in one place, so the driver's
membership test and the leg's floor assertion pick the new members up without edit. The THIRD
consumer, leg check 16 arm D, reads the constant against the protocol's run-order list and does need
the carrier edit S3 names — rev-1 missed it by naming the wrong carrier. The prose arm S4 adds is
modelled on the leg's existing DoD count-sentence arm rather than invented.
Measured before speccing: a phase added through `PHASES_EXTRA` was accepted by `--phase` and left the
leg green, which is what establishes that the composer needs no change and only the constant does.
