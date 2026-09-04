# TOOL-aSurfacedLexicon-12 — the conf rewrite, the owed records, and the spec-template cell line

**Status:** SPECCED · rev-5 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 7

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close the rebuild: replace the declaration's pin archaeology with the row-shaped block the tool emits,
write the three records owner ruling Q9 owes, settle the kill-rule arithmetic on its single carrier per
owner ruling Q8, and add the one spec-template line that names a minted identifier's cell. Everything
here is bookkeeping the code cannot do for itself, and every item is a thing a later reader would
otherwise find as a contradiction rather than a record.

## 2. Scope (IN)

- **S1** — Rewrite `.lexicon.conf`'s pin region. Measured at base `6c670b02`: the file is 216 lines
  (`wc -l .lexicon.conf`) of which 178 are comments (`grep -cE '^#' .lexicon.conf`), and 139 of those
  comments sit in the single region between the `LANGS=` line and `VERB_OFFENDER_PIN=`, lines 24
  through 163 (`awk 'NR>=24 && NR<=163' .lexicon.conf | grep -cE '^#'`). That region is eleven recorded
  pin moves with hand-written name lists. It goes, replaced by the `PINS:` block that
  `python tools/lexicon/lexicon.py --measure` emits whole. Git keeps every byte.
- **S2** — Record (a): a supersession of `TOOL-dScaffoldedMirror-18`, live at `memory/DECISIONS.md:100`,
  which instructs a reader to build a grandfather backfill for a pressure chain this rebuild does not
  build. The supersession was recorded as owed by that build's own round-2 review and never written.
- **S3** — Record (b): an id recording that the per-surface convention ruling REVERSES the earlier
  casing refusal. That refusal lives only in a build record today and would be a supersession nobody
  finds. It is the easy kind to argue: the refusal promised a compensating README line telling adopters
  to wire their own linter, and no such line exists, so the reversal closes an uncovered gap rather than
  overriding a covered exemption.
- **S4** — Record (c): an id for the P3 removal with its compensating check, which is the source scan
  asserting no `tools/lexicon/*.py` imports `codebase-map`, on the `lexicon naming predicates` leg.
- **S5** — Owner ruling Q8. `build_lexicon_marginal_offense_rate`'s docstring at
  `tools/drift-audit/drift_report.py:945` becomes the SOLE carrier of the kill-rule arithmetic. The
  record copies are superseded in place, additively, and the count of them is corrected below.
- **S6** — The arithmetic itself, stated once so the correction is unambiguous. The docstring requires
  the fresh-file rate to stay at or below roughly 5% across two FURTHER readings. The first reading was
  4.3%. Today's reading is 3.6%, being 5 of 138 from
  `python tools/drift-audit/drift_report.py --json` as measured by the research pass. That makes today
  the FIRST of the two further readings, so a THIRD reading is owed before the pressure chain is
  abandoned.
- **S7** — The three carriers of `TOOL-dClosedLexicon-2`'s status agree. Measured at writing time they
  give three different answers: `memory/map/features/lexicon.md:166` says BLOCKED,
  `memory/backlog/TOOL.md:118` says SPECCED, and the spec's own header at
  `memory/builds/dClosedLexicon/spec/2026-08-16-spec-dClosedLexicon-2.md:3` says CLOSED. The map
  wiring it describes is live — `memory/map/generated/inventories.json` carries 23 `lexicon-verbs`
  keys — so CLOSED is the true reading and the other two are corrected to it.
- **S8** — The spec-template line. A spec names each identifier it will mint together with its cell, and
  cites the surface-aware suggest invocation where a name was refused. One line, in §4's already
  canonical `### Inventory` sub-head, deliberately ungated.
- **S9** — That line lands in BOTH `tools/memory-tree/SPEC-TEMPLATE.template.md` and its rendered copy
  `memory/TEMPLATE-SPEC.md`. The pair is byte-compared by `tools/memory-tree/kit-dogfood-parity.test.sh`
  at `:53` and `:114`, so a one-sided edit reds the `kit/dogfood doc parity` leg.
- **S10** — The `ratified=` stamp in `.lexicon.conf` is re-stamped in the same commit as any `LANGS=`
  edit, or `signal_lexicon_ratified_stale` at `tools/drift-audit/drift_report.py:846` fires.
- **S11** — The charter's `kit:lexicon` conditional block describes the tool this build actually
  ships. Measured at writing time it names three things — a closed verb table, a banned type-suffix
  list and forbidden import directions — of which the third is DELETED by
  `TOOL-aSurfacedLexicon-2` and the other two are no longer the whole surface. It gains the
  (language, surface) cell matrix, the convention predicate, the prefix selector and the canon
  unfreeze stamp. Without this the charter's naming bullets survive the build describing a tool that
  no longer matches the kit, which is the two-answers-to-one-question class on the document that
  states the rule against it.
- **S12** — S11 is paid for out of the bytes `TOOL-aSurfacedLexicon-2` frees, not out of the
  template's headroom. Measured at writing time `bash tools/check-template-size.sh` reports 48867 of
  49152 bytes with 285 free and already WARN past its recorded high-water, so the ceiling is an owner
  decision and this unit may not spend into it. The order is load-bearing: S11 is written only after
  the P3 deletion has landed, and if the net is positive the fix is to trim the block's
  non-instructional prose rather than to raise the ceiling.
- **S14** — THE `CELLS` MATRIX, AND THE PROMOTION IT CARRIES. `TOOL-aSurfacedLexicon-6` states this
  as an OWED ITEM rather than a routing, on the ground that no sibling spec had ever accepted it —
  measured there by grepping the set, and reproduced here: before this revision `grep -c CELLS` over
  this file returned 0. This unit accepts it, because it is the unit that rewrites the declaration
  and there is no other candidate at any build order. Three obligations, in the receiving unit's
  words as that spec wrote them. Write the full `CELLS` matrix into `.lexicon.conf`. Set
  `UNDECLARED_CELL_ARMED = True` in `tools/lexicon/lexicon.py` in the SAME commit, so the report-only
  arm that unit landed dark becomes a refusal on the commit that makes it satisfiable. PRESERVE that
  unit's `py.constant` row and its population comment. A matrix that lands with the constant left
  off ships an arm that reports and can never refuse, which is the land-dark-then-flip rule with its
  second half missing — and `TOOL-aSurfacedLexicon-5` and `TOOL-aSurfacedLexicon-9` both already
  name this unit as the owner, so declining it would leave two specs pointing at nothing.
- **S13** — The `PINS:` block this unit pastes is emitted and committed BLANK-SEPARATED: exactly one
  blank line between every pin row. That whitespace IS the merge property under
  `TOOL-aSurfacedLexicon-4`'s ratified F1, not a formatting preference, so a later tidying edit that
  closes the gaps silently removes it. The property is narrower than it sounds and this unit records
  the bound rather than inheriting a comfortable reading of it: blank separation survives
  drain-vs-drain, and does NOT survive drain-vs-INSERT — a drain against an insertion after the same
  row still exits 1 with one conflict marker, which is the edit shape every cell-arming commit
  produces. Whichever unit emits the block emits it blank-separated; nothing here claims the
  insertion case away.

## 3. Non-goals (OUT)

- **Not taking the third reading.** S6 records that one is owed and what it would decide. Taking it is
  a measurement against a later window and belongs to whoever is standing there when the window is
  wide enough to mean something.
- **Not wiring the cell line into `tools/memory-tree/check-memory-hygiene.sh`.** See §4 for the
  compensating check and the precedent.
- **Not renaming the seven hyphenated Python filenames.** Owner ruling Q3 ships `py.file` armed at a
  pin of 7 and files the renames as their own unit.
- **Not editing `memory/HYGIENE.md`.** It carries zero lexicon references today
  (`grep -c -i lexicon memory/HYGIENE.md`) and this unit gives it none.
- **Not abandoning the pressure chain.** S6 settles which reading today is, not what to do about it.
- **Not deleting any prose copy.** The corrections are additive notes beside the quoted claims.

## 4. Design

### The conf rewrite

The pin archaeology exists because a one-sided pin carries no machine-readable previous value, so every
move had to be narrated. Under owner ruling Q2 the pins become two-sided and per-cell, and
`python tools/lexicon/lexicon.py --measure` emits the whole `PINS:` block, so the successor to 139 lines
of narration is a block the tool writes and a human pastes. What survives from the region is the small
number of comments that state a DECISION rather than a history: the boundary between what the owner
declares and what the kit owns, the note on the seven Python filename offenders that owner ruling
Q3 pins rather than waives, and the `py.constant` population comment carrying all three measured
readings that owner ruling Q6 requires, each with the reading that produced it. **THE FIGURES ARE
THAT UNIT'S, NOT THIS ONE'S, and this spec carried the wrong ones until now.** Rev-3 reproduced a
triple of 527 against 419, 432 against 413, and 331 against 331; `TOOL-aSurfacedLexicon-6` re-measured
at this base and its AC5 asserts 544 against 436, 449 against 430, and 346 against 346, with the
counting rule stated beside them — the earlier triple was taken at the pre-rebase tree. Preserving the
comment as rev-3 quoted it would have preserved numbers that RED the selftest arm this unit is
preserving them for. This unit copies whatever that unit's arm asserts at the time it lands, rather
than restating a triple here that can go stale again; the figures above are shown to say WHICH ones
were wrong, not to become a second carrier. Its first row disagreed with the research record's 539;
`TOOL-aSurfacedLexicon-6` declares that reconciled and withdrawn at its rev-3, so this spec no longer
carries it as UNRECONCILED.

The row shape is not cosmetic here. Owner ruling Q2 makes the pins two-sided, so a correct rename blocks
the bar until a second commit edits the pin, and two nodes each draining one name would produce a
conflicting single-line edit in a shared mutable scalar. Through rev-3 this section said that a
row-shaped block reconciles under this repo's existing row merge driver the way the backlogs do. That
was WRONG, and it is corrected rather than hedged. `.lexicon.conf` carries no merge attribute —
`git check-attr merge -- .lexicon.conf` prints `unspecified`, and `grep -n "merge=" .gitattributes`
returns five hits of which only two are declarations, the append-only decision log at `:61` and the
backlogs at `:62`; the other three are that file's own comment prose. The driver's row predicate
matches a markdown bullet (`grep -n "_ROW_RE = " tools/memory-tree/merge-rows.py` puts it at `:252`),
so an indented conf row is classified as STRUCTURE and handed to a positional three-way merge. Wired
up and run against the shipped driver, the attribute produced `1 structure conflicts, CONFLICT` with
`rows O/A/B 0/0/0 -> 0 written (0 keyed, 0 hashed)` — zero rows keyed, exit 1.

`TOOL-aSurfacedLexicon-4` ratified a different mechanism for the same property: a single blank line
between pin rows. Measured on this worktree by that unit's F1 resolution, two branches draining
ADJACENT cells merge at exit 0 with zero conflict markers where the dense block exits 1 with one
marker. The mechanism belongs to that unit, which builds the block; this unit only pastes the measured
values into it, blank-separated per S13.

### The records, and how a supersession is written here

`memory/DECISIONS.md` is append-only: a ratified record is never rewritten, it is superseded by a new id
with a note. The three records get new ids in the `TOOL` family under this build's slug, allocated by
the building session as a plain 1-up above its own high-water, which is why no id is pinned in this
spec — the unit roster already reaches 13 and an id typed here would contest one.

The convention for correcting a claim in a landed record is established at
`memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-7.md:279`: this repo supersedes
a ratified claim by QUOTING it beside its supersession, which is why an absence grep would have forced
the one edit shape the convention forbids. The Q8 corrections follow that shape.

### Inventory — the Q8 carriers, measured rather than inherited

The rulings record names two prose copies plus the build README line. Run at writing time,
`grep -rn "two further readings" memory/ tools/ --include=*.md --include=*.py` finds the claim in the
docstring plus THREE record files, and the rulings record's own text is a fourth hit that is not a
carrier:

| Carrier | What it says today |
|---|---|
| `tools/drift-audit/drift_report.py` | two further readings — the sole carrier under owner ruling Q8 |
| `memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-7.md` | two further readings, twice |
| `memory/builds/dScaffoldedMirror/build/2026-08-25-build-TOOL-dScaffoldedMirror-7.md` | two further readings — a carrier neither the research record nor the rulings record named |
| `memory/builds/dScaffoldedMirror/README.md:121` | reading one of two, which is the line that disagrees |

Each of the three record carriers gains a supersession note beside its claim, pointing at the docstring
and stating that today's 3.6% is the first of the two further readings.

### Migration

None mechanical. The conf rewrite is a content edit whose result the reader parses or refuses; the
records are appends; the template line is a two-file edit under a byte-compare.

### Rollout

Nothing lands dark. The conf rewrite is the last of this build's declaration changes and is expected to
land after the units that give the `PINS:` block its grammar.

One ordering hazard is RECORDED here rather than resolved, so neither implementer trips it. This unit
is build order 7 and `TOOL-aSurfacedLexicon-10` is order 6, and that unit's S7 has `--expand` tell the
operator that the `PINS:` block must be re-measured and re-pasted — a block that does not exist in
`.lexicon.conf` until this unit lands. The grammar is not the problem; `TOOL-aSurfacedLexicon-4`
supplies it at order 2. The pasted block is. So unit 10's message must read correctly against a conf
carrying no `PINS:` block, the same way its `expanded=` guard already reads an absent key as empty,
and this unit must not assume unit 10 has pasted one.

### Files touched (estimate)

- `.lexicon.conf` — the region rewrite, the pasted `PINS:` block, the re-stamp.
- `memory/DECISIONS.md` — three appended rows.
- `memory/backlog/TOOL.md` — the `TOOL-dClosedLexicon-2` row's status, and any rows the three records
  close.
- `memory/map/features/lexicon.md` — the BLOCKED claim about the map wiring.
- `memory/builds/dScaffoldedMirror/README.md`, its spec 7, and its build record 7 — three supersession
  notes.
- `tools/memory-tree/SPEC-TEMPLATE.template.md` and `memory/TEMPLATE-SPEC.md` — the one line, both
  sides.

### Alternatives rejected

**Gating the spec-template line in hygiene check 12.** The governing precedent is
`memory/HYGIENE.md`'s own treatment of an adjacent kit: hygiene SANCTIONS a neighbouring kit's files
and refuses to enforce that kit's rules, because the map's coverage and freshness enforcement is its own
test file and not that script. The cautionary measurement is §10's own reuse audit, the only
prose-graded arm this repo has built: it needed its probe half truncated at the first terms marker,
end-of-line truncation was tried and leaked, and `memory/TEMPLATE-SPEC.md` still admits an open hole
where one line can satisfy both arms. A second prose-graded arm would be a weaker grader of a question
the code predicate already answers on the real definition site. **The compensating check for that
exemption is the gate itself**: the identifier is graded the day it exists in code, which is a stronger
claim than a spec bullet can make. If teeth are wanted later, the precedented shape is a sixth dated
cutoff in check 12 beside the five that exist, grading SHAPE only — that a bullet names a cell, never
that the cell exists.

**Editing only `memory/TEMPLATE-SPEC.md`.** That is what the research record's one-line description
implies and it is half the edit. `tools/memory-tree/adopt-memory-tree.sh:90` renders that file from
`tools/memory-tree/SPEC-TEMPLATE.template.md`, so a rendered-only edit is overwritten on the next adopt
and reds `kit/dogfood doc parity` before then.

**Deleting the disagreeing prose copies.** Rejected by this repo's own convention, and by the fact that
the deletion leaves a reader who remembers the old claim with nothing to reconcile against.

## 5. Production-readiness checklist

- security — N/A. No executable path changes; every edit is declaration or record content.
- perf / scale — the conf shrinks, so the reader does less work. Not measured, because the parse is
  already far below the leg's declared 300 s ceiling.
- a11y — N/A, no user interface.
- i18n — N/A, records are English by convention here.
- error / empty / loading states — the rewritten conf must still parse and still ratify:
  `bash tools/lexicon/adopt-lexicon.sh --check` is the arm that catches an over-enthusiastic deletion,
  and it reds on an empty `ratified` value.
- observability — `python tools/drift-audit/drift_report.py` is the instrument that says whether these
  records still describe the tree, and S7 exists because it currently would not.
- risks (concurrency, data-loss, rollback hazards) — the real one is deleting a comment that carried a
  decision rather than a history. Mitigated by keeping the boundary comment and the Q3 filename note,
  and by the fact that git keeps every deleted byte.
- testing + left-shift gates — no new predicate, so no new failing case to stage. The pin-block
  round-trip in AC2 is the one observation with a staged break.
- migration / rollback — every edit is revertable as one commit; the conf rewrite is the only one whose
  revert would matter and it is self-contained.
- user docs — `.lexicon.conf`'s own comments are the user doc for the declaration, and the template line
  is the user doc for the spec integration.

## 6. Acceptance criteria

- **AC1** — When the rewrite has landed, `wc -l .lexicon.conf` is smaller by at least the 139 comment
  lines measured in lines 24 through 163 at base `6c670b02`, and
  `python tools/lexicon/lexicon_conf.py --print-verbs .lexicon.conf` still prints the same 23 rows.
- **AC2** — When `python tools/lexicon/lexicon.py --measure` is run, its emitted `PINS:` block is
  byte-identical to the block committed in `.lexicon.conf`; staging a one-digit edit to any pin row
  makes `python tools/lexicon/lexicon.py` exit non-zero, and unstaging it greens. The RED is observed.
- **AC3** — When `grep -n "TOOL-aSurfacedLexicon" memory/DECISIONS.md` is run, three new rows are
  present: the supersession of `TOOL-dScaffoldedMirror-18`, the casing-refusal reversal, and the P3
  removal with its compensating check named.
- **AC4** — When `grep -rn "two further readings" memory/ tools/` is run, the docstring in
  `tools/drift-audit/drift_report.py` is present and each of the three record carriers listed in §4
  carries a supersession note beside its claim naming that docstring as the sole carrier.
- **AC5** — When `grep -n "reading one of two" memory/builds/dScaffoldedMirror/README.md` is run, the
  line is still there and is followed by its correction: today's 3.6% is the first of the two further
  readings, so a third is owed.
- **AC6** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` is run after the template line
  lands, it exits 0. Staging the line into `memory/TEMPLATE-SPEC.md` alone makes it exit non-zero
  first, which is the observed RED for the two-file rule.
- **AC7** — When `grep -c -- "--as" memory/TEMPLATE-SPEC.md` is run, it is at least 1, and the hit sits
  in the `### Inventory` bullet of the recurring sub-heads.
- **AC8** — When the three `TOOL-dClosedLexicon-2` carriers are read,
  `memory/map/features/lexicon.md` no longer calls it BLOCKED, `memory/backlog/TOOL.md` no longer calls
  it SPECCED, and the spec header still reads CLOSED.
- **AC9** — When any `LANGS=` edit lands without a `ratified=` re-stamp in the same commit,
  `python tools/drift-audit/drift_report.py` reports `signal_lexicon_ratified_stale`; with the re-stamp
  it does not. Both observed.
- **AC10** — When `bash tools/memory-tree/check-memory-hygiene.sh` is run over the tree with all of the
  above in place, it exits 0.
- **AC11** — When the charter's `kit:lexicon` block is updated per S11, `grep -c 'forbidden import'
  coding-governance-agents.template.md` is 0 and the block names the cell matrix, the convention
  predicate, the selector and the unfreeze stamp. `bash tools/check-placeholders.sh` stays green, so
  no new `{{TOKEN}}` is introduced without a deploy-time substitution.
- **AC12** — When S11 has landed, `bash tools/check-template-size.sh` reports a byte count at or
  BELOW the count it reported after `TOOL-aSurfacedLexicon-2`'s deletion, and does not WARN past a
  new high-water. Both readings are recorded in this unit's acceptance ledger, because a budget
  claim with one reading is an assertion.
- **AC14** — When the commit landing S14 is read, `.lexicon.conf` carries a `CELLS` block and
  `tools/lexicon/lexicon.py` carries `UNDECLARED_CELL_ARMED = True`, in THAT SAME commit — asserted
  by a check over the commit rather than over the tree, because the two landing separately is the
  exact failure S14 exists to prevent and a tree-scoped check cannot see it. `python
  tools/lexicon/lexicon.py --check` is then green on the tracked tree, which is the armed run
  `TOOL-aSurfacedLexicon-6` requires observed before landing, and the `py.constant` row and its
  population comment are still present. The RED half is observed too: with the matrix landed and the
  constant left at its default, the undeclared-cell arm prints and does not refuse, and that is
  recorded as the failing case rather than assumed.
- **AC13** — When the rewritten `.lexicon.conf` is read, every consecutive pair of `PINS:` rows is
  separated by exactly one blank line, and `python tools/lexicon/lexicon_conf.py --print-verbs
  .lexicon.conf` still parses the file. The merge property that separation buys is
  `TOOL-aSurfacedLexicon-4`'s AC5 and is deliberately not re-asserted here; what this criterion
  observes is that the block as COMMITTED still carries the shape that arm assumes.

## 7. Gates

- `lexicon wiring` — guard `[]`, ceiling 330 in `tools/gate-legs.json`. Fires on the conf-only diff and
  is what catches a rewrite that broke the parse or the ratification.
- `lexicon naming predicates` — chunk `declarations`, ceiling 300. Carries the pasted pins and the P3
  compensating check that record (c) names.
- `kit/dogfood doc parity` — its guard in `tools/memory-tree/kit.toml:136` names
  `{memory_root}/TEMPLATE-SPEC.md`, so it selects itself on the S9 edit and is the leg that enforces the
  two-file rule.
- The memory-tree hygiene leg, for the three records, the backlog edit and this spec.
- `drift-audit records` and the drift-audit selftest, for the ratified-stale signal and the map dossier
  edit.

No new bar leg, so no wall-clock ceiling and no `memory/project/testsuite-count-waivers.txt` row is
owed. That registry is shrink-only and a row naming a compliant suite reds as stale, so adding one
speculatively would be a defect rather than caution.

## 8. Open questions

- **Q8 is not open.** RESOLVED (owner, 2026-09-04): `tools/drift-audit/drift_report.py` is the sole
  carrier of the kill-rule arithmetic, the prose copies are superseded, and one more reading is owed
  before the pressure chain may be abandoned.
- **Q9 is not open.** RESOLVED (owner, 2026-09-04): all three owed records get written in this build.
- **F1 — does the spec-template line ship to every memory-tree adopter, or only to one that has the
  lexicon kit?** `tools/memory-tree/SPEC-TEMPLATE.template.md` is a `rendered` file with placeholders,
  and it ships to adopters most of whom carry no lexicon at all. An unconditional sentence naming a
  cell and a suggest invocation is an instruction pointing at a tool the reader may not have, which is
  the exact defect a prior review found when another kit's doc named the lexicon unconditionally.
  A conditional block costs the renderer a new conditional and the descriptor a new placeholder.
  Recommendation: word the line so it is a no-op without the kit — name the cell as an optional
  qualifier on an identifier a spec already had to list — rather than adding renderer machinery for one
  sentence. State plainly in the record that this is a wording workaround and not a conditional, so the
  next person adding a kit-conditional line to this template does not read it as a precedent.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against owner rulings Q8 and Q9 of the same date.
- rev-2 · 2026-09-04 · cross-spec audit. The conf-rewrite survivor list named two decision comments
  and dropped a third: `TOOL-aSurfacedLexicon-6` S5 writes the Q6 `py.constant` population comment into
  the same region at build order 4 and gates it with an AC5 selftest arm, so this rewrite at order 7
  would have deleted an artifact another unit's acceptance asserts.
- rev-3 · 2026-09-04 · the charter gap closed. The cross-spec audit found that no spec updated §12's
  `kit:lexicon` block, so the charter would have survived the build describing a tool that no longer
  matches the kit. S11 writes the block, S12 binds it to the bytes the P3 deletion frees rather than
  to the template's 285 free bytes, and AC11 and AC12 gate both halves.
- rev-4 · 2026-09-04 · the merge-driver claim REFUTED and the base re-pinned. §4 said a row-shaped
  `PINS:` block reconciles under this repo's row merge driver the way the backlogs do; wired up and
  run, the driver printed `1 structure conflicts, CONFLICT` with zero rows keyed, because
  `.lexicon.conf` carries no merge attribute and `_ROW_RE` matches a markdown bullet. The mechanism
  that does deliver the property is `TOOL-aSurfacedLexicon-4`'s ratified F1 — one blank line between
  pin rows — and this spec was the last carrier still saying otherwise. S13 now requires the block to
  be emitted blank-separated and records that the property covers drain-vs-drain only, so every
  cell-arming commit still conflicts; AC13 observes the committed shape. The Rollout sub-head gains
  the order-6-before-order-7 hazard, `TOOL-aSurfacedLexicon-10`'s `--expand` message naming a `PINS:`
  block that does not exist until this unit lands. Base re-pinned from `d0a18683` to the run's base
  `6c670b02` in the status header, S1 and AC1, because all three S1 figures reproduce there:
  `wc -l < .lexicon.conf` is 216, `grep -cE '^#' .lexicon.conf` is 178, and
  `awk 'NR>=24 && NR<=163' .lexicon.conf | grep -cE '^#'` is 139, all unchanged.
- rev-5 · 2026-09-04 · this unit ACCEPTS the matrix and the promotion `TOOL-aSurfacedLexicon-6` stated as an
  OWED ITEM, as S14 and AC14; it is the unit that rewrites the declaration and there was no other
  candidate at any build order, and two siblings already named it as owner. AC14 asserts the matrix
  and the arming constant land in the SAME commit, over the commit rather than over the tree,
  because a tree-scoped check cannot see them landing separately. Separately: this spec reproduced
  the `py.constant` triple from the pre-rebase tree, so preserving the comment as written would have
  preserved numbers that RED the selftest arm it is preserved for. It now copies whatever that
  unit's arm asserts instead of carrying a second copy that can go stale again.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "supersede a ratified decision record and correct a number
that two prose copies restate"` returns no seam this unit can use, and that is the expected answer for a
records unit. Its ranked candidates are the record readers rather than any writer: `records` in
`tools/memory-tree/gotchas.py` at fan-in 2, `extract_records` and `zero_record_diagnosis` in
`tools/memory-recall/extract.py` at fan-in 1 each, and
`test_dossier_prose_headings_pinned` in `tools/codebase-map/test_codebase_map.py`. Nothing in this repo
WRITES a decision record programmatically, by design — the log is append-only and hand-authored, and a
generator for it would be the authored-status defect one level up. No existing seam fits. The two seams
this unit does depend on were found by reading source: the render-and-byte-compare pair at
`tools/memory-tree/kit-dogfood-parity.test.sh:53`, which is what makes the template line a two-file
edit, and `signal_lexicon_ratified_stale` at `tools/drift-audit/drift_report.py:846`, which is what
makes the re-stamp mandatory in the same commit as a `LANGS=` edit.

Recall terms used: `python tools/memory-recall/query.py "what does the kill rule require before the
lexicon pressure chain can be abandoned and where is its arithmetic carried" --terms "kill rule
marginal offense rate fresh-file arm two further readings pressure chain pin drift_report carrier
supersede prose copy"`.
