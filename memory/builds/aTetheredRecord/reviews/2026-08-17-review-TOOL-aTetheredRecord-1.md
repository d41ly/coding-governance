# Review — the aTetheredRecord spec set (M4 spec audit)

**Serves:** spec-audit TOOL-aTetheredRecord-1..7


## Verdict: BLOCKED

Seven units, five lenses, 64 confirmed defects merged to 29. Three units cannot be built from their
specs without inventing a decision the set never made: **unit 6** (its central design paragraph is
mechanically false and contradicts its own scope item), **unit 4 branch 4** (its input does not exist
in the interface unit 2 defines and has already shipped), and **unit 7 S1** (the rename map's
derivation rule is missing four of its five fields). Units 1, 2, 3 and 5 are buildable with edits.

**Live-state warning, which changes what a fold means here.** The tree is not pre-code. `7f2b7b0`
landed unit 1 and `e7dbe93` landed unit 2, including `read_bindings`, `RECORD_KIND_TOKENS`,
`BIND_HEAD_LINES = 12`, the range grammar and `--print-bindings`. Several defects below are already
decided in code by a builder who had to invent them. Where that happened the remedy is to RATIFY the
landed choice in the spec, not to re-decide it — each such edit says so.

The three highest-value questions were answered as follows. *Can a builder build each unit without
inventing a decision?* No, for units 4, 6 and 7 — and demonstrably not, since the unit-2 builder
already invented two (the range token `FAM-slug-N..M` and the fourth `absent` state). *Do the seven
agree on scope, interface, ordering and acceptance?* They disagree on the class vocabulary
(interface), on the branch count (acceptance), on the adopter's first-run verdict (scope) and on the
leg name at landing time (ordering). *Are the claims about existing code true?* Line cites are
exact — all eight check-count carriers, `check-memory-hygiene.sh:313`, `corpus_ids.py:195/215-220/221`,
`check-arms.py:104-113`, `gen_build_index.py:200-228`, `BUILD-METHOD.md:85` all verify. Three counts
do not: the 107/65 reference figure, the 54-of-76 census, and unit 5's nine arms.

---

## Blockers

### B1 — Unit 6 §4 promises an adopter a green tree that unit 4 branch 1 makes impossible, and contradicts its own S2

*Filed independently by three lenses (1-0, 2-13, 3-10).*

**Evidence.** Unit 4 §4:53-55 defines branch 1 as bare presence — "A record whose head carries no
conformant line" — with no pin, no waiver and no registry anywhere in the set (§4:150-153 explicitly
rejects a registry). `RECORD_UNBOUND_PIN` (unit 4 S4:23-26) is read only by branch 3, whose population
is §4:64-67 "records carrying the unbound form", i.e. an authored `none — reason` line. The two
populations are disjoint, and the landed parser proves it: `gen_build_index.py:305-310` returns
`absent` separately from `unbound`, and `--print-bindings` on the live tree prints 76 `A` rows plus
`N 1`. An adopter's untouched records are all `absent`. No value of the pin makes them green.

Unit 6 §4:38-41 nevertheless states the pin "equals their whole record count — which makes their tree
green on day one and leaves the ratchet pointing down", while unit 6 S2:18-20 orders the runbook to
carry "a plain statement that an untouched tree holding records reds on first run". Both sentences are
in one document; only one can ship. Unit 6 §3:25-27 forbids asking the adopter to retrofit, and AC2
only scaffolds an EMPTY repo, where the population guard skips the check entirely — so no acceptance
criterion touches the case the unit exists for. The defect is in exactly one document: unit 6.

**Exact edit (unit 6).**
1. Delete §4:38-41's sentence from "which makes their tree green on day one" through "leaves the
   ratchet pointing down". Replace the paragraph with: *For an adopter the first run is RED: branch 1
   names every record carrying no line. Their migration is one mechanical pass writing
   `**Serves:** none — <reason>` onto each record, which needs no judgement about what a document was
   about and is not a cutoff. They then measure `RECORD_UNBOUND_PIN` at that count and drain it as
   they bind records. The pin bounds the deliberate escape, never the absent line.*
2. Reword S1 so the measurement step is ordered AFTER that pass, and route it through
   `python tools/memory-tree/gen_build_index.py --print-bindings` (unit 2 S3), which reports the count
   with no pin set.
3. Add **AC2b**: *When the adopter script scaffolds into a scratch repo that already holds one build,
   one spec and two records with no binding line, `bash tools/memory-tree/check-memory-hygiene.sh`
   exits 1 naming branch 1, and exits 0 after the mechanical `none` pass with the pin measured at 2.*
4. §5 observability: replace "the gate reports the adopter's remaining unbound count on every run"
   with the branch-1 count, which is what actually falls during their migration.

If the owner instead wants a genuinely green day one, that is a **fifth scalar in unit 4 bounding
branch 1** — an owner decision and a new fork, not a spec edit, and it must be recorded in unit 4.

### B2 — Unit 4 branch 4 has no input: unit 2's `--print-bindings` emits nothing for a bound record, and unit 2 is already committed

*Filed by lens 3 (3-1); its branch-2 half is refuted below.*

**Evidence.** Unit 4 S2:16-19 delegates the parse to "the module from `TOOL-aTetheredRecord-2`" and
branch 4's literal (§4:106) asserts *"record filenames whose family and ordinal name an id their own
`Serves` line does not list"* — a per-record membership test that needs the record's id SET. Unit 2 S3
defines the mode as "one tab-separated row per finding plus a count row". A conformant bound record is
not a finding. The landed contract confirms it: `do_print_bindings` (`gen_build_index.py:365-388`)
emits `A\t<path>\t<why>` for absent/malformed, `B\t<path>\t<token>` for unresolvable ids, and one
`N\t<count>` — a bound record emits nothing at all. Branch 4 therefore cannot be computed from the
module's output, and unit 4 §10's claim of "four seams, none new" is false for it. Because unit 2 is
landed at `e7dbe93` with a `--selftest` leg over that output, this is an interface change to a shipped
unit, which no document in the set authorises.

(Branch 2 needs no change: the `B` row already carries exactly its population.)

**Exact edit (unit 4).** Add to §2:
- **S2b** — *Extend `--print-bindings` with one row per BOUND record —
  `S\t<path>\t<kind>\t<space-separated expanded ids>` — so branch 4 computes filename-vs-header
  membership from the module's output rather than from a second parse. This amends
  `TOOL-aTetheredRecord-2` S3, which shipped before Fork A created branch 4; the amendment is recorded
  here rather than by revising a landed unit.*

Then: name the `S` row in §4's branch-4 paragraph; add to §10 seam 2 that the emission is extended,
not reused as-is; add **AC1c** — *`python tools/memory-tree/gen_build_index.py --selftest` covers the
`S` row for a bound record, and `--print-bindings` still exits 0 and writes nothing*; and add a line
to unit 2's §9 revision log pointing at this amendment so the two documents cannot drift.

### B3 — Unit 7 S1's target-name recipe supplies one of the grammar's five fields, and forbids the builder from filling the rest

*Merges 3-15, 2-0, 1-4, 1-6, 1-7, 2-2, 0-6, 2-9, 2-10, plus the residues the refutations of 0-5 and
4-0 preserved.*

**Evidence.** `check-memory-hygiene.sh:313` is
`^[0-9]{4}-[0-9]{2}-[0-9]{2}-$kind-(($FAM_ALT)-)?[A-Za-z0-9]+-[0-9]+$REC_TAIL\.md$`, spelled at :317
as `YYYY-MM-DD-<kind>[-<FAMILY>]-<slug>-<seq>.md`. Unit 7 S1:13-16 gives the target as "its kind, the
family and ordinal of the lowest id its binding line lists, and a tail" — and then says *"never by
hand"*, while §4:69 rejects one big commit because "a mistake in it is indistinguishable from a
mistake in the map". Five gaps, each a decision the builder must invent and bake permanently into the
tree:

- **The slug slot is never assigned.** Neither unit 7 S1 nor unit 4 §4:87-92 says whether it carries
  the record's housing build or the served id's build. The corpus makes this live:
  `memory/builds/aDrainedSluice/reviews/2026-08-08-review-aDrainedSluice-3.md:1` is scoped over
  "aDrainedSluice V1-V9 + aBatchedTribunal W1-W2". Both answers pass check 5 (`[A-Za-z0-9]+`), and
  branch 4 reconstructs an id from that slot — so the wrong choice reds a correctly-renamed record.
- **"The lowest id" has no total order.** `.memory-tree.conf:15` declares
  `FAMILIES="playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL"`, whose order (PLAY<KICK<TOOL<DEPL)
  disagrees with the lexicographic order a builder reaches for (DEPL<KICK<PLAY<TOOL). Five builds have
  multi-family spec sets — aPrunedCeremony, aSealedCaravan, aSiftedPlaybook, cKeyedLaunchpad,
  dClosedLexicon — and `aSiftedPlaybook` alone holds `PLAY-…-1` and `TOOL-…-1` at the same ordinal.
- **"Its kind" is two-valued inside this build.** Fork E gave `kind` a second closed vocabulary
  (unit 2 §4:59-68, landed as `RECORD_KIND_TOKENS`), while check 5 derives the filename's kind from the
  SUBFOLDER (`check-memory-hygiene.sh:311-312`). `spec-audit` in a filename reds twice over.
- **No date rule.** S1 omits the mandatory `YYYY-MM-DD-` prefix. One in-scope record has no date to
  keep: `memory/builds/aRatchetForge/build/manifest-ratchet-build-report.md`.
- **No extension rule.** `memory/builds/aMooredAnchor/build/2026-08-11-build-aMooredAnchor-1-repro.sh`
  is in check 21's deliberately extension-agnostic population but outside check 5's `\.md$` selector,
  so §10's "the grammar it renames INTO is the one `check 5` already enforces" is false for it.

**Exact edit (unit 7 S1).** Replace the derivation sentence with:

> For each record the target is `<date>-<kind>-<FAMILY>-<slug>-<seq>[-<tail>]<ext>`, where: `<date>`
> is the record's existing date, or for a dateless record its add-commit author date
> (`git log --diff-filter=A --format=%ad --date=short -- <path>`); `<kind>` is the token `check 5`
> derives from the subfolder (`build`, `review`, `prompt`) — never the Fork E relation kind, which is
> header-only; `<FAMILY>`, `<slug>` and `<seq>` are the family, build slug and ordinal of the LOWEST id
> the binding line lists, where lowest orders by family position in `.memory-tree.conf` `FAMILIES`,
> then slug bytewise, then ordinal — so the filename spells a whole id, and a cross-build record takes
> the SERVED id's slug, not its housing build's; `<tail>` is the record's existing ordinal preserved
> verbatim, a disambiguator carrying no binding meaning; `<ext>` is the record's own extension.
> Every field is derived; the tail is the only one the author may override, and an override is noted
> in the map.

Then: (a) add the two worked targets — `aSiftedPlaybook` review 1 and `aDrainedSluice` review 3 — to
S1 so the multi-family and cross-build cases are settled in the spec; (b) mirror the same total-order
sentence into unit 4 §4's "serves several specs" row and change branch 4's literal to read *family,
slug and ordinal* rather than *family and ordinal*, so the projection it asserts is a whole id;
(c) add the cross-build fixture to unit 4 S6; (d) add to unit 7 §10 that check 5 does not grade the
one `.sh` record, so branch 4 is its only gate.

---

## High

### H1 — Unit 4 says three fail branches in four places and four in five, and never states the ARMS_FLOORS target

*Merges 0-3, 1-2, 2-5, 2-14, 3-13.* THREE at §1:7, the §4:51 heading, §5:168 and AC2:178-179. FOUR at
S3:20, S5:27-28, S6:29-32, §4:52-71 with four literals at :103-106, and AC1:174-176. §9:227 records
that Fork A added branch 4. AC1 and AC2 of the same section are mutually unsatisfiable.

The consequence is worse than a typo. `.memory-tree.conf:88` pins
`tools/memory-tree/check-memory-hygiene.sh:14:14`, and `check-arms.py:282` compares `got[i] < want[i]`
— a **one-sided** floor. A builder who reads AC2 and sets `18:17` gets a permanently slack armed floor
and a GREEN bar, which is precisely the regression class the floor exists to catch.

**Exact edit (unit 4).** Change "three" to "four" at §1:7, the §4:51 heading, §5:168 and AC2:179. Add
to S5 the literal target: *`ARMS_FLOORS` moves `tools/memory-tree/check-memory-hygiene.sh` from `14:14`
to `18:18`.* Add to AC1: *the floor is one-sided, so an under-set floor passes silently and must be
asserted by value.* Log the correction in the §9 rev-2 entry rather than overwriting it silently.

### H2 — Unit 4's non-goals name the LOSING fork option as the one shipping

*Merges 1-3, 3-14.* §3:40-41 reads: "**No filename change.** Fork A in §8 is the owner's, and this
unit ships the recommended option: one sentence stating that the ordinal is an ordinal." §8:208-209
records the opposite — "option 2, against the recommendation on this spec, which argued for option 1"
— and §4 ships the override in full (the :73 heading, branch 4 at :68-71, its literal at :106, its
fixture at S6). §3 is the section a builder reads to decide what NOT to build.

**Exact edit (unit 4 §3).** Replace the first non-goal with: *"**No filename MOVES.**
`TOOL-aTetheredRecord-7` performs them. This unit ships §4's redefinition of the ordinal and branch 4,
which enforces it."* Then re-read the whole of §1, §3 and §5 for the same class — the rev-2 fold
touched §4, §8 and §9 and left §1, §3 and §5 at rev-1, which is the pattern behind H1 as well.

### H3 — Unit 2 names three parse classes where the corpus needs four, and "unbound" then means two different sets across four units

*Merges 1-5, 4-5, 0-8.* Unit 2 S1:13-16 enumerates "bound, unbound-with-reason, or malformed". Before
the retrofit a record carries no line at all, which is none of the three. The unit-2 builder had to
mint the fourth: `gen_build_index.py:308` documents "state is one of: bound · unbound · malformed ·
absent". The collision is visible across the set — unit 3 AC1:125-127 uses "unbound-classification
rows" (must reach zero) and "unbound-form count" (equals the pin) as different sets in one sentence;
unit 2 AC1:145-147 asserts a quantity that is wrong under both readings (today `A`=76, `N`=1, records
=77); unit 6 §4 reads "unbound" as absent, which is where B1 comes from. The defect is in one
document — unit 2, which owns the vocabulary.

**Exact edit (unit 2).** In S1 name four non-colliding classes matching the landed code: **`bound`**,
**`unbound`** (the authored `none — reason` escape branch 3 counts), **`malformed`**, **`absent`** (no
line). Rewrite AC1 to: *"…it exits 0, its `A`-row count equals the record count minus the already-bound
records before the retrofit, and is zero after it."* Then align unit 3 AC1 (`A` rows zero; `N` equals
the pin), unit 4 §4:64-67 (branch 3 counts `unbound`, branch 1 counts `absent` and `malformed`) and
unit 6 §4 onto exactly those four words.

### H4 — Unit 4's new population guard is vacuous: its precondition is the population

*Merges 0-4, 2-15.* S1:13-15 spells the precondition as "tracked files under a build's non-spec
subfolders"; S2:16-19 defines the population as "any tracked file at any depth under a build's
`build/`, `prompts/` or `reviews/` folder". `RECORD_KINDS` is the closed tuple
(`spec`,`build`,`reviews`,`prompts`), so non-spec ≡ the three; I measured both at 77.
`pop_guard` (`check-memory-hygiene.sh:124-128`) returns early when the population is >0 and again when
the precondition is 0, so it fires only on population==0 AND precondition>0 — unreachable when the two
selectors are identical. §4:118's promise of "non-zero with an empty population only when the selector
is wrong" is undeliverable, and AC3 asserts only the QUIET direction, which a vacuous guard satisfies
exactly as well as a correct one. §5:166-167 names this as the failure mode that matters.

**Exact edit (unit 4).** Rewrite S1 as a predicate coarser by CONSTRUCTION, in `PRE_RECORD`'s shape at
:131-134: *"**S1** — `PRE_BINDABLE`, a new precondition beside the existing four: a count over `$FILES`
of paths matching `/(build|prompts|reviews)/`, un-anchored to `$M/builds/<slug>/`. It is coarser than
check 21's population by construction, so a mis-anchored or wrong-depth population selector leaves it
non-zero."* Delete the "under a build's non-spec subfolders" phrasing. Add **AC3b**: *a scratch tree
holding a record at a pre-flatten path (`memory/<slug>/build/x.md`) produces a `check 21:` line in the
mis-segmented-population report.*

---

## Medium (11)

- **M1 — unit 2: the range separator is never named.** No range token appears in any of the seven
  documents, while §4:82-84 and AC3 make range expansion mandatory. The builder invented it:
  `gen_build_index.py:288` ships `…-(?P<lo>\d+)\.\.(?P<hi>\d+)$`. *Fix:* rev-3 of unit 2 §4 states the
  shipped token literally — `FAM-slug-N..M`, one family and slug, expanded at parse time — with one
  worked example. Lazier and worth considering: delete the range from §4/S5/AC3; the largest
  enumeration in this corpus is seven ids.
- **M2 — unit 3 §4:50 instructs the retrofit to author lines the landed parser rejects.** "Each
  authored line also carries the KIND token" vs unit 2 §4:52-55's unbound form, which has no ids;
  `gen_build_index.py:336-341` makes the kind optional there and required on the bound form
  (`**Serves:** research none — …` classifies `malformed`). The disagreement is unit 3's. *Fix:* narrow
  §4:50 to "Each authored BOUND line also carries the KIND token; the unbound form takes none." Also
  state in unit 2 §4 that `Commissions` carries no kind (ratifying `gen_build_index.py:327-331`) and
  add a `--selftest` arm for that shape.
- **M3 — unit 3 AC2's witness cannot produce the comparison.** `git grep -c 'Serves:' -- memory/builds`
  emits per-file rows and no total (three today, two of them non-records), and cannot skip a fenced
  example. *Fix:* delete AC2 — AC1 already asserts it through the gate's own predicate — or reassert on
  the `A`-row count of `--print-bindings` being zero.
- **M4 — the 107/65 reference figure exists at no commit.** Four lenses re-measured: at BASE `96141aed`
  103 lines / 62 files / 5 markdown links; at HEAD 106/65 by basename, 107/66 by stem. The design pass
  at `build/…-design-pass.md:37` says 103/62 and the README:54-56 names it the dated source. *Fix:*
  restore 103 / 62 / 5 to unit 7 S3 and the §4 inventory, spell the needle in the "How" column
  (basename including extension), correct §5's derived residue from 102 to 98, and fix the copy in
  unit 4 §8:214.
- **M5 — the blank-pin semantics are undecided in the document that owns the key.** Unit 4 S4 says only
  "blank in the shipped example conf". `.memory-tree.conf.example:45-48` says blank turns a MEASURED
  pin off; `tools/memory-tree/README.md:19` says undeclared means 0 for the POLICY pin
  `ROW_DUPLICATE_PIN`, which ships with a value. Unit 6 §4:63-64 asserts blank "is the strictest value",
  which is false for the class it assigned. *Fix:* decide in unit 4 S4 — recommend the policy-pin
  treatment (`RECORD_UNBOUND_PIN="0"` shipped with a comment naming it a policy refusal) — and drop the
  "strictest" clause from unit 6 §4.
- **M6 — the sole `prompts/` record has no kind token that fits.**
  `aGuardedTally/prompts/2026-08-03-prompt-aGuardedTally-1.md:1` is the brief that COMMISSIONED an
  audit; unit 3 §4:52-53's precedence classifies it `spec-audit` on its own H1, which lets a brief count
  as audit coverage in unit 5 S2's second derived line — the exact claim unit 2 §3:39-42 forbids. *Fix:*
  in unit 2 §4, state that a commissioning brief classifies `research` regardless of its H1 phrasing,
  and add that rule to unit 3 §4's precedence.
- **M7 — branch 4 is partial on a filename with no family qualifier.** §4:82-83 declares the qualifier
  "REQUIRED" only for multi-family builds and no branch enforces it; the spec never says whether such a
  record is skipped or red. *Fix:* make branch 4 total — a record with a non-`none` binding whose
  filename carries no family qualifier reds on branch 4 — drop the multi-family carve-out (unit 7 S1 is
  unconditional anyway), and add the no-qualifier fixture to S6.
- **M8 — branch 3's arm signature is not the run unit 4 predicts.** `check-arms.py:104-113` takes
  `max(parts, key=len)` after splitting on interpolations; for §4:105 that is the trailing clause
  ("— bind them, or move the pin…", 71 chars), not the leading run (49). An arm written against the
  lead arms nothing and the 18-armed floor reds. *Fix:* reword branch 3 so every interpolation FOLLOWS
  the literal run, and quote in §4 the exact signature string each of the four arms must contain
  verbatim — the extractor chooses it, not the author.
- **M9 — unit 4 owes a kit-version bump it does not scope.** `check-verdict-epoch.sh:68` puts
  `check-memory-hygiene.sh` in the epoch scan; unit 2 already spent `2.17` at `e7dbe93`, so unit 4's
  engine edit makes W newer than S and the leg exits 1 at :188. §7:193-195 lists neither `verdict
  epoch` nor `kit version markers`. *Fix:* add a scope item bumping `KIT_MEMORY_TREE_VERSION` and the
  `gov:kit memory-tree@` marker in the three files `check-verdict-epoch.sh:160-166` names, re-rendered
  through `kit-dogfood-parity.test.sh --render`; add both legs to §7 and an AC in the shape of unit 2's
  AC5/AC6.
- **M10 — unit 5 owes the same bump.** `gen_build_index.py` is in `DELEGATES`
  (`check-verdict-epoch.sh:69`), unit 5 §4:60 touches it, and §7:110-111 lists neither leg. *Fix:* same
  edit as M9. Fold M9, M10 and unit 2's precedent as one pass so the set states the rule once: any unit
  touching the engine or a delegate bumps in its own commit.
- **M11 — unit 4 AC5's predicate over-collects, and its inventory misses two RANGE carriers.**
  `git grep -nE '[0-9]+[- ]check'` returns 141 lines in 78 files, including `memory-recall`'s "18
  checks" and `check-12` hits that must never move. Separately, `tools/memory-tree/README.md:18`
  ("1-12 in the shell") and `AGENTS.md:94` ("checks 9, 13-16, 17-19 and 20 delegate…") need structural
  repair, not a count bump. *Fix:* scope AC5 to the eight carriers by citing the §4 inventory table,
  state that records and other builds' landed specs are out of scope, mark those two rows RANGE in the
  table, and extend AC5 to assert no delegation or shell-range enumeration omits 21.

## Low (11)

- **L1 — unit 6 AC5's drift-signal clause is a no-op.** `drift_signals.py:117-134` matches legs on the
  argv SCRIPT PATH, which `AGENTS.md:94` already spells, so the signal reads identically before and
  after the rename. *Fix:* strike the clause after "check 21 is named there".
- **L2 — unit 5 mis-describes its own anchor and miscounts its arms.** The sentence is derived from
  `RECORD_KINDS` (`gen_build_index.py:502-503`, :540-543) and includes `spec/` — this build's own
  README:87 renders "Records live under `spec/` and `build/`." And eleven `arm(` calls reference it, not
  nine. *Fix:* S1 says "below the derived `Records live under …` sentence, whose folder list includes
  `spec/`"; §3 drops the numeral rather than re-measuring a figure that will move again.
- **L3 — unit 6 S2 names a `WIRE-INTO-PROJECT.md` section that does not exist.** There is no
  "kit-version section"; only `### 3a` (:188-215) carries all four elements S2 lists. *Fix:* name §3a by
  heading and state the insertion point (a sibling `### 3e` under §3).
- **L4 — unit 2 §4:95's "118 after `TOOL-aTetheredRecord-1`" is seven low** (125 measured; the 113
  baseline predates this build's own seven specs). Unit 1 already repaired the identical defect in its
  own §9. *Fix:* restate relatively — "measured at BASE `96141aed` as 113, re-measured by the unit."
- **L5 — the numbered HYGIENE catalog entry 21 lands three commits before the engine has a check 21**
  (it is at `memory/HYGIENE.md:205` today, from `e7dbe93`, while the engine has 14 branches). Parity
  passes because both halves agree. *Fix:* state in unit 2 S4 that the entry lands un-numbered and
  unit 4 numbers it, or move the numbered entry to unit 4 S8.
- **L6 — unit 5 §7 names a leg that will not exist when it runs.** It spells `memory hygiene (20
  checks)` while landing after unit 4's rename. *Fix:* `memory hygiene`, as units 4 and 6 already write
  it.
- **L7 — unit 7 AC3's witness passes for free.** `git ls-files -- memory/` emits paths, so an old
  basename is absent from it by construction after `git mv`. *Fix:* "When `git grep -F <old-basename>
  -- memory/` runs for every basename moved in a batch, it returns nothing outside the append-only
  areas."
- **L8 — unit 4 S6's fixture constraint gives a false reason.** Branch 2's population is authored lines
  only (§4:57-62), so an unresolvable filename projection cannot red there. The constraint is
  unnecessary, not wrong. *Fix:* replace the reason; keep AC1b and the fixture.
- **L9 — "in the shape check 9 already uses" is imprecise.** Check 9 is one exit-code branch
  (`check-memory-hygiene.sh:463-465`) and `do_print_bindings` always returns 0; check 21 consumes rows.
  *Fix:* in S2 and §10 item 2 say "one invocation of the read-only mode, its rows split in the shell
  into four branch populations, each with its own `fail 21` call site". Keep the "no new leg" clause.
- **L10 — the README's and design pass's "54 of 76 records" is 55 at the six-line window they name**
  (54 only at 12 lines; the flip record is `aSiftedPlaybook/reviews/…-2.md`, whose first id sits at
  line 12). *Fix:* restate as the 12-line window to match `BIND_HEAD_LINES`, or correct to 55.
- **L11 — unit 2 §4:93's head-window justification is false.** A markdown findings table at line 12 of
  `aSiftedPlaybook/reviews/…-2.md` exists at BASE, so 12 lines does admit body prose. *Fix:* give the
  true reason — the window is bounded and the parse is key-anchored, so prose inside it cannot parse —
  and drop the unverifiable "line 4" figure.

---

## Refuted — do not fold

Named so a later reader cannot mistake silence for absence. Twelve claims were examined and rejected:

1. **A continuation rule for a wrapped binding line is missing** (unit 2). Refuted: §4:50 says "one
   line", the parser implements it as obvious code, and there is no line-length gate anywhere in the
   kit.
2. **Unit 7 S1 leaves four items "never named"** (map content, tail, derivation, committed path).
   Refuted: each is determined by S1's own next clause, unit 4 §4:89, AC1, or unit 3 S1's sibling
   precedent. The slug and total-order residues from that sentence ARE real and are folded into B3.
3. **Unit 3 §3 and unit 7 §3 conflict over who may edit a citing file.** Refuted: unit 3's non-goal is
   scoped to unit 3; unit 7 S3 mandates the repair and AC3 grades it.
4. **Unit 5's coverage join must choose build-scoped vs tree-wide.** Refuted: §4:47 qualifies only the
   minuend, and unit 2's functions are tree-wide by construction — the plain reading, the lazy
   implementation and the argued one coincide.
5. **The closed kind vocabulary has no enforcement owner.** Refuted: unit 4 §5:161-162 ("a malformed
   line is branch 1, not a crash") plus unit 2's `malformed` class; the landed parser rejects an unknown
   token at `gen_build_index.py:342-352` with a selftest fixture. No fifth branch needed.
6. **Six aSiftedPlaybook review tails must be invented.** Refuted as an invention: no gate reads the
   tail and no reference depends on it. B3 gives it a mechanical rule anyway.
7. **`legacy-files.txt`'s stale-line guard is unscoped.** Refuted: unit 7 S4, AC5 and AC6 all cover it.
8. **An unknown kind token needs a fifth fail branch.** Refuted, same as (5); the proposed remedy would
   break unit 4 S5 and AC1's 18:18 floor.
9. **The sole `prompts/` record has no derivable kind.** Refuted on its own H1, which matches
   `spec-audit`'s gloss almost verbatim. The separate *coverage-claim* defect it raises is M6.
10. **Unit 7 S1's kind ambiguity is high severity.** Refuted on severity: §3, §10 and AC2 pin the target
    to check 5's grammar, which rejects a wrong reading on the first batch. Folded into B3 as a wording
    edit, not a blocker of its own.
11. **The one `.sh` record leaves branch 4 undecidable.** Refuted: `check-memory-hygiene.sh:307` skips
    legacy files, unit 7 S4 renames the two legacy record rows, and keeping an extension is obvious
    code. The §10 imprecision is folded into B3(d).
12. **Unit 4 AC5 "cannot be made green without editing history."** Refuted: AC5's subject is "every live
    carrier", and §4's inventory enumerates that set exhaustively and correctly. The looseness is M11.

Two lens claims were *partially* refuted and survive only in narrowed form: branch 2 needs no new
emission (B2 covers branch 4 only), and `ARMS_FLOORS` is one-sided upward rather than two-sided — which
makes H1 worse, not better.
