# TOOL-aSurfacedLexicon-12 — the conf rewrite, the owed records, and the spec-template cell line

**Status:** CLOSED · rev-9 · 2026-09-05 · node a · Tier-2 · base 6c670b02 · streams tooling · order 7 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aSurfacedLexicon-8-acceptance-ledger.md](../build/2026-09-05-build-TOOL-aSurfacedLexicon-8-acceptance-ledger.md) | journal | TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-8 |
| [2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-11 |
| [2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-8-spec-audit-round2.md) | spec-audit | TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-11 |

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
  pin moves with hand-written name lists — eleven by a loose read of the region and TEN by the strict
  head-anchored form AC1 uses, which is why AC1 states its own predicate rather than inheriting this
  count. Both are measurements of the same region under different regexes and neither is wrong; a
  criterion keyed to the looser number would fail against the stricter grep it names. It goes,
  replaced by the `PINS:` block that
  `python tools/lexicon/lexicon.py --measure` emits whole. Git keeps every byte.
- **S2** — Record (a): a supersession of `TOOL-dScaffoldedMirror-18`, live at `memory/DECISIONS.md:100`,
  which instructs a reader to build a grandfather backfill for a pressure chain this rebuild does not
  build. The supersession was recorded as owed by that build's own round-2 review and never written.
- **S3** — Record (b): an id recording that the per-surface convention ruling REVERSES the earlier
  casing refusal. That refusal lives only in a build record today and would be a supersession nobody
  finds. It is the easy kind to argue: the refusal promised a compensating README line telling adopters
  to wire their own linter, and no such line exists, so the reversal closes an uncovered gap rather than
  overriding a covered exemption.
- **S4** — Record (c): an id for the P3 removal with its compensating check, on the
  `lexicon naming predicates` leg. The check is QUOTED from `TOOL-aSurfacedLexicon-2`, which owns
  it, rather than paraphrased: "Every non-relative import in a `.py` file sitting beside
  `lexicon.py` names either a stdlib top-level module or another `.py` file in that same
  directory." That unit records it as "stronger than the deleted rule, because it refuses any
  foreign kit rather than one named directory", and it carries no hand-kept name list. Rev-5 of
  this spec called it "the source scan asserting no `tools/lexicon/*.py` imports `codebase-map`",
  which is wrong twice over: it is the narrow named-directory rule unit 2 REPLACED, and unit 2
  rejects the mechanism the word "scan" implies — the check "judges IMPORT STATEMENTS through
  `extract`, never file text", a whole-file text search being the
  `memory/gotchas/absence-assertion-over-whole-file-text.md` class that "would fire here on its own
  documentation". This wording lands in append-only `memory/DECISIONS.md`, where the only correction
  is a supersession, so the quote is load-bearing rather than tidy.
- **S5** — Owner ruling Q8. `build_lexicon_marginal_offense_rate`'s docstring becomes the SOLE
  carrier of the kill-rule arithmetic. The cite is SYMBOL-ANCHORED, because rev-5 pointed at
  `tools/drift-audit/drift_report.py:945`, which is a blank line; measured at `bb03dda4`,
  `grep -n "def build_lexicon_marginal_offense_rate" tools/drift-audit/drift_report.py` puts the
  definition at `:946` and the docstring opens at `:947`. The record copies are superseded in
  place, additively, and the carriers are enumerated by measurement in §4 rather than counted here.
  The supersession notes are deliberately ID-LESS, and that is a decision rather than an omission.
  The rulings record routes the Q8 prose corrections into Q9's record (a), and record (a) is the
  `TOOL-dScaffoldedMirror-18` supersession per S2 — a different subject. Filing a kill-rule
  correction under an id whose record is about a grandfather backfill would make the append-only log
  harder to read, not easier, so the corrections ride the note-beside-the-quoted-claim convention
  §4 cites and this bullet is where the routing is declined rather than silently inherited.
- **S6** — THE ARITHMETIC, RE-DERIVED AT THIS REVISION, AND THE RULING INVERTS. The docstring at
  `tools/drift-audit/drift_report.py:947` carries TWO branches, not one: a fresh-file rate that
  stays at or below roughly 5% across two FURTHER readings ABANDONS the pressure chain, and "a rate
  that CLIMBS in fresh files across two readings" is the evidence `TOOL-dScaffoldedMirror-9` was
  missing and "promotes it from probation to scheduled". Rev-5 quoted only the first branch, which
  is why it could reach only one conclusion.
- **S6a** — The reading, and the ONE command that prints it:
  `python tools/drift-audit/drift_report.py --json`, read on the `lexicon_marginal_offense_rate`
  signal's fresh-file arm — the arm whose own note reads "files written FRESH in the window — the
  reading the kill-rule watches". Re-run on 2026-09-05 at head `2d487019` it prints `added 340`,
  `offenders 181`, `rate_pct 53.2`, which is far ABOVE the roughly 5% bar. Those are the figures the
  four supersession notes assert and the figures AC4 grades against; no figure in this spec is a
  value to paste into a record, since every record takes the reading at ITS OWN landing commit from
  that same command. Two superseded readings are quoted here rather than deleted, which is this
  repo's convention: rev-5 stated 3.6%, being 5 of 138 — both operands wrong, the 138 being the
  research pass's coverage count rather than the arm's `added` — and rev-6 stated 10.6%, being 15 of
  142 at `bb03dda4`, which was the arm's own reading on a tree this build has since rewritten.
  Neither is continued.
- **S6b** — What the reading decides, and what it does not. It does not CONTINUE the abandon chain,
  it BREAKS it: today is not the first of two further readings, and no third reading is owed under
  that branch. The recorded prior reading is 4.3%, being 5 of 117 at
  `memory/builds/dScaffoldedMirror/build/2026-08-25-build-TOOL-dScaffoldedMirror-7.md:18`, so on the
  docstring's own words 4.3% then 53.2% is the CLIMB branch and not the abandon branch. This unit
  RECORDS that and does not act on it; the promotion it implies is a decision with its own scope
  (§3). Every figure this unit writes into a record is the one
  `python tools/drift-audit/drift_report.py --json` prints AT THE LANDING COMMIT, not one carried
  from this spec — the reading in S6a is what inverted the ruling, not a value to paste.
- **S7** — The three carriers of `TOOL-dClosedLexicon-2`'s status agree. Measured at writing time they
  give three different answers: `memory/map/features/lexicon.md:166` says BLOCKED,
  `memory/backlog/TOOL.md:121` says SPECCED (rev-5 cited `:118`, which is a
  `TOOL-cBriefedPilot` row), and the spec's own header at
  `memory/builds/dClosedLexicon/spec/2026-08-16-spec-dClosedLexicon-2.md:3` says CLOSED. The map
  wiring it describes is live — `memory/map/generated/inventories.json` carries 23 `lexicon-verbs`
  keys — so CLOSED is the true reading and the other two are corrected to it.
- **S8** — The spec-template line. A spec names each identifier it will mint together with its
  cell. That is the whole binding content; whether the line ALSO names a suggest invocation is F1's
  to decide and this bullet deliberately does not pre-empt it. The line goes in the `### Inventory`
  entry of the recurring-sub-heads bullet at `memory/TEMPLATE-SPEC.md:116` — rev-5 said "§4's
  already canonical `### Inventory` sub-head", and that artifact has no such heading:
  `grep -n Inventory memory/TEMPLATE-SPEC.md` returns `:116` and `:182` only, and the skeleton's
  `## 4. Design` carries no `###` beneath it. Deliberately ungated; see §4.
- **S9** — That line lands in BOTH `tools/memory-tree/SPEC-TEMPLATE.template.md` and its rendered copy
  `memory/TEMPLATE-SPEC.md`. The pair is byte-compared by `tools/memory-tree/kit-dogfood-parity.test.sh`
  at `:53` and `:114`, so a one-sided edit reds the `kit/dogfood doc parity` leg.
- **S10** — The `ratified=` stamp in `.lexicon.conf` is re-stamped in the same commit as any `LANGS=`
  edit, or `signal_lexicon_ratified_stale` at `tools/drift-audit/drift_report.py:846` fires.
- **S11** — The charter's `kit:lexicon` conditional block describes the tool this build actually
  ships. Measured at `bb03dda4` it names three things — a closed verb table, a banned type-suffix
  list and forbidden import directions — of which the third is DELETED by
  `TOOL-aSurfacedLexicon-2` and the other two are no longer the whole surface. It gains the
  (language, surface) cell matrix, the convention predicate, the prefix selector and the canon
  unfreeze stamp. Without this the charter's naming bullets survive the build describing a tool that
  no longer matches the kit, which is the two-answers-to-one-question class on the document that
  states the rule against it.
- **S11a** — THE CHARTER IS A RENDERED PAIR AND BOTH HALVES ARE IN SCOPE. `grep -n 'forbidden
  import' coding-governance-agents.template.md AGENTS.md` returns two hits at `bb03dda4`: the
  template at `:319`, carrying `{{LEXICON_CONF}}`, and the rendered `AGENTS.md` at `:384`, where
  that token is already substituted to `.lexicon.conf`. The rendered hit sits INSIDE the generated
  region — `grep -n 'gov:playbook' AGENTS.md` returns `:78` and `:473` — so the leg that catches a
  one-sided edit is `playbook render wiring`, which runs
  `bash tools/playbook/adopt-playbook.sh --target . --check` and asserts the region equals a fresh
  render. It carries no `guard` key in `tools/gate-legs.json`, so it runs on every bar. Editing one
  half reds it in either direction. S9 already gets this two-file discipline right for
  `SPEC-TEMPLATE.template.md` / `memory/TEMPLATE-SPEC.md`; this bullet is the same rule, and rev-5
  named only the template side.
- **S12** — THERE IS NO BUDGET. S11 IS NET-NON-GROWING ON ITS OWN. Rev-3 and rev-5 said S11 is
  paid for out of the bytes `TOOL-aSurfacedLexicon-2` frees, against a headroom of 285. Both halves
  are dead. Measured at `bb03dda4`, `bash tools/check-template-size.sh` reports
  `49144 / 49152 bytes (8 under, 100.0%)` and `wc -c < coding-governance-agents.template.md` agrees:
  the headroom is EIGHT bytes. `TOOL-aSurfacedLexicon-2`'s AC8 already ruled that exact pair dead in
  writing — "the rev-1 pair `48867` / `285` free bytes was measured at `d0a18683` and is dead at
  this rev's base" — and this spec is the copy that did not get the correction.
- **S12a** — The funding source does not exist. `TOOL-aSurfacedLexicon-2`'s AC8 requires only that
  its §12 edit be "net-neutral or net-negative in bytes", which guarantees ZERO freed bytes rather
  than a budget. So S11 may not be sized against a saving nobody promised. S11 therefore REPLACES
  the stale clause rather than appending to it, and its criterion is measured on its own edit alone:
  the byte count after S11 is no larger than the byte count immediately before it. If the block
  cannot be re-described without growth, the scope item does not land and §8 gains the fork —
  trimming the block's non-instructional prose is the first move, and raising the ceiling is not one
  this unit may make.
- **S12b** — The RENDERED half is tighter than the template and rev-5 never measured it. At
  `bb03dda4`, `bash tools/check-template-size.sh AGENTS.md` reports
  `64506 / 64512 bytes (6 under, 100.0%)`, on the unguarded `charter size` leg. So the binding
  headroom for S11 is SIX bytes on the rendered side, not eight on the template side, and a template
  edit that grows by n grows the render by roughly n. This is the second reason S11 is written as a
  replacement.
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

- **Not acting on the climb branch.** S6b records which branch the reading selects; promoting
  `TOOL-dScaffoldedMirror-9` from probation to scheduled is a change to a pressure chain this
  rebuild does not build, and it belongs to whoever owns that chain. Rev-5 wrote this non-goal as
  "not taking the third reading", which presupposed the abandon branch S6a disproves — under a
  reading above the bar no third reading is owed at all.
- **Not wiring the cell line into `tools/memory-tree/check-memory-hygiene.sh`.** See §4 for the
  compensating check and the precedent.
- **Not renaming the hyphenated Python filenames.** Owner ruling Q3 ships `py.file` armed and files
  the renames as their own unit, `TOOL-aSurfacedLexicon-15`. The POPULATION IS EIGHT, not the seven
  the ruling names: `git ls-files '*.py' | xargs -n1 basename | cut -d. -f1 | sort -u | grep -cvE
  '^[a-z0-9_]+$'` returns 8 at `bb03dda4`, `check-kit-placeholders` having joined since the ruling's
  measurement at `d0a18683`, and `memory/backlog/TOOL.md:342` already records that 8 with the same
  command. Under owner ruling Q2's two-sided equality a pin of 7 against a measured 8 reds the bar,
  and this is the unit that pastes the pin block, so the value written is the one the command prints
  at the landing commit. The ruling's substance — ship pinned, rename separately — is untouched;
  only its operand is corrected, additively, beside the quoted claim.
- **Not editing `memory/HYGIENE.md`.** It carries zero lexicon references today
  (`grep -c -i lexicon memory/HYGIENE.md`) and this unit gives it none.
- **Not abandoning the pressure chain.** S6a settles what the reading IS and S6b settles which
  branch it selects; neither settles what to do about it.
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
`TOOL-aSurfacedLexicon-6` declares that reconciled and withdrawn, so this spec no longer
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
spec — an id typed here would contest one. Rev-5 justified that with a roster count, and the count
was wrong by four; it is dropped rather than corrected, because a count of a derived population
cannot be right for longer than a commit and §2's grep-check makes the instruction beside it
self-computing.

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

Each of the three record carriers gains a supersession note beside its claim, pointing at the
docstring and stating the reading `python tools/drift-audit/drift_report.py --json` prints at the
landing commit together with the branch that reading selects — which on 2026-09-05 is
`added 340, offenders 181, rate_pct 53.2`, far above the bar, and therefore the climb branch (S6a,
S6b). Rev-5 required those notes to say "today's 3.6%
is the first of the two further readings", which is the wrong number and the wrong branch, and it
would have written both into records that are corrected only by supersession.

TWO MORE CARRIERS OF THE SUPERSEDED FIGURE, both inside this build, neither named by rev-5. Run at
`bb03dda4`, `grep -rn "3\.6%" memory/` finds two files under
`memory/builds/aSurfacedLexicon/build/`: the owner-rulings record at its line 101, and the
rebuild-research record at its lines 142 and 724. Both are
`2026-09-04-build-TOOL-aSurfacedLexicon-1` files and each gains the same additive note. The
rulings record's is the delicate one and the note
says so explicitly: owner ruling Q8's SUBSTANCE — the docstring is the sole carrier, the prose
copies are superseded — stands untouched, and what is corrected is the operand in its closing
paragraph, which was inherited from the research pass rather than ruled on.

### Migration

None mechanical. The conf rewrite is a content edit whose result the reader parses or refuses; the
records are appends; the template line is a two-file edit under a byte-compare.

### Rollout

Nothing lands dark. The conf rewrite is the last of this build's declaration changes and is expected to
land after the units that give the `PINS:` block its grammar.

One ordering hazard is RECORDED here rather than resolved, so neither implementer trips it — and it
is CONDITIONAL ON `TOOL-aSurfacedLexicon-10` BEING UNPARKED. The build README parks that unit: its
fork F1 lost both options to the M3 veto ladder, so nothing below describes work this run will do.
It is kept because a parked unit can be unparked and the hazard would then be live again. This unit
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
- `coding-governance-agents.template.md` AND `AGENTS.md` — the S11 block, both sides of the rendered
  pair per S11a. Rev-5 named only the template. The rendered half is regenerated rather than
  hand-edited, in the same commit, which is what `playbook render wiring` asserts.

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
- testing + left-shift gates — FOUR staged breaks, and one new refusal. Rev-5 said "no new
  predicate, so no new failing case to stage" and named AC2 alone; §6 carries AC2 (the pin-row
  round-trip), AC6 (the template line staged into the rendered half only), AC9 (the `LANGS=` edit
  without its `ratified=` re-stamp) and AC14 (the matrix landed with the arming constant left at its
  default). The "no new predicate" half is wrong on its own terms: S14 sets
  `UNDECLARED_CELL_ARMED = True`, which converts the report-only arm `TOOL-aSurfacedLexicon-6`
  landed dark into a REFUSAL. That is a behaviour change in a predicate and it arrives in this unit,
  so it owes its observed RED like any other. This row is derived from §6 and not authored beside
  it; if a criterion gains or loses a staged break, this row is re-derived rather than remembered.
- migration / rollback — every edit is revertable as one commit; the conf rewrite is the only one whose
  revert would matter and it is self-contained.
- user docs — `.lexicon.conf`'s own comments are the user doc for the declaration, and the template line
  is the user doc for the spec integration.

## 6. Acceptance criteria

- **AC1** — A LANDING-TIME DELTA OVER THE REGION, NOT A FILE-LENGTH CEILING. Three parts, all
  measured on the tree this unit actually starts from. (a) The pin archaeology is GONE:
  `grep -cE '^# *(RAISED |LOWERED )?[0-9]+ -> [0-9]+' .lexicon.conf` returns 0, against 10 at
  `bb03dda4`, and all 10 of those sit inside lines 24 through 163
  (`awk 'NR>=24 && NR<=163' .lexicon.conf | grep -cE ...` returns 10 as well). (b) The declaration
  still parses and still declares the same table:
  `python tools/lexicon/lexicon_conf.py --print-verbs .lexicon.conf | wc -l` prints 23, as it does
  today. (c) `grep -cE '^#' .lexicon.conf` after the rewrite is strictly smaller than the same
  command's output on the tree at this unit's own build order, which is RE-MEASURED then rather than
  read from this spec.
- **AC1a** — Why AC1 no longer names a line-count ceiling, recorded so it is not re-tightened by a
  later reader. Rev-5 required the file to shrink by at least the 139 comment lines of region
  24-163, i.e. to 77 lines or fewer against 216 today; deleting the entire region outright lands at
  76, so the whole budget was spent before one byte was added, and the same unit then pastes the
  blank-separated `PINS:` block (S13), the full `CELLS` matrix (S14) and the three surviving
  decision comments §4 requires. That ceiling could not be satisfied without dropping scope this
  unit owes. The 216 was also the wrong base: `TOOL-aSurfacedLexicon-2` at order 1 deletes three
  conf lines, `TOOL-aSurfacedLexicon-5` at order 3 ADDS a `461 -> 462` narration in the
  RAISED-by-name form that part (a) then sweeps, and `TOOL-aSurfacedLexicon-6` at order 4 writes the
  `py.constant` row and its comment — all before order 7.
- **AC2** — When `python tools/lexicon/lexicon.py --measure` is run, the two SCALAR pin lines it
  emits — `VERB_OFFENDER_PIN="968"` and `SUFFIX_OFFENDER_PIN="0"` — are byte-identical to the two
  committed in `.lexicon.conf`; staging a one-digit edit to either makes
  `python tools/lexicon/lexicon.py` exit non-zero, and unstaging it greens. The RED is observed.
  CORRECTED 2026-09-05, and the correction is to this criterion rather than to the code: this
  criterion read "its emitted `PINS:` block is byte-identical to the block committed in
  `.lexicon.conf`", and `--measure` emits no block at all. It writes those two lines and nothing
  else, verified by re-running it; the `PINS:` block in `.lexicon.conf` holds the per-cell rows
  `TOOL-aSurfacedLexicon-4` introduced, which `--measure` has never printed. The criterion named a
  command output that did not exist, so no evidence against it could have been real.
- **AC3** — When `grep -n "TOOL-aSurfacedLexicon" memory/DECISIONS.md` is run, three new rows are
  present: the supersession of `TOOL-dScaffoldedMirror-18`, the casing-refusal reversal, and the P3
  removal with its compensating check named.
- **AC4** — When `grep -rn "two further readings" memory/ tools/` is run, the docstring in
  `tools/drift-audit/drift_report.py` is present and each of the three record carriers listed in §4
  carries a supersession note beside its claim naming that docstring as the sole carrier. Every
  number a note ASSERTS AS CURRENT is a value
  `python tools/drift-audit/drift_report.py --json` prints at the landing commit for the
  `lexicon_marginal_offense_rate` fresh-file arm — `added`, `offenders`, `rate_pct`, all three, with
  that command named beside them. A note asserting any current figure the command does not print at
  that commit FAILS this criterion. This is the criterion form of the build's measure-never-estimate
  rule, and it exists because rev-5 would have written a superseded figure into records that are
  corrected only by supersession.
  CORRECTED 2026-09-05, and the correction is to this criterion rather than to the notes. It read
  "Every NUMBER in every one of those notes ... A note carrying any figure the command does not
  print at that commit FAILS this criterion, including 3.6%" — and the notes carry 3.6% three
  times: twice in the owner-rulings record and once in the rebuild-research record. That is not a
  defect in them. This repo's convention is to QUOTE a superseded claim beside its supersession
  rather than delete it, and both notes exist precisely to say that 3.6% did not reproduce, which
  they cannot do without spelling it. A criterion banning the figure banned the supersession's own
  subject, so it was unsatisfiable by construction and no note could ever have passed it. What is
  gradeable is the figure a note ASSERTS, and re-running the command on 2026-09-05 prints
  `added 340`, `offenders 181`, `rate_pct 53.2` — which is what all four notes assert.
- **AC5** — When `grep -n "reading one of two" memory/builds/dScaffoldedMirror/README.md` is run,
  the line is still there and is followed by its correction, and the correction says what the
  reading actually decides: the landing-commit rate is ABOVE the docstring's roughly 5% bar, so the
  reading DISQUALIFIES today as one of the two further readings rather than being the first of them,
  the abandon chain is broken rather than continued, and the branch the docstring selects is the
  climb clause. A correction line that says today is the first of two further readings fails this
  criterion. If the landing-commit reading is instead at or below the bar, the correction says so
  and names the abandon clause — the criterion grades the branch against the printed operands, not
  against a branch chosen here.
- **AC6** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` is run after the template line
  lands, it exits 0. Staging the line into `memory/TEMPLATE-SPEC.md` alone makes it exit non-zero
  first, which is the observed RED for the two-file rule.
- **AC7** — When `grep -n "the cell that grades it" memory/TEMPLATE-SPEC.md` is run, there is
  exactly one hit and it sits in the `### Inventory` entry of the recurring-sub-heads bullet, at
  `:116` today. The line it belongs to requires a spec to name each identifier it mints together
  with the cell that grades it, and the same phrase is present in
  `tools/memory-tree/SPEC-TEMPLATE.template.md` per S9. This criterion deliberately does
  NOT name `--as`: rev-5 required `grep -c -- "--as" memory/TEMPLATE-SPEC.md` to be at least 1, and
  `--as` appears only inside the tool-pointing instruction that F1's own recommendation would
  remove, so that criterion decided an open fork — and S9 byte-couples this file to the memory-tree
  kit's shipped `SPEC-TEMPLATE.template.md`, which would have shipped F1's named defect to every
  adopter as a landing condition. No criterion in this section names a branch of F1.
- **AC8** — When the three `TOOL-dClosedLexicon-2` carriers are read,
  `memory/map/features/lexicon.md` no longer calls it BLOCKED, `memory/backlog/TOOL.md` no longer calls
  it SPECCED, and the spec header still reads CLOSED.
- **AC9** — When any `LANGS=` edit lands without a `ratified=` re-stamp in the same commit,
  `python tools/drift-audit/drift_report.py` reports `signal_lexicon_ratified_stale`; with the re-stamp
  it does not. Both observed.
- **AC10** — When `bash tools/memory-tree/check-memory-hygiene.sh` is run over the tree with all of the
  above in place, it exits 0.
- **AC11** — When the charter's `kit:lexicon` block is updated per S11 and S11a,
  `grep -c 'forbidden import' coding-governance-agents.template.md AGENTS.md` is 0 on BOTH halves of
  the rendered pair — rev-5 grepped the template only, and the rendered hit at `AGENTS.md:384` would
  have survived it — and the block names the cell matrix, the convention predicate, the selector and
  the unfreeze stamp on both. `bash tools/playbook/adopt-playbook.sh --target . --check` exits 0,
  which is what proves the rendered half was regenerated rather than hand-edited, and
  `bash tools/check-placeholders.sh` stays green, so no new `{{TOKEN}}` is introduced without a
  deploy-time substitution.
- **AC12** — When S11 has landed, `bash tools/check-template-size.sh` reports a byte count at or
  BELOW the count the same command reported immediately BEFORE the S11 edit, and its `OK` line still
  reports a non-negative margin under the ceiling. Both readings are recorded in this unit's
  acceptance ledger, because a budget claim with one reading is an assertion. The measurement is of
  the S11 edit ALONE, not of the distance from some earlier base, because S12a shows there is no
  guaranteed saving to measure against.
- **AC12a** — The same two readings are taken on the rendered half:
  `bash tools/check-template-size.sh AGENTS.md` before and after, with the after no larger than the
  before. That is the BINDING one — S12b measures six bytes of margin there against eight on the
  template.
- **AC12b** — THE WARN IS ADVISORY AND IS NOT A PASS CONDITION. Rev-5 required the leg not to WARN
  past a new high-water, which contradicts the reading `TOOL-aSurfacedLexicon-2`'s AC8 already
  ratified: the leg "also WARNs past its recorded high-water independently of the ceiling, and that
  warning is advisory and does not satisfy or fail this criterion". The tree already warns on a
  clean checkout — `TEMPLATE-SIZE WARN — 48378 -> 49144 (+766)` at `bb03dda4`, and `60930 -> 64506
  (+3576)` on `AGENTS.md` — so rev-5's AC12 could not green unless this unit shrank the charter by
  766 bytes, which nothing in its scope proposes. Both WARN lines are RECORDED in the acceptance
  ledger as context and neither is graded.
- **AC14** — When the commit landing S14 is read, `.lexicon.conf` carries a `CELLS` block and
  `tools/lexicon/lexicon.py` carries `UNDECLARED_CELL_ARMED = True`, in THAT SAME commit — asserted
  by a check over the commit rather than over the tree, because the two landing separately is the
  exact failure S14 exists to prevent and a tree-scoped check cannot see it. THE COMMIT-SCOPED HALF
  HAS A COMMAND, which rev-5 omitted: `git show <sha> -- .lexicon.conf | grep -q '^+CELLS:'` and
  `git show <sha> -- tools/lexicon/lexicon.py | grep -q '^+UNDECLARED_CELL_ARMED = True'` both exit
  0 for the SAME `<sha>`, run by hand at landing and recorded in the acceptance ledger with that
  sha. It is not a bar leg and §7 lists none for it; the tree-side half below is what the bar
  carries. `python tools/lexicon/lexicon.py --check` is then green on the tracked tree, which is the
  armed run `TOOL-aSurfacedLexicon-6` requires observed before landing, and the `py.constant` row
  and its population comment are still present. The RED half is observed too: with the matrix landed
  and the constant left at its default, the undeclared-cell arm prints and does not refuse, and that
  is recorded as the failing case rather than assumed.
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
- THE FIVE UNGUARDED LEGS S11 SELECTS, none of which rev-5 named. Read out of
  `tools/gate-legs.json` at `bb03dda4`, each with `subject: repo` and NO `guard` key, so nothing
  scopes any of them off this commit's bar: `playbook render wiring` (chunk `wiring`, ceiling 300,
  `bash tools/playbook/adopt-playbook.sh --target . --check`) is the one that catches a one-sided
  edit of the rendered pair; `template size <=48KiB` (chunk `product`, ceiling 300) and
  `charter size` (chunk `product`, ceiling 300, the same script over `AGENTS.md`) are the two budget
  legs AC12 and AC12a read; `playbook parity` (chunk `product`, ceiling 560) and
  `playbook placeholder catalogue` (chunk `product`, ceiling 300) both select on a §12 edit.
- The memory-tree hygiene leg, for the three records, the backlog edit and this spec.
- `drift-audit records` and the drift-audit selftest, for the ratified-stale signal and the map dossier
  edit.

No new bar leg, so no wall-clock ceiling and no `memory/project/testsuite-count-waivers.txt` row is
owed. That registry is shrink-only and a row naming a compliant suite reds as stale, so adding one
speculatively would be a defect rather than caution.

## 8. Open questions

- **Q8 is not open.** RESOLVED (owner, 2026-09-04): `tools/drift-audit/drift_report.py` is the sole
  carrier of the kill-rule arithmetic, and the prose copies are superseded. That routing is
  untouched. Its trailing clause — "one more reading is owed before the pressure chain may be
  abandoned" — rested on a reading of 3.6% that S6a disproves, so the clause is
  superseded ADDITIVELY by S6b rather than rewritten: no further reading is owed under the abandon
  branch, because the abandon chain is broken rather than continued. The ruling itself is not
  reopened here, and nothing in this unit acts on the branch the corrected reading selects (§3).
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
  **F1 REMAINS OPEN AND NO CRITERION DECIDES IT.** Rev-5's AC7 required `--as` to appear in
  `memory/TEMPLATE-SPEC.md`, and `--as` lives only in the instruction F1's own recommendation would
  remove, so the criterion ratified one branch of an unratified fork — and S9 byte-couples the file
  to the shipped `SPEC-TEMPLATE.template.md`, which would have carried that branch to every
  memory-tree adopter. S8 and AC7 are now written against the part BOTH branches share, the cell,
  and say nothing about the invocation. Whoever ratifies F1 edits S8 and AC7 together; until then
  neither may be read as a ruling.

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

- rev-6 · 2026-09-05 · the round-1 spec audit folded, and the KILL-RULE READING INVERTS. Re-running
  `python tools/drift-audit/drift_report.py --json` at `bb03dda4` prints `added 142, offenders 15,
  rate_pct 10.6` on the fresh-file arm, not the 3.6% (5 of 138) rev-5 carried from the research
  pass, and 10.6% is ABOVE the docstring's roughly 5% bar — so the reading BREAKS the abandon chain
  rather than continuing it, no third reading is owed, and the branch selected is the climb clause.
  S6 splits into S6, S6a and S6b; AC4 now grades every written figure against what the command
  prints at the landing commit and AC5 grades the BRANCH, because rev-5 would have written a
  superseded number and a disproved ruling into three append-only supersession notes. The charter
  budget is corrected the same way: `bash tools/check-template-size.sh` reports `49144 / 49152` (8
  free) and the same command over `AGENTS.md` reports `64506 / 64512` (6 free), while
  `TOOL-aSurfacedLexicon-2`'s AC8 — which had already ruled the 48867/285 pair dead — guarantees
  only a net-neutral edit and so frees nothing, so S12 splits into S12, S12a and S12b and S11
  becomes a replacement measured on its own edit. S11a adds the rendered half of the charter pair
  and names `playbook render wiring` as the leg that catches a one-sided edit; §7 gains the five
  unguarded legs S11 selects and Files touched gains `AGENTS.md`. AC12b adopts unit 2's ratified
  reading that the size WARN is advisory and grades neither half. AC1 becomes a landing-time delta
  over the pin region — 0 narration heads against 10, 23 verb rows, a strictly smaller comment count
  re-measured at order 7 — because rev-5's 77-line ceiling was already spent by deleting the region
  alone. AC7 and S8 stop naming `--as`, so F1 stays open. §5's testing row is re-derived from §6 and
  names four staged breaks and the `UNDECLARED_CELL_ARMED` arming as the new refusal it is; AC14's
  commit-scoped half gains its two `git show` commands. S4 now QUOTES unit 2's replacement predicate
  instead of describing the named-directory rule it replaced. Smaller: the hyphenated-filename
  population is 8 and carries its command, the roster count is dropped rather than corrected, the
  Rollout hazard is marked conditional on `TOOL-aSurfacedLexicon-10` being unparked, S5 records the
  Q8-into-Q9 routing as declined rather than inherited, and three line cites are re-derived
  (`drift_report.py:946`/`:947`, `memory/backlog/TOOL.md:121`, and `memory/TEMPLATE-SPEC.md:116` for
  the `### Inventory` entry that is a bullet and not a heading).
- rev-7 · 2026-09-05 · the status header UNWRAPPED. The rev-6 fold left it broken across two lines, splitting
  `order` from its value, and the index generator then dropped this unit out of the build-order table
  entirely — a silent scope loss from one line break. S1's eleven pin moves reconciled against AC1's
  ten: two regexes over one region, and a criterion keyed to the looser count would fail the stricter
  grep it names. Cross-spec rev pins dropped.
- rev-8 · 2026-09-05 · TWO CRITERIA GRADED SOMETHING THAT DOES NOT EXIST, and both were corrected
  against a re-run rather than against the code. AC2 asserted `--measure` emits a `PINS:` block; it
  emits two scalar pin lines and no block at all, so nothing it claimed to compare was ever
  comparable. AC4 banned the figure `3.6%` from the supersession notes; the notes carry it three
  times ON PURPOSE, because this repo quotes a superseded claim beside its supersession and a note
  saying "3.6% did not reproduce" cannot say so without the number. Both criteria were unsatisfiable
  by construction, so any evidence recorded against either was false evidence. AC4 now grades the
  figure a note ASSERTS, which `python tools/drift-audit/drift_report.py --json` re-printed on
  2026-09-05 as `added 340`, `offenders 181`, `rate_pct 53.2`. Separately, four numbers written in
  prose beside code and reproduced by no command were DELETED rather than corrected: the
  `py.constant` sensitivity block in `.lexicon.conf` and its four downstream echoes, a selftest arm
  count in `lexicon.py` that the revert it describes does not reproduce, and a comment claiming this unit
  retires `VERB_OFFENDER_PIN` when it writes the matrix — it wrote the matrix and did not.
- rev-9 · 2026-09-05 · the DESIGN half brought onto the same figures as the acceptance half. Rev-8
  corrected AC4 onto `added 340`, `offenders 181`, `rate_pct 53.2` and left S6a, S6b and §4's
  carrier table asserting `added 142`, `offenders 15`, `rate_pct 10.6` at `bb03dda4` — one spec
  giving two answers to the question its own AC4 grades, which is the two-answers-to-one-question
  class on the document that files it. The design half now carries the figures the four supersession
  notes ACTUALLY carry, re-derived rather than copied: re-run on 2026-09-05 at head `2d487019`,
  `python tools/drift-audit/drift_report.py --json` prints `added 340`, `offenders 181`,
  `rate_pct 53.2` on the `lexicon_marginal_offense_rate` signal's fresh-file arm. The branch is
  unchanged and is now stated against the current operands: 4.3% then 53.2% is the climb branch, so
  the abandon chain is broken rather than continued. Both superseded readings — 3.6% and 10.6% — are
  QUOTED in S6a beside their supersession rather than deleted, which is the convention rev-8 records
  and the reason AC4 cannot ban a figure.

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
