**Serves:** spec-audit TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11

# Spec audit round 1 — aJoinedCanon

Tier-2 · node a · 2026-09-05 · a pre-code pass over the whole eleven-unit spec set at rev-2/rev-3, before any unit opened and before owner scope approval.

**ROUND 1** over eleven subjects, each pinned at the blob it was read at: [TOOL-aJoinedCanon-1](../spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md)@`2ae0f59f9c0d` · [TOOL-aJoinedCanon-2](../spec/2026-09-04-spec-TOOL-aJoinedCanon-2.md)@`c5b5340cfb8c` · [TOOL-aJoinedCanon-3](../spec/2026-09-04-spec-TOOL-aJoinedCanon-3.md)@`a3381c4e610b` · [TOOL-aJoinedCanon-4](../spec/2026-09-04-spec-TOOL-aJoinedCanon-4.md)@`fd974db93667` · [TOOL-aJoinedCanon-5](../spec/2026-09-04-spec-TOOL-aJoinedCanon-5.md)@`797706b07d6c` · [TOOL-aJoinedCanon-6](../spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md)@`d6a67dbd9838` · [TOOL-aJoinedCanon-7](../spec/2026-09-04-spec-TOOL-aJoinedCanon-7.md)@`420dfef33dcf` · [TOOL-aJoinedCanon-8](../spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md)@`dd51403e6fd4` · [TOOL-aJoinedCanon-9](../spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md)@`2bb4797a8d90` · [TOOL-aJoinedCanon-10](../spec/2026-09-04-spec-TOOL-aJoinedCanon-10.md)@`1f837e7a45de` · [TOOL-aJoinedCanon-11](../spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md)@`6b0390e09a86`.

## Verdict: BLOCKED

Two findings say a unit cannot be built as its own design section describes it, and both are the
same shape the build exists to remove: an arm whose real population is narrower than its spec
believes, so the arm passes by finding nothing. `TOOL-aJoinedCanon-4` nests its failure-mode test
inside the acceptance-witness walk, whose entry is guarded by a THIRD cutoff the spec never names —
`SPEC_WITNESS_CUTOFF`, shipped blank in the adopter example — so in an unarmed adopter tree the arm
never executes while its own key reads as armed. `TOOL-aJoinedCanon-8` introduces three corpus-wide
JOIN arms into a check that is live under `--staged`, where the selection is the staged set alone,
so committing one half of a correctly declared edge pair reds pre-commit on honest work. Neither is
fixable during a build pass: each needs a design decision the spec has not made.

Everything else is repairable inside the specs, and most of it in one line each. The build's
diagnosis is sound and its eleven mechanisms are the right ones — what is wrong is that a spec set
written to close the "numbered but not joined" class committed that class against itself eleven
times over. Six of the seventeen defects below are one unit pinning a literal that a sibling unit,
earlier in the same declared chain, moves before it lands.

## Review shape

| Raw | Confirmed | Refuted | Unverified | Precision |
|---|---|---|---|---|
| 49 | 30 | 19 | 0 | 0.61 |

Precision 0.61 clears the ~0.5 floor §8 sets, so the shape of round 2 should not change: same lens
count, narrower scope. Nothing came back unverified — every finding below survived a skeptic asked
to refute it, so none is an open question about whether it is true.

The 30 confirmed collapse to **17 distinct defects**, because two lens pairs found the same four
instances of the example-conf class independently (8 confirmed findings, 4 instances, one fix) and
the stale-literal class was found from both the criterion side and the scope-item side. The
consolidation is stated per finding below. It is a priming artefact, not a scoping one: the fan was
handed eleven specs and no map of which units share a write set, so it re-derived that map eleven
times and reported each derivation.

Two units drew no confirmed finding at all: `TOOL-aJoinedCanon-2` and `TOOL-aJoinedCanon-5`, the two
rev-3 units the owner already ruled on. Both are Tier-1 and both write template prose rather than
engine arms, which is the honest reason and not a compliment.

## Severity as adjudicated here

One finding carries a severity here different from the one the review fan assigned.

- **Raised to HIGH — H9, the false observer join in `TOOL-aJoinedCanon-3`.** The fan called it
  medium. H7 — a scope item with NO criterion — is graded high by the same fan, and H9 is a scope
  item with a criterion that cannot fail, which is strictly worse: the missing join announces
  itself, the false one reads as coverage. It is also committed inside the unit whose entire subject
  is joining scope items to the criteria that observe them. Grading one instance of a class below
  another instance of the same class is how the class survives.

| Severity | Count |
|---|---|
| BLOCKER | 2 |
| HIGH | 9 |
| MEDIUM | 6 |

## The findings at a glance

| # | Sev | Unit | Address | The defect |
|---|---|---|---|---|
| B1 | blocker | `TOOL-aJoinedCanon-4` | §2 S3, §4 Rollout | the arm's real population is an intersection with a third cutoff the spec never names |
| B2 | blocker | `TOOL-aJoinedCanon-8` | §2 S5 and S6, §4 | three corpus-wide joins inherit no `--staged` hold, so half a correct pair reds pre-commit |
| H1 | high | units 1, 3, 4 | §2 S6 / S7 / S6 | three sequenced units claim the same fixture block in one shared scratch tree |
| H2 | high | units 4, 7, 10, 11 | §6 AC7, §6 AC5, §2 S7, §4 | five literals pinned against values the build's own chain moves first |
| H3 | high | units 1, 4, 6, 11 | §2 S4 / S2 / S4 / S1 | a new cutoff key never reaches the shipped example conf, redding a leg each unit names |
| H4 | high | `TOOL-aJoinedCanon-6` | §7, against §2 and §4 | two engine arms land with neither `verdict epoch` nor `kit version markers` in §7 |
| H5 | high | `TOOL-aJoinedCanon-7` | §2 S7, §4 | §7 is located by NUMBER, so a legal Tier-1 spec reds with no remedy |
| H6 | high | `TOOL-aJoinedCanon-8` | §3, against §2 S5 and S6 | an edge INTO a Tier-1 sibling reds on a correct pair, and §3 calls that a gap |
| H7 | high | `TOOL-aJoinedCanon-1` | §2 S5, §6 | the zero-population notice — the only thing separating silence from coverage — has no criterion |
| H8 | high | `TOOL-aJoinedCanon-6` | §6 AC10 | the criterion grades against a "tolerance" stated nowhere in the spec |
| H9 | high | `TOOL-aJoinedCanon-3` | §2 S2 and S3, §6 AC6 | the named observer is a byte-compare that is green when neither file was touched |
| M1 | medium | `TOOL-aJoinedCanon-9` | §4, against §6 AC6/AC7 and §8 | a live fork that falsifies two criteria is parked in §4, and the header reads ratified |
| M2 | medium | `TOOL-aJoinedCanon-8` | §3 Edges | the worked example of the new grammar demands of unit 10 the thing unit 10 refuses |
| M3 | medium | `TOOL-aJoinedCanon-7` | §4 | "two of the 93 names contain a `/`" — one does, and the other is a different exclusion class |
| M4 | medium | `TOOL-aJoinedCanon-4` | §6 AC5 `Red when:` | the break is named against the wrong line, in the unit that introduces `Red when:` |
| M5 | medium | `TOOL-aJoinedCanon-7` | §5 risks | the co-editor enumeration the re-render discipline rests on is short by seven units |
| M6 | medium | `TOOL-aJoinedCanon-9` | §4 Files touched | a paragraph about the cost of an undercount restates the undercount |

---

## Blockers

### B1 — the failure-mode arm's real population is an intersection, and the third gate is nowhere in the spec

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-4.md` §2 S3 and §4
Rollout.

**Defect.** S3 places the failure-mode test INSIDE the acceptance-witness walk and reuses that
walk's `acc` accumulator. That walk opens at `tools/memory-tree/check-memory-hygiene.sh:1020` with
`if (wcut != "" && fdate != "" && fdate >= wcut) {`, where `wcut` is bound
`-v wcut="$SPEC_WITNESS_CUTOFF"` on the awk at `:956`. The arm's population is therefore the
INTERSECTION of `SPEC_WITNESS_CUTOFF` and the new `SPEC_FAILURE_MODE_CUTOFF`, and when the walk is
not entered the accumulator the arm reads is never even built. §4 Rollout calls the arm "doubly
gated" and names only the new key and `[ -n "$SPEC_FORMAT_CUTOFF" ]` at `:913`. The third gate
appears in no section of the spec.

**Why it is real.** Verified at source: `:1020` is the guard, `:1049` closes it, `:956` binds
`wcut`, `:913` is the outer `SPEC_FORMAT_CUTOFF` gate. `tools/memory-tree/.memory-tree.conf.example`
ships `SPEC_WITNESS_CUTOFF=""`, so every adopter tree that arms the failure-mode key without having
armed the witness ratchet gets an arm that never executes while its own key reads as armed — a
demand that silently evaporated, indistinguishable from one that passed, which is the exact shape
this unit exists to close. AC6 tests only the blank-`SPEC_FAILURE_MODE_CUTOFF` direction and cannot
see it. Partial mitigation, stated because it narrows the blast radius and not because it clears the
finding: the self-test's scratch conf at `check-memory-hygiene.test.sh:67` does set
`SPEC_WITNESS_CUTOFF="2026-08-08"`, so AC1-AC5 will not pass-by-finding-nothing in THIS repo's
fixtures. The undocumented third gate and the adopter dead-arm both stand.

**Fix.** State in §4 Data model that the test is nested under the witness guard and that its
population is the intersection. Then choose, in §2, one of: (a) hoist the accumulator out of the
`wcut` guard so both arms drive it independently; or (b) declare the intersection as the intended
population and add a scope item plus an AC — a fixture dated at or after `SPEC_FAILURE_MODE_CUTOFF`
with `SPEC_WITNESS_CUTOFF` BLANK must still red on a clauseless bullet, observed before the arm
lands. Pin both cutoffs in the fixture conf either way.

**Left-shift.** A `gotchas/` class record for "an arm nested inside another arm's cutoff guard
inherits that cutoff as an undeclared precondition", so `python tools/memory-tree/gotchas.py
--for-diff` puts it on every reviewer's checklist for this engine. The gateable half is cheaper than
it looks and belongs to `TOOL-aJoinedCanon-5`, which is already building a preconditions declaration
for criteria: extend that declaration to require a `cutoffs:` field naming EVERY cutoff variable on
the awk path the arm sits on, and have the self-test derive the enclosing `-v <name>cut` guards of
each new emitter and red when the spec's field does not name them all.

### B2 — three corpus-wide joins land in a check that is live under `--staged`, where only one end of an edge is in the selection

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md` §2 S5 and S6,
and §4 "Where it lives".

**Defect.** The reciprocity arm (S5) and the order arm (S6) join two spec FILES, but the awk's only
input is `c12_sel`, built at `check-memory-hygiene.sh:943-948`, whose loop calls `in_scope "$f" ||
continue` — and `in_scope` at `:304` narrows the selection to the staged set under `--staged`. The
loop's own inline comment says it: "no-op in full mode; decides the WHOLE selection under
`--staged`". §4 states "Nothing re-reads a file" and never states that both ends of an edge must be
in one selection.

**Why it is real.** `.githooks/pre-commit` runs `bash check-memory-hygiene.sh --staged` whenever
`memory/**` is staged, and check 12 is NOT held under `--staged` the way check 23 is at `:1404`,
which prints an explicit HELD notice for precisely this reason — "a corpus-wide join over every
closed Tier-2 unit; the push-boundary run is where they bind". Unit 8 introduces three corpus-wide
joins into check 12 and inherits none of that guard. Committing one spec of a correctly declared
pair therefore reds pre-commit on honest work: unit B's spec is absent from the selection, so its
`consumes-from` is invisible and S5 reports "B declares no matching consumes-from A". Every one of
AC1-AC8 runs a FULL harness pass, so no criterion in the spec can observe this.

**Fix.** Add a scope item holding the three JOIN arms under `--staged` the way check 23 is held at
`:1404`, with the same announce line, leaving only the per-file SHAPE arm (S4) live in pre-commit.
Add an AC: staging one spec of a conforming edge pair and running `--staged` must not red. State the
population constraint in §4 "Where it lives" — the join is closed over `c12_sel`, and `c12_sel` is
the staged set under `--staged`.

**Left-shift.** A self-test arm, not a gate, and it generalises past this unit: for every arm in
check 12 that reads more than one file, stage exactly one of the pair and assert silence. Cheaper
still as a structural rule the next author reads — `memory/HYGIENE.md`'s check-12 section gains one
line saying a cross-file join inside check 12 owes a `--staged` hold and its announce line, in the
same words check 23's header already uses.

---

## High

### H1 — three sequenced units claim the same fixture block in one shared scratch tree

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md` §2 S6 and §4
Files touched; `…-3.md` §2 S7; `…-4.md` §2 S6 and §6 AC1-AC5. Consolidates confirmed findings 14,
45 and 46.

**Defect.** Unit 1 (order 1) claims `tFixture-90` through `95`. Unit 3 (order 3) claims "the free
block from `tFixture-90`". Unit 4 (order 4) claims "90 through 94". All three are in
`tools/memory-tree/check-memory-hygiene.test.sh`, and each spec justifies its block with the same
sentence — that the highest fixture in the file today is `tFixture-86`, which is true only for
whichever unit lands first.

**Why it is real.** Verified: the file's high-water is `tFixture-86`, and line 69 sets ONE shared
fixture tree `D=memory/builds/tFixture` that the bulk of the arms write into. Assertions there are
keyed by fixture name (`hit`/`miss` on a filename substring), so a duplicate number does not error —
it silently makes one unit's assertions grade another unit's fixture, which is a green arm observing
nothing. Unit 4 is the worst placed: it lands last of the three AND hard-codes the numbers into
AC1-AC5, so a collision repoints five acceptance criteria at a sibling's files. That the build saw
this and closed only part of it is itself evidence — unit 8's S9 takes "from 100 up" and cites
unit 3's claim alone, deconflicting one edge deep.

**Fix.** Give each unit a disjoint declared block, as unit 8 already does, and state the allocation
ONCE in the build README's rules so the chain has a single owner of the number space: 1 → 90-95,
3 → 96-99, 4 → 120-129, 6 → 130+, 9 → 140+, 11 → 150+. Drop every spec's "the highest in the file
today is `tFixture-86`" claim. Phrase unit 4's AC1-AC5 against fixture ROLES with the numbers
resolved from the allocation, not from the file's high-water at build time.

**Left-shift.** A self-test arm inside `check-memory-hygiene.test.sh` itself: derive the fixture ids
the file declares and red on a duplicate. It is a `grep -oE 'tFixture-[0-9]+' | sort | uniq -d`
against an empty expectation, it costs nothing, and it turns a silent misgrade into a named refusal
for every future build that adds fixtures to this harness — which is most of them.

### H2 — five literals pinned against values the build's own declared chain moves first

**Address.** `…-11.md` §6 AC7; `…-10.md` §6 AC5 and §3; `…-4.md` §2 S7 and §4 Inventory; `…-7.md`
§4. Consolidates confirmed findings 15, 33, 16, 43 and 44.

**Defect.** Five criteria and scope items pin a value that an earlier unit in the same `order` chain
changes before the pinning unit runs.

- Unit 11 AC7 asserts `python tools/memory-tree/check-arms.py --report` "still reports `20:20`" for
  `check-memory-hygiene.sh`. Unit 6 (order 6) adds two `fail 23` branches to that file and unit 8
  (order 8) adds three `fail 12` branches. Unit 11 is order 11.
- Unit 10 AC5 requires `check-kit-versions.sh` to exit 0 "with `KIT_MEMORY_TREE_VERSION` unchanged
  at `2.59`". Unit 10 is order 10, and units 1, 3, 4, 8, 9 and 11 each declare a bump of that
  constant.
- Unit 4 S7 and its Inventory row pin the move as `2.59` → `2.60`. Units 1 and 3 bump it first, so
  `2.60` is either a no-op or a regression.
- Unit 7 §4 argues from "2.59 in both carriers today" for the same reason.

**Why it is real.** Verified at source. `.memory-tree.conf:203` carries
`tools/memory-tree/check-memory-hygiene.sh:20:20` today and `check-arms.py --report` prints the
DISCOVERED counts beside the floors, not the pin, so AC7 is unobservable at order 11 — a builder
chasing it either reverts a sibling's floor bump or records a false green, and AC7's real content
(this arm adds no new `fail` branch) goes unchecked. `check-memory-hygiene.sh:20` is
`KIT_MEMORY_TREE_VERSION=2.59` today, so unit 10's AC5 is falsified by the chain before it starts
and can only pass by the build failing to do what six siblings scoped. `verdict epoch` and `kit
version markers` red on a regressed constant, so unit 4's pinned pair costs a full bar cycle to
discover. The irony is load-bearing rather than decorative: this is the stale-pinned-literal class
`TOOL-aJoinedCanon-5` is being built to name, committed five times inside the build that names it.

**Fix.** Strip the literal from all five and derive instead.

- Unit 11 AC7: run `--report` at this unit's base sha and again after the change, assert the pair is
  UNCHANGED between the two, name no value. Add unit 5's `figure: DERIVED at observation time` line.
- Unit 10 AC5: "exits 0, and `KIT_MEMORY_TREE_VERSION` is unchanged by THIS diff." Same edit to §3's
  "Both files already carry `memory-tree@2.59`".
- Unit 4 S7 and Inventory: "the constant advances by one minor in this landing, in the constant and
  in every `gov:kit memory-tree@` carrier, the carrier set derived with `grep -rl`." Unit 3 §4 and
  unit 8 S10 already phrase it derived — match them.
- Unit 7 §4: state the invariant (marker equals constant) and name no value.
- Correct the two consequential knock-ons: unit 8 §4's "moves the floor from `20:20`" is already
  stale by unit 6's two branches, and unit 9 §4's "check 12 has exactly one `fail 12` site" is true
  today and false after unit 8's three land.

**Left-shift.** This one is already in the build — it is `TOOL-aJoinedCanon-5`'s `figure: DERIVED`
sub-field. Make it bind here by adding a build README rule for round 2: no criterion or scope item
in this set names a numeric value that any unit at a lower `order` writes, and the fold pass greps
each spec for the constants the chain moves (`KIT_MEMORY_TREE_VERSION`, `ARMS_FLOORS`, the
`tFixture-` high-water) before the spec is re-marked SPECCED. Gateable later as a check-12 arm: a
criterion whose text contains a backticked value that also appears in a sibling spec's Files-touched
write set is a warn, which is exactly the join this build is about.

### H3 — a new cutoff key never reaches the shipped example conf, redding a leg each unit names

**Address.** `…-1.md` §2 S4 and §4 Files touched (`REV_SCOPE_CUTOFF`); `…-4.md` §2 S2 and §4
Inventory (`SPEC_FAILURE_MODE_CUTOFF`); `…-6.md` §2 S4 and §4 Files touched (`LEDGER_LABEL_CUTOFF`,
`LEDGER_TOKEN_CUTOFF`); `…-11.md` §2 S1 and §4 Files touched (`BASE_RESOLVE_CUTOFF`). Consolidates
confirmed findings 29, 30, 31, 32, 39, 40, 41 and 42 — two lens pairs found the same four instances
independently.

**Defect.** Four units add five new cutoff keys to `tools/memory-tree/check-memory-hygiene.sh` and
declare each in `.memory-tree.conf`, but none of the four names
`tools/memory-tree/.memory-tree.conf.example` in its scope items or its Files-touched table.

**Why it is real.** Verified at source. The parity arm at `check-memory-hygiene.test.sh:1550-1574`
derives `_engpresets` with `grep -oE '^[A-Z][A-Z0-9_]*_CUTOFF='` over the comment-stripped engine,
unions it with the `${NAME:-}` read form, exempts exactly `GOV_PYTHON` and `MAP_ROOT`, and then
fails naming any remaining key the shipped example does not declare: "an adopter cannot discover
it". Both read forms are covered, so unit 6's two keys — read exactly as `alcut` is at `:1376` — are
inside the population as surely as the bare presets are. All eight existing engine presets are
declared in the example today, and the arm's own comment records this exact hole swallowing
`FORK_MARK_CUTOFF` and `REVIEW_VERDICT_CUTOFF` once already. Every one of the four units names
`memory-hygiene self-test` in its own §7 as an owed leg, so each reds on its landing commit for a
reason unrelated to the arm it is building — five reds across four units, the most expensive way in
the tree to learn a one-line omission.

This is not a withheld non-goal, and it is not a fresh judgement call. `TOOL-aProvenReuse-5` is a
CLOSED unit that made the declaration mandatory and built the derivation that enforces it, and
siblings in this very set carry the line explicitly — unit 3 S1, unit 8 S3 ("shipped blank in
`tools/memory-tree/.memory-tree.conf.example`"), and unit 7, which records a deliberate absence. The
convention exists inside the spec set; four units are silently outside it.

**Fix.** Add `tools/memory-tree/.memory-tree.conf.example` to the scope item and the Files-touched
table of all four units, shipping each key blank, and add one AC per unit observing
`grep -qE '^<KEY>=' tools/memory-tree/.memory-tree.conf.example` and the self-test exiting 0. Copy
unit 8 S3's wording.

**Left-shift.** The gate already exists and works — this is a spec-authoring miss, not a coverage
gap, so the left-shift belongs one level up: `memory/TEMPLATE-SPEC.md`'s Files-touched guidance
gains a line saying a spec that adds a conf key names every CARRIER of that key, and the carrier set
for this kit is the engine, `.memory-tree.conf` and the shipped example. Cheap machine version, and
it fits `TOOL-aJoinedCanon-7`'s existing §7-contract arm: red a spec whose diff-scope adds a
`*_CUTOFF` to the engine and whose Files-touched table has no example-conf row.

### H4 — two engine arms land with neither `verdict epoch` nor `kit version markers` in §7

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md` §7, against §2
S1-S2 and §4 Files touched. Also `…-3.md` §7.

**Defect.** Unit 6 adds two awk emitters, two bash walks and two `fail 23` branches inside
`tools/memory-tree/check-memory-hygiene.sh`. Its §2 declares no `KIT_MEMORY_TREE_VERSION` bump, its
§4 Files-touched table omits the constant entirely, and its §7 names neither `verdict epoch (kit
version dates the engine)` nor `kit version markers`.

**Why it is real.** `tools/memory-tree/check-verdict-epoch.sh:68` sets
`ENGINE=tools/memory-tree/check-memory-hygiene.sh` and applies a topological rule: the newest commit
moving a behaviour-bearing engine line must be an ancestor of, or equal to, the newest commit that
CHANGES `KIT_MEMORY_TREE_VERSION` in the range. Both legs are unguarded in `tools/gate-legs.json`,
so they run on every bar. Unit 6's landing commit changes the engine's verdicts and reds a merge-bar
leg its own Gates section does not name — a §4 Design the §7 Gates does not cover. The build's
Definition of Done reads §7, so the failure surfaces at the push boundary rather than at the diff.
Sibling units 1, 3, 4, 8, 9 and 11 all declare that obligation for the same file and unit 7
explicitly reasons why it owes none, so the authors address this deliberately everywhere except
here. Unit 3 is the lesser half of the same defect: it scopes the bump in §4 and still does not name
the leg in §7.

**Fix.** Add both leg names to unit 6's §7, add a scope item for the constant plus every `gov:kit
memory-tree@` carrier with the set derived by `grep -rl` and never counted, and add the rows to §4's
Files touched. Add `verdict epoch` to unit 3's §7.

**Left-shift.** This is exactly what `TOOL-aJoinedCanon-7` is building — §7's contract, where a leg
name resolves — so extend that unit's arm by one rule rather than inventing a leg: a spec whose
Files-touched set includes a path named by an unguarded leg's `ENGINE`/subject must name that leg in
§7. The data is already in `tools/gate-legs.json` and in the spec's own table, and it turns the most
expensive discovery point in the tree into a spec-lint red.

### H5 — §7 is located by NUMBER, so a legal Tier-1 spec reds with no remedy

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-7.md` §2 S7 and §4
"The checker change".

**Defect.** S7 turns a §7 that contributes no leg name into a RED, but `tools/check-spec-tokens.py`
locates the section by NUMBER — `SEC = r"^## %s\.[^\n]*\n(.*?)(?=\n## |\Z)"` at `:50`, called as
`extract_section(text, 7)` at `:162`, returning `""` when the section is absent — and the `specs`
population at `:129-136` filters on LIVE status only, with no tier filter anywhere. §4 never says
the arm assumes §7 is Gates.

**Why it is real.** `memory/TEMPLATE-SPEC.md:106-108` states the Tier-1 light profile explicitly:
the nine-section canon is not enforced, "write the few sections that matter". This corpus already
contains the counter-case, and the engine records it verbatim at
`check-memory-hygiene.sh:1372-1375`: "THE HEADING IS LOCATED BY TEXT, never by number… a Tier-1
spec's section 6 may be Gates — two closed ones in this corpus are — and a check reading section 6
by NUMBER would red a spec that is legal under the format it enforces." The first post-cutoff Tier-1
spec written under the light profile reds with no remedy but a per-path waiver. Sibling unit 3 pins
this same class deliberately, citing `dUnstalledConvoy` review M13 for keying on `## 6.`, and unit 8
scopes its arm to Tier-2 and states the Tier-1 residual in its non-goals. Unit 7 does neither, so it
re-opens a class two of its own siblings closed.

**Fix.** Either locate §7 by HEADING TEXT (`^## [0-9]+\. Gates`) as check 12 does and as unit 3's S5
requires, or scope S7 to Tier-2 by reading the header's `Tier-` field. Add the exclusion to §3
non-goals, and add an AC: a post-cutoff LIVE Tier-1 fixture with no `## 7.` heading is silent.

**Left-shift.** A `gotchas/` class record — "a spec-format check that locates a section by number
reds a legal Tier-1 spec" — so `gotchas.py --for-diff` fires on any diff touching
`check-spec-tokens.py` or check 12. The engine already carries the lesson in a comment where only
its own author reads it; the point of the record is that the lesson travels to the checker one
directory over that has not learned it yet.

### H6 — an edge INTO a Tier-1 sibling reds on a correct pair, and §3 calls that a gap

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md` §3 "Tier-1 is
not graded", against §2 S5 and S6.

**Defect.** The shape arm sits below the Tier-1 cut at `check-memory-hygiene.sh:1172`
(`if (hdr ~ /Tier-1/) next`), so a Tier-1 sibling is `next`-ed before it registers anything. The
reciprocity and order arms therefore cannot distinguish "sibling not in the graded set" from
"sibling declared no reciprocal". §3 names that exact scenario — "the reciprocal side of an edge
INTO a Tier-1 unit" — and calls it "unenforceable", when the arm's actual behaviour is a RED on a
correct pair.

**Why it is real.** Verified: `:1172` is the cut, and S5 makes a `hands-off` naming a sibling with
no matching `consumes-from` a red. §3 exempts Tier-1 from carrying the block at all, so a correct
Tier-2 → Tier-1 edge has no reciprocal to find. This build's own roster makes it the common case and
not an edge: four of eleven units are Tier-1 (2, 5, 10, 11), and unit 8's own `### Edges` block
declares `hands-off TOOL-aJoinedCanon-10`, whose header reads Tier-1 — so the first instance of the
shape in the tree is the failing case. §4's "What the arms do not check" names only the
rubber-stamp limit, and AC3 exercises two Tier-2 fixtures, so nothing in the spec observes it.

**Fix.** Add a membership test: an edge whose target is absent from the graded population is SILENT,
not red, and record that silence as the declared gap. Add an AC — a Tier-2 fixture declaring
`hands-off` a Tier-1 sibling is silent. Correct §3's wording from "unenforceable" to "skipped, and
here is the test that skips it", which is the §7 rule about a gate's header stating what it does not
check, applied to a spec.

**Left-shift.** No new gate — the fix IS the arm. What generalises is the rule behind it, and it
belongs in `memory/HYGIENE.md` beside check 12: an arm that joins a graded record to another record
tests MEMBERSHIP before it tests agreement, because absence from the population and disagreement
inside it are different answers. That sentence would also have caught B2.

### H7 — the zero-population notice, the only thing separating silence from coverage, has no criterion

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md` §2 S5,
against §6.

**Defect.** S5 is the zero-population notice. No criterion in §6 mentions the notice, the announce
line, or a zero-population run.

**Why it is real.** I read all eleven criteria: AC1-AC11 cover the red fixture, the grandfather, the
rev-1 exemption, the continuation fold, the blank cutoff, the clean tracked-tree run, parity, the
verdict epoch, the arms floors and the kickoff stamp. None names the notice, and AC7 asserts the
opposite (exit 0). Under the ratified `2026-09-06` cutoff this arm grades zero specs on day one, so
S5's notice is the only thing separating its silence from coverage — §4's Rollout says exactly that.
With no criterion, the unit can be called done with the arm landed and the notice never written, and
the resulting green is indistinguishable from an arm that is mis-scoped or broken. Every sibling
that ships the same notice grades it: unit 3 AC7, unit 6 AC7, unit 8 AC8.

**Fix.** Add an AC in the shape of unit 3's AC7. When no tracked spec reaches `REV_SCOPE_CUTOFF`, a
full `bash tools/memory-tree/check-memory-hygiene.sh` run prints the named zero-population line on
stdout naming `REV_SCOPE_CUTOFF`; when the cutoff is lowered to a date the corpus reaches, the line
is absent.

**Left-shift.** `TOOL-aJoinedCanon-3` is the gate — a §2 scope item names the criterion that
observes it, or says why none does — so this finding is a live instance of the class unit 3 closes,
found in the spec that lands three units ahead of it. Run unit 3's predicate over all eleven specs
in this set BEFORE unit 3's cutoff is chosen, per §7's "run a candidate gate predicate over the real
tree before wiring it". It is a grep, and it will surface the rest of this class in one pass instead
of one review each.

### H8 — the criterion grades against a "tolerance" stated nowhere in the spec

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md` §6 AC10.

**Defect.** AC10 grades the offender count as landing "within a stated tolerance of the
315-of-1,241 figure". No tolerance is stated anywhere — `grep` for `toleran` over the file returns
exactly that one line.

**Why it is real.** The criterion has no pass/fail boundary. Any offender count between 1 and 1,241
can be argued into or out of "tolerance" at build time, so AC10 cannot fail on a wrong count and is
graded by whoever runs it. Unlike the cutoff dates, which this same spec pins to a derivation
command, the tolerance has no source. It matters more than a normal loose criterion because AC10 is
this unit's only re-derivation of arm B's 25.4% rate, which is the number the whole red-vs-advisory
ruling in FORK-1 rests on — and FORK-1's resolution invokes charter §7 to refuse exactly this
could-not-fail shape.

**Fix.** State the band in AC10 ("between 280 and 350 offenders, and the run RED"), or better,
replace the tolerance with the two observations that cannot drift: the run exits 1, and the count is
recorded in the build record beside the 315/1,241 probe figure for comparison.

**Left-shift.** `TOOL-aJoinedCanon-5`'s preconditions sub-fields already carry `figure:`; add the
rule that a criterion naming a numeric expectation states either a literal band or the command that
derives it, and that a comparative word with no band is a refusal. That is a grep for the hedging
vocabulary (`tolerance`, `roughly`, `about`, `approximately`) inside a `## 6.` section — cheap,
and it fires on a class this corpus produces steadily.

### H9 — the named observer is a byte-compare that is green when neither file was touched

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-3.md` §2 S2 and S3,
against §6 AC6. Raised from medium; the reason is in "Severity as adjudicated here".

**Defect.** S2 and S3 both write "Observed by AC6". AC6 runs only `kit-dogfood-parity.test.sh`,
which renders the template and byte-compares it to the live copy. It is green when the template
gained the paragraph and the copy was re-rendered, and equally green when neither file was touched
at all.

**Why it is real.** The rule text itself — the paragraph in the skeleton's §2 body and the clause on
the numbering bullet — has no observation that could fail. No other criterion and no leg in §7
reaches the paragraph's content; `spec tokens` resolves this spec's own names, not the template's
prose. The unit could land the awk arm and the cutoff with the template never stating the rule, and
§6 would be fully green — which is precisely the arm-without-an-author-facing-rule state the unit
exists to avoid. S1's third half, the key shipped blank in
`tools/memory-tree/.memory-tree.conf.example`, is unobserved for the same reason. A false observer
join, declared in the unit whose subject is joining scope items to the criteria that observe them,
is the finding this build most needs to not have.

**Fix.** Add a criterion that reads the rendered `memory/TEMPLATE-SPEC.md` and asserts its §2 body
names `AC<n>` and the `NOT OBSERVED` escape, and that the numbering bullet carries the new clause —
a grep with a derived pre-change count of zero, in the shape unit 7's AC1 uses. Add the example-conf
grep alongside it (see H3).

**Left-shift.** Same gate as H7, one rule wider, and it is the one addition this build should make
to `TOOL-aJoinedCanon-3`'s own mechanism: a scope item may not name as its observer a criterion
whose only command is a PARITY or byte-compare check, because such a check grades sameness and never
content. That is a small deny-list of leg names inside unit 3's arm, and it converts the whole "the
observer exists but cannot fail" class from a review finding into a red.

---

## Medium

### M1 — a live fork that falsifies two criteria is parked in §4, and the header reads ratified

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md` §4 "Measured
before wiring", second re-measurement bullet, against §6 AC6/AC7 and §8.

**Defect.** §4 states that the declared `READINESS_ROWS` value and the measurement the arm is sized
against "do not describe the same predicate", that the long label `risks (concurrency, data-loss,
rollback hazards)` is missing from 324 of 364 Tier-2 specs, that this is "fatal the first time
anyone sets the cutoff backwards, AC6's own second sentence included", and that the builder picks
between two resolutions — one of which "drops AC7's byte-identity". It closes: "This spec does not
pick." §6 nonetheless ships AC6 (which depends on the 48-spec measurement) and AC7 (byte-identity)
as if both hold, §8 holds only F1 and F2, both RESOLVED, and the header reads `ratified 2026-09-05`.

**Why it is real.** Two acceptance criteria on the same spec are mutually exclusive under one of the
two futures the spec itself names, and the choice between them sits in §4 rather than in §8 where a
fork is machine-read and owner-ruled. The spec presents as fully resolved and scope-approvable while
carrying a live design decision it calls fatal.

**Fix.** Move it into §8 as a fork with a recommendation — short tokens in the declaration with AC7
dropped, versus prefix matching up to the first parenthesis with AC7 kept — mark the header
unratified until it is ruled, and rewrite AC6 and AC7 to whichever branch wins. Do not leave the
reconciliation as an S6 build-time instruction; S6 is a measurement step, not a decision.

**Left-shift.** Check 12 already grades fork marks (`FORK_MARK_CUTOFF`). Extend that arm in the
direction this finding points: a §4 body containing a decision phrase ("this spec does not pick",
"the builder chooses", "either form") while §8 holds no OPEN fork is a red. It is a grep over two
sections the checker already extracts, and it is the mechanical half of the rule that a fork lives
where the owner reads it.

### M2 — the worked example of the new grammar demands of unit 10 the thing unit 10 refuses

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md` §3
`### Edges`, the `hands-off TOOL-aJoinedCanon-10` bullet.

**Defect.** Unit 8's declared handoff reads: "`SPEC_EDGES_CUTOFF` is one more declared cutoff key,
so the sentence unit 10 corrects must count it." Unit 10 S1 says the opposite in as many words — the
sentence "stops saying 'beside the three other cutoffs' and puts no other count in its place" — and
unit 10 AC1 asserts `grep -n 'three other cutoffs'` matches nothing, with no replacement number.
Unit 10 declares no `### Edges` block and no reciprocal at all.

**Why it is real.** Both halves verified verbatim. S12 offers this block as "the first instance in
the tree on the day the rule lands", so the demonstration instance of the new grammar is both
factually wrong about its target and non-conforming under its own unit's S5 reciprocity arm. See H6
for why the Tier-1 half of that also reds.

**Fix.** Rewrite the bullet's payload to what unit 10 actually accepts — a handoff that the count is
DELETED rather than updated, so unit 8 owes unit 10 nothing but the key's existence — or drop the
edge and declare `hands-off external`. Either way add the reciprocal `consumes-from
TOOL-aJoinedCanon-8` to unit 10's §3, or state in unit 8 §4 that a Tier-1 sibling carries no block.

**Left-shift.** Unit 8's own S5 arm is the gate; what this finding shows is that it must be run
against this build's eleven specs before its cutoff is chosen, which is charter §7's
run-the-predicate-over-the-real-tree rule and is already owed by the unit.

### M3 — "two of the 93 names contain a `/`" — one does, and the other is a different exclusion class

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-7.md` §4 "What the
join reads today", final paragraph.

**Defect.** The paragraph claims two of the 93 manifest names contain a `/` and are discarded by
`NOT_A_LEG` before they can resolve, naming `kit/dogfood doc parity` and `python resolver (behaviour
+ inline parity + idiom ban)`.

**Why it is real.** Derived against the sources the spec cites: `tools/gate-legs.json` holds 93 legs
and exactly ONE name contains a `/`. The second is excluded by `NOT_A_LEG`'s `^python3? `
alternative at `tools/check-spec-tokens.py:60`, not by the path alternative. §3's non-goal and AC5
are both written around `/` alone — AC5's fixture "lists a manifest name containing a `/`" — so S4's
resolve-first change covers a second exclusion class that no criterion observes. §4's own simulation
("graded §7 tokens 56 → 57") is consistent with one name and not two, and was not read as the
contradiction it is.

**Fix.** Correct the sentence to name the two DIFFERENT exclusion alternatives, and split AC5 into
two arms — one fixture listing `kit/dogfood doc parity`, one listing `python resolver (behaviour +
inline parity + idiom ban)` — each observed RED against the unpatched checker.

**Left-shift.** Nothing new. This is the finding that argues for the build README rule H1 and H2
also want: a measurement quoted in a spec is re-derived at the start of that unit's build pass, and
the command that derives it is written beside the figure. `TOOL-aJoinedCanon-5`'s `figure: DERIVED
at observation time` sub-field is that rule for criteria; extend the same discipline to §4 prose.

### M4 — the break is named against the wrong line, in the unit that introduces `Red when:`

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-4.md` §6 AC5, the
`Red when:` clause.

**Defect.** AC5's failure-mode clause names "the `if (hdr ~ /Tier-1/) next` cut at
`check-memory-hygiene.sh:1170`". That line is 1172.

**Why it is real.** Verified byte-exact: 1170 is the closing `}` of the terminal-status block, 1171
is blank, 1172 is the cut. Three specs in this set give three numbers for the same anchor — unit 4
says 1170, unit 1 §4 says 1173, units 3 and 8 say 1172 — and only one is right. AC5 is the criterion
pinning unit 4's both-tiers placement, so the unit that teaches "name the break that would turn it
red" ships a break named against a wrong anchor, in a file five earlier units in the chain also
edit. The checker cannot catch it: `check-spec-tokens.py` skips citations whose path is untracked, a
basename citation like `check-memory-hygiene.sh:1170` is skipped and counted, and even when graded
it resolves RANGE only, so 1170 passes against a 1600-line file.

**Fix.** Correct unit 4 AC5 and unit 1 §4 to `:1172`. Better, since units 1, 3, 4, 6, 8, 9 and 11
all edit this file in sequence: cite the cut by its literal source text (`if (hdr ~ /Tier-1/) next`)
rather than by line number, which is the only citation form that survives the chain.

**Left-shift.** A build README rule for round 2 — inside a build whose units share a write set, an
anchor into a shared file is cited by literal text or heading, never by line number. The gateable
version is a narrowing of `check-spec-tokens.py`: a `file:line` citation whose path resolves and
whose line does not contain the backticked text cited beside it is a red. That is strictly stronger
than the range check it already does, and it costs one `sed -n`.

### M5 — the co-editor enumeration the re-render discipline rests on is short by seven units

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-7.md` §5, risks row.

**Defect.** The row reads "units 1, 2 and 5 also edit `tools/memory-tree/SPEC-TEMPLATE.template.md`,
so this unit re-renders after landing rather than assuming its own copy of the live file." Ten of
the eleven specs name that file — only unit 6 does not.

**Why it is real.** Units 3 (S2, at `:173`, `:210`, `:93`) and 4 (§4 Inventory, at `:210-214`) both
declare edits to it and both land BEFORE unit 7; units 8 (S1), 9 (S3), 10 and 11 edit it after. Those
declarations existed at the same fold that produced unit 7's rev-2, so this is a present error and
not a base-pinning artefact. The enumeration under-counts by seven the units nearest to it in the
chain, which is the half the risk row exists to cover. I confirmed every anchor unit 7 pins is
correct at base `750ca0ca` — both halves of the template are 271 lines, `:126` is `## §10 Reuse
audit`, `:216-218` is the `## 7. Gates` skeleton body, `:210-214` is the acceptance-witness
paragraph — so the anchors are exactly the fragile thing, and no spec in the set says its template
anchors are re-derived at build time.

**Fix.** Replace the enumeration with a derived statement — "every unit at a lower `order` that
lists this path in its Files touched" — and add one line to the build README's rules: anchors into
`SPEC-TEMPLATE.template.md` are cited by heading or literal text, and any line number in a spec is
re-derived at the start of that unit's build pass rather than trusted from the spec.

**Left-shift.** Same left-shift as M4, and the same one rule covers both files. If only one thing
from this report reaches the README, make it that rule — it is the cheapest of the lot and it
answers four findings.

### M6 — a paragraph about the cost of an undercount restates the undercount

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md` §4 Files
touched, closing paragraph.

**Defect.** The paragraph states the kit version bump "touches SIX `gov:kit memory-tree@` carriers,
not the three that `check-verdict-epoch.sh`'s remediation message names". The derived count is
SEVEN: six marker files plus the `KIT_MEMORY_TREE_VERSION` constant at `check-memory-hygiene.sh:20`,
whose line carries both the constant and a marker.

**Why it is real.** `git grep -l 'memory-tree@2.59'` returns seven non-record carriers. Siblings 1
(§4), 8 (S10) and 11 (§4) each state seven, and unit 8 notes in terms that `TOOL-dSettledRoster-4`
says six and that this is the reason to derive rather than count. I tried the charitable reading —
that six means the doc markers and the engine is the separate table row — but the sentence offers
its number as the CORRECTION to a remediation message that undercounts, so it reads as a total, and
six is the exact figure the backlog row records as the wrong one. A paragraph whose whole point is
that an undercount costs a bar cycle should not restate the undercount.

**Fix.** Replace the literal with the derivation the same paragraph already recommends —
`grep -rl 'gov:kit memory-tree@'` plus the constant — and state no number.

**Left-shift.** Charter §7's "NO count of a derived population is written in prose", applied inside
a spec rather than inside a checker. The mechanical form is a check-12 arm: a §4 body containing a
spelled-out or digit count immediately followed by the word `carriers`, `legs`, `arms` or `rows` is
a warn unless the same paragraph names the command that derives it. Narrow, greppable, and it fires
on the class this corpus keeps producing — including in the document that states the rule.

---

## What the hunt found and did not find

The prompt named six hunts. Five produced findings: a §2 item with no §6 criterion (H7, and H9 as
its worse cousin), a criterion naming no observation it could fail on (H8, H9), §2 against §3 (M2,
H6), §4 Design against §7 Gates (H4), and what must be true of existing code for §4 to work that §4
never says (B1, B2, H5). The sixth — whether a record already decided this — produced two hits, both
of which the specs contradict rather than cite: `TOOL-aProvenReuse-5` already made the example-conf
declaration mandatory and built the derivation that enforces it (H3), and `TOOL-dSettledRoster-4`
already recorded six-instead-of-seven as the wrong carrier count (M6).

Line-number claims were checked against source rather than taken. `check-memory-hygiene.sh:1020`,
`:304`, `:913`, `:943-948`, `:956`, `:1172` and `:1404` are all correct as cited by whichever spec
cites them correctly; `:1170` and `:1173` are not (M4). `check-memory-hygiene.test.sh:1550-1574` is
the cutoff-parity arm as described (H3). `check-verdict-epoch.sh:68` sets the engine path as
described (H4). `check-spec-tokens.py:50`, `:60`, `:129-136` and `:162` are correct (H5, M3).
`tools/gate-legs.json` holds 93 legs (M3). `.memory-tree.conf:203` carries `20:20` and
`check-memory-hygiene.sh:20` carries `2.59` (H2). The fixture high-water is `tFixture-86` (H1).
`tools/memory-tree/SPEC-TEMPLATE.template.md` is 271 lines in both halves with every unit-7 anchor
landing where the spec says (M5).

## What round 2 should look like

Same lens count, narrower scope — precision 0.61 says the fan is calibrated. Two changes to priming
would remove most of the duplication: hand the fan the units' write sets as a table so it stops
re-deriving which units share a file, and hand it this report so it hunts new defects rather than
re-finding the eleven instances of the two classes above.

Three of the fixes are one rule in the build README rather than eleven spec edits, and they should
land before round 2 reads anything: a single owner for the `tFixture` number space (H1), a ban on
naming a value a lower-`order` unit writes (H2), and citation by literal text rather than line
number inside a shared write set (M4, M5). Two of the seventeen are design decisions the owner
should rule on before any unit opens — B1's population question and M1's parked fork — and both
belong in a §8 fork with a recommendation, not in a build pass.
