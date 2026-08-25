# TOOL-dHonouredPark-2 — the build method's declared line budget rises to 350, and the byte half stays where it is

**Status:** SPECCED · rev-2 · 2026-08-25 · node d · Tier-1 · base 60ba1d60 · order 1 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md) | spec-audit | TOOL-dHonouredPark-1 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/BUILD-METHOD.md` declares its own budget as ≤24 KB and ≤310 lines. Measured at BASE it
is 312 lines and 24126 B, so it has been two lines over the declared half since before
`dFramedEntrypoint` touched it. The owner ruled the line figure rises to 350.

The spec audit established what that ruling does and does not buy, and the difference is the reason
this unit is not one line of prose. 24576 − 24126 leaves 450 B; at the file's 77 B mean line that is
about 5.8 lines. **The byte half becomes binding at roughly line 318**, so the 40-line raise yields
about 6 usable lines. The owner was shown that arithmetic and ruled the byte cap stays at 24576. This
unit therefore moves one figure, records what the ruling costs, and adds the acceptance criterion
that says which half binds — because a budget with two halves and no statement of precedence is a
budget nobody can plan against.

## 2. Scope (IN)

- **S1** — the budget sentence in `tools/memory-tree/BUILD-METHOD.template.md` declares ≤350 lines,
  edited in the TEMPLATE first with `memory/guides/BUILD-METHOD.md` re-rendered from it, because the
  parity harness renders live from template and editing the pair together inverts that direction.
- **S2** — the raise carries its reason inline, in the same sentence that carries the two previous
  movements: it is an owner call, dated 2026-08-25, and it is a raise rather than a trim.
- **S3** — the sentence states that adding a gate for the pair is a SEPARATE unruled question. It
  does NOT restate that no gate enforces the pair: `BUILD-METHOD.template.md` line 12 already carries
  "No gate enforces this pair, which is why exceeding it silently was the one option not taken."
  verbatim, and `memory/guides/BUILD-METHOD.md` renders it identically. Only the unruled-question
  clause is new. An implementer reading this item as wholly new work would add a second sentence
  saying what already ships, into a file with no bytes to spare for it.
- **S4** — the byte half is UNCHANGED at 24576, by owner ruling of 2026-08-25, taken with the ~6-line
  arithmetic in front of them.
- **S5** — the sentence states WHICH HALF BINDS: the byte cap, because it is the one that runs out
  first at the file's current mean line length. This is the clause the audit found missing, and it is
  the only part of the ruling a future author actually has to plan against.
- **S6** — this unit prices its own read-path charge and moves `READ_PATH_CEILING` by it. At BASE the
  read path is 133673 B over 6 files against a ceiling of 133733 — **60 bytes** — and
  `corpus_ids.py:450-457` is check 16, which hard-fails on breach. The charge is measured before and
  after, and the ceiling is raised to the measured total plus the 153 B margin every prior movement in
  `.memory-tree.conf` uses, with the reason recorded in that file's running narrative in the same
  commit.
- **S7** — the charge includes this unit's `memory/DECISIONS.md` row. That file is itself a capped
  read-path member at 18096 B and the conf's own header records the previous raise as `+122` for ONE
  row. Pricing only the guide file was the audit's finding; the decision row is part of the same
  budget.

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
`.memory-tree.conf` for S6 · `memory/DECISIONS.md` for S7 ·
`tools/memory-tree/check-memory-hygiene.sh` and the three template markers for the kit version.

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

## 7. Gates

`memory hygiene` (incl. check 16) · `kit/dogfood doc parity` · `check-kit-versions.sh` ·
`check-verdict-epoch.sh` · `method carriers`.

## 8. Open questions

- **F1 — does the pair get a gate?** UNRULED, and deliberately left so. The owner was asked only about
  the budget figure and the byte cap; the gate was never put to them, and `RUN.md:37` records three
  options with no recommendation. rev-1 carried a `RESOLVED (owner, 2026-08-25)` stamp on this
  question while its own text said the question stays unruled — a contradiction that was also
  load-bearing, because `plan_state`'s regex at `unattended.sh:1432` reads that mark over the whole
  section and flipped this spec from FORKED to READY on a resolution nobody made. The stamp is
  withdrawn.

## 9. Revision log

- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s second park.
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
pattern for this unit's S6: it already records two movements from the parent build, each attributed to
the unit that charged it, each carrying its measurement and its reason, each keeping the same 153 B
margin. This unit joins that narrative rather than inventing a form for it.
