# Pre-code review, round 6 — part 1 of 2, the engine and safety units, DEPL-dCarriedReceipt-1..8

**Serves:** spec-audit DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8

**Reviewed:** all 15 specs plus the build README, against the round-5 fold at `1d19b58b` and the
reproduction record at `7ef2a60a`. **Base:** `7ef2a60a`.
**Harness:** four primed finder lenses over the fold diff (fold fidelity, fold collateral, citation
integrity, convergence), then batched default-refute skeptics, then one synthesis. Ten agents, all
returned. Sixteen confirmed entries arrived; deduplicated they are 12 distinct defects across both
parts, and 12 were refuted.
**Why two parts:** the Serves id list renders into one build-README row and 15 ids blow its entry
cap. That is DEPL-dCarriedReceipt-16; rounds 1, 4 and 5 split on the same boundary.

This record carries the findings against units 1-8, and all six land in `-7`. Units 9-15 are
part 2, `2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md`, which carries the convergence
answer and the single High.

## Verdict: CLEAN WITH FIXES

Zero blockers, twelve defects, all of them stale prose with a written edit.

## Medium

**M1 — `-7` S1 enumerates three of `cmd_apply`'s FOUR row producers, and the missing one is the row
the fold's own reproduction listed first.**
*Unit `-7` §2 S1 (:42-49), with a matching gap in S9's neither-arm gloss (:85-92). Provenance:
round-4 M4, round-5 B1.*

S1's new sentence reads "There is a THIRD channel" and names `:2417`. There are four producers.
`cmd_apply` synthesizes one `attributes` row at `govkit.py:2350-2355` carrying `path`, `role`, `kit`,
`version`, `block_id`, `marker_style`, `mode`, `normalized`, `block_sha256`, `patterns` and
`written` — no `commit`, no `source`, no `sha256`, neither identity — and it comes through none of
S1's three channels. The reproduction record lists that row FIRST in its six-row table with
`commit`, `gov_oid`, `oid` and `sha256` all "no". `-13` S11 names the class and decides its fields
for `adopt`; `-7`, the unit that owns `apply`'s row shapes and the identity rule, does not mention it.

Nothing refuses today — the row carries neither field, so S9's second arm passes it over correctly.
This is a completeness defect, and it sits in the exact place that produced this build's last two
blockers: round 4 found S1 unqualified, round 5 found it enumerating two where the tree had three,
and it now enumerates three where the tree has four.

**Edit.** In S1, replace "There is a THIRD channel." with *"There are TWO more producers, and
neither carries either identity."*, and after the `:2417` sentence add: *"The `attributes` row
`apply` synthesizes at `:2350` carries neither identity either, and no `commit` or `source` to derive
one from: gov's bytes there are a block `lf_pins()` composes rather than a blob it shipped, which is
why it carries `block_sha256` alone (`-13` S11). Those four are the whole producer set, observed on
one six-row receipt in
`memory/builds/dCarriedReceipt/build/2026-08-25-build-DEPL-dCarriedReceipt-7-merged-row-reproduction.md`."*
In S9, change "those are the rows `apply` writes at `:2440` — `project-owned`, `generated` and
`rendered`" to *"those are the rows `apply` writes at `:2440` — `project-owned`, `generated` and
`rendered` — and the `attributes` row at `:2350`, which carries neither for the same reason and is
passed over by this same arm"*.

**M2 — `-7` S7 still says `cmd_apply` records both identities, unqualified, which reads over all four
producers and breaks `-13` S11's inheritance argument.**
*Unit `-7` §2 S7 (:77-78). Against S1 (:42-49) and `-13` §2 S11 (:151-153).*

S7 is the scope item a builder implements the identity write from, and it is unscoped: "`cmd_apply`
records both identities: `gov_oid` from the blob it wrote, and `oid` read from the index after the
`git add` it already performs at `:2477`." That `git add` is not a per-channel stage — verified at
`:2477-2478` it is the single `git add -- staged` over every path, and `staged.append(dest)` at
`:2416` puts merged destinations into it. Read literally, S7 covers all four producers and directly
contradicts S1's own new sentence.

The consequence lands in `-13`, which inherits and lands later. S11 asserts "neither carries
`gov_oid` or `oid`" for both synthesized classes and justifies it with "`adopt` writes the same row
`apply` writes". If S7 stamps `oid` on `apply`'s `:2350` row and S11 does not on `adopt`'s, the two
producers of one row class diverge and S11's whole justification collapses. Worse, a `gov_oid`
stamped onto a row carrying no `commit` is S9's own exactly-one shape, which refuses the run. `-7`'s
own criteria do not catch it: AC5 scopes its assertion to `engine` rows.

Same unqualified-quantifier class as round-4 M4 (S1) and round-5 M4 (`-9` S3), surviving one scope
item over.

**Edit.** Scope the quantifier the way S1 now is: *"`cmd_apply` records both identities on the
`writes` channel's rows only: `gov_oid` from the gov blob it wrote, and `oid` read from that path's
index entry after the `git add` at `:2477` — which stages every channel's paths, so the read is per
row and not per stage. The `:2440`, `:2417` and `:2350` rows take neither, per S1."*

**M3 — `-7` §3's land-alone paragraph is wrong on the count, the multiplicity and the citation, and
the fold's new AC11 contradicts its fixture claim.**
*Unit `-7` §3 Land-alone (:128-134). Against §6 AC11 (:264-273), `govkit.py:1420-1424` and `:2350`.*

The paragraph reads: "Acceptance runs on the `memory-tree` fixture, and that kit declares five
`[[lf_pin]]` blocks, each becoming a `role:\"attributes\"` row at `:1420-1424`."

Four problems, in one paragraph that grounds this build's most load-bearing landing dependency.

- **The multiplicity is wrong.** `cmd_apply` appends exactly ONE `attributes` row at `:2350`, with
  every pattern folded into a `patterns` list. `-13` S11 says "the ONE `attributes` row", `-13` AC13
  asserts "exactly one row with `role: \"attributes\"`", and the reproduction observed one such row
  from `push-main`, which declares two pins. So the build now says both things.
- **The citation is wrong.** `:1420-1424` is `planned_writes`' per-pattern PLAN emitter, `kind:
  "order"`, `dest: ".gitattributes:" + pat`. The paragraph then reasons about those plan rows as if
  `cmd_update` iterated them; it iterates `receipt["files"]` at `:2972`.
- **The fixture claim is now partial.** AC11, added by this fold, takes its own `apply --kits
  push-main` target, and `push-main.kit.toml` declares two `[[lf_pin]]` blocks (:69-74), so that
  fixture carries an `attributes` row too and AC11's "the run exits 0" also depends on `-2` landing
  first. §3 records the dependency but justifies it for only one of the two fixtures, so an editor
  who later drops the memory-tree arm drops a dependency AC11 silently needs.
- **The count is correct and should still go.** `git show 9ddcc5c9:tools/memory-tree/kit.toml` has
  five pins; today's tree has seven. The spec's base stamp covers the difference, so "five" is not
  an error — but it is a derived count typed in prose beside the source that owns it, and it has
  already moved once. §7 bans exactly this.

The CONCLUSION survives all four: `UPDATE_ROLE["attributes"]` is `"refuse"` at `:2864`, one refusing
row reaches `r.fail` + `continue` at `:3009-3012`, and `if r.problems:` at `:3115` returns at `:3123`
before `:3125` stamps the schema. `-7` still lands behind `-2` and the README order is unaffected.

**Edit.** Replace :129-131 with: *"Acceptance runs on TWO fixtures and both need it: `memory-tree`
for AC1–AC6 and `push-main` for AC11. Each kit's `[[lf_pin]]` blocks become plan rows at
`:1420-1424` — `cmd_plan`'s per-pattern `kind: \"order\"` rows, which never reach a receipt — and
`cmd_apply` collapses them into ONE `role:\"attributes\"` receipt row at `:2350`, carrying every
pattern in its `patterns` list. `UPDATE_ROLE[\"attributes\"]` is `\"refuse\"` at `:2864`, so that
single row takes `r.fail` + `continue` at `:3009-3012` — one is enough"*, leaving the
`:3115`/`:3123`/`:3125` chain and the AC5 sentence as they stand, and appending *"AC11's exit-0 claim
depends on the same landing."* Do not restate a pin count.

## Low

**L1 — `-7` AC10's half-populated fixture names no role, so AC11 now asserts the opposite outcome for
the same field shape.**
*Unit `-7` §6 AC10 (:260-263). Against §6 AC11 (:264-273) and §2 S9 (:95-100). Provenance: this
fold's own AC11.*

AC10: "A fixture row carrying `commit` and no `gov_oid` refuses by name, writes nothing, and leaves
the receipt byte-identical." AC11, added by the same fold, asserts that a row with that exact field
set does NOT refuse and the run exits 0. After Direction A the only discriminator is `role`, and
AC10 is the criterion that does not name it — while AC10's own closing clause is about not building
the scoping as a blanket pass, which is now exactly what S9 sanctions for one role. AC9, its
fixture-mate, names roles for both its rows, so the omission is AC10's alone.

Low rather than medium: AC11 builds its own `push-main` target rather than sharing AC9's fixture, and
a hand-built row with no `role` key defaults to `engine` at `:2973` and does not match the exemption
anyway. A builder who did reach for a merged row reds the arm rather than shipping a wrong
implementation. Worth taking for symmetry with the identical fix this same fold made in `-13` AC6.

**Edit.** Amend AC10's first sentence to *"A fixture row whose `role` is `engine` — any role S9's
`merged` exemption does not cover — carrying `commit` and no `gov_oid` refuses by name, writes
nothing, and leaves the receipt byte-identical."* Keep the mirrored-row sentence and add the
partition line the fold already wrote into `-13` AC6: *"AC11 owns role `merged`, which is exempt by
ROLE and does not refuse on this same field shape; the two criteria partition the population and
neither generalizes to the other's half."*

**L2 — `-7` §5 tells a builder that `-13` S7 skips any row missing both identity fields, which is the
field-absence reading S7 exists to refuse.**
*Unit `-7` §5 error/empty/loading states (:199-200), with the same elision in `-13` §2 S7 (:112-113).
Provenance: round-5 L3, folded into the README but not into these two.*

`-7` §5 reads: "A row carrying neither identity field is not an error state on this unit at all: S9
passes over it, and `-13` S7 skips it by name inside the loop."

`-13` S7 refuses that in bold: "**`evidence: \"unattributed\"` is the SOLE predicate, and
field-absence is deliberately not an equivalent form of it.** An earlier rev said 'equivalently, a
row carrying neither `commit` nor `gov_oid`', and that clause was false and destructive." It then
enumerates the four dispositions the field-absence reading silently deletes: `skip` at `:3006-3008`
(13 rows on inCMS alone), the `adopter` re-render report at `:3021`, `block`'s block-hash compare,
and `-10`'s `report`.

Measured against the population, `-7` §5's sentence is wrong for every class it covers. The `:2440`
rows (`project-owned`, `generated`, `rendered`, and `-10`'s `forked`) carry neither identity and no
`evidence`, so S7 skips none of them. After Direction A the merged row carries neither identity
either, and S7 skips it too — it dispatches to `block`. `-13` S7's own sequencing clause at :112-113
makes the same elision, ending "this precondition then catches that row inside the classification
loop", which is true only for the `evidence`-carrying subset.

Behaviourally inert — §5 is a production-readiness bullet and `-13` carries the bolded rule in the
scope item a builder implements from — but `-7` lands at README step 3, two steps before `-13`, so it
is the last word a builder has on this before `-13` exists.

**Edit.** Replace `-7` §5 :199-200 with: *"A row carrying neither identity field is not an error
state on this unit at all: S9 passes over it because there is nothing to compare, and what happens to
it next is its ROLE's business in the classification loop — `skip`, `adopter`, `block` or `-10`'s
`report`, each dispatching normally. It is NOT the same population as `-13` S7's skip, which is keyed
solely on `evidence: \"unattributed\"` and scoped to the `table` disposition; S7 says in terms that
field-absence is not an equivalent form of that predicate."* In `-13` S7 :112-113, change "this
precondition then catches that row inside the classification loop" to *"this precondition then
catches such a row inside the classification loop only when it carries `evidence:
\"unattributed\"`"*.

**L3 — `-7` S1's third-channel sentence credits `-8` with keeping `block_sha256`; `-8` never mentions
that field and is about the three-way merge of engine rows.**
*Unit `-7` §2 S1 (:45-49). Against `-8` in full and `govkit.py:2417-2424`. Provenance: round-5's
Direction A text, carried verbatim.*

S1 ends: "…which is why `-8` keeps `block_sha256` for it." Grepped: `block_sha256` occurs in `-7`:48,
`-13`:144, `-13`:146 and the reproduction record, and nowhere in `-8`. `-8` is titled "a merge result
never overwrites `gov_oid`" and its subject is the three-way branch for ENGINE rows — S1 is "the
merge branch stops deriving `gov_oid` from anything the target produced", its §4 table row is
"three-way merged (`:3097-3099`)", and its §10 states `UPDATE_ROLE` (`:2857`) is untouched by it.
"Merged" there means three-way-merged, not role `merged`.

The field's owners are `cmd_apply` at `:2417-2422`, which writes it today at gov HEAD and which no
unit in this build changes, and `-13` S11, which has `adopt` measure it from the block the target
holds. The substance is right — no whole-file gov blob exists for a block — but the attribution is
wrong, and this is the load-bearing justification sentence for the newly ratified direction. The
error is inherited: the round-5 record's Direction A text carries the same clause at line 92.

**Edit.** In `-7` S1 (:48) replace "which is why `-8` keeps `block_sha256` for it" with *"which is
why the row carries `block_sha256` instead — written by `cmd_apply` at `:2417-2422` today and
measured from the block the target holds by `-13` S11. `-8` is not its owner: that unit is the
three-way merge of ENGINE rows at `:3097-3099` and leaves `UPDATE_ROLE` untouched."*

---

## What remains unverified

- **The merged-row refusal has still never been RUN.** The reproduction observed the row SHAPE that
  would trip it — `commit` present, `gov_oid` absent — on a receipt this tree's own kit produces.
  It did not observe a refusal, because `-7` S9 does not exist yet. Direction A's exemption is an
  unexercised design decision, and `-7` AC11 is the first thing its build owes. A gate whose failing
  case has never been staged is an assertion about nothing, and this one is specified rather than
  observed.
- **The AC13/AC14 fixture family exists only as a `-13` §4 estimate.** Round 5 flagged this and it is
  unchanged. Several findings across the last two rounds turn on which fixture a criterion runs over,
  and the answer is currently in a section headed "(estimate)". No `seed` rule is named there while
  AC14 needs an unattributed `seed` row. This resolves when the arms are written, not before.
- **No acceptance criterion observes the four-producer set as a set.** M1's fix makes `-7` S1 name
  all four, and the reproduction record shows all four on one receipt, but nothing asserts that a
  future `cmd_apply` change adding a fifth producer reds anything. The receipt row-class population
  is documented, not gated.
- **`-7` AC11's exit-0 claim depends on `-2` landing first, and that dependency is not stated in
  `-7` §3.** M3's edit adds it. Until then the criterion is correct and its precondition is recorded
  only for the other fixture.
- **The inCMS figures — 41 unattributable rows, 13 `project-owned`, 11 carried — are carried forward
  from `-9` §4 and `-13` §4 and were not re-measured this round.** They are load-bearing in `-12`'s
  "scope it by nothing" argument and in S7's disposition-deletion count. No finding depends on them
  and none contradicts them.
- **`-13` §4's `sha256` narrowing was verified in prose but not against a carried row.** F5 says the
  field hashes the target's bytes; the reproduction ran `push-main`, which produces no `eol` or
  `relocate` row, so the case where gov's blob and the target's bytes differ is still unobserved.
