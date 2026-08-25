# TOOL-dHonouredPark-2 — the build method's declared line budget rises to 350, and the byte half stays where it is

**Status:** CLOSED · rev-5 · 2026-08-25 · node d · Tier-1 · base 60ba1d60 · order 1 · streams tooling · ratified 2026-08-25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round1.md) | diff-review | TOOL-dHonouredPark-1 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |
| [2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round2-graded.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round2-graded.md) | diff-review | TOOL-dHonouredPark-1 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |
| [2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round3.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-diff-review-round3.md) | diff-review | TOOL-dHonouredPark-1 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md) | spec-audit | TOOL-dHonouredPark-1 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round2.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round2.md) | spec-audit | TOOL-dHonouredPark-1 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |
| [2026-08-26-review-TOOL-dHonouredPark-1-diff-review-round2.md](../reviews/2026-08-26-review-TOOL-dHonouredPark-1-diff-review-round2.md) | diff-review | TOOL-dHonouredPark-1 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/BUILD-METHOD.md` declares its own budget as ≤24 KB and ≤310 lines. Measured at BASE it
is 312 lines and 24126 B, so it stands two lines over the declared half. It was three over at
`dFramedEntrypoint`'s base and that build reduced it to two, which `.memory-tree.conf` records; rev-2
said it had been two over "since before" that build, which reversed the direction. The owner ruled the
line figure rises to 350.

The spec audit established what that ruling does and does not buy, and the difference is the reason
this unit is not one line of prose. 24576 − 24126 leaves 450 B. The mean over ALL 312 lines is 77 B,
but 72 of those lines are blank; the 240 lines that carry prose average 100 B, and a raise is spent on
prose. So 450 B buys about **four and a half** added lines and the byte half binds near line 316 —
call it four, not the six a whole-file mean suggests and not the forty the line figure suggests.

The owner was shown that arithmetic and ruled the byte cap stays at 24576. This unit therefore moves
one figure, records what the ruling costs, and adds the acceptance criterion that says which half
binds — because a budget with two halves and no statement of precedence is a budget nobody can plan
against.

Round 2 corrected the denominator: rev-2 divided by the whole-file mean and overstated the remaining
room by about 30%, in the record this unit exists to leave.

## 2. Scope (IN)

- **S1** — the budget sentence in `tools/memory-tree/BUILD-METHOD.template.md` declares ≤350 lines,
  edited in the TEMPLATE first with `memory/guides/BUILD-METHOD.md` re-rendered from it, because the
  parity harness renders live from template and editing the pair together inverts that direction.
- **S2** — the raise carries its reason inline, in the same sentence that carries the two previous
  movements: it is an owner call, dated 2026-08-25, and it is a raise rather than a trim.
- **S3** — the sentence states that adding a gate for the pair is a SEPARATE unruled question. It
  does NOT restate that no gate enforces the pair: the M1 budget passage of
  `tools/memory-tree/BUILD-METHOD.template.md` already carries "No gate enforces this pair, which is
  why exceeding it silently was the one option not taken." verbatim, wrapped across two lines, and
  `memory/guides/BUILD-METHOD.md` renders it identically. Only the unruled-question clause is new. An
  implementer reading this item as wholly new work would add a second sentence saying what already
  ships, into a file with no bytes to spare for it. Locate the clause by GREP, not by line number:
  rev-2 cited a line and cited the wrong one, which is the failure this item exists to prevent.
- **S4** — the byte half is UNCHANGED at 24576, by owner ruling of 2026-08-25, taken with the ~6-line
  arithmetic in front of them.
- **S5** — the sentence states WHICH HALF BINDS: the byte cap, because it is the one that runs out
  first at the file's current mean line length. This is the clause the audit found missing, and it is
  the only part of the ruling a future author actually has to plan against.
- **S6** — this unit prices its own read-path charge and moves `READ_PATH_CEILING` by it. At BASE the
  read path is 133673 B over 6 files against a ceiling of 133733 — **60 bytes** — and `corpus_ids.py`'s
  check 16 hard-fails on breach. The charge is measured before and after, and the ceiling is raised to
  the measured total plus **153 B**, with the reason recorded in `.memory-tree.conf`'s running
  narrative in the same commit.

  On 153: it is the margin the five most recent movements use, and the conf frames it explicitly as a
  DEPARTURE from the measure-plus-`READ_PATH_HEADROOM` jump the tool prints. rev-2 called it "the
  margin every prior movement uses", which is false — the earlier movements took the tool's jump. The
  narrower figure is chosen deliberately here, for the reason the conf already gives, and this item
  states that rather than inheriting it by assertion.
- **S7** — the charge includes this unit's `memory/DECISIONS.md` row. That file is itself a capped
  read-path member at 18096 B and the conf's own header records the previous raise as `+122` for ONE
  row. Pricing only the guide file was the audit's finding; the decision row is part of the same
  budget. AC7 asserts the row is inside the measured window, because §4 binds only the prose to the
  conf commit and a row landing after it would have to come out of the margin.
- **S8** — the STRANDED FRAGMENT is removed, and it pays for most of this unit. The M1 passage carries
  a headless sentence tail — "governance carrier and M3's veto 2 makes changing one an owner turn
  rather than an agent's." — left dangling when the 2026-08-21 raise rewrote the sentence it used to
  continue. It is about 92 B, roughly a fifth of the 450 B whose scarcity §1 is entirely about, and it
  reads as a fragment to anyone who reaches it. Removing it is not the trimming §3 forbids: that
  non-goal protects prose that says something, and this says nothing because its head is gone.
  Found by round 2, which also noted that rev-2 inventoried the passage twice without seeing it.

## 3. Non-goals (OUT)

- No gate for the pair. The owner ruled the raise and was told explicitly that it fixes the breach
  and not the blindness; adding a leg is a different decision nobody has taken.
- No trimming of method prose. The raise is the ruling; trimming would spend another build's content
  to make room the owner already granted.
- No movement of the byte cap, ruled 2026-08-25 after the ~6-line arithmetic was put to the owner.
- No change to M1's argument for having a budget at all.
- No raising of `READ_PATH_HEADROOM`. It is advice to an author and never an input to check 16, by
  the conf's own comment; moving it would change nothing this unit needs.

## 4. Design

### Data model

None. One declared figure and two clauses in one sentence.

### Inventory

The read path at BASE, from `python tools/memory-tree/corpus_ids.py --report`, 6 files totalling
133673 B: `UNATTENDED-PROTOCOL.md` 48838 · `SESSION-KICKOFF.md` 25358 · `BUILD-METHOD.md` 24126 ·
`DECISIONS.md` 18096 · `REVIEW-PROTOCOL.md` 15614 · `LIVE.md` 1641. This unit touches the third and
the fourth. The figures are recorded here as the BASE measurement this unit prices against, and are
re-derived rather than trusted at build time.

### Migration

The template is edited and the live copy re-rendered by
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. Adopters take the new figure on their
next kit update; nothing in an adopter's tree reds in the meantime, because no gate reads the pair.

`.memory-tree.conf`'s ceiling moves in the SAME commit as the prose that charges it. The file's own
convention is one recorded movement per charging unit — "each priced its own charge, which is why the
two movements above are recorded separately" — so this unit adds its own line to that narrative
rather than folding into a build-wide raise.

### Alternatives rejected

**Trimming to 310.** Offered to the owner and declined. It would have spent prose belonging to other
builds to stay under a figure the owner was willing to move.

**Adding the gate in the same unit.** Listed to the owner as one of three options at
`memory/builds/dFramedEntrypoint/RUN.md:37`, alongside trimming and raising. **No recommendation was
recorded**, and the dispositions record's ruling 3 says of the gate that nobody has been asked. The
rev-1 claim that it was "offered as the recommendation and declined" was contradicted by both records
this unit derives from and is withdrawn.

**Raising the byte cap to match.** Put to the owner with the ~6-line arithmetic and declined. Recorded
here because a future author reading a 350-line budget will ask why it does not fit.

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md` · `memory/guides/BUILD-METHOD.md` (re-rendered) ·
`.memory-tree.conf` for S6 · `memory/DECISIONS.md` for S7.

**NOT the kit version.** `check-verdict-epoch.sh` scans the engine and six named delegates, none of
them a `.template.md`, and `check-kit-versions.sh` asserts only that the constant and the markers
AGREE — so a template PROSE edit compels no bump. Taking one anyway would force re-renders of
`memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`, the other two pairs the dogfood-parity harness
checks, and reds the parity leg §7 names. rev-2 listed the bump; round 2 established it is both
unforced and under-scoped.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A. No mechanism ships.
- observability — none, and that is the point of S3: the pair remains unobserved, said out loud.
- risks — the read path, and it is priced rather than described. S6 carries the measurement and the
  ceiling movement; the rev-1 phrasing ("the delta is small but must be measured") named the risk
  without pricing it, which is what this build's own rules slot forbids.
- testing + left-shift gates — none new. The parity harness already asserts template and live agree.
- migration / rollback — one figure and two clauses, revertible; the ceiling movement inverts with it.
- user docs — the sentence is the doc.

## 6. Acceptance criteria

- **AC1** — When `memory/guides/BUILD-METHOD.md` is read at HEAD, its M1 budget sentence declares
  ≤350 lines and ≤24 KB, and names the raise as an owner call dated 2026-08-25.
- **AC2** — When `wc -l -c memory/guides/BUILD-METHOD.md` runs, the line count is at or under 350 and
  the byte count under 24576. **This criterion is green at BASE** (312 lines, 24126 B) and is kept as
  a regression guard, not as evidence the unit did anything — the criteria that can only pass after
  the edit are AC1, AC4 and AC5.
- **AC3** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, template and live agree.
- **AC4** — `memory/guides/BUILD-METHOD.md` M1 — its budget sentence states that adding a gate for the
  pair is unruled, AND states that the BYTE half is the binding one. Both clauses are absent at BASE,
  so this criterion has a failing state on an untouched tree; the "no gate enforces this pair" clause
  it does NOT add is already present at line 12 and must not be duplicated.
- **AC5** — When `python tools/memory-tree/corpus_ids.py --report` runs before and after, both totals
  are recorded in the commit message, `.memory-tree.conf` carries a new movement line naming this
  unit and its measured charge, and `READ_PATH_CEILING` equals the measured total plus 153.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, it is green including check
  16. Observed RED first by staging the prose edit WITHOUT the ceiling movement, which is the state
  the audit found this unit would otherwise land in.
- **AC7** — When `git show --stat` names the commit that moves `READ_PATH_CEILING`, that commit also
  carries this unit's `memory/DECISIONS.md` row. A row landing after the measured window would have to
  be absorbed by the 153 B margin, and the conf's own precedent prices one row at +122.
- **AC8** — When the M1 passage is read at HEAD, the headless sentence tail S8 names is gone, and
  `wc -c` records the bytes it returned.

## 7. Gates

`memory hygiene` (incl. check 16) · `kit/dogfood doc parity` · `check-kit-versions.sh` ·
`check-verdict-epoch.sh` · `method carriers`.

Guarded legs this unit's own diff trips, which rev-2 omitted: `memory-hygiene self-test` and
`verdict-epoch self-test` (guarded on `tools/memory-tree/`), and `dead-path carriers self-test` and
`python resolver` (guarded on `tools/`). Read from `tools/gate-legs.json`; the same class round 1
confirmed against unit 3.

## 8. Open questions

- **F1 — does THIS UNIT add a gate for the pair?** RESOLVED (agent, 2026-08-25, delegated) — no, which
  §3's first non-goal already states. The fork is decided for this unit and nothing here is left open.

  **Whether a gate is EVER added is a different question and it is PARKED, not resolved.** M3's veto 2
  puts a change to a governance carrier's own constraints outside the delegated mandate, and the budget
  pair is exactly that, so no resolver this run holds exists for it. The owner was asked about the line
  figure and the byte cap and was never asked this; the parent build's `RUN.md` records three options
  with no recommendation. The park carries it to the wrap-up.

  It is described here rather than quoted, and that is not fastidiousness. `plan_state` in
  `tools/unattended/unattended.sh` decides FORKED against READY by matching the stamp's pattern
  anywhere in this section's squeezed text, so rev-2's prose — which quoted the withdrawn stamp
  verbatim in order to withdraw it — re-asserted it. Measured: `--plan` printed this unit READY while
  its three siblings printed FORKED. The classifier cannot tell a quotation from an assertion, which is
  a defect in the classifier and is filed as its own backlog row; this spec simply stops writing the
  bytes that trip it.

## 9. Revision log

- rev-5 · 2026-08-25 · BUILT and CLOSED at b7366549. All eight criteria met; check 16 observed RED
  twice, once before each ceiling movement, the second forced by the manifest repair this unit's own
  watched files triggered.
- rev-4 · 2026-08-25 · M3 fork sweep. F1 split: whether THIS unit adds a gate is resolved (no, per
  §3), and whether one is ever added is PARKED under veto 2 as a governance-carrier change no
  delegated mandate reaches.
- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s second park.
- rev-3 · 2026-08-25 · round-2 fold. Corrected the mean-line denominator, which counted 72 blank lines
  and overstated the remaining room by ~30%. Stopped quoting the withdrawn resolution stamp, which
  `plan_state` was reading as an assertion and which had this spec classified READY while its siblings
  read FORKED. Corrected the 153 B claim (it is a deliberate departure from the tool's jump, not the
  convention every movement used) and the parent build's movement count (three attributed plus one
  unattributed, not two). Added S8 to remove a headless 92 B sentence tail that pays for most of this
  unit, and AC7/AC8 for the decision row and that removal. Dropped the kit-version bump as unforced and
  under-scoped, and named the guarded self-test legs this diff trips. Replaced line-number citations
  with grep-locatable names, after round 2 found rev-2's citation of the already-shipping clause was
  off by one line.
  AC numbering was RESEQUENCED in this revision; AC labels in the entries below refer to the
  numbering of the revision that wrote them, not to this one.

- rev-2 · 2026-08-25 · spec-audit fold. Priced the read-path charge and took the ceiling movement into
  scope (S6, S7, AC5, AC6) after the audit measured 60 B of headroom against a check that hard-fails.
  Added S5 and AC4's second clause on the owner's byte-cap ruling. Corrected S3: the first clause
  already ships verbatim and only the unruled-question half is new. Withdrew the false
  "offered as the recommendation" claim and the false `RESOLVED` stamp on F1. Marked AC2 as green at
  BASE rather than presenting it as evidence.

## 10. Reuse audit

Memory-recall terms for the regrounding read: `build method budget lines bytes owner call raise trim
governance carrier veto gate enforcement declared pair read path ceiling`. The seam is
`tools/memory-tree/BUILD-METHOD.template.md`'s own M1 sentence, which already carries two prior
movements with their reasons and is the only place the figure is stated — `check-method-carriers.sh`
asserts which files point AT the method, never what its budget is. No existing gate reads the
line/byte pair, which is the finding rather than a gap to fill here.

The second seam is `.memory-tree.conf`'s `READ_PATH_CEILING` narrative, which is the established
pattern for this unit's S6. The parent build left THREE unit-attributed movements there plus a fourth
for the owner rulings that names no unit — rev-2 said "two", having read a mid-narrative comment as the
total. Each carries its measurement and its reason. This unit joins that narrative rather than
inventing a form for it, and takes the 153 B margin the recent movements use rather than the tool's
printed jump, for the reason S6 gives.
