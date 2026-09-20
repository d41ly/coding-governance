**Serves:** spec-audit TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-6 TOOL-dTracedLattice-7

# dTracedLattice — spec audit of the seven-unit set, round 3: the never-read surface

*Node `d`, 2026-09-06. A Tier-2 adversarial pass over the two surfaces no review has ever touched:
units 6 and 7 in full, which have never been audited at all, and the text specs 1–5 gained at rev-4,
rev-5 and rev-6 — revisions driven by owner ratifications, a measurement reversal, and reconciliation
against node `a`'s `aWeighedCompass`/`aTunedCompass` landing on `main` mid-build, none of which came
out of rounds 1 or 2. Round 1 returned BLOCKED (3 blockers / 8 highs / 2 mediums, all folded);
round 2 returned BLOCKED (2 blockers / 4 highs / 2 mediums, all folded at rev-3). This repo's own
`fold-text-is-unreviewed-surface` gotcha is the reason for the scoping: most round-N findings live in
text the previous fold added, and here five specs moved three further revisions with no review
behind them. A primed finder fan, a skeptic stage prompted to REFUTE each finding, one synthesis.
Every finding below carries a `file:line` from the TREE and was re-checked against source before it
was written down.*

**Round: 3.** Subjects, each pinned at the blob it was read at:

- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-1.md@b36074ac0978f8d84cf832422669c87152ec16a0`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-2.md@bfb2d7fbcc2177772734a15caaccbdaf94d22d1a`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-3.md@699f55934ff56c48565833e894d670df31fd71a7`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-4.md@a87249ac2f47bf7bb839a7f704102a753c8e5adc`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-5.md@2203846f31e9cf4f1e7412f0eed853fac0eb335d`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-6.md@d18a73c98649df70d32711b02024777974abcc9a`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-7.md@859af1ffe6e4b8dc0f39628aeacbe20e286b2223`

Range reviewed: the seven blobs above, plus the build README and the tree they cite at `HEAD`.

## Verdict: BLOCKED

Three blockers, twelve highs, four mediums and one low. All three blockers are in the two specs
nobody had read: two in unit 6, which is order 1 across two builds and is still rev-1, and one in
unit 1's rev-6 text. The dominant defect class this round is not a bad design — it is a **stale
pointer**. Unit 1's rev-5 renumbered its own §2 and rewrote its §6, and nothing that cites those
items was re-pointed: not unit 1's own §5 and §8, not unit 5's two handoffs, not unit 6's entire
warrant. Eight of the twenty findings are one shape, and a builder following any of them lands on an
item that grades something else.

The second class is **an ungraded deliverable**: six scope items or ratified obligations are named by
no acceptance criterion, so the unit can be closed at its Definition of Done with the thing it exists
to do left undone. The third is **a criterion that cannot fail** — unit 7's AC3 is green before the
fix, after it, and after a revert.

Nothing here reopens a question rounds 1 or 2 settled, and nothing here disputes the relations answer,
the three owner rulings, or the rev-6 design of unit 1.

## Review shape

Raw 51, confirmed 27, refuted 24, unverified 0, precision **0.53**.

Precision has moved 0.22 → 0.34 → 0.53 across the three rounds, and it is the first round to clear the
~0.5 floor `AGENTS.md` §8 asks for. Round 2's lever was requiring a `file:line` from the tree; this
round's was scope — pointing the fan at the never-read surface (units 6 and 7, and the rev-4/5/6 text)
rather than re-reading five specs two rounds had already been over. That is the move §8 prescribes
when precision is low: tighten scope, do not add agents. The fan was four lenses, unchanged from
round 2.

**Run integrity.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. No lens or batch was lost,
so a zero count in this report is evidence of absence rather than a hole in the fan — the finding set
is complete for the scope that was reviewed. There are no UNVERIFIED findings outstanding.

**Synthesis merge, stated because it changes the arithmetic.** The pipeline's duplicate detector is
structural and found 0. Semantically, seven of the 27 confirmed findings are second and third reports
of a defect another finding already carries, so this report presents **20 distinct defects**. The
merges are listed below; nothing was dropped, and each absorbed id is named in the row that carries it.

| Defect | Confirmed ids folded in |
|---|---|
| B1 unit 1 receiver-binding three-way contradiction | 17 |
| B2 unit 6 leaves three live callers unreachable | 30 |
| B3 unit 6 S3 states another artifact's limits | 44 |
| H1 unit 1 §10 calls the seam prior art | 48 |
| H2 unit 1 S8 withholding has no carrier | 22 |
| H3 unit 1 S6 graded by nothing | 6 |
| H4 unit 1 S9 graded by nothing | 9 |
| H5 unit 5 handoffs into unit 1 are dead | 10, 23 |
| H6 the held-legs paragraph is false in four specs | 21, 34, 28 |
| H7 unit 6's warrant cites the wrong item | 19, 32 |
| H8 unit 5 §10 orders the design §4 retracted | 20, 39, 51 |
| H9 unit 7 §7 inverts which legs are held | 26 |
| H10 unit 3 S1's ground is false at HEAD | 49 |
| H11 unit 7 AC3 cannot fail | 4, 37 |
| H12 unit 6 S1's move list is incomplete | 31 |
| M1 unit 5 AC1 drops the remedy half | 13 |
| M2 unit 3 has no criterion for the legacy file | 15 |
| M3 unit 4's header disclosure is ungraded | 16 |
| M4 unit 1's §5 and §8 pointers are stale | 24 |
| L1 unit 3 speaks of a resolved fork as open | 27 |

Severity is this report's adjudication, not the lens's. Three ids arrived at a lower severity than the
row they merged into carries: 37, 39 and 51 came in at medium and are folded into highs, because in
each case a second lens established the same defect at the higher grade and the merged row is graded
once.

## Findings

| # | Sev | Unit | Address | One line |
|---|---|---|---|---|
| B1 | blocker | 1 | §3 vs §4 vs §6 AC8 | the receiver-binding pass is in scope, out of scope and unbuildable at once |
| B2 | blocker | 6 | §4 Migration | three live lexicon callers cannot reach the moved resolver |
| B3 | blocker | 6 | §2 S3, §6 AC5 | the header AC5 mandates states the prototype's limits, not the function's |
| H1 | high | 1 | §10 final sentence | the reuse audit calls the ratified seam read-only prior art |
| H2 | high | 1 | §2 S8 | "withheld from adopters" with neither carrier in the write set |
| H3 | high | 1 | §2 S6 vs §6 | the liveness item is named by no criterion |
| H4 | high | 1 | §2 S9 vs §6/§8 | the `map_diff.py` item is graded by nothing and Q1 misroutes |
| H5 | high | 5 | §2 S4, §3 | both handoffs into unit 1 name items that own something else |
| H6 | high | 1,2,3,5 | §7 held-legs | a leg that runs on every bar is described as held |
| H7 | high | 6 | §1, §3, §5 | the whole warrant cites a scope item that disclaims the need |
| H8 | high | 5 | §10 closing | §10 orders two states, §4 orders three modes |
| H9 | high | 7 | §7 held-legs | held and unheld are exactly inverted |
| H10 | high | 3 | §2 S1, §10 | "every existing consumer" is false two ways out of three |
| H11 | high | 7 | §6 AC3 | the only merge-bar criterion is a guaranteed pass |
| H12 | high | 6 | §2 S1 | three of five transitive dependencies are unnamed |
| M1 | medium | 5 | §2 S3 vs AC1 | the refusal's remedy half is ungraded |
| M2 | medium | 3 | §5 vs AC3 | no criterion meets the file the ratification orphans |
| M3 | medium | 4 | §8 Q1 vs §6 | the header disclosure is ungraded |
| M4 | medium | 1 | §5, §8 Q1 | pre-rev-5 numbering in live cross-references |
| L1 | low | 3 | S2, §4, §10 | a ratified fork still spoken of as open |

---

## B1 — unit 1's receiver-binding pass is in scope, out of scope, and unbuildable at once

**Address:** `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-1.md` §3 (non-goals,
`:94`) against §4 Data model, §2 S6, and §6 AC8 (§5 perf row at `:182-183`).

§3 says "No receiver-binding pass in this unit. It was rev-1's S2; the measurements put it behind S1
and S2 and it needs its own spec." §4's Data model IS that pass — "A second pass resolves receiver
names to repo modules using the import statements already parseable with `ast`". S6 promises to report
"attribute sites bound, sites left unresolved", which only that pass can produce. §5 prices the pass at
a median 1.761 s against `build_reference_index`'s 0.595 s, and AC8 caps the unit at "at most 0.05 s
added, and no second full-corpus scan" — a +1.166 s delta against a 0.05 s ceiling. §3's own next
bullet ("A receiver that cannot be bound by import analysis alone stays unresolved") presupposes the
binding it excludes. Rev-5 demoted the pass and left §4, S6 and §5 unrevised.

**Impact.** A builder cannot tell whether to change `map_lib.fan_in`'s signature at
`tools/codebase-map/map_lib.py:823` to take a resolved definer set or to ship S1's name-merge alone,
and whichever they choose, one of §3, §4/S6 or AC8 fails the unit at its Definition of Done. This is
the central mechanism of the build's largest unit.

**Fix.** Pick one and make the other two agree. If the pass stays out — which §3, AC8 and the rollout
paragraph all imply — rewrite §4's Data model to describe only the definer-set change S1 needs, and
re-scope S6 to report what the index can already count (files scanned, layers unscanned, parse skips)
with no bound/unresolved split. If it stays in, delete the §3 non-goal and re-derive AC8's ceiling
against the 1.761 s measurement.

**Left-shift.** A spec-internal consistency leg: a scope item whose verb the non-goals negate is a
named refusal. Cheaply approximated by asserting that no §3 bullet's subject phrase reappears as a §2
scope item's subject phrase in the same document. Cheaper still and worth more: the AC-coverage leg in
the consolidated section below, which would have caught S6 independently.

*(One overreach in the original report, corrected here: unit 6's rescued resolver does keep a consumer
via unit 1's S8 harness, so the "decides whether unit 6 has any consumer at all" half of the impact is
wrong. The contradiction is not.)*

## B2 — unit 6 moves `resolve_import` out from under three live callers and never says how they reach it

**Address:** `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-6.md` §4 Migration,
and §2 S5. Tree: `tools/lexicon/lexicon.py:527` (`module_index = build_module_index(files)`), `:536`
(`scan_unselective_rules(layers, files, module_index)`), `:595`
(`check_layer_violation(rel, target, layers, module_index)`), which reaches `resolve_import` at `:436`.

S4 requires this unit to land FIRST and S5 requires the lexicon kit's behaviour unchanged, but the
destination is unreachable from the source. `tools/lexicon/lexicon.py:346-352` records in its own words
that `tools/codebase-map/` "is exactly that case: no Python import can ever produce the hyphen", and
`AGENTS.md` §12 bans a kit file naming a sibling kit by literal. The spec also refutes itself: S2
preserves precisely the rule `tools/lexicon/* -> tools/codebase-map/*`, so the lexicon importing its
own rescued resolver would violate the rule this unit exists to keep. Only `TOOL-aSurfacedLexicon-2`,
in a different build, deletes those callers.

**Impact.** The inter-build window resolves one of two ways nobody chose: the lexicon legs stay red
between the two landings, or the implementer silently duplicates the resolver and ships the second copy
§12 exists to forbid, with no parity gate over the pair. §5's "nothing is deleted here" does not rescue
it — it either contradicts S1's "move out of" or sanctions the duplicate.

**Fix.** §4 states the window disposition explicitly — copy-then-delete, with the deletion named as an
item `TOOL-aSurfacedLexicon-2` S1 already covers, or a declared `sys.path` seam with its §12 waiver —
and §6 gains an AC that `lexicon selftest` and `lexicon naming predicates` are green at the commit this
unit lands, before the sibling build runs.

**Left-shift.** The gate already exists and is not cited: `lexicon selftest` is `subject: kit` in
`tools/gate-legs.json` and is HELD on a plain bar, so this breakage would not surface until a
`GATE_SELFTESTS=1` run. Make the AC name that invocation. Structurally: a cross-build leg asserting
that a unit which MOVES a symbol names every surviving caller's disposition — see the consolidated
section.

## B3 — unit 6's S3 states the limits of the research prototype, not of the function being moved

**Address:** `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-6.md` §2 S3
(`:28`), §6 AC5 (`:86`). Tree: `tools/lexicon/lexicon.py:386-433` versus
`memory/builds/dTracedLattice/build/2026-09-05-build-TOOL-dTracedLattice-1-resolver.py:48/50/63/70/103-104`.

S3's two limit claims — "binds same-directory sibling imports" and "resolves 554 sites against 9112
unresolved attribute sites" — are properties of the committed research prototype, which carries the
same-directory filter (`Path(c).parent.as_posix() == d`) at both import branches and counts
`resolved_sites` / `unresolved_attr_sites` over `ast.Attribute` nodes. `lexicon.py`'s `resolve_import`
takes `(target, importer, index)`, returns candidate repo paths, and contains no `ast.Attribute`, no
`unresolved`, and no site counting at all. It is also not same-directory-bound: for a dotted Python
target the importer's directory "gets no precedence" (`:414-421`), and a bare name falls back to
`local or hits`. The provenance is on record — the dossier attributes the figure to "The AST resolver"
at `2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md:231`, and round 1's B2 already established
that the scratchpad harness carries its own resolver.

**Impact.** AC5 makes shipping that header a Definition-of-Done item, so the unit **cannot be closed
truthfully as written**: the moved function would ship a header pinning another artifact's measurement,
and the header understates the function's actual reach while sounding precise. This is the exact class
the build README names as its load-bearing lesson — "a measurement that described a different artifact"
— reproduced inside the build that learned it.

**Fix.** Rewrite S3 from `lexicon.py:386-433`: `resolve_import` returns CANDIDATE paths (empty means
external or unresolvable, never a violation), it is language-branched on the importer's extension, and
for a bare Python name it prefers the importer's directory but falls back to every stem hit. Move the
554/9112 attribute-site figures into a sentence that names the prototype as their source, or drop them.
Restate AC5 over the candidate-set semantics and the language branch, not "the site-resolution figures".

**Left-shift.** This build's own measurement-provenance rule is the gate: a figure quoted in a spec
carries the artifact it was measured on. A leg over `memory/builds/*/spec/*.md` requiring every numeric
claim in a §2 scope item to cite either a tree path or a build-folder artifact would have caught it,
and is the same discipline `AGENTS.md` §7's "NO count of a derived population is written in prose"
already asserts for code.

---

## H1 — unit 1's reuse audit calls the ratified seam read-only prior art

**Address:** `…-TOOL-dTracedLattice-1.md:294-297` (§10, final sentence), against S8 and the rev-4 log.

§10 still reads "`resolve_import` … is SPECCED for deletion by `TOOL-aSurfacedLexicon-2` at order 1, so
it is prior art rather than a seam to wire through". Rev-4's owner ratification reversed exactly that:
S8 says "The AST resolver comes from `TOOL-dTracedLattice-6` at order 1" and the rev-4 log says "S6
extends `TOOL-dTracedLattice-6`'s resolver instead of building one". The same sentence routes the prior
art to "S2", which after the rev-5 reorder is the behaviour-phrase-to-seam stem bridge.

**Impact.** §10 is the section a builder reads to find the seam — `memory/TEMPLATE-SPEC.md` §10 makes
it mandatory — and it sends that reader away from a seam that exists, then to the wrong scope item.

**Fix.** Replace the final sentence: `resolve_import` is the seam, wired through by
`TOOL-dTracedLattice-6` which rescues it into `tools/codebase-map/` at order 1 before
`TOOL-aSurfacedLexicon-2` S1 deletes it; its consumers here are S6 and S8. Delete the "prior art rather
than a seam" framing and the S2 reference.

**Left-shift.** The cross-reference resolver leg (consolidated section) catches the S2 half; the
"prior art" half needs the §10 claim to name the unit that owns the seam, which the same leg can check
by requiring any `TOOL-<slug>-<n>` cited in §10 to be a real id.

## H2 — unit 1's S8 claims files are withheld from adopters with neither carrier in the write set

**Address:** `…-TOOL-dTracedLattice-1.md` §2 S8, against §6 and §7. Tree:
`tools/codebase-map/kit.toml:9-11` (`include = "**"`, `role = "engine"`),
`tools/memory-recall/kit.toml:23-25` (the `role = "project-owned"` precedent),
`WIRE-INTO-PROJECT.md:311` (codebase-map copy-install) and `:375` (the memory-recall removal line).

S8 lands new tracked files under `tools/codebase-map/` and asserts "A fixture measured against THIS
corpus is withheld from adopters, the way `recall-fixture.json` is". That precedent takes two tracked
edits this spec makes nowhere — a `[[files]] … role = "project-owned"` claim in the kit descriptor and
a removal row in the copy-install runbook, because a `cp -r` does not read `kit.toml`. Neither file is
in this unit's write set, no AC grades the withholding, and §7 says "No new leg".

**Impact.** `tools/codebase-map/kit.toml` declares `include = "**"`, so a new file in that directory
SHIPS by default and no gate objects. The variant harness, the scenario sets and a corpus-specific
graded fixture would land in every adopter's tree — the pin-copied-from-another-corpus shape the
`kit.toml` comment was written to prevent — while the spec claims they are withheld.
`tools/codebase-map/kit.toml` is also unit 4's S4 write target, so the omission hides a second write-set
intersection the README's sequencing bullet does not name.

**Fix.** Add both carriers to S8 explicitly and give them a criterion: after this unit lands, `govkit
apply` writes none of the new fixtures and the copy-install runbook removes them.

**Left-shift.** A `deploy your own tooling as a DECLARED population` leg already exists in spirit
(`AGENTS.md` §7). Extend it: a new tracked file under a kit dir whose descriptor declares
`include = "**"` must be claimed by a `[[files]]` role, or the leg reds. That is a ratchet over
`kit.toml`, not over prose, and it would have caught this without anyone reading the spec.

## H3 — unit 1's S6, the item implementing the charter's liveness rule, is graded by nothing

**Address:** `…-TOOL-dTracedLattice-1.md` §2 S6, against §6 (AC1–AC11) and §5 (`:189-190`).

S6 — "Report the index's own coverage on every call: attribute sites bound, sites left unresolved, and
every language layer not scanned at all" — is named by no criterion; grepping the whole AC block for
coverage, unresolved or layer returns nothing. §5 contradicts itself two lines apart: `:189` says "The
skip is counted and reported by S6" and `:190` says "observability — S3 is the observability item",
where S3 is the stem-specificity secondary sort key at `:59`.

**Impact.** A builder can ship the ranking changes, skip the reporting, and be green on every AC. The
mislabelled §5 row makes S6 look already accounted for, which is how it stays unnoticed. This is the
item that satisfies `AGENTS.md` §7's rule that a probe which cannot move must say so.

**Fix.** Add an AC over `reuse_lookup`'s own output — it prints bound sites, unresolved sites and
unscanned layers on every call, asserted by an arm that reds when any of the three is absent. Correct
§5's observability row to name S6. Note the interaction with B1: if the receiver-binding pass stays out
of scope, the bound/unresolved split cannot be reported and S6 must be re-scoped first.

**Left-shift.** The AC-coverage leg (consolidated section): every `S<n>` in §2 is named by at least one
criterion in §6.

## H4 — unit 1's S9 is graded by nothing and §8 Q1 promises a disclosure no criterion obliges

**Address:** `…-TOOL-dTracedLattice-1.md` §2 S9, against §6 and §8 Q1. Tree:
`tools/codebase-map/map_diff.py:204` (the `fan_in` call) and `:207` (the `dead_exports` figure), both
verified at base `c4fcf5ad`.

S9 — "Update `tools/codebase-map/map_diff.py`, which calls `fan_in` at `:204` and computes the
dead-export figure at `:207`" — is named by no criterion: no AC mentions `map_diff.py`, `dead_exports`,
or the 451→532 movement. Q1 says "this unit reports the movement per AC8", and AC8 at rev-6 is the
0.05 s cost ceiling. The rev-2 log records `map_diff.py` entering the write set "as S7 with AC8"; rev-5
renumbered both and left the citation behind.

**Impact.** The write-set item §4 says every production call site must satisfy is graded by nothing,
and Q1 points a reader at a criterion about wall clock. The `dead_exports` inflation this unit knowingly
causes can land unreported, in the same run that tells `TOOL-aScouredKit-17`'s next reader they are
comparing two trees.

**Fix.** Add an AC that `map_diff.py --converge` is produced with the definer-set signature and reports
the fan-in-0 population before and after, naming both readings and the sha each was taken at; repoint
Q1 at that AC's number. AC10 is already the disclosure-shaped criterion and is the cheaper home.

**Left-shift.** The same AC-coverage leg as H3, plus the cross-reference resolver, which catches
"per AC8" pointing at a criterion whose text has nothing to do with the claim.

## H5 — unit 5's two handoffs into unit 1 name items that own something else

**Address:** `…-TOOL-dTracedLattice-5.md` §2 S4 and §3 (bullet 3), against
`…-TOOL-dTracedLattice-1.md` at rev-6. Tree: the banner at
`tools/codebase-map/reuse_lookup.py:443-446`.

S4 says "`TOOL-dTracedLattice-1` AC3 owns the banner rewrite"; unit 1's AC3 is the 200-shuffle chance
control, and the word "banner" appears zero times in the whole of unit 1 at rev-6. §3 says "Not the
coverage reporting inside `fan_in` — `TOOL-dTracedLattice-1` S3 owns that"; unit 1's S3 is the
stem-specificity sort key and its S6 is the coverage report — the same S3/S6 slip unit 1's own §5
carries.

**Impact.** S4's whole design is to hand a derived value to an output another unit rewrites, and unit
5's sequencing after unit 1 rests on that handover. As written it has no owner: the banner is graded by
nothing in unit 1, so unit 5 can land its derived set into an output whose shape unit 1 never
contracted, and §3's boundary against double-reporting fences off the wrong item. These are label
references into a sibling spec's current text, so no base-drift defence applies.

**Fix.** Repoint §3 at unit 1's S6. For S4, either get unit 1 to add a criterion for the banner's
contents, or state that unit 5 owns the banner outright with AC2 and AC4 as its criteria. An ungraded
handover between two sequenced units is what `BUILD-METHOD.md` M6 clause 3 is about.

**Left-shift.** The cross-reference resolver leg — this is its single highest-value case, since both
citations are dead against the current sibling text.

## H6 — the held-legs paragraph is false in four specs, about the gate one of them exists to change

**Address:** `…-TOOL-dTracedLattice-2.md` §7 (the held-leg disclosure sentence), with byte-identical
text in specs 1, 3 and 5. Tree: `tools/gate-legs.json` gives `codebase-map coverage + freshness`
`"subject": "repo"`, `"chunk": "declarations"` and **no guard**; `tools/run-gates/run-gates.sh:947-948`
holds a leg only when `subject = kit` OR `chunk = selftests`.

The sentence "Both `codebase-map kit selftest` and `codebase-map coverage + freshness` are kit-subject
legs and are HELD on a plain bar" is false about the second leg, which is neither kit-subject nor
guarded: it runs on every bar in this repo and in every adopter. Verified identical at the pinned base
`c4fcf5ad` and at HEAD, so this is fold text, not drift. Spec 4's variant of the sentence is correct,
because its two legs really are `subject: kit`. **Spec 3 has a second defect on top:** the leg its
sentence names is not in its own §7 leg list (`codebase-map kit selftest` · `memory hygiene` ·
`dead-path carriers` · `harness arms`), so its declared merge bar describes a bar the unit does not run.

**Impact.** That leg's argv is `python3 tools/codebase-map/test_codebase_map.py` — unit 2's write
target. Four builders are told the gate over their own diff is dormant unless `GATE_SELFTESTS=1` is
passed, when a red there fails every commit's bar everywhere. A plain-bar green gets misread as "the
leg was held"; a plain-bar red gets misattributed to a leg the spec says was not exercised.

**Fix.** In specs 1, 2 and 5 the sentence names only `codebase-map kit selftest` as held and records
that `codebase-map coverage + freshness` runs on every bar. In spec 3 the sentence drops the leg
entirely, and discloses the hold for `codebase-map kit selftest` alone.

**Left-shift.** A leg-name-and-classification check over spec §7 blocks: every leg named must exist in
`tools/gate-legs.json`, and any claim that it is held must agree with the manifest's
`subject`/`chunk`. This is `AGENTS.md` §16's rule — the expected leg set is READ from the manifest,
never typed into a document — applied to spec prose, and it is mechanical.

## H7 — unit 6's entire warrant cites a scope item that now disclaims the need

**Address:** `…-TOOL-dTracedLattice-6.md` §1 Goal, §3 (first bullet) and §5 perf/scale, against
`…-TOOL-dTracedLattice-1.md` at rev-6. Tree: `tools/lexicon/lexicon.py:386`.

§1 and §3 say "`TOOL-dTracedLattice-1` S6 needs exactly that capability as a tracked file" and "Nothing
here improves the resolver; `TOOL-dTracedLattice-1` S6 does that". Unit 1's S6 is now the
coverage-report item, and unit 1 §3 now says "No receiver-binding pass in this unit" — so nothing in
unit 1 improves the resolver. The surviving consumer is unit 1's S8 ("The AST resolver comes from
`TOOL-dTracedLattice-6` at order 1"). §5 says "unit 1 S4 re-declares the ceiling once it has a
consumer"; unit 1's S4 is "Report a miss as a miss", and unit 1 §5 records that the re-declaration
moved onto AC8 at rev-5.

**Impact.** Unit 6 is order 1 across two builds — the first thing this build builds — and is a pure
move justified entirely by a downstream consumer. Every pointer to that consumer names the wrong item,
and the improvement §3 promises is one unit 1 explicitly declines. A builder verifying the premise at
`tools/lexicon/lexicon.py:386` cannot confirm the rescue is still needed or who re-declares its cost
ceiling. Unit 6 is still rev-1; unit 1 has moved five revisions under it.

**Fix.** Point §1 and §3 at unit 1 S8, the tracked variant harness and its `ast`-verified edge fixtures.
State plainly that no unit currently improves the resolver — the receiver-binding pass has its own
future spec per unit 1 §3 — and change §5 to name unit 1's AC8 rather than S4. Add a §8 line recording
that unit 1's scope numbering moved at rev-5, so the next reconciliation is cheap.

**Left-shift.** The cross-reference resolver leg. A stronger version, worth the extra work here: when a
spec is re-versioned, any sibling spec citing one of its `S<n>`/`AC<n>` labels is listed for
re-pointing — the same class as `AGENTS.md` §7's lockstep-invariant guard.

## H8 — unit 5's §10 orders the design §4 retracted

**Address:** `…-TOOL-dTracedLattice-5.md:182-184` (§10 closing paragraph), against §4 `:79-89`
("Alternatives rejected"). Tree: `tools/codebase-map/map_extractors.py:226` — verified, the `kit-js`
entry is labelled "Export scan UNION definition probe".

§10 still ends "this unit narrows that three-mode design to two states for the reason §4 gives". §4 at
rev-3 says "This unit ADOPTS the three-mode vocabulary rather than narrowing it" and destroys the
narrowing premise: "Rev-2 justified a two-state model by asserting codebase-map has no probe tier. That
is false". §10 does not merely state the retracted design — it cites as its ground the section that
refutes it. Round 2's H3 fixed the claim where it was reported and left this copy standing.

**Impact.** Two sections order opposite implementations of the unit's only deliverable, and §10 is the
half a builder reads last. An implementer following §10 ships parser/dark and mislabels the `kit-js`
layer as covered when `map_extractors.py:226` records it as a documented floor — precisely the
false-coverage failure §1 says this unit exists to prevent.

**Fix.** Rewrite the closing paragraph: `tools/lexicon/` implements `AGENTS.md` §12's
declared-coverage-mode rule and this unit ADOPTS its three modes — parser, probe, dark — citing
`map_extractors.py:226` as the probe tier that forced it, with `tools/lexicon/lexicon.py:167`'s
definition-carrier filter as S2's prior art.

**Left-shift.** Hard to gate mechanically; this is the class `AGENTS.md` §10 keeps as a documented
manual check. The cheap approximation that would have caught it: when a fold rewrites §4's
"Alternatives rejected", §10 is re-read in the same pass, because §10 is where the rejected alternative
is usually restated. Add that as a fold checklist line in `BUILD-METHOD.md`.

## H9 — unit 7's §7 inverts which recall legs are held

**Address:** `…-TOOL-dTracedLattice-7.md` §7 (held-legs paragraph), against S3 and AC1. Tree:
`tools/gate-legs.json` gives `recall floor arms` (argv `python3 tools/memory-recall/test_recall_floor.py`)
`subject: repo` with `chunk: selftests`, and `recall floor` `subject: repo` with `chunk: declarations`,
guarded on `tools/memory-recall/`; `tools/run-gates/run-gates.sh:947` holds on EITHER predicate.

§7 says "The kit-subject legs are HELD on a plain bar", which covers only `memory-recall kit selftest`.
`recall floor arms` is held too, by its chunk. `recall floor` is not held and does run on a plain bar.
The runner's own comment at `:933-938` names this exact mistake — the subject-only predicate "left SIX
legs in the `selftests` chunk running on every bar … the recall floor arms" among them.

**Impact.** `recall floor arms` runs `test_recall_floor.py`, the natural home for S3's multi-`PYTHONHASHSEED`
arm and the leg that grades AC1 — the unit's only left-shift. A builder reading §7 believes that arm
executes on a plain bar and can land the fix with the arm never having run: green by absence, which is
the shape S3 exists to close.

**Fix.** Name the legs and the predicate: `memory-recall kit selftest` (subject=kit) and `recall floor
arms` (chunk=selftests) are held and need `GATE_SELFTESTS=1`; `recall floor` and `harness arms` run on
a plain bar, which is what makes AC3's plain `bash tools/run-gates/run-gates.sh` spelling correct.

**Left-shift.** The same manifest-classification leg as H6, which covers both.

## H10 — unit 3's S1 rests on a claim that is false at HEAD, and instructs a write that reds its own AC6

**Address:** `…-TOOL-dTracedLattice-3.md` §2 S1 and §10 (`:144-150`). Tree:
`tools/run-gates/run-gates.sh:95` (`GD="$(git rev-parse --git-dir …)"`) and `:158`
(`LEDGER="$gd/gate-ledger.tsv"`), `tools/push-main.sh:29`
(`marker="$(git rev-parse --git-dir)/push-main-active"`), `tools/memory-recall/query.py:233`
(`--git-common-dir`, with its reason at `:229`).

S1's ground — "every existing consumer uses the former [`--git-common-dir`]" — is false two ways out of
three, and §10's reuse evidence ("the gate runner writes `gate-ledger.tsv` under the same root") is
false in precisely the linked-worktree case S1 invokes as its reason, which is the case this build is
running in. S1 also tells a builder to write "beside `gate-ledger.tsv`", which resolves to
`.git/worktrees/<name>/`, while AC6 requires the write to follow `--git-common-dir`.

**Impact.** The ratified destination is right and its justification is wrong, which is worse than
either alone: a builder following S1 literally reds AC6, and a reader checking the reuse evidence finds
it does not hold. Note `run-gates.sh` itself uses `--git-common-dir` at `:421` for a different purpose,
so the tree is not uniform and cannot be summarised in one clause.

**Fix.** Correct S1: ONE existing consumer uses `--git-common-dir` (`query.py:233`), the gate runner
and lander use `--git-dir` (`run-gates.sh:95`/`:158`, `push-main.sh:29`), and this unit deliberately
follows the former because the record must survive `git worktree remove`. Drop "beside
`gate-ledger.tsv`" from S1 and §10, or qualify it as a different root.

**Left-shift.** A quantifier check is the general form and it is cheap: a spec claim of the shape
"every existing consumer …" must cite the enumeration that establishes it. `AGENTS.md` §7's "NO count
of a derived population is written in prose" already bans the numeric version of this; "every" is the
same claim with the count elided.

## H11 — unit 7's only merge-bar criterion cannot fail on this tree

**Address:** `…-TOOL-dTracedLattice-7.md` §6 AC3, against §4. Tree: `.memory-tree.conf:286`
(`RECALL_FLOOR="records:fts5:r@5>=0.81"`), `tools/memory-recall/check-recall.py:203`
(`bench.rank_with(pin["sub"], …)`), `tools/memory-recall/bench.py:308-330` (dispatches `run_rm3` only
for `sub == "rm3"`).

AC3 asks the `recall floor` leg to report the same score on two runs. That leg grades `fts5`, which
this spec's own §4 records as byte-identical across all fourteen runs, and it never executes `run_rm3`
at all. AC3 is therefore green before the fix, after the fix, and after a revert. §3 forbids changing
which substrate this repo pins, so it cannot be made red either.

**Impact.** The one acceptance criterion naming the merge bar is a tautology on this tree — the
could-not-fail shape `AGENTS.md` §7 names, and a class this build has already folded once (round 1's
H2 on unit 2's AC4). Gate readers are told the leg is now stable when the leg was never unstable. AC1
carries the real observation alone, which is what limits this to high rather than blocker.

**Fix.** Drop AC3, or restate it over an invocation that reaches the code — `python
tools/memory-recall/bench.py --subs rm3` run twice under different `PYTHONHASHSEED` values, or the
floor leg with the floor overridden to an `rm3` substrate, with the pre-fix run observed RED. Say
plainly in §5 that this repository's own floor leg does not exercise `rm3`, so the merge bar is not
where this fix is verified. If AC3 is kept as a negative control, label it one — a control is not an
acceptance criterion.

**Left-shift.** `AGENTS.md` §7 already binds it and the spec template can enforce it: a new gate is not
landed until its failing case has been observed. Make "pre-fix run observed RED" a required field on
any AC that names a gate leg, and this AC cannot be written.

## H12 — unit 6's S1 names two of the five things that must travel

**Address:** `…-TOOL-dTracedLattice-6.md` §2 S1. Tree: `resolve_import` (`tools/lexicon/lexicon.py:386`)
calls `_resolve_relative` at `:399`/`:408`, `_check_path_suffix` at `:417`/`:432`, and `ext_of` at
`:396`/`:417`/`:422`/`:432` (plus `:382` transitively inside `_resolve_relative`).

S1 names only `resolve_import` and "the module index it resolves against". `_check_path_suffix` and
`_resolve_relative` are both on `TOOL-aSurfacedLexicon-2` S1's deletion list, so a move of only the two
named items ships a rescued resolver whose helpers are deleted under it by the very unit this rescue
exists to beat. `ext_of` is the opposite problem: it is read at eight further lexicon sites (`:171`,
`:521`, `:551`, `:611`, `:727`, `:940`, `:995`, `:1077`), is absent from the deletion list, and cannot
move — so the rescued copy must DUPLICATE it, which S1 does not authorise and §3's "no new capability"
does not cover.

**Impact.** A spec that troubles to enumerate what travels enumerated an incomplete set, and the two
omissions fail in opposite directions. Compounds B2: the duplication question is now open for `ext_of`
as well as for the whole resolver.

**Fix.** S1 enumerates the transitive closure — `build_module_index`, `_resolve_relative`,
`_check_path_suffix`, `resolve_import` MOVED; `ext_of` COPIED with the duplication stated — and AC1
gains the assertion that the moved module imports nothing from `tools/lexicon/`.

**Left-shift.** AC1's assertion is itself the gate and it is worth writing as a leg rather than a
one-time check: the moved module has no `tools/lexicon` import, asserted by the lexicon kit's own
layer-direction rule, which already exists in `.lexicon.conf` and is the mechanism S2 preserves.

---

## M1 — unit 5's AC1 grades two of the three things S3 requires

**Address:** `…-TOOL-dTracedLattice-5.md` §2 S3 against §6 AC1.

S3 requires the refusal to name the layer, its file count, and the two ways to clear it. AC1 grades
"the run REFUSES naming that layer and its file count". AC2 grades behaviour after the extension is
declared, AC3 the stale-declaration case, AC6 a different refusal. None observes the remedies, and §5's
risks row ("the message must make clearing it a one-line conf edit") is likewise ungraded.

**Impact.** The remedy half of the deliverable message can be omitted or degraded with every AC green.
An adopter then meets a refusal that names a problem and no repair.

**Fix.** Extend AC1 to assert the refusal names both clearing paths — register an extractor, or add the
extension to `RECALL_DARK_LAYERS` — with the conf key spelled as an adopter would type it.

**Left-shift.** The AC-coverage leg, extended one notch: a scope item enumerating N required elements
is matched against criteria naming all N. The enumeration is explicit in S3's text, so this is
checkable.

## M2 — unit 3 has no criterion for the file its own ratification orphans

**Address:** `…-TOOL-dTracedLattice-3.md` §5 risks, against §6 AC3.

§5 requires that an adopter who has already run `--converge` be told about the untracked
`memory/map/reinvention-backlog.md` this change orphans ("the message must say so rather than deleting
anything"). AC1 is explicitly scoped to a CLEAN fixture worktree; AC2 grades the zero-flag case; AC3
grades only that a fresh run "names the path it wrote them to"; AC6 the linked-worktree path. Nothing
observes the migration case, which exists only because rev-4's ratification moved the destination.

**Impact.** The run can relocate its output silently and leave a stale file inside the gated memory
tree with nothing said — the same shape as the original defect this unit exists to fix.

**Fix.** Add an AC over a fixture that already carries `memory/map/reinvention-backlog.md`: the run
names the legacy path, states it is no longer written, leaves the file in place, and `git status` still
shows it — observed before the fix so the silent case is seen once.

**Left-shift.** The AC-coverage leg does not reach this one, because the obligation lives in §5 rather
than §2. Widen it: a §5 risks row phrased as an obligation ("the message must …") is a gradable claim
and needs a criterion, same as a scope item.

## M3 — unit 4's ratified header disclosure is graded by nothing, while its sibling grades exactly that

**Address:** `…-TOOL-dTracedLattice-4.md` §8 Q1 and §5, against §6.

Q1 resolves to "the discriminator ships with its limit stated in the check's own header rather than
implied away", and §5 repeats it. No criterion observes that header text: AC1 grades a failure, AC2 a
customised pass, AC3 the unset-`GATE_FILE` skip, AC4 `kit.toml`. Unit 2's AC3 grades precisely this
disclosure on the same kit ("its header states which staleness classes it does not detect").

**Impact.** The known blind spot — a gate naming an artifact but comparing it wrongly still passes —
can be dropped with a green bar, leaving a structural check that reads as a semantic one. `AGENTS.md`
§7 makes the header disclosure a rule, not a nicety.

**Fix.** Add an AC mirroring unit 2's AC3: when the new check's source is read, its header states that
it compares the SET of artifacts each side handles and does not verify that a named artifact is
compared correctly.

**Left-shift.** Gateable directly and worth more than the AC: a leg asserting every check script under
`tools/` carries a "does not check" clause in its header. `AGENTS.md` §7 already states the rule; this
would be the first mechanical enforcement of it.

## M4 — unit 1's live cross-references still use pre-rev-5 numbering

**Address:** `…-TOOL-dTracedLattice-1.md` §5 observability row and §8 Q1.

§5 says "observability — S3 is the observability item"; S3 is the stem-specificity sort key and S6 is
the coverage report. §8 Q1 says "`TOOL-aScouredKit-17` … says it should land with `-16`, the row S5
amends"; S5 subtracts same-name definers and S7 is the item that amends `TOOL-aScouredKit-16`. The
third pointer, "reports the movement per AC8", is carried by H4.

**Impact.** Three pointers resolve to the wrong item inside one document. §5's observability row leaves
S6 — already at risk from B1 and H3 — with no checklist owner.

**Fix.** Renumber: §5's observability row to S6, §8 Q1's amendment reference to S7. Repoint the AC8
citation per H4.

**Left-shift.** The cross-reference resolver leg, in its intra-document form, which is the cheapest
half to build: every `S<n>`/`AC<n>` mentioned anywhere in a spec exists in that spec's §2/§6.

---

## L1 — unit 3 still speaks of a fork the owner resolved

**Address:** `…-TOOL-dTracedLattice-3.md` §2 S2, §4 Rollout, §10, against §8 Q1.

Q1 carries "RESOLVED (owner, 2026-09-05): outside the worktree", the rev-4 log records the
ratification, and S1 states the ratified disposition including the `--git-common-dir` derivation. Yet
S2 opens "Whichever disposition wins", §4's Rollout sequences "S1 and S2 after the fork resolves", and
§10 reads "If Q1 resolves to the outside-the-worktree option, this unit follows that spelling".

**Impact.** §4's Rollout is an executable instruction telling a builder to wait on a decision already
made, and §10 leaves the one detail the ruling settles reading as provisional. Not a style point: this
build's own spec 5 §8 states the principle — the owner's ruling and an agent's earlier guess must not
be indistinguishable afterwards — and spec 3 fails it.

**Fix.** Make all three unconditional: S2 states the destination, §4's Rollout drops "after the fork
resolves", and §10 states the unit follows the `<git-common-dir>` spelling of
`tools/memory-recall/query.py` and the gate ledger, per the ratified Q1.

**Left-shift.** Mechanical and small: in a spec whose §8 marks a question RESOLVED, the conditional
forms that name it ("if Q1 resolves", "whichever disposition wins", "after the fork resolves") are a
refusal. A grep-shaped leg over `memory/builds/*/spec/*.md`, and the one gate on this list that could
land in an afternoon.

---

## Left-shift, consolidated: four legs would have caught fourteen of these twenty

Per-finding suggestions are above; these are the four that repay building, ranked by findings covered.

1. **The cross-reference resolver.** Every `TOOL-<slug>-<n>` `S<k>`/`AC<k>` label cited in any spec —
   in its own text or a sibling's — resolves to an item that exists in the named spec's CURRENT text.
   Covers H1, H3, H4, H5, H7, M4, and half of B1. Six findings, all of them the same accident: unit 1's
   rev-5 renumbered §2 and rewrote §6, and nothing that cited those items was re-pointed. This is a
   lockstep invariant in `AGENTS.md` §7's sense, and it is entirely mechanical — the labels are
   regular and the target files are in the same tree. Build this one first.
2. **AC coverage over scope items.** Every `S<n>` in §2 is named by at least one criterion in §6, and
   every §5 risks row phrased as an obligation likewise. Covers H3, H4, M1, M2, M3. Five findings, all
   of them "the unit can be closed with the thing it exists to do left undone". Weaker than the first
   leg — a criterion can name an item and still grade nothing, as H11 shows — so it is a floor, not a
   proof, and its header should say so.
3. **Gate-leg claims read from the manifest.** Any leg named in a spec §7 exists in
   `tools/gate-legs.json`, and any held/guarded/runs-on-every-bar claim about it agrees with that
   file's `subject` and `chunk`. Covers H6 (four specs) and H9. This is `AGENTS.md` §16's rule — the
   expected leg set is READ at emission time, never typed into a document — applied to spec prose.
4. **A resolved fork is stated, never conditioned.** In a spec whose §8 marks a question RESOLVED, the
   conditional forms naming it are a refusal. Covers L1, and it is a grep.

Not gateable and left as documented checks: H8 (two sections ordering opposite designs — add a fold
checklist line that a rewrite of §4's "Alternatives rejected" re-reads §10), B3 (a figure quoted in a
spec carries the artifact it was measured on — the build README's own load-bearing lesson, and the
strongest candidate for a §10 checklist entry), and H10's quantifier check, which is the prose form of
§7's ban on writing a derived count in prose.

## Coverage notes, so a green row is not misread

- **This pass did NOT re-derive the dossier's measured figures.** The precision table, the medians and
  the 127-row / 329-edge ground truth are taken as reported, as in rounds 1 and 2. B3 is the exception
  and it is about attribution, not arithmetic: the 554/9112 figures are real, they were measured on the
  prototype, and the spec attributes them to a different function.
- **This pass did NOT re-audit what rounds 1 and 2 read and left alone.** Specs 1–5 were read only at
  the text rev-4/5/6 added and at the sections that text made stale. Absence of a finding in the older
  half of those specs means no lens looked, not that nothing is there. Units 6 and 7 were read in full.
- **This pass did NOT verify buildability.** Every finding is about what the specs say. Whether unit
  1's rev-6 design achieves the precision it targets is a question for the build, not this audit — with
  the exception of B1, where the spec's own numbers make one reading of it unbuildable under its own
  criterion.
- **Run integrity was clean** — 4/4 lenses, 5/5 skeptic batches, nothing died, nothing demoted,
  nothing discarded. A zero in this report is a measurement.

## What this round says about the build

Unit 6 should not be built as written, and it is order 1, which makes it the whole build's blocker.
Unit 1's B1 has to be settled before either unit is built, because the answer decides what unit 6's
resolver is for.

The 27-finding raw count across seven specs after two folds is not a sign the specs are bad. Nineteen
of the 27 are pointers and coverage gaps created by revisions the earlier rounds never saw: rev-5's
renumbering of unit 1 alone accounts for eight. That is the `fold-text-is-unreviewed-surface` gotcha
being right again, and it is the argument for the first left-shift leg above — the defect class is
mechanical, it recurs on every fold, and a machine can find all of it.
