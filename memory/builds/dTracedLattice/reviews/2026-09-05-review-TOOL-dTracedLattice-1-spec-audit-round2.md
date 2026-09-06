**Serves:** spec-audit TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5

# dTracedLattice — spec audit of the five-unit set, round 2: the fold

*Node `d`, 2026-09-05. A Tier-2 adversarial pass whose PRIMARY SUBJECT is the round-1 fold, not the
specs round 1 already read. Round 1 returned BLOCKED with 3 blockers, 8 highs and 2 mediums; all
thirteen were folded at `c8f026ae` and every spec went to rev-2. The base `7880a523` is round 1's
reviewed tip, so `git diff 7880a523..HEAD` IS this pass's subject. This repo's own
`fold-text-is-unreviewed-surface` gotcha records 42 of 62 findings in a previous round 2 as CAUSED by
the round-1 fold, which is why the priming pointed the fan at the new text rather than at what round 1
left alone. A primed finder fan, a skeptic stage prompted to REFUTE each finding, one synthesis. Per
round 1's own precision note, every finding here was required to carry a `file:line` from the TREE and
was re-checked against source at `c8f026ae` before it was written down.*

**Round: 2.** Subjects, each pinned at the blob it was read at:

- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-1.md@a1ff31fc7004327bab5a6962b3ba10333f10dc8a`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-2.md@1ed6e491e774ff9cdd0d7f6874ef9fe3c80704e1`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-3.md@656f6dcfcc78152e6de6ca35ca9e13e4e6b6847a`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-4.md@bf55abe5c63bbad21921c4b9616e3c1c667443a8`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-5.md@809807c6603a711c77bce649932d9f7da047c711`

Range reviewed: `7880a523..HEAD` (the fold commit `c8f026ae`), plus the build README at the same tip.

## Verdict: BLOCKED

Two blockers stand and both are the same shape: a round-1 fix that fixed its symptom and left its
other half standing. Neither is a defect the fold invented from nothing — each is a round-1 finding
whose remedy landed on one side of a two-sided edit. The build README's independence bullet was
correctly rewritten and every spec was correctly re-versioned, so the fold's bookkeeping is sound.
What failed is the payload.

The scale is worth stating plainly, because it is the argument for reviewing folds at all. The fold
touched five specs and one README for 754 insertions. Every one of the eight defects below lives in
text the fold ADDED, or in text the fold should have touched and did not. Nothing in this report
re-opens a question round 1 settled, and nothing here disputes the relations answer or the rev-2
design.

## Review shape

Raw 38, confirmed 13, refuted 25, unverified 0, precision 0.34. The 13 confirmed findings collapse to
8 distinct defects: three lenses independently landed on the unit-1 receiving half, and four on the
`fan_in` call-site enumeration, which is what a fan does when a defect is both real and conspicuous.

Precision rose from 0.22 to 0.34 after round 1's priming change — require a `file:line` from the tree,
not merely a section address in the spec — and that is the single most useful measurement this pass
produced. It is still under the ~0.5 floor `AGENTS.md` §8 sets, so on a document target the correct
next move remains tightening scope rather than adding agents. The residual 25 refutations were
dominated by the same class round 1 named: a lens reading rev-2 prose for internal consistency and
manufacturing a plausible-sounding complaint that no source check survives.

Two coverage notes, so a green row is not misread. The dossier's measured figures were again NOT
re-derived — the precision table, the medians and the 127-row / 329-edge ground truth are taken as
reported. Round 1's B2 remains the finding that nothing in the tree lets a builder check them; the
fold's S6 answers it, and this pass confirmed S6 exists without auditing whether what it describes can
be built. And this pass did NOT independently re-prove the ten round-1 folds it found clean. Absence
from this report means no lens raised a survivable complaint about that fold, which is weaker evidence
than a verification.

| Defect | Raw ids folded in |
|---|---|
| B1 the amendment's receiving half | 1, 10, 25 |
| B2 the enumeration that drops its own hard case | 2, 12, 23, 30 |
| H1 the threshold re-derivation with no criterion | 3 |
| H2 the exclusivity clause that moved the collision | 31 |
| H3 the probe tier this kit does have | 33 |
| H4 the extension population with no carrier filter | 34 |
| M1 the disclosure that landed in one spec of five | 7 |
| M2 "silently held", against the runner that names them | 16 |

## Findings

| # | Severity | Unit | Address | One line |
|---|---|---|---|---|
| B1 | blocker | 1, 3 | unit 1 §2 S5 and §6 AC6, against unit 3 §2 S3 and §6 AC4 | Unit 3 hands unit 1 three corrections; unit 1's scope and acceptance were never widened to receive them, so no unit's scope produces the edit unit 3's AC4 grades. |
| B2 | blocker | 1 | unit 1 §4 Data model, the fold-added paragraph | The new call-site enumeration omits the production site it then calls "the hard case" and substitutes one of five test assertions for it. |
| H1 | high | 1 | unit 1 §2 S8 and §6 AC7 | S8's deliverable — a re-derived threshold or a recorded measurement — has no criterion; AC7 grades a fixed-threshold regression pin instead. |
| H2 | high | 1, 3 | unit 1 §2 S7, against unit 3 §2 S1/S2 and §6 AC2/AC3 | "It is in this unit's write set, not unit 3's" claims a file exclusively that unit 3 cannot meet its own scope without editing. |
| H3 | high | 5 | unit 5 §4 Alternatives rejected | "codebase-map has no probe tier to declare" is false against the tree, and it is the sole justification offered for the two-state model. |
| H4 | high | 5 | unit 5 §4 Data model, against §6 AC1 | The chosen extension vocabulary carries no definition-carrier filter, so S2's refusal fires on nine data extensions of this repo's own tree. |
| M1 | medium | 1, 2, 3, 5 | each spec's §7 Gates | The held-leg disclosure round 1's M2 asked for in every spec landed in unit 4 only. |
| M2 | medium | 4 | unit 4 §7, the fold-added paragraph | "a builder ... sees them silently held" accuses the gate runner of a defect it was built to avoid and demonstrably does not have. |

---

### B1 — blocker — unit 1 §2 S5 and §6 AC6, against unit 3 §2 S3 and §6 AC4

**The defect.** Round 1's B1 fix said to move "the whole `TOOL-aScouredKit-16` amendment into exactly
ONE unit". The fold moved the GIVING side and never widened the RECEIVING side.

Unit 3's rev-2 S3 now reads: "Supply the three corrections `TOOL-aScouredKit-16` needs — it is not
tracked, the fiction is not permanent, it does not ship to adopters — to `TOOL-dTracedLattice-1`,
which is the ONLY unit that edits that row." Unit 3's AC4 grades exactly those three claims and closes
"This unit supplies the wording per S3 and does not edit the file."

Unit 1's S5 was touched by the fold only to gain the sentence "This unit is the ONLY one that edits
that row." Its payload is unchanged: "Amend `TOOL-aScouredKit-16` in place with the measurement that
rejects its second proposal." AC6 was not touched at all and still grades one thing: the row "carries
the amendment naming the rejected half and the measurement that rejected it."

Neither line reaches the three false clauses, and those clauses are live text. The row at
`memory/backlog/TOOL.md:294` carries "`map_diff.py --converge` APPENDED 31 WARN rows to the tracked
reinvention-backlog" and "that file is append-only and deduped, so the fiction is permanent and it
SHIPS to adopters". Two of the three are checkable in one command: `git ls-files | grep reinvention`
returns nothing, so the file has never been tracked and therefore cannot ship in an adopter's clone.
Unit 3's own §1 states the same fact.

**Why it is a blocker and not a documentation nit.** The failure is mechanical and ordered. Unit 1 is
order 1. Its builder implements S5 exactly, satisfies AC6 with the measurement amendment alone, and
lands DONE with all three clauses intact. Unit 3 then arrives at order 3 owning an acceptance
criterion — AC4, the row "no longer claims the backlog is tracked, that the fiction is permanent, or
that it ships to adopters" — whose satisfying edit its own S3 and AC4 forbid it to make. No unit's
scope produces that edit. AC4 is unsatisfiable by any pass following the specs, and unit 3 becomes
unlandable on a criterion it cannot itself reach.

One sub-claim a lens raised does NOT survive, and is recorded here rather than folded in: the ordering
is not itself the problem. Unit 3's spec is committed at rev-2, so the correction WORDING exists on
disk before unit 1 builds. The gap is ownership, not sequencing.

**Fix.** Widen unit 1 S5 to carry both payloads — the measurement that rejects the row's second
proposal AND the three factual corrections unit 3 S3 supplies — and extend AC6 to name all four claims
the amended row must no longer make. Add a cross-reference in S5 naming unit 3 S3 as the source of the
correction wording, so the handover is visible from the receiving side, and a line in unit 1 §9
recording that it absorbed it. The build README's "AMENDED by unit 1's measurement" bullet at
`memory/builds/dTracedLattice/README.md:43` needs the same widening, since "by unit 1's measurement"
now understates what unit 1 owes.

**Left-shift.** A `gen_build_index.py` check, and it generalises past this build: an acceptance
criterion whose text names ANOTHER unit's id ("When `TOOL-dTracedLattice-1` lands, ...") must have a
scope item in that named unit which the generated build-order block places at an earlier order. The
generator already parses every spec's §2 and §6 and already computes the order, so both halves are in
hand. This is the machine form of "acceptance and scope must agree", applied across a unit boundary,
which is exactly where a fold moves work and forgets one side.

---

### B2 — blocker — unit 1 §4 Data model, paragraph 2 (fold text), and the §9 rev-2 line's H1 clause

**The defect.** The fold added this paragraph to answer round 1's H1, whose fix said "enumerate all
four call sites in §4 and state what each one passes":

> `fan_in` has FOUR call sites in three files, not one: `map_diff.py:204`, `reuse_lookup.py:264` and
> `:274`, and `selftest.py:936`. Each must supply the definer set, and `detect_collisions` is the hard
> case ... a silent fallback to the old behaviour at one call site is how a precision fix half-lands.

The enumeration is wrong in both directions, and the omission is the one the same paragraph then
argues about. `grep -n 'fan_in(' tools/codebase-map/*.py` returns:

- `tools/codebase-map/map_diff.py:204` — production, the dead-export sum
- `tools/codebase-map/map_lib.py:1240` — production, `fe = fan_in(ref_index, e["id"], e["file"])`, INSIDE `detect_collisions` (defined at `map_lib.py:1204`)
- `tools/codebase-map/reuse_lookup.py:264` and `:274` — production, the ranking
- `tools/codebase-map/selftest.py:898`, `:899`, `:900`, `:901`, `:936` — five test assertions, not one

So there are four PRODUCTION call sites in FOUR files, and the paragraph substitutes one selftest
assertion for `map_lib.py:1240`. That is the exact call site round 1's H1 was filed about — the one
the very next sentence calls "the hard case" and then never locates, never gives an address for, and
never says what it passes.

**Why it is a blocker.** Three consequences compound, and the paragraph's own last sentence names the
first of them.

1. **The half-landing the paragraph exists to prevent.** An implementer working the list literally
   edits three files and leaves `map_lib.py:1240` passing a bare `e["file"]` string into a signature
   that now takes a definer set. Passing a `str` where a set is expected does not raise in Python, so
   the collision loop's `if fe < threshold` at `map_lib.py:1241` keeps applying the OLD counting to a
   number the ranking no longer uses. One symbol gets two fan-ins inside one kit.
2. **The write set has no line for it.** S7 justifies claiming `map_diff.py` by "line 204" and "207"
   only. No §2 item names `map_lib.py:1240`, and none names `map_diff.py:165-168`, which is
   `detect_collisions`'s only caller and the place a head definer set would have to be threaded
   through. The paragraph decides `detect_collisions` "is given one by its caller" without putting
   that caller in anyone's scope.
3. **No criterion observes the collision path at all.** §6 runs AC1 through AC8 and not one of them
   reads a fan-in through `detect_collisions`. The gap is therefore invisible to the bar as specced.

And the §9 rev-2 line records "H1 (§4 names `fan_in`'s four call sites and the `detect_collisions`
case)" as folded, so to the next reader the omission reads as verified.

**Fix.** Replace the enumeration with the four production sites and what each is given —
`map_diff.py:204` (head rows), `map_lib.py:1240` inside `detect_collisions` (today `e["file"]`, and
the honest answer about which pool it can build a definer set from is `base_symbols`, not head),
`reuse_lookup.py:264` in `seed_affordances`, `reuse_lookup.py:274` in `_rank`. List the five selftest
assertions separately as a consequential edit, not as a call site. Extend S7 to name
`map_diff.py:165-168`. Add a criterion that reads one pinned fan-in figure through BOTH
`reuse_lookup`'s ranking and the `detect_collisions` path over the same fixture, and reds when they
disagree. Correct the §9 H1 clause to say which sites were enumerated.

**Left-shift.** A gate for the class, since this is the second time a spec's enumeration of call sites
has been trusted and wrong: any spec paragraph asserting a COUNT of call sites for a named symbol has
that count re-derived from the tree at gate time. The shape is greppable — a backticked symbol name,
a numeral, and the words "call site" — and `map_lib.py` already ships the reference index that answers
it. The narrower and more valuable half: for any `path.py:NNN` cited in a spec's §2 or §4, assert the
line still exists and still contains the symbol the spec says it does. That single check would have
caught B2, and it catches every future line-number citation as the tree moves under it.

---

### H1 — high — unit 1 §2 S8 and §6 AC7

**The defect.** Round 1's H7 fix asked for three things. The fold landed one.

S8 is new and correct: "Re-derive `SEAM_FANIN_THRESHOLD` against the new metric, or record with the
measurement that `3` still means what it meant." AC7 is new and grades something else entirely: "When
`seed_affordances` is run on the fixture corpus at threshold `3` before and after S1, the seam
population is pinned at both readings, so any later change to `fan_in` that moves the seam set reds
rather than drifting."

That is a regression pin at a FIXED threshold of 3. It is a fine criterion for a different scope item.
It does not grade a re-derivation and it does not grade a recorded judgment, so S8's actual
deliverable — a new value with its reading, or a recorded measurement that 3 still holds — has no
criterion at all. A builder can skip S8 whole and AC7 still passes.

The other two things H7 asked for are simply absent, and both are checkable:

- The seam-count pin ON THIS TREE, which H7 asked for "the way AC4 already pins `load_conf`'s
  fan-in". AC7's population is the fixture corpus, not this repo. The magnitude of what goes
  unobserved is this repo's own measurement at `memory/backlog/TOOL.md:294`: "71 of 165 SEAMs fall
  below threshold on that filter alone" — 43% of the seam set moves and no criterion watches it.
- The adopter-facing lines. `.codebase-map.conf:29-31` still reads "Kept at the kit default of 3 —
  this is a small tree and the threshold has not been re-measured against it", which will be false the
  moment S1 lands and which the fold did not touch. Unit 1's §5 user-docs row at line 100 still says
  only that the READMEs "state what the ranking means", with nothing about the scale moving. An
  adopter who tuned their value against the old metric gets a silently stricter bar.

**Fix.** Add a criterion that grades S8's own fork — either the re-derived value with its reading, or
a recorded measurement that 3 still holds, observable in the diff. Add the seam-count-before-and-after
pin on THIS tree. Add a scope item updating the `.codebase-map.conf` comment and the kit README to
tell adopters the scale moved, and reflect it in the §5 user-docs row.

**Left-shift.** The general check, which this build keeps needing: every §2 scope item must be named
by at least one §6 criterion, and the mapping must be explicit rather than inferred. Round 1's H2
found a criterion grading a population of one, and round 1's M2 found a gate list that could not fire;
this is the third instance of acceptance and scope disagreeing, so the class is established. A checker
reading the two lists and reporting orphaned scope items is a `gen_build_index.py` addition, and its
failure case here is a one-line RED naming S8.

---

### H2 — high — unit 1 §2 S7, against unit 3 §2 S1/S2 and §6 AC2/AC3

**The defect.** The fold's S7 closes: "It is in this unit's write set, not unit 3's, because the
signature S1 changes is the one that line passes." The first half is right and was round 1's ask. The
clause after the comma is not, and it moved the collision rather than removing it.

Unit 3 cannot meet its own scope without editing `tools/codebase-map/map_diff.py`. The whole
disposition unit 3 exists to implement lives in one function, `_converge`, beginning at
`map_diff.py:140`:

- `map_diff.py:171` — `backlog_path = map_dir / "reinvention-backlog.md"`, the destination literal that IS unit 3's S1 fork
- `map_diff.py:174-177` — the read, the `m.append_backlog` call, and the write
- `map_diff.py:187` — the relative path printed to stdout, which unit 3's AC3 grades directly
- `map_diff.py:204` and `:207` — unit 1's `fan_in` call and dead-export figure

Unit 3's AC2 ("when the run produces zero flags, no `reinvention-backlog.md` is created") grades the
behaviour of `map_diff.py:173-177`. Its S2 requires `--converge` to leave the worktree clean, which is
the same block. Round 1's B1 fix enumerated unit 3's write set as "`map_diff.py`,
`memory/backlog/TOOL.md`, `tools/codebase-map/README.md`" and asked only that the file be DECLARED
inside unit 1's scope — never that it be made exclusive.

**Why it matters.** Both units land work in one function. The exclusivity clause tells whichever
builder runs second that the file is not their business, which is the silent-clobber setup at a merge
and precisely the confusion the README's rewritten sequencing bullet was meant to end. The build
README compounds it: the fold's bullet says "Collisions were removed rather than documented", and this
one was documented away rather than removed.

**Fix.** Restate S7 as line-range ownership rather than file ownership: unit 1 owns the `fan_in` call
and the dead-export figure at `map_diff.py:204` and `:207`; unit 3 owns the backlog destination at
`map_diff.py:170-177` and the stdout path at `:187`. Record `tools/codebase-map/map_diff.py` in BOTH
units' write sets with those ranges. The sequencing already permits this — the units are ordered 1 and
3 with Parallel `no` — so nothing about the dispatch changes, only the claim.

**Left-shift.** Extend the write-set check B1's left-shift proposes: a spec asserting EXCLUSIVE
ownership of a path ("not unit N's", "the ONLY unit that") reds when another unit in the same build
names that path in its own §2 or §6. Both sides are declared text in files the generator already
parses, and exclusivity claims are the ones worth machine-checking precisely because they are the ones
a reader trusts without looking.

---

### H3 — high — unit 5 §4 "Alternatives rejected"

**The defect.** The fold added a paragraph citing the lexicon kit, which round 1's H8 said unit 5
should have cited. It cites it and then dismisses it on a premise that is false against the tree:

> This unit deliberately keeps a TWO-state model rather than adopting the three-mode vocabulary,
> because codebase-map has no probe tier to declare: an extractor either exists for a layer or it does
> not.

This kit's own JS extractor IS a probe, and its source says so in those words.
`tools/codebase-map/map_extractors.py:226` labels the registry entry "Export scan UNION definition
probe". The `_build_js_layer` docstring at `map_extractors.py:205` records "MEASURED at `b4f0cf1c`: 3
export rows, 30 definition rows, DISJOINT" — one scan alone indexed 3 of 33. And
`.codebase-map.conf:24`, three lines above the `RECALL_DARK_LAYERS` value this same §4 quotes, calls
the JS coverage "an enumeration floor".

Round 1's H8 stated this exact fact. The fold answered the finding by asserting the negation of what
the finding proved, which is the most expensive way a fold can fail: the record now reads as though
the question was considered and settled.

**Why it matters, beyond the false sentence.** Under the two-state derived set this unit ships, `.js`
reports COVERED on the strength of an admitted enumeration floor. That is a falsely-confident "no seam
fits" for JS — the exact class `RECALL_DARK_LAYERS` was created to prevent, per
`.codebase-map.conf:22-27` and the `bConvergentLodestar` review that produced it — reintroduced by the
unit written to remove it. Unit 5's §3 does not withhold this: it excludes new extractors and changes
to `map_extractors.py`'s interface, and a coverage-mode declaration is neither.

**Fix.** Delete the false premise and decide the vocabulary on the tree as it is. Either adopt the
three-mode `parser | probe | dark` vocabulary the sibling kit already ships and declare `kit-js` a
probe, or keep two states and state the real cost in the same paragraph — that a probe-covered layer
is reported as covered. Either way add a criterion pinning the mode the JS layer is REPORTED at, so
the choice is observable rather than argued.

**Left-shift.** Hard to gate as prose, so this goes to the recurring-class checklist, with one
gateable half. The checklist entry: a spec that narrows a landed sibling's design must state the
narrowing's cost on THIS tree, and the review asks what the sibling's extra state would have caught
here. The gateable half is narrower and worth having on its own: an arm asserting that every
`SYMBOL_EXTRACTORS` entry whose own source comment or docstring contains "probe" or "floor" is
reported by `reuse_lookup` as something other than fully covered. That arm reds today on `kit-js`,
which is what makes it worth writing.

---

### H4 — high — unit 5 §4 "Data model", against §6 AC1 and §5 error-states

**The defect.** The fold rewrote §4 to fix the three-vocabulary blocker and picked extension as the
vocabulary: "The derived set is therefore `{extension -> file count}` over the same tracked walk the
index uses." The choice is defensible. What did not come across from the prior art it now cites is the
FILTER.

`tools/lexicon/lexicon.py:167` defines `scan_definition_carriers`, applied at `:662` and `:727`, with
its argued `SNIFF_SKIP` set at `:154`. It exists because a bare extension population reports prose and
data files as coverage holes. Unit 5's §4 specifies no filter at all, and it cannot be inheriting one:
the walk cannot be `build_reference_index`'s, which derives its extensions from the symbols the
already-covered layers produced, and AC4 requires the derived set to contain `.sh`, so it must be a
raw tracked walk.

Measured on this tree right now, that population is 12 extensions of which 9 carry no definitions
whatsoever:

| ext | files | ext | files |
|---|---|---|---|
| md | 1291 | js | 8 |
| sh | 94 | conf | 4 |
| py | 49 | example | 3 |
| toml | 30 | tsv | 1 |
| txt | 25 | gitignore | 1 |
| json | 9 | gitattributes | 1 |

S2 refuses "when a present layer is neither covered nor declared dark". On gov's own tree that fires
for `.md`, `.toml`, `.txt`, `.json`, `.conf`, `.example`, `.tsv`, `.gitignore` and `.gitattributes`
alongside the `.sh` it is meant to fire for. Clearing it means declaring nine data extensions dark in
`.codebase-map.conf` — the "reds an honest adopter whose dark extensions are all data files" failure
the lexicon kit already recorded and fixed.

Nothing in §6 can expose this. AC1's fixture is a single synthetic layer; §5's error-states row covers
only "a corpus with one layer and no declaration". This is the same shape round 1's H2 caught in unit
2 — a criterion over a population that cannot fail — arriving in a different unit via the fold.

**Fix.** Restrict the derived population to definition-carrying files, reusing
`scan_definition_carriers`'s shape and citing it in §4 and §10 rather than leaving the reuse audit
silent on it. Add a criterion that runs the derivation over THIS tree and asserts the refusal names
only layers a symbol extractor could plausibly cover — a criterion whose fixture is the repo, which is
the half AC1 is missing.

**Left-shift.** A gate, and it is nearly free: an arm that runs unit 5's derivation over the real
tracked tree and asserts the refusal set is a subset of the declared code extensions. It is the same
"run a candidate gate predicate over the real tree before wiring it" rule `AGENTS.md` §7 already
states, turned into an arm. Its value is that it makes the fixture-versus-tree gap structural rather
than something a reviewer has to happen to notice.

---

### M1 — medium — the §7 Gates section of units 1, 2, 3 and 5

**The defect.** Round 1's M2 fix said, in these words: "Add a line to each spec's §7 stating that the
kit-subject legs need `GATE_SELFTESTS=1`, since a builder reading §7 and running the plain bar will
see them silently held." The fold added that line to unit 4 and to no one else.

Unit 4 §7 now closes: "Both kit-subject legs are HELD on a plain bar and need `GATE_SELFTESTS=1`."
Unit 1 §7 still reads "`codebase-map kit selftest` · ... No new leg: the arms join the kit's existing
selftest", with no disclosure. Units 2, 3 and 5 list the same leg in the same silence.

The manifest is unambiguous. In `tools/gate-legs.json`, the `codebase-map kit selftest` entry carries
`"chunk": "selftests"` and `"subject": "kit"`, which the merge-bar section of `AGENTS.md` says
`GATE_FULL=1` holds and only `GATE_SELFTESTS=1` runs — on demand only, set by no boundary.

What that costs unit 1 specifically: AC1 and AC2, the headline precision and MAE criteria whose whole
point after the fold's S6 is that they are scorable by something tracked, are scored by arms in
`tools/codebase-map/selftest.py`. So are AC5 and AC7. None of them runs on
`bash tools/run-gates/run-gates.sh` and none runs at the push boundary. Unit 1's §7 therefore claims
gate coverage from a leg that will be held, which is the same defect round 1 raised against unit 4.

The obvious objection does not rescue it. Yes, `AGENTS.md` says a DoD for KIT work owes
`GATE_FULL=1 GATE_SELFTESTS=1`, and every unit here is kit work. Round 1's M2 named that fact itself
and still required the disclosure, because §7 is where a builder reads their bar. This is the
instance-not-class fold shape — fix the file the finding pointed at, leave the class standing — which
`AGENTS.md` §7 names outright.

**Fix.** Copy unit 4's disclosure into units 1, 2, 3 and 5 §7, corrected per M2 below, and state in
each unit's DoD which command is owed: `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.

**Left-shift.** The check round 1 already proposed, which this pass endorses more strongly now that it
has two instances: validate a spec's §7 leg names against `tools/gate-legs.json` — every named leg
exists, every named leg's guard intersects the unit's declared write set, and every named leg carrying
`subject: kit` or `chunk: selftests` is accompanied by the hold disclosure. All three arms read one
manifest that `AGENTS.md` already points every reader at, and the third arm is what makes the fix a
class fix rather than four edits.

---

### M2 — medium — unit 4 §7, the fold-added paragraph

**The defect.** The one paragraph the fold added to unit 4's §7 closes: "so a builder running
`bash tools/run-gates/run-gates.sh` sees them silently held." The substance is right and the adverb is
false at HEAD.

`tools/run-gates/run-gates.sh:1175` prints, per held leg:

```
GATE held  <name>  (self-test, set GATE_SELFTESTS=1 to run)
```

`run-gates.sh:1258` carries a per-chunk tally with `held` as its own column, and the comment above it
at `:1256` explains that a held leg and a guard-skip are printed differently because "the two have
different remedies". `run-gates.sh:1347` adds a summary note naming the held count. And `:1383` goes
further than reporting: a run where every leg is a held kit self-test REFUSES rather than reporting
green.

So the runner names held legs deliberately and by recorded decision. The paragraph accuses it of the
announce-your-skip defect it was explicitly built to avoid — and does so inside a build whose unit 2
exists to fix that same class elsewhere.

It is one word, but it is a false claim about the toolchain in a document that will be read as a
record, and the harm is not hypothetical: a builder who believes it may add redundant hold-reporting,
or discount the held rows the runner already prints as untrustworthy.

**Fix.** "Both kit-subject legs are HELD on a plain bar and NAMED as held by the runner;
`GATE_SELFTESTS=1` runs them, and a DoD for kit work owes `GATE_FULL=1 GATE_SELFTESTS=1`." Use that
wording for the four copies M1 asks for, so the correction propagates rather than the error.

**Left-shift.** Checklist, not gate — "silently" is not a greppable defect in general. The entry is
narrow and this build earned it: a spec asserting that a shipped tool FAILS to report something must
cite the line where it does not, the same way every finding in this report had to. Round 1 scored 0.22
and round 2 scored 0.34 on exactly that constraint; applying it to spec prose is the same lever.

---

## What this pass did not cover

- The fold's answer to round 1's B2 — S6 landing the scoring instrument — was confirmed to exist as a
  scope item and was not itself audited. Whether the AST resolver and harness S6 describes can be
  built as specced is a question for the build pass, not this one.
- The dossier's measured figures were again taken as reported, not re-derived. Nothing here depends on
  them.
- Ten of the thirteen round-1 findings had folds that no lens produced a survivable complaint about.
  That is not the same as ten independently verified folds, and this report does not claim it is.
- The relations answer was not re-litigated, for the second round running. The README rules it closed
  on `AGENTS.md` §12 grounds and this pass took that as given.
- Unit 2's rev-2 was the lightest fold in the set at 20 changed lines and produced no confirmed
  finding. It was read, but a quiet unit is weaker evidence than a noisy one.
- The specs were audited against the tree at `c8f026ae`. No code exists yet, so nothing here was run
  against a build.
